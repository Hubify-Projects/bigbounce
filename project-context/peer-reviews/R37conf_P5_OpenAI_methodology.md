# P5 R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.72.pdf` md5=544b6af2 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6634 chars)
**Wall time**: 422.4s

---

Referee report (methodology/statistics): P5 — Environmental Dependence of Spiral Chirality

Scope of review
- Focus: statistical methodology, derivations, dimensional analyses, internal arithmetic, null procedures, multiple-testing control, and whether the abstract/conclusions are fully supported by the body.
- I read all 32 pages, all tables/figures, and audited the load‑bearing numbers and equations where feasible from the in‑paper data.

Overall assessment
- The central estimand is clear: environment-conditioned differences in fCW. The primary test (DESIVAST-anchored void vs non‑void contrast) is well defined and the two-sample statistics are simple to audit; the reported numbers check out.
- Multiple-testing and “look-elsewhere” control is handled reasonably (Bonferroni and empirical max-stat label-shuffle). NMC=1000 is adequate for the coarse p-value bands actually quoted.
- However, the manuscript contains numerous instances of internal version-history prose (“earlier draft… withdrawn… superseded…”) and inline file-path provenance throughout the narrative that are not PRD style; these must be removed or moved to a dedicated data availability section/supplement.
- The paper relies load‑bearingly on a non–peer-reviewed “companion Paper IV” for both the chirality labels and the catalog-monopole estimate, and repeatedly quotes Paper IV results as inputs. For PRD, the present manuscript must be self‑contained to the extent required to evaluate the validity of the labels and the monopole propagation without needing to consult an unpublished companion.
- Nomenclature is confusing: the paper implements the Hahn (2007) tidal-tensor “T‑Web” but repeatedly calls it “V‑Web,” while also acknowledging the velocity-shear “V‑Web” is a different classifier. This should be standardized to avoid confusion.

Findings (with required fixes)

ESSENTIAL

P5-E1 (pp. 7, 12, 15, 18, 24; multiple locations) — Version-history/editorial prose in the body
- Problem: Numerous sentences report “An earlier draft quoted…,” “those values are withdrawn…,” “an earlier version…,” “exact reproduction of the earlier numbers under the defect,” etc. Examples:
  - p. 12: “An earlier draft quoted filament bright/dark n… and are withdrawn…”
  - p. 15: “An earlier draft of this table reported per-cell ranges… withdrawn…”
  - p. 18: “An earlier draft reported nvoid = 86,276 / 64,514…”
  - p. 24: “An earlier draft compared the Tempel overlap…”
- Required fix: Remove all version-history and review-log language from the main text. Replace with a clean, single-source-of-truth narrative. If necessary, move provenance notes to a compact Reproducibility/Release Notes appendix or the data repository README, not the paper.

P5-E2 (Abstract; pp. 2–3; §II; passim) — Load-bearing reliance on an unpublished “Paper IV”
- Problem: The chirality labels and the catalog-wide monopole value ΔfCW = −0.0026 (and its uncertainty) are taken from a companion manuscript “in preparation and not yet peer-reviewed.” Multiple core inferences here (e.g., σpred in Eq. 1, σvs monopole residuals, robustness interpretations) depend on that external estimate. PRD requires the present argument to stand on its own.
- Required fix: Make this paper self-contained with respect to the classification input. At minimum:
  - Include a concise technical appendix summarizing the classifier used to generate labels (architecture, training data/augmentation, class definition, label QA; the “equivariant ViT‑Small with Z2 TTA” line is not sufficient).
  - Re‑estimate the catalog monopole on the subset actually used here (e.g., the 812,793 env‑labeled rows and the 791,635 unique chirality‑relevant matched spirals) within this paper, report its uncertainty, and propagate it into σpred. Do not require the reader to accept Paper IV to evaluate key null predictions.
  - Alternatively, cite a stable, citable preprint (arXiv) with an invariant version and mirror the minimal derivations/data in this paper, so the methodology does not hinge on a non‑archived “in preparation” document.

