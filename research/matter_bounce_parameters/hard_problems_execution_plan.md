# Hard Problems Execution Plan

**Date:** 2026-03-24
**Status:** Two genuinely hard computational problems remain.

---

## Problem 1: Full In-In Integral from Scratch

### What it is

The in-in bispectrum integral for the matter bounce involves 4 cubic action vertices, each producing time integrals of products of three mode functions. Individual vertex integrals DIVERGE (~10⁹). The physical f_NL (~4) emerges from near-perfect cancellation between all vertices.

Our attempt (Tier 1A) captured only the field redefinition (+1.25) plus a tiny time-integral correction (-0.05). The dominant growing-mode contributions from vertices 2-4 were missed because the Wick contraction assignments in the squeezed limit are more complex than a naive product of mode functions.

### Why it's hard

1. **Divergence/cancellation:** Each vertex gives O(10⁹), but they cancel to O(1). Numerical precision must resolve 9 orders of magnitude of cancellation.

2. **Momentum assignments:** In the squeezed limit (k₁ ≪ k₂ = k₃ = k), each vertex term produces MULTIPLE Wick contractions depending on which external momentum is assigned to which field in the vertex. The number of assignments is:
   - ζζ̇²: 3 assignments (which ζ is undifferentiated)
   - ζ(∂ζ)²: 3 assignments × momentum dot products
   - ζ̇(∂ζ)(∂χ): 6 assignments (χ involves inverse Laplacian)
   - ζ(∂ᵢ∂ⱼχ)²: 3 assignments × angular contractions

3. **χ definition:** χ ≡ ∂⁻²ζ̇ (inverse Laplacian of ζ̇). In k-space: χ_k = -ζ̇_k/k². The ∂ᵢ∂ⱼ tensor structure introduces angular factors (kᵢkⱼ/k²) that depend on the triangle geometry.

4. **Phase convention:** Cai uses e^{+ikη} (confirmed from paper). The original failed attempt used e^{-ikη}.

### The correct approach

The most reliable path is to follow Cai's computation EXACTLY, using:

**Step 1:** Implement the FULL cubic action from Cai Eq. (15) in k-space, with ALL momentum assignments written out explicitly for each vertex.

**Step 2:** For each vertex, enumerate ALL Wick contractions in the squeezed limit:
- Identify which external momentum (k₁, k₂, k₃) is assigned to which field
- Compute the momentum dot products (k₂·k₃ = -(k₁² - k₂² - k₃²)/2, etc.)
- Include the χ angular structure where applicable

**Step 3:** Sum ALL contracted terms into a COMBINED integrand at each time step.

**Step 4:** Integrate the combined integrand from τ₀ to τ_f.

**Step 5:** Verify at ε = 3/2 by comparing the final A_T polynomial against the known benchmarks.

### What we already have

- ODE-solved mode functions ζ_k(τ), ζ̇_k(τ) at arbitrary ε (WORKING)
- Interpolation for numerical integration (WORKING)
- Cai's exact mode function expressions Eqs. (23-24) (KNOWN)
- The correct polynomial A_T = (3/256Πk²) × P(k) with unique coefficients (KNOWN)

### What we need to build

A complete k-space Wick contraction module that:
1. Takes the cubic action vertices
2. Enumerates all momentum assignments
3. Computes the integrand at each τ
4. Sums before integrating

### Compute requirements

- **Where:** RunPod CPU pod (current pod is fine)
- **Runtime:** ~1-4 hours per ε value with mpmath high precision
- **Total for ε scan:** ~1-2 days for 10 ε values
- **Precision:** Need 30+ digit precision to resolve cancellations
- **Risk:** If the cancellation is too delicate for double precision but tractable with mpmath

### Success criteria

- Reproduces A_T(squeezed) = -(21/8)k³ at ε = 3/2
- Reproduces A_T(equilateral) = -(255/64)(3/256) bracket at ε = 3/2
- Gives a smooth f_NL(ε) curve across [1.48, 1.52]
- Allows extraction of the exact ε correction coefficient

### Fallback if it fails

The bounded range [1-8%] stands. The polynomial approach (verified coefficients, injection-validated r) is already strong enough for the paper. The in-in integral would add "independently derived" but is not strictly necessary.

---

## Problem 2: NaMaster at Full Resolution

### What it is

Our NaMaster EB analysis at NSIDE=256 gives β = 0.14 ± 0.11° — too noisy to be informative. At NSIDE=2048 (the native Planck resolution), NaMaster would give much tighter constraints but requires:
- More memory (~8 GB per map at NSIDE=2048)
- Much longer coupling matrix computation (hours, not seconds)
- Careful apodization at high resolution
- Validation against known Planck results

### Why it matters

The published Planck birefringence measurement (Minami & Komatsu 2020) uses a specialized D-estimator that marginalizes over the instrumental miscalibration angle. Our simple EB/EE ratio estimator does NOT do this. Getting a credible β measurement requires either:

