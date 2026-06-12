# P2 R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.54.pdf` md5=aae083ab pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9365 chars)
**Wall time**: 344.6s

---

Referee report for “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- Focus: methodology rigor — correctness of derivations, dimensional consistency, statistical validity, traceability of numerical claims, internal consistency between abstract, body, figures, tables, and appendices.
- I audited every stated scalar appearing in the abstract and conclusions, recomputing from definitions and numbers in the text. I also checked equations for dimensional consistency and estimator definitions, and verified that null-procedure significances are kept distinct.

Overall assessment
The paper presents a sensitivity recast of SPHEREx and MegaMapper forecasts for a bounce prediction fNL = −35/8, including a detailed template-overlap study, an extensive discussion of systematics, and a Bayesian model-comparison exercise. The technical presentation is careful in many places, with numerous caveats. However, there are critical internal inconsistencies in the Bayes-factor calculations against the “tuned multifield competitor,” repeated version-history “Correction note” prose in the body, code-artifact filenames embedded in the main text, and a placeholder DOI in the Data Availability. Several quantitative claims (photo-z degradation, multi-tracer anomaly-source gains) are asserted without sufficient derivational detail for a PRD methods paper. The paper is also longer than needed for the claimed contribution and mixes multiple analysis channels in ways that will confuse a standalone reader unless tightened.

Below I list findings with classification, page, quotation, and required fix.

Findings

ESSENTIAL

P2-E1. Bayes factor arithmetic inconsistency vs tuned multifield competitor (multiple places)
- Location: Sec. VI.C (pp. 11–14), Table II (p. 13), Table III (p. 17), and surrounding prose.
- Problem: The closed-form Bayes factor used for a delta prior at fNL = −35/8 against a uniform competitor prior [fmin, fmax] with a Gaussian likelihood of width σ is
  B ≈ (fmax − fmin) × Lmax / ∫ L df = (fmax − fmin) / [2π σ^2] (for wide bounds),
  because Lmax = 1/(√(2π)σ) and ∫ L df ≈ √(2π)σ.
  With σeff = 0.7 and width 10 for a “narrow” [−5,+5] prior: B = 10 / (2π × 0.7^2) = 10 / 3.0788 = 3.25, not 7.0 as reported in Table III, “Ideal (no GR) BF vs. Tuned = 7.0.” With σeff = 0.860 (σGR = 0.5), B = 10/(2π × 0.860^2) = 2.15, not 6.1. With σeff = 1.221 (σGR = 1.0), B = 10/(2π × 1.49) = 1.07, not 4.7. Similarly, for the “broad” prior [−15,+15] (width 30), B = 30/(2π × 0.7^2) = 9.75 (consistent with 9.80 in the text), but other cells (e.g., “∼17” in the delta/broad cell) are inconsistent with σ = 0.7. The narrow-prior column is systematically high by factors ~2–4 relative to Eq. (8).
- Required fix: Recompute all Bayes factors against the “tuned multifield competitor” using Eq. (8) with the explicitly stated σeff per row (σeff = √(0.7^2 + σGR^2) for Table III rows). Replace all inconsistent numbers in the prose, Table II, and Table III. If any other likelihood or prior was actually used (e.g., truncated integral effects, non-flat priors), write down the exact formula and evaluate it transparently. Where “template-mismatch bookkeeping” is applied, specify which quantity is rescaled (σ → σ/r, fobs → r fobs, or competitor prior width), and show the algebra; then recompute the reported BF numbers consistently. Update the abstract headline Bayes-factor range accordingly.

P2-E2. Version-history prose remains in the body (“Correction note: …”) and must be removed
- Location: Sec. VI.C.b (p. 14), Sec. VII.C (p. 15), Sec. IX.D (p. 20), Table III note (p. 17), and elsewhere.
- Problem: Multiple in-line “Correction note: an earlier version …” statements appear in the main text and table notes. PRD does not allow version-history commentary in the body of the paper.
- Required fix: Remove all version-history notes from the main text and tables. If essential to the scientific record, condense a single neutral clarifying sentence without referring to “earlier version,” or move a brief note to an endnote/Supplemental Material.

