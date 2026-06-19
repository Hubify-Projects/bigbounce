# P2 D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=99e6426c pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6542 chars)
**Wall time**: 250.3s

---

Referee report for Physical Review D submission: “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Part A. Production/editorial visual QA (camera‑ready presentation; page numbers refer to the rendered PDF)

- D1-MAJOR, p. 11 (Fig. 2). The multi-bar “Survey Detection Significance” figure appears cramped in a single-column width. Tick labels and legend text are small and difficult to read. Required fix: Make Fig. 2 a full-width figure* with larger fonts; ensure colorblind-safe palette (see D6).

- D2-MAJOR, p. 15–16 (Table II). Table II is extremely dense, with long prose embedded in table cells and footnotes. In two-column layout it risks overflows and legibility issues. Required fix: Move Table II to a full-width table* and compress prose into a short caption; move explanatory text to the main body or an appendix.

- D3-MAJOR, p. 20 (Table IV). The consolidated systematic budget table is wide and text-heavy. In a two-column format, columns are tight and can wrap awkwardly. Required fix: Render as full-width table* and shorten per-row prose; move “Combination rule” explanations to caption.

- D4-MINOR, p. 28 (Table V). Table V fits, but the caption plus the parenthetical explanations are long. Required fix: Split the caption into a short caption plus a paragraph in the main text immediately before/after the table.

- D5-MINOR, p. 5–6. Orphaned subsection heading “B. UV-Completion Independence (Conditional on Faithful Cubic-Order Transfer)” lands at the bottom of p. 5 with no body text until p. 6. Required fix: Reflow pagination to avoid orphaned headings.

- D6-MAJOR, p. 22 (Fig. 6) and p. 11 (Fig. 2). Both figures rely on red/green color coding to indicate acceptance/exclusion regions and significance bars. Required fix: Adopt a colorblind-safe palette and add texture/patterns for grayscale print.

- D7-MINOR, p. 17 (Fig. 5). Axes are readable but small in single-column format. Required fix: increase font sizes slightly; ensure axis units (“%” on bϕ prior) are explicitly labeled.

- D8-MINOR, Throughout. Some author names with diacritics appear as LaTeX escape sequences in the text (e.g., “M¨unchmeyer”). Required fix: Ensure proper UTF-8 rendering of diacritics.

- D9-MINOR, Appendix A. Several long display equations (A2–A7) are close to the column width. Required fix: Use aligned environments to break lines consistently; avoid overflow into margins.

- D10-MINOR, Figures. Consider adding an additional 2D triangle-shape heatmap showing the bounce/local mismatch across configuration space (e.g., BNL/|BNL|squeezed over (k2/k3, k1/k3)), to complement 1D Fig. 1 and substantiate r and rcos results visually.

- D11-MINOR, Method flow. A one-panel flow chart of the “sensitivity recast” pipeline (inputs from Heinrich et al.; template mismatch r; systematic stacking assumptions; Bayes-factor post-processing) would improve readability and self-containment.

Part B. Methodology and statistical rigor audit

I audited all equations, table/figure numbers, reported σ-levels, ratios, and percentages for internal arithmetic and dimensional consistency. Below are findings, each with an ID, location, issue, and required action.

ESSENTIAL

- P2-E1 — Data and Code Availability, p. 24–25: “archived at Zenodo (DOI inserted at submission).” A placeholder remains. Required fix: Provide a permanent DOI and the precise frozen release tag/commit hash used for this paper. List the exact paths for all named artifacts (JSONs/py scripts) and confirm they exist in the archived snapshot.

- P2-E2 — Sec. III.B (Template Projection), p. 8–9 and reiterated p. 10–11: “SPHEREx-like” and “LSS/SPHEREx noise-weighted” schemes are invoked to produce r = 0.829–0.835, but the weighting definitions are not precisely specified (e.g., k-ranges, binning, mask treatment, redshift weights). Required fix: Provide explicit mathematical definitions for each weighting used to compute r (weights w(k1,k2,k3), triangle domain, binning, survey window approximations). Put these in an appendix or methods box and link to the corresponding code function names.

