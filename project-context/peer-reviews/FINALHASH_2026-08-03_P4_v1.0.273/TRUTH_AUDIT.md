# P4 exact-final-hash truth audit

- Candidate: `pipelines/p2_chirality/chirality_catalog_paper.pdf`
- Exact SHA-256: `88bb513284db6adf4c6cf22ee7e08be2787cf8c3ebf43ffdcc289f2d369cee05`
- Receipt: `project-context/SSOT/final-acceptance/portfolio-preflight-2026-08-03.json` (`PASS`, HEAD `97258772`)
- Round: `FINALHASH_2026-08-03_P4_v1.0.273`; context `ApJS exact final candidate`
- Raw outputs: sibling flat files `FINALHASH_2026-08-03_P4_v1.0.273_P4_{Gemini_cosmology,Grok_brutal,Perplexity_citations}.md`

## Provider outcomes and evidence limits

| Route | Outcome |
|---|---|
| Grok | **Completed** on fallback (`grok-4.3`); exact hash and 32-page identity in header; pass 2 added no findings. The implementation rasterizes at most 25 pages, so pages 26–32 were not visually supplied. |
| Gemini | **Failed**. Primary packet build hit the parallel receipt-evaluator race; fallback `gemini-2.0-flash` returned 404 retired-model. |
| Perplexity | **Failed**. Primary packet build hit the same race; fallback returned 401 insufficient quota. |
| OpenAI API / Anthropic | **Unavailable by design** in this engine run; the tool explicitly disables both routes. |

The main-process receipt verification passed before dispatch. The worker-only “stale receipt” messages are a concurrency artifact: `verify_receipt()` runs an evaluator containing process-global stdout redirection simultaneously in three threads. HEAD and canonical P4 source/PDF remained clean and hash-matched.

## Finding-by-finding adjudication

| Finding | Truth-audit verdict | Exact-PDF/source basis and prior disposition |
|---|---|---|
| E1 draft/date/version/class footer | **FALSIFIED as defect** | August 3, 2026 is the actual candidate date; “Draft version” and the AASTeX 7.0.2 footer are class-generated journal-review furniture. The PDF contains no pipeline path on page 1. Version identity is intentional release provenance. |
| E2 “internal bookkeeping throughout” | **RE-FLAG / already closed structurally; no defect** | v1.0.272 moved dense hashes/paths from load-bearing prose into the artifact-provenance register/Data Availability and uses stable artifact pointers. Dataset name `Smith42/galaxies`, seeds, immutable revisions, and Zenodo identifiers are real reproducibility metadata, not review-log language. No compiled `R7/R8` tags were found. Prior closure: `INT_v3/TRUTH_AUDIT_RESWEEP_2026-07-23.md`, P4 inline-provenance item. |
| E3 abstract omits physical-bound qualifier | **FALSIFIED** | Abstract lines 12–14 in the exact PDF say verbatim that `A_95^obs` is an “observed-label sensitivity floor, not a physical parity-amplitude bound,” gated on morphology transfer. |
| E4 null families lack non-comparability warnings | **FALSIFIED / re-flag** | Abstract says WLS/harmonic paths use different supports or nulls and are diagnostics. Table `headline_summary` states the rows are “not directly comparable”; `primary_callout` repeats it; notation states which nulls answer different questions. The prompt’s demand to repeat an identical sentence at every paragraph is not a scientific defect. |
| E5 abstract lacks exact mask/seed | **FALSIFIED** | Abstract supplies selection, excluded-row count, supported-row count, and fixed-occupancy label-randomization null. Section 2 defines `HC-REALSPACE-INCLUSIVE` as 23,633 pixels and the release receipt binds the array/generator. A seed and full mask contract do not belong in an abstract. |
| M1 length | **EDITORIAL OPINION** | Exact candidate is 32 line-numbered AASTeX pages and is an ApJS catalog-and-methods article, not merely a one-scalar null note. No cited ApJS page limit establishes a defect. |
| M2 historical CE retrain undermines catalog | **RE-FLAG-DISCLOSED** | The manuscript explicitly distinguishes unchanged historical observed labels from the manifest-retained GZ1-core retrain and the honest-negative CE-included retrain. The catalog is released as an observed-label product with QC/quarantine, not as a claim that the historical training realization is recoverable. |
| M3 missing pre-quarantine map | **FALSIFIED / scope request** | Figure `fig_raw_vs_eq` and the surrounding text quantify raw/equivariant and unsafe-inclusive/release-safe changes; the raw Catalog A and quarantined-primary values are stated. A second sky map is an optional new presentation, not missing evidence for the declared primary. |
| M4 no physical transfer curve | **FALSIFIED** | The paper explicitly does not claim a physical calibration. It provides the 2,000-axis observed-label coverage curve and labels the spatial morphology transfer function an open gate. Requiring a physical curve is outside the stated estimand. |
| N1 62% lacks parent size | **FALSIFIED** | The parent is defined immediately before the gallery (8,474,566 source images; final catalog 8,474,531). The 62% statement is the displayed non-spiral fraction and is traceable from exact class counts. |
| N2 precision mismatch | **FALSIFIED / unspecified** | Integer counts and quoted binomial quantities are present; the report identifies no incorrect recomputation or concrete inconsistent cell. |
| NIT1–4 | **FALSIFIED / cosmetic opinion** | `canonical canonical-mask` is absent; `A_p` is defined; page-number cross-references in every caption are not required. No correctness issue. |

