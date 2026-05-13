# P3 v3.1.37 — Adversarial Cosmology-Theory Peer Review (Gemini-3.1-Pro persona)

**Reviewer persona:** Google Gemini-3.1-Pro simulating a senior cosmology theorist with a Hobbs / Vagnozzi / Burke-Spolaor / Madhavacheril profile — pulsar-timing-array spectral characterization (NANOGrav 15-yr + EPTA DR2 + IPTA DR3 combined), gravitational-wave cosmology, SMBHB population synthesis, multi-tracer $f_{\rm NL}$ forecasting, and cross-paper bouncing-cosmology bibliography.

**Date:** 2026-05-13 14:30 PT
**Paper under review:** `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.37 (1,134 lines, ~36 bibitems), revtex4-2 PRD.
**Charter:** Find adversarial cosmology-theory defects beyond what R42 Waves 11–14 / R43 / R44 closures and the CCAI R45–R51 self-review rounds already addressed. Do NOT redundantly raise items already closed (Wave 14-BB header-stratification harmonization, Wave 14-N S>5 absolute-MSE vs percentile policy clarification, Wave 14-O α-bias-enhancement abstract flag, Wave 14-R zero-systematic caveat, Wave 14-II quantitative systematics Fisher recompute, Wave 14-X 100K Jaccard PUSHBACK, Wave 14-RR NANOGrav local-CPU reproduction, Wave 14-VVV empirical α calibration, Wave 14-KKKK Gold+Silver Path-B, Wave 14-NNN 637 cross-survey clusters, Wave 14-III readiness reset, Wave 13-B real-KDE recovery γ=2.567±0.382, NANOGrav 15yr citation, Heinrich2023 anchor, Pipeline-1 1.58× correction). I have read the SSOT before opening this review.

**Verdict TL;DR:** P3 v3.1.37 is the most internally honest of the four papers — the abstract reads like a forensic accounting of every concession the paper has ever made (Path-C rebuild, ACT quarantine, two-tier 378,080/200 stratification, α-empirical/Fisher symmetric-vs-asymmetric envelope, Wave 14-VVV/KKKK estimator-selection rules) and there is virtually no place a reader can extract a single bare number without seeing the caveat in the same sentence. **But the §VI NANOGrav-bounce subsection is a different paper from the rest of the manuscript**, and at the theory level it is the most exposed section in the catalog. The §VI Bayes factor of ~22,000 favoring bounce-over-SMBHB is computed in a way that no PTA-collaboration referee will let stand, the abstract's NANOGrav exclusion narrative double-counts the SMBHB prior, and the cross-paper P1A/P2/P4 self-cite layer that R41 ripped out has left §VI standing on its own without the framework anchor it needs to be cosmology and not a free-spectrum-fitting exercise. **2 BLOCKERs, 6 MAJORs, 7 MINORs, 3 NITs.** The most concerning issue is **G-B1: the bounce-vs-SMBHB Bayes factor is computed by collapsing a 2D posterior to a 1D Gaussian around the marginal $\gamma$ mean, dropping the $\log_{10}A$-axis evidence integral entirely, and using a fully degenerate $4\sigma$-equivalent strength claim that no Bayes-factor practitioner would sign.**

---

## BLOCKER (2) — must address before standalone arXiv submission

### G-B1 [§VI L557, Conclusions item 5 L633] — Bayes factor BF(bounce/SMBHB) ≈ 2.2×10⁴ is computed by Δχ² of point estimates, not posterior evidence; the ">4σ-equivalent" claim is unsupported

The §VI calculation is laid out explicitly:

> "Under flat $\gamma \in [0,7]$, $\log_{10}A \in [-18,-11]$ priors and a **Gaussian posterior approximation** with $\sigma_\gamma \approx 0.382$, the per-hypothesis $\Delta\chi^2$ relative to the posterior mean $\gamma_{\rm obs} = 2.567$ is $\Delta\chi^2_{\rm SMBHB} = (4.33 - 2.567)^2/0.382^2 = 21.31$ ... $\Delta\chi^2_{\rm bounce} = (3.0 - 2.567)^2/0.382^2 = 1.28$, giving a Bayes factor $\mathrm{BF}({\rm bounce}/{\rm SMBHB}) = \exp(-(1.28 - 21.31)/2) = \exp(10.0) \approx 2.2 \times 10^{4}$."

This is **not a Bayes factor.** It is a likelihood ratio at the maximum-likelihood point of a *single* marginal axis, packaged with the name "Bayes factor." A theorist who has read Vagnozzi 2023 (NANOGrav implications for new physics), Mitridate et al. 2023 (PTArcade), or Afzal et al. 2023 (NANOGrav 15yr new-physics paper) will reject this on three independent grounds:

1. **The $\log_{10}A$ axis is silently marginalized at the posterior mean.** Both the matter-bounce and SMBHB predictions are *2D* points in $(\gamma, \log_{10}A)$ space, not 1D points on the $\gamma$ axis. The matter-bounce template at $\gamma = 3.0$ predicts $\log_{10}A_{\rm bounce}$ via the contracting-phase mode-function normalization (Cai 2014 review, Eq. 7; Quintin–Cai–Brandenberger 2014, Eq. 12); the SMBHB at $\gamma = 13/3$ predicts $\log_{10}A_{\rm SMBHB} \sim -14.5$ to $-15.5$ from population-synthesis (Burke-Spolaor 2019, Sec. 5.2; Sesana et al. 2008, Phinney 2001). The paper's "$\log_{10}A = -14.025 \pm 0.380$" recovery is consistent with the SMBHB prior at ~1σ. **The SMBHB hypothesis is therefore favored on the amplitude axis by an amount comparable to what it is "disfavored" on the spectral-index axis**, and the proper 2D Bayes factor must integrate the likelihood × prior over both axes. The paper does neither; it collapses to 1D and then claims a 2D model comparison.

2. **A Gaussian-posterior approximation around the marginal mean is the wrong calculation even on the $\gamma$ axis alone.** The Bayes factor between two parameter values requires the *prior-weighted* likelihood ratio integrated over nuisance parameters, not the likelihood ratio evaluated at the maximum. For a flat prior on $\gamma \in [0, 7]$ and a Gaussian posterior $\mathcal{N}(2.567, 0.382)$, the Savage–Dickey density ratio between $\gamma = 3.0$ and $\gamma = 4.33$ is $\exp[-(1.28 - 21.31)/2]$ at the *peak*, but the posterior probability ratio at *those specific values* is the right quantity for parameter-comparison, not the *model-comparison* Bayes factor between two distinct models. The paper conflates parameter-shift Bayes factors (Verde et al. 2013) with model-comparison Bayes factors (Trotta 2007). These are different quantities.

3. **The ">4σ-equivalent" framing is incoherent.** $\ln \mathrm{BF} \approx 10$ does not correspond to "$> 4\sigma$" in any of the standard Bayes-factor calibrations (Jeffreys 1961, Kass–Raftery 1995, Trotta 2008). $\ln \mathrm{BF} = 10$ is "decisive" on the Kass–Raftery scale (their threshold is $\ln \mathrm{BF} > 10$ for "very strong"), but the frequentist-σ analogue is a domain-specific calibration. A theorist reading "$4\sigma$-equivalent" expects a sampling-distribution argument that is not provided.

**Why this is a blocker.** The §VI subsection is sold in the abstract as the **NANOGrav-side cosmological deliverable of the paper**. The abstract says "the matter-bounce hypothesis is therefore favored over the softened-SMBHB hypothesis at $>\!4\sigma$-equivalent strength" — that is the headline NANOGrav claim. It is computed on a method that any PTA-collaboration referee at Caltech or NANOGrav will mark as "incorrect Bayes-factor calculation, please redo." When the proper 2D-marginalized model comparison is done (integrating likelihood × prior over the SMBHB $\log_{10}A$ prior $\sim \mathcal{N}(-15, 0.7)$ and the bounce $\log_{10}A$ prior fixed at the matter-bounce mode-function prediction), my back-of-envelope says the favored direction stays bounce-over-SMBHB but the BF drops to $\sim 10$–$10^{2}$, with $\ln \mathrm{BF} \sim 2$–$5$ — "moderate" on Kass–Raftery, not "decisive" and certainly not "$4\sigma$-equivalent."

**Disposition: hard fix required.** Three acceptable resolutions, in order of preference:

1. **Do the 2D Bayes factor properly.** Run a Savage–Dickey or nested-sampling model comparison on the NANOGrav 15-yr KDE likelihood comparing $\mathcal{M}_{\rm bounce}: (\gamma, \log_{10}A) = (3.0, \log_{10}A_{\rm bounce-pred})$ vs $\mathcal{M}_{\rm SMBHB}: \gamma = 13/3, \log_{10}A \sim \mathcal{N}(-15.0, 0.7)$ (Burke-Spolaor 2019 informed prior). PTArcade does this natively; the existing `emcee` chain already has the 2D samples. Report the actual $\ln \mathrm{BF}$ on the Kass–Raftery scale and drop the "$\sigma$-equivalent" language. This is ~4 hours of CPU + writeup.

2. **Demote the §VI Bayes factor to a $\Delta\chi^2$ parameter-shift statistic and rename.** Change "Bayes factor $\mathrm{BF}({\rm bounce}/{\rm SMBHB}) \approx 2.2 \times 10^{4}$" to "the per-hypothesis $\Delta\chi^2$ at the marginal $\gamma$ posterior mean prefers $\gamma_{\rm bounce}$ over $\gamma_{\rm SMBHB}$ by $\Delta\chi^2 \approx 20$ on the $\gamma$-axis alone (with the $\log_{10}A$ axis marginalized at its mean; a full 2D model-comparison Bayes factor including the SMBHB amplitude prior is deferred to a stand-alone PTA paper)." Drop the "$> 4\sigma$-equivalent" claim everywhere (abstract, conclusion item 5, §VI body). This is a 30-minute prose fix.

3. **Cite NANOGrav 15-yr new-physics paper's own bounce-vs-SMBHB BF.** Afzal et al. 2023 (the NANOGrav 15-yr new-physics companion paper) reports model-comparison Bayes factors for a suite of new-physics scenarios including domain walls, cosmic strings, and inflation. They do *not* report a matter-bounce BF (they exclude pure power-law new-physics models from the new-physics search), but the framework is correct and their numerical values can be used as a sanity benchmark. Cite Afzal2023 and frame the §VI calculation as an exploratory check that motivates the stand-alone PTA paper.

Option (2) is the cheapest acceptable fix; option (1) is what a PRD submission requires. Right now §VI cannot ship as written.

---

### G-B2 [§VI, Conclusions item 5, Abstract] — Cross-paper P1A/P2/P4 self-cite layer is missing; §VI is unmoored from the framework that motivates it

The R41 round (per SSOT line 43) deliberately removed all `\cite{Golden:2026framework/forecast/chirality}` self-cites and replaced them with primary-source citations (Heinrich2023, Lentati2013, WilsonEwing2012). This was the right call for an arXiv-standalone deliverable. **However, the rip-out has left §VI structurally orphaned in a way that the other three papers' R41 closures didn't suffer.**

Concretely, §VI as currently written:

- Cites `Quintin2014, Cai2014` for the matter-bounce $\gamma = 3.0$ prediction (correct primary sources).
- Cites `Sesana2016, Burke-Spolaor2019` for the SMBHB $\gamma = 4.33$ benchmark (correct primary sources).
- Cites `Heinrich2023` for the $f_{\rm NL}$ methodology (correct).
- **Cites nothing for why a NANOGrav $\gamma = 3.0$ prediction is connected to the $f_{\rm NL} = -35/8$ prediction.** These are the same matter-bounce mode-function calculation in two different observables — Cai et al. 2009 for $f_{\rm NL}$ (contracting-phase three-point), Cai 2014 review for the induced GW spectrum. Without that connection the §VI subsection reads as "we fit a power-law to NANOGrav, the slope happens to be 0.4σ from 3.0, here's a free-spectrum exercise."

This is the **load-bearing cross-paper coupling** that P3 needs:

> The same contracting-phase mode-function calculation (Cai et al. 2009; Quintin–Cai–Brandenberger 2014; Wilson-Ewing 2012) that fixes $f_{\rm NL}^{\rm local} = -35/8$ (the prediction tested in the P2 SPHEREx forecast paper) also fixes the induced-GW power-law spectral index $\gamma_{\rm GW} = 3.0$ (the prediction tested here against NANOGrav 15-yr). These are not two independent predictions; they are two observables of one mode-function calculation. A SPHEREx detection of $f_{\rm NL} = -4.375$ AND a PTA confirmation of $\gamma = 3.0$ would be a consistency check on the matter-bounce mode functions; a SPHEREx null result OR a PTA $\gamma \neq 3$ at $\gtrsim 3\sigma$ would falsify the matter-bounce class in the corresponding observable.

Without this paragraph, a hostile theorist asks "why is the NANOGrav fit in this paper?" and gets no answer. The paper-3 SSOT line 71 says "γ = 3.20 ± 0.42 (0.48σ from bounce prediction γ=3.0), σ(f_NL) 6.1%/16.4% improvements, SPHEREx projection 4.38σ" — that is the framework story the paper is *not* telling.

**Why this is a blocker.** The §VI subsection is sold in the abstract and conclusion as "cosmological applications of the anomaly-selected tracers" — but the NANOGrav fit is not done on the anomaly-selected tracers. It is done on the public NANOGrav 15-yr free-spectrum. The only reason §VI belongs in this paper is the framework coupling to the $f_{\rm NL}$ forecast that DOES use the anomaly tracers. Without the framework paragraph, §VI is an off-topic appendix that a referee will recommend moving to a stand-alone PTA paper. With the framework paragraph (and a one-line P2/P3 cross-reference noting that "the companion focused paper on multi-tracer $f_{\rm NL}$ uses the same mode-function calculation" — which can be a primary-source citation chain, not a `\cite{Golden:2026...}` self-cite), §VI earns its place.

**Disposition: hard fix required.** Insert a short paragraph (4-6 sentences) at the start of §VI titled "Why a NANOGrav consistency check belongs in this paper" or "Framework coupling between $f_{\rm NL}$ and $\gamma_{\rm GW}$." The paragraph should:

1. Cite Cai et al. 2009 (`Cai:2009fn` — already in the bib) for the contracting-phase three-point that gives $f_{\rm NL} = -35/8$.
2. Cite Cai 2014 review (`Cai2014` — already in the bib) for the same mode functions giving $\gamma_{\rm GW} = 3.0$.
3. State the consistency-check logic: same mode-function calculation, two observables, both must agree for the bounce model to survive.
4. State the failure modes: $f_{\rm NL}$ null at SPHEREx OR $\gamma \neq 3$ at $\gtrsim 3\sigma$ in a future PTA dataset → matter-bounce falsification.
5. Frame §VI as the PTA half of this consistency check on the current data, with explicit acknowledgment that the present $\gamma = 2.567 \pm 0.382$ recovery is consistent with both predictions at the present S/N and cannot yet discriminate.

No `\cite{Golden:2026...}` self-cites needed. The framework is in the primary-source bibliography; the paper just needs to assemble it.

---

## MAJOR (6)

### G-M1 [Abstract, §VI L557, Appendix L949] — Real-KDE vs synthetic-power-law shift of $-1.48\sigma$ is genuine and well-flagged, but the abstract still leads with "$\gamma = 3.20 \pm 0.42$" framing in the historical-record context, and §VI's "$+1.13\sigma$ above the posterior mean" should explicitly NOT be called "marginally consistent"

The Wave 13-B update (SSOT 2026-05-01 09:30) correctly replaced the synthetic-power-law fit ($\gamma = 3.20 \pm 0.42$) with the real-KDE recovery ($\gamma = 2.567 \pm 0.382$). The §VI and Appendix paragraphs report the real-KDE values consistently. Two residual framing issues:

1. **The CLAUDE.md / SSOT line 71 / Conclusions item 5 still cites "γ = 3.20 ± 0.42 (0.48σ from bounce prediction γ=3.0)"** as the canonical figure for the lab's cross-paper records. The §VI body correctly says "this real-likelihood result supersedes the synthetic-from-power-law summary-statistic fit ($\gamma = 3.20 \pm 0.42$)" but the abstract doesn't carry the supersession statement, and a reader who lands on the abstract sees no $\gamma$ number at all. **Action:** add to the abstract one sentence — "A direct fit of the matter-bounce power-law GWB template to the NANOGrav 15-yr HD-correlated free-spectrum KDE likelihood (Zenodo 8060824) recovers $\gamma = 2.567 \pm 0.382$, placing the matter-bounce prediction $\gamma_{\rm GW} = 3.0$ at $+1.13\sigma$ above the posterior mean and the SMBHB-only prediction $\gamma = 13/3$ at $+4.6\sigma$ above (excluded)."

2. **"+1.13σ above the posterior mean (marginally consistent at the present S/N)"** — calling $+1.13\sigma$ "marginally consistent" is more concession than the data demand. $+1.13\sigma$ on a one-tailed test is $p = 0.13$, which is plainly consistent, not marginal. The "marginally consistent" framing was appropriate when the cited tension was $\sim 2\sigma$ in the synthetic-fit era; on the real KDE it's not. Rewrite as "$+1.13\sigma$ above the posterior mean (consistent at the present S/N)."

### G-M2 [§VI L557] — The SMBHB γ = 4.33 benchmark is correctly cited but the "$\gamma_{\rm SMBHB} = 13/3$ from circular-inspiral GW emission" derivation is never given; a referee will demand it

The §VI body cites Sesana2016 and Burke-Spolaor2019 for $\gamma_{\rm SMBHB} = 4.33$. The bibliography has both. Neither in the body nor in the appendix is the standard derivation given: a population of circular-inspiral SMBHBs in vacuum gives $h_c(f) \propto f^{-2/3}$ in characteristic strain, which translates to a free-spectrum power-law $\Phi(f) \propto f^{-\gamma}$ with $\gamma = 13/3 = 4.333$ in the timing-residual $\rho_i$ representation. The paper uses $\gamma = 4.33$ throughout as if it were a self-evident benchmark.

Two-line fix: add a footnote at first use — "The benchmark $\gamma_{\rm SMBHB} = 13/3 = 4.33$ assumes a population of GW-driven circular-inspiral SMBHBs in vacuum, giving characteristic strain $h_c \propto f^{-2/3}$ and timing-residual free-spectrum power-law $\gamma = 13/3$ (Phinney 2001; Sesana et al. 2008; Burke-Spolaor 2019, Eq. 17). Environmental coupling (stellar scattering, gas-disk torque) or finite eccentricity reduces $\gamma$ at the lowest frequencies; the 'softened-SMBHB' framing in the literature acknowledges this without specifying a fixed value."

Without this footnote, a reader who doesn't carry the $h_c \to \rho_i$ conversion in their head will think 4.33 is a number we made up. Add the footnote and add `Phinney2001` to the bibliography (Phinney 2001 is the original derivation; one bibitem).

### G-M3 [§VI, Abstract] — Multi-PTA combination (EPTA DR2, PPTA DR3, MeerKAT, IPTA DR3) is deferred but not explained; a referee asks why a 2026 paper uses only NANOGrav 15-yr

Appendix `app:pta_mcmc` line 953 says:

> "Multi-PTA combination (EPTA + PPTA + IPTA), free-spectrum + new-physics joint chains, and bounce-specific spectral-template Bayes-factor model comparison are out-of-scope for the present anomaly-catalog paper and are explicitly deferred to a stand-alone PTA paper."

This deferral is procedurally fine but it leaves a referee asking: "Why not EPTA DR2 (Antoniadis et al. 2023, the EPTA-PPTA-InPTA joint paper) which has comparable sensitivity and was released the same week as NANOGrav 15-yr?" The answer presumably is "scope" but the paper doesn't say so. A two-line addition:

> "We restrict the present consistency check to the NANOGrav 15-yr KDE release because (a) the Zenodo 8060824 free-spectrum KDE pack is Ceffyl-compatible out-of-the-box, (b) the EPTA DR2 (Antoniadis et al. 2023) and PPTA DR3 (Reardon et al. 2023) free-spectrum products are released in different formats requiring per-collaboration likelihood reimplementation, and (c) IPTA DR3 (in preparation) will supersede all three with a combined-Bayesian-analysis product. A multi-PTA combination is deferred to a stand-alone PTA paper alongside the bounce-vs-SMBHB Bayes-factor model comparison flagged in §VI."

Add `Antoniadis2023` (EPTA DR2 GWB paper) and `Reardon2023` (PPTA DR3 GWB paper) to the bibliography — both have arXiv IDs (2306.16214 and 2306.16215). This costs nothing and closes the obvious referee question.

### G-M4 [§V.A L550, Wave 14-II Fisher block] — The internal "σ(f_NL) ≈ 0.07–0.12" Fisher floor is correctly held aside as "internal-consistency check pending an auditable cross-tracer covariance release" but the 3–10× gap with Münchmeyer+2019 needs a load-bearing technical explanation, not the current hand-wave

The Wave 14-II block (§V.A, the long paragraph at L550) reports an internal Fisher floor $\sigma(f_{\rm NL}) \approx 0.067$–$0.116$ across six configurations, with the caveat "reflecting that our multi-tracer Fisher does not damp cross-correlations by realistic photo-z correlation kernels and treats the magnification-bias coupling at linear order only." This is a partial explanation. A theorist with Münchmeyer 2019 open on the desk will ask:

1. **What is the photo-z correlation kernel that the internal Fisher omits?** Münchmeyer et al. (2019) Eq. 22 damps the cross-tracer power spectrum by a factor $\exp[-k_\parallel^2 \sigma_z^2 (1+z)^2 / 2]$ for each tracer in the cross-correlation; the internal Fisher presumably uses the same shot-noise-weighted $C_\ell$ but without this damping. State this explicitly.

2. **At what level does the magnification-bias coupling enter beyond linear order?** Magnification-bias $\delta s$ contributes to the observed clustering through the $5s - 2$ prefactor on the lensing convergence (Bonvin–Durrer 2011). At nonlinear order, magnification-bias couples to $f_{\rm NL}$ through the $\delta s \cdot f_{\rm NL}$ cross-term in the bispectrum (Cabass et al. 2018). The paper says "linear order only" without saying what the linear-order treatment is. Be specific.

3. **Why is the internal-Fisher central value 3–10× tighter than Münchmeyer's consensus?** The paper says "reflecting [the two effects above]" but doesn't quantify which one dominates. A factor of 3–10 is a big gap; if photo-z damping accounts for a factor of 2 and magnification-bias nonlinearity accounts for a factor of 2, that's a factor of 4 — consistent with the low end of the 3–10× gap. If the dominant factor is something else (e.g., the internal Fisher treats the cross-tracer correlation kernel as identity rather than Münchmeyer's anisotropic kernel), say so.

The Wave 14-II block does the right thing by demoting the internal Fisher to "relative-ranking deliverable, not literature-consensus replacement," but the technical gap needs to be load-bearing — three sentences, one citation each — rather than the current "reflecting that..." hand-wave.

### G-M5 [§V.A Wave 14-VVV / 14-KKKK paragraph, L550] — The Gold+Silver 3.17× geomean vs 2.83×±2.03 jackknife discrepancy is named but not explained; reads like the paper is hiding an estimator-selection problem

The Wave 14-KKKK block reports two Gold+Silver bias-ratio estimators:

> "Two related $b$-ratio estimators are reported on the Gold+Silver subset — the per-bin geomean over three signal bins gives 3.17 (no error bar at the per-bin level); the jackknife geomean over 30 footprint realizations gives 2.83 ± 2.03 (1σ jackknife). We adopt the jackknife geomean as the headline because it carries a defensible statistical error budget."

The estimator-selection rule is correctly stated, but the *value gap* (3.17 vs 2.83 — a $\sim 12\%$ shift on the central value) is unexplained. A theorist asks: do the two estimators commute? If the angular bins are symmetric and the jackknife footprint regions are large enough to be statistically independent, the per-bin geomean and the jackknife geomean should agree to a few %. A 12% disagreement says one of three things:

1. **The per-bin geomean is dominated by one outlier bin** (the highest-signal bin), and the jackknife geomean averages over more realizations where the outlier-bin contribution is suppressed. This is the most likely explanation given the small sample.

2. **The jackknife footprint regions are too small** and the 2.83 value carries hidden footprint-systematic bias. Less likely with 30 regions but worth checking.

3. **The Landy-Szalay estimator on the Gold+Silver subset is sensitive to the random-baseline choice** in a way that the full $5{,}384$-sample estimator is not. This is the concerning explanation; if Gold+Silver has a different mean radial selection function than the full sample, the anomaly-window-matched randoms may not be the right baseline.

The paper says the per-bin geomean is "sensitive to the highest-signal bin and is reported as a sanity check on the central value" — that is explanation (1), and it is plausible. But the *quantitative* statement should be: "the highest-signal bin contributes $b_3 = X.XX$ and the lower-signal bins $b_1 = Y.YY, b_2 = Z.ZZ$; the per-bin geomean is therefore weighted toward $b_3$ while the jackknife geomean balances them." Without those three numbers (which are in `pipelines/p1_highz_tracers/outputs/step6_alpha_empirical/alpha_highconfidence_results.json` per the SSOT), a hostile reader thinks the paper picked the lower estimator because it has an error bar that makes the result consistent with zero.

**Action:** add the three per-bin $b$ values in a one-sentence footnote or in the same paragraph. The Wave 14-KKKK closure was a real effort; finishing the explanation of the estimator gap is 30 minutes of work.

### G-M6 [§VI Conclusions item 5, Abstract] — The "both candidates lie on the same side of the posterior; the matter-bounce is favored by the smaller deviation, not by the direction of the deviation" framing is honest but misses the load-bearing point

The §VI body and conclusion item 5 both state:

> "Both candidates lie on the same side of the posterior; the matter-bounce is favored by the smaller deviation, not by the direction of the deviation."

This is technically correct and is the kind of honesty that elevates this paper above the others. But the load-bearing point is **not** that the matter-bounce is favored by smaller deviation — it is that the **NANOGrav 15-yr KDE prefers $\gamma = 2.567 \pm 0.382$, which is genuinely below both the matter-bounce $\gamma = 3.0$ and the SMBHB $\gamma = 13/3$**, suggesting that *neither pure model* is what the data want. The "third option" — a mixed astrophysical+cosmological background, or a cosmic-string contribution, or environmental SMBHB softening — is the actually interesting science here.

The §VI subsection does not discuss this. It picks bounce vs SMBHB and computes a (wrong) Bayes factor. A theorist looking at $\gamma_{\rm obs} = 2.567$ says: "this is suggestive of either a cosmological background that is *softer* than matter-bounce (cosmic strings give $\gamma \approx 1$, smooth turnover in inflationary GW gives $\gamma$ ramping toward zero at low freq), OR a mixed astrophysical-plus-cosmological scenario where the cosmological piece pulls the SMBHB-dominated $\gamma = 13/3$ down toward 2.5."

**Action:** add a one-paragraph "Third-option framing" subsection to §VI noting that the posterior mean is between the two candidate predictions and *below both*, that this can be naturally accommodated by (a) a mixed astrophysical-plus-cosmological background, (b) environmental SMBHB softening (stellar-scattering or gas-disk torque, Sampson–Cornish–McWilliams 2015, Kelley et al. 2017), or (c) a turning-point in the GW spectrum below ~10 nHz from a new-physics scenario other than matter-bounce. Cite Afzal et al. 2023 (NANOGrav 15-yr new-physics) for the suite of alternatives. The matter-bounce prediction is one of the more well-motivated candidates but the data do not yet prefer it over the alternatives. This framing is what a PTA-collaboration referee will *want* to see — it shows the paper is not advocating, it is reporting.

---

## MINOR (7)

### G-m1 [Abstract] — "GR projection / b_φ marginalization" mentioned in CLAUDE.md not in P3 paper itself
CLAUDE.md line 33 says the P2 forecast budget includes "noise-weighted shape mismatch, ε-correction, b_φ marginalization, GR projection" before getting to 3-5σ. P3 §V.A says the headline σ(f_NL) anchors to Heinrich+2024 σ ≈ 0.7 (bispectrum-only) — that is the right external anchor. But the paper does not explicitly say it is *not* including GR projection or b_φ marginalization in the internal Fisher. State that the internal Fisher (Wave 14-II) marginalizes over $\delta b$ (the linear bias amplitude — which absorbs through cross-correlations) but does *not* marginalize over $b_\phi$ (the scale-dependent-bias amplitude in the $f_{\rm NL}$ response, which is the relevant nuisance for the local-shape signal); this is consistent with the "linear order only" magnification-bias treatment flagged in G-M4 but should be said.

### G-m2 [§VI L557, Appendix L925] — The free-spectrum likelihood uses 30 Fourier bins; the matter-bounce template peaks at the lowest bins; report the per-bin contribution to the $\gamma$ posterior
A standard PTA-paper convention is to report which Fourier bins drive the $\gamma$ constraint. For a 30-bin free-spectrum the lowest ~6-10 bins typically dominate. State this explicitly in the appendix: "the $\gamma$ posterior is driven primarily by Fourier bins 1–7 ($f \in [3.2, 22.4]$ nHz); bins 8–30 contribute primarily to the $\log_{10}A$ posterior and have $S/N \lesssim 1$ on the per-bin spectral-index handle."

### G-m3 [§VI Conclusions, Limitations §VI.D L583] — The "Cobaya / enterprise / PTArcade" pipeline-stack disambiguation is unstated
The PTA literature has three standard analysis stacks: enterprise (Ellis et al. 2019), PTArcade (Mitridate et al. 2023), Ceffyl (Lamb et al. 2023). The paper's appendix mentions "Ceffyl-compatible KDEs" but does not state which stack the analysis used. State that the analysis uses a Ceffyl-style log-KDE summed over Fourier bins, not enterprise's full per-pulsar likelihood — this is a real methodological difference (Ceffyl marginalizes over pulsar-noise nuisance parameters at the KDE-construction step rather than at the sampling step) and a referee will want it stated.

### G-m4 [Abstract, §V.A] — "Heinrich+2024 σ ≈ 0.7 (bispectrum-only)" — clarify whether 0.7 is the SPHEREx forecast or the DESI+SPHEREx combined forecast
Heinrich, Doré, Krause 2023 (arXiv:2311.13082, JCAP 2024:074) reports σ(f_NL) ≈ 0.5 for SPHEREx alone (deep+all-sky) and ≈ 0.3 for SPHEREx+DESI combined (their Table 3). The "0.7" anchor used in P3 abstract is the more conservative number that includes additional systematic-degradation budget (per CLAUDE.md line 33 "after systematic budget (noise-weighted shape mismatch, ε-correction, b_φ marginalization, GR projection); 5.2-5.5σ optimistic before GR/b_φ degradation"). The abstract should state "σ(f_NL) ≈ 0.7 after standard systematic budget" to disambiguate from the raw Heinrich+2024 σ ≈ 0.5 (SPHEREx alone) or σ ≈ 0.3 (combined) numbers.

### G-m5 [§V.A L550, Wave 14-VVV paragraph] — The "$\alpha_{\rm jk} = 0.19 \pm 0.65$ consistent with the prior fiducial $\alpha = 0.15$ at $0.06\sigma$" framing
The "0.06σ" agreement is one-tenth of the jackknife dispersion. The text correctly notes this "undersells the precision of the agreement" but the framing risks the opposite reading — that the agreement is suspiciously tight. With $\sigma_\alpha = 0.65$ and a fiducial value of 0.15 (a number chosen post-hoc to be representative of the multi-tracer-improvement literature), an empirical recovery within 0.04 of fiducial is genuinely meaningless — it would also be "consistent" with fiducials 0.0, 0.05, 0.10, 0.20, 0.30. State this: "the central agreement to one-tenth of $\sigma_\alpha$ is statistically consistent with *any* fiducial value in the range $[-0.5, +0.8]$ and should not be over-interpreted as a positive confirmation of $\alpha = 0.15$."

### G-m6 [§VI.D Limitations item 5, L583] — "NANOGrav analysis uses derived free-spectrum values consistent with published results rather than raw timing residual data" — this caveat is fine but obsolete after Wave 13-B
Wave 13-B (SSOT 2026-05-01) replaced the synthetic-derived free-spectrum with the real-KDE Zenodo 8060824 product. The Limitations item 5 still reads as if the synthetic-from-power-law fit were in the paper. Rewrite: "The NANOGrav analysis uses the published 30-Fourier-bin HD-correlated free-spectrum KDE (NANOGrav 2023, Zenodo 8060824) rather than per-pulsar timing-residual data; per-pulsar noise marginalization is therefore taken at the Ceffyl-KDE-construction step rather than at the sampling step. A direct enterprise-style per-pulsar likelihood analysis is deferred to the stand-alone PTA paper."

### G-m7 [§V.A L550] — The empirical α₉₅ CI of [-1.08, +1.46] is well-flagged but the asymmetric σ(f_NL) envelope [5.91, 12.92] is not in the abstract or conclusion
The body correctly maps the α 95%-CI through the linear-in-α Fisher scaling to the asymmetric σ(f_NL) envelope. The abstract and conclusion both report the symmetric "8.27 ± 2.37 (±28.7% fractional uncertainty)" form. **A theorist reading the abstract sees a 28.7% symmetric uncertainty; a theorist reading §V.A sees a [5.91, 12.92] asymmetric envelope. These are not the same statement.** Move the asymmetric envelope into the abstract one sentence — "with an asymmetric 95% CI of [5.91, 12.92] reflecting the asymmetric α-CI mapping."

---

## NIT (3)

### G-n1 [Bibliography] — `Cai:2009fn` formatted with `:` inconsistent with `Cai2014`, `Quintin2014`, `WilsonEwing2012`
Cosmetic but the `:` makes the cite key look like it was imported from a different bib. Either rename to `Cai2009fn` for consistency or accept the inconsistency. Doesn't affect compile.

### G-n2 [Abstract L54] — "$\sim 141\times$ increase over the largest prior single-survey anomaly search (Liang et al. 2023, 2,685 anomalies; ratio computed against the 378,080 point-source-only sub-aggregate so that the comparison is point-source vs. point-source: 378,080/2,685 = 140.8 ≈ 141)"
The verbose parenthetical disclosing the ratio derivation is the right level of caveat. Cosmetic suggestion: move the derivation to a footnote so the abstract reads cleaner; the body sentence retains the explanatory math. Nit only.

### G-n3 [§VI Appendix L949] — "synthetic-from-power-law summary-statistic fit ($\gamma = 3.20 \pm 0.42$; raw fit $3.193 \pm 0.423$)"
Three-significant-figure rounding is fine; the parenthetical "raw fit 3.193 ± 0.423" is reproducibility-tier detail that belongs in a JSON artifact, not the paper. Drop it or footnote it.

---

## Disposition summary

**Counts:** 2 BLOCKERs, 6 MAJORs, 7 MINORs, 3 NITs (total 18).

**Cap implications.** Per the 95%-cap rule (CLAUDE.md `feedback_readiness_oscillation`), this is a cross-vendor R-round simulated by an Anthropic model; it counts toward the eventual genuine cross-vendor closure but does NOT in itself lift the 95% cap. Even if all BLOCKERs and MAJORs are closed, P3 stays at ≤ 99% until a real non-Anthropic-vendor R-round closes clean AND Houston signs off.

**Recommended close-out order (highest ROI first):**

1. **G-B2 framework paragraph** (~30 min): insert the 4-6 sentence "Why a NANOGrav consistency check belongs in this paper" paragraph at the start of §VI. No new compute, no new citations beyond primary sources already in the bib.
2. **G-B1 Bayes-factor demotion (Option 2 path)** (~30 min): rewrite the §VI Bayes-factor block as a $\Delta\chi^2$ parameter-shift statistic, drop the "$> 4\sigma$-equivalent" claim from abstract + §VI + conclusion item 5. Defer the proper 2D model-comparison Bayes factor to the stand-alone PTA paper. This is the cheapest acceptable closure; if the lab wants the Option 1 path (proper PTArcade 2D BF), that's ~4 hours of CPU + writeup.
3. **G-M2 SMBHB γ = 13/3 derivation footnote** (~10 min): one footnote, one new bibitem (Phinney2001).
4. **G-M3 EPTA DR2 / PPTA DR3 scope statement** (~10 min): two lines of text, two new bibitems (Antoniadis2023, Reardon2023).
5. **G-M1 + G-m6 framing harmonization** (~15 min): abstract gets the $\gamma = 2.567 \pm 0.382$ headline; "marginally consistent" → "consistent"; Limitations item 5 obsolete-text update.
6. **G-M6 third-option paragraph** (~30 min): one paragraph in §VI noting the data prefer a softer-than-both spectrum, citing Afzal2023 and Kelley2017 (one new bibitem).
7. **G-M4, G-M5** (~1 hour each): the technical-gap explanations are real work but neither blocks submission; they're MAJOR-tier rigor.
8. **G-m1 through G-m7** (~15 min each): mostly prose tweaks.

**Most concerning theory issue (top of the stack):** **G-B1** — the §VI Bayes factor of ~22,000 is not a Bayes factor. The "$> 4\sigma$-equivalent" claim in the abstract is the §VI's headline NANOGrav deliverable, and it is computed by a method (Δχ² of point estimates with the second posterior axis silently marginalized) that any PTA-collaboration referee will reject on the first read. Either do the proper 2D model-comparison Bayes factor with PTArcade on the existing chain (~4 hours, gives a real number the paper can defend), or demote the §VI calculation to a Δχ² parameter-shift statistic and drop the "$\sigma$-equivalent" language everywhere (~30 minutes, cheap acceptable fix). Until one of those is done, §VI cannot ship as written even though the rest of the paper is in publication shape.

**What I did not raise (already closed):** the Wave 14-NNN 637 cross-survey clusters, Wave 14-VVV α calibration, Wave 14-KKKK Gold+Silver Path-B, Wave 14-II quantitative Fisher recompute, Wave 14-X 100K Jaccard PUSHBACK, Wave 14-RR NANOGrav local-CPU reproducibility, Wave 14-N S>5 absolute-MSE policy, Wave 14-O α-fiducial abstract demotion, Wave 14-R zero-systematic caveat, Wave 14-L SIMBAD-58.8 → 17.8 reframe, Wave 14-BB header-stratification harmonization, R41 Golden:2026 self-cite rip-out, Path-C rebuild closure, ACT-DR6 quarantine and the 378,480 sensitivity-check variant, B-dominant 22.7% calibration-suspect flag, LAMOST 98% blue-excess training-bias lesson. These are all genuinely closed and I read the SSOT before opening this review.

— **Gemini-3.1-Pro (cosmology theorist persona)**, 2026-05-13 14:30 PT.
