#!/usr/bin/env python3
"""
BigBounce GPU Freeze Manager — Convergence-Only Freeze Logic
==============================================================
Replaces the old 48-hour time-cap freeze logic. Chains are NEVER stopped
or frozen based on elapsed time. Freezing occurs ONLY when convergence
criteria are satisfied on cohort_main (chains 2-7).

RULES:
  - NEVER stop, restart, or interrupt active Cobaya chains
  - NEVER freeze based solely on time
  - Freezing only via convergence thresholds or manual command

Convergence criteria (cohort_main, chains 2-7):
  R-hat-1 < 0.01 for H0 and delta_neff
  R-hat-1 < 0.02 for tau
  ESS >= 2000 for H0 and delta_neff
  ESS >= 1000 for tau
  drift < 0.2 sigma for H0 and delta_neff

On convergence, creates:
  A) Science freeze pack (chains 2-7 only)
  B) Full archival pack (chains 1-7, chain 1 excluded from science)

Periodic safety snapshots every 6 hours (regardless of convergence).
Hourly monitoring and backups continue indefinitely after convergence.

Outputs:
  - project_status_latest.txt
  - project_status_latest.json

Usage:
  python3 gpu_freeze_manager.py [--registry pod_registry.yaml] [--timeout 10]
                                [--dry-run] [--force-freeze DATASET]
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time

import yaml


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REGISTRY = os.path.join(SCRIPT_DIR, "pod_registry.yaml")
STATUS_TXT = os.path.join(SCRIPT_DIR, "project_status_latest.txt")
STATUS_JSON = os.path.join(SCRIPT_DIR, "project_status_latest.json")

SSH_KEY = os.path.expanduser("~/.ssh/id_ed25519")
SSH_BASE_OPTS = [
    "-i", SSH_KEY,
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "LogLevel=ERROR",
]

DATASETS = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]

# Science freeze criteria — cohort_main (chains 2-7)
CONVERGENCE_CRITERIA = {
    "rhat_m1": {
        "H0": 0.01,
        "delta_neff": 0.01,
        "tau": 0.02,
    },
    "ess": {
        "H0": 2000,
        "delta_neff": 2000,
        "tau": 1000,
    },
    "drift_max": 0.2,  # sigma, for H0 and delta_neff
}

SAFETY_SNAPSHOT_INTERVAL_H = 6

# Terminal formatting
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
            full_cmd, capture_output=True, text=True,
            timeout=timeout + 30,
        )
        return proc.returncode == 0, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "", "SSH timeout after %ds" % (timeout + 30)
    except Exception as exc:
        return False, "", "SSH error: %s" % str(exc)


def ssh_alive(host, port, timeout=10):
    ok, out, _ = ssh_command(host, port, "echo ok", timeout=timeout)
    return ok and out.strip() == "ok"


# ---------------------------------------------------------------------------
# Data collection from GPU pod
# ---------------------------------------------------------------------------

def get_chain_sample_counts(host, port, chains_dir, dataset, timeout):
    """Get sample counts for each chain in a dataset."""
    counts = {}
    # Chain 1 is in chains_dir/dataset/spin_torsion.1.txt
    cmd = "wc -l %s/%s/spin_torsion.1.txt 2>/dev/null | awk '{print $1}'" % (chains_dir, dataset)
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        try:
            counts[1] = max(int(out.strip()) - 1, 0)  # subtract header
        except ValueError:
            pass

    # Chains 2-7 are in chains_dir/dataset_chain{N}/spin_torsion.1.txt
    for i in range(2, 8):
        cmd = "wc -l %s/%s_chain%d/spin_torsion.1.txt 2>/dev/null | awk '{print $1}'" % (chains_dir, dataset, i)
        ok, out, _ = ssh_command(host, port, cmd, timeout)
        if ok and out.strip():
            try:
                counts[i] = max(int(out.strip()) - 1, 0)
            except ValueError:
                pass
    return counts


def get_convergence_diagnostics(host, port, status_file, timeout):
    """Read convergence CSV from the pod."""
    info = {"available": False, "rows": []}
    if not status_file:
        return info
    ok, out, _ = ssh_command(host, port, "cat %s 2>/dev/null" % status_file, timeout)
    if ok and out.strip():
        info["available"] = True
        lines = out.strip().splitlines()
        if len(lines) > 1:
            header = lines[0].split(",")
            for line in lines[1:]:
                vals = line.split(",")
                if len(vals) >= len(header):
                    row = {}
                    for h, v in zip(header, vals):
                        h = h.strip()
                        v = v.strip()
                        try:
                            row[h] = float(v)
                        except ValueError:
                            row[h] = v
                    info["rows"].append(row)
    return info


def get_freeze_check(host, port, working_dir, timeout):
    """Read the freeze_check.txt from the pod's cosmology dir."""
    cmd = "cat %s/cosmology/freeze_check.txt 2>/dev/null" % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        return out
    # Try alternate location
    cmd = "cat %s/freeze_check.txt 2>/dev/null" % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    return out if ok else ""