P2-E3. Code-artifact filenames and internal bookkeeping appear in the narrative
- Location: Sec. II.A (pp. 3–5), footnote on p. 3, Sec. III.B (p. 8), Sec. VI.C (pp. 11–14), Data & Code Availability (p. 21), Appendix A (pp. 22–24).
- Problem: Strings like “artifact c9i epsilon ratio check.json,” “null space analysis.py,” “phase3 fisher overlap.json,” etc. are embedded throughout the narrative and footnotes as if they were part of the scientific argument.
- Required fix: Move all such artifact names and file paths to the Data & Code Availability or to a Supplemental Material inventory. In the main text, refer to results descriptively (e.g., “see Supplemental Material, Sec. S1; artifact S1.3”), not via raw file names. Ensure the deposited archive is a frozen release with a DOI and clear folder structure mapping to the references in the text.

P2-E4. Data & Code Availability contains a placeholder DOI
- Location: Data and Code Availability (p. 21): “archived at Zenodo (DOI inserted at submission)”.
- Problem: PRD requires a live, citable DOI for deposited materials at submission. A placeholder is not acceptable.
- Required fix: Provide the actual Zenodo (or equivalent) DOI for a frozen release matching the manuscript. Include a version tag/commit hash in the text. Ensure the deposit contains everything claimed.

P2-E5. Ambiguity/incompleteness in the definition of BNL (Eq. (2)); need explicit, unambiguous normalization
- Location: Sec. II.A (p. 3), Eqs. (1)–(2).
- Problem: As typeset, Eq. (2) is difficult to parse unambiguously in relation to Eq. (1). The dimension-counting discussion implies BNL ∝ AT / Σi k_i^3 (which is dimensionless, since AT has degree 3 after the 1/(k1^2 k2^2 k3^2) prefactor), but the printed line “BNL = (10/3) P/AT Σ k_i^3 …” reads like P divided by AT, which would not be dimensionless under the given counting. The next sentence (“no cancellation of P occurs between Eqs. (1) and (2)”) suggests BNL depends on P via AT.
- Required fix: Rewrite Eq. (2) explicitly and unambiguously, with all factors and parentheses, and state the direct relation to the physical ζ-bispectrum in the Planck convention. Provide a single, fully normalized expression for Bζ(k1,k2,k3) in terms of AT and Pζ and show how fNL ≡ BNL|squeezed maps to the Planck normalization. This is a load-bearing definition for the template-overlap and must be crystal clear.

P2-E6. Mixing of significance numbers from different channels without an explicit “not directly comparable” tag at every juxtaposition
- Location: Fig. 5 caption and text (p. 15), Sec. IV vs Sec. VII (pp. 8–10, 14–16), Fig. 2 caption (p. 10).
- Problem: The paper frequently presents SPHEREx bispectrum-only significances (σ = 0.7 → 5.2–5.5σ) alongside MegaMapper SDB-only significances or joint SDB (fNL, nfNL) constraints. While many caveats are given elsewhere, some figure captions and summary sentences juxtapose these without the explicit statement “not directly comparable; different statistics and systematics.”
- Required fix: Where numbers from different observables are placed side-by-side (esp. figure captions and any lines that summarize “X vs Y”), append a short clause: “Note: not directly comparable; these use different estimators/covariances (bispectrum vs SDB) and systematic budgets.”

MAJOR

