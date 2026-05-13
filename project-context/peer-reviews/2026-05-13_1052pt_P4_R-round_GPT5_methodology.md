# P4 v1.0.47 — GPT-5 Adversarial Review (Methodology)

**Reviewer persona:** OpenAI GPT-5, statistical-methodology lens (Gelman/Vehtari profile)
**Paper:** chirality_catalog_paper.tex v1.0.47 / 2,732 lines / 38 bibitems
**Date:** 2026-05-13

> Note on scope. The prior 5-agent multi-vendor round (v1.0.46 → v1.0.47) closed
> 3/3 BLOCKERs and 14/15 MAJORs, including the σ canonical-N fix (M1), the
> 1/√(2(N−1)) MC SE formula (M2), and the Table III bandpower ℓ_eff bin-edge
> relabel (B3). I therefore avoid re-litigating those — every finding below is
> a NEW issue that the 5-agent round did not surface, located by re-deriving
> the paper's arithmetic from the displayed values and stress-testing the
> language around MASTER, Fisher-vs-empirical sensitivity, the χ²/dof figures
> sitting next to the "consistent with null" headline, and the framing of the
> 0.5% number that is now in the paper's title.

## Summary counts
- BLOCKERs: 2
- MAJORs: 6
- MINORs: 5
- NITs: 4

## BLOCKERs

### B1: "0.5% upper limit" in the title is not an upper limit — it is a 50%-detection-threshold sensitivity floor (lines 49, 90–93, 2415–2419, 2422–2426)
**Quote (title, line 48–50):** "A Survey-Scale Chirality Catalog of 8.47 Million Galaxies (3.2 Million Spirals): A $0.5\%$ Upper Limit on Large-Scale Parity Violation in Galaxy Morphology"

**Quote (abstract, line 89–94):** "The empirical injection-recovery $50\%$-detection threshold (systematic-inclusive) sits at $|A_{\rm dipole}|\approx 0.5\%$; we adopt this as the conservative survey-scale upper limit, with the Fisher-floor value $0.2\%$ retained as a statistical-only asymptote".

**Quote (Sensitivity, line 2018–2022):** "The smallest amplitude satisfying both $\langle\sigma\rangle{>}2$ and $P(\sigma{>}2){>}0.5$ in this strict per-pixel-shuffle null is $\notin \{0.05\%, ..., 0.50\%\}$; an empirical $50\%$-recovery threshold therefore lies above $0.5\%$".

**Issue:** What the Wave 14-NN injection-recovery study actually delivers is a *minimum detectable amplitude* under a 50%-power criterion (median σ > 2 *and* P(σ>2) > 0.5). That is the *sensitivity floor* of the experiment — the smallest *true* amplitude at which the dipole would be detected half the time at the 2σ bar. By construction it tells you nothing about the upper limit on the *measured* signal. A frequentist upper limit on |A_dip| at 95% (or 99.7%, for 3σ) is constructed from the measured A_dip and its uncertainty (here, A_dip ≈ 0 with σ(A_dip) ≈ 0.048% per the Fisher derivation in Eq. 13, or some larger empirical σ that accounts for systematics). With a null measurement at σ=0.43, a frequentist 3σ upper limit would be on the order of *0.14–0.5% depending on what σ you trust*, but the number must come from the *measurement uncertainty on A_dip*, not from the experiment's *50%-detection power threshold*. These are different quantities. The title and abstract conflate them and present what is, in fact, the experiment's *sensitivity* as the result's *upper limit*. A Gelman/Vehtari-style methodology referee will not accept this — the title is asserting a 0.5% bound on parity violation when the actual statistic is "this experiment could spot 0.5% half the time."

**The empirical injection sweep was {0.05, 0.10, 0.20, 0.30, 0.50}% (line 1994), all of which produced P(σ>2) ≤ 0.18.** That means the experiment cannot reliably detect a 0.5% signal — at A=0.5% the recovery probability is 18%, not 50%. The "50%-recovery threshold lies above 0.5%" sentence (line 2021) admits this. So even the sensitivity claim "we can detect 0.5%" is itself an *extrapolation outside the simulated grid*. A reviewer will demand the sweep be extended to A=1.0% and A=2.0% to actually bracket the 50%-power point, OR the language be retracted to "the empirical 50%-recovery threshold is > 0.5% (not bracketed within the simulated grid)."

