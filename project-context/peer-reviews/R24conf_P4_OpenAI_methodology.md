# P4 R24conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v168.pdf` md5=90c4a8a3 pages=19
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9619 chars)
**Wall time**: 368.4s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (19 pages)

Scope of review
I audited the statistical methodology, estimator definitions, null procedures, arithmetic/internal consistency, dimensional checks, and whether the abstract/conclusions are traceable to the body. Below are all issues found, classified by severity.

ESSENTIAL findings (must be fixed for PRD)

P4-E1 — Sec. IV C–D and Table III (pp. 7–10): Inconsistent canonical-mask MASTER ℓ=1 significance
- Problem: The text repeatedly cites a “post-MASTER canonical-mask residual” of +3.64σ (e.g., Sec. IV D text and figure narrative), yet Table III reports for the “canonical, unapod.” row z=+7.93 (Cdata=7.27×10−6, ⟨C⟩null=0.57×10−6, σnull=0.84×10−6 → z≈7.97). The caption states these rows are MASTER-decoupled with galaxy-weighted mask-mean subtraction. That appears to be the same “post-MASTER canonical-mask” category that the text characterizes as +3.64σ. This is an internal contradiction in a load‑bearing diagnostic.
- Required fix: Unify estimator definitions and values. If there are truly two distinct canonical estimators (e.g., different field conventions, monopole treatment, coupling-matrix binning), give each a precise, unique label and list both, with a short table mapping each number to its exact recipe (field, subtraction, weight, binning, ℓ-range, NMC). Remove all mixed references (“the canonical residual is +3.64σ”) or qualify each with the exact estimator label. As written, the reader cannot tell which canonical number is operative.

P4-E2 — Sec. VII (p. 12) and throughout: Very large harmonic-channel injection significances quoted without in-paper evidence
- Problem: The paper claims harmonic-channel completeness with staggering significances (e.g., injected Ap=1.7% gives median z≈68–218; Ap=3% gives z≈209–685). No numeric table, plot, or summary statistics for these injections appear in the paper; they are only referenced via repository “artifacts.” For PRD, such decisive figures must be in the manuscript or its Supplemental Material, not only in external logs.
- Required fix: Add a table/figure in the paper (or Supplemental Material submitted to PRD) giving, for a grid of injected Ap and several fixed axes, the recovered C1, null mean/σ, and z (with NMC stated), including axis dependence percentiles. Otherwise, remove the extreme z claims.

P4-E3 — Sec. IV C (p. 6–7): Provide an explicit 95% CL upper limit on the dipole amplitude from the primary estimator
- Problem: The headline real-space amplitude is Adip=4.4×10−3 (Ap units) with rank-p=0.31 (z=0.41). An empirical sensitivity floor via injection is given, but there is no formal confidence interval/upper limit on Adip from the real-space estimator itself.
- Required fix: Report a 95% CL upper limit on Adip from the real-space dipole fit using the same null (e.g., the rank-based bound from the permutation distribution or a parametric bootstrap), and translate it into fCW deviation (A/2) for clear interpretation. This is standard for PRD-level null results.

P4-E4 — Sec. IV C (pp. 6–7): Detection criterion and “σ” definition for injection/recovery tests are not fully specified
- Problem: Table V quotes P(σ>3) but does not explicitly define the σ used in the injection workflow for the real-space estimator (moment-z relative to which null distribution? same as in headline? how is variance estimated under finite NMC?) within the injection section itself. The body mentions both permutation and label-shuffle nulls elsewhere.
- Required fix: Define precisely the σ statistic used in injection-recovery: which null, how z is computed (moment-z vs. empirical-rank), one-sided vs two-sided, and the NMC per point. Include uncertainty from finite NMC (e.g., binomial error bars on P(σ>3)).

P4-E5 — Sec. IV D, Fig. 8, Table III (pp. 9–10): Mixed null sizes and conventions across plots/tables without harmonization
- Problem: Different displays use different NMC (200, 500, 10,000), different field conventions, and different subtraction steps. While some captions attempt to clarify, the reader is forced to reconcile multiple incompatible configurations. For PRD, the main figures/tables must present a single, harmonized setup so numbers are directly comparable.
- Required fix: Choose a canonical null size (≥10,000) and a single, fully specified field convention for all key harmonic diagnostics (both apodized and canonical masks). Recompute Fig. 8 and the canonical rows in Table III under that same convention, and ensure the text references the harmonized numbers. If legacy values are kept for discussion, label them unambiguously as legacy and remove them from summary statements.

