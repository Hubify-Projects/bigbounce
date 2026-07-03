#!/usr/bin/env python3
"""
EXTENDED forward model of the canonical-mask ell=1 chirality residual with
REAL per-galaxy DR8-sweep MORPHOLOGY (b/a, fracdev, shape_r) added to the
imaging systematic basis.

CONTEXT (2026-07-02, AUTHORIZED REAL COMPUTE):
  Imaging-only forward model reproduces 54% of the +3.64 sigma canonical-mask
  l=1 chirality residual (cos +0.83). The ~46% remainder was flagged as
  un-modelled pending per-galaxy morphology. This script pulls the DR8-sweep
  morphology for the 3.2M spirals (see pull_dr8_morph.py), builds b/a, fracdev,
  shape_r per-galaxy templates, orthogonalizes them against the imaging basis,
  re-fits the chirality field, projects onto l=1 (canonical mask), and measures
  the EXTENDED fraction vs 54%.

METHOD: identical NSIDE=64 chirality field / canonical |b|>15 mask / brick
  depth-PSF-EBV-leg-density templates as systematic_l1_forward_model.py; ADDS
  three galaxy-count-weighted per-pixel morphology templates orthogonalized
  against the imaging basis (so they carry only the morphology info not already
  in imaging), fit by WLS, projected to l=1.

  Per-galaxy morphology from DR8 sweeps:
    b/a       = (1-|e|)/(1+|e|), |e|=sqrt(e1^2+e2^2) from SHAPEDEV/SHAPEEXP
                (deV shape if TYPE in {DEV,COMP} else EXP shape)
    fracdev   = FRACDEV (0=exp .. 1=deV)
    shape_r   = effective radius (SHAPEDEV_R if deV-ish else SHAPEEXP_R)

NEVER fabricate. Report the real measured extended fraction.
Output: outputs/systematic_l1_forward_model_dr8morph.json  (written on pod;
        also mirrored back to the repo)
"""
from __future__ import annotations
import json, time, urllib.request
from pathlib import Path
import numpy as np, healpy as hp, pandas as pd
from astropy.io import fits
from huggingface_hub import hf_hub_download

NSIDE = 64
WORK = Path("/workspace/dr8morph")
CACHE = Path("/tmp/p4_brick_cache"); CACHE.mkdir(exist_ok=True)
URL_NORTH = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/north/survey-bricks-dr8-north.fits.gz"
URL_SOUTH = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr8/south/survey-bricks-dr8-south.fits.gz"
MORPH = WORK / "out" / "spiral_morphology.parquet"
OUT = WORK / "out" / "systematic_l1_forward_model_dr8morph.json"

OBS_A1_AMPLITUDE = 0.007040031846243215
OBS_C1_DECOUPLED = 2.348109981323473e-05
OBS_SIGMA_DIRECT = 3.64
OBS_SIGMA_DENSITY_STRAT = 3.80
NULL_MEAN_C1 = 1.7113319696431786e-06
NULL_STD_C1 = 3.052393324112356e-06
IMAGING_ONLY_FRAC_AMP_PRIOR = 0.5389442635381818

t0 = time.time()
def log(m): print(f"[{time.time()-t0:6.1f}s] {m}", flush=True)

def canonical_mask(nside):
    npix = hp.nside2npix(nside)
    theta, phi = hp.pix2ang(nside, np.arange(npix))
    theta_g, _ = hp.Rotator(coord=["C","G"])(theta, phi)
    b = 90.0 - np.degrees(theta_g)
    return (np.abs(b) > 15.0).astype(float)

def download_bricks():
    paths = {}
    for tag, url in [("north",URL_NORTH),("south",URL_SOUTH)]:
        local = CACHE / Path(url).name
        if not local.exists():
            log(f"downloading {tag} bricks"); urllib.request.urlretrieve(url, local)
        paths[tag] = local
    return paths

