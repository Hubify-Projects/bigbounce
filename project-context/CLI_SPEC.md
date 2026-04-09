# Hubify Labs — CLI Specification (`hubify`)

**Status:** SPEC IN PROGRESS · Category F of `BUILD_READINESS_CHECKLIST.md`
**Author:** Houston Golden + Claude
**Date locked:** 2026-04-08
**Linked from:** PRD §45 (placeholder · TBD), `BUILD_READINESS_CHECKLIST.md` Category F
**Depends on:** `API_SPEC.md` (Category D) + `MCP_SERVER_SPEC.md` (Category E)
**Reference implementation:** Go (single static binary, fast startup, easy distribution via Homebrew/Scoop/apt)

---

## 0. The premise

The `hubify` CLI is **how Houston (and every other researcher) drives Hubify Labs from a terminal.** The CLI is a thin client over the REST API (`API_SPEC.md` §3) plus a stdio MCP server (`MCP_SERVER_SPEC.md` §6.1) plus an interactive TUI mode.

**Why a CLI matters:**
- Houston lives in the terminal. Most of his existing workflow is `ssh`, `git`, `pdflatex`, `python`, and Claude Code in a terminal split. The web UI is for monitoring + chat; the CLI is for everyday work.
- Researchers without admin access to a Mac (Linux servers, headless RunPod pods) need a way to interact with the platform without a browser
- Cron jobs + CI pipelines need to invoke Hubify Labs operations (dispatch experiments, post review results, etc.) — that's a CLI use case
- Every CLI command maps 1:1 to a REST endpoint, so the CLI is also the easiest way to learn and debug the API

**Reference implementations to mirror:**
- `gh` (GitHub CLI) — the gold standard for command structure + auth flow + Cobra-style subcommands
- `vercel` — simple `vercel deploy`, `vercel logs` patterns
- `convex` — TypeScript-native CLI with great `convex dev` and `convex deploy` UX
- `claude` (Claude Code) — `claude --resume`, `claude --print`, the slash command pattern

**Decision: write the CLI in Go.** Reasons:
- Single static binary, no runtime dependencies
- Fast startup (~10ms vs Node.js ~150ms vs Python ~200ms) — matters when Houston is typing `hubify status` 50 times a day
- Cobra (CLI framework) is mature and battle-tested
- Cross-compile to macOS / Linux / Windows from a single Go toolchain
- Easy distribution via Homebrew, Scoop, apt, snap, direct binary download

**Why not TypeScript / Node.js:** slower startup, requires Node runtime, harder to distribute (Houston would need `npm install -g @hubify-labs/cli`).
**Why not Python:** same problems plus the dependency hell.
**Why not Rust:** great choice but Cobra in Go is more mature than Clap in Rust for our needs, and the perf gap is irrelevant for a CLI.

---

## 1. Command structure

Top-level: `hubify <noun> <verb> [args] [flags]` — the `gh` pattern.

### 1.1 Lab commands

```bash
hubify lab list                                     # List all labs you have access to
hubify lab create <slug>                            # Create a new lab (interactive prompts for mission/north-star)
hubify lab create <slug> --from-template bounce-cosmology  # From a template
hubify lab show [<slug>]                            # Show current lab metadata (defaults to active lab)
hubify lab switch <slug>                            # Switch the active lab for subsequent commands
hubify lab share <slug> --with <other-slug>         # Configure cross-lab sharing
hubify lab share <slug> --public published-only     # Set public sharing mode
hubify lab delete <slug>                            # Delete a lab (soft-delete, 30-day recovery)
hubify lab open [<slug>]                            # Open the lab in the web UI (browser)
```

### 1.2 Project commands

```bash
hubify project list [--lab <slug>]                  # List projects in current/specified lab
hubify project create <slug>                        # Create a new project (interactive)
hubify project show [<id>]                          # Show project Overview (auto-maintained per PRD §40.12)
hubify project goal <id> "<goal text>"              # Update goal field
hubify project deliverable <id> "<deliverable>"     # Update deliverable field
hubify project measurable <id> "<measurable>"       # Update measurable field
hubify project archive <id>                         # Archive (soft-delete)
hubify project papers <id>                          # List papers associated with this project
hubify project papers <id> link <paper-id> --role primary    # Associate a paper (M:M per PRD §40.4)
```

