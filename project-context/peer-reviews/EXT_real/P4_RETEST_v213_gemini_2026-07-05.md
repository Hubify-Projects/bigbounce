# P4 v1.0.213 De-biased EXT Re-test — GEMINI

- **Reviewer:** Gemini (gemini.google.com, /u/1/)
- **Account:** houston@bamf.com (Work, Ultra)
- **Model:** Gemini Pro
- **Timestamp:** 2026-07-05
- **Chat URL:** https://gemini.google.com/u/1/app/5cf067f80a178c0a
- **PDF:** /tmp/retest_P4_v213.pdf (974375 bytes)
- **Prompt:** standard PRD referee prompt (VERDICT / ISSUES [MAJOR|MINOR] / one-sentence central-claim)
- **(1) VERDICT line:** MINOR REVISIONS

---

## RAW RESPONSE (verbatim)

VERDICT: MINOR REVISIONS

ISSUES:

[MAJOR] Abstract and Manuscript Readability: The manuscript suffers from extreme structural density, specifically the overuse of deeply nested parenthetical statements that span multiple lines (e.g., the abstract contains a single, highly technical 90-word parenthetical clause). Key statistical results, null definitions, and dataset splits are buried in these blocks. The author must restructure the abstract and Results sections to state primary measurements, uncertainties, and nulls in clear, declarative sentences to meet the readability standards of Physical Review D.

[MAJOR] Section VI.A (Pseudo-label Independence): The author notes that 66.5% of training labels derive from CE-ResNet, risking inherited survey bias. To counter this, a sub-model trained purely on human GZ1 labels is used, but only on a highly restricted sample of N=1.5×10^4 galaxies, which inflates the statistical floor by a factor of ≈7.9. The text claims a full-catalog re-inference is a "straightforward compute extension" that would match the headline floor. Given its critical importance to the total independence of the result, the author should clarify the specific technical limitations preventing this full run, or ideally, perform the extension to close the loop.

[MINOR] Table Captions: The captions for several tables (e.g., Tables V, VIII, and XIII) are excessively long, functioning as localized analysis paragraphs rather than descriptive text. The analytical interpretations—such as the discussion of rank-deficiency and conditioning in Table XIII—should be moved to the main text (e.g., Appendix D) to streamline the presentation.

[MINOR] Section IV.D (Forward Model Residual): The forward model of the canonical-mask l=1 residual accounts for roughly 52-54% of the amplitude, leaving ~47% as an explicitly open item. While the author correctly argues that the primary null relies on the real-space estimator that bypasses this harmonic leakage, the manuscript would benefit from a brief mathematical demonstration or tighter logical bounding explicitly showing why this specific 47% unmodeled harmonic structure cannot mathematically project into the real-space dipole estimator and perfectly mask a genuine signal.

The central claim of a null real-space chirality dipole at sub-percent sensitivity is highly robust and fully supported by the rigorous equivariant bias-mitigation pipeline and the exhaustive characterization of the monopole-mask leakage channel.
