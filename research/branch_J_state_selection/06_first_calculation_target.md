# First-Calculation Target Assessment

**Date:** 2026-03-16

---

## Status After Screening

Zero candidates survived the OOM screening. All five mechanism
classes are killed by the Liouville + naturalness combination.

Under normal circumstances, this section would identify the best
Phase 2 target. Given the screening results, this section instead
assesses whether ANY calculation could change the conclusion.

---

## Could a Detailed Calculation Save Any Candidate?

### Candidate A (pNGB): Full ODE through contraction + bounce

**Calculation:** Solve θ̈ + 3H(t)θ̇ + ξR(t)θ = 0 for the full
contraction → bounce → expansion trajectory, for a grid of
(θ_pre, θ̇_pre) initial conditions.

**What it would show:** The map (θ_pre, θ̇_pre) → (θ_post, θ̇_post)
explicitly. Could quantify the narrowing ratio.

**Why it probably won't help:**

The equation is LINEAR in θ (for small θ or for the quadratic
approximation). A linear equation maps the 2D input space to the
2D output space via a 2×2 matrix. The matrix has determinant 1
(Liouville). The narrowing ratio is exactly 1.

For NONLINEAR evolution (large θ, periodic potential): the map is
nonlinear but still Hamiltonian (area-preserving). Phase space is
distorted but not contracted. Narrow regions get stretched while
wide regions get compressed, but total area is conserved.

**The only hope:** If the contraction phase (H < 0, long duration)
provides significant net ANTI-friction that amplifies θ̇, followed
by the expansion phase friction that damps it. The asymmetry
between contraction and expansion could give a net effect.

But: for m ~ H₀, the field is frozen during both contraction and
expansion (m ≪ |H|). The friction/anti-friction terms act on
a zero velocity — they do nothing. The field is INERT throughout.

**Estimated probability of success: < 5%.**

### Candidate B (multi-vacuum): Nonlinear basin analysis

**Calculation:** Solve the nonlinear equation φ̈ + 3Hφ̇ + V'(φ)
+ ξR(t)φ = 0 for a multi-well potential, mapping pre-bounce
basins to post-bounce basins.

**What it would show:** Which pre-bounce vacua map to which
post-bounce vacua. A "basin diagram" of the bounce map.

**Why it probably won't help:**

We already know the answer: during the bounce, ξR dominates V,
so all fields are driven to φ ≈ 0. After the bounce, they fall
into the vacuum nearest φ = 0. The basin diagram is trivial:
ALL pre-bounce vacua → vacuum nearest φ = 0.

The only question is whether some pre-bounce vacua DON'T get
fully reset (fields that start far from φ = 0 and don't reach
it during the bounce). But for ξ ~ O(1), the curvature force
is Planck-scale and the bounce easily moves the field by
~ M_Pl (the potential scale) in time ~ t_Pl.

**Estimated probability of new insight: < 5%.**

### Candidate E (nonadiabatic): Exact Bogoliubov coefficients

**Calculation:** Compute |β_k|² for a massive scalar with
curvature coupling through the bounce, for various m and ξ.

**What it would show:** Exact spectrum of produced particles
and condensate amplitude.

**Why it probably won't help:**

We already did this calculation for the tensor sector (Branch H).
The mathematical structure is identical (replace tensor → scalar,
add mass term). The result: |β_k|² ∝ 1/k² for k ≪ k_b, with
P ~ 10⁻⁶⁴-scale amplitude after dilution. Adding ξ ~ O(1)
changes the amplitude by O(1) factors, not by 10⁶.

The fundamental suppression is dilution: (a_b/a_0)^n ~ 10⁻³²n.
No coupling constant changes this.

**Estimated probability of success: < 1%.**

---

## The Honest Assessment

No calculation is likely to reverse the Phase 1 conclusion.
The failures are STRUCTURAL:

1. **Liouville's theorem** is a mathematical fact that cannot
   be circumvented by better numerics.

2. **The naturalness dilemma** (ξ ~ O(1) vs. mass protection)
   is a field-theory result independent of the bounce details.

3. **Scale separation** (10⁶¹ in mass) cannot be bridged by
   O(1) couplings.

These are the same barriers that closed previous branches,
manifesting in a new context (state selection instead of energy
budget or compatibility).

---

## If Forced to Choose One Calculation

If a Phase 2 calculation MUST be done (to achieve complete
closure), the best target would be:

### The pNGB contraction attractor test

**Model:** θ̈ + 3H(t)θ̇ + ξR(t)θ = 0 with full spin-torsion
bounce background from t = -∞ to t = +∞.

**Grid:** 100 × 100 values of (θ_pre, θ̇_pre) uniformly in
[0, 2π] × [-M_Pl, M_Pl].

**Output:** The distribution of θ_post. If it is narrower than
[0, 2π], quantify the narrowing ratio.

**What would kill it quickly:** If the narrowing ratio is > 0.5
(less than factor-2 narrowing), the mechanism provides no useful
predictive content.

**Expected result:** Narrowing ratio ≈ 1.0 (no narrowing) for
m ~ H₀, because the field is frozen during the entire
contraction + bounce + expansion. The map is approximately
the identity.

**Time estimate:** 1 session (simple ODE integration).

### Why this is the best target

1. It directly tests the strongest candidate (A: pNGB)
2. It would definitively close the narrowing question
3. The calculation is fast (1D ODE, not PDE)
4. A null result is publishable as part of a comprehensive
   closure paper
5. It provides a quantitative number (narrowing ratio) rather
   than a qualitative argument

### What would need to happen for it to succeed

For a non-trivial result, we would need: the contraction phase
(H < 0) to amplify θ̇ by enough that the bounce kick creates a
nonlinear (wrapping) effect, mapping the circle [0, 2π] onto
itself multiple times. This would concentrate the probability
density at specific θ values (caustics).

This requires: anti-friction amplification factor > 2π/θ_typical.
For θ_typical ~ O(1): need amplification > O(1). For m ~ H₀:
the amplification during contraction is ~ 1 (field is frozen).
For m ~ M_Pl (not DE): amplification could be large.

**The mechanism only works for Planck-mass fields, not DE fields.**

---

## Recommendation

**Do not proceed to Phase 2.** The structural barriers
(Liouville + naturalness + scale separation) are comprehensive
and well-understood. A numerical calculation would confirm the
analytic conclusion at the cost of 1-2 sessions with no
scientific gain.

The remaining scientific value is in the CLOSURE ITSELF:
documenting that state selection joins the list of failed
mechanisms, with the specific identification of the Liouville
barrier as the ninth structural obstacle.
