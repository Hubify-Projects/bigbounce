# P5 auto-2026-06-09_0025pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 206.4s

---

# Meta-review: P5 DESIVAST/V-Web spiral chirality

Three of the five prior reviewers actually returned content (Grok_brutal, Perplexity_citations, and Claude_brutal which returned essentially nothing; OpenAI and Gemini failed entirely). Grok and Perplexity converged on the same headline blockers: unpublished Paper IV dependency, future-dated arXiv IDs, post-hoc primary path designation, n=428 underpowered void bin, and the toy-EFT operator. Below are issues that survived both reports.

---

## NEW FINDINGS

### P5-META-E1 (ESSENTIAL) — Circular monopole subtraction in §VIII.F (p. 12)

**Why missed:** Both reviewers focused on whether the Paper IV monopole was *citable*, not whether the in-paper *re-subtraction* of that monopole is self-referential.

**Problem:** Table X is the key load-bearing table for the headline ("All four V-Web classes fall within |σ_vs monopole| < 1.15"). But the quantity subtracted is

> "f_CW^P5 = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals … the observed −5.00σ corresponds to ΔfCW^P5 ≈ −0.0028, ∼8% larger than the P4 catalog-mean."

The "P5 monopole" being subtracted is **the sample mean of the very sample being tested**. Subtracting the sample mean and then reporting that the residuals are consistent with zero is a tautology: by construction Σ_class n_class (f_class − f̄) = 0, so the weighted σ_vs monopole values must average to zero. The test of environment-independence requires comparison against a *fixed external* expectation (either 0.5 or a Paper IV value with its own uncertainty propagated), not the in-sample mean. The paper actually concedes the P5 monopole is 8% larger than P4 — this discrepancy is the residual that should be propagated, not absorbed.

**Required fix:** Either (a) propagate σ(f_P4) as an independent prior into Table X residuals so that the comparison has nonzero degrees of freedom, or (b) report residuals against fCW=0.5 with an explicit (non-self-consistent) model statement, and acknowledge that the "monopole-subtracted" framing in the headline is not a parameter-free test.

---

### P5-META-E2 (ESSENTIAL) — Confidence interval on the DESIVAST Δf_CW is not what the abstract implies (p. 11, Table VII–VIII)

**Why missed:** Both reviewers accepted the "<0.002 at all three independent void definitions" claim as evidence of a null; neither computed the SE of the *difference*.

**Problem:** Abstract: "three-algorithm DESIVAST robustness … returns |Δf_CW| < 0.002 at all three independent void definitions". Table VII reports Δf_CW = +0.0007 for VoidFinder at n_void=56,981, n_non-void=621,964. The standard error on the difference of two binomial proportions at p=0.5 is

SE(Δf) = √[0.25(1/56,981 + 1/621,964)] ≈ 0.00215.

So the observed difference of 0.0007 has a 95% CI of approximately [−0.0035, +0.0049]. The paper's framing — "|Δf_CW| < 0.002 at all three independent void definitions" — is the **point estimate**, not an upper bound. The actual 2σ upper bound on a true environmental effect from this measurement is ~0.005, i.e., 0.5 percentage points, not 0.2 pp. This conflates measurement (point) and sensitivity (interval) precisely in the way item #3 of the meta-prompt warns about.

**Required fix:** Replace every instance of "|Δf_CW| < 0.002" with a properly-stated upper bound (e.g., "consistent with zero; 95% CI on Δf_CW: [−0.0035, +0.0049]") and re-write the abstract to quote the 2σ upper bound rather than the point estimate.

---

### P5-META-M1 (MAJOR) — Cluster σ_obs is 1.4σ *larger* than the monopole prediction, not "within order unity" (§VI.A, p. 6)

**Why missed:** Both reviewers checked whether the cluster σ was significant against zero; neither audited the σ_obs − σ_pred arithmetic.

**Problem:** Quote: "σ_pred(filament)≈ −3.16 and σ_pred(cluster)≈ −3.28, both within order-unity of observation. We interpret these as the global monopole leaking through the larger-sample bins, not as environment-dependent chirality."

But σ_obs(cluster) = −4.66 vs σ_pred = −3.28 ⇒ residual = **−1.38σ excess**. Recomputing σ_pred = 2 × 0.0026 × √397,505 = 3.28 ✓. The cluster class is showing **more** deviation than the monopole predicts, by 1.4σ. The within-class density stratification (Table IV) makes this worse: cluster Q1 σ=−3.07 and Q2 σ=−3.42 individually cross the Bonferroni-4 threshold (|σ|=2.50 at α=0.05). The paper attributes this to "boundary-misclassification leakage from filament" but provides no quantitative leakage model — the asserted resolution is qualitative.

