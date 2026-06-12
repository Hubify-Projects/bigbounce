# P4 R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v176.pdf` md5=baa9467c pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4723 chars)
**Wall time**: 298.7s

---

Referee report on P4 (PRD submission), Round R34conf

Scope of review
- Focus: statistical methodology rigor, internal arithmetic consistency, null procedures, estimator declarations, effect-size interpretation, provenance/reproducibility surfaces.
- I audited the abstract and conclusions against the body, recomputed all checkable ratios/proportions, and examined the treatment of σ- and p-values across different nulls.

Overall assessment
The manuscript contains a substantial and careful analysis with many explicit checks. However, there are several methodology/provenance inconsistencies and presentation issues that must be corrected before this can meet PRD standards. In particular: (i) an inconsistency in the training/validation split and augmentation accounting; (ii) pervasive version-history/audit-log prose that belongs in a response letter or supplementary repository, not in the main paper; (iii) confusing and internally inconsistent look-elsewhere handling for the hemisphere scan; and (iv) multiple places where σ’s from different null procedures are juxtaposed in the abstract/conclusions without an explicit “not cross-comparable” reminder. I list all findings in detail below.

Findings

ESSENTIAL

P4-E1 (Sec. II.B, p. 2–3): Inconsistent training/validation split and augmentation accounting
- Text: “6,637 + 17,153 + 2,000 = 25,790 … after flip augmentation of the training split the combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323; augmented duplicates contribute to the 826-image difference …).”
- Problem: If augmentation is applied “to the training split” only, the total should be ntrain = 0.8×25,790 + 826 = 21,458 and nval = 0.2×25,790 = 5,158, not the reported 21,293 and 5,323. The 165-example shortfall in train is exactly mirrored as an excess in val, which suggests leakage or a misdescription of when the split was performed relative to augmentation.
- Required fix: Precisely document the split and augmentation pipeline, and provide exact counts by source and by split before and after augmentation. If any augmented samples entered validation, state it explicitly and justify. If not, correct the counts. This is load-bearing for reported accuracies.

P4-E2 (Multiple sections/pages, incl. Abstract p. 1; Secs. III–VII; Appendices): Version-history and internal-audit prose in the body
- Problems/examples:
  - Abstract, p. 1: “An earlier version of this paper … withdrawn (Appendix A).”
  - Sec. III.B, p. 3–4: “declared in early versions … predates the provenance audit.”
  - Throughout: extensive “artifact pipelines/… .json” file paths, seeds, commit hashes, and revision tags (“v1.0.76”, “post-R29”, “≤v1.0.165”), and an extended “two-step stamp-then-pin” explanation in Data Availability (p. 20–21).
- Required fix: Remove all version-history, revision-log, and audit-narrative text from the main paper. Keep a concise, journal-appropriate Data Availability statement with a frozen DOI of the exact data/model/code release used. Any detailed provenance (file paths, seeds) belongs in a companion reproducibility repository/readme, not in PRD main text.

P4-E3 (Table I row (v), p. 5; Appendix C, p. 18): Incoherent look-elsewhere accounting for the hemisphere scan
- Text: Table I row (v): “post-look-elsewhere-corrected significance; the raw direct-MC value is pLEE ≤ 10−4 … the additional Bonferroni/BH pass … is a second, deliberately conservative penalty.”
- Problem: The direct-MC max-statistic null already incorporates the directional trials. Describing pLEE ≤ 10−4 as “raw” and then applying a second Bonferroni/BH correction double-counts the trials and is methodologically incorrect. Moreover, within the paper the same result is described as both “pLEE ≤ 10−4” and “< 1σ after look-elsewhere correction,” which is self-contradictory.
- Required fix: Choose one principled correction. Either (a) quote only the direct-MC max-statistic pLEE (preferred), or (b) if you insist on a heuristic Bonferroni/BH, then do not present the MC pLEE as “raw” or “post-LEE”; make clear you are replacing it. Present a single corrected value consistently (σ or p), and remove the contradictory phrasing.

