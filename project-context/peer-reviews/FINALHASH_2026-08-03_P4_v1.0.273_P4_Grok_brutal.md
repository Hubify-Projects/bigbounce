# P4 FINALHASH_2026-08-03_P4_v1.0.273 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3` [FALLBACK from grok-4]
**Input PDF**: `pipelines/p2_chirality/chirality_catalog_paper.pdf` sha256=88bb513284db6adf4c6cf22ee7e08be2787cf8c3ebf43ffdcc289f2d369cee05 pages=32
**Review packet(s)**: `b0613d1a5bb5ea83dcd34e68f602c4ee27565efecd4485c57384b17b6e2c67bc`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 359.1s

---

**Referee Report (Adversarial Review — APJS Catalog+Methods Standards)**

**P4-E1 (ESSENTIAL, p. 1, abstract & title page)**  
The rendered first page contains “DRAFT VERSION AUGUST 3, 2026”, “Version v1.0.273”, and the footer “Typeset using IAETEX twocolumn style in AASTeX7.0.2”. These are internal production tags. Required fix: complete removal of all draft/version strings, dates, and pipeline paths before any resubmission.

**P4-E2 (ESSENTIAL, throughout, e.g. pp. 2, 4–5, 7, 9, 11, 13, 16, 21)**  
Hundreds of occurrences of internal bookkeeping language: “raw_flip_qc_unsafe”, “pipelines/p2_chirality/outputs/g1_full_composition_manifest.json”, “seed 42”, “entry A1/A7/A10/A12 of Table 18”, “manifest-retained retrain”, “immutable model-repository receipt”, “Hugging Face dataset Smith42/galaxies”, “Zenodo 10.5281/zenodo.7167388”, “ce_resnet.present=false”, “R7/R8” implied by repeated provenance blocks. These are not acceptable in an ApJS article. Required fix: excise every script path, seed, commit hash, and internal-audit tag; replace with a clean Data Availability statement.

**P4-E3 (ESSENTIAL, abstract + p. 16 Eq. 7)**  
Abstract states “coverage-calibrated observed-label injection-recovery … A_95^obs ≃ 0.98% (full-amplitude)”. Body (Eq. 7 and surrounding text) explicitly qualifies the identical number as an *observed-label* floor, *not* a physical parity-amplitude bound. The abstract omits the qualifier. Required fix: rewrite abstract sentence to match body’s final calibrated wording exactly.

**P4-E4 (ESSENTIAL, Tables 2–3, 6–7, 9 and surrounding text)**  
Multiple distinct null procedures (fixed-occupancy label randomization, block-bootstrap, binomial-monopole, label-shuffle, max-statistic MC) are placed side-by-side with z or p values but without the explicit repeated disclaimer “not directly comparable across rows” at every juxtaposition. Required fix: insert the disclaimer in every table caption and every paragraph that reports more than one null family.

**P4-E5 (ESSENTIAL, p. 1 abstract + p. 7 Table 2 row (i))**  
Abstract headline “z_mom = +0.635, one-sided rank p = 0.23768” is recomputed correctly from the 10 000-draw fixed-occupancy null on the 23 633-pixel HC-RI mask, but the paper never states the exact mask definition and seed in the abstract itself. The reader cannot verify the quoted scalar without the internal ledger. Required fix: move the precise mask definition and null-array identifier into the abstract or delete the numerical claim.

**P4-M1 (MAJOR, length)**  
The manuscript runs ~32 pages (metadata note) for a single null result on one dipole amplitude. The contribution is a QC catalog release plus a demonstration that earlier 2–4 % signals were systematics. ApJS catalog papers of comparable scope are typically 8–12 pages. Required fix: condense to ≤14 pages or justify the length.

**P4-M2 (MAJOR, p. 2 and Table 13)**  
The paper repeatedly documents that the “historical CE-included accuracy is not reproducible under honest ingestion” and that the released Catalog C labels are unchanged from a non-reproducible training run. This directly undermines the scientific claim that the catalog is a reliable public resource. Required fix: either (a) re-train and re-release with a fully reproducible manifest or (b) withdraw the claim that the catalog supersedes prior work.

**P4-M3 (MAJOR, Figs. 4, 7 and Sec. 4.3)**  
The sky maps and dipole fits are shown only after the unsafe-row quarantine. No pre-quarantine map is provided, so the reader cannot judge the magnitude of the correction. Required fix: add the raw (pre-quarantine) A_p map as a supplementary figure.

**P4-M4 (MAJOR, Sec. 6.2 & Table 10)**  
Finite-grid injection scores are reported as “pilot” fractions (0.55–1.00) but are never converted into a calibrated physical-amplitude recovery curve with uncertainty. The paper therefore supplies no number that can be compared with a future physical-parity search. Required fix: provide the full transfer-function curve with 1σ envelope or remove all physical-amplitude language.

**P4-N1 (MINOR, p. 3 Fig. 1 caption)**  
Caption states “~62 % of the parent sample would leak into the spiral classification” without the parent sample size or exact selection function. Add the number.

**P4-N2 (MINOR, multiple tables)**  
Binomial σ values are quoted to 4–5 digits while the underlying counts are given only to 6 significant figures; rounding inconsistency. Standardize.

**P4-NIT1–NIT4**  
Minor typographic issues (duplicate “canonical canonical-mask” phrasing absent; axis labels on Fig. 8 are legible but use non-standard “A_p [%]” notation; several figure captions repeat “see text” without page reference). These are cosmetic.

**Summary recommendation**  
**REJECT**

The manuscript as rendered is an internal audit log, not a journal article. It contains pervasive draft tags, script paths, seed numbers, and unreproducible training records that violate every standard of a citable ApJS catalog release. The central scientific claim (a coverage-calibrated observed-label null at A_95^obs ≃ 0.98 %) is presented in the abstract without the explicit physical-bound caveat that the body itself insists upon. Multiple null families are compared without the required repeated disclaimers. Until the internal bookkeeping is removed, the reproducibility conflict is resolved, the length is reduced by more than half, and every abstract scalar is made independently verifiable from the displayed text alone, the paper does not meet ApJS standards.