P2-M1. “Template-mismatch bookkeeping” for Bayes factors is underspecified and numerically inconsistent
- Location: Sec. VI.C.a (p. 14).
- Problem: The text reports transformations like “17.1 → 14.4” (delta, broad), “7.0 → 6.2” (delta, narrow) under a “bounce-amplitude bookkeeping consistent with significance,” but does not provide the precise rule (σ → σ/r vs f → rf vs both). Different consistent bookkeepings produce materially different BFs. The reported numbers do not match any standard rescaling using Eq. (8).
- Required fix: State the exact bookkeeping rule adopted (e.g., “we adopt σeff = σ/r and keep the competitor prior fixed” or “we map to measured space fobs → r fobs, σ fixed”), justify it, and recompute all BF values accordingly. Alternatively, report both sets for completeness and mark one as the fiducial choice.

P2-M2. Photo-z outlier degradation estimate lacks methodology; result used in narrative
- Location: Sec. VII.D (p. 16): “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼ 5% (from 0.70 to 0.74).”
- Problem: This is presented as a “simplified Fisher degradation estimate” but no formula, mock setup, or assumptions (outlier redshift distribution, scale cut, window-function treatment, bispectrum impact) are given. For PRD methods, a numeric claim needs enough information to be reproducible.
- Required fix: Provide a short methodological summary (how outliers are modeled in the bispectrum Fisher, what triangle cuts are applied, what survey window is assumed) and the explicit calculation leading to the 5% figure. Otherwise, soften to a qualitative statement and remove the 5% number from the main text.

P2-M3. “Anomaly-selected tracer” improvement (10–20%) appears without a documented Fisher computation
- Location: Sec. IV (p. 10).
- Problem: The stated improvement is caveated as an “upper bound” but still quantitative without derivation or a pointer to a supplementary calculation.
- Required fix: Either include the Fisher setup and assumptions that produce the 10–20% bound (number density, bias, shot-noise model, redshift distribution), or remove the numbers and state qualitatively that anomaly-selected subsamples could potentially enhance multi-tracer conditioning, with quantification left for future work.

P2-M4. SPHEREx-like and LSS weighting schemes for computing r need precise definitions
- Location: Sec. III.B (pp. 7–9), Eq. (6).
- Problem: You report r for “SPHEREx-like,” “LSS/SDB,” and “CMB Fisher” weightings with different endpoints. For reproducibility, a methods paper should define the weighting kernels precisely.
- Required fix: Specify the weights used in each case (e.g., w ∝ Slocal^2/Fishervar with Var derived from X; for SPHEREx-like: include survey n(z), Pshot, sky fraction, and redshift binning). If these are implemented in code, summarize in text and point to a documented function in the deposit.

P2-M5. Abstract and conclusion Bayes-factor headlines must be updated after correcting E1/M1
- Location: Abstract (p. 1), Conclusion (p. 21).
- Problem: The abstract reports “BF ≈ 9–14 under noise-weighted r ≈ 0.84 bookkeeping (∼10–17 at r → 1)”; these derive from the inconsistent BF arithmetic flagged in E1.
- Required fix: Once the Bayes factors are recomputed consistently, update the abstract and conclusion headlines accordingly. Add a one-sentence parenthetical stating which bookkeeping is used for the headline.

P2-M6. Equation (7) six-point covariance “heuristic check” used to claim < 10^-3 impact needs a tangible bound or consistent labeling
- Location: Sec. IV (p. 9), Eq. (7).
- Problem: The paragraph uses Eq. (7) to argue that σ(fNL) is invariant under fiducial shifts at the few ×10^-4 level. While labeled “heuristic,” the number is used to justify not recomputing the Fisher. The scaling is correct in ζ-space, but the mapping to the galaxy covariance is not shown.
- Required fix: Either (a) move this to a footnote, add a clear “scoping heuristic only” label at the end of the paragraph, and ensure it is not used as a quantitative bound; or (b) provide a short derivation bridging to galaxy-field covariance (bias and shot-noise factors, redshift binning), sufficient to justify the claimed order of magnitude.

