# P2 auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11072 chars)
**Wall time**: 402.3s

---

# Referee Report — P2: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

This paper claims that a "natural" spectator ALP with $f_a \sim M_{\rm Pl}$, $m \sim H_0$, $\theta_i \sim O(1)$ predicts $\beta \approx 0.27^\circ$, supported by a Gaussian summary-likelihood combination of Planck NPIPE and ACT DR6 plus three small MCMC runs, and forecast as a $9\sigma$ LiteBIRD test. The arithmetic of the summary combination is correct, but the central "naturalness" narrative is not earned by the equations, the MCMC reporting is internally inconsistent with the displayed triangle plot, key inputs are uncited or undefined, and the Bayes factor and significance reporting are sloppy. The paper is short on novel content: the model class is acknowledged to be Fujita et al. (2021).

---

## ESSENTIAL findings

### P2-E1 — Naturalness claim contradicted by the paper's own equations (Sec. 2.2, p. 2; abstract)
Eq. (1) gives $\Delta\phi/f_a \approx (1-J_0(m/H_0))\theta_i \approx 0.24\,\theta_i$ for $m/H_0\sim 1$. Eq. (2) then gives $\beta = (C_0/2)(\Delta\phi/f_a)$. Plugging in: $\beta \approx 0.12\, C_0\,\theta_i\,{\rm rad} \approx 6.9^\circ\, C_0\,\theta_i$. For $C_0,\theta_i \sim O(1)$ the **prediction is $\beta \sim$ few degrees, not $0.27^\circ$.** The text then asserts without derivation that "the cosmological field evolution gives $\Delta\phi/f_a \sim 10^{-2}$," contradicting Eq. (1) by a factor of $\sim 25$. The "no fine tuning" claim that is the central marketing of the paper (abstract; Sec. 6 bullet 1; Sec. 7) therefore is not supported by the equations as displayed. Either Eq. (1) is wrong, or $C_0\theta_i$ must be $\sim 4\times 10^{-2}$ — i.e., tuned. This must be reconciled before publication.

### P2-E2 — Direct internal inconsistency between Sec. 3.3 and Figure 1
Text (Eq. 8): "$C_{a\gamma}\times\theta_i = 3.4 \pm 1.1$". 
Figure 1 medians: $\theta_i = 1.33^{+0.44}_{-1.1}$, $C_{a\gamma} = 13.4^{+5.6}_{-11}$. The product of medians is $\approx 17.8$, not $3.4$. Even allowing for a strongly anti-correlated degeneracy, the marginal medians shown cannot map to a product posterior centered at $3.4$. Either the value in the text is wrong, the figure is wrong, or it is being computed from a different chain. As written the two are incompatible and this number is load-bearing for the "consistent with $O(1)$" claim.

### P2-E3 — Undefined parameter $f_{\rm photon}$ used as a headline number
Abstract and Eq. (5) report "$f_{\rm photon}\times C_0 = 1.73 \pm 0.44$" as evidence of order-unity coupling. The symbol $f_{\rm photon}$ is never defined anywhere in the paper. The reader cannot verify whether 1.73 is "order unity" relative to the model, nor reconstruct its derivation from $\beta_{\rm combined}=0.242^\circ$. Headline numbers cannot be undefined. Either define $f_{\rm photon}$ with units and the formula $\beta = K\, f_{\rm photon} C_0$, or remove this number.

### P2-E4 — "Eskilt et al. joint Planck + ACT analysis" value is uncited
The abstract and Sec. 3.1/3.3 use $\beta_{\rm obs} = 0.342\pm 0.094^\circ$ attributed to "Eskilt et al. joint Planck + ACT". The bibliography contains only Eskilt & Komatsu 2022 (Planck NPIPE, $0.30\pm 0.11^\circ$). There is no joint Planck+ACT Eskilt reference. This is the value driving Run 1, Run 3, and the abstract's "3.6σ"; it must be tied to a citable, retrievable paper.

