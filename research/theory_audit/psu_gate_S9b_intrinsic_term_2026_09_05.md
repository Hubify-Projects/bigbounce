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

## 3. What the in-in must supply, and whether it can close the gap (step 2, verdict block)

Closing (S9.5) would need $-\tfrac{55}{16}+f^{\rm intr}=-\tfrac52$, i.e. $f^{\rm intr}=+\tfrac{15}{16}$ at dust, $\tfrac{5(6-\epsilon)}{24}$
in general. Solving (S9b.2) for the initial-data coefficient:
$$
r_{\rm req}=\frac{\sqrt3\,(\epsilon-6)(W-1)}{4\sqrt\epsilon\,(\epsilon-3)}\quad\Big(=\tfrac{3\sqrt2}{4}(W-1)\ \text{at dust}\Big),\qquad(\text{S9b.4})
$$
which **grows with the final time** ($W=e^{\alpha(s_f-s_i)}$). Initial data at $t_i$ cannot depend on $t_f$; so no flat-slice
three-point function — computed by in-in from the flat-gauge cubic action or otherwise — reconciles the two numbers. The only
loophole would be an intrinsic ratio at $t_i$ that itself grows like $e^{\alpha(s_i-s_\times)}$ since the short modes' Hubble exit;
that is excluded by the end-time independence of the in-in squeezed bispectrum on this background (S9.2 of the S9/S10 note, asserted
there: $A_2\propto\zeta_L\zeta_S$), because for growing-mode data the flat-gauge $(\delta\phi,\delta\pi)$ at $t_i$ are a
time-independent linear-plus-quadratic transform of $(\zeta,\dot\zeta)$, so $r_i$ is a $t_i$-independent pure number (self-similar),
not a growing one. In the ODE language: the intrinsic ratio $r(s)=u_2/u_1^2$ obeys $r'=-\alpha(r+\beta)$ — a *forgetting* equation with
fixed point $-\beta$; the lane's $W\to\infty$ number is that fixed point, independent of $r_i$.

**The number $r_i$ itself is not computed here** (the flat-gauge in-in three-point function on the constant-$\epsilon$ contraction
with the Seery–Lidsey/Maldacena cubic action remains an open computation); the verdict does not depend on its value, only on the
two properties above, both of which any such computation has.

## 4. Validations (step 4; all asserted)

- **USR (NFS 2013).** $N(\phi,\pi)=-\tfrac13\ln[1-3H(\phi_e-\phi)/\pi]$ on the trajectory with $N_0$ e-folds left, Gaussian $\delta\phi$,
  $\delta\pi=0$: $\zeta_2/\zeta_1^2=\tfrac32$, $f_{\rm NL}=\tfrac52$ exactly; the intrinsic weight is $(5/3)/N_\phi=-\tfrac{5\pi}{3H}e^{-3N_0}$,
  so NFS's vanishing intrinsic term is doubly safe there (the cubic action is $O(\epsilon)$ *and* its weight is $e^{-3N_0}$). Same mechanism.
- **Attractor / no-growth ($W\to0$).** $\partial f/\partial r\to\tfrac{5\sqrt{3\epsilon}(\epsilon-3)}{18}$: finite, $O(1)$ — with no growth the
  initial-data non-Gaussianity passes through undiluted (the Maldacena-type intrinsic term); the suppression is a growing-mode effect,
  not an artefact of the formula.
- **Exact nonlinear ODE (mpmath, 40 digits, $\Sigma=6$, $W=e^6$).** Non-Gaussian data $u_i=u_g+ru_g^2$, $r\in\{0,\pm3\}$: numeric
  $f_{\rm NL}$ matches $f_{\rm NL}(0)+\tfrac{5r\alpha}{3P(W-1)}$ to $4\times10^{-10}$ ($f(0)=-3.44216$, $f(\pm3)=-3.43557/-3.44875$).

## 5. Verdict and the printable sentence

**VERDICT S9b: NOT RECONCILED.** Intrinsic term: $f^{\rm intr}_{\rm NL}=\tfrac{5\sqrt{3\epsilon}(3-\epsilon)}{18}\,\tfrac{r_i}{W-1}$
($=\tfrac{5\sqrt2}{8}\tfrac{r_i}{W-1}$ at $\epsilon=\tfrac32$) $\to0$ in the growing-mode-dominated limit for any $t_f$-independent $r_i$;
it is not $-\tfrac{15}{16}$ (nor $+\tfrac{15}{16}$), and $-\tfrac{55}{16}+f^{\rm intr}\neq-\tfrac52$. **Residual:** $5(6-\epsilon)/24$
unchanged. **Step where it arises:** the super-Hubble evolution between the flat slice at $t_i$ and the uniform-density slice at $t_f$ —
the separate-universe map (S9b.1) versus the in-in evolution threaded in S9 — not the initial data. Candidate (named, not asserted here):
the $\delta N$ integration keeps no shift, whereas the growing mode has $\tfrac13\int\partial_iN^i\,dt=(\epsilon/3)\zeta$ at linear order
($\lambda=1-\epsilon/3$); its second-order partner is exactly what the threading kernels $M_{\rm extra}$, $A_2$ carry.

**Sentence paper-su / A3M may print:** "The separate-universe δN value on uniform-density slices, $f_{\rm NL}=5(\epsilon-7)/8=-55/16$
at dust, is not the second-order uniform-density threading of the in-in bispectrum, $5(2\epsilon-15)/24=-5/2$: the difference,
$5(6-\epsilon)/24$, is not an omitted intrinsic non-Gaussianity of the flat-slice initial data (any such term enters with weight
$\propto1/W$ and vanishes in the growing-mode-dominated limit) but arises in the super-Hubble evolution between the two slices, so the
two numbers must not be presented as the same physics in a third variable."

Receipts: script sha256 `adfb4db13fd885d9…`, json `0c73d74511536f1f…` (regenerated by the script; key `verdict`), 9 s local CPU.
