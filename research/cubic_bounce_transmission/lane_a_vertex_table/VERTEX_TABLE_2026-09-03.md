# Lane (a) — cubic-vertex table for ζ through a nonsingular bounce

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2, second half (intrinsic bounce
contribution to f_NL). Lane (a) of three; lane (b) = numerical in-in over the bounce window, lane (c) =
model-specific (Horndeski / dressed-metric) vertex corrections. Both are separate.
**Date:** 2026-09-03 · **Venue:** local CPU (sympy 1.14, numpy) · **Cost:** $0 · **Wall clock:** 2.0 s.
**Artifacts (this directory):** `cubic_vertex_table.py` → `cubic_vertex_table.log`, `vertex_table.json`;
`REGULARISATION_ASSUMPTION.md`; manifest
`reproducibility/manifests/experiments/p2-a2-lane-a-cubic-vertex-table.json`.
**Provenance rule:** every coefficient in §1 is *literature* (cited by paper + equation, transcribed,
not derived); every pole order, kernel, closed form and number in §2–§5 is *computed* by the committed
script. The contraction value $-35/16$ is ledger #1 (closed) and is not re-derived.

Conventions: $M_{\rm Pl}^2=1$, $a_B=1$, $t_B=0$; $\epsilon=-\dot H/H^2$, $\eta_{\rm sr}=\dot\epsilon/(\epsilon H)$,
$s=\dot c_s/(c_sH)$, $\Sigma = H^2\epsilon/c_s^2$, $\lambda = X^2P_{XX}+\tfrac23X^3P_{XXX}$;
$\tilde\chi\equiv\partial^{-2}\dot\zeta$ (Chen's $\chi = a^2\epsilon\tilde\chi/c_s^2$).

## 1. The cubic action (literature)

$S_3=\int dt\,d^3x\sum_V c_V(t)\,O_V + \int dt\,d^3x\, f(\zeta)\,\frac{\delta L_2}{\delta\zeta}\Big|_1$, with
(Chen, Huang, Kachru & Shiu 2007 hep-th/0605045 Eq. 4.28; Seery & Lidsey 2005 astro-ph/0503692 Eq. 51;
Maldacena 2003 astro-ph/0210603 Eq. 3.9 at $c_s=1,\lambda=0$):

| id | operator $O_V$ | coefficient $c_V(a,H,\epsilon,\eta_{\rm sr},c_s)$ | $c_s=1$, $\lambda=0$ |
|---|---|---|---|
| V1 | $\dot\zeta^3$ | $-\dfrac{a^3}{H}\Big[\dfrac{\epsilon H^2}{c_s^2}\Big(1-\dfrac1{c_s^2}\Big)+2\lambda\Big]$ | 0 |
| V2 | $\zeta\dot\zeta^2$ | $\dfrac{a^3\epsilon}{c_s^4}\,(\epsilon-3+3c_s^2)$ | $a^3\epsilon^2$ |
| V3 | $\zeta(\partial\zeta)^2/a^2$ | $\dfrac{a\,\epsilon}{c_s^2}\,(\epsilon-2s+1-c_s^2)$ | $a\epsilon^2$ |
| V4 | $\dot\zeta\,\partial\zeta\,\partial\tilde\chi$ | $-\dfrac{2a^3\epsilon^2}{c_s^4}$ | $-2a^3\epsilon^2$ |
| V5 | $\zeta^2\dot\zeta$ | $\dfrac{a^3\epsilon}{2c_s^2}\,\dfrac{d}{dt}\Big(\dfrac{\eta_{\rm sr}}{c_s^2}\Big)$ | $\tfrac12a^3\epsilon\,\dot\eta_{\rm sr}$ |
| V6 | $\partial\zeta\,\partial\tilde\chi\,\partial^2\tilde\chi$ | $\dfrac{a^3\epsilon^3}{2c_s^4}$ | $\tfrac12a^3\epsilon^3$ |
| V7 | $\partial^2\zeta\,(\partial\tilde\chi)^2$ | $\dfrac{a^3\epsilon^3}{4c_s^4}$ | $\tfrac14a^3\epsilon^3$ |

Field redefinition $\zeta=\zeta_n+f(\zeta_n)$ (Chen et al. 2007 Eq. 4.29; Maldacena 2003 Eq. 3.10):

| id | $f\ni$ | coefficient |
|---|---|---|
| R1 | $\zeta^2$ | $\eta_{\rm sr}/(4c_s^2)$ |
| R2 | $\zeta\dot\zeta$ | $1/(c_s^2H)$ |
| R3 | $-(\partial\zeta)^2+\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\zeta)$ | $1/(4a^2H^2)$ |
| R4 | $(\partial\zeta)(\partial\tilde\chi)-\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\tilde\chi)$ | $\epsilon/(2c_s^2H)$ |

