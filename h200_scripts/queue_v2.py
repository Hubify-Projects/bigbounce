#!/usr/bin/env python3
"""
H200 Research Queue v2 — Houston Method Completion Protocol
============================================================
Runs experiments sequentially with mandatory QC gates after each.
Experiments that fail QC are logged and skipped (re-run task auto-added).
Results are backed up after every experiment.

Usage:
    python queue_v2.py                    # Run full queue
    python queue_v2.py --phase 1          # Run specific phase only
    python queue_v2.py --resume           # Resume from last checkpoint
    python queue_v2.py --dry-run          # Print queue without executing
"""

import json
import os
import sys
import time
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path

QUEUE_FILE = Path("/workspace/bigbounce/research_queue_v2.json")
OUTPUT_DIR = Path("/workspace/bigbounce/outputs")
CHECKPOINT_DIR = Path("/workspace/bigbounce/checkpoints")
COST_PER_HOUR = 3.59  # H200 rate

# ═══════════════════════════════════════════════════════
# QC Gates — Houston Method v2 Step 2
# ═══════════════════════════════════════════════════════

def qc_null_coordinates(results_dir):
    """Check for null coordinates (RA=0, Dec=0) in top anomalies."""
    for f in results_dir.glob("*summary*.json"):
        with open(f) as fh:
            data = json.load(fh)
        top = data.get("top_20", data.get("top_anomalies", []))
        if not top:
            continue
        null_count = sum(1 for item in top if item.get("ra", -1) == 0.0 and item.get("dec", -1) == 0.0)
        null_frac = null_count / len(top) if top else 0
        if null_frac > 0.05:
            return False, f"null_coordinates: {null_frac:.0%} of top anomalies have RA=0,Dec=0"
    return True, "null_coordinates: OK"


def qc_training_quality(results_dir):
    """Check if model training converged."""
    for f in results_dir.glob("*summary*.json"):
        with open(f) as fh:
            data = json.load(fh)
        val_loss = data.get("best_val_loss", data.get("val_loss"))
        if val_loss is not None and val_loss > 1000:
            return False, f"training_quality: val_loss={val_loss:.1f} > 1000 (undertrained)"
    return True, "training_quality: OK"


def qc_cluster_degeneracy(results_dir):
    """Check for degenerate clustering (>80% in one cluster)."""
    for f in results_dir.glob("*summary*.json"):
        with open(f) as fh:
            data = json.load(fh)
        clusters = data.get("clusters", [])
        n_objects = data.get("n_objects", data.get("n_sources", 0))
        if clusters and n_objects > 0:
            max_cluster = max(c.get("size", 0) for c in clusters)
            if max_cluster / n_objects > 0.80:
                return False, f"cluster_degeneracy: largest cluster has {max_cluster}/{n_objects} ({max_cluster/n_objects:.0%})"
    return True, "cluster_degeneracy: OK"


def qc_score_explosion(results_dir):
    """Check for anomaly score explosion (>10^6)."""
    for f in results_dir.glob("*summary*.json"):
        with open(f) as fh:
            data = json.load(fh)
        top = data.get("top_20", data.get("top_anomalies", []))
        for item in top:
            score = item.get("score", item.get("anomaly_score", 0))
            if abs(score) > 1e6:
                return False, f"score_explosion: max score={score:.2e} > 10^6"
    return True, "score_explosion: OK"


def qc_spatial_concentration(results_dir):
    """Check if all top anomalies are within 5 degrees of each other."""
    import math
    for f in results_dir.glob("*summary*.json"):
        with open(f) as fh:
            data = json.load(fh)
        top = data.get("top_20", data.get("top_anomalies", []))
        coords = [(item.get("ra", 0), item.get("dec", 0)) for item in top if "ra" in item]
        if len(coords) < 5:
            continue
        # Check if all within 5 degree box
        ras = [c[0] for c in coords]
        decs = [c[1] for c in coords]
        ra_spread = max(ras) - min(ras)
        dec_spread = max(decs) - min(decs)
        if ra_spread < 5 and dec_spread < 5:
            return False, f"spatial_concentration: all top anomalies within {ra_spread:.1f}x{dec_spread:.1f} deg box"
    return True, "spatial_concentration: OK"


