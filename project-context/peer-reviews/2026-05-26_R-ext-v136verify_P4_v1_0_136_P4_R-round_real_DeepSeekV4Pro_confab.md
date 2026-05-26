# P4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v136verify_P4_v1_0_136
**Wall time**: 147.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=98756, completion=10860, reasoning=9182, total=109616

---

## Findings

### PAPER-DEE-M1 — MAJOR
**§Conclusions (enumerated item 2).** The text claims the equivariant spiral subsample is “∼2.5× larger than the Shamir 2022 DESI Legacy spiral sample” and parenthetically cites “nearly 1.3×10⁶ spirals” from Shamir’s abstract. Shamir 2022’s abstract says “nearly 1.3×10⁶ **galaxies**”, not spirals; the paper’s own §I correctly notes that after Ganalyzer cuts the spiral sample is ∼2×10⁵. The correct size ratio is therefore 3.2×10⁶ / 2×10⁵ ≈ 16×, not 2.5×. This misstatement inflates the apparent sample-size advantage by a factor of ∼6 and appears in a headline comparison.  
**Fix:** Replace “∼2.5× larger than the Shamir 2022 DESI Legacy spiral sample (``nearly 1.3×10⁶ spirals'' per the published abstract)” with the correct ratio (∼16×) using the 2×10⁵ spiral count, or remove the quantitative claim and simply note the samples are not like‑for‑like.

### PAPER-DEE-M2 — minor
**Abstract, §IX Data Availability, and Conclusions.** The paper version is `v1.0.136`, but the abstract and data-availability section repeatedly cite the immutable release tag `paper4-v1.0.134`. The artifacts, scripts, and catalog are therefore pinned to an older version; a reader who fetches the release tag will not obtain the v1.0.136 additions (e.g., the hard‑label variance derivation).  
**Fix:** Update the release tag to `paper4-v1.0.136` (or the actual tag that matches the submitted manuscript) throughout the abstract, footnotes, and Data Availability section.

### PAPER-DEE-M3 — minor
**Abstract (real‑space dipole).** The abstract states “∼0.6% residual amplitude” for the real‑space Catalog C dipole, but no artifact, table, or equation in the abstract or the immediately referenced dipole section directly yields this number. The dipole significance (0.43σ) is given, but the amplitude is not tabulated.  
**Fix:** Either cite the specific artifact that contains the fitted dipole amplitude (e.g., `dipole/summary.json`) or replace “∼0.6%” with the significance and a pointer to the section where the amplitude is reported.

### PAPER-DEE-M4 — minor
**Abstract (CW fraction uncertainty).** The abstract quotes the global CW fraction as “0.4974 ± 0.000279” without qualification. The paper’s own §IV.B notes that this binomial error assumes independent classifications and that spatial correlations (seeing, PSF, depth) reduce the effective sample size, so “the true uncertainty may be larger.” Presenting the naïve binomial uncertainty as the headline precision is potentially misleading.  
**Fix:** Add a parenthetical “(binomial)” after the uncertainty, or replace with a conservative effective‑sample‑size uncertainty and cite the relevant caveat.

### PAPER-DEE-M5 — nit
**Abstract (post‑MASTER ℓ=1 significance).** The abstract reports the subsample‑mask MASTER result as “−0.122σ”. The underlying distribution is an empirical 500‑MC null; the paper later states the rank‑based p‑value is ≈0.45. Quoting a Gaussian‑equivalent z‑score without the empirical p‑value may give a false impression of parametric precision.  
**Fix:** Append “(p_MC≈0.45)” or replace “−0.122σ” with “p_MC≈0.45 (Gaussian‑equivalent −0.12σ)” to make the non‑parametric nature clear.

### PAPER-DEE-M6 — nit
**Abstract (canonical‑mask +3.64σ).** The abstract states the canonical‑mask post‑MASTER direct‑MC residual is “+3.64σ” (moment‑z). The paper later clarifies that the empirical‑rank two‑sided p_MC = 15/500 = 0.030, which does not correspond to a 3.64σ Gaussian tail. Using the moment‑z as the headline number without the empirical p‑value overstates the significance under a non‑Gaussian null.  
**Fix:** Report the empirical p‑value alongside the moment‑z, e.g., “+3.64σ (moment‑z; empirical p_MC=0.030)”, to avoid misinterpretation.
