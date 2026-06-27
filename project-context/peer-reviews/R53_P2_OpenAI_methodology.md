# P2 R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P2/02_full_draft.pdf` md5=7a1425ed pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7123 chars)
**Wall time**: 367.8s

---

Referee report — Physical Review D methodology review

Scope of this review
I evaluated the full 28‑page manuscript including abstract, figures, tables, equations, appendices, and references, with emphasis on methodological rigor, derivation chains, statistical validity, error propagation, arithmetic consistency, and reproducibility. Below I list all issues found, classified by severity.

ESSENTIAL (must fix before acceptance)

P2-E1 (Abstract; p.1 and throughout; Data and Code Availability, p.24)
Problem: Reproducibility placeholder remains. “archived at Zenodo (DOI inserted at submission).” No frozen DOI, no tag, no commit SHA are provided for the code/data used to produce the numbers (r values, Bayes factors, Monte Carlo ensembles, figures).
Required fix: Provide a permanent archive DOI (Zenodo/OSF), the exact tag or commit SHA for the repository used to produce the paper’s results, and a manifest mapping each figure/table/number to the script and input hashes. Replace the placeholder with the actual DOI.

P2-E2 (Sec. VI.C; pp.12–16; Table II pp.15; Table III p.19)
Problem: Bayes-factor methodology for the Gaussian bounce prior is not explicitly written down. The text says “with the bounce likelihood replaced by the prior-convolved marginal,” but only Eq. (8) (delta prior) and its CDF form (Eq. (9)) are shown. Yet Tables II–III report numbers for σtheory = 1.0 Gaussian bounce prior (e.g., BF = 9.80).
Required fix: Write the explicit analytic expression used for the Gaussian bounce prior case (closed form of the convolution integral: a product of Gaussians integrated over fNL) and show the derivation or a direct reference with equation numbers. Include the exact input parameters (σeff used, prior bounds, any hyperpriors) to make BF values reproducible from the text alone.

P2-E3 (Sec. II.C; pp.6–7 and Sec. VIII.B p.19–20)
Problem: Quantitative claim “ϵ-correction 0.6–8%” rests on a schematic range for κϵ ∈ [5.6, 80] (“≈14× the prefactor-only value”) without a derivation or a controlled bound. This range feeds the systematic budget and Bayes-factor prior widths.
Required fix: Either (a) provide a derivation (or numerics) bounding κϵ with clear assumptions (mode-function dependence and AT(ϵ) scaling treated consistently across all four vertices), or (b) remove the 80 endpoint, replace 0.6–8% with a defensible bound supported by a calculation (even if conservative), and propagate the revised range into the systematic budget and headline language.

P2-E4 (Sec. III.B; pp.8–9, Eq. (5), Eq. (6); Abstract p.1)
Problem: The “SPHEREx-like” and “LSS/SDB” Fisher weights used to compute the amplitude-recovery factor r are not fully specified (which exact w(k1,k2,k3), triangle-bin edges, k‑cuts, redshift weighting, and noise model define each line in the r = 0.829–0.876 span?).
Required fix: Provide explicit mathematical definitions for each weighting used (CMB Fisher, SPHEREx bispectrum Fisher, scale-dependent-bias 1/k^2, any mask variants), exact integration limits, and the triangle grid resolution. Add a small table listing r for each weighting with numerical values (central and uncertainty from numerical integration).

P2-E5 (Sec. II.A–B; pp.3–6)
Problem: Null-space sampling is basis dependent by construction, but the reported “r = 0.85 ± 0.13 (range 0.55–1.14)” is used to motivate robustness claims and a “16th percentile floor” (4.4–4.7σ pre‑systematics). No check is provided for invariance under a linear reparametrization (e.g., random orthogonal transforms) of the six-monomial basis beyond the statement that the shape cosine rcos is stable.
Required fix: Add a robustness test that repeats the 10,000‑sample null-space scan under at least one orthonormal rotation of the six‑monomial basis (or an explicitly different monomial normalization) and report how the r distribution changes. If materially different, qualify the “16th percentile floor” accordingly or replace it with a basis‑invariant robustness statement.

P2-E6 (Sec. II.A; Eq. (2), p.3; Fig. 1 caption p.5; Table I p.5)
Problem: Definition of BNL (Eq. (2)) lacks the exact normalization used in the local-template projection (i.e., how Slocal is normalized in the Fisher product; “Stempl ∝ Slocal” is vague). For reproducibility of r and rcos, the precise normalization is required.
Required fix: Specify the exact normalization of Stempl (L^2 norm over the same triangle grid and measure used for Sbounce) and confirm whether Slocal is normalized to unit norm before computing rcos. If different normalizations are used between r and rcos channels, state them explicitly.

