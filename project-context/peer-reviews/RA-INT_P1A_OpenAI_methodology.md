# P1A RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=b5197dc0 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4702 chars)
**Wall time**: 282.4s

---

Referee report for PRD submission “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of this review
- Focus: methodology rigor, statistical-method validity, derivation chains, dimensional analysis, internal arithmetic consistency, and claims traceability.
- I audited all equations, tables, figures, quoted σ/p/ratios/percentages in the abstract, conclusions, and body, and recomputed the ones that are explicitly computable from provided numbers.
- I assessed companion-paper dependencies under a standalone-reader standard.

Overall assessment
The manuscript is a theory/methods paper arguing a channel-level closure for four “minimal ECH” routes to late-time dark energy and presenting a “perturbation transparency” theorem. The analytic parts (Hehl–Datta torsion elimination; Bianchi-identity argument for the Holst dual contraction; dimensional and order-of-magnitude budget closures) are generally sound and carefully caveated as ansätze where appropriate. However:
- The paper repeatedly relies on in-preparation companion works for quantitative context (SPHEREx Fisher significance; ACT/Planck pipeline validation; MCMC posteriors; PTA reanalysis), and incorporates those numbers in tables/figures. Even if declared “not load-bearing,” presenting unverified external results inside the main paper is not acceptable for PRD standards unless they are purely illustrative and clearly segregated.
- Reproducibility is incomplete: the Data/Code section points to a mutable GitHub branch without an archived, versioned DOI or commit hash tied to the submission.
- Several quantitative claims (e.g., “>100 orders” galaxy spin underprediction; Barrier 12 GW ceiling scaling; fine-tuning scoreboard 10^60/10^40) are asserted without a derivation or proper citation traceable within the manuscript.
- Forecast figures (Figs. 4, 7) and Table I mix significance values from different null procedures (you do note non-comparability, which is good) but still present them side-by-side with trend lines labeled as “detection timeline,” which risks overclaim without providing the underlying derivations in this paper.

Below I list all issues found, with severity classification and required fixes.

Findings

ESSENTIAL

P1A-E1 — Abstract (p. 1) and throughout: Use of companion, in-preparation results as quantitative anchors
Problem: The paper repeatedly quotes numerical results from “in preparation” companions and displays them in figures/tables (e.g., SPHEREx 2.6–5σ forecast; MCMC H0, ∆Neff; ACT/Planck EB pipeline validation; PTA γPTA from “real-KDE GPU MCMC”). Even if the text says they are “not load-bearing,” their presence in the main manuscript gives them the appearance of peer-reviewed evidence.
Required fix: Remove all numeric results that depend on in-prep companions from the main text, tables, and figures, or replace them with published/peer-reviewed sources. If retained as “illustrative,” move them to a clearly marked non-load-bearing appendix with an explicit disclaimer (“illustrative only; not used in any proof/result”). Figures whose curves depend on these numbers should be removed or re-rendered using only published inputs. Table II should be deleted or restricted to published inputs only.

P1A-E2 — Data and Code Availability (p. 25): Missing archived, immutable artifact
Problem: Only a GitHub URL is provided; no archived Zenodo DOI, no specific commit hash/tag matching the submission. The text promises a future Zenodo release.
Required fix: At acceptance, PRD requires fully reproducible artifacts. Provide a permanent DOI (e.g., Zenodo) and a specific Git commit hash/tag that reproduces all plots/tables in the submitted version. Update the text accordingly.

P1A-E3 — Barrier 12 (p. 19): Unjustified scaling ΩGW,bounce ≲ (ρcrit/ρPl)^2
Problem: Eq. (20) is presented as an “order-of-magnitude ceiling ansatz” without derivation or citation. Yet it is highlighted as a named “Barrier 12.”
Required fix: Either (a) supply a derivation (even heuristic) or a published reference justifying the quadratic scaling; or (b) demote Barrier 12 to a qualitative remark and remove the equation. Make clear it is not used in any subsequent closure if not derived.