def get_process_count(host, port, timeout):
    """Count cobaya processes."""
    ok, out, _ = ssh_command(host, port, "pgrep -c cobaya 2>/dev/null || echo 0", timeout)
    try:
        return int(out.strip()) if ok else 0
    except ValueError:
        return 0


def check_existing_frozen_packs(host, port, working_dir, timeout):
    """List existing frozen packs on the pod."""
    cmd = "ls -d %s/frozen_packs/frozen_gpu_* 2>/dev/null" % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        return [os.path.basename(d.strip()) for d in out.splitlines() if d.strip()]
    return []


def check_existing_snapshots(host, port, working_dir, timeout):
    """List existing safety snapshots on the pod."""
    cmd = "ls -d %s/frozen_packs/snapshot_gpu_* 2>/dev/null | sort -r | head -5" % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        return [os.path.basename(d.strip()) for d in out.splitlines() if d.strip()]
    return []


def get_latest_snapshot_age(host, port, working_dir, timeout):
    """Get the age in hours of the most recent safety snapshot."""
    cmd = (
        "ls -dt %s/frozen_packs/snapshot_gpu_* 2>/dev/null | head -1 | "
        "xargs -I{} stat -c %%Y {} 2>/dev/null"
    ) % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        try:
            mtime = float(out.strip())
            return (time.time() - mtime) / 3600.0
        except ValueError:
            pass
    return None


def get_latest_file_age(host, port, path, timeout):
    """Get age of newest file under path in hours."""
    cmd = "find %s -type f -printf '%%T@\\n' 2>/dev/null | sort -rn | head -1" % path
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if ok and out.strip():
        try:
            mtime = float(out.strip())
            return (time.time() - mtime) / 3600.0
        except ValueError:
            pass
    return None


# ---------------------------------------------------------------------------
# Convergence evaluation — cohort_main (chains 2-7)
# ---------------------------------------------------------------------------

def parse_cohort_convergence(conv_data, freeze_check_text):
    """
    Parse convergence data for cohort_main (chains 2-7).
    Returns dict keyed by dataset with convergence metrics.
    """
    results = {}

    # Parse from convergence CSV (has both all and new columns)
    for row in conv_data.get("rows", []):
        ds = row.get("dataset", "")
        param = row.get("param", "")
        if not ds or not param:
            continue
        if ds not in results:
            results[ds] = {"params": {}, "converged": False}
        results[ds]["params"][param] = {
            "rhat_m1_all": row.get("Rhat_m1_all", float("nan")),
            "rhat_m1_cohort": row.get("Rhat_m1_new", float("nan")),
            "ess_all": row.get("ESS_all", float("nan")),
            "ess_cohort": row.get("ESS_new", float("nan")),
            "drift_all": row.get("drift_all", float("nan")),
            "drift_cohort": row.get("drift_new", float("nan")),
        }

    # Also parse from freeze_check.txt for cohort_new data
    if freeze_check_text:
        current_ds = None
        current_mode = None
        for line in freeze_check_text.splitlines():
            line = line.strip()
            ds_match = re.match(r"^--- (.+) ---$", line)
            if ds_match:
                current_ds = ds_match.group(1).lower().replace(" ", "_")
                continue
            if "[cohort_new]" in line or "[cohort_main]" in line:
                current_mode = "cohort"
                continue
            if "[all_chains]" in line:
                current_mode = "all"
                continue
            if current_ds and current_mode == "cohort":
                ess_match = re.search(r"ESS\(H0\)\s*=\s*([\d.]+)\s+ESS\(.*Neff\)\s*=\s*([\d.]+)", line)
                if ess_match:
                    if current_ds not in results:
                        results[current_ds] = {"params": {}, "converged": False}
                    if "H0" not in results[current_ds]["params"]:
                        results[current_ds]["params"]["H0"] = {}
                    if "delta_neff" not in results[current_ds]["params"]:
                        results[current_ds]["params"]["delta_neff"] = {}
                    results[current_ds]["params"]["H0"]["ess_cohort"] = float(ess_match.group(1))
                    results[current_ds]["params"]["delta_neff"]["ess_cohort"] = float(ess_match.group(2))

    return results


