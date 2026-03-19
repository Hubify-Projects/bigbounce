# Ranked Remaining Paths: LQC-Specific and High-Value Bounce

**Created:** 2026-03-18
**Purpose:** Priority-ordered paths remaining after the LQC openings map, incorporating lessons from the f_NL derivation execution and next flagship program verdicts.

---

## #1: Complete Independent f_NL = -35/8 Verification (Gradient Expansion)

**Why #1:** The ENTIRE program rests on this single number. We are at 75% confidence. Convention is resolved but the numerical coefficient hasn't been independently reproduced. Li & Brandenberger get -35/16. This MUST be resolved before any other work matters.

**Novelty potential:** MEDIUM (verification, not discovery -- but essential foundation)

**Observational leverage:** MAXIMAL (if wrong, everything falls)

**Effort:** MEDIUM (Salopek-Bond gradient expansion, 1-2 focused sessions)

**Sprawl risk:** ZERO

**Quick kill:** If gradient expansion gives -35/8 -> confirmed in days. If -35/16 -> weakened but alive.

**Success:** f_NL = -35/8 confirmed -> confidence rises to >95%, program on granite foundation.

**Rationale for promotion to #1 (over formalism audit):** The previous ranked stack placed the LQC perturbation-formalism audit at #1 and this verification at #2. That ordering is wrong. Here is why:

1. **Foundation before decoration.** The formalism audit asks "is the prediction robust to quantum gravity corrections?" But if the prediction itself is wrong at the classical level (i.e., the pre-bounce f_NL is actually -35/16), then formalism robustness is irrelevant. You don't audit the earthquake resistance of a building before verifying the foundation is load-bearing.

2. **The derivation execution verdict is explicit.** File `fnl_derivation_execution/final_verdict.md` states: confidence is 75%, the time integral was NOT independently reproduced, and the exact next calculation is the numerical evaluation of that integral. The gradient expansion is the analytic counterpart of the same verification.

3. **The formalism audit will almost certainly return "trivially insensitive."** Both formalisms reduce to classical GR for modes with k/k_LQC ~ 10^{-56}. The bispectrum is generated during contraction, before the bounce. The probability that the formalism audit produces a non-trivial result is <5%. Spending a session on a 95%-likely-trivial check while the 25%-uncertain foundation remains unresolved is a misallocation.

4. **Every outcome of the gradient expansion is high-value.** Confirmation -> granite. Disagreement -> discovery. The formalism audit's most likely outcome is "they agree" -> no new information.

---

## #2: LQC Perturbation-Formalism Sensitivity Check

**Why #2:** Cleanest remaining "could be novel" LQC-specific question. Does the choice of dressed-metric vs hybrid affect our observables?

