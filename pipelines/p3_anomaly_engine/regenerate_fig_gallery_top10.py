#!/usr/bin/env python3
"""
Regenerate ONLY figures/fig_gallery_top10.{pdf,png} — P3 v3.1.80 closure
(R22prov OpenAI-E7: undefined burned-in "AE" raw-residual values removed).

Reuses generate_gallery_figures.py (taxonomy loader, cutout cache, layout);
the _sublabel() fix there drops the unnormalized taxonomy-pipeline residual
scores from the panel labels (RA only; the high-z QSO panel shows z and the
per-arm Z-arm sub-score r_Z, which is defined in the paper).

Run from pipelines/p3_anomaly_engine/:  python3 regenerate_fig_gallery_top10.py
"""
import generate_gallery_figures as G


def main():
    print("Loading DESI taxonomy catalog...", flush=True)
    families = G.load_taxonomy()

    family_order = [
        "High-z QSO", "QSO", "AGN", "BAL-QSO", "ELG",
        "LRG", "Post-starburst", "Blue-compact", "Star", "Unknown",
    ]

    top_per_family = []
    for fam in family_order:
        if fam == "High-z QSO":
            obj = dict(G.HIGHZ_QSO_OBJECTS[0])
            obj["label"] = "High-z QSO"
            top_per_family.append(obj)
            continue
        items = families.get(fam, [])[:10]
        picked = None
        for candidate in items:
            img = G.fetch_cutout(candidate["ra"], candidate["dec"])
            if G._is_real_image(img):
                picked = dict(candidate)
                picked["label"] = fam
                break
            print(f"  [top10 skip] {candidate['ra']:.1f},{candidate['dec']:.1f}"
                  " — no coverage, trying next", flush=True)
        if picked is not None:
            top_per_family.append(picked)
        elif items:
            obj = dict(items[0])
            obj["label"] = fam
            top_per_family.append(obj)

    G.make_gallery_figure(
        objects=top_per_family,
        ncols=5,
        title="DESI DR1 Spectral Anomalies: Representative Objects by Taxonomy Family",
        subtitle=(
            "One highest-scoring anomaly per family. "
            "grz RGB composites from DESI Legacy Survey. "
            "Border color indicates taxonomy class."
        ),
        outname="fig_gallery_top10",
        show_family_label=True,
    )


if __name__ == "__main__":
    main()
