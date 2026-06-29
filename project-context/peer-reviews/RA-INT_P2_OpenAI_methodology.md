# P2 RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=8dabb71b pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7830 chars)
**Wall time**: 410.9s

---

Referee report (PRD methodology)

Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Length: 29 pages, 5 figures, 5 tables, appendix

Overall scope: This is presented as a sensitivity recast of a published SPHEREx multi-tracer bispectrum forecast to the matter-bounce signal fNL = −35/8, plus ancillary checks (template overlap r, injection/recovery, Bayes factors, partial SDB Fisher with running). The authors repeatedly state it is not an independent forecast and combine systematics additively in quadrature.

I have read the full manuscript carefully and recomputed all explicit numerics. Most arithmetic checks out, and the abstract conforms in wording to the body’s “sensitivity recast” framing. However, at PRD methodological standards, a number of items require correction or strengthening before publication. I list findings below.

Findings

ESSENTIAL

P2-E1 (Abstract; Sec. IV, pp. 1, 9–12, 20): Over-interpretation of “detection significance” without a joint covariance treatment
- Problem: The abstract and body repeatedly present 5.2–5.5σ “bispectrum-only” and 2.6–5.5σ “realistic” “detection significance” figures derived from an imported σ(fNL)=0.7 and a heuristic additive-in-quadrature systematic budget (GR, bϕ, photo-z, etc.). No joint bispectrum Fisher/marginalized covariance over the dominant nuisances (e.g., bϕ per tracer, GR projection amplitude) is provided. The single joint Fisher that is computed is for the SDB power spectrum, not the bispectrum that underpins the headline σ’s.
- Required fix: Either (a) provide a bispectrum-level joint Fisher (or equivalent likelihood) that marginalizes over the dominant nuisances you include in your budget, and update all σ/“significance” values accordingly; or (b) rephrase all occurrences of “detection significance” in the abstract and throughout (including Fig. 2 caption and Table IV header) to “sensitivity estimate” and remove any implication of a forecasted measurement precision. In the abstract’s opening sentences, explicitly state “sensitivity recast, not a forecast,” and remove the 5σ phrasing unless supported by a joint covariance. Make this caveat equally prominent at every juxtaposition with numerical σ values.

P2-E2 (Data and Code Availability, p. 25): Missing frozen release/DOI; non-reproducible pointer
- Problem: The text says “archived at Zenodo (DOI inserted at submission)”. This is a placeholder. PRD requires a fixed, citable software/data artifact to reproduce all numerical results.
- Required fix: Provide a working Zenodo DOI (or equivalent) corresponding to an immutable release of the exact code and inputs used to produce all numbers and figures in the paper, and list the exact git commit hash(es). Ensure the repository contains scripts/notebooks to regenerate the key scalars (r values under each weighting, the Bayes-factor tables, the SVD/null-space scan outputs, and Fig./Table products). Replace all “inserted at submission” placeholders.

P2-E3 (Sec. III.B, II, Figs. 1–2, pp. 8–11, 5): Insufficient specification of the weighting kernels and integration domains that produce r = 0.84 ± 0.02
- Problem: The central, load-bearing number r = 0.84 ± 0.02 is ascribed to “SPHEREx-like,” “SDB 1/k^2,” “CMB Fisher k^2,” and “flat/uniform” weightings, plus masked variants. However, the exact weight definitions and domains that produce r = 0.830, 0.829, 0.876, 0.835 are not given in a form a reader can reproduce (e.g., the precise k-ratio tiling, triangle-shape sampling, and survey noise kernels used for the LSS weighting).
- Required fix: Add a table listing, for each weighting scheme used, the explicit weighting function w(k1,k2,k3), the triangle-shape domain and sampling (e.g., bounds on x2 ≡ k2/k1, x3 ≡ k3/k1, binning, masking rules), and the resulting r. Provide the numerical values that underpin the stated range r ∈ [0.829, 0.876]. This is necessary for reproducibility and to justify the ±0.02 spread.

