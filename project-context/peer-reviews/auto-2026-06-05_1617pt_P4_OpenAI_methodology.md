# P4 auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (11751 chars)
**Wall time**: 465.7s

---

Referee report (Methodology/Statistics) for: “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, …”

Overall: I audited the full manuscript, recomputed quoted fractions and σ-values where possible, checked internal arithmetic, dimensional consistency, and the mapping between abstract/conclusions and the body. The analysis is ambitious, and many ingredients are documented; however, there are multiple internal inconsistencies, ambiguous definitions, and several claims that cannot be verified from the provided numbers. These must be corrected before the paper can meet PRD methodological standards.

Findings

ESSENTIAL

P4-E1 (Sec. IV.A, Table II; page 4) — Inconsistent σ computations and N used across tiers
- Offending text: “Uncertainties are 1σ binomial (σ = sqrt(p(1 − p)/N, Nspiral = 3,201,160). Dev. (σ): A(raw) 28.8; B(calibrated) 14.6; C(equivariant) 9.5.”
- Problem: Using Nspiral=3,201,160 for all three tiers while reporting different tier-wise deviations yields inconsistencies. Recomputing with N=3,201,160 gives for Tier A: (0.5079−0.5)/0.0002794=28.3σ, not 28.8σ. For Tier B: (0.504−0.5)/0.0002794=14.33σ, not 14.6σ. If you used different N for A and B, Table II’s footnote is incorrect; if you used N=3,201,160, the quoted devs are wrong.
- Required fix: Recompute and report exact deviations with the correct N for each tier, and correct the Table II footnote to specify the N actually used per tier. Provide the spiral counts (Nspiral) for Tiers A and B; do not reuse Catalog C’s Nspiral for other tiers.

P4-E2 (Sec. IV.B; page 4 and Appendix A; page 7) — Undefined/contradictory “asymmetry-suppression factor”
- Offending text: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates …”
- Problem: Nowhere in the main text is “+2.05%” defined or derived (global cw excess for A is +0.79%). Appendix A gives ⟨A⟩mask,gw = −0.005294 (−0.5294%), which corresponds to the −0.53%. The origin, definition, and calculation of the “+2.05%” are not shown. As written, this contradicts Table II and is not reproducible.
- Required fix: Explicitly define the statistic for both the +2.05% and −0.53% numbers (e.g., galaxy-weighted mask-mean asymmetry vs. global unweighted spiral fraction), show their computation (with N and masks), and correct the factor “3.86×” if needed. If +2.05% is not used elsewhere, remove it.

P4-E3 (Abstract; page 1; and Sec. VI.A; page 6) — Incorrect selection criterion for HC subsample
- Offending text: “471 049 high-confidence per-spiral after peqCW > 0.9” (abstract).
- Problem: A threshold on peqCW alone would asymmetrically select CW objects and bias any injection test. Elsewhere (Appendix E), you define HC cuts using max-class probability peq>0.6/0.8. The abstract’s criterion is inconsistent and, if taken literally, methodologically invalid.
- Required fix: Replace “peqCW > 0.9” with “max(peqCW, peqCCW) > 0.9” (or the exact rule you used), and ensure this criterion and the resulting N=471,049 are stated consistently everywhere an HC sample is used.

P4-E4 (Sec. IV.D; page 4 and Table IV; page 5 vs. Appendix C; page 8) — Conflicting hemisphere asymmetry significances
- Offending text: “local hemisphere maximum of 3.05σ” (Sec. IV.D); Table IV shows “Hemisphere max|A| … z=+4.42”.
- Problem: Two different σ-values are quoted for the hemisphere max statistic without explaining they refer to different nulls and/or setups. This is confusing and prevents verification.
- Required fix: Clearly distinguish the hemisphere statistic(s): define the estimator, mask, direction grid, and null for each case. Report both values side-by-side but explicitly label which null (random-label permutation, monopole-only, etc.) and why they differ. Provide the data value, the null mean and standard deviation for each, and the number of MC realizations.

P4-E5 (Appendix A; page 7) — Contradictory statement on C1 and σ after monopole subtraction, missing numbers
- Offending text: “Monopole subtraction reduces decoupled C1 at ℓ=1 from 2.30×10−5 to 1.51×10−5 (~34%) and increases σ from +1.85 to +3.64.”
- Problem: A smaller C1 achieving a larger σ implies the null mean/σ changed; those numbers are not given, and the masks differ by context in the paper (canonical vs. subsample). This is not verifiable as written and conflicts with Table III’s ℓ=1 value (1.494×10−6 for the subsample mask).
- Required fix: Provide the null mean and σ used to compute both +1.85σ and +3.64σ, and explicitly state which mask and field definition each C1 corresponds to (canonical vs. subsample; monopole-subtracted or not). Also provide the canonical-mask ℓ=1 C1 value used to obtain +3.64σ, so the change in σ can be checked.

P4-E6 (Multiple locations: Abstract p.1; Sec. IV.C–D pp.4–5; Conclusions pp.6–7) — Juxtaposition of σ-values from different nulls without an immediate caveat
- Offending text examples: “−0.122σ (subsample mask)… +0.43σ (real-space cross-check)” (abstract); “+3.64σ … 0.43σ … −0.122σ” (Conclusions b–c).
- Problem: Although the paper states once that σ-values are null-dependent and “not directly comparable,” PRD requires that whenever different-σ values are juxtaposed, the non-comparability be explicit to avoid misinterpretation.
- Required fix: Add an explicit parenthetical “(σ-values are from different null distributions and are not directly comparable)” at each location where multiple σ-values from different nulls are placed side-by-side (abstract, results summary paragraphs, and conclusions items b–c).

P4-E7 (Sec. IV.D; page 4) — Internal version-history language
- Offending text: “were interpreted in earlier paper versions as…”
- Problem: Version-history language must be removed from the body of a PRD submission.
- Required fix: Delete this phrase and any other internal development comments. Replace with a neutral, self-contained description of the current interpretation.

P4-E8 (Table III; page 5) — Missing null means for bandpower significances
- Offending text: Table III lists Cℓ and σnull and “Significance (σ)” for bandpowers, but does not list the null mean ⟨Cℓ⟩null used to compute z = (Cℓ − ⟨Cℓ⟩null)/σnull.
- Problem: Without the null mean for each bandpower, the quoted “+6.097σ,” “+2.232σ,” etc., cannot be verified.
- Required fix: Add the null means to Table III (or to a table footnote) for each band/bandpower reported, and state explicitly the mask and field for those values.

P4-E9 (Appendix D.a; page 8 and throughout) — Undefined “C 2 2◦ apodization” notation
- Offending text: “C 2 2◦ apodization” (also appears in main text).
- Problem: The apodization kernel is not standardly denoted “C 2 2◦”. This is ambiguous (cosine-squared? C2?).
- Required fix: Define the apodization explicitly in words and/or formula (e.g., cosine-squared apodization with 2° taper), and standardize the notation.

P4-E10 (Sec. IV.D; page 4; Appendix D.c,d; page 8) — Cross-spectrum rℓ and σ undefined
- Offending text: “C(Ap×ntotal) at ℓ=2 gives r=−0.65 with σ=−2.89 against permutation null.”
- Problem: rℓ is not defined (Pearson correlation? normalized cross-power?), the sampling distribution and NMC are not given, and the sign convention for σ (negative σ quoted) is unclear.
- Required fix: Define rℓ precisely, specify the normalization and binning, the null generation, number of MC realizations, and whether p-to-σ mapping is one- or two-sided. Report p-values alongside σ.

P4-E11 (Appendix D.f; pages 8–9) — Implausibly large z-values without covariance specification
- Offending text: “naive WLS posterior … z = −264.5 … block-bootstrap … inflates σ by 14.7×, reducing z to ≈ −18.1…”
- Problem: z=O(10^2) is not credible without full detail on the design matrix, noise model, spatial covariance, and diagnostic checks of the bootstrap estimator’s normality and stability. As written, these “z” values are not reproducible and likely overstate significance.
- Required fix: Provide the exact WLS setup (design matrix, weights, covariance), the bootstrap scheme (block size, resampling units, number of realizations), distribution diagnostics (QQ-plots or skew/kurtosis), and recompute conservative p-values. Alternatively, remove these σ-values and present effect sizes with uncertainties only.

MAJOR

P4-M1 (Abstract p.1; Appendix A.c p.7) — Ambiguous use of “n=5,547,858” for a weighted map count
- Offending text: “strict-superset subsample mask (n= 5,547,858, fsky=0.659)” and “Analysis subsample mask: fsky = 0.659, n = 5,547,858.”
- Problem: This “n” is Nmap,weighted = Σp Wp (all classes). Calling it “n” suggests a galaxy count and is confusing.
- Required fix: Replace “n” with “Nmap,weighted” consistently and restate the spiral-galaxy count separately.

P4-M2 (Sec. IV.B; page 4; Appendix A.a; page 7) — Mixing galaxy-weighted mask means with global fractions
- Offending text: uses both “0.4974” (global spiral cw-fraction) and “⟨A⟩mask,gw = −0.005294.”
- Problem: These are not commensurate, but are compared interchangeably.
- Required fix: Clearly distinguish and report both the global spiral cw-fraction and the galaxy-weighted mask-mean asymmetry for each mask/tier, and refrain from comparing them directly without noting the difference.

P4-M3 (Sec. IV.D; page 4; Table IV; page 5) — “99.3% reproduced” claim lacks uncertainty
- Offending text: “reproduced at 99.3% of its observed amplitude by a controlled monopole-only generative null”
- Problem: This is a ratio of two means; no uncertainty is provided.
- Required fix: Provide an uncertainty on the 99.3% figure (e.g., via error propagation from the MC standard error) and/or a confidence interval or a p-value for the observed-vs-null difference.

P4-M4 (Sec. III.C; page 3; Appendix B.c; page 7) — Justification for limiting TTA to horizontal flip only
- Offending text: “We restrict to 2-fold TTA … D4-TTA … argmax labels flip in 21.4% of cases between Z2 and D4 on borderline galaxies…”
- Problem: Given a 21.4% argmax instability on borderline objects, the choice to exclude rotational TTA needs a clear justification in terms of its effect on the asymmetry field A(n). It is not shown that excluding rotations cannot bias A(n).
- Required fix: Quantify the impact on the pixelized Ap map and on C1 when using Z2 vs D4 TTA (e.g., show ΔC1 and ΔA histograms), and justify the choice in terms of negligible bias on the cosmological estimators.

P4-M5 (Sec. II.B; page 2; Sec. III.B; page 3) — “GZ1 cross-match 234,282” likely misattributed
- Offending text: “The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91%.”
- Problem: GZ1 did not provide ~234k robust chirality labels; that scale is more consistent with Galaxy Zoo DESI or other catalogs. As written, this is not credible.
- Required fix: Identify the exact catalog used for the 234,282-object chirality labels (name, reference, and selection thresholds). If it is not GZ1, correct the citation and text and provide the per-threshold counts. If it is GZ1, document how many of those have chirality labels and how they were obtained.

P4-M6 (Table III caption; page 5; Sec. IV.C; page 4) — Joint χ2/dof reported without binning and covariance
- Offending text: “Joint χ2/dof (38 bandpowers) — 161.2/38 = 4.24”
- Problem: The number of bandpowers and the binning scheme are not specified, and the covariance model (including off-diagonals) is not described. With ℓmax=191 and nlb=1 cited elsewhere, “38 bandpowers” is unexplained.
- Required fix: Provide the full binning scheme used for the χ2 computation, and describe the covariance matrix estimation. If using diagonal-only covariance, state so and caution that χ2/dof is not a full goodness-of-fit.

P4-M7 (Multiple locations; e.g., Abstract p.1; Sec. IV.D p.4; Appendix D.f p.8) — One- vs two-sided p-to-σ mapping is inconsistent
- Offending text: “pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent” (would be ≈2.17σ two-sided); “family-corrected p=0.0086 (≈2.4σ family-wise)” (two-sided 0.0086 ≈ 2.64σ).
- Problem: The mapping is alternately one-sided and two-sided without being stated, leading to inconsistent σ translations.
- Required fix: State your convention (one- or two-sided) and apply it consistently to all Gaussian-equivalent σ in the paper. Report p-values alongside σ to avoid ambiguity.

P4-M8 (Abstract p.1; Sec. VI.A p.6; Conclusions d p.6) — “Falsification criterion” mixes detection amplitude and σ thresholds
- Offending text: “A future survey detecting a chirality dipole at σ >5 with full amplitude ≳ 0.75% … would falsify the present null.”
- Problem: 0.75% is your 50%-recovery-at-3σ threshold on a particular HC subsample. Tying a >5σ detection criterion to that amplitude floor is not principled as a general falsification statement.
- Required fix: Rephrase as an illustrative statement tied to your pipeline and sample (e.g., “Under our pipeline and null, amplitudes ≥0.75% would be detected at ≥3σ in the HC subsample; a future ≥5σ detection at comparable or lower amplitude would be in tension with our null”). Or provide a principled falsification bound derived for the full sample.

P4-M9 (Multiple; e.g., Abstract p.1; Appendix A.c p.7) — “strict-superset subsample mask” unclear
- Offending text: “strict-superset subsample mask”
- Problem: It is not defined which mask is a superset of which, and by what rule.
- Required fix: Define both the “canonical” and “subsample” masks, and precisely state which pixels are included in each and how one is a superset/subset of the other.

P4-M10 (Sec. IV.C.a; page 4) — Isotropic-bootstrap real-space null not specified
- Offending text: “p = 0.30, isotropic-null bootstrap, NMC = 10,000”
- Problem: The resampling unit (galaxies? pixels?), whether survey-depth is preserved, and the bootstrap procedure are not described.
- Required fix: Provide a clear description of the bootstrap (resampling scheme, preservation of pixel weights, any stratification), and the estimator used in each resample.

P4-M11 (Sec. VI.A; page 6) — Injection-recovery needs details and uncertainties
- Offending text: “50%-recovery-3σ threshold at A ≈ 0.75%, above the Fisher floor…”
- Problem: The injection model (how Adipole is applied per pixel/galaxy) and uncertainties on the 50% point are not given.
- Required fix: Describe the injection procedure, show a recovery curve with confidence intervals, and provide the uncertainty on the 50%-at-3σ threshold.

P4-M12 (Appendix E.a; page 9) — Edge-on contamination percentage lacks details
- Offending text: “65.7% of b/a<0.3 objects receive CW or CCW classifications…”
- Problem: No sample size, b/a source, or uncertainty is given.
- Required fix: Provide the counts, source of b/a, and uncertainties; or move to supplementary material.

MINOR

P4-N1 (Front matter; page 1) — PACS numbers
- Offending text: “PACS numbers: …”
- Required fix: PRD no longer uses PACS; remove or update to current indexing if required by the journal.

P4-N2 (Throughout) — Formatting/terminology consistency
- Examples: “un-monopole-subtracted,” “NaMaster MASTER,” “canonical-N MASTER direct compute.”
- Required fix: Standardize terminology and hyphenation; use “NaMaster/MASTER” once; avoid awkward phrases like “direct compute.”

P4-N3 (Table IV; page 5) — Undefined “NSIDEdir = 8”
- Offending text: “Hemisphere max|A| (NSIDEdir = 8)”
- Required fix: Define “NSIDEdir” (grid of directions for hemisphere splits) and justify the choice.

P4-N4 (Units in tables; Table III p.5; Table IV p.5) — Cℓ units and formatting
- Offending text: “Cℓ × 10^6 (sr)”
- Required fix: Clarify the units (dimensionless Cℓ; if multiplied by 10^6 sr, explain the convention) and apply consistently.

P4-N5 (Sec. V.A; page 5) — “30× extension” ambiguous baseline
- Offending text: “(30× extension)”
- Required fix: State the baseline sample size you are comparing against (e.g., Shamir 2012’s 1.27×10^5) and compute the exact factor, or remove the parenthetical.

P4-N6 (Appendix A.c; page 7 vs. Appendix D.a; page 8) — Apodization description inconsistency
- Offending text: Appendix A: “Apodization: none on the canonical mask”; Appendix D.a reports an apodization test on the canonical mask.
- Required fix: Clarify that an apodized-mask robustness test was also run on the canonical mask and state the exact configuration in Appendix A.

P4-N7 (Sec. II.A; page 2) — “dr8 id identifiers” redundancy
- Required fix: Edit for clarity (“unique dr8_id identifiers”).

P4-N8 (Sec. V.B; page 5) — “cw/ccw = 0.998”
- Required fix: Clarify this is the cw-to-ccw ratio (i.e., cw fraction ~0.499), to avoid ambiguity.

Length
- The paper is 10 pages; not excessive. However, several appendices contain load-bearing methodology (e.g., Appendix D). Consider moving essential definitions (mask definitions, null descriptions) from appendices into the main Methods/Results sections for clarity.

Bibliography
- Spot checks of years and arXiv IDs appear plausible; however, ensure the “Galaxy Zoo 1” vs “Galaxy Zoo DESI” citations are correct where the 234k cross-match is discussed (see P4-M5).

Abstract accuracy
- The abstract mostly reflects reported results; however, the HC selection criterion is incorrect (P4-E3), and the “asymmetry-suppression factor” language is unclear without definitions (P4-E2). Fix both.

## Summary recommendation
MAJOR REVISIONS

There are multiple essential methodological clarifications and numerical inconsistencies that must be fixed (notably the tier-wise σ calculations, the hemisphere-statistic discrepancy, the HC selection criterion, undefined/apparent contradictions in C1 and σ after monopole subtraction, missing null means for reported bandpower significances, and undefined/ambiguous notations and nulls). Several claims of very high σ in the systematic template fits are not reproducible from the given information and should either be fully documented or toned down. With these corrections and clearer, fully specified null procedures and mask definitions, the paper could meet PRD standards; as submitted, it does not.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

I re-checked the manuscript line-by-line against classes A–J. Below are only NEW issues not already listed in my initial report. Numbering continues from prior IDs.

ESSENTIAL

P4-E12 (Sec. II.B; page 2) — Training-label counts don’t sum; derived percentage inconsistent
- Offending text: “(1) GZ1: 6,637; (2) CE-ResNet: 17,153; (3) Synthetic: 2,000… The combined training set contains 26,636 images… 67.6% of training labels derive from CE-ResNet predictions.”
- Problem: 6,637 + 17,153 + 2,000 = 25,790, not 26,636. Using your stated total 26,636, the CE-ResNet fraction is 17,153/26,636 = 64.4%, not 67.6%. Using 25,790, it’s 66.5%.
- Required fix: Correct the component counts and the combined total; recompute and report the correct CE-ResNet percentage. If there are additional sources, list them and provide exact counts.

P4-E13 (Table II; page 4) — Catalog C σ-value miscomputed
- Offending text: “C (equivariant) 0.4974 ± 0.000279 … Dev. (σ) 9.5.”
- Problem: |0.4974 − 0.5| / 0.0002794 = 9.31σ, not 9.5σ. My earlier P4-E1 covered A and B tiers; this additionally flags C’s number specifically.
- Required fix: Recompute and correct the deviation for Tier C.

P4-E14 (Table IV; page 5) — z-scores inconsistent with tabulated means/σ
- Offending text: Pre-MASTER pseudo-C(ℓ=1)ℓ data 1.696×10−2; null (1.685 ± 0.007)×10−2; “+1.68σ”. Hemisphere max|A| data 3.48×10−3; null (1.69 ± 0.41)×10−3; “+4.42σ”.
- Problem: Using the provided numbers: (0.01696−0.01685)/0.00007 = 1.57σ, not 1.68σ; and (3.48−1.69)/0.41 = 4.37σ, not 4.42σ.
- Required fix: Correct the reported z-scores or the null mean/σ entries to be mutually consistent. Provide at least three significant figures for null means and σ to avoid rounding artifacts.

P4-E15 (Sec. VI.A; page 6) — Fisher floor arithmetic internally inconsistent; unexplained fsky
- Offending text: “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”
- Problem: σ(A/2)=0.048% implies σ(A)=0.096%, which back-solves to Neff ≈ 1.08×10^6. But Nspiral × fsky = 3.201×10^6 × 0.46 ≈ 1.47×10^6, which would give σ(A)=0.082% and σ(A/2)=0.041% (3σ ≈ 0.25%), not 0.29%. The fsky=0.46 value also appears nowhere else.
- Required fix: Show the exact derivation of the Fisher floor, define Neff, justify fsky=0.46, and correct the 0.29% if needed.

P4-E16 (Appendix A.a,c; page 7 vs. Sec. IV.C; page 4) — Field definition inconsistency (fCW−0.5 vs Ap; ambiguous “Ntotal”)
- Offending text: “uses a single declared data vector: fCW(n̂)−0.5…” and later “Field: Ap = (NCW − NCCW)/Ntotal … with galaxy-weighted mask-mean subtraction.”
- Problem: In the main text Ap is defined with denominator NCW+NCCW (spirals only). In Appendix A, “Ntotal” is used ambiguously just after introducing Nall = NCW+NCCW+NNS for weights. It is unclear whether “Ntotal” means NCW+NCCW or all classes. There is also a mismatch between stating the estimator uses fCW−0.5 vs Ap.
- Required fix: Unambiguously define the exact field used for each analysis (fCW−0.5 or Ap), and explicitly define denominators (spiral-only vs all-classes) wherever “Ntotal” appears. Ensure the same field definition is used consistently across sections.

P4-E17 (Sec. IV.D; page 4 vs. Conclusions; pages 6–7) — Contradiction about MASTER “removing” leakage
- Offending text: “MASTER decoupling removes the canonical-mask pseudo-Cℓ leakage… The post-MASTER canonical-mask residual is +3.64σ…”
- Problem: “Removes” is contradicted by the reported +3.64σ post-MASTER canonical-mask residual. The current text oscillates between “removes” and “does not fully invert.”
- Required fix: Rephrase to accurately reflect that MASTER reduces but does not eliminate leakage on the canonical footprint; specify quantitatively the before/after amplitudes under the same mask and field.

P4-E18 (Sec. IV.E; page 5 vs. Appendix E.b; page 9) — Conflicting σ for peq > 0.6 cuts
- Offending text 1 (Sec. IV.E): “cutting to peq > 0.6 gives −0.03σ.”
- Offending text 2 (Appendix E.b): “collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict).”
- Problem: These disagree unless they refer to different estimators/nulls (e.g., canonical-mask ℓ=1 vs real-space dipole, or monopole-preserving vs demonopole). As written, readers cannot reconcile the values.
- Required fix: Explicitly state the estimator and null for each σ. If they are different, present them side-by-side with labels.