Additionally: σ_pred(filament) ≈ −3.16 is arithmetically wrong; the correct value is 2 × 0.0026 × √408,187 = **3.32**, not 3.16. Minor but it shifts the "within order unity" claim.

**Required fix:** Acknowledge the cluster −1.4σ residual excess explicitly; either propagate it as a candidate environmental signal or provide a quantitative boundary-leakage model that absorbs it. Fix the σ_pred(filament) arithmetic.

---

### P5-META-M2 (MAJOR) — The V-Web 4-class scheme is effectively a 2-class scheme; the "4-class null" is partially trivial (§IV.B, Table II)

**Why missed:** Reviewers accepted the void/wall/filament/cluster taxonomy at face value.

**Problem:** Volume fractions (Fig. 1): {void 24.4%, wall 41.3%, filament 33.3%, cluster 1.0%}. Galaxy fractions (Table II): {void 0.05%, wall 0.84%, filament 51.6%, cluster 50.2%}. So 99.1% of chirality-relevant matched spirals are in filament+cluster despite those classes being only 34% of the in-footprint volume; the wall class — *the volume-dominant class at 41%* — contains 0.84% of galaxies, and the void class is essentially empty. This is a ~50× anti-bias for walls and ~450× anti-bias for voids, which is implausible for genuine biased-tracer behavior on a 25 Mpc/h smoothing scale (expected halo bias factors are O(1–5), not O(50–500)).

The almost certain explanation: the survey-footprint mask dilation (§IV.A step 5) creates a large boundary layer of void/wall-classified cells that contain no DESI galaxies because they sit at the survey edge. The "4-class" test is therefore effectively a "filament vs cluster" test, and the headline null on the small void/wall bins (Table II) is a counting-statistics statement about almost-empty bins rather than an environmental statement.

**Required fix:** Either restrict the V-Web analysis to cells more than 1× R_s from the mask boundary (and re-run the null) or restate the headline as a filament-vs-cluster test on the 99% population. The current four-class presentation overclaims the structural diversity being probed.

---

### P5-META-M3 (MAJOR) — The ASTRA cross-check is presented as a robustness success but is actually a robustness *failure* (§X, pp. 16–17)

**Why missed:** Both reviewers focused on the DESIVAST and V-Web paths.

**Problem:** Direct quote: "ASTRA argmax distributes the 25,186 spirals as 11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot, while V-Web puts essentially the entire sample into filament (31.7%) and cluster (68.3%), with only 3 spirals total in the V-Web void + wall classes." This is **near-total per-galaxy classifier disagreement**. The paper then concludes: "Despite this strong classifier disagreement on per-galaxy environment assignment, the chirality-vs-environment headline is recovered identically by both. … This is a strong robustness result."

This logic is inverted. If two classifiers assign opposite per-galaxy labels and both return a null, the only thing demonstrated is that **chirality is uniform on the sky at the EDR overlap scale** — which is the trivial null already established by Paper IV's catalog-monopole result. It is not evidence that the V-Web environmental signal is robust; it is evidence that the EDR-overlap subsample carries no environmental signal *under any classifier*, which is consistent with the classifiers being uncorrelated noise on this sample.

**Required fix:** Remove the "strong robustness result" framing in §X and Conclusions. State explicitly that the ASTRA cross-check tests only the catalog-wide uniformity (already known from Paper IV), not the environment-dependent chirality null per se.

---

### P5-META-M4 (MAJOR) — Tempel "isolated" σ=−2.54 is **double** the monopole prediction; dismissed as "counting statistics" without arithmetic (§IX.A, Table XI)

**Why missed:** Reviewers focused on the headline filament concordance (0.026 pp) and did not check the lower-richness Tempel classes.

**Problem:** Tempel isolated: n=58,539, σ_obs=−2.54. The Paper IV monopole prediction is σ_pred = 2 × 0.0026 × √58,539 = **−1.26**. Observed is 2.0× the prediction, residual ≈ −1.3σ — the same magnitude excess as the V-Web cluster bin. The paper writes: "The V-Web void (n=428) and the Tempel isolated bins differ by counting statistics at the small-n end" — this is the wrong dismissal; n=58,539 is not small, and the σ excess over the monopole is the relevant statistic.

If anything, *both* cross-classifier checks (V-Web cluster excess and Tempel isolated excess) point in the same direction: dense and isolated environments may show a ~−1σ residual excess relative to filament/wall after monopole subtraction. The paper does not test this directly.

**Required fix:** Add the σ_obs − σ_pred residual column to Table XI and compute the joint significance of the Tempel-isolated + V-Web-cluster residual excess against a uniform-monopole null.

---

