# P2 auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13937 chars)
**Wall time**: 364.8s

---

# Referee Report: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

**Manuscript:** P2 | **Journal:** Physical Review D | **Recommendation: REJECT**

---

## Overview

This paper claims to identify a "natural" parameter point ($f_a \sim M_{\rm Pl}$, $m \sim H_0$, $\theta_i \sim \mathcal{O}(1)$, $C_0 \sim \mathcal{O}(1)$) for an ALP that produces $\beta \approx 0.27^\circ$ matching the observed isotropic cosmic birefringence signal. The author explicitly concedes in the body that this model class is well-studied (Fujita et al. 2021, Namikawa et al.) and that "Our contribution is not the model itself." What remains is (i) a parameter identification that is *already in the cited literature*, (ii) a trivial Gaussian summary-likelihood combination of two published numbers, and (iii) an MCMC inference that the paper itself admits is undersampled. This is not a PRD-level contribution. Beyond the threshold-of-novelty issue, the paper has numerous quantitative, internal-consistency, and presentation failures.

---

## ESSENTIAL findings

### P2-E1: Bibliography is broken throughout — every citation is "[?]"
**Pages 1–7.** Literally every citation in the paper renders as `[?]`, including the Eskilt et al. analysis that the headline $3.6\sigma$ number is taken from, the Planck NPIPE and ACT DR6 data citations, the LiteBIRD forecast citation, the Fujita et al. and Namikawa et al. theory citations, and the companion paper. There is **no bibliography section** at all. A PRD submission with zero working references cannot be reviewed for traceability and cannot be accepted under any circumstances.
**Fix:** Provide a complete reference list with arXiv IDs, journals, years; verify every quoted statistic ($0.342\pm 0.094^\circ$, $\sigma(\beta)\approx 0.03^\circ$, etc.) against the cited source.

### P2-E2: Headline "$3.9\sigma$" and the abstract "$0.27^\circ$" prediction are quantitatively inconsistent with each other AND with the dataset choices
**Abstract & §3.2, p. 1–3.**
- The abstract states $\beta_{\rm combined}=0.242\pm 0.061^\circ$ ($3.9\sigma$).
- Recomputing the inverse-variance combination of the *stated* inputs (Planck NPIPE $0.30\pm0.11$, ACT DR6 $0.215\pm0.074$):
  - weights $w_1 = 1/0.11^2 = 82.6$, $w_2 = 1/0.074^2 = 182.6$
  - $\bar\beta = (82.6\times 0.30 + 182.6\times 0.215)/(82.6+182.6) = (24.78 + 39.26)/265.2 = 0.2415^\circ$ ✓
  - $\sigma = 1/\sqrt{265.2} = 0.0614^\circ$ ✓
  - So the arithmetic checks; the central value is $0.242$.
- But the **abstract** claims the prediction $\beta\approx 0.27^\circ$ "consistent with the $3.6\sigma$ isotropic birefringence signal ($\beta_{\rm obs}=0.342\pm 0.094^\circ$)." The headline-prediction value $0.27^\circ$ is **inconsistent at $\sim 0.5\sigma$ with the combined likelihood the paper itself derives** ($0.242\pm 0.061$ vs. $0.27$ — fine), but the paper then pivots to the Eskilt $0.342\pm 0.094$ value (different from the combined likelihood by $1.2\sigma$) to compute the $3.6\sigma$ significance and the $9\sigma$ LiteBIRD forecast.

The paper is **double-dipping**: using one combination ($0.242\pm 0.061$) for parameter inference and a different number ($0.342\pm 0.094$) for "matches the observed signal." These two numbers cannot both be correct simultaneously — Planck NPIPE + ACT DR6 cannot give both $0.242$ and $0.342$ from the same data. The paper waves at this in §3.1 ("differs because it fits the full EB cross-spectrum rather than combining point estimates") but then uses **both** as if they were the same measurement.
**Fix:** Pick one. Justify quantitatively. Restate every $\sigma$ value, the LiteBIRD forecast significance, and the $f_{\rm photon}\times C_0$ derived parameter against that single choice.

### P2-E3: $9\sigma$ LiteBIRD forecast is overstated
**§4, p. 4.** "$0.27/0.03 = 9\sigma$." But:
- The combined-likelihood central value is $0.242$ (not $0.27$). $0.242/0.03 = 8.1\sigma$.
- If using Eskilt's $0.342$, then $0.342/0.03 = 11.4\sigma$, not $9$.
- The "natural prediction range" $0.17$–$0.43^\circ$ (§2.2) implies $5.7\sigma$–$14\sigma$.
- The forecast significance assumes the LiteBIRD systematic floor is zero, which the paper itself contradicts in §7 ("contingent on the self-calibration strategy and systematic error budget").

The "$9\sigma$" claim is presented in the abstract as a clean prediction; it is neither earned nor robust.
**Fix:** Quote the range of forecasts across the natural parameter band; state the systematic floor.

