# HANDOFF_SYNC — the two-machine ONE-LAB operating model

Houston runs **one** bigbounce lab across **two (or more) machines**. This doc is
the operating model that lets them behave as a single lab without collisions.

Three coordination planes, each with one job:

| Plane | Role | Mechanism | Already in place |
|---|---|---|---|
| **git** | the SYNC BUS | plain `push` / `pull --rebase` | pre-push site-freshness gate (`.git/hooks/pre-push` → `tools/site_freshness_check.sh`) runs on both machines |
| **Convex** | shared LIVE STATE | idempotent HTTP mutations to `brilliant-panther-471.convex.cloud` (no key, no deploy) | `upsertByLabelDate`, clobber/regression guards in `tools/post_verdict.sh` |
| **lab lease** | WHO DRIVES | `tools/lab_lease.sh` (remote `origin/main` snapshot + isolated `commit-tree` compare-and-swap) | hardened MVP |

---

## What syncs automatically vs manually

**Automatic (travels over git `pull --rebase`):**
- the whole repo — paper sources, `.tex`, compiled PDFs, figures
- ledgers & manifests — `project-context/peer-reviews/**`, DISPOSITIONS, EXT_real/ raws
- site data source — `site/src/data/*.ts` (papers, live-status, reviewTimeline)
- the lease file itself — `ops/handoff/LEASE.json`

**Automatic (travels over Convex, no git):**
- live readiness / verdict grid / activity feed / paper versions. These APIs are
  shared, but review writes are serialized by the driver lease. `post_verdict.sh`
  intentionally follows the newest raw verdict and may lower a cap honestly; it
  is not a "keep the better verdict" conflict resolver.

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
  compute (RunPod jobs, figure regen, MCMC), reproducibility checks, and disjoint
  docs/tooling. It does **not** drive a browser, adjudicate, write verdict/ledger
  state, or commit/push review/site-surface bundles. Independently committable
  work still rebases before push.

When A stops, B claims the lease and becomes the driver. Roles are not pinned to
hardware — whoever holds the lease drives.

---

## The lease in one paragraph

`tools/lab_lease.sh` first fetches and validates the lease from `origin/main`.
Mutations build a new tree from that exact remote commit using a temporary index,
`git commit-tree`, and `git push --force-with-lease=<fetched-sha>`; one contender
wins and every stale contender fails closed. No command pulls, rebases, stashes,
stages, moves `HEAD`, or writes the current checkout. `holds <machine-id>` is the
quiet driver gate. Renew every ~20 min for an interactive 45-minute lease;
`tools/bigbounce_cron_tick.sh` uses a 75-minute lease to cover its 50-minute cap.
Release when stopping intentionally; expired leases remain stealable. Promote
the same CLI contract to a Convex CAS only if git latency becomes material.

## Heartbeat gains a machineId

`project-context/LOOP_HEARTBEAT.json` should carry a `machineId` field so the
watchdog and the live site can attribute each tick to a machine and detect which
box is currently driving:

```json
{ "lastTickUTC": "2026-07-13T20:00:00Z", "machineId": "macbook-air",
  "source": "orchestrator", "note": "tick — driving (lease held)" }
```

`ops/RUNBOOK.md` now gates browser/adjudication on `holds`, stamps `machineId` +
role, and routes non-holders to lease-free work. The canonical durable source is
`tools/bigbounce_cron_tick.sh`; the App Support copy is only its deployed runtime.

---

## Phase-0 acceptance test

Two-machine ONE-LAB is accepted only after all of these pass on real machines:

1. `bootstrap.sh` reports zero FAIL on both machines; the intended driver also
   has a healthy `Mode: headed` browser with ChatGPT, Grok, and Gemini logged in.
2. A simultaneous claim test yields exactly one DRIVER. The loser remains
   lease-free, and neither checkout/index changes during `status`, `holds`, or a
   lost claim.
3. Driver renewal and TTL failover are demonstrated. Driver heartbeats carry the
   matching `machineId`; watchdog recovery is explicitly `role: lease-free`.
4. One full wave completes with raw+screenshot capture, one adjudication, no
   duplicate browser/verdict work, Convex/site/SSOT same-commit consistency, and
   a clean site build + freshness check.
5. Cron and watchdog are deployed from their tracked `tools/` sources, survive
   closing the interactive agent session, and their launchd jobs exit 0.

---

## Recovery when a machine goes dark

1. The dark machine stops renewing → its lease TTL expires.
2. The live machine's `tools/lab_lease.sh status` reports `EXPIRED`; its next
   `claim` succeeds against the expired holder (steal-on-expiry) — no manual
   cleanup, no stuck lock.
3. The OS-level watchdog notices a stale heartbeat and fires a **lease-free**
   recovery: machine-attributed heartbeat, freshness diagnostics, and raw harvest
   only. It never claims the lease or adjudicates/writes verdict state.
4. Interactive leases use 30–45 minutes; the hourly canonical cron uses 75
   minutes so its lease cannot expire during the 50-minute process cap.
