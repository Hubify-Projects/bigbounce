# MANIFEST — full_tension Frozen Artifact Pack

## Freeze Metadata

| Field | Value |
|-------|-------|
| **Dataset** | full_tension (Planck + BAO + SN + H0 + S8) |
| **Model** | LCDM + Delta_Neff |
| **Chain count** | 6 |
| **Total accepted samples** | 176,240 |
| **Burn fraction** | 0.3 |
| **Pod ID** | 83ubwlcdk0gat2 |
| **Hardware** | CPU5 Compute-Optimized (32 vCPU, 64 GB RAM) |
| **Region** | EUR-IS-1 (Iceland, Secure Cloud) |
| **Network Volume ID** | a9d3xb63bv |
| **Network Volume** | bigbounce-paper1-canonical (150 GB) |
| **Cobaya version** | 3.6.1 |
| **CAMB version** | 1.6.5 |
| **Python** | 3.11 |
| **Freeze timestamp** | 20260311_1728 UTC |
| **Freeze directory** | /workspace/bigbounce/frozen/full_tension_20260311_1728 |

## Chain Summary

| Chain | Accepted Samples |
|-------|-----------------|
| chain_01 | 15,054 |
| chain_02 | 14,817 |
| chain_03 | 14,700 |
| chain_04 | 14,670 |
| chain_05 | 14,532 |
| chain_06 | 102,467 |
| **Total** | **176,240** |

## Convergence Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| R-1 (H0) | 0.000629 | < 0.01 | PASS |
| R-1 (delta_neff) | 0.000517 | < 0.01 | PASS |
| R-1 (tau) | 0.000511 | < 0.02 | PASS |
| ESS (H0) | 5513 | > 2000 | PASS |
| ESS (delta_neff) | 4832 | > 2000 | PASS |
| ESS (tau) | 5475 | > 1000 | PASS |
| Drift (H0) | 0.0508sigma | < 0.1sigma | PASS |
| Drift (delta_neff) | 0.0686sigma | < 0.1sigma | PASS |
| Drift (tau) | 0.0728sigma | < 0.1sigma | PASS |
| GetDist R-1 (worst) | 0.004470 | < 0.05 | PASS |

## Parameter Summary

| Parameter | Mean | Std |
|-----------|------|-----|
| H0 | 0.803476 | 0.008446 |
| delta_neff | 13.821224 | 0.166971 |
| tau | 1.040921 | 0.000381 |
| sigma8 | 0.308060 | 0.005470 |
| omegam | 0.814133 | 0.008516 |
| ns | 0.022265 | 0.000157 |

## File Inventory (70 files)

| File | Size |
|------|------|
| SHA256SUMS.txt | 7,065 bytes |
| tables/parameter_summary.md | 485 bytes |
| plots/full_tension_chain_comparison.png | 204,747 bytes |
| plots/full_tension_posteriors.pdf | 123,104 bytes |
| plots/full_tension_posteriors.png | 180,718 bytes |
| plots/full_tension_triangle.pdf | 152,710 bytes |
| plots/full_tension_triangle.png | 189,979 bytes |
| diagnostics/convergence_summary.json | 308 bytes |
| diagnostics/freeze_diagnostics.json | 1,963 bytes |
| diagnostics/parameter_summary.json | 782 bytes |
| configs/chain_seeds.json | 754 bytes |
| configs/generate_configs.py | 7,436 bytes |
| covmats/full_tension.covmat | 7,454 bytes |
| covmats/planck_bao.covmat | 6,618 bytes |
| covmats/planck_bao_sn.covmat | 6,634 bytes |
| covmats/planck_only.covmat | 6,618 bytes |
| chains/chain_06/cobaya.pid | 5 bytes |
| chains/chain_06/cobaya_config.yaml | 2,766 bytes |
| chains/chain_06/spin_torsion.1.txt | 91,503,924 bytes |
| chains/chain_06/spin_torsion.checkpoint | 107 bytes |
| chains/chain_06/spin_torsion.covmat | 7,464 bytes |
| chains/chain_06/spin_torsion.input.yaml | 2,710 bytes |
| chains/chain_06/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_06/spin_torsion.progress | 8,078 bytes |
| chains/chain_06/spin_torsion.updated.yaml | 10,672 bytes |
| chains/chain_05/cobaya.pid | 5 bytes |
| chains/chain_05/cobaya_config.yaml | 2,766 bytes |
| chains/chain_05/spin_torsion.1.txt | 12,977,969 bytes |
| chains/chain_05/spin_torsion.checkpoint | 108 bytes |
| chains/chain_05/spin_torsion.covmat | 7,456 bytes |
| chains/chain_05/spin_torsion.input.yaml | 2,710 bytes |
| chains/chain_05/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_05/spin_torsion.progress | 3,090 bytes |
| chains/chain_05/spin_torsion.updated.yaml | 10,671 bytes |
| chains/chain_04/cobaya.pid | 5 bytes |
| chains/chain_04/cobaya_config.yaml | 2,767 bytes |
| chains/chain_04/spin_torsion.1.txt | 13,101,203 bytes |
| chains/chain_04/spin_torsion.checkpoint | 107 bytes |
| chains/chain_04/spin_torsion.covmat | 7,470 bytes |
| chains/chain_04/spin_torsion.input.yaml | 2,711 bytes |
| chains/chain_04/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_04/spin_torsion.progress | 3,146 bytes |
| chains/chain_04/spin_torsion.updated.yaml | 10,672 bytes |
| chains/chain_03/cobaya.pid | 5 bytes |
| chains/chain_03/cobaya_config.yaml | 2,767 bytes |
| chains/chain_03/spin_torsion.1.txt | 13,127,993 bytes |
| chains/chain_03/spin_torsion.checkpoint | 108 bytes |
| chains/chain_03/spin_torsion.covmat | 7,460 bytes |
| chains/chain_03/spin_torsion.input.yaml | 2,711 bytes |
| chains/chain_03/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_03/spin_torsion.progress | 3,146 bytes |
| chains/chain_03/spin_torsion.updated.yaml | 10,672 bytes |
| chains/chain_02/cobaya.pid | 5 bytes |
| chains/chain_02/cobaya_config.yaml | 2,767 bytes |
| chains/chain_02/spin_torsion.1.txt | 13,232,474 bytes |
| chains/chain_02/spin_torsion.checkpoint | 108 bytes |
| chains/chain_02/spin_torsion.covmat | 7,462 bytes |
| chains/chain_02/spin_torsion.input.yaml | 2,711 bytes |
| chains/chain_02/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_02/spin_torsion.progress | 3,145 bytes |
| chains/chain_02/spin_torsion.updated.yaml | 10,672 bytes |
| chains/chain_01/cobaya.pid | 5 bytes |
| chains/chain_01/cobaya_config.yaml | 2,766 bytes |
| chains/chain_01/spin_torsion.1.txt | 13,444,115 bytes |
| chains/chain_01/spin_torsion.checkpoint | 106 bytes |
| chains/chain_01/spin_torsion.covmat | 7,470 bytes |
| chains/chain_01/spin_torsion.input.yaml | 2,710 bytes |
| chains/chain_01/spin_torsion.input.yaml.locked | 0 bytes |
| chains/chain_01/spin_torsion.progress | 3,208 bytes |
| chains/chain_01/spin_torsion.updated.yaml | 10,671 bytes |

## Integrity

SHA256SUMS.txt contains checksums for all 70 files in this pack.
Verify with: `cd /workspace/bigbounce/frozen/full_tension_20260311_1728 && sha256sum -c SHA256SUMS.txt`
