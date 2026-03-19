# Ranked Future Exploration Stack

**Created:** 2026-03-18
**Purpose:** Strict priority-ordered list of research paths worth pursuing, with exact entry questions and kill conditions.

---

## #1: LQC Perturbation-Formalism Audit (Dressed-Metric vs Hybrid for f_NL)

**Why #1:** Directly impacts the single remaining flagship prediction. If f_NL is formalism-sensitive, that is either a problem (weakens prediction) or an opportunity (LQC-specific observable). Either way, we need to know before claiming f_NL = -35/8 as a prediction of "the" LQC bounce.

**Exact question:** Does f_NL = -35/8 survive in both dressed-metric and hybrid formalisms?

**Quick kill:** If both formalisms agree at leading order for superhorizon modes -> resolved, move on. If the literature already shows they agree for the bispectrum -> resolved in days, not weeks.

**Success condition:** Formalism-dependent f_NL -> genuine LQC-specific prediction distinguishing quantum gravity quantization approaches. This would be a quantum-gravity-meets-observation result.

**Estimated effort:** 1-2 focused sessions (literature audit + targeted calculation).

**Risk if skipped:** We claim f_NL = -35/8 and a referee asks "in which formalism?" and we have no answer.

---

## #2: Complete Independent f_NL Gradient-Expansion Derivation

**Why #2:** The entire program rests on f_NL = -35/8 from a single paper (Cai et al. 2009). Li and Brandenberger get -2.19. We are at 75% confidence after the execution phase. Must reach >95%.

**Exact question:** What does the Salopek-Bond gradient expansion give for f_NL in matter contraction with w = 0?

**Quick kill:** If it gives -35/8 -> confirmed. If it gives -35/16 -> weakened but alive (4.4 sigma at MegaMapper instead of 8.75 sigma).

**Success condition:** Independent confirmation of -35/8 -> foundation crisis resolved. Confidence rises to >95%.

**Estimated effort:** 1-3 sessions. The calculation is a well-defined second-order perturbation theory problem in a power-law background. The growing mode complication is known and understood from our execution phase.

**Risk if skipped:** The program's flagship prediction rests on a single calculation that disagrees with at least one other group. No referee will accept this without independent verification.

---

## #3: PBH + Induced GW Channel Assessment

**Why #3:** Genuinely independent second observable family. If viable, breaks the single-point-of-failure architecture that makes the program fragile.

**Exact question:** Does the Wilson-Ewing LQC transition from matter contraction to expansion produce sufficient perturbation enhancement for asteroid-mass PBH production?

**Quick kill:** If the LQC transition is too smooth (adiabatic for all relevant k-modes) -> no enhancement -> channel dead. An order-of-magnitude estimate using the LQC transition timescale vs. the relevant k^-1 can test this in one session.

**Success condition:** PBH production at asteroid mass (10^17 - 10^23 g) with induced GW spectrum in the LISA/ET frequency band -> second discriminator independent of f_NL.

**Estimated effort:** 1 session for OOM estimate. If promising, 2-4 sessions for proper calculation.

**Risk if skipped:** We remain in single-point-of-failure mode indefinitely.

**Key reference to check first:** The 2026 dust-radiation PBH calculation already showed vanishing fractions. Need to understand whether Wilson-Ewing transition is different from that calculation.

---

## #4: Quasi-Dust Ekpyrotic LQC Viability Check

**Why #4:** Could provide a more complete model with better n_s mechanism AND a different f_NL. The 2025 paper (arXiv:2509.06148) claims viability for a two-field ekpyrotic LQC model.

**Exact question:** Does the two-field ekpyrotic LQC model produce both n_s approximately 0.965 AND f_NL approximately -4?

**Quick kill:** If f_NL in the ekpyrotic model is slow-roll suppressed (as in standard single-field ekpyrosis where f_NL ~ O(epsilon)) -> no advantage over Wilson-Ewing, and Wilson-Ewing is simpler.

**Success condition:** Joint n_s + f_NL prediction from a single LQC model that is DIFFERENT from the Wilson-Ewing prediction -> allows model comparison within LQC.

