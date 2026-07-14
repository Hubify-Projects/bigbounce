# P1B P1EXACT91ad88e3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/project-context/peer-reviews/INT_v3/ROUND_2026-07-14-P1-EXACTPDF-91ad88e3-NONANTHROPIC/P1B/frozen/arxiv/paper1b_mcmc_companion.pdf` md5=246b407b pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4881 chars)
**Wall time**: 454.3s

---

Referee report for PRD (methods) on “Reproducible Cosmological Proxy and Pipeline Checks: Stock-CAMB ΛCDM+ΔNeff MCMC, Synthetic NaMaster Recovery, and a Generic Spectator-ALP Birefringence Fit” (P1B)

Scope of review
- Focused on methodology rigor, statistics, dimensional analysis, internal arithmetic, reproducibility claims, estimator declarations, and the traceability of all abstract/conclusion scalars to the body text.
- I read the full 21-page manuscript, all figures, tables, equations, captions, footnotes, and appendices.

Overall assessment
The paper documents three separate, limited-scope numerical exercises and is commendably explicit about what is and is not being claimed. However, several essential issues prevent acceptance in PRD in its current form: (i) abstract scalars that are not supported or derived in the body, (ii) unresolved placeholder identifiers and “to be inserted” text inside the manuscript, (iii) a mislabeled axis in a load-bearing figure, and (iv) several methodological items that require additional robustness checks or clarifications to prevent misinterpretation (especially the “systematic floor” language for a pipeline bias that is estimator-specific). In addition, the paper is longer than warranted for its contribution and contains a large amount of repository/version bookkeeping that belongs in a compact Data/Code Availability or a companion data note.

Findings

ESSENTIAL

P1B-E1 (Abstract, p.1): Unsupported “prior-predictive” fractions
- Offending text: “A prior-predictive calculation finds 11.6% of fixed-coupling draws and 6.1% of broad-coupling draws within the published 1σ band…”
- Problem: These two percentages do not appear anywhere in the body, tables, or appendices; no derivation, no definition of the “1σ band” used, no estimator declaration, and no artifact pointer. They are not reproducible from the text.
- Required fix: Either (a) supply a section in Sec. VI or Appendix C with the exact prior-predictive protocol (priors, random seeds/sizes, β-band definition, tolerance, and the chain/artifact file name), report the numbers with uncertainties, and link to the archived outputs; or (b) remove these two figures from the abstract and conclusions.

P1B-E2 (Introduction, p.2; multiple occurrences): Placeholder arXiv ID in the body
- Offending text: “Paper I(a) … [arXiv:XXXX.XXXXX] … placeholder.”
- Problem: PRD cannot accept manuscripts with placeholder identifiers embedded in the main text.
- Required fix: Replace all placeholders with the actual arXiv ID (or remove the inline citation) before acceptance. Ensure no residual “placeholder” language remains anywhere in the PDF.

P1B-E3 (Data and Code Availability, p.16; Appendix A, p.18): “DOI pending/identifiers will be inserted”
- Offending text: “DOI assignment is pending (identifiers will be inserted at submission)… No DOI is fabricated here. In the interim…”
- Problem: Non-final archival references and forward-looking language are not acceptable in a published PRD paper. Persistent, citable archives must be in place at acceptance.
- Required fix: Provide finalized DOIs (Zenodo or equivalent) for all frozen artifacts (chains, NaMaster outputs, ALP chains) referenced in the text, and remove all “will be inserted” wording. If Git commit hashes are retained, confine them to a succinct Data Availability paragraph; do not rely on mutable URLs.

P1B-E4 (Fig. 2 caption/panel a, p.7): Axis label mismatch
- Offending item: Panel (a) shows the marginal of ΔNeff, but the x-axis label reads “Neff.”
- Problem: Mislabeling a key parameter on a figure used to support an abstract result is unacceptable; it can mislead readers.
- Required fix: Relabel the x-axis as “ΔNeff” (or “Neff − Neff,SM”) consistently in figure and caption, and ensure all related text uses the same symbol.

