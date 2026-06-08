# P1B auto-2026-06-08_1354pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11857 chars)
**Wall time**: 51.3s

---

I cannot complete the requested citation-forensics audit to the standard you asked for from the text alone, because I do **not** have actual web search access in this chat and I cannot verify arXiv/ADS records or page images beyond the pasted manuscript text. I can, however, give a **text-based referee report** on internal consistency, unsupported claims, and bibliographic red flags visible in the manuscript itself.

The paper contains several **major and essential** problems on the face of the text: the bibliography has multiple entries that are clearly **in preparation** rather than citable published work; several load-bearing numerical claims are presented without enough derivation; the manuscript repeatedly blurs the line between a stock ΛCDM+ΔNeff proxy and claims about the ECH theory itself; and some statistical statements are not properly qualified as non-comparable. Below is a complete audit based only on the provided text.

- **P1B-E1** — **Abstract / Sec. III / Sec. V / Sec. VI** — The paper repeatedly attributes stock-CAMB **ΛCDM+ΔNeff** results to the ECH spin-torsion program, while also stating that the proxy “carries no torsion modifications” and “does not verify the spin-torsion theory module itself.” The offending text includes: “reported as a null-consistency test … for the ECH spin-torsion framework” and “current data neither require nor exclude a small positive ΔNeff from the spin-torsion sector.” The required fix is to remove all theory-validation language tied to the proxy run, or explicitly reframe it as a generic ΛCDM extension analysis with *no direct evidentiary weight* for ECH.

- **P1B-E2** — **Abstract / Sec. IV / Sec. VI** — The birefringence section mixes three different quantities as though they were interchangeable: published sky measurements, inverse-variance combinations, and pipeline-recovery injections. The manuscript states “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ,” then later gives an auxiliary combined value “3.9σ,” and elsewhere quotes “3.6σ.” These are **not directly comparable**, and the text does not always mark every juxtaposition as such. This is an **essential** fix under your own instruction: every side-by-side sigma comparison from different null procedures or different data combinations must be explicitly qualified as *not directly comparable*.

- **P1B-E3** — **Abstract / Sec. VI / Table III** — The abstract claims “the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ)” and then uses it as a “spectator-ALP consistency check.” But the manuscript itself later says the model-independent fit is **βfree = 0.344° ± 0.096°**, while the ALP-model fit gives **βALP = 0.336° ± 0.107°**. The abstract does not clearly distinguish which number comes from which fit, and it overstates the theorem-like status of a model-independence check. Required fix: separate the **published observational constraint** from the **paper’s own internal ALP fit**, and state plainly that the paper reproduces consistency, not a new detection.

- **P1B-E4** — **Sec. III / Table I** — The paper gives two different H0 values for the “full-tension” dataset: the abstract says **67.68 ± 1.06**, while later text says **67.69 ± 1.06**. That difference is small but nontrivial in a paper that is hyper-focused on quoted precision. Required fix: use one value consistently throughout and explain whether the difference is due to rounding or different posterior summaries.

- **P1B-E5** — **Sec. III / Table II** — The manuscript reports a **w0 wa** posterior with **w0 = −0.8122 ± 0.0436**, **wa = −0.6666 ± 0.1864**, and **w0 + wa = −1.4788 ± 0.1485**, then calls this the “canonical quintom signature.” This is a strong interpretive claim for a posterior summary, not a theorem. The required fix is to downgrade the language: this is an empirical posterior preference within a chosen likelihood stack, not a proof of quintom physics.

- **P1B-E6** — **Sec. III / Table II** — The text says “the LCDM point (w0, wa)=(-1,0) lies at > 4σ in the joint marginal tails and is therefore unsampled by the Metropolis-Hastings chain.” This is used to justify a refusal to report Bayes factors. But “>4σ in the tails” does **not** by itself prove that a Savage-Dickey estimate is invalid; it only means the estimate may be unstable. Required fix: either provide a controlled evidence calculation or present a more technically correct reason that the chain does not sample the nested point densely enough for a reliable density ratio.

