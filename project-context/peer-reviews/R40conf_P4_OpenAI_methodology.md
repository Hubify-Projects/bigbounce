# P4 R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=1e2501db pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4876 chars)
**Wall time**: 470.9s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (23 pp)

Scope of review
I audited statistical methodology, estimator declarations, null procedures, dimensional consistency, arithmetic, internal consistency of tables/figures, and reproducibility claims. I recomputed quoted fractions and checked all load‑bearing scalars in the abstract and conclusions against the body.

Overall assessment
The paper is careful about null-procedure distinctions and effect sizes for the primary real‑space dipole estimator. However, there are several essential reproducibility and internal‑consistency issues (most critically, a mismatch in training‑set augmentation arithmetic, pervasive inclusion of internal pipeline/round metadata in the body text, and the absence of a frozen DOI for the released artifacts). Additional major revisions are required to standardize MC sizes/precision for diagnostic significances, tighten multiplicity statements, and correct data‑product inconsistencies noted by the authors themselves.

Findings

ESSENTIAL

P4-E1 — Sec. II.B (Training Labels), p. 3
Problem: Inconsistent training-set augmentation arithmetic. Text states 25,790 source images; after horizontal‑flip augmentation of the training split the “combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323). The 826‑image difference … arises entirely from horizontal‑flip augmentation applied to the training split only.” This is inconsistent with “flip augmentation of the training split”: if every training image were flipped, the pool should increase by ntrain (O(20k)), not by 826. Current numbers imply only ~4% of training images were duplicated via flip, contrary to the description.
Required fix: Precisely document the augmentation policy and reconcile the counts. Provide: (i) the pre‑augmentation 80/20 counts; (ii) the exact number of augmented instances and the selection rule (all vs. subset, class‑balanced, etc.); (iii) corrected totals consistent with the stated policy; and (iv) a small manifest excerpt (hashes/IDs) in Supplementary to verify the split.

P4-E2 — Throughout body (e.g., Secs. II.B p. 3; III.B p. 4; IV.B–E pp. 5–12; Appendices A–E pp. 15–21)
Problem: Pervasive inclusion of internal pipeline paths, round/version tags, and audit‑artifact filenames in the main text (e.g., “pipelines/p2_chirality/.../c17_item13_training_semantics.json”, “c12_r24conf_local_batch.json”, “post‑R29”, “c9b”, “canonical_provenance/…”, “seed 42”). PRD does not accept internal bookkeeping in the body; it also creates brittleness and violates the instruction to avoid review‑log/round‑metadata in the PDF.
Required fix: Move all file‑path mentions, round/version tokens (“Rxx”, “r24conf”, “post‑R29”, “c9a/c9b”), seed values, and artifact names out of the main text into a formal Data/Code Availability subsection or Supplemental Material with stable URLs/DOIs. In the body, replace with neutral references (e.g., “see Supplementary Sec. S3.2”). Remove all review‑round jargon.

P4-E3 — Data Availability, pp. 21–22
Problem: No persistent DOI for the released catalog/code/model at submission time (“A persistent archival DOI … has not yet been minted”). PRD requires a frozen, citable release for reproducibility.
Required fix: Mint DOIs (e.g., Zenodo) for: (i) the exact catalog used (all three tiers), (ii) model weights, and (iii) analysis scripts producing the reported numbers, with version hashes pinned. Replace provisional links and commit‑only references with DOIs in the PDF. State the exact tag/commit corresponding to the DOI.

P4-E4 — Appendix B.d (QC flip reconstruction), p. 17
Problem: The public Parquet release contains 2.9% of rows where “recovered flip probability falls outside [0,1] by up to 0.09,” stemming from a raw/equivariant pass mismatch. Although a QC flag is provided, leaving inconsistent columns in the main data product is a reproducibility hazard; tables/figures in the paper rely on derived quantities from these columns.
Required fix: Regenerate the public release so all probability columns are internally consistent (no [0,1] violations). Alternatively, remove the inconsistent reconstructed‑flip columns from the public catalog and supply a separate, verified companion with exact reconstructions. In the paper, state explicitly that all scientific results were recomputed with the corrected dataset, and update any numbers affected (you report +0.52→+0.48σ for one check; ensure no other statistic changes).

