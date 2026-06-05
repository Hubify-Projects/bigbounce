# P5 R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7860 chars)
**Wall time**: 437.4s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of this review
- Focus: methodology rigor (statistical validity, internal arithmetic consistency, derivations, error propagation).
- I audited every load-bearing scalar and sigma quoted in the abstract and conclusions against the body, and checked figures/tables for consistency.

Overall assessment
The paper presents a large-scale cross-match of a spiral-galaxy chirality catalog with DESI DR1 environments, concluding “no environment dependence” once a catalog-wide monopole offset is accounted for. The core idea is reasonable and potentially useful. However, there are several critical internal inconsistencies and methodological gaps that must be resolved before this work meets Physical Review D standards. Most importantly, (i) sample sizes and σ claims are inconsistent across sections, (ii) the primary independence claim is not supported by a single, formal test-of-independence across the four V-Web classes, (iii) the Phase-2 sweep cites a class count that exceeds the total chirality-labeled sample by a factor ≈4.7, and (iv) key “bright vs dark” subsample sizes are inconsistent within the paper.

Detailed findings

ESSENTIAL

P5-E1 (Section VII, p.10): Impossible Phase-2 class size and σ claim
- Offending text: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole leaking through the largest sample bin and is predicted, not measured... the observed −11.3...”
- Problem: n = 3,696,152 for a single environment class exceeds the total number of chirality-labeled matched spirals (791,635) by a factor > 4.6. No environment re-binning can increase the total number of chirality-labeled objects. Moreover, you describe the 11.32 as “observed,” yet simultaneously say it is “predicted.” This is irreconcilable.
- Required fix: Correct the class count and the σ claim. If this number came from a different parent (e.g., all spectroscopic DR1 objects without chirality labels), state that explicitly and do not mix it with chirality-based σ estimates. Provide the correct per-class n for the chirality sample for each sweep cell, and recompute any σ that are “observed.” Remove any “observed” σ computed on objects without chirality labels.

P5-E2 (Sections VI.A/C/D; V.B; VIII.F; multiple pages): Lack of a single formal test of independence across environment classes
- Problem: The headline “no environment dependence” is argued via (i) per-class deviations from 0.5, (ii) comparisons to the Paper IV monopole prediction, and (iii) descriptive “range across classes.” None of these constitute a single omnibus test of chirality independence across the four V-Web classes (void, wall, filament, cluster). Testing “each class vs 0.5” is not the same as testing “all classes have equal fraction,” and a descriptive range is not a test statistic with a defined null distribution for “independence.”
- Required fix: Provide (at minimum) one formal independence test on the same sample used for Table II:
  - A 2×4 Pearson χ2 test of independence (CW/CCW × environment), or
  - A logistic regression of the CW indicator on environment factor (four levels), optionally with a fixed offset for the catalog monopole (or equivalently, a regression on centered residuals fCW − fP5 with robust s.e.). Report test statistic, d.o.f., and p-value. If you use the “monopole-subtracted” residuals, propagate the uncertainty of fP5 or treat fP5 as a nuisance parameter estimated from the same data (do not treat it as known).
  - Do the same for the DESIVAST void vs non-void binary classification (two-proportion test; see P5-E4).

P5-E3 (Section VI.D.b, p.7 vs. Section VI.D.c, p.7; Section VI.D overall): Inconsistent tracer-program sample sizes (dark counts)
- Offending text:
  - “dark (LRG, ELG, QSO; n = 14,782...)” (p.7, tracer-program split on the matched-spiral catalog)
  - “filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85” (p.7)
- Problem: The filament dark subsample size (21,203) exceeds the entire dark-program count (14,782) reported two paragraphs earlier on the same page. This is impossible unless different parent samples are being used without disclosure (e.g., the 812,793-labeled “superset” introduced later in §VIII.F). This undermines all bright/dark significance statements, including the quoted “|z| ≈ 3.4σ on the filament class.”
- Required fix: Unify the sample definition across the paper or explicitly state when a different parent (e.g., the 812,793 env-labeled superset) is used. Recompute and report all bright/dark counts and σ on the same parent. If you retain the 812,793 superset for the bright/dark analyses, clearly mark that all statistics in those subsections are on that superset and not on the 791,635 headline sample; recompute any totals accordingly and remove contradictory counts.

