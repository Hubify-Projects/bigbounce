# Adjudication: the squeezed-limit MONOPOLE of the matter-contraction $f_{\rm NL}$ — in-in ($-15/8$) vs comoving $\delta N$ ($-5$)

**BigBounce theory-audit lane · 2026-09-03 · independent adjudicator (NEXT_SCIENCE_LEDGER #1, reopened by A3-2)**

Artifacts
- script: `research/theory_audit/fnl_monopole_adjudication_2026_09_03.py` (sha256 `058447db00cb61978e05dd0503983ebbe29a558abfd94ad5270fd87e5c3880aa`)
- companion (general constant $\epsilon$): `fnl_monopole_adjudication_2026_09_03_general_eps.py` (sha256 `0c30afe73b8080e5443fa2af28461782a8a5a01bdebe147830f57f5563d447d7`)
- results: `fnl_monopole_adjudication_2026_09_03.json`, `fnl_monopole_adjudication_2026_09_03_general_eps.json`
- manifest: `reproducibility/manifests/experiments/p2-fnl-monopole-adjudication.json`
- venue: local CPU · \$0 · wall clock 15 s + 8 s · deterministic exact sympy

---

## VERDICT — **IN-IN MONOPOLE $-15/8$ CORRECT (isoceles $-35/16$), $\delta N$ DEFECT LOCATED**

For $\zeta$ *as defined* — Maldacena's comoving-gauge curvature perturbation, $h_{ij}=a^2e^{2\zeta}\delta_{ij}$ on uniform-$\phi$ slices, the variable of Cai+2009, Li+2016, Paper 2 and lane (A) — the squeezed limit at the end of the dust contraction is

$$
f_{\rm NL}^{\rm sq}(\mu)=-\frac{35}{16}+\frac{15}{16}\mu^2,\qquad \text{monopole }-\frac{15}{8},
$$

and it is **a zeroth-order-in-gradients ($k\to0$) quantity**: this work reproduces lane (A)'s in-in result *per vertex and for the full shape function* by a different organisation (the classical second-order super-Hubble solution with the $O(k^0)$ non-local shift terms kept; §1). The $\delta N$ value $-5$ is **not** the $f_{\rm NL}$ of this variable and **cannot** be: the isotropic separate universe computes the curvature perturbation in the *zero-shift threading*, $\delta N_c=\psi^{\rm zs}$, and in a non-attractor phase

$$
\delta N_c=\Big(1-\frac{\epsilon}{3}\Big)\zeta_{\rm Mald}\quad(\text{linear order; }=\tfrac12\zeta\text{ at }\epsilon=\tfrac32),
$$

because the comoving-gauge shift $N_i=\partial_i\psi$, $\psi\supset a^2\epsilon\,\partial^{-2}\dot\zeta$, is $O(1/k_L)$ — the gradient-expansion assumption "$N_i=O(\nabla)$" (literature: Lyth–Malik–Sasaki 2005, astro-ph/0411220, §2; Salopek–Bond 1990) fails. The shift's finite $O(k_L^0)$ remainders (class [X] below) supply **100 % of the quadrupole and $+5/4$ of the monopole**, with $1/k_L$ poles that cancel only in the sum over vertices; no separate universe (isotropic or Bianchi-I-with-projection) contains them. Located defect, at the equation level:

| quantity | value (this work) | origin |
|---|---|---|
| [L] long mode enters only as $\zeta_L,\dot\zeta_L$ (lapse/curvature) | $-25/8$, pure monopole | local response; general $\epsilon$: $5(\epsilon-4)/4$ |
| [K] long mode enters as $\partial_i\partial_j\tilde\chi_L$ (its $\delta K$ **and** shear) | **0** | the $T_4$ pieces cancel between varied legs |
| [X] long mode enters as $\partial_i\tilde\chi_L$ (its **shift**, $\propto1/k_L$) | $\tfrac{15}{16}+\tfrac{15}{16}\mu^2$ (monopole $5/4$) | $T_3$ bulk $+\tfrac{15}{8}\mu^2$, boundary $f_b$ $+\tfrac{15}{16}-\tfrac{15}{16}\mu^2$ |
| [S] long mode sourced by the short pair | 0 | suppressed |
| **total** | $-\tfrac{35}{16}+\tfrac{15}{16}\mu^2$ | $=$ lane (A) in-in exactly |
| comoving $\delta N$ (lanes A/B/C) | $-5$, isotropic | different variable ($\delta N_c$), no [X] |

So in-in monopole $-\,\delta N_c$ $=25/8$ $=$ [X]$_{\rm mono}$ $(5/4)$ $+$ ([L]$-\delta N_c$) $(15/8)$; in general $\epsilon$: $5\epsilon(9-\epsilon)/18$ $=$ $5\epsilon(9-2\epsilon)/36$ $+$ $5\epsilon/4$. The second piece is the second-order part of the threading map $\zeta_{\rm Mald}\to\delta N_c$; it is *recorded* as exactly the pure pair-translation coefficient $(5/12)(3\epsilon)$ (§4), a computed identity, not a claimed mechanism.

**Quadrupole (factor 2) resolved — real, not convention.** The in-in $\mu^2$ coefficient is $5\epsilon^2/12$ ($=15/16$); lane (C)'s projection gives $5\epsilon/4$ ($=15/8$); ratio $\epsilon/3$. The $T_3$ bulk coupling to the long mode's shift reproduces lane (C)'s $15/8\,\mu^2$ **exactly** (it is the dynamical anisotropic-rescaling effect lane (C) modelled), but the field-redefinition/boundary term $f_b=(\epsilon/2\mathcal H)[\partial\zeta\partial\tilde\chi-\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\tilde\chi)]$ — the final-time re-threading of the short modes by the long mode's shift, absent from lane (C) — subtracts $(1-\epsilon/3)\times\tfrac{5\epsilon}{4}\mu^2$ and adds the $+15/16$ monopole. Same $\mu$ definition throughout ($\mu=\hat k_L\cdot\hat k_S$); isoceles $\mu=0$.

---

## 1. The in-in leading term is the classical $O(k^0)$ super-Hubble solution (Q1, Q3)

Every vertex integral $\int_{-\infty(1-i0)}^{\eta_*}\eta^{-n}e^{iK\eta}d\eta$ reduces at leading order in $S=-\eta_*$ to its antiderivative at the upper limit; the commutator is the retarded Green's function of $(a^2\epsilon\zeta')'=0$, exact as $k\to0$ up to $O(k^2\eta^2)$; the particular solution of $2(a^2\epsilon\zeta^{(2)\prime})'={\delta S_3^{\rm bulk}}/{\delta\zeta_{-k}}$ with a source $\propto\eta^{-4}$ is the unique $\eta^{-6}$ term. The script solves this with $\zeta^{(1)}_k=Z_k\eta^{-3}$, adds $\zeta=\zeta_n+f(\zeta_n)$ at $\eta_*$, and forms $A=\tfrac12\sum_ik_i^3F(k_i;k_j,k_l)$. Results (script §3–4):

