# P4 RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_RC.pdf` md5=a53c7966 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4673 chars)
**Wall time**: 362.8s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (24 pp)

Scope of review
I reviewed the entire manuscript, all figures/tables/equations, and audited the numerical claims in the abstract and conclusions against the body. I verified arithmetic, units, and the stated null procedures where possible from the provided numbers. My focus is methodology rigor, significance conventions, estimator declarations, and reproducibility.

Overall: The statistical methodology is unusually explicit and careful about null definitions and non-comparability of σ-values, and most headline numbers in the abstract are traceable to body sections. However, there are several essential issues that must be resolved prior to PRD publication: (i) an inconsistency in the training/augmentation arithmetic that makes the data pipeline unclear; (ii) the Data Availability section contains live-branch language and placeholders (“will be inserted at submission”)—PRD requires immutable, citable artifacts; and (iii) given that 66.5% of training labels are inherited pseudo-labels, an independent validation (trained only on human labels) of the primary null result is needed to exclude survey-inherited structure as a confound for the primary estimator. I also list several major/minor items to improve clarity and eliminate potential confusion between different null procedures.

Findings

ESSENTIAL

P4-E1 (Sec. II.B, p. 3) — Training/augmentation arithmetic inconsistent
Quoted text (paraphrased): “Combined training set 25,790 source images; after flip augmentation of the training split the combined pool is 26,616. Pre-augmentation split 79.4/20.6; ntrain = 21,293 post-augmentation, nval = 5,323 never augmented. The 826-image difference arises entirely from horizontal-flip augmentation applied to the training split only.”
Problem: If the training split contains 25,790 − 5,323 = 20,467 source images, a standard “flip augmentation” that duplicates each training image would produce 20,467 additional images, not 826. The numbers given imply only 826 training images were actually duplicated. As written, the protocol is ambiguous and internally inconsistent with normal augmentation practice and with your own description.
Required fix: Precisely specify the augmentation protocol and counts. State the number of training images before augmentation, the number augmented, and why only 826 were added. If only a subset was augmented, define the selection rule. Provide a small table summarizing train/val counts pre- and post-augmentation and ensure these numbers are self-consistent.

P4-E2 (Data Availability, p. 23) — Placeholders and live-branch reproducibility
Quoted text: “An immutable archival snapshot … will be deposited at journal submission; … inserted here in place of this sentence at submission.” “A persistent archival DOI has not yet been minted; until it is, the versioned release tag above is the citable artifact.” “live main branch.”
Problem: PRD requires immutable, citable artifacts. Placeholders and references to a “live main branch” are not acceptable at acceptance.
Required fix: Before acceptance, provide (i) a DOI (e.g., Zenodo) for an immutable archive containing the exact code, configuration, and committed analysis artifacts used to produce the paper; (ii) commit hashes for the code and model; (iii) DOIs for the catalog/weights (not just HuggingFace URLs). Remove all placeholder language.

P4-E3 (Throughout; e.g., Secs. IV–Appendices; multiple pages) — Excess of internal “artifact” path references in body text
Problem: The manuscript is saturated with repository-internal file paths (e.g., pipelines/p2_chirality/outputs/…json) used as citations for intermediate numbers. While laudable for reproducibility, these are not persistent scholarly references and clutter the main narrative. PRD expects such technical pointers in a Supplement or Data Appendix, backed by a permanent archive/DOI.
Required fix: Move the exhaustive file-path “artifact” references to a single Reproducibility Appendix or to Supplemental Material linked via DOI. In the main text, keep only the quantitative result plus a single stable pointer (DOI + commit hash).

MAJOR

P4-M1 (Appendix E.a, p. 22) — Unsubstantiated “65.7% edge-on receive CW/CCW” claim
Problem: The text states “65.7% of visually identified edge-on systems (b/a<0.3) receive CW or CCW classifications” but no supporting counts, sample size, or cross-match description are provided. Later you note this is “qualitative pending the axis-ratio cross-match,” which contradicts the specific 65.7% number.
Required fix: Either (i) provide the actual cross-match methodology, sample size, and counts (table) supporting 65.7%, or (ii) remove the specific percentage and rephrase as a qualitative expectation, deferring the quantitative statement to future work.

P4-M2 (Sec. IV.D + Table III + Abstract; pp. 11–12, 1) — Two different post-MASTER canonical ℓ=1 σ’s (+3.64 and +7.93) create confusion
Problem: You report a canonical, unapodized, post-MASTER ℓ=1 significance of +3.64σ (500-MC, per-pixel label-shuffle null) and elsewhere +7.93σ (10^4 per-galaxy label-shuffle null). While you do state that these are distinct estimators/nulls, presenting two headline σ-values for the same “channel” is confusing.
Required fix: Choose a single canonical estimator/null for each channel (e.g., per-galaxy shuffle with N=10^4 permutations) and report only that σ in the abstract and conclusions. Relegate the alternative (500-MC/per-pixel shuffle) to an Appendix with a clear explanation of the null differences.

