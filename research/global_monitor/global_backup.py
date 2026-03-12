#!/usr/bin/env python3
"""
BigBounce Global Backup Manager
=================================
For each pod in pod_registry.yaml, create timestamped backup tarballs
of critical outputs directly on the pod (read-only, non-disruptive).

Outputs:
  - global_backup_latest.txt
  - backup_history/TIMESTAMP.txt

Usage:
  python3 global_backup.py [--registry pod_registry.yaml] [--timeout 10] [--dry-run]
"""

import argparse
import datetime
import os
import subprocess
import sys
import time

import yaml


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REGISTRY = os.path.join(SCRIPT_DIR, "pod_registry.yaml")
BACKUP_HISTORY_DIR = os.path.join(SCRIPT_DIR, "backup_history")
LATEST_TXT = os.path.join(SCRIPT_DIR, "global_backup_latest.txt")

SSH_KEY = os.path.expanduser("~/.ssh/id_ed25519")
SSH_BASE_OPTS = [
    "-i", SSH_KEY,
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "LogLevel=ERROR",
]

BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
SEP = "=" * 78

# Backup targets by track type
MCMC_BACKUP_PATHS = [
    "chains/",
    "controls_lcdm/",
    "covmats/",
    "frozen_packs/",
    "cosmology/",
    "*.yaml",
    "*.log",
    "*.png",
]

PAPER2_BACKUP_PATHS = [
    "runs/",
    "figures/",
    "outputs/",
    "*.py",
    "*.md",
    "model.pt",
]


# ---------------------------------------------------------------------------
# SSH helpers
# ---------------------------------------------------------------------------

def ssh_command(host, port, cmd, timeout=10):
    """Run a command over SSH. Returns (success, stdout, stderr)."""
    if not host or not port:
        return False, "", "No SSH credentials configured"

    full_cmd = (
        ["ssh"]
        + SSH_BASE_OPTS
        + ["-o", "ConnectTimeout=%d" % timeout]
        + ["-p", str(port)]
        + ["root@%s" % host]
        + [cmd]
    )
    try:
        proc = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            timeout=timeout + 30,  # Backup commands may take longer
        )
        return proc.returncode == 0, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "", "SSH timeout after %ds" % (timeout + 30)
    except Exception as exc:
        return False, "", "SSH error: %s" % str(exc)


def ssh_alive(host, port, timeout=10):
    """Quick alive check."""
    ok, out, _ = ssh_command(host, port, "echo ok", timeout=timeout)
    return ok and out.strip() == "ok"


# ---------------------------------------------------------------------------
# Backup logic
# ---------------------------------------------------------------------------

def check_paths_exist(host, port, working_dir, paths, timeout):
    """Check which backup paths actually exist on the pod. Returns list of existing paths."""
    existing = []
    for p in paths:
        full_path = "%s/%s" % (working_dir, p)
        # Handle glob patterns
        if "*" in p:
            ok, out, _ = ssh_command(
                host, port,
                "ls %s 2>/dev/null | head -1" % full_path,
                timeout,
            )
            if ok and out.strip():
                existing.append(p)
        else:
            ok, out, _ = ssh_command(
                host, port,
                "test -e %s && echo yes || echo no" % full_path.rstrip("/"),
                timeout,
            )
            if ok and out.strip() == "yes":
                existing.append(p)
    return existing


def create_backup_tarball(host, port, working_dir, existing_paths, pod_name, timestamp, timeout, dry_run=False):
    """
    Create a timestamped tarball on the pod.
    Returns (success, tarball_path, size_bytes, message).
    """
    if not existing_paths:
        return False, "", 0, "No paths to back up"

    backup_dir = "%s/backups" % working_dir
    tarball_name = "backup_%s_%s.tar.gz" % (pod_name, timestamp)
    tarball_path = "%s/%s" % (backup_dir, tarball_name)

    # Build tar command — include only existing paths
    path_args = " ".join(existing_paths)

    if dry_run:
        msg = "DRY RUN: would tar %s into %s" % (path_args, tarball_path)
        return True, tarball_path, 0, msg

    # Create backup directory
    ok, _, err = ssh_command(
        host, port,
        "mkdir -p %s" % backup_dir,
        timeout,
    )
    if not ok:
        return False, "", 0, "Failed to create backup dir: %s" % err

    # Create tarball
    tar_cmd = "cd %s && tar czf %s %s 2>&1" % (working_dir, tarball_path, path_args)
    ok, out, err = ssh_command(
        host, port,
        tar_cmd,
        timeout=timeout + 60,  # tarballs can take time
    )
    if not ok:
        return False, "", 0, "tar failed: %s %s" % (out, err)

    # Get size
    ok, out, _ = ssh_command(
        host, port,
        "stat -c %%s %s 2>/dev/null || wc -c < %s" % (tarball_path, tarball_path),
        timeout,
    )
    size_bytes = 0
    if ok:
        try:
            size_bytes = int(out.strip())
        except ValueError:
            pass

    return True, tarball_path, size_bytes, "Backup created successfully"


