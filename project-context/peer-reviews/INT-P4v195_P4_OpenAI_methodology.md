# P4 INT-P4v195 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_v195.pdf` md5=87d3eb2c pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7896 chars)
**Wall time**: 521.4s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (24 pp)

Scope of review
- Focus: methodology/statistics rigor, estimator declaration, null procedures, internal arithmetic consistency, dimensional/units checks, claims vs evidence, and reproducibility surfaces as per PRD standards.
- I read the full 24-page manuscript (figures, tables, appendices) and recalculated each load‑bearing scalar where possible from the numbers in the paper.

Overall assessment
- Strengths: The analysis hierarchy is explicitly pre‑declared; real‑space dipole is clearly the primary cosmological estimator; the paper consistently distinguishes among null procedures (pixel‑permutation, label‑shuffle, monopole‑generative) and avoids mixing σ’s from different nulls; amplitudes are traced back to pixelized HEALPix fields with explicit masks/weights; internal arithmetic checks out across the catalog totals, fractions, binomial errors, and most quoted z values. The “monopole+mask leakage” demonstration is careful and numerically consistent. The injection‑recovery floors are operationally defined with the scorer and axis protocol documented.
- Main block to acceptance: reproducibility pointers remain unfrozen. The Data Availability section promises a frozen DOI/commit at submission and points to a live “main” branch today, and the text contains numerous path‑level artifact pointers that are not yet mapped to a fixed, citable release. PRD requires an immutable record at acceptance.

Findings (ESSENTIAL, MAJOR, MINOR, NIT)

P4-E1 (ESSENTIAL) — Data Availability and frozen reproducibility pointer
- Location: Data Availability (page 23), plus many inline artifact pointers throughout (e.g., pp. 3–22).
- Issue: The manuscript repeatedly references internal artifact paths (e.g., pipelines/p2_chirality/outputs/…) and a live main-branch repository, and states: “An immutable archival snapshot … with a frozen release tag and a Zenodo DOI will be deposited at journal submission; that tagged commit and DOI will be the single citable reproducibility handle … inserted here in place of this sentence at submission.”
- Required fix:
  - Replace the forward-looking placeholder sentence with the minted DOI(s) and a pinned commit hash or release tag for the exact code and artifact bundle used to generate the paper’s figures/tables.
  - Provide a single landing page (README/manifest) in that release that maps each in-text artifact ID (e.g., “artifact c9b”, file paths) to an accessible file within the release.
  - Ensure the released catalog (HuggingFace) also has a versioned DOI or that the exact version tag v2026.04 is mirrored to a DOI (e.g., Zenodo-integration of the release).
  - PRD standard: at acceptance, all reproducibility assets must be immutable and citable.

P4-E2 (ESSENTIAL) — Units/notation ambiguity for amplitudes quoted “in Ap units” as percents
- Location: Sec. V.A (page 12), multiple other occurrences where percent is used with Ap.
- Issue: The manuscript sometimes expresses Ap amplitudes as “percent” (e.g., “0.32% (in Ap units)”), which is ambiguous because Ap is dimensionless and the paper elsewhere uses both Ap and fCW units with a factor-of-two conversion. This can confuse readers about whether “0.32%” means Ap = 0.0032 or fCW deviation = 0.0016.
- Required fix:
  - For every amplitude given as a percent, explicitly give both numbers and the unit: e.g., “Ap = 0.0032 (0.32%), which corresponds to fCW − 1/2 = 0.0016 (0.16%).”
  - Add a one-line reminder at first use in the abstract and again in Sec. IV.C: “Ap = 2(fCW − 1/2); Ap is dimensionless; we sometimes express it as a percent of unity.”

P4-E3 (ESSENTIAL) — Abstract juxtaposition of σ values from different nulls must carry explicit caveat inline
- Location: Abstract (page 1), paragraph listing “+3.64σ … +7.28σ …”
- Issue: You do add a “Note: the σ values quoted … arise from distinct null procedures … not directly comparable” later in the abstract, but the first juxtaposition of +3.64σ and +7.28σ appears before the explicit caveat. The PRD instruction requires a “not comparable” qualifier at every juxtaposition to prevent misinterpretation.
- Required fix:
  - Insert “(distinct nulls; not directly comparable)” immediately after the first paired listing of “+3.64σ … +7.28σ …” in the abstract, not only later in the paragraph.