MAJOR

P1B-M1 (Sec. IV, pp.8–10; Fig. 3): Estimator-specific “systematic floor” wording
- Offending text: “we carry the worst case |Δβ̂| = 0.040° forward as the NaMaster systematic floor (deconvolution-algebra bias on foreground-free skies; not a real-sky bias bound).”
- Problem: “Systematic floor” suggests a lower bound on systematic uncertainty; here the effect is demonstrably estimator-specific (unweighted χ2), and 80% disappears with inverse-variance weighting. The current phrasing risks misinterpretation.
- Required fix: Reword throughout to “observed MC bias for the unweighted χ2 template estimator on foreground-free synthetic skies.” Do not call it a “floor.” State the corresponding weighted-estimator bias value and its uncertainty next to it, and keep the “not a real-sky bound” caveat in-line wherever the number appears.

P1B-M2 (Sec. IV, pp.8–10): Missing noise-level robustness
- Offending scope: All MC results and the bias attribution are at ΔP = 10 μK·arcmin only.
- Problem: The claim that the dominant bias originates from equal-weighting of noise-dominated high-ℓ bins should be shown to vary predictably with noise amplitude.
- Required fix: Add at least a two-point noise sweep (e.g., ΔP = 5, 10, 20 μK·arcmin) for the canonical mask to demonstrate (i) the change in the unweighted-bias magnitude with noise level and (ii) the stability of the weighted estimator. Report β̂ means ± SE and per-realization σβ for each case.

P1B-M3 (Sec. IV, pp.8–10): Limited ℓ-binning/ℓ-range robustness
- Offending scope: Single 20-bin linear scheme, with only a binary test “restrict to ℓ ≤ 1024 changes nothing.”
- Problem: If the unweighted estimator over-weights noisy high-ℓ bins, then dropping the upper bins or adopting coarser binning should reduce the bias. This is an important cross-check of the bias attribution.
- Required fix: Add a minimal ℓ-range/ℓ-binning robustness set (e.g., drop highest 2–4 bins; rebin to 10 linear bins) and report the recovered β̂ and bias change. If unchanged within SE, state so explicitly.

P1B-M4 (Sec. V B, p.10–11; Release-pairing note): Mixed Planck PR4 high-ℓ with 2018 low-ℓ/lensing in the primary frozen chains
- Problem: You do provide a verification re-run (“c15”) with PR4-consistent low-ℓ/lensing and 0.04σ agreement in ΔNeff for the Planck+BAO+SN combo. However, the headline “full-tension” chain (with H0 and DES-Y3) still uses mixed releases only, and no PR4-consistent cross-check is shown for that exact stack.
- Required fix: Either (a) provide the same PR4-consistent re-run for the full-tension combination and report the ΔNeff shift (or a bound), or (b) move the PR4-consistent Planck+BAO+SN result into the headline summary and demote the mixed-release full-tension numbers to a secondary row, with a prominent limitation note.

P1B-M5 (Sec. IV, Fig. 3 caption, p.8; text pp.8–10): Clarity on “template SNR” vs “angle SNR”
- Problem: While footnote 4 defines SNRtmpl, the figure caption itself juxtaposes β̂ and “template-fit SNR” without recalling the definition, inviting confusion with the SNR of β̂ per realization.
- Required fix: Add “SNRtmpl ≡ [∑b (Ceb,th/σMC,b)2]1/2 (not the SNR of β̂)” in the caption or an immediate parenthetical in text where SNR values (20.32, 25.71) are first quoted.

P1B-M6 (Acknowledgments, p.17): Vendor-specific AI acknowledgments
- Offending text: “Anthropic Claude… OpenAI GPT-5/o3, xAI Grok-4, Google Gemini 2.5…”
- Problem: PRD discourages vendor advertising language in acknowledgments. If AI assistance is acknowledged, it should be generic and free of promotional product/version strings.
- Required fix: Replace with a single neutral sentence acknowledging “AI-assisted tools were used for code generation and cross-checks under the author’s supervision,” or remove entirely.

