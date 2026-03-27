#!/bin/bash
# Sync enhanced 18M batches from H200 pod to local + B2
# Run periodically to prevent disk quota overflow on pod
# Usage: ./sync_batches.sh

set -e

REMOTE_HOST="root@205.196.17.44"
REMOTE_PORT=10789
SSH_KEY="$HOME/.ssh/id_ed25519"
REMOTE_DIR="/workspace/desi_dr1/outputs/enhanced_catalog"
LOCAL_DIR="$HOME/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M"
B2_BUCKET="b2://bigbounce/enhanced_18M"

SSH_CMD="ssh -o ConnectTimeout=15 -o StrictHostKeyChecking=no -i $SSH_KEY -p $REMOTE_PORT $REMOTE_HOST"
SCP_CMD="scp -o StrictHostKeyChecking=no -i $SSH_KEY -P $REMOTE_PORT $REMOTE_HOST"

mkdir -p "$LOCAL_DIR"

echo "=== Checking remote batches ==="
REMOTE_FILES=$($SSH_CMD "ls $REMOTE_DIR/*.parquet 2>/dev/null" || true)

if [ -z "$REMOTE_FILES" ]; then
    echo "No parquet files on remote"
    exit 0
fi

# Count remote files
REMOTE_COUNT=$(echo "$REMOTE_FILES" | wc -l | tr -d ' ')
echo "Remote has $REMOTE_COUNT parquet files"

# Download any files we don't have locally
for f in $REMOTE_FILES; do
    BASENAME=$(basename "$f")
    if [ ! -f "$LOCAL_DIR/$BASENAME" ]; then
        echo "Downloading $BASENAME ..."
        scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$REMOTE_PORT" "$REMOTE_HOST:$f" "$LOCAL_DIR/"
        echo "  Downloaded"
    fi
done

# Check disk usage on remote
DISK_USED=$($SSH_CMD "du -sm /workspace/ 2>/dev/null | awk '{print \$1}'" || echo "0")
echo "Remote workspace: ${DISK_USED}MB"

# If above 7GB, delete batches that are safely downloaded locally
if [ "$DISK_USED" -gt 7000 ]; then
    echo "=== Disk above 7GB, cleaning old batches ==="
    for f in $REMOTE_FILES; do
        BASENAME=$(basename "$f")
        if [ -f "$LOCAL_DIR/$BASENAME" ]; then
            # Verify local file size matches
            LOCAL_SIZE=$(stat -f%z "$LOCAL_DIR/$BASENAME" 2>/dev/null || stat -c%s "$LOCAL_DIR/$BASENAME" 2>/dev/null)
            REMOTE_SIZE=$($SSH_CMD "stat -c%s $f 2>/dev/null" || echo "0")
            if [ "$LOCAL_SIZE" = "$REMOTE_SIZE" ] && [ "$LOCAL_SIZE" -gt 0 ]; then
                echo "  Deleting $BASENAME from remote (safely backed up locally: ${LOCAL_SIZE} bytes)"
                $SSH_CMD "rm $f"
            fi
        fi
    done
    NEW_DISK=$($SSH_CMD "du -sm /workspace/ 2>/dev/null | awk '{print \$1}'" || echo "0")
    echo "Remote workspace after cleanup: ${NEW_DISK}MB"
fi

# Show progress
echo ""
echo "=== Progress ==="
$SSH_CMD 'python3 -c "
import json
with open(\"/workspace/desi_dr1/outputs/enhanced_catalog/checkpoint.json\") as f:
    ckpt = json.load(f)
px = len(ckpt[\"processed_pixels\"])
print(f\"Pixels: {px} / 27488 ({px/27488*100:.1f}%)\")
print(f\"Rows written: {ckpt[\"total_rows_written\"]:,}\")
print(f\"Batch: {ckpt[\"batch_idx\"]}\")
print(f\"Spectra: {ckpt.get(\"total_spectra\", 0):,}\")
"' 2>/dev/null

LOCAL_COUNT=$(ls "$LOCAL_DIR"/*.parquet 2>/dev/null | wc -l | tr -d ' ')
echo "Local parquet files: $LOCAL_COUNT"

echo ""
echo "=== Done ==="
