# 03: Predictivity vs Flexibility Scorecard

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Scorecard Framework

Each model is scored on:
1. Number of continuous free parameters beyond base cosmology (H_0, Omega_m, etc.)
2. Number of extra fields beyond the inflaton/contracting scalar
3. Number of distinct mechanisms invoked
4. Tightness of observable predictions
5. Whether inflation can mimic the signatures
6. Whether current data pressure the model
7. Whether next-gen data could kill it

---

## Model B: Wilson-Ewing LCDM Quasi-Dust Bounce

### Parameter Count

| Parameter | Role | Constrained by | Free? |
|-----------|------|---------------|-------|
| rho_c (or gamma) | LQC bounce density | Immirzi parameter | Fixed by theory (gamma = 0.274) |
| epsilon (= -w) | EOS deviation from dust | n_s | YES — 1 free parameter |
| Lambda | Cosmological constant | Provides w < 0 | Already in LCDM (not new) |

**Continuous free parameters beyond minimal matter bounce: 1** (epsilon, which determines n_s)

**Extra fields: 0** (the matter is dust + Lambda, both already in LCDM)

**Distinct mechanisms invoked: 2**
1. LQC quantum bounce (resolves singularity, suppresses r)
2. Quasi-dust contraction with Lambda (provides red tilt)

### Observable Predictions

| Observable | Prediction | Tightness |
|-----------|-----------|-----------|
| n_s | 1 - 12*epsilon (one-parameter family) | MEDIUM — tuned to fit, but tight once epsilon is fixed |
| r | ~10^-4 | TIGHT — set by LQC, not adjustable |
| f_NL | -35/8 = -4.375 (if correct convention) | **VERY TIGHT** — parameter-free |
| f_NL | +5/12 = 0.42 (if other convention) | TIGHT but useless (too small) |
| alpha_s | ~+10^-4 | TIGHT but unmeasurable |
| n_T | >0 (blue) | TIGHT but unmeasurable (r too small) |

### Inflation Mimicry

| Observable | Can inflation reproduce? |
|-----------|------------------------|
| n_s = 0.964 | YES — trivially (Starobinsky, or any slow-roll V(phi)) |
| r ~ 10^-4 | YES — many small-field models |
| f_NL = -4.375 | **DIFFICULT** — single-field gives ~0; multi-field typically gives positive f_NL |
| f_NL = +0.42 | YES — trivially (within single-field prediction) |
| alpha_s > 0 | YES — some inflation models; not distinctive |

### Current Data Pressure

| Constraint | Status |
|-----------|--------|
| n_s = 0.964 | CONSISTENT with Planck |
| r < 0.036 | CONSISTENT (r ~ 10^-4) |
| f_NL = -0.9 +/- 5.1 | CONSISTENT (whether -4.375 or +0.42) |
| alpha_s = -0.005 +/- 0.007 | CONSISTENT (alpha_s ~ 10^-4 is within 1sigma of zero) |

**No current data pressure.** But also no current data support beyond consistency.

### Next-Gen Kill Potential

| Experiment | Could it kill Model B? |
|-----------|----------------------|
| LiteBIRD (sigma(r) ~ 0.001) | NO — r ~ 10^-4 is below sensitivity |
| CMB-S4 (sigma(f_NL) ~ 2.5) | MARGINAL — if f_NL = -4.375, it would be 1.8 sigma. Not enough to kill but suggestive |
| SPHEREx (sigma(f_NL) ~ 1.5) | MARGINAL — 2.9 sigma if f_NL = -4.375. Getting interesting |
| MegaMapper (sigma(f_NL) ~ 0.5) | **YES** — 8.75 sigma if f_NL = -4.375. Would confirm or kill decisively |
| CMB-S4 alpha_s (sigma ~ 0.003) | NO — predicted alpha_s ~ 10^-4 is undetectable |

### Classification: **MEDIUM_PREDICTIVITY**

Rationale:
- One tight parameter-free prediction (f_NL, IF the convention is correct)
- One fitted parameter (epsilon for n_s)
- One untestable prediction (r ~ 10^-4)
- Low parameter count (good)
- But the single testable discriminator depends entirely on a convention question

---

## Comparison: Starobinsky R^2 Inflation

### Parameter Count
- **Continuous free parameters: 1** (M^2, the Starobinsky mass, fixed by A_s)
- **Extra fields: 0**
- **Mechanisms: 1** (R^2 gravity = scalar field with specific potential)

### Observable Predictions
| Observable | Prediction | Tightness |
|-----------|-----------|-----------|
| n_s | 1 - 2/N ~ 0.964 (N=55) | **VERY TIGHT** — predicted from e-folds |
| r | 12/N^2 ~ 0.004 | **TIGHT** — testable by LiteBIRD |
| f_NL | ~O(n_s - 1) ~ -0.04 | TIGHT but unmeasurable |
| alpha_s | -2/N^2 ~ -0.0007 | TIGHT but unmeasurable |

### Classification: **HIGH_PREDICTIVITY**

Starobinsky has 1 parameter, predicts n_s from N (not fitted), and has a TESTABLE r prediction. Model B has 1 parameter, fits n_s from epsilon, and has an untestable r prediction but potentially testable f_NL.

---

## Head-to-Head Comparison

| Criterion | Model B (LCDM Bounce) | Starobinsky R^2 |
|-----------|----------------------|-----------------|
| Free parameters | 1 (epsilon) | 1 (M^2, but effectively 0 since fixed by A_s) |
| n_s predicted or fitted | Fitted (from epsilon) | **Predicted** (from N) |
| r testable? | No (10^-4) | **Yes** (0.004, LiteBIRD target) |
| f_NL distinctive? | **Yes** (if -4.375) / No (if +0.42) | No (~0) |
| alpha_s testable? | No | No |
| Singularity resolved? | **Yes** | No |
| BKL problem? | Need ekpyrotic pre-phase (adds complexity) | N/A |
| Trans-Planckian? | **Absent** | Present |
| Kill experiment | MegaMapper (f_NL, ~2035) | LiteBIRD (r, ~2030) |

**Starobinsky is more predictive overall.** Model B's only competitive advantage is f_NL (if negative and large) and the theoretical virtues of singularity resolution and trans-Planckian absence.

---

## Model C: ILS Ekpyrotic (for completeness)

### Parameter Count
- Continuous free parameters: **3+** (potential shape, Omega(phi) function shape, conversion dynamics)
- Extra fields: **1** (entropy field chi)
- Mechanisms: **3** (ekpyrotic contraction, non-minimal kinetic coupling, entropy-to-adiabatic conversion)

### Observable Predictions
| Observable | Prediction | Tightness |
|-----------|-----------|-----------|
| n_s | Tunable via Omega(phi) | LOW — functional freedom |
| r | ~0 | TIGHT but untestable |
| f_NL | ~+5 | MEDIUM — depends on conversion details |
| alpha_s | ~0 by construction | TIGHT but unmeasurable |

### Classification: **LOW_PREDICTIVITY**

Too much functional freedom. The kinetic coupling function Omega(phi) essentially plays the same role as the inflaton potential V(phi) — it can be engineered to produce any n_s. The model has more free functions than inflation, not fewer.

---

## Summary Table

| Model | Params | Extra Fields | Mechanisms | Predictivity | Best Test |
|-------|--------|-------------|------------|-------------|-----------|
| B: LCDM Bounce | 1 | 0 | 2 | MEDIUM | f_NL (if -4.375) |
| C: ILS Ekpyrotic | 3+ | 1 | 3 | LOW | None sharp |
| Starobinsky R^2 | 0-1 | 0 | 1 | HIGH | r (LiteBIRD) |
