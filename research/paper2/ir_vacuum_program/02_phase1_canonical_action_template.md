# Phase 1 Template: Canonical Action Memo

**Status:** NOT STARTED
**Target:** Month 1–2

This document is a template for the canonical action memo. Fill in each section with explicit equations. No ambiguity should remain after this memo is complete.

---

## 1. Field Content

| Field | Symbol | Type | Dynamical? | Role |
|-------|--------|------|-----------|------|
| Tetrad | e^I_μ | Lorentz vector-valued 1-form | YES | Gravitational field |
| Spin connection | ω^{IJ}_μ | Lorentz-valued 1-form | ALGEBRAIC (non-propagating in EC) | Encodes torsion |
| Dirac fermion(s) | ψ_i | Spinor | YES | Source of torsion |
| Barbero-Immirzi | γ | Scalar | FIXED / FIELD? | **DECIDE** |

## 2. The Full Action

Write explicitly:

```
S_total = S_EC + S_Holst + S_Dirac + S_boundary
```

**S_EC (Einstein-Cartan):**
```
S_EC = (M_Pl²/2) ∫ ε_{IJKL} e^I ∧ e^J ∧ F^{KL}[ω]
```

**S_Holst:**
```
S_Holst = (M_Pl²/2γ) ∫ e^I ∧ e^J ∧ F_{IJ}[ω]
```

**S_Dirac:**
```
S_Dirac = ∫ d⁴x |e| [ψ̄ iγ^μ (∂_μ + ¼ ω_{μ}^{IJ} γ_I γ_J) ψ - m ψ̄ψ]
```

**S_boundary (Nieh-Yan):**
```
[TO BE SPECIFIED — does this contribute after integration?]
```

## 3. Torsion Decomposition

Decompose spin connection: ω = ω̊ + K (Levi-Civita + contorsion)

Decompose torsion: T^I = (1/3) e^I ∧ V + S^I + (1/3) *[e^I ∧ A]
- V_μ: trace vector
- A_μ: axial trace vector
- S^I_{μν}: tensor part (tracefree, totally antisymmetric part vanishes in 4D)

**Key:** Only the axial part A_μ couples to fermions in EC gravity.

## 4. Torsion Equation of Motion

Vary S_total w.r.t. ω^{IJ}_μ. The result (non-propagating torsion):

```
T^I_{μν} = [DERIVE EXPLICITLY — include Holst term contribution]
```

**With Holst term, the axial torsion becomes:**
```
A_μ = -(3κ²/8) × (1 + 1/γ²)⁻¹ × (ψ̄ γ_μ γ⁵ ψ + (1/γ) ψ̄ γ_μ ψ)
```

[VERIFY — the 1/γ mixing of vector and axial currents is the source of parity violation]

## 5. Reduced Action (After Torsion Elimination)

Substitute torsion back into the action:

```
S_reduced = S_GR[g] + S_Dirac_minimal[g, ψ] + S_4-fermi[ψ]
```

where:
```
S_4-fermi = ∫ d⁴x √-g [-G_V (ψ̄ γ^μ ψ)² - G_A (ψ̄ γ^μ γ⁵ ψ)² - G_VA (ψ̄ γ^μ ψ)(ψ̄ γ_μ γ⁵ ψ)]
```

**The coupling constants G_V, G_A, G_VA depend on γ:**

```
G_V = [DERIVE]
G_A = [DERIVE]
G_VA = [DERIVE] ← THIS IS THE PARITY-ODD COUPLING
```

When γ → ∞: G_VA → 0 (parity restored). This is the key.

## 6. Fierz Rearrangement

Rewrite in scalar/pseudoscalar channels for Hubbard-Stratonovich:

```
-G_A (ψ̄ γ^μ γ⁵ ψ)² = G_s (ψ̄ψ)² + G_p (ψ̄ iγ⁵ψ)² + ...
```

[DERIVE the exact Fierz identities with γ-dependent coefficients]

## 7. Parity Properties

| Term | Parity | Present when γ → ∞? |
|------|--------|---------------------|
| G_V (ψ̄ γ^μ ψ)² | Even | YES (standard EC) |
| G_A (ψ̄ γ^μ γ⁵ ψ)² | Even | YES (standard EC) |
| G_VA (vector × axial) | **Odd** | **NO** (vanishes) |
| G_s (ψ̄ψ)² | Even | YES |
| G_p (ψ̄ iγ⁵ψ)² | Even | YES |

**The parity-odd term G_VA is the ONLY new physics from the Holst term.**

## 8. Questions This Memo Must Answer

- [ ] What is the exact value of G_VA in terms of κ, γ?
- [ ] Does the Nieh-Yan boundary term contribute after torsion elimination?
- [ ] How many independent fermion species contribute?
- [ ] Is G_VA large enough for dynamical symmetry breaking?
- [ ] Does the parity-odd coupling generate a pseudoscalar condensate that the standard (γ → ∞) theory does not?

## 9. Literature Cross-Check

| Reference | Result to verify |
|-----------|-----------------|
| Hehl+ 1976 | Standard EC four-fermion interaction |
| Freidel-Minic-Takeuchi 2005 | Holst-induced parity-odd term |
| Mercuri 2006, 2009 | Fermion coupling to Holst action |
| Shapiro-Teixeira 2014 | Quantum EC with Holst |
| Chattopadhyay 2023 | One-loop in chiral EC |
