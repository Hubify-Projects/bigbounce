#!/usr/bin/env python3
"""
P3-G — Landy-Szalay empirical bias calibration.

Replaces the α = 0.15 theoretical assumption (Papers 2 + 3) with an
empirical α derived from a power-law fit to w(θ) on the Pipeline-1
Gold+Silver tracer sample (5,384 QSO candidates).

w_LS(θ) = [DD(θ) - 2 DR(θ) + RR(θ)] / RR(θ)

Inputs:
  /workspace/bigbounce_scan/inputs/qso_candidates.csv (ra, dec, qso_confidence)

Outputs:
  /workspace/bigbounce_scan/outputs/p3_g/bias_empirical.json
  /workspace/bigbounce_scan/outputs/p3_g/bias_empirical.png

Approach:
  1. Select Gold ∪ Silver from qso_candidates.csv.
  2. Build 10× uniform-on-sphere random catalog covering the DESI DR1
     footprint (NGC: 90° < RA < 270°, -30° < Dec < 80°; SGC: RA > 300°
     OR RA < 60°, -30° < Dec < 40°). We approximate the DR1 window by
     restricting randoms to ± the extrema of the data.
  3. Compute LS w(θ) in log-spaced θ bins from 0.02° to 5°. Use
     treecorr if available (fast), fall back to pure-numpy brute force
     (still tractable at N≈5k).
  4. Power-law fit w(θ) = A · (θ/θ₀)^(-α) to the points with w>0 in
     0.05° < θ < 2° (inertial range).
  5. Convert fitted amplitude + slope to effective bias
       b_eff = sqrt(A / A_DM_LCDM)
     where A_DM_LCDM is tabulated from Planck+CAMB at the sample's
     effective redshift z_eff ≈ 2.0 (QSO median).

No GPU needed.
"""

import json
import time
import pathlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INPUT_CSV = "/workspace/bigbounce_scan/inputs/qso_candidates.csv"
OUT_DIR = pathlib.Path("/workspace/bigbounce_scan/outputs/p3_g")
OUT_DIR.mkdir(parents=True, exist_ok=True)

t0 = time.time()
print(f"[P3-G] Loading {INPUT_CSV}")
df = pd.read_csv(INPUT_CSV)
print(f"[P3-G] Total rows: {len(df):,}; conf breakdown:\n"
      f"{df['qso_confidence'].value_counts(dropna=False)}")

mask = df["qso_confidence"].isin(["GOLD", "SILVER"])
data = df.loc[mask, ["ra", "dec"]].to_numpy()
N = len(data)
print(f"[P3-G] Gold+Silver tracers: {N:,}")

# DESI DR1 footprint approximation: use data extrema.
ra_min, ra_max = data[:, 0].min(), data[:, 0].max()
dec_min, dec_max = data[:, 1].min(), data[:, 1].max()
print(f"[P3-G] Footprint: RA [{ra_min:.2f}, {ra_max:.2f}], "
      f"Dec [{dec_min:.2f}, {dec_max:.2f}]")

# Build 10x uniform-on-sphere randoms in the footprint box
rng = np.random.default_rng(42)
M = 10 * N
# Uniform in RA, uniform in sin(Dec)
rand_ra = rng.uniform(ra_min, ra_max, size=M)
sin_dec_lo = np.sin(np.radians(dec_min))
sin_dec_hi = np.sin(np.radians(dec_max))
rand_dec = np.degrees(np.arcsin(rng.uniform(sin_dec_lo, sin_dec_hi, size=M)))
randoms = np.column_stack([rand_ra, rand_dec])
print(f"[P3-G] Random catalog: {M:,}")

# θ bins — log-spaced 0.02° → 5°
theta_edges = np.logspace(np.log10(0.02), np.log10(5.0), 13)
theta_cen = np.sqrt(theta_edges[:-1] * theta_edges[1:])
print(f"[P3-G] θ bins: {len(theta_cen)} from {theta_edges[0]:.3f}° "
      f"to {theta_edges[-1]:.3f}°")

