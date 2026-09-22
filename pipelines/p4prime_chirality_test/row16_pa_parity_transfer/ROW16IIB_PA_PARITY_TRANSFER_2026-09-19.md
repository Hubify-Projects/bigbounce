# Row 16(ii-b) — how much of a real handedness reversal survives the released P4′ chirality pipeline?

**Pre-registered** in `PREREGISTRATION_2026-09-19.md`, git `12248d70`, committed
before any statistic in this document was computed. Lane `bb-LS-ledger16`,
2026-09-19, local CPU/MPS, no rented GPU, no new data downloaded.
Manifest: `reproducibility/manifests/experiments/row16iib-pa-parity-transfer.json`.

---

## 1. Why this, and not a larger N

Row 16(ii) proposed "the same pixel-parity injection at larger N" as its next
step. That step is declined here, on a derivation and a number.

*The derivation.* The production post-processing (`equivariant_postprocess.py`)
is a 2-fold horizontal-flip test-time average,
`eq_cw(I) = (p_cw(I) + p_ccw(MI))/2`, `eq_ccw(I) = (p_ccw(I) + p_cw(MI))/2`,
`eq_ns(I) = (p_ns(I) + p_ns(MI))/2`. Since `MM = 1`, this is **exactly**
antisymmetric under the detector-aligned mirror — `eq_cw(MI) = eq_ccw(I)`,
`eq_ns(MI) = eq_ns(I)` — for every image, with no reference to the network's
weights. The row 16(ii) injection *is* that mirror. So the hard-argmax class of
a pre-mirrored image is the CW↔CCW swap of the original class, identically, and
for the paper's statistic `A = 2N_CW/(N_CW+N_CCW) − 1` the injection curve obeys
`E[A(f)] = A₀(1−2f)` at every `N`. The experiment is a relabelling theorem.

*The number* (statistic S4, `s4_n20k_slope_reanalysis.json`). Beyond being
uninformative in principle, the committed N = 20,000 result was quoted with an
error bar that omits its dominant term — see §7 — and the design first reaches
3σ power at `N ≈ 7.3 × 10⁵`.

So this step instead runs the injection that **breaks** the identity.

## 2. What a genuine handedness reversal actually is

Mirroring an image about the detector x-axis reverses handedness *and* maps the
galaxy's position angle `PA → −PA`. A physical handedness reversal leaves the
galaxy where it is, at the position angle it has. The counterfactual image is
therefore the mirror **about the galaxy's own major axis**,

    I_counterfactual = R(2·PA) · M · I ,

i.e. mirror, then rotate by `φ = 2·PA` to restore the observed orientation.
That composite is *not* the pipeline's TTA symmetry — the TTA averages over one
mirror, never over rotations — so its transfer efficiency is a genuine, unknown
property of the released classifier, and it is the calibration P4′ does not
have.

## 3. Measurement

For each of the **19,800** Legacy DR9 cutouts already cached from the row 16(ii)
sample (no new downloads; the 200 missing are the 2026-09-04 fetch failures,
left absent rather than replaced), and for
`φ ∈ {0, 45, 90, 135, 180, 225, 270, 315}°` — eight angles, uniformly spaced
over the circle (an unbiased marginalisation over a uniform PA distribution)
and closed under negation mod 360 —

    A_φ = Resize₂₂₄( CentreCrop₁₀₆( Rot_φ( I   ) ) )
    B_φ = Resize₂₂₄( CentreCrop₁₀₆( Rot_φ( M I ) ) )

were pushed through the committed classifier
(`bamfai/galaxy-chirality-v2 @ 237d021c…`, the identical revision pin used by
row 16(ii)): 316,800 forward passes on local MPS. The 106 px centre crop keeps
every retained pixel inside the original frame at every angle
(`106·√2/2 = 74.95 ≤ 75`) and is applied at `φ = 0` too, so rotation is the only
thing that changes across the grid. `φ ∈ {0, 90, 180, 270}` use PIL transposes,
which are exact pixel permutations carrying **no interpolation artefact at
all**; `45/135/225/315` use bicubic.

Because the centre crop is mirror-symmetric,
`M·Crop·Rot_φ = Crop·Rot_{−φ}·M`, so with `X_φ = A_φ` (observed galaxy at
rotation φ) and `Y_φ = B_φ` (parity-flipped galaxy, PA restored, same rotation)
the production equivariant triple is available in closed form from those two
forward passes per angle, with no further inference.

