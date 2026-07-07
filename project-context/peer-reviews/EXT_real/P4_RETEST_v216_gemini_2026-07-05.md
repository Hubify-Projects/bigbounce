# P4 RETEST — v1.0.216 — Gemini EXT (VERIFIABLE)

- **Reviewer:** Gemini (houston@bamf.com Ultra, /u/1, Gemini Pro)
- **Date:** 2026-07-05
- **Paper:** P4 (Galaxy Chirality and Environment) v1.0.216
- **PDF:** /tmp/retest_P4_v216.pdf (983360 bytes)
- **Chat (fresh):** https://gemini.google.com/u/1/app/b1fe7d4f3dbaa6d8
- **Screenshot:** P4_RETEST_v216_gemini_2026-07-05.png
- **Prompt:** PRD referee, exact (1)VERDICT / (2)ISSUES [MAJOR]/[MINOR] / (3) central-claim sentence
- **VERDICT (verbatim from "(1) VERDICT:" line):** MINOR REVISIONS

## Raw verbatim response

VERDICT: MINOR REVISIONS

ISSUES:

[MAJOR] Unmodelled l=1 Residual (Section IV D): The forward model using imaging and morphology templates successfully captures only 52-54% of the observed l=1 harmonic residual. Leaving approximately 47% of this systematic anomaly explicitly unmodelled is a notable loose end. While the manuscript correctly demonstrates that even if this entire remainder were a cosmological dipole, it would fall below the real-space 50%-recovery floor (A_50 ≈ 0.75%), the author attributes the remainder to a deferred, compute-heavy confidence-vs-depth response map. The manuscript would be strengthened by either running this deferred analysis to close the budget or providing a tighter theoretical bound on why the specific morphology-correlated selection effect cannot mimic a primordial dipole.

[MAJOR] Edge-On Galaxy Contamination and Tie-Breaks (Appendix E): The empirical measurement that 15.8% of the classified spiral sample consists of edge-on galaxies is treated purely as a sensitivity dilution factor due to the flip-equivariant Test-Time Averaging (TTA). However, the manuscript notes that the hard-argmax tie-break on borderline probabilities (p_CW^eq ≈ p_CCW^eq ≈ 0.4) flips in 21.4% of cases under extended D_4 validation. While the author isolates this coherence to the DECALS footprint, the non-linear propagation of argmax decisions near the decision boundary requires a more robust mathematical defense to ensure it cannot introduce an insidious directional bias at sub-percent levels.

[MINOR] Classifier Overconfidence (Section IV A): The ViT model is highly miscalibrated, exhibiting a mean catalog confidence of 0.951 despite a true cross-matched three-class accuracy of only 58.7% against Galaxy Zoo 1 labels. The author adequately defends the p_eq > 0.6 cut as a monotone ranking threshold rather than a probabilistic certainty. However, the lack of probabilistic calibration (e.g., Platt scaling) prior to the hard cut makes the threshold highly specific to this exact model state, slightly hindering generalized reproducibility on future survey pipelines.

[MINOR] Prose Density and Nested Parentheticals: Throughout the manuscript, critical scientific arguments are obscured by extremely long sentences containing multiple nested parentheticals and numerical lists (e.g., Sections I, III B, and IV C). Removing parenthetical detours and breaking these into distinct sentences or footnotes will significantly improve readability for the PRD audience without sacrificing rigor.

CONCLUSION:
The central claim of a null real-space cosmological chirality dipole is robustly supported by the extensive, bias-hardened equivariant pipeline and rigorous systematics controls, successfully demonstrating that prior sub-percent detections were likely artifacts of monopole-mask leakage and imaging systematics.

## Orchestrator note

Gemini moved to **MINOR REVISIONS** (from its prior 2-MAJOR stance). Its two [MAJOR]-labeled items are now framed as "notable loose end" / "would be strengthened by" strengthening requests that EXPLICITLY acknowledge the v216 residual-exclusion computation (A_50 ≈ 0.75% floor, dipole excluded) and the tie-break DECALS-isolation test are present in the paper — i.e. the prior majors were LIFTED to acknowledgment-plus-polish. Central claim "robustly supported." No NEW majors surfaced. Under the recalibrated gate this reads as an effective MINOR-tier ACCEPT-track verdict.
