# Branch Registry

Structured registry of every major branch, foundation, and program in the research program.

See [10_status_legend.md](10_status_legend.md) for definitions of all status and rating labels.

---

## Pre-Branch Era

### Paper 1 (Original Manuscript)

| Field | Value |
|-------|-------|
| **ID** | Paper-1 |
| **Goal** | Derive dark energy from ECH spin-torsion bounce; fit H_0 and sigma_8 tensions |
| **Status** | SUPERSEDED |
| **One-line significance** | Ambitious but overclaimed; MCMC verification disproved key tension-reduction claims |
| **Main files** | `arxiv/main.tex`, `arxiv/main.pdf`, `paper/` (38 section files) |
| **Publication potential** | LOW (in original form) |
| **Novelty** | N1 — framework is correct but claims were inflated |
| **Reusable assets** | ECH action derivation, modified Friedmann equations, Cobaya configs |

### Paper 1.2 (Restructured Manuscript)

| Field | Value |
|-------|-------|
| **ID** | Paper-1.2 |
| **Goal** | Honest assessment: ECH framework + structural closure + ALP birefringence consistency |
| **Status** | ACTIVE (nearly ready to write) |
| **One-line significance** | The actual publishable paper — closure + surviving positive result |
| **Main files** | `research/paper_1_2_archive/` (32 files), `research/final_phase/` |
| **Publication potential** | HIGH |
| **Novelty** | N2-N3 — systematic closure is new; ALP prediction matches data |
| **Reusable assets** | Claims lock, figure plan, referee simulation, submission checklist |

### IR Vacuum Program (4-Route Closure)

| Field | Value |
|-------|-------|
| **ID** | IR-Vacuum |
| **Goal** | Test all 4 minimal routes to w = -1 from the ECH framework |
| **Status** | CLOSED (all 4 routes fail) |
| **One-line significance** | Definitively establishes the framework as phenomenological at minimal-model level |
| **Main files** | `research/paper2/ir_vacuum_program/` (22 subdirectories), `supplement_negative_results.pdf` |
| **Publication potential** | MODERATE (as companion technical note) |
| **Novelty** | N2 — systematic closure not previously done for ECH |
| **Reusable assets** | Negative-result supplement (272 KiB, publication-quality) |

---

## Foundations A-G (Mechanism Class Testing)

### Foundation A — Propagating Torsion in PGT

| Field | Value |
|-------|-------|
| **ID** | Foundation-A |
| **Goal** | Can ghost-free propagating torsion modes serve as dark energy? |
| **Status** | CLOSED |
| **One-line significance** | Mass-coupling lock: m and g tied by gravitational constant; fine-tuning transferred, not eliminated |
| **Main files** | `research/foundation_A_pgt/phase1_verdict.md`, `phase2/` (13 follow-up tests) |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N2 — mass-coupling lock theorem is original |
| **Reusable assets** | `pgt_mode_analysis.ipynb`, mass formula derivation |

### Foundation B — Breaking the Mass-Coupling Lock

| Field | Value |
|-------|-------|
| **ID** | Foundation-B |
| **Goal** | Can the mass-coupling lock be broken via geometric ALP (Nieh-Yan in MAG)? |
| **Status** | CLOSED |
| **One-line significance** | Topological-Shift Duality: mass protection and geometric content are mutually exclusive |
| **Main files** | `research/foundation_B_lock_breaking/phase1_results.md`, `phase2/02_nieh_yan_mag_analysis.md` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N3 — Topological-Shift Duality theorem is original and general |
| **Reusable assets** | `04_symbolic_model_exploration.ipynb`, MAG Nieh-Yan computation |

### Foundation C — Environmental Mass Mechanisms

| Field | Value |
|-------|-------|
| **ID** | Foundation-C |
| **Goal** | Can curvature-dependent mass evade the lock and duality? |
| **Status** | CLOSED |
| **One-line significance** | Scalar-Tensor Universality: on FRW, all geometric scalars reduce to known EFT (T_0 = Q_0 = 0) |
| **Main files** | `research/foundation_C_environmental_mass/phase1_results.md` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N2 — FRW wash-out analysis is original |
| **Reusable assets** | `04_environmental_mass_symbolics.ipynb` |

### Foundation D — Disformal Coupling Survival

