# P2 INT-X-P2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=8d67f8a1 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6509 chars)
**Wall time**: 322.8s

---

Referee report for Physical Review D (methods): “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope and framing
- This manuscript is a sensitivity recast, not an independent end‑to‑end forecast. The authors generally keep that framing explicit (title, abstract, Sec. IV), and most headline numbers are traced to Heinrich et al. (2024) and then adjusted for shape mismatch and a systematic budget treated additively in quadrature. That framing should be preserved consistently in every place where a “forecast” number appears.

Overall methodology
- The statistical pipeline is mostly transparent: the template overlap r is computed and vetted several ways; the main σ(fNL) is imported; degradations are combined in a stated (heuristic) way; Bayes factors are derived in closed form and validated by Monte Carlo. Many cross‑checks are included.
- The manuscript is long for the contribution (29 pages for a recast), with extensive digressions. Significant tightening without loss of content is feasible.

Findings and required actions
Below, each item includes: ID, location, issue, and required fix. Severity levels: ESSENTIAL (blocker), MAJOR (significant revision), MINOR (address but likely proceed), NIT (cosmetic).

ESSENTIAL

- P2-E1 (Data/code provenance; Data & Code Availability, pp. 24–25)
  Issue: The repository is referenced with “Zenodo (DOI inserted at submission)” and a GitHub path, with many artifact filenames (json/py) but no frozen release DOI or commit/tag. For PRD‑level reproducibility the current text is a placeholder.
  Required fix: Provide a public, immutable archive (Zenodo or equivalent) with a DOI, and a git commit hash/tag corresponding to the exact version used for all results. Include minimal run instructions to reproduce: (i) r = 0.84 ± 0.02 noise‑weighted value and weighting definitions, (ii) ℓ‑space Fisher overlap, (iii) the 10,000‑sample null‑space scan summary statistics (rcos distribution, r range), (iv) Bayes‑factor tables (Tables II–III), and (v) the SDB joint (fNL, nfNL) Fisher matrices and the quoted numbers (σ 1.53 → 3.08 → 7.06; ρ). Replace “DOI inserted at submission” with the actual DOI.

- P2-E2 (Abstract, p. 1; Sec. IV, pp. 9–11; Table IV, p. 20; consistency of “realistic 2.6–5σ” label)
  Issue: The 2.6–5σ “realistic” range is obtained by an additive‑in‑quadrature systematic budget that is explicitly heuristic (not a joint, marginalized bispectrum Fisher). Although you note this in the body text, the abstract sentence “reducing to a realistic ∼2.6–5σ after the systematic budget … these systematics are combined additively in quadrature” still risks being read as a forecasted measurement precision.
  Required fix: In the abstract and anywhere this 2.6–5σ is labeled “realistic,” add an explicit qualifier that it is a scoping sensitivity range under an additive‑quadrature heuristic, not a joint‑covariance forecast; state that a full bispectrum joint Fisher is not performed here. Add the same qualifier in the Conclusions where this range is restated.

MAJOR

- P2-M1 (Sec. VII.B, Fig. 5, p. 18; bϕ prior degradation quantification)
  Issue: The claimed σ(fNL) degradation vs bϕ prior width (20% → σ≈1.0 for MegaMapper SDB; 50% → σ≈2.2) and the SPHEREx bispectrum sensitivity to bϕ (20–50% leading to ≈0.9–1.0) are central to the systematic narrative but lack explicit quantitative inputs (k‑ranges, n(z), P(k), shot noise) or a clear pointer to a reproducible artifact beyond the figure. 
  Required fix: Provide a short quantitative description of the Fisher setup used to generate Fig. 5 (assumed number densities, bias models, k‑cuts, window, redshift bins, and which terms in the bispectrum estimator are responsible for the bϕ coupling). Archive the Fisher input files with the DOI in P2‑E1 and add a one‑line pointer to the exact artifact (filename) used to produce Fig. 5.

