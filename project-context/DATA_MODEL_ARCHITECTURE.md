# Bigbounce Data Model + Skill/MCP Architecture — committed plan

**Status:** PLAN. Drafted 2026-05-29 PDT in response to Houston's pushback ("the statuses on the site all show 95%... unsynced disparate statuses/tasks/blockers... maddness for months... needs to get real organized structured and do all this properly once and for all now"). Cron `05764ea4` killed at the same time so we don't keep adding to the mess.

**Goal:** One normalized live source of truth for paper state. All surfaces (homepage, paper pages, NEEDS_HOUSTON, SSOT, in-paper status blocks, external-review prompt, R-round audit table) READ from that source. Any R-round / closure / pod lifecycle event WRITES to that source. Every Claude Code (or other) agent can use a documented MCP + skill to read/write — no more hand-editing 5 unsynced files per fire.

---

## The current pain (verbatim from Houston)

1. *"the statuses on the site all show 95% and the dates and details are so fucking confusing as hell"*
2. *"unsynced disparate statuses/tasks/blockers etc etc across the homepage and the paperpages and everything it is all conflicting and confusing AF"*
3. *"not ever up to date which it should be updated on every R-round"*
4. *"we probably need to get really serious about thinking about the actual data model for the research"*
5. *"create a proper mcp/api/skillstack ... for sure the project needs proper status, progress, whats running live updates, external prompt to copy for external review etc, and all the stuff/data etc related to managing these ongoing papers and tasks and R-rounds to drive to 100"*
6. *"connect with Convex real-time db and our projects own api/mcp that you (claude code) or any agent knows how to use bc we have a package of skills that come with the project install locally"*
7. *"nice api/mcp/skills documentaiton page for this so claude code or any other agent can also contribute"*
8. *"manage the runpods and tasks etc etc"*
9. *"get this real organized structured and do all this properly once and for all now"*

---

## The current data sprawl (what we have to consolidate)

| File / surface | What it stores | Drift mode |
|---|---|---|
| `site/src/data/papers.ts` | Paper schema, readiness, version, lastUpdated, tldr, blockingItems, status (long), description, keyResults, surveys, predictions, figures, remainingWork, preprintId, pdfMeta, artifacts | Hand-edited every fire. Readiness drifts; version+lastUpdated forgotten ~50% of fires. |
| `site/src/data/live-status.ts` | Top-level lastUpdatedISO, lastUpdatedDisplay, big homepage headline string, per-paper {version, readiness, pendingWork string} | Duplicates 4 of the papers.ts fields. Drifts. |
| `site/src/app/papers/[slug]/page.tsx` | Hardcoded per-paper `focusAreas` array used to build the external-review prompt | Drifts. Found stale references to old sample counts (309K vs 425K) on 2026-05-29. |
| `project-context/SSOT/index.md` | Cross-paper dashboard (one-line per paper, readiness %, gaps) | Stale; drift from papers.ts within hours. |
| `project-context/SSOT/paper-N/status.md` | Per-paper detail + close-the-gap section | Stale; markdown text drift. |
| `project-context/SSOT/queue.md` | Open tasks, owners, machine-checkable criteria | Stale; 100KB+ append-only log. |
| `project-context/SSOT/drive-to-100.md` | Plan doc + loop log | Mixed plan and log; stale phases retained for "audit trail." |
| `project-context/NEEDS_HOUSTON.md` | Truly-blocked items (Houston-only) | Hand-edited. Drifts. |
| `pipelines/p3_anomaly_engine/paper3_draft.tex` (and 5 others) | Comment block at top of .tex (lines 1-300) with full version-history closure log | 300+ lines per paper, embedded in source, would ship to arXiv if uncommented. Grok-nit 2026-05-29: "Delete the entire block before arXiv upload." |
| `project-context/peer-reviews/*.md` | R-round per-vendor outputs (200+ files) | Append-only, no index, no findings-table normalization. |
| `pipelines/p3_anomaly_engine/r42_results/*.json` | On-disk artifacts (Savage-Dickey, BigAE-IF intersection, etc.) | Authoritative for the science but disconnected from paper-state tracking. |
| `pipelines/*/pod_runs/*.log` | Pod-run history | Free-form. Pod costs / artifacts / status not tracked in any structured form. |

**That's 10+ surfaces holding partially-redundant paper state, none of them normalized, none of them live-synced. Every fire I do has to update 3-7 of them by hand.** This is why "all show 95%" — when I forget to update one of them, the homepage shows a stale number.

