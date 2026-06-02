# P1B R-multi-round6 — synthesis

**Date**: 2026-06-01
**Paper**: P1B Technical Verification Companion (`arxiv/paper1b_mcmc_companion.tex`)
**Version reviewed**: v1B.0.34
**Version after closure**: v1B.0.34 (no bump; 0 VERIFIED)
**Round vendors**: Grok-4 (direct), gpt-4o (direct, fallback from gpt-5), Perplexity Sonar Pro (direct). Gemini-2.5-pro skipped.
**Protocol**: `feedback_peer_review_truth_audit_protocol` — per-finding truth-audit before any closure.

---

## Aggregate

| Reviewer | Findings | BLOCKER | MAJOR | minor |
|---|---|---|---|---|
| Grok-4 (brutal) | 6 | 2 (B1-B2) | 3 (B3-B5) | 1 (B6) |
| GPT-4o (methodology) | 6 | 0 | 0 (framed as "issue/fix" without severity, treated as MAJOR-equivalent) | 6 |
| Perplexity Sonar Pro (citations) | 6 | 1 (B1) | 3 (M1-M3) | 2 |
| **Total** | **18** | **3** | **6** | **9** |

---

## Truth-audit verdicts

| Reviewer–ID | Verdict | Evidence |
|---|---|---|
| GRO-B1 (preamble audit log) | OPINION | Stripped at arXiv bundle stage; same as v1B.0.28 R28-GRO-B5, round-4 GRO-B5, round-5 GRO-B1 |
| GRO-B2 (retitle "not an ECH test") | OPINION | Companion-paper scope by design; same as round-5 GRO-B2 |
| GRO-B3 (iter2 ±4.3σ to appendix) | OPINION | fn:wcaveat already labels as non-Bayesian tail extrapolation; same as round-5 GRO-B4 |
| GRO-B4 (NaMaster SNR delete) | OPINION | Abstract + §IV already disclaim pipeline-validation vs sky-detection; framing is intentional. Same as round-5 GPT-B2 |
| GRO-B5 (delete or appendix §VI ALP) | STALE | §VI explicitly says "not a distinctive ECH prediction"; same as round-5 GRO-B5, round-4 GRO-B4, round-3 GRO-B3 |
| GRO-B6 (delete cross-paper table) | OPINION | SSOT-mirror meta-Author note; same as round-5 GRO-B6 |
| GPT-B1 (ΔNeff proxy derivation) | STALE | §I/§III scope notes already state companion paper does null-consistency, no torsion mods; same as round-5 GPT-B1 |
| GPT-B2 (NaMaster SNR calc explanation) | STALE | Abstract L298-301 + §IV scope-note L668-673 already explain; same as round-5 GPT-B2 |
| GPT-B3 (AIC/BIC/ln B inconsistency impact) | STALE | Table app:claims explicitly defers Nested Sampling to v1B.0.18+; explicit deferred-by-design; same as round-5 GPT-B5 |
| GPT-B4 (ALP-not-ECH context+refs) | STALE | §VI L997-1001 already cites Fujita2021 + flags non-distinctive; same as round-5 GPT-B3 |
| GPT-B5 (MCMC compute resources) | OPINION | Reproducibility appendix already points to GitHub manifest; cost-per-config is project-management detail |
| GPT-B6 (claims-table verification criteria) | OPINION | Table app:claims already has Status column with VERIFIED/PARTIAL/DEFERRED; criteria implicit in source-line citations |
| **PER6-B1 (Eskilt2022b PR4/NPIPE → PR3 REVERSE)** | **FALSIFIED** | L1004-1006 current text reads "joint WMAP9 + Planck PR4/NPIPE analysis"; matches Eskilt reproduction repo github.com/LilleJohs/Cosmic_Birefringence ("Planck Data Release 4 (NPIPE)"). Reviewer's proposed "fix" to PR3 is exactly the round-3 regression that round-4 corrected. **No action — accepting would re-introduce round-3 regression. Third consecutive round Perplexity has confidently mis-attributed Eskilt; in-tex audit-log block L65-99 documents the oscillation.** |
| PER6-M1 (NaMaster NPIPE blurs with PR3) | OPINION | §IV NaMaster runs on Commander map (component-separated); β-injection comparisons against Eskilt2022b (correctly labelled PR4/NPIPE) + DiegoPalazuelos2025 ACT DR6 are separately attributed; not blurred. Premise that Eskilt is PR3 is itself FALSIFIED per PER6-B1 |
| PER6-M2 (Liu ECTorsionDESI2025 arXiv 2507.04265 not real) | STALE | references.bib L571-579 has the real entry; flagged round-1 PER-B1 FALSIFIED, round-2 same, round-3 same, round-4 same, round-5 PER5-M2 STALE |
| PER6-M3 (DiegoPalazuelos2025 ACT DR6 arXiv 2509.13654 not real) | STALE | references.bib L444-466 has the entry; flagged round-1 PER-B3 FALSIFIED, round-3 PER3-B3, round-4 PER4-M1, round-5 PER5-M3 |
| PER6-m1 (Fujita "previously studied" softer) | OPINION | §VI L1001 already cites Fujita2021 as model-class precedent, not exact equivalence |
| PER6-nit1 (LiteBIRD σ(β)≈0.03° anchor) | OPINION | Canonical LiteBIRD design target; round-3 PER3-B6 OPINION, round-4 PER4-m1, round-5 PER5-m1 same grounds |

