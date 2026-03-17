#!/usr/bin/env bash
# compile_on_pod.sh — Compile main.tex on a remote Linux machine via SSH
#
# Usage: ./compile_on_pod.sh [HOST] [PORT] [USER]
#   Defaults: HOST=157.157.221.30  PORT=36579  USER=root
#
# Prerequisites on the remote: texlive-latex-extra texlive-publishers
#   texlive-fonts-recommended texlive-science texlive-fonts-extra
#
# Installs missing packages automatically if apt is available.

set -euo pipefail

HOST="${1:-157.157.221.30}"
PORT="${2:-36579}"
USER="${3:-root}"
REMOTE_DIR="/root/arxiv_compile"
LOCAL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== BigBounce LaTeX Compilation Script ==="
echo "Remote: ${USER}@${HOST}:${PORT}"
echo "Local:  ${LOCAL_DIR}"

# 1. Ensure remote directory exists
ssh -o StrictHostKeyChecking=no -p "${PORT}" "${USER}@${HOST}" \
  "mkdir -p ${REMOTE_DIR}"

# 2. Copy arxiv/ to the remote
echo "--- Uploading arxiv/ to remote ---"
scp -o StrictHostKeyChecking=no -P "${PORT}" -r "${LOCAL_DIR}" \
  "${USER}@${HOST}:${REMOTE_DIR}/"

# 3. Install texlive if needed
echo "--- Checking / installing texlive ---"
ssh -o StrictHostKeyChecking=no -p "${PORT}" "${USER}@${HOST}" bash -s <<'INSTALL'
if ! command -v pdflatex &>/dev/null; then
  echo "pdflatex not found, installing texlive..."
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
    texlive-latex-extra texlive-publishers texlive-fonts-recommended \
    texlive-science texlive-fonts-extra
else
  echo "pdflatex already installed: $(which pdflatex)"
  # Check for bbold specifically
  if ! kpsewhich bbold.sty &>/dev/null; then
    echo "Installing texlive-fonts-extra for bbold.sty..."
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq texlive-fonts-extra
  fi
fi
INSTALL

# 4. Compile: pdflatex + bibtex + pdflatex x3 (safe for label convergence)
echo "--- Compiling ---"
ssh -o StrictHostKeyChecking=no -p "${PORT}" "${USER}@${HOST}" bash -s <<COMPILE
cd ${REMOTE_DIR}/arxiv_v2
rm -f main.aux main.bbl main.blg main.log main.pdf main.out

echo "Pass 1..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "BibTeX..."
bibtex main 2>&1 | grep -E "Warning|Error" || true

echo "Pass 2..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "Pass 3..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "Pass 4 (label convergence)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

# Check results
if [ -f main.pdf ]; then
  PAGES=\$(pdfinfo main.pdf 2>/dev/null | grep Pages | awk '{print \$2}' || echo "?")
  SIZE=\$(ls -lh main.pdf | awk '{print \$5}')
  echo "SUCCESS: main.pdf — \${PAGES} pages, \${SIZE}"

  # Check for remaining issues
  UNDEF=\$(grep -c "undefined" main.log 2>/dev/null || echo 0)
  echo "Undefined references: \${UNDEF}"
else
  echo "FAILED: no main.pdf produced"
  tail -30 main.log
  exit 1
fi
COMPILE

# 5. Copy PDF back
echo "--- Downloading PDF ---"
scp -o StrictHostKeyChecking=no -P "${PORT}" \
  "${USER}@${HOST}:${REMOTE_DIR}/arxiv_v2/main.pdf" "${LOCAL_DIR}/main.pdf"

echo "=== Done: ${LOCAL_DIR}/main.pdf ==="
