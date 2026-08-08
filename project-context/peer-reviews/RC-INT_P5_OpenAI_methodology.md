# P5 RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=91742098 pages=34
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5363 chars)
**Wall time**: 413.9s

---

Referee report (PRD methodology; tag P5)

Scope of review
I audited the methodology, statistics, dimensional analysis, and internal arithmetic throughout the manuscript, including all tables/figures/equations. I recomputed quoted σ, p-values, ranges, and key ratios from the numbers provided, and checked abstract/conclusion scalars against the body.

Overall
The core estimand (void vs non-void ΔfCW) is well-defined and, in the DESIVAST-anchored analysis, is computed with standard two-sample binomial statistics. The paper makes a commendable effort to separate “raw σ-from-half” from monopole-referenced residuals and to control multiplicity in the primary family. However, several issues require correction/clarification before PRD publication. One error (a miswritten Clopper–Pearson bound) is mathematical and must be corrected. The paper also contains internal versioning/back-compat prose and LaTeX label mentions that should not appear in a PRD paper. Finally, while the authors do declare primary vs secondary after the fact, PRD requires that the abstract/conclusions be crystal-clear about post-hoc designation and scope of inference; a few places overstate or obscure this.

Findings

ESSENTIAL

P5-E1 (Sec. VIII A, p. 18): Miswritten one-sided Clopper–Pearson expression
- Quote: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n for 0 successes in n trials...)”
- Problem: As printed, “0.051/6” is the wrong operation and equals 0.0083, not 0.607. The intended formula is 1 − α^(1/n); with α = 0.05 and n = 6, α^(1/6) ≈ 0.607 → 1 − 0.607 = 0.393 (39.3%). The text mixes superscript and division, which is mathematically incorrect as printed.
- Required fix: Replace “1 − 0.051/6” with “1 − 0.05^(1/6) = 0.393”. Also replace “α1/n” with “α^(1/n)” everywhere. Verify all other exponentiation notations render unambiguously in the final typeset PDF.

P5-E2 (Multiple places incl. Abstract p. 1–2, Sec. V B pp. 7–8, Sec. XV pp. 30–31): Post-hoc primary analysis designation and headline wording
- Problem: The primary DESIVAST path is designated post-hoc (“primary designation is declared post-hoc — no single a priori preregistered plan was filed”). While this is acknowledged in-body, the Abstract and Conclusion present results in a headline form that reads as if the primary estimand was pre-declared. PRD requires that post-hoc selection be explicitly and prominently stated wherever “primary” claims are made, and that the scope of inference be accurately conveyed in the Abstract.
- Required fix: In the Abstract and Conclusions, add a brief clause making the post-hoc nature explicit, e.g., “We designated, post hoc, the DESIVAST-anchored void contrast as primary; results are robust to this choice.” Also include a one-sentence multiplicity disclaimer in the Abstract that the five DESIVAST estimators were controlled as a Bonferroni-5 family (list threshold and that none approach it), to match body claims.

P5-E3 (Sec. IV A, p. 5–6): Internal versioning/back-compat labels in scientific prose
- Quote: “this paper uses ‘T-Web’ ... (the artifact filename [A3] and the sec:vweb cross-reference label are retained for backward compatibility...)”
- Problem: Internal LaTeX label (“sec:vweb”) and artifact filename considerations should not appear in scientific prose.
- Required fix: Remove “sec:vweb cross-reference label” and rephrase to a neutral nomenclature note without internal labels/repo implementation details. Keep the data/code availability pointers in Appendix/DA section only.

P5-E4 (Sec. VII, Table VIII, p. 16; Sec. VI E, Table VII, p. 13): Monte Carlo resolution vs significance claims
- Problem: All permutation p-values use NMC = 1000. The text quotes p-values to three decimals and sometimes contrasts 0.13 vs 0.14 vs 0.23 etc. The paper does note the MC SE (~0.010–0.015) in Sec. V, but in tables/captions the precision is not always accompanied by this caveat. PRD requires that numerical precision reflect MC resolution whenever p-values are used inferentially.
- Required fix: In the captions of Tables VII and VIII (and any figure/table where permutation p is reported), append “NMC = 1000; MC SE ~0.01–0.015” or round to two decimals consistently and refer to Sec. V for resolution. Ensure no sub-SE comparisons are used argumentatively.