**Totals**: 0 VERIFIED / 6 STALE / 11 OPINION / 1 FALSIFIED / 0 BLOCKER outstanding.

---

## Closure (v1B.0.34 stands)

**Zero VERIFIED findings.** No version bump. No recompile. No PDF mirror. No Convex bump.

**Persistent-vigilance dispatch confirmed**: Perplexity BLOCKER-1 (proposing PR4/NPIPE → PR3 reversion, third consecutive round) was truth-audited against the Eskilt reproduction repo per Houston's explicit directive. The reviewer was wrong; current v1B.0.34 phrasing at L1004-1006 ("joint WMAP9 + Planck PR4/NPIPE analysis") matches the repo and is correct. Accepting the reviewer's "fix" would re-introduce the round-3 regression. The in-tex audit-log block (L65-99) documents the full oscillation history and is performing exactly its intended function: future rounds (and this one) reject the same mis-attribution without rebuilding.

---

## Cascaded-R-rounds telemetry

| Round | Eskilt label state | Vendor clean | Counter |
|---|---|---|---|
| Round 4 closure (v1B.0.34) | corrected back to "PR4/NPIPE" via repo cross-check | 0/3 | 0/3 |
| Round 5 (v1B.0.34) | stable; reviewer-proposed reversion FALSIFIED | 0/3 substantive, 0 novel BLOCKER | 1/3 |
| **Round 6 (this round, v1B.0.34)** | **stable; reviewer-proposed reversion FALSIFIED again** | **0/3 substantive, 0 novel BLOCKER** | **2/3** |

**Convergence signal**: All 18 findings collapsed to STALE / OPINION / FALSIFIED. No novel BLOCKER, no novel MAJOR. Cross-round overlap is now near-total — Grok, GPT, and Perplexity are re-raising prior-round verdicts with near-identical wording. The Eskilt thread is stable across three rounds.

---

## Clean-vendor counter

- **Round 6**: 0 of 3 vendors fully clean by raw count, but 0 of 18 findings survive truth-audit. Convergent-silent round.
- **Counter advances**: **2/3** on v1B.0.34.
- **99%-gate**: One more convergent-silent round at v1B.0.34 to exit cascade.

---

## Next round

- No rebuild; v1B.0.34 stands.
- Dispatch round 7 against v1B.0.34 (retry Gemini if available, else 3-vendor set).
- If one more round returns convergent-silent (counter 3/3), exit cascade and queue P1B for arXiv submission per `cascaded-r-rounds` exit criterion.
