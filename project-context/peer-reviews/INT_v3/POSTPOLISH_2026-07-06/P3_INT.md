# P3 v3.1.140 — POST-POLISH INT (Claude leg, full-source, read-only)

**Paper:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Scope:** verify the D-round polish (2b8fb0be) — title/abstract/prose/disclosures — under the ZERO-numbers-changed guarantee; catch polish regressions.
**Verdict: ACCEPT (polish is faithful; zero-numbers CONFIRMED).**

## Zero-numbers guarantee — CONFIRMED
Extracted every distinct numeric token added/removed in the diff, then checked each against the full current + parent `.tex`:
- Numbers the abstract *stopped* mentioning (`195{,}829`, `22.5`M, `378{,}280`, `81.5`%, `5.2`%, ACT loss `2.2×10^4`) all still present in the body/tables/appendix — abstract condensation only:
  - `2.2×10^4` → paper3_draft.tex:981, :992, :1720
  - `195{,}829` → :971, :992, :1435 (19 total)
  - `5.2%` (former-Gaia recovery) → :972, :1442
  - `81.5%` (eROSITA XV) → :1409, :1442 (5 total)
- Numbers "added" (`496`, `4.0`) already existed in body; abstract now echoes them (`496`-bin scorer at :862, :895, :940, :971, :1435). No new numeric value introduced; none deleted. **0 distinct numeric values changed vs v3.1.139.**

## Required disclosures — all present ≥once
- **Process-volume framing:** retained, now stated ONCE in a dedicated `\emph{Process-volume framing (read once):}` block (:866). ✓
- **268,519 vs 2,468 distinction:** both in abstract (`268{,}519`×5, `2{,}468`×1, `377{,}780`×1); the like-for-like 2,468 / 0.92× / 2,685 benchmark preserved. ✓
- **377,780→abstract move:** accurate — full inclusive `377{,}780` (`377{,}580` PS + `200` Planck) now stated in the abstract (removed from title), with the LAMOST ~113k FAIL and eROSITA 298 membership-only exclusions intact. ✓
- **eROSITA / LAMOST caveats:** each present in abstract (eROSITA ×3, LAMOST ×2) and body. ✓
- Title: 20 words, propagated within the .tex (metadata comment block, cover-letter paraphrase). ✓

## Polish regressions
[MINOR] **Submission-kit title staleness (out-of-D-round-scope, flag for P-round).** The old title survives in `submissions/P3/ARXIV_METADATA.txt:4`, `pipelines/p3_anomaly_engine/DATA_RELEASE_MANIFEST.md:2`, and the stale `submissions/P3/arxiv_p3_v3.1.139.tar.gz`. These are P-round/submission artifacts NOT touched by the D-round commit (which was correctly scoped to .tex + PDF mirrors); update at arXiv-packaging time.

No numeric, disclosure, or prose-integrity regression in the paper itself.
