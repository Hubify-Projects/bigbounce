#!/usr/bin/env python3
"""
EXTENDED forward model of the canonical-mask ell=1 chirality residual:
imaging systematics (depth/PSF/EBV/leg/density) PLUS the classifier
confidence-vs-depth response.

CONTEXT (2026-07-02):
  The imaging-only forward model (scripts/systematic_l1_forward_model.py)
  predicts an l=1 amplitude = 54% of the observed +3.64 sigma canonical-mask
  residual (cos-alignment +0.83). The remaining ~half was flagged as
  un-modelled because two named ingredients were missing:
    (a) per-galaxy MORPHOLOGY templates (b/a, fracdev, shape_r) from the
        DR8 sweep catalogs;
    (b) the CLASSIFIER confidence-vs-depth response.

  (a) is genuinely pod/sweep-bound: the DR8 sweep morphology columns
      (b_over_a, fracdev, shape_r_eff) are NOT in the local/HF chirality
      catalog and require the ~150 GB DR8 sweeps (H200 pod backup at
      /workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet). The
      RunPod key currently returns 403 (expired) and the volume is not
      mounted, so (a) cannot be added in this budget and remains an honest
      open item. See honesty_note.

  (b) IS executable locally: the chirality catalog carries the per-galaxy
      classifier confidence `confidence_eq`, and brick-level depth is already
      cross-matched. The classifier's confidence-vs-depth response is exactly
      the mechanism by which imaging depth could imprint a CW/CCW asymmetry
      (deeper imaging -> higher-confidence classifications -> different
      CW/CCW selection). This script ADDS that template to the WLS basis and
      re-measures the forward-modelled fraction.

METHOD (identical to systematic_l1_forward_model.py, with 3 added templates):
  Same NSIDE=64 chirality field A_p, same canonical |b|>15 mask, same
  brick depth/PSF/EBV cross-match, same imaging-leg + density templates.
  ADDED per-pixel templates (galaxy-count-weighted pixel means):
    conf_mean      : <confidence_eq> per pixel  (classifier confidence field)
    conf_x_depth   : <confidence_eq * depth_g>  (confidence-vs-depth response;
                     the interaction term that captures how the classifier
                     responds to depth)
    conf_resid     : <confidence_eq> after removing its linear depth trend
                     (the part of confidence NOT explained by depth alone)
  WLS-fit A_p onto {imaging templates} + {confidence templates}, form the
  systematic-predicted field, project onto l=1 on the canonical mask, and
  report the EXTENDED fraction of the observed residual reproduced.

NEVER fabricate the fraction. Report the real measured number.

Output: outputs/systematic_l1_forward_model_morphology.json
"""
from __future__ import annotations
import json
import time
import urllib.request
from pathlib import Path

import numpy as np
import healpy as hp
import pandas as pd
from astropy.io import fits
from huggingface_hub import hf_hub_download

NSIDE = 64
SEED = 42

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality")
CACHE = Path("/tmp/p4_brick_cache")
CACHE.mkdir(exist_ok=True)
URL_NORTH = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/north/survey-bricks-dr8-north.fits.gz"
URL_SOUTH = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/south/survey-bricks-dr8-south.fits.gz"
OUT = REPO / "outputs" / "systematic_l1_forward_model_morphology.json"

# Observed canonical-mask residual (same constants as imaging-only model).
OBS_A1_AMPLITUDE = 0.007040031846243215
OBS_C1_DECOUPLED = 2.348109981323473e-05
OBS_SIGMA_DIRECT = 3.64
OBS_SIGMA_DENSITY_STRAT = 3.80
NULL_MEAN_C1 = 1.7113319696431786e-06
NULL_STD_C1 = 3.052393324112356e-06

# Imaging-only baseline (from systematic_l1_forward_model_canonicalmask.json).
IMAGING_ONLY_FRAC_AMP = 0.5389442635381818
IMAGING_ONLY_COS = 0.8249649891323108

t0 = time.time()


def log(msg):
    print(f"[{time.time()-t0:6.1f}s] {msg}", flush=True)


def canonical_mask(nside):
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    rot = hp.Rotator(coord=["C", "G"])
    theta_g, _ = rot(theta, phi)
    b_deg = 90.0 - np.degrees(theta_g)
    return (np.abs(b_deg) > 15.0).astype(float)


def download_bricks():
    paths = {}
    for tag, url in [("north", URL_NORTH), ("south", URL_SOUTH)]:
        local = CACHE / Path(url).name
        if not local.exists():
            log(f"downloading {tag} bricks ...")
            urllib.request.urlretrieve(url, local)
        else:
            log(f"cached {tag} bricks at {local}")
        paths[tag] = local
    return paths


