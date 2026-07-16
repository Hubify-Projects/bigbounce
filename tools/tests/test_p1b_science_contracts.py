from __future__ import annotations

import json
import hashlib
import tempfile
from pathlib import Path

import pytest

from tools.verify_p1b_science_contracts import verify


def fixture(root: Path) -> dict[str, str]:
    paths = {
        "manuscript": "paper.tex",
        "namaster_summary": "namaster.json",
        "namaster_c10_receipt": "c10.json",
        "namaster_declared_receipt": "declared.json",
        "bbn_execution_receipt": "bbn.json",
        "s8_overlay_receipt": "s8.json",
        "analysis_manifest": "manifest.json",
    }
    (root / "paper.tex").write_text(
        "\\newcommand{\\paperVersion}{v2}\nThe full-$EB$ limitation is retained.\n"
    )
    (root / "namaster.json").write_text(json.dumps({
        "run_mode": "production",
        "n_mc_realizations": 500,
        "physical_spectra": {
            "generator": "CAMB",
            "expected_camb_version": "1.6.6",
            "resolved_camb_version": "1.6.6",
            "production_version_match": True,
            "contract": {"raw_cl": True},
            "sha256": {
                "cl_ee_raw_uK2": "a" * 64,
                "cl_bb_raw_uK2": "b" * 64,
            },
            "validation": {
                "status": "pass",
                "raw_cl_ee_at_ell_check_uK2": 0.0003,
            },
        },
        "window_equivalence_max_abs": 1e-12,
    }))
    for filename, suite in (
        ("c10.json", "c10_merged"),
        ("declared.json", "declared_fsky_sign_merged"),
    ):
        (root / filename).write_text(json.dumps({
            "suite": suite,
            "n_real": 500,
            "seed_start": 42,
            "seed_end": 541,
            "result_sha256": "d" * 64,
        }))
    (root / "bbn.json").write_text(json.dumps({
        "status": "PASS",
        "camb_version": "1.6.5",
        "executed_table": "PRIMAT_Yp_DH_ErrorMC_2021.dat",
        "executed_table_sha256": "c" * 64,
        "public_yaml_setting": "PRIMAT_Yp_DH_ErrorMC_2021.dat",
        "validated_configs": [
            {
                "path": f"config-{index}.yaml",
                "sha256": hashlib.sha256(f"config-{index}".encode()).hexdigest(),
                "bbn_predictor": "PRIMAT_Yp_DH_ErrorMC_2021.dat",
            }
            for index in range(4)
        ],
    }))
    for index in range(4):
        (root / f"config-{index}.yaml").write_text(f"config-{index}")
    s8_result = root / "s8-result.json"
    s8_result.write_text("{}")
    (root / "s8.json").write_text(json.dumps({
        "status": "PASS",
        "burn_in_fraction": 0.30,
        "raw_samples": 1000,
        "post_burn_samples": 700,
        "result_file": s8_result.name,
        "result_sha256": hashlib.sha256(s8_result.read_bytes()).hexdigest(),
    }))
    (root / "manifest.json").write_text(json.dumps({"paper_version": "v2"}))
    return paths


def test_accepts_complete_contract():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        result = verify(root, fixture(root))
        assert result["verdict"] == "PASS"
        assert all(result["contracts"].values())


@pytest.mark.parametrize(
    ("filename", "field", "value", "message"),
    [
        ("bbn.json", "public_yaml_setting", "PArthENoPE", "public YAML"),
        ("s8.json", "burn_in_fraction", 0.0, "30 percent"),
        ("manifest.json", "paper_version", "v1", "does not match"),
    ],
)
def test_rejects_reviewed_regressions(filename, field, value, message):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = fixture(root)
        path = root / filename
        payload = json.loads(path.read_text())
        payload[field] = value
        path.write_text(json.dumps(payload))
        with pytest.raises(ValueError, match=message):
            verify(root, paths)


def test_rejects_unsupported_prior_edge_wording():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = fixture(root)
        (root / "paper.tex").write_text(
            "\\newcommand{\\paperVersion}{v2}\n"
            "The full-$EB$ limitation is retained and the mass piles toward the upper edge.\n"
        )
        with pytest.raises(ValueError, match="prior-edge"):
            verify(root, paths)


def test_rejects_manifest_matching_only_historical_version_text():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = fixture(root)
        (root / "paper.tex").write_text(
            "% prior release v1\n"
            "\\newcommand{\\paperVersion}{v2}\n"
            "The full-$EB$ limitation is retained.\n"
        )
        (root / "manifest.json").write_text(json.dumps({"paper_version": "v1"}))
        with pytest.raises(ValueError, match="does not match"):
            verify(root, paths)


def test_rejects_d_ell_like_namaster_summary():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paths = fixture(root)
        path = root / "namaster.json"
        payload = json.loads(path.read_text())
        payload["physical_spectra"]["contract"]["raw_cl"] = False
        path.write_text(json.dumps(payload))
        with pytest.raises(ValueError, match="raw C_ell"):
            verify(root, paths)