- **P1B-E7** — **Sec. III / footnote 1 and Table I** — The manuscript states 309,189 frozen samples across two chains, with 176,240 and 132,949 raw accepted samples, but the burn-in arithmetic is not exact: 70% of the chains gives approximately 216,432 post-burn-in samples, yet the text later says the full-tension subset post-burn-in is **123,129**, which is “within ±1%” of **123,368 exact computation**. This is numerically sloppy for a methods paper. Required fix: present exact integer counts from the sampler output and avoid approximate arithmetic when discussing chain lengths and effective sample size.

- **P1B-M1** — **Sec. III / Table I** — The paper says the full-tension combination includes the SH0ES prior, but then claims H0 is still Planck-dominated because of inverse-variance weight. That is plausible, but the paper should show the actual likelihood weights or posterior decomposition if it wants this claim to be load-bearing. Required fix: add a quantitative decomposition or remove the “Planck-dominated” causal explanation.

- **P1B-M2** — **Sec. III / Table I** — The text claims “the canonical 3.6σ Hubble tension” and later equates this with a **0.155 mag offset** in MB and “exactly” the same tension in the MB axis. That “exactly” is not justified by the displayed numbers. A 0.155 mag shift divided by σMB = 0.049 gives about **3.16σ**, not 3.6σ. Required fix: either compute the equivalence correctly with the full covariance structure, or stop claiming exact equality between the MB-axis offset and the H0 tension.

- **P1B-E8** — **Sec. III / Table I** — The paper states “A robust ln B recompute therefore requires dedicated nested sampling … or thermodynamic integration” and later “the Model-comparison statistics paragraph” is deferred. That is fine, but the paper still uses the posterior as if it supports model selection claims. Required fix: ensure no model-selection language remains unsupported by evidence calculations.

- **P1B-M3** — **Sec. IV** — The pseudo-\(C_\ell\) validation uses Commander Q/U maps at **Nside = 2048** but then says the map is “foreground-cleaned CMB-only product; no separate foreground component is included.” If the goal is a pipeline validation, that is acceptable; if the goal is a sky birefringence measurement, it is insufficient. The manuscript mostly acknowledges this, but the distinction should be stated more prominently in the section heading and caption. Required fix: make the validation-only nature explicit in the figure caption and first paragraph.

- **P1B-M4** — **Sec. IV** — The paper states that the “primary observational evidence for cosmic birefringence remains the published Planck/ACT DR6 2.4–2.9σ measurements,” but then derives a combined inverse-variance result of **3.9σ** and later highlights **9σ** LiteBIRD forecast significance. These different significances mix data, forecast, and internal cross-checks. Required fix: separate observed, auxiliary-combined, and forecast sigmas in distinct sentences and do not let them bleed into each other.

- **P1B-M5** — **Sec. IV / Eq. (1)** — The pipeline-recovery values are presented as **β̂NaMaster = 0.238°** and **SNR = 20.32** for injected **β = 0.27°**, but the paper does not state the exact uncertainty used to obtain the SNR or how the bias correction was computed. Required fix: provide the underlying variance and the formula for SNR and bias.

- **P1B-E9** — **Sec. VI / Eq. (2)–(4)** — The ALP evolution and birefringence estimates are under-justified. The paper asserts \(\Delta\phi/f_a \approx 0.65\) for \(m = H_0, \theta_i = 1\), then uses that to claim \(\beta \approx 0.29^\circ\) for \(C_{a\gamma}=8\). The paper gives no derivation of the numerical factor 1.07 in Eq. (3). Required fix: show the actual numerical integration and parameter mapping, or place these values in a supplemental derivation.

- **P1B-M6** — **Sec. VI** — The manuscript says the prediction spans **β ≈ 0.17–0.43°** over \(C_{a\gamma}\in[4,12]\), \(m/H_0\in[1,3]\), \(\theta_i\in[0.5,2]\), and then says the “spectator-consistent corner” \(\theta_i \sim 0.1\) requires ~25× tuning relative to the prior midpoint. Those statements are in tension: one range is used for the scan, another for the physically permitted spectator regime. Required fix: clearly separate *scan range*, *physically allowed subrange*, and *posterior-weighted region*.

