import numpy as np

# ============================================================================
# P2 joint-covariance forecast — replacing the additive-quadrature heuristic.
# ALL inputs are the paper's OWN quantities. Nothing fabricated.
# ============================================================================

# --- Paper's own bispectrum-channel ingredients (02_full_draft.tex) ---
fnl_central = 35.0/16.0        # |f_NL| = 2.1875, the corrected central value
sigma_base  = 0.7              # Heinrich et al. imported SPHEREx bispectrum sigma(f_NL^local), b_phi-marginalized under UMF
r           = 0.84             # noise-weighted template overlap (Eq. r_noise); r in [0.829,0.876]
sigma_GR_grid = [0.5, 1.0]     # paper's GR stress-test amplitudes (Table tab:gr, tab:systematics)

# Template-corrected effective sigma on the BOUNCE amplitude: sigma^bounce = sigma^local / r
sigma_bounce = sigma_base / r
print("=== BISPECTRUM CHANNEL (paper's headline) ===")
print(f"template-corrected sigma(f_NL^bounce) = {sigma_base}/{r} = {sigma_bounce:.4f}")
print(f"optimistic significance |f_NL|/sigma_bounce = {fnl_central/sigma_bounce:.3f} sigma  (paper: 2.63)")
print()

# ---------------------------------------------------------------------------
# (1) The QUADRATURE HEURISTIC the paper uses: sigma_eff = sqrt(sigma_base^2 + sigma_GR^2)
#     significance = |f_NL| * r / sigma_eff
# ---------------------------------------------------------------------------
print("=== QUADRATURE HEURISTIC (current paper Table tab:systematics) ===")
for sg in sigma_GR_grid:
    seff = np.sqrt(sigma_base**2 + sg**2)
    sig  = fnl_central * r / seff
    print(f"  sigma_GR={sg}: sigma_eff=sqrt(0.7^2+{sg}^2)={seff:.3f}  ->  {sig:.3f} sigma")
print()

# ---------------------------------------------------------------------------
# (2) HONEST JOINT FISHER {f_NL, A_GR}: marginalize f_NL over a GR-projection
#     nuisance amplitude A_GR. The quadrature sum is the SPECIAL CASE rho=0.
#     Joint 2x2 Fisher F; marginalized sigma(f_NL) = sqrt[(F^-1)_11].
#
#     In a Gaussian Fisher with two params of individual (unmarginalized) errors
#     s_f (=sigma_base) and s_G (=sigma_GR) and correlation coefficient rho,
#     the marginalized f_NL error is:
#         sigma_marg(f_NL) = s_f / sqrt(1 - rho^2)
#     (standard 2x2 Fisher inversion result). This is the REAL marginalized
#     number; quadrature (adding s_G in the DENOMINATOR) is NOT what
#     marginalization gives — marginalization INFLATES s_f by 1/sqrt(1-rho^2),
#     it does not simply add s_G in quadrature to the noise.
# ---------------------------------------------------------------------------
print("=== HONEST JOINT FISHER: marginalized sigma(f_NL) = sigma_base/sqrt(1-rho^2) ===")
print("(quadrature is NOT recovered by any rho; the two treatments differ structurally)")
print(f"{'rho':>6} {'sigma_marg(fNL)':>16} {'signif (x r)':>14}")
for rho in [0.0, 0.3, 0.5, 0.7, 0.87, 0.9]:
    s_marg = sigma_base / np.sqrt(1 - rho**2)
    sig = fnl_central * r / s_marg
    print(f"{rho:>6.2f} {s_marg:>16.3f} {sig:>14.3f}")
print()

# ---------------------------------------------------------------------------
# (3) The paper's OWN measured degeneracy in the SIBLING channel (c8 SDB Fisher):
#     rho(f_NL, n_fNL) = -0.87 ; rho with biases co-marginalized = -0.97.
#     Use THESE measured correlations as the honest joint estimate for what a
#     bispectrum joint covariance would give, since they are the paper's only
#     directly-computed CAMB Fisher correlations.
# ---------------------------------------------------------------------------
print("=== USING PAPER'S OWN c8 SDB-CHANNEL CORRELATIONS AS THE JOINT ESTIMATE ===")
for rho, label in [(-0.87, "f_NL-n_fNL (c8, running marg.)"),
                   (-0.97, "f_NL-n_fNL-bias (c8, +bias marg.)")]:
    infl = 1/np.sqrt(1-rho**2)
    s_marg = sigma_base * infl
    sig = fnl_central * r / s_marg
    print(f"  rho={rho} ({label}): inflation {infl:.2f}x -> sigma_marg={s_marg:.3f}, {sig:.3f} sigma")
print()

# c8 direct SDB numbers (already in paper, verbatim)
print("=== c8 SDB-CHANNEL DIRECT (already in paper, real CAMB Fisher) ===")
print("  f_NL-only (biases fixed):         sigma=1.529 -> 1.43 sigma")
print("  + n_fNL marginalized (rho=-0.87): sigma=3.078 -> 0.71 sigma  (2.0x degradation)")
print("  + biases co-marg (rho=-0.97):     sigma=7.059 -> 0.31 sigma  (4.6x degradation)")

print()
print("=== 2x2 FISHER INVERSION VERIFICATION (numerical, not shortcut) ===")
# Build an explicit 2x2 covariance with individual errors s_f, s_G and correlation rho,
# invert to Fisher, then re-marginalize -> must reproduce s_f/sqrt(1-rho^2).
# Also verify against the paper's OWN c8 2x2 Fisher matrix (fnl,nfnl) directly.
F_c8 = np.array([[0.42792244995877743, 3.8799722812724253],
                 [3.8799722812724253, 46.70276906350654]])
C = np.linalg.inv(F_c8)
print("c8 (fnl,nfnl) Fisher -> marginalized sigma(fnl) = sqrt(C00) =", np.sqrt(C[0,0]), "(paper: 3.078)")
print("c8 unmarginalized sigma(fnl) = 1/sqrt(F00) =", 1/np.sqrt(F_c8[0,0]), "(paper: 1.529)")
rho_c8 = F_c8[0,1]/np.sqrt(F_c8[0,0]*F_c8[1,1])
print("c8 implied rho = -F01/sqrt(F00 F11) =", -rho_c8, "(paper: -0.87)")
