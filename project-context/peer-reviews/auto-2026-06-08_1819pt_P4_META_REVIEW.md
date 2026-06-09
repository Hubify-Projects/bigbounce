# P4 auto-2026-06-08_1819pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 233.8s

---

# META-REVIEW — P4

After reading the PDF and the five prior reports, I focus only on issues that none of the five reviewers caught. The most damaging findings concern (a) an internal contradiction in the *definition* of the chirality field Aₚ between two passages of Appendix A — affecting the entire MASTER chain — and (b) the unsupported A₉₅ claim that anchors the abstract's "falsification criterion" and the Shamir-tension statement.

---

## NEW ESSENTIAL findings

### P4-META-E1. Contradictory definitions of the asymmetry field Aₚ within Appendix A.
**Page 9, Appendix A.** No reviewer caught this because it is buried inside the NaMaster configuration paragraph and the two formulas are separated by half a page of prose; both look correct individually.

Appendix A, paragraph (a):
> "*The asymmetry field is Aₚ = (N⁽ᵖ⁾_CW − N⁽ᵖ⁾_CCW)/(N⁽ᵖ⁾_CW + N⁽ᵖ⁾_CCW) (spirals only).*"

Appendix A, paragraph (c) — same appendix:
> "*Field: scalar (spin-0) asymmetry map Aₚ = (N⁽ᵖ⁾_CW − N⁽ᵖ⁾_CCW)/N⁽ᵖ⁾_total, with galaxy-weighted mask-mean subtraction…*"

These are not the same field. The first uses a spirals-only denominator (N_CW+N_CCW), the second uses N_total = N_CW+N_CCW+N_NS (i.e., includes the ~62% not-spiral pixel content). The two definitions differ by a factor of ~1/0.38 in per-pixel amplitude, propagating directly into the MASTER-decoupled Cℓ, into σ_null, and into the canonical-mask +3.64σ residual. Equation (3) in the main text uses the spirals-only definition; Table I caption uses W_p = N⁽ᵖ⁾_all (depth proxy). Footnote 1 on page 5 then conflates the field denominator with the mask weight (Claude_brutal flagged this confusion but did not realize Appendix A *itself* uses both definitions for Aₚ).

**Required fix:** Adopt one definition. State it explicitly in the main text at Eq. (3) and in *every* appendix. Recompute the post-MASTER Cℓ chain (1.494×10⁻⁶, σ_null = 4.290×10⁻⁷, −0.122σ; canonical +3.64σ; Table III bandpowers) under the single declared definition. Until this is done, the headline σ values cannot be reproduced from the manuscript.

### P4-META-E2. The falsification criterion A₉₅ ≈ 1.5–2% is asserted without supporting injection-recovery data.
**Page 8, §VI A.** No reviewer caught this because the criterion appears in the abstract as a fait accompli and the relevant injection-sweep text reads at first glance like it supports the claim.

The paper provides only two empirical injection-recovery data points:
- A = 0.75% → P(σ>3) = 0.55
- A = 0.50% → P(σ>3) = 0.15

From these two points alone the paper announces:
> "*the corresponding 95%-recovery-at-3σ threshold (the falsification boundary) is A₉₅ ≈ 1.5 − 2%*"

A two-point sweep cannot constrain a 95%-recovery percentile with the quoted ±0.25% precision. No injection at A = 1.0%, 1.25%, 1.5%, or 2.0% is reported. The A₉₅ value is the centerpiece of the abstract's falsification statement and the Shamir-tension claim — and it is an extrapolation from two data points spanning 15%–55% recovery, then projected onto the 95% level with no fit or error bar.

**Required fix:** Run injection-recovery at additional amplitudes (≥4 amplitudes covering 50% to >95% recovery), fit a logistic-style sigmoid with reported CI, and report A₉₅ ± uncertainty. Or remove the A₉₅ = 1.5–2% claim from the abstract.

