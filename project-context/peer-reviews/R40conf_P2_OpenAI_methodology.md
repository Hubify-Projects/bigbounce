# P2 R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper2_fnl_forecast.pdf` md5=cab7e43f pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7193 chars)
**Wall time**: 427.9s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- I reviewed all 29 pages, including equations, figures, tables, footnotes, appendix, and the Data & Code Availability section.
- Focus was methodology rigor: statistical validity, derivation chains, dimensional analysis, internal arithmetic, error propagation, and abstract-to-body consistency.
- Below I list all findings with severity tags and specific required fixes.

ESSENTIAL findings (must be fixed before PRD publication)

P2-E1 (Sec. II.A, p.3; Eqs. (1)–(2); dimensional consistency and definition)
- Problem: Equation (2) as written implies BNL = (10/3) × (P/AT) / Σi k_i^3 (the PDF shows “BNL = 10/3 P/AT i k_i^3”). Combined with Eq. (1) AT = (3/(256 k1^2 k2^2 k3^2)) P, this makes BNL ∝ (k1 k2 k3)^2/Σk_i^3 with residual k^3 dimension, contradicting the text on the same page stating “BNL is dimensionless by construction.” The paragraph further claims “no cancellation of P occurs between Eqs. (1) and (2),” which is inconsistent with P/AT canceling P entirely.
- Required fix: Correct Eq. (2) and the accompanying paragraph to be dimensionally consistent and unambiguous. If, as the text suggests, BNL was intended to be BNL = (10/3) × AT/(Σi k_i^3), state that explicitly and confirm that no P-cancellation occurs (since AT already contains P). Alternatively, if another definition was used in code/figures, present it explicitly and show the degrees-of-k counting that makes BNL dimensionless. Propagate this correction consistently through the paper (Fig. 1 label, Table I caption, any code/DOI material relying on Eq. (2)) and add a sentence confirming that all numerical results used the corrected definition.

P2-E2 (Sec. IV, p.10, “Shot-noise caveat” paragraph)
- Problem: Internal numerical contradiction. You write “a simple Poisson estimate gives a ∼ 15–30% degradation in σ(fNL) ... scaling as σ_shot/σ_CV ∼ sqrt(1 + 1/(nP0)) ... for n ≃ 10^−5 and P0 ≃ 10^4, 1/(nP0) ≃ 10, giving σ inflated by sqrt(11) ≈ 3.3×,” yet conclude “the bispectrum estimator effective degradation ... is moderate, 15–30%.” The two statements are inconsistent by more than a factor of 10.
- Required fix: Provide a consistent, survey-appropriate derivation of shot-noise degradation for the bispectrum estimator actually used (not the power-spectrum heuristic), with either a quantitative bispectrum Fisher recalculation or a validated analytic scaling specific to the squeezed configurations that dominate the local signal. If you retain the 15–30% figure, show the calculation that leads to this range and reconcile it with the sqrt(1+1/(nP0)) estimate. If no robust computation is available, remove the 15–30% claim and present this as an open modeling item.

P2-E3 (Data and Code Availability, p.25)
- Problem: Reproducibility placeholders and missing provenance. The text says “archived at Zenodo (DOI inserted at submission).” No DOI is given; no frozen commit hash is provided for the GitHub repository; several artifacts are referenced only by local filenames in prose (e.g., “c9i epsilon ratio check.json,” “null space analysis.py,” etc.).
- Required fix: Provide a working Zenodo DOI for a frozen release that matches the exact version used to produce all results in this manuscript. Include a top-level README with environment, dependency versions, and a one-command (or step-by-step) reproduction script. List the exact commit hash(es) used and ensure every artifact referenced in the text is present in the archival release. PRD requires durable, citable, versioned resources; placeholders are not acceptable.

