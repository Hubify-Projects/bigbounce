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

## 2. Second order: $f_{\rm map}$, the general-$w$ form, and the limits

### 2.1 Constant $\epsilon$ (input, frozen)
With $\delta N_c^{(2)}=\mathcal M\,\zeta_L\zeta_S$ from the exact second-order constraints, the squeezed bispectrum of
$\delta N_c$ is $f_{\delta N}=f^{\rm in\text{-}in}/\lambda+f_{\rm map}$ with (final-position label)
$$
f_{\rm map}(\epsilon,\mu)=-\frac{5\epsilon}{4}\,(1-\mu^2),\qquad \text{monopole }-\frac{5\epsilon}{6},\tag{2.1}
$$
and every piece of $\mathcal M$ (`zlap`, `psi2`, `grad`, `wl_fin`, `lab_init`) carries an explicit factor
$\epsilon$ — they are all generated by the $\chi$ part of the shift, i.e. by the same $\epsilon\dot\zeta$ that gives
$\Theta$. Since the in-in amplitude is $f^{\rm in\text{-}in}=\tfrac{5}{12}(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12)$,
the isotropic separate-universe value is $f_{\delta N}=-5$ (initial-position label, exactly, all constant $\epsilon$)
and the discrepancy from the in-in monopole is $5\epsilon(9-\epsilon)/18=\tfrac{5\epsilon}{3}+\tfrac{5\epsilon(3-\epsilon)}{18}$
(linear rescaling + second-order map). **Both terms are $O(\epsilon)$ with $O(1)$ coefficients**: at $\epsilon=O(1)$ the
failure is $O(1)$; at $\epsilon\to0$ it vanishes linearly in $\epsilon$. That is the whole criterion.

### 2.2 General constant $w$ ($\epsilon=\tfrac32(1+w)$, $c_s=1$ scalar-field realisation)
$$
\lambda=\frac{1-w}{2},\qquad \Theta=-\frac94\,(1-w^2),\qquad
f_{\rm map}=-\frac{15}{8}(1+w)(1-\mu^2),\qquad f_{\rm map}^{\rm mono}=-\frac54(1+w),
$$
$$
f^{\rm in\text{-}in}=\frac{15}{16}(1+w)^2(\mu^2-1)+\frac{15}{4}(1+w)-5,\qquad
f_{\delta N}^{\rm(initial\ label)}=-5\ \ (\text{all }w),\qquad
f_{\delta N}^{\rm(final\ label)}=-\frac{5(3w-5)}{4(w-1)}-\frac{15(1+w)}{4(w-1)}\,\mu^2 .
$$
Checks: $w=0$ gives $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ vs $-5$; $w=-1$ (de Sitter, $\epsilon=0$) gives $\lambda=1$,
$f_{\rm map}=0$; $w=1$ (kination, $\epsilon=3$): $\lambda=0$ — $\delta N_c$ has no linear response and is not a usable
variable there; the in-in monopole $\to0$ there. $\Theta$ vanishes at both $w=\pm1$ but for different reasons
(constant $\zeta$ at $w=-1$; logarithmic growth at $w=1$, where the integrated $\langle\epsilon\rangle_\zeta=3$ still
gives $\lambda=0$ — the integrated form (1.2), not the instantaneous $\Theta$, is the criterion).

### 2.3 Why $\delta N$ with $N(\phi,\pi)$ reproduces USR's $5/2$ although the shift is $O(1/k_L)$ there too
Two *independent* things can go wrong with a separate-universe computation in a non-attractor phase:

1. **Initial-data (Namjoo–Firouzjahi–Sasaki 2013).** The growing mode needs the momentum as an independent datum:
   $N(\phi)$ misses it, $N(\phi,\pi)$ restores it. This concerns whether the separate universe computes *its own*
   variable $\delta N_c$ correctly. It is present in every non-attractor phase, inflationary or contracting, and it is
   fully fixed by $N(\phi,\pi)$ — in the lab's dust contraction, lane (B)'s $N(\phi,\pi)$ ODE system gives $-5$, which
   the threading note shows is exactly the bispectrum of $\delta N_c$. So $N(\phi,\pi)$ works there too.
