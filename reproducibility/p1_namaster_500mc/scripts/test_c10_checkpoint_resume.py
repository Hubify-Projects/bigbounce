#!/usr/bin/env python3
"""Fast regressions for c10 intra-shard checkpoint/resume integrity."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np

import c10_robustness_battery as c10
from checkpoint_io import publish_json, validate_json_receipt


CFG = {"name": "purify_b", "purify_b": True}


def fake_realization(index, _state):
    # Values exercise exact JSON float round-tripping and preserve seed order.
    rng = np.random.RandomState(c10.SEED_BASE + index)
    return rng.standard_normal(20).astype(np.float64)


def scientific_bytes(realizations):
    values = np.asarray(realizations, dtype=np.float64)
    payload = {
        "ordered_realizations": values.tolist(),
        "mean": values.mean(axis=0).tolist(),
        "std": values.std(axis=0).tolist(),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


class CheckpointResumeTest(unittest.TestCase):
    def test_interrupted_resume_is_bitwise_scientifically_identical(self):
        with tempfile.TemporaryDirectory(prefix="c10_checkpoint_test_") as tmp:
            checkpoint = Path(tmp) / "purify.checkpoint.json"
            with mock.patch.object(c10, "N_REAL", 52), mock.patch.object(
                c10, "_simulate_realization", side_effect=fake_realization
            ):
                uninterrupted = [fake_realization(i, {}) for i in range(c10.N_REAL)]

                calls = 0

                def crash_after_31(index, state):
                    nonlocal calls
                    calls += 1
                    if calls == 32:
                        raise RuntimeError("injected crash")
                    return fake_realization(index, state)

                with mock.patch.object(
                    c10, "_simulate_realization", side_effect=crash_after_31
                ):
                    with self.assertRaisesRegex(RuntimeError, "injected crash"):
                        c10._collect_serial_realizations(CFG, {}, checkpoint)

                payload = json.loads(checkpoint.read_text(encoding="utf-8"))
                self.assertEqual(payload["completed"], 25)
                self.assertEqual(payload["seed_end"], c10.SEED_BASE + 24)

                resumed = c10._collect_serial_realizations(CFG, {}, checkpoint)

            expected = scientific_bytes(uninterrupted)
            actual = scientific_bytes(resumed)
            self.assertEqual(actual, expected)
            self.assertEqual(
                hashlib.sha256(actual).hexdigest(),
                hashlib.sha256(expected).hexdigest(),
            )

    def test_checkpoint_receipt_rejects_config_code_and_operator_mismatch(self):
        with tempfile.TemporaryDirectory(prefix="c10_checkpoint_receipt_") as tmp:
            checkpoint = Path(tmp) / "purify.checkpoint.json"
            with mock.patch.object(c10, "N_REAL", 500):
                values = [fake_realization(i, {}) for i in range(25)]
                c10._publish_realization_checkpoint(checkpoint, CFG, values)

                with self.assertRaisesRegex(ValueError, "configs"):
                    c10._load_realization_checkpoint(
                        checkpoint, {"name": "purify_b", "purify_b": False}
                    )

                with mock.patch.object(c10, "code_sha256", return_value="0" * 64):
                    with self.assertRaisesRegex(ValueError, "code_sha256"):
                        c10._load_realization_checkpoint(checkpoint, CFG)

                with mock.patch.object(c10, "THEORY_OPERATOR", "wrong operator"):
                    with self.assertRaisesRegex(ValueError, "theory_operator"):
                        c10._load_realization_checkpoint(checkpoint, CFG)

    def test_legacy_final_receipt_without_code_hash_remains_valid(self):
        with tempfile.TemporaryDirectory(prefix="c10_legacy_receipt_") as tmp:
            result = Path(tmp) / "c10_purify_b.json"
            publish_json(
                result,
                {"configs": [{"name": "purify_b"}]},
                {
                    "suite": "c10",
                    "config_names": ["purify_b"],
                    "configs": [CFG],
                    "n_real": 500,
                    "seed_start": 42,
                    "seed_end": 541,
                    "theory_operator": c10.THEORY_OPERATOR,
                },
            )
            _, receipt = validate_json_receipt(
                result,
                expected_suite="c10",
                expected_configs=["purify_b"],
                expected_config_metadata=[CFG],
                expected_n_real=500,
                expected_seed_start=42,
                expected_seed_end=541,
                expected_theory_operator=c10.THEORY_OPERATOR,
            )
            self.assertNotIn("code_sha256", receipt)


if __name__ == "__main__":
    unittest.main()
