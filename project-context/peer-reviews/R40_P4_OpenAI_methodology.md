# P4 R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6960 chars)
**Wall time**: 418.9s

---

Referee report (methodology/statistics), Physical Review D

Paper: “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole …”

Scope of review
- Focus: statistical validity, estimator declarations, null procedures, internal arithmetic and dimensional consistency, significance claims, reproducibility surfaces, and whether abstract/conclusions are fully supported by body text.
- I checked all quoted counts, fractions, and main σ/p claims against the equations and tables provided in the PDF.

Overall assessment
- The work presents a very large chirality catalog and a careful null-detection analysis with extensive systematic diagnostics. Many numerical claims check out (counts, fractions, key σ values).
- However, there are several issues that must be fixed for PRD standards: one clear internal inconsistency (hemisphere look-elsewhere), pervasive in-text references to ephemeral “artifact” file paths and revision-log language inside the body, lack of an immutable archived DOI for the exact version reviewed, and a few load-bearing numbers that only appear via unarchived artifact pointers rather than in the manuscript proper. There are also places where σ values from different null procedures are juxtaposed without a local “not comparable” disclaimer.

Findings

ESSENTIAL

P4-E1
- Location: Sec. III.B (page 4, “Declared Analysis Hierarchy”) vs. Appendix C.c (page 19) and Table I row (v) (page 5)
- Problem: In Sec. III.B you write: “hemisphere maximum-asymmetry (3.05σ … < 1σ after look-elsewhere correction; Appendix C).” But Appendix C.c states the principled, direct-MC look-elsewhere correction gives pLEE ≤ 10−4 (i.e., highly significant), while only a heuristic Bonferroni gives < 1σ. Table I row (v) also lists “pLEE ≤ 10−4” (and labels it “post-look-elsewhere-corrected significance”). These are mutually inconsistent and confuse “principled” vs. heuristic corrections.
- Required fix: Reconcile and state a single, correct result for the look-elsewhere-corrected hemisphere statistic. If the direct-MC maximum-statistic null is your declared correction, report that consistently in Sec. III.B, Table I, and Appendix C; remove the contradictory “< 1σ after look-elsewhere” language (or clearly label it as a heuristic Bonferroni cross-check, not the adopted correction). Make the wording in Table I consistent (don’t call a quantity both “post-LEE” and “raw direct-MC” in the same cell).

P4-E2
- Location: Appendix E.d (page 21–22)
- Problem: Revision-log prose in the body: “An earlier version of this paragraph overstated the stability as ‘< 0.5σ variation’. The sweep has now been recomputed …”
- Required fix: Remove revision-history language and present the current, final result only. PRD does not accept internal version-history narrative in the manuscript.

P4-E3
- Location: Appendix D, footnote (page 20; the NSIDE=8/4/16 block-scale sensitivity footnote)
- Problem: Internal version tag appears: “computed post-R29 on the same catalog …”
- Required fix: Remove “post-R29” (review-round/internal tag). State only the current analysis details.

P4-E4
- Location: Throughout (e.g., pages 3, 5–16, 18–22; many instances)
- Problem: Pervasive in-text references to ephemeral internal artifact paths and filenames (e.g., “pipelines/p2_chirality/outputs/canonical_provenance/c12_r24conf_local_batch.json,” “artifact c9b,” etc.). These are not citable research artifacts and will not be usable by PRD readers.
- Required fix: Replace all such path-level references by (i) stable, archived DOIs (Zenodo/OSF) for the exact, immutable analysis artifacts used; and (ii) concise, human-readable figure/table or appendix references in the paper. Move any large runbooks/JSON dumps into a single “Supplemental Material” with a DOI. No local filesystem paths in the body text.

P4-E5
- Location: Data Availability (page 22)
- Problem: No immutable DOI for the exact code/data snapshot used; “A persistent archival DOI … has not yet been minted.” Also includes internal version stamp text (“commit 53b41d12 (v1.0.185 lineage) … same-day metadata and figure commits …”).
- Required fix: Before acceptance, provide immutable archived DOIs (or equivalent PRD-vetted repositories) for: (a) the exact catalog used; (b) the exact code state and configuration; (c) the committed masks/weight maps; (d) the primary summary artifacts supporting each headline result. Remove internal version-log prose; cite only the frozen releases/DOIs.

