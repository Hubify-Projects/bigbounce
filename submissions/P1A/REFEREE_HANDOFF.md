# Referee Handoff — P1A (Einstein–Cartan–Holst No-Go)

`arxiv/paper1a_ech_nogo.tex` · slug `paper-1a`

## Convergence status
P1A has reached the RS11 LLM-refereeing floor: **0 genuinely-new real findings**.
RS11 verdicts — **Grok MAJOR REVISIONS**, **Gemini MAJOR REVISIONS**. Every RS11
major re-flags content the paper already discloses (Grok's own list is scope-vs-claim,
ansatz-based route closures, on-shell DE mapping, transparency-theorem scope, barrier-catalog
heterogeneity — all with in-text disclosures; Gemini explicitly tags its two majors
"disclosed cross-refs" / "disclosed"). No re-flag identifies a correctness defect; they are
editorial/scope judgment calls.

## Recurring objections a human referee should adjudicate

1. **Channel-level vs operator-basis closure.**
   - Concern: the no-go closes the *chosen* minimal-ECH subset via one-loop channels, not an
     exhaustive operator basis (Jackiw–Pi, parity-odd 4-fermion omitted).
   - Disclosed: Intro Scope paragraph + four-route "illustrative, non-exhaustive" note; abstract
     says "channel-level, not operator-level."
   - Judgment call: **is channel-level closure + an ansatz-bounded route survey a sufficient
     PRD contribution, or does it need the operator-basis follow-up first?**

2. **Ansatz-dependence of R2/R3/R4 amplitude bounds.**
   - Concern: Routes R2/R3 and the dark-energy mapping (ρ_Λ ~ Ξ M_Pl⁴) rest on a phenomenological
     on-shell scaling ansatz "motivated by not derived from" Mercuri/Shapiro/Date, not a controlled EFT.
   - Disclosed: §II.C / App B state the mapping is not a controlled EFT derivation; note added that
     any dim-4 completion reproduces the same on-shell budget.
   - Judgment call: **do Tier-III ansatz-level dimensional bounds meet PRD's rigor bar, or must they
     be labeled consistency checks rather than no-gos?** (framing/editorial)

3. **Companion-paper dependency + barrier-catalog framing.**
   - Concern: observational inputs cite 4 unposted companions; the "13 mechanism-class" catalog mixes
     first-principles results with naturalness/heuristic entries.
   - Disclosed: `tab:companion_inputs` isolates every imported number as non-load-bearing; `sec:barriers`
     status paragraph defines "distinct mechanism-class" and flags B5/6/7/10/13 general, B9 heuristic.
   - Judgment call: **coordinated-submission companion reliance + honest barrier-tiering — acceptable, or
     hold until companions post?** (venue/timing)

## What is NOT in question
No genuinely-new correctness defect remains. The perturbation-transparency theorem and the
four-route closure logic are truth-audited sound within their stated (channel-level, ansatz-bounded) scope.

## Recommended venue / next step
Submit to **PRD** with the scope (channel-level, ansatz-dependent Tier-III bounds) and companion-dependency
caveats flagged to the editor up front. Optional pre-submission strengthening: the operator-basis
completion, if a reviewer treats exhaustiveness as a hard bar — but that is a distinct follow-up paper, not
a defect fix.
