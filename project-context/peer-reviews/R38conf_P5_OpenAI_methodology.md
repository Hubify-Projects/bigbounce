# P5 R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.73.pdf` md5=4109fb18 pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5916 chars)
**Wall time**: 372.2s

---

Referee report on “Environmental Dependence of Spiral Chirality …”

Scope of review
I evaluated the full manuscript for statistical and methodological rigor, internal arithmetic consistency, dimensional correctness, appropriate multiple-testing control, fidelity between abstract and body, and reproducibility claims. Below I list all issues found, classified by severity and with concrete required fixes.

ESSENTIAL

P5-E1 (Title page, p.1): Version tag and internal build string in the scientific title block
- Problem: “(Dated: June 2026 — v0.1.73-2026-06-13)” appears under the title. This is internal versioning/ship metadata and is not acceptable in a PRD publication.
- Required fix: Remove the explicit internal version tag from the PDF. Retain only a standard “(Dated: Month Year)” if desired.

P5-E2 (Throughout; e.g., Abstract p.1; Sec. II pp.3–4): Load-bearing reliance on an unpublished “Paper IV” for both the chirality labels and the global monopole calibration; version-history language in the body
- Problem: Numerous statements import results from “Paper IV [3] … in preparation and not yet peer reviewed,” including the −0.26 pp global monopole, its interpretation as classifier bias, and a long digression on withdrawn harmonic-channel statistics (“Paper IV v1.0.166 … earlier version withdrawn”). PRD expects the present paper to be self-contained. Using an unpublished work as a load-bearing source for the central calibration (∆fCW = −0.0026) and for interpretive claims is not acceptable. Version-history language (“v1.0.166”) and process narration do not belong in the body text.
- Required fix: Make the analysis fully self-contained by:
  - Recasting all monopole-referenced predictions and residuals to use ONLY the matched-sample monopole measured within this paper (fP5_CW = 0.49719 on n = 812,793 env-labeled rows, or the corresponding unique-sample value), with its own propagated uncertainty. Remove dependence on ∆fCW from Paper IV in all load-bearing places (e.g., Eq. (1), σpred values, density-quintile comparisons). Where comparison to the catalog-wide monopole is informative, present it as context in Discussion only, not as a required calibration.
  - Remove version-history and audit-log prose about Paper IV revisions from the body. If necessary, retain a brief neutral citation indicating that the chirality catalog is public (include a DOI or archived hash) and that a companion analysis exists, without relying on its conclusions.

P5-E3 (Throughout; Abstract title line, Sec. IV p.4 footnote, captions): Inconsistent and potentially misleading nomenclature “V-Web” used for T-Web (tidal tensor) classifier
- Problem: The manuscript implements the tidal-tensor Hessian/eigenvalue classifier (Hahn et al. 2007) but repeatedly labels it “V-Web,” which in the literature denotes the velocity-shear classifier (Hoffman et al. 2012). A footnote tries to justify the naming, but the mismatch can confuse readers and bibliographic searches.
- Required fix: Rename the implemented classifier consistently as “T-Web (tidal-tensor, Hahn et al. 2007),” and reserve “V-Web” only for velocity-shear contexts. Update the title, abstract, body text, figure captions, and tables to use “T-Web” for your implementation. If you wish to mention that parts of the community loosely say “V-Web,” do so once in a parenthetical note, but use “T-Web” everywhere else.

P5-E4 (Throughout; many places, e.g., Secs. IV–VIII; captions; parentheses): Internal file paths, JSON filenames, and pipeline internals appear in the main text
- Problem: The paper embeds many internal repository paths and filenames (e.g., “pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json”) throughout the scientific narrative. This is not standard PRD style and impedes readability. Such details belong in a Data/Code Availability section or Supplement.
- Required fix: Remove all inline file paths and JSON artifact names from the body and figure captions. Consolidate them in a single Data and Code Availability section or Supplement, ideally with a single DOI to an immutable archive and a brief table listing key outputs and their file names there.

