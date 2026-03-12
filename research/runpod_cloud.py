#!/usr/bin/env python3
"""
RunPod Cloud Management — BigBounce GPU Infrastructure

CLI + Python API for managing RunPod pods for BigBounce research.
Uses the RunPod GraphQL API: https://graphql-spec.runpod.io/

Usage:
    python3 research/runpod_cloud.py status        # Show pod status
    python3 research/runpod_cloud.py ssh            # Print SSH command
    python3 research/runpod_cloud.py stop            # Stop pod (keeps volume)
    python3 research/runpod_cloud.py start           # Restart stopped pod
    python3 research/runpod_cloud.py push-keys       # SCP .env.local to pod
    python3 research/runpod_cloud.py gpus            # List available GPUs
    python3 research/runpod_cloud.py setup           # Full environment setup
    python3 research/runpod_cloud.py run <cmd>       # Run command on pod via SSH
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

# Load .env.local
try:
    from dotenv import load_dotenv
    _env = Path(__file__).resolve().parent.parent / ".env.local"
    if _env.exists():
        load_dotenv(_env)
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNPOD_API_URL = "https://api.runpod.io/graphql"
DEFAULT_POD_ID = "47htajss1ng2ig"


# ── API helpers ──────────────────────────────────────────────────────

def _api_key() -> str:
    """Load RunPod API key from environment."""
    key = os.environ.get("RUNPOD_API_KEY", "")
    if not key:
        print("ERROR: RUNPOD_API_KEY not set. Add it to .env.local")
        sys.exit(1)
    return key


def _graphql(query: str, variables: dict = None) -> dict:
    """Execute authenticated GraphQL request against RunPod API."""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    data = json.dumps(payload).encode()
    # RunPod GraphQL uses query param auth, not Bearer header
    url = f"{RUNPOD_API_URL}?api_key={_api_key()}"
    req = Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "BigBounce-Research/1.0",
        },
        method="POST",
    )

    try:
        resp = urlopen(req, timeout=30)
        result = json.loads(resp.read().decode())
        if "errors" in result:
            for err in result["errors"]:
                print(f"  GraphQL Error: {err.get('message', err)}")
            return None
        return result.get("data", {})
    except URLError as e:
        print(f"  Network error: {e}")
        return None


# ── Pod lifecycle ────────────────────────────────────────────────────

def list_pods() -> list:
    """List all RunPod pods with status, GPU, and IP."""
    query = """
    query {
        myself {
            pods {
                id
                name
                desiredStatus
                runtime {
                    uptimeInSeconds
                    gpus {
                        id
                        gpuUtilPercent
                        memoryUtilPercent
                    }
                    ports {
                        ip
                        isIpPublic
                        privatePort
                        publicPort
                        type
                    }
                }
                machine {
                    gpuDisplayName
                }
                gpuCount
                vcpuCount
                memoryInGb
                volumeInGb
                containerDiskInGb
                imageName
                costPerHr
            }
        }
    }
    """
    data = _graphql(query)
    if not data:
        return []
    return data.get("myself", {}).get("pods", [])


def get_pod(pod_id: str = None) -> dict:
    """Get details for a single pod."""
    pid = pod_id or DEFAULT_POD_ID
    query = """
    query Pod($podId: String!) {
        pod(input: { podId: $podId }) {
            id
            name
            desiredStatus
            runtime {
                uptimeInSeconds
                gpus {
                    id
                    gpuUtilPercent
                    memoryUtilPercent
                }
                ports {
                    ip
                    isIpPublic
                    privatePort
                    publicPort
                    type
                }
            }
            machine {
                gpuDisplayName
            }
            gpuCount
            vcpuCount
            memoryInGb
            volumeInGb
            containerDiskInGb
            imageName
            costPerHr
        }
    }
    """
    data = _graphql(query, {"podId": pid})
    if not data:
        return {}
    return data.get("pod", {})


def create_pod(
    gpu_type: str = "NVIDIA RTX 6000 Ada Generation",
    name: str = "bigbounce-gpu",
    image: str = "runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04",
    volume_gb: int = 50,
    container_disk_gb: int = 20,
    network_volume_id: str = None,
) -> dict:
    """Launch a new RunPod pod. If network_volume_id is provided, attaches
    the network volume and ignores volume_gb (NV provides /workspace)."""
    if network_volume_id:
        query = """
        mutation CreatePod(
            $name: String!
            $imageName: String!
            $gpuTypeId: String!
            $containerDiskInGb: Int
            $gpuCount: Int
            $networkVolumeId: String
        ) {
            podFindAndDeployOnDemand(input: {
                name: $name
                imageName: $imageName
                gpuTypeId: $gpuTypeId
                containerDiskInGb: $containerDiskInGb
                gpuCount: $gpuCount
                networkVolumeId: $networkVolumeId
                startSsh: true
            }) {
                id
                name
                desiredStatus
                machine {
                    gpuDisplayName
                }
                costPerHr
            }
        }
        """
        variables = {
            "name": name,
            "imageName": image,
            "gpuTypeId": gpu_type,
            "containerDiskInGb": container_disk_gb,
            "gpuCount": 1,
            "networkVolumeId": network_volume_id,
        }
    else:
        query = """
        mutation CreatePod(
            $name: String!
            $imageName: String!
            $gpuTypeId: String!
            $volumeInGb: Int
            $containerDiskInGb: Int
            $gpuCount: Int
        ) {
            podFindAndDeployOnDemand(input: {
                name: $name
                imageName: $imageName
                gpuTypeId: $gpuTypeId
                volumeInGb: $volumeInGb
                containerDiskInGb: $containerDiskInGb
                gpuCount: $gpuCount
                startSsh: true
            }) {
                id
                name
                desiredStatus
                machine {
                    gpuDisplayName
                }
                costPerHr
            }
        }
        """
        variables = {
            "name": name,
            "imageName": image,
            "gpuTypeId": gpu_type,
            "volumeInGb": volume_gb,
            "containerDiskInGb": container_disk_gb,
            "gpuCount": 1,
        }
    data = _graphql(query, variables)
    if not data:
        return {}
    return data.get("podFindAndDeployOnDemand", {})


def create_network_volume(
    name: str = "bigbounce-paper1-canonical",
    size_gb: int = 75,
    datacenter_id: str = "US-TX-3",
) -> dict:
    """Create a persistent network volume."""
    query = """
    mutation CreateNetworkVolume(
        $name: String!
        $size: Int!
        $dataCenterId: String!
    ) {
        createNetworkVolume(input: {
            name: $name
            size: $size
            dataCenterId: $dataCenterId
        }) {
            id
            name
            size
            dataCenterId
        }
    }
    """
    data = _graphql(query, {
        "name": name,
        "size": size_gb,
        "dataCenterId": datacenter_id,
    })
    if not data:
        return {}
    return data.get("createNetworkVolume", {})


def list_network_volumes() -> list:
    """List all network volumes."""
    query = """
    query {
        myself {
            networkVolumes {
                id
                name
                size
                dataCenterId
            }
        }
    }
    """
    data = _graphql(query)
    if not data:
        return []
    return data.get("myself", {}).get("networkVolumes", [])


def stop_pod(pod_id: str = None) -> dict:
    """Stop a pod (keeps volume data)."""
    pid = pod_id or DEFAULT_POD_ID
    query = """
    mutation StopPod($podId: String!) {
        podStop(input: { podId: $podId }) {
            id
            desiredStatus
        }
    }
    """
    data = _graphql(query, {"podId": pid})
    if not data:
        return {}
    return data.get("podStop", {})


def start_pod(pod_id: str = None) -> dict:
    """Restart a stopped pod."""
    pid = pod_id or DEFAULT_POD_ID
    query = """
    mutation StartPod($podId: String!) {
        podResume(input: { podId: $podId, gpuCount: 1 }) {
            id
            desiredStatus
        }
    }
    """
    data = _graphql(query, {"podId": pid})
    if not data:
        return {}
    return data.get("podResume", {})


def terminate_pod(pod_id: str = None) -> dict:
    """Destroy a pod and its volume. IRREVERSIBLE."""
    pid = pod_id or DEFAULT_POD_ID
    query = """
    mutation TerminatePod($podId: String!) {
        podTerminate(input: { podId: $podId })
    }
    """
    data = _graphql(query, {"podId": pid})
    return data or {}


def list_gpu_types() -> list:
    """List available GPU types with pricing."""
    query = """
    query GpuTypes {
        gpuTypes {
            id
            displayName
            memoryInGb
            secureCloud
            communityCloud
            lowestPrice(input: { gpuCount: 1 }) {
                minimumBidPrice
                uninterruptablePrice
            }
        }
    }
    """
    data = _graphql(query)
    if not data:
        return []
    return data.get("gpuTypes", [])


# ── SSH helpers ──────────────────────────────────────────────────────

def _get_ssh_info(pod_id: str = None) -> tuple:
    """Extract SSH host and port from pod runtime info."""
    pod = get_pod(pod_id)
    if not pod or not pod.get("runtime"):
        return None, None

    ports = pod["runtime"].get("ports", [])
    for p in ports:
        if p.get("privatePort") == 22 and p.get("isIpPublic"):
            return p["ip"], p["publicPort"]

    return None, None


def get_ssh_command(pod_id: str = None) -> str:
    """Generate the SSH command for a pod."""
    ip, port = _get_ssh_info(pod_id)
    if not ip:
        return "Pod not running or SSH not available"
    return f"ssh root@{ip} -p {port} -i ~/.ssh/id_ed25519"


def push_keys(pod_id: str = None) -> bool:
    """SCP .env.local to the pod's /workspace/bigbounce/ directory."""
    env_file = PROJECT_ROOT / ".env.local"
    if not env_file.exists():
        print("  ERROR: .env.local not found")
        return False

    ip, port = _get_ssh_info(pod_id)
    if not ip:
        print("  ERROR: Pod not running or SSH not available")
        return False

    # Ensure target directory exists
    mkdir_cmd = f"ssh -o StrictHostKeyChecking=no root@{ip} -p {port} -i ~/.ssh/id_ed25519 'mkdir -p /workspace/bigbounce'"
    subprocess.run(mkdir_cmd, shell=True, check=True)

    # SCP the file
    scp_cmd = (
        f"scp -o StrictHostKeyChecking=no -P {port} -i ~/.ssh/id_ed25519 "
        f"{env_file} root@{ip}:/workspace/bigbounce/.env.local"
    )
    result = subprocess.run(scp_cmd, shell=True)
    if result.returncode == 0:
        print("  .env.local pushed to pod:/workspace/bigbounce/.env.local")
        return True
    else:
        print("  SCP failed")
        return False


