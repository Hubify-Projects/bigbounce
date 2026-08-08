# ApJS portal submission kit — P3 v3.2.0-r15

Prepared 2026-08-03 from the current P3 source, PDF, source-bundle receipt, and
AAS official pages checked on that date. This is a portal working document, not a
submission record and not a readiness change. Houston's explicit sign-off remains
required before any upload or submission.

## 1. Exact artifact binding

| Item | Current binding |
|---|---|
| Venue | *The Astrophysical Journal Supplement Series* (ApJS) |
| Source | `paper3_apjs.tex` · v3.2.0-r15 · SHA-256 `5ba0f87c6d7782d0fa1ae37cab9411c5460bbc5c429ace0c381f5ce731aa04e4` |
| PDF | `paper3_apjs.pdf` · pdfTeX canonical/served build · 495,346 bytes · 17 pages · MD5 `6659b909c928488873179ba71af8556d` · SHA-256 `793575f5705c421a3c75bfa2fe66b9f3c07aed327a2a75e01f835f952aee47ef` |
| Source bundle | `paper3_apjs_arxiv_v3.2.0-r15.tar.gz` · SHA-256 `14689637cdd7bb1ec89ab0907bebc382a57c6e9b96b4a3076a2f9b4394ba9fe7` |
| Flat portal staging | `apjs_portal_submission_v3.2.0-r15/` · checksum manifest SHA-256 `32652baf6033a45f653e9027a04cc4aee75ea95b3299c7ac148d5666c4254d54` |
| Evidence receipt | `FINAL_PACKAGE_RECEIPT_v3.2.0-r15_2026-08-03.md` |

The receipt separately retains the clean-room Tectonic/xdvipdfmx r15 checksum
(`ecbce4fdc12ff9348b89f0d4679e78d960042b5957d678ed9801579434e4fb49`;
MD5 `1622dd1810fb6bc4089f1d67f8d108a9`; 17 pages). The current canonical PDF
above is the pdfTeX artifact mirrored byte-for-byte to every served r15 path.
Both clean-room and flat-package builds have zero undefined references/citations;
the 1.82327 pt overflow is below the 10 pt visual-risk threshold and pages 1, 6,
and 8 were visually audited.

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

**Running title:** `Public-ID Recovery for DESI DR1` (present as `\shorttitle` in
the r15 source).

**Author:** Houston Golden (sole author and corresponding author)

**Affiliation shown in the manuscript:** `Independent Researcher, Los Angeles, California, USA`.
The AAS guidance calls for a complete postal address including ZIP or country code;
confirm the portal's required form and add the appropriate postal detail if needed.

**Email:** `houston@hubify.com`

**ORCID:** `0009-0008-5616-5994` (printed in the r15 author block). Confirm the
same iD in the live portal.

**Keywords from the current manuscript:**

```text
catalogs; surveys; methods: data analysis; methods: statistical;
galaxies: spectra; quasars: general
```

**UAT search terms (select only literal options returned by the portal):**
`astronomical catalogs`, `galaxy surveys`, `spectroscopic surveys`, `data analysis`,
`astronomical databases`, `large-scale structure of the universe`.

### Abstract — exact current text for the portal

This is transcribed from `paper3_apjs.tex` v3.2.0-r15; its source approximation is
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
public TARGETID associations, forming the v3.2.0-r2 release audited in this v3.2.0-r15
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

### Manuscript package — flat, line-numbered portal copy prepared

`apjs_portal_submission_v3.2.0-r15/` is the paper-local portal staging directory.
Every uploadable file is at one level; its source uses
`\documentclass[twocolumn,linenumbers]{aastex702}` and bundles the official
AASTeX 7.0.2 class. It compiled to 17 pages and passed the visual audit.

| Portal staging file | Current source |
|---|---|
| `paper3_apjs.tex` | r15 staging copy, with only its three figure paths flattened |
| `aastex702.cls` | official AASTeX 7.0.2 class |
| `p3_v320_r6_chance_control.pdf` | `figures/p3_v320_r6_chance_control.pdf` |
| `p3_v320_selection_waterfall.pdf` | `figures/p3_v320_selection_waterfall.pdf` |
| `p3_v320_catalog_overview.pdf` | `figures/p3_v320_catalog_overview.pdf` |

`SHA256SUMS` binds every staging file. Use this directory for upload; do not add
subdirectories or replace the source with a differently compiled copy.

### Digital assets, data, and code

| Asset | Portal description / link |
|---|---|
| Machine-readable catalog | 181 rows × 43 columns: `aas_submission_v3.2.0-r4/tab3.tsv`, with `ReadMe` and `AAS_DIGITAL_ASSET_MANIFEST.json`. The verified aggregate bundle is `apjs_submission_bundle_v3.2.0-r7`. |
| Primary public release | Hugging Face: <https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog>, correction tag `p3-v3.2.0-r2`, immutable commit `1a9e85ee004894956665444b4f110111f1090b79`. |
| Submission/data bundle | <https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine/apjs_submission_bundle_v3.2.0-r7> — manifest, SHA-256 sums, table, software, controls, and lineage. |
| Code | <https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine/scripts>. |
| Public DESI input | <https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/>. |
| Archival deposit | Zenodo version DOI <https://doi.org/10.5281/zenodo.21461888>; concept DOI <https://doi.org/10.5281/zenodo.21461887>. These bind reviewed r10 bytes, not the current r15 manuscript. |

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

- [ ] Houston has given an explicit P3 v3.2.0-r15 sign-off. This remains the final
  readiness input and is not supplied by this kit.
- [ ] Bounded final-hash active-leg confirmation is recorded as complete, or any
  confirmed regression has been resolved and the package rebound.
- [ ] Houston approves the live portal's ApJS topical corridor and UAT selections.
- [ ] Houston confirms the affiliation postal detail and the listed ORCID in the portal.
- [x] A flat, line-numbered staging package has been compiled and visually audited;
  its expected title, author, version, figures, and references are present.
- [x] The manuscript now contains an evidence-bounded AI/LLM-use acknowledgement:
  it names only reviewer legs retained in the P3 archive and assigns all scientific
  judgment and responsibility to the author.
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

**Ready now:** exact r15 PDF/source/tar bindings, current AASTeX 7.0.2 source,
line-numbered flat portal package, AI-use acknowledgement, current metadata/abstract,
public data and code links, and a validated ApJS data bundle.

**Not ready to submit yet:** Houston sign-off; final-hash confirmation; the live
portal's corridor/UAT/DAR/financial/data-upload selections; and Houston-supplied
reviewer/conflict/originality information.
