#!/usr/bin/env python3
"""
BigBounce Global Status Monitor
================================
SSH into every pod in pod_registry.yaml, collect live telemetry,
and produce a concise terminal dashboard plus persistent logs.

Outputs:
  - global_status_latest.txt   (human-readable)
  - global_status_latest.json  (machine-readable)
  - global_status_history/TIMESTAMP.txt

Usage:
  python3 global_status.py [--registry pod_registry.yaml] [--timeout 10]
"""

import argparse
import csv
import datetime
import json
import os
import subprocess
import sys
import time
import traceback

import yaml


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REGISTRY = os.path.join(SCRIPT_DIR, "pod_registry.yaml")
HISTORY_DIR = os.path.join(SCRIPT_DIR, "global_status_history")
LATEST_TXT = os.path.join(SCRIPT_DIR, "global_status_latest.txt")
LATEST_JSON = os.path.join(SCRIPT_DIR, "global_status_latest.json")

SSH_KEY = os.path.expanduser("~/.ssh/id_ed25519")
SSH_BASE_OPTS = [
    "-i", SSH_KEY,
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "LogLevel=ERROR",
]

DISK_WARN_PERCENT = 80
STALE_OUTPUT_HOURS = 2

# Terminal formatting helpers
BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
SEP = "=" * 78


# ---------------------------------------------------------------------------
# SSH helpers
# ---------------------------------------------------------------------------

def ssh_command(host, port, cmd, timeout=10):
    """Run a single command over SSH. Returns (success, stdout, stderr)."""
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
            timeout=timeout + 5,
        )
        return proc.returncode == 0, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "", "SSH timeout after %ds" % timeout
    except Exception as exc:
        return False, "", "SSH error: %s" % str(exc)


def ssh_alive(host, port, timeout=10):
    """Quick alive check — just run 'echo ok'."""
    ok, out, err = ssh_command(host, port, "echo ok", timeout=timeout)
    return ok and out.strip() == "ok"


# ---------------------------------------------------------------------------
# Collectors — each returns a dict of findings
# ---------------------------------------------------------------------------

def collect_process_info(host, port, timeout):
    """Count cobaya/python processes, list key process names."""
    info = {"cobaya_count": 0, "python_count": 0, "key_processes": []}

    ok, out, _ = ssh_command(host, port, "pgrep -c cobaya 2>/dev/null || echo 0", timeout)
    if ok:
        try:
            info["cobaya_count"] = int(out.strip())
        except ValueError:
            pass

    ok, out, _ = ssh_command(host, port, "pgrep -c python 2>/dev/null || echo 0", timeout)
    if ok:
        try:
            info["python_count"] = int(out.strip())
        except ValueError:
            pass

    ok, out, _ = ssh_command(
        host, port,
        "ps aux --no-headers | grep -E 'cobaya|python|freeze|monitor' | grep -v grep | awk '{print $11}' | sort | uniq -c | sort -rn | head -10",
        timeout,
    )
    if ok and out:
        info["key_processes"] = [line.strip() for line in out.splitlines() if line.strip()]

    return info


def collect_disk_usage(host, port, working_dir, timeout):
    """df -h on the working directory's mount."""
    info = {"raw": "", "percent_used": None, "total": "", "used": "", "avail": ""}
    ok, out, _ = ssh_command(host, port, "df -h %s | tail -1" % working_dir, timeout)
    if ok and out:
        info["raw"] = out
        parts = out.split()
        if len(parts) >= 5:
            info["total"] = parts[1]
            info["used"] = parts[2]
            info["avail"] = parts[3]
            try:
                info["percent_used"] = int(parts[4].rstrip("%"))
            except ValueError:
                pass
    return info


def collect_memory_usage(host, port, timeout):
    """free -m summary."""
    info = {"raw": "", "total_mb": None, "used_mb": None, "free_mb": None}
    ok, out, _ = ssh_command(host, port, "free -m | grep '^Mem:'", timeout)
    if ok and out:
        info["raw"] = out
        parts = out.split()
        if len(parts) >= 4:
            try:
                info["total_mb"] = int(parts[1])
                info["used_mb"] = int(parts[2])
                info["free_mb"] = int(parts[3])
            except (ValueError, IndexError):
                pass
    return info


