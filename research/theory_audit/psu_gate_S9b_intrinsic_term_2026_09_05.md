# paper-su gate S9b — the intrinsic flat-slice initial-data term in the δN lane (2026-09-05)

**Status:** IN PROGRESS (plan header committed first; derivation steps appended per commit).

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
