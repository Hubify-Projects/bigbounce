# Phase 4: Numerical Evolution Pipeline Design

**Date:** 2026-03-13
**Status:** PIPELINE SPECIFICATION — algorithm and solver choices defined, not implemented

---

## 1. ODE System

### 1a. Background System (5 coupled ODEs in conformal time)

```
da/dτ = a² H                                                   [1]
dH/dτ = a × [−(κ/2)(ρ_eff + P_eff)(1 − 2ρ_eff/ρ_c)]         [2]
dφ/dτ = a × π_φ                                                [3]
dπ_φ/dτ = a × [−3H π_φ − V'(φ)]                               [4]
dn/dτ = −3 a H n                                               [5]
```

where:
- κ = 8πG
- π_φ = dφ/dt (physical time momentum)
- ρ_eff = (1/2)π_φ² + V(φ) + V_s(n)
- P_eff = (1/2)π_φ² − V(φ) + n dV_s/dn − V_s(n)
- V_s(n): spin condensate closure (phenomenological)
- V(φ): inflaton potential (e.g., Starobinsky R²)

**State vector:** y = (a, H, φ, π_φ, n)
**Dimension:** 5

### 1b. Perturbation System (2 ODEs per mode, per polarization)

**Scalar (for each k):**
```
dv_k/dτ = v_k'                                                 [6]
dv_k'/dτ = −[c_s²(τ) k² − U_s(τ)] v_k                        [7]
```

where U_s(τ) = z''/z is computed from the background solution.

**Tensor (for each k, each λ = ±1):**
```
du_{λ,k}/dτ = u_{λ,k}'                                        [8]
du_{λ,k}'/dτ = −[k² − a''/a + λ μ_PV k Φ'(τ)] u_{λ,k}       [9]
```

**Total per k:** 2 (scalar) + 4 (tensor L+R) = 6 real ODEs
(v_k is complex → 4 real for scalar; but we can track Re and Im together as 2 complex)

---

## 2. Integration Range

### 2a. Conformal Time Domain

```
τ_start ← deep in contraction (when all modes of interest are sub-Hubble)
τ_bounce ← H = 0 (bounce point)
τ_end ← well into slow-roll inflation (when all modes of interest are frozen)
```

**Estimating τ_start:**

For the highest k of interest (k_max ~ 10¹⁶ Mpc⁻¹):
```
Need k² ≫ |U_s(τ_start)|
Since U_s ~ (aH)² near the bounce, and aH ~ a_bounce × H_max at maximum:
τ_start must be chosen so that k_max/aH(τ_start) ≫ 1
```

In practice: set τ_start at ~10-50 e-folds before the bounce in the contraction.

**Estimating τ_end:**

For the lowest k of interest (k_min ~ 10⁻⁴ Mpc⁻¹ for CMB):
```
Need k_min ≪ aH(τ_end) (mode is frozen, super-Hubble)
This requires τ_end ~ 60 e-folds after bounce into inflation
```

**Total range:** ~100+ e-folds of evolution in conformal time.

### 2b. k-Grid

```
k_min = 10⁻⁴ Mpc⁻¹     (CMB quadrupole)
k_max = 10¹⁶ Mpc⁻¹      (sub-bounce-scale; well beyond feature)
```

Logarithmic spacing:
```
N_k = 10⁴ points
Δ(ln k) = ln(k_max/k_min) / N_k = ln(10²⁰) / 10⁴ ≈ 4.6 × 10⁻³
```

**Note:** The bounce feature is at k ~ 10¹⁴-10¹⁵ Mpc⁻¹. We need dense sampling around this scale. Use adaptive k-grid:
- Coarse: 100 points from 10⁻⁴ to 10¹² Mpc⁻¹ (CMB + LSS, scale-invariant)
- Dense: 5000 points from 10¹² to 10¹⁶ Mpc⁻¹ (bounce feature region)
- Coarse: 100 points from 10¹⁶ to 10¹⁸ Mpc⁻¹ (UV tail)

Total: ~5200 k-modes.

---

## 3. Stiffness and Numerical Stability

### 3a. Stiffness Analysis

The mode equation:
```
v_k'' + ω_k²(τ) v_k = 0,    ω_k² = c_s² k² − U_s(τ)
```

is oscillatory (not stiff) when ω_k² > 0 (sub-Hubble modes). The "stiffness" arises from:

1. **Wide dynamic range:** ω_k varies from ~10¹⁶ (high-k, deep sub-Hubble) to ~0 (super-Hubble freeze-out). The oscillation frequency spans 20 orders of magnitude.

