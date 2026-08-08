#!/usr/bin/env python3
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import runpod_external_watchdog as watchdog


COMMIT = "a" * 40
NOW = dt.datetime(2026, 7, 15, 12, tzinfo=dt.timezone.utc)


def intent(**changes):
    value = {
        "schema": watchdog.SCHEMA,
        "active": True,
        "git_commit": COMMIT,
        "pod_name": f"p1b-physical-spectrum-500mc-{COMMIT[:12]}",
        "created_not_before": "2026-07-15T10:00:00Z",
        "deadline": "2026-07-15T14:00:00Z",
        "max_hourly_rate_usd": 1.0,
        "max_total_budget_usd": 10.0,
    }
    value.update(changes)
    return value


class Client:
    def __init__(self, pods):
        self.pods = pods

    def list_pods(self):
        return {"pods": self.pods}


def pod(**changes):
    value = {"id": "pod-1", "name": intent()["pod_name"], "status": "RUNNING", "costPerHr": 0.5}
    value.update(changes)
    return value


class WatchdogTests(unittest.TestCase):
    def test_malformed_intent_rejected(self):
        for bad in ({}, intent(extra=True), intent(git_commit="short"),
                    intent(pod_name="wrong"), intent(max_total_budget_usd=0)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                watchdog.validate_intent(bad)

    def test_no_matching_pod_does_not_delete(self):
        calls = []
        result = watchdog.run_once(Client([pod(name="other")]), intent(), now=NOW,
                                   terminate_fn=lambda *args: calls.append(args))
        self.assertEqual(result["reason"], "no_matching_pod")
        self.assertEqual(calls, [])

    def test_inactive_intent_does_not_list_or_delete(self):
        class NoCalls:
            def list_pods(self):
                raise AssertionError("inactive intent must not list pods")
        result = watchdog.run_once(NoCalls(), intent(active=False), now=NOW)
        self.assertEqual(result["reason"], "inactive_intent")

    def test_duplicate_live_matches_are_all_deleted(self):
        calls = []
        pods = [pod(id="one"), pod(id="two")]
        result = watchdog.run_once(Client(pods), intent(), now=NOW,
                                   terminate_fn=lambda client, pod_id: calls.append(pod_id) or True)
        self.assertEqual(calls, ["one", "two"])
        self.assertEqual(result["reasons"], ["duplicate_matches"])

    def test_deadline_deletes(self):
        calls = []
        result = watchdog.run_once(Client([pod()]), intent(),
                                   now=NOW + dt.timedelta(hours=3),
                                   terminate_fn=lambda client, pod_id: calls.append(pod_id) or True)
        self.assertEqual(result["reasons"], ["deadline"])
        self.assertEqual(calls, ["pod-1"])

    def test_budget_accrues_conservatively_from_intent(self):
        calls = []
        bounded = intent(max_total_budget_usd=1.5)
        result = watchdog.run_once(Client([pod()]), bounded, now=NOW,
                                   terminate_fn=lambda client, pod_id: calls.append(pod_id) or True)
        self.assertEqual(result["reasons"], ["budget"])

    def test_price_ambiguity_and_exceedance_delete(self):
        for row, reason in ((pod(costPerHr=None), "hourly_price_ambiguous"),
                            (pod(costPerHr=1.01), "hourly_price_exceeded")):
            with self.subTest(reason=reason):
                result = watchdog.run_once(Client([row]), intent(), now=NOW,
                                           terminate_fn=lambda *_: True)
                self.assertEqual(result["reasons"], [reason])

    def test_terminal_pod_is_not_deleted(self):
        calls = []
        result = watchdog.run_once(Client([pod(status="EXITED", costPerHr=None)]), intent(), now=NOW,
                                   terminate_fn=lambda *args: calls.append(args))
        self.assertEqual(result["reason"], "already_terminal")
        self.assertEqual(calls, [])

    def test_full_commit_metadata_must_match_when_available(self):
        with self.assertRaisesRegex(ValueError, "commit metadata"):
            watchdog.run_once(Client([pod(metadata={"git_commit": "b" * 40})]), intent(), now=NOW)

    def test_delete_ambiguity_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "could not be confirmed"):
            watchdog.run_once(Client([pod(costPerHr=None)]), intent(), now=NOW,
                              terminate_fn=lambda *_: False)


if __name__ == "__main__":
    unittest.main()
