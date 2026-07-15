# Paper 1B NaMaster 500-MC birefringence validation

This directory reproduces the foreground-free synthetic-CMB validation used
in Paper 1B. It is a pipeline test, not a Planck/ACT map analysis, a real-sky
systematics budget, or evidence for Einstein--Cartan--Holst gravity.

## Current status: physical-spectrum rerun required

The complete bandpower-window operator is validated, but the July 14 ensemble
used a D-ell-like semi-analytic EE amplitude as raw C-ell and a `0.05*EE` BB
proxy. Its numerical values below are historical only and are not a physical
noise/scatter/SNR calibration. `results/SUPERSEDED.md` records the disposition.

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

Superseded exact-window artifacts:

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
| corrected sky spectra | CAMB 1.6.6 `lensed_scalar`, raw C-ell in microkelvin-squared |
| corrected `BB` model | physical CAMB lensed BB |

The canonical mask is the intersection of `|b| > 20 deg` and
`-65 deg <= dec <= 25 deg`, Gaussian-smoothed at 2 degrees FWHM and clipped
to `[0, 1]`. The corrected sky model uses raw CAMB lensed EE and BB with the
parameters, units, resolved version, validation readout, and array SHA-256
recorded in every new result. No beam, foreground, anisotropic noise, or real
CMB map enters the calculation.

## Files and execution

```text
scripts/namaster_500mc.py              canonical three-injection run
scripts/physical_spectra.py            pinned raw CAMB EE/BB + fail-closed contract
scripts/test_physical_spectra.py       D-ell/C-ell and physical-BB regressions
scripts/windowed_rotation.py           exact bandpower-window response
scripts/test_windowed_rotation.py      algebra/operator regression
scripts/c10_robustness_battery.py      five robustness configurations
scripts/test_c10_checkpoint_resume.py  crash/resume and receipt regression
scripts/declared_fsky_sign_battery.py  two f_sky and one negative-sign check
scripts/checkpoint_io.py               atomic result/receipt publication
scripts/merge_c10_partials.py          strict eight-shard validator/merger
scripts/plot_exact_window_results.py   paper figure generator
```

Create an isolated Python 3.11 environment and install the dependencies in
`requirements.txt`. The corrected production contract pins CAMB 1.6.6. New
output metadata records exact resolved versions and raw-spectrum hashes.

Run the regression and canonical ensemble:

```bash
python scripts/test_windowed_rotation.py
python scripts/test_physical_spectra.py
NAMASTER_OUTPUT_DIR=results/physical_spectrum_v2 python scripts/namaster_500mc.py
```

For a deterministic bounded route (one realization at NSIDE 128/LMAX 256):

```bash
NAMASTER_SMOKE=1 NAMASTER_OUTPUT_DIR=/tmp/p1b-namaster-smoke \
  python scripts/namaster_500mc.py
```

Production refuses a CAMB version other than 1.6.6 and refuses to overwrite an
existing `summary.json` unless `NAMASTER_OVERWRITE=1` is explicitly set. The
unversioned-CAMB override is for bounded tests only.

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
When all five c10 and
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

## Zero-spend RunPod production preflight

`runpod_production_contract.json` freezes the container by immutable registry
digest (while retaining its human-readable source tag), the PyMaster build recipe,
one canonical command, eight independently receipted robustness commands,
output paths, and merge acceptance gates. Generate a manifest against an exact
clean commit (the API key is checked but never printed or stored):

```bash
RUNPOD_API_KEY=... python scripts/prepare_runpod_production.py \
  --expected-commit "$(git rev-parse HEAD)" --manifest /tmp/p1b-runpod-manifest.json
```

This is deliberately a **manifest-only, zero-spend** operation. The default
never launches anything. Even `--launch` fails closed after requiring both a
positive `--max-budget-usd` and the literal confirmation
`LAUNCH-P1B-500MC`, because provider mutation is not implemented in this
contract. Tests never contact RunPod.

### Prospective RunPod lifecycle primitives (launch disabled)

`scripts/runpod_budget_launcher.py` uses RunPod's official REST v1 pod routes
(`GET/POST /v1/pods`, `GET/DELETE /v1/pods/{id}`). Its default is a
non-mutating dry run. **Actual launch is disabled** by the contract's
`provider_mutation_ready: false` gate and refuses before listing or creating a
pod. The retained REST methods and mocked tests are prospective primitives, not
an approved production launcher. RunPod's documented REST v1 pod API does not expose the
account's console credit balance, so launch requires a recent, user-supplied
JSON receipt copied from the RunPod console:

```json
{"source":"runpod-console","amount_usd":10.0,"observed_at":"2026-07-15T20:00:00Z"}
```

