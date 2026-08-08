# P4 DP4-E2E-RETEST-v1.0.238 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/chirality_catalog_paper.pdf` md5=03f03e2a pages=35
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7385 chars)
**Wall time**: 324.5s

---

Referee report on “A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning”

Scope of this review
I evaluated methodology rigor, statistical validity, dimensional and arithmetic consistency, significance reporting, estimator pre-declaration, and reproducibility claims. I audited the abstract and conclusions scalars against the body and checked figures/tables for consistency.

Overall assessment
The paper makes a careful case that a real-space chirality dipole is consistent with null when labels are produced with a flip-equivariant model and a high-confidence cut, and it relegates harmonic-channel excesses to diagnostics. The estimator hierarchy and repeated caveats about non-comparable σ values are appreciated. However, there are several essential methodological and reproducibility issues that must be corrected before PRD publication, plus a number of major and minor points.

Findings

ESSENTIAL

P4-E1 (Sec. IV A, p. 8; Data Availability, p. 33–34)
Problem: Inconsistent percentages for the “flip-identity QC” flagged rows. The text states: “A catalog-wide QC pass flags 59,515 HC rows (2.9% of catalog rows; 1.6% on the single CW channel) …” With NCatalog = 8,474,531 and NHC = 949,584, 59,515 corresponds to 0.70% of all rows, 6.27% of the HC subsample, and 3.74% of the CW-channel count (59,515/1,592,107). None of these equal the quoted 2.9% or 1.6%. The same inconsistency reappears in Data Availability.
Required fix: Correct the denominators and percentages everywhere this figure appears. Explicitly state whether percentages are relative to the full catalog, the HC subsample, or per-class counts. Provide a single, consistent set of numbers and recomputed percentages.

P4-E2 (Throughout; e.g., Sec. III A & IV C–D; Tables II, V; multiple pages)
Problem: Ambiguous null nomenclature and abbreviation collision. The paper uses “pixel-permutation null,” “per-pixel label-shuffle,” “per-galaxy label-shuffle,” and “pp-shuffle” seemingly interchangeably. In some places “pp-shuffle” appears to mean per-galaxy label shuffling within pixels; elsewhere it appears to mean pixel-permutation. This risks misinterpretation of the primary z and p values.
Required fix: Add a concise glossary defining every null exactly once (e.g., “pixel-permutation” = permute Ap across in-mask pixels; “per-galaxy label-shuffle” = shuffle CW/CCW labels preserving Nspiral(p); “depth-stratified shuffle” = shuffle within Nall deciles; “monopole-only generative” = binomial draws with pglobal). Replace every “pp-shuffle” by the unambiguous name. Ensure Table captions and the text use the same names.

P4-E3 (Sec. IV D, pp. 14–16)
Problem: Mapping the ℓ = 1 harmonic residual to a real-space “amplitude” of |a1| = 6.95 × 10−3 (Ap = 0.695%) and then comparing it to the real-space A50/A95 thresholds is asserted but not derived in the text. Cℓ values are given (Table V), but the exact definition of the quoted |a1| (masked projection? least-squares on Y1m? normalization?) and its equality of units to the real-space Ap dipole amplitude is not shown. Without this, the critical claim “the ℓ = 1 residual lies below A50” is not verifiable from the manuscript alone.
Required fix: Provide the explicit definition used for |a1| (equation), the normalization (spherical harmonics convention), whether the masked sky is used and how, and the numerical calculation leading to |a1| = 6.95 × 10−3 on the same field used for the real-space A estimator. Include either a short derivation or a table with the Y1m-projection coefficients, so that the amplitude-vs-threshold comparison is auditable.

P4-E4 (Data Availability, p. 33–34)
Problem: Reproducibility artifacts are not frozen. The paper promises a future Zenodo DOI and a “release tag” but provides neither a minted DOI nor immutable commit hashes for all load-bearing artifacts at submission. PRD requires a stable archival snapshot for acceptance.
Required fix: Prior to publication, deposit an immutable archival snapshot containing: (i) the catalog tier C (and A/B if included), (ii) all analysis scripts needed to reproduce the reported numbers and figures, (iii) the specific NaMaster configuration files and masks, (iv) the injection–recovery run scripts and outputs, and (v) the WLS/block-bootstrap artifacts. Provide minted DOIs and the exact git commit(s) in the manuscript. Remove all “will be deposited” language and replace with fixed identifiers.

