# Branch V: Upside Matrix

**Created:** 2026-03-17

---

## Scoring Methodology

Each extension × channel combination is scored on three axes:

- **Signal strength (S)**: 0–3 (0 = undetectable, 1 = marginal, 2 = detectable with next-gen, 3 = detectable now)
- **Distinctiveness (D)**: 0–3 (0 = generic, 1 = constrains bounce class, 2 = constrains ECH specifically, 3 = uniquely ECH)
- **Calculability (C)**: 0–3 (0 = intractable, 1 = order-of-magnitude, 2 = semi-analytic, 3 = fully numerical)

**Upside score = S × D × C** (max = 27). We also note whether existing data already provides hints.

---

## Extension × Channel Matrix

### V1: Time Asymmetry

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 2 | 1 | 3 | **6** | Oscillatory features; period encodes Δt_bounce |
| PBH | 0 | 0 | 3 | 0 | No enhancement mechanism |
| Induced GW | 0 | 0 | 3 | 0 | No scalar enhancement |
| Non-Gaussianity | 1 | 1 | 2 | **2** | Weak f_NL from asymmetric matching |
| Tensor mods | 1 | 1 | 3 | **3** | Slight tilt correction to n_T |
| N_eff / reheating | 1 | 1 | 2 | **2** | Entropy production modifies N_eff slightly |
| Large-scale anomalies | 1 | 1 | 2 | **2** | Too small to explain anomalies alone |
| **Total** | | | | **15** | |

### V2a: Dust Contraction + ECH Bounce

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 3 | 2 | 3 | **18** | n_s ≈ 1 from contraction; low-ℓ cutoff from finite duration |
| PBH | 1 | 1 | 2 | **2** | Possible at small scales with modified growth |
| Induced GW | 1 | 1 | 2 | **2** | Weak secondary signal |
| Non-Gaussianity | 3 | 3 | 3 | **27** | f_NL^local = 5/12 — UNIQUE, parameter-free prediction |
| Tensor mods | 2 | 2 | 3 | **12** | n_T = 0 with small r; consistency relation r = -8n_T violated |
| N_eff / reheating | 1 | 1 | 2 | **2** | Standard unless spectator sector modified |
| Large-scale anomalies | 2 | 2 | 2 | **8** | Finite contraction → low-ℓ cutoff matches Planck anomaly |
| **Total** | | | | **71** | **HIGHEST TOTAL** |

### V2b: Ekpyrotic Contraction + ECH Bounce

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 2 | 2 | 2 | **8** | Scale-invariant via entropy mechanism; depends on ε |
| PBH | 1 | 1 | 2 | **2** | Blue scalar tilt → no enhancement at small scales |
| Induced GW | 0 | 0 | 2 | 0 | No scalar enhancement |
| Non-Gaussianity | 2 | 2 | 2 | **8** | f_NL^equil ~ -c²/8 ~ -10; distinctive but model-dependent |
| Tensor mods | 1 | 2 | 2 | **4** | r ≈ 0 (decisive against inflation if confirmed) |
| N_eff / reheating | 1 | 1 | 2 | **2** | Standard |
| Large-scale anomalies | 1 | 1 | 1 | **1** | Ekpyrotic doesn't naturally explain anomalies |
| **Total** | | | | **25** | |

### V2c: Kinetic Contraction + ECH Bounce

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 1 | 1 | 3 | **3** | Blue scalar spectrum (n_s = 3); needs modification |
| PBH | 0 | 0 | 3 | 0 | Blue spectrum suppresses small scales |
| Induced GW | 2 | 2 | 3 | **12** | Blue tensor spectrum → enhanced at high-f; LISA/DECIGO |
| Non-Gaussianity | 1 | 1 | 2 | **2** | f_NL equilateral ~ O(1) |
| Tensor mods | 3 | 3 | 3 | **27** | n_T = 2 is UNIQUE smoking gun; detectable if r > 10⁻³ |
| N_eff / reheating | 1 | 1 | 2 | **2** | Standard |
| Large-scale anomalies | 0 | 0 | 2 | 0 | Blue tilt doesn't help |
| **Total** | | | | **46** | |

