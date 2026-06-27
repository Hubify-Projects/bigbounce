# EXTDB P5 ChatGPT — chat: https://chatgpt.com/c/6a3f8a02-a154-83e8-b18c-399269902b30

Provider: ChatGPT
Model/Tier: Instant (fast, gpt-4o)
PDF: /tmp/EXTDB_P5.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MINOR REVISIONS

No blockers. The paper is unusually transparent about its post-hoc primary/secondary split, T-Web limitations, DESIVAST anchoring, RSD caveats, duplicate rows, and selection-function issues. The main null result is well supported. I would not require major re-analysis before publication, but several claims should be tightened before acceptance.

2. BLOCKERS
None.

3. MAJORS

M1 — The "largest / to date" framing should be softened or precisely scoped.
The manuscript claims the DESIVAST-anchored re-analysis is "to our knowledge, the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date." This may be true within the paper's custom chirality catalog and DESIVAST-matched subset, but it is not independently established. Rephrase as "largest within this catalog and DESI DR1/DESIVAST construction" unless a literature audit is provided.

M2 — The DESIVAST primary path is declared post hoc.
The paper handles this honestly, but because the primary statistic was chosen after exploring multiple classifiers, the abstract/headline should explicitly say "post-hoc declared primary path." This does not invalidate the null, but it affects the evidentiary weight.

M3 — T-Web environment labels are heavily compromised by selection/radial-shell effects.
The corrected rebuild dramatically changes class populations and only 26.6% of matched spirals retain class labels in the randoms-weighted test. The paper appropriately demotes T-Web to secondary, but some abstract/title wording still gives T-Web near-equal billing. The title and abstract should make DESIVAST the clear primary result and T-Web explicitly secondary.

M4 — The RSD language remains slightly overconfident.
The manuscript says DESIVAST is "RSD-bounded" but it does not reconstruct the void catalog under RSD. This is acceptable if framed as a membership-sensitivity test, not a full RSD robustness proof. Tighten all "RSD-bounded" phrasing accordingly.

4. MINORS

m1 — The abstract is too dense and overburdened with diagnostics. It reads like a response memo rather than a paper abstract. Move many robustness numbers to a "robustness summary" paragraph in the main text.
m2 — Clarify row-level vs unique-galaxy inference earlier. The duplicate-row issue is handled well later, but the abstract introduces 812,793 rows and 783,820 unique spirals in a way that may confuse readers.
m3 — The toy EFT appendix should be clearly labeled non-inferential. It is already caveated, but avoid giving the impression that a physical coupling constraint has been derived.
m4 — The "no room for Shamir amplitude" statement should be scoped. The paper constrains environment-conditioned asymmetry, not the global Shamir-style dipole claim. Make the scope explicit wherever it appears.
m5 — Figures 6/8 captions and visuals are somewhat hard to parse. Improve figure spacing and avoid overlapping labels.

5. Strengths

1. Strong primary null: DESIVAST VoidFinder gives ΔfCW = +0.0007 with z = +0.31, p = 0.76, and the three DESIVAST algorithms all remain null.
2. Excellent transparency about analysis multiplicity, post-hoc primary selection, duplicate rows, and classifier-monopole subtraction.
3. The paper separates raw σ-from-half from monopole-referenced residuals, preventing a common large-N misinterpretation.
4. Robustness suite is unusually broad: DESIVAST variants, GALZONE native membership, T-Web sweeps, grid checks, redshift/density/sky tests, Tempel, ASTRA, and program splits.
5. The limitations section is candid and scientifically useful, especially on redshift-space classification and T-Web selection-function contamination.
