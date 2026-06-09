# P2 auto-2026-06-09_1042pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17050 chars)
**Wall time**: 289.8s

---

# Referee Report: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

**Manuscript:** P2 | **Recommendation will follow at end**

---

## Overview

This paper claims that a spectator ALP with $f_a \sim M_{\rm Pl}$, $m \sim H_0$, and $\theta_i \sim \mathcal{O}(1)$ naturally produces the observed cosmic birefringence $\beta \approx 0.27°$. The author performs a Gaussian summary-likelihood combination of Planck NPIPE and ACT DR6, runs MCMC, computes a Bayes factor, and forecasts LiteBIRD sensitivity. The result is presented as "no fine-tuning" and a "9σ falsifiable test."

The paper has fundamental problems with novelty, internal arithmetic consistency, broken citations, and—most damningly—the author's own Sec. 5 calculation contradicts the central naturalness claim of the abstract.

---

## ESSENTIAL FINDINGS

### P2-E1. Broken citations throughout — every reference rendered as "[?]"
**Pages 1–6, throughout.** Literally every \cite command in the manuscript renders as `[?]`. Examples:
- p.1: "The Planck HFI analysis [?] reported..."
- p.2: "in the conventions of ?"
- p.2: "Planck NPIPE [?]", "ACT DR6 [?]"
- p.4: "LiteBIRD is projected to achieve σ(β) ≈ 0.03° [?]"
- p.5: "companion Paper I(a) [?]"
- p.6: "see the companion paper [?]", "Namikawa, Murai & Naokawa [?]"
- p.6: "The matter-bounce non-Gaussianity ... [?]"
- p.6: "well-studied in the literature [?]"

There is **no bibliography section** in the rendered PDF. A PRD submission with zero working references is not reviewable on its face. **Fix:** include a complete bibliography and verify each citation compiles.

### P2-E2. Sec. 5 internally contradicts the abstract's central naturalness claim
**Page 5, Sec. 5.** The author derives $\Omega_\phi \approx \frac{1}{6}(m/H_0)^2 (f_a/M_{\rm Pl})^2 \theta_i^2$ and finds **$\Omega_\phi \sim 0.17$** at the headline parameter point ($f_a \sim M_{\rm Pl}$, $m \sim H_0$, $\theta_i \sim 1$). To recover the spectator condition $\Omega_\phi \ll 1$, the author admits requiring $\theta_i \sim 0.22$ — a **~25× tuning** of the initial misalignment.

But the abstract states: "the match to the observed signal depends on $\theta_i$ and $C_0$ both being $\mathcal{O}(1)$ at their natural prior values" and the headline number $\beta \approx 0.27°$ is computed in Sec. 2.2 with $\theta_i = 1$. The abstract claim "without … fine-tuning" is directly contradicted by the author's own energy-density calculation. The disclaimer "cosmological-constant-class tuning" is rhetorical sleight of hand — a 25× tuning of an ALP misalignment angle is a tuning of an ALP parameter, not of $\Lambda$.

Furthermore, Sec. 2.2 uses $\theta_i = 1$ to derive $\beta \approx 0.29°$; if the spectator-consistent value is $\theta_i \sim 0.22$, then $\beta$ scales linearly with $\Delta\phi \propto \theta_i$ (in the small-field regime) and the prediction collapses to $\beta \sim 0.06°$, **inconsistent with the data**.

**Fix:** Either (i) abandon the "no fine-tuning" framing and present the model honestly as requiring a 25× misalignment tuning, OR (ii) abandon the strict spectator framing and address the $\Omega_\phi \sim 0.17$ dark-energy-like component against ΛCDM constraints quantitatively (not by hand-waving "allowed at ∼10%").

### P2-E3. The abstract's headline σ values are inconsistent with each other
**Page 1, Abstract.** The abstract cites the Eskilt et al. signal as "**3.6σ** ($\beta_{\rm obs} = 0.342 \pm 0.094°$)." Recompute: $0.342/0.094 = 3.64σ$. OK.

Then states the author's own combined fit is "$\beta = 0.242 \pm 0.061°$ (**3.9σ from zero**)." Recompute: $0.242/0.061 = 3.97σ$. OK.

But: the author's combined value $0.242°$ is **more than $1σ$ lower** than Eskilt's $0.342°$. The author opens by celebrating consistency with Eskilt's signal, then derives a value that is in mild tension with it, and never reconciles this. Worse, the inputs to the combination (Planck NPIPE $0.30 \pm 0.11°$ and ACT DR6 $0.215 \pm 0.074°$, p.2) overlap heavily with the data Eskilt et al. analyzed jointly — these are **not independent measurements**, so the inverse-variance combination in Eq. 3 is statistically illegitimate. **Fix:** justify independence of NPIPE and ACT DR6 birefringence measurements explicitly, or remove Eq. 4 and Sec. 3.2.

