# P1B R26conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper1b_mcmc_companion_v1B.0.53.pdf` md5=86261d4b pages=16
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique

---

## Pass 1 — native-PDF brutal referee read

Companion paper to P1A. Three independent verification analyses: (i) stock-CAMB ΛCDM+ΔNeff MCMC proxy on two frozen dataset combinations (176,240 + 132,949 = 309,189 samples; third Planck-only run still accumulating at R̂−1∼0.05), (ii) NaMaster pseudo-Cℓ pipeline validation on synthetic ΛCDM polarization skies (Nside=512, ACT-like fsky=0.32, 500 MC), (iii) spectator-ALP consistency check using the published Eskilt–Komatsu joint WMAP+Planck β=0.342°±0.094° as the headline observational anchor. Scope is rigorously disclaimed: the stock CAMB run is NOT a spin-torsion theory module; the NaMaster validation is NOT a competitive sky detection; the spectator-ALP check is NOT a distinctive ECH prediction (same result arises in GR+identical ALP). The honest "we are not curing the tensions" framing in §II + Conclusions is appropriate given the data.

I verified every load-bearing arithmetic claim in the manuscript. Findings below.

---

### P1B-E1 — none

No fabrication-grade or first-order falsification issues found. The flagged calibration items (S8 correction, c10 battery honest-negative, cosθ-prior cross-check, §VI [0.064, 1.19] envelope, required-C 8.6–160 union-over-box, beta_combined 3.9σ auxiliary-only) all reproduce numerically and are correctly disclaimed in the text.

---

### P1B-M1 — Marginal-tail "+4.3σ" / "−3.6σ" labels in Table II still risk being read as frequentist tensions despite fn. (a)

Pass-1 read of pp. 5 + 9 + Table II row labels: `w_0  −0.8122 ± 0.0436  (marg.-tail, +4.3σ)` and `w_a  −0.6666 ± 0.1864  −3.6σ from 0`. Footnote (a) attached to w0 says explicitly this is "posterior-tail extrapolation distance only, not a Bayes-factor or ln B exclusion and not a frequentist tension." Good — that is the right disclaimer. BUT: the w_a row reuses the bare "−3.6σ from 0" string with no analogous footnote attached, and the §V.B prose at L981 reuses the bare "$w_0$ departs by $+4.3\sigma$ and $w_a$ departs by $-3.6\sigma$" formulation without re-anchoring fn:wcaveat. A skim-reader who sees only the prose paragraph or only the w_a row will export those numbers as frequentist tensions, exactly the failure mode fn:wcaveat is designed to prevent. **Fix**: attach `\footnote{Same marginal-tail caveat as fn.~\ref{fn:wcaveat}.}` to the w_a row entry AND to both "$+4.3\sigma$" and "$-3.6\sigma$" mentions in the §V.B Results prose so the caveat is co-located with every export-vector instance, not only on the first w0 cell.

---

### P1B-M2 — `χ²_total = 14037.4 ± 5.6` vs channel sum `14037.5` arithmetic-rounding artifact noted in footnote (c) is genuine but the σ propagation is unverifiable from what's shown

Table II footnote (c): "The mean-of-total χ² here is GetDist's weighted-sample average over the full posterior, which differs from the sum of the individual-channel means (10.6 + 10983.9 + 3043.0 = 14037.5) by a 0.1-unit arithmetic-rounding artifact; the two are formally identical to within sampling precision." OK — the 0.1 offset is the channels-sum residual and is fine. BUT: the σ for total χ² is reported as ±5.6 while the channel σ's are ±1.8, ±5.3, ±1.6 which combined in quadrature would give √(1.8² + 5.3² + 1.6²) = 5.83, while the reported ±5.6 implies positive correlation between channels. That correlation is physical (cosmological parameter degeneracies couple BAO+CMB+SN residuals) but is nowhere stated. **Fix**: one sentence after the footnote (c) parenthetical: "(channel σ's are not independent: BAO/CMB/SN χ² residuals are positively correlated through shared cosmological parameters; the GetDist total-χ² σ=5.6 reflects that correlation, while the naive quadrature √(1.8²+5.3²+1.6²)=5.83 would assume independence.)"

---

