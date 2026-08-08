# P4 EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6656 chars)
**Wall time**: 480.4s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Journal: Physical Review D (methods/statistics rigor).
- Focus: statistical-method validity, estimator declaration, internal numerical consistency, error propagation, consistency of σ/p conventions, and reproducibility.

Overall assessment
The manuscript presents a very large chirality-labeled galaxy catalog and a careful null test for a dipole in spiral handedness. The analysis includes multiple estimators and an unusually detailed systematics audit. However, there are several essential issues that must be addressed before the paper can meet PRD methodology standards: an internal contradiction in the hemisphere look-elsewhere assessment, presence of revision-history language in the body, ambiguous use of “bootstrap” vs permutation nulls, and insufficient quantification of Monte Carlo uncertainty on quoted significances built from small NMC. The text is also burdened with internal pipeline path references that should be moved to Supplementary Material and the data/code release requires a frozen DOI.

Findings

ESSENTIAL

P4-E1 — Section III.B (Declared Analysis Hierarchy), page 4; Appendix C (Hemisphere asymmetry), page 19
Problem: Contradictory look-elsewhere result for hemisphere max-asymmetry.
- Main text (Sec. III.B, bullet (v)) states: “hemisphere maximum-asymmetry (3.05σ local maximum against the label-shuffle null, < 1σ after look-elsewhere correction; Appendix C).”
- Appendix C(c) states: “The direct-MC look-elsewhere test (N = 10,000 random-label shuffles of the maximum statistic) gives pLEE ≤ 10−4 (rejection of the random-label null) … the principled look-elsewhere control.”
These statements are mutually inconsistent. pLEE ≤ 10−4 corresponds to a >3.7σ Gaussian-equivalent, not <1σ.
Required fix: Resolve and correct the look-elsewhere statement consistently across the paper. If the principled direct-MC max-statistic null yields pLEE ≤ 10−4, remove the “< 1σ” claim and report the correct post-LEE p (and its Gaussian-equivalent), together with the explicit null definition. If instead the intended result is <1σ after LEE, provide the correct MC-derived pLEE and reconcile the contradiction in Appendix C. Do not mix a Bonferroni heuristic with the direct-MC result; choose and defend a single, principled LEE correction (the direct-MC max-statistic is the natural choice).

P4-E2 — Appendix D(g), page 20; Appendix E(d), page 21
Problem: Revision-history and round-tracking language in the body.
- Examples: “post-R29,” “An earlier version of this paragraph overstated the stability … has now been recomputed.”
PRD requires a clean, standalone manuscript without internal version history commentary.
Required fix: Remove all revision-history phrases (“post-Rxx,” “earlier version,” “now recomputed,” “retained for continuity,” “superseded”) from the body text. Present only the final, verified analysis with necessary methodological details. If you wish to document changes, do so in a non-public change log, not in the article.

P4-E3 — Data Availability, page 22
Problem: Reproducibility artifacts not frozen; no minted archival DOI; reliance on mutable commit and dataset tags.
- The text promises a future Zenodo DOI, but none is provided; many results depend on external artifacts.
Required fix: Before acceptance, deposit the exact analysis artifacts (catalog snapshot, code, configuration, masks, and MC outputs sufficient to reproduce all tables/figures) to a permanent repository with a citable DOI (Zenodo/OSF). Replace mutable URLs/commit hashes and “will be deposited” language with the actual DOI(s). Provide a concise “Reproducibility Checklist” enumerating what is needed to regenerate each figure/table/number.

MAJOR

P4-M1 — Throughout (e.g., Sec. IV.D p.10; Table III p.11; Figure 8 p.10)
Problem: Quoted significances from small Monte Carlo ensembles lack Monte Carlo uncertainty; some results use only NMC = 200–500 realizations while quoting multi-decimal z.
- Example: canonical-mask MASTER single-mode result reported as +3.64σ against a 500-draw null (pMC = 0.030). With NMC = 500, the sampling error on mean/s.d. of the null is non-negligible, and “3.64” should carry an MC error bar or be recomputed with larger NMC.
Required fix: For every result derived from MC-null moments or ranks, either (a) increase NMC to ≥10,000 for the quoted channel, or (b) report z and p with appropriate MC uncertainties (e.g., via jackknife/bootstrapping the null ensemble or by analytic variance of σnull estimates). As a minimum, recompute the canonical-mask single-mode result with 10^4 permutations to match the apodized-block and tabulate both, including rank-p and moment-z with MC error.

