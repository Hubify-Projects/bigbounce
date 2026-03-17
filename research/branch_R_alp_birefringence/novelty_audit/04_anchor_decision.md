# Paper-Anchor Decision

**Date:** 2026-03-17

---

## Decision: CAN_BE_INCLUDED_BUT_NOT_MAIN_ANCHOR

---

## Reasoning

### Why NOT "STRONG_ENOUGH_TO_ANCHOR":

1. **The core ALP birefringence result is not new.** Fujita+ 2021 already showed that a Planck-scale spectator ALP fits the birefringence data with MCMC. Our version uses a slightly different parametrization (θ_i, m instead of g, m) and a simpler likelihood, but arrives at the same physical conclusion.

2. **Our data analysis is the weakest in the literature.** We use a single Gaussian summary statistic (β_obs ± σ). Namikawa+ 2025 uses the full Planck EB power spectrum with multi-frequency foreground marginalization. We cannot claim our MCMC adds new constraints.

3. **The naturalness argument is not unique.** Multiple papers claim their ALP models naturally explain β ~ 0.3° (Nakagawa+ 2025 with c_γ ~ O(1), Lin & Yanagida 2023 with f_a ~ 10^{16} GeV). "Natural parameters → β ~ 0.3°" is a feature of the entire ALP-birefringence model class, not specific to our parametrization.

4. **A paper anchored on "we fit β with an ALP" in 2026 would be incremental.** The field has moved beyond simple fitting to EB spectrum shape analysis, anisotropic birefringence tomography, and joint EDE+birefringence constraints. Our work would look dated.

### Why NOT "TOO_CLOSE_TO_PRIOR_WORK":

1. **The closure assessment IS novel.** No paper systematically investigates 15 routes through ECH cosmology and identifies 13 structural barriers. This is substantial original theoretical work.

2. **The "sole survivor" framing IS novel.** Presenting ALP birefringence not as "here's another model" but as "the last prediction standing after exhaustive testing" is a genuinely different and more compelling narrative.

3. **The ALP ≡ free-β demonstration IS novel in execution.** While expected, no paper runs the explicit 3-model comparison. This is the honest conclusion the field needs.

4. **The ECH → ALP → birefringence chain IS a new connection.** The torsion-axion literature (Castillo-Felisola+ 2015) and the ALP-birefringence literature have not been bridged before.

### Why "CAN_BE_INCLUDED_BUT_NOT_MAIN_ANCHOR":

The ALP birefringence result is a legitimate, well-executed piece of the paper that adds value. But the paper's primary novelty lies in:

1. **The theoretical framework assessment** (bounce, closure, 13 barriers)
2. **The systematic elimination methodology** (15 branches tested)
3. **The honest conclusion** (framework viable but observationally inert except for one handle)

The ALP is the *payoff* of this investigation, not its *foundation*. The paper should be anchored on the closure assessment, with the ALP as the reward for doing the hard theoretical work.

---

## Recommended Paper Structure (Revised)

**OLD anchor:** "Here's a Planck-scale spectator ALP that fits cosmic birefringence."
→ Incremental. Fujita+ 2021 already did this.

**NEW anchor:** "We comprehensively assess ECH bounce cosmology. Thirteen barriers close all routes to DE and distinctive signatures. One testable prediction survives: birefringence via a Planck-scale ALP. We present MCMC constraints and demonstrate it is statistically equivalent to free β but physically richer."
→ Novel framing. The closure IS the contribution; the ALP is the surviving handle.

### Implications for section balance:

| Section | Old weight | New weight |
|---------|-----------|------------|
| Theory (bounce) | Supporting | Co-anchor |
| Closure assessment | Supporting | **Primary anchor** |
| ALP prediction | Primary anchor | **Payoff** |
| MCMC results | Primary anchor | Supporting evidence |
| Discussion | Summary | Synthesis of closure + ALP |

The paper should be titled something closer to:
- "Comprehensive Assessment of Einstein-Cartan-Holst Cosmology: Thirteen Structural Barriers and One Surviving Prediction"

rather than:
- "Cosmic Birefringence from a Planck-Scale ALP in Spin-Torsion Cosmology"

The first title signals that the main contribution is the assessment; the ALP is the bonus. The second title competes directly with Fujita+ 2021 and Nakagawa+ 2025 on territory where we are weaker.

---

## What Role Should the ALP Play?

**Not appendix.** The ALP result is real, well-executed, and provides a concrete positive conclusion. Demoting it to an appendix would waste good work.

**Not the main anchor.** For reasons above.

**A substantial section (3–4 pages) as the culmination of the paper.** The structure should be:
1. Set up the framework (ECH bounce)
2. Show everything that doesn't work (closure, 13 barriers)
3. Show the one thing that does work (ALP birefringence)
4. Demonstrate it honestly (ALP = free β, but physically richer)
5. Forecast its future (LiteBIRD decisive)

This makes the ALP section the climax of a narrative arc, not the standalone contribution. The narrative — "comprehensive assessment → systematic elimination → one survivor → testable" — is the actual novelty.
