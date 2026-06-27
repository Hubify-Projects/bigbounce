# P4 R54 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R54_P4/chirality_catalog_paper.pdf` md5=bda86fa1 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 281.2s

---

**Referee Report – Physical Review D**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA … (P4)

**Recommendation on first read:** REJECT

The manuscript is a 23-page methods paper whose central scientific claim is a null result (real-space dipole consistent with zero at <1σ under the primary estimator). The length, the proliferation of distinct null constructions whose numerical outputs are presented side-by-side, the heavy reliance on non-public “artifact” files, and the absence of a concise, self-contained statistical argument all place the work well below the PRD threshold for a first-round submission.

Below is an exhaustive list of findings.  No finding has been softened.

### ESSENTIAL (paper cannot be accepted without these fixes)

**P4-E1** Abstract (p. 1) and Sec. IV C (p. 7)  
The abstract juxtaposes “+0.41σ (moment-z against the isotropic (pixel-)permutation null … empirical-rank p = 0.31” with “robust under a per-galaxy label-shuffle null, z = 0.70” without repeating the explicit qualifier “these σ values … are not directly comparable” that appears only later in the body.  
**Required fix:** Either remove one of the two numbers from the abstract or insert the full comparability caveat at the first juxtaposition.

**P4-E2** Abstract (p. 1) – load-bearing scalars  
The abstract states “N ≈ 9.5 × 10^5 spirals” for the HC subsample used in the primary dipole fit.  Table I (p. 5) gives exactly 949 584.  The abstract also quotes “+0.41σ” and “z ≈ –18”.  None of these three numbers is recomputed or derived in the abstract itself; the reader must hunt through five pages.  
**Required fix:** Abstract must be numerically self-contained or the quoted values must be removed.

**P4-E3** Sec. III A (p. 3) and Table III (p. 11)  
Multiple σ values obtained from qualitatively different null procedures (pixel-permutation, label-shuffle, block-bootstrap, direct-MC, hemisphere max-statistic) are listed in the same table and discussed in the same paragraph without the phrase “not directly comparable” appearing after every row or every sentence.  Instruction 7 is therefore triggered.  
**Required fix:** Insert the explicit qualifier after every numerical entry that crosses null families, or move all secondary nulls to a supplementary table labeled “diagnostic only.”

**P4-E4** Sec. IV D (p. 9–10) and Fig. 8 (p. 10)  
The claim that the monopole-only generative null “reproduces 99.32 % of the observed pre-MASTER pseudo-C_ℓ^(ℓ=1) power” is presented as a quantitative result, yet the only supporting number is a single scalar (0.40 pp) whose derivation is relegated to an unreleased artifact script.  No effect-size statement (fractional power, Cramér’s V, etc.) accompanies the headline percentage.  
**Required fix:** Provide the exact arithmetic and the artifact pointer, or downgrade the claim to qualitative.

**P4-E5** Data Availability (p. 22)  
The release commit hash (53b41d12) and the Zenodo DOI are stated, but the text simultaneously refers to “artifact c11b_hc_dipole_qc_rerun.json”, “c12_r24conf_local_batch.json”, etc.  These internal bookkeeping strings appear inside the published PDF.  
**Required fix:** Remove every internal artifact filename from the main text; move them to a machine-readable manifest that is version-stamped with the same DOI.

**P4-E6** Length vs. contribution  
A 23-page manuscript whose headline result is “dipole consistent with null at 0.41σ” violates the implicit PRD expectation that a null-result methods paper be concise.  Recommended maximum length for this class of result: 10–12 pages including appendices.

### MAJOR (significant revision required)

**P4-M1** Sec. I (p. 2) – “largest chirality-labeled galaxy catalog to date”  
The claim is repeated in the abstract and introduction.  No quantitative comparison table against Shamir (2022), Jia et al. (2023), or the full DESI EDR release is supplied.  The statement is therefore unsupported.

**P4-M2** Sec. IV B (p. 6) and Fig. 3 (p. 7)  
The global f_CW = 0.4974 is stated to 4 decimal places, yet the only uncertainty quoted is the binomial σ = 2.79 × 10^{-4}.  No systematic floor from the GZ1 training-label bias (explicitly acknowledged on p. 3) is propagated into this number.

**P4-M3** Fig. 4 (p. 8) and caption  
The color scale is given as [–0.08, +0.08] in A_p units, but the text never states whether this is the full dynamic range or a clipped range chosen for visual effect.  Axis label is present but the clipping decision is undocumented.

**P4-M4** Sec. V A (p. 12) – comparison with Shamir  
The paper asserts that its 0.32 % WLS amplitude is “in tension” with Shamir’s 1.7–4 %.  No matched-footprint reanalysis of the Shamir catalog is performed; the comparison therefore rests on an apples-to-oranges claim.

**P4-M5** Appendix D (p. 19–20)  
Eight “anchor” systematics tests are described, yet only two (apodization and WLS) receive quantitative numbers in the main text.  The remaining six are summarized by the single sentence “all eight tests pass.”  This is insufficient for a PRD methods paper.

### MINOR

**P4-m1** Duplicate phrasing on p. 11: “canonical canonical-mask residual”.  
**P4-m2** Future date “June 13, 2026” on title page.  
**P4-m3** Inconsistent use of “z” for both redshift and moment-ratio significance (reader must disambiguate from context).  
**P4-m4** Table II (p. 7) quotes excess in both percent and σ without a column header clarifying the units.

### NIT (cosmetic)

- Several figure captions contain the internal string “artifact … .json”.  
- Page 1 contains the parenthetical “(Dated: June 13, 2026)” which is unnecessary for a journal submission.

## Summary recommendation

**REJECT**

The manuscript’s central result is a carefully documented null detection whose statistical machinery is spread across more than twenty pages and multiple incommensurable null constructions.  The abstract is not numerically self-contained, internal artifact filenames appear in the published text, and the length is disproportionate to the scientific claim.  These deficiencies are structural; they cannot be repaired by minor editing.  A substantially shortened (≤12 page), self-contained version that presents only the primary estimator and its single, explicitly qualified null would be required for re-submission.