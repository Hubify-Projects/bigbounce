# P2 auto-2026-06-08_1632pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10931 chars)
**Wall time**: 296.8s

---

# Referee Report: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

**Manuscript tag:** P2 | **Submitted to:** Physical Review D

---

## Overview

This 6-page manuscript claims that a spectator ALP with f_a ~ M_Pl and m ~ H_0 "naturally" predicts β ≈ 0.27°, matching the observed cosmic birefringence signal. The paper performs a Gaussian summary-likelihood combination of Planck NPIPE and ACT DR6, runs MCMC, computes a Bayes factor, and forecasts LiteBIRD sensitivity. By the author's own admission (Sec. 6), the model class is well-studied (Fujita et al. 2021 already showed Planck-scale ALPs give β ~ 0.3°), and the contribution is "the specific parameter identification" plus "the inference framework demonstrating internal consistency." This is a thin contribution. Combined with multiple serious technical issues, this paper does not meet the PRD bar.

---

## ESSENTIAL findings

### P2-E1 — Headline σ values from different procedures juxtaposed without qualification
**Abstract, p.1.** The abstract states "3.6σ isotropic birefringence signal (β_obs = 0.342 ± 0.094°)" and then "β = 0.242 ± 0.061° (3.9σ from zero)" from the author's own combination. Note: 0.342/0.094 = 3.64σ, while 0.242/0.061 = 3.97σ. These are different central values from different procedures (joint EB fit vs. point-estimate combination) — yet the abstract presents both without any qualifier that they are not directly comparable. The body (Sec. 3.1) admits "they differ because [Eskilt] fits the full EB cross-spectrum rather than combining point estimates" but the abstract does not. Worse, the paper has it both ways: it uses the higher Eskilt central value (0.342°) for the MCMC and the "best-fit prediction" claim (0.27° matching 0.342°), but quotes the lower combined value (0.242°) for headline significance. **Required fix:** explicitly state in the abstract that the two β values come from incompatible procedures; do not allow side-by-side σ values without qualification at every juxtaposition.

### P2-E2 — The β ≈ 0.27° prediction is post-hoc and not derived
**Sec. 2.2, p.2.** Equation (2) gives β ≈ (C_0 θ_i / 2) × O(1). The paper then asserts "the cosmological field evolution gives Δφ/f_a ~ 10⁻² (from the ratio of field displacement to decay constant over the Hubble time), yielding β ≈ C_0 θ_i × 5×10⁻³ rad ≈ 0.27°." But Eq. (1) gives Δφ/f_a = θ_i × (1 − J_0(m/H_0)/J_0(0)), which for m/H_0 ~ 1 is 0.24 × θ_i ~ O(0.1), **not 10⁻²**. There is a factor-of-10 inconsistency between Eq. (1) and the numerical estimate. With Δφ/f_a ~ 0.24, β ~ C_0 θ_i × 0.12 rad ~ 7°, not 0.27°. The "natural" prediction is therefore not natural at all — it requires either C_0 θ_i ~ 0.02 (small) or a different cosmological suppression factor that is not derived. The author cannot have it both ways: either show the full Bessel/integration calculation that gives 5×10⁻³, or admit the 0.27° number requires tuning. **Required fix:** present the actual cosmological integration (the EOM solution between recombination and today) and show exactly how 5×10⁻³ rad emerges. The current presentation is hand-waving and the central claim of naturalness collapses.

