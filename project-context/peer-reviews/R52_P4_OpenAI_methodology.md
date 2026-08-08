# P4 R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6007 chars)
**Wall time**: 530.8s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Methodology rigor: estimators, nulls, significance conventions, dimensional consistency, internal arithmetic, and reproducibility claims.
- I read the entire PDF (23 pages), audited tables/figures/equations, and recomputed every quoted scalar where possible.

Global assessment
- The analysis is generally careful about significance conventions and nulls, and most key numbers check out arithmetically.
- However, there are several essential issues that must be corrected before the manuscript can meet PRD standards: an internal inconsistency on the hemisphere look-elsewhere result, pervasive inclusion of internal versioning/review-process prose and path-like artifact pointers in the body text, and the absence (at submission time) of a frozen, citable DOI for the released data/code. There is also at least one numerical inconsistency in a load-bearing table that needs correction.

Detailed findings

ESSENTIAL

P4-E1 (Sec. III.B p.4 and Appendix C p.19): Internal inconsistency on hemisphere look-elsewhere result.
- Offending text:
  - p.4, Sec. III.B bullet “Secondary diagnostic estimators (v)”: “hemisphere maximum-asymmetry (3.05σ …, < 1σ after look-elsewhere correction; Appendix C).”
  - Appendix C (p.19): “The direct-MC look-elsewhere test … gives pLEE ≤ 10−4 (rejection of the random-label null) … Bonferroni … <1σ is noted only as a qualitative cross-check.”
- Problem: The body text asserts “< 1σ after look-elsewhere correction” while Appendix C’s principled direct-MC look-elsewhere result is pLEE ≤ 10−4 (≈ 3.7σ, one-sided Gaussian-equivalent). These statements conflict.
- Required fix: Remove the “< 1σ after look-elsewhere correction” claim. Report one consistent, principled look-elsewhere statistic (the direct-MC max-statistic pLEE with its Gaussian-equivalent if desired), and keep the “systematics-attributed” caveat. Ensure Table I row (v) and all mentions of this diagnostic are made consistent with Appendix C.

P4-E2 (Multiple locations: p.4; Appendix D p.20 n.2; p.21–22; passim): Internal version/review-process language in the body text.
- Offending text/examples:
  - p.4: “was declared in early versions of this analysis and predates the provenance audit …”
  - Appendix D p.20 n.2: “computed post-R29 …”
  - p.21 Appendix E: “An earlier version of this paragraph overstated the stability …”
  - p.22 Data Availability: “Repository state for this version: commit 53b41d12 (v1.0.185 lineage, June 2026) …”
  - Numerous in-line “artifact pipelines/p2_chirality/… .json” paths across the paper.
- Problem: PRD requires a clean, archival scientific record. Version-history narration, “earlier version” commentary, and internal review-round tags (e.g., “post-R29”) do not belong in the published article. Long path-like artifact pointers in the main text read as internal book-keeping/logging rather than scientific narrative.
- Required fix: Remove all process/version/round language from the main text. Move specific artifact file-paths and run-IDs to a consolidated “Supplemental Material: Reproducibility Checklist,” or cite a stable DOI (see P4-E3). Keep short, human-readable identifiers in the body only when essential. Replace “was declared in early versions” with a neutral declaration of estimator hierarchy with no process claims.

P4-E3 (Data Availability p.22): No frozen DOI/archival handle at submission; “has not yet been minted.”
- Offending text: “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact.”
- Problem: For PRD, data/code availability must be stable and citable upon acceptance. A moving target (“not yet minted”) is insufficient.
- Required fix: Before acceptance, deposit the exact analysis artifacts (catalog, model checkpoint, code snapshot, configuration files, masks, and the committed “canonical-provenance” arrays used to compute reported numbers) to a long-term archive (Zenodo or similar) and provide permanent DOIs. Reference those DOIs in the manuscript (and Supplemental if you maintain large artifact lists).

MAJOR

P4-M1 (Table II p.5): Numerical inconsistency in “Catalog B (calibrated)” Dev. column.
- Offending entry: “B (calibrated) 0.504 ± 0.0003; Excess +0.4%; Dev. +14.6σ.”
- Problem: With fCW = 0.504 and σ = 0.0003, the deviation (0.004/0.0003) is ≈ 13.3σ, not 14.6σ. If σ is smaller (e.g., 0.000274), Dev. ≈ 14.6σ, but then the quoted ±0.0003 is inconsistent.
- Required fix: Recompute and correct the “Dev. (σ)” using the actually used Nspiral for Catalog B and the unrounded fCW. Report consistent σ and Dev., or supply the precise fCW with trailing digits (as done in other rows) so readers can reproduce the value.