P1A-E4 — Galaxy spin “>100 orders of magnitude” underprediction (p. 10)
Problem: The manuscript asserts that the ECH coupling underpredicts plausible galaxy spin asymmetry by >100 orders of magnitude, but provides no derivation for this numerical claim (no mapping from α/M to dipole amplitude A0).
Required fix: Provide a quantitative back-of-the-envelope linking the α/M scale to an expected dimensionless galaxy spin dipole (with assumptions stated), yielding the stated >100 OOM gap; or remove the numerical claim and retain only the qualitative statement that the predicted effect is negligible relative to current sensitivities.

P1A-E5 — Fine-tuning scoreboard (Fig. 5 bottom, p. 31): Unsupported “10^60” and “10^40” entries
Problem: The chart compares “fine-tuning scores” for ΛCDM (10^122), quintessence (10^60), f(R) gravity (10^40), spin-torsion (10^5), but no derivations/citations are provided for the quintessence and f(R) numbers.
Required fix: Either (a) provide explicit citations to peer-reviewed sources where these orders-of-magnitude are defined and justified, or (b) remove the chart or replace the non-derivable entries with text that avoids numeric claims.

P1A-E6 — Fig. 4 and Fig. 7 (pp. 30, 32): Forecast significance curves without in-paper derivations
Problem: The plots present detection timelines and combined significances (ρ = 0, 0.3, 0.5) without any derivation in this manuscript. You cite a companion forecast (in preparation) as the source.
Required fix: Remove the forecast curves or provide sufficient derivation details in this paper (estimator definition, survey specs, template mismatch factor, GR-projection degradation, photo-z marginalization, Fisher-matrix setup) to allow a referee to reproduce the plotted σ values. At minimum, move these to a non-load-bearing appendix or delete.

P1A-E7 — R3 (Sec. IV C, p. 13): Running of γ — ad hoc β-function
Problem: The paper uses dγ/d ln μ = [(NLF−NRF)/(12π^2)] γ as an “upper-bound EFT ansatz,” but the actual perturbative β-function depends nontrivially on γ (Benedetti & Speziale 2011). The chosen form materially affects the size of ∆γ/γ.
Required fix: Either (a) use the actual computed β-function from Benedetti & Speziale and evaluate ∆γ/γ across a realistic μ-range; or (b) clearly state a rigorous inequality bounding ∆γ/γ from those results. The current O(10^−2) to O(10^−1) estimate should be tied to an explicit calculation or removed.

P1A-E8 — Reproducibility mismatch between text and figures (p. 29, Fig. 3)
Problem: Fig. 3 uses H0 = 69.2 km/s/Mpc for the spin–torsion curve, whereas Table V (p. 26) quotes the adopted H0 = 67.68 ± 1.06 from an internal MCMC. The caption says “illustrative,” but the figure presents a % deviation curve that can be misread as a model prediction.
Required fix: Either (a) align figure inputs with the parameter table used in the text; or (b) move Fig. 3 to a clearly marked illustrative appendix and remove the % deviation panel. If kept, also annotate directly on the plot that the difference is entirely due to the different H0 baselines (as the caption states).

MAJOR

P1A-M1 — Over-reliance on “posted concurrently / in preparation” across the manuscript (many pages)
Problem: Numerous places say “posted concurrently” or “in preparation” and then quote numbers from those works (Table I/II; text in Sec. III, VII; PTA result in Sec. X G; ALP MCMC in Table II).
Required fix: Replace such references with either published sources or remove their numeric outputs. Restrict the paper to results fully established within it. If retained for context, move to a dedicated “Context” appendix and remove numbers from the main narrative.

