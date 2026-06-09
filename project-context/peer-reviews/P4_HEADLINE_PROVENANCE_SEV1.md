# SEV-1 — P4 headline −0.122σ subsample-mask null: synthetic-footprint provenance

**Date:** 2026-06-09 ~12:30 PT · **Status:** HOUSTON DECISION REQUIRED before any P4 .tex edit
**Trigger:** publish-plan compute job C3 (Wp-invariance check, pod 5i2td3deu3hojr)

## Evidence chain (each item independently verified)

1. **The published mask cannot be built from the real catalog.** Paper claims
   subsample mask = 32,384 px / f_sky = 0.659. C3 swept predicates N_all ≥
   {1,2,3,5,10} on the production HF catalog → every variant gives ~24.2–24.3k px
   / f_sky ≈ 0.49. There is no threshold that yields 0.659.
   (`c3_wp_invariance_fsky.json` → `mask_candidates`.)
2. **The producer script was never committed.** `master_results/master_power_spectrum.json`
   (n_galaxies=5,547,858, f_sky=0.6588…, −0.122σ) was added by commit `c58ed751`
   (April 2026 "close 4 future-work items" wave: "Dipole significance drops from
   2.75σ to −0.12σ"). No generating script exists in the repo; the JSON carries
   no catalog-source provenance fields.
3. **The original pod log says synthetic.** The pod2 run log (recovered during C3
   setup) reads "Generating galaxy catalog … 5,547,858 galaxies (DESI Legacy
   footprint approximation)" — i.e., the catalog for that run was GENERATED, not
   loaded from the production parquet.
4. **A faithful real-catalog rerun is strongly non-null.** C3 reproduced the
   paper's declared recipe exactly (A_p with galaxy-weighted mask-mean
   subtraction, C² 2° apodization, 500-MC per-galaxy label-shuffle null, seed 42,
   single-mode MASTER ℓ=1): **Wp=N_all → +7.28σ; Wp=N_spiral → +9.78σ.**
5. **Corroborating inconsistency:** paper fn quotes ⟨N_all/N_spiral⟩ ≈ 1.49; the
   real catalog gives 2.827 (consistent with global 8.47M/3.20M = 2.65).

## What this does NOT break

- **Real-space dipole +0.43σ (p=0.30)** — computed locally on the real catalog,
  well-provenanced. Survives as a real null.
- **Monopole-mask leakage demonstration (99.3%)** — C2 just re-verified it on the
  real catalog under BOTH trial pools (99.322% / 99.327%). Robust.
- **Canonical-mask +3.64σ systematics attribution** — all five interpretation-(ii)
  anchors (leg-stratified 25%, ℓ=2 anti-alignment r=−0.65, density-stratified
  null +3.80σ, WLS z≈−18 vs 1.7% dipole, HC-cut collapse) are real-catalog
  results and stand.
- **Formal exclusion of interpretation (i) at 1.7%** via joint nuisance fit — real.

## Likely corrected story (pending C6 diagnostic)

The "strict-superset subsample mask at f_sky=0.659" never existed in data; the
real footprint ≈ the canonical footprint (0.494). On the real footprint the
post-MASTER ℓ=1 excess is +3.6σ (unapodized canonical, published) to +7–10σ
(apodized, weight-map dependent) — same systematics-attributed family. The
paper's headline null must shift from "−0.122σ MASTER" to the real-space dipole
+0.43σ + the 99% formal exclusion of a 1.7% dipole, with the MASTER channel
reframed entirely as the leakage/systematics diagnostic it already is for the
canonical mask. C6 (depth-stratified null on the real apodized footprint) will
test whether the +7–9σ excess is absorbed by depth conditioning, completing the
attribution before any rewrite.

## Decision asks (Houston)

- [ ] **D1.** Approve retraction/replacement of the −0.122σ headline estimator
      (Table I row (ii), abstract, conclusions) with the corrected real-catalog
      framing above. This is a MAJOR revision of P4's abstract.
- [ ] **D2.** P4 was first in the submission order. Keep P4 first (rewrite
      tomorrow after C6) or promote P1A+P1B / P3 ahead of it?
- [ ] **D3.** The April `c58ed751` wave closed several "future-work" items in one
      commit. C2/C3 re-verified its P4-M6 item; the FW-1/FW-2/FW-11 items from
      the same wave (P2/P3 Fisher + NANOGrav numbers) should get the same
      provenance audit before submission. Approve audit job C7?

## Immediate actions taken (no .tex edits)

- C2/C3 artifacts + scripts committed; compute-queue.json live on /status panel.
- C6 diagnostic queued on pod 5i2td3deu3hojr ($0.17/hr).
- PUBLISH_PLAN.md updated: P4 submission gate now blocked on D1/D2.
