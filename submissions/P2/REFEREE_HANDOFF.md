# Referee Handoff — P2 (SPHEREx f_NL Sensitivity Recast)

`research/focused_paper_source_integration/02_full_draft.tex` · slug `paper-2`

## Convergence status
P2 has reached the RS11 LLM-refereeing floor: **0 genuinely-new real findings**.
RS11 verdicts — **Grok MAJOR REVISIONS**, **Gemini MAJOR REVISIONS**. Both re-flag the same two
disclosed structural limitations (cubic-transmission conditionality; single-source Heinrich recast);
neither found a correctness defect. Grok's minors (prior-dependent Bayes factors, illustrative MegaMapper,
31pp length) are all already labeled in-text.

## Recurring objections a human referee should adjudicate

1. **Single-source (Heinrich recast) vs independent forecast.**
   - Concern: every SPHEREx significance rescales one external Heinrich+2023 Fisher σ≈0.7 by overlap r=0.84;
     non-local bispectrum tails not propagated; not independent evidence.
   - Disclosed: abstract Scope banner — "sensitivity recast of a single externally published forecast, not an
     independent forecast"; `subsec:Caveats` single-source-limitation sentence names the independent
     bounce-fiducial multi-tracer Fisher re-run as the required follow-up.
   - Judgment call: **is a clearly-labeled single-source sensitivity recast publishable as-is, or does PRD need
     the independent Fisher re-run before the 2.6–5.5σ envelope can appear as a headline?**

2. **Cubic-order bispectrum transmission (the "single weakest link").**
   - Concern: f_NL = −35/8 assumes faithful cubic-order transfer through the bounce, verified only at linear
     order + an order-of-magnitude superhorizon estimate (δf_NL~10⁻³, not a derived bound).
   - Disclosed: abstract carries a load-bearing (★) caveat; Conclusion opening + `sec:assumptions` (d) name it
     the #1 follow-up (full cubic in-in across an explicit bounce).
   - Judgment call: **does a forecast conditioned on an unverified cubic transfer belong in PRD now, framed as
     conditional, or does the cubic in-in computation gate submission?** (scope)

3. **Additive-quadrature systematic budget.**
   - Concern: systematics combined heuristically in quadrature, not via a joint multi-tracer nuisance Fisher.
   - Disclosed: `sec:systematics` up-front heuristic banner; the joint SDB Fisher cross-check shows the
     degeneracy *loosens*, bounding the heuristic's direction.
   - Judgment call: **heuristic budget with a cross-check — acceptable for a recast, or must be replaced by a
     full joint covariance?** (editorial)

## What is NOT in question
No genuinely-new correctness defect remains. Arithmetic (r=0.84 propagation through the BF grid, the 2.6σ floor,
Table IV) has been re-verified across rounds; prior "mismatches" were PDF-font extraction artifacts, not errors.

## Recommended venue / next step
Submit to **PRD** as an explicitly-scoped sensitivity recast, with the single-source and cubic-transmission
caveats flagged to the editor. The genuinely-value-adding (not merely defensive) strengthening would be the
independent bounce-fiducial multi-tracer Fisher re-run — worth doing pre-submission *if* the target editor
treats single-source dependence as disqualifying; otherwise a named follow-up.
