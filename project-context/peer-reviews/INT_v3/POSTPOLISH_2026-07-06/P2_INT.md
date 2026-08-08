# P2 POST-POLISH INT (Claude leg, canonical spec §1) — v1.7.98

**Scope:** verify D-round polish (abstract contribution-first restructure; fig 2/3/5 −35/16 value-sync; Wong palette; 76pt overflow fix; Cai email) preserved zero-numbers-changed + top-journal quality. Read-only. Commit `37253620`; HEAD `062606eb`.

## Verdict: **ACCEPT (minor)** — polish is clean, fig sync arithmetically correct; one MINOR hygiene gap.

## Zero-numbers-changed: CONFIRMED

Abstract diff (`02_full_draft.tex` L83–96) restructures 3 paragraphs (contribution → forecast/scope → load-bearing caveat) — a re-ordering, not a re-computation. Abstract number-set old→new is identical for every physics value: −35/16=−2.1875, −35/8, r∈[0.829,0.876] (0.876 CMB / 0.83 LSS), 83–88%, 2.6–2.75σ, 1.3–2.75σ, r_cos>0.97, 200 realizations, 10,000-sample scan, BF 9/14/10–17/4–7 (mid-abstract paras 3–4, unchanged by the diff), 146, 0.015, n_s=0.9649, SDB 1.53→3.08→7.06, ρ≈−0.87..−0.97, ≥5σ retired-headline reference. Only tokens removed: SPHEREx calendar dates 2025/2027/2028 (launch/survey/release) — **calendar dates, not results, and retained in body** ("launched...2025; science data release expected ∼2028", `sec:spherex`). CAVEATS preserved: scope/sensitivity-recast, no-independent-Fisher, cross-correlations-neglected, sigmas-not-inter-comparable, and the ★ cubic-transmission load-bearing caveat all survive (now once each, cleaner).

## Fig 2/3/5 value-sync: VERIFIED CORRECT (no invention)

Generator `research/live_forecast_packaging/generate_all_figures.py` finished the −35/8→−35/16 label-sync begun in v1.7.97. Each rendered value is exactly ½ the retracted −35/8 (significance ∝ |f_NL|), and each matches the paper's own already-corrected caption verbatim:
- **Fig 2** (`fig:surveys`, caption L900): bars `[3.13, 2.675, 2.025, 1.35, 3.775, 2.5, 1.5, 0.875]` with low/high = naive 2.1875/0.70=**3.13** ✓ · optimistic **2.6–2.75** ✓ · realistic **1.3–2.75** ✓ · all-combined **1.3–1.4** ✓ · MegaMapper ideal **3.7–3.85** ✓ · illustrative **1.5–3.5** ✓. Rendered PNG title reads "f_NL = −35/16"; visually confirmed, legible, Wong palette.
- **Fig 3** (`fig:kmin`, caption L1052): `FNL=2.1875`, `sig=FNL/σ`; SPHEREx bispectrum line **3.1σ** (2.1875/0.7=3.125 ✓; was 6.3σ at −35/8). Left panel (σ vs k_min, amplitude-independent) correctly unchanged.
- **Fig 5** (landscape): matter-bounce marker + SPHEREx ±0.7 error bar + the −4.375 exclusion bar all moved to **FNL=−35/16=−2.1875** ✓. PNG confirmed: diamond at ≈−2.19, not −4.375.

All PNGs regenerated and mirrored to both `research/live_forecast_packaging/` and the paper dir. No f_NL/σ value invented — pure label-sync of already-corrected headline numbers.

## Wong-palette legibility: CONFIRMED
Fig 2 and Fig 5 rendered and inspected: colorblind-safe Wong 2011 palette (blues/oranges/vermillion/green), consistent fonts, thresholds and markers legible.

## 76pt overflow fix: CONFIRMED
Raw path `project-context/peer-reviews/INT_v3/DATA_UNLOCK_2026-07-05.md` (`sec:systematics` L1043) now wrapped in breakable `\path{}`; `\UrlBreaks` extended to `/ _ - .`. Presentation-only.

## Cai courtesy email: CONFIRMED professional + accurate
`CAI_COURTESY_EMAIL_DRAFT.md` (86 lines): "DO NOT SEND" header, correct recipients (Cai yifancai@ustc.edu.cn, Brandenberger rhb@physics.mcgill.ca), respectful tone, accurately states the −35/16 vs −35/8 resolution and cites Wang & Cai 2017 Eq. 5.1. Pre-send checklist included. Appropriate courtesy note.

## AI-methods disclosure: CONFIRMED honest
Expanded to reproducibility-framed statement; specifically credits the Cai–Li resolution to a from-scratch symbolic re-summation cross-checked 3 ways against arXiv sources. AI = verification instrument, not author. Strengthened, nothing lost.

## MINOR (hygiene, non-reader-facing)
**[MINOR]** Stale legacy PDF alias `site/public/papers/02_full_draft.pdf` = md5 `ca8e376d` (last touched v1.7.97), NOT re-mirrored in the D-round; every other served copy is `7af1d09f`. Directive-G asks ALL served paths byte-identical. **Not a reader regression**: `papers.ts` L265–266 serves `/papers/paper2_fnl_forecast_v1.7.98.pdf` (in sync, `7af1d09f`); the `02_full_draft.pdf` alias is not referenced by the live site. Recommend the next hygiene pass overwrite the alias for cleanliness.

**Bottom line:** presentation + disclosure only, guarantee held, fig 2/3/5 sync arithmetically correct and visually verified. One unused stale alias to sweep.
