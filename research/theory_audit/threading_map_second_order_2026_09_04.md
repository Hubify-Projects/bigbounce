# Threading map at second order: Maldacena's comoving $\zeta$ vs the zero-shift $\delta N_c$ in a non-attractor contraction

**BigBounce theory-audit lane · 2026-09-04 · NEXT_SCIENCE_LEDGER row 11(c)**

## Plan (written first, anti-stall)

Goal: derive the mechanism behind the identity recorded in
`fnl_monopole_adjudication_2026_09_03.md` §4:
$[L]-\delta N_c = 5\epsilon/4 = (5/12)(3\epsilon)$, i.e. the second-order part of the
threading map from Maldacena's comoving gauge ($N_i=\partial_i\psi$, $\psi\supset a^2\epsilon\,\partial^{-2}\dot\zeta$,
$O(1/k_L)$) to the zero-shift threading in which the isotropic separate universe computes
$\delta N_c=(1-\epsilon/3)\zeta$.

Steps (each committed by explicit path as it lands):
1. Set up the coordinate transformation $x^i\to \tilde x^i = x^i+\xi^i(t,x)$ that removes the long
   mode's shift; compute $\xi^i$ on the growing mode; show $\xi$ is $O(1/k_L)\times\zeta_L$ so $k_L\xi=O(1)$.
2. Transform the short-mode curvature perturbation to second order: the argument shift
   $\zeta_S(x)\to\zeta_S(x+\xi)$ (pure translation) plus the Jacobian/dilation piece
   $\partial_i\xi^i$ and the time re-threading of the slicing. Identify which pieces survive at
   $O(k_L^0)$ in the squeezed limit.
3. Compute the induced squeezed bispectrum contribution of each piece in the adjudication's
   conventions ($B_{\rm sq}=(12/5)f\,P_LP_S$, $\mu=\hat k_L\cdot\hat k_S$), general constant $\epsilon$.
4. Validate in sympy: $\epsilon=3/2$ gives $5/4$; general $\epsilon$ gives $5\epsilon/4$; attractor
   $\epsilon\to0$ (constant $\zeta$, $\dot\zeta_L\to0$) gives 0 with the Maldacena consistency
   relation untouched; USR if tractable.
5. Verdict + Appendix-A paragraph; script + json; manifest; ledger row 11(c) line.

(Derivation, validation and verdict follow below as they are completed.)

---

## 1. Setup and the exact threading identity

Comoving gauge ($\delta\phi=0$), Maldacena variables: $h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N=1+\alpha$,
$N_i=\partial_i\psi+\tilde N_i$; at first order $\alpha=\dot\zeta/H$, $\psi=-\zeta/H+\chi$,
$\partial^2\chi=a^2\epsilon\dot\zeta$. For a scalar field the $\delta\phi=0$ slices are orthogonal to the
fluid four-velocity, so the **zero-shift threading is the fluid (normal) congruence**, $n^\mu=(1/N,-N^i/N)$,
$dx^i/dt=-N^i$ — not the comoving coordinate lines $x^i={\rm const}$, which carry the shift.

The expansion of the normal congruence is $K=\nabla_\mu n^\mu=\frac{1}{N\sqrt h}\big[\partial_t\sqrt h-\partial_i(\sqrt h\,N^i)\big]$.
Along a fluid worldline, $\frac{d}{dt}\ln\sqrt h=\partial_t\ln\sqrt h-N^i\partial_i\ln\sqrt h$, hence the
**exact** (fully nonlinear) identity
$$
N K=\frac{d}{dt}\ln\sqrt h\Big|_{\rm worldline}-\partial_iN^i .\tag{1}
$$
The separate universe's variable is the local e-fold number of the fluid congruence, $\delta N_c=\int\frac{K}{3}N\,dt-\bar N$,
from the asymptotically flat comoving slice at $t\to-\infty$ (growing mode, $\zeta\to0$) to the final comoving
slice. With $\ln\sqrt h=3\ln a+3\zeta$, (1) gives the threading map in closed form:
$$
\boxed{\;\delta N_c(x_f)=\zeta(t_f,x_f)-\frac13\int_{-\infty}^{t_f}\partial_iN^i\big(t,x(t)\big)\,dt,\qquad \dot x^i=-N^i,\ x(t_f)=x_f\;}\tag{2}
$$
Every difference between $\zeta_{\rm Mald}$ and $\delta N_c$ is the divergence of the shift integrated along the
fluid worldline: (i) $\partial_iN^i$ itself, to second order (needs the second-order lapse and shift from the exact
ADM constraints); (ii) its evaluation along the worldline displaced by the long mode,
$x(t)=x_f+\Delta(t)$, $\Delta^i(t)=\int_t^{t_f}N_L^i\,dt'$; (iii) the choice of label (final position $x_f$ vs
initial position $x_i=x_f+\Delta(-\infty)$), a rigid translation of the whole final field.

