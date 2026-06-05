# P5 auto-2026-06-05_1418pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7704 chars)
**Wall time**: 237.7s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V‑Web Cross‑Check Across 791,635 DR1 Matched Spirals”

Scope of review
I evaluated the full 20‑page manuscript for methodological rigor with emphasis on statistical validity, internal arithmetic consistency, clarity of estimator definitions, null procedures, and traceability of all headline numbers. I re‑computed all sigmas, ranges, and simple ratios that are numerically determined by quantities shown in the text/tables.

Overall assessment
The analysis is carefully executed in many places, and most of the numerics I could recompute from the displayed inputs check out. However, there are several essential inconsistencies, one clear numerical impossibility, and a few places where the statistical framework is under‑specified or contradictory. The most serious issues are (i) an internal contradiction in program‑split results, (ii) an impossible sample size quoted in the Phase‑2 discussion, (iii) a units inconsistency already in the abstract, and (iv) use of an external “monopole prediction” without proper uncertainty propagation while sometimes switching to a different in‑sample monopole baseline. In addition, the “primary” estimator designation is explicitly post‑hoc. These must be fixed before the paper can meet PRD standards.

Findings

ESSENTIAL

P5‑E1 (Abstract, p.1): Units inconsistency in Phase‑2 headline
- Offending text: “the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3)”.
- Problem: 0.22 percentage points equals 0.0022 in absolute fraction. Writing “max 0.0022” immediately after “percentage points” mixes units within the same parenthetical.
- Required fix: State the maximum once, consistently: either “0.22 percentage points” or “0.0022 in absolute fraction,” not both. Propagate the same unit convention throughout the manuscript and figure captions (check Table VI and Fig. 5 text).

P5‑E2 (Phase 2 sensitivity sweep, pp.9–10): Impossible sample size for sigma computation
- Offending text: “The largest single‑cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152).”
- Problem: The chirality‑relevant matched‑spiral sample contains 791,635 galaxies (Table I). No class count can exceed this. Reporting n = 3.70×10^6 for any chirality sigma is impossible given the defined sample. This undermines the stated σ = 11.32 and any inference drawn from it.
- Required fix: Correct the sample size and the associated σ. If this number refers to something other than the chirality‑relevant set (e.g., the parent DR1 spectroscopic counts used to build the field), state that explicitly and remove any σ computation that uses a population without CW/CCW labels.

P5‑E3 (Systematics, p.17, §XI vs earlier §VI D.b, p.7): Direct contradiction in program‑split results
- Offending texts:
  • §XI: “target‑class split (BGS vs. LRG‑ELG‑QSO) with BGS‑only CW fraction within ±0.001 of LRG‑ELG‑QSO.”
  • §VI D.b: “bright (BGS‑dominated; n = 775,760) fCW = 0.4970 … dark (LRG, ELG, QSO; n = 14,782) fCW = 0.5051.”
- Problem: 0.4970 vs 0.5051 differs by 0.0081 (0.81 percentage points), not “within ±0.001.” These two statements cannot both be true for the same dataset.
- Required fix: Resolve and correct. If §XI used a different cut or sample, specify precisely, report the matching sample sizes, and reconcile the two results numerically. Otherwise, correct §XI and adjust any downstream interpretations (including the claim that “no test produces a > 3σ residual after Paper IV‑monopole correction”).

P5‑E4 (Use of external “monopole prediction,” multiple sections): Baseline inconsistency and missing uncertainty propagation
- Offending texts:
  • §V: “We explicitly compare … against the Paper IV‑predicted classifier‑monopole offset … ∆fCW = −0.0026.”
  • §VIII F/Table X: “after subtracting the P5 matched‑spiral catalog monopole fP5CW = 0.4972 …”
- Problems:
  1) Two different baselines are used (Paper IV’s −0.0026 and this paper’s in‑sample −0.0028), each driving different σpred values. In Table X you switch to the in‑sample monopole but still refer to “P4‑monopole subtraction” elsewhere.
  2) In all places where you subtract a “monopole,” there is no propagation of the uncertainty in that baseline into residual significances; yet you draw significance conclusions on the residuals (e.g., |σvs monopole| < 1.15).
- Required fix: Choose a single baseline for all residual/”vs‑monopole” calculations in the main text (preferably the in‑sample fP5CW for internal consistency), define it once with its uncertainty, and propagate that uncertainty into any per‑class residual significance claims. Where Paper IV’s value is used, move it to a secondary cross‑check and include its reported uncertainty. Revise all σpred and σvs‑monopole numbers accordingly. Make the formula used in Table X explicit.

