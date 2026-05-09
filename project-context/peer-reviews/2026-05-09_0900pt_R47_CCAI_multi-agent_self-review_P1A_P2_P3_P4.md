# R47 multi-agent adversarial peer review — 2026-05-09 09:00 PT (Wave 14-BBBBB)

Houston directive: continuous R-round adversarial review until findings dwindle to next-to-nothing. R43 → R44 → R45 → R46 ran the loop; **R47 is the SECOND CONVERGENCE TEST after R46.** Exit condition: <3 BLOCKER + <5 MAJOR for two consecutive rounds.

Four parallel Claude general-purpose subagents reviewed the post-Wave 14-AAAAA versions on disk at commit 7a907a67; P1B excluded (compute-gated on cobaya R̂−1 < 0.01). Per-paper reports saved at `2026-05-09_0900pt_R47_CCAI_P{1A,2,3,4}.md`.

## R47 totals

| Paper | Version | BLOCKER | MAJOR | MINOR | NIT | Total | R46 prior | Δ |
|---|---|---|---|---|---|---|---|---|
| P1A | v1A.0.12 | 1 | 1 | 3 | 1 | 6 | 9 | −33% |
| P2  | v1.7.19  | 1 | 3 | 3 | 2 | 9 | 11 | −18% |
| P3  | v3.1.30  | 0 | 2 | 3 | 2 | 7 | 12 | −42% |
| P4  | v1.0.38  | 0 | 3 | 4 | 2 | 9 | 9 | 0% (FLAT) |
| **R47 total** | | **2** | **9** | **13** | **7** | **31** | **41** | **−24%** |

**Round-on-round convergence trajectory:**

| Round | BLOCKER | MAJOR | MINOR | NIT | Total | Δ vs prior |
|---|---|---|---|---|---|---|
| R43 | 10 | 31 | 30 | — | 71 | — |
| R44 |  5 | 23 | 17 |  5 | 50 | −29% |
| R45 |  6 | 21 | 17 |  6 | 50 |  0% |
| R46 |  3 | 15 | 14 |  9 | 41 | −18% |
| R47 |  2 |  9 | 13 |  7 | 31 | **−24%** |

**Convergence is real and accelerating.** Total findings down 24% (R46→R47) after 18% (R45→R46). BLOCKER count down to 2 (1 P1A + 1 P2 — both cross-section consistency issues, not new science errors). MAJOR count down 40% (15→9). However, the **<3 BLOCKER + <5 MAJOR** exit condition is NOT yet met (9 MAJORs remaining). One more clean closure wave + a clean R48 would meet the exit condition.

## Two R47 BLOCKERs are propagation failures from R46-closure waves

- **P1A-R47-B1** (most consequential — cross-paper): The Wave 14-AAAAA m3 closure introduced a `‡` footnote at L1056 that reads: "see Paper~I(b) §VII.H for the zero free-$w_0w_a$-sample disclosure." But Paper 1B has NO §VII.H — §VII is "Cross-Paper Verification Status" with no lettered subsections. WORSE, the footnote claims "zero free-$w_0w_a$ samples" but Paper 1B Table III line 481 explicitly lists "DESI DR2 w0wa (new): ~109 accepted, Running." A referee opening Paper 1B catches the contradiction immediately. **Fix:** coordinate cross-paper edit — either (a) add §VII.H to Paper 1B with the explicit disclosure, or (b) re-anchor Paper 1A's footnote to the actual §VII content. Both must land in the SAME commit.

- **P2-R47-B1**: Table 4 (`tab:bayes`) row 5 claims BF~17 at "delta + broad multifield [-15,+15] + σ_GR=0.5"; Table 5 (`tab:gr`) BF-vs-Tuned column at σ_GR=0.5 gives 9.4. If "Tuned" = broad multifield, Table 4 and Table 5 disagree by 1.8×. If "Tuned" uses a narrower competitor prior (presumably [-5,+5]), this is never stated. The XXXX-r46 BF~17 row addition collided with the existing Table 5 framing. **Fix:** add competitor-prior-width to Table 5 caption + reconcile Table 4 row 4 ("8–11", labeled "theoretical maximum only") vs row 5 (BF~17).

## P3 is BLOCKER-free at R47 — newly cleanest paper

P3's tier-rebuild (YYYY) and AAAAA polish held up under R47 scrutiny. Cluster-manifest pointer, PTA sign convention, 9.6× α-vs-b distinction, NANOGrav γ rounding, eROSITA 298 top-cut, and 378,080 + 200 = 378,280 stratification all check out. The two surviving MAJORs are both consistency drift, not new science errors:
- M1: §sec:limitations L583 still labels 17.8% as "provisional upper bound" while abstract uses "single-sample point estimate" — the AAAAA m1 closure didn't quite finish the propagation.
- M2: Data availability paragraph L651 points readers at `pathc_unique_objects.parquet` (the with-ACT 378,480-row sensitivity-check file) for "all headline numbers", contradicting the ACT-quarantine policy. Off-by-200 reproducibility hit.

## P4 is FLAT (R46→R47: 9→9) — propagation failures from ZZZZ+AAAAA