| Field | Value |
|-------|-------|
| **ID** | Foundation-D |
| **Goal** | Can disformal effective metrics produce distinctive geometric signatures? |
| **Status** | CLOSED |
| **One-line significance** | Planck Suppression Theorem: 1 partial-phi per vertex from connection coupling; all distinctive effects ~ 10^{-122} |
| **Main files** | `research/foundation_D_disformal_survival/phase1_results.md` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N2 — connection-coupling argument is original |
| **Reusable assets** | `05_disformal_symbolics.ipynb` |

### Foundation E — Global Vacuum Integrals

| Field | Value |
|-------|-------|
| **ID** | Foundation-E |
| **Goal** | Can global spacetime integrals (Kaloper-Padilla sequestering) link bounce to DE? |
| **Status** | CLOSED |
| **One-line significance** | Scale Separation: bounce V_4 / total V_4 ~ 10^{-60}; bounce contribution negligible |
| **Main files** | `research/foundation_E_global_vacuum/phase1_results.md`, `phase2_curvature_constraint/` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N1 — scale separation is known; application to bounce-sequestering is incremental |
| **Reusable assets** | Sequestering-on-bounce calculation |

### Foundation F — Initial Conditions from Bounce

| Field | Value |
|-------|-------|
| **ID** | Foundation-F |
| **Goal** | Can bounce physics determine initial conditions for late-time DE fields? |
| **Status** | CLOSED |
| **One-line significance** | Attractor-Sensitivity Dilemma: attractors erase memory OR fine-tuning required; no middle ground |
| **Main files** | `research/foundation_F_initial_conditions/phase1_results.md` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N2 — structural impossibility framing is original |
| **Reusable assets** | Attractor analysis for 4 quintessence models |

### Foundation G — Bounce-Conditioned Vacuum Selection

| Field | Value |
|-------|-------|
| **ID** | Foundation-G |
| **Goal** | Can the bounce, via cyclic sequestering, determine late-time Lambda? |
| **Status** | CLOSED |
| **One-line significance** | Parameter Immunity: cyclic matching does not constrain mu^4; bounce provides infrastructure, not content |
| **Main files** | `research/foundation_G_bounce_vacuum_selection/phase1_results.md`, `phase2_cyclic_sequestering/` |
| **Publication potential** | MODERATE (as part of closure paper) |
| **Novelty** | N2 — Planck-scale matching barrier is original |
| **Reusable assets** | Cyclic sequestering on spin-torsion bounce calculation |

---

## Branches H-O (Post-AG Pivot: Bounce-Only Tests)

### Branch H — Bounce-Only Tensor Spectrum

| Field | Value |
|-------|-------|
| **ID** | Branch-H |
| **Goal** | Compute tensor perturbation spectrum through the spin-torsion bounce |
| **Status** | CLOSED |
| **One-line significance** | P_T ~ 10^{-64}, n_T = 0; parity-even interaction prevents chirality; unobservable |
| **Main files** | `research/branch_H_bounce_only/` (problem statement, candidates, ranking, tensor/parity subdirs) |
| **Publication potential** | LOW (null result, technically clean) |
| **Novelty** | N1 — time-reversal symmetry resolution of growing mode is known |
| **Reusable assets** | Tensor mode solver infrastructure |

### Branch I — Bounce-Compatible Dark Energy

| Field | Value |
|-------|-------|
| **ID** | Branch-I |
| **Goal** | Which DE models are compatible with a spin-torsion bounce? |
| **Status** | CLOSED (WEAK) |
| **One-line significance** | Scale separation dominates; 4/6 Horndeski classes trivially compatible, 2/6 have EFT breakdown |
| **Main files** | `research/branch_I_bounce_compatible_DE/` (5 files + Horndeski subdir) |
| **Publication potential** | LOW |
| **Novelty** | N1 — scale separation argument is well-known |
| **Reusable assets** | Horndeski stability at Planck curvature analysis |

### Branch J — State Selection via Bounce

| Field | Value |
|-------|-------|
| **ID** | Branch-J |
| **Goal** | Can the bounce dynamically select or prepare a dark-energy sector state? |
| **Status** | CLOSED |
| **One-line significance** | Barrier 9: Liouville's theorem prevents state contraction for reversible selection |
| **Main files** | `research/branch_J_state_selection/` (5 files + phase1_results) |
| **Publication potential** | MODERATE (clean no-go theorem) |
| **Novelty** | N2 — Barrier 9 is new and applies specifically to state-selection mechanisms |
| **Reusable assets** | Phase-space conservation argument |

