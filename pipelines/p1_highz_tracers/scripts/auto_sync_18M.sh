#!/bin/bash
# Auto-sync enhanced 18M batches from H200 pod
# Runs in a loop every 2 hours, downloads new batches, cleans up if disk >7GB
# Usage: nohup ./auto_sync_18M.sh > auto_sync.log 2>&1 &

REMOTE_HOST="root@205.196.17.44"
REMOTE_PORT=10789
SSH_KEY="$HOME/.ssh/id_ed25519"
REMOTE_DIR="/workspace/desi_dr1/outputs/enhanced_catalog"
LOCAL_DIR="$HOME/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M"
INTERVAL=7200  # 2 hours

SSH="ssh -o ConnectTimeout=15 -o StrictHostKeyChecking=no -i $SSH_KEY -p $REMOTE_PORT $REMOTE_HOST"

mkdir -p "$LOCAL_DIR"

echo "$(date): Auto-sync started. Interval: ${INTERVAL}s"

while true; do
    echo ""
    echo "============================================="
    echo "$(date): Sync cycle"
    echo "============================================="

    # 1. Check if pod is reachable
    if ! $SSH "echo ok" > /dev/null 2>&1; then
        echo "$(date): Pod unreachable, waiting..."
        sleep $INTERVAL
        continue
    fi

    # 2. Check progress
    PROGRESS=$($SSH 'python3 -c "
import json
with open(\"/workspace/desi_dr1/outputs/enhanced_catalog/checkpoint.json\") as f:
    ckpt = json.load(f)
px = len(ckpt[\"processed_pixels\"])
print(f\"Pixels: {px}/27488 ({px/27488*100:.1f}%) | Rows: {ckpt[\"total_rows_written\"]:,} | Batch: {ckpt[\"batch_idx\"]}\")
if px >= 27488:
    print(\"COMPLETE\")
"' 2>/dev/null)
    echo "$PROGRESS"

    # 3. Check if complete
    if echo "$PROGRESS" | grep -q "COMPLETE"; then
        echo "$(date): RUN COMPLETE! Downloading final files..."
        # Download everything remaining
        for f in $($SSH "ls $REMOTE_DIR/*.parquet 2>/dev/null"); do
            BASENAME=$(basename "$f")
            if [ ! -f "$LOCAL_DIR/$BASENAME" ]; then
                echo "  Downloading $BASENAME"
                scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$REMOTE_PORT" "$REMOTE_HOST:$f" "$LOCAL_DIR/"
            fi
        done
        # Download final checkpoint
        scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$REMOTE_PORT" "$REMOTE_HOST:$REMOTE_DIR/checkpoint.json" "$LOCAL_DIR/"
        echo "$(date): ALL DONE! All batches downloaded."
        break
    fi

    # 4. Download new batches
    REMOTE_FILES=$($SSH "ls $REMOTE_DIR/*.parquet 2>/dev/null" || true)
    NEW=0
    for f in $REMOTE_FILES; do
        BASENAME=$(basename "$f")
        if [ ! -f "$LOCAL_DIR/$BASENAME" ]; then
            echo "  Downloading $BASENAME"
            scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$REMOTE_PORT" "$REMOTE_HOST:$f" "$LOCAL_DIR/"
            NEW=$((NEW + 1))
        fi
    done
    echo "  Downloaded $NEW new files"

    # 5. Check remote disk and clean if needed
    DISK_MB=$($SSH "du -sm /workspace/ 2>/dev/null | awk '{print \$1}'" || echo "0")
    echo "  Remote disk: ${DISK_MB}MB"

    if [ "$DISK_MB" -gt 7000 ]; then
        echo "  Disk above 7GB, cleaning backed-up batches..."
        CLEANED=0
        for f in $REMOTE_FILES; do
            BASENAME=$(basename "$f")
            if [ -f "$LOCAL_DIR/$BASENAME" ]; then
                LOCAL_SIZE=$(stat -f%z "$LOCAL_DIR/$BASENAME" 2>/dev/null || stat -c%s "$LOCAL_DIR/$BASENAME" 2>/dev/null || echo "0")
                REMOTE_SIZE=$($SSH "stat -c%s $f 2>/dev/null" || echo "0")
                if [ "$LOCAL_SIZE" = "$REMOTE_SIZE" ] && [ "$LOCAL_SIZE" -gt 0 ]; then
                    echo "    Removing $BASENAME from pod (${LOCAL_SIZE} bytes verified)"
                    $SSH "rm $f"
                    CLEANED=$((CLEANED + 1))
                fi
            fi
        done
        echo "  Cleaned $CLEANED files"
        NEW_DISK=$($SSH "du -sm /workspace/ 2>/dev/null | awk '{print \$1}'" || echo "?")
        echo "  Disk after cleanup: ${NEW_DISK}MB"
    fi

    # 6. Also download updated checkpoint
    scp -o StrictHostKeyChecking=no -i "$SSH_KEY" -P "$REMOTE_PORT" "$REMOTE_HOST:$REMOTE_DIR/checkpoint.json" "$LOCAL_DIR/" 2>/dev/null

    echo "$(date): Next sync in ${INTERVAL}s"
    sleep $INTERVAL
done
