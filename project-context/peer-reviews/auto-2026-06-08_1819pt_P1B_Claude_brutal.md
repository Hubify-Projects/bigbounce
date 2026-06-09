# P1B auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (9652 chars)
**Wall time**: 476.8s

---

# Referee Report — P1B (Technical Verification Companion)

## Overall assessment

The paper repeatedly and explicitly disclaims that any of its three analyses verifies the ECH spin-torsion program it advertises as a "Technical Verification Companion" to. Specifically:

- Analysis (1) is "Not a spin-torsion theory module" (Sec. III header, Sec. I item 1).
- Analysis (2) is "Not a competitive sky detection" (Sec. I item 2).
- Analysis (3) is "Not a distinctive ECH prediction... the same β ≈ 0.27° arises in any GR+ALP setup" (Sec. I item 3).

This is a self-defeating frame: the companion paper to the ECH program contains zero numerical results that bear on the ECH program. By the author's own admission. This is fatal to the publication case as written.

Beyond the framing issue, there are arithmetic errors, sample-count gymnastics, undisclosed-in-abstract analyses, version-history prose in the body, and admitted fine-tuning rebadged as "natural" consistency.

I list findings below.

---

## ESSENTIAL

### P1B-E1 — Scope: paper does not do what its title promises
**Sec. I, Sec. III header, Sec. VI Note.** Title is "Technical Verification Companion to the ECH Spin-Torsion Program," but by the author's repeated statements no analysis in the paper tests the ECH spin-torsion sector at all. The Boltzmann code is stock; the NaMaster work is a pipeline self-test; the ALP analysis works identically in GR. **Required fix:** either (a) retitle as "ΛCDM+ΔNeff Companion and ALP Birefringence Consistency Check — Not a Direct Test of ECH" and remove every claim to the contrary, or (b) actually compute one ECH-specific signature (modified Boltzmann hierarchy with torsion source, modified ALP-torsion coupling derived from the Holst action, etc.). As written, this is not a verification of anything in Paper I(a).

### P1B-E2 — Table II footnote b: arithmetic of σ_wpivot is wrong
**Page 4, footnote b.** Quoted: "σ²_wpivot = σ²_w0 + (1 − ap)²σ²_wa = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²."

Recomputing the LHS as stated: 0.0436² + 0.332²·0.1864² = 0.001901 + 0.003830 = **0.005731 = (0.0757)²**, not (0.0301)² = 0.000906. The displayed identity is off by a factor ≈ 6. The correct decorrelation formula for the pivot variance is σ²_wpivot = σ²_w0 − Cov²/σ²_wa (variance is *reduced* at the decorrelation pivot, not the sum-of-positives quoted). The displayed equation is dimensionally a sum, but algebraically requires the negative covariance term. The footnote's pedagogical derivation of ap=0.6680 is therefore internally inconsistent with its claimed numerical output. **Required fix:** derive ap and σ_wpivot correctly, quote the actual Cov(w0,wa) from the chain, and either verify σ_wpivot = 0.0301 or correct the value.

### P1B-E3 — DESI w0wa quintom analysis is not in the abstract
**Table II, Sec. V.** The most substantive numerical content of the paper — a 128,385-sample DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+ chain returning w0 = −0.812 ± 0.044, wa = −0.667 ± 0.186, "phantom-crossing required," "canonical quintom signature" — is absent from the abstract. The abstract advertises three analyses; the paper contains four. This is a significant abstract–body mismatch for the headline quintom result. **Required fix:** either add the w0wa analysis to the abstract (with the caveats from §V about the deferred ln B / nested-sampling work) or remove Table II and the §V quintom discussion to a separate paper.

### P1B-E4 — "+4.3σ" and "−3.6σ" w0/wa departures juxtaposed with disclaimers in different parts of the paper
**Table II, footnote a, §V Results.** The paper quotes w0 at "+4.3σ" and wa at "−3.6σ" from ΛCDM, computes a (w0+wa) phantom-crossing claim, but discloses (in footnote a) that LCDM is *unsampled by the chain* and these are "marginal-tail posterior-extrapolation departures" — not Bayes factors, not frequentist tensions. Yet the body text in §V then says "the headline result is w0 = −0.812 ± 0.044 (departing from the ΛCDM point w0 = −1 at +4.3σ)... requiring phantom crossing (the canonical quintom signature)." Headline-significance language for an unsupported quantity. **Required fix:** at every juxtaposition of these σ-values, attach "marginal-tail extrapolation, not a Bayes factor or frequentist tension," not only in the footnote. The body should not say "departing... at +4.3σ" in headline voice when the same paper has already disowned that interpretation in a footnote.

