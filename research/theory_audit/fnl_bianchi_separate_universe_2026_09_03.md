# A3-2 — Bianchi-I separate-universe cross-check of the matter-contraction $f_{\rm NL}$

**NEXT_SCIENCE_LEDGER #1 (open item) / #3 (A3-2) · 2026-09-03 · BigBounce theory-audit lane**

Artifacts
- script: `research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.py`
  (sha256 `cc393a1236869745236923a90e168b6126a21f9011eeb38f5d6a47079fa2aac4`)
- result: `research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.json`
- manifest: `reproducibility/manifests/experiments/a3-2-fnl-bianchi-separate-universe.json`
- venue: local CPU · \$0 · wall clock ≈ 4 s · deterministic exact sympy

---

## VERDICT — **DISAGREES**, and it **falsifies the reconciliation mechanism**

The anisotropic (Bianchi-I) separate universe, carrying the long mode's shear at
leading order, gives

$$f_{\rm NL}^{\rm sq}(\mu)\;=\;-5+\frac{5\epsilon}{12}\,(3\mu^2-1)
\;\overset{\epsilon=3/2}{=}\;-\frac{45}{8}+\frac{15}{8}\mu^2,$$

against the in-in $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$:

| quantity | this work (Bianchi-I SU) | in-in (2026-09-02) | ratio / gap |
|---|---|---|---|
| monopole (angle average) | $-5$ | $-15/8$ | gap $-25/8$ |
| $\mu^2$ coefficient | $15/8$ | $15/16$ | **exactly $2\times$** |
| $P_2(\mu)$ coefficient | $5/8$ | $5/16$ | exactly $2\times$ |
| isoceles ($\mu=0$) | $-45/8$ | $-35/16$ | — |

**The shear finding (the point of the exercise).** The adjudication is *right about
the order*: the long mode's shear is $\mathcal O(k_L^0)$, not $\mathcal O(k_L^2)$.
Explicitly, in comoving gauge with $\psi=-\zeta/H+a^2\epsilon\,\partial^{-2}\dot\zeta$,
the $1/k_L^2$ of $\partial^{-2}$ cancels the $k_ik_j$ of $\partial_i\partial_j\psi$ and

$$\sigma^i{}_j=\varsigma\,\epsilon\dot\zeta_L\Big(\hat k_i\hat k_j-\tfrac13\delta_{ij}\Big),
\qquad
\beta_z\equiv\!\int\!\sigma^z{}_z\,dt=\varsigma\,\frac{2\epsilon}{3}\,\zeta_L
\;\overset{\epsilon=3/2}{=}\;\varsigma\,\zeta_L ,$$

($\varsigma=\pm1$ is the $\partial^{-2}\to\mp1/k^2$ sign convention; see §4). The
accumulated anisotropy of the local scale factors is therefore **as large as the
long mode itself** — a genuinely $\mathcal O(1)$ tidal background, which is why
this check was worth doing.

**But it cannot do the job it was assigned.** The shear is *traceless*. Its
squeezed response is exactly $\propto(3\mu^2-1)$, whose angular average is zero,
so it contributes **identically zero monopole** (computed, not asserted:
`comparison.shear_monopole_contribution == 0`). The residual it was supposed to
carry — comoving $\delta N$ $(-5)$ vs the in-in monopole $(-15/8)$, i.e. $-25/8$ —
is a *monopole*. No traceless linear-in-$\zeta_L$ response can produce it. The
2026-09-02 statement "the residual is carried by the long mode's shear, not
$\mathcal O(k^2)$" is therefore **half right (order) and wrong (mechanism)**.

**What this does *not* say.** It does not overturn $-35/16$. This route computes a
gradient-expansion *response* of the short-mode power spectrum, not the
bispectrum; the in-in remains the only complete calculation, and the two objects
differ by exactly the terms a leading-order separate universe drops. What is
established is that the *stated reconciliation* fails, so ledger #1's closure note
must be amended: the $\delta N$–in-in gap is still **unexplained**.

---

## 1. What was computed (each step derived, nothing quoted)

1. **Background.** Constant $\epsilon$: $a\propto|t|^{1/\epsilon}$, $H=1/(\epsilon t)$;
   $\epsilon=-\dot H/H^2$ re-derived from $H$ (assert).
