#!/usr/bin/env bash
# site_freshness_check.sh — machine-checkable site-freshness gate.
#
# Kills the recurring stale-surface failure class (overview banner N days old,
# skills chart flat for days, missing board rounds, stale version chips).
# Surface sync used to depend on agents remembering; this checks it mechanically.
#
# Checks (exit 1 if ANY stale, exit 0 = all fresh):
#   1. Banner   — live-status.ts lastUpdatedISO vs newest wave (Convex listWaves)
#                 and newest harvested EXT manifest row. Stale if >6h older.
#   2. Skills   — last skillsSeries point vs newest lesson-commit
#                 (~/.claude/scistack .../bigbounce-r-round/SKILL.md) and newest
#                 tools/ commit. Stale if a commit is >12h newer.
#   3. Board    — latest externalVerdictRounds date vs newest harvested round.
#                 Stale if a harvested round has no board entry after 6h.
#   4. Versions — Convex paperVersions:current per paper MUST appear in
#                 live-status.ts. Reports each mismatch.
#
# Flags:
#   --report   print a table either way (default: silent on pass)
#
# INSTALL the pre-push hook (blocks push on stale; override FRESHNESS_SKIP=1):
#   cp tools/hooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push
#
# bash-3.2 safe. macOS `stat -f`, `date` handled with a python fallback.

set -uo pipefail

REPO="/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
LIVE_STATUS="$REPO/site/src/data/live-status.ts"
REVIEW_TIMELINE="$REPO/site/src/data/reviewTimeline.ts"
EXT_REAL="$REPO/project-context/peer-reviews/EXT_real"
CONVEX_URL="https://brilliant-panther-471.convex.cloud"
SCISTACK="$HOME/.claude/scistack"
SKILL_MD_REL="astrostack/bigbounce-r-round/SKILL.md"

REPORT=0
for a in "$@"; do
  case "$a" in
    --report) REPORT=1 ;;
  esac
done

# All parsing + comparison is done in one python pass for robustness. It prints
# lines "STATUS<TAB>SURFACE<TAB>DETAIL" then a final "OVERALL<TAB>PASS|FAIL".
HEARTBEAT="$REPO/project-context/LOOP_HEARTBEAT.json"
PYOUT="$(python3 - "$LIVE_STATUS" "$REVIEW_TIMELINE" "$EXT_REAL" "$CONVEX_URL" "$SCISTACK/$SKILL_MD_REL" "$REPO" "$HEARTBEAT" <<'PY'
import sys, os, re, json, subprocess, glob
from datetime import datetime, timezone

live_status, review_timeline, ext_real, convex_url, skill_md, repo, heartbeat = sys.argv[1:8]

def now_utc():
    return datetime.now(timezone.utc)

def parse_iso(s):
    """Parse an ISO-8601 datetime or a bare YYYY-MM-DD date to aware UTC."""
    if not s:
        return None
    s = s.strip()
    m = re.match(r'^(\d{4}-\d{2}-\d{2})$', s)
    if m:
        return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    t = s.replace("Z", "+00:00")
    try:
        d = datetime.fromisoformat(t)
    except Exception:
        m = re.match(r'^(\d{4}-\d{2}-\d{2})', s)
        if not m:
            return None
        return datetime.strptime(m.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)

def hours_between(a, b):
    return (a - b).total_seconds() / 3600.0

def read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ""

def convex_query(path, args=None):
    body = json.dumps({"path": path, "args": args or {}})
    try:
        p = subprocess.run(
            ["curl", "-s", "-X", "POST", f"{convex_url}/api/query",
             "-H", "Content-Type: application/json", "-d", body],
            capture_output=True, text=True, timeout=30)
        d = json.loads(p.stdout)
        if d.get("status") != "success":
            return None
        return d.get("value")
    except Exception:
        return None

def git_last_commit_iso(cwd, path):
    try:
        p = subprocess.run(
            ["git", "-C", cwd, "log", "-1", "--format=%cI", "--", path],
            capture_output=True, text=True, timeout=30)
        return parse_iso(p.stdout.strip()) if p.stdout.strip() else None
    except Exception:
        return None

