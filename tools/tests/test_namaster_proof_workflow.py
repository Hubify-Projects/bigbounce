import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github" / "workflows" / "namaster-proof.yml"


class NamasterProofWorkflowTests(unittest.TestCase):
    def test_multiline_posix_example_selects_bash_on_every_runner(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        step = text.split("- name: Run independent example", 1)[1].split(
            "- name: Build wheel", 1
        )[0]
        self.assertIn("shell: bash", step)
        self.assertIn("\\\n", step)
        self.assertIn("${RUNNER_TEMP}", step)


if __name__ == "__main__":
    unittest.main()
