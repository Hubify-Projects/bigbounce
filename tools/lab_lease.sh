#!/usr/bin/env bash
# lab_lease.sh — single-driver lease coordinated through an isolated git CAS.
#
# The lease is stored at ops/handoff/LEASE.json on origin/main. Every command
# reads a freshly fetched remote snapshot. Mutating commands build a commit with
# a temporary index + git commit-tree, then push with --force-with-lease against
# the fetched parent. They never checkout, pull, rebase, stash, stage, commit, or
# otherwise modify the caller's worktree, index, or current branch.
#
# Usage:
#   lab_lease.sh claim   <machine-id> <ttl-minutes>
#   lab_lease.sh renew   <machine-id> [<ttl-minutes>]
#   lab_lease.sh release <machine-id>
#   lab_lease.sh status
#   lab_lease.sh holds   <machine-id>
#
# Exit codes: 0 success/fresh hold; 1 denied/not holder; 2 invalid invocation;
# 3 expired; 4 free; 5 remote/parse/CAS failure (fail closed).

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEASE_REL="ops/handoff/LEASE.json"
REMOTE="${BIGBOUNCE_LEASE_REMOTE:-origin}"
BRANCH="${BIGBOUNCE_LEASE_BRANCH:-main}"
BRANCH_REF="refs/heads/$BRANCH"
REMOTE_REF="refs/remotes/$REMOTE/$BRANCH"
CONVEX_MUTATION_URL="https://brilliant-panther-471.convex.cloud/api/mutation"

TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/bigbounce-lease.XXXXXX")" || exit 5
SNAPSHOT="$TMP_DIR/LEASE.remote.json"
CANDIDATE="$TMP_DIR/LEASE.candidate.json"
INDEX_FILE="$TMP_DIR/index"
trap 'rm -rf "$TMP_DIR"' EXIT HUP INT TERM

now_iso() { date -u +%Y-%m-%dT%H:%M:%SZ; }
now_epoch() { date -u +%s; }
_git() { git -C "$REPO_ROOT" "$@"; }
_closed() { echo "ERROR: $* (lease state unknown; failing closed)." >&2; exit 5; }

_validate_machine_id() {
  case "${1:-}" in
    ""|*[!A-Za-z0-9._-]*|-*|.*|_* )
      echo "ERROR: machine-id must be 1-64 chars, start alphanumeric, and use only A-Z a-z 0-9 . _ -." >&2
      return 1 ;;
  esac
  [ "${#1}" -le 64 ] || {
    echo "ERROR: machine-id exceeds 64 characters." >&2
    return 1
  }
}

_validate_ttl() {
  case "${1:-}" in
    ""|*[!0-9]*) echo "ERROR: ttl-minutes must be an integer from 5 through 240." >&2; return 1 ;;
  esac
  [ "$1" -ge 5 ] 2>/dev/null && [ "$1" -le 240 ] 2>/dev/null || {
    echo "ERROR: ttl-minutes must be from 5 through 240." >&2
    return 1
  }
}

_validate_snapshot() {
  python3 - "$SNAPSHOT" <<'PY' >/dev/null 2>&1
import datetime, json, re, sys
d = json.load(open(sys.argv[1]))
required = {"holder", "claimedUTC", "expiresUTC", "ttlMinutes", "lastAction", "seq"}
assert isinstance(d, dict) and required <= set(d)
holder = d["holder"]
assert isinstance(holder, str)
assert holder == "" or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", holder)
assert isinstance(d["claimedUTC"], str)
assert isinstance(d["expiresUTC"], str) and d["expiresUTC"]
datetime.datetime.fromisoformat(d["expiresUTC"].replace("Z", "+00:00"))
assert isinstance(d["ttlMinutes"], int) and not isinstance(d["ttlMinutes"], bool)
assert (holder == "" and d["ttlMinutes"] == 0) or (holder != "" and 5 <= d["ttlMinutes"] <= 240)
assert isinstance(d["lastAction"], str)
assert isinstance(d["seq"], int) and not isinstance(d["seq"], bool) and d["seq"] >= 0
PY
}

_remote_snapshot() {
  # Fetch only the lease branch. Updating a remote-tracking ref does not touch
  # HEAD, the worktree, or the user's index.
  _git fetch --quiet --no-tags "$REMOTE" "+$BRANCH_REF:$REMOTE_REF" || return 1
  BASE_SHA="$(_git rev-parse --verify "$REMOTE_REF^{commit}" 2>/dev/null)" || return 1
  _git cat-file -e "$BASE_SHA:$LEASE_REL" 2>/dev/null || return 1
  _git show "$BASE_SHA:$LEASE_REL" > "$SNAPSHOT" 2>/dev/null || return 1
  _validate_snapshot || return 1
}