P1B-M7 (Sec. VI, pp.11–15; Table IV p.16): One-sided spectator fractions are prior-dependent—need explicit caveat in abstract or main text where first quoted
- Problem: The 44% (Ωa < 0.1) and 13% (Ωa < 0.01) subset masses are strongly prior-dependent (θi prior in particular). While you mention prior dependence in-body, the first place where a subset fraction is highlighted (Abstract) lacks an explicit “prior-dependent” qualifier.
- Required fix: Add “prior-dependent” language next to the spectator-fraction claim in the Abstract, or move such numerical subset fractions out of the Abstract and keep them in-body with the existing caveats.

MINOR

P1B-m1 (Table II, p.6): One-sided 95% ΔNeff limits absent from the table
- Problem: The one-sided 95% limits (0.31 and 0.40) are only buried in the running text.
- Required fix: Add a small row/footnote to Table II listing the one-sided 95% upper bounds (with your precise truncated-posterior definition).

P1B-m2 (Sec. III A, pp.3–4): Reduced Planck mass convention
- Problem: You switch between GN and MPl without reiterating “reduced” every time. While correct, it can confuse readers.
- Required fix: Add a short parenthetical after Eq. (2): “using the reduced MPl (MPl−2 = 8πGN).”

P1B-m3 (Sec. V A, p.10; Table III p.11): “diagnostic (not in headline)” and similar internal-process language in table
- Problem: PRD tables should avoid internal pipeline/process tags.
- Required fix: Move such notes to the caption or text; keep the table content factual (dataset stacks).

P1B-m4 (Sec. V B, p.10): Chain convergence for the c15 re-run
- Problem: You quote R̂ − 1 = 0.0147 for the independent re-run; this is above your own convergence threshold (< 0.01).
- Required fix: Either continue the run to R̂ − 1 < 0.01 and update the numbers, or explicitly mark it “sub-converged test only; used solely as a release-pairing cross-check; main results from converged frozen chains (R̂ − 1 ≤ 0.003).”

P1B-m5 (Fig. 1 caption, p.5): Sample counts
- Problem: Caption quotes “119,617 post-burnin samples” but the footnote and text list several slightly different numbers (123,129 post-burn-in; thinned figures).
- Required fix: Ensure exact consistency (state whether reported counts are pre/post thinning and use the same variant in caption and body).

P1B-m6 (Appendix A, p.18): “expunged”/bug-process prose in the main text
- Problem: Over-detailed internal process language appears in the main manuscript.
- Required fix: Move the column-permutation bug provenance to a short Supplemental or a README in the repository; keep only a single-sentence note that a corrected file is used.

P1B-m7 (Sec. II, p.3): H0/MB tension quantification phrasing
- Problem: You do state that the 3.2σ and 3.6σ are not directly comparable. Good. For full clarity, add a parenthetical reminding which uncertainties each σ uses.
- Required fix: Add “(normalized to σMB of this chain vs. survey-to-survey uncertainty in H0, respectively).”

P1B-m8 (Sec. VI, p.13): Coupling prior extension rationale
- Problem: You state that [1,4) “lies entirely below the minimum coupling ≈ 8.6 required to reach the central value” but then that [4,8.6) “remains posterior-supported.” The logic is correct but could be misread as contradictory.
- Required fix: Clarify explicitly: “[4,8.6) cannot reach the central value βobs but is allowed because the Gaussian summary likelihood admits β below the central value.”

NITS

P1B-n1 (Table II note, p.6): “agreement at the 0.01σ level”
- Problem: The means are identical; “0.01σ level” is a slightly awkward phrasing for identical centroids with slightly different σ. Not wrong, but odd.
- Suggested fix: Replace with “centroids identical; uncertainties differ by 0.001.”

P1B-n2 (Typography, multiple pages): Inconsistent MPl/Mpl capitalization
- Suggested fix: Standardize to “MPl” (reduced Planck mass) everywhere.

