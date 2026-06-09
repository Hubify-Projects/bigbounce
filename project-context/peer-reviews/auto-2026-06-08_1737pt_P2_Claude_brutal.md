# P2 auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12204 chars)
**Wall time**: 310.1s

---

# Referee Report: "Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts"

**Reviewer:** Brutal-honesty PRD referee
**Recommendation preview:** REJECT

---

## Overview

This 6-page manuscript claims that a spectator ALP with $f_a \sim M_{\rm Pl}$, $m \sim H_0$, $\theta_i \sim \mathcal{O}(1)$ "naturally" produces $\beta \approx 0.27°$, matches the Eskilt et al. signal, and will be tested by LiteBIRD at $9\sigma$. The paper's own Discussion (Sec. 6) admits the model class and parameter identification is already done by Fujita et al. (2021). What remains is a Gaussian combination of two published numbers, a small MCMC, and a forecast division. This is not a PRD-level contribution, and several quantitative claims do not survive recomputation.

---

## ESSENTIAL findings

### P2-E1 — The headline "natural" prediction $\beta \approx 0.27°$ is not derived; it is asserted.

**Sec. 2.2, p. 2:** "the cosmological field evolution gives $\Delta\phi/f_a \sim 10^{-2}$ (from the ratio of field displacement to decay constant over the Hubble time), yielding $\beta \approx C_0 \theta_i \times 5\times 10^{-3}$ rad $\approx 0.27°$."

But Eq. (1) gives $\Delta\phi/f_a \approx \theta_i (1-J_0(m/H_0)) \approx 0.24\,\theta_i$ for $m/H_0\sim 1$. That is $\sim 0.24$, NOT $\sim 10^{-2}$. There is a factor of ~25 discrepancy between Eq. (1) and the prose used to obtain $0.27°$. With $\Delta\phi/f_a \sim 0.24$, Eq. (2) would give $\beta \sim C_0\theta_i \times 0.12$ rad $\sim 7°$, two orders of magnitude above the data. The author has silently inserted an unexplained $\mathcal{O}(10^{-2})$ suppression to land on the desired number. **This is the central physics claim of the paper and it is internally inconsistent.** Required fix: derive $\Delta\phi$ from a proper integration of the Klein-Gordon equation in a $\Lambda$CDM background, show the actual numerical value, and either justify $0.27°$ or retract the "natural" claim.

### P2-E2 — Recomputed combined $\beta$ disagrees with the quoted value.

**Sec. 3.2, Eq. (4), p. 2:** Inverse-variance combination of Planck NPIPE ($0.30 \pm 0.11°$) and ACT DR6 ($0.215 \pm 0.074°$):
- weights: $1/0.11^2 = 82.64$, $1/0.074^2 = 182.62$
- mean: $(82.64\times 0.30 + 182.62\times 0.215)/(82.64+182.62) = (24.79 + 39.26)/265.26 = 0.2415°$ ✓
- $\sigma = 1/\sqrt{265.26} = 0.0614°$ ✓
- significance: $0.2415/0.0614 = 3.93\sigma$ ✓

OK — Eq. (4) is reproducible. **However**, the author then quotes Eq. (5) "$f_{\rm photon}\times C_0 = 1.73 \pm 0.44$" with **no defining equation**. There is no formula relating $\beta_{\rm combined}$ to "$f_{\rm photon}\times C_0$" anywhere in the paper. $f_{\rm photon}$ is never defined. The number $1.73$ is unjustified. Required fix: define $f_{\rm photon}$, give the equation, or remove Eq. (5).

### P2-E3 — Two incompatible datasets are presented as the "combined" measurement without consistency check.

**Sec. 3.1, p. 2:** "We use two independent birefringence measurements... For the MCMC parameter estimation (Sec. 3.3), we use the Eskilt et al. joint analysis value $\beta_{\rm obs} = 0.342 \pm 0.094°$, which differs because it fits the full EB cross-spectrum rather than combining point estimates."

So the *abstract* quotes $\beta_{\rm obs}=0.342\pm 0.094°$ from "Eskilt et al. joint Planck+ACT analysis." But Sec. 3.1 lists only "Eskilt and Komatsu 2022" (Planck NPIPE) at $0.30\pm 0.11°$ and "Diego-Palazuelos and Komatsu 2025" (ACT DR6) at $0.215\pm 0.074°$. **There is no Eskilt et al. joint Planck+ACT paper in the bibliography**, and the cited Eskilt+Komatsu 2022 paper does not include ACT data (ACT DR6 birefringence postdates 2022). The "joint" value $0.342\pm 0.094°$ is unattributed. Required fix: cite the actual paper for the $0.342\pm 0.094°$ joint number, or remove the claim.

