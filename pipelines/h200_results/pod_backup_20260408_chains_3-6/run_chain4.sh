#!/bin/bash
LOG=/root/logs/chain4.log
mkdir -p /root/logs

while [ ! -f /root/logs/chain3_complete.flag ]; do
  sleep 15
done

echo "=== CHAIN4 START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  python3 -u /root/experiments/${name}.py >> $LOG 2>&1
  echo "=== [$(date)] DONE: $name (exit $?)" >> $LOG
  return 0
}

# Run bigae_production again with different config (could re-train with more epochs)
run_one bigae_production
run_one bigae_production
run_one bigae_production

# Plus more iterations
for i in 1 2 3 4 5; do
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder
done

echo "=== CHAIN4 COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain4_complete.flag