P4-M2 — Terminology: “isotropic-bootstrap null” vs “pixel-permutation null,” multiple sections (Abstract; Sec. III.A/B; Sec. IV.C)
Problem: The paper uses “isotropic-bootstrap null” for a procedure that (from the description) is a permutation/randomization (“Ap randomly permuted across in-mask pixels”). “Bootstrap” typically denotes resampling with replacement; you also employ a “block-bootstrap” elsewhere, leading to nomenclature ambiguity.
Required fix: Standardize terminology. If the null is a permutation/randomization (reshuffling per-pixel Ap), call it “pixel-permutation null” or “randomization null.” Reserve “bootstrap” exclusively for the spatial block bootstrap in Appendix D. Update all occurrences in the abstract, text, figures, and tables.

P4-M3 — Estimator pre-declaration, Sec. III.B (p.4)
Problem: The text claims the estimator hierarchy “was declared in early versions … predates the provenance audit,” but provides no immutable record. For PRD, the paper must stand alone; unverifiable pre-registration claims should not be used to support primacy.
Required fix: Remove unverifiable language about prior declarations, or provide an immutable, time-stamped record (e.g., DOI to a pre-registration note) contemporaneous with that declaration. Otherwise, simply state that the primary estimator for this paper is the real-space dipole on the HC subsample and all other channels are diagnostics.

P4-M4 — Overuse of internal pipeline path references in the main text (numerous, e.g., pp. 3, 5–13, 15–21)
Problem: The body is littered with internal file paths such as “pipelines/p2_chirality/outputs/…json” that interrupt readability and are not stable citations.
Required fix: Move all low-level artifact-path references to a single Supplementary “Artifact Index” or to the archived repository’s README, and cite that DOI/section once. In the main text, keep only brief parenthetical references (e.g., “see Supplementary Artifact A3”).

P4-M5 — Abstract and Sec. VII: exclusion language relative to Shamir amplitudes (pages 1, 14–15)
Problem: Statements like “disfavors a clean 1.7% dipole at z ≈ −18” and “Shamir ∼3% amplitude class is excluded by a factor of ∼6–12 under the present pipeline” risk being overinterpreted as likelihood-level exclusions despite the authors’ own caveats about non-matched estimators and footprints.
Required fix: Soften to “we find no evidence for a dipole, and our pipeline would have detected a clean 1.7–3% dipole with overwhelming significance; however, a formal exclusion of prior claims would require a matched-footprint, matched-estimator reanalysis.” Ensure the abstract and conclusions carry this explicit caveat.

P4-M6 — MC completeness curves and harmonic-channel claims, Sec. VII(a) (pp. 14–15)
Problem: The axis-dependent median z ranges (“≈68–218,” “≈209–685”) are reported without tabulated underlying numbers in the paper (only an artifact pointer). For PRD, effect sizes underlying strong completeness claims should be documented in the manuscript or Supplementary.
Required fix: Add a small table (or Supplement) listing, for each injected amplitude and axis, the median and interquartile range of recovered z, and the P(≥3σ) with binomial SE. Keep the pointer to archived artifacts as secondary.

P4-M7 — Table II (Global CW fraction, Catalog B row), page 5
Problem: The “Dev. (σ) = +14.6” cannot be independently verified from the rounded 0.504 ± 0.0003 shown.
Required fix: Provide enough significant figures for the calibrated fCW (e.g., 0.5039xx) to reproduce the quoted σ, or report the σ computed from the printed central value and printed uncertainty.

P4-M8 — Reporting precision vs NMC, multiple places
Problem: Several z values are quoted to two decimal places from nulls with NMC = 200–500 (e.g., per-ℓ significances in Fig. 8 caption from a 200-MC battery).
Required fix: Reduce the number of significant figures or increase NMC, and report the MC uncertainty (see P4-M1).

MINOR

P4-m1 — Consistency of “not directly comparable” caveat when juxtaposing σ from different nulls
The paper is generally careful; ensure every juxtaposition (e.g., Table I rows, Sec. IV.C juxtaposing +0.41σ vs +7.28σ) explicitly repeats that they are from different nulls and not comparable. A few instances rely on context rather than an immediate qualifier.
Required fix: Add the explicit caveat at each juxtaposition point where it is missing or ambiguous.

P4-m2 — Terminology: “isotropic” null vs actual operation (Sec. IV.C, p.7)
Permuting Ap across in-mask pixels preserves the one-point distribution and mask geometry, but is not “isotropic” in the sense of drawing from a known isotropic sky distribution. Consider renaming to “pixel-permutation null on the mask” to avoid implying rotationally invariant sampling.

P4-m3 — Style/typography
- Ensure consistent capitalization of CW/CCW across text and tables.
- Clarify C2 2° apodization notation; typeset cleanly (avoid “C 2 2 ◦” artifacts).
- Ensure all figures have axis labels and units in the PDF (not checkable here; please verify).

P4-m4 — Effect size reporting
You are generally good about reporting amplitudes; continue to pair every σ with the associated fractional amplitude (as you do for Adip). Add an explicit quantitative effect-size sentence near each major σ headline.

NIT

