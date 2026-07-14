# Paper 1B NaMaster 500-MC birefringence validation

This directory reproduces the foreground-free synthetic-CMB validation used
in Paper 1B. It is a pipeline test, not a Planck/ACT map analysis, a real-sky
systematics budget, or evidence for Einstein--Cartan--Holst gravity.

## Current canonical result

The current analysis contracts the complete rotated `[EE, EB, BE, BB]`
theory through `NmtWorkspace.get_bandpower_windows()`. The older analysis
evaluated the theory at effective-ell bin centres and is preserved only as
superseded evidence under the top-level `results/` directory.

| Injection | Mean recovery | Exact-window template SNR |
|---:|---:|---:|
| `0.000 deg` | `-0.001 deg` | `0.00` |
| `0.270 deg` | `0.269 deg` | `20.0095` |
| `0.342 deg` | `0.341 deg` | `25.3190` |

For the canonical `0.270 deg` injection, the signed mean bias is
`-0.0010 deg`, the per-realization scatter is `0.05140 deg`, and the standard
error of the 500-realization mean is `0.00230 deg`. The mean residual is
therefore unresolved. These template SNR values measure an injected synthetic
signal against single-realization scatter; they are not sky-detection
significances.

Canonical artifacts:

- `results/exact_window_500mc/summary.json`
- `results/exact_window_500mc/bandpowers.npz`

## Configuration

| Parameter | Value |
|---|---:|
| `NSIDE` | 512 |
| simulated `LMAX` | 1024 |
| canonical apodized `f_sky` | 0.3226 |
| polarization white noise | 10 uK-arcmin |
| bins | 20 integer-edge bins from ell 30 to 1536 |
| realizations per injection/configuration | 500 |
| seed range per injection/configuration | 42--541 |
| canonical `BB` model | `0.05 * EE` |

The canonical mask is the intersection of `|b| > 20 deg` and
`-65 deg <= dec <= 25 deg`, Gaussian-smoothed at 2 degrees FWHM and clipped
to `[0, 1]`. The sky model is a semi-analytic `EE` spectrum with a
lensing-like `BB` proxy. No beam, foreground, anisotropic noise, or real CMB
map enters the calculation.

## Files and execution

```text
scripts/namaster_500mc.py              canonical three-injection run
scripts/windowed_rotation.py           exact bandpower-window response
scripts/test_windowed_rotation.py      algebra/operator regression
scripts/c10_robustness_battery.py      six robustness configurations
scripts/test_c10_checkpoint_resume.py  crash/resume and receipt regression
scripts/declared_fsky_sign_battery.py  two f_sky and one negative-sign check
scripts/checkpoint_io.py               atomic result/receipt publication
scripts/merge_c10_partials.py          strict nine-shard validator/merger
scripts/plot_exact_window_results.py   paper figure generator
```

Create an isolated Python 3.11 environment and install the dependencies in
`requirements.txt`. The production environment used NumPy 1.26.4, healpy
1.19.0, PyMaster 2.6, and CAMB 1.6.6 for the lensed-`BB` robustness row.

Run the regression and canonical ensemble:

```bash
python scripts/test_windowed_rotation.py
NAMASTER_OUTPUT_DIR=results/exact_window_500mc python scripts/namaster_500mc.py
```

Long robustness work is one configuration per atomic shard. For example:

```bash
C10_NREAL=500 python scripts/c10_robustness_battery.py \
  --only-config apod_fwhm_0p5

DECLARED_NREAL=500 python scripts/declared_fsky_sign_battery.py \
  --only-config fsky_0p65
```

Each production shard records the exact configuration object, `N=500`, seed
range, operator, equivalence residual, core software versions, byte count,
and SHA-256 in a sidecar `*.json.receipt.json`. The c10 driver also atomically
checkpoints ordered per-realization bandpowers every 25 realizations. Resume
requires an exact config, seed range, theory operator, and combined source-code
fingerprint match; a mismatch fails closed. The checkpoint is removed only
after the final result and receipt publish successfully. Restarting skips a shard only
after all receipt fields and the result hash validate. Historical final-shard
receipts without a source fingerprint remain valid under their original strict
config/N/seed/operator checks; only new resumable checkpoints require one.
When all six c10 and
all three declared shards exist, validate and merge them with:

```bash
python scripts/merge_c10_partials.py
python scripts/plot_exact_window_results.py
python scripts/test_c10_checkpoint_resume.py
```

The merger rejects missing, duplicated, reordered, parameter-mismatched,
mixed-operator, mixed-software, wrong-ensemble, or failed-equivalence inputs.
Merged outputs record every child SHA-256 and are themselves written
atomically.

## Determinism and numerical checks

- Every configuration uses exactly 500 seeds, `42, 43, ..., 541`.
- The canonical three injections reuse the same noisy realization per seed;
  uniform Q/U rotation is applied algebraically to the coupled spectra.
- Direct rotated-field and algebraic-rotation paths agree to `8.67e-19` in
  the committed regression.
- Direct bandpower-window contraction and
  `decouple_cell(couple_cell(theory))` agree to `3.19e-16` in the regression;
  every production workspace separately enforces a `1e-10` ceiling.
- Package/ABI changes may alter low-order floating-point digits; receipts and
  the analysis manifest identify the frozen outputs exactly.

## Superseded artifacts and scope

See `results/SUPERSEDED.md` before using any top-level historical JSON. The
pre-July-2026 outputs are retained for provenance but must not be cited as the
current calibration result.

The validation cannot break the cosmic-rotation/instrument-angle degeneracy
because it contains no unrotated Galactic foreground. Its results must not be
treated as a real-sky detection, foreground residual, beam/calibration bound,
or systematic floor.