### Branch K — Scalar Perturbations Through Bounce

| Field | Value |
|-------|-------|
| **ID** | Branch-K |
| **Goal** | Compute scalar transfer function T(k) through the bounce |
| **Status** | CLOSED (GENERIC) |
| **One-line significance** | T(k) = 1 exactly for all observable modes; time-reversal symmetry; no bounce-specific features |
| **Main files** | `research/branch_K_scalar_perturbations/` (5 files + notebook + phase1_results) |
| **Publication potential** | LOW (consistency check, not discovery) |
| **Novelty** | N1 — confirms known result in ECH context |
| **Reusable assets** | `04_scalar_mode_solver.ipynb` (Jupyter notebook) |

### Branch L — UV to IR Bridge

| Field | Value |
|-------|-------|
| **ID** | Branch-L |
| **Goal** | Identify minimal extensions bridging 10^28 scale gap between bounce and observables |
| **Status** | MIXED |
| **One-line significance** | Barrier 10: UV-IR specificity dilemma; 1 survivor (PGT lower-scale bounce) conditional |
| **Main files** | `research/branch_L_uv_ir_bridge/` (5 files + PGT parameter scan + phase1_results) |
| **Publication potential** | MODERATE (sharp dichotomy result) |
| **Novelty** | N2 — specificity dilemma framing is original |
| **Reusable assets** | PGT parameter scan infrastructure |

### Branch M — PGT Bounce GW Spectrum

| Field | Value |
|-------|-------|
| **ID** | Branch-M |
| **Goal** | Compute GW spectrum from PGT lower-scale bounce |
| **Status** | CLOSED (GENERIC) |
| **One-line significance** | Barrier 12: vacuum amplification ceiling; minimum detector gap 10^17; spectrum distinctive but undetectable |
| **Main files** | `research/branch_M_pgt_bounce_gw/` (6 files + notebook + phase1_results) |
| **Publication potential** | LOW (undetectable) |
| **Novelty** | N1 — confirms known vacuum amplification scaling |
| **Reusable assets** | `03_gw_spectrum_solver.ipynb`, detector forecast |

### Branch N — Baryogenesis and Relics

| Field | Value |
|-------|-------|
| **ID** | Branch-N |
| **Goal** | Can the bounce drive baryogenesis or produce observable relics? |
| **Status** | CLOSED |
| **One-line significance** | Barrier 13 Face N: gravitational democracy — torsion is 1 of ~100 Planck-scale channels (~1% contribution) |
| **Main files** | `research/branch_N_baryogenesis_relics/` (5 files + phase1_results) |
| **Publication potential** | MODERATE (clean null result with named barrier) |
| **Novelty** | N2 — gravitational democracy concept applied to bounce relics is original |
| **Reusable assets** | 7-mechanism screening framework |

### Branch O — Hidden-Sector Vacuum Selection

| Field | Value |
|-------|-------|
| **ID** | Branch-O |
| **Goal** | Can irreversible transitions (phase transitions, tunneling) triggered by bounce determine vacuum energy? |
| **Status** | CLOSED |
| **One-line significance** | Barrier 13 Face O: bounce-vacuum decoupling — trigger and outcome structurally separated |
| **Main files** | `research/branch_O_hidden_sector_vacuum/` (5 files + phase1_results) |
| **Publication potential** | MODERATE (closes irreversible route; complements Branch J reversible closure) |
| **Novelty** | N2 — together with J, exhausts the space of state-change mechanisms |
| **Reusable assets** | Reversible + irreversible exhaustion argument |

---

## Branches P-W (Extensions and Positive Results)

### Branch P — PGT Lower-Scale Bounce Phenomenology

| Field | Value |
|-------|-------|
| **ID** | Branch-P |
| **Goal** | Survey all observable channels for PGT lower-scale bounce |
| **Status** | MIXED (gated on torsion energy fraction) |
| **One-line significance** | Strongest survivor: torsion relic cosmology with BBN constraint IF energy fraction ~ O(1) |
| **Main files** | `research/branch_P_pgt_bounce_program/` (6 files + torsion relic gating + phase1_results) |
| **Publication potential** | MODERATE (conditional on energy fraction calculation) |
| **Novelty** | N2 — systematic PGT observable survey is original |
| **Reusable assets** | 8-channel observable survey framework |

