# P5 Truth Audit — Round H17 (2026-07-10)

Paper: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.113 → v0.1.114)
Reviewers audited: EXT ChatGPT (REJECT, ~14 MAJOR), EXT Grok (MINOR, 2 [MAJOR]-tagged),
INT Claude (MINOR), INT OpenAI/gpt-5.5 (REJECT), INT Grok (MINOR).

Integrity: verdict-first; every disposition source-cited. No fabrication; recomputed nothing —
all values below are read from committed artifacts.

---

## PRIORITY 1 — three concrete checkable ChatGPT MAJORs

### (a) Primary-estimand inconsistency — **REAL, FIXED (text)**
- **Finding (ChatGPT + OpenAI item 1/15):** Abstract (l.719-724) + §VIII B (l.2968-2977)
  designate the *footprint-restricted* contrast **Δf_CW=+0.0018, n_nonvoid=253,276** as primary;
  but **Conclusions §XV (l.4544-4546)** state "The *primary* result is … Δf_CW=+0.0007 at
  n_void=56,981" — the unrestricted/sensitivity value. Two different central estimands labeled
  "primary" in the same paper. **Independently flagged by both ChatGPT and OpenAI (gpt-5.5).**
- **Verdict: VERIFIED real editable defect.** Cross-checked lines: abstract=+0.0018 primary,
  §VIII B=+0.0018 primary, Conclusions=+0.0007 primary → genuine contradiction.
- **Fix:** Conclusions rewritten to lead with the footprint-restricted +0.0018 (n_nonvoid=253,276)
  as the single primary DESIVAST estimand and demote +0.0007 to the same-verdict sensitivity check,
  matching the abstract + §VIII B exactly. One consistent primary everywhere.

### (b) Table X mixes k=20 void with exact footprint control; exact void n_CW missing — **REAL, FIXED (table)**
- **Finding (ChatGPT + OpenAI item 3):** `tab:desivast_canonical` (l.2956-2964) tabulates the void
  row as **k=20** (n=56,981, n_CW=28,286) alongside the **exact** footprint-restricted non-void row
  (n=253,276, n_CW=126,202). The +0.0018 primary contrast is therefore not reproducible from the
  table (the exact void n_CW is absent), and the known-inexact k=20 rows are kept "for continuity."
- **Verdict: VERIFIED.** The exact-membership counts for the +0.0018 contrast **exist** in committed
  artifact `outputs/29_ext3_desivast_footprint_retabulation.json`:
  void_class = {n:57,081, n_cw:28,339, f_cw:0.49647}; nonvoid_footprint_restricted =
  {n:253,276, n_cw:126,202, f_cw:0.498279}; Δ=+0.001809, z=0.781, p=0.4349 — exactly the paper's
  primary +0.0018.
- **Fix:** Added an explicit **exact-membership void row** (57,081 / 28,339 / 0.49647) to Table X so
  the primary +0.0018 = 0.498279 − 0.49647 is reproducible from integer counts using exact membership
  on both sides. k=20 rows retained but relabeled as the sensitivity-check control (their +0.0007 row),
  not the primary; caption updated to state the primary contrast is exact-vs-exact.

### (c) GALZONE non-void definition pools catalog-invalid rows — **NOT REAL: text mis-describes code; TEXT MATCHED TO CODE**
- **Finding (ChatGPT):** void = OUT=0 ∧ ZONE≥0 ∧ VOID0≥0; non-void = "all joined rows that fail the
  conjunction," which ChatGPT reads as including catalog-invalid rows (OUT≠0, invalid ZONE) →
  non-void ≠ valid-footprint complement; two headline tests uninterpretable.
