# P3 v3.2.0-r8 Codex finding truth audit

Source review: `project-context/peer-reviews/INT_apjs/CONFIRM_2026-07-14_P3_v3.2.0-r7_761e35ec/API_P3APJS_codex_140430.md`
Raw-report SHA-256: `1cfc6e8807da881a9e7f1550fdf9e1c8784d980f782c3128f0b5f22e957fa22b`
Reviewed manuscript commit: `ba2f5b93a30de41122dc2ed31b543ac0da9a37c8`
Reviewed PDF SHA-256: `761e35ec840e93599163d68c6b4db9b8d75293545e49c45c978dc0be0f38cb2b`

This receipt adjudicates the five findings from the bounded subscription-Codex review. The review verified the exact 16-page PDF, visually inspected pages 1--16, read the full source and bounded bundle, and made no FITS or network access.

| # | Referee severity | Truth-audit class | Source-cited disposition | r8 action |
|---|---|---|---|---|
| 1 | MAJOR | **REAL, packaging-only** | At the reviewed commit, the r7 bundle Git tree contained 38 files while its complete contract requires 41. The three absent copies are listed in `BUNDLE_MANIFEST.json` with exact byte counts and hashes. This makes the advertised bundle validator fail after a fresh checkout even though the scientific products exist elsewhere. One subclaim was false: the separately cited warned-auxiliary source directory does contain its 352,155-byte Parquet at the reviewed commit (`git cat-file -s ba2f5b93:.../desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet` = 352155). | Preserve the manifest and component bytes; track exactly the three already-present, hash-matching bundle copies. A clean-tree-equivalent replay passes 41/41 files. No reader-visible scientific claim changes. |
| 2 | MINOR | **REAL, reader-visible** | Section 3.4 stated that the 1-arcsec join was predeclared but did not state the provenance of the 0.1-arcsec quality boundary. No evidence supports calling the latter predeclared. | `paper3_apjs.tex:301` now states in one sentence that 0.1 arcsec was introduced post hoc as a descriptive tier, is not a predeclared selection cut, and does not alter the 181-row membership. |
| 3 | MINOR | **ALREADY CLOSED** | Section 5.3 already says direct candidate-count comparisons are not meaningful and that evaluation against a representative control sample remains required (`paper3_apjs.tex:585`--`591`). “Testing” in Section 5.2 is therefore bounded to cross-scoring/follow-up use, not discrimination, calibration, completeness, or false-positive-rate validation. | No edit. |
| 4 | MINOR | **ALREADY CLOSED** | The abstract states that production normalization and physical-feature sensitivity are not reconstructed and calls the product a reproducible follow-up list, not a validated detection (`paper3_apjs.tex:37`--`64`). Section 7 separately disclaims exact score reproduction, physical classification, novelty, identity, and purity (`paper3_apjs.tex:681`--`703`). | No edit. |
| 5 | MINOR | **OPTIONAL PRESENTATION** | All 16 r8 pages were rendered and inspected. Page 5's float flow and pages 13--15's whitespace are visible but do not obscure content; there is no clipping, overlap, margin escape, or gutter crossing. | No edit; formatting audit PASS. |

## Closure recommendation

The only blocker was the incomplete Git representation of an otherwise hash-complete bundle. Tracking the three unchanged payload copies and passing the isolated 41-file validator closes that blocker without changing the scientific contract. The one genuine reader-facing provenance ambiguity is closed by the r8 sentence. The remaining findings are already bounded in the manuscript or optional presentation comments. This is a closure audit, not a new review wave and not an acceptance or readiness claim.
