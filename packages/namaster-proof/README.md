# NaMaster Proof

NaMaster Proof is a small, installable toolkit for two failure-prone parts of
pseudo-\(C_\ell\) validation:

1. contracting a uniformly rotated spin-2 spectrum through the complete
   NaMaster bandpower-window operator without an effective-\(\ell\) or
   bin-centre approximation; and
2. publishing JSON results atomically with content-addressed sidecar receipts,
   then failing closed when the result or declared execution contract changes.

The package extracts the reusable operators validated in the BigBounce P1B
synthetic-CMB campaign. It does not perform a real-sky analysis, supply a
foreground model, or make a gravity-model inference.

## Installation

```bash
python -m pip install ./packages/namaster-proof
```

PyMaster is not required to install the package. The exact-window functions
accept a workspace implementing `get_bandpower_windows()`, `couple_cell()`,
and `decouple_cell()`. Install PyMaster separately when using a real
`pymaster.NmtWorkspace`.

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

edges = bandpower_edges(nside=256, lmax=512, n_bins=10)
field_options = field_harmonic_kwargs(lmax=512, purify_b=True)
response = build_rotation_response(workspace, cl_ee, cl_bb)
error = validate_window_equivalence(workspace, response, beta_rad=0.01)
assert error <= 1e-10

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

Receipt metadata cannot override the content-addressed fields
`schema_version`, `result_file`, `result_bytes`, or `result_sha256`.

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
