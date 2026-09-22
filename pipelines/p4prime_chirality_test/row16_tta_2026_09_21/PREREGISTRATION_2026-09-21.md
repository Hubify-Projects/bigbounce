# Rows 13/16 follow-ups — PRE-REGISTRATION (2026-09-21, committed BEFORE any statistic was run)

**Lane** `bb-LS6-row16-tta` (science lane of
`project-context/campaigns/CAMPAIGN_2026-09-18_publication_push.md`).
**Ledger rows** 16 (galaxy chirality at scale, image-level program) and 13.
**Parent result** `../row16_pa_parity_transfer/ROW16IIB_PA_PARITY_TRANSFER_2026-09-19.md`
(commits `34b6ece9`, `ffc0e682`), which retired the mirror-injection-at-larger-N
GPU step on an exact algebraic identity and named, but did not run, the three
zero-cost steps pre-registered here (its §10 and §11 deviation 2).
**Directive basis** R1 (the ledger defines the work), Q2 (reproducibility
manifest per run), L (real computation, honest integration),
`/never-fabricate-derivation`, nulls stay nulls.

This file is committed before any script below is executed. Statistics,
estimators, thresholds, decision rules and the two hard-assert controls are
fixed in advance. Deviations are recorded in the results document, never
silently. Every number produced is published as it comes out.

---

# Step T — how much of the ε deficit is recoverable by rotation equivariance?

Row 16(ii-b) established that the deficit is a **rotation**-equivariance
failure, not a parity failure: `ε(φ)` tracks the rotation-only class stability
`R(φ)`, and the parity operation transfers exactly wherever the released
2-element flip-TTA covers it. The open decision is whether a D4-equivariant
retrain (row 16(iii)) is worth GPU budget. A test-time-augmentation average
over rotations, applied to the **existing committed checkpoint**, is the free
proxy for that retrain, and the bound it gives is the decision input.

## T0 — theorem, declared in advance, checked numerically as a control

Let `eq(·)` be the released equivariant triple (2-element flip TTA) and define
the `G`-TTA for `G = C_n ⋊ Z2` (rotations by `Φ_n = {360k/n}` plus the mirror)

    Q_c(J) = (1/n) Σ_{ψ ∈ Φ_n} eq_c( Rot_ψ J ) .

Then, exactly and independently of the network's weights:

1. `Q` is `C_n`-invariant: `Q(Rot_θ J) = Q(J)` for `θ ∈ Φ_n`; hence the label
   self-disagreement `d_Q(θ) = 0` for every `θ ∈ Φ_n`.
2. `Q` inherits the exact mirror antisymmetry `Q_cw(M J) = Q_ccw(J)`,
   `Q_ns(M J) = Q_ns(J)`.
3. With the row-16(ii-b) pairing `X_φ = Rot_φ I`, `Y_φ = Rot_φ M I` (the
   PA-restoring counterfactual at presented rotation `φ`), 1 and 2 give
   `Q_cw(Y_φ) = Q_ccw(X_{-φ}) = Q_ccw(X_φ)` whenever `2φ ∈ Φ_n`, i.e. the
   parity-transfer efficiency is **identically** `ε_Q(φ) = 1` at every such `φ`.

**Consequence, stated before any run:** an angle grid closed under a TTA's own
rotation group cannot measure that TTA's residual deficit. On the existing
45°-spaced 8-angle grid, the D4 TTA (`n = 4`) has `ε ≡ 1` at every angle and
`d ≡ 0` within each coset — by construction, carrying no information. The same
algebra says that on a 22.5°-spaced grid the D8 TTA (`n = 8`) still has
`ε ≡ 1` everywhere (every grid `φ` has `2φ ∈ Φ_8`), while its `d` **is**
measurable on the 22.5° coset. Measuring `ε_D8` would need an 11.25° grid and
is explicitly NOT attempted here.

**Hard control T0-C.** The three identities above are asserted numerically at
machine precision on the realised probabilities (`d_G(θ) == 0` exactly for
`θ ∈ Φ_n`; `max |Q_cw(Y_φ) − Q_ccw(X_φ)| == 0` at every `φ` with `2φ ∈ Φ_n`).
A failure means a code defect and the run is declared INVALID, not reported.

## T1 — new inference (stage 3)