2. **Growing mode.** $\zeta_D\propto|t|^{1-3/\epsilon}$, verified to solve the exact
   super-horizon equation $\tfrac{d}{dt}(a^3\epsilon\dot\zeta)=0$ (assert); gives
   $\dot\zeta=(\epsilon-3)H\zeta$, i.e. $-\tfrac32H\zeta$ at $\epsilon=3/2$ —
   the non-attractor mode, matching Cai's Eq. (25).
3. **Shear.** ADM comoving gauge, $h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N_i=\partial_i\psi$,
   $K^i{}_j=(H+\dot\zeta)\delta^i{}_j-\partial_i\partial_j\psi/(a^2e^{2\zeta})$. Only the
   $a^2\epsilon\partial^{-2}\dot\zeta$ piece of $\psi$ survives $k_L\to0$; the $-\zeta/H$
   piece is $\mathcal O(k_L^2)$ and drops. Result above.
4. **Accumulated anisotropy.** With $h_{ij}=a^2e^{2\lambda_i}$ one has
   $K^i{}_j=(H+\dot\lambda_i)\delta^i{}_j$, hence $\dot\beta_i=\sigma^i{}_i$ and, on the
   pure growing mode, $\beta_z=(2\epsilon/3)\varsigma\,\zeta_L$.
5. **Isotropic response = comoving $\delta N$, rederived independently here.**
   Exponential potential $\lambda^2=2\epsilon$, $x=\dot\phi/(\sqrt6H)$,
   $dx/dN=(1-x^2)(\sqrt6\lambda/2-3x)$, $d\phi/dN=\sqrt6x$; flat initial slice,
   uniform-$\phi$ final slice, growing-mode displacement $u_i=x_i-x_*$ only;
   second-order solution with the ODE residual verified $0$; growing-mode-dominated
   limit. Output: $f^{\delta N}_{\rm comoving}=-5$ for **all** $\epsilon$ — an
   independent reproduction of the 2026-09-02 value by a different parametrisation
   (that work integrated in $s=\ln|H|$; this one in $\phi$).
6. **Projection onto the global comoving grid.** The short-mode correlations are
   isotropic in the local Bianchi-I frame, $\tilde x_i=e^{\lambda_i}x_i$ with
   $\lambda_i=\zeta_L+\beta_i$, so
   $P_{\rm glob}(\mathbf k)=e^{-\sum_i\lambda_i}P_{\rm loc}(\tilde k)$,
   $\tilde k_i=e^{-\lambda_i}k_i$, $P_{\rm loc}=Ak^{n_s-4}$:
   $$\delta\ln P=-\sum_i\lambda_i-(n_s-4)\sum_i\hat k_i^2\lambda_i
   =\underbrace{(1-n_s)\zeta_L}_{\text{isotropic}}+\underbrace{\tfrac{4-n_s}{2}\beta_z(3\mu^2-1)}_{\text{shear}} .$$
7. **Assembly.** $f_{\rm NL}^{\rm sq}=\tfrac5{12}\,\partial\ln P_s/\partial\zeta_L$
   (normalisation fixed by requiring the attractor limit to be Maldacena's
   $\tfrac5{12}(1-n_s)$), $n_s=1$ exactly for the matter contraction.

## 2. Validation (all asserts in the script; the run fails if any breaks)

| check | why | result |
|---|---|---|
| $\epsilon$ recovered from $H$; $\zeta_D$ solves $\tfrac{d}{dt}(a^3\epsilon\dot\zeta)=0$ | background + mode are the right ones | PASS |
| isotropic part of $\delta\ln P$ $=(1-n_s)\zeta_L$ | Maldacena consistency relation on an attractor; fixes the $5/12$ | PASS |
| attractor ($\dot\zeta=0\Rightarrow\sigma=0$): $f=\tfrac5{12}(1-n_s)$, **no quadrupole** | single-field squeezed limit has no $\mathcal O(k_L^0)$ tide | PASS |
| USR ($\epsilon\to0$): shear $\propto\epsilon\to0$, pure monopole | Namjoo–Firouzjahi–Sasaki's $5/2$ is angle-independent; a shear term surviving there would be wrong | PASS |
| comoving $\delta N$ ODE residual at $\mathcal O(u_i^2)$ | second-order solution | $\equiv0$ |
| $f^{\delta N}_{\rm comoving}=-5$, all $\epsilon$ | independent reproduction of the 09-02 value | PASS |

The USR check is the sharp one: it is the only known non-attractor benchmark, and
it constrains the shear term to vanish there — which the derived
$\sigma\propto\epsilon\dot\zeta$ does, automatically.

## 3. Two exact coincidences, recorded as leads, **not** claims