### P2-E4: The "naturalness" argument is internally inconsistent and the abstract misrepresents what is proved
**Abstract & §5, p. 1, 4–5.** The abstract claims "no fine-tuning," with $\theta_i\sim\mathcal{O}(1)$ and $C_0\sim\mathcal{O}(1)$ at "natural prior values." Then §5 explicitly admits:
- At the natural prior point ($\theta_i\sim 1$, $f_a\sim M_{\rm Pl}$, $m\sim H_0$), the ALP contributes $\Omega_\phi \sim 0.17$ — i.e., it is **not a spectator field**, contradicting the entire framing.
- To restore the spectator condition the paper "adopts option (a)": $\theta_i\sim 0.22$, which is a ~$25\times$ tuning relative to the natural prior midpoint.
- The mass tuning $m\sim H_0$ is a cosmological-constant-class fine-tuning, admitted in §5.

So the paper's headline claim is "no fine-tuning" but its own §5 establishes a ~$25\times$ tuning of $\theta_i$ AND a cosmological-constant-class tuning of $m$. The abstract scope note tries to launder this by claiming $f_a$ cancels in $\beta$, but the parameter values used in §2.2 ($\theta_i = 1$, not $0.22$) are exactly the ones §5 says are excluded by the spectator condition. If one consistently uses $\theta_i=0.22$ in §2.2, then $\beta$ drops by a factor of ~5 to $\sim 0.06^\circ$, well below the observed signal — **destroying the headline match unless $C_{a\gamma}$ is correspondingly boosted by ~$5\times$ from its "natural" value $C_{a\gamma}=8$ to $C_{a\gamma}\sim 40$**, which lies *outside* the §2.2 "natural range" $C_{a\gamma}\in[4,12]$.

The paper cannot simultaneously claim (i) spectator condition satisfied, (ii) $\beta\approx 0.27^\circ$ achieved, and (iii) all parameters at natural $\mathcal{O}(1)$ values. The naturalness claim is **falsified by the paper's own §5 calculation**.
**Fix:** Either drop the naturalness claim, or show explicitly with new MCMC enforcing $\Omega_\phi<0.01$ that the $\beta$ prediction survives.

### P2-E5: The $\beta\approx 0.27^\circ$ headline does not match the §2.2 numerical example
**§2.2, p. 2.** The example gives $C_{a\gamma}=8$, $\theta_i=1$, $m\approx 2H_0$, $\Delta\phi/f_a\approx 1.07$, "yielding $\beta = (\alpha_{\rm EM}\times 8/4\pi)\times 1.07 \approx 0.29^\circ$."

Recomputing: $\alpha_{\rm EM}/(4\pi) = (1/137)/(4\pi) = 5.81\times 10^{-4}$ rad. Times $8\times 1.07 = 8.56$ gives $4.97\times 10^{-3}$ rad $= 0.285^\circ$. ✓ (rounded to $0.29^\circ$.)

But the abstract and conclusion quote **$\beta\approx 0.27^\circ$**, with no example shown that produces $0.27^\circ$ exactly. The fiducial case $m=H_0$, $\theta_i=1$ uses $\Delta\phi/f_a\approx 0.65$ (§2.1), which gives $\beta = 8.56\times 0.65/1.07 \times 0.29^\circ \approx 0.18^\circ$, not $0.27^\circ$. So the headline number is neither the §2.1 fiducial value (which gives $0.18^\circ$) nor the §2.2 example value (which gives $0.29^\circ$). What is it?
**Fix:** State exactly which $(m,\theta_i,C_{a\gamma})$ values produce $0.27^\circ$ and use that consistently.

### P2-E6: $f_{\rm photon}\times C_0 = 1.73\pm 0.44$ has no derivation
**§3.2, p. 3, Eq. 5.** This quantity is announced with no definition. What is $f_{\rm photon}$? How does $\beta_{\rm combined}=0.242\pm 0.061^\circ$ map onto $1.73\pm 0.44$? What is the conversion factor? The abstract leans on this as evidence of "order-unity, no fine-tuning" but the quantity is undefined.
**Fix:** Define $f_{\rm photon}$ explicitly; derive Eq. 5 from Eq. 4 with all factors.

### P2-E7: Bayes-factor calculation is undocumented and admits prior dependence destroys its meaning
**§3.4, p. 3.** $\ln B = 5.17$ for prior $[0,1]^\circ$, $4.48$ for $[0,2]^\circ$, $5.86$ for $[0,0.5]^\circ$. With only $720$ accepted samples in Run 3 (and Savage-Dickey requires reliable estimation of the posterior density *at $\beta=0$*, which is in the deep tail), the numerical precision of $\ln B$ is at best $\pm 0.5$ from Monte Carlo error alone — comparable to the "prior-dependence" spread. The paper's own §3.3 admits "small effective sample sizes ($N_{\rm eff}\sim 1000$) limit the precision of tail estimates and evidence calculations." A Bayes factor that the paper itself flags as unreliable should not appear in the abstract.
**Fix:** Either re-run with $\gtrsim 50{,}000$ samples (as the paper itself recommends!) and a proper nested-sampling evidence calculation, or remove from abstract.

