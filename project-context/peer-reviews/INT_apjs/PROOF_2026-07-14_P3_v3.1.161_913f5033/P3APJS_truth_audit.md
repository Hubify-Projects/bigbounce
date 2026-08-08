# P3 ApJS v3.1.161 non-Anthropic INT truth audit

Date: 2026-07-14  
Status: **intermediate snapshot review, not the final publication verdict**  
Reviewed commit: `913f5033ee2ed56fa92bc2cc77b2a9436cac9ce5`  
Reviewed PDF: `pipelines/p3_anomaly_engine/paper3_apjs.pdf`  
PDF SHA-256 at launch: `ef7065b05badbdfe8bbeaf44f04895bccbc06354044a63c1651a4a8e5d5b56d1`  
PDF git blob: `1127c615d7cfea0dedf618ca01bd6d22a04637c9`  
Reviewed source: `pipelines/p3_anomaly_engine/paper3_apjs.tex`  
Source SHA-256 at launch: `e9e2a49c7969fc59341701b5fb20b80d537f38649e83fdfdc51d0ac13e6edf6d`  
Source git blob: `fa4f06b252d3b874ad71971c69fb53535a81f692`  

## Integrity and provenance

- The launch gate failed closed unless both the PDF and source matched commit `913f5033` and the expected PDF SHA-256. An intentionally wrong hash was tested first and failed before launch.
- The prompt was neutral: it asked each referee to assess correctness, reproducibility, completeness, and ApJS suitability independently and explicitly said not to presume either venue fit or support for the central claim.
- Codex ran through ChatGPT subscription login as `gpt-5.6-sol`, reasoning effort `high`, with `OPENAI_API_KEY`, `CODEX_API_KEY`, and `ANTHROPIC_API_KEY` removed, read-only sandbox, never-approve, and ephemeral execution. No Codex API-key fallback was possible.
- The first Codex attempt failed before model launch because the CLI global flags were placed after `exec`; its `ABSENT` record and raw failure are retained. The corrected subscription-only retry completed with rc=0 and does not erase the failed attempt.
- The API PDF payloads were launched while the worktree matched the reviewed commit. During the long Codex full-repository pass, a concurrent release-finalization lane advanced the worktree to v3.1.162. Codex repeatedly addressed the pinned commit with `git show 913f5033`, and its response is specific to the v3.1.161 text, but this concurrent movement is recorded rather than hidden. No v3.1.161 result is extrapolated to v3.1.162.
- No Claude/Anthropic review was run. Therefore the project review-integrity skill's Opus adjudication requirement is intentionally unsatisfied under the no-Anthropic constraint, and this audit does **not** declare convergence, acceptance, readiness, or a clean-wave advance.

## Raw verdict matrix

| Leg | Model/modality | Verdict | Raw SHA-256 |
|---|---|---:|---|
| OpenAI | `gpt-5.5`, native PDF | **REJECT** | `2d9272308ecda0fffe5ee40215646307f9995223697b7b85247c9117eeaa2820` |
| Grok | `grok-4.3`, native PDF | **MAJOR REVISIONS** | `2ee1f3ee128b8064f671abd6ac7a5f6c28d093a62c7a6d094a554cc8acfcd37d` |
| Gemini | `gemini-3.1-pro-preview`, native PDF | **REJECT** | `a18d2c5b5ef1f4e81a2b02d711b47d57f6b6c076e6531d39d3abfae6884401fb` |
| Codex | `gpt-5.6-sol/high`, subscription CLI/full repo | **REJECT** | `09cfb5ccb80eb86d4084c5971e5ce9ce65ba2c0a98e9778438eb0120e11109c3` |

Codex execution log SHA-256: `941994310034f4352fad9d192a68ea1e3cb5975e7acf254c03f9479b0ff96064`.

## Evidence keys

All line anchors below refer to `git show 913f5033:pipelines/p3_anomaly_engine/paper3_apjs.tex`, not the later worktree.

