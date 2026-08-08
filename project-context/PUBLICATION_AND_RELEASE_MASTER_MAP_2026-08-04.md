# BigBounce publication and release master map

**Canonical plain-English map · 2026-08-04**

## One-sentence strategy

Publish three clear scientific stories, with the data, code, models, and
provenance needed to reproduce each story shipped alongside it—not inflated
into derivative papers—and preserve earlier artifacts as explicitly labelled
historical evidence where their lineage cannot be reproduced.

## The one-screen map

| Program | Lead scientific result | Specialist / companion work | Attached release |
|---|---|---|---|
| **Bounce theory** | **P2**: exact matter-contraction non-Gaussian amplitude | P1A theory boundary Note; P1B software metapaper | P1B code + receipts; P2 source/reproduction evidence |
| **DESI anomaly discovery** | **Rebuilt anomaly flagship**: reproducible DESI candidate populations | — | P3 public-ID recovery; rerun data, model, manifests, validation, and catalog |
| **Galaxy chirality** | **P4**: observed-label catalog and dipole null | P5: environment-dependence companion | P4 catalog/classifier/reproducer; P5 derived join/config/results |

**Endpoint:** six eventual standalone works—P2, P1A, P1B, the rebuilt anomaly
flagship, P4, and P5—plus **P3 as a citable supporting data/provenance release**.
The number follows the questions; it is not a quota.

## The six works and one supporting release

### 1. P2 — exact matter-contraction non-Gaussianity

- **Why / contribution:** lead bounce-theory paper deriving the exact
  four-vertex result `f_NL^local = -35/16` and its independently checked
  ordered coefficients.
- **Does not claim:** a detection, a complete bounce model, or an unconditional
  observational forecast.
- **Venue / status:** *Physical Review D* research article; v1.7.130 is at
  95/100 pending Houston approval. Kit:
  [`SSOT/PRD_SUBMISSION_KIT_P2_2026-07-24.md`](SSOT/PRD_SUBMISSION_KIT_P2_2026-07-24.md).