**Estimated effort:** 1-2 sessions (literature extraction + consistency check).

**Risk if skipped:** Low. Wilson-Ewing is already viable. This is an enrichment, not a necessity.

**IMPORTANT CAVEAT:** This path was filtered in the viable model pass 2. Model C (ILS Ekpyrotic) failed the distinctiveness test because the bounce does zero predictive work --- all observables are set by the two-field sector. Only pursue this if the ekpyrotic version produces a DIFFERENT f_NL that is still bounce-controlled.

---

## #5: Scale-Dependent f_NL from LQC

**Why #5:** Natural extension of the f_NL program. Could produce a testable prediction beyond the squeezed-limit amplitude.

**Exact question:** Is f_NL scale-dependent near the bounce scale? Does LQC introduce a characteristic k-dependence that shows up at observable scales?

**Quick kill:** If k_LQC (the LQC transition scale) is too far from observable k (it is, by roughly 56 orders of magnitude) -> no observable scale-dependence -> kill.

**Success condition:** Scale-dependent f_NL(k) testable by multi-tracer surveys (MegaMapper, SPHEREx) -> enriches the prediction package from a single number to a function.

**Estimated effort:** 1 session for the scale analysis. The LQC bounce scale is known; the question is whether the transfer function introduces k-dependence at observable k.

**Risk if skipped:** Low. The squeezed-limit f_NL is already the flagship. Scale dependence is a bonus.

**Honest assessment:** Almost certainly dead on arrival. The LQC bounce scale is k_LQC ~ (rho_c)^{1/4} ~ 10^{18} GeV, while CMB scales are k ~ 10^{-4} Mpc^{-1} ~ 10^{-38} GeV. The ratio is 10^{56}. No plausible transfer function has structure over 56 orders of magnitude in k. But the quick kill is fast enough that it is worth confirming.

---

## #6: LQC Anomaly / Low-ell Modulation

**Why #6:** Low priority but worth a quick check during the LQC perturbation audit (#1).

**Exact question:** Does our Wilson-Ewing model make any specific quantitative prediction at ell < 30?

**Quick kill:** If prediction is "qualitatively consistent" but not quantitative (no specific amplitude, no specific scale, no Bayesian comparison) -> deprioritize. This is the current state of the literature (Agullo et al. 2021 is qualitative).

**Success condition:** Specific, testable low-ell prediction (e.g., "power deficit at ell = 2-5 with amplitude X from LQC transition") -> connects to Planck anomaly with a number, not a narrative.

**Estimated effort:** Piggybacked on path #1. No standalone effort justified.

**Risk if skipped:** Negligible. The anomalies are 2-3 sigma and may be flukes.

---

## #7: Third-Order LQC Bounce Transfer for Bispectrum

**Why #7:** Important for completeness but technically very difficult. Needed eventually but not immediately.

**Exact question:** Does the LQC bounce modify the pre-bounce f_NL during transmission?

**Quick kill:** OOM estimate: if superhorizon modes have k/k_bounce ~ 10^{-56} -> transfer coefficient = 1 trivially. The bounce cannot modify modes that are 56 orders of magnitude larger than its own scale.

**Success condition:** Non-trivial bounce modification of f_NL -> genuinely LQC-specific effect. But this is almost certainly not the case (see quick kill).

**Estimated effort:** 1 session for the OOM. Full calculation (if OOM is non-trivial) would be 4-8 sessions and would require extending LQC perturbation theory to third order.

**Risk if skipped:** Low in the short term. The OOM argument (modes too far superhorizon) is robust. A full third-order calculation is a publication in itself and should only be attempted after paths #1 and #2 are resolved.

---

## Decision Protocol

When starting a new session, consult this stack:
1. Is path #1 resolved? If no, work on #1.
2. Is path #2 resolved? If no, work on #2.
3. Paths #1 and #2 resolved: assess whether f_NL program is confirmed. If yes, proceed to #3 for a second observable. If no (f_NL killed), reassess entire program.
4. Only proceed to #4-#7 after #1-#3 are resolved or killed.

Do not work on lower-ranked paths while higher-ranked paths remain open. The stack is strict.
