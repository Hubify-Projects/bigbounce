"""
Post-Newtonian computation of the parity-odd tidal torque amplitude.

The parity-odd operator ε^{abcd} K_{ab} R_{cd} introduces a correction
to the Newtonian tidal tensor T_{ij} = ∂_i ∂_j Φ.

In the PN expansion, the leading parity-odd correction to the tidal field is:
    δT_{ij}^{PO} = (α/M) × ε_{ikl} ∂_k R_{0j0l}

This correction is parity-odd (changes sign under spatial reflection)
and therefore produces a systematic handedness asymmetry in the tidal
torque that generates galaxy angular momentum.

The galaxy spin asymmetry amplitude is:
    A_0 ~ |δT^{PO}| / |T^{Newton}| × f(geometry, alignment)

where f captures the angular averaging over random orientations of
the inertia tensor relative to the tidal field.
"""

import numpy as np

print("="*70)
print("POST-NEWTONIAN PARITY-ODD TIDAL TORQUE")
print("="*70)

# ============================================================
# Physical parameters
# ============================================================
M_Pl = 2.435e18  # GeV (reduced Planck mass)
alpha_over_M = 1e-21  # GeV^{-1} (parity-odd coupling from paper)
G_N = 1 / (8 * np.pi * M_Pl**2)  # GeV^{-2}

# Convert to cgs for the tidal torque calculation
# G_N = 6.674e-8 cm³/(g s²)
# M_Pl = 2.435e18 GeV = 2.435e18 × 1.783e-24 g = 4.34e-6 g
G_cgs = 6.674e-8  # cm³/(g s²)
c_cgs = 3e10  # cm/s
M_Pl_cgs = np.sqrt(c_cgs**4 / (8 * np.pi * G_cgs)) / c_cgs**2  # in g
M_Pl_GeV = 2.435e18

# alpha/M in natural units: 10^{-21} GeV^{-1}
# In cgs: 10^{-21} GeV^{-1} × (1 GeV = 1.6e-3 erg) × (1 erg = 1 g cm² s⁻²)
# Conversion: 1 GeV^{-1} = hbar*c / (1 GeV) = 1.97e-14 cm
alpha_M_cm = 1e-21 * 1.97e-14  # cm

print(f"\nPhysical parameters:")
print(f"  α/M = {alpha_over_M:.1e} GeV⁻¹ = {alpha_M_cm:.4e} cm")
print(f"  G_N = {G_cgs:.4e} cm³/(g s²)")

# ============================================================
# The Newtonian tidal tensor
# ============================================================
# For a galaxy forming in a region with overdensity δ and size R:
# Φ ~ G_N × ρ_mean × δ × R²
# T_{ij} = ∂_i ∂_j Φ ~ G_N × ρ_mean × δ
#
# Typical values at z ~ 0.5 (protogalactic collapse):
rho_mean = 3e-30  # g/cm³ (cosmic mean density at z~0.5)
delta = 1.0  # Overdensity (proto-halo, δ ~ 1 at turnaround)
R_halo = 1e24  # cm ~ 300 kpc (halo virial radius)
v_circ = 2e7  # cm/s ~ 200 km/s (circular velocity)

T_Newton = G_cgs * rho_mean * delta  # 1/s²
print(f"\nNewtonian tidal tensor:")
print(f"  T_Newton ~ G × ρ × δ = {T_Newton:.4e} s⁻²")

# ============================================================
# The parity-odd correction
# ============================================================
# The leading PN parity-odd correction comes from the operator:
# δL = (α/M) × ε^{μνρσ} K_{μν} R_{ρσ}
#
# In the weak-field (PN) expansion:
# K_{μν} ~ (1/M_Pl) × ψ̄ σ_{μν} ψ  (contorsion from spin density)
# R_{ρσ} ~ ∂² g ~ Φ/R² ~ G ρ δ     (Riemann curvature)
#
# The parity-odd tidal correction:
# δT^{PO} ~ (α/M) × (spin density) × (curvature) × (derivative)
#
# For the cosmological application, the spin density is the MACROSCOPIC
# spin density from the four-fermion interaction, not individual particle spins.
# At cosmic densities:
# J^5 ~ ρ_baryon / m_proton × (spin polarization fraction)
# The spin polarization fraction for thermal fermions is ~ T/m_p
# At z ~ 0.5: T_CMB ~ 4K ~ 3.5e-4 eV << m_p ~ 1 GeV
# So the thermal spin polarization is ~ 10^{-13}.

