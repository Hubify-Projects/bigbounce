# P1B auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10613 chars)
**Wall time**: 494.2s

---

# Brutal-Honesty PRD Referee Report — P1B

**Paper:** "Technical Verification Companion to the ECH Spin-Torsion Program..."
**Reviewer disposition:** REJECT in present form. The paper, by its own explicit construction, verifies none of the load-bearing physics of the parent program; multiple headline quantities are not reproducible from the displayed inputs; the body contains review-log prose; and the central "spectator-ALP" analysis is performed on a prior box that the paper itself flags as inconsistent with spectator status.

---

## ESSENTIAL findings

### P1B-E1 — Title and Sec. VI are inconsistent with the prior actually sampled
**Page 7–11, Sec. VI + Appendix C + fn. 5/6.**
The paper's third headline result is a "spectator-ALP consistency check" (title, abstract). Footnote 5 (p. 7) and footnote 6 (p. 11) both state explicitly that spectator status (Ω_a ≪ 1) requires θ_i ∼ 0.1 (a "∼25× fine-tuning relative to the prior-midpoint θ_i = 0.5"). Yet the ALP-MCMC prior in Appendix C is uniform on θ_i ∈ [0.5, 2], i.e. the prior is entirely **outside** the spectator-consistent regime. The quoted β_ALP = 0.336° ± 0.107° therefore samples the **dark-energy ALP** posterior, which the paper itself "explicitly excludes from this spectator-consistency companion check." The title claim and Sec. VI headline are not supported by the actual MCMC.
**Required fix:** Either (a) re-run the MCMC with θ_i ∈ [0, 0.2] and report the result in that prior (which will not match β_obs without compensating C_aγ ≳ 50), or (b) retitle and rewrite Sec. VI as a "dark-energy ALP" consistency check, dropping "spectator" from the title and abstract.

### P1B-E2 — Arithmetic error in w_pivot uncertainty (Table II fn. b, p. 4)
The footnote claims
σ²_wpivot = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)².
Direct evaluation: (0.0436)² + (0.3320·0.1864)² is not what the prose says, but taking the formula as written,
(0.0436)² + (0.3320)²·(0.1864)² = 0.001901 + 0.110224·0.034745 = 0.005731,
√0.005731 = **0.0757**, not 0.0301. (0.0301)² = 0.000906, which is **less than** σ²_w0 = 0.001901 alone — impossible for a positive-definite linear combination unless w_0 and w_a are anti-correlated and a cross term is being subtracted, which the displayed formula does not contain. Either the displayed formula, the input numbers, or the quoted ±0.0301 is wrong. This is the **load-bearing** quantity behind the "−1.1σ from −1" headline.
**Required fix:** Recompute σ_wpivot from the full posterior covariance (must include the 2(1−a_p)Cov(w_0,w_a) cross term), display the actual covariance value, and correct the −1.1σ tension figure.

### P1B-E3 — Scope of the entire paper undermines its existence
**Sec. III headline + Sec. IV scope note + Sec. VI Note (pp. 2, 5, 7).**
The paper explicitly states:
- §III: stock-CAMB ΛCDM+∆N_eff "does NOT test the ECH spin-torsion sector directly" and "does not verify the spin-torsion theory module itself."
- §IV: NaMaster validation "is not a competitive sky detection" and does **not** separate β from miscalibration α.
- §VI: ALP birefringence "is not a distinctive ECH prediction" and "the same result arises in standard GR."

A "technical verification companion" that verifies none of its parent program's distinctive physics is not a PRD-grade contribution. The paper has no independent physics result; it is a methods cross-check whose null result is consistent with both ECH and ΛCDM.
**Required fix:** Either (a) demonstrate at least one calculation that is genuinely diagnostic of ECH (e.g. a torsion-modified Boltzmann code, an ECH-specific photon-torsion coupling derivation), or (b) withdraw the paper and merge the salvageable methods content into the parent paper as an appendix.