- **P1B-E10** — **Sec. VI / Appendix C** — The paper reports **9,720 total accepted samples across 3 configurations** for the ALP-MCMC and calls this “convergence” with \( \hat R - 1 < 0.01\). That is a weak basis for a quantitative parameter claim if the posterior is multimodal or if the scan includes only three fixed \(C_{a\gamma}\) values. Required fix: report effective sample sizes, autocorrelation lengths, and whether the posterior is sensitive to the discrete coupling choices.

- **P1B-M7** — **Sec. VI / Appendix C** — The model-independent fit uses a prior \(\beta \in [-2^\circ, 2^\circ]\), but the paper does not show whether the posterior is prior-limited near the boundaries. Required fix: provide posterior edge diagnostics.

- **P1B-M8** — **Sec. VI** — The paper claims “the same prediction \(\beta \approx 0.27^\circ\) arises in standard GR with an identical ALP Lagrangian and natural parameters.” This is fine as physics, but it is not a distinctive ECH output. The manuscript already says this, but the abstract still risks implying ECH relevance. Required fix: remove any remaining wording that suggests the ALP result supports ECH specifically.

- **P1B-M9** — **Sec. V / Table II** — The table reports **\(\chi^2_{\text{total}} = 14037.4 \pm 5.6\)** and the three channel contributions **10.6**, **10983.9**, **3043.0**, then claims the sum differs by **0.1** only because of rounding. That arithmetic is consistent at the displayed precision, but the uncertainty \(\pm 5.6\) on \(\chi^2\) is unusual and requires explanation. Required fix: clarify whether these are weighted-sample dispersions, standard errors, or posterior spreads.

- **P1B-M10** — **Sec. V / Table II** — The paper says “w0 departs by +4.3σ and wa departs by −3.6σ” while also noting that these are “marginal-tail posterior-extrapolation departures,” not frequentist tensions. This is technically acceptable only if the distinction is repeated every time the sigma numbers appear. Required fix: label all such sigmas as posterior-tail distances wherever they are mentioned.

- **P1B-E11** — **References [1], [4], [5], [6], ** — These are all listed as **“in preparation”** or otherwise unpublished companion papers. In a PRD submission, heavy reliance on unpublished internal manuscripts is a major bibliographic weakness unless those materials are publicly accessible and stable. Required fix: either replace them with published sources, preprints with archival identifiers, or make the companion manuscripts fully available and citable.

- **P1B-E12** — **References [1], ** — The reference list contains internal-bookkeeping prose inside the citations themselves, e.g. “ … canonical quintom-cosmology review … Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers.” That is not bibliographic style; it is manuscript bookkeeping. Required fix: strip all explanatory prose from the reference list.

- **P1B-M11** — **Reference [3]** — The citation is rendered as “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” Without external verification I cannot confirm the title/ID, but the paper itself uses this citation to support ACT DR6 birefringence numbers. Required fix: verify that the arXiv ID, title, and claimed statistics match the preprint and, if the work is not actually published, cite it as a preprint only.

- **P1B-M12** — **Reference ** — The manuscript cites “DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738.” Without web verification I cannot validate the journal issue/year from the text alone, but the volume/year pairing is unusual enough that it must be checked. Required fix: verify the final journal metadata and arXiv match.

- **P1B-M13** — **Reference ** — The text says this paper “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4),” while elsewhere the manuscript quotes **β = 0.30° ± 0.11°** and uses it in an inverse-variance combination. Required fix: ensure the citation’s exact published number, dataset, and rounding match the original paper.

- **P1B-M14** — **Reference ** — The paper cites DES Y3 cosmological constraints with a 2022 PRD article and uses it in a 2026 analysis. That is likely acceptable, but the manuscript elsewhere references **DES-Y5** and **DES-SN5YR** interchangeably. Required fix: standardize the survey nomenclature and make sure the citation supports the specific data release actually used.