## Net decision

- Genuinely-new-real defects: **0**.
- Known non-review gate: update the existing Zenodo record from archived v1.0.268 to current v1.0.273 before submission (already tracked; not newly found).
- Reopen P4: **NO**. The sole completed vendor report adds no new real finding. This round is not multi-provider/full-document evidence because two providers failed and Grok saw only pages 1–25; that coverage limitation must travel with the no-reopen decision.

## Recovered full-document Gemini leg (FINALHASH2)

- Raw report: sibling flat file `FINALHASH2_2026-08-03_P4_v1.0.273_P4_Gemini_cosmology.md`
- Identity: exact PDF SHA-256 above; **32/32 pages supplied natively**.
- Provider/model: Gemini, `gemini-3.1-pro-preview`; report verdict **MAJOR REVISIONS**.
- Pass 1 completed successfully. The optional pass-2 self-critique was not run because the refreshed portfolio receipt became stale after packet dispatch; this does not invalidate the already-returned, packet-bound pass-1 report.

| Gemini finding | Truth-audit verdict | Exact-source/prior-history basis |
|---|---|---|
| P4-E1 stale release-overlay / Zenodo version labels | **KNOWN MANUAL GATE; not new** | The `v1.0.259` identifier is the immutable strict-primary data-overlay version, not a manuscript version. The Zenodo paragraph truthfully says the published record contains reviewed v1.0.268 while the candidate is v1.0.273. Refreshing that record to v1.0.273 is already the explicit pre-submission gate above and in `FINAL_APPROVAL_SUBMISSION_BOARD_2026-08-03.md`; it is not a newly discovered hash inconsistency. |
| P4-E2 side-by-side 2.31 / 6.48 sigma values | **RE-FLAG / known editorial family** | The statistics do use different null conventions. The paper globally declares such values non-interchangeable, identifies the raw real-space value as the legacy isotropic-permutation diagnostic, identifies the harmonic value as pre-MASTER, and the Figure 7 caption warns that the products have different provenance/support/null conventions. This exact `2.31` / `6.48` juxtaposition and local-caveat request was already logged in `R29_P4_TRUTH_AUDIT.md`; no new statistical defect. |
| P4-E3 internal review/history wording | **MIXED: necessary disclosure + known style opinion** | The post-review/unblinded timing is scientifically necessary disclosure, `superseded` prevents the naive WLS row being mistaken for the adopted uncertainty, and `next re-stage` states the known archive gate. `pod-bound` is internal jargon worth copy-editing, but this removal request is the already-audited version-history/style family (R29/R36), not a new correctness issue. |
| P4-M1 missing effect sizes for diagnostic sigmas | **MIS-TIERED / re-flag** | The cited values are explicitly systematics or signal-hunt diagnostics, not headline detections. Their nearby physical scales include the raw classifier CW excess (`0.79%`), the $A_p=2(f_{CW}-1/2)$ convention/range, and the release-safe primary amplitude/sensitivity statements. A per-diagnostic amplitude could improve presentation, but the request does not expose a new missing effect size for the declared primary claim. |
| P4-M2 uncomputed spiral-fraction bias assertion | **PARTIAL, already-scoped transfer/systematics limitation** | The source's isolated sentence is too categorical when read alone, but the same analysis supplies slab/equal-area tests, a low-ell directional regression, a constant-monopole generative test, and explicitly leaves multiplicative morphology/depth coupling open. A `2%` total spiral-selection variation has no unique induced chirality dipole without specifying differential handedness selection, so the requested single bound is not derivable from that scalar alone. No new executable defect. |
| P4-M3 forensic overload / restructure | **EDITORIAL OPINION** | Catalog A and historical-training material document how the released Catalog C was bias-hardened and delimit its label provenance. Moving it is an ApJS organization choice, not a factual/statistical defect; the current paper already concentrates signal-hunt diagnostics in appendices. |
| P4-N1 undefined CE / ECE | **SPLIT: CE FALSIFIED; ECE VERIFIED MINOR** | Immediately before Eq. B1, the source says “class-weighted cross-entropy $\\mathcal L_{\\rm CE}$,” so CE is defined. `ECE measurement` does precede the later expansion “Expected Calibration Error” by about one page. Expanding ECE at first use is one genuinely new, purely editorial minor. |
| P4-N2 1.7e7 vs 1.69e7 | **FALSIFIED as discrepancy** | `1.7e7` is the two-significant-figure rounding of `1.69e7`; the values are consistent and the body retains the more precise count. |

### Recovered-leg net

- Genuinely-new-real: **1 MINOR editorial item** (expand ECE at first use); **0 scientific, statistical, provenance, MAJOR, or ESSENTIAL defects**.
- Reopen P4: **NO**. The minor can travel as copy-edit polish; all substantive Gemini items are known gates, prior re-flags, disclosed limitations, or venue opinions.
- Evidence status improves from a 25-page raster-only completed leg to one **complete 32-page native-PDF Gemini leg**. It is still not a completed two-pass Gemini review because the optional self-critique was receipt-gated after pass 1.