Script check (computed): at $c_s=1,\lambda=0$ the table reduces to the lab's adjudication Lagrangian,
including the verified rewrite $V6+V7 \to -\tfrac12a^3\epsilon^3\zeta\dot\zeta^2+\tfrac12a^3\epsilon^3\zeta(\partial_i\partial_j\tilde\chi)^2$
+ total derivative, giving the familiar $a^3(\epsilon^2-\epsilon^3/2)\zeta\dot\zeta^2$.
Literature on the dropped boundary terms: Arroja & Tanaka 2011 (arXiv:1103.1102), Burrage, Ribeiro & Seery
2011 (arXiv:1103.4126) — the R-terms reproduce their effect on the correlator at $\eta_*$.

## 2. The bounce backgrounds (computed, exact in $t$)

| background | $H(t)$ | $\epsilon(t)$ | $\eta_{\rm sr}(t)$ | at $t\to0$ |
|---|---|---|---|---|
| Quintin+2015 phase (arXiv:1508.04141) | $\Upsilon t$, $a=e^{\Upsilon t^2/2}$ | $-1/(\Upsilon t^2)$ | $-2/(\Upsilon t^2)$ | $\eta_{\rm sr}=2\epsilon$ exactly |
| LQC effective, dust ($H^2=\tfrac{\rho}{3}(1-\tfrac{\rho}{\rho_c})$) | $\dfrac{\rho_c t/2}{1+\tfrac34\rho_ct^2}$, $a^3=1+\tfrac34\rho_ct^2$ | $\tfrac32-\dfrac{2}{\rho_ct^2}$ | $\dfrac{4(3\rho_ct^2+4)}{\rho_ct^2(3\rho_ct^2-4)}$ | $\Upsilon_{\rm eff}=\rho_c/2$, $\eta_{\rm sr}/\epsilon\to2$ |

The LQC dust bounce is locally *exactly* a Quintin-type bounce with $\Upsilon=\rho_c/2$ (closed form verified
against the Friedmann equation), so the pole structure below is common to both.

## 3. Behaviour of every coefficient at $H\to0$ (computed; `cubic_vertex_table.log` §C)

Leading term $c_V \sim \kappa_V\,t^{n}$ (Quintin; LQC has the same $n$ with $\Upsilon\to\rho_c/2$):

| id | $n$ | $\kappa_V$ (Quintin) | comment |
|---|---|---|---|
| V1 | $-1$ | $c_s^{-2}-c_s^{-4}-2\lambda/\Upsilon$ | odd; $\propto \dot H/H$ |
| V2 | $-4$ | $1/(\Upsilon^2c_s^4)$ | $\epsilon^2$ |
| V3 | $-4$ | $1/(\Upsilon^2c_s^2)$ | $\epsilon^2$, gradient |
| V4 | $-4$ | $-2/(\Upsilon^2c_s^4)$ | $\epsilon^2$ |
| V5 | $-5$ | $-2/(\Upsilon^2c_s^4)$ | odd; $\epsilon\,\dot\eta_{\rm sr}$ |
| V6 | $-6$ | $-1/(2\Upsilon^3c_s^4)$ | $\epsilon^3$ (constraint sector) |
| V7 | $-6$ | $-1/(4\Upsilon^3c_s^4)$ | $\epsilon^3$ (constraint sector) |
| R1 | $-2$ | $-1/(2\Upsilon c_s^2)$ | $\eta_{\rm sr}$ |
| R2 | $-1$ | $1/(\Upsilon c_s^2)$ | $1/H$ |
| R3 | $-2$ | $1/(4\Upsilon^2)$ | geometric $1/(aH)^2$ |
| R4 | $-3$ | $-1/(2\Upsilon^2c_s^2)$ | $\epsilon/H$ |

## 4. The table: operator × {coefficient, $|\epsilon|\to\infty$ behaviour, removability, expected sign}

