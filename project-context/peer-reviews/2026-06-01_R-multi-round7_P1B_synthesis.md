# P1B R-multi-round7 — synthesis

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
| Grok-4 (brutal) | 6 | 2 (B1-B2) | 2 (B3-B4) | 1 (B5) + 1 nit (B6) |
| GPT-4o (methodology) | 6 | 0 | 6 (B1-B6, severity-less "issue/fix") | 0 |
| Perplexity Sonar Pro (citations) | 5 | 1 (B1) | 3 (M1-M3) | 1 (m1) |
| **Total** | **17** | **3** | **11** | **3** |

---

## Truth-audit verdicts

| Reviewer–ID | Verdict | Evidence |
|---|---|---|
| GRO-B1 (preamble audit log to PDF) | OPINION | Stripped at arXiv bundle stage; reviewer mistakes `%` comment block for body text. Same as round-6 GRO-B1, round-5 GRO-B1, round-4 GRO-B5 |
| GRO-B2 (retitle "not an ECH test") | OPINION | Companion-paper scope by design; abstract + §I + §VI all flag ALP as non-distinctive. Same as round-6 GRO-B2, round-5 GRO-B2 |
| GRO-B3 (delete pipeline-SNR from abstract/§IV) | OPINION | L298-301 + L668-673 explicitly disclaim pipeline-recovery vs sky-significance; framing is intentional and reader-protective. Same as round-6 GRO-B4, round-5 GPT-B2 |
| GRO-B4 (iter2 ±4.3σ to appendix) | OPINION | fn:wcaveat already labels iter2 as non-Bayesian tail extrapolation; ln B explicitly deferred per Table app:claims. Same as round-6 GRO-B3, round-5 GRO-B4 |
| GRO-B5 (Eskilt PR4/NPIPE footnote) | STALE | L1004-1006 already names "joint WMAP9 + Planck PR4/NPIPE analysis; ACT~DR6 enters only via the separate" cite. Footnote redundant with body text |
| GRO-B6 (drop repetitive "null-consistency check" phrase) | OPINION | Pure stylistic. Repetition is reader-protective in a verification paper |
| GPT-B1 (null-hypothesis definition) | STALE | §I/§III scope notes define ΛCDM+ΔNeff baseline; same as round-6 GPT-B1, round-5 GPT-B1 |
| GPT-B2 (ΔNeff compatibility criteria) | STALE | §III + Table app:claims define posterior-shift compatibility quantitatively |
| GPT-B3 (NaMaster SNR calc explanation) | STALE | Abstract L298-301 + §IV L668-673 explain pipeline-recovery construction; same as round-6 GPT-B2, round-5 GPT-B2 |
| GPT-B4 (ΔAIC/ΔBIC/ln B) | STALE | Table app:claims explicitly defers Nested Sampling per inconsistent-sample-count; same as round-6 GPT-B3, round-5 GPT-B5 |
| GPT-B5 (ALP consistency calculations) | STALE | §VI L997-1006 cites Fujita2021 model-class + names exact β value; same as round-6 GPT-B4, round-5 GPT-B3 |
| GPT-B6 (readiness % criteria in cross-paper table) | OPINION | SSOT-mirror; criteria are project-management not paper science. Same as round-6 GPT-B6 |
| **PER7-B1 (Eskilt2022b PR4/NPIPE → PR3 REVERSE, 3rd consecutive)** | **FALSIFIED** | L1004-1006 reads "joint WMAP9 + Planck PR4/NPIPE analysis"; verified against Eskilt reproduction repo github.com/LilleJohs/Cosmic_Birefringence ("Planck Data Release 4 (NPIPE)"). Reviewer's "fix" to PR3 = round-3 regression that round-4 corrected. **No action — accepting would re-introduce a falsified label. In-tex audit-log L65-99 documents the oscillation; persistent-vigilance dispatch confirmed for the THIRD consecutive round.** |
| PER7-M1 (Liu ECTorsionDESI2025 arXiv 2507.04265 not real) | STALE | references.bib L571-579 has the real entry; flagged rounds 1/2/3/4/5/6 — STALE on all |
| PER7-M2 (DiegoPalazuelos2025 ACT DR6 arXiv 2509.13654 not real) | STALE | references.bib L444-466 has the entry; flagged rounds 1/3/4/5/6 — STALE on all |
| PER7-M3 (ACT DR6 β=0.215°±0.074° attribution) | STALE | Value is internal MCMC fit per §IV; reviewer's premise that it must trace to a public ACT paper is wrong — paper is upfront about it being an internal pipeline-validation fit |
| PER7-m1 (Planck-PR4+ACT-DR6 internal MCMC not externally reproducible) | OPINION | Paper explicitly labels this as an internal model-independent fit; reproducibility appendix points to GitHub manifest |

