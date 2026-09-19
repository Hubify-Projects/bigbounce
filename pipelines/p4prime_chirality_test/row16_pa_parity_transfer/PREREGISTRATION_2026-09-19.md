# Row 16(ii-b) — PRE-REGISTRATION (2026-09-19, committed BEFORE any statistic was run)

**Lane** `bb-LS-ledger16` (science-continuation lane of
`project-context/campaigns/CAMPAIGN_2026-09-18_publication_push.md`).
**Ledger row** 16 (galaxy chirality at scale, image-level program), sub-item (ii)
"pixel-level parity injection at scale as the calibration of the dipole".
**Directive basis** R1 (ledger defines the work), Q2 (reproducibility manifest),
L (real computation, honest integration), never-fabricate.

This file is committed before the analysis scripts are run. Statistics, nulls,
thresholds, and the kill condition below are fixed in advance. Deviations are
recorded in the results document, never silently.

---

## 1. Why this step, and not "N > 20k"

Row 16(ii) ran a pixel-level parity injection at N = 20,000 through the
production equivariant pipeline and reported a slope `dA/df`. Reading the
committed code
(`../injection_pilot/run_injection_scale20k.py`,
`../injection_pilot/analyze_injection_scale20k.py`) shows the design is
**degenerate for the paper's statistic**, for a reason that no increase in N
can remove:

The production post-processing is a 2-fold horizontal-flip test-time average,

    eq_cw(I)  = ( p_cw(I) + p_ccw(M I) ) / 2 ,
    eq_ccw(I) = ( p_ccw(I) + p_cw(M I) ) / 2 ,
    eq_ns(I)  = ( p_ns(I) + p_ns(M I) ) / 2 ,     M = horizontal mirror.

Because `M M = 1`, this construction is **exactly** antisymmetric under the
detector-aligned mirror: `eq_cw(M I) = eq_ccw(I)`, `eq_ns(M I) = eq_ns(I)`,
identically, for every image, with no reference to the network's weights. The
injection used by row 16(ii) *is* that mirror. Therefore the hard-argmax class
of a pre-mirrored image is the CW<->CCW swap of the original class, exactly;
the injection is a relabelling theorem, not a measurement of the classifier.
For the paper's statistic `A = 2 N_CW/(N_CW + N_CCW) - 1` this forces
`E[A(f)] = A0 (1 - 2f)` identically, i.e. `dA/df = -2 A0` with **no information
content at any N**. Running the same injection at N = 50k or 500k would
reproduce the same identity with smaller scatter and would still measure
nothing about the pipeline. Option (b) of this lane's task (an N > 20k
extension) is therefore declined on a stated scientific reason, and replaced by
the test below, which breaks the identity.

**What a real parity flip actually is.** A genuine handedness reversal of a
galaxy leaves it at its observed position angle (PA) on the sky. Mirroring an
image about the detector x-axis maps PA -> -PA. So the physically correct
injection is *mirror, then rotate by phi = 2 PA to restore the observed
orientation*. That composite operation is NOT the pipeline's TTA symmetry
(the TTA averages over one mirror, not over rotations), so its transfer
efficiency is a genuine, unknown, measurable property of the released
classifier. It is the calibration P4' does not have.

## 2. Hypothesis

