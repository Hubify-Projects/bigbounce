#!/usr/bin/env python3
"""Mock-only tests for the deliberately destructive watchdog deletion drill."""

from __future__ import annotations

import datetime as dt
import json
import signal
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import runpod_watchdog_deletion_drill as drill


COMMIT = "a" * 40
IMAGE = "runpod/pytorch@sha256:" + "b" * 64
NOW = dt.datetime(2026, 7, 15, 12, tzinfo=dt.timezone.utc)


class Client:
    def __init__(self, pods=None):
        self.pods = [] if pods is None else pods
        self.created = []

    def list_pods(self):
        return self.pods

    def create_pod(self, payload):
        self.created.append(payload)
        return {"id": "pod-1", "name": payload["name"], "imageName": payload["imageName"],
                "gpuCount": 1, "gpuTypeId": payload["gpuTypeIds"][0],
                "costPerHr": 0.50, "status": "CREATED"}


class Variables:
    def __init__(self):
        self.intents = []

    def publish_and_verify(self, intent):
        self.intents.append(intent)

    @property
    def variable_path(self):
        return "/intent"

    def request(self, method, path):
        intent = dict(self.intents[-1])
        intent["active"] = False
        return {"name": drill.launcher.WATCHDOG_INTENT_VARIABLE,
                "value": json.dumps(intent, sort_keys=True, separators=(",", ":"))}


class DrillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.balance = self.root / "balance.json"
        self.balance.write_text(json.dumps({"source": "runpod-console", "amount_usd": 1,
                                            "observed_at": NOW.isoformat()}))
        self.contract = {"container": {"image": IMAGE}, "provider_mutation_ready": False}

    def tearDown(self):
        self.temp.cleanup()

    def run_drill(self, **overrides):
        values = dict(client=Client(), github_variables=Variables(), contract=self.contract,
                      expected_commit=COMMIT, balance_path=self.balance,
                      balance_max_age_minutes=15, max_hourly_rate=0.50,
                      max_total_budget=0.05, max_runtime_minutes=6,
                      gpu_type_id="NVIDIA RTX A4000", confirmation=drill.CONFIRMATION,
                      now_fn=lambda: NOW, kill_fn=mock.Mock())
        values.update(overrides)
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            with self.assertRaisesRegex(RuntimeError, "SIGKILL unexpectedly returned"):
                drill.crash_after_create(**values)
        return values

    def test_publishes_intent_before_create_and_kills_without_local_ledger(self):
        events = []

        class OrderedVariables(Variables):
            def publish_and_verify(self, intent):
                events.append("intent")
                super().publish_and_verify(intent)

        class OrderedClient(Client):
            def create_pod(self, payload):
                events.append("create")
                return super().create_pod(payload)

        killer = mock.Mock(side_effect=lambda pid, sig: events.append("kill"))
        values = self.run_drill(client=OrderedClient(), github_variables=OrderedVariables(),
                                kill_fn=killer)
        self.assertEqual(events, ["intent", "create", "kill"])
        killer.assert_called_once_with(mock.ANY, signal.SIGKILL)
        payload = values["client"].created[0]
        self.assertEqual(payload["name"], drill.launcher.pod_name(COMMIT))
        self.assertEqual(payload["gpuCount"], 1)
        self.assertNotIn("networkVolumeId", payload)
        self.assertEqual(payload["imageName"], IMAGE)
        self.assertIn("timeout --foreground", payload["dockerStartCmd"][0])
        self.assertIn("exec sleep 360", payload["dockerStartCmd"][0])

    def test_contract_need_not_be_enabled_and_no_matching_name_allowed(self):
        self.run_drill()
        existing = Client([{"name": drill.launcher.pod_name(COMMIT), "status": "RUNNING"}])
        variables = Variables()
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            with self.assertRaisesRegex(ValueError, "existing deterministic"):
                drill.crash_after_create(
                    client=existing, github_variables=variables, contract=self.contract,
                    expected_commit=COMMIT, balance_path=self.balance, balance_max_age_minutes=15,
                    max_hourly_rate=.5, max_total_budget=.05, max_runtime_minutes=6,
                    gpu_type_id="GPU", confirmation=drill.CONFIRMATION, now_fn=lambda: NOW,
                    kill_fn=mock.Mock())
        self.assertFalse(variables.intents)
        self.assertFalse(existing.created)

    def test_all_preconditions_fail_before_publish_or_create(self):
        cases = [
            {"confirmation": "wrong"}, {"max_hourly_rate": 0},
            {"max_total_budget": 0.101}, {"max_runtime_minutes": 11},
            {"max_runtime_minutes": 0}, {"gpu_type_id": ""},
            {"contract": {"container": {"image": "unpinned:latest"}}},
        ]
        for override in cases:
            with self.subTest(override=override):
                client, variables = Client(), Variables()
                values = dict(client=client, github_variables=variables, contract=self.contract,
                              expected_commit=COMMIT, balance_path=self.balance,
                              balance_max_age_minutes=15, max_hourly_rate=.5,
                              max_total_budget=.05, max_runtime_minutes=6, gpu_type_id="GPU",
                              confirmation=drill.CONFIRMATION, now_fn=lambda: NOW,
                              kill_fn=mock.Mock())
                values.update(override)
                with mock.patch.object(drill.prep, "git", return_value=COMMIT):
                    with self.assertRaises(ValueError):
                        drill.crash_after_create(**values)
                self.assertFalse(client.created)
                self.assertFalse(variables.intents)

    def test_rejects_bad_create_response_without_kill(self):
        client = Client()
        client.create_pod = mock.Mock(return_value={"id": "pod", "imageName": IMAGE,
                                                     "gpuCount": 2, "gpuTypeId": "GPU",
                                                     "costPerHr": .5, "status": "CREATED"})
        killer = mock.Mock()
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            with self.assertRaisesRegex(ValueError, "mismatch"):
                drill.crash_after_create(
                    client=client, github_variables=Variables(), contract=self.contract,
                    expected_commit=COMMIT, balance_path=self.balance, balance_max_age_minutes=15,
                    max_hourly_rate=.5, max_total_budget=.05, max_runtime_minutes=6,
                    gpu_type_id="GPU", confirmation=drill.CONFIRMATION, now_fn=lambda: NOW,
                    kill_fn=killer)
        killer.assert_not_called()

    def receipt(self, **changes):
        value = {"schema": drill.GITHUB_RECEIPT_SCHEMA, "run_id": 123,
                 "event_name": "schedule", "conclusion": "success", "git_commit": COMMIT,
                 "pod_name": drill.launcher.pod_name(COMMIT), "action": "delete_confirmed",
                 "deleted_pod_id": "pod-1",
                 "deadline": NOW.isoformat(),
                 "watchdog_observed_at": (NOW + dt.timedelta(minutes=5)).isoformat(),
                 "completed_at": (NOW + dt.timedelta(minutes=6)).isoformat()}
        value.update(changes)
        path = self.root / "github.json"
        path.write_text(json.dumps(value))
        return path

    def inactive_variables(self):
        variables = Variables()
        variables.intents.append(drill.launcher.watchdog_intent(
            commit=COMMIT, created_not_before=NOW - dt.timedelta(minutes=6),
            max_runtime_minutes=6, max_hourly_rate=.5, max_total_budget=.05))
        return variables

    def test_verify_accepts_only_zero_matching_pods(self):
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            absent = drill.verify(
                client=Client(), github_variables=self.inactive_variables(),
                expected_commit=COMMIT, github_run_receipt=self.receipt(),
                initial_balance_path=self.balance, final_balance_path=self.balance,
                max_total_budget=.05, now_fn=lambda: NOW)
        self.assertEqual(absent["provider_state"], "absent")
        self.assertFalse(absent["contract_auto_enabled"])
        self.assertFalse(absent["durable_intent_active"])

    def test_verify_rejects_live_or_unsuccessful_receipt(self):
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            with self.assertRaisesRegex(ValueError, "still exists"):
                drill.verify(
                    client=Client([{"name": drill.launcher.pod_name(COMMIT),
                                    "status": "DELETED"}]),
                    github_variables=self.inactive_variables(), expected_commit=COMMIT,
                    github_run_receipt=self.receipt(), initial_balance_path=self.balance,
                    final_balance_path=self.balance, max_total_budget=.05,
                    now_fn=lambda: NOW)
            with self.assertRaisesRegex(ValueError, "does not prove"):
                drill.verify(client=Client(), github_variables=self.inactive_variables(),
                             expected_commit=COMMIT, github_run_receipt=self.receipt(conclusion="failure"),
                             initial_balance_path=self.balance, final_balance_path=self.balance,
                             max_total_budget=.05, now_fn=lambda: NOW)

    def test_verify_rejects_manual_or_delayed_run_and_active_intent(self):
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            for changes in ({"event_name": "workflow_dispatch"},
                            {"watchdog_observed_at": (NOW + dt.timedelta(minutes=11)).isoformat()}):
                with self.subTest(changes=changes), self.assertRaises(ValueError):
                    drill.verify(client=Client(), github_variables=self.inactive_variables(),
                                 expected_commit=COMMIT, github_run_receipt=self.receipt(**changes),
                                 initial_balance_path=self.balance, final_balance_path=self.balance,
                                 max_total_budget=.05, now_fn=lambda: NOW)
            variables = self.inactive_variables()
            variables.request = mock.Mock(return_value={
                "name": drill.launcher.WATCHDOG_INTENT_VARIABLE,
                "value": json.dumps({**variables.intents[-1], "active": True})})
            with self.assertRaisesRegex(ValueError, "not restored inactive"):
                drill.verify(client=Client(), github_variables=variables,
                             expected_commit=COMMIT, github_run_receipt=self.receipt(),
                             initial_balance_path=self.balance, final_balance_path=self.balance,
                             max_total_budget=.05, now_fn=lambda: NOW)

    def test_verify_rejects_balance_delta_over_budget(self):
        final = self.root / "final-balance.json"
        final.write_text(json.dumps({"source": "runpod-console", "amount_usd": .8,
                                     "observed_at": NOW.isoformat()}))
        with mock.patch.object(drill.prep, "git", return_value=COMMIT):
            with self.assertRaisesRegex(ValueError, "balance delta"):
                drill.verify(client=Client(), github_variables=self.inactive_variables(),
                             expected_commit=COMMIT, github_run_receipt=self.receipt(),
                             initial_balance_path=self.balance, final_balance_path=final,
                             max_total_budget=.05, now_fn=lambda: NOW)


if __name__ == "__main__":
    unittest.main()