- **Code checked:** `scripts/30_ext4_galzone_complement_contrasts.py` lines 119-123:
  `j = lz.merge(gal, left_on="desi_targetid", right_on="TARGET", how="inner")` — the **inner join to
  the GALZONE HDU is itself the valid-BGS-parent restriction**; only galaxies present in the DESIVAST
  GALZONE catalog survive. `nonvoid = j[~base_void]` = complement **within that valid joined parent**,
  NOT within the full matched catalog. Arithmetic confirms: V2-REVOLVER void 104,912 + non-void 40,877
  = 145,789 = total joined parent; V2-VIDE 74,111 + 71,678 = 145,789 (same parent). No catalog-invalid
  row enters — they are dropped by the inner join before the split.
- **Verdict: FALSIFIED as a code defect** (source: script lines 119-123 + artifact-30 counts summing to
  the joined parent). The code restricts to a valid parent first, exactly as ChatGPT demands. The paper
  TEXT is imprecise ("GALZONE-joined rows that fail the void cut" without stating the join = the valid
  parent). **Fix = tighten the TEXT** in §VIII D (l.3020-3046) and the catalog-native subsection
  (l.3327-3347) to state explicitly that the non-void complement is the failure-of-conjunction taken
  **within the GALZONE-joined valid BGS parent (inner join)** — so both classes share the identical
  catalog-native valid footprint by construction and no OUT≠0 / invalid-zone row is pooled in.

---

## PRIORITY 2 — remaining MAJORs

| # | Reviewer/item | Verdict | Disposition (source-cited) |
|---|---------------|---------|----------------------------|
| P2.1 | Footprint ≠ selection-matched (ChatGPT, OpenAI-4) | already-disclosed re-flag | §VIII B l.2984-3002 "Footprint ≠ selection function" paragraph already states the footprint is *geometric*, NOT the DESIVAST/BGS completeness mask/vetoes/randoms, and that a fully selection-matched control is not constructed; residual mismatch folded into `tab:systematic_budget`. Disclosed limitation, not a new defect. |
| P2.2 | Sample not volume-limited (ChatGPT) | already-disclosed / honest scope | §VIII text states the void geometry is volume-limited BGS; the chirality sample is z≤0.24-truncated. Disclosed in limitations; genuinely-new claim that the paper *asserts* volume-limited outcome sample is not supported by the text (paper only claims the void anchor is volume-limited). No edit needed beyond existing disclosure. |
| P2.3 | Environment-stratified confusion matrix absent (ChatGPT, Grok, OpenAI-7) | already-disclosed real limitation | Abstract l.751-753 + §limitations + App A already state "no environment-stratified confusion matrix is available" and that de-attenuation carries extra uncertainty. Real open item, honestly disclosed. Not editable without new Paper-IV compute (out of scope here). |
| P2.4 | 2a−1 de-attenuation / 2.26pp caveat (ChatGPT, Grok, OpenAI-7) | already-disclosed | Abstract l.744-753 flags the symmetric-error approximation + missing stratified matrix; §XII B/App A carry the caveat. Disclosed. |
| P2.5 | Binomial independence / spatial covariance (ChatGPT) | real, partially-disclosed open item | Counting-only CI is explicitly labeled "counting-statistics-only … not a full systematic budget" (l.3048-3051). Cluster/void-level bootstrap not done. Ensured disclosed in limitations as a real open item; not closeable locally without recompute. |
| P2.6 | ≈0.9pp quadrature coverage (ChatGPT, OpenAI-5) | already-disclosed method choice | §VIII l.3059-3076 gives the explicit term list + √0.885=0.94pp and states terms are "approximately independent" and are peak-excursions vs SDs. Method fully shown; a reviewer may disagree with quadrature but it is disclosed, not hidden. Disposition: OPINION on statistical philosophy, honestly presented. |
| P2.7 | RSD MC does not model RSD (ChatGPT, Grok, OpenAI-10) | already-disclosed real limitation | Abstract l.758-765 + §limitations state all bounds are fixed-redshift-space, no reconstruction, RSD inherited; anisotropic-tidal channel "not quantified." Disclosed limitation. |
| P2.8 | Bonferroni post-hoc family (ChatGPT, Grok, OpenAI-9) | already-disclosed | §V B `sec:primary_path` + `tab:analysis_tree` disclose post-hoc designation, few-dozen-trial tree, "no timestamped plan predates the data." Disclosed garden-of-forking-paths bound. |
| P2.9 | T-Web not valid classification (ChatGPT, OpenAI-8, Grok MINOR) | already-disclosed / demoted | T-Web explicitly secondary/diagnostic/not-load-bearing (abstract l.718; Conclusions l.4552-4553); the ~23× randoms sensitivity + 73% relabel is the paper's OWN disclosure driving the demotion. Grok MINOR asks to de-emphasize the n=428 void bin prominence — cheap; addressed by a one-line demotion note (see below). |
| P2.10 | "three independent algorithms" overstatement (ChatGPT MINOR) | partially-valid nuance | VoidFinder vs V2/ZOBOV are 2 families; REVOLVER/VIDE are pruning variants. Paper already says "three-algorithm" but §desivast_three_algo notes REVOLVER/VIDE are watershed variants. Softened to "two algorithm families (sphere-growing + watershed) across five void definitions" where the "three independent" phrasing is strongest — minor honesty polish. |
| P2.11 | Imported labels not independently reviewable / placeholder arXiv (ChatGPT, OpenAI-6) | real venue/coordination item, disclosed | §I "Independence from Paper IV internals" + App A already carry the public-labels-inspectable-now + coordinated-submission disclosure. This is the known venue/coordination barrier (Houston-gated), not an editable defect. |
| P2.12 | Toy EFT non-derived (ChatGPT, OpenAI-13) | already-disclosed / relegated | App B + Conclusions l.4600-4605 explicitly label it "speculative … outside the empirical scope … not a derived constraint." Disclosed. |
| P2.13 | Abstract XIII "all five in Table XIII" but table has 3 rows (OpenAI-2) | real minor citation defect | `tab:desivast_three_algo` shows 3 sphere-PIS rows; 2 GALZONE rows live in §desivast_catalog_native / `tab:analysis_tree`. Abstract cross-ref tightened to point to the analysis-tree family table for all five, not a single 3-row table. |
| G1 | Grok: Data Availability Statement absent | real editable minor | Added explicit DAS listing DESI DR1 zall-pix-iron version, DESIVAST VAC release, HF catalog version, and DOI pointer (§ data_code). |
| G2 | Grok: de-emphasize T-Web n=428 void bin | cheap | one-line "not load-bearing; n=428 dominated by survey-shell selection" reinforcement at first prominent mention. |