P2-E7 (Sec. II.B, Appendix A; pp.6–7, 24–26)
Problem: The operator‑algebra identity i⟨[ζ^3, Hint]⟩ = −2 Im⟨ζ^3 Hint⟩ is correctly stated, but the paper relies on benchmark‑point matching (Table I) and algebraic arguments rather than a minimal numerical reproduction of one full bispectrum integral to close the normalization audit. Given this single factor‑of‑two underwrites the headline forecast, at least one explicit numeric evaluation (beyond the three benchmark limits) should be shown.
Required fix: Provide one intermediate‑shape numerical evaluation of the full (−2 Im) integral (for a non‑squeezed, non‑folded, non‑equilateral triangle) that reproduces the Cai et al. value and differs by exactly a factor of two from the Li et al. single‑ordering value, or provide a symbolic demonstration with explicit Wick‑contraction counting that maps precisely onto the coefficients of Eq. (37) in Cai et al. including the in-in doubling.

P2-E8 (Sec. II.C; p.7; assumptions list)
Problem: Assumption (d) “faithful transmission of the bispectrum through the bounce at third order” is acknowledged as the weakest link; yet quantitative forecasts are presented without a systematic uncertainty term for possible third‑order transfer failure (beyond a verbal “∼10^−3” scaling argument).
Required fix: Introduce an explicit “bounce‑transfer” uncertainty term (even as a labeled scenario band), quantify it (with a bound or a parametric scaling study), and propagate into the final significance ranges and Bayes‑factor tables. Label it clearly as conditional if you keep the “assumption (d)” formulation.

P2-E9 (Sec. VI.C; Abstract p.1; Table III p.19)
Problem: Inconsistent Monte Carlo sample sizes are reported. Abstract: “three independent 10^5‑realization ensembles.” Table III caption: “P(BF > 3) … fraction of 2×10^5 mock‑detection realizations.” Sec. VI.C also mentions “2×10^5 draws per σeff.”
Required fix: Harmonize and document the exact NMC used in each Bayes‑factor computation, clearly distinguishing between (i) the analytic closed‑form evaluations (no MC uncertainty) and (ii) the MC validation runs, with their sample sizes and resulting sampling errors.

P2-E10 (Sec. IV; p.10; Table IV p.20)
Problem: Systematics are combined “additively in quadrature” even when they are not statistically independent (e.g., GR projection and bϕ uncertainties may covary). The paper acknowledges this choice is a “transparent scoping choice,” but it is then used for the headline realistic range 2.6–5σ.
Required fix: Provide at least one joint‑marginalization check with a 2D (GR × bϕ) covariance toy model (even with conservative correlation coefficients ρ = ±0.5), showing how the 2.6–5σ envelope moves. Alternatively, clearly downgrade the 2.6–5σ to a scenario range (not a single “realistic” range) in the abstract and conclusions.

MAJOR (significant revisions needed)

P2-M1 (Sec. II.A; p.4; coefficient sets)
Problem: The text mentions “five Cai polynomial coefficient sets satisfying the benchmark constraints” (Sec. III.B) in addition to the 10,000 null‑space samples, but only one explicit set (2, 7, 3, −12, −69, 19) is printed.
Required fix: List the five exact coefficient sets used for the CMB‑Fisher overlap cross‑check (or provide them in a small table or appendix) so that readers can reproduce the r = 0.867–0.888 spread.

P2-M2 (Sec. II.A; pp.3–5)
Problem: The triangle-grid setup states “50 logarithmic bins per side,” convergence checked at “100 and 200,” but no explicit kmin, kmax are given (only a qualitative note that scale‑free shapes imply dependence on ratios). Without the exact grid definition, rcos cannot be reproduced.
Required fix: State the explicit dimensionless triangle ratio domain used (e.g., x2 = k2/k3 ∈ […], x1 = k1/k3 ∈ […], triangle inequality enforced), including any bin‑edge conventions and the antialiasing/measure used. Confirm that reshaping to ratios is indeed what is implemented in the released code.

