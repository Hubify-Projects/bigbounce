# PROPAGATION NOTE — lane `bb-LS10-indomain-d180` → P4′ (paper owned by another lane)

**From** lane `bb-LS10-indomain-d180`, 2026-09-22. **Do not edit `main.tex` from
this lane** — `bb-L4e-p4p-hold-correction` owns P4′ right now. Items are
numbered R-n so they do not collide with the row-16(ii-b) note's P-1…P-5
(`../row16_pa_parity_transfer/PROPAGATION_NOTE.md`) or the row-16 TTA note's
Q-1…Q-4 (`../row16_tta_2026_09_21/PROPAGATION_NOTE.md`). Every number below is
read from a committed JSON in this directory; nothing is estimated.

Target: `pipelines/p4prime_chirality_test/paper/main.tex` — Assumption 2 of
§`sec:bh`, §`sec:robustness_disclosure`, Table `tab:pixel_calib`, and
§`sec:catalog_schema` (line ~171).

---

## R-1 — the hold is **LIFTED WITH DIFFERENT NUMBERS**. Print these instead.

**Status: resolves item Q-1 of the row-16 TTA note, which held item P-5 of the
row-16(ii-b) note.** Not a retraction of the *argument* — the argument is
unchanged and now measured in-domain. The *numbers* change, in the
conservative direction.

### What was established first (the gate, not the result)

The released catalogue **is** reproducible from the released checkpoint and the
released preprocessing on its documented image source, and only on that source:

| control | agreement with the released catalogue's class |
|---|---|
| in-domain, catalogue scale (8,474,531 galaxies, `e2e_fullrun`, A100, 2026-07-11) | **99.936 %** — and **100.000 %** on the 949,584 `primary_hc` galaxies |
| in-domain, this lane's own 40,000 drawn galaxies at `θ = 0°` | **99.95 %** — **100.000 %** on `primary_hc` |
| out-of-domain viewer cutouts (rows 13/16) | 43.9 % |

Pre-registered in-domain threshold: ≥ 99.0 %. Passed
(`c1_e2e_catalogue_agreement.json`, `s1_indomain_dilution.json`
`control_C2_this_lane`). The domain gap is a 3.41× difference in angular field,
measured not assumed: the in-domain cutouts are 512 × 512 px at 0.262″/px = a
**134.1″** field (median pixel correlation 0.992 against Legacy Survey cutouts
at that scale, ≤ 0.25 at every other grid point, `posthoc_pixel_scale.json`),
against the viewer cutouts' 39.3″ field upsampled 150 → 224.

### The in-domain measurement

Same statistic, same estimator (`eq_triple` imported verbatim from
`s5b_nocrop_dilution.py`), same checkpoint, same released preprocessing, lossless
90° transposes, 40,000 galaxies drawn uniformly from the parent, 320,000 forward
passes (`s1_indomain_dilution.json`):

| selection | N | `D ≤ 1 − max_θ d(θ)` | `D ≤ 1 − d(180°)` (assumption-free) | ⇒ `A₉₅^phys = A₉₅^obs / D` |
|---|---|---|---|---|
| all spirals | 15,219 | `0.5237 ± 0.0038` | `0.5612 ± 0.0044` | `≥ 1.87 %` / `≥ 1.75 %` |
| `primary_hc`, the catalogue's own cut | 4,579 | **`0.5998 ± 0.0065`** | `0.6599 ± 0.0075` | **`≥ 1.63 %`** / `≥ 1.49 %` |
| `primary_hc ∧ ¬raw_flip_qc_unsafe` | 4,296 | `0.6037 ± 0.0070` | `0.6616 ± 0.0076` | `≥ 1.62 %` / `≥ 1.48 %` |

`D` is bounded away from 1 at **61σ** (`primary_hc`) and 127σ (all spirals).
`g = 0.398` still sits below the bound, so P-5's consistency statement holds
unchanged in kind. On the `θ = 180°` row the pipeline changes its own answer for
**34.0 %** of high-confidence spirals handed a lossless 180° rotation of the
identical image (the held figure was 21.1 %).

### The exact substitutions for the already-drafted P-5 / P-5a / P-5b / Q-2 text

Every held sentence stands; only these tokens change.

