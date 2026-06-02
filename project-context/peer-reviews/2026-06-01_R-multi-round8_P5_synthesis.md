# P5 R-multi-round8 — synthesis (EXIT GATE)

**Date**: 2026-06-01
**Paper**: P5 (DESI DR1 chirality × cosmic-web environment)
**Input version**: v0.1.38-2026-06-01
**Output version**: v0.1.38-2026-06-01 (NO BUMP — 0 VERIFIED)
**Reviewers fired (direct vendor, NOT OpenRouter)**:
- Grok-4 brutal-honesty (13.0s, 33,738 tokens) — 2 B / 2 M / 2 m
- GPT-4o (fallback from gpt-5) methodology (9.4s, 36,247 tokens) — 1 B / 5 M
- Perplexity sonar-pro citation forensics (14.1s, 36,979 tokens) — 1 B / 3 M / 1 m / 1 nit
- Gemini-2.5-Pro — SKIPPED (billing/dunning 403 PERMISSION_DENIED; persistent vendor flake across rounds 1–8)

Counter status going IN: **2/3**
Counter status going OUT: **3/3** — **P5 HITS CASCADED-R-ROUND EXIT** per AGENT_RULES §4.4.1

---

## Truth-audit table (per `feedback_peer_review_truth_audit_protocol`)

| ID | Reviewer | Severity-claimed | Verdict | Justification |
|----|----------|------------------|---------|---------------|
| GRO-B1 | Grok | BLOCKER | OUT-OF-SCOPE | Reviewer protests in-paper audit-comment block ("per R-ext-GRO-M2", "GRO/PER/GPT labels"). These are LaTeX `%`-comments (lines 1-290), NOT abstract/§I content; reviewer is reading the source file's compile-time audit block, not the rendered abstract. Compiled PDF abstract contains zero reviewer-labels. FALSIFIED on premise. |
| GRO-B2 | Grok | BLOCKER | STALE | "Strongest single piece of positive evidence" ordering at §VII is the quantitatively-justified n=56,981 vs n=428 ordering claim, identical to R7 GRO-B1. Already closed v0.1.38 audit blocks L40, L77, L202, L249. Title remains accurate: V-Web IS the headline classifier; DESIVAST is an external-anchor consistency check, both clearly disclosed. |
| GRO-M1 | Grok | MAJOR | STALE | "Sub-percent contamination expected" + "consistent with that bound" wording at L1822, L1832 is identical to text already explicitly hedged at L1820, L1826: "scalar-displacement comparison above is a necessary but not sufficient" check, and "a full anisotropic eigenvalue deformation requires reconstructed-position re-classification." Closed v0.1.36 GRO-M2 + reaffirmed v0.1.38. Identical to R7 GRO-M2. |
| GRO-M2 | Grok | MAJOR | OPINION | Appendix A toy EFT already labeled "speculative," "not derived," "order-of-magnitude only" (closed v0.1.31 + v0.1.34 + v0.1.36 + v0.1.38). "Delete Appendix A entirely" is structural preference, not factual error. Identical to R7 GRO-m2. |
| GRO-m1 | Grok | minor | OPINION | "Upper bound any future model must satisfy" framing is standard observational-cosmology rhetoric for a null on a parameter no model currently predicts. Identical to R7 GRO-M1. |
| GRO-m2 | Grok | minor | OPINION | Title-vs-DESIVAST emphasis is a structural preference. V-Web IS the headline classifier per the title; DESIVAST is consistently disclosed as a re-projection consistency check on a larger but correlated subsample. Identical to R7 GRO-B1 sub-claim. |
| GPT-B1 | GPT-4o | BLOCKER | STALE | "Catalog-wide classifier-monopole offset" already covered with full quantitative breakdown in §IX (per-class σ = 1/(2√N) baseline + monopole-offset subtraction tabulated). All five residuals shown below Bonferroni-5 threshold at L800-811. Identical to R7 GPT-B1 / GPT-M3 fused complaint. |
| GPT-M1 | GPT-4o | MAJOR | STALE | Empirical max-stat MC null is PRIMARY (L596-705 explicitly), Bonferroni reported as transparent secondary benchmark. Reviewer hasn't read §VI.B. Identical to R7 GPT-M1 and to R6 closure. Audit block L54-55 + L95-97 cite this directly. |
| GPT-M2 | GPT-4o | MAJOR | STALE | Phase 2 sensitivity sweep already reports max Δf_CW range across the V-Web hyperparameter grid; statistical significance assessment is via the same per-class σ framework that produces the headline null. Closed v0.1.32 GRO-m1. |
| GPT-M3 | GPT-4o | MAJOR | STALE | Error propagation through systematic budget covered in §IX (per-class σ = 1/(2√N) + monopole-offset baseline + Bonferroni-5 threshold tabulation). Identical to R7 GPT-M3. |
| GPT-M4 | GPT-4o | MAJOR | STALE | RSD scalar-displacement caveat explicitly bounded at L1817-1832 with "reconstructed-position re-classification cross-check" deferred-work line; reviewer's "reconstructed-position rerun" demand is the exact deferred-work item already disclosed. Identical to R7 GRO-M1 / GPT-min1. |
| GPT-M5 | GPT-4o | MAJOR | OPINION | "Critical examination of alternative explanations" — §IX-§X already discusses systematics, classifier offset, RSD, smoothing-scale effects. Reviewer wants more discussion; structural preference. |
| PER-B1 | Perplexity | MAJOR | STALE | Shamir2022 bibitem at L2036 already carries "doi:10.1093/mnras/stac2372, arXiv:2208.13866" plus MNRAS journal designation. Volume/issue page-number completeness is cosmetic. Identical to R7 PER-B4 closure. |
| PER-M1 | Perplexity | MAJOR | OPINION | DESIVAST author-list truncation "Rincon, BenZvi, Douglass, Veyrat et al." is house style; ADS first-author "Hernán Rincon" matches "H. Rincon" exactly. First-author identity correct. Stylistic preference. Identical to R7 PER-n1. |
| PER-M2 | Perplexity | MAJOR | STALE | ASTRA arXiv:2604.01456 is already disclosed at L141 audit block as "EDR-based preprint"; in-text wording "currently available only as an EDR-based arXiv preprint" is already the recommended fix. WebFetch verified preprint status v0.1.36. Identical to R7 PER-M2. |
| PER-M3 | Perplexity | MAJOR | STALE | TWebDESI2026 bibitem at L2049 already says "submitted to MNRAS (2026), arXiv:2604.02463." Reviewer wants "arXiv preprint (submitted to MNRAS)" — semantically identical. Identical to R7 PER-B1. |
| PER-m1 | Perplexity | minor | STALE | golden_chirality_2026 / golden_fnl_2026 already labeled "(companion work, not yet peer-reviewed)" at L327 + L442 + bibitem entries L1991/L2000 ("Internal companion artifact; an arXiv identifier will be assigned upon submission"). Closed v0.1.38 GRO-m1. Identical to R7 PER-M1. |
| PER-n1 | Perplexity | nit | OPINION | DESIVAST `\artifact{}` path format is a presentation choice; URL nesting matches public DESI DR1 VAC layout (verified). Cosmetic. |