P4-M3 (Sec. IV.D, p. 12) — Post-MASTER monopole-only reproduction “~12%” lacks numbers
Problem: You state that the monopole-only null reproduces “∼12% of the post-MASTER decoupled C1,” but no explicit numbers (C1,data, ⟨C1⟩null, ratio ± error) are given for this specific test.
Required fix: Add the actual numbers for the post-MASTER decoupled C1 monopole-only generative null: data C1, null mean ± standard deviation, and the ratio (with uncertainty). This is a load-bearing diagnostic.

P4-M4 (Sec. VI.A, pp. 13–14) — Pseudo-label dependence: need an independent validation of the primary null
Problem: 66.5% of training labels are inherited from CE-ResNet. While you present thoughtful diagnostics that argue inherited survey structure would bias away from a null rather than hide a signal, the clean solution is to show that the primary real-space HC null result persists when training on truly independent human labels (even at lower accuracy).
Required fix: Provide a companion result where the model is trained solely on human-verified GZ1 labels (no pseudo-labels), inferred over the full catalog, and the primary real-space HC (peq>0.6) dipole estimator is re-run. Report the corresponding z and p. If GPU cycles preclude full re-inference, at minimum demonstrate on a large, representative sky subregion that the null persists; document the subregion selection a priori.

P4-M5 (Sec. IV.C/Table III; pp. 9–11) — Inconsistent canonical numbers across sections for the apodized ℓ=1 null mean/sigma
Problem: Sec. IV.C states for the apodized ℓ=1 case C1,null mean = 1.71×10−6, σ = 2.99×10−6 (+7.28σ), while Table III (10^4 permutations) lists ⟨C1⟩ = 1.93×10−6, σ = 3.12×10−6 (+7.31σ). This likely reflects different null sample sizes and/or conventions, but the reader needs one canonical set.
Required fix: Select and propagate a single canonical set of numbers (mean, σ, z) throughout the paper for each estimator, and explicitly identify in-text whenever a different null or run-size is used. Align the abstract/conclusions with the canonical choice.

P4-M6 (Sec. IV.C, p. 9; Fig. 9 caption, p. 16) — Observed harmonic σ differs between bodies of text and the completeness figure
Problem: The completeness figure’s internal background null yields σ = 7.21 for the observed data, while the body quotes +7.28 (500-MC) and +7.31 (10^4). The caption attempts to explain this, but the multiplicity of numbers is confusing.
Required fix: In the figure and main text, use the same canonical observed σ. If the figure necessarily uses a different background null, add a single sentence in the main text clarifying that the completeness plot internally rescored the observed data under its own null and thus yields σ = X, but the canonical observed σ used throughout is Y.

MINOR

P4-m1 (Abstract, p. 1; Sec. III.A, multiple) — σ-values from different nulls
Comment: The manuscript is commendably careful to state that σ-values from different null procedures are not directly comparable. Ensure this caveat is present at every juxtaposition. I did not find a blatant omission, but please re-scan especially the abstract and figure captions once you consolidate canonical numbers (P4-M2/M5).

P4-m2 (Sec. VI.B, p. 14–15; Table V) — Axis-draw convention for injection
Comment: You report both θ-uniform and area-uniform axis-draw checks and state that results are consistent. This is good; to avoid any ambiguity, add the numerical A50/A95 from the area-uniform sweep to the main text (not only as a parenthetical), or show a small comparison table.

P4-m3 (Appendix D.g, p. 21; Table X) — WLS template fit: present the dipole amplitude also in percent of fCW for clarity
Comment: You give Adipole = 4.55×10−3 in Ap units; also state the equivalent in fCW units (0.2275%), so readers can compare directly to the 1.7% reference.

P4-m4 (Appendix D.h, p. 21; Table XI) — Mask equivalence audit
Comment: Good practice. Please also state explicitly whether any galaxies lie outside the Nall≥1 footprint, and if so, how many (should be 0 for the DESI Legacy footprint as defined).

P4-m5 (Appendix B.d, p. 19) — Flip-identity QC: 2.9% out-of-range recovered flip probabilities
Comment: You mitigate this with a QC flag and demonstrate null persistence after exclusion. Consider regenerating and republishing the released Parquet with internally consistent “raw-eq” columns so users don’t encounter out-of-range values, or state prominently in Data Availability that these columns are not to be used probabilistically and must be filtered by the QC flag.

P4-m6 (Various) — Formatting of “C2 2◦”
Comment: Normalize the apodization notation to “C2, 2° apodization” everywhere.

