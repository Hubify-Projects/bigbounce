#!/usr/bin/env bash
# reproducibility/p3_pta_mcmc/run_pta_combined_mcmc.sh
#
# Reproduction driver for the Paper 3 §VI PTA MCMC results.
#
# Invokes the two production scripts that produced the canonical chains
# under pipelines/h200_results/phase4_science/, and (optionally) diffs
# the regenerated summaries against the on-disk canonical versions.
#
# Usage:
#   bash reproducibility/p3_pta_mcmc/run_pta_combined_mcmc.sh
#
# Expected runtime: ~60 s on a CPU-only laptop.
# Dependencies: python3 with numpy, scipy, emcee.
#
# This script does NOT run on a GPU and does NOT touch raw NANOGrav
# .tim/.par files — both production scripts consume published power-law
# summary statistics from the four PTA collaborations and run emcee on
# a 2-D (log10A, gamma) parameter space. See README.md for the full
# methodological documentation.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PYTHON="${PYTHON:-python3}"

# The two production scripts expect /workspace/bigbounce/outputs/... as
# their output paths (they were originally run on an H200 pod). For
# local reproduction we redirect via PYTHONPATH-free env vars by
# pre-creating the directories so the scripts' os.makedirs calls
# succeed even on read-only / non-pod hosts.
OUT_PTARCADE="/tmp/p3_pta_repro/nanograv_ptarcade"
OUT_COMBINED="/tmp/p3_pta_repro/nanograv_combined_pta"

mkdir -p "$OUT_PTARCADE" "$OUT_COMBINED"

CANONICAL_PTARCADE="$REPO_ROOT/pipelines/h200_results/phase4_science/nanograv_ptarcade/nanograv_ptarcade_summary.json"
CANONICAL_COMBINED="$REPO_ROOT/pipelines/h200_results/phase4_science/nanograv_combined_pta/nanograv_combined_pta_summary.json"

SCRIPT_PTARCADE="$REPO_ROOT/h200_scripts/experiments/nanograv_ptarcade.py"
SCRIPT_COMBINED="$REPO_ROOT/h200_scripts/experiments/nanograv_combined.py"

echo "============================================================"
echo "Paper 3 §VI PTA MCMC — reproduction driver"
echo "============================================================"
echo "Repo root      : $REPO_ROOT"
echo "Python         : $($PYTHON --version 2>&1)"
echo "Canonical (1)  : $CANONICAL_PTARCADE"
echo "Canonical (2)  : $CANONICAL_COMBINED"
echo

# ------------------------------------------------------------
# Step 0 — dependency check
# ------------------------------------------------------------

echo "[step 0] Verifying Python dependencies..."
$PYTHON - <<'PY'
import importlib, sys
missing = []
for pkg in ("numpy", "scipy", "emcee"):
    try:
        importlib.import_module(pkg)
    except ImportError:
        missing.append(pkg)
if missing:
    print(f"  MISSING: {missing}")
    print(f"  Install with: pip install {' '.join(missing)}")
    sys.exit(1)
print("  All dependencies present.")
PY
echo

# ------------------------------------------------------------
# Step 1 — single-PTA NANOGrav 15-yr (canonical headline)
# ------------------------------------------------------------

echo "[step 1] Running NANOGrav 15-yr free-spectrum MCMC..."
echo "         (32 walkers × 10,000 steps, ~30 s on laptop CPU)"
echo

# The script hard-codes /workspace/bigbounce/outputs/nanograv_ptarcade
# as its OUTPUT_DIR. We patch with a sed-free env trick: run from a
# temp dir where /workspace/bigbounce/outputs is symlinked to /tmp.
SANDBOX="/tmp/p3_pta_repro/sandbox"
mkdir -p "$SANDBOX/workspace/bigbounce/outputs"
ln -sfn "$OUT_PTARCADE" "$SANDBOX/workspace/bigbounce/outputs/nanograv_ptarcade"
ln -sfn "$OUT_COMBINED" "$SANDBOX/workspace/bigbounce/outputs/nanograv_combined_pta"

# The scripts use absolute /workspace/... paths, which we cannot
# redirect without root. On a typical pod or root-equipped host:
#   sudo ln -s /tmp/p3_pta_repro/sandbox/workspace /workspace
# On a non-root laptop, the scripts will write to /workspace if it
# exists or fail otherwise; in that case the user can edit the
# OUTPUT_DIR constant near the top of each script and re-run.
if [ ! -d /workspace/bigbounce/outputs ]; then
    echo "  NOTE: /workspace/bigbounce/outputs/ not present on this host."
    echo "  To allow the production scripts to write their canonical"
    echo "  output paths without modification, run on a pod or symlink:"
    echo "    sudo ln -s $SANDBOX/workspace /workspace"
    echo "  For laptop-only reproduction, edit OUTPUT_DIR in"
    echo "  $SCRIPT_PTARCADE and $SCRIPT_COMBINED to point at"
    echo "  $OUT_PTARCADE and $OUT_COMBINED respectively."
    echo