P2-E4 (Multiple locations; e.g., Sec. II.A p.4 n.1; Sec. II.A p.5; Sec. VI.C p.12–15; Appendix A p.25)
- Problem: Internal bookkeeping/file-path strings appear throughout the main text (e.g., “artifact c9i epsilon ratio check.json,” “null space analysis.py,” “phase3 fisher overlap.json,” “c9g bf table recompute.py,” “appendix A1 wick doubling.py”). These are not conventional for PRD body text and read like internal audit notes.
- Required fix: Move all file and script names out of the main text and into a consolidated Data & Code Availability section or Supplement, with a clean mapping table (script → purpose → figure/table numbers it reproduces). In the body, replace these with standard references to the Supplement/Zenodo record.

P2-E5 (Sec. VI.C, Table II, p.16–17; Abstract, p.1)
- Problem: The abstract headlines Bayes factors “≈ 9–14” after applying the r ≈ 0.84 “rebooking,” whereas Table II lists the r→1 endpoint values. The text mentions rebooking in prose, but a reader comparing abstract vs Table II cannot see the rebooked values tabulated anywhere.
- Required fix: Add a second table column (or a companion table) that explicitly reports the rebooked Bayes factors at σeff = 0.7/0.84 ≈ 0.833 for the same prior choices, so that the abstract’s “≈ 9–14” numbers are directly traceable to a table entry. Explicitly label r→1 vs rebooked columns.

P2-E6 (Sec. VI.C, p.12–13; “105 realizations”)
- Problem: Ambiguous MC sample size notation. The text repeatedly uses “105 realizations” and “3×105 aggregate,” which in plain reading is 105 (one hundred five), not 10^5. This ambiguity affects claimed precision in later columns (e.g., probabilities reported to <0.1 percentage points).
- Required fix: Typeset the MC count unambiguously as 10^5 (or 3×10^5), and confirm the sample size used to compute P(BF>3) in Table III (p.19). If it is 105 per ensemble, recompute with adequate N to support the quoted precision; if it is 10^5, correct the notation throughout.

P2-E7 (Primary estimator declaration; throughout, but especially Abstract p.1 and Sec. IV p.9–10)
- Problem: The paper alternates among multiple “null procedures” and estimators (SPHEREx multi-tracer bispectrum Fisher from Heinrich et al.; your KSW-type flat-sky injection-recovery; your shape-projection Fisher overlaps), and shows their σ’s side-by-side in some places. Although you often state they are not directly comparable, there are still juxtapositions where a casual reader could conflate them (e.g., Fig. 2 shows the “naive uncorrected 6.25σ” bar alongside the template-corrected and post-budget bars).
- Required fix: At every location where two σ’s from different null procedures or estimators are juxtaposed (figures, tables, bulleted lists), include an explicit in-figure or in-caption note that they are not directly comparable and state exactly which estimator each bar uses. In the main text, predeclare the primary estimator that underwrites the headline (Heinrich et al. bispectrum Fisher with your shape-overlap r), and ensure every other σ is clearly labeled “diagnostic only.”

MAJOR findings (significant revisions required)

P2-M1 (Sec. II.A, p.5–6; “Null-space r = 0.85 ± 0.13” used as a systematic)
- Problem: You emphasize that the ±0.13 spread in r from the 3D coefficient null space is basis-dependent (“uniform Euclidean measure in this monomial basis is not invariant under linear reparametrizations,” p.4–5), yet in the abstract and §IV you appear to include this ±0.13 as part of the systematic budget narrative. A basis-dependent “systematic” is not well-defined.
- Required fix: Either (a) remove ±0.13 as a systematic component and reframe it strictly as a diagnostic spread under one internal parametrization, or (b) provide a basis-invariant bound (e.g., extremize r under all linear reparametrizations preserving the three benchmarks, or demonstrate invariance across two or more orthonormalized bases) and use that invariant bound in the budget. At minimum, quantify how much the post-budget 2.6–5σ range would change if the null-space sampling measure were altered.

