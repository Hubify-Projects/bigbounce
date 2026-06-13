# P5 R40conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/p5_desi_chirality.pdf` md5=e6ceb5ff pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7797 chars)
**Wall time**: 373.0s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T‑Web (Hahn 2007) Tidal‑Tensor Cross‑Check Across the DR1 Matched‑Spiral Sample” (P5)

Scope of review
- Focus: statistical–method validity, derivation chains, dimensional analysis, internal arithmetic, uncertainty propagation.
- I read the full manuscript (32 pp), including all tables, figures, equations, captions, and appendices, and recomputed the quoted statistics where possible.

Overall assessment
The paper is carefully executed and presents a thorough set of null tests for environment dependence of spiral chirality within DESI DR1, with a clearly declared primary estimand (the DESIVAST void vs non‑void contrast), multiple cross‑checks, and transparent multiplicity control. However, several issues prevent acceptance at PRD in its present form:
- The work relies critically on an “in preparation” companion (Paper IV) for the galaxy chirality labels and for the catalog‑monopole calibration, which is used repeatedly and quantitatively throughout, but is not self‑contained here.
- The paper intermingles internal repository paths and version identifiers throughout the main text instead of confining them to a compact Reproducibility section with a frozen DOI.
- Some nomenclature and presentation choices (calling a T‑Web implementation “V‑Web” in most of the paper; a combative footnote on units) need standardization/toning.
- A few numerical statements would benefit from explicit recalculations/clarifications and clearer uncertainty accounting for predicted vs observed σ.

Below I enumerate specific findings.

ESSENTIAL (acceptance contingent on all fixes)

P5-E1 (Abstract, pages 1–2; Secs. I–III, V–VI, VIII; pervasive). Load‑bearing reliance on an unpublished, in‑preparation “Paper IV”
- Problem: The chirality labels for all galaxies and the catalog‑wide monopole ∆fCW = −0.0026 (used for predictions, residuals, thresholds, and multiple interpretive statements) come from Paper IV (“in preparation”). The present paper repeatedly uses that value, and invokes Paper IV’s claim of a ∼9σ catalog‑level monopole, but does not provide a self‑contained, citable source nor a minimal in‑paper summary of the chirality classifier, its test‑time augmentation, per‑leg biases, and calibration uncertainties.
- Required fix:
  - Either (a) replace every use of the Paper IV monopole with a self‑contained estimate derived within this paper (e.g., the matched‑sample monopole fP5CW = 0.4972 is already computed and could be used consistently as the reference), or (b) include a compact but sufficient Methods appendix describing the chirality labeling pipeline, accuracy metrics, the estimator for the monopole including its uncertainty, and per‑leg systematics, and cite a stable DOI/arXiv version of Paper IV (not “in preparation”).
  - Remove/rephrase all “Paper IV v1.0.166” version‑history text; PRD requires a citable reference, not a repository version string.

