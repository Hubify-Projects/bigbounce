#!/usr/bin/env bash
# skills_autolog.sh — generative skill/self-improvement changelog for reviewTimeline.ts.
#
# THE PROBLEM this fixes: per-round skill/process/tooling logging used to require
# agents to REMEMBER which commits qualified as skill/process improvements and hand-
# craft the TS literal from scratch each round. Both steps are error-prone and slow.
# This script derives the entries DIRECTLY from git history, emitting paste-ready
# draft TS literals so the agent only has to verify counters, not reconstruct provenance.
#
# What it does:
#   Default mode: given --since <ref-or-date> (default = last skillsSeries dateISO),
#     scans TWO git logs (bigbounce repo + scistack spec repo) for skill/process/tooling
#     commits and emits:
#       1. A draft skillsSeries SkillsPoint object.
#       2. A draft reviewTimeline skill-improvement ReviewRound object.
#     Both drafts are sha-cited, paste-ready into site/src/data/reviewTimeline.ts.
#
#   --check mode: exits 2 if there are ANY unlogged skill/process/tooling commits since
#     the last skillsSeries point whose 8-char sha does NOT appear in reviewTimeline.ts.
#     Prints a count to stderr. Used as a WARN-level gate (e.g. pre-push).
#     Exit codes: 0 = all logged, 2 = unlogged commits found.
#
# Keyword regex for "skill/process/tooling commit" (case-insensitive, on subject):
#   feat(tools)|chore(tools)|fix(tools)|skill|feat(reviews).*(gate|automation|tracking|
#   instrument|ledger)|watchdog|pattern-0|prompt.?rule|protocol|self-improve|freshness|
#   autolog|directive
# Also: any commit touching tools/ (bigbounce) or astrostack/ (scistack), regardless
# of subject.
#
# bash-3.2 safe (macOS default). Python3 heredoc does all parsing/formatting.
# set -uo pipefail (bash-3.2 does not support pipefail reliably on pipe builtins,
# but the flag is included for best-effort strictness on modern bash).

set -uo pipefail

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
SCISTACK="$HOME/.claude/scistack"
REVIEW_TIMELINE="$REPO/site/src/data/reviewTimeline.ts"
GH_BASE="https://github.com/Hubify-Projects/bigbounce"

# ---------------------------------------------------------------------------
# Arg parsing
# ---------------------------------------------------------------------------
CHECK_MODE=0
SINCE_ARG=""

while [ $# -gt 0 ]; do
  case "$1" in
    --check) CHECK_MODE=1 ;;
    --since)
      shift
      SINCE_ARG="${1:-}"
      ;;
    --since=*) SINCE_ARG="${1#--since=}" ;;
    *) echo "skills_autolog: unknown flag: $1" >&2; exit 1 ;;
  esac
  shift
done

# ---------------------------------------------------------------------------
# Determine --since: default = last skillsSeries dateISO in reviewTimeline.ts
# ---------------------------------------------------------------------------
SINCE="$(python3 - "$REVIEW_TIMELINE" "$SINCE_ARG" <<'PY'
import sys, re
timeline_path, since_arg = sys.argv[1], sys.argv[2]

# If explicitly provided, use it.
if since_arg:
    print(since_arg)
    sys.exit(0)

# Parse the skillsSeries array, collect all dateISO values, return the max.
try:
    with open(timeline_path) as f:
        text = f.read()
    # find the skillsSeries block
    m = re.search(r'export const skillsSeries\b', text)
    if not m:
        print("7 days ago")
        sys.exit(0)
    block = text[m.end():]
    # find end of array (next `export const`)
    nxt = re.search(r'\nexport const ', block)
    if nxt:
        block = block[:nxt.start()]
    dates = re.findall(r'dateISO:\s*"([0-9]{4}-[0-9]{2}-[0-9]{2})"', block)
    if not dates:
        print("7 days ago")
        sys.exit(0)
    print(max(dates))
except Exception:
    print("7 days ago")
PY
)"

# ---------------------------------------------------------------------------
# Read last skillsSeries counters (patterns, promptRules, tooling)
# ---------------------------------------------------------------------------
LAST_COUNTERS="$(python3 - "$REVIEW_TIMELINE" <<'PY'
import sys, re

