# Lane 9b-2 — Δf_NL^bounce[S2] from the RAW ADM cubic Lagrangian on exact S2 modes (ledger row 9 / A3-1e)

**Date:** 2026-09-04 · **Owner:** Claude lane 9b-2 · **Status:** IN PROGRESS (plan header committed first, anti-stall).
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

## 1. Raw ADM cubic Lagrangian (computed) — TBD
## 2. Gate (i): S1 reproduction — TBD
## 3. Exact S2 modes — TBD
## 4. Bounce-window integral, gates (ii)/(iii) — TBD
## 5. VERDICT — TBD