- P2-M2 (Sec. IV, p. 10–11; anomaly‑tracer “∼10–20% improvement”)
  Issue: The improvement claimed for autoencoder anomaly‑selected tracers is presented as an “upper bound,” but still quantitative and not backed by a documented Fisher/covariance calculation (and later you note shot‑noise caveats).
  Required fix: Either (a) move this to a brief speculative sentence without a number, or (b) provide the calculation details and archive the inputs/outputs with the DOI (shot‑noise model, number densities, biases, redshift distribution, and the exact Fisher result).

- P2-M3 (Sec. II.B/III.B, pp. 5–9; template‑overlap definitions)
  Issue: “SPHEREx‑like weighting” and the other Fisher weights are invoked, but “SPHEREx‑like” is not defined. The headline r = 0.84 ± 0.02 depends on the weighting definition set.
  Required fix: Define explicitly the weighting schemes used in Eq. (5): write w(k1,k2,k3) for the “SPHEREx‑like” case (or cite/point to a released configuration file with the DOI). As a minimal change, list concise formulas for all weights that underlie the reported r values and give the triangle‑shape domain and any k‑cuts used.

- P2-M4 (Sec. IV, p. 9–11; injection–recovery test)
  Issue: The flat‑sky, KSW‑type 2D estimator with isotropic Gaussian noise and no mask is very far from a 3D photometric‑redshift galaxy bispectrum estimator. You do say it is a Fisher‑space consistency check, not a full pipeline, but the numbers are quoted with tight errors (0.90 ± 0.01).
  Required fix: Add an explicit caveat next to the 0.90 ± 0.01 result stating that it is a 2D CMB‑style proxy not directly applicable to 3D LSS bispectrum estimators and that it is not used to derive any SPHEREx σ(fNL) figure.

- P2-M5 (Sec. VII.C, Table III, p. 19; BF vs. SSFSR and GR marginalization)
  Issue: The extremely large Bayes factors vs SSFSR rely on modeling SSFSR as a point hypothesis at fNL ≈ 0 and on the same σeff used for the bounce. This is fine in principle, but the table should specify explicitly the likelihood used for SSFSR in each row (delta vs. Gaussian), to avoid ambiguity.
  Required fix: Add one line to the Table III caption (or footnote) stating the exact SSFSR likelihood model (delta at fNL = 0 with the same σeff in the numerator/denominator ratio) used to produce the BF vs. SSFSR entries.

MINOR

- P2-m1 (Table IV, p. 20; ε‑correction “≲ 0.4σ”)
  Issue: You state the ε‑correction produces “0.6–8% in fNL” and then list “≲ 0.4σ effect.” Using 8% × 4.375 = 0.35 and σ = 0.70 gives 0.50σ, not 0.4σ. With r = 0.84 it is 0.42σ. The table entry is ambiguous.
  Required fix: Clarify whether the “σ‑equivalent” column is computed using σ = 0.70 and r = 1, or r = 0.84; give the consistent figure (0.50σ if using σ = 0.70 and r = 1; 0.42σ if using σ = 0.70 and r = 0.84). Adjust the table line accordingly.

- P2-m2 (Sec. II.A, p. 3; definition of BNL)
  Issue: The notation BNL is used as a configuration‑dependent “nonlinearity amplitude.” To minimize ambiguity with the standard bispectrum Bζ, add one clarifying sentence in Sec. II.A that BNL is a dimensionless, template‑normalized amplitude distinct from Bζ and equals fNL in the local template.
  Required fix: Add a clarifying sentence after Eq. (2), and ensure BNL is consistently distinguished from Bζ in later sections.

- P2-m3 (Sec. III.B, pp. 8–9; rcos projection‑noise discussion)
  Issue: You use rcos computed with unweighted inner products as a qualitative indicator of projection noise. That is acceptable, but the distinction vs. survey‑weighted overlap could be made clearer.
  Required fix: Add one sentence explicitly noting that rcos is an unweighted shape cosine and not a bound on estimator mismatch under the SPHEREx weighting.

- P2-m4 (Sec. VII.A, Fig. 4 caption, p. 17)
  Issue: The caption mixes SDB and bispectrum channels; the dotted “SPHEREx bispectrum” line is stated as σ = 0.7 and “less sensitive to ultra‑large scales,” which is fine, but the precise kmin range plotted for the SDB curves should be stated in the caption for clarity.
  Required fix: Add the kmin range and step used for the curves in Fig. 4 to the caption.