P1B-n3 (Appendix C, p.20): “Effect of the summary-likelihood approximation” sentence is long
- Suggested fix: Split into two sentences.

P1B-n4 (Sec. IV, p.6–10): Where possible, abbreviate repeated parenthetical pathnames to a single reference in Data Availability.

Length
- At 21 pages, the paper is long relative to its stated scope (a stock-CAMB ΔNeff proxy report, a synthetic NaMaster recovery check, and an ALP accommodation exercise). I recommend trimming to ≤ 12–15 pages by:
  - Moving long chain-accounting footnotes and repository-path discussions to a brief Supplemental or the repository README.
  - Consolidating the robustness battery into a concise table plus one paragraph summary.
  - Relocating the AI-acknowledgment and versioning details to minimal form.

Abstract-last drift sweep (pattern-045)
- With the exception of the unsupported “11.6%/6.1%” prior-predictive fractions (ESSENTIAL; P1B-E1), the abstract’s numerical claims match the body: ΔNeff means and σ’s (Table II), NaMaster biases (Sec. IV; Fig. 3), ALP fixed-coupling β estimate (Eq. 7), and median m ≈ 36 H0 (Table IV / Sec. VI). The LiteBIRD 9σ vs 0.7σ distinction is correctly framed.

Provenance surfaces (patterns-046/047)
- The paper includes a great deal of provenance. Before acceptance, finalize DOIs and remove “pending/insert” language (ESSENTIAL; P1B-E3). Keep commit hashes to the Data Availability only.

Uncomputed quantitative claims (pattern-048)
- The only clear offender is the abstract’s 11.6%/6.1% (P1B-E1). Most other claims are adequately quantified or caveated.

Standalone-reader test
- The paper is self-contained as to the three numerical exercises. However, all placeholder IDs must be resolved (P1B-E2). No result should depend on opening “Paper I(a).”

Effect sizes and null-procedure distinctions
- Generally well handled. The “3.9σ” naive combination is correctly labeled as an upper bound with positive correlation caveat. The MB/H0 σs are flagged as not directly comparable.

## Summary recommendation
MAJOR REVISIONS

The manuscript cannot be accepted as is. Key blockers are the unsupported abstract percentages (11.6%, 6.1%), placeholder identifiers and “DOI pending/insert” language inside the paper, a mislabeled axis on Fig. 2, and the need to rephrase and minimally extend the NaMaster robustness (noise sweep, ℓ-binning/ℓ-range) to prevent misinterpretation of an estimator-specific bias as a “floor.” Additional minor editorial and presentation refinements will also improve clarity and suitability for PRD. Once the essential and major issues are addressed, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P1B-E5 (Sec. VI, LiteBIRD separation formula): Mis-specified uncertainty combination
- Offending text: “(|0.342 − 0.27|/ √ 0.032 + 0.0942 ≈ 0.7σ)”
- Problem: The denominator should combine uncertainties in quadrature, i.e., √(0.03^2 + 0.094^2). As written, “√ 0.032 + 0.0942” is ambiguous and dimensionally wrong. The numeric conclusion (≈0.7σ) is only correct if the intended expression has squares.
- Required fix: Replace by “|0.342 − 0.27| / √(0.03^2 + 0.094^2) ≈ 0.7σ.”


MAJOR

P1B-M8 (Sec. VI; Table IV): Spectator-fraction classification uses small-angle approximation without boundary validation
- Context: The Ωa subsets (44% for Ωa < 0.1; 13% for Ωa < 0.01) are computed using the small-angle quadratic approximation V ≈ ½ m^2 a ϕ^2 (Eq. 12), with an 8% stated error at θi ∼ 1 and ≲1% within Ωa ≤ 0.01.
- Problem: The 44% mass fraction at Ωa < 0.1 is close enough to the boundary that a few-percent systematic in Ωa could change counts. No spot-check is shown near the Ωa = 0.1 threshold where θi may be O(0.5–0.7).
- Required fix: Validate the Ωa < 0.1 classification with full EOM energy computation for a random subset of samples near the boundary (e.g., 100–200 points with 0.08 ≤ Ωa,approx ≤ 0.12). Quote the misclassification rate and confirm the reported 44% is stable within stated uncertainties.