### P1B-M3 — "$w_0+w_a = -1.48 \pm 0.15$ requiring phantom crossing" — phantom-crossing claim is correct but does not state the redshift range over which crossing must occur for THIS chain's pivot

The text at L981–982 says "requiring phantom crossing in the redshift range probed by DESI DR2 BAO + DES-Y5 + Pantheon+." That is the data range, not the equation-of-state crossing redshift. For a CPL w(a) = w_0 + (1−a) w_a, the crossing w(z*)=−1 occurs at a* = 1 − (1+w_0)/w_a → with w_0=−0.812, w_a=−0.667: a* = 1 − (0.188)/(−0.667) = 1.282, i.e. z*=1/a*−1 = −0.22 — IN THE FUTURE, NOT THE PAST. The chain is in the quintom-B regime where w<−1 today and w>−1 in the past, with crossing in the future direction. The phrasing "requiring phantom crossing in the redshift range probed by [data]" is therefore misleading: at the posterior mean the crossing is OUTSIDE the data redshift range. The chain DOES sample posterior tails where crossing falls inside the data range, but the central-value statement is wrong. **Fix**: either compute a*/z* for the posterior mean (above) and add it explicitly with the sign, OR rephrase to "consistent with phantom crossing of w(z)=−1 along the CPL trajectory (the canonical quintom signature)" without the redshift-range qualifier.

---

### P1B-M4 — DES-Y3 weak-lensing S8 reference citation reused across L1047 and the S8 prior label, but Table II quotes σ8 = 0.8057 ± 0.0083 and S8 = 0.8245 ± 0.0089 derived from σ8 (Ωm/0.3)^0.5 — independent arithmetic check

Computing S8 from Table II σ8 = 0.8057 and Ωm = 0.3142 (from same Table): S8 = 0.8057 × (0.3142/0.3)^0.5 = 0.8057 × 1.0235 = 0.8246. Paper quotes 0.8245. Verified to 4 decimal places. ✓ No flag needed on the central value. BUT: the σ propagation S8 = 0.8245 ± 0.0089 implies the σ8 and Ωm uncertainties are propagated correctly only if their correlation is included. From the Table σ_σ8 = 0.0083 and σ_Ωm = 0.0045, the naive uncorrelated propagation gives σ_S8 ≈ √((0.0083×1.0235)² + (0.8057 × 0.5 × 0.0045/0.3)²) = √(0.0850² + 0.00604²)·10⁻³·... let me recompute: ∂S8/∂σ8 = (Ωm/0.3)^0.5 = 1.0235; ∂S8/∂Ωm = 0.5 σ8 / (Ωm × 0.3)^0.5 = 0.5 × 0.8057 / √(0.0943) = 0.5 × 0.8057 / 0.3071 = 1.312; σ_S8(uncorr) = √((1.0235×0.0083)² + (1.312×0.0045)²) = √(0.0085² + 0.0059²) = 0.0103. Paper quotes 0.0089, smaller than the uncorrelated bound — implies negative correlation between σ8 and Ωm in this chain. That is physically expected (CMB acoustic-scale + lensing constrain a degeneracy) but is nowhere stated. **Fix**: one parenthetical at the foot of Table II: "(σ_S8=0.0089 is computed from the full chain covariance; the implied σ8-Ωm correlation ρ<0 is the standard CMB degeneracy.)"

---

### P1B-M5 — Eq. (3) prefactor `α_EM × 8 / (4π) × 1.06` lacks a stated reproducibility cross-check

L1620-something: `β = (α_EM × 8)/(4π) × 1.06 = 4.93 × 10⁻³ rad × 180°/π ≈ 0.28°`. I independently computed: α_EM/(4π) at α_EM=1/137.036 = 5.804×10⁻⁴; × 8 = 4.643×10⁻³; × 1.06 = 4.922×10⁻³ rad = 0.2820°. Paper quotes 4.93×10⁻³ → 0.28° rounded. ✓ Verified. The 0.001 difference in 4.93 vs 4.92 is rounding of α_EM (paper likely used a value to 4–5 sig figs different from 1/137.036). Fine. BUT: the 1.06 factor is identified as "Δφ/fa from the committed EOM integration" — that single number is the load-bearing translator from C×Δφ/fa to β. The text quotes "the committed EOM integration there gives Δφ/fa = 1.06" but provides no integration-cross-check (independent code, alternate ODE solver, Mathematica sanity). **Fix**: add a single-line cross-check in fn., e.g. "(Independent 4th-order Runge–Kutta integration of the same EOM in [code/notebook artifact] reproduces Δφ/fa = 1.06 to 3 sig figs at C_aγ=8, θ_i=1, m=3.9H_0.)" — this is cheap and closes the trust gap on the eq.(3) load-bearing constant.

