# Lane 9b-2 — Δf_NL^bounce[S2] from the RAW ADM cubic Lagrangian on exact S2 modes (ledger row 9 / A3-1e)

**Date:** 2026-09-04 · **Owner:** Claude lane 9b-2 · **Status:** DONE — verdict **S2 ≠ S1** (scheme-dependent; §5).
**Headline (Quintin, $k\eta_B=10^{-3}$):** S2 raw, exact modes: $f_{\rm NL}^{\rm before}=-2.187$, $f_{\rm NL}^{\rm after}=-1.249$,
$\Delta_T=+1.01$, NEC-window $+1.64$ (window-convention dependent); S1 (lane b): $\Delta=-0.140$, $f^{\rm after}=-0.500$.
**Artifacts (this dir):** `lane9b2_s2_rawadm.py` → `results.json`, `lane9b2_s2_rawadm.log`,
`integrand_across_bounce.png`, `dfnl_bounce_s2_vs_ketaB.png`;
manifest `reproducibility/manifests/experiments/p2-a3-lane-9b2-s2-rawadm.json`.
**Venue:** local CPU (numpy/scipy), $0. **Provenance rule:** *computed* = produced by the committed script;
*literature* = cited, not re-derived. Nothing is steered toward S1 = S2.

## 0. Plan (written before any number exists)

Question: lane 9b showed the S2 (effective-fluid, $z^2=2a^2\epsilon/c_s^2$) bounce-window divergence is a
total-derivative pole of the Maldacena/Chen integrated-by-parts form, and that the raw ADM cubic Lagrangian is
finite on-shell at $H=0$. This lane computes the finite number and compares it with S1's
$\Delta f_{\rm NL}^{\rm bounce}[{\rm S1}]=-\tfrac{5}{24}\rho_B$ (lane b: Quintin −0.1398, LQC −0.1043, poly −0.1271).

Steps and gates (in order; each step is a commit):
1. Write the raw ADM cubic Lagrangian (Maldacena 2003 Eq. 2.9–2.11 expanded to cubic order in
   $\{\zeta,\dot\zeta,N_1,\psi\}$, **before** any integration by parts, with $N_1$, $\psi$ substituted; explicit
   $1/H$ never introduced — $N_1$ and $\psi$ are evaluated on the exact modes as regular functions).
   Derive the vertex table symbolically (sympy) and record it in §1.
2. **Gate (i) — S1 reproduction.** On the S1 variables ($z=a$, $\epsilon_{\rm eff}=1/2$, $c_s=1$) the raw-ADM
   route through the same in-in engine (lane b conventions, 3! attachments, no hand symmetry factors) must
   reproduce lane b's bulk+redefinition total $=-\tfrac{5}{24}\rho_B$ to ≲1e−3. If it fails: STOP, report UNRESOLVED.
3. Exact S2 modes: solve the S2 MS equation in the regular form
   $\frac{d}{dt}(z^2\dot\zeta/a)\cdot$… rewritten as a first-order system in $(\zeta, \Pi\equiv z^2\dot\zeta/a)$, which is
   regular at $H=0$ because $z^2\dot\zeta\propto(\dot\zeta/H^2)$ is finite on the exact solution; seed the series
   at $t_B$ from lane 9b Frobenius data, integrate outward, match to the adiabatic-vacuum contraction mode (lane b).
4. Bounce-window in-in integral for the squeezed isoceles configuration ($k_L/k_S=0.02$) at
   $k\eta_B\in\{10^{-3},3\times10^{-3},10^{-2}\}$; window ±η_B, η_* scan, step convergence (gate ii);
   integrand plotted across $t_B$ and checked finite (gate iii).
5. Verdict: S2 = S1 / S2 ≠ S1 (values, ratio, responsible operator) / UNRESOLVED (failing gate named).

## 1. Raw ADM cubic Lagrangian and its Fourier kernel (computed, script `raw_lagrangian`/`build_kernels`)

