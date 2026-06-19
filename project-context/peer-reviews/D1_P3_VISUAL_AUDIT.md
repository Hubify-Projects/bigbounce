# D1 P3 — Visual / Camera-Ready Audit (D-ROUND lead)

**Paper:** P3 v3.1.112 (30pp) — `pipelines/p3_anomaly_engine/paper3_draft.pdf` (md5 62d7b294)
**Source:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Method:** rendered PDF read as images (pp. 1-2, 7-9, 11-13, 16-18, 22-26) + D1 vendor visual reviews (Gemini/Grok/OpenAI/Perplexity) truth-audited against the actual render.
**Scope:** VISUAL / packaging only. Science findings deferred to the science D-round.

## Float inventory (from .tex grep)
- **13 figures**: 8 full-width `figure*` (Figs 2,3,4,7,8,9,10,12 + sky-dist + cross-survey + fnl), 5 single-column `figure` (Figs 1,5,6,11 + B11/injection).
- **8 tables**: 4 full-width `table*` (Tables I, II?, VI, + one), 4 single-column `table` (Tables III, IV, V, VII/VIII).
- Most heavy multi-panel content is ALREADY `figure*`/`table*`. The "promote to full-width" advice from D1 vendors is largely **STALE** — a prior round already widened them.

## Truth-audit of vendor visual findings

| Vendor item | Verdict | Note |
|---|---|---|
| D1-V1 abstract is one dense >20-line paragraph (OpenAI) | **VERIFIED** | p1 abstract = single ~50-line block filling all of p1, bleeds to p2. Genuinely heavy. |
| D1-V2 make Table I `table*` (OpenAI) | **STALE** | Table I already `table*` (full-width). |
| D1-V2 Table I footnotes read like body text | **VERIFIED** | p9 footnote block (¶▽♠‡∥§) runs ~15 dense lines, reads as main text. |
| D1-V3 Fig 2 legend small / ACT confusion | **PARTIAL/STALE** | p7 legend readable; ACT-quarantine warning in caption. Cosmetic only. |
| D1-V4 make Fig 3 full-width | **STALE** | Already `figure*`. y-label "Prob. density" (R) vs "Probability density" (L) — real cosmetic inconsistency. |
| D1-V5 Tables III/IV full-width | **STALE** | Table IV = 5-row single-col, fits fine. No change needed. |
| D1-V6 Figs 7/8 crowded, promote | **STALE** | Both already `figure*`; panels legible at render. |
| D1-V7 §V.A heading orphaned bottom p18 | **VERIFIED** | "NANOGrav Bounce Consistency" heading sits ~2 lines from page bottom. |
| D1-V9 Fig 11 normalization note long | **STALE** | Already in caption, plot uncluttered. |
| D1-V10 Fig 12 gallery fonts small | **STALE** | p26 panels + RA labels legible; but ~half of p26 is orphaned whitespace. |
| D1-V11 raw long file-paths wrap in columns | **VERIFIED** | Inline `\texttt` paths in BODY: p16 `pathc_dedup/r23conf_dedup_audits.json`, p11 `r24conf_erosita_axis_sweep.json`, p12 `fm2_planck_top200_train_overlap.json`, p23 `DATA_RELEASE_MANIFEST.md`. Wrap awkwardly mid-paragraph. |
| D1-V13 Data-availability paragraph dense, URLs | **VERIFIED (downgrade MAJOR→MINOR)** | p23 long justified block w/ inline URLs; URLs DO wrap, no hard margin overflow. |
| D1-V15 30pp / move galleries to Supplement | **OPINION/science-scope** | Length reduction is an editorial call, not a render defect. Out of visual-packaging scope. |
| Table VI footnote density (own find) | **VERIFIED** | p24 Table VI footnote ~12 lines w/ inline pod-provision JSON paths. |
| Fig 12 orphaned whitespace p26 (own find) | **VERIFIED** | `figure*[p]` leaves bottom half of p26 blank. |
| Date "June 18, 2026" future placeholder | **VERIFIED (science/meta)** | Title page; flagged for completeness, owned by version-bump. |

## No overflow into margins or adjacent column detected
Display equations (incl. Eq. E1, p25) fit the measure. No `figure*`/`table*` overlap. No `\texttt` path crosses the right margin (they wrap, just awkwardly).

## Prioritized fix list
See RETURN block in agent report.
