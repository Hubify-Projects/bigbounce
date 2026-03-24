#!/bin/bash
# Automated backup from RunPod H100 pod to local machine
# Run: bash pipelines/backup_runpod.sh
# Or schedule with cron: */30 * * * * cd /Users/houstongolden/Desktop/CODE_2026/bigbounce && bash pipelines/backup_runpod.sh >> data/runpod_backups/backup.log 2>&1

set -e

POD_HOST="root@64.247.201.47"
POD_PORT="10778"
SSH_KEY="$HOME/.ssh/id_ed25519"
SSH_OPTS="-o ConnectTimeout=15 -o StrictHostKeyChecking=no"
LOCAL_BACKUP="$(dirname "$0")/../data/runpod_backups"

echo "=== RunPod Backup $(date) ==="

# Create backup dirs
mkdir -p "$LOCAL_BACKUP"/{analysis1,analysis3,analysis3/matched_chunks,analysis4,models,logs}

# Test connection
if ! ssh $SSH_OPTS -p $POD_PORT -i $SSH_KEY $POD_HOST "echo connected" 2>/dev/null; then
    echo "ERROR: Cannot connect to pod. Pod may be stopped/deleted."
    exit 1
fi

echo "Connected. Starting backup..."

# Backup Analysis 1 (bispectrum)
echo "  Syncing Analysis 1..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis1_outputs/*.json \
    "$LOCAL_BACKUP/analysis1/" 2>/dev/null || true

# Backup Analysis 3 (chirality) — the big one
echo "  Syncing Analysis 3 metadata..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis3_outputs/crossmatch_metadata.csv \
    $POD_HOST:/workspace/analysis3_outputs/summary.json \
    $POD_HOST:/workspace/analysis3_outputs/audit_results.json \
    "$LOCAL_BACKUP/analysis3/" 2>/dev/null || true

# Backup matched image chunks (training data)
echo "  Syncing matched image chunks..."
scp $SSH_OPTS -r -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis3_outputs/matched_chunks/ \
    "$LOCAL_BACKUP/analysis3/matched_chunks/" 2>/dev/null || true

# Backup trained models
echo "  Syncing models..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis3_outputs/chirality_model_best.pt \
    $POD_HOST:/workspace/analysis3_outputs/chirality_head_best.pt \
    "$LOCAL_BACKUP/models/" 2>/dev/null || true

# Backup catalogs (can be large)
echo "  Syncing catalogs..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis3_outputs/chirality_catalog_full.parquet \
    "$LOCAL_BACKUP/analysis3/" 2>/dev/null || true

# Backup any checkpoint parquets
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis3_outputs/chirality_catalog_checkpoint_*.parquet \
    "$LOCAL_BACKUP/analysis3/" 2>/dev/null || true

# Backup Analysis 4 (EB spectra)
echo "  Syncing Analysis 4..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/analysis4_outputs/*.json \
    $POD_HOST:/workspace/analysis4_outputs/*.npz \
    "$LOCAL_BACKUP/analysis4/" 2>/dev/null || true

# Backup logs
echo "  Syncing logs..."
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/chirality_v*.log \
    "$LOCAL_BACKUP/logs/" 2>/dev/null || true

# Backup scripts
scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
    $POD_HOST:/workspace/real_*.py \
    "$LOCAL_BACKUP/" 2>/dev/null || true

echo "  Local backup: $(du -sh "$LOCAL_BACKUP" | cut -f1)"

# Also sync to Backblaze B2 (if rclone configured)
if command -v rclone &> /dev/null && rclone ls b2:bigbounce &> /dev/null; then
    echo "  Syncing to Backblaze B2..."
    # Sync models
    scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
        $POD_HOST:/workspace/analysis3_outputs/chirality_model_v2_best.pt \
        /tmp/chirality_model_v2_best.pt 2>/dev/null && \
        rclone copy /tmp/chirality_model_v2_best.pt b2:bigbounce/models/ 2>/dev/null && \
        rm -f /tmp/chirality_model_v2_best.pt
    # Sync results
    for f in v2_fast_results.json bias_hardening_results.json audit_results.json v2_inference_summary.json; do
        scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY \
            $POD_HOST:/workspace/analysis3_outputs/$f /tmp/$f 2>/dev/null && \
            rclone copy /tmp/$f b2:bigbounce/results/ 2>/dev/null && rm -f /tmp/$f
    done
    # Sync checkpoints
    for f in $(ssh $SSH_OPTS -p $POD_PORT -i $SSH_KEY $POD_HOST "ls /workspace/analysis3_outputs/v2_ckpt_*.parquet 2>/dev/null" 2>/dev/null); do
        fname=$(basename $f)
        if ! rclone ls b2:bigbounce/checkpoints/$fname &>/dev/null; then
            scp $SSH_OPTS -P $POD_PORT -i $SSH_KEY $POD_HOST:$f /tmp/$fname 2>/dev/null && \
                rclone copy /tmp/$fname b2:bigbounce/checkpoints/ 2>/dev/null && rm -f /tmp/$fname
            echo "    Uploaded checkpoint: $fname"
        fi
    done
    echo "  B2 sync complete"
else
    echo "  Backblaze B2 not configured (install rclone + configure b2 remote)"
fi

echo "=== Done $(date) ==="
