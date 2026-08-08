"""Regression tests for the P4 v1.0.257 computational closure generators."""

from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path
import unittest

import healpy as hp
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


P4 = Path(__file__).resolve().parents[1]
CATALOG = P4 / "apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class P4V10257ComputationalClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.primary = load_module(
            "p4_primary_strict",
            P4 / "generate_p4_primary_label_shuffle_strict_v1_0_257.py",
        )

    def test_strict_primary_selection_is_exact(self):
        table = pq.read_table(
            CATALOG,
            columns=["primary_hc", "raw_flip_qc_unsafe"],
        )
        strict = self.primary.select_strict_primary(table)
        self.assertEqual(strict.num_rows, 890_069)
        receipt = json.loads(
            (
                P4
                / "outputs/canonical_provenance/"
                "p4_primary_hc_safe_label_shuffle_10k_v1_0_257.json"
            ).read_text(encoding="utf-8")
        )
        counts = receipt["selection_counts"]
        self.assertEqual(counts["n_selected_rows"], 890_069)
        self.assertEqual(counts["n_unsafe_rows_selected"], 0)
        self.assertEqual(
            len(counts["selected_row_mask_packbits_little_sha256"]), 64
        )

    def test_full_spiral_support_is_exact_24087_pixels(self):
        table = pq.read_table(
            CATALOG, columns=["ra_deg", "dec_deg", "class_eq"]
        )
        labels = np.asarray(table["class_eq"].combine_chunks().to_pylist())
        spiral = np.logical_or(labels == "CW", labels == "CCW")
        ra = table["ra_deg"].combine_chunks().to_numpy()[spiral]
        dec = table["dec_deg"].combine_chunks().to_numpy()[spiral]
        pix = hp.ang2pix(
            64, np.radians(90.0 - dec), np.radians(ra % 360.0)
        )
        counts = np.bincount(pix, minlength=hp.nside2npix(64))
        self.assertEqual(int((counts >= 10).sum()), 24_087)
        self.assertEqual(int((counts > 0).sum()), 24_270)
        self.assertNotEqual(int((counts >= 10).sum()), int((counts > 0).sum()))

    def test_strict_selection_rejects_unsafe_hc_rows(self):
        table = pa.table(
            {
                "primary_hc": [True, True, False, False],
                "raw_flip_qc_unsafe": [False, True, False, True],
            }
        )
        selected = self.primary.select_strict_primary(table)
        self.assertEqual(selected.num_rows, 1)
        self.assertFalse(selected["raw_flip_qc_unsafe"][0].as_py())

    def test_reduced_draw_fixture_binds_one_common_support(self):
        receipt_path = (
            P4
            / "outputs/canonical_provenance/"
            "p4_fsc_exact_support_harmonics_v1_0_257_fixture.json"
        )
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        support = receipt["support"]
        invariants = receipt["common_support_invariants"]
        self.assertEqual(support["n_pixels"], 24_087)
        self.assertEqual(
            invariants["all_data_fields_use_mask_sha256"],
            support["mask"]["sha256"],
        )
        self.assertEqual(
            invariants["all_null_fields_use_mask_sha256"],
            support["mask"]["sha256"],
        )
        self.assertTrue(invariants["apodized_weight_derived_from_same_binary_mask"])
        self.assertTrue(invariants["apodized_nonzero_pixels_subset_of_support"])
        self.assertEqual(
            receipt["arrays"]["members"]["fixed_occupancy_binary_c1_to_c5"],
            [8, 5],
        )
        for record in (
            support["mask"],
            support["indices"],
            receipt["arrays"],
            receipt["generator"],
        ):
            path = Path(record["path"])
            if not path.is_absolute():
                path = P4.parents[1] / path
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(digest, record["sha256"])

    def test_closure_sha256_ledger_is_complete_and_valid(self):
        ledger_path = (
            P4
            / "outputs/canonical_provenance/"
            "p4_v1_0_257_computational_closure_sha256.json"
        )
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(len(ledger["files"]), 8)
        for record in ledger["files"]:
            path = P4.parents[1] / record["path"]
            self.assertTrue(path.is_file(), record["path"])
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                record["sha256"],
                record["path"],
            )


if __name__ == "__main__":
    unittest.main()
