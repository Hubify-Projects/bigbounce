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

*(filled in below once the row 16(ii-b) rotation measurement completes; the
statistic, threshold and geometry argument are pre-registered in
`PREREGISTRATION_2026-09-19.md` §5 S5 and derived in
`ROW16IIB_PA_PARITY_TRANSFER_2026-09-19.md` §4.)*