P5-E3 (Title; pp. 1, 4–8; footnote a) — Misleading classifier nomenclature (“V‑Web” vs “T‑Web”)
- Problem: The implementation is the tidal-tensor (Hahn 2007) classifier, commonly called “T‑Web,” but the term “V‑Web” is used throughout (with a footnote that acknowledges the velocity-shear V‑Web is different). This is likely to confuse readers, especially because the paper simultaneously cites Hoffman et al. (2012) (the true V‑Web).
- Required fix: Standardize terminology. Use “T‑Web (Hahn 2007 tidal‑tensor)” consistently throughout text/figures/tables, and reserve “V‑Web” for velocity‑shear. If you insist on legacy “V‑Web” usage, state once, very early, that you will call it “T‑Web,” and then do so uniformly thereafter, including in figure/table captions and the abstract.

P5-E4 (pp. 17; §VIII.A) — Overstatement from an n=6 purity check
- Problem: “0/6 V‑Web ‘void’ spirals fall inside any … DESIVAST … holes… this … quantifies the V‑Web void-class purity…” With n=6 this does not “quantify” anything; you later acknowledge the sample is too small for a formal constraint, but the preceding wording is too strong.
- Required fix: Rephrase to “illustrates but does not quantify,” remove any language suggesting it constrains purity. Provide only the one‑sided 95% binomial bound (which you already do), and ensure the narrative does not imply more than that bound.

P5-E5 (pp. 31; Appendix B; Table XVI) — Homogeneity χ2 must be recomputed on the exact table and reported consistently
- Problem: The main text reports χ2 = 3.55 (p = 0.31) on the 812,793-row parent and χ2 = 3.00 (p = 0.39) on the 783,820 unique TARGETIDs. Appendix B Table XVI provides the explicit 4×2 counts. That integer table must exactly regenerate the χ2 = 3.55 claim.
- Required fix: Confirm and state explicitly that running a Pearson χ2 on Table XVI with a common-proportion null reproduces 3.55 (3 d.o.f.). Add a sentence with this round-trip confirmation, or correct the reported χ2/p if any rounding of the per-class nCW was applied before forming Table XVI.

MAJOR

P5-M1 (pp. 4–29; passim) — Extensive inline file-paths and repository internals in the narrative
- Problem: The text is peppered with internal file paths (“pipelines/p5_desi_chirality/outputs/…json”), config names, and local artifacts. This is not PRD style and distracts from the scientific narrative.
- Required fix: Move all file-path provenance to a concise Data/Code Availability section or Supplemental Material. In the body, refer to “Supplementary Fig./Table X” or “Data release DOI Y” rather than in‑repo paths. Ensure a single DOI-archived bundle covers every artifact you cite.

P5-M2 (pp. 22–23; §IX.A) — Completeness-weighted rebuild: missing normalization definition
- Problem: You define δw = ng/(α nr) − 1 and state “BGS_BRlGHT clustering randoms” with α scaling but do not define α (ratio of totals? per-shell normalization? mask‑restricted?). This impedes reproducibility and evaluation of the selection-weighted stress test.
- Required fix: Specify α precisely (e.g., α = Σcells ng / Σcells nr over the randoms‑supported mask within the z‑window), and state the randoms catalog used (version, number of points, whether FKP or not) and how cells without randoms are treated. Provide the numeric α used.

P5-M3 (pp. 6–7; Eq. 2; Table VI) — Bonferroni threshold formula and examples
- Problem: You define |σ|Bonf = √2 erfc−1(α/K), which is correct for two-sided Gaussian tails; however, your worked example for K = 1054, α = 0.05 gives 4.05, whereas Φ−1(1 − 0.05/(2·1054)) ≈ 4.24. The mismatch is not used for acceptance decisions (you use empirical max-stat), but clarity is needed.
- Required fix: Either (i) replace Eq. (2) with the simpler z = Φ−1(1 − α/(2K)) and recompute the stated numeric thresholds; or (ii) keep Eq. (2) and correct the worked examples to match it. State explicitly that you use empirical max-stat pLEE as primary, with Bonferroni only as a cross‑check.