P4-E4 (Abstract p. 1; Conclusions p. 14): σ’s from different null procedures juxtaposed without explicit cross-comparability caveat
- Text: Abstract lists “+3.64σ … canonical mask; +7.28σ, apodized footprint,” alongside the headline +0.41σ dipole, without an explicit reminder that these are different estimators and nulls. A similar juxtaposition appears in the Conclusions (bullets a–c).
- Required fix: In the abstract and conclusions, add an explicit, immediately adjacent statement that these σ’s are relative to their own nulls/fields/weights and are not cross-comparable to each other nor to the real-space dipole σ. PRD requires that readers not be misled by side-by-side σ’s.

P4-E5 (Appendix D, p. 19): Typo in headline exclusion statistic
- Text: “the headline exclusion statistic is z ≈ −18.1.34”
- Problem: Spurious “.34” appended to the z-value.
- Required fix: Correct to a single number (e.g., “z ≈ −18.1”) and ensure the same number is used consistently where quoted elsewhere (abstract has “≈ −18”).

P4-E6 (Data Availability, p. 20–21 vs. front matter p. 1): Commit/version mismatch and lack of frozen DOI
- Text: Dated “June 11, 2026 — v1.0.176” (front matter), but Data Availability cites “commit 53b41d12 (v1.0.175) … a Zenodo DOI snapshot … has not yet been minted.”
- Problem: The analysis version is not frozen to a persistent DOI, and the commit/version labeling in the paper is inconsistent with the stated manuscript version.
- Required fix: Freeze and cite a persistent Zenodo (or equivalent) DOI for the exact code, models, and data artifacts used in this manuscript. Ensure the paper’s version tag matches the archived artifact. Remove the “two-step stamp-then-pin” explanation from the paper.

P4-E7 (Sec. IV.D, p. 10–11; Table III p. 11; Conclusions p. 14): Two different σ values (+3.64 and +7.93) for the same “canonical” ℓ=1 channel sow confusion
- Text: The same canonical, unapodized channel is reported as +3.64σ (500-MC) and +7.93σ (10k permutations).
- Problem: While you do note they arise from different null ensembles, maintaining two disparate σ’s for the same physical channel is confusing for readers and easily misinterpreted.
- Required fix: Choose one canonical reporting convention (e.g., the 10k-permutation set) and demote the other to a footnote/supplement, or report both but convert them to a single common metric (e.g., empirical rank p) and state one headline value. Make the choice consistent across the paper.

MAJOR

P4-M1 (Sec. III.D, p. 4; Appendix B.a, p. 16): Equivariance/augmentation scope vs. validation accounting
- Text: “We restrict to 2-fold TTA … rotation-TTA probes classifier non-equivariance … flip augmentation … equivariance loss act on training batches only.” Yet the nval count appears to have absorbed 165 examples (see P4-E1).
- Problem: The stated protocol and the reported counts do not align. Even if P4-E1 resolves the arithmetic, the paper must explicitly state that validation contains no augmented duplicates and is untouched by the equivariance loss, to avoid data leakage concerns.
- Required fix: Clarify in the methods that validation images are never augmented nor used in the equivariance loss, and that early stopping/selection used only validation metrics computed on un-augmented data. Provide a simple table with train/val by source and by augmentation flag.

P4-M2 (Table I, p. 5; Sec. IV.C–D, p. 8–11): Units/fields switching
- Issue: The manuscript toggles between Ap and fCW fields, and between pre-MASTER pseudo-Cℓ and post-MASTER deconvolved Cℓ, with different weight/mean-subtraction conventions. Although text attempts to keep this straight, readers can be lost.
- Required fix: Add a single summary table mapping each quoted σ/number in the abstract to: field (Ap or fCW), mask, weight map, mean subtraction convention, MASTER vs pseudo-Cℓ, null type, and MC size. This will also satisfy PRD’s traceability requirement.