**Linear order.** $N^i=a^{-2}\partial_i\psi$, $\partial_iN^i=\epsilon\dot\zeta-\partial^2\zeta/(a^2H)\to\epsilon\dot\zeta$
on super-Hubble scales, so $\delta N_c=\zeta-\frac{\epsilon}{3}\int\dot\zeta\,dt=(1-\epsilon/3)\,\zeta$
for constant $\epsilon$ — the adjudication's linear factor, now obtained from (2) rather than from
"Friedmann + lapse" (the two are the same statement: the Hamiltonian constraint is the local Friedmann equation).

## 2. What a pure translation can and cannot do (exact, before any computation)

Let the short modes be rigidly translated by the long mode's displacement, $\zeta_S(x)\to\zeta_S(x+\Delta_L)$,
$\Delta_L(k)=i\,c\,\hat k\,\zeta_L(k)/k$ with $c=O(\epsilon)$ (so $k_L\Delta_L=O(\zeta_L)$, the $1/k_L$ of the shift
cancelled by one gradient). In the bispectrum the two short legs give, with $p=k_S-\tfrac12k_L$, $q=-k_S-\tfrac12k_L$
and $\mu=\hat k_L\cdot\hat k_S$,
$$
\frac{B_{\rm transl}}{P_LP_S}=-\frac{c}{k_L}\,\hat k_L\cdot\big[q\,P(q)+p\,P(p)\big]\Big/P(k_S)
= c\,\big[1+(n_s-4)\mu^2\big]+O(k_L/k_S)\;\xrightarrow{n_s=1}\;c\,(1-3\mu^2).\tag{3}
$$
The individual legs carry $O(k_S/k_L)$ poles; they cancel between the legs (the $P(p)-P(q)$ difference is
$O(k_L)$ and multiplies the pole). **The angular average of (3) vanishes for a scale-invariant spectrum**: a
translation cannot change an isotropically averaged equal-time correlator. Hence *no* pure pair-translation can
supply a monopole; the adjudication's bookkeeping "$i(p-k_L)\cdot\xi+i(q-k_L)\cdot\xi=-3i\,k_L\cdot\xi$" dropped
the $P(p)-P(q)$ pole-cancellation term and mis-assigned the momentum carried by $\xi$; its "$(5/12)(3\epsilon)$" is
therefore a numerical coincidence, not a translation. What a position-dependent translation *does* produce is the
quadrupole $-3c\,\mu^2$ (and, for $n_s\neq1$, a dilation monopole $c\,(n_s-1)/3$): it is the shear/dilation of the
displacement field $\partial_i\Delta_j=c\,\hat k_i\hat k_j\zeta_L$, not the translation itself.

The rest of this note computes every term of (2) exactly (script) and identifies where the monopole comes from.

## 3. The map at second order (computed exactly; script §"threading map")