P4-E4 (ESSENTIAL) — Small-NMC moment‑z reported with high precision; report rank‑p or uncertainty
- Location: Sec. IV.D and Appendix D (pages 10–12, 20–22), canonical-mask post‑MASTER residual “+3.64σ” based on 500 MC.
- Issue: With NMC=500, the sampling error on the null mean/variance propagates non‑negligibly into z. You do provide a rank pMC=0.030 for the direct run elsewhere, but not every place that quotes +3.64σ also gives the corresponding rank p or an uncertainty on z.
- Required fix:
  - Wherever you quote the 500‑MC “+3.64σ” value, append “(rank pMC=0.030; finite‑MC)” or provide the finite‑MC uncertainty on z (e.g., via bootstrap of the null moments) to prevent overinterpretation of a high-precision σ from a small null sample.

P4-M1 (MAJOR) — Consolidate path-level artifact pointers into a Reproducibility Appendix or manifest
- Location: Throughout (many pages).
- Issue: The main text is cluttered with literal file paths and internal artifact IDs. While commendably transparent, this is not typical PRD style and makes the narrative hard to follow.
- Required fix:
  - Move path‑level details to a single Reproducibility Appendix (or refer to a manifest in the archived release), and in the main text retain short identifiers (e.g., “artifact c9b”) with a pointer to the manifest.

P4-M2 (MAJOR) — Independence from CE-ResNet pseudo‑labels: add a minimal confirmatory check
- Location: Sec. VI.A (page 13).
- Issue: 66.5% of training labels originate from CE‑ResNet. You explain the limitation and provide surrogate diagnostics (template regressions, cross‑spectra). However, a minimal direct independence check (even on a representative sky patch) would bolster confidence.
- Required fix:
  - Add a supplementary analysis on a representative sky region using a model trained only on the 6,637 human‑verified GZ1 labels (or a k‑fold variant thereof), re‑classify that region, and re‑compute the primary real‑space dipole estimator. Report the resulting Adip and null significance. It need not be full‑sky, but should demonstrate that the primary null does not hinge on CE‑ResNet pseudo‑labels.

P4-M3 (MAJOR) — Injection axis convention: standardize to area‑uniform as primary
- Location: Sec. VI.B (pages 13–14).
- Issue: The injection sweep uses θ‑uniform axes (not area‑uniform), and then presents an area‑uniform spot check. While you argue they agree within MC error, PRD readers will expect area‑uniform as the default.
- Required fix:
  - Recompute the A50/A95 sweep with area‑uniform axes as the primary curve (retain the θ‑uniform run as a cross‑check), or explicitly re‑state the area‑uniform recomputation results in the main text (not only as an aside), including the exact A50/A95 numbers.

P4-M4 (MAJOR) — Clarify the “0.32%” WLS amplitude (units and where it comes from)
- Location: Sec. V.A (page 12).
- Issue: The text states “maximum WLS template amplitude … 0.32% (in Ap units) …” but the global joint WLS fit in Appendix D reports Abest,dipole = 4.55×10−3 in Ap (0.455%). The “regional equal‑area” context is not sufficiently explained and the unit phrasing is ambiguous (see P4‑E2).
- Required fix:
  - Specify the exact estimator/region and provide both Ap and fCW amplitudes for the “0.32%” figure, and reconcile it with the 0.455% global Abest reported in Appendix D so the reader can see both are consistent but refer to different selections.

P4-M5 (MAJOR) — Hemisphere scan methodology description
- Location: Appendix C (page 19–20).
- Issue: You use a 10° grid (648 directions) for the maximum‑hemisphere statistic. The resolution choice and robustness to grid refinement are not justified here.
- Required fix:
  - State the tested coarser/finer grid checks (e.g., 5° grid or HEALPix NSIDEdir sweeps) or briefly justify why 10° suffices (e.g., convergence of the max statistic), and confirm that pLEE is stable under reasonable grid refinements.