P4-m7 (Appendix E.b, p. 22) — “+4.31σ monopole-preserving” mention
Comment: Provide the corresponding data and null mean/σ values in a short parenthesis for completeness, analogous to other channels.

NIT

P4-n1 (Typos/consistency) — Minor spacing and hyphenation issues (e.g., mixed “MASTER”/“NaMaster”, occasional extra spaces around symbols). A final copy-edit pass should fix these.

P4-n2 (Length) — The manuscript is long for the claimed contribution. Consider moving most artifact-path mentions and extended numeric audits to a Supplement and aiming for ≤18 pages main text.

Numerical audits performed (spot checks)

- Class fractions (Sec. IV.A, p. 5): NCW/Ntot = 1,592,107/8,474,531 ≈ 0.18787 (18.787%); NCCW/Ntot ≈ 0.18987 (18.987%); NS/Ntot ≈ 0.62226 (62.226%). Spiral fraction 3,201,160/8,474,531 ≈ 0.37774 (37.774%). All consistent.

- Global CW fraction among spirals (Table II, p. 7): fCW = 1,592,107/3,201,160 ≈ 0.497353; binomial σ ≈ 0.5/√N ≈ 0.000279; deviation (f−0.5)/σ ≈ −9.49σ (tabulated −9.47). Consistent.

- Catalog A/B deviations (Table II): 0.507879−0.5 = 0.007879; divide by σ ≈ 0.000274 gives ≈ +28.75σ (tabulated +28.72). 0.50400 likewise ≈ +14.6σ. Consistent.

- Pre-MASTER leakage test (Table IV, p. 12): Data 1.6961×10−2 vs null mean (1.6846±0.0068)×10−2 → reproduction 1.6846/1.6961 ≈ 0.9932 (99.32%); z = (1.6961−1.6846)/0.0068 ≈ 1.69σ. Consistent.

- MASTER apodized ℓ=1 (Table III): z = (24.74−1.93)/3.12 ≈ 7.31; rank p = 6/10001 = 6.0×10−4. Consistent.

- WLS bootstrap exclusion (Appendix D.g): Aref = 1.7% in fCW units equals 0.034 in Ap units. Abest = 0.00455; Δ = 0.02945; σboot = 0.00163 → z = −18.1. Consistent.

- Fisher floor (Eq. 4, p. 14): σ(A) = √(3/N). For N=3.20116×10^6, σ ≈ 9.68×10^−4 (0.097% full amplitude). For N=949,584, σ ≈ 1.78×10^−3. Consistent.

- GZ1 spiral-chirality accuracy (Table IX, p. 19): Accuracy among GZ1 spirals classified CW/CCW: (39,011+42,928)/(39,011+18,889+16,377+42,928) = 81,939/117,205 ≈ 0.699. Matches 69.91%.

Effect sizes: The primary real-space amplitude Adip = 4.4×10−3 (Ap units, i.e., 0.22% in fCW) is reported; completeness/falsification thresholds are quantified (A50 ~ 0.75%; A95 ~ 1.0–1.5%). Good.

Abstract-last drift sweep
I re-checked the abstract line-by-line:

- Catalog size, Nspiral, and release: consistent with Sec. IV.A and Data Availability (except for missing DOI; see P4-E2).

- Primary real-space null (+0.41σ; p=0.31; robustness): consistent with Sec. IV.C (peq>0.6). The qualification about different nulls for the 0.41 vs 0.58 values is present.

- WLS bootstrap exclusion at z≈−18: consistent with Appendix D.g.

- Monopole-leakage 99.32% pre-MASTER, MASTER residuals +3.64σ and +7.28σ: numbers appear in Sec. IV.D/Table III, but see P4-M2 on consolidating a single canonical σ-value for the canonical mask.

- Falsification criterion A95 ∈ (1.0%, 1.5%], A50 ≈ 0.75%, and the non-interchangeability of harmonic completeness: consistent with Sec. VI.B and VII/Table VI.

The abstract’s claims match the body once the canonical σ-values are unified and the DOI placeholder is resolved.

Bibliography
Spot checks of key references (Shamir 2012/2020/2022; Jia et al. 2023; NaMaster) are consistent in year/journal/arXiv identifiers.

## Summary recommendation
MAJOR REVISIONS

The paper is strong on statistical care and transparency, and most headline results are internally consistent. However, before PRD publication the authors must (i) fix the training/augmentation inconsistency (P4-E1), (ii) provide immutable, citable artifacts and remove placeholders (P4-E2–E3), and (iii) supply an independent validation of the primary null using only human labels (P4-M4), or an equally strong quantitative bound excluding pseudo-label inheritance as a confound for the primary estimator. Additionally, unify canonical σ-values per channel and streamline the presentation of different nulls. After these corrections and clarifications, the manuscript would meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