### V3: Spectator Field

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 2 | 1 | 2 | **4** | Enhanced P(k) at resonance scale |
| PBH | 2 | 1 | 2 | **4** | Possible formation at resonance scale |
| Induced GW | 2 | 1 | 2 | **4** | Peaked signal from enhanced scalars |
| Non-Gaussianity | 2 | 1 | 2 | **4** | Curvaton-type f_NL |
| Tensor mods | 1 | 1 | 2 | **2** | Indirect through energy budget |
| N_eff / reheating | 1 | 1 | 1 | **1** | Spectator decay products |
| Large-scale anomalies | 0 | 0 | 1 | 0 | Wrong scale |
| **Total** | | | | **19** | |

### V4: Ekpyrotic + ECH Bounce

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 2 | 2 | 2 | **8** | Same as V2b but with clean bounce matching |
| PBH | 0 | 0 | 2 | 0 | Same as V2b |
| Induced GW | 0 | 0 | 2 | 0 | Same as V2b |
| Non-Gaussianity | 2 | 2 | 2 | **8** | Same as V2b |
| Tensor mods | 2 | 3 | 2 | **12** | r ≈ 0 + ECH bounce = unique combination |
| N_eff / reheating | 1 | 1 | 2 | **2** | Standard |
| Large-scale anomalies | 1 | 1 | 1 | **1** | Same as V2b |
| **Total** | | | | **31** | |

### V5: Loitering Phase

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 2 | 1 | 2 | **4** | Near-scale-invariant from loiter |
| PBH | 1 | 1 | 1 | **1** | Possible if loiter amplifies specific scales |
| Induced GW | 1 | 1 | 1 | **1** | Possible secondary signal |
| Non-Gaussianity | 1 | 1 | 1 | **1** | Depends on details |
| Tensor mods | 2 | 1 | 2 | **4** | Loiter amplifies tensors; possibly detectable |
| N_eff / reheating | 1 | 1 | 1 | **1** | Standard |
| Large-scale anomalies | 1 | 1 | 1 | **1** | Same as V1 |
| **Total** | | | | **13** | |

### V6: Sound Speed Deformation

| Channel | S | D | C | Score | Notes |
|---------|---|---|---|-------|-------|
| Scalar features | 1 | 1 | 2 | **2** | Modified features near bounce scale |
| PBH | 1 | 1 | 1 | **1** | If c_s < 1 brings features to accessible scales |
| Induced GW | 1 | 1 | 1 | **1** | Secondary |
| Non-Gaussianity | 2 | 1 | 2 | **4** | f_NL ~ 1/c_s² enhanced for small c_s |
| Tensor mods | 1 | 1 | 2 | **2** | Modified c_T possible |
| N_eff / reheating | 0 | 0 | 1 | 0 | No effect |
| Large-scale anomalies | 0 | 0 | 1 | 0 | Wrong scale |
| **Total** | | | | **10** | |

---

## Final Rankings

| Rank | Extension | Total Score | Best Channel (Score) | Existing Data Hint? |
|------|-----------|-------------|---------------------|---------------------|
| **1** | **V2a (Dust + ECH)** | **71** | Non-Gaussianity (27) | Yes: Planck low-ℓ deficit |
| **2** | **V2c (Kinetic + ECH)** | **46** | Tensor tilt (27) | No: needs LiteBIRD/CMB-S4 |
| **3** | **V4 (Ekpyrotic + ECH)** | **31** | Tensor + f_NL (12+8) | No: needs CMB-S4/SPHEREx |
| **4** | **V2b (Ekpyrotic contraction)** | **25** | f_NL + scalar (8+8) | No: needs next-gen |
| **5** | **V3 (Spectator)** | **19** | Multiple weak (4 each) | Possible: PTA excess |
| **6** | **V1 (Time asymmetry)** | **15** | Scalar features (6) | Marginal |
| **7** | **V5 (Loitering)** | **13** | Tensor + scalar (4+4) | No |
| **8** | **V6 (Sound speed)** | **10** | f_NL (4) | No |

---

## Key Takeaway

**V2a (dust contraction + ECH bounce) dominates the matrix** because it produces:
1. A parameter-free non-Gaussianity prediction (f_NL = 5/12) that is the HIGHEST-scoring individual cell
2. A near-scale-invariant spectrum that matches Planck observations
3. A natural explanation for the low-ℓ deficit (finite contraction duration)
4. Clean tensor predictions testable by LiteBIRD

The runner-up V2c (kinetic contraction) has a single spectacular prediction (n_T = 2) but fails on the scalar side without modification.

**Recommendation: V2a is the best single target.** V4 (ekpyrotic + ECH) is the best secondary target because ECH solves ekpyrotic's biggest weakness.