---

## The target architecture

### Layer 1 — Convex schema (canonical source of truth)

Convex is Houston's chosen real-time DB (per `project_hubify_labs_compute`). It gives us:

- TypeScript-first schema with zod-style validation
- Real-time subscriptions (site re-renders on mutation, no manual `lastUpdated` field needed)
- Functions = mutations/queries (no separate API server)
- Free tier sufficient for this scale (~6 papers × dozens of R-rounds × hundreds of findings)

**Tables:**

```typescript
// convex/schema.ts (proposed)

papers: defineTable({
  slug: v.string(),               // "paper-1a"
  number: v.string(),             // "1A"
  title: v.string(),
  shortTitle: v.string(),
  targetJournal: v.union(v.literal("PRD"), v.literal("MNRAS"), v.literal("JCAP"), v.literal("ApJ")),
  status: v.union(
    v.literal("paused-houston-external"),  // P1A + P4 right now
    v.literal("active-drive-to-100"),       // P1B + P2 + P3 + P5 right now
    v.literal("submitted-arxiv"),
    v.literal("in-revision"),
    v.literal("accepted")
  ),
  // Readiness is COMPUTED from open findings count (see below), not hand-set.
  // Manual override only via houston_sign_off field below.
  houstonSignOff: v.optional(v.string()),  // ISO date when Houston says "ship it"
  currentVersion: v.id("paper_versions"),
})
.index("by_slug", ["slug"]),

paper_versions: defineTable({
  paperId: v.id("papers"),
  version: v.string(),            // "v1A.0.36"
  datestamp: v.string(),          // "2026-05-28"
  texCommit: v.string(),          // git SHA of the .tex file
  pdfMd5: v.string(),
  pdfPages: v.number(),
  pdfSizeBytes: v.number(),
  changelog: v.string(),          // short single-paragraph human summary
  arxivTarballPath: v.optional(v.string()),
  arxivTarballSizeBytes: v.optional(v.number()),
})
.index("by_paper", ["paperId"]),

r_rounds: defineTable({
  paperId: v.id("papers"),
  paperVersion: v.string(),        // version this round reviewed
  roundLabel: v.string(),          // "2026-05-29_R-direct-v1b"
  dispatchedAt: v.number(),        // unix ms
  source: v.union(v.literal("openrouter"), v.literal("direct"), v.literal("subagent"), v.literal("houston-external")),
  vendors: v.array(v.string()),    // ["openai/gpt-5", "google/gemini-2.5-pro", ...]
})
.index("by_paper", ["paperId"]),

findings: defineTable({
  roundId: v.id("r_rounds"),
  reviewerName: v.string(),        // "Gemini25Pro_cosmology"
  findingId: v.string(),           // "PAPER-GRO-M2"
  classification: v.union(v.literal("BLOCKER"), v.literal("MAJOR"), v.literal("MINOR"), v.literal("NIT")),
  location: v.string(),            // "§sec:fnl L310" or "abstract"
  claim: v.string(),
  proposedFix: v.string(),
  // Truth-audit verdict (per feedback_peer_review_truth_audit_protocol):
  truthAudit: v.optional(v.union(
    v.literal("VERIFIED"),         // claim accurate, fix needed
    v.literal("FALSIFIED"),        // claim wrong, no fix needed
    v.literal("STALE"),            // claim was true earlier but already closed
    v.literal("OUT-OF-SCOPE")
  )),
  // Closure state (only after truthAudit set):
  closureStatus: v.union(
    v.literal("open"),
    v.literal("in-progress"),
    v.literal("closed-by-real-action"),
    v.literal("closed-by-truth-audit-falsification"),
    v.literal("deferred-genuine")  // VERY rare; needs explicit Houston OK
  ),
  closureCommit: v.optional(v.string()),
  closureArtifact: v.optional(v.string()),   // path to JSON/script that proves closure
  closedAt: v.optional(v.number()),
})
.index("by_round", ["roundId"])
.index("by_paper", ["paperId"]),

pathc_caveats: defineTable({   // separate from R-round findings: these are paper-internal
  paperId: v.id("papers"),
  label: v.string(),             // "b", "d", "f", "g", "h", etc.
  description: v.string(),
  status: v.union(v.literal("open"), v.literal("deferred"), v.literal("closed")),
  closureMethod: v.optional(v.union(
    v.literal("real-computation"),
    v.literal("artifact-verification"),
    v.literal("truth-audit-falsification"),
    v.literal("text-only-no-real-action")  // FLAG — this is the caveat-as-closure anti-pattern Houston called out
  )),
  closureArtifact: v.optional(v.string()),
  closureCommit: v.optional(v.string()),
})
.index("by_paper", ["paperId"]),

pods: defineTable({
  podId: v.string(),             // RunPod ID, e.g. "ijzftpy3klystt"
  name: v.string(),
  status: v.union(v.literal("running"), v.literal("exited"), v.literal("terminated")),
  gpu: v.string(),
  volumeGb: v.number(),
  containerGb: v.number(),
  hourlyCost: v.number(),
  startedAt: v.number(),
  stoppedAt: v.optional(v.number()),
  totalCostUsd: v.number(),
  purpose: v.string(),           // human description
  artifactsBackedUp: v.boolean(),
  backupLocations: v.array(v.string()),  // ["HF: bamfai/...", "local: reproducibility/..."]
})
.index("by_pod_id", ["podId"]),

tasks: defineTable({
  paperId: v.optional(v.id("papers")),  // null for cross-paper / infrastructure tasks
  title: v.string(),
  description: v.string(),
  priority: v.union(v.literal("P0"), v.literal("P1"), v.literal("P2")),
  owner: v.union(v.literal("agent"), v.literal("houston")),
  status: v.union(v.literal("pending"), v.literal("in-progress"), v.literal("blocked"), v.literal("done")),
  blockedBy: v.optional(v.array(v.id("tasks"))),
  createdAt: v.number(),
  closedAt: v.optional(v.number()),
  closureCommit: v.optional(v.string()),
}),

// Computed read-only view (Convex query, not a table):
//   getPaperState(slug) → {
//     ...paper, currentVersion, openFindingsCount, openCaveatsCount,
//     readinessComputed: 95 - 2*openBlockers - 1*openMajors - 0.2*openMinors,
//     readinessFloor: capped at 95 pre-houstonSignOff,
//     externalReviewPrompt: generated from focusAreas in paper + open caveats,
//     lastUpdated: max(currentVersion.datestamp, latest closed finding date)
//   }
```