P2-M2 (Sec. II.A, p.5–6; injection-recovery test; rmeasured = 0.90 ± 0.01 with N=200)
- Problem: The reported ±0.01 uncertainty on rmeasured with only 200 realizations is not justified. You do not report the sample standard deviation, so the standard error of the mean cannot be verified. Moreover, the noise model is diagonal and full-sky; this test does not approximate the 3D SPHEREx bispectrum estimator and is not representative of survey systematics.
- Required fix: Report the sample standard deviation and standard error for rmeasured; if the per-realization scatter is ≳0.14, 200 realizations indeed give ~0.01 SE, but this must be shown. Clearly label this test as CMB-like and not representative of the SPHEREx 3D bispectrum pipeline. Consider moving it to a Supplement.

P2-M3 (Sec. VI.C, p.12–15; closed-form Bayes factor with Gaussian bounce prior)
- Problem: The analytic expression is given explicitly only for the delta-prior case and the uniform competitor. For the Gaussian bounce prior σtheory you refer to “prior-convolved marginal” without writing the closed-form expression actually used.
- Required fix: Add the explicit closed-form Bayes factor expression used for the Gaussian bounce prior (the convolution of two Gaussians in the numerator), or cite a standard formula with parameters filled in. Ensure Table II values can be reproduced from the printed formulas without running your code.

P2-M4 (Sec. IV, p.10; “anomaly-detected tracers” 10–20% improvement claim)
- Problem: You claim an ∼10–20% σ(fNL) improvement from anomaly-selected subsamples “pending the shot-noise-corrected Fisher analysis,” i.e., without the needed calculation; this is speculative and, given the shot-noise inconsistency (P2-E2), potentially misleading.
- Required fix: Remove the 10–20% quantitative claim unless you provide a substantiated Fisher calculation with the correct shot-noise term for these subsamples. Qualitative statements about potential benefits are fine.

P2-M5 (Sec. III.B, p.8–9; CMB Fisher overlap r = 0.878 ± 0.012)
- Problem: No methodological details are given for how the ℓ-space Fisher overlap uncertainty ±0.012 is obtained (integration range, binning, quadrature, noise model).
- Required fix: Provide a one-paragraph methods description (ℓ-range, CAMB settings, noise curves used, numerical quadrature parameters) and report the numerical stability checks (e.g., convergence with respect to ℓmax or bin resolution). If this is in the code archive, add an explicit pointer and summarize here.

P2-M6 (Sec. VIII.B, p.20–21; κϵ range [5.6, 80])
- Problem: The upper-end estimate κϵ ≈ 80 is described as a “schematic scaling bound” without a derivation, yet it propagates to the allowed fNL(ns) band (Eq. 12) quoted in the text.
- Required fix: Either provide a derivation (even order-of-magnitude) of the 80 figure in an appendix, or narrow the presentation to a conservative lower bound with a clear statement that the upper range is illustrative. The final quoted fNL(ns) interval should be tied to a stated and reproducible κϵ estimate.

MINOR findings (address but do not block)

P2-n1 (Abstract p.1; Sec. IV p.9–11): Length and scope
- The paper is long (29 pages) relative to the primary contribution (a shape-overlap audit and sensitivity recast). Consider tightening to 15–18 pages by moving some discursive material (e.g., detailed anomaly-tracer discussion, cosmic birefringence aside in §IX.E, repeated caveats) to an appendix or to the code/Zenodo note.

P2-n2 (Sec. VI.A p.11; novelty claim)
- Claim: “a literature search confirming no prior quantification of this overlap exists (2009–2024).” Novelty claims require caution. Please soften to “to our knowledge” and/or add a brief sentence on search criteria; or remove the claim.

P2-n3 (Sec. II.A p.4; footnote 1)
- The long footnote giving the Wick-permutation factor mapping between Cai’s basis and yours belongs in an Appendix. Move it, or compress it, and keep Eq.(37) mapping precise but concise in the main text.

P2-n4 (Typographic clarity; multiple pages)
- Replace awkward strings like “10−4” with 10^−4 consistently; ensure all powers are typeset; avoid hyphenation breaks (e.g., “en￾ters”) in the final PDF.

P2-n5 (Sec. III.A p.7; Eqs. (3)–(4))
- State explicitly the cosmological parameters used (Ωm, H0, transfer function normalization) for any numerical σ or scaling statements that rely on M(k,z), even if the final overlaps are scale-free.

