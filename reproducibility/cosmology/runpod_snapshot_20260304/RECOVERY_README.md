# BigBounce MCMC Recovery Guide

## RunPod Connection
```bash
ssh -i ~/.ssh/id_ed25519 -p 38115 root@195.26.233.79
```

## Check if chains are still running
```bash
ps aux | grep cobaya | grep -v grep | wc -l
# Should show ~31 processes if still running
```

## Run analysis
```bash
cd /workspace/bigbounce/reproducibility
python3 analyze_chains.py
```

## Latest backup on pod
```bash
ls -lt /workspace/backups/chains_*.tar.gz | head -1
```

## Key file locations ON RUNPOD
- Chain data: `/workspace/bigbounce/reproducibility/chains/*/spin_torsion.1.txt`
- YAML configs (backed up from /tmp): `/workspace/bigbounce/reproducibility/configs/`
- Analysis script: `/workspace/bigbounce/reproducibility/analyze_chains.py`
- Backup script: `/workspace/backup_chains.sh`
- Cobaya logs: `/workspace/outputs/`
- Hourly backups: `/workspace/backups/`

## Download EVERYTHING to local Mac
```bash
# Full chain data (will be large after 48+ hrs):
scp -r -i ~/.ssh/id_ed25519 -P 38115 \
  root@195.26.233.79:/workspace/bigbounce/reproducibility/chains/ \
  ~/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/chains/

# Configs, scripts, analysis:
scp -r -i ~/.ssh/id_ed25519 -P 38115 \
  root@195.26.233.79:/workspace/bigbounce/reproducibility/configs/ \
  ~/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/configs/

# Backups:
scp -r -i ~/.ssh/id_ed25519 -P 38115 \
  root@195.26.233.79:/workspace/backups/ \
  ~/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/runpod_backups/

# Logs:
scp -r -i ~/.ssh/id_ed25519 -P 38115 \
  root@195.26.233.79:/workspace/outputs/ \
  ~/Desktop/CODE_2026/bigbounce/reproducibility/cosmology/logs/
```

## Generate triangle plots (after chains converge)
```bash
ssh -i ~/.ssh/id_ed25519 -p 38115 root@195.26.233.79
cd /workspace/bigbounce/reproducibility
python3 generate_plots.py   # Claude will create this script
```

## Column ordering WARNING
Each dataset has DIFFERENT column order in spin_torsion.1.txt!
- planck_only: has extra `s8h5` and `omegamh2` columns
- full_tension: has extra `Mb` column before `As`, shifting all indices
- MUST read each file's own header line (`#` row) for correct column mapping
- `analyze_chains.py` handles this correctly — always use it, don't manually parse

## What to do after convergence (R-1 < 0.01)
1. Run `analyze_chains.py` for final parameter table
2. Generate triangle plots with GetDist
3. Download ALL data to local
4. Update paper (arxiv/main.tex) Table IV with converged values
5. Add new figures (triangle plot, comparison overlay)
6. Recompile PDF
7. Update site HTML pages
8. Commit as v1.3.0
9. STOP THE POD

## Convergence target
- Gelman-Rubin R-1 < 0.01 for all key params (H0, delta_neff, sigma8, omegam)
- ~100,000+ effective samples per dataset
- ~48-72 hours total runtime