- P2-m5 (Sec. VI.C, pp. 12–15; Bayes‑factor bookkeeping)
  Issue: The abstract/headline BF ≈ 9–14 vs the r → 1 endpoint BF ≈ 10–17 is carefully explained in the body. To help readers, cross‑reference in the abstract where the rebooking is defined (Eq. (5)).
  Required fix: In the abstract, add “(using the σeff = σ/r rebooking from Eq. (5))” to the Bayes‑factor sentence.

- P2-m6 (Sec. II.A, p. 4; SVD conditioning: “far from any rank‑deficiency tolerance”)
  Issue: This is qualitative. Give the three singular values or the condition number to make the statement quantitative.
  Required fix: Report the three singular values (or their ratios) in a parenthetical.

- P2-m7 (Sec. VIII.A, p. 20; Planck PR4 recast central value)
  Issue: You write “fNL = −0.1 ± 5.7,” then parenthetically note that recasting the central value as well (−0.11) leaves the same 0.75σ. To avoid confusion, report the fully recast pair (−0.11 ± 5.7) in the main sentence.
  Required fix: Replace the sentence with the fully rescaled pair and keep the 0.75σ check as is.

- P2-m8 (Throughout; length and repetition)
  Issue: Several points are repeated verbosely (r bookkeeping, Cai vs Li factor‑two) and can be shortened.
  Required fix: Remove repeated explanations where already given (e.g., once in abstract and once in Appendix A), and aim to reduce main text length by 20–30% (≤ 18–20 pages excluding references and appendix) while retaining all load‑bearing derivations and numbers.

NIT

- P2-n1 (Typographic consistency; pp. 1–29)
  Issue: Mixed hyphenation (“post‑systematic‑budget,” “post systematic budget”). 
  Required fix: Standardize hyphenation throughout.

- P2-n2 (Acronyms)
  Issue: Define “UMF” on first use in Sec. VII.B (you do in prose, but an explicit parenthetical “UMF” would help).
  Required fix: Add acronym definition at first mention.

Arithmetic consistency checks (spot‑verifications)
- 4.375/0.7 = 6.25 (naive S/N): correct.
- Template‑corrected S/N with r = 0.829–0.876: 4.375×0.829/0.7 = 5.18; 4.375×0.876/0.7 = 5.47: matches “5.2–5.5σ.”
- GR degradation σeff = sqrt(0.7^2 + 1.0^2) = 1.221; S/N = 4.375×0.84/1.221 = 3.01: matches “∼3.0σ.”
- bϕ widening to 0.9: S/N = 4.375×0.84/0.9 = 4.08: matches “∼4.1σ.”
- All‑combined σeff = sqrt(0.9^2 + 1.0^2) = 1.345; S/N = 4.375×0.84/1.345 = 2.73: matches “∼2.7σ.”
- Bayes factor delta, W = 30, σ = 0.7: 30/(√(2π)×0.7) = 17.10: matches.
- Narrow competitor delta, W = 10, σ = 0.7: exact 7.01 (as computed from Eq. 9): matches.
- Planck PR4 recast: 5.0/0.876 = 5.71; |−4.375 − (−0.11)|/5.71 ≈ 0.75σ: matches.

Dimensional analysis spot‑checks
- Eqs. (3)–(4): Δb dimensionless; M(k,z) dimensionless with k^2/H0^2 factor; consistent.
- Eq. (1)–(2): BNL dimensionless after division by Σk_i^3; consistent.

Abstract–body coherence (abstract‑last sweep)
- Two headline σ ranges (5.2–5.5σ optimistic; 2.6–5σ after systematics) are supported in Sec. IV and Table IV; ensure the “realistic” qualifier is caveated as per P2‑E2.
- Bayes‑factor ranges map to Table II and Sec. VI; abstract mentions r rebooking and prior sensitivity; good.
- Template mismatch r = 0.83–0.88 appears several times and is backed by Sec. III.B; good.
- Statement that this is a sensitivity recast (not independent forecast) is consistent with Sec. IV; good.

