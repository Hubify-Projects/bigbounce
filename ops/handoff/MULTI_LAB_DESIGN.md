# Multi-Lab Independent-Replication Design (post-MVP blueprint)

**Status:** DESIGN-ONLY. Nothing here is wired in. This is the blueprint for
*after* the two-machine MVP proves out. Do not implement any part of this until
the single-lab two-machine loop is stable and Houston green-lights phase 1.

**Author:** Claude Fable 5, on Houston's vision.
**Guardrail Houston set:** *"I don't want to overcomplicate things that are
already not fully working."* — every phase below has a hard entry gate; you do
not skip ahead, and you do not fork into two labs until the single lab is
boring-reliable.

---

## 0. Houston's vision (verbatim, honored)

> "running the orchestrator and reproducing the same research in different
> environments with different orchestrators... two parallel research labs in
> tandem, communicate with each other, try to reproduce the same results...
> multiple frontier-leading orchestrators as well as open-source leading
> orchestrators trying to reproduce the science... fully cloned research labs
> running in parallel and strategically sharing versus not sharing to most
> effectively not cross-contaminate results... helping each other but not overly
> influencing each other."

The whole design is a formalization of one sentence in that quote:
**strategically sharing versus not sharing to most effectively not
cross-contaminate results.** Everything below is the mechanism for "help each
other but don't overly influence each other."

---

## 1. Why — the scientific case

Independent replication is the strongest evidence class in empirical science.
The bigbounce program's residual gap is **not a content gap** — per
`project-context/PROCESS_AUDIT_2026-07-14.md` §1, content is converged and
genuinely-new real defects surface at ~1 per 10 waves. The residual gap is the
**pattern-066 verdict-word floor**: the same byte-identical PDF draws
ACCEPT→MINOR→MAJOR→MINOR from one LLM referee and REJECT↔MAJOR from another
across consecutive waves with zero content change. More text waves do not move
the verdict word — this is measured, not asserted.

That floor is a direct symptom of the **LLM self-review ceiling**: a single
family of reasoning systems reviewing its own program cannot escape its own
structural biases, no matter how many waves you run. The strongest available
answer to that critique is not "run more reviews" — it is **independent
methodological replication**:

- Two agentic labs, **different orchestrator models** (different reasoning
  systems), **same data and pipeline** (same science), reproduce the same
  numeric results.
- If Lab A (Claude/Fable) and Lab B (Codex/GPT), and later Lab C (an
  open-source harness), independently land the same f_NL, the same anomaly
  count, the same mirror-flip asymmetry — that is genuine replication, not
  self-agreement. Divergence is *equally* valuable: it localizes a real
  method/seed/data sensitivity that a single lab would have rationalized away.
- This converts the program's headline from "our LLM referees eventually stop
  finding new defects" (a ceiling) to "the results reproduce across independent
  reasoning systems" (a floor of evidence). It is the one lever that attacks the
  self-review critique at its root instead of relitigating verdict words.

**Non-goal:** this is not about getting more ACCEPT verdicts. It is about
producing replication evidence. Verdict farming remains banned (directives K/L/M).

---

## 2. Lab definition

A **lab** is a fully-specified, self-contained reproduction unit:

| Component | Definition | Notes |
|---|---|---|
| **Orchestrator model** | The planning/judgment brain (Fable, GPT-5.x, Qwen-Coder, DeepSeek-based harness) | The defining axis — different orchestrators = different reasoning systems |
| **Subagent pool** | Worker models the orchestrator fans out to | Can differ per lab; recorded in the lab manifest |
| **Working branch / fork** | `lab/<labId>/...` branches off the shared tagged start-state | One lab never writes to another lab's branch namespace |
| **Convex namespace** | A `labId` field on live tables (schema sketch §3.4) | Live dashboards filter by `labId`; no cross-lab overwrite |
| **Review battery sessions** | The lab's own INT/EXT sessions, raws, dispositions | Sealed during blind phase (§3) |
| **Lab manifest** | `exchange/labs/<labId>.json` — orchestrator id, subagent pool, host stack, capabilities, start-tag | Declares what the lab can/can't do |