### Branch Q — Sourced Parity Violation

| Field | Value |
|-------|-------|
| **ID** | Branch-Q |
| **Goal** | Can parity-violating extensions produce observable ECH-specific signals? |
| **Status** | CLOSED (WEAK) |
| **One-line significance** | Phenomenologically identical to standard ALP after torsion elimination; ABJ anomaly is universal |
| **Main files** | `research/branch_Q_sourced_parity/` (5 files + exact elimination subdir + phase1_results) |
| **Publication potential** | LOW |
| **Novelty** | N1 — confirms known ABJ universality |
| **Reusable assets** | Dynamical Barbero-Immirzi field analysis |

### Branch R — ALP Cosmic Birefringence

| Field | Value |
|-------|-------|
| **ID** | Branch-R |
| **Goal** | Generic ALP birefringence phenomenology motivated by ECH |
| **Status** | ACTIVE / PROMISING |
| **One-line significance** | beta = 0.27 deg prediction matches observed 0.35 +/- 0.09 deg within 1-sigma; LiteBIRD falsifiable |
| **Main files** | `research/branch_R_alp_birefringence/` (5 files + novelty audit + phase2_mcmc/) |
| **Publication potential** | HIGH |
| **Novelty** | N2 — prediction matches data; not unique to ECH but well-motivated |
| **Reusable assets** | Phase 2 MCMC infrastructure (25+ subdirectories), Cobaya + axionCAMB setup |

### Branch S — Photon-Torsion Vertex (One-Loop)

| Field | Value |
|-------|-------|
| **ID** | Branch-S |
| **Goal** | Does minimal ECH generate effective photon-polarization rotation via loops? |
| **Status** | CLOSED |
| **One-line significance** | ABJ anomaly exists but is universal (not ECH-specific); beta ~ 10^{-30} deg (28-40 orders too weak) |
| **Main files** | `research/branch_S_photon_torsion_vertex/` (7 files + phase1_results) |
| **Publication potential** | LOW (confirms known result; closes salvage path) |
| **Novelty** | N1 — ABJ universality is known |
| **Reusable assets** | VVA triangle computation in ECH context |

### Branch T — Sourced Axion Bridge

| Field | Value |
|-------|-------|
| **ID** | Branch-T |
| **Goal** | Can an external axion kicked by the bounce amplify gauge fields observably? |
| **Status** | CLOSED |
| **One-line significance** | Source strength requires free parameter (axial current); no genuine novelty over generic ALP |
| **Main files** | `research/branch_T_sourced_axion_bridge/` (7 files + phase1_results) |
| **Publication potential** | LOW |
| **Novelty** | N1 |
| **Reusable assets** | Axion-gauge amplification estimate |

### Branch U — Two-Field ALP + DE

| Field | Value |
|-------|-------|
| **ID** | Branch-U |
| **Goal** | Can two-field ALP resolve rolling-vs-freezing tension (birefringence + DE)? |
| **Status** | DEFERRED |
| **One-line significance** | Reintroduces fine-tuning (m_2 ~ H_0); not prioritized unless single-field ALP fails |
| **Main files** | `research/branch_U_twofield_alp_de/` (6 files + phase1_results) |
| **Publication potential** | LOW (speculative) |
| **Novelty** | N1 |
| **Reusable assets** | Two-field background equations |

### Branch V — Bounce Evidence Program (Matter Bounce + ECH)

| Field | Value |
|-------|-------|
| **ID** | Branch-V |
| **Goal** | Identify minimal extensions producing detectable bounce signatures |
| **Status** | ACTIVE (Phase 1 to begin) |
| **One-line significance** | FLAGSHIP: dust contraction + ECH bounce predicts f_NL = 5/12 (SPHEREx testable), low-ell cutoff |
| **Main files** | `research/branch_V_bounce_evidence/` (7 files + dust bounce spectrum + novelty audit + final_verdict) |
| **Publication potential** | FLAGSHIP |
| **Novelty** | N3 — parameter-free prediction from explicit bounce mechanism; connects to Planck anomaly |
| **Reusable assets** | Phase 1 blueprint, observable channel map, upside matrix |

### Branch Vb — ECH Perturbation Gate