P2-E4 (Appendix A and Sec. II.C, pp. 25–27, 6–8): Incomplete documentation of the Cai–Li factor-of-two reconciliation
- Problem: The conclusion that Li et al.’s −35/16 is the single-time-ordering intermediate and Cai et al.’s −35/8 is the full in-in result is plausible. Appendix A.1 gives the general −2 Im identity, but the manuscript also claims “all four individual vertex contributions … agree … at the level of the ∑k_i^3 coefficients (checked numerically to six significant figures)” and that orbit-dependent Wick-permutation factors lead to a full doubling. No explicit numerical ledger of these terms is shown.
- Required fix: Add a compact table (or a supplemental file referenced in the main text) that, for each of the four Maldacena vertices, lists the numeric coefficients of the three benchmark configurations from both papers and demonstrates equality after consistent normalization, and shows explicitly the factor-of-two doubling from single-ordering to full commutator. This should include the orbit-by-orbit permutation-count ratios used to map between bases. Without this, the central normalization audit remains claim-based rather than documented.

P2-E5 (Data and Code Availability/throughout, pp. 25; multiple pages): Internal artifact names in main text; lack of self-contained specification
- Problem: The body text references repository file names (e.g., “c9i epsilon ratio check.json,” “phase3 bispectrum shape overlap.json,” “appendix A1 wick doubling.py”) as evidence for results, without presenting their essential contents in the paper or SI. This violates the standalone-reader test.
- Required fix: Move all references to internal file names to a single Data and Code section or footnotes. For each load-bearing result that currently points to a file, include in-paper tables/figures summarizing the numeric outcomes (e.g., the SVD singular values and the constraint matrix; the distribution of r across the 10,000 null-space samples; the per-weighting r values; the ℓ-space Fisher overlap numbers). Keep the repository as replication support, but make the manuscript self-contained.

MAJOR

P2-M1 (Sec. II, III.B, p. 5 and 9–10): Injection–recovery using an inappropriate estimator for the target observable
- Problem: The rmeasured = 0.90 ± 0.01 “injection/recovery” is obtained with a 2D CMB KSW-type estimator on tiled flat-sky patches and isotropic Gaussian noise, not with a 3D galaxy-bispectrum estimator with survey window and photo-z scatter appropriate for SPHEREx. The test’s geometry and noise are mismatched to the headline observable.
- Required fix: Either provide a 3D galaxy-bispectrum injection–recovery using a SPHEREx-like selection, window, and photo-z model, or remove this line of evidence. If retained only as a qualitative cross-check, strip the ±0.01 quantitative precision and relegate it to a brief consistency note.

P2-M2 (Sec. IV, p. 11): “Anomaly-detected tracers” improvement (10–20%) presented without a quantitative, shot-noise–aware Fisher
- Problem: The claimed 10–20% σ(fNL) improvement from anomaly-selected tracers is not backed by a Fisher calculation that includes their number densities, biases, and shot noise, and the text admits it is an “upper bound.”
- Required fix: Remove the 10–20% number from the main narrative (keep as a brief hypothesis if desired), or provide a proper multi-tracer Fisher with representative n(z), b(z), and shot noise showing the gain. At minimum, move this to a short “future work” remark.

P2-M3 (Sec. VII.C, Table III, pp. 18–19): Ad hoc mapping from relativistic-projection results to σGR = 0.5–1.0
- Problem: The σGR values used in additive quadrature are chosen as a “stress-test amplitude grid” referencing Addis et al., but no quantitative translation is given from the Addis biases (e.g., best-fit fNL shifts) to σGR. The resulting Bayes-factor table and “realistic” σ ranges depend sensitively on σGR.
- Required fix: Provide a quantitative mapping (or bracketing argument) from published relativistic-projection bias amplitudes into an equivalent σGR for SPHEREx-like samples, or clearly decouple the σGR table from any “realistic” phrasing and call it a pure stress test. If you keep σGR = 0.5–1.0 as realistic, justify it numerically.