P4-m1 (MINOR) — Abstract length/density
- Location: Abstract (page 1).
- Issue: The abstract is unusually long and dense for PRD, with multiple null conventions and caveats embedded.
- Required fix:
  - Condense to the primary finding (HC real‑space dipole null; amplitude floors; diagnostic harmonic residual and its attribution). Move secondary caveats to the body.

P4-m2 (MINOR) — Typographical/notation nits
- Locations:
  - Fig. 9 caption and elsewhere: stray diacritics in “x, ˆ y, ˆ zˆ”.
  - Sec. IV.C (page 9): “Wp = Nall +6.9σ” reads awkwardly; use “(z = +6.9σ with Wp = Nall)”.
  - Consistent spacing in “C2 2◦ apodization” vs “C 2 2◦”.
- Required fix: Clean up these minor typesetting issues.

P4-m3 (MINOR) — Edge‑on contamination number needs provenance
- Location: Appendix E (page 22).
- Issue: “65.7% of b/a < 0.3 objects receive CW/CCW” is stated without a pointer to a measured cross‑match; the paragraph later says the b/a cross‑match is pending.
- Required fix:
  - Either add the artifact/analysis pointer for this 65.7% figure or explicitly label it as an illustrative pilot estimate (and remove the significant digits).

P4-m4 (MINOR) — Clarify “Gaussian‑equivalent” z usage
- Location: Abstract (page 1), Sec. IV.D (pages 10–12).
- Issue: You translate pMC=0.030 to “≈1.9σ Gaussian‑equivalent” while also quoting moment‑z=+3.64 from the same 500‑MC run. This is correct but could confuse.
- Required fix:
  - When both are presented together, add a parenthetical “(moment‑z vs. null moments; Gaussian‑equivalent z from rank‑p)” at first appearance and once in the main text.

P4-n1 (NIT) — Page count guidance
- The paper’s length (24 pages) is acceptable for PRD given the methodological content and reproducibility detail. If shortening is desired, consider moving the long path‑level artifact references and some of Appendix‑level diagnostics to Supplementary Material without removing any load‑bearing steps.

Arithmetic and consistency spot-checks (passed)
- Catalog counts/percentages (Sec. IV.A, Fig. 3): NCW=1,592,107; NCCW=1,609,053; NNS=5,273,371; Ntotal=8,474,531; spiral fraction 37.774% — consistent within rounding.
- Table II binomial σ and z: reproduced 0.000274 (A) and 0.000279 (C); Dev −9.47 for C — consistent.
- Fisher floor (Eq. 4): σ(A)=√(3/N)=9.7×10−4 for N=3.201M; 3σ≈0.29% — consistent.
- MASTER apodized ℓ=1: z=(2.348×10−5−1.71×10−6)/2.99×10−6≈7.28 — consistent.
- Monopole‑only leakage: 1.6846/1.6961=0.9932 (99.32%); residual z≈1.69 — consistent.
- WLS block‑bootstrap exclusion: (0.00455−0.034)/0.00163≈−18.1 — consistent.
- GZ1 cross‑match chirality accuracy: (39,011+42,928)/(57,900+59,305)=0.6996≈69.9% — consistent.

Repository-pin/reproducibility-pointer concerns
- Yes, concerns remain at this stage: the manuscript points to a live “main” branch and promises that a frozen tag/DOI will be inserted at submission. For PRD acceptance, this must be resolved (P4‑E1). Once a pinned release/DOI and a manifest mapping all artifact references are provided, this concern is addressed.

## Summary recommendation
MINOR REVISIONS

The methodological core is sound: estimator hierarchy is pre‑declared; null procedures are consistently distinguished; internal arithmetic is correct; and conclusions are appropriately conservative. The main blocker is reproducibility: replace the forward‑looking text with a minted DOI and a pinned, citable release (and consolidate the many artifact pointers). Clarify amplitude units wherever percents are used with Ap, and make small presentation fixes noted above. With these addressed, the paper meets PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (beyond the initial review)

