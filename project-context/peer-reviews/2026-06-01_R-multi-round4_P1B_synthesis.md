# P1B R-multi-round4 — synthesis

**Date**: 2026-06-01
**Paper**: P1B Technical Verification Companion (`arxiv/paper1b_mcmc_companion.tex`)
**Version reviewed**: v1B.0.33
**Version after closure**: v1B.0.34
**Round vendors**: Grok-4 (direct), gpt-4o (direct, fallback from gpt-5), Perplexity Sonar Pro (direct). Gemini-2.5-pro skipped on billing failure.
**Protocol**: `feedback_peer_review_truth_audit_protocol` — per-finding truth-audit before any closure.

---

## Aggregate

| Reviewer | Findings | BLOCKER | MAJOR | minor |
|---|---|---|---|---|
| Grok-4 (brutal) | 6 | 0 | 2 (B1, B2) | 4 |
| GPT-4o (methodology) | 6 | 0 | 0 | 6 |
| Perplexity Sonar Pro (citations) | 6 | 0 | 4 (B1, B2, M1, M2) | 2 |
| **Total** | **18** | **0** | **6** | **12** |

---

## Truth-audit verdicts

| Reviewer–ID | Verdict | Evidence |
|---|---|---|
| GRO-B1 (narrative-hedging cross-check) | OPINION | Auxiliary cross-check + 3.6σ headline both retained by design (in-cell caveats visibility rule from v1B.0.27 cascade) |
| GRO-B2 (iter2 P1A-anchor framing) | STALE | Table caption already labels "data product for P1A §Structural Tension"; v1B.0.30 R28-GRO-B2 push-back closure |
| GRO-B3 (redundant scope disclaimers ×5) | OPINION | Redundant disclaimers retained per Technical Verification Companion scope; "in-cell caveats win on visibility" rule |
| GRO-B4 (ALP MCMC adds no ECH verification value) | STALE | §VI L946 already says "not a distinctive ECH prediction"; abstract L305-306 same; v1B.0.31 GRO-B3 push-back |
| GRO-B5 (source preamble audit log) | OPINION | Stripped at arXiv bundle stage by standing protocol; v1B.0.28 R28-GRO-B5 "no action required" closure |
| GRO-B6 (LiteBIRD ~9σ forecast unsubstantiated) | OPINION | LiteBIRD design sensitivity 0.03° ≈ 5×10⁻⁴ rad is canonical collaboration target; standard literature claim |
| GPT-B1 (ln B missing) | STALE | Table app:claims row "Model-comparison ΔAIC/BIC/ln B — Omitted (pending v1B.0.18+ Nested Sampling)"; fn:wcaveat says "Savage-Dickey not viable at this tail depth" |
| GPT-B2 (NaMaster validation framing) | STALE | Abstract L298-301 + §IV scope-note L668-673 both label as pipeline-validation, not sky-detection |
| GPT-B3 (ALP rationale) | STALE | §VI ALP subsection explicitly says "not a distinctive ECH prediction" |
| GPT-B4 (AIC/BIC/ln B omission) | STALE | Same as GPT-B1; deferred-by-design item in Table app:claims |
| GPT-B5 (error propagation through systematic budget) | STALE | fn:wcaveat already discloses tail-extrapolation vs frequentist tension distinction |
| GPT-B6 (citation/attribution precision) | STALE | Cascade rounds 1–3 already closed every concrete attribution gap surfaced |
| PER4-B1 (Liu et al. ECTorsionDESI2025 doesn't exist) | STALE | references.bib L571-579 has the real Liu+Li+Xu+Biesiada+Wang EPJC 2025 arXiv 2507.04265 entry; Perplexity web-search consistently fails to resolve this preprint |
| **PER4-B2 (Eskilt2022b dataset mis-labelled "PR3")** | **VERIFIED** | External verification against the Eskilt & Komatsu 2022 public reproduction repository ([github.com/LilleJohs/Cosmic_Birefringence](https://github.com/LilleJohs/Cosmic_Birefringence)) README: "The detector split maps of Planck Data Release 4 (NPIPE) can be found on NERSC". Eskilt & Komatsu 2022 used **Planck PR4 NPIPE + WMAP9**, NOT PR3. Round-3 closure (PER3-B2 fix "PR4 NPIPE + WMAP" → "WMAP9 + Planck 2018 (PR3)") introduced a regression. v1B.0.32 original phrasing "PR4 NPIPE + WMAP" was correct; v1B.0.33 over-corrected. **Note**: Perplexity's proposed fix ("Planck 2018 PR3 only") is also wrong — the right answer is PR4 NPIPE + WMAP9. |
| PER4-M1 (DiegoPalazuelos2025 ACT DR6 doesn't exist) | STALE | references.bib L444-466 has DiegoPalazuelos+Komatsu 2025 (arXiv 2509.13654); round-1 PER-B3 FALSIFIED on same grounds; round-3 PER3-B3 STALE same grounds |
| PER4-M2 (ACT DR6 β=0.215±0.074° label) | STALE | Same disambiguation thread as PER3-M2; already in §VI L825 and L982 |
| PER4-m1 (LiteBIRD 0.03° units citation) | OPINION | Canonical LiteBIRD sensitivity target; round-3 PER3-B6 OPINION same grounds |
| PER4-m2 (ALP MCMC custom-likelihood-stack provenance) | OPINION | §VI L996 already labels "our internal model-independent MCMC fit"; provenance explicit |

**Totals**: 1 VERIFIED / 12 STALE / 5 OPINION / 0 BLOCKER outstanding.

---

## Closure (v1B.0.34)

**Single VERIFIED fix**: PER4-B2 (Eskilt2022b dataset label).

**Site**: `arxiv/paper1b_mcmc_companion.tex` line 951.

**Change**: "the joint WMAP9 + Planck 2018 (PR3) analysis" → "the joint WMAP9 + Planck PR4/NPIPE analysis".

**External verification** (cited in the v1B.0.34 audit-log block): The Eskilt & Komatsu 2022 (arXiv:2205.13962) public reproduction code at [github.com/LilleJohs/Cosmic_Birefringence](https://github.com/LilleJohs/Cosmic_Birefringence) confirms the paper analyzes Planck PR4 NPIPE detector-split maps jointly with WMAP9, NOT Planck PR3 2018.

**Rebuild**:
- `cd arxiv && pdflatex -interaction=nonstopmode -halt-on-error paper1b_mcmc_companion.tex` × 3 → 11 pages, 0 undefined refs.
- Mirror: `site/public/papers/paper1b_mcmc_companion.pdf` (700,113 bytes) + `paper1b_mcmc_companion_v1B.0.34.pdf`.
- Convex bump: pending caller invocation of `/bigbounce-bump` (MCP not loaded in this triage session).

---

## Cascaded-R-rounds telemetry

Across four rounds the same dataset-attribution sentence has now been corrected three times:

| Round | Before | After | Verdict |
|---|---|---|---|
| Round 1 closure (v1B.0.31) | "joint Planck+ACT value" | (no fix; round-1 FALSIFIED on bib-existence grounds) | Missed prose-attribution defect |
| Round 2 closure (v1B.0.32) | "joint Planck+ACT value" | "joint WMAP+Planck value (the PR4 NPIPE + WMAP analysis; ACT DR6 enters only via the separate DiegoPalazuelos2025 measurement)" | VERIFIED prose-attribution fix |
| Round 3 closure (v1B.0.33) | "PR4 NPIPE + WMAP analysis" | "WMAP9 + Planck 2018 (PR3) analysis" | VERIFIED — but **introduced a NEW dataset-label regression** |
| Round 4 closure (v1B.0.34) | "WMAP9 + Planck 2018 (PR3) analysis" | "WMAP9 + Planck PR4/NPIPE analysis" | VERIFIED via external code-repo cross-check |

**Lesson**: When correcting dataset labels in closure prose, always cross-check against the cited paper's public code artifacts (repo / ancillary files / NASA-ADS metadata). Round-3 swung from one mis-labelled extreme to another because the truth-audit relied on neighbouring-paper context rather than verifying against Eskilt & Komatsu's actual reproduction code. Pattern baked into v1B.0.34 audit-log entry for future closures.

---

## Clean-vendor counter

- **Round 4**: 0 of 3 vendors fully clean (Grok 6 opinions, GPT 6 stale, Perplexity 1 VERIFIED + 5 stale/opinion).
- **Counter**: 0/3 streak on v1B.0.34. New streak begins on next round.
- **99%-gate**: NOT yet cleared; need 3+ of 5 vendors convergent-silent across one round per `cascaded-r-rounds` skill exit criterion.

---

## Next round

- Restamp PDF metadata + Convex bump via `/bigbounce-bump`.
- Dispatch fresh cascaded round 5 against v1B.0.34 (`tools/cross_vendor_review_direct.py` with the 3 vendors that responded; retry Gemini once billing clears).
- If round 5 returns convergent silence across 3+ vendors AND no novel BLOCKER/MAJOR, exit cascade and queue for arXiv submission per `cascaded-r-rounds` exit criterion.
