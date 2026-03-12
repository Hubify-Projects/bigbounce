# Model Limit Behavior Checks

**Date:** 2026-03-12
**Purpose:** Verify that the spin-torsion framework reduces to standard physics in appropriate limits.

---

## Limit 1: Torsion → 0

**Physical meaning:** No fermionic matter, or fermion spin density vanishes.

### Expected behavior:
When T^{abc} → 0, the Einstein-Cartan-Holst action should reduce to standard GR + a topological term.

### Verification:

**Step 1:** The torsion equation T^{abc} = 8πG · S^{abc} gives T → 0 when S^{abc} → 0 (no spin density). ✓

**Step 2:** The Holst term S_Holst = (M_Pl²/γ) ∫ e_I ∧ e_J ∧ R^{IJ}(ω) becomes topological when torsion vanishes, since in the torsion-free case ω = ω̊ (Levi-Civita) and the integrand becomes the Euler density (in 4D, proportional to the Gauss-Bonnet term). It does not affect the equations of motion. ✓

**Step 3:** The four-fermion interaction L_int ∝ G_N × J²_{(A)} vanishes since J_{(A)} → 0 when there are no fermions. ✓

**Step 4:** The parity-odd effective action S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ}[K, R̊] vanishes since F^{IJ}[K, R̊] depends on the contorsion K, which vanishes when torsion vanishes. Specifically, ω = ω̊ + K, and K = 0 when T = 0. ✓

**Step 5:** The effective cosmological constant reduces to:
```
Λ_eff = Ξ · M_Pl² + c_ω ω²  →  0 + c_ω ω²  →  0  (if also ω → 0)
```
or simply Λ_eff → Λ_bare (whatever bare cosmological constant exists). ✓

**Result: In the torsion → 0 limit, the theory reduces to standard GR with a bare cosmological constant.** The Holst term becomes topological, all torsion-dependent terms vanish, and the Friedmann equation reverts to the standard form. ✓ **PASS**

---

## Limit 2: Parity-odd amplitude → 0 (α/M → 0)

**Physical meaning:** The quantum correction generating parity violation is switched off.

### Expected behavior:
The framework should reduce to standard Einstein-Cartan theory with no parity violation, and no dynamical dark energy from the spin-torsion sector.

### Verification:

**Step 1:** The parity-odd effective action S_eff = (α/M) ∫ e_I ∧ e_J ∧ F^{IJ} → 0 directly. ✓

**Step 2:** The dimensionless suppression factor Ξ = [(α/M)·M_Pl] × D_inf → 0. ✓

**Step 3:** The vacuum energy contribution from the spin-torsion mechanism:
```
ρ_Λ = [(α/M)·M_Pl] × D_inf × M_Pl⁴ → 0
```
The mechanism produces no dark energy. ✓

**Step 4:** The four-fermion interaction L_int = -(3πG_N/2) × [γ²/(γ²+1)] × J²_{(A)} SURVIVES — this is present in standard Einstein-Cartan theory regardless of α/M. The BI parameter modifies the coupling strength but the contact interaction exists independently of the parity-odd one-loop term. ✓

**Step 5:** Cosmic birefringence angle β → 0 (no polarization rotation). ✓

**Step 6:** Galaxy spin asymmetry A₀ ∝ (α/M) → 0 (no preferred chirality). ✓

**Step 7:** The bounce mechanism (Eq. 12) is UNAFFECTED by α/M — it depends only on γ and G through ρ_crit. The quantum bounce survives. ✓

**Result: In the α/M → 0 limit, the theory reduces to standard Einstein-Cartan cosmology with a quantum bounce but no parity violation, no spin-torsion dark energy, no cosmic birefringence, and no galaxy spin asymmetry.** Standard ΛCDM behavior is recovered if a bare Λ is added by hand. ✓ **PASS**

---

## Limit 3: Inflationary suppression → 1 (D_inf → 1, i.e., N_tot → 0)

**Physical meaning:** No inflation occurred; the primordial parity-odd coefficient is unsuppressed.

### Expected behavior:
The vacuum energy should be at the Planck scale (catastrophically large), corresponding to the cosmological constant problem in its original form.

### Verification:

**Step 1:** D_inf = exp(-3 × 0) × (T_reh/M_GUT)^{3/2} = (T_reh/M_GUT)^{3/2}.
For T_reh ~ M_GUT, D_inf → 1. ✓

**Step 2:** The vacuum energy becomes:
```
ρ_Λ = [(α/M)·M_Pl] × 1 × M_Pl⁴ ~ 10⁻² × M_Pl⁴ ~ 10⁻² × (1.22×10¹⁹)⁴ GeV⁴
     ~ 10⁷⁴ GeV⁴
```
This is ~10¹²¹ times larger than the observed value. ✓

**Step 3:** This reproduces the standard cosmological constant problem — without inflationary dilution, any Planck-scale vacuum energy contribution overwhelms observations by ~120 orders of magnitude. ✓

**Step 4:** The framework correctly identifies inflation as the mechanism that bridges the 120 orders of magnitude. Without it, the mechanism fails to produce a viable cosmology. ✓

**Result: In the D_inf → 1 limit, the predicted vacuum energy is ~10⁷⁴ GeV⁴ ≈ 10⁻² M_Pl⁴, which is catastrophically large — exactly as expected.** The cosmological constant problem is reproduced in its standard form. Inflation is essential to the mechanism. ✓ **PASS**

---

## Limit 4: γ → 0 (Barbero-Immirzi parameter vanishes)

**Physical meaning:** The Holst modification is removed.

### Verification:

**Step 1:** The BI suppression factor γ²/(γ²+1) → 0. The four-fermion interaction coupling vanishes. ✓

**Step 2:** However, the Holst term S_Holst = (M_Pl²/γ) ∫ e ∧ e ∧ R → ∞ (diverges).

**This limit is singular** — γ = 0 is not a physical limit of the theory. The Holst term coefficient diverges, which is the expected behavior: γ parameterizes the canonical structure of LQG, and γ = 0 corresponds to a degenerate quantization. ✓

**Result: γ → 0 is a singular limit, as expected. The theory requires γ > 0 for consistency.** ✓ **PASS** (singular limit correctly excluded)

---

## Limit 5: γ → ∞ (Barbero-Immirzi parameter large)

**Physical meaning:** The Holst term contribution vanishes; theory approaches standard ECSK.

### Verification:

**Step 1:** The Holst term S_Holst = (M_Pl²/γ) ∫ e ∧ e ∧ R → 0. The parity-odd modification disappears. ✓

**Step 2:** The BI suppression factor γ²/(γ²+1) → 1. The four-fermion interaction recovers the standard ECSK form L_int = -(3πG_N/2) × J²_{(A)}. ✓

**Step 3:** The area-gap mass M = √γ · M_Pl → ∞. The parity-odd coefficient α/M → 0 (since M → ∞). ✓

**Step 4:** The bounce critical density ρ_crit = (√3/32π²γ³) ρ_Pl → 0. The bounce occurs at arbitrarily low density — this is the classical singularity limit (bounce disappears). ✓

**Result: In the γ → ∞ limit, the theory reduces to standard Einstein-Cartan-Sciama-Kibble theory: the Holst term vanishes, parity violation disappears, and the quantum bounce occurs at infinitesimally low density (effectively no bounce).** ✓ **PASS**

---

## Summary

| Limit | Expected behavior | Actual behavior | Status |
|-------|-------------------|-----------------|--------|
| T^{abc} → 0 | Standard GR | Standard GR (Holst topological) | **PASS** |
| α/M → 0 | EC theory, no parity violation | EC theory, bounce survives, no DE | **PASS** |
| D_inf → 1 | ρ_Λ ~ M_Pl⁴ (CC problem) | ρ_Λ ~ 10⁻² M_Pl⁴ (10¹²¹ × observed) | **PASS** |
| γ → 0 | Singular (degenerate) | Divergent Holst term (correctly excluded) | **PASS** |
| γ → ∞ | Standard ECSK, no bounce | ECSK recovered, ρ_crit → 0 | **PASS** |

**All 5 limit checks pass.** The model has correct limiting behavior in every physically meaningful regime, and correctly reduces to ΛCDM/GR when the spin-torsion modifications are removed.
