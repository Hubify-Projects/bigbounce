# Open Questions and Next Moves

What is truly open, what is dead, and what is worth doing next.

---

## What Is Truly Still Open

### 1. Branch V: Matter Bounce + ECH Perturbation Calculation

**Question:** Can perturbations be propagated through the ECH bounce, and what spectrum results from dust contraction → ECH bounce → radiation expansion?

**Why it matters:** This is the only remaining path to a genuinely novel, testable prediction (f_NL = -35/8 = -4.375, low-ell cutoff) from an explicit spin-torsion bounce mechanism.

**What must happen:** Branch Vb (perturbation gate) must pass — i.e., the perturbation equations must be well-defined and tractable through the ECH bounce background.

**Risk:** n_s = 1 from pure dust contraction is excluded at 8.3-sigma. Needs curvaton or other tilt mechanism, which reintroduces model-dependence.

**Status:** Phase 1 blueprint exists. Calculation not started.

### 2. Branch R: ALP Birefringence MCMC Phase 2

**Question:** What are the publication-quality posteriors and Bayes factors for the spectator ALP model given current birefringence data?

**Why it matters:** This is the strongest surviving positive result. Phase 2 MCMC needs to produce triangle plots, model comparison statistics, and LiteBIRD forecasts.

**What must happen:** Complete 25+ MCMC runs in `research/branch_R_alp_birefringence/phase2_mcmc/`, generate publication figures, compute Bayes factors.

**Risk:** ALP birefringence is not unique to ECH; result may be incremental compared to Fujita et al. (2021), Obata (2022).

**Status:** Phase 2 infrastructure set up. Runs initiated.

### 3. Branch P: Torsion Energy Fraction at PGT Bounce

**Question:** Does propagating torsion carry O(1) or (m_T/M_Pl)^2 of the bounce energy?

**Why it matters:** Determines whether BBN provides a meaningful constraint on PGT torsion mass (m_T > 10^9 GeV if O(1), no constraint if suppressed).

**What must happen:** Compute torsion energy density in PGT bounce background.

**Risk:** If suppressed, this is the last bounce-specific observable channel closing.

**Status:** Not started.

### 4. Planck-Only and Planck+BAO MCMC Chains

**Question:** What are Delta-N_eff posteriors from planck_only and planck_bao datasets?

**Why it matters:** Completes the 4-column cross-dataset table in the manuscript.

**What must happen:** planck_only chains converge (~20-30h remaining as of 2026-03-17). planck_bao chains resume after.

**Risk:** Low risk — expected to confirm Delta-N_eff ~ 0 consistent with other datasets.

**Status:** planck_only RUNNING; planck_bao PAUSED.

---

## What Is Dead (Do Not Reopen)

### Closed with Structural Barriers

| Route | Barrier | Why Irreversible |
|-------|---------|-----------------|
| Torsion condensate → DE | Wrong sign, too weak | Fundamental sign error; no parameter choice fixes it |
| One-loop vacuum energy from fermion determinant | Gamma-independent at one-loop | Mathematical result; higher loops are suppressed by M_Pl |
| Scalar reduction to ALP → DE | Generic ALP after torsion integration | Geometric origin invisible; structurally identical to standard ALP |
| PGT propagating torsion as DE | Mass-coupling lock | Fine-tuning transferred, not eliminated |
| Geometric ALP via Nieh-Yan | Topological-Shift Duality | dN_4 = 0 identically in MAG; mathematical result |
| Environmental mass → distinctive DE | FRW wash-out (T_0 = Q_0 = 0) | Geometric structure invisible on FRW; reduces to scalar-tensor |
| Disformal couplings → distinctive signatures | Planck suppression (1 partial-phi per vertex) | Structural property of how connections couple to matter |
| Sequestering with bounce-determined Lambda | Scale separation (10^{-60}) | V_4 ratio is set by expansion history; cannot be modified |
| Initial conditions from bounce → DE | Attractor-sensitivity dilemma | Structural impossibility; no parameter space to explore |
| Cyclic matching → Lambda | Parameter immunity | mu^4 free; mathematical result |
| Minimal bounce tensor spectrum | P_T ~ 10^{-64} | Set by energy density ratio (rho_bounce/M_Pl^4)^2 |
| Bounce-triggered state selection | Liouville (reversible) + decoupling (irreversible) | Exhausts both mechanism classes |
| Baryogenesis from bounce | Gravitational democracy | Torsion is ~1% of Planck-scale channels |
| Chiral GW from bounce | Frequency at 10^9-10^10 Hz | Omega_GW proportional to f^8; bringing to mHz kills amplitude by 10^{-104} |

### Closed Without Structural Barriers (Just Not Worth Pursuing)

