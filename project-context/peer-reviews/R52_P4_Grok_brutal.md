# P4 R52 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 77.6s

---

**Referee Report**

**P4-E1 (ESSENTIAL)**  
Section: Abstract (page 1)  
Problem: Abstract states “the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies”. Body (page 5, Table I caption and Sec. IV A) gives exactly this number only after image-quality QA cuts on the parent 8,474,688-object sample. The abstract therefore reports a post-selection number as the headline catalog size without the qualifier present in the body.  
Required fix: Rewrite abstract sentence to “largest … catalog after quality cuts (8.47 M galaxies)” or move the raw parent number into the abstract.

**P4-E2 (ESSENTIAL)**  
Section: Abstract + Sec. III A (page 3)  
Problem: Abstract quotes “+0.41σ (moment-z …) … p = 0.31, 10⁴ isotropic-bootstrap null” and “z = 0.70, per-galaxy label-shuffle null” side-by-side. Sec. III A and every table caption explicitly warn these two numbers “are not directly comparable as detection significances”. The abstract juxtaposes them without repeating the warning.  
Required fix: Abstract must carry the identical qualifier at the point the two numbers appear, or report only the single declared primary estimator.

**P4-M1 (MAJOR)**  
Section: Entire paper (23 pages)  
Problem: A null-result systematics paper of this length exceeds typical PRD limits for a single observational methods claim. The core cosmological result is a sub-percent null; the bulk of the text is an eight-anchor internal audit.  
Required fix: Condense to ≤12 pages (main text + 2 figures/tables) or split into a short Letter + companion methods paper.

**P4-M2 (MAJOR)**  
Section: Sec. IV C (page 7) and Fig. 4  
Problem: The canonical-mask ℓ = 1 residual is reported as +3.64σ (label-shuffle) yet is labeled “not a cosmological detection”. No quantitative statement of the practical effect size (fractional monopole leakage amplitude) is given alongside the σ value, violating the effect-size requirement.  
Required fix: Add explicit fractional amplitude (or equivalent) next to every headline σ.

**P4-M3 (MAJOR)**  
Section: Sec. VI A and Table V (page 13)  
Problem: The 50 %-recovery-at-3σ threshold A₅₀ ≈ 0.75 % is derived from an axis-uniform injection grid on the HC subsample. The text never states whether this threshold remains valid under the actual spatially varying survey-depth mask used for the primary estimator.  
Required fix: Explicit recomputation of the recovery curve with the canonical N_all-weighted mask.

**P4-N1 (MINOR)**  
Section: Table I footnote a (page 5)  
Problem: f_sky = 0.4801 is quoted for the HC subsample while the main analysis uses f_sky = 0.49005. The two values are not cross-referenced in the table.  
Required fix: Add a one-line reconciliation.

**P4-N2 (MINOR)**  
Section: Fig. 7 caption (page 10)  
Problem: Color scale is labeled in f_CW units while the left panel title says “chirality sky maps … per-pixel CW fraction”. The numerical range [0.47, 0.53] is therefore ambiguous without an explicit conversion note.  
Required fix: State “color = f_CW” in the caption.

**P4-NIT1–NIT3**  
Minor typographic or reference-formatting issues (e.g., repeated “canonical canonical-mask” phrasing absent; citation years consistent; no duplicate phrases found).

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents a technically thorough null result backed by an unusually extensive internal systematics audit. However, three essential violations (abstract–body mismatch on catalog size and σ comparability, missing effect-size statements, and unjustified length for a null claim) together with one major methodological gap (recovery threshold under the actual mask) prevent acceptance in its current form. The paper cannot be published without the fixes listed above; once addressed it would meet PRD standards for a detailed methods null-result paper.