P5-M4 (pp. 1, 30; title block and Reproducibility Checklist) — Version tags in the paper
- Problem: Title page contains “(Dated: June 2026 — v0.1.72-2026-06-13)” and the checklist repeats internal tags/seed. PRD articles should not show internal version strings.
- Required fix: Remove code-style tags from the title page. If you want to timestamp data/code, do it in the Data Availability paragraph (with DOI and commit hash), not in the scientific narrative or title block.

P5-M5 (pp. 14–16; Table VII narrative) — “Range vs. counting floor” argument is descriptive, not a calibrated test
- Problem: You compare the per-cell range of class fractions to the void-bin 2σ floor as evidence the spread is dominated by counting noise. While intuitive, a range is not directly comparable to a single-bin 2σ unless formally justified.
- Required fix: Retain the range as descriptive, but emphasize that significance control comes from the per-class σobs − σpred residuals and the empirical max-stat permutation pLEE (which you already provide). Adjust wording to avoid implying a formal bound is established by the 2σ void floor.

P5-M6 (pp. 7–13; Figs 3, 5, 6 captions; Table III caption) — Keep σfrom half vs σvs monopole distinctions explicit wherever they are juxtaposed
- Problem: You are mostly careful, but in a few places σ values from different nulls appear in proximity without a reiteration of non-comparability across different N. For PRD clarity, this should be explicit every time σfrom half across rows/classes is presented.
- Required fix: In every figure/table caption that lists σfrom half across multiple classes/bins, add the explicit sentence: “σfrom half scales as √N at fixed fractional offset and is not comparable across rows; inference uses either σvs monopole residuals or empirical permutation p-values.” You already do this in Table III; propagate uniformly.

P5-M7 (pp. 24–26; §IX.B; Fig. 9) — Tempel cross-validation accounting
- Problem: The like-for-like comparison is ultimately done on the overlap; earlier drafts/wording could be read as comparing disjoint populations. The current wording is better, but add one line explicitly stating that the V‑Web panel at left is the full-sample reference and that the concordance statistic is computed on the 96,753‑spiral overlap only.
- Required fix: Clarify in Fig. 9 caption and §IX.B that the 0.29 pp filament‑like concordance is computed on the overlap subsets only, and that the left V‑Web panel is shown only as a visual reference for the full sample.

MINOR

P5-m1 (pp. 6–7; Eq. 1 discussion) — Propagation of monopole uncertainty
- Comment: You correctly quantify the induced uncertainty on σpred (≈ 0.36–0.7 depending on parent). In a few places you interpret residuals of order 1–2σ without restating that band. Add a parenthetical reminder where you cite the 1.64σ maximum residual.
- Fix: Add “(recall σpred uncertainty ≈ 0.4–0.7 on these Ns)” where residuals ~1–2σ are interpreted.

P5-m2 (pp. 20; Table XI; §VIII.E) — “0 maximal voids per pixel” as a coverage proxy
- Comment: You eventually provide a proper footprint-restricted control using the union of hole discs. Good. Up‑front in §VIII.E note that the 0‑void bin is an imperfect proxy and that the robust control is the explicit footprint re-tabulation reported later in the section.
- Fix: One sentence early in §VIII.E pointing to the later footprint-restricted analysis as the formal control.

P5-m3 (pp. 10; Table IV caption) — Make explicit whether σpred uses Paper IV or the in‑paper matched-sample monopole
- Fix: Add “using ΔfCW from Paper IV” in the first sentence to keep consistency with §V.

P5-m4 (pp. 11; Fig. 5 right panel) — Axis annotation
- Fix: Label the y‑axis “σfrom half” and add a legend item “Paper IV monopole prediction σpred” to make the overlay self‑contained.

P5-m5 (pp. 22; Fig. 8 bottom) — Color bar label
- Fix: Add “σfrom half” (units) to the color bar; indicate that σ is computed per‑pixel against 0.5.

P5-m6 (pp. 28; Table XV) — Consistency check of totals
- Comment: North + South + DES-only count equals 791,635 (good). Because the program split rows omit DES-only explicitly, add a note that the “program” split is orthogonal to the “footprint” split and that totals need not sum across different stratifications.
- Fix: Add a one‑line note to Table XV caption.