The prospective code rejects stale/future/insufficient receipts, dirty or
hash-mismatched manifest inputs, duplicate deterministic pod names, mutable
images, more than one GPU, and inconsistent rate/runtime/budget ceilings. Those
guards are not sufficient for useful production. Before mutation can be enabled,
an independently reviewed lifecycle must add the remaining contract blockers.
The exact-commit bootstrap generator and resumable offline production runner now
close the former checkout/bootstrap and nine-job execution gaps: they verify the
manifest-bound commit and every required input hash, install and import-check the
pinned scientific runtime, run one canonical plus exactly eight robustness jobs,
write atomic log/output-hash receipts, run the strict merger, and promote a final
completion receipt only after every receipt and merged output verifies. They do
not trust executable fields in the transported manifest: commands, dependency
installation, outputs, acceptance rules, and merge semantics are re-derived
from the hash-verified exact-commit contract. Before rerunning an unverified job,
all of its declared outputs are removed so stale files cannot satisfy a no-op.
The evidence set includes all eight scientific shard receipts and both merged
result receipts, in addition to their result files. They do not contact RunPod
or any other provider. The runner now requires an explicit absolute
`--retention-root` intended for an attached RunPod network volume, separate
from its repository, ephemeral workspace, and state directory. The recommended
topology is retention at `/workspace/p1b-retention` (RunPod's persistent network
volume mount), with the clone and state under separate ephemeral paths outside
`/workspace`; this also keeps the retained tree addressable through RunPod's
supported direct network-volume access. After strict merge it
copies the bound manifest, final production receipt, every orchestration
status/receipt/log, canonical outputs, all eight result/scientific-receipt
pairs, and both merged result/scientific-receipt pairs into a commit-scoped
staging directory. Every source and destination is size/hash checked, files
and directories are fsynced, and the directory is atomically promoted only
after `RETENTION_COMPLETE.json` is written last and the inventory re-verifies.

```bash
python scripts/retain_remote_production.py \
  --validate /runpod-volume/p1b-retention/CONTRACT--COMMIT
```

Partial staging is preserved for inspection; a completed inconsistent set is
never overwritten; an identical completed set is idempotent. A prospective
in-process supervisor begins in the same call frame immediately after pod
creation and first writes an atomic recovery ledger. It requires a RunPod
network volume mounted at `/workspace`, uses only
an allowlisted direct-S3 endpoint for the chosen datacenter, and receives S3
credentials solely through boto3's standard environment/provider chain. It
polls the exact commit-scoped `RETENTION_COMPLETE.json`, downloads the marker
and every declared object to local staging, rejects missing and extra objects,
and reruns the complete retention inventory/hash validator. Only an atomically
written local verification receipt permits deletion on the successful path.
Terminal pods with absent, corrupt, or ambiguous S3 evidence are retained for
manual review; active pods crossing a price, budget, or deadline ceiling are
deleted for cost safety and explicitly recorded as unverified. Pod status alone
is never treated as scientific success.

This closes the in-process implementation gap prospectively, but does not
authorize any provider mutation. A process cannot protect itself from SIGKILL,
host loss, or a prolonged network partition. An independently hosted crash-safe
watchdog must consume the durable recovery ledger and enforce deletion before
mutation can be enabled. `provider_mutation_ready` therefore remains false and
launch still fails before any RunPod HTTP request.

Until that exists and `provider_mutation_ready` is deliberately changed,
even a fully confirmed command fails before provider HTTP:

```bash
RUNPOD_API_KEY=... python scripts/runpod_budget_launcher.py \
  --manifest /tmp/p1b-runpod-manifest.json \
  --expected-commit "$(git rev-parse HEAD)" \
  --receipt /tmp/p1b-runpod-events.jsonl \
  --launch --confirm LAUNCH-P1B-500MC-WITH-BUDGET-GUARD
```

For an independently created existing pod, the prospective watchdog requires
the immutable original creation time. Restarting it accrues budget from that
time, not from watchdog invocation:

```bash
RUNPOD_API_KEY=... python scripts/runpod_budget_launcher.py \
  --manifest /tmp/p1b-runpod-manifest.json --expected-commit "$(git rev-parse HEAD)" \
  --receipt /tmp/p1b-runpod-events.jsonl --watchdog --pod-id POD_ID \
  --created-at ORIGINAL_ISO_TIMESTAMP --deadline ISO_TIMESTAMP \
  --cost-per-hour-usd RETURNED_RATE \
  --max-total-budget-usd 1.00
```

Emergency termination is explicit and receipted:

```bash
RUNPOD_API_KEY=... python scripts/runpod_budget_launcher.py \
  --manifest /tmp/p1b-runpod-manifest.json --expected-commit "$(git rev-parse HEAD)" \
  --receipt /tmp/p1b-runpod-events.jsonl --terminate --pod-id POD_ID \
  --confirm TERMINATE-P1B-POD
```

To stop without deleting, replace `--terminate` with `--stop` and confirm with
`STOP-P1B-POD`. Stopping is not a substitute for deletion at the watchdog's
hard deadline; the watchdog always calls `DELETE /v1/pods/{id}`.

After creation, any returned price, image, GPU-count, or status mismatch causes
an immediate `DELETE` and a sanitized receipt. The API key is used only in the
Authorization header and is never printed or stored. All launcher tests mock HTTP.

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