P4-E19 (Multiple: Sec. IV.D; pages 4–5; Appendix D.f; page 8) — “Amplitude ∼1.7%” not derived
- Offending text: Interpretation (i) uses a “clean dipole at amplitude ∼1.7%” as a reference.
- Problem: The 1.7% amplitude is used repeatedly without a derivation or a pointer to where it is computed from the data.
- Required fix: Show explicitly how 1.7% is obtained (estimator, mask, field, and mapping from C1 to full-amplitude), or remove the specific number.

P4-E20 (Table III; page 5) — Implied negative null mean for the ℓeff=4 band
- Offending text: “ℓeff = 4: Cℓ = 3.210; σnull = 0.804; Significance +6.097σ.”
- Problem: This implies ⟨Cℓ⟩null = 3.210 − 6.097×0.804 ≈ −1.697 (in the table’s units), i.e., a negative null mean power. Without the null means (see previous P4-E8), this looks unphysical for an average over MC realizations from random labels.
- Required fix: Add the null means (per P4-E8) and explain how a negative null mean arises (estimator bias, deconvolution ringing, or bookkeeping/units). If this is a computation or reporting error, correct it.

P4-E21 (Sec. IV.C.a; page 4) — Unverifiable “+6.48σ in the lowest bandpower” for Catalog A
- Offending text: “Catalog A (raw) shows … +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower…”
- Problem: No table or numbers are provided to reproduce this 6.48σ; and the nearest table (Table III) lists +6.097σ for a different setup/mask. As written, the 6.48σ is not verifiable.
- Required fix: Provide the exact bandpower value, null mean and σ, mask, and field used to compute +6.48σ (or correct the number).