### P2-E4. Recomputation of summary-likelihood combination
**Page 3, Eq. 4.** Inverse-variance combination of $0.30 \pm 0.11°$ and $0.215 \pm 0.074°$:
- weights: $1/0.11^2 = 82.6$, $1/0.074^2 = 182.6$
- $\beta_{\rm combined} = (82.6 \times 0.30 + 182.6 \times 0.215)/(82.6+182.6) = (24.78 + 39.26)/265.2 = 0.2415°$
- $\sigma_{\rm combined} = 1/\sqrt{265.2} = 0.0614°$

So $0.242 \pm 0.061°$ is arithmetically correct **conditional on independence**, which is not justified (see E3). Flag the independence assumption.

### P2-E5. "9σ" LiteBIRD forecast is an apples-to-oranges sigma
**Page 4, Eq. 10.** The forecast computes $0.27°/0.03° = 9σ$ — this is the significance for *detecting a signal of amplitude 0.27°* against statistical noise alone. But the LiteBIRD systematic floor on $\beta$ is dominated by self-calibration ambiguity (which the author acknowledges in Sec. 7), not statistical error. A 9σ detection claim from a purely statistical $\sigma(\beta) = 0.03°$ — with the author themselves noting "depending on the self-calibration strategy and systematic error budget" — is overclaim. The abstract advertises "9σ" without this qualification.

**Fix:** either revise to "9σ statistical, systematics-limited" with explicit systematic budget, or quote a realistic effective sensitivity.

### P2-E6. Eq. 2 arithmetic disagrees with abstract headline
**Page 2, Sec. 2.2.** Author computes:
$\beta = (\alpha_{\rm EM} \times 8 / 4\pi) \times 1.07$
$= (1/137 \times 8 / 4\pi) \times 1.07$
$= 0.00465 \times 1.07 = 0.00497$ rad
$= 0.285° \approx 0.29°$. OK.

But the abstract states the prediction as $\beta \approx 0.27°$. Where does $0.27°$ come from? It is not derived anywhere in the paper. The body gives $0.29°$ for the fiducial case. This is a small numerical inconsistency but the headline number should match the derivation. **Fix:** unify.

### P2-E7. "Effective photon coupling $f_{\rm photon} \times C_0 = 1.73 \pm 0.44$" is undefined
**Page 3, Eq. 5.** The quantity $f_{\rm photon} \times C_0$ has no definition in the paper. It is introduced without a defining equation. It cannot be the standard $g_{a\gamma}$ (which has units of inverse mass). It cannot be $C_{a\gamma}$ alone (Eq. 2 uses $C_{a\gamma} \approx 8$, not 1.73). The number is not connected to any model parameter. This appears to be a fitted normalization with no physical interpretation, presented as if it were a meaningful "order-unity" coupling. **Fix:** define $f_{\rm photon}$ explicitly with an equation, or remove this claim.

### P2-E8. Bayes factor is sample-size–limited but quoted as load-bearing
**Page 3, Sec. 3.4.** The author admits Run 3 ($\beta$-free model used for the Savage-Dickey null comparison) has **only 720 samples**, with $N_{\rm eff} \sim 1000$. A Savage-Dickey computation at the prior-edge $\beta = 0$ requires resolution of the posterior density at a 3.9σ tail — which from 720 samples has an irreducible Monte Carlo error on $\ln B$ of order unity. The reported $\ln B = 5.17$ has uncertainty comparable to the prior-dependence already noted (4.48 to 5.86). The author calls it "indicative" but the abstract still reports it as a load-bearing number. **Fix:** rerun Run 3 with $\geq 50{,}000$ samples (as the author concedes is needed) before claiming $\ln B = 5.17$ in the abstract.

### P2-E9. Novelty claim is honestly disclaimed but then re-asserted
**Page 6, Sec. 7.** The author writes: "We emphasize that the ALP birefringence model class is well-studied … Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces $\beta \sim 0.3°$, and Namikawa, Murai & Naokawa provide superior ALP mass constraints…"

This is fatal for a PRD submission. If the central result ($\beta \sim 0.3°$ from Planck-scale ALP) was already demonstrated in 2021, and there are stronger constraints in Namikawa et al., what is this paper's contribution? The author claims the contribution is "the specific parameter identification ($f_a \sim M_{\rm Pl}$, $m \sim H_0$)" — but this is exactly the Fujita et al. (2021) identification. **PRD requires novelty.** The Gaussian summary-likelihood combination of two public numbers is a five-line calculation, not a PRD-worthy result.

### P2-E10. MCMC parameter $\theta_i = 1.33^{+0.44}_{-1.1}$ (Fig. 1) is inconsistent with spectator requirement
**Page 4, Fig. 1 + Page 5, Sec. 5.** The MCMC posterior shows $\theta_i = 1.33$, but the spectator condition requires $\theta_i \sim 0.22$ (Sec. 5). The MCMC is therefore sampling parameter space that **violates the model's own self-consistency**. No prior cut on the spectator condition is applied. The $C_{a\gamma} \times \theta_i = 3.4 \pm 1.1$ result (Eq. 8) is also sampled in a regime where the ALP is dark-energy-like, not spectator. **Fix:** redo MCMC with a prior enforcing $\Omega_\phi < $ some threshold, and report the implications for the $C_{a\gamma} \times \theta_i$ posterior.

