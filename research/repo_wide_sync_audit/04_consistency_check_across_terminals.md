# Consistency Check Across Terminals

**Created:** 2026-03-19
**Purpose:** Identify contradictions between results produced by different terminal sessions.

---

## Comparison 1: Gradient Expansion vs f_NL Execution

### Apparent contradiction: f_NL value

| Source | Value | Sign |
|--------|-------|------|
| GE terminal (`gradient_expansion_fnl_derivation/`) | "f_NL in [-35/8, -35/16]" | Negative |
| Execution: fnl_combined_integrand/ | "+25/16 = +1.5625" | POSITIVE |
| Execution: fnl_symbolic_cancellation/ | "+2.186 = 35/16" (Terms 1-4) | POSITIVE |
| Execution: fnl_discrepancy_resolution/ | "+25/16 (T1 only)" | POSITIVE |

**Is this a real contradiction?** NO. It is a difference in SCOPE, not a disagreement.

- The GE reports the EXPECTED final value (negative, from the full calculation including all terms)
- The execution reports PARTIAL results: Term 1 alone (+1.56), Terms 1-4 combined (+2.19)
- Both terminals agree that the FULL answer including Terms 3-6 is expected to be negative
- The execution terminal's fnl_discrepancy_resolution explicitly states: "The sign flip comes from the chi-sector terms, which likely dominate the physical bispectrum for epsilon = 3/2. This is consistent with Cai and Li-Brandenberger both reporting negative values."

**Resolution:** No contradiction. The positive values are partial results; the full answer is expected negative. CANONICAL WORDING: "The independent partial computation gives f_NL(T1-T4) = +35/16. The full f_NL including all six Maldacena terms is expected to be negative, in the range [-35/8, -35/16], pending resolution of the growing-mode cancellation in Terms 5-6."

### Apparent contradiction: Confidence in -35/8

| Source | Confidence in -35/8 |
|--------|---------------------|
| GE terminal | "Structurally yes" -- implies high confidence |
| fnl_derivation_program | 35% |
| fnl_derivation_execution | 75% (up from 50%) |
| fnl_numerical_integral_check | 65% |
| fnl_symbolic_cancellation | "Magnitude 35/8 is WEAKENED" -- implies <50% |
| cai_action_audit | 75% (up from 40%) |
| gradient_expansion verdict | "~75% to ~80%" |

**Is this a real contradiction?** PARTIALLY. The symbolic cancellation finding (independently getting 35/16) is in tension with the GE's optimistic 80% for -35/8. The SymPy work provides quantitative evidence favoring 35/16 over 35/8.

**Which is more authoritative?** The symbolic cancellation is more authoritative because it provides a NUMERICAL result (2.186 matching 35/16 to 0.07%), whereas the GE provides only a structural argument. The SymPy analysis directly computed Terms 1-4 and found they sum to 35/16, not 35/8.

**Resolution:** CANONICAL WORDING: "Independent computation of the first four Maldacena terms gives f_NL = 35/16, matching Li-Brandenberger (2016). Cai et al.'s -35/8 requires the chi-sector (Terms 5-6 and their interaction with Term 3) to contribute an additional -35/16, which is structurally plausible but not independently verified. Current best estimate: f_NL in [-35/8, -35/16] with 35/16 slightly favored by independent computation."

---

## Comparison 2: f_NL Execution vs Viable Model Work

### Apparent contradiction: f_NL value in Branch V

| Source | f_NL value |
|--------|-----------|
| branch_V_bounce_evidence/ | f_NL = 5/12 |
| branch_V novelty_audit/ | "f_NL = 5/12 is WRONG. The correct value is -35/8." |
| All execution-phase files | f_NL in [-35/8, -35/16] |
| project_master_dossier/05_results_matrix | Row 27: "f_NL = 5/12 (parameter-free)" |

**Is this a real contradiction?** YES. The results matrix still lists f_NL = 5/12 for Branch V, but the novelty audit conclusively identified this as the Maldacena slow-roll value, not the matter bounce value. The correct value for a matter-dominated contraction is -35/8 or -35/16, not 5/12.

**Which is more authoritative?** The novelty audit and ALL subsequent execution-phase work. The 5/12 was traced to a faulty delta-N derivation in Branch V Phase 1a file 06_fNL_estimate.md.

**Resolution:** The results matrix row 27 should be CORRECTED to read f_NL = -35/8 (or the range [-35/8, -35/16]). The CLAUDE.md file also lists "f_NL = 5/12" as a key scientific result and must be corrected.

**CRITICAL: CLAUDE.md currently states "Branch V matter bounce + ECH: f_NL = 5/12 (parameter-free, SPHEREx testable)" -- this is WRONG.** The correct value is f_NL in [-35/8, -35/16] = [-4.375, -2.188].

---

## Comparison 3: Viable Model Pass 2 vs LQC Openings Audit