P4-E5 (ESSENTIAL) — Canonical post-MASTER σ inconsistency: +3.64σ (500-MC) vs +7.93σ (10k-MC)
- Location: Abstract (page 1), Sec. IV.D (pp. 10–12), Table III, Conclusions (page 16).
- Issue: For the same “canonical, unapodized” field, two very different moment-z values are quoted: +3.64σ (500-MC “direct” run) and +7.93σ (10k-permutation run in Table III). The paper attributes differences variously to null-run size and estimator conventions, but for the canonical unapodized case the Table III caption explicitly matches the field and weight conventions (“fCW−0.5 = Ap/2 field, Nspiral-weighted subtraction”). Since z is invariant under constant field rescaling, a factor ≈ 2× discrepancy is unlikely to be explained solely by finite-MC noise.
- Required fix:
  - Reproduce both computations side-by-side in a single table with the exact estimator configuration for each (field definition, monopole-subtraction formula, mask, weight, binning/decoupling settings, and random seed). Confirm they are indeed measuring the same estimator. If they are the same estimator, explain the origin of the large difference; if they are not, rename one of them to avoid “canonical” ambiguity, and designate a single canonical σ (preferably the higher-statistics 10k-MC value) for all subsequent references.

P4-M6 (MAJOR) — Block-bootstrap super-pixel construction (440 NSIDE=8 blocks) is under-specified
- Location: Appendix D.g (pages 20–21, footnote 3) and Table X context.
- Issue: The block bootstrap is pivotal to the “z ≈ −18” exclusion, yet the procedure for constructing the 440 NSIDE=8 super-pixel blocks is not fully defined. The canonical NSIDE=64 mask has fsky ≈ 0.490; 440/768 ≈ 0.573 suggests the super-pixel set is defined by an “any subpixel in-mask” rule, expanding the geometric support. This needs to be explicit to ensure the resampling does not introduce off-mask structure.
- Required fix:
  - Precisely specify the rule for selecting “in-mask” NSIDE=8 blocks (e.g., “a block is in if any of its 64 NSIDE=64 subpixels is in the canonical mask”). Archive and cite the exact list of NSIDE=8 indices used (a small text file in the frozen release).
  - State the random seed and resampling protocol (with/without replacement) and confirm that only the NSIDE=64 in-mask pixels contained in the sampled blocks are used in each bootstrap draw (no leakage).
  - Since you already provide NSIDE sensitivity, add the effective fsky of the NSIDE=8 block union in Table VII or Appendix D.g for clarity.

P4-M7 (MAJOR) — Harmonic-channel completeness uses only 3 fixed axes
- Location: Conclusions a (page 15) and Fig. 9 caption.
- Issue: The MASTER ℓ=1 completeness curve is “axis-averaged” only over {x, y, z}. This under-samples axis dependence and is not directly comparable to the real-space injection’s random-axis sampling.
- Required fix:
  - Recompute harmonic-channel completeness with area-uniform random axes (e.g., ≥100 axes) and report the axis-averaged P(≥3σ) curve and spread. Retain the 3-axis curves as a visualization if desired, but treat the many-axis average as primary.

P4-M8 (MAJOR) — CE-ResNet comparison metric mismatch; report apples-to-apples ratio
- Location: Sec. V.B (page 13).
- Issue: CE-ResNet is quoted by the cw/ccw ratio (0.998), whereas Catalog C is quoted by the CW fraction fCW = 0.4974. This is potentially confusing.
- Required fix:
  - Also report Catalog C’s cw/ccw ratio and uncertainty (cw/ccw = 0.9896 ± δ, from binomial propagation), or convert CE-ResNet’s result to fCW for side-by-side comparison. Clarify the metric alignment in the text.

P4-M9 (MAJOR) — Parent dataset pinning
- Location: Data description Sec. II.A (page 2) and Data Availability (page 23).
- Issue: The parent image set “Smith42/galaxies” on HuggingFace is referenced without a version DOI or SHA/pinned snapshot. Your catalog release is versioned, but the upstream cutouts source must also be immutable for full reproducibility.
- Required fix:
  - Pin the exact dataset revision of Smith42/galaxies (commit hash/release tag) and archive a DOI (e.g., via Zenodo/HF integration) in the frozen manifest. If you mirror the subset actually used (DR8 ids + image hashes), link that index in the release.

