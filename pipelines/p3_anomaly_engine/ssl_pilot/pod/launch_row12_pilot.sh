#!/bin/bash
# Local-machine launcher for the row12 SSL pilot pod. Provisions a GPU pod,
# waits for SSH, rsyncs the small required subset of the repo + cached
# reference data + the v2 catalogue onto it, installs deps, launches
# pod_row12_pilot.sh under nohup with a background 5h watchdog self-stop
# as the absolute fallback, then exits (the caller polls separately).
set -uo pipefail
cd "$(dirname "$0")/../../../.." || exit 1
REPO_ROOT="$(pwd)"
ENV_FILE="$REPO_ROOT/.env.local"

RUNPOD_API_KEY=$(grep '^RUNPOD_API_KEY=' "$ENV_FILE" | cut -d= -f2-)
HF_TOKEN=$(grep '^HF_TOKEN=' "$ENV_FILE" | cut -d= -f2-)
B2_APPLICATION_KEY_ID=$(grep '^B2_APPLICATION_KEY_ID=' "$ENV_FILE" | cut -d= -f2-)
B2_APPLICATION_KEY=$(grep '^B2_APPLICATION_KEY=' "$ENV_FILE" | cut -d= -f2-)
B2_BUCKET=$(grep '^B2_BUCKET=' "$ENV_FILE" | cut -d= -f2-)

gql() {
  # NOTE (2026-09-04 3rd attempt): "Authorization: Bearer" returns HTTP 403 on
  # the current RunPod API; the working auth is the ?api_key= query param
  # (confirmed live against this account before this run).
  curl -sf -X POST "https://api.runpod.io/graphql?api_key=$RUNPOD_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$1"
}

echo "=== balance before ==="
gql '{"query":"query { myself { clientBalance } }"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['myself']['clientBalance'])"

# NOTE (2026-09-04 3rd attempt): prefer SECURE cloud first -- RunPod docs
# confirm SECURE always gets a public IP automatically, while COMMUNITY needs
# supportPublicIp:true and is less reliable (2 prior COMMUNITY pods this
# session never got SSH). Explicit ports:"22/tcp" added below (previously
# relied on startSsh:true alone, which does not guarantee a mapped port).
GPU_CONFIGS=(
  'NVIDIA GeForce RTX 3090|SECURE'
  'NVIDIA GeForce RTX 4090|SECURE'
  'NVIDIA RTX A5000|SECURE'
)

POD_ID=""
for cfg in "${GPU_CONFIGS[@]}"; do
  GPU_TYPE="${cfg%%|*}"
  CLOUD="${cfg##*|}"
  echo "trying $GPU_TYPE ($CLOUD)..."
  RESP=$(gql "{\"query\": \"mutation { podFindAndDeployOnDemand(input: { name: \\\"bigbounce-row12-pilot\\\", imageName: \\\"runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04\\\", gpuTypeId: \\\"$GPU_TYPE\\\", gpuCount: 1, volumeInGb: 150, containerDiskInGb: 50, startSsh: true, ports: \\\"22/tcp\\\", supportPublicIp: true, cloudType: $CLOUD }) { id } }\"}")
  POD_ID=$(echo "$RESP" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('data',{}).get('podFindAndDeployOnDemand',{}).get('id',''))" 2>/dev/null)
  if [ -n "$POD_ID" ]; then
    echo "created pod $POD_ID ($GPU_TYPE, $CLOUD)"
    break
  fi
  echo "  failed: $RESP"
done

if [ -z "$POD_ID" ]; then
  echo "FATAL: could not provision any GPU pod"
  exit 1
fi

echo "$POD_ID" > /tmp/row12_pod_id.txt