P2-M3 (Sec. III.B; p.9; injection–recovery test)
Problem: The 2D flat‑sky KSW‑type injection–recovery test uses “SPHEREx photometric‑z power spectra as the diagonal noise covariance” on tiled flat‑sky patches but lacks key details (ℓ range, patch size and overlap, filtering, beam, mask treatment). The reported ±0.01 precision on rmeas with only 200 realizations is not verifiable without these.
Required fix: Specify the ℓ‑range, patch geometry, tiling strategy, noise level/beam, and the estimator normalization used. Report the sample variance of the recovered r over the 200 runs and the standard error of the mean to justify the ±0.01 quoted uncertainty.

P2-M4 (Sec. VII.B; p.16–18; Fig. 5)
Problem: The 20%, 30%, 50% priors on bϕ and their propagation to σ(fNL) (e.g., “SPHEREx widens to 0.9–1.0”) are asserted without an explicit Fisher‑matrix re‑solve under those priors (even schematically). This is load‑bearing for the 2.6–5σ envelope.
Required fix: Provide a simple Fisher‑matrix calculation (or cite a published calculation with numbers) that shows σ(fNL) as a function of σ(bϕ)/bϕ for the SPHEREx bispectrum channel. If done via Heinrich et al.’s public pipeline, cite it and show the numeric mapping (a small table suffices).

P2-M5 (Sec. IV; p.10; “shot-noise caveat”)
Problem: The “naive Poisson amplitude scaling gives σ inflated by √11 ≈ 3.3× … for n̄ ∼ 10^−5” and then “effective degradation … ∼15–30%” are asserted without calculation details and appear inconsistent with each other.
Required fix: Show the calculation behind both numbers, clarify the regime (k‑bins, z, P0 used), and reconcile the apparent contradiction (3.3× vs 15–30%). If the 3.3× number applies to a different observable or regime, state it unambiguously.

P2-M6 (Fig. 2; p.11)
Problem: The bar “naive uncorrected 6.25σ” is plotted alongside the template‑corrected bars. While the caption notes it is “shown only for reference,” the figure as presented invites direct comparison of quantities from different null procedures.
Required fix: Add a visual separator or explicit “not directly comparable” label on the figure itself (e.g., bracketed label or a different subplot), and state in the caption that the 6.25σ bar is a different null procedure and cannot be compared directly.

P2-M7 (Sec. V; p.11–12)
Problem: MegaMapper “3–7σ” range combines design uncertainty and systematics into a single informal envelope. No concrete survey configuration or Fisher inputs are specified, yet this range appears in the abstract.
Required fix: Either provide one concrete MegaMapper configuration with inputs and a quantitative σ(fNL) value after r‑correction (and separately list the design‑uncertainty band), or move the “3–7σ” range to a speculative discussion and remove it from the abstract headline.

P2-M8 (Sec. IX.D; pp.21–22)
Problem: Joint (fNL, nfNL) Fisher numbers (σ(nfNL) = 0.295/0.596; σmarg(fNL) = 3.08/7.06) are given, but the exact SDB Fisher inputs (kmin, kmax, window, redshift‑binning, tracer biases, number densities) are not provided.
Required fix: Supply a table of the six bins with n(z), b1(z), fsky, k‑range, and the kernel used for the SDB Fisher (M(k, z), Pm(k)), so that these numbers can be reconstructed.

P2-M9 (Sec. III.A; p.7)
Problem: Eq. (4) defines M(k, z) but does not state whether Φ or ζ is used downstream in δ = M × (field), and whether c = 1 units (c = 1) are assumed. This is relevant because of the factor mapping discussed in Appendix A.
Required fix: State explicitly which primordial variable couples to M(k, z) in your pipeline (Φ vs. ζ) and whether c = 1 units are assumed; add a one‑line check that your Eq. (3)–(4) recover the canonical Dalal et al. Δb(k) expression.

P2-M10 (Sec. VIII.A; p.18–19)
Problem: Planck PR4 recast: you state “recasting … with r = 0.876 gives fNL^bounce = −0.1 ± 5.7 (0.75σ from bounce).” The 0.75σ distance appears to compare to the central −4.375 prediction without r. If the observable is the local fNL (gauge frame), the distance should be |−0.1 − (−4.375)|/5.71 = 4.275/5.71 = 0.75 (OK). Please show the arithmetic inline or in a footnote for transparency.
Required fix: Add the explicit arithmetic or a short footnote confirming the 0.75σ number.

MINOR (address but can proceed)

