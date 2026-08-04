"""Bounded local smoke test; never downloads DESI spectra or runs inference."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "pipelines/p1_highz_tracers/clean_rerun_contract.py"
SPEC = importlib.util.spec_from_file_location("clean_rerun_contract", MODULE_PATH)
assert SPEC and SPEC.loader
contract_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contract_tool)


class CleanRerunContractSmokeTest(unittest.TestCase):
    def test_local_model_contract_receipt_dedup_and_comparison(self) -> None:
        try:
            import pyarrow as pa
            import pyarrow.parquet as pq
        except ImportError as exc:  # pragma: no cover - environment prerequisite
            self.skipTest(f"pyarrow unavailable: {exc}")

        digest = "a" * 64
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            input_manifest = {
                "manifest_version": "desi-dr1-clean-rerun-input/v1",
                "source_revision": "iron",
                "catalog_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
                "catalog_checksum_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum",
                "catalog_sha256": digest,
                "targetid_column": "TARGETID",
                "spectrum_locator": {"type": "desi_dr1_iron_healpix", "base_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/"},
                "locator_inventory_sha256": "b" * 64,
            }
            calibration = {
                "artifact_version": "desi-bigae-calibration/v1",
                "status": "sealed",
                "score_definition": "mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins",
                "fit_scope": "held_out_training_validation_split",
                "mse_mean": 0.1,
                "mse_std": 0.02,
                "selection_threshold": 5.0,
                "training_manifest_sha256": "c" * 64,
                "validation_manifest_sha256": "d" * 64,
                "fit_code_sha256": "e" * 64,
            }
            input_path, calibration_path = work / "input.json", work / "calibration.json"
            input_path.write_text(json.dumps(input_manifest))
            calibration_path.write_text(json.dumps(calibration))
            contract = contract_tool.build_contract(
                ROOT / "best_model_47k.pt",
                ROOT / "pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py",
                input_path,
                calibration_path,
            )
            contract_path = work / "contract.json"
            contract_tool.write_json_atomic(contract_path, contract)

            shard_dir = work / "shards"
            shard_dir.mkdir()
            shard = shard_dir / "part-000.parquet"
            pq.write_table(pa.table({"targetid": [1, 1, 2], "anomaly_score": [4.0, 6.0, 7.0]}), shard)
            receipt_dir, checkpoint = work / "receipts", work / "checkpoint.json"
            contract_tool.record_receipt(contract_path, shard, receipt_dir, checkpoint)
            self.assertEqual(contract_tool.verify_receipts(contract_path, shard_dir, receipt_dir), [shard])

            summary = contract_tool.summarize_after_dedup(
                contract_path, shard_dir, receipt_dir, work / "dedup.sqlite", work / "summary.json"
            )
            self.assertEqual(summary["raw_rows"], 3)
            self.assertEqual(summary["unique_targetids"], 2)
            self.assertEqual(summary["threshold_count_after_dedup"], 2)
            comparison = contract_tool.compare_generations(work / "summary.json", work / "comparison.json")
            self.assertEqual(comparison["policy"], "separate_generations_only_no_count_targeting_or_merging")

    def test_missing_calibration_fails_closed(self) -> None:
        with self.assertRaises(contract_tool.ContractError):
            contract_tool.build_contract(ROOT / "best_model_47k.pt", MODULE_PATH, Path("missing-input.json"), Path("missing-calibration.json"))


if __name__ == "__main__":
    unittest.main()
