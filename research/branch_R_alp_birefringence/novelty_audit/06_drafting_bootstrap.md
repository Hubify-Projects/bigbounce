# Drafting Bootstrap

**Date:** 2026-03-17
**Premise:** Branch R is CAN_BE_INCLUDED_BUT_NOT_MAIN_ANCHOR. Paper reanchored on closure assessment.

---

## Revised Title

**"Comprehensive Assessment of Einstein-Cartan-Holst Cosmology: Structural Barriers, Spectator ALP Birefringence, and a Falsifiable Prediction"**

Alternative (shorter):
**"Spin-Torsion Bounce Cosmology: Thirteen Structural Barriers and One Surviving Prediction"**

---

## First 2 Sections to Draft Now

### Section to draft FIRST: Section 3 — Structural Closure Assessment

**Why first:**
- This is the paper's PRIMARY NOVELTY
- The content is fully documented (branches A–O, 13 barriers)
- No additional computation needed
- Sets the stage for the ALP payoff

**Structure:**
- 3.1: Methodology (how branches were identified and tested)
- 3.2: The 13 barriers in compact catalog form (Table)
  - Each barrier: name, mechanism, which branch, one-line proof sketch
- 3.3: Five failure modes (taxonomy)
  - Too high-energy for late-time observables
  - Too generic at its own scale
  - Too decoupled from late-time vacuum
  - Too universal (indistinguishable from other bounces)
  - Hamiltonian phase-space conservation
- 3.4: Implications — "The bounce is viable but observationally inert in the direct sector"

**Source material:**
- `research/post_AG_pivot/` — closure memos
- `research/branch_H_bounce_only/` through `research/branch_O_hidden_sector_vacuum/`
- Memory file: `project_post_AG_pivot.md`

**Target length:** 3 pages (dense, table-heavy)

---

### Section to draft SECOND: Section 5 — ALP Birefringence: The Surviving Prediction

**Why second:**
- Builds directly on closure assessment ("after eliminating everything else, this remains")
- MCMC results are complete and documented
- The honest framing requires the closure context to land properly

**Structure:**
- 5.1: The effective spectator ALP (Lagrangian, parameters, f_a cancellation)
- 5.2: Prediction — β = Cα θ_i η / (4π) ~ 0.27° for θ_i = 1
- 5.3: MCMC constraints (Run 1 results: θ_i = 1.36 ± 0.44, β = 0.336 ± 0.107°)
- 5.4: Model comparison
  - ALP (C=8) vs ALP (C free) vs free β
  - All produce identical β posteriors
  - ALP is statistically equivalent to free β (ΔAIC = +2)
  - "Physical interpretation, not statistical improvement"
- 5.5: Relationship to prior work
  - Cite Fujita+ 2021, Nakagawa+ 2025, Namikawa+ 2025 explicitly
  - State what we add: specific 2-parameter model, free-β comparison, ECH context
  - State what we DON'T add: no new data analysis, no EB spectrum shape

**Source material:**
- `phase2_mcmc/run1_results.md`, `run2_results.md`, `run3_comparison.md`, `phase2_results.md`
- `paper1_salvage_alp/04_effective_sector_spec.md`
- Chain plots from `chains/run1_full/`, `chains/run2_extended/`

**Target length:** 3.5 pages

---

## Figures to Create FIRST

### Priority 1: Barrier Summary Table/Figure (for Section 3)
- The 13 barriers in a single, visually clear table
- Columns: #, Name, Branch, Mechanism, Failure Mode
- This is the paper's signature visual contribution
- Simple LaTeX table; no matplotlib needed

### Priority 2: β vs θ_i Prediction Plot (for Section 5)
- x-axis: θ_i [0, π]
- y-axis: β [deg]
- Blue line: β = 0.27° × θ_i (C=8, η=1)
- Orange horizontal band: β_obs = 0.342 ± 0.094°
- Green vertical band: θ_i = 1.36 ± 0.44 (from posterior)
- Gray shaded: "natural" region θ_i ∈ [0.3, π]
- Simple matplotlib, high impact

### Priority 3: MCMC Triangle Plot (for Section 5)
- Already exists: `chains/run1_full/triangle_plot.png`
- May need cosmetic cleanup for publication quality

---

## How to State the ALP Result Without Overclaiming

### The Template Paragraph (for abstract/intro):

> "The framework's Planck-scale parity-odd sector motivates an effective spectator axion-like particle with f_a ~ M_Pl and Standard Model anomaly coupling C = 8. This ALP predicts cosmic birefringence β = Cα θ_i / (4π) ≈ 0.27° for O(1) initial misalignment, consistent with the observed 0.342 ± 0.094° [Eskilt+ 2022, Diego-Palazuelos+ 2022]. MCMC analysis yields θ_i = 1.36 ± 0.44 (Gelman-Rubin R̂ - 1 = 0.008). The ALP model is statistically equivalent to a free birefringence parameter on current data (ΔAIC = +2) but provides physical interpretation: natural O(1) parameters, f_a-independent prediction, and falsifiable structure testable by LiteBIRD. We note that spectator ALP models with similar conclusions have been studied previously [Fujita+ 2021]; our contribution is the specific ECH-motivated parametrization and the demonstration that this is the sole surviving testable prediction of the minimal framework."

### Key Phrases to USE:
- "motivates" (not "derives" or "predicts")
- "consistent with" (not "explains" or "confirms")
- "statistically equivalent to free β" (honest)
- "physical interpretation, not statistical improvement" (honest)
- "studied previously [Fujita+ 2021]" (citing prior work explicitly)
- "our contribution is..." (stating the delta clearly)

### Key Phrases to AVOID:
- "We predict..." (Fujita+ 2021 already predicted this)
- "Novel constraint..." (our constraints are weaker than Namikawa+ 2025)
- "First demonstration..." (Fujita+ 2021 was first)
- "Uniquely derived from ECH..." (not unique)

---

## If This Bootstrap Feels Deflationary...

It should. The ALP birefringence result is genuine but incremental. The paper's real value is the closure assessment — 13 barriers across 15 branches is substantial original theoretical work that no other paper has done. The ALP is the cherry on top, not the cake.

A paper that says "we did the hard theoretical work, found that almost everything is closed, and the one surviving prediction happens to match data" is MORE compelling than "we fit β with an ALP." The first paper is a definitive assessment; the second is entry #15 in a crowded field.
