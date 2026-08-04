# ApJS portal kit — Paper IV v1.0.274

Prepared 2026-08-03. This is a copy/paste staging sheet, not evidence that the manuscript has been submitted.

## Portal metadata

- Desired journal: The Astrophysical Journal Supplement Series (ApJS)
- Scope rationale: a released 8.5-million-galaxy catalog, its validation and provenance contract, and a reference null analysis. This matches the ApJS scope for significant catalogs and reference compilations.
- Article type: Regular Article — Houston must confirm the portal's current label.
- Title: An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog
- Author: Houston Golden
- Affiliation: Independent Researcher, Los Angeles, California, USA
- Email / corresponding author: houston@hubify.com / Houston Golden
- ORCID: not present in project truth; Houston must enter or confirm omission.

### Abstract (source-exact TeX)

> We release observed chirality labels for $8{,}474{,}531$ DESI Legacy DR8 galaxies and test one primary high-confidence observed-label dipole. Starting from 949,584 high-confidence spirals, we exclude 59,515 rows marked \texttt{raw\_flip\_qc\_unsafe}, leaving 890,069 quality-controlled rows; 887,472 enter the supported-pixel fit and fixed-occupancy label-randomization null. The result is consistent with zero ($z_{\rm mom}=+0.635$, one-sided rank $p=0.23768$). A coverage-calibrated observed-label injection--recovery on this primary channel places a $95\%$ sensitivity upper limit $A_{95}^{\rm obs}\simeq0.98\%$ (full-amplitude); this is an observed-label sensitivity floor, not a physical parity-amplitude bound, which remains gated on the morphology transfer function. WLS and harmonic analyses use different supports or nulls and are retained only as systematics diagnostics. A classifier-injection forward model over $1.7\times10^{7}$ banked network passes excludes classifier confusion as the source of the residual handedness monopole ($0.0\%$ of the observed value) and localizes its origin upstream of the classifier, without resolving whether that origin is a true sky asymmetry or a DESI imaging systematic. A from-scratch, manifest-retained retrain of the GZ1-core classifier component validates on a provably training-disjoint high-confidence GZ1 sample (Cohen's $\kappa=0.97$); a composition-faithful CE-included retrain instead collapses to chance on chirality, so the historical CE-included accuracy is \emph{not} reproducible under honest ingestion, and the released catalog labels are unchanged. Spatial transfer calibration, a full joint likelihood, an independent matched-footprint estimator and a complete systematics-metadata sidecar remain open. The parity-even morphology observable yields no physical primordial-parity bound (that bound remains gated on the unresolved morphology transfer function).

### Suggested UAT concepts

Verified preferred labels in UAT v6.0.0. Houston must select 1–12 in the portal:

- Spiral galaxies
- Catalogs
- Galaxy classification systems
- Galaxy properties
- Large-scale structure of the universe
- Observational cosmology
- Astrostatistics techniques
- Sky surveys

## Upload inventory and immutable bindings

Upload the flat contents of `paper4_arxiv_v1.0.274.tar.gz` (main file `chirality_catalog_paper.tex`): official `aastex702.cls`, 11 referenced figures, and the TeX source with inline bibliography. Do not upload the proof JSON as manuscript content.

| Artifact | SHA-256 | MD5 | Bytes |
|---|---|---|---:|
| `chirality_catalog_paper.tex` | `42c3cb34776a6159ef69fdc3c1b1c325b979e26eaf3edacb0b284e7ddc10c7c3` | — | 244,792 |
| `chirality_catalog_paper.pdf` | `2641a228af1e3decf17d18341570c4e779483a823267421fe041aade1375e0d7` | `6c7de2b81dfa3d7af2a7414214d57cfc` | 33,988,973 |
| `paper4_arxiv_v1.0.274.tar.gz` | `9503ddd1a3f8ebe42c2e1f26cc60c5f1fb71175023268636477af35f9d2be736` | — | 26,826,544 |
| `paper4_arxiv_v1.0.274.proof.json` | `4746006bafb1e8439d907b053d134c6c6fe001433d61f54f84f8c2423029a453` | — | 1,803 |

Staging status: AASTeX 7.0.2; line-numbered; the retained and served pdfTeX PDF is byte-identical across 16 mirrors. Separately, the exact 14-member extracted package compiles under Tectonic to 32 pages with zero errors, undefined references, or overfull boxes. All 32 canonical PDF pages were visually audited; all 47 unique embedded HTTP(S) targets returned 2xx; local repository artifact targets were cross-checked. The manuscript includes Data Availability, an AI-method disclosure, no-conflicts declaration, and no-external-funding declaration.

## Cover letter draft

Dear Editors,

Please consider “An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog” for publication in The Astrophysical Journal Supplement Series. The manuscript releases a large observed-label spiral-chirality catalog with explicit quality-control, immutable provenance, validation products, and a reference dipole-null analysis. Its primary result is null-consistent, and the manuscript sharply separates observed-label sensitivity from any physical primordial-parity inference. The catalog and reproducibility materials are publicly available as described in the Data Availability section. The manuscript is original, is not under consideration elsewhere, and the author takes full responsibility for its content. Thank you for your consideration.

Sincerely,<br>
Houston Golden

## Houston / portal-only completion checklist

- [ ] Confirm ApJS and the portal's article type/topical corridor.
- [ ] Enter ORCID, or confirm that leaving it blank is intended and permitted.
- [ ] Choose dual-anonymous review status and adjust the source if required.
- [ ] Confirm 1–12 UAT concepts and any portal keywords.
- [ ] Confirm originality/not-under-review wording in the cover letter before using it.
- [ ] Enter reviewer suggestions/exclusions and any editor note.
- [ ] Confirm conflict, funding, data-editor, license, publication-charge, and waiver responses.
- [ ] Update the existing Zenodo record so the current v1.0.274 bytes are archived; the manuscript states that the current patch is ahead of archived v1.0.268.
- [ ] Review the portal-generated proof and click Submit.
