# When does the isotropic separate universe fail? A criterion for the $O(1)$ breakdown of $\delta N$ in non-attractor phases

**BigBounce theory-audit lane · 2026-09-04 · novelty lift #2 (`project-context/NOVELTY_AUDIT_2026-09-04.md` C2) · proposed NEXT_SCIENCE_LEDGER row 16**

## Plan (written first, anti-stall)

Input (frozen, not re-derived here): the exact threading identity
$\delta N_c(x_f)=\zeta(t_f,x_f)-\tfrac13\int\partial_iN^i\,dt$ along the fluid worldline, and the constant-$\epsilon$
second-order map $f_{\delta N}=f^{\rm in\text{-}in}/\lambda+f_{\rm map}$, $\lambda=1-\epsilon/3$,
$f_{\rm map}=-\tfrac{5\epsilon}{4}+\tfrac{5\epsilon}{4}\mu^2$
(`threading_map_second_order_2026_09_04.{md,py,json}`; in-in inputs from `fnl_monopole_adjudication_2026_09_03.md`).

Steps, each committed by explicit path as it lands:
1. Linear order for a **general** history $\epsilon(t)$, $\zeta_L(t)$: derive $\lambda$ as a functional of the
   history; identify the dimensionless control parameter and show where $\lambda\ne1$ comes from.
2. Second order at constant $\epsilon$: $f_{\rm map}(\epsilon,\mu)$, its general-$w$ form, and the $\epsilon\to0$
   (USR-type) and $\dot\zeta\to0$ (attractor) limits; state precisely why $\delta N$ with $N(\phi,\pi)$ works in
   USR although the shift is $O(1/k_L)$ there too.
3. Validations: dust contraction ($\epsilon=3/2$), USR inflation, attractor slow-roll, ekpyrotic contraction
   ($\epsilon\gg3$, both $\zeta$ modes). Script + JSON (exact sympy, closed forms; no new constraint solve).
4. The criterion in one line; literature placement (Namjoo–Firouzjahi–Sasaki 1210.3692; Chen–Firouzjahi–Namjoo–Sasaki
   1301.5699; Pajer–Schmidt–Zaldarriaga 1305.0824; Dai–Pajer–Schmidt 1504.00351; Cai et al. 1712.09998;
   Bravo–Mooij–Palma–Pradenas 1711.02680 / 1711.05290; Passaglia–Hu–Motohashi 1812.08243; Artigas–Grain–Vennin
   2110.11720; Jackson et al. 2311.03281); what is new relative to each; the sentences a short note could claim.
5. VERDICT; manifest; ledger row-16 proposal line (not added to the ledger by this lane).

Conventions as in the inputs: $B_{\rm sq}=\tfrac{12}{5}f\,P_LP_S$, $\mu=\hat k_L\!\cdot\!\hat k_S$, $\epsilon=-\dot H/H^2$
(positive in contraction), $\delta N_c$ = e-folds of the fluid (zero-shift) congruence = the variable the isotropic
separate universe computes.

(Derivation, validations, criterion and verdict follow as they are completed.)

---

## 1. Linear order for a general history: where $\lambda\neq1$ comes from

Comoving gauge, super-Hubble long mode. The first-order ADM solution is $\alpha=\dot\zeta/H$ and
$N^i=a^{-2}\partial_i\psi$, $\psi=-\zeta/H+\chi$, $\partial^2\chi=a^2\,\frac{\epsilon}{c_s^2}\,\dot\zeta$
(Maldacena 2003 for $c_s=1$; Chen–Huang–Kachru–Shiu 2006 for $P(X)$). Hence, exactly in $k$,
$$
\partial_iN^i=\frac{\epsilon}{c_s^2}\,\dot\zeta-\frac{\partial^2\zeta}{a^2H}
\;\xrightarrow{\,k\ll aH\,}\;\frac{\epsilon}{c_s^2}\,\dot\zeta+O\!\Big(\frac{k^2}{a^2H^2}\Big)H\zeta .\tag{1.1}
$$
The **only** $O(k^0)$ divergence of the comoving shift is $\epsilon\dot\zeta/c_s^2$: the $-\zeta/H$ part of $\psi$ is
$O(1/k)$ too, but its divergence is $O(k^2)$, while the $\chi$ part is $O(1/k_L)\times\epsilon\dot\zeta$, whose
divergence is $O(k^0)$. So "the shift is $O(1/k_L)$" is **not** the operative statement — every comoving shift is
$O(1/k)$ — the operative statement is that the $\chi$ part carries the amplitude $\epsilon\dot\zeta_L$.

