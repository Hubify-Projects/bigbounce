"""
ALP background ODE solver for spectator birefringence model.

Integrates the homogeneous ALP equation of motion on an LCDM background:
    theta'' + 3 H(t) theta' + m^2 sin(theta) = 0
where theta = phi / f_a is the dimensionless misalignment angle.

The cosmic birefringence angle is:
    beta = (C_{agamma} * alpha_em / (4 pi)) * [theta(z_rec) - theta(z=0)]

Units: natural units (hbar = c = 1) with masses in eV throughout.
"""

import numpy as np
from scipy.integrate import solve_ivp

# Physical constants (natural units, masses in eV)
ALPHA_EM = 1.0 / 137.036  # fine structure constant
M_PL_GEV = 2.435e18       # reduced Planck mass in GeV
M_PL_EV = M_PL_GEV * 1e9  # reduced Planck mass in eV
H0_EV = 1.44e-33           # H_0 = 67.36 km/s/Mpc in eV (hbar=c=1)
Z_REC = 1089.8              # redshift of recombination

# Conversion
EV_TO_INV_SEC = 1.519e15   # 1 eV = 1.519e15 s^{-1} in natural units
SEC_TO_INV_EV = 1.0 / EV_TO_INV_SEC


def hubble_lcdm(z, H0_eV=H0_EV, Omega_m=0.315):
    """LCDM Hubble parameter H(z) in eV."""
    Omega_L = 1.0 - Omega_m
    return H0_eV * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


def _ode_rhs_lna(ln_a, y, m_eV, H0_eV, Omega_m):
    """
    RHS of the ALP EOM in terms of ln(a) as the independent variable.

    Using ln(a) instead of cosmic time avoids numerical stiffness from
    the huge dynamic range in time between z=3000 and z=0.

    Variables:
        y[0] = theta            (dimensionless angle)
        y[1] = d(theta)/d(ln a) (= theta_dot / H)

    The EOM theta'' + 3H theta' + m^2 sin(theta) = 0 becomes:
        d(theta)/d(ln a) = theta_dot / H
        d(theta_dot/H)/d(ln a) = -(3 + H'/H) * (theta_dot/H) - (m/H)^2 sin(theta)

    where H'/H = d(ln H)/d(ln a).
    """
    theta, dtheta_dlna = y

    a = np.exp(ln_a)
    z = 1.0 / a - 1.0

    Omega_L = 1.0 - Omega_m
    E2 = Omega_m * (1 + z)**3 + Omega_L  # (H/H0)^2
    H = H0_eV * np.sqrt(E2)

    # d(ln H)/d(ln a) = -3 Omega_m (1+z)^3 / (2 E^2)
    dlnH_dlna = -1.5 * Omega_m * (1 + z)**3 / E2

    # (m/H)^2
    m_over_H_sq = (m_eV / H)**2

    # EOM in ln(a) coordinates
    d2theta_dlna2 = -(3.0 + dlnH_dlna) * dtheta_dlna - m_over_H_sq * np.sin(theta)

    return [dtheta_dlna, d2theta_dlna2]


