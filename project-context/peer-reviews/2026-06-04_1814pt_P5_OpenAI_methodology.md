# P5 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 35.8s

---

Referee Report for P5: “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

================================================================
NB: “page X” refers to the PDF pagination visible on my copy.

FINDINGS
----------------------------------------------------------------
ESSENTIAL
----------------------------------------------------------------
P5-E1  (Sec. V B, p. 6)  
Problem  The primary estimator (DESIVAST void/non-void ∆fCW) was selected post-hoc: “the choice of which classifier to report as “primary” is therefore made post-hoc, and we declare it explicitly here…”.  This violates PRD policy that the key test statistic must be defined before looking at the data.  
Fix     A fully-specified analysis plan (including selection of primary estimator, all hyper-parameters, stopping rules and multiple-test control) must be deposited in a time-stamped public repository and the manuscript revised to demonstrate that the presented result follows it exactly, or the work must be reframed as exploratory with every quoted σ reduced to descriptive √N errors only.

P5-E2  (Abstract & Table I, p. 1 & 4)  
Problem  Median match separation is reported as 0.0066″, almost two orders of magnitude smaller than DESI’s 0.13″ median astrometric precision and one order of magnitude smaller than the 0.04″ public astrometry floor.  This is physically impossible and indicates a units bug (degrees mistaken for arc-sec?).  
Fix     Audit the cross-match code; report the separation distribution in consistent units; propagate any change to all match-count numbers and subsequent statistics.

P5-E3  (Sec. IV A, p. 3)  
Problem  V-Web classification is carried out in observed redshift space without RSD reconstruction but eigenvalue threshold λth = 0 is treated as a physical boundary.  No quantitative estimate of the class-misclassification rate induced by Kaiser + FoG anisotropies is propagated into σfrom-half.  
Fix     Either (a) repeat the V-Web run on a reconstructed real-space density field and re-derive all environment counts, or (b) propagate a mis-classification uncertainty term (e.g. Monte-Carlo on 20 reconstructed mocks) into every σ and update all significance statements.

P5-E4  (Tables II / VI / X, many pages)  
Problem  σfrom-half values are compared across mutually-incommensurable nulls: (i) exact binomial, (ii) permutation max-stat, (iii) Paper-IV monopole prediction.  The resulting mixed “σ” are plotted on the same axis and quoted in the text as if they are the same Gaussian σ.  
Fix     Quote each deviation in the native units of its own null; if you insist on σ, convert every null to the same variance definition and re-compute.  If not possible, remove direct σ comparisons.

P5-E5  (Throughout, e.g. Abstract, p. 2)  
Problem  The paper adopts the catalogue monopole ∆fCW = –0.0026 from Paper IV, which is “not yet peer-reviewed”, as if it were a fixed constant and then uses it to subtract 4–5σ from every measured class.  This imports an un-vetted systematic into PRD.  
Fix     Supply an internal blind cross-check (e.g. rerun the parity test on a pre-registered 5 % random hold-out of the images) that reproduces the 0.26 % monopole with quoted uncertainty, or express all results without subtracting the Paper-IV monopole.

P5-E6  (Sec. III A/B, p. 2–4)  
Problem  Several numbers do not self-consist:  
• nCW + nCCW + nNS = 28 592 + 398 043 + 1 440 577 ≠ 2 232 212.  
• In Table II nCW = 203 261 implies fCW = 0.4983, not 0.4980 as printed.  
Fix     Trace every scalar in Abstract and Conclusions back to the code; publish a machine-readable table of audited numbers.

P5-E7  (p. 16, “toy EFT mapping”)  
Problem  A parity-violating operator is introduced that explicitly breaks rotational invariance through the fixed vector ẑ.  The paper claims it is “a heuristic only” yet still uses it to set a numerical upper bound.  This is dimensionally and conceptually unsound.  
Fix     Either develop a proper gauge- and rotation-invariant operator and redo the mapping, or delete Appendix A entirely.

