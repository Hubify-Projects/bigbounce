# P4 auto-2026-06-09_0025pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 232.2s

---

# META-REVIEW P4 — Issues None of the 5 Prior Reviewers Caught

**Reviewer**: META (post-hoc audit)
**Prior reviews scanned**: Claude_brutal (empty output), OpenAI_methodology (timeout), Gemini_cosmology, Grok_brutal, Perplexity_citations

I focused on issues that survive Gemini's numerical audit, Grok's adversarial framing, and Perplexity's citation/definition forensics. Eight new findings follow.

---

## P4-META-E1 [ESSENTIAL] — The +3.64σ headline number is, by the paper's own admission, ≈1.9σ
**Section**: Abstract (p. 1); Sec. IV D, Table IV (p. 6); Conclusions (p. 8)
**Why missed**: Buried inside a parenthetical in the abstract's third paragraph; reviewers focused on the leading "+3.64σ" number itself, not the parenthetical demolition that immediately follows it.
**Problem**: The abstract states, verbatim:
> "The post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σ_null moment-ratio; **empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent**; 500-MC binomial per-pixel-shuffle null)"

That parenthetical is the paper confessing that the rank-based, distribution-free significance is 1.9σ, while "+3.64σ" is a moment-ratio that implicitly assumes Gaussianity of the null. The 1.9σ–3.64σ gap *is* the non-Gaussianity of the null. Yet the body, Table III, Table IV, Sec. VI, Sec. VII, and Appendix D all quote "+3.64σ" without the 1.9σ qualifier. This is not an inconsistency between sections (which Gemini and Perplexity hunted) — it is a single section quoting two mutually contradictory numbers and using the larger one everywhere downstream.
**Required fix**: Replace "+3.64σ" with the rank-based 1.9σ (or report both at every occurrence) throughout the paper, including all section headers, tables, figure captions, and the title. The current title's claim of "Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual" is predicated on a 1.9σ effect, which does not survive the look-elsewhere correction applied elsewhere in the paper.

## P4-META-E2 [ESSENTIAL] — N_MC = 500 caps achievable empirical significance at ~2.88σ
**Section**: Sec. IV D (p. 4–5), Appendix A (p. 9), Table IV
**Why missed**: Reviewers verified the MC procedure ran, but did not check whether the MC budget could in principle support the quoted significance.
**Problem**: The per-pixel-shuffle null uses N_MC = 500. The minimum non-zero achievable p-value is 1/500 = 0.002, corresponding to a two-sided Gaussian-equivalent of ~2.88σ. The reported p_MC = 15/500 = 0.030 (= 1.88σ one-sided) is internally consistent, but the "moment-ratio" +3.64σ cannot be *empirically validated* by a 500-realization null; any value above ~2.88σ is unfalsifiable with this MC budget. Similarly, the hemisphere result "p_LEE ≤ 10⁻⁴" in Table I uses N_MC = 10,000, meaning that quoted bound is *saturated* — it means zero hits, not a measured value — and the "≤" hides this saturation.
**Required fix**: Either (i) raise N_MC to ≥ 10⁵ for the canonical-mask null and ≥ 10⁶ for the LEE test, or (ii) explicitly report both the moment-ratio σ *and* the empirical rank σ, and acknowledge that the empirical significance is MC-budget-saturated at ~2.88σ (canonical) and ~3.7σ (LEE).

## P4-META-E3 [ESSENTIAL] — Headline "subsample mask" is chosen post-hoc; no pre-registration
**Section**: Sec. III A (p. 3), Sec. IV C (p. 4), Appendix A (p. 9)
**Why missed**: All reviewers treated the mask hierarchy as given. Nobody asked whether the f_sky = 0.659 "subsample" mask was selected *because* it gave the null result.
**Problem**: The same Catalog C data evaluated on the **canonical mask** (f_sky = 0.49005) gives +3.64σ post-MASTER at ℓ=1, while evaluated on the **strict-superset subsample mask** (f_sky = 0.659) gives −0.122σ. The latter is declared the "primary" headline estimator. The paper provides no a-priori, pre-registered criterion for choosing the subsample mask as primary. The mask is defined as a "strict superset" of the canonical mask — that is, it *adds* pixels — yet adding pixels (lower-S/N regions on the survey edge) is statistically *worse*, not better, unless one is hunting for null cancellation. The two masks differ by Δf_sky = 0.17, i.e. ~30% of the sky. The decision rule "use the subsample mask as headline" looks selected-on-significance.
**Required fix**: (a) State the date and rationale of the subsample-mask definition; (b) report both masks as co-equal primary estimators in the abstract and conclusions; (c) if the subsample mask was chosen after seeing the canonical-mask result, demote the −0.122σ to a secondary/robustness number and acknowledge the +3.64σ as the canonical-mask headline.