P4-M3 (Sec. VI.A, p. 12–13; Table V p. 13): Injection-recovery threshold reporting lacks uncertainty
- Text: “A50 ≈ 0.75%; A95 ∈ (1.0%, 1.5%] … Ninj = 100 per amplitude … binomial SE ≤ 0.05.”
- Problem: The crossing uncertainty on A50 is not quantified; A95 is only bracketed. For a main falsification criterion, readers need a quantitative CI on A50 and a tighter/explicit estimate for A95 or a statement why higher Ninj was not feasible.
- Required fix: Provide binomial-CI-derived uncertainty on A50 (e.g., via logistic fit or monotone spline with bootstrap) and increase Ninj at key amplitudes to quote A95 with an uncertainty, or clearly move A95 to supplementary and state that the operative bound is bracketed.

P4-M4 (Appendix E, p. 20): Edge-on contamination quantitative claim without derivation
- Text: “reduces effective sample size by ∼ 10–15%, corresponding to a ∼ 5–8% sensitivity penalty.”
- Problem: The derivation from the reported 65.7% edge-on mis-triage is not shown.
- Required fix: Provide a short derivation or simulation showing how the stated contamination level maps to the quoted effective-N and sensitivity penalties, or remove the percentages.

P4-M5 (Sec. V.A, p. 12): “Maximum regional asymmetry is 0.32%”
- Problem: No figure/panel or table number supports that single number; readers cannot verify.
- Required fix: Cite the exact figure/table (or include a panel) that defines “regional” and shows the 0.32% value, or remove the number.

P4-M6 (Appendix A.c, p. 15–16): Notation/formatting of apodization
- Text alternates between “C2 2◦,” “C 2 2 ◦,” and prose.
- Required fix: Standardize the apodization notation (e.g., “C2 apodization, 2° length”) throughout.

MINOR

P4-n1 (Sec. IV.B, p. 5–6): Slab statistics
- Text: “deviations … −0.110% to −0.463% … RA partition comparable.”
- Fix: Provide the full list of slab values in an appendix table or move a compact numeric list into the text, to support “spatially uniform” claim.

P4-n2 (Sec. IV.C, p. 7): Dipole amplitude units
- Text: “fitted dipole has amplitude 4.4 × 10−3 toward …”
- Fix: Append “in Ap units (full-amplitude A)” to the sentence to avoid ambiguity.

P4-n3 (Sec. III.A, p. 3): Significance conventions
- Text: “These three values are from different null-run sizes … and are not mutually comparable.”
- Fix: Add an explicit sentence reminding that Gaussian z-equivalents from rank p may not match moment-z due to heavy tails. This helps readers reconcile the 500 vs 10k permutations.

P4-n4 (Sec. VII, p. 14): Very large z claims in harmonic completeness
- Text: “Ap = 1.7% yields median recovered significance z ≈ 68–218.”
- Fix: Provide median and 16–84% range, and a one-line note (e.g., estimator normalization) to explain such extreme z to readers unfamiliar with this channel.

NIT

P4-N1 (Throughout): Hyphenation/spacing artifacts
- Examples: “esti￾mator5”, “C 2 2 ◦”, broken words at line wraps, “ℓ= 1” vs “ℓ = 1”.
- Fix: Clean typesetting artifacts.

P4-N2 (Bibliography, p. 21–22): Ensure all DOIs/arXiv IDs correspond to the cited year and journal titles; spot-check suggests consistency, but a final pass is advised.

P4-N3 (Sec. V.B, p. 12): “1.6× the spiral coverage” claim
- Fix: For precision, append the absolute counts being compared (3.20M vs 1.95M).

