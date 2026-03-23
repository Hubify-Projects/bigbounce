#!/usr/bin/env python3
"""
RunPod Pod Launcher — tries to resume existing pods or create new ones.
Run this script periodically until pods become available.

Usage: python3 pipelines/launch_runpod.py
"""
import os
import json
import time
import subprocess

# Load API key
env_file = os.path.join(os.path.dirname(__file__), '..', '.env.local')
api_key = None
if os.path.exists(env_file):
    for line in open(env_file):
        if line.startswith('RUNPOD_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

if not api_key:
    print("ERROR: No RUNPOD_API_KEY found in .env.local")
    exit(1)

def graphql(query):
    """Execute a RunPod GraphQL query."""
    import urllib.request
    req = urllib.request.Request(
        'https://api.runpod.io/graphql',
        data=json.dumps({'query': query}).encode(),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

# Existing pods to try resuming
EXISTING_PODS = [
    ('uktt3hghbs1djo', 'paper2-p6-eb', 'RTX A5000', 1),      # GPU pod
    ('mz3srzbzxxv1yj', 'paper2-wp5-spin', 'RTX A5000', 1),    # GPU pod
    ('83ubwlcdk0gat2', 'bigbounce-paper1-cpu5', 'CPU', 0),     # CPU pod
]

# New pod configs to try if existing can't resume
NEW_POD_CONFIGS = [
    ('NVIDIA GeForce RTX 3090', 'COMMUNITY'),
    ('NVIDIA GeForce RTX 4090', 'COMMUNITY'),
    ('NVIDIA RTX A5000', 'SECURE'),
    ('NVIDIA RTX A4000', 'SECURE'),
    ('NVIDIA RTX 6000 Ada Generation', 'SECURE'),
]

print("="*60)
print("RunPod Pod Launcher for BigBounce Phase 2 Pipelines")
print("="*60)

# Try resuming existing pods
print("\n--- Attempting to resume existing pods ---")
resumed = []
for pod_id, name, gpu_type, gpu_count in EXISTING_PODS:
    print(f"  Trying {name} ({pod_id}, {gpu_type})...", end=" ")
    try:
        result = graphql(f'mutation {{ podResume(input: {{podId: "{pod_id}", gpuCount: {gpu_count}}}) {{ id desiredStatus }} }}')
        if result.get('data', {}).get('podResume'):
            print(f"RESUMED!")
            resumed.append((pod_id, name))
        else:
            err = result.get('errors', [{}])[0].get('message', 'Unknown error')
            print(f"FAILED: {err}")
    except Exception as e:
        print(f"ERROR: {e}")

if resumed:
    print(f"\n✓ {len(resumed)} pod(s) resumed! Waiting for SSH...")
    time.sleep(30)

    # Get SSH details
    result = graphql('query { myself { pods { id name desiredStatus runtime { ports { ip isIpPublic publicPort privatePort } } } } }')
    for pod in result['data']['myself']['pods']:
        if pod['desiredStatus'] == 'RUNNING' and pod.get('runtime') and pod['runtime'].get('ports'):
            for p in pod['runtime']['ports']:
                if p['privatePort'] == 22 and p.get('isIpPublic'):
                    print(f"  {pod['name']}: ssh root@{p['ip']} -p {p['publicPort']} -i ~/.ssh/id_ed25519")
    exit(0)

# Try creating a new pod
print("\n--- Attempting to create new pod ---")
for gpu_type, cloud_type in NEW_POD_CONFIGS:
    print(f"  Trying {gpu_type} ({cloud_type})...", end=" ")
    try:
        result = graphql(f'''mutation {{ podFindAndDeployOnDemand(input: {{
            name: "bigbounce-phase2",
            imageName: "runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04",
            gpuTypeId: "{gpu_type}",
            gpuCount: 1,
            volumeInGb: 100,
            containerDiskInGb: 30,
            startSsh: true,
            cloudType: {cloud_type}
        }}) {{ id }} }}''')
        if result.get('data', {}).get('podFindAndDeployOnDemand'):
            pod_id = result['data']['podFindAndDeployOnDemand']['id']
            print(f"CREATED! Pod ID: {pod_id}")
            print(f"\nWaiting for pod to boot (this can take 2-5 minutes)...")
            for i in range(12):
                time.sleep(30)
                status = graphql('query { myself { pods { id runtime { ports { ip isIpPublic publicPort privatePort } } } } }')
                for pod in status['data']['myself']['pods']:
                    if pod['id'] == pod_id and pod.get('runtime') and pod['runtime'].get('ports'):
                        for p in pod['runtime']['ports']:
                            if p['privatePort'] == 22 and p.get('isIpPublic'):
                                print(f"\n✓ READY: ssh root@{p['ip']} -p {p['publicPort']} -i ~/.ssh/id_ed25519")
                                exit(0)
                print(f"  Still booting... ({(i+1)*30}s)")
            print("  Pod created but didn't get SSH in 6 minutes. Check dashboard.")
            exit(1)
        else:
            err = result.get('errors', [{}])[0].get('message', 'Unknown')[:60]
            print(f"FAILED: {err}")
    except Exception as e:
        print(f"ERROR: {e}")

print("\n✗ No pods available right now. RunPod is supply-constrained.")
print("  Try again in 30-60 minutes, or use the RunPod dashboard to deploy manually.")
print("  All Phase 2 scripts are written and ready to deploy at: pipelines/")