P4-E6 — Throughout body (multiple pages): Heavy use of internal repository “artifact” filenames and run logs in the scientific narrative
- Problem: The text repeatedly cites paths like pipelines/p2_chirality/... and “artifact c9b”, which are internal bookkeeping, not stable scientific references. PRD requires self-contained descriptions (or a formal Supplemental Material) so readers can follow without chasing ephemeral repository states.
- Required fix: Move all such run-log/file-path references to a structured Supplemental Material or a Data/Code Availability appendix with stable DOIs. In the main text, replace each “artifact” reference with a pointer to a figure/table in the paper/Supplement or to a dataset DOI with a clear description.

MAJOR findings (significant revision)

P4-M1 — Sec. IV C (p. 6): Real-space estimator weighting choice not fully justified or stress-tested
- Problem: The healpy.fit_dipole with uniform pixel weighting on Ap (after masking with Nspiral≥10) is used for the headline. While two null procedures are tested, there is no companion result for a galaxy-count–weighted fit or an analysis of robustness to the Nspiral threshold (N≥10, 20, 50) within the real-space estimator itself (not just harmonic channel).
- Required fix: Provide a robustness panel/table for the real-space dipole: (i) uniform vs. Nspiral-weighted fits; (ii) Nspiral(p) threshold sweep; and show the fitted amplitude and null p-values for the HC-broad selection. If the results are statistically indistinguishable, state so; if not, justify the chosen default.

P4-M2 — Sec. VI A (p. 11): “Harmonic-channel completeness” claims depend on estimator differences not made explicit
- Problem: The text notes that harmonic-channel completeness is not interchangeable with the real-space falsification boundary, but then uses those extreme completeness numbers rhetorically in Conclusions. This risks reader confusion.
- Required fix: Clearly segregate the two channels in Conclusions with a short boxed statement (bulleted) listing, per channel: field, mask, weights, null, estimator; and explicitly state that harmonic-channel completeness is diagnostic-only and not used to set cosmological limits.

P4-M3 — Appendix D (p. 16): WLS template fit under near-collinearity without condition-number diagnostics
- Problem: Table IX notes imaging-leg fraction templates are nearly collinear with the constant, yielding very large naive errors. The block bootstrap inflates uncertainties, but no condition number or regularization/orthogonalization is discussed.
- Required fix: Report the design-matrix condition number and either (i) orthogonalize the nuisance basis (or use ridge regression with a stated penalty, validated by cross-validation) and show that the marginalized dipole posterior is stable, or (ii) demonstrate via projections that the dipole subspace is sufficiently orthogonal to the nuisance subspace that the bootstrap is robust to collinearity.

P4-M4 — Sec. IV C (p. 6–7): “Unthresholded sample” 0.57% dipole at z≈4.2–4.4 labeled as systematics without quantitative support in-paper
- Problem: The claim that this comes from “low-confidence tail” is plausible but not quantitatively demonstrated in the paper.
- Required fix: Add a short figure of Adip and z as a function of the confidence cut peq (e.g., peq ∈ {0, 0.4, 0.5, 0.6, 0.7, 0.8}) using the same null and estimator, to show the monotonic suppression as confidence increases. This directly supports the systematics attribution.

P4-M5 — Sec. IV B (p. 5): Slab-uniformity claim depends on external artifact files
- Problem: The seven-slab fCW numbers (0.49537–0.49890) are quoted but only “artifact” files are cited.
- Required fix: Include a small table with per-slab N, fCW, and binomial σ in the paper or Supplemental Material.

P4-M6 — Sec. VI A (p. 11): Axis-draw protocol in injection tests is not area-uniform
- Problem: The text acknowledges θ∼U(0,π) (not area-uniform) and states a spot check with area-uniform axes is consistent. For publication, completeness curves should not depend on a subtle axis prior.
- Required fix: Redo the injection-recovery with area-uniform axes for the main curve in Table V (or provide both with differences). Provide binomial error bars on P(σ>3).

P4-M7 — Sec. A (p. 13): Monopole subtraction description vs. quoted canonical significances
- Problem: Appendix A notes that monopole subtraction reduces C1 from 2.30×10−5 to 1.51×10−5 and “increases σ from +1.85 to +3.64.” This is a non-intuitive juxtaposition; it ties back to P4-E1 and the lack of a harmonized canonical estimate.
- Required fix: Once P4-E1 is resolved, ensure Appendix A statements exactly match the canonical numbers in the revised Table(s), and explain, in one sentence, why z increases when C1 decreases (e.g., tighter null width after subtraction).

