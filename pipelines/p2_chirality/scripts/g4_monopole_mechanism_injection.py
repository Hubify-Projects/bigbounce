#!/usr/bin/env python3
"""
G4 (open-compute gate) — monopole-mechanism isolation via image-level
classifier-injection: per-pixel confusion tensor + generative parity-null.

Answers reviewer gate M5 (the −9.47σ monopole has no causal mechanism
isolated). Per COMPUTE_CAMPAIGN_2026-07-17.md §G4, the required pieces are
(1) the production ViT run on the 8.47M images + their per-pixel mirror pairs
    → per-pixel CW↔CCW↔NS confusion tensor;
(2) a generative null that forward-models the global monopole from classifier
    confusion alone under a parity-symmetric input ensemble;
(3) comparison of the confusion-generated monopole to the observed −9.47σ,
    bounding each candidate mechanism (GZ1 training-prior CW excess /
    residual orientation bias / DESI photometric asymmetry).

REAL-COMPUTE PROVENANCE of piece (1): the 16,949,062 ViT forward passes
(8,474,531 galaxies × {original, horizontal mirror}) were executed on pod
0hh3humgpacgz1 (A100 80GB) 2026-07-11→12 and banked per-galaxy in
`e2e_mirror_pairs.parquet` (HF bamfai/galaxy-chirality-catalog; also B2 +
local `outputs/canonical_provenance/e2e_fullrun/e2e_shards/`, byte-verified —
see e2e_fullrun/RUN_SUMMARY.md). This script does NOT re-run the inference; it
builds the per-pixel confusion aggregation and the generative null on top of
that banked inference, joined to sky positions via dr8_id ↔
catalog_production.parquet. No new GPU pass is scientifically required: every
per-galaxy quantity the confusion tensor and null need is already recorded.

GENERATIVE NULL (piece 2): under a parity-symmetric universe, the ensemble of
input images is invariant under mirroring each image independently with
probability 1/2. For each of N_REAL realizations we draw a mirror mask
m_i ~ Bernoulli(1/2), assign each galaxy the classifier's ACTUAL recorded
label for that parity state (class_eq vs class_eq_mirror; class_raw vs
class_raw_mirror), re-apply the HC selection, and record the global monopole
f_CW − 0.5. The spread of this distribution is the monopole the classifier's
real confusion structure can generate from a parity-symmetric sky:
  * EQ mode  — the production Z2-TTA labels the paper's monopole is measured
               on (antisymmetric by construction; T_eq = 0.99974).
  * RAW mode — the single-pass labels WITHOUT the antisymmetrization guard;
               bounds the "residual orientation bias" mechanism if the
               equivariance were absent.

PER-PIXEL CONFUSION (pieces 1+3): NSIDE=64 maps of the 3x3 mirror-confusion
tensor (rows=original class, cols=mirror class) in both modes, the
confusion-propagated CW-fraction bias field
  b_p = 0.5·(f_CW,orig,p + f_CW,mirror,p) − 0.5
(the expected per-pixel CW-fraction deviation a parity-symmetric sky would
show through the classifier), its monopole/dipole, a North/South split
(DESI photometric-asymmetry candidate), and the raw-channel classifier PRIOR
asymmetry mean[0.5(p_cw+p_cw_mirror)] − mean[0.5(p_ccw+p_ccw_mirror)]
(the training-prior / GZ1-CW-excess candidate as expressed at inference).

Outputs:
  outputs/canonical_provenance/g4_monopole_mechanism_injection.json
  outputs/canonical_provenance/g4_perpixel_confusion_nside64.npz
Run:  python3 g4_monopole_mechanism_injection.py [--smoke]   (smoke: N_REAL=20)
"""
from __future__ import annotations

import glob
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd

NSIDE = 64
N_REAL = 500
SEED = 42
CONF_THRESH = 0.6
GAL_LAT_CUT_DEG = 15.0
OBSERVED_MONOPOLE_SIGMA_BINOMIAL = -9.47  # paper's per-pixel-independent binomial z

HERE = Path(__file__).resolve().parent
_repo_out = HERE.parent / "outputs" / "canonical_provenance"
OUT_DIR = _repo_out if _repo_out.is_dir() else HERE / "out"
OUT_JSON = OUT_DIR / "g4_monopole_mechanism_injection.json"
OUT_NPZ = OUT_DIR / "g4_perpixel_confusion_nside64.npz"

SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_REAL = 20

t0 = time.time()
CLS = {"CW": 0, "CCW": 1, "NOT_SPIRAL": 2, "NS": 2}


def log(msg: str) -> None:
    print(f"[{time.time()-t0:7.1f}s] {msg}", flush=True)