### 2.1 Lab roster (pragmatic capability notes)

| Lab | Orchestrator | INT (API reviews) | EXT (browser reviews) | Pipeline re-run | GPU |
|---|---|---|---|---|---|
| **Lab A — Fable** (frontier) | Claude Code / Fable | Yes (host-agnostic APIs) | Yes — has gstack headed browser | Yes | RunPod |
| **Lab B — Codex** (frontier) | Codex / GPT-5.x | Yes | Only if gstack stack present on its host; else INT-only | Yes | RunPod |
| **Lab C — OSS** (open-source) | Qwen/DeepSeek agent harness | Yes (any host-agnostic API it can call) | **No** unless it can drive gstack; assume INT-only | Yes (code is host-agnostic) | RunPod if wired |

**Capability truths to bake in:**
- **INT API reviews are host-agnostic** — any lab that can make HTTPS calls to
  OpenAI/XAI/Gemini/Anthropic-equivalent endpoints can run the INT battery. The
  Claude INT leg is the *running orchestrator itself on subscription* (CLAUDE.md
  I1), so each lab's "Claude-equivalent INT leg" is *its own orchestrator*, not
  a shared API. This is a feature: it keeps INT genuinely independent per lab.
- **EXT browser reviews need the gstack headed-browser stack** (CLAUDE.md I4).
  A lab without it cannot run verifiable EXT. Do **not** fake EXT for a lab that
  lacks the stack — mark its EXT column `N/A (no browser stack)` on the grid.
- **Pipeline code is host-agnostic** — any lab can reproduce a pipeline cell
  given the tagged commit + pinned data. This is the shared substrate that makes
  replication meaningful.

---

## 3. Isolation protocol (anti-contamination) — the crux

The whole value of multi-lab collapses if the labs contaminate each other. The
rule is: **share the inputs, seal the process, reveal the outputs.**

### 3.1 SHARED (identical across labs, pinned, immutable during a round)

- **Raw input data** — pinned HuggingFace release tags (dataset revision hash,
  not `main`). Both labs load byte-identical inputs.
- **Pipeline code** at a **tagged commit** (`repro/<target>/<tag>`). No lab
  edits pipeline logic mid-round.
- **Paper PDFs** at their tagged versions (the object under replication).
- **Acceptance-test definitions** — the numeric cells to reproduce + their
  tolerances, written *before* the round (`exchange/targets/<target>.md`).

### 3.2 NOT SHARED during a round (sealed until reveal)

- Intermediate results (partial arrays, per-seed outputs, logs)
- Adjudication verdicts and review raws
- Dispositions and truth-audit conclusions
- Analysis choices (which estimator, which cut, which seed-averaging scheme) —
  each lab makes these independently; convergent *choices* are themselves a
  replication signal.

### 3.3 Blind-phase → reveal-phase cycle (cryptographic pre-registration)

```
  t0  Both labs start from the SAME tagged state (repro/<target>/<tag>).
      Same pinned data. Same acceptance-test defs. No contact on process.

  ── BLIND PHASE ──────────────────────────────────────────────
  Each lab independently runs the target, produces a results manifest
  (the numeric cells + method notes), and computes SHA-256 over the
  canonicalized results file.

  Each lab commits ONLY its hash to exchange/seals/<target>/<labId>.sha256
  BEFORE seeing the other lab's results. This is a commit-reveal:
  the sealed hash is a cryptographic pre-registration of the result.

  A round's reveal gate = every participating lab has pushed its .sha256.

  ── REVEAL PHASE ─────────────────────────────────────────────
  Only after all seals are in, each lab pushes its full results file
  to exchange/reveals/<target>/<labId>.json. The orchestrator (or a
  neutral adjudicator agent) verifies each revealed file hashes to its
  pre-committed seal — proving no lab tuned its result after seeing the
  other's. THEN the corroboration protocol (§4) runs.
```

