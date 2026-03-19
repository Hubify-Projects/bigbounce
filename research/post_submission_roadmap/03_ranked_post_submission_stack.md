# Ranked Post-Submission Research Stack

**Created:** 2026-03-19
**Purpose:** Priority-ordered research directions for the period after the focused PNG paper is submitted.

---

## #1: PBH + Induced GW Second Observable Channel

**Why #1:** Breaks the single-point-of-failure architecture. The entire focused paper rests on f_NL = -35/8 being detectable by SPHEREx/MegaMapper. If that measurement fails (wrong value, excluded by systematics, survey underperforms), we have nothing. A second observable family at completely different scales and experiments would make the science case resilient.

The independence is genuine: different k-range (10^5 - 10^15 Mpc^{-1} vs 0.01 Mpc^{-1}), different experiments (LISA/ET vs SPHEREx/MegaMapper), different generation mechanism (bounce transition dynamics vs pre-bounce contraction dynamics), different systematics. Correlation between failure modes is near zero.

**Success:** PBH mass function f_PBH(M) peaked in the asteroid-mass window (10^{17} - 10^{22} g) + induced GW spectrum Omega_GW(f) in the LISA/ET band. This would be a second paper of comparable impact: "Primordial Black Holes from the LQC Matter Bounce: Predictions for LISA and Einstein Telescope."

**Quick kill:** If the Wilson-Ewing LQC bounce is too smooth (Gaussian-like, symmetric, w ~ 0 on both sides), then T(k) ~ 1 for all k, no perturbation enhancement, channel dead. Determinable in 1 session via OOM estimate of the bounce sharpness parameter.

**First action:** Compute the effective equation of state w_eff(t) through the Wilson-Ewing LQC bounce using H^2 = (8piG/3) rho (1 - rho/rho_c). Determine the transition duration, sharpness, and asymmetry. Compare with Papanikolaou et al.'s enhancement criterion.

---

## #2: LQC Formalism Sensitivity Audit

**Why #2:** Directly addresses whether the flagship f_NL prediction has hidden theoretical uncertainty. The dressed-metric and hybrid LQC perturbation formalisms differ in how quantum geometry backreacts on perturbations. If this difference reaches the bispectrum, it is testable quantum gravity. If it does not, the prediction's robustness is formally established.

This is lower-priority than PBH because its most likely outcome is a null (both formalisms agree for k/k_LQC ~ 10^{-56}), whereas PBH has a 30-50% chance of a positive result. But it directly strengthens the submitted paper's claims, making it high-value for referee response.

**Success:** Formalism dependence found: genuine LQC-specific result, paper material. Or: independence confirmed: prediction robustness documented, strengthens the submitted paper.

**Quick kill:** If arXiv:2405.12296 already shows superhorizon power spectrum is formalism-independent, and bispectrum inherits this by dimensional analysis, resolved in hours.

**First action:** Read arXiv:2405.12296 carefully. Determine if their comparison extends to bispectrum or only power spectrum. If only power spectrum, assess whether their superhorizon-mode results imply bispectrum insensitivity.

---

## #3: Paper 1 Framework Paper Completion

**Why #3:** Already 75% written. Uses existing material. Publishes the ECH closure (14 barriers) + ALP birefringence prediction (beta = 0.27 degrees, matching 3.9-sigma detection) + MCMC verification (236K samples, Delta-N_eff ~ 0) that are sitting in the repo.

This is the lowest-risk path: the material exists, the draft is mostly done, and the paper has inherent value as a comprehensive assessment of what the ECH bounce can and cannot do. It also establishes the group's authority before the focused PNG paper appears.

**Success:** Published paper positioning the broader program. Provides context for the focused PNG paper. Citations to both papers reinforce each other.

**First action:** Review `research/final_phase/01_final_paper_structure.md` and `arxiv/main.tex`. Assess remaining gaps. Identify which sections need updating to reflect focused-path results (particularly the f_NL range shift from 5/12 to -35/8).

---

## #4: Companion Theory Paper (ECH -> LQC Narrative)

**Why #4:** Compilation exercise using existing verdicts. Lower novelty than the other paths but establishes the logical bridge: ECH provides the singularity resolution framework, LQC provides the perturbation predictions, and the Wilson-Ewing model is the unique viable implementation.

The systematic closure of 14 ECH perturbation routes has not been published anywhere. The community currently has no comprehensive map of which bounce-cosmology routes are closed. This paper would serve that function.

**First action:** Outline from `research/post_ech_positive_program/` + `research/bounce_evidence_audit/`. Draft structure: (1) ECH bounce mechanism, (2) 14-barrier closure, (3) pivot to LQC, (4) Wilson-Ewing viability, (5) f_NL as the observable bridge.

---

## #5: Scale-Dependent f_NL

**Why #5:** Only worth pursuing if #1 or #2 opens a door. The LQC-specific running is negligible (k_LQC/k_obs ~ 10^{56} produces corrections of order 10^{-112}). The contraction-dynamics running from epsilon = 0.003 produces delta(f_NL)/f_NL ~ 1.5% over the observable range, which is ~0.14 sigma at MegaMapper precision. Even with optimal multi-tracer, this reaches ~0.7 sigma. Not significant.

**First action:** OOM estimate confirming the above numbers. If confirmed: document as a known-but-undetectable LQC correction. If surprisingly large: escalate.

---

## Decision Protocol

**Strict stack ordering. Do not skip ahead.**

1. Is #1 (PBH channel) assessed? If no -> work on #1.
2. Is #2 (formalism audit) resolved? If no -> work on #2. (Can run in parallel with #1.)
3. Both resolved: what is the architecture?
   - PBH viable + formalism robust: two-observable paper. Strong program.
   - PBH dead + formalism robust: single-observable. Proceed to #3 (Paper 1 completion).
   - PBH dead + formalism sensitive: formalism paper. Reframe program.
4. Only proceed to #4-#5 after #1-#3 are resolved or killed.

**Do not work on lower-ranked paths while higher-ranked paths remain open.**