P4-M2 (Sec. II.B p.3): Training-set accounting ambiguous/inconsistent with “80/20 split” and flip augmentation.
- Offending text: “after flip augmentation of the training split the combined pool is 26,616 images (80/20 split: ntrain = 21,293, nval = 5,323); the 826-image difference … arises entirely from horizontal-flip augmentation applied to the training split only …”
- Problem: The counts add (21,293+5,323=26,616), but the “80/20 split” description is confusing because the base training split implied by these numbers is 20,467/5,323 (≈79.3/20.7), not 80/20, and it is unclear why only 826 training images are augmented.
- Required fix: Provide exact pre/post-split counts (before augmentation) and a clear description of the augmentation policy (which subset was augmented and why). If the split deviates from 80/20, state the actual split fraction.

P4-M3 (Terminology, multiple pages): Inconsistent naming for null procedures risks confusion.
- Offending usage: “isotropic-bootstrap null,” “pixel-permutation null,” “per-galaxy label-shuffle null,” “binomial-monopole realizations,” sometimes side-by-side.
- Problem: Although the manuscript often adds caveats, the proliferation of names makes it hard for readers to map results across sections.
- Required fix: Introduce a compact “Null Procedures Glossary” early in Sec. III.A or III.B that precisely defines each null (inputs preserved, what is permuted, what is held fixed), assign unambiguous labels (e.g., N1=per-pixel permutation of Ap; N2=per-galaxy label-shuffle preserving Nspiral(p); N3=monopole-only generative; N4=depth-stratified shuffle), and use those labels consistently in text/figures/tables.

P4-M4 (Sec. IV.C p.9 and Table III p.11): Present one canonical post-MASTER number; move alternates to Appendix with reason for drift.
- Offending text: p.9 gives C1 = 2.348×10−5 with null mean 1.71×10−6 (σ = 2.99×10−6; z = 7.28σ). Table III (10k perms) reports ⟨C1⟩null = 1.93×10−6 and σ = 3.12×10−6 (z = 7.31).
- Problem: Different runs (500 vs 10k permutations, slightly different field conventions) yield slightly different z. This is acceptable but confusing as-is.
- Required fix: Designate a single canonical value in the main text (choose one estimator + null + field convention) and state it once. Relegate alternate runs (with explicit differences in estimator/field/mask/null) to an appendix table that explains the expected drift.

P4-M5 (Multiple places, especially p.4 and across all sections): Excessive in-line artifact file paths impede readability.
- Problem: Long path-like strings (e.g., pipelines/p2_chirality/outputs/…) appear dozens of times in the main text and captions.
- Required fix: Move these to Supplemental Material or to a machine-readable “reproducibility manifest.” In the main text, replace with short labels (e.g., “Artifact A1”) that resolve to a DOI/file in the Supplemental.

P4-M6 (Length, whole paper): The paper reads longer than necessary for the stated methodological result (null real-space dipole + leakage channel characterization).
- Required change: Consider trimming the main text to ~18 pages by moving implementation and multi-variant numerical audits (that are not load-bearing) to Supplemental Material. Keep the estimator definitions, primary results, and one canonical set of diagnostic numbers in the body.

MINOR

P4-N1 (Sec. IV.B p.5–6): Slab-statistics phrasing.
- Offending text: “max |z| = 2.9 vs. the global rate” and “consistent with the coherent low-ℓ systematic structure …”
- Suggestion: Provide the actual maximum deviation values (already partly given) alongside z to keep the effect-size visible. You mostly do this; ensure every z is paired with a magnitude.

P4-N2 (Sec. IV.C p.7): Unit reminders could be tightened.
- Offending text: Several repetitions of “Ap = 2(fCW − 1/2)” appear within a few paragraphs.
- Suggestion: Retain it once near Eq. (3) and refer back to it rather than repeating.

P4-N3 (Appendix A p.16–17): Formatting of “C 2 2◦ apodization.”
- Suggestion: Normalize to “C2 apodization with 2° scale” throughout.

P4-N4 (Sec. V.A p.12): WLS amplitude “0.32% in Ap units.”
- Suggestion: State both Ap and fCW units explicitly to avoid confusion (0.0032 in Ap units = 0.16% in fCW units).

P4-N5 (Data Availability p.22): Small grammatical edits.
- Suggestion: “A future survey detecting a chirality dipole … would be in tension” → keep this in Conclusions, and keep Data Availability strictly informational.

Arithmetic and dimensional checks performed (selected)