def run_command(pod_id: str = None, cmd: str = "echo ok") -> str:
    """Execute a command on the pod via SSH."""
    ip, port = _get_ssh_info(pod_id)
    if not ip:
        return "Pod not running or SSH not available"

    ssh_cmd = (
        f"ssh -o StrictHostKeyChecking=no root@{ip} -p {port} "
        f"-i ~/.ssh/id_ed25519 '{cmd}'"
    )
    result = subprocess.run(ssh_cmd, shell=True, capture_output=True, text=True, timeout=120)
    output = result.stdout
    if result.stderr:
        output += "\n" + result.stderr
    return output.strip()


def setup_pod(pod_id: str = None) -> bool:
    """Full environment setup: install deps, clone repo, push keys."""
    pid = pod_id or DEFAULT_POD_ID
    print("\n  BigBounce RunPod Setup")
    print("  " + "=" * 40)

    # 1. Install Python deps
    print("\n  [1/4] Installing Python dependencies...")
    deps = (
        "transformers datasets astroML astroquery anthropic openai "
        "google-generativeai python-dotenv scipy matplotlib seaborn "
        "huggingface_hub timm cobaya camb healpy getdist requests pandas"
    )
    output = run_command(pid, f"pip install -q {deps} 2>&1 | tail -5")
    print(f"    {output}")

    # 2. Clone BigBounce repo
    print("\n  [2/4] Cloning BigBounce repo to /workspace/bigbounce...")
    output = run_command(
        pid,
        "cd /workspace && "
        "(git clone https://github.com/Hubify-Projects/bigbounce.git 2>&1 || "
        "(cd bigbounce && git pull 2>&1))"
    )
    print(f"    {output}")

    # 3. Push API keys
    print("\n  [3/4] Pushing API keys...")
    push_keys(pid)

    # 4. Validate environment
    print("\n  [4/4] Validating environment...")
    output = run_command(
        pid,
        "cd /workspace/bigbounce && python3 research/env_check.py 2>&1"
    )
    print(f"    {output}")

    # Verify GPU
    print("\n  GPU Check:")
    output = run_command(
        pid,
        "python3 -c \"import torch; print(f'GPU: {torch.cuda.get_device_name(0)}'); "
        "print(f'VRAM: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB'); "
        "print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')\""
    )
    print(f"    {output}")

    print("\n  Setup complete!")
    return True