def collect_gpu_info(host, port, timeout):
    """nvidia-smi query for utilization and memory."""
    info = {"available": False, "util_percent": None, "mem_used_mb": None, "raw": ""}
    ok, out, _ = ssh_command(
        host, port,
        "nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader,nounits 2>/dev/null",
        timeout,
    )
    if ok and out:
        info["available"] = True
        info["raw"] = out
        parts = out.split(",")
        if len(parts) >= 2:
            try:
                info["util_percent"] = int(parts[0].strip())
                info["mem_used_mb"] = int(parts[1].strip())
            except ValueError:
                pass
    return info


def collect_latest_output_timestamps(host, port, expected_outputs, timeout):
    """Find the newest file under expected_outputs and its mtime."""
    info = {"newest_file": None, "newest_mtime": None, "age_seconds": None, "stale": False}
    if not expected_outputs:
        return info

    cmd = (
        "find %s -type f -printf '%%T@ %%p\\n' 2>/dev/null | sort -rn | head -1"
        % expected_outputs
    )
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out:
        parts = out.split(None, 1)
        if len(parts) == 2:
            try:
                mtime = float(parts[0])
                info["newest_file"] = parts[1]
                info["newest_mtime"] = datetime.datetime.utcfromtimestamp(mtime).strftime(
                    "%Y-%m-%d %H:%M:%S UTC"
                )
                age = time.time() - mtime
                info["age_seconds"] = int(age)
                if age > STALE_OUTPUT_HOURS * 3600:
                    info["stale"] = True
            except (ValueError, OSError):
                pass
    return info


def collect_mcmc_convergence(host, port, status_file, timeout):
    """Read ess_eta_latest.txt (or similar convergence status file)."""
    info = {"raw": "", "available": False}
    if not status_file:
        return info

    ok, out, _ = ssh_command(host, port, "cat %s 2>/dev/null" % status_file, timeout)
    if ok and out:
        info["raw"] = out
        info["available"] = True
    return info


def collect_chain_count(host, port, chains_dir, timeout):
    """Count .txt chain files under the chains directory."""
    info = {"chain_files": 0, "chain_dirs": []}
    if not chains_dir:
        return info

    ok, out, _ = ssh_command(
        host, port,
        "find %s -name '*.txt' -type f 2>/dev/null | wc -l" % chains_dir,
        timeout,
    )
    if ok and out:
        try:
            info["chain_files"] = int(out.strip())
        except ValueError:
            pass

    ok, out, _ = ssh_command(
        host, port,
        "ls -d %s/*/ 2>/dev/null | head -20" % chains_dir,
        timeout,
    )
    if ok and out:
        info["chain_dirs"] = [os.path.basename(d.rstrip("/")) for d in out.splitlines() if d.strip()]

    return info


def collect_paper2_outputs(host, port, working_dir, timeout):
    """Check for Paper 2 specific outputs."""
    info = {"dirs_found": [], "model_pt": False, "scripts": 0, "markdown_docs": 0}
    for subdir in ["runs", "figures", "outputs"]:
        path = "%s/%s" % (working_dir, subdir)
        ok, out, _ = ssh_command(host, port, "test -d %s && echo yes || echo no" % path, timeout)
        if ok and out.strip() == "yes":
            info["dirs_found"].append(subdir)

    ok, out, _ = ssh_command(
        host, port,
        "test -f %s/model.pt && echo yes || echo no" % working_dir,
        timeout,
    )
    if ok and out.strip() == "yes":
        info["model_pt"] = True

    ok, out, _ = ssh_command(
        host, port,
        "find %s -maxdepth 2 -name '*.py' -type f 2>/dev/null | wc -l" % working_dir,
        timeout,
    )
    if ok:
        try:
            info["scripts"] = int(out.strip())
        except ValueError:
            pass

    ok, out, _ = ssh_command(
        host, port,
        "find %s -maxdepth 2 -name '*.md' -type f 2>/dev/null | wc -l" % working_dir,
        timeout,
    )
    if ok:
        try:
            info["markdown_docs"] = int(out.strip())
        except ValueError:
            pass

    return info


