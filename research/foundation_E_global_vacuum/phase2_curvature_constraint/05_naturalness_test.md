# Phase 2 — Naturalness Test

**Date:** 2026-03-15

---

## Question

Is the resulting Λ from the curvature constraint natural, stable
under quantum corrections, and free from reintroducing the CC problem?

---

## Test 1: Parameter Sensitivity

### The Λ formula

```
Λ = (χ₀ M̃_Pl² + I_matter) / (4V₄)
```

This depends on:
- χ₀ (free parameter)
- M̃_Pl² = M_Pl² + 2λ (effective Planck mass)
- I_matter = V_c ∫ dt a³(2ρ + 6p) (matter integral)
- V₄ = V_c ∫ dt a³ (spacetime 4-volume)

### Sensitivity to χ₀

For Λ_obs ~ 10⁻¹²² M_Pl⁴:

```
χ₀ ~ 4Λ_obs V₄ / M̃_Pl² - I_matter / M̃_Pl²
```

Both terms on the right are huge in Planck units (V₄ and I_matter
involve a_max³ ~ 10^{90} × a_min³). The difference must be fine-tuned
to give Λ_obs ~ 10⁻¹²² M_Pl⁴.

This is EXACTLY the same fine-tuning problem as the original CC
problem, with χ₀ playing the role of the bare Λ.

**FAILS. The tuning is relocated, not resolved.**

---

## Test 2: Radiative Stability

### The question

If a phase transition shifts the vacuum energy by δV₀, does the
constraint automatically adjust Λ, or must χ₀ be retuned?

### Analysis

Under L_matter → L_matter + V₀ (constant vacuum shift):

```
I_matter → I_matter + (2V₀ + 6 × 0) V₄ = I_matter + 2V₀ V₄
```

(since vacuum has p = -V₀, so 2ρ + 6p = 2V₀ - 6V₀ = -4V₀.
Actually wait:

For vacuum energy: ρ_vac = V₀, p_vac = -V₀.
So 2ρ + 6p = 2V₀ - 6V₀ = -4V₀.

```
I_matter → I_matter - 4V₀ V₄
```

Then:
```
Λ → (χ₀ M̃_Pl² + I_matter - 4V₀ V₄) / (4V₄)
   = Λ_old - V₀
```

**The effective Λ SHIFTS by -V₀ under a vacuum energy shift V₀.**

This means the constraint does NOT protect Λ against vacuum energy
shifts. A phase transition that adds V₀ to the vacuum directly
shifts Λ by -V₀.

Wait — this seems wrong. Let me check.

Actually, the effective cosmological constant in the Friedmann
equation includes BOTH the bare Λ and the vacuum contribution V₀.
The total is:

```
Λ_total = Λ + V₀ = (Λ_old - V₀) + V₀ = Λ_old
```

Ah — so the constraint DOES absorb the shift! When V₀ shifts the
vacuum, Λ (the bare CC in the action) adjusts by -V₀, keeping the
TOTAL Λ_total = Λ + V₀ unchanged.

**But:** This only works for the SELF-CONSISTENT solution. The
constraint ∫√g R = χ₀ determines the full cosmological evolution
including the vacuum shift. The Λ that solves the self-consistency
equation automatically absorbs constant vacuum shifts.

**Hmm — but this means Λ_total is fixed by χ₀, not by the vacuum
energy. The vacuum shift just reshuffles between bare Λ and V₀.**

### So is this radiatively stable?

PARTIALLY. The mechanism absorbs constant vacuum shifts (the self-
consistent Λ_total is independent of V₀). But:

1. This only holds for CONSTANT shifts. Time-dependent vacuum
   contributions are not absorbed.
2. The self-consistent Λ_total still depends on χ₀, which must
   be tuned.
3. Quantum corrections to the GRAVITATIONAL sector (renormalization
   of M_Pl²) are not absorbed.

**MARGINAL PASS on radiative stability for constant vacuum shifts.
FAILS on the broader naturalness question because χ₀ is tuned.**

---

## Test 3: Reintroduction of the CC Problem

### Does the mechanism solve the CC problem?

The cosmological constant problem has three aspects:

1. **Old CC problem:** Why is Λ_obs so much smaller than M_Pl⁴?
2. **New CC problem:** Why is Λ_obs ~ ρ_matter today (coincidence)?
3. **Radiative CC problem:** Why doesn't Λ receive large loop
   corrections?

The curvature constraint addresses:
- Radiative problem: PARTIALLY (absorbs constant vacuum shifts)
- Old problem: NOT ADDRESSED (χ₀ must be tuned to reproduce Λ_obs)
- Coincidence: NOT ADDRESSED (no mechanism links Λ to ρ_matter)

**The mechanism relocates the old CC problem from "why is Λ small?"
to "why is χ₀ tuned to make Λ small?" This is not progress.**

---

## Test 4: Comparison with Simply Inserting Λ

### Is the constraint better than just putting Λ in by hand?

With Λ by hand: one free parameter (Λ), must be tuned to 10⁻¹²².
With the constraint: one free parameter (χ₀), must be tuned to give
Λ ~ 10⁻¹²².

The constraint adds:
- A global variable λ (shifts M_Pl²)
- A self-consistency equation (transcendental, hard to solve)
- Potential acausality (requires future boundary data)

The constraint does NOT add:
- An explanation for why Λ is small
- A prediction for the value of Λ
- A connection to bounce physics

**The constraint is STRICTLY WORSE than inserting Λ by hand: same
number of tuned parameters, more mathematical complexity, potential
acausality, and no additional predictions.**

---

## Summary

| Test | Result |
|------|--------|
| Parameter sensitivity | FAILS — χ₀ must be tuned equivalently to Λ |
| Radiative stability (constant shifts) | MARGINAL PASS — absorbed by self-consistency |
| Radiative stability (general) | FAILS — M_Pl² corrections not absorbed |
| Old CC problem | NOT ADDRESSED — tuning relocated to χ₀ |
| Coincidence problem | NOT ADDRESSED |
| Better than hand-inserted Λ? | NO — same tuning, more complexity |

---

## Verdict

**The global curvature constraint ∫√g R = χ₀ FAILS the naturalness
test.** It relocates the cosmological constant fine-tuning from Λ
to χ₀ without reducing the degree of tuning or providing additional
explanatory power.

The partial success (absorption of constant vacuum shifts) is
genuine but insufficient. It does not address the core problem
(why is the effective Λ small?) and does not connect to bounce
physics.

This failure mode is: **FAIL_HIDDEN_TUNING** — the mechanism
relocates rather than eliminates the fine-tuning.