### P2-E5 — Two distinct $\beta$ measurements presented without "not directly comparable" qualification
The paper alternates between $\beta_{\rm combined}=0.242\pm 0.061^\circ$ (3.9σ; Eq. 4) and $\beta_{\rm obs}=0.342\pm 0.094^\circ$ (3.6σ; Sec. 3.3) as if they were interchangeable, even using one in the summary likelihood and the other in MCMC and the LiteBIRD forecast. The difference between $0.242^\circ$ and $0.342^\circ$ is itself $\sim 1\sigma$ — non-trivial. Per the review standard, every juxtaposition of these requires an explicit "not directly comparable" qualification; the paper currently has none.

### P2-E6 — LiteBIRD "9σ" uses the prediction value, not the data
$9\sigma = 0.27^\circ/0.03^\circ$ uses the theoretical prediction. The data-driven forecast would be $0.242^\circ/0.03^\circ = 8.1\sigma$, and the MCMC-posterior-driven value would be $\sim 11\sigma$. The abstract states "9σ" as the headline. Pick a single, defensible statistic, label it clearly, and report all three transparently.

### P2-E7 — Bayes factor calculation is not reproducible
Eq. (9) asserts $\ln B = 5.17$ via Savage–Dickey on prior $[0^\circ,1^\circ]$, with $4.48$ and $5.86$ at $[0^\circ,2^\circ]$ and $[0^\circ,0.5^\circ]$. I attempted to reproduce: using $\beta_{\rm combined}=0.242\pm 0.061^\circ$ I get $\ln B \approx 6.0/5.3/6.7$; using the ALP MCMC ($0.336\pm 0.107$) I get $\ln B \approx 3.6/2.9/4.3$; using the "$\beta$ free" run ($0.344\pm 0.096$) I get $\ln B \approx 5.0/4.3/5.7$. None of the three exactly matches. The paper must state explicitly which posterior was used and show the computation. Additionally, calling $\ln B = 5.17$ "indicative" undersells the language inconsistency: on Jeffreys' scale this is "strong"; on a prior-dependent Savage–Dickey it is hand-waving.

### P2-E8 — Theoretical content is acknowledged to be a re-presentation, not novel
Sec. 6 explicitly states: "Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces $\beta \sim 0.3^\circ$." The paper's own claimed contribution is then "the specific parameter identification ($f_a\sim M_{\rm Pl}, m\sim H_0$) that produces a natural prediction matching the observed signal." This is precisely what Fujita et al. (2021) demonstrated. The paper therefore contributes (i) a summary-likelihood combination already implicit in the literature and (ii) a small MCMC. The novelty bar for PRD is not cleared. The author must either identify a genuinely new technical result or recast as a brief comment.

---

## MAJOR findings

### P2-M1 — Summary likelihood treats Planck NPIPE and ACT DR6 as fully independent
Eq. (3) assumes uncorrelated errors. These analyses share calibration assumptions (Minami–Komatsu self-calibration), shared foreground models, and overlap with the WMAP+Planck Eskilt result. Without a covariance argument, the $3.9\sigma$ combined significance is overstated. Quantify or qualify.