H0 (null, the paper's implicit assumption): the released pipeline transmits a
genuine handedness reversal into its hard catalogue label with efficiency
eps = 1 at every position angle, so the label-level bound A_95 = 0.98%
(strict 887,472 subset) needs no PA correction.

H1: eps(phi) < 1 for phi not a multiple of 180 deg, because the ViT-S/16
backbone is not rotation-equivariant and the TTA averages only the mirror.
Then a true parity signal is attenuated and the published bound is optimistic
by the corresponding factor.

## 3. Data (fixed before the run)

- Sample: the galaxies of `../injection_pilot/scale20k_sample.parquet` whose
  Legacy DR9 `jpeg-cutout` (150 px, layer `ls-dr9`) is already cached at
  `../injection_pilot/cutout_cache_scale20k/<idx>.jpg`. No new downloads.
  Expected N ~= 19,800 of 20,000 (the rest failed to download in 2026-09-04).
  The exact N and the exact index list are recorded in the results JSON.
- Model: `bamfai/galaxy-chirality-v2`, file `chirality_model_v2_best.pt`,
  revision `237d021c451d75cf86a875e86d4de498b74e2f12` (identical pin to
  row 16(ii); asserted in the runner).
- Device: local Apple MPS. No RunPod, no new data on disk beyond small
  outputs (< 50 MB).

## 4. Image operations (fixed before the run)

For each cached cutout `I` (150x150):

    A_phi = Resize_224( CenterCrop_106( Rotate_phi( I ) ) )
    B_phi = Resize_224( CenterCrop_106( Rotate_phi( M I ) ) )

with `Rotate` = PIL bicubic, `expand=False`, and the 106 px centre crop chosen
so that every retained pixel comes from inside the original frame at every phi
(106 * sqrt(2)/2 = 74.95 <= 75). The identical crop is applied at phi = 0, so
the only difference across phi is the rotation. Normalisation is the committed
ImageNet transform used by row 16(ii).

Angle grid: **phi in {0, 45, 90, 135, 180, 225, 270, 315} deg** — 8 angles,
uniformly spaced over the full circle (an unbiased marginalisation over a
uniform PA distribution) and closed under negation mod 360, which is what the
TTA bookkeeping below requires.

Bookkeeping (no redundant inference). Since the centre crop is symmetric,
`M CenterCrop Rotate_phi = CenterCrop Rotate_{-phi} M`, so with
`X_phi = A_phi` (normal galaxy at rotation phi) and
`Y_phi = B_phi` (parity-flipped galaxy, PA restored, same rotation phi):

    eq_cw(X_phi)  = ( p_cw(A_phi)  + p_ccw(B_{-phi}) ) / 2
    eq_cw(Y_phi)  = ( p_cw(B_phi)  + p_ccw(A_{-phi}) ) / 2
    eq_ns(X_phi)  = ( p_ns(A_phi)  + p_ns(B_{-phi}) ) / 2
    eq_ns(Y_phi)  = ( p_ns(B_phi)  + p_ns(A_{-phi}) ) / 2   (and cw<->ccw)

so only `p(A_phi)` and `p(B_phi)` at the 8 angles are needed: 16 forward passes
per galaxy, ~317k total.

## 5. Pre-declared statistics

**S1 (primary) — parity-transfer matrix.** For each phi, the 3x3 matrix
`T(phi)[c, c'] = P( class(Y_phi) = c' | class(X_phi) = c )`, classes
{CW, CCW, NS}, class = argmax of the equivariant triple. From it:

    eps(phi)  = ( T[CW,CCW] + T[CCW,CW] ) / 2      parity transfer efficiency
    rho(phi)  = ( T[CW,CW]  + T[CCW,CCW] ) / 2     handedness retained (error)
    L(phi)    = ( T[CW,NS]  + T[CCW,NS]  ) / 2     leakage out of the spiral set

and the PA-marginalised `eps_bar = mean_phi eps(phi)` over the 8-angle grid,
plus `eps_bar_informative` over the 6 angles that are not exact controls.

**S2 (positive control, hard assert).** At phi = 0 and phi = 180 the TTA
identity is exact (`M` commutes with `Rotate_180`), so the run MUST return
`eps = 1.000000`, `rho = 0`, `L = 0` to machine precision. A deviation means a
code defect, and the run is declared INVALID rather than reported.

**S3 — injection-recovery slope at each phi.** The same statistic row 16(ii)
reported, `dA_cls/df` with `A_cls = 2 N_CW/(N_CW + N_CCW) - 1`, evaluated in
closed form over the realised label sets at each phi, over
f in {0, 0.005, 0.01, 0.02, 0.05} x 200 injection seeds.

**S4 — correction of the committed row 16(ii) error bar (re-analysis, no new
inference).** Using `../injection_pilot/scale20k_pairs.parquet`: build the exact
null distribution of the fitted slope under the identity of section 1 by
Monte-Carlo over 2,000 injection-seed realisations of the same f-grid, and
place the committed 10-seed slope in it as a z-score. Also compute the sample
size `N_req` at which `3 SE(slope) = |2 A0|`, i.e. the N at which the
row 16(ii) design would first have 3-sigma power — reported so the decision to
decline an N-extension rests on a number, not an opinion.

**S5 — rotation-stability control.** `R(phi) = P( class(X_phi) = class(X_0) )`,
the class stability of the *unflipped* galaxy under rotation alone. This
separates "the pipeline loses parity information" from "the pipeline is simply
unstable under rotation". Reported for context; not part of the threshold.

**S6 — sky dependence.** `eps_bar` recomputed in the two hemispheres defined by
the P4' strict-subset dipole axis (RA 195.5 deg, Dec -57.2 deg, from
`../full_parent/row16i_full_parent_dipole.json`).

## 6. Errors and nulls

- Galaxy-level cluster bootstrap, 1,000 resamples over galaxies (each galaxy
  carries all 8 angles, so resampling is at the galaxy level, never at the
  angle level). Every quoted uncertainty is that bootstrap's standard
  deviation.
- Null for S1: the exact-control angles (phi = 0, 180) provide an internal
  zero-deficit null, computed the same way as the informative angles.
- Look-elsewhere: 6 informative angles. A per-angle claim requires
  p_local < 0.0006 (3 sigma after x6 LEE). The marginalised `eps_bar` is a
  single pre-declared number and carries no LEE.

## 7. Pre-declared thresholds and kill condition

