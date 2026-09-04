"""
Ledger #4, step 1 - lab-native sanity check on the DESI DR1 public LSS
clustering catalogues (QSO, v1.5) downloaded to
~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/.

This is deliberately NOT a measurement.  It answers only: did we get the file
DESI serves, does it contain what the DR1 PNG analysis says it contains, and
are the columns the plan's sections 2-3.4 depend on actually present?

Checks
  1. sha256 of every downloaded file (provenance binding for the manifest).
  2. Row counts per cap, and the QSO total against Chaussidon et al. 2024
     (arXiv:2411.17623): 1,189,129 QSOs in 0.8 < z < 3.1.
  3. Redshift histogram (both caps) + the published z-range occupancy.
  4. Footprint sky plot (RA/Dec, equal-area Mollweide) with NGC/SGC coloured.
  5. Weight-column inventory and summary stats - in particular WEIGHT_SYS,
     the imaging-systematics weight that section 3.4 test 1 switches off.

Outputs: outputs/dr1_lss_sanity.json, outputs/dr1_lss_sanity_zhist.png,
         outputs/dr1_lss_sanity_footprint.png
Venue: local, CPU only, no GPU, cost $0.

Data licence: CC BY 4.0 (DESI public data releases).  Required acknowledgment:
"This research used data obtained with the Dark Energy Spectroscopic Instrument
(DESI). DESI construction and operations is managed by the Lawrence Berkeley
National Laboratory."
"""
from __future__ import annotations
import hashlib, json, time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from astropy.io import fits

DATA = Path.home() / "Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss"
HERE = Path(__file__).resolve().parent
OUTD = HERE / "outputs"
OUTD.mkdir(exist_ok=True)

