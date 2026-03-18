# 00: Master Status Integration

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Current Positive Lane

After: 13-barrier ECH closure, bounce evidence audit (16 claims), first-pass viable model analysis, second-pass distinctiveness filter, and three deep-dive literature/derivation investigations, **one positive research lane survives:**

**Wilson-Ewing LCDM Quasi-Dust Matter Bounce in LQC**

| Component | Status |
|-----------|--------|
| Background: H^2 = (rho/3M^2)(1 - rho/rho_c) | Well-established in LQC |
| EOS: w = -epsilon = -0.003 | Provides red tilt n_s = 1 - 12*epsilon = 0.964 |
| n_s = 0.964 | Matches Planck (fitted, not predicted) |
| r ~ 10^-4 | LQC dressed-metric suppression (untestable) |
| f_NL^local = -35/8 = -4.375 | **THE flagship discriminator** |
| BKL stability | Requires ekpyrotic pre-phase (w >> 1) |
| Extra fields | 0 (dust + Lambda from LCDM) |
| Extra parameters | 1 (epsilon) |

---

## Recent Corrections (All Critical)

### 1. f_NL Convention (RESOLVED)
- f_NL = -35/8 = -4.375 IS the Planck-convention value (Cai et al. 2009, arXiv:0903.0631)
- The earlier 5/12 value in branch_V files was WRONG (faulty delta-N + spurious conversion)
- Convention verified: zeta = zeta_G + (3/5) f_NL zeta_G^2 gives same numerical f_NL as Phi = Phi_G + f_NL Phi_G^2

### 2. EOS Sign (RESOLVED)
- Red tilt requires w = -epsilon < 0 (NEGATIVE), not positive
- n_s = 1 - 12*epsilon for P = -epsilon*rho
- Lambda provides the mechanism for w < 0 (LCDM bounce, Cai & Wilson-Ewing 2015)

### 3. Curvaton Tilt Sign (RESOLVED — NEGATIVE RESULT)
- Curvaton tilt is BLUE in matter contraction (n_sigma = 1 + 2m^2/(3H^2) > 1)
- This KILLS Model A (LQC + Curvaton)
- The red tilt must come from w < 0, not from a spectator field

### 4. f_NL Foundation Cracks (NEW — CRITICAL)
Three discrepancies discovered in the f_NL = -35/8 foundation:

| Issue | Detail | Severity |
|-------|--------|----------|
| Li & Brandenberger 2016 formula | Their f_NL ~ -165/16 + 65/(8c_s^2) gives -2.2 at c_s=1, not -4.375 | HIGH |
| Quintin et al. citation | They quote -35/16 (not -35/8) — factor-of-2 discrepancy | MEDIUM |
| Shape is "loosely local" | Cai et al. themselves say the mapping to f_NL^local is approximate | MEDIUM |

**These discrepancies must be resolved before building anything on f_NL = -35/8.**

---

## Dead Branches (Confirmed Dead, Do Not Revisit)

| Branch/Model | Death Certificate |
|-------------|------------------|
| Model A: LQC + Curvaton | Curvaton tilt is blue |
| Model C: ILS Ekpyrotic | Bounce does no predictive work |
| ECH perturbation signatures | ECH is perturbation-transparent (Branch Vb) |
| Chiral GW | Frequency gate: f_0 ~ 10^9-10^10 Hz |
| ALP curvaton tilt | 75-order mass incompatibility |
| Galaxy chirality | Krolewski 2024 debunked the 7-sigma signal |
| CMB anomalies | Durrer 2023 challenged; qualitative only |
| Geometric DE from bounce | 13 barriers; A-G program closed |
| DBI evasion of Quintin no-go | r proportional to c_s^2 with O(10) prefactor; need c_s < 0.04, gives |f_NL^equil| ~ 625 |

---

## What Remains Uncertain

### HIGHEST PRIORITY
1. **Is f_NL = -35/8 robust?** Three literature discrepancies (Li-Brandenberger, Quintin citation, shape approximation). No independent reproduction exists.
2. **Does f_NL survive the bounce?** Cai et al. compute f_NL in the contracting phase only. The Quintin no-go: suppressing r at the bounce enhances f_NL to exclusion. The LQC dressed-metric approach may evade this but has not been computed at third order.

### HIGH PRIORITY
3. **What is the LQC bounce transfer matrix at third order?** The dressed-metric approach gives scalar amplification (suppressing r). Does this amplification also enhance f_NL? If so, by how much?
4. **Is the -35/8 value or the Li-Brandenberger -2.2 value correct?** A factor-of-2 error in either direction changes the MegaMapper detection significance from ~8.75 sigma to ~4.4 sigma (still interesting) or makes the discrepancy worse.

### MEDIUM PRIORITY
5. How exactly does the ekpyrotic pre-phase (for BKL) connect to the matter phase?
6. What is the exact r in the LQC dressed-metric approach for w = -0.003?
7. Does the LQC bounce produce any additional bispectral features on observable scales?

---

## What the Program Stands or Falls On

**Single point of failure: f_NL = -35/8 being a correct, robust, parameter-free, Planck-convention prediction that survives through the LQC bounce.**

If this holds: the matter bounce has a genuine hard-to-mimic discriminator testable by MegaMapper.
If this falls: the model has zero testable discriminators and becomes observationally superfluous.

The newly discovered foundation cracks (Li-Brandenberger discrepancy, Quintin factor-of-2, shape approximation) make resolving this the IMMEDIATE priority before any further downstream analysis.
