# P5 R38conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.73.pdf` md5=? pages=?
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 339.8s

---

**Referee Report**

**Paper:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample  
**Journal:** Physical Review D  
**Reviewer stance:** Adversarial, PRD standards

**P5-E1**  
**Section:** Entire manuscript (pp. 1–25+)  
**Problem:** The manuscript contains dozens of internal pipeline paths and code-repository strings (e.g., “pipelines/p5_desi_chirality/outputs/23_unique_parent_rebuild.json”, “pipelines/p5_desi_chirality/outputs/17_v0151_closure_recomputes.json”, “pipelines/p5_desi_chirality/env_finder/01_compute_vweb.py”, etc.). These appear in the body text, footnotes, and figure captions.  
**Required fix:** Remove every such string. Replace with archival data-product DOIs or table/figure references only. This is internal bookkeeping and unacceptable in a PRD submission.

**P5-E2**  
**Section:** Abstract (p. 1) and §II (p. 3)  
**Problem:** The headline result and all quantitative claims rest on “Paper IV” (companion work, “not yet peer-reviewed”). Multiple load-bearing numbers (monopole offset −0.0026, classifier systematic 0.26 pp, etc.) are imported by citation without being recomputed or tabulated here. The argument is not standalone.  
**Required fix:** Either (a) make the present paper self-contained by reproducing the necessary Paper IV numbers in an appendix, or (b) withdraw until Paper IV is public and citable.

**P5-E3**  
**Section:** Abstract (p. 1) and Table III (p. 8)  
**Problem:** Abstract states “the CW fraction shows no environment dependence beyond … ≈0.26 pp”. Table III reports per-class \(\sigma_{\rm from\,half}\) values (−0.68, +0.55, −2.61, −4.66) that are computed from different \(n\) and different null procedures. No sentence states that these \(\sigma\) values are “not directly comparable across rows.” Instruction 7 violation.  
**Required fix:** Add an explicit, repeated qualifier at every juxtaposition of \(\sigma\) values derived from different nulls or different bin sizes.

**P5-M1**  
**Section:** Abstract length and structure (pp. 1–2)  
**Problem:** The “abstract” occupies >1.5 pages and functions as an executive summary containing results, robustness tests, and secondary-path declarations. PRD abstracts are limited to ~250 words.  
**Required fix:** Reduce to a conventional abstract; move detailed claims to the body.

**P5-M2**  
**Section:** §V.A and §VI.A (pp. 5–8)  
**Problem:** Multiple distinct null procedures (label-shuffle, position-shuffle, maximal-void-density permutation, etc.) are used. Effect-size measures (Cramér’s V, fractional deviation, etc.) are supplied only sporadically; most headline \(\chi^2\) and \(\sigma\) statements lack them. Instruction 19 violation.  
**Required fix:** Attach a practical-significance metric to every \(\chi^2/\sigma\) claim.

**P5-M3**  
**Section:** Figure 6 (p. 14) and associated text  
**Problem:** HEALPix map caption and body claim “no coherent large-scale structure.” The map shows isolated high-|\(\sigma\)| pixels; the quantitative test that these pixels are consistent with the label-shuffle null is only the global \(p=0.135\). No per-pixel or cluster-size test is shown.  
**Required fix:** Provide the explicit statistic that rules out coherent structure (e.g., two-point correlation of signed \(\sigma\) pixels or size distribution of |\(\sigma\)|>3 islands).

**P5-N1**  
**Section:** Date line (p. 1)  
**Problem:** “Dated: June 2026 — v0.1.73-2026-06-13”. Future date and internal version tag.  
**Required fix:** Replace with submission date only.

**P5-N2**  
**Section:** Multiple figure captions (e.g., Fig. 2, Fig. 7)  
**Problem:** Captions contain parenthetical pipeline paths and “see §VIII” cross-references that are meaningless without the companion paper.  
**Required fix:** Remove.

**Additional observations (no new IDs)**  
- The manuscript is ~25–31 pages for a null-result cross-check. PRD typically expects ≤15–18 pages for such a focused methods test.  
- No Data Availability section with frozen DOIs or commit hashes is visible in the rendered pages.  
- Several tables (III, VII, X) report \(\sigma_{\rm from\,half}\) values whose numerical origin (exact binomial or Monte-Carlo) is not recomputed in the text; the reader must trust the pipeline output.

**Summary recommendation**  
**MAJOR REVISIONS**

The combination of pervasive internal code-path artifacts, non-self-contained dependence on an unpublished companion paper, non-comparable \(\sigma\) values presented without explicit qualification, and an abstract that functions as a results section places the manuscript well below the PRD threshold in its current form. The scientific content (a carefully executed null result with multiple cross-checks) may be publishable after the essential and major items above are addressed, but the present draft cannot be accepted.