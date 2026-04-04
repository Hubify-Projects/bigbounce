#!/bin/bash
# Auto-backup script — runs every 20 minutes via cron
# Backs up all outputs to /workspace/bigbounce/backups/ (persistent storage)

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=/workspace/bigbounce/backups/$TIMESTAMP
OUTPUTS=/workspace/bigbounce/outputs
LOG=/workspace/bigbounce/backup.log

echo "[$TIMESTAMP] Starting backup..." >> $LOG

# 1. Local backup on pod (persistent /workspace survives restarts)
mkdir -p $BACKUP_DIR
cp -r $OUTPUTS/*.log $BACKUP_DIR/ 2>/dev/null
for dir in $OUTPUTS/*/; do
    if [ -d "$dir" ]; then
        dirname=$(basename "$dir")
        mkdir -p $BACKUP_DIR/$dirname
        cp $dir/*.json $BACKUP_DIR/$dirname/ 2>/dev/null
        cp $dir/*.csv $BACKUP_DIR/$dirname/ 2>/dev/null
        cp $dir/*.npz $BACKUP_DIR/$dirname/ 2>/dev/null
        cp $dir/*.parquet $BACKUP_DIR/$dirname/ 2>/dev/null
        cp $dir/*.pt $BACKUP_DIR/$dirname/ 2>/dev/null
    fi
done

# Count what we backed up
N_FILES=$(find $BACKUP_DIR -type f | wc -l)
SIZE=$(du -sh $BACKUP_DIR 2>/dev/null | cut -f1)
echo "[$TIMESTAMP] Backed up $N_FILES files ($SIZE) to $BACKUP_DIR" >> $LOG

# 2. Keep only last 6 backups (2 hours of history) to avoid filling disk
ls -dt /workspace/bigbounce/backups/*/ 2>/dev/null | tail -n +7 | xargs rm -rf 2>/dev/null

# 3. Write latest pod status JSON
python3 << 'PYSTATUS'
import json, os, glob
from datetime import datetime

status = {"timestamp": datetime.utcnow().isoformat(), "experiments": {}}
outputs = "/workspace/bigbounce/outputs"

for d in sorted(glob.glob(os.path.join(outputs, "*/"))):
    name = os.path.basename(d.rstrip("/"))
    summaries = glob.glob(os.path.join(d, "*summary*.json"))
    if summaries:
        try:
            with open(summaries[0]) as f:
                s = json.load(f)
            status["experiments"][name] = {
                "status": s.get("status", "complete"),
                "n_anomalies": s.get("n_anomalies_top1pct", s.get("n_anomalies", "?")),
                "val_loss": s.get("best_val_loss", "?"),
            }
        except Exception:
            status["experiments"][name] = {"status": "json_parse_error"}
    else:
        # Check if log file exists (still running)
        logfile = os.path.join(outputs, name + ".log")
        if os.path.exists(logfile):
            status["experiments"][name] = {"status": "running"}
        else:
            status["experiments"][name] = {"status": "no_summary"}

n_complete = sum(1 for e in status["experiments"].values() if e["status"] in ("complete", "COMPLETE"))
n_running = sum(1 for e in status["experiments"].values() if e["status"] == "running")
status["summary"] = {"complete": n_complete, "running": n_running, "total": len(status["experiments"])}

with open("/workspace/bigbounce/pod_status.json", "w") as f:
    json.dump(status, f, indent=2)

print(f"Status: {n_complete} complete, {n_running} running, {len(status['experiments'])} total")
PYSTATUS

echo "[$TIMESTAMP] Backup complete" >> $LOG
