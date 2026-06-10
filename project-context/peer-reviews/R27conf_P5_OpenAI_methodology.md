# P5 R27conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.58.pdf` md5=6ffcd714 pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5410 chars)
**Wall time**: 271.8s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three‑Algorithm Test …”

Scope of review
You asked for a methodology/statistics audit. I checked derivations, dimensional consistency, internal arithmetic, null procedures, look‑elsewhere handling, and whether every load‑bearing scalar in the abstract/conclusions is traceable to the body. I recomputed all numbers that can be reconstructed from the tables/figures/equations.

Overall assessment
The core methodology (binomial proportions by environment, permutation nulls, and multiple robustness checks) is sound and, numerically, most quoted values are internally consistent. However, there are several non‑negotiable issues for PRD: (i) explicit mathematical errors in the text, (ii) pervasive “earlier draft/withdrawn/commit path/seed” version‑history language inside the manuscript, (iii) post‑hoc designation of the “primary” analysis, and (iv) a few places where statistical quantities are mixed or not fully specified. These must be fixed before the paper can meet PRD standards. I list all findings below.

Findings

ESSENTIAL

P5‑E1 — §V (Statistics), p.6: Incorrect formula for standard error
- Offending text: “the Paper IV catalog-wide ∆fCW (N = 3.2 × 10^6, se ≈ 0.25/3.2 × 10^6 = 2.8 × 10−4) …”
- Problem: The binomial standard error at p≈0.5 is se = sqrt(0.25/N). The text drops the square root but still quotes the correct numerical value. 0.25/N = 7.8×10^-8, not 2.8×10^-4.
- Required fix: Replace with se = sqrt(0.25/N) ≈ 2.8×10^-4 and correct the preceding expression. Audit the same logic anywhere else the SE is propagated.

P5‑E2 — §VIII A (DESIVAST cross‑match), p.14–15: Wrong 0‑of‑n upper bound formula
- Offending text: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39% …”
- Problem: The formula is incorrect (and dimensionally nonsensical). The standard Clopper–Pearson upper 95% bound for 0 successes in n trials is 1 − α^(1/n) (with α=0.05), i.e., 1 − 0.05^(1/6) ≈ 0.393. The manuscript’s “1 − 0.051/6” is wrong arithmetic and wrong form.
- Required fix: Replace with the correct Clopper–Pearson expression and value; show the calculation.

P5‑E3 — Throughout (multiple pages): Version‑history/“earlier draft/withdrawn” and internal pipeline provenance in the body text
- Offending text (examples):
  - §V B, p.6–7: “pre‑registration caveat … we designate … post‑hoc”; 
  - §VI D, p.10: “An earlier draft quoted filament bright/dark n … and are withdrawn …”;
  - §VII, p.12–13: “An earlier draft quoted |σ| = 11.32 … withdrawn …”;
  - §VIII D, p.16: “An earlier draft reported nvoid = … these values reproduce only under a zone‑indexing defect … corrected join …”;
  - §IX B, p.21: “An earlier draft … is withdrawn …”;
  - Multiple sections: embedded filesystem paths, RNG seeds, commit tags, and “now been run”.
- Problem: PRD manuscripts must not contain internal revision logs, earlier‑draft commentary, file system paths, seeds, or artifact bookkeeping in the body. These belong in a data/code availability note or a supplementary reproducibility appendix, not in the scientific narrative. As written, the paper reads as a lab notebook rather than a journal article.
- Required fix: Remove all “earlier draft/withdrawn” commentary and pipeline path/seed chatter from the main text, consolidate reproducibility details into a short Data/Code Availability section or an ancillary file, and present only the final, audited numbers in the paper.

