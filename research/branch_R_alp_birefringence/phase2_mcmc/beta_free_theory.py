"""
Trivial Cobaya Theory class for the baseline beta-free model.

The birefringence angle beta is a direct sampled parameter with no
underlying physics model. This serves as the null comparison for
the ALP model.
"""

from cobaya.theory import Theory


class BetaFreeTheory(Theory):
    """Passes the sampled beta_deg directly to the likelihood."""

    input_params_defaults = {'beta_deg': None}

    def get_can_support_params(self):
        return ['beta_deg']

    def get_can_provide_params(self):
        return []

    def get_can_provide(self):
        return ['beta_deg']

    def calculate(self, state, want_derived=True, **params_values):
        state['beta_deg'] = params_values['beta_deg']
        state['derived'] = {}
        return True

    def get_beta_deg(self):
        return self.current_state['beta_deg']
