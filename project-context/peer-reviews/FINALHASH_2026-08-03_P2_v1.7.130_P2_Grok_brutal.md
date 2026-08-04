# P2 FINALHASH_2026-08-03_P2_v1.7.130 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3` [FALLBACK from grok-4]
**Input PDF**: `research/focused_paper_source_integration/02_full_draft.pdf` sha256=d3afe79fe70ce13cee5ec8149e84c4b42c78224ca6a90569058ec501222f5c2f pages=12
**Review packet(s)**: `4c749ff6698e0d31ecef0f5842f546a5f9d7bd4d903a8654ee1d8e3b3eab44d0`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 777.3s

---

**Referee Report (PRD Research Article)**

**P2-E1 (ESSENTIAL, Abstract + Sec. II.A, p. 1–2)**  
Abstract states “gives a local-type non-Gaussian amplitude \(f_{\rm NL}^{\rm local}=-35/16=-2.1875\)” and claims this “corrects the unreproduced printed −35/8 literature value.” Body (Eq. 2, Table I, Appendix B) shows the value is obtained only after restricting to the matter-dominated contraction phase with \(w=0\), \(\epsilon=3/2\), Bunch–Davies vacuum, and the specific Maldacena cubic action. The abstract omits these restrictions and the explicit statement (p. 3) that the result is conditional on assumption (d). Required fix: rewrite abstract sentence to include the four limiting assumptions or move the numerical claim out of the lead sentence.

**P2-E2 (ESSENTIAL, Abstract + Sec. IV, p. 4–5)**  
Abstract lists four numerical significances (2.63\(\sigma\), 3.1\(\sigma\), 2.3\(\sigma\), 0.4\(\sigma\)) for SPHEREx. These are obtained by direct substitution of the published Heinrich et al. baseline \(\sigma(f_{\rm NL}^{\rm local})\simeq0.7\) into Eq. (9) with an ad-hoc \(r=0.84\) weighting envelope. The paper itself labels them “illustrative conditional diagnostics, not an observational headline.” No new covariance, mask, or tracer selection is performed. The abstract therefore presents conditional arithmetic as quantitative results. Required fix: remove all numerical \(\sigma\) values from the abstract or qualify every one with “under the published Heinrich covariance and the stated 30 % \(b_\phi\) prior.”

**P2-M1 (MAJOR, Sec. I + entire length, p. 1–12)**  
The manuscript is 12 pages. The sole new algebraic result is the ordered-basis coefficient vector (3,1,−9,5,−33,9) and the verification that the four-vertex sum equals −35/16. All LSS mapping sections (III–VIII) are re-applications of existing kernels (Eqs. 6–8) to a new template shape. PRD research-article length for a coefficient correction plus illustrative re-mapping exceeds the frontier standard; comparable corrections appear as 4–6 page papers or letters.

**P2-M2 (MAJOR, Sec. II.C + Appendix B, p. 3, 8–10)**  
The claim that the result is “exact” is qualified by six explicit assumptions, two of which ((d) and (f)) are stated to be unverified beyond linear order. The torsion correction estimate (Eq. 5) is an order-of-magnitude parametric bound, not a computed integral. The paper therefore presents a conditional algebraic identity as an “exact” amplitude while simultaneously acknowledging that the physical regime in which the identity holds has not been demonstrated. Required fix: replace every occurrence of “exact” with “exact within the stated assumptions” and move the torsion bound to an explicit caveat paragraph.

**P2-M3 (MAJOR, Sec. IV + Table III, p. 4–5)**  
Table III juxtaposes four \(\sigma\) values obtained from qualitatively different null procedures (fixed nuisances, marginalization over \(A_{\rm GR}\), 30 % Gaussian prior, free \(b_\phi\)) without any statement that the numbers are not directly comparable. This violates the explicit instruction in the review criteria. Required fix: add the qualifier at every row or remove the table.

**P2-N1 (MINOR, Fig. 1 caption, p. 2)**  
Caption states the curve “approaches −35/16”; the plotted function visibly asymptotes to that value only for \(k_L/k_S\to0\). The caption should read “approaches the squeezed limit −35/16.”

**P2-N2 (MINOR, Data Availability, p. 7)**  
The repository link is given without a frozen commit hash or DOI for the exact v1.7.130 release. Minor archival hygiene issue.

**P2-NIT1–NIT3**  
Minor typographic items (header version string, repeated “exact” in captions, one redundant clause in Sec. IX) do not affect content.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript’s sole load-bearing result is an algebraic verification that four cubic vertices sum to \(f_{\rm NL}=-35/16\) under a tightly specified set of assumptions already present in the literature. All subsequent sections consist of conditional re-mappings of existing bias and projection kernels. The present length, the unqualified numerical significances in the abstract, and the side-by-side presentation of non-comparable \(\sigma\) values fall below PRD standards for a research article. A substantially shortened version focused on the vertex sum and the explicit resolution of the Cai–Li discrepancy could be reconsidered as a letter or brief report.