P5‑E4 — §V B (Primary vs secondary analysis), p.6: Post‑hoc choice of “primary” analysis
- Offending text: “Primary analysis path … The choice of which classifier to report as ‘primary’ is therefore made post‑hoc …”
- Problem: The paper designates its “primary” estimator after exploring many forks. PRD requires a clear, a priori definition of the load‑bearing estimator, or, absent preregistration, a correct multiplicity treatment across the tested families. As written, the headline is vulnerable to forking‑paths concerns.
- Required fix: Move the primary analysis definition to the Introduction, define it prospectively (not post‑hoc), and treat all other analyses as secondary. Alternatively, explicitly control family‑wise error across all tested classifier/stratification families (not just within‑family Bonferroni), or state plainly that the result is exploratory and adjust language in the abstract/conclusions accordingly.

P5‑E5 — Abstract and body (multiple places): Use of two different reference monopoles without always stating which is used
- Offending text: e.g., Abstract references the Paper IV monopole (∆fCW≈−0.0026) and later sections use the matched‑sample monopole fP5CW=0.4972 for residuals; not always restated at each juxtaposition with σfrom half.
- Problem: σfrom half and σvs‑monopole are not directly comparable, and different monopole references are used in different places. While the manuscript often warns about √N scaling, every place where a raw σ and a monopole‑referenced σ/residual appear side by side must state explicitly which baseline is used.
- Required fix: At every juxtaposition of σfrom half with σvs‑monopole, restate (i) which monopole is being used, and (ii) that the two σ’s are not directly comparable. Prefer a uniform convention: use the P5 matched‑sample monopole for residuals throughout the DESI analyses, and reserve the Paper IV value for context. Table/figure captions must carry this clarification.

P5‑E6 — §IX A (Completeness‑weighted rebuild), p.18–19: Insufficient quantitative specification of the weighted‑rebuild result
- Offending text: “per‑class fCW moves by only +0.05 pp (filament) and −0.03 pp (cluster) … −0.40 pp (wall), and +2.7 pp in the n≈430 void bin …”
- Problem: This paragraph introduces a materially different environment field (weighted by large random catalogs) and asserts the headline is unchanged, but does not provide per‑class n and fCW with uncertainties in a table (only deltas are given). For a load‑bearing robustness claim, PRD requires the actual numbers.
- Required fix: Add a table for the completeness‑weighted rebuild with per‑class n, fCW, σfrom half and σvs‑monopole, and the corresponding unweighted control over the same selection window.

MAJOR

P5‑M1 — §VI A/Table II, p.7: Homogeneity χ^2 test assumptions and duplicate handling
- Issue: The main χ^2 test is computed on a parent with 2.7% duplicate TARGETIDs. You do recompute on the unique‑TARGETID set; good. However, in the abstract you cite the 4×2 homogeneity null based on the row‑level parent without immediately qualifying that duplicates exist.
- Required fix: In the abstract and main text where the omnibus test is first stated, add “(reproduced on unique‑TARGETIDs with χ^2=3.00, p=0.39; duplicates do not affect the verdict)” to avoid implying all tests are i.i.d. on first reading.

P5‑M2 — §VII/Table VI, p.13: Multiple‑testing control across Phase‑2 sweep cells
- Issue: You control LEE within each cell (K=4 classes), but not across the nine cells. You later mention a “global max‑stat correction” pglobal=0.36 in a parenthetical. Given the sweep is a single robustness exercise, the across‑cell correction should be primary.
- Required fix: Promote the across‑cell max‑stat result to the main sentence in §VII (and summarize in the abstract only if space permits). Provide the simple Bonferroni‑9 bound alongside.

P5‑M3 — §IX B (Tempel FoF cross‑validation), p.21–22: Like‑for‑like definition and usable bins
- Issue: The main concordance statement is for the “filament‑like” bin (fine), but the text spends space on “isolated/void” and “small group/wall” where the V‑Web overlap n is 23 and 145, respectively — these are effectively meaningless comparisons and could be misread.
- Required fix: Move the low‑n pairs to a brief footnote or explicitly label them “non‑informative at these n; reported for completeness only.”

P5‑M4 — §VIII/E. Table IX, p.16–17: “No‑voids” sky‑region proxy vs actual footprint
- Issue: You use “maximal voids per pixel = 0” as a proxy for being outside DESIVAST coverage. This is reasonable but imperfect.
- Required fix: Provide a simple angular footprint mask overlay (or cite the released mask) and repeat Table IX using the explicit in‑footprint vs out‑of‑footprint split, or, at minimum, quantify the contamination fraction of in‑footprint pixels in the “0‑voids” bin.

