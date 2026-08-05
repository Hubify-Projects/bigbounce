"""Offline unit tests for the AUG-011 clean-rerun campaign scaffold.

No network access; no full-scale DESI download. Covers only the pure,
locally-computable pieces of the campaign under
`pipelines/p1_highz_tracers/clean_rerun/`:

  - inventory path-construction and grouping rules, against a synthetic
    zcatalog-like FITS table;
  - the deterministic 40,000/20,000/20,000 seeded split;
  - the anomaly-score arithmetic, run through the real archived `BigAE`
    class (imported unmodified from `enhanced_18M_inference.py`) with a
    fixed-seed state dict, against a hand-computed z-score.
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


class SeededSplitTest(unittest.TestCase):
    def test_deterministic_and_disjoint(self) -> None:
        n_rows = 100_000
        drawn_a = calibration_tool.draw_seeded_indices(n_rows)
        drawn_b = calibration_tool.draw_seeded_indices(n_rows)
        np.testing.assert_array_equal(drawn_a, drawn_b)  # same seed -> same draw
        self.assertEqual(len(drawn_a), calibration_tool.N_TOTAL_SAMPLE)
        self.assertEqual(len(set(drawn_a.tolist())), calibration_tool.N_TOTAL_SAMPLE)  # no duplicates

        fit_idx, val_idx = calibration_tool.split_fit_validation(drawn_a)
        self.assertEqual(len(fit_idx), calibration_tool.N_FIT)
        self.assertEqual(len(val_idx), calibration_tool.N_TOTAL_SAMPLE - calibration_tool.N_FIT)
        self.assertTrue(set(fit_idx.tolist()).isdisjoint(set(val_idx.tolist())))
        np.testing.assert_array_equal(np.concatenate([fit_idx, val_idx]), drawn_a)

        # Matches the documented API call directly: Generator(PCG64(seed=20260804)).choice(...)
        rng = np.random.Generator(np.random.PCG64(calibration_tool.SEED))
        expected = rng.choice(n_rows, size=calibration_tool.N_TOTAL_SAMPLE, replace=False)
        np.testing.assert_array_equal(drawn_a, expected)

    def test_refuses_oversized_draw(self) -> None:
        with self.assertRaises(calibration_tool.CalibrationError):
            calibration_tool.draw_seeded_indices(n_rows=100, n_total=40_000)


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


if __name__ == "__main__":
    unittest.main()
