# NaMaster Proof

NaMaster Proof is a small, installable toolkit for two failure-prone parts of
pseudo-\(C_\ell\) validation:

1. contracting a uniformly rotated spin-2 spectrum through the complete
   NaMaster bandpower-window operator without an effective-\(\ell\) or
   bin-centre approximation; and
2. publishing JSON results and content-bound sidecar receipts with atomic
   replacement of each file, then failing closed when result bytes or
   caller-asserted execution metadata change.

The package extracts the reusable operators validated in the BigBounce P1B
synthetic-CMB campaign. It does not perform a real-sky analysis, supply a
foreground model, or make a gravity-model inference.

## Installation

```bash
python -m pip install ./packages/namaster-proof
```

In an archived snapshot of the BigBounce monorepo, the package is isolated at
`packages/namaster-proof`; either run the command above from the archive root or
copy that directory intact and install from the copied directory.

PyMaster is not required to install the package. The exact-window functions
accept a workspace implementing `get_bandpower_windows()`, `couple_cell()`,
and `decouple_cell()`. They require the input spectra to have exactly the
workspace's harmonic support; short or long spectra are rejected rather than
silently padded or truncated. Install PyMaster separately when using a real
`pymaster.NmtWorkspace`. Physical validation used PyMaster 2.6.

## Python API

```python
from pathlib import Path
from namaster_proof import (
    bandpower_edges,
    build_rotation_response,
    field_harmonic_kwargs,
    publish_json,
    validate_json_receipt,
    validate_window_equivalence,
)

result = Path("shard.json")
publish_json(
    result,
    {"values": [1.0, 2.0]},
    {"suite": "example", "n_real": 2, "seed_start": 42, "seed_end": 43},
)
payload, receipt = validate_json_receipt(
    result,
    expected={"suite": "example", "n_real": 2},
)
```

The complete executable window example, including a deterministic workspace
and spectra, is in `examples/synthetic_window.py` and is exercised below.

Receipt metadata cannot override the content-binding fields
`schema_version`, `result_file`, `result_bytes`, or `result_sha256`.
The result and receipt are two sequential atomic file replacements, not one
filesystem transaction and not a cryptographic signature. A coordinated
replacement of both files is detectable only when the caller supplies trusted
expected metadata or anchors the receipt digest externally.
Each publisher derives its receipt from its own serialized byte snapshot rather
than re-reading the shared destination path, so concurrent same-path publishers
cannot cross-bind one execution's metadata to another execution's result bytes.

## CLI

Verify only the content binding:

```bash
namaster-proof verify shard.json
```

Validate the binding and declared metadata:

```bash
namaster-proof validate shard.json \
  --expect suite=example \
  --expect n_real=2
```

Values after `=` are decoded as JSON when possible, so numbers, booleans,
arrays, and objects retain their types. Both commands emit a deterministic JSON
summary and return nonzero on missing, malformed, stale, or mismatched receipts.

## Development

```bash
python -m pip install -e './packages/namaster-proof[test]'
python -m pytest packages/namaster-proof/tests
```

The exact-window implementation follows NaMaster's two-spin ordering
`[EE, EB, BE, BB]` and expected window shape
`[4, n_band, 4, lmax+1]`.

## Independent synthetic example

The example below uses a deterministic linear workspace and synthetic spectra.
It requires neither PyMaster, BigBounce data, nor repository production
artifacts:

```bash
python packages/namaster-proof/examples/synthetic_window.py \
  --output /tmp/namaster-proof-example.json \
  --beta-deg 0.25

namaster-proof validate /tmp/namaster-proof-example.json \
  --expect suite=namaster-proof-synthetic-window-v1 \
  --expect deterministic=true
```

It recovers the injected grid value, checks direct window contraction against
the linear operator, and emits a digest-bound receipt.

## Real PyMaster integration

An independent optional example constructs a real `pymaster.NmtWorkspace`,
checks package window contraction against `decouple_cell(couple_cell(...))`,
recovers a declared rotation, and compares it with an effective-multipole
shortcut:

```bash
python packages/namaster-proof/examples/pymaster_integration.py \
  --output packages/namaster-proof/examples/pymaster_integration_result.json
```

This requires separately installed PyMaster and healpy. The retained result and
receipt record the resolved PyMaster version and deterministic configuration.
