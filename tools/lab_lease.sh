#!/usr/bin/env bash
# lab_lease.sh — single-driver LAB LEASE across machines (MVP).
#
# WHY: Houston runs ONE lab on two (or more) machines. Both machines pull/push
# the same repo and write the same Convex live state. Without coordination, two
# machines would drive the headed browser EXT sweeps and write competing
# verdict/ledger bundles at the same time (the exact collision directive
# "cron-tick-overlap-detection" warns about). The lease makes exactly ONE
# machine the DRIVER at a time; the other(s) do lease-free work (INT API waves,
# compute, site edits) and wait to claim the driver role.
#
# MECHANISM (MVP tradeoff — deliberately simple):
#   The lease is a git-tracked file  ops/handoff/LEASE.json  claimed via a
#   commit + push RACE with `git pull --rebase` conflict detection. Git is
#   already the sync bus on both machines and already has the pre-push freshness
#   gate, so the lease travels for free and needs NO Convex schema change / no
#   `npx convex deploy`. The cost: claiming is O(seconds) (a pull+push round
#   trip) and the race window is the push latency — acceptable for a 2-machine
#   lab with a ~20-min cron cadence. If contention ever gets tight, promote the
#   lease to a Convex mutation with an atomic compare-and-set; the CLI contract
#   here (claim/status/release/renew/holds) stays identical.
#
# SEMANTICS:
#   lab_lease.sh claim  <machine-id> <ttl-minutes>   # become the driver (fails if held & fresh by another)
#   lab_lease.sh renew  <machine-id> [<ttl-minutes>] # extend your own hold (heartbeat)
#   lab_lease.sh release <machine-id>                # give up the driver role
#   lab_lease.sh status                              # print holder / expiry / freshness (exit 0 held-fresh, 3 expired, 4 free)
#   lab_lease.sh holds  <machine-id>                 # exit 0 iff <machine-id> currently holds a FRESH lease (loop gate)
#
# The loop's browser-driving + ledger/verdict adjudication ONLY proceed while
# `lab_lease.sh holds "$MACHINE_ID"` returns 0. Lease-free work needs no hold.
#
# A dark machine self-heals: its lease TTL expires, and the other machine's
# `claim` succeeds against the expired holder (steal-on-expiry).

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEASE_FILE="$REPO_ROOT/ops/handoff/LEASE.json"
LEASE_REL="ops/handoff/LEASE.json"
CONVEX_MUTATION_URL="https://brilliant-panther-471.convex.cloud/api/mutation"

now_iso()   { date -u +%Y-%m-%dT%H:%M:%SZ; }
now_epoch() { date -u +%s; }

# --- read helpers (tolerate a missing/empty file) -------------------------
_field() { # _field <key>  → prints value or empty
  [ -f "$LEASE_FILE" ] || { echo ""; return; }
  python3 - "$LEASE_FILE" "$1" <<'PY' 2>/dev/null || echo ""
import sys, json
try:
    d = json.load(open(sys.argv[1]))
    print(d.get(sys.argv[2], "") if d else "")
except Exception:
    print("")
PY
}

_expiry_epoch() {
  local exp; exp="$(_field expiresUTC)"
  [ -z "$exp" ] && { echo 0; return; }
  python3 - "$exp" <<'PY' 2>/dev/null || echo 0
import sys, datetime
try:
    s = sys.argv[1].replace("Z", "+00:00")
    print(int(datetime.datetime.fromisoformat(s).timestamp()))
except Exception:
    print(0)
PY
}

_is_fresh() { # 0 = a holder exists AND not expired
  local holder exp_ep now
  holder="$(_field holder)"; [ -z "$holder" ] && return 1
  exp_ep="$(_expiry_epoch)"; now="$(now_epoch)"
  [ "$exp_ep" -gt "$now" ] 2>/dev/null
}

_write_lease() { # _write_lease <holder> <ttl-min> <action>
  local holder="$1" ttl="$2" action="$3" now exp seq
  now="$(now_iso)"
  exp="$(python3 - "$ttl" <<'PY'
import sys, datetime
m = int(sys.argv[1])
print((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=m)).strftime("%Y-%m-%dT%H:%M:%SZ"))
PY
)"
  seq="$(now_epoch)"
  python3 - "$LEASE_FILE" "$holder" "$now" "$exp" "$ttl" "$action" "$seq" <<'PY'
import sys, json
path, holder, iso, exp, ttl, action, seq = sys.argv[1:8]
json.dump({
    "holder": holder,
    "claimedUTC": iso,
    "expiresUTC": exp,
    "ttlMinutes": int(ttl),
    "lastAction": action,
    "seq": int(seq),
}, open(path, "w"), indent=2)
open(path, "a").write("\n")
PY
}

# --- Convex mirror (best-effort; a network failure never blocks the lease) -
_convex_note() { # _convex_note <title> <body>
  command -v curl >/dev/null 2>&1 || return 0
  local payload
  payload="$(python3 - "$1" "$2" "$(now_iso)" <<'PY' 2>/dev/null
import sys, json
title, body, iso = sys.argv[1:4]
print(json.dumps({
    "path": "activityFeed:add",
    "args": {
        "type": "ops",
        "date": iso,
        "title": title,
        "body": body,
        "tags": [{"label": "lab-lease", "kind": "info"}],
    },
    "format": "json",
}))
PY
)"
  [ -z "$payload" ] && return 0
  curl -sS -m 8 -X POST "$CONVEX_MUTATION_URL" \
    -H 'Content-Type: application/json' -d "$payload" >/dev/null 2>&1 || true
}