- **E1 — mixed product explicitly disclosed:** lines 1045–1055 call 268,319 a process-volume count, state that validation is mixed, identify SDSS's continuity slice and NEOWISE's geometry-only gate, exclude the archival Planck rows from the validated science product, and state the frozen release boundaries.
- **E2 — threshold heterogeneity:** lines 1071, 1125, 1206, 1240–1249, and 1336 disclose SDSS 77,905 vs native top-1% 19,253 vs strict `S>5` 12; LAMOST is exploratory; the released Planck rows are cross-transfer; and score thresholds are not directly comparable.
- **E3 — DESI validation and reproducibility ceiling:** lines 1049 and 1128 disclose correlated short proxy-fold checks, the failed `val_loss<=0.30` proxy gate, broad-feature injection sensitivity, 86.6% hashed IDs, about 1.3% re-pullability, and the missing exact released-row rescore/linkage.
- **E4 — LAMOST/Planck release boundary:** lines 1164–1166, 1206, 1240–1249, and 1658 state that LAMOST fails detector sensitivity and has no released row table; the released Planck 200 is the failed cross-transfer diagnostic; the native Planck row-level product is unavailable.
- **E5 — eROSITA/Gaia provenance:** lines 1393 and 1421 state that eROSITA's production score axis is irreproducible and Gaia is a synthetic quarantined historical artifact. Both are excluded from reported counts.
- **E6 — novelty/follow-up scope:** lines 1049 and 1459 define 178/1,000 as a top-stratum point estimate/upper bound, not a survey-wide rate. The high-redshift objects remain candidates needing follow-up.
- **E7 — cross-survey composition:** direct read of the pinned six-table bundle gives 637 rows: 627 `lamost_dr10,sdss_dr18`, 8 `desi_dr1,sdss_dr18`, and 2 `desi_dr1,lamost_dr10`. This is new supporting computation for the already-ledgered 637-coincidence interpretation, not a new defect class.
- **E8 — spatial diagnostic scope:** lines 1491–1509 explicitly call the chi-square footprint-dominated, selection-uncorrected, and not a catalog-science result.
- **E9 — exact v161 release-pointer defect:** line 1658 cites old tag `p3-v3.1.157`, says no new v3.1.161 tag exists, and requires a replacement release tag. This is true for the reviewed PDF and maps to DP3-24. A subsequent v3.1.162 finalization changes this fact and therefore requires an exact new-artifact review.
- **E10 — schema inspection:** the six Parquet payloads have ordinary pandas schema metadata but no field-level units/definitions/selection-tier metadata. This is a data-product documentation issue already covered by DP3-20/DP3-24, not a newly discovered numerical defect.

Verdict labels used below: **VERIFIED RE-FLAG** = factual limitation already represented in the ledger; **MIXED** = valid core concern plus a false/overstated subclaim; **OPINION** = editorial/venue judgment; **SNAPSHOT-TRUE** = correct in exact v161 but affected by the later release-only v162 change.

## OpenAI per-finding audit

