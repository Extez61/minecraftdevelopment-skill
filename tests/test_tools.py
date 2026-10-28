import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
inspector = load('inspector', ROOT/'skills/minecraft-development/scripts/inspect_project.py')
validator = load('validator', ROOT/'tools/validate_pack.py')

class InspectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()
    def put(self, name, text=''):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);return p
    def test_empty(self):
        r=inspector.inspect_project(self.root)
        self.assertEqual(r['platform_signals_not_verified_targets'], [])
        self.assertTrue(r['read_only'])
    def test_fabric_kotlin_no_secret_echo(self):
        self.put('src/main/resources/fabric.mod.json', '{"id":"demo"}')
        self.put('build.gradle.kts', 'plugins { id("fabric-loom") }; val secret = "DO_NOT_ECHO_123"')
        self.put('src/main/kotlin/Test.kt', 'class Test')
        r=inspector.inspect_project(self.root)
        self.assertIn('fabric', r['platform_signals_not_verified_targets'])
        self.assertEqual(r['source_file_counts']['kotlin'], 1)
        self.assertNotIn('DO_NOT_ECHO_123', json.dumps(r))
    def test_classic_descriptor_not_paper_proof(self):
        self.put('src/main/resources/plugin.yml', 'name: Demo')
        r=inspector.inspect_project(self.root)
        self.assertIn('bukkit-style-plugin',r['platform_signals_not_verified_targets'])
        self.assertNotIn('paper',r['platform_signals_not_verified_targets'])
    def test_multiple_signals(self):
        self.put('paper/build.gradle.kts','compileOnly("io.papermc.paper:paper-api:x")')
        self.put('neo/src/main/resources/META-INF/neoforge.mods.toml','')
        self.assertEqual(inspector.inspect_project(self.root)['platform_signals_not_verified_targets'],['neoforge','paper'])
    def test_skip_generated_and_secrets(self):
        self.put('build/fabric.mod.json','{}')
        self.put('world/src/Test.java','class Test {}')
        self.put('.env','SECRET=never_read')
        self.put('.git/config','secret')
        r=inspector.inspect_project(self.root)
        self.assertEqual(r['metadata_files'],[])
        self.assertEqual(r['source_file_counts']['java'],0)
    def test_large_metadata_bounded(self):
        self.put('gradle.properties','x'*(inspector.MAX_BYTES+1))
        self.assertEqual(inspector.inspect_project(self.root)['oversized_metadata_skipped'],['gradle.properties'])
    def test_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as other:
            p=Path(other);(p/'fabric.mod.json').write_text('{}')
            (self.root/'external').symlink_to(p,target_is_directory=True)
            (self.root/'plugin.yml').symlink_to(p/'fabric.mod.json')
            self.assertEqual(inspector.inspect_project(self.root)['platform_signals_not_verified_targets'],[])
    def test_scan_cap(self):
        for i in range(5):self.put(f'{i}.txt','x')
        r=inspector.inspect_project(self.root,2)
        self.assertTrue(r['scan_truncated']);self.assertEqual(r['files_examined'],2)
    def test_read_only(self):
        p=self.put('build.gradle','// example')
        before=p.read_bytes(),p.stat().st_mtime_ns
        inspector.inspect_project(self.root)
        self.assertEqual(before,(p.read_bytes(),p.stat().st_mtime_ns))
    def test_invalid_root_or_limit(self):
        with self.assertRaises(FileNotFoundError): inspector.inspect_project(self.root/'missing')
        with self.assertRaises(ValueError): inspector.inspect_project(self.root,0)

class ValidatorTests(unittest.TestCase):
    def test_pack_valid(self):
        r=validator.validate(ROOT)
        self.assertTrue(r['ok'],r['errors']);self.assertEqual(r['skill_count'],6)
    def clone(self, directory):
        root=Path(directory)/'pack'
        shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        return root
    def test_broken_link_caught(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.clone(d);(p/'broken.md').write_text('[oops](absent.md)')
            self.assertTrue(any('broken link' in x for x in validator.validate(p)['errors']))
    def test_invalid_frontmatter_caught(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.clone(d);f=p/'skills/minecraft-paper/SKILL.md';f.write_text('\n'+f.read_text())
            self.assertFalse(validator.validate(p)['ok'])
    def test_link_escape_caught(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.clone(d);(p/'bad.md').write_text('[bad](../../outside.md)')
            self.assertTrue(any('escapes package' in x for x in validator.validate(p)['errors']))
    def test_permission_field_caught(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.clone(d);f=p/'skills/minecraft-paper/SKILL.md'
            f.write_text(f.read_text().replace('name: minecraft-paper','allowed-tools: Bash(*)\nname: minecraft-paper'))
            self.assertFalse(validator.validate(p)['ok'])

if __name__=='__main__': unittest.main()