def evaluate_convergence(dataset_metrics):
    """
    Evaluate whether a dataset meets ALL convergence criteria.
    Returns (converged: bool, details: dict).
    """
    criteria = CONVERGENCE_CRITERIA
    params = dataset_metrics.get("params", {})

    gates = {
        "rhat_H0": False,
        "rhat_nnu": False,
        "rhat_tau": False,
        "ess_H0": False,
        "ess_nnu": False,
        "ess_tau": False,
        "drift_H0": False,
        "drift_nnu": False,
    }
    values = {}

    # R-hat gates
    for param_key, gate_key in [("H0", "rhat_H0"), ("delta_neff", "rhat_nnu"), ("tau", "rhat_tau")]:
        p = params.get(param_key, {})
        rm1 = p.get("rhat_m1_cohort", float("nan"))
        target = criteria["rhat_m1"].get(param_key, 0.01)
        values[gate_key] = rm1
        try:
            if float(rm1) < target:
                gates[gate_key] = True
        except (ValueError, TypeError):
            pass

    # ESS gates
    for param_key, gate_key in [("H0", "ess_H0"), ("delta_neff", "ess_nnu"), ("tau", "ess_tau")]:
        p = params.get(param_key, {})
        ess = p.get("ess_cohort", float("nan"))
        target = criteria["ess"].get(param_key, 2000)
        values[gate_key] = ess
        try:
            if float(ess) >= target:
                gates[gate_key] = True
        except (ValueError, TypeError):
            pass

    # Drift gates
    for param_key, gate_key in [("H0", "drift_H0"), ("delta_neff", "drift_nnu")]:
        p = params.get(param_key, {})
        drift = p.get("drift_cohort", float("nan"))
        values[gate_key] = drift
        try:
            if abs(float(drift)) < criteria["drift_max"]:
                gates[gate_key] = True
        except (ValueError, TypeError):
            pass

    converged = all(gates.values())
    return converged, {"gates": gates, "values": values}


def estimate_remaining_samples(dataset_metrics):
    """
    Rough estimate of remaining samples needed to reach convergence.
    Based on current R-hat-1 and ESS trajectories.
    """
    params = dataset_metrics.get("params", {})
    estimates = {}

    for param_key in ["H0", "delta_neff", "tau"]:
        p = params.get(param_key, {})
        rm1 = p.get("rhat_m1_cohort", float("nan"))
        ess = p.get("ess_cohort", float("nan"))
        target_rm1 = CONVERGENCE_CRITERIA["rhat_m1"].get(param_key, 0.01)
        target_ess = CONVERGENCE_CRITERIA["ess"].get(param_key, 2000)

        est = {"rhat_factor": None, "ess_factor": None}
        try:
            rm1 = float(rm1)
            if rm1 > 0 and rm1 > target_rm1:
                # R-hat decreases roughly as 1/sqrt(N)
                est["rhat_factor"] = (rm1 / target_rm1) ** 2
        except (ValueError, TypeError):
            pass
        try:
            ess = float(ess)
            if ess > 0 and ess < target_ess:
                # ESS grows roughly linearly
                est["ess_factor"] = target_ess / ess
        except (ValueError, TypeError):
            pass

        estimates[param_key] = est

    return estimates


# ---------------------------------------------------------------------------
# Freeze pack creation (via SSH, on-pod)
# ---------------------------------------------------------------------------

def create_science_freeze_pack(host, port, working_dir, chains_dir, dataset, timestamp, timeout, dry_run=False):
    """
    Create science freeze pack with chains 2-7 only.
    frozen_gpu_cohort_main_<dataset>_<timestamp>/
    """
    pack_name = "frozen_gpu_cohort_main_%s_%s" % (dataset, timestamp)
    pack_dir = "%s/frozen_packs/%s" % (working_dir, pack_name)

    if dry_run:
        return True, pack_name, "DRY RUN: would create %s" % pack_dir

    cmds = [
        "mkdir -p %s" % pack_dir,
    ]

    # Copy chains 2-7
    for i in range(2, 8):
        chain_src = "%s/%s_chain%d" % (chains_dir, dataset, i)
        cmds.append(
            "test -d %s && cp -r %s %s/chain%d/ || echo 'chain%d not found'" % (
                chain_src, chain_src, pack_dir, i, i
            )
        )

    # Generate convergence report
    cmds.append(
        "echo 'Science Freeze Pack — cohort_main (chains 2-7)' > %s/convergence_report.txt" % pack_dir
    )
    cmds.append(
        "echo 'Dataset: %s' >> %s/convergence_report.txt" % (dataset, pack_dir)
    )
    cmds.append(
        "echo 'Frozen: %s' >> %s/convergence_report.txt" % (timestamp, pack_dir)
    )
    cmds.append(
        "echo 'Criteria: R-hat-1 < 0.01 (H0, dNeff), < 0.02 (tau), ESS >= 2000 (H0, dNeff), >= 1000 (tau), drift < 0.2sigma' >> %s/convergence_report.txt" % pack_dir
    )
    cmds.append(
        "cat %s/cosmology/freeze_check.txt >> %s/convergence_report.txt 2>/dev/null || true" % (working_dir, pack_dir)
    )

    # Copy any existing triangle plots and 1D posteriors
    cmds.append(
        "cp %s/cosmology/trace_%s_*.png %s/ 2>/dev/null || true" % (working_dir, dataset, pack_dir)
    )

    # Create manifest
    manifest_content = (
        "MANIFEST — Science Freeze Pack\\n"
        "================================\\n"
        "Pack: %s\\n"
        "Dataset: %s\\n"
        "Chains included: 2-7 (cohort_main)\\n"
        "Chain 1 EXCLUDED: documented separately in archival pack\\n"
        "Frozen at: %s\\n"
        "Freeze trigger: Convergence criteria satisfied\\n"
        "\\n"
        "Convergence criteria:\\n"
        "  R-hat-1 < 0.01 for H0 and delta_neff\\n"
        "  R-hat-1 < 0.02 for tau\\n"
        "  ESS >= 2000 for H0 and delta_neff\\n"
        "  ESS >= 1000 for tau\\n"
        "  drift < 0.2 sigma for H0 and delta_neff\\n"
    ) % (pack_name, dataset, timestamp)
    cmds.append("echo -e '%s' > %s/MANIFEST.md" % (manifest_content, pack_dir))

    # Create checksums
    cmds.append(
        "cd %s && find . -type f ! -name CHECKSUMS.txt -exec sha256sum {} + > CHECKSUMS.txt 2>/dev/null || true" % pack_dir
    )

    full_cmd = " && ".join(cmds)
    ok, out, err = ssh_command(host, port, full_cmd, timeout=timeout + 60)
    if not ok:
        return False, pack_name, "Failed: %s %s" % (out, err)
    return True, pack_name, "Created successfully"


