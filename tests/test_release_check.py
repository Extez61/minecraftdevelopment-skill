"""Offline release hygiene checks; no GitHub or client integration."""
from pathlib import Path
import importlib.util
import json
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('release_check',ROOT/'tools/release_check.py')
release=importlib.util.module_from_spec(spec);spec.loader.exec_module(release)
class ReleaseTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.r=Path(self.t.name)/'repo'
  shutil.copytree(ROOT,self.r,ignore=shutil.ignore_patterns('__pycache__','.git','MANIFEST.json'))
 def tearDown(self):self.t.cleanup()
 def test_current_structure(self):
  result=release.scan(self.r);self.assertTrue(result['ok'],result['errors'])
 def test_empty_file_rejected(self):
  (self.r/'empty.md').write_text('  \n')
  self.assertIn('Empty file: empty.md',release.scan(self.r)['errors'])
 def test_invalid_fence_and_python_rejected(self):
  (self.r/'broken.md').write_text('```java\nmissing close\n')
  (self.r/'broken.py').write_text('def broken(:\n')
  e=release.scan(self.r)['errors']
  self.assertIn('Unclosed code fence: broken.md',e)
  self.assertIn('Python syntax error: broken.py',e)
 def test_manifest_missing_rejected(self):
  self.assertFalse(release.scan(self.r,True)['ok'])
 def test_manifest_hash_mismatch_rejected(self):
  files=[p for p in self.r.rglob('*') if p.is_file()]
  import hashlib
  m={'files':[{'path':p.relative_to(self.r).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
     'skills':sorted(release.EXPECTED),'plugin_version':json.loads((self.r/'.claude-plugin/plugin.json').read_text())['version']}
  (self.r/'MANIFEST.json').write_text(json.dumps(m))
  self.assertTrue(release.scan(self.r,True)['ok'])
  (self.r/'README.md').write_text('Changed\n')
  self.assertIn('Manifest hash/size mismatch: README.md',release.scan(self.r,True)['errors'])
 def test_private_access_is_documented(self):
  s=(self.r/'README.md').read_text()
  self.assertIn('Private repository',s)
  self.assertIn('No Python is required to install',s)
  s=(self.r/'docs/PUBLISHING.md').read_text()
  self.assertIn('git add .',s)
  self.assertIn('Do not force-push',s)
