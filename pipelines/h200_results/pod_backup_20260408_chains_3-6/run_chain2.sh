#!/bin/bash
LOG=/root/logs/chain2.log
mkdir -p /root/logs

# Wait for chain1 to finish
while [ ! -f /root/logs/chain_complete.flag ]; do
  sleep 10
done

echo "=== CHAIN2 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=========================================" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  echo "=========================================" >> $LOG
  python3 /root/experiments/${name}.py >> $LOG 2>&1
  local rc=$?
  echo "=== [$(date)] DONE: $name (exit $rc)" >> $LOG
  return 0
}

# BIG one first - production training (~30-60 min)
run_one bigae_production

# Re-run with successful patches from chain1
run_one second_level_autoencoder
run_one dyson_sphere
run_one frb_chime
run_one emission_line_finder
run_one anomaly_lightcurve_sim
run_one ztf_dr21
run_one sdss_native_autoencoder

# Plus repeats with different seeds
for i in 1 2 3; do
  run_one second_level_autoencoder
  run_one dyson_sphere
done

echo "" >> $LOG
echo "=== CHAIN2 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain2_complete.flag