def slice_array(text, const_name):
    """Return the substring of the named `export const NAME ... [ ... ]` block."""
    m = re.search(r'export const %s\b' % re.escape(const_name), text)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r'\nexport const ', text[start:])
    end = start + nxt.start() if nxt else len(text)
    return text[start:end]

now = now_utc()
results = []  # (status, surface, detail)  status in FRESH/STALE/WARN
overall_fail = False

ls_text = read(live_status)
rt_text = read(review_timeline)

# ---------------------------------------------------------------------------
# newest wave dateISO (Convex) + newest harvested EXT manifest row
# ---------------------------------------------------------------------------
waves = convex_query("readinessMetrics:listWaves") or []
newest_wave = None
newest_wave_label = ""
for w in waves:
    d = parse_iso(w.get("dateISO", ""))
    if d and (newest_wave is None or d > newest_wave):
        newest_wave = d
        newest_wave_label = w.get("waveLabel", "?")

# newest harvested manifest row: use directory-name date + file mtime as the
# freshness signal (manifest rows have inconsistent per-row date fields).
newest_harvest = None
newest_harvest_src = ""
for mf in glob.glob(os.path.join(ext_real, "**", "manifest.jsonl"), recursive=True):
    # any row with a harvested-ish status counts; else fall back to file mtime.
    has_harvest = False
    try:
        for line in open(mf):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            st = str(r.get("status", "")).lower()
            if "harvest" in st or r.get("verdict"):
                has_harvest = True
                break
    except Exception:
        pass
    # date from the directory name (…/LABEL_YYYY-MM-DD/…)
    dm = re.search(r'(\d{4}-\d{2}-\d{2})', mf)
    dir_date = parse_iso(dm.group(1)) if dm else None
    mtime = datetime.fromtimestamp(os.path.getmtime(mf), tz=timezone.utc)
    cand = mtime if not dir_date else max(dir_date, mtime) if False else mtime
    # use file mtime (real harvest write time) when the row is harvested;
    # else the directory date (submission day).
    cand = mtime if has_harvest else (dir_date or mtime)
    if cand and (newest_harvest is None or cand > newest_harvest):
        newest_harvest = cand
        newest_harvest_src = os.path.relpath(mf, repo)

# ---------------------------------------------------------------------------
# 1. BANNER
# ---------------------------------------------------------------------------
m = re.search(r'lastUpdatedISO:\s*"([^"]+)"', ls_text)
banner = parse_iso(m.group(1)) if m else None
newest_activity = None
na_src = ""
for cand, src in ((newest_wave, "Convex wave %s" % newest_wave_label),
                  (newest_harvest, "harvest %s" % newest_harvest_src)):
    if cand and (newest_activity is None or cand > newest_activity):
        newest_activity = cand
        na_src = src
if banner is None:
    results.append(("STALE", "banner", "could not parse lastUpdatedISO"))
    overall_fail = True
elif newest_activity is None:
    results.append(("WARN", "banner", "no wave/harvest to compare against"))
else:
    lag = hours_between(newest_activity, banner)  # activity newer than banner => positive
    if lag > 6:
        results.append(("STALE", "banner",
            "banner %s is %.1fh older than newest %s (%s)" %
            (banner.isoformat(), lag, na_src, newest_activity.isoformat())))
        overall_fail = True
    else:
        results.append(("FRESH", "banner",
            "banner %s within 6h of newest %s (%s; lag %.1fh)" %
            (banner.isoformat(), na_src, newest_activity.isoformat(), lag)))

# ---------------------------------------------------------------------------
# 2. SKILLS SERIES
# ---------------------------------------------------------------------------
skills_block = slice_array(rt_text, "skillsSeries")
skill_dates = [parse_iso(x) for x in re.findall(r'dateISO:\s*"([0-9-]+)"', skills_block)]
skill_dates = [d for d in skill_dates if d]
last_skill = max(skill_dates) if skill_dates else None
# resolve scistack repo root + the relative SKILL.md path
scistack_root = skill_md.split("/astrostack/")[0]
skill_rel = "astrostack/" + skill_md.split("/astrostack/")[1]
skill_commit = git_last_commit_iso(scistack_root, skill_rel)
tools_commit = git_last_commit_iso(repo, "tools/")