def create_archival_freeze_pack(host, port, working_dir, chains_dir, dataset, timestamp, timeout, dry_run=False):
    """
    Create full archival pack with chains 1-7.
    frozen_gpu_all_chains_<dataset>_<timestamp>/
    """
    pack_name = "frozen_gpu_all_chains_%s_%s" % (dataset, timestamp)
    pack_dir = "%s/frozen_packs/%s" % (working_dir, pack_name)

    if dry_run:
        return True, pack_name, "DRY RUN: would create %s" % pack_dir

    cmds = [
        "mkdir -p %s" % pack_dir,
    ]

    # Copy chain 1
    chain1_src = "%s/%s" % (chains_dir, dataset)
    cmds.append(
        "test -d %s && cp -r %s %s/chain1/ || echo 'chain1 not found'" % (
            chain1_src, chain1_src, pack_dir
        )
    )

    # Copy chains 2-7
    for i in range(2, 8):
        chain_src = "%s/%s_chain%d" % (chains_dir, dataset, i)
        cmds.append(
            "test -d %s && cp -r %s %s/chain%d/ || echo 'chain%d not found'" % (
                chain_src, chain_src, pack_dir, i, i
            )
        )

    # Copy convergence diagnostics
    cmds.append(
        "cp %s/cosmology/convergence_latest.csv %s/ 2>/dev/null || true" % (working_dir, pack_dir)
    )
    cmds.append(
        "cp %s/cosmology/freeze_check.txt %s/ 2>/dev/null || true" % (working_dir, pack_dir)
    )
    cmds.append(
        "cp %s/cosmology/bottlenecks_latest.txt %s/ 2>/dev/null || true" % (working_dir, pack_dir)
    )
    cmds.append(
        "cp %s/cosmology/trend_monitor_latest.txt %s/ 2>/dev/null || true" % (working_dir, pack_dir)
    )

    # Create manifest explaining chain 1 exclusion
    manifest_content = (
        "MANIFEST — Full Archival Pack\\n"
        "================================\\n"
        "Pack: %s\\n"
        "Dataset: %s\\n"
        "Chains included: 1-7 (ALL chains)\\n"
        "Frozen at: %s\\n"
        "\\n"
        "IMPORTANT: Chain 1 was EXCLUDED from science interpretation.\\n"
        "Chain 1 started from a different initial point and has significantly\\n"
        "fewer samples than chains 2-7. Its inclusion inflates R-hat for nnu\\n"
        "due to incomplete mixing. The science-quality results are in the\\n"
        "companion pack: frozen_gpu_cohort_main_%s_%s\\n"
        "\\n"
        "This archival pack preserves ALL chain data for reproducibility\\n"
        "and future re-analysis.\\n"
    ) % (pack_name, dataset, timestamp, dataset, timestamp)
    cmds.append("echo -e '%s' > %s/MANIFEST.md" % (manifest_content, pack_dir))

    # Checksums
    cmds.append(
        "cd %s && find . -type f ! -name CHECKSUMS.txt -exec sha256sum {} + > CHECKSUMS.txt 2>/dev/null || true" % pack_dir
    )

    full_cmd = " && ".join(cmds)
    ok, out, err = ssh_command(host, port, full_cmd, timeout=timeout + 120)
    if not ok:
        return False, pack_name, "Failed: %s %s" % (out, err)
    return True, pack_name, "Created successfully"