### P5-META-M5 (MAJOR) — Pearson r=+0.006 at n=727 is a 1/n^½ ≈ 0.04 sensitivity test; the claim of "statistically indistinguishable from zero" overstates the upper bound (§VIII.F, Fig. 6)

**Why missed:** Reviewers accepted the p=0.88 verdict without checking the corresponding sensitivity envelope.

**Problem:** At n=727 pixels, the 2σ upper bound on a Pearson correlation is approximately 2/√n ≈ 0.074. So a true environmental correlation of r=0.07 would not be detectable; the measurement rules out only |r| > ~0.07. The paper writes: "indistinguishable from zero. A genuinely environment-dependent chirality signal would produce a detectable monotonic correlation" — the second sentence is only true for correlations above the 0.07 sensitivity floor, which is non-trivial for an a-priori weak effect. This is again the precision-vs-sensitivity conflation (meta-prompt item #3).

**Required fix:** State explicit 2σ upper bound: "r = +0.006 ± 0.037 (1σ), 95% CI [−0.07, +0.08]; the test rules out |r| > 0.07 at 2σ but is not sensitive to weaker correlations."

---

### P5-META-m1 (MINOR) — The Phase 2 sweep at R_s=50 Mpc/h does not test sensitivity but tests over-smoothing (§VII, Table VI)

**Why missed:** Reviewers did not analyze what the sweep actually measures.

**Problem:** At R_s=50 Mpc/h on a 25.9 Mpc/h grid, the Gaussian smoothing kernel spans roughly 4×4×4 cells, washing out essentially all sub-cluster structure. Finding that the inter-class range is small (0.05–0.13 pp) at R_s=50 is trivially expected: the four eigenvalue classes converge to a single density-density label. The "robustness to V-Web hyperparameters" claim is therefore weakest exactly where the paper claims it is strongest. The genuinely informative sensitivity probe (R_s < 10 Mpc/h, where halo-scale physics is resolved) is missing.

**Required fix:** Add a R_s = 5 Mpc/h cell to the sweep, or reframe the sweep as testing robustness over a *limited* range that excludes the halo-resolved regime.

---

### P5-META-m2 (MINOR) — The "0/6 V-Web void spirals fall inside any DESIVAST hole" small-sample sanity check is logically presented backwards (§VIII.A)

**Why missed:** Reviewers accepted it as cross-classifier disagreement.

**Problem:** With only n=6 test cases and 101,863 DESIVAST holes spanning ~10% of the BGS volume, the *a priori* probability of any of the 6 random matched-spiral positions landing in a hole is ~10%, so 0/6 versus 1/6 has p ≈ 0.53 under the null. The "0/6" result is not informative about V-Web vs DESIVAST agreement at the small-sample level; the paper's interpretation ("the V-Web 'void' label at low z should be read as 'not in a DESIVAST-defined cosmic-web density minimum'") cannot be supported by n=6.

**Required fix:** Drop the 0/6 cross-check or replace it with an n>200 sample by relaxing the z≤0.24 cut to match a fairer matched-volume comparison.

---

### P5-META-N1 (NIT) — Broken internal cross-reference

§VIII says "This is in contrast to the V-Web secondary path (§XIII)" but §XIII is "Limitations," not a V-Web secondary path. (Perplexity caught a related instance but flagged it differently; this one is the actual broken anchor.) Fix the cross-reference.

---

## Meta-review recommendation

**REJECT**

Given the union of all six reviews: the unpublished/non-citable Paper IV dependency (Grok E1, Perplexity E1–E2), the three future-dated or mis-cited arXiv IDs (Perplexity E3), the post-hoc primary-path designation (Grok E2), the under-powered void bin headline (Grok E3), the self-referential monopole subtraction (P5-META-E1), the misstated CI on the DESIVAST Δf_CW (P5-META-E2), and the V-Web 4-class scheme that is structurally a 2-class scheme (P5-META-M2) constitute **at least 7 independent blockers**, of which two (P5-META-E1 and -E2) directly undermine the headline-result framing. The toy EFT operator (Grok M4, Perplexity E7) and the buried 3.4σ filament bright-vs-dark sign-flip (Grok M3, also flagged here) compound the picture. My confidence that this paper would survive non-bigbounce external peer review at PRD in its current form is **below 5%**; even a non-hostile referee at MNRAS or PASP would require the Paper IV dependency to be discharged and the monopole-subtraction logic rebuilt against an external reference before consideration. The path to publication is conditional on (i) Paper IV being publicly archived first, (ii) the monopole-subtraction methodology being recast to use an external prior rather than the sample mean, (iii) properly-stated upper-bound intervals throughout, and (iv) compression to ≤12 pages with the toy EFT and ASTRA paragraphs removed.