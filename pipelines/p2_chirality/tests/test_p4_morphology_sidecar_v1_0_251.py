"""Synthetic regression tests for the P4 v1.0.251 morphology join contract."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

import pyarrow as pa
import pyarrow.parquet as pq


MODULE = (
    Path(__file__).parents[1]
    / "apjs_release_v1.0.251_morphology_sidecar"
    / "validate_p4_morphology_join_v1_0_251.py"
)
SPEC = importlib.util.spec_from_file_location("p4_morph_sidecar", MODULE)
assert SPEC and SPEC.loader
sidecar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sidecar)


SAFE_SCHEMA = {
    "object_id": pa.string(), "ra_deg": pa.float64(), "dec_deg": pa.float64(),
    "class_eq": pa.string(), "score_cw_eq": pa.float64(),
    "score_ccw_eq": pa.float64(), "score_ns_eq": pa.float64(),
    "score_eq_max": pa.float64(), "is_spiral": pa.bool_(),
    "primary_hc": pa.bool_(), "raw_flip_qc_unsafe": pa.bool_(),
}
MORPH_SCHEMA = {
    "BRICKID": pa.int64(), "OBJID": pa.int64(), "TYPE": pa.string(),
    "FRACDEV": pa.float64(), "SHAPEDEV_R": pa.float64(),
    "SHAPEDEV_E1": pa.float64(), "SHAPEDEV_E2": pa.float64(),
    "SHAPEEXP_R": pa.float64(), "SHAPEEXP_E1": pa.float64(),
    "SHAPEEXP_E2": pa.float64(),
}


def safe_table(ids: list[str], spiral: list[bool] | None = None) -> pa.Table:
    n = len(ids)
    spiral = spiral or [True] * n
    values = {
        "object_id": ids, "ra_deg": [1.0] * n, "dec_deg": [2.0] * n,
        "class_eq": ["CW"] * n, "score_cw_eq": [0.8] * n,
        "score_ccw_eq": [0.1] * n, "score_ns_eq": [0.1] * n,
        "score_eq_max": [0.8] * n, "is_spiral": spiral,
        "primary_hc": [True] * n, "raw_flip_qc_unsafe": [False] * n,
    }
    return pa.table({name: pa.array(values[name], type=typ) for name, typ in SAFE_SCHEMA.items()})


def morph_table(keys: list[tuple[int, int]]) -> pa.Table:
    n = len(keys)
    values = {
        "BRICKID": [key[0] for key in keys], "OBJID": [key[1] for key in keys],
        "TYPE": ["EXP"] * n, "FRACDEV": [0.0] * n,
        "SHAPEDEV_R": [1.0] * n, "SHAPEDEV_E1": [0.1] * n,
        "SHAPEDEV_E2": [0.2] * n, "SHAPEEXP_R": [1.1] * n,
        "SHAPEEXP_E1": [0.2] * n, "SHAPEEXP_E2": [0.3] * n,
    }
    return pa.table({name: pa.array(values[name], type=typ) for name, typ in MORPH_SCHEMA.items()})


class SidecarContractTests(unittest.TestCase):
    def validate(self, safe: pa.Table, morph: pa.Table, expected: int):
        with tempfile.TemporaryDirectory() as directory:
            safe_path = Path(directory) / "safe.parquet"
            morph_path = Path(directory) / "morph.parquet"
            pq.write_table(safe, safe_path)
            pq.write_table(morph, morph_path)
            return sidecar.validate_join(safe_path, morph_path, expected_spirals=expected)

    def test_exact_bidirectional_coverage_passes_and_excludes_nonspirals(self) -> None:
        result = self.validate(
            safe_table(["10_1", "10_2", "99_9"], [True, True, False]),
            morph_table([(10, 2), (10, 1)]),
            2,
        )
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["unique_join_rows"], 2)
        self.assertEqual(result["missing_rows"], 0)
        self.assertEqual(result["extra_rows"], 0)

    def test_duplicate_safe_key_fails_closed(self) -> None:
        with self.assertRaisesRegex(sidecar.JoinContractError, "safe spiral object_id"):
            self.validate(safe_table(["10_1", "10_1"]), morph_table([(10, 1), (10, 2)]), 2)

    def test_duplicate_morphology_key_fails_closed(self) -> None:
        with self.assertRaisesRegex(sidecar.JoinContractError, "BRICKID/OBJID keys"):
            self.validate(safe_table(["10_1", "10_2"]), morph_table([(10, 1), (10, 1)]), 2)

    def test_missing_and_extra_key_fail_closed(self) -> None:
        with self.assertRaisesRegex(sidecar.JoinContractError, "exact-coverage contract"):
            self.validate(safe_table(["10_1", "10_2"]), morph_table([(10, 1), (10, 3)]), 2)

    def test_row_count_mismatch_fails_before_join(self) -> None:
        with self.assertRaisesRegex(sidecar.JoinContractError, "row-count contract"):
            self.validate(safe_table(["10_1", "10_2"]), morph_table([(10, 1)]), 2)


if __name__ == "__main__":
    unittest.main()
