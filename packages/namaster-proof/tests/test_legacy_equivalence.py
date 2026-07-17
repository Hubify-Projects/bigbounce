from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

from namaster_proof import (
    bandpower_edges,
    build_rotation_response,
    field_harmonic_kwargs,
    rotate_eb_spectra,
    windowed_bandpowers,
)

ROOT = Path(__file__).resolve().parents[3]

_LEGACY_SCRIPTS = ROOT / "reproducibility" / "p1_namaster_500mc" / "scripts"
_WINDOWED_ROTATION = _LEGACY_SCRIPTS / "windowed_rotation.py"
_MULTIPOLE_CONTRACT = _LEGACY_SCRIPTS / "multipole_contract.py"

_MONOREPO_MISSING = not (_WINDOWED_ROTATION.exists() and _MULTIPOLE_CONTRACT.exists())
_MONOREPO_SKIP_REASON = (
    "requires bigbounce monorepo checkout for legacy-equivalence replay"
)


def load_legacy(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Workspace:
    def __init__(self) -> None:
        rng = np.random.default_rng(17)
        self.windows = rng.normal(size=(4, 3, 4, 12))

    def get_bandpower_windows(self):
        return self.windows


@pytest.mark.skipif(_MONOREPO_MISSING, reason=_MONOREPO_SKIP_REASON)
def test_window_operators_match_production_helpers() -> None:
    legacy = load_legacy(
        "legacy_windowed_rotation",
        "reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py",
    )
    workspace = Workspace()
    ee = np.linspace(0.0, 1.0, 12)
    bb = np.linspace(0.2, 0.0, 12)
    packaged = build_rotation_response(workspace, ee, bb)
    original = legacy.build_rotation_response(workspace, ee, bb)
    for beta in (-0.03, 0.0, 0.07):
        np.testing.assert_allclose(
            windowed_bandpowers(packaged, beta),
            legacy.windowed_bandpowers(original, beta),
            rtol=0,
            atol=0,
        )
    cls = np.arange(48, dtype=float).reshape(4, 12)
    np.testing.assert_allclose(
        rotate_eb_spectra(cls, 0.02),
        legacy.rotate_eb_spectra(cls, 0.02),
        rtol=0,
        atol=0,
    )


@pytest.mark.skipif(_MONOREPO_MISSING, reason=_MONOREPO_SKIP_REASON)
def test_multipole_contract_matches_production_helper() -> None:
    legacy = load_legacy(
        "legacy_multipole_contract",
        "reproducibility/p1_namaster_500mc/scripts/multipole_contract.py",
    )
    np.testing.assert_array_equal(
        bandpower_edges(nside=256, lmax=512, n_bins=10),
        legacy.bandpower_edges(nside=256, lmax=512, n_bins=10),
    )
    assert field_harmonic_kwargs(
        lmax=512, purify_b=True
    ) == legacy.field_harmonic_kwargs(lmax=512, purify_b=True)