P4-E5 — Abstract and Conclusions, pp. 1, 14
Problem: Several σ values from distinct null procedures are juxtaposed. While many caveats are present, in the abstract some pairs are not accompanied by a plain p‑value or amplitude, potentially inviting misinterpretation (e.g., “+3.64σ … ≈1.9σ Gaussian‑equivalent” without p in the abstract).
Required fix: For every σ quoted in the abstract and conclusions, add the associated one‑sided rank p (or make explicit that Gaussian‑equivalent σ is derived from that p) and the effect size (Adip or C1 value). Retain the “not directly comparable” language. This must be explicit in the abstract itself.

MAJOR

P4-M1 — Multiple sections (IV.C–D pp. 7–12; Appendix A pp. 15–17)
Problem: Mixed MC sizes (NMC = 500 vs 10,000) are used for closely related diagnostic claims, yet σ is reported with two‑decimal precision for the N = 500 streams (e.g., “+3.64σ”, “+4.84σ”). Finite‑MC uncertainty on z is not provided; some headline numbers (e.g., +3.64σ) are later superseded by 10k runs (+7.93σ) under a different field convention, which complicates interpretation.
Required fix: Adopt a single high‑statistics null (≥10k permutations) for all load‑bearing diagnostic σ’s in the paper, or accompany each σ with its MC uncertainty (e.g., via jackknife or by quoting the sampling error on μnull and σnull). Where a number is superseded, report only the definitive value in the body; move legacy values to Supplement.

P4-M2 — Table II (Global CW fraction), p. 5
Problem: The Catalog B (calibrated) row reports fCW = 0.504 ± 0.0003 and z = +14.6 but does not state Nspiral for Catalog B. The quoted uncertainty implies N ≈ 2.8–3.3M but should be explicit.
Required fix: Add a column with Nspiral for each tier (A/B/C) or a footnote with N_B, and verify that the stated σ matches σ = sqrt(f(1−f)/Nspiral). If the tier sample sizes differ (as they likely do), remark on implications for the z-comparison across tiers.

P4-M3 — Appendix C.e (Per‑imaging‑leg multiplicity), p. 19
Problem: The statement “a Gaussian Bonferroni‑15 estimate would underpredict this family‑wise p by ∼250×” is quantitative but unsupported by numbers.
Required fix: Provide the exact Bonferroni p estimate used, the empirical family‑wise p from the max‑statistic null, and the ratio; or remove the “∼250×” claim.

P4-M4 — Diagnostic σ presentation for heavy‑tailed nulls (Sec. IV.D, Appendix A; multiple pages)
Problem: The paper rightly emphasizes that the permutation null is heavy‑tailed and that “moment‑z” and Gaussian‑equivalent σ need not agree. However, many panels foreground moment‑z alone.
Required fix: For every low‑ℓ diagnostic where non‑Gaussian nulls are used, report rank p (with finite‑N resolution) alongside moment‑z in the main text/tables, not only in captions/footnotes. When both are shown, clarify which one is used for any completeness/comparative statement.

P4-M5 — Length vs. contribution (entire manuscript)
Problem: The body interleaves primary results with extensive audit‑artifact prose, making the paper longer and harder to parse than necessary for the stated contribution.
Required fix: Move detailed artifact paths, additional mask sweeps, and secondary diagnostics (e.g., many of the Appendix C/E stratifications) to Supplement. A tight main paper of ≈16–18 pages would suffice, with a clearly organized Supplement referencing stable DOIs.

MINOR

P4-m1 — Appendix D.g, p. 20
Problem: Typo “z ≈ −18.1.23” (stray “23” footnote marker).
Required fix: Correct to “z ≈ −18.1” and place the footnote marker properly.

P4-m2 — Abstract phrasing, p. 1
Problem: “+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent” is potentially confusing without a p‑value; the parenthetical note later in the abstract is long.
Required fix: Add “(one‑sided p ≈ 0.03)” next to the 3.64σ diagnostic in the abstract, or streamline to “3.64σ (p ≈ 0.03; diagnostic only)”.

