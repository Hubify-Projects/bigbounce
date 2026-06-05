# P2 R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12050 chars)
**Wall time**: 310.6s

---

# Referee Report — P2: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overall assessment

This is a 6-page note that recycles a well-known model (Fujita et al. 2021, with the same parameter choices fa~MPl, m~H0) under the guise of "specific parameter identification." The author admits as much in §6. Beyond the (thin) novelty issue, the paper has multiple internal numerical inconsistencies that I can recompute directly from the displayed numbers: the headline prediction does not follow from the displayed equations, the Bayes factor uses a different dataset than the headline σ, the figure-1 numbers contradict the body equations, and the citations are partially misattributed. PRD cannot accept this as is.

---

## ESSENTIAL findings

### P2-E1 — The "natural" β ≈ 0.27° prediction does not follow from Eqs. (1)–(2) (page 2)

Equation (1) gives Δφ ≈ fa θi (1 − J0(1)) ≈ 0.24 fa θi for m/H0 ≈ 1. Substituting into Eq. (2):
  β = (C0/2fa) Δφ ≈ 0.12 C0 θi rad ≈ 6.9° × C0 θi.

For C0 ~ θi ~ 1 this predicts β ≈ 7°, *not* 0.27°. The next sentence in §2.2 then asserts "the cosmological field evolution gives Δφ/fa ~ 10⁻²" — but Eq. (1) gives Δφ/fa ~ 0.24. A factor of ~25 has been swapped silently. Either Eq. (1) is wrong, or the central naturalness argument requires C0 θi ≈ 0.04 — i.e. *not* O(1), and the entire "no fine-tuning" claim collapses.

**Fix:** Derive Δφ/fa numerically (the actual late-time slow-roll integral, not J0), display the integrand, and state explicitly what value of C0 θi is required to match β_obs. If it is ~0.04, withdraw the naturalness claim.

### P2-E2 — Bayes factor in Eq. (9) is computed from a different β than the headline (page 3)

ln B = 5.17 with flat prior β ∈ [0°, 1°]. Using the *combined* posterior (0.242 ± 0.061°, the headline 3.9σ result in Eq. 4), I get
  posterior density at β=0: (1/√(2π)/0.061) exp(−0.242²/(2·0.061²)) ≈ 2.5 × 10⁻³ deg⁻¹,
  BF = 1/2.5×10⁻³ = 400, ln B ≈ 6.0.
Using instead β = 0.342 ± 0.094° (the Eskilt joint value used elsewhere) reproduces ln B = 5.18 exactly, and the [0,2°] and [0,0.5°] variants reproduce 4.48 and 5.87. The Bayes factor therefore uses the *single Eskilt measurement*, not the "combined" likelihood the paper presents as the headline result. This is a methodological inconsistency — the headline σ and the headline Bayes factor cannot both refer to "the data."

**Fix:** Either redo the Savage–Dickey at the combined posterior, or move the 3.9σ headline to a secondary status.

### P2-E3 — Figure 1 disagrees with Eq. (8) by a factor ~5 (page 4)

Figure 1 marginals (visible in the triangle plot, Run 2, C free): θi = 1.33₋₁.₁⁺⁰·⁴⁴, Caγ = 13.4₋₁₁⁺⁵·⁶. The product of medians is 1.33 × 13.4 ≈ 17.8, but Eq. (8) reports Caγ × θi = 3.4 ± 1.1. These are inconsistent by a factor ~5. Additionally, Figure 1 displays β = 0.324 ± 0.099°, but the body never reports this value — Eq. (6) is 0.336 ± 0.107° (Run 1), Eq. (7) is 0.344 ± 0.096° (Run 3). No equation in the body matches the figure.

**Fix:** Reconcile the figure marginals with the equations. If the product 3.4 is the *posterior mean of the product* (which can differ from the product of marginals under strong banana degeneracy), state this explicitly.

### P2-E4 — Misattribution of cited measurements (pages 2 and 6)

§3.1 cites "Eskilt and Komatsu, 2022" for β = 0.30 ± 0.11°, and the abstract attributes β = 0.342 ± 0.094° to an "Eskilt et al. joint Planck + ACT analysis." Both are wrong:
- 0.30 ± 0.11° is from Eskilt (2022, single-author, Planck PR4/NPIPE), not Eskilt & Komatsu.
- 0.342 ± 0.094° is from Eskilt et al. (2023) joint *WMAP + Planck* (not Planck + ACT). ACT DR6 was added separately by Diego-Palazuelos et al.