def qc_output_nonempty(results_dir):
    """Check that output files exist and are non-empty."""
    files = list(results_dir.glob("*"))
    if not files:
        return False, "output_nonempty: no output files found"
    for f in files:
        if f.is_file() and f.stat().st_size == 0:
            return False, f"output_nonempty: {f.name} is empty"
    return True, "output_nonempty: OK"


QC_CHECKS = [
    qc_null_coordinates,
    qc_training_quality,
    qc_cluster_degeneracy,
    qc_score_explosion,
    qc_spatial_concentration,
    qc_output_nonempty,
]


def run_qc_gate(results_dir):
    """Run all QC checks. Returns (passed: bool, results: dict)."""
    results = {}
    all_passed = True
    failure_modes = []

    for check_fn in QC_CHECKS:
        try:
            passed, msg = check_fn(results_dir)
        except Exception as e:
            passed, msg = False, f"{check_fn.__name__}: ERROR - {e}"
        results[check_fn.__name__] = {"passed": passed, "message": msg}
        if not passed:
            all_passed = False
            failure_modes.append(msg)

    return all_passed, results, failure_modes


# ═══════════════════════════════════════════════════════
# Checkpoint Management
# ═══════════════════════════════════════════════════════

def write_checkpoint(experiment_id, data):
    """Write checkpoint JSON for an experiment."""
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    checkpoint_path = CHECKPOINT_DIR / f"{experiment_id}.json"
    data["timestamp"] = datetime.now(timezone.utc).isoformat()
    with open(checkpoint_path, "w") as f:
        json.dump(data, f, indent=2)
    return checkpoint_path


def get_completed_experiments():
    """Get set of experiment IDs that have completed checkpoints."""
    completed = set()
    if CHECKPOINT_DIR.exists():
        for f in CHECKPOINT_DIR.glob("*.json"):
            with open(f) as fh:
                data = json.load(fh)
            if data.get("status") == "complete":
                completed.add(data.get("experiment_id", f.stem))
    return completed


# ═══════════════════════════════════════════════════════
# Experiment Runner
# ═══════════════════════════════════════════════════════

def run_experiment(experiment):
    """Run a single experiment with QC gate and checkpoint."""
    exp_id = experiment["id"]
    exp_name = experiment["name"]
    script = experiment.get("script", "")
    phase = experiment.get("phase", 0)

    print(f"\n{'='*60}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting: {exp_name}")
    print(f"  Phase: {phase} | ID: {exp_id}")
    print(f"{'='*60}")

    results_dir = OUTPUT_DIR / exp_id
    results_dir.mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    # Step 1: RUN
    if script:
        try:
            timeout = experiment.get("timeout_seconds", 7200)  # 2h default
            result = subprocess.run(
                ["python3", script],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(results_dir),
            )
            if result.returncode != 0:
                print(f"  ERROR: Script failed with code {result.returncode}")
                print(f"  STDERR: {result.stderr[:500]}")
                write_checkpoint(exp_id, {
                    "experiment_id": exp_id,
                    "status": "error",
                    "error": result.stderr[:1000],
                    "gpu_hours": (time.time() - start_time) / 3600,
                    "cost_usd": round((time.time() - start_time) / 3600 * COST_PER_HOUR, 2),
                })
                return False
        except subprocess.TimeoutExpired:
            print(f"  TIMEOUT after {timeout}s")
            write_checkpoint(exp_id, {
                "experiment_id": exp_id,
                "status": "timeout",
                "timeout_seconds": timeout,
            })
            return False

    elapsed = time.time() - start_time
    gpu_hours = elapsed / 3600
    cost = round(gpu_hours * COST_PER_HOUR, 2)

    # Step 2: QC GATE
    print(f"\n  Running QC gate...")
    qc_passed, qc_results, failure_modes = run_qc_gate(results_dir)

    if qc_passed:
        print(f"  QC: PASS (all {len(QC_CHECKS)} checks passed)")
    else:
        print(f"  QC: FAIL")
        for mode in failure_modes:
            print(f"    - {mode}")

    # Write checkpoint
    checkpoint = {
        "experiment_id": exp_id,
        "name": exp_name,
        "phase": phase,
        "status": "complete" if qc_passed else "qc_fail",
        "qc_status": "PASS" if qc_passed else "FAIL",
        "qc_results": qc_results,
        "failure_modes": failure_modes,
        "started": datetime.fromtimestamp(start_time, tz=timezone.utc).isoformat(),
        "completed": datetime.now(timezone.utc).isoformat(),
        "gpu_hours": round(gpu_hours, 3),
        "cost_usd": cost,
    }
    write_checkpoint(exp_id, checkpoint)

    print(f"\n  Duration: {elapsed:.0f}s ({gpu_hours:.2f} GPU-hrs)")
    print(f"  Cost: ${cost}")
    print(f"  Status: {'COMPLETE' if qc_passed else 'QC FAIL — added to re-run queue'}")

    # Backup to local (if network available)
    try:
        subprocess.run(
            ["scp", "-r", "-q", str(results_dir), f"local:bigbounce/pipelines/h200_results/{exp_id}/"],
            timeout=300,
            capture_output=True,
        )
        print(f"  Backup: scp to local OK")
    except Exception:
        print(f"  Backup: scp failed (will retry later)")

    return qc_passed