P2-n6 (Sec. VI.C, p.12; “realization-marginalized” language)
- When reporting “P(BF>3) = 99.9%,” include the exact N and the binomial SE once (you partly do in Table III). Ensure all such percentages carry the same precision and SE.

NITs (cosmetic)

P2-nt1 (Sec. VI.C p.12–13; use 10^5 consistently)
- Use 10^5 (or 3×10^5) consistently; avoid “105” to prevent confusion.

P2-nt2 (Fig. 2 caption, p.11)
- The caption contains several parenthetical clauses; consider simplifying. Also add explicit labels in the bar chart for which estimator each bar corresponds to (see P2-E7).

P2-nt3 (Fig. 1 caption, p.5)
- Add explicit axis labels (“k1/k” on x, “BNL” on y) and units if any; note the squeezed limit value as a horizontal reference line.

P2-nt4 (Sec. IX.E, p.24; AI tooling acknowledgment)
- The AI-tools sentence is fine but not standard for PRD. Leave it if the journal allows, otherwise move it to the Acknowledgments footnote.

Abstract-to-body consistency (pattern-045) audit
- All abstract scalars were recomputed and are traceable in the body: |fNL|=4.375; ratio ≈ 290; r-range [0.829, 0.876]; σ(fNL)=0.7 baseline; 5.2–5.5σ optimistic; 2.6–5σ post-budget; MegaMapper 7.4–7.7σ ideal; Bayes factors ≈9–14 (post-rebooking) and ≈10–17 (r→1); single-time-ordering half-value halves significance. Good.
- Caveat: the Bayes-factor headline relies on rebooking r; Table II currently reports only r→1 endpoint. Fix per P2-E5.

Figures and tables audit
- Fig. 1: Provide explicit axes and confirm Eq. (2) correction; Table I values are consistent with quoted numbers.
- Fig. 2: Include explicit estimator labels; the “naive” bar is flagged in caption as not used, which is acceptable; keep the “not directly comparable” warning per P2-E7.
- Fig. 4–5: Axes labeled; check units for kmin plot; the trends qualitatively match narrative.
- Table II–III: Numbers are internally consistent with formulas; add rebooked Bayes-factor column.

Arithmetic spot-checks
- 4.375/0.015 = 291.7 ≈ 290 (as stated).
- Template-corrected SPHEREx: 4.375×0.84/0.7 = 5.25; with r=0.829 gives 5.18; with r=0.876 gives 5.47 → reported 5.2–5.5 OK.
- GR σeff = sqrt(0.7^2 + 1.0^2) = 1.22 → 4.375×0.84/1.22 = 3.01 ≈ 3.0 OK.
- “All-combined” σeff = sqrt(0.9^2 + 1.0^2) = 1.345 → 3.675/1.345 = 2.73 OK; sqrt(1^2+1^2)=1.414 → 3.675/1.414=2.60 OK.
- MegaMapper ideal: 3.675/0.5 = 7.35; 3.85/0.5=7.7 OK.
- Bayes factor W/(√(2π) σeff): 30/(2.5066×0.7)=17.1; 30/(2.5066×0.833)=14.4 OK. Narrow prior [−5,+5] gives 4.01 exact vs 5.69 approx; your caution is correct.

Bibliography and provenance
- Citations appear consistent with years/outlets. Ensure that Planck PR4 values used (Jung et al. 2025) match the cited paper’s abstract/table. Preprints (Addis et al. 2025) are fine but label their status.

Page-length recommendation
- Recommend reducing the main text to ≤18 pages by moving detailed implementation logs, extended prior-sensitivity grids, and side channels (e.g., anomaly-detector and birefringence aside) to appendices or the Zenodo record.

## Summary recommendation
MAJOR REVISIONS