$\mathcal L=\tfrac12\sqrt h\,[N R^{(3)}-2NV+N^{-1}(E_{ij}E^{ij}-E^2)+N^{-1}\dot\phi^2]$ (Maldacena 2003 Eq. 2.4, $M_{\rm pl}^{-2}=1$),
$h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N=1+N_1$, $N_i=\partial_i\psi$, $E_{ij}=a^2e^{2\zeta}(H+\dot\zeta)\delta_{ij}-\nabla_i\nabla_j\psi$,
$R^{(3)}=-2a^{-2}e^{-2\zeta}[2\partial^2\zeta+(\partial\zeta)^2]$. Background enters only as $(a,H,\dot H)$ via
$\dot\phi^2=\rho+p=-2\dot H$, $V=3H^2+\dot H$ ($c_s=1$, $P$ linear in $X$; sign of $P_X$ irrelevant). The expansion to cubic
order in $(\zeta,N_1,\psi)$ is done by inserting plane-wave superpositions and extracting the trilinear $E_1E_2E_3$
coefficient (multilinear algebra, no integration by parts anywhere): **184-term kernel**
$K_3(a,H,\dot H;\mathbf k_j;\zeta_j,\dot\zeta_j,N_{1j},\psi_j)$. All $3!$ leg attachments are counted once, exactly as in
lane (b) and the adjudication engine. In-in: $B=-2\,{\rm Im}[u_1u_2u_3(t_*)\int dt\,K_3(t;u^*_j,\dot u^*_j,\dots)]$,
$f_{\rm NL}=\tfrac56 B/\sum P_iP_j$. The constraints are substituted on-shell at evaluation time:
$N_1=\dot\zeta/H$, $\psi=-\zeta/H-a^2\epsilon\dot\zeta/k^2$, $\epsilon=-\dot H/H^2$.

**Gate (i-a), symbolic, PASS.** Varying the raw *quadratic* Fourier Lagrangian w.r.t. $N_1(-\mathbf k)$ and $\psi(-\mathbf k)$
returns exactly $N_1=\dot\zeta/H$ and $\psi=-\zeta/H-a^2\epsilon\dot\zeta/k^2$ (Maldacena Eq. 2.13–2.14). The on-shell
quadratic kernel is $2a^3\epsilon\,\dot\zeta_1\dot\zeta_2-2a\epsilon k^2\zeta_1\zeta_2+\frac{d}{dt}[\,2ak^2\zeta_1\zeta_2/H+\dots]$
— the $1/H$ total derivatives of lane 9b are visible already at quadratic order.

## 2. Gate (i): what "S1 reproduction" can and cannot mean (computed)

| test | result |
|---|---|
| **(i-a)** constraints from the raw quadratic Lagrangian | PASS (exact) |
| **(i-b)** exact background (power-law inflation, $\epsilon\in\{0.1,0.2\}$, $k_L/k_S\in\{0.02,0.1\}$), raw in-in from the vacuum (contour $\eta=\eta_*+s(1-i\delta)$) vs Maldacena-form in-in on the same modes | raw/Mald $-1=-6.7(k\eta_*)^2+O(10^{-4})$: **PASS** (extrapolated $\le 1\times10^{-4}$; the $(k\eta_*)^2$ piece is the late-time boundary term $\propto(k/aH)^2$); contour independence $5\times10^{-6}$; Mald vs consistency relation $\tfrac56\epsilon/(1-\epsilon)$ within $10^{-3}$ |
| **(i-b′)** raw in-in over the exact matter contraction (true fluid, $\epsilon=3/2$) from the vacuum to $-t_m$ | $f_{\rm NL}=-2.18728,\ -2.18723,\ -2.18669$ at $k\eta_B=10^{-3},3\times10^{-3},10^{-2}$ vs $-35/16=-2.1875$: **PASS** ($10^{-4}$). The raw form reproduces the adjudicated Maldacena-form+redefinition value *with* $\dot\zeta\neq0$ at the endpoint, i.e. boundary terms $\equiv$ field-redefinition terms here. |
| **(i-c)** this engine's S1 modes + Maldacena-form kernel over $[-\eta_B,\eta_B]$ vs lane (b) bulk | $-0.139639$ vs $-0.139635$ at $k\eta_B=10^{-3}$ (**$3\times10^{-5}$**); $-2\times10^{-3}$, $-8\times10^{-3}$ at $3\times10^{-3},10^{-2}$ (lane b's own $\eta_*$ rule differs there); $|\zeta_{\rm after}/\zeta(-t_m)|=6.059=2/(1-\rho_B)$ ✓ |
| **(i) literal** raw ADM on the S1 variables ($\epsilon_{\rm eff}=\tfrac12$, $\dot H\to-H^2/2$, $z=a$) | **VOID (structural).** S1 modes obey $\ddot\zeta+3H\dot\zeta+k^2\zeta/a^2=0$ (no $-2/t$ friction), so $\dot\zeta(0)\neq0$ and $N_1=\dot\zeta/H$, $-\zeta/H$ are $\propto1/t$: measured integrand pole orders odd $1.00$, even $1.01$ (subdominant); the symmetrically excised integral tends to $-4.84$ (not $-0.140$) — a PV prescription, not a derivation. |

