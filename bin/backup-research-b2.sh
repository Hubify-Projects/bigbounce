#!/usr/bin/env bash
# backup-research-b2.sh — offsite backup of bigbounce HEAVY research data to
# Backblaze B2 (S3-compatible). The 3rd location: local + GitHub + B2.
# Incremental: aws s3 sync only uploads new/changed files.
#
# Creds come from bigbounce/.env.local (values never printed):
#   B2_APPLICATION_KEY_ID, B2_APPLICATION_KEY, B2_BUCKET, B2_ENDPOINT
# Requires the AWS CLI (already installed). Run: bash bin/backup-research-b2.sh
set -uo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
set -a; . ./.env.local 2>/dev/null; set +a
: "${B2_APPLICATION_KEY_ID:?set in .env.local}"
: "${B2_APPLICATION_KEY:?set in .env.local}"
: "${B2_BUCKET:?set in .env.local}"
: "${B2_ENDPOINT:?set in .env.local}"

command -v aws >/dev/null 2>&1 || { echo "aws CLI missing"; exit 1; }
export AWS_ACCESS_KEY_ID="$B2_APPLICATION_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$B2_APPLICATION_KEY"
EP="https://$B2_ENDPOINT"
LOG="$REPO/project-context/ops/b2-backup.log"; mkdir -p "$(dirname "$LOG")"
ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
log() { echo "[$(ts)] $*" | tee -a "$LOG"; }

# Heavy research dirs to protect offsite. data/ first (the 12GB local-only gap).
DIRS="${B2_BACKUP_DIRS:-data pipelines reproducibility research arxiv}"

log "=== B2 research sync START → s3://$B2_BUCKET ($B2_ENDPOINT) ==="
rc=0
for d in $DIRS; do
  [ -d "$REPO/$d" ] || { log "skip $d (absent)"; continue; }
  log "syncing $d/ ..."
  aws s3 sync "$REPO/$d" "s3://$B2_BUCKET/$d" --endpoint-url "$EP" \
    --exclude '.git/*' --exclude '*/.git/*' --exclude '*/node_modules/*' \
    --exclude '*/__pycache__/*' --exclude '.DS_Store' --only-show-errors >>"$LOG" 2>&1 \
    || { log "WARN: sync $d failed (rc=$?)"; rc=1; }
  log "  done $d/"
done
log "=== B2 research sync DONE (rc=$rc) ==="
exit $rc
