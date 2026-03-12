#!/usr/bin/env python3
"""
BigBounce Global Artifact Index
==================================
Scan all pods for frozen/reproducible artifacts (frozen_packs/,
MANIFEST.md, CHECKSUMS.txt, summary.json) and build a CSV index.

Outputs:
  - artifact_index.csv
  - artifact_index_latest.txt

Usage:
  python3 global_artifact_index.py [--registry pod_registry.yaml] [--timeout 10]
"""

import argparse
import csv
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
CSV_FILE = os.path.join(SCRIPT_DIR, "artifact_index.csv")
LATEST_TXT = os.path.join(SCRIPT_DIR, "artifact_index_latest.txt")

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

# Artifact search locations (relative to working_dir)
ARTIFACT_SEARCH_DIRS = [
    "frozen_packs",
    "runs",
    "outputs",
    "backups",
]

# Key artifact files to look for within each found directory
ARTIFACT_MARKERS = [
    "MANIFEST.md",
    "CHECKSUMS.txt",
    "summary.json",
    "metadata.json",
    "README.md",
]


# ---------------------------------------------------------------------------
# SSH helpers
# ---------------------------------------------------------------------------

def ssh_command(host, port, cmd, timeout=10):
    """Run a command over SSH. Returns (success, stdout, stderr)."""
    if not host or not port:
        return False, "", "No SSH credentials"

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
            timeout=timeout + 15,
        )
        return proc.returncode == 0, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "", "SSH timeout"
    except Exception as exc:
        return False, "", "SSH error: %s" % str(exc)


def ssh_alive(host, port, timeout=10):
    """Quick alive check."""
    ok, out, _ = ssh_command(host, port, "echo ok", timeout=timeout)
    return ok and out.strip() == "ok"


# ---------------------------------------------------------------------------
# Artifact scanning
# ---------------------------------------------------------------------------

def find_artifact_dirs(host, port, working_dir, timeout):
    """
    Find directories that look like frozen artifacts or run outputs.
    Returns list of absolute paths on the pod.
    """
    dirs_found = []

    for search_dir in ARTIFACT_SEARCH_DIRS:
        full_path = "%s/%s" % (working_dir, search_dir)

        # Check if directory exists
        ok, out, _ = ssh_command(
            host, port,
            "test -d %s && echo yes || echo no" % full_path,
            timeout,
        )
        if not ok or out.strip() != "yes":
            continue

        # List subdirectories (each could be a separate artifact/run)
        ok, out, _ = ssh_command(
            host, port,
            "find %s -maxdepth 1 -mindepth 1 -type d 2>/dev/null | sort" % full_path,
            timeout,
        )
        if ok and out.strip():
            for d in out.splitlines():
                d = d.strip()
                if d:
                    dirs_found.append(d)

        # Also treat the directory itself as a potential artifact location
        dirs_found.append(full_path)

    return dirs_found