## P4-META-M1 [MAJOR] — Bias-hardening T6 and T8 thresholds are loose by factors of 12–35× relative to the science
**Section**: Appendix B, Table V (p. 10)
**Why missed**: Reviewers verified the tests "pass" but did not compare the pass thresholds to the sensitivity floor claimed in the science.
**Problem**: T8 declares CW/CCW balance acceptable at 50% ± 10%, and the result is 49.7%. The science claims sensitivity to chirality dipole amplitudes at A₅₀ ≈ 0.75% (i.e. ±0.375% from 50/50). A test that accepts ±10% balance offers ≈ **27× too loose a threshold** to falsify a balance violation at the 0.75% sensitivity scale. T6 (hemispheric null < 10%, result < 0.4%) is similarly loose: the Catalog C global monopole is 9.5σ from 50/50, and Appendix C reports a 3.05σ hemisphere asymmetry, yet T6 "passes" because the hemispheric CW *difference* (not the dipole projection) is < 10%. Both tests are theatrical: they cannot fail at the precision level the paper claims to constrain.
**Required fix**: Replace T6 and T8 thresholds with values matched to the sensitivity claim (e.g. T8: |f_CW − 0.5| < 3 × σ_binom ≈ 0.084%; T6: hemispheric difference < 0.5%). Re-run and report. T8 in particular fails any rigorous version at 9.5σ.

## P4-META-M2 [MAJOR] — Injection-recovery uses 471k HC subsample but is applied to 3.2M sample
**Section**: Sec. VI A (p. 8), Table I row (vi)
**Why missed**: Grok demanded an injection campaign and Perplexity asked about A₉₅ definition, but neither checked the sample-size mismatch between the injection target and the science target.
**Problem**: The empirical 50%-recovery-at-3σ threshold A₅₀ ≈ 0.75% is derived on the high-confidence subsample N = 471,049 (Table I row vi). The headline dipole nulls (rows i, ii) are evaluated on N = 3,201,160. Naive √N scaling gives σ_A ∝ 1/√N, so a 6.8× larger sample should drive A₅₀ down by a factor of √6.8 ≈ 2.6. The HC-derived A₅₀ = 0.75% therefore over-states the full-sample sensitivity floor by ~2.6×; the *full-sample* empirical floor should be A₅₀ ≈ 0.29% (which coincidentally matches the Fisher floor — not by accident). The paper's falsification criterion at A₉₅ ≈ 1.5–2% is therefore quoted on the wrong sample.
**Required fix**: Re-run the injection-recovery sweep on the full N = 3,201,160 Catalog C sample (the same sample on which the headline ℓ=1 null is measured), or explicitly justify why the HC-subsample sensitivity transfers to the full sample. The current presentation conflates a 471k sensitivity with a 3.2M science claim.

## P4-META-M3 [MAJOR] — Single-mode ℓ=1 MASTER with 3 a_ℓm modes is cosmic-variance dominated
**Section**: Sec. IV C, Table III (p. 6); Appendix A (p. 9)
**Why missed**: All reviewers accepted MASTER as a black box; none audited the multipole-counting.
**Problem**: At ℓ=1 there are 2ℓ+1 = 3 a_1m modes. The full-sky Gaussian cosmic variance on C_1 is √(2/(2ℓ+1)) × C_1 = 82% of the mean. Mode-coupling on f_sky = 0.659 inflates this. The label-shuffle null used as the σ denominator (σ_null = 4.29×10⁻⁷) is the *classifier-shot-noise* variance, not the cosmic-variance of a true dipole, and the two are *not* the same. The paper interprets −0.122σ against the shot-noise null as "consistent with no dipole at ℓ=1" — but a real cosmological dipole would have to compete against an irreducible 80%+ cosmic-variance floor on a single-mode measurement that the paper never computes. The reported sensitivity floor is therefore the *classifier-noise* floor, not the *cosmological-detection* floor.
**Required fix**: Compute and quote the cosmic-variance contribution to σ(C_1) explicitly; revise the falsification criterion to be the quadrature sum of classifier-noise + cosmic-variance σ. The paper currently understates the minimum amplitude required for a real dipole detection.

