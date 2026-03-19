# Live Open Paths: Canonical Post-Submission List

**Created:** 2026-03-19
**Purpose:** The definitive list of genuinely open research paths after the focused PNG paper is submitted.

---

## Path 1: PBH + Induced GW Second Observable Channel

**Exact question:** Does the Wilson-Ewing LQC bounce transition produce small-scale perturbation enhancement sufficient for asteroid-mass PBH production and an induced GW background?

**Why still open:** Nobody has computed the bounce transfer function T(k) at k ~ k_bounce for the Wilson-Ewing model. Papanikolaou et al. (2024, arXiv:2404.03779) propose the mechanism for a generic bounce but have not applied it to LQC specifically. The 2026 dust-radiation PBH calculation showed vanishing fractions, but the Wilson-Ewing LQC effective equations may produce a qualitatively different transition.

**Closeness to live case:** VERY CLOSE -- same bounce model, different k-range. The Wilson-Ewing model is already the unique surviving viable model (0 extra fields, 1 fitted parameter). This path asks what it predicts at small scales, not whether it exists.

**Novelty potential:** HIGH -- genuinely independent second observable. PBH mass function + induced GW spectrum in the LISA/ET band. No existing paper computes this for the Wilson-Ewing LQC model specifically.

**Observational leverage:** HIGH -- completely different experiments from SPHEREx/MegaMapper. PTA (NANOGrav, EPTA), LISA (mHz), Einstein Telescope (Hz-kHz). Different k-range (k ~ 10^5 - 10^15 Mpc^{-1} vs k ~ 0.01 Mpc^{-1}). Different systematics. Failure modes are uncorrelated with the f_NL channel.

**Effort:** MEDIUM -- OOM estimate first (1 session: compute w_eff(t) through the bounce, determine sharpness parameter). Full calculation if viable (1-2 weeks: solve Mukhanov-Sasaki equation numerically, compute PBH mass function, compute induced GW spectrum).

**Kill criterion:** If the Wilson-Ewing bounce is smooth enough that T(k) ~ 1 for all k, there is no perturbation enhancement and the channel is dead. The LQC bounce is Gaussian-like (symmetric, smooth), and the Wilson-Ewing model returns to matter domination on both sides (w ~ 0 -> w -> -infinity -> w ~ 0). If this symmetry kills the parametric resonance that Papanikolaou et al. rely on, the channel closes in one session.

**Estimated viability probability:** 30-50%.

---

## Path 2: LQC Formalism Sensitivity for Bispectrum

**Exact question:** Does the choice of dressed-metric vs hybrid LQC perturbation formalism affect the transmitted f_NL?

**Why still open:** Nobody has compared bispectrum transfer across formalisms. Power spectrum comparisons exist (arXiv:2405.12296, Agullo-Ashtekar-Nelson 2012 vs Fernandez-Mendez-Mena-Marugan-Olmedo 2012) but bispectrum is untouched. The dressed-metric and hybrid approaches differ in how the quantum geometry backreacts on perturbations. For superhorizon modes at k/k_bounce ~ 10^{-56}, both should reduce to classical GR -- but this has not been proven for third-order perturbation theory.

**Closeness:** VERY CLOSE -- directly about the flagship observable f_NL = -35/8.

**Novelty potential:** MEDIUM-HIGH. If formalism-dependent: this is testable quantum gravity (different formulations of LQC give different predictions for a measurable quantity). If formalism-insensitive: the prediction's robustness is formally established, strengthening the paper's claims.

**Observational leverage:** HIGH if sensitive (observable depends on choice of quantum gravity formulation), ZERO if insensitive (but the null result has publication value as a robustness theorem).

**Effort:** MEDIUM -- literature audit first (days). Read arXiv:2405.12296 carefully. Determine if any paper computes f_NL through an LQC bounce in BOTH formalisms. If no paper exists, assess the feasibility of doing the calculation (weeks).

**Kill criterion:** If superhorizon modes at k/k_bounce ~ 10^{-56} are trivially insensitive to the formalism at the power spectrum level (which arXiv:2405.12296 may already show), and the bispectrum inherits this insensitivity by dimensional analysis, then the question is resolved without new calculation. Could be done in hours.

**Estimated viability probability:** 15-25% that a non-trivial formalism dependence exists for observable modes.