### P4-META-E3. The Shamir-tension "factor of 6–12" requires equating observed amplitudes from non-matched classifiers, but the paper's own dilution factor undoes the comparison.
**Page 2 §I, Page 8 §VI B.** No reviewer noticed that the paper's own GZ1-dilution factor sabotages the headline Shamir tension claim.

Page 8: "*GZ1-dilution factor g = 2a−1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼1.88%*"

So in *true underlying* amplitude, this analysis's 50%-recovery sensitivity is 1.88%, not 0.75%. Under the same logic, the A₉₅ ≈ 1.5–2% observed corresponds to A₉₅ ≈ 3.8–5% in true underlying amplitude. Shamir's reported ~3% asymmetry, if interpreted as observed asymmetry under his classifier, has its own dilution; if interpreted as true amplitude, then it is *below* this paper's A₉₅ in true-amplitude units. Either way, the "factor 6–12" tension is not numerically supported once the GZ1-dilution g = 0.398 (which the paper itself invokes) is applied consistently.

**Required fix:** Either (a) drop the "factor 6–12" tension claim from §I and §V A, or (b) state what classifier-accuracy correction is applied to Shamir's 3% before computing the ratio, and justify it.

### P4-META-E4. The "subsample mask" (fsky = 0.659) selection threshold is never defined; the headline result depends on an unspecified post-hoc choice.
**Multiple sections; primarily Page 4 Table I and Page 9 Appendix A.** No reviewer caught this because both fsky values are quoted as if they were objective survey footprints rather than analyst-chosen pixel-inclusion thresholds.

The canonical mask is defined as "pixels with ≥10 spirals" (fsky = 0.49005). The subsample mask is called "strict-superset" with fsky = 0.659, but the pixel-inclusion threshold defining it is never given. Appendix E reports a sweep from 5 to 50 spirals/pixel and says "<0.5σ variation in the headline ℓ=1 MASTER result" — but does not state which threshold is the headline subsample-mask choice (≥1? ≥5? something else?), nor whether the −0.122σ depends on choosing the optimum.

Given the canonical-mask result is +3.64σ and the subsample-mask result is −0.122σ — a swing of nearly 4σ depending on mask geometry — the pixel-inclusion threshold is *the* dominant analysis choice. The headline null cannot be assessed without knowing whether the threshold was pre-registered or selected from a sweep.

**Required fix:** State the exact pixel-inclusion threshold defining the subsample mask, justify it independently of the dipole result, and show the ℓ=1 σ as a function of threshold over the full sweep (not just the headline value).

---

## NEW MAJOR findings

### P4-META-M1. The look-elsewhere result is internally contradictory by ~3 orders of magnitude.
**Appendix C, page 10.** Reviewers noted the LEE handling was qualitative, but none flagged the numerical inconsistency.

> "*The direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤ 10⁻⁴ (rejection of the random-label null); the conservative Bonferroni/BH penalty across ∼ 650 tested directions reduces post-LEE significance to < 1σ.*"

These are not different views of the same statistic; they are mutually incompatible global p-values. Direct-MC p < 10⁻⁴ ↔ ≳3.7σ global; Bonferroni p > 0.16 ↔ <1σ global. The ratio is >1000×. Either the per-pixel-shuffle null destroys spatial correlations that hemispheres rely on (making the direct-MC p artificially small), or Bonferroni is grotesquely over-conservative for 650 highly correlated hemisphere directions. The paper cannot keep both numbers and call the LEE-corrected significance "<1σ" while also claiming pLEE ≤ 10⁻⁴.

**Required fix:** Reconcile or pick one. The natural compromise is a max-stat MC under a *spatially correlated* null (Gaussian field with matched Cℓ on the canonical mask); this is the standard treatment and would replace both numbers with a single defensible global p-value.

### P4-META-M2. The headline real-space dipole +0.43σ result is reported without an amplitude.
**Page 4 §IV C a, Page 8 conclusions.** The MASTER chain gets full Cℓ tables; the real-space dipole — described in §III A as the *primary* cosmological estimator — never has its fitted amplitude quoted.