**Positive control (S2).** At `φ = 0` and `φ = 180` the mirror commutes with the
rotation, so the TTA identity is exact and the run must return a CW↔CCW swap
for *every* galaxy. It does: exact-swap fraction `1.000000` at both angles.
Nothing downstream is reported unless this holds.

## 4. The dilution bound (derived from the pre-registered S5)

A galaxy's true handedness `h` does not depend on the orientation at which it is
presented. Let `L(θ)` be the pipeline's label for the galaxy rotated by `θ`. Any
disagreement between `L(0)` and `L(θ)` therefore *proves* a label error in at
least one of the two. The survey presents each galaxy at its own position angle,
uniformly distributed and independent of the galaxy's intrinsic properties, so
the population error rate `e = P(L ≠ h)` is the same at every `θ`. The union
bound then gives

    d(θ) ≡ P( L(0) ≠ L(θ) )  ≤  P(L(0)≠h) + P(L(θ)≠h) = 2e ,

so `e ≥ d(θ)/2`. The TTA's exact mirror-antisymmetry makes the error process
parity-symmetric, so a true population asymmetry `A_true` appears in the labels
diluted by `D = 1 − 2e`, and therefore

    **D ≤ 1 − d(θ)   for every θ,   hence   D ≤ 1 − max_θ d(θ).**

A dilution `D` means the paper's observed-label sensitivity floor corresponds to
a physical-parity floor `A₉₅ / D`. This is exactly the "observed-to-physical
bridge factor" that P4′ carries as the illustrative, non-adopted `g = 0.398`
(which is `2 × 0.6991 − 1`, i.e. the Galaxy-Zoo-1 chirality-agreement rate of
its Table `tab:gz1_confusion`). The bound above is an **independent** handle on
the same quantity, derived with no human truth labels at all — only the fact
that handedness is rotation-invariant. `d` is measured on galaxies labelled
spiral at **both** orientations, so the NOT_SPIRAL channel cannot inflate it,
and it is quoted from the exact-rotation angles only, so no resampling artefact
can inflate it either.

---

## 5. Result

**A genuine handedness reversal does not survive the released P4′ chirality
pipeline. It is registered as a reversal in only about two thirds of galaxies.**

The pre-registered primary statistic, marginalised over the six informative
angles:

    eps_bar_informative = 0.6363 +- 0.0024   (z = -149.8 vs unity)

The pre-registered threshold of §7.2 — "deficit declared iff
`eps_bar_informative < 1` by more than 3σ of its cluster-bootstrap error" — is
met by a very wide margin, on the threshold exactly as written before the run.
Verdict in the results JSON: `PA-DEPENDENT PARITY-TRANSFER DEFICIT DETECTED`.

**Positive control (S2) passed first.** At the two angles where the mirror
commutes with the rotation the TTA identity must hold exactly, and it does: the
maximum identity residual `max |eq_cw(Y) − eq_ccw(X)|` is **exactly 0.0** at
both φ = 0 and φ = 180, and the class-swap fraction among non-tied galaxies is
exactly 1 (4 and 3 exact `eq_cw == eq_ccw` ties respectively; see §11.1). Nothing
below would have been reported had this failed.

### 5.1 Per angle (N = 19,800 galaxies, cluster bootstrap over galaxies, 1,000 resamples)

`ε` = parity flip correctly registered, `ρ` = handedness *retained* (an outright
error), `L` = leaked out of the spiral set into NOT_SPIRAL, `R` = class
stability of the *unflipped* galaxy under the same rotation (S5, no parity
operation at all), `ε_obs` = post-hoc transfer against the orientation the
catalogue actually saw, `X_0`.

| φ [deg] | ε(φ) | ρ(φ) | L(φ) | R(φ) | ε_obs(φ) | role |
|---|---|---|---|---|---|---|
| 0 | 0.9999 ± 0.0001 | 0.0001 | 0.0000 | 1.0000 | 0.9999 | control (exact) |
| 45 | 0.6115 ± 0.0038 | 0.3540 | 0.0345 | 0.6463 | 0.6246 | informative |
| 90 | 0.6818 ± 0.0037 | 0.2892 | 0.0290 | 0.6564 | 0.6127 | informative |
| 135 | 0.6167 ± 0.0039 | 0.3504 | 0.0329 | 0.6389 | 0.6166 | informative |
| 180 | 1.0000 ± 0.0000 | 0.0000 | 0.0000 | 0.7225 | 0.6816 | control (exact) |
| 225 | 0.6160 ± 0.0039 | 0.3501 | 0.0339 | 0.6457 | 0.6098 | informative |
| 270 | 0.6801 ± 0.0037 | 0.2881 | 0.0318 | 0.6590 | 0.6076 | informative |
| 315 | 0.6119 ± 0.0038 | 0.3543 | 0.0338 | 0.6518 | 0.6178 | informative |

