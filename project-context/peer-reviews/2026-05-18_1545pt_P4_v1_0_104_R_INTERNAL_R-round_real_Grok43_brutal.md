# P4_v1_0_104_R_INTERNAL R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1545pt
**Wall time**: 38.0s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=77530, completion=3069, reasoning=2167, total=80599

---

**PAPER-GRO-B1**  
**Section: Abstract (multiple sites) + Conclusions**  
**BLOCKER**  
The paper asserts a headline "no-dipole" verdict while the canonical-mask post-MASTER direct-MC yields +1.85σ, which explicitly fails the released JSON's own |σ|<1 null criterion. The text labels this an "unresolved sub-detection-threshold systematic" and retains the subsample-mask −0.12σ as load-bearing, but never reconciles the internal inconsistency or runs the injection sweep on the canonical mask.  

**Fix:** Either (a) drop the |σ|<1 criterion and state the null is mask-dependent, or (b) perform the full injection-recovery on the canonical mask and report the resulting amplitude threshold.

**PAPER-GRO-B2**  
**Section: Abstract + §IX (Comparison with Previous Work)**  
**MAJOR**  
The paper claims Shamir's ~2–4% asymmetry is "inconsistent in amplitude... by a factor of ~6–12" under the present pipeline, yet repeatedly caveats that a matched-footprint reanalysis with Shamir's exact Ganalyzer + magnitude/redshift cuts "is not performed here." The amplitude comparison is therefore cross-pipeline and cross-selection, not a direct test.  

**Fix:** Remove the quantitative "factor of ~6–12" inconsistency claim or qualify it as "under our classifier and footprint only; a matched reanalysis is required for any formal exclusion."

**PAPER-GRO-B3**  
**Section: Abstract + §IX.J (Sensitivity Floor)**  
**MAJOR**  
The empirical 50%-recovery-at-3σ threshold is quoted as |A_dipole| ≈ 0.75% on the HC subsample (N=471k), while the ideal-statistical Fisher floor on the full 3.2M catalog is ~0.29%. The text notes the full-catalog injection sweep is "deferred to future work" and retracts the prior ~2.5× cross-sample ratio as invalid, yet still presents 0.75% as the operational sensitivity without a like-for-like full-catalog empirical bound.  

**Fix:** Either run the injection sweep on the full Catalog C or explicitly state that the quoted 0.75% threshold applies only to the HC subsample and that the full-catalog systematic-inclusive floor remains unmeasured.

**PAPER-GRO-B4**  
**Section: Abstract + §IV (Monopole+Mask Leakage) + Conclusions**  
**MAJOR**  
The central novel claim (a quantifiable monopole-mask leakage channel reproducing 99.3% of pre-MASTER C_1) is load-bearing, but the paper simultaneously asserts the ℓ=1 dipole is "fully consistent with null" while the low-ℓ bandpowers remain +2–6σ post-MASTER and are attributed to the same leakage. The text does not demonstrate that the leakage channel is fully removed at all scales relevant to the isotropy-breaking observable.  

**Fix:** Either show that the residual low-ℓ power after MASTER is consistent with the monopole-only null at the same significance as the ℓ=1 mode, or retract the claim that the leakage is fully characterized and removed.

**PAPER-GRO-B5**  
**Section: Throughout (multiple P4-EXT notes)**  
**minor**  
Multiple internal review-closure artifacts remain in the published text ("P4-EXT ChatGPT-B3", "P4-EXT 3-vendor convergent MAJOR closure", "P4-EXT-Gemini-B2 closure", etc.). These are meta-commentary on prior review rounds, not scientific content.  

**Fix:** Delete all such meta notes before submission; they belong in a review-response document, not the paper.

**PAPER-GRO-B6**  
**Section: Title + Abstract opening**  
**nit**  
The title and abstract lead with the leakage-channel demonstration, yet the headline scientific claim is still framed as a new null result on parity violation. Prior nulls (Iye et al. 2021, Tadaki et al. 2020) already exist; the incremental contribution is sample size + explicit leakage diagnostic, not a first detection of absence.  

**Fix:** Shorten the title to emphasize the leakage channel and reframe the abstract's null claim as "extends prior null results with explicit pre/post-MASTER leakage quantification."
