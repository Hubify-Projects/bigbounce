# P1A INT — FINAL pre-sign-off full-source referee review

- **Paper:** P1A v1A.0.110 — `arxiv/paper1a_ech_nogo.tex` (Einstein-Cartan-Holst no-go).
- **Leg:** Claude Code INT (Houston subscription), full source access, read-only.
- **Date:** 2026-07-05 (final round).
- **Verdict:** **ACCEPT — publish-ready confirmed.** No genuinely-new real finding. 0 BLOCKER, 0 MAJOR, 0 MINOR requiring an edit.

## What was verified against source

### 1. f_NL → −35/16 propagation complete + consistent — CONFIRMED
Non-comment grep of all `35/8` / `35/16` / f_NL occurrences:
- **Exactly ONE** non-comment `-35/8` remains, at **L3767**, explicitly the "historical Cai et al." value that is "superseded by the −35/16 resolution" (provenance/context prose). NOT a live adopted value. ✔
- Adopted matter-bounce value is `-35/16` consistently at all 23 live sites: abstract L1076/L1082, L1264/L1279/L1285, tables L1443/L4066, L3032/L3045, figure caption L3734, provenance L3762–3769. ✔
- No stale −35/8-era significances (`4.375`, `6.25σ` absent; swept to `2.1875`/`3.13σ`). ✔

### 2. Abstract ↔ body sync (post-v110) — HELD
Abstract states `\fnl = -35/16` (L1076); body/tables/figures agree. The `\fbox` scope box (L1181–1211) carries no f_NL number (no mismatch possible). Headline structural claims (channel-level assessment, 13/14 barrier/catalog counts, N_tot≈92 structural tension) match the referenced body sections. No mismatch found. ✔

### 3. tab:companion_inputs artifact paths EXIST — CONFIRMED
All four companion-input paths resolve repo-relative (correct root):
- `reproducibility/cosmology/chains` — EXISTS ✔
- `reproducibility/p1_namaster_500mc` — EXISTS ✔
- `pipelines/p2_chirality` — EXISTS ✔
- `pipelines/p3_anomaly_engine` — EXISTS ✔

### 4. TODO-SUBMISSION markers coherent — CONFIRMED
Only in-tex marker is L994 `%\preprint{arXiv:XXXX.XXXXX}` — commented-out, intentional pre-submission arXiv-ID placeholder. Changelog L52 notes arXiv-ID TODO markers retained in `.bib` (not in this .tex). No real unresolved gaps. ✔

### 5. NDA dimensional chain / BS integration / ST coefficients + misc referee scan
No literal `??`, no undefined-ref indicators in text; compile log (`arxiv/paper1a_ech_nogo.log`, current) shows **0 undefined references**. `\date{\paperTimestamp}` is a macro — no overflow risk. No doubled-word or dangling-ref issues surfaced. (NDA chain / BS integration number / ST coefficients read as internally consistent with the −35/16 companion figures; no arithmetic contradiction found on the full-source pass.)

## Findings
**None — publish-ready confirmed.**