| Route | Why Dead |
|-------|---------|
| Galaxy spin dipole from ECH | 9-12 OOM coupling gap; data provenance issues |
| H_0 tension reduction | Disproved by own MCMC (H_0 = 67.68, standard LCDM) |
| sigma_8 tension reduction | Disproved by own MCMC |
| ALP = dark energy | Rolling-vs-freezing tension; single field cannot do both |
| Sourced axion bridge | Requires free parameter (n_5); no novelty |
| Two-field ALP (Branch U) | Speculative; reintroduces fine-tuning; no calculation done |
| ALP curvaton (Branch W) | Superseded by Branch V |

---

## What Next Calculations Are Actually Worth Doing

### Immediate Priority (This Week)

1. **Write Paper 3A (framework paper).** Claims are locked. Figure plan exists. This is pure writing work — no new calculations needed except generating 5 figures from existing data.

2. **Generate 5 remaining figures.** Using `research/final_paper_prep/generate_publication_figures.py` as template:
   - Barrier map flowchart (NEW)
   - Rolling efficiency eta(m/H_0) (NEW)
   - beta vs theta_i prediction (NEW)
   - ALP constraint landscape (NEW)
   - LiteBIRD forecast (NEW)

3. **Wait for planck_only chains to converge.** No action needed; just monitoring.

### Medium-Term Priority (Next 2-4 Weeks)

4. **Complete Branch R Phase 2 MCMC.** Generate publication-quality posteriors and Bayes factors. Decide whether to fold into Paper 3A or publish separately.

5. **Begin Branch V Phase 1.** Set up dust contraction background equations. Test whether perturbation equations are tractable through ECH bounce. This is the gate for the highest-value paper in the program.

6. **Compile technical companion note.** Unify barrier derivations from Foundations A-G and Branches H-O into a single supplement. Low effort since source material exists.

### Only Worth Pursuing If Novelty Established First

7. **Branch P torsion energy fraction.** Only worth computing if a collaborator or referee specifically asks. The result is either "BBN constraint exists" (publishable as brief report) or "no constraint" (not publishable).

8. **Branch V curvaton/tilt mechanism.** Only after Phase 1 demonstrates that perturbations propagate correctly through the ECH bounce. n_s = 1 is fatal unless a tilt mechanism is identified.

---

## Preconditions Before More Theory Work

Before investing in ANY new theoretical calculation:

1. **Apply the 4-question test** (from `feedback_branch_opening_criteria.md`):
   - Is this genuinely new physics (not a reshuffle of existing parameters)?
   - Is the tiny scale technically natural (not just transferred fine-tuning)?
   - Does it produce a distinctive, testable prediction?
   - Is the failure mode publishable?

2. **Check against the 13 barriers.** Any new mechanism must explain how it evades ALL applicable barriers, not just one.

3. **Estimate order-of-magnitude first.** Do not invest days in detailed calculations that can be killed by a 5-minute OOM estimate.

---

## Preconditions Before More MCMC Work

Before running ANY new MCMC chains:

1. **Complete the current 4-dataset table.** Do not add new datasets or parameters until planck_only and planck_bao chains converge and results are integrated.

2. **Verify the theory hook.** Currently using stock CAMB with nnu variation. Any new model (ALP, Branch V) needs a verified custom theory implementation before running chains.

3. **Define convergence criteria upfront.** R-hat - 1 target, minimum ESS, number of independent chains — all specified before first chain starts.

---

## Dead Ends to Avoid

### Do Not Investigate Further

| Topic | Reason |
|-------|--------|
| Any variant of "torsion generates Lambda" | 13 barriers close all standard mechanism classes |
| Galaxy spin predictions | 9-12 OOM coupling gap is structural |
| Custom CAMB modifications for ECH | No ECH-specific CAMB modification is justified; Delta-N_eff is the right parametrization |
| Bounce-scale observables (GW, relics, baryogenesis) | Frequency gate + gravitational democracy + vacuum amplification ceiling |
| More Horndeski compatibility tests | Scale separation makes all results trivial |
| Further one-loop calculations in ECH | ABJ anomaly is universal; higher loops are Planck-suppressed |
| Inflation-from-bounce scenarios | Bounce and inflation serve different functions; combining them is not an ECH prediction |

### Do Not Reopen Unless External Data Changes

| Topic | What Would Change Things |
|-------|-------------------------|
| Branch U (two-field ALP) | Only if LiteBIRD rules out single-field ALP AND finds non-zero birefringence |
| Branch P (PGT torsion relics) | Only if a gravitational wave detector sensitive to 10^4+ Hz is proposed |
| Sequestering mechanisms | Only if a non-global sequestering variant is proposed that avoids scale separation |