| ID | Disposition | Ledger mapping | Evidence / truth finding |
|---|---|---|---|
| O1 | VERIFIED RE-FLAG | DP3-07/-08/-09/-14/-16 | E1/E2/E4/E5. The release is heterogeneous; this is disclosed and previously ledgered. |
| O2 | VERIFIED RE-FLAG | DP3-07/-09/-11/-12 | E1/E2/E3. The 268,319 label is mixed-validation/process-volume, not physical confirmation. |
| O3 | VERIFIED RE-FLAG | DP3-07/-11 | E1/E3. The paper itself foregrounds 2,468 science-target clusters and ~98.7% non-primary stream. |
| O4 | VERIFIED RE-FLAG | DP3-09/-14 | E2. All three SDSS thresholds and the continuity choice are explicit. |
| O5 | VERIFIED RE-FLAG | DP3-01/-09/-13 | E1/E2. NEOWISE passes geometry QA by construction, not detector sensitivity. |
| O6 | VERIFIED RE-FLAG | DP3-07/-14/-20/-21 | E4. LAMOST's failed/exploratory and no-row-table status is true and disclosed. |
| O7 | VERIFIED RE-FLAG | DP3-06/-23/-24 | E4/E9. v161 contains the cross-transfer Planck table, not the native product. |
| O8 | VERIFIED RE-FLAG | DP3-08 | E5. eROSITA is membership-only and excluded from counts. |
| O9 | VERIFIED RE-FLAG | DP3-08/-24 | E5/E9. Synthetic Gaia remains in the old frozen inventory; v162 release confirmation must test its corrected status. |
| O10 | VERIFIED RE-FLAG | DP3-15/-23/-24 | E3/E4/E9. End-to-end row-level reproduction remains incomplete even though headline arithmetic is reproducible. |
| O11 | VERIFIED RE-FLAG | DP3-01/-12/-15/-22 | E3. Proxy-fold and broad-injection limitations are stated verbatim. |
| O12 | VERIFIED RE-FLAG | DP3-06/-09/-14 | E2/E4. The score axes and cuts are heterogeneous and not cross-survey commensurate. |
| O13 | VERIFIED RE-FLAG | DP3-07/-09/-11 | E6. 17.8% is explicitly not a survey-wide rate. |
| O14 | VERIFIED RE-FLAG | DP3-11/-12 | Candidate status and need for visual/re-observation are disclosed; reviewer preference about emphasis is editorial. |
| O15 | SNAPSHOT-TRUE RE-FLAG | DP3-24 | E9. Exact v161 really lacks the corrected tag. The later v162 release-only change may close this one finding but cannot alter the other verdicts without a new review. |
| O16 | OPINION / RE-FLAG | DP3-16/-17 | The “post-hoc audit” characterization is a venue/editorial judgment based on disclosed failure modes. |
| O17 | VERIFIED RE-FLAG | DP3-14/-16 | Captions deliberately retain historical/cross-transfer diagnostics; confusion risk is real but not new. |
| O18 | VERIFIED RE-FLAG | DP3-09 | E8. The paper already limits the chi-square to a footprint-dominated diagnostic. |
| O19 | VERIFIED RE-FLAG | DP3-13 | E2/E3. Full-sample scaler leakage is admitted and partly bounded only for eROSITA. |
| O20 | OPINION / PROCESS NIT | DP3-16/-17 | Organization and repetition are editorial; no new scientific contradiction identified. |

## Grok per-finding audit

| ID | Disposition | Ledger mapping | Evidence / truth finding |
|---|---|---|---|
| G1 | VERIFIED RE-FLAG | DP3-07/-11/-16 | E1/E3. The process-volume/science-target distinction is true and explicit. |
| G2 | **MIXED** | DP3-08/-14/-21 | LAMOST failure/no table is true (E4). The statement that eROSITA “still contributes to continuity counts” is false: E1/E5 explicitly exclude it from all counts. |
| G3 | **MIXED** | DP3-06/-08/-23/-24 | Planck's archival 200 rows enter continuity counts; Gaia does **not** enter any reported count. Both old-release provenance concerns remain true (E4/E5/E9). |
| G4 | VERIFIED RE-FLAG | DP3-01/-09/-12/-22 | E1/E3. Mixed validation, correlated proxy folds, and geometry-only NEOWISE are disclosed. |
| G5 | VERIFIED RE-FLAG | DP3-03/-04/-13 | Full-sample scaling is true; 37.3M reconciliation is a standing accounting/presentation issue, not a new number. |

## Gemini per-finding audit

| ID | Disposition | Ledger mapping | Evidence / truth finding |
|---|---|---|---|
| M1 | **MIXED** | DP3-11/-15 | E3 verifies the linkage/rescore ceiling. However, “cannot be traced back to actual astronomical coordinates” is false: the released DESI table has finite `ra`/`dec` for all 195,829 rows. The lost join is to source spectra/true TARGETIDs, not sky position. |
| M2 | VERIFIED RE-FLAG | DP3-08/-15/-23/-24 | E3/E4/E5. Several row-level/native products or generating steps are unavailable; headline arithmetic remains reproducible. |
| M3 | VERIFIED RE-FLAG | DP3-08/-24 | E5/E9. The synthetic Gaia file is a real old-release provenance defect, albeit disclosed and excluded. |
| M4 | VERIFIED RE-FLAG | DP3-06/-23/-24 | E4/E9. Released Planck rows are failed cross-transfer diagnostics, not the native science product. |
| M5 | VERIFIED RE-FLAG | DP3-13 | E2/E3. Full-sample scaling leakage is real; wording that the whole pipeline is “uncorrected” overgeneralizes beyond tabular tiers. |