### 1.3 Experiment commands (with PRD §41 routing)

```bash
hubify experiment list [--status running|pass|fail]  # List experiments
hubify experiment show <id>                           # Show experiment detail
hubify experiment dispatch <spec.yaml>                # Dispatch from a YAML spec file
hubify experiment dispatch --gpu H100 --duration 45 --cmd "python train.py"  # Inline dispatch
hubify experiment dispatch --cpu --cmd "pdflatex main.tex"                    # CPU-only dispatch
hubify experiment logs <id> [--follow] [--lines 100]  # Tail logs (SSE stream)
hubify experiment cancel <id>                          # Graceful cancel (SIGTERM + 30s checkpoint window)
hubify experiment promote <id>                         # Promote results to a contribution
```

The dispatch command enforces PRD §41 routing: if you don't specify `--gpu` or `--cpu`, the CLI prompts you. **No dispatch without an explicit compute mode.**

### 1.4 Pipeline commands

```bash
hubify pipeline list                                 # List pipelines in current lab
hubify pipeline show <id>                            # Show pipeline detail (steps, output, current state)
hubify pipeline run <id>                             # Trigger the full pipeline
hubify pipeline run <id> --from-step 3               # Resume from a specific step
hubify pipeline status <id>                          # Current step + progress
```

### 1.5 Chat commands (per PRD §40.6, §40.7, §40.13)

```bash
hubify chat new [--project <id>]                     # Start a new chat (optionally project-scoped)
hubify chat resume <id>                              # Resume a chat (full history)
hubify chat list                                     # List recent chats
hubify chat show <id>                                # Print chat history to stdout
hubify chat promote <id>                             # Trigger chat-to-project graduation per PRD §40.6
hubify chat notechat <id>                            # Save chat to Notes per PRD §40.8
hubify chat send <id> "<message>"                    # Post a message to a chat (no-action mode)
```

### 1.6 Note commands (per PRD §38)

```bash
hubify note new [filename]                           # Create a new note (defaults to today's daily journal)
hubify note list [--group daily|prompts|snippets|links|evergreen]  # List notes
hubify note open <filename>                          # Open in $EDITOR (vim, nvim, code, cursor)
hubify note search "<query>"                         # Full-text search
hubify note star <filename>                          # Star/unstar to pin to top
```

### 1.7 Pod + compute commands (per PRD §24, §41)

```bash
hubify pod status                                    # Show all running pods + GPU util + cost
hubify pod ssh [<id>]                                # SSH into a pod (defaults to first running)
hubify pod kill <id>                                 # Graceful kill with 30s checkpoint window
hubify pod restart <id>                              # Restart a stopped pod (volume preserved)
hubify pod logs <id> [--follow]                      # Tail pod-level logs
hubify credits                                       # Show balance + 24h burn + projected runway
hubify credits stream                                # Live stream of credit changes (SSE)
hubify dispatch decide --requires-gpu --duration 45  # Show what §41 routing would pick (no actual dispatch)
```

### 1.8 Agent commands

```bash
hubify agent list                                    # List agents in the current lab
hubify agent show <name>                             # Show 10-tab agent detail (per PRD §34)
hubify agent invoke <name> --payload '<json>'        # Invoke an agent
hubify agent wake <name>                             # Wake an idle agent
hubify agent sleep <name>                            # Sleep an active agent
hubify agent learnings <name>                        # Tail the agent's learnings.jsonl
hubify agent diff <name>                             # Show the diff for the agent's current version
```

### 1.9 Memory commands (per PRD §20)

```bash
hubify memory search "<query>" [--layer user|agent|lab|global|all]
hubify memory save --type feedback --title "..." --body "..."
hubify memory list --layer lab
```

### 1.10 Standup commands (per PRD §27)

```bash
hubify standup list                                  # List recent standups
hubify standup show <id>                             # Show transcript
hubify standup trigger                               # Trigger an unscheduled standup (per `/standup-now` slash command)
hubify standup next                                  # Show next scheduled standup time
```

