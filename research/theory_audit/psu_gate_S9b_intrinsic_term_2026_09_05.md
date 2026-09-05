# paper-su gate S9b — the intrinsic flat-slice initial-data term in the δN lane (2026-09-05)

**Status:** DONE 2026-09-05 — **VERDICT S9b: NOT RECONCILED.** The intrinsic flat-slice term is $O(1/W)$ and vanishes in the growing-mode-dominated limit that defines the lane number; the residual $5(6-\epsilon)/24$ ($15/16$ at dust) arises in the super-Hubble evolution step, not in the initial data. Script `psu_gate_S9b_intrinsic_term_2026_09_05.py` + json (sympy 1.14 + mpmath, 9 s, all asserts pass).

## Plan

Input gap (S9.4 of `psu_gates_S9_S10_2026_09_05.md`): the lab's δN lane
(`fnl_matter_contraction_second_method_2026_09_02.{md,py}`) gives $f^{\delta N}_{\rm NL}=5(\epsilon-7)/8=-55/16$ at dust
from *Gaussian* flat-slice data $(u_i,s_i)$; the second-order uniform-density threading of the in-in result gives
$f^\rho=5(2\epsilon-15)/24=-5/2$. Gap $5(6-\epsilon)/24=15/16$. Candidate named there: the intrinsic flat-slice bispectrum of
the field perturbation omitted by the δN integration (Namjoo–Firouzjahi–Sasaki 2013 caveat for non-attractor phases).

Steps (each a commit, script `psu_gate_S9b_intrinsic_term_2026_09_05.py` + json):

1. **General initial data through the δN map, exactly.** Re-derive $N(u_i,s_i)$ to second order with the lane's closed forms;
   add $u_i=u_g+r_i u_g^2$, $\delta s_i=\delta s_g+c_s\,\delta s_g^2$ (arbitrary intrinsic NG of the flat-slice data) and obtain the
   intrinsic contribution to $\zeta_2/\zeta_1^2$ and to $f^\rho_{\rm NL}$ in closed form (general constant $\epsilon$, finite $W$).
2. **The $(\delta\phi,\delta\pi)$ chain.** $N_\phi,N_\pi,N_{\phi\phi},N_{\pi\pi},N_{\phi\pi}$ from $N(u,s)$ composed with the
   flat-slice map $u_i(\delta\phi,\delta\pi)$, $s_i(\delta\phi,\delta\pi)$ (local Friedmann constraint); the intrinsic
   $\langle\delta\phi^3\rangle,\langle\delta\phi^2\delta\pi\rangle,\dots$ enter only through $r_i,c_s$ of step 1.
3. **What the in-in must supply.** State the in-in flat-gauge three-point function's role as $r_i(t_i)$; use only two properties
   that any initial-data computation has (it does not know $t_f$; on a power-law background the $u$-cumulant ratio is
   $t_i$-independent) and test whether $-55/16+(\text{intrinsic})=-5/2$ can hold at $\epsilon=3/2$, and the general-$\epsilon$ form.
4. **Validations.** USR: $N(\phi,\pi)$ with vanishing intrinsic term reproduces $f_{\rm NL}=5/2$ (NFS). Attractor / no-growth
   limit: the intrinsic term passes through with unit weight. mpmath integration of the exact nonlinear patch ODE with
   non-Gaussian initial data confirms the closed-form intrinsic weight.
5. Verdict, the sentence paper-su / A3M may print, manifest, ledger rows.

Never steer toward reconciliation: the closed form of step 1 decides.

## 1. What the lane's map does with arbitrary initial data (exact, finite growth)

