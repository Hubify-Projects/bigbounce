#!/usr/bin/env python3
"""Figures and tables for the full anomaly-flagship draft (vAF.0.2).

Extends `assemble_flagship_evidence.py` (whose loaders and joins are reused
verbatim, so the numbers here and there cannot diverge) with the products the
full manuscript needs beyond the vAF.0.1 skeleton:

figures/
  fig_score_distribution.pdf   released-sample score histogram + survival curve
  fig_sky_distribution.pdf     Mollweide sky map, matched vs unmatched, FT-A marked
  fig_band_residuals.pdf       score vs per-camera residual (the V11 result)
  fig_redshift_distribution.pdf  ZWARN==0 redshifts by SPECTYPE, z>=4 marked
  fig_latent_silhouette.pdf    V12 silhouette against its permutation null

tables/ (written into ../anomaly_flagship_draft/tables/)
  tab_provenance_chain.tex     the eight hash-bound links of the run contract
  tab_catalogue_schema.tex     released column groups
  tab_sky_fraction.tex         per-score-bin fibre census (the V9 numbers)
  tab_counterpart_types.tex    SIMBAD/NED counterpart-type breakdown
  tab_family_sky.tex           per-family survey purity and sky extent
  tab_recovery_benchmark.tex   regenerated from recovery_benchmark.json (adds
                               recovery fraction, 95% CI and base rate)
  tab_ft_a.tex                 the four FT-A z>=4 candidates with Legacy g/r/z

outputs/
  draft_numbers.json           every derived number the manuscript prose quotes

CPU only, no network, deterministic (the V12 null is seeded, 50 draws).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble_flagship_evidence as afe  # noqa: E402  (shared loaders/joins)

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "outputs"
FIG = HERE / "figures"
DRAFT = HERE.parent / "anomaly_flagship_draft"
DFIG = DRAFT / "figures"
DTAB = DRAFT / "tables"
BENCH = afe.PHASE3 / "recovery_benchmark/recovery_benchmark.json"
CALIB = afe.REPO / "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/calibration.json"
for p in (OUT, FIG, DFIG, DTAB):
    p.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
    "figure.dpi": 200, "savefig.bbox": "tight", "axes.grid": True,
    "grid.alpha": 0.25, "grid.linewidth": 0.4,
})
C_MATCH, C_UNMATCH, C_ACC = "#4C72B0", "#C44E52", "#55A868"


def save(fig, name: str) -> None:
    for d in (FIG, DFIG):
        fig.savefig(d / f"{name}.pdf")
    fig.savefig(FIG / f"{name}.png", dpi=200)
    plt.close(fig)


def texnum(n: int) -> str:
    return f"{n:,}".replace(",", "{,}")


def esc(s) -> str:
    """LaTeX-escape a raw requirement/label string from a JSON artifact.

    These strings contain shell- and code-like characters (`>`, `<`, `|`,
    `->`, `_`) that OT1 text mode silently renders as the wrong glyph, so the
    escaping has to be explicit rather than left to LaTeX.
    """
    s = str(s)
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                 ("#", r"\#"), ("_", r"\_"), ("$", r"\$"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
                 ("->", r"$\to$"), (">", "$>$"), ("<", "$<$"), ("|", "$|$")):
        s = s.replace(a, b)
    return s


# --------------------------------------------------------------------- figures
def fig_score_distribution(m: pd.DataFrame, d: dict, nums: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.6))
    ax = axes[0]
    bins = np.logspace(np.log10(3.0), np.log10(m.anomaly_score.max() * 1.02), 28)
    for lab, col, c in (("SIMBAD/NED matched", "matched", C_MATCH),
                        ("unmatched", "unmatched", C_UNMATCH)):
        ax.hist(m.loc[m.crossmatch == col, "anomaly_score"], bins=bins,
                histtype="step", lw=1.2, color=c, label=lab)
    ax.set_xscale("log"), ax.set_yscale("log")
    ax.set_xlabel(r"anomaly score $S$"), ax.set_ylabel("objects per bin")
    ax.legend(frameon=False, loc="upper right")

    ax = axes[1]
    grid = [3, 4, 5, 6, 8, 10]
    allf = [320418, 86053, 52188, 27180, 3810, 337]          # science_target_summary.json
    sci = [d["threshold"]["counts_by_threshold"][str(g)] for g in grid]
    ax.plot(grid, allf, "o-", color="0.35", lw=1.2, ms=3.5, label="all fibres")
    ax.plot(grid, sci, "s-", color=C_ACC, lw=1.2, ms=3.5, label="science targets")
    ax.axvline(3, color=C_UNMATCH, ls="--", lw=0.9)
    ax.annotate("released cut", (3, 4e2), xytext=(3.6, 4e2), color=C_UNMATCH,
                fontsize=7, va="center")
    ax.set_yscale("log")
    ax.set_xlabel(r"threshold $S>$"), ax.set_ylabel(r"$N(>S)$")
    ax.legend(frameon=False)
    save(fig, "fig_score_distribution")
    nums["score_min"] = float(m.anomaly_score.min())
    nums["score_max"] = float(m.anomaly_score.max())
    nums["score_median_released"] = float(m.anomaly_score.median())
    nums["score_p90_released"] = float(m.anomaly_score.quantile(0.90))


def fig_sky_fraction(d: dict) -> None:
    """The V9 curve, redrawn from the released JSON on a readable scale.

    The landed run's own PNG plots the fraction on a 0-1 axis, where every bar
    is visually identical at ~1.0 and the rise with score is invisible.
    """
    bins = d["sky_fraction"]["bins"]
    x = np.arange(len(bins))
    frac = np.array([b["sky_or_nonscience_fraction"] for b in bins]) * 100.0
    sci = np.array([b["science_target_count"] for b in bins])
    tot = np.array([b["total"] for b in bins])

    fig, axes = plt.subplots(2, 1, figsize=(3.4, 3.4), sharex=True,
                             gridspec_kw={"height_ratios": [1.5, 1.0]})
    ax = axes[0]
    ax.plot(x, frac, "o-", color=C_UNMATCH, lw=1.3, ms=4)
    ax.set_ylim(99.4, 100.02)
    ax.axhline(99.5, color="0.5", ls="--", lw=0.8)
    ax.annotate(r"$99.5\%$", (0, 99.5), xytext=(2, 3), textcoords="offset points",
                fontsize=6.5, color="0.4")
    ax.set_ylabel("sky/non-science (%)")

    ax = axes[1]
    ax.bar(x - 0.2, tot, 0.4, color="0.45", label="all fibres")
    ax.bar(x + 0.2, sci, 0.4, color=C_ACC, label="science targets")
    ax.set_yscale("log")
    ax.set_ylabel("fibres in bin")
    ax.set_xticks(x)
    ax.set_xticklabels([b["bin"] for b in bins], fontsize=6.5, rotation=20)
    ax.set_xlabel(r"anomaly-score bin")
    ax.legend(frameon=False, fontsize=6.5)
    save(fig, "fig_sky_fraction")


def fig_sky_distribution(m: pd.DataFrame, fu: pd.DataFrame) -> None:
    fig = plt.figure(figsize=(7.0, 3.4))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.grid(alpha=0.25, lw=0.4)

    def rad(ra, dec):
        r = np.asarray(ra, dtype=float).copy()
        r = np.where(r > 180.0, r - 360.0, r)
        return np.deg2rad(r), np.deg2rad(np.asarray(dec, dtype=float))

    for lab, col, c, s in (("SIMBAD/NED matched", "matched", C_MATCH, 3.0),
                           ("unmatched", "unmatched", C_UNMATCH, 3.0)):
        sub = m[m.crossmatch == col]
        x, y = rad(sub.target_ra, sub.target_dec)
        ax.scatter(x, y, s=s, c=c, alpha=0.55, lw=0, label=lab)
    fta = fu[fu.tier == "FT-A"]
    x, y = rad(fta.target_ra, fta.target_dec)
    ax.scatter(x, y, s=42, facecolors="none", edgecolors="k", lw=1.0,
               label=r"FT-A ($z\geq4$ candidates)")
    ax.set_xticklabels([])
    ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, -0.22), ncol=3)
    save(fig, "fig_sky_distribution")


def fig_band_residuals(m: pd.DataFrame, nums: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.4), sharey=True)
    out = {}
    for ax, band, c in zip(axes, ("B", "R", "Z"), (C_MATCH, C_ACC, "#8172B2")):
        col = f"r{band}"
        sub = m[["anomaly_score", col]].dropna()
        r = stats.spearmanr(sub.anomaly_score, sub[col])
        out[band] = {"rho": float(r.statistic), "p": float(r.pvalue), "n": int(len(sub))}
        ax.scatter(sub[col], sub.anomaly_score, s=2.5, c=c, alpha=0.45, lw=0)
        ax.set_yscale("log")
        ax.set_xlabel(rf"$r_{{{band}}}$ (per-camera residual)")
        ax.set_title(rf"$\rho_s={r.statistic:+.3f}$", fontsize=8)
    axes[0].set_ylabel(r"anomaly score $S$")
    save(fig, "fig_band_residuals")
    nums["band_residual_spearman"] = out
    nums["band_residual_medians"] = {b: float(m[f"r{b}"].median()) for b in ("B", "R", "Z")}


def fig_redshift_distribution(m: pd.DataFrame, nums: dict) -> None:
    z0 = m[m.zwarn == 0]
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.5))
    ax = axes[0]
    bins = np.linspace(0, 7, 36)
    for lab, c in (("GALAXY", C_MATCH), ("QSO", C_UNMATCH), ("STAR", "0.35")):
        v = z0.loc[z0.spectype == lab, "z"]
        if len(v):
            ax.hist(v, bins=bins, histtype="step", lw=1.2, color=c,
                    label=f"{lab} ({len(v)})")
    ax.axvline(4.0, color="k", ls=":", lw=0.9)
    ax.set_yscale("log")
    ax.set_xlabel(r"DESI pipeline redshift $z$ ($\mathtt{ZWARN}=0$)")
    ax.set_ylabel("objects per bin")
    ax.legend(frameon=False)

    ax = axes[1]
    for lab, col, c in (("matched", "matched", C_MATCH), ("unmatched", "unmatched", C_UNMATCH)):
        sub = z0[z0.crossmatch == col]
        ax.scatter(sub.z, sub.anomaly_score, s=3.5, c=c, alpha=0.6, lw=0, label=lab)
    ax.axvline(4.0, color="k", ls=":", lw=0.9)
    ax.set_yscale("log")
    ax.set_xlabel(r"$z$ ($\mathtt{ZWARN}=0$)"), ax.set_ylabel(r"anomaly score $S$")
    ax.legend(frameon=False)
    save(fig, "fig_redshift_distribution")

    nums["zwarn0_n"] = int(len(z0))
    nums["zwarn0_z_median"] = float(z0.z.median())
    nums["zwarn0_n_z_gt2"] = int((z0.z > 2).sum())
    nums["zwarn0_n_z_gt4"] = int((z0.z >= 4).sum())
    nums["zwarn0_n_z_gt6"] = int((z0.z >= 6).sum())
    nums["zwarn0_spectype"] = {k: int(v) for k, v in z0.spectype.value_counts().items()}
    nums["z_max_released"] = float(m.z[m.zwarn == 0].max())


def fig_latent_silhouette(m: pd.DataFrame, nums: dict) -> None:
    from sklearn.metrics import silhouette_score
    lat = [c for c in m.columns if c.startswith("latent_")]
    sub = m[m.crossmatch == "unmatched"].dropna(subset=["family_id"])
    X = sub[lat].to_numpy(dtype=float)
    X = (X - X.mean(0)) / np.where(X.std(0) == 0, 1.0, X.std(0))
    labels = sub.family_id.to_numpy(dtype=int)
    sil = float(silhouette_score(X, labels))
    rng = np.random.default_rng(42)
    null = np.array([silhouette_score(X, rng.permutation(labels)) for _ in range(50)])

    fig, ax = plt.subplots(figsize=(3.4, 2.4))
    ax.hist(null, bins=14, color="0.65", lw=0)
    ax.axvline(sil, color=C_UNMATCH, lw=1.5)
    ax.annotate(f"observed\n{sil:+.4f}", (sil, ax.get_ylim()[1] * 0.78),
                xytext=(-4, 0), textcoords="offset points", color=C_UNMATCH,
                fontsize=7, ha="right")
    ax.set_xlim(null.min() - 0.0015, sil + 0.0035)
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(5))
    ax.set_xlabel("silhouette over the 128 latent dimensions")
    ax.set_ylabel("permutation draws")
    save(fig, "fig_latent_silhouette")

    nums["latent_silhouette"] = sil
    nums["latent_null_mean"] = float(null.mean())
    nums["latent_null_sd"] = float(null.std())
    nums["latent_null_max"] = float(null.max())
    nums["latent_p_emp"] = float((null >= sil).mean())
    nums["latent_n_dims"] = len(lat)


def fig_fta_photometry(m: pd.DataFrame, nums: dict) -> None:
    """Legacy Survey grz fluxes of the four FT-A candidates against the sample.

    A Lyman break at the pipeline redshift requires the bands blueward of it to
    go dark. One candidate fails that test on public imaging alone.
    """
    recs = nums["ft_a"]
    fig, ax = plt.subplots(figsize=(3.4, 2.5))
    width, bands = 0.26, ("flux_g", "flux_r", "flux_z")
    colours = ("#4C72B0", "#C44E52", "#8172B2")
    xs = np.arange(len(recs))
    for i, (b, c) in enumerate(zip(bands, colours)):
        ax.bar(xs + (i - 1) * width, [r[b] for r in recs], width, color=c,
               label=b.split("_")[1])
    ax.axhline(float(m.flux_g.median()), color="0.35", ls="--", lw=0.9)
    ax.annotate("sample median $f_g$", (len(recs) - 0.55, float(m.flux_g.median())),
                xytext=(0, 4), textcoords="offset points", fontsize=6.5, color="0.35",
                ha="right")
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$z={r['z']:.2f}$" for r in recs], fontsize=7)
    ax.set_ylabel("Legacy Survey flux (nmgy)")
    ax.set_ylim(top=max(r["flux_g"] for r in recs) * 1.35)
    ax.legend(frameon=False, ncol=3, fontsize=7, loc="upper left")
    save(fig, "fig_fta_photometry")


# ---------------------------------------------------------------------- tables
def tab_provenance_chain(d: dict, nums: dict) -> None:
    rows = [
        ("run contract", "clean-rerun-6699d09ff886", afe.PHASE3.parent.parent /
         "sealed_2026-08-05/run-contract.json"),
    ]
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l l}",
             r"Artifact & SHA-256 (first 16 hex) \\", r"\hline"]
    chain = [
        ("DESI DR1 zcatalog \\texttt{zall-pix-iron.fits}",
         "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b"),
        ("sealed run contract (\\texttt{clean-rerun-6699d09ff886})",
         "6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf"),
        ("archived model \\texttt{best\\_model\\_47k.pt}",
         "f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07"),
        ("inference code",
         "3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996"),
    ]
    for name, h in chain:
        lines.append(f"{name} & \\texttt{{{h[:16]}\\ldots}} " + r"\\")
    for fname, h in sorted(afe.LANDING_SHA256.items()):
        lines.append(f"\\texttt{{{esc(fname)}}} & \\texttt{{{h[:16]}\\ldots}} " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_provenance_chain.tex").write_text("\n".join(lines) + "\n")
    nums["n_hashed_artifacts"] = len(chain) + len(afe.LANDING_SHA256)
    _ = rows


def tab_catalogue_schema(m: pd.DataFrame, nums: dict) -> None:
    groups = [
        ("identification", ["targetid", "target_ra", "target_dec", "survey", "program",
                            "healpix"]),
        ("anomaly", ["anomaly_score", "mean_mse", "rB", "rR", "rZ", "worst_band",
                     "peak_residual_wavelength", "residual_kurtosis"]),
        ("latent", [f"latent_{i:03d}" for i in range(128)]),
        ("DESI pipeline", ["z", "zerr", "zwarn", "spectype", "subtype", "deltachi2"]),
        ("exposure", ["coadd_numexp", "coadd_exptime", "median_coadd_snr_b",
                      "median_coadd_snr_r", "median_coadd_snr_z", "tsnr2_qso",
                      "tsnr2_elg", "tsnr2_lrg", "tsnr2_bgs"]),
        ("Legacy Survey photometry", ["flux_g", "flux_r", "flux_z", "flux_w1", "flux_w2",
                                      "morphtype", "sersic", "shape_r", "ebv", "parallax",
                                      "gaia_phot_g_mean_mag"]),
        ("AllWISE cross-match", ["w1", "w2", "w1_w2", "match_separation_arcsec",
                                 "match_flag"]),
        ("SIMBAD/NED cross-match", ["simbad_found", "simbad_main_id", "simbad_otype",
                                    "ned_found", "ned_name", "ned_type"]),
        ("taxonomy", ["cluster_id", "family_id", "family_descriptor", "is_core_member"]),
        ("derived colours, flags \\& join tags",
         ["mean_fiber_ra", "mean_fiber_dec", "gr_color", "rz_color", "w1w2_color",
          "is_point_source", "is_star_candidate", "crossmatch", "snr_med"]),
        ("unpopulated placeholder", ["classification", "discovery_potential"]),
    ]
    # rendered inside a full-width table* float in the manuscript
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r p{0.66\textwidth}}",
             r"Group & $N_{\rm col}$ & Columns \\", r"\hline"]
    total = 0
    for name, cols in groups:
        present = [c for c in cols if c in m.columns]
        total += len(present)
        if name == "latent":
            shown = r"\texttt{latent\_000}--\texttt{latent\_127}"
        else:
            shown = ", ".join(f"\\texttt{{{esc(c)}}}" for c in present)
        lines.append(f"{name} & {len(present)} & {shown} " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_catalogue_schema.tex").write_text("\n".join(lines) + "\n")
    nums["n_columns_joined"] = total
    nums["n_columns_master_frame"] = int(m.shape[1])


def tab_sky_fraction(d: dict, nums: dict) -> None:
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r r r}",
             r"Score bin & All fibres & Science targets & Sky/non-science \\", r"\hline"]
    for b in d["sky_fraction"]["bins"]:
        lines.append(f"${esc(b['bin'])}$ & {texnum(b['total'])} & "
                     f"{texnum(b['science_target_count'])} & "
                     f"{100*b['sky_or_nonscience_fraction']:.2f}\\% " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_sky_fraction.tex").write_text("\n".join(lines) + "\n")
    fr = [b["sky_or_nonscience_fraction"] for b in d["sky_fraction"]["bins"]]
    nums["sky_fraction_min"] = float(min(fr))
    nums["sky_fraction_max"] = float(max(fr))
    nums["parent_unique_targetids"] = int(d["sky_fraction"]["unique_targetids_all_shards"])
    nums["parent_raw_rows"] = int(d["sky_fraction"]["raw_rows_all_shards"])
    nums["parent_max_score"] = float(d["sky_fraction"]["max_score_observed"])


def tab_counterpart_types(m: pd.DataFrame, nums: dict) -> None:
    mt = m[m.crossmatch == "matched"]
    ned = mt.ned_type.replace("", np.nan).dropna().value_counts()
    sim = mt.simbad_otype.replace("", np.nan).dropna().value_counts()
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r l r}",
             r"NED type & $N$ & SIMBAD type & $N$ \\", r"\hline"]
    ned_t, sim_t = list(ned.items())[:8], list(sim.items())[:8]
    for i in range(max(len(ned_t), len(sim_t))):
        a = f"\\texttt{{{esc(ned_t[i][0])}}} & {ned_t[i][1]}" if i < len(ned_t) else " & "
        b = f"\\texttt{{{esc(sim_t[i][0])}}} & {sim_t[i][1]}" if i < len(sim_t) else " & "
        lines.append(f"{a} & {b} " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_counterpart_types.tex").write_text("\n".join(lines) + "\n")
    nums["n_matched"] = int((m.crossmatch == "matched").sum())
    nums["n_unmatched"] = int((m.crossmatch == "unmatched").sum())
    nums["n_ned_found"] = int(mt.ned_found.fillna(False).astype(bool).sum())
    nums["n_simbad_found"] = int(mt.simbad_found.fillna(False).astype(bool).sum())
    nums["n_both_services"] = int((mt.ned_found.fillna(False).astype(bool)
                                   & mt.simbad_found.fillna(False).astype(bool)).sum())
    nums["ned_types_top"] = {str(k): int(v) for k, v in ned_t}
    nums["simbad_types_top"] = {str(k): int(v) for k, v in sim_t}
    nums["n_ned_types_distinct"] = int(len(ned))
    nums["n_simbad_types_distinct"] = int(len(sim))


def tab_family_sky(nums: dict) -> None:
    fam = pd.read_csv(OUT / "family_evidence.csv")
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{r r r r r}",
             r"Family & $N$ & Dom.\ share & R.A.\ span & Dec.\ span \\",
             r"\hline"]
    for _, r in fam.iterrows():
        lines.append(f"{int(r.family_id)} & {int(r.n_objects)} & "
                     f"{100*r.f_dominant_surveyprog:.1f}\\% & "
                     f"{r.ra_span_deg:.1f}$^\\circ$ & {r.dec_span_deg:.1f}$^\\circ$ " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_family_sky.tex").write_text("\n".join(lines) + "\n")
    w = (fam.f_dominant_surveyprog * fam.n_objects).sum() / fam.n_objects.sum()
    nums["family_dominant_share_weighted"] = float(w)
    nums["family_min_ra_span_deg"] = float(fam.ra_span_deg.min())
    nums["family_n"] = int(len(fam))
    nums["family_n_clusters"] = int(fam.n_clusters.sum())


def tab_recovery_benchmark(nums: dict) -> None:
    b = json.loads(BENCH.read_text())
    parent_science = nums["parent_science_unique_targetids"]
    parent_all = b["catalogs"][0]["parent_total"]
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{l r r l r}",
             r"Reference class & $N_{\rm ref}$ & $N_{\rm match}$ & "
             r"Recovery (95\% CI) & Enrichment \\", r"\hline"]
    for r in b["results"]:
        # escape first, then insert math: esc() would otherwise escape the $
        name = esc(r["class_name"]).replace("Lyman-alpha", r"Lyman-$\alpha$")
        ci = (f"{100*r['recovery']:.3f}\\% "
              f"[{100*r['recovery_ci_95_lo']:.3f}, {100*r['recovery_ci_95_hi']:.3f}]")
        # Enrichment vs. the science-target parent (21,793,550), not the
        # all-TARGETID parent (27,547,223) -- Sec. II A's own declared
        # denominator convention. R1 truth-audit MAJOR-7 (Claude/Grok
        # convergent): the raw benchmark JSON's `enrichment` field uses the
        # all-TARGETID denominator and must not be printed here uncorrected.
        enrichment_science = r["enrichment"] * parent_science / parent_all
        lines.append(f"{name} & {texnum(r['n_reference_in_footprint'])} & "
                     f"{r['n_matched']} & {ci} & {enrichment_science:.1f}$\\times$ " + r"\\")
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_recovery_benchmark.tex").write_text("\n".join(lines) + "\n")
    nums["benchmark"] = {
        "base_rate": float(b["results"][0]["base_rate"]),
        "radius_arcsec": float(b["parameters"]["radius_arcsec"]),
        "n_classes_total": int(b["reference_manifest_summary"]["n_classes"]),
        "n_classes_fetched": int(b["reference_manifest_summary"]["n_fetched"]),
        "n_classes_unavailable": int(b["reference_manifest_summary"]["n_unavailable"]),
        "n_classes_no_id": int(b["reference_manifest_summary"]["n_no_catalog_id_known"]),
        "n_classes_timeout": int(b["reference_manifest_summary"]["n_timeout"]),
        "parent_total": int(b["catalogs"][0]["parent_total"]),
        "closed_loop_candidates": len(b["closed_loop_candidates"]),
        # The released benchmark's base rate divides by ALL unique TARGETIDs.
        # The reference classes are science targets, so the science-target
        # denominator is the fairer one: it raises the base rate by
        # 27,547,223 / 21,793,550 and therefore LOWERS every enrichment by the
        # inverse of that ratio. Reported so the released number can be read
        # either way; the pre-declared 10x bar is missed under both.
        "enrichment_science_denominator": {
            r["class_id"]: r["enrichment"] * nums["parent_science_unique_targetids"]
            / b["catalogs"][0]["parent_total"]
            for r in b["results"]},
        "base_rate_science_denominator":
            nums["n_released"] / nums["parent_science_unique_targetids"],
        "citations": {r["class_id"]: r["citation"] for r in b["results"]},
    }


def tab_ft_a(m: pd.DataFrame, fu: pd.DataFrame, nums: dict) -> None:
    """The four FT-A candidates with the Legacy Survey fluxes that settle them."""
    fta = fu[fu.tier == "FT-A"].merge(
        m[["targetid", "flux_g", "flux_r", "flux_z", "flux_w1", "morphtype",
           "coadd_exptime", "deltachi2", "family_id"]],
        on="targetid", how="left", suffixes=("", "_m"))
    lines = [r"\begin{ruledtabular}", r"\begin{tabular}{r r r r r r r}",
             r"\TARGETID & $z$ & $S$ & $\Delta\chi^2$ & $f_g$ & $f_r$ & $f_z$ \\",
             r"\hline"]
    recs = []
    for _, r in fta.sort_values("z", ascending=False).iterrows():
        lines.append(f"{int(r.targetid)} & {r.z:.4f} & {r.anomaly_score:.3f} & "
                     f"{r.deltachi2:.1f} & {r.flux_g:.3f} & {r.flux_r:.3f} & "
                     f"{r.flux_z:.3f} " + r"\\")
        recs.append({"targetid": int(r.targetid), "z": float(r.z),
                     "S": float(r.anomaly_score), "deltachi2": float(r.deltachi2),
                     "flux_g": float(r.flux_g), "flux_r": float(r.flux_r),
                     "flux_z": float(r.flux_z), "flux_w1": float(r.flux_w1),
                     "morphtype": str(r.morphtype),
                     "coadd_exptime": float(r.coadd_exptime),
                     "family_id": int(r.family_id)})
    lines += [r"\end{tabular}", r"\end{ruledtabular}"]
    (DTAB / "tab_ft_a.tex").write_text("\n".join(lines) + "\n")

    # Lyman-break consistency of each FT-A candidate against the released
    # Legacy Survey fluxes. The released schema carries no FLUX_IVAR, so a
    # per-object detection significance cannot be formed; the sample-wide
    # flux_g distribution is used as the only available yardstick.
    gmed, gp99 = float(m.flux_g.median()), float(m.flux_g.quantile(0.99))
    for r in recs:
        lya = 1215.67 * (1.0 + r["z"])
        r["lya_observed_angstrom"] = lya
        r["g_band_fully_blueward_of_break"] = bool(lya > 5500.0)   # DECam g: ~3900-5500 A
        r["r_band_fully_blueward_of_break"] = bool(lya > 7000.0)   # DECam r: ~5500-7000 A
        r["flux_g_over_flux_r"] = (r["flux_g"] / r["flux_r"]) if r["flux_r"] else None
        r["flux_g_percentile_in_sample"] = float((m.flux_g < r["flux_g"]).mean())
        r["flux_g_vs_sample_median"] = r["flux_g"] / gmed if gmed else None
    nums["ft_a"] = recs
    nums["ft_a_dropout_note"] = (
        "flux_g sample median %.3f nmgy, 99th percentile %.3f nmgy; the released "
        "schema carries no FLUX_IVAR, so no per-object detection significance is "
        "available" % (gmed, gp99))


# ------------------------------------------------------------------------ main
def main() -> None:
    d = afe.load()
    m = afe.build_master(d)
    fu = pd.DataFrame(json.loads((OUT / "followup_targets.json").read_text())["targets"])
    nums: dict = {}

    calib = json.loads(CALIB.read_text())
    nums["calibration"] = {
        "mse_mean": calib["mse_mean"], "mse_std": calib["mse_std"],
        "n_fit": calib["n_fit"], "n_validation": calib["n_validation"],
        "n_groups_selected": calib["n_groups_selected"],
        "sampling_design": calib["sampling_design"],
        "score_definition": calib["score_definition"],
        "stability_bound": calib["stability_check"]["bound"],
        "stability_observed": calib["stability_check"]["observed_deviation"],
        "stability_passed": calib["stability_check"]["passed"],
        "validation_mse_mean": calib["validation_mse_mean"],
    }

    sci = json.loads(json.loads(
        (afe.PHASE3 / "science_target_summary.json").read_text())["raw_describe_output"])
    nums["parent_science_unique_targetids"] = int(sci["science_only"]["unique_targetids"])
    nums["parent_all_quantiles"] = sci["quantiles"]
    nums["parent_science_quantiles"] = sci["science_only"]["quantiles"]
    nums["n_released"] = int(len(m))
    nums["released_fraction_of_science_parent"] = (
        len(m) / sci["science_only"]["unique_targetids"])
    nums["released_fraction_of_all_unique"] = len(m) / int(sci["unique_targetids"])
    nums["n_duplicate_rows_removed"] = int(sci["raw_rows"]) - int(sci["unique_targetids"])

    nums["n_wise_matched"] = int(m.match_flag.fillna(0).astype(float).sum()) \
        if "match_flag" in m.columns else None
    nums["wise_w1w2_median_matched"] = float(m.w1_w2.dropna().median())
    nums["n_point_source"] = int(m.is_point_source.fillna(False).astype(bool).sum())
    nums["morphtype_counts"] = {(k if k else "(empty)"): int(v)
                                for k, v in m.morphtype.value_counts(dropna=False).items()}
    # Gaia columns are zero-filled, not null-filled, for non-detections.
    nums["n_gaia_counterpart"] = int((m.gaia_phot_g_mean_mag > 0).sum())
    nums["n_gaia_counterpart_unmatched"] = int(
        (m.loc[m.crossmatch == "unmatched", "gaia_phot_g_mean_mag"] > 0).sum())
    nums["n_parallax_nonzero"] = int((m.parallax.abs() > 0).sum())
    nums["has_flux_ivar_columns"] = bool([c for c in m.columns if "ivar" in c.lower()])
    nums["flux_g_median_all"] = float(m.flux_g.median())
    nums["flux_g_p99_all"] = float(m.flux_g.quantile(0.99))
    nums["exptime_median_s"] = float(m.coadd_exptime.median())
    nums["snr_median"] = float(m.snr_med.median())

    fig_sky_fraction(d)
    fig_score_distribution(m, d, nums)
    fig_sky_distribution(m, fu)
    fig_band_residuals(m, nums)
    fig_redshift_distribution(m, nums)
    fig_latent_silhouette(m, nums)

    tab_provenance_chain(d, nums)
    tab_catalogue_schema(m, nums)
    tab_sky_fraction(d, nums)
    tab_counterpart_types(m, nums)
    tab_family_sky(nums)
    tab_recovery_benchmark(nums)
    tab_ft_a(m, fu, nums)
    fig_fta_photometry(m, nums)

    afe.jdump(nums, OUT / "draft_numbers.json")
    print(json.dumps(nums, indent=2, default=str)[:4000])
    print("\nfigures ->", sorted(p.name for p in DFIG.glob("*.pdf")))
    print("tables  ->", sorted(p.name for p in DTAB.glob("*.tex")))


if __name__ == "__main__":
    main()