### P2-E8: MCMC posteriors in §3.3 contradict the summary-likelihood §3.2 with no reconciliation
**§3.2 vs. §3.3, p. 3.**
- §3.2: $\beta_{\rm combined} = 0.242 \pm 0.061^\circ$ (Planck NPIPE + ACT DR6).
- §3.3 Run 3 ($\beta$ free): $\beta_{\rm free}=0.344\pm 0.096^\circ$.
- These are claimed to use the same data. They differ by $1.0\sigma$ in central value, and the error bar in Run 3 is $1.6\times$ larger than in the summary likelihood. This is mathematically impossible if both used the same two Gaussian likelihoods — the summary-likelihood combination *is* the correct posterior under flat prior. Run 3 must be using *different* data (likely Eskilt alone, $0.342\pm 0.094$, which matches Run 3's output exactly).
**Fix:** State explicitly which dataset each run uses. The current presentation is misleading.

### P2-E9: Figure 1 corner plot is inconsistent with the quoted $C_{a\gamma}\times\theta_i$ posterior
**Fig. 1, p. 4.** The figure marginals show $\theta_i = 1.33^{+0.44}_{-1.1}$ and $C_{a\gamma}=13.4^{+5.6}_{-11}$. Product of central values: $1.33\times 13.4 = 17.8$, not $3.4$. Even taking the modes of the (heavily skewed) marginals, one cannot read $3.4\pm 1.1$ off the figure without computing it from the joint samples, which are not shown. The lower-bound on $\theta_i$ extends to ~$0.2$ and on $C_{a\gamma}$ to ~$2$, with strong anti-correlation along the $C_{a\gamma}\theta_i = $ const direction — yet the product $3.4\pm 1.1$ would imply most of the contour falls along a single hyperbola, which the contours do not show.
**Fix:** Show the actual posterior distribution of the product $C_{a\gamma}\theta_i$, or recompute and reconcile.

### P2-E10: Spectator-density estimate is missing a key factor
**§5, Eq. 11, p. 5.** $\Omega_\phi \approx \frac{1}{6}(m/H_0)^2 (f_a/M_{\rm Pl})^2 \theta_i^2$. Substituting $m=H_0$, $f_a=M_{\rm Pl}$, $\theta_i=1$: $\Omega_\phi = 1/6 = 0.167$. ✓ matches "$\Omega_\phi\sim 0.17$."

But the derivation $\rho_\phi = \tfrac12 m^2 f_a^2 \theta_i^2$ implicitly uses $\rho_{\rm crit}=3 M_{\rm Pl}^2 H_0^2$ (reduced Planck mass) vs. $M_{\rm Pl}^2 H_0^2 / (8\pi)$ (non-reduced) — this needs to be stated. More importantly, for $m\sim H_0$, the field is in slow roll, so $\rho_\phi$ also has a kinetic component; and the potential is $V=m^2 f_a^2(1-\cos\theta_i)$, not $\tfrac12 m^2 f_a^2 \theta_i^2$, which differs by $\theta_i^2/12$ at $\theta_i=1$ (a 10% correction). Minor on its own, but the entire spectator argument hinges on Eq. 11.
**Fix:** State convention; include kinetic energy; use exact $V$.

### P2-E11: "$3.6\sigma$" attribution to Eskilt et al. is unverifiable from the paper
**Abstract & throughout.** The Eskilt et al. value $0.342\pm 0.094^\circ$ corresponds to $0.342/0.094 = 3.64\sigma$ ✓ (so the $3.6\sigma$ number is internally consistent with the quoted error bar). However, the paper provides no traceable citation (see E1), and the description "joint Planck + ACT analysis" needs verification against the actual Eskilt et al. publication; conflating Planck data releases (NPIPE? HFI?) with ACT DR6 is non-trivial.
**Fix:** Provide working citation, exact dataset description, and reproduce the original Eskilt et al. value with quoted error bar.

---

## MAJOR findings

### P2-M1: Abstract conflates two different inferences as "the result"
The abstract presents both $\beta\approx 0.27^\circ$ (theory prediction) and $\beta=0.242\pm 0.061^\circ$ ($3.9\sigma$ data combination) and $\beta_{\rm obs}=0.342\pm 0.094^\circ$ (Eskilt) without clarifying that these three numbers are not the same thing and disagree at the $\gtrsim 0.5\sigma$ level among themselves. A careful reader cannot tell which is "the answer."

### P2-M2: Caγ degeneracy structure undermines the falsifiability claim
§7 claims "sharp falsifiability" at $9\sigma$. But §2.2's "natural range" allows $\beta\in[0.17, 0.43]^\circ$, and §5 further allows $\theta_i$ to be tuned by $25\times$. A null LiteBIRD result $\beta=0\pm 0.03$ excludes only the *specific* parameter point $C_{a\gamma}=8, \theta_i=1, m=2H_0$, not the model class. The "decisive exclusion" claim is overstated.

### P2-M3: Numerical solution of the ALP EOM in §2.1 is undocumented
"$\Delta\phi/f_a \approx 0.65$" (fiducial) and "$\approx 1.07$" ($m=2H_0$) are quoted with no shown solution, no code, no convergence test. For a paper whose entire argument rests on these two numbers, this is unacceptable.
**Fix:** Show $\Delta\phi/f_a$ as a function of $m/H_0$ in a figure; release code.

### P2-M4: Claimed contribution is described inconsistently
§7 admits: "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces $\beta\sim 0.3^\circ$." So the central numerical result is **already in a 2021 paper**. The author then claims novelty in "the specific parameter identification ($f_a\sim M_{\rm Pl}$, $m\sim H_0$) that produces a natural prediction matching the observed signal" — but this *is* exactly what Fujita et al. 2021 did. The "inference framework demonstrating internal consistency" is a trivial inverse-variance combination of two published numbers plus an admittedly undersampled MCMC. PRD requires substantively new physics or methodology.

### P2-M5: "Companion paper" / ECH framework references are dangling
§6, §7, p. 5–6: "companion paper [?]", "Paper I(a) [?]". These are paywall references to unavailable work, on which the "$f_a\sim M_{\rm Pl}$ natural motivation" partially depends. PRD does not accept arguments-by-reference to inaccessible companion manuscripts.

### P2-M6: §6 admits the central motivation is "qualitative"
"this motivation is qualitative—no derivation connects the Holst action to a specific ALP potential or coupling—and the birefringence prediction does not depend on this identification." So §6 is filler that should be removed.

### P2-M7: Tension between "C₀" and "C_aγ" notation
The abstract introduces "photon anomaly coefficient $C_0$"; §2.2 uses $C_{a\gamma}$. Are these the same? Eq. 5 references $f_{\rm photon}\times C_0$. The notation is not unified.

### P2-M8: F(m/H₀) function is introduced in the abstract but never defined
"$\beta = (C_0\theta_i/2) F(m/H_0)$" appears in the abstract scope note but $F$ is never defined in the body. Eq. 2 has no $F$ in it. The reader is left to guess.

### P2-M9: Fig. 2 caption claims "all three are consistent" while displaying obvious shift
Fig. 2 shows the $\beta$-free model centered at ~$0.34$ and the ALP models centered at ~$0.34$ as well, but the green vertical band labeled "Observed" is centered at $0.342$. If §3.2 also gives $0.242$, why is that not shown? The figure cherry-picks the one of the three datasets that agrees best with the ALP model.

### P2-M10: Per-detector polarization angle calibration discussion in §7 is unsupported
§7 cites "active debate about whether residual ~$0.1$–$0.3^\circ$ systematics could arise" with no citation. If the systematic floor is genuinely $0.1$–$0.3^\circ$, then **the entire signal could be systematic** and the paper's headline significance collapses. This needs explicit treatment, not a half-paragraph hedge.

### P2-M11: $f_{\rm NL}=-35/8$ matter-bounce reference is unsupported
§7: "The matter-bounce non-Gaussianity $f_{\rm NL}=-35/8$ provides a complementary and independent test [?]." Reference broken; this is the result the abstract uses to differentiate from "bounce cosmology," but if the only test of the bounce is in a companion paper that we cannot read, it cannot be cited as supporting evidence.

### P2-M12: Inverse-variance combination is invalid if errors are correlated
§3.2 assumes "independent errors" for Planck NPIPE and ACT DR6. But both analyses share calibration with WMAP/Crab nebula, and both depend on the Minami-Komatsu self-calibration assumption. The independence assumption is unjustified; the true combined error bar is larger than $0.061^\circ$.

---

## MINOR findings

### P2-m1: Page 1 has bare `[?]` adjacent to "Planck HFI analysis" in the body of the introduction — this is the abstract's headline citation
### P2-m2: "Caγ is an integer of natural size" — DFSZ has $C_{a\gamma}=8/3$, not $8$; KSVZ has values like $-1.92$. Calling $8$ "DFSZ-type" needs justification (and $8/3$ is not an integer).
### P2-m3: "Planck 2018 parameters ($\Omega_m=0.315, \Omega_\Lambda=0.685, H_0=67.4$ km/s/Mpc)" — these check arithmetically but no source.
### P2-m4: "$\alpha_{\rm EM}\approx 1/137$" — should use the running value or be stated as "at zero momentum" for precision.
### P2-m5: Run 3 with only 720 samples is wholly inadequate for a quoted posterior to 3 significant figures ($0.344\pm 0.096$). At $N=720$, $\sigma/\sqrt{N}\sim 0.004$, so the central value is only good to $\sim 0.01^\circ$.
### P2-m6: §3.3 priors on $\log_{10}(m/{\rm eV})\in[-35,-30]$ correspond to $m\in[10^{-35}, 10^{-30}]$ eV. $H_0\sim 10^{-33}$ eV, so prior spans $\pm 2$ decades around $H_0$. Fine, but state this.
### P2-m7: "Eskilt et al." is mentioned three times in the abstract without an arXiv ID. The reader cannot verify the $3.6\sigma$ headline.
### P2-m8: The acknowledgments state "The author acknowledges the use of AI research assistants during the analysis and manuscript preparation." This is fine to disclose but the manuscript's bibliographic failures (P2-E1) strongly suggest that the AI assistance was not adequately supervised.
### P2-m9: "consumer hardware" computation is fine to disclose but irrelevant to the physics.
### P2-m10: Equation 10 writes "Significance $= 0.27/0.03 = 9\sigma$" — this is not how significance is computed. Significance is a ratio of *expected signal to noise floor*, and ignores prior, model uncertainty, and look-elsewhere effects.
### P2-m11: Eq. 4 quoted as "$3.9\sigma$ from zero": $0.242/0.061 = 3.97\sigma$, so rounded to $3.9\sigma$ ✓.
### P2-m12: Eq. 5: "$f_{\rm photon}\times C_0 = 1.73 \pm 0.44$" → $1.73/0.44 = 3.93\sigma$ from zero ✓ matches Eq. 4's significance, so these are the same quantity expressed differently. Should be stated explicitly.

---

## NITS

### P2-N1: "9σ" appears in the abstract with no decimal — given the $0.27\to 0.242$ ambiguity (E2/E3), should be e.g. "$\sim 8\sigma$" with stated input.
### P2-N2: Title says "Predictions, Constraints, and LiteBIRD Forecasts" — but the "predictions" are post-hoc parameter tuning and the "constraints" are a trivial likelihood combination.
### P2-N3: Page count: 7 pages for a contribution that admits its model is from 2021 — recommended max page count if this were ever publishable would be a 3-page Comment, not a full Article.
### P2-N4: Repeated phrases: "natural", "fine-tuning", "spectator-condition" appear extremely frequently and somewhat repetitively, especially across §5 and §7/§8.

---

## Summary recommendation

# REJECT

This manuscript fails on three independent grounds, any one of which would warrant rejection from PRD. **First**, every citation in the paper is broken (`[?]`), and there is no bibliography section — the headline statistics, including the Eskilt et al. $3.6\sigma$ number, the Planck NPIPE and ACT DR6 measurements, and the LiteBIRD forecast, are untraceable. **Second**, the central "no fine-tuning" claim of the abstract is falsified by the paper's own §5: at the natural-prior parameter point, the ALP contributes $\Omega_\phi\sim 0.17$ (not a spectator), and restoring the spectator condition requires a ~$25\times$ tuning of $\theta_i$, which then reduces the predicted $\beta$ by $\sim 5\times$ below the observed value — destroying the headline match unless $C_{a\gamma}$ is correspondingly tuned outside its stated "natural range." **Third**, the author explicitly admits in §7 that Fujita et al. (2021) "already demonstrated that a Planck-scale ALP naturally produces $\beta\sim 0.3^\circ$," reducing the novel contribution to a trivial inverse-variance combination of two published numbers plus an undersampled MCMC (which the author concedes has "modest" sample sizes that "limit the precision of tail estimates and evidence calculations"). The $9\sigma$ LiteBIRD forecast and $\ln B = 5.17$ Bayes factor in the abstract are both unreliable by the paper's own internal logic. PRD requires substantively new physics, rigorously documented; this manuscript provides neither.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Second Pass

Several issues escaped the initial review. Most consequentially, the corner plot in Fig. 1 contains information that flatly contradicts the paper's central naturalness narrative.

---

## ESSENTIAL findings (new)

### P2-E12: My initial P2-m11 ✓ check was wrong — "3.9σ" headline is itself an arithmetic error
**Abstract & Eq. 4.** Recomputed: $0.242/0.061 = 3.967$. Conventional rounding gives **$4.0\sigma$, not $3.9\sigma$**. To get $3.9\sigma$ exactly, the central value would have to be $0.061 \times 3.9 = 0.238$, not $0.242$. The paper's headline significance is rounded *down* by 0.1σ — a minor arithmetic error in isolation, but it occurs in the abstract on the headline statistic, and my initial review wrongly marked it ✓.

### P2-E13: Fig. 1's mass posterior peaks at $m_a \approx 25\,H_0$, contradicting the entire "$m \sim H_0$" framing
**Fig. 1, p. 4.** The marginal shows $\log_{10}(m_a/\text{eV}) = -31.4^{+1.4}_{-1.2}$. Converting: $\hbar H_0 \approx 1.44\times 10^{-33}$ eV, so $\log_{10}(H_0/\text{eV}) \approx -32.8$. Therefore
$$m_a/H_0 = 10^{-31.4 - (-32.8)} = 10^{1.4} \approx 25.$$
The MCMC posterior **prefers a mass $\sim 25\times$ the Hubble scale**, which puts the ALP firmly in the oscillating regime, where:
- §2.1's "frozen by Hubble friction until $z\sim 1$" picture is wrong;
- $\Delta\phi/f_a$ is no longer $\mathcal{O}(1)$ — for $m\gg H_0$, the field has oscillated many times between recombination and today, and the integrated rotation $\beta = (g_{a\gamma}/2)\int \dot\phi\, dt$ **averages to zero** to leading order;
- §5's energy-density estimate Eq. 11 needs correction (the oscillating-regime scaling is $\rho \propto a^{-3}$);
- The entire "$\beta \sim 0.27^\circ$ predicted at $m\sim H_0$" headline is inconsistent with what the MCMC actually prefers.

The most charitable reading is that $m_a$ does not actually enter the MCMC likelihood (it's prior-dominated), in which case the MCMC isn't testing the ALP model class — it's just refitting $\beta$ with extra unconstrained nuisance parameters. Either reading is fatal to the headline claim.
**Fix:** Show $m_a$ enters the likelihood non-trivially via the ALP EOM integration; if it does, explain why the data prefer $m\gg H_0$ contradicting §2; if it doesn't, drop the MCMC framing as "constraining the ALP model."

### P2-E14: The "natural range $\beta \in [0.17, 0.43]^\circ$" in §2.2 is internally inconsistent — true range is ~5× wider
**§2.2, p. 2.** The paper claims "the prediction spans $\beta \approx 0.17$–$0.43^\circ$ across the natural parameter range $m/H_0 \in [1,3]$, $\theta_i \in [0.5, 2]$, $C_{a\gamma}\in[4,12]$." Using the paper's own formulas:
$$\beta = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi}\cdot\frac{\Delta\phi}{f_a} = 0.0333^\circ \times C_{a\gamma}\times(\Delta\phi/f_a)$$
At the extremes:
- $C_{a\gamma}=4$, $\theta_i=0.5$, $m=H_0$ → $\Delta\phi/f_a \approx 0.32$ (linear scaling from §2.1) → $\beta \approx 0.043^\circ$
- $C_{a\gamma}=12$, $\theta_i=2$, $m=3H_0$ → $\Delta\phi/f_a \approx 2.2$ → $\beta \approx 0.88^\circ$

True range across the stated natural priors is $\sim[0.04, 0.88]^\circ$, which is roughly **a factor of 5 wider in each direction** than the quoted $[0.17, 0.43]^\circ$. The "comfortably bracketing the observed value" claim is correct, but trivially so: a 20× range will bracket *any* observed value in this regime. The natural parameter range *does not select for the observed signal* — it just doesn't exclude it.
**Fix:** Either restrict the quoted natural range to a much smaller, justifiable parameter window (in which case the headline match becomes a coincidence again), or accept that the natural range is wide and drop the "natural prediction" framing.

### P2-E15: §2.1 fiducial and §2.2 fiducial use *different* $m$ values, yielding two different predictions, neither of which is the abstract's $0.27^\circ$
**§2.1 vs §2.2, p. 2.**
- §2.1 fiducial: $m=H_0$, $\theta_i=1$, $\Delta\phi/f_a \approx 0.65$. With $C_{a\gamma}=8$: $\beta = 0.0333 \times 8 \times 0.65 = 0.173^\circ$.
- §2.2 fiducial: $m=2H_0$, $\theta_i=1$, $\Delta\phi/f_a \approx 1.07$. With $C_{a\gamma}=8$: $\beta = 0.0333 \times 8\times 1.07 = 0.285^\circ \approx 0.29^\circ$.
- Abstract & Conclusion: $\beta \approx 0.27^\circ$.

**There is no parameter point in the paper that produces $0.27^\circ$.** The headline number is between the two fiducials, possibly interpolated, but is never derived. This is the central numerical claim of the paper.
**Fix:** Pick one fiducial; document it.

---

## MAJOR findings (new)

### P2-M13: Bayes factor "prior-dependence" is mathematically trivial and uninformative
**§3.4, p. 3.** The three quoted values are $\ln B = 5.86, 5.17, 4.48$ for prior ranges $[0, 0.5]^\circ, [0,1]^\circ, [0,2]^\circ$. The successive differences are:
- $5.86 - 5.17 = 0.69 \approx \ln 2$
- $5.17 - 4.48 = 0.69 \approx \ln 2$

This is **exactly** what one expects from the Savage-Dickey density ratio $B = p_{\rm prior}(0)/p_{\rm post}(0)$: when the prior is uniform with range $R$, $p_{\rm prior}(0) = 1/R$, so $\ln B$ shifts by $-\ln(R_2/R_1)$ when changing the prior range. The "prior dependence" therefore contains **no information about how robust the evidence is** — it just reflects the fact that broader priors give smaller $p_{\rm prior}(0)$. The author presents this as a hedge ("indicative; prior-dependent") but it is in fact a *trivial* prior dependence that does not constrain the evidence at all. A genuinely robust Bayes factor would use a physically motivated prior (e.g., truncated normal centered on theory expectation) and report the sensitivity to *non-trivial* prior choices.

### P2-M14: Both $\theta_i$ and $C_{a\gamma}$ posteriors are essentially prior-dominated; MCMC adds nothing
**Fig. 1 vs §3.3 priors.**
- Prior on $\theta_i$: flat on $[0.01, \pi]$. Prior median: $\sim 1.57$. Posterior central: $1.33^{+0.44}_{-1.1}$. Update: $\sim 0.2$ shift, within the posterior width.
- Prior on $C_{a\gamma}$: flat on $[1, 30]$. Prior median: $15.5$. Posterior central: $13.4^{+5.6}_{-11}$. Update: $\sim 2$ shift, well within the posterior width.

**The MCMC posteriors on $\theta_i$ and $C_{a\gamma}$ individually are within $\sim 0.1\sigma$ of their priors.** Only the *product* $C_{a\gamma}\theta_i = 3.4 \pm 1.1$ is data-constrained, and that is equivalent to the simple summary-likelihood for $\beta$ (since $\beta \propto C_{a\gamma}\theta_i$ in the linear-regime approximation). The MCMC is not providing independent inference; it is reformulating $\beta = 0.34\pm 0.10$ as a product of two unconstrained parameters and presenting the marginals as if they constrain the ALP model.

### P2-M15: $M_{\rm Pl}$ convention in Eq. 11 unspecified — answer changes by factor of $8\pi$
**§5, Eq. 11, p. 5.** $\Omega_\phi = (1/6)(m/H_0)^2(f_a/M_{\rm Pl})^2\theta_i^2$. This uses $\rho_{\rm crit} = 3 H_0^2 M_{\rm Pl}^2$, which is correct only if $M_{\rm Pl}$ is the **reduced** Planck mass ($\approx 2.4\times 10^{18}$ GeV). If the **standard** Planck mass ($\approx 1.2 \times 10^{19}$ GeV) is intended, then $\rho_{\rm crit} = (3/8\pi)H_0^2 M_{\rm Pl}^2$ and Eq. 11 gains a factor of $8\pi \approx 25$ — giving $\Omega_\phi \approx 0.007$ at $\theta_i=1$, which **automatically satisfies the spectator condition with no tuning**. The convention is never stated. The entire $25\times$ fine-tuning claim in §5 is contingent on which $M_{\rm Pl}$ is used, and the headline naturalness claim swings completely depending on convention.

### P2-M16: $\Omega_\phi \sim 0.17$ as dark-energy contribution wrongly described as "allowed at the ∼10% level"
**§5, p. 5.** "reinterpreting the ALP as a dark-energy-like component contributing $\Omega_\phi \sim 0.17$ ... allowed under ΛCDM at the $\sim 10\%$ level by current constraints." 

$0.17$ is **25%** of $\Omega_\Lambda = 0.685$, not 10%. Current CMB+BAO+SNe constraints on $\Omega_\Lambda$ are at the $\pm 0.01$ level — well below a 0.17 modification. A $\Omega_\phi = 0.17$ slow-roll component is *not* allowed by current data; it would require a complete refit of cosmological parameters and would likely worsen $H_0$, $S_8$, and BAO tensions. The casual dismissal "allowed at ∼10% level" is wrong.

### P2-M17: Null LiteBIRD result would falsify the *observed signal*, not the *ALP model* — exclusion framing is wrong
**§4, p. 4.** "If LiteBIRD measures $\beta = 0\pm 0.03^\circ$, the ALP explanation is excluded at $9\sigma$." But Planck+ACT currently report $\beta \neq 0$ at $\sim 3.6\sigma$. If LiteBIRD measures zero at $\pm 0.03$, the primary inference is that the existing signal is a systematic — which falsifies *any* astrophysical explanation, not just the ALP. The cleaner framing would be "if LiteBIRD confirms the signal at the ALP-predicted amplitude, the ALP model is favored; if LiteBIRD measures a value inconsistent with $0.27^\circ$, the specific parameter point is excluded but the model class survives by retuning $C_{a\gamma}\theta_i$." The current framing overclaims the falsifiability scope.

### P2-M18: Run 2's $\beta$ posterior visible in Fig. 1 ($0.324\pm 0.099^\circ$) is never quoted in body text
**Fig. 1 vs §3.3.** The §3.3 text quotes Run 1's $\beta_{\rm ALP} = 0.336\pm 0.107^\circ$ and Run 3's $\beta_{\rm free} = 0.344\pm 0.096^\circ$, but Run 2 (the *extended* model with $C$ free, which is the focus of Fig. 1) gives $\beta = 0.324\pm 0.099^\circ$ — visible in Fig. 1's $\beta$ marginal title. This value is **never quoted in the body**, even though Fig. 2 plots all three posteriors. A reader trying to extract Run 2's $\beta$ must read it off the figure title.

### P2-M19: "$25\times$ fine-tuning" in §5 has no consistent derivation
**§5, p. 5.** "$\theta_i \sim 0.22$ (a ~25× fine-tuning of the initial misalignment relative to the natural prior midpoint)." Possible interpretations:
- $\theta_{\rm prior\,midpoint}/\theta_{\rm allowed} = (\pi/2)/0.22 \approx 7.1\times$
- $(\theta_{\rm midpoint}/\theta_{\rm allowed})^2 = 50\times$ (energy-density tuning)
- Prior volume reduction $\pi/0.22 \approx 14\times$
- $1/\theta_{\rm allowed}^2 = 1/0.0484 \approx 21\times$

None of these is $25$. The "$25\times$" number cannot be reproduced from any natural definition.

---

## minor findings (new)

### P2-m13: "$\sqrt{0.05}$" choice for the spectator threshold is arbitrary
**§5, p. 5.** Why is "spectator" defined as $\Omega_\phi < 0.05/6 \approx 0.008$? The threshold $0.05$ is not derived from any constraint; it is asserted. A different threshold (e.g., $0.01$) would give a $\sim 50\times$ tuning instead of $25\times$.

### P2-m14: Fig. 1's $\theta_i$ marginal title "$\theta_i = 1.33^{+0.44}_{-1.1}$" is misleadingly presented as central+error
The asymmetric errors with $-1.1$ from a central of $1.33$ implies the lower 1σ goes to $\theta_i = 0.23$ — the distribution is heavily skewed, and quoting $1.33$ as if it were a peak is not representative. Reading the marginal shape, the mode appears to be at small $\theta_i$. This suggests the $\theta_i$ posterior is concentrated against the prior boundary $\theta_i = 0.01$, raising the possibility that the data prefer arbitrarily small $\theta_i$ (with correspondingly large $C_{a\gamma}$) and only the prior keeps the parameters at $\mathcal{O}(1)$.

### P2-m15: Eq. 2 uses $g_{a\gamma} = \alpha C_{a\gamma}/(2\pi f_a)$; this is one of several conventions in the literature
The Fujita et al. convention sometimes differs by factor of 2. Without a working citation (P2-E1), the reader cannot check which is used; the predicted $\beta$ could be off by factor of 2 depending on which convention the data analyses used.

### P2-m16: Run 1 with "$C=8$ fixed" implicitly fixes $\theta_i C_{a\gamma}$ to vary only through $\theta_i$, but Run 1's quoted $\beta_{\rm ALP} = 0.336$ requires $\theta_i \sim 1.05$ (using $\Delta\phi/f_a \approx \theta_i \times 0.65$ at $m=H_0$); no $\theta_i$ marginal for Run 1 is shown to verify.

### P2-m17: Table 1's "Samples" column gives accepted samples (720, 2160, 6840). These are not "samples" in the usual MCMC sense (which would be steps); the distinction matters for $N_{\rm eff}$ but is not explained.

---

## Nits (new)

### P2-N5: "Bare $\theta_i$" appears with subscript-on-Cay implicit alignment, but Eq. 8 ($C_{a\gamma}\times\theta_i = 3.4\pm 1.1$) and the abstract's "$C_0 \theta_i$" use inconsistent notation.

### P2-N6: Fig. 2 caption claims posteriors are "consistent with each other and with the observed value $\beta_{\rm obs}=0.342\pm 0.094^\circ$" — but the green band shown in Fig. 2 looks centered at the *summary-likelihood* value $\sim 0.24$, not at Eskilt's $0.34$. (Hard to tell from the figure without higher resolution.) This is another instance of the dataset confusion (P2-E2).

### P2-N7: Eq. 11's "$\rho_\phi \approx \frac{1}{2}m^2 f_a^2 \theta_i^2$" omits the kinetic energy in the slow-roll regime. For $m\sim H_0$ slow-roll, $\dot\phi/m \sim f_a\theta_i$, so kinetic $\sim$ potential — a factor-of-2 missing from the energy density.

---

## Revised assessment

The most damaging new finding is **P2-E13**: the MCMC posterior on $m_a$ peaks at $m_a/H_0 \approx 25$, not at $\sim 1$. This either (a) puts the ALP in the oscillating regime where $\beta \to 0$, contradicting the headline; or (b) reveals that $m_a$ doesn't enter the likelihood, in which case the MCMC is theater. Combined with **P2-M14** (both $\theta_i$ and $C_{a\gamma}$ are prior-dominated), this means the entire MCMC analysis is reducible to the trivial summary-likelihood for $\beta$.

The rejection recommendation stands and is reinforced. The paper's "natural parameter identification" is undermined by its own MCMC, its naturalness range is cherry-picked by a factor of 5, its Bayes factor's prior-dependence is mathematically trivial, and its central numerical prediction $0.27^\circ$ corresponds to no calculation actually in the manuscript.