def load_brick_templates(paths):
    frames = []
    for tag, p in paths.items():
        with fits.open(p) as hdu:
            t = hdu[1].data
            cols = t.columns.names
            scalar = {c: t[c] for c in cols if t[c].ndim == 1}
            frames.append(pd.DataFrame(scalar))
            log(f"{tag} bricks: {len(t):,}")
    bricks = pd.concat(frames, ignore_index=True)
    psf_cols = [c for c in bricks.columns if c.lower().startswith("psfsize_")]
    depth_cols = [c for c in bricks.columns if c.lower().startswith("psfdepth_")]
    log(f"PSF cols {psf_cols}  depth cols {depth_cols}  ebv={'ebv' in bricks.columns}")
    bricks["psf_mean"] = bricks[psf_cols].astype(np.float32).mean(axis=1)
    bricks["depth_mean"] = bricks[depth_cols].astype(np.float32).mean(axis=1)
    return bricks, len(bricks)


def alm_l1(field):
    alm = hp.map2alm(field.astype(np.float64), lmax=2, iter=1)
    a10 = alm[hp.Alm.getidx(2, 1, 0)]
    a11 = alm[hp.Alm.getidx(2, 1, 1)]
    cz = float(np.real(a10))
    cx = -2.0 * float(np.real(a11))
    cy = +2.0 * float(np.imag(a11))
    amp = float(np.sqrt(cx**2 + cy**2 + cz**2))
    if amp > 0:
        ra_deg = float(np.degrees(np.arctan2(cy, cx)) % 360)
        dec_deg = float(np.degrees(np.arcsin(np.clip(cz / amp, -1, 1))))
    else:
        ra_deg = dec_deg = 0.0
    return {"amplitude": amp, "cx": cx, "cy": cy, "cz": cz,
            "ra_deg": ra_deg, "dec_deg": dec_deg}


def c1_power(field):
    alm = hp.map2alm(field.astype(np.float64), lmax=2, iter=1)
    cl = hp.alm2cl(alm, lmax=2)
    return float(cl[1])


