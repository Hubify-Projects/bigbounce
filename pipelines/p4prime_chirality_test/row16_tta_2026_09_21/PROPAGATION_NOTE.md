# PROPAGATION NOTE — lane `bb-LS6-row16-tta` → P4′ (paper owned by another lane)

**From** lane `bb-LS6-row16-tta`, 2026-09-21/22. **Do not edit `main.tex` from
this lane.** Items are numbered Q-n so they do not collide with the row-16(ii-b)
note's P-1…P-5 (`../row16_pa_parity_transfer/PROPAGATION_NOTE.md`). Every number
below is read from a committed JSON in this directory; nothing is estimated.

Target: `pipelines/p4prime_chirality_test/paper/main.tex` — Assumption 2 of
§`sec:bh`, §`sec:robustness_disclosure`, and the dipole-limit discussion.

---

## Q-1 — HOLD the row-16(ii-b) dilution bound. Do not print `D ≤ 0.7166` or `A₉₅^phys ≥ 1.37 %` yet.

**Status: BLOCKING, on item P-5 of the row-16(ii-b) propagation note.** Not a
retraction — a hold, with a named test that lifts it.

Row 16(ii-b) measured its dilution bound on Legacy Survey **viewer cutouts**
(`jpeg-cutout?…&size=150&layer=ls-dr9`, a 39.3″ field upsampled 150 → 224),
taken from the `image_url` column that `run_eq_fast.py:265-270` appends to
`catalog_production.parquet` for display. The catalogue's own inference ran on
the **`Smith42/galaxies`** images the paper documents at
`main.tex:171` — 224 × 224 px, `grz`, 0.262″/px, DESI Legacy DR8, a 58.7″ field
at native resolution (`run_eq_fast.py:37`).

Re-running the released preprocessing through the released checkpoint on the
viewer cutouts reproduces the released catalogue's class for **43.9 %** of
19,800 galaxies (42.4 % and 44.7 % on two further independent draws), against
**99.99 %** agreement with the row-16 lane's own committed forward passes —
so the implementation is right and the images are different
(`p_d180_catalogue_wide.json → positive_controls`,
`posthoc_provenance_diagnostic.json`, `posthoc_fov_test.json`).

Therefore: `D ≤ 0.7166 ± 0.0047`, `D ≤ 0.6296`, `A₉₅^phys ≥ 1.37 %`, and every
`d(θ)` in row 16(ii-b) §6 are **out-of-domain** measurements. An out-of-domain
instability bounds the in-domain one in neither direction.

**What lifts the hold:** re-run the θ ∈ {0, 90, 180, 270} pass on images pulled
from `Smith42/galaxies` at the pinned revision
`bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2` (provenance table entry A1) and
re-derive `d(θ)` and `D` there. Bounded work; needs disk, not a GPU.

**What is NOT affected** (print these as already drafted): row-16(ii-b) items
P-1…P-4 — the corrected error bar on the N = 20,000 slope, the withdrawal of the
`47σ`, `2.9σ`, `0.038` and `≈ 26 %` numbers, and the retirement of the
mirror-injection extension. Those are re-analyses of committed label-level
quantities and of the exact identity `eq_cw(MI) = eq_ccw(I)`, which holds for
any image whatsoever. No image enters them.

### Q-1a — what P4′ CAN say today, if a sentence is needed now

Printable as written, with no image-domain dependence:

> The production post-processing averages over the horizontal mirror only, so it
> is exactly antisymmetric under a detector-aligned reflection but carries no
> invariance under rotation; a ViT-S/16 backbone supplies none. A genuine
> handedness reversal leaves a galaxy at its observed position angle and is
> therefore *not* the detector-aligned mirror, so the assumption that it is
> transmitted into the catalogue label with unit efficiency is not supported by
> the architecture. We quantify the resulting dilution in a companion
> calibration and quote the observed-label bound here without asserting
> `D = 1`.

## Q-2 — `d(180°)` on the largest feasible sample (for the calibration, once Q-1 is lifted)

`p_d180_catalogue_wide.json`. The de-duplicated union of all three committed
cutout caches — **N = 25,254** galaxies, 46 duplicates removed, three
independent draws (seeds 42/43/44, two sky-sampling resolutions) — gives, on the
exact released preprocessing with a lossless 180° transpose and no interpolation
anywhere:

> `d(180°) = 0.3090 ± 0.0034`, i.e. `D ≤ 0.6910 ± 0.0034`
> (`0.2501 ± 0.0057` → `D ≤ 0.7499` on the catalogue's
> `primary_hc ∧ ¬raw_flip_qc_unsafe` selection).