### P2-E4 — Two different $\beta$ values are used as "the observed signal" with no reconciliation.

The summary-likelihood combination gives $\beta = 0.242 \pm 0.061°$. The MCMC uses $\beta_{\rm obs} = 0.342 \pm 0.094°$. These are **not consistent** ($0.342-0.242 = 0.10°$, comparable to either error bar). The paper calls both "the observed signal" interchangeably, and the abstract simultaneously claims the model accommodates $0.27°$, matches $0.342\pm 0.094°$, and is tested at $3.9\sigma$ via Eq. (4). The model "naturally" producing both numbers cannot be true. Required fix: pick one observational benchmark and use it throughout.

### P2-E5 — The "$9\sigma$" LiteBIRD forecast is computed against a number the data do not actually prefer.

**Sec. 4, p. 3, Eq. (10):** "$0.27/0.03 = 9\sigma$." But Eq. (4) gives $\beta=0.242°$, and the MCMC gives $\beta_{\rm ALP}=0.336°$. The forecast uses neither. Using the combined value, $0.242/0.03 = 8.1\sigma$; using the MCMC, $11.2\sigma$. The author cherry-picks $0.27°$ — a number that does not appear in any inference table — to get a clean $9\sigma$. Abstract's "$9\sigma$" claim is therefore unsupported by the paper's own inference. Required fix: report the forecast significance using the *actual posterior* on $\beta$, propagating its uncertainty.

### P2-E6 — Bayes factor calculation is unreproducible and prior-dependent in a way that undermines the headline.

**Sec. 3.4, p. 3:** "$\ln B = 5.17$... computed via the Savage-Dickey density ratio with a flat prior $\beta \in [0°, 1°]$. The evidence is prior-dependent: $\ln B = 4.48$ for $\beta \in [0°, 2°]$ and $\ln B = 5.86$ for $\beta \in [0°, 0.5°]$."

The Savage-Dickey ratio is $B_{10} = p(\beta=0|\text{prior})/p(\beta=0|\text{data})$. For a flat prior of width $W$ and a Gaussian posterior centered at $\hat\beta$ with width $\sigma_\beta$:
$\ln B = \ln[\sigma_\beta\sqrt{2\pi}/W] + \hat\beta^2/(2\sigma_\beta^2)$

Using $\hat\beta=0.342°$, $\sigma=0.094°$, $W=1°$:
$\ln B = \ln(0.094\sqrt{2\pi}/1) + (0.342)^2/(2\cdot 0.094^2) = \ln(0.236) + 6.62 = -1.45 + 6.62 = 5.18$ ✓

OK, $\ln B=5.17$ checks out. But the prior $[0°,1°]$ is one-sided — Savage-Dickey requires the prior to bracket the null. A one-sided prior is a choice that doubles the prior density at the null and biases ln B by $\ln 2 \approx 0.69$. The "indicative" hedge does not rescue this — the abstract still markets "ln B = 5.17" prominently. Required fix: use a two-sided physical prior or justify the one-sided choice from theory.

### P2-E7 — Sample sizes are far too small for the claimed evidence.

**Sec. 3.3 + Table 1, p. 3:** "Run 1: 2,160 samples; Run 2: 6,840; Run 3: 720." The author acknowledges this ("sample sizes... are modest by modern standards") but then proceeds to quote a Bayes factor and posterior summaries to 3 significant figures (e.g., $C_{a\gamma}\times\theta_i = 3.4\pm 1.1$). 720 samples cannot resolve a posterior tail well enough to report $\ln B$ to two decimal places. The Run 1 result $\beta_{\rm ALP} = 0.336\pm 0.107°$ has 2,160 samples but the prior on $C$ is fixed at 8, which essentially preordains $\beta\approx 0.27 \cdot$ (something) — not a meaningful test.

This is below PRD standards for any inference-driven paper. Required fix: rerun with $\geq 10^5$ samples; recompute all Bayes factors and posterior intervals.

### P2-E8 — The "naturalness" argument is rhetorical, not physical.