Arithmetic/consistency checks I performed
- Catalog totals: 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531 (OK).
- Spiral fraction: 3,201,160 / 8,474,531 ≈ 0.37778 (OK).
- Catalog C fCW = 1,592,107 / (1,592,107 + 1,609,053) ≈ 0.497353 (OK). Binomial σ ≈ 0.000279; deviation −0.002647 → −9.49σ (table lists −9.47σ, OK at rounding).
- Catalog A fCW = 0.507879; σ ≈ 0.000274; deviation 0.007879 → 28.8σ (table 28.72σ, OK).
- MASTER apodized ℓ=1: (2.348e−5 − 1.71e−6)/2.99e−6 ≈ 7.28σ (OK).
- Table III apodized ℓ=1: (24.74−1.93)/3.12 ≈ 7.31σ (OK).
- Table IV reproduction: 1.6846e−2 / 1.6961e−2 = 0.9932 (OK); z = (1.6961−1.6846)/0.0068 ≈ 1.69 (OK).
- Fisher floor: √(3/3,201,160) ≈ 9.68×10−4; 3σ ≈ 0.29% (OK).
- HC Fisher floor N=949,584: √(3/N) ≈ 1.78×10−3; 3σ ≈ 0.53% (OK).

Abstract-last drift sweep
- The abstract mostly tracks the body. However, the hemisphere LEE handling is confusing (see P4-E3), and the abstract juxtaposes σ’s from distinct nulls without an explicit “not cross-comparable” reminder (P4-E4). The “withdrawn” provenance note belongs outside the abstract (P4-E2).

Provenance surfaces
- The main paper reads like a lab notebook in places, with internal file paths and revision commentary. PRD expects a clean narrative with a stable, public DOI to the exact artifacts. See P4-E2 and P4-E6.

Effect sizes
- The manuscript frequently gives effect sizes (percent amplitudes, Ap units). This is good. Ensure the real-space dipole amplitude (4.4×10−3 Ap) is always quoted with units when σ is provided (P4-n2).

Page length
- The paper is long (22 pages main text + appendices). Given the single headline cosmological result is a null, I recommend moving most audit-path “artifact” references and some of the eight-anchor systematic diagnostics to a supplementary PDF or repository readme, keeping in-paper references concise. A target of ≤16 pages main text plus appendices would be reasonable.

## Summary recommendation
MAJOR REVISIONS

The analysis is careful and potentially publishable, but cannot be accepted in its current form. The training/validation split inconsistency must be resolved; the look-elsewhere handling must be made methodologically coherent; σ’s from different nulls should be presented unambiguously; the manuscript must be cleaned of version-history/audit-log prose; and provenance must be frozen to a DOI. Once these are addressed, along with the other listed issues, I would be willing to re-review.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass after R34conf)

ESSENTIAL

P4-E8 (Table II, p. 5): Catalog-B uncertainty vs Dev inconsistency and missing Nspiral
- Table reports f = 0.504 ± 0.0003 with Dev = +14.6σ. A 0.004 deviation divided by 0.0003 would be ≈ 13.3σ, not 14.6σ. The Dev = 14.6σ matches σ ≈ 0.000274 (i.e., using NA_spiral = 3,321,795 from Tier A), not the listed ±0.0003. Also, Nspiral for Tier B is not given. Required fix: State the exact Nspiral used to compute σ for Tier B and make the “±” uncertainty and the Dev consistent (same σ). If Tier B uses NA_spiral, say so; otherwise correct the σ and Dev.

P4-E9 (Sec. IV.C, p. 7): Units mixing “percent” with Ap units
- Text: “unthresholded … yields a 0.57% (Ap-unit) dipole at z ≈ 4.2–4.4.” Ap is dimensionless in [−1,1] and equals the full-amplitude A; writing “% (Ap-unit)” is self-contradictory. Required fix: State either “A = 0.57% (i.e., Ap = 0.0057)” or “Ap = 5.7 × 10−3,” and use a single convention consistently throughout.