try:
    with open(sys.argv[1]) as f:
        text = f.read()
    m = re.search(r'export const skillsSeries\b', text)
    if not m:
        print("71 37 13")
        sys.exit(0)
    block = text[m.end():]
    nxt = re.search(r'\nexport const ', block)
    if nxt:
        block = block[:nxt.start()]
    # Find ALL entries (objects in the array)
    # Each entry: { ... patterns: N, promptRules: M, tooling?: T ... }
    pat_vals   = [int(x) for x in re.findall(r'\bpatterns:\s*(\d+)', block)]
    pr_vals    = [int(x) for x in re.findall(r'\bpromptRules:\s*(\d+)', block)]
    tool_vals  = [int(x) for x in re.findall(r'\btooling:\s*(\d+)', block)]
    patterns   = pat_vals[-1]   if pat_vals   else 71
    promptRules = pr_vals[-1]   if pr_vals    else 37
    tooling    = tool_vals[-1]  if tool_vals  else 13
    print(patterns, promptRules, tooling)
except Exception:
    print("71 37 13")
PY
)"

LAST_PATTERNS=$(echo "$LAST_COUNTERS" | awk '{print $1}')
LAST_PROMPTRULES=$(echo "$LAST_COUNTERS" | awk '{print $2}')
LAST_TOOLING=$(echo "$LAST_COUNTERS" | awk '{print $3}')

# ---------------------------------------------------------------------------
# Collect skill/process/tooling commits — two repos
# ---------------------------------------------------------------------------
KEYWORD_RE='feat\(tools\)|chore\(tools\)|fix\(tools\)|skill|feat\(reviews\).*(gate|automation|tracking|instrument|ledger)|watchdog|pattern-0|prompt.?rule|protocol|self-improve|freshness|autolog|directive'

# Helper: gather commits from a repo since SINCE, filtered by keyword subject OR
# path touch (tools/ for bigbounce, astrostack/ for scistack).
# Output: lines of "SHORT_SHA REPO_TAG DATE_ISO SUBJECT"

collect_commits() {
  local repo_dir="$1" tag="$2" path_filter="$3"

  # Guard: skip absent repos silently
  if [ ! -d "$repo_dir/.git" ] && [ ! -f "$repo_dir/.git" ]; then
    return
  fi

  # 1) commits matching keyword on the subject (any path)
  git -C "$repo_dir" log \
    --since="$SINCE" \
    --format="%h|$tag|%ci|%s" \
    2>/dev/null \
    | grep -iE "$KEYWORD_RE" \
    | awk -F'|' '{
        split($3,d," "); date_iso=substr(d[1],1,10);
        printf "%s %s %s %s\n", $1, $2, date_iso, $4
      }' \
    || true

  # 2) commits touching the path_filter (any subject)
  git -C "$repo_dir" log \
    --since="$SINCE" \
    --format="%h|$tag|%ci|%s" \
    -- "$path_filter" \
    2>/dev/null \
    | awk -F'|' '{
        split($3,d," "); date_iso=substr(d[1],1,10);
        printf "%s %s %s %s\n", $1, $2, date_iso, $4
      }' \
    || true
}

BB_COMMITS="$(collect_commits "$REPO" "bigbounce" "tools/")"
SC_COMMITS="$(collect_commits "$SCISTACK" "scistack" "astrostack/")"

ALL_COMMITS_RAW="$(printf '%s\n%s\n' "$BB_COMMITS" "$SC_COMMITS" | grep -v '^[[:space:]]*$' || true)"

# ---------------------------------------------------------------------------
# De-duplicate and sort via python3 (use a temp file to avoid stdin conflict
# between the pipe and the heredoc — python3 reads the data file, the script
# is supplied as the heredoc via process substitution).
# ---------------------------------------------------------------------------
_TMPRAW="$(mktemp /tmp/skills_autolog_raw.XXXXXX)"
printf '%s\n' "$ALL_COMMITS_RAW" > "$_TMPRAW"
COMMITS_DEDUPED="$(python3 <<PY
import sys, os

raw_path = "$_TMPRAW"
try:
    with open(raw_path) as fh:
        raw = fh.read()
except Exception:
    raw = ""

seen = {}
lines = []
for line in raw.splitlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split(None, 3)
    if len(parts) < 4:
        continue
    sha = parts[0]
    if sha not in seen:
        seen[sha] = True
        lines.append(line)
lines.sort(key=lambda l: l.split(None, 3)[2])
print("\\n".join(lines))
PY
)"
rm -f "$_TMPRAW"

