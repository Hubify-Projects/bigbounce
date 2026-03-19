# Final Verdict: Remaining Live Paths Audit

**Created:** 2026-03-18
**Status:** COMPLETE

---

## 1. What important paths remain genuinely untested?

**Three high-value paths are genuinely untested in our program:**

1. **LQC perturbation-formalism sensitivity for f_NL.** No paper has checked whether the dressed-metric and hybrid formalisms give the same bispectrum for modes at k << k_LQC. Our flagship prediction assumes formalism independence. This assumption has not been verified.

2. **PBH + induced GW channel in the Wilson-Ewing matter bounce transition.** The LQC bounce transition could enhance perturbations at short scales, producing asteroid-mass PBHs and an induced GW spectrum in the LISA/ET band. The 2026 dust-radiation calculation showed vanishing fractions, but the Wilson-Ewing transition may differ. Not assessed.

3. **Quasi-dust ekpyrotic two-field LQC as an alternative viable model.** The 2025 paper (arXiv:2509.06148) claims viability. Whether it produces a DIFFERENT and still bounce-controlled f_NL has not been checked.

**Two medium-value paths are under-tested:**

4. **Scale-dependent f_NL from LQC-specific structure.** Almost certainly dead (k_LQC/k_obs ~ 10^56), but the quick kill has not been formally executed.

5. **Third-order perturbation transfer through LQC bounce.** Expected to be trivial (transfer coefficient = 1 for k << k_LQC), but not formally confirmed.

---

## 2. Which are worth pursuing?

**Paths #1-#3 are clearly worth pursuing.** They have high observational leverage, bounded effort, and low sprawl risk.

| Path | Observational leverage | Effort | Sprawl risk |
|------|----------------------|--------|-------------|
| #1 Formalism audit | HIGH (directly impacts flagship) | LOW (1-2 sessions) | NONE |
| #2 Independent f_NL derivation | HIGH (confirms or kills flagship) | MEDIUM (1-3 sessions) | NONE |
| #3 PBH + induced GW | HIGH (second observable family) | MEDIUM (1-4 sessions) | LOW |
| #4 Scale-dependent f_NL | LOW (likely dead) | LOW (1 session) | NONE |
| #5 Third-order transfer | LOW (likely trivial) | HIGH if non-trivial | LOW |

Paths #4-#5 are worth pursuing as quick-kill checks during the LQC audit but not as standalone programs.

---

## 3. Which should be deprioritized?

**Firmly deprioritize (see file 04 for detailed reasoning):**

| Path | Reason | Time cost if pursued |
|------|--------|---------------------|
| ECH perturbation loops | Structural closure (14 barriers). Dead. | 2-4 months wasted |
| Teleparallel / f(T) / f(Q) bounce builders | Sprawl without discriminators | 6+ months, no prediction |
| GFT condensate cosmology | Too far from observation | Multi-year, qualitative only |
| Non-minimal ECH with fermions | Planck-suppressed, different theory | 1-2 months, same wall |
| CMB anomaly programs (without sharp predictions) | Evidence too weak, fits qualitative | 2-3 months, no number |
| Hybrid DE splice | Exhaustively rejected (7 forms) | Any time is wasted |
| More MCMC without new theory hooks | Reconfirms Delta-N_eff = 0 | Weeks of chains, no information |

The common failure mode: generating activity without advancing the discriminator.

---

## 4. What is the single best next remaining research path?

**LQC Perturbation-Formalism Audit.**

It directly impacts the flagship prediction, has bounded effort (1-2 sessions), every outcome is informative, and it feeds directly into the paper. No other path combines all four properties.

The decision tree after this path:
- Formalisms agree -> move to path #2 (independent derivation)
- Formalisms disagree -> major finding, write it up as the paper's strongest LQC-specific result
- Literature resolves it -> free confidence boost, move to path #2 immediately

---

## 5. What exact next calculation or audit should be done immediately?

**Read arXiv:2405.12296 (2024 LQC perturbation comparison) and determine whether dressed-metric vs hybrid formalisms have been compared for the bispectrum.**

- If they HAVE been compared: extract the answer and document it. Check whether the comparison applies at k << k_LQC (our regime).
- If they have NOT been compared: confirm this is a genuine gap. This gap itself is informative --- it means our formalism-sensitivity question is novel and worth answering.

**Then:**

Check whether ANY paper has computed f_NL through an LQC bounce in BOTH formalisms. If yes, extract the comparison. If no, that calculation is the target.

This takes hours, not weeks. It either confirms the prediction's robustness (confidence rises to ~90%+) or reveals a genuine LQC-specific observable (formalism-dependent f_NL). Either way, it advances the science case.

---

## Program Status After This Audit

| Component | Status | Confidence |
|-----------|--------|-----------|
| ECH bounce -> DE | CLOSED (14 barriers) | 100% |
| ECH perturbation signatures | CLOSED (perturbation transparency) | 100% |
| ALP birefringence | ALIVE but bounce-independent | N/A |
| Wilson-Ewing model viability | ALIVE | 85% |
| f_NL = -35/8 correctness | ALIVE, needs verification | 75% |
| f_NL formalism robustness | UNTESTED | Unknown |
| PBH + induced GW channel | UNTESTED | Unknown |
| Tensor sector (r, n_T) | SILENCED by LQC suppression | N/A |
| DE splice | DEAD (7 forms rejected) | 100% |
| MCMC infrastructure | IDLE (no new theory to test) | N/A |

**Bottom line:** The program has exactly one live prediction (f_NL = -35/8) resting on two unverified assumptions (Cai et al. calculation is correct; formalism choice does not matter). Both can be resolved with bounded effort. Resolve them. Then assess whether a second observable (PBH/GW) exists. Everything else is noise.
