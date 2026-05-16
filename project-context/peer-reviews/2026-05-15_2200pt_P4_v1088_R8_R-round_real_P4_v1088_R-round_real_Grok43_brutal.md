# P4_v1088 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2200pt_P4_v1088_R8_R-round_real
**Wall time**: 31.4s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=71193, completion=2893, reasoning=2058, total=74086

---

**PAPER-GRO-B1 (BLOCKER)**  
**Section:** Abstract (paragraph 1, ~lines 40-60) and Sec. 1 (Introduction, Shamir comparison)  
**Issue:** The text states the result "strongly disfavors Shamir's (2020, 2022) claimed ~3% asymmetry signal... by a factor of ~6--12 in amplitude" while explicitly noting that no matched-footprint reanalysis under Shamir's Ganalyzer pipeline was performed. This is an amplitude comparison under mismatched classifier/selection/footprint conditions, not a statistical exclusion. The phrasing is written to imply stronger exclusion than the methods support.  
**Fix:** Replace "strongly disfavors" with "is inconsistent in amplitude with under the present pipeline" and move the matched-reanalysis caveat into the same sentence.

**PAPER-GRO-B2 (BLOCKER)**  
**Section:** Sec. 1 (Introduction) and Sec. 7 (Comparison), Iye et al. citation  
**Issue:** The Iye:2026P6 entry remains "in preparation, arXiv ID pending; cited per private communication." This is unverifiable and violates PRD/MNRAS standards for bibliographic entries. Prior rounds already flagged similar regressions (e.g., Shamir DOI).  
**Fix:** Remove the citation or replace with a verifiable published reference; rephrase the sentence to avoid reliance on the pending work.

**PAPER-GRO-M1 (MAJOR)**  
**Section:** Table I (headline_summary) footnote b and Sec. 4.3 (Monopole+Mask Leakage)  
**Issue:** Footnote b correctly notes that the post-MASTER +1.85σ lives under a different null, but the surrounding prose and Table III restructuring still risk cross-null conflation for readers. The monopole-only generative null is load-bearing for the leakage interpretation yet is not the null used for the headline post-MASTER numbers.  
**Fix:** Add an explicit one-sentence disclaimer in the Table I caption and Sec. 4.3: "All post-MASTER significances use label-shuffle MC unless otherwise stated; the monopole-only null is used only for pre-MASTER leakage calibration."

**PAPER-GRO-M2 (MAJOR)**  
**Section:** Sec. 9 (Sky Region Balance), Table II footnote and global_cw_fraction.json reference  
**Issue:** The footnote claims the per-region breakdown "is reported in the table cells directly above" while the cited artifact is global_cw_fraction.json and a dedicated per-region JSON is queued for v1.0.89. This creates an artifact-to-table mismatch that prior rounds explicitly required verification on.  
**Fix:** Either commit the per-region JSON now or change the footnote to state that the table is the sole source of the per-region numbers.

**PAPER-GRO-m1 (minor)**  
**Section:** Sec. 5.2 (D4-TTA hold-out) and Sec. 4.3  
**Issue:** The ~21% rotational uncertainty is now numerically consistent with the argmax flip rate, but the D4 hold-out (N=1,558) has a Poisson floor of ±1.3% that is larger than the 0.26% monopole residual it is meant to bound. The limitation is noted but buried.  
**Fix:** Move the Poisson-amplitude caveat into the main paragraph rather than a footnote.

**PAPER-GRO-m2 (minor)**  
**Section:** Abstract and Sec. 1 (first paragraph)  
**Issue:** Framing as "one of the most extensive published bias-hardening audit suites" and "the largest survey-scale chirality measurement" is technically true by sample size but not novel in the parity-violation channel (prior nulls from Iye, Tadaki, and CE-ResNet exist). The title and abstract lead with the non-detection rather than the leakage-channel quantification, which is the actual incremental contribution.  
**Fix:** Lead the abstract with the leakage demonstration and demote the "largest" claim to a parenthetical size comparison.
