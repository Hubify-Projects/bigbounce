# CLAUDE INT referee — P4 re-sweep (raw report)

- Round: ROUND_2026-07-23-P4-v1.0.270-EXACTPDF-ac7b39ba-CLAUDESTACK-RESWEEP
- Referee: Claude INT (Opus), standard high referee bar, no steering
- Date: 2026-07-23
- Paper: P4 — "An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled
  High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"
- File: pipelines/p2_chirality/chirality_catalog_paper.pdf
- Version stamped (title page): v1.0.270; Dated July 22, 2026
- Pages: 32 (all read)

## 0. Binding / integrity

- Expected sha256 (resweep_bindings.json, P4):
  ac7b39baca9a8196826227fde50c7b76be00a77f11213f833b85bbeca4cda33e (sha8 ac7b39ba)
- Computed sha256 of on-disk PDF:
  ac7b39baca9a8196826227fde50c7b76be00a77f11213f833b85bbeca4cda33e
- MATCH. Binding verified; not BINDING-FAILED. Page count 32 == expected 32.

This re-sweep carries ONLY the 2026-07-22 confirmation-wave closures for P4:
(1) Table 5 label "Excluded rows / valid pixels"; (2) epoch wording disambiguated
(plateau breakout by epoch 5, best 0.9931 at epoch 47, cross-ref Table 13);
(3) abstract parity-bound sentence hardened. Each verified below at the exact site
plus neighboring cross-refs, checking for regression.

## 1. Closure verification (exact sites + neighbors)

### Closure 1 — Table 5 label "Excluded rows / valid pixels" — VERIFIED

Table 5 ("Primary HC estimator audit"), the row now reads:
  "Excluded rows / valid pixels        2,597 / 23,633"
directly under "Nselected / Nsupport   890,069 / 887,472".

Arithmetic + cross-ref checks (all consistent, no regression):
- Excluded rows 2,597 = Nselected − Nsupport = 890,069 − 887,472. Correct: these are
  HC-selected rows not landing in a supported (Nspiral ≥ 10) pixel.
- Valid pixels 23,633 = the HC-RI support pixel count. Matches body §3.2
  ("Nsupport = 887,472 enter the 23,633 supported pixels"), §4.3
  ("887,472 enter the 23,633-pixel HC-RI support"), Table 2 footnote a
  ("HC-RI contains 23,633 of 49,152 pixels after excluding all 59,515 raw flip qc
  unsafe HC rows"), and Table 5 body row (Adip/monopole, zmom, rank p all unchanged).
- The label is now unambiguous and describes exactly the two quantities shown. No
  neighboring number shifted; Nselected/Nsupport, seed 20260715, null draws 10,000,
  zmom +0.6346509, rank p 0.2376762 all internally consistent with the abstract
  (890,069 / 887,472; zmom +0.635; p 0.23768).

### Closure 2 — epoch wording disambiguation — VERIFIED

Two prose sites + the table cross-ref, all now consistent:
- §2 (Introduction/data): "an identical-optimizer GZ1-only run broke out of the same
  0.66 plateau by epoch 5 and climbed to its best 0.9931 three-class validation
  accuracy at epoch 47 (Table 13)."
- Appendix B (root-cause item iv): "an identical-optimizer, identical-model GZ1-only
  run broke out of the same 0.66/0.62 plateau by epoch 5 and climbed to its best
  0.9931 three-class validation accuracy at epoch 47 (Table 13), whereas here training
  accuracy is stuck at 0.667 for all 26 epochs..."
- Table 13 (bottom block): "Retrain: best-epoch val. accuracy   99.31% (epoch 47)".

Cross-ref integrity: 0.9931 == 99.31% (Table 13). The distinct CE-included retrain
figure — "best three-class validation accuracy 0.5617 at epoch 11 (26 epochs,
early-stopped)" — is kept clearly separate and does not collide with the GZ1-only
"epoch 47 / 0.9931" statement. The prior epoch ambiguity (which run, which epoch) is
resolved: breakout epoch 5, best epoch 47 for the GZ1-only run; CE-included run stuck
at 0.667 train / 0.5617 val at epoch 11. No regression; the two runs are never conflated.