Bibliography spot‑checks
- Heinrich et al. 2024 citation and σ(flocalNL) ≈ 0.7: consistent.
- Planck PR4 fNL = −0.1 ± 5.0 (Jung et al. 2025): plausible; please ensure citation details (A&A 702, A204) match the final journal entry at proof time.
- Dalal et al. (2008) SDB formula: correct references.

Recommended page length
- The paper can be reduced to ~18–20 pages by consolidating repeated explanations and moving some extended narrative to an appendix, without sacrificing methodological rigor.

Summary recommendation
MAJOR REVISIONS

Justification
The core numerical claims are mostly consistent and carefully caveated, and the recast framing is clear. However, PRD‑level reproducibility requires a fixed DOI/commit and explicit inputs to reproduce all load‑bearing numbers. A few central quantitative statements (bϕ prior degradation, “realistic” 2.6–5σ label) need clearer qualification and/or minimal additional methodological detail. Addressing the essential provenance item and the listed major fixes will bring the manuscript to PRD methodological standards. The rest are minor editorial/numerical clarifications.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL
- None newly identified beyond P2-E1 and P2-E2. The most critical reproducibility and framing issues were already captured there.

MAJOR

- P2-M6 (Sec. III.A, Eqs. (3)–(4); units/normalization of M(k,z))
  Issue: You assert M(k,z) is dimensionless while also stating k is in h Mpc−1 and using H0^2. In common LSS usage α(k,z) = 2k^2T(k)D(z)/(3ΩmH0^2) is dimensionless only if k and H0 are carried in consistent units (often k/H0 with c=1), or if an explicit c factor is included. Because you later use this M in the joint SDB Fisher (σ(fNL)=1.53→3.08→7.06), the precise unit convention matters.
  Required fix: State explicitly the unit convention used in all code (e.g., k and H0 both in h Mpc−1 via H0 = 100h km s−1 Mpc−1 and c = 1 with the usual conversion, or adopt α(k,z) as in Dalal et al. with k in physical 1/Mpc). Quote the exact α/M formula implemented in the released Fisher code, including any factors of c or 100h, and ensure dimensional consistency. Archive a minimal test (JSON or notebook) showing that Δb(k) is dimensionless for representative k, z.

- P2-M7 (Sec. VII.D, photo‑z outliers; arithmetic and sourcing)
  Issue: The “first‑order Fisher correction” says 10% catastrophic outliers yield only ~5% σ(fNL) degradation, with a heuristic term fcat^2/(1+fcat)^2 ≈ 0.008 quoted inside the paragraph. That term by itself corresponds to <1% dilution, not 5%. The final 5% figure is not reconciled quantitatively with the displayed 0.008 estimate nor tied to a cited Fisher calculation.
  Required fix: Reconcile the arithmetic. Either show the explicit Fisher calculation that produces ~5% at fcat=0.1 (and archive it with the DOI), or revise the text to a number that follows from the stated formula and/or clearly attribute the 5% to an independent citation with matching survey setup.

- P2-M8 (Table III vs. text around continuous GR marginalization; BF vs. SSFSR spread)
  Issue: The table lists enormous Bayes factors vs SSFSR (e.g., 3.5×10^8 ideal), while the text a few paragraphs later states a continuous σGR ∼ U[0,1] marginalization gives BF ≈ 8.6×10^3. This is a 4–5 order‑of‑magnitude change that could be read as an inconsistency if the reader overlooks the different σGR treatment.
  Required fix: Add an explicit warning in the Table III caption that the BF vs. SSFSR entries are exponentially σ‑sensitive point‑σ results (σeff fixed per row), and that continuous σGR marginalization reduces them dramatically (quote the 8.6×10^3 value and the reference to the code artifact). Consider moving the BF‑vs‑SSFSR numbers to an appendix or adding a footnote box to avoid overinterpretation.