def load_brick_templates(paths):
    frames = []
    for tag,p in paths.items():
        with fits.open(p) as hdu:
            t = hdu[1].data
            frames.append(pd.DataFrame({c: t[c] for c in t.columns.names if t[c].ndim==1}))
    bricks = pd.concat(frames, ignore_index=True)
    psf = [c for c in bricks.columns if c.lower().startswith("psfsize_")]
    dep = [c for c in bricks.columns if c.lower().startswith("psfdepth_")]
    bricks["psf_mean"] = bricks[psf].astype(np.float32).mean(axis=1)
    bricks["depth_mean"] = bricks[dep].astype(np.float32).mean(axis=1)
    return bricks, len(bricks)

def alm_l1(field):
    alm = hp.map2alm(field.astype(np.float64), lmax=2, iter=1)
    a10 = alm[hp.Alm.getidx(2,1,0)]; a11 = alm[hp.Alm.getidx(2,1,1)]
    cz = float(np.real(a10)); cx = -2.0*float(np.real(a11)); cy = 2.0*float(np.imag(a11))
    amp = float(np.sqrt(cx**2+cy**2+cz**2))
    if amp>0:
        ra = float(np.degrees(np.arctan2(cy,cx))%360); dec = float(np.degrees(np.arcsin(np.clip(cz/amp,-1,1))))
    else: ra=dec=0.0
    return {"amplitude":amp,"cx":cx,"cy":cy,"cz":cz,"ra_deg":ra,"dec_deg":dec}

def c1_power(field):
    alm = hp.map2alm(field.astype(np.float64), lmax=2, iter=1)
    return float(hp.alm2cl(alm, lmax=2)[1])