### 1.11 Cost commands (per PRD §11, §41)

```bash
hubify costs                                         # Today's spend + MTD + projected runway
hubify costs by-provider                             # Breakdown per provider (RunPod / Anthropic / OpenAI / Vercel / Convex)
hubify costs history --days 30                       # 30-day spend history
hubify costs top-experiments [--limit 10]            # Most expensive experiments
```

### 1.12 Backup + sync commands (per PRD §6)

```bash
hubify backup list                                   # List backup destinations
hubify backup sync <dest>                            # Trigger immediate sync to a destination
hubify backup verify <dest>                          # Run integrity check
hubify backup history                                # Last 30 days of backup events
```

### 1.13 Cross-lab comms commands (per PRD §40.11)

```bash
hubify comm send --to <other-lab> --type suggestion --subject "..." --body "..."
hubify comm inbox                                    # Show pending comms in this lab's inbox
hubify comm accept <id>                              # Accept a suggestion (apply the change)
hubify comm reject <id>                              # Reject a suggestion
hubify comm sent                                     # Show comms this lab has sent
```

### 1.14 Search command (universal)

```bash
hubify search "<query>"                              # Universal search across papers/experiments/agents/files/contributions/surveys/chats/notes
hubify search "<query>" --type paper                 # Filter to specific entity type
hubify search "<query>" --json                       # Output as JSON for piping
```

### 1.15 MCP server commands

```bash
hubify mcp serve [--lab <slug>]                      # Run the MCP server in stdio mode (default — for Claude Code)
hubify mcp serve --sse --port 3030                   # Run in SSE mode on a local port
hubify mcp tools list                                # List all tools the server exposes
hubify mcp tools describe <tool-name>                # Show schema for a specific tool
hubify mcp resources list                            # List all resources
hubify mcp prompts list                              # List all prompt templates
hubify mcp test <tool-name> --input '<json>'         # Test-call a tool (validates auth + schema)
hubify mcp audit [--follow]                          # Tail the MCP audit log
```

### 1.16 Auth commands

```bash
hubify auth login                                    # Browser-based OAuth flow (GitHub default)
hubify auth login --token <token>                    # Login with a service token
hubify auth status                                   # Show current auth state (user, scopes, expiration)
hubify auth logout                                   # Revoke the current token
hubify auth tokens list                              # List service tokens (admin only)
hubify auth tokens create --name "ci-bot"            # Create a new service token
hubify auth tokens revoke <id>                       # Revoke a service token
```

### 1.17 Config commands

```bash
hubify config get [<key>]                            # Get all config OR a specific key
hubify config set <key> <value>                      # Set a config key
hubify config list                                   # List all config keys
hubify config edit                                   # Open ~/.hubify/config.yaml in $EDITOR
hubify config path                                   # Print the config file path
```

### 1.18 Status / system commands

```bash
hubify status                                        # Quick health: connected · current lab · credits · runway · running experiments
hubify open <hubify://...>                           # URL scheme handler (per PRD §40.17 Tier 4)
hubify version                                       # Print CLI version + API version
hubify help [<command>]                              # Show help (auto-generated from command structure)
```

### 1.19 TUI mode (interactive)

```bash
hubify                                               # No args → opens the TUI (interactive terminal UI)
hubify tui                                           # Explicit form
```

The TUI is an interactive terminal interface mirroring the web UI's main views (Director, Experiments, Papers, Agents, Compute) using the same data via the API. Built with `bubbletea` (the Charmbracelet TUI framework). Keyboard shortcuts mirror the web UI: ⌘1-9 for views, `/` for search, `?` for help.

The TUI is for users who want to live entirely in the terminal — no browser at all. Houston specifically asked for this in PRD §30 ("hubify CLI in terminal — auto-launches 4 sessions").

**Total: ~120 commands across 19 categories.**

---

## 2. Output formats

Every command supports `--format` for machine-readable output:

| Format | When to use |
|---|---|
| `text` (default) | Human-readable, colored, with tables for lists |
| `json` | Pipe to `jq` or another tool |
| `yaml` | Config-style output |
| `table` | Forced table format (text default for some commands is bullet lists) |
| `tsv` | Tab-separated, for `awk`/spreadsheet import |

