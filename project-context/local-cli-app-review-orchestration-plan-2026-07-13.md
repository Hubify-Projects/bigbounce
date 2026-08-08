# Local CLI/App Review Orchestration Plan

**Date:** 2026-07-13  
**Status:** shareable planning note; no paper claims, reviewer verdicts, PDFs, tarballs, site readiness values, or public artifacts changed.  
**Purpose:** capture the intended shift from browser-only external review toward a reproducible local CLI/app + browser EXT hybrid, so the next development/design agent can implement against the same operating model.

## Executive Decision

Do not replace browser ChatGPT/Gemini/Grok external review with local CLIs or desktop apps. Replace the old mental model with a stricter two-lane protocol:

1. **Local CLI/app lanes are INT lanes.** They are best for reproducibility, source inspection, dataset access, shell/API access, test execution, and exact closure evidence.
2. **Browser/app chat lanes remain EXT lanes.** They are best for fresh-reader simulation: what a capable outside reviewer sees when handed the PDF, prompt, public links, and no privileged repo context.
3. **CMUX or another multi-agent orchestrator may coordinate both lanes, but must preserve provenance.** The orchestrator can dispatch, collect, normalize, and ledger findings; it must not collapse local-source findings and browser-fresh-reader findings into one undifferentiated verdict.

The goal is not "browser vs API vs CLI." The goal is evidence diversity with clean audit trails.

## Why The Browser Reviews Were Valuable

The browser ChatGPT/Gemini/Grok workflow was not fundamentally wrong. It measured a real thing: how a fresh, strong, non-local reviewer reacts to the artifact package as a referee-like reader.

That absence of full repo context is partly the point. A journal referee usually does not get the private codebase, all local experiments, the closure history, and every SSOT note. Browser EXT review is therefore useful as a harsh public-artifact test.

But browser review is weak as a reproducibility tool. It has hidden product harnesses, changing model snapshots, opaque file parsing, inconsistent retrieval behavior, possible memory/session contamination, and limited local execution. Treat it as observed reviewer behavior, not as a pinned scientific instrument.

## Boundary Definitions

| Lane | Surfaces | Access | Use | Verdict Weight |
|---|---|---|---|---|
| `INT-local` | Codex desktop/app, Codex CLI, Claude Code, Gemini CLI, Grok Build, local scripts | repo, source, datasets, shell, APIs, tests | truth-audit, recomputation, code review, artifact hashing, closure evidence | strongest for factual correctness |
| `INT-api` | pinned vendor APIs through review scripts | controlled prompt/model settings, native PDF where available | cross-vendor repeatability and structured comparisons | strong when model/version/input modality is logged |
| `EXT-browser` | ChatGPT web/app, Gemini web/app, Grok web/app | PDF/public links/prompt only | fresh-referee simulation and public artifact clarity | strong for presentation/referee reaction; weak for reproducibility |
| `EXT-human` | Houston/human referee/journal | real scientific judgment | final authority and publication gate | decisive |

Same model family can land in different lanes. Codex with local repo access is `INT-local`; ChatGPT browser with only the PDF is `EXT-browser`.

## Current Vendor-Surface Notes

These are implementation notes, not guarantees. Recheck vendor docs before wiring hard assumptions into automation.

- OpenAI Codex can be used through ChatGPT plan surfaces, including local clients, with usage drawing from plan/agentic usage or credits depending on plan and seat configuration. This makes it attractive as a local INT lane, but not "free API." See OpenAI Help: `https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan`.
- Gemini CLI supports Google-account OAuth and local tool use, with documented free-tier quotas and API-key/Vertex alternatives. This is a good candidate INT-local lane when the account/terms allow the intended use. See Google Gemini CLI docs: `https://google-gemini.github.io/gemini-cli/`.
- xAI Grok Build is an official terminal coding-agent surface and has subscription/free-beta language in current public materials. It is promising for INT-local diversity, but any subscription-auth automation should use only official install/auth flows. See xAI CLI page: `https://x.ai/cli`.

Do not token-scrape, cookie-hijack, or automate consumer subscription surfaces in a way that violates vendor terms. If the vendor provides a CLI login flow, use that. If the vendor provides only browser chat, keep it as a browser EXT lane and capture raw evidence.

## Recommended Operating Model

Use one director, not two competing top-level brains. The director can be Claude Code, Codex desktop/app, or CMUX depending on the active machine, but it should have one canonical task ledger and one canonical artifact packet.

Recommended default:

- **Director/orchestrator:** one frontier local agent with repo access.
- **Local OpenAI auditor:** Codex desktop/app or CLI, full source + artifact packet.
- **Local Claude/Gemini/Grok auditors:** use available CLIs/apps where terms and auth permit.
- **Browser EXT reviewers:** ChatGPT + Gemini + Grok fresh chats, with only PDF/public links/prompt.
- **Cheap workers:** hash checks, route/link checks, PDF metadata, ledger normalization, screenshot collection, grep sweeps, formatting checks.