P1B-M9 (Sec. III A, footnote 2): “Propagating torsion” inconsistency
- Offending text: “above this scale the contact-operator description breaks down and the full Holst-sector dynamics with propagating torsion must be retained.”
- Problem: The manuscript elsewhere stresses that in minimal ECH the torsion is algebraic (non-propagating). The footnote’s “propagating torsion” phrasing contradicts that point and may mislead readers into thinking a kinetic term exists in minimal ECH.
- Required fix: Clarify that the contact-operator EFT breaks down near the strong-coupling scale, where the full algebraic torsion (still non-propagating in minimal ECH) must be treated at the action level; remove “propagating” unless you explicitly introduce a kinetic term beyond minimal ECH.


MINOR

P1B-m9 (Eq. 1; notation): κ-symbol definition ambiguity
- Offending text: “κ 2 = 8πGN = M−2 Pl” appears after a coefficient written with “− 3κ 2 /16 ...”
- Problem: The typography makes it unclear whether “κ 2” means κ^2 or κ/2. While the intent is κ^2 ≡ 8πG = M−2 Pl (reduced), the spacing and superscript use are inconsistent across lines.
- Required fix: Define explicitly “κ^2 ≡ 8πG = M−2 Pl (reduced Planck mass)” once and use κ^2 consistently thereafter.

P1B-m10 (Sec. III A): Mixed unit conventions in α definition
- Offending text: “α = κ^2 (ℏc)^2/32” then immediately proceeds in natural units.
- Problem: Mixing SI factors (ℏc) with an otherwise natural-units derivation is confusing.
- Required fix: State up front that you work in natural units (ℏ = c = kB = 1) and drop (ℏc); or carry SI consistently.

P1B-m11 (Sec. IV, footnote 4 and sky-fraction sweep text): Angle-SNR definition inconsistency
- Offending text: “|β̂|/σβ = 5.2 per realization (fsky = 0.32).”
- Problem: This “angle SNR” is computed using the recovered |β̂| (≈0.238°), not the injected 0.27°. Readers may expect SNR ≈ βinj/σβ ≈ 0.27/0.046 ≈ 5.9.
- Required fix: Define which convention you use and, for clarity, give both numbers: |β̂|/σβ and βinj/σβ.

P1B-m12 (Eq. 7; units): Angle labeled “rad”
- Offending text: “= 4.93 × 10−3 rad × 180°/π ≈ 0.28°.”
- Problem: β is dimensionless; writing “rad” in the intermediate line is colloquial but can be confusing.
- Suggested fix: Replace by “= 4.93 × 10−3 (in radians) × 180°/π …” or omit “rad.” 

P1B-m13 (Table IV caption and entries): Heterogeneous reporting of m/H0 quantiles
- Problem: For subsets you report m/H0 as 16/50/84 percentiles (e.g., 4.7/37.7/264), but for the “full chain” row you provide only “median ≃ 36 (broad).”
- Required fix: Report consistent quantiles for all rows (or state explicitly why the full-chain marginal is not summarized with the same 16–50–84% format).

P1B-m14 (Appendix C, “Effect of the summary-likelihood approximation”): Mean/median wording
- Offending text: “the reported posterior medians (m ≃ 36 H0 …) are set by the mean of the same Eskilt–Komatsu datum…”
- Problem: This mixes “median” and “mean.” 
- Required fix: Rephrase to avoid conflating statistics (e.g., “the posterior central values are anchored by the central value of …”).

NITS

P1B-n5 (Typographic precision): Use of “rad” and missing squares in uncertainty combinations
- Suggest standardizing angle units phrasing (dimensionless; convert to degrees at the end), and ensure all uncertainty combinations are written with explicit squares under the square root to avoid ambiguity.

These items are in addition to, and do not repeat, the findings already listed in my initial report.