# ApJS portal submission kit — P3 v3.2.0-r14

Prepared 2026-08-03 from the current P3 source, PDF, source-bundle receipt, and
AAS official pages checked on that date. This is a portal working document, not a
submission record and not a readiness change. Houston's explicit sign-off remains
required before any upload or submission.

## 1. Exact artifact binding

| Item | Current binding |
|---|---|
| Venue | *The Astrophysical Journal Supplement Series* (ApJS) |
| Source | `paper3_apjs.tex` · v3.2.0-r14 · SHA-256 `5000b09d55191aaf858956e297dd2304ec1a20642ffd6b93c688f562b5b90a4e` |
| PDF | `paper3_apjs.pdf` · 17 pages · MD5 `e9c947e2c56d15851242e74330da93de` · SHA-256 `4b5a51949a9f91264e4ae4bf97fcd946997053d68d6a7343ab008156c094313b` |
| Source bundle | `project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r14.tar.gz` · SHA-256 `6ef3a614add20eba1f588d625a8555ad2f7d4ec78745b7005c1ecdfdd4cd9c3d` |
| Evidence receipt | `FINAL_PACKAGE_RECEIPT_v3.2.0-r14_2026-08-03.md` |

The receipt records a fresh 17-page clean-room build with zero undefined
references/citations. Its one 1.82327 pt overflow is below the 10 pt visual-risk
threshold and remains a Houston visual-review item.

## 2. Official entry points

- Submission information and the official portal link: <https://journals.aas.org/submission/>.
- Direct portal destination exposed by that official page: <https://aas.msubmit.net/>.
- Pre-submission checklist: <https://journals.aas.org/pre-submission-checklist-for-aas-journal-authors/>.
- Manuscript preparation and AASTeX guidance: <https://journals.aas.org/manuscript-preparation/>.
- Digital assets and machine-readable tables: <https://journals.aas.org/data-guide/>.
- Submission help: `journals.manager@aas.org`; data-asset help: `data-editors@aas.org`.

The official checklist says the portal asks for a desired journal and topical
corridor, digital-asset details, dataset information, financial information, and
1–12 Unified Astronomy Thesaurus (UAT) concepts. It also requires line numbers,
an abstract under 250 words, current author emails, and all uploaded files at one
directory level. Confirm the portal's live labels before choosing any dropdown.

## 3. Paste-ready metadata

**Desired journal:** `The Astrophysical Journal Supplement Series`

**Topical corridor / category:** choose the live portal option closest to
`Catalogs and surveys` / `Data analysis`; the literal corridor labels have not
been captured, so do not treat this wording as a portal value.

**Title:**

```text
Public-ID Recovery for a Historical DESI DR1 Anomaly List:
170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations
```

**Running title:** unresolved. The AAS preparation guidance asks for a ≤44-character
short title; no `\shorttitle` is currently present. Proposed text for Houston to
approve: `Public-ID Recovery for DESI DR1`.

**Author:** Houston Golden (sole author and corresponding author)

**Affiliation shown in the manuscript:** `Independent Researcher, Los Angeles, California, USA`.
The AAS guidance calls for a complete postal address including ZIP or country code;
confirm the portal's required form and add the appropriate postal detail if needed.

**Email:** `houston@hubify.com`

**ORCID:** `0009-0008-5616-5994` — confirm Houston wants this exact iD entered.
It is not currently printed in the P3 author block.

**Keywords from the current manuscript:**

```text
catalogs; surveys; methods: data analysis; methods: statistical;
galaxies: spectra; quasars: general
```

**UAT search terms (select only literal options returned by the portal):**
`astronomical catalogs`, `galaxy surveys`, `spectroscopic surveys`, `data analysis`,
`astronomical databases`, `large-scale structure of the universe`.

### Abstract — exact current text for the portal

This is transcribed from `paper3_apjs.tex` v3.2.0-r14; its source approximation is
244 words, under the AAS 250-word cap. Preserve the numbers and limitations exactly.

```text
We recover public identifiers for a frozen historical DESI anomaly list whose legacy
identifiers mixed public-looking values with internal hashes. The primary deliverable is
reusable, memory-bounded join and provenance/validation machinery; the 181-row catalog is its
first instance. The immutable clustering and BigAE lineage are documented; the unavailable
production normalization and physical-feature sensitivity are not. Streaming all 28,425,963
rows of the DESI Data Release 1 (DR1) redshift catalog in 200,000-row chunks against a k-d
tree of 190,015 clusters, a predeclared 1 arcsec match to a main-survey row with one of five
DESI_TARGET bits reproduces exactly 20,299,155 eligible DESI rows and 2,468 matches.
Requiring the global primary redshift row leaves 2,448; requiring ZWARN=0 leaves 181 unique
public TARGETID associations, forming the v3.2.0-r2 release audited in this v3.2.0-r14
manuscript: 170 high-coordinate-consistency core associations at or below 0.1 arcsec and 11
lower-confidence associations between 0.1 arcsec and 1 arcsec. Neither tier is a secure
object-identity or purity claim. Sixteen deterministic 60–120 arcsec local shifts yield 86.7
± 14.4 parent and 76.2 ± 13.3 warning-free-primary associations within 1 arcsec (versus 2,468
and 181 observed), and 75.6 ± 13.0 in the 0.1–1 arcsec annulus versus 11 observed, so that
tail is not treated as secure candidate-level identity. The sub-0.1 arcsec excess is the
expected self-recovery of the seed DESI members whose coordinates define the cluster centroids:
it verifies the recovery end-to-end rather than providing independent association evidence,
and the control is informative only for the 0.1–1 arcsec tail. These are reproducible follow-up
lists, not validated detections or unbiased samples for anomaly-rate inference.
```

## 4. Upload inventory

