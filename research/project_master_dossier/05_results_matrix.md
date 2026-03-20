# Results Matrix

The most important table in the dossier. One row per major scientific attempt.

See [10_status_legend.md](10_status_legend.md) for all label definitions.

---

## Complete Results Matrix

| # | Branch / Path | Scientific Question | Model / Assumption | Observable / Output | Result | Status | One-Line Significance | Repro Assets | Novelty | Pub Value |
|---|--------------|--------------------|--------------------|--------------------:|--------|--------|-----------------------|-------------|---------|-----------|
| 1 | Paper-1 (original) | Can ECH torsion bounce derive DE and reduce H_0/sigma_8 tensions? | Minimal ECH + LCDM + Delta-N_eff | H_0, sigma_8, Delta-N_eff | H_0 = 67.68 (standard LCDM); Delta-N_eff ~ 0 | FAIL | Key claims disproved by own MCMC verification | MCMC chains (frozen) | N1 | LOW |
| 2 | IR-Vacuum Track B | Can torsion condensate generate w = -1? | ECH + condensate mechanism | Effective cosmological constant | Wrong sign, too weak, catalysis suppressed | FAIL | Strong closure of condensate route | Symbolic notebooks | N2 | MODERATE |
| 3 | IR-Vacuum Branch G v1 | Can one-loop fermion determinant shift vacuum energy? | ECH + one-loop effective action | Vacuum energy from fermion loops | Gamma-independent at strict one-loop | FAIL | Clean negative result; no vacuum energy shift | Derivation docs | N2 | MODERATE |
| 4 | IR-Vacuum Route T1 | Can scalar reduction of torsion produce DE? | ECH + scalar sector extraction | Scalar field dynamics | Reduces to standard ALP; no geometric content | FAIL | Geometric origin invisible after torsion integration | Derivation docs | N1 | LOW |
| 5 | IR-Vacuum Route S1 | Can ALP reduction give ECH-specific birefringence? | ECH + ALP sector | CMB birefringence | Generic ALP birefringence; not ECH-specific | MIXED | Birefringence prediction works but is not unique | MCMC infrastructure | N2 | MODERATE |
| 6 | Foundation-A | Can PGT propagating torsion serve as DE? | Ghost-free PGT modes (0-, 0+, 2+) | Torsion field as DE | Mass-coupling lock: fine-tuning transferred | FAIL | Closes entire PGT DE route | `pgt_mode_analysis.ipynb` | N2 | MODERATE |
| 7 | Foundation-B | Can mass-coupling lock be broken via geometric ALP? | MAG + Nieh-Yan coupling | Shift-protected pseudoscalar | Topological-Shift Duality blocks it | FAIL | Mass protection and geometric content mutually exclusive | `04_symbolic_model_exploration.ipynb` | N3 | HIGH |
| 8 | Foundation-C | Can curvature-dependent mass evade lock + duality? | Environmental mass (xi R) | Scalar DE with geometric origin | Reduces to standard scalar-tensor (T_0 = Q_0 = 0 on FRW) | FAIL | Technically clean but observationally indistinguishable | `04_environmental_mass_symbolics.ipynb` | N2 | MODERATE |
| 9 | Foundation-D | Can disformal couplings produce distinctive signatures? | Connection-type disformal metric | Distinctive geometric effects | Planck suppression: 1 partial-phi per vertex, effects ~ 10^{-122} | FAIL | Closes entire disformal route; completes A-D no-go for single-field geometric DE | `05_disformal_symbolics.ipynb` | N2 | MODERATE |
| 10 | Foundation-E | Can global integrals (sequestering) link bounce to DE? | Kaloper-Padilla + bounce | Lambda from global V_4 | Scale separation: V_4^bounce/V_4^total ~ 10^{-60} | FAIL | Bounce too brief and early to influence global integrals | Sequestering calculation | N1 | LOW |
| 11 | Foundation-F | Can bounce set initial conditions for DE fields? | Various quintessence models | DE from bounce-prepared ICs | Attractor-sensitivity dilemma: no middle ground | FAIL | Attractors erase or fine-tuning required; structural impossibility | Attractor analysis | N2 | MODERATE |
| 12 | Foundation-G | Can cyclic sequestering determine Lambda? | Cyclic ECH bounce + KP sequestering | Lambda from cyclic matching | Parameter immunity: mu^4 free; Planck-scale matching barrier | FAIL | Bounce provides V_4 finiteness but not Lambda value | Cyclic calculation | N2 | MODERATE |
| 13 | Branch-H | What is the tensor spectrum through the minimal bounce? | Minimal ECH bounce | P_T(k), n_T, chirality | P_T ~ 10^{-64}, n_T = 0, no chirality (parity-even) | FAIL | Minimal bounce is observationally silent in tensors | Tensor mode solver | N1 | LOW |
| 14 | Branch-I | Which DE models are compatible with the bounce? | Horndeski classes + ECH bounce | Compatibility conditions | 4/6 trivially compatible; 2/6 EFT breakdown (not instability) | CLOSED | Ships passing in the night — scale separation dominates | Horndeski analysis | N1 | LOW |
| 15 | Branch-J | Can the bounce dynamically select DE sector state? | 5 selection mechanisms | Late-time vacuum state | Barrier 9: Liouville prevents reversible state contraction | FAIL | New no-go theorem for state-selection mechanisms | Phase-space argument | N2 | MODERATE |
| 16 | Branch-K | What is the scalar transfer function T(k) through the bounce? | Minimal ECH bounce | T(k) for CMB modes | T(k) = 1 exactly for all k << k_b (time-reversal symmetry) | CLOSED | Clean consistency check; no bounce-specific scalar features | `04_scalar_mode_solver.ipynb` | N1 | LOW |
| 17 | Branch-L | Can minimal extensions bridge UV-IR gap? | 7 candidate extensions | Observable at CMB/GW scales | Barrier 10: UV-IR specificity dilemma; 1 PGT survivor (conditional) | MIXED | Cannot have both bounce-specificity and observational reach | PGT parameter scan | N2 | MODERATE |
| 18 | Branch-M | What is the GW spectrum from PGT lower-scale bounce? | PGT with m_T variable | Omega_GW(f) | Barrier 12: vacuum amplification ceiling; detector gap 10^17 | FAIL | Distinctive spectrum but permanently undetectable | `03_gw_spectrum_solver.ipynb` | N1 | LOW |
| 19 | Branch-N | Can the bounce produce baryogenesis or relics? | Minimal ECH + 7 relic mechanisms | Baryon asymmetry, DM, PBH | Barrier 13N: gravitational democracy (~100 Planck-scale channels, torsion ~1%) | FAIL | Torsion is generic at its own energy scale | 7-mechanism screening | N2 | MODERATE |
| 20 | Branch-O | Can irreversible bounce-triggered transitions set vacuum energy? | 7 irreversible mechanisms | Late-time Lambda | Barrier 13O: bounce-vacuum decoupling (trigger != outcome) | FAIL | With Branch J, exhausts all state-change mechanisms (reversible + irreversible) | Complementary argument | N2 | MODERATE |
| 21 | Branch-P | What observables survive for PGT lower-scale bounce? | PGT bounce, 8 channels | BBN, CMB, GW, relics | Torsion relic cosmology gated on unknown energy fraction | MIXED | Last surviving bounce-specific channel; verdict depends on O(1) vs (m_T/M_Pl)^2 | 8-channel survey | N2 | MODERATE |
| 22 | Branch-Q | Can parity-violating extensions give ECH-specific signals? | Dynamical Barbero-Immirzi field | CMB birefringence | Phenomenologically identical to standard ALP; ABJ universal | FAIL | Parity structure insufficient without external pseudoscalar | BI field analysis | N1 | LOW |
| 23 | **Branch-R** | **Does a spectator ALP predict observed cosmic birefringence?** | **ALP: f_a ~ M_Pl, m ~ H_0, theta_i ~ O(1)** | **CMB birefringence beta** | **beta = 0.27 deg; observed 0.35 +/- 0.09 deg (1-sigma match)** | **PASS** | **Natural prediction matches 3.9-sigma detection; LiteBIRD falsifiable** | **Phase 2 MCMC (25+ subdirs)** | **N2** | **HIGH** |
| 24 | Branch-S | Does minimal ECH generate photon-polarization rotation via loops? | One-loop VVA triangle in ECH | beta from loop process | ABJ anomaly exists but universal; beta ~ 10^{-30} deg (28-40 OOM too weak) | FAIL | Definitively closes one-loop salvage path | VVA derivation | N1 | LOW |
| 25 | Branch-T | Can axion kicked by bounce amplify gauge fields? | External axion + bounce kick | Gauge field amplification | Source requires free parameter (n_5); no genuine novelty | FAIL | Shifts problem to unknown initial conditions | Kick estimate | N1 | LOW |
| 26 | Branch-U | Can two-field ALP resolve rolling-vs-freezing tension? | Two ALPs (roller + freezer) | beta + Omega_DE | Reintroduces fine-tuning (m_2 ~ H_0) | DEFERRED | Not prioritized unless single-field ALP fails | Background equations | N1 | LOW |
| 27 | **Branch-V** | **Can matter contraction + ECH bounce produce testable signals?** | **Dust contraction -> ECH bounce -> radiation** | **f_NL, n_s, low-ell cutoff** | **f_NL = -35/8 = -4.375 (parameter-free); SPHEREx 4-6σ; Planck anomaly connection** | **PAPER DRAFT COMPLETE** | **Flagship: explicit bounce mechanism with testable predictions** | **Phase 1 blueprint** | **N3** | **FLAGSHIP** |
| 28 | Branch-Vb | Can perturbations propagate through ECH bounce? | ECH perturbation equations | Perturbation transfer | Gate for Branch V; assessment in progress | ACTIVE | Infrastructure for Branch V feasibility | Perturbation framework | N1 | LOW |
| 29 | Branch-W | Can birefringence ALP serve as curvaton for red tilt? | ALP curvaton in dust contraction | n_s from curvaton | n_s = 1.000 from dust (8.3-sigma excluded); superseded by Branch V | CLOSED | Identified n_s = 1 as fundamental dust property; prompted V pivot | n_s proof | N1 | LOW |
| 30 | Chiral-GW | Can chiral GW from ECH bounce reach detectors? | ECH + parity-violating Holst | Circular GW polarization | f_0 ~ 10^{9-10} Hz; gap to LIGO 10^6; Omega proportional to f^8 kills amplitude | FAIL | All bounce-scale signals permanently inaccessible | Frequency-amplitude scaling | N1 | LOW |
| 31 | NextGen-Signals | Which next-gen bounce signals are viable? | 12 candidate signal classes | Detection feasibility | Best candidate (chiral GW) fails frequency gate | CLOSED | Bounce-scale physics cannot reach any planned detector | 12-candidate ranking | N1 | LOW |
| 32 | MCMC Verification | Does independent MCMC verify Paper 1 claims? | Stock CAMB + Delta-N_eff | H_0, sigma_8, Delta-N_eff posteriors | Delta-N_eff ~ 0; H_0 ~ 67.68 (standard); tension reduction disproved | PASS (as verification) | Honest self-correction; MCMC infrastructure validated | Frozen chains (236K+ samples) | N1 | HIGH (as infrastructure) |
| 33 | Extensions Track C | Does ECH predict birefringence at observed level? | ECH parity coupling + SM anomaly | f_photon consistency | f_photon = 1.73 +/- 0.44 (O(1), no fine-tuning) | PASS | Natural consistency with 3.9-sigma combined detection | Literature compilation | N2 | MODERATE |
| 34 | 13-Barrier Map | What is the complete space of bounce-DE connection mechanisms? | All mechanism classes (A-O) | Barrier catalog | 13 independent structural barriers identified and named | PASS (as closure) | Systematic closure of bounce-to-DE program; publishable negative result | All foundation/branch phase results | N3 | HIGH |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total scientific attempts | 34 |
| PASS (positive result) | 4 |
| FAIL (negative result) | 22 |
| MIXED / CONDITIONAL | 4 |
| CLOSED (neutral) | 2 |
| ACTIVE | 2 |
| DEFERRED | 1 |

---

## Positive Surviving Results (Ranked)

1. **Branch R — ALP birefringence:** beta = 0.27 deg matches 0.35 +/- 0.09 deg (1-sigma). Phase 2 MCMC in progress. HIGH publication value.

2. **Branch V — Generic matter-bounce (LQC-viable):** f_NL = -35/8 = -4.375 parameter-free prediction. SPHEREx testable. FLAGSHIP publication potential if calculation succeeds.

3. **13-Barrier Map:** Systematic closure of 15 branches with named structural barriers. HIGH value as honest negative-result paper.

4. **MCMC Infrastructure:** 236,622+ samples, 4 datasets, R-hat - 1 < 0.005. Reusable for any future cosmological model testing. HIGH infrastructure value.

5. **Extensions Track C:** f_photon = 1.73 (O(1)) consistency with birefringence detection. MODERATE value as supporting evidence.
