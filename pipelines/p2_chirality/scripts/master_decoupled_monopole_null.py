#!/usr/bin/env python3
"""
MASTER-decoupled monopole-only null × 500 — ChatGPT external review v1.0.119
BL-4 closure.

The pre-MASTER monopole-only null (already on-record in
monopole_mask_null_results.json) reproduces 99.3% of the observed
pre-MASTER pseudo-C_1 power, demonstrating the leakage channel.
ChatGPT BL-4 noted that Table I footnote b admits the POST-MASTER
monopole-only null was NOT computed, while methods text implied it
demonstrated the post-MASTER +3.64σ canonical residual. This script
closes that gap: apply MASTER mode-coupling deconvolution to each of
500 binomial-monopole null realizations on the canonical mask, then
quote the post-MASTER C_1 distribution under that null.

If the post-MASTER null distribution at ℓ=1 has mean ~ 0 and σ
comparable to the data-side null calibration, then the
+3.64σ residual IS still surprising under the monopole-only-leakage
hypothesis — i.e., the post-MASTER residual is NOT explained by
monopole-only leakage alone. If the post-MASTER null at ℓ=1 has
HIGH variance under monopole-only realizations, the +3.64σ is
absorbed within the null and the monopole-only-leakage hypothesis
remains viable.

Algorithm (mirroring canonical_l1_namaster_pod.py for the data side):
  1. Load the P4 catalog from HF; filter to spirals on canonical mask
     (f_sky = 0.49005, NSIDE=64).
  2. Build the canonical mask + apodization (C^2, 2° = none for direct
     binary; matches existing v1.0.108 canonical run).
  3. Pre-compute the MASTER coupling matrix M_{ℓℓ'} via
     nmt.NmtWorkspace.compute_coupling_matrix() with the binary mask;
     nlb=1 single-mode bandpower; lmax=191.
  4. For each of 500 binomial-monopole realizations:
     a. Draw iscw_shuf ~ Binomial(1, p_CW^global) per spiral.
     b. Build per-pixel CW-fraction map; subtract galaxy-weighted
        mask-mean monopole (v1.0.107+ proper-monopole-subtraction
        convention).
     c. Compute pseudo-C_ℓ via nmt.NmtField + nmt.compute_coupled_cell.
     d. MASTER-decouple: C_decoupled = M^{-1} pseudo_C
     e. Record decoupled C_1.
  5. Compare data post-MASTER C_1 = 1.51e-5 (v1.0.107 corrected) to
     the null distribution; quote σ and empirical-rank p-value.

Cost: ~10-30 minutes wall on a 32 GB laptop. Memory: ~2 GB.

Output: master_decoupled_monopole_null.json
"""
from __future__ import annotations
import json
import time
from pathlib import Path
import numpy as np
import pandas as pd
import healpy as hp
import pymaster as nmt
from huggingface_hub import hf_hub_download

NSIDE = 64
LMAX = 3 * NSIDE - 1  # 191
N_MC = 500
SEED = 42
OUT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/outputs/canonical_provenance/master_decoupled_monopole_null.json")


