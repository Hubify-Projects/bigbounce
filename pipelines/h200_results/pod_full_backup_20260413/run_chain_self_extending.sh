#!/bin/bash
# Self-extending chain — runs forever until killed.
# Each iteration runs experiments, then loops back.
LOG=/root/logs/chain_loop.log
mkdir -p /root/logs
ITER=1

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=== [$(date)] iter=$ITER RUNNING: $name" >> $LOG
  timeout 600 python3 -u /root/experiments/${name}.py >> $LOG 2>&1
  echo "=== [$(date)] iter=$ITER DONE: $name (exit $?)" >> $LOG
  return 0
}

echo "=== SELF-EXTENDING CHAIN START $(date) ===" > $LOG

while true; do
  echo "" >> $LOG
  echo "########### ITERATION $ITER START $(date) ###########" >> $LOG

  run_one bigae_production
  run_one second_level_autoencoder
  run_one dyson_sphere
  run_one frb_chime
  run_one emission_line_finder

  echo "########### ITERATION $ITER END $(date) ###########" >> $LOG
  ITER=$((ITER+1))
done