### P1B-E5 — Version-history / internal-audit prose throughout the body
The body contains explicit revision-log language:

- Page 3: "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w0wa samples at the LCDM point..."
- Page 3: "(note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but with zero free-w0wa samples at the LCDM point the KDE estimator fails catastrophically)"
- Page 5: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood..."
- Page 4: "MB–H0 joint-posterior offset check. A concern was raised that the joint posterior mean..."
- Page 6: "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°, a relative ~12% amplitude-dependent component"
- Page 8: "§VI for the explicit numerical derivation correcting the earlier Caγθi product"

This is review-log prose that does not belong in a published manuscript. **Required fix:** remove every "earlier draft," "earlier count," "addressing reviewer concerns," "prior caveat promised," "initially characterized" reference and rewrite the affected paragraphs in clean expositional voice.

### P1B-E6 — Sample-count headline inflation
**Abstract, footnote 1.** The abstract advertises "309,189 frozen samples." Footnote 1 admits this is raw accepted samples; after burn-in only 216,432 remain; after getdist thinning the full-tension chain (Fig. 1) is 119,617. So the actual usable independent samples advertised in the corner plot are ~38% of the headline. The abstract figure is not what a competent reader would understand "samples" to mean for an MCMC. **Required fix:** quote the post-burnin or post-thinning ESS in the abstract. The minimum ESS (4,744) — which is what actually matters — is buried in Table I.

### P1B-E7 — "Pipeline-recovery SNR" of 20.32σ / 25.71σ is dimensionally a Monte Carlo standard-error figure
**Sec. IV, footnote 3.** The footnote correctly identifies that the headline "SNR = 20.32" is SNR_SE = β̂√N / σ_β̂ — i.e., a standard error on the *mean of 500 MC realizations*, not a per-sky detection. The per-realization SNR is ~0.91. The footnote acknowledges this but the body still presents the 20.32σ / 25.71σ numbers without parenthetical disambiguation at every occurrence. **Required fix:** every quoted SNR number must be tagged either SNR_SE (estimator-calibration) or SNR_real (per-map detectability); a single footnote far from the headline number is insufficient. Better: drop these MC-mean SNR numbers from the body entirely since they are uninterpretable as detection significances.

### P1B-E8 — "Spectator" claim and θi tuning are at war with each other
**Abstract, Sec. VI, footnote 5.** Abstract: ALP with fa ∼ MPl, m ∼ H0 is "consistent with" the joint signal. Spectator-status caveat then says the spectator label requires θi ≪ 1. Footnote 5 in §VI: spectator-consistent regime is θi ∼ 0.1, requiring ~25× fine-tuning relative to the natural θi ∼ 0.5 prior midpoint. The body §VI then says the data-anchored MCMC posterior is at *higher* θi than the natural prior box — i.e., the data prefers the regime in which the ALP is *not* a spectator and must be treated as the dark-energy field itself. So the model that the paper validates against data is the model the paper says is excluded from the analysis. **Required fix:** decide which regime is being defended. If the spectator analysis is the headline, the MCMC needs to be redone with θi ∈ [0.05, 0.2] (and Caγ allowed to float into the required ~50× enhancement range). If the data-preferred regime is the headline, the "spectator ALP" framing must be dropped.

---

## MAJOR

### P1B-M1 — Eq. 3 internal consistency
**Page 7, Eq. 3.** "β ≈ αEM × 8 / (4π) × 1.07 ≈ 0.29°" but the abstract and §VI lead text claim fiducial β = 0.27°. Recomputing: (1/137.036)(8)(1.07)/(4π) = 4.969×10⁻³ rad = 0.285° ≈ 0.29° as written. The 0.27° abstract value must therefore correspond to a different (m, θi) pair than the one used to derive Eq. 3. The text claims "the fiducial 0.27° corresponds to m ≈ 1.8 H0, Δφ/fa ≈ 1.0" — but Eq. 3 has Δφ/fa = 1.07 from a different parameter point. Body is making a moving target out of the "fiducial." **Required fix:** pick one fiducial parameter point, compute β at that point once, and use that single value everywhere.

