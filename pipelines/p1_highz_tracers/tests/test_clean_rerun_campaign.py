"""Offline unit tests for the AUG-011 clean-rerun campaign scaffold.

No network access; no full-scale DESI download. Covers only the pure,
locally-computable pieces of the campaign under
`pipelines/p1_highz_tracers/clean_rerun/`:

  - inventory path-construction and grouping rules, against a synthetic
    zcatalog-like FITS table;
  - the deterministic two-stage PPS cluster sample (group selection, row-
    budget allocation, per-group sampling, and the fit/validation split),
    run entirely against small synthetic group tables — no FITS file
    involved;
  - the anomaly-score arithmetic, run through the real archived `BigAE`
    class (imported unmodified from `enhanced_18M_inference.py`) with a
    fixed-seed state dict, against a hand-computed z-score;
  - the AUG-011 public-ID-first scan filter: `export-group-targetids`
    against a synthetic zcatalog-like FITS table, `run_scan.py`'s Parquet
    predicate-pushdown group-targetid loader against a synthetic Parquet
    file, and `run_scan.py`'s per-group filter/audit-record logic against
    synthetic scored rows (no coadd download, no torch inference involved).
"""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
CLEAN_RERUN_DIR = ROOT / "pipelines/p1_highz_tracers/clean_rerun"
sys.path.insert(0, str(CLEAN_RERUN_DIR))

import derive_locator_inventory as inventory_tool  # noqa: E402
import build_calibration as calibration_tool  # noqa: E402
import run_scan as run_scan_tool  # noqa: E402


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _write_synthetic_zcatalog(path: Path, rows: list[tuple[int, str, str, int]]) -> None:
    """Write a minimal FITS binary table with TARGETID/SURVEY/PROGRAM/HEALPIX,
    standing in for `zall-pix-iron.fits` without touching the network."""
    from astropy.io import fits

    targetid = np.array([r[0] for r in rows], dtype=np.int64)
    survey = np.array([r[1] for r in rows], dtype="S10")
    program = np.array([r[2] for r in rows], dtype="S10")
    healpix = np.array([r[3] for r in rows], dtype=np.int64)
    columns = fits.ColDefs(
        [
            fits.Column(name="TARGETID", format="K", array=targetid),
            fits.Column(name="SURVEY", format="10A", array=survey),
            fits.Column(name="PROGRAM", format="10A", array=program),
            fits.Column(name="HEALPIX", format="K", array=healpix),
        ]
    )
    hdu = fits.BinTableHDU.from_columns(columns, name="ZCATALOG")
    hdul = fits.HDUList([fits.PrimaryHDU(), hdu])
    hdul.writeto(path, overwrite=True)