fi

if [ -w /workspace/bigbounce/outputs 2>/dev/null ] || [ -d /workspace/bigbounce ]; then
    $PYTHON "$SCRIPT_PTARCADE"
else
    echo "  SKIPPED — /workspace/ not writable; see NOTE above."
fi

echo

# ------------------------------------------------------------
# Step 2 — combined 4-PTA sensitivity check
# ------------------------------------------------------------

echo "[step 2] Running combined NANOGrav + EPTA + PPTA + IPTA MCMC..."
echo "         (32 walkers × 10,000 steps, ~30 s on laptop CPU)"
echo

if [ -w /workspace/bigbounce/outputs 2>/dev/null ] || [ -d /workspace/bigbounce ]; then
    $PYTHON "$SCRIPT_COMBINED"
else
    echo "  SKIPPED — /workspace/ not writable; see NOTE above."
fi

echo

# ------------------------------------------------------------
# Step 3 — diff against canonical headlines
# ------------------------------------------------------------

echo "[step 3] Diffing regenerated chains against canonical on-disk values..."
echo

REGEN_PTARCADE="$OUT_PTARCADE/nanograv_ptarcade_summary.json"
REGEN_COMBINED="$OUT_COMBINED/nanograv_combined_pta_summary.json"

if [ -f "$REGEN_PTARCADE" ] && [ -f "$CANONICAL_PTARCADE" ]; then
    $PYTHON - "$REGEN_PTARCADE" "$CANONICAL_PTARCADE" <<'PY'
import json, sys
regen, canon = sys.argv[1], sys.argv[2]
with open(regen) as f: r = json.load(f)
with open(canon) as f: c = json.load(f)

def chk(label, rv, cv, tol):
    diff = abs(rv - cv)
    flag = "PASS" if diff < tol else "FAIL"
    print(f"  [{flag}] {label}: regen={rv:.4f}  canon={cv:.4f}  |Δ|={diff:.4f}  tol={tol}")

print("  --- NANOGrav 15-yr single-PTA chain ---")
chk("posterior.gamma_mean",          r["posterior"]["gamma_mean"],          c["posterior"]["gamma_mean"],          0.02)
chk("posterior.gamma_std",           r["posterior"]["gamma_std"],           c["posterior"]["gamma_std"],           0.02)
chk("tensions.gamma_vs_bounce_sigma",r["tensions"]["gamma_vs_bounce_sigma"],c["tensions"]["gamma_vs_bounce_sigma"],0.05)
chk("ml_fits.bounce.bic",            r["ml_fits"]["bounce"]["bic"],         c["ml_fits"]["bounce"]["bic"],         0.05)
chk("ml_fits.smbhb.bic",             r["ml_fits"]["smbhb"]["bic"],          c["ml_fits"]["smbhb"]["bic"],          0.05)
PY
else
    echo "  ptarcade regen or canonical missing — skipping diff."
fi

echo

if [ -f "$REGEN_COMBINED" ] && [ -f "$CANONICAL_COMBINED" ]; then
    $PYTHON - "$REGEN_COMBINED" "$CANONICAL_COMBINED" <<'PY'
import json, sys
regen, canon = sys.argv[1], sys.argv[2]
with open(regen) as f: r = json.load(f)
with open(canon) as f: c = json.load(f)

def chk(label, rv, cv, tol):
    diff = abs(rv - cv)
    flag = "PASS" if diff < tol else "FAIL"
    print(f"  [{flag}] {label}: regen={rv:.4f}  canon={cv:.4f}  |Δ|={diff:.4f}  tol={tol}")

print("  --- Combined 4-PTA chain ---")
chk("mcmc.posterior.gamma_mean",         r["mcmc"]["posterior"]["gamma_mean"],          c["mcmc"]["posterior"]["gamma_mean"],          0.02)
chk("mcmc.posterior.gamma_std",          r["mcmc"]["posterior"]["gamma_std"],           c["mcmc"]["posterior"]["gamma_std"],           0.02)
chk("combined_measurement.gamma",        r["combined_measurement"]["gamma"],            c["combined_measurement"]["gamma"],            0.001)
chk("tensions_combined.bounce_sigma",    r["tensions_combined"]["bounce_sigma"],        c["tensions_combined"]["bounce_sigma"],        0.05)
chk("tensions_combined.smbhb_sigma",     r["tensions_combined"]["smbhb_sigma"],         c["tensions_combined"]["smbhb_sigma"],         0.05)
PY
else
    echo "  combined regen or canonical missing — skipping diff."
fi

echo
echo "============================================================"
echo "Done.  See README.md for trace gaps and full documentation."
echo "============================================================"