2. **Threading (this note).** Whether $\delta N_c$ *is* $\zeta_{\rm Mald}$. By the exact identity the difference is
   $\tfrac13\int\partial_iN^i dt$ along the fluid worldline, with $\partial_iN^i=\epsilon\dot\zeta$ at $O(k^0)$ and every
   second-order piece $\propto\epsilon$. In USR, $\epsilon\ll1$ throughout the growth of $\zeta_L$, so
   $\delta N_c=\zeta_{\rm Mald}\,[1+O(\epsilon)]$ at linear order (§1.1, exact) and $f_{\delta N}=f^{\rm in\text{-}in}+O(\epsilon)$
   at second order (each map piece is $\int\epsilon(t)\,F[\zeta_L,\zeta_S]\,dt$ and is bounded by the same
   $\langle\epsilon\rangle_\zeta$-type average; this is a structural statement, the constant-$\epsilon$ kernels with
   $\epsilon\to0$, not a re-solve with $\epsilon\propto a^{-6}$). Since $5/2$ is itself the leading term in $\epsilon$,
   $\delta N(\phi,\pi)$ and in-in must agree at that order — and they do.

So the shift's $1/k_L$ scaling is *necessary* for an $O(1)$ failure (it is what makes $\partial_iN^i$ $O(k^0)$) but not
sufficient: the coefficient of the $1/k_L$ term is $\epsilon\dot\zeta_L$, and only when $\epsilon=O(1)$ during the growth
of the mode does the divergence become $O(1)\,H\zeta_L$. Inflationary non-attractors (USR and the $P(X)$ generalisation
of Chen–Firouzjahi–Namjoo–Sasaki 2013, where $\epsilon$ also decays) sit in the $\epsilon\to0$ corner; contracting
non-attractors with a growing $\zeta$ ($1<\epsilon<3$) sit at $\epsilon=O(1)$. The inflationary literature could
therefore only ever see failure mode 1; failure mode 2 is invisible at $O(\epsilon)$ and was never tested there.

### 2.4 The criterion (one line)
> **The isotropic separate universe ($\delta N$, with $N(\phi,\pi)$ so that the growing mode is captured) reproduces
> the squeezed bispectrum of the comoving curvature perturbation $\zeta$ iff the $\zeta$-growth-weighted mean
> $\langle\epsilon/c_s^2\rangle_\zeta=\tfrac{1}{\zeta_{L,f}}\!\int\!(\epsilon/c_s^2)\,d\zeta_L$ vanishes — equivalently iff the
> divergence of the long mode's comoving shift, $\partial_iN^i_L=(\epsilon/c_s^2)\dot\zeta_L$, integrates to nothing
> along the fluid worldline, i.e. iff the long mode's comoving density contrast (Bardeen potential) stays
> $O(k^2/a^2H^2)$ [$O(1)$] while it grows. When $\langle\epsilon\rangle_\zeta=O(1)$ — every constant-$\epsilon$
> contraction with a growing $\zeta$ — $\delta N_c=(1-\langle\epsilon\rangle_\zeta/3)\,\zeta$ and the squeezed
> amplitudes differ at $O(1)$: $f_{\delta N}=f^{\rm in\text{-}in}/\lambda-\tfrac{5\epsilon}{4}(1-\mu^2)$.
> When $\langle\epsilon\rangle_\zeta\ll1$ (attractor: $\dot\zeta_L=0$; inflationary USR: $\epsilon\ll1$) the two
> agree to $O(\langle\epsilon\rangle_\zeta)$, which is why $\delta N$ never failed in the inflationary tests.**

## 3. Validations (script `separate_universe_failure_criterion_2026_09_04.py`, exact sympy, 0.2 s)

