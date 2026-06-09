# P4 R22prov — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (1841 chars)
**Wall time**: 62.5s

---

**P4-E1 (ESSENTIAL)**  
Page 1 (abstract), lines ~15–20: “Withdrawn note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ=1 null on a putative ‘strict-superset subsample mask’ … a provenance audit found that result was computed on a synthetic-footprint catalog and it is withdrawn”.  
This is internal review-log / version-history prose. Required fix: delete every sentence referencing prior versions, withdrawn results, provenance audits, or round identifiers. No such language belongs in a submitted manuscript.

**P4-E2 (ESSENTIAL)**  
Abstract (page 1) and Table I (page 4) juxtapose multiple σ values (0.43σ, 3.64σ, 7.28σ, etc.) from distinct null procedures. Although a general disclaimer exists, it is not repeated at every load-bearing comparison in the abstract or §IV C–D. PRD requires explicit “not directly comparable” qualification at each such juxtaposition. Required fix: insert the qualifier at every instance or remove cross-estimator numerical comparisons from the abstract.

**P4-E3 (ESSENTIAL)**  
Abstract claims “a null real-space chirality dipole” at +0.43σ (p=0.30) as the headline scientific result. The body (§IV C, page 6) shows this is obtained only after 2-fold TTA + MASTER deconvolution; the raw Catalog A dipole is 2.31σ. The abstract therefore mis-states what the pipeline actually measures before post-processing. Required fix: rewrite the abstract to state the raw result first and the post-processed null second.

**P4-M1 (MAJOR)**  
The manuscript is 15 pages (plus appendices) for a null-result systematics paper. PRD cosmology methods papers reporting a non-detection are routinely expected to be ≤8–10 pages. The extensive diagnostic sections (§IV D–E, Appendices C–E) largely repeat the same conclusion (monopole-mask leakage). Required fix: condense to ≤10 pages or justify the length.

**P4-M2 (MAJOR)**  
Figure 4 (page 7) and the associated MASTER band-power table (Table III) show the ℓ=1 residual is +7.28σ on the apodized footprint, yet the text repeatedly labels it “non-headline” and “systematics-attributed.” No quantitative test demonstrates that the same pipeline would recover an injected cosmological dipole of the amplitude claimed by Shamir et al. (~1.7–3 %). Required fix: add an end-to-end injection-recovery test on the real DESI footprint that quantifies completeness versus the claimed prior signals.

**P4-M3 (MAJOR)**  
The falsification criterion (§I, page 2) is defined at A95≈1.5–2 % for a future 5σ detection. No calculation shows how this threshold maps onto the present survey’s effective number of independent modes after mask and depth weighting. Required fix: derive the numerical threshold from the survey’s mode count and mask power spectrum.

**P4-N1 (MINOR)**  
Page 1 states “Dated: June 2026”. A submission date in the future is an artifact. Required fix: remove or correct.

**P4-N2 (MINOR)**  
Table I caption and footnote 1 contain inconsistent wording on whether Nmap weighted includes NS galaxies. The numerical value 8 474 531 appears without an explicit statement that it equals Σ Wp. Required fix: make the definition unambiguous.

**P4-N3 (NIT)**  
Several axis labels in Figures 4, 5, 7 use mixed capitalization (“Equatorial”, “log10”) and non-standard color-bar ranges. Required fix: enforce consistent style.

**Summary recommendation**  
REJECT

The manuscript contains multiple instances of internal review language that must be removed before any scientific evaluation can proceed (E1). Even after that excision, the abstract mis-represents the raw versus post-processed results (E3), cross-estimator σ values are presented without the required comparability caveats at every use (E2), and the paper is substantially over-length for its actual scientific payload (M1). The central claim—a clean null after bias hardening—is not yet supported by the quantitative injection test that would be mandatory for a PRD cosmology methods paper. These deficiencies are not cosmetic; they prevent a fair review.

---

## PASS 2 — self-critique findings (what initial review missed)

**P4-E4 (ESSENTIAL)**  
Abstract and §IV C both quote the headline dipole as “+0.43σ (p=0.30)” from an isotropic bootstrap (N_MC=10,000). The body text never states the exact bootstrap realization count used for the p-value itself; the only N_MC=10,000 reference is to a different test. Required fix: either recompute and report the p-value from the stated 10,000 realizations or remove the parenthetical p-value.

**P4-M4 (MAJOR)**  
§VI A states the Fisher Poisson floor at 3σ is “~0.29% full-amplitude (from σ(A/2)≈0.048%…)”. Direct recalculation from the binomial error on N_spiral=3,201,160 gives σ(f−0.5)=2.79×10^{-4}, hence σ_A=5.58×10^{-4} (0.0558%) if A≡2(f−0.5). The quoted 0.048% and 0.29% figures are therefore numerically inconsistent with the N_spiral value used everywhere else. Required fix: correct the arithmetic or define A explicitly.

**P4-m1 (MINOR)**  
Figure 7 caption claims the right-hand (Catalog C) map is “Catalog C (equivariant)”. The color bar is labeled in units of the per-pixel CW fraction, yet the body text (§IV B) and Table II report the same quantity only as a sky-averaged monopole. No per-pixel color-bar calibration is supplied, so the map cannot be read quantitatively against the quoted 0.4974 global fraction.

**P4-N4 (NIT)**  
Page 2, “Dated: June 2026” appears in the author block. A submission date 18 months in the future is an obvious artifact and must be removed.

**P4-N5 (NIT)**  
Table I row (v) lists “p_LEE ≤10^{-4}” while the caption states the null is “max-stat MC”. The two descriptions are not equivalent; the table entry is therefore ambiguous.

NO ADDITIONAL FINDINGS on dimensional consistency, internal cross-references, or appendix/main-text mismatch; those checks were clean. All new items above are arithmetic, caption-body, or presentation defects missed on the first pass.