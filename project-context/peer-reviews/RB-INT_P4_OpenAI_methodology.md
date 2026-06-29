# P4 RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_RB.pdf` md5=b8dc2625 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6777 chars)
**Wall time**: 320.1s

---

Referee report for PRD (methods/statistics) — Paper P4

Scope of review
- Focus: statistical methodology rigor, estimator declarations, null procedures and significance reporting, internal arithmetic and unit consistency, reproducibility, and abstract–body alignment.
- I read the full 24-page manuscript, including figures, tables, appendices, and the abstract, and recomputed all numerically checkable quantities from the values provided.

Overall assessment
The paper presents a very large chirality-labeled catalog (8.47M galaxies; 3.20M spirals) and a primary null result for a real-space chirality dipole using an explicitly declared estimator hierarchy. The manuscript is unusually diligent about separating null procedures and repeatedly states non-comparability of σ values derived under different nulls. Many internal arithmetic checks pass. However, there are several essential issues that must be corrected for PRD standards, including (i) reproducibility gaps and unresolved placeholders for archived artifacts/DOIs, (ii) a materially confusing duplication for the canonical ℓ=1 MASTER result (+3.64σ vs +7.93σ) that is not sufficiently reconciled and presently undermines clarity, and (iii) an inconsistency in quoted best-fit WLS dipole amplitudes (0.32% vs 0.455%) that needs unambiguous resolution. In addition, the “−18σ” template-fit “exclusion” uses a block bootstrap but is still expressed in Gaussian σ; this should be reported with bootstrap percentile CIs, not a nominal “σ” which implies Gaussian tails the bootstrap does not guarantee.

Findings

ESSENTIAL

P4-E1 (Data availability, frozen artifacts, and placeholders)
- Location: Data Availability (p. 23); scattered throughout main text referencing internal artifact paths.
- Problem: The manuscript relies critically on code and “committed artifacts” referenced via internal repository paths (e.g., pipelines/p2_chirality/outputs/... and shorthand tags like “artifact c9b”), but:
  • No immutable archived snapshot/DOI is provided (“will be deposited at journal submission”).
  • The HuggingFace catalog link shown in the PDF has embedded spaces/line breaks (“https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog”), which is not a resolvable URL as printed.
  • Numerous body-text references to artifact filenames and path suffixes are not useful to readers unless the exact commit/snapshot is frozen and available as Supplemental Material or a DOI-archived bundle.
- Required fix: Before acceptance, provide:
  • A single immutable, versioned archive (Zenodo DOI) containing all “committed artifacts” referenced, including the exact masks, null arrays, MASTER config files, injection-recovery outputs, and the “c9b” and similar bundles. Replace all “will be deposited” text with an actual DOI and version tag.
  • Correct, copy-pasteable URLs without line breaks; specify exact version/timestamp/commit for the HuggingFace datasets and model, or archive identical copies in the DOI package.
  • Move all internal path references to a structured Supplemental Material index (with SM figure/table labels) and refer to those rather than raw repository paths in the body.

P4-E2 (Canonical ℓ=1 MASTER: 500-MC +3.64σ vs 10k-permutation +7.93σ mismatch)
- Location: Abstract (p. 1), Sec. IV D (pp. 11–12), Table III (p. 11), Conclusions item (c) (p. 16).
- Problem: For the same “canonical unapodized” MASTER ℓ=1 diagnostic, the manuscript presents two materially different z-values:
  • +3.64σ (500-MC direct run; pMC = 0.030).
  • +7.93σ (10^4-permutation recompute; Table III).
  The text states they are “from different null-run sizes,” but the factor >2 jump in z cannot be explained by increasing the number of null realizations alone. Table III’s caption mentions a specific field normalization (fCW−0.5 with Nspiral-weighted subtraction), but the +3.64σ panel does not clearly specify whether it is the same field/normalization and coupling matrix. As it stands, the reader is left with two incompatible “canonical” values.
- Required fix:
  • Unambiguously document the estimator definitions and inputs for both numbers in one place (mask, weight map, field definition and monopole treatment, coupling matrix, and null-construction details). State explicitly what differs between the +3.64σ and +7.93σ computations beyond NMC.
  • If they are genuinely the same estimator under the same field/mask, resolve the discrepancy and retain a single canonical value (preferably the high-statistics 10k run), demoting the other to a historical note in SM.
  • At every remaining juxtaposition of σ from different nulls/fields/masks, add the explicit “not directly comparable” language locally (not only by cross-reference to Sec. III A).