def create_safety_snapshot(host, port, working_dir, chains_dir, dataset, timestamp, timeout, dry_run=False):
    """
    Create a periodic safety snapshot.
    snapshot_gpu_<dataset>_<timestamp>/
    """
    snap_name = "snapshot_gpu_%s_%s" % (dataset, timestamp)
    snap_dir = "%s/frozen_packs/%s" % (working_dir, snap_name)

    if dry_run:
        return True, snap_name, "DRY RUN: would create %s" % snap_dir

    cmds = [
        "mkdir -p %s" % snap_dir,
    ]

    # Copy current chains (all 7)
    chain1_src = "%s/%s" % (chains_dir, dataset)
    cmds.append(
        "test -d %s && cp -r %s %s/chain1/ || true" % (chain1_src, chain1_src, snap_dir)
    )
    for i in range(2, 8):
        chain_src = "%s/%s_chain%d" % (chains_dir, dataset, i)
        cmds.append(
            "test -d %s && cp -r %s %s/chain%d/ || true" % (chain_src, chain_src, snap_dir, i)
        )

    # Copy current convergence diagnostics
    cmds.append("cp %s/cosmology/convergence_latest.csv %s/ 2>/dev/null || true" % (working_dir, snap_dir))
    cmds.append("cp %s/cosmology/freeze_check.txt %s/ 2>/dev/null || true" % (working_dir, snap_dir))

    # Create manifest
    manifest_content = (
        "MANIFEST — Safety Snapshot\\n"
        "============================\\n"
        "Snapshot: %s\\n"
        "Dataset: %s\\n"
        "Taken at: %s\\n"
        "Type: Periodic safety snapshot (every 6 hours)\\n"
        "Convergence NOT required — this is a data safety measure.\\n"
        "Chains were NOT stopped for this snapshot.\\n"
    ) % (snap_name, dataset, timestamp)
    cmds.append("echo -e '%s' > %s/MANIFEST.md" % (manifest_content, snap_dir))

    full_cmd = " && ".join(cmds)
    ok, out, err = ssh_command(host, port, full_cmd, timeout=timeout + 120)
    if not ok:
        return False, snap_name, "Failed: %s %s" % (out, err)
    return True, snap_name, "Created successfully"


# ---------------------------------------------------------------------------
# Improvement rate estimation
# ---------------------------------------------------------------------------

def compute_improvement_rate(host, port, working_dir, timeout):
    """Read convergence history and compute recent improvement rate."""
    cmd = "tail -100 %s/cosmology/convergence_history.csv 2>/dev/null" % working_dir
    ok, out, _ = ssh_command(host, port, cmd, timeout)
    if not ok or not out.strip():
        return {}

    lines = out.strip().splitlines()
    # Parse CSV
    history = []
    for line in lines:
        parts = line.split(",")
        if len(parts) >= 6:
            try:
                history.append({
                    "epoch": float(parts[0]),
                    "dataset": parts[2].strip(),
                    "param": parts[3].strip(),
                    "rhat_m1": float(parts[4]),
                    "ess": float(parts[5]),
                })
            except (ValueError, IndexError):
                continue

    if not history:
        return {}

    now_epoch = time.time()
    rates = {}

    for ds in DATASETS:
        rates[ds] = {}
        for param in ["H0", "delta_neff", "tau"]:
            ds_param_pts = sorted(
                [h for h in history if h["dataset"] == ds and h["param"] == param],
                key=lambda x: x["epoch"]
            )
            if len(ds_param_pts) < 2:
                continue

            # 12h window comparison
            recent = ds_param_pts[-1]
            older = None
            for pt in ds_param_pts:
                age_h = (now_epoch - pt["epoch"]) / 3600.0
                if age_h >= 10 and age_h <= 14:
                    older = pt
                    break
            if older is None and len(ds_param_pts) >= 2:
                older = ds_param_pts[0]

            if older:
                dt_h = (recent["epoch"] - older["epoch"]) / 3600.0
                if dt_h > 0:
                    rm1_rate = (older["rhat_m1"] - recent["rhat_m1"]) / dt_h
                    pct_improvement = (
                        (older["rhat_m1"] - recent["rhat_m1"]) / older["rhat_m1"] * 100
                        if older["rhat_m1"] > 0 else 0
                    )
                    rates[ds][param] = {
                        "rhat_m1_rate_per_h": rm1_rate,
                        "pct_improvement": pct_improvement,
                        "window_hours": dt_h,
                        "improving": rm1_rate > 0,
                    }

    return rates


# ---------------------------------------------------------------------------
# Status report generation
# ---------------------------------------------------------------------------

