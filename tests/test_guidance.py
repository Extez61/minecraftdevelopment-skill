"""Static packaging/guardrail checks; not runtime anti-cheat or model evaluations."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'skills/minecraft-development/references'
class GuidanceTests(unittest.TestCase):
    def test_on_demand_guides_exist(self):
        for name in ('token-efficiency.md','companion-skills.md','anticheat-development.md'):
            self.assertIn('extez061',(REF/name).read_text())
    def test_platforms_link_anticheat(self):
        for p in (ROOT/'skills').glob('*/SKILL.md'):
            self.assertIn('anticheat-development.md',p.read_text())
    def test_token_quality_guardrails(self):
        s=(REF/'token-efficiency.md').read_text()
        for phrase in ('No fixed savings percentage','Do not silently change model','exit status','full log','necessary integration'):
            self.assertIn(phrase,s)
    def test_optional_companion_boundaries(self):
        s=(REF/'companion-skills.md').read_text()
        for phrase in ('not bundled','No automatic installation','one primary workflow owner','user-invoked','not a passed end-to-end client test'):
            self.assertIn(phrase,s)
    def test_anticheat_safety_and_evidence(self):
        s=(REF/'anticheat-development.md').read_text()
        for phrase in ('Do not provide stealth bypasses','NOT evidence of 26.2 support','Preserve incoming cancellation state','Do not copy examples that cancel all flags','No generic exemption API signature','not proof','p95/p99'):
            self.assertIn(phrase,s)
    def test_core_stays_compact(self):
        s=(ROOT/'skills/minecraft-development/SKILL.md').read_text()
        self.assertLess(len(s.split()),2300)
        self.assertIn('Load this core once',s)
if __name__=='__main__':unittest.main()
