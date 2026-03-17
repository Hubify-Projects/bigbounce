"""
Cobaya Theory class for spectator ALP birefringence.

Wraps alp_ode.py to provide the predicted birefringence angle beta
to the likelihood module.

Model 2: LCDM + spectator ALP (ALP does not affect background).
"""

import numpy as np
from cobaya.theory import Theory
from alp_ode import compute_alp_birefringence, M_PL_EV


class ALPBirefringence(Theory):
    """
    Spectator ALP birefringence theory for Cobaya.

    Sampled parameters:
        theta_i     : initial misalignment angle (rad)
        log10_m_eV  : log10(m_a / eV)

    Fixed parameters (set in YAML or here):
        f_a_eV      : decay constant in eV (default: M_Pl)
        C_agamma    : anomaly coefficient (default: 8)
        Omega_m     : matter density (default: 0.315)

    Provides derived quantities:
        beta_deg, eta, Omega_a, w_a_0
    """

    # Fixed parameters with defaults
    f_a_eV: float = M_PL_EV
    C_agamma: float = 8.0
    Omega_m: float = 0.315

    def initialize(self):
        self.log.info(
            f"ALPBirefringence initialized: f_a={self.f_a_eV:.3e} eV, "
            f"C_agamma={self.C_agamma}, Omega_m={self.Omega_m}"
        )

    # Declare input parameters this theory uses
    # C_agamma can be sampled or fixed via the class attribute above
    input_params_defaults = {'theta_i': None, 'log10_m_eV': None}

    def get_requirements(self):
        return {}

    def must_provide(self, **requirements):
        return {}

    def get_can_support_params(self):
        return ['theta_i', 'log10_m_eV', 'C_agamma']

    def get_can_provide_params(self):
        return ['beta_deg', 'eta', 'Omega_a', 'w_a_0']

    def get_can_provide(self):
        return ['beta_deg']

    def calculate(self, state, want_derived=True, **params_values):
        theta_i = params_values.get('theta_i')
        log10_m_eV = params_values.get('log10_m_eV')
        # Use sampled C_agamma if provided, otherwise fall back to fixed value
        C_agamma = params_values.get('C_agamma', self.C_agamma)

        if theta_i is None or log10_m_eV is None:
            raise ValueError(
                f"Missing required parameters. Got theta_i={theta_i}, "
                f"log10_m_eV={log10_m_eV}"
            )

        try:
            result = compute_alp_birefringence(
                theta_i=theta_i,
                log10_m_eV=log10_m_eV,
                f_a_eV=self.f_a_eV,
                C_agamma=C_agamma,
                Omega_m=self.Omega_m,
            )
        except RuntimeError as e:
            self.log.warning(f"ODE integration failed: {e}")
            return False

        state['beta_deg'] = result['beta_deg']
        state['eta'] = result['eta']
        state['Omega_a'] = result['Omega_a']
        state['w_a_0'] = result['w_a_0']
        state['derived'] = {
            'beta_deg': result['beta_deg'],
            'eta': result['eta'],
            'Omega_a': result['Omega_a'],
            'w_a_0': result['w_a_0'],
        }
        return True

    def get_beta_deg(self):
        return self.current_state['beta_deg']
