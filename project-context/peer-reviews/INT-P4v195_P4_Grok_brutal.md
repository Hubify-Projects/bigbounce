# P4 INT-P4v195 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/P4_v195.pdf` md5=87d3eb2c pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 181.8s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (P4)

**Journal bar:** Physical Review D (rigorous cosmology methods)

**Findings**

**P4-E1 (ESSENTIAL)**  
Section: Title page (rendered p. 1)  
Problem: “(Dated: June 28, 2026)” appears in the author block.  
Required fix: Remove entirely; a submission cannot carry a future date.

**P4-E2 (ESSENTIAL)**  
Section: Abstract (p. 1) and repeated throughout (e.g., pp. 3, 7, 10, 11)  
Problem: Multiple distinct null procedures are quoted side-by-side with numerical \(\sigma\) or \(z\) values (e.g., “+0.41\(\sigma\) … \(z=0.58\) … +3.64\(\sigma\) … +7.93\(\sigma\)”) even though the paper itself states they “are not directly comparable as detection significances.” The parenthetical qualification is not present at every juxtaposition.  
Required fix: Either (a) remove all cross-null numerical comparisons from the abstract and every results table/figure caption or (b) insert the explicit non-comparability sentence immediately before every such block.

**P4-E3 (ESSENTIAL)**  
Section: Entire body (multiple occurrences on pp. 2–12, 15, 20–22)  
Problem: Internal repository/script paths and provenance tags appear verbatim in the running text and captions, e.g.,  
“artifact pipelines/p2_chirality/outputs/canonical_provenance/c11_meta_m4_slab_stats.json”,  
“pipelines/p2_chirality/outputs/canonical_provenance/c12_r24conf_local_batch.json”,  
“artifact c9b”, “R7”, “R-round”, “superseded”, etc.  
These are internal-audit / version-control artifacts, not scientific content.  
Required fix: Delete every such string; replace with stable, citable artifact DOIs or remove the reference.

**P4-E4 (ESSENTIAL)**  
Section: Abstract (p. 1) vs. body (pp. 7, 10, 12)  
Problem: Abstract claims “the largest chirality-labeled galaxy catalog to date: 8,474,531” and presents the +0.41\(\sigma\) result as the primary scientific outcome. The body repeatedly qualifies the same number as “diagnostic-only” and shows that the real-space dipole is consistent with a 9.5\(\sigma\) monopole leakage channel. The abstract therefore overstates both novelty and the strength of the null result.  
Required fix: Rewrite the abstract to match the body’s final calibrated statement (null result after systematics attribution; catalog size secondary).

**P4-M1 (MAJOR)**  
Section: pp. 1–24 (paper length)  
Problem: 24-page manuscript whose primary result is a null detection after exhaustive systematics tests. PRD expects concise Letters or short articles for such outcomes.  
Required fix: Condense to \(\leq 12\) pages or reformat as a focused Methods + one key systematics figure paper.

**P4-M2 (MAJOR)**  
Section: Table I, Table III, Fig. 8, and all MASTER \(\ell=1\) claims  
Problem: The paper reports \(\sigma\) values from 500-MC, \(10^4\)-permutation, block-bootstrap, and label-shuffle nulls without a single consolidated table that states (a) exact sample, (b) exact mask, (c) exact weighting, and (d) the explicit statement that these \(\sigma\)s are incomparable. Readers cannot reproduce the quoted numbers from the displayed inputs alone.  
Required fix: Provide one self-contained table with all four quantities and the non-comparability caveat.

**P4-M3 (MAJOR)**  
Section: Data Availability (p. 22)  
Problem: Links point to a live “main” branch rather than a frozen release tag or immutable Zenodo DOI. Several artifact descriptions (units, mask definition, burn-in) are inconsistent with the body text.  
Required fix: Deposit a single frozen release (tag + DOI) whose manifest exactly matches every number and mask used in the paper.

**P4-N1–N8 (MINOR)**  
Multiple instances of duplicated phrases (“canonical canonical-mask”), missing axis labels on supplementary figures, inconsistent capitalization of “NaMaster” vs. “namaster”, and citation years that do not match the cited arXiv abstracts.  
Required fix: Standard copy-editing pass.

**Summary recommendation**  
**REJECT**

The manuscript in its present form contains multiple internal-audit strings, an impossible future date, and repeated numerical comparisons across incommensurable nulls that the text itself declares invalid. These are not cosmetic issues; they violate PRD standards for reproducibility and clarity. Even after those fixes, the 24-page length for a systematics-dominated null result would still require major compression. The work may contain valuable technical content, but the current submission does not meet the journal’s threshold.