#!/usr/bin/env python3

import importlib.util
import os
import sys
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().with_name("prepare_runpod_production.py")
SPEC = importlib.util.spec_from_file_location("prepare_runpod_production", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class RunPodProductionContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = __import__("json").loads(MODULE.DEFAULT_CONTRACT.read_text())
        cls.head = MODULE.git("rev-parse", "HEAD")

    def test_preflight_is_manifest_only_and_has_nine_jobs(self):
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "test-only"}):
            result = MODULE.preflight(self.contract, self.head)
        self.assertFalse(result["provider_mutation_performed"])
        self.assertTrue(result["runpod_api_key_present"])
        self.assertEqual(len(result["robustness_commands"]), 8)
        self.assertIn("NAMASTER_NREAL=500", result["canonical_command"])
        self.assertNotIn("test-only", repr(result))

    def test_missing_key_fails_closed(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "RUNPOD_API_KEY is required"):
                MODULE.preflight(self.contract, self.head)

    def test_commit_mismatch_fails_closed(self):
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "test-only"}):
            with self.assertRaisesRegex(ValueError, "exactly equal current HEAD"):
                MODULE.preflight(self.contract, "0" * 40)

    def test_launch_confirmation_is_constant_and_non_secret(self):
        self.assertEqual(MODULE.CONFIRMATION, "LAUNCH-P1B-500MC")
        self.assertNotIn("RUNPOD_API_KEY", MODULE.CONFIRMATION)

    def test_launch_without_budget_fails_closed(self):
        argv = [
            str(SCRIPT), "--expected-commit", self.head, "--launch",
            "--confirm", MODULE.CONFIRMATION,
        ]
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "test-only"}), mock.patch.object(
            sys, "argv", argv
        ):
            with self.assertRaisesRegex(ValueError, "positive --max-budget-usd"):
                MODULE.main()

    def test_fully_confirmed_launch_still_performs_no_mutation(self):
        argv = [
            str(SCRIPT), "--expected-commit", self.head, "--launch",
            "--max-budget-usd", "25", "--confirm", MODULE.CONFIRMATION,
        ]
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "test-only"}), mock.patch.object(
            sys, "argv", argv
        ):
            with self.assertRaisesRegex(ValueError, "mutation is intentionally not implemented"):
                MODULE.main()


if __name__ == "__main__":
    unittest.main()
