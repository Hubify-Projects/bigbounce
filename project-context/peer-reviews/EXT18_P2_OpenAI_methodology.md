# P2 EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5a8a1af4 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7497 chars)
**Wall time**: 625.2s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
I reviewed the full manuscript (29 pages), all equations, figures, tables, and the abstract. I checked dimensional consistency, recomputed quoted ratios/significances where possible from values in the text/tables, and audited the statistical methodology and internal bookkeeping against the stated goals. Below are all findings, classified by severity with precise page/section references, the specific issue, and the required fix.

ESSENTIAL

P2-E1 (Sec. II.A, p. 3; Eqs. (1)–(2)): Dimensional inconsistency and likely algebraic typo in the definition of BNL
- Problem: Eq. (1) defines AT(k1,k2,k3) = 3/[256 k1^2 k2^2 k3^2] × P(k1,k2,k3). Immediately after, Eq. (2) defines the configuration–dependent amplitude as BNL = (10/3) × P / [AT Σi k_i^3], and asserts BNL is dimensionless “by construction: P has degree 9, the prefactor of Eq. (1) removes degree 6, and the Σk^3 denominator removes the remaining degree 3.” But with Eq. (1) as written, AT has net degree 3, so P/AT has degree 6 and dividing by Σk^3 still leaves net degree 3: BNL is not dimensionless. In addition, with Eq. (2) as written, P cancels between numerator and AT’s numerator, contradictory to the next sentence “BNL retains its full dependence on the coefficients (c1,…,c6) through P via AT; no cancellation of P occurs.”
- Required fix: Correct the definition of BNL so that it is dimensionless and consistent with the stated dependence on P. Two self-consistent options exist:
  1) If Eq. (1) is correct, then BNL should be defined as BNL = (10/3) × AT / (Σi k_i^3). This yields degree 3/degree 3 → dimensionless, and preserves the P-dependence via AT.
  2) If Eq. (2) is to be kept as written, then Eq. (1) must be correspondingly changed so that AT has degree 6 (e.g., a 1/(k1 k2 k3) prefactor rather than 1/(k1^2 k2^2 k3^2)). 
  The paper currently mixes these two possibilities; as written the algebra and dimensional analysis are inconsistent. After correcting the equations, explicitly state which definition is used in all numerical evaluations (Table I, Fig. 1, all overlap computations), and re-verify that the benchmark values in Table I are reproduced by the corrected formula. This is load-bearing and must be fixed before publication.

P2-E2 (Abstract; §III.B p. 9–10; §II.A p. 5–6; Fig. 2 caption p. 11): Mischaracterization of the “injection–recovery validation”
- Problem: The abstract claims the template-overlap r was “validated via ℓ-space Fisher overlap, 200 injection-recovery realizations, and a 10,000-sample null-space scan.” In §II.A (p. 5–6), the paper explains the “injection–recovery” uses a 2D KSW-type CMB estimator on flat-sky patches with isotropic Gaussian noise and no mask, applied to a SPHEREx-like photometric-z noise covariance. This is not a 3D galaxy-bispectrum estimator and is not methodologically commensurate with the LSS bispectrum pipeline. Although the body text includes caveats, the abstract still treats it as a validation on par with the other checks.
- Required fix: Either (a) remove the injection–recovery test from the abstract’s list of validation pillars and clearly demote it in the main text to a 2D CMB-style heuristic consistency check, or (b) replace it with a proper 3D galaxy-bispectrum mock injection–recovery using an estimator consistent with the SPHEREx bispectrum analysis (including window/mask and redshift binning). Without (b), do not present the current 2D KSW test as validation for the LSS use-case.

P2-E3 (Data and Code Availability, p. 24–25): Missing frozen release/DOI and reproducibility provenance
- Problem: The manuscript says “archived at Zenodo (DOI inserted at submission)”. This is a placeholder. PRD requires stable, citable artifacts. Numerous internal file names are referenced in the main text (e.g., c9i epsilon ratio check.json), but no frozen tag/commit hash/DOI is provided for the repository these artifacts belong to.
- Required fix: Provide a final, public, immutable archival DOI (Zenodo or equivalent) and the exact Git commit hash(s) for the code and data used to produce all figures/tables. Replace “DOI inserted at submission” with the actual DOI. Ensure every named artifact in the text exists in the archived release and is referenced by path. If any figures/tables depend on stochastic seeds, include the seeds or store the generated data products in the archive.

