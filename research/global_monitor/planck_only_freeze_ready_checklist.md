# Planck-Only Freeze-Ready Checklist

**Created:** 2026-03-12
**Status:** NOT READY — chains at ~2,360 samples, need ~10,000+ for convergence
**Estimated ready:** ~2026-03-19 (6-7 days from start)

---

## Pre-Freeze Gates (ALL must pass)

| # | Gate | Target | Current | Status |
|---|------|--------|---------|--------|
| 1 | Total accepted samples | ≥ 10,000 | ~2,360 | FAIL |
| 2 | Active chains | ≥ 4 | 6 | PASS |
| 3 | Worst R̂−1 (any parameter) | < 0.01 | ~0.71 | FAIL |
| 4 | Min ESS (any key parameter) | > 2,000 | ~45 | FAIL |
| 5 | Max drift (any key parameter) | < 0.1σ | ~0.70σ | FAIL |
| 6 | All chains actively writing | yes | yes | PASS |
| 7 | No NaN/inf in chain files | 0 | 0 | PASS |
| 8 | Cobaya logs error-free | yes | yes | PASS |
| 9 | Checkpoints current | < 1h old | yes | PASS |

---

## Freeze Execution Workflow (run when ALL gates pass)

### Step 1: Final Diagnostics
```bash
# SSH to pod
ssh -p <port> root@<pod-ip>

# Run convergence check
python3 /workspace/bigbounce/mcmc_monitor_v5.py --dataset planck_only --check-freeze

# Verify all 9 gates pass
```

### Step 2: Create Frozen Artifact Pack
```bash
FREEZE_TS=$(date -u +%Y%m%d_%H%M)
FREEZE_DIR=/workspace/bigbounce/frozen/planck_only_${FREEZE_TS}

mkdir -p ${FREEZE_DIR}/chains
mkdir -p ${FREEZE_DIR}/diagnostics

# Copy chain files (DO NOT move — keep originals until verified)
for i in 01 02 03 04 05 06; do
  CHAIN_DIR=/workspace/bigbounce/chains/dneff/planck_only/chain_${i}
  cp ${CHAIN_DIR}/spin_torsion.*.txt ${FREEZE_DIR}/chains/chain_${i}/
  cp ${CHAIN_DIR}/spin_torsion.*.checkpoint ${FREEZE_DIR}/chains/chain_${i}/ 2>/dev/null
  cp ${CHAIN_DIR}/spin_torsion.*.covmat ${FREEZE_DIR}/chains/chain_${i}/ 2>/dev/null
  cp ${CHAIN_DIR}/spin_torsion.*.progress ${FREEZE_DIR}/chains/chain_${i}/ 2>/dev/null
  cp ${CHAIN_DIR}/spin_torsion.*.input.yaml ${FREEZE_DIR}/chains/chain_${i}/ 2>/dev/null
  cp ${CHAIN_DIR}/spin_torsion.*.updated.yaml ${FREEZE_DIR}/chains/chain_${i}/ 2>/dev/null
done

# Copy cobaya config
cp /workspace/bigbounce/chains/dneff/planck_only/cobaya_config.yaml ${FREEZE_DIR}/ 2>/dev/null
```

### Step 3: Generate SHA256 Checksums
```bash
cd ${FREEZE_DIR}
find . -type f ! -name 'SHA256SUMS.txt' -exec sha256sum {} \; > SHA256SUMS.txt
echo "$(wc -l < SHA256SUMS.txt) files checksummed"
```

### Step 4: Create MANIFEST
```bash
cat > ${FREEZE_DIR}/MANIFEST.md << 'MANIFEST_EOF'
# Frozen Dataset: planck_only
# Freeze timestamp: ${FREEZE_TS} UTC
# Dataset: Planck 2018 NPIPE (CamSpec TTTEEE + lowl + lowE + lensing)
# Sampler: Cobaya v3.6.1, adaptive blocked Metropolis-Hastings
# Theory: CAMB v1.6.5 (stock, no modifications)
# Model: LCDM + delta_Neff
# Chains: 6
# Total samples: [FILL FROM DIAGNOSTICS]
# R-hat (worst): [FILL FROM DIAGNOSTICS]
# ESS (min): [FILL FROM DIAGNOSTICS]
MANIFEST_EOF
```

### Step 5: Generate Diagnostics Report
```bash
python3 -c "
# Run full convergence analysis and save to diagnostics/convergence_report.txt
# [Use same script as planck_bao_sn freeze]
" > ${FREEZE_DIR}/diagnostics/convergence_report.txt
```

### Step 6: Create Tarball
```bash
cd /workspace/bigbounce/frozen
tar czf planck_only_${FREEZE_TS}.tar.gz planck_only_${FREEZE_TS}/
sha256sum planck_only_${FREEZE_TS}.tar.gz > planck_only_${FREEZE_TS}.tar.gz.sha256
```

### Step 7: Sync to Local
```bash
# From LOCAL machine:
rsync -avz --progress -e "ssh -p 36579" \
  root@<pod-ip>:/workspace/bigbounce/frozen/planck_only_${FREEZE_TS}/ \
  /Users/houstongolden/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/frozen/planck_only_${FREEZE_TS}/

# Verify checksums locally
cd /Users/houstongolden/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/frozen/planck_only_${FREEZE_TS}/
sha256sum -c SHA256SUMS.txt
```

### Step 8: Stop Chains (only after local verification passes)
```bash
ssh -p <port> root@<pod-ip> "kill 8165 8166 8167 8168 8169 8170"
# Verify stopped:
ssh -p <port> root@<pod-ip> "ps aux | grep cobaya | grep -v grep"
```

### Step 9: Resume planck_bao
```bash
# Only after planck_only freeze is verified
ssh -p <port> root@<pod-ip> "cd /workspace/bigbounce/chains/dneff/planck_bao && nohup cobaya-run cobaya_config.yaml --resume &"
```

---

## Post-Freeze Deliverables

After freeze, generate:
1. Updated `master_cosmology_results_table.md` with planck_only values
2. Updated comparison figures (3-dataset versions)
3. Updated ΔNeff viability figure (3-dataset version)
4. Fill [PENDING: planck_only] markers in `arxiv/main.tex`
5. Recompile PDF

---

## Manuscript Placeholders to Fill

| Location | Marker | Value Source |
|----------|--------|-------------|
| Table `\ref{tab:verification}`, line ~458 | Planck-only row | Frozen diagnostics |
| Table `\ref{tab:verification}`, line ~475 | Cross-dataset narrative | Frozen + comparison |
| Appendix B footnote, line ~1306 | planck_only verification values | Frozen diagnostics |
