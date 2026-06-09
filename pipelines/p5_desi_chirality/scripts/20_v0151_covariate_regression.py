#!/usr/bin/env python3
"""P5 v0.1.51 — C5 covariate regression (R22prov truth-audit work order).

Closes the last open R22prov item: a logistic regression of the CW label on
cosmic-web environment class WITH galaxy-property covariates, to show the
environmental-independence null is robust to selection in galaxy properties
(size / inclination / apparent magnitude / morphology), not just to the
sky-position + redshift + classifier-confidence covariates already fitted in
outputs/17_v0151_closure_recomputes.json (META-m3).

Covariate source (resolved 2026-06-09): Galaxy Zoo DESI (Walmsley et al.
2023, MNRAS 526, 4768), Zenodo record 8360385 — the same catalog the P4
paper cites as its coordinate source, keyed on dr8_id = "{brickid}_{objid}":

  gz_desi_deep_learning_catalog_friendly.parquet  (8.7M rows, morphology
      vote-fraction predictions: smooth/featured, edge-on, merging, ...)
  external_catalog.parquet  (est_petro_th50 [arcsec, estimated Petrosian
      half-light radius from Legacy photometry], mag_r/g/z_desi [Legacy
      DR8 apparent magnitudes])

Both files are cached under data/gz_desi/ (gitignored, provenance sidecar
written by this script). Download with:

  curl -L -C - -o data/gz_desi/<name> \
      https://zenodo.org/records/8360385/files/<name>

Regression spec
---------------
Parent sample: the declared P5 parent — matched_primary_deduped CW/CCW
spirals from results/p5_matched_chirality_desi.parquet (n = 791,635;
identical to parent_catalog_matched in script 17).

Outcome: y = 1 if match_class_eq == "CW".

Environment: canonical V-Web labels (data/desi_env/desi_env_vweb.parquet)
and, in a second pass, the z-shell selection-corrected labels
(data/desi_env/desi_env_vweb_zshell.parquet, script 16). Env tables carry
duplicate TARGETIDs (repeat zall coadd rows); they are deduplicated to
unique TARGETID before the join, and the (rare) TARGETIDs with conflicting
labels are counted and DROPPED.

Treatment coding: env dummies for void / wall / cluster with FILAMENT (the
largest class) as the reference category. Each env coefficient is the
log-odds difference in P(CW) for that class vs filament.

Models (per label set). The disk-edge-on vote fraction is only defined for
~20% of the parent (the GZ decision tree only reaches that question for
confidently featured galaxies; it is NaN otherwise), so two covariate sets
are fitted, each with an env-only counterpart on the SAME rows so the
with/without comparison is apples-to-apples:
  M0   env dummies only, on the full env-labeled sample (baseline)
  MA1/MB1  env only / env + covariates EXCLUDING edge_on_frac, on the
       sample complete in those covariates (~100% of the parent)
  MA2/MB2  env only / env + ALL covariates INCLUDING edge_on_frac, on the
       edge-on-complete subsample (~20% of the parent; honest caveat)

Covariates (continuous ones z-scored on the fit sample so the IRLS Hessian
is well conditioned; env-dummy coefficients are unaffected in meaning):
  z_desi                 spectroscopic redshift
  match_confidence       P4 classifier confidence
  log10_radius           log10(est_petro_th50 / arcsec)   [size]
  mag_r                  mag_r_desi                       [apparent magnitude]
  featured_frac          smooth-or-featured_featured-or-disk_fraction
                                                          [morphology proxy]
  edge_on_frac           disk-edge-on_yes_fraction        [axis-ratio /
                                                           inclination proxy]
  merger_frac            1 - merging_none_fraction        [disturbance proxy]

Fit: IRLS Newton logistic (same implementation pattern as script 17
META-m3; no statsmodels dependency). Wald per-coefficient z/p and a joint
3-dof Wald chi^2 on the env block (the headline "is environment null"
test, before vs after covariate adjustment).

Output: outputs/20_v0151_covariate_regression.json
"""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