Example:
```bash
hubify experiment list --format json | jq '.[] | select(.status == "running")'
hubify costs by-provider --format tsv > spend.tsv
```

When `stdout` is not a TTY, the CLI auto-disables colors and progress bars.

---

## 3. Auth flow

### 3.1 Browser-based OAuth (default)

```bash
$ hubify auth login
→ Opening https://hubify-labs.com/oauth/authorize?...
→ Waiting for callback on http://localhost:7642/...
✓ Logged in as houston@hubify.com
✓ Active lab set to bigbounce-hubify
✓ Token saved to ~/.hubify/credentials (mode 0600)
```

The CLI opens a browser to the OAuth authorize URL, runs a local HTTP server on a random port to receive the callback, exchanges the code for a token, and saves it to disk.

PKCE (Proof Key for Code Exchange) is used for the desktop OAuth flow per RFC 7636.

### 3.2 Service token (for CI / cron / headless)

```bash
$ HUBIFY_TOKEN=hbf_st_abc123... hubify experiment dispatch ...
```

The CLI checks `HUBIFY_TOKEN` env var first, falls back to `~/.hubify/credentials`.

### 3.3 Token storage

- **macOS:** `~/.hubify/credentials` (mode 0600), with optional Keychain integration via `security` command
- **Linux:** `~/.hubify/credentials` (mode 0600), with optional libsecret integration
- **Windows:** `%USERPROFILE%\.hubify\credentials`, with optional Credential Manager integration

The credentials file is YAML:
```yaml
default_profile: houston
profiles:
  houston:
    user: houston@hubify.com
    token: hbf_user_eyJ...
    expires_at: 2026-04-09T00:00:00Z
    refresh_token: hbf_refresh_xyz...
  ci-bot:
    token: hbf_st_abc123...
    expires_at: 2026-07-08T00:00:00Z
```

### 3.4 Profile switching

```bash
hubify --profile ci-bot experiment list
HUBIFY_PROFILE=ci-bot hubify status
```

---

## 4. Local config + secrets

### 4.1 Config file location

`~/.hubify/config.yaml`:
```yaml
active_lab: bigbounce-hubify
default_format: text
api_endpoint: https://api.hubify-labs.com
mcp_server:
  default_transport: stdio
  default_lab: bigbounce-hubify
editor: nvim                           # for `hubify note open`
ssh_key_path: ~/.ssh/id_ed25519        # for `hubify pod ssh`
runpod_api_key_env: RUNPOD_API_KEY     # which env var holds the RunPod key for credit checks
```

### 4.2 Per-lab config override

`<lab>/.hubify/config.yaml` overrides the global config when running CLI commands inside a lab directory. Useful for project-specific settings.

### 4.3 Secrets handling

The CLI **never stores secrets in the config file**. Secrets go in:
- Environment variables (`HUBIFY_TOKEN`, `RUNPOD_API_KEY`, etc.)
- The credentials file (`~/.hubify/credentials`, mode 0600)
- macOS Keychain / Linux libsecret / Windows Credential Manager

The `hubify config get` command never prints secrets. Attempting to set a secret via `hubify config set` fails with an error pointing to the env var pattern.

---

## 5. Plugin system (deferred to v1.1)

Stub spec for the future plugin system:

```bash
hubify plugin install <name>           # Install a community plugin
hubify plugin list                     # List installed plugins
hubify plugin update                   # Update all plugins
hubify plugin remove <name>            # Uninstall
```

Plugins are Go binaries placed in `~/.hubify/plugins/` and invoked as `hubify <plugin-name>`. The `gh extensions` pattern.

**v1.0 ships without the plugin system.** The CLI stays compact and curated for the first release. v1.1 adds plugins.

---

## 6. Distribution

### 6.1 Homebrew (macOS + Linux)

```bash
brew install hubify-labs/tap/hubify
brew upgrade hubify
```

A Homebrew tap is set up at `Hubify-Labs/homebrew-tap`. The formula points to the latest GitHub release.

### 6.2 Direct binary download

```bash
curl -fsSL https://hubify-labs.com/install.sh | sh
```