**Counts:** Priority-1 → 2 real-fixed (a,b), 1 text-matched-code (c).
Priority-2 → closed with real edit: G1 (DAS), P2.13 (abstract cite), P2.10 (algorithm-count softening), G2 (T-Web demote); dispositioned already-disclosed re-flag: P2.1, P2.3, P2.4, P2.6, P2.7, P2.8, P2.9, P2.12; honest open item (disclosed, needs Paper-IV/recompute): P2.2, P2.5, P2.11.

**Integrity note:** ChatGPT + OpenAI both independently caught the same-primary contradiction (a) — a
genuinely-new real defect this round, now closed. Directive-H disposition: (a)/(b) closed by real edit;
(c) closed by truth-audit (text matched to verified code, not a code error). No ACCEPT faked; no finding
dismissed without a source-cited verdict.

## Addendum — Gemini EXT raw (harvested after owner pass; P5_gemini.md, MAJOR REVISIONS)

| # | Finding | Disposition |
|---|---------|-------------|
| G1 [MAJOR] | Cross-manuscript dependency on Paper IV (class_eq labels, κ=0.40); acceptance "must be strictly conditional on co-review/acceptance of Paper IV" | NOT-EDITABLE / PROCESS CONDITION — coordinated-submission structure is already the disclosed plan (§II, §XIII "Relation to Companion Paper IV"); Gemini itself frames this as a co-review condition, not an error. Matches ChatGPT's imported-label item, dispositioned identically by owner. |
| G2 [MINOR] | Post-hoc primary-path designation | RE-FLAG of self-disclosed limitation — Gemini's own text: "the author transparently discloses this limitation and effectively controls the family-wise error rate." §V B discloses no ex-ante plan verbatim. No new content. |
| G3 [MINOR] | RSD in fixed redshift space; reconstruction deferred | RE-FLAG of disclosed limitation — Gemini cites the paper's own FoG MC + deferral (§XIII). No new content. |
| G4 [MINOR] | Target-program × T-Web non-orthogonality (χ²=4933, V=0.078; 2.1σ filament sign flip) | RE-FLAG of disclosed residual — numbers Gemini quotes are the paper's own §VI D disclosure, already flagged in-text as unresolved ambiguity requiring future mocks. No new content. |