Reserve top-tier models for planning, truth audits, derivations, contradiction resolution, and final synthesis. Use cheaper/faster workers for mechanical file walking, conversion, screenshots, route checks, and structured extraction.

## Canonical Review Packet

Every review round should start from a frozen packet:

- paper id and title
- exact PDF path
- PDF hash and page count
- source commit
- source `.tex` path
- artifact/public links
- claims ledger for the review
- known disclosed limitations
- reviewer prompt template id
- lane assignment: `INT-local`, `INT-api`, `EXT-browser`, or `EXT-human`
- allowed context: `repo+data`, `PDF-only`, `PDF+public-links`, or `public-site`

No reviewer verdict is durable unless it cites the packet id and artifact hash.

## Finding Ledger Schema

Use findings, not vibes or vote counts, as the durable unit.

```text
finding_id
paper_id
round_id
lane
surface
reviewer_label
artifact_hash
severity_claimed
category
location
claim
evidence
truth_status
required_action
closure_commit
closure_evidence
```

Suggested `truth_status` values:

- `verified`
- `partially_verified`
- `falsified`
- `stale_artifact`
- `disclosed_limitation`
- `venue_judgment`
- `style_opinion`
- `needs_human_referee`

## CMUX Footnote / Integration Path

CMUX can be useful if it acts as a provenance-preserving dispatcher, not as an opaque super-reviewer.

In the MacBook Air setup, CMUX could run as the coordination shell that:

- launches local CLI/app workers against the frozen review packet,
- assigns one worker per independent paper or lane,
- collects structured finding JSON/Markdown,
- keeps browser EXT legs separate from local INT legs,
- records raw transcripts, screenshots, hashes, model/surface labels, and command logs,
- exposes disagreements to the director instead of averaging them away.

The main CMUX risk is boundary blur: a local CLI worker with repo access is not an external reviewer, even if it uses the same vendor model as the browser reviewer. The CMUX UI should therefore label each worker by lane and context entitlement, not just by model name.

Good CMUX architecture:

- fixed review phases remain explicit: freeze packet -> fan-out -> normalize -> truth-audit -> close -> re-review -> sync site/SSOT;
- dynamic orchestration is allowed inside each phase for independent work;
- worker outputs are structured and traceable to task ids;
- failures are first-class states, not missing rows;
- browser EXT raw text/screenshots are saved immediately before any synthesis;
- the final director synthesis cites finding ids and closure evidence.

Bad CMUX architecture:

- one blended "consensus verdict" without lane labels;
- browser and local CLI outputs merged before truth audit;
- reviewer agents allowed to edit source;
- closure agents allowed to dismiss findings without source-cited evidence;
- subscription/browser automation that depends on unofficial auth extraction;
- dynamic agent choice for a fixed paper-review protocol where the order is already known.

## Pilot Plan

Run the hybrid protocol on two papers before moving the whole six-paper campaign:

- **P4:** best test of disclosed limitation vs genuine defect, because public-artifact clarity matters.
- **P2:** best test of scientific load-bearing derivation review and factor-of-two/literature consistency.

For each pilot paper:

1. Freeze the review packet.
2. Run `INT-local` Codex/Claude-equivalent with repo+data access.
3. Run one additional local CLI lane if available under official auth.
4. Run browser `EXT-browser` ChatGPT/Gemini/Grok fresh chats.
5. Do not edit during comparison.
6. Normalize all findings into the ledger.
7. Truth-audit every substantive finding.
8. Measure overlap, unique real findings, false positives, stale-artifact flags, and closure cost.

Success criterion: the hybrid pipeline finds at least as many verified real issues as browser-only review while producing cleaner closure evidence and fewer ambiguous "reviewer said" rows.

## Immediate Next Steps

1. Add a machine-readable review packet template under `project-context/templates/`.
2. Add a structured finding ledger template under `project-context/templates/`.
3. Teach the current review scripts/agents to emit lane labels and artifact hashes.
4. Run the P4/P2 pilot without changing the PDFs mid-round.
5. If CMUX is used, make lane/context labels visible in the UI and in exported logs.

## Non-Claims

This plan does not claim:

- browser chat models are identical to API or CLI models;
- browser reviews are scientifically reproducible enough to stand alone;
- subscription CLI usage replaces API usage for all workloads;
- CMUX automatically improves review quality;
- a model-count majority is a truth signal.

The core claim is narrower: local CLI/app lanes improve reproducibility, browser lanes preserve fresh-referee pressure, and a good orchestrator can coordinate both if it keeps provenance explicit.
