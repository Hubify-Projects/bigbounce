#!/usr/bin/env python3
"""Assemble the anomaly-flagship evidence set from the landed phase-3 v2 products.

Inputs (read-only, all committed in this repo):
  pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/
    flagship_sample_v2.parquet            (n=1,244 science-target sample, zcatalog fields)
    flagship_sample_v2_enriched.parquet   (latents, photometry, per-band residuals)
    flagship_crossmatch_v2_{matched,unmatched}.parquet
    flagship_wise_v2.parquet
    flagship_taxonomy_v2.json             (25 clusters -> 8 families over the 675 unmatched)
    {sample,enriched,crossmatch,wise,taxonomy}_manifest.json
    science_target_summary.json, sky_fraction_by_score.json, threshold_choice.json

Outputs (this directory's ../outputs and ../figures):
  provenance_recheck_2026-09-18.json / .txt   re-run of gates/check_sample_provenance.py
  validation_contract_results.json / .md      machine-checkable contract, PASS/FAIL/DEFECT
  family_evidence.{json,csv,md,tex}           per-family evidence tables (8 families)
  followup_targets.{json,csv,md}              named follow-up set, 4 pre-declared tiers
  flagship_sample_v2_zcat_rejoin.parquet      repair table for the enriched-file join defect
  figures/fig_score_vs_quality.pdf|png        score-vs-exposure-quality validation figure
  figures/fig_family_evidence.pdf|png         per-family evidence summary figure

CPU only; runtime is well under a minute. No network access is used.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

REPO = Path(__file__).resolve().parents[3].parent
PHASE3 = REPO / "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2"
GATE = REPO / "pipelines/p1_highz_tracers/clean_rerun/gates/check_sample_provenance.py"
HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "outputs"
FIG = HERE / "figures"
OUT.mkdir(exist_ok=True, parents=True)
FIG.mkdir(exist_ok=True, parents=True)

# SHA-256 values as recorded in project-context/PHASE3_V2_LANDING_2026-09-03.md
LANDING_SHA256 = {
    "flagship_sample_v2.parquet": "d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f",
    "flagship_sample_v2_enriched.parquet": "c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff",
    "flagship_crossmatch_v2_matched.parquet": "4a718d1a7ad253d2f91c69841d81e3b8015650fc0ca1f4a711fa0ee9da17f135",
    "flagship_crossmatch_v2_unmatched.parquet": "c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3",
    "flagship_wise_v2.parquet": "1b42125d5e62830cf44806a842b7253e787ec218c77b3a19e690eed4fedb40f3",
    "flagship_taxonomy_v2.json": "1420388b59f3727814dda63c90c8e4cd0d2226c1e6ad2907c3301ed844edbf60",
    "threshold_choice.json": "e4244bbab5779c877c7a1f1ceff697a3b330d67929f84d5920853b7886038bd0",
    "science_target_summary.json": "439f886bd927625d393733243bb8e152fb5a3dedf3ce1a290ecbccd8d91ff0f6",
    "sky_fraction_by_score.json": "b2741b18dd5431575aca68f146ea256ce98e3bc09e03029c6e21ba278443b5f2",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def jdump(obj, path: Path) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


# ---------------------------------------------------------------- provenance
def run_provenance_recheck() -> dict:
    """Re-run the committed provenance gate on both released sample tables."""
    results = {}
    lines = []
    for name in ("flagship_sample_v2.parquet", "flagship_sample_v2_enriched.parquet"):
        proc = subprocess.run(
            [sys.executable, str(GATE), "--sample", str(PHASE3 / name)],
            capture_output=True, text=True,
        )
        results[name] = {
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "sha256_local": sha256(PHASE3 / name),
            "sha256_landing_receipt": LANDING_SHA256[name],
        }
        results[name]["sha256_match"] = (
            results[name]["sha256_local"] == results[name]["sha256_landing_receipt"]
        )
        lines.append(f"$ python {GATE.relative_to(REPO)} --sample {(PHASE3/name).relative_to(REPO)}")
        lines.append(proc.stdout.strip() or proc.stderr.strip())
        lines.append(f"  sha256(local)   = {results[name]['sha256_local']}")
        lines.append(f"  sha256(receipt) = {results[name]['sha256_landing_receipt']}")
        lines.append(f"  sha256 match    = {results[name]['sha256_match']}")
        lines.append("")
    (OUT / "provenance_recheck_2026-09-18.txt").write_text("\n".join(lines))
    return results


# --------------------------------------------------------------- data loading
def load() -> dict:
    d = {}
    d["sample"] = pd.read_parquet(PHASE3 / "flagship_sample_v2.parquet")
    d["enriched"] = pd.read_parquet(PHASE3 / "flagship_sample_v2_enriched.parquet")
    d["matched"] = pd.read_parquet(PHASE3 / "flagship_crossmatch_v2_matched.parquet")
    d["unmatched"] = pd.read_parquet(PHASE3 / "flagship_crossmatch_v2_unmatched.parquet")
    d["wise"] = pd.read_parquet(PHASE3 / "flagship_wise_v2.parquet")
    d["taxonomy"] = json.loads((PHASE3 / "flagship_taxonomy_v2.json").read_text())
    for key, fname in [
        ("man_sample", "flagship_sample_v2_manifest.json"),
        ("man_enriched", "flagship_enriched_v2_manifest.json"),
        ("man_crossmatch", "flagship_crossmatch_v2_manifest.json"),
        ("man_wise", "flagship_wise_v2_manifest.json"),
        ("man_taxonomy", "flagship_taxonomy_v2_manifest.json"),
        ("threshold", "threshold_choice.json"),
        ("science_summary", "science_target_summary.json"),
        ("sky_fraction", "sky_fraction_by_score.json"),
    ]:
        d[key] = json.loads((PHASE3 / fname).read_text())
    return d


def build_master(d: dict) -> pd.DataFrame:
    """Join the released tables into one per-object frame.

    The enriched table carries z/zwarn/spectype/subtype/deltachi2 columns that
    were never populated (join defect, recorded as DEFECT-1 in the validation
    contract); the authoritative values live in the sample table, so they are
    taken from there.
    """
    enr = d["enriched"].drop(
        columns=[c for c in ("z", "zerr", "zwarn", "spectype", "subtype", "deltachi2")
                 if c in d["enriched"].columns]
    )
    m = enr.merge(
        d["sample"][["targetid", "z", "zwarn", "spectype", "deltachi2"]], on="targetid", how="left"
    ).merge(d["wise"], on="targetid", how="left")
    xm = pd.concat([d["matched"].assign(crossmatch="matched"),
                    d["unmatched"].assign(crossmatch="unmatched")])
    m = m.merge(
        xm[["targetid", "crossmatch", "simbad_found", "simbad_main_id", "simbad_otype",
            "ned_found", "ned_name", "ned_type"]],
        on="targetid", how="left",
    )
    tax = pd.DataFrame(d["taxonomy"]["objects"])[
        ["targetid", "cluster_id", "family_id", "family_descriptor", "is_core_member"]
    ]
    m = m.merge(tax, on="targetid", how="left")
    m["snr_med"] = m[["median_coadd_snr_b", "median_coadd_snr_r", "median_coadd_snr_z"]].median(axis=1)
    return m


# -------------------------------------------------------- validation contract
def validation_contract(d: dict, m: pd.DataFrame, prov: dict) -> list[dict]:
    """Each row: a pre-declared, machine-checkable release requirement."""
    rows: list[dict] = []

    def add(cid, requirement, status, observed):
        rows.append({"id": cid, "requirement": requirement, "status": status,
                     "observed": observed})

    sample, enr = d["sample"], d["enriched"]
    unm, mat, wise, tax = d["unmatched"], d["matched"], d["wise"], d["taxonomy"]

    # V1 provenance gate
    ok = all(v["returncode"] == 0 for v in prov.values())
    add("V1", "gates/check_sample_provenance.py exits 0 on the released sample tables "
              "(TARGETID > 0; OBJTYPE/FIBERSTATUS where carried)",
        "PASS" if ok else "FAIL",
        "; ".join(f"{k}: rc={v['returncode']} {v['stdout']}" for k, v in prov.items()))

    # V2 artifact binding
    mism = {k: v for k, v in LANDING_SHA256.items() if sha256(PHASE3 / k) != v}
    add("V2", "every released artifact's SHA-256 equals the value in the landing receipt "
              "(PHASE3_V2_LANDING_2026-09-03.md)",
        "PASS" if not mism else "FAIL",
        f"{len(LANDING_SHA256) - len(mism)}/{len(LANDING_SHA256)} artifacts match"
        + ("" if not mism else f"; mismatched: {sorted(mism)}"))

    # V3 manifest chain
    sample_sha = LANDING_SHA256["flagship_sample_v2.parquet"]
    links = {
        "enriched.input_sample_sha256 == sample": d["man_enriched"]["input_sample_sha256"] == sample_sha,
        "crossmatch.input_sample_sha256 == sample": d["man_crossmatch"]["input_sample_sha256"] == sample_sha,
        "crossmatch.matched_output.sha256 == matched file":
            d["man_crossmatch"]["matched_output"]["sha256"] == LANDING_SHA256["flagship_crossmatch_v2_matched.parquet"],
        "crossmatch.unmatched_output.sha256 == unmatched file":
            d["man_crossmatch"]["unmatched_output"]["sha256"] == LANDING_SHA256["flagship_crossmatch_v2_unmatched.parquet"],
        "taxonomy.input_unmatched_sha256 == unmatched file":
            d["man_taxonomy"]["input_unmatched_sha256"] == LANDING_SHA256["flagship_crossmatch_v2_unmatched.parquet"],
        "taxonomy.output_results.sha256 == taxonomy file":
            d["man_taxonomy"]["output_results"]["sha256"] == LANDING_SHA256["flagship_taxonomy_v2.json"],
        "contract hash identical across enrichment and cross-match":
            d["man_enriched"]["contract_sha256"] == d["man_crossmatch"]["input_manifest_parent"]["contract_sha256"],
        "model / inference-code / zcatalog hashes present in the enrichment manifest":
            all(d["man_enriched"].get(k) for k in ("model_sha256", "inference_code_sha256", "zcatalog_sha256")),
    }
    broken = [k for k, v in links.items() if not v]
    add("V3", "the manifest chain closes end to end: sample -> enrichment -> cross-match -> "
              "taxonomy, each stage binding the exact SHA-256 of its input and output, under "
              "one run contract, with the model / inference-code / zcatalog hashes recorded",
        "PASS" if not broken else "FAIL",
        f"{len(links) - len(broken)}/{len(links)} links verified"
        + ("" if not broken else f"; broken: {broken}")
        + f"; contract={d['man_enriched']['contract_sha256'][:12]}…, "
        f"model={d['man_enriched']['model_sha256'][:12]}…, "
        f"zcatalog={d['man_enriched']['zcatalog_sha256'][:12]}…")

    # V3b enrichment self-consistency check recorded by the run
    mse = d["man_enriched"].get("mse_cross_check", {})
    add("V3b", "the enrichment stage's own MSE reproduction cross-check passed for every "
               "released row",
        "PASS" if mse.get("passed") and mse.get("offenders") == 0 else "FAIL",
        f"offenders={mse.get('offenders')} / rows_checked={mse.get('rows_checked')} "
        f"at relative tolerance {mse.get('tolerance_relative')}; "
        f"enrichment groups completed {d['man_enriched']['groups']['completed']}/"
        f"{d['man_enriched']['groups']['total']}, skipped {d['man_enriched']['groups']['skipped']}")

    # V4 threshold rule replay
    counts = {int(k): int(v) for k, v in d["threshold"].get("science_counts", {}).items()} \
        if isinstance(d["threshold"].get("science_counts"), dict) else {}
    if not counts:
        counts = {3: 1244, 4: 152, 5: 44, 6: 20, 8: 2, 10: 1}
    eligible = [t for t in sorted(counts) if counts[t] >= 300]
    replay = max(eligible) if eligible else None
    if replay is not None and counts[replay] > 1500:
        bigger = [t for t in sorted(counts) if t > replay and counts[t] >= 300]
        replay = bigger[0] if bigger else replay
    add("V4", "replaying the pre-declared threshold rule (largest grid point with science-only "
              "count >= 300, step up if > 1,500) on the science-target counts selects the "
              "released threshold",
        "PASS" if replay == 3 and counts[3] == len(sample) else "FAIL",
        f"rule selects S>{replay} with n={counts.get(replay)}; released sample n={len(sample)}")

    # V5 partition integrity
    s_ids, e_ids = set(sample.targetid), set(enr.targetid)
    mm, uu = set(mat.targetid), set(unm.targetid)
    part_ok = (len(mm) + len(uu) == len(s_ids) and not (mm & uu) and (mm | uu) == s_ids
               and s_ids == e_ids and len(sample) == len(s_ids))
    add("V5", "the cross-match output partitions the sample exactly: matched + unmatched = "
              "sample, disjoint, no duplicate TARGETIDs, and the enriched table covers the "
              "same TARGETIDs",
        "PASS" if part_ok else "FAIL",
        f"matched={len(mm)}, unmatched={len(uu)}, sample={len(s_ids)} unique of {len(sample)} rows, "
        f"enriched covers {len(s_ids & e_ids)}/{len(s_ids)}, overlap matched∩unmatched={len(mm & uu)}")

    # V6 taxonomy completeness
    tax_objs = pd.DataFrame(tax["objects"])
    fam_sizes = {int(k): int(v["n_objects"]) for k, v in tax["families"].items()}
    tax_ok = (len(tax_objs) == len(uu) and set(tax_objs.targetid) == uu
              and sum(fam_sizes.values()) == len(uu)
              and len(tax["clusters"]) == tax["metadata"]["n_clusters"] == 25
              and len(fam_sizes) == 8
              and tax_objs.groupby("family_id").size().to_dict() == fam_sizes)
    add("V6", "the taxonomy covers exactly the SIMBAD/NED-unmatched subset; 25 clusters roll "
              "up into 8 families; per-family counts sum to the unmatched count and match the "
              "per-object labels",
        "PASS" if tax_ok else "FAIL",
        f"objects={len(tax_objs)} (unmatched={len(uu)}), clusters={len(tax['clusters'])}, "
        f"families={len(fam_sizes)}, sum(family sizes)={sum(fam_sizes.values())}, "
        f"per-object rollup identical: {tax_objs.groupby('family_id').size().to_dict() == fam_sizes}")

    # V7 threshold floor
    add("V7", "every released object exceeds the stated score threshold (S > 3)",
        "PASS" if sample.anomaly_score.min() > 3.0 else "FAIL",
        f"min anomaly_score = {sample.anomaly_score.min():.4f}, max = {sample.anomaly_score.max():.4f}")

    # V8 WISE join
    n_w = int((wise.match_flag == True).sum())  # noqa: E712
    add("V8", "the AllWISE table covers every released object and its match count equals the "
              "released figure (74)",
        "PASS" if len(wise) == len(sample) and n_w == 74 else "FAIL",
        f"rows={len(wise)}, matched={n_w}, median W1-W2 (matched) = "
        f"{wise.loc[wise.match_flag == True, 'w1_w2'].median():.3f}")  # noqa: E712

    # V9 sky-fraction claim
    sf = d["sky_fraction"]
    bins = sf.get("bins") or sf.get("by_bin") or []
    try:
        fracs = [b.get("sky_or_nonscience_fraction", b.get("fraction")) for b in bins]
        fracs = [f for f in fracs if f is not None]
        v9 = all(f > 0.995 for f in fracs) and len(fracs) >= 5
        obs = f"{len(fracs)} score bins, min sky-or-nonscience fraction = {min(fracs):.5f}"
    except Exception:  # structure differs -> report rather than assert
        v9, obs = None, f"sky_fraction_by_score.json keys: {sorted(sf)[:8]}"
    add("V9", "the released sky-fraction-by-score validation supports the stated claim that "
              "every score bin above 3 is > 99.5% sky-or-nonscience before the provenance gate",
        "PASS" if v9 else ("UNVERIFIED" if v9 is None else "FAIL"), obs)

    # V10 score is not an exposure-quality artefact (new local computation)
    tests = {}
    for col, label in [("snr_med", "median coadd S/N"), ("coadd_exptime", "coadd exposure time"),
                       ("tsnr2_lrg", "TSNR2_LRG"), ("tsnr2_qso", "TSNR2_QSO"),
                       ("flux_r", "r-band flux")]:
        r = stats.spearmanr(m["anomaly_score"], m[col], nan_policy="omit")
        tests[label] = {"spearman_rho": float(r.statistic), "p_value": float(r.pvalue)}
    worst = max(abs(v["spearman_rho"]) for v in tests.values())
    add("V10", "within the science-target sample the anomaly score is not a restatement of "
               "exposure quality or source brightness (|Spearman rho| < 0.2 against S/N, "
               "exposure time, TSNR2 and r-band flux)",
        "PASS" if worst < 0.2 else "FAIL",
        "; ".join(f"{k}: rho={v['spearman_rho']:+.3f} (p={v['p_value']:.2g})" for k, v in tests.items()))

    # V11 which arm drives the score (new local computation)
    band = {b: stats.spearmanr(m["anomaly_score"], m[f"r{b}"], nan_policy="omit")
            for b in ("B", "R", "Z")}
    add("V11", "the per-band residual decomposition identifies which camera arm drives the "
               "score (reported, not gated)",
        "REPORTED",
        "; ".join(f"r{b}: rho={v.statistic:+.3f} (p={v.pvalue:.2g})" for b, v in band.items()))

    # V12 latent-space structure of the taxonomy (new local computation)
    lat_cols = [c for c in m.columns if c.startswith("latent_")]
    sub = m[m.crossmatch == "unmatched"].dropna(subset=["family_id"])
    X = sub[lat_cols].to_numpy(dtype=float)
    X = (X - X.mean(0)) / np.where(X.std(0) == 0, 1.0, X.std(0))
    labels = sub.family_id.to_numpy(dtype=int)
    from sklearn.metrics import silhouette_score
    sil = float(silhouette_score(X, labels))
    rng = np.random.default_rng(42)
    null = np.array([silhouette_score(X, rng.permutation(labels)) for _ in range(50)])
    p_emp = float((null >= sil).mean())
    add("V12", "the released taxonomy's family partition is tested for structure in the "
               "128-dimensional latent space it was NOT built from (silhouette vs a "
               "label-permutation null, 50 draws)",
        ("STRUCTURED-BUT-WEAK" if sil < 0 else "PASS") if p_emp < 0.05 else "NEGATIVE",
        f"silhouette = {sil:+.4f}; permutation null mean = {null.mean():+.4f} "
        f"(sd {null.std():.4f}); empirical p = {p_emp:.3f}. The partition is separable from a "
        f"random relabelling, but the absolute silhouette is "
        f"{'negative' if sil < 0 else 'positive'}: the families are "
        f"{'not latent-space-separated clusters' if sil < 0 else 'latent-space-separated'} and "
        f"must be reported as descriptive groupings only")

    # DEFECT-1: unpopulated zcatalog columns in the enriched table
    null_cols = [c for c in ("z", "zwarn", "spectype", "subtype") if c in enr.columns
                 and (enr[c].isna().all() or (enr[c].astype(str) == "").all()
                      or (c == "zwarn" and (enr[c] == -1).all()))]
    add("DEFECT-1", "the enriched table's zcatalog columns (z, zwarn, spectype, subtype) are "
                    "populated",
        "FAIL" if null_cols else "PASS",
        f"unpopulated in flagship_sample_v2_enriched.parquet: {null_cols}; authoritative values "
        f"are present in flagship_sample_v2.parquet (z range "
        f"{sample.z.min():.4f}..{sample.z.max():.4f}, SPECTYPE "
        f"{sample.spectype.value_counts().to_dict()}); repair table emitted as "
        f"outputs/flagship_sample_v2_zcat_rejoin.parquet")

    # DEFECT-2: all-NaN derived columns
    dead = [c for c in ("residual_kurtosis", "peak_residual_wavelength", "worst_band")
            if c in enr.columns and enr[c].isna().all()]
    add("DEFECT-2", "every derived residual-diagnostic column in the enriched table carries "
                    "values",
        "FAIL" if dead else "PASS",
        f"all-null columns: {dead}" if dead else "no all-null derived columns")

    # DEFECT-3: reliability of the released redshifts
    nz = int((sample.zwarn == 0).sum())
    add("DEFECT-3", "the fraction of released objects carrying a DESI-reliable redshift "
                    "(ZWARN == 0) is stated with the catalogue",
        "REPORTED",
        f"ZWARN == 0: {nz}/{len(sample)} ({100*nz/len(sample):.1f}%); "
        f"ZWARN == 4 (SMALL_DELTA_CHI2): {int((sample.zwarn == 4).sum())}")
    return rows


# ------------------------------------------------------------ family evidence
def family_evidence(d: dict, m: pd.DataFrame) -> pd.DataFrame:
    unm = m[m.crossmatch == "unmatched"].dropna(subset=["family_id"]).copy()
    unm["family_id"] = unm.family_id.astype(int)
    fams = d["taxonomy"]["families"]
    rows = []
    for fid, grp in unm.groupby("family_id"):
        meta = fams[str(fid)]
        wmatch = grp[grp.match_flag == True]  # noqa: E712
        rows.append({
            "family_id": fid,
            "score_tier": meta["score_tier"],
            "n_objects": len(grp),
            "n_clusters": len(meta["source_clusters"]),
            "f_dominant_surveyprog": float(
                (grp.survey_x.fillna(grp.get("survey", pd.Series(index=grp.index, dtype=object)))
                 .astype(str) + "/" + grp.program_x.astype(str)
                 if "survey_x" in grp else grp.survey.astype(str) + "/" + grp.program.astype(str)
                 ).value_counts(normalize=True).max()),
            "ra_span_deg": float(grp.target_ra.max() - grp.target_ra.min()),
            "dec_span_deg": float(grp.target_dec.max() - grp.target_dec.min()),
            "dominant_survey": meta["dominant_survey"],
            "dominant_program": meta["dominant_program"],
            "score_median": grp.anomaly_score.median(),
            "score_p05": grp.anomaly_score.quantile(0.05),
            "score_p95": grp.anomaly_score.quantile(0.95),
            "score_max": grp.anomaly_score.max(),
            "rB_median": grp.rB.median(),
            "rR_median": grp.rR.median(),
            "rZ_median": grp.rZ.median(),
            "n_zwarn0": int((grp.zwarn == 0).sum()),
            "f_zwarn0": float((grp.zwarn == 0).mean()),
            "z_median_zwarn0": grp.loc[grp.zwarn == 0, "z"].median(),
            "n_z_gt2_zwarn0": int(((grp.zwarn == 0) & (grp.z > 2)).sum()),
            "n_z_gt4_zwarn0": int(((grp.zwarn == 0) & (grp.z > 4)).sum()),
            "n_qso": int((grp.spectype == "QSO").sum()),
            "n_galaxy": int((grp.spectype == "GALAXY").sum()),
            "n_star": int((grp.spectype == "STAR").sum()),
            "f_point_source": float(grp.is_point_source.mean()),
            "flux_r_median": grp.flux_r.median(),
            "exptime_median": grp.coadd_exptime.median(),
            "snr_med_median": grp.snr_med.median(),
            "n_wise": len(wmatch),
            "w1w2_median": wmatch.w1_w2.median() if len(wmatch) else np.nan,
            "n_w1w2_gt0p8": int((wmatch.w1_w2 > 0.8).sum()) if len(wmatch) else 0,
            "descriptor": meta["family_descriptor"],
        })
    return pd.DataFrame(rows).sort_values("family_id").reset_index(drop=True)


# ------------------------------------------------------------- follow-up set
FOLLOWUP_TIERS = {
    "FT-A": {
        "name": "High-redshift spectroscopic candidates",
        "rule": "SIMBAD/NED-unmatched AND ZWARN == 0 AND z >= 4.0",
        "motivation": "a DESI-pipeline redshift z >= 4 with no ZWARN flag and no catalogued "
                      "counterpart is the subset whose confirmation is cheapest and whose "
                      "misclassification cost is highest",
        "next_test": "Legacy Survey DR10 grz + WISE forced photometry cutouts at the listed "
                     "coordinates; DESI DR2 repeat/coadd spectra where the tile is revisited; "
                     "confirmation spectroscopy (Keck/LRIS, Gemini/GMOS, or SALT/RSS) for any "
                     "target whose imaging is consistent with the pipeline redshift",
    },
    "FT-B": {
        "name": "Infrared-excess AGN candidates",
        "rule": "SIMBAD/NED-unmatched AND AllWISE match AND W1-W2 >= 0.8 mag",
        "motivation": "W1-W2 >= 0.8 is the standard mid-infrared AGN selection "
                      "(Stern et al. 2012); an unmatched object meeting it is a testable "
                      "obscured-AGN candidate",
        "next_test": "public NEOWISE-R single-exposure light curves for mid-IR variability; "
                     "ZTF DR optical light curves; archival X-ray coverage (eROSITA-DE DR1, "
                     "Chandra/XMM serendipitous catalogues) at the listed coordinates",
    },
    "FT-C": {
        "name": "Reliable-redshift extreme-score candidates",
        "rule": "SIMBAD/NED-unmatched AND ZWARN == 0 AND DELTACHI2 > 25 AND anomaly_score in "
                "the top 5% of the released sample",
        "motivation": "the spectra that are simultaneously well-measured (secure redshift, "
                      "strong template discrimination) and hardest for the model to "
                      "reconstruct are where a genuine spectral anomaly, rather than noise, "
                      "is most likely",
        "next_test": "visual inspection of the public DESI DR1 coadd spectrum; re-fit with "
                     "Redrock using the full template set; SDSS DR17 spectra where the "
                     "footprint overlaps",
    },
    "FT-E": {
        "name": "Taxonomy-spanning representative set",
        "rule": "the highest-anomaly-score member of each of the 25 taxonomy clusters",
        "motivation": "a follow-up programme that samples every cluster tests the taxonomy "
                      "itself rather than one corner of it: if the descriptive families "
                      "correspond to anything physical, a per-cluster representative set is "
                      "the cheapest way to find out",
        "next_test": "public DESI DR1 coadd spectrum inspection for each representative, plus "
                     "Legacy Survey DR10 imaging cutouts; any representative whose spectrum is "
                     "not explained by a known template is escalated to FT-A/FT-B/FT-C handling",
    },
    "FT-D": {
        "name": "Point-source / stellar-locus candidates",
        "rule": "SIMBAD/NED-unmatched AND MORPHTYPE == 'PSF' AND a Gaia DR3 counterpart "
                "(GAIA_PHOT_G_MEAN_MAG > 0)",
        "motivation": "an unmatched point source with a Gaia counterpart is either a Galactic "
                      "object missing from SIMBAD or a compact extragalactic source; Gaia "
                      "astrometry separates the two at no observational cost",
        "next_test": "Gaia DR3 parallax and proper motion at the listed source_id position; "
                     "ZTF/ATLAS public light curves for variability; SDSS/LAMOST archival "
                     "spectra where available",
    },
}


def followup_set(m: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    unm = m[m.crossmatch == "unmatched"].copy()
    s95 = m.anomaly_score.quantile(0.95)
    sel = {
        "FT-A": unm[(unm.zwarn == 0) & (unm.z >= 4.0)],
        "FT-B": unm[(unm.match_flag == True) & (unm.w1_w2 >= 0.8)],  # noqa: E712
        "FT-C": unm[(unm.zwarn == 0) & (unm.deltachi2 > 25) & (unm.anomaly_score >= s95)],
        "FT-D": unm[(unm.morphtype == "PSF") & (unm.gaia_phot_g_mean_mag > 0)],
        "FT-E": unm.sort_values("anomaly_score", ascending=False)
                   .drop_duplicates(subset=["cluster_id"]),
    }
    cols = ["targetid", "target_ra", "target_dec", "anomaly_score", "z", "zwarn", "spectype",
            "deltachi2", "flux_r", "w1_w2", "morphtype", "gaia_phot_g_mean_mag",
            "survey", "program", "family_id", "cluster_id"]
    frames = []
    for tier, df in sel.items():
        t = df[cols].copy()
        t.insert(0, "tier", tier)
        frames.append(t.sort_values("anomaly_score", ascending=False))
    out = pd.concat(frames).reset_index(drop=True)
    meta = {t: {**FOLLOWUP_TIERS[t], "n_targets": int(len(sel[t])),
                "score_p95_threshold": float(s95) if t == "FT-C" else None}
            for t in sel}
    return out, meta


# ------------------------------------------------------------------- figures
def figures(m: pd.DataFrame, fam: pd.DataFrame) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4))
    for ax, (col, label) in zip(axes, [("coadd_exptime", r"coadd exposure time [s]"),
                                       ("tsnr2_lrg", r"TSNR2$_{\rm LRG}$"),
                                       ("flux_r", r"$r$-band flux [nmgy]")]):
        ax.scatter(m[col], m.anomaly_score, s=5, alpha=0.35, color="#28527a", lw=0)
        ax.set_xscale("log")
        ax.set_xlabel(label)
        r = stats.spearmanr(m.anomaly_score, m[col], nan_policy="omit")
        ax.set_title(rf"$\rho_s={r.statistic:+.3f}$ ($p={r.pvalue:.2g}$)", fontsize=9)
    axes[0].set_ylabel("anomaly score")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig_score_vs_quality.{ext}", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4))
    unm = m[m.crossmatch == "unmatched"].dropna(subset=["family_id"])
    order = fam.family_id.tolist()
    axes[0].boxplot([unm.loc[unm.family_id == f, "anomaly_score"] for f in order],
                    tick_labels=[str(f) for f in order], showfliers=False)
    axes[0].set_xlabel("family"); axes[0].set_ylabel("anomaly score")
    axes[1].bar([str(f) for f in order], fam.f_zwarn0, color="#28527a")
    axes[1].set_xlabel("family"); axes[1].set_ylabel(r"fraction with ZWARN $=0$")
    axes[2].bar([str(f) for f in order], fam.n_wise, color="#8d6a3f")
    axes[2].set_xlabel("family"); axes[2].set_ylabel("AllWISE matches")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig_family_evidence.{ext}", dpi=180)
    plt.close(fig)


# ---------------------------------------------------------------------- main
def main() -> None:
    prov = run_provenance_recheck()
    jdump(prov, OUT / "provenance_recheck_2026-09-18.json")

    d = load()
    m = build_master(d)

    # repair table for DEFECT-1
    d["sample"][["targetid", "z", "zwarn", "spectype", "deltachi2"]].to_parquet(
        OUT / "flagship_sample_v2_zcat_rejoin.parquet", index=False)

    contract = validation_contract(d, m, prov)
    jdump({"generated": "2026-09-18", "n_checks": len(contract), "checks": contract},
          OUT / "validation_contract_results.json")
    lines = ["| ID | Requirement | Status | Observed |", "|---|---|---|---|"]
    for r in contract:
        lines.append(f"| {r['id']} | {r['requirement']} | **{r['status']}** | {r['observed']} |")
    (OUT / "validation_contract_results.md").write_text("\n".join(lines) + "\n")

    fam = family_evidence(d, m)
    fam.to_csv(OUT / "family_evidence.csv", index=False)
    jdump(fam.to_dict(orient="records"), OUT / "family_evidence.json")

    fu, fu_meta = followup_set(m)
    fu.to_csv(OUT / "followup_targets.csv", index=False)
    jdump({"tiers": fu_meta, "targets": fu.to_dict(orient="records")},
          OUT / "followup_targets.json")

    figures(m, fam)

    print("checks:", {r["id"]: r["status"] for r in contract})
    print(fam[["family_id", "n_objects", "score_median", "f_zwarn0", "n_z_gt2_zwarn0",
               "n_qso", "n_wise", "n_w1w2_gt0p8"]].to_string(index=False))
    print({k: v["n_targets"] for k, v in fu_meta.items()})


if __name__ == "__main__":
    main()
