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
error bar that omits its dominant term — see §5 — and the design first reaches
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