**Reading.** The raw form is unambiguous only on the *true* background ($\dot H$ enters explicitly); S1 replaces $\epsilon$ by
$\tfrac12$ inside coefficients that were obtained by integrating by parts with the background equations, and the true
$\dot H=\Upsilon$ is not $-\tfrac12H^2$. Hence S1 has no raw-ADM counterpart; it is a Maldacena-form-defined,
assumption-labelled anchor (lane a wording stands). The engine is validated instead by (i-a), (i-b), (i-b′), (i-c).
Conversely the raw form is regular on the S2 modes (lane 9b) and singular on the S1 modes: **each scheme is finite only
in the other scheme's singular form.**

## 3. Exact S2 modes (computed, `BounceModes`)

Contraction: adiabatic vacuum $v=e^{-ik\eta_m}(1-i/k\eta_m)/\sqrt{2k}$, $\zeta=v/z$, $z^2=2a^2\epsilon$ ($\epsilon=3/2$).
Junctions at $|t|=t_m$ ($\epsilon:+\tfrac32\to-\tfrac32$): $\zeta$ and $a^3\epsilon\dot\zeta$ continuous ($\dot\zeta$ flips sign).
Window: two power-series solutions of $t\ddot\zeta+(3\Upsilon t^2-2)\dot\zeta+k^2te^{-\Upsilon t^2}\zeta=0$ (exponents 0, 3;
$c_1=0$ forced; order 90; ODE residual $\le4\times10^{-16}$, tail $10^{-27}$). The regular constraint data are evaluated as
series: $N_1=w/\Upsilon$ with $w=\dot\zeta/t$, $\psi=(a^2w/k^2-\zeta)/(\Upsilon t)$ whose numerator vanishes at $t=0$ to
$10^{-12}$ (lane 9b residue cancellation, checked numerically on every mode). Expansion: real matter basis
$g_1=\cos x-\sin x/x$, $g_2=\sin x+\cos x/x$ (the $(e^{\mp ikη})$ basis is degenerate at $k\eta\sim10^{-3}$ and loses all
digits). Wronskian $2a^3\epsilon(u\dot u^*-u^*\dot u)/i=1$ to $10^{-9}$ at every probed $t$ including inside the window.
**By-product:** exact-mode S2 linear transmission $|\zeta(t_*)/\zeta(-t_m)|=0.9696,\,0.9678,\,0.9647$ ($k\eta_B=10^{-3},3\times10^{-3},10^{-2}$)
— the growing mode passes through the fluid-scheme bounce almost unchanged, versus S1's amplification $2/(1-\rho_B)=6.06$.
## 4. S2 numbers, gates (ii)/(iii) (computed; squeezed isoceles $k_L/k_S=0.02$, $\eta_*=\min(50,0.2/k\eta_B)\,\eta_B$)

| $k\eta_B$ | NEC-window raw $\int_{-t_m}^{t_m}$ | $f_{\rm NL}^{\rm before}$ (raw, at $-t_m$) | $f_{\rm NL}^{\rm after}$ (raw, end-to-end) = contraction + window + expansion | $|\lambda|$ | $\Delta_T\equiv f^{\rm after}-f^{\rm before}/|\lambda|$ |
|---|---|---|---|---|---|
| $10^{-3}$ | **+1.6401** | $-2.1873$ | **$-1.2488$** $=-2.7269+1.6401-0.1620$ | 0.9696 | **+1.007** |
| $3\times10^{-3}$ | +1.6400 | $-2.1872$ | $-1.2457$ $=-2.7266+1.6400-0.1590$ | 0.9678 | +1.014 |
| $10^{-2}$ | +1.6719 | $-2.1867$ | $-1.2437$ $=-2.7618+1.6719-0.1537$ | 0.9647 | +1.023 |

Reference S1 (lane b, same background/configuration): $\Delta f_{\rm NL}^{\rm bounce}=-0.1398,-0.1394,-0.1387$; $-(5/24)\rho_B=-0.1396$;
$f_{\rm NL}^{\rm after}=T(-35/16)+\Delta=-0.5002$ with $T=0.165$.