P4-E3 (Inconsistent best-fit WLS dipole amplitude: 0.32% vs 0.455%)
- Location: Sec. V.A (p. 12): “maximum WLS template amplitude ... 0.32% (in Ap units)”; Appendix D Table X (p. 21): “Adipole = 4.55×10−3 in Ap units,” i.e., 0.455%.
- Problem: The body presents 0.32% as the “maximum WLS template amplitude in the full-footprint regional fit” while Appendix D’s joint nuisance-marginalized WLS on the canonical mask recovers 0.455%. Without a precise explanation of the estimator/regression design and footprint differences, these appear contradictory.
- Required fix: Specify precisely:
  • What “full-footprint regional fit” refers to (design matrix, mask, weighting, and whether it is the same as the 9-template canonical-mask WLS of Table X).
  • Why the “maximum” in Sec. V (0.32%) is lower than the canonical joint fit (0.455%). If they are different partitions or estimators, label them clearly and avoid cross-comparing amplitudes without that caveat.
  • Provide the observed-space effect size consistently for the adopted primary-template regression (i.e., quote 0.455% with its block-bootstrap CI) and relegate the 0.32% regional result to SM with full configuration.

P4-E4 (Abstract/URLs; copy-editing of critical links)
- Location: Abstract (p. 1), Data section (p. 2), Data Availability (p. 23).
- Problem: Several URLs are broken by line breaks/spaces in the PDF (e.g., the HuggingFace dataset link in Data Availability has inserted spaces).
- Required fix: Ensure all URLs are unbroken in the typeset PDF (use \url or equivalent) so they are directly usable. Provide precise resource identifiers (version tags/SHAs/DOIs) for all external datasets used, including Smith42/galaxies.

MAJOR

P4-M1 (Bootstrap-based “−18σ” exclusion reported as Gaussian-z)
- Location: Appendix D, Table X (p. 21) and text; Sec. III.B (p. 3).
- Problem: The “primary exclusion” of a clean 1.7% dipole is reported as “z ≈ −18.1 under the adopted NSIDE=8 block-bootstrap error model.” While you did a block-size sensitivity test, you still quote a Gaussian σ for a bootstrap-derived uncertainty. With 1000 bootstrap replicates (and blocks of size NSIDE=8), interpreting the difference/σboot as “−18σ” implies a precise normality that bootstraps do not guarantee, and 1000 draws do not calibrate such extreme tail probabilities.
- Required fix: Replace the “−18σ” language with:
  • A percentile bootstrap confidence interval for Adipole and a clear statement that Aref = 1.7% lies well outside the 99.9% CI (report the actual CI).
  • If you retain a standardized difference, label it as “difference divided by bootstrap SE” and explicitly state that it is not a Gaussian significance. Provide the full bootstrap distribution of Adipole in SM.

P4-M2 (Overuse of internal artifact names and code paths in main text)
- Location: Many sections (e.g., Sec. IV C, IV D, Appendices), throughout.
- Problem: The main text is peppered with raw repository path names (“pipelines/p2_chirality/...”) and internal short tags (“artifact c9b”) that are not meaningful to readers unless they have the exact repository snapshot. PRD style prefers self-contained descriptions in the body and relegating run logs to SM.
- Required fix: Consolidate these details into a Supplemental Material file with stable figure/table labels (e.g., SM-Fig. S1, SM-Table S2). In the body, replace path strings with SM references and one-sentence descriptions of what each artifact contains.

P4-M3 (Harmonic-channel completeness claims — report numerics)
- Location: Conclusions item (a) (p. 15), Fig. 9 (p. 16), Table VI (p. 15).
- Problem: You state P(≥3σ) ≥ 0.999 at Ap ≥ 0.75% and give a median z range for 1.7% and 3.0%. To meet PRD standards, the sampling uncertainty on these completeness estimates (with 10^3 injections per amplitude per axis) should be reported. The figure notes “axis-averaged” but the exact axes used should be enumerated in the caption or text.
- Required fix: For each amplitude point in Table VI, add binomial SE on P(≥3σ). In Fig. 9 caption, list the axes used for the per-axis curves, and point to SM for the full table of per-axis results.