P5‑E5 (Section VI A, p.8; §VI D.d, p.8): Non‑quantitative p‑value reporting (“p < 10−1000”)
- Offending text: “χ^2 = 4932, 3 d.o.f., p < 10−1000.”
- Problem: This is not a meaningful p‑value report. State an actual p‑value (or an upper bound within numerical precision) computed from the χ^2 distribution. Hyperbolic expression “< 10−1000” is not acceptable for PRD.
- Required fix: Report the computed p‑value to a reasonable floor (e.g., p < 10−300 if this is the machine‑precision lower bound) and the method/library used. Alternatively, report only the χ^2 and state “p-value effectively zero within double‑precision.”

P5‑E6 (Multiple places; Table V/HEALPix p‑values and σ’s): Explicit comparability of different null procedures
- Observation: The manuscript juxtaposes raw σfrom‑half values (parametric Normal scaling) with permutation‑based p‑values (label‑shuffle) and with Bonferroni thresholds derived from Gaussian tails.
- Problem: In several places these appear side‑by‑side without an explicit reminder that the parametric σ and the empirical permutation p are not directly interchangeable statistics (e.g., Table V caption and the surrounding text).
- Required fix: Add explicit wording wherever parametric |σ| thresholds and permutation‑based p‑values are shown together (HEALPix scans, density quintiles, Phase‑2 per‑cell statements) to note they are different null procedures and are not directly comparable. Clarify which is primary for each analysis and use a single procedure when declaring pass/fail against a threshold.

P5‑E7 (Data/code availability, Appendix B, p.19): Missing persistent link/DOI for “companion data repository”
- Offending text: “Analysis drivers are available in the companion data repository.” and “available in the companion data repository.”
- Problem: No URL or DOI is provided. PRD reproducibility requires an accessible, persistent resource.
- Required fix: Provide a persistent DOI (Zenodo or similar) or a public URL for the exact code and data snapshots used to produce the results, and ensure the repository includes the stated config and seeds.

P5‑E8 (Abstract and Conclusions): Strength of claim vs. post‑hoc “primary” choice
- Offending text: “Primary analysis path… We designate the DESIVAST‑anchored void cross‑check … as the primary … the headline‑result statement therefore rests on …”
- Problem: The choice of “primary” is explicitly post‑hoc (§V B), which means that headline significance should be treated with additional caution due to analysis selection. The abstract and conclusions present the null as a robust result without reflecting this selection.
- Required fix: In the abstract and conclusion, qualify the headline result to note that the designated “primary” analysis path was chosen post‑hoc and that multiplicity/selection does not inflate Type I error here because the result is a null. If you keep any positive detection claims (you do not), you would need to adjust for selection. As it stands, make the selection caveat explicit in the abstract.

MAJOR

P5‑M1 (Section V, p.4): “exact binomial 95% credible interval” terminology
- Offending text: “exact binomial 95% credible interval,” “Jeffreys binomial credible intervals.”
- Problem: Jeffreys intervals are Bayesian credible intervals with Beta(1/2,1/2) prior; they are not the “exact” Clopper‑Pearson intervals. The wording is internally inconsistent.
- Required fix: Replace “exact” with “Jeffreys (Beta(1/2,1/2)) 95% credible intervals.” If you use Clopper‑Pearson anywhere, specify that instead.

P5‑M2 (Redshift dependence, p.6): Underdocumented logistic regression
- Offending text: “A logistic regression … gives a z‑coefficient of 0.0059 with no significant intercept (0.000652) …”
- Problem: Missing model specification details (covariates exactly, standard errors, z‑scores/p‑values, link function confirmation, sample size used, handling of class weights). The coefficient’s scale is uninterpretable without these.
- Required fix: Report the regression formula, coefficients with standard errors and p‑values, sample size, and whether robust/clustered errors were used. Otherwise, remove the regression and keep the permutation test.

P5‑M3 (Survey‑mask dilation, §IV A.5, p.3): Reproducibility of masking step
- Offending text: “Build a survey‑footprint mask by dilation of occupied cells: 2,417,697 occupied → 3,150,086 in‑mask …”
- Problem: The dilation kernel, number of iterations, and boundary conditions are unspecified; this step can materially affect class fractions and assignments.
- Required fix: Specify the dilation operator in full (structuring element, iterations, padding behavior) or provide code. State how sensitive your in‑mask counts are to this choice.