P2-M7. Overlength relative to the claimed contribution; numerous digressions and meta-commentary
- Location: Global (25 pages).
- Problem: For a sensitivity recast with a template-overlap study and a Bayes-factor calculation, 25 pages is excessive. The body contains repeated caveats, version-history notes, and meta-commentary that obscure the main methodological thread.
- Required fix: Reduce to ≲18 pages by: (i) removing version-history notes (E2), (ii) moving extended null-space sampling details, artifact descriptions, and ancillary discussions (e.g., cosmic birefringence aside) to Supplemental Material, and (iii) condensing the narrative around systematics to core quantitative points with a crisp checklist table.

MINOR

P2-n1. Appendix A normalization statement: “both fNL and σ(fNL) scale as 1/c” — consistent but add one line derivation
- Location: Appendix A (p. 22).
- Problem: The sentence is correct (Fisher variance ∝ 1/c^2), and consistent with Eq. (A1) and the ζ↔Φ mapping shown, but adding a single sentence “Fisher information ∝ c^2, hence σ ∝ 1/c” will solidify the claim.
- Required fix: Add the one-line justification to Appendix A.

P2-n2. Clarify the precise definition of the shape cosine rcos
- Location: Sec. II.A (p. 4), Sec. III.B (p. 7).
- Problem: You define rcos as a normalized Euclidean inner product on a triangle grid with a “uniform Euclidean measure,” but the exact discretization (grid in side ratios? ordering constraints?) could use one more sentence.
- Required fix: Add a one-sentence formal definition with the domain and measure.

P2-n3. Squeezed-cutoff insensitivity claim (< 0.0002 change in r)
- Location: Sec. III.B (p. 8).
- Problem: The stated change is extremely small; a small table (two or three rows) or a plot in the SM would anchor this.
- Required fix: Provide a 2–3 line mini-table in the SM with x3,min values and the corresponding r.

P2-n4. Minor arithmetic verifications
- Location: Multiple
- Checks: 
  - 4.375/0.7 = 6.25 (naive significance) – OK.
  - With r = 0.83: 4.375 × 0.83 / 0.7 = 5.19 – OK.
  - With r = 0.876: = 5.48 – OK.
  - GR-only floor: σeff = √(0.7^2 + 1.0^2) = 1.221; Significance ≈ 2.98 – OK.
  - CMB PR4 recast: −0.1 ± 5.0 → −0.1 ± (5.0/0.876) ≈ −0.1 ± 5.71 – OK.
- Required fix: None, but consider collecting these into a single “sanity check” box.

NITS

P2-N1. Minor typography in Eq. (2) and surrounding text
- Location: Sec. II.A (p. 3)
- Problem: Parentheses and summation symbols are cramped; risk of misreading.
- Required fix: Re-typeset Eq. (2) with clear parentheses and an explicit Σ symbol.

P2-N2. Consistent hyphenation and capitalization
- Location: Global
- Examples: “multi-tracer” vs “multitracer,” “Fisher-space” vs “Fisher space,” “bispectrum-shaped” vs “bispectrum shaped.”
- Required fix: Standardize.

P2-N3. Remove informal asides (“not undertaken here,” “this is a scoping heuristic,” etc.) where redundant
- Location: Global
- Required fix: Retain only where needed to mark a limitation; otherwise tighten.

P2-N4. Acknowledgment of AI tooling
- Location: Acknowledgments (p. 24)
- Comment: Acceptable, but ensure this aligns with PRD’s policy at time of submission.

Abstract-last drift sweep (pattern-045)
- The abstract’s significance numbers (6.25 naive; 5.2–5.5 template-corrected; 2.6–5 realistic; Li single-ordering half) are traceable and consistent with the body.
- The Bayes-factor headline (BF ≈ 9–14, and “≈ 10–17 at r → 1”) derives from the inconsistent arithmetic flagged in E1; must be corrected.
- The “84–88% recovery” matches r ∈ [0.829, 0.876]. OK.
- The “MegaMapper 3–7σ envelope” is a broad, design-uncertain statement; acceptable if marked illustrative in the abstract — it is.

