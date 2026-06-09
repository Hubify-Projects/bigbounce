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

## C6 verdict (2026-06-09 19:05 UTC) — attribution analysis COMPLETE

C6 reran the C3 real-footprint apodized MASTER ℓ=1 measurement against a
**depth-stratified** per-galaxy label-shuffle null (labels permuted within 10
N_all(p) pixel-density deciles, 500 MC, seed 42, same field/apodization):

| Estimator | vs global shuffle (C3) | vs depth-stratified null (C6) | Absorbed by depth? |
|---|---|---|---|
| Wp=N_all | +7.28σ | **+7.13σ** (0/500 null exceed) | NO (−2%) |
| Wp=N_spiral | +9.78σ | **+9.06σ** (0/500 null exceed) | NO (−7%) |

Depth conditioning absorbs essentially none of the excess — **exactly mirroring
the published canonical-mask behavior** (density-stratified null +3.80σ,
already in the paper). Per-decile CW fractions are flat (0.4960–0.4988),
confirming no gross depth–chirality correlation; the excess lives in the
low-ℓ spatial coherence of the apodized weighted field, which is precisely what
the paper's five interpretation-(ii) anchors (leg stratification 25%, ℓ=2
anti-alignment r=−0.65, WLS template z≈−18, HC-cut collapse, stratified nulls)
attribute to a coherent survey-geometry/sampling systematic. Artifact:
`pipelines/p2_chirality/outputs/canonical_provenance/c6_depth_stratified_null.json`.

## Corrected story (now fully evidenced)

The "strict-superset subsample mask at f_sky=0.659" never existed in data; the
real footprint ≈ the canonical footprint (0.494). On the real footprint the
post-MASTER ℓ=1 excess is +3.6σ (unapodized canonical, published) to +7–9σ
(apodized, weight-map dependent; C3/C6) — one systematics-attributed family,
not absorbed by depth conditioning (C6), anti-aligned with density at ℓ=2,
collapsing under HC cuts. The paper's headline null shifts from "−0.122σ
MASTER" to the real-space dipole +0.43σ + the 99% formal exclusion of a 1.7%
dipole, with the MASTER channel reframed entirely as the leakage/systematics
diagnostic it already is for the canonical mask.

## DRAFT corrected abstract + Table I (for D1 — no .tex edits made)

**Abstract, headline sentences (replace current lines 75 + 81 headline claims):**

> The headline scientific result is a **null** real-space chirality dipole:
> the post-TTA Catalog C dipole fit gives +0.43σ (p=0.30, isotropic-null
> bootstrap, N_MC=10,000), and a joint nuisance-marginalized template fit
> formally excludes a clean cosmological dipole of amplitude 1.7% at 99%.
> The MASTER-deconvolved pseudo-Cℓ channel is presented as a systematics
> *diagnostic*, not an independent null: on the canonical footprint
> (f_sky=0.494) the post-MASTER ℓ=1 residual is +3.64σ and is attributed to a
> coherent survey-geometry/sampling systematic by a five-anchor battery (leg
> stratification, ℓ=2 anti-alignment r=−0.65, density- AND depth-stratified
> nulls, WLS template z≈−18, HC-cut collapse). [Erratum note: v≤1.0.165
> reported a −0.122σ MASTER null on an f_sky=0.659 "strict-superset subsample
> mask"; a provenance audit (2026-06-09) found that result was computed on a
> synthetic-footprint catalog and it is withdrawn in this version.]

**Table I (tab:headline_summary):** delete row (ii) "MASTER deconv … 5,547,858
… 0.659 … −0.122"; promote real-space dipole to sole row-(i) headline; add
diagnostic rows: canonical-mask MASTER +3.64σ (systematics-attributed) and
apodized real-footprint MASTER +7.1/+9.1σ vs global/depth-stratified nulls
(C3/C6, systematics-attributed). Fix ⟨N_all/N_spiral⟩ 1.49 → 2.827.

**Cascade sites (grep −0.122 / 0.659 / 5{,}547{,}858):** abstract (L75, L81),
intro (L99), estimator list (L147), Table I (L162), Table multipole caption+row
(L329, L336), §leakage (L360, L382), §future (L425), §direct-exec (L438),
App A (L457, L463), App D (L546), HC-robustness (L555). ~14 sites, one rewrite
pass + recompile + /latex-audit + full sync → v1.0.166.

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