MINOR findings (address, but can proceed)

P4-n1 — Sec. II B (p. 2): Catalog B fraction and “+14.6σ” dev
- Problem: Catalog B row shows 0.504 ± 0.0003 with dev +14.6σ; from rounded numbers, 0.004/0.0003=13.3σ. You note the dev is computed from the unrounded calibrated fraction; fine, but it is misleading as printed.
- Required fix: Print the unrounded value to enough digits (e.g., 0.5040x) or add a footnote that the dev uses the unrounded calibrated fraction to avoid apparent mismatch.

P4-n2 — Sec. VI A (p. 11): Terminology — “face-on (high-inclination-angle)”
- Problem: Face-on corresponds to low inclination, not “high-inclination-angle.”
- Required fix: Correct the wording.

P4-n3 — Formatting (multiple pages): Apodization notation
- Problem: “C 2 2 ◦” spacing and superscripts appear irregular.
- Required fix: Standardize to “C2 apodization with 2° apodization length.”

P4-n4 — Data/Code availability (p. 17): Stable archiving
- Problem: No DOI for the catalog/code snapshot at submission time.
- Required fix: Provide a Zenodo (or equivalent) DOI for the exact version used in this manuscript prior to final acceptance, per PRD best practice.

NITs (cosmetic)

P4-N1 — Typos and micro-edits
- Example: “evquivariant,” “per-imaging-leg × confidence-bin” hyphenation inconsistencies, stray spaces around mathematical symbols in Table I and captions. Do a careful proofread.

P4-N2 — Repetition
- Several places repeat the same caveat that σ values from different nulls are not comparable; keep the most prominent instances and streamline where redundant.

Arithmetic/consistency checks (spot audits)

- Table II: Catalog A and C binomial σ recomputed and match (0.000274, 0.000279); z from (f–0.5)/σ checks out (28.7, −9.5). Asymmetry suppression factor |1.576%|/|0.529%|≈2.98: correct.
- Fisher floor Eq. (4): σ(A)=√(3/Nspiral)=√(3/3.20116e6)=9.68×10−4 and σ(A/2)=0.048%; 3σ≈0.29%: correct (dimensional consistency fine).
- Real-space dipole amplitude 4.4×10−3 (Ap) → 0.22% fCW deviation (A/2): consistent.
- Apodized MASTER ℓ=1 (Sec. IV C.b): Cdata=2.348×10−5, ⟨C⟩null=1.71×10−6, σnull=2.99×10−6 ⇒ z=7.28; rank-p=(5+1)/(10^4+1)=6.0×10−4: correct.
- Monopole+mask leakage (Table IV): Data 1.6961×10−2 vs null mean 1.6846×10−2 with std 0.0068×10−2 ⇒ z≈1.69 and reproduction 99.32%: correct.
- Block-bootstrap WLS exclusion (Appendix D): Aref=0.034 (Ap units), Abest=4.55×10−3, σboot=1.63×10−3 ⇒ z≈(0.00455−0.034)/0.00163≈−18.1: correct.

Length and focus
- The manuscript is dense with repeated caveats and run-log references. For the claimed methodological advance plus a null detection, 19 pages is on the long side, mostly due to repetition. I recommend trimming 2–4 pages by (i) consolidating null/estimator caveats into a concise “Estimator dictionary” box, (ii) moving internal run-log/path mentions to Supplemental Material, and (iii) harmonizing all harmonic-channel results into one table plus one figure.

## Summary recommendation
MAJOR REVISIONS

The central real-space null result appears methodologically sound and the arithmetic cross-checks mostly pass. However, there is a critical internal inconsistency between the quoted “post-MASTER canonical-mask” ℓ=1 significance (+3.64σ in the text) and the MASTER-decoupled canonical row in Table III (+7.93σ), and several key claims (extreme harmonic injection significances, systematics attribution of the unthresholded 0.57% dipole) rely on external “artifacts” rather than in-paper evidence. PRD requires a harmonized, self-contained presentation of estimators and nulls, formal limits on the dipole amplitude, and removal of repository run-log clutter from the narrative. Addressing the ESSENTIAL and MAJOR points above will bring the paper up to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL (must be fixed for PRD)

