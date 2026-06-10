#!/usr/bin/env python3
"""P3 R24conf compute-queue closures #34, #35, #36, #41
(queue: project-context/peer-reviews/R24CONF_COMPUTE_QUEUE.md).

  #34 OpenAI-E3 — INDEPENDENT 6-way dedup (DESI + SDSS + eROSITA + Planck +
      Gaia + NEOWISE; no LAMOST, no ACT) at the canonical 5" link radius,
      same survey parquets + UnionFind machinery as
      pathc_dedup/r23conf_dedup_audits.py, verifying the catalog-grade
      counts 264,938 (with the 200 Planck map patches) / 264,738
      (point-source only) currently attributed by headline-minus-LAMOST.

  #35 META-M1 + META-m2 — document the 38,330-pixel HEALPix selection
      (occupied Nside=64 pixels of the deduplicated catalog; subset of
      49,152) and the chi^2 expectation model (uniform mean over occupied
      pixels, Poisson variance), and rerun the uniformity test under that
      stated model.

  #36 META-M3 — document the Planck 64x64 SMICA patch preprocessing from the
      committed pipeline (cmb_native_retrain.py) and run the DC/gradient
      robustness check on the top-200 ranking: rescore all 200,000 patches
      with the production autoencoder under (a) unmodified, (b) re-demeaned,
      (c) best-fit-plane-removed patches; report score reproduction vs the
      stored all-scores parquet, top-200 set overlap, and Spearman rho.

  #41 OpenAI-E10 residue — SDSS native-retrain convergence epoch recovered
      from the backed-up pod training logs
      (data/runpod_backups/ktds4mkmzb7ven_20260427/outputs/sdss_native/).

Output: pipelines/p3_anomaly_engine/r24conf_pod_session_batch.json
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
P3 = REPO / "pipelines/p3_anomaly_engine"
BACKUP = REPO / "data/runpod_backups/ktds4mkmzb7ven_20260427"
OUT = P3 / "r24conf_pod_session_batch.json"
T0 = time.time()

# canonical survey parquets (verbatim from pathc_dedup/r23conf_dedup_audits.py,
# LAMOST row removed for the 6-way catalog-grade configuration)
SURVEYS_6WAY = [
    ("desi_dr1", "pipelines/p1_highz_tracers/outputs/step2_crossmatch/anomaly_crossmatch.parquet"),
    ("erosita_dr1", "pipelines/p3_anomaly_engine/hf_staging_pod/erosita_dr1_anomalies.parquet"),
    ("planck_cmb", "pipelines/p3_anomaly_engine/hf_staging/planck_cmb_anomalies.parquet"),
    ("gaia_dr3", "pipelines/p3_anomaly_engine/hf_staging/gaia_dr3_anomalies.parquet"),
    ("neowise_pathc", "pipelines/p3_anomaly_engine/pathc_neowise_ecliptic/neowise_pathc_masked_anomalies.parquet"),
    ("sdss_dr18", "pipelines/p3_anomaly_engine/hf_staging/sdss_dr18_pathc_native.parquet"),
]
RADIUS = 5.0
NSIDE = 64


def log(m):
    print(f"[{time.time()-T0:.1f}s] {m}", flush=True)


class UnionFind:
    def __init__(self, n):
        self.p = np.arange(n)
        self.r = np.zeros(n, dtype=np.int32)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.r[rx] < self.r[ry]:
            rx, ry = ry, rx
        self.p[ry] = rx
        if self.r[rx] == self.r[ry]:
            self.r[rx] += 1


def main() -> int:
    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "pipelines/p3_anomaly_engine/r24conf_pod_session_batch.py",
    }

    # ---------------- #34: independent 6-way dedup ---------------------------
    log("#34: 6-way dedup")
    from astropy.coordinates import SkyCoord, search_around_sky
    import astropy.units as u
    parts = []
    per_survey = {}
    for name, path in SURVEYS_6WAY:
        df = pd.read_parquet(REPO / path)
        p = pd.DataFrame({"survey": name,
                          "ra": df["ra"].astype("float64").values,
                          "dec": df["dec"].astype("float64").values})
        p = p[np.isfinite(p["ra"]) & np.isfinite(p["dec"])].reset_index(drop=True)
        per_survey[name] = int(len(p))
        parts.append(p)
    cat = pd.concat(parts, ignore_index=True)
    sc = SkyCoord(ra=cat["ra"].values * u.deg, dec=cat["dec"].values * u.deg,
                  frame="icrs")
    i1, i2, _, _ = search_around_sky(sc, sc, RADIUS * u.arcsec)
    m = i1 < i2
    uf = UnionFind(len(cat))
    for a, b in zip(i1[m], i2[m]):
        uf.union(a, b)
    labels = np.array([uf.find(i) for i in range(len(cat))])
    n_unique_6way = int(len(np.unique(labels)))
    # point-source tier: drop clusters whose members are ALL planck_cmb patches
    cat["cid"] = labels
    is_planck = (cat["survey"] == "planck_cmb").to_numpy()
    cl_all_planck = pd.Series(is_planck).groupby(labels).all()
    n_planck_only_clusters = int(cl_all_planck.sum())
    out["item34_sixway_dedup"] = {
        "surveys": [s for s, _ in SURVEYS_6WAY],
        "radius_arcsec": RADIUS,
        "per_survey_detections": per_survey,
        "n_input_detections": int(len(cat)),
        "n_unique_6way": n_unique_6way,
        "n_planck_patch_only_clusters": n_planck_only_clusters,
        "n_unique_point_source": n_unique_6way - n_planck_only_clusters,
        "published_claims": {"catalog_grade_with_patches": 264938,
                             "catalog_grade_point_source": 264738},
        "matches_published": {
            "with_patches": bool(n_unique_6way == 264938),
            "point_source": bool((n_unique_6way - n_planck_only_clusters) == 264738),
        },
    }
    log(f"  6-way unique = {n_unique_6way:,} "
        f"(point-source {n_unique_6way - n_planck_only_clusters:,})")
    OUT.write_text(json.dumps(out, indent=1))

    # ---------------- #35: HEALPix 38,330-pixel selection + chi^2 ------------
    log("#35: HEALPix occupied-pixel uniformity rerun")
    import healpy as hp
    res35 = {}
    for tag, pqf in [("8way_incl_act", P3 / "pathc_dedup/unique_objects.parquet"),
                     ("7way_headline", P3 / "pathc_dedup/unique_objects_no_act.parquet")]:
        u_ = pd.read_parquet(pqf, columns=["ra_mean", "dec_mean"])
        pix = hp.ang2pix(NSIDE, u_["ra_mean"].to_numpy(),
                         u_["dec_mean"].to_numpy(), lonlat=True)
        counts = np.bincount(pix, minlength=hp.nside2npix(NSIDE))
        occ = counts[counts > 0]
        nbar = occ.mean()
        chi2 = float(((occ - nbar) ** 2 / nbar).sum())
        res35[tag] = {
            "n_objects": int(len(u_)),
            "n_occupied_pixels": int(len(occ)),
            "n_total_pixels": int(hp.nside2npix(NSIDE)),
            "expectation_model": "uniform mean over OCCUPIED pixels; "
                                 "Poisson variance (chi^2 = sum (n-nbar)^2/nbar)",
            "nbar_per_occupied_pixel": float(nbar),
            "chi2": chi2,
            "dof": int(len(occ) - 1),
            "chi2_reduced": float(chi2 / (len(occ) - 1)),
        }
        log(f"  {tag}: occ={len(occ):,} chi2={chi2:,.0f} "
            f"chi2_nu={chi2/(len(occ)-1):.2f}")
    res35["published_claims"] = {"n_pixels": 38330, "chi2": 143936,
                                 "dof": 38329, "chi2_reduced": 3.76}
    out["item35_healpix_uniformity"] = res35
    OUT.write_text(json.dumps(out, indent=1))

    # ---------------- #41: SDSS native-retrain convergence epoch -------------
    log("#41: SDSS convergence epoch from backed-up logs")
    tl = json.load(open(BACKUP / "outputs/sdss_native/training_log.json"))
    out["item41_sdss_convergence_epoch"] = {
        "source": "data/runpod_backups/ktds4mkmzb7ven_20260427/outputs/"
                  "sdss_native/training_log.json (+ logs/sdss_native_retrain.log)",
        "best_epoch": tl["best_epoch"],
        "best_val_loss": tl["best_val_loss"],
        "early_stop_epoch": 17,
        "max_epochs": tl["config"].get("max_epochs"),
        "patience": tl["config"].get("patience"),
        "n_train": tl["n_train"], "n_val": tl["n_val"],
        "passes_gate_0p30": tl["passes_gate_0p30"],
    }
    OUT.write_text(json.dumps(out, indent=1))

    # ---------------- #36: SMICA preprocessing doc + DC/gradient check -------
    log("#36: CMB patch preprocessing doc + robustness rescore")
    import torch
    import torch.nn as nn

    class CMBAutoencoder(nn.Module):  # verbatim from cmb_native_retrain.py
        def __init__(self, latent=128):
            super().__init__()
            self.encoder_conv = nn.Sequential(
                nn.Conv2d(1, 16, 3, 2, 1), nn.BatchNorm2d(16), nn.ReLU(True),
                nn.Conv2d(16, 32, 3, 2, 1), nn.BatchNorm2d(32), nn.ReLU(True),
                nn.Conv2d(32, 64, 3, 2, 1), nn.BatchNorm2d(64), nn.ReLU(True),
            )
            self.encoder_fc = nn.Sequential(nn.Flatten(), nn.Linear(64 * 8 * 8, latent))
            self.decoder_fc = nn.Sequential(nn.Linear(latent, 64 * 8 * 8), nn.ReLU(True))
            self.decoder_conv = nn.Sequential(
                nn.ConvTranspose2d(64, 32, 3, 2, 1, 1), nn.BatchNorm2d(32), nn.ReLU(True),
                nn.ConvTranspose2d(32, 16, 3, 2, 1, 1), nn.BatchNorm2d(16), nn.ReLU(True),
                nn.ConvTranspose2d(16, 1, 3, 2, 1, 1), nn.Tanh(),
            )

        def forward(self, x):
            z = self.encoder_fc(self.encoder_conv(x))
            h = self.decoder_fc(z).view(-1, 64, 8, 8)
            return self.decoder_conv(h), z

    dev = "cpu"
    model = CMBAutoencoder()
    sd = torch.load(BACKUP / "outputs/cmb_native/best_cmb_native.pt",
                    map_location=dev)
    if isinstance(sd, dict) and "model" in sd:
        sd = sd["model"]
    elif isinstance(sd, dict) and "state_dict" in sd:
        sd = sd["state_dict"]
    model.load_state_dict(sd)
    model.eval()

    patches = np.load(BACKUP / "outputs/cmb_native/cmb_native_patches.npy",
                      mmap_mode="r")
    scores_ref = pd.read_parquet(
        BACKUP / "outputs/cmb_native/cmb_native_all_scores.parquet")
    ref = scores_ref.sort_values("idx")["anomaly_score"].to_numpy()
    n = len(patches)

    # best-fit plane basis (gradient removal)
    yy, xx = np.mgrid[0:64, 0:64].astype(np.float64)
    gx = (xx - xx.mean()) / xx.std()
    gy = (yy - yy.mean()) / yy.std()
    norm_gx = (gx ** 2).sum()
    norm_gy = (gy ** 2).sum()

    def rescore(transform, label):
        s = np.zeros(n, dtype=np.float64)
        bs = 2048
        with torch.no_grad():
            for i0 in range(0, n, bs):
                b = np.array(patches[i0:i0 + bs], dtype=np.float32)
                if transform == "demean":
                    b = b - b.mean(axis=(1, 2), keepdims=True)
                elif transform == "deplane":
                    b = b - b.mean(axis=(1, 2), keepdims=True)
                    cx = (b * gx[None]).sum(axis=(1, 2)) / norm_gx
                    cy = (b * gy[None]).sum(axis=(1, 2)) / norm_gy
                    b = b - cx[:, None, None] * gx[None] \
                          - cy[:, None, None] * gy[None]
                    b = b.astype(np.float32)
                t = torch.from_numpy(b).unsqueeze(1)
                rec, _ = model(t)
                s[i0:i0 + bs] = ((rec.squeeze(1).numpy() - b) ** 2).mean(axis=(1, 2))
                if (i0 // bs) % 20 == 0:
                    log(f"  rescore[{label}] {i0:,}/{n:,}")
        return s

    from scipy.stats import spearmanr
    s_plain = rescore(None, "plain")
    repro_max_abs = float(np.max(np.abs(s_plain - ref)))
    repro_rho = float(spearmanr(s_plain, ref).statistic)
    top200_ref = set(np.argsort(ref)[-200:])
    top200_plain = set(np.argsort(s_plain)[-200:])

    s_dm = rescore("demean", "demean")
    s_dp = rescore("deplane", "deplane")

    def cmp(s, name):
        top = set(np.argsort(s)[-200:])
        return {"variant": name,
                "top200_overlap_with_stored": int(len(top & top200_ref)),
                "spearman_rho_vs_stored": float(spearmanr(s, ref).statistic)}

    out["item36_cmb_patch_preprocessing"] = {
        "preprocessing_documented_from": "pipelines/p3_anomaly_engine/cmb_native_retrain.py",
        "preprocessing": {
            "map": "Planck SMICA_2048 R3.00 full-mission temperature "
                   "(COM_CMB_IQU-smica_2048_R3.00_full.fits, K_CMB)",
            "patching": "healpy gnomview 10x10 deg, 64x64 px "
                        "(9.375 arcmin/px), centers at |b|>=20 deg",
            "units_normalization": "per-patch standardization: subtract patch "
                                   "mean, divide by patch std (so the DC mode "
                                   "is removed by construction), NaN->0, "
                                   "clip to +/-10",
            "apodization": "NONE (no taper/window applied to patches)",
            "mean_removal": "per-patch (above); map-level monopole+dipole "
                            "removed in the released SMICA product",
        },
        "score_reproduction": {
            "max_abs_score_diff_vs_stored": repro_max_abs,
            "spearman_rho_vs_stored": repro_rho,
            "top200_overlap_plain": int(len(top200_plain & top200_ref)),
        },
        "robustness": [cmp(s_dm, "re-demeaned (DC)"),
                       cmp(s_dp, "best-fit plane removed (gradient)")],
        "n_patches": int(n),
    }
    OUT.write_text(json.dumps(out, indent=1))
    log("DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