_field() {
  python3 - "$SNAPSHOT" "$1" <<'PY'
import json, sys
v = json.load(open(sys.argv[1]))[sys.argv[2]]
print(v)
PY
}

_expiry_epoch() {
  python3 - "$SNAPSHOT" <<'PY' 2>/dev/null
import datetime, json, sys
s = json.load(open(sys.argv[1]))["expiresUTC"].replace("Z", "+00:00")
print(int(datetime.datetime.fromisoformat(s).timestamp()))
PY
}

_is_fresh() {
  local holder exp
  holder="$(_field holder)" || return 1
  [ -n "$holder" ] || return 1
  exp="$(_expiry_epoch)" || return 1
  [ "$exp" -gt "$(now_epoch)" ] 2>/dev/null
}

_render_candidate() { # holder ttl action
  python3 - "$SNAPSHOT" "$CANDIDATE" "$1" "$2" "$3" "$(now_iso)" <<'PY'
import datetime, json, sys
src, out, holder, ttl, action, now = sys.argv[1:7]
old = json.load(open(src))
ttl = int(ttl)
dt = datetime.datetime.fromisoformat(now.replace("Z", "+00:00"))
if holder:
    claimed = old["claimedUTC"] if action == "renew" and old["claimedUTC"] else now
    expires = (dt + datetime.timedelta(minutes=ttl)).strftime("%Y-%m-%dT%H:%M:%SZ")
else:
    claimed, expires, ttl = "", now, 0
doc = {
    "holder": holder,
    "claimedUTC": claimed,
    "expiresUTC": expires,
    "ttlMinutes": ttl,
    "lastAction": action,
    "seq": int(old["seq"]) + 1,
}
with open(out, "w") as f:
    json.dump(doc, f, indent=2)
    f.write("\n")
PY
}

_publish_candidate() { # commit message; return 0 pushed, 1 CAS lost/error
  local msg="$1" blob tree commit
  rm -f "$INDEX_FILE"
  GIT_INDEX_FILE="$INDEX_FILE" _git read-tree "$BASE_SHA" >/dev/null 2>&1 || return 1
  blob="$(_git hash-object -w "$CANDIDATE")" || return 1
  GIT_INDEX_FILE="$INDEX_FILE" _git update-index --add --cacheinfo "100644,$blob,$LEASE_REL" >/dev/null 2>&1 || return 1
  tree="$(GIT_INDEX_FILE="$INDEX_FILE" _git write-tree)" || return 1
  commit="$(printf '%s\n' "$msg" | \
    GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-bigbounce-lab-lease}" \
    GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-lab-lease@bigbounce.local}" \
    GIT_COMMITTER_NAME="${GIT_COMMITTER_NAME:-bigbounce-lab-lease}" \
    GIT_COMMITTER_EMAIL="${GIT_COMMITTER_EMAIL:-lab-lease@bigbounce.local}" \
    _git commit-tree "$tree" -p "$BASE_SHA")" || return 1
  _git push --quiet --no-verify \
    --force-with-lease="$BRANCH_REF:$BASE_SHA" \
    "$REMOTE" "$commit:$BRANCH_REF" >/dev/null 2>&1
}

_convex_note() {
  [ "${BIGBOUNCE_LEASE_CONVEX_NOTE:-1}" = "1" ] || return 0
  command -v curl >/dev/null 2>&1 || return 0
  local payload
  payload="$(python3 - "$1" "$2" "$(now_iso)" <<'PY' 2>/dev/null
import json, sys
title, body, iso = sys.argv[1:4]
print(json.dumps({"path":"activityFeed:add","args":{"type":"ops","date":iso,
  "title":title,"body":body,"tags":[{"label":"lab-lease","kind":"info"}]},
  "format":"json"}))
PY
)"
  [ -n "$payload" ] || return 0
  curl -sS -m 8 -X POST "$CONVEX_MUTATION_URL" \
    -H 'Content-Type: application/json' -d "$payload" >/dev/null 2>&1 || true
}

cmd="${1:-status}"
[ "$#" -gt 0 ] && shift

