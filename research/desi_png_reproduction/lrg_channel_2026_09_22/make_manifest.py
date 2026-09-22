#!/usr/bin/env python3
"""Q2 reproducibility manifest for the ledger row 4 LRG channel."""
import hashlib
import json
import os
import platform
import subprocess

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce"
LANE = "research/desi_png_reproduction/lrg_channel_2026_09_22"
OUT = f"{HERE}/{LANE}/outputs"
DEST = f"{HERE}/reproducibility/manifests/experiments/ledger4-desi-dr1-lrg-fnl-channel.json"

CODE = ["http_stream.py", "lrg_official_io.py", "lrg_fit_core.py",
        "stream_lrg_cache.py", "fit_lrg_headline.py", "pk_lrg_splits.py",
        "fit_lrg_splits.py", "compare_lrg_qso.py", "tests/regress_qso.py"]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    stream = json.load(open(f"{OUT}/stream_manifest.json"))
    head = json.load(open(f"{OUT}/fnl_lrg_headline.json"))
    cmp_ = json.load(open(f"{OUT}/lrg_vs_qso.json"))
    tab = json.load(open(f"{OUT}/systematics_table_lrg.json")) if os.path.exists(
        f"{OUT}/systematics_table_lrg.json") else {}
    pk_files = sorted(os.listdir(f"{OUT}/pk")) if os.path.isdir(f"{OUT}/pk") else []
    pk_secs = 0.0
    for f in pk_files:
        try:
            pk_secs += json.load(open(f"{OUT}/pk/{f}"))["seconds"]
        except Exception:
            pass
    cat_sha = {k: dict(url=v["url"], sha256=v["sha256"], bytes=v["bytes"],
                       nrows_file=v["nrows_file"], nrows_kept=v["nrows_kept"])
               for k, v in stream.items() if not k.startswith("_")}
    total_streamed = stream["_total_streamed_bytes"] + head["streamed_bytes"]
    man = {
        "manifest_version": "bigbounce-experiment/v1",
        "id": "ledger4-desi-dr1-lrg-fnl-channel",
        "title": ("Ledger #4 - LRG channel of the DESI DR1 scale-dependent-bias "
                  "f_NL^loc measurement, opened at the v5 QSO fidelity by HTTP-range "
                  "streaming (zero bulk catalogue bytes on disk): headline f_NL per "
                  "z-bin and combined, the same 5-row systematics table, and the "
                  "LRG-vs-QSO comparison on one convention"),
        "program": "bounce-theory",
        "paper": "A3",
        "kind": "analysis",
        "inputs": [
            {"name": "Official DESI DR1 full-shape-bao-clustering v1.0 VAC - LRG "
                     "window matrix, measured P_ell and EZmock covariance, all three "
                     "z-bins (z0.4-0.6, z0.6-0.8, z0.8-1.1), GCcomb",
             "type": "external-dataset",
             "locator": "https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/v1.0/data/",
             "checksum": ("sha256 of the exact streamed bytes for each of the 9 files "
                          "recorded in " + LANE + "/outputs/fnl_lrg_headline.json "
                          "(\"sha256\" block); streamed by HTTP range read into "
                          "memory with h5py's fileobj driver, never written to disk"),
             "license": "CC BY 4.0 (DESI public data releases)"},
            {"name": "DESI DR1 LRG clustering + randoms catalogues (LSScats v1.5), "
                     "NGC+SGC, 4 random realisations per cap - same catalogue version "
                     "v5 used for QSO",
             "type": "external-dataset",
             "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
             "checksum": ("whole-file sha256 for each of the 10 files in " + LANE +
                          "/outputs/stream_manifest.json, computed during a single "
                          "sequential byte-0-to-EOF pass; only RA/DEC/Z/WEIGHT/"
                          "WEIGHT_SYS/WEIGHT_FKP were kept in memory and no bulk "
                          "catalogue was written to disk"),
             "license": "CC BY 4.0 (DESI public data releases)"},
            {"name": "Legacy Survey DR9 imaging pixweight map (main/dark, nside 256 "
                     "nested) for EBV / STARDENS / GALDEPTH_Z - local, same file v4 used",
             "type": "external-dataset",
             "locator": "bigbounce_datasets/desi_dr1_lss/imaging_pixweight/pixweight-dark.fits",
             "checksum": "sha256 in imaging_pixweight/pixweight-dark.fits.sha256",
             "license": "CC BY 4.0"},
            {"name": "v3/v5 QSO headline (comparison baseline, unchanged)",
             "type": "internal-artifact",
             "locator": "research/desi_png_reproduction/outputs/fnl_official_nshot0_summary.json",
             "checksum": None},
            {"name": "Chaussidon et al. 2024 - DESI DR1 LRG+QSO local PNG constraint",
             "type": "external-literature",
             "locator": "https://arxiv.org/abs/2411.17623", "checksum": None,
             "license": None},
            {"name": "Streaming pattern reused from lane bb-LS10-indomain-d180",
             "type": "internal-artifact",
             "locator": "pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/run_indomain_rotations.py",
             "checksum": None},
        ],
        "apis": [{"name": "DESI public data server (anonymous HTTP range requests, no key)",
                  "endpoint": "https://data.desi.lbl.gov/public/dr1/",
                  "auth_required": False}],
        "code": [{"path": f"{LANE}/{c}", "entrypoint": f"python3 {c}",
                  "sha256": sha(f"{HERE}/{LANE}/{c}")} for c in CODE],
        "environment": {
            "python": ("python3.12.13 (research/desi_png_reproduction/.venv312, "
                       "gitignored): numpy 2.5.2, scipy 1.18.1, h5py 3.16.0, "
                       "fitsio 1.4.2, healpy 1.20.0, astropy 8.0.1, camb 2.0.4, "
                       "pypower 1.0.0, cosmoprimo 1.0.0"),
            "hardware": (f"cpu-only, ~4 GB RAM peak, >=3 GB free disk; Apple M-series "
                         f"MacBook Air, macOS {platform.release()} {platform.machine()}"),
        },
        "original_run": {
            "venue": "local",
            "gpu": None,
            "pod_id_or_host": platform.node(),
            "date": "2026-09-22",
            "wall_clock": (
                f"streamed {total_streamed} B ({total_streamed/1e9:.2f} GB) total: "
                f"{stream['_total_streamed_bytes']} B of LRG catalogues + randoms in "
                f"{sum(v['seconds'] for k, v in stream.items() if not k.startswith('_')):.0f} s "
                f"and {head['streamed_bytes']} B of official VAC products; "
                f"bulk catalogue bytes written to disk = 0; peak disk = "
                f"{stream['_cache_bytes']} B ({stream['_cache_bytes']/1e9:.2f} GB) of "
                f"derived float32 columns outside the repo "
                f"(bigbounce_datasets/desi_dr1_lss/lrg_stream_cache, 10 files, "
                f"59,525,171 rows); headline fit {head['wall_seconds']:.0f} s; "
                f"{len(pk_files)} pypower P(k) measurements totalling {pk_secs:.0f} s"),
            "actual_cost_usd": 0.0,
        },
        "reproduction": {
            "recommended_venue": "local",
            "est_wall_clock": "~10 min to stream the 6.2 GB cache + ~1 h for the 60 "
                              "P(k) measurements + ~25 min of fits",
            "est_cost_usd": 0.0,
            "parallelizable": True,
            "resume_support": True,
            "notes": ("Needs >=3 GB free disk. No pre-downloaded product is required: run stream_lrg_cache.py "
                      "(6.2 GB over the wire, 2.4 GB derived cache), then "
                      "fit_lrg_headline.py (streams the 652 MB of official products), "
                      "then pk_lrg_splits.py (resumable per measurement) and "
                      "fit_lrg_splits.py, then compare_lrg_qso.py. "
                      "tests/regress_qso.py is a hard gate: it must reproduce v5's "
                      "published QSO headline before any LRG number is believed, and "
                      "it needs the local QSO official_products/ from v3."),
        },
        "outputs": [
            {"locator": f"{LANE}/outputs/fnl_lrg_headline.json", "type": "result-json"},
            {"locator": f"{LANE}/outputs/systematics_table_lrg.json", "type": "result-json"},
            {"locator": f"{LANE}/outputs/lrg_vs_qso.json", "type": "result-json"},
            {"locator": f"{LANE}/outputs/stream_manifest.json", "type": "result-json"},
            {"locator": f"{LANE}/outputs/regress_qso.json", "type": "result-json"},
            {"locator": f"{LANE}/outputs/split_medians.json", "type": "result-json"},
            {"locator": f"{LANE}/LEDGER4_LRG_RESULT_2026-09-22.md", "type": "document"},
            {"locator": f"{LANE}/RUN_LOG.md", "type": "document"},
            {"locator": f"{LANE}/PROPAGATION_NOTE.md", "type": "document"},
            {"locator": f"{LANE}/PRE_REGISTRATION.md", "type": "document"},
        ],
        "verification": ("Re-run tests/regress_qso.py: it must reproduce v5's published "
                         "QSO headline (p=1.6 f_NL=-2.169, p=1.0 f_NL=-1.127, b1=2.24932, "
                         "chi2=62.401, 48 data bins) to within 2% of sigma, and "
                         "verify_quadratic must stay below 1e-9. Then re-run the LRG "
                         "chain and confirm the headline, the 5-row table verdicts and "
                         "the LRG-vs-QSO |T| reported in "
                         f"{LANE}/LEDGER4_LRG_RESULT_2026-09-22.md."),
        "status": "runnable-now",
        "provenance": [
            "project-context/NEXT_SCIENCE_LEDGER.md item 4",
            "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md",
            "research/desi_png_reproduction/LEDGER4_RESULT_v5_2026-09-04.md "
            "(the QSO channel this one is matched to)",
            f"{LANE}/PRE_REGISTRATION.md",
            f"{LANE}/RUN_LOG.md",
            "directive Q2 (reproducibility manifests), R1 (ledger-first), "
            "R6 (claims at their evidential strength)",
        ],
    }
    schema = json.load(open(f"{HERE}/reproducibility/manifests/experiment.schema.json"))
    try:
        import jsonschema
        jsonschema.validate(man, schema)
        print("schema: VALID")
    except ImportError:
        print("schema: jsonschema not installed -- checking required keys only")
        missing = [k for k in schema["required"] if k not in man]
        extra = [k for k in man if k not in schema["properties"]]
        assert not missing and not extra, (missing, extra)
        print("schema: required/extra key check OK")
    json.dump(man, open(DEST, "w"), indent=2)
    print(f"wrote {DEST}")


if __name__ == "__main__":
    main()
