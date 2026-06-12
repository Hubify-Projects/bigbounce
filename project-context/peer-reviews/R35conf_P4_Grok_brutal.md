# P4 R35conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v178.pdf` md5=0275961b pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 108.5s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (DESI Legacy, 8.47M galaxies)

**Journal target:** Physical Review D

**Date of review:** based on rendered PDF pages 1–22

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P4-E1** (Abstract, p. 1; also §IV C p. 7, Table I p. 5)  
The abstract states the primary result as “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations)” for the real-space dipole. Table I and the surrounding text present five other estimators on the same catalog that return +3.64σ, +7.28σ, +7.13σ, etc. The paper repeatedly states these estimators are “not directly comparable” and “not two independent detection claims,” yet the abstract juxtaposes only the +0.41σ number without the required qualifier. This violates the rule that sigma values from different null procedures must carry an explicit non-comparability statement at every load-bearing location.

**P4-E2** (entire manuscript, >30 instances)  
Internal-audit and version-history language appears throughout the body and appendices: “An earlier version of this paper reported… that result is withdrawn (Appendix A)”, “superseded”, “earlier run”, “R7”, “artifact c11_…json”, “pipelines/p2_chirality/…”, commit hashes, “seed 42”, “provenance note”, “withdrawn subsample-mask null”, etc. These are not part of the scientific record and must be removed.

**P4-E3** (Abstract p. 1; §VI A p. 12; Table V p. 13)  
Abstract claims “50 %-recovery-at-3σ injection-recovery threshold at |A_dipole| ≥ 0.75 %”. Table V and the injection-sweep text show this threshold is estimator-specific (HC-broad subsample, per-pixel binomial null) and is not the falsification boundary for the primary real-space dipole. The abstract therefore states a stronger claim than the body’s final calibrated statement.

**P4-E4** (§IV D p. 9, Table III p. 11, Appendix D p. 18)  
The +3.64σ canonical-mask residual (pre-MASTER) and the +7.28σ / +7.31σ post-MASTER values are presented side-by-side without the mandatory “not directly comparable” clause at each juxtaposition. Instruction 7 requires this qualification wherever different null procedures appear together.

**P4-E5** (Data Availability p. 21)  
The reproducibility section lists commit hash 53b41d12 (v1.0.175) and multiple artifact JSON files whose units, masks, and sample definitions are inconsistent with the final Catalog C numbers quoted in the abstract and Table I. No frozen-release DOI or end-to-end script hash is provided that would allow a standalone reader to regenerate the exact numbers used in the abstract.

### MAJOR findings (significant revision required)

**P4-M1** (length)  
22 pages for a null-result + systematics-diagnosis paper exceeds PRD norms for this class of result. Recommended maximum: 12–14 pages after removal of internal notes and redundant diagnostic figures.

**P4-M2** (§I p. 2, §V p. 12)  
Claims of “largest chirality-labeled galaxy catalog to date” and “to our knowledge” are not benchmarked against any contemporaneous public release; the statement is unsupported.

**P4-M3** (Fig. 8 p. 10, Table III p. 11)  
The MASTER pseudo-C_ℓ band-power plot and the tabulated C_b values use different normalizations (apodized vs. canonical) without an explicit conversion factor shown on the figure or in the caption. A reader cannot recompute the quoted +7.31σ from the plotted points.

**P4-M4** (multiple sections)  
Every inequality or robustness assertion (“robust to”, “consistent with”, “dominates”, “negligible”) lacks the required numerical value or artifact pointer (pattern-048). Examples: p. 7 “robust under a per-galaxy label-shuffle null”, p. 9 “99.32 % of the raw pre-MASTER power”.

**P4-M5** (Appendix B p. 16)  
The D4-TTA validation is performed on only ~4 000 galaxies; the claimed flip-equivariance (Δp_CW < 0.0016) is not re-tested on the full 8.47 M catalog or on the HC-broad subsample used for the primary dipole.

### MINOR findings

**P4-m1** Duplicate or near-duplicate phrasing in several figure captions (“canonical canonical-mask”).  
**P4-m2** Axis labels on Fig. 4 and Fig. 7 omit explicit units for A_p (should read “A_p = 2(f_CW – ½)”).  
**P4-m3** Reference list contains arXiv IDs whose quoted statistics (e.g., Shamir 2012 2–4σ) cannot be verified from the cited abstracts alone; page numbers or table references are missing.

### NIT findings

**P4-n1** Inconsistent use of “f_sky = 0.49005” vs. “0.494” for the same mask in different tables.  
**P4-n2** Several figure captions contain file-path strings that survived copy-editing.

### Summary recommendation

**REJECT**

The manuscript in its present form is not a journal submission; it is an internal development document containing withdrawn results, superseded analyses, commit hashes, artifact file names, and version-history commentary on virtually every page. Even after those layers are stripped, the abstract makes quantitative claims that are not traceable to a single, consistently qualified estimator in the body, and multiple σ values from incommensurable null procedures are presented without the required non-comparability statements. These are not cosmetic issues; they are violations of PRD standards for reproducibility, clarity of statistical claims, and separation of the scientific record from the authors’ audit trail. The paper would require a complete rewrite (not merely minor revisions) before it could be considered for Physical Review D.