P4-E6
- Location: Sec. V.A (page 12)
- Problem: A load-bearing numerical claim (“our maximum WLS template amplitude … 0.32% in Ap units”) appears only via an unarchived artifact pointer; it is not tabulated or plotted in the paper.
- Required fix: Include this number (with uncertainty and method details) in a table or figure within the paper (or in Supplemental Material with DOI). The body must contain the numerical value and how it is obtained (mask, weights, null, uncertainty).

P4-E7
- Location: Abstract (page 1); Sec. IV.D/Table X (pages 10/20)
- Problem: The abstract states “disfavors a clean cosmological dipole at the 1.7% reference amplitude at z ≈ −18” without clarifying units. In the body, Aref = 1.7% is in fCW units, which corresponds to 3.4% in Ap units (Aref = 0.034 in Table X).
- Required fix: Specify units in the abstract to avoid confusion (e.g., “1.7% in fCW units (Ap = 3.4%)”). Similarly, ensure the first mention in the conclusions clarifies this conversion.

P4-E8
- Location: Sec. IV.C para ending with “Catalog A (raw) shows a 2.31σ real-space dipole and a +6.48σ pre-MASTER …” (page 8), and any other lines that juxtapose σ from different nulls without a local caveat
- Problem: σ values from different null procedures are listed side-by-side without an explicit local “not directly comparable” qualifier in that sentence (even though the paper carries such caveats elsewhere).
- Required fix: Add an explicit local qualifier whenever heterogeneous σ are juxtaposed in the same sentence (“from distinct null procedures; not directly comparable”).

MAJOR

P4-M1
- Location: Sec. IV.C (pages 8–9) vs. Table III (page 11)
- Problem: Two different ℓ = 1 MASTER estimators are used: (i) single-mode-only decoupling (C1 = 2.348×10−5) and (ii) the ℓ = 1 band from a full 39-band deconvolution (C1 ≈ 24.74×10−6). The paper says they are “distinct estimators” but does not explain why they differ numerically and what practical impact that has.
- Required fix: Add a concise methodological paragraph clarifying the difference between the two ℓ = 1 constructions, why the values differ by ~5%, and confirm that both use identical masks/fields/monopole treatments except for the binning scheme. State explicitly which one is the declared diagnostic estimator.

P4-M2
- Location: Secs. IV.D, VII.c, Table III (pages 10–15)
- Problem: Mixed null-sample sizes are used for headline σ (500 and 10,000 permutations) for the canonical-mask and apodized-footprint diagnostics. While you mention this, the presentation is still confusing.
- Required fix: For each quoted σ/p, state NMC and (if applicable) the MC uncertainty on σ or on the rank-p (e.g., Clopper–Pearson for exceedances). Consider standardizing on the larger null sample (10,000) for the tabulated diagnostics, or clearly tag which is canonical for the paper’s conclusions.

P4-M3
- Location: Sec. IV.C (pages 7–9) “A95,nq” null-quantile bound
- Problem: You present A95,nq (95th percentile of the permutation null) but do not show the MC uncertainty on this quantile from NMC = 10,000, nor do you show sensitivity to mask/weighting choice.
- Required fix: Quote the MC error on A95,nq (e.g., via order-statistic variance) and clarify that this is estimator- and mask-specific. Alternatively, move it to Supplemental with a short sentence in the body.

P4-M4
- Location: Sec. V.A (page 12)
- Problem: The claim “discrepancy most likely reflects two factors” implicitly attributes Shamir-class signals to the leakage channel plus audit limitations, but without a matched-footprint reanalysis this remains qualitative.
- Required fix: Soften the phrasing or add a quantitative bound showing what amplitude a clean “Shamir-like” dipole would yield in your harmonic channel (you partly do this in VII.a; ensure explicit cross-link and quantify the mismatch in effect-size units).

P4-M5
- Location: Sec. III.D and Appendix B (pages 4, 17)
- Problem: Rotation-equivariance checks and flip-TTA protocol are clear, but the role of calibration is only discussed qualitatively; the catalog is admitted to be strongly overconfident.
- Required fix: Add a short quantitative reliability diagram or ECE number for the spiral-only CW/CCW probabilities on the GZ1 cross-match (acknowledging GZ1 noise), or make explicit that peq is used solely as a ranking score and not a probability, with all thresholds defined operationally (you already state this; a one-sentence reinforcement with a pointer to a reliability plot in Supplemental would resolve this).