P4-E5 (Sec. IV D, p. 12–13; Table VI caption; Sec. III A)
Problem: Confusing juxtaposition of σ and empirical p for the same estimator. E.g., “+3.64σ (pMC = 0.030)” can be read as inconsistent. While the text elsewhere explains “moment-z vs empirical rank p,” the first occurrences should be explicit and uniform to avoid misinterpretation.
Required fix: For every place where both a moment-based z and an empirical rank-p are given for the same quantity, label them as “moment-z” and “empirical rank p (one-sided)” and add a parenthetical note “not Gaussian z→p.” Do this at first mention in Sec. IV D and in any table/figure captions where both appear.

MAJOR

P4-M1 (Length and redundancy; whole manuscript)
Problem: The manuscript is considerably longer than necessary for the methodological claims, with repeated paragraphs (e.g., duplicated “Independence cross-check … same clean null … z = −0.54σ” statements in Sec. II B, p. 3), extensive pathnames embedded throughout the text, and verbose caveats repeated multiple times. This hinders readability.
Required fix: Condense to ≤ 22 pages (text and figures, excluding appendices), removing duplicated prose, moving long pathnames and internal artifact pointers to a concise Data/Code Availability appendix, and keeping only the minimal estimator hierarchy, primary results, and the core diagnostics needed to justify the systematics attribution.

P4-M2 (Significance reporting consistency; multiple sections and tables)
Problem: Some significance entries still mix null procedures without a uniform pattern of presentation. For example, Table V shows both z and rank-p but not for every band in both footprints; the text alternates between “+7.28σ” (500-MC) and “+7.31σ with p = 6.0 × 10−4” (10^4 permutations) without a single canonical primary diagnostic and its companion p for that footprint.
Required fix: For each harmonic diagnostic footprint, choose a single canonical null run (e.g., the 10^4-permutation run) and report both z_mom and empirical rank-p for ℓ = 1 once in the body and in the table, clearly noting that this channel is diagnostic only. Retain other runs in an appendix as cross-checks.

P4-M3 (Primary estimator pre-registration clarity; Sec. IV C, p. 10–11)
Problem: The pre-registration claim relies on a git commit hash in text. PRD readers cannot easily verify. Also, the justification for the 0.6 cut is valid but scattered.
Required fix: Move the pre-registration proof to a short, self-contained paragraph: cite the public repo URL, the immutable commit hash, the exact file path and line exhibiting the cut, and a timestamp. Present the confidence-cut sweep once in a compact panel with consistent nulls and spell out that the 0.6 threshold excludes the depth-dominated tail.

P4-M4 (Harmonic-to-real-space effect-size linkage; Sec. VII, p. 22–23; Fig. 9)
Problem: The harmonic-channel completeness curve is presented for ℓ = 1 MASTER, and later the observed +7.28σ is used to argue incompatibility with a 1.7% real dipole. This is reasonable but the mapping between an injected real-space Ap dipole amplitude and the measured ℓ = 1 C1 (under mask and weights) is not explicitly summarized in the main text (only implied by injections).
Required fix: Add one sentence (with a pointer to the injection artifacts) stating the empirical transfer function between a pure Ap dipole and the recovered C1 (or z) on the analysis footprint, so the reader understands the end-to-end normalization without inferring it from the figure.

P4-M5 (Training-label provenance clarity; Sec. II B, p. 2–3; Table XI)
Problem: The augmentation protocol is unusual (only 826 augmented instances added). While arithmetically consistent (21,293 − 20,467 = 826), the rationale is not stated and could confuse readers expecting full flip augmentation.
Required fix: Add a one-line clarification explaining why horizontal-flip augmentation was applied to a subset only (or confirm that it was applied adaptively and quantify the selection rule), and confirm that the equivariant TTA at inference supersedes any augmentation asymmetry.

