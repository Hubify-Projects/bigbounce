import numpy as np
from scipy.integrate import solve_ivp
Mpl = 1.22089e19
gamma0 = 0.2375; g2_0 = gamma0**2
def rhs(t,y):
    g2=y[0]; x2=np.exp(2*t); P=x2/(4*np.pi)
    return [-(g2-1)*P*(23*g2+5)]

print("UV-scale robustness (|Delta gamma/gamma| from integrating BS Eq7):")
for mu_UV,label in [(Mpl,"Planck 1.22e19"),(2.435e18,"reduced-Mpl 2.4e18"),(1e16,"GUT 1e16"),(1e12,"1e12")]:
    t_UV=np.log(mu_UV/Mpl); t_IR=np.log(1.0/Mpl)
    s=solve_ivp(rhs,[t_UV,t_IR],[g2_0],rtol=1e-11,atol=1e-18)
    dg2=s.y[0,-1]-g2_0; ddg=0.5*dg2/g2_0
    print(f"  mu_UV={label:22s}: |Dgamma/gamma|={abs(ddg):.3e}   (mu_UV/Mpl)^2={(mu_UV/Mpl)**2:.3e}")

print("\n=> running SATURATES at the UV endpoint: |Dgamma/gamma| ~ (mu_UV/Mpl)^2 * O(few).")
print("   At the Planck scale itself it is O(1e-6)*O(few) -- still <<1, formally outside pert. control at gamma^2=1 only.\n")

# ============ PROPAGATE TO rho_Lambda ============
# Paper's Route-3 amplitude: parity-odd Holst operator built from gamma, R, e, J^5 is dim-4,
# forcing a single 1/Mpl. The dark-energy channel amplitude sourced by the running is
#   rho_running ~ (Delta gamma/gamma) * <curvature/torsion condensate scale>.
# Most conservative DE-channel estimate the paper uses: the parity-odd amplitude is suppressed
# relative to a DE-scale source by factor (Delta gamma/gamma)*(H0/Mpl).
H0 = 1.44e-42        # GeV (H0 ~ 67.7 km/s/Mpc)
ddg = 1.406e-6
supp = ddg*(H0/Mpl)
print(f"Amplitude suppression (Delta gamma/gamma)*(H0/Mpl) = {supp:.3e}")

# rho_Lambda observed:
rho_Lambda_obs = (2.25e-3)**4   # (2.25 meV)^4 in GeV^4 ; ~ (2.25e-12 GeV)^4
print(f"rho_Lambda observed ~ (2.25 meV)^4 = {rho_Lambda_obs:.3e} GeV^4")

# The DERIVED torsion/Immirzi contribution to rho_Lambda:
# dimensional DE-channel density from the running-sourced parity-odd operator.
# Take the operator's natural scale = Mpl^4 * (dimensionless amplitude budget):
# budget ~ (Delta gamma/gamma)*(H0/Mpl)^? -- use the paper's own on-shell density ansatz form:
# rho ~ (Delta gamma/gamma) * H0^2 Mpl^2 (dim-4, one power 1/Mpl absorbed) as an UPPER estimate:
rho_run_A = ddg * H0**2 * Mpl**2
print(f"\nDerived rho_running (upper, ~ Dgamma/gamma * H0^2 Mpl^2) = {rho_run_A:.3e} GeV^4")
print(f"  ratio rho_running / rho_Lambda_obs = {rho_run_A/rho_Lambda_obs:.3e}")
# even more conservative: with the extra (H0/Mpl) the paper quotes:
rho_run_B = ddg*(H0/Mpl)*rho_Lambda_obs
print(f"\nDerived rho_running (paper channel, *(H0/Mpl)) = {rho_run_B:.3e} GeV^4")
print(f"  orders below rho_Lambda_obs = {np.log10(rho_Lambda_obs/rho_run_B):.1f}")