P4-M6
- Location: Data Availability (page 22)
- Problem: The current Hugging Face links are mutable tags (“v2026.04”) and the model checkpoint is not linked to an immutable DOI. PRD reproducibility policy expects archival stability at publication.
- Required fix: Provide permanent DOIs (Zenodo, etc.) for the dataset snapshot, model weights, and code (or fixed commit submodules), and cite them in the paper.

P4-M7
- Location: Whole manuscript
- Problem: The manuscript is very long for a single-methods paper; substantial space is spent on path-level artifact references and cross-run bookkeeping not needed in a PRD article.
- Required fix: Trim to ≲18 pages by moving implementation details and artifact references to a single Supplemental Material (with DOI). Keep in-body only the minimal, declared estimators, the main numbers (with uncertainties), and the eight-anchor systematics summary.

MINOR

P4-N1
- Location: Table II (page 5)
- Problem: Catalog B line: fraction “0.504 ± 0.0003” and “+14.6σ” implies a Δf/σ ≈ 13.3 if σ = 0.0003 exactly. This likely reflects the unrounded internal σ or fraction.
- Required fix: Either provide one more significant digit in the fraction or compute the σ entry from the printed numbers to avoid apparent mismatch.

P4-N2
- Location: Sec. IV.A (page 5)
- Problem: “percentages rounded to maintain sum-to-one consistency at the second decimal” — the precise unrounded values are later given; good. Consider moving the exact values into Table I/II footnotes for ease of reference.
- Required fix: None strictly required; optional consolidation.

P4-N3
- Location: Appendix A.c (page 16)
- Problem: You report the effect of monopole subtraction on C1 and z. It would help readers if you showed the before/after C1 and ⟨C1⟩null, σnull in a small table, since this is central to the leakage narrative.
- Required fix: Add a 2-row mini-table or fold these numbers into Table III (or Supplemental).

P4-N4
- Location: Appendix B.d (page 17–18)
- Problem: T5 (metadata leakage) uses linear Pearson r with RA, which you correctly note is circular. You already flag the limitation; consider adding Spearman on sin/cos(RA) or a spherical harmonic regression snippet in Supplemental (you partly do a low-ℓ Yℓm regression later).
- Required fix: Optional clarification that the low-ℓ regression is the preferred check.

P4-N5
- Location: Acknowledgments (page 22)
- Problem: “AI tool usage” note is fine, but PRD typically expects clarity that all scientific results are fully reproducible without proprietary AI tools. You’ve stated verification by the author.
- Required fix: None required; optional rephrase to match PRD style.

NITS

P4-Ni1
- Location: Multiple
- Problem: Occasional mixed typography in symbols (ˆ y, ˆ zˆ) and accents.
- Required fix: Standardize unit vectors and accents.

P4-Ni2
- Location: Figures 4, 5, 7
- Problem: Color bars lack units (even if dimensionless, stating “Ap” or “fCW” adds clarity).
- Required fix: Label “Ap” or “fCW” explicitly on the color bar.

P4-Ni3
- Location: References
- Problem: Style: Ref. [39] is a GitHub repository; ensure citation format matches PRD style with access date/commit.
- Required fix: Update to PRD reference style for software.

Arithmetic and internal-consistency spot checks (passed)
- Catalog C counts sum correctly: 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531.
- fCW(C) = 1,592,107 / 3,201,160 = 0.497353; binomial σ ≈ 0.000279; deviation −9.47σ consistent with Table II.
- HC sample size quoted as 949,584 (≈ 9.5×10^5) matches Abstract.
- Real-space dipole: Adip = 4.4×10−3 (Ap units) with moment-z 0.41 vs an isotropic-permutation null of NMC = 10,000, and rank-p = 0.31, consistent with the text.
- NaMaster apodized ℓ = 1: C1,data = 2.348×10−5, ⟨C1⟩null = 1.71×10−6, σnull = 2.99×10−6 → z ≈ 7.28; matches.
- Canonical-mask pre-MASTER leakage reproduces 99.32% of pseudo-Cℓ=1 with residual +1.69σ (Table IV values check).
- Block-bootstrap WLS: Abest = 4.55×10−3, σboot = 1.63×10−3. Test vs Aref = 0.034 (Ap units) → z ≈ (0.00455−0.034)/0.00163 ≈ −18.1; matches.
- Fisher floor: σ(A) = √(3/N) → 9.7×10−4 for N = 3,201,160 and 1.78×10−3 for N = 949,584; matches.