---

## MAJOR FINDINGS

### P2-M1. Range $\Delta\phi/f_a \approx 0.2$–$1.1$ but then $1.07$ used for fiducial
**Page 2.** Eq. 1 quotes the range $\Delta\phi/f_a \approx 0.2$–$1.1$ for $m/H_0 \in [0.5, 3]$. Then in Sec. 2.2, the fiducial value $\Delta\phi/f_a \approx 1.07$ is used for $m \approx 2H_0$ — which sits at the upper edge of the range. This is cherry-picking the parameter that maximizes the prediction. **Fix:** report $\beta$ for the central case $m = H_0$ (which gives $\Delta\phi/f_a \approx 0.65$, hence $\beta \approx 0.18°$, inconsistent with data at $1.7σ$).

### P2-M2. Sec. 2.1 redundancy
**Page 2.** The sentence "For $m \sim H_0$ and $\theta_i \sim \mathcal{O}(1)$, the field is frozen by Hubble friction during radiation and matter domination and begins rolling at $z \sim \mathcal{O}(1)$ when $H(z) \sim m$" appears **twice** in Sec. 2.1, once in the second paragraph and again as a near-verbatim duplicate of the first paragraph. **Fix:** remove duplicate.

### P2-M3. "Caγ ∼ O(1)–O(10)" then $C_{a\gamma} = 8$ called "natural DFSZ-type"
**Page 2.** Saying "typically $\mathcal{O}(1)$–$\mathcal{O}(10)$" and then choosing 8 to fit the data is parameter tuning dressed up as naturalness. DFSZ models have specific integer values (e.g., 2/3, 8/3 depending on choices) — the assertion that "$C_{a\gamma} = 8$" is "DFSZ-type" needs a citation and derivation. Without it, this is fitting a free parameter and labeling it natural.

### P2-M4. Fig. 1 caption claim does not match figure content
**Page 4, Fig. 1.** Caption says "$C_{a\gamma} \times \theta_i$ is centered at $3.4 \pm 1.1$." But the figure shows marginal posteriors $\theta_i = 1.33^{+0.44}_{-1.1}$ and $C_{a\gamma} = 13.4^{+5.6}_{-11}$. Product of medians: $1.33 \times 13.4 = 17.8$, not 3.4. The author must be quoting the product on a per-sample basis with strong anti-correlation — but the figure shows $\theta_i$ posterior peaking near 0.5–1 (visually), while $C_{a\gamma}$ peaks near 5. Even taking the lower edges: $0.5 \times 5 = 2.5$. The arithmetic does not close from the figure alone. **Fix:** show the $C_{a\gamma} \times \theta_i$ posterior directly or reconcile with the marginals.

### P2-M5. $C_{a\gamma} = 13.4^{+5.6}_{-11}$ from MCMC violates "natural O(1)" claim
**Page 4, Fig. 1.** The MCMC posterior peaks at $C_{a\gamma} = 13.4$, with a prior of $[1, 30]$. This is not "$\mathcal{O}(1)$" — it is $\mathcal{O}(10)$ pushed by the data and bounded by the prior. The lower error bar extends to $\sim 2.4$, but the central value is **prior-bounded above**. The "naturalness" framing in the abstract is not supported by this posterior.

### P2-M6. Eskilt et al. value: source unclear
**Page 1 vs. Page 2.** Abstract attributes $\beta_{\rm obs} = 0.342 \pm 0.094°$ to "Eskilt et al. joint Planck + ACT." Sec. 3.1 says "we use the Eskilt et al. joint analysis value." But the reference is broken ([?]) and the actual Eskilt et al. (2023) joint Planck+ACT paper, to my recollection, quotes a value closer to $0.342°$ from Planck-only PR4 analyses, not a joint Planck+ACT result. **Fix:** verify the citation and the quoted value match the cited paper.

### P2-M7. Self-citation to "Paper I(a)" with broken reference
**Page 5.** "the cosmological-constant-class tuning admitted in companion Paper I(a) [?]" — this is a load-bearing argument deflecting fine-tuning concerns to a companion paper, but the companion is not cited. A PRD paper cannot lean on unspecified companion work for its naturalness argument.

### P2-M8. ECH gravity / Holst action paragraph is undermotivated filler
**Pages 5–6, Sec. 6.** The author admits: "this motivation is qualitative—no derivation connects the Holst action to a specific ALP potential or coupling—and the birefringence prediction does not depend on this identification." Then why include it? This is speculation labeled as theoretical context. PRD does not publish qualitative non-derivations. **Fix:** remove Sec. 6 or derive the connection.

### P2-M9. Matter-bounce $f_{\rm NL} = -35/8$ aside is irrelevant
**Page 6.** The matter-bounce non-Gaussianity reference is irrelevant to a paper claiming bounce-independence. It serves only to point to other unpublished work. **Fix:** remove.

