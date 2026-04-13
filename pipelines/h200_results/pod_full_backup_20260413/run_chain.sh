#!/bin/bash
LOG=/root/logs/chain.log
mkdir -p /root/logs
echo "=== CHAIN START $(date) ===" > $LOG

run_one() {
  local name=$1
  echo "" >> $LOG
  echo "=========================================" >> $LOG
  echo "=== [$(date)] RUNNING: $name" >> $LOG
  echo "=========================================" >> $LOG
  python3 /root/experiments/${name}.py >> $LOG 2>&1
  local rc=$?
  echo "=== [$(date)] DONE: $name (exit $rc)" >> $LOG
  return 0  # always continue chain
}

run_one desi_transformer
run_one multi_modal_joint
run_one second_level_autoencoder
run_one dyson_sphere
run_one frb_chime
run_one gw_echo_ligo
run_one emission_line_finder
run_one anomaly_lightcurve_sim
run_one ztf_dr21
run_one sdss_native_autoencoder

echo "" >> $LOG
echo "=== CHAIN COMPLETE $(date) ===" >> $LOG
touch /root/logs/chain_complete.flag