P5-m7 (pp. 25–27; Table XIV) — n for V‑Web on the overlap
- Fix: Add the total Noverlap = 25,186 in the table caption to make the context explicit.

P5-m8 (pp. 1; title line) — Remove internal version/date string
- Fix: Delete “— v0.1.72-2026-06-13.”

NITS

P5-n1 (pp. 9) — Typography: “−0.68σfrom half” lacks a space
- Fix: Insert thin space: “−0.68 σ from half” or keep your consistent “σfrom half” token but avoid fusing with numerals.

P5-n2 (pp. 4; Table I) — Units
- Fix: Add units to “p50 separation” and “p99 separation” column headers (arcsec).

P5-n3 (pp. 6; Eq. 2) — Cite the mapping to normal tail
- Fix: Add “This corresponds to z = Φ−1(1 − α/(2K)) under a two‑sided normal tail” for readers unfamiliar with erfc.

P5-n4 (pp. 5; Fig. 2) — Caption clarity
- Fix: Spell out that fractions are by volume of in‑footprint cells, not by number of galaxies.

P5-n5 (pp. 23; “cube-connected 3-iteration dilation variant”) — Define connectivity
- Fix: Replace “cube-connected” with “26‑connected structuring element” (if that is what you used) or define precisely.

Arithmetic and consistency audits (selected)

- Table III: All fCW and σfrom half recompute from the listed counts. Range 1.98 pp = 0.5034 − 0.4836 checks.
- Eq. (1): Dimensionally correct; numeric σpred examples check for N ≈ 4 × 10^5 (≈ −3.3σ for ΔfCW = −0.0026).
- Density‑quintile example: σpred = 2×0.0026×√158,327 ≈ 2.07; residual 3.94 − 2.07 = 1.87 < 3.09 (Bonferroni-5 at α=0.01); checks.
- DESIVAST primary contrast (Table VIII): ∆fCW = 0.00067; SE(∆) = 0.00219 from 0.5·√(1/56981+1/621964); z = 0.31; p = 0.76; 95% CI [−0.0036, +0.0050]; all match recomputation.
- Three‑algorithm DESIVAST (Table X): REVOLVER SE(∆) ≈ 0.00169 (matches 0.0017), z ≈ −1.12 (p ≈ 0.26); VIDE SE(∆) ≈ 0.00195, z ≈ −0.05 (p ≈ 0.96); checks.
- σvs monopole (Table XII): residuals computed as 2 (fclass − fP5) √Nclass; filament residual ≈ +1.0; cluster ≈ −1.1; check.
- HEALPix scan: Max |σ|obs at NSIDE 32 is 4.13; null |σ|max,p99 = 4.78; p = 0.135; consistent with NMC = 1000 sampling noise (±0.015).

Length and focus
- At 32 pages, the manuscript is overly long for a single (important but negative) result. The core result (DESIVAST primary + T‑Web cross‑checks + a compact systematics section) could be presented in ~18–20 pages. I recommend moving pipeline remakes, randoms‑weighted stress tests, and per-pixel maps to Supplementary Material, keeping only the essential summary statistics and the main tables/figures in the body.

Standalone-reader test
- Without Paper IV in hand, the reader has enough to re‑compute every in‑paper statistic that depends only on the chirality labels. However, because the global monopole propagation is a key interpretive scaffold, the present paper must either re‑derive it on its own matched sample or include an appendix with the estimator, number, and uncertainty. Otherwise, the foundation of σpred and σvs monopole is opaque.

Effect sizes
- Where you provide massive χ2 values (e.g., class × program χ2 = 4932), you also give Cramér’s V = 0.078. Good. Keep this practice consistently for any large‑n χ2 statistics.

Abstract-last drift sweep (pattern‑045)
- I re‑checked every load‑bearing abstract number; all major figures (N’s, fCW per class, σ’s, ranges, p-values, and DESIVAST contrasts) are traceable in the body and numerically consistent.
- The only overstatement is the phrasing around the 0/6 V‑Web vs DESIVAST void purity check; fix per P5‑E4.

