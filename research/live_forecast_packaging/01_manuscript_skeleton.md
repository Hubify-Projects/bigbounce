# 01: Manuscript Skeleton

## Abstract (~200 words)
- State the prediction: f_NL^local = -35/8 from matter bounce (Cai et al. 2009)
- Note mechanism independence (ECH, LQC, etc. give same result)
- State SPHEREx forecast: σ(f_NL) ~ 0.7 (bispectrum), ~6σ detection
- State MegaMapper forecast: σ(f_NL) ~ 0.5-1.5, 3-9σ (conditional on systematics)
- Note key systematic: ultra-large-scale mode access, GR projection effects, b_φ uncertainty
- Conclude: SPHEREx provides the more robust first test; MegaMapper provides the more powerful but fragile follow-up
- No overclaim about "proving" bounce

## 1. Introduction (~2 pages)
**Purpose:** Motivate the paper. Establish inflation as baseline, bounce as alternative, f_NL as discriminator.
**Key points:**
- Inflation predicts f_NL ≈ 0 (single-field consistency relation)
- Matter bounce predicts f_NL = -35/8 (parameter-free, from growing mode)
- This is 300× larger than slow-roll and opposite sign
- Next-gen LSS surveys can test this sharply
- Brief mention: bounce mechanism (ECH, LQC) is perturbation-transparent — prediction is generic
**Equations needed:** f_NL definition, Maldacena consistency relation
**Claims that belong:** "This paper presents forecasts for testing f_NL = -35/8..."
**Claims that do NOT belong:** "We derive f_NL from first principles..." (Cai et al. did that)

## 2. The Matter-Bounce Bispectrum (~2 pages)
**Purpose:** Present the theoretical benchmark. NOT a re-derivation — a summary with verification.
**Key points:**
- Cubic action in matter contraction (cite Maldacena 2003, Cai et al. 2009)
- Shape function AT = (3/(256Πk²)){polynomial}
- Verified at 3 special cases: squeezed -35/8, equilateral -255/64, folded -9/4
- Note on literature discrepancy resolution (cosmic vs conformal time conventions)
- Shape is "effectively local" for LSS purposes (exact in squeezed limit)
**Equations needed:** Shape function, |B|_NL definition, 3 benchmark values
**Figures needed:** Shape function plot over triangle space (or at least squeezed convergence)
**Tables needed:** Prediction package table

## 3. Observational Framework (~1.5 pages)
**Purpose:** Establish the estimator mapping. Why SDB and bispectrum are the right channels.
**Key points:**
- Scale-dependent bias: Δb(k) ∝ f_NL·(b₁-1)/k² (Dalal et al. 2008)
- Galaxy bispectrum: direct three-point measurement
- For the matter-bounce shape: cos(θ) = 1.0 for SDB (squeezed limit exact)
- Both channels available for SPHEREx and MegaMapper
**Equations needed:** SDB formula, Fisher information expression
**Claims that belong:** "The matter-bounce shape projects exactly onto the local template for SDB"
**Claims that do NOT belong:** Detailed estimator pipeline description (that's the experimentalists' job)

## 4. SPHEREx Forecast (~2 pages)
**Purpose:** Present the near-term test.
**Key points:**
- Mission overview (all-sky, photometric, IR, multi-tracer across z-bins)
- Bispectrum forecast: σ(f_NL) = 0.7 (cite arXiv:2311.13082)
- Combined P+B: σ(f_NL) = 0.5
- Photo-z degradation: moderate (3-18%)
- Significance for f_NL = -4.375: 6.3σ (B only), 8.75σ (P+B)
- Decision thresholds
**Tables needed:** SPHEREx significance scenarios
**Figures needed:** Decision threshold plot

## 5. MegaMapper Forecast (~2 pages)
**Purpose:** Present the long-term decisive test.
**Key points:**
- Survey concept (spectroscopic, z=2-5, multi-tracer LBGs)
- SDB forecast: σ(f_NL) = 0.5 (design, multi-tracer)
- Systematics: GR projection effects (~20σ raw, ~0.3-1σ after correction)
- b_φ uncertainty: up to factor-several degradation if uncalibrated
- Multi-tracer: 15-20% improvement beyond single-tracer
- k_min dependence: dominant fragility
- Significance range: 3-7σ (realistic), 8.75σ (ideal)
**Tables needed:** MegaMapper significance scenarios, systematics impact table
**Figures needed:** Fisher sensitivity to k_min

## 6. Robustness and Systematics (~2 pages)
**Purpose:** Honest assessment of fragilities.
**Key points:**
- k_min is the dominant fragility for SDB channel
- GR projection effects must be modeled (computable but uncertain for LBGs at z>2)
- b_φ uncertainty degrades constraints unless simulation-calibrated priors are used
- Bispectrum channel (SPHEREx) avoids some SDB systematics
- Combined P(k) + bispectrum is more robust than either alone
**Tables needed:** Systematics threat matrix
**Figures needed:** Fisher robustness surface (σ vs k_min)

## 7. Comparison with Inflation (~1 page)
**Purpose:** Sharpen the discrimination.
**Key points:**
- Single-field: f_NL ≈ 0 (off by 300×, wrong sign)
- Standard curvaton: minimum f_NL ≈ -1.25 (cannot reach -4.375)
- Multi-field: can reach -4 but requires engineered construction + free parameters
- The COMBINATION of magnitude + sign + parameter-free is what makes the bounce distinctive
**Claims that do NOT belong:** "This rules out inflation" — it doesn't, it disfavors single-field

## 8. Discussion and Conclusion (~1.5 pages)
**Purpose:** State what was established, what remains, and what the measurement means.
**Key points:**
- f_NL = -35/8 is a generic, mechanism-independent matter-bounce prediction
- SPHEREx provides the more robust first test (~2028, ~6σ via bispectrum)
- MegaMapper provides the more powerful follow-up (~2032+, 3-7σ, fragile-but-strong)
- A robust detection of f_NL ≈ -4 would provide strong evidence favoring bounce over single-field inflation
- A null result (f_NL consistent with zero) would strongly disfavor the quasi-dust matter bounce
- The dominant systematic uncertainty is ultra-large-scale mode access, not theoretical modeling
**Claims that do NOT belong:** "This constitutes the first proof of a pre-Big-Bang contracting phase"

## Total: ~15 pages + references