P4-M4 (Primary selection threshold pre-specification)
- Location: Sec. III.B (p. 3), Sec. IV C (pp. 7–9).
- Problem: You assert peq > 0.6 was pre-specified in the generator script and show robustness to alternative cuts. For PRD, pre-specification should be anchored by the frozen analysis code commit (or SM log) prior to looking at the primary dipole results.
- Required fix: In SM, provide the git commit hash and timestamp of the exact script (“run_dipole_catalog_c.py”) establishing peq > 0.6 before running the null-calibrated primary estimator. If not available, explicitly downgrade “pre-specified” to “adopted a priori and verified robust by a full cut-sweep.”

P4-M5 (Clarify the sample/mask footprint differences wherever amplitudes/σ are compared)
- Location: Several places where results across canonical mask vs apodized Nall footprint are compared (e.g., Sec. IV C–D, Table I/III).
- Problem: While you often state that numbers are not comparable, the reader must infer the exact field/mask differences from scattered text.
- Required fix: Add one consolidated table (in main text) that lists, for every quoted σ/amplitude in the paper, the triplet {field definition, mask/weight, null type}. This will prevent misinterpretation and make the “not comparable” statements fully traceable.

MINOR

P4-n1 (Arithmetic and consistency checks)
- Location: Table II (p. 7–8), Sec. IV A/B.
- Check: Recomputed fCW and binomial errors match:
  • Catalog C: 1,592,107/(1,592,107+1,609,053) = 0.4973526; σ = 0.0002796; z = −9.47; Excess = −0.265% — all consistent.
  • Catalog A: σ ≈ 0.0002742; z ≈ +28.7 — consistent.
  No action required.

P4-n2 (Units, notation, and axes)
- Location: Passim; e.g., Figures 4, 7, 8 and Table III.
- Notes: Units and asymmetry conventions are generally clear; you consistently note Ap = 2(fCW − 1/2). Keep this in figure captions to avoid ambiguity, especially in Fig. 7 where the color scale is in fCW. Ensure all figures use unambiguous axis labels (e.g., “Ap (dimensionless)”, “fCW”).
- Suggested fix: Add explicit axis labels/units to each figure panel (if not already present in the high-resolution PDF).

P4-n3 (Typos/formatting)
- Location: Multiple places
  • “C 2 2◦” spacing inconsistent; use “C2 2°” or “C2 with 2° apodization” consistently.
  • Footnote 2 on p. 11–12: duplicated phrase fragment “reproduces 99.33% of the observed pre-MASTER pseudo-C(ℓ=1)ℓ power, vs. 99.32% for the observed pre-MASTER pseudo-C(ℓ=1)ℓ power” looks like an editing artifact. Clean up.
  • Ensure all URLs have no embedded spaces/line breaks.
- Fix: Copyedit.

P4-n4 (Effect size with σ)
- Location: Sec. IV C, Appendix D.
- Note: You usually provide amplitudes with σ; keep doing so everywhere (e.g., also report the observed Ap amplitude alongside the +7.28σ harmonic-channel number in Table III).

P4-n5 (Length)
- Location: Whole paper (24 pages).
- Comment: The manuscript is long for a primary null result and a catalog release. Consider moving detailed internal path references and some diagnostic panels from the main text to SM. A 18–20 page target would improve readability without losing content.

NIT

P4-N1 (Terminology)
- Location: Passim.
- Suggest replacing “σ (moment-z)” by “z (moment-based)” consistently to avoid conflating with Gaussian σ.

P4-N2 (Seeds)
- Location: Multiple.
- Suggest summarizing RNG seed usage once in Methods/SM rather than in-line.

P4-N3 (“Flip-swap correlation = 1.000”)
- Location: Sec. III D (p. 4–5).
- Minor stylistic: “= 1 by construction” is sufficient; extra decimals imply unwarranted precision.

Abstract-last drift sweep (pattern-045)
I re-read the abstract after the full body:
- The key numbers in the abstract (+0.41σ real-space, z = 0.58 under per-galaxy shuffle; N ≈ 9.5×10^5 spirals; WLS exclusion of 1.7% at z ≈ −18; harmonic-channel +3.64σ (canonical) and +7.28σ (apodized); monopole-mask leakage reproducing 99.32% pre-MASTER ℓ=1 power; injection-recovery A50 ≈ 0.75% and A95 bracketed 1.0–1.5%) are all present in the body. However, the abstract also mentions the “+7.93σ” (Table III) indirectly via the canonical rows and the +3.64σ value elsewhere; see P4-E2 — these must be reconciled (present one canonical number and stick to it).
- The abstract carefully notes non-comparability of σ from different nulls. Good.
- The “falsification criterion” is tied to A95 bracket; backed in Sec. VI B/Table V. Good.
- The statement “block-bootstrap WLS template fit disfavors a clean 1.7% dipole … at z ≈ −18” needs de-Gaussianizing (P4-M1).

