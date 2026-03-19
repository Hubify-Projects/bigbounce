# Duplication and Supercession Audit

**Created:** 2026-03-19
**Purpose:** For each claim in the gradient-expansion final_verdict.md, determine whether it was already known, still open, or superseded by work elsewhere in the repo.

---

## Claims from gradient_expansion_fnl_derivation/final_verdict.md

| # | Claim | Status | Evidence | Superseding/Supporting File |
|---|-------|--------|----------|----------------------------|
| 1 | "f_NL is negative" | ALREADY KNOWN | fnl_derivation_execution verdict Sec 3: "sign (negative) EXPECTED from T3-T6 dominance (70%)"; fnl_symbolic_cancellation: structural argument for negative from chi-sector | `research/fnl_derivation_execution/final_verdict.md`, `research/fnl_symbolic_cancellation/final_verdict.md` |
| 2 | "f_NL is O(epsilon) = O(1)" | ALREADY KNOWN | fnl_derivation_execution: T1 alone gives +1.56; combined T1-T4 gives 2.19; full expected ~4. All O(1). | `research/fnl_derivation_execution/final_verdict.md`, `research/fnl_symbolic_cancellation/final_verdict.md` |
| 3 | "f_NL has local shape" | ALREADY KNOWN | Squeezed-limit convergence verified numerically in execution phase; template projection computed as cos(theta) ~ 0.95 for SDB. Observational decision framework confirmed cos(theta) = 1.0 for LSS. | `research/fnl_derivation_execution/final_verdict.md`, `research/observational_decision_framework/final_verdict.md` |
| 4 | "f_NL is parameter-free" | ALREADY KNOWN | bispectrum_self_ownership: "f_NL = -35/8 is a property of ANY matter-dominated contraction with standard GR, Bunch-Davies, single canonical scalar." ech_bispectrum_gate: "GENERIC ONLY." | `research/bispectrum_self_ownership_and_ech_test/final_verdict.md`, `research/ech_bispectrum_gate/final_verdict.md` |
| 5 | "Exact coefficient is NOT independently determined" | STILL TRUE | The symbolic cancellation got 35/16 for Terms 1-4 but could not compute Terms 5-6 due to UV divergences. Full 6-term coefficient remains unresolved. | `research/fnl_symbolic_cancellation/final_verdict.md` |
| 6 | "Structural result confirmed from two independent formalisms" | NEW (partially) | The gradient expansion IS a genuinely different formalism. However, the execution phase already had multiple cross-checks (analytical + numerical + SymPy). The GE adds one more independent check. | `research/gradient_expansion_fnl_derivation/final_verdict.md` (this is the GE's main contribution) |
| 7 | "Confidence raised from ~75% to ~80%" | REASONABLE but note: the symbolic cancellation independently computing 35/16 is a STRONGER confidence update than the GE structural confirmation | The 35/16 result from SymPy (matching Li-Brandenberger to 0.07%) is a quantitative verification. The GE confirmation is qualitative. The SymPy result actually CHANGED the balance between -35/8 and -35/16. | `research/fnl_symbolic_cancellation/final_verdict.md` |
| 8 | "MegaMapper SNR 8.75 sigma (at -4.375) or 4.4 sigma (at -2.19)" | ALREADY KNOWN and FURTHER HARDENED | Forecast hardening, Fisher surface, survey realism reconciliation, and last-mile robustness all computed these numbers with much more detail (scenarios, degradation, systematics). | `research/forecast_hardening_program/final_verdict.md`, `research/fisher_robustness_surface/final_verdict.md`, `research/survey_realism_reconciliation/final_verdict.md` |
| 9 | "Science case not dependent on resolving factor-of-2" | ALREADY KNOWN | Explicitly stated in multiple focused-path files: observational_decision_framework, survey_realism_reconciliation, live_forecast_packaging. Both values produce detectable signals. | `research/observational_decision_framework/final_verdict.md` |
| 10 | "Next step Option A: numerical evaluation of in-in time integral" | ALREADY PARTIALLY DONE | fnl_numerical_integral_check computed T1 numerically (+1.5613). fnl_symbolic_cancellation computed T1-T4 via SymPy (2.186). The remaining bottleneck is T5-T6 with UV divergences. | `research/fnl_numerical_integral_check/final_verdict.md`, `research/fnl_symbolic_cancellation/final_verdict.md` |
| 11 | "Next step Option B: PBH + induced GW channel" | IDENTIFIED EARLIER | lqc_specific_openings_audit already identified this as the #2 ranked LQC-specific path. remaining_live_paths_audit ranked it as path #3. | `research/lqc_specific_openings_audit/final_verdict.md`, `research/remaining_live_paths_audit/final_verdict.md` |
| 12 | "Paper readiness ~70%" | OUTDATED | The focused-path terminal has completed the full packaging pass. Paper readiness is closer to 90%. Skeleton, figures (5 generated), claims table, abstract notes, 800k MC samples all complete. | `research/live_forecast_packaging/final_verdict.md` |
| 13 | "Resolve -35/8 vs -35/16 OR acknowledge ambiguity and quote range" | STILL OPEN but BETTER INFORMED | The symbolic cancellation independently favors 35/16. The Cai action audit diagnosed WHY Cai gets a different answer. The honest quote should be f_NL in [-4.4, -2.2] with discussion of which value is more likely. | `research/fnl_symbolic_cancellation/final_verdict.md`, `research/cai_action_audit/final_verdict.md` |
| 14 | "Assess bounce transfer (does f_NL pass through bounce unchanged?)" | STILL OPEN | Neither the GE nor the execution phase addressed this. lqc_specific_openings audit notes it as path #5 (expected trivial but unconfirmed). remaining_live_paths_audit also notes it. | `research/lqc_specific_openings_audit/final_verdict.md` |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| ALREADY KNOWN from execution/focused path | 8 |
| STILL TRUE / STILL OPEN | 4 |
| NEW contribution from gradient expansion | 1 (partial: independent formalism confirmation) |
| OUTDATED by subsequent work | 1 (paper readiness estimate) |

---

## Key Finding

**13 of 14 claims in the gradient expansion verdict are either already known or still open without resolution. Only 1 claim (independent formalism confirmation) represents a genuinely new contribution, and even that is a qualitative cross-check rather than a quantitative advance.**

The gradient expansion terminal was operating without awareness of the extensive focused-path work that had already been completed in 21 other directories. As a result, it re-derived and re-stated results that were already established, sometimes at lower precision.