Detects OS + arch, downloads the right binary from GitHub releases, places it in `/usr/local/bin/hubify`, runs `hubify --version` to verify.

### 6.3 Scoop (Windows)

```powershell
scoop bucket add hubify https://github.com/Hubify-Labs/scoop-bucket
scoop install hubify
```

### 6.4 Linux package managers

- **apt:** `sudo apt install hubify` (after adding the Hubify Labs apt repo)
- **snap:** `sudo snap install hubify`
- **AUR:** `yay -S hubify` (Arch User Repository)

### 6.5 Source build

```bash
git clone https://github.com/Hubify-Labs/cli
cd cli
make install
```

### 6.6 Release cadence

- **Patch releases** (bug fixes): as-needed, auto-published from main on tagging
- **Minor releases** (new commands): every 2-4 weeks
- **Major releases** (breaking changes): tied to API major versions, ~6-12 months apart

The `tauri-action` GitHub Action handles cross-compilation + signing + release on every git tag.

---

## 7. Auto-update channel

The CLI checks for updates on every command (background, non-blocking) and prompts to update when a new version is available:

```bash
$ hubify status
✓ Lab: bigbounce-hubify · 47h runway · 3 experiments running

ⓘ A new version of hubify is available: 1.2.0 (you are on 1.1.4)
  Run 'hubify update' to upgrade.
```

`hubify update` checks the install method (Homebrew/Scoop/binary) and runs the appropriate upgrade command. For binary installs, it downloads the new release and replaces itself in place.

The check is rate-limited to once per 24 hours and can be disabled with `hubify config set check_updates false`.

---

## 8. Shell completions

```bash
hubify completion bash > /usr/local/etc/bash_completion.d/hubify
hubify completion zsh > /usr/local/share/zsh/site-functions/_hubify
hubify completion fish > ~/.config/fish/completions/hubify.fish
hubify completion powershell > $PROFILE/_hubify.ps1
```

Cobra auto-generates these. The completion script provides:
- Command + subcommand completion
- Flag completion
- Dynamic completion for slugs (lab slugs, project IDs, agent names) — via async API calls

---

## 9. Error handling

Same RFC 7807 format as `API_SPEC.md` §5, but rendered in human-readable form by default:

```bash
$ hubify experiment dispatch --cmd "python train.py"
✗ Experiment dispatch failed
  Type: validation-failed
  Reason: Missing required field 'requires_gpu'
  Per PRD §41 Rule 1, every experiment must declare CPU vs GPU before dispatch.
  Try: hubify experiment dispatch --gpu H100 --duration 45 --cmd "python train.py"
       hubify experiment dispatch --cpu --duration 10 --cmd "python train.py"
```

With `--format json`, the error is returned as the raw RFC 7807 JSON.

The CLI exit codes follow the convention:
- `0` — success
- `1` — generic error
- `2` — usage error (bad flags, missing args)
- `3` — auth error
- `4` — validation error
- `5` — upstream error (API/RunPod down)
- `6` — rate limited
- `7` — not found

---

## 10. Logging + verbosity

```bash
hubify <command>                       # Default: terse, no debug output
hubify <command> -v                    # Verbose: show API calls
hubify <command> -vv                   # Very verbose: show full request/response bodies
hubify <command> --quiet               # Suppress all non-essential output (for piping)
```

A debug log is always written to `~/.hubify/logs/hubify-<date>.log` regardless of verbosity. Useful for troubleshooting after the fact.

---

## 11. The CLI YAML lock

Just like the API spec has `api-spec.openapi.yaml`, the CLI spec has:

```
project-context/cli-spec.yaml
```

(This is the next item in Category F — to be written after this human-readable spec is locked.)

The YAML enables:
- Auto-generated command help text
- Auto-generated documentation for the Mintlify docs site
- Shell completion auto-generation
- CLI integration tests
- Cross-CLI consistency checks (e.g., every `hubify <noun> list` should support `--format json`)

---

## 12. Out of scope for v1