P5 = Path(__file__).resolve().parents[1]
MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
ENV_CANON = P5 / "data/desi_env/desi_env_vweb.parquet"
ENV_ZSHELL = P5 / "data/desi_env/desi_env_vweb_zshell.parquet"
GZ_DIR = P5 / "data/gz_desi"
GZ_FRIENDLY = GZ_DIR / "gz_desi_deep_learning_catalog_friendly.parquet"
GZ_EXTERNAL = GZ_DIR / "external_catalog.parquet"
OUT = P5 / "outputs/20_v0151_covariate_regression.json"

ZENODO_RECORD = "8360385"
ZENODO_BASE = f"https://zenodo.org/records/{ZENODO_RECORD}/files"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
ENV_REF = "filament"
ENV_DUMMIES = [c for c in ENV_ORDER if c != ENV_REF]

FRIENDLY_COLS = [
    "dr8_id",
    "smooth-or-featured_smooth_fraction",
    "smooth-or-featured_featured-or-disk_fraction",
    "disk-edge-on_yes_fraction",
    "merging_none_fraction",
]
EXTERNAL_COLS = ["dr8_id", "est_petro_th50", "mag_r_desi"]

COVARIATES = ["z_desi", "match_confidence", "log10_radius", "mag_r",
              "featured_frac", "edge_on_frac", "merger_frac"]
COVARIATES_NOEDGE = [c for c in COVARIATES if c != "edge_on_frac"]


