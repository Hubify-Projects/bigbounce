# Ledger row 9 (A3-1e), lane 9c-2 — exact dressed-metric modes and the bounce-window in-in integral at $k\eta_B\sim1$

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` row 9 — bounce-scale enhancement at
$k\eta_B\sim1$ (A3-1e).
**Date:** 2026-09-04 · **Venue:** local CPU · **Cost:** \$0.
**Predecessor:** `../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md`, whose §5 verdict was
*NOT DETERMINABLE WITHOUT A COMPUTATION* and named this computation exactly. This file executes it.

## Plan (this file)

1. **Modes.** Integrate $\mu''+(k^2-\mathfrak W(\eta))\mu=0$ on the LQC-dust dressed-metric
   background with the bounded geometric potential $\mathfrak W=a''/a$ implemented in
   `../g1_dressedmetric_transmission.py`, for $k\eta_B\in\{0.1,0.3,1,3,10\}$, with three initial
   states: (S-lab) the lab's adiabatic-vacuum contraction mode of A2 §4; (S-ABS0) an
   adiabatic-order-zero vacuum set at a fixed pre-bounce time (ABS §IV F); (S-ad4) the 4th-order
   adiabatic vacuum. Report $|\zeta_{\rm after}/\zeta_{\rm before}|$ and
   $\mathcal P_{\rm after}/\mathcal P_{\rm before}$ per state.
2. **Gate (implemented first).** The scheme-S1 bounce-window in-in integral over lane (a)'s
   V2–V7 + R1–R4, evaluated with these exact modes at $k\eta_B=10^{-3}$ with the lab state, must
   reproduce lane (b)'s $\Delta f_{\rm NL}^{\rm bounce}=-5/48$ per unit $\rho_B$ to $\lesssim10^{-3}$
   relative. No downstream number is reported if the gate fails; the failing gate is named instead.
3. **$\Delta f_{\rm NL}^{\rm bounce}(k\eta_B)$** for the squeezed-isoceles configuration, per initial
   state, over $k\eta_B\in[0.1,10]$; per-vertex decomposition to identify the dominant vertex at
   $k\eta_B\approx1$.
4. **Comparison to ABS.** Their $|f_{\rm NL}|\sim10^{3}$ plateau (their §IV B / §VII) and their
   $e^{-\alpha k_t/k_{\rm LQC}}=e^{-1.830\,k\eta_B}$ decay (their §V, $\alpha\simeq0.64677$;
   $k_{\rm LQC}\eta_B=1.060$ for lab dust, lane 9c §2.2). Partition the gap into initial state,
   matter sector (dust vs kinetic-dominated scalar), and unexplained residual.
5. **Verdict:** ENHANCEMENT PRESENT (magnitude, window, state-dependence, and whether it changes the
   PBH-channel null at $k\eta_B\approx3$ given lane 9c's 7.0-dex / $408\sigma$ estimate) /
   ENHANCEMENT ABSENT-OR-SUPPRESSED / UNRESOLVED (naming the failing gate).

**Provenance rule (inherited).** Every equation attributed to a paper is cited by equation number.
Nothing is invented. Where a numerical gate fails, that is reported and the conclusion is stated at
the evidential strength the computation supports. No steering toward any verdict.

*Sections follow below as they are completed.*

---

## 0. What was run

`lane9c2_lqc_modes.py` imports lane (b)'s in-in machinery **verbatim**
(`bounce_cubic_inin.vertex_fnl`, `redef_fnl`, `_dots`, the V1–V7 coefficients/kernels and the
R1–R4 redefinition terms) and A2's LQC-dust background
(`a2_transmission_linear.bg_lqc`, dressed geometric potential
$\mathfrak W = a''/a = x^{1/3}(1/6 + x/3)$, $x=\rho/\rho_{\rm c}$, already validated in
`../g1_dressedmetric_transmission.py`). **Only the initial state of the mode functions and the
$k$-range are new**; no vertex coefficient, kernel, sign, or in-in convention was touched.

Background: $\eta_B = 1.060146$, $I_\infty = 1.813798$, $A = 1/12$, $\rho_B = 0.5000003$,
integration domain $|\eta| \le 309.4$. Configuration: squeezed isoceles $k_1 = 0.02\,k$,
$k_2=k_3=k$ (lane (b)'s configuration). Runtime 64 s, CPU only, \$0.

## 1. GATE (implemented first, as required)

| quantity | value |
|---|---|
| lane (b) total at $k\eta_B=10^{-3}$, $\eta_*=50\eta_B$ | $-0.1043113297$ |
| lane 9c-2 total, same point, state S-lab | $-0.1043113297$ |
| **relative difference** | $\mathbf{2.4\times10^{-11}}$ — **PASS** ($\le10^{-3}$) |
| lane (a) closed form $-5/48$ | $-0.1041666667$ |
| lane 9c-2 **V2 alone** vs $-\tfrac5{24}\rho_B$ | $-0.1041984$ vs $-0.1041667$, rel $3.0\times10^{-4}$ |
| lane 9c-2 **total** vs $-5/48$ | rel $1.39\times10^{-3}$ |
| Wronskian $\mathrm{Im}(\mu^*\mu')$ at $\eta=0$ | $-0.500000000$ (exact $-1/2$) |

**Reading of the gate, stated precisely.** The closed form $-\tfrac5{24}\rho_B=-5/48$ is the **V2
vertex alone** (lane (a) §5); the exact-mode pipeline reproduces it to $3.0\times10^{-4}$. The
*total* sits $1.39\times10^{-3}$ away from $-5/48$ because it additionally carries the genuine
subleading V3 + V4 + V6 + V7 bulk terms and the R1–R4 boundary terms — this is lane (b)'s own
number, reproduced here to eleven digits, not a numerical error. The gate as posed (reproduce
lane (b)'s LQC result at $k\eta_B=10^{-3}$ with the lab state to $\lesssim10^{-3}$) **passes**; the
gate against the *analytic* $-5/48$ passes at the vertex it describes and misses by $1.4\times10^{-3}$
on the total, for the reason just named. Both are recorded rather than one being quoted.

## 2. Exact modes: growth factor and power-spectrum modification

**Definition used (stated because it must be well defined at $k\eta_B\gtrsim1$, where $\zeta$ is
neither constant nor slowly varying).** With $\mu = (\alpha e^{-i\int\Omega}+\beta e^{+i\int\Omega})/\sqrt{2\Omega}$
the combination $N(\eta)\equiv\omega|\mu|^2+|\mu'|^2/\omega = |\alpha|^2+|\beta|^2$ is
oscillation-free and equals $1$ in the instantaneous adiabatic vacuum; the WKB-averaged
$|\zeta|^2 = N/(2\omega a^2)$. The LQC-dust background is **exactly time-symmetric**
($a(-\eta)=a(\eta)$), so at a WKB-safe reference time $\eta_{\rm ref}$ (chosen per $k$ as the
smallest $|\eta|\ge10\eta_B$ with $k^2\ge10\,\mathfrak W$)
$$\Big|\frac{\zeta_{\rm after}}{\zeta_{\rm before}}\Big| = \sqrt{\frac{N(+\eta_{\rm ref})}{N(-\eta_{\rm ref})}},\qquad
\frac{\mathcal P_{\rm after}}{\mathcal P_{\rm before}} = \frac{N(+\eta_{\rm ref})}{N(-\eta_{\rm ref})}.$$
States set at a finite $\eta_0$ are evolved **backward** as well as forward, so $N(-\eta_{\rm ref})$
is measured, not extrapolated.

| $k\eta_B$ | $\eta_{\rm ref}/\eta_B$ | S-lab $\ \vert\zeta_a/\zeta_b\vert$ ($\mathcal P$ ratio) | S-ABS0 | S-ad4 | $\vert\beta\vert^2$ after (lab / ABS0 / ad4) |
|---|---|---|---|---|---|
| 0.1 | 42.3 | **198.71** (3.95e4) | **26.83** (720.0) | **198.77** (3.95e4) | 1.97e4 / 2.52e3 / 1.98e4 |
| 0.3 | 12.5 | **9.100** (82.81) | **7.631** (58.22) | **9.103** (82.87) | 40.9 / 30.9 / 40.9 |
| 1 | 10.0 | **1.0464** (1.0950) | **1.0390** (1.0795) | **1.0467** (1.0957) | 4.75e-2 / 4.01e-2 / 4.78e-2 |
| 3 | 10.0 | **1.0000** (1.000001) | 1.0000 | 1.0000 | 2.8e-7 / 2.4e-6 / 2.8e-7 |
| 10 | 10.0 | **1.0000** (1.000000) | 1.0000 | 1.0000 | $<10^{-8}$ / 3.3e-8 / $<10^{-8}$ |

Notes carried by the run: for S-ABS0 the order-zero state is itself excited relative to the
adiabatic vacuum at $-\eta_{\rm ref}$ ($N(-\eta_{\rm ref}) = 7.00$ at $k\eta_B=0.1$, $1.08$ at $0.3$,
$1.0006$ at $1$), which is why its *ratio* is smaller than S-lab's while its absolute post-bounce
$|\beta|^2$ is only a factor $\sim8$ below. S-ad4 could not be built at $\eta_0=-3\eta_B$ for
$k\eta_B\le0.3$ (there $k^2<\mathfrak W$: a super-Hubble mode has no adiabatic vacuum); the run
relocated it to the latest pre-bounce time with $k^2\ge10\,\mathfrak W$ ($-42.3\eta_B$ and
$-12.5\eta_B$ respectively) and records the relocation. For legs with no such time anywhere on the
grid — the long leg $k_1=0.02k$ of the squeezed triangle — the code falls back to the exact dust
positive-frequency solution at $\eta\to-\eta_{\rm far}$, which *is* the adiabatic vacuum to all
orders there, and records the fallback.

**Result of §2.** The linear bounce imprint is real and is confined to $k\eta_B\lesssim1$: the
power spectrum is amplified by $4\times10^{4}$ at $k\eta_B=0.1$, by $83$ at $0.3$, by $1.095$ at
$1$, and by $1+10^{-6}$ at $3$ — i.e. it switches off within a factor $\sim3$ in $k$ above
$k_{\rm LQC}\eta_B=1.06$, in agreement with ABS's own statement that the power spectrum is affected
only for $k\lesssim k_{\rm LQC}$ (their §IV A). **The initial state changes this by less than a
factor 8, and in the direction of *less* amplification, not more.**
