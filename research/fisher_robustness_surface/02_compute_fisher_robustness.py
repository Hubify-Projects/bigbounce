#!/usr/bin/env python3
"""
Fisher forecast for σ(f_NL) from scale-dependent bias.

Computes the Fisher information on f_NL from the galaxy power spectrum,
scanning over survey assumptions to map the robustness surface.

The scale-dependent bias effect (Dalal et al. 2008):
  b(k,z) = b₁ + Δb(k) where Δb(k) = 2(b₁-1)·f_NL·δ_c / [D(z)·T(k)·(k/k_pivot)²·(3Ω_m H₀²/2)]

For a galaxy survey, the Fisher information on f_NL is:
  F(f_NL) = Σ_k [ (∂P_g/∂f_NL)² / Var(P_g) ]

where P_g(k) = [b₁ + Δb(k)]² · P_m(k) + 1/n_g  (shot noise)
and Var(P_g) = 2·P_g²/(N_modes) with N_modes = V_eff·k²·Δk/(2π²).

Multi-tracer: with N_t tracers, cosmic variance cancels and
σ(f_NL)_multi ≈ σ(f_NL)_single / √(N_t · contrast_factor).
"""
import numpy as np

# ==================================================================
# COSMOLOGICAL PARAMETERS (Planck 2018 LCDM)
# ==================================================================
h = 0.6736
Omega_m = 0.3153
delta_c = 1.686  # spherical collapse threshold
H0 = 100 * h  # km/s/Mpc

# Simple matter power spectrum P_m(k) ~ k^(n_s-4) · T(k)² (Eisenstein-Hu approximation)
n_s = 0.9649
A_s = 2.1e-9  # scalar amplitude
k_pivot = 0.05  # Mpc^-1

