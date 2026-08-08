# RBEXT P5 ChatGPT — chat: https://chatgpt.com/c/6a42c541-1718-83e8-a714-c14d554abf29
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (default/Instant tier)
PDF: RBEXT_P5.pdf | md5: 4765d0ff8114815c4ef333b93f945433
Harvested: 2026-06-29

---

1. Recommendation: MAJOR REVISIONS

The paper is substantially strengthened versus a simple T-Web-only analysis, and the DESIVAST-anchored null appears plausible. However, the manuscript is over-claimed and internally over-expanded: the nominal primary analysis is post-hoc, the T-Web classifier is demonstrably selection-function/RSD sensitive, and many robustness claims rely on complex private artifacts rather than directly inspectable tables. I would not reject, but it needs a tighter, cleaner, journal-grade presentation before acceptance.

2. BLOCKERS

- Post-hoc primary designation is still a real statistical weakness. The paper admits no a priori plan and then declares DESIVAST primary after many classifiers/stratifications were explored. The Bonferroni-5 accounting helps, but does not fully solve garden-of-forking-paths risk.
- T-Web environmental labels are not robust enough for headline framing. The paper itself shows selection correction changes class populations massively and randoms-weighted rebuilding reshapes the field dramatically. This makes the T-Web analysis secondary at best; the title/abstract should not present it as co-equal with DESIVAST.
- RSD limitation remains unresolved. The paper acknowledges fixed-redshift-space classification and anisotropic tidal-tensor deformation, but still uses broad "environment independence" language. The claim should be explicitly redshift-space / DESIVAST-void-space limited.

3. MAJORS

- Overlong robustness narrative obscures the actual result. Reorganize around one primary estimand: DESIVAST void vs non-void ΔfCW, then short secondary checks.
- Dependence on Paper IV labels/monopole should be stated more neutrally. The result depends fully on Paper IV classifier labels. Monopole-subtraction interpretation is reasonable but should not substitute for independent chirality-classifier validation inside P5.
- Private artifact dependence is too heavy. Many claims cite artifact IDs rather than giving self-contained numbers or exact reproducibility steps for key robustness tests.
- The dark/bright residual is under-resolved. The ∼2σ bright/dark sign flip is not fatal but is the most suspicious residual. The manuscript should avoid implying it is fully explained by BGS selection effects.
- DESIVAST hole-union vs maximal-sphere definitions need clearer hierarchy. Specify which definition is primary and which are supporting.

4. MINORS

- The title is too long and over-specific.
- Several "largest / cleanest / strongest" phrasings should be softened.
- Figures 6 and 8 are visually dense; add clearer captions and perhaps split panels.
- The toy EFT appendix is speculative and should be shortened or moved to discussion.
- Some notation around σfrom_half, σpred, and σvs_monopole is cumbersome; simplify.

5. Strengths

- The DESIVAST primary null is statistically persuasive: ΔfCW ≈ +0.0007 with p ≈ 0.76.
- The manuscript is unusually transparent about limitations, post-hoc choice, RSD, duplicate rows, and classifier monopole.
- The three-algorithm DESIVAST cross-check is a strong robustness feature.
- The paper avoids claiming a positive signal and frames the result mostly as an upper-bound/null test.
- The appendix contingency tables improve reproducibility.
