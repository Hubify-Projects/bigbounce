# P3-ApJS M44 non-Anthropic INT truth audit

**Audit date:** 2026-07-14
**Reviewed manuscript:** v3.1.159-apjs, `public/papers/paper3_apjs_v3.1.159.pdf`
**Closure candidate checked:** `pipelines/p3_anomaly_engine/paper3_apjs.tex` / PDF, v3.1.160-apjs
**Scope:** ledger-first, source-independent adjudication. No source, SSOT, site, Convex, or HuggingFace mutation was performed.

## Input integrity and verdict preservation

All three raw responses were read verbatim before adjudication. There are no `[FALLBACK`, `Reviewer call FAILED`, or `ROUND DEGRADED` markers.

| Reviewer file | Actual in-text verdict | Finding count |
|---|---:|---:|
| `API_P3APJS_openai.md` (`gpt-5.5`) | **REJECT** | **12 MAJOR + 3 MINOR = 15** |
| `API_P3APJS_grok.md` (`grok-4.3`) | **REJECT** | **4 MAJOR + 1 MINOR = 5** |
| `API_P3APJS_gemini.md` (`gemini-3.1-pro-preview`) | **REJECT** | **3 MAJOR + 2 MINOR = 5** |
| **Total** | **3 REJECT** | **19 MAJOR + 6 MINOR = 25** |

The v3.1.159 PDF is 41 pages, MD5 `b7b8f8a56efa5b7096c13449e6110cf2`, and renders the July 13, 2026 title beginning “268,519 Reconstruction-Outlier Sources…”. This matches the reviewer metadata and the committed v3.1.159 source at `e24b42a9`; no wrong-paper or stale-PDF substitution was found.

## Ledger-first pass

Commands:

```bash
python3 tools/ledger_match.py API_P3APJS_openai.md P3
python3 tools/ledger_match.py API_P3APJS_grok.md P3
python3 tools/ledger_match.py API_P3APJS_gemini.md P3
```

Results, preserved exactly:

- OpenAI: **6/15 MATCHED, 9 UNMATCHED**.
- Grok: **4/5 MATCHED, 1 UNMATCHED**.
- Gemini: **2/5 MATCHED, 3 UNMATCHED**.

`UNMATCHED` means only that the lexical matcher was conservative. Every unmatched row was independently source-checked below; none was silently converted to a clean finding.

## Source-verification basis

The main checks were:

```bash
git show e24b42a9:pipelines/p3_anomaly_engine/paper3_apjs.tex | nl -ba
pdftotext public/papers/paper3_apjs_v3.1.159.pdf -
rg -n '<claim signatures>' pipelines/p3_anomaly_engine/paper3_apjs.tex
jq ... pipelines/p3_anomaly_engine/outputs/held_out_rescore_result.json
jq ... pipelines/p3_anomaly_engine/RELEASE_MANIFEST.json
git ls-remote https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog \
  refs/tags/p3-v3.1.157 'refs/tags/p3-v3.1.157^{}'
```

The pre-closure source verifies the reviewers read the actual contested text: v3.1.159 line 1037 called `268,519` a “validated catalog-grade subset”; line 1654 called the five-fold Jaccard a “genuine out-of-sample re-score”; and the Planck/release prose conflated native summaries with the released parquet. The v3.1.160 checks cited below are against the live source, not reviewer summaries.

## Per-finding adjudication

Verdict terminology follows `/peer-review-truth-audit`: `CORRECT` means the factual limitation is real; `RE-FLAG-DISCLOSED` means it was already ledgered and disclosed rather than newly discovered; `MISLABELED` means the stated severity exceeds the verified issue; `OUT-OF-SCOPE` means the reviewer applied a venue criterion outside this ApJS variant.

