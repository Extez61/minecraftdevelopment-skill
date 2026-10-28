"""Static Git/native installation contract; no remote clone or live plugin test."""
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
class GitInstallationTests(unittest.TestCase):
 def test_python_installers_absent(self):
  for name in ('install_skills.py','install_from_link.py','setup_cli.py'):
   self.assertFalse((R/'tools'/name).exists())
 def test_no_python_commands_in_install_guides(self):
  for name in ('README.md','INSTALL.md','docs/OTHER-TOOLS.md'):
   s=(R/name).read_text()
   self.assertNotIn('python tools/',s)
   self.assertNotIn('--apply',s)
   self.assertNotIn('--backup-existing',s)
 def test_native_plugin_and_copy_paths(self):
  s=(R/'README.md').read_text()
  for text in ('git clone https://github.com/Extez61/minecraftdevelopment-skill.git','claude plugin marketplace add .','/plugin install minecraft-development@extez061-skills','.opencode/skills/','all six directories'):
   self.assertIn(text,s)
 def test_optional_analysis_retained(self):
  for name in ('inspect_project.py','inspect_mods.py'):
   self.assertTrue((R/'skills/minecraft-development/scripts'/name).is_file())
  self.assertIn('Optional read-only inspection tools',(R/'README.md').read_text())