## Codex subscription per-finding audit

| ID | Disposition | Ledger mapping | Evidence / truth finding |
|---|---|---|---|
| C1 | VERIFIED RE-FLAG | DP3-07/-09/-14/-16 | E1/E2. Codex independently reproduced the 268,319 arithmetic but rejected scientific coherence of the “validated” union. |
| C2 | VERIFIED RE-FLAG | DP3-12/-15 | E3. Hashed IDs, ~1.3% re-pullability, score-normalization non-reproduction, and the >50% uncurated-SPARCL behavior are standing disclosed limits. |
| C3 | VERIFIED RE-FLAG | DP3-01/-12/-15 | E3. Injection substrate/threshold scope does not establish full-stream purity/completeness. |
| C4 | VERIFIED RE-FLAG | DP3-07/-11/-12/-15 | E1/E3. Science-target fraction, insecure Redrock interpretation, and lack of a per-object top-200 audit trail are standing catalog-validity concerns. |
| C5 | VERIFIED RE-FLAG | DP3-09/-14 | E2. SDSS continuity membership and cross-transfer taxonomy mismatch are explicit and previously ledgered. |
| C6 | VERIFIED RE-FLAG with **new supporting computation** | DP3-07/-09/-14 | E7 independently verifies that 629/637 cross-survey clusters involve failed-exploratory LAMOST; only 8 are DESI-SDSS in the central point-source product. This sharpens, but does not create, the already-ledgered “637 coincidences do not validate the central catalog” concern. |
| C7 | VERIFIED RE-FLAG | DP3-07/-09/-11 | E6. No pinned row-level workflow supporting 178/1,000 was found; the manuscript already scopes it as a top-stratum candidate-novelty estimate. |
| C8 | VERIFIED RE-FLAG | DP3-07 | The 0.92 count ratio is arithmetically correct, but rates differ by ~88x; the “like-for-like” interpretation has been repeatedly ledgered and remains editorially contestable. |
| C9 | SNAPSHOT-TRUE + VERIFIED RE-FLAG | DP3-20/-24 | E9/E10. Exact v161 lacks a corrected immutable tag and the scoped tables lack field-level catalog metadata. The tag-pointer part is the only item directly targeted by v162. |
| C10 | VERIFIED RE-FLAG / PROCESS NIT | DP3-09 | E8. The spatial test is already labeled diagnostic and footprint-dominated; removal/recomputation is an editorial recommendation. |

## Genuinely-new finding determination

**0 genuinely-new defect classes.** Every scientific/release issue maps to DP3-01 through DP3-24. Codex C6 supplies a useful new quantitative decomposition of an existing cross-survey-validation concern, but it does not create a new issue class. OpenAI O15 and Codex C9 correctly detect that the exact v3.1.161 snapshot predates the corrected immutable release; that is DP3-24, not a new D-id.

This result does **not** advance a clean-review streak: all four actual verdicts are adverse, the no-Anthropic constraint prevents the project-standard Opus integrity adjudication, and v3.1.162 was created after launch.

## Real actionable findings carried to exact-v162 confirmation

1. Confirm that the PDF/source now cite immutable tag `p3-v3.1.161` and exact target `cdaaa03a72c69d86f011be128d93f261dc5b39a8`, eliminating only DP3-24's obsolete-pointer defect.
2. Re-check the released manifest/file inventory against the exact new source; do not assume the tag-pointer edit fixes missing LAMOST/native-Planck products, the quarantined Gaia history, or Parquet field metadata.
3. Preserve the structural open items unchanged unless new evidence exists: DP3-15 DESI row-linkage ceiling, mixed/continuity selection semantics, and weak central-product cross-survey support (8 DESI-SDSS rows vs 637 total).
4. Do not convert the v161 REJECT/MAJOR verdict words into a v162 verdict. Run a new exact-artifact confirmation with immutable hashes.