The commit-reveal makes "I got the same number" *falsifiable*: a lab cannot
retroactively claim agreement, because its hash was fixed before it could see
the other's number.

### 3.4 Contamination classes and their controls

| Class | What leaks | Control |
|---|---|---|
| **Verdict leakage** | Lab B sees Lab A's ACCEPT/REJECT and anchors to it | Verdicts live in each lab's sealed session; never in shared branches until reveal; the grid shows per-lab verdicts side-by-side, never a merged verdict pre-reveal |
| **Prompt leakage** | Labs converge on identical review/analysis prompts, killing independence | Each lab owns its prompt set in its own branch; the shared `exchange/` carries *targets and tolerances only*, never prompts; prompt divergence is logged in the lab manifest |
| **Fix leakage** | Lab A's paper edit / bug-fix propagates to Lab B mid-round, so they're no longer reproducing the *same* start-state independently | The start-state is a frozen tag; fixes discovered mid-round go into a **post-reveal** merge queue (§4), applied to the shared paper only after both labs independently surfaced or reviewed them |

**Golden rule:** during the blind phase, the only bytes that cross between labs
are the pinned inputs (which were identical to begin with) and the sealed
hashes. Nothing else.

### 3.5 Convex schema addition (SKETCH — do not implement)

Current live tables (`convex/schema.ts`): `papers`, `readinessMetrics`,
`papers_externalReviews`, `activityFeed`, `r_rounds`, `findings`, etc. The
multi-lab addition is a single optional field plus a labs table:

```ts
// SKETCH — additive, backward-compatible. Absent labId == "lab-a" (default lab).
labs: defineTable({
  labId: v.string(),            // "lab-a" | "lab-b" | "lab-c"
  displayName: v.string(),      // "Fable (frontier)"
  orchestrator: v.string(),     // "claude-code/fable"
  tier: v.string(),             // "frontier" | "open-source"
  capabilities: v.object({      // what the grid may render for this lab
    intReviews: v.boolean(),
    extBrowser: v.boolean(),
    pipelineReRun: v.boolean(),
    gpu: v.boolean(),
  }),
  startTag: v.string(),         // repro/<target>/<tag> this lab is bound to
}).index("by_labId", ["labId"]),

// Add an OPTIONAL labId to the live tables (default -> "lab-a" so all
// existing rows/queries keep working unchanged):
//   readinessMetrics:      + labId: v.optional(v.string())
//   papers_externalReviews:+ labId: v.optional(v.string())
//   activityFeed:          + labId: v.optional(v.string())
//   r_rounds:              + labId: v.optional(v.string())
// New indexes: .index("by_lab_paper", ["labId", "paperId"]) where applicable.
```

No mutation is rewritten in this doc. When implemented, the default-to-`lab-a`
rule means the single-lab MVP data stays valid with zero migration.

---

## 4. Corroboration protocol (post-reveal)

Once seals are verified and results are revealed:

1. **Numeric comparison against stated tolerances.** For each acceptance-test
   cell, compare Lab A vs Lab B values against the tolerance declared *before*
   the round (`exchange/targets/<target>.md`). Within tolerance = **corroborated**.
2. **On divergence → structured disagreement doc.**
   `exchange/disagreements/<target>-<cell>.md` captures both values, both method
   notes, and a root-cause hypothesis tree: **data?** (pin mismatch — check
   dataset revision hash) → **seed?** (RNG/seed policy differs) → **method?**
   (estimator/cut/averaging choice differs).
