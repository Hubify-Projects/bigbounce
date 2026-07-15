#!/usr/bin/env python3
"""Static policy tests for the independent P1B RunPod watchdog workflow."""

from pathlib import Path
import re
import unittest


WORKFLOW = (
    Path(__file__).resolve().parents[3]
    / ".github"
    / "workflows"
    / "p1b-runpod-watchdog.yml"
)


class WatchdogWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = WORKFLOW.read_text(encoding="utf-8")

    def test_has_scheduled_and_manual_triggers(self) -> None:
        self.assertIn("schedule:", self.text)
        self.assertIn("workflow_dispatch:", self.text)
        cron = re.search(r'cron: "([^"]+)"', self.text)
        self.assertIsNotNone(cron)
        minute = cron.group(1).split()[0]
        self.assertNotEqual(minute, "*/5")
        self.assertRegex(minute, r"^[1-9][0-9]?-[1-5][0-9]/5$")

    def test_is_singleton_with_minimal_permissions(self) -> None:
        self.assertIn("group: p1b-runpod-external-watchdog", self.text)
        self.assertIn("cancel-in-progress: false", self.text)
        self.assertRegex(self.text, r"permissions:\n  contents: read\n")

    def test_official_actions_are_immutable_and_python_is_311(self) -> None:
        self.assertRegex(self.text, r"actions/checkout@[0-9a-f]{40}")
        self.assertRegex(self.text, r"actions/setup-python@[0-9a-f]{40}")
        self.assertIn('python-version: "3.11"', self.text)
        self.assertIn("filter: blob:none", self.text)
        self.assertIn("sparse-checkout: reproducibility/p1_namaster_500mc/scripts", self.text)

    def test_configuration_fails_closed(self) -> None:
        self.assertIn("if: ${{ vars.P1B_RUNPOD_INTENT != '' }}", self.text)
        self.assertIn("secrets.RUNPOD_API_KEY", self.text)
        self.assertIn("vars.P1B_RUNPOD_INTENT", self.text)
        self.assertIn('[[ -z "${RUNPOD_API_KEY}" ]]', self.text)
        self.assertIn('[[ -z "${P1B_RUNPOD_INTENT}" ]]', self.text)
        self.assertIn("exit 1", self.text)

    def test_intent_is_written_privately_without_printing(self) -> None:
        self.assertIn(
            "printf '%s' \"${P1B_RUNPOD_INTENT}\" > "
            '"${RUNNER_TEMP}/p1b-runpod-intent.json"',
            self.text,
        )
        self.assertNotIn("echo \"${P1B_RUNPOD_INTENT}", self.text)
        self.assertIn('chmod 600 "${RUNNER_TEMP}/p1b-runpod-intent.json"', self.text)

    def test_invokes_external_watchdog_with_temp_intent(self) -> None:
        self.assertIn(
            "python reproducibility/p1_namaster_500mc/scripts/"
            "runpod_external_watchdog.py",
            self.text,
        )
        self.assertIn(
            '--intent "${RUNNER_TEMP}/p1b-runpod-intent.json"', self.text
        )


if __name__ == "__main__":
    unittest.main()