- Catalog counts (p.5): NCW=1,592,107; NCCW=1,609,053; NNS=5,273,371; sum = 8,474,531. Nspiral = 3,201,160; correct.
- Fractional uncertainties (Table II): Catalog C σ = sqrt(p(1−p)/N) ≈ 0.0002795; deviation from 0.5 is −0.002647; Dev. ≈ −9.47σ; matches.
- Catalog A σ ≈ 0.000274; Dev. ≈ +28.77σ (table: +28.72; acceptable rounding).
- Real-space dipole (p.7): amplitude 4.4×10−3 = 0.44% (Ap units), z = 0.41 against isotropic pixel-permutation null; consistent with stated quantiles {3.5, 4.4, 6.0, 6.8, 8.4}×10−3.
- MASTER ℓ=1 (p.9): (2.348×10−5 − 1.71×10−6)/2.99×10−6 ≈ 7.28σ; correct.
- Table III (apodized): 24.74−1.93 = 22.81; 22.81/3.12 ≈ 7.31σ; correct.
- Monopole leakage (Table IV): 1.6846/1.6961 ≈ 0.9932; (1.6961−1.6846)/0.0068 ≈ 1.69σ residual; correct.
- Block-bootstrap WLS (Appendix D Table X): Abest = 4.55×10−3; Aref = 0.034; (0.00455−0.034)/0.00163 ≈ −18.1σ; correct.
- Fisher floor (Sec. VI.A): σ(A)=sqrt(3/N) = 9.68×10−4 for N=3,201,160; and 1.78×10−3 for N=949,584; correct.
- Dilution factor g = 2a − 1 with a = 0.6991 gives g ≈ 0.398; implied true-amplitude threshold ≈ 0.75%/0.398 ≈ 1.88%; consistent.

Sigma comparability
- The manuscript is generally careful. At essentially every juxtaposition of σ-values from different nulls/fields, a “not directly comparable” caveat is included (Abstract; Table I; several figure captions; Sec. III.A). This is good practice. Keep this discipline after addressing P4-E1.

Bibliography
- Spot-checked entries [1]–[12]; bibliographic details and arXiv IDs appear correct and consistent with claims in the text.

Standalone-reader test
- The work is self-contained in definitions/estimators. The heavy use of internal artifact file paths in the narrative (P4-M5) should be relocated to Supplemental/DOI manifests for clarity.

Effect sizes
- In most places, σ-values are paired with amplitudes or fractions. Keep this standard uniformly (e.g., in the hemisphere diagnostic once P4-E1 is fixed).

## Summary recommendation
MAJOR REVISIONS

The analysis is careful and most numbers check out, but there are essential issues that must be fixed for PRD: (1) a clear internal contradiction on the hemisphere look-elsewhere result, (2) removal of internal versioning/review-process language and path-like artifact pointers from the body text, and (3) provision of a frozen archival DOI for the released data/code before acceptance. Additionally, correct the numerical inconsistency in Table II (Catalog B Dev.) and streamline/standardize the presentation of null procedures and canonical diagnostic numbers. After these corrections and consolidation of reproducibility materials into a DOI-backed Supplemental, the manuscript will meet PRD’s methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT (fresh eyes)

ESSENTIAL

P4-E4 (Figure 8 caption vs estimator type, pp.10–11): Mixed pre-/post-MASTER language in one caption.
- Offending text: Fig. 8 caption begins “Pseudo-Cℓ of the chirality field Ap on the canonical mask” (i.e., pre-MASTER), but then states “The post-MASTER canonical-mask residual is +3.64σ …”.
- Problem: The panel appears to show pre-MASTER pseudo-Cℓ (and its 200-MC null), while the +3.64σ value is a post-MASTER, single-ℓ result from a different estimator and null. Mixing them in one caption invites misinterpretation.
- Required fix: State explicitly which estimator the figure shows (pre-MASTER pseudo-Cℓ) and remove the post-MASTER number from this caption, or clearly segregate them (e.g., “Panel: pre-MASTER pseudo-Cℓ; separate post-MASTER ℓ=1 result: +3.64σ, see Sec. IV.D”). Also note the relevant null sizes (200-MC for the panel vs 500-MC for +3.64σ).

MAJOR

P4-M7 (Appendix E, edge-on contamination, p.21): Quantitative claim not supported by provided numbers.
- Offending text: “Edge-on galaxy contamination … reduces effective sample size by ∼10–15%, corresponding to a ∼5–8% sensitivity penalty.”
- Problem: You report “65.7% of b/a<0.3 objects receive CW/CCW labels” but do not give the fraction of the catalog with b/a<0.3. The asserted 10–15% Neff reduction cannot be derived from the supplied numbers and may be materially different if edge-ons are common.
- Required fix: Provide the fraction of b/a<0.3 in the spiral catalog and derive the 10–15% Neff reduction (or replace with a measured Neff estimate using per-galaxy weights). Otherwise, rephrase as qualitative.