P2-E4 (Abstract; §IV p. 10–11; Table IV p. 20): Mixing headline significances from different null procedures
- Problem: The paper is careful in many places to say which numbers are “not used in any headline,” but in the abstract it states: “validated via ℓ-space Fisher overlap [CMB-like], injection–recovery [2D CMB-like], and [LSS] noise-weighted r ≈ 0.83,” and later juxtaposes CMB-Fisher endpoint (r=0.876) and LSS-noise endpoints (r≈0.83) to motivate the 5.2–5.5σ band. For PRD, every time numbers from incommensurate procedures are placed side-by-side they must be explicitly marked as not directly comparable at that location, not only elsewhere.
- Required fix: In the abstract sentence that lists the r determinations, explicitly flag which are CMB-like versus LSS and add “the latter is used for SPHEREx, the former are cross-checks only.” In §IV/Fig. 2 caption already good; mirror that explicit caveat at every juxtaposition of CMB-Fisher and LSS-noise results (including the abstract) to comply with the journal’s comparability rule.

MAJOR

P2-M1 (Throughout, especially §II.A p. 3–6; §III.B p. 8–10): Basis-dependent null-space sampling is used to quote percentile “floors”
- Problem: The 10,000-sample null-space exploration is explicitly basis-dependent (uniform Euclidean measure in a chosen monomial basis). Yet the text quotes 16th–84th percentile ranges of |fNL| r/σ(fNL) as “floors” or “robustness bounds” (e.g., “gives a conservative lower endpoint 4.7σ…”). While you include caveats, these percentiles are not basis-invariant and therefore should not be given interpretive weight in the main narrative.
- Required fix: Move all percentile-based statements that depend on the basis-specific null-space measure to an appendix, and in the main text restrict to the central noise-weighted r = 0.84 ± 0.02 (weighting-scheme variation) and the CMB-Fisher cross-check. If you keep any percentile language in the main text, include an explicit bold caveat that it is basis-dependent and not a robustness bound.

P2-M2 (Length vs. contribution; entire manuscript): Overlength for a sensitivity recast
- Problem: The paper is a sensitivity recast (not an independent Fisher forecast) with a clear main result: mapping fNL = −35/8 to SPHEREx/MegaMapper, a template-overlap study, and a Bayes factor comparison. At 29 pages it is substantially longer than needed. Large portions are repeated caveats, internal artifact name listings in the main body, and extended discussions that could be appendixed (e.g., S3-orbit basis pedagogy, repeated restatements of assumptions (a)–(f), extended QSFI sidebars, long code-artifact inventories in running text).
- Required fix: Streamline the manuscript. Suggested target: ≤18 pages main text, moving (i) the S3 orbit/basis and null-space sampling details, (ii) the extended GR systematics parameter scan, and (iii) the long Bayes-factor prior-grid exposition into appendices. Keep in the main text the corrected core derivations, the validated r, the SPHEREx/Mega headline numbers (with clear caveats), and a concise Bayes-factor result.

P2-M3 (Appendix A; Sec. II.C p. 6–7): The “operator-algebra identity” check does not actually audit the contested normalization
- Problem: The Appendix correctly reminds that the in–in commutator yields −2 Im of the single time-ordered correlator. But the disagreement with Li et al. is not about the identity; it is whether their reported intermediate should be doubled for the physical observable in the stated convention. You have not re-derived the full time integrals, and the “symbolic” algebra stops before the integrals/control of late-time growth. As written, the paper risks appearing to overstate how much has been re-verified.
- Required fix: Rephrase all instances of “verified symbolically; Appendix A.1” (Abstract; §II.C) to: “we clarify that the single-ordering intermediate must be doubled by the −2 Im identity for the physical bispectrum; our numerical cross-checks are via benchmark-configuration matching to Cai et al.” This accurately states what was and was not done.