Provenance surfaces (patterns 046/047)
- The repository link is provided; DOI is missing (E4). Ensure the archive matches the current manuscript and includes a README mapping every named artifact to a figure/table/result.

Uncomputed quantitative claims (pattern-048)
- Photo-z 5% degradation (M2).
- Anomaly-tracer 10–20% gain (M3).
- Squeezed-cutoff insensitivity < 0.0002 (n3).

Standalone-reader test
- Most symbols are defined. However, the precise normalization of BNL (E5) needs to be fixed to avoid ambiguity; otherwise a standalone reader cannot reconstruct the estimator projection.

Effect sizes
- The paper consistently translates amplitudes to σ(fNL) significances and provides fractional overlap r; fine.

## Summary recommendation
MAJOR REVISIONS

The paper contains an important methodological recast and careful systematics discussion, but cannot be accepted in its current form due to the internally inconsistent Bayes-factor arithmetic against the tuned multifield competitor, version-history text embedded in the body, code-artifact references in the main text, a placeholder DOI, and an ambiguous load-bearing equation. Correcting the Bayes-factor computations and tightening the presentation (with explicit definitions and removals of non-scientific meta-commentary) are mandatory. Once these issues are addressed and the abstract/conclusions updated accordingly, the work could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E7. Mis-citation of the Planck tilt when computing fNL,inf
- Location: Abstract (p. 1) and Sec. I (p. 2): “… finfNL ≈ 0.015 at ns = 0.9649 [2] …”
- Problem: Ref. [2] is Maldacena (2003), not the Planck measurement of ns. The numerical value ns = 0.9649 comes from Planck (e.g., PR3/PR4), not [2].
- Required fix: Replace the citation “[2]” with the appropriate Planck ns reference (e.g., [32] for PR3 or [31] for PR4), and ensure all ns-dependent statements point to the correct data source.

P2-E8. Figure 2 caption: malformed σeff expression suggests subtraction instead of two values
- Location: Fig. 2 caption (p. 10): “σeff = √(0.9^2 + 1.0^2– √1.0^2 + 1.0^2 = 1.35–1.41)”
- Problem: As typeset, this reads like a subtraction “√(0.9^2+1.0^2) − √(1.0^2+1.0^2)” rather than two separate σeff values. This is confusing and risks misinterpretation.
- Required fix: Re-typeset to clearly show two separate values, e.g., “σeff = √(0.9^2 + 1.0^2) = 1.35 and √(1.0^2 + 1.0^2) = 1.41.” Also insert “Note: not directly comparable; different estimators/systematics” per P2-E6.

P2-E9. Units/normalization ambiguity in M(k, z) and Δb(k)
- Location: Eqs. (3)–(4), Sec. III.A (p. 7).
- Problem: k is stated to be in h Mpc−1 while H0 is implicit in s−1 unless c is set to unity and H0 is converted to h Mpc−1 units. As written, Δb is dimensionless, but this requires a consistent unit convention (c = 1 and H0 in h Mpc−1) or explicit conversion factors.
- Required fix: State the unit convention explicitly (e.g., c = 1, H0 expressed in h Mpc−1 units via H0 = 100 h km s−1 Mpc−1 and 1 km s−1 = 1/977.8 Mpc Gyr−1, or specify the internal unit handling in the code). This prevents dimensional mismatches when reproducing numbers.