Effect sizes and “not comparable σ” disclaimers
- In most places you clearly flag that σ values come from distinct nulls and are not comparable; keep this rigor everywhere you juxtapose heterogeneous σ. See P4-E8 for the one sentence that needs a local caveat.

Standalone-reader test
- The main derivations and estimators are self-contained, but many supporting numerical claims are only pointed to via internal artifact paths. These must be either brought into the paper (tables/figures with numbers) or moved to Supplemental with an immutable DOI and described in prose in the body.

Page length
- The paper (23 pages) is long for the net methodological contribution. Much of the length stems from inline artifact pointers and process notes that belong in Supplemental. Consider a target of ≲18 pages by moving operational details and keeping the eight-anchor systematics summary concise.

## Summary recommendation
MAJOR REVISIONS

The core methodology and most numerical claims are sound and carefully caveated, and the primary conclusions (null real-space dipole; leakage-dominated pre-MASTER artifacts; post-MASTER residuals as systematics) are supported by the presented analyses. However, there are critical issues that must be fixed for PRD: (i) the internal inconsistency on hemisphere look-elsewhere correction; (ii) pervasive internal file-path references and revision-log language in the body; (iii) lack of immutable archived DOIs for the exact analysis artifacts; and (iv) a few load-bearing numbers that are only referenced via artifacts, not shown in the paper. Addressing the ESSENTIAL and MAJOR items above will make the manuscript compliant with PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL

P4-E9
- Location: Sec. II.B (page 3), training-split/augmentation counts
- Problem: The stated “80/20 split: ntrain = 21,293, nval = 5,323” with a source manifest of 25,790 and “+826 due to flip augmentation applied to the training split only” is arithmetically inconsistent.
  • If 20% of 25,790 went to validation without augmentation, nval should be 5,158, not 5,323 (+165).
  • If augmentation adds 826 items only to training after the split, ntrain should be 20,632 + 826 = 21,458, not 21,293 (−165).
  • The 165-image discrepancy exactly mirrors the validation excess, indicating the split is not truly 80/20 as written.
- Required fix: Recompute and report the exact split fractions and augmentation accounting, or restate as “approximately 80/20” with correct counts. Provide a clear recipe: (i) split sizes before augmentation; (ii) number augmented and criterion; (iii) final per-split counts.

P4-E10
- Location: Throughout (e.g., Sec. IV.C, Table I notes, Appendix A–D)
- Problem: Inconsistent terminology for nulls: “isotropic-bootstrap null,” “pixel-permutation null,” “per-pixel random-label permutation,” “per-galaxy label-shuffle,” “binomial per-pixel label-shuffle,” etc. In several places the same construction appears to be referenced by different names, while in other places different constructions are given similar names.
- Required fix: Define each null once in a short glossary (e.g., NPX = pixel-permutation of Ap across in-mask pixels; NGL = per-galaxy label-shuffle within pixels; NDS = depth-stratified label-shuffle; NBIN = binomial-monopole generative), then use those exact labels everywhere. Add a one-line reminder near every σ where the null is invoked.

P4-E11
- Location: Multiple harmonic-channel statements (e.g., Sec. IV.C par. “Angular power spectrum”; Sec. VII.a; Table I rows (iii)–(iv) outside Table III)
- Problem: For non-Gaussian permutation nulls you often report only z without a paired rank-p at the point of first mention (rank-p only appears later in Table III). This invites over-interpretation of z as Gaussian.
- Required fix: Accompany every headline MASTER-channel σ with its rank-p (or explicitly state “rank-p in Table III”), or add a parenthetical “non-Gaussian permutation null; see Table III for rank-p.”

