#!/bin/bash
# launch_pod3.sh -- waits for cobaya install to finish, then dispatches MCMC
# Run on Pod 3 H200: bash launch_pod3.sh > launch.log 2>&1 &

set -u
cd /workspace/quintom_dr2

# 1. Wait for install to finish
echo "[$(date)] Waiting for COSMO_INSTALL_OK in install.log..."
while ! grep -q "COSMO_INSTALL_OK" install.log 2>/dev/null; do
  sleep 30
  if grep -qi "error\|failed\|traceback" install.log 2>/dev/null; then
    if ! grep -q "COSMO_INSTALL_OK" install.log; then
      echo "[$(date)] install.log shows errors but no OK marker -- inspecting:"
      tail -40 install.log
    fi
  fi
done
echo "[$(date)] Install complete."

# 2. Verify DESI DR2 likelihood is available; fall back to DR1 if not
python3 - <<'PY'
import sys
try:
    import cobaya
    from cobaya.likelihoods.bao import desi_dr2
    print("DESI DR2 OK")
    sys.exit(0)
except Exception as e:
    print(f"DESI DR2 unavailable: {e}; will fallback to DR1")
    sys.exit(1)
PY
DR2_OK=$?

if [ $DR2_OK -ne 0 ]; then
  echo "[$(date)] Patching config: DESI DR2 -> DESI DR1 (bao.desi_2024.bao_all)"
  sed -i 's|bao.desi_dr2.desi_bao_all|bao.desi_2024.bao_all|' cobaya_config.yaml
fi

# 3. Verify DES-SN5YR available; fall back to Pantheon+ only if not
python3 - <<'PY' 2>&1
try:
    from cobaya.likelihoods.sn import des_y5
    print("DES-SN5YR OK")
except Exception as e:
    print(f"DES-SN5YR unavailable: {e}")
PY

# 4. Set MPI environment for 4 chains
export OMP_NUM_THREADS=8

# 5. Launch the MCMC in background under nohup
echo "[$(date)] Launching cobaya-run with mpirun -n 4..."
nohup mpirun -n 4 --allow-run-as-root cobaya-run cobaya_config.yaml --packages-path /workspace/quintom_dr2/packages > mcmc.log 2>&1 &
echo $! > mcmc.pid
echo "[$(date)] MCMC PID: $(cat mcmc.pid)"

# 6. Tail the log briefly so we know it actually started
sleep 30
echo "=== first 40 lines of mcmc.log ==="
head -40 mcmc.log
