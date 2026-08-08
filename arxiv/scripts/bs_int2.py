import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

# ================= EXACT SETUP =================
# BS Eq7:  d(gamma^2)/d ln mu = -(gamma^2-1) * (mu^2 kappa^2)/(8pi)^2 * (23 gamma^2+5)
# kappa^2 = 16 pi G  (FIXED constant, NOT running -- BS Eq7 is written with fixed kappa^2;
#   the g-running is a separate refinement handled below).
# Non-reduced Mpl: G = 1/Mpl^2, Mpl = 1.22089e19 GeV.
#   mu^2 kappa^2 = 16 pi mu^2 / Mpl^2.
# Let x = mu/Mpl. prefactor P(mu) = (16 pi x^2)/(8pi)^2 = 16 pi x^2/(64 pi^2)= x^2/(4 pi).
Mpl = 1.22089e19
gamma0 = 0.2375           # LQG value at UV
g2_0 = gamma0**2

def dg2_dlnmu(t, y):
    # t = ln(mu/Mpl); mu = Mpl e^t ; x=mu/Mpl=e^t
    g2 = y[0]
    x2 = np.exp(2*t)                      # (mu/Mpl)^2
    P = x2/(4*np.pi)                      # = mu^2 kappa^2/(8pi)^2
    return [-(g2-1)*P*(23*g2+5)]

# Integrate from UV (mu=1e16 GeV) DOWN to IR (mu=1 GeV).
mu_UV = 1e16; mu_IR = 1.0
t_UV = np.log(mu_UV/Mpl)     # negative (since mu<Mpl)
t_IR = np.log(mu_IR/Mpl)
print(f"t_UV=ln(mu_UV/Mpl)={t_UV:.3f}, t_IR={t_IR:.3f}")

sol = solve_ivp(dg2_dlnmu, [t_UV, t_IR], [g2_0], rtol=1e-11, atol=1e-16, dense_output=True)
g2_IR = sol.y[0,-1]
print(f"\ngamma^2(UV)={g2_0:.8f}  ->  gamma^2(IR)={g2_IR:.10f}")
dg2 = g2_IR - g2_0
print(f"Delta(gamma^2) = {dg2:.6e}")
# Delta gamma/gamma = (1/2) Delta(gamma^2)/gamma^2  for small change
dgamma_over_gamma = 0.5*dg2/g2_0
print(f"Delta gamma / gamma = {dgamma_over_gamma:.6e}")
print(f"|Delta gamma/gamma| = {abs(dgamma_over_gamma):.3e}")

# ---- Analytic check: since gamma^2 barely moves, freeze (gamma^2-1)(23gamma^2+5) at gamma0:
C = -(g2_0-1)*(23*g2_0+5)/(4*np.pi)   # dg2/dt = C * e^{2t}
# integral from t_UV to t_IR of C e^{2t} dt = C/2 (e^{2 t_IR}-e^{2 t_UV})
dg2_analytic = C/2*(np.exp(2*t_IR)-np.exp(2*t_UV))
print(f"\nAnalytic (frozen-coeff) Delta(gamma^2) = {dg2_analytic:.6e}")
print(f"Analytic |Delta gamma/gamma| = {abs(0.5*dg2_analytic/g2_0):.3e}")
# The integral is dominated by e^{2 t_UV} (UV endpoint), magnitude ~ (mu_UV/Mpl)^2:
print(f"(mu_UV/Mpl)^2 = {(mu_UV/Mpl)**2:.3e}   <- the power-suppression scale")