**Fix:** Two options, both required.
1. Retitle to remove "0.5% Upper Limit." The defensible empirical headlines are: (a) "no dipole detected: σ_dipole = 0.43, p = 0.30"; (b) "post-MASTER ℓ=1 = −0.12σ, consistent with null"; (c) "minimum dipole detectable at 50% power is > 0.5% under per-pixel-shuffle null." A retitle like "A Null Detection of Large-Scale Parity Violation in 3.2 Million Spiral Galaxies (σ_dipole = 0.43)" is honest and stronger than the current claim.
2. Construct a proper frequentist UL on |A_dipole|. Given the post-MASTER null (z = −0.12) and the empirical injection-recovery σ(A_dip)_emp at A=0.5% (≈ 0.25–0.30%, inferable from the σ-recovery values 0.08–0.68 in the table), the 3σ UL on |A_dip| is approximately 3 × σ(A_dip)_emp = ~0.75–0.90%. That is the correct number to put against the title.

### B2: Total post-MASTER χ²/dof = 4.22 over 38 bandpowers contradicts the "fully consistent with null" headline (line 1222, fn:mc_count vicinity)
**Quote (line 1222, body of the lengthy footnote):** "The corrected total $\chi^2$/dof is $243.8/38$ (pseudo) and $160.5/38 = 4.22$ (decoupled); the empirical p-value of the lowest-$\ell$ bin against 1000 label-shuffle nulls is $0.0$ (all 1000 nulls fall below the data). After full MASTER mode-coupling deconvolution the canonical significance is $-0.12\sigmaunit$, fully consistent with null."

**Issue:** A χ²/dof = 4.22 over 38 bandpowers is *not* consistent with null. Under the null hypothesis (data = noise), the expected χ²/dof is 1 ± √(2/dof) ≈ 1 ± 0.23. A value of 4.22 corresponds to χ²=160.5 with 38 dof, which has a p-value of ~10⁻¹⁶ (effective z ≈ 8.2σ for the joint multi-bandpower null). And — this is the critical point — that is the *post-MASTER-decoupled* χ². The MASTER deconvolution corrects the *mean* but the *covariance* of the deconvolved bandpowers should also be propagated; if 500-MC null realizations of the full inversion give a sample covariance matrix whose diagonal is σ_null² and the bandpowers are approximately independent, then the joint χ²(38) ≈ 160 means at least *some* bandpower combination is rejecting the null at high significance. The paper then quotes only the ℓ=1 number (−0.12σ) and declares the *whole spectrum* consistent with null. That is selective reporting.

Either: (i) the 38-bin χ² is computed against the wrong covariance (e.g., using the analytic Poisson floor 1.93e−6 rather than the empirical 500-MC null σ matrix), in which case the χ²/dof number is meaningless and should be removed; or (ii) the post-MASTER spectrum genuinely rejects null in *some* bandpower direction outside ℓ=1, and the paper has buried that under headline-by-cherry-pick.

A Gelman/Vehtari reviewer will pin you to the wall on this footnote. It survives v1.0.47 only because the prior 5-agent round was focused on title/sensitivity/MC-formula text and didn't audit the χ²/dof line.

**Fix:** Either (a) recompute the 38-bin χ² using the *empirical* 500-MC null covariance (with off-diagonal mode-coupling residuals), report the corrected p-value, and if it is still p < 0.01 in any bandpower direction add an explicit "the lowest few bandpowers reject null at z > 3 against the simpler diagonal null; with the full empirical covariance the joint test is consistent with null" sentence; OR (b) drop the χ²/dof = 243.8/38 and 160.5/38 = 4.22 numbers from the footnote because they are computed against the wrong covariance and are not what supports the "consistent with null" headline. The honest headline is the *single-bandpower* ℓ=1 = −0.12σ from the rank-based MC test; the multi-bandpower χ² is then either properly framed or removed.

## MAJORs

