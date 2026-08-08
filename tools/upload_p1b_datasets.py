#!/usr/bin/env python3
"""Upload P1B reproducibility datasets to HuggingFace under bamfai account."""

import os
import re
import shutil
import tempfile
from pathlib import Path

# Load .env.local
env_path = Path(__file__).parent.parent / ".env.local"
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ[k] = v

token = os.environ.get('HF_TOKEN', '')
if not token:
    raise RuntimeError("HF_TOKEN not found in .env.local")

from huggingface_hub import HfApi, upload_file, upload_folder

api = HfApi(token=token)
who = api.whoami()
print(f"Logged in as: {who['name']}")

BASE = Path(__file__).parent.parent
LICENSE = "cc-by-4.0"
PAPER_VERSION = "v1B.0.75"

# ─── Dataset 1: p1b-mcmc-diagnostics ───────────────────────────────────────

DATASET1_ID = "bamfai/p1b-mcmc-diagnostics"
COSMO_DIR = BASE / "reproducibility" / "cosmology"

readme1 = f"""---
license: {LICENSE}
language:
- en
pretty_name: "P1B MCMC Chain Diagnostics and Convergence (bigbounce)"
size_categories:
- n<1K
task_categories:
- other
tags:
- cosmology
- mcmc
- convergence
- cobaya
- big-bounce
- reproducibility
---

# P1B MCMC Chain Diagnostics

**Title:** MCMC chain diagnostics and convergence CSV files

## Description

This dataset contains the top-level MCMC chain diagnostic and convergence summary files
produced by the Cobaya MCMC sampler for the P1B cosmological parameter inference runs.
It corresponds to **Appendix A, item 1** of the paper
"P1B — Technical Verification Companion to the ECH Spin-Torsion Program" ({PAPER_VERSION}).

Files include convergence CSVs (R-1 statistics per chain), chain-mean summaries,
dataset-to-chain mapping, configuration hashes for reproducibility verification,
and the Cobaya YAML configuration files used for each run (Planck-only, Planck+BAO,
Planck+BAO+SN, full-tension, and quintom w0wa test).

## Provenance

- **Paper:** P1B — Technical Verification Companion to the ECH Spin-Torsion Program ({PAPER_VERSION})
- **GitHub:** [github.com/Hubify-Projects/bigbounce](https://github.com/Hubify-Projects/bigbounce)
- **Reproducibility directory:** `reproducibility/cosmology/` (top-level files only; raw chains excluded)
- **Appendix A item:** 1 — MCMC chain diagnostics and convergence CSV files
- **Paper PDF:** [bigbounce.hubify.app](https://bigbounce.hubify.app)
"""

# Gather files: top-level only (no subdirs), specific patterns
INCLUDE_PATTERNS = [
    "*.csv",
    "CHAIN_SUMMARY_LATEST.txt",
    "mcmc_results_latest.txt",
    "bottlenecks_latest.txt",
    "convergence_latest.csv",
    "chain_means_latest.csv",
    "dataset_chain_map.csv",
    "config_hashes.csv",
    "convergence_cohort_main.csv",
    "cobaya_*.yaml",
    # Also include other informative txt files at top level
    "getdist_convergence_validation_*.txt",
    "reproduce_cosmology.sh",
    "COUNT_EXPLANATION.md",
    "README_w0wa_quintom.md",
]

SKIP_SUBDIRS = {"chains", "archives", "cpu1_diagnostics", "cpu2_diagnostics",
                "frozen", "iter2_converged_2026-05-18", "paper1_clean_restart_sync",
                "planck_only_live_sync", "runpod_snapshot_20260304",
                "paper1_clean_restart_sync"}


def gather_top_level_files(src_dir, include_patterns, skip_subdirs):
    """Gather only top-level files matching patterns, skipping subdirs."""
    import fnmatch
    files = []
    for item in src_dir.iterdir():
        if item.is_dir():
            continue  # skip all subdirs
        for pat in include_patterns:
            if fnmatch.fnmatch(item.name, pat):
                files.append(item)
                break
    return files