Inserting (1.1) into the exact identity (threading note eq. 2), for a long mode that grows from
$\zeta_L(-\infty)=0$ to $\zeta_L(t_f)$ (growing-mode initial condition; for a mode that is constant over some
interval the integrand vanishes there):
$$
\boxed{\;\delta N_c=\lambda\,\zeta_L,\qquad \lambda=1-\frac{\langle\epsilon/c_s^2\rangle_\zeta}{3},\qquad
\langle X\rangle_\zeta\equiv\frac{1}{\zeta_L(t_f)}\int_{-\infty}^{t_f}X\,\dot\zeta_L\,dt=\frac{1}{\zeta_L(t_f)}\int X\,d\zeta_L\;}\tag{1.2}
$$
i.e. the linear rescaling is one minus a third of the **$\zeta$-growth-weighted mean of $\epsilon/c_s^2$**: the
value of $\epsilon/c_s^2$ during the part of the history in which the long mode acquired its amplitude. This is the
general-history form of the constant-$\epsilon$ result $\lambda=1-\epsilon/3$ (which follows immediately since a
constant pulls out of the integral, for any growing-mode exponent). Three readings of the same quantity:

- **Instantaneous rate.** $\Theta\equiv\dfrac{\partial_iN^i_L}{H\zeta_L}\Big|_{k\to0}=\dfrac{\epsilon}{c_s^2}\dfrac{\dot\zeta_L}{H\zeta_L}$;
  then $1-\lambda=\tfrac13\int\Theta\,(\zeta_L/\zeta_{L,f})\,dN$. For a constant-$\epsilon$ power law
  $a\propto(-\eta)^{p}$, $p=1/(\epsilon-1)$, the non-constant mode is $\zeta\propto(-\eta)^{(\epsilon-3)/(\epsilon-1)}$ so
  $\dot\zeta/(H\zeta)=\epsilon-3$ and $\Theta=\epsilon(\epsilon-3)$ (script: `Theta_const_eps`).
- **Local expansion rate on comoving slices.** $K=3H(1-\alpha)+3\dot\zeta-\partial_iN^i$ gives
  $\delta K|_{k\to0}=-\epsilon\dot\zeta/c_s^2$, i.e. $\delta H_{\rm loc}/H=-\tfrac13\Theta\,\zeta_L$: the fluid's
  expansion rate on the comoving slicing is perturbed **at $O(k^0)$**. The gradient expansion assumes this is $O(k^2)$
  (Lyth–Malik–Sasaki 2005, the "$N_i=O(\nabla)$" assumption) — that assumption is exactly $\Theta=0$.
- **Comoving density contrast.** Hamiltonian constraint on comoving slices: $6H\delta H_{\rm loc}=\delta\rho_c/M_p^2$,
  so $\delta\rho_c/\rho=-\tfrac23\Theta\,\zeta_L$. The separate universe fails at $O(1)$ **iff the comoving density
  contrast of the long mode is $O(k^0)\,\zeta_L$ instead of $O(k^2/a^2H^2)\,\zeta_L$** — equivalently, iff the Bardeen
  potential of the long mode is $\Psi_L=O((aH/k)^2)\,\zeta_L$ (a growing Newtonian potential), which is the textbook
  signature of the non-attractor contraction (Wands 1999; Finelli–Brandenberger 2002).

Three regimes, read off (1.2):

| phase | $\dot\zeta_L/(H\zeta_L)$ | $\epsilon$ during growth | $\Theta$ | $\langle\epsilon\rangle_\zeta$ | $\lambda$ |
|---|---|---|---|---|---|
| attractor (constant $\zeta$) | $0$ | any | $0$ | $0$ | $1$ |
| inflationary USR ($\epsilon\propto a^{-6}$, $\zeta\propto a^{3}$) | $3$ | $\epsilon\ll1$ | $3\epsilon\ll1$ | $\epsilon_{\rm f}-\sqrt{\epsilon_{\rm s}\epsilon_{\rm f}}\ll1$ (§1.1) | $1+O(\epsilon)$ |
| constant-$\epsilon$ contraction, $1<\epsilon<3$ | $\epsilon-3$ | $O(1)$ | $\epsilon(\epsilon-3)=O(1)$ | $\epsilon$ | $1-\epsilon/3$ |

**§1.1 USR exactly (linear).** Take $\epsilon=\epsilon_{\rm s}(a/a_{\rm s})^{-6}$ and $\zeta_L\propto a^3$ from the start of
the USR phase at $a_{\rm s}$ (preceded by slow roll, where the mode was frozen and contributes nothing to the integral).
Then $\int\epsilon\,d\zeta_L=\epsilon_{\rm s}\zeta_{\rm s}-\epsilon_{\rm f}\zeta_{\rm f}$ exactly ($\epsilon\propto\zeta^{-2}$),
so $\langle\epsilon\rangle_\zeta=\sqrt{\epsilon_{\rm s}\epsilon_{\rm f}}-\epsilon_{\rm f}$ and
$$
\lambda_{\rm USR}=1+\frac{\epsilon_{\rm f}}{3}-\frac{\sqrt{\epsilon_{\rm s}\epsilon_{\rm f}}}{3}=1+O(\epsilon)\quad(\text{script: `lambda_USR_exact`}).
$$
The sign is opposite to the contraction case because $\epsilon$ *decreases* while $\zeta$ grows, but the magnitude is
what matters: USR has a $1/k_L$ shift and $\dot\zeta_L\neq0$, yet $\lambda=1$ up to $O(\epsilon)$ because the
shift's coefficient $\epsilon$ is small throughout the growth. This is the first half of the answer to "why does
$\delta N$ with $N(\phi,\pi)$ work in USR" (the second-order half is §2.3).