P2-M4 (Sec. IX.D, pp. 22–23): Joint SDB Fisher results lack in-paper numerical specification
- Problem: The joint (fNL, nfNL) Fisher is a new computation. The paper quotes σunmarg(fNL)=1.53, σmarg(fNL)=3.08/7.06 (fixed-bias/bias-marginalized), σ(nfNL)=0.295/0.596 and ρ values, but does not present the actual Fisher inputs (redshift bins, volumes, tracer densities, bias priors), the kernel used, or a table summarizing the main numbers and the per-bin set-up.
- Required fix: Add a compact table with the redshift bins, sky fraction, assumed n(z), b1(z), survey window, and the resulting Fisher elements or at least the marginalized covariance matrix over (fNL, nfNL). This must be sufficient for another group to reproduce your SDB Fisher without relying on your code.

P2-M5 (Sec. II.A–B, pp. 3–6): 3×6 SVD constraint matrix described but not shown
- Problem: The underdetermination/singular-value discussion is central to the null-space scan. The paper does not print the 3×6 constraint matrix (the rows evaluated at the three benchmark configurations) nor the singular values.
- Required fix: Add the explicit 3×6 matrix and the three singular values (with the stated normalization), and show one concrete coefficient vector that solves the system. This will make the null-space discussion auditable.

P2-M6 (Table II; Sec. VI, pp. 14–16): Bayes-factor methodology presented partly in prose; missing explicit formula for Gaussian bounce prior case
- Problem: For the Gaussian bounce prior, you say the likelihood is “replaced by the prior-convolved marginal” but give no explicit formula. Readers should not have to infer this.
- Required fix: Add the explicit Gaussian–Gaussian convolution result for the numerator (i.e., Lmarg(ˆfNL) = N(ˆfNL; μbounce, σeff^2 + σtheory^2)) and update Eq. (9) accordingly when used for the Gaussian prior rows. This will remove any ambiguity.

P2-M7 (Throughout): Excessive use of internal-repo file names in the main text
- Problem: File names like “c9g bf table recompute.py,” “phase3 fisher overlap.json,” etc., appear throughout the narrative.
- Required fix: Consolidate these references into the Data/Code section or footnotes and remove them from the scientific narrative.

MINOR

P2-m1 (Abstract, p. 1): Ratio |f_bounce|/|f_inf| quoted as ≈ 290
- Check: 4.375/0.015 = 291.67. Consider “≈ 292” or “≈ 290–292.” Not critical, but tighten rounding or give one extra significant figure.

P2-m2 (Sec. IV; Fig. 2 caption, p. 11): Juxtaposition of naive 6.25σ and template-corrected values
- Comment: You do mark the naive bar as “shown only for reference, not used in any headline,” which satisfies the “not directly comparable” requirement. Keep this explicit note anywhere the naive 6.25σ is shown alongside corrected σ’s.

P2-m3 (Sec. III.B, p. 9): “The corresponding σ(fNL) degradation factors are 1.14×, 1.20×, 1.21×.”
- Check: 1/0.876=1.142; 1/0.830=1.205; 1/0.829=1.206. Numbers are correct. Please add which weighting corresponds to each factor in-line for clarity.

P2-m4 (Sec. II.D, p. 7): rt notation clarification
- Comment: You note the potential confusion with r (overlap) and adopt rt for tensor-to-scalar ratio. Good. Ensure rt is used consistently; spot-checks look fine.

P2-m5 (Sec. VIII.A, p. 20): Planck PR4 recast arithmetic
- Check: σrec = 5.0/0.876 = 5.71; |−4.375 − (−0.11)|/5.71 = 0.747 (~0.75σ). |−0.11|/5.71 = 0.019. Correct. Consider adding the recast central value explicitly in text for completeness.

P2-m6 (Appendix A.1, p. 26): “Hermiticity on the vacuum” phrasing
- Suggestion: Replace with “for Hermitian Hint, ⟨Hint ζ^3⟩ = ⟨ζ^3 Hint⟩*” to avoid ambiguity.

