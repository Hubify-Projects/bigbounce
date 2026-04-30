# Peer Reviews — Navigation Index

This directory tracks every adversarial peer review (LLM panels and external reviewers) for all 4 BigBounce papers, organized by round.

**Master tracker:** [`REVISION_TRACKER.md`](REVISION_TRACKER.md) — round-by-round summary, finding counts, closure status.

**Standing protocol** for handling new reviews: [`../houston-method-v2.md`](../houston-method-v2.md) Principles 12 (take critiques seriously) + 13 (PDF restamp protocol).

---

## Active round

**[`r42/`](r42/)** — R42+ adversarial multi-agent review (2026-04-30 onward, currently being collected)

**[`master/2026-04-30_R42_master.md`](master/2026-04-30_R42_master.md)** — running R42+ master log; summary of R34-R41 master appended at the bottom for context.

---

## Master adversarial logs (consolidated, multi-round)

| File | Rounds covered | Status | Date |
|---|---|---|---|
| [`master/2026-04-27_R34-R41_master.md`](master/2026-04-27_R34-R41_master.md) | R34-R41 — 5 parallel Opus agents + cross-LLM consensus (ChatGPT Deep Think, Grok Heavy, Gemini) — 80+ findings, 28 cross-cite removals, P1 negative-rhetoric reframe | CLOSED 2026-04-30 (R41) | 2026-04-27 → 2026-04-30 |
| [`master/2026-04-30_R42_master.md`](master/2026-04-30_R42_master.md) | R42+ | OPEN | 2026-04-30 |

---

## Round-specific reviews (single-round, per-paper)

### R31-R32 (2026-04-29) — Late-stage individual paper audits
| File | Paper | Reviewer |
|---|---|---|
| [`r31_paper1_2026-04-29.md`](r31_paper1_2026-04-29.md) | P1 spin-torsion | Hostile adversarial, Claude Opus 4.7 |
| [`r31_paper2_2026-04-29.md`](r31_paper2_2026-04-29.md) | P2 fNL forecast | Hostile adversarial, Claude Opus 4.7 |
| [`r31_paper3_2026-04-29.md`](r31_paper3_2026-04-29.md) | P3 anomaly catalog | Hostile adversarial, Claude Opus 4.7 |
| [`r31_paper4_2026-04-29.md`](r31_paper4_2026-04-29.md) | P4 chirality catalog | Hostile adversarial, Claude Opus 4.7 |
| [`r31_site_2026-04-29.md`](r31_site_2026-04-29.md) | Site (bigbounce.hubify.app) | Hostile adversarial, Claude Opus 4.7 |
| [`r32_paper2_2026-04-29.md`](r32_paper2_2026-04-29.md) | P2 (deferred-LOW closure pass) | Hostile adversarial, Claude Opus 4.7 |

### Autonomous review (2026-04-18) — 6-agent panel + arXiv production editor
[`autonomous-2026-04-18/`](autonomous-2026-04-18/) — 7 files (per-paper grumpy referees + cross-paper theorist + arXiv production editor + arXiv ID substitution plan)

### Foundation audits (2026-03) — v1.0 and product-architecture passes
| File | Scope |
|---|---|
| [`2026-03-02_1917PST_claims-table.md`](2026-03-02_1917PST_claims-table.md) | Claims-table audit |
| [`2026-03-02_1917PST_comprehensive-audit.md`](2026-03-02_1917PST_comprehensive-audit.md) | Comprehensive v1.0 audit |
| [`2026-03-04_0000PST_v1.0-research-issues.md`](2026-03-04_0000PST_v1.0-research-issues.md) | v1.0 research issues |
| [`2026-03-11_0000PST_product-architecture-audit.md`](2026-03-11_0000PST_product-architecture-audit.md) | Product/architecture audit v1 |
| [`2026-03-12_0000PST_product-architecture-audit-v2.md`](2026-03-12_0000PST_product-architecture-audit-v2.md) | Product/architecture audit v2 |

---

## How to add a new round

When new peer-review feedback (LLM panel, external reviewer, or human) arrives:

1. **If single-round, single-paper:** drop in directly under `peer-reviews/` as `r{N}_paper{K}_YYYY-MM-DD.md`.
2. **If multi-paper, multi-agent panel:** create `peer-reviews/r{N}/` subfolder with one file per reviewer/paper.
3. **Always:** append a row to the relevant master file (`master/2026-04-30_R42_master.md` for R42+) with classification (BLOCKER/MAJOR/MINOR/REJECTED-AS-WRONG) and disposition (FIX-FULL / FIX-EDIT / NO-OP-WITH-CITATION).
4. **Open the fix queue** in `../SSOT/queue.md` with one row per actionable finding.
5. **Close the round** with the standing PDF restamp bundle (Principle 13 — recompile + restamp + version-bump + mirror + site-sync, single commit).

---

## Triage classification system (R42+)

Every finding gets one of these labels at the top of the master file, surfaced by severity:

| Label | Meaning | Disposition |
|---|---|---|
| 🔴 BLOCKER | Cannot ship without full fix; requires retrain / rerun / regenerate / redo MCMC | Open queue row, plan H200 hours, execute end-to-end |
| 🟠 MAJOR | Substantive edit required; rewrite section, add appendix, recompute statistic | Open queue row, schedule for current round |
| 🟡 MINOR | Wording or clarification edit | Open queue row, batch with other minors |
| ⚪ REJECTED-AS-WRONG | Reviewer staleness or context-gap; cite file/data/code that proves it | Document in master file with citation; no edit |

**Default for ambiguous cases is BLOCKER, not MINOR.** See Principle 12 in `houston-method-v2.md`.