`ε_bar` over all eight angles is 0.7272; over the six informative angles,
0.6363 ± 0.0024. Figure: `fig_row16iib_pa_parity_transfer.png` (left panel).

Three features of this table are worth stating explicitly, because each one
closes off an "it's an artefact of the test, not the pipeline" reading:

1. **The failure mode is a wrong handedness, not a refusal to answer.** `ρ ≈
   0.29–0.35` — a third of galaxies keep the handedness they had *after their
   chirality was physically reversed* — while `L ≈ 0.03` is an order of
   magnitude smaller. The pipeline is confidently wrong, not abstaining.
2. **The deficit is a rotation effect, not a parity effect.** `ε(φ)` tracks
   `R(φ)` almost exactly at every informative angle (e.g. 0.6818 vs 0.6564 at
   90°, 0.6119 vs 0.6518 at 315°). The classifier is simply not rotation-
   equivariant, and the two-element flip TTA does nothing about that. The parity
   operation itself transfers perfectly wherever the TTA covers it (φ = 0, 180).
3. **The 90/270 pair sits above the 45/135/225/315 quartet** (0.68 vs 0.61–0.62).
   Those are exactly the angles reachable by a lossless pixel transpose, so the
   ~0.07 gap is the bicubic-interpolation penalty. The measured deficit survives
   with no interpolation anywhere — see §6.

### 5.2 The catalogue's own high-confidence cut

Restricting to the selection the released catalogue itself applies
(`primary_hc`: spiral **and** `max(eq_cw, eq_ccw) > 0.6`, from
`build_apjs_release_v1_0_244.py:163-168`), N = 7,982 of 19,800:

    eps_bar_informative = 0.7262 +- 0.0032   (still ~85 sigma below unity)

and the post-hoc confidence-decile stratification runs monotonically from
`ε_bar = 0.577` in the lowest-confidence decile to `0.778` in the ninth. The
deficit is *reduced* by confidence selection and is nowhere close to removed by
it. There is no cut of the released catalogue on which `ε = 1`.

## 6. The same measurement on the exact released preprocessing (addendum A1)

The eight-angle grid of §5 uses a 106 px centre crop, so that every retained
pixel comes from inside the original frame at every angle. Addendum A1 — written
and committed before the statistic it governs was computed — recorded that this
crop is *not* benign: only **68.3%** of galaxies keep the class they have under
the committed uncropped 150 px preprocessing
(`POSTHOC_crop_effect_on_baseline`). The crop is common-mode between `X_φ` and
`Y_φ`, so it cannot manufacture a parity asymmetry, but it can inflate the
classifier's intrinsic noise, and every number propagated to P4′ must be free of
it.

A second inference stage therefore repeated the measurement with **no crop and
no interpolation at all** — `Resize₂₂₄` of the full 150 px cutout, which is
literally the released preprocessing, with rotations restricted to the lossless
transposes θ ∈ {0, 90, 180, 270} — 158,400 further forward passes. Sanity check:
at θ = 0 this chain *is* the committed pipeline, and its classes agree with the
committed catalogue values on **99.99%** of the 19,800 galaxies (the residual is
the tie set). The positive control passes again at θ = 0 and 180 (identity
residual exactly 0.0, non-tie class swap exactly 1).

| quantity (released preprocessing, no crop) | all galaxies (N = 19,800) | `primary_hc` (N = 7,982) |
|---|---|---|
| `ε̄` co-rotated, informative θ ∈ {90, 270} | 0.6704 ± 0.0038 (z = −87.3) | 0.7543 ± 0.0048 (z = −51.1) |
| `ε̄` vs the observed frame `X_0`, θ ∈ {90, 180, 270} | 0.6289 ± 0.0028 (z = −131.6) | 0.7237 ± 0.0036 (z = −76.6) |
| `d(90)` label self-disagreement | 0.3704 | 0.2822 |
| `d(180)` label self-disagreement | 0.3072 | 0.2113 |
| `d(270)` label self-disagreement | 0.3627 | 0.2834 |
| **`D ≤ 1 − max_θ d(θ)`** | **0.6296 ± 0.0040** (z = −93.5) | **0.7166 ± 0.0047** (z = −60.2) |
| `D ≤ 1 − d(180)` (assumption-free anchor) | 0.6928 ± 0.0038 | 0.7887 ± 0.0047 |