**Sec. 2.2, p. 2:** "this prediction involves no small or large numbers beyond the cosmological integration factor. Every input is $\mathcal{O}(1)$ in natural units." But the prediction requires $\Delta\phi/f_a \sim 10^{-2}$ (Sec. 2.2), which IS a small number, and the "cosmological integration factor" is the entire dynamics of the field — exactly the part the paper does not compute. The phrase "every input is $\mathcal{O}(1)$" is misleading. Furthermore the abstract's coupling $f_{\rm photon}\times C_0 = 1.73\pm 0.44$ is *not* $\mathcal{O}(1)$ from first principles — it is whatever value is needed to fit. Required fix: rewrite naturalness claims honestly.

### P2-E9 — Triangle plot (Fig. 1, p. 4) inconsistent with body text.

**Sec. 3.3 quotes** $C_{a\gamma}\times\theta_i = 3.4\pm 1.1$ as "consistent with $\mathcal{O}(1)$ values." But Fig. 1 shows $C_{a\gamma} = 13.4^{+5.6}_{-11}$ and $\theta_i = 1.33^{+0.44}_{-1.1}$. The marginal central value of $C_{a\gamma}$ is **13.4, not $\mathcal{O}(1)$**, and the product would be $\sim 18$, not $\sim 3.4$. Either the product quoted in the text is wrong, or the marginals in Fig. 1 are wrong, or the prior on $C_{a\gamma}\in[1,30]$ is dominating and the "natural $\mathcal{O}(1)$" claim is empty. The Bayesian inference is also evidently bimodal (skewed) and the asymmetric errors are huge. Required fix: reconcile Fig. 1 with text; if $C_{a\gamma}\sim 13$ is preferred, retract the "no fine-tuning" claim.

### P2-E10 — Citation errors.

- **"Eskilt et al. joint Planck + ACT analysis"** (Abstract): no such paper in the bibliography. The bibliography has "Eskilt and Komatsu 2022" (Planck only) and "Diego-Palazuelos and Komatsu 2025" (ACT DR6). The "joint" number $0.342\pm 0.094°$ is unattributed.
- **Namikawa, Murai, and Naokawa 2025**: listed as "In preparation" but cited as if providing existing constraints ("Namikawa, Murai & Naokawa provide superior ALP mass constraints"). Cannot cite results from a paper in preparation.
- **Golden 2026a, 2026b**: self-citations to "companion papers, submitted simultaneously" — no DOI, no arXiv ID. PRD requires either acceptance or arXiv ID for "in prep" companion citations.
- **Minami and Komatsu 2020** PRL 125:221301: title is correct, but the abstract value $\beta = 0.35\pm 0.14°$ at $2.5\sigma$ — the actual Minami+Komatsu 2020 reports $\beta = 0.35\pm 0.14°$ with $2.4\sigma$. Minor traceability issue, but consistent with body.

---

## MAJOR findings

### P2-M1 — Equation (1) is dimensionally and conceptually confused.

The expression $\Delta\phi \approx f_a\theta_i(1 - J_0(m/H_0)/J_0(0))$ uses Bessel functions, which arise for free massive scalar field oscillations in *flat* (Minkowski) space, not for an axion in an expanding universe with $H(z)$ evolving through matter and dark-energy domination. The actual solution requires numerical integration of $\ddot\phi + 3H\dot\phi + m^2\sin(\phi/f_a)f_a = 0$. The Bessel formula is wrong, and the "$\approx f_a\theta_i\times\mathcal{O}(1)$" hides the error by an $\mathcal{O}(1)$ factor that the author then secretly takes to be $10^{-2}$ (see E1). Required fix: solve the actual equation of motion.

### P2-M2 — The integer "8" for $C$ in Run 1 is unmotivated.

**Table 1, p. 3:** "ALP (C = 8 fixed)." Nowhere in the paper is the choice $C=8$ justified. For a gauge-theory anomaly $C_0$ is typically $\mathcal{O}(1{-}10)$ depending on the UV completion, but picking exactly 8 with no rationale undermines Run 1 as a "natural" benchmark. Required fix: justify or remove.

### P2-M3 — Calibration systematics section is honest but undermines the whole paper.

**Sec. 6, p. 5:** "There is an active debate about whether residual $\sim 0.1{-}0.3°$ systematics could arise from bandpass mismatch effects, residual polarized dust emission, or beam asymmetries." Given the signal is $\sim 0.24-0.34°$, a $0.1{-}0.3°$ systematic floor means the signal itself may be unphysical. The abstract makes no mention of this; it just says "$3.6\sigma$ isotropic birefringence signal." Required fix: convey this caveat in the abstract, not buried in Discussion.

### P2-M4 — Sec. 5 cross-references the ECH paper inappropriately.