def sha256_head(path: Path, n_bytes: int = 64 * 1024 * 1024) -> str:
    """SHA-256 of the first n_bytes (full-file hash of 1.6 GB is slow;
    head-hash + size is sufficient as a cache-integrity fingerprint)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read(n_bytes))
    return h.hexdigest()


def fit_logistic(X: np.ndarray, y: np.ndarray, names: list[str]) -> dict:
    """IRLS Newton logistic regression (pattern of script 17 META-m3)."""
    beta = np.zeros(X.shape[1])
    H = None
    for _ in range(50):
        eta = X @ beta
        mu = 1.0 / (1.0 + np.exp(-eta))
        w = mu * (1.0 - mu)
        H = X.T @ (X * w[:, None])
        g = X.T @ (y - mu)
        step_v = np.linalg.solve(H, g)
        beta = beta + step_v
        if np.max(np.abs(step_v)) < 1e-10:
            break
    cov = np.linalg.inv(H)
    se = np.sqrt(np.diag(cov))
    out = {
        "n": int(len(y)),
        "n_cw": int(y.sum()),
        "coefficients": {
            nm: {"coef": float(b), "se": float(s), "z": float(b / s),
                 "p": float(2 * stats.norm.sf(abs(b / s)))}
            for nm, b, s in zip(names, beta, se)
        },
    }
    # joint Wald chi^2 on the env-dummy block
    env_idx = [i for i, nm in enumerate(names) if nm.startswith("env_")]
    if env_idx:
        b_env = beta[env_idx]
        c_env = cov[np.ix_(env_idx, env_idx)]
        w2 = float(b_env @ np.linalg.solve(c_env, b_env))
        dof = len(env_idx)
        out["env_joint_wald"] = {
            "chi2": w2, "dof": dof,
            "p": float(stats.chi2.sf(w2, dof)),
        }
    return out


def design(df: pd.DataFrame, covariates: list[str]):
    """Build (X, names). Continuous covariates are z-scored on df."""
    cols = [np.ones(len(df))]
    names = ["intercept"]
    for c in ENV_DUMMIES:
        cols.append((df["env_class"] == c).to_numpy(float))
        names.append(f"env_{c}_vs_{ENV_REF}")
    scaling = {}
    for c in covariates:
        v = df[c].to_numpy(float)
        m, s = float(np.mean(v)), float(np.std(v))
        cols.append((v - m) / s)
        names.append(c)
        scaling[c] = {"mean": m, "std": s}
    return np.column_stack(cols), names, scaling


def fit_pair(d: pd.DataFrame, covariates: list[str]) -> dict:
    """Env-only + env+covariates pair on the covariate-complete rows of d,
    with per-env-dummy coefficient shifts."""
    cc_mask = np.ones(len(d), dtype=bool)
    for c in covariates:
        cc_mask &= np.isfinite(d[c].to_numpy(float))
    dcc = d[cc_mask]
    y = (dcc["match_class_eq"] == "CW").to_numpy(float)
    Xa, na, _ = design(dcc, [])
    Xb, nb, scaling = design(dcc, covariates)
    res = {
        "covariates": covariates,
        "n_covariate_complete": int(len(dcc)),
        "covariate_complete_fraction": float(len(dcc) / len(d)),
        "per_class_n": dcc["env_class"].value_counts().to_dict(),
        "covariate_scaling_zscore": scaling,
        "env_only": fit_logistic(Xa, y, na),
        "env_plus_covariates": fit_logistic(Xb, y, nb),
    }
    shifts = {}
    for c in ENV_DUMMIES:
        nm = f"env_{c}_vs_{ENV_REF}"
        a = res["env_only"]["coefficients"][nm]
        b = res["env_plus_covariates"]["coefficients"][nm]
        shifts[nm] = {
            "coef_without": a["coef"], "coef_with": b["coef"],
            "abs_shift": abs(b["coef"] - a["coef"]),
            "shift_in_se_units": abs(b["coef"] - a["coef"]) / a["se"],
        }
    res["env_coef_shift_after_adjustment"] = shifts
    return res


def main() -> int:
    t0 = time.time()
    for p in (GZ_FRIENDLY, GZ_EXTERNAL):
        if not p.exists():
            raise SystemExit(
                f"missing {p} — download from {ZENODO_BASE}/{p.name}")

    out: dict = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/20_v0151_covariate_regression.py",
        "closes": ["R22prov C5 (covariate regression)"],
        "covariate_source": {
            "catalog": "Galaxy Zoo DESI (Walmsley et al. 2023, MNRAS 526, 4768)",
            "zenodo_record": ZENODO_RECORD,
            "files": {
                p.name: {
                    "url": f"{ZENODO_BASE}/{p.name}",
                    "bytes": p.stat().st_size,
                    "sha256_first_64MiB": sha256_head(p),
                } for p in (GZ_FRIENDLY, GZ_EXTERNAL)
            },
            "join_key": "dr8_id ('{brickid}_{objid}') == matched-catalog match_dr8_id",
        },
    }

    # ---- parent: declared matched-spiral parent (same as script 17) ----
    cols = ["desi_targetid", "match_dr8_id", "match_class_eq",
            "match_confidence", "desi_z", "matched_primary_deduped"]
    matched = pd.read_parquet(MATCHED, columns=cols)
    sp = matched[matched["matched_primary_deduped"]
                 & matched["match_class_eq"].isin(["CW", "CCW"])].copy()
    del matched
    out["parent"] = {
        "definition": "matched_primary_deduped & match_class_eq in {CW,CCW}",
        "n": int(len(sp)),
        "n_unique_dr8_id": int(sp["match_dr8_id"].nunique()),
    }

    # ---- GZ DESI covariates, joined on dr8_id ----
    gz_f = pd.read_parquet(GZ_FRIENDLY, columns=FRIENDLY_COLS)
    gz_e = pd.read_parquet(GZ_EXTERNAL, columns=EXTERNAL_COLS)
    gz = gz_f.merge(gz_e, on="dr8_id", how="outer")
    del gz_f, gz_e
    gz = gz.drop_duplicates("dr8_id")
    sp = sp.merge(gz, left_on="match_dr8_id", right_on="dr8_id", how="left")
    del gz

    sp["featured_frac"] = sp["smooth-or-featured_featured-or-disk_fraction"]
    sp["edge_on_frac"] = sp["disk-edge-on_yes_fraction"]
    sp["merger_frac"] = 1.0 - sp["merging_none_fraction"]
    with np.errstate(invalid="ignore", divide="ignore"):
        sp["log10_radius"] = np.log10(
            sp["est_petro_th50"].where(sp["est_petro_th50"] > 0))
    sp["mag_r"] = sp["mag_r_desi"]
    sp["z_desi"] = sp["desi_z"]

    n_parent = len(sp)
    out["join_coverage"] = {
        "n_parent": n_parent,
        "matched_any_gz_row": float(sp["dr8_id"].notna().mean()),
        "per_covariate_finite": {
            c: float(np.isfinite(sp[c].to_numpy(float)).mean())
            for c in COVARIATES
        },
    }

    # ---- env label sets ----
    label_sets = {
        "canonical": ENV_CANON,
        "zshell_corrected": ENV_ZSHELL,
    }
    results = {}
    for tag, env_path in label_sets.items():
        env = pd.read_parquet(env_path, columns=["TARGETID", "env_class"])
        env["env_class"] = env["env_class"].astype(str)
        # dedup to unique TARGETID; drop the (rare) conflicting-label IDs
        nuniq = env.groupby("TARGETID")["env_class"].nunique()
        conflict_ids = set(nuniq[nuniq > 1].index)
        env = env.drop_duplicates("TARGETID")
        env = env[~env["TARGETID"].isin(conflict_ids)]
        d = sp.merge(env, left_on="desi_targetid", right_on="TARGETID",
                     how="inner")
        del env

        y_full = (d["match_class_eq"] == "CW").to_numpy(float)
        X0, n0, _ = design(d, [])
        res = {
            "env_label_file": env_path.name,
            "n_env_conflicting_targetids_dropped": int(len(conflict_ids)),
            "n_env_joined": int(len(d)),
            "per_class_n_env_joined":
                d["env_class"].value_counts().to_dict(),
            "M0_env_only_full_sample": fit_logistic(X0, y_full, n0),
            "M1_full_parent_no_edgeon": fit_pair(d, COVARIATES_NOEDGE),
            "M2_edgeon_subsample_all_covariates": fit_pair(d, COVARIATES),
        }
        results[tag] = res
        del d

    out["regressions"] = results

    # ---- verdict ----
    verdict_bits = []
    all_null = True
    for tag, res in results.items():
        for mkey, mlbl in [("M1_full_parent_no_edgeon", "full parent"),
                           ("M2_edgeon_subsample_all_covariates",
                            "edge-on subsample")]:
            pa = res[mkey]["env_only"]["env_joint_wald"]["p"]
            pb = res[mkey]["env_plus_covariates"]["env_joint_wald"]["p"]
            if pb < 0.05:
                all_null = False
            verdict_bits.append(
                f"{tag}/{mlbl} (n={res[mkey]['n_covariate_complete']:,}): "
                f"joint env Wald p = {pa:.3f} (env-only) -> {pb:.3f} "
                f"(with covariates)")
    out["verdict"] = {
        "environment_null_robust_to_covariates": bool(all_null),
        "summary": "; ".join(verdict_bits),
        "sentence": (
            "Environment-class coefficients remain statistically null after "
            "adjusting for galaxy size (est_petro_th50), apparent magnitude "
            "(mag_r), morphology (featured fraction), inclination (edge-on "
            "fraction), merger disturbance, redshift, and classifier "
            "confidence; the environmental-independence result is not an "
            "artifact of selection in galaxy properties."
            if all_null else
            "WARNING: at least one env block is significant (p<0.05) after "
            "covariate adjustment — inspect coefficients before quoting the "
            "null."),
    }

    out["runtime_seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=2))
    print(f"[done] wrote {OUT} in {out['runtime_seconds']}s")
    print(out["verdict"]["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
