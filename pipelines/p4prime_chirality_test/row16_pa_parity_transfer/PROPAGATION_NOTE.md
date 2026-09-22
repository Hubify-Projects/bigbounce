# PROPAGATION NOTE — row 16(ii-b) → P4′ (paper owned by lane L4)

**From** lane `bb-LS-ledger16`, 2026-09-19. **Do not edit `main.tex` from this
lane.** This note lists the exact sentences P4′ should carry, each with the
committed artifact it comes from. Every number below is read from
`s4_n20k_slope_reanalysis.json` / `s1_pa_transfer_results.json` in this
directory; nothing is estimated.

Target section: `pipelines/p4prime_chirality_test/paper/main.tex`
§`sec:robustness_disclosure` (currently lines ~1016–1076 in v4P.0.9), plus
Assumption 2 of §`sec:bh` (~line 849) and Table `tab:pixel_calib`.

---

## P-1 — Table `tab:pixel_calib`: the quoted significances use the wrong error bar

**What the paper says now** (v4P.0.9, Table `tab:pixel_calib` and the paragraph
above it): pixel-level injection `dA/df = +0.0167 ± 0.0089`; "naive label
identity `+0.434`, `47σ` from the pixel result"; "mixture-corrected label
identity `−0.0093`, `2.9σ`", described as "an unresolved discrepancy, not a
consistency, between the two label-level identities."

**What is wrong.** The `±0.0089` is the bootstrap error *at a fixed injection
realisation* (`analyze_injection_scale20k.py`, `boot_se_spiral_classified`),
i.e. it propagates galaxy-sampling noise only. The dominant term is the
hypergeometric fluctuation in *which* galaxies are drawn into the injected
subset, which the committed analysis never propagated. Re-running the exact
committed design (5 fractions × 10 seeds) 2,000 times gives the true standard
error of that fitted slope:

| statistic | exact identity | committed slope | correct SE | σ from identity |
|---|---|---|---|---|
| hard, spiral-classified (the paper's `A`) | `−0.011791` | `+0.029671` | `0.023754` | **1.75** |
| soft, mean over all classes | `−0.009337` | `+0.016726` | `0.011454` | **2.28** |

(`s4_n20k_slope_reanalysis.json`; the Monte-Carlo mean recovers the identity,
`−0.012472` vs `−0.011791` and `−0.009606` vs `−0.009337`, which validates the
null.) There is **no discrepancy**: the measured slope is consistent with the
exact label identity at 1.8σ / 2.3σ. The `2.9σ` and the phrase "unresolved
discrepancy … not a consistency" should be withdrawn.

## P-2 — the `+0.434` row compares a statistic to an identity that does not apply to it

`+0.434 = −2A₀` with `A₀ = −0.2172` is the identity for the *soft* statistic
`2·mean(eq_cw) − 1` taken over **all three classes**, in which the NOT_SPIRAL
probability mass sits inside the mean. The committed analysis script says so
itself (`note_on_comparison_scope`, and the derivation of the mixture identity
`A₀_ccw − A₀_full = −0.0093`). Quoting `47σ` against `+0.434` therefore measures
the NOT_SPIRAL mass, not the pipeline. The `+0.434` row and the `47σ` should be
removed from `tab:pixel_calib`, or relabelled explicitly as "identity for a
different normalisation, not applicable".

## P-3 — the response ratio `0.038` and the `≈26%` physical floor do not follow

The paper computes "implied response ratio `0.0167/0.434 ≈ 0.038`", calls it
"roughly an order of magnitude smaller than `g = 0.398`", and propagates it to
"a physical-amplitude floor of order `0.98%/0.038 ≈ 26%`" (it does not adopt
this, but it does state it as a tension). Both the numerator (a slope
consistent with its own identity, P-1) and the denominator (an inapplicable
identity, P-2) fail, so the ratio, the "order of magnitude" comparison, and the
`26%` number have no content and should be withdrawn.

There is a deeper reason this channel can never measure the bridge factor. The
production post-processing is a 2-fold horizontal-flip test-time average, so
`eq_cw(M I) = eq_ccw(I)` *identically*, for every image, independent of the
network's weights (pre-registration §1). The injected operation **is** that
mirror. Its transfer is therefore exactly unity by construction, and the
experiment is a relabelling theorem, not a measurement of the classifier's
morphology transfer. The sentence "the production pipeline suppresses
pixel-level parity leakage well below what the label-level injection model
alone would predict" states the opposite of what the algebra requires and
should be replaced.

## P-4 — what the injection channel *can* say, quantitatively

For the paper's hard statistic the injection curve obeys `E[A(f)] = A₀(1−2f)`
exactly at every `N`. The design first reaches 3σ power only at
**`N ≈ 7.3 × 10⁵`** (`n_required_for_3sigma_power_spiral_classified`, with the
error scaling measured, not assumed: the fitted exponent is `−0.5009` over
`N ∈ {2500, 5000, 10⁴, 2×10⁴}`). So neither `N = 20,000` nor any feasible
extension of it constrains anything — and at `N ≈ 7×10⁵` it would only confirm
the theorem. Recommended replacement sentence: *"the image-level mirror
injection is exactly the symmetry of the production post-processing, so it
transfers with unit efficiency by construction and carries no information about
the observed-to-physical transfer function; we therefore report it as a
consistency check of the post-processing implementation only."*

## P-5 — a real, independent bound on the bridge factor (replaces the withdrawn one)

**Status: measured.** Statistic pre-registered in `PREREGISTRATION_2026-09-19.md`
§5 S5 and addendum A1; geometry argument derived in
`ROW16IIB_PA_PARITY_TRANSFER_2026-09-19.md` §4; numbers in
`s5b_nocrop_dilution.json` and `s1_pa_transfer_results.json`; result in §5–§6 and
§9 of the same document.

**The measurement.** A genuine handedness reversal — the mirror about the
galaxy's *own* major axis, i.e. `R(2·PA)·M·I`, which leaves the galaxy at the
position angle it is observed at — is registered as a reversal by the released
pipeline in only `ε̄ = 0.6363 ± 0.0024` of galaxies (`149σ` below unity), and in
`0.7543 ± 0.0048` on the catalogue's own `primary_hc` cut measured with the
**exact released preprocessing** (no crop, lossless 90/180/270° rotations). The
failure is a rotation-equivariance failure, not a parity failure: the two-element
flip TTA makes the parity operation exact wherever it commutes with the rotation
(`ε = 1.000000` at `φ = 0, 180`, the positive control), and `ε(φ)` tracks the
rotation-only class stability `R(φ)` at every other angle.

**The bound.** Handedness does not depend on the orientation at which a galaxy is
presented, so `L(0) ≠ L(θ)` proves a label error in one of the two, giving
`d(θ) ≡ P(L(0) ≠ L(θ)) ≤ 2e` and hence, for the dilution `D = 1 − 2e` of any true
population asymmetry, `D ≤ 1 − max_θ d(θ)`. Measured on the released
preprocessing, on galaxies labelled spiral at both orientations:

| selection | `D ≤ 1 − max_θ d(θ)` | `D ≤ 1 − d(180)` (assumption-free) | ⇒ `A₉₅^phys = A₉₅^obs / D` |
|---|---|---|---|
| all spirals (N = 19,800) | `0.6296 ± 0.0040` | `0.6928 ± 0.0038` | `≥ 1.56%` / `≥ 1.42%` |
| `primary_hc`, the catalogue's own cut (N = 7,982) | **`0.7166 ± 0.0047`** | `0.7887 ± 0.0047` | **`≥ 1.37%`** / `≥ 1.24%` |

`θ = 180` needs no PA-uniformity argument at all: position angle is defined
mod 180°, so a cutout rotated by 180° depicts the same galaxy at the same
position angle and the two error rates are equal by construction. On that row
alone the pipeline changes its own answer for `21.1%` of high-confidence spirals
handed a lossless 180° rotation of the identical image.

`g = 0.398` sits below the bound (`0.398 ≤ 0.7166`), so the illustrative GZ1
bridge and this measurement are **consistent**; the new statement is that `D` is
bounded away from 1 at `60σ`, with no human truth labels anywhere in the
derivation.

---

### P-5a — replacement sentences for Assumption 2 of §`sec:bh` (~line 853–859)

Delete: *"Sec.~\ref{sec:robustness_disclosure} reports a first direct empirical
probe of that transfer function whose implied response is roughly an order of
magnitude smaller than $g=0.398$; taken at face value this would weaken, not
strengthen, the present exclusion, and is not resolved here."*

Insert:

> Sec.~\ref{sec:robustness_disclosure} reports a direct measurement of that
> transfer function. Presenting the released pipeline with a genuine handedness
> reversal --- the mirror about each galaxy's own major axis, which preserves
> its observed position angle --- and marginalising over position angle, the
> reversal is registered in $\bar\epsilon = 0.754 \pm 0.005$ of
> high-confidence spirals, $51\sigma$ below unity. Because handedness does not
> depend on the orientation at which a galaxy is presented, the rate at which
> the pipeline contradicts itself between two orientations of the same image
> bounds the dilution $D$ of any true population asymmetry from above,
> $D \le 1 - \max_\theta P\big(L(0) \ne L(\theta)\big) = 0.717 \pm 0.005$, with
> no human truth labels entering the argument. The observed-label floor
> $A_{95}^{\rm obs} = 0.98\%$ therefore corresponds to a physical-parity floor
> $A_{95}^{\rm phys} = A_{95}^{\rm obs}/D \ge 1.37\%$. This is consistent with
> the illustrative $g = 0.398$ used above (which would give $2.46\%$) and
> supersedes it as the quantity we can defend: it is an upper bound on $D$, so
> it can only weaken the exclusion, and we adopt it in that direction only.

### P-5b — replacement paragraph for §`sec:robustness_disclosure` (~lines 1026–1060)

Delete the paragraph containing *"an unresolved discrepancy, not a consistency,
between the two label-level identities"* and the sentence *"the production
pipeline suppresses pixel-level parity leakage well below what the label-level
injection model alone would predict"*, together with Table~\ref{tab:pixel_calib}'s
`+0.434` / `47\sigma` row and the `0.038` response ratio and `\approx 26\%`
figure (P-1, P-2, P-3 above). Insert:

> The pixel-level mirror injection is exactly the symmetry of the production
> post-processing: the two-fold horizontal-flip test-time average satisfies
> $\mathrm{eq}_{\rm cw}(MI) = \mathrm{eq}_{\rm ccw}(I)$ identically for every
> image, independent of the network's weights. The injected operation \emph{is}
> $M$, so it transfers with unit efficiency by construction and the recovered
> curve obeys $E[A(f)] = A_0(1-2f)$ at every $N$; we report it as a consistency
> check of the post-processing implementation, not as a measurement of the
> morphology transfer function. Propagating the injection-realisation variance
> that the original analysis omitted, the fitted slope
> $dA/df = +0.0297 \pm 0.0238$ is consistent with that identity at $1.8\sigma$,
> and the design would first reach $3\sigma$ power at $N \approx 7.3\times10^5$.
>
> The transfer function is instead measured directly, by presenting the pipeline
> with a genuine handedness reversal at the galaxy's observed position angle
> (Assumption~2). Marginalised over position angle, a real reversal is
> registered in $\bar\epsilon = 0.754 \pm 0.005$ of high-confidence spirals; the
> deficit is a rotation-equivariance failure rather than a parity failure, since
> the flip test-time average renders the parity operation exact wherever it
> commutes with the rotation ($\bar\epsilon = 1$ at $0^\circ$ and $180^\circ$,
> the positive control) and $\epsilon(\varphi)$ tracks the rotation-only class
> stability elsewhere. The implied dilution bound
> $D \le 0.717 \pm 0.005$ raises the physical-parity sensitivity floor to
> $A_{95}^{\rm phys} \ge 1.37\%$, which is the figure we quote. Transfer
> efficiency is not uniform on the sky --- it differs by
> $0.036 \pm 0.005$ between the hemispheres of the strict-subset dipole axis ---
> and we flag that position-dependent dilution as an open systematic rather than
> correcting for it here.

### P-5c — Table `tab:pixel_calib` replacement rows

| row | keep / change |
|---|---|
| `dA/df` pixel-level | keep the central value `+0.0297` (hard, spiral-classified), **replace** `± 0.0089` with `± 0.0238` and the `2.9σ` with `1.8σ` |
| naive label identity `+0.434`, `47σ` | **delete** (identity for a different normalisation; P-2) |
| mixture-corrected identity `−0.0093` | keep, now quoted as consistent at `2.3σ` on the soft statistic |
| implied response ratio `0.038` | **delete** (P-3) |
| — new row — | `ε̄` (PA-restoring reversal, `primary_hc`, released preprocessing) `= 0.754 ± 0.005` |
| — new row — | `D ≤ 1 − max_θ d(θ) = 0.717 ± 0.005` ⇒ `A₉₅^phys ≥ 1.37%` |

### P-5d — citations for every number above

| number | artifact | key |
|---|---|---|
| `ε̄ = 0.6363 ± 0.0024` (cropped grid, 6 informative angles) | `s1_pa_transfer_results.json` | `S1_eps_bar_informative`, `S1_eps_bar_informative_boot_se` |
| `ε̄ = 0.7543 ± 0.0048` (`primary_hc`, released preprocessing) | `posthoc_nocrop_eps.json` | `primary_hc_subset.eps_bar_corotated_informative` |
| `ε = 1` positive control | `s1_pa_transfer_results.json` | `S2_positive_control_exact_swap_fraction` (`max_identity_residual = 0.0`) |
| `D ≤ 0.7166 ± 0.0047`, `d(180) = 0.2113` | `s5b_nocrop_dilution.json` | `primary_hc_subset.D_upper_bound`, `.per_theta.180` |
| `dA/df = +0.0297 ± 0.0238`, `1.75σ`, `N ≈ 7.26×10⁵` | `s4_n20k_slope_reanalysis.json` | `committed_slope_spiral_classified`, `mc_se_slope_spiral_classified`, `z_committed_vs_identity_spiral_classified`, `n_required_for_3sigma_power_spiral_classified` |
| hemisphere `Δ = 0.0356 ± 0.0050` | `s1_pa_transfer_results.json` | `S6_hemisphere_split.strict_887k_axis` |
| `g = 0.397616` | P4 catalog paper `chirality_catalog_paper.tex:1533`, Table `tab:gz1_confusion` | — |

Suggested artifact link for the paper:
`\artifact{pipelines/p4prime_chirality_test/row16_pa_parity_transfer}` (directory:
`/tree/`, not `/blob/`), and the reproducibility manifest
`reproducibility/manifests/experiments/row16iib-pa-parity-transfer.json`.

**Directive-G reminder for lane L4:** adopting any of these sentences changes a
quantitative claim, so the same bundle must bump `\paperVersion` + `\date`,
recompile with 0 undefined references, re-run `/latex-audit`, re-mirror the PDF
byte-identically to every served path, and — once Convex is reachable again —
`paperVersions:bump` with the real md5/pages. Figure `tab:pixel_calib` is a
table, not an image, so directive I6 does not bite there. The image check was
still run in this lane: P4′ v4P.0.9 has exactly three `\includegraphics`
(`fig_sky_map.png` line 431, `fig_injection_recovery.png` line 534,
`fig_p5_cw_by_env_bar.png` line 675); all three were rendered and inspected, and
none of them draws `0.0089`, `47σ`, `0.038`, `26%` or `g=0.398`.
`fig_injection_recovery.png` does render `A_95^obs = 0.98%` and
`A_dip = 0.467%` — both **observed-label** quantities, which this result does not
change (it changes only the conversion to physical parity), so that figure needs
no regeneration.
