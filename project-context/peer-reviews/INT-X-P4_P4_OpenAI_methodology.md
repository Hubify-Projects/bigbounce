# P4 INT-X-P4 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_int.pdf` md5=077eeee9 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6575 chars)
**Wall time**: 440.0s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, …” (24 pages)

Scope of review
I reviewed the full 24-page PDF, including abstract, all sections, equations, figures, and tables. I audited numerical claims and internal consistency of the methodology and statistics. Below I list concrete findings with required fixes and severities.

Findings

P4-E1 (ESSENTIAL)
Section: Appendix A.b + Table III caption; Pages 16–17 and 11
Problem: Inconsistency in NaMaster binning description. Appendix A.b states the ℓ = 1 number is “the single-multipole bin … nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1)” (which creates 192 single-ℓ bins). Table III caption says “Band 1 is the single mode ℓ = 1 decoupled within the full 39-band coupling matrix.” “39-band” is inconsistent with nlb=1.
Required fix: Precisely document the bandpower configuration used for Table III vs. Sec. IV C. If Table III used nlb=5 (or similar) leading to 39 bands, state that explicitly and reconcile with Appendix A.b. If both configurations were used in different places, clearly label each occurrence and ensure the code/config in the repository reproduces exactly those two distinct settings.

P4-E2 (ESSENTIAL)
Section: Data Availability; Page 22
Problem: No frozen, citable archival DOIs. The paper promises a future Zenodo DOI and relies throughout on ephemeral repository paths and a moving GitHub repo. PRD requires reproducibility with stable artifacts at acceptance.
Required fix: Before acceptance, deposit (i) the exact catalog release used in the paper, (ii) the model checkpoints, and (iii) the analysis scripts and configuration files, together with (iv) the committed null arrays used for all quoted σ and p. Mint DOIs (e.g., Zenodo) and replace all ephemeral repository references with DOI links in the body or, preferably, in a dedicated Supplemental Material document referenced from the main text.

P4-E3 (ESSENTIAL)
Section: Data Availability; Page 22
Problem: Broken dataset URL with spaces. The link is printed as “https://huggingface.co/datasets/bamfai/galaxy- chirality- catalog”, which is not a valid URL.
Required fix: Correct the URL to a valid, space-free link (e.g., https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog). Verify that the printed URL resolves.

P4-E4 (ESSENTIAL)
Section: Throughout (multiple); e.g., Pages 5, 7–12, 14–21, 22
Problem: Numerous in-text references to internal file paths and analysis artifacts (e.g., “pipelines/p2_chirality/outputs/...json”), seed values, and audit file names are embedded in the narrative. These are not standard PRD citations and are not citable/stable. They read as internal bookkeeping and version-control notes (pattern 046/047).
Required fix: Move all such artifact references to a structured Supplemental Material or a Reproducibility Appendix, and replace them with concise references to DOIs (see P4‑E2). In the main text, keep only the statistic and the stable pointer (DOI + filename) needed to reproduce it.

P4-E5 (ESSENTIAL)
Section: II.B Training Labels; Page 3
Problem: Augmentation/count arithmetic is unclear and potentially confusing. Text says: 25,790 source images → split 79.4/20.6; post-augmentation pool 26,616; ntrain=21,293, nval=5,323; “the 826-image difference … arises entirely from horizontal-flip augmentation applied to the training split only.” This sounds like only 826 augmented copies were added, not a systematic flip of the training split, which is atypical. The “79.4%” fraction implies 20,467 train pre-augmentation (20,467+5,323=25,790), so +826 yields 21,293, but the choice of 826 rather than flipping all training items is not justified.
Required fix: Provide an explicit, unambiguous table of counts: pre-augmentation train/val split sizes, the exact number of augmented items added, and the augmentation policy (deterministic flip of a subset? sampling probability?). Clarify why only 826 flips were added and demonstrate that this choice does not bias the learned flip-equivariance (e.g., by reporting the learned-model pre‑TTA flip-swap error on the validation set).

P4-E6 (ESSENTIAL)
Section: Data Availability; Page 22
Problem: The parent imaging dataset is identified as “Smith42/galaxies” on HuggingFace in Sec. II.A (Page 2), but the Data Availability section only lists the derived catalog/model/code. There is no stable citation (DOI) to the parent imaging cutouts actually used.
Required fix: Provide a stable citation (DOI or archival link) for the exact parent image dataset version used, or archive a frozen copy under DOI. If only IDs/coordinates are used from Smith42/galaxies and the workflow re-downloads cutouts from DESI Legacy DR8, describe that precisely and cite DR8 directly as the image source of record.

