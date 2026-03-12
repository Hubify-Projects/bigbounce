"""
parity_bias_model.py — Parity-odd bias extension to TTT
========================================================

Extends the standard Tidal Torque Theory with a parity-odd correction
term that breaks the CW/CCW symmetry along a preferred direction
(the "bounce axis" in the BigBounce framework).

Formalism:
  Start from TTT:
    L_i = epsilon_{ijk} T_{jl} I_{lk}                              [Eq. 2]

  Add a parity-odd correction:
    L -> L + epsilon_PO * (n_hat . L) * (n_hat x L)                [Eq. 7]

  where:
    n_hat     = preferred direction (bounce axis)
    epsilon_PO = dimensionless parity-odd coupling parameter

  This breaks the CW/CCW symmetry along n_hat. The handedness
  probability becomes angle-dependent:

    P(CW | theta) = 0.5 + epsilon_PO * f(theta, lambda, delta_rms) [Eq. 8]

  where theta is the viewing angle relative to n_hat and f is a
  geometric coupling factor.

  The dipole amplitude, averaged over a galaxy sample:

    A_0 = epsilon_PO * <|cos theta|> * g(lambda_mean, delta_rms)   [Eq. 9]

  where g encapsulates the TTT-level spin response:

    g ~ (2/3) * lambda_mean / delta_rms                            [Eq. 10]

  And <|cos theta|> = 2/pi for uniform viewing angles.

  Therefore:
    A_0 ~ epsilon_PO * (2/3) * lambda / delta_rms * (2/pi)
        ~ epsilon_PO * 0.015   (for standard parameters)           [Eq. 11]

  For the observed A_0 ~ 0.003 (Shamir 2024):
    epsilon_PO ~ 0.003 / 0.015 ~ 0.2                              [Eq. 12]

References:
  - White (1984), ApJ 286, 38
  - Porciani, Dekel & Hoffman (2002), MNRAS 332, 325
  - Shamir (2024), Asymmetry between galaxy spin directions
"""

import numpy as np
from scipy import stats