def collect_backup_status(host, port, pod, timeout):
    """Check if freeze/backup loop is alive via PIDs from registry."""
    info = {"freeze_alive": False, "monitor_alive": False}

    freeze_pid = pod.get("freeze_loop_pid")
    if freeze_pid:
        ok, out, _ = ssh_command(
            host, port,
            "kill -0 %s 2>/dev/null && echo alive || echo dead" % str(freeze_pid),
            timeout,
        )
        if ok and out.strip() == "alive":
            info["freeze_alive"] = True

    monitor_pid = pod.get("monitor_pid")
    if monitor_pid:
        ok, out, _ = ssh_command(
            host, port,
            "kill -0 %s 2>/dev/null && echo alive || echo dead" % str(monitor_pid),
            timeout,
        )
        if ok and out.strip() == "alive":
            info["monitor_alive"] = True

    return info


def check_manifest(host, port, working_dir, timeout):
    """Check if MANIFEST.md exists."""
    ok, out, _ = ssh_command(
        host, port,
        "test -f %s/MANIFEST.md && echo yes || echo no" % working_dir,
        timeout,
    )
    return ok and out.strip() == "yes"


# ---------------------------------------------------------------------------
# Warning generation
# ---------------------------------------------------------------------------

def generate_warnings(pod_name, alive, disk, output_ts, has_manifest, track):
    """Return a list of (severity, message) tuples."""
    warnings = []

    if not alive:
        warnings.append(("CRITICAL", "%s is UNREACHABLE" % pod_name))
        return warnings  # nothing else to check

    if disk.get("percent_used") is not None and disk["percent_used"] >= DISK_WARN_PERCENT:
        warnings.append((
            "HIGH",
            "%s disk at %d%% (%s used of %s)" % (
                pod_name, disk["percent_used"], disk["used"], disk["total"]
            ),
        ))

    if output_ts.get("stale"):
        age_hr = output_ts.get("age_seconds", 0) / 3600.0
        warnings.append((
            "MEDIUM",
            "%s outputs stale (%.1f hours old)" % (pod_name, age_hr),
        ))

    if not has_manifest:
        warnings.append((
            "LOW",
            "%s missing MANIFEST.md" % pod_name,
        ))

    return warnings


def generate_recommendations(all_warnings, all_results):
    """Return a list of recommended action strings."""
    recs = []
    for w_sev, w_msg in all_warnings:
        if w_sev == "CRITICAL" and "UNREACHABLE" in w_msg:
            pod = w_msg.split(" ")[0]
            recs.append("Check pod %s — may need restart via RunPod dashboard" % pod)
        elif w_sev == "HIGH" and "disk" in w_msg:
            pod = w_msg.split(" ")[0]
            recs.append("Free disk space on %s — archive old chains or increase volume" % pod)
        elif "stale" in w_msg:
            pod = w_msg.split(" ")[0]
            recs.append("Investigate stale outputs on %s — process may have crashed" % pod)

    # Check for converged chains
    for res in all_results:
        conv = res.get("mcmc_convergence", {})
        if conv.get("available") and "R-1" in conv.get("raw", ""):
            raw = conv["raw"]
            # Try to detect good convergence
            if "R-1 < 0.01" in raw or "CONVERGED" in raw.upper():
                recs.append(
                    "MCMC on %s may be converged — review and archive" % res["pod_name"]
                )

    if not recs:
        recs.append("No immediate actions required")

    return recs


# ---------------------------------------------------------------------------
# Main collection loop
# ---------------------------------------------------------------------------