P4-m3 — Notational consistency, various
Problem: Occasional spacing/diacritics inconsistencies (“C 2 2 ◦”, “ˆ zˆ”).
Required fix: Standardize to “C2 apodization with 2° length” and consistent vector hats.

P4-m4 — Claim of “largest chirality‑labeled catalog,” p. 2 and Conclusions p. 14
Problem: Novelty claim is plausible (3.2M spirals vs 1.95M in Jia et al.). Tighten wording to “largest to date to our knowledge; 3.2M spirals vs. ~1.95M in CE‑ResNet (Jia et al. 2023).” Ensure the comparator in [7] indeed refers to spirals with chirality labels, not total galaxies.

P4-m5 — Reporting precision, various tables
Problem: Mixed significant‑figure usage (e.g., fractions with 6 decimals vs. percentages to 3 s.f.; Cℓ “×10^6” vs raw units).
Required fix: Adopt a uniform reporting precision consistent with MC/statistical uncertainty.

NIT

P4-n1 — Minor grammar/linebreak artifacts in URLs and names (Data Availability, pp. 21–22).
Required fix: Avoid hyphenating URLs; ensure copy‑and‑paste works.

P4-n2 — Figure/caption cross‑references
Problem: Some captions include long parentheticals about null conventions without directly pointing to the exact subsection.
Required fix: Add explicit “see Sec. III A for null‑procedure definitions.”

Abstract‑last drift sweep
- All primary abstract claims (N = 8.47M; Nspiral = 3.201M; HC real‑space dipole +0.41σ, p = 0.31; WLS template exclusion z ≈ −18 for A = 1.7%; harmonic diagnostics +3.64σ/+7.28σ with caveats; A50 ≈ 0.75%; A95 bracketed 1.0–1.5%) are traceable to the body. However, the abstract should add p alongside “+3.64σ” to prevent misinterpretation and must not rely on internal artifact nomenclature (fix via P4‑E2 and P4‑E5).

Provenance surfaces
- Commit hash without DOI and future‑tense promises to mint DOIs are insufficient for PRD (P4‑E3).
- Several internal labels/round notations remain in the body (P4‑E2).

Effect sizes
- Generally adequate; amplitudes (Adip, C1) accompany the σ claims in the body. Ensure this is also true in the abstract for all σ mentions (P4‑E5).

## Summary recommendation
MAJOR REVISIONS

Justification: The science case and primary estimator are sound, and the paper is unusually careful about null procedures. However, essential reproducibility and internal‑consistency problems must be fixed before PRD can consider acceptance: clarify and correct the training‑set augmentation arithmetic; remove internal pipeline/round metadata from the body; provide frozen DOIs for all artifacts; and correct the catalog data‑product inconsistency in reconstructed flip probabilities. Standardize MC sizes/precision for diagnostic σ’s and support quantitative multiplicity statements. With these addressed and some trimming/streamlining, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

ESSENTIAL

P4-E6 — Canonical-mask “in-mask spiral count” inconsistency (Sec. IV.C vs. Appendix D.h)
- The body states that, for the unthresholded test, “all 3,200,420 in-mask equivariant spirals; the remaining 740 of the catalog’s 3,201,160 spirals lie in pixels below the Nspiral(p) ≥ 10 canonical-mask threshold” (Sec. IV.C).
- Appendix D.h’s WLS mask-equivalence audit table, however, reports “In-mask spiral count = 3,201,160” on the canonical mask (Nspiral(p) ≥ 10).
- Both cannot be true simultaneously: if there are 740 spirals in pixels with Nspiral(p) < 10 (outside the canonical mask), then the in-mask spiral count cannot equal the full 3,201,160. This undermines the mask-equivalence claim and any statistic that depends on the exact in‑mask total (e.g., WLS normalization, effective fsky bookkeeping).
- Required fix: Recompute and correct the “in-mask spiral count” in Appendix D.h (and anywhere else it propagates), or correct the Sec. IV.C counts. State the correct number explicitly and update any downstream results if affected.