P2-E10. MegaMapper “∼3.5σ conservative” at σ(fNL) = 0.7 is underspecified and inconsistent with the two GR scenarios given
- Location: Sec. V (p. 10): “At an intermediate σ(fNL) = 0.7 … ∼ 5.2σ optimistic, ∼ 3.5σ conservative.”
- Problem: Using your own systematics prescriptions: with r = 0.84 and σGR = 1.0, significance is 3.675/√(0.7^2+1.0^2) ≈ 3.0σ, not 3.5σ. With σGR = 0.5, it is ≈ 4.3σ. “3.5σ conservative” is not reproduced under either GR case unless additional degradations (e.g., bϕ priors) are specified; these assumptions are not stated here.
- Required fix: Specify precisely which systematics are combined for the “conservative” number (e.g., GR = 0.5 plus 30% bϕ prior widening) and recompute the value; otherwise, revise/remove the 3.5σ figure.

P2-E11. Inconsistent “1 − rcos^2 ≲ 0.03” vs. earlier bound rcos > 0.97
- Location: Sec. III.B (p. 8): “projection noise is suppressed by 1 − rcos^2 ≲ 0.03 given the high shape cosine rcos > 0.97”.
- Problem: If rcos > 0.97, then 1 − rcos^2 < 0.06. The ≲ 0.03 suppression holds only if rcos ≈ 0.985 (your stated mean), not under the looser “> 0.97” lower bound quoted in the same paragraph.
- Required fix: Make the statement consistent: either tie the 0.03 figure to the mean rcos ≈ 0.985, or relax it to < 0.06 when invoking only the lower bound rcos > 0.97.

P2-E12. SPHEREx timeline statements inconsistent; needs citation or harmonization
- Location: Sec. IX.A (p. 18): “first all-sky survey completed December 2025”; Abstract and Conclusion: “primary survey through ∼2027; ∼25 months of operations.”
- Problem: “First all-sky survey completed December 2025” (≈9 months after launch) and “primary survey complete after ~25 months” can both be true (first pass vs full survey), but the current text reads as contradictory and is uncited.
- Required fix: Add a project-citation for the cadence, and clarify “first sky pass” vs “primary 25-month survey.” Alternatively, remove calendar specifics not essential to the methods.

P2-E13. Table III label “Corrected (10% residual; = Ideal, verification only)” is internally inconsistent
- Location: Table III note (p. 17).
- Problem: The row title says “10% residual,” but the note clarifies it is the “strict zero-residual limit,” hence identical to “Ideal.” This is contradictory labeling.
- Required fix: Rename the row unambiguously (e.g., “Corrected (zero residual; verification only)”) and, if you wish to include the 10% residual example, add a separate row with σGR = 0.05 and the corresponding BF values.

MAJOR

P2-M8. κϵ bound 5.6–80 lacks a derivation; the “≈14×” amplification is asserted without equations
- Location: Sec. VIII.B (pp. 18–19).
- Problem: You state “Explicit prefactor scaling alone gives κϵ ≈ 5.6; the mode-function channel adds a multiplicative correction … ≈14× … giving κϵ ≈ 80” with no derivation. This bound is then used to argue the fNL shift (≈0.36) sits within σtheory = 1.0.
- Required fix: Provide the explicit steps (or a short SM derivation) showing: (i) how the AT ∝ 1/ϵ^3 prefactor yields κϵ ≈ 5.6 at ϵ = 3/2, and (ii) how the mode-function dependence contributes the quoted ~14× factor. Include the intermediate formulae and numeric evaluation sufficient for reproduction. If this is only a dimensional estimate, mark it clearly as such and avoid using a precise “14×” in the main text.

P2-M9. bϕ-prior dependence in Fig. 5 is quantitative but methods-free
- Location: Sec. VII.B and Fig. 5 (p. 15): “at 20% prior width, MegaMapper SDB gives σ(fNL) ≈ 1.0; at 50%, σ ≈ 2.2…”
- Problem: These are concrete numbers, but no Fisher setup (tracers, n(z), k-cuts, covariance treatment) is provided to reproduce them.
- Required fix: Add a brief methodological summary for the bϕ prior scan (data vector, Fisher kernel, priors applied, scales), or move the panel to SM with a methods paragraph. If this is only illustrative, soften the language and remove specific numbers from the main text.