Provenance surfaces (patterns 046/047)
- The manuscript relies on a live repository and lacks a frozen DOI. Essential to fix (P4-E1).

Uncomputed quantitative claims (pattern-048)
- Most qualitative claims are backed by numbers or artifact pointers. Where words like “dominated”, “unchanged”, “persist” appear (e.g., harmonic channel under depth-stratified null), you provide the two σ values (+7.28 vs +7.13). Acceptable.

Standalone-reader test
- The primary methodology is self-contained. However, reliance on internal path references (without a frozen SM) harms reproducibility. Address with SM and DOI (P4-E1, P4-M2).

Bibliography
- Spot checks (e.g., Jia et al. 2023 ApJ 943:32; Iye et al. 2021 ApJ 907:123; DESI Legacy Surveys AJ 157:168) match. Good.

## Summary recommendation
MAJOR REVISIONS

Rationale
The paper’s primary null result appears methodologically sound and carefully caveated. Many internal numerical checks pass. However, PRD acceptance requires (i) fully frozen and accessible reproducibility artifacts/DOIs, (ii) reconciliation of the conflicting canonical ℓ=1 MASTER significances (+3.64σ vs +7.93σ) under a single, clearly defined estimator, and (iii) correction of an internal inconsistency in quoted WLS amplitudes (0.32% vs 0.455%). Additionally, the bootstrap-based “−18σ” language must be reframed using bootstrap CIs rather than Gaussian σ. With these essential and major issues resolved and the artifact references moved to well-structured Supplemental Material, the manuscript could be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P4-E5 (Training/augmentation arithmetic inconsistency; split semantics unclear)
- Location: Sec. II.B (p. 3), Appendix B.a (p. 18).
- Problem: The counts for the train/val split and flip augmentation don’t add up. You state the source pool is 25,790 images, split 79.4/20.6 “pre-augmentation,” with nval = 5,323 (never augmented) and ntrain = 21,293 “post-augmentation,” and that the 826-image increase from 25,790 to 26,616 “arises entirely from horizontal-flip augmentation applied to the training split only.” But:
  • A 79.4% split implies ~20,480 training images pre-augmentation, not accounted for explicitly.
  • “Horizontal-flip augmentation applied to the training split only” would typically double the training pool, not add ~4% (826). 
  • The stated numbers imply only a small fraction of the training set was actually duplicated by flip, contrary to the prose.
- Required fix: Provide an exact accounting table: pre-augmentation train/val counts, how many images were flip-augmented (and why only those), and the deterministic rules/seed used. If augmentation is on-the-fly (not manifested as extra files), restate the language to avoid implying a fixed-count increase and remove the “826-image difference” explanation.

P4-E6 (Apodized MASTER C1 amplitude mismatch: 2.348×10−5 vs 2.474×10−5)
- Location: Sec. IV.C.b (p. 9): “C1 = 2.348×10−5, +7.28σ”; Table III (p. 11), apodized ℓ=1 row: “Cdata ×10^6 = 24.74” (i.e., 2.474×10−5), z = +7.31.
- Problem: These are presented as the same diagnostic channel (apodized footprint, Wp=Nall), yet C1 differs by ~5%. The caption suggests both are single-ℓ decouplings, so the “distinct estimator” rationale is unclear here.
- Required fix: Recompute and reconcile. If one value is superseded, keep only the canonical number (with its null) in the main text; move the other to SM with a precise statement of what differs (seed, mask, monopole subtraction convention, binning object, or code version).

MAJOR

P4-M6 (Map-level rotation robustness missing)
- Location: Sec. III.D (p. 4–5), Appendix B.c (p. 18).
- Problem: You report a D4-TTA hold-out on small subsamples showing 21.4% argmax flips between Z2 and D4 for borderline cases, but there is no catalog-level rotation robustness test of the actual cosmological estimators (real-space dipole, MASTER ℓ=1). Since only Z2 TTA is used in production, rotational non-equivariance could couple to the patchy footprint.
- Required fix: Add a map-level audit: re-infer a representative sky patch with D4-TTA (or rotate the images by 90°/180° and re-run the estimators) to demonstrate the real-space dipole and MASTER ℓ=1 do not change beyond null scatter. If computationally prohibitive, provide a quantified upper bound via a targeted large patch plus SM documentation.

