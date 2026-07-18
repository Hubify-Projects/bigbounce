#!/usr/bin/env bash
# pod_bootstrap_sshd.sh — bring up clean direct SSH on a resumed RunPod pod whose
# container came back with NO host keys and an empty PUBLIC_KEY env (so the
# template sshd exited: "no hostkeys available -- exiting", direct port refused).
#
# It reaches the pod through RunPod's proxy relay (which does NOT need the
# container sshd), generates host keys, installs your local pubkey, and starts
# /usr/sbin/sshd so the direct TCP port opens for scp/rsync/ssh.
#
# Usage: PROXY=<podId>-<pubkeyid>@ssh.runpod.io ./pod_bootstrap_sshd.sh
#   e.g. PROXY=580dgszgib3ti4-644119b0@ssh.runpod.io ./pod_bootstrap_sshd.sh
#
# The RunPod proxy shell is INTERACTIVE and ignores ssh command args — commands
# must be piped on stdin (the -tt + printf pattern below).
set -euo pipefail
PROXY="${PROXY:?set PROXY=<podId>-<pubkeyid>@ssh.runpod.io}"
MYPUB="$(cat "$HOME/.ssh/id_ed25519.pub")"
printf 'ssh-keygen -A 2>&1 | tail -1\nmkdir -p ~/.ssh /run/sshd; chmod 700 ~/.ssh\necho "%s" > ~/.ssh/authorized_keys; chmod 600 ~/.ssh/authorized_keys\n/usr/sbin/sshd && echo SSHD_STARTED\nsleep 2\nss -tlnp 2>/dev/null | grep :22 && echo PORT22_UP || echo PORT22_DOWN\necho MARKER_END\nexit\n' "$MYPUB" \
  | timeout 60 ssh -tt -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
        -o ConnectTimeout=25 -i "$HOME/.ssh/id_ed25519" "$PROXY"