def scan_artifact(host, port, artifact_path, timeout):
    """
    Scan a single artifact directory for markers and metadata.
    Returns a dict describing the artifact.
    """
    info = {
        "path": artifact_path,
        "run_id": os.path.basename(artifact_path),
        "has_manifest": False,
        "has_checksums": False,
        "has_summary": False,
        "has_metadata": False,
        "timestamp": "",
        "size_bytes": 0,
        "size_human": "",
        "file_count": 0,
        "key_deliverables": [],
        "status": "unknown",
        "type": "unknown",
    }

    # Check marker files
    for marker in ARTIFACT_MARKERS:
        marker_path = "%s/%s" % (artifact_path, marker)
        ok, out, _ = ssh_command(
            host, port,
            "test -f %s && echo yes || echo no" % marker_path,
            timeout,
        )
        if ok and out.strip() == "yes":
            key = "has_%s" % marker.split(".")[0].lower()
            if key in info:
                info[key] = True

    # Get total size
    ok, out, _ = ssh_command(
        host, port,
        "du -sb %s 2>/dev/null | awk '{print $1}'" % artifact_path,
        timeout,
    )
    if ok and out.strip():
        try:
            info["size_bytes"] = int(out.strip())
        except ValueError:
            pass

    # Get file count
    ok, out, _ = ssh_command(
        host, port,
        "find %s -type f 2>/dev/null | wc -l" % artifact_path,
        timeout,
    )
    if ok and out.strip():
        try:
            info["file_count"] = int(out.strip())
        except ValueError:
            pass

    # Get newest file timestamp
    ok, out, _ = ssh_command(
        host, port,
        "find %s -type f -printf '%%T@ %%p\\n' 2>/dev/null | sort -rn | head -1" % artifact_path,
        timeout,
    )
    if ok and out.strip():
        parts = out.split(None, 1)
        if len(parts) >= 1:
            try:
                mtime = float(parts[0])
                info["timestamp"] = datetime.datetime.utcfromtimestamp(mtime).strftime(
                    "%Y-%m-%d %H:%M:%S UTC"
                )
            except (ValueError, OSError):
                pass

    # Identify key deliverables (notable file types)
    ok, out, _ = ssh_command(
        host, port,
        "find %s -maxdepth 2 -type f \\( -name '*.tar.gz' -o -name '*.pdf' -o -name '*.png' -o -name '*.csv' -o -name '*.pt' -o -name '*.json' -o -name '*.txt' \\) 2>/dev/null | head -20" % artifact_path,
        timeout,
    )
    if ok and out.strip():
        info["key_deliverables"] = [os.path.basename(f) for f in out.splitlines() if f.strip()]

    # Try to read checksums file content for the index
    info["checksums_content"] = ""
    if info["has_checksums"]:
        ok, out, _ = ssh_command(
            host, port,
            "head -5 %s/CHECKSUMS.txt 2>/dev/null" % artifact_path,
            timeout,
        )
        if ok:
            info["checksums_content"] = out.replace("\n", " | ")

    # Determine artifact type
    if "frozen_packs" in artifact_path:
        info["type"] = "frozen_pack"
        info["status"] = "frozen"
    elif "runs" in artifact_path:
        info["type"] = "run_output"
        info["status"] = "complete" if info["has_summary"] or info["has_manifest"] else "partial"
    elif "outputs" in artifact_path:
        info["type"] = "output"
        info["status"] = "complete" if info["file_count"] > 0 else "empty"
    elif "backups" in artifact_path:
        info["type"] = "backup"
        info["status"] = "archived"

    # Human-readable size
    info["size_human"] = format_size(info["size_bytes"])

    return info


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
# Index building
# ---------------------------------------------------------------------------

def scan_pod(pod, timeout):
    """Scan a single pod for all artifacts. Returns list of artifact dicts."""
    pod_name = pod.get("pod_name", "unknown")
    host = pod.get("ssh_host")
    port = pod.get("ssh_port")
    working_dir = pod.get("working_dir", "/workspace")
    track = pod.get("track_name", "")
    ssh_str = pod.get("ssh")

    if not ssh_str or not host or not port:
        print("  %-30s %sSKIPPED%s (no SSH)" % (pod_name, YELLOW, RESET))
        return []

    print("  %-30s scanning..." % pod_name, end="", flush=True)

    if not ssh_alive(host, port, timeout=timeout):
        print("\r  %-30s %sUNREACHABLE%s" % (pod_name, RED, RESET))
        return []

    # Find artifact directories
    artifact_dirs = find_artifact_dirs(host, port, working_dir, timeout)

    if not artifact_dirs:
        print("\r  %-30s %sNO ARTIFACTS%s" % (pod_name, YELLOW, RESET))
        return []

    # Scan each directory
    artifacts = []
    for adir in artifact_dirs:
        art = scan_artifact(host, port, adir, timeout)
        art["pod_name"] = pod_name
        art["track_name"] = track
        # Only include if it has files
        if art["file_count"] > 0:
            artifacts.append(art)

    print("\r  %-30s %s%d artifacts%s" % (pod_name, GREEN, len(artifacts), RESET))
    return artifacts