2. **Bounce crossing:** At the bounce, U_s(τ) has a sharp spike. The effective frequency ω_k changes rapidly, requiring small time steps.

3. **Super-Hubble regime:** For k² < U_s, the equation becomes:
```
v_k'' − |ω_k²| v_k = 0    (growing + decaying modes)
```
This is potentially unstable if the growing mode dominates.

### 3b. Recommended Solver

**Primary solver:** DOP853 (explicit Runge-Kutta of order 8, Dormand-Prince)
- Excellent for oscillatory problems
- Adaptive step size control
- Available in scipy.integrate.solve_ivp

**Alternative for stiff regions:** Radau IIA (implicit RK, order 5)
- Use if DOP853 fails near the bounce
- Available in scipy.integrate.solve_ivp

**High-precision alternative:** LSODA (automatic stiff/non-stiff switching)
- Good for long integrations with mixed character
- Available in scipy.integrate.odeint

### 3c. Step Size Requirements

Near the bounce:
```
Δτ < 1/ω_k_max ~ 1/(c_s × k_max × a_bounce)
```

For k_max = 10¹⁶ Mpc⁻¹ and a_bounce ~ 10⁻³⁰ (very small):
```
ω_k ~ k × a_bounce ~ 10¹⁶ × 10⁻³⁰ ~ 10⁻¹⁴ (in natural units)
```

This is actually very slow — the conformal-time frequency is small because a_bounce is tiny.

**The real challenge is the opposite end:** during inflation, a grows exponentially, making aH large and the freeze-out behavior hard to track.

### 3d. Numerical Precision

- Relative tolerance: 10⁻¹⁰ (need ≤0.1% accuracy in P_R(k))
- Absolute tolerance: 10⁻¹⁵ (prevent underflow in decaying modes)
- Double precision (float64) should suffice
- May need quad precision (float128) for k ~ k_bounce modes that undergo maximum amplification

---

## 4. Algorithm

### Step 1: Solve Background Once

```python
# Solve background ODEs from τ_start to τ_end
# Store a(τ), H(τ), φ(τ), n(τ) on a fine grid
# Interpolate using cubic spline for perturbation evolution
τ_grid = adaptive_grid(τ_start, τ_end, N_points=10⁵)
background = solve_ivp(background_rhs, [τ_start, τ_end], y0,
                        method='DOP853', t_eval=τ_grid, rtol=1e-12)
```

### Step 2: Compute z''/z and c_s² on the Grid

```python
# From background solution, compute:
z = a * sqrt(2 * epsilon1) * M_Pl / c_s
z_pp_over_z = numerical_second_derivative(z, τ_grid) / z

# Also compute a''/a for tensor equation
a_pp_over_a = numerical_second_derivative(a, τ_grid) / a
```

**CRITICAL:** Use high-order finite differences or spectral differentiation for z''/z. Standard 3-point finite differences introduce ~1% errors that can corrupt the power spectrum.

Recommended: Chebyshev spectral differentiation on each smooth segment, with separate treatment at the bounce point.

### Step 3: Evolve Perturbations (Parallelizable)

```python
for k in k_grid:  # EMBARRASSINGLY PARALLEL
    # Set initial conditions (vacuum choice)
    v0, vp0 = initial_conditions(k, τ_start, vacuum_type)

    # Evolve through bounce
    sol = solve_ivp(perturbation_rhs, [τ_start, τ_end], [v0, vp0],
                     method='DOP853', rtol=1e-10, atol=1e-15,
                     args=(k, z_pp_over_z_interp, c_s_interp))

    # Extract power spectrum
    v_final = sol.y[0, -1]
    z_final = z_interp(τ_end)
    P_R[k] = k**3 / (2 * pi**2) * abs(v_final / z_final)**2
```

### Step 4: Extract Results

```python
# Build P_R(k) from all modes
# Identify features: bumps, oscillations, suppression
# Compare to scale-invariant reference: P_R_ref = A_s (k/k_*)^{n_s - 1}
# Compute transfer function: T(k) = P_R(k) / P_R_ref(k)
```

---

## 5. Validation Tests

### 5a. Consistency Checks

1. **Standard inflation limit:** Turn off bounce (ρ_c → ∞). P_R(k) should recover the standard nearly scale-invariant spectrum with correct A_s and n_s.

2. **Wronskian conservation:** The Wronskian W[v_k, v_k*] = v_k v_k*' − v_k* v_k' = −i should be conserved throughout the evolution. Monitor |W + i| as an error diagnostic.