P4-E4 (Abstract; Sec. IV.C, pp. 1, 8–9) — “Null robust across a full confidence-cut sweep” is misleading/incorrect
Issue: The abstract states the high-confidence primary result is “robust across a full confidence-cut sweep, peq ∈ {0, 0.4, 0.5, 0.6, 0.7, 0.8},” implying null consistency across the sweep. But the body explicitly reports strong non-null values at lower cuts: z = +4.3, +4.1, +4.0 for peq = 0, 0.4, 0.5, with the null collapsing only at ≥0.6. As written, “robust across a full sweep” contradicts the presented numbers.
Required fix: Rephrase to state clearly that the null is robust across the high-confidence regime (peq ≥ 0.6) and that the low-confidence tail (peq < 0.6) shows significant excess attributed to systematics. Avoid language suggesting null robustness “across the full sweep.”

MAJOR

P4-M7 (Appendix D.d, p. 20) — “~25% leg-induced ℓ=1 partial closure” lacks quantitative backing
Issue: You claim the summed imaging-leg proxy fields account for ~25% of the observed canonical-mask ℓ=1 amplitude, but you don’t show the numbers used to reach 25% (e.g., measured C1,data; proxy-induced contribution with uncertainties).
Required fix: Provide the explicit ℓ=1 amplitudes (and uncertainties) for (i) the Ap field, (ii) each leg-proxy cross-term, and (iii) their summed projection onto ℓ=1, along with the ratio and uncertainty that produce “~25%.” A short table suffices.

P4-M8 (Appendix D.e vs Table III; pp. 20–21, 10–11) — Density-stratified null uses a different field/normalization without stating it
Issue: The density-stratified null paragraph quotes C1,null = 3.44×10−6, σ = 3.07×10−6 (z = +3.80) for the “canonical” estimator, but Table III’s canonical rows have null means ~0.57×10−6 with different σ. The text does not state that this density-stratified test uses a different field convention/normalization than Table III, creating unit/confusion risk.
Required fix: Explicitly state the field/weight/monopole-subtraction convention used for the density-stratified null and reconcile its units with Table III (or add a parenthetical noting that this paragraph uses a different normalization than Table III). If possible, report the density-stratified result in the same convention as the canonical Table III block for direct comparability.

P4-M9 (Sec. VII.c, p. 16; Table III) — “Same canonical unapodized field” wording is inaccurate
Issue: You write “the 10^4-permutation recompute of the same canonical unapodized field … gives z = +7.93σ,” but earlier you stress that these rows use different field/weight/monopole-subtraction conventions and that z should not be compared across them. Calling it “the same field” is misleading.
Required fix: Replace “same canonical unapodized field” with precise language (e.g., “the canonical unapodized configuration under its own committed field convention,” or similar) and point to the field differences (Ap vs fCW−0.5; subtraction/weights) to prevent readers from assuming identity.

MINOR

P4-m8 (Sec. IV.C, p. 9) — Missing “not directly comparable” qualifier in a juxtaposition
Issue: You juxtapose the raw Catalog A 2.31σ real-space dipole with a +6.48σ pre-MASTER pseudo-Cℓ artifact without explicitly repeating that the σ’s come from different null procedures/estimators. Elsewhere you are careful; here it’s easy for readers to misread.
Required fix: Add the standard qualifier (“distinct null procedures; not directly comparable”) at this juxtaposition as you do in other places.

P4-m9 (Formatting; Fig. 9 caption; Sec. VII/Table VI) — Inconsistent “10^3” typesetting
Issue: The number of injections is sometimes written as “103” (no caret). While readable in context, PRD typesetting should be consistent (“10^3”).
Required fix: Normalize “10^3” formatting where it appears (e.g., Fig. 9 caption, Table VI notes, nearby text).

P4-m10 (Appendix A.c, p. 17) — Clarify σ-change statement context
Issue: You note that monopole subtraction reduces C1 (2.30×10−5 → 1.51×10−5) but increases σ from +1.85 to +3.64 “(the canonical-mask number).” It’s not obvious to a reader that these two σ’s refer to the same canonical unapodized single-ℓ MASTER setting and not to a different mask/weight. 
Required fix: Add a parenthetical explicitly confirming that both σ values are computed under the same canonical unapodized single-ℓ MASTER configuration (and same null), or clarify if conventions differ.

NIT

P4-n3 (Typographic consistency) — Occasional stray diacritics/markers
Issue: Occasional stray diacritics (e.g., “ŷ, ẑ” rendered as “ˆ y, ˆ zˆ”) appear in a few places. 
Fix: Clean up vector accents and ensure consistent math markup.