1. If S2 fails, the run is INVALID; nothing is reported as science.
2. **Deficit declared** iff `eps_bar_informative < 1` by more than 3 sigma of
   its cluster-bootstrap error. Otherwise the result is reported as a null:
   "no PA-dependent parity-transfer deficit at the measured precision", with
   the achieved 1-sigma precision quoted.
3. If a deficit is declared, the consequence for P4' is stated as the measured
   number only — `eps_bar` and the implied attenuation — with no re-derivation
   of A_95 in this lane (P4' is owned by lane L4; a `PROPAGATION_NOTE.md` in
   this directory carries the exact sentences).
4. **Kill for the whole row 16(ii) injection programme**: if S4 shows the
   committed N = 20k slope is consistent with its own noise floor (|z| < 3)
   AND S1 returns `eps_bar = 1` within errors, then the pixel-injection channel
   is recorded as *calibrated and uninformative* — the row 16(ii) "Next: larger
   N" line is retired with that reason, and the remaining row-16 compute goes
   to (v) Euclid Q1 / DR10 domain adaptation instead.
5. Whatever the outcome, it is published as it comes out. A null is a null.

## 8. What this lane will NOT do

No paper `.tex`, SSOT, site, or Convex edit (P4' belongs to lane L4). No
RunPod. No `git add -A`. Only the row-16 status cell of
`project-context/NEXT_SCIENCE_LEDGER.md` is touched, re-read immediately
before editing.

---

# ADDENDUM A1 (2026-09-19, committed before the statistic it governs was run)

**Why.** The pre-registered post-hoc crop diagnostic, evaluated on the partial
checkpoint, shows that the 106 px centre crop is not benign: only **69.0%** of
galaxies keep the class they have under the committed uncropped 150 px
preprocessing. The crop is common-mode between `X_φ` and `Y_φ`, so it cannot
manufacture a parity asymmetry; but it can make the classifier intrinsically
noisier, and the S5b dilution bound `D ≤ 1 − d(θ)` is a bound on the *released*
pipeline, which does not crop. A `d` inflated by the crop would make that bound
look stronger than it is — the one direction in which an error here would
matter.

**What is added.** For rotations by multiples of 90° no crop is needed at all: a
150×150 image rotated by 90/180/270° is still 150×150 and the rotation is a
lossless pixel permutation. A second inference stage therefore recomputes, for
`θ ∈ {0, 90, 180, 270}` and the identical committed sample and checkpoint,

    A'_θ = Resize₂₂₄( Rot_θ( I ) )        A'_θ,M = Resize₂₂₄( Rot_θ( M I ) )

i.e. **the exact released preprocessing** (`Resize((224,224))` on the full
cutout, as in `run_injection_scale20k.py`), with no crop and no interpolation
anywhere in the chain. The angle set is closed under negation mod 360, so the
production equivariant triple at each θ follows in closed form as before.

**Statistic (unchanged in form).** `d_nocrop(θ) = P(L(0) ≠ L(θ))` on galaxies
labelled spiral at both orientations, and the bound
`D ≤ 1 − max_{θ∈{90,180,270}} d_nocrop(θ)`, with the same 1,000-resample
galaxy-level cluster bootstrap. `θ = 180` is reported separately as the
assumption-free anchor: a cutout rotated by 180° depicts the same galaxy at the
same position angle (PA is defined mod 180°), so the two error rates are equal
by construction and no PA-uniformity argument is needed at all.

**Threshold.** Unchanged: a deficit is declared only if the effect exceeds 3σ of
its cluster-bootstrap error. `d_nocrop` is the number that will be propagated to
P4′; the cropped-grid `d` and `ε(φ)` are reported beside it, never instead of
it, and if `d_nocrop` comes back consistent with 0 the whole bound is reported
as a null at its achieved precision.

**Positive control, unchanged:** `θ = 0` and `θ = 180` must satisfy the exact
TTA identity `eq_cw(Y) = eq_ccw(X)` at machine precision.

# ADDENDUM A2 — recorded deviations from the original text

1. **S2 wording.** The original S2 said the hard-class exact-swap fraction must
   be `1.000000`. The claim it encodes is the identity on the equivariant
   triples; the class swap is that identity composed with `argmax`, which is
   undefined at an exact `eq_cw == eq_ccw` tie. Such ties exist (a saturated
   galaxy at `eq = (0.5, 0.5, 7×10⁻¹²)`), and `argmax` then sends both `X` and
   `Y` to CW. S2 is therefore evaluated as: identity residual exactly `0.0`,
   **and** class-swap fraction exactly 1 among non-tied galaxies, with the tie
   count reported.
2. **S6 axis source.** The pre-registration cited the strict-subset dipole axis
   as coming from `../full_parent/row16i_full_parent_dipole.json`. That file
   carries the *full-parent* axis (278.63°, +25.32°); the strict-887,472 axis
   (195.5°, −57.2°) is in
   `../full_parent/ROW16IB_AXIS_SHIFT_2026-09-04.md` line 95. Both splits are
   reported.