P4-M8 (Terminology in abstract and Table I row (i)): “Isotropic-bootstrap” is a permutation, not a bootstrap.
- Offending text: Abstract and Table I row (i) call the real-space null “isotropic-bootstrap”.
- Problem: The body defines it as a per-pixel permutation of Ap across in-mask pixels (Sec. IV.C), i.e., a permutation/shuffle, not a bootstrap (resampling with replacement). The label matters for reproducibility.
- Required fix: Rename consistently to “per-pixel permutation null” (or your glossary label once you add it per P4-M3 in the first report), including in the abstract and tables.

P4-M9 (Figure 7 caption and body, pp.10, 8): The “+6.48σ pre-MASTER” number for Catalog A is never defined with its estimator/null.
- Offending text: Fig. 7 caption: “produces … +6.48σ pre-MASTER ℓ = 1 artifact.” Body: Sec. IV.C references the same number once.
- Problem: No table/appendix shows the exact estimator configuration (mask, weight, mean-subtraction status) and null used to compute the +6.48σ value, unlike other ℓ=1 results (which are meticulously documented).
- Required fix: Add a short appendix line or footnote specifying the estimator (pre-MASTER pseudo-Cℓ, mask/weights, monopole-subtraction status) and the null (type, Nrealizations, seed) that yield +6.48σ, or move the claim to Supplemental with a DOI pointer.

MINOR

P4-N6 (Post-/pre-MASTER nomenclature drift, multiple places): “Pseudo-Cℓ” is used loosely.
- Issue: In some places “pseudo-Cℓ” appears to refer to the decoupled (post-MASTER) result; elsewhere it refers to the raw, undeconvolved spectrum. This is especially confusing around Fig. 8 and Sec. IV.D.
- Suggestion: Reserve “pseudo-Cℓ” for the raw, undeconvolved quantity; use “MASTER-decoupled Cℓ” for the deconvolved estimate. State the convention once (Appendix A) and apply it uniformly.

P4-N7 (Real-space p-value convention, Sec. IV.C p.7): Ranking rule not stated.
- Issue: For the primary real-space dipole p-value (p = 0.31), the manuscript does not state whether you use the conservative (k+1)/(N+1) convention (you do state it for Table III). This affects the reported digit in p for finite N.
- Suggestion: Add one sentence in Sec. IV.C: “Real-space rank p is computed as (k+1)/(N+1) with N=10,000 permutations.”

P4-N8 (Appendix A vs body numbers, pp.16 vs 9): Context switch could be clearer.
- Issue: Appendix A states that monopole subtraction reduces decoupled C1 from 2.30×10−5 to 1.51×10−5 and raises z to +3.64 on the canonical mask; the body’s main harmonic number (2.348×10−5, +7.28σ) is for the apodized Nall≥1 footprint with Wp=Nall. The estimators are different and that’s why the numbers differ.
- Suggestion: Add a parenthetical in Appendix A (“canonical mask, not the apodized footprint of Sec. IV.C”) to prevent readers from thinking these are contradictory.

P4-N9 (Appendix D.d, p.19): “~25% of the observed ℓ=1 amplitude” lacks numbers.
- Issue: You quote rℓ=1(BASS+MzLS×Ap)=+0.65 and rℓ=1(DES×Ap)=−0.73, then state the summed leg-induced amplitude is ∼25% of the observed ℓ=1. The mapping from these cross-correlations to the 25% claim is not shown.
- Suggestion: Provide the actual ℓ=1 cross-power amplitudes and the observed C1 amplitude so readers can reproduce the ~25% figure, or move the 25% to Supplemental with the numeric recipe.

P4-N10 (Stale/near-duplicate σ values sprinkled across text/figures): Minor housekeeping.
- Issue: You cite +7.28σ (500-MC apodized), +7.31σ (10k permutations, Table III), +7.21 (internal injection artifact caption). These are all valid in context, but the proliferation of slightly different “observed” σ values can confuse.
- Suggestion: Pick one canonical “observed” σ for the body text (per P4-M4 in your first review) and note in a footnote that alternative field/null choices give 7.21–7.31σ; keep the rest in an appendix table.

WHY THESE ARE NEW
- None of the items above were covered in my initial review. They arose from a second-pass alignment check between captions vs estimator types (P4-E4), unbacked quantitative claims (P4-M7), precise null taxonomy (P4-M8), and places where numbers are quoted without the usual estimator/null provenance that the manuscript otherwise maintains (P4-M9). I also found smaller consistency and clarity issues (P4-N6–N10) that are easy to fix and will improve readability and reproducibility.