- **P1B-M15** — **Sec. I / Abstract / Sec. VII** — The manuscript claims “14 independent structural constraints,” “13 logically-independent structural barriers,” “perturbation-transparency theorem,” and “surviving matter-bounce-specific test predictions” without providing those items in this paper. If these are supposed to be in Paper I(a), the present manuscript should not present them as if they are established here. Required fix: consistently attribute all such claims to the companion paper and avoid restating them as part of this paper’s own results.

- **P1B-N1** — **Abstract / Sec. VI** — The text contains dense reviewer-facing meta-language embedded in the prose, including phrases like “published PR3+WMAP9,” “repository README is the authoritative source,” and repeated parenthetical clarifications that belong in a data appendix, not the scientific narrative. Required fix: move implementation metadata to an appendix or supplement.

- **P1B-N2** — **Throughout** — The manuscript repeatedly uses parenthetical self-corrections such as “earlier count erroneously quoted,” “initially characterized as strictly stable,” and “correcting the earlier Caγ θi product.” This is honest, but it reads like revision history inside the body. Required fix: consolidate all errata into a short “Corrections relative to earlier draft” note in an appendix, not the main text.

- **P1B-N3** — **Throughout** — There is inconsistent notation and capitalization: ΛCDM, LCDM, Planck/PR4, PR4/NPIPE, Planck NPIPE, DES-Y5/DES-SN5YR, \(H_0.\mathrm{riess2020Mb}\), and \(Mb\) are used in mixed forms. Required fix: standardize notation and survey naming throughout.

- **P1B-N4** — **Sec. IV / Fig. 1 caption** — The caption says “Full-tension MCMC corner plot (119,617 post-burnin samples, getdist-thinned from 176,240 raw)” but the body explains that thinning is on the full-tension chain only, while the dataset combo includes two frozen chains. Required fix: state explicitly which chain the figure uses and how the thinning was performed.

- **P1B-N5** — **Table I** — The note says “Worst R̂ − 1 = 9.74 × 10−4; all 17 sampled parameters … satisfy R̂ − 1 < 3 × 10−3.” This is consistent internally, but the claim that the third Planck-only chain is “not aggregated into any frozen-posterior summary statistic” should be repeated in the table note if the table includes “Chains = 6” and “Total samples” only for the frozen subsets. Required fix: make the sample accounting unambiguous.

- **P1B-N6** — **References [7], , , ** — The paper uses some survey and supernova dataset names in forms that may not match the cited papers exactly, especially “DES-SN5YR” vs “DES-Y5” and “Pantheon+.” Because I cannot web-verify from the provided text alone, this must be checked against the source papers. Required fix: standardize the dataset labels to those used in the cited works.

## Summary recommendation
**REJECT**

The manuscript is internally detailed, but it does not meet PRD-level rigor in its current form. The biggest problems are not cosmetic: it repeatedly blurs proxy calculations with theory validation, mixes non-comparable sigma significances without consistent qualification, relies on unpublished “in preparation” references for core context, and presents several numerically delicate claims without sufficient derivation or unambiguous accounting. A publication at this level needs a much cleaner separation between what is measured, what is reproduced, what is merely consistent, and what is conjectural.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E13 — **Arithmetic / significance mismatch (MB-axis vs H0 tension)**  
Location: Sec. III (“MB–H0 joint-posterior offset check”)  
Issue class: A (ARITHMETIC), H (UNQUANTIFIED HEDGES)  

The text states that the 0.155 mag offset “corresponds exactly to the canonical 3.6σ Hubble tension manifesting in the MB axis,” but the only uncertainty actually quoted in the paragraph is the marginal MB width σMB = 0.049, which gives 0.155/0.049 ≈ 3.16σ, not 3.6σ. The text appeals to an “exact” equality that is not demonstrated from the displayed numbers, and no covariance-based computation is shown. Required fix: either (i) show the full 2D covariance calculation that yields a 3.6σ displacement in the joint (MB,H0) space, or (ii) explicitly downgrade the claim to “≈3.2σ in MB alone, broadly consistent with the 3.6σ H0 tension,” without using the word “exactly.”  

