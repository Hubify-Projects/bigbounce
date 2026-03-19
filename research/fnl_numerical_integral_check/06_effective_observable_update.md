# 06: Effective Observable Update

---

## Status of f_NL^eff

From the execution phase:
- Convention equivalence: f_NL(Planck) = |B|_NL(Cai) in squeezed limit — PROVEN
- Template projection: cos(θ) ≈ 0.95 ± 0.03 — ESTABLISHED
- f_NL^eff = f_NL × cos(θ)

### If Cai is correct (f_NL = -35/8):
- f_NL^eff = -4.375 × 0.95 = **-4.16**
- MegaMapper σ(f_NL) = 0.5: detection at **8.3σ**
- Worst case (cos θ = 0.75): f_NL^eff = -3.28, detection at **6.6σ**

### If Li-Brandenberger is correct (f_NL = -35/16):
- f_NL^eff = -2.1875 × 0.95 = **-2.08**
- MegaMapper: detection at **4.2σ**

### Our numerical check:
- Cannot distinguish between -35/8 and -35/16 due to the multi-vertex cancellation issue.
- The single-vertex result (+1.56) is NOT the physical f_NL — it's a partial contribution.

---

## What Changes from This Analysis

**NOTHING changes in the effective observable.** The numerical check attempted to independently verify -35/8 but hit a structural limitation (growing-mode divergences requiring analytical cancellation). The previously established results — convention equivalence, template projection, MegaMapper forecast — all stand.

The STATUS of f_NL = -35/8 is:
- CLAIMED by Cai et al. (2009) via analytical calculation
- SUPPORTED by consistent internal structure (the numerator 35 appears in both Cai and L-B)
- NOT YET INDEPENDENTLY VERIFIED by us (attempted, hit structural obstacle)
- NOT CONTRADICTED by our computation (our partial result is consistent with the full answer requiring multi-vertex cancellation)

---

## Forecast Table (unchanged from execution phase)

| Quantity | Value | Source |
|----------|-------|--------|
| f_NL (Cai) | -35/8 = -4.375 | Cai et al. (2009) |
| cos(θ) | 0.95 ± 0.03 | Template projection (file 05) |
| f_NL^eff | -4.16 ± 0.15 | f_NL × cos(θ) |
| σ(f_NL) MegaMapper | 0.5 | MegaMapper forecast |
| Detection significance | 8.3σ | f_NL^eff / σ |
| σ(f_NL) SPHEREx | 1.0 | SPHEREx forecast |
| Detection significance | 4.2σ | f_NL^eff / σ |
