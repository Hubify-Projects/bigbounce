# Branch U: Two-Field ALP + DE — Problem Statement

**Date:** 2026-03-17
**Status:** Phase 1 Theory Investigation

---

## The Rolling-vs-Freezing Tension

The spectator ALP model (Branch R) successfully predicts cosmic birefringence:

| Quantity | Spectator ALP | Observed |
|----------|--------------|----------|
| β (deg) | 0.27 × θ_i | 0.342 ± 0.094 |
| θ_i needed | ~1.3 | — |

But this model **cannot** simultaneously explain dark energy. The Phase 2 prefit (Branch R, `05_quick_prefit.md`) established:

| Regime | Birefringence (η) | Dark energy (w) | Conflict |
|--------|-------------------|-----------------|----------|
| Spectator (m >> H_0) | η → 1 (good) | Ω_a → 0 (no DE) | Need separate Λ |
| DE-like (m ~ H_0) | η ~ 0.5 (reduced) | w ~ -0.95 (good) | max β ~ 0.16° (factor 2 below obs) |

**The single-field ALP cannot do both jobs at once.** Birefringence demands rolling (large η); DE demands freezing (w ~ -1, small η). On the Ω_a = 0.68 contour, max β ≈ 0.16° — a factor 2 below the observed 0.35°.

---

## The Question

Can a **two-field model** resolve this tension?

The idea: one field φ_1 (light, m_1 >> H_0) provides birefringence by rolling freely, while a second field φ_2 (ultralight, m_2 ~ H_0) provides dark energy by remaining frozen. Each field does what it does best.

---

## Why This Might Work

1. **Division of labor.** φ_1 handles birefringence (needs to roll), φ_2 handles DE (needs to freeze). No single field is asked to do both.
2. **Natural in ALP landscape.** String/M-theory compactifications generically produce multiple axions at different mass scales (the "axiverse"). Two ALPs is not ad hoc.
3. **ECH motivation.** The parity-odd sector could in principle generate multiple pseudoscalar modes at different scales (Barbero-Immirzi + additional PGT modes).
4. **Phenomenological simplicity.** Each field has 2-3 parameters; the model has ~5-6 total. This is comparable to w_0-w_a CDM.

---

## Why This Might Fail

1. **No unique ECH derivation.** The two-field model is not derived from ECH any more than the single-field spectator. ECH *motivates* f_a ~ M_Pl but does not predict the number of fields or their masses.
2. **Cosmological constant problem.** The DE field φ_2 with m_2 ~ H_0 reintroduces the CC problem: why is m_2 ~ 10^{-33} eV? This is the same tuning as bare Λ.
3. **Overparameterization risk.** With 5-6 free parameters and effectively one birefringence data point + standard cosmology, the model may be underconstrained.
4. **Branch I lesson.** The Horndeski stability analysis (Branch I) showed that DE fields are frozen at the bounce — scale separation kills any bounce-era DE imprint. Two fields likely have the same problem.
5. **Occam's razor.** If single-field spectator + Λ fits all data, what does two-field add? It must provide a concrete improvement, not just aesthetic unification.

---

## Success Criteria

Branch U succeeds if:
1. The two-field model resolves the rolling-vs-freezing tension quantitatively (β ≥ 0.3° with Ω_DE = 0.68)
2. Parameter space is natural (no fine-tuning beyond what Λ already requires)
3. The model makes at least one distinctive prediction beyond the spectator ALP
4. The bounce adds something nontrivial (otherwise it's just standard axiverse cosmology)

Branch U is **not worth pursuing** if:
- It reduces to spectator ALP + Λ with extra unused parameters
- The bounce connection is purely motivational (no quantitative consequence)
- All distinctive predictions require LiteBIRD-level data that the spectator model also predicts

---

## Relationship to Other Branches

| Branch | Status | Lesson for Branch U |
|--------|--------|-------------------|
| R (spectator ALP) | ALP_EQUIVALENT_TO_BETA | Baseline to beat |
| I (Horndeski stability) | WEAK | DE frozen at bounce (scale separation) |
| J (state selection) | CLOSED | Bounce cannot select vacuum state |
| O (hidden-sector vacuum) | CLOSED | Bounce determines WHETHER, not WHAT |
| A-G (direct DE) | CLOSED | 7 barriers against minimal DE derivation |

The key constraint from these branches: **the bounce cannot communicate with the DE sector.** Any two-field model must acknowledge this — the bounce is cosmological background, not a DE generation mechanism.