**Fix:** Correct the abstract's "joint Planck + ACT" phrasing and the citation keys.

### P2-E5 — Quantity "f_photon × C0 = 1.73 ± 0.44" is undefined (page 2, Eq. 5; abstract)

f_photon never appears in the model Section §2 and is not defined anywhere in the paper. The reader cannot evaluate "order-unity, no fine-tuning" without a definition. Numerically, 1.73 = 0.242°/0.14°, suggesting it is a ratio of the observed angle to some reference; but no reference is shown.

**Fix:** Define f_photon in §2, give the formula relating it to β, and show how 1.73 is obtained.

### P2-E6 — LiteBIRD 9σ forecast is double-counted and inconsistent with the data (page 3, Eq. 10)

The 9σ figure assumes β = 0.27° (the theory prediction) divided by σ(β) = 0.03°. But the combined *measurement* is 0.242 ± 0.061° — at face value LiteBIRD would forecast 0.242/0.03 ≈ 8σ, with a non-negligible probability of β being lower if calibration systematics absorb some of the present signal. Calling it "9σ — either decisive confirmation or clean exclusion" misrepresents the forecast as falsifiability when in reality, given the current data uncertainty alone, the credible range is roughly 5–10σ.

**Fix:** Forecast as a posterior-predictive distribution propagating σ(β_current), not a point estimate.

### P2-E7 — Citations to unpublished and "in preparation" works as load-bearing references (page 5–6)

- Diego-Palazuelos & Komatsu (2025): "arXiv preprint" with no arXiv ID. The value β = 0.215 ± 0.074° drives the combined 3.9σ headline. Untraceable.
- Namikawa, Murai & Naokawa (2025): explicitly labeled "In preparation".
- Golden 2026a, 2026b: "Companion paper, submitted simultaneously" — these are not published and the connection to "ECH gravity" / "14-barrier catalog" and "matter bounce" is not assessable.

A PRD paper cannot have its central data input traced only to an unidentifiable preprint and an "in preparation" reference. **Fix:** Provide DOIs / arXiv numbers, or remove dependence.

---

## MAJOR findings

### P2-M1 — Independence assumption in Eq. (3) is not justified (page 2)

Both Planck NPIPE (Eskilt 2022) and the joint Eskilt+Komatsu analysis use Planck data; the combination treats them as independent. ACT DR6 and Planck both observe overlapping sky and may share residual foreground systematics. The paper provides no estimate of the systematic covariance. The headline 3.9σ is therefore overstated.

### P2-M2 — Novelty claim contradicts admission in §6 (page 5)

The abstract advertises "predictions and constraints," but §6 admits Fujita et al. (2021) "already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°." The only stated novelty is "specific parameter identification (fa ~ MPl, m ~ H0)" — which is exactly Fujita's choice. PRD requires a genuine increment. The Bayes factor + LiteBIRD forecast does not constitute a methodological contribution at PRD level.

### P2-M3 — MCMC sample sizes are self-admittedly inadequate (page 3)

The author concedes 720–6,840 accepted samples (Neff ~ 1,000) "limit the precision of tail estimates and evidence calculations." Then the paper still reports a Bayes factor to two decimal places (ln B = 5.17). This is incoherent: either run longer chains before publication, or do not report the Bayes factor as a numerical headline.

### P2-M4 — "Indicative" Bayes factor with prior dependence ±0.7 nat (page 3)

Going from [0°,2°] to [0°,0.5°] swings ln B by 1.4. Per Jeffreys' scale this is the entire difference between "moderate" and "very strong" evidence. Reporting any single number is misleading.

### P2-M5 — Calibration systematics dismissed in one paragraph (page 5)

§6 acknowledges that the Minami–Komatsu self-calibration is the load-bearing assumption and that residual 0.1°–0.3° systematics are actively debated. Then the abstract reports 3.9σ statistical-only with no systematic budget. The headline σ is not earned.

### P2-M6 — "βcombined = 0.242 ± 0.061° (3.9σ)" arithmetic — minor but flagged

Inverse-variance combination: w1 = 1/0.11², w2 = 1/0.074² gives β = 0.2416 and σ = 0.0614. Significance 0.2416/0.0614 = 3.94, which the paper rounds to 3.9σ. OK numerically, but should state explicitly that this is a Z-score, not a likelihood-ratio σ.