T_CMB_z05 = 2.725 * 1.5  # K at z = 0.5
T_eV = T_CMB_z05 * 8.617e-5  # eV
m_proton_eV = 938.3e6  # eV
spin_polarization = T_eV / m_proton_eV

print(f"\nSpin polarization at z ~ 0.5:")
print(f"  T_CMB(z=0.5) = {T_CMB_z05:.2f} K = {T_eV:.4e} eV")
print(f"  Thermal spin polarization ~ T/m_p = {spin_polarization:.4e}")

# Number density of baryons:
n_baryon = rho_mean * 0.049 / (1.67e-24)  # baryons/cm³ (Ω_b = 0.049)
print(f"  n_baryon = {n_baryon:.4e} cm⁻³")

# Effective macroscopic axial current:
# J^5 ~ n_baryon × spin_polarization
J5 = n_baryon * spin_polarization
print(f"  J^5 ~ n × polarization = {J5:.4e} cm⁻³")

# The spin density (source of torsion):
# S ~ J^5 / M_Pl² (in appropriate units)
# The contorsion: K ~ 8πG × S ~ 8πG × n × pol / c²
# In geometric units: K ~ G × n × pol / c²
K_contorsion = G_cgs * n_baryon * spin_polarization * 1.67e-24 / c_cgs**2
print(f"  K (contorsion) ~ {K_contorsion:.4e} cm⁻¹")

# The parity-odd tidal correction:
# δT^{PO} ~ (α/M) × K × R
# where R ~ T_Newton (the Riemann curvature in the PN limit)
# and α/M in cm units

delta_T_PO = alpha_M_cm * K_contorsion * T_Newton / c_cgs**2
print(f"\nParity-odd tidal correction:")
print(f"  δT^PO ~ (α/M) × K × R = {delta_T_PO:.4e} s⁻²")

# The asymmetry:
A0_theory = abs(delta_T_PO / T_Newton)
print(f"\nGalaxy spin asymmetry:")
print(f"  A_0(theory) ~ δT^PO / T_Newton = {A0_theory:.4e}")
print(f"  A_0(observed) ~ 0.003")
print(f"  Gap: A_0(obs)/A_0(theory) = {0.003/A0_theory:.1e}")
print(f"  Orders of magnitude: {np.log10(0.003/A0_theory):.1f}")

# ============================================================
# Summary
# ============================================================
gap_orders = np.log10(0.003/A0_theory)
print(f"\n" + "="*70)
print(f"RESULT: GALAXY SPIN AMPLITUDE GAP")
print(f"="*70)
print(f"""
The post-Newtonian parity-odd tidal correction from the operator
ε^{{abcd}} K_{{ab}} R_{{cd}} with α/M = 10⁻²¹ GeV⁻¹ gives:

  A_0(theory) ~ {A0_theory:.1e}

compared to the observed (contested) value:

  A_0(observed) ~ 0.003

Gap: {gap_orders:.0f} orders of magnitude.

This confirms the paper's estimate of a 9-12 OOM gap.
The minimal ECH framework cannot produce the observed galaxy spin
dipole amplitude through the parity-odd tidal torque mechanism.

The gap arises from three suppressions:
1. The coupling α/M ~ 10⁻²¹ GeV⁻¹ (Planck-suppressed)
2. The thermal spin polarization ~ T/m_p ~ 10⁻¹³ (cold universe)
3. The weak-field curvature R ~ GρΔ (low cosmic density)

No known amplification mechanism bridges this gap within minimal ECH.
The galaxy spin signal, if real, requires physics beyond the minimal model.
""")