# Chaussidon et al. 2024, arXiv:2411.17623, abstract (verbatim numbers)
PUBLISHED = {
    "reference": "Chaussidon et al. 2024, arXiv:2411.17623 (abstract)",
    "n_qso": 1189129,
    "z_range": [0.8, 3.1],
    "n_lrg": 1631716,
    "lrg_z_range": [0.6, 1.1],
    "fnl_merger_model": {"central": -3.6, "plus": 9.0, "minus": 9.1, "cl": 0.68},
    "fnl_universality": {"central": 3.5, "plus": 10.7, "minus": 7.4, "cl": 0.68},
}
CAPS = ["NGC", "SGC"]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    t0 = time.time()
    out: dict = {
        "task": "Ledger #4 step 1 - DESI DR1 public LSS (QSO v1.5) sanity check",
        "published_reference": PUBLISHED,
        "source_root": ("https://data.desi.lbl.gov/public/dr1/survey/catalogs/"
                        "dr1/LSS/iron/LSScats/v1.5/"),
        "licence": "CC BY 4.0 (DESI public data releases)",
        "files": {}, "caps": {}, "weights": {}, "checks": {},
    }

    for p in sorted(DATA.iterdir()):
        if p.is_file():
            out["files"][p.name] = {"bytes": p.stat().st_size, "sha256": sha256(p)}

    ra_all, dec_all, z_all, cap_all = [], [], [], []
    n_total = 0
    for cap in CAPS:
        f = DATA / f"QSO_{cap}_clustering.dat.fits"
        with fits.open(f, memmap=True) as hdul:
            t = hdul[1].data
            cols = [c.name for c in hdul[1].columns]
            z = np.asarray(t["Z"], float)
            ra = np.asarray(t["RA"], float)
            dec = np.asarray(t["DEC"], float)
        n = z.size
        n_total += n
        ra_all.append(ra); dec_all.append(dec); z_all.append(z)
        cap_all.append(np.full(n, cap))
        lo, hi = PUBLISHED["z_range"]
        out["caps"][cap] = {
            "file": f.name, "n_rows": int(n), "n_columns": len(cols),
            "columns": cols,
            "z_min": float(z.min()), "z_max": float(z.max()),
            "z_median": float(np.median(z)),
            "n_in_published_z_range": int(((z >= lo) & (z <= hi)).sum()),
            "frac_in_published_z_range": float(((z >= lo) & (z <= hi)).mean()),
            "ra_range": [float(ra.min()), float(ra.max())],
            "dec_range": [float(dec.min()), float(dec.max())],
        }
        # weight columns
        with fits.open(f, memmap=True) as hdul:
            t = hdul[1].data
            wcols = [c for c in cols if c.startswith("WEIGHT") or c in ("NX", "NZ")]
            out["weights"][cap] = {}
            for c in wcols:
                v = np.asarray(t[c], float)
                finite = np.isfinite(v)
                out["weights"][cap][c] = {
                    "mean": float(v[finite].mean()), "std": float(v[finite].std()),
                    "min": float(v[finite].min()), "max": float(v[finite].max()),
                    "n_nonfinite": int((~finite).sum()),
                    "n_exactly_one": int((v == 1.0).sum()),
                }

    ra = np.concatenate(ra_all); dec = np.concatenate(dec_all)
    z = np.concatenate(z_all); capv = np.concatenate(cap_all)

    # randoms: row count + column presence only (large file, no plotting)
    rf = DATA / "QSO_SGC_0_clustering.ran.fits"
    with fits.open(rf, memmap=True) as hdul:
        rcols = [c.name for c in hdul[1].columns]
        n_ran = int(hdul[1].header["NAXIS2"])
    out["randoms"] = {
        "file": rf.name, "n_rows": n_ran, "columns": rcols,
        "ratio_to_SGC_data": round(n_ran / out["caps"]["SGC"]["n_rows"], 2),
        "note": "one of 18 realisations (0..17); the plan's section 2 volume table",
    }

    lo, hi = PUBLISHED["z_range"]
    n_pub_range = int(((z >= lo) & (z <= hi)).sum())
    out["checks"] = {
        "n_qso_total_downloaded": int(n_total),
        "n_qso_published": PUBLISHED["n_qso"],
        "n_qso_in_published_z_range": n_pub_range,
        "ratio_zrange_to_published": round(n_pub_range / PUBLISHED["n_qso"], 4),
        "abs_diff_zrange_vs_published": int(n_pub_range - PUBLISHED["n_qso"]),
        "WEIGHT_SYS_present": all("WEIGHT_SYS" in out["caps"][c]["columns"] for c in CAPS),
        "WEIGHT_FKP_present": all("WEIGHT_FKP" in out["caps"][c]["columns"] for c in CAPS),
        "verdict_note": (
            "The clustering catalogue carries the full tracer sample; the published "
            "1,189,129 is the count entering the PNG fit after its own z-cut and any "
            "further selection. Agreement of the z-range count to within a few percent "
            "is the pass condition here; an exact match is NOT expected and is not claimed."
        ),
    }

    # --- figures ---
    fig, ax = plt.subplots(figsize=(7, 4))
    for cap, colr in zip(CAPS, ["#1f77b4", "#d62728"]):
        ax.hist(z[capv == cap], bins=np.arange(0.0, 4.05, 0.05), histtype="step",
                lw=1.6, color=colr, label=f"QSO {cap} (N={int((capv==cap).sum()):,})")
    ax.axvline(lo, ls="--", c="k", lw=1); ax.axvline(hi, ls="--", c="k", lw=1)
    ax.set_xlabel("redshift z"); ax.set_ylabel("N per Δz = 0.05")
    ax.set_title("DESI DR1 QSO clustering catalogue (v1.5)\ndashed: published PNG fit range 0.8 < z < 3.1", fontsize=10)
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(OUTD / "dr1_lss_sanity_zhist.png", dpi=140); plt.close(fig)

    fig = plt.figure(figsize=(9, 5))
    ax = fig.add_subplot(111, projection="mollweide")
    step = max(1, ra.size // 200000)
    lam = np.radians(((ra[::step] + 180) % 360) - 180)
    phi = np.radians(dec[::step])
    for cap, colr in zip(CAPS, ["#1f77b4", "#d62728"]):
        m = capv[::step] == cap
        ax.scatter(lam[m], phi[m], s=0.12, c=colr, lw=0, label=f"QSO {cap}")
    ax.grid(True, lw=0.3, alpha=0.5)
    ax.set_title("DESI DR1 QSO clustering footprint (v1.5), equatorial Mollweide", fontsize=10)
    ax.legend(markerscale=30, fontsize=8, loc="lower right")
    fig.tight_layout(); fig.savefig(OUTD / "dr1_lss_sanity_footprint.png", dpi=140); plt.close(fig)

    out["wall_clock_s"] = round(time.time() - t0, 1)
    (OUTD / "dr1_lss_sanity.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out["checks"], indent=2))
    print("rows:", {c: out["caps"][c]["n_rows"] for c in CAPS}, "randoms:", n_ran)
    print("wall clock", out["wall_clock_s"], "s")


if __name__ == "__main__":
    main()
