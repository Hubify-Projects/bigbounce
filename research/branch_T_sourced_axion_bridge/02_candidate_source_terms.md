# Branch T: Candidate Source Terms for Axion Kick

**Date:** 2026-03-16

---

## Setup

External ALP field "a" with mass m_a and decay constant f_a. We seek couplings that source da/dt during the bounce.

General EOM for a in FRW:

    a-double-dot + 3 H a-dot + m_a^2 a = S(t)

where S(t) is the source from the bounce. We need S(t) large enough during the bounce epoch to produce da-dot ~ 2 f_a H (i.e., xi >= 1).

---

## Candidate A: Derivative coupling to axial current

**Action term:** (1/f_a) partial_mu(a) J^{5 mu}

**Symmetry:** Allowed by shift symmetry a -> a + const. Dimension-5, standard ALP-fermion coupling.

**Source in FRW:** S_A = (1/f_a) [J-dot^5_0 + 3H J^5_0]

**Minimal or new?** Standard. Present in any ALP-fermion theory.

**Assessment:**
- J^5_0 = n_5 = n_R - n_L (net chiral number density)
- At the bounce, J-dot^5_0 can be large if n_5 changes rapidly
- BUT: in thermal equilibrium, n_5 = 0 unless there is a prior chiral asymmetry mu_5
- A nonzero n_5 is a FREE PARAMETER, not sourced by the bounce geometry
- Fluctuations: delta(n_5) ~ T^{3/2} per Hubble volume, stochastic not coherent
- The gravitational chiral anomaly partial_mu J^{5 mu} ~ R-tilde-R = 0 on FRW, so the bounce does not anomalously generate n_5

**Risk level:** HIGH. Source vanishes in thermal equilibrium on FRW.

---

## Candidate B: Coupling to gravitational Pontryagin density

**Action term:** (a / f_a) R_{ab} wedge R^{ab} = (a / f_a) R-tilde-R

**Symmetry:** Parity-odd, shift-symmetric under a -> a + const (total derivative). Standard gravitational Chern-Simons coupling.

**Source in FRW:** S_B = -(1/f_a) d(R-tilde-R)/da ... but actually the source comes from varying the action:

    S_B = (1/f_a) R-tilde-R

**Minimal or new?** Standard in gravitational ALP literature.

**Assessment:**
- R-tilde-R = 0 on exact FRW (established in Branch H)
- R-tilde-R = epsilon^{mu nu rho sigma} R_{mu nu alpha beta} R_{rho sigma}^{alpha beta}
- For FRW: the Riemann tensor is determined by H(t) and a(t), and the contraction with epsilon vanishes by the symmetry of the Friedmann spacetime
- Nonzero only for perturbations or anisotropies

**Risk level:** FATAL on FRW. Dead at background level.

---

## Candidate C: Coupling to torsion pseudoscalar invariant

**Action term:** (a / f_a) epsilon^{mu nu rho sigma} T_{mu nu alpha} T_{rho sigma}^{alpha}

**Symmetry:** Parity-odd, allowed. Dimension-6 in the torsion formulation.

**Source in FRW:** After torsion elimination (T^mu_{nu rho} = kappa * spin density), this becomes:

    S_C ~ (kappa^2 / f_a) (J^5)^2

where kappa^2 ~ G^2 ~ M_Pl^{-4}.

**Minimal or new?** Arises naturally in ECH with ALP coupling. Not independent of Candidate A after torsion elimination.

**Assessment:**
- (J^5)^2 = (J^5_0)^2 - |J^5_i|^2
- In FRW: (J^5)^2 ~ n_5^2
- Source: S_C ~ G^2 n_5^2 / f_a ~ M_Pl^{-4} n_5^2 / f_a
- Even at n_5 ~ M_Pl^3 (maximal): S_C ~ M_Pl^2 / f_a ~ M_Pl (for f_a ~ M_Pl)
- The time integral: Delta(a-dot) ~ S_C * t_bounce ~ M_Pl * M_Pl^{-1} ~ 1 ... in Planck units
- But xi ~ a-dot / (f_a H) ~ 1/(M_Pl * M_Pl) * M_Pl ... need to be more careful
- After careful dimensional analysis (see File 03): this reduces to the same estimate as Candidate A
- NOT independent after torsion elimination

**Risk level:** HIGH. Same as A after algebraic elimination of torsion.

---

## Candidate D: Immirzi-axion mixing

**Action term:** Replace gamma -> gamma_0 + a/f_a in the Holst action: (1/2kappa) (gamma_0 + a/f_a)^{-1} e^I wedge e^J wedge R_{IJ}

**Symmetry:** Breaks shift symmetry of a (appears without derivative). Requires specific UV completion.

**Source in FRW:** This IS Branch Q. After torsion elimination, the Immirzi parameter drops out of the classical equations on-shell. The axion "a" becomes a spectator.

**Minimal or new?** This is the dynamical Immirzi field, extensively studied (Taveras-Yunes, Calcagni-Mercuri).

