#!/usr/bin/env python3
"""
Mock-Based Estimator Realism Validation.

Generates synthetic galaxy power spectrum observations with:
  - Bounce signal (f_NL = -4.375) via scale-dependent bias
  - Realistic shot noise and cosmic variance
  - Survey window / effective k_min loss
  - GR systematic contamination
  - b_phi uncertainty
  - Multi-tracer success/failure

Then RECOVERS the Bayes factor from the mock data by fitting
bounce vs inflation models to the synthetic observations.

This goes BEYOND the closed-form Monte Carlo by actually
generating and fitting mock power spectra.
"""
import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize_scalar

# ============================================================
# COSMOLOGICAL SETUP (simplified but physical)
# ============================================================
h = 0.6736
Omega_m = 0.3153
delta_c = 1.686
n_s = 0.9649

def transfer_function(k):
    k_eq = 0.073 * Omega_m * h
    q = k / k_eq
    T = np.log(1 + 2.34*q) / (2.34*q + 1e-30) * (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    return np.where(k > 0, T, 1.0)

def growth_factor(z):
    Oz = Omega_m * (1+z)**3 / (Omega_m*(1+z)**3 + 1-Omega_m)
    return (1/(1+z)) * (5*Oz/2) / (Oz**(4/7) - (1-Oz) + (1+Oz/2)*(1+(1-Oz)/70))

def P_matter(k, z):
    A_s = 2.1e-9
    k_piv = 0.05
    T = transfer_function(k)
    D = growth_factor(z) / growth_factor(0)
    return A_s * (k*h/k_piv)**(n_s-1) * T**2 * (2*np.pi**2/k**3) * D**2 * h**3

def delta_b_per_fnl(k, z, b1):
    """Scale-dependent bias per unit f_NL."""
    H0c = h / 2997.9
    D = growth_factor(z) / growth_factor(0)
    T = transfer_function(k)
    return (b1 - 1) * 3 * delta_c * Omega_m * H0c**2 / (k**2 * T * D + 1e-30)


# ============================================================
# MOCK POWER SPECTRUM GENERATOR
# ============================================================

def generate_mock_Pk(k_arr, z, b1, n_g, f_NL_true, V_eff,
                     gr_shift=0.0, bphi_error=0.0):
    """
    Generate a mock galaxy power spectrum observation.

    Returns: (P_obs, sigma_P) for each k bin.
    P_obs includes signal + noise + systematics.
    sigma_P is the Gaussian error on each P(k) bin.
    """
    Pm = P_matter(k_arr, z)

    # True scale-dependent bias
    db = delta_b_per_fnl(k_arr, z, b1) * f_NL_true

    # b_phi error: the observer THINKS b_phi = standard, but it's off
    # This effectively shifts the inferred f_NL
    db_observed = db * (1 + bphi_error)

    # GR systematic: adds a fake 1/k^2 signal
    db_gr = delta_b_per_fnl(k_arr, z, b1) * gr_shift

    # Total observed bias
    b_total = b1 + db_observed + db_gr

    # Galaxy power spectrum
    Pg_true = b_total**2 * Pm + 1.0/n_g

    # Number of modes per k-bin
    dk = np.diff(np.log(k_arr), prepend=np.log(k_arr[0]) - 0.1)
    N_modes = V_eff * k_arr**2 * dk * k_arr / (2 * np.pi**2)
    N_modes = np.maximum(N_modes, 1)

    # Gaussian error
    sigma_P = Pg_true * np.sqrt(2.0 / N_modes)

    # Observed power (add noise realization)
    P_obs = Pg_true + np.random.randn(len(k_arr)) * sigma_P

    return P_obs, sigma_P, Pm


def fit_fnl_from_mock(k_arr, P_obs, sigma_P, Pm, z, b1, n_g):
    """
    Fit f_NL from mock power spectrum data.
    Returns: best-fit f_NL and chi2 for bounce model and free-f_NL model.
    """
    def chi2(f_NL):
        db = delta_b_per_fnl(k_arr, z, b1) * f_NL
        b_total = b1 + db
        Pg_model = b_total**2 * Pm + 1.0/n_g
        return np.sum(((P_obs - Pg_model) / sigma_P)**2)

    # Bounce model: f_NL fixed at -4.375
    chi2_bounce = chi2(-35.0/8.0)

    # Best-fit f_NL (free parameter)
    result = minimize_scalar(chi2, bounds=(-15, 15), method='bounded')
    fnl_bestfit = result.x
    chi2_bestfit = result.fun

    # Standard inflation: f_NL = 0
    chi2_ssfsr = chi2(0.015)

    return fnl_bestfit, chi2_bounce, chi2_bestfit, chi2_ssfsr


# ============================================================
# FULL MOCK ENSEMBLE
# ============================================================

def run_mock_ensemble(n_mocks=100000, seed=42):
    """Run the full mock-based validation ensemble."""
    rng = np.random.default_rng(seed)
    np.random.seed(seed)

    # Survey configurations
    configs = [
        {
            'name': 'SPHEREx-like',
            'z': 1.5, 'b1': 1.8, 'n_g': 3e-3,
            'V_eff': 30e9,  # 30 (Gpc/h)^3 in (Mpc/h)^3
            'k_min_base': 3e-4, 'k_max': 0.1,
            'gr_sigma': 0.3, 'bphi_sigma': 0.15,
        },
        {
            'name': 'MegaMapper-like',
            'z': 3.0, 'b1': 3.0, 'n_g': 5e-4,
            'V_eff': 100e9,
            'k_min_base': 2e-4, 'k_max': 0.15,
            'gr_sigma': 0.7, 'bphi_sigma': 0.2,
        },
    ]

    FNL_TRUE = -35.0/8.0
    n_k = 30  # number of k bins

    for cfg in configs:
        print(f"\n{'='*70}")
        print(f"MOCK ENSEMBLE: {cfg['name']} ({n_mocks} mocks)")
        print(f"{'='*70}")

        # Storage
        fnl_recovered = np.zeros(n_mocks)
        chi2_bounce_arr = np.zeros(n_mocks)
        chi2_free_arr = np.zeros(n_mocks)
        chi2_ssfsr_arr = np.zeros(n_mocks)

        for i in range(n_mocks):
            # Randomize survey assumptions
            k_min_eff = cfg['k_min_base'] * rng.lognormal(0, 0.3)
            k_min_eff = np.clip(k_min_eff, 1e-4, 5e-3)

            gr_shift = rng.normal(0, cfg['gr_sigma'])
            bphi_err = rng.normal(0, cfg['bphi_sigma'])

            # Multi-tracer for MegaMapper (70% success)
            if 'MegaMapper' in cfg['name']:
                mt_success = rng.random() < 0.7
                V_eff = cfg['V_eff'] if mt_success else cfg['V_eff'] / 9
            else:
                V_eff = cfg['V_eff']

            k_arr = np.geomspace(k_min_eff, cfg['k_max'], n_k)

            # Generate mock
            P_obs, sigma_P, Pm = generate_mock_Pk(
                k_arr, cfg['z'], cfg['b1'], cfg['n_g'],
                FNL_TRUE, V_eff, gr_shift, bphi_err)

            # Fit
            fnl_bf, chi2_b, chi2_f, chi2_s = fit_fnl_from_mock(
                k_arr, P_obs, sigma_P, Pm, cfg['z'], cfg['b1'], cfg['n_g'])

            fnl_recovered[i] = fnl_bf
            chi2_bounce_arr[i] = chi2_b
            chi2_free_arr[i] = chi2_f
            chi2_ssfsr_arr[i] = chi2_s

        # Bayes factor proxy: exp(-Δχ²/2) × Occam factor
        # BF(bounce vs free) ≈ (prior_width) × exp(-(χ²_bounce - χ²_free)/2)
        # For free model with prior [-15,+15]: Occam = 30 × σ_posterior / prior_width
        delta_chi2_bf = chi2_bounce_arr - chi2_free_arr
        # Approximate: BF ≈ prior_width / (2πσ²)^(1/2) × exp(-Δχ²/2)
        # where σ is the posterior width on f_NL
        # Simplified: use the Laplace approximation
        bf_bounce_vs_free = 30 * np.exp(-delta_chi2_bf / 2)  # Occam × likelihood ratio

        delta_chi2_bs = chi2_bounce_arr - chi2_ssfsr_arr
        bf_bounce_vs_ssfsr = np.exp(-delta_chi2_bs / 2)

        # Report
        print(f"\n  f_NL recovered: median={np.median(fnl_recovered):.3f}, "
              f"std={np.std(fnl_recovered):.3f}")
        print(f"  f_NL true: {FNL_TRUE:.3f}")
        print(f"  Bias (median - true): {np.median(fnl_recovered) - FNL_TRUE:.3f}")

        bf = np.clip(bf_bounce_vs_free, 1e-10, 1e10)
        print(f"\n  Bounce vs Free-f_NL (Laplace approx):")
        print(f"    Median BF:           {np.median(bf):.1f}")
        print(f"    P(BF > 3) [moderate]:{np.mean(bf > 3)*100:.1f}%")
        print(f"    P(BF > 10) [strong]: {np.mean(bf > 10)*100:.1f}%")
        print(f"    P(BF < 1) [free wins]:{np.mean(bf < 1)*100:.1f}%")

        bf2 = np.clip(bf_bounce_vs_ssfsr, 1e-30, 1e30)
        print(f"\n  Bounce vs SSFSR:")
        print(f"    Median BF:           {np.median(bf2):.1e}")
        print(f"    P(BF > 100):         {np.mean(bf2 > 100)*100:.1f}%")
        print(f"    P(BF < 1):           {np.mean(bf2 < 1)*100:.1f}%")


if __name__ == "__main__":
    print("MOCK-BASED ESTIMATOR REALISM VALIDATION")
    print("100,000 synthetic power spectrum observations per survey")
    run_mock_ensemble(n_mocks=100000)
    print("\nDone.")
