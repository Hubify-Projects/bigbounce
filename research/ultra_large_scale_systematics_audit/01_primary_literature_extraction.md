# 01: Primary Literature Extraction

## Paper 1: Barreira (2022) — "Can we actually constrain f_NL using galaxy surveys?"
**arXiv: 2205.05673**

### Key Finding
Nearly ALL existing f_NL constraints and forecasts assume precise knowledge of the PNG bias parameter b_φ. This assumption is unjustified.

### Quantitative Impact
Using identical BOSS DR12 data but different b_φ assumptions:
- Strongest: f_NL = 16 ± 16
- Loosest: f_NL = 230 ± 226
- **Variation: up to 14× in σ(f_NL) depending on b_φ treatment**

### Key Warning
"Marginalization over b_φ with wide priors is not conservative, and leads in fact to biased constraints through parameter space projection effects."

### Implication for Us
The published MegaMapper/SPHEREx σ(f_NL) ~ 0.5 assumes b_φ is well-known. If b_φ is uncertain by even ~30%, σ(f_NL) could degrade by a factor of several. This is an ADDITIONAL degradation on top of the k_min issue.

**Severity: HIGH.** This is a fundamentally different systematic from k_min — it affects the AMPLITUDE of the SDB signal, not just the accessible k-range.

---

## Paper 2: arXiv:2511.09466 — "Unbiased analysis of primordial non-Gaussianity: the multipoles of the full relativistic power spectrum"

### Key Finding
Ignoring relativistic effects (Doppler, lensing, ISW) biases f_NL by **~20σ for MegaMapper-like surveys.**

### Quantitative Impact
- Euclid-like (H-alpha): ~3σ bias in f_NL
- **MegaMapper-like (Lyman-break at z>2): ~20σ bias in f_NL**
- Bright-faint multi-tracer split: 15-20% improvement (helps but doesn't solve the problem)

### Key Point
The relativistic effects create signals that scale as 1/k² on ultra-large scales — EXACTLY mimicking the f_NL SDB signal. The higher redshift of MegaMapper's LBG sample makes this WORSE, not better.

### Implication for Us
Even if k_min ~ 10⁻⁴ is accessible, the primordial f_NL signal must be disentangled from a relativistic "fake" f_NL of potentially comparable magnitude. The GR contamination IS computable in principle, but requires accurate modeling of the luminosity function, magnification bias, and evolution bias at z > 2.

**A 20σ bias means: if not properly modeled, the GR effects would completely overwhelm our -4.375 signal.** The GR "fake" f_NL is of order 1-5 (depending on the survey), comparable to our signal of 4.375.

**Severity: CRITICAL.** This is not a nuisance — it is a fundamental contamination that must be modeled and subtracted.

---

## Paper 3: arXiv:2311.13082 — "Measuring f_NL with the SPHEREx Multi-tracer Redshift Space Bispectrum"

### Key Finding
SPHEREx can achieve σ(f_NL) = 0.7 from the bispectrum alone, and σ(f_NL) = 0.5 when combined with the power spectrum.

### Quantitative Impact
- Bispectrum only: σ = 0.7
- With power spectrum: σ = 0.5
- Photo-z degradation (ℓ_max=0 mode): 18% increase in σ
- Photo-z degradation (ℓ_max=2): 3% increase only
- Multi-tracer: better redshift samples dominate while worse samples reduce cosmic variance

### Key Point
The SPHEREx forecast is MORE ROBUST than our simple Fisher code suggested because:
1. It uses the BISPECTRUM (3-point function of galaxies), not just the power spectrum
2. The bispectrum provides additional information independent of scale-dependent bias
3. Multi-tracer across redshift bins provides effective cosmic variance cancellation
4. Photo-z effects are moderate (3-18% degradation) because the best-redshift samples dominate

### Implication for Us
SPHEREx's σ(f_NL) = 0.5-0.7 is more credible than our simple Fisher code suggested. The bispectrum channel provides a QUALITATIVELY DIFFERENT measurement that doesn't rely solely on ultra-large-scale modes.

**For our signal: significance = 4.375/0.7 = 6.3σ (bispectrum only) or 4.375/0.5 = 8.75σ (combined)**

**Severity of SPHEREx concerns: REDUCED.** The bispectrum channel makes SPHEREx more robust than a pure SDB forecast would suggest.

---

## Summary: Three Threats, Ranked

1. **Relativistic projection effects (20σ bias for MegaMapper)** — CRITICAL, must be modeled
2. **b_φ uncertainty (up to 14× degradation in σ)** — HIGH, need theoretical priors
3. **k_min access (100-1000× impact in our Fisher scan)** — HIGH, but partially mitigated by bispectrum channel

The game-changer from this literature review: **the bispectrum estimator (Paper 3) provides a SECOND channel** that is less sensitive to ultra-large-scale systematics. SPHEREx's bispectrum-based forecast is more robust than our power-spectrum-only Fisher scan.
