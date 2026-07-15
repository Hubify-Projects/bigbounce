"""Regression tests for the P4 v1.0.244 fail-closed release split."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


MODULE_PATH = Path(__file__).parents[1] / "build_apjs_release_v1_0_244.py"
SPEC = importlib.util.spec_from_file_location("p4_release_244", MODULE_PATH)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)
CLAIM_SPEC = importlib.util.spec_from_file_location(
    "p4_claims_244", Path(__file__).parents[1] / "validate_p4_v1_0_244_claims.py"
)
assert CLAIM_SPEC and CLAIM_SPEC.loader
claims = importlib.util.module_from_spec(CLAIM_SPEC)
CLAIM_SPEC.loader.exec_module(claims)


def fixture_table() -> pa.Table:
    """Four rows: safe HC, unsafe HC, unsafe non-HC, safe non-HC."""
    return pa.table(
        {
            "dr8_id": ["safe-hc", "unsafe-hc", "unsafe-ns", "safe-ns"],
            "ra": [1.0, 2.0, 3.0, 4.0],
            "dec": [-1.0, -2.0, -3.0, -4.0],
            "class_eq": ["CW", "CCW", "NOT_SPIRAL", "NOT_SPIRAL"],
            "p_cw_eq": [0.8, 0.1, 0.05, 0.1],
            "p_ccw_eq": [0.1, 0.8, 0.05, 0.1],
            "p_ns_eq": [0.1, 0.1, 0.9, 0.8],
            # y is the full-coverage raw leg. Row 2 reconstructs flip-CW=1.5;
            # row 3 reconstructs flip-NS=1.7. The remaining rows stay bounded.
            "p_cw_raw_x": [0.8, 0.1, 0.05, 0.1],
            "p_ccw_raw_x": [0.1, 0.8, 0.05, 0.1],
            "p_ns_raw_x": [0.1, 0.1, 0.9, 0.8],
            "p_cw_raw_y": [0.8, 0.1, 0.05, 0.1],
            "p_ccw_raw_y": [0.1, 0.1, 0.05, 0.1],
            "p_ns_raw_y": [0.1, 0.1, 0.1, 0.8],
        }
    )


def expected_fixture_counts() -> dict[str, int]:
    return {
        "catalog_rows": 4,
        "primary_hc_rows": 2,
        "unsafe_catalog_rows": 2,
        "unsafe_primary_hc_rows": 1,
        "strict_primary_hc_rows": 1,
    }


class ReleaseContractTests(unittest.TestCase):
    def test_every_new_manuscript_number_has_a_pinned_source(self) -> None:
        result = claims.audit()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["failed_gates"], [])
        self.assertTrue(all(result["gates"].values()))

    def test_split_quarantines_catalog_and_hc_counts_without_exposing_raw_columns(self) -> None:
        primary, quarantine, stats = release.split_batch(fixture_table().to_batches()[0])

        self.assertEqual(primary.num_rows, 4)
        self.assertEqual(primary.schema.names, list(release.PRIMARY_COLUMNS))
        self.assertFalse(any(
            "raw_score" in name or "reconstructed" in name for name in primary.schema.names
        ))
        self.assertEqual(primary["primary_hc"].to_pylist(), [True, True, False, False])
        self.assertEqual(
            primary["raw_flip_qc_unsafe"].to_pylist(), [False, True, True, False]
        )

        self.assertEqual(quarantine.num_rows, 2)
        self.assertEqual(quarantine["object_id"].to_pylist(), ["unsafe-hc", "unsafe-ns"])
        self.assertEqual(quarantine["is_primary_hc"].to_pylist(), [True, False])
        self.assertEqual(quarantine["do_not_use_for_science"].to_pylist(), [True, True])
        self.assertEqual(set(quarantine["unsafe_reason_code"].to_pylist()), {release.REASON})
        self.assertEqual(
            {key: stats[key] for key in expected_fixture_counts()},
            expected_fixture_counts(),
        )


    def test_machine_schema_calls_scores_uncalibrated_and_keeps_archive_gate_open(self) -> None:
        schema = json.loads(release.SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertIn("no calibrated label probabilities", schema["scientific_scope"])
        self.assertEqual(schema["release_gates"]["immutable_archive_or_doi"], "OPEN")
        for column in schema["quarantine_product"]["columns"]:
            if "score" in column["name"]:
                self.assertIs(column.get("calibrated"), False)


    def test_small_release_build_validates_and_fails_closed_on_wrong_counts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            source = tmp_path / "source.parquet"
            pq.write_table(fixture_table(), source)
            null_path = tmp_path / "null.npy"
            np.save(null_path, np.array([0.1, 0.2, 0.3]))
            schema_path = tmp_path / "schema.json"
            schema = json.loads(release.SCHEMA_PATH.read_text(encoding="utf-8"))
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            source_sha256 = release.sha256_file(source)
            receipt_path = tmp_path / "receipt.json"
            receipt_path.write_text(
                json.dumps(
                    {
                        "catalog": {
                            "sha256": source_sha256,
                            "bytes": source.stat().st_size,
                            "rows": 4,
                            "revision": "fixture",
                        }
                    }
                ),
                encoding="utf-8",
            )

            with (
                mock.patch.object(release, "SOURCE_BYTES", source.stat().st_size),
                mock.patch.object(release, "SOURCE_SHA256", source_sha256),
                mock.patch.object(release, "EXPECTED", expected_fixture_counts()),
            ):
                good = tmp_path / "good"
                manifest = release.build_release(
                    source, good, schema_path, null_path, receipt_path
                )
                self.assertEqual(manifest["counts"], expected_fixture_counts())
                validation = release.validate_release(good)
                self.assertEqual(validation["status"], "PASS")
                self.assertTrue(validation["primary_raw_score_columns_absent"])
                self.assertTrue(all(validation["semantic_gates"].values()))
                primary = pq.read_table(good / schema["primary_product"]["filename"])
                self.assertEqual(primary["raw_flip_qc_unsafe"].to_pylist().count(True), 2)

            wrong = {**expected_fixture_counts(), "unsafe_catalog_rows": 3}
            with (
                mock.patch.object(release, "SOURCE_BYTES", source.stat().st_size),
                mock.patch.object(release, "SOURCE_SHA256", source_sha256),
                mock.patch.object(release, "EXPECTED", wrong),
                self.assertRaisesRegex(release.ReleaseError, "count contract failed"),
            ):
                bad = tmp_path / "bad"
                release.build_release(source, bad, schema_path, null_path, receipt_path)
            self.assertFalse((bad / schema["primary_product"]["filename"]).exists())
            self.assertFalse((bad / schema["quarantine_product"]["filename"]).exists())

    def test_source_identity_rejects_same_size_corruption_before_parquet_read(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            source = tmp_path / "source.parquet"
            pq.write_table(fixture_table(), source)
            source_sha256 = release.sha256_file(source)
            source_bytes = source.stat().st_size
            receipt_path = tmp_path / "receipt.json"
            receipt_path.write_text(
                json.dumps(
                    {
                        "catalog": {
                            "sha256": source_sha256,
                            "bytes": source_bytes,
                            "rows": 4,
                            "revision": "fixture",
                        }
                    }
                ),
                encoding="utf-8",
            )
            with source.open("r+b") as handle:
                handle.seek(source_bytes // 2)
                original = handle.read(1)
                handle.seek(source_bytes // 2)
                handle.write(bytes([original[0] ^ 0x01]))

            with (
                mock.patch.object(release, "SOURCE_BYTES", source_bytes),
                mock.patch.object(release, "SOURCE_SHA256", source_sha256),
                mock.patch.object(release, "EXPECTED", expected_fixture_counts()),
                self.assertRaisesRegex(release.ReleaseError, "current source SHA-256 mismatch"),
            ):
                release.validate_source_identity(source, receipt_path)


if __name__ == "__main__":
    unittest.main()
