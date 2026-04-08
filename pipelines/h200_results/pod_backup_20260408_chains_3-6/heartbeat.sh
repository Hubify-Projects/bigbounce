#!/bin/bash
LOG=/root/logs/heartbeat.log
while true; do
  echo "=== $(date) ===" >> $LOG
  nvidia-smi --query-gpu=utilization.gpu,memory.used,temperature.gpu --format=csv,noheader >> $LOG
  echo "tmux:" >> $LOG
  tmux ls 2>&1 >> $LOG
  echo "active python:" >> $LOG
  ps aux | grep -E "python.*experiment" | grep -v grep | wc -l >> $LOG
  echo "" >> $LOG
  sleep 300
done