P5-E4 (Section VIII.B, Table VII, p.11): No formal significance for DESIVAST void vs non-void difference
- Offending text: “returns fvoidCW = 0.4964 vs fnon−voidCW = 0.4971, ∆fCW = 0.0007, statistically indistinguishable.”
- Problem: The adjective “statistically indistinguishable” is not supported with a formal two-proportion test or p-value. The DESIVAST void analysis is declared as the primary path (§V.B); it therefore must carry a formal significance calculation.
- Required fix: Provide a two-sample difference-of-proportions test (z or χ2), reporting z and p, and the 95% CI on ∆fCW. By my back-of-envelope (treating p≈0.5), the SE is ≈0.00219 and z≈0.32 for ∆=0.0007, but you must report the exact computation you use.

P5-E5 (Section VI.A, p.5): Incorrect/suspect σpred for filament
- Offending text: “predicting σpred from ∆fCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28...”
- Problem: With Nfil = 408,187, σpred = 2·∆fCW·√N = 2·(−0.0026)·√(408,187) ≈ −3.32, not −3.16. The cluster value (−3.28 for N=397,505) is consistent. This suggests either an inconsistency in N, in ∆fCW, or a rounding/slip for filament.
- Required fix: Recompute σpred for all classes using the stated ∆fCW and the class-specific N from Table II, and correct the text. If you use a different ∆fCW locally, state it.

P5-E6 (Abstract + throughout): “Primary” analysis declared post hoc; headline conclusion depends on post-selection
- Offending text: “Primary analysis path... is designated... post hoc” (p.5).
- Problem: You openly acknowledge that the “primary” DESIVAST path was designated after looking at multiple classifier/stratification options. PRD does not require preregistration, but a post hoc choice requires extra care to control Type I error inflation and to avoid selective reporting. The current manuscript attempts to address this by labeling V-Web/Tempel/ASTRA as “secondary,” but it does not provide a pre-specified primary estimator nor a pre-specified decision rule.
- Required fix: Tighten the inferential framework. Define a single, explicit primary test statistic for the DESIVAST path (e.g., ∆fCW with two-proportion z-test) and state the decision rule (α) before presenting results. If you want to keep the V-Web and other analyses, (i) clearly separate them as exploratory and (ii) refrain from using them to support headline claims except as cross-checks. Alternatively, move some exploratory content to Supplementary Material.

MAJOR

P5-M1 (Section VII, p.10): Use of “range of fCW across classes” as a robustness metric is not a valid hypothesis test
- Problem: The per-cell “range” statistic is descriptive and depends on which classes happen to be sample-size limited (void, wall). It is not a valid test for equality of proportions across classes, and comparing it to the “dominant per-class counting-statistics floor” does not control the false positive rate.
- Required fix: Replace or augment the “range” descriptor with a formal test per cell (e.g., a 2×4 χ2 or a logistic regression term for environment), report the max-statistic across the nine cells, and evaluate it using the label-shuffle max-stat null you already implement. The “range” plot can remain descriptive, but the conclusion should rely on a test with a defined null.

P5-M2 (Section VIII.F, p.12–13): Monopole-subtracted σvs-monopole treats fP5CW as known; uncertainty not propagated
- Problem: You subtract fP5CW estimated from the same or a closely related sample and assess residual σ vs monopole. The uncertainty of fP5CW (and sample overlap) is ignored.
- Required fix: Either (i) propagate the uncertainty of fP5CW into the residual test (e.g., via parametric bootstrap or delta-method) or (ii) treat fP5CW as a nuisance parameter and use a test of equal proportions across classes without subtracting the monopole (which the χ2 test naturally accommodates).

P5-M3 (Section VI.E/ Table V / Fig. 4, p.9): Clarify the HEALPix “npix” and mask definition
- Problem: At NSIDE=16 the full sky has 3072 pixels, but Table V lists npix=1054. Similar reductions occur at NSIDE=32 (should be 12,288; table shows 3303) and NSIDE=64 (should be 49,152; table shows 7208). This is presumably a mask/occupancy cut, but it is not defined in the text of §VI.E.
- Required fix: Define the per-NSIDE pixel selection rules (e.g., “valid” pixels require ≥N spirals; masking detail); ensure npix matches those rules and is consistent between text and figure captions.