MAJOR

P4-M13 (Appendix A.a; page 7) — Weighting the spiral-only field by Nall (all classes) needs justification and robustness check
- Offending text: “The NaMaster weight map assigns Wp = Nall … The asymmetry field is Ap (spirals only).”
- Problem: Weighting a spiral-only field by all-classes depth can couple non-spiral spatial systematics into the variance and residual mode-coupling. It’s nonstandard and could bias uncertainties and bandpower mixing.
- Required fix: Justify Wp = Nall vs Wp = Nspiral and provide a robustness check (e.g., re-run with Wp = Nspiral and report ΔC1, Δσ).

P4-M14 (Multiple) — Unjustified heterogeneity in NMC and seeds; no stability analysis
- Offending text: NMC varies (500, 1,000, 5,000, 10,000), seeds sometimes specified (42), often not.
- Problem: Reported σ can be sensitive to NMC; seed dependence hinders reproducibility checks.
- Required fix: Provide a stability test of key σ-values vs. NMC (e.g., 500→5,000) and report Monte Carlo standard errors or confidence intervals. Standardize seed reporting or omit seeds if not critical.

P4-M15 (Appendix C vs. Table IV; pages 8 and 5) — Direction-count mismatch for hemisphere LEE
- Offending text: “NSIDEdir = 8” (which implies 12×8^2 = 768 directions) vs. “∼ 650 tested directions” used for Bonferroni/BH.
- Problem: The discrepancy is unexplained (antipodal pairing? mask cuts?).
- Required fix: State the exact number of hemisphere centers evaluated, how antipodal redundancy was handled, and why the LEE correction used ~650 (not 768).