P4-M7 (Figure/Table harmonization for canonical diagnostics)
- Location: Fig. 8 (p. 10), Table III (p. 11), Appendix D.b (p. 20).
- Problem: Canonical low-ℓ significances differ across panels due to differing null batteries and field conventions (e.g., Fig. 8 shows σℓ=1 = +3.63; Table III canonical row ℓ=1 z = +7.93). Although you note non-comparability, a casual reader could misinterpret the differences as run-to-run instability.
- Required fix: Provide a single harmonized SM table where the canonical pre- and post-MASTER values at ℓ=1–5 are recomputed under a unified null and field normalization. In the body, add a one-line pointer to that SM table next to Fig. 8 and Table III to preempt confusion.

P4-M8 (QC: probabilities outside [0,1] in recovered flip pass; production-data hygiene)
- Location: Appendix B.d (p. 18–19).
- Problem: You report that, for 2.9% of rows (1.6% CW-channel rate), probabilities reconstructed for the “flip pass” fall outside [0,1] by up to 0.09, attributed to a raw/equivariant pipeline-pass mismatch. While you flag those rows and show negligible impact on the HC dipole, PRD catalog releases should avoid such anomalies in primary columns.
- Required fix: Either (i) include explicit stored flip-pass probabilities in the released catalog so no reconstruction is needed, or (ii) regenerate the raw/equivariant columns so that reconstruction yields valid probabilities in [0,1] for all rows. Document the fix and ensure the HC results are unchanged.

MINOR

P4-n6 (Typesetting/notation error in Eq. 4; missing radical)
- Location: Sec. VI.B.a (p. 13–14).
- Problem: Equation prints “σ(A) = s 3/Nspiral” instead of σ(A) = sqrt(3/Nspiral). Also, the relation σ(A) = 2√3 σ(fCW) is correct but would benefit from parentheses.
- Fix: Correct to σ(A) = sqrt(3/Nspiral) and add parentheses for clarity.

P4-n7 (Hemisphere LEE p-value reported as “≤ 10−4” without k)
- Location: Appendix C.c (p. 20).
- Problem: Reporting pLEE ≤ 10−4 is ambiguous. With N = 10,000 shuffles, the minimum possible p is 1/(N+1) ≈ 1.0×10−4, but the exact exceedance count k is not given.
- Fix: Report k and N explicitly (e.g., k = 0 of 10,000; p = 1/(N+1) = 1.0×10−4, one-sided). State the sidedness in-line.

P4-n8 (WLS coefficient scaling; interpretability of nuisance-template z’s)
- Location: Appendix D.g, Table X (p. 21).
- Problem: Leg-fraction coefficients have enormous naive σ (~6×10^2) due to near-collinearity and unstandardized predictors, rendering the individual z’s uninformative. Meanwhile, you do interpret some other nuisance-template z’s.
- Fix: Standardize all regressors before WLS or report coefficients/z’s in standardized units (or suppress individual nuisance-template z’s entirely and focus on the marginalized dipole with its CI).

P4-n9 (Primary-mask fsky clarity)
- Location: Table I note a (p. 5), Sec. IV.C (pp. 7–9).
- Problem: The primary real-space estimator is run on the HC subset with fsky = 0.4801 (Nspiral(p)≥10 recomputed on HC), not the often-cited canonical-mask fsky = 0.49005. While this is footnoted in Table I, some narrative sentences still refer to “the canonical mask … used throughout” and could mislead.
- Fix: Add a brief parenthetical in Sec. IV.C at first mention of the primary estimator: “Using the HC recomputed Nspiral(p)≥10 mask (fsky = 0.4801), not the full-catalog canonical 0.49005.”

P4-n10 (URL/textual nits beyond those already flagged)
- Location: Sec. III.C (p. 4), figure captions.
- Problem: Minor spacing/formatting artifacts (“V iT − Small”; inconsistent “C 2 2◦” spacing) appear in several places beyond those already listed.
- Fix: Copyedit for uniform typography (e.g., “ViT-Small”; “C2 apodization with 2° length”).

NO OTHER ISSUES FOUND in classes A–J beyond those already reported and the additions above. Most arithmetic spot-checks remain consistent; equations are dimensionless where appropriate; and cross-references generally point to the right sections.