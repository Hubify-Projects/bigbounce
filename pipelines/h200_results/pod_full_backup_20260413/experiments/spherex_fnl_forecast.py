"""
SPHEREx f_NL Fisher Forecast: Bounce Detection Timeline
=========================================================
Computes σ(f_NL) for:
  1. Current DESI+SDSS multi-tracer (baseline comparison)
  2. SPHEREx-alone (400M galaxies, photometric redshifts)
  3. SPHEREx + DESI multi-tracer (combined forecast)
  4. SPHEREx + anomaly tracers (our bounce-specific multi-tracer)

Target: f_NL = -35/8 = -4.375 (matter bounce, parameter-free)
Question: When does this become detectable?

Uses GPU-accelerated Fisher matrix integration via PyTorch.
Reference: Seljak 2009, Schmittfull & Seljak 2018, Munchmeyer et al. 2019
"""

import os
import json
import time
import numpy as np
import torch

OUTPUT_DIR = "/root/results/spherex-fnl-forecast"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("=" * 70)
print("SPHEREX f_NL FISHER FORECAST: BOUNCE DETECTION TIMELINE")
print(f"  Device: {DEVICE}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# Cosmological parameters (Planck 2018 best-fit)
# -------------------------------------------------------------------------
H0        = 67.68          # km/s/Mpc
Omega_m   = 0.3089
Omega_b   = 0.0487
Omega_Lambda = 0.6911
sigma8    = 0.8159
n_s       = 0.9667
C_LIGHT   = 2.998e5        # km/s
f_NL_bounce = -35.0/8.0    # = -4.375, matter bounce prediction

print(f"  f_NL target: {f_NL_bounce:.4f} (matter bounce, parameter-free)")

# -------------------------------------------------------------------------
# Transfer function & growth factor (Eisenstein & Hu 1998 approximation)
# -------------------------------------------------------------------------
k_eq = 0.073 * Omega_m * H0**2 / C_LIGHT**2 * C_LIGHT  # h/Mpc

def transfer_function_torch(k):
    """Eisenstein & Hu 1998 approximation (no baryons). k in h/Mpc."""
    q = k / (13.41 * k_eq)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    T0 = torch.log(torch.tensor(np.e) + 1.8 * q) / (torch.log(torch.tensor(np.e) + 1.8 * q) + C0 * q**2)
    return T0

def growth_factor_approx(z):
    """ΛCDM growth factor D(z) normalized to D(0)=1."""
    a = 1.0 / (1.0 + z)
    Omega_z = Omega_m / a**3 / (Omega_m / a**3 + Omega_Lambda)
    return a * (1.0 + (5.0/7.0) * Omega_m * (1.0 - Omega_z))  # approximate

def comoving_distance(z):
    """Comoving distance in Mpc/h (simple trapezoidal integration)."""
    z_arr = np.linspace(0, z, 500)
    integrand = C_LIGHT / H0 / np.sqrt(Omega_m * (1+z_arr)**3 + Omega_Lambda)
    return np.trapezoid(integrand, z_arr) * H0 / 100.0  # convert to Mpc/h units

def hubble_at_z(z):
    """H(z) in km/s/Mpc."""
    return H0 * np.sqrt(Omega_m * (1+z)**3 + Omega_Lambda)

# -------------------------------------------------------------------------
# Matter power spectrum (linear, normalized to sigma8)
# -------------------------------------------------------------------------
K_GRID = torch.logspace(-4, 0, 500, device=DEVICE)  # h/Mpc

T_K = transfer_function_torch(K_GRID)
P_PRIMORDIAL = K_GRID**(n_s - 4)  # P(k) ~ k^{n_s-4} primordial
P_LINEAR_0 = P_PRIMORDIAL * T_K**2  # shape only

# Normalize to sigma8 at z=0
R8 = 8.0  # h/Mpc
W8 = 3.0 * (torch.sin(K_GRID * R8) - K_GRID * R8 * torch.cos(K_GRID * R8)) / (K_GRID * R8)**3
sigma8_unnorm = torch.sqrt(torch.trapz(K_GRID**2 * P_LINEAR_0 * W8**2 / (2.0 * np.pi**2), K_GRID))
A_s = (sigma8 / sigma8_unnorm.item())**2
P_LINEAR_0 = A_s * P_LINEAR_0

print(f"  sigma8 check: {torch.sqrt(torch.trapz(K_GRID**2 * P_LINEAR_0 * W8**2 / (2*np.pi**2), K_GRID)).item():.4f} (target: {sigma8})")

# -------------------------------------------------------------------------
# Scale-dependent bias from f_NL: Δb = 2 f_NL (b-1) δ_c / alpha(k,z)
# alpha(k,z) = (2/3)(kc/H0)² T(k) D(z) / Omega_m
# -------------------------------------------------------------------------
def alpha_fnl_torch(k, z):
    """Non-Gaussianity transfer function. k in h/Mpc."""
    T_k = transfer_function_torch(k)
    D_z = float(growth_factor_approx(z))
    c_over_H0 = C_LIGHT / H0  # ~2998 Mpc/h
    return (2.0 / 3.0) * (k * c_over_H0)**2 * T_k * D_z / Omega_m

# delta_c = 1.686
DELTA_C = 1.686

def delta_b_fnl(k, z, bias, f_NL=1.0):
    """Scale-dependent bias shift for unit f_NL."""
    return 2.0 * f_NL * (bias - 1.0) * DELTA_C / alpha_fnl_torch(k, z)

# -------------------------------------------------------------------------
# Survey definitions
# -------------------------------------------------------------------------
# Each survey: {name, n_bar (Mpc/h)^-3, bias b(z), z_mean, dz, f_sky, N_gal}
# SPHEREx: Munchmeyer et al. 2019, 400M galaxies, multi-z
SURVEYS = {
    "current_desi_sdss": {
        "description": "Current DESI+SDSS multi-tracer (our baseline)",
        "tracers": [
            {"name": "DESI_QSO",     "n_bar": 1e-5,  "b": 2.1, "z": 1.5, "dz": 1.0, "f_sky": 0.33, "N_gal": 2.9e6},
            {"name": "DESI_ELG",     "n_bar": 5e-4,  "b": 1.4, "z": 1.1, "dz": 0.8, "f_sky": 0.33, "N_gal": 1.7e7},
            {"name": "SDSS_QSO",     "n_bar": 1e-5,  "b": 2.5, "z": 1.8, "dz": 1.5, "f_sky": 0.25, "N_gal": 5e5},
            {"name": "anomaly_tracer","n_bar": 3e-7,  "b": 4.2, "z": 1.5, "dz": 1.0, "f_sky": 0.33, "N_gal": 328},  # our 328K anomalies, effective subsample
        ],
    },
    "spherex_alone": {
        "description": "SPHEREx standalone forecast (Munchmeyer+2019)",
        "tracers": [
            # SPHEREx photometric bins (5 redshift slices)
            {"name": "SPHEREx_z0.5",  "n_bar": 2e-2,  "b": 1.3, "z": 0.5, "dz": 0.5, "f_sky": 0.75, "N_gal": 4e7},
            {"name": "SPHEREx_z1.0",  "n_bar": 1e-2,  "b": 1.5, "z": 1.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 8e7},
            {"name": "SPHEREx_z1.5",  "n_bar": 5e-3,  "b": 1.7, "z": 1.5, "dz": 0.5, "f_sky": 0.75, "N_gal": 1e8},
            {"name": "SPHEREx_z2.0",  "n_bar": 2e-3,  "b": 2.0, "z": 2.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 1.2e8},
            {"name": "SPHEREx_z3.0",  "n_bar": 5e-4,  "b": 2.5, "z": 3.0, "dz": 1.0, "f_sky": 0.75, "N_gal": 5e7},
        ],
    },
    "spherex_plus_desi": {
        "description": "SPHEREx + DESI combined (multi-tracer)",
        "tracers": [
            # SPHEREx bins
            {"name": "SPHEREx_z0.5",  "n_bar": 2e-2,  "b": 1.3, "z": 0.5, "dz": 0.5, "f_sky": 0.75, "N_gal": 4e7},
            {"name": "SPHEREx_z1.0",  "n_bar": 1e-2,  "b": 1.5, "z": 1.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 8e7},
            {"name": "SPHEREx_z1.5",  "n_bar": 5e-3,  "b": 1.7, "z": 1.5, "dz": 0.5, "f_sky": 0.75, "N_gal": 1e8},
            {"name": "SPHEREx_z2.0",  "n_bar": 2e-3,  "b": 2.0, "z": 2.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 1.2e8},
            # DESI tracers
            {"name": "DESI_QSO",      "n_bar": 1e-5,  "b": 2.1, "z": 1.5, "dz": 1.0, "f_sky": 0.33, "N_gal": 2.9e6},
            {"name": "DESI_ELG",      "n_bar": 5e-4,  "b": 1.4, "z": 1.1, "dz": 0.8, "f_sky": 0.33, "N_gal": 1.7e7},
        ],
    },
    "spherex_plus_anomalies": {
        "description": "SPHEREx + our anomaly tracers (bounce-optimized)",
        "tracers": [
            # SPHEREx
            {"name": "SPHEREx_z1.0",  "n_bar": 1e-2,  "b": 1.5, "z": 1.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 8e7},
            {"name": "SPHEREx_z1.5",  "n_bar": 5e-3,  "b": 1.7, "z": 1.5, "dz": 0.5, "f_sky": 0.75, "N_gal": 1e8},
            {"name": "SPHEREx_z2.0",  "n_bar": 2e-3,  "b": 2.0, "z": 2.0, "dz": 0.5, "f_sky": 0.75, "N_gal": 1.2e8},
            # Anomaly tracers (high-bias)
            {"name": "anomaly_DESI",   "n_bar": 3e-6,  "b": 4.2, "z": 1.5, "dz": 1.0, "f_sky": 0.33, "N_gal": 1127},
            {"name": "anomaly_EROSITA","n_bar": 1e-6,  "b": 5.0, "z": 0.8, "dz": 0.6, "f_sky": 0.50, "N_gal": 6796}, # 73% novel
        ],
    },
}

# -------------------------------------------------------------------------
# [1/4] Single-tracer Fisher matrix for f_NL
# -------------------------------------------------------------------------
print("\n[1/4] Fisher matrix computation — single tracer f_NL...")

def compute_sigma_fnl_single(tracer, k_grid=K_GRID, n_k=500):
    """
    Compute σ(f_NL) for a single tracer using the Fisher matrix:
    F(f_NL) = (f_sky * V_survey / (4π²)) ∫ dk k² [∂ ln P(k) / ∂ f_NL]² / 2
    where ∂ ln P / ∂ f_NL = 2 Δb(k) / (b + Δb + 1/[n P(k)])
    """
    n_bar   = tracer["n_bar"]   # (Mpc/h)^-3
    b       = tracer["b"]       # galaxy bias
    z_mean  = tracer["z"]       # mean redshift
    f_sky   = tracer["f_sky"]   # sky fraction

    # Survey volume (Mpc/h)^3
    chi_min = comoving_distance(max(0.01, z_mean - tracer["dz"]/2))
    chi_max = comoving_distance(z_mean + tracer["dz"]/2)
    V_survey = f_sky * (4.0/3.0) * np.pi * (chi_max**3 - chi_min**3)

    # Growth factor at z_mean
    D_z = growth_factor_approx(z_mean)

    # P(k,z) = D(z)² P_linear(k,0)
    P_k_z = D_z**2 * P_LINEAR_0  # on K_GRID

    # Scale-dependent bias: Δb(k) = 2 f_NL (b-1) δ_c / alpha(k,z)
    alpha_k = alpha_fnl_torch(k_grid, z_mean)
    delta_b = 2.0 * (b - 1.0) * DELTA_C / alpha_k  # per unit f_NL

    # Shot noise
    P_shot = 1.0 / n_bar

    # Effective P(k): P_eff = (b + Δb·f_NL)² P(k,z) + 1/n
    # Derivative d(ln P_eff)/d(f_NL) at f_NL=0:
    # ≈ 2 δ_b / b  (shot noise term included)
    b_tot = b  # at f_NL=0
    P_eff = b_tot**2 * P_k_z + P_shot

    # Fisher integrand: (1/2) [2 δ_b P(k,z) / P_eff]²
    dlogP_dfnl = 2.0 * delta_b * P_k_z / P_eff

    # F(f_NL) = (f_sky * V / 4π²) ∫ dk k² (1/2) [dlogP/dfnl]²
    integrand = k_grid**2 * 0.5 * dlogP_dfnl**2
    F_fnl = float(f_sky) * V_survey / (4.0 * np.pi**2) * torch.trapz(integrand, k_grid).item()

    sigma_fnl = 1.0 / np.sqrt(max(F_fnl, 1e-30))
    return sigma_fnl, V_survey, F_fnl

# -------------------------------------------------------------------------
# [2/4] Multi-tracer Fisher matrix
# -------------------------------------------------------------------------
print("[2/4] Multi-tracer Fisher matrix...")

def compute_sigma_fnl_multitracer(tracers, k_grid=K_GRID):
    """
    Multi-tracer Fisher matrix for f_NL.
    F_MT(f_NL) = sum over k modes * (N_t x N_t covariance)
    For N tracers at same redshift, multi-tracer cancels cosmic variance.

    Using the Seljak 2009 multi-tracer estimator:
    σ_MT^{-2} = Σ_{ij} δb_i δb_j C_ij^{-1} × V/(4π²) ∫ dk k²
    where C_ij is the cross-power matrix.
    """
    # Group tracers by redshift bin (within dz tolerance)
    # For simplicity, use effective single-tracer Fisher at each z,
    # then apply multi-tracer improvement factor

    # First get single-tracer Fisher per bin
    F_single_list = []
    z_list = []
    n_list = []
    b_list = []
    delta_b_list = []
    V_list = []

    for t in tracers:
        sigma_i, V_i, F_i = compute_sigma_fnl_single(t, k_grid)
        F_single_list.append(F_i)
        z_list.append(t["z"])
        n_list.append(t["n_bar"])
        b_list.append(t["b"])
        V_list.append(V_i)

        # delta_b per unit f_NL at k=0.01 (scale representative)
        k_ref = torch.tensor([0.01], device=DEVICE)
        alpha_ref = alpha_fnl_torch(k_ref, t["z"])
        db_ref = 2.0 * (t["b"] - 1.0) * DELTA_C / alpha_ref.item()
        delta_b_list.append(abs(db_ref))

    # Multi-tracer gain factor (Seljak 2009 approximation):
    # The multi-tracer eliminates cosmic variance on very large scales.
    # For N tracers with different biases, the improvement scales as:
    # σ_MT / σ_single = 1 / sqrt(1 + Σ_i (δb_i / σ_P_i)² × V_survey)
    #
    # Practical approximation: compute Fisher matrix summed over k
    # using the full N_t × N_t covariance matrix

    n_tracers = len(tracers)
    if n_tracers == 1:
        sigma_total = 1.0 / np.sqrt(max(F_single_list[0], 1e-30))
        return sigma_total, F_single_list[0]

    # Sum all single-tracer Fisher (ignores multi-tracer gain)
    F_sum_single = sum(F_single_list)
    sigma_single_combined = 1.0 / np.sqrt(max(F_sum_single, 1e-30))

    # Multi-tracer Fisher via full covariance inversion
    # Use k=0.003 h/Mpc (where scale-dependent bias dominates)
    k_mt_vals = torch.logspace(-3.5, -1.0, 200, device=DEVICE)

    F_mt_total = 0.0

    # Representative effective volume for multi-tracer (use largest overlap volume)
    f_sky_eff = max(t["f_sky"] for t in tracers)
    # Pick dominant z range
    z_rep = np.median(z_list)
    chi_min = comoving_distance(max(0.01, z_rep - 0.5))
    chi_max = comoving_distance(z_rep + 0.5)
    V_eff = f_sky_eff * (4.0/3.0) * np.pi * (chi_max**3 - chi_min**3)

    # For each k mode, build the N_t × N_t covariance and invert
    # C_ij(k) = [b_i + Δb_i(k,f_NL)] [b_j + Δb_j(k,f_NL)] P(k,z) + δ_ij/n_i
    # ∂C/∂f_NL at f_NL=0: [Δb_i(k) b_j + b_i Δb_j(k)] P(k,z)

    for k_val in k_mt_vals:
        k_scalar = k_val.item()
        alpha_vals = []
        delta_b_k = []
        P_k_vals = []

        for i, t in enumerate(tracers):
            D_zi = growth_factor_approx(t["z"])
            k_ten = torch.tensor([k_scalar], device=DEVICE)
            T_ki = transfer_function_torch(k_ten)
            P_ki = D_zi**2 * A_s * k_scalar**(n_s-4) * T_ki.item()**2

            a_i = alpha_fnl_torch(k_ten, t["z"]).item()
            db_i = 2.0 * (t["b"] - 1.0) * DELTA_C / a_i

            P_k_vals.append(P_ki)
            delta_b_k.append(db_i)

        # Build signal + noise matrix C (using geometric mean z-dependent P)
        C = np.zeros((n_tracers, n_tracers))
        dC = np.zeros((n_tracers, n_tracers))  # ∂C/∂f_NL

        for i in range(n_tracers):
            for j in range(n_tracers):
                b_i = tracers[i]["b"]
                b_j = tracers[j]["b"]
                # Use geometric mean of P for cross terms
                P_ij = np.sqrt(P_k_vals[i] * P_k_vals[j])
                C[i,j] = b_i * b_j * P_ij
                if i == j:
                    C[i,j] += 1.0 / tracers[i]["n_bar"]
                # ∂C_ij/∂f_NL = [Δb_i(k) b_j + b_i Δb_j(k)] P_ij
                dC[i,j] = (delta_b_k[i] * b_j + b_i * delta_b_k[j]) * P_ij

        # Fisher: F_k = (1/2) Tr[C^{-1} dC C^{-1} dC]
        try:
            C_inv = np.linalg.inv(C)
            M = C_inv @ dC
            F_k = 0.5 * np.trace(M @ M)
        except np.linalg.LinAlgError:
            F_k = 0.0

        # dk contribution (log spacing)
        if len(k_mt_vals) > 1:
            dk = k_scalar * (np.log(k_mt_vals[-1].item()) - np.log(k_mt_vals[0].item())) / (len(k_mt_vals) - 1)
        else:
            dk = 1e-3

        F_mt_total += V_eff / (4.0 * np.pi**2) * k_scalar**2 * F_k * dk

    sigma_mt = 1.0 / np.sqrt(max(F_mt_total, 1e-30))
    return sigma_mt, F_mt_total

# -------------------------------------------------------------------------
# [3/4] Run all forecasts
# -------------------------------------------------------------------------
print("\n[3/4] Running all survey forecasts...")

results = {}

for survey_name, survey in SURVEYS.items():
    print(f"\n  Survey: {survey_name}")
    print(f"  Description: {survey['description']}")
    print(f"  N tracers: {len(survey['tracers'])}")

    # Single-tracer Fisher (summed)
    F_singles = []
    for t in survey["tracers"]:
        sig_i, V_i, F_i = compute_sigma_fnl_single(t)
        F_singles.append(F_i)
        print(f"    {t['name']}: σ(f_NL)={1/np.sqrt(max(F_i,1e-30)):.2f}, V={V_i:.2e} (Mpc/h)³")

    sigma_single = 1.0 / np.sqrt(max(sum(F_singles), 1e-30))

    # Multi-tracer
    sigma_mt, F_mt = compute_sigma_fnl_multitracer(survey["tracers"])

    # Improvement
    improvement_pct = 100.0 * (sigma_single - sigma_mt) / sigma_single if sigma_single > 0 else 0.0

    # Detection significance for f_NL = -4.375
    detection_snr_single = abs(f_NL_bounce) / max(sigma_single, 1e-30)
    detection_snr_mt = abs(f_NL_bounce) / max(sigma_mt, 1e-30)

    # Years to detection (simple scaling: σ ∝ 1/√V ∝ 1/√time)
    # At current σ=11.71, we need σ=4.375/3 ≈ 1.46 for 3σ detection
    target_3sigma = abs(f_NL_bounce) / 3.0
    years_to_3sigma_mt = None
    if sigma_mt > target_3sigma:
        years_to_3sigma_mt = ((sigma_mt / target_3sigma)**2)  # relative to current survey time

    print(f"  σ(f_NL) single-tracer combined: {sigma_single:.3f}")
    print(f"  σ(f_NL) multi-tracer: {sigma_mt:.3f}")
    print(f"  Multi-tracer improvement: {improvement_pct:.1f}%")
    print(f"  Bounce f_NL=-4.375 detection: {detection_snr_mt:.2f}σ (multi-tracer)")

    results[survey_name] = {
        "description": survey["description"],
        "n_tracers": len(survey["tracers"]),
        "sigma_fnl_single": round(sigma_single, 4),
        "sigma_fnl_multitracer": round(sigma_mt, 4),
        "improvement_pct": round(improvement_pct, 2),
        "bounce_detection_sigma_single": round(detection_snr_single, 3),
        "bounce_detection_sigma_mt": round(detection_snr_mt, 3),
    }

# -------------------------------------------------------------------------
# [4/4] Summary: detection timeline
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("[4/4] DETECTION TIMELINE SUMMARY")
print("=" * 70)

print(f"\n  f_NL bounce = {f_NL_bounce:.4f} (parameter-free matter bounce prediction)")
print(f"\n  {'Survey':<35s} {'σ(f_NL) MT':>12s} {'Bounce SNR':>12s} {'3σ detect?':>12s}")
print("  " + "-" * 75)
for name, res in results.items():
    snr = res["bounce_detection_sigma_mt"]
    detected = "YES" if snr >= 3.0 else "no"
    print(f"  {name:<35s} {res['sigma_fnl_multitracer']:>12.3f} {snr:>12.2f}σ {detected:>12s}")

# SPHEREx detection timeline
spherex_sigma = results["spherex_alone"]["sigma_fnl_multitracer"]
spherex_snr = results["spherex_alone"]["bounce_detection_sigma_mt"]
current_sigma = results["current_desi_sdss"]["sigma_fnl_multitracer"]
current_snr = results["current_desi_sdss"]["bounce_detection_sigma_mt"]
combined_sigma = results["spherex_plus_desi"]["sigma_fnl_multitracer"]
combined_snr = results["spherex_plus_desi"]["bounce_detection_sigma_mt"]

print(f"\n  KEY RESULTS:")
print(f"  Current multi-tracer: σ = {current_sigma:.2f} → {current_snr:.2f}σ on bounce f_NL")
print(f"  SPHEREx alone: σ = {spherex_sigma:.2f} → {spherex_snr:.2f}σ on bounce f_NL")
print(f"  SPHEREx+DESI:  σ = {combined_sigma:.2f} → {combined_snr:.2f}σ on bounce f_NL")

# Improvement factors
print(f"\n  SPHEREx vs current: {current_sigma/spherex_sigma:.1f}× improvement")
print(f"  SPHEREx+DESI vs current: {current_sigma/combined_sigma:.1f}× improvement")

# When does bounce become detectable?
target_2sigma = abs(f_NL_bounce) / 2.0
target_3sigma = abs(f_NL_bounce) / 3.0
target_5sigma = abs(f_NL_bounce) / 5.0
print(f"\n  Detection thresholds for f_NL = {f_NL_bounce:.4f}:")
print(f"  2σ detection: σ(f_NL) < {target_2sigma:.3f}")
print(f"  3σ detection: σ(f_NL) < {target_3sigma:.3f}")
print(f"  5σ detection: σ(f_NL) < {target_5sigma:.3f}")

timeline = {
    "current_status": f"σ={current_sigma:.2f}, SNR={current_snr:.2f}σ — NOT YET DETECTABLE",
    "spherex_2027_status": f"σ={spherex_sigma:.2f}, SNR={spherex_snr:.2f}σ — {'DETECTABLE at 3σ' if spherex_snr >= 3.0 else 'needs combination'}",
    "spherex_plus_desi_status": f"σ={combined_sigma:.2f}, SNR={combined_snr:.2f}σ — {'DETECTABLE at 3σ' if combined_snr >= 3.0 else 'marginal'}",
}
for k, v in timeline.items():
    print(f"  {k}: {v}")

elapsed = time.time() - t0
print(f"\n  Runtime: {elapsed:.1f}s")

summary = {
    "experiment": "SPHEREx f_NL Fisher Forecast: Bounce Detection Timeline",
    "device": str(DEVICE),
    "f_NL_bounce_target": f_NL_bounce,
    "cosmology": {"H0": H0, "Omega_m": Omega_m, "sigma8": sigma8, "n_s": n_s},
    "results": results,
    "timeline": timeline,
    "detection_thresholds": {
        "2sigma": round(target_2sigma, 4),
        "3sigma": round(target_3sigma, 4),
        "5sigma": round(target_5sigma, 4),
    },
    "key_comparison": {
        "current_sigma": round(current_sigma, 3),
        "spherex_sigma": round(spherex_sigma, 3),
        "spherex_plus_desi_sigma": round(combined_sigma, 3),
        "spherex_improvement_factor": round(current_sigma/max(spherex_sigma, 1e-10), 2),
        "bounce_detectable_spherex": spherex_snr >= 3.0,
        "bounce_detectable_spherex_desi": combined_snr >= 3.0,
    },
    "runtime_seconds": elapsed,
}

try:
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
except Exception as e:
    print(f"[warn] json save: {e}")

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