- P2-M9 (Sec. III.B, Eq. (5) and surrounding text; scale in “1/k^2” weighting for r)
  Issue: You report r under “scale‑dependent‑bias weighting w ∝ 1/k^2,” yet elsewhere emphasize the overlap is evaluated on a scale‑free triangle‑ratio grid. A 1/k^2 weight requires an absolute k‑range and measure; otherwise r is not uniquely defined. The later “x3,min sweep changes r by < 0.0002” also presumes a particular scale treatment.
  Required fix: Specify the absolute k‑range, measure, and any Jacobian used for the 1/k^2 weight in the r computation (or explain how the weighting reduces to a pure shape weight independent of scale). Archive the exact configuration file (with DOI) used for the “SDB 1/k^2” and “SPHEREx‑like” cases. This is separate from P2‑M3’s request for the analytic form of w(k1,k2,k3).

MINOR

- P2-m9 (Sec. II.D, p. 7; amplitude‑scatter percentage)
  Issue: You characterize the null‑space amplitude scatter as “∼ 13%.” With r = 0.85 ± 0.13, the relative 1σ scatter is 0.13/0.85 ≈ 15%. 
  Required fix: Update “∼ 13%” to “∼ 15%” (or report the precise percentage used elsewhere if different).

- P2-m10 (Sec. IV, x3,min sensitivity claim; significant figures)
  Issue: “Varying x3,min from 0.001 to 0.200 changes r by < 0.0002.” Given Monte‑Carlo and numerical quadrature noise elsewhere at the 0.01 level, this degree of precision is surprising without a reproducibility artifact.
  Required fix: Either (a) relax to a more defensible precision (e.g., “< 0.001”), or (b) cite and archive an artifact that tabulates r vs. x3,min to 1e−4 precision, including numerical‑error control parameters.

- P2-m11 (Eq. (12) numerics; explicit mapping check)
  Issue: The mapping fNL(ns) ≈ −35/8 − c′(ns−1) with c′ ∈ [0.7,10] yields a shift of +0.025 to +0.351 at ns = 0.9649, hence fNL ∈ [−4.350, −4.024]. You quote [−4.35, −4.02]. This is fine, but consider adding the actual c′ bounds in the sentence for quick verification.
  Required fix: Add “c′ ∈ [0.7,10] implies ΔfNL ≈ +0.025…+0.351 at ns = 0.9649” inline or in a short footnote.

- P2-m12 (Appendix A, mapping between Φ and ζ conventions; dimensional clarity)
  Issue: The derivation rightly shows Bζ = (6/5) fNL PζPζ [+perms], but it would help reproducibility to add a one‑line reminder that PΦ = (3/5)^2 Pζ in the matter era and that all power spectra are comoving, with units handled consistently in the conversion.
  Required fix: Add that one‑line unit note in Appendix A.

- P2-m13 (Sec. VII.C; “∼ 23% inflation” wording)
  Issue: For σeff = sqrt(0.7^2 + 0.5^2) = 0.860, the inflation factor is 0.860/0.700 = 1.2286 (22.9%). Good numerically, but the basis for choosing σGR = 0.5 as “central” remains qualitative here.
  Required fix: Add a parenthetical pointer to the precise Addis et al. survey/regime motivating σGR = 0.5 (e.g., redshift and tracer), or label it explicitly as a stress‑test anchor without direct Fisher calibration.

NIT

- P2-n3 (Notation consistency)
  Issue: “nfNL,” “n fNL,” and “(fNL, nfNL)” all appear. 
  Required fix: Standardize to “nfNL” throughout (main text, captions, tables).

- P2-n4 (Fig. 2 caption; axis labels)
  Issue: The bar plot shows “Significance,” but the y‑axis units/scale (σ) are only implied in the caption text.
  Required fix: Explicitly add “(σ)” to the y‑axis label in the figure or state it in the caption.

Explanation
The fresh‑eyes pass focused on items commonly missed on first review: unit/normalization rigor for M(k,z) used in SDB, a small but real arithmetic inconsistency in the photo‑z degradation paragraph, the potential ambiguity introduced by scale‑weighted r without a k‑range, and the stark BF‑vs‑SSFSR spread between fixed‑σ rows and continuous σGR marginalization. Other smaller clarity/precision items are flagged as minor or nit fixes. All previously raised issues are not repeated here.