P5-E8  (body text search)  
Problem  Line-level review artefacts present, e.g. “R-upgraded-round9 close: 7 do-now fixes”, “v0.1.44 PER-M1 clarification”, “GPT-B2 closure”, “R-ext-GRO-M2”.  
Fix     Purge all internal version-history and review-log tokens.

----------------------------------------------------------------
MAJOR
----------------------------------------------------------------
P5-M1  (Sec. V, p. 5)  
Problem  σfrom-half is defined as (nCW − 0.5 N)/(0.5√N).  That denominator equals √(0.25N) – not the standard binomial σ = √[0.25/N].  The supplied σ’s are therefore inflated by √N/2, i.e. shown ~2× larger than conventional.  
Fix     Re-express all significances in standard units or defend the unusual scaling mathematically.

P5-M2  (Sec. VI D, p. 7)  
Problem  The bright–dark programme flip is reported at “|z|≈3.4σ” but the multiplicity of target-class × environment × density bins (>40) is never accounted for.  
Fix     Apply a global FDR or Šidák correction across the full space of sub-analysis cells and revise the quoted significance.

P5-M3  (Phase-2 Sweep, p. 9)  
Problem  Only Rs = 10,25,50 Mpc h⁻¹ are tested.  The abstract claims sensitivity down to 5 pp in voids, yet class fractions at Rs = 10 are dominated by smoothing aliasing (cell size 25.9 Mpc h⁻¹).  
Fix     Extend the sweep to at least Rs = 5 Mpc h⁻¹ or withdraw the sensitivity claim.

P5-M4  (Table IX, p. 13)  
Problem  HEALPix sky test uses cuts ≥ 200 spirals per pixel which removes >60 % of the sky and leaves the mask geometry highly irregular; the permutation null therefore under-estimates variance.  
Fix     Adopt a jack-knife in equal-area equal-population regions or use MASTER to debias.

P5-M5  (Data availability statement)  
Problem  GitHub path prefixes are given but no DOI, no commit hash, and the repository is presently private.  
Fix     Deposit the entire pipeline (code + configs + TAGGED container) on Zenodo or equivalent and supply DOI.

----------------------------------------------------------------
MINOR
----------------------------------------------------------------
P5-m1  (Title)  
“Three-Algorithm Test on 56,981 Void Spirals” understates that the main sample used elsewhere is 791,635 spirals.  
Fix  Retitle or clarify in first paragraph.

P5-m2  (Sec. III C)  
Ambiguous phrase: “Driver is …03_crossmatch.py” – unclear to readers without code.  
Fix  Annotate briefly what this script does in prose.

P5-m3  (Sec. IV B)  
Cell size 25.9 Mpc h⁻¹ is larger than smoothing Rs = 25; forward referencing confuses readers.  
Fix  Explain that the Gaussian kernel is applied in Fourier space and therefore not Nyquist-limited.

P5-m4  (Sec. VI A fig. 2 caption)  
Y-axis ticks labelled 0.43,0.44… but plotted range is 0.48–0.51.  
Fix  Correct figure.

P5-m5  Duplicate phrase “catalog-monopole catalog-monopole” appears once (p. 8).  
Fix  Delete duplicate.

----------------------------------------------------------------
NIT
----------------------------------------------------------------
P5-n1  Footnote symbol “∗” for author e-mail appears twice.  
P5-n2  Eq. (2) typesets erfc⁻¹ without argument brackets.  
P5-n3  Occasional spelling “per-galaxy GALZONE memebrship”.  
P5-n4  Missing comma after “Cautun et al. 2014” several places.

================================================================
Recommended maximum length
The current draft is 21 pages; after removal of internal log artefacts and the speculative EFT appendix, 17 pages is sufficient.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains interesting and potentially publishable work, but the statistical protocol is not yet rigorous enough for PRD.  In particular the primary estimator is chosen post-hoc, internal review tags remain, the DESI–chirality match units are inconsistent, and the dependence on an unpublished Paper IV monopole is unsafe.  Addressing the ESSENTIAL items (E1–E8) and the methodological MAJOR items (M1–M5) is mandatory before further consideration.