- **Ship with:** source package, derivation/reproduction material, and the
  existing Zenodo record [10.5281/zenodo.21461881](https://doi.org/10.5281/zenodo.21461881)
  versioned to the exact approved final candidate before submission.
- **Next gate:** Houston approval, then portal metadata and submission.

### 2. P1A — algebraic Cartan elimination

- **Why / contribution:** a narrow, convention-audited boundary result for
  minimal Einstein--Cartan--Holst gravity after eliminating the non-propagating
  connection.
- **Does not claim:** a dark-energy model, a universal torsion no-go theorem,
  or an empirical discovery.
- **Venue / status:** *Classical and Quantum Gravity* Note; v1A.0.127 is
  95/100 pending Houston approval. Kit:
  [`SSOT/CQG_SUBMISSION_KIT_P1A_2026-07-24.md`](SSOT/CQG_SUBMISSION_KIT_P1A_2026-07-24.md).
- **Ship with:** final source/PDF and the existing Zenodo record
  [10.5281/zenodo.21481838](https://doi.org/10.5281/zenodo.21481838).
- **Next gate:** Houston approval, then ScholarOne submission.

### 3. P1B — `namaster-proof`

- **Why / contribution:** a reusable verification library preventing two
  concrete pseudo-`C_ell` failures: shortcutting complete NaMaster windows and
  breaking the binding between result bytes and execution receipts.
- **Does not claim:** a real-sky measurement or a second bounce-physics result.
- **Venue / status:** *Journal of Open Research Software* software metapaper;
  v2B.0.16 is 95/100 pending Houston approval. Kit:
  [`SSOT/JORS_SUBMISSION_KIT_P1B_2026-07-24.md`](SSOT/JORS_SUBMISSION_KIT_P1B_2026-07-24.md).
- **Ship with:** installable [`packages/namaster-proof`](../packages/namaster-proof),
  tests/examples, reproducibility receipts, and software DOI
  [10.5281/zenodo.21481753](https://doi.org/10.5281/zenodo.21481753), alongside
  the paper archive [10.5281/zenodo.21481842](https://doi.org/10.5281/zenodo.21481842).
- **Next gate:** Houston approval plus three real reviewer names/emails and an
  APC/waiver decision.

### 4. Rebuilt DESI anomaly-science flagship

- **Why / contribution:** the lead discovery paper will answer which DESI
  candidate populations survive a reproducible, SNR-aware anomaly selection
  and external-catalog follow-up. Its intended centerpiece is a manifest-bound
  selected sample, taxonomy, per-class validation, and named follow-up cases.
- **Does not claim yet:** a submission-ready catalog, a reconciled historical
  anomaly count, confirmed discoveries, a universal false-positive rate, or an
  `f_NL` improvement.
- **Venue / status:** future primary discovery/catalog article; no approvable
  manuscript and no selected journal until the clean rerun produces its
  evidence base.
- **Ship with:** immutable public-ID input manifest; locked model, scaler,
  code, shard/checkpoint and deduplication receipts; row-level new catalog;
  selection/taxonomy code; held-out and per-class injection validation; and P3
  provenance material.
- **Next gate:** execute the fail-closed contract at
  [`pipelines/p1_highz_tracers/clean_rerun_contract.md`](../pipelines/p1_highz_tracers/clean_rerun_contract.md),
  then draft only from the new auditable sample.

### 5. P4 — observed-label chirality catalog and dipole null

- **Why / contribution:** the lead chirality result releases labels for
  8,474,531 DESI Legacy DR8 galaxies and tests a declared quality-controlled
  observed-label dipole, consistent with zero.
- **Does not claim:** calibrated true spin, a physical primordial-parity bound,
  or resolution of the upstream label asymmetry.
- **Venue / status:** *ApJS* catalog/methods article; v1.0.274 is 95/100
  pending Houston approval. Kit:
  [`pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`](../pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md).
- **Ship with:** the safe catalog, raw/flip quarantine, strict null array,
  morphology sidecar, schema/validator, classifier checkpoint and executable
  reproducer. Public provider roots are
  [dataset](https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog)
  and [model](https://huggingface.co/bamfai/galaxy-chirality-v2); archive record
  [10.5281/zenodo.21461899](https://doi.org/10.5281/zenodo.21461899) must be
  refreshed to the v1.0.274 bytes after approval.
- **Next gate:** Houston approval, immutable-provider/Zenodo refresh, then
  portal submission.

### 6. P5 — chirality--environment null test

- **Why / contribution:** a distinct, catalog-native DESIVAST void/non-void
  test using P4 labels, with selection and spatial controls; its focal contrast
  is null-consistent.
- **Does not claim:** preregistration, a physical-handedness measurement, a
  real-space result, or a cosmological constraint.
- **Venue / status:** *Astronomical Journal* companion article; v0.1.147 is
  95/100 pending Houston approval. Kit:
  [`pipelines/p5_desi_chirality/paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md`](../pipelines/p5_desi_chirality/paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md).
- **Ship with:** versioned analysis configuration, input/derived join tables,
  provenance sidecars, result tables and figures, all bound to the P4 catalog
  version used.
- **Next gate:** Houston approval, immutable tag and first Paper V Zenodo
  snapshot/DOI, metadata back-patch, rebuild/re-audit, then AJ submission.

### Supporting release — P3: DESI public-ID recovery

- **Why / contribution:** recovers 181 warning-free public TARGETID
  associations (170 core + 11 lower-confidence) for a historical anomaly list
  and binds the recovery to executable provenance.
- **Does not claim:** detector validation, anomaly rate/purity, classification,
  or replacement of the original anomaly-discovery survey.
- **Status / ship with:** v3.2.0-r17 technical package is complete; its receipt
  is [`pipelines/p3_anomaly_engine/FINAL_PACKAGE_RECEIPT_v3.2.0-r17_2026-08-03.md`](../pipelines/p3_anomaly_engine/FINAL_PACKAGE_RECEIPT_v3.2.0-r17_2026-08-03.md).
  It ships inside the rebuilt flagship's data/provenance release, not to ApJS as
  a standalone slot.
- **Next gate:** bind the recovery package and its existing Zenodo lineage
  [10.5281/zenodo.21461888](https://doi.org/10.5281/zenodo.21461888) to the new
  flagship's immutable release.

## Dependency and release rules

```text
P2 ── independent theory result
P1A ── independent boundary Note
P1B ── independent software release

clean DESI rerun ──> anomaly flagship ──> P3 provenance release attached

P4 catalog + classifier ──> P5 derived environment analysis
```

1. **No derivative-paper inflation.** P3, model checkpoints, catalogs, code,
   figures, tables, and validation receipts are releases cited by their lead
   paper unless they answer a new, independently reviewable scientific question.
2. **Historical anomaly material stays historical.** The frozen 195,829-row
   DESI table, the 2,145/1,127 downstream tables, and the archived BigAE
   checkpoint are useful comparison/provenance artifacts. The enhanced parent,
   its 46 Parquets, calibration and selection lineage are missing or
   unreconciled; no historical count becomes the new flagship's headline.
3. **No standalone P3 or old multi-survey ApJS route.** The old P3
   `DATA_RELEASE_MANIFEST.md` describes a superseded multi-survey scope and
   must not be used as current publication guidance.
4. **P4 and P5 release metadata need repair, not new papers.** The P4 provider
   READMEs still describe v1.0.244-era payload/state while the paper is v1.0.274;
   refresh them atomically with the approved final release. The root P5 README
   still says “Bootstrap” despite the current final package; replace it with the
   final-package status when the P5 archive is minted.

## Submission and release order

1. Houston review: **P2 → P1A → P4 → P1B → P5**. A specific `APPROVE` moves
   only that work from 95 to 100.
2. After each approval, complete that work's atomic release bundle immediately;
   do not hold approved papers for the slow anomaly rerun.
3. Run the clean DESI rerun in parallel; submit the rebuilt flagship only after
   its new catalog, validation, and release contract are complete.

## Why these venues fit

- **P2 → Physical Review D:** PRD explicitly covers gravity, cosmology, and
  astrophysics, and accepts full research articles. This is the right home for
  the program's lead exact theory result rather than splitting its conditional
  forecast material into another paper.
- **P1A → Classical and Quantum Gravity:** CQG covers gravitational physics
  and spacetime broadly; a focused Note matches P1A's narrow algebraic boundary
  better than presenting it as another full cosmology flagship.
- **P1B → Journal of Open Research Software:** JORS is designed for short
  software metapapers whose subject is open, usable research software. That is
  exactly P1B's role.
- **P4 → Astrophysical Journal Supplement Series:** ApJS explicitly publishes
  catalogs and large compilations, matching the 8.47-million-row observed-label
  release and its methods/audit contract.
- **P5 → Astronomical Journal:** AJ is appropriate for a distinct
  observation-derived astronomy analysis with its own controlled scientific
  question, rather than a catalog description.
- **Rebuilt anomaly flagship → decide after the result exists:** choose ApJS if
  the durable contribution is primarily a reference catalog/method, or AJ/ApJ
  if validated astrophysical populations and discovery interpretation become
  the scientific center. Do not select a venue to justify a paper before the
  clean rerun establishes what the paper actually is.

Official scope references: [PRD scope](https://journals.aps.org/prd/about) and
[author guidance](https://journals.aps.org/prd/authors),
[CQG scope](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-and-quantum-gravity/),
[AAS journal scope statements](https://journals.aas.org/scope-statements/), and
[JORS submission guidance](https://openresearchsoftware.metajnl.com/about/submissions).

### Atomic post-approval release bundle

1. Freeze source, PDF, data/code/model versions and hashes.
2. Create or update the immutable tag/provider revision and Zenodo version;
   retain the receipt and DOI.
3. Insert only the real identifiers, rebuild the exact submission PDF, and run
   package, link, and visual-PDF audits.
4. Publish the matching data/code/model release and update its README,
   citation, schema, license, and dependency pointers.
5. Update SSOT, Convex, site, submission kit, and public links in the same
   commit; then obtain the portal/arXiv/endorsement receipt separately.

## Naming rules

- Use **P2**, **P1A**, **P1B**, **P4**, and **P5** only for their standalone
  manuscripts; call the future anomaly article **Rebuilt DESI anomaly-science
  flagship** until it has a final title/ID.
- Call current P3 **Supporting Data Release · DESI Public-ID Recovery**.
- Describe P4 as an **observed-label** catalog/null and P5 as a
  **classifier-labelled** environment test; never imply physical parity/spin.
- Label unreproducible anomaly generations as **historical comparison
  artifacts**, never as the current release or submission sample.

For readiness, exact PDF links, and Houston decisions, use the
[`SSOT/FINAL_APPROVAL_SUBMISSION_BOARD_2026-08-03.md`](SSOT/FINAL_APPROVAL_SUBMISSION_BOARD_2026-08-03.md)
and [`SSOT/HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md`](SSOT/HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md).
