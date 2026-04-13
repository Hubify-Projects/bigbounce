# Lab Spec — Hubify Self-Improving Lab (Lab #2 / Meta-Lab)

**Status:** SPEC ONLY — NOT seeded · Houston will create via the platform after Lab #1 ships
**Priority:** #2
**Slug:** `hubify-meta` (working name — see §0.1)
**Target repo:** `Hubify-Labs/hubify-meta`
**Target subdomain:** `meta.hubify-labs.com` or `lab.hubify-labs.com`
**Lab Site (per PRD §53):** Auto-generated from `hubify-lab-default` template. Unique stress test: the meta-lab's public site showcases platform improvements, not scientific results. Vibe-codable via site agent chat.
**Stress-test target:** **self-improvement loops** — the lab's job is to make Hubify Labs (the platform) better
**Author:** Houston Golden + Claude
**Date:** 2026-04-08
**Linked from:** PRD §40

---

## 0. The premise

Houston's #2 lab is a **meta-lab** whose research target is the Hubify Labs platform itself. The lab's agents continuously analyze platform usage, surface bugs, propose improvements, run experiments on platform features, write the platform's docs, and ship updates. It's an AutoAgent-style self-improvement harness pointed at the product Houston is building.

This is the cleanest possible test of whether Hubify Labs works **without bias toward bounce cosmology**. If the platform can host a lab whose domain is "improving SaaS products", the architecture is genuinely domain-agnostic.

### 0.1 Naming

Working name: `hubify-meta`. Alternatives:
- `hubify-self` — clean, self-referential
- `hubify-improve` — describes the function
- `meta-lab` — most generic, but might confuse with the company Meta
- `hubify-labs-lab` — playful, Inception-style

Houston picks the final name when he creates the lab via the platform.

### 0.2 Mission + North Star

**Mission:** "Continuously improve the Hubify Labs platform — its web app, CLI, desktop apps, API, MCP server, agent harness, and documentation — by running an autonomous research loop that measures platform performance, identifies friction, prototypes improvements, and ships them."

**North Star:** **Verified novel scientific contributions per week, summed across ALL Hubify-Labs-hosted labs, weighted by N-score.** This is the platform's actual reason to exist — accelerating science. The meta-lab's job is to make this number go up, week over week.

**Why this North Star (not the obvious SaaS metrics):** Houston explicitly rejected normal SaaS north-star metrics like MAU / retention / revenue. The platform's purpose is scientific output, not engagement. The right thing to maximize is what the labs *produce*, not how much they *log in*. (If we maximize the latter, we end up with another notification-spam tool.)

---

## 1. The 5 initial Projects

### Project 1: Platform Telemetry Pipeline

**Goal:** Build a telemetry layer that captures every meaningful event in Hubify Labs (lab created, project created, experiment dispatched, contribution promoted, paper shipped, agent error, etc.) and ships it into a queryable timeline.

**Deliverable:** A working telemetry pipeline + dashboard at `hubify-labs.com/admin/telemetry` that the meta-lab orchestrator can query.

**Measurable:**
- Coverage: % of platform events captured (target: ≥ 95%)
- Latency: time from event to dashboard (target: < 30 sec)
- Cost: $/month for the telemetry infrastructure (target: < $50/mo)

### Project 2: Friction Hunter

**Goal:** Identify the top 5 friction points in the Hubify Labs UX every week. Friction = anywhere a user takes more than 3 clicks for something that should be 1 click, or any flow with > 30% drop-off.

**Deliverable:** Weekly "Friction Report" markdown delivered to the Director's standup briefing every Monday morning.

**Measurable:**
- Number of friction points identified (target: ≥ 5/week)
- Number of friction points fixed in the following week (target: ≥ 2/week — close at least 40%)
- User-reported friction (via in-app feedback widget) per week (target: trending down)

### Project 3: Agent Effectiveness Benchmark

**Goal:** Continuously benchmark every agent role (orchestrator, leads, workers, cross-provider reviewers) against a held-out task suite. Identify which agents are getting better, which are getting worse, and which models are best for which roles.