### M1: Higher-multipole bandpower z-scores in Table III (1.47, 1.63, 0.91, 1.22) are individually null but jointly suggestive — no joint test reported (Table III lines 1142–1153)
**Quote (Table III, lines 1146–1150):**
```
$4$ ($\ell\!\in\![2,6]$)    & 1.494 & $-0.122$ & Null (MASTER-deconvolved)
$9$ ($\ell\!\in\![7,11]$)   & 1.546 & $1.47$   & Null
$14$ ($\ell\!\in\![12,16]$) & 1.81  & $1.63$   & Null
$19$ ($\ell\!\in\![17,21]$) & 0.88  & $0.91$   & Null
$24$ ($\ell\!\in\![22,26]$) & 1.12  & $1.22$   & Null
```

**Issue:** Four of the five tabulated z-scores are positive and three are above 1σ. Under the null with 5 independent draws, P(all 4 of [z9,z14,z19,z24] > 0) = 1/16 = 0.0625; expected number > 1σ is 0.8 but observed is 3. The χ² of the four ℓ>1 bandpowers against null is 1.47²+1.63²+0.91²+1.22² = 7.49 on 4 dof (p ≈ 0.11). Borderline, but a joint test is the right test, and the paper does not report one. The "Null" label in column 4 is a per-bin statement, not a joint statement, and the multi-bandpower direction is exactly where a real coherent (non-dipole) parity signal would live (e.g., a chiral large-scale structure correlator would give a quadrupole or higher-pole excess). The reviewer will ask for the joint p-value over all 5 (or all 38) post-MASTER bandpowers using the proper empirical null covariance.

**Fix:** Add a row "Joint (all 5)" with χ² = 7.49 + (−0.12)² ≈ 7.50 on 5 dof (p ≈ 0.19) — or, with the proper empirical covariance, whatever the correct number is. Adjacent text should say explicitly "joint multi-bandpower test does not reject null." If the proper joint test does reject (which the dof=38 footnote suggests), say so.

### M2: σ_null = 4.290e-7 in the abstract is not arithmetically reconciled with the displayed Table III C_ℓ × 10⁶ column (lines 84–87, 1146)
**Quote (abstract, line 84–87):** "$C_1 = (1.494 \pm 0.429)\!\times\!10^{-6}$\,sr against $\langle C_1^{\rm null}\rangle = 1.546\!\times\!10^{-6}$\,sr from $500$ mode-coupling-inverted MC realizations"

**Quote (Table III, line 1146):** "$4$ ($\ell\!\in\![2,6]$) & 1.494 & $-0.122$"

**Issue:** Abstract carries the uncertainty as ±0.429e−6 (= 4.29e−7), but Table III does not display the uncertainty for any bandpower — only the central C_ℓ and the resulting z. The reader cannot reconstruct z for any of the four ℓ>1 rows because σ_null is not displayed. With the abstract value σ_null = 4.29e−7 = 0.429 in the table's units, the table's z-scores back-derive to σ_null values that don't all match 0.429:
- ℓ_eff=4: (1.494−1.546)/σ = −0.122 → σ = 0.426 (consistent with 0.429 at 3-sig-fig precision)
- ℓ_eff=9: ?/σ = 1.47 → if C_meas=1.546, C_null=? — table caption says "raw pseudo-$C_\ell$ relative to 1000-MC null" for ℓ≥2 (different MC count, different estimator stage). So the ℓ=4 row is post-MASTER 500-MC, but ℓ_eff=9,14,19,24 are *pre*-MASTER 1000-MC pseudo-C_ℓ. **The table mixes two different estimators across rows** and the caption (line 1133–1140) discloses this only obliquely.

A reviewer arriving at the table cold will not know that row 1 is post-MASTER and rows 2–5 are pre-MASTER. The "Interpretation" column says "Null (MASTER-deconvolved)" for row 1 and "Null" for rows 2–5, which is the only hint, but the column header "Significance (σ)" uses the same units and the row distinction is buried in caption prose. This is a significant readability/reproducibility issue: the table is the load-bearing reference for the post-MASTER null and it is internally inhomogeneous.

**Fix:** Add a σ_null column (or equivalent error bar on C_ℓ) for every row. Split the table into a clearly-labeled "post-MASTER (ℓ=1)" upper block and a "pre-MASTER raw pseudo-C_ℓ (ℓ≥2)" lower block, with a horizontal rule or a column for the estimator stage. Or — preferred — recompute all five bandpowers in the post-MASTER inversion and report a homogeneous table; the 500-MC vs 1000-MC count difference is a footnote, not a row-by-row inconsistency.

