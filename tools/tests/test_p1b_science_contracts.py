from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from tools.verify_p1b_science_contracts import verify


def fixture(root: Path) -> dict[str, str]:
    paths = {
        "manuscript": "paper.tex",
        "namaster_physical_spectrum_receipt": "namaster.json",
        "bbn_execution_receipt": "bbn.json",
        "s8_overlay_receipt": "s8.json",
        "analysis_manifest": "manifest.json",
    }
    (root / "paper.tex").write_text(
        "\\newcommand{\\paperVersion}{v2}\nThe full-$EB$ limitation is retained.\n"
    )
    (root / "namaster.json").write_text(json.dumps({
        "status": "PASS",
        "spectrum_convention": "raw_C_ell",
        "ee_source": "CAMB",
        "bb_source": "CAMB_lensed",
        "production_realizations": 500,
        "spectrum_sha256": {"EE": "a" * 64, "BB": "b" * 64},
    }))
    (root / "bbn.json").write_text(json.dumps({
        "status": "PASS",
        "camb_version": "1.6.5",
        "executed_table": "PRIMAT_Yp_DH_Error.dat",
        "executed_table_sha256": "c" * 64,
        "public_yaml_setting": "PRIMAT_Yp_DH_Error.dat",
    }))
    (root / "s8.json").write_text(json.dumps({
        "status": "PASS",
        "burn_in_fraction": 0.30,
        "raw_samples": 1000,
        "post_burn_samples": 700,
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
        ("namaster.json", "spectrum_convention", "D_ell", "raw C_ell"),
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
