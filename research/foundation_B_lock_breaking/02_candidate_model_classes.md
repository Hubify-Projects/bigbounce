# Foundation B — Candidate Model Classes

**Date:** 2026-03-14

---

## Overview

We identify five candidate mechanisms that could, in principle, break
the mass-coupling lock by introducing independent parameters for mass
and coupling. Each is assessed for its structural promise and risks.

---

## Model A: Torsion + Independent Higgs-like VEV Sector

### Action sketch

```
S = S_PGT[e, ω] + ∫ d⁴x √g [ -½ (∂σ)² - V(σ) - λ σ² B_μ B^μ ]
```

where B_μ is the 0⁻ axial torsion mode and σ is a scalar field with
potential V(σ) = -μ_σ² σ²/2 + λ_σ σ⁴/4 that develops a VEV ⟨σ⟩ = v.

### Mass and coupling after SSB

```
m_B² = m_PGT² + λ v²     (mass gets independent contribution)
g_eff ~ 1/(M_Pl √|t₃|)    (coupling unchanged — from gravitational sector)
```

### Why it might break the lock

The torsion mass now has two sources: the PGT kinetic normalization
(∝ M_Pl/√|t₃|) AND the Higgs portal (∝ √λ v). If λv² ≫ m_PGT², the
mass is set by the Higgs sector while the coupling is set by the
gravitational sector. These are independent.

But wait — does the coupling also shift? The σ-B coupling λσ²B²
contributes to the B propagator but NOT to the B-J matter vertex
(which is fixed by the gauge structure). So the mass gets an
independent contribution while the coupling does not. The lock
breaks IF the Higgs mass dominates.

### Biggest risk

**The coupling is still suppressed.** The matter coupling g_eff comes
from the PGT sector and scales as 1/(M_Pl √|t₃|). Making B light
via the Higgs sector allows m_B to be small, but g_eff is STILL
suppressed if |t₃| is large. The problem is that we still need
|t₃| to be large for other reasons (ghost-freedom constraints, or
simply because the PGT mass contribution must not dominate).

Actually: if the Higgs portal dominates the mass (λv² ≫ M_Pl²/|t₃|),
we can take |t₃| ~ O(1) and get:

```
m_B ~ √λ v      (set by Higgs sector, can be meV if v is chosen)
g_eff ~ 1/M_Pl   (gravitational strength — NOT suppressed)
```

This is UNLOCKED if |t₃| ~ O(1) is consistent with ghost-freedom.

**Critical check:** Are there ghost-free PGT configurations with
|t₃| ~ O(1)? Yes — the ghost-free conditions constrain signs and
ratios but do not require large |t₃|. The hierarchy problem was
introduced by CHOOSING |t₃| large to get a light mass from PGT alone.
If the mass comes from elsewhere, |t₃| ~ O(1) is allowed.

**Second risk:** Where does the tiny v come from? Need √λ v ~ meV.
If λ ~ O(1), need v ~ meV. This is a new hierarchy. If v ~ M_EW,
need λ ~ 10⁻⁴⁴. This is the standard scalar hierarchy problem —
we have moved the fine-tuning from |t₃| to λv².

**Verdict: PARTIALLY_UNLOCKED.** The lock breaks structurally, but the
naturalness problem is transferred to the Higgs portal sector. Progress
on the coupling; no progress on naturalness.

---

## Model B: Metric-Affine Pseudoscalar with Non-Topological Nieh-Yan

### Action sketch

In metric-affine gravity (MAG), the connection has both torsion AND
non-metricity. The Nieh-Yan 4-form N₄ = d(e^I ∧ T_I) is NOT exact
when non-metricity Q_μνρ ≠ 0:

```
S = S_MAG[e, Γ] + ∫ d⁴x √g [ -½ f(Γ)(∂θ)² + α θ N₄ ]
```

where θ is a pseudoscalar and α is the coupling constant.

### Why it might break the lock

In standard PGT (metric-compatible), the Nieh-Yan coupling θ N₄ is a
total derivative after torsion elimination — this is why Route T1
failed. But in MAG, the non-metricity modifies the exterior derivative
structure, and θ N₄ retains local dynamical content.

The mass of θ comes from the potential V(θ), which can be protected
by a shift symmetry θ → θ + c (broken softly or by non-perturbative
effects to generate a small mass). The coupling to matter comes from
the θ N₄ term, which involves torsion — this coupling has its own
coefficient α, independent of the shift-symmetry-breaking scale.

