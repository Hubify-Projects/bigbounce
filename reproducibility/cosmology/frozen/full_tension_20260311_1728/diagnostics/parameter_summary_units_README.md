# parameter_summary.json — Column-Permutation Warning

## WARNING: Wrong columns extracted — NOT a units issue

`parameter_summary.json` was produced by a chain-extraction script that
read the **wrong column index** for every parameter (off-by-one offset:
the script read `column[i+1]` where it should have read `column[i]`).
The result is a JSON file whose **keys do not match the values** — each
key is paired with the value of the NEXT chain column, not the column
the key names.

This is a **column-permutation bug in the export script**, NOT a
Cobaya internal-normalisation or unit-conversion issue. There are no
"conversions" that recover the physical values from the raw JSON
entries; the raw values are simply *the wrong columns*.

## Verified mapping (R29 truth-audit, 2026-06-10)

Stacked all 6 chains
(`reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/chain_*/spin_torsion.1.txt`),
applied 30 % burn-in, computed weighted mean ± std on
**123,369 post-burn samples**. The chain header (line 1 of each
`spin_torsion.1.txt`) gives the canonical column order:

```
0=weight  1=minuslogpost  2=logA  3=nnu  4=ns  5=ombh2  6=omch2
7=tau  8=theta_MC_100  9=A_planck  ... 20=H0  21=sigma8  22=omegam
23=S8  24=delta_neff  25=age  ...
```

| JSON key | Raw value stored | Actual chain column read | What it really is | True column for this key |
|----------|------------------|--------------------------|-------------------|---------------------------|
| `H0` | 0.8035 | col 21 (`sigma8`) | σ₈ posterior mean | col 20 (`H0`) |
| `sigma8` | 0.308 | col 22 (`omegam`) | Ω_m posterior mean | col 21 (`sigma8`) |
| `omegam` | 0.814 | col 23 (`S8`) | S₈ posterior mean | col 22 (`omegam`) |
| `delta_neff` | 13.82 | col 25 (`age`) | universe age in Gyr | col 24 (`delta_neff`) |
| `tau` | 1.041 | col 8 (`theta_MC_100`) | 100·θ_MC | col 7 (`tau`) |
| `ns` | 0.0223 | col 5 (`ombh2`) | ω_b h² | col 4 (`ns`) |

All six keys are uniformly off by **+1 column index** — a single-line
bug in the extraction script's column indexing.

## Correct physical-unit summary

`parameter_summary_CORRECTED.json` in this same directory contains the
correctly-extracted physical values that match Paper 1B Table I:

| Parameter | Physical value (mean ± 1σ) | Verified column |
|-----------|---------------------------|-----------------|
| H₀ | 67.68 ± 1.06 km s⁻¹ Mpc⁻¹ | col 20 |
| ΔN_eff | −0.020 ± 0.169 | col 24 |
| τ | 0.054 ± 0.007 | col 7 |
| σ₈ | 0.803 ± 0.008 | col 21 |
| Ω_m | 0.308 ± 0.005 | col 22 |
| n_s | 0.965 ± 0.006 | col 4 |

These values were re-verified independently during the R29 truth-audit
by loading the raw chains with `numpy.loadtxt`, applying the
30 % burn-in cut, and computing weight-aware moments using the chain
`weight` column. Verification command:

```python
import numpy as np, glob
with open('chains/chain_01/spin_torsion.1.txt') as f:
    header = f.readline().strip().lstrip('#').split()
chain_files = sorted(glob.glob('chains/chain_*/spin_torsion.1.txt'))
data = np.vstack([np.loadtxt(cf)[int(0.3*len(np.loadtxt(cf))):]
                  for cf in chain_files])
w = data[:, 0]
for name in ['H0', 'sigma8', 'omegam', 'delta_neff', 'tau', 'ns']:
    idx = header.index(name)
    x = data[:, idx]
    m = np.average(x, weights=w)
    s = np.sqrt(np.average((x - m)**2, weights=w))
    print(f'{name}: mean={m:.6f}  std={s:.6f}')
```

GetDist-based extraction (`from getdist import loadMCSamples`,
`.getMeans()` on `param_names=['H0','sigma8','omegam','delta_neff','tau','ns']`)
yields the same numbers to 5 significant figures.

## For reproducers

Use `parameter_summary_CORRECTED.json` for any downstream analysis or
comparison against the paper. `parameter_summary.json` is retained as a
frozen record of the original (buggy) chain-extraction output;
**do not rewrite it** as it would alter the SHA256 of the frozen
artifact bundle. The extraction script's off-by-one bug has been
documented here rather than silently corrected in the export.

See Paper 1B (arxiv/paper1b_mcmc_companion.tex) §III footnote
fn:sample_stratification and the Data Availability section for the
pointer to this README from the paper body.

Generated: 2026-06-10 as part of EXT1-P1B closure wave (A1).
Revised: 2026-06-10 (R29 truth-audit) — original "unit warning"
framing was incorrect; the issue is a column-permutation bug in the
extraction script, not a Cobaya-units conversion.
