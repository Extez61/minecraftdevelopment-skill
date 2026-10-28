#!/usr/bin/env python3
"""Read-only release hygiene and optional exact manifest verification (Python 3.10+)."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

SKIP_DIRS={'.git','__pycache__','.pytest_cache','.venv','venv'}
EXPECTED={'minecraft-development','minecraft-fabric','minecraft-paper','minecraft-bukkit','minecraft-neoforge','minecraft-server-operations'}
REQUIRED={'.gitignore','.gitattributes','.github/workflows/validate.yml','.claude-plugin/plugin.json',
          '.claude-plugin/marketplace.json','README.md','INSTALL.md','CONTRIBUTING.md','SECURITY.md',
          'docs/PUBLISHING.md','tools/validate_pack.py','tools/release_check.py'}

def scan(root: Path, verify_manifest: bool=False) -> dict:
    root=root.resolve()
    errors=[]
    files={}
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):continue
        if p.is_symlink():
            errors.append(f'Symlink: {rel.as_posix()}');continue
        if not p.is_file():continue
        name=rel.as_posix()
        if p.suffix in {'.pyc','.class','.zip','.log'}:
            errors.append(f'Generated artifact: {name}')
        data=p.read_bytes();files[name]=data
        if not data.strip():errors.append(f'Empty file: {name}')
        try:text=data.decode('utf-8')
        except UnicodeDecodeError:
            errors.append(f'Unexpected non-UTF-8 file: {name}');continue
        if '\ufffd' in text:errors.append(f'Replacement character: {name}')
        if p.suffix=='.py':
            try:compile(text,name,'exec')
            except SyntaxError:errors.append(f'Python syntax error: {name}')
        if p.suffix=='.json':
            try:json.loads(text)
            except (ValueError,RecursionError):errors.append(f'Invalid JSON: {name}')
        if p.suffix=='.md':
            opened=None
            for line in text.splitlines():
                match=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
                if not match:continue
                fence,tail=match.groups()
                if opened is None:opened=(fence[0],len(fence))
                elif fence[0]==opened[0] and len(fence)>=opened[1] and not tail.strip():opened=None
            if opened:errors.append(f'Unclosed code fence: {name}')
    for name in sorted(REQUIRED-set(files)):errors.append(f'Missing release file: {name}')
    actual={p.parent.name for p in (root/'skills').glob('*/SKILL.md')}
    if actual!=EXPECTED:errors.append('Skill set mismatch')
    try:
        plugin=json.loads(files['.claude-plugin/plugin.json'])
        market=json.loads(files['.claude-plugin/marketplace.json'])
        if plugin['name']!='minecraft-development' or plugin['author']['name']!='extez061':
            errors.append('Plugin identity mismatch')
        if market['name']!='minecraftdevelopment-skill' or market['owner']['name']!='extez061':
            errors.append('Marketplace identity mismatch')
        if len(market['plugins'])!=1 or market['plugins'][0]['name']!=plugin['name'] or market['plugins'][0]['source']!='./':
            errors.append('Marketplace source/name mismatch')
        if set(plugin)&{'hooks','mcpServers','agents','settings','workflows','experimental'}:
            errors.append('Unexpected executable/behavioral plugin component')
    except (KeyError,ValueError,TypeError,IndexError):errors.append('Invalid plugin/marketplace structure')
    if verify_manifest:
        try:
            manifest=json.loads(files['MANIFEST.json'])
            expected={}
            for item in manifest['files']:
                name=item['path'];path=PurePosixPath(name)
                if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name or name in expected:
                    errors.append('Unsafe/duplicate manifest path');continue
                expected[name]=item
            distribution=set(files)-{'MANIFEST.json'}
            if set(expected)!=distribution:errors.append('Manifest file-set mismatch')
            for name in sorted(set(expected)&distribution):
                if expected[name]['bytes']!=len(files[name]) or expected[name]['sha256']!=hashlib.sha256(files[name]).hexdigest():
                    errors.append(f'Manifest hash/size mismatch: {name}')
            if manifest['plugin_version']!=plugin['version']:errors.append('Manifest plugin-version mismatch')
            if set(manifest['skills'])!=EXPECTED:errors.append('Manifest skill-set mismatch')
        except (KeyError,ValueError,TypeError):errors.append('Invalid or missing manifest')
    return {'ok':not errors,'files_checked':len(files),'skill_count':len(actual),
            'manifest_verified':verify_manifest and not errors,'errors':errors}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--verify-manifest',action='store_true')
    a=p.parse_args();result=scan(a.root,a.verify_manifest)
    print(json.dumps(result,indent=2));return 0 if result['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