---

### P1B-m1 — "the pipeline-recovery bias is Δβ̂ ≡ β̂ − β_inj, is −0.032°" at L1267 reads as if -0.032° is the worst-case but it is the canonical-injection bias at β=0.27°

§IV body: "The pipeline-recovery bias ... is −0.032°. ... For β = 0.342° ..., the pipeline recovers 0.302° at template-fit SNR = 25.71; for β = 0", recovered = 0.000°. The pipeline-recovery bias is Δβ̂ = −0.032° at β=0.27° (β̂=0.238°) and Δβ̂ = −0.040° at β=0.342° (β̂=0.302°)." OK — both numbers are present. The abstract on p.1 says "worst-case bias across injections, −0.040°" — also fine. But the §IV opening prose presents "−0.032°" first as if it is THE bias number, then walks to "−0.040°" as the floor. **Fix**: lead the §IV results paragraph with the worst-case floor: "The pipeline-recovery bias Δβ̂ ≡ β̂ − β_inj is, in absolute value, ≤0.040° across the three injection points (0.000° at β=0, −0.032° at β=0.27°, −0.040° at β=0.342°); we carry the worst-case |Δβ̂| = 0.040° forward as the NaMaster systematic floor." Reads cleaner and is the value used downstream.

---

### P1B-m2 — Fig. 3 caption sky-fraction notation "(b)" / "(a)" panel labels conflict with body text

The Fig. 3 caption (p. 7) describes panel (a) as "500-MC mean recovered β̂ vs. injected β_inj ∈ {0, 0.27°, 0.342°}" and panel (b) as "the β_inj=0.27° sky-fraction sweep". The body text §IV at "Sky-fraction sweep" paragraph says "we repeat the β=0.27° injection-recovery exercise at fsky=0.85 (Planck-like) and fsky=0.65 (ACT-DR6-like)." That matches the caption. ✓ However, the figure caption "−0.000°, −0.032°, −0.040°" line lists three biases but the body says the canonical-fsky=0.32 σ_β at the fsky=0.32 point was NOT recorded in the original canonical run, so only the bias-magnitude is plotted at that point. The caption should make this explicit: "(at fsky=0.32 only the mean β̂ is plotted; per-realization σ_β was not recorded in the original canonical run — a dedicated 500-MC rerun, fn. 3, measures σ_β = 0.046°)." Adding the σ_β disclaimer to the caption avoids a reader expecting error bars at the leftmost point.

---

### P1B-m3 — Appendix C `run2_extended` is retained "for the prior-truncation comparison only" but its readout is never reported

Appendix C: "the C_aγ ∈ [1, 30] chain run2_extended (6,840 samples) is retained for the prior-truncation comparison only." Section VI body text says "[1,30] prior of the original extended configuration (which truncated ~28% of the posterior mass above C_aγ=30)" — that 28% IS the prior-truncation comparison readout. So the appendix line "retained for the prior-truncation comparison only" is correct, but the body text never explicitly cross-references "see Appendix C, run2_extended" for the 28% figure. **Fix**: add a single in-line reference: "(28% truncation computed from run2_extended of Appendix C)" — cheap traceability.

---

### P1B-m4 — Abstract uses "no torsion modifications to the Boltzmann equations" as bold text, but then the same disclaimer is repeated verbatim three more times in §I, §III, and the Conclusions

Reader-fatigue issue, not a science issue. The "stock CAMB, no torsion modifications" disclaimer appears in: abstract bullet (1), §I bullet 1, §III scope statement opening, §VII conclusions paragraph 1, and Table III row 1 status. Five copies. **Fix**: keep abstract + §III scope statement (the load-bearing two) and reduce the §I + §VII + Table III copies to "(see §III for the no-torsion-modification scope statement)" pointers. Shaves ~80 words and prevents the appearance of defensive over-explanation that a brutal referee will read as "this paper is anxious about its scope."