P5‑M4 (Cosmology parameters, scattered, e.g., §IV A.2 vs §VIII A): Inconsistent/unspecified cosmology
- Offending text: “Planck 2018” (no parameters) vs later “H0 = 67.66 km/s/Mpc, Ωm = 0.315.”
- Problem: The fiducial cosmology must be stated once and used consistently for all comoving conversions.
- Required fix: Declare the full set of cosmological parameters (H0, Ωm, ΩΛ) used everywhere near §IV A and ensure later sections reference the same values.

P5‑M5 (Position‑shuffle null, §V, p.4): Defined but never reported
- Offending text: “(ii) a position‑shuffle that preserves labels but scrambles positions. Both nulls draw NMC = 1000 …”
- Problem: Later sections report only the label‑shuffle results; the position‑shuffle null is never shown, so its utility is unclear.
- Required fix: Either report the position‑shuffle results alongside label‑shuffle where introduced (HEALPix, density, redshift) or justify why it was not used further.

P5‑M6 (Novelty claims, various): “largest matched‑sample environmental‑dependence test … to date”
- Offending text: §VIII B: “This … is the largest matched‑sample environmental‑dependence test … in DESI DR1 to date …”
- Problem: This claim needs a citation or should be softened; there are concurrent catalogs and analyses (e.g., ASTRA, T‑Web, other cross‑checks).
- Required fix: Either add a citation supporting the “largest” claim or rephrase to “to our knowledge … within DR1 matched‑spiral samples of this kind.”

MINOR

P5‑n1 (Notation, many places): “wall” vs “sheet”
- Problem: You alternate between “wall” and “sheet” for the same V‑/T‑Web class. This can confuse readers.
- Fix: Choose one term and note the correspondence once.

P5‑n2 (Helpful explicit formulas): σvs‑monopole definition
- Problem: Table X shows “σvs monopole” but the exact formula (σobs − σpred with σpred computed from which baseline) is not stated where the table appears.
- Fix: Add the definition of σvs‑monopole in the table caption.

P5‑n3 (Clarity, §VIII A, p.10): The “0/6 V‑Web void spirals” statement
- Problem: The sample size is extremely small; although you acknowledge it, adding the exact sky coverage and redshift window here would help frame the limitation.
- Fix: Briefly state the sky‑area overlap fraction and that only 6 of the 428 V‑Web voids fall at z ≤ 0.24 in the matched sample.

P5‑n4 (Typographic consistency): Consistent use of “pp”
- Problem: Sometimes you write “0.2 pp,” elsewhere “0.002” (fraction). Mixing occurs even within the same sentence (see P5‑E1).
- Fix: Standardize to either fraction or “percentage points,” and include a note in the notation section.

NIT

P5‑N1 (Hyper‑precise significant digits): Reported CIs and σ to 2–3 s.f.
- Suggestion: Round σ and fractions to 2–3 significant figures consistently.

P5‑N2 (Rhetorical emphasis): “garden‑of‑forking‑paths” language
- Suggestion: Replace with neutral phrasing acceptable for PRD style.

P5‑N3 (Punctuation/typography): Occasional em‑dash/excess hyphenation artifacts
- Suggestion: Clean up typesetting (e.g., “sensi‑ tivity”, “clas‑ sifier”) before final submission.

Arithmetic audits that check out (no action requested)
- Table I totals, SPECTYPE, leg sums, and deduplicated counts are internally consistent.
- Table II σ values recompute exactly from n and nCW; class‑range 1.98 pp is correct.
- Density‑quintile σobs, σpred (from ∆f = −0.0026) and residuals are consistent; Bonferroni‑5 threshold 3.09 correct.
- HEALPix NSIDE 16/32/64 max‑|σ| and permutation p‑values are self‑consistent; reported p99 values (4.50, 4.78, 4.77) are plausible for NMC = 1000.
- DESIVAST void vs non‑void table (Table VII): σ computations verify; differences are at the stated 0.07 pp level.
- Three‑algorithm DESIVAST robustness (Table VIII) σ values and Δf are consistent.
- HEALPix maximal‑void stratification (Table IX): σ values recompute; Paper‑IV‑monopole residual estimates are numerically consistent.
- Tempel+2014 overlap (Table XI): σ values check out; class‑pair differences cited are consistent.
- Pearson r = 0.006, p = 0.88 (Fig. 6) is consistent with stated pixel counts.