The only new forward passes in this lane's step T. Identical preprocessing,
checkpoint and pairing to row 16(ii-b) stage 1 — `Resize₂₂₄(CentreCrop₁₀₆(
Rot_φ(·)))`, model `bamfai/galaxy-chirality-v2` @
`237d021c451d75cf86a875e86d4de498b74e2f12` — on the **same 19,800 cached
cutouts**, at the eight 22.5°-offset angles

    Φ' = {22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5}°

for both kinds (`A_φ = Rot_φ I`, `B_φ = Rot_φ M I`): 16 passes per galaxy,
316,800 total. `Φ'` is closed under negation mod 360, which the equivariant
bookkeeping requires. Stage 1 ∪ stage 3 is then a uniform 16-angle 22.5° grid
on one preprocessing. No new downloads; no rented GPU; local Apple MPS.

**Partial-run rule, fixed in advance.** Galaxies are processed in the order of
a seeded permutation `numpy.random.default_rng(20260921).permutation(N)`, so
any truncation is an unbiased subsample rather than the class-ordered prefix of
the sample file. Checkpoint every 2,000 galaxies. Hard wall-clock cap **90
minutes**: at the cap the run stops and every step-T statistic is computed on
exactly the galaxies completed, with that `N` reported in the results JSON and
in the document. No statistic is extrapolated to the full 19,800.

## T2 — pre-declared statistics

All on the cropped grid (stage 1 ∪ stage 3), for the three TTA groups
`G ∈ {Z2 (the released pipeline), D4, D8}`, reported for all galaxies and for
the catalogue's own `primary_hc` cut (`is_spiral` and `max(eq_cw, eq_ccw) > 0.6`
on the committed uncropped probabilities, as in
`build_apjs_release_v1_0_244.py:163-168`).

- **T2a `d_G(φ)`** `= P( L_G(X_φ) ≠ L_G(X_0) | both labelled spiral )`, over the
  15 non-zero grid angles. *Informative* `φ` for `G` are those whose offset is
  not in `G`'s rotation subgroup: all 15 for `Z2`; offsets `{22.5, 45, 67.5}`
  (mod 90) for `D4`; the 22.5° coset for `D8`.
- **T2b dilution bound** `D_G ≤ 1 − max_{informative φ} d_G(φ)`, the row-16(ii-b)
  §4 bound evaluated for each TTA. Cluster bootstrap over galaxies, 1,000
  resamples, `default_rng(20260921)`.
- **T2c `ε_G(φ)`, `ρ_G(φ)`, `L_G(φ)`** by the row-16(ii-b) S1 definition (the
  row-normalised 3×3 transition matrix between `L_G(X_φ)` and `L_G(Y_φ)`), and
  `ε̄_G` over the angles that are informative for `G` (for `D4`: the eight
  22.5-offset angles; for `D8`: none — see T0).
- **T2d recovery fraction** `F_G = (D_G − D_Z2) / (1 − D_Z2)`, the share of the
  released pipeline's dilution gap that the TTA closes, with a bootstrap SE on
  the difference (same resamples for numerator and denominator).
- **T2e catalogue churn**: the fraction of galaxies whose `L_G` at `θ = 0`
  differs from the committed released catalogue class — what adopting the TTA
  would change in a re-release.

## T3 — decision rule for row 16(iii), fixed before the numbers exist

Let `F ≡ F_D4` and let the residual be `1 − D_D4`.

- **GPU GO** iff `F ≥ 0.5` **and** `1 − D_D4 ≥ 0.10`: rotation-orbit instability
  is the dominant term (so equivariance is the right lever) *and* enough is left
  after free equivariance for better learned features to be worth buying.
- **NO-GPU, ADOPT-TTA** iff `F ≥ 0.5` and `1 − D_D4 < 0.10`: the free
  inference-time TTA already captures essentially all of the recoverable
  deficit; a retrain buys little, and the right action is to adopt the TTA in
  the released pipeline.
- **NO-GPU, WRONG-LEVER** iff `F < 0.5`: equivariance is not the dominant
  failure axis, and a D4-equivariant retrain would not deliver the recovery
  row 16(iii) was costed on.

The recommendation is recorded whichever way it comes out, together with the
realised `F`, `D_D4`, `D_D8` and their bootstrap errors. The threshold is not
moved after the fact. **Scope of the claim, stated in advance:** a TTA over
non-equivariant weights and a genuinely D4-equivariant architecture agree
exactly on part 1 of T0 (both annihilate `d` on the `C4` orbit — a theorem),
and differ only in the quality of the learned features that set the *off-group*
residual. This measurement therefore bounds the equivariance-attributable part
of the deficit exactly and says nothing about the feature-quality part; that
limitation is reported with the number, not after it.