**Novelty potential:** HIGH (if formalism-dependent, that's testable quantum gravity)

**Observational leverage:** HIGH (directly impacts f_NL robustness)

**Effort:** MEDIUM (literature audit first, targeted calculation if needed)

**Sprawl risk:** LOW

**Quick kill:** If superhorizon modes (k/k_bounce ~ 10^{-56}) are trivially insensitive to formalism -> resolved.

**Success:** Formalism sensitivity found -> genuine LQC-specific result, paper material.

**Key papers:**
- arXiv:2405.12296 (2024 LQC perturbation comparison)
- Agullo, Ashtekar, Nelson (2012) -- dressed-metric
- Fernandez-Mendez, Mena Marugan, Olmedo (2012) -- hybrid
- Wilson-Ewing (2013) -- matter bounce in LQC

**Execution:** Literature extraction first. If no paper has compared bispectrum across formalisms, that gap is itself a finding. If papers exist, extract the comparison and assess whether the difference reaches observable k.

---

## #3: PBH + Induced GW Channel Feasibility

**Why #3:** Best candidate for second independent observable. Breaks single-point-of-failure.

**Novelty potential:** HIGH (second observable family, different experiments)

**Observational leverage:** HIGH (PTA/LISA/ET, not same surveys as f_NL)

**Effort:** MEDIUM (OOM estimate of bounce transition sharpness, then transfer function)

**Sprawl risk:** LOW (specific mechanism, bounded question)

**Quick kill:** If Wilson-Ewing bounce is too smooth (T(k) ~ 1 for all k) -> dead.

**Success:** Enhancement found -> PBH mass function + GW spectrum -> second discriminator.

**Key constraint:** The 2026 dust-radiation PBH calculation already showed vanishing fractions. Must determine whether the Wilson-Ewing LQC transition is physically different from that setup. If the bounce is adiabatic for all relevant k-modes, no enhancement occurs and the channel is dead.

**Target:** Asteroid-mass PBH (10^{17} - 10^{23} g) with induced GW spectrum in LISA/ET band.

---

## #4: Quasi-Dust Ekpyrotic LQC Literature Check

**Why #4:** "Have we exhausted viable models?" question. The 2025 paper (arXiv:2509.06148) claims viability.

**Novelty potential:** MEDIUM (model extension, not new observable)

**Observational leverage:** MEDIUM (could change n_s mechanism, might modify f_NL)

**Effort:** LOW (literature check, not original calculation)

**Sprawl risk:** MEDIUM (two-field models expand parameters)

**Quick kill:** If f_NL is very different from -35/8 -> competing model, not enrichment.

**Success:** Consistent f_NL + improved n_s mechanism -> more complete model.

**IMPORTANT CAVEAT:** This path was filtered in the viable model pass. Model C (ILS Ekpyrotic) failed the distinctiveness test because the bounce does zero predictive work -- all observables are set by the two-field sector. Only pursue this if the ekpyrotic version produces a DIFFERENT f_NL that is still bounce-controlled. If f_NL is slow-roll suppressed (as in standard single-field ekpyrosis where f_NL ~ O(epsilon)), there is no advantage over Wilson-Ewing, and Wilson-Ewing is simpler.

---

## #5: Scale-Dependent f_NL from LQC

**Why #5:** Natural extension of flagship observable. If f_NL(k) is scale-dependent, multi-tracer surveys could detect it.

**Novelty potential:** MEDIUM-HIGH (LQC-specific prediction beyond generic bounce)

**Observational leverage:** MEDIUM (requires next-gen multi-tracer techniques)

**Effort:** HIGH (new calculation of bounce-transfer for bispectrum as function of k)

**Sprawl risk:** LOW

**Quick kill:** If k_LQC is 56 orders above observable k -> no effect at any observable scale.

**Success:** Detectable running of f_NL -> enriches prediction package.

**Honest assessment:** Almost certainly dead on arrival. The LQC bounce scale is k_LQC ~ (rho_c)^{1/4} ~ 10^{18} GeV, while CMB scales are k ~ 10^{-4} Mpc^{-1} ~ 10^{-38} GeV. The ratio is 10^{56}. No plausible transfer function has structure over 56 orders of magnitude in k. But the quick kill is fast enough that it is worth confirming.

---

## #6: LQC Anomaly / Low-ell Program

**Why #6:** Already assessed as weak evidence. Only worth if LQC audit reveals specific testable prediction.

**Novelty potential:** LOW-MEDIUM

**Observational leverage:** LOW (2-3 sigma anomalies)

**Effort:** MEDIUM

**Quick kill:** If no specific quantitative prediction emerges -> deprioritize.

**Success:** Specific ell < 30 prediction -> modest but publishable.

**Current state of literature:** Agullo et al. (2021) is qualitative ("consistent with") rather than quantitative ("predicts amplitude X at ell Y"). Unless the LQC perturbation audit reveals a specific number, this path produces narratives, not predictions. Piggybacked on path #2, no standalone effort justified.

---

## #7: Third-Order LQC Bounce Transfer

**Why #7:** Important but technically very difficult. Lower priority because OOM estimate suggests superhorizon modes pass through trivially.

**Effort:** VERY HIGH

**Quick kill:** OOM estimate of bounce corrections to bispectrum transfer.

**The argument:** Observable modes have k/k_LQC ~ 10^{-56}. The bounce lasts approximately one Planck time. A mode that is 10^{56} times larger than the bounce scale experiences the bounce as an instantaneous event with unit transfer coefficient. The correction to f_NL from the bounce is of order (k/k_LQC)^2 ~ 10^{-112}, which is observationally zero.

**When to revisit:** Only after paths #1-#3 are resolved AND a third-order LQC perturbation framework exists in the literature. This is a publication-scale calculation (4-8 sessions minimum) and should not be attempted speculatively.

---

## Decision Protocol

**Strict stack ordering. Do not skip ahead.**

1. Is path #1 (f_NL verification) resolved? If no -> work on #1.
2. Is path #2 (formalism audit) resolved? If no -> work on #2.
3. Paths #1 and #2 resolved: is f_NL confirmed? If yes -> proceed to #3 (PBH channel). If no (f_NL killed or weakened to -35/16) -> reassess program architecture.
4. Only proceed to #4-#7 after #1-#3 are resolved or killed.

**Do not work on lower-ranked paths while higher-ranked paths remain open.**