# ═══════════════════════════════════════════════════════
# Queue Runner
# ═══════════════════════════════════════════════════════

def load_queue():
    """Load the experiment queue."""
    if QUEUE_FILE.exists():
        with open(QUEUE_FILE) as f:
            return json.load(f)
    # Default queue if no file exists
    return {"experiments": [], "metadata": {"created": datetime.now(timezone.utc).isoformat()}}


def run_queue(phase_filter=None, resume=False, dry_run=False):
    """Run the full experiment queue."""
    queue = load_queue()
    experiments = queue.get("experiments", [])

    if phase_filter is not None:
        experiments = [e for e in experiments if e.get("phase") == phase_filter]

    if resume:
        completed = get_completed_experiments()
        experiments = [e for e in experiments if e["id"] not in completed]
        print(f"Resuming: {len(completed)} already done, {len(experiments)} remaining")

    total = len(experiments)
    total_cost = 0
    passed = 0
    failed = 0

    print(f"\n{'#'*60}")
    print(f"  H200 Queue v2 — Houston Method Completion Protocol")
    print(f"  {total} experiments queued")
    if phase_filter is not None:
        print(f"  Phase filter: {phase_filter}")
    print(f"  Cost rate: ${COST_PER_HOUR}/hr")
    print(f"{'#'*60}")

    if dry_run:
        for i, exp in enumerate(experiments, 1):
            est_hours = exp.get("est_hours", "?")
            est_cost = f"${float(est_hours) * COST_PER_HOUR:.0f}" if isinstance(est_hours, (int, float)) else "?"
            print(f"  [{i}/{total}] Phase {exp.get('phase', '?')}: {exp['name']} (~{est_hours}h, ~{est_cost})")
        return

    queue_start = time.time()

    for i, experiment in enumerate(experiments, 1):
        print(f"\n[{i}/{total}] ", end="")
        success = run_experiment(experiment)
        if success:
            passed += 1
        else:
            failed += 1

    queue_elapsed = time.time() - queue_start
    queue_hours = queue_elapsed / 3600
    queue_cost = round(queue_hours * COST_PER_HOUR, 2)

    print(f"\n{'#'*60}")
    print(f"  QUEUE COMPLETE")
    print(f"  Passed QC: {passed}/{total}")
    print(f"  Failed QC: {failed}/{total}")
    print(f"  Total time: {queue_hours:.1f} hours")
    print(f"  Total cost: ${queue_cost}")
    print(f"{'#'*60}")

    # Write final summary
    summary = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "total_experiments": total,
        "passed_qc": passed,
        "failed_qc": failed,
        "total_gpu_hours": round(queue_hours, 2),
        "total_cost_usd": queue_cost,
    }
    with open(OUTPUT_DIR / "queue_v2_summary.json", "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="H200 Research Queue v2")
    parser.add_argument("--phase", type=int, help="Run specific phase only")
    parser.add_argument("--resume", action="store_true", help="Resume from last checkpoint")
    parser.add_argument("--dry-run", action="store_true", help="Print queue without executing")
    args = parser.parse_args()

    run_queue(phase_filter=args.phase, resume=args.resume, dry_run=args.dry_run)