P5‑M5 — Appendix A, p.26: Toy EFT operator (relevance/placement)
- Issue: The toy operator is explicitly non‑covariant and acknowledged to be schematic. It is not used anywhere in the analysis. As such, it distracts from a methods paper and invites misinterpretation.
- Required fix: Move Appendix A to ancillary material, or reduce it to a two‑sentence qualitative remark in the Discussion with no equations.

P5‑M6 — §IV A/Step 5, p.4–5: Mask construction and dilation choice
- Issue: The mask is built by binary dilation with a chosen structuring element and iterations. You later provide a variant (“cube‑connected 3‑iteration dilation”) with small shifts. This is important because mask geometry affects void purity.
- Required fix: Summarize (in the main text) the quantitative effect of varying the dilation scheme on per‑class n and fCW in a compact table (currently buried in a parenthetical). This keeps the boundary‑condition sensitivity fully visible.

MINOR

P5‑m1 — Abstract vs §III B, p.1 and p.3: DR1 “16.4×10^6” vs “16,361,731”
- Issue: Abstract rounds to 16.4M; body uses 16,361,731 after cuts. Acceptable, but add “(16.36M after quality cuts)” in the abstract to avoid the impression of two different parent counts.

P5‑m2 — §IV A Step 2, p.4: Unit conversion wording
- Issue: “astropy returns χ in Mpc and we multiply by h explicitly to work in h−1 Mpc” is easy to misread.
- Required fix: Rephrase to “we convert χ [Mpc] to χ [h−1 Mpc] via χh−1Mpc = h × χMpc (Planck‑2018 h = 0.6766); χ(z=0.2)=570.4 h−1 Mpc.” Optionally, cite the exact astropy cosmology used.

P5‑m3 — §V A, p.6: Bonferroni formula
- Issue: Eq. (2) is correct for a two‑sided Gaussian tail; state explicitly that the formula corresponds to a two‑sided family‑wise α (so readers don’t need to infer the factor of 2).

P5‑m4 — §VI B, p.8: Logistic regression specification
- Issue: The regression includes “confidence” (a classifier property). It would help to state explicitly whether this is the same score used to define the equivariant labels, and whether including it meaningfully alters environment coefficients (you mention p≈0.02 but not the effect size).
- Required fix: Add the estimated coefficient and its sign for “confidence,” or drop it from the summary.

P5‑m5 — §VII, Fig. 7 caption, p.14: “pp” units
- Issue: The caption uses “pp” without restating “percentage points.”
- Required fix: Expand “pp = percentage points” in the first figure where it appears.

P5‑m6 — §VIII B/Table VII, p.15: Round‑off consistency
- Issue: For the DESIVAST void vs non‑void split, fCW values are reported to four decimals elsewhere and to four here; σfrom half is reported to two decimals. Consider consistent significant figures across all tables (e.g., three decimals on fCW, two on σ).
- Required fix: Harmonize significant figures across tables.

P5‑m7 — §XI/Table XIII, p.24: “backup + other”
- Issue: Very small n=1,093; quoting fCW=0.5105 to four decimals overstates precision.
- Required fix: Reduce to two decimals or quote with 95% CI.

NIT

P5‑n1 — Minor typos
- §VI D, p.10: “marginally exceeds the Bonferroni‑4 |σ| = 3.02 threshold at α = 0.01” — use “threshold” once.
- §IX C, p.22: “preprint (2026)” vs “in submission to MNRAS” — unify phrasing across [11], [12] citations.

P5‑n2 — Repetitive phrasing
- The phrase “dominates by the counting noise of the small void bin” appears multiple times nearly verbatim. Vary wording or consolidate.

P5‑n3 — Over‑long manuscript for the claimed contribution
- At 27 pages, the paper is long for a null‑result methods study. Many pipeline details and internal audits can move to an ancillary reproducibility note.

Audit of abstract and conclusion numbers