P4-n1 — Minor typos and hyphenation artifacts occur (e.g., “equivari￾ant,” “decon￾volution”) due to PDF line-breaking. Clean final typeset.

P4-n2 — The title is long and contains multiple clauses. Consider a crisper title appropriate for PRD.

Length
The manuscript is dense (23 pages) for a methods null result. Much of the internal artifact path material can be moved to Supplementary to reduce length by ~3–4 pages without loss of scientific content. The core narrative (data, estimators, main results, the key leakage demonstration, and the WLS block-bootstrap) should remain.

Checks of numerical consistency (spot-audits)
- Catalog counts and fractions (Sec. IV.A): NCW=1,592,107; NCCW=1,609,053; NNS=5,273,371 sum to 8,474,531. fCW = 1,592,107/3,201,160 = 0.497353; σbin ≈ 2.795×10−4; Dev ≈ −9.49σ (reported −9.47σ). OK.
- Tier A cw fraction 0.507879 with Nspiral=3,321,795: σ ≈ 2.74×10−4; Dev ≈ +28.8σ (reported +28.72). OK within rounding.
- Real-space dipole amplitude: Adip = 4.4×10−3 = 0.44%. Below injection A50 ≈ 0.75%. OK.
- Null-quantile A95,nq = 6.8×10−3 = 0.68% > Aobs; OK.
- MASTER apodized ℓ=1: (2.348×10−5 −1.71×10−6)/2.99×10−6 ≈ 7.28σ; rank-p = 6/(10001) ≈ 6×10−4. OK.
- Monopole+mask leakage (Table IV): (1.6961−1.6846)/0.0068 ≈ 1.69σ. OK.
- Fisher floor (Eq. 4): σ(A)=√(3/N)=9.69×10−4; 3σ ≈ 0.29%. OK.
- GZ1 confusion-derived chirality accuracy: (39,011+42,928)/(39,011+18,889+16,377+42,928) = 81,939/117,205 ≈ 69.91%. OK.

Bibliography
Spot-checked key citations (Shamir 2012/2020/2022; Jia et al. 2023 CE-ResNet; NaMaster 2019; MASTER 2002) — metadata appear correct. Ensure that any “largest to date” claim is maintained as “to our knowledge” (already done) and that the CE-ResNet sample size context is correctly described.

Standalone-reader test
The paper is largely self-contained. However, heavy reliance on internal artifact path references (without a stable DOI) hinders standalone reproducibility. Addressed by P4-E3/P4-M4.

## Summary recommendation
MAJOR REVISIONS

The study is ambitious and, with the corrections above, could set a solid methodological benchmark for chirality dipole searches. However, the current manuscript contains an essential internal contradiction (hemisphere look-elsewhere), revision-history language inappropriate for a final PRD submission, ambiguous “bootstrap” terminology for permutation nulls, and insufficient Monte Carlo precision/uncertainty reporting for several quoted σ values. A frozen, DOI-based reproducibility package is also required. Addressing these points will materially improve clarity, rigor, and reproducibility to meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (NEW ONLY)

ESSENTIAL

P4-E4 — Training/validation split and augmentation arithmetic inconsistent (Sec. II.B p.3; App. B.a p.17)
- The text says: source images = 25,790; “after flip augmentation of the training split the combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323); the 826-image difference … arises entirely from horizontal-flip augmentation applied to the training split only — the validation split … is never augmented.”
- Arithmetic and protocol do not match:
  • If you first 80/20 split the 25,790 sources (≈20,632 train, 5,158 val) and then augment the training split, the final pool size should be 20,632 + Naug + 5,158. With Naug = 826 (your stated delta), the training size should be 21,458, not 21,293, and validation should remain 5,158, not 5,323.
  • Instead, 26,616 × 0.2 = 5,323 implies the 80/20 split was performed after augmentation, contradicting “augmentation applied to the training split only.”
  • App. B.a also calls the validation “un-augmented held-out random 80/20 split (nval = 5,323 of 26,616),” which again implies the split used the post-augmentation pool, making it unclear how augmented samples were kept out of validation.
Required fix: Provide an unambiguous, step-by-step description with counts before/after each operation (split first vs augment first), and confirm there is no leakage of augmented variants into validation. Reconcile ntrain/nval with the stated Naug, or correct the numbers.