### P2-E3 — Dimensional / order-of-magnitude error in the "natural" estimate
**Sec. 2.2, p.2.** Following on E2: 5×10⁻³ rad = 0.286°, which the paper rounds to 0.27°. But Eq. (1) with the stated J_0(1) ≈ 0.24 → Δφ ≈ 0.24 f_a θ_i → β = (C_0 / 2f_a)(0.24 f_a θ_i) = 0.12 C_0 θ_i rad ≈ 6.9° for C_0 θ_i ~ 1. This is **25× too large**. There is no resolution of this in the paper. The MCMC Run 1 uses "C = 8 fixed" (Sec. 3.3 / Table 1), which alongside θ_i ~ 0.3 would make C_0 θ_i ~ O(1) only if the formula in Eq. (2) is reinterpreted. Sec. 3.3 even reports C_aγ × θ_i = 3.4 ± 1.1 — far from O(1). **Required fix:** reconcile Eqs. (1)–(2) with the numerical prediction, the "C = 8 fixed" choice (why 8 and not ~1?), and the C_aγ × θ_i = 3.4 result. As written, the paper contains an internal arithmetic contradiction that destroys the "no fine-tuning" claim.

### P2-E4 — Bayes factor is essentially uninterpretable
**Sec. 3.4, p.3.** ln B = 5.17 is reported as the headline number in the abstract, but the body admits ln B ranges from 4.48 to 5.86 depending on the prior interval [0°, 2°] vs [0°, 0.5°]. Additionally, the MCMC has only 720–6,840 samples (Table 1), with N_eff ~ 1,000, which the author concedes is inadequate for evidence calculations. A Bayes factor with these properties does not belong in the abstract. **Required fix:** remove the ln B = 5.17 number from the abstract; or, rerun with ≥50,000 samples and physically motivated priors. Currently the headline evidence number is an artifact of arbitrary prior choice and undersampled chains.

### P2-E5 — "C = 8 fixed" is not justified and contradicts the "no fine-tuning" claim
**Sec. 3.3, Table 1, p.3.** Run 1 fixes C = 8. The text never justifies why C_0 = 8 is the appropriate fixed value. If "C_0 is an order-unity coefficient from the ABJ anomaly" (Sec. 2.2), C_0 = 8 is at the upper edge of "order unity" and corresponds to a specific UV completion that is not specified. Furthermore, fixing C = 8 while claiming naturalness "without any fine-tuning" is contradictory. **Required fix:** justify the choice C_0 = 8 from a specific UV model (e.g., DFSZ-like, KSVZ-like, multi-fermion anomaly), or drop the C-fixed run entirely.

### P2-E6 — Figure 1 reports values inconsistent with text
**Fig. 1 (triangle plot), p.4.** The figure marginals quote θ_i = 1.33 (+0.44 / −1.1), C_aγ = 13.4 (+5.6 / −11), log_10(m_a/eV) = −31.4 (+1.4 / −1.2), β = 0.324 ± 0.099°. But Sec. 3.3 reports for the same Run 2: C_aγ × θ_i = 3.4 ± 1.1. Cross-check: 1.33 × 13.4 = 17.8, not 3.4. There is a 5× inconsistency between the marginals shown in the figure and the product quoted in the body. **Required fix:** either the product is from the joint posterior (in which case state this and show the actual joint sample-by-sample product), or the marginals are wrong. Currently the reader cannot reconcile them.

### P2-E7 — LiteBIRD 9σ forecast double-counts the same observation
**Sec. 4, p.3.** The forecast significance 0.27/0.03 = 9σ treats the *predicted* β as if it were a measurement. But the only reason to expect β ≈ 0.27° in the first place is the current Planck+ACT signal. If that signal is partly systematic (Sec. 6 admits an "active debate" about 0.1–0.3° residual systematics), then LiteBIRD will not necessarily reproduce 0.27°. The forecast does not propagate the uncertainty on the prediction itself. A proper forecast would marginalize over the posterior on β: σ(β_LiteBIRD) ≈ 0.03° gives a detection significance over the *posterior range* 0.24 ± 0.06°, which yields 8 ± 2σ — not a clean "9σ test." **Required fix:** reformulate the forecast as a posterior-predictive significance with uncertainty bands. The "either confirms or rules out at 9σ" framing in the abstract is misleading.