P2-m7 (Paper length): 29 pages for a sensitivity recast
- Recommendation: The paper is long relative to the incremental methodological content. Consider reducing length to ≈18–20 pages by moving verbose Bayes-factor prose, code-artifact listings, and repeated disclaimers to a succinct Methods/Appendix, and by consolidating the many repeated “bookkeeping” paragraphs.

NIT

P2-N1 (Throughout): Repetitive wording
- Problem: “bookkeeping,” “endpoint,” “headline” are used very frequently, which hampers readability.
- Fix: Edit for concision.

P2-N2 (Acknowledgments, p. 27): “AI-assisted software tooling (Anthropic Claude)”
- Comment: Not required for PRD; consider removing.

P2-N3 (Introduction/elsewhere, multiple pages): Operational timelines (“launched March 2025”)
- Comment: PRD papers need not include mission timeline statements; consider removing.

P2-N4 (Typesetting artifacts): Occasional odd Unicode characters (e.g., ∑︁)
- Fix: Ensure standard TeX output with PRD class to avoid rendering artifacts.

P2-N5 (Typos): Occasional “rebooking” where “recasting” or “rescaling” might read more clearly.
- Fix: Light copyedit.

Checks passed (selected)

- Arithmetic checks: 6.25 = 4.375/0.7; template-corrected 5.19–5.48σ for r∈[0.829,0.876]; GR 1.0 addition gives σeff=1.221 and 3.01σ; bϕ widening to 0.9 yields ~4.08σ; combined bϕ 0.9 + GR 1.0 gives 2.73σ; all consistent with Table IV.
- Fractional variation between folded and squeezed values: (|−2.25 − (−4.375)|)/4.375 = 0.486 (~49%) as claimed.
- SDB identity for σmarg using ρ: numbers reproduce (3.08 and 7.06) from quoted ρ’s.
- SY inequality estimate τNL≈27.6 for |fNL|=4.375 is correct.

Abstract-last drift sweep

- The abstract largely mirrors the body’s caveats (“sensitivity recast,” “additively in quadrature,” “not a joint-covariance forecast”), which is good. However, see P2-E1: the presentation still reads as a “headline forecast.” Please implement the rephrasing requested above, and make the “sensitivity recast” qualifier appear before any σ numbers.

Provenance surfaces

- Missing fixed DOI (P2-E2). Also, ensure that all scripts mentioned actually reproduce the paper’s numbers from a clean checkout. Provide a minimal “make all figures & tables” script.

Uncomputed quantitative claims

- A few qualitative statements (“squeezed-cutoff change < 2×10^−4,” “rcos > 0.95 across radii”; “σ degradation from photo-z catastrophic outliers ~5%”) are given without in-paper numeric support beyond brief notes. Since these are not load-bearing to the main headline, they can remain, but adding one small table with these numbers would strengthen the paper.

Standalone-reader test

- The manuscript depends only on Heinrich et al. (for σ(fNL)=0.7) and provides formulae for recasting. After implementing P2-E3/E5/M4, it should be fully self-contained.

Effect sizes

- For every σ headline, you already provide an effect-size interpretation as |fNL| r / σeff; this is adequate.

## Summary recommendation
MAJOR REVISIONS

The core arithmetic and many caveats are carefully handled, but PRD methodological standards require stronger reproducibility and clearer statistical framing. The most important fixes are: (i) either provide a bispectrum-level joint covariance over the key nuisances or consistently downgrade all “detection significance” phrasing to “sensitivity estimate” in the abstract and body; (ii) supply a fixed DOI/commit for the replication code; (iii) document the weighting kernels and domains that yield r = 0.84 ± 0.02 in a reproducible table; and (iv) provide a compact, in-paper ledger for the Cai–Li normalization resolution and the SDB Fisher inputs/results. These changes are substantive but feasible and will bring the paper up to PRD rigor for a sensitivity-recast methods contribution.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E6 (Sec. II vs. Sec. III.B; notation/consistency, pp. 3–4 and 8–9): Inconsistent squeezed-limit labeling and triangle ordering
- Issue: In Sec. II the squeezed limit is defined with k1 the long mode and k2 ≈ k3 ≡ k the hard modes (k1/k → 0). Later, Sec. III.B defines x3 ≡ k3/k1 as the “squeezed-limit ratio” with x3 → 0 corresponding to k3 ≪ k1. This contradicts the earlier convention and also the stated grid ordering k1 ≤ k2 ≤ k3 used for the triangle sampling (under which x3 ≥ 1 always).
- Required fix: Choose one consistent convention across the paper. If k1 is the long mode, use x1 ≡ k1/k3 (or k1/k2) for the squeezed ratio; if you insist on x3, then re-order the triangle labeling accordingly (smallest index = long mode). Update all references (including the x3,min sweep text) to avoid logical contradictions.