- $\dfrac{15/8}{15/16}=2$ exactly: the tidal quadrupole is exactly twice the in-in one.
- this work $-$ in-in $=\;-\tfrac{55}{16}+\tfrac{15}{16}\mu^2$, and $-55/16$ is
  precisely the uniform-density $\delta N$ value of the second method.

Factors of two ($\zeta_\rho=2\zeta_c$; Cai's amplitude step; now the quadrupole)
keep recurring in this problem. No mechanism is claimed here, and no step was
adjusted to produce or remove any of them.

## 4. Honest incompleteness (what would close this)

1. **Sign convention $\varsigma$ is not independently pinned.** Deriving
   $\partial^{-2}\to-1/k^2$ (the standard convention) gives $\varsigma=-1$ and a
   *negative* quadrupole $-\tfrac{15}8\mu^2$; the 2026-09-02 adjudication quotes
   $\sigma=+\epsilon\dot\zeta(\hat k\hat k-\delta/3)$, i.e. $\varsigma=+1$, matching the
   in-in's sign. Both are carried symbolically here. Neither of the two available
   benchmarks (de Sitter, USR) has any shear, so the sign is **not cross-validated**
   by this work. It does not affect the verdict (the magnitudes and the zero
   monopole are $\varsigma$-independent).
2. **The projection prescription in a non-attractor background is the weak joint.**
   Evaluating $\beta_i$ at the end of contraction and treating the local frame as an
   anisotropically rescaled FRW patch is the standard conformal-Fermi-coordinate
   move (Pajer–Schmidt–Zaldarriaga 2013; Dai–Pajer–Schmidt 2015), but those
   constructions are set up for attractor backgrounds where the shift's effect on
   short modes is a genuine gauge mode. Here $\dot\zeta_L\ne0$ and the advection
   term $N^i\partial_i$ acts on super-Hubble short modes too; whether it produces an
   additional $\mu$-independent contribution is **not settled by this work**.
   That is the only identified route by which a monopole could still appear at
   $\mathcal O(\zeta_L)$ — and it is not shear.
3. **The dynamical (as opposed to projection) shear effect is separately
   negligible**, by a one-line argument recorded here: the anisotropy enters the
   short-mode equation only through $k_{\rm eff}^2$, so its effect on a super-Hubble
   short mode is $\mathcal O(k_s^2\eta_B^2)\to0$; the shear matters only through the
   projection above. This is *why* the whole effect is a pure quadrupole.

## 5. Consequence for the ledger

- Ledger #1's closure text says the $\delta N$/in-in residual "is carried by the
  long mode's shear, not $\mathcal O(k^2)$". **Amend:** the shear is indeed
  $\mathcal O(k_L^0)$ and does generate the $\mu^2$ quadrupole (within a factor 2),
  but it is traceless and provably supplies no monopole; the $-25/8$ monopole gap
  between comoving $\delta N$ and the in-in remains **open and unexplained**.
- The flagship value $-35/16$ still rests on the single from-scratch in-in
  computation (itself validated on de Sitter and USR). This work does not confirm
  it by a second route. The honest statement remains the one in the second-method
  §8: the amplitude is $\mathcal O(\text{few})$ and negative robustly; the exact
  rational rests on the in-in route alone.
- Next concrete step (successor to A3-2): resolve incompleteness item 2 — a CFC
  construction valid on a non-attractor background, i.e. transform the in-in
  squeezed kernel into conformal Fermi coordinates and read off which parts are
  projection and which are physical response. That is a bounded calculation and it
  would either produce the missing $-25/8$ or localise the error.

## 6. Integrity note

No step was adjusted to land on $-35/16$; the disagreement is the primary
reported finding. The two literature values are used only in §3 and the
comparison table, after the computation. Every structural claim is an executed
assertion in the script. Items that could not be settled are in §4, stated as
unsettled.

## References
Maldacena astro-ph/0210603 · Creminelli & Zaldarriaga astro-ph/0407059 ·
Namjoo, Firouzjahi & Sasaki 1210.3692 · Pajer, Schmidt & Zaldarriaga 1305.0824 ·
Dai, Pajer & Schmidt 1504.00351 · Cai, Xue, Brandenberger & Zhang 0903.0631 ·
Li, Quintin, Wang & Cai 1612.02036 · lab: `fnl_matter_contraction_adjudication_2026_09_02.*`
(aa2987cf), `fnl_matter_contraction_second_method_2026_09_02.*` (d7dac953).