# ── Display helpers ──────────────────────────────────────────────────

def _format_uptime(seconds: int) -> str:
    """Format seconds into human-readable uptime."""
    if not seconds:
        return "—"
    hours = seconds // 3600
    mins = (seconds % 3600) // 60
    if hours > 0:
        return f"{hours}h {mins}m"
    return f"{mins}m"


def print_status(pod_id: str = None):
    """Print formatted pod status."""
    pod = get_pod(pod_id)
    if not pod:
        print("  Pod not found or API error")
        return

    print(f"\n  BigBounce RunPod Status")
    print(f"  {'=' * 40}")
    print(f"  Pod ID:    {pod.get('id', '—')}")
    print(f"  Name:      {pod.get('name', '—')}")
    print(f"  Status:    {pod.get('desiredStatus', '—')}")
    print(f"  GPU:       {pod.get('machine', {}).get('gpuDisplayName', '—')} x{pod.get('gpuCount', 1)}")
    print(f"  vCPU:      {pod.get('vcpuCount', '—')}")
    print(f"  RAM:       {pod.get('memoryInGb', '—')} GB")
    print(f"  Volume:    {pod.get('volumeInGb', '—')} GB")
    print(f"  Disk:      {pod.get('containerDiskInGb', '—')} GB")
    print(f"  Image:     {pod.get('imageName', '—')}")
    print(f"  Cost:      ${pod.get('costPerHr', 0):.3f}/hr")

    runtime = pod.get("runtime")
    if runtime:
        uptime = _format_uptime(runtime.get("uptimeInSeconds", 0))
        print(f"  Uptime:    {uptime}")

        gpus = runtime.get("gpus", [])
        for i, gpu in enumerate(gpus):
            util = gpu.get("gpuUtilPercent", 0)
            mem = gpu.get("memoryUtilPercent", 0)
            print(f"  GPU {i}:     {util}% util, {mem}% VRAM")

    ssh_cmd = get_ssh_command(pod_id)
    print(f"\n  SSH:       {ssh_cmd}")
    print()


