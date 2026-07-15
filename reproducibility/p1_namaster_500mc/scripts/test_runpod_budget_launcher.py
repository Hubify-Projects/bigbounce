#!/usr/bin/env python3

import datetime as dt
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().with_name("runpod_budget_launcher.py")
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("runpod_budget_launcher", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)
NOW = dt.datetime(2026, 7, 15, 20, 0, tzinfo=dt.timezone.utc)


class Client:
    def __init__(self, pods=None, created=None):
        self.pods = pods or []
        self.created = created or {
            "id": "pod-safe", "name": "ignored", "costPerHr": 0.25,
            "imageName": "repo/image@sha256:" + "a" * 64,
            "gpuCount": 1, "gpuTypeId": "NVIDIA RTX A4000", "status": "CREATED",
        }
        self.create_calls = []
        self.deleted = []
        self.get_result = {"status": "RUNNING"}

    def list_pods(self): return self.pods
    def create_pod(self, payload):
        self.create_calls.append(payload)
        return self.created
    def get_pod(self, pod_id): return self.get_result
    def delete_pod(self, pod_id): self.deleted.append(pod_id)


class LauncherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.balance = self.root / "balance.json"
        self.receipt = self.root / "events.jsonl"
        self.balance.write_text(json.dumps({
            "source": "runpod-console", "amount_usd": 10,
            "observed_at": NOW.isoformat(),
        }))
        self.commit = "1" * 40
        self.image = "repo/image@sha256:" + "a" * 64
        self.manifest = {"git_commit": self.commit, "container": {"image": self.image}}

    def tearDown(self): self.temp.cleanup()

    def launch(self, client, **updates):
        values = dict(
            client=client, manifest=self.manifest, expected_commit=self.commit,
            contract={}, balance_path=self.balance, balance_max_age_minutes=15,
            max_hourly_rate=0.5, max_total_budget=1, max_runtime_minutes=60,
            gpu_type_id="NVIDIA RTX A4000", receipt_path=self.receipt,
            now_fn=lambda: NOW,
        )
        values.update(updates)
        with mock.patch.object(MODULE, "validate_manifest"):
            return MODULE.launch(**values)

    def test_default_cli_dry_run_does_not_construct_or_mutate_client(self):
        argv = [str(SCRIPT), "--manifest", str(self.root / "manifest.json"),
                "--expected-commit", self.commit, "--receipt", str(self.receipt)]
        (self.root / "manifest.json").write_text("{}")
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "secret"}), \
             mock.patch.object(MODULE, "validate_manifest"), \
             mock.patch.object(MODULE, "RunPodREST") as rest, \
             mock.patch("sys.argv", argv):
            self.assertEqual(MODULE.main(), 0)
            rest.return_value.list_pods.assert_not_called()
            rest.return_value.create_pod.assert_not_called()

    def test_stale_and_insufficient_balance_fail_before_http(self):
        client = Client()
        self.balance.write_text(json.dumps({"source": "runpod-console", "amount_usd": 0.2,
                                            "observed_at": NOW.isoformat()}))
        with self.assertRaisesRegex(ValueError, "insufficient"):
            self.launch(client)
        self.balance.write_text(json.dumps({"source": "runpod-console", "amount_usd": 10,
                                            "observed_at": (NOW - dt.timedelta(hours=1)).isoformat()}))
        with self.assertRaisesRegex(ValueError, "stale"):
            self.launch(client)
        self.assertEqual(client.create_calls, [])

    def test_duplicate_name_fails_before_create(self):
        client = Client(pods=[{"name": MODULE.pod_name(self.commit)}])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.launch(client)
        self.assertEqual(client.create_calls, [])

    def test_overprice_response_is_immediately_deleted_and_receipted(self):
        client = Client(created={"id": "pod-over", "costPerHr": 0.75,
                                 "imageName": self.image, "gpuCount": 1, "status": "CREATED"})
        with self.assertRaisesRegex(ValueError, "hourly-rate ceiling"):
            self.launch(client)
        self.assertEqual(client.deleted, ["pod-over"])
        self.assertIn("create_mismatch_deleted", self.receipt.read_text())

    def test_deadline_watchdog_deletes(self):
        client = Client()
        result = MODULE.watchdog(client, "pod-1", NOW, 1, 0.25, self.receipt,
                                 now_fn=lambda: NOW, sleep_fn=lambda _: None)
        self.assertEqual(result, "deadline")
        self.assertEqual(client.deleted, ["pod-1"])

    def test_key_never_leaks_to_receipt_or_error(self):
        secret = "super-secret-runpod-key"
        client = Client(created={"id": "pod-bad", "costPerHr": 10,
                                 "imageName": self.image, "gpuCount": 1, "status": "CREATED"})
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": secret}):
            with self.assertRaises(ValueError) as caught:
                self.launch(client)
        combined = str(caught.exception) + self.receipt.read_text()
        self.assertNotIn(secret, combined)

    def test_create_requests_exactly_one_gpu_and_digest_image(self):
        client = Client()
        self.launch(client)
        payload = client.create_calls[0]
        self.assertEqual(payload["gpuCount"], 1)
        self.assertEqual(payload["gpuTypeIds"], ["NVIDIA RTX A4000"])
        self.assertEqual(payload["imageName"], self.image)


if __name__ == "__main__":
    unittest.main()
