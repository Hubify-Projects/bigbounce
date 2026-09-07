# paper-su gate S9c — the dropped shift-divergence term in the δN uniform-density lane (2026-09-05)

**Status:** IN PROGRESS (plan header committed first, anti-stall).

## Plan

Open item after S9b (`psu_gate_S9b_intrinsic_term_2026_09_05.md` §5): the δN lane's uniform-density value
$f^{\delta N}_{\rm NL}=5(\epsilon-7)/8=-55/16$ (`fnl_matter_contraction_second_method_2026_09_02.{md,py}`) differs from the
second-order uniform-density threading map's $f^\rho=5(2\epsilon-15)/24=-5/2$ (`psu_gates_S9_S10_2026_09_05.md`, S9) by
$5(6-\epsilon)/24=15/16$ at dust. S9b showed the intrinsic initial-data channels vanish as $1/W$, so the residual lives in the
super-Hubble evolution between the flat initial slice and the uniform-density final slice. Candidate: the shift-divergence term
$\partial_iN^i$ that the lane's separate-universe integration drops, i.e. the exact worldline identity
$\delta N_c=\zeta-\tfrac13\int\partial_iN^i\,dt$ (`threading_map_second_order_2026_09_04.md`, eq. 2) generalised to $\rho$-threading.

Steps (one commit each, script `psu_gate_S9c_evolution_residual_2026_09_05.py` + json):
1. Evolution with the shift kept: $\zeta_\rho$ / $\delta N_{c,\rho}$ to second order from the flat slice in a constant-$\epsilon$
   non-attractor background, versus the lane's $N^i=0$ evolution; isolate the shift-divergence contribution to $f_{\rm NL}$.
2. Test whether it equals $5(6-\epsilon)/24$ (general $\epsilon$; $15/16$ at $\epsilon=3/2$) or state the residual.
3. Validate: attractor (term vanishes), USR (NFS $5/2$ unaffected), comoving-threading cross-check ($-5$, initial label).
4. Consequence + verdict (RECONCILED / NOT / UNRESOLVED), printable sentences, manifest, ledger rows 1 + 17.

---

## 1. Where the shift can and cannot enter (exact, before any computation)

Write the exact worldline identity of `threading_map_second_order_2026_09_04.md` eq. (1) once more,
$NK=\tfrac{d}{dt}\ln\sqrt h\,|_{\rm worldline}-\partial_iN^i$, with $K=\nabla_\mu n^\mu$ the expansion of the
normal (= fluid, $\delta\phi=0$) congruence. Two different objects are called "$\zeta$" in the two lanes:

* the **metric variable** $\zeta_{\rm Mald}=\tfrac13\delta\ln\sqrt h$ (Maldacena, in-in), and
* the **e-fold variable** $\delta N_c=\int\tfrac13NK\,dt-\bar N$ of the fluid congruence (separate universe).

The shift divergence is *exactly* their difference, eq. (2) of that note: $\delta N_c=\zeta_{\rm Mald}-\tfrac13\int\partial_iN^i\,dt$.
The $\delta N$ lane never forms $\ln\sqrt h$: its output is the e-fold count of a local FRW patch, $N_{\rm loc}=\int H_{\rm loc}\,d\tau$,
and $H_{\rm loc}$ is obtained from the local Friedmann + Klein–Gordon equations, i.e. from the equations of the **$n$-frame
quantities** $(K,\ d\phi/d\tau,\ \rho)$. In the 3+1 equations projected on $n^\mu$ the shift never appears explicitly — it is a
threading choice — and the $O(k^0)$ super-Hubble equations of the normal congruence are (units $8\pi G=1$)
$$
\tfrac23K^2-\sigma_{ij}\sigma^{ij}+R^{(3)}=2\rho,\qquad
\dot K=-\tfrac13K^2-\sigma^2-\tfrac12(\rho+3p)+D_ia^i,\qquad
\ddot\phi+K\dot\phi=-V'(\phi)\ (\text{dots}=d/d\tau,\ D_i\phi=0),
$$
with $R^{(3)}=O(k^2/a^2)$ and $D_ia^i=\partial^2\alpha/a^2=O(k^2)$. The isotropic separate universe is these equations with
$\sigma=0$. Hence the **only** $O(k^0)$ term the lane drops is $\sigma^2$; and in comoving gauge the shear *is* the traceless
part of the shift gradient, $\sigma_{ij}=-a^{-2}(\partial_i\partial_j\psi-\tfrac13\delta_{ij}\partial^2\psi)=-\epsilon\dot\zeta\,(\hat k_i\hat k_j-\tfrac13\delta_{ij})$
on the growing mode (the $\partial_iN^i$ trace part is what eq. (2) already accounts for). Its long–short cross term is
$2\sigma_L{:}\sigma_S\propto\dot\zeta_L\dot\zeta_S\,(\mu^2-\tfrac13)$, a **pure quadrupole**: it cannot move an isotropic number
(this is the Bianchi-I finding of `fnl_bianchi_separate_universe_2026_09_03.*`, "traceless, zero monopole", seen from the constraint side).