P1A-M2 — Barrier 1 density estimate uses ISM-like nψ but the claim is “late-time dark energy” (p. 12)
Problem: The suppression estimate ρNJL ~ nψ^2/MPl^2 is shown for nψ ≈ 100 cm^−3 (deliberate upper bound). But the qualitative conclusion is about the cosmological mean at late times, which is ∼2×10^−7 cm^−3, far smaller.
Required fix: Add a line giving the value using the cosmic mean baryon density, to show the bound is even tighter (and thus not dependent on the “high” ISM proxy). This will close a possible interpretive loophole.

P1A-M3 — R2 (Sec. IV B, p. 12): Dimensionless ratio construction needs a clear, single adopted form
Problem: You present a dimensionless ratio ∆θone-loop/∆θobs ~ 10^−60 but also mention “an alternative ordering ∼10^−33” that is not used. This invites confusion.
Required fix: Present a single, unambiguous dimensionless ratio derivation (with units tracked), state that all consistent orderings give suppression ≪ 10^−30, and remove the “alternative ordering” remark. Keep the detailed unit check in a footnote or appendix.

P1A-M4 — Barrier 5 (Scale separation, p. 17) and Appendix B: Ambiguity in off-shell vs on-shell dimensional bookkeeping
Problem: You correctly state Eq. (6) has off-shell mass dimension +1 and treat the mapping to ρΛ as a phenomenological on-shell ansatz. However, the text sometimes seems to traverse between on-shell and off-shell logic in nearby sentences.
Required fix: Consolidate the dimensional discussion: choose one clear path (either the on-shell curvature insertion or a fully local dimension-4 completion with α MPl^3/M), show how it enters the Ntot bookkeeping, and then explicitly wall off the alternative as an aside. This will prevent reader confusion.

P1A-M5 — “>100 OOM” and “structural tension” narrative vs. SPHEREx forecasts (Sec. XIII–XIV)
Problem: The paper states that Ntot ≈ 92 erases the matter-bounce fNL signal at SPHEREx scales, yet elsewhere retains forecast plots claiming 2.6–5σ detectability. The text caveats the incompatibility but the figures still project detections.
Required fix: Make the mutual-exclusion logic explicit at each figure/table where both narratives appear. If Ntot ≈ 92 is adopted anywhere in the main text, then remove or footnote the fNL forecast plots as “incompatible with the Ntot ≈ 92 scenario; shown only as a generic bounce-class example.”

P1A-M6 — Bibliographic assertions in Fig. 5 and Sec. XII B require citations
Problem: Claims like “quintessence 10^60” and “f(R) gravity 10^40” require references. Similarly, statements about “stiff matter” for a dynamical Immirzi field need precise source/citation.
Required fix: Add references to primary literature (or append a brief derivation) for each quantitative or categorical claim in these sections.

MINOR

P1A-m1 — Abstract and Sec. III A: Birefringence σ’s from different null procedures
Problem: You correctly note they are not directly comparable in the abstract and in captions. Ensure this disclaimer appears every time you juxtapose them (it mostly does).
Required fix: Scan once more to ensure each juxtaposition (text, figures, tables) carries the “not directly comparable” note. If any instance lacks it, add.

P1A-m2 — Table II caption and text reference to Table V (pp. 7, 26)
Problem: Table II says “numerical values are reproduced from Table V.” But Table V is a parameter summary; Table II contains companion-imported inputs (some not present in V).
Required fix: Reword Table II caption to remove “reproduced from Table V,” or ensure Table V actually reproduces all Table II numbers. Alternatively, delete Table II per P1A-E1.

P1A-m3 — Notation clarity: M vs MPl vs Marea-gap (pp. 6–8, 14)
Problem: You define M = Marea-gap ~ MPl/√γ, and later use MPl explicitly in dimensionless brackets [(α/M) MPl]. This is fine but easy to misread.
Required fix: Add a one-line reminder at the first use in Sec. IV D that M ≡ Marea-gap = MPl/√γ. Consider using a distinct symbol (e.g., MΔ) consistently to avoid conflation with generic mass scales.

