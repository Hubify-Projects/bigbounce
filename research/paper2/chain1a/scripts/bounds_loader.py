"""
PBH constraint bounds loader.

Provides digitized monochromatic upper limits f^mono_{max}(M) from
the major constraint channels.  These are simplified but representative
curves based on the 2024-2026 constraint compilations:

  - Carr, Kohri, Sendouda, Yokoyama (2020)
  - Green & Kavanagh (2021)
  - Escriva, Bagui, Clesse (2025), arXiv:2601.06024

For a production run, replace with machine-readable tables from
PBHbounds (github.com/bradkav/PBHbounds) or PBHconstraints.

Each bound is returned as (log10_M_grams, log10_f_max) arrays.
"""

import numpy as np

# ---- Individual constraint channels ------------------------------------

def _evaporation_bound():
    """Hawking evaporation: extragalactic gamma-ray background.
    Constrains M < ~5e14 g (fully evaporated) and M ~ 5e14 - 1e17 g
    (evaporating now, producing gamma rays).
    """
    log_M = np.array([14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0])
    log_f = np.array([-99, -8.0, -6.0, -4.5, -3.5, -2.0, -1.0])
    return log_M, log_f, "Evaporation (gamma-ray)"


def _femtolensing_bound():
    """Femtolensing of gamma-ray bursts.
    Constrains M ~ 1e17 - 1e20 g.
    """
    log_M = np.array([17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0])
    log_f = np.array([-1.0, -0.5, -0.3, -0.15, -0.2, -0.3, -0.5])
    return log_M, log_f, "Femtolensing"


def _asteroid_window():
    """The asteroid-mass window: M ~ 1e20 - 1e24 g.
    This is the LEAST constrained region.  f_PBH ~ 1 is allowed.
    """
    log_M = np.array([20.0, 21.0, 22.0, 23.0, 24.0])
    log_f = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    return log_M, log_f, "Asteroid window (weak)"


def _hsc_microlensing():
    """HSC/Subaru microlensing.
    Constrains M ~ 1e22 - 1e28 g.
    """
    log_M = np.array([22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0])
    log_f = np.array([0.0, -0.5, -1.0, -1.3, -1.5, -1.3, -1.0])
    return log_M, log_f, "HSC microlensing"


def _eros_macho():
    """EROS/MACHO microlensing.
    Constrains M ~ 1e26 - 1e34 g.
    """
    log_M = np.array([26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0,
                       33.0, 34.0])
    log_f = np.array([-1.0, -1.5, -2.0, -1.8, -1.5, -1.3, -1.5,
                       -1.8, -1.5])
    return log_M, log_f, "EROS/MACHO"


def _cmb_accretion():
    """CMB accretion bounds (Ali-Haimoud & Kamionkowski, Serpico+).
    Constrains M ~ 1e33 - 1e38 g (1 - 10^5 M_sun).
    """
    log_M = np.array([33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0,
                       37.0, 38.0])
    log_f = np.array([-2.5, -3.0, -3.5, -4.0, -3.5, -3.0, -2.5,
                       -2.0, -1.5])
    return log_M, log_f, "CMB accretion"


def _dynamical():
    """Dynamical constraints: wide binaries, ultra-faint dwarfs,
    disk heating.  Constrains M > ~10^36 g.
    """
    log_M = np.array([36.0, 37.0, 38.0, 39.0, 40.0])
    log_f = np.array([-2.0, -1.5, -1.0, -1.0, -1.0])
    return log_M, log_f, "Dynamical"


# ---- Main interface ----------------------------------------------------

ALL_BOUNDS = [
    _evaporation_bound,
    _femtolensing_bound,
    _asteroid_window,
    _hsc_microlensing,
    _eros_macho,
    _cmb_accretion,
    _dynamical,
]


def load_all_bounds():
    """Return a list of (log10_M, log10_f_max, label) tuples."""
    return [fn() for fn in ALL_BOUNDS]


def envelope_bound(log10_M_query):
    """Compute the tightest monochromatic f_max at given masses.

    Parameters
    ----------
    log10_M_query : array, log10(M/gram) values

    Returns
    -------
    log10_f_max : array, tightest upper bound at each mass
    """
    bounds = load_all_bounds()
    result = np.zeros_like(log10_M_query)
    for i, lm in enumerate(log10_M_query):
        best = 0.0  # log10(f) = 0 means f = 1 (no constraint)
        for log_M, log_f, _ in bounds:
            if log_M[0] <= lm <= log_M[-1]:
                val = np.interp(lm, log_M, log_f)
                if val < best:
                    best = val
            # For masses below the lowest bound point, no constraint
        result[i] = best
    return result