**Totals**: 17 findings audited. **VERIFIED: 0.** STALE: 11. OPINION: 5. OUT-OF-SCOPE: 1.

---

## Real closures applied (v0.1.38 → v0.1.38)

**None.** Zero VERIFIED findings.

---

## Round-by-round trend

| Round | Real findings | VERIFIED | Notes |
|-------|---------------|----------|-------|
| R1 (true95) | 9 | many | initial closure pass |
| R2 | 8 | several | |
| R3 | 5 | several | |
| R4 | 3 | 0 (Douglass false alarm) | counter reset |
| R5 | 3 | 3 (PER-M1, PER-M2, GRO-m2) | counter reset; v0.1.37→v0.1.38 |
| R6 | 3 real claims | 0 | first clean round; counter 1/3 |
| R7 | 3 surface findings | 0 | second clean round; counter 2/3 |
| **R8** | **17 surface findings** | **0** | **third clean round; counter 3/3 — EXIT** |

R-trend: **9 → 8 → 5 → 3 → 3 → 0 → 0 → 0-VERIFIED**. Convergent silence achieved on 3 of 3 vendors fired (Gemini billing-blocked across all 8 rounds; persistent vendor flake, not silence-from-paper).

Note on R8 surface count: 17 findings vs R7's 7 reflects reviewers becoming pickier and re-flagging in larger volume as substantive issues vanish — exactly the pattern AGENT_RULES §4.4.1 predicts at the exit boundary. The R8 BLOCKERs (GRO-B1, GRO-B2, GPT-B1) are all reflags of R7 content already audited STALE or OUT-OF-SCOPE.

---

## Cascaded-R-round exit criteria (per /cascaded-r-rounds + AGENT_RULES §4.4.1)

- [x] 3 consecutive rounds with zero VERIFIED BLOCKER/MAJOR (R6, R7, R8).
- [x] Convergent silence ≥ 3 of 4 vendors (Grok, GPT, Perplexity — all returning stale-only or opinion-only flags; Gemini is vendor-side billing block, not paper-side silence).
- [x] No regressions of prior closures.
- [x] Surface BLOCKERs are all reflags or premise-failures, not novel content claims.

**RESULT: P5 EXITS the cascaded R-round loop at v0.1.38-2026-06-01.**

---

## Build & mirror

**SKIPPED** — no version bump, no recompile. Current artifact (v0.1.38-2026-06-01, 940,711 B, 18 pages) stands as the post-cascade frozen state.

---

## Counter state

- Round 8: 0 VERIFIED → no bump, no recompile, no mirror, no Convex bump.
- Counter: **3/3** consecutive clean rounds → **EXIT FIRED**.
- All 6 papers (P1A, P1B, P2, P3, P4, P5) now meet AGENT_RULES §4.4.1 cascaded-loop-exit per their respective synthesis docs.
- Next gate: Houston external sign-off + final readiness award per `/readiness-cap-99`.

---

## Git status

NO commit performed. No source files modified this round. Synthesis MD created only (this file).