def collect_pod_status(pod, timeout):
    """Collect all status info for a single pod. Returns a dict."""
    pod_name = pod.get("pod_name", "unknown")
    host = pod.get("ssh_host")
    port = pod.get("ssh_port")
    working_dir = pod.get("working_dir", "/workspace")
    expected_outputs = pod.get("expected_outputs")
    status_file = pod.get("status_file")
    track = pod.get("track_name", "")
    ssh_str = pod.get("ssh")

    result = {
        "pod_name": pod_name,
        "track_name": track,
        "purpose": pod.get("purpose", ""),
        "pod_id": pod.get("pod_id", ""),
        "hardware": pod.get("hardware", ""),
        "tags": pod.get("tags", []),
        "alive": False,
        "ssh_configured": bool(ssh_str),
        "processes": {},
        "disk": {},
        "memory": {},
        "gpu": {},
        "output_timestamps": {},
        "mcmc_convergence": {},
        "chain_count": {},
        "paper2_outputs": {},
        "backup_status": {},
        "has_manifest": False,
        "warnings": [],
        "collected_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    }

    if not ssh_str or not host or not port:
        result["warnings"] = [("CRITICAL", "%s — SSH not configured (pending boot)" % pod_name)]
        return result

    # Alive check
    print("  Checking %s (%s:%s) ..." % (pod_name, host, port))
    alive = ssh_alive(host, port, timeout=timeout)
    result["alive"] = alive

    if not alive:
        result["warnings"] = [("CRITICAL", "%s is UNREACHABLE" % pod_name)]
        return result

    # Collect all metrics
    result["processes"] = collect_process_info(host, port, timeout)
    result["disk"] = collect_disk_usage(host, port, working_dir, timeout)
    result["memory"] = collect_memory_usage(host, port, timeout)
    result["gpu"] = collect_gpu_info(host, port, timeout)
    result["output_timestamps"] = collect_latest_output_timestamps(
        host, port, expected_outputs, timeout
    )
    result["has_manifest"] = check_manifest(host, port, working_dir, timeout)
    result["backup_status"] = collect_backup_status(host, port, pod, timeout)

    # Track-specific collection
    if "paper1" in track or "mcmc" in (pod.get("tags") or []):
        chains_dir = expected_outputs if expected_outputs else "%s/chains" % working_dir
        result["chain_count"] = collect_chain_count(host, port, chains_dir, timeout)
        result["mcmc_convergence"] = collect_mcmc_convergence(host, port, status_file, timeout)
    elif "paper2" in track:
        result["paper2_outputs"] = collect_paper2_outputs(host, port, working_dir, timeout)

    # Generate warnings
    result["warnings"] = generate_warnings(
        pod_name, alive, result["disk"], result["output_timestamps"],
        result["has_manifest"], track,
    )

    return result


# ---------------------------------------------------------------------------
# Terminal dashboard rendering
# ---------------------------------------------------------------------------

def fmt_severity(sev):
    """Color a severity label."""
    if sev == "CRITICAL":
        return RED + sev + RESET
    elif sev == "HIGH":
        return YELLOW + sev + RESET
    elif sev == "MEDIUM":
        return YELLOW + sev + RESET
    return sev


def render_pod_summary(result):
    """One-line summary for the pod status table."""
    name = result["pod_name"]
    alive = result["alive"]
    ssh_ok = result["ssh_configured"]

    if not ssh_ok:
        status = YELLOW + "PENDING" + RESET
    elif alive:
        status = GREEN + "ALIVE" + RESET
    else:
        status = RED + "DOWN" + RESET

    procs = result.get("processes", {})
    cobaya = procs.get("cobaya_count", "-")
    python = procs.get("python_count", "-")

    disk = result.get("disk", {})
    disk_pct = disk.get("percent_used")
    disk_str = "%d%%" % disk_pct if disk_pct is not None else "-"

    mem = result.get("memory", {})
    mem_used = mem.get("used_mb")
    mem_total = mem.get("total_mb")
    if mem_used is not None and mem_total is not None:
        mem_str = "%dMB/%dMB" % (mem_used, mem_total)
    else:
        mem_str = "-"

    gpu = result.get("gpu", {})
    if gpu.get("available"):
        gpu_str = "%d%% / %dMB" % (
            gpu.get("util_percent", 0),
            gpu.get("mem_used_mb", 0),
        )
    else:
        gpu_str = "n/a"

    return "  %-30s  %s  cob=%-3s py=%-3s  disk=%-5s  mem=%-16s  gpu=%s" % (
        name, status, cobaya, python, disk_str, mem_str, gpu_str,
    )


def render_mcmc_section(results):
    """Render Paper 1 MCMC details."""
    lines = []
    mcmc_pods = [r for r in results if "paper1" in r.get("track_name", "")]
    if not mcmc_pods:
        lines.append("  No Paper 1 MCMC pods found.")
        return "\n".join(lines)

    for r in mcmc_pods:
        lines.append("  %s%s%s (%s)" % (BOLD, r["pod_name"], RESET, r["hardware"]))
        chains = r.get("chain_count", {})
        lines.append("    Chain files: %d   Dirs: %s" % (
            chains.get("chain_files", 0),
            ", ".join(chains.get("chain_dirs", [])) or "none",
        ))
        conv = r.get("mcmc_convergence", {})
        if conv.get("available"):
            # Show first 5 lines of convergence status
            raw_lines = conv["raw"].splitlines()[:8]
            for cl in raw_lines:
                lines.append("    | %s" % cl)
        else:
            lines.append("    Convergence status: not available")
        bk = r.get("backup_status", {})
        lines.append("    Freeze loop: %s   Monitor: %s" % (
            GREEN + "alive" + RESET if bk.get("freeze_alive") else RED + "dead/unknown" + RESET,
            GREEN + "alive" + RESET if bk.get("monitor_alive") else RED + "dead/unknown" + RESET,
        ))
        ts = r.get("output_timestamps", {})
        if ts.get("newest_mtime"):
            age_hr = ts.get("age_seconds", 0) / 3600.0
            lines.append("    Latest output: %s (%.1fh ago)" % (ts["newest_mtime"], age_hr))
        lines.append("")
    return "\n".join(lines)


def render_paper2_section(results):
    """Render Paper 2 track details."""
    lines = []
    p2_pods = [r for r in results if "paper2" in r.get("track_name", "")]
    if not p2_pods:
        lines.append("  No Paper 2 pods found.")
        return "\n".join(lines)

    for r in p2_pods:
        name = r["pod_name"]
        alive = r["alive"]
        ssh_ok = r["ssh_configured"]

        if not ssh_ok:
            status_str = YELLOW + "PENDING BOOT" + RESET
        elif alive:
            status_str = GREEN + "ALIVE" + RESET
        else:
            status_str = RED + "DOWN" + RESET

        lines.append("  %s%s%s — %s — %s" % (BOLD, name, RESET, status_str, r.get("purpose", "")))

        if alive:
            p2 = r.get("paper2_outputs", {})
            lines.append("    Dirs: %s   model.pt: %s   Scripts: %d   Docs: %d" % (
                ", ".join(p2.get("dirs_found", [])) or "none",
                "yes" if p2.get("model_pt") else "no",
                p2.get("scripts", 0),
                p2.get("markdown_docs", 0),
            ))
            ts = r.get("output_timestamps", {})
            if ts.get("newest_mtime"):
                age_hr = ts.get("age_seconds", 0) / 3600.0
                lines.append("    Latest output: %s (%.1fh ago)" % (ts["newest_mtime"], age_hr))
        lines.append("")
    return "\n".join(lines)


def render_dashboard(results, all_warnings, recommendations, elapsed):
    """Print the full terminal dashboard."""
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    alive_count = sum(1 for r in results if r["alive"])
    total_count = len(results)
    pending_count = sum(1 for r in results if not r["ssh_configured"])

    lines = []
    lines.append("")
    lines.append(SEP)
    lines.append(
        "%s  BIGBOUNCE GLOBAL STATUS DASHBOARD%s  %s" % (BOLD + CYAN, RESET, now)
    )
    lines.append(
        "  Pods: %d/%d alive   %d pending boot   Scan took %.1fs"
        % (alive_count, total_count, pending_count, elapsed)
    )
    lines.append(SEP)

    # Pod Status Table
    lines.append("")
    lines.append("%s  POD STATUS%s" % (BOLD, RESET))
    lines.append("  %-30s  %-8s  %-10s  %-6s  %-17s  %s" % (
        "NAME", "STATUS", "PROCESSES", "DISK", "MEMORY", "GPU",
    ))
    lines.append("  " + "-" * 76)
    for r in results:
        lines.append(render_pod_summary(r))

    # Paper 1 MCMC
    lines.append("")
    lines.append(SEP)
    lines.append("%s  PAPER 1 — MCMC CONVERGENCE%s" % (BOLD, RESET))
    lines.append(render_mcmc_section(results))

    # Paper 2 Tracks
    lines.append(SEP)
    lines.append("%s  PAPER 2 — RESEARCH TRACKS%s" % (BOLD, RESET))
    lines.append(render_paper2_section(results))

    # Warnings
    lines.append(SEP)
    lines.append("%s  WARNINGS%s" % (BOLD, RESET))
    if all_warnings:
        for sev, msg in sorted(all_warnings, key=lambda w: {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}.get(w[0], 4)):
            lines.append("  [%s] %s" % (fmt_severity(sev), msg))
    else:
        lines.append("  " + GREEN + "No warnings." + RESET)

    # Recommended Actions
    lines.append("")
    lines.append(SEP)
    lines.append("%s  RECOMMENDED ACTIONS%s" % (BOLD, RESET))
    for i, rec in enumerate(recommendations, 1):
        lines.append("  %d. %s" % (i, rec))

    lines.append("")
    lines.append(SEP)

    dashboard = "\n".join(lines)
    print(dashboard)
    return dashboard


# ---------------------------------------------------------------------------
# File output
# ---------------------------------------------------------------------------

def strip_ansi(text):
    """Remove ANSI escape codes for file output."""
    import re
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)