Data/code availability (patterns 046/047)
- You promise a DOI‑minted archival snapshot of the code/data directory. Ensure the DOI and an explicit commit hash are present in the final submission (they are not in the current PDF). Remove internal seed/version tags from the body.

Uncomputed quantitative claims (pattern‑048)
- Claims such as “the range collapse by a factor ∼40” (z‑shell corrected rebuild) should be accompanied by the numeric before/after values (you do: 1.98 pp to 0.05 pp). Keep that practice throughout. Where you use terms like “dominated by survey‑edge artifacts,” you subsequently quantify them; good.

## Summary recommendation
MAJOR REVISIONS

The core statistical methodology and the primary DESIVAST‑anchored estimand are sound, and the principal numbers check out. However, the manuscript in its current form does not meet PRD presentation standards: it contains extensive version‑history language in the body, relies load‑bearingly on an unpublished companion for essential inputs, uses confusing “V‑Web” nomenclature for a T‑Web implementation, and embeds too much repository‑internal detail in the narrative. Addressing the ESSENTIAL and MAJOR items above will produce a clean, self‑contained PRD‑level paper.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS AFTER SECOND PASS

P5-E6 (pp. 10–11; Table V and surrounding text) — Density covariate labeling/unit inconsistency
- Problem: The caption states “Quartiles binned by the V‑Web per-galaxy log-density covariate … ρ̄ is the quartile mean of log10(1+δsmooth).” But the quoted ρ̄ values (e.g., 1.55, 1.80, 2.01, 2.21 for “cluster” quartiles; 0.90–1.86 for “filament”) are only physically plausible as linear densities (1+δ), not as log10(1+δ): log10(1+δ)=1.55 would imply 1+δ≈35, far too large at Rs=25 Mpc/h. The narrative also compares ρ̄ numerically across classes (“cluster Q1 1.55 vs filament Q4 1.86”), which only makes sense for linear densities.
- Required fix: Clarify precisely: (i) the binning variable (log10(1+δsmooth) vs linear 1+δsmooth); (ii) which quantity’s mean is reported in ρ̄ (it appears to be the linear 1+δsmooth). If you binned on log10 but report linear means, say so explicitly and correct the caption.

P5-M8 (pp. 17–20; §VIII.B/E; Table VIII) — Two different DESIVAST membership definitions are interleaved without a single canonical choice
- Problem: The primary DESIVAST void/non‑void contrast in Table VIII uses a k=20 KDTree sphere-membership approximation (nvoid=56,981), while later sections use the exact k‑unbounded membership (nvoid=57,081; and the non‑void count drops to 621,864). Although you state the difference is only +100 objects (0.18%), these mixed denominators appear in different places and can confuse readers.
- Required fix: Adopt a single, exact (k‑unbounded) membership definition as the canonical DESIVAST result everywhere (tables, text, abstract numbers if affected), and confine the k=20 result to a brief robustness note. Where footprint-restricted controls use the exact build, state that the different n arise solely from exact membership.

P5-M9 (pp. 6–8; §V–§VI; passim) — Family-wise error control level α alternates without a unifying statement
- Problem: Some multi-bin families are controlled at α=0.01 (density quintiles), others at α=0.05 (Bonferroni‑5 DESIVAST family, Bonferroni‑4 quartiles). The choices are sensible but not summarized, which makes it hard to follow the logic across families.
- Required fix: Add a concise table or paragraph listing each family (K, bins) and the α used, with rationale (e.g., primary family α=0.05; descriptive scans α=0.01). Ensure captions and in‑text thresholds consistently reference that table.