P2-N1 (Throughout; multiple pages)
Problem: Overloaded notation “r” (template overlap) vs “rt” (tensor‑to‑scalar ratio). You note an attempt to avoid collision, but “r” appears very frequently without a subscript/context on some pages.
Required fix: Add a one‑line reminder near the first use in each major section, or use a distinct symbol for the template‑overlap factor (e.g., ρ or α) to avoid misreading.

P2-N2 (Fig. 1; p.5)
Problem: y‑axis label “BNL(k1, k, k)” is clear, but it would help to label the x‑axis as “squeeze ratio k1/k (dimensionless)” explicitly in the axis, not only in the caption.
Required fix: Update axis label.

P2-N3 (Sec. IV; p.10)
Problem: The “1/√fsky ≈ 1.19” degradation is presented in a CMB‑style aside for a 2D flat‑sky test. This may confuse readers since the main observable is a 3D bispectrum in LSS.
Required fix: Add a boxed note or footnote clarifying “this 1/√fsky scaling is not used anywhere in the SPHEREx 3D bispectrum forecast.”

P2-N4 (Sec. VI.C; p.13–14)
Problem: Some Bayes‑factor numbers are rounded inconsistently (e.g., “≈ 9.8 (≈ 10 in the abstract)” vs “≈ 9.2” after rebooking). Minor, but standardize significant figures.
Required fix: Use consistent rounding (e.g., one decimal place) across the text and tables.

P2-N5 (Sec. VII.D; p.18)
Problem: “Integral constraint” and “magnification bias” are listed qualitatively. A short numeric estimate (order‑of‑magnitude) would strengthen the point.
Required fix: Add 1–2 sentences with typical amplitudes or cite a figure/table from the literature with numbers.

P2-N6 (Sec. XI Acknowledgments; p.27)
Problem: “AI‑assisted software tooling (Anthropic Claude)….” PRD has no explicit policy against such acknowledgments, but this sentence is unnecessary for methods reproducibility.
Required fix: Remove or move to a footnote if the journal prefers.

NIT (cosmetic)

P2-T1 (Throughout)
Problem: Hyphenation artifacts (e.g., “con￾traction,” “computa￾tion”) appear in the text extraction but likely are PDF line breaks. If present in the manuscript source, please clean.
Required fix: Ensure final typeset version has clean hyphenation.

P2-T2 (Sec. V; p.11)
Problem: “MegaMap￾per” split across lines in several places.
Required fix: Nonbreaking hyphen or manual linebreak reflow.

P2-T3 (Table II; p.15)
Problem: Table layout mixes two different comparisons (vs tuned multifield; vs SSFSR) and footnotes a/b. Visual clarity could be improved.
Required fix: Split into two tables or add subheaders.

P2-T4 (Fig. 2; p.11)
Problem: Small font sizes on axis labels and legend; difficult to read in print.
Required fix: Increase font size by ~20–30%.

Arithmetic/dimensional audits spot‑checked

- Headline 5.2–5.5σ: Using |fNL| × r/σ = 4.375 × 0.84 / 0.70 = 5.25σ (low end) and with r = 0.876 → 5.48σ (rounds to 5.5σ). Consistent.
- “Conservative floor” with σGR = 1.0: σeff = √(0.7^2 + 1^2) = 1.2207; significance = 4.375 × 0.84 / 1.2207 = 3.10σ (text quotes ~3.0σ; acceptable rounding).
- “All combined (0.9, 1.0)”: σeff = √(0.9^2 + 1^2) = 1.345; significance = 4.375 × 0.84 / 1.345 = 2.73σ (reported ~2.7σ). OK.
- Planck PR4 recast: σ/ r = 5.0 / 0.876 = 5.71; distance to −4.375 is 4.275/5.71 = 0.75σ. OK.
- Bayes factor (delta, W = 30, σ = 0.7): B ≈ 30/(√(2π) 0.7) = 17.1; (delta, W = 10) with finite CDF tail: 5.70/0.814 = 7.0. OK.

Abstract-last drift sweep (pattern‑045): All abstract claims are represented in the body with appropriate caveats, except as noted in ESSENTIAL items: (a) the absence of the explicit Gaussian‑prior Bayes‑factor formula, (b) the missing DOI/commit hash, and (c) the unconditional phrasing of the “2.6–5σ realistic” range that actually assumes additive‑in‑quadrature systematics without covariance. Please align the abstract wording with the body by marking the 2.6–5σ as a “scenario envelope under additive‑quadrature systematics” unless a joint covariance check is added.