P5-E5 (Sec. V p.6 and subsequent use): σ values from different reference models juxtaposed without always explicitly reminding non-comparability
- Problem: The paper generally distinguishes raw σfrom half, σpred (monopole model), and σvs monopole residuals, but several juxtapositions (e.g., Abstract reporting void σ = −0.68 alongside filament/cluster σ = −2.61/−4.66; Sec. VI A Fig. 3 caption) present raw σ values from different N side-by-side. Although you note at points that σ scales as √N, this caution is not uniformly reiterated at every juxtaposition, as requested in the journal’s guidance.
- Required fix: At every place where σfrom half for different classes/bins are listed side-by-side, add an explicit sentence that these σ are not directly comparable across bins of different N and that the appropriate comparable statistic is the monopole-subtracted residual or a two-sample test. In tables, add a footnote to this effect.

P5-E6 (Primary analysis declaration, Sec. V.B p.7): Primary estimand chosen post hoc
- Problem: You explicitly state no preregistration and that the “primary” analysis path (DESIVAST-anchored) is designated post hoc. While preregistration is not required by PRD, the paper must avoid any appearance that the primary was selected because it produced the desired outcome. The multiplicity handling is otherwise careful, but the present framing invites concerns.
- Required fix: Define the primary estimand and analytic path in a neutral, prospective manner in the Methods section without process narrative. Make clear that the DESIVAST void vs non-void contrast is the prespecified estimand reported with its two-sample test (z, p, CI), and move all other paths to clearly labeled secondary/robustness sections. Remove language about choosing the primary after inspecting results.

MAJOR

P5-M1 (Data/Code availability, Appendix C p.31 and mentions throughout): Missing immutable archival DOI and exact frozen commit hashes
- Problem: The text promises “A DOI-minted archival snapshot … accompanies journal submission,” but no DOI is provided. The GitHub path and “manuscript tag v0.1.73-2026-06-13” are not immutable identifiers. PRD requires concrete, citable archival references for reproducibility.
- Required fix: Provide an immutable DOI (e.g., Zenodo) for the exact code and artifacts used. Include a short manifest in Appendix C listing the key artifacts (datasets, environment labels, statistics tables) with checksums, and the exact git commit hash(es). If the chirality catalog is on HuggingFace, include its exact version/tag hash as well.

P5-M2 (Terminology and scope, Sec. VIII RSD treatment, pp.15–16): RSD sensitivity claims partly qualitative; quantitative bound conflates displacement and eigenvalue deformation
- Problem: The RSD discussion mixes a scalar “σv/(aH) ≲ 5 Mpc/h” heuristic and an anisotropic eigenvalue deformation narrative. The concluding “3–5% of cells near boundaries; expected effect sub-dominant at ~10^-3 precision” is plausible but not rigorously derived.
- Required fix: Clarify which statements are heuristic (label as such) and which are quantitatively checked. Where claiming sub-percent contamination, provide a simple bound calculation with numbers (e.g., boundary-cell fraction × maximal class-flip impact on ∆fCW), or relegate this to a clearly marked caveat. The existing ±5 Mpc/h Monte Carlo membership sensitivity test is useful—foreground that result as the quantitative bound for the DESIVAST primary analysis, and de-emphasize the heuristic eigenvalue-band argument unless you formalize it.

P5-M3 (Length and focus): Manuscript is overly long for the contribution
- Problem: 31 pages are spent to establish robust nulls and reproducibility. While thoroughness is appreciated, a methods paper in PRD should be concise. Several long digressions (e.g., Paper IV version history; multiple repetitions of pipeline file paths; Appendix A toy EFT operator) are not necessary to support the main methodological claims.
- Required fix: Reduce to ≈20–22 pages by:
  - Removing Paper IV process/history and reducing references to it to a single short paragraph in Data, as per P5-E2.
  - Moving all file-path specifics out of the main text (P5-E4).
  - Dropping Appendix A (toy EFT mapping) or moving it to Supplementary Material with a one-sentence pointer; it is unrelated to the methodology proofs presented here.

