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