class InventoryPathConstructionTest(unittest.TestCase):
    def test_sorted_unique_groups_and_coadd_paths(self) -> None:
        rows = [
            (1, "main", "dark", 12345),
            (2, "main", "dark", 12345),  # duplicate group, distinct TARGETID
            (3, "main", "bright", 12345),
            (4, "main", "dark", 999),
            (5, "sv3", "dark", 999),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            zcatalog_path = work / "zcatalog.fits"
            _write_synthetic_zcatalog(zcatalog_path, rows)
            digest = _sha256_file(zcatalog_path)
            manifest_path = work / "manifest.json"
            manifest_path.write_text(json.dumps({"catalog_sha256": digest}))
            output_path = work / "inventory.jsonl"

            written = inventory_tool.derive_inventory(zcatalog_path, manifest_path, output_path, chunk_rows=2)

            records = [json.loads(line) for line in written.read_text().splitlines()]
            self.assertEqual(len(records), 4)  # 4 unique (survey, program, healpix) groups

            keys = [(r["survey"], r["program"], r["healpix"]) for r in records]
            self.assertEqual(keys, sorted(keys))  # deterministic ascending order

            by_key = {(r["survey"], r["program"], r["healpix"]): r for r in records}
            self.assertEqual(
                by_key[("main", "dark", 12345)]["coadd_relative_path"],
                "healpix/main/dark/123/12345/coadd-main-dark-12345.fits",
            )
            self.assertEqual(by_key[("main", "dark", 12345)]["targetid_count"], 2)
            self.assertEqual(
                by_key[("main", "bright", 12345)]["coadd_relative_path"],
                "healpix/main/bright/123/12345/coadd-main-bright-12345.fits",
            )
            self.assertEqual(
                by_key[("main", "dark", 999)]["coadd_relative_path"],
                "healpix/main/dark/9/999/coadd-main-dark-999.fits",
            )
            self.assertEqual(by_key[("sv3", "dark", 999)]["targetid_count"], 1)

    def test_checksum_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            zcatalog_path = work / "zcatalog.fits"
            _write_synthetic_zcatalog(zcatalog_path, [(1, "main", "dark", 1)])
            manifest_path = work / "manifest.json"
            manifest_path.write_text(json.dumps({"catalog_sha256": "0" * 64}))
            with self.assertRaises(inventory_tool.LocatorDerivationError):
                inventory_tool.derive_inventory(
                    zcatalog_path, manifest_path, work / "inventory.jsonl", chunk_rows=10
                )

    def test_finalize_manifest_injects_real_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            inventory_path = work / "inventory.jsonl"
            inventory_path.write_text('{"a": 1}\n')
            draft_path = work / "draft.json"
            draft_path.write_text(
                json.dumps(
                    {
                        "catalog_sha256": "a" * 64,
                        "locator_inventory_sha256": "PENDING-POD-DERIVATION",
                        "_draft_note": "drop me",
                    }
                )
            )
            output_path = work / "final.json"
            manifest = inventory_tool.finalize_manifest(draft_path, inventory_path, output_path)
            self.assertNotIn("_draft_note", manifest)
            self.assertEqual(manifest["locator_inventory_sha256"], _sha256_file(inventory_path))
            self.assertNotEqual(manifest["locator_inventory_sha256"], "PENDING-POD-DERIVATION")


def _synthetic_row_indices_by_group(n_groups: int, base_count: int = 40, step: int = 7) -> dict:
    """Build a small synthetic (survey, program, healpix) -> row-index-array
    table standing in for the real zcatalog's per-group row indices, with
    deliberately unequal group sizes so PPS-vs-uniform selection and
    largest-remainder allocation are both meaningfully exercised."""
    table = {}
    cursor = 0
    for i in range(n_groups):
        survey = "main" if i % 2 == 0 else "sv3"
        program = "dark" if (i // 2) % 2 == 0 else "bright"
        healpix = 1000 + i
        count = base_count + (i * step) % 97  # unequal, deterministic group sizes
        table[(survey, program, healpix)] = np.arange(cursor, cursor + count, dtype=np.int64)
        cursor += count
    return table


class TwoStagePPSClusterSampleTest(unittest.TestCase):
    """Exercises the AUG-012 two-stage PPS cluster sample (replacing the
    original naive 40,000-uniform-row draw) against synthetic group tables
    scaled down from the production 200-of-~35,000-groups /
    40,000-of-~23M-rows design to a tractable 20-of-50 / 400-row analog."""

    N_GROUPS = 20
    N_ROWS = 400
    N_FIT = 200

    def test_selects_exact_group_count_from_more_available(self) -> None:
        table = _synthetic_row_indices_by_group(n_groups=50)
        counts_by_group = {g: len(rows) for g, rows in table.items()}
        rng, selected_groups, alloc = calibration_tool.select_pps_groups_and_allocate(
            counts_by_group, seed=calibration_tool.SEED, n_groups=self.N_GROUPS, n_rows=self.N_ROWS
        )
        self.assertEqual(len(selected_groups), self.N_GROUPS)
        self.assertEqual(len(set(selected_groups)), self.N_GROUPS)  # distinct groups
        self.assertEqual(selected_groups, sorted(selected_groups))  # ascending order

    def test_allocation_sums_exactly_to_row_budget(self) -> None:
        table = _synthetic_row_indices_by_group(n_groups=50)
        counts_by_group = {g: len(rows) for g, rows in table.items()}
        _rng, selected_groups, alloc = calibration_tool.select_pps_groups_and_allocate(
            counts_by_group, seed=calibration_tool.SEED, n_groups=self.N_GROUPS, n_rows=self.N_ROWS
        )
        self.assertEqual(len(alloc), self.N_GROUPS)
        self.assertEqual(sum(alloc), self.N_ROWS)  # exact total, largest-remainder rounding
        for group, k in zip(selected_groups, alloc):
            self.assertGreaterEqual(k, 0)
            self.assertLessEqual(k, len(table[group]))  # never exceeds a group's capacity

    def test_allocate_row_budget_respects_capacity_on_skewed_input(self) -> None:
        # A very small group next to much larger ones: largest-remainder
        # rounding must still land the tiny group at exactly its natural
        # share without exceeding its capacity.
        selected_counts = [2, 50, 50, 50]
        alloc = calibration_tool.allocate_row_budget(selected_counts, n_rows=140)
        self.assertEqual(sum(alloc), 140)
        for k, cap in zip(alloc, selected_counts):
            self.assertLessEqual(k, cap)
        self.assertEqual(alloc[0], 2)

    def test_allocate_row_budget_never_overflows_capacity(self) -> None:
        # Property fuzz test proving the invariant documented in
        # `allocate_row_budget`'s docstring: since `n_rows <=
        # sum(selected_counts)` is always enforced,
        # `proportional[i] <= selected_counts[i]` for every group, so
        # largest-remainder rounding can never push an allocation above a
        # group's capacity — the capacity-redistribution branch exists as
        # a defensive guard but is never expected to trigger in practice.
        rng = np.random.default_rng(1234)
        for _ in range(200):
            n = int(rng.integers(1, 12))
            counts = rng.integers(1, 5000, size=n).tolist()
            total = sum(counts)
            n_rows = int(rng.integers(0, total + 1))
            alloc = calibration_tool.allocate_row_budget(counts, n_rows)
            self.assertEqual(sum(alloc), n_rows)
            for k, cap in zip(alloc, counts):
                self.assertGreaterEqual(k, 0)
                self.assertLessEqual(k, cap)

    def test_deterministic_across_two_runs_same_seed(self) -> None:
        table = _synthetic_row_indices_by_group(n_groups=50)
        fit_a, val_a, groups_a, alloc_a = calibration_tool.draw_two_stage_pps_sample(
            table, seed=calibration_tool.SEED, n_groups=self.N_GROUPS, n_rows=self.N_ROWS, n_fit=self.N_FIT
        )
        fit_b, val_b, groups_b, alloc_b = calibration_tool.draw_two_stage_pps_sample(
            table, seed=calibration_tool.SEED, n_groups=self.N_GROUPS, n_rows=self.N_ROWS, n_fit=self.N_FIT
        )
        self.assertEqual(groups_a, groups_b)
        self.assertEqual(alloc_a, alloc_b)
        np.testing.assert_array_equal(fit_a, fit_b)
        np.testing.assert_array_equal(val_a, val_b)

    def test_fit_validation_disjoint_and_correct_sizes(self) -> None:
        table = _synthetic_row_indices_by_group(n_groups=50)
        fit_idx, val_idx, selected_groups, alloc = calibration_tool.draw_two_stage_pps_sample(
            table, seed=calibration_tool.SEED, n_groups=self.N_GROUPS, n_rows=self.N_ROWS, n_fit=self.N_FIT
        )
        self.assertEqual(len(fit_idx), self.N_FIT)
        self.assertEqual(len(val_idx), self.N_ROWS - self.N_FIT)
        self.assertTrue(set(fit_idx.tolist()).isdisjoint(set(val_idx.tolist())))
        self.assertEqual(len(set(fit_idx.tolist())), len(fit_idx))  # no duplicates within fit
        self.assertEqual(len(set(val_idx.tolist())), len(val_idx))  # no duplicates within validation

        # Every drawn row must actually belong to one of the selected groups.
        all_selected_rows = set()
        for group in selected_groups:
            all_selected_rows.update(table[group].tolist())
        self.assertTrue(set(fit_idx.tolist()) <= all_selected_rows)
        self.assertTrue(set(val_idx.tolist()) <= all_selected_rows)

    def test_refuses_more_groups_than_available(self) -> None:
        table = _synthetic_row_indices_by_group(n_groups=10)
        counts_by_group = {g: len(rows) for g, rows in table.items()}
        with self.assertRaises(calibration_tool.CalibrationError):
            calibration_tool.select_pps_groups_and_allocate(
                counts_by_group, seed=calibration_tool.SEED, n_groups=20, n_rows=self.N_ROWS
            )

    def test_refuses_oversized_row_budget(self) -> None:
        with self.assertRaises(calibration_tool.CalibrationError):
            calibration_tool.allocate_row_budget([5, 5, 5], n_rows=100)

    def test_production_defaults_are_self_consistent(self) -> None:
        self.assertEqual(calibration_tool.DEFAULT_N_GROUPS, 200)
        self.assertEqual(calibration_tool.DEFAULT_N_ROWS, 40_000)
        self.assertEqual(calibration_tool.DEFAULT_N_ROWS % 2, 0)
        self.assertEqual(calibration_tool.SAMPLING_DESIGN, "two-stage-pps-cluster/v2")


class AnomalyScoreArithmeticTest(unittest.TestCase):
    def test_matches_hand_computed_zscore_through_archived_bigae(self) -> None:
        import torch

        inference_module = calibration_tool.load_archived_inference_module()

        torch.manual_seed(20260804)
        model = inference_module.BigAE(n_in=496, n_lat=128)
        model.eval()

        rng = np.random.default_rng(7)
        n_spectra = 16
        raw_flux = rng.normal(loc=5.0, scale=3.0, size=(n_spectra, 496)).astype(np.float32)

        # Exactly enhanced_18M_inference.process_healpix's per-spectrum
        # median-|flux| normalization: med = median(|flux|), X = clip(flux/med, -10, 10).
        med = np.median(np.abs(raw_flux), axis=1, keepdims=True)
        med = np.where(med > 0, med, 1.0)
        X = np.clip(raw_flux / med, -10, 10)

        with torch.no_grad():
            batch = torch.from_numpy(X)
            recon = model(batch)
            residuals = (batch - recon) ** 2
            raw_mse = torch.mean(residuals, dim=1).numpy().astype(np.float64)

        # Accumulate mean/std in float64 so the z-score sanity check below
        # is not swamped by float32 rounding noise from the model itself.
        mse_mean = float(raw_mse.mean())
        mse_std = float(raw_mse.std(ddof=1))

        for value in raw_mse:
            expected = (float(value) - mse_mean) / mse_std
            observed = calibration_tool.anomaly_score_from_calibration(float(value), mse_mean, mse_std)
            self.assertAlmostEqual(observed, expected, places=12)

        scores = np.array(
            [calibration_tool.anomaly_score_from_calibration(float(v), mse_mean, mse_std) for v in raw_mse]
        )
        # A z-score population is exactly standardized by construction.
        self.assertAlmostEqual(float(scores.mean()), 0.0, places=9)
        self.assertAlmostEqual(float(scores.std(ddof=1)), 1.0, places=9)
        self.assertEqual(int(np.argmax(raw_mse)), int(np.argmax(scores)))


class ExportGroupTargetidsTest(unittest.TestCase):
    """`derive_locator_inventory.py export-group-targetids`: streams a
    synthetic zcatalog-like FITS table into a sorted
    (survey, program, healpix, targetid) Parquet file."""

    def test_writes_sorted_parquet_matching_zcatalog_rows(self) -> None:
        import pyarrow.parquet as pq

        rows = [
            (5, "main", "dark", 100),
            (1, "main", "dark", 100),
            (3, "main", "bright", 50),
            (2, "sv3", "dark", 50),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            zcatalog_path = work / "zcatalog.fits"
            _write_synthetic_zcatalog(zcatalog_path, rows)
            digest = _sha256_file(zcatalog_path)
            manifest_path = work / "manifest.json"
            manifest_path.write_text(json.dumps({"catalog_sha256": digest}))
            output_path = work / "group_targetids.parquet"

            written = inventory_tool.export_group_targetids(
                zcatalog_path, manifest_path, output_path, chunk_rows=2
            )
            self.assertTrue(written.is_file())
            printed_sha = inventory_tool.sha256_file(written)
            self.assertEqual(printed_sha, _sha256_file(written))
            self.assertEqual(len(printed_sha), 64)

            table = pq.read_table(written)
            self.assertEqual(table.num_rows, 4)
            self.assertEqual(set(table.schema.names), {"survey", "program", "healpix", "targetid"})
            records = table.to_pylist()
            keys = [(r["survey"], r["program"], r["healpix"], r["targetid"]) for r in records]
            self.assertEqual(keys, sorted(keys))  # deterministic ascending order
            self.assertEqual(
                keys,
                [
                    ("main", "bright", 50, 3),
                    ("main", "dark", 100, 1),
                    ("main", "dark", 100, 5),
                    ("sv3", "dark", 50, 2),
                ],
            )

    def test_checksum_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            zcatalog_path = work / "zcatalog.fits"
            _write_synthetic_zcatalog(zcatalog_path, [(1, "main", "dark", 1)])
            manifest_path = work / "manifest.json"
            manifest_path.write_text(json.dumps({"catalog_sha256": "0" * 64}))
            with self.assertRaises(inventory_tool.LocatorDerivationError):
                inventory_tool.export_group_targetids(
                    zcatalog_path, manifest_path, work / "group_targetids.parquet", chunk_rows=10
                )


class LoadGroupTargetidsTest(unittest.TestCase):
    """`run_scan.py`'s `load_group_targetids`: pyarrow predicate-pushdown
    read of a group's targetid set from the sorted Parquet export."""

    @staticmethod
    def _write_group_targetids_parquet(path: Path, rows: list[tuple[str, str, int, int]]) -> None:
        import pyarrow as pa
        import pyarrow.parquet as pq

        table = pa.table(
            {
                "survey": pa.array([r[0] for r in rows], type=pa.string()),
                "program": pa.array([r[1] for r in rows], type=pa.string()),
                "healpix": pa.array([r[2] for r in rows], type=pa.int64()),
                "targetid": pa.array([r[3] for r in rows], type=pa.int64()),
            }
        )
        table = table.sort_by(
            [
                ("survey", "ascending"),
                ("program", "ascending"),
                ("healpix", "ascending"),
                ("targetid", "ascending"),
            ]
        )
        pq.write_table(table, path)

    def test_loads_only_requested_groups(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "group_targetids.parquet"
            rows = [
                ("main", "dark", 100, 1),
                ("main", "dark", 100, 2),
                ("main", "bright", 50, 9),  # not requested
                ("cmx", "other", 2154, 42),
            ]
            self._write_group_targetids_parquet(path, rows)
            groups = [("main", "dark", 100), ("cmx", "other", 2154), ("sv3", "dark", 7)]  # zero rows in file
            result = run_scan_tool.load_group_targetids(path, groups)
            self.assertEqual(result[("main", "dark", 100)], {1, 2})
            self.assertEqual(result[("cmx", "other", 2154)], {42})
            self.assertEqual(result[("sv3", "dark", 7)], set())
            self.assertNotIn(("main", "bright", 50), result)

    def test_export_then_load_roundtrip(self) -> None:
        rows = [
            (5, "main", "dark", 100),
            (1, "main", "dark", 100),
            (3, "main", "bright", 50),
            (2, "sv3", "dark", 50),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            zcatalog_path = work / "zcatalog.fits"
            _write_synthetic_zcatalog(zcatalog_path, rows)
            digest = _sha256_file(zcatalog_path)
            manifest_path = work / "manifest.json"
            manifest_path.write_text(json.dumps({"catalog_sha256": digest}))
            output_path = work / "group_targetids.parquet"
            inventory_tool.export_group_targetids(zcatalog_path, manifest_path, output_path, chunk_rows=2)

            groups = [("main", "dark", 100), ("main", "bright", 50), ("sv3", "dark", 50)]
            loaded = run_scan_tool.load_group_targetids(output_path, groups)
            self.assertEqual(loaded[("main", "dark", 100)], {1, 5})
            self.assertEqual(loaded[("main", "bright", 50)], {3})
            self.assertEqual(loaded[("sv3", "dark", 50)], {2})


class PublicIdFirstFilterTest(unittest.TestCase):
    """`run_scan.py`'s `filter_group_to_zcatalog`: the public-ID-first scan
    filter that drops surplus coadd spectra with an honest audit trail,
    modeled directly on the AUG-011 smoke-test gap (group cmx/other/2154:
    139 zcatalog rows, 284 coadd spectra)."""

    def test_surplus_rows_dropped_and_kept_equals_intersection(self) -> None:
        scored_rows = [
            {"targetid": 1, "anomaly_score": 0.1, "mean_mse": 0.01},
            {"targetid": 2, "anomaly_score": 0.2, "mean_mse": 0.02},
            {"targetid": 3, "anomaly_score": 0.3, "mean_mse": 0.03},  # surplus: not in zcatalog
            {"targetid": 4, "anomaly_score": 0.4, "mean_mse": 0.04},  # surplus: not in zcatalog
        ]
        zcat_ids = {1, 2}  # both zcatalog ids have a spectrum in the coadd; 3, 4 are surplus
        kept_rows, audit = run_scan_tool.filter_group_to_zcatalog(scored_rows, zcat_ids, "cmx", "other", 2154)
        self.assertEqual({r["targetid"] for r in kept_rows}, {1, 2})
        self.assertEqual(
            audit,
            {
                "survey": "cmx",
                "program": "other",
                "healpix": 2154,
                "coadd_rows": 4,
                "zcat_rows": 2,
                "kept": 2,
                "surplus_dropped": 2,
                "zcat_missing_from_coadd": 0,
            },
        )

    def test_realistic_aug_011_gap_group_counts(self) -> None:
        # 139 zcatalog targetids, all present in a 284-row coadd (145 surplus).
        zcat_ids = set(range(1, 140))
        scored_rows = [{"targetid": i, "anomaly_score": 0.0, "mean_mse": 0.0} for i in range(1, 285)]
        kept_rows, audit = run_scan_tool.filter_group_to_zcatalog(scored_rows, zcat_ids, "cmx", "other", 2154)
        self.assertEqual(len(kept_rows), 139)
        self.assertEqual(audit["coadd_rows"], 284)
        self.assertEqual(audit["zcat_rows"], 139)
        self.assertEqual(audit["kept"], 139)
        self.assertEqual(audit["surplus_dropped"], 145)
        self.assertEqual(audit["zcat_missing_from_coadd"], 0)

    def test_fails_closed_on_zero_zcatalog_ids(self) -> None:
        with self.assertRaises(run_scan_tool.ScanError):
            run_scan_tool.filter_group_to_zcatalog(
                [{"targetid": 1, "anomaly_score": 0.1, "mean_mse": 0.01}], set(), "main", "dark", 1
            )

    def test_exactly_one_percent_missing_passes(self) -> None:
        zcat_ids = set(range(1, 101))  # 100 zcatalog ids
        scored_rows = [{"targetid": i, "anomaly_score": 0.0, "mean_mse": 0.0} for i in range(1, 100)]  # 99 rows
        kept_rows, audit = run_scan_tool.filter_group_to_zcatalog(scored_rows, zcat_ids, "main", "dark", 1)
        self.assertEqual(audit["zcat_missing_from_coadd"], 1)  # exactly 1/100 = 1%
        self.assertEqual(audit["kept"], 99)
        self.assertEqual(audit["surplus_dropped"], 0)

    def test_fails_closed_when_missing_fraction_exceeds_one_percent(self) -> None:
        zcat_ids = set(range(1, 101))  # 100 zcatalog ids
        scored_rows = [{"targetid": i, "anomaly_score": 0.0, "mean_mse": 0.0} for i in range(1, 98)]  # 97 rows -> 3 missing = 3%
        with self.assertRaises(run_scan_tool.ScanError):
            run_scan_tool.filter_group_to_zcatalog(scored_rows, zcat_ids, "main", "dark", 1)

    def test_fails_closed_on_kept_count_mismatch_from_duplicate_targetids(self) -> None:
        zcat_ids = {1, 2, 3}
        scored_rows = [
            {"targetid": 1, "anomaly_score": 0.0, "mean_mse": 0.0},
            {"targetid": 1, "anomaly_score": 0.0, "mean_mse": 0.0},  # duplicate targetid in coadd
            {"targetid": 2, "anomaly_score": 0.0, "mean_mse": 0.0},
            {"targetid": 3, "anomaly_score": 0.0, "mean_mse": 0.0},
        ]
        with self.assertRaises(run_scan_tool.ScanError):
            run_scan_tool.filter_group_to_zcatalog(scored_rows, zcat_ids, "main", "dark", 1)


class ScanAuditLogTest(unittest.TestCase):
    def test_append_audit_line_writes_exact_json_lines_without_truncating(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            audit_path = Path(tmp) / "nested" / "audit.jsonl"
            record_a = {
                "survey": "main",
                "program": "dark",
                "healpix": 1,
                "coadd_rows": 5,
                "zcat_rows": 5,
                "kept": 5,
                "surplus_dropped": 0,
                "zcat_missing_from_coadd": 0,
            }
            record_b = {
                "survey": "cmx",
                "program": "other",
                "healpix": 2154,
                "coadd_rows": 284,
                "zcat_rows": 139,
                "kept": 139,
                "surplus_dropped": 145,
                "zcat_missing_from_coadd": 0,
            }
            run_scan_tool.append_audit_line(audit_path, record_a)
            run_scan_tool.append_audit_line(audit_path, record_b)
            lines = audit_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(json.loads(lines[0]), record_a)
            self.assertEqual(json.loads(lines[1]), record_b)


if __name__ == "__main__":
    unittest.main()
