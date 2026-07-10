I have completed a thorough verification against the committed artifacts. Here is my referee report.

---

## Referee Report — P4: *A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning*

**(1) VERDICT: MAJOR REVISIONS**

The analysis is careful, the central null is genuinely supported, and — importantly — every headline number I spot-checked reproduces exactly against the committed artifacts (see below). The paper is held back from acceptance by one headline-level quantitative/internal-consistency problem (the Shamir amplitude mapping) plus several traceability wrinkles. None require re-analysis; all are fixable editorially, but the first is significant enough that it must be resolved before publication.

**What I verified as correct (for the record):**
- **Transfer-chain g_eff = g.** The derivation `g_eff = s_CW + s_CCW − 1` (derivative of `q·s_CW + (1−q)(1−s_CCW)`) is correct, and its coincidence with `g = 2a−1` is real: from `tab:gz1_confusion`, s_CW = 39011/57900 = 0.674, s_CCW = 42928/59305 = 0.724, pooled a = 81939/117205 = 0.6991, so g_eff = 0.398 = 2a−1 = 0.3982. Verified. (One wording nit under MINORs.)
- **GZ1 independence numbers.** `gz1only_fullN_dipole_result.json`: z = −0.539 (p=0.666), per-galaxy z = −0.551 (p=0.675), N = 46,017, CW frac = 0.4836, dipole amp = 0.0546, and the 667944/190225/48414/46017 selection chain — all match the paper (Sec. Data, Sec. pseudolabel_independence) exactly.
- **Monopole 99.32% figure.** `monopole_mask_null_results.json`: pre_master_reproduction = 99.322%, residual +1.69σ, hemisphere +4.42σ, p_CW = 0.49736, and every Table `tab:monopole_mask_null` entry (1.6961e-2 / 1.6846±0.0068e-2, 3.484e-3 / 1.693±0.405e-3). Verified.
- **Injection floors.** `c16_r24conf_pod_batch.json`: HC-broad area-uniform P(σ>3) = 0.59 @0.75%, 0.91 @1.0%, 1.00 @1.5% → A_50≈0.75%, A_95∈(1.0%,1.5%]; and the full-sample A_50≈0.36%/A_95≈0.63% (loglinear 0.3577%). Verified.
- **WLS fit.** Appendix D Table: A_best = 4.55e-3 (A_p units), σ_boot = 1.63e-3, z = −18.1 vs A_ref = 0.034; mask-equivalence audit (24,087 px, f_sky 0.49005) verified.

**(2) ISSUES**