| case | $\dot\zeta_L/(H\zeta_L)$ | $\Theta$ | $\langle\epsilon\rangle_\zeta$ | $\lambda$ | $f^{\rm in\text{-}in}_{\rm sq}$ | $f_{\delta N}$ (isotropic SU) | criterion says | literature |
|---|---|---|---|---|---|---|---|---|
| dust contraction, $\epsilon=3/2$ ($w=0$) | $-3/2$ | $-9/4$ | $3/2$ | $1/2$ | $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ (mono $-15/8$) | $-5$ | **fails at $O(1)$**: gap $25/8=\tfrac{5}{2}+\tfrac{5}{8}$ | lab in-in (2026-09-02/03), $\delta N$ lanes A/B/C; Cai+2009 $\times2$ located |
| general $1<\epsilon<3$ contraction | $\epsilon-3$ | $\epsilon(\epsilon-3)$ | $\epsilon$ | $1-\epsilon/3$ | $\tfrac{5}{12}(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12)$ | $-5$ (all $\epsilon$) | fails at $O(\epsilon)$, coefficient $O(1)$ | this work (general-$w$ form §2.2) |
| inflationary USR ($\epsilon\propto a^{-6}$) | $+3$ | $3\epsilon$ | $\sqrt{\epsilon_s\epsilon_f}-\epsilon_f$ | $1+O(\epsilon)$ (exact: $1+\tfrac{\epsilon_f}{3}-\tfrac{\sqrt{\epsilon_s\epsilon_f}}{3}$; $0.99997$ at $\epsilon_s=10^{-2},\epsilon_f=10^{-6}$) | $5/2$ | $5/2$ with $N(\phi,\pi)$ | **agrees to $O(\epsilon)$** — both failure modes accounted for (§2.3) | NFS 2013 ✓ (reproduced by construction) |
| attractor slow roll | $0$ | $0$ | $0$ | $1$ | $\tfrac{5}{12}(1-n_s)$ | same | identity map (`div_cross = 0` at second order) | Maldacena 2003 ✓ |
| ekpyrotic, $\epsilon\gg3$, dominant mode | $0$ (constant mode; the other mode $\propto(-\eta)^{(\epsilon-3)/(\epsilon-1)}$ decays) | $0$ | $0$ | $1$ | attractor-like | same | identity map — **not** a failure although contracting | Creminelli–Nicolis–Zaldarriaga 2004 ✓ (constant mode dominates; consistency relation holds) |
| ekpyrotic, non-dominant mode (growing $\Psi$) | $\epsilon-3$ | $\epsilon(\epsilon-3)\gg1$ | $\epsilon$ | $1-\epsilon/3<0$ | — | — | $\delta N_c$ not a usable variable; irrelevant since this mode never sets $\zeta_L(t_f)$; constant-$\epsilon$ kernels not applicable ($m<0$) | — |
| kination $\epsilon=3$ ($w=1$) | $\to0$ (log) | $\to0$ | $3$ | $0$ | mono $\to0$ | — | degenerate: integrated form needed | — |

Reading: the criterion **discriminates** — it does not say "contraction fails"; it says "growing $\zeta$ while
$\epsilon=O(1)$ fails". Ekpyrosis (contracting, $\epsilon\gg3$) passes because $\zeta$ sits on its constant mode;
USR (expanding, $\dot\zeta\neq0$) passes because $\epsilon\ll1$; the matter-like contraction ($1<\epsilon<3$, growing
$\zeta$, $\epsilon=O(1)$) is the unique corner where both ingredients are present, and there the failure is
$5\epsilon(9-\epsilon)/18$ in the monopole — $25/8$ at $\epsilon=3/2$, i.e. a factor $8/3$ in $f_{\rm NL}$.

Scope of what was actually computed (honest): (i) the linear criterion (1.2) is exact for any single-field history
with a growing-mode initial condition, any $c_s$; (ii) the second-order $f_{\rm map}$ is exact for constant $\epsilon$,
$c_s=1$, $1<\epsilon<3$ (frozen input, not re-solved here); (iii) the USR second-order statement is structural
(every frozen kernel $\propto\epsilon$; `all_map_pieces_carry_eps = true`), not a re-solve with $\epsilon(t)$;
(iv) the ekpyrotic check is a mode-dominance argument, no new constraint solve; (v) general-$w$ is substitution
$\epsilon=\tfrac32(1+w)$ into (ii), valid for the scalar-field realisation ($c_s=1$), not for a genuine fluid with
$c_s^2=w$ — that extension needs the $c_s$-dependent second-order constraints (open, bounded, \$0).

## 4. Placement against the literature (what each paper knows; what is new here)