| ID | Reviewer / severity | Finding preserved | Ledger result | On-disk verification | Verdict / v3.1.160 status |
|---|---|---|---|---|---|
| O1 | OpenAI MAJOR | The `268,519` “validated catalog-grade” headline mixes detector-sensitivity and NEOWISE geometry-only validation. | DP3-07 (0.40) | v159 L1037 says “validated catalog-grade” while immediately admitting mixed validation. v160 L1043 instead defines **268,319 point sources**, explicitly says validation is mixed, and labels the extra 200 Planck rows archival continuity only. | **CORRECT framing defect; CLOSED reader-visibly in v160.** The broader venue judgment about mixed survey-specific validation remains a disclosed limitation, not a new computation. |
| O2 | OpenAI MAJOR | DESI's 195,829 rows cannot be reproduced object-by-object because 86.6% use hashes and only about 1.3% are re-pullable. | UNMATCHED; source mapping DP3-15 | v160 L1128 retains the exact 169,611-hash / ~1.3%-re-pull ceiling and states exact released-row re-inference is structurally blocked. | **CORRECT, RE-FLAG-DISCLOSED; OPEN structural limitation.** v160 does not pretend to recover missing linkage. The assertion that this alone invalidates any catalog claim is a venue judgment. |
| O3 | OpenAI MAJOR | DESI's scale comparison is not like-for-like: 2,468 science-target clusters, about 0.92× Liang, with ~98.7% non-primary rows. | DP3-07 (0.93) | v159 L1039 already states all four numbers and says the multipliers are not like-for-like. v160 L1045/L1069/L1680 preserve and foreground that scope. | **CORRECT, RE-FLAG-DISCLOSED; no new defect.** |
| O4 | OpenAI MAJOR | Survey-dependent thresholds (`S>5`, fixed-size SDSS slice, LAMOST top 1%, predetermined top-percent selections) undermine a combined catalog. | DP3-06 (0.51) | v160 L1125 enumerates every threshold; L1168/L1211–1244 separates analysis tallies, validated product, and continuity accounting. | **CORRECT heterogeneity, RE-FLAG-DISCLOSED.** “Undermines” is interpretive; no hidden common threshold is claimed. |
| O5 | OpenAI MAJOR | Failed-exploratory LAMOST contributes about 113,000 rows to `377,482`, so the inclusive object is not uniformly science-usable. | DP3-21 (0.30; semantically DP3-08/-09/-16) | v160 L1043 and L1384 explicitly call LAMOST a 98% training-bias / 5.8%-recovery FAIL, place it only in the 377,282 point-source continuity accounting, and disclose that no per-object LAMOST table is released. | **CORRECT, RE-FLAG-DISCLOSED.** v160 improves the label from “catalog” to “continuity”; the failed tier remains intentionally present as methodology history. |
| O6 | OpenAI MAJOR | NEOWISE was counted as catalog-grade although its test validates mask geometry by construction, not detector sensitivity. | UNMATCHED; maps DP3-01/-08/-09/-13 | v159 L1037 made NEOWISE part of the 268,519 headline while disclosing geometry QA. v160 L1043/L1047 calls the product survey-specifically validated, explicitly names geometry-only QA, and removes Planck from that product. | **CORRECT framing concern; CLOSED as far as labeling can close it.** NEOWISE's weaker validation basis remains explicitly disclosed. |
| O7 | OpenAI MAJOR | eROSITA's score axis is irreproducible and 1.2%-recovery FAIL; retaining a rank-only addendum is scientifically confusing. | DP3-08 (0.40) | v160 L1125, L1391, and L1639 say the axis is irreproducible, the detector gate fails, the tier is excluded from all counts, and only membership is usable. | **CORRECT provenance limitation, RE-FLAG-DISCLOSED.** Whether to omit the diagnostic section is editorial, not a new defect. |
| O8 | OpenAI MAJOR | Planck selection is not an adequate physical tier: native checkpoint/tensor are absent, held-out evidence is limited, and injection is simplified. | UNMATCHED; maps DP3-06/-11 and M44 C7 | Direct artifact check shows the public parquet is cross-transfer (`patch_idx<20,000`, scores 0.306–62.999), while native checkpoint/tensor/table remain absent. v160 L1414 and L1723 now distinguish them and exclude released Planck from the validated product. | **CORRECT. C7's identity error is CLOSED locally/reader-visibly in v160; the unavailable native product remains an honestly open data limitation.** Public-tag closure is separately incomplete below. |
| O9 | OpenAI MAJOR | The 17.8% “genuine novelty” value is top-1,000-only; SIMBAD-unmatched rates are not discovery rates. | UNMATCHED; maps DP3-07/-09/-11 | v160 L1047/L1452/L1456/L1639/L1697 limits 17.8% to one top-1,000 stratum, gives its Wilson interval, calls full-catalog extrapolation untested, and demotes SIMBAD rates to coverage diagnostics. | **CORRECT, RE-FLAG-DISCLOSED.** The phrase “genuine novelty/discovery-rate figure” remains semantically stronger than “no counterpart in the tested catalogs”; not new to M44. |
| O10 | OpenAI MAJOR | The `f_NL` application is null, selection-function-limited, and not a PRD-grade physics result. | UNMATCHED; maps DP3-10/-19 | v160 L1051/L1574/L1576/L1603 calls it a secondary demonstration, reports `alpha=0.19±0.65`, exact de-biased zero improvement, and states zero-systematics/selection limitations. | **CORRECT scientific limitation; MISLABELED as an undisclosed defect.** PRD suitability is a venue opinion for an ApJS variant. A separate cross-paper numerical defect is documented below. |
| O11 | OpenAI MAJOR | NANOGrav compares against idealized circular SMBHB with a factorized KDE; environmental SMBHB models can mimic `gamma≈2.5–3`. | UNMATCHED; maps DP3-10/-19 | v160 L1051/L1618–1622 and Appendix E disclose the factorized-KDE approximation and state the Bayes factor is decisive only against circular-orbit `gamma=4.33`, not environmental SMBHBs. | **CORRECT, RE-FLAG-DISCLOSED.** “Too incomplete” is a scope/editorial judgment, not new evidence. |
| O12 | OpenAI MAJOR | Full-sample scalers, failed proxy retain gates, single-architecture dependence, unweighted MSE, and narrow-line floor limit ML validation. | UNMATCHED; maps DP3-01/-12/-13/-15 | v160 L1108, L1116, L1128, and L1639 disclose every listed limitation; the proxy artifacts record `best_val_mean=1.91`, `all_folds_pass_gate=false`, and narrow-line recovery only at ≥15σ. | **CORRECT, RE-FLAG-DISCLOSED.** C4's distinct OOF-label error is closed in v160, but these limitations remain. |
| O13 | OpenAI MINOR | Manuscript is long, repetitive, defensive, and caveat-heavy. | UNMATCHED; maps DP3-16 | Source/PDF confirm the style. This is not a falsifiable science defect. | **MISLABELED / EDITORIAL OPINION.** v160 is shorter (37 vs 41 pages) but no objective acceptance gate follows. |
| O14 | OpenAI MINOR | Multiple scan denominators/totals are hard to audit. | DP3-04 (0.65) | v160 L1168 and L1244 explicitly reconcile 36.76M, 36.93M, 37.29M, 37.3M, 377,482, 378,280, and 378,480 in one provenance/accounting surface. | **CORRECT presentation concern, substantially CLOSED in v160.** |
| O15 | OpenAI MINOR | Figures 3, 4, and 8 use historical/cross-transfer/display-only score axes and may mislead. | UNMATCHED; maps DP3-14/-16 | v160 Figure 3 caption labels the LAMOST/SDSS history; Figure 4 is titled “Cross-transfer SDSS baseline”; Figure 8 explicitly says display scores are not catalog scores (L1348/L1550 and captions). | **CORRECT risk, RE-FLAG-DISCLOSED; placement is editorial.** |
| G1 | Grok MAJOR | The abstract's single `268,519` validated headline hides nonuniform tier status. | DP3-07 (0.40) | Same evidence as O1: v159 L1037 versus v160 L1043. | **CORRECT; CLOSED reader-visibly by the 268,319 point-source + 200 archival split.** |
| G2 | Grok MAJOR | eROSITA's 0.259 axis is irreproducible despite a released membership list; provenance treatment is inadequate for a catalog. | DP3-08 (0.30) | v160 L1125/L1391 and the released-axis reproduction artifact preserve the failure and restrict use to rank membership. | **CORRECT, RE-FLAG-DISCLOSED; venue judgment remains.** |
| G3 | Grok MAJOR | DESI rests on one production sensitivity gate; correlated short-trained proxies that fail the retain gate are only corroboration. | DP3-02 (0.33; also DP3-01/-12 and M44 C4) | v159 L1654 correctly listed the proxy failure but falsely called the Jaccard “genuine out-of-sample.” v160 L1128/L1149/L1663 and `held_out_rescore_result.json` now call it model-ranking stability and reserve “direct OOS” for the disjoint-tail statistic. | **CORRECT. C4 is CLOSED in v160.** The single production-gate scope remains candidly disclosed. |
| G4 | Grok MAJOR | Full-sample tabular scaling plus 86.6% hashed DESI IDs prevent exact score reproduction. | UNMATCHED; maps DP3-13/-15 | v160 L1108 and L1128 verify both independent limitations; neither is presented as solved. | **CORRECT, RE-FLAG-DISCLOSED; structural residual remains OPEN.** |
| G5 | Grok MINOR | Null secondary cosmology occupies too much space. | DP3-10 (0.42) | v160 L1574 explicitly labels both applications secondary/non-detections. | **MISLABELED / EDITORIAL OPINION.** |
| M1 | Gemini MAJOR | The paper is out of scope for PRD and better suited to ApJS/Astronomy and Computing. | UNMATCHED; maps DP3-10/-16 | The reviewed file is explicitly `P3APJS`, formatted AASTeX, and titled as an ApJS variant. Gemini's own recommended venue is the venue of this manuscript. | **OUT-OF-SCOPE / INCORRECT venue frame for this artifact.** It does not establish an ApJS defect. |
| M2 | Gemini MAJOR | The `f_NL` tracer forecast lacks selection-function/redshift/systematics validation. | UNMATCHED; maps DP3-09/-10/-13/-19 | v160 L1576/L1603/L1639 discloses zero-systematics assumptions, noisy bias, selection limits, and conditional status. | **CORRECT, RE-FLAG-DISCLOSED.** It remains a secondary, non-detection demonstration. |
| M3 | Gemini MAJOR | NANOGrav's circular-SMBHB comparison cannot discriminate environmental SMBHBs from a bounce. | DP3-19 (0.49) | v160 L1051/L1620 states this exact non-discrimination and limits the Bayes-factor interpretation. | **CORRECT, RE-FLAG-DISCLOSED.** |
| M4 | Gemini MINOR | Raw paths/JSON filenames/commit hashes clutter the manuscript. | UNMATCHED; maps DP3-04/-16 | PDF/source visibly contain many `\artifact{}` paths. They are intentional reproducibility anchors; v160 removes the raw external commit hash from the paper but retains artifact paths. | **MISLABELED / EDITORIAL OPINION.** |
| M5 | Gemini MINOR | eROSITA/Gaia failure-mode discussion should be condensed or moved to an appendix. | DP3-08 (0.40) | v160 L1391/L1421 retains the sections because they disclose released-data provenance and quarantine; both tiers are excluded from science counts. | **MISLABELED / EDITORIAL OPINION.** No scientific error is identified. |