P5-M4 (Section VIII.A, p.11): “0/6 V-Web void spirals inside any DESIVAST hole” needs explicit reproducible selection and uncertainty
- Problem: While illustrative, 0/6 is a very small N. The selection criteria for these 6 galaxies are not fully specified (e.g., are they within z≤0.24 after all cuts?).
- Required fix: Specify the exact selection steps and provide the 95% Clopper–Pearson upper bound on the V-Web-void purity under this cross-match (so the reader can interpret 0/6 quantitatively).

P5-M5 (Section VI.C, Table III, p.6–7): Density-quintile analysis: residuals vs monopole
- Observation: You state the max residual |σobs − σpred| ≈ 1.87, below Bonferroni-5 at α=0.01 (3.09). This is fine, but please also show (or report) the simple 2×5 χ2 test for independence of chirality on density quilted bins. This would align the presentation with the environment-class independence tests requested in P5-E2/M1.

MINOR

P5-m1 (Abstract vs body): “16.4 × 10^6 ZWARN=0 input rows” vs Table I “16,361,731 DESI DR1 input rows”
- Required fix: Make the abstract number match Table I (16.36×10^6), or clarify any minor filtering that explains the difference.

P5-m2 (Section VI.A, p.5): Text says σpred(filament)≈ −3.16 (see P5-E5). Once corrected, ensure the abstract’s narrative about “tracking the monopole” uses the corrected values.

P5-m3 (Section VIII.B, p.11): When quoting ∆fCW = 0.0007 (DESIVAST void vs non-void), give it in the same unit as the rest of the paper (percentage points) once in parentheses: “0.07 pp,” and report the formal z and p (see P5-E4).

P5-m4 (Section VIII.E, Table IX, p.12): The “0 maximal voids per pixel” bin is effectively “outside DESIVAST coverage.” State this explicitly in the table caption or text adjacent to the table to prevent misinterpretation.

P5-m5 (Section IX.A, Fig. 7, p.16): The Tempel–V-Web “concordance 0.026 pp” is stated, but the V-Web values used for the exact same overlap sample are not in the text. The figure appears to show them; consider adding a small table in the text or caption with the exact numbers used to compute 0.026 pp.

P5-m6 (Multiple locations): Over-precision/overstatement of p-values, e.g., “p<10−1000” (p.8). Replace with “p ≪ 10−10” or “p effectively zero to machine precision for χ2=4932 with 3 d.o.f.” PRD discourages unrealistically precise tail probabilities without computation details.

P5-m7 (Equation (2), p.4): State explicitly that this uses a standard normal approximation for σfrom-half under the binomial null (and that it is two-sided). This will help readers map the erfc−1 threshold to z-scores.

P5-m8 (Section XI, p.17–18): The “confidence-threshold sweep pmax_cls_eq ∈ {0.4,…,0.8}” appears without a prior definition of this quantity. Add a brief definition (e.g., “maximum softmax probability from the chirality classifier”).

NITS

P5-n1 (Terminology consistency): You alternate between “pp,” “percentage points,” and fractional differences. Standardize throughout (e.g., always report both, like “0.0007 (0.07 pp)” at first mention in a section).

P5-n2 (Typos/wording): A few typos and duplicated hyphenation (e.g., “pre-monopole- subtraction”; “class-to- overall”). A careful proofread will fix these.

P5-n3 (Units): Ensure consistent spacing “Mpc/h” vs “Mpc h−1” and consistent use of “comoving” when referring to grid scales.

P5-n4 (Figure captions): Fig. 5 (“Phase 2 sensitivity heat-map”) – define explicitly that the color is “max minus min fCW across classes in percentage points.”