### P2-M7 — "Eskilt et al. joint Planck + ACT" appears in abstract; in §3.1 the same value is described as fitting "the full EB cross-spectrum" of a different combination

The abstract, §3.1, and §3.3 give three different descriptions of where 0.342 ± 0.094° came from. Pick one and use it consistently.

### P2-M8 — Heuristic ECH motivation is unsupported

§5: "no derivation connects the Holst action to a specific ALP potential or coupling." Then why is the link made at all? Either delete or supply the derivation.

---

## MINOR findings

### P2-m1 — Eq. (1): the formula Δφ ≈ fa θi (1 − J0(m/H0)/J0(0)) is not derived; J0(0)=1 is trivial; the Bessel form is for a *Minkowski* harmonic oscillator, not a Hubble-friction-dominated FRW field. The factor 0.24 is unjustified — the proper integral is over conformal time with H(z) varying through matter + Λ.

### P2-m2 — Eq. (2): factor of ½ in β = gaγ Δφ / 2 is correct for the line-of-sight integral, but should cite the standard Carroll/Field/Jackiw derivation.

### P2-m3 — Caption to Figure 1 says posterior on Caγ × θi is "centered at 3.4 ± 1.1, consistent with order-unity natural values." A product centered at 3.4 with 1σ width 1.1 is *not* O(1) — it is closer to ~3. Stop calling 3.4 "order unity."

### P2-m4 — Figure 2 caption: "All three are consistent with each other and with the observed value." Visual inspection shows they are nearly identical Gaussians shifted by ≲ 0.01° — i.e. the figure is essentially redundant with Eqs. (6)–(7).

### P2-m5 — Acknowledgments: "AI research assistants during the analysis and manuscript preparation." Welcome the disclosure, but please clarify scope: numerical analysis, equation derivation, or prose only? PRD will increasingly require this.

### P2-m6 — Page count: 6 pages is fine for the genuine content here — really only ~2 pages of original analysis. If the inconsistencies above are fixed, the paper still does not warrant more than a short paper / Letter, and arguably belongs in PRD Letters track or as a comment on Fujita et al.

### P2-m7 — Intro: "Combined, the evidence exceeds 3.5σ" — but the abstract claims 3.6σ. Be consistent.

### P2-m8 — Table 1: Run 3 "β free" is the model-independent fit. Why 720 samples when Run 2 has 6,840? No explanation.

---

## NIT findings

### P2-n1 — Eq. (4) and Eq. (10) display "deg" inconsistently; sometimes °, sometimes typeset as superscript ◦.

### P2-n2 — Reference "Diego-Palazuelos and Komatsu" is missing arXiv ID; reference "Namikawa et al." has no year of arxiv submission.

### P2-n3 — "ABJ anomaly" introduced without citation (Adler–Bell–Jackiw).

### P2-n4 — "fphoton × C0" in (5) is written with non-standard subscript; if you mean f_a × C0, write it; if not, define.

### P2-n5 — Equation (2) double-uses C0/(2fa) but then writes ≈ C0 θi /2 × O(1) — dimensionally the first form is rad, the second is unitless. Either Δφ/fa or the O(1) factor must carry the radian.

---

## Summary recommendation

**REJECT**

The paper recycles the Fujita et al. (2021) Planck-scale ALP scenario without a clearly new theoretical or methodological contribution, and the analysis as displayed is internally inconsistent at the load-bearing level: (i) the headline prediction β ≈ 0.27° does not follow from Eqs. (1)–(2) — it is off by ~×25 unless C0 θi ≈ 0.04, contradicting the "no fine-tuning" claim; (ii) the Bayes factor uses a different posterior than the headline 3.9σ result; (iii) Figure 1 marginals disagree with Eq. (8) by a factor ~5 and display a β value that appears nowhere in the body; (iv) data citations are misattributed (Eskilt single-author vs Eskilt et al.; "Planck + ACT" vs Planck + WMAP); (v) central input (ACT DR6 β) is cited only to an unidentifiable 2025 preprint; (vi) calibration systematics that could absorb the entire signal are acknowledged then ignored in the headline σ. This is not the standard for PRD. If the author wishes to resubmit, the paper must (a) honestly derive the prediction and quantify the required C0 θi, (b) demonstrate genuine novelty beyond Fujita et al., (c) reconcile every quoted number across abstract / equations / figure / Bayes factor, and (d) substantiate all cited data values with traceable references.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings — Fresh-Eyes Pass

## ESSENTIAL findings (new)