P4-E10 (Appendix A.a, p. 15): Monopole-subtraction example mixes footprints/weights
- The paragraph describes the Wp = Nall, apodized footprint diagnostic, then immediately quotes “monopole subtraction reduces C1 from 2.30 × 10−5 to 1.51 × 10−5 … and increases σ to +3.64 (the canonical-mask number).” The +3.64σ is for the canonical, unapodized, binary-weight channel, not the Wp = Nall footprint just described. Required fix: Show the before/after monopole-subtraction numbers within one and the same mask/weight convention, and avoid cross-channel numbers in a single example.

MAJOR

P4-M7 (Appendix B.d, p. 17): Flip-swap “error” metric undefined
- The text quotes “mean flip-swap error 0.267 (median 0.0006) at max p > 0.9 vs. 0.383 (median 0.364) at max p < 0.7,” but never defines the error (L1? L2? 1 − corr?). Required fix: Provide the exact definition/formula of the “flip-swap error” used.

P4-M8 (Appendix D.d, p. 18–19): “∼25% of ℓ = 1 amplitude” claim lacks numeric derivation
- You report rℓ=1(BASS+MzLS×Ap) = +0.65 and rℓ=1(DES×Ap) = −0.73 and then state “the summed leg-induced ℓ = 1 amplitude is ∼25% of the observed canonical … amplitude.” Required fix: Show the actual ℓ = 1 template amplitudes and their quadrature/linear combination, with uncertainties, to substantiate the “25%” figure.

P4-M9 (Appendix C.d, p. 18): Brick-boundary attribution unquantified
- Text: “−2.41σ at θ ≈ 0.5° is attributable to DR8 brick-boundary artifacts (confirmed by vanishing to −0.03σ in the brick-interior subsample).” No figure/table is cited, and the brick-interior criterion is not specified. Required fix: Provide a brief quantitative definition of the brick-interior cut and cite a panel/table showing both curves.

MINOR

P4-n5 (Sec. IV.D, p. 9–11): In-body juxtaposition of σ’s from different nulls without local caveat
- Early in Sec. IV.D you present +3.64σ (canonical decoupled) and 3.05σ (hemisphere, label-shuffle null) side by side as “candidate manifestations” without the immediate “not cross-comparable” reminder (the generic caveat appears elsewhere). Required fix: Add a one-line local qualifier that these σ’s arise from different estimators and nulls and are not directly comparable.

P4-n6 (Table I footnote a, p. 5): fsky rounding vs pixel count mismatch
- Footnote states fsky = 0.4801 (HC sample) and “23,600 of 49,152 pixels.” 23,600/49,152 = 0.48020…, i.e., 0.4802 at 4 decimals, not 0.4801. Required fix: Harmonize the decimal fsky with the integer pixel count (or state both precisely).

P4-n7 (Data Availability, p. 21): Repository tag formatting
- HuggingFace dataset slug printed as “galaxy- chirality- catalog” (with internal spaces around hyphens). Required fix: Normalize the slug text to the exact canonical path users can click/copy.

NIT

P4-N4 (Throughout): Normalize amplitude nomenclature
- The paper alternates between “Ap units,” “full-amplitude A,” and “fCW deviation.” Even with reminders, readers stumble. Required fix: Add a one-line, consistent style guide near Eq. (3) (e.g., “We report dipole amplitudes as A ≡ Ap; percent values mean 100 × A”) and adhere to it everywhere, especially when giving both σ and amplitude.

NO OTHER NEW ISSUES FOUND IN CLASSES A–J
- I rechecked all arithmetic spot-verified in the first review (σ computations; Table III z’s; Table IV ratios; Fisher floor; slab σ), and they remain correct within rounding.
- Figure captions vs body claims match on units and ranges (e.g., Figs. 4, 7, 8).
- Equations are dimensionless/consistent.
- Most cross-references point to the intended content.
- The abstract is broadly faithful to the body; the earlier issues (LEE handling, σ juxtaposition, withdrawn-result provenance) are already captured by P4-E2–E4.