### P1B-M2 — Pipeline bias is fraction of the signal
**Sec. IV, page 6.** Injected β = 0.27° recovered at 0.238° → 12% bias. Injected 0.342° recovered at 0.302° → 12% bias. These are not "well below the signal" — they are comparable to the systematic envelope on the published Planck NPIPE 0.30° ± 0.11° (where 0.04° bias is ~36% of the 1σ uncertainty). Calling this "unbiased at the 0.04° level" understates the impact. **Required fix:** quote the bias as a fraction of the signal and as a fraction of the published statistical uncertainty, and discuss why a 12% multiplicative bias is acceptable for a pipeline being held up as validation.

### P1B-M3 — Required Caγ range "9 to 51" includes regions outside any known UV completion
**Page 8.** "the entire required range therefore lies outside minimal ALP photon-coupling benchmarks and requires non-minimal model building... the upper end (∼51) requires either substantial UV-completion enhancement..." This is a strong negative result that is reported in passive voice and then waved away with "the signal is therefore accommodated across the considered parameter space rather than fine-tuned only at one benchmark." It is fine-tuned — by ~25× in θi at fixed Caγ = 8, or by 9–51× in Caγ over the natural range. **Required fix:** the statement "consistent with the published joint... value" in the abstract should be replaced with "accommodates the published... value only at non-natural Caγ ≳ 9 with a 25× tuning of θi."

### P1B-M4 — "Convergence" claim for the third combination is hidden
**Abstract, Sec. III, footnote 1.** "a third Planck-only combination ongoing" — footnote 1 admits R̂−1 ~ 0.05, which is 5× the convergence threshold. This is not "ongoing"; it is unconverged. **Required fix:** state plainly that the Planck-only chain has *not* converged at the publication threshold and is excluded from frozen results.

### P1B-M5 — Cobaya version inconsistency
**Sec. V A.** "Parameter estimation uses Cobaya [20] (v3.5 original; v3.6.1 verification)." Which version produced the headline numbers? Was the v3.5 chain re-run on v3.6.1, or are different parts of Table I from different code versions? **Required fix:** state explicitly which numerical results come from which Cobaya version and confirm reproducibility across versions.

### P1B-M6 — Equation 2 evaluated at θi = 1 contradicts the spectator-status caveat
**Page 7, Eq. 2.** "∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)" but the abstract says spectator-status requires θi ≪ 1. So the load-bearing ALP-EOM number quoted in the body is computed at a parameter point the abstract explicitly excludes from the spectator regime. **Required fix:** recompute Eq. 2 at θi = 0.1 (the spectator-consistent value per footnote 5) and report that number as the fiducial.

### P1B-M7 — Reference [11] (Liu et al.) cross-validation does not actually validate this work
**Sec. III.** "Liu et al. constrained an EC torsion model... finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8." But the Liu et al. model has torsion *modifications* to the Boltzmann equations — exactly what this paper's MCMC explicitly does *not* include. The H0 / σ8 agreement is therefore an agreement on Planck-dominated standard-cosmology parameters, not a validation of the spin-torsion content. **Required fix:** drop the implication that this constitutes "cross-validation" of the torsion-sector claim.

### P1B-M8 — "Phantom-crossing required" is a model-prior choice, not a data-driven requirement
**Table II, Sec. V.** The w0wa parametrization with flat priors over a generous range will, generically, find non-zero wa whenever any redshift dependence in the SN distance modulus is present. Quoting "phantom crossing required" as a discrimination against ΛCDM, in a chain that does not sample the ΛCDM point, conflates posterior-extrapolation with model selection. **Required fix:** report the actual Bayes factor against ΛCDM via nested sampling (which the paper itself defers), or downgrade the "phantom crossing required" language to "the w0wa posterior is centered in the phantom-crossing region of parameter space."