Provenance surfaces (patterns 046/047): Besides the missing DOI and SHA, several JSON/script artifact names are cited. Please ensure the archived release contains those exact filenames and an index that maps them to figures/tables. Add a short “Reproduction map” table in the Data Availability section.

Uncomputed quantitative claims (pattern‑048): The 10–20% anomaly‑tracer improvement (Sec. IV) lacks a computation and is explicitly labeled “preliminary”/“upper bound,” but it still reads as quantitative. Either provide the calculation or move it to a brief speculative sentence without numbers.

Standalone-reader test: The paper is largely self‑contained. However, the use of Heinrich et al. forecasts and Barreira’s bϕ discussion should be supplemented by 1–2 lines of equations that define how bϕ enters the bispectrum channel (you do this in words; a compact equation would improve clarity).

Paper length: At 28 pages for a sensitivity recast rather than a full independent Fisher forecast, this is long. Much of Sec. II’s null‑space/basis discussion and Sec. VII’s long caveat lists could be condensed or moved to appendices. A target length of ~18–20 pages would improve focus without loss of content.

## Summary recommendation
MAJOR REVISIONS

The manuscript presents a careful sensitivity recast with extensive internal cross‑checks and many correct arithmetic statements. However, acceptance in PRD requires fixing several methodological and reproducibility issues: provide a frozen code/data archive with DOI and commit SHA, supply the explicit Gaussian‑prior Bayes‑factor formula used for the tabulated values, justify or revise the κϵ range that feeds the ϵ‑correction, specify the exact Fisher weightings used to compute r (with a small numeric table), add a basis‑invariance robustness check for the null‑space scan, and qualify the “realistic 2.6–5σ” range unless a joint systematics covariance check is added. Addressing these items will materially improve reproducibility and methodological clarity.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E11 (Sec. II.A; pp.4–5; percentile-significance mismatch)
Problem: The text gives two different pre-systematic 16th–84th percentile detection ranges derived from the null-space r distribution. Using the stated percentiles r16 = 0.75 and r84 = 0.94 with σ = 0.70 gives 4.375 × 0.75 / 0.70 = 4.69σ and 4.375 × 0.94 / 0.70 = 5.88σ. The manuscript elsewhere states “4.4–6.2σ (median 5.3σ)” for the same percentile band. The 4.4σ and 6.2σ are inconsistent with the printed r percentiles and σ = 0.70.
Required fix: Harmonize these numbers. Either correct the 16th/84th r values or update the propagated σ-band (and show the arithmetic inline).

P2-E12 (Abstract p.1 vs. Table IV p.20; central r used in significance)
Problem: Abstract says “Only the noise-weighted r ≈ 0.83 enters the SPHEREx significance,” but Table IV and the main text use r = 0.84 as the central noise-weighted value for the headline 5.2–5.5σ. This is a small but concrete inconsistency.
Required fix: Pick a single central value (0.83 or 0.84) and use it consistently in the abstract, main text, and Table IV, or explicitly explain why the abstract cites 0.83 but calculations use 0.84.

P2-E13 (Fig. 6 caption p.21 and graphic; MegaMapper “σ = 1.5 conservative”)
Problem: The decision-threshold figure includes a “MegaMapper conservative (σ = 1.5)” bar, but no survey configuration, Fisher inputs, or calculation in the body motivates σ = 1.5 for MegaMapper. This value is used visually in a key decision graphic without a referenced derivation.
Required fix: Provide the configuration and calculation that lead to σ = 1.5 (area, n(z), bias, k-range, systematics assumed), or remove/replace this bar with a clearly labeled hypothetical marker not used in any conclusion.

P2-E14 (Fig. 2 p.11; figure–body mismatch for MegaMapper bars)
Problem: The caption lists MegaMapper bars “template-corrected ideal 7.4–7.7σ; the illustrative 3–7σ design-uncertainty envelope; conservative; and single-tracer.” The body never defines numeric values for the “conservative” and “single-tracer” MegaMapper cases plotted, nor the inputs behind those particular bars.
Required fix: Either (a) define the numbers and inputs for each MegaMapper bar in the body (or a table), or (b) remove those bars or relabel them as schematic with no quantitative interpretation.

