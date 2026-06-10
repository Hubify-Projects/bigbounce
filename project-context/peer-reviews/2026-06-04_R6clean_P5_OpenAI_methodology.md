# P5 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 56.4s

---

Referee report — PRD methodology audit  
Manuscript: “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

────────────────────────────────────────
FINDINGS
────────────────────────────────────────

ESSENTIAL

ID P5-E1  
Sec. VI A, p. 5 (table II and surrounding text)  
Problem “σpred = 2·ΔfCW·√N” is treated as an error-free reference although ΔfCW = –0.0026 ± 0.000279 is quoted (Paper IV). The uncertainty on ΔfCW is never propagated into σpred or into any subsequent σvs monopole residuals, yet those residuals are used as deciding criteria.  
Fix Propagate the quoted ±0.000279 uncertainty through eq. (1) to obtain σpred ± δσpred and include it in every residual test. Re-evaluate all “within 1.15 σ” or similar statements with the full propagated error.

ID P5-E2  
Sec. IV, p. 3 & App. C discussion of RSD; Sec. XI, “Limitations”  
Problem The V-Web classification is performed in observed redshift space. The manuscript acknowledges that anisotropic RSD can shift tidal-tensor eigenvalues but provides only a heuristic 3–5 % cell-crossing estimate without any quantitative propagation into fCW. No reconstruction or mock-catalog test is supplied, yet the V-Web classes drive every headline σ number appearing in the abstract.  
Fix Provide a reconstructed-position rerun (standard Zel’dovich or BAO reconstruction) of the V-Web grid and show that the class membership of the 791 635-spiral sample is stable, or else propagate an RSD-induced systematic into every σ value.

ID P5-E3  
Sec. VIII B, p. 10 (DESIVAST void test)  
Problem Membership is decided by a point-in-sphere test against the 101 863 VoidFinder “holes”. This ignores the DESIVAST catalog’s ZONE/EDGE/DEPTH flags and therefore double-counts galaxies lying inside truncated spheres that are outside the actual mask-limited void volume. The “nvoid = 56 981” statistic is thus not identical to the DESIVAST void population advertised.  
Fix Re-compute void membership with the catalog-native GALZONE and ZONEVOID flags (the method already used later in §VIII D) and report the corrected nvoid and fCW. Make this the primary void statistic.

ID P5-E4  
Sec. VI D, p. 6 (density-quartile follow-up)  
Problem The wall and void quartiles are treated as independent when the same galaxies appear in multiple quartiles in projection. The binomial formula implicitly assumes independence, biasing σ.  
Fix Use disjoint three-dimensional density bins or supply a bootstrap with galaxy-level resampling that respects the sample overlap.

ID P5-E5  
Sec. IX A, p. 14 (Tempel FoF cross-check)  
Problem The Tempel catalogue stops at z = 0.2 whereas the matched V-Web set reaches z ≈ 3.8, but no redshift-matched control is applied. The 0.026 pp “concordance” therefore mixes different underlying redshift distributions and cannot be interpreted as a like-for-like cross-validation.  
Fix Repeat the comparison after restricting the V-Web sample to z ≤ 0.2.

ID P5-E6  
Several places (example: p. 3 “χ2 = 4932, p < 10–1000”)  
Problem P-values smaller than the floating-point machine precision are reported (“p < 10-1000”). These numbers cannot be reproduced and constitute a numerical overclaim.  
Fix Quote p-values only down to the resolution allowed by the number of Monte-Carlo realisations or by double precision (≈10-16), e.g. “p < 10-16”.

ID P5-E7  
Entire paper (abstract, §V, §VI, tables)  
Problem σ values obtained from different null procedures (binomial half-null, Paper IV monopole-null, permutation max-stat null) are displayed on the same numeric scale without systematic separation. This violates instruction #7.  
Fix Whenever σ is computed relative to different reference distributions, label the scale explicitly (e.g. σ½, σmono, σperm) and never plot or tabulate them side-by-side without that label.

MAJOR

ID P5-M1  
Abstract & §II B  
Problem The primary estimator (“DESIVAST-anchored void/non-void ∆fCW”) is chosen post-hoc; the data themselves motivated the switch from V-Web void to DESIVAST. This garden-of-forking-paths problem inflates false-positive control.  
Fix Provide a pre-analysis plan or a full accounting of every estimator inspected, with the corresponding multiplicity correction covering *all* choices, not just the DESIVAST subset.

ID P5-M2  
Sec. V A, p. 4 (Bonferroni)  
Problem The Bonferroni correction is used even when bin statistics are manifestly correlated (adjacent HEALPix pixels, overlapping density quintiles). This renders the stated significance thresholds non-conservative or ill-defined.  
Fix For each family of correlated tests supply an empirical max-stat permutation threshold; do not quote parametric Bonferroni in those cases.

ID P5-M3  
Tables III & IV  
Problem Reported σpred uses ∆fCW = –0.0026 from Paper IV as an exact value, yet Paper IV is “not yet peer-reviewed.” The uncertainty of the external input must be included or the bias treated as unknown.  
Fix Either propagate the Paper IV uncertainty or re-measure the monopole on the matched sample directly.

ID P5-M4  
App. A (toy EFT mapping)  
Problem Presents an apparent constraint “|gϕ ∇ϕ|/H0 ≲ 10-2” but then states it is “not a derived constraint.” Mixing speculative interpretation with results section misleads readers.  
Fix Remove the numerical bound or move the entire discussion to a clearly marked speculative outlook without giving numbers.

MINOR

ID P5-m1  
Sec. III D, p. 2, Table I heading  
Problem “p50 separation 0.0066′′” but the acceptance radius is 1.0″; four significant figures are unnecessary.  
Fix Round to two significant figures.

ID P5-m2  
Sec. V B, “deterministic-seed: 20260515”  
Problem The seed is not recorded in the public code repository as claimed; reproducibility breaks.  
Fix Commit the seed to the published config file.

ID P5-m3  
Sec. VIII F, p. 12 (σvs monopole table)  
Problem The table title omits units (σ is dimensionless).  
Fix Add explicit “dimensionless” in caption.

ID P5-m4  
Throughout: inconsistent spellings “filament/filament”, “VoidFinder/Void- finder”.  
Fix Standardise terminology.

NIT

ID P5-n1  
Duplicate phrase “catalog-monopole monopole-subtracted” appears p. 6.  
Fix delete duplicate word.

ID P5-n2  
Equation (2) missing “erfc−1” argument delimiter.  
Fix typeset properly.

ID P5-n3  
Reference [11] missing journal information (“in submission”).  
Fix update or cite arXiv only.

ID P5-n4  
Typos: “filamentary” spelled “filamentary” once, “survey-shell” hyphenation inconsistent.  
Fix copy-edit.

────────────────────────────────────────
Page-length assessment  
20 pages are reasonable for the scope; no reduction requested.

────────────────────────────────────────
## Summary recommendation  
MAJOR REVISIONS

While the internal arithmetic checks out, several methodological and statistical problems (propagation of Paper IV uncertainty, un-corrected RSD, post-hoc estimator choice, mixing of σ scales, impossible p-values) must be fixed before the manuscript meets PRD methodological standards.