### P1B-M9 — Page length disproportionate to content
The paper is 11 pages including references. After removing review-log prose, the deferred-to-future-work caveats, the contradictory regime caveats, and the cross-paper pointers, there is approximately 4 pages of actual numerical content (Table I, Table II, Fig. 1–3, and one paragraph each on the three analyses). **Recommended maximum:** 6 pages including references for the actual scientific content. Alternatively, fold P1B into P1A as an appendix; standalone publication is not warranted.

### P1B-M10 — Eskilt & Komatsu PR3 vs PR4 footnote in abstract
**Abstract footnote a.** The dataset attribution for the central observational claim of §VI is in a footnote on the abstract page, disclosing that the headline 3.6σ number is from PR3+WMAP9 but "ALP-MCMC re-runs actually use" PR4/NPIPE. This means the model is fit to one dataset and "consistency-checked" against the headline number from a different dataset. **Required fix:** rerun the ALP-MCMC against the PR3+WMAP9 likelihood that actually produced the 3.6σ headline, or rerun the headline number on PR4/NPIPE and quote that as the comparison value.

### P1B-M11 — χ² total reconciliation hand-waved
**Table II footnote c.** "The mean-of-total χ² here is GetDist's weighted-sample average over the full posterior, which differs from the sum of the individual-channel means (10.6 + 10983.9 + 3043.0 = 14037.5) by a 0.1-unit arithmetic-rounding artifact." The discrepancy is reported as 14037.4 ± 5.6 vs sum 14037.5. The "rounding artifact" framing is fine, but the ± 5.6 uncertainty on a sum of (10.6, 10983.9, 3043.0) numbers all of which have smaller individual uncertainties (1.8, 5.3, 1.6) suggests the total uncertainty should be sqrt(1.8² + 5.3² + 1.6²) = 5.84, which is consistent. Then this isn't a "rounding artifact," it's just sampling variance of the channel sums — but the wording is misleading. **Required fix:** state that the ±5.6 propagates from the channel uncertainties as expected, not as a rounding artifact.

---

## MINOR

### P1B-Mn1 — Reference [4], [5], [6] are "in preparation"
The paper cites three companion papers (II, III, IV) by the same author that are not available for refereeing. Cross-references to numerical results in not-yet-existing papers (e.g., "Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at pLEE < 10⁻⁴") cannot be evaluated.

### P1B-Mn2 — Inconsistent presentation of (ω/H)0
**Sec. II, Sec. V A.** The angular-momentum parameter is mentioned in motivation but explicitly fixed to zero. This is a confusing framing: either the bounce predicts something or it does not. Just say (ω/H)0 = 0 in stock ΛCDM+ΔNeff and move on; don't motivate the run with a parameter you have set to zero.

### P1B-Mn3 — ACKNOWLEDGMENTS mentions Claude as research assistant
Standard for some journals but the disclosure "All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author" needs to actually be true given the arithmetic errors flagged here (P1B-E2 in particular). Either the verification was not done or the error escaped it; either way the disclosure as written is undermined by the paper's actual error content.

### P1B-Mn4 — Fig. 1 caption sample count
**Fig. 1 caption:** "119,617 post-burnin samples, getdist-thinned from 176,240 raw." This is consistent with the table but contradicts the abstract's 309,189-headline. The body figure caption shows the actual usable sample count, the abstract does not.

### P1B-Mn5 — Fig. 3 caption claim vs body
**Fig. 3 caption:** "Bias β̂ − β_inj is below 0.04° across the natural resolution range." Body says 0.040° is the worst-case at β = 0.342°. "Below 0.04°" is misleading when the worst point equals 0.040° exactly. Use "at or below 0.04°."

### P1B-Mn6 — Footnote 1 reconciliation gymnastics
Footnote 1 spans ~250 words reconciling 309,189 / 216,432 / 119,617 / 123,368 / 123,129 / 114,992. Six different sample numbers in one footnote. This level of reconciliation prose indicates the headline number was not the natural one to quote; pick the right one and quote only it.