The script solves the **exact ADM Hamiltonian and momentum constraints** to second order in the $L\times S$ cross
term (second-order lapse $\alpha_2$, scalar shift $\psi_2$ and transverse shift $\tilde N_i$ at wavevector
$k_L+k_S$; the first-order Maldacena solution is verified to satisfy the constraints identically, all $k$), forms
$\partial_iN^i=\partial_i(h^{ij}N_j)$ with $h^{ij}=a^{-2}e^{-2\zeta}\delta^{ij}$, takes the super-Hubble limit
($k_L,k_S\ll aH$ jointly; the long mode's shift is $O(1/k_L)$ and is kept), and integrates (2) along the fluid
worldline. Writing $\delta N_c^{(2)}=\mathcal M\,\zeta_L\zeta_S$ at $t_f$ (end-time independent on the growing
mode $m=3/\epsilon-1$), the kernel has five pieces of distinct geometric origin:

| piece | origin in (2) | kernel $\mathcal M$ | $f_{\rm NL}$ contribution ($\delta N_c$ normalisation) | monopole |
|---|---|---|---|---|
| `zlap` | $-2\zeta\,\partial^2\psi$ from $e^{-2\zeta}$ in $N^i=h^{ij}N_j$ (long $\times$ short both ways) | $2\epsilon/3$ (local) | $\dfrac{5\epsilon}{(3-\epsilon)^2}$ | $\dfrac{5\epsilon}{(3-\epsilon)^2}$ |
| `psi2` | second-order scalar shift $\partial^2\psi_2/a^2$ (constraints) | non-local, $O(k_S/k_L)$ poles | $\dfrac{5\epsilon(-2\epsilon^2+11\epsilon-24)}{8(3-\epsilon)^2}+\dfrac{5\epsilon(2\epsilon^2-9\epsilon+12)}{8(3-\epsilon)^2}\mu^2$ | $\dfrac{5\epsilon(-\epsilon^2+6\epsilon-15)}{6(3-\epsilon)^2}$ |
| `grad` | $-2\partial_i\zeta\,\partial_i\psi_1/a^2$ | $\epsilon\mu(k_L^2+k_S^2)/(3k_Lk_S)$ | $\dfrac{-5\epsilon}{4(3-\epsilon)^2}+\dfrac{15\epsilon}{4(3-\epsilon)^2}\mu^2$ | **0** |
| `wl_fin` | $\partial_iN^i_S$ read along the worldline displaced by $\Delta_L(t)=\int_t^{t_f}N_L\,dt'$ | $-\epsilon^2k_S\mu/(6k_L)$ | $\dfrac{5\epsilon^2}{8(3-\epsilon)^2}-\dfrac{15\epsilon^2}{8(3-\epsilon)^2}\mu^2$ | **0** |
| `lab_init` (+`wl_initextra`) | rigid translation $x_f\to x_i$ (initial-position label) | $-\epsilon k_S\mu/k_L$ | $\propto(1-3\mu^2)$, eq. (3) with $c=\epsilon$ | **0** |

**Totals.** Final-position label: $f_{\rm map}=-\tfrac{5\epsilon}{4}+\tfrac{5\epsilon}{4}\mu^2$, monopole $-5\epsilon/6$.
Initial-position label (the separate-universe label): monopole again $-5\epsilon/6$; the quadrupole changes by the
translation term only. Every $1/k_L$ pole cancels between the two short legs (asserted), exactly as in §2.

The linear factor from (2) for a **general** history $\zeta\propto\tau^{-m}$ ($m>0$) is $\delta N_c/\zeta=1-\epsilon/3$,
independent of $m$; and every cross kernel carries an explicit factor $\epsilon$.

## 4. Closure against the in-in result (read only after the map was frozen)

With $B_{\delta N_c}=\lambda^3B_\zeta^{\rm in\text{-}in}+\lambda^2P_L[\mathcal M(k_L,q)P(q)+\mathcal M(k_L,p)P(p)]$,
$\lambda=1-\epsilon/3$, $f_{\delta N_c}=f^{\rm in\text{-}in}/\lambda+f_{\rm map}$, and the adjudication's
$f^{\rm in\text{-}in}(\mu,\epsilon)=\tfrac{5}{12}(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12)$:
$$
f_{\delta N_c}^{\rm (initial\ label)}=-5\quad\text{exactly, isotropic, for every constant }\epsilon;\qquad
f_{\delta N_c}^{\rm (final\ label)}=-\frac{15(\epsilon-4)}{4(\epsilon-3)}+\frac{15\epsilon}{4(3-\epsilon)}\mu^2
\ \ (\text{monopole }-5).\tag{4}
$$
At $\epsilon=3/2$: $-5$ (initial label) and $-\tfrac{25}{4}+\tfrac{15}{4}\mu^2$ (final label). The isotropic separate
universe's $-5$ is therefore **the bispectrum of the fluid-congruence e-fold variable labelled by initial position,
obtained from the in-in $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ through (2)** — the two methods agree exactly once the
variable is matched; there was never a discrepancy in the physics, only in the variable. Inverting (4) reproduces
the adjudication's general-$\epsilon$ in-in monopole $-5(\epsilon-3)(\epsilon-6)/18$ (asserted).

**The gap, decomposed honestly** ($f^{\rm in\text{-}in}_{\rm mono}-f_{\delta N_c}=5\epsilon(9-\epsilon)/18$):
$$
\underbrace{5(1-\lambda)}_{\text{linear rescaling: }5\epsilon/3}\;+\;\underbrace{(-\lambda f_{\rm map,mono})}_{\text{second-order map: }5\epsilon(3-\epsilon)/18}
\;=\;\frac{5\epsilon(9-\epsilon)}{18}.\tag{5}
$$
Neither summand is $5\epsilon/4$, and no single map piece equals $5\epsilon/4$ in in-in normalisation
(`zlap` $=\tfrac{5\epsilon}{3(\epsilon-3)}$, `psi2` $=\tfrac{5\epsilon(-\epsilon^2+6\epsilon-15)}{18(\epsilon-3)}$, the
rest $0$; script key `five_eps_over_4_matches_a_map_term = []`). The adjudication's "$[L]-\delta N_c=5\epsilon/4$"
is the difference between a vertex-leg class of the in-in calculation and a differently-normalised variable; it is
not a term of the threading map, and — by §2 — it cannot be a pair translation, whose monopole is identically zero
(script: `pure_translation_init` monopole $0$, quadrupole $-\tfrac{45\epsilon}{4(3-\epsilon)^2}$).

## 5. Limits

- **Attractor** ($\dot\zeta=0$, $m=0$, any constant $\epsilon$): $\chi=0$, $N^i=-\partial_i\zeta/(a^2H)$, so
  $\partial_iN^i=O(k^2/a^2H^2)$ at linear *and* second order (script: `div_linear = 0`, `div_cross = 0` at
  $O(k^0)$). The map is the identity, $\delta N_c=\zeta_{\rm Mald}$, and Maldacena's consistency relation
  $f_{\rm NL}=\tfrac{5}{12}(1-n_s)$ is untouched — the $O(k^0)$ shift terms exist only while $\dot\zeta_L\neq0$.
- **USR-type** ($\epsilon\to0$ at fixed $\dot\zeta/\zeta$): every cross kernel is $O(\epsilon)$ (asserted), the linear
  factor is $1-\epsilon/3\to1$, and for USR proper ($\epsilon\propto a^{-6}$, $\zeta\propto a^3$)
  $\int\epsilon\dot\zeta\,dt=O(\epsilon)\zeta$; hence $\delta N_c=\zeta(1+O(\epsilon))$ and the known agreement
  $\delta N=$ in-in $=5/2$ (Namjoo–Firouzjahi–Sasaki 2012; adjudication §1) is consistent with (2). A full
  time-dependent-$\epsilon$ run was not attempted (the constant-$\epsilon$ solver would need the exact
  $a^3\propto\sinh$ background); the statement above is structural, not a re-derivation of $5/2$.
- **Kination** $\epsilon\to3$: $\lambda\to0$ and the map's $f$ contributions blow up as $(3-\epsilon)^{-2}$ while
  $f^{\rm in\text{-}in}_{\rm mono}\to0$: $\delta N_c$ ceases to be a usable variable exactly where the
  adjudication's monopole vanishes — consistent.

## 6. VERDICT — **MECHANISM DERIVED** (and the "pair-translation" reading refuted)

The second-order relation between Maldacena's comoving $\zeta$ and the zero-shift-threading $\delta N_c$ is the
exact identity (2): $\delta N_c$ differs from $\zeta$ by the divergence of the comoving shift integrated along the
fluid worldline. Solving the ADM constraints to second order and assembling the squeezed bispectrum, the in-in
result $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ maps to **exactly $-5$, isotropic, for every constant $\epsilon$** when
the patch is labelled by its initial position — the separate-universe answer — so the $\delta N$ value is
*derived from* the in-in value rather than merely explained away. The monopole gap $5\epsilon(9-\epsilon)/18$ is
(5): $5\epsilon/3$ from the linear renormalisation $\delta N_c=(1-\epsilon/3)\zeta$ plus
$5\epsilon(3-\epsilon)/18$ from two second-order terms — the $e^{-2\zeta}$ conformal factor in $N^i=h^{ij}N_j$
(local, kernel $2\epsilon/3$) and the second-order scalar shift $\psi_2$ (non-local). The recorded
"$[L]-\delta N_c=5\epsilon/4=(5/12)(3\epsilon)$" is **not** a term of the map and **not** a pair translation: a
translation of the short modes by $\Delta_L=\int N_L\,dt$ has zero monopole by translation invariance (eq. 3) and
only re-shuffles the quadrupole between labelling conventions (final-position label: $+\tfrac{15\epsilon}{4(3-\epsilon)}\mu^2$;
initial-position label: $0$). The coincidence arose from a momentum-bookkeeping slip in the adjudication's
translation estimate (the $P(p)-P(q)$ pole-cancellation term was dropped). The $[L]/[K]/[X]$ vertex classes and the
geometric pieces of (2) are different decompositions of the same number; only the totals are comparable.

**Appendix-A-ready paragraph.** *The isotropic separate universe computes the e-fold number of the fluid
congruence, $\delta N_c$, which is related to the comoving curvature perturbation by the exact identity
$\delta N_c(x_f)=\zeta(t_f,x_f)-\frac13\int^{t_f}\partial_iN^i\,dt$ along the fluid worldline $\dot x^i=-N^i$; in a
non-attractor phase the comoving shift $N_i=\partial_i\psi$, $\psi\supset a^2\epsilon\,\partial^{-2}\dot\zeta$, is
$O(1/k_L)$, so its divergence is $O(k^0)$ and the map is non-trivial: $\delta N_c=(1-\epsilon/3)\zeta$ at linear
order, with second-order terms from the conformal factor in $N^i=h^{ij}N_j$ and from the second-order shift.
Solving the ADM constraints to second order, the in-in squeezed limit
$f_{\rm NL}=\frac{5}{12}(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12)$ maps exactly to the separate-universe value
$f_{\rm NL}^{\delta N}=-5$ (isotropic, all constant $\epsilon$; initial-position label), so the two methods agree once
the variable is matched; the translation of the short modes by the long mode's displacement contributes no
monopole and only sets the quadrupole's labelling convention.*

## 7. Integrity note

Eq. (2), the constraint solver and the bispectrum assembly were written and frozen before any adjudication
number was substituted (the comparison section reads $f^{\rm in\text{-}in}$ only after the kernels are computed
and printed). All assertions are exact rational/symbolic (sympy 1.14.0); no coefficient was tuned. The label
dependence of the quadrupole is reported rather than chosen. Lane (C)'s Bianchi-I quadrupole ($\tfrac{15}{8}\mu^2$
at $\epsilon=3/2$) matches neither label here ($\tfrac{15}{4}\mu^2$ final, $0$ initial); that comparison is
outside this row and is recorded as an open note, not a finding.

Artifacts: `threading_map_second_order_2026_09_04.py` (sha256 `b0c934158add4ddec7fbf…`), `.json`
(`b961e8678c3e8eb291cf7…`), manifest `reproducibility/manifests/experiments/row11c-threading-map-second-order.json`.
Venue local CPU, \$0, wall clock ~3 min (constraint solve 105 s) · deterministic.
