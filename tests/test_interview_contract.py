"""Static prompt-contract checks, not a model-behavior evaluation.

Only read the two tracked Markdown files beside this test's parent directory.
No application imports, subprocesses, network, or persistent writes.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InterviewContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_popup_is_conditional(self):
        self.assertIn("When AskUserQuestion is available", self.skill)
        self.assertNotIn("Never pose questions as plain text", self.skill)

    def test_text_fallback_preserves_single_question(self):
        self.assertIn("If AskUserQuestion is unavailable", self.skill)
        self.assertIn("one plain-text question", self.skill)
        self.assertIn("Wait for the user's answer", self.skill)

    def test_unattended_run_stops_without_inventing_answers(self):
        self.assertIn("If no user reply channel is available", self.skill)
        self.assertIn("stop the interview", self.skill)
        self.assertIn("Do not invent answers", self.skill)

    def test_flow_does_not_reintroduce_unconditional_tool_call(self):
        self.assertNotIn("next question via AskUserQuestion", self.skill)
        self.assertIn("question method above", self.skill)

    def test_readme_explains_limits(self):
        self.assertIn("plain-text question", self.readme)
        self.assertIn("unresolved decisions", self.readme)
        self.assertIn("not model-behavior", self.readme)


if __name__ == "__main__":
    unittest.main()