P1A-m4 — R4 basis-conversion footnote (p. 15)
Problem: The footnote successfully clarifies gaγ vs α/M but suggests a 10× gap that “is not an internal inconsistency.” This could confuse readers about the benchmark’s origin.
Required fix: Add a final sentence: “For the purposes of this paper α/M is treated as an effective phenomenological parameter constrained by β; no claim is made that this equals gaγ for any specific UV completion.”

P1A-m5 — Minor arithmetic checks (PASSED but suggest to record)
- Eq. (7): [(α/M)MPl] ≈ 3×10^-3 recomputed from your choices; consistent.
- Eq. (11): Dinf ~ e^-3N × (Treh/MGUT)^(3/2) with N≃92; numbers consistent.
- Sec. IV A: ρNJL ≈ 4×10^-81 eV^4 and ≈ 1.4×10^-70 of ρΛ; consistent.
- Sec. IV B: ∆θ ratio ≈ 10^-60; consistent within units.
- Sec. IV D: ρθ ≈ 1.6×10^-10 eV^4 for β ≃ 0.342°, m ≃ H0, α/M ≃ 10^-21 GeV^-1; consistent.

NITS

P1A-n1 — Typographical consistency (multiple pages)
- “Domaga la”/“Domagała”: keep a consistent transliteration (journal custom).
- Remove stray diacritics artifacts (e.g., “ans¨atze” on p. 1).
- Uniform spacing in “γBI/(γ2BI+1)” (add parentheses consistently).

P1A-n2 — Acknowledgments: AI usage statement (p. 25)
PRD has no explicit policy against this; still, keep neutral tone and remove brand names unless required by policy.

P1A-n3 — Length
At 32 pages, the manuscript is long for its core contribution (a closure argument and a theorem). Consider trimming to ≲20–22 pages by removing the forecast figures (Figs. 4, 7), the illustrative H(z) overlay (Fig. 3), and the fine-tuning bar chart (Fig. 5), or moving them to supplementary.

Methodological highlights that passed checks
- The perturbation-transparency argument (Holst dual contraction vanishes pointwise by the first Bianchi identity for torsionless connections) is correct and crisply stated.
- The R1 amplitude bound is correct and conservative; dimensional counting is sound.
- The R2 one-loop parity-violation amplitude estimate as an upper-bound budget is logically consistent and numerically negligible relative to observed β.
- R4 algebra from the Chern–Simons coupling to β = (α/2M) ∆ϕ is correctly derived in App. C, including the 1/2 factor and WKB regime check.

## Summary recommendation
MAJOR REVISIONS

The core analytic claims (channel-level closure logic and perturbation transparency) are promising and appear technically sound. However, the manuscript currently integrates numerous non-peer-reviewed, companion-dependent numerical results into its tables/figures and makes several quantitative assertions without in-paper derivations or citations (GW ceiling scaling; fine-tuning scoreboard; >100 OOM spin underprediction). Reproducibility artifacts are not yet archived. With the essential fixes above—removing or relocating non-load-bearing forecasts, supplying derivations/citations for quantitative claims, tightening the off-/on-shell dimensional bookkeeping, and providing a proper archived code/data release—the paper could meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

New essential issues

P1A-E9 — Fig. 5 (top): “Renormalization Group Running of α/M” shown without a β-function or calculation
Problem: The plot suggests a specific monotonic running of α/M across ≈20 decades in μ, annotated with a “Primordial α/M ∼ 10^−21 GeV−1” band, but the manuscript never defines a β-function for α/M, specifies thresholds, or gives an integration. Elsewhere α/M is treated as a phenomenological constant. This figure is therefore quantitatively unsupported and risks implying a derived result.
Required fix: Either (a) provide the explicit RG equation(s), thresholds, and integration producing the curve; or (b) remove the panel (or replace by a schematic labeled “cartoon,” with the y-axis de-numericized).

