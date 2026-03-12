#!/bin/bash
# Paper-1 Off-Pod Sync — runs on LOCAL machine
# Syncs chain data from RunPod pod to local backup every 30 minutes
#
# Usage: bash paper1_offpod_sync.sh
# Or add to crontab: */30 * * * * /path/to/paper1_offpod_sync.sh

set -euo pipefail

POD_HOST="157.157.221.30"
POD_PORT="36579"
SSH_KEY="$HOME/.ssh/id_ed25519"
SSH_OPTS="-o StrictHostKeyChecking=no -o ConnectTimeout=15"

LOCAL_SYNC="/Users/houstongolden/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/paper1_clean_restart_sync"
TIMESTAMP=$(date -u +%Y-%m-%d_%H%M)
LOGFILE="/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/global_monitor/sync_log.txt"

mkdir -p "$LOCAL_SYNC"/{chains,covmats,manifests,snapshots}

echo "[$TIMESTAMP] Starting off-pod sync" >> "$LOGFILE"

# Test SSH connectivity
if ! ssh $SSH_OPTS -i "$SSH_KEY" -p "$POD_PORT" "root@$POD_HOST" 'echo ok' > /dev/null 2>&1; then
    echo "[$TIMESTAMP] ALERT: Pod unreachable!" >> "$LOGFILE"
    echo "ALERT: BigBounce pod unreachable at $TIMESTAMP" > "$LOCAL_SYNC/ALERT_POD_UNREACHABLE.txt"
    exit 1
fi

# Remove any stale alert
rm -f "$LOCAL_SYNC/ALERT_POD_UNREACHABLE.txt"

# Rsync chain files
rsync -avz --progress \
    -e "ssh $SSH_OPTS -i $SSH_KEY -p $POD_PORT" \
    "root@$POD_HOST:/workspace/bigbounce/chains/" \
    "$LOCAL_SYNC/chains/" >> "$LOGFILE" 2>&1

# Rsync covmats
rsync -avz \
    -e "ssh $SSH_OPTS -i $SSH_KEY -p $POD_PORT" \
    "root@$POD_HOST:/workspace/bigbounce/covmats/" \
    "$LOCAL_SYNC/covmats/" >> "$LOGFILE" 2>&1

# Rsync manifests
rsync -avz \
    -e "ssh $SSH_OPTS -i $SSH_KEY -p $POD_PORT" \
    "root@$POD_HOST:/workspace/bigbounce/manifests/" \
    "$LOCAL_SYNC/manifests/" >> "$LOGFILE" 2>&1

# Generate local SHA256SUMS
find "$LOCAL_SYNC/chains" -name "spin_torsion.1.txt" -exec shasum -a 256 {} \; > "$LOCAL_SYNC/SHA256SUMS_${TIMESTAMP}.txt" 2>/dev/null || true

echo "[$TIMESTAMP] Off-pod sync complete" >> "$LOGFILE"
