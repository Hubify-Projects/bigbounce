# P2 INT — FINAL pre-sign-off full-source referee review

- **Paper:** P2 v1.7.95 — `research/focused_paper_source_integration/02_full_draft.tex`
- **Leg:** Claude Code INT (Houston subscription), full source access, read-only.
- **Date:** 2026-07-05 (final round).
- **Verdict:** **ACCEPT — publish-ready confirmed.** No genuinely-new real finding. 0 BLOCKER, 0 MAJOR, 0 MINOR requiring an edit.

## What was verified against source

### 1. Every remaining `-35/8` is labeled-erroneous-only — CONFIRMED
`awk` sweep of all non-comment lines: every `-35/8` instance in the body, tables, and figure captions is explicitly framed as the *erroneous published Cai value* ("erroneous", "would have produced", "retained only as a footnote/upper-bookkeeping reference"). The adopted central value is `-35/16 = -2.1875` everywhere:
- Eq.(2) squeezed limit (L711): `-> -35/16`. ✔
- Abstract (L658–666): headline `-35/16`; `-35/8` only as the resolved literature error. ✔
- Fig 1/3/4/5 captions, tab:systematics, tab:dualnorm, tab:bayes, tab:gr: all `-35/16` headline; `-35/8` rows explicitly the "doubled significance the Cai et al. arithmetic error would have produced." ✔
- No `-35/8` used as a live/adopted value anywhere in the non-comment body.

### 2. `-35/16` vertex certification — RE-RUN CONFIRMED (independent sympy)
Independent symbolic re-summation of Cai et al.'s four cubic vertices at ε=3/2 (Table tab:vertices, L1232–1238), forming f_NL=(10/3)A/Σk³ and taking k₁→0 with k₂=k₃=k:
- Leading squeezed term = **−35/16** ✔ (matches Eq. decisive_sqz / vertexsum).
- Subleading = **+(35/64)(k₁²/k²)** ✔ (matches L1216/L1244).
- Equilateral = **−255/128** ✔ (matches L1219).
- Li et al. cross-check: −165/16 + 65/(8c_s²) = **−35/16** at c_s=1 ✔.
The "6 ordered permutations" reading of Σ_{ijl} is required to reproduce −35/16 (the distinct-monomial reading gives −285/128), consistent with the paper's "six all-distinct triples" wording. The printed-minus-vertexsum = +(99/128)Σk³ term is not independently checkable without Cai's Eq.37 in-source, but App A is honest about this: it states +(99/128)Σk³ is "one identified discrepancy," NOT a naive additive shift, and that −35/16 is the certified vertex-sum limit (the App-A reconciliation held after v1.7.93/95).

### 3. Significance values propagate consistently — CONFIRMED
Current headline is uniformly **2.6–2.75σ (bispectrum-only)** and **1.3–2.75σ (realistic post-budget)** across abstract, body, conclusion, tab:systematics, and all figure captions. No stale −35/8-era range (5.2–5.5σ / 2.6–5.5σ) survives as a live claim; every such string is explicitly labeled erroneous. The naive 3.13σ (2.1875/0.7) reference bar is consistently marked "not used in any headline."

### 4. c8/c10/c11/c12 numbers match committed JSONs — CONFIRMED
| Artifact | Paper claim | JSON | Match |
|---|---|---|---|
| `outputs/c8_fnl_running_fisher.json` | ρ=−0.868/−0.8679; σ_unmarg=1.53; σ_marg 3.08; bias-marg 7.06 | ρ=−0.86791; 1.5287; 3.0775; 7.0595 | ✔ |
| `outputs/c9h_nullspace_significance_propagation.json` | r_16=0.702→4.4σ; r_25≈0.746; r_84=0.989 | 0.702 (sig 4.388); 0.7463; 0.9892 | ✔ |
| `scripts/c10_joint_covariance_marginalization.py` | σ_marg=1.41; floor ~1.3σ | script-only (no JSON claimed at L1204); numbers reproduced by c8 (σ_marg 1.4097, sig 1.303) | ✔ (corroborated) |
| `scripts/c11_nonlocal_template_projection.json` | LOCAL −0.985, EQUIL −0.45, ORTHO +0.94; frac 0.970→0.974 (Δr≤+0.002) | −0.98495, −0.45307, +0.93947; 0.97012→0.97368; Δr 0.00180 | ✔ |
| `outputs/c12_gr_projection_dBdAgr_probe.json` | \|ρ\|~0.95 (0.9485/0.9493); σ_marg~0.83σ; grid 23,098 | 0.94850 (sig 0.83153); 0.94926 (0.82555); n_valid=23098 | ✔ |
| `phase3_bispectrum_shape_overlap.json` | r=0.84, [0.829,0.876] | 0.84±0.02; {0.829,0.83,0.835,0.876} | ✔ |
| `phase3_fisher_overlap.json` (L1204) | archived in repo | EXISTS at `research/matter_bounce_parameters/phase3_fisher_overlap.json` (sibling dir; "same repository" claim TRUE) | ✔ |

## Findings
**None — publish-ready confirmed.** The two initial artifact flags (phase3_fisher_overlap.json "missing", c10 "no JSON") both resolved to non-issues on second look: the phase3 file exists in a sibling repo dir (the paper says "archived in the same repository," which is accurate), and L1204 does not claim a c10 JSON (only c9-series JSONs + scripts).