def format_size(size_bytes):
    """Human-readable size."""
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    idx = 0
    size = float(size_bytes)
    while size >= 1024.0 and idx < len(units) - 1:
        size /= 1024.0
        idx += 1
    return "%.1f %s" % (size, units[idx])


# ---------------------------------------------------------------------------
# Per-pod backup
# ---------------------------------------------------------------------------

def backup_pod(pod, timestamp, timeout, dry_run=False):
    """
    Perform backup for a single pod.
    Returns a result dict.
    """
    pod_name = pod.get("pod_name", "unknown")
    host = pod.get("ssh_host")
    port = pod.get("ssh_port")
    working_dir = pod.get("working_dir", "/workspace")
    track = pod.get("track_name", "")
    ssh_str = pod.get("ssh")

    result = {
        "pod_name": pod_name,
        "track_name": track,
        "ssh_configured": bool(ssh_str),
        "alive": False,
        "paths_checked": [],
        "paths_found": [],
        "backup_created": False,
        "tarball_path": "",
        "size_bytes": 0,
        "size_human": "0 B",
        "message": "",
        "timestamp": timestamp,
    }

    # Skip if SSH not configured
    if not ssh_str or not host or not port:
        result["message"] = "SSH not configured (pending boot) — skipped"
        print("  %-30s %sSKIPPED%s (no SSH)" % (pod_name, YELLOW, RESET))
        return result

    # Alive check
    print("  %-30s checking..." % pod_name, end="", flush=True)
    alive = ssh_alive(host, port, timeout=timeout)
    result["alive"] = alive

    if not alive:
        result["message"] = "UNREACHABLE — skipped"
        print("\r  %-30s %sUNREACHABLE%s" % (pod_name, RED, RESET))
        return result

    # Determine backup paths based on track
    if "paper1" in track:
        backup_paths = MCMC_BACKUP_PATHS
    elif "paper2" in track:
        backup_paths = PAPER2_BACKUP_PATHS
    else:
        # Generic — try both
        backup_paths = list(set(MCMC_BACKUP_PATHS + PAPER2_BACKUP_PATHS))

    result["paths_checked"] = backup_paths

    # Check which paths exist
    existing = check_paths_exist(host, port, working_dir, backup_paths, timeout)
    result["paths_found"] = existing

    if not existing:
        result["message"] = "No critical outputs found to back up"
        print("\r  %-30s %sNO DATA%s  (checked: %s)" % (
            pod_name, YELLOW, RESET, ", ".join(backup_paths),
        ))
        return result

    # Create backup
    ok, tarball_path, size_bytes, msg = create_backup_tarball(
        host, port, working_dir, existing, pod_name, timestamp, timeout, dry_run,
    )
    result["backup_created"] = ok
    result["tarball_path"] = tarball_path
    result["size_bytes"] = size_bytes
    result["size_human"] = format_size(size_bytes)
    result["message"] = msg

    if ok:
        print("\r  %-30s %sOK%s  %s  (%s)  [%s]" % (
            pod_name, GREEN, RESET, format_size(size_bytes),
            ", ".join(existing), tarball_path,
        ))
    else:
        print("\r  %-30s %sFAILED%s  %s" % (pod_name, RED, RESET, msg))

    return result


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def save_backup_report(results, elapsed, timestamp):
    """Save backup report to latest and history files."""
    if not os.path.isdir(BACKUP_HISTORY_DIR):
        os.makedirs(BACKUP_HISTORY_DIR)

    lines = []
    lines.append("BigBounce Global Backup Report")
    lines.append("Generated: %s UTC" % datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("Duration: %.1fs" % elapsed)
    lines.append(SEP.replace("\033[", ""))  # no ANSI in files
    lines.append("")

    total_size = 0
    success_count = 0
    skip_count = 0
    fail_count = 0

    for r in results:
        status = "OK" if r["backup_created"] else ("SKIP" if not r["alive"] else "FAIL")
        if r["backup_created"]:
            success_count += 1
            total_size += r["size_bytes"]
        elif not r["ssh_configured"] or not r["alive"]:
            skip_count += 1
        else:
            fail_count += 1

        lines.append("%-30s  [%s]" % (r["pod_name"], status))
        lines.append("  Track: %s" % r["track_name"])
        lines.append("  Paths found: %s" % (", ".join(r["paths_found"]) or "none"))
        if r["backup_created"]:
            lines.append("  Tarball: %s (%s)" % (r["tarball_path"], r["size_human"]))
        lines.append("  Message: %s" % r["message"])
        lines.append("")

    lines.append("=" * 78)
    lines.append("Summary: %d OK, %d skipped, %d failed" % (success_count, skip_count, fail_count))
    lines.append("Total backup size: %s" % format_size(total_size))

    report = "\n".join(lines)

    with open(LATEST_TXT, "w") as f:
        f.write(report)

    history_file = os.path.join(BACKUP_HISTORY_DIR, "%s.txt" % timestamp)
    with open(history_file, "w") as f:
        f.write(report)

    print("\nBackup report saved:")
    print("  %s" % LATEST_TXT)
    print("  %s" % history_file)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_registry(path):
    """Load pod_registry.yaml and return list of pod dicts."""
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    pods = data.get("pods", [])
    if not pods:
        print("WARNING: No pods found in registry %s" % path)
    return pods


def parse_args():
    parser = argparse.ArgumentParser(
        description="BigBounce Global Backup Manager — create timestamped backup tarballs on all pods."
    )
    parser.add_argument(
        "--registry",
        default=DEFAULT_REGISTRY,
        help="Path to pod_registry.yaml (default: %s)" % DEFAULT_REGISTRY,
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="SSH connect timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be backed up without creating tarballs",
    )
    parser.add_argument(
        "--pod",
        type=str,
        default=None,
        help="Back up only this specific pod (by pod_name)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    pods = load_registry(args.registry)

    if args.pod:
        pods = [p for p in pods if p.get("pod_name") == args.pod]
        if not pods:
            print("ERROR: Pod '%s' not found in registry." % args.pod)
            sys.exit(1)

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    print("%sBigBounce Global Backup Manager%s" % (BOLD, RESET))
    if args.dry_run:
        print("%sDRY RUN — no tarballs will be created%s" % (YELLOW, RESET))
    print("Backing up %d pods (timeout=%ds, timestamp=%s)...\n" % (
        len(pods), args.timeout, timestamp,
    ))

    start_time = time.time()
    results = []

    for pod in pods:
        try:
            result = backup_pod(pod, timestamp, args.timeout, dry_run=args.dry_run)
            results.append(result)
        except Exception as exc:
            pod_name = pod.get("pod_name", "unknown")
            print("  %-30s %sERROR%s %s" % (pod_name, RED, RESET, str(exc)))
            results.append({
                "pod_name": pod_name,
                "track_name": pod.get("track_name", ""),
                "ssh_configured": bool(pod.get("ssh")),
                "alive": False,
                "paths_checked": [],
                "paths_found": [],
                "backup_created": False,
                "tarball_path": "",
                "size_bytes": 0,
                "size_human": "0 B",
                "message": "Exception: %s" % str(exc),
                "timestamp": timestamp,
            })

    elapsed = time.time() - start_time

    # Summary
    success = sum(1 for r in results if r["backup_created"])
    total_size = sum(r["size_bytes"] for r in results)
    print("\n%s" % SEP)
    print(
        "%sSummary:%s %d/%d backups created, total size %s, took %.1fs"
        % (BOLD, RESET, success, len(results), format_size(total_size), elapsed)
    )

    save_backup_report(results, elapsed, timestamp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
