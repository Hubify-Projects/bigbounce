#!/bin/bash
# Paper-1 Clean Restart — Chain Launcher
# Launches Cobaya MCMC chains in priority order with resource management.
#
# Usage:
#   bash paper1_launch_chains.sh [phase]
#   phase 1: full_tension ΔNeff only (4 chains)
#   phase 2: all ΔNeff datasets (16 chains)
#   phase 3: ΛCDM controls (16 chains)
#   phase all: everything (32 chains)

set -euo pipefail

CANONICAL="/workspace/bigbounce/reproducibility/cosmology/canonical_run_001"
LOGDIR="/workspace/logs/cobaya"
PHASE="${1:-1}"
NCPU=$(nproc)

export COBAYA_PACKAGES_PATH=/workspace/cobaya_packages

echo "=========================================="
echo "Paper-1 Chain Launcher — Phase $PHASE"
echo "Date: $(date -u)"
echo "CPUs: $NCPU"
echo "=========================================="

launch_chain() {
    local model="$1"
    local dataset="$2"
    local chain_num="$3"
    local chain_dir="$CANONICAL/$model/$dataset/chain_$(printf '%02d' $chain_num)"
    local config="$chain_dir/cobaya_config.yaml"
    local logfile="$LOGDIR/${model}_${dataset}_chain$(printf '%02d' $chain_num).log"

    if [ ! -f "$config" ]; then
        echo "  ERROR: Config not found: $config"
        return 1
    fi

    # Set OMP threads based on available CPUs and expected concurrency
    local omp_threads=2
    if [ "$NCPU" -ge 32 ]; then
        omp_threads=4
    elif [ "$NCPU" -ge 16 ]; then
        omp_threads=2
    else
        omp_threads=1
    fi

    echo "  Launching $model/$dataset/chain_$(printf '%02d' $chain_num) (OMP_NUM_THREADS=$omp_threads)"

    OMP_NUM_THREADS=$omp_threads \
    nohup cobaya-run "$config" \
        > "$logfile" 2>&1 &

    echo $! > "$chain_dir/cobaya.pid"
    echo "    PID: $! → log: $logfile"
}

verify_chain() {
    local model="$1"
    local dataset="$2"
    local chain_num="$3"
    local chain_dir="$CANONICAL/$model/$dataset/chain_$(printf '%02d' $chain_num)"
    local prefix="spin_torsion"
    [ "$model" = "lcdm" ] && prefix="lcdm"
    local chain_file="$chain_dir/${prefix}.1.txt"

    if [ -f "$chain_dir/cobaya.pid" ]; then
        local pid=$(cat "$chain_dir/cobaya.pid")
        if kill -0 "$pid" 2>/dev/null; then
            local samples=0
            if [ -f "$chain_file" ]; then
                samples=$(wc -l < "$chain_file" | tr -d ' ')
            fi
            echo "  ✓ $model/$dataset/chain_$(printf '%02d' $chain_num) — PID $pid alive, $samples samples"
            return 0
        else
            echo "  ✗ $model/$dataset/chain_$(printf '%02d' $chain_num) — PID $pid DEAD"
            return 1
        fi
    else
        echo "  ? $model/$dataset/chain_$(printf '%02d' $chain_num) — no PID file"
        return 1
    fi
}

# Phase 1: full_tension ΔNeff only
if [ "$PHASE" = "1" ] || [ "$PHASE" = "all" ]; then
    echo ""
    echo "--- Phase 1: full_tension ΔNeff (4 chains) ---"
    for c in 1 2 3 4; do
        launch_chain "dneff" "full_tension" "$c"
    done
    echo ""
    echo "Waiting 60s for chains to start writing..."
    sleep 60
    echo ""
    echo "--- Verification ---"
    for c in 1 2 3 4; do
        verify_chain "dneff" "full_tension" "$c"
    done
fi

# Phase 2: remaining ΔNeff datasets
if [ "$PHASE" = "2" ] || [ "$PHASE" = "all" ]; then
    echo ""
    echo "--- Phase 2: remaining ΔNeff datasets (12 chains) ---"
    for ds in planck_bao_sn planck_bao planck_only; do
        for c in 1 2 3 4; do
            launch_chain "dneff" "$ds" "$c"
        done
    done
fi

# Phase 3: ΛCDM controls
if [ "$PHASE" = "3" ] || [ "$PHASE" = "all" ]; then
    echo ""
    echo "--- Phase 3: ΛCDM controls (16 chains) ---"
    for ds in full_tension planck_bao_sn planck_bao planck_only; do
        for c in 1 2 3 4; do
            launch_chain "lcdm" "$ds" "$c"
        done
    done
fi

echo ""
echo "=========================================="
echo "Launch complete: $(date -u)"
echo "Running Cobaya processes: $(pgrep -c cobaya-run 2>/dev/null || echo 0)"
echo "=========================================="