print("\n=== Dataset 1: p1b-mcmc-diagnostics ===")
api.create_repo(repo_id=DATASET1_ID, repo_type="dataset", private=False, exist_ok=True)
print(f"Repo created/confirmed: {DATASET1_ID}")

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    # Write README
    (tmpdir / "README.md").write_text(readme1)
    # Copy files
    files1 = gather_top_level_files(COSMO_DIR, INCLUDE_PATTERNS, SKIP_SUBDIRS)
    for f in files1:
        shutil.copy2(f, tmpdir / f.name)

    all_files = list(tmpdir.iterdir())
    print(f"Files to upload: {len(all_files)}")
    for f in sorted(all_files):
        print(f"  {f.name} ({f.stat().st_size} bytes)")

    result1 = upload_folder(
        folder_path=str(tmpdir),
        repo_id=DATASET1_ID,
        repo_type="dataset",
        token=token,
        commit_message=f"Upload P1B MCMC diagnostics ({PAPER_VERSION})",
    )
    print(f"Upload result: {result1}")


# ─── Dataset 2: p1b-namaster-artifacts ─────────────────────────────────────

DATASET2_ID = "bamfai/p1b-namaster-artifacts"
NAMASTER_DIR = BASE / "reproducibility" / "p1_namaster_500mc"

readme2 = f"""---
license: {LICENSE}
language:
- en
pretty_name: "P1B NaMaster Pipeline Artifacts (500 MC realizations)"
size_categories:
- n<1K
task_categories:
- other
tags:
- cosmology
- namaster
- power-spectrum
- monte-carlo
- big-bounce
- reproducibility
- cmb
---

# P1B NaMaster Pipeline Artifacts

**Title:** NaMaster pipeline artifacts (mask, MC seeds, output spectra)

## Description

This dataset contains the complete NaMaster pipeline reproducibility artifacts for
the 500 Monte Carlo realizations used in P1B's power-spectrum null tests.
It corresponds to **Appendix A, item 2** of the paper
"P1B — Technical Verification Companion to the ECH Spin-Torsion Program" ({PAPER_VERSION}).

Files include output spectra in JSON format, analysis and plotting scripts (Python),
and a requirements.txt pinning the exact software environment. The 500-MC results
fully document the null test methodology described in Appendix A.

## Provenance

- **Paper:** P1B — Technical Verification Companion to the ECH Spin-Torsion Program ({PAPER_VERSION})
- **GitHub:** [github.com/Hubify-Projects/bigbounce](https://github.com/Hubify-Projects/bigbounce)
- **Reproducibility directory:** `reproducibility/p1_namaster_500mc/`
- **Appendix A item:** 2 — NaMaster pipeline artifacts (mask, MC seeds, output spectra)
- **Paper PDF:** [bigbounce.hubify.app](https://bigbounce.hubify.app)
"""

print("\n=== Dataset 2: p1b-namaster-artifacts ===")
api.create_repo(repo_id=DATASET2_ID, repo_type="dataset", private=False, exist_ok=True)
print(f"Repo created/confirmed: {DATASET2_ID}")

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    # Copy entire directory tree
    shutil.copytree(str(NAMASTER_DIR), str(tmpdir / "p1_namaster_500mc"))
    # Write README at root
    (tmpdir / "README.md").write_text(readme2)

    all_files = []
    for f in tmpdir.rglob("*"):
        if f.is_file():
            all_files.append(f)
    print(f"Files to upload: {len(all_files)}")
    for f in sorted(all_files):
        print(f"  {f.relative_to(tmpdir)} ({f.stat().st_size} bytes)")

    result2 = upload_folder(
        folder_path=str(tmpdir),
        repo_id=DATASET2_ID,
        repo_type="dataset",
        token=token,
        commit_message=f"Upload P1B NaMaster artifacts ({PAPER_VERSION})",
    )
    print(f"Upload result: {result2}")


# ─── Dataset 3: p1b-alp-chains ─────────────────────────────────────────────

DATASET3_ID = "bamfai/p1b-alp-chains"
ALP_DIR = BASE / "research" / "branch_R_alp_birefringence" / "phase2_mcmc"

