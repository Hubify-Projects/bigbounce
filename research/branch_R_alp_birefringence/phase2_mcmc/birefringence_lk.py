"""
Cobaya Likelihood class for cosmic birefringence measurement.

Simple Gaussian likelihood on the observed birefringence angle:
    log L = -0.5 * ((beta_pred - beta_obs) / sigma_beta)^2

Data:
    beta_obs  = 0.342 deg  (Eskilt et al. 2025, Planck PR4 + ACT DR6 combined)
    sigma     = 0.094 deg  (1-sigma statistical + systematic)
"""

import numpy as np
from cobaya.likelihood import Likelihood


class BirefringenceLikelihood(Likelihood):
    """
    Gaussian likelihood for isotropic cosmic birefringence.

    Requires the theory provider to supply 'beta_deg'.
    """

    # Observed values (can be overridden in YAML)
    beta_obs: float = 0.342   # degrees
    sigma_beta: float = 0.094  # degrees

    def initialize(self):
        self.log.info(
            f"BirefringenceLikelihood: beta_obs={self.beta_obs} +/- "
            f"{self.sigma_beta} deg"
        )

    def get_requirements(self):
        return {'beta_deg': None}

    def logp(self, **params_values):
        beta_pred = self.provider.get_param('beta_deg')
        chi2 = ((beta_pred - self.beta_obs) / self.sigma_beta) ** 2
        return -0.5 * chi2