---

# Step P — `d(180)` beyond the 19,800-galaxy sample

## P0 — feasibility, declared in advance

A literal `d(180)` on the 8,474,531-row parent requires one forward pass per
galaxy per orientation **on the image**, and the repository caches cutouts for
only 25,300 galaxies (19,800 + 5,000 + 500, all 150 px `ls-dr9`). Fetching
8.47M cutouts is excluded by this lane's no-large-download and ~10 GB disk
constraint (and would be ~8.5M HTTP cutout requests against a public NOIRLab
service). **The full parent is therefore declared infeasible here, in advance,
and the largest feasible subset is the union of the three committed caches.**
No step below is described as a measurement on 8.47M galaxies.

## P1 — new inference (stage 4)

The **exact released preprocessing** (`Resize₂₂₄` of the full 150 px cutout, no
crop) at `θ ∈ {0, 180}` — lossless PIL transposes, no interpolation anywhere —
for both kinds, on the 5,000-galaxy (`cutout_cache_scale`, seed 43, NSIDE=32
sky-uniform) and 500-galaxy (`cutout_cache`, seed 42) samples: 4 passes per
galaxy, ≈ 22,000 passes. Same checkpoint pin. `θ = 180` is the orientation that
needs no PA-uniformity argument at all (position angle is defined mod 180°), so
this is the assumption-free anchor of the row-16(ii-b) §4 bound.

## P2 — pre-declared statistics

- **P2a** `d(180)` and `D ≤ 1 − d(180)`, computed exactly as
  `../row16_pa_parity_transfer/s5b_nocrop_dilution.py` does (restricted to
  galaxies labelled spiral at both orientations), **separately for each of the
  three independent draws** and for their de-duplicated union (duplicates
  matched on `(ra, dec)` within 1e-6 deg). Cluster bootstrap, 1,000 resamples,
  `default_rng(20260921)`. Cross-draw consistency is the pre-declared internal
  check; the three draws use different seeds and two different sky-sampling
  resolutions, so a common value is evidence of stability and a discrepancy is
  reported as one.
- **P2b** the same on the `primary_hc` subset of each draw.
- **P2c positive control (hard assert)**: at `θ = 0` the no-crop chain *is* the
  committed pipeline, so its classes must agree with the committed catalogue on
  ≥ 99.9% of matched galaxies, and the mirror identity residual must be exactly
  `0.0` at `θ ∈ {0, 180}` with a class-swap fraction of exactly 1 among non-tied
  galaxies. Failure ⇒ INVALID, nothing reported.

## P3 — the catalogue-wide number is an ESTIMATE, and is labelled one

A stratified re-weighting, run and reported **as an explicit extrapolation**:

    d̂_parent(180) = Σ_s w_s · d̂_s(180)

with strata `s` = deciles of `score_eq_max` (the released per-galaxy confidence,
present for all 8,474,531 rows of
`../../p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet`)
taken over the parent spiral set `class_eq ∈ {CW, CCW}`; `w_s` the parent
fraction in stratum `s`; `d̂_s` measured on the union sample, whose galaxies are
matched to their parent rows on `(ra, dec)` within 1e-6 deg (the match rate is
reported, and unmatched galaxies are dropped, not imputed).

**Assumption declared in advance:** within a `score_eq_max` stratum, `d(180)` is
independent of the quantities the sky-uniform sampling distorts (principally
local sky density). The motivation is the row-16(ii-b) §5.2 finding that the
deficit varies strongly and monotonically with confidence (`ε̄` 0.577 → 0.778
across deciles) and only at the few-percent level across hemispheres.
**Sensitivity check:** the same re-weighting on (confidence decile × hemisphere
of the strict-887,472 axis), evaluated only if every cell holds ≥ 50 measured
galaxies; otherwise recorded as not evaluable rather than reported at low count.

The bound propagated to P4′ remains the **measured** one on the stated N. The
re-weighted number is quoted beside it, explicitly as an estimate under the
assumption above. No threshold, no kill condition: this step reports what it
finds.

---

# Step S — projecting the S6 sky dependence onto a dipole