Length and scope
For a null result with robust cross-checks, 20 pages is long. Much of the secondary material (multiple classifier cross-checks and extensive HEALPix scans) could move to Supplementary Material. I recommend aiming for ≤ 12–14 pages in the main text, with the DESIVAST “primary” analysis, a single formal omnibus test for V-Web classes, and one or two key robustness checks retained.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains critical internal inconsistencies (impossible class counts; contradictory subsample sizes), and the headline “no environment dependence” is not supported by a single formal omnibus test of independence across environment classes. The DESIVAST “primary” void vs non-void result lacks a formal two-proportion significance test. The Phase-2 sweep reports an “observed” σ based on an n that cannot come from the chirality-labeled sample, which must be corrected. These problems are fixable, but they require substantial revision, recalculation, and clearer inferential framing before the paper can meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P5-E7 (Sec. I, p.2): Mischaracterization of Paper IV parity result by ≈×9
- Offending text: “Paper IV … establishes the global mixture … 0.4974 ± 0.000279, consistent with parity at ∼ 1σ.”
- Problem: 0.5 − 0.4974 = 0.0026; 0.0026 / 0.000279 ≈ 9.3σ from 0.5, not ∼1σ. The manuscript elsewhere correctly treats this as a classifier monopole, but the “∼1σ” statement is arithmetically false and undermines the narrative discipline around the monopole.
- Required fix: Correct to reflect a ≈9.3σ offset from 0.5 in Paper IV (interpreted there as a classifier monopole), or explicitly rephrase to say “statistically inconsistent with 0.5 but attributed to classifier monopole bias.”

P5-E8 (Sec. XI, p.17–18 vs. Sec. VI.D.b, p.7): Direct contradiction on bright vs dark overall CW fractions
- Offending texts:
  - Sec. VI.D.b: “bright … fCW = 0.4970 … dark … fCW = 0.5051 …” (difference 0.0081 = 0.81 pp; dark higher).
  - Sec. XI systematics: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.”
- Problem: These two statements cannot both be true on the same parent sample. The earlier section reports a sizeable 0.81 pp bright–dark difference; the systematics section claims ≤0.1 pp. No parent-sample switch or conditioning is disclosed in Sec. XI.
- Required fix: Recompute and reconcile. If Sec. XI uses a different parent (e.g., a different mask, redshift cut, or the 812,793 superset), state it explicitly and provide the exact counts and fractions. Otherwise correct/remove the “±0.001” claim.

MAJOR

P5-M6 (Sec. VIII, RSD paragraph, p.10): Incorrect internal cross-reference
- Offending text: “This is in contrast to the V-Web secondary path (§XIII) …”
- Problem: §XIII is “Limitations,” not the V-Web description. The intended reference is §IV (V-Web classifier) or §VII (sweep).
- Required fix: Correct the section reference.

P5-M7 (Per-pixel statistics; Sec. VI.E Table V vs. Sec. VIII.F text vs. Fig. 6 caption): Inconsistent/undefined pixel-selection rules and pixel counts
- Observations:
  - Table V: NSIDE=32 npix=3,303 (global HEALPix scan).
  - Sec. VIII.F: distribution over “1,821 valid pixels” at NSIDE=32 (monopole-subtracted residuals, full matched-spiral catalog).
  - Fig. 6 caption (NSIDE=32): “1,496 valid pixels” for z ≤ 0.24; Pearson computed over 727 pixels with both voids and ≥200 spirals.
- Problem: Multiple, different npix values at the same NSIDE are used without a precise, centralized definition of selection/validity criteria (spiral-count thresholds, void-coverage requirement, monopole subtraction, redshift cuts). This impedes reproducibility and invites misinterpretation.
- Required fix: Add a compact table or paragraph enumerating, for each NSIDE and analysis, the exact selection rules (pixel occupancy thresholds, whether void-coverage is required, redshift cut, monopole-subtraction applied or not) and the resulting npix. Ensure captions reference those rules.

P5-M8 (Sec. VII, first paragraph, p.8): Ambiguous sweep specification “Ngrid = 256 × …”
- Offending text: “sweep over nine cells {Rs, λth} ∈ {10, 25, 50} Mpc/h×{0.0, 0.1, 0.3}, Ngrid = 256 × …”
- Problem: The grid is elsewhere specified as 256^3. “Ngrid = 256 × …” is ambiguous and suggests a one-dimensional grid or a multiplication by λth.
- Required fix: State unambiguously that all cells use a 256^3 grid; remove any “× λth” ambiguity.

P5-M9 (Sec. XIII, RSD estimate, p.18): Inconsistent magnitude for the eigenvalue shift from RSD
- Offending text: “At σrsd ∼ 5 Mpc/h and Rs = 25 Mpc/h, the eigenvalue-shift magnitude is ∼ 0.04 σλ.”
- Problem: Earlier in the same paragraph, the heuristic shift is tied to σrsd/Rs, which is ≈ 5/25 = 0.20, not 0.04. The appearance of “0.04 σλ” is unexplained and dimensionally unclear (σλ is not defined here). This undermines the back-of-envelope boundary-crossing rate estimate.
- Required fix: Either justify the 0.04 factor from a defined σλ with a derivation or correct to the stated σrsd/Rs ≈ 0.20 scale. Clarify units and definitions.