### P1B-E4 — Sample-count chaos cannot be reconciled to the abstract
The abstract states "309,189 frozen samples across two converged dataset combinations." Tracking through the paper:
- Table I: 176,240 + 132,949 = 309,189 raw ✓
- Footnote 1 (p. 2): 216,432 post-burnin total; full-tension post-burnin 123,368 (analytic) or 123,129 (actual); Fig 1 caption uses 119,617.
- **Fig. 2 caption (p. 5): "Full tension (175,545 samples)"** — does not match 176,240 in Table I, does not match 123,368/123,129/119,617 post-burnin. There is no reconciliation of 175,545 anywhere.
- Conclusions (p. 8) re-state 309,189 + a separate 114,992 Planck-only — fine but adds further numbers.

At minimum five mutually inconsistent sample counts appear for the same chains.
**Required fix:** A single sample-accounting table with raw / post-burnin / getdist-thinned / plotted columns for every figure and table, and a single agreed total in the abstract.

### P1B-E5 — Embedded review-log prose throughout the body
The body of a PRD paper must not contain response-to-referee language. Instances visible in the rendered PDF:
- p. 3 "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain..."
- p. 3 "(note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, w_a) marginal, but with zero free-w0wa samples..."
- p. 4 "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood..."
- p. 4 "A concern was raised that the joint posterior mean ... was inconsistent ... Direct arithmetic audit: ... NOT a YAML alias failure..."
- p. 6 "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°..."

This is internal version-history / review-log text, not paper text.
**Required fix:** Remove every instance. Present only the final values; do not narrate prior errors or reviewer exchanges.

### P1B-E6 — Side-by-side σ values from heterogeneous procedures without comparability disclaimer at each juxtaposition
- Abstract: "pipeline-recovery bias 0.032°" next to "Planck/ACT DR6 2.4–2.9σ" sky detection.
- §VI: "βALP = 0.336° ± 0.107°", "βfree = 0.344° ± 0.096°", "βobs = 0.342° ± 0.094°", and the auxiliary inverse-variance "3.9σ" — these mix (a) a model-dependent ALP posterior, (b) a model-independent posterior on the same data, (c) the published joint analysis, and (d) a naive inverse-variance combination that the paper itself states overestimates significance. The "not directly comparable" qualifier is needed at every juxtaposition; it is given inconsistently.
- §IV: "SNR^SE = 25.71" pipeline-recovery vs published 2.4–2.9σ — the per-realization SNR^real ≈ 1.15 is buried in fn. 3.

**Required fix:** Tag every σ-value side-by-side with its null procedure; remove SNR^SE = 25.71 and 20.32 from prose entirely (they are not detection significances and have no physical meaning for the reader).

---

## MAJOR findings

### P1B-M1 — Title misrepresents content
"Spectator-ALP Model" — see E1. Either remove or qualify.

### P1B-M2 — All four references to companion papers are "in preparation"
Refs. [1], [4], [5], [6] are all unpublished and unposted; Ref. [1] (Paper I(a)) is the parent paper this work depends on for its entire framing. PRD will not accept a paper whose theoretical foundation is a non-existent reference.
**Required fix:** Either post Paper I(a) to arXiv and cite that, or self-contain the necessary theory in this paper.

### P1B-M3 — Eskilt–Komatsu citation is internally tangled
The abstract footnote (a) discloses that the headline 3.6σ value comes from PR3+WMAP9 but the ALP-MCMC actually uses PR4/NPIPE code, then Appendix C says the likelihoods are "Planck PR4 + ACT DR6 EB-spectrum." So the "consistency with the published 3.6σ" is consistency between a model fit to PR4+ACT-DR6 and a published number from PR3+WMAP9 — not the same data. The 3.6σ figure should not be quoted as the comparison target without an apples-to-apples re-analysis.

### P1B-M4 — C_aγ ∈ [9, 51] is presented as "accommodating" but is far outside benchmarks
§VI states explicitly "Both ends are larger than the standard KSVZ/DFSZ benchmark range, which predicts |C_aγ| ∼ O(1); the entire required range therefore lies outside minimal ALP photon-coupling benchmarks." This is a quantitatively significant fine-tuning, not "natural parameters" (abstract). The abstract uses "natural" language that the body refutes.
**Required fix:** Remove "natural" framing from abstract and §VII; replace with explicit statement that C_aγ ≥ 9 is required and lies above KSVZ/DFSZ benchmarks.

