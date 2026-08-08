# Referee Handoff — P1A (Einstein–Cartan–Holst No-Go)

`arxiv/paper1a_ech_nogo.tex` · slug `paper-1a` · **current version: v1A.0.112 (2026-07-07)**

## Headline result

A **channel-level** no-go that minimal Einstein–Cartan–Holst (ECH) spin-torsion cannot
be the late-time dark-energy route. Four enumerated minimal-ECH channels are closed
channel-by-channel at M_Pl power-counting. Structure:

- **Tier-I (rigorous):** the perturbation-transparency theorem (torsion vanishes at all
  classical perturbation orders for canonical scalar matter, so the Holst sector
  decouples from scalar/tensor EOM) and the Planck-suppressed NJL four-fermion result (R1).
- **R3 is now DERIVED** from the real Benedetti–Speziale β-function via explicit
  integration (scripts `arxiv/scripts/bs_*.py`): the BS fermion-coupled β-function is
  four-fermion-driven, has its sole fixed point at γ²=1, and its sign depends on |γ|≷1 —
  this grounds R3's |γ|-dependent Immirzi running.
- **ρ_Λ mapping** is presented as a **single-scale NDA no-go** (the +1→+4 mass-dimension
  gap is the mechanism), with the honest single-scale residual kept, not a circular
  assume-ρ_Λ-to-derive-ρ_Λ step.
- **Route-2** is one-loop-grounded (Shapiro–Teixeira) and NDA-bounded.
- Both previously-omitted parity-odd operators are **closed at the operator level**: the
  Jackiw–Pi CS term (constant coupling θ → Pontryagin density is a total derivative in
  4D → zero EOM/ρ_Λ contribution) and the parity-odd V·A four-fermion Holst partner
  (inherits R1's M_Pl⁻² suppression + vanishing coherent mean field).

The operator basis is **complete within minimal ECH**; the single named open item is the
**Fierz-by-Fierz lemma** for the full dim-6 parity-odd basis (a scoped follow-up, disclosed
as such).

**Figure hygiene:** `fig_theory_map.png` previously carried a baked-in f_NL=−35/8 in its
"Observable prediction" box; regenerated to **−35/16** at v1A.0.112 (generator
`arxiv/scripts/fig_theory_map.py`, PNG re-mirrored byte-identical to all served paths).
The body carries 26 −35/16 instances; the sole surviving −35/8 is the cited historical Cai
value being corrected. No scientific number changed.

## Convergence status

P1A has reached the LLM-refereeing floor: **0 genuinely-new real findings** across the
FINAL (2026-07-05) and POSTPOLISH (2026-07-06) truth-audited rounds
(`project-context/peer-reviews/FINAL_SIGNOFF_AUDIT_2026-07-05.md`). On the identical
v1A.0.112-class PDF: **Grok "mature, publication-ready"**; **Gemini MAJOR REVISIONS**
(majors tagged by Gemini itself as "disclosed cross-refs"); **ChatGPT REJECT and openai
gpt-5.5 REJECT** — the maximally-harsh-referee structural floor (directive H). Gemini's
"excessive and repetitive disclaimers" major is literal disclosure-backfire (penalizing the
same honest scoping Grok praises). The one concrete new numeric flag of the POSTPOLISH round
(the Fig-map −35/8) was real and is now **fixed at v1A.0.112**. No re-flag identifies a
surviving correctness defect.

## Recurring objections a human referee should adjudicate

1. **Channel-level vs operator-basis closure.**
   - Concern: the no-go closes the minimal-ECH subset channel-by-channel, not via an
     exhaustive operator-level proof; the dim-6 parity-odd basis Fierz-by-Fierz lemma is
     named open.
   - Disclosed: abstract says "channel-level, not operator-level"; the Jackiw–Pi CS and
     parity-odd 4-fermion partners are explicitly closed at operator level; the Fierz lemma
     is the single scoped open item. Grok confirms "the one scoped item left open."
   - Judgment call: **is channel-level closure + operator-basis completeness within minimal
     ECH + explicit parity-odd operator closures a sufficient PRD "no-go" contribution,
     expecting a real scope exchange on the one open Fierz lemma — or must that lemma be
     closed first?**

2. **Tier of the R2/R3/R4 amplitude bounds.**
   - Concern: whether R2 (one-loop effective action), R3 (Immirzi running), and R4
     (naturalness / explanatory-deficit) meet PRD's rigor bar for a "no-go."
   - Disclosed + strengthened: R3 is now integrated from the real |γ|-dependent
     Benedetti–Speziale β-function (not a schematic ansatz); R2 is one-loop-grounded
     (Shapiro–Teixeira) and NDA-bounded; the ρ_Λ mapping is a single-scale NDA no-go with a
     non-circularity signpost; R4 is correctly closed at the naturalness/explanatory-deficit
     level. Grok reads the identical content as supporting the scoped claim.
   - Judgment call: **do the NDA-bounded amplitude routes + the derived R3 running meet
     PRD's rigor bar for a no-go, or should any route be labeled a consistency check?**

3. **Companion-paper dependency + barrier-catalog framing.**
   - Concern: observational inputs cite coordinated companions; the barrier catalog mixes
     first-principles results with naturalness/heuristic entries.
   - Disclosed: `tab:companion_inputs` isolates every imported number as non-load-bearing
     (`\cite{BigBounceRepro}`, committed artifacts make imports referee-able now);
     `sec:barriers` tiers the catalog (Table III labels only perturbation-transparency
     Tier-I rigorous). Grok: "core claims do not load-bear on companion MCMC numbers."
   - Judgment call: **coordinated-submission companion reliance + honest barrier-tiering —
     acceptable now, or hold until companions post?** (venue/timing)

## What is NOT in question

No genuinely-new correctness defect remains. The perturbation-transparency theorem, the
four-route closure logic, the derived R3 |γ|-running, the single-scale NDA ρ_Λ no-go, and
both operator-level parity-odd closures are all truth-audited sound within their stated
(channel-level, minimal-ECH) scope. The Fig-1/theory-map −35/8 legend was the sole real
POSTPOLISH item and is fixed (−35/16, v1A.0.112). A ChatGPT/openai flag of "Fig 3 H0=69.2
vs 67.68" was verified STALE — the caption discloses 69.2 as a deliberately-high
illustrative benchmark (the 2.7% is the H0 offset, not a torsion signal; closed v1A.0.85).

## Recommended venue / next step

Submit to **PRD** (or JCAP) with the scope — channel-level, operator-basis complete within
minimal ECH, one open Fierz lemma, coordinated-companion dependency — flagged to the editor
up front. Expect a real scope exchange on the "no-go" label and the open Fierz lemma; that
is normal refereeing, not a defect. The full dim-6 operator-basis completion is a distinct
follow-up paper, not a defect fix.
