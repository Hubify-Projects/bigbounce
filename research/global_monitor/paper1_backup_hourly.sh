#!/bin/bash
# Paper-1 — Hourly On-Volume Backup
# Creates timestamped tarballs of all chain data.
# Run from cron: 0 * * * * /workspace/bigbounce/research/global_monitor/paper1_backup_hourly.sh
set -euo pipefail

CANONICAL="/workspace/bigbounce/reproducibility/cosmology/canonical_run_001"
BACKUP_DIR="/workspace/backups/hourly"
MANIFEST_DIR="/workspace/backups/manifests"
LOG="/workspace/logs/backup/hourly_$(date -u +%Y%m%d).log"
TIMESTAMP=$(date -u +%Y-%m-%d_%H%M)

mkdir -p "$BACKUP_DIR" "$MANIFEST_DIR" "$(dirname "$LOG")"

echo "[$TIMESTAMP] Starting hourly backup" >> "$LOG"

# Create tarball of chain data files + covmats
TARBALL="$BACKUP_DIR/chains_${TIMESTAMP}.tar.gz"
cd "$CANONICAL"

find . -name "*.txt" -o -name "*.covmat" -o -name "*.yaml" -o -name "*.json" | \
    tar czf "$TARBALL" -T - 2>>"$LOG"

TARBALL_SIZE=$(du -h "$TARBALL" | cut -f1)
echo "[$TIMESTAMP] Backup created: $TARBALL ($TARBALL_SIZE)" >> "$LOG"

# Generate SHA256SUMS
SHA_FILE="$MANIFEST_DIR/SHA256SUMS_${TIMESTAMP}.txt"
find . -name "*.1.txt" -exec sha256sum {} \; > "$SHA_FILE" 2>>"$LOG"
echo "[$TIMESTAMP] SHA256SUMS: $SHA_FILE" >> "$LOG"

# Generate sample count manifest
MANIFEST="$MANIFEST_DIR/manifest_${TIMESTAMP}.json"
python3 -c "
import os, json, glob
from datetime import datetime, timezone

canonical = '$CANONICAL'
counts = {}
for model in ['dneff', 'lcdm']:
    counts[model] = {}
    for ds in ['full_tension', 'planck_only', 'planck_bao', 'planck_bao_sn']:
        counts[model][ds] = {}
        total = 0
        for c in range(1, 5):
            chain_dir = f'{canonical}/{model}/{ds}/chain_{c:02d}'
            prefix = 'spin_torsion' if model == 'dneff' else 'lcdm'
            chain_file = f'{chain_dir}/{prefix}.1.txt'
            n = 0
            if os.path.exists(chain_file):
                with open(chain_file) as f:
                    n = sum(1 for line in f if not line.startswith('#'))
            counts[model][ds][f'chain_{c:02d}'] = n
            total += n
        counts[model][ds]['total'] = total

manifest = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'run_id': 'canonical_run_001',
    'sample_counts': counts,
    'backup_file': '$TARBALL',
}
with open('$MANIFEST', 'w') as f:
    json.dump(manifest, f, indent=2)
print(json.dumps(counts, indent=2))
" >> "$LOG" 2>&1

echo "[$TIMESTAMP] Manifest: $MANIFEST" >> "$LOG"

# Prune old backups (keep last 48 hours = 48 files)
cd "$BACKUP_DIR"
ls -1t chains_*.tar.gz 2>/dev/null | tail -n +49 | xargs rm -f 2>/dev/null || true
echo "[$TIMESTAMP] Pruned old backups" >> "$LOG"

# Check for chain stalls (no writes in >2 hours)
python3 -c "
import os, time, glob

canonical = '$CANONICAL'
stale_threshold = 7200  # 2 hours
now = time.time()
stale = []

for chain_file in glob.glob(f'{canonical}/*/*/chain_*/spin_torsion.1.txt') + \
                   glob.glob(f'{canonical}/*/*/chain_*/lcdm.1.txt'):
    mtime = os.path.getmtime(chain_file)
    age = now - mtime
    if age > stale_threshold:
        stale.append((chain_file, int(age/3600)))

if stale:
    alert_file = '/workspace/logs/backup/ALERT_STALE_CHAINS.txt'
    with open(alert_file, 'w') as f:
        f.write(f'ALERT: {len(stale)} chains stale (no writes >2h)\n')
        for path, hours in stale:
            f.write(f'  {path}: {hours}h since last write\n')
    print(f'WARNING: {len(stale)} stale chains')
else:
    # Clear any previous alert
    alert_file = '/workspace/logs/backup/ALERT_STALE_CHAINS.txt'
    if os.path.exists(alert_file):
        os.remove(alert_file)
" 2>>"$LOG"

echo "[$TIMESTAMP] Hourly backup complete" >> "$LOG"