### P1B-Mn7 — "1σ" claim in ALP-MCMC paragraph (page 8)
"βALP = 0.336° ± 0.107°... consistent with the model-independent fit βfree = 0.344° ± 0.096°... and the observed βobs = 0.342° ± 0.094°. All three within 1σ." Three numbers fit to the same likelihood stack agreeing at <1σ is not a non-trivial consistency check — it is a tautology. The "1σ" agreement claim is not informative.

### P1B-Mn8 — Reference [3] arXiv 2509.13654 dating
Listed as 2025 arXiv preprint; check that the manuscript date (2026-06-08) is consistent with the cited reference being available.

---

## NITS

### P1B-N1 — "the spin torsion.input.yaml"
**Page 5.** Filename "spin_torsion.input.yaml" rendered as "spin torsion.input.yaml" — the underscore is dropped.

### P1B-N2 — Acronym spelling
"DESI" / "DESI DR2" / "DESI 2024 DR1" — three names for the BAO datasets across the paper. Standardize.

### P1B-N3 — Tense
"frozen" used throughout to mean "post-burnin, finalized for analysis" — this is non-standard MCMC terminology; "converged" or "production" is more conventional.

### P1B-N4 — Repeated long sentences in §V Results
Multi-clause sentences exceeding 6 lines (e.g., the model-comparison-statistics paragraph) impair readability. Split.

### P1B-N5 — "in km s⁻¹ Mpc⁻¹" in abstract appears after both H0 numbers; the second occurrence is in parentheses and could be moved to a single units note.

---

## Summary recommendation

**REJECT**

The paper is a "verification companion" whose author explicitly states verifies none of the substantive claims of the program it accompanies. The three advertised analyses are each disowned in their own scope statements; the most substantive numerical content (the DESI w0wa quintom analysis in Table II) is not in the abstract, contains an arithmetic error in its σ_wpivot derivation (P1B-E2), is presented with "+4.3σ" headline language for a quantity the same paper acknowledges is an unsampled posterior-tail extrapolation (P1B-E4), and the headline ALP "consistency check" requires a ~25× fine-tuning of θi and a Caγ outside any minimal UV completion. The body carries review-log prose, multiple sample-count reconciliations spanning six different numbers, an unconverged third chain mis-described as "ongoing," and a fitted-to-PR4 / compared-against-PR3 dataset mismatch buried in an abstract-page footnote. The contribution does not meet PRD standards for novelty (the ALP result works identically in GR), for self-consistency (P1B-E2, P1B-M1, P1B-M6), or for editorial cleanliness (P1B-E5). Folding the genuine content (Table I MCMC posteriors, NaMaster pipeline check) into Paper I(a) as a one-section appendix would be more appropriate than separate publication.

---

## PASS 2 — self-critique findings (what initial review missed)

# Re-Review — Additional Findings

After a closer second pass, I identified additional issues, particularly in arithmetic, dataset attribution, and bibliographic hygiene. The most consequential are P1B-E9 (which strengthens E2) and P1B-M19 (a real DESI-release inconsistency between the methods section and the headline table).

---

## ESSENTIAL

### P1B-E9 — Table II footnote b implies |ρ(w0,wa)| > 1 (mathematically impossible)
**Page 4, Table II footnote b.** Beyond the additive-vs-subtractive error flagged in E2, the *underlying inputs* in footnote b are mutually impossible. The decorrelation condition that defines the pivot is Cov(w0,wa) + (1−ap)·Var(wa) = 0, hence

|Cov(w0,wa)| = |1−ap|·σ²_wa = 0.332 × (0.1864)² = 0.01153.

But the maximum possible covariance for σ_w0 = 0.0436 and σ_wa = 0.1864 is σ_w0·σ_wa = 0.00813. The implied correlation is

|ρ| = 0.01153 / 0.00813 = **1.42**,

which exceeds the Cauchy–Schwarz bound |ρ| ≤ 1. No valid posterior covariance matrix can produce the quoted σ_w0, σ_wa, and ap simultaneously. Independently, using the standard identity σ²_wpivot = σ²_w0·(1−ρ²), the quoted σ_wpivot = 0.0301 with σ_w0 = 0.0436 implies |ρ| = 0.72, which is fine — but then the decorrelation pivot must be ap ≈ 0.832, *not* 0.6680. The displayed footnote ap and σ_wpivot are mutually contradictory regardless of what one takes as primary. **Required fix:** quote Cov(w0,wa) directly from the chain, recompute ap and σ_wpivot from that covariance, and verify the result. As displayed, the pivot derivation is internally non-physical.

