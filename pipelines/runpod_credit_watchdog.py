#!/usr/bin/env python3
"""
RunPod Credit Watchdog — Auto-stops all running pods when credits drop below threshold.

Checks your RunPod balance every CHECK_INTERVAL seconds. If credits fall below
MIN_CREDITS_USD, all running pods are stopped (not terminated — volumes preserved).

Usage:
  # Run in background on any always-on machine (local Mac, CI, etc.)
  nohup python3 pipelines/runpod_credit_watchdog.py > watchdog.log 2>&1 &

  # Or run as a one-shot check (e.g., from cron every 5 minutes)
  python3 pipelines/runpod_credit_watchdog.py --once

Environment:
  RUNPOD_API_KEY — set in .env.local or as env var
  RUNPOD_MIN_CREDITS — override minimum balance (default: $10)
  RUNPOD_CHECK_INTERVAL — override check interval in seconds (default: 300 = 5 min)
"""
import os
import sys
import json
import time
import urllib.request
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────
MIN_CREDITS_USD = float(os.environ.get("RUNPOD_MIN_CREDITS", "10"))
CHECK_INTERVAL = int(os.environ.get("RUNPOD_CHECK_INTERVAL", "300"))  # 5 minutes
ONE_SHOT = "--once" in sys.argv

# ── Load API key ────────────────────────────────────────────────────────────
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env.local')
api_key = os.environ.get("RUNPOD_API_KEY", "")
if not api_key and os.path.exists(env_file):
    for line in open(env_file):
        if line.startswith('RUNPOD_API_KEY='):
            api_key = line.strip().split('=', 1)[1]

if not api_key:
    print("ERROR: No RUNPOD_API_KEY found. Set in .env.local or environment.")
    sys.exit(1)


def log(msg):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {msg}", flush=True)


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
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def get_balance():
    """Get current RunPod credit balance."""
    result = graphql('{ myself { currentSpendPerHr creditBalance } }')
    me = result['data']['myself']
    return float(me.get('creditBalance', 0)), float(me.get('currentSpendPerHr', 0))


def get_running_pods():
    """Get list of currently running pods."""
    result = graphql('{ myself { pods { id name desiredStatus machineId machine { gpuDisplayName } } } }')
    pods = result['data']['myself']['pods']
    return [p for p in pods if p.get('desiredStatus') == 'RUNNING']


def stop_pod(pod_id):
    """Stop a pod (preserves volume)."""
    result = graphql(f'mutation {{ podStop(input: {{podId: "{pod_id}"}}) {{ id desiredStatus }} }}')
    return result.get('data', {}).get('podStop')


def check_and_protect():
    """Main check: if balance is low, stop all running pods."""
    try:
        balance, spend_per_hr = get_balance()
    except Exception as e:
        log(f"WARNING: Failed to check balance: {e}")
        return

    running = get_running_pods()
    n_running = len(running)

    if spend_per_hr > 0:
        hours_remaining = balance / spend_per_hr
        eta_msg = f", ~{hours_remaining:.1f}h until empty"
    else:
        hours_remaining = float('inf')
        eta_msg = ""

    log(f"Balance: ${balance:.2f} | Spend: ${spend_per_hr:.2f}/hr | "
        f"Running: {n_running} pod(s) | Min: ${MIN_CREDITS_USD:.2f}{eta_msg}")

    if balance < MIN_CREDITS_USD and n_running > 0:
        log(f"CRITICAL: Balance ${balance:.2f} < ${MIN_CREDITS_USD:.2f} threshold!")
        log(f"AUTO-STOPPING {n_running} pod(s) to preserve credits...")

        for pod in running:
            pod_name = pod.get('name', pod['id'])
            gpu = pod.get('machine', {}).get('gpuDisplayName', 'unknown')
            log(f"  Stopping {pod_name} ({pod['id']}, {gpu})...")
            try:
                result = stop_pod(pod['id'])
                if result:
                    log(f"  STOPPED {pod_name}")
                else:
                    log(f"  FAILED to stop {pod_name}")
            except Exception as e:
                log(f"  ERROR stopping {pod_name}: {e}")

        log("All pods stop commands sent. Volumes are preserved.")
        log("Resume pods manually when credits are topped up.")
    elif balance < MIN_CREDITS_USD * 2 and n_running > 0:
        log(f"WARNING: Balance getting low (${balance:.2f}). "
            f"Will auto-stop at ${MIN_CREDITS_USD:.2f}.")


# ── Main loop ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    log(f"RunPod Credit Watchdog started")
    log(f"  Min credits: ${MIN_CREDITS_USD:.2f}")
    log(f"  Check interval: {CHECK_INTERVAL}s")
    log(f"  Mode: {'one-shot' if ONE_SHOT else 'continuous'}")

    if ONE_SHOT:
        check_and_protect()
    else:
        while True:
            check_and_protect()
            time.sleep(CHECK_INTERVAL)
