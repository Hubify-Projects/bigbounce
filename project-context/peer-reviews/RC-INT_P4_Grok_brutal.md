# P4 RC-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/P4_RC.pdf` md5=a53c7966 pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 213.3s

---

**Referee Report (Adversarial Review — PRD)**

**Paper:** P4 (Golden, “Survey-Scale Galaxy Chirality with Equivariant TTA…”)

**Finding P4-E1 (ESSENTIAL)**  
Section I / p. 2 and abstract: “to our knowledge, the largest chirality-labeled galaxy catalog to date: 8,474,531…”. No citation or explicit search is supplied for any post-2023 catalog exceeding this size. Required fix: either delete the claim or add a dated literature search statement.

**Finding P4-E2 (ESSENTIAL)**  
Abstract + p. 1: “+0.41σ (moment-z…)” and “z = 0.58 (per-galaxy label-shuffle null…)” appear in the same sentence. Although a parenthetical note exists, the abstract itself juxtaposes the two numbers without the qualifier. Every load-bearing scalar in the abstract must be traceable to a single, explicitly qualified estimator. Required fix: rewrite abstract so that no two distinct-null σ values are ever presented without the “not directly comparable” clause attached to each.

**Finding P4-E3 (ESSENTIAL)**  
Abstract claims “a Quantifiable Monopole-Mask Leakage Channel” as a primary result. The body (p. 11, Table IV) shows that the generative monopole-only null reproduces 99.32 % of the raw pre-MASTER power; the residual +1.69σ is therefore a statement about the null model, not an independent measurement of leakage amplitude. The abstract phrasing is stronger than the calibrated body statement. Required fix: change abstract wording to “evidence that a monopole-mask leakage channel accounts for the bulk of the pre-MASTER ℓ = 1 power.”

**Finding P4-M1 (MAJOR)**  
The manuscript is 24 pages of main text plus extensive appendices. PRD length guidelines and the actual information content (null dipole + systematics audit) are mismatched. A 12–14 page Letter or a condensed Methods paper would be appropriate. Required fix: cut to ≤14 pages or justify the length in a cover letter.

**Finding P4-M2 (MAJOR)**  
66.5 % of training labels come from CE-ResNet (p. 3). The label-shuffle and per-pixel permutation nulls therefore test only the ViT-TTA stage, not independence from the upstream model. The paper acknowledges this (p. 13) but still presents the nulls as “diagnostic-only” without quantifying the inherited bias floor. Required fix: add an explicit upper bound on the CE-ResNet-induced systematic (e.g., via the GZ1 cross-match residuals) or downgrade all “null” claims to “conditional on CE-ResNet labels.”

**Finding P4-M3 (MAJOR)**  
Table III and p. 10–11 present +3.64σ (canonical, label-shuffle) and +7.28σ (apodized, label-shuffle) side-by-side. Although the text states they are “not directly comparable,” the numerical values are used to argue that the MASTER channel is systematics-dominated. A single consistent null (or explicit conversion between the two) is required before any comparative claim.

**Finding P4-N1 (MINOR)**  
Figure 4 caption and p. 7: color scale is given in A_p units but the figure itself is labeled with the raw (N_CW – N_CCW)/(N_CW + N_CCW) range [−0.08, +0.08]. The conversion factor 2 is never stated on the figure. Add the factor explicitly.

**Finding P4-N2 (MINOR)**  
Several appendix file names contain internal tags (“r24conf_local_batch.json”, “c11_meta_m4_slab_stats.json”). These are harmless but should be renamed to stable, version-free identifiers before public release.

**Finding P4-NIT1 (NIT)**  
Duplicate phrasing “canonical canonical-mask” appears once in the rendered text (p. 11, left column). Typo only.

**Abstract-last drift sweep**  
All quantitative claims in the abstract were re-checked against the body. After the fixes listed in E2 and E3, the abstract will be consistent.

**Bibliography & provenance**  
All cited arXiv IDs, years, and sample sizes match the referenced papers. Data-availability section lists DOIs and scripts that are internally consistent with the text.

**Summary recommendation**  
**MAJOR REVISIONS**

The paper contains a thorough, well-documented null result and a valuable systematics audit. However, three essential fixes (abstract qualification of distinct-null σ values, removal or sourcing of the “largest catalog” claim, and recalibration of the “quantifiable leakage channel” phrasing) plus a mandatory length reduction are required before the manuscript meets PRD standards. Once those are addressed, the work would be suitable for publication.