def print_gpus():
    """Print available GPU types with pricing."""
    gpus = list_gpu_types()
    if not gpus:
        print("  No GPU types found or API error")
        return

    print(f"\n  RunPod Available GPUs")
    print(f"  {'=' * 70}")
    print(f"  {'GPU':<35} {'VRAM':>6} {'On-Demand':>10} {'Spot':>8}")
    print(f"  {'-' * 35} {'-' * 6} {'-' * 10} {'-' * 8}")

    # Sort by VRAM
    gpus.sort(key=lambda g: g.get("memoryInGb", 0))

    for gpu in gpus:
        name = gpu.get("displayName", "—")
        vram = gpu.get("memoryInGb", 0)
        pricing = gpu.get("lowestPrice") or {}
        on_demand = pricing.get("uninterruptablePrice")
        spot = pricing.get("minimumBidPrice")

        on_demand_str = f"${on_demand:.2f}/hr" if on_demand else "—"
        spot_str = f"${spot:.2f}/hr" if spot else "—"

        if on_demand or spot:  # Only show GPUs with pricing
            print(f"  {name:<35} {vram:>4} GB {on_demand_str:>10} {spot_str:>8}")

    print()


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        print_status()
    elif cmd == "ssh":
        print(get_ssh_command())
    elif cmd == "stop":
        result = stop_pod()
        print(f"  Pod stopped: {result}")
    elif cmd == "start":
        result = start_pod()
        print(f"  Pod started: {result}")
    elif cmd == "push-keys":
        push_keys()
    elif cmd == "gpus":
        print_gpus()
    elif cmd == "setup":
        setup_pod()
    elif cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: runpod_cloud.py run <command>")
            sys.exit(1)
        remote_cmd = " ".join(sys.argv[2:])
        output = run_command(cmd=remote_cmd)
        print(output)
    elif cmd == "terminate":
        confirm = input("  DANGER: This will destroy the pod and volume. Type 'yes' to confirm: ")
        if confirm.strip().lower() == "yes":
            result = terminate_pod()
            print(f"  Pod terminated: {result}")
        else:
            print("  Cancelled")
    else:
        print(f"  Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