P2-M4 (Figures 4–5; captions p. 16–17): Axis units/definitions must be explicit and data provenance linked
- Problem: Figure 4 (σ(fNL) vs kmin) and Figure 5 (σ(fNL) vs bϕ prior) do not specify the binning, survey volume, sky fraction, redshift binning, or whether curves are SDB-only or bispectrum-only, and the axes lack units in the caption. The text implies SDB (blue/orange) and bispectrum (red dashed), but the figure must be self-contained for methods review.
- Required fix: Update captions/axes to state: which observable (SDB/bispectrum), the assumed survey parameters (fsky, volume/redshift range), the exact priors (20/30/50%), and units (kmin in h Mpc−1). Add a pointer to the archived JSON/NPY used to plot the curves.

MINOR

P2-n1 (Abstract; §IV p. 10–11): Consistent rounding on significances
- Problem: Using r = 0.84 and σ = 0.7, |fNL| r / σ = 4.375 × 0.84 / 0.7 = 5.25. Text alternates between 5.2 and 5.25. For the CMB-Fisher endpoint, 4.375 × 0.876 / 0.7 = 5.48 (rounded to 5.5). Keep consistent rounding in the abstract and main text.
- Required fix: Choose one rounding scheme (e.g., two significant digits for σ-levels) and apply consistently to all headline figures.

P2-n2 (§VIII.A p. 19): Planck PR4 recast arithmetic
- Check: fNL = −0.1 ± 5.0 (PR4); recast with r = 0.876 gives σ ≈ 5.71. Center −0.1/0.876 ≈ −0.114. The text reports “−0.1 ± 5.7” (without re-centering). Acceptable, but add a parenthetical “center shifts to −0.11 if recentered” for completeness.
- Required fix: Minor wording clarification as above (optional but recommended).

P2-n3 (Bibliography entries [27], [18], [32]): Verify metadata
- Problem: Some arXiv identifiers appear future-dated (e.g., arXiv:2511.09466). Ensure all citations are correct at acceptance time.
- Required fix: Double-check all references (journal, year, arXiv IDs) and update to final bibliographic metadata if published.

NITS

P2-N1 (Throughout): Typographic artifacts from PDF hyphenation (e.g., “per￾s”, “conser￾vative”)
- Required fix: Clean hyphenation artifacts in the final typeset version.

P2-N2 (§Data & Code Availability, p. 24–25): Internal file names in main text
- Required fix: Retain these pointers but move the exhaustive artifact list to a small table in the appendix or to the repository README, and keep only a succinct pointer in the main text.

Arithmetic spot-checks (all OK unless noted)
- |f_bounce|/|f_inf|: 4.375 / (5/12 × (1 − 0.9649)) ≈ 4.375 / 0.014625 ≈ 299; using 0.015 gives ≈ 292; your “≈ 290” is acceptable as an order-of-magnitude contrast, but consider quoting ≈ 295 if using the Planck central value.
- SPHEREx bispectrum significance (template-corrected): 4.375 × 0.84 / 0.7 = 5.25σ (OK).
- GR degradation σeff = √(0.7^2 + 1.0^2) = 1.22 → 4.375 × 0.84 / 1.22 = 3.01σ (OK).
- All-combined (bϕ 30% + GR 1.0): σeff = √(0.9^2 + 1.0^2) = 1.345 → 2.73σ (OK).
- MegaMapper ideal with template correction (σ = 0.5): 4.375 × 0.84 / 0.5 = 7.35σ; with r=0.88 → 7.70σ (OK).
- Planck PR4 recast: σeff = 5.0 / 0.876 = 5.71 (OK).
- Bayes factor delta prior, W = 30, σeff = 0.7: 30/(√(2π)×0.7) ≈ 17.1 (OK).
- Bayes factor with σeff = 0.833: 30/(√(2π)×0.833) ≈ 14.3–14.4 (OK).

Standalone-reader test
- Generally self-contained with clear assumptions (a)–(f). However, the BNL definition inconsistency (P2-E1) currently breaks the chain of definitions and must be corrected.

Effect sizes/context
- You consistently provide fractional degradations (e.g., r values, bϕ prior widening, GR σGR) and place σ-levels in context. Good.

Abstract-last drift sweep
- After corrections to E2 and consistent caveats on comparability (E4), the abstract will better match the calibrated statements in the body.