Without A_dipole ± σ(A_dipole) from the real-space fit, one cannot:
- compare the real-space estimator to the Fisher floor (0.29%) or to A₅₀ (0.75%),
- check internal consistency with the +4.31σ "monopole-preserving" full-Cat-C dipole flagged in Appendix E,
- assess whether the +0.43σ corresponds to A ≈ 0.05% (Poisson-floor-noisy) or A ≈ 0.4% (sensitivity-limited).

**Required fix:** Report the fitted amplitude, its uncertainty, and the direction (l, b) for both the +0.43σ Catalog C result and the +4.31σ monopole-preserving Catalog C result so the reader can confirm they are mathematically consistent given the monopole subtraction.

### P4-META-M3. Bandpower σ values in Table III are not auditable from the table.
**Page 6 Table III.** Reviewers noted the χ²/dof = 4.24 was unjustified but missed that the individual row σ values cannot be derived from the displayed numbers.

For ℓ_eff = 9: Cℓ = −0.248 × 10⁻⁶, σ_null = 0.574 × 10⁻⁶, reported significance = +2.232. By |Cℓ|/σ_null = 0.432, not 2.232. The discrepancy means the null *mean* is non-zero and equal to roughly ⟨C⟩ ≈ −0.248 − 2.232 × 0.574 ≈ −1.53 × 10⁻⁶. The null mean is never displayed.

The same arithmetic problem affects ℓ_eff = 14, 19, 24 (all four "Residual mask coupling" rows). Without the null mean, the reader cannot reproduce or audit any of the row significances.

**Required fix:** Add a column "⟨C_null⟩ × 10⁶" to Table III. State the sign convention used for σ (signed difference vs absolute).

### P4-META-M4. Sensitivity floor was measured on the HC subsample, not the headline sample, and is not properly re-scaled.
**Page 8 §VI A.** The injection-recovery sweep is on the HC-spiral subsample (N = 471,049). The headline real-space dipole and MASTER analyses are on N = 3,201,160 (Catalog C all-spiral) — 6.8× larger. Statistical uncertainty scales as 1/√N, so the *full-catalog* 50%-recovery threshold should be ~0.75% / √6.8 ≈ 0.29% (Fisher floor), not 0.75%.

The paper applies the 0.75% threshold to the headline analyses anyway, claiming a "sub-percent sensitivity floor" with no scaling. This is sample-size mismatched and inconsistent with the abstract's framing.

**Required fix:** Re-run the injection sweep on the full Catalog C sample (or scale the HC result and validate against the Fisher floor). State explicitly which sample the A₅₀ = 0.75% applies to.

### P4-META-M5. Comparison to Iye/Tadaki is asserted but never demonstrated.
**Page 7 §V A.** The paper claims it "*corroborates and extend[s] the methodological critique of Iye et al. (2021)*" but does not analyze Iye's footprint, classifier, or selection. Iye (2021) is SDSS; this paper is DESI Legacy DR8. No matched-footprint comparison is provided. The corroboration is rhetorical, not statistical.

**Required fix:** Either run on the Iye/Shamir SDSS catalog footprint, or downgrade the language from "corroborates and extends" to "is consistent with the qualitative direction of".

---

## NEW MINOR findings

