# P4 RB-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/P4_RB.pdf` md5=b8dc2625 pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 225.9s

---

**Referee Report**

**P4-E1** (Abstract, p. 1)  
The abstract juxtaposes “+0.41σ (moment-z …)”, “empirical-rank p = 0.31”, “z = 0.58 (per-galaxy label-shuffle)”, and “z = 0.70 (independent re-implementation)” without repeating the explicit qualifier “not directly comparable as detection significances” inside the same sentence. Per instruction 7 this is ESSENTIAL.  
Fix: insert the qualifier immediately after each numerical claim or move all numerical claims to a single sentence that already contains the qualifier.

**P4-E2** (Abstract, p. 1; §IV C, p. 7)  
Abstract states the primary result is “a real-space chirality dipole consistent with null”. Body (§IV C) shows the same data vector yields +0.41σ (isotropic pixel permutation) but +3.64σ (canonical-mask label-shuffle) and +7.93σ (10^4-permutation canonical unapodized). The abstract therefore over-claims uniformity of the null verdict. ESSENTIAL.  
Fix: replace “consistent with null” with “consistent with null under the isotropic pixel-permutation null but systematics-dominated under the canonical-mask null”.

**P4-E3** (Abstract, p. 1)  
Abstract claims “N ≈ 9.5 × 10^5 spirals” for the high-confidence dipole fit. Body Table I row (i) gives exactly 949,584. The approximation is unnecessary and risks transcription error. MINOR.  
Fix: write the exact integer.

**P4-M1** (entire ms, 24 pp)  
PRD length guideline for a null-result methods paper with no positive detection is ~10–12 pages. The present 24-page length (including 5 appendices of internal diagnostics) violates this. MAJOR.  
Fix: condense to ≤12 pages; move all but the two primary nulls (isotropic permutation + block-bootstrap WLS) to a supplemental archive.

**P4-M2** (§I, p. 2; §V A, p. 12)  
Claim “to our knowledge, the largest chirality-labeled galaxy catalog to date” is unsupported by a systematic literature search; only three prior catalogs are cited. MAJOR.  
Fix: add an explicit table comparing N_spiral, mask definition, and TTA protocol against Shamir (2012, 2020, 2022), Tadaki et al. (2021), and Jia et al. (2023).

**P4-M3** (Fig. 4 caption & §IV C, p. 7)  
Color scale is labeled in fractional units (N_CW – N_CCW)/(N_CW + N_CCW) while the text repeatedly quotes A_p = 2(f_CW – ½). The figure therefore cannot be read without the conversion factor supplied in the caption. MAJOR.  
Fix: add a second color bar in A_p units or state the conversion explicitly on the figure.

**P4-M4** (Table III, p. 11)  
All z-values are computed against distinct null ensembles (apodized vs. canonical mask, 10^4 vs. 500 realizations). No column warns the reader that the numerical z-values are incommensurable. MAJOR.  
Fix: add a footnote on every page containing Table III: “z-values in this table are not directly comparable across rows.”

**P4-N1** (p. 1, author affiliation)  
“Independent Researcher, Los Angeles, California, USA” with future date “June 29, 2026”. NIT (cosmetic).  
Fix: supply a conventional institutional affiliation or remove the date.

**P4-N2** (multiple locations)  
Phrases such as “canonical canonical-mask” and “pp-shuffle / d-str.” appear; these are typographic artifacts. NIT.  
Fix: proof-read.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically elaborate null result whose central claim (“dipole consistent with null”) is only true under one of several null constructions while being systematics-dominated under the others. The abstract does not faithfully reflect this hierarchy, the paper is twice the appropriate length for PRD, and multiple numerical claims are presented without the required incommensurability warnings. These are not cosmetic defects; they affect the scientific interpretation of the primary result. A substantially shortened version that (i) states the null verdict only under the isotropic pixel-permutation null, (ii) explicitly labels every other σ-value as a systematics diagnostic, and (iii) removes the internal-audit appendices would be reconsidered.