### P2-M10. No EB spectrum fit performed
**Throughout.** The paper performs no actual analysis of the EB cross-spectrum. It combines two published $\beta$ values via Eq. 3 and runs MCMC on a Gaussian likelihood over $\beta$. This is a meta-analysis, not a CMB data analysis. The MCMC over ALP parameters is essentially toy: it samples ($\theta_i$, $C_{a\gamma}$, $m$) with the only constraint being the Gaussian likelihood on $\beta$. The "MCMC parameter estimation" framing oversells what is being done.

### P2-M11. "Independent of bounce cosmology" — what does this add?
**Abstract, Pages 1, 6.** The repeated assertion that "this prediction is independent of bounce cosmology" reveals that this paper is part of a series, and the reviewer is being told what the paper is *not* about. PRD readers should not need to know what other papers in the series do; the standalone scope must justify the standalone submission.

### P2-M12. Inconsistent $\beta$ headline values throughout
- Abstract: "$\beta \approx 0.27°$"
- Sec. 2.2: "$\beta \approx 0.29°$" (numerical example)
- Sec. 2.2: "$\beta \approx 0.17$–$0.43°$" (range)
- Sec. 3.2: "$\beta_{\rm combined} = 0.242 \pm 0.061°$" (their fit)
- Sec. 3.3: "$\beta_{\rm ALP} = 0.336 \pm 0.107°$" (Run 1)
- Sec. 4: "$\beta = 0.27°$" (forecast)

Where does 0.27° come from? It's used as the forecast input but is not derived anywhere. **Fix:** unify the headline number with a single, defensible derivation.

---

## MINOR FINDINGS

### P2-Mi1. Table 1 sample sizes look like total samples, not effective
The author admits $N_{\rm eff} \sim 1000$, but the table shows "2,160 / 6,840 / 720 samples" without specifying these are post-burn-in raw or effective. Clarify.

### P2-Mi2. Fig. 2 caption duplicates body claim
The caption of Fig. 2 (p.5) just restates the surrounding text. Either tighten or add value (e.g., quantify overlap fraction).

### P2-Mi3. Eq. 2 missing $\hbar = c = 1$ statement
Dimensional consistency of $\beta = (g_{a\gamma}/2)\Delta\phi$ requires natural units. State this once.

### P2-Mi4. "Order-unity natural values" rhetoric
The phrase "order-unity" appears 8+ times. Once is fine; repetition reads as overcompensation for a tuning concern.

### P2-Mi5. Acknowledgment "use of AI research assistants"
Standard disclosure, but in combination with the broken references and arithmetic inconsistencies, suggests inadequate human review before submission.

### P2-Mi6. "Hubify" affiliation
Independent Researcher with corporate-domain email is fine, but the institution-style affiliation line "Independent Researcher, Los Angeles" reads unusually. Cosmetic.

### P2-Mi7. Page count vs. content
Paper is 7 pages including acknowledgments. Given (a) the prior literature already covers the model and (b) the analysis is a one-parameter Gaussian combination plus toy MCMC, the contribution can fit in a 3–4 page Letter at most, or be folded into the companion paper series.

### P2-Mi8. Decimal/percent confusion in Sec. 5
"$\sqrt{0.05} \theta_{\rm nat} \approx 0.22$" — what is $\theta_{\rm nat}$? It is not defined. From context it appears to be 1, but the relation $\sqrt{0.05} \times 1 = 0.224$ checks out only if $\Omega_\phi = 0.05$ is the threshold. State the threshold explicitly.

### P2-Mi9. "3.6σ Eskilt et al." vs "3.5σ exceeded" (p.1) vs "3.9σ combined"
Three different significance values in the intro region. State which is the headline observational input and stick to it.

### P2-Mi10. No figure of $\Delta\phi/f_a$ vs $m/H_0$
The central physics input — the ODE solution — is not shown. A figure would help readers verify the claimed range.

---

## NITPICKS

### P2-N1. "βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis"
Minor typesetting issue: "Eskilt et al." without first name and reference number in the abstract is sub-standard for PRD.

### P2-N2. "fphoton" used as both a variable name and a label
Defining a variable as `fphoton × C_0` is non-standard notation in this subfield. Use $g_{a\gamma}$ or a clean physical variable.

### P2-N3. Equation 11 inline vs displayed inconsistency
The first equality is inline with `⇒` then displayed. Format as a single displayed equation.

### P2-N4. Missing punctuation in Sec. 5 inline equation lists
"option (a, b, c)" should be "options (a), (b), (c)" for readability.

---

## Summary recommendation

**REJECT**

This paper should be rejected outright. The novelty claim is honestly undermined by the author's own Sec. 7 admission that Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated the central result, with stronger constraints available from Namikawa et al.; the abstract's "no fine-tuning" claim is directly contradicted by the author's own Sec. 5 calculation showing that the spectator condition requires a 25× tuning of $\theta_i$, which would then push $\beta$ well below the observed value; every single bibliographic reference renders as `[?]` with no bibliography in the PDF, making the manuscript unreviewable on standard PRD grounds; the headline forecast value $\beta = 0.27°$ is never actually derived (Sec. 2.2 gives 0.29°, Sec. 3.2 gives 0.24°, Run 1 gives 0.34°); the "9σ" LiteBIRD claim ignores the systematic floor the author themselves flags; the MCMC posteriors ($C_{a\gamma} = 13.4$, prior-bounded) directly contradict the "$\mathcal{O}(1)$ natural" claim; and the combination of NPIPE and ACT DR6 as "independent" measurements is statistically illegitimate. The paper is not at PRD standard and the core scientific contribution beyond existing literature is unclear. A complete rewrite as a short note acknowledging it as a re-analysis of public summary statistics, with honest treatment of the spectator-condition tuning, could potentially be submitted to a less rigorous venue.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings (Fresh-Eyes Pass)