class ParityBiasModel(object):
    """
    Parity-odd extension to TTT for galaxy spin handedness.

    The model adds a coupling epsilon_PO that generates a preferred
    handedness along a direction n_hat (the "bounce axis").

    Parameters
    ----------
    epsilon_PO : float
        Dimensionless parity-odd coupling parameter.
        Range of interest: [0.01, 1.0].
    n_hat : array-like, shape (3,)
        Preferred direction unit vector (bounce axis).
    lambda_mean : float
        Mean spin parameter. Default: 0.035 (TTT standard).
    sigma_lnlambda : float
        Log-normal width of spin distribution. Default: 0.5.
    delta_rms : float
        RMS overdensity of halo formation environment. Default: 1.0.
        Controls the tidal field strength normalization.
    """

    def __init__(self, epsilon_PO, n_hat, lambda_mean=0.035,
                 sigma_lnlambda=0.5, delta_rms=1.0):
        self.epsilon_PO = epsilon_PO
        self.n_hat = np.array(n_hat, dtype=float)
        self.n_hat = self.n_hat / np.linalg.norm(self.n_hat)
        self.lambda_mean = lambda_mean
        self.sigma_lnlambda = sigma_lnlambda
        self.delta_rms = delta_rms

    def _geometric_factor_g(self):
        """
        Compute the geometric coupling factor g [Eq. 10].

        g ~ (2/3) * lambda_mean / delta_rms

        This factor encapsulates how efficiently the parity-odd
        correction in the tidal torque translates into a net
        handedness signal. The (2/3) arises from angular averaging
        of the tidal tensor eigenvalue ratios in the TTT framework.

        Returns
        -------
        g : float
            Geometric coupling factor.
        """
        return (2.0 / 3.0) * self.lambda_mean / self.delta_rms

    def _mean_abs_cos_theta(self):
        """
        Mean absolute cosine for uniform viewing angle distribution.

        <|cos theta|> = integral_0^pi |cos theta| sin theta d(theta) / 2
                      = 2/pi ~ 0.6366

        This is the angular dilution factor: only the component of
        the spin axis projected along the line of sight contributes
        to the apparent CW/CCW classification.

        Returns
        -------
        mean_abs_cos : float
        """
        return 2.0 / np.pi

    def handedness_probability(self, theta):
        """
        Probability of CW rotation as a function of viewing angle [Eq. 8].

        P(CW | theta) = 0.5 + epsilon_PO * f(theta, lambda, delta_rms)

        where f(theta) = |cos theta| * g captures the projection
        of the parity-odd bias along the line of sight.

        We clip the result to [0, 1] for physical validity
        (large epsilon_PO may violate this in the toy model).

        Parameters
        ----------
        theta : float or ndarray
            Viewing angle relative to n_hat, in radians.

        Returns
        -------
        p_cw : float or ndarray
            Probability of clockwise rotation.
        """
        theta = np.atleast_1d(np.array(theta, dtype=float))
        g = self._geometric_factor_g()
        f_theta = np.abs(np.cos(theta)) * g
        p_cw = 0.5 + self.epsilon_PO * f_theta
        p_cw = np.clip(p_cw, 0.0, 1.0)
        if p_cw.size == 1:
            return float(p_cw[0])
        return p_cw

    def dipole_amplitude(self):
        """
        Compute the galaxy spin dipole amplitude A_0 [Eq. 11].

        A_0 = epsilon_PO * <|cos theta|> * g(lambda_mean, delta_rms)
            = epsilon_PO * (2/pi) * (2/3) * lambda_mean / delta_rms

        Returns
        -------
        A0 : float
            Dipole amplitude.
        """
        g = self._geometric_factor_g()
        mean_cos = self._mean_abs_cos_theta()
        A0 = self.epsilon_PO * mean_cos * g
        return A0

    def dipole_amplitude_uncertainty(self):
        """
        Estimate uncertainty on A_0 from scatter in spin parameter.

        The dominant source of uncertainty is the scatter in lambda.
        Since A_0 ~ epsilon_PO * lambda, the fractional uncertainty is:

            sigma(A_0) / A_0 ~ sigma(lambda) / lambda_mean

        For the log-normal distribution:
            sigma(lambda) / lambda_mean = sqrt(exp(sigma_ln^2) - 1)

        This is a statistical uncertainty on the population-averaged
        A_0, not the uncertainty on any individual galaxy.

        Returns
        -------
        sigma_A0 : float
            1-sigma uncertainty on the dipole amplitude.
        """
        # Fractional scatter in lambda for log-normal
        frac_scatter = np.sqrt(np.exp(self.sigma_lnlambda**2) - 1.0)
        A0 = self.dipole_amplitude()
        sigma_A0 = A0 * frac_scatter
        return sigma_A0

    def required_epsilon(self, A0_target=0.003):
        """
        Invert the scaling to find epsilon_PO needed for a target A_0 [Eq. 12].

        epsilon_PO = A0_target / (<|cos theta|> * g)

        Parameters
        ----------
        A0_target : float
            Target dipole amplitude. Default: 0.003 (Shamir 2024).

        Returns
        -------
        eps_required : float
            Required epsilon_PO value.
        """
        g = self._geometric_factor_g()
        mean_cos = self._mean_abs_cos_theta()
        denominator = mean_cos * g
        if denominator == 0:
            return np.inf
        return A0_target / denominator

    def scaling_curve(self, epsilon_range):
        """
        Compute A_0(epsilon_PO) scaling curve with uncertainties [Eq. 11].

        Parameters
        ----------
        epsilon_range : array-like
            Array of epsilon_PO values to evaluate.

        Returns
        -------
        eps_arr : ndarray
            Input epsilon_PO values.
        A0_arr : ndarray
            Corresponding dipole amplitudes.
        sigma_A0_arr : ndarray
            1-sigma uncertainties on A_0.
        """
        epsilon_range = np.atleast_1d(np.array(epsilon_range, dtype=float))
        g = self._geometric_factor_g()
        mean_cos = self._mean_abs_cos_theta()
        frac_scatter = np.sqrt(np.exp(self.sigma_lnlambda**2) - 1.0)

        A0_arr = epsilon_range * mean_cos * g
        sigma_A0_arr = A0_arr * frac_scatter

        return epsilon_range, A0_arr, sigma_A0_arr

    def summary(self):
        """Print a summary of the parity-odd model predictions."""
        g = self._geometric_factor_g()
        mean_cos = self._mean_abs_cos_theta()
        A0 = self.dipole_amplitude()
        sigma_A0 = self.dipole_amplitude_uncertainty()
        eps_req = self.required_epsilon(0.003)

        lines = [
            "=" * 60,
            "Parity-Odd TTT Extension — Predictions",
            "=" * 60,
            "Input parameters:",
            "  epsilon_PO = %.4f" % self.epsilon_PO,
            "  n_hat = [%.3f, %.3f, %.3f]" % tuple(self.n_hat),
            "  lambda_mean = %.4f" % self.lambda_mean,
            "  sigma_ln(lambda) = %.2f" % self.sigma_lnlambda,
            "  delta_rms = %.2f" % self.delta_rms,
            "",
            "Derived quantities:",
            "  g = (2/3) * lambda / delta_rms = %.5f" % g,
            "  <|cos theta|> = 2/pi = %.5f" % mean_cos,
            "  Scaling coefficient = g * <|cos theta|> = %.5f" % (g * mean_cos),
            "",
            "Predictions:",
            "  A_0 = %.6f +/- %.6f" % (A0, sigma_A0),
            "  P(CW, theta=0) = %.4f" % self.handedness_probability(0.0),
            "  P(CW, theta=pi/2) = %.4f" % self.handedness_probability(np.pi / 2),
            "",
            "Inversion:",
            "  For A_0 = 0.003: epsilon_PO = %.4f" % eps_req,
            "=" * 60,
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    # ---- Self-test and demonstration ----
    print("Running parity bias model self-test...\n")

    # Fiducial model: epsilon_PO = 0.2, bounce axis along z
    model = ParityBiasModel(
        epsilon_PO=0.2,
        n_hat=[0.0, 0.0, 1.0],
        lambda_mean=0.035,
        sigma_lnlambda=0.5,
        delta_rms=1.0
    )

    print(model.summary())

    # Verify the key scaling relation
    A0 = model.dipole_amplitude()
    expected = 0.2 * (2.0 / 3.0) * 0.035 / 1.0 * (2.0 / np.pi)
    print("\nScaling verification:")
    print("  A_0 (computed)  = %.6f" % A0)
    print("  A_0 (expected)  = %.6f" % expected)
    assert abs(A0 - expected) < 1e-10, "Scaling mismatch!"
    print("  PASSED")

    # Verify inversion
    eps_req = model.required_epsilon(0.003)
    print("\nInversion verification:")
    print("  Required epsilon_PO for A_0=0.003: %.4f" % eps_req)
    model_check = ParityBiasModel(eps_req, [0, 0, 1])
    A0_check = model_check.dipole_amplitude()
    print("  Check: A_0(eps_req) = %.6f (should be ~0.003)" % A0_check)
    assert abs(A0_check - 0.003) < 1e-6, "Inversion mismatch!"
    print("  PASSED")

    # Handedness probability profile
    print("\nHandedness probability vs viewing angle:")
    theta_arr = np.linspace(0, np.pi, 7)
    for theta in theta_arr:
        p = model.handedness_probability(theta)
        print("  theta = %.2f rad (%.1f deg)  ->  P(CW) = %.4f" % (
            theta, np.degrees(theta), p))

    # Scaling curve
    eps_range = np.logspace(-2, 0, 50)
    eps_out, A0_out, sig_out = model.scaling_curve(eps_range)
    print("\nScaling curve (selected points):")
    for i in range(0, len(eps_out), 10):
        print("  eps_PO = %.3f  ->  A_0 = %.5f +/- %.5f" % (
            eps_out[i], A0_out[i], sig_out[i]))

    print("\nAll tests passed.")