### P1B-E10 — Editorial annotations inside published references
**Reference [15]:** the bibliography entry contains the phrase "the value used at L256/L416 of P1B" — an internal line-number pointer that does not belong in a citation. **Reference [22]:** contains a paragraph of editorial annotation ("canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers."). These are drafting notes that have leaked into the bibliography. **Required fix:** strip all non-bibliographic content from references.

### P1B-E11 — DESI release mismatch between methods and headline analysis
**Sec. V A vs Table II vs §VII.** Sec. V A ("Datasets and Configuration") explicitly lists "+DESI 2024 DR1 BAO [18]" (reference [18] = arXiv:2404.03002, DESI 2024 VI, DR1). Table II caption and stack: "DESI DR2 BAO" with reference [12] (DESI DR2 results II, arXiv:2503.14738). Conclusions §VII: "DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR" chain. So the methods section describes a DR1 configuration while the headline quintom analysis in Table II and the conclusion both use DR2 — different data releases with different BAO measurements. This is not a notation issue; DR1 vs DR2 are different datasets. **Required fix:** state explicitly which DESI release was used for each chain (the Table I ΔNeff combinations and the Table II w0wa chain) and correct §V A. As written, the reader cannot reproduce the headline result from the methods section.

---

## MAJOR

### P1B-M12 — Fig. 2 sample count (175,545) does not match any other reported number
**Fig. 2 caption.** "Full tension (175 545 samples)". Table I full-tension raw = 176,240. Fig. 1 caption = 119,617 (post-burnin/thinning). Footnote 1 reconciles 176,240 ↔ 123,368 (post-burnin) ↔ 123,129 (actual) ↔ 119,617 (further thinned). The Fig. 2 value 175,545 — 695 samples below the raw count — appears nowhere in the reconciliation footnote. This is a *fourth* distinct sample count for the same chain. Either it represents a minor post-burnin truncation that wasn't documented, or it is a stale draft number. **Required fix:** explain or correct.

### P1B-M13 — H0 = 67.69 (page 5) vs 67.68 (abstract, Table I, Conclusions)
**Page 5, mid-paragraph:** "The full-tension chain returns H0 = 67.69 ± 1.06 km/s/Mpc with ΔNeff = −0.02 ± 0.17." Abstract, Table I, and Conclusions consistently say 67.68 ± 1.06. A 0.01 km/s/Mpc inconsistency in the headline H0 suggests page 5 was not re-synchronized after a rerun. Either harmonize to the chain's actual value or document why one section reports a different rounding.

### P1B-M14 — Abstract "2.4–2.9σ" lower bound is unsourced
**Abstract, Sec. I item 2, Sec. VII.** "the published Planck/ACT DR6 2.4–2.9σ [2, 3]". From the two cited references: Planck NPIPE (ref [15], or the headline 3.6σ of [2] for the joint analysis) yields 0.30/0.11 = 2.7σ; ACT DR6 (ref [3]) yields 0.215/0.074 = 2.9σ. The 2.4σ lower bound is not supported by either cited reference and appears to come from an unsourced earlier measurement (possibly Minami & Komatsu 2020). **Required fix:** cite the source of the 2.4σ end of the range, or change the range to 2.7–2.9σ to match the actually cited works.

### P1B-M15 — Mb mis-categorized as a "Planck likelihood nuisance" parameter
**Table I footnote a.** "10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude." Mb is a supernova-likelihood nuisance, not a Planck nuisance. The count "10" includes a mis-categorized parameter. **Required fix:** separate the nuisance counts (9 Planck + 1 SN), which is conceptually important because Mb is the parameter that carries the SH0ES distance-ladder information (the load-bearing parameter for the very tension this paper discusses).