### M3: "1-dof chi-squared" framing for ℓ=1 ignores the 2ℓ+1=3 m-modes (line 1248)
**Quote (line 1247–1255):** "Because the post-MASTER null at $\ell=1$ is a 1-dof chi-squared rather than a Gaussian, the canonical primary statistic is the rank-based empirical p-value against the 500-MC null distribution"

**Issue:** C_ℓ at ℓ=1 averages power over 3 m-modes (m = −1, 0, +1). Under the null, each m-mode is an independent Gaussian, so |a_{1m}|² is χ²(2) (since complex), and the sum (= C_1 estimator times 2ℓ+1) is χ²(2·3 dof = 6 dof) for a complex-valued harmonic decomposition. Calling C_1 a "1-dof chi-squared" treats it as a single scalar bin with one variance, which is what `anafast` returns, but the underlying distribution is *not* χ²(1) — it is χ²(2·(2ℓ+1)) for a real scalar map ∝ χ²(6) at ℓ=1. The "1-dof chi-squared" claim affects the tail-probability statement at line 1254 ("the complementary one-tailed χ² tail probability for |z|=0.12 is ≈ 0.91") — for a *correct* χ²(6)/6 distribution the tail at the measured value would give a slightly different number.

**Fix:** Either (a) replace "1-dof chi-squared" with the correct dof (5 for a real-valued ℓ=1 power spectrum estimator, or 2(2ℓ+1)=6 for complex), recompute the χ² tail probability, and update the 0.91 number; or (b) drop the "χ² tail probability" sentence entirely and lean exclusively on the rank-based MC p-value (which is the canonical primary anyway and doesn't depend on the dof choice).

### M4: McNemar Z = 6.77 is reported as a numerical headline despite being explicitly labeled "assumed-discordance result" and not measurement-grade (lines 822–858)
**Quote (line 839–842):** "the exact per-galaxy joint label tabulation would pin these numbers at the data-availability level but is pod-side-only at the present compute allocation; we therefore report the $Z = 6.77$ figure below as the assumed-discordance result rather than a measurement-grade headline."

**Issue:** The Z = 6.77 is computed assuming b+c = 7,812 (line 837), but the paragraph itself acknowledges the *actual* discordance b+c is bounded in [598, 23009] with Z ∈ [3.94, ∞]. Quoting Z = 6.77 as "the McNemar Z value for the Cat-C vs GZ1 monopole comparison" without the bracketing range visible in the immediate sentence will be picked up by readers (and bibliometric tools, and the Hubify auto-summarizer) as the *measured* value. The current text *eventually* discloses the modeling assumption, but the Z = 6.77 number is bolded by repetition and the bracketing range is buried.

This is also a compute-deferral pattern that the SSOT flags as M10 deferred. A Gelman/Vehtari referee won't accept "compute-bound" as an excuse for not running the joint-table tabulation when the data are on disk and the operation is a single pandas groupby on ~46k rows.

**Fix:** Either (a) run the joint-table tabulation NOW (it is, again, a pandas operation on 46,017 rows — seconds on a laptop, not pod-bound) and report the exact Z; or (b) move all Z values into a "modeling-assumption range" sentence: "under the modeling assumption b+c=7,812, McNemar Z = 6.77; the range under uncorrelated-to-degenerate Cat-C/GZ1 discordance is Z ∈ [3.94, ∞]"; or (c) drop the Z=6.77 specific number and report only "the joint McNemar test gives Z > 3.94 even in the most-conservative uncorrelated case, but the load-bearing parity test is the dipole, not the monopole."

The "pod-side only" excuse for not computing a 46k-row contingency is not credible. The reviewer will say so.

### M5: 171 spirals/pixel figure (line 1126) does not match the canonical spiral count and NSIDE=64 geometry
**Quote (line 1126):** "Additional power above $\ell = 5$ is dominated by Poisson shot noise at the per-pixel galaxy density of $\sim\!171$~spirals/pixel"

**Issue:** N_spiral / N_pix (NSIDE=64) = 3,201,160 / 49,152 = 65.1 spirals/pixel globally, or 3,201,160 / (49,152 × 0.491) = 132.6 per *active* pixel. Neither rounds to 171. The 171 figure traces to the older buggy N_total = 8,474,531 / 49,152 = 172.4 — i.e., the *full catalog* density before the N_spiral correction landed in Wave 11-C. The "spirals/pixel" number is therefore a stale pre-Wave-11-C survival in the production-running text. The other downstream uses of N_spiral were updated (the σ in §V, the shot-noise floor 1.93e−6, the χ²/dof, the per-pixel σ_pix in §X.B); this one wasn't.

**Fix:** Replace "$\sim\!171$~spirals/pixel" with the corrected value. The right value depends on which pixel sample is meant — "$\sim\!65$~spirals/pixel averaged over the full HEALPix sphere" or "$\sim\!133$~spirals/pixel in the unmasked DESI Legacy footprint." The latter is the physically meaningful number and is consistent with the §V and §X.B treatments.

### M6: 69.91% GZ1 cross-validation accuracy is reported with no baseline comparison and no calibration disclosure (lines 314–322)
**Quote (line 313–322):** "the spiral-only CW versus CCW accuracy on the 117{,}205 GZ1 spirals where the model also predicts a chirality is $\mathbf{69.91\%}$. Both numbers are well below the headline $93.7\%$ measured against the CE-ResNet-augmented training validation set."

**Issue:** 69.91% on a binary CW/CCW task has a chance baseline of 50%, so the model is 19.91pp above chance on the GZ1 independent sample. That is a *substantially* weaker discrimination than the 93.7% headline (43.7pp above chance, i.e., 22% above chance vs 43% above chance), but the paper does not give the reader a baseline-adjusted comparison and does not anchor 69.91% against the GZ1 *inter-human-rater* agreement (which for Galaxy Zoo binary spiral-handedness is reportedly in the 75–85% range — Land et al. 2008, Lintott et al. 2008). Without this anchor, "69.91% is the conservative spiral-chirality accuracy floor" (line 322) is unverifiable: is it floor relative to chance (50%)? Floor relative to GZ1 self-consistency? Floor relative to the CE-ResNet pseudo-labels?

This matters because the 69.91% number is the *only* number in the paper that anchors the classifier's performance against an independent reference. Every other accuracy figure (93.7%, 93.2%, 94.9%) is against the training pool that is 67.6% CE-ResNet-pseudo-labeled.

**Fix:** Add a footnote or one sentence in §II.B that gives (a) the chance baseline (50%), (b) the GZ1 internal-rater agreement on the same matched 117,205-spiral subsample (computable from GZ1's published vote-fraction histograms — e.g., if 85% of GZ1 spirals have ≥0.8 majority CW or ≥0.8 majority CCW votes, that's the human-rater agreement upper bound on 69.91%), and (c) the Cohen's κ statistic for the classifier-vs-GZ1 agreement, which corrects for chance. The current paper says "we treat 69.91% as the conservative spiral-chirality accuracy floor" without disclosing what the ceiling is — meaningless without the human inter-rater number.

## MINORs

### m1: σ_null reported as 4.290e−7 (line 1230) and 0.429e−6 (line 84) — verify last digit precision
**Quote:** "(σ_{\rm null} = 4.290 \times 10^{-7})" (line 1230); "$C_1 = (1.494 \pm 0.429)\!\times\!10^{-6}$" (line 84). Internally consistent (4.290 ↔ 0.429 at 3 sig figs), but the abstract drops the last "0" of 0.4290. Adopt a single 3-sig-fig convention throughout (recommended: 0.429 in the abstract, σ_null = 4.29e−7 in the body, drop the trailing 0 in 4.290).

### m2: σ_global = 0.028% (line 1825) is computed with p ≈ 0.5 approximation but is reported in §X.B without acknowledging that it agrees with σ ≈ 0.000279 of §V only because p ≈ 0.5
**Issue:** σ_global = 1/(2√N) = 0.02795% is exactly σ for the p=0.5 limit. The paper's actual measured p is 0.4974, which gives σ = √(0.4974·0.5026/N) = 0.02795% — agreement is exact at 4 sig figs only because p − 0.5 = 0.0026 is small. The body of §X.B (line 1827–1829) says "the exact formula σ = √(p(1−p)/N) used in Sec V gives an identical result to four significant figures at p = 0.4974" but does not warn the reader that if the equivariant catalog ever drifted to p = 0.48 or p = 0.52 (still well within the "monopole" regime), the two formulae would diverge. Cosmetic but worth a one-clause clarification.

### m3: 0.205% → 0.2% rounding in Eq. 13 derivation absorbs a 47% margin (line 1885–1892) — quantify the budget breakdown explicitly
**Issue:** The text says the 0.205% → 0.2% rounding "captures a 40% margin." Actually 0.205 / 0.146 = 1.40 → 40% margin, and 0.2 / 0.146 = 1.37 → 37% margin. Minor inconsistency in the 40% vs 37% claim and the "captures a ~40% margin" phrasing. Either compute the actual margin to 2 sig figs ("captures a 37% margin") or restate as "rounds 0.205% to 0.2% as a conservative two-sig-fig statement."

### m4: Wave 14-NN sweep grid {0.05, 0.10, 0.20, 0.30, 0.50}% does not bracket the 50%-power point (line 1994, 2018–2022)
**Issue:** Per the recovery table (line 2008–2017), at A=0.50% the recovery probability P(σ>2) is 0.18, not 0.50. The conclusion that "the 50%-recovery threshold lies above 0.5%" is an *extrapolation* outside the grid. A proper sensitivity floor requires the grid to include the 50%-power point. The paper should either (a) add two more amplitudes (e.g., A=1.0% and A=2.0%) to bracket P(σ>2)=0.5, OR (b) restate the result as "the 50%-recovery threshold is > 0.5% but is not bracketed within the simulated grid; the empirical detection floor is therefore lower-bounded at 0.5% but its actual value requires an extended sweep." The latter is honest; the former is the right experiment.

### m5: Sky-balance table footnote (line 1441) admits the canonical row "inherits" 0.4974 from the snapshot — verification artifact is forward-referenced but not promised to exist before submission
**Issue:** Line 1441 says "An explicit per-region recompute at the canonical denominator is deferred to the verification artifact wave14_canonical_recount/sky_balance_canonical.json; the snapshot row is retained alongside the canonical row so the reader can verify the ≲4% insensitivity claim directly." Reviewer: does that JSON exist? If yes, why is the per-region recompute not in the table now? If no, the paper is forward-referencing a file the public release won't have. A 3-sig-fig per-region recount on a 3.2M-row catalog is a 5-minute pandas operation. Run it; put the numbers in the table.

## NITs

### n1: \keywords line 131 includes "large-scale structure of Universe" which is non-standard PRD/MNRAS style — should be "large-scale structure of universe" lowercase or replaced.
### n2: "uniform at 7-region survey granularity" is awkward phrasing and appears 9+ times by replace-all. Consider "uniform across 7 survey footprint regions" once and back-reference thereafter.
### n3: Equation labels eq:sigma_pix and eq:sigma_dip use \ref instead of \eqref in some prose (e.g., line 1879 "Analytically (Eqs.~\ref{eq:sigma_pix}--\ref{eq:sigma_dip})"). Minor — \eqref preferred for PRD style consistency.
### n4: "complementary one-tailed χ² tail probability for |z|=0.12 is ≈ 0.91" (line 1254) — for a 1-dof χ², the survival function at χ²=0.12² = 0.0144 is sf(0.0144) ≈ 0.90, consistent. But this only works *because* it's labeled as 1-dof. If M3's correction lands (5-dof or 6-dof for ℓ=1), this sentence's 0.91 number changes substantially. Audit jointly with M3.

## Reviewer disposition

**Major revision.** The catalog construction, the equivariant TTA pipeline, and the dipole-null measurement itself are sound and represent a real advance over Shamir's positive claims. The methodological *framing* of the results — what is an upper limit vs a sensitivity floor (B1), what the post-MASTER χ²/dof = 4.22 means relative to "consistent with null" (B2), the joint-bandpower test (M1), the dof choice at ℓ=1 (M3), and the deferred McNemar tabulation that takes seconds on a laptop (M4) — needs another pass. Fix B1 and B2 and this is a solid PRD-ready null-result catalog paper. Leave them and a competent statistics referee will request the same revisions I have requested above. The 5-agent round closed a lot of surface text but did not pressure-test the χ²/dof footnote or the title's "upper limit" claim against the actual statistic being computed.
