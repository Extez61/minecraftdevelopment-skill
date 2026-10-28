#!/usr/bin/env python3
"""Read-only, bounded discovery. Never execute builds or print configuration values."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path

SKIP = {'.git', '.gradle', 'build', 'target', 'node_modules', '.idea', '.vscode',
        '.claude', 'run', 'runs', 'world', 'world_nether', 'world_the_end', 'logs',
        'crash-reports', '__pycache__', '.venv', 'venv', 'dist', 'out'}
BUILDS = {'build.gradle', 'build.gradle.kts', 'settings.gradle', 'settings.gradle.kts',
          'gradle.properties', 'libs.versions.toml', 'pom.xml', 'gradle-wrapper.properties'}
DESCRIPTORS = {'fabric.mod.json', 'plugin.yml', 'paper-plugin.yml', 'neoforge.mods.toml', 'mods.toml'}
MAX_BYTES = 131072

def inspect_project(root: Path, max_files: int = 5000) -> dict:
    root = root.expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Project root must be a directory')
    if max_files < 1:
        raise ValueError('max_files must be positive')
    files_seen = 0
    truncated = False
    candidates: list[Path] = []
    source_counts = {'java': 0, 'kotlin': 0}
    for base, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP and not d.startswith('.')
                         and not (Path(base) / d).is_symlink())
        for name in sorted(files):
            path = Path(base) / name
            if path.is_symlink():
                continue
            files_seen += 1
            if files_seen > max_files:
                truncated = True
                break
            if name in BUILDS | DESCRIPTORS:
                candidates.append(path)
            if path.suffix == '.java':
                source_counts['java'] += 1
            if path.suffix == '.kt':
                source_counts['kotlin'] += 1
        if truncated:
            break
    metadata = []
    skipped_large = []
    unreadable = []
    signals = set()
    for path in candidates:
        rel = path.relative_to(root).as_posix()
        try:
            if path.stat().st_size > MAX_BYTES:
                skipped_large.append(rel)
                continue
            with path.open('rb') as handle:
                raw = handle.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                skipped_large.append(rel)
                continue
            text = raw.decode('utf-8', errors='replace').lower()
            metadata.append(rel)
            if path.name == 'fabric.mod.json' or 'fabric-loom' in text or 'fabric-api' in text:
                signals.add('fabric')
            if path.name == 'paper-plugin.yml' or 'io.papermc.paper' in text or 'paper-api' in text:
                signals.add('paper')
            if path.name == 'plugin.yml' or 'spigot-api' in text or 'org.bukkit' in text:
                signals.add('bukkit-style-plugin')
            if path.name == 'neoforge.mods.toml' or 'net.neoforged' in text:
                signals.add('neoforge')
            if path.name == 'mods.toml' or 'net.minecraftforge' in text:
                signals.add('legacy-forge-or-shared-metadata:inspect-manually')
        except OSError:
            unreadable.append(rel)
    return {
        'read_only': True,
        'project_name': root.name,
        'files_examined': min(files_seen, max_files),
        'scan_truncated': truncated,
        'source_file_counts': source_counts,
        'metadata_files': sorted(metadata),
        'platform_signals_not_verified_targets': sorted(signals),
        'oversized_metadata_skipped': sorted(skipped_large),
        'unreadable_metadata': sorted(unreadable),
        'wrapper_files_present': {name: (root/name).is_file() and not (root/name).is_symlink()
                                  for name in ('gradlew', 'gradlew.bat')},
        'next_steps': ['Inspect exact versions, source sets, Java/Kotlin targets and mappings manually.',
                       'Read the matching platform skill; multiple signals do not prove multiple deployable targets.',
                       'No builds, network requests, dependency downloads or runtime tests were executed.']
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project_root', type=Path)
    parser.add_argument('--max-files', type=int, default=5000)
    args = parser.parse_args()
    try:
        result = inspect_project(args.project_root, args.max_files)
    except (ValueError, OSError) as exc:
        parser.exit(2, 'Inspection failed: ' + str(exc) + '\n')
    print(json.dumps(result, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