echo "=== waiting for SSH (up to 15 min) ==="
SSH_HOST=""
SSH_PORT=""
for i in $(seq 1 30); do
  sleep 30
  STATUS=$(gql '{"query":"query { myself { pods { id runtime { ports { ip isIpPublic publicPort privatePort } } } } }"}')
  LINE=$(echo "$STATUS" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for p in d['data']['myself']['pods']:
    if p['id'] == '$POD_ID' and p.get('runtime') and p['runtime'].get('ports'):
        for port in p['runtime']['ports']:
            if port['privatePort'] == 22 and port.get('isIpPublic'):
                print(f\"{port['ip']} {port['publicPort']}\")
")
  if [ -n "$LINE" ]; then
    SSH_HOST=$(echo "$LINE" | awk '{print $1}')
    SSH_PORT=$(echo "$LINE" | awk '{print $2}')
    echo "SSH ready: root@$SSH_HOST:$SSH_PORT"
    break
  fi
  echo "  still booting ($((i*30))s)"
done

if [ -z "$SSH_HOST" ]; then
  echo "FATAL: no SSH after 15 min, terminating pod $POD_ID"
  gql "{\"query\": \"mutation { podTerminate(input: {podId: \\\"$POD_ID\\\"}) }\"}"
  exit 1
fi

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p $SSH_PORT"
SSH="ssh $SSH_OPTS root@$SSH_HOST"

echo "=== bootstrap: mkdir + rsync required subset ==="
$SSH "mkdir -p /workspace/bigbounce/pipelines/p3_anomaly_engine/ssl_pilot /workspace/bigbounce/pipelines/p1_highz_tracers/clean_rerun/gates /workspace/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M /workspace/row12/recovery_refs"

rsync -az -e "ssh $SSH_OPTS" \
  "$REPO_ROOT/pipelines/p3_anomaly_engine/ssl_pilot/" \
  "root@$SSH_HOST:/workspace/bigbounce/pipelines/p3_anomaly_engine/ssl_pilot/"

rsync -az -e "ssh $SSH_OPTS" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/clean_rerun/derive_locator_inventory.py" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/clean_rerun/build_calibration.py" \
  "root@$SSH_HOST:/workspace/bigbounce/pipelines/p1_highz_tracers/clean_rerun/"

rsync -az -e "ssh $SSH_OPTS" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/clean_rerun/gates/check_sample_provenance.py" \
  "root@$SSH_HOST:/workspace/bigbounce/pipelines/p1_highz_tracers/clean_rerun/gates/"

rsync -az -e "ssh $SSH_OPTS" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py" \
  "root@$SSH_HOST:/workspace/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M/"

rsync -az -e "ssh $SSH_OPTS" \
  "$REPO_ROOT/pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2.parquet" \
  "root@$SSH_HOST:/workspace/row12/flagship_sample_v2.parquet"

rsync -az -e "ssh $SSH_OPTS" \
  "$HOME/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/" \
  "root@$SSH_HOST:/workspace/row12/recovery_refs/"

echo "=== install deps ==="
$SSH "pip install -q pyarrow astropy huggingface_hub astroquery b2 2>&1 | tail -5"

echo "=== write env + launch ==="
$SSH "cat > /workspace/row12_env.sh <<EOF
export HF_TOKEN='$HF_TOKEN'
export RUNPOD_API_KEY='$RUNPOD_API_KEY'
export RUNPOD_POD_ID='$POD_ID'
export B2_APPLICATION_KEY_ID='$B2_APPLICATION_KEY_ID'
export B2_APPLICATION_KEY='$B2_APPLICATION_KEY'
export B2_BUCKET='$B2_BUCKET'
EOF
chmod +x /workspace/bigbounce/pipelines/p3_anomaly_engine/ssl_pilot/pod/pod_row12_pilot.sh
source /workspace/row12_env.sh
nohup bash -c 'source /workspace/row12_env.sh && bash /workspace/bigbounce/pipelines/p3_anomaly_engine/ssl_pilot/pod/pod_row12_pilot.sh' > /workspace/row12/nohup.out 2>&1 &
disown
nohup bash -c 'source /workspace/row12_env.sh && sleep 18000 && curl -sf -X POST \"https://api.runpod.io/graphql?api_key=\$RUNPOD_API_KEY\" -H \"Content-Type: application/json\" -d \"{\\\"query\\\": \\\"mutation { podStop(input: {podId: \\\\\\\"\$RUNPOD_POD_ID\\\\\\\"}) { id } }\\\"}\"' > /workspace/row12/watchdog.out 2>&1 &
disown
echo LAUNCHED"

echo "POD_ID=$POD_ID"
echo "SSH_HOST=$SSH_HOST"
echo "SSH_PORT=$SSH_PORT"