def generate_status_report(pod, conv_results, sample_counts, cobaya_count,
                           frozen_packs, snapshots, improvement_rates,
                           freeze_actions, snapshot_actions, dry_run):
    """Generate the unified project status report."""
    now = datetime.datetime.utcnow()
    ts = now.strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    json_data = {
        "report": {
            "generated_at": ts,
            "method": "Live SSH probe — convergence-only freeze logic",
            "freeze_policy": "CONVERGENCE ONLY — no time cap",
        },
        "convergence_criteria": CONVERGENCE_CRITERIA,
        "datasets": {},
        "freeze_actions": freeze_actions,
        "snapshot_actions": snapshot_actions,
        "improvement_rates": {},
    }

    lines.append(SEP)
    lines.append("  BIGBOUNCE GPU FREEZE MANAGER — STATUS REPORT")
    lines.append("  Generated: %s" % ts)
    lines.append("  Policy: CONVERGENCE ONLY — no time cap, chains never stopped")
    lines.append(SEP)

    # Cobaya processes
    lines.append("")
    lines.append("  Active cobaya processes: %d" % cobaya_count)
    lines.append("  Existing frozen packs: %s" % (", ".join(frozen_packs) if frozen_packs else "none"))
    lines.append("  Recent snapshots: %s" % (", ".join(snapshots[:3]) if snapshots else "none"))

    # Per-dataset convergence
    lines.append("")
    lines.append(SEP)
    lines.append("  CONVERGENCE STATUS — cohort_main (chains 2-7)")
    lines.append(SEP)

    closest_ds = None
    closest_score = float("inf")

    for ds in DATASETS:
        metrics = conv_results.get(ds, {})
        converged, details = evaluate_convergence(metrics)
        gates = details.get("gates", {})
        values = details.get("values", {})
        counts = sample_counts.get(ds, {})
        estimates = estimate_remaining_samples(metrics)

        # Compute "distance to convergence" score
        score = 0
        for gk, gv in gates.items():
            if not gv:
                score += 1
        if score < closest_score:
            closest_score = score
            closest_ds = ds

        ds_label = ds.upper().replace("_", " ")
        lines.append("")
        lines.append("  --- %s ---" % ds_label)
        lines.append("  Status: %s" % (GREEN + "CONVERGED" + RESET if converged else YELLOW + "RUNNING" + RESET))

        # Sample counts
        cohort_samples = [counts.get(i, 0) for i in range(2, 8)]
        chain1_samples = counts.get(1, 0)
        if cohort_samples:
            lines.append("  Samples: chain1=%d  cohort_main=%d-%d  total=%d" % (
                chain1_samples,
                min(cohort_samples) if cohort_samples else 0,
                max(cohort_samples) if cohort_samples else 0,
                chain1_samples + sum(cohort_samples),
            ))

        # Gate status table
        lines.append("")
        lines.append("    %-12s  %-12s  %-10s  %-8s" % ("Criterion", "Value", "Target", "Status"))
        lines.append("    %s  %s  %s  %s" % ("-" * 12, "-" * 12, "-" * 10, "-" * 8))

        def fmt_val(v):
            try:
                return "%.5f" % float(v)
            except (ValueError, TypeError):
                return "N/A"

        gate_rows = [
            ("R-hat H0", values.get("rhat_H0"), "< 0.01", gates.get("rhat_H0")),
            ("R-hat nnu", values.get("rhat_nnu"), "< 0.01", gates.get("rhat_nnu")),
            ("R-hat tau", values.get("rhat_tau"), "< 0.02", gates.get("rhat_tau")),
            ("ESS H0", values.get("ess_H0"), ">= 2000", gates.get("ess_H0")),
            ("ESS nnu", values.get("ess_nnu"), ">= 2000", gates.get("ess_nnu")),
            ("ESS tau", values.get("ess_tau"), ">= 1000", gates.get("ess_tau")),
            ("Drift H0", values.get("drift_H0"), "< 0.2sig", gates.get("drift_H0")),
            ("Drift nnu", values.get("drift_nnu"), "< 0.2sig", gates.get("drift_nnu")),
        ]
        for label, val, target, passed in gate_rows:
            status = "PASS" if passed else "FAIL"
            lines.append("    %-12s  %-12s  %-10s  %s" % (label, fmt_val(val), target, status))

        # Improvement rate
        ds_rates = improvement_rates.get(ds, {})
        if ds_rates:
            lines.append("")
            lines.append("  Improvement rates (last ~12h):")
            for param, rate_info in ds_rates.items():
                if rate_info.get("improving"):
                    lines.append("    %s: %.5f/h improvement (%.1f%% over %.1fh)" % (
                        param, rate_info["rhat_m1_rate_per_h"],
                        rate_info["pct_improvement"], rate_info["window_hours"],
                    ))
                else:
                    lines.append("    %s: stalled or worsening" % param)

        # Estimated remaining
        if not converged:
            lines.append("")
            lines.append("  Estimated factors to convergence:")
            for param, est in estimates.items():
                parts = []
                if est.get("rhat_factor"):
                    parts.append("R-hat: ~%.1fx more samples" % est["rhat_factor"])
                if est.get("ess_factor"):
                    parts.append("ESS: ~%.1fx more samples" % est["ess_factor"])
                if parts:
                    lines.append("    %s: %s" % (param, ", ".join(parts)))

        # Store in JSON
        json_data["datasets"][ds] = {
            "converged": converged,
            "gates": {k: v for k, v in gates.items()},
            "values": {k: (float(v) if v is not None else None) for k, v in values.items()},
            "sample_counts": counts,
            "estimates": estimates,
        }
        json_data["improvement_rates"][ds] = ds_rates

    # All-chains diagnostic
    lines.append("")
    lines.append(SEP)
    lines.append("  ALL-CHAINS CONVERGENCE (chains 1-7, for archival reference)")
    lines.append(SEP)
    for ds in DATASETS:
        metrics = conv_results.get(ds, {})
        params = metrics.get("params", {})
        ds_label = ds.upper().replace("_", " ")
        h0_all = params.get("H0", {}).get("rhat_m1_all", "N/A")
        nnu_all = params.get("delta_neff", {}).get("rhat_m1_all", "N/A")
        tau_all = params.get("tau", {}).get("rhat_m1_all", "N/A")
        lines.append("  %-18s  H0=%-10s  nnu=%-10s  tau=%-10s" % (
            ds_label,
            fmt_val(h0_all), fmt_val(nnu_all), fmt_val(tau_all),
        ))

    # Actions taken
    if freeze_actions or snapshot_actions:
        lines.append("")
        lines.append(SEP)
        lines.append("  ACTIONS TAKEN THIS CYCLE")
        lines.append(SEP)
        for action in freeze_actions:
            lines.append("  [FREEZE] %s" % action)
        for action in snapshot_actions:
            lines.append("  [SNAPSHOT] %s" % action)

    # Summary
    lines.append("")
    lines.append(SEP)
    lines.append("  SUMMARY")
    lines.append(SEP)
    lines.append("")
    lines.append("  Closest to convergence: %s (%d of 8 gates failing)" % (
        closest_ds or "unknown", closest_score,
    ))
    lines.append("")
    lines.append("  Current R-hat-1 values (cohort_main):")
    for ds in DATASETS:
        metrics = conv_results.get(ds, {})
        params = metrics.get("params", {})
        h0 = params.get("H0", {}).get("rhat_m1_cohort", "N/A")
        nnu = params.get("delta_neff", {}).get("rhat_m1_cohort", "N/A")
        tau = params.get("tau", {}).get("rhat_m1_cohort", "N/A")
        lines.append("    %-18s  H0=%-10s  nnu=%-10s  tau=%-10s" % (
            ds, fmt_val(h0), fmt_val(nnu), fmt_val(tau),
        ))

    lines.append("")
    lines.append("  Current ESS values (cohort_main):")
    for ds in DATASETS:
        metrics = conv_results.get(ds, {})
        params = metrics.get("params", {})
        h0 = params.get("H0", {}).get("ess_cohort", "N/A")
        nnu = params.get("delta_neff", {}).get("ess_cohort", "N/A")
        tau = params.get("tau", {}).get("ess_cohort", "N/A")
        lines.append("    %-18s  H0=%-10s  nnu=%-10s  tau=%-10s" % (
            ds, fmt_val(h0), fmt_val(nnu), fmt_val(tau),
        ))

    lines.append("")
    lines.append("  Improvement still occurring:")
    any_improving = False
    for ds in DATASETS:
        ds_rates = improvement_rates.get(ds, {})
        improving_params = [p for p, r in ds_rates.items() if r.get("improving")]
        if improving_params:
            any_improving = True
            lines.append("    %s: YES (%s)" % (ds, ", ".join(improving_params)))
        else:
            lines.append("    %s: no recent improvement data" % ds)

    lines.append("")
    lines.append("  Policy reminders:")
    lines.append("    - Chains run indefinitely until convergence")
    lines.append("    - No time-based freeze cap")
    lines.append("    - Safety snapshots every %dh" % SAFETY_SNAPSHOT_INTERVAL_H)
    lines.append("    - Hourly backups continue after convergence")
    lines.append("")
    lines.append(SEP)
    lines.append("  END OF REPORT")
    lines.append(SEP)

    json_data["summary"] = {
        "closest_to_convergence": closest_ds,
        "gates_failing": closest_score,
        "any_improving": any_improving,
    }

    return "\n".join(lines), json_data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_registry(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("pods", [])


def strip_ansi(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)


def parse_args():
    parser = argparse.ArgumentParser(
        description="BigBounce GPU Freeze Manager — convergence-only freeze logic."
    )
    parser.add_argument("--registry", default=DEFAULT_REGISTRY)
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without creating packs")
    parser.add_argument("--force-freeze", type=str, default=None,
                        help="Force-freeze a specific dataset (manual override)")
    return parser.parse_args()


def main():
    args = parse_args()
    pods = load_registry(args.registry)

    # Find the GPU validation pod
    gpu_pod = None
    for pod in pods:
        if pod.get("pod_name") == "bigbounce-gpu-validation":
            gpu_pod = pod
            break

    if not gpu_pod:
        print("ERROR: bigbounce-gpu-validation pod not found in registry.")
        sys.exit(1)

    host = gpu_pod.get("ssh_host")
    port = gpu_pod.get("ssh_port")
    working_dir = gpu_pod.get("working_dir", "/workspace/bigbounce/reproducibility")
    chains_dir = "%s/chains" % working_dir

    print("%sBigBounce GPU Freeze Manager%s" % (BOLD, RESET))
    print("Policy: CONVERGENCE ONLY — no time cap")
    print("Checking pod %s (%s:%s)...\n" % (gpu_pod["pod_name"], host, port))

    if not ssh_alive(host, port, timeout=args.timeout):
        print("%sERROR: GPU pod is UNREACHABLE%s" % (RED, RESET))
        sys.exit(1)

    print("  Pod is alive. Collecting data...\n")

    # Collect data
    cobaya_count = get_process_count(host, port, args.timeout)
    frozen_packs = check_existing_frozen_packs(host, port, working_dir, args.timeout)
    snapshots = check_existing_snapshots(host, port, working_dir, args.timeout)
    freeze_check_text = get_freeze_check(host, port, working_dir, args.timeout)
    conv_data = get_convergence_diagnostics(
        host, port,
        gpu_pod.get("status_file", "%s/cosmology/convergence_latest.csv" % working_dir),
        args.timeout,
    )

    sample_counts = {}
    for ds in DATASETS:
        sample_counts[ds] = get_chain_sample_counts(host, port, chains_dir, ds, args.timeout)

    conv_results = parse_cohort_convergence(conv_data, freeze_check_text)
    improvement_rates = compute_improvement_rate(host, port, working_dir, args.timeout)

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    # Evaluate convergence and create freeze packs
    freeze_actions = []
    snapshot_actions = []

    for ds in DATASETS:
        metrics = conv_results.get(ds, {})
        converged, details = evaluate_convergence(metrics)

        # Check if already frozen
        science_pack_exists = any("cohort_main_%s" % ds in p for p in frozen_packs)

        if args.force_freeze == ds:
            print("  %s[MANUAL FREEZE]%s %s" % (YELLOW, RESET, ds))
            if not science_pack_exists:
                ok, name, msg = create_science_freeze_pack(
                    host, port, working_dir, chains_dir, ds, timestamp,
                    args.timeout, dry_run=args.dry_run,
                )
                freeze_actions.append("%s science pack: %s (%s)" % (ds, name, msg))
                ok2, name2, msg2 = create_archival_freeze_pack(
                    host, port, working_dir, chains_dir, ds, timestamp,
                    args.timeout, dry_run=args.dry_run,
                )
                freeze_actions.append("%s archival pack: %s (%s)" % (ds, name2, msg2))
            else:
                freeze_actions.append("%s already has science freeze pack — skipped" % ds)

        elif converged and not science_pack_exists:
            print("  %s[CONVERGENCE FREEZE]%s %s — all criteria satisfied!" % (GREEN, RESET, ds))
            ok, name, msg = create_science_freeze_pack(
                host, port, working_dir, chains_dir, ds, timestamp,
                args.timeout, dry_run=args.dry_run,
            )
            freeze_actions.append("%s science pack: %s (%s)" % (ds, name, msg))
            ok2, name2, msg2 = create_archival_freeze_pack(
                host, port, working_dir, chains_dir, ds, timestamp,
                args.timeout, dry_run=args.dry_run,
            )
            freeze_actions.append("%s archival pack: %s (%s)" % (ds, name2, msg2))

        elif converged and science_pack_exists:
            print("  %s[CONVERGED]%s %s — already frozen" % (GREEN, RESET, ds))

        else:
            gates = details.get("gates", {})
            passing = sum(1 for v in gates.values() if v)
            total = len(gates)
            print("  %s[RUNNING]%s %s — %d/%d gates passing" % (YELLOW, RESET, ds, passing, total))

    # Safety snapshots — every 6 hours
    for ds in DATASETS:
        latest_snap_age = get_latest_snapshot_age(host, port, working_dir, args.timeout)
        needs_snapshot = (latest_snap_age is None or latest_snap_age >= SAFETY_SNAPSHOT_INTERVAL_H)

        if needs_snapshot:
            print("  %s[SNAPSHOT]%s %s — creating safety snapshot" % (CYAN, RESET, ds))
            ok, name, msg = create_safety_snapshot(
                host, port, working_dir, chains_dir, ds, timestamp,
                args.timeout, dry_run=args.dry_run,
            )
            snapshot_actions.append("%s: %s (%s)" % (ds, name, msg))

    # Generate report
    report_text, json_data = generate_status_report(
        gpu_pod, conv_results, sample_counts, cobaya_count,
        frozen_packs, snapshots, improvement_rates,
        freeze_actions, snapshot_actions, args.dry_run,
    )

    # Print to terminal
    print("")
    print(report_text)

    # Save outputs
    plain_text = strip_ansi(report_text)
    with open(STATUS_TXT, "w") as f:
        f.write(plain_text)

    with open(STATUS_JSON, "w") as f:
        json.dump(json_data, f, indent=2, default=str)

    print("\nOutputs saved:")
    print("  %s" % STATUS_TXT)
    print("  %s" % STATUS_JSON)

    return 0


if __name__ == "__main__":
    sys.exit(main())
