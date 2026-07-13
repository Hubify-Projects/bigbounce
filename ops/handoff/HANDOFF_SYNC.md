# HANDOFF_SYNC — the two-machine ONE-LAB operating model

Houston runs **one** bigbounce lab across **two (or more) machines**. This doc is
the operating model that lets them behave as a single lab without collisions.

Three coordination planes, each with one job:

| Plane | Role | Mechanism | Already in place |
|---|---|---|---|
| **git** | the SYNC BUS | plain `push` / `pull --rebase` | pre-push site-freshness gate (`.git/hooks/pre-push` → `tools/site_freshness_check.sh`) runs on both machines |
| **Convex** | shared LIVE STATE | idempotent HTTP mutations to `brilliant-panther-471.convex.cloud` (no key, no deploy) | `upsertByLabelDate`, clobber/regression guards in `tools/post_verdict.sh` |
| **lab lease** | WHO DRIVES | `tools/lab_lease.sh` (git-tracked `ops/handoff/LEASE.json`, claimed via commit+push race) | this MVP |

---

## What syncs automatically vs manually

**Automatic (travels over git `pull --rebase`):**
- the whole repo — paper sources, `.tex`, compiled PDFs, figures
- ledgers & manifests — `project-context/peer-reviews/**`, DISPOSITIONS, EXT_real/ raws
- site data source — `site/src/data/*.ts` (papers, live-status, reviewTimeline)
- the lease file itself — `ops/handoff/LEASE.json`

**Automatic (travels over Convex, no git):**
- live readiness / verdict grid / activity feed / paper versions — idempotent writes,
  so both machines writing the same round is safe (last-writer-wins on identical data;
  `post_verdict.sh` guards against regressing a better verdict).

**Manual per-machine (does NOT travel — set up once on each box):**
- **browser reviewer logins** — HEADED Chrome sessions (ChatGPT/Grok/Gemini) are
  per-machine; sign in via `/connect-chrome` on each machine that will run EXT.
- **`.env.local`** — restored via the `/machine-sync` skill (You.md Secret Vault),
  never committed, never synced through git.
- **launchd plists** — the durable loop guarantee (`com.bigbounce.loopwatchdog`,
  `com.bigbounce.cron-tick`) is installed per-machine; `bootstrap.sh` reports if missing
  and prints the install command from the repo copies in `tools/launchd/`.

---

## Recommended division of labor

Both machines commit and both write Convex. The **lease gates only the
browser-driving + verdict/ledger-adjudication role** — everything else runs freely
in parallel, which is how two machines make the lab faster instead of contended.

- **Machine A — DRIVER (holds the lease):** headed-browser EXT sweeps, per-finding
  truth-audit adjudication, verdict-grid writes, ledger/disposition commits, the
  loop heartbeat.
- **Machine B — lease-FREE work:** INT API review waves (OpenAI/Grok/Gemini native-PDF),
  compute (RunPod jobs, figure regen, MCMC), site polish, doc/skill work. Commits
  freely; `pull --rebase` before each push (disjoint files → clean rebases).

When A stops, B claims the lease and becomes the driver. Roles are not pinned to
hardware — whoever holds the lease drives.

---

## The lease in one paragraph

`tools/lab_lease.sh claim <machine-id> <ttl-min>` writes `ops/handoff/LEASE.json`
and commits+pushes it; if the push is rejected (the other machine claimed first),
the claim loses the race and reports the real holder. `holds <machine-id>` is the
quiet loop gate — the driving section runs **only while it exits 0**. `renew` every
~20 min while driving; `release` when you stop. **Tradeoff (MVP):** git-as-lock has a
push-latency race window and costs a pull+push round-trip per claim — fine for a
2-machine lab on a ~20-min cadence. Promote to a Convex atomic compare-and-set
mutation if contention ever tightens; the CLI contract stays identical.

## Heartbeat gains a machineId

`project-context/LOOP_HEARTBEAT.json` should carry a `machineId` field so the
watchdog and the live site can attribute each tick to a machine and detect which
box is currently driving:

```json
{ "lastTickUTC": "2026-07-13T20:00:00Z", "machineId": "macbook-air",
  "source": "orchestrator", "note": "tick — driving (lease held)" }
```

> **RUNBOOK patch note:** `ops/RUNBOOK.md` did not exist when this MVP landed. When
> it is written, its heartbeat-writing step must stamp `machineId` (matching the
> lease holder while driving) and gate the browser/adjudication section on
> `tools/lab_lease.sh holds "$MACHINE_ID"`. Until then, the loop entry point is
> `project-context/AGENT_ONBOARDING.md` §4.

---

## Recovery when a machine goes dark

1. The dark machine stops renewing → its lease TTL expires.
2. The live machine's `tools/lab_lease.sh status` reports `EXPIRED`; its next
   `claim` succeeds against the expired holder (steal-on-expiry) — no manual
   cleanup, no stuck lock.
3. The OS-level `com.bigbounce.loopwatchdog` launchd agent independently notices a
   stale `LOOP_HEARTBEAT.json` (>45 min) and fires a headless recovery tick +
   Convex alert, so the loop keeps moving even with a closed session.
4. Keep TTLs short enough (30–45 min) that a dark machine frees the driver role
   within one cron cadence.