# --- git sync helpers ------------------------------------------------------
_git() { git -C "$REPO_ROOT" "$@"; }

_pull_rebase() {
  # bring LEASE.json current; --autostash so an in-flight working tree is fine.
  _git pull --rebase --autostash --no-edit >/dev/null 2>&1
}

_commit_push_lease() { # _commit_push_lease <msg>  → 0 pushed, 1 lost-race/failed
  _git add "$LEASE_REL" >/dev/null 2>&1
  _git commit -m "$1" --no-verify >/dev/null 2>&1 || return 1
  # FRESHNESS_SKIP: the lease commit only touches LEASE.json — the site-freshness
  # pre-push gate is about paper/site surfaces, irrelevant here.
  if FRESHNESS_SKIP=1 _git push --no-verify >/dev/null 2>&1; then
    return 0
  fi
  # rejected → someone else pushed first. Rebase and report lost race so the
  # caller re-reads the (possibly now-held-by-other) lease.
  _pull_rebase
  return 1
}

# ==========================================================================
cmd="${1:-status}"; shift || true

case "$cmd" in
  claim)
    MACHINE_ID="${1:?usage: lab_lease.sh claim <machine-id> <ttl-minutes>}"
    TTL="${2:?usage: lab_lease.sh claim <machine-id> <ttl-minutes>}"
    _pull_rebase
    holder="$(_field holder)"
    if _is_fresh && [ "$holder" != "$MACHINE_ID" ]; then
      echo "DENIED: lease held by '$holder' until $(_field expiresUTC) (fresh)."
      echo "  → run lease-free work, or wait for TTL expiry to steal it."
      exit 1
    fi
    _write_lease "$MACHINE_ID" "$TTL" "claim"
    if _commit_push_lease "chore(lab-lease): $MACHINE_ID claim ttl=${TTL}m"; then
      echo "CLAIMED: $MACHINE_ID holds the lab lease until $(_field expiresUTC)."
      _convex_note "Lab lease claimed" "$MACHINE_ID is now the single lab driver (ttl ${TTL}m)."
      exit 0
    fi
    # lost the push race — re-read who won.
    holder="$(_field holder)"
    echo "DENIED: lost the claim race to '$holder' (pushed first). Re-run to retry."
    exit 1
    ;;

  renew)
    MACHINE_ID="${1:?usage: lab_lease.sh renew <machine-id> [<ttl-minutes>]}"
    _pull_rebase
    holder="$(_field holder)"
    if [ "$holder" != "$MACHINE_ID" ]; then
      echo "REFUSED: you ('$MACHINE_ID') are not the holder ('$holder'). Not renewing."
      exit 1
    fi
    TTL="${2:-$(_field ttlMinutes)}"; TTL="${TTL:-30}"
    _write_lease "$MACHINE_ID" "$TTL" "renew"
    if _commit_push_lease "chore(lab-lease): $MACHINE_ID renew ttl=${TTL}m"; then
      echo "RENEWED: $MACHINE_ID lease extended to $(_field expiresUTC)."
      exit 0
    fi
    echo "WARN: renew push lost a race; re-run. Current holder now '$(_field holder)'."
    exit 1
    ;;

  release)
    MACHINE_ID="${1:?usage: lab_lease.sh release <machine-id>}"
    _pull_rebase
    holder="$(_field holder)"
    if [ -n "$holder" ] && [ "$holder" != "$MACHINE_ID" ]; then
      echo "REFUSED: lease held by '$holder', not you ('$MACHINE_ID')."
      exit 1
    fi
    # write a FREE lease (empty holder, expired) so the other machine can claim.
    python3 - "$LEASE_FILE" "$(now_iso)" "$MACHINE_ID" <<'PY'
import sys, json
path, iso, who = sys.argv[1:4]
json.dump({
    "holder": "",
    "claimedUTC": "",
    "expiresUTC": iso,
    "ttlMinutes": 0,
    "lastAction": f"release by {who}",
    "seq": 0,
}, open(path, "w"), indent=2)
open(path, "a").write("\n")
PY
    if _commit_push_lease "chore(lab-lease): $MACHINE_ID release"; then
      echo "RELEASED: lab lease is now FREE — any machine may claim."
      _convex_note "Lab lease released" "$MACHINE_ID released the lab lease; lease is free."
      exit 0
    fi
    echo "WARN: release push lost a race; re-run. Current holder now '$(_field holder)'."
    exit 1
    ;;

  status)
    _pull_rebase
    holder="$(_field holder)"
    if [ -z "$holder" ]; then
      echo "LAB LEASE: FREE (no holder). Any machine may claim."
      exit 4
    fi
    exp="$(_field expiresUTC)"
    if _is_fresh; then
      echo "LAB LEASE: HELD by '$holder' until $exp (FRESH). This machine drives only if it IS '$holder'."
      exit 0
    fi
    echo "LAB LEASE: EXPIRED — last holder '$holder' (expired $exp). Steal with: lab_lease.sh claim <me> <ttl>."
    exit 3
    ;;

  holds)
    # loop gate — quiet; exit 0 iff this machine holds a FRESH lease.
    MACHINE_ID="${1:?usage: lab_lease.sh holds <machine-id>}"
    _pull_rebase
    [ "$(_field holder)" = "$MACHINE_ID" ] && _is_fresh
    exit $?
    ;;

  *)
    echo "usage: lab_lease.sh {claim|renew|release|status|holds} ..." >&2
    exit 2
    ;;
esac
