# P2_v1730 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P2_v1730_R3_R-round_real
**Wall time**: 184.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=31095, completion=13126, reasoning=12043, total=44221

---

## PAPER-GEM-B1: Confabulated / Anachronistic Citations (BLOCKER)
**Section:** Throughout (e.g., Sec 2.3, Sec 7.3, Sec 8.1, Sec 9.5)
**Issue:** The manuscript relies on several hallucinated or anachronistic citations to support load-bearing claims. Specifically: `Zhu:2026echoes` (future/fake), `Jung2025PlanckPR4fNL` (Planck PR4 $f_{\rm NL}$ was published by Jung et al. in 2022/2023, not 2025), `Jolicoeur:2025` (future/fake), and `DiegoPalazuelos2025` (ACT DR6 birefringence does not have a 2025 Diego-Palazuelos paper; Diego-Palazuelos et al. 2022 is Planck PR4). 
**Fix:** Remove all confabulated 2025/2026 citations and replace them with the actual published literature (e.g., Jung et al. 2022/2023 for Planck PR4).

## PAPER-GEM-B2: QSFI Scaling Dimension and Local Limit Reversed (BLOCKER)
**Section:** 6.3 (Bayes-factor closure) and 9.4 (Joint Forecast)
**Issue:** The text claims that QSFI at $\mu/H = 3/2$ reproduces the local template, and $\mu/H = 0$ produces a super-squeezed $(k_3/k_1)^{-3/2}$ divergence. This is physically backwards. In QSFI, the squeezed bispectrum scales relative to the local template as $(k_3/k_1)^{3/2 - \nu}$ where $\nu = \sqrt{9/4 - \mu^2/H^2}$. At $\mu/H = 0$ ($\nu=3/2$), the ratio is $(k_3/k_1)^0 = 1$, which is exactly the local shape. At $\mu/H = 3/2$ ($\nu=0$), the ratio is $(k_3/k_1)^{3/2}$, which is suppressed in the squeezed limit (equilateral-like). The text incorrectly subtracts an extra $3/2$ in the exponent.
**Fix:** Correct the QSFI scaling dimension math: $\mu/H \to 0$ is the local limit (where the Bayes factor against the bounce collapses), and $\mu/H \to 3/2$ is the equilateral-like suppressed limit.

## PAPER-GEM-M1: Erroneous Error Bar in Cosmoglobe Birefringence (MAJOR)
**Section:** 9.5 (Caveats)
**Issue:** The text quotes the Cosmoglobe DR1 II reanalysis (`Eskilt2023Cosmoglobe`) as reporting a cosmic birefringence angle of $\beta = 0.35^\circ \pm 0.70^\circ$. The actual published error bar for the Cosmoglobe DR1 WMAP+Planck reanalysis (Eskilt et al. 2023, A&A 675, A82) is $\pm 0.14^\circ$. An error of $0.70^\circ$ is a factor of 5 too large and misrepresents the precision of the measurement.
**Fix:** Correct the Cosmoglobe DR1 error bar to $\pm 0.14^\circ$.

## PAPER-GEM-M2: Contradictory Shot-Noise Claim for Anomaly Tracers (MAJOR)
**Section:** 4 (SPHEREx Forecast)
**Issue:** The text claims a preliminary Fisher forecast on anomaly tracers projects a "10--20% improvement" in $\sigma(f_{\rm NL})$, but immediately follows with a "Shot-noise caveat" acknowledging that the low number density of these tracers ($\bar{n} \sim 10^{-5}$) causes a "15--30% degradation". It is mathematically contradictory to quote a 10-20% improvement as an "upper bound" if the baseline shot-noise penalty (15-30%) entirely erases the gain.
**Fix:** Clarify whether the 10-20% improvement is net of the shot-noise penalty, or remove the quantitative improvement claim for anomaly tracers until a proper shot-noise-inclusive Fisher matrix is computed.

## PAPER-GEM-m1: Inconsistent Citation Year for Heinrich et al. (minor)
**Section:** Abstract, 4, 9.4
**Issue:** The text repeatedly refers to the SPHEREx multi-tracer bispectrum forecast as "Heinrich \etal~2024" in the prose, but the bibliography key and some inline references use `Heinrich:2023`. 
**Fix:** Standardize the year to match the bibliography entry consistently.
