# Foundation D — FRW Survival Test

**Date:** 2026-03-14

---

## Purpose

Determine whether any candidate disformal mechanism remains nontrivial
on FRW cosmological backgrounds. This is the mandatory filter for
cosmological relevance.

---

## FRW Background Conditions

On flat FRW with standard matter (perfect fluids, scalars, fermions
without macroscopic spin or hypermomentum alignment):

```
Torsion:        T₀ = 0     (no macroscopic spin density)
Non-metricity:  Q₀ = 0     (no hypermomentum source)
Ricci scalar:   R = 6(Ḣ + 2H²) ≠ 0 in matter/DE eras
Weyl tensor:    C_μνρσ = 0  (FRW is conformally flat)
Pontryagin:     RR̃ = 0     (vanishes on conformally flat backgrounds)
```

---

## Candidate-by-Candidate FRW Test

### Candidate A: 0⁻ ALP-fermion coupling

**On FRW:** If B is a light rolling pseudoscalar, B = B₀(t), then
∂_μB = (Ḃ₀, 0, 0, 0).

The coupling (∂_μB)(ψ̄γ^μγ₅ψ) = Ḃ₀(ψ̄γ⁰γ₅ψ) is nonzero.

**FRW Verdict: SURVIVES** — but as standard ALP birefringence.
The effect is a CMB polarization rotation angle Δα ~ g_eff ΔB.
This is not disformal. It is generic ALP physics (Foundation B).

### Candidate B: 0⁺ vector-fermion coupling

**On FRW:** Removable by field redefinition regardless of background.

**FRW Verdict: N/A** — no physical effect.

### Candidate C: Non-metricity-fermion coupling

**On FRW:** Q₀ = 0. No non-metricity on FRW. Even if a non-standard
coupling existed, its source vanishes.

**FRW Verdict: FAILS** — Q₀ = 0.

### Candidate D: Heavy torsion → contact EFT

**On FRW:** The four-fermion interaction (ψ̄γ₅ψ)² exists on FRW.
But its magnitude is:

```
ρ_contact ~ (g_eff²/μ²) × (fermion density)² ~ (1/M_Pl²μ²) × n²
```

For thermal fermions at T_today ~ 10⁻⁴ eV:

```
n ~ T³ ~ 10⁻¹² eV³
ρ_contact ~ n² / (M_Pl² μ²) ~ 10⁻²⁴ / (10³⁶ × 10³⁶) ~ 10⁻⁹⁶ eV⁴
```

Compare to dark energy: ρ_Λ ~ 10⁻⁴⁷ eV⁴.

Ratio: ρ_contact/ρ_Λ ~ 10⁻⁴⁹. Utterly negligible.

**FRW Verdict: SURVIVES formally but is 10⁴⁹ orders of magnitude
below dark energy density. Cosmologically irrelevant.**

### Candidate E: R² → modified GW speed

**On FRW:** R̄ ≠ 0. The GW speed modification IS nonzero:

```
|c²_GW - 1| ~ |b_i| × H² / M_Pl² ~ 10⁻¹²⁰ |b_i|
```

**FRW Verdict: SURVIVES formally but is 10¹⁰⁵ orders below the
GW170817 constraint.** Cosmologically irrelevant for b_i ~ O(1).

### Candidate F: Chern-Simons / Pontryagin coupling

**On FRW:** The Pontryagin density RR̃ = 0 on conformally flat
backgrounds. The Chern-Simons effect only appears in perturbations
(GW propagation through the rolling pseudoscalar background).

The background evolution of θ IS affected (θ equation of motion
involves ∂V/∂θ), but the Chern-Simons term RR̃ doesn't contribute
to the background dynamics on FRW.

**FRW Verdict: PARTIAL** — background dynamics unaffected, but
perturbation-level effects (GW birefringence) exist. These are
standard Chern-Simons gravity predictions, not new.

---

## The Central Failure Pattern

### Why disformal effects vanish or are negligible on FRW

Three mechanisms conspire to kill disformal effects on cosmological
backgrounds:

**1. Homogeneity kills spatial gradients.**

On homogeneous FRW, ∂_iφ = 0 for any background field φ(t). A
disformal term B(φ)(∂_μφ)(∂_νφ) reduces to:

```
B(φ) φ̇² δ^0_μ δ^0_ν
```

This is a CONFORMAL modification of the g₀₀ component only. It
does NOT modify the spatial metric. In the ADM language, it changes
the lapse function but not the spatial metric or shift vector.

A purely time-dependent disformal modification is EQUIVALENT to
a conformal transformation plus a time reparametrization. It does
not produce genuinely disformal effects (those require spatial
gradients).

**2. T₀ = Q₀ = 0 on FRW.**

All geometric effects specific to torsion or non-metricity vanish
because these quantities are sourced by spin density and hyper-
momentum, which are zero for macroscopic homogeneous matter.

This is not a technicality — it reflects the SYMMETRY of FRW.
Torsion requires spin (breaking of parity or boost symmetry at the
microscopic level). Non-metricity requires hypermomentum (scale
or shear current). Homogeneous isotropic matter has neither.

**3. Gravitational suppression.**

Any disformal structure from a gravitational theory is suppressed
by at least M_Pl⁻² (from the gravitational coupling). For the
non-minimal curvature-fermion coupling (Toy IV), the suppression
is M_Pl⁻⁴. These suppressions make the effects unobservable by
enormous margins.

---

## Perturbation-Level Effects

Even if the background (homogeneous FRW) shows no disformal effects,
perturbations (inhomogeneities) might:

**Scalar perturbations:** δφ(t,x) has spatial gradients. The
disformal term B(φ)(∂_μδφ)(∂_νδφ) includes spatial components.
This modifies the sound speed of perturbations:

```
c²_s = 1 + B(φ)(∂φ)² / (kinetic normalization)
```

In Horndeski theory, this is the kinetic braiding effect. It is
cosmologically relevant and observationally constrained.

But: in PGT/MAG, the disformal coefficient B is M_Pl⁻⁴ suppressed
(from the non-minimal coupling analysis). So:

```
|c²_s - 1| ~ |B| × (∂δφ)² ~ M_Pl⁻⁴ × (H M_Pl)² ~ H²/M_Pl² ~ 10⁻¹²²
```

Unobservable.

**Tensor perturbations (GWs):** The R² correction to GW speed IS
a perturbation-level effect. As computed: |Δc²| ~ 10⁻¹²⁰. Unobservable.

**Vector perturbations:** Typically decay in FRW. Not cosmologically
relevant.

---

## Summary

| Candidate | FRW background | FRW perturbations | Cosmologically relevant? |
|-----------|---------------|-------------------|------------------------|
| A | ALP birefringence | Standard ALP | Generic ALP (Found. B) |
| B | No effect | No effect | No |
| C | Q₀ = 0 | Q ≠ 0 in perturbations | No (no source) |
| D | Contact ~ 10⁻⁴⁹ ρ_Λ | Contact + derivatives | No (Planck-suppressed) |
| E | Δc² ~ 10⁻¹²⁰ | Same | No (unobservable) |
| F | RR̃ = 0 | GW birefringence | Generic CS gravity |

**No candidate produces cosmologically relevant disformal effects.**

The strongest effects are:
- ALP birefringence (Candidate A) — but this is Foundation B
- GW birefringence (Candidate F) — but this is generic Chern-Simons

Both are standard frameworks, not new. The genuinely new geometric
effects (from torsion/non-metricity coupling) are all Planck-
suppressed to unobservability.