- ❌ Plugin system (deferred to v1.1)
- ❌ Multi-account support (one user at a time per profile, no profile sync)
- ❌ Built-in update server (we use GitHub releases for v1)
- ❌ Telemetry (no usage data sent home in v1 — privacy-first; opt-in telemetry in v1.1)
- ❌ Custom theme support (the CLI uses a default sage-aligned color palette)
- ❌ Interactive scripts / pipelines (the TUI is interactive; scripts use individual commands)

---

## 13. The next steps

After this spec is reviewed by Houston:

1. **Lock the CLI YAML** (`cli-spec.yaml`)
2. **Bootstrap the Go project** — `cmd/hubify/main.go` with Cobra root command
3. **Stub each command** — every command from §1 gets a Cobra subcommand with the help text
4. **Wire to the API** — implement each command as an HTTP call to the corresponding API endpoint
5. **Wire the MCP server** — `hubify mcp serve` runs the MCP server from `MCP_SERVER_SPEC.md`
6. **Build the TUI** — `bubbletea` app for interactive mode
7. **Set up Homebrew tap + GitHub releases**
8. **Write user-facing docs** for the Mintlify site

---

## 14. Open questions

1. **Go vs Rust** — Go is the default. Reconsider only if startup time becomes a real bottleneck (it won't).
2. **TUI framework** — `bubbletea` (Charmbracelet) is the default. Alternative: `tview` (older but stable).
3. **Browser open behavior** — should `hubify lab open` use `xdg-open` / `open` / `start.exe` or always print the URL? Default: open the browser, fall back to printing if no display.
4. **JSON output strictness** — should `--format json` ever include human-readable fields like timestamps in local time, or always UTC ISO 8601? Default: always UTC ISO 8601 + machine-friendly types.
5. **Color in CI** — auto-detect via `$CI` and `$NO_COLOR` env vars, default off in CI.
6. **Default editor** — `$EDITOR` env var first, fall back to `vim` on Unix and `notepad` on Windows.
7. **TUI vs web parity** — the TUI is intended for power users in the terminal. Should it have full feature parity with the web UI, or just the most-used 60%? Default: 60% parity for v1 (Director / Experiments / Papers / Agents / Compute / Chat), full parity in v1.1.

---

## 15. What this spec stress-tests

- **The CLI as a thin client over the API** — proves that one REST surface can serve a feature-rich CLI without per-command custom logic
- **The MCP server hosting via the CLI** — `hubify mcp serve` is the deployment pattern for stdio MCP. If this works for Houston with Claude Code, it works for any researcher with any MCP-compatible client.
- **The §41 routing discipline at the CLI layer** — `experiment dispatch` requires `--gpu` or `--cpu` as a hard input. Houston cannot accidentally dispatch GPU work as CPU or vice versa.
- **Auth profile switching** — Houston can have a personal token + a CI bot token + multiple lab tokens, all in one credentials file, switched via `--profile`
- **Cross-lab comms** — `hubify comm send` is the only way to suggest changes across labs, enforcing the Lab Sovereignty Rule at the CLI layer
- **The TUI option** — proves the platform doesn't require a browser, supports headless and accessibility-first workflows

If the CLI ships and Houston can `hubify status`, `hubify experiment dispatch`, `hubify chat new`, `hubify mcp serve`, and `hubify` (TUI) all from his terminal, the platform is fully driveable from a keyboard alone.

---

## 16. Status

**This file:** Category F item 1 of the BUILD_READINESS_CHECKLIST. Bootstraps Category F from 0% → ~88% in one shot:

- ✅ Item 1: Write CLI_SPEC.md (this file)
- ✅ Item 2: Command structure (~120 commands across 19 categories)
- ✅ Item 3: TUI mode (covered in §1.19, bubbletea framework)
- ✅ Item 4: Output formats (§2 — text/json/yaml/table/tsv)
- ✅ Item 5: Auth flow (§3 — browser OAuth + service tokens + profile switching)
- ✅ Item 6: Local config + secrets (§4)
- ⏸ Item 7: Plugin system (§5 — DEFERRED to v1.1, explicitly out of scope for v1)
- ⏸ Item 8: CLI YAML lock — `cli-spec.yaml` (next Category F iteration)

**6 of 8 Category F items checked off in one iteration** (item 7 explicitly deferred, item 8 is the next iteration).