P5-M4 (Classifier naming in figures/captions): Figures and captions must be updated to coherent terminology
- Problem: Figures 2, 3, 6, 7, 9 and related captions mix “V-Web”/“T-Web” and “sheet/wall” language inconsistently.
- Required fix: After resolving P5-E3, revise all figure titles, axis labels, and captions to use consistent class names and classifier terminology. Ensure that “wall” vs “sheet” mapping is clearly stated once (e.g., “wall (sheet)”) and used consistently thereafter.

P5-M5 (Abstract-last drift sweep): Ensure every abstract number is traceable in-body and phrased identically
- Problem: The abstract states “the counting-statistics floor of ±2.4 pp (the 1σ binomial half-width of the n = 428 V-Web void bin; 2σ half-width ±4.8 pp), whose observed 1.64 pp offset is well inside the 1σ floor (−0.68σ from half)”. The 1.64 pp refers to |fvoid − 0.5|; this is correct but could be misread as the cross-class range. Everything else I checked is consistent (see audit below), but please ensure the “1.64 pp” phrase is explicitly labeled as “offset of the void class from parity” in the abstract to avoid misinterpretation.
- Required fix: Replace “whose observed 1.64 pp offset” with “whose observed void-class offset from parity |fCW − 0.5| = 1.64 pp”.

MINOR

P5-m1 (Arithmetic and consistency audit): All checked numbers consistent, but add a few explicit pointers
- Findings checked:
  - Table III σfrom half values recompute to −0.68, +0.55, −2.61, −4.66 exactly from the tabulated counts.
  - Cross-class range 1.98 pp: 0.5034 − 0.4836 = 0.0198.
  - Omnibus χ^2 = 3.55 (p = 0.31) on the 4×2 table is consistent with Appendix B counts; Cramér’s V = sqrt(4932/811,609) = 0.078 matches.
  - Density-quintile σpred = 2·(−0.0026)·√158,327 ≈ −2.07; residuals in Table IV consistent.
  - Phase-2 pLEE range 0.13–0.56, and max |σobs − σpred| ≤ 1.64 in resolved cells agrees with Table VII.
  - DESIVAST void vs non-void ∆fCW = +0.00067, SE = 0.00219, z = 0.31, p = 0.76, 95% CI [−0.0036, +0.0050] recompute exactly.
  - Catalog-native V2 contrasts (Sec. VIII.D) recompute to the reported z, p.
  - HEALPix σ bin residuals vs Paper IV monopole predictions (Sec. VIII.E) numerically consistent; Pearson r = +0.006 reported with p = 0.88 is coherent.
- Required fix: None, beyond the abstract phrasing in P5-M5. You may add short parenthetical “sanity” calculations to the Methods where you first introduce Eq. (1) to help readers reproduce σpred values.

P5-m2 (Clarity on Jeffreys intervals): Specify Jeffreys prior explicitly in figure captions that show CIs
- Problem: Some figures refer to “95% binomial CIs” without indicating Jeffreys prior, while the Methods commit to Jeffreys.
- Required fix: In captions for Figs. 3, 4, 5 explicitly state “95% Jeffreys binomial credible intervals” for consistency.

P5-m3 (Units and axis labeling): Ensure all figure axes include units where relevant
- Problem: In Fig. 1, the x-axis “DESI z” uses a unitless redshift; fine. In Figs. 6 and 8 HEALPix maps, include NSIDE value and note pixel area once in caption (you did at one place; standardize across figures).
- Required fix: Harmonize axis/caption unit notes across figures.

P5-m4 (Ambiguous shorthand): Define “pp” at first occurrence
- Problem: “pp” (percentage points) is used early without definition.
- Required fix: Define “pp ≡ percentage points” at the first use in the Abstract or Introduction.

P5-m5 (Over-precise p-value statement): “p ≪ 10−300 (log10 p ≈ −1069)”
- Problem: Over-precise. For readability, give “p < 10−300 (log10 p ≈ −1069)”.
- Required fix: Truncate to a sensible bound.

NITS

P5-n1 (Typography): Minor line-break artifacts around equations (e.g., “0.5
√
N”) appear due to typesetting.
- Fix: Reflow inline math to avoid awkward breaks.

P5-n2 (Redundant phrasing): A few duplicated descriptors (“primary robustness evidence … primary analysis”) can be tightened.
- Fix: Light copyedit for concision.

