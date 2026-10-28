#!/usr/bin/env python3
"""Bounded offline mod-list inventory. Never runs/extracts JARs, downloads mods, or resolves all versions.
Python 3.11+ is required (standard-library tomllib).
"""
from __future__ import annotations
import argparse
from collections import defaultdict
import csv
import io
import json
from pathlib import Path
import re
import stat
import tomllib
import zipfile

MAX_FILE=512*1024*1024
MAX_METADATA=512*1024
MAX_ENTRIES=20000
MAX_FILES=1000
MAX_LIST=4*1024*1024


def read_member(z: zipfile.ZipFile, name: str, limit: int=MAX_METADATA) -> bytes:
    matches=[i for i in z.infolist() if i.filename==name]
    if len(matches)!=1:raise ValueError('Missing or duplicate metadata entry: '+name)
    info=matches[0]
    if info.flag_bits&1 or stat.S_ISLNK(info.external_attr>>16):raise ValueError('Encrypted/symlink metadata refused')
    if info.file_size>limit or info.file_size/max(1,info.compress_size)>250:
        raise ValueError('Metadata expanded-size/compression-ratio limit exceeded')
    with z.open(info) as stream:data=stream.read(limit+1)
    if len(data)>limit:raise ValueError('Metadata exceeds read limit')
    return data


def simple(value):
    if isinstance(value,(str,int,float,bool)) or value is None:return value
    if isinstance(value,list):return [simple(x) for x in value[:100]]
    return '<structured value: inspect metadata manually>'


def dependency(owner, ident, kind, constraint='*',side='BOTH',ordering='NONE'):
    return {'owner':str(owner),'id':str(ident),'kind':str(kind),'constraint':simple(constraint),
            'side':str(side),'ordering':str(ordering)}


