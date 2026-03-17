# Observability and Distinctiveness Assessment

**Date:** 2026-03-15

---

## The Result

The minimal Einstein-Cartan bounce model produces:

```
Chirality:  Δχ(k) = (P_L - P_R)/(P_L + P_R) = 0    (exact)
```

There is NO parity-violating tensor signal. This section assesses
whether any remnant or indirect parity signature could be
observable, and whether this null result is itself distinctive.

---

## Assessment of Potential Observables

### Observable 1: TB and EB Correlations in the CMB

**What it measures:** Cross-correlations between temperature (T)
or E-mode polarization and B-mode polarization. TB and EB are
zero in a parity-symmetric theory.

**Bounce prediction:** TB = EB = 0 (no parity violation in
tensor sector).

**Current data:** Planck measures α_EB = 0.30° ± 0.11° (2.4σ
hint of cosmic birefringence). This is consistent with a small
parity-violating effect.

**Assessment:** The bounce does NOT predict the observed hint.
If the birefringence is real, it must come from a DIFFERENT
source (e.g., axion-photon coupling during propagation), not
from the bounce tensor sector.

**Distinctive?** No — the bounce prediction (TB = EB = 0) is
the same as standard GR.

### Observable 2: Chiral Gravitational Wave Background

**What it measures:** Asymmetry between left and right circular
polarization in the stochastic GW background.

**Bounce prediction:** No asymmetry. Δχ = 0 at all frequencies.

**Current data:** No measurement of GW chirality exists (would
require multiple non-coplanar detectors).

**Assessment:** The bounce predicts nothing here.

**Distinctive?** No — same as standard GR.

### Observable 3: Frequency-Dependent Chirality

**What it measures:** A chirality that varies with frequency,
potentially detectable as a spectral shape difference between
L and R at different GW detector bands.

**Bounce prediction:** No frequency-dependent chirality. Δχ = 0
at all k.

**Assessment:** Even if chirality existed, the absolute GW
amplitude from the bounce is ~10⁻⁶⁴ — undetectable. A
frequency-dependent ratio would be 0/0.

**Distinctive?** Not applicable.

### Observable 4: Gravitational Leptogenesis

**What it measures:** Baryon asymmetry generated through
gravitational parity violation producing a chiral fermion
asymmetry.

**Mechanism:** The gravitational chiral anomaly ∂_μ J^{5μ} ∝ R̃R
could generate a lepton asymmetry during the bounce (where R̃R
is large).

**Bounce assessment:** R̃R at the bounce on FRW:

For FRW: R_μνρσ has only time-time and time-space components
(in the standard decomposition). The Pontryagin density:

```
R̃^{μν}_{ρσ} R^{ρσ}_{μν} = ε^{μνκλ} R_{μνab} R_{κλ}^{ab}
```

On FRW: the ε tensor contracts spatial and temporal indices.
For a purely isotropic metric, the Weyl tensor vanishes, and
the Riemann tensor is determined by the Ricci tensor. The
Pontryagin density on FRW is:

```
R̃R = 0    on exact FRW
```

This vanishes because FRW has no Weyl curvature, and the
Pontryagin density of the Ricci part is zero by symmetry.

**VERDICT:** R̃R = 0 on FRW → no gravitational leptogenesis
from the bounce on an exact FRW background.

(Note: perturbative corrections from tensor and scalar
perturbations can give R̃R ≠ 0 at second order, but this is
suppressed by P_T ~ 10⁻⁶⁴ and is negligible.)

**Distinctive?** No — FRW kills the Pontryagin density
regardless of the bounce model.

### Observable 5: Parity Violation in Scalar Sector

**What it would measure:** Asymmetry in scalar perturbations
under parity.

**Assessment:** Scalar perturbations do not carry a chirality
label (they are spin-0). Parity violation in the scalar sector
would appear as a correlation between scalars and pseudoscalars,
but on FRW there is no pseudoscalar background to correlate with
(n_5 = 0 in thermal equilibrium).

**Distinctive?** Not applicable.

---

## Is the NULL Result Itself Distinctive?

The null result (Δχ = 0) is GENERIC: it is predicted by standard
GR, by any parity-symmetric gravity theory, and by any bounce
model without explicit parity violation.

However, one could ask: is the COMBINATION of {Δχ = 0} + {n_T ≈ 0}
+ {specific amplitude} distinctive?

| Prediction | Spin-torsion bounce | Standard inflation | Matter bounce |
|-----------|-------------------|-------------------|--------------|
| n_T | ≈ 0 | -r/8 < 0 | ≈ 0 |
| Δχ | 0 | 0 | 0 |
| P_T amplitude | ~10⁻⁶⁴ | ~10⁻¹⁰ × r | Model-dep. |

The spin-torsion bounce is distinguished from inflation by n_T
(0 vs negative) and amplitude (tiny vs potentially observable).
But it is NOT distinguished from other radiation bounces or
matter bounces in the chirality sector.

**The null chirality result does NOT add any distinctive
information beyond what was already known from the tensor
amplitude calculation.**

---

## The Ratio Argument Revisited

The initial hope was that a chirality RATIO Δχ = (P_L - P_R)/
(P_L + P_R) could evade the absolute amplitude suppression.

This hope fails for a structural reason: the chirality ratio
is zero, not because numerator and denominator are both small
and cancel, but because the NUMERATOR IS IDENTICALLY ZERO.

There is no parity-odd physics in the minimal model. The ratio
Δχ = 0/P_total = 0 regardless of what P_total is.

**The dilution argument is irrelevant because the chirality is
zero before dilution, not after.**

---

## What Would Change the Story

For a nonzero chirality signal, one would need to ADD to the
minimal model:

| Addition | Effect | Already tested? |
|----------|--------|----------------|
| Dynamical Chern-Simons | Δχ ~ O(α_CS φ'/M_Pl²) | Not in EC; separate theory |
| Dynamical Immirzi field | Δχ ~ O(β'/β) | Foundation B: generic ALP |
| Explicit Lorentz violation | Δχ ~ O(b_0/k) | Not motivated by EC |
| Gravitational anomaly | Δχ ~ O(R²/(192π² M_Pl⁴)) | Zero on FRW |

None of these are part of the minimal spin-torsion bounce.

---

## Summary

| Observable | Bounce prediction | Distinctive? | Observable? |
|-----------|------------------|-------------|------------|
| TB/EB in CMB | 0 | NO (same as GR) | N/A |
| Chiral GW background | 0 | NO (same as GR) | N/A |
| Frequency-dep. chirality | 0 | NO | N/A |
| Gravitational leptogenesis | 0 (R̃R = 0 on FRW) | NO | N/A |
| Scalar parity violation | 0 | NO | N/A |

**Every parity-related observable is zero in the minimal model.
None provide distinctive or observable signatures.**