P5-E5 (Abstract p. 1–2; Sec. VI A pp. 8–9): Distinguish incomparable σ consistently at juxtaposition
- Problem: The manuscript usually distinguishes raw σfrom half and σvs monopole, but there are places in the Abstract where raw σ from different-class Ns are placed together without an immediate “not comparable across Ns” caveat (e.g., listing −2.61σ filament and −4.66σ cluster alongside +0.55σ wall and −0.68σ void). The in-body Table IV caption contains the caveat, but the Abstract does not.
- Required fix: In the Abstract sentence listing per-class σ, add “(σ scales as √N and is not comparable across classes; see Table IV)”. This satisfies the required explicit qualification at every juxtaposition.

MAJOR

P5-M1 (Sec. IV A p. 5–6, footnote 1): Unit-conversion exposition
- Problem: The multiply-by-h convention discussion is helpful, but the phrase “The incorrect divide-by-h operation ... is not a valid alternative” is overly didactic and could confuse readers accustomed to common community shorthand. PRD prefers neutral, equation-based clarity.
- Required fix: Replace with a short equation block showing D[h−1 Mpc] = h · D[Mpc], and remove the rhetorical “incorrect” sentence. Keep the sanity check χ(z = 0.2) numeric example.

P5-M2 (Sec. IX A pp. 23–25): Selection correction and mask handling
- Problem: The canonical T-Web classifier is built with a global mean δ over 0.01 ≤ z ≤ 2 without angular completeness weighting; the authors then provide a shell-corrected rebuild and a BGS-randoms-weighted stress test limited to z < 0.5. The description is thorough, but the headline analysis remains the unweighted canonical run. For PRD-level methods, a brief quantitative statement of how much the canonical results could be biased at z > 0.5 under unmodeled selection would help bound interpretation (beyond the shell-corrected low-z collapse of range to 0.05 pp).
- Required fix: Add an explicit statement quantifying the fraction of the env-labeled spirals above z = 0.5 (or show that it is negligible), and state that the shell-corrected rebuild covering all 21 shells (up to 1.7–2.0) yields χ^2 = 0.11 (p = 0.99) on the same parent. If the shell-corrected rebuild differs (e.g., only δ correction, not randoms), say so and bound residual risk at high-z. As written, some readers may overinterpret the unweighted canonical result at z > 0.5.

P5-M3 (Abstract p. 1–2; Sec. II p. 4; Sec. VIII F p. 21–22): Standalone-reader clarity on P4 dependence
- Problem: The paper depends on two inputs from Paper IV (labels and the global monopole amplitude). It states that the primary DESIVAST contrast does not depend on the amplitude. However, the Abstract references the P4 monopole multiple times without, in that location, stating clearly that the internal matched-sample monopole fP5 = 0.49719 is used for σvs monopole residuals, and that all permutation tests condition on observed counts.
- Required fix: In the Abstract or footnote, add one sentence: “All permutation tests condition on the observed catalog-wide CW fraction in this matched sample; σvs monopole residuals use the internally measured fP5 = 0.49719; the primary void contrast is independent of any catalog-wide monopole.”

P5-M4 (Sec. X pp. 27–28; Table XV): T-Web vs ASTRA per-object disagreement description
- Problem: The EDR-overlap cross-check shows extreme per-object class disagreement (T-Web argmax nearly all filament+cluster; ASTRA has all four classes). This is attributed to grid/edge effects, but the text could benefit from a more quantitative descriptor of how many overlapping TARGETIDs agree/disagree (confusion matrix fractions).
- Required fix: Add a 4×4 confusion matrix (counts or fractions) for ASTRA argmax vs T-Web class on the Noverlap sample to substantiate the qualitative statement, and note the fraction of objects in pixels within one grid cell of the EDR rosette boundary, if available.

