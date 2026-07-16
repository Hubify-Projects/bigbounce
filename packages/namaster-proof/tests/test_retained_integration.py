from __future__ import annotations

from pathlib import Path

import pytest

from namaster_proof import validate_json_receipt


def test_retained_real_pymaster_integration_receipt():
    result = (
        Path(__file__).resolve().parents[1]
        / "examples"
        / "pymaster_integration_result.json"
    )
    payload, _ = validate_json_receipt(
        result,
        expected={
            "suite": "namaster-proof-pymaster-integration-v1",
            "pymaster_version": "2.6",
            "deterministic": True,
        },
    )
    assert payload["exact_recovered_beta_deg"] == pytest.approx(0.25)
    assert payload["exact_operator_equivalence_max_abs"] < 1e-10
    assert payload["effective_ell_shortcut_recovered_beta_deg"] == pytest.approx(
        0.315
    )