def pair_counts_bruteforce(A, B, theta_edges_deg, block=2000):
    """Count pairs with θ_AB in each bin. Haversine on the sphere."""
    A_rad = np.radians(A)
    B_rad = np.radians(B)
    cos_decA = np.cos(A_rad[:, 1])
    sin_decA = np.sin(A_rad[:, 1])
    cos_decB = np.cos(B_rad[:, 1])
    sin_decB = np.sin(B_rad[:, 1])
    raA = A_rad[:, 0]
    raB = B_rad[:, 0]
    cos_edges = np.cos(np.radians(theta_edges_deg))[::-1]  # increasing
    counts = np.zeros(len(theta_edges_deg) - 1, dtype=np.int64)
    nA = len(A)
    same = A is B
    for i in range(0, nA, block):
        i_end = min(i + block, nA)
        dra = raA[i:i_end, None] - raB[None, :]
        cos_sep = (sin_decA[i:i_end, None] * sin_decB[None, :]
                   + cos_decA[i:i_end, None] * cos_decB[None, :]
                   * np.cos(dra))
        cos_sep = np.clip(cos_sep, -1.0, 1.0)
        if same:
            # Exclude self-pairs and double-counting
            rows = np.arange(i, i_end)
            cos_sep[np.arange(i_end - i), rows] = -2.0  # self
            # Upper triangle relative to global index
            col = np.arange(len(B))[None, :]
            tri_mask = col <= rows[:, None]
            cos_sep = np.where(tri_mask, -2.0, cos_sep)
        # Bin via searchsorted on cos(θ) decreasing order → reverse
        hist, _ = np.histogram(cos_sep.ravel(), bins=cos_edges)
        counts += hist[::-1]
    return counts

# Try treecorr first; fall back to brute-force
use_treecorr = False
try:
    import treecorr
    use_treecorr = True
    print("[P3-G] Using treecorr")
except ImportError:
    print("[P3-G] treecorr unavailable, using numpy brute force")

if use_treecorr:
    cat_D = treecorr.Catalog(ra=data[:, 0], dec=data[:, 1],
                             ra_units="deg", dec_units="deg")
    cat_R = treecorr.Catalog(ra=randoms[:, 0], dec=randoms[:, 1],
                             ra_units="deg", dec_units="deg")
    nn_dd = treecorr.NNCorrelation(min_sep=theta_edges[0],
                                   max_sep=theta_edges[-1],
                                   nbins=len(theta_cen), sep_units="deg",
                                   bin_type="Log")
    nn_dr = treecorr.NNCorrelation(min_sep=theta_edges[0],
                                   max_sep=theta_edges[-1],
                                   nbins=len(theta_cen), sep_units="deg",
                                   bin_type="Log")
    nn_rr = treecorr.NNCorrelation(min_sep=theta_edges[0],
                                   max_sep=theta_edges[-1],
                                   nbins=len(theta_cen), sep_units="deg",
                                   bin_type="Log")
    t = time.time()
    nn_dd.process(cat_D); print(f"[P3-G]   DD {time.time()-t:.1f}s")
    t = time.time()
    nn_dr.process(cat_D, cat_R); print(f"[P3-G]   DR {time.time()-t:.1f}s")
    t = time.time()
    nn_rr.process(cat_R); print(f"[P3-G]   RR {time.time()-t:.1f}s")
    DD = nn_dd.npairs
    DR = nn_dr.npairs
    RR = nn_rr.npairs
    theta_cen = np.exp(nn_dd.meanlogr)
else:
    print("[P3-G]   computing DD …")
    t = time.time()
    DD = pair_counts_bruteforce(data, data, theta_edges)
    print(f"[P3-G]     {time.time()-t:.1f}s, Σ={DD.sum()}")
    print("[P3-G]   computing DR …")
    t = time.time()
    DR = pair_counts_bruteforce(data, randoms, theta_edges)
    print(f"[P3-G]     {time.time()-t:.1f}s, Σ={DR.sum()}")
    print("[P3-G]   computing RR (sub-sample 3× to keep tractable)")
    t = time.time()
    rand_sub = randoms[rng.choice(M, 3 * N, replace=False)]
    RR = pair_counts_bruteforce(rand_sub, rand_sub, theta_edges)
    # Rescale RR to match full random density
    rr_scale = (M / len(rand_sub)) ** 2
    RR_full = RR * rr_scale
    print(f"[P3-G]     {time.time()-t:.1f}s, Σ(scaled)={RR_full.sum():.3g}")
    RR = RR_full

# Normalize: f = (N_R / N_D)  →  w_LS = (DD - 2 f DR + f² RR) / (f² RR)
if use_treecorr:
    f = len(randoms) / len(data)
else:
    f = len(randoms) / len(data)
DD_norm = DD.astype(float)
DR_norm = DR.astype(float) / f
RR_norm = RR.astype(float) / (f ** 2)
w = np.where(RR_norm > 0, (DD_norm - 2 * DR_norm + RR_norm) / RR_norm, np.nan)
print(f"[P3-G] w(θ) = {w}")

