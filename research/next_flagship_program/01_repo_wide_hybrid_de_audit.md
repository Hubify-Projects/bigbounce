# 01: Repo-Wide Audit of the Hybrid DE Loophole

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Definition of the Loophole

"Hybrid splice-in DE" = adding phenomenological late-time dark energy freedom (dynamical w(z), CPL w0wa, quintessence, etc.) on top of a bounce cosmology framework to improve observational fits, without deriving the DE sector from the bounce mechanism itself.

---

## Exhaustive Repo Search Results

### Hit 1: Program Salvage Audit — Candidate A

**File:** `research/program_salvage_audit/03_positive_program_candidates.md`
**What:** Proposed "Reframe the ECH scaling ansatz as a generic effective model. Update MCMC with DESI DR2, Planck PR4. Fit LCDM + Delta-Neff + possibly w0-wa."
**Stage:** Conceptual only
**Outcome:** REJECTED. Ranked last (5th of 6). Explicitly called out: "This is not a research program; it is routine parameter estimation on a standard extension."
**Would have saved Paper 1?** Probably improved chi-squared, but with zero theory content.

### Hit 2: All MCMC Configs

**Files:** `reproducibility/cosmology/cobaya_full_tension.yaml` (and 3 others)
**What:** Standard LCDM + N_eff. The only extended parameter is nnu. **No w0, wa, w(z), or any DE EOS parameter appears in any MCMC config in the entire repo.**
**Stage:** Actually run (236,622 samples, 64 chains)
**Outcome:** w = -1 fixed throughout
**Key fact:** The loophole was NEVER implemented at computational level.

### Hit 3: Foundation F — Bounce-Prepared Late-Time DE Sector

**Files:** `research/foundation_F_bounce_linked_DE/01_problem_statement.md`, `research/foundation_F_initial_conditions/phase1_results.md`
**What:** Tested whether bounce initial conditions could constrain a late-time DE sector (inverse-power quintessence, pNGB, exponential quintessence, hilltop).
**Stage:** Phase 1 analytic calculations
**Outcome:** CLOSED. "Attractor-Sensitivity Dilemma" — if DE has an attractor, bounce conditions are erased; if it lacks one, initial conditions require 10^-30 precision.
**Would have saved Paper 1?** Never reached fitting stage; theoretical obstacles killed it first.

### Hit 4: Foundation G — Cyclic Vacuum Selection

**Files:** `research/foundation_G_bounce_vacuum_selection/phase2_cyclic_sequestering/phase2_results.md`
**What:** Tested whether cyclic bounce cosmology could select the vacuum energy via finite four-volume constraint (Kaloper-Padilla sequestering).
**Stage:** Phase 2 calculations
**Outcome:** CLOSED. Three obstacles: cyclic incompatible with Lambda_obs, action parameter immune to bounce matching, continuous solution family with no discreteness.
**Final verdict in file:** "The bounce has NO CONNECTION to late-time dark energy."

### Hit 5: Branch I — Bounce-Compatible DE (Horndeski Stability)

**Files:** `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/phase1_results.md`
**What:** Screened 6 Horndeski/scalar-tensor DE model classes for compatibility with the bounce.
**Stage:** Phase 1 analytic
**Outcome:** WEAK. 4/6 trivially compatible. Assessment: "the bounce and dark energy are ships passing in the night, separated by 122 orders of magnitude."
**Implication for loophole:** ANY reasonable DE model is compatible with the bounce, meaning a w0wa extension would work fine but would have zero bounce-specific physics content.

### Hit 6: Branch U — Two-Field ALP + DE

**Files:** `research/branch_U_twofield_alp_de/01_problem_statement.md`
**What:** Two ALP fields: one for birefringence, one for DE. A genuine splice-in attempt.
**Stage:** Problem statement only (opened 2026-03-17)
**Outcome:** OPEN but self-identified 5 failure risks including "No unique ECH derivation" and "Branch I lesson: the bounce cannot communicate with the DE sector."

### Hit 7: Paper 1 (arxiv/main.tex) — Open Question

**File:** `arxiv/main.tex` (line ~1187)
**What:** "if the parity-odd coefficient runs with the Hubble scale... this could produce an effective w(z) != -1 at the few-percent level, potentially connecting to the DESI evidence for dynamical dark energy."
**Stage:** Conceptual only (listed as open question)
**Outcome:** Never computed. Aspirational language only.

### Hit 8: Paper 1.2 — Explicit w = -1 Assumption

**File:** `submission/paper_1_2/main.tex` (lines 146-147, 1667)
**What:** "The equation of state w = -1 is assumed, not derived." Claims table: "w = -1 at late times | Assumed | Observational input | Not derived."
**Stage:** Published statement
**Outcome:** Honest documentation that w = -1 was never derived from the framework.

