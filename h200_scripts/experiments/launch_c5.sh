#!/usr/bin/env bash
# C5 launch script — P1B Cagamma continuous-grid MCMC (prior [4,60])
# Run ON THE POD inside tmux session "c5".
# Pipeline ground truth: research/branch_R_alp_birefringence/phase2_mcmc/
# (Cobaya 3.6.1 + custom ALP theory/likelihood; NO Planck/CAMB downloads needed
#  — the likelihood is the Gaussian summary on beta = 0.342 +/- 0.094 deg.)
set -uo pipefail

cd /workspace/c5
mkdir -p /workspace/c5_results

NPROC=$(nproc)
# Likelihood eval is a single scipy ODE solve (~ms); cap OMP threads to avoid
# oversubscription, MCMC is serial per chain anyway.
export OMP_NUM_THREADS=4
echo "[c5] nproc=${NPROC} OMP_NUM_THREADS=${OMP_NUM_THREADS}"
echo "[c5] cobaya version: $(python3 -c 'import cobaya; print(cobaya.__version__)')"

# Prefer 4 MPI chains (proper multi-chain R-1) if mpi4py + mpirun are available;
# fall back to single-chain (cobaya computes intra-chain R-1 from segments).
if python3 -c "import mpi4py" 2>/dev/null && command -v mpirun >/dev/null 2>&1; then
    echo "[c5] launching 4 MPI chains"
    exec mpirun --allow-run-as-root -n 4 \
        cobaya-run -r /workspace/c5/c5_cagamma_continuous.yaml
else
    echo "[c5] mpi4py/mpirun unavailable — launching single chain (resume-safe)"
    exec cobaya-run -r /workspace/c5/c5_cagamma_continuous.yaml
fi
