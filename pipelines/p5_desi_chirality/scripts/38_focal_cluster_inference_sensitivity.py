#!/usr/bin/env python3
"""Deterministic low-dimensional and wild-cluster sensitivity for P5's focal arm."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
from pathlib import Path

import numpy as np
import pandas as pd
import patsy
import scipy
import scipy.special


P5 = Path(__file__).resolve().parents[1]
REPO = P5.parents[1]
SOURCE = P5 / "scripts/36_desivast_native_selection_control.py"
ROWS = P5 / "outputs/36_desivast_native_selection_rows.parquet"
FOCAL = P5 / "outputs/36_desivast_native_selection_control.json"
OUTPUT = P5 / "outputs/38_focal_cluster_inference_sensitivity.json"
SEED = 20260715
WILD_DRAWS = 99_999


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_control_module():
    spec = importlib.util.spec_from_file_location("p5_a37", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def nonconstant_design(formula: str, frame: pd.DataFrame) -> pd.DataFrame:
    design = patsy.dmatrix(formula, frame, return_type="dataframe")
    return design.loc[:, [
        column == "Intercept" or design[column].nunique(dropna=False) > 1
        for column in design
    ]]


def main() -> int:
    control = load_control_module()
    frame = control.prepare_analysis(pd.read_parquet(ROWS))
    formula = (
        "void + desi_z + r_mag + log_shape_r + confidence_eq + ebv + "
        "C(photsys) + C(morphtype) + galzone_edge"
    )
    xdf = nonconstant_design(formula, frame)
    x = xdf.to_numpy(float)
    y = frame["cw"].to_numpy(float)
    beta, solver = control.fit_unpenalized_logit(x, y)
    groups = frame["angular_block_nside4"].to_numpy()
    covariance, sandwich = control.cluster_sandwich(x, y, beta, groups)
    marginal = control.marginal_result(
        x, beta, covariance, xdf.columns.get_loc("void")
    )

    # Null-imposed Rademacher wild-cluster efficient-score bootstrap. The
    # nuisance model is re-estimated under H0 and the exposure is projected off
    # nuisance in the fitted Bernoulli information metric.
    zdf = nonconstant_design(formula.replace("void + ", ""), frame)
    z = zdf.to_numpy(float)
    beta0, null_solver = control.fit_unpenalized_logit(z, y)
    p0 = scipy.special.expit(z @ beta0)
    weights = p0 * (1.0 - p0)
    exposure = frame["void"].to_numpy(float)
    projection = np.linalg.pinv(
        z.T @ (weights[:, None] * z), rcond=1e-11, hermitian=True,
    ) @ (z.T @ (weights * exposure))
    efficient_exposure = exposure - z @ projection
    scores = efficient_exposure * (y - p0)
    unique_groups, inverse = np.unique(groups, return_inverse=True)
    cluster_scores = np.bincount(inverse, weights=scores)
    denominator = float(np.sqrt(np.sum(cluster_scores ** 2)))
    observed = float(cluster_scores.sum() / denominator)
    rng = np.random.default_rng(SEED)
    extreme = 0
    for start in range(0, WILD_DRAWS, 10_000):
        count = min(10_000, WILD_DRAWS - start)
        signs = rng.choice((-1.0, 1.0), size=(count, len(unique_groups)))
        simulated = signs @ cluster_scores / denominator
        extreme += int(np.count_nonzero(np.abs(simulated) >= abs(observed)))
    wild_p = (extreme + 1.0) / (WILD_DRAWS + 1.0)

    focal = json.loads(FOCAL.read_text(encoding="utf-8"))["primary_out_zero"]
    payload = {
        "schema": "p5.focal-cluster-inference-sensitivity/v1",
        "purpose": (
            "rank-robustness sensitivity for the focal hybrid released-parent "
            "estimand; does not replace the prespecified focal 78-column estimate"
        ),
        "command": "python3 pipelines/p5_desi_chirality/scripts/38_focal_cluster_inference_sensitivity.py",
        "seed": SEED,
        "input_sha256": {
            str(ROWS.relative_to(REPO)): sha256_file(ROWS),
            str(SOURCE.relative_to(REPO)): sha256_file(SOURCE),
            str(FOCAL.relative_to(REPO)): sha256_file(FOCAL),
            str(Path(__file__).resolve().relative_to(REPO)): sha256_file(Path(__file__).resolve()),
        },
        "original_focal_model_caution": {
            "n": focal["adjusted_logistic"]["n_rows"],
            "k": focal["adjusted_logistic"]["n_design_columns"],
            "clusters": focal["adjusted_logistic"]["coarse_healpix_nside4"]["sandwich"]["n_clusters"],
            "note": "K=78 exceeds G=50; ordinary CR1 normal inference can be fragile even though the scalar result is reproducible.",
        },
        "reduced_cr1": {
            "formula": formula,
            "n": len(frame),
            "k": x.shape[1],
            "design_rank": int(np.linalg.matrix_rank(x)),
            "clusters": len(unique_groups),
            "delta_nonvoid_minus_void": marginal["average_marginal_delta_nonvoid_minus_void"],
            "se": marginal["se"],
            "ci95": marginal["ci95"],
            "normal_p_two_sided": marginal["p_two_sided"],
            "sandwich": sandwich,
            "solver": solver,
        },
        "null_imposed_rademacher_wild_cluster_score": {
            "cluster_unit": "HEALPix NSIDE=4",
            "draws": WILD_DRAWS,
            "seed": SEED,
            "observed_score_t": observed,
            "p_two_sided": wild_p,
            "null_solver": null_solver,
        },
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__, "pandas": pd.__version__,
            "patsy": patsy.__version__, "scipy": scipy.__version__,
        },
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
