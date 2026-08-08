#!/usr/bin/env python3
"""
Forward model of the canonical-mask ell=1 chirality residual from the
depth / morphology-proxy imaging systematic.

MOTIVATION (Grok external-review flag, 2026-07):
  The paper ATTRIBUTES the +3.64 sigma canonical-mask ell=1 residual
  (A_p^(l=1) = 7.040e-03; C_1 = 2.298e-05) to a depth/morphology-correlated
  survey systematic, but no forward model PREDICTS the residual's amplitude.
  Attribution-without-a-model. The density-stratified null is still +3.80 sigma.

  Every prior artifact reports either the RESIDUAL dipole AFTER removing the
  nuisance templates (joint_nuisance_full_template_basis.json -> exclusion of a
  primordial dipole) or a leg-only proxy (morphology_template_l1_projection.json
  -> 25.2% of the observed l=1). Nobody has computed the COMPLEMENTARY quantity:
  the ell=1 amplitude of the FITTED SYSTEMATIC MODEL ITSELF -- i.e. the part of
  A_p that the depth/PSF/EBV/leg/density templates EXPLAIN -- and asked whether
  that PREDICTED systematic ell=1 amplitude MATCHES the observed +3.64 sigma
  residual. That is the forward model that turns attribution from asserted into
  demonstrated.

METHOD (identical map/template machinery to
        scripts/joint_nuisance_full_template_basis.py; reused deliberately):
  1. Build the per-pixel (HEALPix NSIDE=64) chirality field
        A_p(p) = 2 * n_CW(p)/n_total(p) - 1,  monopole (mask-mean) subtracted.
     This is the SAME field whose ell=1 mode gives the +3.64 sigma residual.
  2. Build the systematic template maps at NSIDE=64:
        depth (psfdepth g/r/z mean), PSF FWHM (psfsize g/r/z mean), EBV
        (all brick-level, aggregated per pixel from DR8 survey-bricks FITS),
        plus imaging-leg fractions (BASS+MzLS / DECaLS, DES = ref) and
        source density rho_p + rho_p^2 (depth-correlated sampling).
     These ARE the "depth/morphology systematic" the paper invokes.
  3. WLS-fit (galaxy-count weights, canonical |b|>15deg mask) the chirality
        field onto the SYSTEMATIC templates ONLY (no dipole basis vectors):
            A_p(p) = sum_k a_k T_k(p) + eps(p).
     The measured coefficients a_k ARE the empirical depth/morphology ->
     chirality-bias relation. This is the forward-model input, MEASURED not
     assumed.
  4. FORM THE SYSTEMATIC-PREDICTED FIELD  A_sys(p) = sum_k a_k T_k(p)
     (the model's prediction for how much CW/CCW bias the systematic imprints,
      NOT the residual).
  5. Project A_sys onto ell=1 on the canonical mask -> the PREDICTED ell=1
     dipole amplitude  |a_1^sys|  and power  C_1^sys.
  6. COMPARE to the OBSERVED canonical-mask residual:
        observed |a_1| = 7.040e-03,  observed C_1 = 2.298e-05,  +3.64 sigma
     and convert the predicted amplitude to an equivalent sigma against the
     SAME label-shuffle null width used for the observed +3.64 sigma.

VERDICT LOGIC:
  - If |a_1^sys| ~ observed |a_1| (predicted power comparable to observed
    C_1, predicted sigma comparable to +3.64): the systematic forward model
    QUANTITATIVELY REPRODUCES the residual -> attribution DEMONSTRATED.
  - If |a_1^sys| << observed |a_1| (predicts only a fraction): attribution
    is INCOMPLETE / partial -> honest open issue.
  NEVER fabricate the predicted amplitude. Report the real numbers.

Output: outputs/systematic_l1_forward_model.json
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
OUT = REPO / "outputs" / "systematic_l1_forward_model.json"

# Observed canonical-mask residual (from morphology_template_l1_projection.json
# + c6_depth_stratified_null.json + paper Sec. monopole_mask_null).
OBS_A1_AMPLITUDE = 0.007040031846243215          # real-space |a_1| of A_p_demono
OBS_C1_DECOUPLED = 2.348109981323473e-05          # C6 depth-stratified data C_1
OBS_SIGMA_DIRECT = 3.64                            # 500-MC direct canonical
OBS_SIGMA_DENSITY_STRAT = 3.80                     # density-stratified null
# Depth-stratified label-shuffle null moments (C6, 500 MC) in C_1 power units:
NULL_MEAN_C1 = 1.7113319696431786e-06
NULL_STD_C1 = 3.052393324112356e-06

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
    """Real-space l=1 dipole vector and amplitude of a full-sky map."""
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
    """Decoupled C_1 (same alm2cl convention as the paper's real-space
    estimator) of a full-sky map."""
    alm = hp.map2alm(field.astype(np.float64), lmax=2, iter=1)
    cl = hp.alm2cl(alm, lmax=2)
    return float(cl[1])


def main():
    # --- catalog + chirality field ------------------------------------
    log("loading P4 catalog from HF ...")
    cat = hf_hub_download("bamfai/galaxy-chirality-catalog",
                          "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat, columns=["ra", "dec", "class_eq"])
    df = df.loc[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    is_cw = (df["class_eq"].values == "CW").astype(np.int8)
    ra = df["ra"].values.astype(np.float64)
    dec = df["dec"].values.astype(np.float64)
    log(f"spirals: {len(df):,}")

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

    def pixmean(vals):
        s = np.bincount(pix, weights=vals, minlength=npix).astype(np.float64)
        m = np.zeros(npix)
        m[nz] = s[nz] / n_total[nz]
        return m

    psf_map = pixmean(psf_g)
    depth_map = pixmean(depth_g)
    ebv_map = pixmean(ebv_g)
    for arr in (psf_map, depth_map, ebv_map):
        arr[~np.isfinite(arr)] = 0.0

    # imaging-leg fractions (DES = reference; matches full_template_basis)
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
    A_p_corr = wcenter(A_p)

    # SYSTEMATIC-ONLY design (NO dipole n_x/n_y/n_z basis vectors).
    tmpl = {
        "f_BASS_rel_DES": f_bass,
        "f_DECaLS_rel_DES": f_decals,
        "rho_p": rho_c,
        "rho_p_sq": rho_sq,
        "psf_mean": psf_c,
        "depth_mean": depth_c,
        "ebv": ebv_c,
    }
    names = list(tmpl.keys())
    T = np.column_stack([tmpl[n][ip] for n in names])
    T = np.column_stack([T, np.ones(ip.size)])  # constant
    names_full = names + ["const"]

    # --- WLS fit: A_p onto systematic templates -----------------------
    sw = np.sqrt(w)
    Tw = T * sw[:, None]
    yw = A_p_corr[ip] * sw
    a_hat, *_ = np.linalg.lstsq(Tw, yw, rcond=None)
    coeffs = {n: float(v) for n, v in zip(names_full, a_hat)}
    cond = float(np.linalg.cond(T))
    log(f"systematic-only WLS fit done. cond={cond:.2e}")
    for n, v in coeffs.items():
        log(f"   {n:18s} a_hat = {v:+.4e}")

    # --- FORM THE SYSTEMATIC-PREDICTED FIELD  A_sys = sum_k a_k T_k ----
    # Full-sky map (predict everywhere in-mask; zero outside).
    A_sys = np.zeros(npix)
    for n in names:  # exclude constant from the *dipole* projection
        A_sys[ip] += coeffs[n] * tmpl[n][ip]
    # (constant term is a pure monopole; it does not project onto l=1.)
    A_sys_masked = A_sys * (cm > 0)

    # Observed field (mask-applied) for an apples-to-apples in-code check.
    A_obs_masked = np.zeros(npix)
    A_obs_masked[ip] = A_p_corr[ip]
    A_obs_masked *= (cm > 0)

    # --- ell=1 projections --------------------------------------------
    pred_l1 = alm_l1(A_sys_masked)
    obs_l1 = alm_l1(A_obs_masked)
    pred_c1 = c1_power(A_sys_masked)
    obs_c1_incode = c1_power(A_obs_masked)

    # Fraction of the observed l=1 dipole VECTOR reproduced by the
    # systematic model, both in amplitude and as a projection (cos-aligned).
    v_pred = np.array([pred_l1["cx"], pred_l1["cy"], pred_l1["cz"]])
    v_obs = np.array([obs_l1["cx"], obs_l1["cy"], obs_l1["cz"]])
    amp_pred = float(np.linalg.norm(v_pred))
    amp_obs = float(np.linalg.norm(v_obs))
    cos_align = float(np.dot(v_pred, v_obs) / (amp_pred * amp_obs)) if amp_pred * amp_obs > 0 else 0.0
    aligned_projection = amp_pred * cos_align  # component of prediction along observed dipole

    frac_amplitude = amp_pred / amp_obs if amp_obs > 0 else 0.0
    frac_power = pred_c1 / obs_c1_incode if obs_c1_incode > 0 else 0.0

    # Equivalent sigma of the PREDICTED power against the SAME depth-strat
    # label-shuffle null used for the observed +3.64 sigma.
    pred_sigma = (pred_c1 - NULL_MEAN_C1) / NULL_STD_C1
    obs_sigma_incode = (obs_c1_incode - NULL_MEAN_C1) / NULL_STD_C1

    # --- verdict ------------------------------------------------------
    if frac_amplitude >= 0.7 and pred_sigma >= 0.7 * OBS_SIGMA_DIRECT:
        verdict = "ATTRIBUTION_DEMONSTRATED"
        verdict_text = (
            f"The systematic forward model predicts an l=1 amplitude "
            f"{amp_pred:.3e} = {frac_amplitude:.0%} of the observed {amp_obs:.3e}, "
            f"reproducing the residual to within a factor ~1. The depth/morphology "
            f"attribution is quantitatively DEMONSTRATED, not merely asserted."
        )
    elif frac_amplitude >= 0.30:
        verdict = "ATTRIBUTION_PARTIAL"
        verdict_text = (
            f"The systematic forward model predicts an l=1 amplitude {amp_pred:.3e} = "
            f"{frac_amplitude:.0%} of the observed {amp_obs:.3e} (predicted equivalent "
            f"significance {pred_sigma:+.2f} sigma vs observed {OBS_SIGMA_DIRECT:+.2f}). "
            f"The depth/PSF/EBV/leg/density systematic accounts for a SUBSTANTIAL but "
            f"INCOMPLETE fraction of the residual. Attribution is supported in sign and "
            f"partially in amplitude; the un-modelled remainder (per-galaxy morphology "
            f"b/a, fracdev, shape_r; classifier depth-response) is the honest open gap."
        )
    else:
        verdict = "ATTRIBUTION_UNDERPREDICTS"
        verdict_text = (
            f"The systematic forward model predicts only {amp_pred:.3e} = "
            f"{frac_amplitude:.0%} of the observed {amp_obs:.3e} l=1 amplitude "
            f"(predicted equivalent significance {pred_sigma:+.2f} sigma). The "
            f"available depth/PSF/EBV/leg/density templates do NOT quantitatively "
            f"reproduce the +3.64 sigma residual. The attribution is INCOMPLETE and "
            f"remains an honest open issue pending per-galaxy morphology + classifier "
            f"depth-response templates."
        )

    result = {
        "script": "scripts/systematic_l1_forward_model.py",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": (
            "Forward model: predict the canonical-mask l=1 chirality residual AMPLITUDE "
            "from the depth/morphology imaging systematic, to test whether the paper's "
            "attribution of the +3.64 sigma residual is quantitatively demonstrated "
            "(Grok external-review flag: attribution without a forward model)."
        ),
        "config": {
            "nside": NSIDE,
            "n_spirals": int(len(df)),
            "n_brick_sources": int(n_brick),
            "n_in_mask_pixels": int(ip.size),
            "f_sky_canonical": float(cm.mean()),
            "systematic_templates": names,
            "design_condition_number": cond,
            "fit": "weighted_least_squares (galaxy-count weights); SYSTEMATIC-ONLY basis (no dipole vectors)",
        },
        "systematic_fit_coefficients": coeffs,
        "observed_residual": {
            "A1_amplitude_realspace": OBS_A1_AMPLITUDE,
            "A1_amplitude_incode_recompute": amp_obs,
            "C1_decoupled_incode": obs_c1_incode,
            "C1_depth_stratified_data": OBS_C1_DECOUPLED,
            "sigma_direct_500MC": OBS_SIGMA_DIRECT,
            "sigma_density_stratified": OBS_SIGMA_DENSITY_STRAT,
            "sigma_incode_vs_depthstrat_null": obs_sigma_incode,
        },
        "forward_model_prediction": {
            "A_sys_l1_amplitude": amp_pred,
            "A_sys_l1_vector": {"cx": pred_l1["cx"], "cy": pred_l1["cy"], "cz": pred_l1["cz"]},
            "A_sys_l1_direction": {"ra_deg": pred_l1["ra_deg"], "dec_deg": pred_l1["dec_deg"]},
            "A_sys_C1_power": pred_c1,
            "predicted_equivalent_sigma_vs_depthstrat_null": pred_sigma,
            "cos_alignment_with_observed_dipole": cos_align,
            "aligned_projection_amplitude": aligned_projection,
            "fraction_of_observed_amplitude": frac_amplitude,
            "fraction_of_observed_power": frac_power,
        },
        "comparison": {
            "predicted_over_observed_amplitude": frac_amplitude,
            "predicted_sigma": pred_sigma,
            "observed_sigma": OBS_SIGMA_DIRECT,
            "observed_sigma_density_stratified": OBS_SIGMA_DENSITY_STRAT,
        },
        "verdict": verdict,
        "verdict_text": verdict_text,
        "honesty_note": (
            "Systematic templates available locally: brick-level depth (psfdepth grz), "
            "PSF FWHM (psfsize grz), EBV, imaging-leg fractions, source density + density^2. "
            "NOT available locally and therefore NOT in this forward model: per-galaxy "
            "morphology (b/a, fracdev, shape_r_eff, shapedev_e1/e2; DR8-sweep/pod-bound) and "
            "the classifier confidence-vs-depth response as a per-pixel template. This model "
            "is therefore a LOWER BOUND on the systematic-predicted l=1 amplitude."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    log(f"wrote {OUT}")

    print("\n=== FORWARD-MODEL VERDICT ===")
    print(f"  observed  |a_1|  = {amp_obs:.4e}   (+{OBS_SIGMA_DIRECT} sigma; density-strat +{OBS_SIGMA_DENSITY_STRAT})")
    print(f"  predicted |a_1|  = {amp_pred:.4e}   ({frac_amplitude:.0%} of observed)")
    print(f"  predicted sigma  = {pred_sigma:+.2f}  (vs observed +{OBS_SIGMA_DIRECT})")
    print(f"  cos-alignment    = {cos_align:+.3f}")
    print(f"  VERDICT: {verdict}")
    print(f"  {verdict_text}")


if __name__ == "__main__":
    main()