def transfer_function(k_hMpc):
    """Simple Eisenstein-Hu-like transfer function (no BAO wiggles)."""
    k_eq = 0.073 * Omega_m * h  # matter-radiation equality scale
    q = k_hMpc / k_eq
    T = np.log(1 + 2.34*q) / (2.34*q) * (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    return np.where(k_hMpc > 0, T, 1.0)

def growth_factor(z):
    """Approximate growth factor D(z)/D(0) for LCDM."""
    Omega_z = Omega_m * (1+z)**3 / (Omega_m*(1+z)**3 + 1-Omega_m)
    return (1/(1+z)) * (5*Omega_z/2) / (Omega_z**(4/7) - (1-Omega_z) + (1+Omega_z/2)*(1+(1-Omega_z)/70))

def P_matter(k_hMpc, z=0):
    """Matter power spectrum P_m(k) in (Mpc/h)³."""
    T = transfer_function(k_hMpc)
    D = growth_factor(z) / growth_factor(0)
    # Normalize to A_s at k_pivot
    P = A_s * (k_hMpc * h / k_pivot)**(n_s - 1) * T**2 * (2*np.pi**2 / k_hMpc**3) * D**2
    # Convert to h^-3 Mpc^3 units
    return P * h**3


# ==================================================================
# SCALE-DEPENDENT BIAS
# ==================================================================

def delta_b(k_hMpc, z, b1, f_NL):
    """Scale-dependent bias correction Δb(k) = 2(b₁-1)·f_NL·δ_c / [D(z)·T(k)·α(k)]
    where α(k) = k²·T(k)·D(z)·(2/3)·(H₀²Ω_m) / (c² actually but we use Poisson eq form)

    More precisely: Δb = 3·f_NL·(b₁-1)·δ_c·Ω_m·H₀² / (c²·k²·T(k)·D(z))
    In h/Mpc units: Δb = 3·f_NL·(b₁-1)·δ_c·Ω_m / (D(z)·T(k)·(k/H0_hMpc)²)
    """
    D = growth_factor(z) / growth_factor(0)
    T = transfer_function(k_hMpc)
    # Dalal et al. formula: Δb = f_NL · (b₁-1) · 3δ_c Ω_m H₀² / (k² T(k) D(z) c²)
    # In natural units with k in h/Mpc, H₀ in h·km/s/Mpc:
    # Factor = 3·δ_c·Ω_m·(H₀/c)² where H₀/c = 1/(2997.9 Mpc) for h=1
    H0_over_c = h / 2997.9  # in h/Mpc units
    factor = 3 * delta_c * Omega_m * H0_over_c**2
    return f_NL * (b1 - 1) * factor / (k_hMpc**2 * T * D)


# ==================================================================
# FISHER INFORMATION ON f_NL
# ==================================================================

def compute_sigma_fnl(z=2.5, b1=2.0, n_g=1e-3, V_survey=50.0,
                      k_min=1e-3, k_max=0.1, n_k=200,
                      sigma_z=0.0, n_tracers=1, tracer_contrast=1.5,
                      f_NL_fiducial=0.0):
    """
    Compute σ(f_NL) from scale-dependent bias Fisher forecast.

    Parameters:
        z: effective redshift
        b1: linear galaxy bias
        n_g: galaxy number density [(h/Mpc)³]
        V_survey: survey volume [Gpc/h)³]
        k_min: minimum k [h/Mpc]
        k_max: maximum k [h/Mpc]
        n_k: number of k bins
        sigma_z: photo-z scatter σ_z/(1+z) — degrades radial modes
        n_tracers: number of galaxy tracers
        tracer_contrast: bias ratio b₂/b₁ for multi-tracer
        f_NL_fiducial: fiducial f_NL (usually 0)
    """
    V = V_survey * 1e9  # convert Gpc³ to (Mpc/h)³ ... wait
    # V_survey in (Gpc/h)³ = 10⁹ (Mpc/h)³ each
    V = V_survey * 1e9  # (Mpc/h)³

    k_arr = np.geomspace(k_min, k_max, n_k)
    dk_arr = np.diff(np.log(k_arr))  # dlog(k) spacing

    Fisher = 0.0

    for i in range(len(k_arr) - 1):
        k = k_arr[i]
        dlnk = dk_arr[i]

        # Matter power spectrum
        Pm = P_matter(k, z)

        # Scale-dependent bias
        db = delta_b(k, z, b1, f_NL_fiducial)
        b_total = b1 + db

        # Galaxy power spectrum (signal + shot noise)
        Pg = b_total**2 * Pm + 1.0/n_g

        # Photo-z degradation: reduces effective radial modes
        # The photo-z scatter washes out radial information for k_parallel > 1/σ_r
        # where σ_r = c·σ_z·(1+z)/H(z) ~ 3000·σ_z·(1+z)/H(z) Mpc/h
        # For k_parallel > k_rad_cutoff, radial modes are lost
        # This effectively reduces the survey volume for those k's
        if sigma_z > 0:
            H_z = H0 * np.sqrt(Omega_m*(1+z)**3 + 1-Omega_m)  # km/s/Mpc
            sigma_r = 2997.9 * sigma_z * (1+z) / (H_z/h)  # Mpc/h
            # Fraction of modes retained: for isotropic k, ~min(1, 1/(k·σ_r))
            # More precisely: the radial FoG-like damping reduces P_g by exp(-k²σ_r²μ²)
            # Averaged over μ: effective degradation factor
            x = k * sigma_r
            if x > 0.01:
                photo_z_factor = np.sqrt(np.pi/2) * (1.0/x) * (1 - np.exp(-x**2/2))
                photo_z_factor = min(photo_z_factor, 1.0)
            else:
                photo_z_factor = 1.0
        else:
            photo_z_factor = 1.0

        # Number of modes in the k-shell
        N_modes = V * k**2 * dlnk * k / (2 * np.pi**2) * photo_z_factor

        if N_modes <= 0:
            continue

        # Derivative of P_g with respect to f_NL
        # d(Pg)/d(f_NL) = 2·b_total·(db/df_NL)·Pm
        # where db/df_NL = Δb/f_NL evaluated at f_NL_fiducial
        # At f_NL_fiducial = 0: db/df_NL = delta_b(k, z, b1, 1.0)
        db_per_fnl = delta_b(k, z, b1, 1.0)
        dPg_dfnl = 2 * b_total * db_per_fnl * Pm

        # Fisher information (Gaussian approximation)
        # F = Σ (dP/df)² / (2P²/N_modes) = Σ N_modes·(dP/df)²/(2P²)
        Fisher += N_modes * dPg_dfnl**2 / (2 * Pg**2)

    # Multi-tracer enhancement
    # With N_t tracers of different bias, cosmic variance partially cancels
    # Enhancement factor ~ N_t × (1 + (b₂/b₁ - 1)²)^(1/2) approximately
    # Simplified: multi-tracer reduces σ by ~ √(N_t × contrast_factor)
    if n_tracers > 1:
        # Seljak (2009) multi-tracer: the improvement scales as
        # σ_multi / σ_single ~ 1/√(N_t) for well-separated tracers
        # More realistically: improvement factor depends on bias contrast
        multi_factor = n_tracers * (1 + (tracer_contrast - 1)**2)
        Fisher *= multi_factor

    sigma_fnl = 1.0 / np.sqrt(Fisher) if Fisher > 0 else np.inf
    return sigma_fnl


# ==================================================================
# SURVEY CONFIGURATIONS
# ==================================================================

# SPHEREx-like
SPHEREX = {
    'name': 'SPHEREx',
    'z': 1.5,
    'b1': 1.8,
    'n_g': 3e-3,  # fairly dense photometric sample
    'V_survey': 30.0,  # ~30 (Gpc/h)³ effective
    'sigma_z': 0.03,  # photo-z scatter σ_z/(1+z)
    'n_tracers': 1,
    'tracer_contrast': 1.0,
    'k_min': 5e-4,
    'k_max': 0.1,
}

# MegaMapper-like
MEGAMAPPER = {
    'name': 'MegaMapper',
    'z': 3.0,
    'b1': 3.0,
    'n_g': 5e-4,  # sparser spectroscopic sample at high z
    'V_survey': 100.0,  # ~100 (Gpc/h)³
    'sigma_z': 0.001,  # spectroscopic: excellent radial resolution
    'n_tracers': 2,
    'tracer_contrast': 2.0,
    'k_min': 2e-4,
    'k_max': 0.15,
}


def run_baseline():
    """Run baseline forecasts for both surveys."""
    print("=" * 70)
    print("FISHER FORECAST: σ(f_NL) FROM SCALE-DEPENDENT BIAS")
    print("=" * 70)

    fnl_signal = 4.375

    for survey in [SPHEREX, MEGAMAPPER]:
        sigma = compute_sigma_fnl(**{k: v for k, v in survey.items() if k != 'name'})
        sig = fnl_signal / sigma
        print(f"\n{survey['name']}:")
        print(f"  σ(f_NL) = {sigma:.3f}")
        print(f"  |f_NL|/σ = {sig:.1f}σ")


def run_robustness_scan():
    """Scan over fragile assumptions."""
    fnl_signal = 4.375

    print("\n" + "=" * 70)
    print("ROBUSTNESS SCAN")
    print("=" * 70)

    # --- SCAN 1: Multi-tracer for MegaMapper ---
    print("\n--- MegaMapper: Multi-tracer vs Single-tracer ---")
    for n_t, tc in [(1, 1.0), (2, 1.5), (2, 2.0), (2, 3.0), (3, 2.0)]:
        cfg = {k: v for k, v in MEGAMAPPER.items() if k != 'name'}
        cfg['n_tracers'] = n_t
        cfg['tracer_contrast'] = tc
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  N_tracer={n_t}, contrast={tc:.1f}: σ={sigma:.3f}, significance={sig:.1f}σ")

    # --- SCAN 2: Photo-z for SPHEREx ---
    print("\n--- SPHEREx: Photo-z degradation ---")
    for sz in [0.003, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1]:
        cfg = {k: v for k, v in SPHEREX.items() if k != 'name'}
        cfg['sigma_z'] = sz
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  σ_z/(1+z) = {sz:.3f}: σ(f_NL)={sigma:.3f}, significance={sig:.1f}σ")

    # --- SCAN 3: k_min for both ---
    print("\n--- k_min scan (MegaMapper) ---")
    for km in [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2]:
        cfg = {k: v for k, v in MEGAMAPPER.items() if k != 'name'}
        cfg['k_min'] = km
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  k_min={km:.1e}: σ={sigma:.3f}, significance={sig:.1f}σ")

    print("\n--- k_min scan (SPHEREx) ---")
    for km in [1e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2]:
        cfg = {k: v for k, v in SPHEREX.items() if k != 'name'}
        cfg['k_min'] = km
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  k_min={km:.1e}: σ={sigma:.3f}, significance={sig:.1f}σ")

    # --- SCAN 4: Galaxy bias ---
    print("\n--- Galaxy bias scan (MegaMapper) ---")
    for b1 in [1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
        cfg = {k: v for k, v in MEGAMAPPER.items() if k != 'name'}
        cfg['b1'] = b1
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  b₁={b1:.1f}: σ={sigma:.3f}, significance={sig:.1f}σ")

    # --- SCAN 5: Number density ---
    print("\n--- Number density scan (MegaMapper) ---")
    for ng in [1e-4, 3e-4, 5e-4, 1e-3, 3e-3]:
        cfg = {k: v for k, v in MEGAMAPPER.items() if k != 'name'}
        cfg['n_g'] = ng
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        print(f"  n_g={ng:.1e}: σ={sigma:.3f}, significance={sig:.1f}σ")

    # --- SCAN 6: Combined worst/best cases ---
    print("\n--- Combined Scenarios ---")
    scenarios = [
        ("MegaMapper BEST", {**{k:v for k,v in MEGAMAPPER.items() if k!='name'},
                            'n_tracers':3, 'tracer_contrast':2.5, 'k_min':1e-4}),
        ("MegaMapper CENTRAL", {k:v for k,v in MEGAMAPPER.items() if k!='name'}),
        ("MegaMapper CONSERVATIVE", {**{k:v for k,v in MEGAMAPPER.items() if k!='name'},
                                     'n_tracers':2, 'tracer_contrast':1.3, 'k_min':1e-3}),
        ("MegaMapper SINGLE-TRACER", {**{k:v for k,v in MEGAMAPPER.items() if k!='name'},
                                      'n_tracers':1, 'k_min':1e-3}),
        ("SPHEREx BEST", {**{k:v for k,v in SPHEREX.items() if k!='name'},
                          'sigma_z':0.003, 'k_min':2e-4}),
        ("SPHEREx CENTRAL", {k:v for k,v in SPHEREX.items() if k!='name'}),
        ("SPHEREx CONSERVATIVE", {**{k:v for k,v in SPHEREX.items() if k!='name'},
                                  'sigma_z':0.06, 'k_min':2e-3}),
        ("SPHEREx PESSIMISTIC", {**{k:v for k,v in SPHEREX.items() if k!='name'},
                                 'sigma_z':0.1, 'k_min':5e-3}),
    ]
    for name, cfg in scenarios:
        sigma = compute_sigma_fnl(**cfg)
        sig = fnl_signal / sigma
        label = "DECISIVE" if sig>=5 else "STRONG" if sig>=3 else "HINT" if sig>=2 else "WEAK"
        print(f"  {name:30s}: σ={sigma:.3f}, {sig:.1f}σ [{label}]")


if __name__ == "__main__":
    run_baseline()
    run_robustness_scan()
    print("\nDone.")