## M44 C4/C7/C8 closure verification

| Defect | v3.1.160 evidence | Closure status |
|---|---|---|
| **C4 — five-model Jaccard mislabeled fully OOF** | `held_out_rescore_result.json` now states each model scores the full 47,000 rows and that Jaccard is model-ranking stability; v160 L1128/L1149/L1663 uses the same language and names reserved-block tail preservation as the direct OOS test. | **CLOSED.** No fully-OOF catalog claim remains. |
| **C7 — released Planck file mislabeled native** | v160 L1043/L1414/L1723 and local `RELEASE_MANIFEST.json` identify the 200 released rows as the `<20,000` cross-transfer baseline (0.306–62.999), exclude them from the validated product, and state the native checkpoint/tensor/top-200 are unavailable. | **CLOSED in manuscript and local release payload.** Native row-level reproducibility remains unavailable by fact, not hidden. The old public tag is not yet repaired. |
| **C8 — Gaia/LAMOST/tag inventory contradiction** | v160 L1421/L1710/L1723 and local `RELEASE_MANIFEST.json`/`HF_DATASET_README.md` say Gaia is a quarantined 500-row synthetic placeholder, LAMOST has no per-object file, and the tag peels to `573b5da…`. | **CLOSED locally, NOT atomically closed on HuggingFace.** Remote `p3-v3.1.157` still has 25 files, calls Planck native and Gaia exploratory-real, contains no LAMOST file, and its manifest incorrectly names `f738267…`; `git ls-remote` proves the tag peels to `573b5da…`. A replacement tag is still required. |