---

P1B-E14 — **Arithmetic: DESI-DR2 χ² decomposition vs. tension wording**  
Location: Table II, Sec. III (“Caveats”; DESI DR2 w0wa chain)  
Issue class: A (ARITHMETIC), H  

Table II quotes  
- χ²total = 14037.4 ± 5.6,  
- χ²BAO = 10.6 ± 1.8, χ²CMB = 10983.9 ± 5.3, χ²SN = 3043.0 ± 1.6,  
and the note says the sum of the means differs from χ²total by only 0.1 “rounding artifact.” Numerically, 10.6 + 10983.9 + 3043.0 = 14037.5, so the 0.1 difference is fine; but the ±5.6 uncertainty on χ²total is never defined. In the conclusions, this χ² decomposition is implicitly used as if it were an ordinary goodness-of-fit check, but the ±5.6 is not identified as a posterior dispersion, a standard error, or something else. Required fix: state explicitly what the ±σ on χ²total and each component represent (e.g. posterior-weighted dispersion of χ² across samples), and clarify that no p‑values or formal “good fit / poor fit” judgments are being derived from these numbers.  

---

P1B-E15 — **Arithmetic: NaMaster bias statement vs. quoted numbers**  
Location: Sec. IV (“Independent verification”), Eq. (1) paragraph  
Issue class: A  

The text first says the bias at β = 0.27° is 0.032°, and that it was “initially characterized as strictly ‘stable across all three injections’ at 0.032°,” but then reports that the β = 0.342° injection gives 0.302°, i.e. a 0.040° bias, and calls this a “∼12% amplitude-dependent component.” In fact, 0.040/0.032 − 1 ≈ 0.25: the relative difference is ~25%, not ~12%. Required fix: correct the quoted percentage (to ~25%) or explicitly define what ratio is being used; as written, the numerical percentage is inconsistent with the displayed biases.  

---

P1B-E16 — **Arithmetic: ALP parameter envelope and β-range**  
Location: Sec. VI, around Eq. (3) and the “prediction spans β ≈ 0.17–0.43°” sentence  
Issue class: A, C (implied unit/normalization), H  

The paper states that:  
- the observed β = 0.342° implies Caγ∆ϕ/fa ≈ 10.3,  
- the numerical integration gives ∆ϕ/fa ∈ [0.2, 1.1] for m/H0 ∈ [1,3], θi ∈ [0.5,2],  
- the prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4,12], m/H0 ∈ [1,3], θi ∈ [0.5,2].  

However, plugging the extremes of the *stated* ranges into β ≈ (αEM/4π) Caγ (∆ϕ/fa) × 1.07 (Eq. (3)) gives a much wider naive envelope:  
- minimum: Caγ = 4, ∆ϕ/fa = 0.2 ⇒ Caγ∆ϕ/fa = 0.8, which yields β ≈ (αEM/4π)×0.8×1.07 ≈ 0.027°,  
- maximum: Caγ = 12, ∆ϕ/fa = 1.1 ⇒ Caγ∆ϕ/fa = 13.2 ⇒ β ≈ 0.44°.  

The manuscript notes that the 0.17–0.43° range is “obtained from a joint-trajectory scan … and not from an independent-extremes product,” but it never shows any constraint that would exclude the β ≈ 0.03–0.16° portion of the naive range. That means the quoted 0.17° lower bound is not derivable from the stated parameter intervals alone. Required fix: either (i) explicitly describe the additional constraints or trajectory correlations that eliminate β < 0.17° from the scan, e.g. by showing a Caγ–∆ϕ/fa scatter plot or a minimal β over the scan, or (ii) expand the β-range to include the full reachable envelope implied by the parameter ranges, and distinguish that from any *prior-weighted* or “typical” range.  

