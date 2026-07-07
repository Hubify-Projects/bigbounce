# P4 — Grok (Expert) — FINAL ROUND
- paper: P4 (galaxy chirality catalog)
- version: v1.0.217
- model: Grok Expert (grok.com)
- timestamp: 2026-07-07T02:02:19Z
- chat_url: https://grok.com/c/b664954a-0b34-4acc-ad7a-76821e156b60?rid=dc367b72-da15-4650-9c22-cc21d8319032

## RAW VERBATIM RESPONSE

VERDICT: MINOR REVISIONS

ISSUES:

[MINOR] Section II.B / Training Labels & VI.A: 66.5% of the 25,790 training labels are CE-ResNet pseudo-labels; the decisive GZ1-human-only dipole cross-check (z = −0.54σ) uses only N ≈ 46k confident spirals (∼21× smaller than the primary HC sample). While the eight-anchor battery and |A_inh| ≲ 1.5% ceiling bound inherited power, the limited statistical power of the fully independent test should be stated more prominently as a caveat on the “largest catalog” claim and on the shuffle-null limitation.
[MINOR] Section IV.D / Monopole+Mask Leakage & forward modeling: The imaging + real-DR8-morphology templates reproduce only ∼53% of the observed |a₁| residual amplitude (cos θ ≈ +0.84). The paper correctly bounds the unmodeled remainder below A₉₅ and notes it is an open item requiring a full per-galaxy confidence-vs-depth map, but this should be elevated to an explicit numbered limitation with a concrete computational path (GPU/pod scale) rather than left as a parenthetical.
[MINOR] Section III.B & IV.C / Declared hierarchy & pre-registration: The peq > 0.6 cut and primary/secondary estimator ordering are declared and the commit hash (94113e5) is cited, but for a journal submission the analysis hierarchy and cut should be presented in a standalone, version-controlled supplementary note or Zenodo deposit rather than relying solely on a git commit that may not be independently browsable by referees.
[MINOR] Section IV.C & Table VIII / Injection-recovery floor: The A₅₀ ≈ 0.75% and A₉₅ ∈ (1.0%, 1.5%] thresholds are correctly reported as estimator- and subsample-specific (HC-broad, peq > 0.6). The text should explicitly caution readers that these floors are not directly interchangeable with the harmonic-channel completeness (Table IX) and that any future claim using a different cut or estimator must recompute its own injection-recovery curve.
[MINOR] Throughout / Notation of significance: Multiple distinct null procedures yield numerically incomparable σ/z values (pixel-permutation moment-z, label-shuffle, block-bootstrap, max-statistic MC). Although the paper repeatedly warns against cross-comparison and supplies Table I as the decision tree, the abstract and opening paragraphs still lead with “+0.41σ” and “+3.64σ / +7.28σ” in a way that invites misreading; the abstract should state the two primary estimators and their specific nulls in one sentence.

The central claim of a null real-space chirality dipole (consistent with zero at +0.41σ, p = 0.31 on the pre-specified HC subsample) together with the exclusion of a clean 1.7% dipole (z ≈ −18) is supported by the real-space estimator, multiple independent null constructions, and empirical injection-recovery calibration.