BB_COUNT="$(printf '%s\n' "$ALL_COMMITS_RAW" | grep -c 'bigbounce' 2>/dev/null | tr -dc '0-9' || true)"
BB_COUNT="${BB_COUNT:-0}"
SC_COUNT="$(printf '%s\n' "$ALL_COMMITS_RAW" | grep -c 'scistack' 2>/dev/null | tr -dc '0-9' || true)"
SC_COUNT="${SC_COUNT:-0}"
TOTAL_COUNT="$(printf '%s\n' "$COMMITS_DEDUPED" | grep -c '[^[:space:]]' 2>/dev/null | tr -dc '0-9' || true)"
TOTAL_COUNT="${TOTAL_COUNT:-0}"

# ---------------------------------------------------------------------------
# Count newly added .sh/.py/.mjs files in tools/ since SINCE (for tooling delta)
# ---------------------------------------------------------------------------
NEW_TOOLS_COUNT=0
if [ -d "$REPO/.git" ] || [ -f "$REPO/.git" ]; then
  _raw="$(git -C "$REPO" log \
    --since="$SINCE" \
    --diff-filter=A \
    --name-only \
    --format="" \
    -- "tools/" \
    2>/dev/null | grep -E '\.(sh|py|mjs)$' | wc -l | tr -dc '0-9' || true)"
  [ -n "$_raw" ] && NEW_TOOLS_COUNT="$_raw"
fi

NEW_TOOLING=$(( ${LAST_TOOLING:-0} + ${NEW_TOOLS_COUNT:-0} ))

# ---------------------------------------------------------------------------
# --check mode: report unlogged commits and exit
# ---------------------------------------------------------------------------
if [ "$CHECK_MODE" -eq 1 ]; then
  if [ "$TOTAL_COUNT" -eq 0 ]; then
    exit 0
  fi

  # Read reviewTimeline.ts to check which shas are already logged
  TIMELINE_TEXT="$(cat "$REVIEW_TIMELINE" 2>/dev/null || echo "")"

  UNLOGGED_COUNT=0
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    SHA="$(echo "$line" | awk '{print $1}')"
    if [ -z "$SHA" ]; then continue; fi
    if ! printf '%s' "$TIMELINE_TEXT" | grep -qF "$SHA"; then
      UNLOGGED_COUNT=$(( UNLOGGED_COUNT + 1 ))
    fi
  done <<EOF
$COMMITS_DEDUPED
EOF

  if [ "$UNLOGGED_COUNT" -gt 0 ]; then
    echo "skillslog: ${UNLOGGED_COUNT} unlogged skill/process improvement(s) since ${SINCE} (run tools/skills_autolog.sh to draft)" >&2
    exit 2
  fi
  exit 0
fi

# ---------------------------------------------------------------------------
# Default mode: emit draft entries
# ---------------------------------------------------------------------------
python3 - \
  "$COMMITS_DEDUPED" \
  "$SINCE" \
  "$LAST_PATTERNS" "$LAST_PROMPTRULES" "$LAST_TOOLING" \
  "$NEW_TOOLING" "$NEW_TOOLS_COUNT" \
  "$GH_BASE" \
  "$TOTAL_COUNT" "$BB_COUNT" "$SC_COUNT" \
  <<'PY'
import sys, re

commits_raw = sys.argv[1]
since       = sys.argv[2]
patterns    = int(sys.argv[3])
prompt_rules= int(sys.argv[4])
last_tooling= int(sys.argv[5])
new_tooling = int(sys.argv[6])
new_tools_n = int(sys.argv[7])
gh_base     = sys.argv[8]
total_count = int(sys.argv[9])
bb_count    = int(sys.argv[10])
sc_count    = int(sys.argv[11])

GH_COMMIT = f"{gh_base}/commit"
GH        = f"{gh_base}/blob/main"

# Parse commit lines: SHA REPO DATE SUBJECT
commits = []
for line in commits_raw.splitlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split(None, 3)
    if len(parts) < 4:
        continue
    sha, repo, date, subject = parts[0], parts[1], parts[2], parts[3]
    commits.append({"sha": sha, "repo": repo, "date": date, "subject": subject})

if not commits:
    newest_date = since if re.match(r'\d{4}-\d{2}-\d{2}', since) else "2026-07-11"
