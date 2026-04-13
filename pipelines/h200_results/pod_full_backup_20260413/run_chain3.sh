#!/bin/bash
LOG=/root/logs/chain3.log
mkdir -p /root/logs

# Wait for chain2 to finish
while [ ! -f /root/logs/chain2_complete.flag ]; do
  sleep 10
done

echo "=== CHAIN3 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  python3 /root/experiments/${name}.py >> $LOG 2>&1
  local rc=$?
  echo "=== [$(date)] DONE: $name (exit $rc)" >> $LOG
  return 0
}

# THE BIG ONE
run_one bigae_production

# Then heavy retraining iterations of working scripts
for i in 1 2 3 4 5; do
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder
  run_one anomaly_lightcurve_sim
done

echo "=== CHAIN3 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain3_complete.flag