def save_outputs(results, all_warnings, recommendations, dashboard_text, elapsed):
    """Save to latest txt/json and history."""
    now = datetime.datetime.utcnow()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    # Ensure history dir
    if not os.path.isdir(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

    # Build JSON-serializable version (warnings are tuples)
    json_results = []
    for r in results:
        jr = dict(r)
        jr["warnings"] = [{"severity": w[0], "message": w[1]} for w in r["warnings"]]
        json_results.append(jr)

    json_payload = {
        "collected_at": now.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scan_duration_seconds": round(elapsed, 1),
        "pod_count": len(results),
        "alive_count": sum(1 for r in results if r["alive"]),
        "pending_count": sum(1 for r in results if not r["ssh_configured"]),
        "warnings": [{"severity": w[0], "message": w[1]} for w in all_warnings],
        "recommendations": recommendations,
        "pods": json_results,
    }

    # Write JSON
    with open(LATEST_JSON, "w") as f:
        json.dump(json_payload, f, indent=2, default=str)

    # Write plain text (strip ANSI)
    plain = strip_ansi(dashboard_text)
    with open(LATEST_TXT, "w") as f:
        f.write(plain)

    # History copy
    history_file = os.path.join(HISTORY_DIR, "%s.txt" % timestamp)
    with open(history_file, "w") as f:
        f.write(plain)

    print("\nOutputs saved:")
    print("  %s" % LATEST_TXT)
    print("  %s" % LATEST_JSON)
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
        description="BigBounce Global Status Monitor — SSH into all pods and report status."
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
        "--json-only",
        action="store_true",
        help="Only output JSON, skip terminal dashboard",
    )
    parser.add_argument(
        "--pod",
        type=str,
        default=None,
        help="Check only this specific pod (by pod_name)",
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

    print("%sBigBounce Global Status Monitor%s" % (BOLD, RESET))
    print("Scanning %d pods (timeout=%ds)...\n" % (len(pods), args.timeout))

    start_time = time.time()
    results = []
    all_warnings = []

    for pod in pods:
        try:
            result = collect_pod_status(pod, args.timeout)
            results.append(result)
            all_warnings.extend(result["warnings"])
        except Exception as exc:
            pod_name = pod.get("pod_name", "unknown")
            print("  ERROR collecting %s: %s" % (pod_name, str(exc)))
            traceback.print_exc()
            results.append({
                "pod_name": pod_name,
                "track_name": pod.get("track_name", ""),
                "alive": False,
                "ssh_configured": bool(pod.get("ssh")),
                "warnings": [("CRITICAL", "%s collection failed: %s" % (pod_name, str(exc)))],
                "collected_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            })
            all_warnings.append(
                ("CRITICAL", "%s collection failed: %s" % (pod_name, str(exc)))
            )

    elapsed = time.time() - start_time

    recommendations = generate_recommendations(all_warnings, results)

    if args.json_only:
        # Just dump JSON to stdout
        json_results = []
        for r in results:
            jr = dict(r)
            jr["warnings"] = [{"severity": w[0], "message": w[1]} for w in r.get("warnings", [])]
            json_results.append(jr)
        json.dump({
            "pods": json_results,
            "warnings": [{"severity": w[0], "message": w[1]} for w in all_warnings],
            "recommendations": recommendations,
        }, sys.stdout, indent=2, default=str)
        print()
    else:
        dashboard_text = render_dashboard(results, all_warnings, recommendations, elapsed)
        save_outputs(results, all_warnings, recommendations, dashboard_text, elapsed)

    # Exit code: 1 if any CRITICAL warnings
    critical_count = sum(1 for sev, _ in all_warnings if sev == "CRITICAL")
    if critical_count:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