Row 16(ii-b) §8 found `ε̄` differs between hemispheres by ±3.6% at ~7σ on both
candidate axes and deliberately stopped there. A position-dependent dilution can
imprint a spurious dipole in the observed labels; this step quantifies that, in
the same estimator and the same units P4′ uses for its limits.

## S0 — mechanism, stated before the computation

Observed-label asymmetry `A_obs(n̂) = D(n̂) · A_true(n̂)`. With `A_true = 0` a
sky-varying `D` produces **no** dipole: dilution cannot manufacture signal from
nothing. The spurious dipole is sourced by the product of the sky-varying
dilution and the **non-zero monopole** of the observed label asymmetry (the
catalogue's own `monopole = −0.005116`, `row16i_full_parent_dipole.json`):
writing `D(n̂) = D̄(1 + δ(n̂))`, `A_obs` acquires a dipole of amplitude
`|A_mono| · a_δ`. That is the quantity being computed, and the estimator is
fixed here so it cannot be chosen after the answer is known.

## S1 — per-galaxy transfer statistic

`ε_i` = (number of informative `φ` with `L(X_φ)` spiral and
`L(Y_φ) = swap(L(X_φ))`) / (number of informative `φ` with `L(X_φ)` spiral), on
the **stage-1 cropped 8-angle grid** — the grid the S6 finding was made on.
Galaxies with no informative spiral angle are dropped and counted. The
population mean of `ε_i` is reported beside the row-16(ii-b) S1 confusion-matrix
`ε̄ = 0.6363` as a consistency check; the two estimators weight galaxies
differently and are not required to be equal.

## S2 — pre-declared statistics

- **S2a** hemisphere split of `ε̄_i` on **both** axes named in row 16(ii-b) §11
  deviation 2 — strict-887,472 `(195.5°, −57.2°)` and full-parent
  `(278.629719594135°, +25.3202680239249°)` — with a galaxy bootstrap, to confirm
  the per-galaxy estimator reproduces the ±3.6% / 7σ S6 result.
- **S2b dipole fit**: NSIDE=8 HEALPix map of mean `ε_i` over pixels holding ≥ 5
  galaxies, `healpy.fit_dipole` (unweighted, the same convention as the P4′
  estimator), giving the fractional dipole amplitude `a_δ` and its direction.
  Errors: 1,000 galaxy-level bootstrap resamples. **Null:** 1,000 random
  permutations of `ε_i` across galaxy positions (destroys sky dependence, keeps
  the `ε` distribution) → rank-p of the observed amplitude.
- **S2c induced spurious label dipole**, projected through the **exact** P4′
  estimator: `build_projector` imported verbatim via
  `../full_parent/full_parent_estimator_lib.py` (NSIDE=64, support ≥ 10
  galaxies/pixel), evaluated on the real parent sky support, with the per-pixel
  asymmetry map `m(n̂) = A_mono · (1 + δ(n̂))` and `δ` the fitted dipole model.
  `A_induced` = the ℓ=1 amplitude of `projector @ m`. Computed on both the full
  parent support and the strict-primary support, and reported in % and as
  fractions of `A_obs = 0.566%`, the full-parent `A95_obs = 0.5095%`, and the
  strict-subset `A95_obs = 0.98%`.
- **S2d** alignment angle between the fitted `ε` dipole axis and the observed
  `A_obs` dipole axis.

## S3 — pre-declared threshold

The P4′ dipole limits **require a written systematic caveat** iff
`A_induced > 0.10 × A95_obs` on either support. If
`A_induced ≤ 0.10 × A95_obs`, the result is recorded as a *quantified and
subdominant* systematic with its number and its null-rank quoted. Either way the
number and the verdict are published, the direction of the effect is stated, and
the threshold is not moved after the fact. If `S2b`'s null rank shows the `ε`
dipole is itself consistent with noise, that is reported as a null and the
propagation is still carried out and quoted as an upper limit.

---

# What this lane will NOT do

No paper `.tex`, no SSOT, no site data, no Convex write (Convex is disabled for
exceeding its spending limit; intended mutations are appended to
`project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md` instead). No RunPod, no
rented GPU, no new cutout downloads, no `git add -A`. Only the **row 13 and
row 16 status cells** of `project-context/NEXT_SCIENCE_LEDGER.md` are touched,
re-read immediately before editing. Exact printable sentences for P4′ go in this
directory's `PROPAGATION_NOTE.md`; the manuscript is owned by another lane.
A Q2 reproducibility manifest is written for every run, under
`reproducibility/manifests/experiments/`.