**Readiness becomes a computed field.** It is never hand-set. It is `95 - 2·openBlockers - 1·openMajors - 0.2·openMinors`, capped at the 95-floor pre-Houston-sign-off (per `feedback_99_pct_readiness_cap`). This eliminates the "I forgot to bump readiness after closing 4 items" drift Houston caught today.

### Layer 2 — MCP server (`bigbounce-mcp`)

Local stdio MCP server installed at `bigbounce/mcp/`. Loaded into Claude Code (and any other MCP-aware agent) per-project via `.claude/mcp_servers.json`:

```json
{
  "mcpServers": {
    "bigbounce": {
      "command": "node",
      "args": ["./mcp/bigbounce-mcp/dist/index.js"]
    }
  }
}
```

**Exposed tools:**

| Tool | Purpose |
|---|---|
| `bigbounce.list_papers()` | Read-only list of all 6 papers w/ computed state |
| `bigbounce.get_paper(slug)` | Full state for one paper |
| `bigbounce.list_open_findings(paperSlug?)` | Open findings across paper(s), filterable |
| `bigbounce.start_r_round(paperSlug, source="direct")` | Dispatches `cross_vendor_review_direct.py` + writes results to Convex |
| `bigbounce.truth_audit_finding(findingId, verdict, evidence)` | Apply truth-audit verdict per protocol |
| `bigbounce.close_finding(findingId, method, commit, artifact)` | Atomic mutation when real-action closure lands |
| `bigbounce.bump_paper_version(slug, newVersion, pdfPath, changelog)` | Single mutation that updates version + datestamp + pdfMd5/pages/size; computes readiness |
| `bigbounce.list_pods()` | RunPod state (uses RUNPOD_API_KEY) |
| `bigbounce.start_pod(spec)` / `bigbounce.stop_pod(id)` / `bigbounce.terminate_pod(id)` | Pod lifecycle with cost accounting written to Convex |
| `bigbounce.list_tasks(filter)` / `bigbounce.create_task(...)` / `bigbounce.close_task(...)` | Task management |
| `bigbounce.get_external_review_prompt(slug)` | Returns the canonical prompt for Houston's copy/paste, generated from current paper state (focus areas + open caveats + version + pdfMeta) |