- $A_{\rm total}$ and all five per-vertex rows equal lane (A)'s in-in $S^{-12}$ coefficients **identically** (difference 0, asserted); $\zeta(\partial\zeta)^2$ and $f_c$ are $O(k^2\eta^2)$ and drop, as in the in-in.
- Hence the whole $f(\mu)$, monopole included, is $k\to0$ physics. **The $-25/8$ gap is not the "sub-leading gradient" issue** and not the "non-attractor $\delta N$ needs the growing mode/momentum" issue (Namjoo–Firouzjahi–Sasaki 2012, arXiv:1210.3692, their $\delta N$ with $N(\phi,\dot\phi)$; Chen–Firouzjahi–Namjoo–Sasaki 2013; Cai et al. 2018, arXiv:1712.09998): lane (B)'s ODE system varies the momentum displacement $u_i=x_i-x_*$ on a flat slice and integrates to a uniform-$\phi$ (or uniform-$\rho$) slice — $N(\phi,\pi)$ **is** included — and the same system gives USR $5/2$ whether $\pi_i$ or $\phi_i$ is varied (script §7).
- Boundary/late-time (Q3): $f_a=\zeta\zeta'/\mathcal H=-\tfrac32\zeta^2$ ($f_{\rm NL}=-5/2$) is the contraction analogue of USR's $+\tfrac32\zeta^2$ (there $\zeta\zeta'/\mathcal H+\tfrac{\eta_{sr}}4\zeta^2=3-\tfrac32$), and the same treatment reproduces $5/2$ in USR (script §1), the only non-attractor benchmark. "Late time" is not asymptotic here, but the leading term is exactly $\propto\eta_*^{-12}\propto P_\zeta^2$ at every $|k\eta_*|\ll1$, so $f_{\rm NL}$ is end-time independent; $f_b$ (non-local) is $O(k^0)$ and is kept; $f_c$ is $O(k^2)$.

Validation before reading any matter-contraction number: USR $\to5/2$ exactly (bulk sources scale as positive powers of $\eta$ and drop); any constant-$\zeta$ attractor $\to$ no $O(k^0)$ source (the Maldacena $O(\epsilon)$ squeezed limit is an $S^0$, sub-Hubble effect — as it must be).

## 2. Where the $\delta N$ loses contact with $\zeta_{\rm Mald}$ (Q2)

On a uniform-$\phi$ slice the lapse is $N=1+\dot\zeta/H$, so Friedmann at fixed $\phi$ gives $\delta H/H=-(\epsilon/3)\dot\zeta_L/H$: the local expansion rate on comoving slices is perturbed at $O(k^0)$, and it is carried by the **trace of the shift gradient**, $\delta K=-\partial^2\psi/a^2\to-\epsilon\dot\zeta_L$. The separate universe defines its $\delta N$ from $\int K/3\,d\tau$ — the zero-shift threading — so $\delta N_c=\zeta+b$ with $\dot b=\delta K/3$, $b=-(\epsilon/3)\zeta_L$ on the growing mode. Script §7 derives $u/\zeta$ from Friedmann + lapse and multiplies by lane (C)'s $\delta N_c$ linear coefficient: $\delta N_c/\zeta_{\rm Mald}=1-\epsilon/3$ (asserted). Consequences: (i) the lab's "$\zeta_\rho=2\zeta_c$ (convention)" is $\delta N_\rho=2(1-\epsilon/3)\zeta_{\rm Mald}$ — $\delta N_\rho=\zeta_{\rm Mald}$ at linear order only because $\epsilon=3/2$; (ii) at second order the map is a time-dependent, non-local ($\partial^{-2}$) spatial diffeomorphism, so **no local $f_{\rm NL}$ relation** exists between $\delta N_c$ and $\zeta_{\rm Mald}$; (iii) lane (B)'s $-55/16$ is the $\delta N$ of the variable closest to $\zeta_{\rm Mald}$ at linear order but still lacks [X].

## 3. What the shear does and does not do (Q4, lane C)

Lane (C) is right that the long mode's shear is $O(k_L^0)$ and traceless. But the dynamical coupling of $\partial_i\partial_j\tilde\chi_L$ (trace + traceless) to the short modes, class [K], **cancels exactly** between the $\zeta$-varied and $\tilde\chi$-varied legs of $T_4$ (script §5: $+\tfrac{15}{128}\mu^2$, $+\tfrac{15}{128}\mu^2$, $-\tfrac{15}{128}\mu^2$, $-\tfrac{15}{128}\mu^2$ per sourced mode). The observed quadrupole is entirely the shift's coordinate-deformation effect ([X]): $T_3$'s $+5\epsilon/4\,\mu^2$ is lane (C)'s $\beta_z$-projection, and $f_b$ corrects it by the threading factor. Lane (C)'s "unsettled advection term" is therefore identified and computed: it is [X], it carries the quadrupole and $+5\epsilon(9-2\epsilon)/36$ of the monopole, and it is not shear.

## 4. General constant-$\epsilon$ contraction (new; label: this work)

$$
f^{\rm sq}(\mu,\epsilon)=\frac{5}{12}\big(\epsilon^2\mu^2-\epsilon^2+6\epsilon-12\big),\quad
\text{monopole }-\frac{5(\epsilon-3)(\epsilon-6)}{18},\quad
\text{isoceles }-\frac{5(\epsilon^2-6\epsilon+12)}{12},\quad
\mu^2:\ \frac{5\epsilon^2}{12},
$$

reducing to $-35/16+\tfrac{15}{16}\mu^2$ at $\epsilon=3/2$; monopole $\to0$ at $\epsilon\to3$ (kination). [L]$(\epsilon)=5(\epsilon-4)/4$, so [L]$-\delta N_c=5\epsilon/4=(5/12)\,(3\epsilon)$, numerically the pure pair-translation coefficient $-3i\,\hat k_L\!\cdot\!\xi$ with $k_L\xi=i\epsilon\zeta_L$ (script §6): recorded as an exact identity, **mechanism not derived**.

## 5. What "observable" means here (honest scope)

Both $\zeta_{\rm Mald}$ and $\delta N_c$ are legitimate curvature variables; their equal-time bispectra differ at $O(1)$ because the threading map is time-dependent and non-local while $\dot\zeta_L\neq0$ (literature on the attractor analogue: Pajer–Schmidt–Zaldarriaga 2013, arXiv:1305.0824; Dai–Pajer–Schmidt 2015, arXiv:1504.00351; for USR: Bravo–Mooij–Palma–Pradenas 2018, arXiv:1711.05290 vs Cai et al. 2018 — the observability of non-attractor squeezed limits is a threading/frame question there too). Nothing at the end of contraction is yet observed; the quantity transported through the bounce (ledger #2) is $\zeta_{\rm Mald}$ with its shift, and the post-bounce constant-$\zeta$ statistics are threading-independent. The correct input to that step is the in-in value. **$-35/16$ stands**, now confirmed by a second organisation (classical $O(k^0)$) sharing only the cubic action with lane (A), with the $\delta N$ discrepancy explained at the equation level rather than reconciled away.

## 6. Integrity note

The classical machinery was frozen after the USR and attractor checks, run once, and only then compared with lane (A)'s JSON. The [L]/[K]/[X]/[S] tags are structural (which leg carries $k_L$), not chosen by value. The $5\epsilon/4$ identity and the $\epsilon/3$ ratio were observed, not imposed. Shared input with lane (A): Maldacena's cubic action in comoving gauge (algebraic consequence of the ADM constraints; valid for either sign of $H$); nothing else is transcribed.

## References checked (2026-09-03)
Maldacena astro-ph/0210603 (cubic action, $f(\zeta)$) · Namjoo–Firouzjahi–Sasaki 1210.3692 (USR $5/2$, $N(\phi,\dot\phi)$) · Chen–Firouzjahi–Namjoo–Sasaki 1301.5699 · Cai, Chen, Namjoo, Sasaki, Wang, Wang 1712.09998 · Lyth–Malik–Sasaki astro-ph/0411220 (gradient expansion, shift assumption) · Salopek–Bond 1990 · Pajer–Schmidt–Zaldarriaga 1305.0824 · Dai–Pajer–Schmidt 1504.00351 · Bravo–Mooij–Palma–Pradenas 1711.05290 · Cai, Xue, Brandenberger, Zhang 0903.0631 · Li, Quintin, Wang, Cai 1612.02036 · lab: `fnl_matter_contraction_adjudication_2026_09_02.*` (aa2987cf), `fnl_matter_contraction_second_method_2026_09_02.*` (d7dac953), `fnl_bianchi_separate_universe_2026_09_03.*` (866cf342).