P4-M16 (Sec. II.A; page 2) — Selection-function inheritance not reproducible as stated
- Offending text: “The parent-sample selection function inherits from Galaxy Zoo DESI: photometric types REX/DEV/EXP/SER, r ≤ 19.0, half-light radius ≥ 3″.”
- Problem: This is not a direct description of a precise query/selection. Without exact SQL-like cuts, counts per class, and source tables, this is not reproducible.
- Required fix: Provide the exact selection criteria applied (catalog columns, thresholds, logical operators) and resulting counts.

P4-M17 (Appendix A.c vs. elsewhere; page 7) — Canonical vs. subsample mask construction unclear/redundant
- Offending text: “Mask: canonical Catalog C mask (pixels with ≥10 spirals). Analysis subsample mask: fsky = 0.659 … Canonical-N mask: fsky = 0.49005…”
- Problem: If the canonical mask is “pixels with ≥10 spirals,” it’s unclear how the subsample mask (with larger fsky) is constructed and why “canonical” then has smaller fsky. The descriptive labels are confusing.
- Required fix: Precisely define each mask (pixel threshold, apodization, any additional cuts) and explicitly state the subset/superset relationship.

MINOR

P4-N9 (Multiple: Sec. VI.A; Appendix A.c; Appendix D.a) — Inconsistent fsky values without context
- Offending text: fsky = 0.46 (Fisher floor), 0.49005 (canonical), 0.482 (apodized), 0.659 (subsample mask).
- Problem: The proliferation of fsky values with no summary table makes it hard to track which analysis uses which footprint.
- Required fix: Add a single summary table listing fsky per estimator/mask and a short justification for each footprint.