P5-n3 (Claims of novelty/scale): Statements like “largest matched-sample environmental-dependence test … to date” are plausible but unreferenced.
- Fix: Either add a reference supporting the scale claim or soften wording.

Methodology/derivation/dimensional audit highlights
- Eq. (1) σpred = 2·∆fCW·√N is dimensionless and consistent with the definition of σfrom half.
- Fourier-space conventions (Φ(k) = −δk/k^2; Tij = −kikj Φ ⇒ Tij = kikj δ/k^2) are internally consistent; classification is invariant to overall normalization for λth = 0.
- Grid and smoothing: 6634 h−1 Mpc box at 256^3 ⇒ 25.9 h−1 Mpc cell; mask dilation counts ceil(Rs/cell)+1 = 2 at Rs = 25, 3 at Rs = 50 are correct.
- Bonferroni thresholds: |σ| ≈ 3.09 for K = 5, α = 0.01 and ≈ 2.58 for K = 5, α = 0.05; |σ| ≈ 2.77 for K = 9, α = 0.05 are consistent with Gaussian quantiles. HEALPix K ≈ 1054 gives |σ| ≈ 4.05 (α = 0.05) plausible.
- Counting-floor for void (n = 428) is ±2.42 pp (1σ), matching the text.

Standalone-reader test
- After addressing P5-E2 and P5-E4 (removing reliance on unpublished Paper IV calibration and internal file paths), the paper will be self-contained: labels are available via public catalog; all sample counts and statistics are reproducible from the provided DR1 selections. As written, however, it still leans on Paper IV’s interpretation and embeds internal artifacts; please correct as specified.

Effect-size statements
- You do report Cramér’s V = 0.078 for the class×program contingency and explicitly state small effect despite huge n. Good. Maintain this practice for other omnibus χ^2 statements where relevant.

## Summary recommendation
MAJOR REVISIONS

The statistical methodology is careful, and my spot checks confirm the arithmetic and uncertainty accounting behind the headline nulls. However, the manuscript in its present form contains: (i) internal versioning metadata in the scientific text, (ii) extensive in-body dependence on an unpublished companion paper for a load-bearing calibration, (iii) confusing classifier nomenclature (V-Web vs T-Web), and (iv) pervasive inclusion of internal file paths that should be moved to a proper data-availability section. Addressing these issues, tightening the length, and providing a concrete archival DOI will make the paper suitable for PRD. The numerical conclusions themselves appear sound and robust once these presentation and independence issues are resolved.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P5-E7 (Abstract, p.1): Low‑z void count misstated
- Problem: “the V-Web void class at z ≲ 0.24 is sample-size limited at n = 428 chirality-relevant spirals …” contradicts §VIII A, which reports only n = 6 V‑Web “void” spirals at z ≤ 0.24 (0/6 inside any DESIVAST hole). The n = 428 figure is the full‑sample V‑Web void count across all redshifts, not the low‑z subset.
- Required fix: Correct the abstract to either (i) remove the “z ≲ 0.24” qualifier when citing n = 428, or (ii) state the actual low‑z overlap size (n = 6) and separately note that the full V‑Web void class has n = 428 across all z.

MAJOR

P5-M6 (Sec. VI.B, covariates paragraph, p.9): 100% covariate completeness claim conflicts with “edge‑on fraction” availability
- Problem: You state that the regression is “100% covariate-complete” on 783,741 galaxies while also noting that the Galaxy Zoo DESI “edge‑on fraction” is defined only “on the 152,455-galaxy featured subsample where the decision tree reaches the question.” These statements are inconsistent unless you imputed or excluded that variable.
- Required fix: Clarify precisely how the “edge‑on fraction” was handled for the majority of objects where it is undefined (e.g., variable dropped; imputed to NA with an indicator; analysis restricted). If imputation/indicator was used, report it and confirm that results are insensitive to excluding the edge‑on variable. If it was omitted from the joint model, say so explicitly and adjust the “100% covariate-complete” claim.