P4-M6 (Terminology and symbol hygiene; multiple sections)
Problem: The manuscript jumps between “HC-broad,” “HC-0.6,” “science cut,” and “high-confidence subsample” without a definitive symbol or short-hand definition block; the same for masks (“canonical mask,” “Nall ≥ 1 footprint,” “binary,” “apodized”).
Required fix: Add a short “Notation and Conventions” box listing: (i) HC-0.6 (peq > 0.6), HC-0.8, etc.; (ii) canonical mask (Nspiral ≥ 10, fsky = 0.49005), footprint mask (Nall ≥ 1, fsky = 0.494), and whether apodization is applied; (iii) unit conventions (Ap vs fCW). Use these consistently.

MINOR

P4-m1 (Sec. II B, p. 3)
Problem: Duplicated “Independence cross-check” paragraph with the same N = 4.60 × 10^4 and z = −0.54σ language appears twice in close succession.
Required fix: Remove the duplicate or merge into a single, crisp statement.

P4-m2 (Appendix B, Table XII, p. 27)
Problem: Test numbering skips T5; T7 is labeled “Calibration proxy,” but criteria are described in prose rather than in the table; T6 criterion reports “< 0.4%” without explicitly stating “difference in CW fraction between hemispheres.”
Required fix: Renumber tests coherently, specify the measured quantity for T6 in the table caption, and add the explicit numeric threshold used for T7.

P4-m3 (Appendix A, Table X, p. 25)
Problem: fsky vs feff_sky definitions are correct but the text interchanges “fsky” and “effective sky fraction” colloquially in one place.
Required fix: Replace every “fsky” used for weighted/apodized masks by “feff_sky,” retaining “fsky” only for binary masks.

P4-m4 (Sec. VI B, p. 19–21)
Problem: The edge-on dilution calculation is correct, but “8.98%” is given without the intermediate number. A reader may benefit from the explicit calculation (1 − δ)−1/2 − 1 with δ = 0.158.
Required fix: Add the one-line numeric computation (e.g., (1 − 0.158)−1/2 − 1 = 0.0897).

P4-m5 (Sec. IV B, p. 8–9)
Problem: The slab statistics narrative is long. A compact table of min/max slab deviations and corresponding z would serve better.
Required fix: Replace the prose with a small 2-row table (RA slabs, Dec slabs): min/max fCW deviation (%) and max |z|.

P4-m6 (References)
Problem: Ensure all references’ metadata (journal/volume/pages/DOIs) are verified; spot checks appear correct, but some recent preprints may have final DOIs.
Required fix: Verify and add DOIs where available (e.g., Jia et al. 2023 DOI already given; double-check others).

NIT

P4-n1 (Style; multiple)
Problem: Frequent in-text absolute file paths and artifact names break reading flow.
Required fix: Move long pathnames to a short “Reproducibility artifacts” appendix and keep the main text readable.

P4-n2 (Terminology)
Problem: Occasional typos (e.g., “demonopole-subtracted”), hyphenation inconsistencies.
Required fix: Proofread for minor typos/hyphenation.

P4-n3 (AI methodology note, p. 34)
Problem: The vendor/model names are not necessary for PRD and may age poorly.
Required fix: Condense to a neutral statement that LLM-based assistants were used for code and internal checks under the author’s supervision, with all quantitative results verified against committed artifacts.

Abstract-last drift sweep (pattern-045)
- “We measure the large-scale chirality dipole of spiral galaxies and find it consistent with null.” Backed by Sec. IV C: z = +0.41 (rank-p 0.31) under pixel-permutation and consistent under label-shuffle nulls. OK.
- “8,474,531 DESI Legacy DR8 galaxies … yielding Nspiral = 3,201,160 spirals.” Matches Sec. IV A.
- “primary estimator — real-space dipole fit … (peq > 0.6, N ≈ 9.5 × 10^5) — gives +0.41σ … p = 0.31.” Matches Sec. IV C.
- “robust across confidence-cut sweep and under per-galaxy label-shuffle.” Numbers given in Sec. IV C. OK.
- “block-bootstrap WLS template fit disfavors a clean Aref = 0.017 dipole at z ≈ −7.6.” Matches Table XV and Appendix D; caveat “not a calibrated frequentist exclusion” appears later in abstract – OK.
- “ℓ = 1 observable is parity-even …” Covered in Sec. VI C. OK.
- “Injection–recovery brackets A95 in (1.0%, 1.5%] (A50 ≈ 0.75%).” Matches Sec. VI B, Table VIII. OK.
- “MASTER pseudo-Cℓ … not an independent cosmological null … residuals … attributed via an eight-anchor battery … ~47% open item lies below A95 … does not affect primary null.” The “below A50/A95” claim depends on the undocumented |a1| = 6.95 × 10−3 mapping (P4-E3). Needs fix as above.
- “Significances from distinct null procedures are not directly comparable.” Consistently said. OK.