---

## Path 3: Scale-Dependent f_NL from LQC

**Exact question:** Does the LQC bounce introduce k-dependence into f_NL near the bounce scale, and does this running extend to observable scales?

**Why still open:** Would be an LQC-specific prediction beyond the generic -35/8. The contraction-dynamics running (from epsilon = 0.003 not being exactly zero) produces delta(f_NL)/f_NL ~ epsilon * ln(k/k_*) ~ 1.5% over the observable range. At MegaMapper precision this is ~0.14 sigma -- not significant, but multi-tracer techniques could push detection to ~0.7 sigma.

**Closeness:** CLOSE -- extends the flagship. Same observable (bispectrum), same surveys, different aspect (running vs amplitude).

**Novelty potential:** MEDIUM -- if detectable, enriches the prediction package. But the LQC-specific running is negligible (10^{-112}). Only the contraction-dynamics running has any hope.

**Effort:** HIGH -- requires new calculation of bounce-transfer for bispectrum as function of k, unless the quick kill resolves it.

**Kill criterion:** If k_LQC >> observable k by 56 orders of magnitude, the LQC-specific running is identically zero to any measurable precision. The contraction-dynamics running is real but likely undetectable. Quick kill via OOM estimate.

**Estimated viability probability:** 5% for detection at any planned survey.

---

## Path 4: Companion Theory Paper (ECH -> LQC Transition Narrative)

**Exact question:** Can we write a clean paper positioning ECH as a singularity-resolution proof framework while LQC provides the perturbation predictions?

**Why still open:** The repo has all the material: ECH perturbation transparency theorem (14 barriers), LQC viable model filtering (Wilson-Ewing unique survivor), f_NL = -35/8 as the observable bridge. No paper exists that maps this transition systematically.

**Closeness:** Direct -- uses existing results from `research/ech_bispectrum_gate/`, `research/ech_tensor_gate/`, `research/project_viable_bounce_model_pass2/`, `research/bounce_evidence_audit/`.

**Novelty potential:** MEDIUM -- framing and synthesis, not new physics. But the systematic closure of 14 ECH routes has not been published anywhere. The community could benefit from knowing which routes are dead.

**Effort:** LOW-MEDIUM -- compilation from existing verdicts. 2-3 sessions for a full draft.

**Kill criterion:** N/A (always publishable if written well). The only risk is low citation impact.

---

## Path 5: Paper 1 Framework Paper Completion

**Exact question:** Can we complete the original framework paper (ECH + 14 barriers + ALP birefringence + MCMC verification)?

**Why still open:** Already approximately 75% ready. The paper structure exists at `research/final_phase/01_final_paper_structure.md`. The ALP birefringence prediction (beta = 0.27 degrees matching 3.9-sigma detection), the 14-barrier closure, and the MCMC verification (236,000+ samples, Delta-N_eff ~ 0) are all documented. Version v1.6.0 of the manuscript has 31 pages and 51 bibliography entries.

**Closeness:** Direct -- uses existing material in `arxiv/main.tex`.

**Effort:** MEDIUM -- review current draft state, identify gaps, fill remaining sections, update to reflect focused-path results. 3-5 sessions for completion.

**Kill criterion:** N/A (publishable as a comprehensive assessment paper).

---

## Paths Considered and Rejected

| Path | Why Rejected |
|------|-------------|
| ECH perturbation novelty | Permanently closed. 14+ barriers. Mathematical proof. |
| Teleparallel / f(T) / f(Q) | Sprawl without discriminators. |
| GFT condensate cosmology | Too far from observation. Years from predictions. |
| Non-minimal ECH with fermions | Planck-suppressed. Different theory after elimination. |
| More MCMC without theory hooks | Reconfirms Delta-N_eff = 0. No new information. |
| Hybrid DE splice (any form) | 7 forms exhaustively rejected. |
| Galaxy spin dipole | 9-12 OOM coupling gap. Effectively falsified. |
| CMB anomalies without sharp predictions | 2-3 sigma, qualitative fits, a posteriori statistics. |
| Chiral GW from ECH | Frequency gate failed (f ~ 10^{9-10} GHz). Five closures. |
| Third-order LQC bounce transfer | VERY HIGH effort, likely trivial result (T ~ 1 for k << k_LQC). |