### P1B-M16 — Data-preferred ALP posterior lies outside the natural-prior box
**Page 8.** The data-anchored MCMC posterior implies Caγ·(Δϕ/fa) ≈ 10.3, giving Δϕ/fa ≈ 1.29 at the fixed Caγ = 8 — but the "natural envelope" upper bound for Δϕ/fa is 1.1 (achieved at θi = 2, m/H0 = 3, the *corners* of the prior box). The data is therefore pulling toward values beyond the prior boundary, which means the posterior is truncated/biased by the prior choice. The reported posterior mean cannot be interpreted as the data preference; it is a prior-edge effect. **Required fix:** rerun with prior θi ∈ [0.05, 5] (or whatever range is needed) and report the unconstrained posterior; alternatively, document that the data is incompatible with the natural-prior box and accept this as the result. The current "consistency check" framing is invalidated by the prior-edge proximity.

### P1B-M17 — Conclusions contain project-management prose
**Page 8, "Forward" paragraph.** "The 16-rank mpirun process terminated automatically upon reaching the convergence threshold; GetDist posteriors on w0wa are available..." This is sysadmin / log-file language. Replace with "the chain reached R̂−1 < 0.01 across two consecutive flushes" and drop the rest.

---

## MINOR

### P1B-Mn8 — "WP4 reheating" and "WP4 decay" undefined
**Fig. 2 caption.** Legend entries "WP4 reheating [0.05, 0.40]" and "WP4 decay [0.01, 0.25]" are never defined in caption or body. The reader cannot identify what theoretical scenario these benchmarks come from. **Required fix:** define WP4 in the caption with a citation.

### P1B-Mn9 — "ACT DR6 central (0.40)" in Fig. 2 ΔNeff axis is unsourced
**Fig. 2 caption.** A ΔNeff central value of 0.40 is attributed to ACT DR6, but reference [3] (the ACT DR6 citation used elsewhere) is the *cosmic birefringence* paper, not a ΔNeff measurement. The 0.40 ΔNeff value lacks a citation to the relevant ACT analysis.

### P1B-Mn10 — Post-burnin fraction does not match Fig. 1 sample count
**Footnote 1 vs Fig. 1.** Footnote 1 says burn-in is 30% (so post-burnin = 70% × 176,240 = 123,368). Fig. 1 caption reports 119,617 post-burnin samples, which is 67.9% of raw, not 70%. The footnote reconciles this with "additional getdist effective-sample weight-based thinning," but the thinning factor (123,368 → 119,617, a loss of 3,751 samples) is unquantified and undocumented. **Required fix:** state the thinning factor and the reason.

---

## NITS

### P1B-N6 — Inconsistent DESI release labels in §VII
**§VII Forward paragraph.** Uses "DESI DR2" while §V A says "DESI 2024 DR1." Already covered in M19 but the inconsistent labeling crops up multiple times in the body — at least three different DESI release names are used in the same paper.

### P1B-N7 — Convergence threshold stated as both 10⁻² and 3×10⁻³
**§VII vs Table I footnote.** §VII says "below the standard R̂−1<10⁻² publication target." Table I demands "R̂−1<3×10⁻³." Both are common but pick one as "standard" for this paper and stick to it.

### P1B-N8 — Spectator-ALP m vs fiducial m inconsistency in body
**Page 7, between Eq. 2 and Eq. 3.** Eq. 2 stated at m = H0; Eq. 3 stated at m ≈ 2H0; "fiducial" defined at m ≈ 1.8H0. Three different m values within a one-paragraph derivation. (Related to M1 but adds Eq. 2's m = H0 as a third value.)

---

## Summary of new findings

The most consequential additions are P1B-E9 (the Table II pivot footnote is *mathematically impossible*, not just algebraically wrong as flagged in E2) and P1B-M19 (a real dataset-version mismatch between the methods section's DESI DR1 and the headline Table II's DESI DR2, which the reader cannot reconcile from the paper as written). The bibliographic hygiene issues (P1B-E10) and unsupported numerical headlines (P1B-M14, the unsourced 2.4σ lower bound) are individually minor but collectively indicate the manuscript was not given a final synchronization pass before submission.

My overall recommendation (REJECT) is unchanged and is strengthened by these additional findings, particularly P1B-E9 (mathematical impossibility in a load-bearing table footnote) and P1B-M19 (dataset-version inconsistency in the headline analysis).