P4-E7 — Fig. 2 caption vs Methods: D4 vs Z2 TTA inconsistency
- Problem: Fig. 2 is titled “Test-time D4 equivariant averaging (TTA)” and the caption states the classifier is evaluated on all eight D4 transforms, calling this “the key methodology distinction between Catalog A, B, and C.” But Sec. III C says production uses 2-fold (horizontal flip only) TTA and explicitly restricts to Z2, with D4 used only for a small hold-out validation. As written, readers will conclude the production Catalog C used full D4 averaging.
- Required fix: Clarify in the caption and body that production Catalog C uses 2-fold (flip-only) TTA; D4 was used solely as a validation experiment on small subsamples. Rename the figure or add a bold note to avoid implying D4 was the production protocol. Also correct the sentence implying TTA is “the” distinction for all tiers (Catalog B is Platt-calibrated, not equivariant).

P4-E8 — Hemisphere look-elsewhere correction described inconsistently (double vs single correction)
- Problem: Table I note says the hemisphere maximum statistic already uses a direct-MC look‑elsewhere null (max over 648 directions) and then applies “an additional Bonferroni/BH pass” as a second, conservative penalty. Appendix C states the empirical joint correction “is applied once (no double correction).”
- Required fix: Choose one correction protocol and apply it consistently. If the max‑statistic MC already accounts for LEE, do not apply a second directional multiple-testing penalty in the main text or table. Report both numbers (pre-/post-extra-penalty) only if clearly labeled, and ensure the same choice is reflected everywhere this result is quoted.

P4-E9 — Misuse of HC-broad injection floor to dismiss unthresholded full-sample signal
- Problem: The text argues the unthresholded-sample dipole (A ≈ 0.57%, z ≈ 4.2–4.4) “sits below the A50 ≈ 0.75% injection floor,” but A50 was derived on the HC‑broad subsample (peq > 0.6, N ≈ 9.5×10^5), not on the full unthresholded sample (N ≈ 3.2×10^6). Sensitivity and the null width differ across these samples; an A50 measured on a smaller, cleaner subsample cannot be used to bound detectability in the larger, noisier full sample without re-running the injections for that sample and estimator.
- Required fix: Provide an injection–recovery curve for the unthresholded full‑sample with the exact estimator/null used to obtain the z ≈ 4.3 value, and then assess detectability against that curve. Alternatively, explicitly withdraw the “below the A50 floor” statement for the full-sample context.

P4-E10 — Conclusions and Sec. VI A mix Fisher/empirical floors across different samples without a matched empirical floor for the full sample
- Problem: The Fisher floor (σ(A) ≈ 0.097% at 1σ for N=3.2M; 3σ ≈ 0.29%) is discussed for the full sample, while the empirical A50 ≈ 0.75% is for the HC‑broad subsample. No empirical floor is given for the full sample, which is the one used to report the unthresholded z ≈ 4.3.
- Required fix: Add an empirical A50/A95 for the full‑sample estimator/null, or confine floor statements to the exact sample on which they were measured (and state that no empirical floor is provided for the unthresholded sample).

MAJOR (significant revision)

P4-M8 — fsky labeling for weighted analyses is inconsistent and potentially misleading
- Problem: Table I lists fsky = 0.494 for the apodized-footprint MASTER diagnostic row while Appendix A (Table VI) states that for weighted/apodized footprints one should quote an effective sky fraction f_eff_sky = ⟨W⟩^2/⟨W^2⟩ (0.452 for Wp=Nall, apod.). The table column header is simply “fsky,” and mixes geometric fractions (binary masks) with effective fractions (weights/apodization) elsewhere.
- Required fix: Harmonize and label clearly: either (i) add a separate “f_eff_sky” column for weighted/apodized rows and keep “fsky (binary)” for geometric pixel fractions, or (ii) report both in footnotes per row. Ensure all places in text and tables use the same convention.

P4-M9 — Bias-hardening T7 (calibration proxy) lacks the promised quantitative checks
- Problem: T7 is said to require that “the flip-swap error of high-confidence (max p > 0.9) predictions be lower than that of low-confidence (max p < 0.7) predictions.” Only the fraction above 0.9 (73.6%) is reported; the flip-swap error comparison is asserted but not quantified.
- Required fix: Report the measured flip-swap error rates for the two confidence regimes, with uncertainties, to substantiate that T7 passes as defined.