- 16.4×10^6 ZWARN=0 rows: §III B gives 16,361,731 — consistent rounding.
- 14,622,283 galaxies used for V‑Web: §III B — exact match.
- 2,232,212 unique matches; 791,635 chirality‑relevant: Table I — exact match.
- Per‑class fCW in canonical run and σfrom half values: Table II — exact match. Recomputed σ’s match to rounding.
- “Range 1.98 pp” across classes: 0.5034–0.4836=0.0198 — correct.
- 4×2 χ^2 = 3.55 (p=0.31): Not recomputable from the paper alone but plausible given counts; the duplicate‑free recomputation is reported (χ^2=3.00, p=0.39).
- Phase‑2 sweep: per‑cell range 1.7–4.1 pp; max residual 1.87σ; pLEE 0.13–0.56: Table VI supports these statements.
- Void‑bin “±4.8 pp (2σ)” at n=428: 2×sqrt(0.25/428)=0.0483 — correct.
- DESIVAST void re‑projection: nvoid=56,981; fvoid=0.4964 vs non‑void 0.4971; Δ=0.0007 — Table VII — consistent; σ’s recompute to −1.71 and −4.59.
- DESIVAST three‑algorithm robustness: Table VIII — |ΔfCW| ≤ 0.0019 — as stated.

Other statistical checks

- Use of Jeffreys intervals (Beta(1/2,1/2)) is fine and stated.
- Distinction between σfrom half and σvs‑monopole is made several times; however, see ESSENTIAL P5‑E5 on making it explicit at every juxtaposition.
- NMC=1000 gives Monte Carlo SE ~0.01–0.02; the paper reports p with two/three decimals and explicitly states MC SE — acceptable.

Length/restructuring recommendation
- The paper is longer than necessary for the central result. I recommend a maximum of 12–15 pages for the main text: move code paths, seeds, and “closure‑wave recomputes” to a reproducibility supplement; remove all earlier‑draft commentary.

## Summary recommendation
MAJOR REVISIONS

The central analysis is careful and the numbers are largely internally consistent, but there are explicit mathematical errors (P5‑E1, P5‑E2), extensive version‑history language that must be removed, a post‑hoc “primary” designation that needs to be made prospective or properly multiplicity‑controlled, and a few robustness claims that need full tabulation. Addressing these issues will bring the manuscript up to PRD standards for clarity, rigor, and presentation.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second‑pass audit)

ESSENTIAL

P5‑E7 — §V (Statistics), p.6: Inconsistent N in σpred uncertainty propagation
- Offending text: “where the matched‑sample monopole fP5CW is the reference (N = 812,793, se ≈ 5.5×10−4), it is ≈ 0.7.”
- Problem: The formula quoted just above is σpred,SE ≈ 2·se·√N. Plugging N = 812,793 and se = 5.5×10−4 gives 2·5.5×10−4·√812,793 ≈ 0.99, not 0.7. The value 0.7 corresponds to N ≈ 4×10^5, i.e., the per‑class size, not the stated N = 812,793.
- Required fix: Either state explicitly that the 0.7 is computed at N ≈ 4×10^5 (class‑size), or recompute for N = 812,793 (≈ 0.99). Be consistent about which N is used in each uncertainty example.

P5‑E8 — §VI D/Table IV, p.9–10: Density covariate definition vs numbers inconsistent
- Offending text: Table IV caption defines ρ̄ as “the quartile mean of log10(1+δsmooth)”, but the reported means are 1.55–2.21 (cluster) and 0.90–1.86 (filament).
- Problem: log10(1+δ) at LSS smoothing scales is O(0.0–0.5). Values ≳1 imply 1+δ ≳ 10–160, which is implausible for a 25 Mpc/h Gaussian field and contradicts the monotone/log statement. The numbers are consistent with linear (1+δ) means, not log10.
- Required fix: Correct the label (if the linear density was used) or correct the numbers (if the log variable was used). State unambiguously whether quartiling and means are on linear (1+δ) or log10(1+δ); ensure the table entries match.

