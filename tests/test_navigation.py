"""Static navigation packaging checks, not AI behavior evaluations."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class NavigationTests(unittest.TestCase):
 def test_installed_map_is_compact(self):
  s=(ROOT/'skills/minecraft-development/AI-INDEX.md').read_text()
  self.assertLess(len(s.split()),850)
  for name in ('Anti-cheat','Mod lists','Token','Companion','Verification'):
   self.assertIn(name,s)
 def test_all_routers_link_map(self):
  for p in (ROOT/'skills').glob('*/SKILL.md'):
   self.assertIn('AI-INDEX.md',p.read_text())
 def test_package_entry_routes(self):
  s=(ROOT/'AI-START-HERE.md').read_text()
  self.assertIn('skills/minecraft-development/AI-INDEX.md',s)
  self.assertIn('INSTALL.md',s)
  self.assertIn('AI-START-HERE.md',(ROOT/'README.md').read_text())