newest_lesson = None
nl_src = ""
for cand, src in ((skill_commit, "scistack SKILL.md"), (tools_commit, "tools/")):
    if cand and (newest_lesson is None or cand > newest_lesson):
        newest_lesson = cand
        nl_src = src
if last_skill is None:
    results.append(("STALE", "skills", "no dated skillsSeries points found"))
    overall_fail = True
elif newest_lesson is None:
    results.append(("WARN", "skills", "no lesson/tool commit to compare against"))
else:
    lag = hours_between(newest_lesson, last_skill)
    if lag > 12:
        results.append(("STALE", "skills",
            "last skills point %s is %.1fh behind newest %s commit (%s)" %
            (last_skill.date().isoformat(), lag, nl_src, newest_lesson.isoformat())))
        overall_fail = True
    else:
        results.append(("FRESH", "skills",
            "last skills point %s within 12h of newest %s commit (lag %.1fh)" %
            (last_skill.date().isoformat(), nl_src, lag)))

# ---------------------------------------------------------------------------
# 3. BOARD (externalVerdictRounds latest date vs newest harvested round)
# ---------------------------------------------------------------------------
board_block = slice_array(rt_text, "externalVerdictRounds")
board_dates = [parse_iso(x) for x in re.findall(r'dateISO:\s*"([0-9-]+)"', board_block)]
board_dates = [d for d in board_dates if d]
last_board = max(board_dates) if board_dates else None
# newest harvested round: use the directory-date of any manifest that has a
# harvested row (a submitted round with results the board must reflect).
newest_harvested_round = None
nhr_src = ""
for mf in glob.glob(os.path.join(ext_real, "**", "manifest.jsonl"), recursive=True):
    harvested = False
    try:
        for line in open(mf):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            st = str(r.get("status", "")).lower()
            if "harvest" in st or r.get("verdict"):
                harvested = True
                break
    except Exception:
        pass
    if not harvested:
        continue
    dm = re.search(r'(\d{4}-\d{2}-\d{2})', mf)
    dd = parse_iso(dm.group(1)) if dm else None
    if dd and (newest_harvested_round is None or dd > newest_harvested_round):
        newest_harvested_round = dd
        nhr_src = os.path.relpath(mf, repo)
if last_board is None:
    results.append(("STALE", "board", "no externalVerdictRounds dates found"))
    overall_fail = True
elif newest_harvested_round is None:
    results.append(("WARN", "board", "no harvested round to compare against"))
else:
    # stale if a harvested round is newer than the last board entry by >6h
    lag = hours_between(newest_harvested_round, last_board)
    if lag > 6:
        results.append(("STALE", "board",
            "harvested round %s (%s) has no board entry (latest board %s; +%.1fh)" %
            (newest_harvested_round.date().isoformat(), nhr_src,
             last_board.date().isoformat(), lag)))
        overall_fail = True
    else:
        results.append(("FRESH", "board",
            "latest board %s covers newest harvested round %s" %
            (last_board.date().isoformat(), newest_harvested_round.date().isoformat())))

# ---------------------------------------------------------------------------
# 4. VERSIONS (Convex paperVersions:current must appear in live-status.ts)
# ---------------------------------------------------------------------------
slugs = ["paper-1a", "paper-2", "paper-3", "paper-4", "paper-5"]
mismatches = []
oks = []
for slug in slugs:
    cur = convex_query("paperVersions:current", {"paperSlug": slug})
    if not isinstance(cur, dict):
        mismatches.append("%s: Convex current unavailable" % slug)
        continue
    ver = cur.get("version", "")
    if not ver:
        mismatches.append("%s: Convex version empty" % slug)
        continue
    if ver in ls_text:
        oks.append("%s=%s" % (slug, ver))
    else:
        mismatches.append("%s: Convex %s NOT in live-status.ts" % (slug, ver))
if mismatches:
    for mm in mismatches:
        results.append(("STALE", "versions", mm))
    overall_fail = True
else:
    results.append(("FRESH", "versions", "all match: " + ", ".join(oks)))