### P1B-M5 — "WP4 reheating" / "WP4 decay" undefined in Fig. 2
Fig. 2 legend cites "WP4 reheating [0.05, 0.40]" and "WP4 decay [0.01, 0.25]" with no in-text definition of what WP4 is, no citation, no derivation of those ranges.

### P1B-M6 — "ACT DR6 central (0.40)" in Fig. 2
Fig. 2 panel (a) is the ∆N_eff posterior with a legend entry "ACT DR6 central (0.40)." No citation, no caveat that this is a different ACT analysis than the DR6 polarization analysis cited for β. Reader cannot trace this number.

### P1B-M7 — Model-comparison statistics deferred yet w0wa table presents +4.3σ tension
Sec. V.B and Table II claim "+4.3σ" departure of w_0 from −1, while the same section admits that the Bayes factor is "deferred to a follow-up nested-sampling analysis" because the ΛCDM point is unsampled. The "+4.3σ" is then footnoted as "marginal-tail posterior-extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension." That makes the +4.3σ number meaningless as a tension claim, yet it propagates into the §V.B "headline result" and §VII text without that qualifier.
**Required fix:** Remove "+4.3σ" and "−3.6σ" tension language from the headline; state only the posterior parameter values until a defensible model-comparison statistic exists.

### P1B-M8 — "Frozen" never defined
"Frozen samples", "frozen dataset combinations", "frozen chains", "frozen posterior" appear ∼20 times. The term has no standard meaning in the Cobaya/CosmoMC literature. Define once at first use, e.g. "chains satisfying R̂−1 < 3×10⁻³ and no longer extended."

### P1B-M9 — "Planck 2018 NPIPE" terminology error
Table II caption: "Planck 2018 NPIPE lowl.EE+TT+highl.CamSpec.TTTEEE+lensing.native." NPIPE is Planck PR4 (2020 reprocessing), not Planck 2018. The likelihood file names being "planck_2018_*" is a Cobaya convention, but the data is not "Planck 2018". This recurs throughout. Standard usage: "Planck NPIPE / PR4."

### P1B-M10 — Table III "Verified" status is meaningless
The MCMC entries are tagged "Verified" with note "Stock CAMB proxy" — but verified against what? They are self-reports of the chain output. There is no external verification. The "Lit. Cited" entry is correctly labeled. "Verified" should be "Reported" or "Internal MCMC output."

### P1B-M11 — Per-realization SNR not consistent with reported 2.7σ
Fn. 3 (p. 6) claims "SNR^real ≡ β̂/σ_β̂ = SNR^SE/√N ≈ 0.91" for the β = 0.27° injection and "≈ 1.15" for β = 0.342°. The text then says this is "the appropriate quantity for comparison to single-sky measurements such as Planck NPIPE β = 0.30° ± 0.11° at ∼2.7σ." 0.91 vs 2.7 is a factor of ∼3 mismatch. Either the MC noise level is wildly more pessimistic than Planck's effective per-mode noise (likely true: ACT-noise floor on a Planck Commander map is the wrong combination), or the pipeline-recovery validation is at a noise level so far from the real Planck measurement that it does not validate anything relevant. This should be discussed.

### P1B-M12 — Pipeline tests Commander, but Commander cannot break α–β degeneracy
The abstract correctly states that the foreground-cleaned Commander map "removes the very component that breaks the β–α degeneracy." But the validation is then performed on exactly that map. The exercise therefore validates the pseudo-C_ℓ mode-coupling deconvolution at fsky=0.32 with a 2° apodization — a generic NaMaster regression test that does not require ALP/birefringence physics at all. The paper should be honest that this is a NaMaster regression test, not even a birefringence-specific test.

### P1B-M13 — DESI w0wa chain χ² breakdown lacks degrees of freedom
Table II reports χ²_total = 14037.4 with no ν_eff, so no χ²/dof, no goodness-of-fit interpretation possible. For a paper claiming a quintom-B detection at the parameter-posterior level, the absolute fit quality must be stated.

