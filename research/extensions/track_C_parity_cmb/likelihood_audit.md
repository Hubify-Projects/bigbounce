# Track C Likelihood Audit

**Date:** 2026-03-13
**Auditor:** Claude (automated audit)
**Program:** Extension Program — Track C (Parity/CMB Birefringence)

---

## 1. Is Any Likelihood Evaluated?

**NO.** No likelihood function is defined, computed, or evaluated anywhere in Track C.

---

## 2. Origin of the "3.9σ" Claim

The 3.9σ significance comes from:

```
β_combined = 0.2415°
σ_combined = 0.0614°
significance = β_combined / σ_combined = 3.93σ
```

This is the signal-to-noise ratio of the inverse-variance weighted average of two published measurements. It is NOT:
- A detection significance from a likelihood ratio test
- A Bayesian evidence ratio
- A p-value from a χ² or similar test statistic
- A result from any analysis performed by Track C

**The 3.9σ is inherited directly from the published measurements.** Track C merely combines them using the standard textbook formula. The significance would be identical if computed by hand on a napkin.

### Breakdown of the weighted average:

| Quantity | Formula | Value |
|----------|---------|-------|
| w₁ (Eskilt) | 1/0.110² | 82.64 |
| w₂ (ACT DR6) | 1/0.074² | 182.55 |
| β_comb | (0.300×82.64 + 0.215×182.55) / (82.64 + 182.55) | 0.2415° |
| σ_comb | 1/√(82.64 + 182.55) | 0.0614° |
| SNR | 0.2415 / 0.0614 | 3.93 |

---

## 3. Data Sources

### Used:

| Measurement | Paper | arXiv | Dataset | Independent? |
|-------------|-------|-------|---------|--------------|
| Eskilt 2022 | β = 0.30° ± 0.11° | 2205.13962 | Planck PR4 | YES |
| Diego-Palazuelos & Komatsu 2025 | β = 0.215° ± 0.074° | 2509.13654 | ACT DR6 | YES |

These two measurements are independent: different telescopes, different data pipelines, different analysis teams.

### Excluded (with reasons):

| Measurement | Why excluded |
|-------------|-------------|
| Minami & Komatsu 2020 (β = 0.35° ± 0.14°) | Superseded by Eskilt 2022 (same Planck data, improved miscalibration correction) |
| SPIDER 2025 (β = 0.50° ± 0.07°) | Calibration degeneracy: instrument polarization angle partially degenerate with cosmic birefringence angle. Including it would overstate significance. |

**Assessment:** The data selection is conservative and defensible. Including Minami & Komatsu would be double-counting. Excluding SPIDER is cautious — its inclusion would increase the combined significance to ~5σ but at the cost of a known systematic uncertainty.

---

## 4. Covariance Structure

No covariance matrix is used. The two measurements are treated as independent Gaussians, which is valid because:
1. They use different telescopes (Planck vs ACT)
2. They use different frequency channels
3. They use different analysis pipelines
4. There is no shared calibration

The inverse-variance weighted average under independence is exact — no approximation is involved.

---

## 5. What Would a Real Likelihood Analysis Require?

A proper likelihood-based analysis of cosmic birefringence would require:
1. **Pixel-level or harmonic-level CMB polarization maps** (not summary statistics)
2. **Full noise covariance matrices** for EE, BB, and EB spectra
3. **Foreground marginalization** (galactic dust, synchrotron)
4. **Instrument systematics model** (polarization angle calibration, beam effects)
5. **MCMC or nested sampling** over β and nuisance parameters

This is what Eskilt 2022 and Diego-Palazuelos & Komatsu 2025 actually did. Track C uses their published results (the summary statistics β ± σ_β) rather than repeating their analysis.

---

## 6. Audit Verdict

**No likelihood is evaluated in Track C.** The "3.9σ" is a simple signal-to-noise ratio from combining two published Gaussian measurements. This is mathematically correct and scientifically standard — but it must be described as "combining published measurements" rather than as "our analysis finds 3.9σ evidence."

The key distinction: Eskilt and Diego-Palazuelos performed the real statistical inference. Track C translates their results into the framework's parameter space.