def main():
    # --- catalog + chirality field + per-galaxy dr8_id -------------------
    log("loading P4 catalog from HF")
    cat = hf_hub_download("bamfai/galaxy-chirality-catalog","catalog_production.parquet",repo_type="dataset")
    df = pd.read_parquet(cat, columns=["dr8_id","ra","dec","class_eq"])
    df = df.loc[df["class_eq"].isin(["CW","CCW"])].reset_index(drop=True)
    bo = df["dr8_id"].str.split("_", expand=True)
    df["BRICKID"] = bo[0].astype("int64"); df["OBJID"] = bo[1].astype("int64")
    is_cw = (df["class_eq"].values=="CW").astype(np.int8)
    ra = df["ra"].values.astype(np.float64); dec = df["dec"].values.astype(np.float64)
    log(f"spirals: {len(df):,}")

    # --- REAL DR8-sweep morphology join ----------------------------------
    m = pd.read_parquet(MORPH)
    log(f"morphology rows pulled: {len(m):,}")
    # b/a from ellipticity; pick deV shape for deV-ish TYPE else EXP
    def ba_from(e1,e2):
        e = np.sqrt(np.asarray(e1,float)**2 + np.asarray(e2,float)**2)
        e = np.clip(e, 0, 0.999)
        return (1.0-e)/(1.0+e)
    typ = m["TYPE"].astype(str).str.upper().values
    dev_like = np.isin(typ, ["DEV","COMP","SER"]) | (m["FRACDEV"].values >= 0.5)
    ba_dev = ba_from(m["SHAPEDEV_E1"], m["SHAPEDEV_E2"])
    ba_exp = ba_from(m["SHAPEEXP_E1"], m["SHAPEEXP_E2"])
    m["b_over_a"] = np.where(dev_like, ba_dev, ba_exp)
    r_dev = np.asarray(m["SHAPEDEV_R"],float); r_exp = np.asarray(m["SHAPEEXP_R"],float)
    m["shape_r"] = np.where(dev_like, r_dev, r_exp)
    m["fracdev"] = np.asarray(m["FRACDEV"],float)
    # PSF/point sources have zero shape -> b/a=1, r=0; keep but mark
    m = m[["BRICKID","OBJID","b_over_a","fracdev","shape_r"]]
    df = df.merge(m, on=["BRICKID","OBJID"], how="left")
    matched = df["b_over_a"].notna()
    log(f"morphology matched to {matched.sum():,} / {len(df):,} spirals "
        f"({100*matched.mean():.1f}%)")
    # fill unmatched with median so they don't bias the pixel means
    for col in ["b_over_a","fracdev","shape_r"]:
        med = np.nanmedian(df[col].values)
        df[col] = df[col].fillna(med).values
    ba_g = df["b_over_a"].values.astype(np.float64)
    fd_g = df["fracdev"].values.astype(np.float64)
    sr_g = df["shape_r"].values.astype(np.float64)
    sr_g = np.clip(sr_g, 0, np.nanpercentile(sr_g, 99.5))  # tame the tail

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0-dec), np.radians(ra))
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    n_cw = np.bincount(pix[is_cw==1], minlength=npix).astype(np.float64)
    nz = n_total > 0
    A_p = np.zeros(npix); A_p[nz] = 2.0*(n_cw[nz]/n_total[nz]) - 1.0

    bricks, n_brick = load_brick_templates(download_bricks())
    from scipy.spatial import cKDTree
    def to_xyz(r,d):
        rr,dd = np.deg2rad(r),np.deg2rad(d); cd=np.cos(dd)
        return np.column_stack([np.cos(rr)*cd, np.sin(rr)*cd, np.sin(dd)])
    tree = cKDTree(to_xyz(bricks["ra"].values, bricks["dec"].values))
    log("cross-matching galaxies -> bricks")
    _, idx = tree.query(to_xyz(ra,dec), k=1, workers=-1)
    psf_g = bricks["psf_mean"].values[idx]; depth_g = bricks["depth_mean"].values[idx]
    ebv_g = bricks["ebv"].values[idx] if "ebv" in bricks.columns else np.zeros(len(df))
    depth_g = np.asarray(depth_g,float); depth_g[~np.isfinite(depth_g)] = np.nanmedian(depth_g[np.isfinite(depth_g)])

    def pixmean(vals):
        vals = np.asarray(vals,float)
        s = np.bincount(pix, weights=vals, minlength=npix).astype(np.float64)
        m2 = np.zeros(npix); m2[nz] = s[nz]/n_total[nz]; return m2
    psf_map=pixmean(psf_g); depth_map=pixmean(depth_g); ebv_map=pixmean(ebv_g)
    ba_map=pixmean(ba_g); fd_map=pixmean(fd_g); sr_map=pixmean(sr_g)
    for arr in (psf_map,depth_map,ebv_map,ba_map,fd_map,sr_map): arr[~np.isfinite(arr)]=0.0

    dec_lo,dec_hi = -20.0,32.0
    bass=(dec>dec_hi); decals=(dec>=dec_lo)&(dec<=dec_hi)
    n_bass=np.bincount(pix[bass],minlength=npix).astype(np.float64)
    n_decals=np.bincount(pix[decals],minlength=npix).astype(np.float64)

    cm = canonical_mask(NSIDE); in_mask=(cm>0)&nz; ip=np.where(in_mask)[0]; w=n_total[ip]
    log(f"in-mask pixels {ip.size:,}  f_sky={cm.mean():.4f}")
    def wcenter(x): return x - np.average(x[ip], weights=w)
    safe=np.maximum(n_total,1.0)
    f_bass=wcenter(n_bass/safe); f_decals=wcenter(n_decals/safe)
    rho=n_total/max(n_total[ip].mean(),1.0); rho_c=wcenter(rho); rho_sq=wcenter(rho_c**2)
    psf_c=wcenter(psf_map); depth_c=wcenter(depth_map); ebv_c=wcenter(ebv_map)
    ba_c=wcenter(ba_map); fd_c=wcenter(fd_map); sr_c=wcenter(sr_map)
    A_p_corr=wcenter(A_p)

    imaging_tmpl = {"f_BASS_rel_DES":f_bass,"f_DECaLS_rel_DES":f_decals,"rho_p":rho_c,
                    "rho_p_sq":rho_sq,"psf_mean":psf_c,"depth_mean":depth_c,"ebv":ebv_c}
    imaging_names=list(imaging_tmpl.keys())
    Timg=np.column_stack([imaging_tmpl[n][ip] for n in imaging_names]+[np.ones(ip.size)])
    swp=np.sqrt(w); Timg_w=Timg*swp[:,None]
    def orth_off_imaging(vec_full):
        y=vec_full[ip]*swp; beta=np.linalg.lstsq(Timg_w,y,rcond=None)[0]
        resid=y-Timg_w@beta; out=np.zeros(npix); out[ip]=resid/swp
        s=np.sqrt(np.average(out[ip]**2,weights=w))
        if s>0: out[ip]/=s
        return out
    # orthogonalized morphology templates (independent of imaging)
    ba_indep=orth_off_imaging(ba_c); fd_indep=orth_off_imaging(fd_c); sr_indep=orth_off_imaging(sr_c)
    morph_tmpl={"b_over_a_indep":ba_indep,"fracdev_indep":fd_indep,"shape_r_indep":sr_indep}
    ext_tmpl={**imaging_tmpl,**morph_tmpl}

    def fit_and_project(tmpl):
        names=list(tmpl.keys())
        T=np.column_stack([tmpl[n][ip] for n in names]+[np.ones(ip.size)])
        sw=np.sqrt(w)
        a_hat,*_=np.linalg.lstsq(T*sw[:,None], A_p_corr[ip]*sw, rcond=None)
        coeffs={n:float(v) for n,v in zip(names+["const"],a_hat)}
        cond=float(np.linalg.cond(T))
        A_sys=np.zeros(npix)
        for n in names: A_sys[ip]+=coeffs[n]*tmpl[n][ip]
        A_sys_m=A_sys*(cm>0)
        return coeffs,cond,alm_l1(A_sys_m),c1_power(A_sys_m)

    A_obs_masked=np.zeros(npix); A_obs_masked[ip]=A_p_corr[ip]; A_obs_masked*=(cm>0)
    obs_l1=alm_l1(A_obs_masked); obs_c1=c1_power(A_obs_masked)
    v_obs=np.array([obs_l1["cx"],obs_l1["cy"],obs_l1["cz"]]); amp_obs=float(np.linalg.norm(v_obs))

    base_coeffs,base_cond,base_l1,base_c1=fit_and_project(imaging_tmpl)
    ext_coeffs,ext_cond,ext_l1,ext_c1=fit_and_project(ext_tmpl)
    log(f"imaging cond={base_cond:.2e} extended cond={ext_cond:.2e}")

    def metrics(l1,c1,label):
        v=np.array([l1["cx"],l1["cy"],l1["cz"]]); amp=float(np.linalg.norm(v))
        cos=float(np.dot(v,v_obs)/(amp*amp_obs)) if amp*amp_obs>0 else 0.0
        frac=amp/amp_obs if amp_obs>0 else 0.0
        aligned=amp*cos; frac_al=aligned/amp_obs if amp_obs>0 else 0.0
        log(f"{label:16s} |a1|={amp:.4e} frac={frac:.1%} cos={cos:+.3f} aligned-frac={frac_al:.1%}")
        return {"l1_amplitude":amp,"l1_vector":{"cx":l1["cx"],"cy":l1["cy"],"cz":l1["cz"]},
                "l1_direction":{"ra_deg":l1["ra_deg"],"dec_deg":l1["dec_deg"]},"C1_power":c1,
                "cos_alignment":cos,"fraction_of_observed_amplitude":frac,
                "fraction_of_observed_power":(c1/obs_c1 if obs_c1>0 else 0.0),
                "aligned_projection_amplitude":aligned,
                "fraction_of_observed_amplitude_aligned":frac_al,
                "predicted_equivalent_sigma_vs_depthstrat_null":(c1-NULL_MEAN_C1)/NULL_STD_C1}
    base_m=metrics(base_l1,base_c1,"imaging-only")
    ext_m=metrics(ext_l1,ext_c1,"imaging+dr8morph")

    ext_frac=ext_m["fraction_of_observed_amplitude"]; base_frac=base_m["fraction_of_observed_amplitude"]
    delta=ext_frac-base_frac; remainder=1.0-ext_frac

    if ext_frac>=0.70:
        verdict="RESIDUAL_LARGELY_SYSTEMATIC"
        vtext=(f"Adding REAL per-galaxy DR8-sweep morphology (b/a, fracdev, shape_r) raises the "
               f"forward-modelled l=1 fraction to {ext_frac:.0%} (from {base_frac:.0%} imaging-only, "
               f"+{delta*100:.1f} pts). Imaging+morphology reproduces most of the +3.64 sigma residual "
               f"-> the residual is largely SYSTEMATIC, strengthening the null.")
    elif delta>=0.03:
        verdict="PARTIAL_IMPROVEMENT_HONEST_REMAINDER"
        vtext=(f"Real DR8-sweep morphology adds +{delta*100:.1f} pts, raising the forward-modelled "
               f"l=1 fraction to {ext_frac:.0%} (from {base_frac:.0%} imaging-only). A real un-modelled "
               f"remainder of {remainder:.0%} persists.")
    else:
        verdict="NO_MEANINGFUL_IMPROVEMENT"
        vtext=(f"Real DR8-sweep morphology changes the forward-modelled l=1 fraction by only "
               f"{delta*100:+.1f} pts ({base_frac:.0%} -> {ext_frac:.0%}). Per-galaxy morphology, "
               f"orthogonalized against imaging, adds little to the l=1 projection. The ~half remainder "
               f"stays a genuine open item.")

    result={"script":"scripts/systematic_l1_forward_model_dr8morph.py",
            "date_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
            "purpose":("EXTENDED forward model with REAL per-galaxy DR8-sweep morphology "
                       "(b/a, fracdev, shape_r) added to the imaging systematic basis; measures the "
                       "forward-modelled fraction of the +3.64 sigma canonical-mask l=1 residual."),
            "config":{"nside":NSIDE,"n_spirals":int(len(df)),
                      "n_morphology_matched":int(matched.sum()),
                      "morphology_match_fraction":float(matched.mean()),
                      "n_brick_sources":int(n_brick),"n_in_mask_pixels":int(ip.size),
                      "f_sky_canonical":float(cm.mean()),
                      "imaging_templates":list(imaging_tmpl.keys()),
                      "added_morphology_templates":list(morph_tmpl.keys()),
                      "imaging_only_condition_number":base_cond,"extended_condition_number":ext_cond,
                      "fit":"WLS (galaxy-count weights); SYSTEMATIC-ONLY basis"},
            "imaging_only_fit_coefficients":base_coeffs,"extended_fit_coefficients":ext_coeffs,
            "observed_residual":{"A1_amplitude_realspace":OBS_A1_AMPLITUDE,
                "A1_amplitude_incode_recompute":amp_obs,"C1_decoupled_incode":obs_c1,
                "C1_depth_stratified_data":OBS_C1_DECOUPLED,"sigma_direct_500MC":OBS_SIGMA_DIRECT,
                "sigma_density_stratified":OBS_SIGMA_DENSITY_STRAT},
            "imaging_only_forward_model":base_m,"extended_forward_model":ext_m,
            "improvement":{"imaging_only_fraction":base_frac,"extended_fraction":ext_frac,
                "delta_fraction_points":delta,"un_modelled_remainder":remainder,
                "imaging_only_cos_alignment":base_m["cos_alignment"],
                "extended_cos_alignment":ext_m["cos_alignment"],
                "prior_committed_imaging_only_fraction":IMAGING_ONLY_FRAC_AMP_PRIOR},
            "verdict":verdict,"verdict_text":vtext,
            "provenance":("Per-galaxy morphology pulled REAL from DESI Legacy DR8 sweep catalogs "
                          "(south 8.0 + north 8.0, columns BRICKID/OBJID/TYPE/FRACDEV/SHAPEDEV_*/"
                          "SHAPEEXP_*), joined to spirals by dr8_id=BRICKID_OBJID. NOT fabricated.")}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    log(f"wrote {OUT}")
    print("\n=== EXTENDED (imaging+DR8 morphology) FORWARD-MODEL VERDICT ===")
    print(f"  observed |a1| = {amp_obs:.4e}  (+{OBS_SIGMA_DIRECT} sigma)")
    print(f"  imaging-only fraction   = {base_frac:.1%}  (cos {base_m['cos_alignment']:+.3f})")
    print(f"  imaging+DR8-morphology  = {ext_frac:.1%}  (cos {ext_m['cos_alignment']:+.3f})")
    print(f"  delta = {delta*100:+.1f} pts;  remainder {remainder:.1%}")
    print(f"  morphology matched: {matched.sum():,}/{len(df):,} ({100*matched.mean():.1f}%)")
    print(f"  VERDICT: {verdict}")

if __name__ == "__main__":
    main()