P4-M1 (MAJOR)
Section: VI.A; Pages 13–14
Problem: CE-ResNet pseudo-label inheritance and the “shuffle-null limitation.” The paper acknowledges that 66.5% of training labels derive from CE-ResNet predictions and that pixel/per-galaxy shuffle nulls cannot test independence from inherited large-scale survey-correlated structure. While the harmonic-channel residuals are treated as diagnostics, this still leaves a risk that inherited survey structure could partially cancel a true cosmological dipole in real space in a footprint-correlated manner not covered by the g=2a−1 dilution argument.
Required fix: Provide at least one independent control: retrain a sub-model on the 6,637 GZ1 labels only (no CE-ResNet pseudo-labels), re-infer on the full 8.47M catalog, and report the primary real-space HC dipole (+ null) for that sub-model. If full-catalog re-inference is infeasible, produce this control on a very large, representative sky subset (e.g., >25% of the footprint with matched depth/mask). This is needed to remove a key circularity concern at PRD standards.

P4-M2 (MAJOR)
Section: IV.C “Simple dipole”; Page 7–9
Problem: Primary null uses pixel-permutation of Ap which does not preserve heteroskedastic pixel noise from varying Nspiral(p). Although a label-shuffle null is also reported, the paper still designates the pixel-permutation as the primary.
Required fix: Elevate the per-galaxy label-shuffle null to equal footing in the primary result presentation (main text, not only as a robustness check). Present both z and rank‑p for both nulls side-by-side (with the “not directly comparable” note). This addresses heteroskedasticity explicitly for the headline estimator.

P4-M3 (MAJOR)
Section: Appendix C; Page 19
Problem: Look-elsewhere correction for the hemisphere scan uses NMC=10,000, leading to the resolution floor pLEE ≥ 1/(N+1)≈1.0×10−4. The paper quotes pLEE ≤ 10−4, i.e., at the Monte Carlo floor. While this is a diagnostic only, the quoted tail probability is at the resolution limit.
Required fix: Either (a) increase the number of null realizations for the hemisphere max-statistic to at least 1,000,000 so the quoted pLEE is resolved well below 10−4, or (b) rephrase the result to state explicitly that the p-value is at the Monte Carlo floor and not resolved (and ensure no claims are conditioned on its exact value). Given it is a diagnostic, option (b) is acceptable if stated clearly.

P4-M4 (MAJOR)
Section: Abstract; Page 1
Problem: The abstract is extremely dense and juxtaposes several σ values from distinct null procedures. While caveats are included in places, the abstract still risks reader confusion by rapid-fire quoting of +0.41σ (pixel-permutation), z=0.58 (label-shuffle), +3.64σ, +7.28σ, +7.93σ, etc., despite later notes that they are not comparable.
Required fix: Streamline the abstract so that (i) the primary cosmological conclusions (real-space HC dipole null and WLS template exclusion) are presented first with their own nulls; (ii) harmonic-channel σ values are grouped under a single “diagnostic, not cosmological” sentence with one canonical value, and the others deferred to the body/Supplement. Include an explicit “not directly comparable” disclaimer directly in the sentence where multiple σ from different nulls appear.

P4-M5 (MAJOR)
Section: IV.D; Table IV; Page 11
Problem: The “99.32% reproduction” statement for the monopole+mask pre-MASTER leakage uses “±0.40 pp per-realization null scatter” but the precision on the mean is ~0.018 pp (0.40/√500). Presenting the ±0.40 pp next to a statement about reproducing the mean can be misread as an uncertainty on the mean.
Required fix: State both (i) the per-realization standard deviation (0.40 pp) and (ii) the uncertainty on the mean reproduction fraction (±0.018 pp), and provide a 68% or 95% CI for the reproduction fraction of the mean to avoid ambiguity.

P4-M6 (MAJOR)
Section: VII Conclusions, item c; Page 15
Problem: The text juxtaposes “+3.64σ direct single-mode value” with “+7.93σ (10^4-permutation)” for the canonical unapodized field, then notes they are not two independent detection claims. However, this is a repeated juxtaposition of two σ on the same field with different null-run sizes and slightly different conventions. As presented, it risks overemphasis.
Required fix: Pick one canonical σ (preferably the higher-statistics 10k-permutation value) for the canonical unapodized field in the Conclusions and move the other to the body as a cross-check. Keep the “diagnostic, not cosmological” qualifier immediately adjacent.

