#!/bin/bash
# accurate counts: identify workers by /proc/<pid>/exe (torch renames comm), exclude self
real=0; declare -A ranges
for p in $(pgrep -f -- "run_scan.py"); do
  exe=$(readlink /proc/$p/exe 2>/dev/null)
  case "$exe" in *python*) real=$((real+1)); r=$(tr "\0" " " < /proc/$p/cmdline | grep -oE -- "--start [0-9]+" | head -1); ranges["$r"]=$(( ${ranges["$r"]:-0} + 1 ));; esac
done
echo "real-python-workers: $real"
for r in "${!ranges[@]}"; do [ "${ranges[$r]}" -gt 1 ] && echo "DUP: $r x${ranges[$r]}"; done
echo "shards: $(ls /workspace/shards 2>/dev/null | wc -l)"