P1A-E10 — Fig. 3 caption: conversion of the vorticity bound to a fraction of ρΛ lacks a derivation and appears dimensionally ad hoc
Problem: The caption maps (ω/H)0^2 < 2.5×10^−21 to “∼1.2×10^−21 of ρΛ by dividing by 3ΩΛ ≈ 2.1.” No equation in the body derives cω ω^2 as an additive energy-density term that scales into a fraction of ρΛ by dividing by 3ΩΛ, and the step as written is dimensionally opaque (curvature vs energy-density normalization). 
Required fix: Provide a clear derivation starting from the background equations (e.g., write 3H^2 = 8πG ρ + … + cω ω^2, show how the ω term maps to an effective ρ component, and justify the 3ΩΛ divisor), or remove the numerical “1.2×10^−21 of ρΛ” statement.

New major issues

P1A-M7 — Foundation A (Eq. 18): undefined units and provenance of t3 in geff ∼ 1/(MPl√|t3|) ∼ H0/MPl
Problem: The parameter t3 is not defined by an explicit PGT Lagrangian, its units are not stated, and the identification √|t3| ∼ mT^−1 is asserted without a reference. As written, the geff ~ H0/MPl scaling is an unsupported dimensional guess.
Required fix: Define the PGT quadratic-torsion action used, state the mass dimensions of t3, derive (or cite) the torsion-mode mass formula and the geff–t3 relation, and then show how mT ∼ H0 leads to geff ∼ H0/MPl.

P1A-M8 — Foundations B and C (pp. 17): barrier statements asserted without derivations/citations
Problem: 
- Barrier 2 (“Topological-Shift Duality”) states “Mass protection ⇔ No geometric fingerprint” without a proof or a literature citation establishing this duality in metric-affine gravity.
- Barrier 3 (“Scalar-Tensor Universality”) claims that torsion-scalar mixing on FRW reduces to the same structure as any scalar and “decouples precisely at the bounce,” but no derivation or reference is provided.
Required fix: Provide proofs/sketches or cite peer-reviewed sources that rigorously establish these claims. Otherwise demote these to qualitative observations, explicitly non-load-bearing.

P1A-M9 — Eqs. (5)–(6): operator definition and normalization are too ambiguous for auditing
Problem: Seff = (α/M) ∫ eI∧eJ∧FIJ[K,R˚] is introduced with F a “functional of K and R˚,” but no explicit component form or normalization is given beyond Eq. (6)’s “leading contribution.” This hampers dimension/normalization checks and later reuse (e.g., in Appendix B’s dimensional discussion).
Required fix: Write the explicit component operator used for all subsequent estimates (with precise index contractions and sign conventions), or move this construction to an appendix with full details so the later budget arguments can be verified against a single concrete operator.

New minor issues

P1A-m6 — Additional σ juxtapositions without an explicit “not directly comparable” reminder
Problem: In Sec. XIII, the sentence pairing “SPHEREx tests at 2.6–5σ” with “LiteBIRD targets ∼9σ” appears without the “different null procedures” disclaimer (present elsewhere). 
Required fix: Add the same “not directly comparable” qualifier here (and in any other remaining instance where different σ’s are shown side-by-side).

P1A-m7 — Broken cross-reference in Appendix C
Problem: The parenthetical “(the convention block of the companion’s §VI8)” is a malformed reference (looks like “Section VI, footnote 8” but is unclear/unresolvable).
Required fix: Correct or remove. If it refers to the present paper, give a valid section/appendix label; if to a companion, per P1A-E1 such references should not be required to follow the calculation.

Explanation
I focused this second pass on items initial reviews often miss: unsupported plotted curves, buried dimensional shortcuts in captions, unproven “barrier” claims presented as results, and ambiguous operator definitions that make later budgets unverifiable. The new issues above are orthogonal to those in my first report and, in my view, must be addressed to meet PRD’s rigor and reproducibility standards.