Gemini's central-claim sentence: "well-supported by the comprehensive multi-algorithm null tests and rigorous systematic error budget." → 0 genuinely-new findings from the Gemini leg.

## Addendum 2 — OpenAI INT re-test (API_P5_openai.md, gpt-5.5, MAJOR REVISIONS)

Re-test raw: `project-context/peer-reviews/INT_v3/ROUND_2026-07-09/API_P5_openai.md` (against v0.1.107 PDF;
audited against CURRENT v0.1.114→115 text). Two items were genuinely-new/actionable this pass and are
CLOSED by real edit in v0.1.115; the rest re-flag already-dispositioned content. Verdict-first, source-cited.

| # (OpenAI) | Finding | Verdict | Disposition (source-cited) |
|---|---------|---------|----------------------------|
| 1 [MAJOR] | Abstract/§VIII/§XV internally inconsistent primary: abstract quotes 56,981 void spirals, §VIII/§XV the footprint-restricted 57,081 exact primary | **REAL — SEAM CLOSED (v0.1.115)** | The prior pass fixed the §XV↔abstract *value* seam but the abstract still attributed the +0.0018 primary to "the same 56,981 void spirals" (l.725) and called the bound "at 56,981 void spirals" (l.738), while the exact primary uses **57,081** (artifact `29_ext3_desivast_footprint_retabulation.json`: `void_class/n`=57,081, `nonvoid_footprint_restricted/n`=253,276, `contrast_footprint_restricted`=+0.001809). Fixed everywhere: abstract now states primary `n_void=57,081, n_non-void=253,276` and attributes 56,981 ONLY to the k=20 sensitivity control; intro Sample-ledger (l.837/843) + robustness parenthetical (l.971) re-labeled so the exact 57,081 is the single primary and 56,981 is the clearly-labeled k=20 control. §XV (l.4592-4601) + primary Table `tab:desivast_canonical` were already correct (57,081 primary / 56,981 sensitivity block). |
| 2 [MAJOR] | Post-hoc analysis phrased as a "bound useful for model exclusion"; reframe as exploratory null | RE-FLAG of self-disclosed framing | Abstract l.716-718 already: "exploratory/post-hoc … all bounds below are exploratory and should not be read as pre-registered exclusions." Body already frames every result "as a bound rather than … a hard exclusion" (l.1138, l.1153, l.3087) and "a real exclusion would require …" (l.4953). No hidden "model-exclusion" claim remains; no cheap tighten outstanding. Matches P2.8. |
| 3 [MAJOR] | "DESIVAST usable footprint" is author-constructed hole-disc/radial union, not the survey completeness mask → not "same-selection-function" in the survey sense | RE-FLAG of disclosed construction | Table `tab:desivast_canonical` caption + §VIII B "Footprint ≠ selection function" paragraph (l.2978-3002) already state the footprint is the *geometric* union of hole-sphere angular discs (NSIDE=64) ∩ radial span — explicitly NOT the DESIVAST/BGS completeness mask/randoms — with residual mismatch folded into `tab:systematic_budget`. Disclosed limitation. Matches P2.1. |
| 4 [MAJOR] | ≈0.9pp "honest systematic envelope" mixes a 2σ counting interval with correlated max-excursions in quadrature; used as an effective bound | RE-FLAG / OPINION on stat philosophy | §VIII l.3059-3076 shows the explicit term list, √0.885=0.94pp, states terms are "approximately independent" and are peak-excursions vs SDs; method fully disclosed. A referee may prefer a calibrated joint interval, but nothing is hidden. Matches P2.6. |
| 5 [MAJOR] | 2a−1 de-attenuation to ≈2.26pp physical bound assumes symmetric, environment-independent label errors while no stratified confusion matrix exists | RE-FLAG of disclosed limitation | Abstract l.749-757 flags the symmetric-error approximation AND that "no environment-stratified confusion matrix is available"; §XII/App A carry the caveat and label the physical bound the weaker quantity. Disclosed. Matches P2.3/P2.4. |
| 6 [MAJOR] | Depends on companion Paper IV with placeholder arXiv IDs + labels not independently reviewed here | NOT-EDITABLE / venue-coordination (Houston-gated) | §I "Independence from Paper IV internals" + App A disclose public-inspectable labels + coordinated submission. Known venue barrier, not an editable defect. Matches P2.11 + Gemini-G1. |
| 7 [MAJOR] | T-Web strongly contaminated by DESI radial selection (~73% reassignment, ~23× void-fraction change); shorten/relegate T-Web | RE-FLAG of the paper's OWN disclosure driving the demotion | T-Web is explicitly secondary/diagnostic/not-load-bearing (abstract l.718; Reader's-guide l.1814-1818; Conclusions); the ~73%/~23× randoms sensitivity is the paper's own result. Already demoted. Matches P2.9. |
| 8 [MAJOR] | Table XIII has only 3 of 5 family tests; 2 GALZONE rows dispersed in text; present full Bonferroni-5 in one table with common sign convention, parent, counts, uncertainty | **REAL — CLOSED (v0.1.115)** | New consolidated `tab:bonferroni5_family` added in §VIII D (after the GALZONE prose): all 5 rows — VoidFinder/V2-REVOLVER/V2-VIDE sphere-PIS (56,981 / 102,911 / 81,354) + V2-REVOLVER/V2-VIDE GALZONE catalog-native (104,912 / 74,111) — with common sign convention Δf_CW≡f_nonvoid−f_void, membership/parent per row, integer void+non-void counts, z_Δ, p_Δ. Correlation labeled honestly ("correlated variants … Bonferroni-5 threshold conservative"). GALZONE numbers artifact-verified (`30_ext4_galzone_complement_contrasts.json`); sphere-PIS non-void = n_lz−n_void by construction (678,945). Supersedes P2.13. |
| 9 [MAJOR] | VoidFinder any-hole point-in-sphere is an author-constructed permissive proxy, not official per-galaxy membership | RE-FLAG of disclosed approximation | `tab:desivast_three_algo` caption (l.3288-3296) + `tab:desivast_canonical` caption already state sphere-PIS is "an author-constructed approximation … not the catalog-native definition" and VoidFinder any-hole is "a permissive proxy (no official VoidFinder per-galaxy HDU)"; the catalog-native GALZONE rows ARE the official definitions and are tabulated. Disclosed + quantified. |
| 10 [MAJOR] | Statistical framework overcomplicated; reduce to the two-sample void/non-void contrast + family-wise interval | RE-FLAG / OPINION (presentation) | The two-sample contrast IS the primary estimand (`tab:desivast_canonical`, +0.0018) and the family-wise Bonferroni-5 null IS the strictly-quotable result (abstract l.710-714). The additional σ diagnostics are disclosed supporting statistics, not competing primaries. Presentation preference, no defect. |
| 11 [MAJOR] | Speculative EFT mapping non-covariant, not data-derived; remove or relegate | RE-FLAG of disclosed relegation | App B + Conclusions already label it "speculative … outside the empirical scope … not a derived constraint." Already relegated. Matches P2.12. |
| 12-18 [MINOR] | Fig 6/8 label crowding; vweb naming; N_MC=1000 precision; match-radius row convention; prose-vs-table cross-checks; DOI/reproduction; length | RE-FLAG / polish | Fig legibility is the standing D-round item; the new `tab:bonferroni5_family` directly answers "tabulate central robustness quantities" (16); DAS/DOI added last pass (G1); naming/precision/length are cosmetic. No science defect. |