## Genuinely-new items beyond C4/C7/C8

### Reviewer-derived result

Across the **25 INT findings**, there is **no genuinely-new reviewer-derived defect beyond the already adjudicated M44 classes**. Every row is one of:

- a direct re-flag of DP3-01…DP3-21;
- an adjacent statement of C4 or C7;
- a venue/editorial opinion; or
- a limitation the paper already states explicitly.

This does **not** turn the three REJECT verdicts into ACCEPT, and it does not mean the paper is release-ready. It means the INT raws add no fourth independent defect class.

### Director-found cross-paper claim-sync defect — genuinely new and live

During acceptance review, a separate defect was found that none of these three INT reviewers identified. P3-ApJS v3.1.160 still states the superseded matter-bounce value `f_NL=-35/8` and its old `2.6–5σ` significance at **six live source locations**:

- `paper3_apjs.tex:1068`
- `paper3_apjs.tex:1576`
- `paper3_apjs.tex:1614`
- `paper3_apjs.tex:1685`
- `paper3_apjs.tex:1703`
- `paper3_apjs.tex:1943`

The canonical P2 source, `research/focused_paper_source_integration/02_full_draft.tex` v1.7.117, instead certifies the corrected central prediction `f_NL=-35/16=-2.1875` (e.g. L997) and reports the updated exact-shape/forecast ranges, including optimistic `2.6–2.75σ` and realistic `1.3–2.75σ` surfaces. This is a **GENUINELY-NEW cross-paper claim-sync defect**. It is not closed by v3.1.160 and was deliberately not edited during this audit.

## Final disposition

- **Reviewer verdicts remain:** OpenAI REJECT, Grok REJECT, Gemini REJECT.
- **Reviewer findings:** 25/25 adjudicated; 0 TBD; no reviewer-derived new defect beyond M44 C4/C7/C8.
- **C4:** closed.
- **C7:** closed in manuscript/local release payload; native data absence remains disclosed; public tag still stale.
- **C8:** closed locally but **not** on the immutable public-release surface until a replacement tag is minted and verified.
- **Release readiness:** **FAIL / NOT READY.** P3-ApJS must not be released as v3.1.160 until P2's v1.7.117 exact-shape numbers are frozen, all six P3 `-35/8` / old-significance surfaces are resynchronized, the paper is version-bumped/recompiled/audited, and the corrected HF release is published and checksum-verified.

No ACCEPT verdict, native Planck product, LAMOST table, exact DESI linkage, or cosmological significance was fabricated in this audit.
