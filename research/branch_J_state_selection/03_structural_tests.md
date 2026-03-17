# Structural Test Framework for Branch J

**Date:** 2026-03-16

---

## Test J1 — Event Strength

**Question:** Is the bounce interaction strong enough to alter
the dark-sector state nontrivially?

### Criterion

The bounce-induced change in the dark-sector state must exceed
the dark sector's own dynamical timescale. Specifically:

```
|ΔV_bounce| > V_barrier    (for discrete selection)
|Δθ_bounce| > θ_resolution  (for angular selection)
|Δφ_bounce| > Δφ_quantum    (for continuous displacement)
```

### How to evaluate

Compute the effective force on the dark-sector field during the
bounce and integrate over the bounce duration:

```
Δφ ~ ∫ F(t) dt² ~ F_peak × t_bounce²
F_peak ~ ξ R_b φ ~ ξ × 21 M_Pl² × φ
t_bounce ~ 1/M_Pl
```

For ξ ~ O(1) and φ ~ v (initial field value):
```
Δφ ~ 21ξ v    (in natural units)
```

For v ~ M_Pl: Δφ ~ M_Pl (O(1) displacement). **PASSES.**
For v ~ meV: Δφ ~ 21ξ meV (tiny displacement, but still large
compared to the DE potential scale). **PASSES.**

### Verdict criterion

**PASS** if Δφ/v > 0.1 (nontrivial displacement relative to
field range).
**FAIL_TOO_WEAK** if Δφ/v < 0.01 (negligible perturbation).

### Assessment for all candidates

| Candidate | Δφ/v | Verdict |
|-----------|------|---------|
| A: pNGB | ~ξ (O(1)) | PASS |
| B: Multi-vacuum | ~ξ v/barrier_width (≫1) | PASS |
| C: Symmetry | ~ξ M_Pl²/μ² (≫1) | PASS |
| D: Metastable | ~ξ M_Pl²/V_barrier (≫1) | PASS |
| E: Nonadiabatic | ω̇/ω² ~ 1 | PASS |

**All candidates pass J1.** The curvature coupling at the bounce
is ALWAYS strong enough to affect DE-scale fields. This is the
EASY test.

---

## Test J2 — Generic-Initial-Condition Collapse

**Question:** Does the result reduce to "the field ends up at
some φ_i" with no predictive content?

### Criterion

The mapping from pre-bounce states to post-bounce states must
be CONTRACTING (many-to-few), not merely ROTATING (one-to-one).

Formally: define the map T: (φ_pre, φ̇_pre) → (φ_post, φ̇_post).

- **Contracting:** The image of T has smaller phase-space volume
  than the domain. Many initial conditions map to the same (or
  similar) final state. PASSES J2.

- **Rotating/shearing:** T is volume-preserving (Hamiltonian
  evolution). The image has the same volume as the domain. Each
  initial condition maps to a unique final state. FAILS J2.

- **Expanding:** Chaotic sensitivity. Small changes in initial
  conditions lead to large changes in final state. FAILS J2.

### The Liouville obstacle