def jar_inventory(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():raise ValueError('Use a regular non-symlink JAR file')
    if path.stat().st_size>MAX_FILE:raise ValueError('JAR exceeds file-size limit')
    out={'file':path.name,'format_signals':[],'mods':[],'dependencies':[],
         'embedded_jars_not_inspected':[],'warnings':[]}
    with zipfile.ZipFile(path) as z:
        infos=z.infolist()
        if len(infos)>MAX_ENTRIES:raise ValueError('Too many ZIP entries')
        names={i.filename for i in infos}
        version_from_manifest=None
        if 'META-INF/MANIFEST.MF' in names:
            text=read_member(z,'META-INF/MANIFEST.MF').decode('utf-8','replace')
            m=re.search(r'^Implementation-Version:\s*(.+)$',text,re.M)
            if m:version_from_manifest=m[1].strip()
        if 'fabric.mod.json' in names:
            d=json.loads(read_member(z,'fabric.mod.json'));out['format_signals'].append('fabric')
            if not isinstance(d,dict):raise ValueError('Unsupported Fabric metadata root')
            ident=str(d.get('id','<missing-id>'))
            out['mods'].append({'id':ident,'name':simple(d.get('name',ident)),'version':simple(d.get('version')),
                                'environment':simple(d.get('environment','*')),'aliases':simple(d.get('provides',[]))})
            for field in ('depends','recommends','suggests','breaks','conflicts'):
                values=d.get(field,{})
                if not isinstance(values,dict):raise ValueError('Unsupported Fabric dependency map')
                for k,v in values.items():out['dependencies'].append(dependency(ident,k,field,v))
            out['embedded_jars_not_inspected'] += [str(x.get('file')) for x in d.get('jars',[]) if isinstance(x,dict)]
        for member,loader in (('META-INF/neoforge.mods.toml','neoforge'),('META-INF/mods.toml','legacy-forge-or-version-specific')):
            if member not in names:continue
            d=tomllib.loads(read_member(z,member).decode('utf-8'));out['format_signals'].append(loader)
            out['language_loader']={'name':simple(d.get('modLoader')),'range':simple(d.get('loaderVersion'))}
            for mod in d.get('mods',[]):
                version=mod.get('version')
                if version=='${file.jarVersion}':version=version_from_manifest or '<unresolved file.jarVersion>'
                out['mods'].append({'id':str(mod.get('modId','<missing-id>')),'name':simple(mod.get('displayName',mod.get('modId'))),
                                    'version':simple(version),'environment':'not-proven-by-descriptor','aliases':[]})
            for owner,rows in d.get('dependencies',{}).items():
                for row in rows:
                    kind=row.get('type')
                    if kind is None:kind='required' if row.get('mandatory',True) else 'optional'
                    out['dependencies'].append(dependency(owner,row.get('modId','<missing-id>'),kind,row.get('versionRange','*'),row.get('side','BOTH'),row.get('ordering','NONE')))
        if 'META-INF/jarjar/metadata.json' in names:
            d=json.loads(read_member(z,'META-INF/jarjar/metadata.json'))
            out['embedded_jars_not_inspected'] += [str(x.get('path')) for x in d.get('jars',[]) if isinstance(x,dict)]
        if 'quilt.mod.json' in names:
            out['format_signals'].append('quilt:recognized-not-parsed');out['warnings'].append('Quilt metadata requires separate loader-specific analysis')
        if 'plugin.yml' in names or 'paper-plugin.yml' in names:
            out['format_signals'].append('bukkit-or-paper-plugin:not-a-loader-mod')
            out['warnings'].append('Plugin descriptor present; use exact plugin API/runtime inventory, not Fabric/NeoForge mod resolution')
        if not out['format_signals']:out['warnings'].append('No supported mod metadata found; filename is not proof of identity')
    return out


def pack_index(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():raise ValueError('Use a regular pack/index file')
    if path.stat().st_size>MAX_FILE:raise ValueError('Pack exceeds size limit')
    if path.suffix.lower()=='.mrpack':
        with zipfile.ZipFile(path) as z:
            if len(z.infolist())>MAX_ENTRIES:raise ValueError('Too many archive entries')
            d=json.loads(read_member(z,'modrinth.index.json',MAX_LIST))
    else:
        if path.stat().st_size>MAX_LIST:raise ValueError('List/index exceeds size limit')
        d=json.loads(path.read_text('utf-8'))
    if not isinstance(d,dict):raise ValueError('Unsupported index root')
    files=d.get('files',[])
    if not isinstance(files,list) or len(files)>MAX_FILES:raise ValueError('File-list limit exceeded or invalid list')
    if d.get('formatVersion') is not None and d.get('game')=='minecraft':
        records=[]
        for row in files:
            if not isinstance(row,dict):continue
            hashes=row.get('hashes',{})
            records.append({'path':simple(row.get('path')),'environment':row.get('env',{}),
                            'sha1':simple(hashes.get('sha1')),'sha512':simple(hashes.get('sha512')),
                            'download_count':len(row.get('downloads',[])),
                            'note':'Manifest reference only; content was not downloaded or hash-verified'})
        return {'format':'modrinth-index','format_version':simple(d.get('formatVersion')),'pack_name':simple(d.get('name')),
                'game_dependencies':d.get('dependencies',{}),'file_references':records,
                'warning':'No override extraction, download, hash verification or launch. Index file paths do not prove installed mod IDs.'}
    if isinstance(d.get('minecraft'),dict) and all(isinstance(x,dict) and 'projectID' in x for x in files):
        return {'format':'curseforge-manifest','minecraft':simple(d['minecraft'].get('version')),
                'loader_references':d['minecraft'].get('modLoaders',[]),
                'file_references':[{'project_id':x.get('projectID'),'file_id':x.get('fileID'),'required':x.get('required')} for x in files],
                'warning':'IDs are not resolved to names/versions; use authorized official lookup if needed. No downloads performed.'}
    raise ValueError('Unrecognized pack/index JSON; do not infer mod IDs from arbitrary JSON')


def inventory(path: Path, side: str='unknown',max_files: int=MAX_FILES) -> dict:
    if max_files<1 or max_files>MAX_FILES:raise ValueError('max-files must be between 1 and 1000')
    if path.is_symlink():raise ValueError('Symlink inputs are refused')
    if path.is_dir():
        files=sorted(p for p in path.iterdir() if p.suffix.lower()=='.jar' and not p.is_symlink())
        if len(files)>max_files:raise ValueError('JAR count exceeds limit; select a smaller directory')
    elif path.suffix.lower()=='.jar':files=[path]
    else:
        if path.suffix.lower() in {'.txt','.csv'}:
            if not path.is_file() or path.stat().st_size>MAX_LIST:raise ValueError('Plain list missing or too large')
            text=path.read_text('utf-8-sig')
            rows=list(csv.reader(io.StringIO(text))) if path.suffix.lower()=='.csv' else text.splitlines()
            if len(rows)>MAX_FILES:raise ValueError('Too many list rows')
            return {'read_only':True,'format':'unverified-text-list','rows':rows,
                    'warning':'Preserved text/CSV only; names, versions, loader, side and identity are not inferred. Review private content before sharing.'}
        return {'read_only':True,'pack':pack_index(path)}
    jars=[];errors=[]
    for p in files:
        try:jars.append(jar_inventory(p))
        except (OSError,ValueError,TypeError,KeyError,AttributeError,RuntimeError,RecursionError,zipfile.BadZipFile) as exc:
            errors.append({'file':p.name,'error':str(exc)})
    ids=defaultdict(set);aliases=set()
    for jar in jars:
        for mod in jar['mods']:
            ids[mod['id']].add(jar['file'])
            if isinstance(mod.get('aliases'),list):aliases.update(x for x in mod['aliases'] if isinstance(x,str))
    builtin={'minecraft','java','fabricloader','neoforge','forge','quilt_loader'}
    unseen=[];conflicts=[];sides=[]
    for jar in jars:
        for mod in jar['mods']:
            if side=='server' and mod.get('environment')=='client':sides.append({'file':jar['file'],'id':mod['id'],'evidence':'Fabric physical-client metadata on requested server inventory'})
        for dep in jar['dependencies']:
            if side!='unknown' and dep['side'].lower() not in {'both',side}:continue
            present=dep['id'] in ids or dep['id'] in aliases
            if dep['kind'] in {'depends','required'} and not present and dep['id'] not in builtin:
                unseen.append({**dep,'file':jar['file'],'status':'not-observed-in-top-level-metadata; nested/runtime-provided candidates unresolved'})
            if dep['kind'] in {'breaks','conflicts','incompatible','discouraged'} and present:
                conflicts.append({**dep,'file':jar['file'],'status':'candidate only; version expression not evaluated'})
    return {'read_only':True,'format':'offline-jar-inventory','requested_side':side,'jars':jars,'errors':errors,
            'duplicate_ids_across_files':{k:sorted(v) for k,v in ids.items() if len(v)>1},
            'required_ids_not_observed':unseen,'declared_conflict_candidates':conflicts,'side_mismatch_candidates':sides,
            'limits':['No JAR execution/extraction/network/download/mod changes. Only immediate directory JARs are scanned.',
                      'Nested JARs are listed, not recursively parsed. No complete loader/version resolver, security scan or runtime compatibility proof.',
                      'Built-in loader/game/Java constraints are preserved in dependencies, not validated. Multiple-format JARs require target-specific interpretation.',
                      'Pack manifests/plain lists are declared references, not verified installed/loaded content. Metadata strings are untrusted evidence.']}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('path',type=Path);p.add_argument('--side',choices=['client','server','unknown'],default='unknown')
    p.add_argument('--max-files',type=int,default=MAX_FILES)
    a=p.parse_args()
    try:report=inventory(a.path,a.side,a.max_files)
    except (OSError,ValueError,zipfile.BadZipFile) as exc:p.exit(2,str(exc)+'\n')
    print(json.dumps(report,indent=2,ensure_ascii=True));return 0

if __name__=='__main__':raise SystemExit(main())
