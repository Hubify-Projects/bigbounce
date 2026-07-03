# Referee Handoff — P1A (Einstein–Cartan–Holst No-Go)

`arxiv/paper1a_ech_nogo.tex` · slug `paper-1a` · **current version: v1A.0.99 (2026-07-03)**

## 2026-07-03 closure (genuinely-new finding, from an authorized derivation attempt)

3. **R3 Immirzi-running arithmetic self-inconsistency — CLOSED** (commit `096993f9`, v1A.0.99)
   - An authorized attempt to *derive* R2/R3 from first principles did **not** produce a
     derivation (they remain honestly ansatz-level), but it **found a real internal
     inconsistency**: the R3 text stated Δγ/γ ~ 10⁻², while its own displayed formula
     `(N_L−N_R)·ln(μ_GUT/μ_IR)/(12π²)` with O(1) chiral count + lever arm ~30–35 gives
     **≈0.27** (verified: 32/118.4 = 0.27) — a 1–2 order self-contradiction.
   - **Fixed honestly:** corrected to Δγ/γ ≈ 0.25–0.30, adopting ~0.3 as the *conservative*
     (least-suppressed) value, fixed the backwards "conservative" framing, reconciled all
     downstream numbers (10⁻⁶³ → 3×10⁻⁶²). **R3 closure is unaffected** — even at 0.3, γ
     retains its order of magnitude and the route keeps ≳60 orders of suppression margin
     (the margin absorbs the correction). **R2 arithmetic separately verified (~10⁻⁶⁰).**
   - **For the referee:** R2/R3 are now internally consistent, but remain *chiral-count EFT
     scaling ansätze*, NOT first-principles derivations — the honest limit. The LLM-referee
     rigor objection (Grok/Gemini RS20: "arbitrary upper-bound ansätze, not derivations")
     is the standing open item a human referee should weigh: is a tiered four-route argument
     (rigorous Tier-I transparency + ansatz Tier-II/III amplitude bounds + Tier-II R4
     naturalness) PRD-appropriate, or must the ansatz tiers be upgraded to full derivations
     (a substantial open theory calculation — the true Immirzi β-function is the
     |γ|-dependent Benedetti–Speziale result, not the schematic one-loop ansatz used for
     the amplitude budget)?

## 2026-07-02 closures (new since 2026-07-01 handoff)

1. **Operator-basis MAJOR — CLOSED** (commits `3c2043c7`, `e295c107`, v1A.0.96)
   - Added explicit closure subsections for BOTH previously-omitted parity-odd operators:
     - **Jackiw–Pi CS term** (`sec:jackiwpi_cs`): constant-coupling θ → Pontryagin density
       is a total derivative in 4D → zero EOM / ρ_Λ contribution (Tier-I, operator level;
       reuses the paper's total-derivative identity). Dynamical θ is not in minimal-ECH
       field content (γ fixed by LQG area spectrum, Barrier 7); if adjoined it is R4-class
       naturalness (Tier-II).
     - **Parity-odd 4-fermion Holst partner** (`sec:r1_parityodd_partner`): the V·A
       four-fermion operator is the third torsion-elimination projection of the same
       operator behind R1 (eq:4fermi); it inherits R1's M_Pl⁻² Planck suppression (~70
       orders below ρ_Λ) and a vanishing coherent mean field (⟨J⁵⟩≈0, ⟨J⟩∝a⁻³ in w=0),
       so it carries no w=−1 structure (Tier-III).
   - Full dim-6 operator basis explicitly scoped as follow-up; abstract and intro updated to
     acknowledge the now-closed CS + parity-odd partners by name.

2. **ρ_Λ-mapping "circularity" re-flag — CLOSED** (commit `e5bbb92b`, v1A.0.97)
   - Grok RS8 re-flagged the on-shell dark-energy mapping (ρ_Λ ~ Ξ M_Pl⁴) as circular
     (assuming ρ_Λ to derive ρ_Λ). Non-circularity signpost added: the on-shell ansatz
     is a conservative UPPER bound (it makes the hierarchy hardest to bridge, not easiest);
     the paper claims no derived amplitude — only that R4 naturalness closure stands even
     under this mapping. Not circular.

## Convergence status (as of RS11 / 2026-07-02 floor)

P1A has reached the LLM-refereeing floor: **0 genuinely-new real findings** across RS11.
RS11 verdicts — **Grok MAJOR REVISIONS, Gemini MAJOR REVISIONS**. Every RS11 major re-flags
content the paper already discloses: scope-vs-claim, ansatz-based route closures, on-shell DE
mapping, transparency-theorem scope, barrier-catalog heterogeneity — all with in-text
disclosures; Gemini explicitly tagged its RS11 majors as "disclosed cross-refs" /
"disclosed." No re-flag identifies a correctness defect.

## Recurring objections a human referee should adjudicate

1. **Channel-level vs operator-basis closure.**
   - Concern: the no-go closes the minimal-ECH subset via one-loop channels, not an exhaustive
     operator basis. The Jackiw–Pi CS and parity-odd 4-fermion partners are now explicitly
     closed (see above); the full dim-6 basis is scoped as follow-up.
   - Disclosed: Intro Scope paragraph + four-route "illustrative, non-exhaustive" note;
     abstract says "channel-level, not operator-level."
   - Judgment call: **is channel-level closure + an ansatz-bounded route survey + explicit
     parity-odd operator closures a sufficient PRD contribution, or does it need the full
     dim-6 basis follow-up first?**

2. **Ansatz-dependence of R2/R3/R4 amplitude bounds.**
   - Concern: Routes R2/R3 and the dark-energy mapping rest on a phenomenological on-shell
     scaling ansatz "motivated by not derived from" Mercuri/Shapiro/Date, not a controlled EFT.
   - Disclosed: §II.C / App B state the mapping is not a controlled EFT derivation; the 2026-07-02
     note clarifies the ansatz is a conservative (worst-case) upper bound.
   - Judgment call: **do Tier-III ansatz-level dimensional bounds + the explicit non-circularity
     signpost meet PRD's rigor bar, or must they be labeled consistency checks rather than no-gos?**

3. **Companion-paper dependency + barrier-catalog framing.**
   - Concern: observational inputs cite 4 unposted companions; the "13 mechanism-class" catalog
     mixes first-principles results with naturalness/heuristic entries.
   - Disclosed: `tab:companion_inputs` isolates every imported number as non-load-bearing;
     `sec:barriers` defines "distinct mechanism-class" and flags B5/6/7/10/13 general, B9 heuristic.
   - Judgment call: **coordinated-submission companion reliance + honest barrier-tiering — acceptable
     now, or hold until companions post?** (venue/timing)

## What is NOT in question

No genuinely-new correctness defect remains. The perturbation-transparency theorem, the four-route
closure logic, the Jackiw–Pi CS closure, and the parity-odd 4-fermion closure are all truth-audited
sound within their stated (channel-level, ansatz-bounded) scope. The 2026-07-02 operator-basis
additions strengthen the operator coverage meaningfully without overclaiming.

## Recommended venue / next step

Submit to **PRD** with the scope (channel-level, two parity-odd operators now explicitly closed,
ansatz-dependent Tier-III bounds, companion-dependency) flagged to the editor up front. Optional
pre-submission strengthening: the full dim-6 operator-basis completion — but that is a distinct
follow-up paper, not a defect fix.