P5-E2 (Appendix C, pages 31–32; pervasive artifact citations in main text). Missing immutable DOI(s) for code and data; excessive inline file‑path references
- Problem: The paper promises “a DOI‑minted archival snapshot” but does not provide the DOI. The main text is saturated with internal paths (pipelines/.../outputs/*.json) that are not stable scholarly references.
- Required fix:
  - Provide one or more minted DOIs (e.g., Zenodo/OSF) for frozen snapshots of: (i) the analysis code (with commit hash), (ii) the derived artifacts used to produce all tables/figures, and (iii) any preprocessed catalogs not available from public survey releases. List checksums for key artifacts.
  - Move virtually all internal path references from the main text into Appendix C (Reproducibility) or a data‑release readme. In the main text, replace them with stable DOI pointers (and a short descriptor).

P5-E3 (Sec. IV.A and title footnote, pages 4–6). Inconsistent nomenclature: “V‑Web” vs “T‑Web”
- Problem: The manuscript repeatedly calls its Hahn‑2007 tidal‑tensor (density Hessian) implementation “V‑Web,” although the “V‑Web” label is more commonly reserved for velocity‑shear classifications. A footnote attempts to explain, but the paper, figures, and captions still use “V‑Web,” while the title parenthetically says “T‑Web (Hahn 2007).”
- Required fix: Standardize terminology across the entire paper (text, figures, captions, tables). Either adopt “T‑Web” consistently, or explicitly define a paper‑local alias up front and then use one label (not both). The title, abstract, and body should match.

P5-E4 (Sec. IV.A, page 5; footnote). Tone and scientific style in unit‑conversion footnote
- Problem: The footnote text (“Any reviewer claim that the correct conversion is … is INCONSISTENT … and FALSIFIED by the pipeline source”) is combative and inappropriate for PRD.
- Required fix: Replace with a neutral derivation and a short example. E.g., “To express distances in h−1 Mpc we multiply the Mpc value by h; e.g., χ=843 Mpc becomes 570 h−1 Mpc for h=0.6766.”

P5-E5 (Stand‑alone reader test, pervasive; especially Secs. III.A, V.B, XI). Minimal, self‑contained description of the chirality labels
- Problem: A reader without access to Paper IV cannot assess how labels were generated, what “confidence” means, or classifier performance. Yet the entire analysis depends on those labels.
- Required fix: Add a concise appendix (1–2 pages) summarizing the labeler: data sources, augmentation, equivariance, cross‑validation performance, how the per‑object “confidence” score is defined, and any known leg‑dependent biases that are propagated here. Provide a frozen DOI for the exact label catalog used.

P5-E6 (Abstract, pages 1–2; Secs. V, VII, VIII; Table XII). Comparisons to the Paper‑IV‑predicted σ need explicit uncertainty accounting or exclusive reliance on the in‑sample monopole
- Problem: You correctly note that σpred = 2∆ fCW√N inherits uncertainty from ∆ fCW, and you quote a propagated uncertainty (≈0.36–0.7 on σpred for large N). However, several headline statements still use hard “max residual = 1.64σ”‑type language without bracketed uncertainty or without also showing the result when using the in‑sample matched‑catalog monopole as reference.
- Required fix: For every place that interprets the observed σ against σpred from Paper IV, present either:
  - Both residuals: σobs−σpred(Paper IV) and σobs−σpred(matched‑sample), or
  - A single residual using the matched‑sample monopole only (which is self‑contained), and remove interpretive language that implicitly treats σpred(Paper IV) as errorless.
  - Where a max residual is highlighted (e.g., 1.64σ in Table VII narrative), add “±0.xx” from the ∆ fCW uncertainty or rephrase conservatively (e.g., “≈1.6σ”).

P5-E7 (Length and focus; whole paper). The manuscript is too long for the contribution and mixes core claims with numerous code‑log details
- Problem: At 32 pages, the paper includes a great deal of pipeline‑level information in the main text that belongs in appendices or a data‑release document.
- Required fix: Trim to ≤ 18–20 pages by:
  - Keeping the primary DESIVAST result and one tidal‑tensor cross‑check in the main text.
  - Moving most internal‑path mentions, RNG‑stream re‑draws, and per‑cell JSON provenance to Appendix C or Supplementary Materials.
  - Consolidating secondary cross‑checks (ASTRA per‑object, Tempel, HEALPix scans) into a concise section with one figure/table each.

MAJOR

P5-M1 (Sec. IV.A, Eqn block, page 5). CIC window deconvolution and λth normalization
- Problem: You state the CIC assignment window is not deconvolved before taking derivatives and that “only the ordering and sign of eigenvalues relative to λth enter.” While acceptable for λth=0, this choice does bias the eigenvalue distributions and the effective threshold at other λth values.
- Required fix: Add a short quantitative comment (e.g., histogram widths/means) showing that the nine‑cell λth sweep conclusions are insensitive to this choice. Alternatively, add a sensitivity note or a deconvolution variant for at least one cell in Table VII.

P5-M2 (Sec. V.A, Eq. 2; Table VI; Sec. VII; Appendix). Multiple‑testing control clarity
- Problem: You correctly distinguish parametric Bonferroni and empirical max‑stat LEE treatments. However, at a few places the text lists raw |σ| and pLEE numbers side‑by‑side without explicitly repeating “these are not directly comparable” (even though §V already states non‑comparability of raw σ across N).
- Required fix: In every figure/table caption or paragraph that juxtaposes raw σfrom half with permutation pLEE, add a one‑line reminder that they are distinct nulls/statistics and not directly comparable.

P5-M3 (Sec. VIII.E, page 19). “Any‑hole vs maximal‑sphere” ∆ fCW continuity statement
- Problem: The text says “continuity within ±0.6 pp,” but the two values quoted are +0.06 pp (any‑hole) and −0.54 pp (maximal‑sphere), i.e. separated by ≈0.60 pp (not “±0.6 pp” around a common mean).
- Required fix: Rephrase to “differ by ≈0.6 pp” (or give both values explicitly and the absolute difference).

P5-M4 (Sec. IX.C, page 25). T‑Web cross‑validation scope
- Problem: The T‑Web fractions you compare are tracer‑dependent and measured in a cubic sub‑volume; your own run is an all‑spectro shell with a different mask. The current text is careful, but the title of §IX.C (“cross‑validation”) might be misconstrued as per‑object validation.
- Required fix: Retitle the subsection to “Concurrent‑literature volume‑fraction comparison” and add one line noting that this is not a per‑object validation.

P5-M5 (Appendix B, Tables XVI–XVII, pages 30–31). Ensure integer counts are fully consistent and reproducible from posted artifacts
- Problem: The provided counts appear consistent (I checked fCW from the integers), but PRD readers must be able to regenerate them from the DOI‑archived artifact.
- Required fix: In Appendix C, indicate the exact CSV/JSON filenames and SHA256 checksums that contain the contingency tables, and confirm that Table XVI and XVII are rendered from those files verbatim.

MINOR

P5-n1 (Abstract p. 1; Sec. VI.A p. 8; Table III p. 8). Filament σ value small rounding discrepancy
- Observation: From counts (203,261/408,187), σfrom half = 2(f−0.5)√N ≈ −2.56, whereas −2.61 is reported. Likely rounding from more precise internal f. Not material.
- Suggested fix: Consider quoting σ to one decimal place or recompute σ directly from integer counts to avoid rounding drift.

P5-n2 (Sec. VI.A, p. 8; Fig. 3). Clarify which parent is used for CIs when duplicates exist
- Suggestion: The caption notes row‑level parents include 3.56% duplicates and the unique‑spiral subset gives nearly identical results. Add a short parenthetical: “CIs are computed on the row‑level parent; recomputing on unique TARGETIDs changes the intervals by ≤2%.”

P5-n3 (Sec. VI.D, p. 10). Within‑class density quartiles: make the density definition explicit in table caption
- Suggested fix: Repeat in Table V caption that ρ is log10(1+δsmooth) with Rs=25 Mpc/h and λth=0.

P5-n4 (Sec. VII, Table VII; page 15). MC p‑values to 2–3 decimals
- Suggestion: Since NMC=1000 implies seMC ≈ 0.01–0.015, round pLEE to two decimals and report seMC in the caption once (you already do this elsewhere).

P5-n5 (Sec. VIII.A, page 17). n=6 per‑object V‑Web vs DESIVAST void disagreement
- Suggestion: The small‑n illustration is fine; add the exact binomial 95% upper bound (you partly do: 39%) with the formula or a citation.

P5-n6 (Sec. X, page 27; Table XIV). Clarify “entropy‑weighted” variance model
- Suggestion: You already mention a Monte Carlo validation; add the one‑sentence statement of the per‑class variance formula used for σ (now in the text) also to the table caption.

P5-n7 (Sec. XIII, page 28–29). RSD discussion
- Suggestion: Add a sentence explicitly stating whether the primary DESIVAST results are in redshift space (they are) and that the RSD robustness is a membership‑sensitivity test, not a re‑derivation of the void catalog under reconstructed positions.

NITS (cosmetic)

P5-N1 (Throughout). Repeated inline pipeline paths and file names in body text
- Move to Appendix C; keep the main text declarative and scientific.

P5-N2 (Sec. II, page 3). Parenthetical “title footnote” syntax appears as “a” floating marker before footnote text
- Fix formatting so the footnote marker and footnote text match PRD style.

P5-N3 (Figure labeling). Ensure all axes include units where applicable (e.g., Fig. 1 “DESI z” is dimensionless redshift; that’s fine, but consider simply “redshift z”).

P5-N4 (Word choice). Replace “sanity value,” “falsified,” etc., with neutral language.

Arithmetic and consistency spot‑checks (all OK unless noted)
- Table III counts produce the reported fCW values; σfrom half for void/wall/cluster match; filament differs by ~0.05σ due to rounding (P5‑n1).
- Omnibus homogeneity test χ2=3.55 (3 d.f., p=0.31) is plausible from the provided counts; the unique‑TARGETID re‑run is internally consistent (χ2=3.00, p=0.39).
- “Range across classes 1.98 pp” = 0.5034–0.4836; correct.
- Void 1σ half‑width 1/(2√428)=0.0242=2.42 pp; 2σ=4.84 pp; abstract values match.
- Cramér’s V = sqrt(4932/811,609) = 0.0780; correct.
- Bonferroni thresholds used (|σ|≈2.58 for K=5 at α=0.05; |σ|≈3.09 for K=5 at α=0.01; |σ|≈2.77 for K=9 at α=0.05) are correct.
- Table VIII: ∆ fCW = +0.00067, SE≈0.00219, z=0.31, p=0.76; correct (I recomputed).
- Table X (three DESIVAST algorithms) ∆ values and SEs check out numerically from nvoid/nnon‑void.
- Table XII σvs‑monopole residuals recompute from the given f and n (within rounding).
- Geometry/footprint/mask volumes: 3,150,086/(256^3)=0.188; “18.8% of cube” correct.
- V‑Web in‑mask volume fractions sum to 1.000.

Bibliography and claims
- Claims of novelty are cautiously phrased. Please remove or soften “largest … to date” unless you provide a citation survey or quantify “to our knowledge” with sample sizes of previous works.
- References [11], [12] are preprints; you use them only for supportive context, which is fine. Do not overstate them as validation.
- DESIVAST [13] is peer‑reviewed; good.

Abstract‑last drift sweep
- The abstract’s numbers (sample sizes, σ, p, ranges, pLEE, DESIVAST contrast, HEALPix p’s) are traceable and consistent with the body. One style adjustment is needed: avoid attributing deterministic precision to residuals when σpred is itself uncertain (P5‑E6).

Effect sizes
- You already report Cramér’s V for the class×program contingency and explain √n scaling. Good.

## Summary recommendation
MAJOR REVISIONS

The core analysis is careful and, in my checks, numerically consistent. The primary DESIVAST void vs non‑void result, the tidal‑tensor cross‑checks, and the multiplicity control are methodologically sound. However, the manuscript cannot be accepted at PRD without (i) removing the dependence on an unpublished “in preparation” Paper IV for load‑bearing inputs, or making the paper self‑contained with a stable DOI and a compact description of the chirality labels/monopole; (ii) supplying immutable DOIs for code/data and moving extensive file‑path logs to an appendix; (iii) standardizing T‑Web/V‑Web nomenclature; (iv) trimming length and toning down non‑scholarly phrasing. Once these essential items are addressed and the minor issues corrected, the paper should be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

The items below are new and do not duplicate points in my initial report. They are organized with the same [P5-Ex/Mx/mx/Nx] tags.

ESSENTIAL

P5-E8 (Sec. IV.A, k-space definitions; dimensional/implementation clarity)
- Issue: The wavevector construction is written as “ki = 2πni/L with L the box side (scipy fftfreq scaled by 2π/cell)”. This wording is ambiguous and can be read as ki = 2π ni / cell, which would be off by a factor Ngrid from the correct ki = 2π ni / L = 2π ni /(Ngrid × cell). If the code passes d=cell to fftfreq and then multiplies by 2π, the implementation is correct; but the prose as written is dimensionally confusing and risks a factor-of-N misinterpretation.
- Required fix: State the exact formula and SciPy call unambiguously, e.g. “k = 2π × fftfreq(N, d=cell) so ki = 2π ni /(N × cell) = 2π ni / L.” If possible, include a one-line code snippet in Appendix C.

P5-E9 (Sec. V, VI, VII; permutation nulls with duplicate rows)
- Issue: Permutation-based pLEE and pixel-scan p-values are computed on the 812,793 env-labeled row-level parent, which includes 3.56% duplicate TARGETIDs. While you verify that χ2 homogeneity on unique TARGETIDs is unchanged, you do not show the same unique-ID control for the permutation p-values (HEALPix, density, Phase-2 per-cell pLEE). Duplicates break strict exchangeability and can bias permutation nulls at the third decimal in borderline cases.
- Required fix: Recompute the label-shuffle p-values on the 783,820 unique-spiral parent (and re-tabulate pLEE for Table VII and Table VI) to show they are stable to duplicates. If differences occur beyond 1 Monte-Carlo s.e., report both.

MAJOR

P5-M6 (Fig. 8 bottom panel; caption vs colorbar range)
- Issue: The caption states the per-pixel σ range is −3.45 to +3.48, but the colorbar spans ±6 with no indication of clipping. This is a presentational mismatch that can mislead readers about the dynamic range.
- Required fix: Match the colorbar limits to the observed range (or state explicitly that the color scale is symmetric ±6 and values outside the stated range would be saturated; showing the actual min/max in the colorbar label is best).

P5-M7 (Parent mixing in DESIVAST sections; exact vs k-limited membership counts)
- Issue: Section VIII.B/Table VIII quote the k=20 KDTree membership counts (nvoid = 56,981; nnon-void = 621,964), while §VIII.E switches to the exact k-unbounded membership (nvoid = 57,081; nnon-void = 621,864) for footprint tests. This is defensible, but the transitions are easy to miss and could be read as inconsistent totals.
- Required fix: Add a one-line reminder in §VIII.E that the footprint re-tabulation uses the exact-membership parent (57,081/621,864), and that this parent differs by +100 void members from the k=20 parent used in Table VIII. Consider adding a small parent-table that lists both variants and where each is used.

P5-M8 (Sign-convention drift in ∆fCW; local reversals)
- Issue: The declared primary estimand is ∆fCW ≡ fnon-void − fvoid, but §VIII.E notes that the committed artifact “stores the opposite-signed fvoid − fnon-void values.” This inversion appears only in that subsection, but it invites confusion when comparing across tables/sections.
- Required fix: Standardize the sign convention in text, tables, and released CSV/JSON; or, if legacy artifacts must remain, add a prominent boxed note in Appendix C and a brief reminder wherever the opposite sign is used in the main text.

MINOR

P5-m4 (Sec. VII, Table VII narrative; σ vs pLEE comparability reminder in this specific location)
- Issue: Although §V.A explains that raw σ and permutation pLEE are different statistics, the Table VII narrative again places “max |σobs − σpred|” and pLEE side by side without the local reminder.
- Suggested fix: Add “Note: |σobs − σpred| and pLEE are not directly comparable statistics; the former is an analytic residual vs the monopole, the latter is an empirical max-statistic p-value.”

P5-m5 (Sec. IX.A, RSD scalar bound numerics)
- Issue: You quote σv/(aH) ≲ 5 Mpc/h at z ≲ 0.24 without showing the plug-in numbers. Readers will try to reproduce it (e.g., σv ≈ 400 km/s, H(z≈0.2) ≈ 74 km/s/Mpc, a ≈ 0.83 → 400/(0.83×74) ≈ 6.5 Mpc). The order of magnitude is right, but the bound depends on the chosen σv and H(z).
- Suggested fix: Give a concrete numerical example (σv, H(z), a) leading to the quoted range and specify the assumed σv. If you intend 5–8 Mpc/h across 0.01–2, say so in-line here (you do elsewhere).

P5-m6 (Sec. IV.A step 9; Gaussian kernel normalization)
- Issue: The Fourier-space Gaussian smoothing is referenced but not normalized (e.g., exp[−k^2 Rs^2 /2]). While standard, the exact convention matters if readers try to reproduce eigenvalue histograms or λth sweeps.
- Suggested fix: State the exact kernel form used in code (e.g., δk ← δk × exp[−k^2 Rs^2 /2]).

P5-m7 (Sec. V, Eq. 3; MC s.e. statement localization)
- Issue: The text gives the generic seMC values (≈0.010–0.015) but this is not echoed in the captions of Table VI and Table VII where the p-values appear.
- Suggested fix: Add “NMC=1000; MC s.e. ≈ 0.01–0.015” to those captions so readers do not need to backtrack.

P5-m8 (Sec. VI.B logistic regression covariates)
- Issue: The positional terms {|sin δ|, cos α} are ad hoc and not orthogonal; one might expect both sinα and cosα if the intent is to capture RA dependence. This is a cosmetic modeling note since primary conclusions do not hinge on it.
- Suggested fix: Clarify that the positional regressors are only a loose nuisance check (or use a full set {sin α, cos α, sin δ, cos δ} or spherical harmonics Y1m if you want to justify the dipole-null consistency).

P5-m9 (Fig./text units consistency)
- Issue: The manuscript alternates “Mpc/h” and “h−1 Mpc.” Both are standard, but mixing styles can confuse. The title/footnote and §IV use “Mpc/h,” while the unit-derivation footnote speaks in “h−1 Mpc.”
- Suggested fix: Pick one style for distances in the main text and figures and stick to it, noting the equivalence once.

P5-m10 (Sec. VIII.E, “continuity within ±0.6 pp” phrasing)
- Issue: Already fixed conceptually in my earlier P5-M3, but here it also appears in the narrative sentence introducing the any-hole vs maximal-sphere contrast. Make sure both the narrative and the parenthetical show the absolute difference (≈0.6 pp).

NITS

P5-N5 (Sec. V.B RNG reuse across families)
- Issue: You note that the same deterministic seed initializes each scan family’s generator, hence “identical underlying random streams are shared across families,” and then show a few stream-independent re-draws. For transparency, this should be summarized once in Appendix C with a statement that all headline p-values were cross-checked with an independent RNG seed and found stable to ±1 seMC; right now, this is scattered.
- Fix: Consolidate the RNG policy and the stream-independence confirmation into Appendix C and cite it where needed.

P5-N6 (Sec. X, Table XIV caption; entropy-weighted σ)
- Issue: The variance model used for entropy-weighted counts is explained in text but not reiterated in the table caption.
- Fix: Add “Per-class σ uses Var ≈ Σi Pclass,i^2/4 under the Bernoulli-0.5 null (MC-validated to ≤1.2%).”

Brief rationale for additional pass
I focused this pass on places where dimensional/implementation ambiguity could plausibly hide a factor error (k-grid definition), where null procedures might be subtly biased (permutations with duplicates), and on smaller caption/figure mismatches that affect clarity (colorbar scaling, parent mixing). The core numerical claims remain consistent on recheck; the new items above are primarily about removing residual ambiguity and ensuring reproducibility/interpretability at PRD standards.