P4-M7 (MAJOR)
Section: Throughout; e.g., Figs. 6, 7 captions; Pages 9–10
Problem: Occasional typographical/formatting artifacts in math and units (e.g., “C 2 2 ◦” instead of “C^2, 2°”, “obs.\ = 7.21” in Fig. 9 caption).
Required fix: Clean all math/formatting artifacts and ensure uniform notation: explicitly define C^2 apodization once; remove LaTeX escape remnants; ensure proper degree symbols and superscripts.

P4-M8 (MAJOR)
Section: Abstract claim of scale/novelty; Page 1
Problem: The novelty claim “largest chirality-labeled galaxy catalog to date” is plausible, but the quantitative comparison is only to CE‑ResNet (1.95M). Other large-scale morphology catalog efforts (e.g., Galaxy Zoo DESI predictions, Walmsley et al. 2023) include detailed morphologies for 8.7M galaxies; while not strictly chirality-labeled, this should be acknowledged to avoid an overbroad “largest” claim.
Required fix: Qualify the statement to “largest chirality-labeled spiral catalog we are aware of (3.2M spirals), exceeding the chirality-labeled sample of CE‑ResNet by ≈1.6×,” and distinguish from general morphology catalogs.

P4-M9 (MAJOR)
Section: IV.C; Page 8
Problem: The description of the confidence-threshold sweep is text-only; given the importance of demonstrating that the primary peq>0.6 threshold was not tuned, this needs a clear, consolidated figure/table in the main text.
Required fix: Add a small table/figure panel showing z (and rank‑p) vs. peq∈{0, 0.4, 0.5, 0.6, 0.7, 0.8} for both nulls. This makes the pre-specification and robustness of the threshold evident to readers without combing through prose.

P4-N1 (MINOR)
Section: Appendix A.a; Page 16–17
Problem: Definition of the mean-subtraction support is a bit buried. It is good that Nspiral=0 pixels are excluded from the mean, but the sentence could be clearer.
Required fix: Add one clarifying sentence: “Pixels with Nspiral=0 do not enter either the field support or the mask-mean subtraction; the mean is computed strictly over pixels with Nall≥1 and Nspiral≥1.”

P4-N2 (MINOR)
Section: IV.B; Page 6
Problem: The slab statistics: “per-slab binomial σ = 7.4×10−4” is correct for N≈4.57×10^5, but the narrative mixes equal-count, equal-area, and equal-RA partitions in a long paragraph.
Required fix: Move the detailed slab numbers to Supplemental Material and keep a concise summary sentence in the main text.

P4-N3 (MINOR)
Section: VI.B; Page 13–14; Table V Page 14
Problem: Axis-draw protocol description flips between θ-uniform and area-uniform in different places (though you do acknowledge/compare them).
Required fix: Consolidate to a single declared axis-draw convention for the headline A50/A95 values and move the alternative-convention cross-checks to Supplemental Material.

P4-N4 (MINOR)
Section: VII; Page 15–16; Table VI and Fig. 9
Problem: The harmonic-channel completeness curve and table are helpful but repeat intermediate σ values (e.g., “obs. σ≈7.21” in the figure caption) that differ from the paper-canonical 7.28σ. This is explained, but can still confuse readers.
Required fix: Replace any non-canonical observed σ in captions with the canonical value and keep a short parenthetical “(minor difference due to different background null in this artifact)”.

P4-N5 (MINOR)
Section: References; Pages 23–24
Problem: Citation formatting is mostly fine; check that all arXiv IDs and DOIs are up to date. For Jia et al. (2023), include the exact sample size used for chirality evaluation if you rely on it in comparisons.
Required fix: Minor copyedit.

P4-N6 (NIT)
Section: Throughout
Problem: Occasional duplicated words and hyphenation artifacts due to line breaks (e.g., “monopole-mask leakage that sources the +6.48σ pre-MASTER pseudo-Cℓ (Sec. IV D). The 3.05σ hemisphere signal … is clas￾sified…”), “ˆ zˆ” with repeated carets.
Required fix: Proofread for OCR/linebreak artifacts and LaTeX math escapes; fix duplicated carets and broken words.

P4-N7 (NIT)
Section: Throughout
Problem: A few places repeat nearly identical disclaimers verbatim in back-to-back sentences. While the caveats are important, they add to verbosity.
Required fix: Consolidate caveats where possible; keep one precise, explicit caveat per juxtaposition.

