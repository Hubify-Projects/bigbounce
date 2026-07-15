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
            "networkVolume": {"id": "vol-1", "dataCenterId": "US-KS-2"},
        }
        self.create_calls = []
        self.deleted = []
        self.get_result = {"status": "RUNNING"}

    def list_pods(self): return self.pods
    def create_pod(self, payload):
        self.create_calls.append(payload)
        return self.created
    def get_pod(self, pod_id):
        if pod_id in self.deleted:
            return {"status": "TERMINATED"}
        return self.get_result
    def delete_pod(self, pod_id): self.deleted.append(pod_id)
    def stop_pod(self, pod_id): pass


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
        self.manifest = {"git_commit": self.commit, "contract_id": "contract-v1",
                         "input_sha256": {"contract.json": "b" * 64},
                         "container": {"image": self.image, "install": ["true"]}}

    def tearDown(self): self.temp.cleanup()

    def launch(self, client, **updates):
        values = dict(
            client=client, manifest=self.manifest, expected_commit=self.commit,
            contract={"provider_mutation_ready": True}, balance_path=self.balance, balance_max_age_minutes=15,
            max_hourly_rate=0.5, max_total_budget=1, max_runtime_minutes=60,
            gpu_type_id="NVIDIA RTX A4000", receipt_path=self.receipt,
            network_volume_id="vol-1", datacenter_id="US-KS-2", s3_client=object(),
            retention_staging=self.root / "download", retention_receipt=self.root / "verified.json",
            now_fn=lambda: NOW,
        )
        values.update(updates)
        with mock.patch.object(MODULE, "validate_manifest"), \
             mock.patch.object(MODULE, "supervise", return_value="verified"):
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
                                 "imageName": self.image, "gpuCount": 1, "status": "CREATED",
                                 "networkVolume": {"id": "vol-1", "dataCenterId": "US-KS-2"}})
        with self.assertRaisesRegex(ValueError, "hourly-rate ceiling"):
            self.launch(client)
        self.assertEqual(client.deleted, ["pod-over"])
        self.assertIn("post_create_exception_cleanup", self.receipt.read_text())

    def test_deadline_watchdog_deletes(self):
        client = Client()
        result = MODULE.watchdog(client, "pod-1", NOW - dt.timedelta(hours=1), NOW, 1, 0.25, self.receipt,
                                 now_fn=lambda: NOW, sleep_fn=lambda _: None)
        self.assertEqual(result, "deadline")
        self.assertEqual(client.deleted, ["pod-1"])

    def test_key_never_leaks_to_receipt_or_error(self):
        secret = "super-secret-runpod-key"
        client = Client(created={"id": "pod-bad", "costPerHr": 10,
                                 "imageName": self.image, "gpuCount": 1, "status": "CREATED",
                                 "networkVolume": {"id": "vol-1", "dataCenterId": "US-KS-2"}})
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
        self.assertEqual(payload["networkVolumeId"], "vol-1")
        self.assertEqual(payload["dataCenterIds"], ["US-KS-2"])
        self.assertEqual(payload["cloudType"], "SECURE")
        self.assertEqual(payload["volumeMountPath"], "/workspace")
        self.assertEqual(payload["dockerEntrypoint"], ["bash", "-lc"])
        self.assertEqual(len(payload["dockerStartCmd"]), 1)
        self.assertIn(self.commit, payload["dockerStartCmd"][0])

    def test_launch_enters_supervisor_immediately(self):
        client = Client()
        with mock.patch.object(MODULE, "validate_manifest"), \
             mock.patch.object(MODULE, "supervise", return_value="verified") as supervisor:
            MODULE.launch(
                client=client, manifest=self.manifest, expected_commit=self.commit,
                contract={"provider_mutation_ready": True}, balance_path=self.balance,
                balance_max_age_minutes=15, max_hourly_rate=0.5, max_total_budget=1,
                max_runtime_minutes=60, gpu_type_id="NVIDIA RTX A4000",
                receipt_path=self.receipt, network_volume_id="vol-1", datacenter_id="US-KS-2",
                s3_client=object(), retention_staging=self.root / "stage",
                retention_receipt=self.root / "verified.json", now_fn=lambda: NOW,
            )
        supervisor.assert_called_once()

    def test_supervisor_verifies_retention_before_delete(self):
        client = Client()
        client.get_result = {"status": "RUNNING", "costPerHr": 0.25}
        with mock.patch.object(MODULE.s3verify, "download_and_verify", return_value={"state": "verified"}):
            result = MODULE.supervise(
                client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
                network_volume_id="vol-1", datacenter_id="US-KS-2",
                retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
                receipt_path=self.receipt, created_at=NOW, deadline=NOW + dt.timedelta(hours=1),
                max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
                now_fn=lambda: NOW, sleep_fn=lambda _: None,
            )
        self.assertEqual(result, "verified")
        self.assertEqual(client.deleted, ["pod-1"])

    def test_terminal_with_corrupt_or_missing_s3_is_retained(self):
        client = Client()
        client.get_result = {"status": "EXITED", "costPerHr": 0.25}
        with mock.patch.object(MODULE.s3verify, "download_and_verify", side_effect=ValueError("missing marker")):
            result = MODULE.supervise(
                client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
                network_volume_id="vol-1", datacenter_id="US-KS-2",
                retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
                receipt_path=self.receipt, created_at=NOW, deadline=NOW + dt.timedelta(hours=1),
                max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
                now_fn=lambda: NOW, sleep_fn=lambda _: None,
            )
        self.assertEqual(result, "terminal_unverified")
        self.assertEqual(client.deleted, [])

    def test_supervisor_deadline_deletes_unverified_for_cost_safety(self):
        client = Client()
        with mock.patch.object(MODULE.s3verify, "download_and_verify") as verifier:
            result = MODULE.supervise(
                client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
                network_volume_id="vol-1", datacenter_id="US-KS-2",
                retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
                receipt_path=self.receipt, created_at=NOW - dt.timedelta(hours=1), deadline=NOW,
                max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
                now_fn=lambda: NOW, sleep_fn=lambda _: None,
            )
        self.assertEqual(result, "deadline")
        self.assertEqual(client.deleted, ["pod-1"])
        verifier.assert_not_called()
        self.assertIn("unverified", self.receipt.read_text())

    def test_s3_exception_and_credentials_never_leak(self):
        secret = "secret-s3-credential-value"
        client = Client()
        client.get_result = {"status": "EXITED", "costPerHr": 0.25}
        with mock.patch.dict(os.environ, {"AWS_SECRET_ACCESS_KEY": secret}), \
             mock.patch.object(MODULE.s3verify, "download_and_verify",
                               side_effect=ValueError(f"request included {secret}")):
            MODULE.supervise(
                client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
                network_volume_id="vol-1", datacenter_id="US-KS-2",
                retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
                receipt_path=self.receipt, created_at=NOW, deadline=NOW + dt.timedelta(hours=1),
                max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
                now_fn=lambda: NOW, sleep_fn=lambda _: None,
            )
        self.assertNotIn(secret, self.receipt.read_text())

    def test_wrong_create_response_volume_is_cleaned_up(self):
        client = Client(created={"id": "pod-wrong", "costPerHr": 0.25,
                                 "imageName": self.image, "gpuCount": 1,
                                 "gpuTypeId": "NVIDIA RTX A4000", "status": "CREATED",
                                 "networkVolume": {"id": "wrong", "dataCenterId": "US-KS-2"}})
        with self.assertRaisesRegex(ValueError, "volume"):
            self.launch(client)
        self.assertIn("pod-wrong", client.deleted)

    def test_receipt_failure_after_create_triggers_confirmed_cleanup(self):
        client = Client()
        with mock.patch.object(MODULE, "validate_manifest"), \
             mock.patch.object(MODULE, "append_receipt", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                MODULE.launch(
                    client=client, manifest=self.manifest, expected_commit=self.commit,
                    contract={"provider_mutation_ready": True}, balance_path=self.balance,
                    balance_max_age_minutes=15, max_hourly_rate=0.5, max_total_budget=1,
                    max_runtime_minutes=60, gpu_type_id="NVIDIA RTX A4000",
                    receipt_path=self.receipt, network_volume_id="vol-1", datacenter_id="US-KS-2",
                    s3_client=object(), retention_staging=self.root / "stage",
                    retention_receipt=self.root / "verified.json", now_fn=lambda: NOW,
                    sleep_fn=lambda _: None)
        self.assertIn("pod-safe", client.deleted)

    def test_missing_live_price_is_cost_safely_deleted(self):
        client = Client()
        client.get_result = {"status": "RUNNING"}
        result = MODULE.supervise(
            client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
            network_volume_id="vol-1", datacenter_id="US-KS-2",
            retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
            receipt_path=self.receipt, created_at=NOW, deadline=NOW + dt.timedelta(hours=1),
            max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
            now_fn=lambda: NOW, sleep_fn=lambda _: None)
        self.assertEqual(result, "hourly_rate")
        self.assertIn("pod-1", client.deleted)

    def test_get_error_keeps_supervising_until_cost_deadline(self):
        class GetErrorClient(Client):
            def get_pod(self, pod_id):
                if pod_id in self.deleted:
                    return {"status": "TERMINATED"}
                raise ValueError("transient GET")
        client = GetErrorClient()
        times = iter([NOW, NOW + dt.timedelta(minutes=61)])
        result = MODULE.supervise(
            client=client, s3_client=object(), pod_id="pod-1", manifest=self.manifest,
            network_volume_id="vol-1", datacenter_id="US-KS-2",
            retention_staging=self.root / "stage", retention_receipt=self.root / "verified.json",
            receipt_path=self.receipt, created_at=NOW, deadline=NOW + dt.timedelta(minutes=60),
            max_total_budget=1, max_hourly_rate=0.5, cost_per_hour=0.25,
            now_fn=lambda: next(times), sleep_fn=lambda _: None)
        self.assertEqual(result, "deadline")
        self.assertIn("supervisor_get_ambiguous", self.receipt.read_text())

    def test_delete_retries_and_confirms(self):
        class FlakyDelete(Client):
            def __init__(self):
                super().__init__()
                self.attempts = 0
            def delete_pod(self, pod_id):
                self.attempts += 1
                if self.attempts == 1:
                    raise ValueError("transient delete")
                super().delete_pod(pod_id)
        client = FlakyDelete()
        self.assertTrue(MODULE.terminate_confirmed(client, "pod-1", sleep_fn=lambda _: None))
        self.assertEqual(client.attempts, 2)

    def test_delete_confirmation_failure_is_reported(self):
        class FailedDelete(Client):
            def delete_pod(self, pod_id): raise ValueError("delete unavailable")
            def get_pod(self, pod_id): return {"status": "RUNNING"}
        self.assertFalse(MODULE.terminate_confirmed(FailedDelete(), "pod-1", sleep_fn=lambda _: None))

    def test_contract_refuses_launch_before_any_provider_http(self):
        client = Client()
        with mock.patch.object(MODULE, "validate_manifest"):
            with self.assertRaisesRegex(ValueError, "provider_mutation_ready is false"):
                MODULE.launch(
                    client=client, manifest=self.manifest, expected_commit=self.commit,
                    contract={"provider_mutation_ready": False}, balance_path=self.balance,
                    balance_max_age_minutes=15, max_hourly_rate=0.5,
                    max_total_budget=1, max_runtime_minutes=60,
                    gpu_type_id="NVIDIA RTX A4000", receipt_path=self.receipt,
                    now_fn=lambda: NOW,
                )
        self.assertEqual(client.create_calls, [])
        self.assertEqual(client.deleted, [])

    def test_launch_cli_refuses_before_list_or_create(self):
        manifest_path = self.root / "manifest.json"
        manifest_path.write_text(json.dumps(self.manifest))
        argv = [
            str(SCRIPT), "--manifest", str(manifest_path),
            "--expected-commit", self.commit, "--receipt", str(self.receipt),
            "--launch", "--confirm", MODULE.CONFIRMATION,
        ]
        with mock.patch.dict(os.environ, {"RUNPOD_API_KEY": "secret"}), \
             mock.patch.object(MODULE, "validate_manifest"), \
             mock.patch.object(MODULE, "RunPodREST") as rest, \
             mock.patch("sys.argv", argv):
            with self.assertRaisesRegex(ValueError, "provider_mutation_ready is false"):
                MODULE.main()
        rest.return_value.list_pods.assert_not_called()
        rest.return_value.create_pod.assert_not_called()

    def test_restarted_watchdog_accrues_from_original_creation_time(self):
        client = Client()
        result = MODULE.watchdog(
            client, "pod-old", NOW - dt.timedelta(hours=5), NOW + dt.timedelta(hours=1),
            1, 0.25, self.receipt, now_fn=lambda: NOW, sleep_fn=lambda _: None,
        )
        self.assertEqual(result, "budget")
        self.assertEqual(client.deleted, ["pod-old"])


if __name__ == "__main__":
    unittest.main()