### P2-E8 — MCMC mass posterior **contradicts** the central naturalness claim "m ~ H₀" (page 4, Figure 1)

Figure 1 reports log₁₀(m_a/eV) = −31.4₋₁.₂⁺¹·⁴. The Hubble scale today, in eV, is ℏH₀ ≈ 1.44 × 10⁻³³ eV, i.e. log₁₀(H₀/eV) ≈ −32.84. The posterior median is therefore m/H₀ ≈ 10¹·⁴ ≈ **25**, with 1σ upper range pushing to m/H₀ ≈ 700.

This is **not** "m ~ H₀". The abstract, intro, §2.1, §2.2, and conclusion all rest on the premise that "m ~ H₀ ensures the field is rolling today." For m ≈ 25 H₀ matter-dominated H(z) = H₀(1+z)^{3/2} gives oscillation onset at 1+z ≈ 25^{2/3} ≈ 8.5, i.e. z ≈ 7.5 — the field has executed many oscillations between recombination and today and the slow-roll estimate Δφ ≈ fa θi (1 − J₀(m/H₀)) breaks down completely. J₀(25) oscillates around zero with amplitude ~0.16, so the prefactor in Eq. (1) is wildly different from 0.24.

The MCMC the paper itself reports therefore **falsifies the naturalness argument** the paper makes in prose. Either the chain is wrong, the mass prior is wrong (see P2-E10), or the prediction story is wrong.

**Fix:** Reconcile. Either restrict the prior to m ~ H₀ (and quote the resulting posterior), or honestly state that the preferred mass is ~30× larger than the natural value and explain how the model still produces β ≈ 0.27° in that regime.

### P2-E9 — Run 1 fixes C₀ = 8 (Table 1); Run 2 marginal posterior gives C_{aγ} = 13.4₋₁₁⁺⁵·⁶ — neither is "order unity"

Page 1: "C₀ ∼ 1". Page 2 Eq. (2): "C₀ is an order-unity coefficient from the ABJ anomaly." Page 2: "For C₀ ∼ 1, θ_i ∼ 1." Page 5 conclusion: "the anomaly coefficient C₀ and initial misalignment θ_i are model-dependent parameters of order unity."

But the actual analyses use:
- Run 1: C = **8 fixed** (Table 1) — never justified.
- Run 2: C_{aγ} marginal = **13.4** (Figure 1) — an order of magnitude away from 1.

If the analysis requires C₀ ≈ 8–13 to match the observed β, then the "no fine-tuning, all inputs O(1)" headline is incorrect. ABJ-anomaly coefficients can in principle be ~O(10) in specific UV completions, but the paper does not say so, and it does not allow itself the luxury of being inconsistent with its own naturalness rhetoric.

**Fix:** Either (i) justify why "C = 8" is the natural prior central value and rewrite the prose to admit C₀ ~ O(10); or (ii) redo the inference with C₀ prior peaked at 1 and report the resulting (worse) fit.

### P2-E10 — Mass prior is flat in log over 5 decades, biasing posterior far from the natural value (page 3)

The prior log₁₀(m/eV) ∈ [−35, −30] flat in log spans 5 orders of magnitude. The "natural" value log₁₀(H₀/eV) ≈ −32.84 sits near the middle, but a flat-log prior puts equal weight on m being 10⁻³⁵ eV vs 10⁻³⁰ eV. There is no penalty for the posterior wandering to m = 30 H₀ where it currently lies.

A natural-value prior should be peaked at log₁₀(H₀/eV) with width O(1 decade). Without this, the posterior cannot test naturalness — it only tests what mass is consistent with data given a prior that says naturalness doesn't matter.

**Fix:** Re-run with a naturalness-motivated prior. The current setup cannot be claimed to demonstrate "naturalness".

### P2-E11 — The MCMC posteriors (Figs. 1 & 2) use a *different* dataset than the headline 3.9σ combined result

Figure 2 shows three Gaussians of width ~0.10°, all centered near 0.33–0.34°. These widths are consistent with using only the single Eskilt input (σ = 0.094°), not the combined likelihood (σ = 0.061°). The headline "β = 0.242 ± 0.061° (3.9σ)" therefore has no counterpart in the MCMC analysis the paper actually performed.

This is the same structural issue as P2-E2 but applied to the figures: the paper is presenting two parallel analyses — a Gaussian summary likelihood combination (Eqs. 3, 4) and an MCMC on a single dataset (Eqs. 6–9 and Figs. 1–2) — and reporting them as if they were one. Figure 2 in particular should be re-done using the combined likelihood, or labeled clearly as "MCMC uses Eskilt point only."