## NEW ESSENTIAL FINDINGS

### P2-E11. The MCMC mass posterior contradicts the model's headline "m ∼ H₀" framing
**Page 4, Fig. 1.** The mass posterior is shown as $\log_{10}(m_a/\text{eV}) = -31.4^{+1.4}_{-1.2}$. Converting: $H_0 = 67.4$ km/s/Mpc $\approx 1.4 \times 10^{-33}$ eV, so $\log_{10}(H_0/\text{eV}) \approx -32.85$. The posterior peak at $-31.4$ corresponds to $m_a \approx 4 \times 10^{-32}$ eV $\approx 28\, H_0$ — **nearly 30× the "Hubble-scale mass" advertised in the title, abstract, and every section of the paper**. The lower 1σ edge at $-32.6$ gives $m \approx 1.8\, H_0$; only the deep lower tail of the posterior is consistent with $m \sim H_0$. This is a fatal blow to the framing: the data does not support the model regime the author claims.

Worse, the posterior is **prior-bounded above**: the prior on $\log_{10}(m_a/\text{eV})$ is $[-35, -30]$ (Sec. 3.3) and the upper 1σ at $-30.0$ touches the prior wall. The author has not reported a prior-edge diagnostic. The data wants higher mass than the prior allows, which would push $\Omega_\phi$ even higher and make the spectator condition (Sec. 5) more violated still. **Fix:** widen prior, redo analysis, and reconcile mass posterior with "$m \sim H_0$" headline.

### P2-E12. Abstract notation $C_0$ vs body notation $C_{a\gamma}$ — undefined and inconsistent
**Page 1, Abstract vs Page 2, Sec. 2.2.** The abstract introduces "order-unity photon anomaly coefficient $C_0 \sim \mathcal{O}(1)$" and an effective coupling "$f_{\rm photon} \times C_0 = 1.73 \pm 0.44$" (also Eq. 5, p.3). The body uses $C_{a\gamma}$, **never** $C_0$, with values 4–12 and fiducial $C_{a\gamma} = 8$. **These are clearly not the same quantity** — $C_{a\gamma} \sim 8$ is incompatible with "$C_0 \sim \mathcal{O}(1)$." The translation $C_0 \leftrightarrow C_{a\gamma}$ is never given. The quantity $f_{\rm photon}$ is undefined (see also E7). 

Furthermore, the abstract's scope note "$\beta = (g_{a\gamma}/2)\Delta\phi \approx (C_0 \theta_i/2) F(m/H_0)$" drops the $\alpha_{\rm EM}/(4\pi)$ prefactor present in Eq. 2. Either the abstract has a factor-$(\alpha_{\rm EM}/2\pi)$ error in the algebra, or $C_0 = (\alpha_{\rm EM}/(2\pi)) \cdot C_{a\gamma}$ implicitly — in which case the "$C_0 \sim \mathcal{O}(1)$" claim is **arithmetically forced**, not a naturalness statement: any $C_{a\gamma}$ in [1,30] gives $C_0$ in [0.001, 0.035], which is **not** order unity. The naturalness rhetoric in the abstract is broken either way. **Fix:** define $C_0$ explicitly with an equation; reconcile with $C_{a\gamma}$.

### P2-E13. Function $F(m/H_0)$ appears in abstract, never defined in body
**Page 1, Abstract.** Three times the abstract invokes "$F(m/H_0)$" as the dimensionless function carrying the mass dependence: in the scope-of-naturalness note and the headline formula $\beta \approx (C_0 \theta_i/2) F(m/H_0)$. **The body never defines $F(m/H_0)$.** The closest analog is the numerical statement "$\Delta\phi/f_a \approx 0.2$–$1.1$" in Eq. 1. A reader cannot reproduce the headline formula from the body. This is a basic reproducibility failure. **Fix:** define $F$ explicitly with its functional form (or its numerical values) tied to the ODE solution.

### P2-E14. Prediction range "0.17–0.43°" lower bound is arithmetically wrong
**Page 2, Sec. 2.2.** The author claims "The prediction spans $\beta \approx 0.17$–$0.43°$ across the natural parameter range $m/H_0 \in [1,3]$, $\theta_i \in [0.5, 2]$, $C_{a\gamma} \in [4, 12]$, comfortably bracketing the observed value." 

