#!/usr/bin/env python3
"""Fail-closed source-to-claim audit for every new P4 v1.0.245 number."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
P4 = ROOT / "pipelines/p2_chirality"
EVIDENCE = {
    "catalog_qc": P4 / "outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json",
    "hc_qc": P4 / "outputs/canonical_provenance/ext3_nfm1_hc_dipole_qc_rerun.json",
    "primary_label_shuffle": P4 / "outputs/canonical_provenance/p4_primary_hc_label_shuffle_10k.json",
    "primary_label_shuffle_array": P4 / "outputs/canonical_provenance/p4_primary_hc_label_shuffle_10k.npy",
    "robustness_panel": P4 / "outputs/canonical_provenance/c12_r24conf_local_batch.json",
    "master_support": P4 / "outputs/canonical_provenance/c6_depth_stratified_null.json",
    "source_receipt": P4 / "outputs/canonical_provenance/fig7_raw_vs_eq_manifest.json",
    "primary_result": P4 / "outputs/dipole/catalog_c_summary.json",
}


class ClaimAuditError(RuntimeError):
    """Raised when a manuscript or release-contract claim loses its source."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def close(observed: float, expected: float, atol: float = 1e-12) -> bool:
    return math.isclose(float(observed), float(expected), rel_tol=0.0, abs_tol=atol)


