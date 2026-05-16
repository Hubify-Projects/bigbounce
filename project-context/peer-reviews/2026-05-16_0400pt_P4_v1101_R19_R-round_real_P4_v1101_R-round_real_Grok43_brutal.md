# P4_v1101 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0400pt_P4_v1101_R19_R-round_real
**Wall time**: 23.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=74993, completion=2115, reasoning=1253, total=77108

---

**PAPER-GRO-B1: Parity framing mismatch**

**Classification:** BLOCKER

**Location:** Title + abstract (first paragraph)

**Issue:** Title and lead sentence claim "No Evidence for Large-Scale Parity Violation," but the text explicitly states the ℓ=1 dipole is parity-even (isotropy test only) while the parity-odd monopole is separately attributed to label bias. This is not a minor semantic slip; it misaligns the central claim with the actual observable tested.

**Fix:** Retitle to "No Evidence for Large-Scale Isotropy Violation in Galaxy Morphology: ..." and move the parity-even caveat to the first sentence of the abstract.

**PAPER-GRO-B2: Sensitivity claim inflation**

**Classification:** MAJOR

**Location:** Abstract + §IX.J + Table I

**Issue:** Headline "sub-percent sensitivity" and "50%-recovery 3σ threshold A≈0.75%" are presented as the experiment's reach, yet the 0.75% figure is measured only on the HC subsample (N=471k); the full-catalog Fisher floor (0.29%) is never empirically validated via injection on the 3.2M sample. The 0.75% vs. 0.29% gap is treated as non-problematic cross-sample comparison rather than an unclosed systematic-inclusive bound.

**Fix:** State the operational sensitivity as "≥0.75% (HC subsample only; full-catalog empirical bound deferred)" and remove "sub-percent" from the abstract title.

**PAPER-GRO-B3: Dodged direct comparison**

**Classification:** MAJOR

**Location:** Abstract + §X.A + §XII (multiple instances)

**Issue:** The paper repeatedly states that Shamir's ~2–4% signal "differs by a factor of ~6–12" and that the leakage channel "explains" prior detections, while explicitly declining to run the matched-footprint Ganalyzer reanalysis required for a formal exclusion. This framing allows an amplitude-based dismissal without performing the test that would make the claim load-bearing.

**Fix:** Either perform the Ganalyzer-matched reanalysis on the DESI Legacy footprint or rephrase all comparative claims as "inconsistent under the present ViT-Small pipeline; a like-for-like test is required for exclusion."

**PAPER-GRO-B4: Monopole significance downplayed**

**Classification:** MAJOR

**Location:** §V.B + Table II + §IX

**Issue:** The 9.5σ global monopole offset (0.26% deficit) is called a "documented systematic-floor artifact" and "not interpreted cosmologically," yet it survives equivariant TTA, is uniform across slabs, and is never shown to have strictly zero dipole projection. The 0.43σ real-space dipole null is then treated as independent of this residual.

**Fix:** Either demonstrate (via PSF/scan-angle cross-power or full D4-TTA) that the monopole has no dipole leakage at the 0.29% level, or qualify the dipole null as conditional on the unverified zero-projection assumption.

**PAPER-GRO-B5: Narrative self-justification density**

**Classification:** minor

**Location:** Throughout (esp. §II, §IV, §IX, footnotes)

**Issue:** Excessive round-note language, "load-bearing," "closure," and repeated disclaimers about what was not done create the impression of a document written to survive review rather than to state the result cleanly. This does not invalidate the data but reduces readability and signals over-engineering.

**Fix:** Remove all v1.0.xx round references, collapse the pre/post-MASTER and mask-variant discussion into one concise paragraph in §IX, and move usage limitations to a single boxed paragraph in §XII.

**PAPER-GRO-B6: No remaining blocker-grade issues on core null**

**Classification:** (none)

**Location:** N/A

**Issue:** After the above, the post-MASTER ℓ=1 null on the subsample mask, the real-space dipole, and the injection-recovery results are internally consistent and correctly null. No additional convergent BLOCKERs were identified in the propagation tail. The paper is ready for Houston external review once the five items above are addressed.