P4-E12
- Location: Sec. IV.C (page 8), sentence comparing the unthresholded-sample 0.57% dipole to the HC-broad A50 ≈ 0.75%
- Problem: Cross-estimator comparison without an immediate, local caveat; A50 cited is for the HC-broad estimator, not the unthresholded estimator used for the 0.57% number (you do later give an A50 ≈ 0.36% for the unthresholded case, but the first comparison is easy to misread).
- Required fix: Add a local clause “note: A50 = 0.75% applies to the HC-broad estimator; the unthresholded estimator has A50 ≈ 0.36% (given below).”

MAJOR

P4-M8
- Location: Sec. II.B (page 3), “after flip augmentation … combined pool is 26,616”
- Problem: The text suggests “flip augmentation of the training split,” yet the net increase is only +826 images relative to 25,790. That is far less than doubling a full training split and therefore implies selective or partial augmentation. The manuscript does not specify the selection rule or target share.
- Required fix: Precisely specify the augmentation policy (e.g., “we augment X% of training images meeting criterion Y”), and provide the exact augmented count and rationale. This is necessary to reproduce training.

P4-M9
- Location: Fig. 9 caption vs. in-panel annotation
- Problem: The caption says the panel uses the canonical observed σ ≈ +7.28, while also noting that the c9b-internal background yields σ = 7.21. It is not fully clear which number is actually plotted/annotated in-panel for the observed point, and whether the plotted completeness curves (per-axis) are scored against the same null used for that observed point.
- Required fix: Clarify in the caption which σ is rendered in the panel and confirm that the completeness curves and the plotted observed point are scored against the same null definition. If not, add a parenthetical “observed point scored against null X; curves against null Y.”

P4-M10
- Location: Sec. IV.C (end of “Simple dipole” para) and Sec. VI.A (Fisher floor vs. injection-recovery)
- Problem: The estimator-specific floors are scattered and partially cross-compared. The reader must track A50/A95 for two different estimators and two different nulls.
- Required fix: Add a short, single table summarizing, side-by-side, for both the HC-broad and unthresholded estimators: N, null type, A50, A95 (with MC errors), and a one-line “do not cross-compare across estimators” reminder.

MINOR

P4-N6
- Location: Sec. II.B (page 3), “80/20 split”
- Problem: Given the concrete counts do not reflect an exact 80/20, label as “approximately 80/20 stratified split” (or state the exact percentages).
- Required fix: Wording tweak plus exact percentages.

P4-N7
- Location: Table IV and surrounding text
- Problem: You use “pp” for “percentage points” without first defining it; some readers may parse it as “percent.”
- Required fix: Define “pp = percentage points” at first use or replace by “percentage points.”

P4-N8
- Location: Sec. IV.C (null-quantile vector: {50,68,90,95,99}% → {3.5,4.4,6.0,6.8,8.4}×10−3)
- Problem: These quantiles are given once in-body; adding the MC half-width on the 95th-quantile (order-statistic CI) would help (distinct from P4-M3 which asks for a general treatment; here, add the number next to the quoted vector).
- Required fix: Append e.g., “A95,nq = (6.8 ± δ)×10−3 with δ computed from NMC = 10,000 order-statistic variance.”

P4-N9
- Location: Appendix A.d (mask declaration and depth-stratification)
- Problem: The same footprint is described as “Nall ≥ 1” and “analysis footprint” in multiple places; a brief parenthetical naming it once (e.g., “Footprint F1”) would reduce cognitive load when cross-reading with Table I.
- Required fix: Introduce a short label for each mask/footprint and use consistently.

NITS

P4-Ni4
- Location: Appendix A (C2 2◦ apodization) vs. main text (sometimes rendered “C 2 2◦”)
- Problem: Inconsistent kerning/spacing for the apodization label “C2”.
- Required fix: Standardize to “C2 2◦ apodization”.

P4-Ni5
- Location: Sec. III.C, Eq. (1)
- Problem: Minor typographic clarity: add explicit “softmax over 3 classes” in the line after the layer list to avoid any ambiguity about where softmax is applied.
- Required fix: Small wording addition.

Explanation
These items were not covered in the initial review. The most critical new issue is the split/augmentation arithmetic inconsistency (P4-E9/P4-M8), which affects training reproducibility. Additional findings focus on terminology standardization for nulls (P4-E10), ensuring rank-p accompanies non-Gaussian σ (P4-E11), eliminating a cross-estimator comparison pitfall (P4-E12), and several clarity/consistency improvements.