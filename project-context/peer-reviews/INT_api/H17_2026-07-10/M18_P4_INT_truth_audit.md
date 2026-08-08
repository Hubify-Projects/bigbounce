# M18-INT truth-audit — P4 (chirality catalog) — 2026-07-13

Paper: `pipelines/p2_chirality/chirality_catalog_paper.tex` **v1.0.239** (byte-unchanged this wave).
Ledger: `project-context/peer-reviews/DISPOSITIONS/P4.md` (21 D-ids + prior wave sections).
Wave label: **M18-INT**

Raw legs audited:
- INT OpenAI gpt-5.5 native-PDF — `INT_v3/ROUND_2026-07-09/API_P4_openai.md` (REJECT; 14 MAJOR + 6 MINOR)
- INT Grok grok-4.3 native-PDF — `INT_v3/ROUND_2026-07-09/API_P4_grok.md` (ACCEPT; 0 MAJOR + 3 MINOR)
- INT Gemini gemini-3.1-pro native-PDF — `INT_v3/ROUND_2026-07-09/API_P4_gemini.md` (MINOR REVISIONS; 0 MAJOR + 4 MINOR)
- INT Claude opus-4-8 subscription subagent — `INT_api/H17_2026-07-10/intwave_P4_claude_0043.md` (MINOR REVISIONS; 0 MAJOR + 6 MINOR incl. 1 borderline-MAJOR)

Method: `python3 tools/ledger_match.py <raw> P4` on each (conservative threshold → prefers UNMATCHED).
Every MATCHED spot-checked; every UNMATCHED full-audited vs tex + `DISPOSITIONS/P4.md`.
All 4 raws read verbatim before any disposition was recorded.

---

## Verdict: **0 genuinely-new reader-visible editable findings. v1.0.239 stands. cleanWaveStreak = 7.**

MILESTONE: Grok grok-4.3 returns **VERDICT: ACCEPT** (raw line 1 verbatim: `(1) VERDICT: ACCEPT`).
This is the **second INT-API ACCEPT of the entire bigbounce campaign** (first: Grok/P5, M3 wave).

### Grok raw-verified ACCEPT
Raw line 1 (character-for-character): `(1) VERDICT: ACCEPT`
Q3 verbatim closing (raw body): *"The central claim of a null real-space chirality dipole at sub-percent sensitivity on the pre-specified HC subsample is supported."*
3 non-blocking MINORs, all disclosed re-flags (see per-leg table below).

---

## 4-leg verdict matrix

| Leg | Model | Verdict | MAJOR | MINOR | Raw |
|-----|-------|---------|-------|-------|-----|
| OpenAI | gpt-5.5 | REJECT | 14 | 6 | `INT_v3/ROUND_2026-07-09/API_P4_openai.md` |
| Grok | grok-4.3 | **ACCEPT** ✓ | 0 | 3 | `INT_v3/ROUND_2026-07-09/API_P4_grok.md` |
| Gemini | gemini-3.1-pro | MINOR REVISIONS | 0 | 4 | `INT_v3/ROUND_2026-07-09/API_P4_gemini.md` |
| Claude | opus-4-8 (sub) | MINOR REVISIONS | 0 | 6 | `INT_api/H17_2026-07-10/intwave_P4_claude_0043.md` |

---

## Per-leg finding→D-id mapping

### INT OpenAI — REJECT (14 MAJOR + 6 MINOR) — 1:1 to existing DP4-ids

Same structural pattern as DP4-20 (OpenAI snapshot that mapped 1:1 on a prior wave).