**Re-test outcome:** 2 genuinely-new actionable items closed by real edit in v0.1.115 (seam 57,081 everywhere; consolidated Bonferroni-5 family table); remaining 10 MAJORs + 7 MINORs are source-cited re-flags of already-disclosed limitations, honest scope, or presentation preference. No ACCEPT faked; no finding dismissed without a source-cited verdict; no value fabricated (all numbers read from artifacts 29 + 30). Consistent with directive-H: genuinely-new real findings closed; correlated-referee re-flags dispositioned.

---

# Addendum 3 — H17 retest2 FUSED-OWNER close→re-test loop (2026-07-10, v0.1.116 → v0.1.117)

**Owner:** P5 fused owner (accelerated pattern, directive H17). Iterated internally; 1 iteration to 0 genuinely-new.

## Fresh raws audited (all on v0.1.116)
- `INT_v3/ROUND_2026-07-09/API_P5_openai.md` (gpt-5.5, MAJOR REVISIONS, 20 items)
- `INT_v3/ROUND_2026-07-09/API_P5_grok.md` (grok-4.3, MINOR REVISIONS, 3 items)
- `INT_api/H17_2026-07-10/retest2_P5_claude.md` (Claude subagent, MINOR REVISIONS, 5 items)
- `EXT_real/H17_2026-07-10/retest/P5_chatgpt_retest.md` (ChatGPT, REJECT, on v0.1.115)

