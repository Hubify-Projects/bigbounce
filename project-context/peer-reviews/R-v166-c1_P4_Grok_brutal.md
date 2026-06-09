# P4 R-v166-c1 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (1743 chars)
**Wall time**: 57.8s

---

**Referee Report – P4 (DESI chirality TTA null result)**

**P4-E1** (Abstract, p. 1)  
The abstract contains explicit version-history language: “Note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ=1 null on a putative ‘strict-superset subsample mask’ … and it is withdrawn”. This is internal audit/provenance text that has no place in a submitted manuscript.  
**Required fix:** Delete every sentence referencing prior versions, withdrawal, or provenance audits. No manuscript may contain review-log bookkeeping.

**P4-E2** (Abstract, p. 1; repeated p. 2)  
Multiple σ values obtained from qualitatively different null procedures (isotropic bootstrap, block-bootstrap WLS, per-pixel label-shuffle, depth-stratified, monopole-only generative) are presented side-by-side without the mandatory qualifier “not directly comparable” at every juxtaposition. Instruction 7 violation.  
**Required fix:** Insert the explicit qualifier at every numerical comparison or remove all cross-null numerical comparisons.

**P4-E3** (Abstract, p. 1)  
The headline claim “+0.43σ (p=0.30, isotropic-null bootstrap, N_MC=10,000)” is presented as the primary scientific result. The body (Table I, Sec. IV C) shows this is the real-space dipole fit on Catalog C after equivariant TTA. The same paragraph immediately juxtaposes it with a 1.7 % template-fit exclusion at z≈−18. These two statements are statistically incommensurate; the abstract therefore misleads.  
**Required fix:** Abstract must state only one primary null result and must not mix incompatible estimators.

**P4-E4** (Title + Abstract, p. 1)  
Title asserts “A Null Real-Space Chirality Dipole”. The measured amplitude is +0.43σ with p=0.30. A non-detection at <1σ does not constitute positive evidence for a null; it is merely consistent with null. Over-claiming.  
**Required fix:** Retitle to reflect an upper-limit or non-detection result.

**P4-E5** (p. 1, “Dated: June 2026”)  
Future date on a manuscript under review.  
**Required fix:** Remove.

**P4-M1** (Sec. I, p. 2; Sec. VII, p. 10)  
Paper length is 15 pages for a single null result whose headline significance is 0.43σ. PRD does not publish 15-page methodology papers whose principal conclusion is “no detection after systematics control”.  
**Required fix:** Condense to ≤6 pages or withdraw.

**P4-M2** (Table I, p. 4; Sec. IV D, p. 6)  
The monopole-only generative null is stated to reproduce “99.3 % of the observed pre-MASTER pseudo-C_ℓ power”. The table and text give no uncertainty on this percentage and no explicit statement that the 0.7 % residual is still +1.68σ. Inconsistent internal accounting.  
**Required fix:** Provide binomial uncertainty and recompute the residual significance.

**P4-M3** (Fig. 4 caption & Sec. IV C, p. 7)  
The Mollweide map is shown with an equatorial coordinate grid but no HEALPix N_side label on the figure itself. The caption claims N_side=64; the axis labels are unreadable at print resolution.  
**Required fix:** Add N_side label and ensure all axis quantities are legible.

**P4-N1** (multiple locations)  
Repeated use of the non-standard abbreviation “CW-vs-CCW” without first defining the acronym in the abstract.  
**Required fix:** Spell out on first use.

**P4-N2** (p. 2)  
“3.2 Million Spirals” in the title parenthetical does not match the body number 3,201,160. Minor rounding inconsistency.

**Summary recommendation**  
**REJECT**

The manuscript contains internal review-log prose that must never appear in a submitted paper (E1, E5). It systematically juxtaposes statistically incommensurate null estimators without the required qualification (E2). Its headline scientific claim is a sub-σ non-detection dressed as a positive “null dipole” result (E3–E4). The work is 15 pages long for a systematics-controlled upper limit whose central value is 0.43σ. These defects are fatal on first read; the paper does not meet PRD standards in its present form.

---

## PASS 2 — self-critique findings (what initial review missed)

**P4-E6** (Table I, p. 4)  
The final column is headed “\(\sigma\)” yet contains the non-\(\sigma\) entry “\(z \approx -18\)” for estimator (ii) and the non-\(\sigma\) entry “50%-rec-3\(\sigma\), \(A=0.75\%\)” for estimator (vii). Column contents are therefore dimensionally heterogeneous.  
**Required fix:** Split the column or relabel.

**P4-E7** (Abstract p. 1; Sec. IV C p. 7; Appendix D p. 12)  
The template-fit exclusion is repeatedly quoted at “\(z \approx -18\)”. No physical redshift can be negative; the symbol is either a mislabeled nuisance parameter or a typographical error.  
**Required fix:** Define the parameter or correct the sign.

**P4-M4** (Table II p. 5)  
The quoted deviation for Catalog C is given as 9.5\(\sigma\). Direct recomputation yields \(0.0026 / 0.000279 \approx 9.32\sigma\). The 0.18\(\sigma\) discrepancy is unreconciled.  
**Required fix:** Either recompute exactly or state the rounding convention.

**P4-N3** (Abstract p. 1)  
“CW-vs-CCW” appears without prior expansion. The acronym is never defined on first use.  
**Required fix:** Write “clockwise versus counter-clockwise (CW vs. CCW)” at first occurrence.

**P4-N4** (p. 2 line 3; Fig. 3 caption)  
Total galaxy count is stated as “8.47 M” while the exact figure is 8,474,531. The rounding is harmless but inconsistent with the precision given for the spiral subsample (3,201,160).  
**Required fix:** Adopt a uniform rounding convention.

NO ADDITIONAL FINDINGS on the remaining checklist items (equations are dimensionally consistent, cross-references match, figure captions agree with body text, appendices reproduce the quoted MASTER configuration, and no stale numerical pairs were located beyond the version-history text already flagged).