| paper | what it establishes | what this note adds relative to it |
|---|---|---|
| Namjoo–Firouzjahi–Sasaki 2013, arXiv:1210.3692 | USR violates Maldacena's consistency relation, $f_{\rm NL}=5/2$; $\delta N$ reproduces it only with $N(\phi,\dot\phi)$ (growing mode needs the momentum) | Identifies a **second, independent** failure mode of $\delta N$ in non-attractors — the threading map $\delta N_c\ne\zeta_{\rm Mald}$ — controlled by $\langle\epsilon\rangle_\zeta$, not by the initial data; shows it is $O(\epsilon)$ in USR (hence invisible in their test, §1.1 exact) and $O(1)$ in contraction |
| Chen–Firouzjahi–Namjoo–Sasaki 2013, arXiv:1301.5699 | $P(X)$ non-attractor, $f_{\rm NL}=\tfrac{5(1+c_s^2)}{4c_s^2}$, $\delta N$ with momentum agrees | Linear criterion carries $c_s$ explicitly ($\langle\epsilon/c_s^2\rangle_\zeta$); their agreement is again the $\epsilon\to0$ corner; the $c_s$-dependent second-order map is stated as the open extension |
| Pajer–Schmidt–Zaldarriaga 2013, arXiv:1305.0824 | In attractors the squeezed limit is a coordinate effect of the long mode; observed squeezed bispectrum vanishes | Attractor = $\Theta=0$ = identity map, so there $\delta N_c=\zeta_{\rm Mald}$ and the only question is observability; in the $\Theta=O(1)$ phase the two curvature variables already differ at $O(1)$ **before** any observability argument, by a time-dependent non-local map along the fluid worldline |
| Dai–Pajer–Schmidt 2015, arXiv:1504.00351 | Conformal Fermi coordinates: local observer's frame removes the long mode's $O(k^0)$ and $O(k)$ effects (attractor, constant $\zeta$) | Not a CFC construction. The note supplies the input a CFC-type treatment of a non-attractor would need: the long mode's comoving shift has $O(k^0)$ divergence $\epsilon\dot\zeta_L$, so the local frame is displaced by $\int N_L\,dt$ and dilated by $\tfrac13\int\partial_iN^i_L\,dt=(\epsilon/3)\zeta_L$; the pure translation contributes no monopole (threading note §2) |
| Cai, Chen, Namjoo, Sasaki, Wang, Wang 2018, arXiv:1712.09998 | Post-USR transition dynamics of $f_{\rm NL}$; $\delta N$ and in-in agree through smooth/sharp transitions (inflation, $\epsilon\ll1$) | Explains *why* they agree (threading term $O(\epsilon)$ throughout) and predicts the regime where they would not: $\epsilon=O(1)$ during growth |
| Bravo–Mooij–Palma–Pradenas 2018, arXiv:1711.02680 (generalized consistency relation) and arXiv:1711.05290 (vanishing observable local $f_{\rm NL}$ in canonical single field) | Non-attractor squeezed limits obey a generalized consistency relation; the USR local $f_{\rm NL}$ is removable by the long mode's effect on physical coordinates | Their removal manipulations are $O(\epsilon)$-controlled in inflation; in a contraction with $\langle\epsilon\rangle_\zeta=O(1)$ the map between the fluid-congruence variable and $\zeta_{\rm Mald}$ is $O(1)$ and explicit ($\lambda$, $f_{\rm map}$); whether a physical-coordinate argument removes the in-in $-35/16$ is a separate question, left open and not claimed |
| Passaglia–Hu–Motohashi 2019, arXiv:1812.08243 | $\delta N(\phi,\pi)$ vs in-in agreement for PBH-motivated USR and transitions | Same as for Cai et al.: agreement is the $\epsilon\ll1$ corner of the criterion |
| Artigas–Grain–Vennin 2022, arXiv:2110.11720; Jackson et al. 2023, arXiv:2311.03281 | Separate-universe (phase-space) breakdown at SR$\to$USR transitions in inflation, on a finite window of super-Hubble scales, from momentum/initial-data mismatch | Different mechanism and different order: here the failure is $O(k^0)$ (all super-Hubble scales), $O(1)$ in amplitude, and comes from the threading (shift divergence), not from the transition; it is present at constant $\epsilon$ with no transition at all |
| Lyth–Malik–Sasaki 2005, astro-ph/0411220; Salopek–Bond 1990 | $\delta N=\zeta$ from the gradient expansion under $N_i=O(\nabla)$ | The criterion is exactly the condition under which that assumption holds at $O(k^0)$: $\Theta=\epsilon\dot\zeta_L/(H\zeta_L)\to0$ |
| Creminelli–Nicolis–Zaldarriaga 2004 (ekpyrotic attractor) | In single-field ekpyrosis the constant $\zeta$ mode dominates; consistency relation holds | Reproduced by the criterion (dominant mode has $\Theta=0$); the note's failure is confined to $1<\epsilon<3$ growing-$\zeta$ contractions |