"Integrand" = $c_V\times O_V$ with the super-Hubble mode $\zeta=C_1+C_2J$, $\dot\zeta=C_2/(az^2)$ in each scheme
(S2 fluid: $z^2=2a^2\epsilon/c_s^2$; S1 geometric: $z=a$). Sign column: sign of the vertex's contribution to the
squeezed $f_{\rm NL}$ over the bounce window, from the computed kernels of §5 where available.
Machine-readable copy: `vertex_table.json`.

| id | coefficient | $\|\epsilon\|\to\infty$: coefficient / S2 integrand / S1 integrand | total-derivative / removable? | expected sign of $\Delta f_{\rm NL}^{\rm sq}$ |
|---|---|---|---|---|
| V1 | $-\tfrac{a^3}{H}[\Sigma(1-c_s^{-2})+2\lambda]$ | $t^{-1}$ / $t^{+5}$ finite / 0 | no; absent for canonical $c_s=1$ | model-dependent ($\lambda$, $c_s$); negligible near bounce ($\dot\zeta^3\propto H^6$) |
| V2 | $a^3\epsilon(\epsilon-3+3c_s^2)/c_s^4$ | $t^{-4}$ / $t^0$ **finite** / finite | no (bulk) | **negative** (computed S1 kernel $\tfrac5{12}(-I_\infty-3J)/I_\infty^2$; closed form $-\tfrac5{24}\rho_B$) |
| V3 | $a\epsilon(\epsilon-2s+1-c_s^2)/c_s^2$ | $t^{-4}$ / $t^{-4}$ **non-integrable** / finite | no (bulk) | $(k\eta_B)^2$-suppressed on super-Hubble scales; sign not fixed by lane (a); regulator-dependent in S2 |
| V4 | $-2a^3\epsilon^2/c_s^4$ | $t^{-4}$ / $t^0$ **finite** / finite | no (bulk) | same time structure as V2 with an angular kernel $-(\mathbf q\!\cdot\!\mathbf r)/r^2$; sign to be fixed by lane (b) (squeezed angular average) |
| V5 | $\tfrac{a^3\epsilon}{2c_s^2}\tfrac{d}{dt}(\eta_{\rm sr}/c_s^2)$ | $t^{-5}$ / $t^{-3}$ odd pole / 0 | yes in part: for $\eta_{\rm sr}$ const it is a total derivative of R1; here $\eta_{\rm sr}=2\epsilon$ is not const | odd in $t$ ⇒ principal value; computed S1-type kernel $\tfrac5{12}(I_\infty^2-2I_\infty J-3J^2)/I_\infty^2$; PV value scheme-dependent |
| V6 | $a^3\epsilon^3/(2c_s^4)$ | $t^{-6}$ / $t^{-2}$ **non-integrable** / finite | partly: V6+V7 $\to -\tfrac12a^3\epsilon^3\zeta\dot\zeta^2 + \tfrac12a^3\epsilon^3\zeta(\partial_i\partial_j\tilde\chi)^2$ + t.d.; the pole survives the rewrite | the $-\tfrac12a^3\epsilon^3\zeta\dot\zeta^2$ piece has the **opposite** sign to V2 in S1 (positive contribution, $\tfrac18$ of V2's weight) |
| V7 | $a^3\epsilon^3/(4c_s^4)$ | $t^{-6}$ / $t^{-2}$ **non-integrable** / finite | see V6 | see V6 |
| R1 | $\eta_{\rm sr}\zeta^2/(4c_s^2)$ | $t^{-2}$ / $t^{-2}$ / 0 | boundary term (removable by redefinition); singular at $H=0$ | $\tfrac{5}{12}\eta_{\rm sr}(\eta_*)$; $\to0$ post-bounce (matter expansion $\eta_{\rm sr}=0$); **generalised** $(5/12)(1-n_s)$ piece: $f_{\rm NL}^{\rm R1+R2}=\tfrac53\big[\tfrac{\eta_{\rm sr}}{4c_s^2}+\tfrac{\dot\zeta}{c_s^2H\zeta}\big]_{\eta_*}$ |
| R2 | $\zeta\dot\zeta/(c_s^2H)$ | $t^{-1}$ / $t^{+1}$ / $t^{-1}$ | boundary term | $\tfrac53\dot\zeta/(H\zeta)$ at $\eta_*$: $-\tfrac52$ at end of contraction (adjudication row), $\to0$ post-bounce |
| R3 | $[\cdots]/(4a^2H^2)$ | $t^{-2}$ / $t^{-2}$ / $t^{-2}$ | boundary term | $O(k^2/a^2H^2)$ post-bounce → 0; singular *at* bounce in every scheme |
| R4 | $\epsilon[\cdots]/(2c_s^2H)$ | $t^{-3}$ / $t^{-1}$ / $t^{-1}$ | boundary term | $\to0$ post-bounce ($\dot\zeta\to0$) |

**Generalised boundary piece.** In slow roll R1+R2 give $\tfrac{5}{12}\eta_{\rm sr}$, the $\eta$-part of
$\tfrac5{12}(1-n_s)$. Through the bounce the general expression is
$$f_{\rm NL}^{\rm redef}(\eta_*)=\frac53\Big[\frac{\eta_{\rm sr}(\eta_*)}{4c_s^2}+\frac{1}{c_s^2}\frac{\dot\zeta}{H\zeta}\Big|_{\eta_*}\Big]
\;=\;\begin{cases}-\tfrac52 & \eta_*=\text{end of matter contraction }(\eta_{\rm sr}=0,\ \dot\zeta=-\tfrac32H\zeta)\\
\text{singular} & \eta_*\ \text{inside the NEC window }(\eta_{\rm sr}=2\epsilon\to-\infty)\\
0 & \eta_*\ \text{post-bounce matter expansion }(\eta_{\rm sr}=0,\ \dot\zeta/H\zeta\propto a^{-3}/H\to0)\end{cases}$$
(normalisation check computed: local $F\zeta^2\Rightarrow f_{\rm NL}=\tfrac53F$.) The $-5/2$ of the contraction
is therefore **not** a separate additive piece post-bounce; it is re-expressed by the bulk integrals through the
bounce, which is what makes the total $\eta_*$-independent (lane (b) test, §5).

## 5. What lane (b) must evaluate, and the analytic bounce-window estimate

**Integral (lab convention, adjudication §1).** For each vertex, in conformal time
($c_V^{\rm conf}=c_V/a^{\,n_{\dot{}}-1}$, $\dot\zeta=\zeta'/a$):
$$B(k_1,k_2,k_3;\eta_*)=-2\,{\rm Im}\Big[u_{k_1}u_{k_2}u_{k_3}(\eta_*)\int_{-\eta_B}^{+\eta_B}\!d\eta\;c_V^{\rm conf}(\eta)\sum_{\sigma\in S_3}K_V(\mathbf k_{\sigma1},\mathbf k_{\sigma2},\mathbf k_{\sigma3})\prod_j T^{(V)}_j\big[u^*_{k_{\sigma j}}(\eta)\big]\Big],$$
$f_{\rm NL}=\tfrac56\,B/(P_1P_2+P_1P_3+P_2P_3)$, $T_j\in\{u^*,u^{*\prime}\}$ by derivative slot, $K_V$ the Fourier
kernel of $O_V$ ($K=1$ for V2, V5; $-(\mathbf q\cdot\mathbf r)/r^2$ for V4; $(\mathbf p\cdot\mathbf q)/(q^2)$-type for V6; $p^2(\mathbf q\cdot\mathbf r)/(q^2r^2)$ for V7),
with the mode functions of `a2_transmission_linear.py` ($u=C_1+C_2J$ on super-Hubble scales; full $\mu''+(k^2-W)\mu=0$
solution when $k\eta_B$ is not small), $\eta_*$ post-bounce, plus the same integrals over the contraction
($-\infty,-\eta_B$) and expansion $(\eta_B,\eta_*)$ windows and $f_{\rm NL}^{\rm redef}(\eta_*)$ from §4.
Required checks: (i) Maldacena-dS and USR-$5/2$ gates of the adjudication engine; (ii) **$\eta_*$-independence** of the
total; (iii) S1 vs regulated-S2 ($d_{\rm cut}$ scaling for V3, V5, V6, V7 per `REGULARISATION_ASSUMPTION.md` §4).

**Super-Hubble reduction (computed, $k\eta_B\ll1$, S1).** With $u_i=C_1^{(i)}+C_2^{(i)}J(\eta)$,
${\rm Im}(C_1C_2^*)=\tfrac12$ (Wronskian, verified for the brief's $\alpha,\beta,r$), $J(\eta_*)=I_\infty$, the
exact-in-$J$ squeezed kernels are
$$\zeta\zeta'^2:\quad \frac{5\,(-162A^4I_\infty^2-486A^4I_\infty J-k^6)}{6I_\infty(324A^4I_\infty^2+k^6)}\;\xrightarrow{|r|\gg1}\;\frac{5(-I_\infty-3J)}{12\,I_\infty^2},\qquad
\zeta^2\zeta':\quad \xrightarrow{|r|\gg1}\;\frac{5(I_\infty^2-2I_\infty J-3J^2)}{12\,I_\infty^2},$$
per unit $c^{\rm conf}(\eta)\,a^{-4}\,d\eta$ (resp. $a^{-2}$). Since $a$ is even and $J$ odd in $\eta$, the $J$-linear
term integrates to zero over the symmetric window and the V2 vertex gives the **closed form**
$$\boxed{\;\Delta f_{\rm NL}^{\rm bounce}[{\rm V2},{\rm S1}]=-\frac{5}{48\,I_\infty}\int_{-\eta_B}^{\eta_B}\frac{d\eta}{a^2}=-\frac{5}{24}\,\rho_B\;}$$
with $\rho_B=|J(-\eta_B)|/I_\infty$ the brief's mixing fraction. Numerically (script §F, agreement with the closed form
$\le4\times10^{-5}$ on the Quintin grids, $2\times10^{-6}$ LQC):

| background | $\rho_B$ | $\Delta f_{\rm NL}^{\rm bounce}[{\rm V2,S1}]$ | vs transmitted contraction value $-\tfrac{35}{16}T_{f_{\rm NL}}$ |
|---|---|---|---|
| Quintin+2015, $\Delta t_B\in\{0.5,1,2\}$ | 0.670 | $-0.1396$ (duration-independent) | $-0.361$ → bounce term is 39 % of it, same sign |
| LQC dust | $1/2$ exact | $-5/48=-0.1042$ | $-35/64=-0.547$ → 19 % |
| poly $\eta_b=1$ | 0.609 | $-0.124$ (grid 2 %) | $-0.428$ → 29 % |

**Order-of-magnitude statement.** $\Delta f_{\rm NL}^{\rm bounce}=O(0.1)$, **negative**, i.e. it *adds to*
$|f_{\rm NL}|$ in the direction the literature calls enhancement (Quintin+2015 §5; Agullo+2017 — literature), but at the
$\sim10$–$40\%$ level of the transmitted $-35/16\,T$, not orders of magnitude, in the bounded S1 scheme with
$k\eta_B\ll1$. It is **$\Upsilon$-independent** in S1 (self-similar, like $T_{f_{\rm NL}}$). $\Upsilon$-dependence enters
only through the S2 poles: the regulated V6+V7 contribution scales as $\propto\Upsilon^{-3}d_{\rm cut}^{-1}\times(\dot\zeta$-weights$)$ and has
no $d_{\rm cut}\to0$ limit — that, not a large finite number, is where "orders of magnitude" can be manufactured, and it is
scheme-dependent. The V6+V7 $\zeta\dot\zeta^2$ piece in S1 has the opposite sign to V2 with weight $1/8$
($\epsilon_{\rm eff}^3/2$ vs $\epsilon_{\rm eff}^2$), so the S1 pure-time total is $\approx-\tfrac{7}{8}\cdot\tfrac{5}{24}\rho_B$;
V4 and the $\zeta(\partial_i\partial_j\tilde\chi)^2$ remainder carry angular kernels and are lane (b).

## 6. Assumptions and limits

(A1) $k\eta_B\ll1$ for the reduction of §5; (A2) $P(X,\phi)$ form of the cubic action — Horndeski/Galileon
terms of the actual Quintin+2015 Lagrangian (literature: Gao & Steer 2011; De Felice & Tsujikawa 2011) are not
included; (A3) S1 cubic coefficients are the linear-scheme substitution $\epsilon\to1/2$, $c_s\to1$ — an assumption,
not the dressed-metric $\mathcal H_3$ of Agullo+2017; (A4) the vacuum $C_1,C_2$ of the brief (adiabatic in the
matter contraction); (A5) first-order in-in, no loop or backreaction terms.