**Sec. 5, p. 4:** Spends paragraphs disclaiming that the birefringence result doesn't depend on bounce cosmology or ECH — then references companion papers anyway. If the result is independent, delete the ECH discussion entirely. The current text reads as cross-promotion for a paper trilogy.

### P2-M5 — Sec. 6 cites $f_{\rm NL} = -35/8$ from "Golden 2026b" without context.

"$f_{\rm NL} = -35/8$" is dropped in one sentence at the end of Sec. 6 with no derivation, no relation to the ALP, and a self-cite. This is irrelevant filler that adds nothing to a birefringence paper. Cut.

### P2-M6 — Figure 1 (triangle plot) labeling is broken.

The y-axis of the $\log_{10}(m_a/{\rm eV})$ panel ranges from $-31$ to roughly $-34$, but the prior is stated as $[-35, -30]$. The posterior appears to hit the upper boundary at $-31$ with a sharp cutoff, suggesting the prior is truncating the posterior. The reported value $\log_{10}(m_a/{\rm eV}) = -31.4^{+1.4}_{-1.2}$ is therefore prior-edge dominated. The mass is unconstrained except by the prior. Required fix: widen prior, or report unconstrained.

### P2-M7 — Eq. (2) drops the time-evolution of $\phi$ entirely.

$\beta = g_{a\gamma}\Delta\phi/2$ assumes line-of-sight integration of $\dot\phi$ collapses to a boundary term $\phi_0 - \phi_{\rm rec}$. This is only true if the photon couples through a total derivative — fine for the standard $\phi F\tilde F$ — but the paper should state this assumption explicitly. As written, the equation glosses over the actual line-of-sight calculation.

### P2-M8 — "9σ test" forecast ignores LiteBIRD's calibration-limited systematic floor.

The forecast $\sigma(\beta)\approx 0.03°$ is the **statistical** sensitivity. LiteBIRD's *total* error budget will include polarization-angle calibration, which is the same source of systematics that limits Planck/ACT. The "9σ" claim assumes systematics-free measurement. Even the LiteBIRD collaboration paper (cited) emphasizes the calibration-limited regime. Required fix: include systematic floor in the forecast.

### P2-M9 — The Bayes factor is "indicative" but quoted in the abstract.

Sec. 3.4 admits "indicative; prior-dependent" but the abstract prominently states "$\ln B = 5.17$." Either it's evidence or it's not. If prior-dependent at the $\pm 0.7$ level over a factor-of-2 prior choice, the headline value is misleading.

---

## MINOR findings

### P2-Mi1 — Inverse-variance combination assumes independence.

Planck NPIPE and the Eskilt joint analysis share Planck data; combining $0.30\pm 0.11°$ (Planck) and $0.215\pm 0.074°$ (ACT) as independent is approximately fine if ACT is independent. But the abstract's "joint Planck+ACT" $0.342\pm 0.094°$ already includes both — combining it further would double-count. The paper avoids this by using different numbers in different places (see E4), but should state independence assumption.

### P2-Mi2 — Eq. (10) significance formula assumes zero null and zero forecast uncertainty.

"Significance $= 0.27/0.03 = 9\sigma$" is the SNR for detecting $\beta=0.27$ against $\beta=0$ with $\sigma=0.03$. Standard, but should write it as "$|\beta|/\sigma(\beta)$" to be unambiguous.

### P2-Mi3 — Figure 2 (p. 5) is filler.

Three Gaussian posteriors that the body text already says are consistent. Adds nothing beyond a numerical table. Remove or replace with something more informative.

### P2-Mi4 — Conclusion section restates abstract verbatim.

Sec. 7 (p. 6) is 90% redundant with the abstract. For a 6-page paper, the conclusion adds no new synthesis.

### P2-Mi5 — Quoting "3.6σ" for the Eskilt et al. signal.

$0.342/0.094 = 3.64\sigma$ ✓. OK.

### P2-Mi6 — The phrase "natural in the sense that..." in abstract.

Three justifications offered: $f_a\sim M_{\rm Pl}$, $m\sim H_0$, $\theta_i\sim\mathcal{O}(1)$. None of these are derived. The first is a statement about UV scales; the second is finely tuned to within one decade of $H_0\sim 10^{-33}$ eV (in fact see Fig. 1 — the prior runs over five decades $[-35,-30]$ and the posterior is prior-edge dominated; "$m\sim H_0$" is asserted, not preferred by data). "Natural" is doing a lot of work here.