### Layer 3 — Skill package (`bigbounce-skills/`)

Per-project skills auto-discovered by Claude Code via `bigbounce/.claude/skills/`. Each skill wraps an MCP tool with the right ergonomics:

| Skill | What it does |
|---|---|
| `/bigbounce-status` | Calls `list_papers()`, prints structured dashboard |
| `/bigbounce-r-round <slug>` | Calls `start_r_round`, waits, prints findings |
| `/bigbounce-close <findingId> <method> <artifact>` | Calls `close_finding` |
| `/bigbounce-bump <slug> <version> <pdfPath>` | Calls `bump_paper_version` |
| `/bigbounce-pod <action>` | Pod lifecycle (list / start / stop / terminate) |
| `/bigbounce-review-prompt <slug>` | Prints the copy/paste prompt for external review |

These supersede the current ad-hoc fires. A drive-to-100 fire becomes: `/bigbounce-status` → pick highest-priority open finding → `/bigbounce-close` → done. No more hand-editing 5 files.

### Layer 4 — Site refactor (live from Convex)

Replace `site/src/data/papers.ts` + `site/src/data/live-status.ts` with a Convex `useQuery` hook. Homepage re-renders on every mutation. Per-paper page generates the external-review prompt server-side from current Convex state. The hardcoded `focusAreas` array in `page.tsx` goes away — replaced by a `paper.focusAreas` field stored in Convex.

### Layer 5 — Docs page (`/api` on the site)

Auto-generated from MCP tool registry. Any external agent or human can read:

- Schema definitions
- Tool catalog
- Example invocations
- Auth / setup instructions

This is what Houston means by *"nice api/mcp/skills documentation page for this so claude code or any other agent can also contribute"*.

---

## Phased build plan

**Pause on drive-to-100 closures until at least Phase 1 + Phase 2 land.** Adding more closures to the broken system makes migration harder.

### Phase 0 — TODAY (this commit)

- [x] Bump P3 readiness 85 → 89 (honest reflection of 5 §pathc_caveats closures landed today)
- [x] Write this architecture plan
- [x] Kill drive-to-100 cron `05764ea4`
- [ ] Commit + push

### Phase 1 — Convex setup + schema (4-6 hours)

- [x] `npx convex dev` initialize in `bigbounce/convex/` — **already done 2026-04-06** (existing `./convex/` dir with 12 .ts files: schema/galaxies/analytics/chatMessages/spectralResults/feedback/pipelineState/models/mcmcStatus/reviews/activityFeed/checklist + `_generated/`). Site `package.json` has `convex@^1.34.1`. Live deployment may need re-auth via `npx convex dev` once when Houston is at the terminal — flagged in NEEDS_HOUSTON if hit. **DISCOVERED ALREADY-DONE during rebuild fire #1 2026-05-29.**
- [x] Write `convex/schema.ts` per the tables above — **rebuild fire #1 2026-05-29**: extended existing schema with 7 new tables for paper-level orchestration (`papers`, `paper_versions`, `r_rounds`, `findings`, `pathc_caveats`, `pods`, `tasks`). Additive only; the 9 existing tables (galaxies/reviews/checklistItems/pipelineState/models/chatMessages/activityFeed/mcmcStatus/spectralResults/pageViews) are untouched. Typechecks clean via `tsc --noEmit`.
- [ ] Write all mutations + queries (per-table CRUD + the computed `getPaperState(slug)` view that derives readiness from open findings)
- [ ] Migration script: read current `papers.ts` / `live-status.ts` / SSOT files / `pathc_caveats` from .tex files → write to Convex
- [ ] Verify: `bigbounce.list_papers()` query returns 6 papers with computed readiness matching today's honest numbers

### Phase 2 — MCP server (6-8 hours)

- [ ] Scaffold `bigbounce/mcp/bigbounce-mcp/` as a TypeScript MCP server (stdio)
- [ ] Implement the 10 tools above
- [ ] Test: invoke from Claude Code session, verify each tool works end-to-end
- [ ] Add to `bigbounce/.claude/mcp_servers.json` so it auto-loads

### Phase 3 — Skill package (4 hours)

- [ ] Create `bigbounce/.claude/skills/bigbounce-status/SKILL.md`, etc.
- [ ] Each skill wraps the corresponding MCP tool
- [ ] First real fire under the new system: `/bigbounce-r-round paper-1b` (first time P1B has been touched)