Stand-alone reader test
The manuscript is self-contained with respect to methodology (no reliance on a companion paper). However, reproducibility currently lacks immutable artifacts (P4-E4).

Effect sizes
Effect sizes (amplitudes in Ap or fCW deviation) are given alongside σ in most primary statements. Good.

## Summary recommendation
MAJOR REVISIONS

Justification
Methodologically, the work is careful in estimator hierarchy and significance handling. However, there are essential inconsistencies (flip-identity QC percentages), ambiguous null nomenclature that can mislead, and a critical missing derivation tying the ℓ = 1 residual “amplitude” to the real-space A50/A95 thresholds used to argue sub-threshold. Reproducibility artifacts are not yet frozen with DOIs/commits. These must be corrected for PRD standards. After addressing the essential and major points (and trimming length), the paper would be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

Note: I do not repeat any items already listed in my initial review. Only new issues found in the second pass are included below, using the same coding schema.

ESSENTIAL

P4-E6 (Table II, row “apod. MASTER (diag.)”; Sec. A.a, A.d; Table X)
Problem: Nmap weighted is reported as 8,474,531 for the apodized-footprint MASTER row, identical to the total number of catalog galaxies. In NaMaster, the “mask/weight” map is the weight map; C2 apodization multiplies that weight map. Therefore, the sum of weights over the analysis footprint should decrease after apodization unless you explicitly define Nmap weighted as the pre-apodization sum. The manuscript does not state which convention is used, and presenting 8,474,531 for an apodized run is misleading.
Required fix: Explicitly define Nmap weighted for each footprint/weight choice as either “sum of Wp before apodization” or “sum after apodization,” and report the correct value for the apodized run. If the pre-apodized sum is intentionally shown, label it as such in Table II and in the caption.

P4-E7 (Sec. VI B, “image-level end-to-end mirror-flip injection” paragraph)
Problem: Logical inconsistency in parity-antisymmetry statement. The text claims “the production Z2-equivariant TTA labeling is exactly parity-antisymmetric at the image level: Teq = 0.9997 with maximum antisymmetry deviation 0.0.” “Exactly parity-antisymmetric” contradicts Teq ≠ 1.0000, and “maximum deviation 0.0” contradicts Teq = 0.9997.
Required fix: Correct the wording and numbers. If Teq = 0.9997, then it is not “exactly” and the maximum deviation from 1.0 is 0.0003 (or whatever the measured maximum is). Provide both the mean (Teq) and the maximum deviation consistently.

P4-E8 (Sec. IV B, last paragraph before “Implications for ℓ = 0 parity searches”)
Problem: Broken cross-reference. The sentence ends with “(Sec. E, Data Availability).” There is no “Sec. E, Data Availability.” Appendix E is “Morphology Systematics,” and “Data Availability” is a separate unnumbered section.
Required fix: Replace the incorrect reference with the correct target (likely just “Data Availability”) and remove “Sec. E.”

P4-E9 (Data Availability, p. 33–34; vs. Sec. IV C main result)
Problem: Baseline HC real-space dipole significance is inconsistent across the paper. The headline HC result is z = +0.41 (isotropic pixel-permutation null). In the flag-exclusion rerun note, the “baseline” cited is +0.52 (c11b 10^4-permutation convention), and the rerun is +0.48. Using a different null and a different “baseline” next to the primary headline result is confusing and risks being read as a silent update of the main number.
Required fix: When discussing the QC flag exclusion, restate the primary baseline (z = +0.41 under the isotropic pixel-permutation null) and then report the rerun under the same null procedure. If you also want to show the 10^4-permutation variant, label it clearly as such and do not call it the “baseline.”

MAJOR

