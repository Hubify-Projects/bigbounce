#!/usr/bin/env bash
# Isolated regression test: all pushes target a temporary local bare remote.
set -euo pipefail

SOURCE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/lab-lease-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT HUP INT TERM

git init --bare -q "$TMP/remote.git"
git init -q -b main "$TMP/seed"
git -C "$TMP/seed" config user.name test
git -C "$TMP/seed" config user.email test@example.invalid
mkdir -p "$TMP/seed/tools" "$TMP/seed/ops/handoff" "$TMP/seed/project-context/cron-logs"
cp "$SOURCE_ROOT/tools/lab_lease.sh" "$TMP/seed/tools/lab_lease.sh"
cp "$SOURCE_ROOT/tools/bigbounce_cron_tick.sh" "$TMP/seed/tools/bigbounce_cron_tick.sh"
chmod +x "$TMP/seed/tools/lab_lease.sh" "$TMP/seed/tools/bigbounce_cron_tick.sh"
printf '%s\n' '{' '  "holder": "",' '  "claimedUTC": "",' \
  '  "expiresUTC": "2020-01-01T00:00:00Z",' '  "ttlMinutes": 0,' \
  '  "lastAction": "test seed",' '  "seq": 0' '}' > "$TMP/seed/ops/handoff/LEASE.json"
printf 'seed\n' > "$TMP/seed/README.md"
git -C "$TMP/seed" add .
git -C "$TMP/seed" commit -qm seed
git -C "$TMP/seed" remote add origin "$TMP/remote.git"
git -C "$TMP/seed" push -qu origin main
git --git-dir="$TMP/remote.git" symbolic-ref HEAD refs/heads/main

git clone -q "$TMP/remote.git" "$TMP/a"
git clone -q "$TMP/remote.git" "$TMP/b"
for repo in a b; do
  git -C "$TMP/$repo" config user.name test
  git -C "$TMP/$repo" config user.email test@example.invalid
done

# Dirty + staged user state must survive every lease operation byte-for-byte.
printf 'dirty\n' >> "$TMP/a/README.md"
printf 'staged\n' > "$TMP/a/staged.txt"
git -C "$TMP/a" add staged.txt
STATUS_BEFORE="$(git -C "$TMP/a" status --porcelain=v1 -uall)"
INDEX_BEFORE="$(git -C "$TMP/a" write-tree)"
HEAD_BEFORE="$(git -C "$TMP/a" rev-parse HEAD)"

export BIGBOUNCE_LEASE_CONVEX_NOTE=0
set +e
"$TMP/a/tools/lab_lease.sh" status >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 4 ]

"$TMP/a/tools/lab_lease.sh" claim machine-a 15 >/dev/null
"$TMP/a/tools/lab_lease.sh" holds machine-a
! "$TMP/b/tools/lab_lease.sh" holds machine-b
! "$TMP/b/tools/lab_lease.sh" claim machine-b 15 >/dev/null 2>&1
"$TMP/a/tools/lab_lease.sh" renew machine-a 20 >/dev/null
! "$TMP/a/tools/lab_lease.sh" claim 'bad id' 15 >/dev/null 2>&1
! "$TMP/a/tools/lab_lease.sh" renew machine-a 999 >/dev/null 2>&1
"$TMP/a/tools/lab_lease.sh" release machine-a >/dev/null

# Concurrent contenders: exactly one isolated CAS wins.
set +e
"$TMP/a/tools/lab_lease.sh" claim machine-a 15 >"$TMP/a.out" 2>&1 & pa=$!
"$TMP/b/tools/lab_lease.sh" claim machine-b 15 >"$TMP/b.out" 2>&1 & pb=$!
wait "$pa"; ra=$?
wait "$pb"; rb=$?
set -e
[ $(( (ra == 0) + (rb == 0) )) -eq 1 ]

[ "$(git -C "$TMP/a" status --porcelain=v1 -uall)" = "$STATUS_BEFORE" ]
[ "$(git -C "$TMP/a" write-tree)" = "$INDEX_BEFORE" ]
[ "$(git -C "$TMP/a" rev-parse HEAD)" = "$HEAD_BEFORE" ]

# Durable cron routing: a non-holder is lease-free; the remote holder is driver.
cron_common=(env BIGBOUNCE_CRON_DRY_RUN=1 BIGBOUNCE_REPO="$TMP/a"
  BIGBOUNCE_LOGDIR="$TMP/cron-logs" BIGBOUNCE_RUNTIME_DIR="$TMP/runtime"
  BIGBOUNCE_CRON_LOCK="$TMP/cron.lock" BIGBOUNCE_LEASE_CONVEX_NOTE=0)
lease_free_out="$("${cron_common[@]}" BIGBOUNCE_MACHINE_ID=cron-outsider "$TMP/a/tools/bigbounce_cron_tick.sh")"
[[ "$lease_free_out" == *"role=lease-free"* ]]
winner="$(git --git-dir="$TMP/remote.git" show main:ops/handoff/LEASE.json | python3 -c 'import json,sys; print(json.load(sys.stdin)["holder"])')"
driver_out="$("${cron_common[@]}" BIGBOUNCE_MACHINE_ID="$winner" "$TMP/a/tools/bigbounce_cron_tick.sh")"
[[ "$driver_out" == *"role=driver"* ]]
python3 - "$TMP/runtime/LOOP_HEARTBEAT.json" "$winner" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
assert d["machineId"] == sys.argv[2]
assert d["role"] == "driver"
PY

# Remote uncertainty fails closed.
git -C "$TMP/a" remote set-url origin "$TMP/missing.git"
set +e
"$TMP/a/tools/lab_lease.sh" holds machine-a >/dev/null 2>&1
rc=$?
set -e
[ "$rc" -eq 5 ]

echo "PASS: isolated lease CAS, cron role routing, validation, fail-closed behavior, and worktree/index invariance"