Recompute the lower bound at $C_{a\gamma} = 4$, $\theta_i = 0.5$, $m/H_0 = 1$ (Δφ/f_a ≈ 0.65 at $\theta_i = 1$ per Sec. 2.1; in the small-angle regime $\Delta\phi$ scales **linearly** with $\theta_i$, so $\Delta\phi/f_a \approx 0.325$ at $\theta_i = 0.5$):
$$\beta_{\min} = \frac{\alpha_{\rm EM}}{4\pi} \cdot C_{a\gamma} \cdot (\Delta\phi/f_a) = \frac{1/137}{4\pi} \cdot 4 \cdot 0.325 = 7.55 \times 10^{-4}\, \text{rad} = 0.043°.$$

This is **a factor of 4 below the quoted 0.17°**, and conspicuously well below the observed $0.342°$. The lower edge of the "natural" range is in tension with the data at $\sim 3.2\sigma$, not "comfortably bracketing" it. The quoted range looks fitted-after-the-fact to bracket the observation. **Fix:** redo the range calculation and report it honestly; this likely undermines the naturalness claim further.

### P2-E15. Bayes factor priors all lie above $\beta_{\rm combined}$
**Page 3, Sec. 3.4.** The Savage-Dickey priors quoted are $\beta \in [0°, 1°]$, $[0°, 2°]$, $[0°, 0.5°]$ — all of which extend well above the combined posterior $\beta = 0.242°$. The reported variation $\ln B = 5.17 \to 4.48 \to 5.86$ (factor of $\sim 4$ in the Bayes factor) directly reflects the prior width-to-posterior ratio sensitivity inherent to Savage-Dickey on a flat prior. None of these priors is physically motivated by an ALP-derived constraint (e.g., $\beta \in [0°, \beta_{\rm max}(f_a, C_{a\gamma})]$). The prior dependence the author flags is itself the entire problem: there is no defensible prior, so the Bayes factor is essentially undefined. **Fix:** either compute $\ln B$ under a model-derived prior or remove this analysis.

---

## NEW MAJOR FINDINGS

### P2-M13. "3.5σ" combined evidence in introduction vs "3.9σ" derived later
**Page 1, Sec. 1 intro vs Page 3, Eq. 4.** Intro says "Combined, the evidence exceeds 3.5σ." The author then derives 3.9σ in Eq. 4 using **the same data** (Planck + ACT). Either the intro number is from a previous version (stale) or from a different combination procedure. The text never explains the discrepancy. The 3.5σ number aligns with no specific cited result, suggesting it's left over from an earlier draft. **Fix:** unify and cite.

### P2-M14. Sec. 3.3 ALP posterior $\beta_{\rm ALP} = 0.336 \pm 0.107°$ is **wider** than the data inputs
**Page 3, Eq. 6.** The author reports Run 1 (ALP, $C=8$ fixed) yields $\beta_{\rm ALP} = 0.336 \pm 0.107°$. The data input is $\beta_{\rm obs} = 0.342 \pm 0.094°$ (Sec. 3.1). **The ALP model posterior has *larger* error bars than the input data** ($0.107 > 0.094$). This is impossible if the ALP model adds information — it can only equal or reduce the error. The most likely explanation is that the ALP model adds a *parameter degeneracy* (with $\theta_i$ or $m$) that broadens $\beta$ relative to the data — meaning the ALP model is *less* predictive than the model-free fit, not more. This contradicts the "natural prediction" framing.

Compare with Run 3 (β free): $\beta_{\rm free} = 0.344 \pm 0.096°$, very close to the data input. So Run 3 essentially reproduces the data (as expected for a flat-prior fit), and Run 1 *worsens* the constraint. **Fix:** explain why the ALP model gives wider posterior and what this means for predictive power.

### P2-M15. Fig. 1 β posterior $0.324 \pm 0.099°$ not quoted in body
**Page 4, Fig. 1.** The triangle plot labels show "$\beta\, [\text{deg}] = 0.324 \pm 0.099$" — this is presumably Run 2 (C free), the configuration plotted. The body Sec. 3.3 quotes Run 1 (0.336 ± 0.107) and Run 3 (0.344 ± 0.096) but **never quotes Run 2's β posterior in text**. The figure-text mismatch makes Run 2's contribution hard to evaluate. **Fix:** quote Run 2's β in the body.

### P2-M16. $\Omega_\phi \approx 0.17$ headline value is the author's own arithmetic but worth quantitative check
**Page 5, Eq. 11.** Recompute at $f_a = M_{\rm Pl}$, $m = H_0$, $\theta_i = 1$:
$$\Omega_\phi = \frac{1}{6} \cdot 1 \cdot 1 \cdot 1 = 0.167 \approx 0.17. ✓$$
Now at the MCMC-favored posterior values ($m \approx 28 H_0$ per P2-E11, $\theta_i \approx 1.33$, $f_a$ unfit):
$$\Omega_\phi = \frac{1}{6} \cdot 28^2 \cdot 1 \cdot 1.33^2 = \frac{1}{6} \cdot 784 \cdot 1.77 = 231.$$
This is **231× the critical density** — totally unphysical, and **the MCMC samples are in a regime that overcloses the universe by two orders of magnitude**. The MCMC has no physicality prior. This is a serious problem with the analysis: the ALP parameter posterior is reported as a scientific result but most of the sampled region is excluded by basic cosmology. **Fix:** impose $\Omega_\phi < 1$ as a hard prior and redo MCMC.