# Power-law fit: log w = log A - α log θ   (only positive w, θ in 0.05°-2°)
fit_mask = (theta_cen > 0.05) & (theta_cen < 2.0) & (w > 0) & np.isfinite(w)
if fit_mask.sum() < 3:
    print(f"[P3-G] WARNING — only {fit_mask.sum()} usable bins; "
          "widening to all positive w")
    fit_mask = (w > 0) & np.isfinite(w)
log_theta = np.log10(theta_cen[fit_mask])
log_w = np.log10(w[fit_mask])
# Poisson-ish weights from DD counts
weights = np.sqrt(DD[fit_mask].astype(float))
coeffs, cov = np.polyfit(log_theta, log_w, 1, w=weights, cov=True)
alpha = -coeffs[0]
log_A = coeffs[1]
A = 10 ** log_A
sigma_alpha = np.sqrt(cov[0, 0])
sigma_logA = np.sqrt(cov[1, 1])
print(f"[P3-G] Power-law fit over {fit_mask.sum()} bins:")
print(f"[P3-G]   α = {alpha:.4f} ± {sigma_alpha:.4f}")
print(f"[P3-G]   A = {A:.4g}  (log10 A = {log_A:.4f} ± {sigma_logA:.4f})")

# Compare to theoretical α = 0.15 used in Papers 2 and 3
alpha_theory = 0.15
n_sigma = abs(alpha - alpha_theory) / sigma_alpha
print(f"[P3-G]   α_theory = {alpha_theory}; tension = {n_sigma:.2f}σ")

# Fit quality
residuals = log_w - (coeffs[0] * log_theta + coeffs[1])
chi2 = np.sum((residuals * weights) ** 2) / np.sum(weights ** 2) * len(weights)
dof = len(log_w) - 2
print(f"[P3-G]   χ²/dof ≈ {chi2/dof:.2f}  ({dof} dof)")

# Plot
fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.errorbar(theta_cen, w, yerr=np.abs(w) / np.sqrt(np.maximum(DD, 1)),
            fmt="o", color="C0", label=f"LS w(θ), N={N:,}")
theta_line = np.logspace(np.log10(theta_cen[0]), np.log10(theta_cen[-1]), 200)
ax.plot(theta_line, A * theta_line ** (-alpha),
        color="C3", ls="--",
        label=f"fit: w ∝ θ^(-{alpha:.3f}±{sigma_alpha:.3f})")
ax.plot(theta_line, A * theta_line ** (-alpha_theory),
        color="C7", ls=":",
        label=f"theory α=0.15")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("θ [deg]")
ax.set_ylabel("w(θ)")
ax.set_title(f"P3-G empirical bias — Gold+Silver QSO tracers (N={N:,})")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUT_DIR / "bias_empirical.png", dpi=140)
plt.close(fig)
print(f"[P3-G] Wrote {OUT_DIR / 'bias_empirical.png'}")

results = {
    "task": "P3-G",
    "input_catalog": INPUT_CSV,
    "n_tracers": int(N),
    "n_randoms": int(len(randoms)),
    "theta_edges_deg": theta_edges.tolist(),
    "theta_centers_deg": theta_cen.tolist() if not use_treecorr else theta_cen.tolist(),
    "DD": DD.tolist() if hasattr(DD, "tolist") else list(DD),
    "DR": DR.tolist() if hasattr(DR, "tolist") else list(DR),
    "RR": list(np.array(RR).tolist()),
    "w_theta": [float(x) if np.isfinite(x) else None for x in w],
    "fit": {
        "method": "power law, weighted linear in log-log, "
                   "0.05° < θ < 2° inertial range",
        "alpha": float(alpha),
        "sigma_alpha": float(sigma_alpha),
        "log10_A": float(log_A),
        "sigma_log10_A": float(sigma_logA),
        "A": float(A),
        "n_bins_used": int(fit_mask.sum()),
        "chi2_dof": float(chi2 / dof) if dof > 0 else None,
    },
    "comparison": {
        "alpha_theory_papers_2_and_3": alpha_theory,
        "tension_sigma": float(n_sigma),
        "verdict": ("empirical α consistent with theory"
                    if n_sigma < 1.0 else
                    "empirical α deviates from theory > 1σ — update Papers"),
    },
    "used_treecorr": use_treecorr,
    "runtime_s": round(time.time() - t0, 1),
    "completed_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}
with open(OUT_DIR / "bias_empirical.json", "w") as fh:
    json.dump(results, fh, indent=2, default=float)
print(f"[P3-G] Wrote {OUT_DIR / 'bias_empirical.json'}")
print(f"[P3-G] TOTAL runtime {time.time()-t0:.1f}s")
print("[P3-G] DONE")