```
m_θ ~ Λ_shift²/f     (from shift-symmetry breaking, can be tiny)
g_eff ~ α/f           (from Nieh-Yan coupling, independent of mass)
```

where f is the pseudoscalar decay constant.

### Biggest risk

**The Nieh-Yan form may still be effectively topological in MAG.**
The claim that N₄ is non-exact in MAG depends on specific assumptions
about the non-metricity sector. If the dynamical equations of MAG
force the relevant non-metricity components to vanish on shell, N₄
reduces back to a total derivative and this model collapses to T1.

This is a precise mathematical question: compute dN₄ in the presence
of non-metricity. If dN₄ ≠ 0, there is local content. If dN₄ = 0
on shell, the model fails.

**Second risk:** The kinetic term f(Γ) depends on the connection.
After solving the connection field equations, this could introduce
a dependence of the kinetic normalization on the same parameters that
control the coupling, reintroducing the lock.

**Verdict: UNKNOWN — requires explicit computation.** If the Nieh-Yan
form is genuinely non-topological in MAG, this is the most promising
candidate because it provides both an independent mass (shift symmetry)
and an independent coupling (geometric Nieh-Yan). But the first check
(is N₄ non-exact on shell in MAG?) must be performed before investing
further.

---

## Model C: Two-Field Geometric System (Mass-Coupling Separation)

### Action sketch

```
S = S_grav[e, ω] + ∫ d⁴x √g [
    -½ Z_A(ω) (∂A)² - ½ Z_B(ω) (∂B)²
    - μ² A² - λ A² B²
    + g_A A J_matter + g_B B J_gravity
]
```

where A is the "coupling carrier" (couples to matter with fixed
strength g_A) and B is the "mass setter" (its VEV or dynamics
determines the mass of A through the portal coupling λ).

### Why it might break the lock

In a two-field system, the mass of A can depend on field B through
the portal term λA²B². If B develops a VEV or a condensate, the
mass of A shifts:

```
m_A² = μ² + λ ⟨B²⟩
```

The coupling of A to matter (g_A) is a separate parameter. As long as
A's kinetic normalization Z_A does not depend on the same parameters
that control ⟨B²⟩, the lock is broken.

### Biggest risk

**Where do A and B come from geometrically?** In PGT, there are at most
three ghost-free single-mode propagating torsion modes (0⁺, 0⁻, 2⁺).
A two-field system requires two simultaneously propagating modes. The
ghost-free conditions for multi-mode PGT are much more restrictive.
Blagojević and Cvetković have shown that most two-mode combinations
are either ghostly or strongly constrained.

Even if a ghost-free two-mode sector exists, both modes' kinetic
normalizations and masses are determined by the same PGT coupling
constants. The lock may just appear in a higher-dimensional parameter
space — a "multi-field lock."

**Verdict: LIKELY_LOCKED.** The two-field idea is correct in principle
(the Standard Model breaks the lock for W bosons via the Higgs). But
in PGT, the geometric origin constrains the parameter space so severely
that independent control of two modes is unlikely. Would need to
demonstrate a ghost-free two-mode parameter region where the portal
coupling is not determined by the same parameters as the kinetic terms.

---

## Model D: Vacuum Sequestering with Torsion-Modified Constraint

### Action sketch

The Kaloper-Padilla sequestering mechanism:

```
S = ∫ d⁴x √g [ M_Pl² R/2 - Λ + L_matter ]
    + σ₁(∫ d⁴x √g Λ/Λ* - 1)
    + σ₂(∫ d⁴x √g L_matter/μ*⁴ - 1)
```

where σ₁, σ₂ are Lagrange multipliers enforcing global constraints,
and Λ*, μ* are reference scales.

In EC gravity with torsion, the gravitational sector includes torsion-
squared terms. The question is whether torsion modifies the global
constraint in a way that provides an independent parameter.

### Why it might break the lock

Sequestering does not produce a propagating dark-energy field — it
dynamically adjusts Λ to be small. The "mass-coupling lock" in the
usual sense does not apply because there is no propagating mode to
lock. Instead, the mechanism directly addresses the cosmological
constant.

If the torsion sector modifies the sequestering constraint (e.g., by
contributing a torsion-dependent term to the global volume integral),
the effective Λ might depend on torsion parameters independently of
the standard gravitational coupling. This would be a different kind
of "lock breaking" — not through an independent propagating mode, but
through a modified global constraint.

