"""
Compute σ(f_NL) as a function of b_φ prior width.

The scale-dependent bias signal is proportional to f_NL × b_φ.
Without external knowledge of b_φ, the constraint on f_NL degrades
as the b_φ prior widens.

This script computes and saves the sensitivity curve for Paper 2.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# The relationship: SDB measures the PRODUCT f_NL × b_φ
# ============================================================
# The observed power spectrum modification:
#   ΔP(k) ∝ f_NL × b_φ × (b₁-1) / k²
#
# A Fisher forecast constrains the combination f_NL × b_φ with
# some σ(f_NL × b_φ). To extract σ(f_NL) alone, you need a prior
# on b_φ.
#
# If b_φ is known perfectly: σ(f_NL) = σ(f_NL×b_φ) / b_φ
# If b_φ has uncertainty σ_bphi: the constraint degrades.
#
# For a Gaussian prior on b_φ with mean b_φ0 and width σ_bphi:
#   σ²(f_NL) ≈ σ²(f_NL|b_φ fixed) × [1 + (f_NL × σ_bphi / b_φ0)²/σ²(product)]
#
# More precisely, marginalizing over b_φ:
#   1/σ²(f_NL) = F_ff - F_fb² / (F_bb + 1/σ²_bphi)
# where F is the Fisher matrix in the (f_NL, b_φ) parameter space.

# Baseline values
f_NL_true = -4.375
b_phi_fid = 1.0  # Fiducial b_φ (universality relation: b_φ = 2δ_c(b₁-1))
b1 = 2.0  # Linear bias
delta_c = 1.686

# For the universality relation: b_φ = 2δ_c(b₁-1) = 2×1.686×1 = 3.37
b_phi_universal = 2 * delta_c * (b1 - 1)
print(f"Universality b_φ = 2δ_c(b₁-1) = {b_phi_universal:.2f}")

# Baseline σ(f_NL) from SPHEREx bispectrum (Heinrich et al.)
sigma_fnl_bispec = 0.7  # bispectrum channel (less sensitive to b_φ)

# Baseline σ(f_NL) from SDB with perfectly known b_φ
# From our Fisher: MegaMapper ideal gives σ ~ 0.5
sigma_fnl_sdb_ideal = 0.5

# The Fisher matrix for (f_NL, b_φ) from SDB:
# The SDB signal is Δb ∝ f_NL × b_φ / k²
# So F_ff ∝ b_φ², F_fb ∝ f_NL × b_φ, F_bb ∝ f_NL²
# At the fiducial f_NL = 0 (null hypothesis): F_fb = 0, F_bb = 0
# → b_φ is unconstrained from the data alone at f_NL = 0!
#
# At f_NL ≠ 0 (detection scenario):
# F_ff = (b_φ/σ_product)², F_fb = f_NL×b_φ/σ_product², F_bb = (f_NL/σ_product)²
# where σ_product is the constraint on the product f_NL×b_φ from the survey.

# For MegaMapper with ideal σ(f_NL) = 0.5 (assuming b_φ known):
# σ(f_NL×b_φ) = σ(f_NL) × b_φ_fid = 0.5 × 3.37 = 1.69
sigma_product = sigma_fnl_sdb_ideal * b_phi_universal

# Fisher matrix elements (at f_NL = -4.375):
F_ff = (b_phi_universal / sigma_product)**2  # = 1/σ²(f_NL|b_φ fixed)
F_fb = f_NL_true * b_phi_universal / sigma_product**2
F_bb = (f_NL_true / sigma_product)**2

print(f"\nFisher matrix (MegaMapper SDB):")
print(f"  F_ff = {F_ff:.4f}")
print(f"  F_fb = {F_fb:.4f}")
print(f"  F_bb = {F_bb:.4f}")

# Scan b_φ prior width
bphi_prior_widths = np.logspace(-2, 1, 100)  # σ(b_φ) from 0.01 to 10
# Also express as fractional: σ(b_φ)/b_φ
bphi_frac = bphi_prior_widths / b_phi_universal

sigma_fnl_marginalized = []
for sig_bp in bphi_prior_widths:
    # Marginalized σ(f_NL) = 1/sqrt(F_ff - F_fb²/(F_bb + 1/σ²_bp))
    F_bb_eff = F_bb + 1.0/sig_bp**2
    F_marg = F_ff - F_fb**2 / F_bb_eff
    if F_marg > 0:
        sigma_fnl_marginalized.append(1.0 / np.sqrt(F_marg))
    else:
        sigma_fnl_marginalized.append(np.inf)

sigma_fnl_marginalized = np.array(sigma_fnl_marginalized)

# Detection significance
significance = abs(f_NL_true) / sigma_fnl_marginalized

# Key points
print(f"\nMegaMapper SDB: σ(f_NL) vs b_φ prior width")
print(f"{'σ(b_φ)/b_φ':>12} {'σ(b_φ)':>8} {'σ(f_NL)':>10} {'Significance':>14}")
print("-" * 50)
for frac_target in [0.01, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0, 5.0]:
    idx = np.argmin(np.abs(bphi_frac - frac_target))
    sf = sigma_fnl_marginalized[idx]
    sig = significance[idx]
    print(f"{bphi_frac[idx]:>12.2%} {bphi_prior_widths[idx]:>8.3f} {sf:>10.3f} {sig:>12.1f}σ")

# Generate figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: σ(f_NL) vs b_φ prior width
ax1.loglog(bphi_frac * 100, sigma_fnl_marginalized, 'b-', linewidth=2, label='MegaMapper SDB')
ax1.axhline(y=sigma_fnl_bispec, color='r', linestyle='--', linewidth=1.5, label=f'SPHEREx bispectrum (σ = {sigma_fnl_bispec})')
ax1.axhline(y=sigma_fnl_sdb_ideal, color='b', linestyle=':', linewidth=1, alpha=0.5, label=f'MegaMapper ideal (σ = {sigma_fnl_sdb_ideal})')
ax1.axvline(x=20, color='gray', linestyle=':', alpha=0.5)
ax1.text(22, 0.55, '20% prior\n(paper assumption)', fontsize=9, color='gray')
ax1.set_xlabel(r'$b_\phi$ prior uncertainty [%]', fontsize=12)
ax1.set_ylabel(r'$\sigma(f_{\rm NL})$', fontsize=12)
ax1.set_title(r'$\sigma(f_{\rm NL})$ vs. $b_\phi$ prior width', fontsize=13)
ax1.set_xlim(1, 500)
ax1.set_ylim(0.3, 20)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Right: Detection significance
ax2.semilogx(bphi_frac * 100, significance, 'b-', linewidth=2, label='MegaMapper SDB')
bispec_sig = abs(f_NL_true) / sigma_fnl_bispec
ax2.axhline(y=bispec_sig, color='r', linestyle='--', linewidth=1.5, label=f'SPHEREx bispectrum ({bispec_sig:.1f}σ)')
ax2.axhline(y=3, color='orange', linestyle=':', linewidth=1, label='3σ threshold')
ax2.axhline(y=5, color='green', linestyle=':', linewidth=1, label='5σ threshold')
ax2.axvline(x=20, color='gray', linestyle=':', alpha=0.5)
ax2.set_xlabel(r'$b_\phi$ prior uncertainty [%]', fontsize=12)
ax2.set_ylabel(r'Detection significance ($\sigma$)', fontsize=12)
ax2.set_title(r'Detection of $f_{\rm NL} = -35/8$ vs. $b_\phi$ uncertainty', fontsize=13)
ax2.set_xlim(1, 500)
ax2.set_ylim(0, 12)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
fig.savefig('bphi_sensitivity.png', dpi=150, bbox_inches='tight')
fig.savefig('bphi_sensitivity.pdf', bbox_inches='tight')
print(f"\nFigure saved: bphi_sensitivity.png/pdf")

# Copy to public
import shutil
shutil.copy('bphi_sensitivity.png', '../../public/images/bphi_sensitivity.png')
print("Copied to public/images/")

print(f"\nKEY TAKEAWAY:")
print(f"  At 20% b_φ prior (paper assumption): σ(f_NL) ≈ {sigma_fnl_marginalized[np.argmin(np.abs(bphi_frac - 0.20))]:.2f}")
print(f"  At 50% b_φ prior (conservative):     σ(f_NL) ≈ {sigma_fnl_marginalized[np.argmin(np.abs(bphi_frac - 0.50))]:.2f}")
print(f"  At 100% b_φ prior (unconstrained):   σ(f_NL) ≈ {sigma_fnl_marginalized[np.argmin(np.abs(bphi_frac - 1.0))]:.2f}")
print(f"  SPHEREx bispectrum (b_φ independent): σ(f_NL) = {sigma_fnl_bispec}")
print(f"\n  The bispectrum channel is ROBUST to b_φ uncertainty.")
print(f"  The SDB channel degrades significantly beyond ~50% b_φ prior.")