P2-M10. MegaMapper “intermediate” σ(fNL) = 0.7 scenario requires explicit systematics combination
- Location: Sec. V (p. 10): “… at an intermediate σ(fNL) = 0.7 …”
- Problem: As used, σ = 0.7 could refer to a partially degraded ideal forecast. But the numbers quoted (∼5.2σ optimistic; ∼3.5σ conservative) depend on what is and is not included (r, GR, bϕ, photo-z, etc.). At present this scenario is not reproducible.
- Required fix: State exactly what ingredients are included/excluded to yield σ = 0.7 and each significance value; otherwise drop the “intermediate” line to avoid mix-and-match interpretations.

P2-M11. Exact finite-interval integral for Eq. (8) should be used (not the “wide-bound” approximation), then numbers recomputed consistently
- Location: Sec. VI.C (pp. 11–14), Tables II–III.
- Problem: Several BF numbers hinge on the integral in Eq. (8). For narrow priors (e.g., [−5, +5]), the “wide-bound” √(2π)σ approximation can be inaccurate if |fobs − prior edges| ≲ few σ; this is precisely where earlier arithmetic inconsistencies arose.
- Required fix: Write the exact finite-interval integral in terms of the error function (erf), evaluate it for each σeff and prior used, and recompute all BF entries. This complements P2-E1 (which flagged inconsistent arithmetic) and will eliminate ambiguity from the approximation.

MINOR

P2-n5. Clarify which rcos value underlies the “1 − rcos^2 ≲ 0.03” suppression
- Location: Sec. III.B (p. 8).
- Fix: Add “using the mean rcos ≈ 0.985 from our 10,000-sample scan” or relax the inequality to “< 0.06” when quoting only the lower bound rcos > 0.97.

P2-n6. Notational overload of “P” for both the degree-9 polynomial and power spectra
- Location: Sec. II.A (pp. 3–5), global.
- Fix: Consider renaming the degree-9 polynomial to Q(k1,k2,k3) (or similar) to avoid confusion with Pζ and PΦ. If keeping “P,” add an inline reminder the first time both notations occur together.

P2-n7. Appendix A uses “c” for the Komatsu–Spergel constant while “ci” denote monomial coefficients in Sec. II
- Location: Appendix A (pp. 22–24) and Sec. II.A (pp. 3–5).
- Fix: Add a short note at the start of Appendix A clarifying that “c” in A.1–A.2 is the local-template normalization constant and unrelated to the monomial coefficients c1–c6.

P2-n8. Add an explicit units note near Eq. (4)
- Location: Sec. III.A (p. 7).
- Fix: One sentence like “We work in c = 1 units, with H0 converted to h Mpc−1 to match k” will preempt unit-confusion for readers attempting to reproduce Δb(k).

P2-n9. Fix σeff formatting in Fig. 2 caption (typographic)
- Location: Fig. 2 caption (p. 10).
- Fix: Replace the current parenthetical with “σeff = √(0.9^2 + 1.0^2) = 1.35 and σeff = √(1.0^2 + 1.0^2) = 1.41.”

NITS

P2-N5. Calendar claims about SPHEREx operations should be cited or softened
- Location: Sec. IX.A (p. 18).
- Fix: Add a NASA/SPHEREx reference for cadence (first-pass vs primary mission) or remove calendar-specific statements that are not central to the methods.

Explanation
This fresh-eyes pass focused on arithmetic, caption–body alignment, units/dimensional consistency, cross-references, and potential stale/misaligned numbers that commonly slip through. In addition to your initial findings, the items above surfaced new inconsistencies (notably a mis-citation for ns, a confusing σeff expression in a figure caption, unit-convention ambiguity in M(k,z), an underspecified MegaMapper “conservative” significance, an inconsistent projection-noise bound vs rcos floor, an inconsistent “10% residual” label, and an undocumented κϵ bound). Addressing these will materially improve rigor and reproducibility.