def compute_alp_birefringence(theta_i, log10_m_eV, f_a_eV=M_PL_EV,
                               C_agamma=8.0, Omega_m=0.315,
                               H0_eV=H0_EV):
    """
    Compute the cosmic birefringence angle for a spectator ALP.

    Parameters
    ----------
    theta_i : float
        Initial misalignment angle (radians, typically 0 < theta_i < pi).
    log10_m_eV : float
        log10 of the ALP mass in eV.
    f_a_eV : float
        ALP decay constant in eV (default: M_Pl).
    C_agamma : float
        Anomaly coefficient (default: 8 for SM).
    Omega_m : float
        Matter density parameter (default: 0.315).
    H0_eV : float
        Hubble constant in eV (default: 1.44e-33 eV).

    Returns
    -------
    dict with keys:
        'beta_deg' : birefringence angle in degrees
        'beta_rad' : birefringence angle in radians
        'eta'      : rolling efficiency (theta_rec - theta_0) / theta_i
        'theta_rec': field value at recombination
        'theta_0'  : field value today
        'Omega_a'  : ALP energy density fraction today
        'w_a_0'    : ALP equation of state today
    """
    m_eV = 10.0**log10_m_eV

    # Integration range in ln(a): from z_init=3000 to z=0
    z_init = 3000.0
    ln_a_start = -np.log(1 + z_init)
    ln_a_end = 0.0  # z=0
    ln_a_rec = -np.log(1 + Z_REC)

    # Initial conditions: field frozen at theta_i, zero velocity
    y0 = [theta_i, 0.0]

    # Solve with dense output for interpolation at z_rec
    sol = solve_ivp(
        _ode_rhs_lna,
        [ln_a_start, ln_a_end],
        y0,
        args=(m_eV, H0_eV, Omega_m),
        method='DOP853',
        rtol=1e-10,
        atol=1e-12,
        dense_output=True,
        max_step=0.05,  # ~5% steps in scale factor
    )

    if not sol.success:
        raise RuntimeError(f"ODE integration failed: {sol.message}")

    # Extract field values at recombination and today
    y_rec = sol.sol(ln_a_rec)
    y_0 = sol.sol(ln_a_end)

    theta_rec = y_rec[0]
    theta_0 = y_0[0]
    dtheta_dlna_0 = y_0[1]

    # Rolling efficiency
    delta_theta = theta_rec - theta_0
    eta = delta_theta / theta_i if abs(theta_i) > 1e-30 else 0.0

    # Birefringence angle
    beta_rad = C_agamma * ALPHA_EM * delta_theta / (4.0 * np.pi)
    beta_deg = np.degrees(beta_rad)

    # ALP energy density today
    H0 = H0_eV
    theta_dot_0 = dtheta_dlna_0 * H0  # theta_dot = (dtheta/dlna) * H
    KE = 0.5 * f_a_eV**2 * theta_dot_0**2
    PE = m_eV**2 * f_a_eV**2 * (1.0 - np.cos(theta_0))
    rho_a = KE + PE

    # Critical density: rho_crit = 3 H0^2 M_Pl^2
    rho_crit = 3.0 * H0**2 * M_PL_EV**2
    Omega_a = rho_a / rho_crit if rho_crit > 0 else 0.0

    # Equation of state
    w_a_0 = (KE - PE) / (KE + PE) if (KE + PE) > 0 else -1.0

    return {
        'beta_deg': beta_deg,
        'beta_rad': beta_rad,
        'eta': eta,
        'theta_rec': theta_rec,
        'theta_0': theta_0,
        'delta_theta': delta_theta,
        'Omega_a': Omega_a,
        'w_a_0': w_a_0,
    }


if __name__ == '__main__':
    # Quick validation
    print("=== ALP ODE Solver Validation ===\n")

    # Test 1: Large mass (m >> H0), full rolling
    r = compute_alp_birefringence(1.0, -30.0)
    print(f"m >> H0 (log10_m=-30): beta={r['beta_deg']:.4f} deg, eta={r['eta']:.4f}")
    print(f"  Expected: beta ~ 0.27 deg, eta ~ 1.0")

    # Test 2: Small mass (m << H0), frozen
    r = compute_alp_birefringence(1.0, -36.0)
    print(f"\nm << H0 (log10_m=-36): beta={r['beta_deg']:.6f} deg, eta={r['eta']:.6f}")
    print(f"  Expected: beta ~ 0, eta ~ 0")

    # Test 3: m ~ H0
    r = compute_alp_birefringence(1.0, -33.0)
    print(f"\nm ~ H0 (log10_m=-33): beta={r['beta_deg']:.4f} deg, eta={r['eta']:.4f}")
    print(f"  Omega_a={r['Omega_a']:.4f}, w_a={r['w_a_0']:.4f}")

    # Test 4: theta_i = 1.3 with full rolling
    r = compute_alp_birefringence(1.3, -30.0)
    print(f"\ntheta_i=1.3, m>>H0: beta={r['beta_deg']:.4f} deg, eta={r['eta']:.4f}")
    print(f"  Expected: beta ~ 0.35 deg")

    # Test 5: Scaling with theta_i
    print("\nScaling with theta_i (m>>H0, log10_m=-30):")
    for ti in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        r = compute_alp_birefringence(ti, -30.0)
        print(f"  theta_i={ti:.1f}: beta={r['beta_deg']:.4f} deg, eta={r['eta']:.4f}")

    # Test 6: Mass scan
    print("\nMass scan (theta_i=1.0):")
    for lm in [-36, -35, -34, -33.5, -33, -32.5, -32, -31, -30]:
        r = compute_alp_birefringence(1.0, lm)
        print(f"  log10_m={lm:6.1f}: beta={r['beta_deg']:.5f} deg, "
              f"eta={r['eta']:.5f}, Omega_a={r['Omega_a']:.2e}, w={r['w_a_0']:.3f}")

    # Timing
    import time
    t0 = time.perf_counter()
    for _ in range(100):
        compute_alp_birefringence(1.0, -32.5)
    dt = (time.perf_counter() - t0) / 100
    print(f"\nTiming: {dt*1000:.1f} ms per evaluation")