### Hit 9: Model Comparison Scorecard

**File:** `versions/manifest.json`
**What:** w0waCDM included as EXTERNAL comparison model (bounce vs w0waCDM), not as a parameter extension.
**Stage:** Comparison only
**Outcome:** w0waCDM treated as a competing model, not as an addition to the bounce model.

### Hit 10: Observational Constraints — "Requiring Additional DE"

**File:** `research/observational-constraints.md` (line 25)
**What:** "Matter-bounce scenarios... face tension with the measured H0 = 68.52 +/- 0.62 km/s/Mpc from DESI+CMB combined analysis, requiring additional dark energy components to reconcile expansion rates."
**Stage:** External tool output (astro-atlas-v1)
**Outcome:** UNADDRESSED. The most explicit statement that a bounce model needs additional DE, but no action taken.

### Hit 11: Foundation A — Ultra-light Torsion as DE

**File:** `research/foundation_A_pgt/05_cosmological_relevance.md`
**What:** Explored whether ultra-light PGT torsion mode (m ~ H_0) could act as dynamical DE with w(z).
**Stage:** Conceptual + assessed
**Outcome:** "|t_I| ~ 10^122 is as fine-tuned as the CC itself." Not pursued.

### Hit 12: IR Vacuum Program — Failure Mode

**File:** `research/paper2/ir_vacuum_program/05_honest_failure_modes.md`
**What:** Lists "the framework is a phenomenological parameterization, like wCDM or CPL" as a FAILURE MODE.
**Stage:** Failure-mode identification
**Outcome:** Explicitly treats "reducing to CPL" as a BAD outcome, not a strategy.

### Hit 13: ALP ODE Solver — w_a_0 as Derived Diagnostic

**File:** `research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py`
**What:** Computes w_a_0 = (KE - PE)/(KE + PE) as a derived quantity, not a free MCMC parameter.
**Stage:** Implemented (diagnostic only)
**Outcome:** In spectator regime, Omega_a -> 0. No DE contribution.

### Hit 14: DESI Literature Awareness

**Files:** `research/outputs/lit_desi_dark_energy_2024_2026.json`, `research/outputs/research_report_2026-03-04.md`
**What:** DESI DR2 dynamical DE preference (3.1-4.2 sigma) documented. Called "MODERATELY SUPPORTIVE" and "Consistent with torsion-mediated dynamical vacuum energy."
**Stage:** Literature awareness only
**Outcome:** No action taken. "Consistent with" framing is aspirational, not demonstrated.

### Hit 15: Quintom / w-Crossing References

**File:** `research/observational-constraints.md`
**What:** "The data shows mild preference (2.5 sigma) for evolving dark energy... potentially accommodating quintom bounce models."
**Stage:** External tool output
**Outcome:** UNADDRESSED. No quintom model was ever built.

---

## Summary Verdict

### Was the loophole explored?
**YES — extensively, in at least 7 distinct disguised forms** (Hits 1, 3, 4, 5, 6, 7, 11). The exploration ranged from problem statements through full Phase-2 calculations.

### Was it ever implemented at the computational (MCMC) level?
**NO. Not once.** All 236,622+ chain samples use fixed w = -1. No w0, wa, or w(z) parameter was ever included as a free MCMC parameter.

### Was it explicitly rejected?
**YES — at multiple levels:**
- Program salvage audit: ranked last, called "routine parameter estimation"
- Foundation F: closed on structural grounds (attractor-sensitivity dilemma)
- Foundation G: closed ("bounce has NO CONNECTION to late-time DE")
- Branch I: "ships passing in the night"
- IR vacuum failure modes: "reducing to CPL" listed as failure
- Paper 1.2: honestly documents w = -1 as assumed, not derived

### Would it have saved Paper 1 at fit level?
**Almost certainly yes.** Adding w0-wa to the MCMC would give two more free parameters to absorb late-time expansion history, improving chi-squared against DESI data. The Branch I finding confirms: any reasonable DE is trivially compatible with the bounce. The fit improvement would be real but entirely from the w0-wa freedom, not from the bounce physics.

### How many disguised forms was it explored in?
At least 7: phenomenological ECH DE (Hit 1), bounce-prepared quintessence (Hit 3), cyclic vacuum selection (Hit 4), Horndeski compatibility (Hit 5), two-field ALP+DE (Hit 6), running parity-odd coefficient (Hit 7), ultra-light torsion (Hit 11). Each approached the same fundamental question from a different angle and arrived at the same answer: the bounce cannot generate or constrain late-time DE.