| Field | Value |
|-------|-------|
| **ID** | Branch-Vb |
| **Goal** | Assess perturbation propagation through ECH bounce background |
| **Status** | ACTIVE |
| **One-line significance** | Gate for Branch V: can perturbations be computed through the ECH bounce? |
| **Main files** | `research/branch_Vb_ech_perturbation_gate/` |
| **Publication potential** | LOW (infrastructure, not standalone) |
| **Novelty** | N1 |
| **Reusable assets** | Perturbation propagation framework |

### Branch W — ALP Curvaton Tilt

| Field | Value |
|-------|-------|
| **ID** | Branch-W |
| **Goal** | Use birefringence-motivated ALP as curvaton to generate red-tilted spectrum |
| **Status** | CLOSED / SUPERSEDED by Branch V |
| **One-line significance** | Dust contraction gives n_s = 1.000 (8.3-sigma excluded); prompted pivot to Branch V |
| **Main files** | `research/branch_W_alp_curvaton_tilt/` (5 files + phase1_results) |
| **Publication potential** | LOW |
| **Novelty** | N1 |
| **Reusable assets** | n_s = 1 proof for dust contraction |

---

## Special Programs

### Next-Generation Bounce Signal Assessment

| Field | Value |
|-------|-------|
| **ID** | NextGen-Signals |
| **Goal** | Assess which observable bounce signals are viable for next-gen detectors |
| **Status** | CLOSED (frequency gate failed) |
| **One-line significance** | All bounce-scale signals at GHz frequencies; permanently inaccessible to detectors |
| **Main files** | `research/project_nextgen_bounce_signals/` (8 files + final_verdict) |
| **Publication potential** | LOW (negative assessment) |
| **Novelty** | N1 |
| **Reusable assets** | 12-candidate ranking, detector gap analysis |

### Chiral Bounce GW Program

| Field | Value |
|-------|-------|
| **ID** | Chiral-GW |
| **Goal** | Can chiral GW signal from ECH bounce reach detectors? |
| **Status** | CLOSED (Phase 0 frequency gate FAILED) |
| **One-line significance** | f_0 ~ 10^9-10^10 Hz; gap to LIGO: 10^6; gap to LISA: 10^12; Omega_GW proportional to f^8 kills amplitude |
| **Main files** | `research/project_chiral_bounce_GW/` (6 files + phase0_results) |
| **Publication potential** | LOW |
| **Novelty** | N1 |
| **Reusable assets** | Frequency-amplitude scaling relations |

### Paper 2 Research Tracks

| Field | Value |
|-------|-------|
| **ID** | Paper-2 |
| **Goal** | Four parallel extension tracks: WP4 (Delta-N_eff), WP5 (spin amplitude), P6 (CMB EB), P7 (CNN classifier) |
| **Status** | MIXED — P6 (birefringence) is the survivor; others have provenance or coupling-gap issues |
| **One-line significance** | P6 combined birefringence 0.242 +/- 0.061 deg (3.9-sigma); WP5 coupling gap; P7 completed |
| **Main files** | `research/paper2/README.md`, per-track subdirectories |
| **Publication potential** | MODERATE (P6 content folded into Paper 1.2) |
| **Novelty** | N1-N2 |
| **Reusable assets** | P6 literature compilation, P7 CNN model, dataset registries |

### Extensions Program (Tracks A-C)

| Field | Value |
|-------|-------|
| **ID** | Extensions |
| **Goal** | Test SMBH seeds, PBH relics, and CMB parity as extension observables |
| **Status** | CLOSED — only Track C (parity/CMB birefringence) viable |
| **One-line significance** | Track A: 10^{-83} suppression. Track B: no production mechanism. Track C: f_photon = 1.73, approved |
| **Main files** | `research/extensions/final_report.md` |
| **Publication potential** | MODERATE (Track C integrated into Paper 1.2) |
| **Novelty** | N1-N2 |
| **Reusable assets** | Track C equation chain, early-structure survey |

### Program Salvage Audit

| Field | Value |
|-------|-------|
| **ID** | Salvage-Audit |
| **Goal** | Inventory surviving assets after program closure |
| **Status** | COMPLETE |
| **One-line significance** | Identified birefringence as strongest surviving positive result; MCMC infrastructure as key reusable asset |
| **Main files** | `research/program_salvage_audit/01_asset_inventory.md`, `final_verdict.md` |
| **Publication potential** | N/A (internal) |
| **Novelty** | N/A |
| **Reusable assets** | Asset inventory itself |