## P4-META-M4 [MAJOR] — W_p = N_all is the wrong weight for a spiral-chirality field
**Section**: Appendix A (p. 9), Table I caption (p. 4)
**Why missed**: Perplexity flagged the definition ambiguity but not the optimality of the choice.
**Problem**: The asymmetry field is A_p = (N_CW − N_CCW)/N_spiral defined on spirals only. The optimal inverse-variance weight is W_p ∝ N_spiral(p), since the shot-noise variance per pixel is ∝ 1/N_spiral. The paper instead uses W_p = N_all(p) = N_CW + N_CCW + N_NS. With ~62% NS contamination spatially uneven (high spiral-fraction in some footprint regions, low in others), N_all is a biased proxy for N_spiral that *down-weights* high-spiral-fraction pixels relative to optimum. This affects every pseudo-C_ℓ in Tables III and IV.
**Required fix**: Either re-run all MASTER computations with W_p = N_spiral(p), or justify the W_p = N_all choice with an explicit comparison showing the noise penalty is < 5%. The N_map_weighted = 5,547,858 number in Table I currently has no statistical meaning given the suboptimal weight.

## P4-META-M5 [MAJOR] — Footnote 1's "robustness" claim is internally contradictory
**Section**: Footnote 1, p. 5 (continued p. 5–6)
**Why missed**: Gemini flagged the "in queue" issue as a major revision, but did not notice the logical contradiction *within* the footnote.
**Problem**: Footnote 1 makes two incompatible claims:
> "the size of the resulting shift in the headline 99.3% reproduction figure (and in the +1.68σ residual of Table IV) is **not predictable analytically**"
followed immediately by:
> "the qualitative reproduction structure... is **robust to the trial-pool choice**; the quantitative 99.3% figure is specific to the N_spiral draw."

If the shift is not analytically predictable, the robustness claim cannot be asserted without running the N_all draw. The footnote both admits the question is unanswered *and* declares the answer robust. The N_spiral vs N_all per-pixel trial-count ratio is 1.49 (footnote's own number); a 49% inflation of the binomial variance could change the +1.68σ residual into −0.5σ or +3.5σ — either of which would substantially change the interpretation of Sec. IV D as evidence for a "monopole-mask leakage channel."
**Required fix**: Run the N_all draw before publication; if not, retract the "robust" claim and present Sec. IV D as a working hypothesis pending the N_all rerun.

## P4-META-N1 [MINOR] — The dilution factor g = 2a − 1 assumes random Bernoulli classifier errors
**Section**: Sec. VI A (p. 8)
**Why missed**: Perplexity flagged the propagation as undocumented but did not audit the model.
**Problem**: The paper writes "GZ1-dilution factor g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ~1.88%." This formula is correct *only* if classifier errors are independent Bernoulli(1−a) with equal CW↔CCW flip probability. But the same paper documents a 9.5σ global CW bias and a 1.2pp CW-vs-CCW recall asymmetry (Appendix B). For asymmetric, spatially-correlated classifier errors, the dilution can be larger or smaller than 2a−1, and is not generally a simple multiplicative factor on the amplitude.
**Required fix**: Replace the g = 2a−1 single-parameter dilution with a 2×2 confusion-matrix model derived from the GZ1 cross-match (the matrix elements are extractable from Cohen's κ = 0.40), and propagate this asymmetric noise into A_50 and A_95.

---

## Meta-review recommendation
**MAJOR REVISIONS** (bordering on REJECT-AND-RESUBMIT)

## Aggregate blocker count and survival assessment
Across the 4 substantive prior reports (Gemini, Grok, Perplexity, and this meta-review; Claude_brutal and OpenAI_methodology returned no usable content), the union of ESSENTIAL issues is approximately **11** (Gemini-E1, Gemini-E2, Grok-E1, Grok-E2, Perplexity-E2 through E17 condensed to ~7, Meta-E1, Meta-E2, Meta-E3) and the union of MAJOR issues is approximately **14**. The most damaging single finding is Meta-E1: the paper's own abstract converts "+3.64σ" to "≈1.9σ Gaussian-equivalent" in a parenthetical and then proceeds to use "+3.64σ" everywhere downstream, including in the manuscript title's framing of "Diagnostic Evidence." Combined with Meta-E2 (the 500-MC budget cannot empirically support the quoted σ), Meta-E3 (mask choice unrebutted as selection-on-significance), and Meta-M3 (cosmic variance never computed for the single-mode ℓ=1 estimator), my confidence that this paper would survive external PRD review **in its current form is below 10%**. The science (a careful null on the largest chirality catalog assembled) is genuinely publication-worthy, but the manuscript currently markets a 1.9σ–at–best canonical-mask "diagnostic" as a 3.64σ result, quotes a sensitivity floor derived on a 7× smaller sample, and uses a headline mask whose selection rule is not pre-registered. After a thorough rewrite addressing the union of all six review streams — particularly demoting "+3.64σ" to its honest 1.9σ rank value, expanding N_MC by 2–3 orders of magnitude, and re-running injection on the full sample — the paper would be a strong PRD candidate and a useful counterweight to the Shamir literature.