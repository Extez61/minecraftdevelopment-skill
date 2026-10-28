#!/usr/bin/env python3
"""Refresh release hashes from Git's staged files, not Windows checkout line endings.

Review and stage intended changes with git add first. This tool only writes
MANIFEST.json; it never stages, commits, fetches, pushes or edits other files.
"""
from pathlib import Path
import hashlib
import json
import subprocess


def refresh(root: Path) -> int:
    def git(*args: str) -> bytes:
        return subprocess.check_output(['git', *args], cwd=root)

    if git('diff', '--name-only', '--diff-filter=U').strip():
        raise RuntimeError('Resolve merge conflicts before updating the manifest.')
    names = sorted(set(git('ls-files', '--cached', '-z').decode('utf-8').split('\0')) - {'', 'MANIFEST.json'})
    path = root / 'MANIFEST.json'
    manifest = json.loads(path.read_text(encoding='utf-8'))
    records = []
    for name in names:
        data = git('show', ':' + name)
        records.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    manifest['files'] = records
    manifest['license_selected'] = 'LICENSE' in names
    path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    print(f'Updated MANIFEST.json for {len(records)} staged files. Review, stage and commit it next.')
    return len(records)


if __name__ == '__main__':
    refresh(Path(__file__).resolve().parents[1])