**Deliverable:** A live benchmark dashboard + a quarterly "Agent Roster Recommendation" paper that proposes role/model changes.

**Measurable:**
- Number of tasks in the held-out suite (target: ≥ 50)
- Time between full benchmark runs (target: ≤ 1 week)
- Number of model swaps recommended per quarter (target: as needed — could be 0)

### Project 4: Documentation Engine

**Goal:** Auto-maintain the public Hubify Labs documentation at `hubify-labs.com/docs` (the Mintlify subpath setup per PRD §40.17 Tier 3). Every platform change triggers a docs update task assigned to a `doc-writer-worker`.

**Deliverable:** Always-current docs. Zero stale pages. Every platform feature has a doc page.

**Measurable:**
- Doc coverage: % of platform features with a docs page (target: 100%)
- Doc freshness: median age of docs page since last update (target: < 14 days)
- Doc helpfulness: thumbs-up rate on each doc page (target: > 80%)

### Project 5: Cross-Lab Pattern Library

**Goal:** Identify patterns that appear across multiple Hubify Labs labs (e.g., "every cosmology lab uses MCMC chains" → publish a `mcmc_runner` skill that any lab can use). Build a shared skill library that benefits all labs.

**Deliverable:** A `Hubify-Labs/skills-library` repo with reusable skills, datasets, and agent templates that other labs can install.