- P2-E3 — Sec. IV (Shot-noise caveat), p. 10: The paragraph mixes (i) a power-spectrum style Poisson degradation factor √(1+1/(nP0)) ≈ 3.3× for n ~ 1e-5 h^3 Mpc^-3 and (ii) a claim that the bispectrum estimator degradation at the squeezed modes is 15–30%. This reads as contradictory without a clear channel separation. Required fix: Cleanly separate channels (power spectrum SDB vs. bispectrum) and provide a quantitative, cited estimate for the bispectrum’s shot-noise degradation at the quoted number densities. If the 15–30% is heuristic, label it explicitly and give the formula/assumptions; otherwise remove/confine to an appendix.

- P2-E4 — Abstract and Sec. IV/VII, various pages: You present optimistic (5.2–5.5σ, template-corrected), mid, and conservative (2.6–5σ) significance values assembled by additive-in-quadrature stacking of systematics (GR, bϕ, photo-z, etc.). While you do state this is a “transparent scoping choice,” the main text and Fig. 2 juxtapose results from different null procedures and estimator regimes. Required fix: At every occurrence where two σ values from different null procedures are placed side-by-side (e.g., naive 6.25σ vs. template-corrected 5.2–5.5σ; bispectrum-only vs. SDB), include an explicit “not directly comparable” label in-line. The Fig. 2 caption already does this for naive 6.25σ; add the same explicit language in Sec. IV’s narrative where the two are contrasted and any other such juxtapositions.

MAJOR

- P2-M1 — Bayes factor bookkeeping clarity, Sec. VI.C, p. 12–16; Table II p. 15–16; Table III p. 18: The analytic derivations are correct as written, and your rebooked r ≈ 0.84 σeff inflation is consistent (e.g., 30/(√(2π)*0.833) ≈ 14.37). However, the presentation is unusually verbose and mixes delta-prior and Gaussian-prior results in the same table without a compact summary. Required fix: Add a compact summary table (or panel) showing just the four canonical corners for σeff = 0.7 and 0.833 (delta vs. Gaussian σtheory = 1; competitor width 10 vs. 30), with references to the detailed derivation below. This will prevent misinterpretation.

- P2-M2 — Weighting dependence of r and rcos, Sec. II and III.B, p. 4–9: The narrative refers to five coefficient sets, 10,000-sample null-space, and multiple weighting schemes, but the precise mapping from “scan measures” to the headline r = 0.84 ± 0.02 remains scattered. Required fix: Add a single consolidated table listing: (i) each weighting scheme name; (ii) its exact weight function; (iii) the resulting r with uncertainty and the coefficient-set dependence; (iv) the domain of triangle shapes used. Cross-reference the code functions.

- P2-M3 — Length vs. contribution, Entire manuscript (29 pages). This is a sensitivity recast (not an independent forecast). For PRD, 29 pages is long relative to the stated methodological increments. Required fix: Reduce the main text length by removing implementation file-name callouts scattered through the prose (move them to Data/Code Availability or an appendix) and trimming explanatory repetition. Target ≤ 20 pages main text plus appendices.

- P2-M4 — AI-tooling disclosure, Acknowledgments p. 27: You note use of “AI-assisted software tooling (Anthropic Claude) … for code development, consistency checking, and manuscript preparation.” PRD has policies regarding use of generative AI. Required fix: Consult PRD policy and either (i) move this to a neutral data/methods footnote describing that no text was generated without author oversight, or (ii) remove, if journal policy requires. Clarify that all scientific content and code were verified by the author.

- P2-M5 — Figure additions, Sec. III.B, p. 8–9: A 2D heatmap over triangle shape space would substantiate the claim that mismatch is “dominated by the folded region” and that squeezed-limit cutoffs do not move r materially. Required fix: Add a single 2D plot of Bbounce/|B|squeezed or the local-template cosine across triangle space with the survey Fisher weighting as the measure.

MINOR

- P2-n1 — Abstract and Sec. I, p. 1–2: “contrast |fbounceNL|/|finfNL| ≈ 290” using finfNL ≈ 0.015. Using ns = 0.9649 gives finfNL = (5/12)(1−ns) ≈ 0.014625 → ratio ≈ 299. Required fix: Either use 0.0146 and say ≈ 300, or retain 0.015 but note that the exact Planck-centered ratio is ≈ 300.