| where | held value (withdraw) | in-domain value (print) |
|---|---|---|
| P-5 table, `primary_hc`, `D ≤ 1 − max_θ d` | `0.7166 ± 0.0047` | **`0.5998 ± 0.0065`** |
| P-5 table, `primary_hc`, `D ≤ 1 − d(180)` | `0.7887 ± 0.0047` | `0.6599 ± 0.0075` |
| P-5 table, all spirals, both columns | `0.6296 ± 0.0040` / `0.6928 ± 0.0038` | `0.5237 ± 0.0038` / `0.5612 ± 0.0044` |
| P-5 table, `A₉₅^phys` (`primary_hc`) | `≥ 1.37 %` / `≥ 1.24 %` | **`≥ 1.63 %`** / `≥ 1.49 %` |
| P-5 table, `A₉₅^phys` (all spirals) | `≥ 1.56 %` / `≥ 1.42 %` | `≥ 1.87 %` / `≥ 1.75 %` |
| P-5, N per row | 19,800 / 7,982 | **15,219 / 4,579** |
| P-5, `d(180)` self-disagreement sentence | `21.1 %` | **`34.0 %`** |
| P-5, significance of `D < 1` | `60σ` | **`61σ`** |
| P-5a, `\bar\epsilon` and its `51\sigma` | not re-measured in-domain — see R-3 | **cut the `\bar\epsilon` clause**, or keep it with the caveat in R-3 |
| P-5a / P-5b, `D \le 0.717 \pm 0.005` | withdraw | **`D \le 0.600 \pm 0.007`** |
| P-5a / P-5b, `A_{95}^{\rm phys} \ge 1.37\%` | withdraw | **`A_{95}^{\rm phys} \ge 1.63\%`** |
| Q-2, `d(180°) = 0.3090 ± 0.0034` | withdraw (out-of-domain) | `0.4388` (all spirals) / `0.3401` (`primary_hc`) |

Do **not** average the held and in-domain values, and do **not** quote them as a
range. The held values were measured on images the catalogue was not built from;
they are withdrawn, not down-weighted.

### R-1a — ready-to-set replacement for Assumption 2 of §`sec:bh`

Supersedes the P-5a insert. Drops the `\bar\epsilon` clause, which was measured
only out-of-domain (R-3):

> Sec.~\ref{sec:robustness_disclosure} reports a direct measurement of that
> transfer function. Because handedness does not depend on the orientation at
> which a galaxy is presented, the rate at which the released pipeline
> contradicts its own label between two lossless rotations of the \emph{same}
> cutout bounds the dilution $D$ of any true population asymmetry from above,
> with no human truth labels entering the argument. Measured on the catalogue's
> own imaging --- the $512\times512$ DESI Legacy DR8 cutouts the released
> inference ran on --- and on the catalogue's own high-confidence selection,
> $D \le 1 - \max_\theta P\big(L(0) \ne L(\theta)\big) = 0.600 \pm 0.007$, with
> $D$ excluded from unity at $61\sigma$; the $\theta = 180^\circ$ row, which
> requires no assumption about position-angle uniformity, gives
> $D \le 0.660 \pm 0.008$. The observed-label floor $A_{95}^{\rm obs} = 0.98\%$
> therefore corresponds to a physical-parity floor
> $A_{95}^{\rm phys} = A_{95}^{\rm obs}/D \ge 1.63\%$. This is consistent with
> the illustrative $g = 0.398$ used above (which would give $2.46\%$) and
> supersedes it as the quantity we can defend: it is an upper bound on $D$, so it
> can only weaken the exclusion, and we adopt it in that direction only.

### R-1b — ready-to-set replacement for the second paragraph of P-5b

The first paragraph of P-5b (the pixel-injection identity, P-1…P-4) is
image-independent and stands as drafted. Replace only the second paragraph:

> The transfer function is instead measured directly, on the catalogue's own
> imaging. Handedness is a property of the galaxy, not of the orientation at
> which it is presented, so whenever the pipeline returns different chiralities
> for two lossless $90^\circ$ rotations of the same cutout at least one of the
> two labels is wrong; the measured disagreement rate therefore bounds the
> per-orientation error rate and hence the dilution
> $D = 1 - 2e$ of any true population asymmetry from above. On the catalogue's
> high-confidence selection the pipeline contradicts itself for $34.0\%$ of
> spirals handed a lossless $180^\circ$ rotation and for $40.0\%$ over the full
> set of right-angle rotations, giving $D \le 0.600 \pm 0.007$ ($61\sigma$ below
> unity; $D \le 0.660 \pm 0.008$ on the assumption-free $180^\circ$ row alone).
> The deficit is a rotation-equivariance failure rather than a parity failure:
> the two-fold horizontal-flip test-time average renders the parity operation
> exact wherever it commutes with the rotation, which we verify as a positive
> control (the flip identity residual is exactly zero at $0^\circ$ and
> $180^\circ$). The implied dilution raises the physical-parity sensitivity floor
> to $A_{95}^{\rm phys} \ge 1.63\%$, which is the figure we quote.