MAJOR

P4-M6 — C1 amplitude/normalization mismatch across sections (Appendix A.c vs. Table III; footprint/field mixing)
- Appendix A.c states: “monopole subtraction reduces decoupled C1 at ℓ = 1 from 2.30×10−5 to 1.51×10−5 … and increases σ from +1.85 to +3.64 (the canonical-mask number).”
- Table III’s canonical-unapodized, MASTER-decoupled ℓ = 1 shows Cdata = 7.27×10−6, but that block explicitly uses the half‑scaled field fCW−0.5 = Ap/2. If 1.51×10−5 is in Ap units, the corresponding Ap/2 value should be 3.78×10−6 (a factor of 4), not 7.27×10−6 (≈×2.08).
- The paragraph in Appendix A.c also mixes footprints (“on the Nall ≥ 1 footprint… the canonical‑mask number”), which further confuses which mask/field the quoted 2.30→1.51×10−5 refers to.
- Required fix: Unambiguously state, for each quoted C1, the exact footprint (canonical vs. Nall ≥ 1), mask/apodization, weight map, and field normalization (Ap vs. Ap/2). Correct the inconsistent numbers so the Ap↔Ap/2 conversion is exact (×4), or explain why they are not expected to match. Avoid mixing footprints/conventions in a single sentence.

MINOR

P4-m6 — Small but systematic z–rounding inconsistencies (Table II; Sec. IV.B)
- Using the displayed uncertainties, Tier A: (0.507879−0.5)/0.000274 = 28.77σ (paper: 28.72); Tier C: (0.497353−0.5)/0.000279 = −9.49σ (paper: −9.47). You note “computed from the unrounded fraction,” but the visible discrepancy exceeds simple rounding of the shown σ. Either report z computed from the displayed numbers or include a note that both numerator and denominator come from higher precision and provide those in Supplementary.

P4-m7 — Table VII header/labeling ambiguity (fsky vs feff_sky)
- The table header reads “fsky,” but several rows are effective sky fractions feff_sky = ⟨W⟩^2/⟨W^2⟩ (weighted/apodized), while others are raw geometric pixel fractions (binary masks). You do explain the distinction in text, but the table heading is misleading.
- Required fix: Rename the rightmost column to “sky fraction (fsky or feff_sky; see text)” and add per‑row markers or a footnote clarifying which rows are geometric fsky and which are feff_sky.

P4-m8 — Null‑naming inconsistency for the primary real‑space dipole (Sec. IV.C vs Table I)
- The text calls the null “per‑pixel isotropic permutation” while Table I labels it “iso. boot.” They appear to be the same procedure. Standardize the naming (“per‑pixel permutation null”) across the paper to avoid confusion, and point to the subsection where it is defined.

P4-m9 — Appendix A.c wording mixes footprints in one sentence
- “On the Nall ≥ 1 footprint … increases σ … (the canonical‑mask number).” This conflates the Nall ≥ 1 footprint (used for the apodized MASTER diagnostic) with the canonical mask. Please split and make each footprint’s numbers self‑contained.

P4-m10 — Figure/number consistency note (Fig. 9 vs. Sec. IV.C; Table III)
- Fig. 9 caption says the panel annotation uses the canonical “obs. σ ≈ +7.28,” but also mentions the injection artifact’s internal background yields 7.21. Elsewhere, Table III reports +7.31 from 10k permutations. The values are all compatible but scattered across conventions. Consider harmonizing the single “observed” number used in captions with a single agreed null (and move alternates to Supplement).

NO OTHER NEW ISSUES FOUND IN CLASSES B, C, D, E, F, G, H, I, J BEYOND THOSE ALREADY REPORTED
- I rechecked figure–caption vs. body claims, displayed equations/units, cross‑references, abstract traceability, novelty claims, and stale‑number risk. Aside from the additional mask‑count inconsistency (P4‑E6) and normalization confusion (P4‑M6), the remaining items were either already covered in the initial report or are internally consistent with the stated caveats about non‑comparable nulls.