---

P1B-E17 — **Dimensional clarity: Eq. (2) / Eq. (3) normalization and units**  
Location: Sec. VI, Equations (2)–(3)  
Issue class: C (EQUATION DIMENSIONAL CONSISTENCY)  

Equation (2) specifies ∆ϕ/fa ≈ 0.65 for m = H0, θi = 1, and Eq. (3) uses β ≈ (αEM/4π)×8×1.07 ≈ 0.29° with no explicit appearance of ∆ϕ/fa in the displayed equation, although the text then mentions “the fiducial value … corresponds to the midpoint m ≈ 1.8H0, ∆ϕ/fa ≈ 1.0.” As written, Eq. (3) looks like a pure number independent of ∆ϕ/fa, which obscures the dependence and dimensionless structure (β ∝ Caγ∆ϕ/fa). Required fix: rewrite Eq. (3) in the explicit form  
β ≈ (αEM/4π) Caγ (∆ϕ/fa) × 1.07,  
then specify the fiducial values of Caγ and ∆ϕ/fa used to obtain 0.29°, so that the units and parameter dependence are transparent.  

---

P1B-E18 — **Abstract vs body: “first precision test” language**  
Location: Abstract last sentence of analysis (also echoed in Conclusions: “CMB-S4 … will provide the first precision test”)  
Issue class: F (ABSTRACT FAITHFULNESS), G (UNSUPPORTED NOVELTY)  

The abstract/conclusion says: “CMB-S4 (σ(Neff) ∼ 0.03) will provide the first precision test” of a spin-torsion ∆Neff contribution. The body never provides a quantitative comparison of current Neff constraints vs CMB‑S4 forecasts, nor does it justify “first precision test” relative to other Stage‑4 surveys or existing Neff limits (Planck, ACT, SPT). Without such a comparison, “first precision test” is an unsupported novelty claim. Required fix: either (i) add a brief quantitative comparison (e.g., current σ(Neff) ~ 0.17 from Table I vs CMB‑S4 forecast σ(Neff) ~ 0.03, with clear reference that this is the first **precision** test specifically of the *spin‑torsion proxy* in this framework), or (ii) replace “first precision test” with a neutral forecast description such as “a significantly more precise test.”  

---

P1B-E19 — **Null-procedure comparability: σ-language around 20.32 / 25.71 / 2.4–2.9σ**  
Location: Abstract; Sec. IV (“Scope note”, “Independent verification”); Sec. VII conclusions  
Issue class: E (NULL PROCEDURE COMPARABILITY)  

The paper has improved its language compared to the earlier draft, but a few juxtapositions remain that can still mislead a casual reader:  

- The Introduction and Sec. IV say “The high pipeline-recovery SNR figures (e.g., 20.32, 25.71) refer to recovery of injected MC signals and must not be conflated with the published Planck/ACT DR6 2.4–2.9σ sky detection.”  
- Later, Sec. VII summarizes again: “SNR consistent with the ACT-noise floor,” next to “primary observational evidence … remains the published 2.4–2.9σ measurements.”  

While each sentence individually warns the reader, the numerical values 20.32, 25.71, 2.4–2.9σ, 3.9σ are repeatedly quoted in close proximity without a consistent, explicit “not directly comparable” marker every time they appear together, especially when the 3.9σ combined value is described as an “auxiliary cross-check.” Required fix: wherever numerical significances from different null procedures are juxtaposed (20.32/25.71 vs 2.4–2.9σ vs 3.9σ vs 3.6σ), add a short parenthetical such as “(from a different null test; not directly comparable)” to enforce the non-comparability, or reorganize the text so sky-detection sigmas and pipeline SNRs are never placed in the same sentence or bullet.  

---

P1B-N7 — **Figure–body mismatch: Nside and dataset description**  
Location: Abstract; Sec. IV “Pipeline configuration”; Fig. 1 caption (corner plot); top of Sec. IV body  
Issue class: B (FIGURE-CAPTION VS BODY-CLAIM), J (STALE NUMBERS)  