- P2-n2 — Sec. VII.E, Table IV p. 20: You state “ϵ-correction 0.6–8% in fNL … ≲ 0.4σ effect.” Check: 8% × 4.375 × r / 0.7 ≈ 0.42σ, consistent; add this one-line arithmetic in a footnote for clarity.

- P2-n3 — Sec. IV, p. 10: “The naive uncorrected |fNL|/σ = 4.375/0.70 = 6.25σ” then “template-corrected optimistic 5.2–5.5σ.” Add an explicit parenthetical as in Fig. 2 caption: “not directly comparable null procedures.”

- P2-n4 — Sec. VIII.A, p. 21: Planck PR4 recast states fNL = −0.1 ± 5.0 → f bounce NL = −0.1 ± 5.7 and “0.75σ from the bounce prediction.” Arithmetic check: |−4.375 + 0.1|/5.71 ≈ 0.75; OK. Recommend adding the intermediate Δ ≈ 4.275 number for transparency.

- P2-n5 — Notation consistency, Throughout: You mix “§VI” with “Sec. VI.” Required fix: Standardize to “Sec.” throughout.

- P2-n6 — Typos/formatting, Throughout: Occasional hyphenation artifacts (“en￾ters”, “per￾haps”) indicate copy-paste from parsed PDF. Ensure final typeset PDF has clean hyphenation and no stray Unicode artifacts.

- P2-n7 — Sec. IV, p. 10: The phrase “DBI inflation is intentionally not propagated…” can be misread. Suggest “DBI produces equilateral-type NG with vanishing local amplitude; hence it is not constrained by the local-template SPHEREx forecast here.”

QUANTITATIVE CROSS-CHECKS (all OK unless noted)

- Naive significance: 4.375/0.7 = 6.25σ (OK).

- Template-corrected: r ∈ [0.829, 0.876] → 4.375 r / 0.7 = 5.18–5.47σ (OK; reported 5.2–5.5σ).

- GR degradation: σeff = √(0.7^2 + 1.0^2) = 1.22 → 4.375*0.84/1.22 = 3.01σ (OK ≈ 3.0σ).

- Combined bϕ 30% + GR 1.0: σeff = √(0.9^2 + 1^2) = 1.35 → 3.675/1.35 ≈ 2.72σ (OK quoted 2.7σ).

- Combined bϕ 50% + GR 1.0: σeff = √(1.0^2 + 1^2) = 1.41 → 3.675/1.41 ≈ 2.60σ (OK).

- Planck PR4 recast: σloc = 5.0 → σbounce = 5.0/0.876 ≈ 5.71 (OK); |−4.375 + 0.1|/5.71 ≈ 0.75σ (OK).

- Bayes factors: delta prior, W=30, σ=0.7 → 30/(√(2π)·0.7)=17.07 (OK; table 17.10). Rebooked σeff=0.833 → 14.37 (OK).

- SDB joint Fisher identity check: σmarg = σunmarg / √(1−ρ^2) with ρ = −0.87 → 1.53/√0.243 ≈ 3.10 (reported 3.08; OK). Bias-marginalized: 1.75/√(1−0.969^2) ≈ 7.03 (reported 7.06; OK).

- Trispectrum order-of-magnitude: τNL ≈ (36/25) fNL^2 → ≈ 27.5 (OK; purely contextual note).

STANDALONE-READER TEST

- The paper is largely self-contained for a recast, but the definitions of the practical weighting schemes that produce the headline r values are currently too implicit (P2-E2). The template-mismatch computation should be reproducible from the text plus the archived code without guesswork.

UNCOMPUTED/QUALITATIVE CLAIMS THAT SHOULD BE NUMERIC

- P2-M6 — Sec. VII.D (Additional systematics), p. 19: Several effects are listed with “O(10–30%)” degradation but without a traceable computation (integral constraint, magnification bias for z>2). Required fix: Either add brief quantitative citations or move these into a clearly labeled qualitative discussion box stating they are not folded into the headline ranges.

ABSTRACT-LAST DRIFT SWEEP