### P1B-M14 — Fig. 3 axis and binning
Fig. 3 plots β̂ vs N_side with only four points (256, 512, 1024, 2048). The "Lead result" annotation appears to point at N_side = 1024, but the body text uses N_side = 512 as the production value (abstract). The figure shows the production N_side as not the lead. Reconcile.

---

## MINOR findings

### P1B-Min1 — PACS numbers
PACS was deprecated by the AIP in 2010; PRD uses PhySH. Replace.

### P1B-Min2 — "(km s⁻¹ Mpc⁻¹)" formatting
Abstract uses "km s⁻¹ Mpc⁻¹" but body Table II/text uses "km/s/Mpc." Standardize.

### P1B-Min3 — Duplicate / awkward phrasing
- p. 3 "the chain has τ free with the standard low-ℓ data constraint, not a Gaussian prior at the Planck best-fit" — appears twice in close succession.
- p. 5 "Beam and pixel window.—The Planck Commander Q/U maps are provided at N_side = 2048 ... we degrade to N_side = 512" — abstract says ℓ_max = 1024 was the configuration; degrading from 2048 to 512 with ℓ_max = 1024 over-samples; the pixel window correction at ℓ ∼ 1024 with N_side = 512 has 10–20% suppression. Confirm this is included.

### P1B-Min4 — Inconsistent number of significant figures
Table I gives ∆N_eff = +0.065 ± 0.17 (Planck+BAO+SN) — two sig figs on the mean and σ. Throughout body uses ±0.169 / ±0.17 inconsistently.

### P1B-Min5 — Fig. 1 caption "119,617 post-burnin samples, getdist-thinned from 176,240 raw"
123,368 → 119,617 is a 3% loss; getdist thinning by ESS is fine, but state the ESS used.

### P1B-Min6 — "2026-06-08 PDT" in title block
Date is fine; just note this is in the future relative to most arXiv timestamps; ensure consistency with submission date.

### P1B-Min7 — Section heading "(NOT A SPIN-TORSION THEORY MODULE)" in all caps in a section title
Use a normal subtitle or remove. The all-caps parenthetical reads as a self-correction.

### P1B-Min8 — Fn. 1 mid-sentence break to footnote about "119,617" disrupts flow
Move the reconciliation to a sample-accounting table (see E4).

### P1B-Min9 — Ref. [2] is cited as "PRD 106, 063503 (2022)" — verify volume formatting matches PRD style.

### P1B-Min10 — "Cobaya v3.5 original; v3.6.1 verification"
States two versions but does not say which produced which numbers. Specify.

---

## NIT
- N1: "Independent verification (production 500-realization run, April 2026)" — "April 2026" is a date stamp from the production run, not a section needed in a PRD paper.
- N2: "RunPod H200 instances" in acknowledgments — compute provider name is unnecessary.
- N3: Acknowledgments admit Claude was used as an AI research assistant. PRD's policy on AI assistance is evolving; verify journal policy.

---

## Page-count assessment
For three null/consistency-check analyses, none of which test the parent theory, 11 pages is roughly 5–6 pages of necessary content padded with disclaimers. Recommended max for the content present: **6 pages including references**, or merge as an appendix to Paper I(a).

---

## Summary recommendation
**REJECT**

This submission is unacceptable in present form for three independent reasons, any one of which would alone be disqualifying for PRD. (i) By the authors' own explicit statements, none of the three analyses tests the ECH spin-torsion physics that the title invokes; the paper is a methods cross-check labeled as theory verification. (ii) The headline "spectator-ALP" result is computed on a θ_i ∈ [0.5, 2] prior that the same paper concedes (fn. 5, fn. 6) lies entirely outside the spectator-consistent regime θ_i ∼ 0.1 — the title claim is contradicted by Appendix C. (iii) Multiple load-bearing quantities are not reproducible from the displayed inputs (the w_pivot σ formula in Table II fn. b does not give the quoted 0.0301; at least five mutually inconsistent sample counts circulate for the same chains; pipeline-recovery SNR^SE values are presented in body and figures without clarifying that the comparable per-realization figure is 0.91, well below the 2.7σ Planck NPIPE detection). On top of these, the body contains substantial review-log prose ("An earlier count erroneously quoted...", "A concern was raised...", "This addresses earlier reviewer concerns..."), the parent paper [1] is "in preparation" and cannot be consulted, and abstract framing ("natural parameters") is directly contradicted by the body (C_aγ ≥ 9 required, above KSVZ/DFSZ benchmarks). The salvageable content is a few paragraphs of NaMaster regression-test results and the ∆N_eff null measurement, which belong as an appendix to the parent paper once that paper exists in citable form.