P2-E15 (Sec. VI.C.c; pp.14–15; prior-width sensitivity arithmetic)
Problem: The text claims “widening [−15, +15] to [−20, +20] adds ΔBF ≲ 1.” For the delta-prior case B ∝ W/(√(2π)σeff), increasing W from 30 to 40 raises B by 33% (e.g., 17.1 → 22.8; ΔBF ≈ 5.7). Even for the Gaussian-bounce-prior case, the Bayes factor scaling with W is non-negligible; a change of +10 in W is not “≲ 1” in absolute BF. This appears arithmetically inconsistent with Eq. (10) and earlier tabulated values.
Required fix: Recompute and report the exact ΔBF for W = 30 → 40 in both the delta- and Gaussian-bounce-prior cases using the stated σeff, and correct or delete the “≲ 1” assertion.

MAJOR

P2-M11 (Sec. II.B and III.B; pp.5, 8–9; injection–recovery geometry inconsistency)
Problem: The injection–recovery test is described as “applies a KSW-type estimator … on tiled flat-sky patches covering the full sky,” yet elsewhere as using “full-sky geometry” with “no galactic mask.” These are mutually inconsistent descriptions (flat-sky tiling vs. full-sky estimator).
Required fix: Clarify the estimator geometry unambiguously (full-sky or flat-sky tiling), and provide the missing technical details (ℓ-range, patch size/overlap if tiled, beam/noise model, filtering, normalization). Report the run-to-run variance and SEM that underwrite the quoted ±0.01 on rmeas with N = 200.

P2-M12 (Sec. III.B; pp.8–9; conceptual inconsistency in r-weighting vs scale-free grid)
Problem: The manuscript states both that (i) the overlap r is computed on a scale-free triangle-ratio grid (so absolute k, cosmology, and redshift do not enter) and that (ii) “SPHEREx-like” and “LSS/SDB” Fisher weights were applied to derive r = 0.830 and r = 0.829. These survey weights generally depend on absolute k and redshift distributions, not solely on triangle shape ratios.
Required fix: Explain precisely how the SPHEREx/LSS weights were mapped onto a scale-free triangle-ratio grid (or, if a fixed-k slice approximation was used, state it and justify it). Without this, the reported “SPHEREx-like” r values are not reproducible.

P2-M13 (Sec. III.B; p.8; squeezed-cutoff insensitivity)
Problem: The text claims “varying x3,min from 0.001 to 0.200 changes r by < 0.0002,” even under LSS/SPHEREx-style weightings where squeezed triangles are emphasized. Such minimal sensitivity over two orders of magnitude in the cutoff is implausible without showing numbers per weighting.
Required fix: Provide a small table (per weighting scheme) showing r as a function of x3,min for several values in [0.001, 0.2], or qualify the statement to the specific weighting where it was observed (e.g., uniform-only) and remove it for others.

MINOR

P2-N7 (Sec. III.B; p.9; novelty claim on overlap quantification)
Problem: The statement “no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024)” is an unreferenced novelty claim.
Required fix: Either support with a brief literature canvass (citations), or tone down to “we are not aware of …”.

P2-N8 (Abstract p.1 vs. body; wording consistency on which r “enters”)
Problem: Abstract states only r ≈ 0.83 “enters the SPHEREx significance,” while the body consistently uses r = 0.84 as the central noise-weighted value. Even if both lie within the stated ±0.02 band, the phrasing invites confusion.
Required fix: Align wording (e.g., “r ≈ 0.84; results stable to ±0.02 across noise weightings”) or explicitly note that 0.83–0.84 are used interchangeably within the noise-weighted range.

P2-N9 (Throughout; significant figures)
Problem: Mixed precision is used for headline ranges (e.g., 5.2–5.5σ; 2.6–5σ) alongside very precise r values (0.829–0.876). This inconsistency can obscure how much is numerical vs. scenario variation.
Required fix: Standardize significant figures (e.g., one decimal place for σ ranges; two or three for r), and apply consistently.

P2-T5 (Throughout; style)
Problem: Inconsistent capitalization of terms like “bispectrum,” “Fisher,” etc., across captions and text.
Required fix: Harmonize capitalization per PRD style.

Explanation
This fresh-eyes pass focused on numerical consistency, figure–text alignment, dimensional checks, cross-references, and comparability of null procedures. The items above are new relative to the initial review. Most notably, I found (i) a concrete inconsistency in the percentile-propagated detection range, (ii) a prior-width sensitivity statement for Bayes factors that is at odds with the displayed formulas and earlier numbers, and (iii) two conceptual/clarity issues in the r-overlap estimation methodology (survey weightings applied on a scale-free grid; squeezed-cutoff insensitivity). Addressing these will materially improve rigor and reproducibility.