Length
The paper is long for the (ultimately null) result, in part due to extensive cross‑checks. If the authors can fix the essential issues, a modest condensation would strengthen the presentation. A target of ~14–16 pages main text (moving some diagnostic scans to an ancillary file with a DOI) would be appropriate.

## Summary recommendation
MAJOR REVISIONS

The core analysis is promising and many numerics check out, but there are several essential issues that must be corrected: an impossible sample size and σ in the Phase‑2 section; a direct contradiction between program‑split summaries; unit inconsistency in the abstract; and inconsistent handling of the monopole baseline with no uncertainty propagation. Additionally, p‑value reporting and null‑procedure comparability require clarification, and reproducibility needs a concrete repository link. Addressing these items should be feasible and would bring the paper up to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-pass audit)

ESSENTIAL

P5‑E9 (Section VI D.c, p.7): Impossible filament bright count exceeds total filament
- Offending text: “filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85 …”
- Problem: The total filament count in Table II is nfilament = 408,187. Reporting filament‑bright n = 416,701 already exceeds the class total, before adding dark/backup/other. This is numerically impossible and indicates a copy/paste or filtering error that undermines the program‑split filament results and any z‑tests built on them.
- Required fix: Recompute all per‑program filament counts and sigmas from the same filtered sample used in Table II; report bright + dark + backup + other that sum exactly to 408,187. Recompute the quoted |z| ≈ 3.4 as well.

P5‑E10 (Eq. 1, p.4): Algebraic inconsistency in σpred formula (missing parentheses)
- Offending text: “σpred = ∆fCW/0.5/√N = 2 · ∆fCW · √N”
- Problem: As typeset, ∆f/0.5/√N = 2∆f/√N, which is not equal to 2∆f√N. The intended expression is σpred = (∆fCW)/(0.5/√N) = 2∆fCW√N; the current form is dimensionally and numerically inconsistent.
- Required fix: Insert parentheses and correct the equality: σpred = ∆fCW / (0.5/√N) = 2∆fCW√N. Audit every place σpred is computed to ensure the correct form was used in code and text.

P5‑E11 (Internal cross‑reference, §VIII “RSD treatment for DESIVAST,” p.10): Wrong section reference
- Offending text: “This is in contrast to the V‑Web secondary path (§XIII) …”
- Problem: §XIII is “Limitations,” not the V‑Web secondary path description. This misreference makes it hard to trace the argument.
- Required fix: Point to the correct section where the V‑Web pipeline is actually defined (likely §IV and/or §VII).

MAJOR

P5‑M7 (Table X, §VIII F, p.13): Mixed definitions in the same table (fraction difference vs sigma difference)
- Offending presentation: Column “fCW − fP5CW” is a fraction difference relative to the in‑sample monopole, while “σvs monopole” is evidently computed as σobs − σpred (sigma difference), not as the z‑score of the fraction difference.
- Problem: Two different residual definitions are juxtaposed without stating that they arise from different normalizations. This impedes reproducibility and invites misinterpretation.
- Required fix: State explicitly in the caption: (i) σvs‑monopole ≡ σobs − σpred, with σpred = 2∆fP5CW√N; (ii) do not suggest that σvs‑monopole is the z‑score of (fCW − fP5CW). Alternatively, add a column giving the z‑score of (fCW − fP5CW) using the binomial SE, and keep σobs − σpred as a separate diagnostic.

P5‑M8 (ASTRA entropy‑weighted σ, §X/Table XII, p.16): Non‑binomial variance treated as binomial‑style σ without derivation
- Offending text: “ASTRA entropy‑weighted classifier … sub‑class variance Pi^2/4 under the Bernoulli‑0.5 null … max |σ|vs 1/2 reported alongside V‑Web binomial σ.”
- Problem: The entropy‑weighted estimator is not binomial; its variance formula is only sketched and not derived. Reporting “σ” for this estimator next to binomial σ (V‑Web) implies comparability that is not established.
- Required fix: Provide a derivation or a bootstrap for the entropy‑weighted estimator’s standard error and make clear that its “σ” is not directly comparable to the binomial σ. Prefer permutation/bootstrap p‑values for ASTRA to avoid parametric miscalibration.

