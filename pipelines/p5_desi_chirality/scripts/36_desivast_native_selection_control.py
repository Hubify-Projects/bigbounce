#!/usr/bin/env python3
"""Catalog-native DESIVAST selection-function and covariate control.

This closure analysis restricts the frozen P5 chirality parent to TARGETIDs in
the released DESIVAST V2/REVOLVER ``GALZONE`` tables.  Those tables are the
catalog-native volume-limited BGS input used by DESIVAST and therefore provide
the strongest *released* representation of its angular/quality/volume
selection.  The DESIVAST repository's actual smoothed mask FITS references
internal NERSC paths and is not part of the public VAC; this script does not
invent or reverse-engineer randoms.

The primary adjusted estimand is the average marginal difference

    f_CW(non-void) - f_CW(void)

from a logistic outcome model spanning redshift, angular block/cap, imaging
leg, r-band magnitude, size, morphology, extinction, classifier confidence,
and the released GALZONE edge flag.  Inference uses a sandwich covariance
clustered by the nearest DESIVAST VoidFinder maximal-void centre.  A bounded
overlap-weighted estimator is reported as a propensity-control sensitivity;
its sandwich treats fitted overlap weights as fixed and is not promoted over
the adjusted outcome model.

Run from the repository root:

  nice -n 5 python3 \
    pipelines/p5_desi_chirality/scripts/36_desivast_native_selection_control.py
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import warnings
from pathlib import Path

import healpy as hp
import numpy as np
import pandas as pd
import patsy
import scipy
import scipy.special
import statsmodels.api as sm
from astropy.io import fits
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning


P5 = Path(__file__).resolve().parents[1]
REPO = P5.parents[1]
SCRIPT35 = P5 / "scripts/35_desivast_cluster_bootstrap.py"
CACHE = P5 / "outputs/35_exact_primary_rows_cache.parquet"
ZALL = P5 / "data/desi_zall.fits"
P4 = P5 / "data/p4_chirality.parquet"
DESIVAST = P5 / "data/desivast"
ROWS_OUT = P5 / "outputs/36_desivast_native_selection_rows.parquet"
RESULT_OUT = P5 / "outputs/36_desivast_native_selection_control.json"
MANIFEST_OUT = P5 / "outputs/36_desivast_native_selection_manifest.json"

DESIVAST_REPO_COMMIT = "11bebc66a5ba62e4f51c6afcc06bd3a62aa6c048"
DESIVAST_REPO_URL = "https://github.com/hbrincon/DESIVAST"
DESIVAST_VAC_URL = "https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/"
DESIVAST_DOC_URL = "https://data.desi.lbl.gov/doc/releases/dr1/vac/desivast/"
LSS_V15_URL = (
    "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/"
    "LSScats/v1.5/"
)
EXPECTED_NATIVE_ROWS = 145_789
EXPECTED_OUT_ZERO_ROWS = 145_766
CHUNK = 1_000_000
ANG_NSIDE = 4


def sha256_file(path: Path, chunk_bytes: int = 16 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(chunk_bytes):
            digest.update(block)
    return digest.hexdigest()


def load_script35():
    spec = importlib.util.spec_from_file_location("p5_script35", SCRIPT35)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SCRIPT35}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def native(values: np.ndarray) -> np.ndarray:
    array = np.asarray(values)
    if array.dtype.byteorder not in ("=", "|"):
        array = array.astype(array.dtype.newbyteorder("="))
    return array


def decode(values: np.ndarray) -> np.ndarray:
    return np.char.strip(native(values).astype("U"))


def load_galzone() -> pd.DataFrame:
    parts: list[pd.DataFrame] = []
    for cap in ["NGC", "SGC"]:
        path = DESIVAST / f"DESIVAST_BGS_VOLLIM_V2_REVOLVER_{cap}.fits"
        with fits.open(path, memmap=True) as hdul:
            data = hdul["GALZONE"].data
            part = pd.DataFrame({
                "desi_targetid": native(data["TARGET"]).astype(np.int64),
                "galzone_zone": native(data["ZONE"]).astype(np.int32),
                "galzone_depth": native(data["DEPTH"]).astype(np.int16),
                "galzone_edge": native(data["EDGE"]).astype(np.int8),
                "galzone_out": native(data["OUT"]).astype(np.int8),
                "galzone_x": native(data["X"]).astype(np.float64),
                "galzone_y": native(data["Y"]).astype(np.float64),
                "galzone_z": native(data["Z"]).astype(np.float64),
            })
            part["cap"] = cap
            parts.append(part)
    frame = pd.concat(parts, ignore_index=True)
    if len(frame) != 694_642 or frame["desi_targetid"].nunique() != len(frame):
        raise RuntimeError("released GALZONE TARGET universe is not the expected 694,642 unique rows")
    return frame


def extract_zall_covariates(targetids: np.ndarray, cached_z: dict[int, float]) -> pd.DataFrame:
    """Stream zall and select one deterministic row per requested TARGETID."""
    wanted = np.sort(np.asarray(targetids, dtype=np.int64))
    pieces: list[pd.DataFrame] = []
    cols = [
        "TARGETID", "Z", "SURVEY", "PROGRAM", "ZCAT_PRIMARY", "MAIN_PRIMARY",
        "PHOTSYS", "MORPHTYPE", "FLUX_R", "SHAPE_R", "EBV", "MASKBITS",
        "COADD_NUMTILE", "DELTACHI2", "TSNR2_BGS",
    ]
    with fits.open(ZALL, memmap=True) as hdul:
        data = hdul["ZCATALOG"].data
        for start in range(0, len(data), CHUNK):
            stop = min(start + CHUNK, len(data))
            block = data[start:stop]
            ids = native(block["TARGETID"]).astype(np.int64)
            keep = np.isin(ids, wanted, assume_unique=False)
            if not keep.any():
                continue
            idx = np.flatnonzero(keep)
            piece: dict[str, np.ndarray] = {"desi_targetid": ids[idx]}
            for col in cols[1:]:
                values = block[col][idx]
                if np.asarray(values).dtype.kind in "SU":
                    piece[col.lower()] = decode(values)
                else:
                    piece[col.lower()] = native(values)
            piece["zall_row"] = start + idx
            pieces.append(pd.DataFrame(piece))
    matches = pd.concat(pieces, ignore_index=True)
    matches["cached_z"] = matches["desi_targetid"].map(cached_z)
    matches["z_distance"] = np.abs(matches["z"].astype(float) - matches["cached_z"])
    # Prefer the canonical zcat/main row, then the row whose redshift exactly
    # matches the frozen historical parent, then original FITS order.
    matches = matches.sort_values(
        ["desi_targetid", "zcat_primary", "main_primary", "z_distance", "zall_row"],
        ascending=[True, False, False, True, True],
        kind="mergesort",
    ).drop_duplicates("desi_targetid", keep="first")
    if len(matches) != len(wanted):
        missing = len(wanted) - len(matches)
        raise RuntimeError(f"zall covariate join missed {missing} DESIVAST-native TARGETIDs")
    return matches.drop(columns=["cached_z", "z_distance"])


def load_classifier_confidence(dr8_ids: np.ndarray) -> pd.DataFrame:
    import pyarrow.dataset as ds

    wanted = np.asarray(dr8_ids).astype(str).tolist()
    # Arrow performs the 8.47M-row projection/filter in compiled code; avoid a
    # Python-level astype(str) over the entire 908 MB source.
    dataset = ds.dataset(P4, format="parquet")
    table = dataset.to_table(
        columns=["dr8_id", "confidence_eq"],
        filter=ds.field("dr8_id").isin(wanted),
    )
    p4 = table.to_pandas()
    p4["dr8_id"] = p4["dr8_id"].astype(str)
    if p4["dr8_id"].duplicated().any():
        raise RuntimeError("P4 dr8_id is not unique")
    return p4.rename(columns={"dr8_id": "match_dr8_id"})


def assign_environment(frame: pd.DataFrame, s35) -> pd.DataFrame:
    holes, maximals, cluster_ids = s35.load_void_geometry()
    xyz, _ = s35.galaxy_xyz(frame)
    frame = frame.copy()
    frame["void"] = s35.exact_union_membership(xyz, holes).astype(np.int8)
    from scipy.spatial import cKDTree
    _, nearest = cKDTree(maximals[:, :3]).query(xyz, k=1)
    frame["vf_cluster_id"] = cluster_ids[nearest].astype(np.int32)
    frame["vf_cluster_distance_mpc_h"] = np.linalg.norm(
        xyz - maximals[nearest, :3], axis=1
    )
    theta = np.deg2rad(90.0 - frame["desi_dec"].to_numpy(float))
    phi = np.deg2rad(np.mod(frame["desi_ra"].to_numpy(float), 360.0))
    frame["angular_block_nside4"] = hp.ang2pix(ANG_NSIDE, theta, phi).astype(np.int16)
    return frame


def prepare_analysis(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame[frame["galzone_out"] == 0].copy()
    if len(out) != EXPECTED_OUT_ZERO_ROWS:
        raise RuntimeError(f"expected {EXPECTED_OUT_ZERO_ROWS:,} OUT=0 rows, got {len(out):,}")
    out["cw"] = (out["match_class_eq"] == "CW").astype(np.int8)
    flux = out["flux_r"].astype(float)
    shape = out["shape_r"].astype(float)
    out["r_mag"] = np.where(flux > 0.0, 22.5 - 2.5 * np.log10(flux), np.nan)
    out["log_shape_r"] = np.log1p(np.clip(shape, 0.0, None))
    out["morphtype"] = out["morphtype"].astype(str).str.strip().replace("", "UNKNOWN")
    out["photsys"] = out["photsys"].astype(str).str.strip().replace("", "UNKNOWN")
    out["cap"] = out["cap"].astype(str)
    # Median imputation is restricted to continuous nuisance covariates and is
    # recorded explicitly.  It does not alter outcome, exposure, or position.
    for col in ["r_mag", "log_shape_r", "ebv", "confidence_eq"]:
        out[f"{col}_missing"] = out[col].isna().astype(np.int8)
        out[col] = out[col].astype(float).fillna(out[col].astype(float).median())
    return out


FORMULA = (
    "void + bs(desi_z, df=5, degree=3, include_intercept=False) + "
    "bs(r_mag, df=4, degree=3, include_intercept=False) + "
    "bs(log_shape_r, df=4, degree=3, include_intercept=False) + "
    "bs(confidence_eq, df=4, degree=3, include_intercept=False) + "
    "bs(ebv, df=4, degree=3, include_intercept=False) + "
    "C(angular_block_nside4) + C(photsys) + C(morphtype) + "
    "galzone_edge + r_mag_missing + log_shape_r_missing + ebv_missing + "
    "confidence_eq_missing"
)


def design(frame: pd.DataFrame) -> pd.DataFrame:
    matrix = patsy.dmatrix(FORMULA, frame, return_type="dataframe")
    # Missingness indicators are retained in the formula but are algebraically
    # zero when the frozen parent has no missing values; EDGE is likewise zero
    # in the EDGE=0 sensitivity.  Remove only constant-zero nuisance columns.
    # The intercept remains.  C(cap) is intentionally absent because cap is an
    # exact linear combination of the non-overlapping angular-block dummies.
    dropped = [
        col for col in matrix.columns
        if col != "Intercept" and matrix[col].nunique(dropna=False) <= 1
    ]
    matrix = matrix.drop(columns=dropped)
    matrix.attrs["dropped_constant_columns"] = dropped
    return matrix


def crude(frame: pd.DataFrame) -> dict:
    void = frame[frame["void"] == 1]
    nonvoid = frame[frame["void"] == 0]
    pv = float(void["cw"].mean())
    pn = float(nonvoid["cw"].mean())
    delta = pn - pv
    se = math.sqrt(pv * (1 - pv) / len(void) + pn * (1 - pn) / len(nonvoid))
    pooled = float(frame["cw"].mean())
    se0 = math.sqrt(pooled * (1 - pooled) * (1 / len(void) + 1 / len(nonvoid)))
    z = delta / se0
    return {
        "void": {"n": len(void), "n_cw": int(void["cw"].sum()), "f_cw": pv},
        "nonvoid": {"n": len(nonvoid), "n_cw": int(nonvoid["cw"].sum()), "f_cw": pn},
        "delta_nonvoid_minus_void": delta,
        "independent_binomial_se": se,
        "independent_binomial_ci95": [delta - 1.959963984540054 * se,
                                       delta + 1.959963984540054 * se],
        "pooled_z": z,
        "p_two_sided": float(2 * stats.norm.sf(abs(z))),
    }


def fit_unpenalized_logit(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, dict]:
    # Centre/scale every nonconstant column for the optimizer, then map the
    # fitted coefficients exactly back to the original design basis.
    means = x.mean(axis=0)
    scales = x.std(axis=0)
    intercept_candidates = np.flatnonzero(scales == 0.0)
    if len(intercept_candidates) != 1 or not np.allclose(x[:, intercept_candidates[0]], 1.0):
        raise RuntimeError("design must contain exactly one constant intercept column")
    intercept_index = int(intercept_candidates[0])
    means[intercept_index] = 0.0
    scales[intercept_index] = 1.0
    scaled = (x - means) / scales
    rank = int(np.linalg.matrix_rank(scaled.T @ scaled))
    if rank != x.shape[1]:
        raise RuntimeError(f"adjusted design remains rank deficient: rank {rank}/{x.shape[1]}")
    estimator = LogisticRegression(
        penalty=None,
        solver="newton-cholesky",
        fit_intercept=False,
        max_iter=100,
        tol=1e-10,
    )
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ConvergenceWarning)
        estimator.fit(scaled, y)
    convergence_warnings = [str(w.message) for w in caught
                            if issubclass(w.category, ConvergenceWarning)]
    beta_scaled = estimator.coef_.ravel()
    beta = beta_scaled / scales
    beta[intercept_index] -= float(np.sum(beta_scaled * means / scales))
    mu = scipy.special.expit(x @ beta)
    mean_score = x.T @ (y - mu) / len(y)
    return beta, {
        "solver": "scikit-learn unpenalized LogisticRegression/Newton-Cholesky",
        "iterations": int(estimator.n_iter_[0]),
        "converged": not convergence_warnings,
        "convergence_warnings": convergence_warnings,
        "design_rank": rank,
        "n_design_columns": x.shape[1],
        "scaled_gram_condition_number": float(np.linalg.cond(scaled.T @ scaled)),
        "max_absolute_mean_score_original_basis": float(np.max(np.abs(mean_score))),
        "coefficient_mapping": "optimizer basis centred/scaled; coefficients mapped back exactly",
    }


def cluster_sandwich(x: np.ndarray, y: np.ndarray, beta: np.ndarray,
                     groups: np.ndarray) -> tuple[np.ndarray, dict]:
    """Finite-sample corrected one-way cluster sandwich for logit MLE."""
    mu = scipy.special.expit(x @ beta)
    weight = mu * (1.0 - mu)
    bread_matrix = x.T @ (weight[:, None] * x)
    rank = int(np.linalg.matrix_rank(bread_matrix))
    bread = np.linalg.pinv(bread_matrix, rcond=1e-11, hermitian=True)
    unique, inverse = np.unique(groups, return_inverse=True)
    scores = x * (y - mu)[:, None]
    order = np.argsort(inverse, kind="mergesort")
    ordered_groups = inverse[order]
    starts = np.r_[0, 1 + np.flatnonzero(np.diff(ordered_groups))]
    cluster_scores = np.add.reduceat(scores[order], starts, axis=0)
    meat = cluster_scores.T @ cluster_scores
    n, p = x.shape
    g = len(unique)
    correction = (g / (g - 1.0)) * ((n - 1.0) / (n - rank))
    covariance = correction * bread @ meat @ bread
    return covariance, {
        "n_clusters": g,
        "finite_sample_correction": float(correction),
        "bread_rank": rank,
        "n_design_columns": p,
        "bread_condition_number": float(np.linalg.cond(bread_matrix)),
        "bread_inverse": "Moore-Penrose pseudoinverse, rcond=1e-11",
    }


def marginal_result(x: np.ndarray, beta: np.ndarray, covariance: np.ndarray,
                    void_index: int, row_mask: np.ndarray | None = None) -> dict:
    selected = np.ones(len(x), dtype=bool) if row_mask is None else row_mask
    x0 = x[selected].copy()
    x1 = x[selected].copy()
    x0[:, void_index] = 0.0
    x1[:, void_index] = 1.0
    p0 = scipy.special.expit(x0 @ beta)
    p1 = scipy.special.expit(x1 @ beta)
    delta = float(np.mean(p0 - p1))
    gradient = np.mean(
        p0[:, None] * (1 - p0[:, None]) * x0
        - p1[:, None] * (1 - p1[:, None]) * x1,
        axis=0,
    )
    se = float(np.sqrt(np.maximum(gradient @ covariance @ gradient, 0.0)))
    z = delta / se
    return {
        "average_marginal_delta_nonvoid_minus_void": delta,
        "se": se,
        "ci95": [delta - 1.959963984540054 * se,
                   delta + 1.959963984540054 * se],
        "z": z,
        "p_two_sided": float(2 * stats.norm.sf(abs(z))),
    }


def adjusted_logistic(frame: pd.DataFrame, x: pd.DataFrame) -> dict:
    matrix = x.to_numpy(float)
    y = frame["cw"].to_numpy(float)
    beta, solver = fit_unpenalized_logit(matrix, y)
    void_index = x.columns.get_loc("void")
    covariance_vf, vf_meta = cluster_sandwich(
        matrix, y, beta, frame["vf_cluster_id"].to_numpy()
    )
    covariance_sky, sky_meta = cluster_sandwich(
        matrix, y, beta, frame["angular_block_nside4"].to_numpy()
    )
    nearest = marginal_result(matrix, beta, covariance_vf, void_index)
    coarse = marginal_result(matrix, beta, covariance_sky, void_index)
    cap_results = {}
    for cap in ["NGC", "SGC"]:
        mask = frame["cap"].to_numpy() == cap
        cap_results[cap] = {
            "n": int(mask.sum()),
            "standardized_with_shared_full_model_nearest_maximals_covariance":
                marginal_result(matrix, beta, covariance_vf, void_index, mask),
            "crude": crude(frame.loc[mask]),
        }
    void_coef = float(beta[void_index])
    void_se_vf = float(np.sqrt(max(covariance_vf[void_index, void_index], 0.0)))
    void_se_sky = float(np.sqrt(max(covariance_sky[void_index, void_index], 0.0)))
    conservative = nearest if nearest["se"] >= coarse["se"] else coarse
    conservative_name = (
        "nearest_voidfinder_maximals" if nearest["se"] >= coarse["se"]
        else "coarse_healpix_nside4"
    )
    return {
        "model": "binomial GLM with logit link",
        "solver": solver,
        "covariance": (
            "explicit finite-sample one-way cluster sandwich; same fitted beta "
            "evaluated under nearest-MAXIMALS and coarse NSIDE=4 sky blocks"
        ),
        "n_rows": len(frame),
        "n_design_columns": x.shape[1],
        "dropped_constant_columns": x.attrs.get("dropped_constant_columns", []),
        "formula": FORMULA,
        "void_log_odds_coefficient": void_coef,
        "void_odds_ratio": float(np.exp(void_coef)),
        "void_log_odds_se": {
            "nearest_voidfinder_maximals": void_se_vf,
            "coarse_healpix_nside4": void_se_sky,
        },
        "nearest_voidfinder_maximals": {**nearest, "sandwich": vf_meta},
        "coarse_healpix_nside4": {**coarse, "sandwich": sky_meta},
        "conservative_of_reported_cluster_sandwiches": {
            "selected": conservative_name,
            **conservative,
        },
        "cap_standardized_results": cap_results,
    }


def standardized_mean_difference(x: np.ndarray, exposure: np.ndarray,
                                 weights: np.ndarray | None = None) -> np.ndarray:
    values = np.asarray(x, dtype=float)
    e = np.asarray(exposure, dtype=bool)
    w = np.ones(len(e), dtype=float) if weights is None else np.asarray(weights, dtype=float)
    result = []
    for col in range(values.shape[1]):
        a, b = values[e, col], values[~e, col]
        wa, wb = w[e], w[~e]
        ma = np.average(a, weights=wa)
        mb = np.average(b, weights=wb)
        va = np.average((a - ma) ** 2, weights=wa)
        vb = np.average((b - mb) ** 2, weights=wb)
        denom = np.sqrt((va + vb) / 2)
        result.append(0.0 if denom == 0 else (ma - mb) / denom)
    return np.asarray(result)


def overlap_weighted(frame: pd.DataFrame, x: pd.DataFrame) -> dict:
    exposure = frame["void"].to_numpy(np.int8)
    xp = x.drop(columns=["void"]).to_numpy(float)
    means = xp.mean(axis=0)
    scales = xp.std(axis=0)
    constant = scales == 0.0
    means[constant] = 0.0
    scales[constant] = 1.0
    xp_scaled = (xp - means) / scales
    propensity_estimator = LogisticRegression(
        C=10.0,
        solver="newton-cholesky",
        max_iter=100,
        tol=1e-10,
        fit_intercept=False,
    )
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ConvergenceWarning)
        propensity_estimator.fit(xp_scaled, exposure)
    propensity_warnings = [
        str(w.message) for w in caught if issubclass(w.category, ConvergenceWarning)
    ]
    score = propensity_estimator.predict_proba(xp_scaled)[:, 1]
    weights = np.where(exposure == 1, 1.0 - score, score)
    y = frame["cw"].to_numpy(float)
    design2 = np.column_stack([np.ones(len(frame)), exposure.astype(float)])
    bread_matrix = design2.T @ (weights[:, None] * design2)
    beta = np.linalg.solve(bread_matrix, design2.T @ (weights * y))

    def weighted_sandwich(groups: np.ndarray) -> tuple[np.ndarray, dict]:
        residual = y - design2 @ beta
        scores = design2 * (weights * residual)[:, None]
        unique, inverse = np.unique(groups, return_inverse=True)
        order = np.argsort(inverse, kind="mergesort")
        starts = np.r_[0, 1 + np.flatnonzero(np.diff(inverse[order]))]
        u = np.add.reduceat(scores[order], starts, axis=0)
        meat = u.T @ u
        n, p = design2.shape
        g = len(unique)
        correction = (g / (g - 1.0)) * ((n - 1.0) / (n - p))
        bread = np.linalg.inv(bread_matrix)
        return correction * bread @ meat @ bread, {
            "n_clusters": g,
            "finite_sample_correction": float(correction),
        }

    cov_vf, vf_meta = weighted_sandwich(frame["vf_cluster_id"].to_numpy())
    cov_sky, sky_meta = weighted_sandwich(frame["angular_block_nside4"].to_numpy())
    # WLS coefficient is void-minus-nonvoid; report the manuscript convention.
    delta = -float(beta[1])
    se_vf = float(np.sqrt(max(cov_vf[1, 1], 0.0)))
    se_sky = float(np.sqrt(max(cov_sky[1, 1], 0.0)))

    def inference(se: float) -> dict:
        z = delta / se
        return {
            "delta_nonvoid_minus_void": delta,
            "se": se,
            "ci95": [delta - 1.959963984540054 * se,
                       delta + 1.959963984540054 * se],
            "z": z,
            "p_two_sided": float(2 * stats.norm.sf(abs(z))),
        }
    smd_before = standardized_mean_difference(xp, exposure)
    smd_after = standardized_mean_difference(xp, exposure, weights)
    return {
        "role": "bounded overlap-weighted propensity sensitivity; fitted weights treated as fixed",
        "propensity_model": "L2 logistic regression on the same nuisance design matrix",
        "propensity_solver": {
            "solver": "scikit-learn LogisticRegression/Newton-Cholesky",
            "iterations": int(propensity_estimator.n_iter_[0]),
            "converged": not propensity_warnings,
            "convergence_warnings": propensity_warnings,
            "scaled_design": True,
            "C": 10.0,
        },
        "weight_definition": "void: 1-e(x); nonvoid: e(x)",
        "propensity_quantiles": {
            str(q): float(np.quantile(score, q))
            for q in [0.0, 0.01, 0.05, 0.5, 0.95, 0.99, 1.0]
        },
        "weight_quantiles": {
            str(q): float(np.quantile(weights, q))
            for q in [0.0, 0.01, 0.05, 0.5, 0.95, 0.99, 1.0]
        },
        "effective_n": {
            "void": float(weights[exposure == 1].sum() ** 2 /
                          np.sum(weights[exposure == 1] ** 2)),
            "nonvoid": float(weights[exposure == 0].sum() ** 2 /
                             np.sum(weights[exposure == 0] ** 2)),
        },
        "max_absolute_design_smd_before": float(np.max(np.abs(smd_before))),
        "max_absolute_design_smd_after": float(np.max(np.abs(smd_after))),
        "nearest_voidfinder_maximals": {**inference(se_vf), "sandwich": vf_meta},
        "coarse_healpix_nside4": {**inference(se_sky), "sandwich": sky_meta},
    }


def fit_specification(frame: pd.DataFrame) -> dict:
    x = design(frame)
    return {
        "crude": crude(frame),
        "adjusted_logistic": adjusted_logistic(frame, x),
        "overlap_weighted_sensitivity": overlap_weighted(frame, x),
    }


def validate_efficient_inference(frame: pd.DataFrame, x: pd.DataFrame) -> dict:
    """Bounded equivalence check against statsmodels IRLS + cluster covariance."""
    # Use a deterministic, evenly spaced subset and a reduced full-rank design.
    idx = np.linspace(0, len(frame) - 1, 5_000, dtype=int)
    candidate = [
        col for col in x.columns
        if col in {"Intercept", "void", "galzone_edge"}
        or col.startswith("bs(desi_z")
        or col.startswith("bs(r_mag")
        or col.startswith("bs(log_shape_r")
        or col.startswith("bs(confidence_eq")
        or col.startswith("bs(ebv")
    ]
    xv = x.iloc[idx][candidate].to_numpy(float)
    yv = frame.iloc[idx]["cw"].to_numpy(float)
    groups = frame.iloc[idx]["angular_block_nside4"].to_numpy()
    beta_fast, solver = fit_unpenalized_logit(xv, yv)
    cov_fast, sandwich_meta = cluster_sandwich(xv, yv, beta_fast, groups)
    reference = sm.GLM(yv, xv, family=sm.families.Binomial()).fit(
        maxiter=200,
        tol=1e-10,
        wls_method="pinv",
        cov_type="cluster",
        cov_kwds={"groups": groups, "use_correction": True},
    )
    pred_fast = scipy.special.expit(xv @ beta_fast)
    pred_reference = reference.predict(xv)
    se_fast = np.sqrt(np.maximum(np.diag(cov_fast), 0.0))
    se_reference = np.asarray(reference.bse)
    return {
        "purpose": (
            "bounded numerical validation of unpenalized Newton-Cholesky MLE and explicit "
            "finite-sample cluster sandwich against statsmodels GLM IRLS"
        ),
        "n_rows": len(idx),
        "n_columns": len(candidate),
        "columns": candidate,
        "cluster_unit": "HEALPix NSIDE=4",
        "fast_solver": solver,
        "reference_converged": bool(reference.converged),
        "max_absolute_prediction_difference": float(np.max(np.abs(pred_fast - pred_reference))),
        "max_absolute_coefficient_difference": float(np.max(np.abs(beta_fast - reference.params))),
        "max_absolute_standard_error_difference": float(np.max(np.abs(se_fast - se_reference))),
        "max_relative_standard_error_difference": float(
            np.max(np.abs(se_fast - se_reference) / np.maximum(se_reference, 1e-15))
        ),
        "explicit_sandwich": sandwich_meta,
    }


def canonical_rows_hash(frame: pd.DataFrame) -> str:
    ordered = frame.sort_values(["desi_targetid", "match_dr8_id"], kind="mergesort")
    digest = hashlib.sha256()
    columns = [
        "desi_targetid", "desi_ra", "desi_dec", "desi_z", "match_class_eq",
        "match_dr8_id", "void", "vf_cluster_id", "galzone_zone", "galzone_edge",
        "galzone_out", "cap", "program", "photsys", "morphtype", "flux_r",
        "shape_r", "ebv", "confidence_eq",
    ]
    for col in columns:
        digest.update(col.encode("utf-8") + b"\0")
        for value in ordered[col].astype(str):
            encoded = value.encode("utf-8")
            digest.update(len(encoded).to_bytes(4, "little"))
            digest.update(encoded)
    return digest.hexdigest()


def main() -> int:
    s35 = load_script35()
    parser = argparse.ArgumentParser()
    parser.add_argument("--force-row-rebuild", action="store_true")
    args = parser.parse_args()
    if ROWS_OUT.exists() and not args.force_row_rebuild:
        rows = pd.read_parquet(ROWS_OUT)
        if len(rows) != EXPECTED_NATIVE_ROWS:
            raise RuntimeError(f"cached archive has {len(rows):,} rows, expected {EXPECTED_NATIVE_ROWS:,}")
        row_source = "reused previously frozen row archive"
    else:
        frozen = pd.read_parquet(CACHE)
        galzone = load_galzone()
        rows = frozen.merge(galzone, on="desi_targetid", how="inner", validate="one_to_one")
        if len(rows) != EXPECTED_NATIVE_ROWS:
            raise RuntimeError(f"expected {EXPECTED_NATIVE_ROWS:,} native rows, got {len(rows):,}")
        cached_z = dict(zip(rows["desi_targetid"].astype(int), rows["desi_z"].astype(float)))
        zall = extract_zall_covariates(rows["desi_targetid"].to_numpy(), cached_z)
        rows = rows.merge(zall, on="desi_targetid", how="left", validate="one_to_one")
        confidence = load_classifier_confidence(rows["match_dr8_id"].to_numpy())
        rows = rows.merge(confidence, on="match_dr8_id", how="left", validate="many_to_one")
        rows = assign_environment(rows, s35)
        rows = rows.sort_values(
            ["desi_targetid", "match_dr8_id"], kind="mergesort"
        ).reset_index(drop=True)
        ROWS_OUT.parent.mkdir(parents=True, exist_ok=True)
        rows.to_parquet(ROWS_OUT, index=False, compression="zstd")
        row_source = "rebuilt and frozen before model fitting"
    analysis = prepare_analysis(rows)
    validation_design = design(analysis)
    efficient_validation = validate_efficient_inference(analysis, validation_design)
    primary = fit_specification(analysis)
    no_edge = fit_specification(analysis[analysis["galzone_edge"] == 0].copy())

    rows_hash = canonical_rows_hash(rows)
    row_file_hash = sha256_file(ROWS_OUT)

    source_paths = [
        CACHE, ZALL, P4, SCRIPT35, Path(__file__),
        DESIVAST / "DESIVAST_BGS_VOLLIM_VoidFinder_NGC.fits",
        DESIVAST / "DESIVAST_BGS_VOLLIM_VoidFinder_SGC.fits",
        DESIVAST / "DESIVAST_BGS_VOLLIM_V2_REVOLVER_NGC.fits",
        DESIVAST / "DESIVAST_BGS_VOLLIM_V2_REVOLVER_SGC.fits",
    ]
    source_hashes = {str(path.relative_to(REPO)): sha256_file(path) for path in source_paths}
    result = {
        "schema": "p5.desivast-native-selection-control.v1",
        "estimand": "f_CW(non-void) - f_CW(void) within released DESIVAST GALZONE TARGET universe",
        "void_definition": "exact point-in-union of 101,863 released VoidFinder hole spheres",
        "selection_control": {
            "definition": (
                "intersection of frozen P5 chirality parent and unique TARGETIDs in the "
                "released DESIVAST V2/REVOLVER GALZONE tables"
            ),
            "released_galzone_target_count": 694_642,
            "frozen_parent_overlap": len(rows),
            "out_zero_primary_rows": len(analysis),
            "out_one_excluded_rows": int((rows["galzone_out"] != 0).sum()),
            "honest_limitation": (
                "The exact DESIVAST smoothed-mask FITS and its construction inputs are "
                "not in the public VAC; public repository code references internal NERSC "
                "paths. GALZONE membership is the strongest exact released selection proxy."
            ),
            "later_lss_v15_not_substituted": (
                "The DR1 LSS v1.5 BGS_BRIGHT-21.5 clustering catalog is a later/different "
                "product with only 15,378 frozen-parent TARGETID overlaps and would change "
                "the estimand; it is provenance context, not an analysis input."
            ),
        },
        "primary_out_zero": primary,
        "sensitivity_out_zero_and_edge_zero": no_edge,
        "efficient_inference_validation": efficient_validation,
        "row_archive": {
            "path": str(ROWS_OUT.relative_to(REPO)),
            "rows": len(rows),
            "sha256_file": row_file_hash,
            "sha256_canonical_scientific_content": rows_hash,
            "cluster_assignment": "nearest namespaced DESIVAST VoidFinder MAXIMALS centre in comoving Mpc/h",
            "construction_this_run": row_source,
        },
        "source_sha256": source_hashes,
        "source_hash_scope": (
            "Hashes cover only the four DESIVAST FITS products actually read: two "
            "VoidFinder files for holes/MAXIMALS and two REVOLVER files for GALZONE. "
            "VIDE and other unused catalog files are intentionally not represented as inputs."
        ),
        "official_provenance": {
            "desivast_vac": DESIVAST_VAC_URL,
            "desivast_documentation": DESIVAST_DOC_URL,
            "desivast_public_code": DESIVAST_REPO_URL,
            "desivast_public_code_commit": DESIVAST_REPO_COMMIT,
            "desi_lss_v1_5_context_only": LSS_V15_URL,
        },
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scipy": scipy.__version__,
            "statsmodels": sm.__version__,
            "patsy": patsy.__version__,
        },
        "command": (
            "nice -n 5 python3 pipelines/p5_desi_chirality/scripts/"
            "36_desivast_native_selection_control.py"
        ),
        "release_state": (
            "No immutable tag/DOI is asserted by this computation. Root integration must "
            "commit, tag, push, and archive the exact script/rows/result/PDF atomically."
        ),
    }
    RESULT_OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    manifest = {
        "schema": "p5.desivast-native-selection-manifest.v1",
        "command": result["command"],
        "artifacts": {
            str(ROWS_OUT.relative_to(REPO)): sha256_file(ROWS_OUT),
            str(RESULT_OUT.relative_to(REPO)): sha256_file(RESULT_OUT),
        },
        "source_sha256": source_hashes,
        "official_provenance": result["official_provenance"],
        "release_state": result["release_state"],
    }
    MANIFEST_OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "rows": len(rows),
        "primary": primary["adjusted_logistic"],
        "overlap": primary["overlap_weighted_sensitivity"],
        "edge_zero": no_edge["adjusted_logistic"],
        "validation": efficient_validation,
        "row_sha256": row_file_hash,
        "result_sha256": sha256_file(RESULT_OUT),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
