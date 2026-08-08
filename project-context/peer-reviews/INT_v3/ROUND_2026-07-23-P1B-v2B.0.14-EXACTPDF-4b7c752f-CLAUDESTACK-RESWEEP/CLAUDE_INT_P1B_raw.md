# Claude INT raw report — P1B (paper1b_namaster_proof.pdf)

- Round: ROUND_2026-07-23-P1B-v2B.0.14-EXACTPDF-4b7c752f-CLAUDESTACK-RESWEEP
- Referee: Claude INT (Opus 4.8, 1M)
- Date: 2026-07-23
- Paper: "namaster-proof: Exact pseudo-Cℓ window inference and content-bound
  validation for reproducible spin-2 analyses"
- Declared: v2B.0.14, 6pp, JORS software metapaper
- Nature of round: routine confirmation-wave re-sweep — verify the three
  2026-07-22 closures landed and introduced no regression; flag anything new.

## Binding verification

- Bindings file sha256 (expected): 4b7c752f791a0199ca7262cb0baaca2f7ba470dfcde0b71d9be730166001a7c3
- On-disk `shasum -a 256 arxiv/paper1b_namaster_proof.pdf`:
  4b7c752f791a0199ca7262cb0baaca2f7ba470dfcde0b71d9be730166001a7c3
- Result: **MATCH** — binding confirmed. Proceeded to review.
- Page count: `pdfinfo` reports 6 pages — matches declared 6pp.
- Title-block version line: "July 22, 2026 — v2B.0.14" — matches binding
  version v2B.0.14.

## Method

- Full-text extraction via `pdftotext -layout` (all 6 pages, 275 lines), read
  end to end: abstract, Keywords, Secs 1–12, Acknowledgements, References
  [1]–[4].
- Layout-sensitive confirmation via `pdftoppm -r 130` render of page 1 (the
  abstract/keywords region, where the Overview-stub removal is verified), to
  confirm the Keywords line sits under the abstract and no empty section
  survives.

## Closure verification (the three 2026-07-22 confirmation-wave edits)

### C1 — Empty Overview stub removed (Keywords under abstract)

- LANDED. Page-1 render and text both show the Abstract followed immediately by
  "Keywords. Python; cosmology; pseudo-Cℓ; NaMaster; reproducibility;
  provenance." and then directly "1 Introduction". There is no empty
  "Overview" heading/stub anywhere in the document.
- Section numbering is contiguous 1→12 (1 Introduction, 2 Statement of Need,
  3 Implementation and Architecture, 4 Exact-Window Inference, 5 Content
  Validation, 6 Quality Control, 7 Worked Examples, 8 Author Contributions,
  9 Limitations, 10 Availability, 11 Reuse Potential, 12 AI Usage Disclosure),
  with no gap or orphaned number where the stub was removed. Clean excision.

### C2 — Null-injection realization count anchored (500)

- LANDED. Sec. 7 "Synthetic CMB recovery campaign": "The null injection, also
  run with 500 realizations, recovered 0.000°." The count is explicit.
- Cross-consistency: the two nonzero angles are each described as a
  "500-realization" run (0.270°↦0.270°, 0.342°↦0.342°); Sec. 10 Availability
  independently states "500 realizations at each of three injected angles"
  (= two nonzero + one null). The 500-per-angle figure is now internally
  consistent across Secs 7 and 10 — no residual unanchored/blank count.

### C3 — Stale blocker sentence removed

- LANDED. No stale blocker/TODO/placeholder/"pending" sentence remains
  anywhere in the body, limitations, or availability sections. Full read
  surfaced no orphaned caveat referencing an unresolved blocker. The
  Limitations (Sec. 9) and Reuse (Sec. 11) text reads as finished prose with
  no dangling clause left behind by the removal.

## Regression sweep (edits must not have broken unchanged content)

- Cross-references: Eqs. (1)–(5) defined and referenced consistently;
  references [1]–[4] all cited (Hivon MASTER, Alonso NaMaster, Lewis CAMB,
  Górski HEALPix) and all present in the bibliography; no broken cross-ref.
- Numerical/quantitative self-consistency (spot re-audit, unchanged content):
  41 automated tests = 39 run + 2 replay-equivalence skipped (Sec. 6) —
  consistent. Workspace shape [4, 20, 4, 1025] identical in Sec. 6 and in the
  rebuild-script mention; max |Δ| = 1.41×10⁻¹⁸ vs 10⁻¹⁰ acceptance threshold —
  consistent. Nside=512, ℓmax=1024, PyMaster 2.6, CAMB 1.6.6, healpy 1.19.0,
  Python 3.10+, NumPy 1.24+ consistent across Secs 7/10. Wall time ~7×10² s
  with eight workers — unchanged and coherent. None perturbed by the closures.
- The "three injected angles" phrasing (Sec. 10) remains consistent with the
  two-nonzero-plus-null enumeration in Sec. 7 after the null count was
  anchored at 500 — closure C2 did not create a mismatch.
- SHA-256 artifact bindings (Sec. 10 Validation artifacts) and Zenodo DOIs
  (software doi:10.5281/zenodo.21481753; manuscript doi:10.5281/zenodo.21481842)
  render intact; no layout break, no margin overflow from the edits.

## New findings (beyond the closures)

- None material. No new BLOCKER, MAJOR, or MINOR surfaced on this re-sweep.
- Observation (non-blocking, pre-existing, NOT a revision request): the paper
  states version "0.1.7" for the software package while the manuscript
  metapaper version is v2B.0.14 — these are two distinct version lines
  (package vs paper) and are used consistently as such; noted only to confirm
  the closures did not introduce a version contradiction.

## Assessment

All three 2026-07-22 confirmation-wave closures landed correctly. The Overview
stub is gone with contiguous section numbering, the null-injection count is
anchored at 500 and consistent with the campaign totals, and no stale blocker
sentence remains. No regression to cross-references, quantitative claims,
section structure, or layout. No new issues of any severity. The metapaper
remains internally consistent and within its declared software-validation
scope.

- Findings this round: BLOCKER 0 / MAJOR 0 / MINOR 0 / new 0.
- Closures confirmed: 3 of 3.

VERDICT: ACCEPT
