#!/usr/bin/env python3
"""Mirror the ASTRA-DESI EDR Zenodo bundle to Hugging Face as
bamfai/astra-desi-edr-mirror for durability per Houston's
"save it somewhere durable" instruction.

HF token loaded from bigbounce/.env.local."""
from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
ASTRA_DIR = REPO_ROOT / "pipelines/p5_desi_chirality/data/desi_env/astra_edr"
HF_REPO_ID = "bamfai/astra-desi-edr-mirror"


def load_hf_token() -> str:
    env_file = REPO_ROOT / ".env.local"
    for line in env_file.read_text().splitlines():
        if line.startswith("HF_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("HF_TOKEN not found in .env.local")


def main() -> int:
    from huggingface_hub import HfApi, create_repo

    token = load_hf_token()
    api = HfApi(token=token)

    # Create dataset repo (idempotent)
    try:
        create_repo(HF_REPO_ID, repo_type="dataset", token=token, exist_ok=True, private=False)
        print(f"  repo ready: https://huggingface.co/datasets/{HF_REPO_ID}", flush=True)
    except Exception as e:
        print(f"  create_repo non-fatal: {e}", flush=True)

    # Write a README in the repo describing the mirror
    readme = f"""# ASTRA-DESI EDR mirror

Mirror of the ASTRA-DESI EDR probabilistic environment catalog
(Zapata-Zuluaga et al. 2026, arXiv:2604.01456 / Zenodo
10.5281/zenodo.19358024) for durability and reproducibility of the
bigbounce P5 paper (Environmental Dependence of Spiral Chirality
Across DESI LSS).

## Original source

Zenodo DOI: 10.5281/zenodo.19358024
arXiv: https://arxiv.org/abs/2604.01456
GitHub: https://github.com/forero/ASTRA-DESI

## Files

- `classification/zone_XX_classified.fits.gz` (20 files, ~5.6 GB total
  uncompressed): per-galaxy + per-random classifications across
  20 ASTRA realizations. Columns: TARGETID, RANDITER, ISDATA, NDATA,
  NRAND, TRACER_ID, TRACERTYPE.
- `probabilities/zone_XX_probability.fits.gz` (20 files, ~6 MB): per-
  galaxy void/sheet/filament/knot membership probabilities aggregated
  across the 100 random realizations. Columns: TARGETID, TRACERTYPE,
  PVOID, PSHEET, PFILAMENT, PKNOT. **This is the primary usage file**
  for per-object cross-validation against deterministic classifiers
  (e.g., the V-Web run in bigbounce P5).
- `raw/zone_XX.fits.gz` (20 files, ~3 GB total uncompressed): input
  galaxy + random catalog rows with positional + photometric attributes.
  Columns: TARGETID, RA, DEC, Z, XCART, YCART, ZCART, TRACERTYPE,
  RANDITER, SED_SFR, SED_MASS, FLUX_G, FLUX_R.

Total galaxies across 20 zones: **657,306 unique TARGETIDs** (BGS_ANY
241,746 + LRG 112,649 + ELG 267,345 + QSO 35,566).

## Citation

If you use this mirror, please cite the original ASTRA-DESI paper:

```
@article{{ASTRADESI2026,
  author = {{Zapata-Zuluaga et al.}},
  title = {{ASTRA-DESI: per-galaxy void/sheet/filament/knot membership probabilities on the DESI Early Data Release}},
  journal = {{arXiv preprint}},
  eprint = {{2604.01456}},
  year = {{2026}},
}}
```

## bigbounce usage

The bigbounce P5 paper cross-matches this catalog per-galaxy against the
P5 deduped-primary matched-spiral catalog and the V-Web env catalog,
recovering N_overlap = 25,186 spirals with all three labels. The cross-match
finds that both V-Web (deterministic) and ASTRA (probabilistic) recover the
same headline null (max |sigma_from_half| ~2.0-2.7, no class clears
Bonferroni K=4 alpha=0.01) despite disagreeing strongly on per-galaxy class
assignment — a publication-grade robustness result.

Mirror created: 2026-05-26.
"""

    api.upload_file(
        path_or_fileobj=readme.encode(),
        path_in_repo="README.md",
        repo_id=HF_REPO_ID,
        repo_type="dataset",
        token=token,
        commit_message="add mirror README",
    )
    print("  README uploaded", flush=True)

    # Upload the 3 directories
    for subdir in ["probabilities", "classification", "raw"]:
        src = ASTRA_DIR / subdir
        if not src.exists():
            print(f"  SKIP {subdir}: not found at {src}", flush=True)
            continue
        print(f"  uploading {subdir}/ ...", flush=True)
        api.upload_folder(
            folder_path=str(src),
            path_in_repo=subdir,
            repo_id=HF_REPO_ID,
            repo_type="dataset",
            token=token,
            commit_message=f"upload {subdir}/",
        )
        print(f"  done {subdir}/", flush=True)

    print(f"DONE — https://huggingface.co/datasets/{HF_REPO_ID}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