### P2-E12 — "f_photon × C₀ = 1.73 ± 0.44" is numerically just β_combined / σ_MinamiKomatsu

I reverse-engineered Eq. (5): 0.242°/0.14° = 1.728 and 0.061°/0.14° = 0.436. **Match to three figures.** "f_photon × C₀" is being computed by dividing the combined measurement by the σ of the *Minami–Komatsu 2020 error bar*. This is not a physical coupling — it is the Z-score of the combined measurement relative to a stale measurement's *uncertainty*. There is no scenario in which dividing by an old paper's σ produces a "photon coupling parameter."

The "1.73 (order-unity, no fine-tuning)" claim in the abstract is therefore a numerical coincidence of arithmetic without physical content.

**Fix:** Either define f_photon physically (with formula and dimensional check) or delete Eq. (5) and the abstract sentence.

---

## MAJOR findings (new)

### P2-M9 — Five distinct β values circulated as if interchangeable

Across the paper:
- **0.27°** — theory prediction (§2.2, abstract, conclusion, used in LiteBIRD forecast Eq. 10)
- **0.242°** — combined NPIPE+ACT (Eq. 4, abstract headline 3.9σ)
- **0.342°** — Eskilt et al. joint (MCMC input, used in Bayes factor)
- **0.30°** — NPIPE single (Eskilt 2022)
- **0.215°** — ACT DR6 (Diego-Palazuelos)

The paper variously says "consistent with the observed signal" without specifying which observed signal, and the LiteBIRD forecast uses 0.27° (theory), not 0.242° (data) — see P2-E6. The "no tension between ALP and data" claim in §3.3 compares Eq. (6)'s 0.336° to βobs = 0.342°, but the abstract uses 0.242° as the data anchor. Pick **one** β as the data input and use it everywhere.

### P2-M10 — Naturalness prediction conversion is off by 6%

Page 2 §2.2: "C₀ θ_i × 5 × 10⁻³ rad ≈ 0.27°". Check: 5 × 10⁻³ rad × (180/π) = 0.2865°. The author has rounded 0.29° down to 0.27° to better match β_obs. Minor arithmetic slip, but it conveniently moves the prediction toward Eskilt's 0.342° rather than away from it. Stated precision is misleading.

### P2-M11 — Run 1 "C = 8 fixed" choice is unmotivated and tuned

Table 1 reports Run 1 with C = 8 fixed. The paper never explains why 8. Common ALP-photon coupling normalizations involve E/N ratios that are O(1) (e.g. KSVZ E/N = 0, DFSZ E/N = 8/3 ≈ 2.7). A value of 8 is not standard. If 8 was chosen to make the predicted β match data, this is post-hoc tuning, which directly contradicts the "no fine-tuning" headline.

### P2-M12 — Eq. (8) "C_{aγ} × θ_i = 3.4 ± 1.1" cannot be reconciled with Fig. 1 even with a banana degeneracy

Even under a strong inverse banana (θ_i × C_{aγ} = const), the product of marginals should equal the median of the product up to skew corrections. Going from product-of-medians 17.8 to median-of-product 3.4 is a factor 5+. This is not a normal banana degeneracy — it is either a different statistic (e.g. *mode* of the product) or a different chain. Specify which.

### P2-M13 — The 1σ upper range of Fig. 1's log₁₀(m/eV) posterior extends to −30.0 — the prior edge

Figure 1: log₁₀(m/eV) = −31.4₋₁.₂⁺¹·⁴. The +1.4 quantile reaches log₁₀(m/eV) = −30, which is the upper prior boundary (Sec 3.3: "log₁₀(m/eV) flat on [−35, −30]"). The posterior is **prior-rail-dominated** on the upper side. This means the data does not constrain the high-mass tail at all, and the quoted +1.4 uncertainty is a prior artifact, not a measurement.

---

## MINOR findings (new)

### P2-m9 — Figure 1 has *no* posterior for β shown labeled in body equations

Figure 1's diagonal panel shows β = 0.324 ± 0.099° (Run 2). The body equations report Run 1 (Eq. 6: 0.336 ± 0.107°) and Run 3 (Eq. 7: 0.344 ± 0.096°) but never Run 2's β posterior. The Run 2 β only appears in the figure caption.