**Consequence for the plan.** The candidate named in the plan — "the lane drops $\partial_iN^i$ in the evolution" — is not a
dynamical omission: $\partial_iN^i$ enters only the *definition* of the variable, and S9 (`psu_gates_S9_S10_2026_09_05.md`) already keeps it
exactly when it continues $\zeta_{\rm Mald}\to\delta N_{c,\rho}$. If the separate-universe dynamics is exact for the monopole,
the lane's $\delta N$ on the $\rho$-slice and S9's $\delta N_{c,\rho}$ are the **same variable** and must agree in the monopole;
an isotropic residual $5(6-\epsilon)/24$ then cannot be an evolution term and must be a bookkeeping error in one of the two
computations. §2 tests this with an independent, exact separate-universe integration (both final slices, general $\epsilon$),
which decides which side carries the error before any further term is hunted.

## 2. Independent exact separate-universe solution, both slices, general $\epsilon$ (script Parts A + B)

Constant-$\epsilon$ scalar contraction, $V=V_0e^{-\lambda\phi}$, $\lambda=\sqrt{2\epsilon}$, in the autonomous variables
$x=\dot\phi/(\sqrt6H)$, $s=\ln|H|$, $N=\ln a$ (flat, scalar-only, so $y^2=1-x^2$):
$$
x'=G(x)\equiv-3x+\tfrac{\sqrt6}{2}\lambda(1-x^2)+3x^3,\qquad s'=-3x^2,\qquad
x_*=\lambda/\sqrt6,\ \ G'(x_*)=\kappa=\epsilon-3,\ \ G''(x_*)=4\sqrt{3\epsilon}.
$$
Growing mode $\propto e^{\kappa N}=a^{-(3-\epsilon)}$ (the $\zeta\propto(-t)^{-(3-\epsilon)/\epsilon}$ mode). A worldline carries
$x=x_*+Ax_1+A^2x_2$, $s=-\epsilon N+As_1+A^2s_2$ with $x_1=W$, $s_1=-6x_*W/\kappa$, $x_2=\tfrac{G''}{2\kappa}(W^2-W)$,
$s_2'=-3(2x_*x_2+x_1^2)$, $W\equiv e^{\kappa N}$ ($W=1$ on the flat slice $N=0$, $W\to\infty$ is the growing-mode-dominated
limit; any $A^2$ initial term is $O(1/W)$, S9b). The final slice is used as the *independent variable*, so the crossing is
exact: $\rho$-slice $s=s_f$; comoving slice $\Phi\equiv2s+\ln(1-x^2)=\Phi_f$ (since $\phi=-\lambda^{-1}[\ln3+\Phi]$).
Solving $F(N,A)=\bar F(N_f)$ for $N(A)=N_f+An_1+A^2n_2$ and $f=\tfrac56\,(2n_2)/n_1^2$ (initial-position label by construction):
$$
f^{\rm SU}_\phi(W)=-5+\frac{10\epsilon}{3W}-\frac{5(\epsilon+1)}{2W^2}\ \xrightarrow{W\to\infty}\ \boxed{-5\ \ (\text{every }\epsilon)},\qquad
f^{\rm SU}_\rho(W)=\frac{5(\epsilon-7)}{8}+\frac{5\epsilon}{3W}-\frac{5(\epsilon+1)}{8W^2}\ \xrightarrow{W\to\infty}\ \boxed{\frac{5(\epsilon-7)}{8}=-\frac{55}{16}\ \text{at dust}},
$$
with $N_1^\rho/N_1^\phi\to2$ ($\lambda'=2\lambda$, as S9 asserts). Cross-checked by direct DOP853 integration of the nonlinear
system at $(\epsilon,\Delta N)=(1.5,3),(1.5,6),(1.2,4),(2.2,6)$: $|f_{\rm num}-f_{\rm closed}|<2\times10^{-5}$ (json
`part_A_numeric_crosscheck`). So:

* the **comoving-slice** separate universe reproduces the threading map's initial-label value $-5$ for **every** constant
  $\epsilon$ — an independent validation that the $\sigma=0$ separate-universe dynamics is exact for the monopole (§1);
* the **uniform-density** separate universe reproduces the lane's $5(\epsilon-7)/8$ for every $\epsilon$, from a different
  parametrisation and a different integrator than `fnl_matter_contraction_second_method_2026_09_02.py`;
* $f^{\rm SU}_\rho-f^{\rm S9}_\rho=5(\epsilon-7)/8-5(2\epsilon-15)/24=-5(6-\epsilon)/24$: the gap is reproduced exactly, and it
  sits on the **S9 side** of the comparison, since the two lanes agree on the $\phi$-slice and the $\phi\to\rho$ step is a
  purely local algebraic continuation.

## 3. Localising the residual inside S9's continuation (script Part C)

S9's continuation (S9.3)–(S9.4) on the growing mode, monopole, keeping the second-order $L\times S$ lapse $A_2$
(coefficient of $\zeta_L\zeta_S$) symbolic and every other input a linear object
($H\delta t^{(1)}=\lambda\zeta$, $\dot\zeta=-(3-\epsilon)H\zeta$, $\alpha_1=\dot\zeta/H$, $\dot{\bar\rho}=-6\epsilon H^3$,
$\ddot{\bar\rho}=18\epsilon^2H^4$, $\delta\dot\rho^{(1)}=-2\epsilon(3-\epsilon)(3+\epsilon)H^3\zeta$):
$$
H\delta t^{(2)}_{LS}=-\frac{A_2}{3}+\frac{(3-\epsilon)^2(3+\epsilon)}{9},\qquad
M_{\rm extra}=H\delta t^{(2)}-\epsilon H^2\delta t_L\delta t_S+\lambda(\dot\zeta_L\delta t_S+\dot\zeta_S\delta t_L)
=-\frac{A_2}{3}+\frac{(3-\epsilon)^2(2\epsilon-3)}{9},
$$
$f_{\rm extra}=\tfrac56M_{\rm extra}/\lambda'^2$ (local kernel, $\rho$ normalisation). With S9's own squeezed $O(k_L^0)$ lapse
monopole, $A_2^{\rm S9}=\epsilon(3-\epsilon)^2/3$ (json key `S9.A2_superhubble_growing`, $\mu^2\to\tfrac13$; the $1/k_L$ pole
$\epsilon(3-\epsilon)\mu k_S/k_L$ has zero monopole at $n_s=1$, eq. (3) of the threading note), this chain returns
$f_{\rm extra}=5(\epsilon-3)/24$ — **exactly S9's `extra_only` monopole** — so the bookkeeping of S9 is reproduced and the
lapse monopole is the only non-linear input. The exact separate universe fixes the combination in which $\zeta^{(2)}_{\rm Mald}$
cancels ($\lambda'=2\lambda$): $f^{\rm SU}_\rho-\tfrac12f^{\rm SU}_\phi=f[M_{\rm extra}-M_\phi]_\rho$, i.e.
$f_{\rm extra}^{\rm req}=5(2\epsilon-9)/24$, hence
$$
\boxed{A_2^{\rm req}=2(3-\epsilon)^2=2\,\alpha_L\alpha_S/(\zeta_L\zeta_S)}\quad\text{vs}\quad A_2^{\rm S9}=\frac{\epsilon(3-\epsilon)^2}{3},
\qquad f_{\rm extra}^{\rm S9}-f_{\rm extra}^{\rm req}=\frac{5(6-\epsilon)}{24}\ (=\tfrac{15}{16}\ \text{at dust}).
$$
The **entire** residual is the difference between these two lapse monopoles ($9/8$ vs $9/2$ at dust). The required value has the
form $N=1+\alpha_1+2\alpha_L\alpha_S$ in the monopole, i.e. $1/N=1-\dot\zeta/H$ with no second-order monopole; it vanishes in the
attractor ($\dot\zeta=0$) like S9's, so the attractor check S9 passed does not discriminate. What this lane cannot do from the
separate universe alone is derive $A_2$ independently: the SU supplies two exact relations (the lapse $1+\alpha=x_*e^{\bar s}/(xe^{s})$
on the comoving slice and $N_c$), but they involve $\zeta^{(2)}_{\rm Mald}$ and the second-order shift divergence as well, and only
the momentum constraint closes the system — that is the S9 constraint solve itself.