### P2-M17. Eq. 11 ignores oscillation when $m > H_0$
**Page 5, Eq. 11.** The energy density formula $\rho_\phi = (1/2) m^2 f_a^2 \theta_i^2$ implicitly assumes the field is **still frozen** (no oscillation). For $m \gg H_0$ the field has begun oscillating and the energy density should be redshifted by a factor of $(a_{\rm osc}/a_0)^3$ where $a_{\rm osc}$ is the scale factor at which oscillations began ($H(a_{\rm osc}) = m$). For $m = 28 H_0$ (the MCMC posterior), oscillations began at $z_{\rm osc}$ where $H(z) = 28 H_0$ — using $H^2 \approx H_0^2 \Omega_m (1+z)^3$ in matter domination, $(1+z_{\rm osc})^3 = 28^2/0.315 \approx 2490$, so $z_{\rm osc} \approx 13.5$. The redshift factor is $(1/14.5)^3 \approx 3 \times 10^{-4}$. So at $m = 28 H_0$, $\Omega_\phi \approx 231 \times 3 \times 10^{-4} \approx 0.07$ — *consistent with spectator!* But Eq. 11 doesn't include this. The author's Sec. 5 argument applies only in the slow-roll regime, but the MCMC samples a regime where the slow-roll formula doesn't apply. The entire Sec. 5 tuning discussion is therefore framework-inconsistent with the actual MCMC posterior. **Fix:** state which regime Eq. 11 applies to and use the correct formula across the MCMC parameter space.

### P2-M18. "Cherry-pick" of $m = 2H_0$ in Sec. 2.2 fiducial
**Page 2, Sec. 2.2.** The fiducial calculation uses "$m \approx 2H_0$" yielding $\Delta\phi/f_a \approx 1.07$, near the **upper edge** of the Eq. 1 range "0.2–1.1". The intro says the model is "$m \sim H_0$" but the fiducial number that produces the headline $\beta = 0.29°$ ($\sim 0.27°$) uses $m = 2H_0$. At the actual $m = H_0$ value, Eq. 1 implies $\Delta\phi/f_a \sim 0.65$ (also stated explicitly), which gives $\beta = (1/137)(8/4\pi)(0.65) = 0.173°$ — only **half** the observed value, and a $1.8\sigma$ tension with $\beta_{\rm obs} = 0.342°$. The headline prediction depends on $m = 2H_0$, not $m = H_0$. **Fix:** state the fiducial mass as $m = 2H_0$ throughout, or recompute with $m = H_0$ and report the tension.

### P2-M19. Effective coupling Eq. 5 — implied normalization
**Page 3, Eq. 5.** Working backwards: $f_{\rm photon} \times C_0 = 1.73 \pm 0.44$ has the same fractional error as $\beta_{\rm combined} = 0.242 \pm 0.061°$ (both give $\sim 3.93$). Therefore $f_{\rm photon} \times C_0 = \beta_{\rm combined}/\beta_{\rm ref}$ for some reference value $\beta_{\rm ref} = 0.242/1.73 = 0.140°$. **What is 0.140°?** It is not the "natural prediction" 0.27° or 0.29°, nor any other number in the paper. It looks like a hidden normalization choice that goes unstated. Unless $f_{\rm photon}$ and $\beta_{\rm ref}$ are explicitly defined, Eq. 5 is a number with no physical meaning. **Fix:** define the normalization explicitly.

### P2-M20. Combined β = 0.242° is in mild tension with Eskilt 0.342°
**Pages 1, 3.** The author treats the Eskilt value (0.342 ± 0.094°) and their combined value (0.242 ± 0.061°) as if both support the conclusion, but they differ by:
$$\Delta\beta/\sigma_{\rm joint} = (0.342 - 0.242)/\sqrt{0.094^2 + 0.061^2} = 0.100/0.112 = 0.89\sigma.$$
This is not yet a serious tension, but it is not negligible either, and the two values cannot both be the "true" $\beta$. The author uses Eskilt 0.342° for the MCMC (Sec. 3.3) and their own 0.242° for the summary likelihood (Sec. 3.2), without flagging that the analyses are using different effective input. The "consistency" claim then conflates two different inputs. **Fix:** pick one and stick to it, or report explicitly that the analyses use different inputs and what the implications are.

---

## NEW MINOR FINDINGS

### P2-Mi11. Eq. 1 range $\Delta\phi/f_a \in [0.2, 1.1]$ vs fiducial $0.65$ at $m=H_0$
The "fiducial case $m = H_0$, $\theta_i = 1$" gives $\Delta\phi/f_a \approx 0.65$, near the middle of the range. But the headline calculation in Sec. 2.2 uses $\Delta\phi/f_a \approx 1.07$ at $m = 2H_0$ (top edge). The reader cannot tell whether 0.65 or 1.07 is the "fiducial" value. State both in a table.