**Gate (ii).** Step convergence of the window integral: $+1.6401338114$ unchanged from 2001 to 16001 points ($<10^{-10}$).
$\eta_*$ scan ($10,20,50,100\,\eta_B$): $2.012,1.674,1.640,1.638$ — converged for $\eta_*\ge50\eta_B$ (the $10\eta_B$ point is the
late-time boundary term $\propto(k/aH)^2$ seen in gate (i-b)). Contour independence of the end-to-end value: $\delta=0.15$ vs
$0.30$ agree to $10^{-8}$. **Window scan (reported, not hidden):** $[-f,f]\,t_m$ with $f=0.5,0.75,1,1.25,1.5,2$ gives
$-0.297,-0.083,+1.640,-0.935,-2.661,-4.801$. The raw form's window integral is *not* bounce-localised: its
total-derivative content is $O(1)$ at the window edges (Wronskian-type pieces, e.g. from $-9\,d(a^3H\zeta^3)/dt$-like
terms), and the integrand is discontinuous at the NEC junctions where $\epsilon$ flips sign. Lane b's S1 Maldacena-form
window scan ($f=0.8\ldots3$ in $\eta_B$) moves only $-0.120\to-0.197$. Therefore the *only* convention-free S2 quantities
are $f_{\rm NL}^{\rm before}$ and $f_{\rm NL}^{\rm after}$; $\Delta_T$ is the closest analogue of lane b's decomposition
$f^{\rm after}=T f^{\rm before}+\Delta$ (with $T=1/|\lambda|$), and the NEC-window number is the literal analogue with an
$O(1)$ convention dependence that S1 does not display.

**Gate (iii).** `integrand_across_bounce.png`: the S2 raw contribution density $d\Delta f_{\rm NL}/dt$ is finite and smooth
through $H=0$ (it crosses zero near $t=0$, extrema $\pm15$ at $|t|\approx0.6\,t_m$), identical for the three $k\eta_B$; the right
panel shows the S1 pseudo-scheme raw integrand's $|t|^{-1}$ pole against the flat S2 curve.

**Operator attribution** (end-to-end $f^{\rm after}$ by lapse/shift content of the raw kernel, $k\eta_B=10^{-3}$):
pure-$\zeta$ (geometric: $e^{3\zeta}$, $R^{(3)}$, $(H+\dot\zeta)^2$) $+6.56$; $N_1^1$: $-13.12$; $N_1^2$: $+5.31$; $N_1\psi$: $+0.83$;
$\psi^1$: $-0.83$; $\psi^2$: $+0.0008$; $N_1^3$, $N_1^2\psi$, $N_1\psi^2$: exactly 0 (contraction and expansion cancel).
The shift sector cancels to $10^{-3}$ (lane 9b's regular $\psi$); the result is a geometric-vs-lapse cancellation
$6.56-13.12+5.31=-1.25$. No single operator "owns" the S2 value.

## 5. VERDICT

**S2 ≠ S1 — the bounce-window cubic contribution is scheme-DEPENDENT.** Engine gates (i-a), (i-b), (i-b′), (i-c) pass;
gate (i) as literally posed is void for a structural reason (§2). In S2 (raw ADM, exact modes, absolutely convergent):
$f_{\rm NL}^{\rm before}=-2.187$ ($=-35/16$ to $10^{-4}$), $f_{\rm NL}^{\rm after}=-1.249$, $\Delta_T=+1.01$, NEC-window
$+1.64$ (window-convention dependent). In S1 (lane b): $\Delta=-0.140=-(5/24)\rho_B$, $f_{\rm NL}^{\rm after}=-0.500$.
Ratios: $f^{\rm after}$ S2/S1 $=2.50$; $\Delta_T[{\rm S2}]/\Delta[{\rm S1}]=-7.2$. The difference is dominated by the
**linear MS-variable choice** — S2 transmits the growing mode with $|\lambda|=0.97$ so $-35/16$ arrives almost intact
($-2.26$), while S1 suppresses it to $T(-35/16)=-0.36$ — plus a cubic-level bounce+expansion net of $+1.0$ (S2) versus
$-0.14$ (S1). This is the cubic-order face of the A2 linear finding: the S1/S2 ambiguity is not regulated away by the raw
form; it is a genuine physical difference between the geometric and effective-fluid continuations through $H=0$, and the
A3M paper must carry both numbers with their scheme labels (or a model-level resolution of which $z$ is physical).
**Not claimed:** equality with $-(5/24)\rho_B$ in any definition; a bounce-localised S2 number (the window scan forbids it).

## 6. Assumptions and limits

(A1) Quintin-type piecewise background only (junction with discontinuous $\dot H$; LQC/poly have $\dot H=0$ crossings where
$z^2=0$ and the S2 $\zeta$ has a logarithmic point — not attempted). (A2) $c_s=1$, $P$ linear in $X$ (ghost sign in the
window, as lane 9b flagged); Horndeski/Galileon constraint corrections are lane (c). (A3) First-order in-in with
$H_3=-L_3$; boundary terms are whatever the raw form contains (no redefinition applied anywhere). (A4) $f_{\rm NL}^{\rm after}$
precision $\sim10^{-3}$ (contraction contour, $1.2\times10^5$ points); window integral $10^{-10}$. (A5) $\epsilon$ in the
window is $-1/(\Upsilon t^2)$: the $z^2<0$ ghost sector is used as in lane (b), flagged, not resolved.