MINOR

P5-m1 (Sec. VI A p. 8–9; Appendix B, Tables XVII–XVIII): χ^2 tests and duplicates
- Comment: The authors correctly recompute the 4×2 homogeneity test on the unique-TARGETID subset. Add the exact count of duplicated TARGETIDs per class to Appendix B for completeness (already implied but not tabulated).

P5-m2 (Sec. VI C p. 10–12): Density-quintile proxy endogeneity
- Comment: The exogenous redefinition using the full matched-primary parent is good. Consider adding the numerical Pearson correlation between endogenous and exogenous quintile indices to quantify concordance.

P5-m3 (Sec. IV A p. 6–7): CIC window deconvolution
- Comment: The decision not to deconvolve the CIC window is fine because only eigenvalue ordering matters, but it would help to state the grid Nyquist wavenumber and a sentence quantifying that deconvolution would not change the λ ordering at the Rs used.

P5-m4 (Sec. VI D p. 11–13): Two-sample z on overlapping splits
- Comment: The caveat is present. Add the unique-TARGETID two-sample result for filament bright vs dark (if computable without overlap) or clearly state it cannot be computed with current artifacts.

P5-m5 (Sec. VIII E p. 20–21; Table XII p. 21): HEALPix pixelization choice
- Comment: You switch between NSIDE = 16 (table) and NSIDE = 32 (figure/correlation). Add a one-sentence note on why NSIDE = 16 is used for the stratified table (stability of counts per pixel) to avoid confusion.

P5-m6 (Sec. VII p. 15–16; Fig. 7 p. 17): “Resolved” vs “unresolved” language
- Comment: Clarify in the caption that Rs = 10 Mpc/h is below the 25.9 Mpc/h grid sampling scale, hence behaves as a near-unsmoothed pixelated limit, and results from these three cells are excluded from robustness claims (this appears in text; mirror it in the figure caption as well).

P5-m7 (Throughout): Terminology “pp”
- Comment: First time “pp” appears in the Abstract/Intro, define explicitly as percentage points.

NITS

P5-n1 (Sec. IV A p. 5–6): Typographical spacing around “σfrom half”
- Fix: Insert thin space or hyphen (e.g., “σ-from-half”) consistently.

P5-n2 (Sec. IV A p. 6): Minor typography
- Quote: “Ngrid = 2563” → typeset as Ngrid = 256^3 throughout.

P5-n3 (Sec. VI B p. 10): Figure 4 caption
- Suggestion: State the number of objects per redshift bin (or typical) for context.

P5-n4 (Sec. XI p. 28–29; Table XVI): Confidence threshold sweep
- Suggestion: Add the effective sample size remaining per threshold row (you list n; consider a parenthetical “fraction of full sample”).

P5-n5 (Appendix A p. 31–32): Toy EFT mapping
- Suggestion: Move the toy-operator mapping to a short paragraph in Discussion or keep in Appendix but add an explicit “not used in any inference” sentence to avoid readers inferring constraints.

Arithmetic and consistency spot-checks (passed)
- Abstract/body numbers: matched after-dedup sample 2,232,212; chirality-relevant 791,635; T-Web parent 14,622,283; all consistent with Tables II and Sec. III B.
- Per-class fCW and σ-from-half (Table IV) recompute correctly within rounding: filament −2.61; cluster −4.66; wall +0.55; void −0.68.
- Range across classes 1.98 pp from Table IV (0.5034 − 0.4836).
- Bonferroni thresholds from Eq. (2) check: K = 5 at α = 0.05 → |σ| ≈ 2.58; K = 9 at α = 0.05 → |σ| ≈ 2.77.
- DESIVAST-anchored ΔfCW = +0.00067, SE = 0.00219, z = +0.31, p = 0.76 (Table IX) recompute from nvoid = 56,981 and nnon-void = 621,964.
- V2-REVOLVER catalog-native ΔfCW = −0.0037, SE = 0.0029, z = −1.25, p = 0.21 (Sec. VIII D) recompute correctly.
- Footprint-restricted non-void contrast ΔfCW = +0.0018, SE = 0.0023, z = +0.78 (Table IX) recompute correctly.
- Density quintile σpred at N = 158,327 equals 2.07; residuals in Table V consistent.
- HEALPix max-|σ| and permutation p-values in Table VII consistent with Figure 6 text.
- Phase 2 per-cell ranges dominated by void-bin binomial floors; reported nvoid = 363–853; 1σ floor 1.7–2.6 pp matches.