## ITERATION 1 — audit + close

### Genuinely-new editable items (3, all from the Claude retest2 leg — the current-version full-context read)

| # | Finding | Verdict | Close (v0.1.117) |
|---|---------|---------|------------------|
| C1 [MAJOR] | Two residual stale "primary Δf_CW=+0.0007" labels at tex L4330 + L2886-87 contradict the promoted footprint-restricted primary +0.0018 (n_void=57,081). Not a science error (both nulls agree to 0.11 pp) but a reader-facing headline-estimand contradiction. | **VERIFIED real editable** (lines confirmed pre-edit) | Both relabeled to primary=+0.0018 (n_void=57,081); +0.0007 explicitly the k=20 same-verdict sensitivity control. Repo grep for surviving "primary"+"0.0007" co-occurrence → empty (confirmed by Claude re-test). |
| C2 [MINOR] | "The symmetric-error premise … now has **direct empirical support**" (L4426) overstates — the support is on imaging-leg/confidence strata, NOT the void axis this paper constrains; and the 0.912 symmetry-demo accuracy vs the 0.699 de-attenuation accuracy is a scope mismatch needing a reconciling sentence. | **VERIFIED real editable** | L4426 sharpened to "direct empirical support *on adjacent (imaging-leg and confidence) strata — not yet on the void axis this paper constrains*". App A (L4869) gained a reconciliation sentence: 0.912–0.961 overlap accuracy vs the conservative 0.699 floor; only the *symmetry* property (magnitude-independent across a 10× accuracy range) is imported, not the accuracy value. |
| C3 [MINOR] | "|z_Δ|≤1.25" family cross-ref at L1687 cites `tab:desivast_three_algo` (whose max is |z|=1.12); the 1.25 extremal value lives in the V2-REVOLVER GALZONE catalog-native row. | **VERIFIED real editable** (L1750 confirms three_algo maxes at 1.12; 1.25 = GALZONE) | L1687 repointed to the V2-REVOLVER GALZONE catalog-native row / consolidated `tab:bonferroni5_family`; abstract full-family ref (L750) repointed from `tab:analysis_tree` to `tab:bonferroni5_family`. |