**For Hamiltonian systems, phase-space volume is CONSERVED
(Liouville's theorem).** The scalar field equation:

```
φ̈ + 3Hφ̇ + V'(φ) + ξRφ = 0
```

is Hamiltonian in the absence of Hubble friction (H = 0 at the
bounce). Near the bounce, the evolution is approximately
Hamiltonian → volume-preserving → the map T is a ROTATION.

**Liouville's theorem directly prevents bounce state selection
from being a contracting map.**

The ONLY escape from Liouville:
1. Hubble friction (3Hφ̇ term) — but H ≈ 0 at the bounce
2. Particle production (energy transfer to other modes) —
   irreversible, could contract the zero-mode phase space
3. Quantum decoherence — requires environment coupling

### Hubble friction assessment

During the bounce, H transitions from negative (contraction)
to positive (expansion). The NET friction over the bounce:

```
∫ 3H(t) dt    from -∞ to +∞
```

For the symmetric bounce: H(t) = 2α²t/(1+4α²t²).
∫ H dt = [ln(1+4α²t²)]/4 evaluated -∞ to +∞ = ∞.

BUT: this integral diverges because H ~ 1/t at late times,
giving cumulative friction that eventually damps the field.
The BOUNCE-SPECIFIC friction (near t = 0) is:

```
∫_{-t_b}^{t_b} 3H(t) dt ≈ 0   (antisymmetric: H(-t) = -H(t))
```

The friction during approach (H < 0, anti-friction) is exactly
canceled by the friction during exit (H > 0, friction). The
NET bounce-specific friction is ZERO at leading order.

At next order: the field changes position during the bounce,
so the friction experienced during exit is slightly different
from the anti-friction during approach. This gives a residual
net friction of order:

```
δ(friction) ~ 3 × (Δφ/φ) × ∫|H| dt ~ 3 × ξ × O(1)
```

This IS a small contraction of phase space — but by O(1), not
by a large factor. The narrowing is at most a factor of a few.

### Assessment for all candidates

| Candidate | Map type | J2 verdict |
|-----------|----------|-----------|
| A: pNGB | Rotation (Liouville) + O(1) friction | **MARGINAL** |
| B: Multi-vacuum | Rotation → reset to φ≈0 → V determines rest | **FAIL** |
| C: Symmetry | Rotation → back to original vacuum | **FAIL** |
| D: Metastable | Same as B | **FAIL** |
| E: Nonadiabatic | Particle production is irreversible | **PASS** (weakly) |

**Most candidates FAIL J2.** The bounce is too nearly
time-symmetric (Hamiltonian) to contract phase space.
Candidate E (particle production) is the only one with a
genuinely irreversible process.

---

## Test J3 — Naturalness/Protection

**Question:** Is the late-time dark sector technically natural
after the bounce coupling is included?

### Criterion

The coupling that enables bounce state selection must not
generate radiative corrections that destabilize the DE potential.

For the curvature coupling ξRφ²:

- Radiative correction to φ mass: δm² ~ ξΛ_UV² (where Λ_UV
  is the UV cutoff). For Λ_UV ~ M_Pl: δm² ~ ξ M_Pl².
  This is ENORMOUS compared to m_DE² ~ H₀².

**The naturalness problem:** ξRφ² coupling with ξ ~ O(1)
generates a Planck-scale mass correction, destroying the
DE potential.

**The standard escape:** If φ is a pNGB (axion), its mass is
protected by a shift symmetry. The curvature coupling ξRφ²
BREAKS the shift symmetry and re-introduces the hierarchy
problem.

**Resolution options:**
1. ξ is technically natural if generated only by gravitational
   loops: ξ_grav ~ m²/(16π² M_Pl²) ~ 10⁻¹²⁴. Far too small
   for bounce state selection.

2. ξ = 1/6 (conformal coupling) is a fixed point of the RG.
   Conformal coupling is radiatively stable but does NOT
   protect the mass (the mass still runs).

3. The coupling is to the Gauss-Bonnet invariant G = R² - 4RμνRμν
   + RμνρσRμνρσ, which is topological in 4D. The coupling φG
   doesn't contribute to the mass at one loop. But G = 0 at the
   bounce on FRW? No: G = 24H²(Ḣ + H²). At H = 0: G = 0.
   The Gauss-Bonnet coupling vanishes at the bounce. Useless.

### Assessment

| Candidate | Coupling | Naturalness | J3 verdict |
|-----------|----------|------------|-----------|
| A: pNGB | ξRφ² | Breaks shift symmetry | **FAIL** (for ξ ~ 1) |
| A': pNGB | ξ ~ 10⁻¹²⁴ | Natural but too weak | **FAIL** (too weak) |
| B–D | ξRφ² | Same as A | **FAIL** |
| E | ξRχ² + m² | Same problem | **FAIL** |

**ALL candidates face the naturalness dilemma:**

```
ξ ~ O(1)  →  strong enough for state selection
             BUT breaks mass protection

ξ ~ 10⁻¹²⁴ → mass is protected
              BUT too weak for state selection
```

This is a SPECIFIC version of the general tension identified
in the problem statement. No candidate resolves it.

### The one escape: non-perturbative coupling

If the bounce couples to the dark sector through a
NON-PERTURBATIVE mechanism (instanton, topology change), the
coupling could be exponentially sensitive to bounce parameters
without generating perturbative mass corrections. But no such
mechanism exists in the minimal EC model.

---

## Test J4 — Predictive Narrowing

**Question:** Does the bounce determine or significantly narrow
a late-time observable?

### Criterion

The mapping θ_pre → θ_post must have a small image relative
to the domain:

```
|range(θ_post)| / |range(θ_pre)| < 0.3    (significant narrowing)
|range(θ_post)| / |range(θ_pre)| < 0.01   (strong narrowing)
```

### Assessment

From J2, the mapping is approximately a rotation (Liouville).
The narrowing ratio is ~ 1 - O(net friction / kinetic energy).
For the bounce: the net friction is ~O(1) in Planck units, and
the kinetic energy is also ~O(1) (for ξ ~ 1). So the narrowing
ratio is ~ 1 - O(1) ~ O(1).

**The narrowing is at most a factor of a few.**

This means: if the pre-bounce state is uniformly distributed
in [0, 2π], the post-bounce state is uniformly distributed
in (roughly) [0, 2π] with O(1) modulation. Not useful.

**The only scenario with strong narrowing:** if the pre-bounce
contraction phase ALREADY narrows the state through Hubble
anti-friction (exponential amplification of φ̇ during
contraction). But this depends on the pre-contraction state,
pushing the initial-conditions problem further back.

| Candidate | Narrowing ratio | J4 verdict |
|-----------|----------------|-----------|
| A: pNGB | ~O(1) | **FAIL** |
| B: Multi-vacuum | Discrete (N → 1 vacuum) | **MARGINAL** |
| C: Symmetry | ~1 (returns to original) | **FAIL** |
| D: Metastable | Same as B | **MARGINAL** |
| E: Nonadiabatic | Continuous, O(1) | **FAIL** |

B and D provide discrete narrowing (the field ends up in the
vacuum nearest φ = 0), but this is determined by the POTENTIAL,
not the bounce. The "prediction" is: "the field is in whatever
vacuum is closest to the symmetric point." This is a statement
about V(φ), not about bounce physics.

---

## Test J5 — Late-Time Viability

**Question:** Does the resulting state produce acceptable DE?

### Criterion

The post-bounce state must yield:
- ρ_DE ~ 10⁻¹²² M_Pl⁴ (correct energy scale)
- w ≈ -1 (equation of state)
- No ghost or gradient instability

### Assessment

This test is TRIVIALLY PASSED by all candidates that simply
embed a standard DE model (quintessence, axion DE, etc.) on
the bounce background. The DE model was already designed to
produce acceptable late-time behavior. The bounce modifies the
initial conditions by O(1) but doesn't change the qualitative
late-time behavior.

The exception: Candidate E (nonadiabatic excitation). The
produced particles have w ≈ 0 (matter-like), not w ≈ -1.
For the condensate to act as DE, the field must not yet have
started oscillating: m < H₀ (ultra-light). The equation of
state for an ultra-light non-oscillating field is w ≈ -1 if
the field is in the slow-roll regime. But particle production
creates excitations that are NOT in slow-roll — they are
high-momentum modes that behave as matter or radiation.

**Only the zero-mode (homogeneous) condensate can act as DE.**
Particle production creates INHOMOGENEOUS excitations that
act as matter/radiation, diluting away. The zero-mode is NOT
enhanced by particle production — it is determined by the
initial displacement.

| Candidate | w | ρ_DE | J5 verdict |
|-----------|---|------|-----------|
| A: pNGB | ≈ -1 (if m < H₀) | Depends on θ_post | **PASS** |
| B: Multi-vacuum | ≈ -1 (CC-like) | V(φ_n) | **PASS** |
| C: Symmetry | ≈ -1 | V(±v) | **PASS** |
| D: Metastable | ≈ -1 | V(φ_meta) | **PASS** |
| E: Nonadiabatic | ≈ 0 (matter) | Wrong | **FAIL** |

---

## Combined Scorecard

| Test | A: pNGB | B: Multi-vac | C: Symmetry | D: Metastable | E: Nonadiab. |
|------|---------|------------|------------|--------------|-------------|
| J1: Strength | PASS | PASS | PASS | PASS | PASS |
| J2: Not arbitrary IC | MARGINAL | FAIL | FAIL | FAIL | PASS (weak) |
| J3: Naturalness | FAIL | FAIL | FAIL | FAIL | FAIL |
| J4: Narrowing | FAIL | MARGINAL | FAIL | MARGINAL | FAIL |
| J5: Late-time viable | PASS | PASS | PASS | PASS | FAIL |

**No candidate passes all five tests.**

**The universal failure is J3 (naturalness):** any curvature
coupling strong enough to affect the state (ξ ~ O(1)) breaks
the mass protection of the DE field. This is the state-selection
analog of the scale-separation barrier.

---

## Verdict Labels

Based on test results:

- **FAIL_TOO_WEAK:** Fails J1. (No candidate fails here.)
- **FAIL_ARBITRARY_INITIAL_CONDITIONS:** Fails J2. (B, C, D.)
- **FAIL_NO_PROTECTION:** Fails J3. (ALL candidates.)
- **FAIL_NO_NARROWING:** Fails J4. (A, C, E.)
- **FAIL_SPECTATOR_COLLAPSE:** Passes all J tests but result
  is indistinguishable from spectator evolution. (None reach this.)
- **SURVIVES_PHASE1:** Passes J1–J5. (**No candidate achieves this.**)