### Manuscript package — needs a flat, line-numbered portal copy

The current source tarball is valid for its stated source-package purpose, but **is
not yet an AAS portal-ready upload layout**: it contains `figures/` as a subdirectory
and the source uses `\documentclass[twocolumn]{aastex701}` without `linenumbers`.
The AAS checklist says subdirectories cannot be parsed and line numbers are required.

Before upload, create and inspect a new, paper-local portal staging directory with
every file at one level (do not alter this bound source bundle):

| Portal staging file | Current source |
|---|---|
| `paper3_apjs.tex` | current source after adding the required line-number option |
| `aastex701.cls` | current source bundle |
| `p3_v320_r6_chance_control.pdf` | `figures/p3_v320_r6_chance_control.pdf` |
| `p3_v320_selection_waterfall.pdf` | `figures/p3_v320_selection_waterfall.pdf` |
| `p3_v320_catalog_overview.pdf` | `figures/p3_v320_catalog_overview.pdf` |

Update the three `\includegraphics{figures/...}` paths only in that staging copy,
compile it, and run the normal LaTeX visual audit before upload. Do not upload the
current non-line-numbered PDF as the reviewer manuscript.

### Digital assets, data, and code

| Asset | Portal description / link |
|---|---|
| Machine-readable catalog | 181 rows × 43 columns: `aas_submission_v3.2.0-r4/tab3.tsv`, with `ReadMe` and `AAS_DIGITAL_ASSET_MANIFEST.json`. The verified aggregate bundle is `apjs_submission_bundle_v3.2.0-r7`. |
| Primary public release | Hugging Face: <https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog>, correction tag `p3-v3.2.0-r2`, immutable commit `1a9e85ee004894956665444b4f110111f1090b79`. |
| Submission/data bundle | <https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine/apjs_submission_bundle_v3.2.0-r7> — manifest, SHA-256 sums, table, software, controls, and lineage. |
| Code | <https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine/scripts>. |
| Public DESI input | <https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/>. |
| Archival deposit | Zenodo version DOI <https://doi.org/10.5281/zenodo.21461888>; concept DOI <https://doi.org/10.5281/zenodo.21461887>. These bind reviewed r10 bytes, not the current r14 manuscript. |

The AAS digital-asset DOI is **pending** and must not be entered as a minted DOI.
Ask the data editor whether the full-table upload should be a flat `tab3.tsv` as
currently prepared or a portal-renamed `tab3.txt`; do not rename or change its
manifest unilaterally.

## 5. Cover-letter draft

```text
Dear ApJS Editors,

Please consider the enclosed manuscript, “Public-ID Recovery for a Historical DESI
DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence
Positional Associations,” for publication in The Astrophysical Journal Supplement
Series.

The manuscript documents a reproducible, memory-bounded recovery and validation
workflow for a frozen historical DESI anomaly list. Its principal release is a
181-row, 43-column public catalog: 170 high-coordinate-consistency associations and
11 explicitly lower-confidence positional associations. The manuscript distinguishes
reproducible follow-up lists from astrophysical detections, does not claim purity or
unbiased anomaly-rate inference, and supplies a checksum-bound machine-readable
table, code, controls, provenance, and public data links.

[Houston: confirm before sending that this work is original, is not under review
elsewhere, and has not been previously published; add any required funding,
conflict, prior-preprint, or related-manuscript statements.]

Suggested reviewers: [Houston to supply names and institutional rationales; do not
invent email addresses.]
Excluded reviewers/conflicts: [Houston to supply, if any.]

Sincerely,
Houston Golden
Independent Researcher, Los Angeles, California, USA
houston@hubify.com
```

## 6. Pre-click checklist — Houston-owned decisions highlighted

- [ ] Houston has given an explicit P3 v3.2.0-r14 sign-off. This remains the final
  readiness input and is not supplied by this kit.
- [ ] Bounded final-hash active-leg confirmation is recorded as complete, or any
  confirmed regression has been resolved and the package rebound.
- [ ] Houston approves the live portal's ApJS topical corridor and UAT selections.
- [ ] Houston confirms the affiliation postal detail and whether to enter the listed ORCID.
- [ ] A flat, line-numbered staging package has been compiled and visually audited;
  its upload PDF has the expected title, author, version, figures, and references.
- [ ] The LLM-use acknowledgement/citation required by current AAS preparation
  guidance is reconciled with the P3 manuscript. No P3 AI/LLM disclosure section
  is present in the current source; do not certify compliance until this is resolved.
- [ ] Houston chooses normal review or the optional dual-anonymous-review route.
  If DAR is selected, anonymize all upload metadata/files and include the required
  author/affiliation/acknowledgment cover-letter material.
- [ ] Houston confirms the originality/exclusive-consideration statements in the
  cover letter and completes reviewer suggestions/exclusions without invented data.
- [ ] Houston identifies grants/funders, conflicts, prior-preprint status, and any
  DESI archive DOI/citation instructions requested by the portal.
- [ ] Fee, waiver/support request, author charge allocation, AAS membership discount,
  and account ownership are confirmed in the live portal. The official checklist
  says these are requested during submission; no amount or entitlement is assumed here.
- [ ] Data editor confirms the preferred flat machine-readable-table upload naming
  and the digital-asset declaration; journal digital-asset DOI stays `pending`.
- [ ] Houston performs the final portal review and clicks submit.

## 7. Status

**Ready now:** exact final PDF/source bindings, source-package receipt, current
metadata/abstract, public data and code links, and a validated ApJS data bundle.

**Not ready to submit yet:** Houston sign-off; final-hash confirmation; a flat
line-numbered reviewer package; LLM-use acknowledgement reconciliation; the live
portal's corridor/UAT/DAR/financial/data-upload selections; and Houston-supplied
reviewer/conflict/originality information.