---

## PASS 2 — self-critique findings (what initial review missed)

# Brutal-Honesty PRD Referee Report — P1B (Second-Pass Additions)

A second careful pass focused on arithmetic, internal consistency, figure-caption/body cross-checks, and citation accuracy. Several substantive new findings, including a mathematical impossibility in Table II that subsumes and amplifies E2 from the initial review.

---

## ESSENTIAL (NEW)

### P1B-E7 — Table II is mathematically self-contradictory (subsumes and worsens E2)

This is more serious than the simple arithmetic error I flagged in E2. The numbers in Table II are mutually inconsistent in three distinct ways, any one of which would force a recompute:

**(i) The displayed σ_wpivot formula does not reproduce the quoted value.**
The footnote states:
σ²_wpivot = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)²
Direct evaluation: 0.001901 + 0.110224 × 0.034745 = **0.005731**, so σ_wpivot = **0.0757**, not 0.0301. The arithmetic is off by a factor of 2.5.

**(ii) The pivot value a_p = 0.6680 is mathematically impossible given the quoted σ_w0 and σ_wa.**
Using the paper's own definition a_p = 1 − Cov(w_0, w_a)/Var(w_a):
|Cov(w_0, w_a)| = (1−a_p) σ²_wa = 0.3320 × 0.034745 = 0.01154.
But the Cauchy–Schwarz bound is |Cov| ≤ σ_w0·σ_wa = 0.0436 × 0.1864 = **0.00813**.
The implied correlation coefficient is 0.01154/0.00813 = **1.42**, which is impossible (|ρ| ≤ 1). Either σ_w0, σ_wa, or a_p is wrong; all three cannot hold simultaneously.

**(iii) σ(w_0 + w_a) = 0.1485 implies the opposite-sign covariance from a_p.**
For w_0 + w_a:
σ²(w_0 + w_a) = σ²_w0 + σ²_wa + 2 Cov(w_0, w_a) = (0.1485)² = 0.02205
→ 2 Cov(w_0, w_a) = 0.02205 − 0.001901 − 0.034745 = **−0.01459**
→ Cov(w_0, w_a) = **−0.00730** (negative).

But from a_p above we required Cov = +0.01154 (positive). The two derivations of Cov(w_0, w_a) from the same chain disagree in **both sign and magnitude**.

**Required fix:** Re-derive the entire (w_0, w_a) posterior summary from the actual chain covariance matrix, display the covariance / correlation coefficient explicitly, and recompute a_p, σ_wpivot, and σ(w_0 + w_a) consistently. As stated, the table cannot be reproduced from any internally consistent posterior.

This finding makes the headline "+4.3σ / −3.6σ marginal-tail departure" numbers unreliable as well: those use σ_w0 and σ_wa from the same table, and if those uncertainties are wrong, so are the departure-in-σ figures.

---

## MAJOR (NEW)

### P1B-M15 — Sec. V.A claims "four dataset combinations" but only three exist

Sec. V.A enumerates four: (1) Planck NPIPE; (2) +BAO; (3) +Pantheon+; (4) +SH0ES+S_8. Yet Sec. III, footnote 1, and the conclusions are explicit that only **two are frozen** (full-tension and Planck+BAO+SN) and **one is ongoing** (Planck-only). The +BAO-only combination is mentioned **nowhere** as either frozen or ongoing. Fig. 2 legend shows only the two frozen combinations. Appendix A lists four YAMLs but the +BAO YAML appears unused.

**Required fix:** Either run the +BAO-only chain and report it, or remove it from Sec. V.A and Appendix A.

### P1B-M16 — Abstract's "2.4–2.9σ" lower bound is untraceable