P5‑E9 — Eq. (1), p.6: Ambiguous algebra (missing parentheses)
- Offending text: “σpred = ∆fCW 0.5/√N = 2·∆fCW·√N”.
- Problem: As written, “∆fCW 0.5/√N” is ambiguous and suggests divide by both 0.5 and √N, which is not algebraically equivalent to 2∆fCW√N. The intended formula is σpred = (∆fCW/0.5)·√N.
- Required fix: Add parentheses: σpred = (∆fCW/0.5)·√N = 2∆fCW√N, and ensure this is the only form used.

MAJOR

P5‑M7 — §E (Sky position) and Table V, p.11: No global LEE across NSIDE scans
- Issue: Three HEALPix scans (NSIDE 16/32/64) are each tested with a within‑scan max‑stat permutation p, but no correction is applied across the three NSIDEs. While each p≫0.05 here, PRD typically expects either a single pre‑specified NSIDE or an across‑NSIDE max‑stat correction.
- Required fix: Report an across‑NSIDE max‑stat permutation p (single stream shuffling labels once and evaluating all three NSIDEs per draw), or justify a priori the single NSIDE of record.

P5‑M8 — §IX A (Selection‑corrected rebuild), p.18–19: Referenced “per‑shell table” missing
- Offending text: “The per‑shell table below … quantifies the correction at the cell level.”
- Problem: No per‑shell table is present in the manuscript; only a repository path is cited. This prevents readers from verifying the shell statistics claimed in the text.
- Required fix: Include the per‑shell summary table (shell z‑range, in‑mask mean δ before/after correction, number of galaxies per shell), or remove the forward reference and move the quantitative claim to a table.

P5‑M9 — Abstract/§VIII B, novelty claim: “largest matched‑sample environmental‑dependence test … in DESI DR1”
- Issue: The claim is plausible, but no quantitative comparison to prior DESI‑based chirality–environment tests is given.
- Required fix: Add a one‑sentence justification with specific comparator sample sizes (or soften to “to our knowledge, among the largest…”, or drop).

MINOR

P5‑m8 — §X/Table XII, p.23: Very small bins appear in “V‑Web on same overlap”
- Issue: The V‑Web overlap row includes void/wall bins with n = 1 and n = 2 but still reports a class range and max |σ| for the four‑class set (even though you state “filtered to classes with n ≥ 100” in the caption).
- Required fix: Either exclude these bins from the reported class range/max |σ| or footnote that the range/max is computed over classes with n ≥ 100 only (and list which classes meet the cut).

P5‑m9 — Terminology consistency, §IX C vs elsewhere: “cluster” vs “knot”
- Issue: The tidal‑tensor high‑density class is variously called “cluster” (V‑Web) and “knot” (T‑Web literature) with occasional mixing in comparative text.
- Required fix: Add a one‑line note early in §IV or §IX C that “cluster (this work) corresponds to knot in T‑Web nomenclature,” and use one term consistently in the narrative with the other in parentheses when first introduced.

P5‑m10 — Units consistency for distances, multiple sections
- Issue: Both “Mpc/h” and “h−1 Mpc” are used interchangeably across sections and figure captions.
- Required fix: Pick one convention (prefer h−1 Mpc for comoving lengths) and use it consistently in text and captions.

NIT

P5‑n4 — Eq./text hygiene
- Minor algebra/notation clean‑ups would improve readability: explicitly write σpred = (∆fCW/0.5)√N (see P5‑E9), avoid chained divisions without parentheses, and ensure every appearance of “pp” expands to “percentage points” on first use in each figure/table caption family (even though you already do this in some places).

Explanation
The initial review did not re‑derive the σpred‑uncertainty example against the stated N (P5‑E7), did not notice the log10 vs linear density inconsistency in Table IV (P5‑E8), and did not flag the missing per‑shell table (P5‑M8) or the lack of an across‑NSIDE max‑stat correction (P5‑M7). The algebraic ambiguity in Eq. (1) (P5‑E9) and a few presentation/consistency items (P5‑m8–m10, P5‑n4) also surfaced only on this pass. All other earlier checks remain valid.