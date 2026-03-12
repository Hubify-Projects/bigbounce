#!/usr/bin/env python3
"""
BigBounce Global Monitor — Python Wrapper
============================================
Runs all three monitor scripts in order:
  1. global_status.py
  2. global_backup.py
  3. global_artifact_index.py

Saves combined output to logs/TIMESTAMP.log

Usage:
  python3 run_all_monitors.py [--timeout 10] [--dry-run] [--pod POD_NAME]
"""

import argparse
import datetime
import os
import subprocess
import sys
import time


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, "logs")

SCRIPTS = [
    ("Global Status", "global_status.py"),
    ("GPU Freeze Manager", "gpu_freeze_manager.py"),
    ("Global Backup", "global_backup.py"),
    ("Artifact Index", "global_artifact_index.py"),
]

BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
SEP = "=" * 78


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_script(script_path, extra_args, log_fh):
    """
    Run a Python script, streaming output to stdout and the log file.
    Returns the exit code.
    """
    cmd = [sys.executable, script_path] + extra_args

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    for line in proc.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
        log_fh.write(line)

    proc.wait()
    return proc.returncode


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="BigBounce Global Monitor — run all monitor scripts in sequence."
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
        help="Pass --dry-run to backup script",
    )
    parser.add_argument(
        "--pod",
        type=str,
        default=None,
        help="Monitor only this specific pod (by pod_name)",
    )
    parser.add_argument(
        "--registry",
        type=str,
        default=None,
        help="Path to pod_registry.yaml",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Build extra args to forward
    extra_args = []
    if args.timeout != 10:
        extra_args.extend(["--timeout", str(args.timeout)])
    if args.dry_run:
        extra_args.append("--dry-run")
    if args.pod:
        extra_args.extend(["--pod", args.pod])
    if args.registry:
        extra_args.extend(["--registry", args.registry])

    # Setup log directory
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOG_DIR, "%s.log" % timestamp)

    now_str = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    print("%s%s%s" % (BOLD + CYAN, SEP, RESET))
    print("%s  BIGBOUNCE GLOBAL MONITOR -- FULL SCAN%s" % (BOLD + CYAN, RESET))
    print("%s  %s%s" % (BOLD + CYAN, now_str, RESET))
    print("%s%s%s" % (BOLD + CYAN, SEP, RESET))
    print("")

    start_time = time.time()
    exit_codes = {}

    with open(log_file, "w") as log_fh:
        log_fh.write("BigBounce Global Monitor Run\n")
        log_fh.write("Started: %s\n" % now_str)
        log_fh.write("%s\n\n" % SEP)

        for i, (label, script_name) in enumerate(SCRIPTS, 1):
            script_path = os.path.join(SCRIPT_DIR, script_name)

            if not os.path.isfile(script_path):
                print("%s[%d/%d] %s -- MISSING: %s%s" % (
                    RED, i, len(SCRIPTS), label, script_path, RESET,
                ))
                exit_codes[label] = -1
                continue

            print("%s[%d/%d] Running %s ...%s\n" % (BOLD, i, len(SCRIPTS), label, RESET))
            log_fh.write("\n[%d/%d] %s\n%s\n" % (i, len(SCRIPTS), label, "-" * 40))

            ec = run_script(script_path, extra_args, log_fh)
            exit_codes[label] = ec

            if ec == 0:
                print("\n  %s%s completed successfully.%s\n" % (GREEN, label, RESET))
            else:
                print("\n  %s%s completed with issues (exit %d).%s\n" % (YELLOW, label, ec, RESET))

    elapsed = time.time() - start_time

    # Summary
    print("%s%s%s" % (BOLD + CYAN, SEP, RESET))
    print("%s  MONITOR RUN COMPLETE%s" % (BOLD + CYAN, RESET))
    print("%s%s%s" % (BOLD + CYAN, SEP, RESET))
    print("")
    print("  Duration: %.1fs" % elapsed)
    for label, ec in exit_codes.items():
        color = GREEN if ec == 0 else (YELLOW if ec == 1 else RED)
        print("  %-20s %sexit %d%s" % (label + ":", color, ec, RESET))
    print("  Log file: %s" % log_file)
    print("")

    # List output files
    output_files = [
        os.path.join(SCRIPT_DIR, "global_status_latest.txt"),
        os.path.join(SCRIPT_DIR, "global_status_latest.json"),
        os.path.join(SCRIPT_DIR, "global_backup_latest.txt"),
        os.path.join(SCRIPT_DIR, "artifact_index.csv"),
        os.path.join(SCRIPT_DIR, "artifact_index_latest.txt"),
    ]

    print("%sOutput files:%s" % (BOLD, RESET))
    for f in output_files:
        if os.path.isfile(f):
            size = os.path.getsize(f)
            if size >= 1024 * 1024:
                size_str = "%.1f MB" % (size / 1024.0 / 1024.0)
            elif size >= 1024:
                size_str = "%.1f KB" % (size / 1024.0)
            else:
                size_str = "%d B" % size
            print("  %s[OK]%s  %s  (%s)" % (GREEN, RESET, f, size_str))
        else:
            print("  %s[--]%s  %s  (not created)" % (YELLOW, RESET, f))
    print("")

    # Overall exit
    overall = 0
    for ec in exit_codes.values():
        if ec != 0:
            overall = 1
            break

    return overall


if __name__ == "__main__":
    sys.exit(main())