P5-m9 (pp. 10–12; quartile/HEALPix thresholds) — Bonferroni numeric thresholds inconsistent for small K
- Problem: For K=4, α=0.05, you quote |σ|=2.50 in §VI.D; the two-sided Gaussian Bonferroni threshold is Φ−1(1−0.05/(2·4))≈2.47 (or equivalently √2 erfc−1(0.05/4)≈2.47). This is minor, but similar to your earlier K=1054 mismatch already flagged; keep all examples numerically consistent with the adopted formula.
- Required fix: Recompute and harmonize the printed Bonferroni examples (K=4, α=0.05 → 2.47; K=4, α=0.01 → 2.99–3.00), and reiterate that empirical max‑stat pLEE is primary.

P5-m10 (p. 15; §VII.A) — Over-strong “equivalence” between range and void-bin σ
- Problem: The text asserts that the inter-class range “is therefore” dominated by the void bin, “equivalently, the void bin’s own deviation … satisfies |σvoid| ≤ 1.35 in all nine cells.” A small |σvoid| does not by itself bound the four-class range; the empirical pLEE and per-class σobs−σpred already provide the calibrated control.
- Required fix: Rephrase as descriptive (e.g., “the extreme class setting the range is always void, and its own |σ| ≤ 1.35”), not as a logical equivalence or formal bound.

P5-m11 (p. 17; §VIII.A) — Clopper–Pearson exponent printed ambiguously
- Problem: The one-sided 95% upper bound is written as “1 − 0.051/6 = 39%,” which reads as a division; the intended form is 1 − 0.05^(1/6). The next phrase (“1−α^(1/n)”) suggests the exponent, but the numeric line can be misread.
- Required fix: Typeset the exponent explicitly (1 − 0.05^{1/6} ≈ 0.393), matching the verbal formula.

P5-m12 (pp. 5 and 23; §IV.A step 5 vs §IX.A) — Minor stale count of in-mask grid cells
- Problem: You quote 3,150,086 in‑mask cells in §IV.A and 3,150,089 in §IX.A. The 3‑cell discrepancy is trivial but avoidable drift.
- Required fix: Reconcile and use a single value for the canonical build, or note that the second figure refers to a rebuild with slightly different mask logic.

P5-m13 (Appendix C; title block echoed) — Internal version tags persist in the appendix
- Problem: Even if you remove code-style tags from the title block (already flagged), the appendix still states “manuscript tag v0.1.72‑2026‑06‑13.”
- Required fix: Move code/seed/commit tags to the Data/Code Availability paragraph or Supplementary Material with a DOI and commit hash. Remove internal tags from the scientific PDF.

P5-m14 (pp. 18; “largest matched-sample … to our knowledge”) — Unsubstantiated novelty claim
- Problem: The claim that this is “the largest matched-sample environmental-dependence test … to date” is plausible but unreferenced.
- Required fix: Either provide a brief comparative citation/scope statement (e.g., list n for the closest prior works) or soften to “a large matched-sample …” without the priority claim.

P5-m15 (pp. 10; Table IV caption) — Provenance of σpred
- Problem: The caption does not explicitly say that σpred uses ΔfCW from Paper IV (while §V does).
- Required fix: Add “σpred computed using ΔfCW from Paper IV” to the caption to make the overlay self-contained.

P5-n6 (pp. 10–11; Table V caption/body) — Clarify the “monotone transform” remark
- Problem: You correctly note quartile membership is identical under log vs linear density. Given the unit confusion above (P5‑E6), a short parenthetical (“binned on log10(1+δ), reported means are linear 1+δ”) would prevent misreadings.
- Fix: Add that parenthetical to Table V caption.

P5-n7 (pp. 22; Fig. 8 bottom) — Label both the method and the redshift window explicitly
- Problem: The map shows σfrom half for z ≤ 0.24 with a σ color bar; elsewhere σ vs monopole (full‑z) maps are discussed. To avoid ambiguity, write “σfrom half (per‑pixel, vs 0.5), z ≤ 0.24.”
- Fix: Add that wording to the color bar/caption.

Explanation
I focused on places where unit/variable definitions, small numeric drifts, and family-wise threshold examples are easy to miss on a first pass. The most substantive new issue is the density-covariate labeling in Table V (log vs linear), which affects the interpretability of the within-class density statements. Other items are consistency/clarity fixes that will prevent misreadings and make the presentation PRD-clean.