P2-E7 (Fig. 4 axis units vs. body text; p. 17): Unit label inconsistency for wavenumber
- Issue: The x-axis label reads kmin [h/Mpc]. The body consistently states k is in h Mpc−1.
- Required fix: Change the axis label to h Mpc−1 and check all other figures for the same unit formatting.

P2-E8 (Fig. 5 caption vs. plotted content; p. 18): Caption mixes SPHEREx bispectrum statements into a panel that only shows MegaMapper SDB curves
- Issue: The right-hand panel plots “Detection of fNL = −35/8 vs. bϕ prior uncertainty” for MegaMapper SDB; the caption then states “The bispectrum channel remains at ∼5σ (optimistic) or ∼3–4σ (after GR degradation).” Those bispectrum statements are not represented in the plotted curves and can be misread as shown.
- Required fix: Clarify in the caption that only the MegaMapper SDB curve is plotted; the SPHEREx bispectrum numbers are textual context, not plotted. Alternatively, add a SPHEREx bispectrum curve (if any dependence on bϕ is being illustrated) or move those sentences to the main text.

P2-E9 (Table III and text around Sec. VII.C; BF vs. SSFSR methodology; pp. 18–19): Bayes factor against SSFSR lacks explicit prior/evidence specification
- Issue: The large Bayes factors vs. SSFSR (e.g., 3.5×10^8) implicitly treat SSFSR as a point (delta) hypothesis with no Occam penalty, but the exact likelihood ratio used and prior volume for SSFSR are not specified. Without an explicit evidence definition, these magnitudes are not auditable.
- Required fix: State explicitly that SSFSR is treated as a point hypothesis and provide the exact likelihood ratio used (e.g., L(fobs|fNL = −35/8)/L(fobs|fNL = 0)) or otherwise define the SSFSR prior and evidence integral. If kept as a point-hypothesis likelihood ratio, say so unambiguously and caution that these values are not Bayes factors in the strict prior-volume sense.

MAJOR

P2-M8 (Sec. III.B; ℓ-space Fisher overlap; p. 9): Missing specification of the ℓ-space Fisher setup
- Issue: You report r = 0.878 ± 0.012 “ℓ-space Fisher” overlap, “stable across ℓref = 50–950,” but do not specify the ℓ-range, beams, noise levels, masks, or exact weighting used. The quoted ±0.012 precision is not reproducible.
- Required fix: Provide the exact ℓ-range(s), beam FWHM(s), noise spectra, frequency combination, sky fraction/mask treatment, and the inner-product definition used, or remove the ±0.012 quantitative precision and keep this as a qualitative sanity check.

P2-M9 (Sec. VII.D; photo-z outlier impact; p. 18): Unjustified 5% degradation claim
- Issue: The statement that a 10% catastrophic photo-z fraction degrades σ(fNL) by ∼5% in the bispectrum channel is attributed to a “first-order Fisher correction” with a back-of-envelope factor fcat^2/(1 + fcat)^2 ≈ 0.008, but no derivation, weighting, or survey window treatment is provided.
- Required fix: Provide the short derivation and assumptions (what observable, which kernel, which redshift-bin couplings) or recast this as a qualitative expectation and remove the 5% numerical claim.