### Void-stratum result (checked per H17 instruction)
`pipelines/p2_chirality/outputs/gz1_stratified_confusion.json` DID gain a `stratified_by_environment_void_P5` key from the parallel compute agent — but its status is **DATA-UNAVAILABLE**: the P5 matched-chirality×DESI-z parquet + DESIVAST void-sphere catalogs are gitignored/absent in the local checkout, so the void/non-void confusion was **honestly NOT COMPUTED (not fabricated)**, with a concrete committed recipe (`P5_VOID=1`). The paper already discloses exactly this (L4874-4885: "This does not directly measure the void-stratified asymmetry … the residual gap is now concrete and recipe-backed rather than open-ended"). C2's sharpening makes the adjacent-strata scope explicit at the abstract-adjacent de-attenuation claim too. **Not integrated as a numeric result — because there is no numeric result to integrate; integrated honestly as a disclosed, recipe-backed limitation** (consistent with the leg/confidence strata, which WERE computed and are cited).

### Re-flags (dispositioned, source-cited — 0 genuinely-new)
- **OpenAI MAJOR (20 items):** all map to prior dispositions — Paper IV dependency (P2.11/OpenAI-6), classifier-label-vs-physical + missing void-stratified matrix (P2.3/P2.4, now sharpened by C2), post-hoc/garden-of-forking-paths (P2.8/OpenAI-2), footprint≠selection-mask (P2.1/OpenAI-3), membership-definition plurality (OpenAI-9, now consolidated in `tab:bonferroni5_family`), T-Web selection-dominated (P2.9/OpenAI-7, paper's own demotion), RSD redshift-space (P2.7/OpenAI-10), 0.9pp quadrature (P2.6/OpenAI-4 OPINION), target-program/2σ sign-flip (Gemini-G4 §VI D disclosure), EFT/length/figs/data-avail (P2.12 + standing D-round/polish). 0 genuinely-new.
- **Grok MINOR (3 items):** 2.26pp uncertainty-propagation (P2.3/P2.4), post-hoc primary (P2.8), RSD MC quantify (P2.7). All disclosed. 0 genuinely-new.
- **ChatGPT REJECT (on v0.1.115):** the standing maximal-harsh-referee floor — every MAJOR maps to a prior disposition (primary-control-not-selection-mask P2.1; multiplicity/exact-vs-Bonferroni-5 OpenAI-8 [consolidated table]; volume-limited-anchor P2.2; no covariate regression P2.5; 2a−1/no void-stratified matrix P2.3; conditioning-on-classifier-output P2.5-family; binomial-independence P2.5; 0.9pp quadrature P2.6; RSD MC P2.7; void-definition estimand OpenAI-9; T-Web P2.9; EFT parity-sign App B P2.12 — App B is explicitly labeled speculative/non-derived; Paper IV P2.11). The "2.8 not 2.26" point uses the 1.1pp Bonferroni input, not the paper's 0.9pp envelope (0.9/0.3982=2.26 is internally consistent) — reviewer-input choice, not a paper error. 0 genuinely-new.

## DIRECTIVE-G HYGIENE (v0.1.117)
- Version bumped `v0.1.116-2026-07-10` → `v0.1.117-2026-07-10` (+ changelog block); \date already July 10, 2026.
- TinyTeX 2-pass recompile: **0 undefined references, 0 undefined citations** (only benign OMS/cmtt font-shape substitution warning); max overfull hbox 2.07pt.
- **md5 = `f866095e3933742ab8ce9d46dbee0053`**, 45 pages, 1,525,584 bytes.
- Mirrored byte-identical to all 8 served paths (public/papers/ versioned+alias, site/public/papers/ versioned+alias, site/public/ root alias, site/out/papers/, site/out/, source dir) — all md5==source ✓. Three-way check compile==served==Convex ✓.
- Page-1 shows "Dated: July 10, 2026"; PDF body carries only `v0.1.117-2026-07-10` (no stale strings); leak-gate: 0 `/Users/houstongolden` paths in text.
- Convex `paperVersions:bump` (slug `paper-5`, v0.1.117-2026-07-10) written — id `k573ft6pxfbfvj5cjvqc64qnw18a8c1m`; sitePdfPath `/papers/p5_desi_chirality_v0.1.117-2026-07-10.pdf`.

## RE-TEST (v0.1.117, all three INT legs)
- **OpenAI (gpt-5.5, native-PDF):** REJECT, 14 items — audited: **0 genuinely-new** (all re-flags of prior dispositions, standing maximal-harsh floor).
- **Grok (grok-4.3, native-PDF):** MINOR REVISIONS, 4 items — audited: **0 genuinely-new** (all disclosed). (First attempt hit a transient XAI media-service file-ingest HTTP-400 = infra FAIL not a verdict; retry succeeded.)
- **Claude subagent (Opus, full-context):** **ACCEPT** — verified all 3 closures landed correctly with no regression, headline numbers reconcile from committed integer counts; 2 MINORs (CI last-digit rounding = benign/pre-existing; three-accuracy-tracking = correctly handled by the added reconciliation sentence). 0 genuinely-new.

## OUTCOME — CONVERGED at the LLM-refereeing floor (pattern-066 / directive-H)
Iteration 1 closed all 3 genuinely-new editable items (1 MAJOR + 2 MINOR) by real edit; the v0.1.117 re-test surfaced **0 genuinely-new real findings across all three INT legs**. Verdict triple: **INT Claude ACCEPT / OpenAI REJECT / Grok MINOR** — the below-ACCEPT verdict words are the known maximal-harsh-referee structural floor (they re-flag only already-disclosed limitations + the Houston-gated Paper IV venue coordination), NOT continuation signal. Loop STOPS per directive H-refined (0 genuinely-new = converged regardless of literal verdict word). No ACCEPT faked; no finding dismissed without a source-cited verdict; no value fabricated; void-stratum honestly integrated as DATA-UNAVAILABLE.

---

## H17F FINAL-WAVE ADDENDUM (2026-07-10, EXT re-test vs v0.1.117)

Raws: `final/P5_grok_final.md`, `final/P5_chatgpt_final.md` (read + verified before any verdict).

- **Grok EXT = ACCEPT** (raw l.25 literally `VERDICT: ACCEPT`). **First EXT ACCEPT in the program.** 4 minors all re-flags: 2a−1 extra-uncertainty note (DP5-09), T-Web not-load-bearing reiteration (DP5-14), caption "key takeaway" polish (DP5-22), "null holds"→"consistent with null" softening (DP5-22). **0 genuinely-new.**
- **ChatGPT EXT = MAJOR REVISIONS** (up a tier from REJECT). 10 MAJOR + 2 MINOR, all map 1:1 to prior dispositions — footprint≠selection-mask (DP5-06), no DESIVAST covariate regression (DP5-19/DP5-08), Bonferroni-5 family/estimand plurality (DP5-01/03/04), family-wise-null≠equivalence (DP5-11/13), 0.9pp quadrature (DP5-11), void-clustered binomial-independence (DP5-10), 2.26pp physical bound / void-stratified matrix (DP5-08/09), RSD membership-only MC (DP5-12), T-Web selection-dominated (DP5-14), Paper-IV placeholder-arXiv dependency (DP5-21), match-radius dedup MINOR (DP5-22), EFT non-derived MINOR (DP5-20). The remaining MAJORs are the **imported-label (Paper-IV, DP5-21) + companion-venue + disclosed-limitation (DP5-08/10 OPEN-COMPUTE)** class — NOT anything new. **0 genuinely-new real+editable.**

**Outcome:** Grok EXT ACCEPT confirms P5 at/above the LLM-referee floor; ChatGPT REJECT→MAJOR is honest improvement on unchanged content. 0 genuinely-new → no bump, no directive-G, v0.1.117 stands. No ACCEPT faked, no finding dismissed without a source-cited verdict, no math fabricated.