MINOR

P5-m9 (Interval nomenclature; multiple places incl. Figs. 2, 3, 7 captions and Sec. V, p.4): “exact binomial 95% credible interval” vs. “95% Jeffreys credible interval”
- Problem: The text alternates between “exact” and “Jeffreys” intervals. Jeffreys is a Bayesian Beta(1/2,1/2) credible interval; “exact” commonly refers to Clopper–Pearson. They are not the same.
- Required fix: State which is used everywhere (preferably Jeffreys if that is what’s plotted) and use consistent terminology throughout.

P5-m10 (Sec. X, Table XII caption/body): Define the normalization for “max |σ| vs 1/2”
- Problem: It is implied σ is the binomial z from half using the same σ-from-half definition, but the caption does not say so, and the ASTRA-weighted case uses fractional counts and variances.
- Required fix: Add a one-sentence note: “σ computed as (fCW − 1/2)/(1/(2√n)) for argmax; for entropy-weighted we propagate per-object weights with variance Σi Pi^2/4.”

P5-m11 (Sec. V.A, “Empirical max-stat MC null”, p.4): Clarify sidedness
- Problem: Eq. (3) records the maximum absolute σ; the caption mentions “two-sided per-bin significance” earlier. The mapping between the one-sided max-stat CDF and the two-sided per-bin α needs one sentence to avoid confusion.
- Required fix: Explicitly note that the max-stat null uses |σ|, corresponding to a two-sided test per bin.

P5-m12 (Sec. III.C, p.3): Justify 1″ match radius as “DESI fiber positioning tolerance”
- Problem: DESI fiber diameter is 1.5″; positioning RMS is smaller but not equal to a hard 1″ tolerance. The cross-match may be fine, but the justification may mislead readers.
- Required fix: Rephrase to “adopt 1″ as a conservative positional-matching radius; sensitivity to {0.5,1,2,3,5}″ is reported below.”

P5-m13 (Sec. VIII.B, p.11): “k = 20 KDTree neighbors sufficient given the 24 Mpc/h maximum hole radius”
- Problem: The 24 Mpc/h “maximum hole radius” is not documented in DESIVAST in this manuscript, and different DESIVAST products list larger effective radii for watershed voids. This is VoidFinder-specific, but the text could confuse readers.
- Required fix: Qualify that the 24 Mpc/h bound refers to VoidFinder hole spheres (not watershed effective radii) and add a parenthetical citation/page/column from the DESIVAST documentation.

P5-m14 (Abstract vs Sec. VII/Table VI units): Be explicit about fraction vs percentage points
- Observation: Abstract states “never exceeds 0.22 percentage points (max 0.0022 …).” Table VI lists “fCW range (pp)”. This is correct but easy to misread.
- Suggested tweak: In the first occurrence in the abstract/body, add “(0.22 pp = 0.0022 in fraction)”.

NITS

P5-n5 (Sec. V.B, “pre-registration caveat”, p.5): Tighten language
- Suggest replacing “was not filed” with “was not specified a priori; analyses are therefore exploratory unless explicitly designated as primary.”

P5-n6 (Sec. VII.A, bullet “Paper-IV-monopole reference”, p.9): Round consistently
- Problem: You list 3.27σ (cluster) and 3.32σ (filament); earlier the text says −3.28 and −3.16 (the latter already flagged in prior review). Ensure consistent rounding/signs when quoting σpred.

P5-n7 (Appendix A, operator units): Clarify dimensional analysis in one line
- Suggest adding a parenthetical noting the dimensions of gϕ needed to render the operator dimensionless in the chosen units, since ∇ϕ and ∇ρ/ρbg each carry 1/length.

Explanation
I focused on new discrepancies not covered in my initial review. The largest new issues are: (i) the 1σ claim for 0.4974 ± 0.000279 (off by ≈9×), (ii) the direct contradiction between Sec. VI.D.b and Sec. XI regarding bright–dark differences, and (iii) several reproducibility/clarity gaps around HEALPix pixel counts and RSD back-of-envelope scaling.