# BOOTSTRAP_PROMPT — paste into a fresh agent on another machine

Paste the block below into a **fresh Claude Code (or Codex) session** on the
second machine. It is a prompt, not a manual — the linked docs carry the detail.

---

```
You are joining Houston's bigbounce lab as a SECOND machine of ONE lab. Do this in order:

1. Clone or pull the repo (KEEP this canonical path — memory restore is path-keyed):
   git clone https://github.com/Hubify-Projects/bigbounce.git ~/Desktop/CODE_YOU/bigbounce
   (already cloned? cd there and `git pull --rebase`)
   For legacy tools that still resolve CODE_2025, add a non-destructive compatibility
   symlink only when that path is absent:
   mkdir -p ~/Desktop/CODE_2025
   [ -e ~/Desktop/CODE_2025/bigbounce ] || ln -s ~/Desktop/CODE_YOU/bigbounce ~/Desktop/CODE_2025/bigbounce

2. Restore secrets + shared stack. DO NOT ask me for keys and NEVER print values.
   Run the /machine-sync skill to restore .env.local from the You.md Secret Vault
   with vault root `~/Desktop/CODE_YOU`,
   then follow the bigbounce-specific bootstrap in project-context/AGENT_ONBOARDING.md
   §1 (repos, skills, toolchain). That doc is the source of truth — extend/point to
   it, don't duplicate it.

3. Verify prerequisites:
   bash ops/handoff/bootstrap.sh
   Resolve every FAIL (WARN is degraded-but-runnable). Re-run until READY.
   First run: the HEADED browser needs my manual reviewer logins — run /connect-chrome
   and tell me to sign into ChatGPT/Grok/Gemini before any EXT sweep.
   Machine-level sticky-headed: add `export BROWSE_HEADED=1` to your shell profile
   (~/.zshrc). The browse server relaunches HEADLESS by default, which reads live
   reviewer chats as dead (false FAILED-dead harvests). The EXT tools + cron tick
   already export it; the profile line covers ad-hoc `browse` calls. bootstrap.sh
   WARNs if it's missing.

4. Read the two-machine operating model: ops/handoff/HANDOFF_SYNC.md
   (git = sync bus, Convex = shared live state, lease = who drives).

5. ACQUIRE THE LAB LEASE before driving anything (browser EXT / verdict + ledger writes):
   tools/lab_lease.sh status
   tools/lab_lease.sh claim <machine-id> 45     # e.g. macbook-air; 45-min TTL
   If DENIED (the other machine holds it), do lease-FREE work only: INT API review
   waves, compute/RunPod, site edits — and re-check status. Renew every ~20 min while
   driving (tools/lab_lease.sh renew <machine-id>); release when you stop.

6. Start the loop per ops/RUNBOOK.md (fall back to project-context/AGENT_ONBOARDING.md
   §4 if RUNBOOK isn't present yet). Write LOOP_HEARTBEAT.json with your machineId each tick.

Orchestrating in Codex/Cursor/Pi instead of Claude Code? First read
ops/handoff/ORCHESTRATOR_PORTABILITY.md for the host-equivalence table.
```

---

**Notes for the human (not part of the paste):**
- The `<machine-id>` is any stable short name (`macbook-air`, `mac-studio`).
- Only ONE machine holds the lease at a time; the lease travels over git, so both
  machines see the same holder after a pull.
- If this machine goes dark, the other machine's `claim` steals the lease once the
  TTL expires — no manual cleanup needed.