- The abstract’s headline detection ranges (5.2–5.5σ optimistic; 2.6–5σ realistic) match the body (Fig. 2; Table IV). The Bayes-factor envelope (≈9–14 under r≈0.84 bookkeeping; 10–17 at r→1 endpoint) maps to Table II and the derivations in Sec. VI.C. The statement about the Cai/Li factor of two is backed by Appendix A. The note that systematics are combined in quadrature with a caveat is present in both abstract and body. No overclaims detected.

Bibliography spot checks

- Key references (Maldacena 2003; Planck 2018; Heinrich et al. 2024) are correctly cited and consistent with the numbers used. The Addis et al. (2025) relativistic power spectrum reference is used qualitatively; fine. Ensure all arXiv IDs and years match the cited works in the final reference list.

Recommended additions

- Add a short appendix or box explicitly defining all Fisher weights and survey cuts used to compute r and rcos, and listing the grid resolutions and triangle-domain parameterizations.

- Add a supplemental figure (full width) with the triangle-space mismatch heatmap under a representative SPHEREx weighting.

## Summary recommendation
MAJOR REVISIONS

The core statistical derivations and arithmetic checks out, and the paper is careful about distinguishing null procedures and caveats. However, before PRD acceptance, the presentation and methodology need tightening: provide a permanent code/data DOI; formalize the definitions of weighting schemes used to derive the headline r values; clean up the mixed-channel shot-noise discussion; reduce length by moving implementation file-name callouts out of the main text; and improve figure/table legibility with several full-width elements and colorblind-safe palettes. These changes are substantive but should be feasible without altering the scientific conclusions.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER FRESH-EYES PASS

ESSENTIAL

- P2-E5 — Eq. (2) definition/inversion and dimensional consistency (Sec. II.A, p. 3).
  Issue: You define AT = (3/256 k1^2 k2^2 k3^2) P (Eq. 1), then write BNL = (10/3) P/AT / Σi k_i^3 (Eq. 2). With this, P cancels and BNL ∝ k1^2 k2^2 k3^2 / Σ k_i^3, which has residual k-dimensions and loses all P(c1…c6) dependence—contradicting the next sentence (“no cancellation of P occurs”). To be dimensionless and to retain P, the numerator must be AT, not P.
  Required fix: Correct Eq. (2) to BNL = (10/3) AT / Σi k_i^3 (or provide the exact intended normalization consistent with Cai et al.), and adjust the surrounding text accordingly. Also fix the “i k3_i” notation to an explicit Σi k_i^3 (see P2-n8).

- P2-E6 — Units in M(k, z) (Eqs. 3–4, Sec. III.A, p. 7).
  Issue: M(k, z) = 2 k^2 T(k) D(z) / (3 Ωm H0^2) mixes k quoted in h Mpc−1 with H0 typically in km s−1 Mpc−1 unless c=1 and a consistent unit system is stated. As written, dimensional balance is ambiguous.
  Required fix: State explicitly the unit convention (e.g., c = 1; H0 in h Mpc−1; k in h Mpc−1) that renders M(k, z) dimensionless. Alternatively, include c factors or rescale H0 accordingly and add a sentence clarifying units.

- P2-E7 — Operator identity notation consistency (Appendix A and main text).
  Issue: The commutator identity is written in the body as i⟨[ζ^3, L]⟩ = −2 Im⟨ζ^3 L⟩, but Appendix A correctly uses Hint in the in-in formalism. Mixing L and H without stating Hint = −∫ d^3x L(3) can confuse readers and obscures the status of the −2 Im doubling.
  Required fix: Use Hint consistently in the commutator identity throughout, or add an explicit line stating Hint = −∫ d^3x L(3) and that the identity is applied to Hint. Update equations and surrounding prose for consistency.

MAJOR

- P2-M7 — Ambiguity in “CMB Fisher” weighting and its qualitative effect (Sec. III.B, p. 8–9).
  Issue: You list a “CMB Fisher, w ∝ k^2” weighting and then state it “preferentially upweights the squeezed configurations.” A k^2 weight generically upweights large-k modes; whether this increases weight of squeezed triangles depends on the exact three-k weighting prescription (which leg receives k^2, or whether a product/symmetric function is used). As written, the qualitative statement is questionable.
  Required fix: Precisely define the “CMB Fisher” weight used in the r computation (is it w ∝ k1^2+k2^2+k3^2, or a product, or ℓ-space Fisher mapped to k?), and revise the qualitative statement to match the actual definition. Cross-reference the code function that implements this weight (this complements P2-E2 from the first report).

