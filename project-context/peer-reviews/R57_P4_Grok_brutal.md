# P4 R57 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R57_P4/chirality_catalog_paper.pdf` md5=5ddefa62 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 277.4s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (P4)

**Journal:** Physical Review D

**Round context:** First read, adversarial standard

**Findings**

**P4-E1 (ESSENTIAL, Abstract + p. 1, Sec. I)**  
The abstract and opening paragraph juxtapose multiple \(\sigma\) values (+0.41\(\sigma\), +3.64\(\sigma\), +7.28\(\sigma\), +7.93\(\sigma\)) drawn from distinct null procedures (pixel-permutation, label-shuffle, block-bootstrap, monopole-only generative) without repeating the explicit qualifier “not directly comparable as detection significances” at every juxtaposition. Table III and the MASTER paragraph on p. 9 repeat the same problem. Required fix: insert the qualifier in every sentence or table footnote where two or more \(\sigma\) values from different nulls appear; otherwise the reader cannot know which number is being treated as a detection significance.

**P4-E2 (ESSENTIAL, Abstract + p. 5, Table I)**  
Abstract states “the largest chirality-labeled galaxy catalog to date: 8,474,531… (3.2 Million Spirals)”. Body (Table I, Catalog C) shows that only the high-confidence subset (\(p_\text{eq}>0.6\), \(N=949{,}584\)) is used for the primary real-space dipole; the full 3.2 M spiral count includes the low-confidence tail that drives the 9.5\(\sigma\) monopole. The abstract claim is therefore stronger than the calibrated statement in Sec. IV C. Required fix: qualify the “largest” claim with the exact selection used for the headline null result.

**P4-E3 (ESSENTIAL, p. 9, Sec. IV D + Table IV)**  
The paper asserts that the monopole-only generative null “reproduces 99.32 % of the observed pre-MASTER pseudo-\(C_\ell\) power”. This quantitative claim is given without the per-realization standard error or the exact artifact pointer for the 500 realizations. The 0.40 pp figure is presented as a load-bearing result; the supporting number and seed must be supplied.

**P4-M1 (MAJOR, entire manuscript length)**  
23 pages + 5 appendices for a null result whose primary cosmological claim is a 0.41\(\sigma\) dipole. The eight-anchor systematic battery, while thorough, inflates the paper far beyond the contribution. Recommended maximum: 12–14 pages. The current length violates PRD’s expectation that a methods paper be proportionate to its incremental advance over Shamir (2012–2022) and Jia et al. (2023).

**P4-M2 (MAJOR, p. 4, Sec. III D + Eq. (2))**  
The 2-fold TTA procedure is presented as enforcing flip-equivariance “by construction”. The \(D_4\) hold-out test on p. 17 shows a 21.4 % flip rate on borderline galaxies, demonstrating that the learned model is not perfectly equivariant. The text never quantifies how much residual non-equivariance leaks into the final \(A_p\) map. Required fix: report the measured post-TTA flip fraction on the production catalog and propagate it into the dipole uncertainty budget.

**P4-M3 (MAJOR, p. 8, Fig. 4 + p. 9, Fig. 5)**  
Fig. 4 (Mollweide) and Fig. 5 (density map) use different effective sky fractions (\(f_\text{sky}=0.494\) vs. 0.49005) and different weighting schemes without a direct statement that the two visualizations are on identical masks. Axis labels are present but the color-bar units in Fig. 4 are given only as \((N_\text{CW}-N_\text{CCW})/(N_\text{CW}+N_\text{CCW})\) while the text repeatedly quotes \(A_p=2(f_\text{CW}-1/2)\). The reader cannot verify numerical consistency without external recomputation.

**P4-M4 (MAJOR, p. 1 abstract + p. 12, Sec. V A)**  
The abstract claims the result is “inconsistent… by a factor of ~5–12” with Shamir’s 2–4\(\sigma\) detections. The comparison uses the present pipeline’s best-fit WLS amplitude (0.32 %) against Shamir’s reported range, but does not re-analyze Shamir’s catalog with the current mask or TTA procedure. This is an apples-to-oranges claim that must be either removed or supported by a matched-footprint reanalysis.

**P4-N1 (MINOR, p. 2, Sec. II A)**  
“\(N=8{,}474{,}688\) galaxy images” vs. “8,474,531 galaxies retained after image-quality QA”. The 157-object difference is never explained; a one-sentence statement is required.

**P4-N2 (MINOR, multiple tables)**  
Several tables (I, III, VII) mix “canonical” and “apodized” footprints without repeating the exact \(N_\text{side}\) and apodization length in every caption. Minor but cumulatively confusing.

**P4-NIT1–NIT3**  
Minor typographic issues (duplicate “canonical canonical-mask” phrasing on p. 20, inconsistent use of “pp” vs. “percentage points”, missing DOI for one cited data release) are cosmetic.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically elaborate null result whose headline cosmological claim is a sub-percent, statistically insignificant dipole. The analysis contains multiple distinct null procedures whose \(\sigma\) values are repeatedly placed in proximity without the required “not directly comparable” qualifier, an over-strong abstract claim about catalog size, an unsubstantiated 99.32 % reproduction figure, and an apples-to-oranges literature comparison. In addition, the 23-page length is disproportionate to the incremental advance. These are not cosmetic defects; they affect the reader’s ability to assess the statistical claims at the level demanded by Physical Review D. A substantially shortened revision that (i) enforces the “not directly comparable” qualifier everywhere, (ii) aligns every abstract scalar with the final calibrated body statement, and (iii) supplies the missing per-realization errors and matched-footprint reanalysis would be required before further consideration.