**What is first-of-kind here, as far as the checked literature goes:** (a) a stated, quantitative criterion
($\langle\epsilon/c_s^2\rangle_\zeta$, eq. 1.2) for the $O(1)$ breakdown of the isotropic separate universe that
separates the threading failure from the Namjoo–Firouzjahi–Sasaki initial-data failure; (b) its evaluation showing
the inflationary non-attractor literature could not have seen it ($O(\epsilon)$); (c) the explicit $O(1)$
correction $\lambda$, $f_{\rm map}$ in a contracting non-attractor with the general-$w$ form. Not claimed as new:
the exact identity's ingredients (ADM), the USR $5/2$, the attractor consistency relation, the ekpyrotic attractor.

## 5. Sentences a short PRD-style note could claim (N3 only where the table supports it)

1. "The isotropic separate-universe ($\delta N$) construction reproduces the squeezed bispectrum of the comoving
   curvature perturbation if and only if the $\zeta$-growth-weighted mean of $\epsilon/c_s^2$ vanishes; the failure
   is linear in that mean." — **N3-shaped** (criterion; not found stated in the checked literature).
2. "In a contracting phase with constant $\epsilon\in(1,3)$ the separate-universe variable is
   $\delta N_c=(1-\epsilon/3)\zeta$ and its squeezed amplitude is $-5$ for every $\epsilon$, while the comoving $\zeta$
   has $f_{\rm NL}=\tfrac{5}{12}(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12)$; the two are related exactly by the
   threading map." — **N3-shaped** (first explicit $O(1)$ correction in a contraction), conditional on the in-in
   input standing (it is lab-derived twice; Cai+2009 $\times2$ located).
3. "Inflationary ultra-slow-roll evades the failure because $\epsilon\ll1$ while $\zeta$ grows, not because the
   comoving shift is small — the shift is $O(1/k_L)$ there too." — **N2/N3 boundary** (a reinterpretation of known
   agreement; new statement, no new number).
4. "Ekpyrotic contraction evades it because $\zeta$ sits on its constant mode." — **N2** (CNZ 2004 restated through
   the criterion).
Do **not** claim: that the in-in $-35/16$ is "the observable", that CFC removes/does not remove it, or anything about
$c_s\neq1$ at second order.

## 6. VERDICT — **CRITERION ESTABLISHED** (linear order exact and general; second order exact at constant $\epsilon$)

Criterion: $\delta N$ (isotropic, with $N(\phi,\pi)$) $=$ in-in squeezed limit of $\zeta_{\rm Mald}$ **iff**
$\langle\epsilon/c_s^2\rangle_\zeta\to0$; otherwise $\delta N_c=(1-\langle\epsilon/c_s^2\rangle_\zeta/3)\zeta$ and, at constant
$\epsilon$, $f_{\delta N}=f^{\rm in\text{-}in}/(1-\epsilon/3)-\tfrac{5\epsilon}{4}(1-\mu^2)$; general $w$:
$\lambda=\tfrac{1-w}{2}$, $f_{\rm map}=-\tfrac{15}{8}(1+w)(1-\mu^2)$. Validated on dust ($O(1)$ failure, $25/8$),
USR (agreement to $O(\epsilon)$, exact linear $\lambda_{\rm USR}=1+\tfrac{\epsilon_f}{3}-\tfrac{\sqrt{\epsilon_s\epsilon_f}}{3}$),
attractor (identity), plus ekpyrosis as the discriminating contracting control. Limits of the claim: §3 (i)–(v).

**Proposed ledger row 16 (orchestrator adds):** `16 | Separate-universe failure criterion (lift #2 of C2): <eps/c_s^2>_zeta
criterion, general-w lambda/f_map, 3 validations + ekpyrotic control | DONE 2026-09-04 (this note, script sha 21668ab6,
json 4e2a49be) | open: c_s-dependent second-order map; eps(t) re-solve for USR at second order; short methods note draft`.

Artifacts: `separate_universe_failure_criterion_2026_09_04.py` (sha256 `21668ab67711…`), `.json` (`4e2a49be541a…`),
manifest `reproducibility/manifests/experiments/lift2-separate-universe-failure-criterion.json`. Local CPU, \$0, 0.2 s.
