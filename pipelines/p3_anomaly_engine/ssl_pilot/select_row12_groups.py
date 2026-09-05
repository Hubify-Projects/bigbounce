#!/usr/bin/env python3
"""Select the Row 12 SSL-pilot healpix groups via the same bounded two-stage
PPS (probability-proportional-to-size) cluster sampler already sealed for
AUG-011 calibration (`build_calibration.py`), reused UNMODIFIED via import,
scaled from its 40,000-row calibration budget to a 1,000,000-row pilot
staging budget with a NEW seed (20260904, distinct from calibration's
20260804) and a larger `--n-groups`.

Input is the CACHED, already-sealed `locator_inventory.jsonl`
(`sealed_2026-08-05/locator_inventory.jsonl` on
`bamfai/bigbounce-aug-011-clean-rerun`, HF) — each line already carries
`{survey, program, healpix, targetid_count, coadd_relative_path}` per
`(survey, program, healpix)` group, i.e. pass-1 (group row counts) is
already done and cached; this script does NOT need the 27 GB zcatalog or a
fresh zcatalog stream at all. See PREFLIGHT_2026-09-04.md for why this is a
valid, honestly-narrower provenance path than the full clean-rerun's
zcatalog join: the science-target gate (OBJTYPE=='TGT' AND
COADD_FIBERSTATUS==0 AND TARGETID>0) is applied directly against each
downloaded coadd's own FIBERMAP HDU in `stage_row12_flux.py`, not via a
separate zcatalog join — the FIBERMAP is the authoritative source those
zcatalog columns are themselves mirrored from.

Output: `row12_group_selection.json` with the selected groups (ascending
survey/program/healpix order) and each group's allocated row budget, ready
for `stage_row12_flux.py` to stream.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "p1_highz_tracers" / "clean_rerun"))
from build_calibration import select_pps_groups_and_allocate, CalibrationError  # noqa: E402

SEED = 20260904
DEFAULT_N_GROUPS = 3000
DEFAULT_N_ROWS = 1_000_000


def load_locator_inventory(path: Path) -> dict[tuple[str, str, int], dict]:
    groups: dict[tuple[str, str, int], dict] = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            key = (rec["survey"], rec["program"], int(rec["healpix"]))
            groups[key] = rec
    if not groups:
        raise CalibrationError(f"locator inventory {path} yielded zero groups")
    return groups


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--locator-inventory", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--n-groups", type=int, default=DEFAULT_N_GROUPS)
    ap.add_argument("--n-rows", type=int, default=DEFAULT_N_ROWS)
    args = ap.parse_args()

    groups = load_locator_inventory(args.locator_inventory)
    counts_by_group = {g: int(rec["targetid_count"]) for g, rec in groups.items()}

    n_groups = min(args.n_groups, len(counts_by_group))
    rng, selected_groups, alloc = select_pps_groups_and_allocate(
        counts_by_group, seed=args.seed, n_groups=n_groups, n_rows=args.n_rows
    )

    out = {
        "design": "two-stage-pps-cluster/v2 (reused from build_calibration.py, "
        "new seed/scale for row12 pilot staging)",
        "seed": args.seed,
        "n_groups_available": len(counts_by_group),
        "n_groups_selected": n_groups,
        "n_rows_target": args.n_rows,
        "n_rows_allocated_total": int(sum(alloc)),
        "groups": [
            {
                "survey": g[0],
                "program": g[1],
                "healpix": g[2],
                "coadd_relative_path": groups[g]["coadd_relative_path"],
                "targetid_count": counts_by_group[g],
                "row_budget": int(a),
            }
            for g, a in zip(selected_groups, alloc)
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as fh:
        json.dump(out, fh, indent=2)
    print(
        f"selected {len(selected_groups)} groups, "
        f"{sum(alloc)} rows allocated (target {args.n_rows}) -> {args.output}"
    )


if __name__ == "__main__":
    main()