- P2-M8 — All-combined 2.6–2.8σ endpoint consistency (Fig. 2 caption; Sec. IV, p. 10–11).
  Issue: The 2.6–2.8σ “all-combined conservative endpoint” is quoted while Table IV gives 2.6–2.7σ for r = 0.84. Hitting 2.8σ requires r ≈ 0.876 (CMB-Fisher endpoint). This mixes different r choices unless explicitly stated.
  Required fix: Tie each endpoint numerically to the r used (e.g., “2.72σ for r = 0.84; 2.85σ for r = 0.876”), and add an explicit “not directly comparable across r choices” qualifier wherever you juxtapose them. Update Fig. 2 caption and the narrative in Sec. IV accordingly.

- P2-M9 — Photo-z and magnification entries in “Additional systematics” (Sec. VII.D, p. 19).
  Issue: Several O(10–30%) degradations are cited for effects not folded into the headline ranges, without quantitative citations specific to the bispectrum channel (integral constraint, magnification bias at z > 2).
  Required fix: Add brief quantitative references for each listed effect (preferably bispectrum-specific), or move the entries into a clearly labeled qualitative box stating they are not included in the quoted σ ranges (complements P2-M6 from the first report).

- P2-M10 — Cosmology used for T(k), D(z) (Sec. III.A; global).
  Issue: You invoke CAMB Cℓ and Planck noise elsewhere, but the fiducial cosmology for T(k), D(z) in M(k, z) is not specified (Ωm, h, n_s, σ8, transfer/growth normalization).
  Required fix: State the fiducial cosmological parameters used to evaluate T(k) and D(z) (and the code/version), or declare that the r and shape-cosine results are strictly shape/ratio based and independent of cosmology (and where cosmology does enter for validation runs).

MINOR

- P2-n8 — Notation clean-up for Σi k_i^3 and permutation sums (Sec. II.A, p. 3–4).
  Issue: “i k3_i ≡ k3_1 + k3_2 + k3_3” and “P_{i̸=j̸=l} …” are hard to read and include stray combining characters likely from PDF parsing. This also affects readability in several monomial-sum lines.
  Required fix: Replace with standard ∑i k_i^3 notation and clean S3/orbit-sum notation; ensure proper Unicode/LaTeX rendering.

- P2-n9 — Clarify which r underlies each σ number in the “all-combined” range (Sec. IV; Fig. 2).
  Issue: The 2.6–2.8σ band conflates r = 0.84 and r = 0.876 unless spelled out (see P2-M8). Minor, but avoid reader confusion.
  Required fix: Add a parenthetical “(r = 0.84 central; r = 0.876 endpoint)” wherever the 2.6–2.8σ band is quoted.

- P2-n10 — Appendix A symmetry factor placement (Eq. A7).
  Issue: You write Bζ = −2 Im ∑v ∑σ (1/Sv) I(σ)v. Depending on how Iv has been defined (with or without internal leg permutations), some readers may expect Sv to multiply or divide. Not obviously wrong, but the convention should be stated.
  Required fix: Add one clarifying sentence defining Iv’s normalization and why the 1/Sv appears (to avoid double counting identical legs).

- P2-n11 — Minor caption/body synchronization (Fig. 5).
  Issue: The right panel caption uses the phrase “corresponding detection significance for fNL = −35/8,” but the body later discusses bϕ priors in percent with slightly different phrasing. Align the phrasing and ensure “%” is present on the horizontal axis (you already flagged font size in D7).

- P2-n12 — CMB-vs-LSS shape-cosine usage caveat (Sec. III.B).
  Issue: You appropriately note that rcos is computed in an unweighted shape metric and is only a heuristic for projection noise. A short parenthetical reminding that an LSS Fisher-weighted rcos would differ slightly would preempt misinterpretation.
  Required fix: Add one sentence explicitly stating that an LSS Fisher-weighted shape metric could shift rcos slightly, but the qualitative “small projection noise” conclusion is unchanged.

If these new issues are addressed alongside the items in the original report, the presentation and methodological clarity should meet PRD standards.