P4-N10 (Appendix B.d; page 7) — Vague “confidence calibration (qualitative, < 50% at confidence > 0.9)”
- Problem: This statement is unclear: what metric is “< 50%”? coverage? overconfidence rate?
- Required fix: Specify the calibration diagnostic (e.g., reliability diagram, ECE), what “< 50%” refers to, and provide a quantitative plot/table.

P4-N11 (Appendix D.f; page 8) — Unit mapping for Abest_dipole ambiguous
- Offending text: “Abest_dipole = 4.55 × 10−3 (0.23% in fCW units)”
- Problem: This relies on the factor-of-two mapping between A and fCW (A = 2(fCW − 0.5)) but is not restated here.
- Required fix: Add a parenthetical reminding readers of the A↔fCW factor-of-two mapping to avoid confusion.

P4-N12 (Appendix C; page 8) — “Monopole-preserving dipole” not defined
- Problem: This phrase appears without a definition, and multiple dipole estimators are in play.
- Required fix: Define “monopole-preserving dipole” explicitly (estimator, mask, field, and whether the global mean is subtracted).

P4-N13 (Sec. IV.C.a; page 4; Table III) — “lowest bandpower” ambiguous
- Problem: With nlb=1 elsewhere, “lowest bandpower” could mean ℓ=2–6 or ℓ=1-only. The text cites +6.48σ with no table; Table III reports +6.097σ at ℓeff ≈ 4 for a different setup.
- Required fix: Define the exact bin edges for “lowest bandpower” wherever referenced.

P4-N14 (Appendix A.c vs. Appendix D.a; pages 7–8) — Apodization description/notation
- Problem: You state “none on the canonical mask” (Appendix A.c) yet later analyze an apodized canonical mask in Appendix D.a; also the “C 2 2°” notation is idiosyncratic.
- Required fix: Clarify that an additional robustness test with cosine-squared (2° taper) apodization was run on the canonical mask; standardize the notation (e.g., cosine-squared apodization with 2° taper).

P4-N15 (Sec. IV.B; page 4) — “within 0.5% of 50/50” claim unquantified
- Problem: The text asserts slab uniformity without numbers.
- Required fix: Provide the per-slab CW fractions with uncertainties in an appendix table or figure.

Explanation
These additional findings arose from recomputing all arithmetic (A), checking dimensional/definition consistency (C), cross-checking internal references and mask/field definitions (D, I), and ensuring abstract/body coherence (F). The most consequential new items are the training-label count inconsistency (P4-E12), the Fisher-floor arithmetic (P4-E15), the field-definition mismatch in Appendix A (P4-E16), and contradictions around MASTER “removing” leakage vs leaving a +3.64σ residual (P4-E17).