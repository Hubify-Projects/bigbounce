#!/usr/bin/env bash
# One-command launcher for the C1/C2/C3 NaMaster compute jobs.
# Blocked 2026-06-09 on RunPod INSUFFICIENT_BALANCE (account at $0.00);
# rerun this script as soon as funds are added.
#
# Usage:  bash h200_scripts/experiments/launch_c123_pod.sh
# Needs:  RUNPOD_API_KEY + HF_TOKEN in bigbounce/.env.local
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
EXP="$REPO/h200_scripts/experiments"
source <(grep -E "^(RUNPOD_API_KEY|HF_TOKEN)=" "$REPO/.env.local" | sed 's/^/export /')

GQL() {
  curl -s -X POST https://api.runpod.io/graphql \
    -H "Authorization: Bearer $RUNPOD_API_KEY" \
    -H "Content-Type: application/json" -d "$1"
}

echo "[1/6] Creating cheap pod (CPU-bound NaMaster MC; try A5000-class first)..."
POD_ID=""
for GPU in "NVIDIA RTX A5000" "NVIDIA RTX A4000" "NVIDIA GeForce RTX 3090" "NVIDIA RTX 2000 Ada Generation"; do
  for CLOUD in COMMUNITY SECURE; do
    RESP=$(GQL "{\"query\":\"mutation { podFindAndDeployOnDemand(input: {cloudType: $CLOUD, gpuCount: 1, gpuTypeId: \\\"$GPU\\\", name: \\\"bigbounce-c123-namaster\\\", imageName: \\\"runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04\\\", containerDiskInGb: 60, volumeInGb: 60, volumeMountPath: \\\"/workspace\\\", ports: \\\"22/tcp\\\", startSsh: true}) { id costPerHr } }\"}")
    POD_ID=$(echo "$RESP" | python3 -c "import sys,json;d=json.load(sys.stdin);p=(d.get('data') or {}).get('podFindAndDeployOnDemand');print(p['id'] if p else '')")
    if [ -n "$POD_ID" ]; then
      COST=$(echo "$RESP" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['podFindAndDeployOnDemand']['costPerHr'])")
      echo "  -> pod $POD_ID ($GPU, $CLOUD, \$$COST/hr)"
      break 2
    else
      echo "  $GPU/$CLOUD: $(echo "$RESP" | head -c 160)"
    fi
  done
done
[ -n "$POD_ID" ] || { echo "FATAL: no pod could be created"; exit 1; }

echo "[2/6] Waiting for SSH..."
SSH_HOST=""; SSH_PORT=""
for i in $(seq 1 60); do
  RT=$(GQL "{\"query\":\"query { pod(input: {podId: \\\"$POD_ID\\\"}) { runtime { ports { ip isIpPublic privatePort publicPort } } } }\"}")
  read -r SSH_HOST SSH_PORT < <(echo "$RT" | python3 -c "
import sys,json
d=json.load(sys.stdin)
rt=(d.get('data') or {}).get('pod',{}) or {}
for p in ((rt.get('runtime') or {}).get('ports') or []):
    if p['isIpPublic'] and p['privatePort']==22:
        print(p['ip'], p['publicPort']); break
else: print('', '')")
  [ -n "$SSH_HOST" ] && break
  sleep 10
done
[ -n "$SSH_HOST" ] || { echo "FATAL: SSH never came up for $POD_ID"; exit 1; }
echo "  -> ssh root@$SSH_HOST -p $SSH_PORT"
SSH="ssh -o StrictHostKeyChecking=no -o ConnectTimeout=15 -p $SSH_PORT root@$SSH_HOST"
until $SSH true 2>/dev/null; do sleep 5; done

echo "[3/6] Env setup (gsl/fftw/cfitsio + pymaster)..."
$SSH "apt-get update -qq && apt-get install -y -qq libgsl-dev libfftw3-dev libcfitsio-dev tmux rsync > /dev/null && pip install -q pymaster healpy astropy pandas pyarrow datasets huggingface_hub && python3 -c 'import pymaster; print(\"pymaster\", pymaster.__version__, \"OK\")'"

echo "[4/6] Copying scripts..."
scp -o StrictHostKeyChecking=no -P "$SSH_PORT" \
  "$EXP/c2_p4_nall_binomial_null.py" \
  "$EXP/c3_p4_wp_invariance_fsky.py" \
  "$EXP/c1_p1b_namaster_fsky_sweep.py" \
  root@"$SSH_HOST":/workspace/
$SSH "echo 'export HF_TOKEN=$HF_TOKEN' >> /root/.bashrc"

echo "[5/6] Launching tmux jobs (C2+C3 first — shared HF catalog; C1 parallel)..."
$SSH "cd /workspace && export HF_TOKEN=$HF_TOKEN && \
  tmux new -s c2 -d 'HF_TOKEN=$HF_TOKEN python3 c2_p4_nall_binomial_null.py 2>&1 | tee c2.log' && \
  sleep 90 && \
  tmux new -s c3 -d 'HF_TOKEN=$HF_TOKEN python3 c3_p4_wp_invariance_fsky.py 2>&1 | tee c3.log' && \
  tmux new -s c1 -d 'python3 c1_p1b_namaster_fsky_sweep.py 2>&1 | tee c1.log'"

echo "[6/6] Verifying (tmux capture-pane)..."
sleep 60
for s in c2 c3 c1; do
  echo "--- $s ---"
  $SSH "tmux capture-pane -t $s -p | tail -8"
done

echo
echo "DONE. Pod: $POD_ID  ssh root@$SSH_HOST -p $SSH_PORT"
echo "Update project-context/SSOT/compute-queue.md with these coords."
