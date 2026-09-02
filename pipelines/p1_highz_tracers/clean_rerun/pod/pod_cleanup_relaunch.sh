#!/bin/bash
# Stop ALL supervisors/workers/backup loops, reconcile shard/receipt/checkpoint integrity
# fail-closed, rebuild per-worker checkpoints from verified receipts, relaunch singletons under flock.
# (Full reconcile python is documented in SSOT/queue.md 2026-08-05 incident; re-derive from
#  clean_rerun_contract.py receipt schema: verify sha256/byte_size/row_count/schema per shard,
#  delete bad/orphan pairs, rebuild checkpoint_w*.json from surviving receipts by inventory index.)
set -uo pipefail
pgrep -f "bash /workspace/pod_babysitter" | xargs -r kill 2>/dev/null
pgrep -f "pod_backup_loop.sh" | xargs -r kill 2>/dev/null
sleep 2; pgrep -f "run_scan.py" | xargs -r kill 2>/dev/null; sleep 8; pgrep -f "run_scan.py" | xargs -r kill -9 2>/dev/null
echo "all stopped — run the reconcile step, then:"
echo "setsid nohup flock -n /workspace/babysitter4.lock /workspace/pod_babysitter_v4.sh > /workspace/babysitter4_stdout.log 2>&1 < /dev/null &"
echo "setsid nohup flock -n /workspace/backup.lock env HF_TOKEN=... B2_APPLICATION_KEY_ID=... B2_APPLICATION_KEY=... B2_BUCKET=... /workspace/pod_backup_loop.sh > /workspace/backup_loop_stdout.log 2>&1 < /dev/null &"
