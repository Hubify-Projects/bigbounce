#!/bin/bash
LOG=/root/logs/chain5.log
mkdir -p /root/logs
echo "=== CHAIN5 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  python3 -u /root/experiments/${name}.py >> $LOG 2>&1
  echo "=== [$(date)] DONE: $name (exit $?)" >> $LOG
  return 0
}

run_one bigae_production
for i in 1 2 3 4 5; do
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder
done
run_one bigae_production
run_one bigae_production

echo "=== CHAIN5 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain5_complete.flag