P5‑M9 (§IV A.7 vs §IV A.12, p.3): Inconsistent field being interpolated (“δ” vs “log‑density”)
- Offending text: Step 7: “Gaussian‑smooth δ”; Step 12: “NN‑interpolate the per‑cell label + smoothed logdensity to each galaxy.”
- Problem: You never define a log‑density field; the pipeline smooths δ. “Smoothed logdensity” is inconsistent with the stated procedure and could affect within‑class density stratifications.
- Required fix: Clarify whether you smooth δ or log(1+δ). If the latter, restate the full method; if the former, correct the wording and audit any analyses that used “smoothed logdensity.”

P5‑M10 (§VIII F, p.12): Underspecified “env‑class uncertainty filter” producing the 812,793 superset
- Offending text: “relaxed env‑label confidence … excluded from the headline by a stricter env‑class‑uncertainty filter.”
- Problem: The filtering criterion (metric, threshold) is not defined, yet it changes the working sample size by ~21k objects and underlies the monopole used in Table X.
- Required fix: Specify the per‑object environment‑label confidence measure, the threshold(s), and show how the 812,793 set maps to the 791,635 headline sample.

MINOR

P5‑n5 (Stale/discordant σpred for filament, §VI A vs §VII A): −3.16 vs −3.32
- Offending text: §VI A: “σpred(filament) ≈ −3.16”; §VII A: “σpred … 3.32σ (filament) at canonical populations.”
- Problem: For N = 408,187 and ∆f = −0.0026, σpred = −0.0052√N = −3.32. The −3.16 value appears stale/inconsistent.
- Fix: Harmonize throughout; audit all quoted σpred values.

P5‑n6 (Contingency result, §VI D.d, p.8): Max deviation misquoted
- Offending text: “max class‑to‑overall bright‑fraction deviation 1.5 pp” with per‑class bright fractions {0.981, 0.962, 0.966, 0.989} and overall 0.978.
- Problem: The largest absolute deviation is |0.962 − 0.978| = 1.6 pp, not 1.5 pp.
- Fix: Correct to 1.6 pp or provide unrounded inputs.

P5‑n7 (Poisson normalization, §IV A.8, p.3): Missing constants/normalization note
- Offending text: “Φ(k) = −δk/k^2.”
- Problem: While the overall scale cancels in a λth = 0 V‑/T‑Web classification, it is helpful for reproducibility to state explicitly that you adopt a dimensionless normalization (no 4πGa^2 factor), and that λth is therefore used in a purely geometric sense.
- Fix: Add a one‑sentence note on the chosen normalization and its implications for λth.

P5‑n8 (Ngrid notation): Inconsistent superscripting
- Observation: “Ngrid = 2563” appears in some places; elsewhere “Ngrid = 256 × …”.
- Fix: Standardize to “Ngrid = 256^3” throughout (including Table VI caption).

P5‑n9 (§VIII B, p.11): KDTree neighbor count justification
- Offending text: “k = 20 nearest‑neighbour KDTree … sufficient given the 24 Mpc/h maximum hole radius.”
- Problem: Sufficiency is asserted, not shown. If centers can be sparse, 20 neighbors may not guarantee inclusion of the containing sphere.
- Fix: State the empirical minimum number of centers within 2Rmax across the volume (or implement an explicit radius search); otherwise, justify k = 20 with a coverage check.

P5‑n10 (Figure/body clarity): Distinguish clearly between NSIDE = 16 and NSIDE = 32 occupied‑pixel counts
- Observation: §VIII E reports 297 occupied pixels at NSIDE = 16; Fig. 6 caption reports 885 occupied pixels at NSIDE = 32. Both are plausible but could confuse readers scanning quickly.
- Fix: Add explicit NSIDE labels in the main‑text sentences where these counts first appear.

NIT

P5‑N4 (Typo/formatting): Table VI header reads “Ngrid = 256 × λth …”
- Suggestion: Correct to “Ngrid = 256^3; λth ∈ {…}”.

P5‑N5 (Equation typography): Use parentheses consistently to avoid division‑order ambiguity, especially in Eq. (1) and any expression of the form a/b/c.

Explanation
This fresh audit focused on arithmetic consistency, equation dimensionality/typography, section cross‑references, and comparability of null procedures. The new essential items include a second numerically impossible count (filament bright > class total) and an algebraic inconsistency in the key σpred equation, both of which materially affect interpretation. Several additional major/minor issues concern mixed estimator definitions, an under‑documented filtering step, and internal stale numbers. These are distinct from, and in addition to, the issues already identified in the initial review.