The four ZZZZ MAJORs all closed cleanly in their target sections, but three NEW MAJORs emerged from incomplete propagation:
- M1: §X Conclusion #1 still quotes "marginal 2.75σ" for ℓ=1 — the SUPERSEDED raw-pseudo-C_ℓ value. Canonical is −0.12σ (MASTER-deconvolved). Paper's own §VII.B claims "abstract, intro, conclusions all quote the high-confidence dipole upper bound" — Conclusion #1 violates this self-stated invariant.
- M2: §X Conclusion #2 reverts to single-number "factor of 9" — abstract/§I/§VIII.A all carry the corrected "factor of ~6-12 (central ~9)" from ZZZZ M3 closure; conclusions weren't updated.
- M3: §III.B claims 3.86× suppression on +0.79% → −0.26% (which gives 3.04×, not 3.86×). The 3.86× is the §IX.B raw-to-eq-NS-pool factor on +2.05% → −0.53%. §III.B grafts a different paragraph's factor onto its own number pair.

These are mechanical, ~30-minute fixes. No new computation needed.

## Per-paper backward step (R47 oscillation cycle launch)

Honest readiness rollback after R47 launch:

| Paper | Pre-R47 | R47 backward | Post-R47 | Reasoning |
|---|---|---|---|---|
| P1A | 85% | −5pp | 80% | 1 BLOCKER (cross-paper ‡-footnote anchor + 1B §VII.H + free-w0wa-sample contradiction) + 1 MAJOR (H-O branch count off-by-one) |
| P1B | 75% |  0  | 75% | excluded from R47 |
| P2  | 83% | −7pp | 76% | 1 BLOCKER (Table 4 vs Table 5 BF disagreement) + 3 MAJORs (3×6 SVD rank check missing, Table 4 row 4 vs row 5 internal contradiction, abstract bispectrum-only headline-vs-joint-Fisher) |
| P3  | 89% | −5pp | 84% | 0 BLOCKERs but 2 MAJORs (limitations vs abstract 17.8% framing inconsistency, data-availability ACT-quarantine contradiction) |
| P4  | 86% | −6pp | 80% | 0 BLOCKERs but 3 NEW MAJORs from ZZZZ+AAAAA propagation failures (Conclusion #1 stale 2.75σ, Conclusion #2 single-number factor-of-9, §III.B 3.86× math mismatch) — FLAT vs R46, sharper backward step than P3 |
| **Average** | **83.6%** | **−4.6pp** | **79.0%** | **smaller backward step than R46 (−5.6pp)** |

**Cycle convergence visible:** R45 launch backward step was −9.2pp; R46 was −5.6pp (40% smaller); R47 is −4.6pp (18% smaller). Per-round backward is shrinking. Two more rounds at this convergence rate would bring the per-round backward step to ~3pp, at which point the <3 BLOCKER + <5 MAJOR exit condition becomes plausibly reachable.

## Wave-letter assignments for closing R47 findings

- **Wave 14-CCCCC:** P1A v1A.0.12 → v1A.0.13 R47 BLOCKER B1 (CROSS-PAPER) — coordinated edit landing P1A footnote re-anchor + P1B §VII.H content addition (DESI DR2 w0wa chain status disclosure) in single commit. P1B will bump v1B.0.2 → v1B.0.3 inside the same commit.
- **Wave 14-DDDDD:** P2 v1.7.19 → v1.7.20 R47 BLOCKER B1 (Table 4 vs Table 5 BF reconciliation) + 3 MAJORs (3×6 SVD rank check, Table 4 row 4 vs row 5, abstract headline-vs-joint-Fisher).
- **Wave 14-EEEEE:** P3 v3.1.30 → v3.1.31 R47 2 MAJORs (limitations 17.8% framing, data-availability parquet path).
- **Wave 14-FFFFF:** P4 v1.0.38 → v1.0.39 R47 3 MAJORs (Conclusion #1 stale 2.75σ → −0.12σ, Conclusion #2 single-number → range, §III.B 3.86× → 3.04× or recompute eq-suppressed pair).
- **Wave 14-GGGGG:** R47 minors+nits sweep (13 minors + 7 nits across all 4 papers).
- **Wave 14-HHHHH:** launch R48 multi-agent adversarial review on post-GGGGG versions — THIRD CONVERGENCE TEST. If R47 + R48 both find <3 BLOCKER + <5 MAJOR, the cross-vendor non-Anthropic R-round can launch.

Continuing R47 → Rn loop until per-round delta meets the <3 BLOCKER + <5 MAJOR exit condition for two consecutive rounds. Then cross-vendor non-Anthropic R-round (GPT-5/Gemini-3.1-Pro/Grok-4/Perplexity) per memory feedback_cross_model_peer_review.md. Then Houston sign-off + arXiv submission.

## R47 review artifact metadata

- **Launched:** 2026-05-09 09:00 PT (Wave 14-BBBBB)
- **Subagents:** 4 parallel Claude general-purpose subagents
- **Versions reviewed:** P1A v1A.0.12, P2 v1.7.19, P3 v3.1.30, P4 v1.0.38
- **P1B excluded:** compute-gated on cobaya R̂−1 < 0.01 (currently 0.076)
- **Source:** local on-disk .tex at commit 7a907a67 (Wave 14-AAAAA)
- **Total findings:** 31 (2 BLOCKER + 9 MAJOR + 13 MINOR + 7 NIT)
- **Net delta vs R46:** −1 BLOCKER, −6 MAJOR, −1 MINOR, −2 NIT, −10 total (−24%)
- **Loop convergence status:** **CONVERGING and accelerating** (R44→R45 0%, R45→R46 −18%, R46→R47 −24%). Per-round backward step shrinking ~18% (R46 −5.6pp → R47 −4.6pp). Exit condition <3 BLOCKER + <5 MAJOR plausibly 1-2 more rounds away.
