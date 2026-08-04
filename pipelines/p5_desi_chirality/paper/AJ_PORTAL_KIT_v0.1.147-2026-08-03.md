# AJ portal kit — Paper V v0.1.147-2026-08-03

Prepared 2026-08-03. This is a copy/paste staging sheet, not evidence that the manuscript has been submitted.

## Portal metadata

- Desired journal: The Astronomical Journal (AJ)
- Scope rationale: an original observation-derived DESI DR1 analysis of galaxy chirality across catalogued cosmic environments, with explicit statistical and selection controls. This matches the AJ scope for significant observational results.
- Article type: Regular Article — Houston must confirm the portal's current label.
- Title: A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1
- Author: Houston Golden
- Affiliation: Independent Researcher, Los Angeles, California, USA
- Email / corresponding author: houston@hubify.com / Houston Golden
- ORCID: not present in project truth; Houston must enter or confirm omission.

### Abstract (source-exact TeX)

> We test whether \emph{classifier-labelled} spiral chirality differs between released DESIVAST~\cite{DESIVAST2025} void and non-void environments in DESI Data Release~1. The focal hybrid released-parent descriptive estimate intersects the companion Paper~IV catalog~\cite{golden_chirality_2026} with the released DESIVAST GALZONE TARGET universe ($694{,}642$ unique TARGETIDs), yielding $145{,}789$ joined rows. We retain the $145{,}766$ rows with \texttt{OUT}$=0$ as the quality parent and define the two arms by exact membership in the union of released VoidFinder holes: $31{,}937$ void and $113{,}829$ non-void. We standardize for redshift, imaging leg, magnitude, size, morphology, extinction, classifier confidence, and the GALZONE edge flag, with coarse sky blocks used as clusters. The focal adjusted non-void-minus-void contrast from a 13-column linear nuisance model is $\Delta f_{\rm CW}=+0.00145442$; a coarse HEALPix NSIDE$=4$ cluster-sandwich calculation gives ${\rm SE}=0.00331502$, 95\% CI $[-0.00504290,+0.00795174]$, and two-sided normal $p=0.66085$. A null-imposed 99,999-draw Rademacher wild-cluster efficient-score test gives $p=0.67345$. Overlap weighting gives the same qualitative result. The author-constructed VoidFinder any-hole sample ($N_{\rm void}=57{,}081$) and the T-Web, Tempel, and ASTRA analyses are sensitivity or secondary diagnostic paths rather than parallel focal measurements. This hierarchy was changed after review and after inspecting the data; the study remains exploratory, post-hoc, and not preregistered. T-Web intervals omit cosmic variance and spatial covariance, all environment assignments remain in redshift space, and a target-program-by-environment interaction is not excluded. The result is therefore a catalog-specific non-detection for classifier labels, not a physical-handedness, real-space, or cosmological constraint.

### Suggested UAT concepts

Verified preferred labels in UAT v6.0.0. Houston must select 1–12 in the portal:

- Spiral galaxies
- Galaxy environments
- Voids
- Cosmic web
- Redshift surveys
- Large-scale structure of the universe
- Observational cosmology
- Astrostatistics techniques

## Upload inventory and immutable bindings

Upload the flat contents of `paper5_aj_v0.1.147-2026-08-03.tar.gz` (main file `p5_desi_chirality.tex`): official `aastex702.cls`, nine referenced figures, and the TeX source with inline bibliography. Do not upload either proof JSON as manuscript content. The arXiv tar is byte-identical to the AJ tar.

| Artifact | SHA-256 |
|---|---|
| `p5_desi_chirality.tex` | `04741ad11fdd5c538fa16758e074f9d3beb4c0bba0a4148bcd6b1175d3c57cd4` |
| `p5_desi_chirality.pdf` | `4eee60aeca6226b699d37642b17401c8b19f833a44d3154c587f39e96d6751f1` |
| `paper5_aj_v0.1.147-2026-08-03.tar.gz` | `a6a444f0516a1e9702c0ea02fed9c39afc81c2def93001efbef568578d630b69` |
| `paper5_arxiv_v0.1.147-2026-08-03.tar.gz` | `a6a444f0516a1e9702c0ea02fed9c39afc81c2def93001efbef568578d630b69` |
| `paper5_aj_v0.1.147-2026-08-03.proof.json` | `ee2758f32b95bcbe83701a4eb7668cb08f1c8a8c3aed716323b412edc5ebf704` |
| `paper5_arxiv_v0.1.147-2026-08-03.proof.json` | `32325b8b86729e144b94188b2a400d120b2e9a15d359f7f80427407601c9d02e` |

Staging status: AASTeX 7.0.2; line-numbered; exact extracted package compiles to 46 pages with zero errors, undefined references, or overfull boxes; all 46 pages visually audited and all nine figures present. The manuscript includes Data Availability, DESI facility acknowledgments, an AI-method disclosure, and explicit caveats that no immutable public v0.1.147 tag or Paper V Zenodo DOI exists yet.

## Cover letter draft

Dear Editors,

Please consider “A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1” for publication in The Astronomical Journal. This manuscript tests a released-parent DESIVAST void/non-void contrast using public DESI DR1 and chirality-catalog inputs, with redshift, imaging, morphology, classifier-confidence, edge, and spatial-clustering controls. The focal adjusted contrast is null-consistent; the paper explicitly identifies the analysis as exploratory and post-hoc and does not interpret the result as a physical-handedness or cosmological constraint. Data, code, retained artifacts, and known reproducibility limits are described in the Data and Code Availability section. The manuscript is original, is not under consideration elsewhere, and the author takes full responsibility for its content. Thank you for your consideration.

Sincerely,  
Houston Golden

## Houston / portal-only completion checklist

- [ ] Create and verify the immutable public v0.1.147 Git tag and Paper V Zenodo DOI/snapshot, then replace the manuscript's explicit pre-submission placeholders and rebuild/re-audit before upload.
- [ ] Confirm AJ and the portal's article type/topical corridor.
- [ ] Enter ORCID, or confirm that leaving it blank is intended and permitted.
- [ ] Choose dual-anonymous review status and adjust the source if required.
- [ ] Confirm 1–12 UAT concepts and any portal keywords.
- [ ] Confirm originality/not-under-review wording in the cover letter before using it.
- [ ] Enter reviewer suggestions/exclusions and any editor note.
- [ ] Confirm competing-interest, author-funder/grant, data-editor, license, publication-charge, and waiver responses; do not infer author funding from the DESI facility acknowledgment.
- [ ] Review the portal-generated proof and click Submit.