def audit() -> dict[str, Any]:
    qc = load(EVIDENCE["catalog_qc"])
    hc = load(EVIDENCE["hc_qc"])
    label_shuffle = load(EVIDENCE["primary_label_shuffle"])
    r24 = load(EVIDENCE["robustness_panel"])
    master = load(EVIDENCE["master_support"])
    receipt = load(EVIDENCE["source_receipt"])
    primary = load(EVIDENCE["primary_result"])
    panel = r24["items"]["queue8_openai_m1_robustness_panel"]
    cells = panel["panel"]

    gates = {
        "catalog_rows": qc["n_rows_total"] == 8_474_531,
        "unsafe_catalog_rows": qc["rows_violating_beyond_1e-3_any_channel"] == 249_066,
        "unsafe_catalog_fraction": close(qc["fraction_violating_beyond_1e-3_any_channel"], 0.029389945001086194),
        "max_bound_excursion": close(qc["bound_excursion_any_channel"]["max"], 0.09009438753128052),
        "primary_hc_rows": hc["n_hc"] == 949_584,
        "unsafe_primary_hc_rows": hc["n_flagged_in_hc"] == 59_515,
        "strict_primary_hc_rows": hc["flagged_rows_excluded"]["n"] == 890_069,
        "hc_support_pixels": hc["baseline"]["n_pix"] == 23_682,
        "full_spiral_support_pixels": r24["items"]["queue6_meta_m3_equal_area_bands"]["n_pix_canonical"] == 24_087,
        "master_support_pixels": master["config"]["mask_n_pix"] == 24_297,
        "source_bytes": receipt["catalog"]["bytes"] == 952_115_239,
        "source_rows": receipt["catalog"]["rows"] == 8_474_531,
        "source_sha256": receipt["catalog"]["sha256"] == "e8525ba5c98576f6361580e4a0aa7a86929ccc9f79b1423808774cfaaf313563",
        "primary_amplitude": close(primary["dipole"]["amplitude"], 0.004597074287780104, 1e-15),
        "primary_null_draws": label_shuffle["n_draws"] == 10_000,
        "primary_null_seed": label_shuffle["seed"] == 20_260_715,
        "primary_null_array_sha256": label_shuffle["array"]["sha256"] == "f6360f4bec22669097cee3e2fad8b176291d3ecbfbfbb9a9290d0bce3d5152c0",
        "primary_null_retained_array_sha256": sha256_file(EVIDENCE["primary_label_shuffle_array"]) == "f6360f4bec22669097cee3e2fad8b176291d3ecbfbfbb9a9290d0bce3d5152c0",
        "primary_null_mean": close(label_shuffle["null_mean"], 0.003489942041063312, 1e-15),
        "primary_null_std": close(label_shuffle["null_std_ddof0"], 0.0015696946246071318, 1e-15),
        "primary_z": close(label_shuffle["significance_sigma_ddof0"], 0.7053169637972659, 1e-14),
        "primary_rank_p": close(label_shuffle["rank_p_one_sided_upper_tail"], 0.22467753224677534, 1e-15),
        "panel_contract": panel["null"] == "2000 pixel-permutation realizations per cell (A_p permuted across in-mask pixels; weights stay attached to pixels), seed 20260610",
        "panel_cells": len(cells) == 6,
    }
    expected_cells = [
        (10, "uniform", 23_682, 0.535620732327616, 0.2698650674662669),
        (10, "N_spiral_weighted", 23_682, 0.7834595272562719, 0.19740129935032483),
        (20, "uniform", 22_078, 0.2680704678769275, 0.35932033983008493),
        (20, "N_spiral_weighted", 22_078, 0.7940214542131249, 0.20339830084957522),
        (50, "uniform", 5_763, -0.38206284677866265, 0.6061969015492253),
        (50, "N_spiral_weighted", 5_763, -0.14082230026961762, 0.5052473763118441),
    ]
    for index, (threshold, fit, n_pix, z_mom, rank_p) in enumerate(expected_cells):
        cell = cells[index]
        gates[f"panel_cell_{index + 1}"] = (
            cell["mask_threshold_nspiral_ge"] == threshold
            and cell["fit"] == fit
            and cell["n_pix"] == n_pix
            and close(cell["z_mom"], z_mom)
            and close(cell["rank_p"], rank_p)
        )

    tex = (P4 / "chirality_catalog_paper.tex").read_text(encoding="utf-8")
    schema = load(P4 / "apjs_release_schema_v1_0_244.json")
    gates.update(
        {
            "paper_version": r"\newcommand{\paperVersion}{v1.0.245}" in tex,
            "paper_prints_catalog_and_hc_counts": "249,066 unsafe rows catalog-wide" in tex and "Exactly 59,515" in tex,
            "paper_prints_primary_null": "population standard deviation are $0.00348994$ and $0.00156969$" in tex and "$p=(2246+1)/(10000+1)=0.22468$" in tex,
            "paper_prints_all_panel_cells": all(token in tex for token in ("(+0.536,0.270)", "(+0.794,0.203)", "(-0.141,0.505)")),
            "paper_names_three_supports": all(token in tex for token in ("HC-REALSPACE-INCLUSIVE", "FULL-SPIRAL-CANONICAL", "MASTER-ALL-GALAXY-FOOTPRINT")),
            "paper_uncertainty_scales_one_over_g": r"\sigma(A_{\rm phys})=\sigma(A_{\rm obs})/g" in tex,
            "paper_doi_gate_open": "No immutable archive or DOI exists yet" in tex,
            "paper_no_false_public_qc_claim": "In the public HuggingFace Parquet release" not in tex,
            "schema_uncalibrated_scope": "no calibrated label probabilities" in schema["scientific_scope"],
            "schema_archive_gate_open": schema["release_gates"]["immutable_archive_or_doi"] == "OPEN",
        }
    )
    failed = [name for name, passed in gates.items() if not passed]
    result = {
        "schema": "p4-v1.0.245-source-to-claim-audit/v1",
        "paper": "P4",
        "paper_version": "v1.0.245",
        "status": "PASS" if not failed else "FAIL",
        "gates": gates,
        "failed_gates": failed,
        "evidence": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": sha256_file(path)}
            for name, path in EVIDENCE.items()
        },
        "scope_guard": {
            "calibrated_probability_claim": False,
            "physical_or_primordial_bound": False,
            "matched_external_estimator_claim": False,
            "formal_preregistration_claim": False,
            "immutable_archive_or_doi": "OPEN",
        },
    }
    if failed:
        raise ClaimAuditError(json.dumps(result, indent=2, sort_keys=True))
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = audit()
    except (OSError, KeyError, ValueError, ClaimAuditError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