P4-M10 — Ambiguous/implausible training accuracy statements (Appendix B)
- Problem: Appendix B reports “headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields 94.9%.” Accuracy typically does not improve when disabling test-time augmentation if the model was validated without it; the statement is ambiguous as to which split (train/val), which labels (mixed CE‑ResNet/GZ1), and which evaluation protocol.
- Required fix: Specify the dataset split and label source for these accuracies (e.g., validation on the 20% holdout of the 25,790 training set; what fraction are CE-ResNet pseudo-labels). Clarify whether “with augmentation active” refers to training or test-time augmentation. If it refers to test-time augmentation, explain why accuracy increases when augmentation is removed, or correct the numbers.

P4-M11 — Hemisphere statistic uses two different direction grids; keep results segregated
- Problem: Appendix C analyzes a 648-direction 10° grid; Table IV’s generative-null hemisphere statistic uses a 768-direction NSIDEdir=8 grid. The σ values are placed side-by-side in Sec. IV D as “candidate manifestations.” Although footnotes note non-comparability, the prose juxtaposes them in a way that invites comparison.
- Required fix: In the main text, present only one hemisphere result per context (or segregate clearly into separate subsections) and avoid side-by-side numerical comparisons across different direction grids. If both are retained, add explicit caveats in the body text, not only in table footnotes.

P4-M12 — Over-strong assertion that weighted-mean subtraction “does not introduce monopole–dipole coupling”
- Problem: Appendix A states that using Wp=Nall and subtracting the galaxy-weighted mask-mean “does not introduce a monopole–dipole coupling.” On a cut sky with non-uniform weights, leakage properties are governed by the mode-coupling matrix; subtracting a weighted mean removes the mean but does not by itself prove absence of induced ℓ=1 coupling in the decoupled estimate.
- Required fix: Soften the claim or provide a short derivation/citation showing that, with NaMaster’s exact mode-coupling treatment and the specified monopole subtraction, the decoupled ℓ=1 estimate is unbiased with respect to a uniform monopole under the given weighting.

MINOR (address but can proceed)

P4-n5 — Table I row (iv) readability
- Problem: The apodized MASTER row reports “+7.28/+7.13” without in-row indication that these correspond to two different nulls. The weight choice Wp and null choice are only in the caption/text.
- Required fix: Add inline labels (e.g., “+7.28 (global shuffle) / +7.13 (depth‑stratified)”) or split into two subrows.

P4-n6 — Undefined notation “σiso”
- Problem: Appendix C uses “σiso” without an explicit definition.
- Required fix: Define σiso on first use (e.g., moment‑z relative to isotropic per‑pixel permutation null).

P4-n7 — Consistent one-sided/two-sided p‑value reporting
- Problem: Some places state both (e.g., p=0.31 one‑sided; two‑sided 0.62); others report only a one‑sided p with no qualifier.
- Required fix: Add a short conventions paragraph early in Sec. IV stating default sidedness and ensure all p‑values specify sidedness or give both.

P4-n8 — Arithmetic in Table IX z-values
- Problem: Appendix D, Table IX lists the dipole ŷ coefficient −4.52×10−3 with naive σ = 1.0×10−4, which implies |z| ≈ 45.2, but the table reports z = −43.3. Either the σ actually used is ≈1.04×10−4 or there is a rounding/typo.
- Required fix: Print σ to sufficient precision (or correct z) so z = â/σ matches the displayed numbers.

P4-n9 — Minor clarity on “reference amplitude” units
- Problem: The text often refers to a “1.7% dipole” without immediately restating whether this is in fCW (half‑amplitude) or Ap units. Appendix D clarifies Aref=0.034 (Ap), but the main text sometimes omits the mapping.
- Required fix: When first mentioning 1.7% in each section, parenthetically add “(fCW units; Ap=0.034)”.

P4-n10 — Figure–text mapping for confidence-stratified suppression
- Problem: Sec. IV E states that the +3.3σ in [0.5,0.6) “does not survive” at peq>0.6, giving “−0.03σ,” but does not explicitly name the estimator or null for the −0.03σ value, and it sits near text that discusses the real‑space dipole (+0.41σ at peq>0.6), inviting confusion.
- Required fix: State explicitly which estimator/null the −0.03σ refers to and keep it in a figure/table showing the estimator dependence across confidence cuts.

Explanation
These items were not covered in the initial review because they emerge from cross-checking figure captions against Methods (D4 vs Z2), reconciling sample‑specific sensitivity floors with claims about different samples (HC‑broad vs full), and verifying table arithmetic/notations (Table IX z-value, σiso). Addressing them will improve internal consistency, remove sources of reader confusion, and align the manuscript with PRD’s standards for methodological clarity.