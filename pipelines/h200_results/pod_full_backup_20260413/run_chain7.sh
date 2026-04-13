#!/bin/bash
LOG=/root/logs/chain7.log
mkdir -p /root/logs
echo "=== CHAIN7 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  timeout 600 python3 -u /root/experiments/${name}.py >> $LOG 2>&1
  echo "=== [$(date)] DONE: $name (exit $?)" >> $LOG
  return 0
}

# 100K spectra bigae_production (5x smaller = should finish in ~2 min)
run_one bigae_production
# Quick iterations
for i in 1 2 3; do
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder
done
run_one bigae_production

echo "=== CHAIN7 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain7_complete.flag