3. **Convergence test:** Double the number of time steps and verify P_R(k) changes by less than the target tolerance.

4. **Known LQC results:** Compare against published results from Agullo et al. (2012-2013) and Zhu et al. (2017) for standard LQC (no torsion). Our code with V_s = 0 should reproduce their spectra.

### 5b. Benchmark Parameters

For validation against standard LQC:
```
V(φ) = (1/2) m² φ²,  m = 1.21 × 10⁻⁶ M_Pl  (Planck-normalized)
V_s(n) = 0  (no spin condensate)
ρ_c = 0.27 ρ_Pl
φ_bounce = 0.97 M_Pl  (standard LQC initial condition)
```

Expected results:
- IR suppression for k < k_LQC ~ O(1) (in LQC Planck units)
- Oscillations at k ~ k_LQC
- Scale invariance at k ≫ k_LQC

---

## 6. Computational Cost Estimate

### Per-mode cost:
```
Integration range: ~100 e-folds in conformal time
Steps per e-fold: ~100-1000 (adaptive, depends on k)
Total steps per mode: ~10⁴ - 10⁵
Time per step: ~1 μs (RK evaluation)
Time per mode: ~0.01 - 0.1 seconds
```

### Total for one parameter point:
```
N_k = 5200 modes
Time per point: 5200 × 0.05s ≈ 4 minutes (single core)
With parallelism (8 cores): ~30 seconds per parameter point
```

### For a grid scan (Phase 5):
```
Grid size: 50 × 50 × 50 = 125,000 points (3 condensate parameters)
× 3 vacuum choices
Total: 375,000 evaluations
Single-core time: 375,000 × 4 min ≈ 25,000 CPU-hours
8-core parallelism: ~3,100 hours ≈ 130 days
GPU parallelism (1000 modes simultaneously): ~30 hours
```

### For MCMC:
```
Chain length: 10⁵ samples
Per sample: 30 seconds (with fast template, NOT full solver)
Full solver calibration grid: ~1000 points (to train template)
Calibration cost: 1000 × 4 min = 67 CPU-hours
```

---

## 7. Software Stack

| Component | Recommended | Alternative |
|-----------|------------|------------|
| Language | Python 3.11+ | Julia 1.10+ (2-5x faster ODE solves) |
| ODE solver | scipy.integrate.solve_ivp | DifferentialEquations.jl (Julia) |
| Interpolation | scipy.interpolate.CubicSpline | Interpolations.jl |
| Parallelism | multiprocessing (CPU) | JAX (GPU) |
| GPU acceleration | JAX + diffrax | CUDA + custom RK4 |
| Spectral derivatives | numpy FFT | FFTW |
| Output | HDF5 (h5py) | HDF5 |
| Plotting | matplotlib | matplotlib |

### Julia Advantage

Julia's DifferentialEquations.jl ecosystem is significantly faster for ODE integration:
- JIT compilation eliminates Python overhead
- Automatic differentiation for sensitivity analysis
- Built-in GPU ODE solvers (DiffEqGPU.jl)
- Estimated 5-10x speedup over Python scipy

### GPU Approach (for production runs)

Using JAX + diffrax or custom CUDA kernels:
- Evolve ALL k-modes simultaneously on GPU
- Each CUDA thread handles one k-mode
- Shared memory for background solution (common to all k)
- Estimated throughput: 10⁴ modes/second on A100

---

## 8. Output Specification

### Per parameter point:
```
output = {
    'background': {
        'tau': array[N_tau],
        'a': array[N_tau],
        'H': array[N_tau],
        'phi': array[N_tau],
        'n': array[N_tau],
        'epsilon1': array[N_tau],
        'c_s': array[N_tau],
        'z_pp_over_z': array[N_tau],
    },
    'power_spectrum': {
        'k': array[N_k],          # Mpc⁻¹
        'P_R': array[N_k],        # dimensionless
        'P_T_L': array[N_k],      # left-handed tensor
        'P_T_R': array[N_k],      # right-handed tensor
    },
    'diagnostics': {
        'wronskian_error': array[N_k],   # max |W + i| per mode
        'convergence': bool,
    },
    'parameters': {
        'V_s_params': dict,
        'V_phi_params': dict,
        'vacuum_type': str,
        'prescription': str,
    }
}
```

Storage per point: ~50 MB (compressed HDF5)
Total for grid: ~6 TB (full grid) or ~50 GB (compressed, storing only P_R(k))