P4-m5 (MINOR) — Make the NSIDE=8 block coverage explicit
- Location: Appendix D.g (pages 20–21).
- Issue: The text mentions “440 super-pixels” but not the corresponding effective coverage; the reader must infer the selection rule (see P4‑M6).
- Required fix:
  - Add a one-line parenthetical: “440 of 768 NSIDE=8 pixels (f ≈ 0.573) contain at least one in-mask NSIDE=64 pixel; we use this block list for bootstrapping while always restricting to the canonical NSIDE=64 in-mask pixels.”

P4-m6 (MINOR) — Clarify field normalization around Appendix A.c’s C1 amplitudes
- Location: Appendix A.c (page 17) vs. Table III (page 11).
- Issue: Appendix A.c gives C1 = 2.30×10−5 → 1.51×10−5 after monopole subtraction, while Table III’s canonical-unapodized C1 is 7.27×10−6. This is consistent with the half-scaled fCW−0.5 = Ap/2 convention noted in Table III, but the reader must transpose conventions mentally.
- Required fix:
  - Add a parenthetical in Appendix A.c: “(these numbers are in Ap units; the canonical-unapodized Table III rows use the half-scaled fCW−0.5 = Ap/2 field, hence ≈ half the amplitudes).”

P4-m7 (MINOR) — Quantify the “∼12%” post-MASTER monopole-only reproduction
- Location: Sec. IV.D (page 11–12).
- Issue: You state “monopole-only reproduces ∼12% of post-MASTER C1” but only quote σ values. Providing the ratio (⟨C1⟩null/C1,data) would mirror the 99.32% pre-MASTER presentation.
- Required fix:
  - Add the explicit amplitude numbers and ratio for the post-MASTER case, e.g., “⟨C1⟩null = …, C1,data = …, ratio = … ≈ 12%.”

P4-m8 (MINOR) — Label null types unambiguously in tables
- Location: Table I (page 5).
- Issue: The shorthand “pp-shuffle” is ambiguous (could be ‘pixel-permutation’ or ‘per‑pixel’). You elsewhere use “per‑galaxy label‑shuffle.”
- Required fix:
  - Standardize to “per‑galaxy label‑shuffle” and “pixel‑permutation” throughout tables/figures.

P4-m9 (MINOR) — Roundoff consistency in Table III canonical z
- Location: Table III (page 11), “canonical, unapodized, ℓ=1” row.
- Issue: Using the displayed rounded values (7.27, 0.57, 0.84) gives z ≈ 7.98, while the table lists +7.93. This is likely rounding from higher-precision numbers.
- Required fix:
  - Either add one more significant digit to Cb and σnull or include a footnote that z is computed from full-precision values (archived in the artifact), so small discrepancies from rounded display values are expected.

P4-m10 (MINOR) — Report cw/ccw ratio uncertainty
- Location: Sec. IV.A/B and V.B (pages 5–6, 13).
- Issue: You frequently discuss the global CW fraction and compare to other works that use cw/ccw. Reporting the cw/ccw ratio with uncertainty would help readers translate between conventions.
- Required fix:
  - Add cw/ccw = 1,592,107 / 1,609,053 = 0.9896 ± 0.0011 (example value; compute precisely with binomial error propagation or delta method) alongside fCW.

Why these were missed previously
- The initial review focused on estimator hierarchy, null-procedure separation, and reproducibility pinning, and spot-checked representative numbers. A second, line-by-line cross-audit of estimator configurations uncovered the large σ discrepancy for the canonical post-MASTER case (P4‑E5) and the under-specified block-bootstrap super-pixel construction (P4‑M6). The completeness-axis sampling limitation (P4‑M7) became apparent only after comparing how axis-averaging was handled across real-space vs harmonic channels. Minor normalizations and display-precision issues (P4‑m6–m9) surfaced during a stricter pass aligning appendix numbers to table conventions and re-evaluating displayed z from rounded entries.