The lane integrates $N(u_i,s_i)=-(s_f-s_i)/\epsilon+N_u(\Sigma)\,u_i+\tfrac12N_{uu}(\Sigma)\,u_i^2$, $\Sigma=s_f-s_i$, with the
closed forms rebuilt here from the same ODE ($\epsilon=3/(1+q^2)$, $\alpha=q^2$, $W=e^{\alpha\Sigma}$; script step 1, asserted against
$-55/16$):
$$
N_u=\frac{2(W-1)(1+q^2)^{3/2}}{3q^2}=\frac{P}{\alpha}(W-1),\qquad
\frac{N_{uu}}{2}=-\frac{(W-1)(1+q^2)^2\,[(7q^2+4)W-q^2-4]}{6q^4}.\qquad(\text{S9b.1})
$$
Let the flat-slice data carry **arbitrary** intrinsic non-Gaussianity, $u_i=u_g+r\,u_g^2$, $\delta s_i=\kappa_s u_g+c_s\kappa_s^2u_g^2$
(whatever an in-in three-point function of the flat-gauge field and momentum at $t_i$ produces, it enters the $\delta N$ expansion only
through the three numbers $r,\kappa_s,c_s$ — this is the NFS 2013 caveat written as an input). Pushing them through (S9b.1) (step 2):
$$
\frac{\zeta_2}{\zeta_1^2}\Big|_{\rm Gauss}=-\frac{3[(7q^2+4)W-q^2-4]}{8(W-1)(1+q^2)}\ \xrightarrow{W\to\infty}\ \frac{3\epsilon-21}{8},\qquad
f^{\rm intr}_{\rm NL}(r)=\frac{5q^2\,r}{2(W-1)(1+q^2)^{3/2}}=\frac{5\,r\,\alpha}{3P\,(W-1)}
=\frac{5\sqrt{3\epsilon}\,(3-\epsilon)}{18}\,\frac{r}{W-1}.\qquad(\text{S9b.2})
$$
At dust $f^{\rm intr}_{\rm NL}=\tfrac{5\sqrt2}{8}\,\tfrac{r}{W-1}$. The $s$-channels give
$W f^{\rm intr}\to\tfrac{5\sqrt3\,\kappa_s(27-6\epsilon-\epsilon^2)}{72\sqrt\epsilon}$ (also $O(1/W)$; $c_s$ enters at $O(1/W^2)$).
**Every intrinsic channel is suppressed by the same growth factor that makes the lane's number a pure number.**

## 2. The $(\delta\phi,\delta\pi)$ chain (step 3)

With the flat-slice local constraint $3H_{\rm loc}^2=\tfrac12\pi_{\rm loc}^2+V(\phi_{\rm loc})$, $u_i=x_{\rm loc}-x_*$,
$\delta s_i=\ln|H_{\rm loc}/\bar H|$ (background $|\bar H|=1$ at $t_i$, $\lambda=\sqrt6x_*$), composition gives, e.g.
$N_\phi=-\tfrac{\sqrt6\,(q^2+2-2W)}{6\sqrt{1+q^2}}$, $N_\pi=-\tfrac{\sqrt6\,(2W-1)\sqrt{1+q^2}}{18}$, and
$N_{\phi\phi},N_{\pi\pi},N_{\phi\pi}\propto W^2$ (full forms in the json, `step3`); $N_\phi=N_u u_\phi+s_\phi/\epsilon$ and
$N_\pi=N_uu_\pi+s_\pi/\epsilon$ are asserted. For a single Gaussian seed $\delta\phi_g$ with growing-mode ratio $\varpi=\delta\pi/\delta\phi$
and intrinsic second-order data $\delta\phi^{(2)}=r_\phi\delta\phi_g^2$, $\delta\pi^{(2)}=r_\pi\delta\phi_g^2$,
$$
f^{\rm intr}_{\rm NL}=\frac53\,\frac{N_\phi r_\phi+N_\pi r_\pi}{(N_\phi+\varpi N_\pi)^2},\qquad
W f^{\rm intr}_{\rm NL}\ \xrightarrow{W\to\infty}\ -\frac{5\sqrt6\sqrt{1+q^2}\,[(1+q^2)r_\pi-3r_\phi]}{2\,[(1+q^2)\varpi-3]^2},\qquad(\text{S9b.3})
$$
$O(1/W)$ for every $\varpi$ with a non-zero growing-mode component, while the Gaussian part of the same chain reproduces $-55/16$ at
dust for every $\varpi$ (asserted). The in-in flat-gauge three-point function fixes $(r_\phi,r_\pi)$ — and nothing else.