### P2-m10 — Figure 2 visually shows posteriors centered near 0.34°, but no axes confirm the unit is degrees

The x-axis label is "β [deg]" — OK — but the "Observed" green band shown in the figure is the Eskilt 0.342° value, not the headline 0.242°. The figure visually anchors the reader on the wrong β.

### P2-m11 — "Effective sample size N_eff ~ 1,000" claim is hand-waved

§3.3 estimates N_eff ~ 1,000 from samples 720–6,840 without showing the autocorrelation calculation. For 3-parameter chains with banana degeneracies, N_eff can easily be < 100, even with R̂ − 1 < 0.01. R̂ is necessary but far from sufficient.

### P2-m12 — Run 1 sample count 2,160 vs Run 2 sample count 6,840: ratio 3.16, not obviously related to dimensionality

If Runs 1 and 2 share infrastructure and differ only by C being free vs fixed, the sample-count ratio should reflect either chain-length choices or thinning ratios. Neither is documented. Doesn't change the science but suggests inconsistent execution.

### P2-m13 — Run 3 ("β free", 720 samples) is the *baseline* for the Bayes factor but has the smallest chain

Bayes-factor estimation requires the densest sampling of the prior, not the sparsest. 720 samples for the null/free model is the worst possible choice for Savage–Dickey. Either run more, or use a closed-form prior density at β = 0 (which is trivially 1/prior_width = 1°⁻¹ for the [0°, 1°] prior — in which case lnB = ln[posterior_density(0)/prior_density(0)] = ln[1°/p(0|D)]).

### P2-m14 — log10(m/eV) prior [-35, -30] excludes m << H₀ ULA regime where the field is *frozen* today

If m < H₀, the field has not begun rolling. The prior is flat-log down to 10⁻³⁵ eV which is m/H₀ ≈ 10⁻²·²ish (still below H₀ by a factor 70). For most of the prior volume, the field is still frozen, Δφ ≈ 0, and β = 0. Yet the posterior places significant weight in this region. Either β is generated some other way in this regime (not described), or this prior region contributes only background to the marginalization. Document.

---

## NIT findings (new)

### P2-N6 — Page 1 intro says "3.5σ" but abstract says "3.6σ" — Minami-Komatsu / ACT combination significance is inconsistent between abstract and §1.

### P2-N7 — Eq. (1) writes "(1 − J₀(m/H₀)/J₀(0))" — J₀(0) = 1 trivially, so the denominator is decorative; just write (1 − J₀(m/H₀)).

### P2-N8 — Figure 1 caption: "centered at 3.4 ± 1.1, consistent with order-unity natural values" — 3.4 is not order unity by any standard reading.

### P2-N9 — Eq. (5) variable name "f_photon" never appears in §2 (model) or §4 (forecast). It is introduced only in §3.2 with no definition.

### P2-N10 — Page 5 §6 cites "matter-bounce non-Gaussianity f_NL = −35/8" with no derivation in this paper; refers to companion 2026b. The 35/8 fraction is mathematically specific (= 4.375) — should be cited to a published derivation, not "in preparation."

### P2-N11 — Conclusion says "9σ statistical significance, contingent on the self-calibration strategy and systematic error budget." If contingent on systematics, it is not a pure statistical forecast — it is conditional. Reword.

### P2-N12 — Eq. (6), (7), (8) all use ± notation but Figure 1 uses asymmetric ⁺/⁻ for upper/lower 1σ. Reconcile the convention.

---

## Summary of fresh-eyes additions

The most consequential additions are **P2-E8** (the MCMC mass posterior contradicts the m ~ H₀ naturalness story by a factor ~30), **P2-E9** (Run 1's C = 8 and Run 2's C_{aγ} = 13.4 are not "order unity"), **P2-E10** (the mass prior is flat-log over 5 decades, so the analysis cannot test naturalness even in principle), and **P2-E12** (the "effective photon coupling 1.73 ± 0.44" is numerically just the combined β divided by the *uncertainty* of the 2020 Minami–Komatsu measurement — a meaningless ratio).

Together with my initial findings, this brings the case to: the paper's central claim of "no fine-tuning, all inputs O(1)" is directly contradicted by the paper's own MCMC posteriors (P2-E8, E9) and by its own choice of fixed coupling C = 8 (P2-M11). The recommendation **REJECT** is reinforced; if a revised version is invited, the author must either (a) restrict the priors to the naturalness regime and accept whatever posterior follows, or (b) withdraw the naturalness claim entirely.