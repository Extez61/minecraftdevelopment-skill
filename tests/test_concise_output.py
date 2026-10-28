"""Static output-policy checks, not a behavioral model evaluation."""
from pathlib import Path
import unittest
R=Path(__file__).resolve().parents[1]
class ConciseOutputTests(unittest.TestCase):
 def test_core_default_and_exceptions(self):
  s=(R/'skills/minecraft-development/SKILL.md').read_text()
  for x in ('Keep user-facing output concise','one to three sentences','used X instead of Y','brevity must never hide it'):
   self.assertIn(x,s)
 def test_operator_guidance(self):
  s=(R/'skills/minecraft-server-operations/references/player-management.md').read_text()
  for x in ('OP / deop','op <player>','deop <player>','last recovery administrator','These are command templates','separate LuckPerms grants'):
   self.assertIn(x,s)
 def test_readme_short_reply_policy(self):
  s=(R/'README.md').read_text()
  self.assertIn('OP/deop',s)
  self.assertIn('short, practical replies',s)