else:
    newest_date = max(c["date"] for c in commits)

# Build note string for skillsSeries (sha-cited)
if commits:
    sha_list = "; ".join(f"{c['repo']} {c['sha']} ({c['subject'][:60]})" for c in commits)
    tooling_note = (
        f"+{new_tools_n} new tools/ script(s) added since {since} (tooling {last_tooling}→{new_tooling}). "
        if new_tools_n > 0
        else f"tooling unchanged at {last_tooling}. "
    )
    note = (
        f"Auto-logged {len(commits)} skill/process/tooling commit(s) since {since}: {sha_list}. "
        + tooling_note
        + "patterns/promptRules: # TODO verify — human check required."
    )
else:
    note = f"No new skill/process/tooling commits found since {since}. All surfaces current."

# Build links list
links = []
for c in commits:
    if c["repo"] == "bigbounce":
        links.append(f'      {{ label: "commit {c["sha"]}", href: `${{GH_COMMIT}}/{c["sha"]}` }},')
    else:
        links.append(f'      {{ label: "scistack {c["sha"]}", href: "https://github.com/Hubify-Projects/bigbounce/commit/{c["sha"]}" }},')

links_str = "\n".join(links) if links else '      { label: "no commits", href: "" },'

# Build keyTakeaways (one per commit, truncated to reasonable length)
takeaways = []
for c in commits:
    ta = f'{c["subject"][:90]} — {c["repo"]} {c["sha"]}'
    takeaways.append(f'      "{ta}",')
if not takeaways:
    takeaways = ['      "no new skill/process/tooling commits since last logged point",']
takeaways_str = "\n".join(takeaways)

# Count summary line for the subject list
heading_count = f"{total_count} skill/process/tooling commits found since {since} (bigbounce: {bb_count}, scistack: {sc_count})"

# Commit list lines
if commits:
    commit_lines = "\n".join(
        f"  {c['sha']}  {c['repo']:<10}  {c['date']}  {c['subject']}"
        for c in commits
    )
else:
    commit_lines = "  (none)"

# Build title (first subject if available)
if commits:
    if len(commits) == 1:
        title = f"Skill/process autolog: {commits[0]['subject'][:80]}"
    else:
        title = f"Skill/process autolog {newest_date}: {len(commits)} commits — {commits[-1]['subject'][:50]}..."
else:
    title = f"Skill/process autolog {newest_date}: no new commits"

# Build summary
if commits:
    subject_summary = "; ".join(f"{c['sha']} {c['subject'][:55]}" for c in commits)
    tooling_summary = (
        f"Tooling counter {last_tooling}→{new_tooling} ({new_tools_n} new .sh/.py/.mjs added in tools/)."
        if new_tools_n > 0
        else f"Tooling unchanged at {last_tooling}."
    )
    summary = (
        f"Auto-generated from git log --since={since}: {len(commits)} skill/process/tooling commit(s) "
        f"found ({bb_count} bigbounce, {sc_count} scistack). {tooling_summary} "
        f"Commits: {subject_summary}. # TODO verify patterns/promptRules counters before pasting."
    )
else:
    summary = f"No new skill/process/tooling commits found since {since} — skills chart is current."

id_slug = f"autolog-{newest_date}"

print(f"""
=== DRAFT skillsSeries point (paste into site/src/data/reviewTimeline.ts) ===
  {{ id: "{id_slug}", dateISO: "{newest_date}", patterns: {patterns}, promptRules: {prompt_rules}, tooling: {new_tooling}, note: "{note}" }},
  // ^ patterns: {patterns} # TODO verify (script cannot count new review-patterns)
  // ^ promptRules: {prompt_rules} # TODO verify (script cannot count new reviewer-prompt rules)
  // ^ tooling: {new_tooling} = last({last_tooling}) + {new_tools_n} new tools/ scripts added since {since}

=== DRAFT reviewTimeline skill-improvement entry (paste into reviewRounds[]) ===
  {{
    id: "{id_slug}",
    dateISO: "{newest_date}",
    kind: "skill-improvement",
    title:
      "{title}",
    papers: ["P1A", "P1B", "P2", "P3", "P4", "P5"],
    summary:
      "{summary}",
    keyTakeaways: [
{takeaways_str}
    ],
    links: [
{links_str}
    ],
  }},

=== {heading_count} ===
{commit_lines}
""")
PY