The paper contains a substantive physics/methods contribution (template-overlap quantification and a careful sensitivity recast), but PRD-level publication requires correcting the definitional/dimensional inconsistency around Eq. (2), resolving a clear numerical contradiction in the shot-noise discussion, and providing proper reproducibility artifacts (final Zenodo DOI, frozen code, and removal of internal filenames from the main text). Additional clarifications are needed for MC sample sizes, the injection-recovery uncertainty, and explicit Bayes-factor formulas/tables. Once these are addressed and the estimator juxtaposition labeling is made watertight, the manuscript could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS AFTER FRESH-EYES PASS

ESSENTIAL

P2-E8 (Sec. VII.E, Table IV; impact of ϵ-correction on headline significance)
- Problem: Table IV states the ϵ-correction “0.6–8% in fNL” yields “≲ 0.1σ effect.” This is too small. An 8% shift of |fNL| = 4.375 is Δ|fNL| = 0.35. With r = 0.84 and σ = 0.7, the change in significance is Δ(|fNL| r/σ) ≈ 0.35×0.84/0.7 ≈ 0.42σ, not ≲ 0.1σ. Even at 5% it’s ≈ 0.26σ.
- Required fix: Recompute and report the correct significance variation from the full 0.6–8% ϵ band (≈ 0.03–0.42σ at r = 0.84, σ = 0.7). Either (a) propagate this as an explicit asymmetric band on all r-corrected significances where you invoked “≲0.1σ,” or (b) justify a tighter ϵ prior (and update Eq. 12 band accordingly). Ensure all quoted “optimistic”/“realistic” ranges reflect this non-negligible contribution.

P2-E9 (Sec. IV, p.10; “Photometric redshift outliers” paragraph)
- Problem: Inconsistent math. You claim 10% catastrophic outliers degrade the bispectrum σ(fNL) by “∼5% (from 0.70 to 0.74),” then justify with a dilution factor fcat^2/(1+fcat)^2 ≈ 0.008 for fcat = 0.1 (i.e., 0.8%, not 5%). The 5% degradation is not supported by the displayed calculation.
- Required fix: Provide a consistent derivation for the 5% figure using a bispectrum Fisher that models inter-bin leakage and window smearing, or revise the text to reflect the 0.8% estimate (and explicitly note that additional window/mode-coupling effects could raise it). If you retain 5%, show the specific calculation leading to 5% and how it differs from the 0.8% dilution.

MAJOR

P2-M7 (Sec. III.A–B, VII.B; bϕ versus δc(b1−1) bookkeeping)
- Problem: The paper alternates between using the explicit universality form ∆b = 2 fNL (b1 − 1) δc/M and the shorthand ∆b ∝ fNL bϕ/k^2 with bϕ = 2δc(b1 − 1). This is fine formally, but later discussions of tree-level cross-terms in the bispectrum simultaneously reference both δc and bϕ and assert “not double-counted,” which is easy to misinterpret.
- Required fix: Add a one-paragraph “bias normalization” box clarifying the single, consistent convention used in forecasts. Explicitly show one example bispectrum term where bϕ appears and demonstrate no δc is reintroduced there if bϕ already absorbed it. This avoids confusion about double counting.

P2-M8 (Appendix A.1, Eq. (A7); unjustified 1/Sv symmetry factor)
- Problem: Eq. (A7) inserts a 1/Sv symmetry factor in the in-in correlator without derivation. In the operator formalism (as written), such diagrammatic symmetry divisions are nontrivial and require justification to match Cai et al.’s normalization. As written, it is unclear whether this 1/Sv is needed or double-counts against the explicit permutation sum.
- Required fix: Derive (or cite) the precise origin of the 1/Sv in the in-in/Wick expansion for each vertex structure, and verify that with this factor Eq. (A7) reproduces Cai et al.’s full bispectrum normalization at the three benchmark triangles. If the factor is redundant, remove it. State unambiguously whether the permutation sum S3 already accounts for identical leg permutations.