Summary recommendation
MAJOR REVISIONS

Justification
The manuscript’s principal numerical conclusions appear internally consistent and well-caveated, and the recast logic is clear. However, there is an essential algebraic/dimensional inconsistency in the load-bearing definition of BNL which must be corrected and traced through; the abstract currently overstates the injection–recovery “validation” (a 2D CMB-style test) for an LSS bispectrum context; and the data/code provenance needs a finalized archival DOI/commit hash. Additionally, the manuscript is substantially overlength for a sensitivity recast and should be streamlined. Once these issues are addressed, together with the minor fixes above, the paper would meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh pass)

ESSENTIAL

P2-E5 (Sec. II.A, p. 5–6): Logical/arithmetic error about percentile significance vs. “pre-systematic band”
- Problem: The text states “the 16th-percentile 4.4σ draw remains comfortably above the pre-systematic significance band” (referring to the 5.2–5.5σ template-corrected baseline). Numerically 4.4σ is below 5.2–5.5σ, not above.
- Required fix: Correct the sentence to reflect that the 16th-percentile null-space draw (4.4σ) is below the pre-systematic central-band (5.2–5.5σ), or remove the comparison.

P2-E6 (Abstract; §III.B p. 8–10): Inconsistent r-range wording vs. numbers
- Problem: The abstract claims “a local estimator recovers 84%–88% of the bounce signal” but immediately gives r ∈ [0.829, 0.876]. The lower endpoint 0.829 corresponds to 82.9%, not 84%.
- Required fix: Make the text and numbers consistent. Either report “83%–88% (r ∈ [0.829, 0.876])” or adjust the numerical interval to match “84%–88%”.

MAJOR

P2-M5 (§IV p. 10–11; Abstract): MegaMapper significance uses SPHEREx systematics without explicit abstract-level caveat
- Problem: In §V you note the MegaMapper 3–7σ envelope is illustrative and that the GR/bϕ budget is not independently calibrated to MegaMapper’s higher-z regime. However, the abstract presents “3–7σ” without explicitly stating that the degradation applied is the SPHEREx budget repurposed for illustration (not a MegaMapper-specific calculation).
- Required fix: In the abstract, explicitly say that the 3–7σ MegaMapper envelope reuses SPHEREx-style systematic assumptions “for illustration only” and is not an independently calibrated MegaMapper systematics forecast.

P2-M6 (§IV p. 10–11, “Shot-noise caveat”): Internal inconsistency in stated shot-noise degradation
- Problem: The paragraph first gives a simple Poisson estimate implying ≈3.3× inflation of σ(fNL) for a sparse anomaly-selected tracer (n̄ ≈ 10−5 h^3 Mpc−3, 1/(n̄P0) ≈ 10). It then asserts that “the bispectrum estimator effective degradation … is moderate, 15–30%,” which is in stark tension with 3.3×. The text does not make clear which figure applies to which observable, scale, or estimator.
- Required fix: Reconcile the numbers. Specify clearly (i) which channel each estimate refers to (power spectrum SDB vs. bispectrum; which triangle/k-ranges), (ii) why the naively large 3.3× does not apply to the actual bispectrum sensitivity at the squeezed-weighted modes, and (iii) provide a quantitative derivation or remove the 15–30% claim. As written, the two figures are contradictory.

P2-M7 (§III.B p. 8–10): Max r reported as “≲1.2” but scan range tops at 1.14
- Problem: You write “can mildly exceed unity (up to r ≲ 1.2 in our 10,000-sample null-space scan),” but elsewhere the sampled range is given as 0.55–1.14. The two statements cannot both describe the same scan.
- Required fix: Harmonize the quoted maximum r. If 1.14 is the actual maximum in the released scan, change “≲1.2” to “≲1.14,” or document a distinct scan where ≲1.2 was observed and cite its archived artifact.

P2-M8 (§VIII.B p. 21, “Linearization note”): Notational ambiguity for ε
- Problem: The same symbol ε is used both for the equation-of-state parameter ε = 3(1 + w)/2 (bounce context) and in the sentence recalling the slow-roll relation (where ε would usually denote the inflationary slow-roll parameter). This can mislead readers into thinking the same ε is used in both relations.
- Required fix: Use distinct symbols or add an explicit remark that the ε in the bounce parametrization (from w) is not the slow-roll ε used in inflation, to avoid confusion.

