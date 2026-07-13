# ORCHESTRATOR_PORTABILITY — run the lab's orchestrator role in Codex / Cursor / Pi

The bigbounce loop was built in Claude Code, but the **orchestrator role is
host-agnostic**: nearly everything it drives is a plain shell script, an HTTP
call, or a CLI. Only a few capabilities bind to the host. This doc maps them so a
second machine can run the loop under whatever agent is installed there.

## Host-equivalence table

| Capability | Claude Code | Codex | Cursor / Pi |
|---|---|---|---|
| Spawn a sub-agent (per-paper owner, per-vendor reviewer) | `Agent` tool (parallel calls in one message) | `spawn_agent` | host's agent/task spawn; if none, run legs sequentially in-session |
| **Claude/Anthropic INT leg** | the **running agent itself** on Houston's subscription — never the Anthropic API (directive I1) | the **running Codex agent** is the "Claude-equivalent" leg on ITS subscription | the running host agent IS that leg on its subscription |
| OpenAI INT leg | OpenAI API via `tools/v3_native_pdf_review.py` | same script, or the Codex agent | same script |
| Grok / Gemini INT legs | XAI / Gemini API via the same script (Gemini→browser when key throttled) | same | same |
| Model routing tiers | Opus judgment / Sonnet execution / Haiku polling | `gpt-5.5` orchestrate / `codex-spark`/`mini` workers | host tiers per the global CLAUDE.md heuristic |
| Durable loop (survives session close) | macOS `launchd`; deploy canonical `tools/{bigbounce_cron_tick,loop_watchdog}.sh` copies to App Support | same only on macOS; non-macOS needs a systemd/Task Scheduler adapter | host scheduler adapter required; never describe launchd as host-independent |
| Skill invocation (`/machine-sync`, `/connect-chrome`, `/bigbounce-r-round`) | Skill tool | equivalent command, or read the SKILL.md and execute its steps | read the SKILL.md and execute its steps |

**Key rule (directive I1):** the Claude-equivalent INT leg is always **the running
agent on its own subscription**, whichever host that is. NEVER ask Houston for an
Anthropic API key and NEVER fail an INT round because an API is disabled.

## Host-agnostic already (works identically everywhere)

- **Core data/review scripts** — `lab_lease.sh`, `post_verdict.sh`,
  `ext_harvest.sh`, `site_freshness_check.sh`, `v3_native_pdf_review.py` are
  shell/Python. `lab_lease.sh` coordinates through remote git CAS without
  touching the caller's worktree/index.
- **Convex HTTP** — `POST brilliant-panther-471.convex.cloud/api/{mutation,query}`,
  no key, no deploy. Same from any host.
- **The manifest / EXT_real raw-capture contract** — save raw reviewer text +
  screenshot before recording any verdict. Host-independent file convention.
- **The headed browser protocol** is host-neutral, but the concrete
  `~/.claude/skills/gstack/browse/dist/browse connect` path exists only where
  gstack is installed. A host without that visible-browser stack is INT-only.
- **The lab lease** — coordinates across hosts too: a Codex machine and a Claude
  Code machine claiming the same git-tracked `LEASE.json` interoperate cleanly.

## What genuinely needs the host

- **Sub-agent spawning / parallel fan-out** — the tool name differs (`Agent` vs
  `spawn_agent`); a host with no spawn runs the review legs sequentially.
- **Skill invocation** — a non-Claude host reads the relevant `SKILL.md`
  (under `~/.claude/scistack/…`) and executes its steps manually instead of `/name`.
- **Durable scheduling is host-bound.** `tools/bigbounce_cron_tick.sh` and
  `tools/loop_watchdog.sh` are the macOS/Claude Code adapter: launchd, App Support,
  `osascript`, and `claude -p`. Codex/Cursor/Pi on another OS need an equivalent
  scheduler + host-agent invocation while preserving the lease/heartbeat contract.

## Bottom line

To move the orchestrator to another host: install that host's agent, run
`ops/handoff/bootstrap.sh`, restore secrets via `/machine-sync`, acquire the lab
lease, and drive the same core scripts. The Claude INT leg becomes "the running
agent on its subscription," and spawning maps to the host primitive. On macOS,
deploy `tools/bigbounce_cron_tick.sh` + `tools/loop_watchdog.sh` to App Support;
else implement the scheduler adapter before claiming durable-loop parity.
