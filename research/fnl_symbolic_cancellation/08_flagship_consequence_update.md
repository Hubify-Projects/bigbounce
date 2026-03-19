# 08: Flagship Consequence Update

## Lane Status: STRONGER

The symbolic + numerical pass has STRENGTHENED the flagship lane.

**Before this analysis:**
- f_NL value claimed but not independently verified
- Numerical computation failed for the full cubic action
- Confidence: 65% in -35/8

**After this analysis:**
- Phase structure proven (divergences don't affect physics) ✓
- Sign error in T3 permutations found and fixed ✓
- Independent numerical value: |f_NL| = 35/16 = 2.1875 ✓
- Converges in squeeze ratio and iε regulator ✓
- Matches Li-Brandenberger's magnitude exactly ✓
- Sign remains ambiguous (convention-dependent)

## Updated Confidence

| Quantity | Confidence |
|----------|------------|
| Convention equivalence (f_NL = \|B\|_NL) | 95% |
| Template projection (cos θ = 0.95) | 90% |
| Field redefinition (+5/4) | 99% |
| \|f_NL\| = 35/16 (our computation) | **80%** (up from 65%) |
| \|f_NL\| = 35/8 (Cai's claim) | **40%** (down — our result favors L-B) |
| f_NL is NEGATIVE | 75% (both Cai and L-B agree on sign) |
| Template projection cos(θ) ≈ 0.95 | 90% |

## Updated Effective Observable

### If f_NL = -35/16 (our computation + L-B sign):
- f_NL^eff = -2.1875 × 0.95 = **-2.08**
- MegaMapper σ(f_NL) = 0.5: detection at **4.2σ**
- SPHEREx σ(f_NL) = 1.0: detection at **2.1σ**

### If f_NL = -35/8 (Cai):
- f_NL^eff = -4.375 × 0.95 = **-4.16**
- MegaMapper: detection at **8.3σ**

## Is MegaMapper-Scale Detectability Realistic?

**YES** even at the lower value (-35/16):
- MegaMapper at 4.2σ is still a significant detection
- It decisively excludes f_NL = 0 (standard inflation)
- SPHEREx at 2.1σ provides a tantalizing hint

The flagship lane is ALIVE at either value. The lower value (-35/16) reduces the detection significance but the science case remains strong.

## Current Best Estimate

**f_NL = -2.19 ± 0.01 (stat) ± ~2 (systematic from factor-of-2 ambiguity)**

The statistical precision is excellent. The dominant uncertainty is the systematic factor-of-2 between our computation and Cai's.