P5-M7 (Sec. VI vs Sec. IX.A, primary within T‑Web path): Canonical environment labels use a known selection‑contaminated δ definition
- Problem: The headline V‑Web/T‑Web environment table and Figure 3 are based on a global‑mean δ that you later show is selection‑contaminated and produces strong class migration. The z‑shell–corrected rebuild (§IX A) is the proper correction and yields an even tighter null.
- Required fix: Present the z‑shell–corrected T‑Web classification as the primary within‑T‑Web result in the Methods/Results, with the canonical (global‑mean) run demoted to a sensitivity check. State explicitly in the Methods that δ is selection‑corrected per shell for the primary labels, and move the global‑mean run to robustness.

P5-M8 (Throughout §VI–§VII figures/tables): Row‑level duplication vs unique‑galaxy independence
- Problem: Key class‑level displays (e.g., Fig. 3; Table III headline) and some σ values are computed on the 812,793 env‑labeled row‑level parent that includes 3.56% duplicate TARGETIDs. While you check homogeneity on the 783,820 unique‑galaxy subset, several other statistics (e.g., class‑level σ in captions/plots) remain shown only for the duplicated parent.
- Required fix: For every headline environment table/figure, present the unique‑TARGETID versions as primary (with row‑level shown as a secondary variant or in Supplement), and ensure all formal tests and σ values that assume i.i.d. are computed on unique galaxies (or adjust for clustering/duplication and state the method).

MINOR

P5-m6 (Sec. VIII A, p.17): Clopper–Pearson bound typeset error
- Problem: The one‑sided 95% CP upper bound for 0/6 successes is written “1 − 0.051/6 = 39%.” This looks like 0.05^1/6 but is missing parentheses and a caret.
- Required fix: Correct to 1 − 0.05^(1/6) ≈ 0.393 and show the exponent explicitly.

P5-m7 (Sec. VI.B redshift scan, p.9): Two different permutation p‑values reported without making the binning difference explicit
- Problem: You first report p = 0.372 for a redshift scan, then later say the “redshift‑quintile look‑elsewhere p” is 0.80 (free) / 0.81 (stratified). It is not clear to the reader that these are for different binning schemes (unspecified vs quintiles).
- Required fix: Clearly label the first test’s binning (e.g., fixed-width z bins used in Fig. 4) and explicitly distinguish it from the quintile test. Consider reporting both sets of p‑values side‑by‑side with binning definitions, or consolidate on a single pre‑declared binning.

P5-m8 (Notation/units, multiple places): Mixed “Mpc/h” vs “h−1 Mpc”
- Problem: The text alternates between “Mpc/h” and “h−1 Mpc.”
- Required fix: Standardize to one convention throughout (PRD typically uses h−1 Mpc).

P5-m9 (Sec. V Eq. (2), p.6): State the reference distribution explicitly
- Problem: The Bonferroni threshold formula uses erfc−1 without stating it is for a standard normal variate.
- Required fix: Add a short parenthetical (“z from N(0,1); two‑sided control”).

NITS

P5-n4 (Typographic precision, Sec. IX A, p.22): Window changes not always reiterated
- Problem: When citing class volume fractions in the selection‑weighted rebuild, you quote void fraction collapsing “from 17.6% to 0.75%,” which is a different redshift window than the canonical 24.4% cited earlier. This is correct but can confuse casual readers.
- Fix: Add a brief “(z < 0.5 window; canonical all‑z void fraction 24.4%)” note at first mention.

P5-n5 (RNG reuse across scans, Sec. V, p.6; §VI.E): Shared random streams
- Problem: You note that identical RNG streams are shared across families by a fixed seed, then show a separate re‑draw. While not wrong, this can couple nulls across families.
- Fix: Derive independent seeds per scan family from a master seed (documented) to avoid unintended cross‑scan coupling; note that results are unchanged.

Explanation for omissions: All other arithmetic, cross‑references, dimensional checks, and figure/body consistency I re‑audited match the displayed inputs or are already covered by the original report’s items. The new issues above focus on a low‑z void count error in the abstract, a covariate‑completeness contradiction, clarity/inference primacy for the selection‑corrected environment labels, unique‑galaxy independence for inferential σ, a typeset CP bound, and clearer labeling of redshift‑scan permutation tests.