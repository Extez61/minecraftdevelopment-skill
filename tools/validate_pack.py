#!/usr/bin/env python3
"""Validate this suite's conservative frontmatter and local Markdown references."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

EXPECTED = {'minecraft-development', 'minecraft-fabric', 'minecraft-paper',
            'minecraft-bukkit', 'minecraft-neoforge', 'minecraft-server-operations'}

def validate(root: Path) -> dict:
    root = root.resolve()
    errors: list[str] = []
    skills = sorted((root/'skills').glob('*/SKILL.md'))
    names = set()
    for path in skills:
        text = path.read_text(encoding='utf-8')
        rel = path.relative_to(root).as_posix()
        if not text.startswith('---\n'):
            errors.append(f'{rel}: frontmatter must start on the first line')
            continue
        chunks = text.split('---\n', 2)
        if len(chunks) != 3:
            errors.append(f'{rel}: unterminated frontmatter')
            continue
        fields = {}
        for line in chunks[1].splitlines():
            if not line.strip():
                continue
            if ':' not in line:
                errors.append(f'{rel}: unsupported frontmatter line')
                continue
            k, value = line.split(':', 1)
            fields[k] = value.strip()
        name = fields.get('name', '')
        if not re.fullmatch(r'[a-z0-9-]{1,64}', name) or name != path.parent.name:
            errors.append(f'{rel}: name must match folder and conservative skill-name syntax')
        if name in names:
            errors.append(f'{rel}: duplicate skill name')
        names.add(name)
        try:
            desc = json.loads(fields.get('description', 'null'))
            if not isinstance(desc, str) or not desc.strip() or len(desc) > 1536:
                raise ValueError('description missing or too long')
        except (ValueError, json.JSONDecodeError):
            errors.append(f'{rel}: expected a nonempty JSON-quoted YAML description under 1537 characters')
        if len(text.splitlines()) >= 500:
            errors.append(f'{rel}: move detail out of SKILL.md (500-line limit)')
        if set(fields) != {'name', 'description'}:
            errors.append(f'{rel}: unexpected frontmatter fields; review permissions/behavior manually')
    if names != EXPECTED:
        errors.append('Missing/unexpected skills: ' + repr(names ^ EXPECTED))
    md_files = list(root.rglob('*.md'))
    checked_links = 0
    for path in md_files:
        if path.is_symlink():
            errors.append(f'Symlink not allowed: {path.relative_to(root)}')
            continue
        text = path.read_text(encoding='utf-8')
        if '\ufffd' in text:
            errors.append(f'{path.relative_to(root)}: replacement character found')
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\s]+)\)', text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            checked_links += 1
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(f'{path.relative_to(root)}: link escapes package: {target}')
                continue
            if not resolved.exists():
                errors.append(f'{path.relative_to(root)}: broken link: {target}')
    required = ['skills/minecraft-server-operations/SKILL.md',
                'skills/minecraft-server-operations/references/sources.md', 'README.md', 'RESEARCH.md', 'QA.md',
                'evals/scenarios.md', 'templates/CLAUDE.minecraft.md',
                'skills/minecraft-development/scripts/inspect_project.py',
                'INSTALL.md',
                'skills/minecraft-development/scripts/inspect_mods.py',
                'skills/minecraft-development/references/api-catalog.md',
                'skills/minecraft-development/references/modlists-compatibility.md']
    for item in required:
        if not (root/item).is_file():
            errors.append('Missing required file: '+item)
    return {'ok': not errors, 'skill_count': len(skills), 'markdown_count': len(md_files),
            'markdown_word_count': sum(len(p.read_text().split()) for p in md_files if not p.is_symlink()),
            'local_markdown_links_checked': checked_links, 'errors': errors}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root)
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