---

### P1B-m5 — "Independent cross-validation" Liu et al. ref [14] cited at p. 5 reports ΔAIC = −5.7 to −6.6 favoring torsion, with "torsion parameter itself consistent with zero" — citation is correct but the implication for THIS paper is unstated

The Liu et al. cite is the ONLY independent EC-torsion MCMC cross-check the paper offers. It is cited at p. 5 with the bare statement "torsion preferred by AIC (ΔAIC = −5.7 to −6.6) but with the torsion parameter itself consistent with zero." Two important things go unsaid: (a) does the Liu result CONTRADICT this paper's "ΔNeff consistent with zero" finding, or is it consistent? (Answer: consistent — both find torsion-channel parameters consistent with zero.) (b) Does the AIC preference for torsion in Liu et al. survive in this paper's stack? (Not addressed because the paper explicitly omits ΔAIC.) **Fix**: one sentence after the Liu cite: "Liu et al.'s torsion-parameter null result is consistent with our ΔNeff = 0 null finding; their AIC torsion-preference is not directly comparable to our stack because our ΔAIC/BIC/ln B model-comparison is deferred to nested-sampling follow-up (§V)."

---

### P1B-N1 — none

No nitpicks above-and-beyond the m# items.

---

## Explicit all-clears (deliberate items NOT flagged)

- **S8 correction note**: `0.831 ± 0.018 → 0.827 ± 0.010` chain-recomputed. Verified — Table I caption reads "an earlier version quoted the Planck+BAO+SN S8 marginal as 0.831±0.018; the ±0.018 width could not be traced to any committed analysis, and a direct GetDist pass over the frozen chains gives 0.827±0.010 (132,949 samples), which replaces it in the table." Honest and well-formatted.
- **S8 naive-combination arithmetic** `0.827 ⊗ 0.776 = 0.814 ± 0.009`: independently verified to 0.8139 ± 0.0086 (≈0.814 ± 0.009 at the quoted precision). Chain headline 0.814 ± 0.008 agreement at the 0.01σ level is correct.
- **S8 posterior-overlap integrals** 0.05 (Planck+BAO+SN vs DES-Y3) and 0.12 (full-tension overlay): consistent with the tension distance 2.6σ (independent recompute 2.59σ).
- **c10 robustness battery**: six-configuration sweep with the matched-BB-template honest-negative ("the residual −0.019° is not attributable to the remaining template-shape mismatch ... the battery sharpens only the attribution, not the floor"). This is exactly the right negative-result-disclosure pattern.
- **cosθ-prior c5 robustness** `C_aγ = 17.1 [6.8, 43.4]`: cross-check shows posterior is "essentially unchanged" under flat-θ_i vs cos-θ_i prior — verified consistent with the body's median 20.7 [7.3, 45.6] under the original prior.
- **§VI ALP narrative numbers**: run1=2160 + run2=6840 + run3=720 = 9720 total accepted samples. ✓ Envelope Δφ/fa ∈ [0.01, 0.48]° NOT claimed — paper uses [0.064, 1.19] for the union-over-box (verified from EOM scan artifact c10b_alp_envelope_scan.json description). Required C_aγ at fixed β=0.342°: my independent computation gives 160.61 at Δφ/fa=0.064 and 8.64 at Δφ/fa=1.19 — paper says "≈8.6 up to ≈160". ✓ Required C × Δφ/fa product = 10.279 — paper claims 10.3. ✓
- **β_combined auxiliary**: independent recompute (0.30/0.11² + 0.215/0.074²)/(1/0.11² + 1/0.074²) = 0.241° ± 0.061°, significance 3.93σ. Paper quotes 0.241° ± 0.061° (3.9σ). ✓ Correctly disclaimed as "an upper bound on the true significance" because shared calibration systematics are not accounted for.
- **β_ALP = 0.336° ± 0.10° vs β_obs = 0.342° ± 0.094°**: |Δ|/σ_combined = 0.006/0.137 = 0.04σ — paper quotes 0.04σ. ✓
- **LiteBIRD ~9σ caveat**: |0.342 − 0.27|/√(0.03² + 0.094²) = 0.73σ — paper quotes 0.7σ as "LiteBIRD alone will not separate the spectator-ALP value 0.27° from the current WMAP+Planck central value 0.342°±0.094° by the published measurement's uncertainty" — correctly disclaimed.
- **z_p = 0.27 collision note**: footnote (b) explicitly disambiguates the iter2 chain's pivot redshift z_p=0.27 from the §IV ALP injection angle β=0.27° as "numerically coincident with, and unrelated to". ✓
- **Model-preference disclaimer**: §V.B "Model-comparison statistics: deferred to a dedicated nested-sampling run. We do not report χ², AIC, BIC, or ln B Bayes-factor model-comparison numbers in this paper." Paired with the Savage-Dickey unviability explanation. Correct and honest.
- **w_pivot derivation in fn:wpivot**: every arithmetic step (Cov=−0.00729 → 1−a_p=0.210 → a_p=0.790 → z_p=0.27 → σ_w_pivot=0.0193 → w_pivot=−0.952) independently reproduces. The footnote is a model of "show your work."
- **w0 and wa marginal-tail distances**: (−0.8122+1)/0.0436 = 4.31σ → paper 4.3σ ✓; (−0.6666)/0.1864 = −3.58σ → paper −3.6σ ✓.
- **Correction notes throughout**: every "an earlier draft quoted X; the committed artifact gives Y" footnote (in §VI on Δφ/fa, on [0.17, 0.43] vs [0.064, 1.19], on the EOM-scan grid) is properly formatted as a correction note. Good practice.
- **309,189 sample-count stratification footnote 1**: 176,240 × 0.7 + 132,949 × 0.7 = 216,432 post-burnin; full-tension subset 176,240 × 0.7 = 123,368 vs the in-Fig.1 119,617 getdist-thinned figure — reconciled in the footnote.

