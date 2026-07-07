import sympy as sp
import numpy as np

# ============================================================
# VERIFIED SOURCE (BS 2011, arXiv:1111.0884 Eq.7):
#   beta_{g2} = mu d(gamma^2)/d(mu) = -(g2-1) * (mu^2 kappa^2)/(8pi)^2 * (23 g2 + 5)
#   kappa^2 = 16 pi G ;  and define dimensionless g = mu^2 kappa^2 / (16 pi)  [Eq.4 defn]
#   so mu^2 kappa^2/(8pi)^2 = mu^2 kappa^2/(64 pi^2) = (16 pi g)/(64 pi^2) = g/(4 pi)
# Also (Eq.4, pure-gravity): beta_g = mu dg/dmu = g(2 - 17 g/(3 pi))
#   [The fermion-coupled sector modifies g-flow subleadingly; BS Eq.4 g-flow used.]
# ============================================================

g2, g, t = sp.symbols('gamma2 g t', positive=True)  # t = ln mu
pi = sp.pi

# rewrite BS Eq7 prefactor in terms of dimensionless g:
# mu^2 kappa^2/(8pi)^2 = g/(4 pi)
beta_g2_symbolic = -(g2 - 1) * (g/(4*pi)) * (23*g2 + 5)
print("beta_{gamma^2} in terms of dimensionless g:")
sp.pprint(beta_g2_symbolic)
# sanity: at g2=gamma^2, this is d gamma^2 / dt  (t=ln mu)

# ---------------------------------------------------------
# STEP A: the "power-suppression" claim in the paper.
# The paper argues: because prefactor carries mu^2 kappa^2 = (mu/Mpl)^2,
# the running is power-suppressed, integral dominated by UV endpoint,
# |Delta gamma/gamma| ~ (mu_UV/Mpl)^2.
# Check that magnitude directly.  kappa^2 = 1/Mpl^2 (reduced) up to 8pi conventions.
# Mpl (reduced) ~ 2.435e18 GeV.  We'll use the *reduced* Planck mass via kappa^2=8piG => Mpl_red^2 = 1/(8piG).
# BS use kappa^2 = 16 pi G. So mu^2 kappa^2 = 16 pi G mu^2 = 2 mu^2/Mpl_red^2 (since Mpl_red^2=1/(8piG)).
# Equivalently in terms of Mpl (=1/sqrt(G), 1.22e19): mu^2 kappa^2 = 16 pi mu^2/Mpl^2.
Mpl = 1.22e19   # GeV, non-reduced
mu_UV = 1e16    # GeV, GUT
gamma0 = 0.2375 # LQG Immirzi (black-hole entropy value)

x_UV = (mu_UV**2) * 16*np.pi / Mpl**2   # mu^2 kappa^2 dimensionless at UV
print("\nmu^2 kappa^2 at GUT (mu=1e16):", x_UV)

# beta_{gamma^2} magnitude at UV endpoint (treating g2~gamma0^2):
g2v = gamma0**2
coef = 1/(8*np.pi)**2
beta_val_UV = -(g2v - 1) * (mu_UV**2 * 16*np.pi/Mpl**2) * (23*g2v+5)  # note mu^2 kappa^2 = 16 pi mu^2/Mpl^2
# wait: prefactor is mu^2 kappa^2/(8pi)^2. mu^2 kappa^2 = 16 pi mu^2/Mpl^2.
beta_val_UV = -(g2v - 1) * (16*np.pi*mu_UV**2/Mpl**2) / (8*np.pi)**2 * (23*g2v+5)
print("beta_{gamma^2} numeric at UV endpoint (per unit d ln mu):", beta_val_UV)
