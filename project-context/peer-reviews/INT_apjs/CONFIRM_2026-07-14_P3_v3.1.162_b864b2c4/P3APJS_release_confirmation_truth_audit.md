# P3 ApJS v3.1.162 exact release-confirmation truth audit

Date: 2026-07-14  
Scope: **release-pointer correction only; not a full-paper rereview**  
Reviewed commit: `b864b2c4` (`release(p3): publish immutable ApJS data surface`)  
PDF SHA-256: `f015bccda601fa998b2a9c5693573763e3d5710b69da07b1d23e33f877b68d64`  
PDF git blob: `8f493a8d3032d75b0d64fb52d72e409fd26518f5`  
Source SHA-256: `93954725bce91f378c2453f339ff3e0d351631ac667c88d0cce1ae123303781d`  
Source git blob: `212403dc36695347c77267425dc375e6bafe72d9`  

## What changed from exact v3.1.161

The committed source diff from `913f5033` to `b864b2c4` changes only:

1. the version stamp from v3.1.161-apjs to v3.1.162-apjs;
2. a changelog comment documenting release finalization; and
3. Data Availability, replacing old tag `p3-v3.1.157` / “no v3.1.161 tag” language with immutable tag `p3-v3.1.161`, peeled target `cdaaa03a72c69d86f011be128d93f261dc5b39a8`, a 27-file inventory, and explicit scoped-release language.

No science, method, catalog membership, count, threshold, result, or known missing-product limitation changed.

## Raw narrow-scope verdict matrix

| Leg | Verdict on release correction only | Raw SHA-256 |
|---|---:|---|
| OpenAI `gpt-5.5` native PDF | **MINOR REVISIONS** | `9463a8e3d45a735d6e2d95a446b33632390ca787ed148481854a8399fc9ecb71` |
| Grok `grok-4.3` native PDF | **ACCEPT** | `7b6e989fa32a8d51d90183859a6f45eb6a6172dafda752fed4baa92423524dd3` |
| Gemini `gemini-3.1-pro-preview` native PDF | **ACCEPT** | `a9af8465e08e743ece5fbe6420ca02489e144bd8c87e6b3f8def9131f294e04e` |
| Codex `gpt-5.6-sol/high` subscription/full repo | **MINOR REVISIONS** | `5d11ddd3142373939ce6140821adf6aa8b13f5f1bf95ddde7e98d2bc636a87a1` |

Codex execution-log SHA-256: `006d374a5f54cc2f0df41ebf3376742df59a890a0d09aa36bc16848ef5ec74e8`.

These verdict words are deliberately **not** full-manuscript verdicts and must not replace or soften the exact-v161 REJECT/MAJOR matrix.

## Independent remote verification

- `refs/tags/p3-v3.1.161` is an annotated tag object `cbd1e203d8296a692e8e3ca01e183e9db55a6adc` whose peeled target is exactly `cdaaa03a72c69d86f011be128d93f261dc5b39a8`.
- The remote `RELEASE_MANIFEST.json` at the tag has SHA-256 `741d93cba5170c41bcfd761ba6fd160ef965287c249abc9a4012aea483e7b8dd`, identical to the manifest committed at `b864b2c4`.
- All six remote scoped tables were freshly streamed from the exact tag and matched the committed bundle manifest:

| File | Verified SHA-256 |
|---|---|
| `desi_dr1_anomalies.parquet` | `0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65` |
| `sdss_dr18_pathc_native.parquet` | `5139c663c12f40217ea646fa8140c91f40194b42ca891912db73301ab78a31e6` |
| `neowise_anomalies.parquet` | `2740d936a2289ab32bc925f4507a449aa14445976e916459303874386aac42da` |
| `planck_cmb_anomalies.parquet` | `9dd3576f8de7251b9ee2bed13e61acc66d3faa530c317ae61dfd2e6b05a92740` |
| `pathc_unique_objects.parquet` | `b14deb02ddc374cc30a54e6013c0695d1c35cbf18cef9144245e338d6138c643` |
| `pathc_multi_survey_matches.parquet` | `3605b16a939b1dc44c4cb76e96dcbb7411a6eeb5917d12567c4fbc35fc85e784` |

Therefore the v161 findings “no corrected v3.1.161 immutable tag exists” and “the six scoped tables have not been verified at that tag” are **closed by exact evidence in v162**.

## Per-leg truth audit

### OpenAI

OpenAI's only MINOR says the native-PDF review packet does not contain repository-side manifest/table artifacts. This is a **modality limitation, not an artifact defect**: the PDF leg could confirm the new citation but could not inspect the repository. The independent remote verification above and the full-repo Codex leg supply the missing evidence. No manuscript/release edit follows from this finding.

### Grok and Gemini

Both returned ACCEPT with no issues for the narrow release correction. Both explicitly stated that the result affects only Data Availability/repository linkage/artifact provenance and cannot be extrapolated into a full-paper verdict. Their conclusions are supported for the pointer correction.

### Codex subscription

Codex verified the corrected tag/table evidence but found two concrete release-hygiene defects. Both independently reproduce:

1. **VERIFIED NEW MINOR — stale tracked release prose.** `pipelines/p3_anomaly_engine/DATA_RELEASE_MANIFEST.md` simultaneously says “v3.1.157,” “no new HF tag uploaded,” “25 files,” and that tables were downloaded from `573b5d...`, despite later lines and the real tagged state saying `p3-v3.1.161` / 27 files. This is internally contradictory and should be mechanically synchronized.
2. **VERIFIED NEW MINOR — stale byte-size fields.** `RELEASE_MANIFEST.json` contains correct hashes but wrong `size_bytes` for four release files:

| Path | Manifest bytes | Exact tagged bytes | SHA-256 status |
|---|---:|---:|---|
| `README.md` | 1,339 | 9,315 | correct |
| `p3_compute_to_accept/SIXWAY_DEDUP_AND_HELDOUT_METHODS.md` | 4,077 | 4,282 | correct |
| `p3_compute_to_accept/held_out_rescore.py` | 8,577 | 8,611 | correct |
| `p3_compute_to_accept/held_out_rescore_result.json` | 3,228 | 3,242 | correct |

The byte counts above were independently measured from the exact remote tag. This is metadata inconsistency, not payload corruption: every listed SHA-256 matches the downloaded file.

## Effect on exact-v161 findings

Affected and resolved by v162:

- OpenAI v161 O15: obsolete/missing corrected immutable tag — **resolved**.
- Codex v161 C9, release-pointer portion: no v3.1.161 release and unverified scoped tables — **resolved**.
- DP3-24's core public-tag/table-hash closure — **substantively verified**, but release documentation remains MINOR due to the two Codex findings above.

Not affected:

- DESI hashed-ID/source-spectrum linkage and exact rescore ceiling (DP3-15);
- mixed/continuity selection semantics and non-uniform validation (DP3-01/-07/-09/-12/-14);
- missing per-object LAMOST and native Planck products (DP3-23/-24 boundary);
- quarantined synthetic Gaia file and eROSITA provenance limitations (DP3-08);
- central-product cross-survey support (only 8 DESI-SDSS rows in the 637-row table);
- novelty, spatial-selection, presentation, and venue judgments.

## Honest disposition

The immutable pointer and all six scoped payload hashes are real and verified. The narrow release change is **substantively successful but not metadata-clean**: two mechanical MINOR release-integrity defects remain. No paper content was edited in this lane, no readiness/cap/streak was changed, and no full-paper verdict was inferred.