case "$cmd" in
  claim)
    [ "$#" -eq 2 ] || { echo "usage: lab_lease.sh claim <machine-id> <ttl-minutes>" >&2; exit 2; }
    MACHINE_ID="$1"; TTL="$2"
    _validate_machine_id "$MACHINE_ID" && _validate_ttl "$TTL" || exit 2
    _remote_snapshot || _closed "cannot fetch or validate $REMOTE/$BRANCH:$LEASE_REL"
    holder="$(_field holder)"
    if _is_fresh && [ "$holder" != "$MACHINE_ID" ]; then
      echo "DENIED: lease held by '$holder' until $(_field expiresUTC) (fresh)."
      exit 1
    fi
    _render_candidate "$MACHINE_ID" "$TTL" "claim" || _closed "cannot render lease candidate"
    if _publish_candidate "chore(lab-lease): $MACHINE_ID claim ttl=${TTL}m"; then
      echo "CLAIMED: $MACHINE_ID holds the lab lease for ${TTL}m."
      _convex_note "Lab lease claimed" "$MACHINE_ID is now the single lab driver (ttl ${TTL}m)."
      exit 0
    fi
    _remote_snapshot >/dev/null 2>&1 || _closed "claim CAS failed and the winning lease cannot be read"
    echo "DENIED: claim lost the compare-and-swap race; current holder '$(_field holder)'."
    exit 1
    ;;
  renew)
    [ "$#" -ge 1 ] && [ "$#" -le 2 ] || { echo "usage: lab_lease.sh renew <machine-id> [<ttl-minutes>]" >&2; exit 2; }
    MACHINE_ID="$1"; _validate_machine_id "$MACHINE_ID" || exit 2
    _remote_snapshot || _closed "cannot fetch or validate $REMOTE/$BRANCH:$LEASE_REL"
    holder="$(_field holder)"
    if [ "$holder" != "$MACHINE_ID" ] || ! _is_fresh; then
      echo "REFUSED: '$MACHINE_ID' does not hold the fresh lease (holder '$holder')."
      exit 1
    fi
    TTL="${2:-$(_field ttlMinutes)}"; _validate_ttl "$TTL" || exit 2
    _render_candidate "$MACHINE_ID" "$TTL" "renew" || _closed "cannot render lease candidate"
    if _publish_candidate "chore(lab-lease): $MACHINE_ID renew ttl=${TTL}m"; then
      echo "RENEWED: $MACHINE_ID lease extended for ${TTL}m."
      exit 0
    fi
    _remote_snapshot >/dev/null 2>&1 || _closed "renew CAS failed and the winning lease cannot be read"
    echo "REFUSED: renew lost the compare-and-swap race; current holder '$(_field holder)'."
    exit 1
    ;;
  release)
    [ "$#" -eq 1 ] || { echo "usage: lab_lease.sh release <machine-id>" >&2; exit 2; }
    MACHINE_ID="$1"; _validate_machine_id "$MACHINE_ID" || exit 2
    _remote_snapshot || _closed "cannot fetch or validate $REMOTE/$BRANCH:$LEASE_REL"
    holder="$(_field holder)"
    [ "$holder" = "$MACHINE_ID" ] || {
      echo "REFUSED: lease held by '$holder', not '$MACHINE_ID'."
      exit 1
    }
    _render_candidate "" 0 "release by $MACHINE_ID" || _closed "cannot render release candidate"
    if _publish_candidate "chore(lab-lease): $MACHINE_ID release"; then
      echo "RELEASED: lab lease is FREE."
      _convex_note "Lab lease released" "$MACHINE_ID released the lab lease."
      exit 0
    fi
    _remote_snapshot >/dev/null 2>&1 || _closed "release CAS failed and the winning lease cannot be read"
    echo "REFUSED: release lost the compare-and-swap race; current holder '$(_field holder)'."
    exit 1
    ;;
  status)
    [ "$#" -eq 0 ] || { echo "usage: lab_lease.sh status" >&2; exit 2; }
    _remote_snapshot || _closed "cannot fetch or validate $REMOTE/$BRANCH:$LEASE_REL"
    holder="$(_field holder)"
    if [ -z "$holder" ]; then
      echo "LAB LEASE: FREE."
      exit 4
    fi
    if _is_fresh; then
      echo "LAB LEASE: HELD by '$holder' until $(_field expiresUTC) (FRESH)."
      exit 0
    fi
    echo "LAB LEASE: EXPIRED — last holder '$holder' (expired $(_field expiresUTC))."
    exit 3
    ;;
  holds)
    [ "$#" -eq 1 ] || { echo "usage: lab_lease.sh holds <machine-id>" >&2; exit 2; }
    MACHINE_ID="$1"; _validate_machine_id "$MACHINE_ID" >/dev/null || exit 2
    _remote_snapshot >/dev/null 2>&1 || exit 5
    [ "$(_field holder)" = "$MACHINE_ID" ] && _is_fresh
    exit $?
    ;;
  *)
    echo "usage: lab_lease.sh {claim|renew|release|status|holds} ..." >&2
    exit 2
    ;;
esac