### P2-M2 — MCMC sample sizes are inadequate even by the paper's own admission
Table 1 reports 720, 2160, 6840 samples; $N_{\rm eff}\sim 1000$. The paper concedes this. For a PRD paper whose central numbers — $C_{a\gamma}\theta_i = 3.4\pm 1.1$, $\ln B$, posterior medians — depend on the chain, this is unacceptable. Rerun with $\geq 50{,}000$ effective samples (the author's own suggested fix) before resubmission.

### P2-M3 — Choice of $C = 8$ in Run 1 is unmotivated
The "natural" model in Sec. 2 has $C_0 \sim 1$. Run 1 fixes $C = 8$ with no justification. Run 2's prior $C_{a\gamma} \in [1, 30]$ excludes natural values $C \lesssim 1$. The chosen priors bias the inference toward large couplings, contradicting the naturalness narrative.

### P2-M4 — Citing an "in preparation" paper as evidence
Namikawa, Murai, Naokawa is listed as "In preparation". PRD does not accept in-prep references as substantive citations. Remove or replace with a published reference.

### P2-M5 — Three companion self-citations (Golden 2026a, 2026b) "submitted simultaneously"
Sec. 5 and Sec. 6 each cite a separate companion. The body of this paper claims the result is "independent of bounce cosmology" yet leans on the companion for theoretical motivation. This self-citation ring inflates the apparent context; the author should either fold the relevant theoretical motivation into this paper or remove the framing entirely.

### P2-M6 — Calibration systematics paragraph (Sec. 6) undermines the headline
The author concedes that residual $\sim 0.1$–$0.3^\circ$ systematics from bandpass, dust, beams may explain the signal — i.e., the entire effect. This destabilizes the abstract's $3.9\sigma$ headline. The abstract must acknowledge this systematics uncertainty quantitatively, not bury it in Discussion.

### P2-M7 — Sec. 2.1 hand-waves the cosmological integration factor
"$1 - J_0(1) \approx 0.24$; the precise value depends on the cosmological integration through the matter and dark-energy eras." A paper whose entire claim rests on this O(1) factor must actually compute it (numerical integration of the Klein–Gordon equation in a $\Lambda$CDM background). Without this, "naturally produces $0.27^\circ$" is unsupported.

### P2-M8 — Discrepancy between intro "3.5σ combined" and abstract "3.6σ" and Eq.(4) "3.9σ"
Three different "combined" significance values appear (3.5, 3.6, 3.9). They are not the same combination but the paper does not say so explicitly. Provide a single, clearly defined number with provenance.

### P2-M9 — Figure 2 is filler
The figure shows three overlapping Gaussians that are by construction nearly identical, and the caption simply restates this. It contributes no information beyond Eqs. (6)–(7) and should be removed.

---

## MINOR findings

### P2-N1 — Eq. (1): $J_0(0) = 1$, so the denominator is redundant.

### P2-N2 — Abstract "9σ" assumes the prediction is exactly correct and the systematic budget is zero; neither is established.

### P2-N3 — "$5\times 10^{-3}$ rad $\approx 0.27^\circ$": $0.27^\circ = 4.71\times 10^{-3}$ rad. Round or be exact.

### P2-N4 — Sec. 3.1: ACT DR6 is attributed "Diego-Palazuelos and Komatsu 2025"; verify this is the citable ACT DR6 birefringence paper and not a different analysis.

### P2-N5 — Acknowledgments disclose use of AI research assistants for "the analysis and manuscript preparation." For PRD, the author must specify which steps of the analysis were AI-generated (the inferential code, the MCMC, the prose). This is a methodological transparency requirement, not an optional disclosure.

### P2-N6 — Figure 1 axis label "$\log_{10}(m_a/{\rm eV}) = -31.4^{+1.4}_{-1.2}$" — for a posterior that hits the prior boundary at $-30$ (visible in the figure), this median is prior-driven and should be flagged as such.

### P2-N7 — "Bayes factor: $\ln B = 5.17$ (indicative evidence for nonzero rotation)" — "indicative" is non-standard for $\ln B > 5$; use Jeffreys' or Kass–Raftery scale labels with the prior-dependence explicit.

### P2-N8 — "spectator field — it does not participate in the bounce dynamics" — but the paper claims to be independent of bounce cosmology, so this paragraph is unnecessary self-positioning.

### P2-N9 — Length: at 6 pages with one substantive figure, one informational figure, one small table, and an MCMC that re-derives published Fujita et al. (2021) results, this is more appropriately a "Brief Report" or PRD Comment, not a full PRD article.

---

## Arithmetic audit summary (independent recomputation)

| Quantity | Paper | Recomputed | Status |
|---|---|---|---|
| $\beta_{\rm combined}$ (inv-var of 0.30±0.11, 0.215±0.074) | $0.242\pm 0.061^\circ$ | $0.241\pm 0.061^\circ$ | ✓ |
| Significance of $\beta_{\rm combined}$ | $3.9\sigma$ | $3.97\sigma$ | ✓ |
| Planck NPIPE significance | $2.7\sigma$ | $2.73\sigma$ | ✓ |
| ACT DR6 significance | $2.9\sigma$ | $2.90\sigma$ | ✓ |
| Eskilt joint significance | $3.6\sigma$ | $3.64\sigma$ | ✓ (but uncited) |
| $\beta$ predicted from $\theta_i\sim 1$, $C_0\sim 1$ via Eqs.(1)–(2) | $0.27^\circ$ | $\sim 7^\circ$ | **✗ off by factor 25** |
| $C_{a\gamma}\theta_i$ from Fig 1 medians | $3.4\pm 1.1$ | $\sim 17.8$ | **✗ inconsistent** |
| $\ln B$ reproducibility | $5.17$ | $5.0$ – $6.0$ depending on posterior | partially reproducible |

---

## Summary recommendation

**REJECT**

The arithmetic of the summary-likelihood combination is sound, but the central physics claim — that the observed birefringence emerges "naturally" with no fine-tuning from $f_a \sim M_{\rm Pl}$, $m\sim H_0$, $\theta_i \sim 1$ — is contradicted by a factor of $\sim 25$ in the paper's own Eqs. (1)–(2). The MCMC reporting in Sec. 3.3 is incompatible with Figure 1 at the level of the headline number $C_{a\gamma}\theta_i = 3.4 \pm 1.1$ versus medians whose product is $\sim 18$. The "$f_{\rm photon} \times C_0 = 1.73$" headline uses an undefined symbol. The key $\beta_{\rm obs} = 0.342 \pm 0.094^\circ$ "Eskilt et al. joint Planck + ACT" value is uncited. The Bayes factor is not reproducible from the stated posteriors. The author's own Sec. 6 admits the model class and the $\sim 0.3^\circ$ prediction are due to Fujita et al. (2021), leaving the present paper's contribution as a small, under-sampled MCMC plus a Gaussian combination — insufficient for PRD. The work could be resubmitted as a Brief Report after the equations are made consistent, $f_{\rm photon}$ is defined, the MCMC is rerun with adequate sample size, the joint Eskilt+ACT reference is identified, and the systematics caveat is moved to the abstract.

---

## PASS 2 — self-critique findings (what initial review missed)

# P2: Second-Pass Review — Additional Findings

After detailed re-examination, I confirm the bulk of my first-pass findings stand, but I also missed several significant issues and made one arithmetic error that needs correction.

---

## CORRECTION to first-pass review

### P2-E7 (correction): Bayes factor IS reproducible — but from a different posterior than I assumed
I claimed the Bayes factor was non-reproducible. Re-doing the Savage–Dickey calculation carefully using the **Eskilt joint posterior** $0.342 \pm 0.094^\circ$:

$$\pi(\beta=0|\text{data}) = \frac{1}{0.094\sqrt{2\pi}}\exp\!\left(-\frac{0.342^2}{2\cdot 0.094^2}\right) = 5.64\times 10^{-3}\;\text{deg}^{-1}$$

For uniform prior on $[0^\circ, 1^\circ]$: $\ln B_{10} = \ln(1/5.64\times 10^{-3}) = 5.18$ ✓ (paper: 5.17)
For $[0^\circ, 2^\circ]$: $\ln B_{10} = 4.49$ ✓ (paper: 4.48)
For $[0^\circ, 0.5^\circ]$: $\ln B_{10} = 5.87$ ✓ (paper: 5.86)

So the Bayes factor is reproducible — but **only from the Eskilt joint posterior** ($0.342\pm0.094^\circ$), NOT from the combined posterior ($0.242\pm 0.061^\circ$) that the paper just spent Sec. 3.2 constructing. This is a new finding, recast below as E10.

---

## New ESSENTIAL findings

### P2-E9 — Abstract misidentifies the data: "Planck HFI" vs. "Planck NPIPE"
Abstract: "*Gaussian summary-likelihood inference using **Planck HFI and ACT DR6** data, finding β = 0.242 ± 0.061°*". 
Sec. 3.1 actually uses **Planck NPIPE** (Eskilt & Komatsu 2022), which is a joint LFI+HFI re-processing distinct from "Planck HFI" (which would normally refer to the 2018 HFI-only release, Minami & Komatsu 2020). The abstract names the wrong dataset for its headline number. This is a data-provenance error in the abstract.

### P2-E10 — Different posteriors feed the two headline numbers, and the paper never says so
- $\beta_{\rm combined} = 0.242\pm 0.061^\circ$ (Eq. 4, abstract): from summary likelihood of Planck NPIPE + ACT DR6.
- $\ln B = 5.17$ (Eq. 9, abstract): only reproducible from the **Eskilt joint** posterior $0.342\pm 0.094^\circ$ — verified by my Savage–Dickey recomputation matching all three prior-dependent values exactly.

So the abstract's two headline numbers use two different posteriors. A consistent analysis would compute both from the same posterior. Using the combined posterior for the Bayes factor would give $\ln B \approx 5.98/5.29/6.67$ — substantially different. The choice of posterior is undisclosed and unjustified.

### P2-E11 — Run 1's MCMC implicitly contradicts Eq. (1)
Run 1 fixes $C = 8$, has prior $\theta_i \in [0.01, \pi]$, and recovers $\beta_{\rm ALP} = 0.336 \pm 0.107^\circ$. If the paper's Eq. (1) is taken at face value ($\Delta\phi/f_a = \theta_i \cdot 0.24$ for $m/H_0\sim 1$), then $\beta = (C/2)\cdot\theta_i \cdot 0.24$ rad and solving for the median: $\theta_i = 2\cdot 0.336^\circ \cdot (\pi/180)/(8\cdot 0.24) = 6\times 10^{-3}$, *below* the prior lower edge $0.01$. The MCMC therefore cannot have used Eq. (1); it must have used the unstated Sec. 2.2 suppression factor $\Delta\phi/f_a \sim 5\times 10^{-3}$, which solves $\theta_i \approx 0.29$ (inside the prior). The MCMC results in §3.3 are produced by a formula different from the one displayed in §2.1, and the discrepancy is concealed.

---

## New MAJOR findings

### P2-M10 — Notation switch $C_0 \to C_{a\gamma}$ without explanation
Sec. 2.2 defines $g_{a\gamma} = C_0/f_a$. Sec. 3.3 introduces $C_{a\gamma}$ in priors and posteriors (Eq. 8). The paper never states that these are the same quantity. The abstract uses $C_0$; Eq. (5) uses $f_{\rm photon}\times C_0$; Eq. (8) uses $C_{a\gamma}\times\theta_i$; Fig. 1 uses $C_{a\gamma}$. Three (possibly four, if $f_{\rm photon}$ encodes a piece of $C_0$) notations for what appears to be one parameter.

### P2-M11 — Figure 1's $\beta$ posterior is a fourth, un-quoted value
Figure 1 caption shows $\beta = 0.324 \pm 0.099^\circ$ (for Run 2). The text quotes:
- Eq. (6) Run 1: $0.336 \pm 0.107^\circ$
- Eq. (7) Run 3: $0.344 \pm 0.096^\circ$
- Abstract: $0.342 \pm 0.094^\circ$ (Eskilt)
- Eq. (4): $0.242 \pm 0.061^\circ$ (combined)

The Figure 1 value $0.324\pm 0.099^\circ$ is never quoted in the body. This is the *fifth* distinct $\beta$ value appearing in a six-page paper. None is identified as "the" result.

### P2-M12 — Posterior boundaries on $\log_{10}(m_a/{\rm eV})$ and $C_{a\gamma}$ are prior-pegged
Figure 1: $\log_{10}(m_a/{\rm eV}) = -31.4^{+1.4}_{-1.2}$ with prior $[-35, -30]$. The $+1.4$ upper tail reaches the prior upper bound $-30$ within $1\sigma$ — the posterior is truncated by the prior on the heavy-mass side. The visible posterior shape in the triangle plot confirms this. Similarly $C_{a\gamma} = 13.4^{+5.6}_{-11}$ with prior $[1, 30]$: the $-11$ lower tail nearly hits the lower prior edge, and the upper $+5.6$ approaches $19$ inside a $30$-edge prior. The asymmetric error bars are the signature of prior-truncation, not data constraint. These posteriors are therefore not robust constraints, contrary to the §6 "consistent with $O(1)$" narrative.

### P2-M13 — Sec. 4's exclusion claim conflates "prediction value" with "model"
"*If LiteBIRD measures $\beta = 0\pm 0.03^\circ$, the ALP explanation is excluded at 9σ.*" Strictly, this excludes only the $0.27^\circ$ prediction. The ALP model with smaller $C_0\theta_i$ (e.g., $\beta = 0.05^\circ$) would survive at $\sim 1.7\sigma$ tension — well within "allowed". The exclusion claim is overstated by conflating a specific point prediction with a parametric model class.

### P2-M14 — Eq. (4) combined significance and Eq. (8) MCMC product are mutually inconsistent under either Eq. (1) or Sec. 2.2
Using Eq. (1): $\beta_{\rm combined} = 0.242^\circ \Rightarrow C_0\theta_i = 0.035$. Using Sec. 2.2's $\Delta\phi/f_a = 10^{-2}$: $C_0\theta_i = 0.85$. Both differ from Eq. (8)'s $C_{a\gamma}\theta_i = 3.4\pm 1.1$ by factors of $\sim 100$ or $\sim 4$ respectively. The summary-likelihood inference, the MCMC inference, and the analytic prediction do not even approximately close on a common $C\theta_i$.

---

## New MINOR findings

### P2-N10 — Eq. (1) Bessel formula is unjustified
The expression $\Delta\phi \approx f_a\theta_i\,(1 - J_0(m/H_0)/J_0(0))$ has no derivation in the paper, no citation, and no obvious motivation: the Klein–Gordon equation for a cosine-potential field in a $\Lambda$CDM background does not generically integrate to a Bessel function. For a free harmonic oscillator started at rest in flat space the displacement is $\theta_i[1 - \cos(mt)]$, not $\theta_i[1 - J_0(mt)]$. In matter-domination, the WKB result is $\theta(a) \sim \theta_i (a_{\rm osc}/a)^{3/2}\cos[\phi(a)]$. The formula appears written by analogy rather than computed. A proper paper would either cite a published derivation or solve the KG equation numerically.

### P2-N11 — "Δφ/fa ~ 10⁻² from the ratio of field displacement to decay constant over the Hubble time"
This is a circular sentence: "the ratio of field displacement to decay constant" is exactly $\Delta\phi/f_a$. The phrase explains nothing. The factor $10^{-2}$ is asserted, not derived.

### P2-N12 — "5×10⁻³ rad ≈ 0.27°" is mis-rounded
$5\times 10^{-3}$ rad $= 0.2865^\circ \approx 0.29^\circ$, not $0.27^\circ$. The "0.27°" appears in the abstract, §1, §2.2, §4 ("$\beta = 0.27^\circ$"), §6, §7. If the paper consistently used the rounded $0.27^\circ$ from a slightly different input (e.g., $\Delta\phi/f_a = 4.7\times 10^{-3}$), the input should be stated; if it is rounded from $0.29^\circ$, the rounding direction is inconsistent. The $9\sigma$ LiteBIRD forecast also assumes $0.27^\circ$ exactly.

### P2-N13 — $J_0(0) = 1$, so Eq. (1) is sloppy
$\Delta\phi \approx f_a\theta_i[1 - J_0(m/H_0)/J_0(0)]$ with $J_0(0) = 1$ should be $f_a\theta_i[1 - J_0(m/H_0)]$. The denominator $J_0(0)$ is redundant and suggests the formula was lifted from a context where it was non-trivial (perhaps a ratio at some other time?). Already in initial review N1, but the denominator $J_0(0)$ being explicitly written hints the formula may not actually be the intended one.

### P2-N14 — $0.27^\circ$ vs combined $0.242^\circ$: paper says "matches at 1σ"
$(0.27 - 0.242)/0.061 = 0.46\sigma$. So "matches at $1\sigma$" is technically true but the actual separation is $0.46\sigma$. Per H (unquantified hedges), the actual delta should be quoted. Note: this means the prediction and the data are *too consistent* to discriminate against a model that predicts any $\beta \in [0.12^\circ, 0.36^\circ]$ — i.e., the model is essentially unconstraining within the data uncertainty.

### P2-N15 — "$5\sigma$ exceeds 3.5σ" vs. "$3.6\sigma$" vs. "$3.9\sigma$" vs. "$\ln B = 5.17$": four different headline statistics
§1: "Combined, the evidence exceeds 3.5σ." Abstract: "$3.6\sigma$". Eq. (4): "$3.9\sigma$". Eq. (9): "$\ln B = 5.17$" (≈ Bayes factor ~176, frequentist analogue $\sim 3.3\sigma$ using $2\ln B = \chi^2$ → $\sqrt{2\cdot 5.17} = 3.22\sigma$). All four refer to roughly the same datasets but via different combinations / metrics. Already partly in M8, but the four-way inconsistency in the abstract+intro+§3.2+§3.4 was understated.

---

## New informational findings

### P2-N16 — Bayes factor "indicative" vs. Jeffreys "strong/decisive"
On the Kass–Raftery scale, $\ln B > 5$ is "very strong" (3.6σ-equivalent); on Jeffreys' scale, $\ln B = 5.17$ is "strong". The paper labels this "indicative", which is a non-standard term that sits below "substantial" on most calibrations. Either the author is implicitly down-weighting due to prior dependence (which should be stated quantitatively) or the terminology is wrong. Strengthens initial N7.

### P2-N17 — "ACT DR6" reference: Diego-Palazuelos & Komatsu (2025) is on Planck, not ACT
Diego-Palazuelos has a 2025 paper on Planck birefringence; the actual ACT DR6 birefringence paper would have an ACT collaboration first author or similar. This citation needs verification. Strengthens N4.

---

## Updated summary recommendation

The second pass uncovered (i) an arithmetic correction (the Bayes factor IS reproducible, but from a different posterior than the headline combined posterior, exposing E10 — different posteriors feeding different headline numbers); (ii) a data-provenance error in the abstract (HFI vs. NPIPE, E9); (iii) the MCMC implicitly using a formula incompatible with displayed Eq. (1) (E11); (iv) prior-pegged posteriors in Fig. 1 (M12); (v) a fifth un-quoted $\beta$ value in the figure caption (M11); (vi) notation switching $C_0 \leftrightarrow C_{a\gamma}$ (M10); and (vii) the unjustified Bessel-function form in Eq. (1) (N10).

The original recommendation **REJECT** stands, and the case is stronger. Beyond the factor-25 contradiction at the heart of the naturalness claim (E1) and the impossible product $C_{a\gamma}\theta_i$ (E2), I now find that the paper's two headline statistics use silently different posteriors (E10) and the MCMC itself silently uses a formula that contradicts the displayed equation (E11). The work is not internally consistent at the level required for PRD.