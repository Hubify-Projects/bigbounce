# INT Codex-subscription Review — P4 v1.0.253 — gpt-5.6-sol (high)
paper: P4  version: v1.0.253  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=f5108031b963d72b0dc5add880ad3213843eb170755ba58d18a121d962077e32  prompt_sha256=7d4c0dd6815ebb1c747a81a7315dc682c5553e4505b11d914be55efe42607406
provenance: commit=1307b5bff08601b1c7f82b27a376a235aa1dd3eb  source_sha256=e12d4ab129f68e84d2f80b6fdc287494feca4c3c0b90af44690b1002a780c615
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/d9030a7bb41daa52a18928372bdcd60d7be91335d4a25bc4d7117083c4f02e43.pdf  sha256=d9030a7bb41daa52a18928372bdcd60d7be91335d4a25bc4d7117083c4f02e43  pages=29
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 1307b5bff08601b1c7f82b27a376a235aa1dd3eb (scope=pipelines/p2_chirality)
UTC: 2026-07-15T20:52:51Z
context-note: Exact v1.0.253 confirmation after public immutable HF release-contract closure. Verify dataset contract revision 2fc392e22b3155107f6f56a60aa8ac75f57c866b, model card revision 3baeab8635a0c854166ecafaa03d83f9a94cea4b, model-loading claims, and whether prior bounded release findings are closed. Preserve standing science gates honestly and identify only genuinely new defects.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Catalog B is not reproducibly defined. The manuscript states that all three tiers contain 8,474,531 Parquet rows and reports \(f_{\rm CW}=0.50400(27)\) for the Platt-calibrated tier (`pipelines/p2_chirality/chirality_catalog_paper.tex:908`, `:1002-1014`), but the public schema defines only Catalog C (`pipelines/p2_chirality/apjs_release_schema_v1_0_244.json:7-23`). The retained recalibration artifact instead reports 0.1865618 with NaN Brier scores (`pipelines/p2_chirality/r42_results/wave_14_fff_gz1_platt_recal.json:20-30`). Publish Catalog B’s exact transform, parameters, payload, and validation receipt, or remove it as a released catalog tier.

2. [MAJOR] The release validator does not enforce the advertised row-level schema semantics. It verifies column names, row counts, selected flags, exclusions, and checksums (`pipelines/p2_chirality/build_apjs_release_v1_0_244.py:259-332`), but not identifier uniqueness/nullness, coordinate ranges, allowed class values, score bounds/simplex, or consistency of `class_eq`, `is_spiral`, `score_eq_max`, and `primary_hc` with their declared definitions (`pipelines/p2_chirality/apjs_release_schema_v1_0_244.json:11-21`). Thus the validation report does not independently establish the machine-readable contract claimed at `pipelines/p2_chirality/chirality_catalog_paper.tex:740` and `:1645`.

3. [MINOR] The v1.0.253 release binding is internally stale. The manuscript is v1.0.253 (`pipelines/p2_chirality/chirality_catalog_paper.tex:58`), while the immutable dataset and model cards identify v1.0.252 as current (`pipelines/p2_chirality/HF_DATASET_README.md:30,104,108`; `pipelines/p2_chirality/HF_MODEL_README.md:36,69,195`), and the fail-closed source-to-claim validator is hard-coded to v1.0.252 and therefore fails on this manuscript (`pipelines/p2_chirality/validate_p4_v1_0_244_claims.py:161,193-195`).

4. [MINOR] The pinned model card advertises “leg provenance” (`pipelines/p2_chirality/HF_MODEL_README.md:159`), contradicting both the dataset card and manuscript, which state that full-catalog imaging-leg metadata is unavailable (`pipelines/p2_chirality/HF_DATASET_README.md:97-99`; `pipelines/p2_chirality/chirality_catalog_paper.tex:1645`).

5. [MINOR] The Discussion causally attributes the hemisphere excess “specifically” to the GZ1-label/depth systematic (`pipelines/p2_chirality/chirality_catalog_paper.tex:1206`), whereas the catalog analysis retains multiple unresolved mechanisms (`:1016`, `:1650`). This should be stated as consistency, not established causation.

6. [MINOR] The 157 rejected parent objects are described only as having failed unspecified quality checks (`pipelines/p2_chirality/chirality_catalog_paper.tex:939`); the catalog selection function needs criteria, reason counts, and a rejected-object ledger.

(3) Yes—the central claim that the declared 949,584-object observed-label HC dipole is consistent with its fixed-occupancy null is supported, but it is not a true-spin or physical-parity constraint.