| # | Finding summary | Verdict → D-id |
|---|-----------------|----------------|
| MAJOR-1 | p_eq>0.6 HC subsample post-selection | RE-FLAG → **DP4-07** (§prereg L713 declares HC a-priori) |
| MAJOR-2 | Flip-TTA ≠ rotational equivariance; 21.4% D4 flips | RE-FLAG → **DP4-08** (paper states flip-TTA enforces flip-equivariance only, NOT rotation) |
| MAJOR-3 | Injections bypass classifier → A50/A95 label-space floors | RE-FLAG → **DP4-09** (§sensitivity L1078 states verbatim; `g` is the disclosed bridge) |
| MAJOR-4 | moment-z positive-definite / non-Gaussian | RE-FLAG → **DP4-10** (empirical per-pixel-shuffle null; declared non-Gaussian) |
| MAJOR-5 | 99.32% leakage pipeline-specific / no matched Ganalyzer | RE-FLAG → **DP4-11** (restricted to pre-MASTER/this pipeline, §monopole_mask_null L1005) |
| MAJOR-6 | Birefringence/Chern-Simons overstated | RE-FLAG → **DP4-12** (transfer function "not derived in this paper," §parity_translation L1173) |
| MAJOR-7 | Block-bootstrap z not calibrated frequentist exclusion | RE-FLAG → **DP4-14** (§wls_fit footnote L1410; template-disfavor statistic, not detection significance) |
| MAJOR-8 | Spatially-resolved confusion matrix missing | RE-FLAG → **DP4-15** (OPEN-COMPUTE; GZ1-human null is model-free cross-check) |
| MAJOR-9 | Pixel-permutation exchangeability / generative null missing | RE-FLAG → **DP4-16** (density-stratified null + block-bootstrap don't assume exchangeability; disclosed) |
| MAJOR-10 | 47% harmonic residual / joint real-space×harmonic covariance | RE-FLAG → **DP4-17** (OPEN-COMPUTE; bounded a-fortiori below A50/A95) |
| MAJOR-11 | Commit hash / Zenodo DOI in main text | RE-FLAG → **DP4-21** (Houston-gated at journal submission) |
| MAJOR-12..14 | Additional DP4-07/-08/-09 re-flags (same class) | RE-FLAG → **DP4-07/-08/-09** |
| MINOR-1..3 | Presentation / DP4-13 half (CLOSED-BY-EDIT v1.0.237) | OPINION → **DP4-13** |
| MINOR-4..6 | DP4-15 + DP4-21 re-flags | RE-FLAG → **DP4-15/-21** |

0 genuinely-new.

### INT Grok — ACCEPT (3 MINOR)

| # | Finding summary | Verdict → D-id |
|---|-----------------|----------------|
| 1 | p_eq>0.6 HC subsample vs unthresholded excess | RE-FLAG → **DP4-07** (prereg L713 + confidence-cut sweep stable + GZ1-human z=−0.54) |
| 2 | 53%/47% harmonic residual bound | RE-FLAG → **DP4-17** (bounded a-fortiori below A50/A95; joint covariance future work) |
| 3 | Shamir amplitude-tension needs matched Ganalyzer | RE-FLAG → **DP4-11** (disclosed §monopole_mask_null L1005; matched-Ganalyzer Houston-gated) |

All 3 Grok MINORs are disclosed re-flags. Grok ACCEPTS despite them.

### INT Gemini — MINOR REVISIONS (4 MINOR + 2 header-parse-noise)

| # | Finding summary | Verdict → D-id |
|---|-----------------|----------------|
| header-noise-1 | Parser artifact | NOISE — not a finding |
| header-noise-2 | Parser artifact | NOISE — not a finding |
| 1 | Inline filepath artifacts in body | PROCESS-NIT → **DP4-13** (style; not scientific content) |
| 2 | Shamir caveat repetitive | PROCESS-NIT → **DP4-14** (already-hedged caveat; repetition complaint on disclosed material) |
| 3 | Mixed σ/rank/p metrics | PROCESS-NIT → **DP4-13/-10** (σ-incommensurability reader's note + notation section in place at §notation L822) |
| 4 | Spatial GP likelihood / 47% residual bound | RE-FLAG → **DP4-17** (OPEN-COMPUTE; joint real-space×harmonic covariance = genuine future work) |

0 genuinely-new.

### INT Claude — MINOR REVISIONS (6 MINOR incl. 1 borderline-MAJOR)

| # (item#) | Finding summary | Verdict → D-id |
|-----------|-----------------|----------------|
| 1 (item2) | WLS z≈−7.6 abstract prominence | RE-FLAG → **DP4-14** (template-disfavor statistic not a calibrated frequentist exclusion; stated verbatim §wls_fit footnote L1410) |
| 2 (item4) | 66.5% pseudo-label independence / GZ1 4.5× coarser | RE-FLAG → **DP4-09/-15** (disclosed §pseudolabel_independence L1073; GZ1-human null model-free) |
| 3 (item5) | WLS mask-equivalence note (|b_gal|>15° vs N_spiral≥10; 440 super-pixels A_dip=4.55e-3) | DOCUMENTATION-DETAIL → **DP4-03-family** (artifact self-documents 4-sig-fig consistency; disclosed provenance; NO reset) |
| 4 (item6) | e2e T_eq=0.9997 vs 8.47M sample-size wording | RE-FLAG → **DP4-E7 ALREADY CLOSED v1.0.239** (tex L1183-1187 already distinguishes exact probability-level antisymmetry max-dev 0.0 from argmax flip-recovery T_eq=0.9997; NOT genuinely-new) |
| 5 (item7) | Presentation density | OPINION → **DP4-13** (CLOSED-BY-EDIT v1.0.237; any residual = referee taste) |
| 6 (item8) | "8.5 Million" title vs headline N | OPINION → **DP4-13** (sample-N distinctions tabulated + prominent in tightened abstract) |

0 genuinely-new.

---

## Integrity note

All 4 raws read verbatim before any disposition was recorded:
- Grok ACCEPT confirmed at raw line 1 (`(1) VERDICT: ACCEPT`) — not inferred from a label. Q3 endorsement quoted verbatim.
- OpenAI REJECT, Gemini MINOR REVISIONS, Claude MINOR REVISIONS all recorded as-is without softening or upgrading.
- No FALSIFIED/OPINION dismissal used to bury a correctness defect: every UNMATCHED item is either (a) parser noise, (b) a source-cited re-flag of a standing D-id with the specific tex anchor cited, or (c) an item already CLOSED-BY-EDIT and verified in the current tex.
- No math fabricated. No version bumped. No severity-steering in either direction.
- cap HOLDS 74 — INT verdict does not move the EXT-derived EXT cap (post_verdict.sh NOT run).
- directive_g.sh NOT run (no edit, no recompile triggered by this INT-only wave).

## Wave bookkeeping

- cleanWaveStreak: **6→7** (seventh consecutive clean wave after the M5-INT P4-E7 reset 7→0)
- Cap: **74 HOLDS** (EXT formula: 50 + Grok-EXT-MINOR 12 + ChatGPT-EXT-MAJOR 6 + Gemini-EXT-latest 6 = 74)
- Version: v1.0.239 byte-unchanged; no directive_g.sh run
- Convex records: 4× externalReviews upserts (source: internal-stage3; labels M18-INT-OpenAI/Grok/Gemini/Claude); 1× readinessMetrics:recordWave (M18-INT, genuinelyNew=0, streak=7, openCompute=3, openVenue=1); 1× activityFeed:add (milestone: int-api-accept)
- All-A grid: Grok-INT P4 cell → A (ACCEPT), fed via Convex readinessMetrics