The abstract says the NaMaster validation uses “Planck Commander CMB polarization map (Nside = 512, ℓmax = 1024, fsky = 0.32, 500 Monte Carlo realizations),” but Sec. IV clarifies that the Commander Q/U maps are “provided at Nside = 2048” and then “we degrade to Nside = 512” for the analysis. The abstract omits the 2048→512 degradation step and presents only the degraded Nside, while Sec. IV emphasizes the native resolution and then the downgrade. This is minor, but in a technical-verification companion the abstract should match the body in describing processing steps. Required fix: in the abstract, explicitly state “Commander maps at native Nside = 2048, degraded to Nside = 512 for NaMaster,” to match Sec. IV and avoid apparent inconsistency.  

---

P1B-N8 — **Cross-reference: ambiguous “§ Headline-result discussion” pointer**  
Location: Sec. III, caveats paragraph ending: “see § Headline-result discussion”  
Issue class: D (INTERNAL CROSS-REFERENCES)  

The phrase “see § Headline-result discussion” appears as if it is a labeled section, but there is no section or subsection with that exact title. The closest relevant text is Sec. V “Model-comparison statistics: deferred to a dedicated nested-sampling run” and the discussion in the Conclusions, but the cross-reference is ambiguous. Required fix: replace “§ Headline-result discussion” with a precise reference to the relevant section/subsection (e.g. “Sec. V B (Results)” or “Sec. VII (Conclusions)”), so that a reader following the cross-reference can actually locate the intended discussion.  

---

P1B-N9 — **Appendix vs main-text mismatch: ALP prior ranges and “spectator” wording**  
Location: Sec. VI, footnotes 4 & 5; Appendix C  
Issue class: I (APPENDIX VS MAIN-TEXT MISMATCH), H  

Sec. VI and footnotes 4–5 state that the ALP-MCMC prior on θi is [0.5, 2] for “envelope-completeness,” but that true “spectator-consistent” status requires θi ~ 0.1 outside this prior, implying a ~25× fine-tuning. Appendix C then lists θi : uniform [0.5, 2] as the sampled prior with no separate “spectator-prior” configuration, while Sec. VI repeatedly talks about the result as a “spectator-ALP” prediction. The appendices do not show (even at a summary level) how the θi ~ 0.1 “spectator” point is treated in the inference (e.g. via reweighting or a separate run). Required fix: clarify in Appendix C whether any MCMC is actually run with θi extended down to 0.1 or whether the “spectator-consistent” corner is only an extrapolated interpretation; if the latter, the main text should explicitly say the spectator constraint is not sampled in the main ALP chains and is an analytic backreaction condition applied after the fact.  

---

P1B-N10 — **Abstract faithfulness: “three analyses … support and contextualize” vs actual load-bearing role**  
Location: Abstract; Introduction “Scope of this paper” paragraph; Conclusions  
Issue class: F, H  

The abstract and introduction say the three analyses “support and contextualize” the structural-closure result of Paper I(a). In the body, however, the ΛCDM+ΔNeff proxy is explicitly framed as a generic radiation test “not a direct test of the spin-torsion sector,” the NaMaster run is purely a pipeline validation, and the ALP birefringence calculation is explicitly “not a distinctive ECH prediction.” The paper does not exhibit any direct logical linkage between these three numerical results and the 14-barrier theorem/proofs in Paper I(a); at best they show consistency with a broad bounce-class picture. Required fix: in the abstract and introduction, explicitly rephrase to “provide technical verification of numerical pipelines used in the broader ECH program” rather than “support” the structural closure result, unless a precise logical dependence (e.g. “the H0 posteriors used in barrier 7 come from Table I here”) is demonstrated with explicit cross-references.  

---

NO OTHER NEW FINDINGS  

Beyond the items above, the remaining σ‑values, percentages, and cross‑references in the provided text either (i) matched the adjacent numbers arithmetically, (ii) were already covered in your initial report, or (iii) were purely descriptive without quantitative implications.