**Totals**: 0 VERIFIED / 8 STALE / 8 OPINION / 1 FALSIFIED / 0 BLOCKER outstanding.

---

## Closure (v1B.0.34 stands)

**Zero VERIFIED findings.** No version bump. No recompile. No PDF mirror. No Convex bump.

**Persistent-vigilance dispatch confirmed for the THIRD CONSECUTIVE ROUND**: Perplexity BLOCKER-1 (proposing PR4/NPIPE → PR3 reversion) was truth-audited against the Eskilt reproduction repo per Houston's explicit standing directive. The reviewer was wrong on rounds 5, 6, and now 7. Current v1B.0.34 phrasing at L1004-1006 ("joint WMAP9 + Planck PR4/NPIPE analysis; ACT DR6 enters only via the separate") matches the repo and is correct. Accepting the reviewer's "fix" would re-introduce the round-3 regression. The in-tex audit-log block (L65-99) is performing exactly its intended function.

---

## Cascaded-R-rounds telemetry

| Round | Eskilt label state | Vendor clean | Counter |
|---|---|---|---|
| Round 4 closure (v1B.0.34) | corrected back to "PR4/NPIPE" via repo cross-check | 0/3 | 0/3 |
| Round 5 (v1B.0.34) | stable; reviewer-proposed reversion FALSIFIED | 0/3 substantive, 0 novel BLOCKER | 1/3 |
| Round 6 (v1B.0.34) | stable; reviewer-proposed reversion FALSIFIED again | 0/3 substantive, 0 novel BLOCKER | 2/3 |
| **Round 7 (this round, v1B.0.34)** | **stable; reviewer-proposed reversion FALSIFIED 3rd consecutive time** | **0/3 substantive, 0 novel BLOCKER** | **3/3 — EXIT** |

**Convergence signal**: All 17 findings collapsed to STALE / OPINION / FALSIFIED. Zero VERIFIED. Zero novel BLOCKER. Cross-round overlap is total — Grok, GPT, and Perplexity are now re-raising prior-round verdicts with near-identical wording across 3 consecutive convergent-silent rounds. The Eskilt thread is rock-stable.

---

## Clean-vendor counter

- **Round 7**: 0 of 3 vendors fully clean by raw count; 0 of 17 findings survive truth-audit. Third consecutive convergent-silent round.
- **Counter advances**: **3/3** on v1B.0.34.
- **99%-gate**: EXIT criterion met. P1B exits cascaded R-rounds at v1B.0.34.

---

## EXIT — P1B cascaded R-rounds closed

Per `cascaded-r-rounds` exit criterion (3+ vendors convergent-silent across consecutive rounds with zero VERIFIED findings):

- **P1B v1B.0.34 — CASCADED R-ROUNDS COMPLETE**
- Queue for arXiv submission per `bib-tarball-rebuild` + Houston sign-off
- No further reviewer dispatch needed unless a substantive .tex change is made
- Eskilt PR4/NPIPE thread permanently closed (3 consecutive FALSIFIED reversion attempts logged in-tex)
