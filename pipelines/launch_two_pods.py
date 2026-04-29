#!/usr/bin/env python3
"""
Launch 2 RunPod pods for the final paper completion sprint.

Pod A: A100 SXM 80GB ($1.39/hr) — Chirality tasks + PDF compile
Pod B: L40S 48GB ($0.79/hr) — NaMaster 500 MC + UMAP stability

Usage: python3 pipelines/launch_two_pods.py
"""
import os
import json
import sys
import urllib.request

# Load API key
env_file = os.path.join(os.path.dirname(__file__), '..', '.env.local')
api_key = None
if os.path.exists(env_file):
    for line in open(env_file):
        if line.startswith('RUNPOD_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

if not api_key:
    print("ERROR: No RUNPOD_API_KEY found in .env.local")
    sys.exit(1)

print(f"API key: {api_key[:8]}...{api_key[-4:]}")

def graphql(query):
    """Execute a RunPod GraphQL query."""
    req = urllib.request.Request(
        'https://api.runpod.io/graphql',
        data=json.dumps({'query': query}).encode(),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"GraphQL error: {e}")
        return None

# Check existing pods
print("\n[1] Checking existing pods...")
result = graphql('{ myself { pods { id name runtime { gpus { id } } } } }')
if result and 'data' in result:
    pods = result['data']['myself']['pods']
    print(f"  Found {len(pods)} existing pod(s)")
    for p in pods:
        print(f"    {p['id']}: {p['name']}")
else:
    print("  No existing pods or query failed")

# Pod configurations
PODS = [
    {
        "name": "paper-sprint-A100",
        "gpu": "NVIDIA A100-SXM4-80GB",
        "cloud": "SECURE",
        "disk": 50,
        "volume": 100,
        "image": "runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04",
        "script": "pod_a_chirality_compile.sh",
        "description": "Pod A: Chirality bias + Catalog C + MASTER + edge-on + PDF compile",
    },
    {
        "name": "paper-sprint-L40S",
        "gpu": "NVIDIA L40S",
        "cloud": "COMMUNITY",
        "disk": 30,
        "volume": 50,
        "image": "runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04",
        "script": "pod_b_namaster_umap.sh",
        "description": "Pod B: NaMaster 500 MC + UMAP stability",
    },
]

# Fallback GPU options (in case primary isn't available)
FALLBACKS = {
    "NVIDIA A100-SXM4-80GB": [
        "NVIDIA A100 80GB PCIe",
        "NVIDIA H100 80GB HBM3",
        "NVIDIA A100-SXM4-80GB",
    ],
    "NVIDIA L40S": [
        "NVIDIA L40S",
        "NVIDIA RTX A6000",
        "NVIDIA GeForce RTX 4090",
        "NVIDIA RTX A5000",
    ],
}

print("\n[2] Launching pods...")

launched = []
for pod_config in PODS:
    print(f"\n--- {pod_config['description']} ---")

    gpu_options = [pod_config['gpu']] + FALLBACKS.get(pod_config['gpu'], [])

    pod_created = False
    for gpu_type in gpu_options:
        print(f"  Trying {gpu_type}...")

        # Check availability + price
        price_query = f'''{{
          gpuTypes(input: {{ id: "{gpu_type}" }}) {{
            id
            displayName
            lowestPrice(input: {{ gpuCount: 1 }}) {{
              minimumBidPrice
              uninterruptablePrice
            }}
          }}
        }}'''
        price_result = graphql(price_query)
        if price_result and price_result.get('data', {}).get('gpuTypes'):
            gpu_info = price_result['data']['gpuTypes'][0]
            lp = gpu_info.get('lowestPrice')
            if lp:
                price = lp.get('uninterruptablePrice') or lp.get('minimumBidPrice', 'N/A')
                print(f"    Available: ${price}/hr")
            else:
                print(f"    No pricing info — may not be available")
                continue
        else:
            print(f"    Not available")
            continue

        # Create pod
        create_query = f'''
        mutation {{
          podFindAndDeployOnDemand(input: {{
            name: "{pod_config['name']}"
            gpuTypeId: "{gpu_type}"
            gpuCount: 1
            cloudType: {pod_config['cloud']}
            containerDiskInGb: {pod_config['disk']}
            volumeInGb: {pod_config['volume']}
            imageName: "{pod_config['image']}"
            startSsh: true
            supportPublicIp: true
          }}) {{
            id
            name
            runtime {{
              ports {{
                ip
                isIpPublic
                privatePort
                publicPort
              }}
            }}
          }}
        }}'''

        create_result = graphql(create_query)
        if create_result and 'data' in create_result and create_result['data'].get('podFindAndDeployOnDemand'):
            pod_data = create_result['data']['podFindAndDeployOnDemand']
            print(f"    CREATED: {pod_data['id']} ({pod_config['name']})")
            launched.append({
                'id': pod_data['id'],
                'name': pod_config['name'],
                'gpu': gpu_type,
                'script': pod_config['script'],
                'description': pod_config['description'],
            })
            pod_created = True
            break
        else:
            errors = create_result.get('errors', []) if create_result else []
            err_msg = errors[0].get('message', 'Unknown error') if errors else 'Unknown error'
            print(f"    Failed: {err_msg}")

    if not pod_created:
        print(f"  WARNING: Could not create pod for {pod_config['description']}")

# Summary
print("\n" + "=" * 70)
print("LAUNCH SUMMARY")
print("=" * 70)

if launched:
    for pod in launched:
        print(f"  {pod['id']}: {pod['name']} ({pod['gpu']})")
        print(f"    Script: {pod['script']}")
        print(f"    Task: {pod['description']}")

    # Save pod info for later use
    info_path = os.path.join(os.path.dirname(__file__), '..', 'project-context', 'active_pods_sprint.json')
    with open(info_path, 'w') as f:
        json.dump({
            'launched': launched,
            'timestamp': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
            'purpose': 'Final paper completion sprint — 15 remaining adversarial review items',
        }, f, indent=2)
    print(f"\n  Pod info saved to {info_path}")

    print(f"\n  Next steps:")
    print(f"  1. Wait ~2 min for pods to boot")
    print(f"  2. SSH into each pod and run the orchestration script:")
    for pod in launched:
        script = pod['script']
        print(f"     ssh root@<IP> -p <PORT> 'bash /root/bigbounce/pipelines/{script}'")
    print("  3. Monitor progress via: ssh root@<IP> -p <PORT> 'cat /root/results/progress.log'")
else:
    print("  No pods launched. Check GPU availability on RunPod.")
    print("  You may need to try different GPU types or wait for availability.")