Abstract footnote a cites "the published Planck/ACT DR6 2.4–2.9σ [2, 3]." References [2] (Eskilt-Komatsu, 3.6σ joint) and [3] (Diego-Palazuelos-Komatsu ACT DR6, central value 0.215° ± 0.074° → 2.9σ) appear elsewhere. Sec. VI cites Ref. [15] for Planck NPIPE β = 0.30° ± 0.11° → 2.7σ. **No analysis in the body produces 2.4σ as a lower bound.** The reader cannot determine what measurement the 2.4σ refers to.

**Required fix:** Either replace "2.4–2.9σ" with "2.7–2.9σ" (Planck NPIPE and ACT DR6 individually), or cite the specific paper giving 2.4σ.

### P1B-M17 — Appendix C contradicts body on f_a

Body §VI consistently writes f_a ∼ M_Pl (proportional). Appendix C states "f_a: fixed at M_Pl (spectator-class theoretical input from the Holst-sector pseudoscalar structure; not sampled)." The MCMC therefore **fixes** the decay constant rather than scanning it, contrary to the body's hedged "∼" notation. This matters because the β prediction scales linearly with the C_aγ × (Δϕ/f_a) product; pinning f_a = M_Pl exactly is a strong theoretical assumption that should be stated in the body, not buried in the appendix.

### P1B-M18 — Fig. 3 caption misreferences equations

Fig. 3 caption states: "Bias β̂ − β_inj is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in **Eq. 1–3**." But Eq. (1) is β̂_NaMaster = 0.238°, Eq. (2) is the ALP field displacement Δϕ/f_a ≈ 0.65, and Eq. (3) is the birefringence-value formula β ≈ α_EM × 8/(4π) × 1.07. **None of these equations adopts a 0.04° systematic floor.** Eq. (4) is the inverse-variance combination of Planck NPIPE and ACT DR6, which similarly does not use a 0.04° floor. The caption-to-body reference is broken.

### P1B-M19 — Ref. [22] (Cai et al., Quintom review) cited as "the underlying ECH cosmology"

Footnote 4 (p. 7): "the quintom-bounce dynamics that supply the early-universe / contracting-phase H(z) in the underlying ECH cosmology [22]." Reference [22] is *Quintom Cosmology: Theoretical implications and observations* by Cai et al. 2010 — a generic two-field dark-energy review with no relationship to Einstein–Cartan–Holst or ECH spin-torsion. This is a citation-attribution error; the intended reference would be either Paper I(a) [1] or specific ECH-bounce literature, not a generic quintom review.

### P1B-M20 — Conclusions' Ref. [12] (DESI DR2) misattributed as a quintom-B reference

Conclusions: "GetDist posteriors on w_0w_a are available as **an empirical test of the quintom-B scenario [12]**." Ref. [12] is the DESI DR2 BAO measurement paper (Abdul-Karim et al.), which is the data, not the quintom-B theory. The cited reference for "the quintom-B scenario" should be a theory paper (probably Ref. [22] Cai et al., though see M19). The references are crossed.

### P1B-M21 — Footnote 4 quantitatively understates the ΛCDM-vs-quintom background systematic

Footnote 4 claims "a quintom late-time w_0w_a background ... shifts H(z) at z ≲ 1 by ∼few percent, propagating to a ≲few-percent systematic on Δϕ/f_a." But the same paper's quintom posterior has w(z = 0) = w_0 = −0.81 (Table II), which is ≈ 20% off from ΛCDM at z = 0. The ALP integration runs from recombination to today, accumulating the H(z) departure across z ∈ [0, 1100]; quoting a "≲ few-percent" systematic without showing the actual ALP-EOM integration on the quintom background is hand-waving.

**Required fix:** Integrate the ALP EOM on the actual posterior-mean quintom H(z) and quote the realized Δ(Δϕ/f_a). Without this, the entire spectator-ALP analysis sits on a ΛCDM background that the cosmological-fits section rejects.

### P1B-M22 — Cobaya likelihood "H0.riess2020Mb" cited against Riess+2022

