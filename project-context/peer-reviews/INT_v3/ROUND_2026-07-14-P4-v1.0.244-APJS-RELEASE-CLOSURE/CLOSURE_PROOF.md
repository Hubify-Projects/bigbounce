# P4 v1.0.244 ApJS release closure proof

Status: **FULL LOCAL RELEASE-CANDIDATE CLOSURE PASS**

This round closes only the bounded P4 v1.0.243 truth-audit findings. It does not
claim that P4 has been submitted, accepted, archived, assigned a DOI, or upgraded
from an observed-label descriptive null to a physical or primordial constraint.

## Closed findings

- The science-facing release schema omits every raw-pass and reconstructed
  flip-pass score column. It retains only `raw_flip_qc_unsafe`.
- A separate provenance-only quarantine contains the expected 249,066 unsafe
  catalog rows, including 59,515 rows in the 949,584-row HC sample. Each row is
  marked `do_not_use_for_science=True`; none of its scores is calibrated.
- The machine schema, compact human data dictionary, safe filters, exact source
  receipt contract, tests, release builder, source-to-claim audit, and minimal
  primary-null reproducer are explicit.
- The paper prints the existing per-galaxy shuffle result and all six cells of
  the 2x3 weight/mask cross-null panel, including their null definitions.
- The three supports are consistently named `HC-REALSPACE-INCLUSIVE`,
  `FULL-SPIRAL-CANONICAL`, and `MASTER-ALL-GALAXY-FOOTPRINT`.
- Equation 4 now states `sigma(A_phys)=sigma(A_obs)/g` and explains that the
  scalar `g=0.398` is not a spatial transfer function and creates no physical
  bound. The abstract and release text state the ApJS catalog/methods fit.

## Verified gates before the full payload pass

- Focused release contract: **5/5 tests pass**, including same-size source
  corruption rejection and a hard gate that raw/reconstructed columns are absent.
- Source-to-claim audit: **PASS**, with every new numerical claim pinned to a
  committed evidence artifact and all prohibited scope escalations false.
- Exact final PDF: 26 pages, 34,064,141 bytes,
  SHA-256 `1b1a536dfbd7d07ea4958304d6694582ce3b5ec7d6ce16b08b5d17fdefc15669`.
- LaTeX/visual audit: **PASS**; zero errors, undefined references/citations, or
  overfull boxes; all 26 pages rendered and inspected with no margin, gutter,
  table, figure, title, or date collision.
- Exact-PDF URI audit: **PASS**; 115 annotations / 39 unique URIs, zero missing
  local targets and zero external failures. New local artifact URLs become
  remotely resolvable only after the same commit is pushed.

Machine receipts:

- `P4_v1.0.244_SOURCE_TO_CLAIM_AUDIT.json`
- `P4_v1.0.244_LATEX_AUDIT.json`
- `P4_v1.0.244_URI_AUDIT.json`

## Heavy-lane payload gate

The builder completed on 2026-07-15 in 39.72 seconds wall time. It first made a
fresh full SHA-256 pass over the 952,115,239-byte source and required the exact
digest
`e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563`.
It then made one streaming transform pass over all 8,474,531 rows. This was
honestly two sequential source reads: one identity pass and one transform pass.

All declared counts passed: 949,584 primary-HC rows; 249,066 quarantined rows
catalog-wide; 59,515 quarantined rows inside primary HC; and 890,069 strict-HC
rows. The science product contains no raw or reconstructed score column, every
quarantine row has the required reason code, and every quarantine row has
`do_not_use_for_science=True`.

Generated local/ignored payloads:

- Science-facing catalog: 386,712,994 bytes, SHA-256
  `139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3`.
- Provenance-only quarantine: 16,665,663 bytes, SHA-256
  `fb98787dd4c5d1a7a0fdb64fcdacd1b02bc2080ab3716c0a803e0ccdfec03fbe`.
- Retained 10,000-draw null: 80,128 bytes, SHA-256
  `62bb1c019231974c2a7ed5d5e43ceb77a5596e4675c82d7ff1c899e029a36492`.

The independent primary reproducer passed at $N=949{,}584$, 23,682 inclusive
pixels, $A_{\rm dip}=0.004597074287780103$, $z=+0.5491201934182964$, and
one-sided upper-tail rank $p=0.26517348265173485$. Its compact receipt SHA-256 is
`a1df09ac77c98f17ec76de752b1612d98aa2efff1e8ff372979eddb733dfcde9`.
The run exposed and closed a receipt-only serialization defect: NumPy boolean
gate values are now converted to built-in booleans before JSON emission. The
science result and payload bytes were unchanged.

Compact retained receipts in this directory are
`P4_v1.0.244_RELEASE_MANIFEST.json`,
`P4_v1.0.244_RELEASE_VALIDATION.json`, and
`P4_v1.0.244_PRIMARY_REPRODUCTION.json`. The large Parquet payloads remain local,
ignored, and unstaged.

## Scope guard

- Calibrated probability claim: **false**
- Physical or primordial bound: **false**
- Formal preregistration claim: **false**
- Matched external-estimator claim: **false**
- Immutable archive or DOI: **open**
- Site, SSOT, Convex, and global `version.json` changes in this closure: **none**