### Biggest risk

**Sequestering may not produce observable signatures (DR3 failure).**
Pure Kaloper-Padilla sequestering sets Λ small but predicts nothing
beyond ΛCDM. If torsion modifies the constraint, it might introduce
an additional prediction — but this is speculative.

**The torsion sector may not affect the global constraints at all.**
In minimal EC, torsion is algebraic and eliminated before the global
constraints are imposed. The sequestering mechanism would then be
identical to the torsion-free version.

**Verdict: ORTHOGONAL.** This does not break the mass-coupling lock
because it does not use a propagating mode. It addresses the CC
problem by a different route (global constraint). Worth investigating
as a separate line, but does not directly address the lock.

---

## Model E: Distortion Field in Metric-Affine Gravity

### Action sketch

In MAG, the connection has 64 independent components, decomposing into:
- Christoffel symbols (Levi-Civita, 40 components)
- Torsion (24 components)
- Non-metricity (40 components — but with overlap)

The "distortion tensor" Δ^λ_μν = Γ^λ_μν - {^λ_μν} (connection minus
Levi-Civita) contains both torsion and non-metricity. In a quadratic
MAG action:

```
S = ∫ d⁴x √g [ M_Pl² R/2 + a₁ T² + a₂ Q² + a₃ T·Q + ... ]
```

the propagating modes, their masses, and their couplings depend on a
much larger parameter space (a₁, a₂, a₃, ...) than in PGT alone.

### Why it might break the lock

With non-metricity included, the propagating sector has more degrees
of freedom and more independent coupling constants. Specifically:

- Torsion-squared terms (a₁) control the torsion mode mass and kinetic
  term.
- Non-metricity-squared terms (a₂) control the non-metricity mode mass
  and kinetic term.
- Cross terms (a₃) control the mixing between torsion and non-metricity.

If a propagating mode is a MIXTURE of torsion and non-metricity, its
mass could depend on one set of couplings (e.g., the diagonal a₁, a₂)
while its matter coupling depends on a different set (e.g., the
cross-term a₃ and the torsion-matter coupling). This is structurally
similar to Model C (two-field system) but with a richer parameter
space that might avoid the multi-field ghost constraints of pure PGT.

### Biggest risk

**The ghost-free sector of MAG is largely unmapped.** While PGT has
been studied for 45+ years with well-known ghost-free regions, the
quadratic MAG ghost structure is much more complex. Percacci, Jiménez,
and others have made progress, but the full ghost-free parameter space
for propagating modes in quadratic MAG is not established.

**Even if ghost-free modes exist, the reduced action might re-lock.**
After solving the non-metricity field equations (which are algebraic
for most non-metricity components in standard MAG), the effective
torsion action might collapse back to a structure where mass and
coupling share a common origin.

**Verdict: UNKNOWN — highest risk but highest potential payoff.** If
the MAG parameter space is rich enough to allow independent mass and
coupling for a mixed torsion/non-metricity mode, this is the most
natural geometric lock-breaking mechanism. But the ghost analysis
is a major technical barrier.

---

## Summary Table

| Model | Mechanism | Lock status | Mass natural? | Risk |
|-------|-----------|-------------|---------------|------|
| A | Higgs portal for torsion mass | PARTIALLY_UNLOCKED | No (transfers hierarchy) | Moderate |
| B | Non-topological Nieh-Yan in MAG | UNKNOWN | Yes (shift symmetry) | High (may be topological) |
| C | Two-field geometric portal | LIKELY_LOCKED | Depends on portal | High (ghost constraints) |
| D | Vacuum sequestering + torsion | ORTHOGONAL | N/A (no prop. mode) | Moderate |
| E | MAG distortion field | UNKNOWN | Unknown | Very high (unmapped ghosts) |

### Priority ranking for investigation

1. **Model A** — can be analyzed immediately with known PGT results.
   The lock-breaking mechanism is clear; the question is whether the
   naturalness problem is solvable.

2. **Model B** — requires one precise mathematical check (is N₄
   non-exact in MAG?). If yes, this is the most promising candidate.

3. **Model E** — highest potential but requires extensive ghost analysis
   in quadratic MAG. Longer-term investigation.

4. **Model C** — likely blocked by PGT ghost constraints. Check the
   multi-mode ghost-free literature before investing.

5. **Model D** — orthogonal to the lock problem. Defer to a separate
   investigation.