### Closure 3 — abstract parity-bound sentence hardened — VERIFIED

Abstract final sentence: "The parity-even morphology observable yields no physical
primordial-parity bound (that bound remains gated on the unresolved morphology
transfer function)." This matches the required hardened wording ("yields no physical
primordial-parity bound...").

Consistency with body (no regression): identical framing recurs at §6.2
("Aobs95 is an observed-label sensitivity floor and explicitly not a physical
parity-amplitude bound: the physical limit Aphys95 additionally requires the spatially
resolved morphology transfer function"), §6.3 ("neither the HC null nor the diagnostic
WLS/harmonic channels establish a physical parity-amplitude bound"), Table 1 row viii
("Aobs95 ≃ 0.98% (not a physical parity bound)"), Conclusions ("an observed-label
sensitivity floor, not a physical parity-amplitude bound, whose physical counterpart
remains gated on the morphology transfer function"). The abstract now aligns exactly
with the body's gated-bound language. No contradictory "bound" claim anywhere.

## 2. Regression scan (full read, 32 pp)

- Numeric backbone consistent throughout: Nselected 890,069, Nsupport 887,472,
  zmom +0.635 (exact +0.6346509), rank p 0.23768, Adip 0.00466520, Aobs95 ≃ 0.98%,
  59,515 unsafe HC rows (949,584 − 59,515 = 890,069). Verified in abstract, §3.2,
  §4.1–4.3, Tables 1/2/3/5, §6.2, Conclusions, Data Availability.
- Monopole significance: −9.47σ exact per-pixel binomial (Table 4), ≈9.5σ rounded
  ("−0.26% (9.5σ)" in Data Availability; "global 9.5σ CW-fraction monopole"). P4's
  own convention is internally consistent (−9.47σ exact / ≈9.5σ rounded). NOTE: the
  ≈9σ→≈9.5σ harmonization in this wave was scoped to P5, not P4; P4 already carried
  the ≈9.5σ/−9.47σ convention and needs no change.
- Joint estimator covariance (Table 9, §4.5): NaMaster-complete 4×4, monopole is the
  only |z|>3 mode (z=−6.57), nearly uncorrelated with dipole/harmonic channels. Internally
  consistent with abstract ("now NaMaster-complete with the MASTER-decoupled ℓ=1 leg").
- No undefined-reference markers (??) anywhere. References [1]–[18] intact.

## 3. New findings

### F1 (MINOR) — version self-reference lag in Data Availability

Title page: "Version v1.0.270". Data Availability paragraph states:
  "That record archives the reviewed v1.0.268 PDF and source (the exact reviewed
  bytes); the present manuscript is v1.0.269, and this and subsequent versions are
  added to the same Zenodo record..."
"the present manuscript is v1.0.269" lags the title stamp (v1.0.270) by one patch.
Cosmetic/editorial provenance inconsistency; changes no science, artifact hash, or
DOI logic (concept DOI 10.5281/zenodo.21461898 → latest; version DOI
10.5281/zenodo.21461899 archives the reviewed bytes). Pre-existing (not introduced by
this closure wave). Recommend updating "v1.0.269" → "v1.0.270" in the Data Availability
prose at the next bump so the self-reference matches the title stamp.

No BLOCKER or MAJOR findings. No regressions of any prior closure.

## 4. Verdict rationale

All three confirmation-wave closures landed at their exact sites with correct
arithmetic and consistent neighboring cross-references; zero regression across the full
32-page read. One genuine but purely cosmetic MINOR item (F1: version self-reference
lag in the Data Availability section). Under a strict high referee bar this concrete,
actionable editorial fix warrants a MINOR-REVISIONS tag; the underlying science and all
closures are clean and regression-free.

VERDICT: MINOR-REVISIONS
