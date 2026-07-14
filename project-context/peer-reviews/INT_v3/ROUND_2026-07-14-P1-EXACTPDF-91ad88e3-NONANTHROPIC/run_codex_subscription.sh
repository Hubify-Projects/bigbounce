#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

run_paper() {
  local paper="$1"
  local frozen="$ROOT/$paper/frozen"
  local raw="$ROOT/$paper/raw"
  local prompt="$raw/PROMPT_Codex_GPT56Sol.txt"
  local images=("$ROOT/$paper/rendered"/page-*.png)
  local image_args=()
  local image
  for image in "${images[@]}"; do
    image_args+=(--image "$image")
  done

  codex exec \
    --ephemeral \
    --ignore-user-config \
    --ignore-rules \
    --model gpt-5.6-sol \
    --config 'model_reasoning_effort="high"' \
    --sandbox read-only \
    --cd "$frozen" \
    --json \
    --output-last-message "$raw/P1EXACT91ad88e3_${paper}_Codex_GPT56Sol.md" \
    "${image_args[@]}" \
    - < "$prompt" > "$raw/P1EXACT91ad88e3_${paper}_Codex_GPT56Sol.events.jsonl" 2> "$raw/P1EXACT91ad88e3_${paper}_Codex_GPT56Sol.stderr.log"
}

run_paper P1A &
p1a_pid=$!
run_paper P1B &
p1b_pid=$!

p1a_status=0
p1b_status=0
wait "$p1a_pid" || p1a_status=$?
wait "$p1b_pid" || p1b_status=$?

printf 'P1A=%s\nP1B=%s\n' "$p1a_status" "$p1b_status"
test "$p1a_status" -eq 0
test "$p1b_status" -eq 0