P4-E5 — Inconsistent ℓ = 1 C1 values and configuration across sections (Sec. IV.C p.9; App. A.c p.16; Table III p.11)
- Sec. IV.C (apodized footprint, Wp = Nall, monopole-subtracted) reports Cmeas1 = 2.348×10−5 with ⟨C1⟩null = 1.71×10−6, σnull = 2.99×10−6 (z = +7.28).
- Table III (same footprint and field convention) lists Cdata
b = 24.74×10−6 (= 2.474×10−5), ⟨Cb⟩null = 1.93×10−6, σnull = 3.12×10−6 (z = +7.31).
- App. A.c states that “monopole subtraction reduces decoupled C1 at ℓ = 1 from 2.30×10−5 to 1.51×10−5 and increases z to +3.64 (the canonical-mask number),” mixing canonical-mask and apodized-footprint contexts and quoting a post-subtraction value (1.51×10−5) that does not match either 2.348×10−5 or 2.474×10−5 for the apodized case.
Required fix: For each estimator/footprint/weight/field convention, give a single canonical C1 value (with its null moments) and keep it consistent across the paper. If the “single-mode-only” vs “39-band matrix” decoupling explains a numerical difference, quantify that expected difference and justify it; otherwise, recompute so the same data vector yields the same C1 everywhere.

MAJOR

P4-M9 — Dual “canonical ℓ = 1” significances presented as coequal (+3.64σ vs +7.93σ) (Sec. IV.D p.10–12; Table III p.11; Sec. VII.c p.15)
- The paper alternates between z = +3.64 (500-MC direct single-mode canonical run) and z = +7.93 (10^4-permutation canonical row in Table III) for the canonical unapodized channel, with both values highlighted in the narrative.
Required fix: Choose one canonical result (preferably the higher-statistics 10^4-permutation value) as the single quoted number in the body; move the 500-MC value to Supplementary as a historical cross-check to avoid ambiguity.

P4-M10 — Figure 8 caption vs body context can confuse pre- vs post-MASTER status (Fig. 8 p.10; Sec. IV.D p.10–12)
- Fig. 8 is labeled “Pseudo-Cℓ … on the canonical mask,” i.e., pre-MASTER, and its embedded z-values (e.g., +3.63 at ℓ = 1) match that context. In nearby text the “post-MASTER canonical-mask residual is +3.64σ,” reusing a very similar number for a different estimator, which invites misreading.
Required fix: Explicitly state in the Fig. 8 caption that the plotted bars are pre-MASTER pseudo-Cℓ and that the post-MASTER canonical residual quoted in text is a different estimator. Consider adding a small panel or line in the caption with the post-MASTER ℓ = 1 number for direct comparison, labeled clearly.

P4-M11 — “Single-mode-only” vs “single-ℓ within full 39-band matrix” decoupling ambiguity (Sec. IV.C p.9; Table III p.11; App. A.b–c p.16)
- The manuscript implies these two decoupling routes yield different C1 for the same field, yet in exact linear algebra with a single-ℓ bin they should be equivalent up to numerical precision if configurations are otherwise identical.
Required fix: Clarify algorithmic differences (field normalization, mask/apodization, weights, monopole treatment) and demonstrate, with a controlled test, that both pipelines recover consistent C1 when configurations match. If not, justify the expected magnitude of discrepancy.

MINOR

P4-m5 — Rounding/consistency: σℓ=1 reported as +3.63 (Fig. 8 caption) vs +3.64 elsewhere
- This is small but contributes to confusion when different canonical numbers are already in play. Standardize to a single rounded value for that specific estimator.

P4-m6 — Equation (4) presentation (Sec. VI.A p.13)
- The identity σ(A) = √(3/N) = 2√3 σ(fCW) assumes p = 1/2 for the global CW fraction and equates a Fisher-forecast variance for a dipole amplitude with the binomial variance of a global fraction. Add a brief derivation or a footnote explicitly stating the assumptions; otherwise the second equality looks ad hoc.

P4-m7 — Typesetting artifact in App. D(g) (p.20)
- “z ≈ −18.1.23” appears where “z ≈ −18.1” with footnote markers “2,3” is intended. Fix to avoid misreading.

P4-m8 — Abstract clarity on injection sample
- The abstract cites “A50 ≈ 0.75%” and “A95 between 1.0% and 1.5%” without specifying that these refer to the real-space HC-broad (peq > 0.6) subsample. Add “on the HC-broad subsample” to prevent misinterpretation as full-sample limits.

P4-m9 — Small stale-number drift across runs (Sec. IV.C p.9 vs Table III p.11)
- For the apodized ℓ = 1 channel, Cmeas1 differs by ≈5% (2.348×10−5 vs 2.474×10−5) between sections. Even if scientifically immaterial, please harmonize the presented central value to a single one derived from your preferred run.

NIT

P4-n3 — Minor formatting
- Clean up “C 2 2 ◦” apodization notation consistently, and ensure axis labels/units are visible in all figures in the final PDF.

Explanation
I focused on fresh classes A–J you requested. The largest new issues are (i) the inconsistent training/validation split-and-augmentation arithmetic/protocol, which affects reproducibility of the classifier, and (ii) inconsistent ℓ = 1 amplitudes and estimator configurations reported across sections, which can confuse readers about what was actually measured. Addressing these, along with unifying the canonical ℓ = 1 significance and tightening captions vs body text, will materially improve rigor and clarity.