# ---------------------------------------------------------------------------
# 5. HEARTBEAT (loop liveness — report-level; the launchd watchdog is the actor)
#    STALE if LOOP_HEARTBEAT.json lastTickUTC is >45min old (or missing).
#    This is a REPORT signal only: tools/loop_watchdog.sh (launchd, ~15min) is
#    what actually notifies + posts a Convex alert + fires recovery.
# ---------------------------------------------------------------------------
try:
    hb = json.load(open(heartbeat))
    last = parse_iso(hb.get("lastTickUTC", ""))
    if last is None:
        results.append(("STALE", "heartbeat", "LOOP_HEARTBEAT.json has no parseable lastTickUTC"))
        overall_fail = True
    else:
        age_min = (now_utc() - last).total_seconds() / 60.0
        if age_min > 45:
            results.append(("STALE", "heartbeat",
                "loop heartbeat %.0fmin old (>45min) — watchdog should have fired; check LOOP_WATCHDOG_LOG.md" % age_min))
            overall_fail = True
        else:
            results.append(("FRESH", "heartbeat", "loop heartbeat %.0fmin old" % age_min))
except FileNotFoundError:
    results.append(("STALE", "heartbeat", "LOOP_HEARTBEAT.json missing — loop never started / watchdog down"))
    overall_fail = True
except Exception as e:
    results.append(("WARN", "heartbeat", "could not read heartbeat: %s" % e))

# emit
for status, surface, detail in results:
    print("%s\t%s\t%s" % (status, surface, detail))
print("OVERALL\t%s\t" % ("FAIL" if overall_fail else "PASS"))
PY
)"

RC=$?
if [ $RC -ne 0 ] && [ -z "$PYOUT" ]; then
  echo "site_freshness_check: internal error running checks" >&2
  exit 2
fi

# ---------------------------------------------------------------------------
# 6. SKILLSLOG (WARN-level — does NOT flip OVERALL to FAIL).
#    tools/skills_autolog.sh --check exits 2 when git history has skill/process/
#    tooling commits whose sha is not yet in reviewTimeline.ts. That is a "you
#    have un-drafted self-improvement to log" nudge, not a blocking staleness —
#    so it is reported WARN and never blocks a push. Run tools/skills_autolog.sh
#    (no flag) to get paste-ready drafts.
SKILLSLOG_SH="$REPO/tools/skills_autolog.sh"
if [ -x "$SKILLSLOG_SH" ]; then
  SKILLSLOG_MSG="$("$SKILLSLOG_SH" --check 2>&1)"
  SKILLSLOG_RC=$?
  if [ "$SKILLSLOG_RC" -eq 2 ]; then
    SKILLSLOG_ROW="WARN	skillslog	${SKILLSLOG_MSG:-unlogged skill/process improvements found}"
  elif [ "$SKILLSLOG_RC" -eq 0 ]; then
    SKILLSLOG_ROW="FRESH	skillslog	all skill/process improvements logged in reviewTimeline.ts"
  else
    SKILLSLOG_ROW="WARN	skillslog	skills_autolog --check error (rc=$SKILLSLOG_RC): ${SKILLSLOG_MSG}"
  fi
  # Insert the skillslog row BEFORE the OVERALL line so it renders in the table
  # body. WARN never flips OVERALL (that stays whatever the 5 gate checks decided).
  PYOUT="$(printf '%s\n' "$PYOUT" | awk -v row="$SKILLSLOG_ROW" -F'\t' \
    '$1=="OVERALL"{print row} {print}')"
fi

OVERALL="$(printf '%s\n' "$PYOUT" | awk -F'\t' '$1=="OVERALL"{print $2}')"

print_table() {
  printf '%-8s %-9s %s\n' "STATUS" "SURFACE" "DETAIL"
  printf '%-8s %-9s %s\n' "------" "-------" "------"
  printf '%s\n' "$PYOUT" | awk -F'\t' '$1!="OVERALL"{printf "%-8s %-9s %s\n",$1,$2,$3}'
  echo "---"
  echo "OVERALL: $OVERALL"
}

if [ "$OVERALL" = "PASS" ]; then
  [ $REPORT -eq 1 ] && print_table
  exit 0
else
  # always print the report on failure (which surface + why)
  echo "SITE FRESHNESS: STALE — fix the surfaces below IN THIS COMMIT before pushing:" >&2
  print_table >&2
  exit 1
fi