### P2-E8 — "Independent of bounce cosmology" claim is trivial and used to inflate scope
**Abstract and Sec. 5.** Three times the paper emphasizes the result is "independent of bounce cosmology." This is true (a spectator ALP doesn't care about the background), but it is also vacuous and exists only to cross-link the author's two companion papers. A reader of this paper alone has no reason to care about bounce cosmology. **Required fix:** remove the "independent of bounce cosmology" framing from the abstract and conclusion. It is filler. Section 5 should be deleted or compressed to a single sentence.

### P2-E9 — Novelty claim is undermined by the author's own admission
**Sec. 6, p.5.** The paper explicitly states "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°." This is the *entire* contribution claimed in the abstract. The author's stated incremental contribution is "the specific parameter identification (f_a ~ M_Pl, m ~ H_0)" — but Fujita et al. used exactly this identification. The remaining contribution is "the inference framework demonstrating internal consistency," which amounts to combining two published β values with a Gaussian likelihood — a trivial exercise. **Required fix:** the abstract and introduction must accurately convey that this paper adds essentially nothing beyond Fujita et al. (2021). As written, the framing is misleading.

### P2-E10 — "Eskilt et al. joint Planck + ACT analysis" citation is missing / inconsistent
**Abstract and Sec. 3.1.** The abstract cites "Eskilt et al. joint Planck + ACT analysis" for β_obs = 0.342 ± 0.094°. The reference list contains Eskilt & Komatsu (2022) (β = 0.30 ± 0.11°, WMAP+Planck, no ACT) and Diego-Palazuelos & Komatsu (2025) (ACT). There is no Eskilt et al. joint Planck+ACT paper cited. The value 0.342 ± 0.094° matches Eskilt, Herold, Komatsu et al. (PRL 2023, "Constraint on Early Dark Energy from Isotropic Cosmic Birefringence") — but that reference is not in the bibliography. **Required fix:** cite the correct paper for β_obs = 0.342 ± 0.094°; the current bibliography does not support the headline number.

### P2-E11 — Namikawa, Murai & Naokawa reference is "in preparation" but used as load-bearing citation
**References, p.6.** "Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. **In preparation**; cited for comparison of ALP mass constraints." Citing an in-preparation paper for a load-bearing claim ("Namikawa, Murai & Naokawa provide superior ALP mass constraints") is unacceptable in PRD. **Required fix:** replace with a published reference or remove the claim.

### P2-E12 — Companion papers cited as "submitted simultaneously" with no arXiv IDs
**References, p.6.** Both Golden 2026a (ECH gravity) and Golden 2026b (matter-bounce f_NL) are cited as "Companion paper, submitted simultaneously." No arXiv ID, no journal, no DOI. The body relies on these for the ECH motivation (Sec. 5) and the f_NL = −35/8 cross-test (Sec. 6). **Required fix:** provide arXiv numbers, or remove the claims that depend on companion papers.

---

## MAJOR findings

### P2-M1 — Eq. (1) is dimensionally and physically obscure
**Sec. 2.1, p.2.** The displacement formula Δφ ≈ f_a θ_i (1 − J_0(m/H_0)/J_0(0)) is presented with no derivation. The Bessel-function form is appropriate for a damped harmonic oscillator solution in radiation domination, but here the field rolls during matter and dark-energy eras. The formula is therefore wrong in this regime; the actual solution requires numerical integration. The text concedes "the precise value depends on the cosmological integration" — so why cite a Bessel function form that doesn't apply? **Required fix:** replace with a numerical solution of the Klein-Gordon equation in the actual ΛCDM background.

### P2-M2 — Section 3.2 likelihood is wrong for correlated foreground systematics
**Sec. 3.2, p.2.** The Gaussian product likelihood assumes independent errors between Planck NPIPE and ACT DR6. The two experiments share foreground templates and observe overlapping sky areas. Independence is not justified. **Required fix:** quantify the correlation or use a more conservative combined error.

### P2-M3 — Arithmetic check on Eq. (4)
**Sec. 3.2, p.2.** Combining 0.30 ± 0.11 and 0.215 ± 0.074 with inverse-variance weighting:
- w_1 = 1/0.0121 = 82.6
- w_2 = 1/0.005476 = 182.6
- β_comb = (0.30 × 82.6 + 0.215 × 182.6) / 265.2 = (24.78 + 39.26) / 265.2 = 0.2415°
- σ_comb = 1/√265.2 = 0.0614°

Result: 0.242 ± 0.061°, σ = 3.94. The quoted value (3.9σ) is correct. **No fix needed** — this is reported as a check.

### P2-M4 — "f_photon × C_0 = 1.73 ± 0.44" is undefined
**Eq. (5), Sec. 3.2.** The quantity "f_photon × C_0" appears only here. It is never defined. Where does 1.73 come from? Is it β_combined / (some normalization)? The reader cannot interpret this number. **Required fix:** define f_photon and the normalization, or remove Eq. (5).

### P2-M5 — Figure 2 is filler
**Fig. 2, p.5.** Three Gaussian curves with means within 0.01° of each other are plotted on the same axis. The figure shows that three models give nearly identical β posteriors — but this is obvious from the equations and adds no information. **Required fix:** drop Fig. 2 or replace with a more informative plot (e.g., posterior over the 2D plane of (C_aγ, θ_i)).

### P2-M6 — MCMC sample sizes are inadequate (admitted) — proceeds anyway
**Sec. 3.3, p.3.** The author admits 720–6,840 samples are inadequate, then publishes the results anyway. This is not acceptable. For a PRD-level inference paper, rerun with ≥50,000 effective samples before submission. **Required fix:** rerun chains.

### P2-M7 — "9σ" forecast assumes LiteBIRD σ(β) = 0.03°
**Sec. 4, p.3.** LiteBIRD forecasts depend strongly on the self-calibration method and the assumed prior on instrumental polarization angles. The cited LiteBIRD paper does not unconditionally guarantee σ(β) = 0.03°; this is a best-case scenario. **Required fix:** quote the actual range from LiteBIRD forecasts and propagate.

### P2-M8 — "Matter-bounce non-Gaussianity f_NL = −35/8" appears with no derivation or context
**Sec. 6, p.5.** This is dropped in without context. It belongs in the companion paper, not here. **Required fix:** remove.

### P2-M9 — Sec. 6 calibration-systematics paragraph contradicts headline confidence
**Sec. 6, p.5.** "There is an active debate about whether residual ~ 0.1–0.3° systematics could arise..." This 0.1–0.3° range *encompasses the entire claimed signal* (0.24°–0.34°). The paper should not be making 9σ forecast claims when the entire signal might be a systematic. **Required fix:** the abstract must acknowledge this systematic concern.

---

## MINOR findings

### P2-m1 — Abstract claim "9σ significance — either confirming the signal or ruling out the ALP explanation decisively"
This is overconfident given E7 and M7. Soften.

### P2-m2 — "Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4)"
"Indicative" is doing a lot of work for a number with ~30% variation across reasonable priors. The qualifier should be stronger.

### P2-m3 — "ECH gravity" / "Barbero-Immirzi pseudoscalar sector of the Holst action"
**Sec. 5, p.4.** This is essentially theoretical name-dropping. The author admits "no derivation connects the Holst action to a specific ALP potential or coupling." Either derive it or remove the paragraph.

### P2-m4 — Eq. (8) reports C_aγ × θ_i = 3.4 ± 1.1 as "consistent with O(1)"
3.4 is not O(1) in the strict sense; it is closer to O(few). The phrasing is loose.

### P2-m5 — Title "Predictions, Constraints, and LiteBIRD Forecasts" overstates content
The paper has one prediction (0.27°), a Gaussian combination (not a new constraint), and a one-line forecast division (0.27/0.03). The title oversells.

### P2-m6 — Sec. 2.2 "The key feature: this prediction involves no small or large numbers beyond the cosmological integration factor."
But the cosmological integration factor *is* the small number (10⁻² claimed, see E2/E3).

### P2-m7 — Eq. (10) uses ratio without uncertainty propagation
σ_LiteBIRD only enters the denominator; σ on the predicted β is ignored.

### P2-m8 — ACT DR6 σ = 0.074° → 0.215/0.074 = 2.9σ
Confirmed. **OK.**

### P2-m9 — Eskilt 0.30/0.11 = 2.73σ → rounded to 2.7σ
Confirmed. **OK.**

---

## NITS

### P2-N1 — "Caγ" in equations vs "Cay" / "C" elsewhere
Notation drifts between C_0, C, C_aγ. Pick one.

### P2-N2 — Sec. 6: "well-studied in the literature [Fujita et al., 2021]"
Single citation does not constitute "well-studied." Add more references or weaken.

### P2-N3 — Reference [Diego-Palazuelos and Komatsu, 2025] has no arXiv number.

### P2-N4 — The abstract twice uses the word "naturally" (and "natural" four more times). Overused.

### P2-N5 — "March 20, 2026" date with 2026 references — consistent but worth noting these are all in-prep/future.

---

## Page-budget assessment

The actual scientific content is: (i) a β ≈ 0.27° estimate (one paragraph, currently broken — see E2/E3), (ii) a Gaussian product of two numbers (one line), (iii) a division 0.27/0.03 = 9 (one line). The companion-paper cross-references (Sec. 5, parts of Sec. 6) inflate the page count without adding content. **Recommended maximum: 3 pages** (PRD Brief Report or short Letter format), and only after E1–E12 are resolved.

---

## Summary recommendation

**REJECT**

This manuscript has a contradictory central calculation (E2/E3: Eq. (1) and the 10⁻² estimate disagree by a factor of ~25, destroying the "no fine-tuning" claim), reports a headline Bayes factor that varies 30% with prior choice from undersampled MCMC chains the author concedes are inadequate (E4, M6), cites a load-bearing measurement (β = 0.342 ± 0.094°) without the corresponding reference in the bibliography (E10), relies on two unsubmitted companion papers and one "in preparation" paper for substantive claims (E11, E12), contains numerically inconsistent figures (Fig. 1 marginals vs. quoted product, E6), and by the author's own admission adds essentially nothing beyond Fujita et al. (2021) (E9). The systematic-error caveat in Sec. 6 acknowledges that the entire signal (~0.2–0.3°) may be a calibration artifact of comparable magnitude — yet the abstract and conclusion claim a "decisive 9σ test." This is not a PRD paper.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Re-Examination

Below are issues my initial review missed. I focus on items uncovered by the targeted classes (A–J).

---

## ESSENTIAL findings (additional)

### P2-E13 — MCMC mass posterior **directly contradicts** the abstract's "m ~ H₀" claim
**Fig. 1 marginal, p.4; abstract, p.1.**

Fig. 1 reports log₁₀(m_a/eV) = −31.4 (+1.4 / −1.2). Converting H₀: H₀ ≈ 70 km/s/Mpc ≈ 1.5 × 10⁻³³ eV, i.e. log₁₀(H₀/eV) ≈ −32.82. The posterior thus prefers **m ≈ 26–30 H₀**, not m ~ H₀.

Consequences:
- Sec. 2.1 says the field "begins rolling at z ~ O(1) when H(z) ~ m." For m ~ 30 H₀, in matter domination H(z)/H₀ = √Ω_m (1+z)^(3/2), which equals 30 at z ≈ 13 — i.e. shortly after recombination, not z ~ 1. The entire "rolling today" picture in §2 is **falsified by the author's own posterior**.
- Eq. (1) used the Bessel-function form valid for m/H₀ ~ 1; for m/H₀ ~ 30 it gives 1 − J₀(30) ≈ 1 (rapid oscillations), changing the prediction by ~4× relative to the m/H₀ ~ 1 case quoted in §2.

The abstract's centerpiece — "m ~ H₀ ensures the field is rolling today" — is **explicitly contradicted by the author's own MCMC**. This is far more damaging than the issues flagged in my first pass.

**Required fix:** either (i) rerun MCMC with a tight prior centered on m = H₀ and quote the resulting β (which I expect is **inconsistent** with the data), or (ii) retract the "m ~ H₀ natural" framing entirely. The author cannot simultaneously claim m ~ H₀ in the abstract and report m ~ 30 H₀ from the fit.

### P2-E14 — MCMC coupling posterior C_aγ ≈ 13.4 is **not** order-unity
**Fig. 1 marginal, p.4.**

C_aγ = 13.4 (+5.6 / −11) is a factor of ~10 larger than the "natural" O(1) value. Worse:
- The prior is C_aγ ∈ [1, 30] (Sec. 3.3) — i.e. the prior **excludes** C_aγ < 1, biasing toward large values.
- C_aγ = 13.4 is half the prior upper bound and well above the "order unity" regime invoked throughout.
- The 1σ lower error bar reaches 2.4 — still not O(1).

This **contradicts the central naturalness claim**. A pseudoscalar with C_aγ = 13 requires a UV completion with ~13 charged fermions in the anomaly loop or large representations — not "natural."

Combined with θ_i ~ 1.3 (also Fig. 1), the marginal-median product C_aγ × θ_i ≈ 17.8, which the text reports as 3.4 ± 1.1 (Eq. 8) without explanation of the 5× discrepancy (presumably from a strongly anti-correlated joint posterior, but this is never discussed).

**Required fix:** widen the prior to include C_aγ < 1 and rerun. If the posterior still prefers C_aγ >> 1, abandon the "no fine-tuning" framing.

### P2-E15 — The analytic estimate and the MCMC posteriors are **mutually inconsistent**
**Sec. 2.2 vs Sec. 3.3 / Fig. 1.**

Cross-checking the analytic prediction against the MCMC:

- Sec. 2.2 claim: β ≈ C_0 θ_i × 5×10⁻³ rad ≈ 0.27° for C_0 θ_i ~ 1.
- Eq. (2): β = (C_0 θ_i / 2) × (1 − J₀(m/H₀)) rad. For C_0 θ_i ~ 1 and m/H₀ ~ 1, this gives β ≈ 0.12 rad ≈ 7°, **25× larger than 0.27°**.
- Sec. 2.2 implicitly requires Δφ/f_a ~ 10⁻² (the suppression factor). But Eq. (1) gives Δφ/f_a = θ_i (1 − J₀(m/H₀)). To produce 10⁻² with θ_i = 1, need (1 − J₀(m/H₀)) = 10⁻², which requires m/H₀ ≈ 0.2 — i.e., **m ≈ 0.2 H₀**, corresponding to log₁₀(m/eV) ≈ −33.5.
- But the MCMC posterior (E13) gives m ~ 30 H₀, where (1 − J₀(m/H₀)) ≈ 1, and the analytic prediction would give β = (C_aγ θ_i / 2) ≈ 9 rad ≈ 500° — clearly nonsense.

So **either the analytic 5×10⁻³ rad estimate is wrong, or the MCMC is not actually using the relation in Eq. (2)**. The paper does not explain what relation the MCMC code actually implements. This is the single largest unresolved issue: the analytic derivation in §2 and the numerical inference in §3 cannot both be right.

**Required fix:** publish the actual β(C_0, θ_i, m) function used in the MCMC, and show explicitly why it agrees with Eq. (2) when m ~ H₀ but produces 0.27° for the fitted m ~ 30 H₀.

### P2-E16 — Eq. (5) is just β_combined relabeled, not an independent measurement
**Eq. (5), Sec. 3.2.**

The undefined quantity "f_photon × C_0 = 1.73 ± 0.44" turns out to be β_combined rescaled by ≈ 0.14°/unit: 1.73 × 0.14° = 0.242°, and 0.44 × 0.14° = 0.062°. The significance 1.73/0.44 = 3.93σ is **identical** to 0.242/0.061 = 3.97σ (Eq. 4) up to rounding.

So Eq. (5) is the same measurement as Eq. (4), differently labeled, with the fiducial normalization (0.14° per unit coupling) **never stated**. Presenting this as a distinct inference inflates the apparent quantitative content.

**Required fix:** define the normalization explicitly, or drop Eq. (5). As-is, it presents a trivially derived quantity as if it were an independent constraint.

---

## MAJOR findings (additional)

### P2-M10 — θ_i posterior is prior-edge-limited
**Fig. 1.** θ_i = 1.33 (+0.44 / −1.1), with prior [0.01, π]. The 1σ upper edge reaches 1.77, with the 95% tail extending past 2.5, hitting the prior wall at π ≈ 3.14. The posterior is **prior-bounded on the upper end**, not data-bounded. Any product like C_aγ × θ_i inherits this dependence. The paper does not address this.

### P2-M11 — Prior on log₁₀(m/eV) ∈ [−35, −30] artificially excludes the relevant regime
The 5-decade flat-in-log prior places only ~37% of prior mass at m > H₀ (log₁₀ > −32.82) and ~63% at m < H₀. Yet the posterior peaks well inside the m > H₀ region. The data are clearly informative on mass — but the prior bias (flat in log over 5 decades) is never discussed. A flat-in-linear prior or a tight log-prior centered at H₀ would yield very different posteriors. **Required fix:** prior-sensitivity analysis on log₁₀(m/eV).

### P2-M12 — Sec. 6 calibration paragraph implies the entire signal could be 0σ
"There is an active debate about whether residual ~ 0.1–0.3° systematics could arise..." — this range encompasses **the entire claimed signal (0.242°)**. If true, the signal could be 0.0° ± 0.3°, i.e. 0σ. This sits in tension with both the 3.9σ headline and the 9σ LiteBIRD forecast, and should appear in the abstract. Already flagged in M9 but worth re-emphasizing: the systematic-floor and the signal magnitude are **of the same order**.

### P2-M13 — The "C = 8 fixed" choice in Run 1 has no analytical correspondence
**Sec. 3.3.** C = 8 is the **geometric center** of the flat prior [1, 30] in log space (log₁₀(1) to log₁₀(30) midpoint is 0.74, giving 5.5; arithmetic midpoint is 15.5; geometric is 5.5; 8 is none of these exactly). There is no physical or statistical justification for 8. It looks like a discretionary parameter choice that yielded a posterior close to β_obs.

### P2-M14 — Run 3 has only 720 samples but R̂ − 1 = 0.005 is reported
**Table 1.** R̂ requires multiple chains and a minimum effective sample size per chain. 720 total samples likely means 4 chains × 180 samples; R̂ statistics are unreliable at this scale. The author admits N_eff ~ 1000 is inadequate but still reports R̂ − 1 < 0.01 as evidence of convergence. R̂ at 720 samples does **not** establish convergence in a meaningful sense.

---

## MINOR findings (additional)

### P2-m10 — Fig. 2 labels do not match Table 1
Fig. 2 legend: "Model 2: ALP (C=8)", "Model 2b: ALP (C free)", "Model 0: beta free." Table 1: "Run 1", "Run 2", "Run 3." Reader must guess which is which.

### P2-m11 — "Model 0" / "Model 2" / "Model 2b" labels suggest a larger model space
The numbering implies Models 1, 3, 4, ... exist elsewhere. Are these from a companion paper / earlier draft? Stale labeling.

### P2-m12 — Eq. (6) (β_ALP = 0.336 ± 0.107°, Run 1) vs Fig. 1 (β = 0.324 ± 0.099°, Run 2)
The text quotes Run 1 result but Fig. 1 shows Run 2. The triangle plot does **not** correspond to Eq. (6). The reader has no posterior visualization of the headline ALP fit (Run 1, C = 8 fixed).

### P2-m13 — "3.4 ± 1.1" vs marginal product 17.8
The text reports Eq. (8) as C_aγ × θ_i = 3.4 ± 1.1, but the marginal medians multiply to 17.8. This is presumably a joint-posterior product (with strong anti-correlation pushing the product down), but the text doesn't say so. A diagonal panel showing the C × θ product would clarify.

### P2-m14 — "the full Planck EB spectrum" (Sec. 6) attributes a method to Namikawa et al.
But Eskilt also uses the full EB spectrum. The distinction is unclear.

### P2-m15 — Date "March 20, 2026" with all 2026 references
All 2026 references are companion papers by the same author. The dating implies coordinated submission of three papers from one author — concerns about parallel arXiv posting flagged but not adjudicated by the manuscript.

### P2-m16 — "1 − J₀(1) ≈ 0.24" (Sec. 2.1) — numerical check
J₀(1) = 0.7651, so 1 − J₀(1) = 0.2349. Correct.

### P2-m17 — Eq. (1) cites J₀(0) = 1 in the denominator
J₀(0) = 1, so dividing by it is trivial. The notation "J₀(m/H₀)/J₀(0)" is artificially complicated when the denominator equals 1.

---

## NITS (additional)

### P2-N6 — "MCMC" used loosely
The paper never states the sampler (emcee? Metropolis-Hastings? NUTS?), step parameters, or chain count. Reproducibility requires this.

### P2-N7 — "MPl" notation inconsistent with the standard convention
The paper never specifies whether M_Pl = (8πG)⁻¹ᐟ² ≈ 2.4×10¹⁸ GeV or G⁻¹ᐟ² ≈ 1.2×10¹⁹ GeV. The factor matters for "f_a ~ M_Pl" naturalness.

### P2-N8 — "fphoton × C0" notation (Eq. 5) vs "C_aγ" (Sec. 3.3)
Multiple notations for related/identical quantities. Already partially flagged in N1 of initial review, but Eq. (5)'s "f_photon" is a separate symbol not defined anywhere.

### P2-N9 — Acknowledgment: "AI research assistants during the analysis and manuscript preparation"
While appropriate disclosure, this combined with the unresolved analytic-vs-MCMC inconsistencies (E15), undefined quantities (M4 / E16), and mismatched figure labels (m10, m12) suggests insufficient human verification of internal consistency.

---

## Updated summary

The fresh-eyes pass uncovered three additional **essential** issues that were not visible on first read:

1. **E13: The MCMC mass posterior contradicts the abstract.** The author claims m ~ H₀ throughout, but the posterior gives m ~ 30 H₀. This invalidates the §2 "begins rolling at z ~ 1" picture and the entire "natural ALP" framing.

2. **E14: The coupling posterior is far from order unity.** C_aγ ≈ 13.4, with a prior that excludes natural O(1) values. This destroys the "no fine-tuning" claim independently of the issues already flagged.

3. **E15: The analytic prediction and the MCMC are mutually inconsistent.** The Sec. 2 derivation and the Sec. 3 fit cannot both implement the same physics. The paper does not reconcile them, and a careful reader cannot reproduce 0.27° from the stated formulas at the fitted parameter values.

These compound the original concerns. The recommendation remains **REJECT**, now with substantially greater certainty: the paper's central physical claim (m ~ H₀, natural O(1) parameters) is **falsified by the author's own posterior**, not merely unjustified.