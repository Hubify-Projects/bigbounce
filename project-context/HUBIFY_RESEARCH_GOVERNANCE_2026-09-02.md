# Hubify research governance — lessons from BigBounce (2026-09-02)

BigBounce's 2026-03 → 07 derailment is the design case for Hubify's
idea → research → formalization → publication pipeline. The failure mode:
review convergence (a measurable, gameable metric) became the product, while
the lab's own ranked next-science list was ignored and the lineup grew by
splits and rescues. Platform requirements so a lab cannot do this silently:

1. **Vision and next-science ledger are first-class objects**, versioned,
   shown on the lab home, and required inputs to every session/agent run.
2. **Convergence is a gate with a budget.** The platform tracks review
   rounds per manuscript against science decisions; more than N consecutive
   rounds without a recorded science/scope decision raises a visible flag.
3. **Lineup changes are decisions, not edits.** Any split/merge/retire/rescope
   requires a recorded original-claim → new-claim entry (lineage), surfaced
   on the lab's papers page.
4. **Drift audits are scheduled.** The platform diffs the live lineup against
   the vision document on a cadence and posts the result.
5. **Reproducibility manifests gate readiness**, not verdict words.
6. **Motivation is declared, not hidden.** A lab can state its guiding bet;
   the platform shows it beside every claim's evidence grade.
Import path: extend the `HUBIFY_REPRO_IMPORT_SPEC_2026-08-05.md` contract
with `vision`, `next_science_ledger`, and `lineage` objects.