def main() -> int:
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] MASTER-decoupled monopole-only null x {N_MC}", flush=True)

    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path, columns=["ra", "dec", "class_eq"])
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals: {len(spirals):,}", flush=True)
    ra = spirals["ra"].values.astype(np.float64)
    dec = spirals["dec"].values.astype(np.float64)
    iscw = (spirals["class_eq"].values == "CW").astype(np.int8)
    p_cw_global = float(iscw.sum() / len(iscw))
    print(f"[{time.time()-t0:.1f}s] p_CW^global = {p_cw_global:.6f}", flush=True)

    npix = hp.nside2npix(NSIDE)
    pix = hp.ang2pix(NSIDE, np.radians(90.0 - dec), np.radians(ra)).astype(np.int64)
    n_total = np.bincount(pix, minlength=npix).astype(np.float64)
    mask = (n_total > 0).astype(np.float64)
    f_sky = float(mask.mean())
    print(f"[{time.time()-t0:.1f}s] f_sky (canonical mask) = {f_sky:.5f}", flush=True)

    # Pre-compute MASTER coupling matrix once
    print(f"[{time.time()-t0:.1f}s] computing MASTER coupling matrix M_lpl ...", flush=True)
    # Single-mode bandpowers (nlb=1) so we get per-ell decoupling
    b = nmt.NmtBin.from_nside_linear(NSIDE, nlb=1)
    # Dummy field on mask to compute the workspace (mask only matters for the coupling)
    dummy_map = np.zeros(npix, dtype=np.float64)
    f0_dummy = nmt.NmtField(mask, [dummy_map], lite=True)
    w = nmt.NmtWorkspace()
    w.compute_coupling_matrix(f0_dummy, f0_dummy, b)
    print(f"[{time.time()-t0:.1f}s] coupling matrix done", flush=True)

    # ---- Data side: compute data post-MASTER C_1 with proper monopole subtraction ----
    # CW-fraction map A_p (galaxy-weighted)
    n_cw_obs = np.bincount(pix[iscw.astype(bool)], minlength=npix).astype(np.float64)
    A_obs = np.zeros(npix, dtype=np.float64)
    nz = n_total > 0
    A_obs[nz] = (n_cw_obs[nz] / n_total[nz]) - 0.5  # symmetric around 0
    # Galaxy-weighted mask mean
    A_gw = float((A_obs[nz] * n_total[nz]).sum() / n_total[nz].sum())
    A_obs_sub = A_obs.copy()
    A_obs_sub[nz] -= A_gw
    A_obs_sub[~nz] = 0.0
    print(f"[{time.time()-t0:.1f}s] data A_gw (galaxy-weighted mask mean) = {A_gw:+.6f}", flush=True)
    f0_data = nmt.NmtField(mask, [A_obs_sub], lite=True)
    cl_coupled_data = nmt.compute_coupled_cell(f0_data, f0_data)
    cl_decoupled_data = w.decouple_cell(cl_coupled_data)
    # bin 0 corresponds to ell=1 with nlb=1 (bin index 0 is ell=1 since bin 0 = [1,2)).
    # Actually NmtBin.from_nside_linear(NSIDE, nlb=1) starts at ell_min=2 by default.
    # Let me check the bin effective ells.
    bin_ells = b.get_effective_ells()
    print(f"[{time.time()-t0:.1f}s] bin effective ells (first 5): {bin_ells[:5]}", flush=True)
    # For nlb=1 starting at ell=2: bin 0 -> ell 2. We need ell=1.
    # Build a custom NmtBin via bpws/ells/weights arrays:
    #   bpws[ell] = bandpower-bin index for that ell (0 for ell=1, 1 for ell=2, ...)
    #   ells[k]   = ell at position k
    #   weights[k] = weight at position k (1.0 for single-ell bins)
    print(f"[{time.time()-t0:.1f}s] re-binning to include ell=1 ...", flush=True)
    bpws = np.full(LMAX+1, -1, dtype=np.int32)
    for ell in range(1, LMAX+1):
        bpws[ell] = ell - 1   # bin 0 = ell 1, bin 1 = ell 2, etc.
    ells_arr = np.arange(LMAX+1, dtype=np.int32)
    weights_arr = np.ones(LMAX+1, dtype=np.float64)
    b_custom = nmt.NmtBin(bpws=bpws, ells=ells_arr, weights=weights_arr, lmax=LMAX)
    w_custom = nmt.NmtWorkspace()
    w_custom.compute_coupling_matrix(f0_dummy, f0_dummy, b_custom)
    cl_coupled_d = nmt.compute_coupled_cell(f0_data, f0_data)
    cl_decoupled_d = w_custom.decouple_cell(cl_coupled_d)
    bin_ells_c = b_custom.get_effective_ells()
    print(f"[{time.time()-t0:.1f}s] custom-bin effective ells (first 5): {bin_ells_c[:5]}", flush=True)
    # bin 0 is now ell=1
    decoupled_C1_data = float(cl_decoupled_d[0][0])
    print(f"[{time.time()-t0:.1f}s] decoupled C_1 (data, post-MASTER) = {decoupled_C1_data:.4e}", flush=True)

    # ---- Null side: N_MC binomial-monopole realizations through MASTER decoupling ----
    rng = np.random.default_rng(SEED)
    C1_nulls = np.zeros(N_MC, dtype=np.float64)
    t_start_nulls = time.time()
    for k in range(N_MC):
        iscw_shuf = rng.binomial(1, p_cw_global, size=len(iscw)).astype(np.bool_)
        n_cw_shuf = np.bincount(pix[iscw_shuf], minlength=npix).astype(np.float64)
        A_shuf = np.zeros(npix, dtype=np.float64)
        A_shuf[nz] = (n_cw_shuf[nz] / n_total[nz]) - 0.5
        A_gw_shuf = float((A_shuf[nz] * n_total[nz]).sum() / n_total[nz].sum())
        A_shuf_sub = A_shuf.copy()
        A_shuf_sub[nz] -= A_gw_shuf
        A_shuf_sub[~nz] = 0.0
        f0_shuf = nmt.NmtField(mask, [A_shuf_sub], lite=True)
        cl_c_shuf = nmt.compute_coupled_cell(f0_shuf, f0_shuf)
        cl_d_shuf = w_custom.decouple_cell(cl_c_shuf)
        C1_nulls[k] = float(cl_d_shuf[0][0])
        if (k+1) % 50 == 0:
            elapsed = time.time() - t_start_nulls
            rate = (k+1) / elapsed
            eta = (N_MC - k - 1) / rate
            print(f"[{time.time()-t0:.1f}s]   {k+1}/{N_MC} ({rate:.2f}/s; ETA {eta:.0f}s); current null mean={C1_nulls[:k+1].mean():.4e}, std={C1_nulls[:k+1].std(ddof=1):.4e}", flush=True)

    null_mean = float(C1_nulls.mean())
    null_std = float(C1_nulls.std(ddof=1))
    sigma_data = (decoupled_C1_data - null_mean) / max(null_std, 1e-30)
    # empirical-rank p-value
    n_exceed = int((np.abs(C1_nulls - null_mean) >= np.abs(decoupled_C1_data - null_mean)).sum())
    p_emp = (n_exceed + 1) / (N_MC + 1)

    print(f"\n[{time.time()-t0:.1f}s] === RESULTS ===", flush=True)
    print(f"  data decoupled C_1 = {decoupled_C1_data:.4e}", flush=True)
    print(f"  null mean = {null_mean:.4e}, std = {null_std:.4e}", flush=True)
    print(f"  sigma (data vs null) = {sigma_data:+.3f}", flush=True)
    print(f"  empirical-rank p (two-sided) = {p_emp:.4f} ({n_exceed}/{N_MC} more extreme)", flush=True)

    result = {
        "version": "v1.0.121-master-decoupled-monopole-null",
        "purpose": "ChatGPT external review v1.0.119 BL-4 closure: MASTER-decoupled monopole-only null x 500 on the canonical mask, with proper galaxy-weighted monopole subtraction (v1.0.107+ convention). Closes the deferred 'post-MASTER monopole-only null is not computed' caveat in Table I footnote b.",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "nside": NSIDE, "lmax": LMAX, "n_mc": N_MC, "seed": SEED,
            "f_sky": f_sky,
            "n_spirals": int(len(spirals)),
            "p_cw_global": p_cw_global,
            "A_gw_mask_mean_data": A_gw,
            "monopole_subtraction": "galaxy-weighted mask-mean (v1.0.107+ proper-monopole-subtraction convention)",
            "binning": "single-ell bandpowers via NmtBin.from_edges(arange(1, LMAX+1), arange(2, LMAX+2))",
            "compute_environment": "local laptop Apple Silicon MPS/CPU; pymaster 2.6 built from source against Homebrew libnmt + libchealpix + GSL + FFTW (libnmt 2.6 with --disable-openmp --enable-fftw-pthreads)",
        },
        "results": {
            "data_decoupled_C1": decoupled_C1_data,
            "null_mean_C1": null_mean,
            "null_std_C1": null_std,
            "sigma_data_vs_null": sigma_data,
            "empirical_rank_p_two_sided": p_emp,
            "n_exceed_null": n_exceed,
        },
        "interpretation_if_sigma_large": (
            "If the post-MASTER MC-decoupled monopole-only null shows the data "
            "+3.64sigma residual is STILL inconsistent with the monopole-only null "
            "(|sigma| >> 1), then monopole-only leakage alone does NOT account for "
            "the post-MASTER residual — the +3.64sigma must include a depth/PSF/"
            "morphology systematic component beyond pure monopole-mask leakage."
        ),
        "interpretation_if_sigma_small": (
            "If the post-MASTER MC-decoupled monopole-only null is consistent with "
            "the data (|sigma| < 1), then monopole-only leakage DOES account for "
            "the post-MASTER residual under MASTER decoupling, vindicating the "
            "v1.0.119 paper's leakage-only hypothesis for the canonical-mask residual."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