### P2-Mi7 — "fphoton" vs "$f_{\rm photon}$" notation never defined.

Eq. (5) uses $f_{\rm photon}\times C_0$, but $f_{\rm photon}$ is introduced nowhere. Looks like it might be $f_a$ in disguise, but cannot tell.

---

## NITs

### P2-N1 — Affiliation: "Independent Researcher, Los Angeles, California, USA" with personal email. Fine, but consider arXiv-categorize affiliation.

### P2-N2 — Sec. 3 typography: "$\log_{10}(m/{\rm eV})$" formatted inconsistently between Sec. 3.3 and Fig. 1.

### P2-N3 — "Caγ" used in some places and "$C_0$" in others to denote the same coefficient.

### P2-N4 — Bibliography: "Diego-Palazuelos and Komatsu 2025" has no arXiv ID or journal volume.

---

## Audit of bibliography/citation traceability

| Citation | Claim | Verified? |
|---|---|---|
| Minami & Komatsu 2020 | $\beta=0.35\pm 0.14°$, $2.5\sigma$ | Title correct; abstract reports $2.4\sigma$. Minor discrepancy. |
| Eskilt & Komatsu 2022 | $\beta=0.30\pm 0.11°$ Planck NPIPE | Eskilt & Komatsu PRD 2022 reports $0.30°\pm 0.11°$ (close) — OK. |
| Diego-Palazuelos & Komatsu 2025 | ACT DR6 $0.215\pm 0.074°$ | No arXiv ID; cannot verify. ACT DR6 has not (to this reviewer's knowledge) released $\beta$ at this precision. **Flagged.** |
| LiteBIRD Collaboration 2023 | $\sigma(\beta)\approx 0.03°$ | LiteBIRD PTEP 2023 supports this order of magnitude — OK. |
| Fujita et al. 2021 | "Planck-scale ALP produces $\beta\sim 0.3°$" | Roughly consistent with Fujita et al. PRD 2021 conclusions — OK. |
| Namikawa, Murai, Naokawa 2025 | "Superior mass constraints" | Cited as "in preparation" — **inadmissible**. |
| Golden 2026a, 2026b | Companion papers | No arXiv ID — **inadmissible**. |

---

## Summary of audit-tag checks

- No "R7", "R8", "round", "superseded", or version-history language in the rendered PDF body. ✓
- No duplicate phrases like "canonical canonical-mask." ✓
- The reviewer metadata block is not in the PDF. ✓

---

## Verdict on the contribution

The paper itself admits (Sec. 6): *"the ALP birefringence model class is well-studied... Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces $\beta\sim 0.3°$, and Namikawa, Murai & Naokawa provide superior ALP mass constraints... Our contribution is not the model itself, but rather the specific parameter identification ($f_a\sim M_{\rm Pl}$, $m\sim H_0$) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency."*

The "specific parameter identification" is identical to Fujita et al.'s. The "inference framework" is a Gaussian product of two published numbers with under-sampled MCMCs. This is not new physics; it is not a new method; and the internal-consistency demonstration breaks under recomputation. PRD is not the venue for this.

---

## Summary recommendation

**REJECT**

The paper has an internally inconsistent central derivation (E1: $\Delta\phi/f_a$ is computed as 0.24 in Eq. (1) but used as $10^{-2}$ in Sec. 2.2 to get the headline 0.27°), uses three different "observed" $\beta$ values interchangeably (E4), bases the marquee "9σ" LiteBIRD forecast on a number that does not appear in any inference table (E5), introduces a key parameter $f_{\rm photon}$ that is never defined while quoting its value to 3 significant figures (E2), cites a "joint Planck+ACT" Eskilt et al. paper that is not in the bibliography (E3, E10), reports a Bayes factor from MCMC chains of 720–6,840 samples (E7), and exhibits direct contradictions between Figure 1 and the body text (E9). The author admits in Sec. 6 that the model class and parameter identification are not new (Fujita et al. 2021), so the residual contribution rests entirely on the inference, which does not survive recomputation. This is not at PRD's bar. If resubmitted, the paper would need: (i) an honest field-evolution calculation, (ii) properly sampled MCMCs ($\geq 10^5$ samples), (iii) consistent observational inputs throughout, (iv) removal of all "in preparation" and companion-paper self-citations, and (v) reconciliation between abstract claims and Discussion-buried systematic caveats. At that point it would still be a derivative analysis paper, more suited to JCAP or PRD as a brief note than as a full PRD article.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Re-examination

Several non-trivial issues escaped the initial pass. Categorized by the user's audit checklist:

---

## NEW ESSENTIAL findings

### P2-E11 — Abstract misidentifies the dataset.

**Abstract:** *"We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data..."*

**Sec. 3.1, p. 2:** Lists the Planck input as **"Planck NPIPE [Eskilt and Komatsu, 2022]"**, not HFI.

These are different data products. The Minami-Komatsu 2020 result used Planck HFI 2018; the Eskilt-Komatsu 2022 result used the NPIPE reprocessing (an iterative joint HFI+LFI pipeline with different foreground handling). The abstract advertises one, the body uses another. This matters because the original Planck HFI result is what is cited later as the "earlier" Minami-Komatsu analysis. The author appears to have conflated the two. Required fix: reconcile abstract with Sec. 3.1.

### P2-E12 — The MCMC mass posterior contradicts the paper's central "naturalness" pitch.

**Sec. 2.1:** *"For m ∼ H₀ and fₐ ∼ MPl, the field... begins rolling at z ∼ O(1) when H(z) ∼ m."*

**Fig. 1 marginal:** $\log_{10}(m_a/\text{eV}) = -31.4^{+1.4}_{-1.2}$.

Since $\log_{10}(H_0/\text{eV}) \approx -32.9$, the posterior peak corresponds to $m \approx 30\,H_0$, **not** $m \sim H_0$. The "$+1.4$" error extends to $\log_{10}(m/\text{eV}) = -30$, which is the **upper prior edge** (prior is $[-35,-30]$). The data wants $m$ *higher* than the prior allows. So:

(i) The central inferred mass is not $H_0$, undermining the "natural" prescription $m\sim H_0$;
(ii) The posterior is **prior-truncated from above**, making the central value a prior artifact.

The abstract's claim that "$m \sim H_0$ ensures the field is rolling today" is contradicted by the paper's own data preference. Required fix: widen the prior to $[-35,-26]$ and report whether the posterior is bounded by physics or by the prior; if the former, retract the $m\sim H_0$ naturalness claim.

### P2-E13 — The inferred coupling-misalignment product is inconsistent with the prediction's input.

**Sec. 2.2:** The headline $\beta \approx 0.27°$ is derived assuming $C_0 \sim 1$, $\theta_i \sim 1$ (product $\approx 1$).
**Sec. 3.3, Eq. (8):** Inferred $C_{a\gamma} \times \theta_i = 3.4 \pm 1.1$.

The inferred product is **3.4σ above** the input product used for the prediction. Either the model's "natural" inputs ($C_0\sim 1$, $\theta_i\sim 1$) are wrong, or the inference is over-fitting. If the true product is 3.4, then the back-of-the-envelope from Sec. 2.2 should give $\beta \approx 3.4 \times 0.27° \approx 0.9°$, three times the observed value. The naturalness claim only survives by conflating the linear product $C_0\theta_i$ in Eq. (2) with the inferred product in Eq. (8) and pretending the factor-of-3 discrepancy doesn't matter. Required fix: explain why $C_0\theta_i\sim 1$ in the prediction but $3.4$ in the inference.

---

## NEW MAJOR findings

### P2-M10 — Sec. 2.2 contains a meaningless dimensional phrase.

**Sec. 2.2, p. 2:** *"the cosmological field evolution gives $\Delta\phi/f_a \sim 10^{-2}$ (from the ratio of field displacement to decay constant over the Hubble time)..."*

$\Delta\phi/f_a$ is already dimensionless. "Over the Hubble time" doesn't divide anything — there is no time ratio in $\Delta\phi/f_a$. The parenthetical is dimensional word salad inserted to make a magic number ($10^{-2}$) sound derived. Required fix: either properly derive $10^{-2}$ from the field equation, or remove the phrase.

### P2-M11 — Sec. 2.1 roll-onset claim is inconsistent with $m=H_0$.

**Sec. 2.1, p. 1:** *"begins rolling at $z\sim O(1)$ when $H(z)\sim m$."*

In ΛCDM, $H(z=1) = H_0\sqrt{\Omega_m(1+z)^3+\Omega_\Lambda} \approx 1.8\,H_0$. So if $m = H_0$, then $H(z=1)\approx 1.8\,m$, and the field is still Hubble-frozen at $z=1$ — it only starts rolling at $z\to 0$. The "begins rolling at $z\sim O(1)$" requires $m \gtrsim 2H_0$, not $m\sim H_0$. (This is consistent with the MCMC preferring $m\sim 30\,H_0$ — E12 — but contradicts the abstract's "$m\sim H_0$".) Required fix: pick one mass scale and be consistent.

### P2-M12 — Sec. 6 misstates the Minami-Komatsu self-calibration method.

**Sec. 6, p. 5:** *"The validity of this method depends on the instrumental polarization angles being constant across the focal plane..."*

This is backwards. The Minami-Komatsu method's defining feature is that it **does NOT require** polarization angles to be constant across the focal plane — it explicitly fits per-detector miscalibration $\alpha_i$ simultaneously with $\beta$. What the method **does** assume is that the per-detector miscalibrations are stable in time and that the foreground EB spectrum is consistent with zero. The Discussion mis-describes the very method the paper's data depend on. Required fix: rewrite to accurately describe what the method does and does not assume.

### P2-M13 — Run 2's $\beta$ posterior is never quoted in the body.

**Fig. 1 marginal:** $\beta = 0.324 \pm 0.099°$ (Run 2, $C$ free).
**Body, Sec. 3.3:** Quotes $\beta_{\text{ALP}} = 0.336 \pm 0.107°$ (Run 1, $C=8$ fixed) and $\beta_{\text{free}} = 0.344 \pm 0.096°$ (Run 3), but **not** $\beta$ for Run 2.

Yet Fig. 2 plots all three. The body silently omits the value the figure plots. The omission is consequential because Run 2 is the "physically motivated" run (treating $C$ as a free parameter), and its $\beta$ is the most appropriate point estimate. Required fix: quote Run 2's $\beta$ in the body and reconcile with Eq. (8).

### P2-M14 — Eq. (5) appears to be a meaningless rescaling.

The recomputation $\beta_{\text{combined}}/0.140° = 0.242/0.140 = 1.73$ and $\sigma_\beta/0.140° = 0.061/0.140 = 0.44$ exactly reproduces Eq. (5). So $f_{\text{photon}}\times C_0 = \beta_{\text{combined}}/(0.140°)$. The denominator $0.140°$ is the **original Minami-Komatsu 2020 error bar**, used here as a reference scale with no physical motivation. Equation (5) is therefore $\beta_{\text{combined}}$ rescaled by a meaningless historical number, presented as a "coupling parameter." Required fix: either define $f_{\text{photon}}$ from physics (with units), or remove Eq. (5).

---

## NEW MINOR findings

### P2-Mi8 — The anomaly coefficient is denoted four different ways.

- **Eq. (2):** $C_0$
- **Eq. (5):** $C_0$
- **Sec. 3.3 prior:** $C_{a\gamma}$
- **Eq. (8):** $C_{a\gamma}$
- **Table 1:** $C$
- **Fig. 1:** $C_{a\gamma}$ (subscripted $a\gamma$ rendered as "aγ")

A reader cannot tell whether $C_0$, $C_{a\gamma}$, and $C$ are the same parameter or different ones. (E.g., is the $C=8$ fixed in Run 1 the same $C_0$ that Eq. (2) takes to be $\sim 1$? If yes, why is the "natural" benchmark fixed at 8?)

### P2-Mi9 — Significance numbers in Sec. 1 vs. Abstract.

- **Abstract:** "the 3.6σ isotropic birefringence signal"
- **Sec. 1, p. 1:** "Combined, the evidence exceeds 3.5σ."

These refer to the same Eskilt + ACT combination. Two thresholds for the same number. Minor but sloppy.

### P2-Mi10 — Sec. 1 makes a combined-evidence claim before the combination is defined.

**Sec. 1:** *"Combined, the evidence exceeds 3.5σ."* But Sec. 3.2 is where any combination is actually performed. Forward reference is missing; reader assumes the 3.5σ is a literature result, when in fact it is the paper's own re-combination.

### P2-Mi11 — Sec. 3.1 explicitly admits its method is inferior.

**Sec. 3.1, p. 2:** *"...the Eskilt et al. joint analysis value $\beta_{\text{obs}} = 0.342\pm 0.094°$, which differs because it fits the full EB cross-spectrum rather than combining point estimates."*

The author tells the reader that the joint EB-spectrum fit is the correct procedure, then performs an inferior point-estimate combination anyway and reports it as "the combined constraint" (Eq. 4). The justification for choosing the inferior method when the better number is available is never given. Required fix: use the joint EB fit throughout, or justify the choice.

### P2-Mi12 — Comparison of "3.9σ" (statistical-only) and "9σ" (statistical-only forecast) without systematic-floor caveat.

The abstract juxtaposes a current measurement significance ($3.9\sigma$, which includes whatever systematics Planck/ACT carry) and a future-instrument SNR ($9\sigma$, statistics only). These are different null procedures: the current $3.9\sigma$ is data-vs-zero; the LiteBIRD $9\sigma$ is signal/statistical-noise assuming systematic floor = 0. The paper itself (Sec. 6) acknowledges $0.1{-}0.3°$ potential systematic floors — which, if real, would limit LiteBIRD to $\sim 3$-$\sigma$, not 9. Required fix: caveat the LiteBIRD significance with the same systematic floor the Discussion warns about.

### P2-Mi13 — Run 2 marginal $\theta_i$ has a $-1.1$ error from a central value of $1.33$, hitting the prior at $0.01$.

**Fig. 1:** $\theta_i = 1.33^{+0.44}_{-1.1}$. Lower bound $= 0.23$, prior min $= 0.01$. The strong asymmetry ($-1.1$ vs $+0.44$) and the prior at 0.01 suggest the posterior is mass-piled near the lower prior edge with a non-Gaussian tail. The triangle plot's diagonal degeneracy between $C_{a\gamma}$ and $\theta_i$ ridge-rides toward small $\theta_i$ and large $C_{a\gamma}$, exactly where the product $C_{a\gamma}\theta_i$ becomes ill-constrained. This is consistent with the inferred product $3.4\pm 1.1$ — but the marginal mean of $C_{a\gamma}\times$ marginal mean of $\theta_i = 13.4\times 1.33 = 17.8$, not 3.4. The degeneracy is so strong that the marginal means are decorrelated from the joint product. The paper should plot the 1D posterior on the product directly. Required fix: show $p(C_{a\gamma}\theta_i)$ as a separate panel.

---

## NEW NITs

### P2-N5 — "Eskilt et al." vs. "Eskilt and Komatsu".

The abstract writes *"Eskilt et al."* for a 2-author paper (Eskilt & Komatsu 2022) and for the unattributed "joint analysis." Style inconsistency. Per most physics journals, *"et al."* is appropriate for 3+ authors. With 2, write *"Eskilt and Komatsu"*.

### P2-N6 — Fig. 2 caption says "$\beta_{\text{obs}} = 0.342 \pm 0.094°$" but the green band in Fig. 2 looks centered higher.

Visually inspecting Fig. 2, the dotted vertical line ("Observed") sits near $\beta\approx 0.34°$, OK. The green band (presumably $\pm 1\sigma$) spans roughly $0.25°$ to $0.44°$, half-width $\approx 0.10°$, broadly consistent with $\sigma=0.094°$. Within plotting tolerance.

### P2-N7 — Sec. 3.3 priors are stated but Table 1 doesn't list them.

Table 1 lists models and samples but not the priors used in each run. For an MCMC paper, prior boundaries belong in the table.

### P2-N8 — "ECH gravity" abbreviation never expanded.

Sec. 5 introduces "ECH gravity" with no prior definition. Probably "Einstein-Cartan-Holst," but a self-contained paper should expand on first use.

---

## Summary of NEW findings impact

The most damaging new findings:

- **E12** (the data prefers $m\sim 30 H_0$, not $m\sim H_0$, and is prior-truncated at the upper edge) directly contradicts the paper's central "naturalness" message that *"$m \sim H_0$ ensures the field is rolling today."* The MCMC actually shows the data **does not want** $m=H_0$.
- **E13** (the inferred coupling-misalignment product is 3.4, not 1) means the parameters that fit the data are not the parameters used in the back-of-envelope.
- **M14** (the "$f_{\text{photon}}\times C_0 = 1.73\pm 0.44$" abstract number is just $\beta_{\text{combined}}/0.14°$, a rescaling by the original 2020 Planck HFI error bar with no physical content) reveals that one of the four numbers in the abstract is meaningless arithmetic.
- **E11** (the abstract claims Planck HFI but the body uses Planck NPIPE) is a careless dataset misidentification visible from the abstract.

Combined with the original review's findings, the paper now exhibits: a broken central derivation (E1), an unattributed primary observational input (E3), four different "observed" $\beta$ values used interchangeably (E4), a forecast against a number not in any posterior (E5), undersampled MCMCs (E7), figure-text contradictions (E9, M13), data-vs-naturalness contradictions (E12, E13), and a meaningless headline coupling number (M14, E2).

**Recommendation stands: REJECT.**