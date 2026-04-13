#!/bin/bash
LOG=/root/logs/chain6.log
mkdir -p /root/logs
echo "=== CHAIN6 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  python3 -u /root/experiments/${name}.py >> $LOG 2>&1
  echo "=== [$(date)] DONE: $name (exit $?)" >> $LOG
  return 0
}

# 3x bigae_production training cycles (now with fixed summary saving)
run_one bigae_production
run_one bigae_production
run_one bigae_production

# Plus heavy iterations of the working scripts
for i in 1 2 3 4 5 6; do
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder
  run_one anomaly_lightcurve_sim
done

# Final bigae_production
run_one bigae_production

echo "=== CHAIN6 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain6_complete.flag
