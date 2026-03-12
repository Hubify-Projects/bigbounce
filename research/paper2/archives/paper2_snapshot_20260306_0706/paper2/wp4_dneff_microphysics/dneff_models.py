#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WP4: Delta-Neff Microphysics Models
====================================

Two toy models for generating Delta-Neff ~ 0.1-0.2 from post-inflation physics:

  Model A: Dark radiation from reheating branching fraction
  Model B: Out-of-equilibrium heavy particle decay

Both models produce Delta-Neff as a function of their respective parameter
spaces, with built-in BBN and CMB constraint checks.

References:
  - Kolb & Turner, "The Early Universe" (1990), Chs. 3-5
  - Brust, Kaplan, Walters & Zurek (2013), arXiv:1303.5379
  - Yeh, Shelton, Olive & Fields (2022), arXiv:2204.11297
  - Planck 2018 VI: Aghanim et al. (2020), arXiv:1807.06209

Author: Houston Golden (2026)
"""

from __future__ import division, print_function
import numpy as np


# ===========================================================================
# Physical constants (natural units where relevant)
# ===========================================================================

# Standard Model effective relativistic degrees of freedom at high T
G_STAR_SM = 106.75  # above EW scale

# Reduced Planck mass in GeV
M_PL = 2.435e18  # GeV

# Standard Neff in SM (with QED corrections)
NEFF_SM = 3.044

# Constraint thresholds (see constraints.md for full citations)
DNEFF_BBN_MAX = 0.50    # Yeh+2022, 95% CL
DNEFF_CMB_MAX = 0.34    # Planck 2018, 2-sigma from zero
DNEFF_TARGET_LO = 0.10  # Paper 1 MCMC lower bound
DNEFF_TARGET_HI = 0.20  # Paper 1 MCMC upper bound


# ===========================================================================
# Model A: Dark Radiation from Reheating Branching
# ===========================================================================

class ReheatingModel(object):
    """
    Dark radiation produced during reheating via a branching fraction
    Br_dr of the inflaton decay products going into a hidden sector.

    The hidden sector has g_star_hidden relativistic degrees of freedom.
    After the hidden sector decouples from the visible sector (which happens
    at or near reheating), entropy conservation in each sector independently
    determines the temperature ratio at later times.

    Key equations (Kolb & Turner 1990, Ch. 3; Brust et al. 2013, Sec. 2):

    At reheating, if a fraction Br_dr of energy goes to the hidden sector:

        rho_dr / rho_vis = Br_dr / (1 - Br_dr)

    After reheating, both sectors cool adiabatically. The temperature ratio
    evolves as visible-sector particles annihilate and dump entropy into
    photons. At neutrino decoupling (T ~ 1 MeV), the visible sector has
    g_star_vis = 10.75 effective dof.

    The dark radiation temperature relative to the photon temperature at
    recombination is:

        (T_dr / T_gamma)^4 = (Br_dr / (1 - Br_dr))
                              * (g_star_vis(T_reh) / g_star_hidden)
                              * (g_star_hidden / g_star_vis(T_nu_dec))^(4/3)

    Simplification for the common case where the hidden sector was briefly
    in equilibrium at reheating then decoupled immediately:

        Delta-Neff = (4/7) * g_star_hidden * (T_dr/T_gamma)^4
                   * (11/4)^(4/3)

    In the regime Br_dr << 1 (small branching), this reduces to:

        Delta-Neff ~ Br_dr * (g_star_hidden / g_star_vis(T_reh))
                     * (g_star_vis(T_reh) / g_star_vis(T_nu_dec))^(4/3)
                     * (43/7) * (4/11)^(4/3) * g_star_hidden

    We implement the full (non-linearized) formula.

    Parameters
    ----------
    Br_dr : float or array
        Branching fraction of reheating energy to hidden sector, in (0, 1).
    g_star_hidden : float or array
        Effective relativistic dof in the hidden sector (>= 1).
    Treh : float
        Reheating temperature in GeV. Determines g_star_vis at reheating.
        Default: 1e9 GeV.
    """

    def __init__(self, Treh=1.0e9):
        """
        Initialize the reheating model.

        Parameters
        ----------
        Treh : float
            Reheating temperature in GeV. Used to determine g_star_vis
            at the reheating epoch. Default: 1e9 GeV (well above EW scale).
        """
        self.Treh = Treh
        self.g_star_vis_reh = self._g_star_visible(Treh)
        # At neutrino decoupling, T ~ 1 MeV
        self.g_star_vis_nu_dec = 10.75

    @staticmethod
    def _g_star_visible(T_GeV):
        """
        Approximate SM g_star as a function of temperature.

        Uses a simplified step function (Kolb & Turner 1990, Table 3.4):
          T > 300 GeV : 106.75 (full SM)
          T > 1 GeV   : 86.25  (above QCD transition)
          T > 0.1 GeV : 61.75  (below charm threshold)
          T > 0.001   : 10.75  (e, mu, nu's, photon)
          T < 0.001   : 3.36   (photon + neutrinos after e+e- annihilation)

        Parameters
        ----------
        T_GeV : float
            Temperature in GeV.

        Returns
        -------
        float
            Effective relativistic degrees of freedom.
        """
        if T_GeV > 300.0:
            return 106.75
        elif T_GeV > 1.0:
            return 86.25
        elif T_GeV > 0.1:
            return 61.75
        elif T_GeV > 1.0e-3:
            return 10.75
        else:
            return 3.36

    def compute_dneff(self, Br_dr, g_star_hidden):
        """
        Compute Delta-Neff from reheating branching fraction.

        The hidden sector receives a fraction Br_dr of the total reheating
        energy. After decoupling, entropy conservation in each sector
        independently determines the temperature evolution.

        The resulting contribution to Neff is (Brust et al. 2013, Eq. 2.5):

            Delta-Neff = (4/7) * (11/4)^(4/3) * g_star_hidden
                         * (T_dr / T_gamma)^4

        where the temperature ratio at recombination is:

            (T_dr/T_gamma)^4 = (Br_dr / (1 - Br_dr))
                               * (g_vis_reh / g_hidden)
                               * (g_hidden / g_vis_nu)^(4/3)

        This comes from:
        1. Energy partition at reheating: rho_dr/rho_vis = Br_dr/(1-Br_dr)
        2. T^4 ~ rho/g_star, so T_dr^4/T_vis^4 = (rho_dr/rho_vis)*(g_vis/g_dr)
        3. Subsequent cooling: visible sector g_star changes from g_vis_reh
           down to g_vis_nu as particles annihilate, heating photons relative
           to the already-decoupled hidden sector by factor
           (g_vis_reh/g_vis_nu)^(1/3) in temperature.

        Parameters
        ----------
        Br_dr : float or numpy.ndarray
            Branching fraction to hidden sector, in (0, 1). Values at or
            above 1.0 are clipped to 0.999 to avoid divergence.
        g_star_hidden : float or numpy.ndarray
            Hidden sector relativistic degrees of freedom (>= 1).

        Returns
        -------
        numpy.ndarray
            Delta-Neff values. Same shape as broadcast(Br_dr, g_star_hidden).
        """
        Br_dr = np.asarray(Br_dr, dtype=np.float64)
        g_star_hidden = np.asarray(g_star_hidden, dtype=np.float64)

        # Clip to avoid division by zero or unphysical values
        Br_dr = np.clip(Br_dr, 1.0e-20, 0.999)
        g_star_hidden = np.clip(g_star_hidden, 1.0, None)

        g_vis_reh = self.g_star_vis_reh
        g_vis_nu = self.g_star_vis_nu_dec

        # Energy ratio at reheating
        energy_ratio = Br_dr / (1.0 - Br_dr)

        # Temperature ratio T_dr/T_gamma at reheating
        # T^4 proportional to rho / g_star
        T_ratio_reh_4 = energy_ratio * (g_vis_reh / g_star_hidden)

        # Cooling factor: visible sector entropy dumps into photons as
        # particles annihilate, raising T_gamma relative to T_dr
        # T_gamma/T_dr grows by factor (g_vis_reh / g_vis_nu)^(1/3)
        # So (T_dr/T_gamma)^4 is suppressed by (g_vis_nu / g_vis_reh)^(4/3)
        cooling_factor = (g_vis_nu / g_vis_reh) ** (4.0 / 3.0)

        # Final temperature ratio at recombination
        T_ratio_4 = T_ratio_reh_4 * cooling_factor

        # Delta-Neff contribution
        # Each species of massless boson contributes 4/7 to Neff
        # relative to a single neutrino species, at the neutrino temperature.
        # The (11/4)^(4/3) factor converts from T_gamma to T_nu.
        prefactor = (4.0 / 7.0) * (11.0 / 4.0) ** (4.0 / 3.0)

        dneff = prefactor * g_star_hidden * T_ratio_4

        return dneff

    def allowed_bbn(self, dneff):
        """Check if Delta-Neff satisfies BBN constraint (Yeh+2022)."""
        return np.asarray(dneff) < DNEFF_BBN_MAX

    def allowed_cmb(self, dneff):
        """Check if Delta-Neff satisfies CMB constraint (Planck 2018)."""
        return np.asarray(dneff) < DNEFF_CMB_MAX

    def in_target(self, dneff):
        """Check if Delta-Neff is in the Paper 1 target range."""
        d = np.asarray(dneff)
        return (d >= DNEFF_TARGET_LO) & (d <= DNEFF_TARGET_HI)

    def allowed_and_target(self, dneff):
        """Check if Delta-Neff satisfies all constraints AND is in target range."""
        return self.allowed_bbn(dneff) & self.allowed_cmb(dneff) & self.in_target(dneff)


# ===========================================================================
# Model B: Out-of-Equilibrium Heavy Particle Decay
# ===========================================================================

class DecayModel(object):
    """
    Dark radiation produced by the out-of-equilibrium decay of a heavy
    particle X with mass m_X, lifetime tau_X, and initial abundance
    Y_X = n_X / s (number density per entropy density).

    A fraction Br_dark of each decay goes to dark radiation (massless
    hidden sector particles).

    The energy injected into dark radiation per unit entropy is:

        epsilon_dr / s = Br_dark * m_X * Y_X

    This energy density redshifts as radiation (a^-4) from the decay
    epoch to recombination. The conversion to Delta-Neff depends on
    whether the decay occurs before or after neutrino decoupling.

    Key relations (Brust et al. 2013, Sec. 3; Kolb & Turner 1990, Ch. 5):

    Decay temperature from lifetime:
        H(T_dec) = 1 / (2 * tau_X)
        T_dec ~ (90 / (8 * pi^3 * g_star))^(1/4) * sqrt(M_Pl / tau_X)

    Approximate scaling:
        T_dec ~ 1.3 MeV * (10.75 / g_star)^(1/4) * (1 sec / tau_X)^(1/2)

    If decay is before neutrino decoupling (T_dec > T_nu_dec ~ 1 MeV):
        The dark radiation thermalizes (or at least contributes to the
        radiation bath). Delta-Neff from energy injection into a decoupled
        dark sector:

        Delta-Neff = (120 / 7) * (11/4)^(4/3) * (rho_dr / rho_gamma)

        where rho_dr / rho_gamma = (Br_dark * m_X * Y_X * s) / rho_gamma
        evaluated at the appropriate epoch.

    If decay is after neutrino decoupling (T_dec < 1 MeV):
        The dark radiation does not thermalize with the photon bath.
        It contributes directly as a free-streaming component.

    Parameters
    ----------
    m_X : float or array
        Mass of decaying particle in GeV.
    tau_X : float or array
        Lifetime in seconds.
    Br_dark : float
        Branching fraction to dark radiation. Default: 1.0.
    Y_X : float
        Initial abundance n_X / s. Default: 1e-10.
    """

    # Neutrino decoupling temperature in GeV
    T_NU_DEC = 1.0e-3  # ~1 MeV

    def __init__(self):
        """Initialize the decay model."""
        pass

    @staticmethod
    def _g_star(T_GeV):
        """
        Approximate SM g_star as function of temperature (same as reheating model).

        Parameters
        ----------
        T_GeV : float or numpy.ndarray
            Temperature in GeV.

        Returns
        -------
        numpy.ndarray
            Effective relativistic degrees of freedom.
        """
        T_GeV = np.asarray(T_GeV, dtype=np.float64)
        g = np.full_like(T_GeV, 3.36)
        g = np.where(T_GeV > 1.0e-3, 10.75, g)
        g = np.where(T_GeV > 0.1, 61.75, g)
        g = np.where(T_GeV > 1.0, 86.25, g)
        g = np.where(T_GeV > 300.0, 106.75, g)
        return g

    @staticmethod
    def decay_temperature(tau_X):
        """
        Compute the decay temperature from the particle lifetime.

        From H(T) = 1/(2*tau_X) in a radiation-dominated universe:

            H^2 = (8*pi^3 * g_star / 90) * T^4 / M_Pl^2

        Solving for T:

            T_dec = (90 / (8*pi^3 * g_star))^(1/4) * sqrt(M_Pl / tau_X)
                  ~ 1.3 MeV * (10.75/g_star)^(1/4) * (1s / tau_X)^(1/2)

        We iterate once to self-consistently determine g_star(T_dec).

        Parameters
        ----------
        tau_X : float or numpy.ndarray
            Lifetime in seconds. Converted to GeV^-1 internally.

        Returns
        -------
        numpy.ndarray
            Decay temperature in GeV.
        """
        tau_X = np.asarray(tau_X, dtype=np.float64)

        # Convert seconds to GeV^-1: 1 sec = 1.519e24 GeV^-1
        tau_gev = tau_X * 1.519e24

        # First pass with g_star = 10.75 (typical for MeV-scale decays)
        g_star_init = 10.75
        coeff = (90.0 / (8.0 * np.pi**3 * g_star_init)) ** 0.25
        T_dec = coeff * np.sqrt(M_PL / tau_gev)

        # Second pass: update g_star
        g_star = DecayModel._g_star(T_dec)
        coeff = (90.0 / (8.0 * np.pi**3 * g_star)) ** 0.25
        T_dec = coeff * np.sqrt(M_PL / tau_gev)

        return T_dec

    def compute_dneff(self, m_X, tau_X, Br_dark=1.0, Y_X=1.0e-10):
        """
        Compute Delta-Neff from heavy particle decay.

        The energy density in dark radiation from the decay is:

            rho_dr = Br_dark * m_X * Y_X * s(T_dec)

        where s(T) = (2*pi^2/45) * g_star_s * T^3 is the entropy density.

        The photon energy density at decay is:

            rho_gamma = (pi^2/15) * T_dec^4

        (using g_gamma = 2 for photon dof).

        The ratio rho_dr/rho_gamma at the decay epoch is:

            rho_dr/rho_gamma = Br_dark * m_X * Y_X * (2*pi^2/45) * g_s * T^3
                               / ((pi^2/15) * T^4)
                             = Br_dark * m_X * Y_X * (2/3) * g_s / T_dec

        Then Delta-Neff is:

            Delta-Neff = (120/7) * (11/4)^(4/3) * (rho_dr / rho_gamma)
                         * dilution_factor

        The dilution_factor accounts for subsequent e+e- annihilation
        (which heats photons but not the dark radiation):
          - If T_dec > T_nu_dec: dilution from g_star(T_dec) to g_star(T_rec)
          - If T_dec < T_nu_dec: no additional dilution (dark sector already
            decoupled from photon bath)

        For decays well before neutrino decoupling (T_dec >> 1 MeV), the
        visible sector heating from e+e- annihilation dilutes the DR
        relative to photons by:

            dilution = (g_star_s(T_nu_dec) / g_star_s(T_dec))^(4/3)

        Parameters
        ----------
        m_X : float or numpy.ndarray
            Mass of X in GeV.
        tau_X : float or numpy.ndarray
            Lifetime in seconds.
        Br_dark : float or numpy.ndarray
            Branching fraction to dark radiation. Default: 1.0.
        Y_X : float or numpy.ndarray
            Initial abundance n_X/s. Default: 1e-10.

        Returns
        -------
        numpy.ndarray
            Delta-Neff values.
        """
        m_X = np.asarray(m_X, dtype=np.float64)
        tau_X = np.asarray(tau_X, dtype=np.float64)
        Br_dark = np.asarray(Br_dark, dtype=np.float64)
        Y_X = np.asarray(Y_X, dtype=np.float64)

        # Decay temperature
        T_dec = self.decay_temperature(tau_X)

        # g_star at decay
        g_star_dec = self._g_star(T_dec)

        # g_star_s ~ g_star for T > 1 MeV (good approximation)
        g_s_dec = g_star_dec

        # Energy density ratio at decay epoch
        # rho_dr / rho_gamma = Br_dark * m_X * Y_X * (2/3) * g_s / T_dec
        rho_ratio = Br_dark * m_X * Y_X * (2.0 / 3.0) * g_s_dec / T_dec

        # Dilution factor from visible sector reheating after decay
        # For T_dec > T_nu_dec: photons are heated by e+e- annihilation
        #   relative to the (already injected) dark radiation
        # The dark radiation temperature ratio to photons decreases by
        #   (g_s(T_nu_dec) / g_s(T_dec))^(1/3) in temperature,
        #   so (...)^(4/3) in energy density ratio
        g_s_nu_dec = 10.75
        dilution = np.where(
            T_dec > self.T_NU_DEC,
            (g_s_nu_dec / g_s_dec) ** (4.0 / 3.0),
            1.0  # No dilution for late decays
        )

        # Convert rho_dr/rho_gamma to Delta-Neff
        # Neff is defined relative to the neutrino energy density:
        #   rho_nu = (7/8) * (4/11)^(4/3) * rho_gamma per species
        # So rho_dr / rho_gamma = Delta-Neff * (7/8) * (4/11)^(4/3)
        # => Delta-Neff = rho_dr/rho_gamma * (8/7) * (11/4)^(4/3)
        # But we need the ratio at recombination, not at decay:
        # (rho_dr/rho_gamma)_rec = (rho_dr/rho_gamma)_dec * dilution
        prefactor = (8.0 / 7.0) * (11.0 / 4.0) ** (4.0 / 3.0)

        dneff = prefactor * rho_ratio * dilution

        return dneff

    def allowed_bbn(self, dneff):
        """Check if Delta-Neff satisfies BBN constraint (Yeh+2022)."""
        return np.asarray(dneff) < DNEFF_BBN_MAX

    def allowed_cmb(self, dneff):
        """Check if Delta-Neff satisfies CMB constraint (Planck 2018)."""
        return np.asarray(dneff) < DNEFF_CMB_MAX

    def in_target(self, dneff):
        """Check if Delta-Neff is in the Paper 1 target range."""
        d = np.asarray(dneff)
        return (d >= DNEFF_TARGET_LO) & (d <= DNEFF_TARGET_HI)

    def allowed_and_target(self, dneff):
        """Check if Delta-Neff satisfies all constraints AND is in target range."""
        return self.allowed_bbn(dneff) & self.allowed_cmb(dneff) & self.in_target(dneff)


# ===========================================================================
# Convenience / testing
# ===========================================================================

def print_model_summary():
    """Print a quick summary of both models at representative parameter values."""
    print("=" * 70)
    print("WP4 Delta-Neff Microphysics — Model Summary")
    print("=" * 70)

    # Model A: Reheating
    print("\n--- Model A: Reheating Branching ---")
    model_a = ReheatingModel(Treh=1.0e9)
    test_cases_a = [
        (1.0e-3, 1.0),
        (1.0e-3, 10.0),
        (1.0e-2, 1.0),
        (1.0e-2, 10.0),
        (0.1, 1.0),
        (0.01, 5.0),
    ]
    print("  {:<12s} {:<16s} {:<12s} {:<8s} {:<8s}".format(
        "Br_dr", "g_star_hidden", "Delta-Neff", "BBN OK", "CMB OK"
    ))
    for Br_dr, g_h in test_cases_a:
        dn = model_a.compute_dneff(Br_dr, g_h)
        bbn = model_a.allowed_bbn(dn)
        cmb = model_a.allowed_cmb(dn)
        print("  {:<12.1e} {:<16.1f} {:<12.4f} {:<8s} {:<8s}".format(
            Br_dr, g_h, float(dn), str(bool(bbn)), str(bool(cmb))
        ))

    # Model B: Decay
    print("\n--- Model B: Heavy Particle Decay ---")
    model_b = DecayModel()
    test_cases_b = [
        (1.0e6, 1.0e-2, 1.0, 1.0e-10),
        (1.0e6, 1.0, 1.0, 1.0e-10),
        (1.0e9, 1.0e-4, 1.0, 1.0e-10),
        (1.0e9, 1.0, 1.0, 1.0e-10),
        (1.0e3, 1.0e2, 0.5, 1.0e-8),
        (1.0e6, 1.0e-2, 0.1, 1.0e-9),
    ]
    print("  {:<12s} {:<12s} {:<10s} {:<12s} {:<12s} {:<8s} {:<8s}".format(
        "m_X [GeV]", "tau_X [s]", "Br_dark", "Y_X", "Delta-Neff", "BBN OK", "CMB OK"
    ))
    for m_X, tau_X, Br_dark, Y_X in test_cases_b:
        dn = model_b.compute_dneff(m_X, tau_X, Br_dark, Y_X)
        bbn = model_b.allowed_bbn(dn)
        cmb = model_b.allowed_cmb(dn)
        print("  {:<12.1e} {:<12.1e} {:<10.2f} {:<12.1e} {:<12.4f} {:<8s} {:<8s}".format(
            m_X, tau_X, Br_dark, Y_X, float(dn), str(bool(bbn)), str(bool(cmb))
        ))

    print("\nConstraint thresholds:")
    print("  BBN (Yeh+2022):     Delta-Neff < {:.2f} (95%% CL)".format(DNEFF_BBN_MAX))
    print("  CMB (Planck 2018):  Delta-Neff < {:.2f} (2-sigma)".format(DNEFF_CMB_MAX))
    print("  Paper 1 target:     {:.2f} <= Delta-Neff <= {:.2f}".format(
        DNEFF_TARGET_LO, DNEFF_TARGET_HI))


if __name__ == "__main__":
    print_model_summary()