**Option A:** Implement the Minami-Komatsu D-estimator (hard but definitive)
**Option B:** Run NaMaster at NSIDE=2048 and accept the miscalibration systematic (easier but less definitive)
**Option C:** Use frequency-split estimator to separate cosmological from instrumental rotation (medium difficulty)

### The correct approach

**Priority: Option B (NaMaster at NSIDE=2048)** because:
- It's straightforward (just increase resolution)
- It gives a real map-level result
- The miscalibration systematic is well-documented and can be quoted as a caveat

**Then Option C (frequency-split)** as a robustness test.

### Compute requirements

- **Where:** RunPod CPU pod (need 64+ GB RAM, which we have)
- **Runtime:** ~2-4 hours for coupling matrix + spectrum estimation at NSIDE=2048
- **Disk:** ~5 GB for maps (already downloaded)
- **Risk:** NaMaster at NSIDE=2048 with lmax=4000 may be very slow. Fallback: NSIDE=1024 (lmax=2000).

### Success criteria

- β uncertainty < 0.05° (competitive with published Planck analysis)
- Null test passes (χ²/dof ≈ 1)
- Result is within 2σ of published values
- Frequency consistency test shows no strong frequency dependence

### What we also need for F3.5 (frequency robustness)

Download Planck HFI frequency maps (100, 143, 217 GHz) — about 2 GB each. Run NaMaster EB on each frequency separately. Compare β across frequencies. A cosmological signal should be frequency-independent.

---

## Execution Plan for Next Session

```
START OF SESSION:
│
├── Pod check: verify kqo1b4e4igycra is running with all data
│
├── PARALLEL TRACK A: Problem 1 (in-in integral)
│   ├── 1. Write complete Wick contraction module
│   │   - All 4 vertices with all momentum assignments
│   │   - Combined integrand function
│   │   - Validation at equilateral (all terms contribute)
│   │
│   ├── 2. Verify at ε = 3/2
│   │   - Must reproduce known polynomial benchmarks
│   │   - If fails: debug momentum assignments
│   │   - If passes: proceed to ε scan
│   │
│   └── 3. ε scan [1.48, 1.52]
│       - 10 values with mpmath precision
│       - Extract exact df_NL/dε
│       - Produce consistency relation coefficient
│
├── PARALLEL TRACK B: Problem 2 (high-res EB)
│   ├── 1. Download frequency maps to pod
│   │   - 100, 143, 217 GHz HFI maps (~6 GB total)
│   │
│   ├── 2. NaMaster at NSIDE=1024 (intermediate step)
│   │   - Test if coupling matrix is tractable at this resolution
│   │   - Expected: ~30 min for coupling matrix
│   │
│   ├── 3. NaMaster at NSIDE=2048 (if 1024 succeeds)
│   │   - May need several hours
│   │   - Run in background
│   │
│   └── 4. Frequency consistency test
│       - EB on each frequency map separately
│       - Compare β across 100/143/217 GHz
│
└── END OF SESSION:
    ├── Backup all results from pod
    ├── Update paper + site with new findings
    └── Final claim hygiene pass if both problems resolved
```

### Time estimates

| Task | Estimated time | Blocking? |
|------|---------------|-----------|
| Wick contraction module | 2-3 hours coding | Yes — blocks ε scan |
| Verification at ε = 3/2 | 30 min compute | Yes — blocks scan |
| ε scan (10 values) | 4-8 hours compute (can run overnight) | No — run in background |
| Frequency map download | 1 hour | No — run in background |
| NaMaster at NSIDE=1024 | 30-60 min compute | No — run in background |
| NaMaster at NSIDE=2048 | 2-4 hours compute | No — run overnight |
| Frequency consistency | 1-2 hours | Needs frequency maps |

### What would change if both problems are solved

| Claim | Current | After Problem 1 | After Problem 2 |
|-------|---------|-----------------|-----------------|
| f_NL normalization | 92% confidence | **98%+** (independently derived) | Unchanged |
| ε correction | Bounded [1-8%] | **Exact coefficient** | Unchanged |
| Template overlap r | Injection-validated 0.88-0.90 | Unchanged | Unchanged |
| Birefringence β | 0.14 ± 0.11° (NSIDE=256) | Unchanged | **0.XX ± 0.0X°** (NSIDE=2048) |
| Frequency consistency | Not tested | Unchanged | **Tested** |

### What if Problem 1 fails again

If the full Wick contraction still doesn't reproduce the benchmarks:
- The polynomial approach (unique verified coefficients) remains the primary evidence
- The bounded ε correction [1-8%] stands
- The paper says "validated by polynomial verification and injection recovery" not "independently derived from cubic action"
- This is still a strong paper — just not the strongest possible version

### What if Problem 2 gives unexpected β

If NaMaster at high resolution gives β significantly different from published values:
- Check for mask/apodization issues first
- Compare against pseudo-Cℓ at the same resolution
- If discrepancy persists, it's a genuine finding about E/B leakage or systematics
- Report honestly regardless of direction