**Measurable:**
- Number of skills in the library (target: 20+ within 6 months)
- Number of labs using each skill (target: ≥ 2 per skill, otherwise it's not actually shared)
- Time saved per skill use (estimated, target: > 1 hour saved per use)

---

## 2. Initial agent roster

| Agent | Role | Model | Tier |
|---|---|---|---|
| **hubify-meta-orchestrator** | Top-level orchestrator for the meta-lab | claude-opus-4-6 | HIGH |
| **telemetry-lead** | Owns Project 1 (telemetry pipeline) | claude-sonnet-4-6 | MED-HIGH |
| **friction-lead** | Owns Project 2 (friction hunter) | claude-sonnet-4-6 | MED-HIGH |
| **bench-lead** | Owns Project 3 (agent effectiveness benchmark) | claude-sonnet-4-6 | MED-HIGH |
| **doc-lead** | Owns Project 4 (documentation engine) | claude-sonnet-4-6 | MED-HIGH |
| **pattern-lead** | Owns Project 5 (cross-lab pattern library) | claude-sonnet-4-6 | MED-HIGH |
| **doc-writer-worker** | Writes individual docs pages | claude-haiku-4-5 | LOW-MED |
| **bench-runner-worker** | Runs the benchmark task suite | claude-haiku-4-5 | LOW |
| **friction-clicker-worker** | Replays user flows to measure click count | claude-haiku-4-5 | LOW |
| **telemetry-collector-worker** | Polls platform events | (no LLM, just a script) | n/a |
| **peer-review-gpt** (cross-lab) | Cross-provider peer review | gpt-5 | HIGH |
| **peer-review-gemini** (cross-lab) | Cross-provider peer review | gemini-2.5-pro | HIGH |

The two cross-provider peer reviewers are shared with Lab #1 (Bounce Cosmology) per the cross-lab sharing model. They bill against this lab when reviewing this lab's work.

---

## 3. Cross-lab sharing relationships

- **Reads from:** ALL other Hubify Labs labs (read-only, for telemetry + benchmark + pattern detection). The meta-lab sees everything.
- **Writes to:** None directly. Per the Lab Sovereignty Rule (§40.11), the meta-lab can only SUGGEST changes to other labs via the comm gateway. Each target lab's orchestrator decides whether to accept.
- **Public sharing:** `published-only`. The meta-lab's papers (e.g., "Agent Roster Recommendation Q3 2026") get published to `hubify-labs.com/research/`. Internal benchmarks stay private.

---

## 4. The self-improvement loop

This is the lab's heartbeat — what makes it different from a normal research lab.

**Daily loop (every 24 hours):**
1. Telemetry pipeline ingests yesterday's events
2. Friction hunter analyzes flows, generates friction candidates
3. Bench runner dispatches the agent benchmark suite
4. Pattern lead scans for emerging patterns across labs
5. Doc lead checks for stale docs
6. Orchestrator compiles the daily summary into a Director briefing

**Weekly loop (every Monday):**
1. Friction Report generated
2. Top 5 friction points become Tasks in the platform repo (`Hubify-Labs/hubify-labs`)
3. Doc lead opens PRs for any docs that need updates
4. Bench lead publishes the week's agent benchmark summary

**Quarterly loop:**
1. Agent Roster Recommendation paper drafted
2. Pattern library update — new skills get added
3. Houston (or his designated reviewer) reviews and ships

---

## 5. Initial datasets

- **Platform telemetry stream** — populated by Project 1's pipeline
- **Held-out benchmark task suite** — 50+ tasks across all agent roles, manually curated. Includes: "summarize this paper", "find the bug in this script", "review this experiment for QC issues", etc.
- **Stale-docs index** — generated daily by the doc-lead crawler

---

## 6. Bootstrap checklist (for when Houston creates the lab)

- [ ] Lab created via `/create lab hubify-meta` from the platform UI
- [ ] Mission + North Star + Director set in `lab.yaml`
- [ ] 5 Projects created with goal/deliverable/measurable
- [ ] Agent roster bootstrapped (12 agents)
- [ ] Cross-lab read access requested from all existing labs
- [ ] Telemetry pipeline deployed
- [ ] First daily loop runs successfully
- [ ] First weekly Friction Report generated
- [ ] First doc page written and shipped
- [ ] First benchmark run completed and dashboard live

---

## 7. What this lab stress-tests on the platform

| Platform feature | How this lab tests it |
|---|---|
| **Domain-agnosticism** | Lab's domain is "improving software", not "physics" — proves the platform isn't bounce-cosmology-biased |
| **Self-referential safety** | The lab proposes changes to the platform itself — tests whether the Lab Sovereignty Rule prevents runaway self-modification |
| **Cross-lab read access** | The lab needs to read every other lab's telemetry — tests the read-only-cross-lab access pattern at scale |
| **Continuous heartbeat loops** | Daily + weekly + quarterly cadences — tests the routine scheduler |
| **Multiple parallel projects** | 5 projects running concurrently — tests project isolation + resource contention handling |
| **Doc-writer-worker pattern** | A worker that writes content (not just runs scripts) — tests the writing-worker pattern that other labs will eventually use |
| **Agent benchmarks** | The bench-lead's task suite is the platform's quality gate for agent prompt changes |

---

## 8. Open questions

1. **Where does the meta-lab live physically?** Same Convex deployment as the platform itself, or a separate deployment? My recommendation: **separate deployment** (so the meta-lab can crash without taking down the platform).
2. **Who pays for the meta-lab's compute?** The meta-lab does its own LLM calls + benchmarks. Assume it bills against a Hubify-internal compute budget, separate from per-user lab budgets.
3. **Should the meta-lab have write access to the platform repo?** Initially no — the meta-lab opens PRs that humans review. Long-term, the meta-lab could earn write access for low-risk changes (docs updates, dependency bumps). Houston decides.
4. **How does the meta-lab avoid being a vanity loop?** The North Star is "verified novel scientific contributions per week, summed across labs". If the meta-lab's improvements don't move that number, the meta-lab is failing at its job. The orchestrator flags this if it happens.

---

## 9. Why this lab is the one Houston wants to build #2

Houston's quote: *"#2 is gonna be 'Hubify Lab' which will be an autonomous research lab directed by me the human director with same setup of orchestrator > leads > workers etc... but the team will actually be focused on building out a kind of AutoAgent (remember the auto improving agent harness project we discussed early on?)"*

The point: the platform isn't done when Lab #1 (Bounce Cosmology) ships. It's done when the platform can improve itself without Houston manually shipping every fix. The meta-lab is the loop that gets us there.

**This is the lab that turns Hubify Labs from a SaaS app into a living research system.**