P2-M9 (Figures 4–5 captions and body; cross-channel comparability warnings)
- Problem: You were careful in Fig. 2 to caution about non-comparability of null procedures, but Fig. 4 (SDB σ vs kmin with a dotted bispectrum line) and Fig. 5 (bϕ-dependence of SDB alongside a fixed SPHEREx bispectrum σ=0.7 line) place different estimators/observables together without an explicit “not directly comparable” warning in-figure/caption.
- Required fix: Add in-caption notes that the overplotted bispectrum references are diagnostic anchors only and not directly comparable to the SDB Fisher curves. State which estimator each curve uses, matching the standard you set in P2-E7 for Fig. 2.

MINOR

P2-m11 (Sec. V, Fig. 2 caption; MegaMapper bars)
- Problem: The caption names four MegaMapper bars (“template-corrected ideal 7.4–7.7σ; illustrative 3–7σ envelope; conservative; single-tracer”) but does not numerically specify the latter two. The body gives several illustrative numbers (e.g., ~3.2σ), but there is no one-to-one mapping to the unlabeled bars.
- Required fix: Either label the bars numerically in-figure or specify the two missing numerical ranges in the caption and tie them to the text scenario (e.g., “conservative = σeff = √(0.7^2+1.0^2) with r = 0.84,” “single-tracer = [value] under [assumption]”).

P2-m12 (Sec. III.A, Eqs. (3)–(4); unit conventions)
- Problem: You state “k quoted in h Mpc−1 throughout,” but M(k, z) uses H0. The dimensionless form requires a consistent h convention (H0 = 100 h km s−1 Mpc−1). This is standard, but it should be spelled out once since you later show kmin-dependent figures.
- Required fix: Add a short sentence fixing units (k in h Mpc−1, H0 = 100 h km s−1 Mpc−1) and state the Ωm and transfer/growth normalizations used in any figure that depends on M (e.g., Fig. 4).

P2-m13 (Sec. III.B; “squeezed-cutoff insensitivity”)
- Problem: You state x3,min from 0.001 to 0.2 changes r by < 2×10−4. That is plausible but surprisingly tiny given folded/intermediate regions dominate mismatch. Readers will wonder about numerical stability.
- Required fix: Add one sentence noting the quadrature settings and triangle-grid convergence checks used for this specific cutoff sensitivity (e.g., number of triangles retained after the cutoff sweep) or move the detail into the code README and cite it.

P2-m14 (Appendix A; sign/normalization cross-check)
- Problem: The commutator identity i⟨[ζ^3, Hint]⟩ = −2 Im⟨ζ^3 Hint⟩ is correct, but the text would benefit from explicitly stating the vacuum-prescription and Hermiticity steps leading to ⟨Hint ζ^3⟩ = ⟨ζ^3 Hint⟩∗ (you half-state it). This underpins the “factor-of-two” closure you rely on.
- Required fix: Add a one-line derivation or reference (e.g., Weinberg 2005 in-in review) to make this airtight.

NITS

P2-nt4 (Sec. VII.C; “Corrected (10% residual; = Ideal, verification only)” row in Table III)
- Problem: The row equals “Ideal” by construction; then you quantify the literal σGR = 0.05 case in the caption. This is slightly confusing.
- Required fix: Either drop the equality row and only report the literal σGR = 0.05 result, or keep the equality row and move the literal 0.05 case to a footnote with a clear “not plotted” marker.

P2-nt5 (Sec. VIII.B; interval presentation)
- Problem: You quote c′ ∈ [0.7, 10] and then fNL(ns) ∈ [−4.35, −4.02]. Consider adding the two endpoint calculations inline (or in a footnote) to show the arithmetic, since this interval is used later.

Explanation of coverage
- The initial review focused on Eq. (2) dimensional issues, shot-noise inconsistency, reproducibility artifacts, Bayes-factor tabulation, MC notation, estimator comparability, and several methodological clarifications. The fresh pass targeted remaining arithmetic and consistency items. The principal new findings are the underestimation of the ϵ-correction effect on significance (P2-E8), the photometric-z degradation inconsistency (P2-E9), and the need to justify the 1/Sv factor in Eq. (A7) (P2-M8), plus additional clarity and comparability fixes for figures and unit conventions.