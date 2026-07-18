#!/usr/bin/env bash
# pod_ssh.sh — clean direct SSH into the G1 A4000 pod (580dgszgib3ti4).
# Direct sshd was bootstrapped this session (ssh-keygen -A + authorized_keys + /usr/sbin/sshd)
# because the resumed pod came up with no host keys and empty PUBLIC_KEY env.
# If the pod is stopped/resumed again, the direct port changes and sshd must be
# re-bootstrapped via the RunPod proxy: 580dgszgib3ti4-644119b0@ssh.runpod.io
# (see tools/pod_bootstrap_sshd.sh).
POD_HOST="${POD_HOST:-193.183.22.54}"
POD_PORT="${POD_PORT:-1206}"
exec ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
     -o ConnectTimeout=20 -o BatchMode=yes \
     -p "$POD_PORT" -i "$HOME/.ssh/id_ed25519" "root@$POD_HOST" "$@"