def write_csv(all_artifacts):
    """Write artifact_index.csv."""
    fieldnames = [
        "track", "pod", "run_id", "path", "timestamp", "status",
        "checksums", "manifest", "key_deliverables", "size", "type",
        "file_count",
    ]

    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for art in all_artifacts:
            writer.writerow({
                "track": art.get("track_name", ""),
                "pod": art.get("pod_name", ""),
                "run_id": art.get("run_id", ""),
                "path": art.get("path", ""),
                "timestamp": art.get("timestamp", ""),
                "status": art.get("status", ""),
                "checksums": "yes" if art.get("has_checksums") else "no",
                "manifest": "yes" if art.get("has_manifest") else "no",
                "key_deliverables": "; ".join(art.get("key_deliverables", [])),
                "size": art.get("size_human", ""),
                "type": art.get("type", ""),
                "file_count": art.get("file_count", 0),
            })

    print("\nCSV index written: %s (%d rows)" % (CSV_FILE, len(all_artifacts)))


def write_txt_report(all_artifacts, elapsed):
    """Write artifact_index_latest.txt."""
    lines = []
    lines.append("BigBounce Global Artifact Index")
    lines.append("Generated: %s UTC" % datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("Duration: %.1fs" % elapsed)
    lines.append("Total artifacts: %d" % len(all_artifacts))
    lines.append("=" * 78)
    lines.append("")

    # Group by track
    tracks = {}
    for art in all_artifacts:
        track = art.get("track_name", "unknown")
        if track not in tracks:
            tracks[track] = []
        tracks[track].append(art)

    for track, arts in sorted(tracks.items()):
        lines.append("TRACK: %s (%d artifacts)" % (track, len(arts)))
        lines.append("-" * 40)
        for art in arts:
            lines.append("  [%s] %s" % (art["type"], art["run_id"]))
            lines.append("    Pod: %s" % art["pod_name"])
            lines.append("    Path: %s" % art["path"])
            lines.append("    Status: %s   Size: %s   Files: %d" % (
                art["status"], art["size_human"], art["file_count"],
            ))
            lines.append("    Timestamp: %s" % art.get("timestamp", "unknown"))
            lines.append("    Manifest: %s   Checksums: %s" % (
                "yes" if art.get("has_manifest") else "no",
                "yes" if art.get("has_checksums") else "no",
            ))
            deliverables = art.get("key_deliverables", [])
            if deliverables:
                lines.append("    Deliverables: %s" % ", ".join(deliverables[:10]))
            lines.append("")
        lines.append("")

    # Summary
    lines.append("=" * 78)
    total_size = sum(art.get("size_bytes", 0) for art in all_artifacts)
    frozen = sum(1 for art in all_artifacts if art.get("type") == "frozen_pack")
    runs = sum(1 for art in all_artifacts if art.get("type") == "run_output")
    lines.append("Summary: %d frozen packs, %d run outputs, total size %s" % (
        frozen, runs, format_size(total_size),
    ))

    report = "\n".join(lines)
    with open(LATEST_TXT, "w") as f:
        f.write(report)

    print("Text report written: %s" % LATEST_TXT)


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
        description="BigBounce Global Artifact Index — scan pods for frozen/reproducible artifacts."
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
        "--pod",
        type=str,
        default=None,
        help="Scan only this specific pod (by pod_name)",
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

    print("%sBigBounce Global Artifact Index%s" % (BOLD, RESET))
    print("Scanning %d pods for artifacts (timeout=%ds)...\n" % (len(pods), args.timeout))

    start_time = time.time()
    all_artifacts = []

    for pod in pods:
        try:
            artifacts = scan_pod(pod, args.timeout)
            all_artifacts.extend(artifacts)
        except Exception as exc:
            pod_name = pod.get("pod_name", "unknown")
            print("  %-30s %sERROR%s %s" % (pod_name, RED, RESET, str(exc)))

    elapsed = time.time() - start_time

    print("\n%s" % SEP)
    print("%sArtifact scan complete:%s %d artifacts found across %d pods (%.1fs)" % (
        BOLD, RESET, len(all_artifacts), len(pods), elapsed,
    ))

    # Write outputs
    write_csv(all_artifacts)
    write_txt_report(all_artifacts, elapsed)

    return 0


if __name__ == "__main__":
    sys.exit(main())