Abstract-last drift sweep
- The abstract’s main scalars (n, ΔfCW, per-class fCW and σ, p-values, range, Phase 2 p-value band, HEALPix p-values, DESIVAST contrasts |ΔfCW| ≤ 0.004 with |z| ≤ 1.25) are all traceable and consistent with body tables and sections.
- Required wording adjustments specified in P5-E2 and P5-E5.

Provenance/data availability
- The GitHub tag and artifact IDs are comprehensive. Ensure a DOI snapshot is actually minted and available at acceptance. Minor editorial: keep artifact IDs in Appendix C/D; minimize in main text.

Page length
- 34 pages for a single primary null result plus extensive diagnostics is long but can be justified given the breadth of robustness checks and the data-release orientation. If the authors trim, focus on streamlining some descriptive secondary paths (e.g., repeated statements of the same null across multiple variants) and moving non-essential prose to Appendix.

## Summary recommendation
MAJOR REVISIONS

The scientific core (DESIVAST-anchored ΔfCW null) is sound and the arithmetic/statistical handling generally careful. However, at least one mathematical error (Clopper–Pearson expression) must be corrected, and the Abstract/conclusion need explicit post-hoc/multiplicity caveats. Internal versioning/label references should be removed from main prose. Clarifications on selection-weighting scope and a quantitative T-Web vs ASTRA confusion matrix are also needed for PRD-level methodological clarity. Addressing these items should be straightforward and will bring the paper to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit; new items only)

ESSENTIAL

P5-E6 (Sec. VIII E, Table IX): Minor σ-from-half mismatch on footprint-restricted control
- Issue: For the “Footprint-restricted non-void (exact)” row (n = 253,276; fCW = 0.4983), recomputation gives σfrom-half ≈ −1.71 using σ = (f − 0.5)/(0.5/√n). The table prints −1.73.
- Required fix: Recompute from the precise internal fCW used (more decimals) or correct the printed σ. If the discrepancy is rounding-driven, add a note that σ is computed from full-precision counts.

MAJOR

P5-M5 (Sec. VI D, Table VI caption/column labels): Ambiguity in “ρ̄” units for within-class density quartiles
- Issue: The table reports “ρ̄” values 0.90–2.21 but explains in the caption only later that these are log10(1 + δsmooth). As printed, “ρ̄” suggests a mean density, not log-density.
- Required fix: Rename the column header to “mean log10(1+δsmooth)” (dimensionless) or add it parenthetically in the header to avoid unit confusion, and keep the example mapping (2.21 → 162×) in the caption.

P5-M6 (Abstract p. 1–2): Causal attribution for the T-Web void σ in low-z
- Issue: The Abstract states the T-Web void σ = −0.68 is “survey-edge artifact dominated at z ≲ 0.24.” While the body (Sec. VIII A/E) substantiates survey-edge impacts and the T-Web-vs-DESIVAST mismatch, the void bin here is also n = 428 and strongly shot-noise limited. The Abstract wording reads as a definitive causal attribution.
- Required fix: Temper the Abstract phrasing to reflect joint causes, e.g., “dominated by small-n and survey-edge systematics at low z (see DESIVAST re-projection).”

MINOR