Section III/V repeatedly refers to "H0.riess2020Mb" but cites Ref. [7] = Riess et al. 2022 ApJL 934 L7. The Cobaya likelihood file is named after Riess+2020 (Riess et al. 2021 ApJ 908 L6), which gave M_B = −19.244 ± 0.037. Riess+2022 gives M_B = −19.253 ± 0.027. The paper compares its M_B posterior to the −19.253 ± 0.027 (Riess+2022) value but uses the Cobaya likelihood named for the 2020 paper. Either the Cobaya likelihood is the 2022-data version with a legacy name, or there is a year-mismatch between the prior actually applied and the value being compared to.

**Required fix:** State explicitly which Riess paper's M_B prior is operative in the Cobaya likelihood, and verify the comparison value matches.

---

## minor (NEW)

### P1B-m4 — Eq. 3 implicit unit conversion

The displayed equation β ≈ (α_EM × 8)/(4π) × 1.07 ≈ 0.29° computes a dimensionless angle in radians on the RHS (= 4.97 × 10⁻³ rad) and reports it in degrees on the LHS. The conversion factor 180/π is implicit. Show the intermediate "≈ 5.0 × 10⁻³ rad ≈ 0.29°" for clarity.

### P1B-m5 — "Eq. 4 (3.9)" missing σ symbol

Eq. (4): "β_combined = 0.241° ± 0.061° (3.9)" should read "(3.9σ)."

### P1B-m6 — DESI DR2 χ²_BAO = 10.6 ± 1.8 lacks dof

DESI DR2 has ~13 distinct BAO measurements. χ² = 10.6 with no dof quoted leaves the per-dof fit quality unverifiable.

### P1B-m7 — Fig. 2(a) "WP4 reheating" and "WP4 decay" undefined and uncited

I noted these in M5 above; additionally, the bracket ranges "[0.05, 0.40]" and "[0.01, 0.25]" are presumably ∆N_eff prediction windows for two model classes (Weak-scale processes? Warm-dark-matter Phase 4?), but neither is defined or sourced. Without a citation, the comparison strip in the figure conveys no information.

### P1B-m8 — Acknowledgments cite "Anthropic Claude" as AI assistant

Already noted in N3; emphasize that PRD's AI-disclosure policy as of 2025–2026 requires a more specific statement (e.g., scope of use, verification protocol).

### P1B-m9 — Fig 2 legend labels "WP4" without definition (see also m7)

Repeated.

### P1B-m10 — H(z) integration window for Δϕ/f_a not stated

§VI Eq. (2): "Δϕ/f_a ≈ 0.65 (m = H_0, θ_i = 1)" — the integration runs "from recombination to today" per the surrounding text, but no plot or check of the actual numerical trajectory is provided. The reader cannot verify 0.65 from inputs.

---

## NIT (NEW)

- **N4**: "ongoing" appears twice describing the Planck-only chain at R̂ − 1 ∼ 0.05; tighten to a single mention with the current sample count.
- **N5**: "GetDist" vs "getdist" inconsistent capitalization throughout.
- **N6**: Date stamp "2026-06-08 PDT" in title block — verify consistency with the arXiv submission date.
- **N7**: "Note." prefix on §VI is informal; replace with a normal sentence opener.

---

## Aggregate updated recommendation

The second pass strengthens rather than softens the initial REJECT verdict. The most serious new finding (E7) shows that the Table II posterior summary is mathematically self-contradictory: the displayed Cov(w_0, w_a) inferred three different ways gives three different answers (one positive, one negative, one Cauchy–Schwarz–violating). This is not a typographical error; it is a posterior that cannot exist. The "+4.3σ" / "−3.6σ" tension headline propagates from those same uncertainties and is therefore unreliable, joining E1's "spectator label on a non-spectator prior" and E3's "verifies-no-physics" as a third independent disqualifier.

The recommended path forward remains: withdraw, recompute the (w_0, w_a) posterior summary from the actual chain covariance matrix, replace the spectator-ALP MCMC with one on a spectator-consistent prior (or rename the analysis), trim to ≤ 6 pages of methods cross-checks, and merge as an appendix to Paper I(a) once that paper exists in citable form.