### Apparent contradiction: LQC specificity

| Source | Claim |
|--------|-------|
| project_viable_bounce_model_pass2/ | "LQC corrections actively shape predictions" (r suppression) |
| post_ech_positive_program/ | "LQC-specific effects confined to k ~ k_bounce (60 OOM from observation)" |

**Is this a real contradiction?** NO, it is a difference in WHICH prediction is discussed.

- r suppression: LQC-specific (dressed-metric corrections matter for tensors at all scales)
- f_NL: generic (set during contraction, not during bounce; LQC corrections negligible)

These are complementary, not contradictory. The r suppression is a BACKGROUND-level correction (modifying the Friedmann equation changes the tensor-to-scalar ratio). The f_NL is a PERTURBATION-level prediction (set by nonlinear dynamics during contraction, transferred unchanged through the bounce).

**Resolution:** CANONICAL WORDING: "LQC plays two distinct roles: (1) suppressing the tensor-to-scalar ratio to r ~ 10^-4 through dressed-metric corrections at the background level, and (2) providing the non-singular bounce mechanism that transfers the contraction-phase bispectrum to the expanding universe. The f_NL prediction is generic to any matter-dominated contraction and does not depend on LQC specifically."

---

## Comparison 4: Bounce Evidence Audit vs Forecast Packaging

### Apparent contradiction: Observational support

| Source | Assessment |
|--------|-----------|
| bounce_evidence_audit/ | "No claim reaches STRONG_EVIDENCE. Bounce does NOT fit better than LCDM + inflation." |
| live_forecast_packaging/ | "THE SCIENCE IS COMPLETE. Draft the paper." |
| bayesian_discrimination_program/ | "Bounce favored 17-24:1 over best competitor for exact detection" |

**Is this a real contradiction?** NO. These are assessing DIFFERENT things:

- bounce_evidence_audit: current observational evidence (no detection yet)
- live_forecast_packaging: theoretical framework for FUTURE test
- bayesian_discrimination: CONDITIONAL result (IF f_NL = -4.375 is detected)

All three are consistent: there is currently no observational evidence favoring bounce over inflation, but IF SPHEREx/MegaMapper detect f_NL ~ -4, the bounce will be strongly favored. The forecast paper documents this conditional argument.

**Resolution:** No correction needed. The framing should always be conditional: "If [measurement], then [conclusion]."

---

## Comparison 5: ECH Closure vs Branch V Activity

### Apparent contradiction: ECH perturbation status

| Source | Claim |
|--------|-------|
| ech_bispectrum_gate/ + ech_tensor_gate/ | "ECH perturbation program COMPREHENSIVELY CLOSED" |
| branch_V_bounce_evidence/ | "ACTIVE -- Flagship research direction" |

**Is this a real contradiction?** PARTIALLY. Branch V was created BEFORE the ECH bispectrum and tensor gates were run. The Branch V verdict discusses "ECH-specific corrections" to the matter bounce, but the gates proved that no such corrections exist (zero torsion -> topological Holst term -> no dynamics).

**Which is more authoritative?** The ECH gates (bispectrum + tensor) are more authoritative. They provide a mathematical proof that ECH contributes no perturbation-level corrections. Branch V's assumption that "ECH corrections" could differ from LQC corrections is contradicted by this proof.

**Resolution:** Branch V should be relabeled from "ECH-specific matter bounce" to "generic matter bounce (with ECH as the bounce mechanism)." The ECH label is appropriate for the background (the modified Friedmann equation) but not for perturbation predictions (which are generic). The Branch V novelty audit already recognized this: "Branch V as Phase 1a (classical perturbation on modified background) is a reproduction of Wilson-Ewing (2013)."

---

## Summary of Contradictions

| Pair | Type | Severity | Resolution |
|------|------|----------|------------|
| GE vs Execution (sign) | Scope difference | LOW | Partial vs full result; no real disagreement |
| GE vs SymPy (-35/8 confidence) | Genuine tension | MODERATE | SymPy is more authoritative; 35/16 slightly favored |
| Branch V vs Execution (5/12 vs -35/8) | Error in Branch V | HIGH | Branch V 5/12 is WRONG; must be corrected everywhere |
| Viable model vs LQC openings | Scope difference | LOW | Different predictions, not contradictory |
| Evidence audit vs Forecast | Different scopes | LOW | Current vs future; conditional framing resolves |
| ECH gates vs Branch V activity | Supercession | MODERATE | Branch V ECH-specific claims invalidated by gates |

### Critical corrections needed:
1. **CLAUDE.md**: Change "f_NL = 5/12" to "f_NL in [-35/8, -35/16]"
2. **project_master_dossier/05_results_matrix.md Row 27**: Correct f_NL value
3. **Branch V status**: Relabel from ECH-specific to generic matter bounce