def find_hf(fname: str) -> str:
    cands = sorted(glob.glob(os.path.expanduser(
        "~/.cache/huggingface/hub/datasets--bamfai--galaxy-chirality-catalog/"
        f"snapshots/*/{fname}")))
    if not cands:
        raise SystemExit(f"{fname} not in HF cache")
    return cands[-1]


def to_cls(series: pd.Series) -> np.ndarray:
    return series.map(CLS).values.astype(np.int8)


def galactic_lat_mask(nside: int) -> np.ndarray:
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    rot = hp.Rotator(coord=["C", "G"])
    theta_g, _ = rot(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > GAL_LAT_CUT_DEG).astype(bool)


def main() -> None:
    e2e_path = find_hf("e2e_mirror_pairs.parquet")
    cat_path = find_hf("catalog_production.parquet")
    log(f"loading e2e mirror pairs: {e2e_path.split('/')[-1]}")
    e2e = pd.read_parquet(e2e_path, columns=[
        "dr8_id", "class_raw", "class_raw_mirror", "class_eq", "class_eq_mirror",
        "p_cw_raw", "p_ccw_raw", "p_cw_raw_mirror", "p_ccw_raw_mirror",
        "conf_raw", "eq_antisym_dev"])
    log(f"e2e rows: {len(e2e):,}")
    log("loading catalog (dr8_id, ra, dec, class_eq, confidence_eq)")
    cat = pd.read_parquet(cat_path, columns=[
        "dr8_id", "ra", "dec", "class_eq", "confidence_eq"])
    log(f"catalog rows: {len(cat):,}")

    log("joining on dr8_id ...")
    df = e2e.merge(cat.rename(columns={"class_eq": "class_eq_cat"}),
                   on="dr8_id", how="inner", validate="one_to_one")
    n_join = len(df)
    agree = float((df["class_eq"] == df["class_eq_cat"]).mean())
    log(f"joined rows: {n_join:,}  (e2e vs catalog class_eq agreement {agree:.6f})")
    del e2e, cat

    cls_eq_o = to_cls(df["class_eq"])
    cls_eq_m = to_cls(df["class_eq_mirror"])
    cls_raw_o = to_cls(df["class_raw"])
    cls_raw_m = to_cls(df["class_raw_mirror"])
    conf_eq = df["confidence_eq"].values.astype(np.float32)
    conf_raw = df["conf_raw"].values.astype(np.float32)
    eq_dev = df["eq_antisym_dev"].values.astype(np.float32)
    p_cw_r = df["p_cw_raw"].values.astype(np.float64)
    p_ccw_r = df["p_ccw_raw"].values.astype(np.float64)
    p_cw_rm = df["p_cw_raw_mirror"].values.astype(np.float64)
    p_ccw_rm = df["p_ccw_raw_mirror"].values.astype(np.float64)
    ra = df["ra"].values.astype(np.float64)
    dec = df["dec"].values.astype(np.float64)
    del df

    pix = hp.ang2pix(NSIDE, np.deg2rad(90.0 - dec), np.deg2rad(ra)).astype(np.int64)
    npix = hp.nside2npix(NSIDE)
    galmask = galactic_lat_mask(NSIDE)
    in_galmask = galmask[pix]

    # ---------------- observed monopole (the target of the mechanism test)
    hc_obs = (cls_eq_o < 2) & (conf_eq > CONF_THRESH) & in_galmask
    n_hc = int(hc_obs.sum())
    f_cw_obs = float((cls_eq_o[hc_obs] == 0).mean())
    mono_obs = f_cw_obs - 0.5
    log(f"observed HC (galmask): n={n_hc:,}  monopole={mono_obs:+.6f}")

    # ---------------- per-pixel 3x3 confusion tensors (banked-inference agg)
    log("building per-pixel confusion tensors (raw + eq) ...")
    conf_raw_pix = np.zeros((npix, 3, 3), np.int64)
    conf_eq_pix = np.zeros((npix, 3, 3), np.int64)
    for a in range(3):
        for b in range(3):
            sel = (cls_raw_o == a) & (cls_raw_m == b)
            conf_raw_pix[:, a, b] = np.bincount(pix[sel], minlength=npix)
            sel = (cls_eq_o == a) & (cls_eq_m == b)
            conf_eq_pix[:, a, b] = np.bincount(pix[sel], minlength=npix)
    n_pix_tot = np.bincount(pix, minlength=npix)

    # confusion-propagated CW-fraction bias field (HC selection, eq + raw)
    def bias_field(cls_o, cls_m, conf, thr):
        sel_o = (cls_o < 2) & (conf > thr)
        sel_m = (cls_m < 2) & (conf > thr)
        n_o = np.bincount(pix[sel_o], minlength=npix).astype(np.float64)
        n_m = np.bincount(pix[sel_m], minlength=npix).astype(np.float64)
        c_o = np.bincount(pix[sel_o & (cls_o == 0)], minlength=npix).astype(np.float64)
        c_m = np.bincount(pix[sel_m & (cls_m == 0)], minlength=npix).astype(np.float64)
        good = (n_o > 0) & (n_m > 0)
        b = np.full(npix, np.nan)
        b[good] = 0.5 * (c_o[good] / n_o[good] + c_m[good] / n_m[good]) - 0.5
        return b, n_o + n_m

    b_eq, w_eq = bias_field(cls_eq_o, cls_eq_m, conf_eq, CONF_THRESH)
    b_raw, w_raw = bias_field(cls_raw_o, cls_raw_m, conf_raw, CONF_THRESH)

    def field_stats(b, w):
        good = np.isfinite(b) & galmask & (w > 0)
        mono = float(np.average(b[good], weights=w[good]))
        # uniform-weight dipole of the centered bias field
        th, ph = hp.pix2ang(NSIDE, np.where(good)[0])
        nh = np.column_stack([np.sin(th) * np.cos(ph),
                              np.sin(th) * np.sin(ph), np.cos(th)])
        M = np.column_stack([np.ones(good.sum()), nh])
        c, *_ = np.linalg.lstsq(M, b[good], rcond=None)
        # N/S split (dec-based, DESI photometric-asymmetry candidate)
        pix_dec = 90.0 - np.degrees(hp.pix2ang(NSIDE, np.arange(npix))[0])
        north = good & (pix_dec >= 32.0)   # BASS/MzLS leg
        south = good & (pix_dec < 32.0)
        mono_n = float(np.average(b[north], weights=w[north])) if north.any() else None
        mono_s = float(np.average(b[south], weights=w[south])) if south.any() else None
        return {"monopole_weighted": mono,
                "dipole_amp_uniform": float(np.linalg.norm(c[1:4])),
                "monopole_north_dec_ge32": mono_n,
                "monopole_south_dec_lt32": mono_s,
                "n_pixels": int(good.sum())}

    stats_eq = field_stats(b_eq, w_eq)
    stats_raw = field_stats(b_raw, w_raw)
    log(f"bias-field monopole: eq={stats_eq['monopole_weighted']:+.3e} "
        f"raw={stats_raw['monopole_weighted']:+.3e}")

    # raw-channel classifier PRIOR asymmetry (training-prior candidate)
    prior_asym_raw = float(np.mean(0.5 * (p_cw_r + p_cw_rm))
                           - np.mean(0.5 * (p_ccw_r + p_ccw_rm)))
    log(f"raw classifier prior asymmetry <p_CW>-<p_CCW> (parity-avg) = "
        f"{prior_asym_raw:+.6f}")

    # ---------------- generative parity-symmetric null
    rng = np.random.default_rng(SEED)
    log(f"generative null: {N_REAL} parity-symmetric realizations "
        f"({'SMOKE' if SMOKE else 'FULL'}) ...")
    mono_eq = np.empty(N_REAL)
    mono_raw = np.empty(N_REAL)
    n = cls_eq_o.size
    for r in range(N_REAL):
        m = rng.random(n) < 0.5
        lab_eq = np.where(m, cls_eq_m, cls_eq_o)
        sel = (lab_eq < 2) & (conf_eq > CONF_THRESH) & in_galmask
        mono_eq[r] = (lab_eq[sel] == 0).mean() - 0.5
        lab_raw = np.where(m, cls_raw_m, cls_raw_o)
        selr = (lab_raw < 2) & (conf_raw > CONF_THRESH) & in_galmask
        mono_raw[r] = (lab_raw[selr] == 0).mean() - 0.5
        if (r + 1) % 50 == 0 or (SMOKE and (r + 1) % 5 == 0):
            log(f"  {r+1}/{N_REAL}  eq mean={mono_eq[:r+1].mean():+.2e} "
                f"raw mean={mono_raw[:r+1].mean():+.2e}")

    def null_summary(arr, obs):
        mu, sd = float(arr.mean()), float(arr.std(ddof=1))
        return {
            "mean": mu, "std": sd,
            "z_observed_vs_null": float((obs - mu) / sd) if sd > 0 else None,
            "fraction_of_observed_monopole_explained_mean": float(mu / obs),
            "fraction_of_observed_monopole_explained_2sigma_bound":
                float((abs(mu) + 2 * sd) / abs(obs)),
        }

    s_eq = null_summary(mono_eq, mono_obs)
    s_raw = null_summary(mono_raw, mono_obs)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        OUT_NPZ,
        confusion_raw_pix=conf_raw_pix.astype(np.int32),
        confusion_eq_pix=conf_eq_pix.astype(np.int32),
        n_pix_total=n_pix_tot.astype(np.int32),
        bias_field_eq=b_eq.astype(np.float32),
        bias_field_raw=b_raw.astype(np.float32),
        galmask=galmask,
        nside=np.array([NSIDE]),
        readme=np.array([
            "confusion_*_pix: [npix,3,3] counts, rows=original class, "
            "cols=mirror class, classes {0:CW,1:CCW,2:NOT_SPIRAL}; "
            "bias_field_*: 0.5*(f_CW_orig+f_CW_mirror)-0.5 per pixel (HC sel); "
            "source inference: e2e_mirror_pairs.parquet (A100 pod 0hh3humgpacgz1)"]))
    log(f"wrote {OUT_NPZ}")

    result = {
        "script": "scripts/g4_monopole_mechanism_injection.py",
        "gate": "G4 — monopole mechanism: per-pixel confusion + generative parity-null",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "inference_provenance": {
            "source": "e2e_mirror_pairs.parquet (HF bamfai/galaxy-chirality-catalog)",
            "inference_run": "pod 0hh3humgpacgz1 A100-80GB 2026-07-11/12, 192/192 shards, "
                             "16,949,062 ViT forward passes (RUN_SUMMARY.md)",
            "model": "bamfai/galaxy-chirality-v2 production checkpoint",
            "note": "this script aggregates the banked per-galaxy inference; "
                    "no forward passes were re-run",
        },
        "n_e2e_catalog_joined": n_join,
        "e2e_vs_catalog_class_eq_agreement": agree,
        "nside": NSIDE,
        "conf_thresh": CONF_THRESH,
        "gal_lat_cut_deg": GAL_LAT_CUT_DEG,
        "n_realizations": N_REAL,
        "seed": SEED,
        "smoke": SMOKE,
        "observed": {
            "n_hc_galmask": n_hc,
            "f_cw": f_cw_obs,
            "monopole": mono_obs,
            "binomial_z_paper": OBSERVED_MONOPOLE_SIGMA_BINOMIAL,
        },
        "generative_null_monopole": {
            "eq_mode_production_labels": s_eq,
            "raw_mode_no_antisymmetrization": s_raw,
            "definition": "each galaxy independently mirrored with p=1/2; "
                          "labels = classifier's recorded outputs for that parity "
                          "state; HC selection re-applied per realization",
        },
        "confusion_propagated_bias_field": {
            "eq_mode": stats_eq,
            "raw_mode": stats_raw,
            "definition": "b_p = 0.5*(f_CW_orig,p + f_CW_mirror,p) - 0.5 (HC sel)",
        },
        "mechanism_candidates": {
            "classifier_confusion_eq_pipeline": {
                "monopole_generated_mean": s_eq["mean"],
                "monopole_generated_std": s_eq["std"],
                "fraction_of_observed_2sigma_bound":
                    s_eq["fraction_of_observed_monopole_explained_2sigma_bound"],
            },
            "residual_orientation_bias_raw_channel": {
                "monopole_generated_mean": s_raw["mean"],
                "monopole_generated_std": s_raw["std"],
                "fraction_of_observed_2sigma_bound":
                    s_raw["fraction_of_observed_monopole_explained_2sigma_bound"],
            },
            "training_prior_gz1_cw_excess_raw_prior_asym": prior_asym_raw,
            "desi_photometric_asymmetry_ns_split": {
                "eq_bias_monopole_north": stats_eq["monopole_north_dec_ge32"],
                "eq_bias_monopole_south": stats_eq["monopole_south_dec_lt32"],
                "raw_bias_monopole_north": stats_raw["monopole_north_dec_ge32"],
                "raw_bias_monopole_south": stats_raw["monopole_south_dec_lt32"],
            },
        },
        "eq_antisym_dev": {"mean": float(eq_dev.mean()),
                           "max": float(eq_dev.max())},
        "perpixel_artifact": str(OUT_NPZ.name),
    }
    OUT_JSON.write_text(json.dumps(result, indent=2))
    log(f"wrote {OUT_JSON}")

    print("\n=== G4 GENERATIVE-NULL SUMMARY ===", flush=True)
    print(f"observed HC monopole              : {mono_obs:+.6f} (n={n_hc:,})")
    print(f"EQ-mode null (production labels)  : {s_eq['mean']:+.3e} ± {s_eq['std']:.3e}"
          f"  -> |explained| 2σ-bound {s_eq['fraction_of_observed_monopole_explained_2sigma_bound']:.4%}")
    print(f"RAW-mode null (no antisym guard)  : {s_raw['mean']:+.3e} ± {s_raw['std']:.3e}"
          f"  -> |explained| 2σ-bound {s_raw['fraction_of_observed_monopole_explained_2sigma_bound']:.4%}")
    print(f"raw classifier prior asymmetry    : {prior_asym_raw:+.6f}")
    print(f"bias-field monopole eq/raw        : {stats_eq['monopole_weighted']:+.3e} / "
          f"{stats_raw['monopole_weighted']:+.3e}")


if __name__ == "__main__":
    main()