readme3 = f"""---
license: {LICENSE}
language:
- en
pretty_name: "P1B ALP Parameter MCMC Chains (birefringence)"
size_categories:
- n<1K
task_categories:
- other
tags:
- cosmology
- alp
- axion
- birefringence
- mcmc
- big-bounce
- reproducibility
- cmb-polarization
---

# P1B ALP Parameter MCMC Chains

**Title:** ALP parameter MCMC chains

## Description

This dataset contains the Axion-Like Particle (ALP) birefringence MCMC chain files
and supporting theory/likelihood scripts used in P1B's ALP constraint analysis.
It corresponds to **Appendix A, item 3** of the paper
"P1B — Technical Verification Companion to the ECH Spin-Torsion Program" ({PAPER_VERSION}).

Contents:
- **chains/** — MCMC chain `.txt` files for runs c14 (costheta), c5 (continuous),
  run1/run2/run3 (baseline/extended), plus associated `.covmat`, `.yaml`, `.progress`
  files and summary plots (`.png`)
- **Theory scripts** — `alp_theory.py`, `beta_free_theory.py`, `birefringence_lk.py`
- **Result JSONs** — `c10a_spectator_slice.json`, `c10b_alp_envelope_scan.json`
- **Priors documentation** — `04_priors_and_ranges.md`

## Provenance

- **Paper:** P1B — Technical Verification Companion to the ECH Spin-Torsion Program ({PAPER_VERSION})
- **GitHub:** [github.com/Hubify-Projects/bigbounce](https://github.com/Hubify-Projects/bigbounce)
- **Source directory:** `research/branch_R_alp_birefringence/phase2_mcmc/`
- **Appendix A item:** 3 — ALP parameter MCMC chains
- **Paper PDF:** [bigbounce.hubify.app](https://bigbounce.hubify.app)
"""

print("\n=== Dataset 3: p1b-alp-chains ===")
api.create_repo(repo_id=DATASET3_ID, repo_type="dataset", private=False, exist_ok=True)
print(f"Repo created/confirmed: {DATASET3_ID}")

# Files to upload:
# - chains/ directory (all subdirs with *.txt chain files)
# - c10a_spectator_slice.json, c10b_alp_envelope_scan.json
# - alp_theory.py, beta_free_theory.py, birefringence_lk.py
# - 04_priors_and_ranges.md

ALP_SPECIFIC_FILES = [
    "c10a_spectator_slice.json",
    "c10b_alp_envelope_scan.json",
    "alp_theory.py",
    "beta_free_theory.py",
    "birefringence_lk.py",
    "04_priors_and_ranges.md",
]

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    # Copy chains dir
    shutil.copytree(str(ALP_DIR / "chains"), str(tmpdir / "chains"))
    # Copy specific files
    for fname in ALP_SPECIFIC_FILES:
        src = ALP_DIR / fname
        if src.exists():
            shutil.copy2(str(src), str(tmpdir / fname))
        else:
            print(f"  WARNING: {fname} not found at {src}")
    # Write README
    (tmpdir / "README.md").write_text(readme3)

    all_files = []
    for f in tmpdir.rglob("*"):
        if f.is_file():
            all_files.append(f)
    total_size = sum(f.stat().st_size for f in all_files)
    print(f"Files to upload: {len(all_files)}, total: {total_size/1024/1024:.1f} MB")
    for f in sorted(all_files):
        print(f"  {f.relative_to(tmpdir)} ({f.stat().st_size} bytes)")

    result3 = upload_folder(
        folder_path=str(tmpdir),
        repo_id=DATASET3_ID,
        repo_type="dataset",
        token=token,
        commit_message=f"Upload P1B ALP birefringence chains ({PAPER_VERSION})",
    )
    print(f"Upload result: {result3}")


# ─── Verification ───────────────────────────────────────────────────────────

print("\n=== Verification ===")
import subprocess

for dataset_id in [DATASET1_ID, DATASET2_ID, DATASET3_ID]:
    name = dataset_id.split("/")[1]
    url = f"https://huggingface.co/datasets/{dataset_id}"

    # HTTP check
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
        capture_output=True, text=True
    )
    http_code = r.stdout.strip()

    # File count
    try:
        files = api.list_repo_files(dataset_id, repo_type="dataset")
        file_list = list(files)
        file_count = len(file_list)
    except Exception as e:
        file_count = f"ERROR: {e}"
        file_list = []

    print(f"\n{dataset_id}:")
    print(f"  URL: {url}")
    print(f"  HTTP: {http_code}")
    print(f"  Files: {file_count}")
    for f in sorted(file_list):
        print(f"    {f}")

print("\n=== Done ===")
print(f"License used: {LICENSE}")