Arithmetic/consistency spot checks (passed)
- Class counts: NCW+NCCW+NNS=8,474,531; Nspiral=3,201,160; fractions quoted are consistent.
- Catalog-C fCW=0.497353 with σbinom≈0.000279; deviation −9.47σ matches Table II.
- Raw Catalog-A fCW=0.507879; deviation ≈+28.7σ matches.
- Real-space dipole amplitude Adip≈4.4×10−3 (0.44%); null quantiles {3.5,4.4,6.0,6.8,8.4}×10−3 consistent.
- MASTER apodized ℓ=1: Cdata=2.348×10−5, ⟨C⟩null=1.71×10−6, σnull=2.99×10−6 => z=7.28 matches.
- Monopole+mask leakage: 1.6961×10−2 vs (1.6846±0.0068)×10−2 gives 99.32% reproduction and z=+1.69.
- Injection‑recovery Table V values are consistent with stated A50≈0.75% and A95∈(1.0%,1.5%]; Fisher floor σ(A)=√(3/N) cross-check matches.

Length and presentation
The manuscript is long (24 pages) for a primarily null result; much of the length is devoted to careful caveats and internal artifact references. I recommend, for clarity and PRD style:
- Main text trimmed to ~15–17 pages by moving internal artifact path references, auxiliary robustness panels, and some diagnostic-channel details to Supplemental Material.
- Keep the primary cosmological estimators and their immediate robustness checks in the main text.

Effect sizes
The paper generally accompanies σ with effect sizes (Adipole in % or Cℓ values). Keep this consistently: whenever a σ appears, include the corresponding amplitude or ratio as done in the main cases.

Abstract-last drift sweep
I re-read the abstract against the body. Most abstract claims are traceable, and caveats about incomparable σ are included. However, because the abstract packs several σ values and null procedures into one paragraph, it still risks misinterpretation (see P4‑M4). Please streamline as requested.

## Summary recommendation
MAJOR REVISIONS

The work is careful and methodologically thoughtful, and the main null conclusion appears statistically sound. However, before PRD acceptance the manuscript must resolve the NaMaster binning inconsistency (P4‑E1), replace ephemeral internal file-path references with stable DOIs and a proper Reproducibility/Supplement (P4‑E2, P4‑E4), correct the broken dataset URL (P4‑E3), clarify the training/augmentation arithmetic (P4‑E5), and provide at least one independent non‑pseudo‑labeled control to address the pseudo‑label inheritance circularity (P4‑M1). Additionally, streamline the abstract presentation of multiple σ values from distinct nulls (P4‑M4) and tidy formatting issues. With these addressed, the paper would meet PRD methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

P4-E7 (ESSENTIAL)
Section: Sec. IV.C footnote 1; Sec. IV.D; Appendix E.b (footnote 5); Pages 9–12, 22
Problem: Contradictory labeling of the canonical “+3.64σ” result as pre‑MASTER vs post‑MASTER.
- Sec. IV.D repeatedly treats +3.64σ as a post‑MASTER, decoupled, canonical‑mask residual (also contrasted with the apodized +7.28σ).
- Appendix E.b explicitly calls a different estimator “monopole‑preserving pre‑MASTER pseudo‑Cℓ” and quotes +4.31σ there (consistent with pre‑MASTER).
- Sec. IV.C footnote 1 states “Catalog‑A pre‑MASTER ℓ=1 … same estimator family as the canonical Catalog‑C +3.64σ result,” implying the +3.64σ is also pre‑MASTER, which conflicts with Sec. IV.D.
Required fix: Unambiguously state, in one place and consistently everywhere, which estimator produced +3.64σ (pre‑ or post‑MASTER; which field normalization; which mask/weight; with/without mean subtraction; null size). Update the conflicting footnote and any text implying it is “the same estimator family” as the pre‑MASTER number if it is in fact a post‑MASTER value.

P4-M10 (MAJOR)
Section: Primary HC real-space dipole; Sec. IV.C vs. Appendix B.d (T7 QC); Pages 7–9, 18
Problem: Two different baseline z values for the same primary estimator appear in the paper: +0.41 (main text, 10k pixel‑perm null) vs. +0.52 (Appendix B.d, “baseline under the c11b 10^4‑permutation convention”) before/after excluding flagged rows. This looks like a stale‑number or null‑calibration mismatch for the headline estimator.
Required fix: Pick one canonical null configuration for the primary HC result, recompute once, and propagate that single z and rank‑p consistently across the paper. If the Appendix uses a different null stream, say so and avoid calling it “baseline.”

P4-M11 (MAJOR)
Section: Hemisphere scan and LEE; Sec. IV.D Table IV vs. Appendix C; Pages 11, 19
Problem: Two different hemisphere‑scan direction grids are used and reported: NSIDEdir=8 (768 dirs; Table IV) and a 10° grid (648 dirs; Appendix C). The reported max statistics and nulls are therefore not directly comparable; the pLEE claim in Sec. VI references only one of these.
Required fix: Standardize on one hemisphere‑scan grid for max‑stat and pLEE reporting, or clearly tag each result by grid and ensure every quoted pLEE/max value is paired with its own grid and null. Provide a canonical (preferred) grid in the main text; move the alternative grid to Supplemental with its own numbers.