### P2-Mi12. Run 2 quotes $\log_{10}(m_a/\text{eV}) = -31.4^{+1.4}_{-1.2}$ — large posterior
The mass posterior spans $\sim 2.6$ decades. Such a wide posterior is essentially data-uninformative, suggesting the data fit any mass that lets the field roll between recombination and today. The author should comment.

### P2-Mi13. Sec. 5 reference "$\sqrt{0.05}\, \theta_{\rm nat} \approx 0.22$" — implicit threshold
The factor $\sqrt{0.05}$ implies a threshold $\Omega_\phi < 0.05$ for "spectator," but this is never stated. Some authors use $\Omega_\phi < 0.1$, others $< 0.01$. **Fix:** state the threshold explicitly.

### P2-Mi14. "Indicative" Bayes factor still appears bolded in equation environment
Eq. 9 displays $\ln B = 5.17$ in a numbered equation — i.e., a load-bearing quoted result — while the surrounding text calls it "indicative." A reader scanning equations will see 5.17 as a result; the qualification is buried in prose. Move the indicative qualifier to the equation label or remove the equation environment.

### P2-Mi15. Sec. 6 ECH motivation includes no citation that survives reference rendering
"see the companion paper [?]" — the broken citation makes the section entirely uncheckable.

### P2-Mi16. Table 1 — "Status: Converged" for Run 3 (720 samples)
720 samples is below typical convergence-claim thresholds. The "Converged" label based purely on $\hat{R}$ is misleading at this sample size — chain mixing and chain length are different diagnostics.

### P2-Mi17. Run 1 and Run 2 sample counts (2,160 / 6,840) inconsistent with prior-driven analysis
The C-free model (Run 2) has 3× more samples than C-fixed (Run 1) — but the C-free model has more parameters and needs *much* more sampling for the same posterior resolution. The ratio is backwards relative to dimensional needs.

### P2-Mi18. Fig. 2 — model labels in figure ("Model 0", "Model 2", "Model 2b") don't match body labels ("Run 1", "Run 2", "Run 3")
**Page 5, Fig. 2.** The legend uses "Model 0: beta free", "Model 2: ALP (C=8)", "Model 2b: ALP (C free)" but the body (Sec. 3.3, Table 1) uses Run 1, 2, 3. The numbering also doesn't match — Run 1 is C=8 (= Model 2?), Run 2 is C free (= Model 2b), Run 3 is β free (= Model 0). The reader has to mentally translate. Suggests an earlier draft used Model X labels and the relabeling was not propagated. **Fix:** unify nomenclature.

### P2-Mi19. Fig. 2 "Observed" band is green-shaded but no width quoted in caption
The shaded band in Fig. 2 presumably represents $\beta_{\rm obs} \pm 1\sigma = [0.248, 0.436]°$, but this is not stated in the caption or legend.

### P2-Mi20. Eq. 1 includes "for $m/H_0 \in [0.5, 3]$, $\theta_i = 1$"
But the natural-range sweep (Sec. 2.2) uses $m/H_0 \in [1, 3]$, $\theta_i \in [0.5, 2]$. The lower edge $m/H_0 = 0.5$ in Eq. 1 isn't carried through to the prediction range. Inconsistent intervals.

---

## NEW NITPICKS

### P2-N5. "yields a birefringence rotation angle $\beta \approx 0.27°$" — value not derived
The abstract's headline value 0.27° appears nowhere as the output of a calculation. The body gives 0.29° (Sec. 2.2). Either round 0.29° to 0.3° or trace where 0.27° comes from.

### P2-N6. "9σ statistical significance, contingent on..."
The conclusion (p.6) qualifies the 9σ claim, but the abstract does not. Standard PRD asks for consistent qualification.

### P2-N7. "The author thanks the Planck and ACT collaborations" — but no collaboration members are listed
Standard acknowledgments name members or working groups; here it's generic. Minor.

### P2-N8. "Computations were performed on consumer hardware"
Irrelevant. PRD doesn't require hardware disclosure.

### P2-N9. Mismatched dashes
Both `–` and `-` used in numerical ranges (e.g., "0.2–1.1" vs "1–3"). Use en-dashes throughout.

### P2-N10. Eq. 2 — $g_{a\gamma}$ notation but no units stated
Implied natural units; state once.

---

## Summary

The fresh-eyes pass surfaced **5 additional Essential findings** and **8 additional Major findings**, several of which strengthen the rejection case:

- **P2-E11**: MCMC mass posterior favors $m \approx 28\, H_0$, falsifying the "Hubble-scale mass" model claim.
- **P2-E12, E13**: Abstract uses undefined notation ($C_0$, $F(m/H_0)$, $f_{\rm photon}$) that doesn't appear in the body.
- **P2-E14**: Prediction-range lower bound (0.17°) is arithmetically wrong by a factor of 4.
- **P2-M14**: ALP-model posterior is *wider* than the data input — the model adds parameter degeneracy rather than predictive power.
- **P2-M16, M17**: At MCMC-posterior parameters, the ALP overcloses the universe by 100× under the author's own Sec. 5 formula; the author has no physicality prior on the MCMC.

These findings deepen but do not change the recommendation: **REJECT**. The paper's analytical and arithmetic foundations are not at PRD standard.