**[MAJOR] Abstract §Abstract (line 616) + Intro (639) / Parity (1155) / Conclusions (1193) — the Shamir amplitude mapping is internally self-contradictory and doubles the headline tension.** The abstract writes "…the 1.7% reference amplitude … *this f_CW asymmetry* maps to A_p=0.034 under A_p=2(f_CW−½)." An *asymmetry* `(N_CW−N_CCW)/(N_CW+N_CCW)` already **equals** A_p; only an f_CW *deviation* (f_CW−½) gets doubled to A_p. The text simultaneously calls 1.7% an "asymmetry" and treats it as a deviation. This is not cosmetic: the headline "∼7–18× tension" (0.455% vs Shamir 3.4–8.0% A_p) and the primary "z≈−18" exclusion (A_ref=0.034, Table `tab:wls_fit` line 1387) both rest on this doubling. Under the standard reading (Shamir's 1.7–4.0% *are* A_p asymmetries), the tension is ∼4–9× and the exclusion is z≈−7.6 — which is exactly this paper's own earlier value (changelog v1.0.206, line 186) and the external referee number the changelog (lines 244–247) dismisses as a "referee miscompute." The manuscript cannot adjudicate this against itself. **Fix required:** quote Shamir (2020/2022) verbatim on his amplitude definition, standardize the word "asymmetry" vs "deviation," and — if Shamir reports a full asymmetry — correct the tension to ∼4–9× and the exclusion to z≈−7.6. I could not web-verify Shamir's convention in-session; as written the claim is unverifiable and internally inconsistent by a factor of 2.

**[MINOR] Sec. `monopole_mask_null` (line 1017) — the observed ℓ=1 residual |a₁| = 6.95e-3 is the smallest of three co-committed values on essentially the same mask, and the 54% vs 52.4→53.0% / 47%-remainder figures are drawn from *different* masks.** `systematic_l1_forward_model_canonicalmask.json` (24,087 px, correct f_sky 0.49005) gives observed 6.951e-3 → 53.9% modelled; but `systematic_l1_forward_model.json` and `_dr8morph.json` (24,187 px) give observed **7.229e-3** → 52.4%→53.0%, un_modelled_remainder = 0.4698 (the paper's "~47%"). The paper's a-fortiori safety bound (A_p=0.695% < A_50=0.75%) uses the smallest value; under 7.23e-3 the margin shrinks from 0.055 to 0.027 pp. The bound still holds (and A_95∈(1.0,1.5] leaves ample room), and the direct +0.41σ null is the real load-bearing result — so no conclusion changes — but the paper should quote *one* canonical-mask value, disclose the 6.95/7.04/7.23e-3 spread, and use the largest for a conservative a-fortiori statement.

**[MINOR] Artifact metadata bug feeding a cited result.** `systematic_l1_forward_model.json`/`_dr8morph.json` record `f_sky_canonical: 0.7409`, but their own `n_in_mask_pixels: 24187` → 24187/49152 = 0.492, not 0.741. The morphology-improvement result (52.4→53.0%, "~47% remainder") that the paper cites comes from these files. The label is a recording error, not a paper error, but since the manuscript relies on these artifacts it should be reconciled/annotated so a reader can confirm the mask.

**[MINOR] Sec. Abstract vs Intro Shamir range.** The abstract's "1.7%–4.0%" lower bound (line 616) is not the same as Intro line 637's "Shamir (2020) … ∼2–4% level." State where the 1.7% lower bound originates.

**[MINOR] Two "our WLS amplitude in A_p units" coexist.** 0.455% (joint nuisance-marginalized, Appendix D, used for the 7–18× claim, lines 1155/1193) and 0.32% (equal-area-partition maximum, Sec. Comparison line 1051). Both appear in Shamir comparisons; clarify which is the headline amplitude and why both are quoted.

**[MINOR] Sec. sensitivity, line 1112 — "the pooled accuracy satisfies a=(s_CW+s_CCW)/2 *exactly*."** This identity is exact only at f_CW=½; at the actual sample it holds to three decimals (0.699 vs 0.699) because the GZ1 CW/CCW-true counts (57,900 vs 59,305) are near-balanced. The numerical claim ("changes g by <10⁻³") is fine; replace "exactly" with "to the quoted precision."

**(3)** The central claim — that the large-scale morphological chirality dipole is consistent with null — **is supported**: the primary real-space HC estimator (+0.41σ, p=0.31) and the model-independent GZ1-human-only cross-check (z=−0.54) both reproduce exactly from committed artifacts, and the null is robust across the confidence-cut sweep; only the *quantitative framing of the Shamir tension/exclusion* (a factor of 2) and minor mask-variant bookkeeping require correction before publication.

---

**Best Next Steps**
1. Resolve the [MAJOR]: pull Shamir (2020/2022) and pin his amplitude definition; if it is a full asymmetry, restate tension as ∼4–9× and exclusion as z≈−7.6, and fix the abstract's "asymmetry"/"deviation" labeling everywhere.
2. Standardize the observed ℓ=1 residual to one canonical-mask value (prefer the conservative 7.04–7.23e-3), disclose the spread, and re-derive the a-fortiori bound from it.
3. Fix the `f_sky_canonical: 0.7409` metadata in the two forward-model artifacts and reconcile the 24,087 vs 24,187-pixel mask variants.
4. Clean up the 0.455% vs 0.32% and 1.7% vs 2–4% presentational inconsistencies.

Say `continue` and I will take the next best scoped step (drafting the Shamir-convention fix + a units-audit patch).