---

## Pass 2 — self-critique against `arxiv/paper1b_mcmc_companion.tex`

Re-read of the .tex source confirms:
- All five M# findings remain after seeing the source. M1 (marginal-tail footnote propagation) IS a real fix because fn:wcaveat is anchored only on the w0 row of Table II and on no body-text use site (L981 prose has no fn ref). M3 (phantom-crossing redshift range mischaracterization) holds — L982 says "requiring phantom crossing in the redshift range probed by DESI DR2 BAO + DES-Y5 + Pantheon+" which is incorrect at the posterior mean; the crossing falls in z<0 territory for the iter2 mean. M2, M4, M5 are tightening recommendations that survive source-level inspection.
- m1–m5 confirmed against source. m4 (reader-fatigue from 5× "stock CAMB, no torsion" repetition) verified by grep on the tex — appears at L (multiple anchors per the grep run). m5 (Liu et al. cite has implications-for-this-paper unstated) confirmed at L (Liu cite block).
- Header/preamble auditing: comment block at L116-128 lists prior R-round closures including the R7 series and the R24conf-edited S8 block. The S8 correction note IS present at L890-899 in the form claimed; my arithmetic verification matches.
- Pass-2 did NOT surface any new findings. No E# or N# emerge from the source-level read that the PDF read missed. No falsified deliberate-calibration item.

---

## Summary recommendation

Paper is in strong shape. Companion-to-P1A scope is rigorously disclaimed in five places (one repetition flagged at m4); every load-bearing arithmetic claim I tested reproduces; the honest-negative disclosures in §IV (c10 battery) and §VI (spectator-ALP 25× tuning) are exactly the format brutal referees should reward. Two real issues to fix before next vendor: (M1) propagate fn:wcaveat to the w_a row AND to L981 prose so the marginal-tail caveat travels with every export-vector instance; (M3) correct or remove the "phantom crossing in the redshift range probed by [data]" qualifier at L982 — for the posterior mean (w_0=−0.812, w_a=−0.667) the CPL crossing falls at a*=1.28 (z*=−0.22), in the future, OUTSIDE the data range. Other M/m items are tightening, not blocking.

**Counts: E=0, M=5, m=5, N=0. Verdict: REVISE-MINOR. Path C (full hard fix on M1 + M3, fold M2/M4/M5 + m1–m5 into the same revision).**