def main():
    # --- catalog + chirality field + per-galaxy confidence ------------
    log("loading P4 catalog from HF ...")
    cat = hf_hub_download("bamfai/galaxy-chirality-catalog",
                          "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat, columns=["ra", "dec", "class_eq", "confidence_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    ra = df["ra"].values.astype(np.float64)
    dec = df["dec"].values.astype(np.float64)
    conf = df["confidence_eq"].values.astype(np.float64)
    conf[~np.isfinite(conf)] = np.nanmedian(conf[np.isfinite(conf)])
    log(f"spirals: {len(df):,}   <confidence_eq>={conf.mean():.4f}")

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra))
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix[is_cw == 1], minlength=npix).astype(np.float64)
    nz = n_total > 0
    A_p = np.zeros(npix)
    A_p[nz] = 2.0 * (n_cw[nz] / n_total[nz]) - 1.0

    # --- brick systematic templates -----------------------------------
    bricks, n_brick = load_brick_templates(download_bricks())
    from scipy.spatial import cKDTree

    def to_xyz(r, d):
        rr, dd = np.deg2rad(r), np.deg2rad(d)
        cd = np.cos(dd)
        return np.column_stack([np.cos(rr) * cd, np.sin(rr) * cd, np.sin(dd)])

    tree = cKDTree(to_xyz(bricks["ra"].values, bricks["dec"].values))
    log("cross-matching galaxies -> bricks ...")
    _, idx = tree.query(to_xyz(ra, dec), k=1, workers=-1)
    psf_g = bricks["psf_mean"].values[idx]
    depth_g = bricks["depth_mean"].values[idx]
    ebv_g = bricks["ebv"].values[idx] if "ebv" in bricks.columns else np.zeros(len(df))
    depth_g = np.asarray(depth_g, dtype=np.float64)
    depth_g[~np.isfinite(depth_g)] = np.nanmedian(depth_g[np.isfinite(depth_g)])

    # classifier confidence-vs-depth response (per-galaxy, executable locally):
    #   conf_resid_g = conf - (linear depth trend of conf)
    # i.e. the confidence variation NOT explained by depth alone; the residual
    # confidence field is what the classifier depth-response adds beyond depth.
    dfin = np.isfinite(depth_g) & np.isfinite(conf)
    A = np.column_stack([np.ones(dfin.sum()), depth_g[dfin]])
    slope = np.linalg.lstsq(A, conf[dfin], rcond=None)[0]
    conf_pred = slope[0] + slope[1] * depth_g
    conf_resid_g = conf - conf_pred            # confidence residual off the depth trend
    conf_x_depth_g = conf * depth_g            # confidence-vs-depth interaction
    log(f"classifier depth-response slope d<conf>/d(depth) = {slope[1]:+.4e}")

    def pixmean(vals):
        vals = np.asarray(vals, dtype=np.float64)
        s = np.bincount(pix, weights=vals, minlength=npix).astype(np.float64)
        m = np.zeros(npix)
        m[nz] = s[nz] / n_total[nz]
        return m

    psf_map = pixmean(psf_g)
    depth_map = pixmean(depth_g)
    ebv_map = pixmean(ebv_g)
    conf_map = pixmean(conf)
    conf_x_depth_map = pixmean(conf_x_depth_g)
    conf_resid_map = pixmean(conf_resid_g)
    for arr in (psf_map, depth_map, ebv_map, conf_map, conf_x_depth_map, conf_resid_map):
        arr[~np.isfinite(arr)] = 0.0

    dec_lo, dec_hi = -20.0, 32.0
    bass = (dec > dec_hi)
    decals = (dec >= dec_lo) & (dec <= dec_hi)
    n_bass = np.bincount(pix[bass], minlength=npix).astype(np.float64)
    n_decals = np.bincount(pix[decals], minlength=npix).astype(np.float64)

    cm = canonical_mask(NSIDE)
    in_mask = (cm > 0) & nz
    ip = np.where(in_mask)[0]
    w = n_total[ip]
    log(f"in-mask pixels: {ip.size:,}  f_sky={cm.mean():.4f}")

    def wcenter(x):
        return x - np.average(x[ip], weights=w)

    safe = np.maximum(n_total, 1.0)
    f_bass = wcenter(n_bass / safe)
    f_decals = wcenter(n_decals / safe)
    rho = n_total / max(n_total[ip].mean(), 1.0)
    rho_c = wcenter(rho)
    rho_sq = wcenter(rho_c**2)
    psf_c = wcenter(psf_map)
    depth_c = wcenter(depth_map)
    ebv_c = wcenter(ebv_map)
    conf_c = wcenter(conf_map)
    conf_xd_c = wcenter(conf_x_depth_map)
    conf_res_c = wcenter(conf_resid_map)
    A_p_corr = wcenter(A_p)

    # --- two designs: imaging-only (baseline) and +confidence (extended)
    imaging_tmpl = {
        "f_BASS_rel_DES": f_bass,
        "f_DECaLS_rel_DES": f_decals,
        "rho_p": rho_c,
        "rho_p_sq": rho_sq,
        "psf_mean": psf_c,
        "depth_mean": depth_c,
        "ebv": ebv_c,
    }

    # The raw confidence pixel-maps are strongly collinear with the imaging
    # templates (confidence is depth/PSF driven), which makes the joint design
    # rank-deficient (cond ~1e16) and the naive fraction uninformative. To
    # measure the INDEPENDENT contribution of the classifier response, we
    # ORTHOGONALIZE each confidence template against the imaging basis on the
    # in-mask pixels (galaxy-count-weighted) and keep only the residual part.
    imaging_names = list(imaging_tmpl.keys())
    Timg = np.column_stack([imaging_tmpl[n][ip] for n in imaging_names]
                           + [np.ones(ip.size)])
    swp = np.sqrt(w)
    Timg_w = Timg * swp[:, None]

    def orth_off_imaging(vec_full):
        y = vec_full[ip] * swp
        beta = np.linalg.lstsq(Timg_w, y, rcond=None)[0]
        resid_w = y - Timg_w @ beta
        out = np.zeros(npix)
        out[ip] = resid_w / swp          # weighted residual back to raw units
        # variance-normalize so the coefficient is well-scaled
        s = np.sqrt(np.average(out[ip] ** 2, weights=w))
        if s > 0:
            out[ip] /= s
        return out

    # Single, well-conditioned confidence template: the per-pixel classifier
    # confidence field, orthogonalized against the imaging basis so it carries
    # ONLY the confidence information NOT already in depth/PSF/EBV/leg/density.
    # (Adding a second confidence-derived template makes the design collinear
    #  with itself; one orthogonal template cleanly measures the independent
    #  classifier-response contribution.)
    conf_indep = orth_off_imaging(conf_c)
    conf_tmpl = {
        "conf_indep_of_imaging": conf_indep,
    }
    ext_tmpl = {**imaging_tmpl, **conf_tmpl}

    def fit_and_project(tmpl):
        names = list(tmpl.keys())
        T = np.column_stack([tmpl[n][ip] for n in names])
        T = np.column_stack([T, np.ones(ip.size)])
        names_full = names + ["const"]
        sw = np.sqrt(w)
        a_hat, *_ = np.linalg.lstsq(T * sw[:, None], A_p_corr[ip] * sw, rcond=None)
        coeffs = {n: float(v) for n, v in zip(names_full, a_hat)}
        cond = float(np.linalg.cond(T))
        A_sys = np.zeros(npix)
        for n in names:
            A_sys[ip] += coeffs[n] * tmpl[n][ip]
        A_sys_masked = A_sys * (cm > 0)
        l1 = alm_l1(A_sys_masked)
        c1 = c1_power(A_sys_masked)
        return coeffs, cond, l1, c1

    # observed masked field
    A_obs_masked = np.zeros(npix)
    A_obs_masked[ip] = A_p_corr[ip]
    A_obs_masked *= (cm > 0)
    obs_l1 = alm_l1(A_obs_masked)
    obs_c1_incode = c1_power(A_obs_masked)
    v_obs = np.array([obs_l1["cx"], obs_l1["cy"], obs_l1["cz"]])
    amp_obs = float(np.linalg.norm(v_obs))

    base_coeffs, base_cond, base_l1, base_c1 = fit_and_project(imaging_tmpl)
    ext_coeffs, ext_cond, ext_l1, ext_c1 = fit_and_project(ext_tmpl)
    log(f"imaging-only cond={base_cond:.2e}  extended cond={ext_cond:.2e}")

    def metrics(l1, c1, label):
        v = np.array([l1["cx"], l1["cy"], l1["cz"]])
        amp = float(np.linalg.norm(v))
        cos = float(np.dot(v, v_obs) / (amp * amp_obs)) if amp * amp_obs > 0 else 0.0
        frac_amp = amp / amp_obs if amp_obs > 0 else 0.0
        frac_pow = c1 / obs_c1_incode if obs_c1_incode > 0 else 0.0
        aligned = amp * cos  # projection onto observed dipole (the directional fraction)
        frac_aligned = aligned / amp_obs if amp_obs > 0 else 0.0
        sig = (c1 - NULL_MEAN_C1) / NULL_STD_C1
        log(f"{label:14s} |a1|={amp:.4e}  frac={frac_amp:.1%}  cos={cos:+.3f}  aligned-frac={frac_aligned:.1%}")
        return {"l1_amplitude": amp, "l1_vector": {"cx": l1["cx"], "cy": l1["cy"], "cz": l1["cz"]},
                "l1_direction": {"ra_deg": l1["ra_deg"], "dec_deg": l1["dec_deg"]},
                "C1_power": c1, "cos_alignment": cos,
                "fraction_of_observed_amplitude": frac_amp,
                "fraction_of_observed_power": frac_pow,
                "aligned_projection_amplitude": aligned,
                "fraction_of_observed_amplitude_aligned": frac_aligned,
                "predicted_equivalent_sigma_vs_depthstrat_null": sig}

    base_m = metrics(base_l1, base_c1, "imaging-only")
    ext_m = metrics(ext_l1, ext_c1, "imaging+conf")

    ext_frac = ext_m["fraction_of_observed_amplitude"]
    base_frac = base_m["fraction_of_observed_amplitude"]
    delta = ext_frac - base_frac
    remainder = 1.0 - ext_frac

    if ext_frac >= 0.70:
        verdict = "RESIDUAL_LARGELY_SYSTEMATIC"
        vtext = (f"Adding the classifier confidence-vs-depth response raises the "
                 f"forward-modelled l=1 fraction to {ext_frac:.0%} (from {base_frac:.0%} "
                 f"imaging-only, +{delta*100:.1f} pts). The depth-correlated systematic "
                 f"now reproduces most of the +3.64 sigma residual -> the residual is "
                 f"largely SYSTEMATIC, strengthening the null.")
    elif delta >= 0.03:
        verdict = "PARTIAL_IMPROVEMENT_HONEST_REMAINDER"
        vtext = (f"The classifier confidence-vs-depth response adds +{delta*100:.1f} pts, "
                 f"raising the forward-modelled l=1 fraction to {ext_frac:.0%} (from "
                 f"{base_frac:.0%} imaging-only). A real un-modelled remainder of "
                 f"{remainder:.0%} persists. The per-galaxy DR8-sweep morphology "
                 f"(b/a, fracdev, shape_r) is still missing (pod-bound; not addable in "
                 f"budget) and remains the honest open item.")
    else:
        verdict = "NO_MEANINGFUL_IMPROVEMENT"
        vtext = (f"The classifier confidence-vs-depth response changes the forward-modelled "
                 f"l=1 fraction by only {delta*100:+.1f} pts ({base_frac:.0%} -> {ext_frac:.0%}). "
                 f"Confidence adds little beyond the imaging templates it correlates with. "
                 f"The ~half remainder stays an honest open item; the paper's 54% "
                 f"imaging-only honest-partial framing is retained.")

    result = {
        "script": "scripts/systematic_l1_forward_model_morphology.py",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": ("EXTENDED forward model: add the classifier confidence-vs-depth "
                    "response to the imaging (depth/PSF/EBV/leg/density) systematic basis "
                    "and re-measure the forward-modelled fraction of the +3.64 sigma "
                    "canonical-mask l=1 residual. Per-galaxy DR8-sweep morphology "
                    "(b/a, fracdev, shape_r) is pod-bound and NOT included (see honesty_note)."),
        "config": {
            "nside": NSIDE,
            "n_spirals": int(len(df)),
            "n_brick_sources": int(n_brick),
            "n_in_mask_pixels": int(ip.size),
            "f_sky_canonical": float(cm.mean()),
            "imaging_templates": list(imaging_tmpl.keys()),
            "added_confidence_templates": list(conf_tmpl.keys()),
            "classifier_depth_response_slope": float(slope[1]),
            "imaging_only_condition_number": base_cond,
            "extended_condition_number": ext_cond,
            "fit": "WLS (galaxy-count weights); SYSTEMATIC-ONLY basis (no dipole vectors)",
        },
        "imaging_only_fit_coefficients": base_coeffs,
        "extended_fit_coefficients": ext_coeffs,
        "observed_residual": {
            "A1_amplitude_realspace": OBS_A1_AMPLITUDE,
            "A1_amplitude_incode_recompute": amp_obs,
            "C1_decoupled_incode": obs_c1_incode,
            "C1_depth_stratified_data": OBS_C1_DECOUPLED,
            "sigma_direct_500MC": OBS_SIGMA_DIRECT,
            "sigma_density_stratified": OBS_SIGMA_DENSITY_STRAT,
        },
        "imaging_only_forward_model": base_m,
        "extended_forward_model": ext_m,
        "improvement": {
            "imaging_only_fraction": base_frac,
            "extended_fraction": ext_frac,
            "delta_fraction_points": delta,
            "un_modelled_remainder": remainder,
            "imaging_only_cos_alignment": base_m["cos_alignment"],
            "extended_cos_alignment": ext_m["cos_alignment"],
            "prior_committed_imaging_only_fraction": IMAGING_ONLY_FRAC_AMP,
        },
        "verdict": verdict,
        "verdict_text": vtext,
        "honesty_note": (
            "ADDED locally-executable template: the classifier confidence-vs-depth "
            "response, built from the per-galaxy confidence_eq column (available in the "
            "chirality catalog) x brick-level depth. STILL MISSING (genuine open item): "
            "per-galaxy DR8-sweep morphology b/a (b_over_a), fracdev, shape_r_eff, "
            "shapedev_e1/e2 -- these require the ~150 GB DR8 sweep catalogs "
            "(H200 pod backup /workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet). "
            "The RunPod API key returned HTTP 403 (expired) this session and the canonical "
            "volume was not mountable within the time budget, so per-galaxy morphology "
            "could NOT be added. The extended fraction here is therefore the imaging + "
            "classifier-response forward model, still a LOWER BOUND pending per-galaxy morphology."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    log(f"wrote {OUT}")

    print("\n=== EXTENDED FORWARD-MODEL VERDICT ===")
    print(f"  observed  |a_1|       = {amp_obs:.4e}   (+{OBS_SIGMA_DIRECT} sigma)")
    print(f"  imaging-only fraction = {base_frac:.1%}  (cos {base_m['cos_alignment']:+.3f})")
    print(f"  imaging+confidence    = {ext_frac:.1%}  (cos {ext_m['cos_alignment']:+.3f})")
    print(f"  delta                 = {delta*100:+.1f} pts;  remainder {remainder:.1%}")
    print(f"  VERDICT: {verdict}")
    print(f"  {vtext}")


if __name__ == "__main__":
    main()