Artifacts: `s5b_nocrop_dilution.json` (the pre-registered addendum-A1 statistic)
and `posthoc_nocrop_eps.json` (the post-hoc `ε` on the same probabilities; that
file labels itself post-hoc in its first field and is never used to decide the
pre-registered threshold). Removing the crop *raises* `ε̄` from 0.636 to 0.670 —
about a third of a bicubic-penalty's worth — and leaves the deficit at 87σ. The
crop is not the cause.

The `θ = 180` row deserves separate mention because it needs no assumption at
all. Position angle is defined mod 180°, so a cutout rotated by 180° depicts the
same galaxy at the same position angle; the two error rates are therefore equal
by construction, with no appeal to PA uniformity. On that row alone the released
pipeline changes its own answer for **21.1%** of high-confidence spirals
(30.7% of all spirals) when handed a lossless 180° rotation of the identical
image.

## 7. The corrected error bar on the N = 20,000 row 16(ii) slope (S4)

Pre-registered statistic S4, re-analysis only, no new inference; input is the
committed `../injection_pilot/scale20k_pairs.parquet`; output
`s4_n20k_slope_reanalysis.json`, reproduced byte-identically in this lane.

The committed row 16(ii) headline quoted `dA/df = +0.0167 ± 0.0089`, where the
`± 0.0089` is `analyze_injection_scale20k.py`'s `boot_se_spiral_classified` — a
bootstrap at a *fixed* injection realisation, i.e. galaxy-sampling noise only.
The dominant term is the hypergeometric fluctuation in *which* galaxies land in
the injected subset, which the committed analysis never propagated. Re-running
the exact committed design (5 fractions × 10 seeds) 2,000 times:

| statistic | exact identity | committed slope | correct SE | σ from identity |
|---|---|---|---|---|
| hard, spiral-classified (the paper's `A`) | −0.011791 | +0.029671 | 0.023754 | **1.75** |
| soft, mean over all classes | −0.009337 | +0.016726 | 0.011454 | **2.28** |

The Monte-Carlo mean recovers the identity (−0.012472 vs −0.011791; −0.009606 vs
−0.009337), which validates the null. So there is **no discrepancy**: the
measured slope is consistent with the exact label identity at 1.8σ / 2.3σ, and
the "2.9σ unresolved discrepancy" in P4′ v4P.0.9 is an artefact of the missing
error term. The measured SE scaling exponent over N ∈ {2500, 5000, 10⁴, 2×10⁴}
is **−0.5009** (i.e. √N, measured rather than assumed), from which the design
first reaches 3σ power at **N ≈ 7.26 × 10⁵**. Figure: right panel.

## 8. Supporting statistics

**S6 — sky dependence.** `ε̄_informative` split on the P4′ strict-887,472 dipole
axis (195.5°, −57.2°): 0.6578 north (n = 7,959) vs 0.6222 south (n = 11,841),
Δ = +0.0356 ± 0.0050 (z = +7.1). On the full-parent axis (278.63°, +25.32°):
0.6194 vs 0.6547, Δ = −0.0353 ± 0.0050 (z = −7.0). The transfer efficiency is
**not** uniform on the sky at the few-percent level. This is a systematic in its
own right — a position-dependent dilution can imprint a spurious dipole — but
this lane deliberately stops at reporting it; quantifying its dipole projection
is a separate pre-registered step (see §10).

**S3 — injection-recovery slope by angle.** The per-angle `dA_cls/df` values
scatter around, and are individually consistent with, the identity slopes
implied by each angle's own `A₀`; with only 200 seeds per angle and `A₀` values
of order 10⁻² the per-angle slopes carry no independent information (the
`slope_over_identity` column ranges from −1.80 to +1.51). Reported for
completeness, as pre-registered; no claim is made from it. The S4 power
calculation above is the quantitative statement about this channel.

## 9. What this means for P4′

**The null stands; its conversion factor to physical parity does not.**

P4′ measures an asymmetry in *labels*. Its strict-887,472 result, `A₉₅ = 0.98%`,
is a bound on the observed-label amplitude. Converting that to a bound on a
physical spin-parity asymmetry requires the bridge factor `D` — the dilution a
true population asymmetry suffers on its way through the classifier — and the
label-level bound as written implicitly assumes `D = 1`, i.e. that a genuine
handedness reversal is registered as one. That assumption is now excluded at
60σ on the paper's own selection and preprocessing.

Quantitatively, with `A₉₅^phys = A₉₅^obs / D` and the `primary_hc` bound of §6:

- `D ≤ 0.7166 ± 0.0047` ⇒ **`A₉₅^phys ≥ 1.37%`**
- assumption-free θ = 180 anchor, `D ≤ 0.7887` ⇒ `A₉₅^phys ≥ 1.24%`

This is an *upper* bound on `D`, hence a *lower* bound on the physical
sensitivity floor: P4′ cannot claim better than ~1.4% in physical-parity units,
whatever else is true. Three consequences:

1. **It is consistent with, and independent of, the paper's illustrative GZ1
   bridge.** P4′ carries `g = 0.398` (= 2 × 0.6991 − 1, the Galaxy-Zoo-1
   chirality-agreement rate of its Table `tab:gz1_confusion`) as an
   illustrative, non-adopted factor implying `A₉₅^phys ≈ 2.46%`. Since
   0.398 ≤ 0.7166, the two are compatible: the new bound brackets `g` from
   above and does not contradict it. What is new is that the bracket is derived
   **with no human truth labels at all** — only the fact that handedness does
   not depend on the orientation at which a galaxy is presented — so it no
   longer rests on transferring a GZ1-era agreement rate onto a DR9 catalogue.
2. **The comparison to the Popławski/Shamir axis is unaffected in direction and
   sharpened in honesty.** The relevant amplitudes there are `≲ 0.2%`; a
   physical floor of `≥ 1.37%` is well above them either way. The paper should
   say so in physical units rather than leaving the reader to assume the label
   bound is the physical bound.
3. **The v4P.0.9 robustness paragraph states the opposite of what the algebra
   requires.** "The production pipeline suppresses pixel-level parity leakage
   well below what the label-level injection model alone would predict" is a
   claim about a mirror injection that is *exactly* the TTA's own symmetry, so
   it transfers with unit efficiency by construction and measures nothing about
   the classifier (§1). The exact sentences P4′ should carry instead, with their
   artifact citations, are in `PROPAGATION_NOTE.md` (P-1 … P-5).

**This is a calibration result, not a retraction.** Nothing here moves the
central value of the P4′ dipole, and nothing here makes the null less of a null.
It changes the units in which the null's strength is quoted, and it removes
three numbers (`47σ`, `2.9σ`, `≈26%`) that were computed against inapplicable
identities.

## 10. What this means for the GPU program (rows 13 and 16(ii))

This is a decision input for Houston, stated as three separate findings so the
parts can be accepted separately.

**(a) The mirror-injection-at-larger-N step is retired — on a derivation, not on
a null.** Row 13 and row 16(ii) both proposed scaling the pixel-level parity
injection to larger N on a rented GPU. That injection is the detector-aligned
mirror `M`, and the production post-processing is a 2-fold `M`-TTA, so
`eq_cw(MI) = eq_ccw(I)` identically for every image, independent of the
network's weights (§1). The experiment is a relabelling theorem: `E[A(f)] =
A₀(1 − 2f)` at every N, with no information content. S4 puts a number on it —
the design first reaches 3σ power at `N ≈ 7.3 × 10⁵`, and at that N it would
only confirm the theorem. **No GPU hours should be spent on this step.** The
retirement rests on the identity, which no increase in N can remove; it does not
depend on any statistic in this document.

**(b) The pre-registered kill condition did NOT fire, and is recorded as not
firing.** §7.4 required *both* `|z| < 3` on the committed slope (satisfied:
z = 1.75) *and* `ε̄ = 1` within errors. `ε̄ = 0.6363 ± 0.0024` is not 1, so the
second clause fails, and the channel is therefore **not** recorded as
"calibrated and uninformative" as that condition would have had it. The
threshold is not moved after the fact. The honest reading is that the kill
condition conflated two different injections: the *mirror* injection is
uninformative (and is retired under (a), on its own derivation), while the
*PA-restoring* injection this lane substituted is highly informative, which is
the opposite of the outcome the kill condition was written to describe.

**(c) The GPU ask should be redirected, not cancelled.** The question the GPU
program existed to answer — "does a real handedness reversal survive the
released pipeline?" — is now answered, at `ε̄ = 0.67 ± 0.004` on the exact
released preprocessing, in **74 minutes of local Apple-MPS inference at zero
marginal cost**. The error bar is already 0.4%; increasing N would shrink a bar
that is not the limiting factor. What the result *creates* is a much stronger
case for the GPU step that was always the expensive one:

- **Row 16(iii) — retrain a D4-equivariant classifier — becomes the highest-value
  GPU item in the program.** The measured deficit is a rotation-equivariance
  failure, not a parity failure (§5.1 point 2): `ε(φ)` tracks the rotation-only
  stability `R(φ)` at every angle, and the parity operation transfers perfectly
  wherever the TTA covers it. A backbone equivariant under the full dihedral
  group D4 — or, failing a retrain, an 8-fold rotation TTA over the existing
  weights — removes exactly this failure mode and would raise `D` toward 1,
  which is the only way the label bound and the physical bound converge.
- **An 8-fold rotation TTA over the existing checkpoint is a local-CPU/MPS
  experiment, not a GPU one**, and should be run before any retrain is costed:
  it bounds how much of the deficit is recoverable without new training. The
  probabilities needed for a 4-fold version are already in `nocrop_probs.npz`.
- **Rows 16(i), (iv), (iv-b) and (v) are untouched by this result.** (v) — the
  Euclid Q1 domain-adaptation pathfinder — remains a genuine GPU item on its own
  merits.

**Recommendation to Houston, in one line:** cancel the mirror-injection
N-extension (a dead channel by algebra), keep the GPU budget, and spend it on
row 16(iii) D4-equivariant retraining — after the zero-cost 8-fold-rotation-TTA
bound says how much the retrain can buy.

Two further zero-cost steps this result opens, neither run here, neither
pre-registered here:

1. **Project the S6 sky dependence onto a dipole.** `ε̄` varies by ±3.6% between
   hemispheres at 7σ; a position-dependent dilution can imprint a spurious
   dipole in the observed labels. This needs its own pre-registration and is not
   claimed either way in this document.
2. **Recompute `d(180)` on the full 8.47M parent.** It requires one lossless
   180° rotation pass and no new cutout downloads, and it would turn the bound
   of §6 from a 19,800-galaxy estimate into a catalogue-wide one.

## 11. Recorded deviations from the pre-registration

Deviations are recorded here, never silently, per §"Errors and nulls" of the
pre-registration.

1. **S2 wording (already recorded as addendum A2.1).** The pre-registration
   phrased the control as "the exact-swap fraction of the hard classes must be
   1.000000". The underlying claim is the identity on the equivariant triples;
   the class swap is that identity composed with `argmax`, which is undefined at
   an exact `eq_cw == eq_ccw` tie. Such ties exist (a saturated galaxy at
   `eq = (0.5, 0.5, 7×10⁻¹²)`) and `argmax` then sends both `X` and `Y` to CW.
   S2 is therefore evaluated as: identity residual exactly `0.0` (it is), **and**
   class-swap fraction exactly 1 among non-tied galaxies (it is), with the tie
   count reported (4 at φ = 0, 3 at φ = 180 on the cropped grid; 5 and 8 on the
   no-crop grid).
2. **S6 axis source (already recorded as addendum A2.2).** The pre-registration
   cited `../full_parent/row16i_full_parent_dipole.json` for the strict-subset
   axis; that file carries the *full-parent* axis (278.63°, +25.32°). The
   strict-887,472 axis (195.5°, −57.2°) is in
   `../full_parent/ROW16IB_AXIS_SHIFT_2026-09-04.md` line 95. Both splits are
   reported.
3. **Bootstrap standard errors were regenerated in this lane.** The results JSON
   checkpointed on 2026-09-19 was written by `s1_pa_transfer_analysis.py` one
   edit before its final state (the S6 `delta_boot_se` / `delta_z` block was
   added a minute later). Re-running the committed script reproduces **every
   point estimate exactly** and shifts three bootstrap standard errors in the
   third significant figure — `S5b_dilution_bound.D_upper_bound_boot_se`
   0.003617 → 0.003719, `POSTHOC_primary_hc_subset.eps_bar_informative_boot_se`
   0.003549 → 0.003232, `POSTHOC_primary_hc_subset.S5b_D_upper_bound_boot_se`
   0.004572 → 0.004849 — because the added S6 bootstrap draws from the same
   seeded RNG stream and re-orders it. No headline number is affected
   (`S1_eps_bar_informative_boot_se` is unchanged at 0.0024). The re-run values
   are the ones committed and quoted here. `s4_n20k_slope_reanalysis.json`
   re-runs byte-identically.
4. **The addendum-A1 and post-hoc no-crop analyses were run in this lane, not in
   the original one.** The 2026-09-19 lane's process ended after the stage-2
   inference completed but before `s5b_nocrop_dilution.py` was ever executed;
   the stored probabilities were untouched and the script is the one committed
   at that time. `posthoc_nocrop_eps.py` is new in this lane and is labelled
   post-hoc in its own first output field, in §6, and here.
5. **Nothing was re-run on new data and no threshold was changed.** The §7.2
   deficit threshold and the §7.4 kill condition are evaluated exactly as
   written; §10(b) records that the kill condition did not fire.

## 12. Reproduction (directive Q2)

Manifest: `reproducibility/manifests/experiments/row16iib-pa-parity-transfer.json`.

| | |
|---|---|
| **Venue** | local workstation `code-you-2d-MacBookAir24GB`, Apple Silicon MPS (Metal), macOS arm64. **No rented GPU.** |
| **Marginal cost** | **$0.00.** No pod, no API spend, no new downloads. |
| **Wall clock, stage-1 inference** | 2,965 s = **49.4 min** — 19,800 galaxies × 8 angles × 2 mirror states = 316,800 forward passes, 6.7 gal/s (`inference.log`) |
| **Wall clock, stage-2 inference (addendum A1)** | 1,489 s = **24.8 min** — 19,800 × 4 lossless rotations × 2 = 158,400 forward passes, 13.2 gal/s (`nocrop.log`) |
| **Wall clock, all analysis** | **< 15 s combined**, CPU only: `s1_pa_transfer_analysis.py` 4 s, `s4_reanalyse_n20k_slope.py` 2 s, `s5b_nocrop_dilution.py` < 1 s, `posthoc_nocrop_eps.py` 2 s, `make_figures.py` 2 s |
| **Total** | **≈ 75 min end-to-end**, single machine, reproducible offline once the cutout cache exists |
| **External data** | Legacy Survey DR9 `jpeg-cutout` 150 px, layer `ls-dr9` (NOIRLab, CC-BY-4.0), already cached from the 2026-09-04 row 16(ii) run — 19,800 of 20,000; the 200 absent are that run's fetch failures, left absent rather than replaced |
| **Model** | `bamfai/galaxy-chirality-v2` @ `237d021c451d75cf86a875e86d4de498b74e2f12`, file `chirality_model_v2_best.pt` — the identical revision pin used by row 16(ii) and asserted in the runner |
| **Environment** | python3.14, torch 2.13.0, timm, PIL, pandas, numpy, huggingface_hub, matplotlib |
| **Resume** | `run_pa_transfer_inference.py` checkpoints every 2,000 galaxies and resumes when the cached-index list matches |
| **Determinism** | every bootstrap and injection stage is seeded (`default_rng(20260919)`, `default_rng(31415)`); S4 reproduces byte-identically, S1 reproduces every point estimate exactly (see §11.3) |

Order of execution, from a clean checkout with the cutout cache present:

    python3 run_pa_transfer_inference.py      # 49 min, writes pa_transfer_probs.npz
    python3 run_exact_rotation_nocrop.py      # 25 min, writes nocrop_probs.npz
    python3 s1_pa_transfer_analysis.py        # -> s1_pa_transfer_results.json
    python3 s4_reanalyse_n20k_slope.py        # -> s4_n20k_slope_reanalysis.json
    python3 s5b_nocrop_dilution.py            # -> s5b_nocrop_dilution.json
    python3 posthoc_nocrop_eps.py             # -> posthoc_nocrop_eps.json  (post-hoc)
    python3 make_figures.py                   # -> fig_row16iib_pa_parity_transfer.png

Every S3/S4 grid point is evaluated in closed form from the stored
probabilities; no stage re-runs inference.