3. **Both labs re-run the disputed cell** under a controlled variation (e.g.
   both fix the seed, or both adopt the other's estimator) to localize the
   source. This is a *joint* diagnostic and may happen with limited, logged
   sharing — the disputed cell only, never the whole result set.
4. **Verdicts/dispositions merge only AFTER independent adjudication.** Each
   lab's truth-audit stands on its own. A finding is merged into the shared
   paper only when both labs have independently reviewed it (or one surfaced it
   and the other confirmed it against source). **Disagreements are preserved,
   not averaged away** — a "Lab A: MINOR / Lab B: ACCEPT" cell is recorded as a
   disagreement, which is *more* informative than a blended number. Averaging
   verdict words would launder exactly the independence we're paying for.

Integrity rules from CLAUDE.md I1–I6 and directives K/L/M apply unchanged inside
every lab: never fake an ACCEPT, never fabricate, every leg saves its raw before
any verdict is recorded, dispositions stay source-cited.

---

## 5. Communication bus

Deliberately minimal — git + a small exchange dir + Convex:

- **Git branches per lab:** `lab/<labId>/...` for each lab's working state;
  `repro/<target>/<tag>` for the frozen shared start-states. Labs never push to
  each other's `lab/` namespace.
- **`exchange/` directory** (the only cross-lab channel):
  ```
  exchange/
    labs/<labId>.json            # lab manifest (orchestrator, capabilities)
    targets/<target>.md          # acceptance-test defs + tolerances (shared, pre-round)
    seals/<target>/<labId>.sha256    # blind-phase commit (hash only)
    reveals/<target>/<labId>.json    # reveal-phase full results
    disagreements/<target>-<cell>.md # structured disagreement docs
    comparisons/<target>.md          # post-reveal corroboration summary
  ```
  The `seals/` files are the pre-registration; `reveals/` are gated on all seals
  being present.
- **Convex `labId`** for live dashboards (§3.5): each lab writes its own rows;
  the site reads all labs and renders them side-by-side. No lab overwrites
  another's readiness/verdict rows.

---

## 6. Site support (SKETCH — component/data-shape notes only)

For a future implementation ticket, not now.

- **/reviews grid gains a lab dimension.** Today the grid is
  `paper × reviewer-leg → verdict` (newest rounds LEFT, per directive M). The
  multi-lab grid adds a lab axis:
  - Per-lab CURRENT columns: `paper × (lab, reviewer-leg) → verdict`, grouped by
    lab so Lab A's block sits beside Lab B's block.
  - A **cross-lab agreement meter** per paper: a small badge/bar summarizing
    corroboration state — e.g. `corroborated (within tol)`, `divergent (1 cell)`,
    `blind (sealed, awaiting reveal)`. Data shape: `{ paperId, labIds[],
    agreement: "corroborated"|"divergent"|"blind", divergentCells: string[] }`,
    derived from `exchange/comparisons/<target>.md` (or a Convex mirror).
  - The all-A terminal criterion (directive M) generalizes: exit shows ACCEPT
    across every paper × reviewer **per lab**, and a corroborated cross-lab meter.
- **Overview gains a lab roster + reproduction-status panel.** Data shape:
  `labs[] = { labId, displayName, orchestrator, tier, capabilities }` plus a
  `reproductionTargets[] = { target, labIds, status, corroborated }`. Render as
  one clean section shell (no nested-card stacks, per Houston's UI prefs): a lab
  roster row-list, then a reproduction-status row-list, spacing/dividers not
  bordered cards.

No components are written here. This is the contract a future ticket implements.

---

## 7. MVP → multi-lab migration path

Hard entry gates. Do not advance a phase until its gate is green. Honors
*"don't overcomplicate what isn't fully working."*

### Phase 0 — NOW: two machines, ONE lab
- **State:** two machines, single Fable lab, the existing single-lab loop.
- **Entry gate:** (this is where we are)
- **Exit gate → phase 1:** every machine-checkable item in
  `ops/handoff/HANDOFF_SYNC.md` §"Phase-0 acceptance test" passes: one lease
  winner, failover, machine-attributed heartbeats, tracked cron/watchdog
  deployment, one unattended full wave with single adjudication and
  raw+screenshot capture, same-commit Convex/site/SSOT consistency, clean site
  build/freshness check, and no duplicate browser/verdict work.

### Phase 1 — Second orchestrator (Codex), SAME lab, division of labor
- **What:** Codex/GPT joins as a *second orchestrator inside the same lab* — no
  isolation yet. Pure division of labor (e.g. Codex owns open-compute closures,
  Fable owns adjudication), sharing freely. This de-risks two-orchestrator
  operations *before* adding the isolation machinery.
- **Entry gate:** phase 0 exit green.
- **Exit gate → phase 2:** two orchestrators co-drive the loop without write
  contention or double-driving (per `feedback_cron_tick_overlap_detection` —
  overlap detection proven); Convex/site stay consistent under two writers.

### Phase 2 — Fork into TWO true labs, blind-phase protocol on ONE bounded target
- **Chosen phase-2 reproduction target: P4 end-to-end mirror-flip re-run.**
  Rationale: it is **cheap, objective, and numeric** — a single mirror-flip
  asymmetry statistic on a fixed catalog, reproducible from the tagged pipeline
  + pinned HF data in bounded compute, with an unambiguous number to compare
  against a stated tolerance. No prose-verdict subjectivity to muddy the first
  independence test. (It's also live in the open-compute tail as P4 image-level
  injection, so the replication doubles as real science.)
- **What:** Lab A (Fable) and Lab B (Codex) each independently reproduce the P4
  mirror-flip statistic from `repro/p4-mirror-flip/<tag>` + pinned data, run the
  full blind→reveal cycle (§3.3), and corroborate (§4). Convex `labId` and the
  side-by-side grid (§6) light up for this one target.
- **Entry gate:** phase 1 exit green; `exchange/` scaffolding + seal/reveal
  tooling built and dry-run tested; Convex `labId` schema addition landed
  (default-to-`lab-a`, zero migration).
- **Exit gate → phase 3:** at least one full blind→reveal→corroborate cycle
  completes on P4 with either a corroborated result *or* a structured
  disagreement doc that localizes root cause — i.e. the machinery demonstrably
  works, regardless of whether the two labs agreed.

### Phase 3 — Open-source lab (Lab C)
- **What:** add a Qwen/DeepSeek-based agent harness as Lab C. INT-only unless it
  can drive gstack (mark EXT `N/A` otherwise). It reproduces the same P4 target,
  then broadens to other targets in the open-compute tail.
- **Entry gate:** phase 2 exit green; Lab C harness can load pinned data + run
  the tagged pipeline cell + emit a results manifest + seal/reveal.
- **Exit gate:** Lab C completes a blind→reveal→corroborate cycle on P4; the
  three-lab grid renders; reproduction status is live on the site.

---

## 8. Cost / effort (human-team vs CC+gstack)

| Task | Human team | CC+gstack | Compression |
|---|---|---|---|
| `exchange/` bus + seal/reveal (SHA-256 commit-reveal) tooling | 3 days | ~30 min | ~140x |
| Convex `labId` schema addition + default-to-lab-a migration | 1 day | ~15 min | ~30x |
| Phase-2 P4 mirror-flip repro harness (per lab) | 1 week | ~1 hr | ~40x |
| Corroboration + disagreement-doc workflow | 2 days | ~30 min | ~90x |
| /reviews grid lab dimension + agreement meter (site) | 3 days | ~2 hr | ~12x |
| Overview lab-roster + reproduction-status panel | 1 day | ~45 min | ~10x |
| Full phase-2 fork (two labs, one target, blind protocol end-to-end) | 3–4 weeks | ~1 day | ~20x |

Completeness is a "lake," not an "ocean": the whole multi-lab machinery is a
bounded build measured in agent-hours, gated behind a stable single-lab loop.
The gating — not the build cost — is the reason to stage it.

---

*Design-only. No code, schema, or site component is wired in by this document.
Implementation begins only when phase 0's exit gate is green and Houston
green-lights phase 1.*
