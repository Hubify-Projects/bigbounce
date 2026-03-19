# Final Verdict: Observational Decision Framework

## 1. Best Current Full Observational Discriminator Package

| Observable | Prediction | Method | Detection |
|-----------|-----------|--------|-----------|
| **f_NL^local = -4.375** | Parameter-free | Scale-dependent bias (LSS) | MegaMapper: 8.75σ |
| Sign(f_NL) = negative | Parameter-free | Same | Same |
| n_s = 0.964 | 1 free parameter | CMB power spectrum | Already measured |
| r ~ 10⁻⁴ | LQC-dependent | CMB B-modes | Below LiteBIRD threshold |

**The discriminator is ONE number: f_NL = -4.375.** Everything else is either mimicked by inflation or unmeasurable.

## 2. Realistic SPHEREx Significance Range

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Optimistic | 0.5 | 8.75σ |
| **Central** | **1.0** | **4.4σ** |
| Conservative | 1.5 | 2.9σ |
| Pessimistic | 3.0 | 1.5σ |

SPHEREx provides a meaningful first test at the central estimate (4.4σ). Not definitive, but enough to reorient the field.

## 3. Realistic MegaMapper Significance Range

| Scenario | σ(f_NL) | Significance |
|----------|---------|-------------|
| Optimistic | 0.3 | 14.6σ |
| **Central** | **0.5** | **8.75σ** |
| Conservative | 1.0 | 4.4σ |
| Pessimistic (single-tracer) | 2.5 | 1.75σ |

MegaMapper is definitive at the central estimate (8.75σ). Even the conservative scenario (4.4σ) provides strong evidence.

## 4. How Robust Is the Local-Template Mapping?

**For galaxy surveys: ESSENTIALLY PERFECT.**

Scale-dependent bias is a squeezed-limit measurement. The matter-bounce bispectrum converges to -35/8 in the squeezed limit (verified numerically). No template projection loss.

Previous estimates of cos(θ) ≈ 0.95 were based on a CMB-style inner product. For LSS surveys:
- cos(θ) ≈ 1.0 (squeezed limit match is exact)
- f_NL^eff = -4.375 (full amplitude, no suppression)
- The MegaMapper significance INCREASES slightly: 8.3σ → 8.75σ

For CMB surveys: a proper overlap computation would require bispectrum transfer functions and noise spectra. This is deferred as CMB is not the primary test.

## 5. Do We Need New MCMC or Heavy Simulations?

**NO.** All current analysis is analytical or light-CPU.

- No new Cobaya MCMC needed (f_NL is parameter-free)
- No GPU jobs needed
- No N-body simulations needed
- RunPod justified only later, for mock-based forecast paper validation
- Everything fits on a laptop

## 6. What Exact Next Calculation Should Follow?

**The observational framework is now COMPLETE for scientific decision-making.**

The remaining work is choosing WHICH deliverable to produce:

### Option A: Fisher Forecast Paper
Write a focused forecast paper: "f_NL = -35/8 as a test of bouncing cosmology with SPHEREx and MegaMapper." This would:
- Present the prediction (referencing Cai 2009)
- Document the ECH perturbation-transparency result (our contribution)
- Provide Fisher forecasts for SPHEREx and MegaMapper
- Define the decision thresholds
- Compute is local (laptop), could be done in 1-2 focused sessions

### Option B: Systematic Audit Paper
Write a comprehensive audit: "Observational viability and structural limits of bouncing cosmology." This would:
- Document the 13 structural barriers (ECH/torsion closures)
- Present the perturbation-transparency theorem
- Present the generic f_NL = -35/8 discriminator
- Include the full discrimination framework
- Larger scope, more work, but more publishable impact

### Option C: Continue Scientific Research
Investigate the r ~ O(1) tension resolution more rigorously:
- How exactly does LQC suppress tensors?
- Is the Wilson-Ewing mechanism unique or generic?
- What happens with different quantization prescriptions?

**RECOMMENDATION: Option A.** It's focused, deliverable, and directly actionable. The computation is light (laptop-only). And SPHEREx data arrives ~2028, making the forecast timely and relevant.
