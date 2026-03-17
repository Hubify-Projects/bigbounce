# Phase 2 — Constrained Action

**Date:** 2026-03-15

---

## The Action

```
S = ∫ d⁴x √g [½M_Pl² R - Λ + L_matter]
    + λ (∫ d⁴x √g R - χ₀)
```

where:
- Λ is the bare cosmological constant (to be determined)
- λ is a GLOBAL Lagrange multiplier (a spacetime constant, not a field)
- χ₀ is a fixed parameter (the "curvature budget" of the spacetime)

---

## Role of the Lagrange Multiplier λ

λ enforces the constraint:

```
∫ d⁴x √g R = χ₀
```

This is a GLOBAL constraint: it does not restrict R(x) at any
individual point, only the integrated total. R(x) is free to vary
locally — the constraint controls the spacetime average.

λ is NOT a local field. It has no kinetic term, no propagation, no
equation of motion beyond the global constraint. It is a single
number determined by requiring the constraint to hold.

---

## Modified Einstein Equations

Varying the action with respect to g^μν at each point:

```
δS/δg^μν = 0
```

The ½M_Pl² R term gives the standard Einstein tensor.
The Λ term gives -Λ g_μν / 2.
The L_matter term gives the stress-energy T_μν.
The λ ∫√g R term gives an ADDITIONAL contribution.

For the constraint term:

```
δ/δg^μν [λ ∫ d⁴x √g R] = λ (R_μν - ½R g_μν + g_μν □ - ∇_μ∇_ν) × 1
```

Wait — since λ is a CONSTANT (not a field), the variation is:

```
λ δ(∫√g R)/δg^μν = λ (G_μν + g_μν □ - ∇_μ∇_ν)(1)
```

But □(1) = 0 and ∇_μ∇_ν(1) = 0. So:

```
λ δ(∫√g R)/δg^μν = λ G_μν
```

No — this needs more care. The variation of √g R with respect to
g^μν is:

```
δ(√g R) = √g (R_μν - ½R g_μν) δg^μν + √g ∇_α(g^μν δΓ^α_μν - g^μα δΓ^β_μβ)
```

The first term gives G_μν. The second term is a total divergence
that integrates to a boundary term (which we discard with appropriate
boundary conditions).

Therefore:

```
δ(∫√g R)/δg^μν = √g G_μν
```

and the full equations of motion are:

```
(½M_Pl² + λ) G_μν - Λ/2 g_μν = ½ T_μν
```

Rewriting:

```
G_μν = T_μν / (M_Pl² + 2λ) + Λ/(M_Pl² + 2λ) g_μν
```

This is standard GR with:
- RESCALED Planck mass: M̃_Pl² = M_Pl² + 2λ
- RESCALED cosmological constant: Λ̃ = Λ/(M_Pl² + 2λ) × M̃_Pl²
  = Λ (since the rescaling cancels)

Actually, let me be more precise. Define M̃_Pl² ≡ M_Pl² + 2λ. Then:

```
G_μν + Λ/M̃_Pl² g_μν = T_μν/M̃_Pl²
```

This is Einstein's equation with effective Newton's constant
G̃ = 1/(8πM̃_Pl²) and effective cosmological constant Λ_eff = Λ.

**The Lagrange multiplier λ rescales Newton's constant but does not
directly modify the cosmological constant.**

---

## How Λ Becomes Determined

The constraint itself provides the additional equation:

```
∫ d⁴x √g R = χ₀
```

On FRW: R = 6(Ḣ + 2H²). The Friedmann equations (with rescaled
M̃_Pl²) determine H(t) in terms of matter content and Λ. The
constraint then fixes Λ (or equivalently λ) by requiring the
integrated R to equal χ₀.

More explicitly:

**Step 1:** Given Λ and λ, solve the Friedmann equations:
```
3M̃_Pl² H² = ρ_total + Λ
-2M̃_Pl² Ḣ = ρ_total + p_total
```

**Step 2:** Compute R(t) = 6(Ḣ + 2H²) from the solution.

**Step 3:** Compute I_R = ∫ d⁴x √g R = ∫₀^∞ dt a³(t) R(t) × V_spatial.

**Step 4:** Enforce I_R = χ₀. This is one equation in two unknowns
(Λ, λ). Combined with the definition M̃_Pl² = M_Pl² + 2λ, we have
a system that determines both Λ and λ in terms of χ₀ and the
matter content.

In practice: for a given matter content, the constraint provides
a RELATION between Λ and the spacetime history. If we know the
matter content (radiation, matter, etc.), the constraint fixes Λ.

---

## Key Observations

### 1. λ rescales G, not Λ directly

The Lagrange multiplier enters as a shift of M_Pl². This means the
constraint modifies the STRENGTH of gravity, not just the vacuum
energy. Observational constraints on G (BBN, CMB, solar system)
limit how large λ can be.

For λ ≪ M_Pl²: the modification is perturbative. G̃ ≈ G(1 - 2λ/M_Pl²).

### 2. The constraint is one equation for the full history

I_R = χ₀ is a single integral equation that connects ALL eras of
cosmic evolution. Changing the matter content at any epoch changes
R(t) and therefore the integral, requiring Λ to readjust.

### 3. Boundary terms matter

The variation of ∫√g R produces boundary terms. In a finite-volume
spacetime (with a bounce as past boundary), these terms may contribute.
The Gibbons-Hawking-York boundary term must be included for a
well-defined variational principle.

### 4. This is NOT the same as unimodular gravity

In unimodular gravity, one fixes √g = constant (or ∫√g = fixed).
Here we fix ∫√g R = χ₀, which is a CURVATURE constraint, not a
volume constraint. The physics is different.

---

## EC/PGT Extension

In Einstein-Cartan gravity:
```
R(Γ) = R(g) + (torsion terms)
```

The constraint becomes:
```
∫ d⁴x √g R(Γ) = χ₀
```

At the bounce, the torsion terms contribute significantly:
```
R(Γ) = R(g) - 4κ²(s^μ s_μ)
```

The spin-squared term is NEGATIVE (reducing the effective curvature).
This modifies the bounce's contribution to the integral.

This will be important in the curvature integral analysis (Task 3).