### P4-META-m1. The 234,282-galaxy independent GZ1 cross-match is implausibly large.
**Page 3 §II B.** GZ1 itself has only ~6,637 high-vote-confidence CW/CCW labels (also used in this paper's training set). It is unclear how a *disjoint* 234,282-galaxy cross-match against GZ1 is constructed — neither the GZ1 confidence threshold nor the matching radius nor the disjointness criterion is specified. The 69.91% accuracy / κ = 0.40 result depends entirely on these undisclosed choices.

**Required fix:** Specify the GZ1 vote threshold (e.g., p_cw > 0.5? > 0.7?), the cross-match radius, and what makes the 234,282 disjoint from the 6,637 training labels.

### P4-META-m2. Mean (0.951) vs median (0.9997) confidence is symptomatic of a bimodal posterior the paper never characterizes.
**Page 4 §IV A.** A 4.6-percentage-point gap between mean and median in a probability distribution bounded in [0,1] indicates either a left-tail of low-confidence objects or a sharp bimodality. This matters because the per-galaxy weighting in the dipole estimator is implicitly p_eq-flat (each galaxy = one count) while the actual information is concentrated near p ≈ 1 and noise is concentrated near p ≈ 0.5. The paper never shows the p_eq histogram.

**Required fix:** Show the p_eq histogram or quantile table. State whether soft-weighted (∝ |p_CW − p_CCW|) estimators were considered.

### P4-META-m3. The "+4.31σ monopole-preserving" full-Catalog-C dipole disclosed only in Appendix E is in tension with §VI B's parity statement.
**Page 11 Appendix E b vs Page 8 §VI B.** §VI B states "*the parity-odd signal lives in the ℓ = 0 monopole and even-ℓ multipoles*." Appendix E reports a +4.31σ result that "collapses" upon HC cuts — but if monopole subtraction is the difference between +4.31σ and the headline +0.43σ, the paper has subtracted the very channel it identifies as parity-odd. This is consistent with Claude_brutal's P4-E11 but the *physics* contradiction with §VI B is the new point: a parity test should not subtract the parity-odd monopole at the data-vector construction step.

**Required fix:** Explicitly justify the monopole subtraction as a *systematic* removal (classifier-zero-point), not a *physical* zero. Distinguish "morphological-classifier monopole" from "parity-odd ℓ=0 cosmological signal".

### P4-META-m4. The σ_null = 4.290×10⁻⁷ from 500 MCs is over-precise.
**Page 4 §IV C b.** Already noted in Claude_brutal N9 but more pointedly: σ on σ from N = 500 is σ/√(2(N−1)) ≈ 3.2%, so the trailing digit "0" in 4.290 is fictitious. With proper rounding, the headline becomes (1.49 − 1.55)/0.43 ≈ −0.14σ, and the "−0.122σ" precision evaporates. The title carries a digit that the MC cannot deliver.

---

## NIT

### P4-META-N1. Reference [2] (Shamir 2022, PASJ) has no in-text citation that I can locate; only [1], [3], [4] are cited for Shamir in §I and §V A.

### P4-META-N2. The 4 × 1 + 4 × 1 line "LayerNorm → … → 256→3 (softmax)" is numbered as Eq. (1), but it is a tensor-shape diagram, not an equation. (Also caught by Claude_brutal M10 — confirming.)

---

## Meta-review recommendation
**REJECT** (with invitation to resubmit after major rework)

Adding my findings to the five prior reports, the consolidated blocker count is approximately **15–20 essential-level issues** (Claude_brutal: 14 essential including pass 2; Gemini: 3; Grok: 2; me: 4 new; OpenAI failed; Perplexity unable to run). Several of these are individually sufficient to block PRD acceptance: the Fig. 2 / Catalog C composition mismatch (Claude E1), the Fig. 1 D₄/Z₂ TTA contradiction (multiple reviewers), the *two different definitions of the asymmetry field Aₚ inside Appendix A* (this meta-review E1), the unsupported A₉₅ extrapolation from two injection points (E2), the unspecified subsample-mask pixel-inclusion threshold (E4), and the load-bearing 99.3% figure the authors themselves admit is pending a rerun (Claude E5). My confidence the paper survives an external (non-bigbounce) PRD referee in its current form is **<10%**; my confidence it survives a methodology-focused referee (e.g., PRD's quantitative-methods desk) is **near zero**, because the Aₚ definitional inconsistency in Appendix A invalidates the entire MASTER chain until reconciled. With a thorough rewrite — definitions cleaned up, mask thresholds pre-registered, injection sweep extended, dilution propagated consistently to the Shamir comparison, length cut to ≤ 8 pages, and figure captions reconciled with figure bodies — the underlying methodological contribution (TTA + MASTER + monopole-leakage generative null at 8.47 M-galaxy scale) is genuinely novel and would be a credible PRD methods paper at perhaps 60% acceptance probability.