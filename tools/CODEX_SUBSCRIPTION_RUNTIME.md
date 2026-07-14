# Codex subscription runtime

## Purpose

The BigBounce runtime uses the installed Codex CLI with the user's ChatGPT
login for repo-aware subscription work. It does not use an Anthropic runtime,
and the Codex subscription leg explicitly removes `OPENAI_API_KEY`,
`CODEX_API_KEY`, and `ANTHROPIC_API_KEY` from its process environment so
authentication cannot silently switch to an API-key path.

Validated locally on 2026-07-14:

- `codex-cli 0.144.3`
- `codex login status` -> `Logged in using ChatGPT`
- locally exposed subscription model: `gpt-5.6-sol`
- `codex exec` supports `--sandbox`, `--ask-for-approval`, `--ephemeral`,
  `--ignore-user-config`, `--output-last-message`, `--cd`, `--model`, and `-c`

The default reasoning setting is `high`. An unsupported model or effort fails
that leg visibly; there is no silent model fallback.

## Controls

These contain no secrets and are shared by the INT, cron, and watchdog tools:

```bash
export BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1  # set 0 to disable immediately
export BIGBOUNCE_CODEX_MODEL=gpt-5.6-sol
export BIGBOUNCE_CODEX_EFFORT=high
export BIGBOUNCE_CODEX_BIN=/opt/homebrew/bin/codex  # optional
export BIGBOUNCE_WATCHDOG_CODEX_TIMEOUT_SECONDS=900
```

Accepted effort values are `minimal`, `low`, `medium`, `high`, `xhigh`, `max`,
and `ultra`; the selected model must support the chosen value. The local
`gpt-5.6-sol` catalog currently exposes `low`, `medium`, `high`, `xhigh`, `max`,
and `ultra`.

The reviewer legs and watchdog recovery are permanently `read-only`,
`approval=never`, and ephemeral. They cannot edit the repository, commit,
push, drive a browser, or write review/Convex/site state. Reviewer final text is
saved under the existing INT evidence directories with `codex` in its filename
and run-log keys (`codex=`, `codex_raw=`).

The durable cron tick is role-sensitive:

- `lease-free`: fixed `read-only`; it reports one recommendation and cannot act.
- `driver`: retains the existing authorized mutation contract only after the
  remote lease is acquired. The default is `danger-full-access` because that
  contract includes repository edits, git commit/push, Convex/network access,
  and possibly the already-headed browser. This is intentionally not used for
  lease-free or watchdog work. `BIGBOUNCE_CRON_DRIVER_SANDBOX=workspace-write`
  may be tested on a machine where its network and git behavior is sufficient.

## No-launch validation

These commands verify resolution and ChatGPT authentication without creating
review output, acquiring a lease, writing a heartbeat, mutating Convex, or
starting an agent:

```bash
BIGBOUNCE_INT_WAVE_DRY_RUN=1 tools/int_wave.sh P1U
BIGBOUNCE_INT_WAVE_DRY_RUN=1 tools/int_wave_apjs.sh
BIGBOUNCE_CRON_DRY_RUN=1 tools/bigbounce_cron_tick.sh
BIGBOUNCE_CRON_DRY_RUN=1 BIGBOUNCE_CRON_DRY_RUN_ROLE=driver tools/bigbounce_cron_tick.sh
BIGBOUNCE_WATCHDOG_DRY_RUN=1 tools/loop_watchdog.sh
```

Static validation:

```bash
bash -n tools/int_wave.sh tools/int_wave_apjs.sh \
  tools/bigbounce_cron_tick.sh tools/loop_watchdog.sh
shellcheck tools/int_wave.sh tools/int_wave_apjs.sh \
  tools/bigbounce_cron_tick.sh tools/loop_watchdog.sh
```

## Deployment

macOS launchd cannot execute the canonical scripts from `~/Desktop` on this
machine, so deploy verified copies without reloading the LaunchAgent:

```bash
install -m 0755 tools/bigbounce_cron_tick.sh \
  "$HOME/Library/Application Support/bigbounce/bigbounce-cron-tick.sh"
install -m 0755 tools/loop_watchdog.sh \
  "$HOME/Library/Application Support/bigbounce/loop_watchdog.sh"
```

After copying, compare SHA-256 hashes and rerun the deployed scripts' dry-run
paths. Reloading launchd is a separate, explicit operation.

The cron and watchdog wrappers now publish heartbeat JSON with temp-file plus
atomic-rename, preventing readers from observing the previous truncate/write
window.

## Rollback

1. Set `BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=0` in the LaunchAgent environment
   to stop all subscription sessions while keeping API legs available.
2. Restore the four canonical scripts from the last known-good git revision,
   then redeploy and hash-compare them.
3. Keep the LaunchAgent unloaded until deployed dry-runs pass.

The `.pre-c2018dc6` deployed copies are forensic backups of the former
Anthropic implementation. Do not reactivate them while the non-Anthropic
constraint is in force.

## Launchd caveat

Interactive ChatGPT authentication is confirmed, but this migration does not
launch or reload the LaunchAgent. The first controlled launchd smoke test must
verify that the user LaunchAgent can access the Codex credential store and read
the Desktop repository under macOS TCC. A dry-run can validate the credential
store from the deployed path, but only a deliberately triggered read-only
recovery can prove repository access. Until that smoke test passes, launchd
noninteractive access remains the sole residual runtime blocker.