P4-M12 (MAJOR)
Section: Appendix A.a; Table III cross‑context; Pages 16–17 and 11
Problem: The paragraph on monopole subtraction (“reduces decoupled C1 from 2.30×10^−5 to 1.51×10^−5 and increases σ from +1.85 to +3.64”) does not specify the exact field/mask/weight convention for those two numbers. Table III then lists different normalizations (Ap vs fCW−0.5) and footprints, warning they are not cross‑comparable.
Required fix: For the “2.30→1.51×10^−5; +1.85→+3.64” statement, explicitly state the precise configuration (footprint, weight Wp, field normalization, mean‑subtraction policy, null size/seed). Add a parenthetical reminding readers that Table III uses different field conventions, hence raw amplitudes there will not match.

P4-M15 (MAJOR)
Section: Abstract; Sec. VII.e (falsification criterion); Pages 1, 15–16
Problem: The falsification criterion includes a sample‑size condition (“≥10^7 galaxies”) that is not derived or justified quantitatively. The stated A50/A95 thresholds are estimator‑ and sample‑specific (HC‑broad N≈9.5×10^5), yet the abstract frames them as general.
Required fix: Either provide a quantitative rationale for the “≥10^7” sample‑size clause (e.g., scaling of σ(A) with N and the DESI‑like footprint geometry) or remove the explicit sample‑size requirement. In both abstract and conclusions, state clearly that A50≈0.75% and A95∈(1.0%,1.5%] apply to the HC‑broad selection and current footprint/null; thresholds scale with N and geometry.

P4-N11 (MINOR)
Section: Sec. IV.C footnote 1; Appendix A.b; Pages 9, 16–17
Problem: NaMaster API names are inconsistently typeset (“from lmax linear” vs from_lmax_linear; missing underscores/spaces). While cosmetic, this can mislead readers trying to replicate.
Required fix: Normalize API names exactly as in pymaster (e.g., nmt.NmtBin.from_lmax_linear). Fix all occurrences.

P4-N12 (MINOR)
Section: Appendix A.a; Page 17
Problem: “Monopole subtraction … reduces decoupled C1 … increases σ …” is given without a reproducibility pointer to the exact DOI’d artifact. In contrast to other places, only generic artifact names are cited.
Required fix: Add the DOI and filename for the exact null array and data vector used to produce those four numbers, matching the reproducibility standard you set elsewhere.

P4-N13 (MINOR)
Section: Table I, row (vi); Page 5
Problem: The “monopole+mask null” row lists “+1.69” without stating explicitly this z refers to the pre‑MASTER pseudo‑Cℓ (not the post‑MASTER decoupled value), which can be misread.
Required fix: Add “(pre‑MASTER pseudo‑Cℓ)” in the row label or a footnote to avoid ambiguity.

P4-N14 (MINOR)
Section: Sec. VI.B.a (Fisher floor); Page 13
Problem: The text notes an O(1), axis‑orientation‑dependent geometric factor on the real footprint but gives no quantitative estimate for DESI‑Legacy‑like masks.
Required fix: Provide a simple numeric factor (e.g., median or range over random axes on the actual footprint) to make the “O(1)” statement concrete.

P4-N15 (MINOR)
Section: Appendix B.e; Page 19
Problem: Cross‑match aperture is written as “1′′” here and “1″” elsewhere. Minor inconsistency.
Required fix: Standardize the arcsecond notation throughout.

P4-N16 (NIT)
Section: Appendix D.g; Page 21
Problem: A visible footnote merge artifact “z ≈ −18.1.34” where “34” is the start of footnotes 3/4, not part of the number.
Required fix: Fix the broken footnote superscripts so the sentence reads “z ≈ −18.1.” with footnote markers properly placed.

Rationale for “fresh eyes”: The main new issues uncovered are (i) a substantive, reproducibility‑relevant inconsistency about whether the canonical +3.64σ is pre‑ or post‑MASTER (P4‑E7), (ii) inconsistent baseline z values for the headline estimator across sections (P4‑M10), and (iii) mixed hemisphere‑scan grids in different sections (P4‑M11). Several smaller clarity items (P4‑M12, P4‑N11–N16) also surfaced when re‑checking figure/body alignment, API names, and footnote rendering. These were not called out in the initial review and should be addressed to meet PRD clarity and reproducibility standards.