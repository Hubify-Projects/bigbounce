# P4 R29 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v172.pdf` md5=f6c1f145 pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 98.8s

---

**Referee Report — P4 (Round R29)**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (DESI Legacy DR8, 8.47 M galaxies)

**Overall assessment:** The manuscript contains an unacceptable volume of internal-audit language, version-control artifacts, and provenance scaffolding that have no place in a PRD submission. In addition, the central statistical claims rest on a chain of null procedures whose numerical outputs are repeatedly placed side-by-side without the required “not directly comparable” qualifier, and several headline numbers in the abstract cannot be recomputed from the displayed inputs without additional external files. These are not cosmetic problems; they are fatal to first-read acceptance.

### ESSENTIAL findings (paper cannot be accepted without correction)

**P4-E1** — Internal version-control and future-date language (title page, §I, throughout)  
Text: “Dated: June 10, 2026 — v1.0.172”, repeated references to “earlier version of this paper”, “withdrawn”, “superseded”, “R7”, “R8”, “manuscript revision v1.0.76”, commit hashes, and file paths such as `pipelines/p2_chirality/outputs/...`.  
Required fix: Remove every instance of internal versioning, audit tags, and future dates. Replace with a single submission date.

**P4-E2** — Non-comparable σ values juxtaposed without explicit qualification (Table I, Table III, §IV C, §IV D, abstract)  
The paper reports +0.41σ (isotropic bootstrap), +3.64σ (direct MC), +7.28σ (apodized), +7.93σ (permutation), etc., on the same page or in the same table without the sentence “these three values … are not mutually comparable” appearing at every such juxtaposition.  
Required fix: Insert the explicit qualifier at every occurrence; recompute and present only one primary null per estimator.

**P4-E3** — Abstract numbers not traceable to displayed body quantities (abstract, Table I, §IV C)  
Abstract states “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations)”. The body gives N = 949 584 for the HC subsample and 10⁴ isotropic realizations, but the exact moment-z calculation and the precise definition of the empirical-rank p-value are not shown; the reader must consult external JSON artifacts.  
Required fix: Provide a self-contained, recomputable derivation of every abstract scalar inside the main text.

**P4-E4** — Artifact file paths and JSON provenance statements embedded in the narrative (multiple locations, e.g., p. 2, 5, 7, 8, 10, 11, 15, 16, 18)  
Dozens of sentences contain strings such as “artifact c12_r24conf.local.batch.json”, “pipelines/p2_chirality/outputs/dipole/catalog_c_summary.json”, etc. These are internal bookkeeping, not scientific content.  
Required fix: Delete all such strings; move any necessary reproducibility information to a clean Data Availability statement.

**P4-E5** — Withdrawn-subsample and superseded-result language retained (p. 2, Appendix A)  
The text still discusses a “withdrawn” −0.122σ result and an earlier synthetic-catalog null.  
Required fix: Remove every reference to withdrawn or superseded analyses.

### MAJOR findings (significant revision required)

**P4-M1** — Length-to-contribution mismatch  
22 pages (plus appendices) for a null result plus a systematics diagnostic. PRD norm for a methods/null-result paper of this scope is ≤12–14 pages.  
Required fix: Condense to ≤14 pages or justify the length.

**P4-M2** — Non-independence of training labels (p. 2, §II B)  
66.5 % of training labels are CE-ResNet predictions; the GZ1 cross-match accuracy is only κ = 0.40. The paper repeatedly treats the catalog as “largest chirality-labeled” while acknowledging the labels are not independent.  
Required fix: State the effective independent sample size and propagate the label-noise floor into all significance claims.

**P4-M3** — MASTER ℓ = 1 channel presented as both diagnostic and null without clear separation (Table I rows iii–iv, §IV D)  
The same +3.64σ and +7.28σ numbers are used both to claim “systematics-attributed residual” and to argue the real-space dipole is null. The logical separation is not maintained.  
Required fix: Designate one channel strictly as a diagnostic and remove it from the primary cosmological claim.

**P4-M4** — Effect-size statements missing for all headline χ²/σ claims (abstract, §IV C, Table III)  
No Cramér’s V, fractional amplitude, or practical-significance metric accompanies any σ or p-value.  
Required fix: Add effect-size quantification for every quoted significance.

**P4-M5** — Abstract drift on “largest catalog” and “null dipole” claims (abstract vs. §IV A, §VII)  
Abstract asserts “largest … to date” and “consistent with null”. Body shows the catalog is 66 % CE-ResNet-derived and the null is estimator-specific.  
Required fix: Align abstract wording exactly with the final calibrated body statements.

### MINOR findings

**P4-m1** — Duplicate phrasing (“canonical canonical-mask”) on p. 11.  
**P4-m2** — Axis labels on Fig. 4 and Fig. 7 use inconsistent Aₚ vs. f_CW conventions without a conversion note in the caption.  
**P4-m3** — Several references list arXiv IDs but omit journal volume/page even when the paper has been published (e.g., ref. 20).  
**P4-m4** — Table II reports excess in percent but does not show the corresponding Aₚ amplitude in the same row.

### NITs (cosmetic)

- Inconsistent use of “CW/CCW” vs. “cw/ccw” in figure labels.  
- Occasional missing units on σ_null in Table III.  
- Figure 1 caption states “conf = 1.000” for every cutout; this is a display artifact, not a scientific claim.

**Summary recommendation: REJECT**

The manuscript in its present form is an internal working draft that has not been cleaned for external review. The combination of pervasive version-control language, non-recomputable abstract numbers, and repeated juxtaposition of non-comparable null statistics without the required qualifier constitutes multiple independent grounds for immediate rejection. A cleaned, shortened, and statistically self-contained resubmission could be reconsidered, but the current document does not meet PRD standards.