The hemisphere-asymmetry clause of the held P-5b (`0.036 ± 0.005` between
hemispheres) and the Q-3 dipole sentence are **not** covered by this
re-measurement — see R-3.

## R-2 — §`sec:catalog_schema` line ~171 misstates the parent cutout size

`main.tex:171` reads "$8{,}474{,}566$ images, $224\times224$~px $grz$ cutouts at
$0.262''$/pixel". The pixel scale is right; the size is not. The
`Smith42/galaxies` `v1.0` files the released inference read
(`pipelines/p2_chirality/run_eq_fast.py:37`, `data/train-*`) store **512 × 512
px** RGB JPEG cutouts — verified directly from the pinned revision, and the
0.262″/px scale verified by cross-correlation against Legacy Survey cutouts
(median correlation 0.992 at 0.262″/px, ≤ 0.25 at 0.131, 0.20, 0.35, 0.45 and
0.524; `posthoc_pixel_scale.json`). 224 is the **network input** after the
pipeline's `Resize((224,224))`.

Suggested replacement for the parenthesis:

> (8,474,566 images; $512\times512$~px $grz$ cutouts at $0.262''$/pixel, a
> $134''$ field, resampled to the $224\times224$ network input)

This matters beyond bookkeeping: the 134″ field is what distinguishes the
catalogue's imaging from the 39.3″ Legacy Survey viewer cutouts that an earlier
round of this work mistook for it, and it is the reason those cutouts reproduced
only 43.9 % of the released labels.

## R-3 — what is still out-of-domain and must not be printed as in-domain

Two items of the row-16 TTA note were measured on the viewer cutouts and are
**not** re-measured here:

* **Q-3, the sky dipole in parity-transfer efficiency** (`a_δ = 0.090 ± 0.010`,
  permutation rank `p ≤ 0.001`, propagating to `0.230 % ± 0.026` = 23 % of the
  strict subset's `A₉₅^obs = 0.98 %`). The *mechanism* — a non-uniform dilution
  on a sample with a non-zero label monopole imprints a spurious dipole — is
  image-independent, and so is the estimator propagation. The *amplitude* is not.
  If P4′ needs a systematic sentence before that re-measurement, print the
  mechanism and the significance and mark the amplitude explicitly as measured on
  a different image sampling, or wait.
* **Q-4, the D4/D8 rotation-TTA recovery fractions** (`F = 0.207 ± 0.010`,
  `0.394 ± 0.009`) and the `\bar\epsilon = 0.754 ± 0.005` PA-restoring transfer
  efficiency of P-5a. Both need the 16-angle grid, not the four right angles run
  here. Since the in-domain rotation instability is *larger* than the
  out-of-domain one, a recovery fraction measured out-of-domain is very likely an
  over-estimate of what TTA would recover in-domain, so quoting it as a
  mitigation claim would be optimistic in the wrong direction. Recommend cutting
  `\bar\epsilon` and the recovery-fraction sentence from the paper until
  re-measured.

**Never affected by any of this**: row-16(ii-b) items **P-1…P-4** (the corrected
`± 0.0238` error bar and `1.8σ`, the withdrawal of `47σ`, `2.9σ`, `0.038` and
`≈ 26 %`, the retirement of the mirror-injection extension, the `N ≈ 7.3×10⁵`
power statement). Those are re-analyses of committed label-level quantities and
of the exact identity `eq_cw(MI) = eq_ccw(I)`, which holds for any image.

---

## Ordering for the P4′ lane

1. Print R-1's table and R-1a / R-1b now. The held `0.7166` / `1.37 %` /
   `21.1 %` / `0.6296` / `1.56 %` numbers are withdrawn everywhere they appear
   (the co-director counted 7+ sites in v4P.0.10, including a table row).
2. Fix §`sec:catalog_schema` per R-2 in the same bundle — it is one parenthesis
   and it is the fact the whole provenance question turned on.
3. Cut, or explicitly caveat, the `\bar\epsilon = 0.754`/`51\sigma` clause and
   the TTA-recovery sentence per R-3.
4. Q-3's systematic caveat: mechanism + significance yes, amplitude marked as
   out-of-domain, or hold it for the re-measurement.