MINOR

P2-n4 (§III.B p. 8–9; Eq. (6) context): Central “noise-weighted” r choice is high vs. listed noise-weighted values
- Problem: The three noise-weighted determinations listed are 0.829, 0.830, 0.835, yet Eq. (6) states a central “noise-weighted” r = 0.84 ± 0.02. While 0.84 is within ±0.02, its center is noticeably above the mean of the listed noise-weighted values (~0.831). This affects headline significances at the percent level.
- Required fix: Either (i) adopt r = 0.83 ± 0.01 as the “noise-weighted” central value reflecting the three listed determinations, or (ii) justify why 0.84 is the appropriate center (e.g., inclusion of additional noise-weighted schemes not enumerated there) and point to the archived computations.

P2-n5 (Sec. II.A p. 5–6): Clarify the two “squeezed-limit insensitivity” tests
- Problem: You claim both that varying x3,min from 10−3 to 0.2 changes r by < 2×10−4 and that a log-weighted squeezed-enhanced grid shifts r by ~0.01. You later explain these probe different sensitivities, but the immediate juxtaposition reads as contradictory.
- Required fix: Add a one-line pointer in the first mention to the later explanatory paragraph (“this is not in tension with the ~0.01 shift under log-weighted re-sampling; see below”), to prevent confusion on first read.

P2-n6 (Abstract; Table II; §VI): Delta-prior “theoretical maximum” phrasing vs. re-booking
- Problem: The abstract says the delta-prior theoretical maximum is BF ≈ 14, which is true only after r = 0.84 re-booking (σeff = 0.833). Table II reports ~17 at r → 1. Although you later note this, the abstract’s “theoretical maximum” wording is potentially confusing.
- Required fix: In the abstract, explicitly qualify “BF ≈ 14 (delta-prior theoretical maximum under r = 0.84 re-booking)” and add a parenthetical that the r → 1 endpoint is ~17 (see Table II).

B, C, D, E, F, H, I, J checks (additional points not previously raised)

B. Figure-caption vs body-claim (additional)
- No further mismatches beyond your earlier Fig. 4–5 caption detail issues (already flagged in P2-M4). Other figures (1–3, 6) are broadly consistent with their textual descriptions.

C. Equation dimensional consistency (additional)
- No further dimensional issues found beyond P2-E1. Eqs. (3)–(5), (7)–(12), and Appendix A relations are dimensionally consistent within the stated conventions.

D. Internal cross-references (additional)
- Cross-references to Secs. II.C, IV, VII, VIII, Appendix A appear accurate; no new mis-citations found.

E. Null-procedure comparability (additional)
- No new juxtaposition issues found beyond P2-E4 and P2-M5.

F. Abstract faithfulness (additional)
- Besides P2-E6 and P2-M5/M6/M7 clarifications above, the abstract tracks the body.

H. Unquantified hedges (additional)
- The “anomaly-selected tracers” 10–20% improvement remains presented as an upper bound, but a brief pointer to a concrete Fisher setup or archived calculation would strengthen this. If kept, add “upper bound from a preliminary Fisher scaling; see archive item …” (optional).

I. Appendix vs main-text mismatch (additional)
- No new inconsistencies found; Appendix A matches the clarified (non-integral) scope described in the body once P2-M3 from the original report is addressed.

J. Stale numbers (additional)
- None beyond P2-M7 and P2-n4 above.

Summary of new issues
- Essential: P2-E5 (wrong “above” vs. “below” claim), P2-E6 (r-range mismatch in abstract).
- Major: P2-M5 (MegaMapper abstract caveat), P2-M6 (shot-noise inconsistency), P2-M7 (rmax inconsistency), P2-M8 (ε notation ambiguity).
- Minor: P2-n4 (central r choice), P2-n5 (clarify two “insensitivity” tests), P2-n6 (abstract BF phrasing vs. re-booking).

Once these additional corrections are made, alongside the fixes from the initial review, the manuscript will better meet PRD standards for numerical rigor, comparability, and clarity.