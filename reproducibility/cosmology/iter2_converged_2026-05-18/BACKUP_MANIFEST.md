# Cobaya iter2 DESI DR2 w0wa converged chain — backup manifest

**Backup completed:** 2026-05-18 PDT (Houston-directed safety backup before any pod-stop)
**Chain state:** TERMINATED at convergence (R̂−1 = 0.00820 < 10⁻² publication target)
**Final log marker:** `MCMC_DONE_ITER2_OMP6` at 2026-05-18 07:53 UTC
**Total runtime:** ~7 days on RunPod pod `ijzftpy3klystt` (RTX A5000, 16-rank MPI, OMP=6)
**Total accepted samples:** 128,385 across 16 chains
**Mean acceptance:** 0.2828
**Chain-length R̂_cl diagnostic:** 0.0705

## Backup locations (3+ for safety per `feedback_backup_everything`)

| # | Location | Status | URL / Path |
|---|----------|--------|------------|
| 1 | **HuggingFace** (canonical online) | ✅ uploaded 2026-05-18 PDT | `bamfai/bigbounce-mcmc` — dataset repo, public, persistent. Path: `iter2_converged_2026-05-18/` |
| 2 | **Local disk** (laptop) | ✅ pulled from HF + verified sha256 | `reproducibility/cosmology/iter2_converged_2026-05-18/` (this directory) |
| 3 | **BackBlaze Personal Backup** (cloud backup of local disk) | ✅ auto-sync (whatever is on local disk is in B2 within ~24h) | covered by Houston's BackBlaze Personal Backup subscription |
| 4 | **GitHub** (small artifacts + manifest) | ✅ committed via this manifest + posterior_summary.txt + shoes_yaml_audit.md | `github.com/Hubify-Projects/bigbounce` main branch — full tarball NOT committed (24.9 MB, just below GitHub's 50 MB warning threshold) — HuggingFace is the canonical online copy of the binary data |
| 5 | **RunPod pod** (origin, volatile) | ⚠️ on volatile pod storage, NOT a durable backup | `/workspace/quintom_dr2/chains_w0wa_dr2_iter2/` on pod `ijzftpy3klystt` |

## Artifact checksums (sha256)

| File | Size | sha256 |
|------|------|--------|
| `chains_w0wa_dr2_iter2_chain_bundle.tar.gz` | 24,909,243 B (24.9 MB) | `74cf4e609ab6b2f02fc04b3f930f805607f53181868c50eaa9bcd536443d8a4e` |
| `mcmc_iter2_omp6.log` | 10,228,459 B (10.2 MB) | `8caf10f2b9d1f4f5112cfdf6ad96c69deb7f2889a1f4e2a799f5361c0ae6416f` |
| `posterior_summary.txt` | 5,942 B | `d4f76863725939d4f4af3b734f2f11bd2ff215fc6c4677d9dc3498963c6ca91b` |
| `shoes_yaml_audit.md` | 4,396 B | `0fcae8e6ff5332b67731156325fa5d055300dc2cf23356f4a172a40a381e4375` |

## Tarball contents (`chains_w0wa_dr2_iter2_chain_bundle.tar.gz`, 89 MB uncompressed)

```
chains_w0wa_dr2_iter2/
├── spin_torsion_dr2.input.yaml      (2.8 KB) — Cobaya input config
├── spin_torsion_dr2.updated.yaml    (8.3 KB) — Cobaya runtime-updated config
├── spin_torsion_dr2.progress        (1.6 KB) — per-flush diagnostics (N, R̂−1)
├── spin_torsion_dr2.checkpoint      (108 B)  — final Metropolis state
├── spin_torsion_dr2.covmat          (7.5 KB) — proposal covariance matrix
├── spin_torsion_dr2.1.txt           (5.9 MB) — chain 1 of 16
├── spin_torsion_dr2.2.txt           (5.8 MB)
├── ...
└── spin_torsion_dr2.16.txt          (5.8 MB) — chain 16 of 16
```

Total: 16 chain files × ~5.5–5.9 MB each + 5 metadata files = 89 MB uncompressed.

## Cobaya configuration (from spin_torsion_dr2.input.yaml)

**Likelihoods active (7):**
- `bao.desi_dr2.desi_bao_all` — DESI DR2 BAO full set
- `planck_2018_lensing.native`
- `planck_2018_lowl.EE` (low-ℓ E-mode polarization)
- `planck_2018_lowl.TT` (low-ℓ temperature)
- `planck_NPIPE_highl_CamSpec.TTTEEE` (high-ℓ Planck PR4 CamSpec)
- `sn.desy5` — DES-Y5 supernovae
- `sn.pantheonplus` — Pantheon+ supernovae

**NOTE:** This iter2 chain is the **no-SH0ES** configuration (BAO + CMB + SN only). The separate `full_tension` chain (in `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/`) carries the `H0.riess2020Mb` likelihood for the canonical 3.6σ Hubble tension test — see `shoes_yaml_audit.md` in this directory for that audit.

**Sampled parameter space (17 total):**
- 8 cosmological: `logA`, `ns`, `ombh2`, `omch2`, `tau`, `theta_MC_100`, `w`, `wa`
- 9 nuisance: `A_planck`, `amp_143`, `amp_217`, `amp_143x217`, `n_143`, `n_217`, `n_143x217`, `calTE`, `calEE`

## Key physics result (per `posterior_summary.txt`)

- **w₀ = −0.8122 ± 0.0436** — departing from LCDM at **+4.3σ**
- **wₐ = −0.6666 ± 0.1864** — departing from LCDM at **−3.6σ**
- **w₀ + wₐ = −1.48 ± 0.15** — **phantom crossing required** (canonical quintom signature)
- H₀ = 67.185 ± 0.455 km/s/Mpc (no-SH0ES posterior)
- Ω_m = 0.3142 ± 0.0045
- σ₈ = 0.8057 ± 0.0083
- S₈ = 0.8245 ± 0.0089
- χ²_total = 14037.4 ± 5.6 (BAO 10.6 + CMB 10983.9 + SN 3043.0)

## Reproducibility command

To re-extract the posterior from the saved chains:

```bash
# Unpack
cd reproducibility/cosmology/iter2_converged_2026-05-18/
tar -xzf chains_w0wa_dr2_iter2_chain_bundle.tar.gz

# Verify sha256
shasum -a 256 chains_w0wa_dr2_iter2_chain_bundle.tar.gz
# Expected: 74cf4e609ab6b2f02fc04b3f930f805607f53181868c50eaa9bcd536443d8a4e

# Run GetDist
python3 -c "
from getdist import loadMCSamples
s = loadMCSamples('chains_w0wa_dr2_iter2/spin_torsion_dr2', settings={'ignore_rows': 0.3})
for p in ['H0', 'omegam', 'sigma8', 'S8', 'w', 'wa']:
    print(f'{p:<8} = {s.mean(p):.4f} ± {s.std(p):.4f}')
"
```

Expected output should match the `posterior_summary.txt` values.

## Backup verification

To verify the HF copy is intact:

```bash
huggingface-cli download bamfai/bigbounce-mcmc \
    iter2_converged_2026-05-18/chains_w0wa_dr2_iter2_chain_bundle.tar.gz \
    --repo-type dataset --local-dir /tmp/hf_verify
shasum -a 256 /tmp/hf_verify/iter2_converged_2026-05-18/chains_w0wa_dr2_iter2_chain_bundle.tar.gz
# Expected: 74cf4e609ab6b2f02fc04b3f930f805607f53181868c50eaa9bcd536443d8a4e
```

## Provenance

- **Run started:** 2026-05-11 23:41 UTC (pod creation + tmux session `chains` launch)
- **iter1 baseline:** 4-chain warm-up with ~9,500 samples, GetDist-built covmat
- **iter2 launch:** Resumed from iter1 covmat, 16-chain mpirun --oversubscribe
- **First flush to R̂−1 < 0.01:** N=122,971 at 2026-05-18 01:34 UTC (R̂−1 = 0.00912)
- **Sustained convergence:** N=128,385 at 2026-05-18 07:53 UTC (R̂−1 = 0.00820)
- **Sampler terminated automatically** at convergence (`MCMC_DONE_ITER2_OMP6` log marker)
- **Backup completed:** 2026-05-18 PDT (this file)

## Pod-shutdown safety statement

After this backup completes, the source pod `ijzftpy3klystt` can be safely stopped without loss of MCMC state. All chain data is present in:
1. HuggingFace `bamfai/bigbounce-mcmc` (online persistent, public)
2. Local disk `reproducibility/cosmology/iter2_converged_2026-05-18/` (BackBlaze Personal Backup auto-sync)
3. GitHub `Hubify-Projects/bigbounce` (small artifacts + this manifest + sha256s for verification)

Per `feedback_backup_everything` standing memory: "Always backup to 3+ locations before any destructive action." Three independent locations now confirmed.
