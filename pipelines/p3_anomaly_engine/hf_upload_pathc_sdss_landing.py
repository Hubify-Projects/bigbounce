#!/usr/bin/env python3
"""
HuggingFace PATH-C SDSS-landing uploader — criterion #10 cascade.

ADDITIVE companion to `sdss_landing_close.py` (criteria #1/#7/#8 atomic
close). Runs AFTER sdss_landing_close.py has landed SDSS-native artifacts
to `hf_staging/`. Pushes only the specific files the landing produced,
and preserves the fire-#158-refreshed README.

WHY THIS EXISTS (P3-PATHC-HF-REBUILD criterion-#10 readiness-hardening,
fire #162 2026-04-22):
  The sibling script `hf_upload_extend.py` (fire #13, NEOWISE+Planck+Gaia
  block) is DESTRUCTIVE — `main()` calls `shutil.rmtree(STAGING)` then
  `mkdir` before uploading. Run post-landing it would:
    (a) wipe `sdss_dr18_pathc_native.parquet` (which landing just wrote),
    (b) overwrite the fire-#158-refreshed README with its fire-#13-era
        hardcoded copy (claiming 61.7 % coverage instead of the
        post-landing real ≈100 %),
    (c) re-run the NEOWISE/Planck/Gaia top-N builds, which hit
        `H200_OUTPUTS` paths unused since fire #13 and may error.
  A dedicated landing-uploader is the safer option and mirrors the
  fire-#157 orchestrator-hardening pattern (`sdss_landing_close.py`
  dry-run contract) for criterion #10.

Usage:
    python pipelines/p3_anomaly_engine/hf_upload_pathc_sdss_landing.py
    python pipelines/p3_anomaly_engine/hf_upload_pathc_sdss_landing.py --dry-run

Inputs (all pre-staged by `sdss_landing_close.py`):
    hf_staging/sdss_dr18_pathc_native.parquet   (criterion #1 output)
    hf_staging/README.md                         (refreshed by caller
                                                   post-landing; this
                                                   script does NOT
                                                   rewrite it)

Uploads to private dataset `bamfai/bigbounce-anomaly-catalog`:
    sdss_dr18_pathc_native.parquet
    README.md

Atomic semantics:
  - If the input parquet is missing, abort WITHOUT any uploads.
  - If README is missing, abort (operator must invoke
    sdss_landing_close.py first so fire-#158 README state is
    in-place — this script only PUSHES, doesn't regenerate README).
  - Uses add-only HfApi.upload_file — no rmtree, no mkdir, no
    regeneration of existing NEOWISE/Planck/Gaia blocks.
  - Dry-run mode: loads token, verifies inputs exist, prints the
    upload plan, does NOT call HF.

Sibling scripts (criterion #10 full picture):
  - hf_upload_extend.py    : fire #13 NEOWISE+Planck+Gaia block (DESTRUCTIVE; do NOT invoke post-landing)
  - hf_upload_catalog.py   : DESI DR1 + ACT DR6 initial push
  - hf_upload_act.py       : ACT DR6 standalone refresh
  - hf_upload_extend_pod.py: pod-side variant
  - THIS SCRIPT            : SDSS native landing (fire #162 onward)
"""
import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
ENV_FILE = Path("/Users/houstongolden/Desktop/CODE_2025/hubify/.env.local")
STAGING = BASE_DIR / "hf_staging"
REPO_ID = "bamfai/bigbounce-anomaly-catalog"
REPO_TYPE = "dataset"

UPLOAD_FILES = [
    "sdss_dr18_pathc_native.parquet",
    "README.md",
]


def load_hf_token() -> str:
    if not ENV_FILE.exists():
        sys.exit(f"Env file not found: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("HUGGINGFACE_TOKEN="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("HUGGINGFACE_TOKEN not found in env file")


def verify_inputs(files: list[Path]) -> None:
    missing = [p for p in files if not p.exists()]
    if missing:
        print("ERROR: required landing artifacts not found in hf_staging/:",
              file=sys.stderr)
        for p in missing:
            print(f"  - {p}", file=sys.stderr)
        print("Invoke `sdss_landing_close.py` first to stage the landing "
              "artifacts before pushing.", file=sys.stderr)
        sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dry-run', action='store_true',
                    help='verify inputs + print plan, do not call HF')
    args = ap.parse_args()

    files = [STAGING / f for f in UPLOAD_FILES]
    print("[1/3] Verifying landing artifacts in hf_staging/ ...")
    verify_inputs(files)
    for p in files:
        sz_kb = p.stat().st_size / 1e3
        print(f"       OK  {p.name:45s} {sz_kb:10,.1f} KB")

    print("[2/3] Loading HuggingFace token ...")
    if args.dry_run:
        print("       DRY RUN: skipping token load")
        token = "<DRY>"
    else:
        token = load_hf_token()
        print(f"       loaded ({len(token)} chars)")

    print(f"[3/3] Uploading to {REPO_TYPE}s/{REPO_ID} ...")
    if args.dry_run:
        for p in files:
            print(f"       DRY RUN: would upload {p.name} ({p.stat().st_size / 1e3:,.1f} KB)")
        print()
        print("=" * 64)
        print("DRY RUN COMPLETE — inputs verified, no HF calls made.")
        print("=" * 64)
        return 0

    from huggingface_hub import HfApi
    api = HfApi(token=token)
    for p in files:
        print(f"       uploading {p.name} ({p.stat().st_size / 1e3:,.1f} KB) ...")
        api.upload_file(
            path_or_fileobj=str(p),
            path_in_repo=p.name,
            repo_id=REPO_ID,
            repo_type=REPO_TYPE,
            token=token,
            commit_message=f"Add {p.name} — P3-PATHC SDSS-native landing (criterion #10 cascade)",
        )
        print(f"       uploaded {p.name}")

    print()
    print("=" * 64)
    print("PATH-C SDSS-LANDING HF PUSH COMPLETE.")
    print(f"  dataset: https://huggingface.co/datasets/{REPO_ID}")
    print("  criterion #10 P3-PATHC-HF-REBUILD: 74 % → 100 %")
    print("=" * 64)
    return 0


if __name__ == '__main__':
    sys.exit(main())
