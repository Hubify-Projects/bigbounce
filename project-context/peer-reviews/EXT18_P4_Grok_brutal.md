# P4 EXT18 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 119.2s

---

**Referee Report for P4 (EXT18 verification)**

**P4-E1 (ESSENTIAL)**  
Abstract (p. 1) + Sec. IV.C (p. 7): “the equivariant-catalog high-confidence dipole fit … gives +0.41σ (moment-z …)”.  
The abstract presents this single scalar as the primary cosmological result. Body text (multiple locations, e.g., Table I caption, Sec. III.A, Sec. IV.C) repeatedly states that moment-z and rank-p values “are not directly comparable as detection significances” and are “diagnostic indicators only.” No single sentence in the abstract carries the required qualifier.  
**Required fix**: Rewrite abstract sentence to read “+0.41σ (moment-z against isotropic-bootstrap null; diagnostic only, not a detection significance)”.

**P4-E2 (ESSENTIAL)**  
Abstract (p. 1) + Sec. IV.D (p. 9) and Table III (p. 11): “+3.64σ canonical-mask residual”.  
Abstract lists this number without the explicit statement (present only in Sec. IV.D and Table III caption) that it is “non-primary … systematics-attributed” and “not a cosmological detection.” The abstract therefore over-claims relative to the body’s final calibrated statement.  
**Required fix**: Remove the 3.64σ figure from the abstract or qualify it identically to the body.

**P4-E3 (ESSENTIAL)**  
Abstract (p. 1) states “a Null Real-Space Chirality Dipole” as the title-level result. Body (Sec. VI.A, p. 12; Sec. VII, p. 14) concludes the real-space dipole is consistent with null only after TTA averaging and after discarding the harmonic-channel residual. The abstract therefore asserts a stronger claim than the body’s final, conditional statement.  
**Required fix**: Change title/abstract framing to “No evidence for a real-space chirality dipole above the 0.75 % injection-recovery floor after bias mitigation”.

**P4-M1 (MAJOR)**  
Throughout (e.g., Table I p. 5, Table III p. 11, Fig. 8 p. 10): multiple σ values from distinct null procedures (isotropic-bootstrap, label-shuffle, block-bootstrap, 10^4-permutation, monopole-only generative) are placed in adjacent columns or sentences. Although the paper occasionally adds the qualifier “not directly comparable,” the qualifier is absent at several juxtapositions (Table I rows (i)–(iii), Table III ℓ=1 row). Instruction 7 requires the qualifier at every juxtaposition.  
**Required fix**: Insert the explicit sentence “These σ values arise from distinct null procedures and are not directly comparable as detection significances” immediately above every table or figure panel that mixes them.

**P4-M2 (MAJOR)**  
Paper length = 23 pages (including 5 appendices). The central scientific claim is a null result plus a systematics audit. PRD norms for a methods/null-result paper of this scope are 10–12 pages. The present length is disproportionate to the incremental advance over Jia et al. (2023) and Shamir (2012–2022).  
**Required fix**: Condense to ≤14 pages; move Tables VII–XI and Figs. 9–10 to supplementary material.

**P4-M3 (MAJOR)**  
Sec. II.B (p. 2) and Appendix B (p. 17): 66.5 % of training labels are CE-ResNet pseudo-labels. The paper acknowledges this but does not propagate the resulting label-noise covariance into the final dipole uncertainty budget. The quoted 0.41σ therefore lacks a complete systematic-error term.  
**Required fix**: Add a quantitative propagation of pseudo-label noise into the real-space dipole posterior (or demonstrate that it is sub-dominant to the quoted floor).

**P4-N1 (MINOR)**  
p. 1: “Dated: June 13, 2026”. Future date is inconsistent with submission.  
**Required fix**: Replace with actual submission date.

**P4-N2 (MINOR)**  
Fig. 1 caption (p. 3) and text (p. 2) contain the repeated phrase “canonical canonical-mask”. Typo.  
**Required fix**: Correct.

**P4-N3 (NIT)**  
Multiple figure captions refer to “artifact c11_…json”, “artifact c12_…json”. These are internal file names; they are not needed in a published caption.  
**Required fix**: Remove or replace with stable DOIs/zenodo tags.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a careful null result and an extensive systematics audit. However, the abstract over-states the strength and cleanliness of the null relative to the body’s own repeated qualifications; multiple σ values from incommensurable nulls are juxtaposed without the required qualifier at every location; the paper is substantially over-length for its incremental contribution; and the dominant training-label noise term is not propagated into the final cosmological uncertainty. These are not cosmetic issues. Until they are corrected the paper does not meet PRD standards for clarity, statistical rigor, and proportionality.