P4-M7 (Appendix D, item g; “extended 24-template fit”)
Problem: The text claims that adding 15 leg × confidence-bin interaction templates yields an “essentially unchanged” dipole posterior, but no numbers are reported and no table/figure shows the 24-template coefficients or updated Adipole and σboot.
Required fix: Provide the corresponding Adipole and σ for the 24-template fit (at minimum), and state whether the bootstrap exclusion z vs Aref changes. A small one-line table or an added row in Table XV would suffice.

P4-M8 (Sec. VII, Fig. 9; harmonic-to-real-space linkage presentation)
Problem: While Fig. 9 and Table IX document the ℓ = 1 MASTER completeness, the main text never states an explicit empirical transfer function from an injected pure Ap dipole to C1 (or z) on the analysis footprint. The body instead requires the reader to infer this from the plot.
Required fix: Add a one-sentence summary (with an artifact pointer) giving the median recovered C1 or z per unit injected Ap for the apodized footprint (e.g., “on this footprint, an injected pure Ap dipole of 1% yields median z ≈ … in the ℓ = 1 channel”), so the normalization is explicit.

MINOR

P4-m7 (Appendix D, block-bootstrap super-pixel counts; internal consistency)
Problem: Two different NSIDE = 4 in-mask super-pixel counts are stated: “∼ 110” (general discussion) and “∼ 127” (cross-scale check). One of these is stale.
Required fix: Recompute and use a single, correct NSIDE = 4 in-mask super-pixel count consistently in both places (and likewise ensure the NSIDE = 8 “∼ 439” vs “440” inconsistency is resolved).

P4-m8 (Table II header/footnotes; clarity)
Problem: The meaning of Nmap weighted is ambiguous across different mask/apodization conventions (see P4-E6). This can confuse readers about what is actually summed when apodization is applied.
Required fix: Augment the table caption with a precise definition for Nmap weighted per row, clarifying whether apodization is included or not in the sum.

P4-m9 (Appendix D, anchor table and main-text references)
Problem: The anchor table (Table VII) lists “quality-quartile stratification: all 4 quartiles |σ| < 1,” while Appendix C reports a +3.29σ in the [0.5, 0.6) confidence bin (a different binning). Readers may find the contrast puzzling without an explicit reminder that quartiles and fixed-threshold bins differ.
Required fix: Add a short parenthetical in Appendix C clarifying that the [0.5, 0.6) bin is not a quartile and that the quartile-based result (Appendix D) does not contradict the fixed-bound bin result.

P4-m10 (Formatting/notation; Appendix A, Table X; scattered)
Problem: Minor inconsistencies in the way the apodization “C2 2°” style is rendered (e.g., “C 2 2 ◦”) and occasional casual use of “fsky” for effective weighted fractions.
Required fix: Normalize the LaTeX rendering of the apodization label and use “feff_sky” consistently for weighted/apodized cases (without rehashing the previously raised P4-m3).

P4-m11 (Equation-to-text alignment; Sec. VI B)
Problem: The edge-on dilution number “8.98%” is correct but the simple numeric evaluation ((1 − 0.158)−1/2 − 1) is not shown, which would help readers follow.
Required fix: Add the explicit one-line numeric calculation, as already suggested in the earlier review, to aid reproducibility at a glance.

P4-m12 (Figure–body micro-alignment; Fig. 8 vs. text)
Problem: Fig. 8 annotates σℓ=1 = +3.63, whereas the body often cites +3.64 for the canonical single-mode result. This is almost certainly rounding and panel/battery differences, but a brief parenthetical “panel shows pre-MASTER pseudo-Cℓ; body cites the post-MASTER single-mode result” would avoid confusion.
Required fix: Add a one-clause clarifier in the caption noting the pre- vs post-MASTER distinction to preempt misreading.

JUSTIFICATION FOR NEW FINDINGS
- The apodization-weight sum (P4-E6) and parity-antisymmetry wording (P4-E7) are correctness/clarity issues that can mislead readers about weighting and invariance.
- Cross-reference P4-E8 is a navigational error.
- Baseline z mismatch (P4-E9) is a presentation inconsistency that could be read as drift of the primary number.
- The extended WLS claim (P4-M7) needs minimal numbers to be auditably true.
- The remaining items (m7–m12) are clarity/consistency improvements that will reduce reader confusion without changing conclusions.