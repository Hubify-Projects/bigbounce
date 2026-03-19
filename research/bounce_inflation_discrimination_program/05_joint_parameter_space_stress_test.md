# 05: Joint Parameter-Space Stress Test

## How Fragile Is the Live Model?

### Test 1: Vary the quasi-dust parameter ε

The canonical value ε = 0.003 gives n_s = 0.964. How sensitive is f_NL to ε?

**f_NL is INDEPENDENT of ε.** The bispectrum coefficient -35/8 comes from the cubic action at ε = 3/2 (the BACKGROUND ε, which is the slow-roll parameter of the contraction). The small correction ε_correction = 0.003 shifts the background ε from exactly 3/2 to 3/2 - 0.003 = 1.497.

Effect on f_NL: the cubic action coefficient (ε²-ε³/2) at ε = 1.497 vs 1.500:
- At ε = 1.500: 2.250 - 1.6875 = 0.5625
- At ε = 1.497: 2.241 - 1.678 = 0.563

Fractional change: 0.1%. **f_NL is stable to quasi-dust corrections.**

### Test 2: Vary LQC tensor suppression

The LQC r-suppression depends on the Immirzi parameter γ (fixed at 0.274 in standard LQC) and the bounce density ρ_crit. These are NOT freely adjustable — they're determined by the LQC quantization.

However, different quantization prescriptions (e.g., the "A-quantization" vs "K-quantization") can shift ρ_crit by factors of O(1). This would shift r by O(1) factors around 10⁻⁴.

**Impact on the discriminator:** NONE. r is secondary — the flagship is f_NL, which doesn't depend on the tensor suppression mechanism.

### Test 3: What if the bounce is not LQC?

If the bounce is ECH instead of LQC:
- f_NL: unchanged (-35/8, mechanism-independent)
- n_s: unchanged (from quasi-dust contraction, before bounce)
- r: CHANGES — ECH doesn't automatically suppress r. Without LQC corrections, r ~ O(1), which is excluded.

**This is the key fragility:** r requires LQC (or an equivalent mechanism) to be viable. Without tensor suppression, the model is excluded by current data. But f_NL is unaffected.

### Test 4: What if Bunch-Davies vacuum is wrong?

If the initial state differs from BD (e.g., from pre-contraction dynamics or quantum gravity effects):
- The mode functions change
- The power spectrum normalization changes
- f_NL COULD change (the growing-mode coefficient depends on the mode function phase)

**Assessment:** BD vacuum is the standard, well-motivated choice for modes deep inside the Hubble radius during contraction. Departures would need to be large to affect f_NL significantly. But this IS a theoretical uncertainty.

### Test 5: What if the contraction is not purely matter-dominated?

If w deviates significantly from 0 (e.g., radiation epoch before matter):
- f_NL changes because the cubic action coefficient depends on ε
- For radiation (w = 1/3, ε = 2): f_NL would be different (larger)
- For stiff matter (w = 1, ε = 3): f_NL would be much larger

**Assessment:** The prediction f_NL = -35/8 requires matter domination. If a pre-matter radiation epoch exists, it would modify the bispectrum for modes that exit the Hubble radius during radiation. But CMB-scale modes typically exit during matter domination in the standard scenario.

## Stability Summary

| Deformation | f_NL impact | n_s impact | r impact |
|------------|-------------|------------|----------|
| ε variation (±0.001) | <0.1% | ±0.012 | None |
| LQC quantization variant | None | None | O(1) factor |
| Non-LQC bounce | None | None | **Excluded** (r~O(1)) |
| Non-BD vacuum | Potentially large | Potentially large | Potentially large |
| Non-matter epoch | Potentially large | Potentially large | Potentially large |

## Verdict: MODERATELY_PREDICTIVE

The model is:
- **Highly stable** in f_NL with respect to quasi-dust parameter, LQC details, and bounce mechanism
- **Fragile** in r with respect to the bounce mechanism (requires LQC or equivalent)
- **Conditionally stable** in all observables with respect to vacuum choice and background composition (standard assumptions are well-motivated but not proven)

The flagship discriminator (f_NL) is ROBUST. The supporting observables (r, n_s) are MODEL-DEPENDENT.
