# EXTDB P1A Gemini — chat: https://gemini.google.com/u/0/app/0120edaacaee4256

Provider: Gemini
Model/Tier: 3.5 Flash (fast)
PDF: /tmp/EXTDB_P1A.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED, R57 PDFs)

---

Referee Report
Journal: High-Tier Physics/Cosmology Journal
Manuscript Title: Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
Author: Houston Golden
Date of Review: June 2026

1. Recommendation
MAJOR REVISIONS

The manuscript presents a rigorous, detailed channel-level assessment of minimal Einstein-Cartan-Holst (ECH) gravity as a driver for late-time dark energy. The analytical proof of "perturbation transparency" for canonical scalar matter—demonstrating that the Holst sector decouples identically at all classical perturbation orders due to the algebraic Bianchi identity—is elegant and robust. However, the paper's quantitative claims and observational validations rely heavily on an extensive network of "in preparation" companion manuscripts. Until these external components are accessible or fully integrated, the empirical conclusions cannot be independently verified by a referee.

2. Blockers
None. There are no fundamental conceptual errors or math failures that would warrant an immediate, un-appealable rejection. The core mathematical foundation (the algebraic vanishing of the Holst term when T=0) is sound.

3. Majors

Major 1 — Heavy Reliance on Unverifiable Companion Papers:
The manuscript frequently anchors its baseline parameters, observational bounds, and pipeline validations on four concurrent papers listed as "in preparation" (Paper I(b) [6], Paper II [2], Paper III [46], and Paper IV [23]). Crucial quantitative results—such as the exact MCMC chains for ΛCDM+ΔNeff, the ViT-Small galaxy chirality classifier data, and the SPHEREx multi-tracer Fisher forecasts—are offloaded to these preprints. For a high-tier journal, a paper must be self-contained enough for the referee to audit its primary empirical inputs. The author needs to either include compressed appendices containing the minimum necessary data from these chains or timeline the publication of this manuscript with the public appearance of the companion pieces.

Major 2 — Dimensional Integrity of the Core Action Ansatz:
As acknowledged in Section II.C and Appendix B, the leading parity-odd operator (Eq. 6) possesses an off-shell mass dimension of +1 instead of the +4 required for a standard local Lagrangian density. The transition to an on-shell dimension of +4 requires explicit scaling assumptions or field insertions based on the Planck-scale bounce geometry. While labeled transparently as an ansatz rather than an EFT derivation, building a definitive "no-go" theorem on an operator framework that is structurally broken off-shell weakens the universality of the conclusion. The author should clarify whether an alternative, fully symmetric, dimension-4 local operator formulation alters the scaling kinetics of the 13 barriers.

4. Minors

Minor 1 — In-Text Discrepancy in Parameter Bookkeeping:
In Section II.C.1, the text notes that matching the observed dark energy density requires Ntot≈92 e-folds, but Appendix B yields ≈94 e-folds, calling it a "~2% reparameterization offset". Table IV lists Ntot≈92 as the reference value but notes underneath that it is erased at SPHEREx scales. This subtle mixing of mathematical scaffolding and physical erasure limits requires cleaner definitions in the table captions.

Minor 2 — Heuristic Nature of Barrier 9:
The presentation of Barrier 9 (Liouville Conservation) admits to being a "heuristic closure under explicit assumptions" (e.g., no particle production, no entropy injection). Given that quantum bounces natively involve particle production and out-of-equilibrium thermodynamics, labeling this a rigid mechanism-class constraint is an overstatement. The text should explicitly downscale the finality of Barrier 9 in the summary sections.

Minor 3 — Reporting of LL / Upper Bounds (Fig. 3):
The rotation contribution is described as "completely invisible on the scale plotted" and bounded by (ω/H)₀ < 5×10⁻¹¹. However, the curve in the lower panel (ΔH/H_ΛCDM) features an arbitrary benchmark setting to match ρΛ. The chart should explicitly state that the curve represents a fine-tuned parameter space designed to illustrate the model's maximum tolerable footprint, rather than a natural prediction.

5. Strengths

S1. Definitive Perturbation-Transparency Resolution — The proof that the Holst dual contraction vanishes identically on the Levi-Civita connection via the first algebraic Bianchi identity is flawlessly executed. Cleanly untangles the Holst term from Pontryagin densities.

S2. Thorough and Transparent Systematic Mapping — The formulation of 14 structural barriers (13 logically independent) provides an exceptional taxonomic map of the minimal-ECH route space. Successfully forces future dark-energy model builders to look outside minimal frameworks.

S3. Clear Falsifiability Timelines — The paper anchors its theoretical exclusions to imminent concrete experimental milestones, mapping specific test windows to SPHEREx (2028) and LiteBIRD (early 2030s). Elevates the paper from abstract field-theory to operationally falsifiable precision cosmology.
