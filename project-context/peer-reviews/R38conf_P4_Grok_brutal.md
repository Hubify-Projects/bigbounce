# P4 R38conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v183.pdf` md5=34b06870 pages=23
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 336.5s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (Golden, 2026)

**Journal:** Physical Review D

**Recommendation basis:** The manuscript contains multiple fatal deficiencies that place it below the acceptance threshold for PRD. The most severe are (i) pervasive internal-audit artifact language that renders the text non-publishable as submitted, (ii) non-self-contained arguments that rely on unreleased companion artifacts and undefined symbols, (iii) abstract claims that are quantitatively stronger than, or lack the caveats present in, the body, and (iv) inconsistent or untraceable numerical claims. These are not cosmetic; they violate PRD standards for reproducibility, clarity, and honesty of presentation.

**ESSENTIAL findings (paper cannot be accepted without correction)**

- **P4-E1 (Title page, p. 1)**: The phrase “(Dated: June 13, 2026 — v1.0.183)” is version-control bookkeeping that has no place in a journal submission. Required fix: remove entirely.
- **P4-E2 (Throughout, e.g. pp. 2, 4, 9, 15, 16, 19, 21)**: Repeated internal artifact paths of the form “pipelines/p2_chirality/outputs/…” and “artifact c12_r24conf_local_batch.json” appear in the main text, figure captions, and tables. These are internal audit tags, not scientific content. Required fix: excise every instance; replace with stable, public DOIs or archive references only.
- **P4-E3 (Abstract, p. 1; body p. 4)**: Abstract states “the largest chirality-labeled galaxy catalog to date: 8,474,531”. Body never demonstrates this is larger than all prior published catalogs after identical quality cuts; the claim is unsupported. Required fix: either prove the statement with a table of prior N or remove the superlative.
- **P4-E4 (Abstract, p. 1)**: “primary scientific result is a real-space chirality dipole consistent with null” is presented without the body’s explicit qualifier that the result is estimator-specific and that the harmonic channel is a separate diagnostic. The abstract is therefore stronger than the calibrated body statement. Required fix: rewrite abstract sentence to match the final calibrated claim on p. 14.
- **P4-E5 (Sec. IV C, p. 7; Table I, p. 5)**: Multiple σ values from distinct null procedures (isotropic-bootstrap, label-shuffle, depth-stratified, monopole-only) are placed side-by-side in the same table and text without the mandatory qualifier “not directly comparable” at every juxtaposition. Violates instruction 7. Required fix: insert the qualifier in every location or recompute all entries on a single, explicitly justified null.
- **P4-E6 (Sec. II B, p. 2; Appendix B, p. 17)**: Training labels are stated to be 66.5 % from CE-ResNet predictions; the GZ1 cross-match accuracy (69.91 %) is given only after the fact. The argument is not standalone; a reader cannot evaluate label contamination without the companion CE-ResNet paper. Required fix: make the paper self-contained or move all label provenance to a citable, frozen public release.
- **P4-E7 (Fig. 8 caption, p. 10; Table III, p. 11)**: The caption claims the ℓ=1,2 broadband excess is “systematics-attributed structure analyzed in Appendix D”, yet Appendix D never quantifies the fraction of power removed by each of the eight listed tests. The figure is therefore not supported by the text. Required fix: supply the missing decomposition or remove the claim.

**MAJOR findings (significant revision required)**

- **P4-M1 (Abstract, p. 1; Sec. VI A, p. 12)**: The 50 %-recovery threshold A₅₀ ≈ 0.75 % is quoted in the abstract but derived only on the HC-broad subsample (N=949,584). The full-sample equivalent is never stated. Effect-size statement missing (instruction 19).
- **P4-M2 (Sec. IV D, p. 9)**: The generative monopole-only null is said to “reproduce 99.32 %” of the raw pre-MASTER power. The binomial variance on that fraction is never propagated; the quoted residual (+1.69σ) therefore lacks an uncertainty.
- **P4-M3 (Fig. 4, p. 8; Sec. IV C, p. 7)**: The color scale of the Mollweide map is given in Aₚ units but the caption never states the conversion A = 2(f_CW – ½). Axis label is therefore dimensionally incomplete.
- **P4-M4 (Bibliography, multiple entries)**: arXiv IDs and journal years for Shamir (2012, 2020, 2022) and Jia et al. (2023) are given, but the quoted dipole amplitudes (∼2–4σ, ∼3 %) are not traceable to the abstracts or tables of those papers. Unsupported citation statistics.
- **P4-M5 (Sec. VII, p. 14)**: The paper is 23 pages long yet its central claim is a null result plus a systematics audit. PRD norm for a methods null-result paper of this scope is ≤12–14 pages. Overlength without commensurate new methodology.

**MINOR / NIT findings (address but paper can proceed)**

- Duplicate phrasing “canonical canonical-mask” appears once (p. 16). Typo.
- Several figure captions (Figs. 2, 6, 7) contain parenthetical artifact file names that survived the first editing pass.
- Table II reports f_CW to six decimal places while the binomial uncertainty is given only to three; inconsistent precision.

**Summary recommendation**

**REJECT**

The manuscript in its present form is not publishable in Physical Review D. It contains internal bookkeeping language, non-reproducible artifact references, abstract–body drift on the central null claim, and multiple untraceable quantitative statements. These deficiencies are not remediable by minor editing; they require a complete rewrite that removes every internal path, makes the argument self-contained, aligns the abstract with the final calibrated body text, and supplies missing uncertainties and effect sizes. Only after such a revision would the scientific content (a careful null result with quantified leakage channels) be evaluable on its merits.