P5-m8 (Sec. VII, Table VIII vs text; Abstract): Range/p-bands consistency note
- Observation: The Abstract quotes Phase-2 look-elsewhere p spanning 0.13–0.56 across nine cells; the text highlights 0.13–0.48 for resolved cells (Rs ∈ {25, 50}). This is consistent (the wider 0.56 includes unresolved Rs = 10), but it would help to say “0.13–0.56 across all nine cells (0.13–0.48 across the six resolved cells).”

P5-m9 (Sec. IV A, step 12; Sec. VI D): Monotone-transform equivalence claim
- Comment: You correctly state that quartiles of log10(1+δ) and of 1+δ coincide (monotone transform). To preempt reader confusion, add a one-liner that the actual bin edges differ numerically but induce identical membership because ranking is preserved.

P5-m10 (Sec. IV A, step 9): Sign/normalization exposition could be tightened
- Comment: You justify the Fourier sign and the effect of not deconvolving the CIC window by appealing to ordering/sign. Consider adding one quantitative sentence that W(k) ≥ 0 for CIC, so mode-wise multiplication cannot flip signs, and that λth = 0 renders absolute scaling immaterial; this closes the loop for readers worried about normalization.

P5-m11 (Sec. VIII E, RSD Monte Carlo paragraph): Define σλ used in boundary-crossing estimate
- Issue: You refer to “∼ 0.04 σλ” without defining σλ in that paragraph (later you do clarify it is the rms width of the per-cell smoothed-eigenvalue distribution). To avoid ambiguity, pull the definition forward to the first mention.

P5-m12 (Sec. VI A text vs Table IV): Duplicate-row inflation caveat near σ listing
- Observation: The text immediately around Table IV properly warns σ are √N-scaled; when reproducing the four σ in prose (outside the caption), append a parenthetical “not comparable across class Ns” there as well (you already do this in the caption; mirroring in-prose keeps the warning co-located with the numbers).

P5-m13 (Sec. X, ASTRA cross-check): Quantify overlap-pixel edge exposure
- Suggestion: You attribute the T-Web vs ASTRA argmax disagreement in the EDR overlap to rosette-edge/grid effects. If available, add the fraction of overlap TARGETIDs whose HEALPix pixels lie within one 25.9 h−1 Mpc grid cell of an EDR rosette boundary (or analogous mask-edge measure). This would substantiate the qualitative edge argument.

NITS

P5-n6 (Sec. VIII E, Table XII): Totals sanity note
- Comment: The four NSIDE = 16 bins in Table XII sum exactly to nlz = 678,945. Consider stating this explicitly in the caption (“bins sum to nlz”) to reassure readers the footprint proxy partition is exhaustive.

P5-n7 (Sec. IX A, selection-weighted rebuild): “99.3%” coverage figure provenance
- Comment: You state “99.3% of matched spirals lie in 0.01 < z < 0.50.” Add the exact counts (e.g., “786,xxx/791,635”) or a pointer to the artifact ID where this is computed, so readers can verify the fraction.

P5-n8 (Appendix B, Table XVIII): Cramér’s V formula note
- Comment: Add “(min(r−1,c−1) = 1 for a 4×2 table, so V = sqrt(χ2/n))” to make clear why no additional divisor appears.

P5-n9 (Sec. VI B, Fig. 4 caption): Bin populations
- Comment: You already note that high-z bins are sparse. Add typical n per bin or the minimum/maximum n to calibrate the CI widths visually.

P5-n10 (Throughout): Mixed units styling
- Comment: You alternate “Mpc/h” and “h−1 Mpc”. Consider standardizing to one convention in running text (keep both where quoting external catalogs).

NO OTHER ARITHMETIC DISCREPANCIES FOUND
- I rechecked all headline scalars, σ, z, p, ranges, and Bonferroni thresholds that can be recomputed from the printed counts. Apart from P5-E6’s minor σ rounding inconsistency in Table IX, all other numbers I tested match to rounding as claimed.