### Phase 4 — Site refactor (6-8 hours)

- [ ] Add `@convex-dev/react` to site
- [ ] Replace `papers.ts` import in all pages with `useQuery(api.papers.list)`
- [ ] Replace hardcoded `focusAreas` in `page.tsx` with `paper.focusAreas` from Convex
- [ ] Delete `papers.ts` + `live-status.ts` (now Convex-backed)
- [ ] Verify: every paper page renders correctly, readiness matches Convex

### Phase 5 — Docs page (2 hours)

- [ ] Generate MCP tool catalog as static markdown in site
- [ ] Add `/api` route with schema + tool list + examples
- [ ] Link from homepage and CLAUDE.md

### Phase 6 — Cleanup (2 hours)

- [ ] Move .tex comment-block status histories to Convex `paper_versions.changelog`
- [ ] Strip the .tex comment blocks (Grok-nit closure)
- [ ] Archive old SSOT/queue.md and SSOT/drive-to-100.md (their data is now in Convex)
- [ ] Update CLAUDE.md to point at Convex + MCP as canonical, with old SSOT/* as deprecated

**Total: 24-30 hours of focused work. Probably 2 full days at the current pace.** During that time, no new paper closures — the cron stays off.

---

## What the world looks like after this lands

- **One source of truth**: Convex tables. Every surface reads from there. Nothing drifts because nothing is hand-edited per-surface anymore.
- **Real-time updates**: When I close a finding, the site re-renders within seconds. Houston sees the change live.
- **Readiness is honest**: Computed from open findings, not hand-set. Can't accidentally leave a paper at 95% after closing nothing.
- **Any agent can contribute**: MCP + skill package + docs page mean another Claude Code session (or Codex, or Cursor) can pick up open findings without reading 10 markdown files first.
- **Pod tracking is real**: Pods have a structured lifecycle with cost accounting and backup verification. No more "1 RUNNING pod, what's even on it?" mystery.
- **External review prompts auto-generated**: Houston's copy/paste prompt for each paper is generated server-side from current state. No more "P1B says 424,781 samples but the canonical is 309,189" drift.
- **R-rounds are first-class**: Each round writes its findings as structured rows. Truth-audit verdicts are tracked. No finding gets "closed by caveat-as-closure" without a flag.
- **Houston gets the management dashboard he's been wanting**: `/api` page + per-paper live state + ongoing R-round queue + pod status + open-tasks list. All visible at https://bigbounce.hubify.app and via `/bigbounce-status` from any agent session.

---

## What this DOES NOT do

- It does not write new science. The Convex DB stores state; the .tex files remain the canonical paper source. The MCP/skills make it easier to track who closed what when, not easier to discover real physics.
- It does not replace human judgment. Houston sign-off remains the final 1%. Truth-audit verdicts still require Claude reasoning. The architecture removes mechanical drift, not the requirement to do real work.
- It does not eliminate the cron entirely. Once Phase 4 lands, a drive-to-100 cron can resume — but its fires will be Convex-backed (single mutation per closure, no 5-file hand-edit), so drift becomes structurally impossible.

---

## Why now and not after the papers ship

Houston's question implicitly: *"why are you stopping closures to build infrastructure?"* The answer:

1. **The closures stopped landing cleanly.** Of today's 8 fires, at least 2 (fires #1, #5) required me to fix drift in adjacent files I'd forgotten. The drift compounds; each fire takes longer than the last.
2. **The papers are mostly ship-ready already.** P1A + P4 sit at 95 pending Houston external review. P3 is at 89 with 4 open §pathc_caveats. P1B/P2/P5 have not been touched today but their actual closure work is mostly text edits. The remaining honest-science items (P3-(c) full Fisher, P3-(e) GR projection, P1B coupled-Friedmann) are 1-day-each tasks that benefit from being tracked in Convex from day one rather than added to the markdown sprawl.
3. **External review is the next big unblock.** When Houston's external reviews on P1A + P4 come back with findings, those findings need to land in the system cleanly. Doing that into the current 10-surface mess will produce more drift, not less. The Convex+MCP infrastructure makes external-review intake atomic.
4. **Houston explicitly asked.** *"get this real organized structured and do all this properly once and for all now."* That's the directive.

---

**Next agent / next session: start Phase 1.** The first action is `npx convex dev` in `bigbounce/convex/` + writing the schema above. No more drive-to-100 fires until Phase 1 + Phase 2 land.