The three draws agree within errors (0.3072 ± 0.0037, 0.3116 ± 0.0075,
0.3497 ± 0.0252), and the N = 19,800 value reproduces row 16(ii-b) §6 exactly
from an independently written analysis path. A literal full-parent `d(180°)`
was declared infeasible in advance (it needs a forward pass per galaxy per
orientation on the image; no parent cutouts are cached). **This number carries
the Q-1 hold with it.**

## Q-3 — the sky-dependence systematic. This one needs a sentence in the paper.

`s_sky_dipole.json`. The row-16(ii-b) §8 hemisphere asymmetry is a genuine
dipole in the classifier's parity-transfer efficiency: fractional amplitude
`a_δ = 0.090 ± 0.010` toward (123.2°, −72.8°), at z = +10.9 against 1,000
random permutations of the per-galaxy efficiency across sky positions (rank
p ≤ 0.001; 0 of 1,000 permutations reached the observed amplitude). Its axis
lies **31.6°** from the strict-887,472 dipole axis.

Propagated through P4′'s **own** estimator (`build_projector` imported verbatim,
NSIDE = 64, support ≥ 10; the reproduction is exact — 887,472 galaxies in
23,633 support pixels, `A_obs` matching `row16i_full_parent_dipole.json`), a
dilution modulated in proportion to it imprints a spurious dipole of

> **0.230 % ± 0.026 on the strict-887,472 support — 23 % of that subset's
> `A₉₅^obs = 0.98 %`** — and 0.046 % ± 0.005 on the full-parent support (9 % of
> `A₉₅^obs = 0.51 %`).

The strict subset is the exposed one because its observed label *monopole* is
`+2.55 %`, five times the full parent's and of opposite sign; the same
fractional sky-variation therefore produces five times the spurious dipole.
A pre-registered threshold (`> 10 % of A₉₅`) was fixed before the computation
and it fires.

Suggested sentence for §`sec:robustness_disclosure`, to be finalised after the
Q-1 in-domain re-measurement (the mechanism and the significance are robust; the
amplitude is the part that moves):

> The classifier's parity-transfer efficiency is not uniform on the sky: it
> carries a dipole of fractional amplitude `0.090 ± 0.010` (permutation-null
> rank `p ≤ 0.001`), whose axis lies 31.6° from the dipole axis of the
> high-confidence subset. Because the observed label asymmetry of that subset
> has a non-zero monopole (`+2.55 %`), a dilution modulated in proportion to the
> measured efficiency map imprints a spurious dipole of `0.23 %` in the observed
> labels — 23 % of the `A₉₅ = 0.98 %` limit quoted here. This is a systematic
> floor on the interpretation of the limit, not a detected contamination: it
> assumes the dilution tracks the measured efficiency map, and a true asymmetry
> of zero produces no dipole under any dilution.

Do **not** write "negligible". Do **not** write "the limit is contaminated".
Both overstate what was measured.

## Q-4 — what the classifier calibration can now say about a fix (context, not a paper claim)

`t_tta_recovery.json`, on a 16-angle 22.5° grid built for the purpose (316,800
new forward passes). A rotation test-time average over the **existing** weights
lifts the dilution bound from `D ≤ 0.6237 ± 0.0033` (released, flip only) to
`0.7017 ± 0.0037` (D4: 4 rotations × flip) and `0.7718 ± 0.0035` (D8: 8
rotations × flip) — recovery fractions `F = 0.207 ± 0.010` and
`0.394 ± 0.009`. A D4-equivariant network and a D4 TTA annihilate the same
quantity exactly (both zero the label self-disagreement on the C4 orbit — a
theorem, verified to float32 precision as control T0-C); they differ only in the
off-group residual, which is where four fifths of the deficit lives.

If P4′ wants one sentence about mitigation, this is the defensible one:

> Averaging the released classifier over the rotation group at inference time
> recovers only a fifth (four-fold) to two fifths (eight-fold) of the measured
> dilution gap, so the residual is a smooth-orientation instability rather than
> a discrete symmetry defect, and an equivariant re-architecture alone would not
> remove it.

(Like Q-2, measured on viewer cutouts; the *ratio* is the most transferable
quantity here, but it carries the Q-1 caveat too.)

---

## Ordering for the P4′ lane

1. Print P-1…P-4 from the row-16(ii-b) note now — unaffected, image-independent.
2. Hold P-5 and Q-2 until the `Smith42/galaxies` in-domain re-measurement (Q-1).
3. Add a Q-3 systematic-caveat sentence now, with the amplitude marked as
   preliminary pending the same re-measurement, or wait and print it once — but
   do not ship the dipole limit with the systematic unmentioned.
4. Q-4 is optional context; it belongs in the calibration discussion, not in the
   limit.