**Assessment:**
- On FRW, the classical Immirzi parameter is topological (multiplies the Holst term, which is a boundary term when torsion is eliminated)
- The axion gets no source from the gravitational sector on FRW
- Quantum corrections (loops) could generate a source, but these are Planck-suppressed
- Branch Q established: reduces to generic ALP with no bounce-specific kick

**Risk level:** FATAL. Already closed by Branch Q.

---

## Candidate E: Coupling to Nieh-Yan density

**Action term:** (a / f_a) N, where N = d(e^I wedge T_I) = T^I wedge T_I - R_{IJ} wedge e^I wedge e^J

**Symmetry:** Parity-odd (N is a pseudoscalar density). Topological in Riemann-Cartan geometry (exact differential).

**Source in FRW:** After torsion elimination:

    N = kappa^2 (J^5)^2 + [Holst-type boundary term]

The boundary term is a total derivative on FRW and does not contribute to the EOM.

**Minimal or new?** Well-studied (Nieh-Yan 1982, Chandia-Zanelli, recent work by Karananas et al.).

**Assessment:**
- Same as Candidate C after torsion elimination
- The Nieh-Yan form is topological in strict RC geometry, so a*N is a total derivative
- In MAG (metric-affine gravity), N is NOT topological — but this opens non-minimal territory (Foundation B result)
- Even in the non-topological MAG case: after torsion elimination, source reduces to (J^5)^2 terms
- No independent bounce kick

**Risk level:** FATAL unless we leave Riemann-Cartan geometry. Same as C in minimal ECH.

---

## Candidate F: Parametric resonance from oscillating scale factor

**Action term:** Standard ALP mass term m_a^2 a^2/2, no special coupling.

**Mechanism:** The bounce itself involves H(t) passing through zero. If the post-bounce expansion has oscillatory features (e.g., reheating oscillations), the 3H a-dot friction term oscillates, potentially driving parametric resonance of the axion.

**Symmetry:** No new couplings needed.

**Source in FRW:** Not a source term per se, but a time-dependent friction coefficient.

**Assessment:**
- This works in standard preheating after inflation (Kofman-Linde-Starobinsky)
- At the bounce: H changes sign once (contraction -> expansion), not oscillatory
- No parametric resonance from a single zero-crossing
- Post-bounce oscillations of H require a specific potential (e.g., phi^2 inflaton)
- In ECH bounce: the bounce is driven by spin density, not a scalar potential
- H(t) is monotonic near the bounce: H < 0 -> H = 0 -> H > 0, no oscillation
- Post-bounce: standard radiation domination, H ~ 1/(2t), no oscillations

**Risk level:** FATAL. No oscillatory H(t) in spin-torsion bounce.

---

## Candidate G: Non-equilibrium chiral production at the bounce

**Action term:** Same as Candidate A, but with a specific physical mechanism for generating n_5.

**Mechanism:** At extreme densities near the bounce, particle physics processes might produce a transient chiral asymmetry:
- Sphaleron-like processes at T ~ M_Pl
- Gravitational particle production with chiral asymmetry
- Schwinger effect in strong gravitational fields

**Source in FRW:** Same coupling as A, but with a dynamically generated n_5(t).

**Assessment:**
- Sphaleron rate: Gamma ~ alpha_W^5 T^4. At T ~ M_Pl, Gamma ~ M_Pl^4, which is FAST — equilibrates chirality, does not produce it
- Gravitational particle production: produces particles but NOT a net chiral asymmetry on FRW (parity-symmetric background)
- Schwinger effect: requires E.B != 0, which requires pre-existing gauge field configuration — circular argument
- The gravitational chiral anomaly: partial_mu J^{5 mu} ~ R-tilde-R = 0 on FRW
- Bottom line: FRW symmetry prevents any parity-odd quantity from being generated at the background level

**Risk level:** FATAL. FRW parity symmetry kills all dynamical n_5 generation.

---

## Summary of candidates

| ID | Coupling | Independent after torsion elim.? | Source on FRW? | Bounce-specific? | Risk |
|----|----------|----------------------------------|----------------|------------------|------|
| A  | partial a . J^5 / f_a | Yes (external ALP) | Requires n_5 != 0 | No (n_5 is free param) | HIGH |
| B  | a R-tilde-R / f_a | Yes | NO (R-tilde-R = 0) | N/A | FATAL |
| C  | a epsilon T T / f_a | No (= A after elim.) | Same as A | Same as A | HIGH |
| D  | Immirzi mixing | No (Branch Q) | NO | N/A | FATAL |
| E  | a N / f_a (Nieh-Yan) | No (= C in RC) | Same as C | Same as C | FATAL |
| F  | Parametric resonance | N/A | No oscillatory H | N/A | FATAL |
| G  | Dynamical n_5 | Same as A | No (FRW parity) | N/A | FATAL |

**Only Candidate A survives initial screening,** and it requires a pre-existing chiral asymmetry n_5 that is not sourced by the bounce itself.