P2-M10 (Sec. III.B; “CMB Fisher k^2 weighting”; p. 8–9): Ad hoc choice of weight
- Issue: The “CMB Fisher” weight w ∝ k^2 is introduced as a surrogate for CMB weighting, but no derivation from the standard CMB bispectrum Fisher (which lives in ℓ-space and includes beam/noise terms) is provided.
- Required fix: Either (i) justify w ∝ k^2 from a mapped ℓ → k correspondence with the assumed CMB Fisher kernel, or (ii) rename it to “signal-weighted (k^2)” to avoid conflating it with an actual CMB Fisher weighting.

P2-M11 (Sec. II.A/Table I; benchmark choice; pp. 5–6): Folded benchmark sits on a degenerate boundary
- Issue: The folded benchmark is evaluated “as the limit k1 = 2k, k2 = k3 = k,” i.e., on the degenerate boundary k1 = k2 + k3. Using a boundary configuration as one of only three constraints can distort the SVD conditioning and the inferred null-space.
- Required fix: Show that moving slightly off the boundary (e.g., k1 = 1.99 k, k2 = k3 = k) does not materially change the 3×6 constraint matrix/SVD or the r distribution. If it does, switch to a non-degenerate near-folded configuration.

P2-M12 (Sec. V; “per-bin baseline” wording; Fig. 5 caption; p. 18): Mischaracterization of σ(fNL) = 0.7 as “per-bin”
- Issue: The caption says “the SPHEREx multi-tracer bispectrum per-bin baseline is σ(fNL) = 0.7.” That 0.7 value is a combined forecast, not a per-bin uncertainty.
- Required fix: Correct the wording to “combined bispectrum baseline” (or similar) to avoid implying per-bin precision.

P2-M13 (Appendix A.1; symmetry-factor placement; pp. 26–27): Ambiguity in 1/Sv factor
- Issue: Eq. (A7) contains a factor 1/Sv but the text says “Sv is the symmetry factor accounting for identical fields within vertex v (Sζẋζ^2 = 2…)”. It is unclear whether you divide or multiply by Sv in your implementation.
- Required fix: State clearly the symmetry-factor convention (divide by Sv to avoid double-counting or multiply to include duplicates) and ensure consistency with the Wick-permutation counting described earlier. Since the factor-of-two audit hangs on permutation accounting, this should be unambiguous.

MINOR

P2-m7 (Sec. III.B; x3,min sweep; p. 9): Provide numeric support for the “< 2×10−4” sensitivity claim
- Suggestion: Add a 1–2 line table with r values across the stated x3,min sweep (0.001–0.2) to substantiate the “< 0.0002” change claim.

P2-m8 (Sec. II; estimator description; p. 5): KSW called “optimal linear estimator”
- Issue: The KSW fNL estimator is cubic in filtered maps (though linear in the amplitude parameter).
- Fix: Rephrase to “optimal (cubic) KSW-type estimator for the bispectrum amplitude.”

P2-m9 (Fig. 1 vs. text; pp. 5–6): Label BNL explicitly as dimensionless on the y-axis
- Suggestion: The caption says “dimensionless,” but the axis label in the embed is just BNL(k1,k,k). Label as “BNL (dimensionless)” for clarity.

NITS

P2-N6 (Units and constants; Eq. 4; p. 7): Clarify normalizations
- Suggestion: You note k in h Mpc−1 and D(z) normalized to D(0) = 1; add a brief parenthetical that H0 includes h and M(k,z) is dimensionless under these conventions.

Rationale for “fresh-eyes” conclusion
- The notational inconsistency around the squeezed-limit ratio and triangle ordering (P2-E6) is new and potentially consequential for reproducibility and for readers attempting to follow the weighting and cutoff tests.
- Several caption/content mismatches (P2-E7/E8) and phrasing issues (P2-M12) can mislead readers about what is plotted or what a number represents.
- The SSFSR Bayes-factor presentation (P2-E9) needs explicit methodology; large numbers are otherwise not interpretable.
- Technical clarifications around ℓ-space weighting (P2-M8/M10), the folded benchmark (P2-M11), photo-z impact (P2-M9), and symmetry factors (P2-M13) are required for PRD-level rigor.

These items are in addition to, and do not duplicate, the issues in my initial review.