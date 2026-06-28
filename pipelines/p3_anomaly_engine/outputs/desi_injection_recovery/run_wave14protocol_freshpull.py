"""
Independent reproduction of R42 Wave 14 P3-CM-B4 BigAE injection-recovery,
EXACT wave14 protocol, on a FRESH 20K SPARCL re-pull (2026-06-28).

Reference: pipelines/p3_anomaly_engine/r42_results/wave14_injection_recovery/
           wave14_injection_recovery.py  (protocol copied verbatim below).

Differences from reference: data source is the fresh re-pull
clean_spectra_20000.npy (already 496-dim), device is MPS/CPU (no CUDA on Mac).
Threshold = p99 of clean HOLDOUT ensemble-mean MSE (NOT full-set p99, NO clip).
Everything else identical: 5 production BigAE seeds, ensemble-mean MSE,
cleanest-5000 substrate, next-ranked holdout, 5 injection types implemented
exactly as wave14, A = snr*spec.std(), n_inj=200/type, rng_seed=20260501,
SNR levels [1,2,3,5,8,10,15,20].
"""
import os, time, json, subprocess
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SEED_DIR = REPO / "pipelines/p3_anomaly_engine/r42_phase2"
DATA = HERE / "clean_spectra_20000.npy"
OUT_JSON = HERE / "desi_injrec_wave14protocol.json"
OUT_PNG = HERE / "desi_injrec_wave14protocol.png"

DEV = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
SEEDS = [101, 202, 303, 404, 505]
SNR_LEVELS = [1, 2, 3, 5, 8, 10, 15, 20]
INJECTIONS = ["broad_emission_spike", "gaussian_noise_burst",
              "narrow_line", "polynomial_bump", "spectral_break"]
N_INJ_PER_TYPE = 200
RNG = np.random.default_rng(20260501)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


class BigAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(496, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 128))
        self.dec = nn.Sequential(
            nn.Linear(128, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(512, 496))

    def forward(self, x):
        return self.dec(self.enc(x))


def score(m, X, bs=4096):
    m.eval()
    out = np.empty(len(X), dtype=np.float32)
    with torch.no_grad():
        Xt = torch.from_numpy(np.ascontiguousarray(X)).to(DEV)
        for i in range(0, len(Xt), bs):
            xb = Xt[i:i+bs]
            rb = m(xb)
            out[i:i+bs] = ((rb - xb)**2).mean(dim=1).cpu().numpy()
    return out


_models = {}
def load_seed(s):
    if s not in _models:
        m = BigAE().to(DEV)
        m.load_state_dict(torch.load(SEED_DIR/f"bigae_seed{s}.pt", map_location=DEV))
        _models[s] = m
    return _models[s]


def ensemble_score(X):
    mses = np.stack([score(load_seed(s), X) for s in SEEDS])
    return mses.mean(axis=0), mses.std(axis=0)


def inject(spec, kind, snr):
    spec = spec.copy()
    n = len(spec)
    sigma = max(spec.std(), 1e-6)
    A = snr * sigma
    if kind == "broad_emission_spike":
        c = RNG.integers(50, n - 50)
        w = RNG.integers(15, 35)
        x = np.arange(n)
        spec += A * np.exp(-((x - c) ** 2) / (2 * w * w))
    elif kind == "gaussian_noise_burst":
        c = RNG.integers(50, n - 50)
        w = RNG.integers(20, 40)
        mask = (np.arange(n) >= c - w) & (np.arange(n) <= c + w)
        spec[mask] += A * RNG.standard_normal(mask.sum())
    elif kind == "narrow_line":
        c = RNG.integers(20, n - 20)
        x = np.arange(n)
        spec += A * np.exp(-((x - c) ** 2) / 4.0)
    elif kind == "polynomial_bump":
        c = RNG.integers(80, n - 80)
        w = RNG.integers(40, 80)
        x = np.arange(n)
        spec += A * np.maximum(0.0, 1.0 - ((x - c) / w) ** 2)
    elif kind == "spectral_break":
        c = RNG.integers(100, n - 100)
        spec[c:] += A
    return spec.astype(np.float32)


def main():
    t0 = time.time()
    log(f"device={DEV}")
    spectra = np.load(DATA).astype(np.float32)
    finite = np.isfinite(spectra).all(axis=1)
    spectra = spectra[finite]
    log(f"fresh spectra (finite): {len(spectra):,} x {spectra.shape[1]}")
    for s in SEEDS:
        load_seed(s)
    base_mean, base_std = ensemble_score(spectra)
    log(f"baseline median MSE = {np.median(base_mean):.4f}, full p99 = {np.percentile(base_mean,99):.4f}")
    order = np.argsort(base_mean)
    cleanest_idx = order[:5000]
    cleanest = spectra[cleanest_idx]
    # EXACT wave14 holdout band (literal [5000:30000]); on a 20k set this
    # collapses to [5000:20000] = all-but-cleanest-5000, INCLUDING the dirty tail.
    held_out_idx = order[5000:30000]
    holdout = spectra[held_out_idx]
    holdout_mean = base_mean[held_out_idx]
    T = float(np.percentile(holdout_mean, 99))
    # INTENT-aligned holdout: a genuinely clean middle band that excludes the
    # high-MSE tail (matches wave14's intent on its 100k set, where [5000:30000]
    # WAS the clean band). Used as a diagnostic threshold T_clean.
    clean_band_idx = order[5000:15000]
    clean_band_mean = base_mean[clean_band_idx]
    T_clean = float(np.percentile(clean_band_mean, 99))
    log(f"n_substrate={len(cleanest)} n_holdout={len(holdout)} "
        f"T_exact(p99 literal-holdout)={T:.6f} T_clean(p99 tail-excluded)={T_clean:.6f}")

    try:
        git_hash = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO).decode().strip()
    except Exception:
        git_hash = "unknown"

    results = {
        "metadata": {
            "reproduction_of": "R42 wave14 P3-CM-B4 injection-recovery",
            "protocol": "wave14 exact (cleanest-5000 substrate, p99-of-holdout threshold, no clip)",
            "provenance": "fresh 20K SPARCL re-pull 2026-06-28, wave14 protocol",
            "date": "2026-06-28",
            "git_hash": git_hash,
            "device": str(DEV),
            "n_substrate": int(len(cleanest)),
            "n_holdout": int(len(holdout)),
            "n_inj_per_type": N_INJ_PER_TYPE,
            "seeds": SEEDS,
            "injection_types": INJECTIONS,
            "snr_levels": SNR_LEVELS,
            "rng_seed": 20260501,
            "threshold_T_p99_holdout": T,
            "threshold_T_clean_tail_excluded": T_clean,
            "n_clean_band_tail_excluded": int(len(clean_band_idx)),
            "holdout_band_note": "literal wave14 [5000:30000] => [5000:20000] on 20k set; includes dirty tail, inflating T ~60x vs wave14",
            "baseline_median_mse": float(np.median(base_mean)),
            "baseline_p99_mse": float(np.percentile(base_mean, 99)),
        },
        "by_snr": {},
        "mean_recall_by_snr": {},
        "by_snr_tail_excluded_threshold": {},
        "mean_recall_by_snr_tail_excluded_threshold": {},
    }

    for snr in SNR_LEVELS:
        snr_results = {}
        snr_results_clean = {}
        recalls = []
        recalls_clean = []
        for kind in INJECTIONS:
            sample_idx = RNG.choice(len(cleanest), N_INJ_PER_TYPE, replace=False)
            injected = np.stack([inject(cleanest[i], kind, snr) for i in sample_idx])
            inj_mean, inj_std = ensemble_score(injected)
            tp = int((inj_mean > T).sum())
            fn = N_INJ_PER_TYPE - tp
            fp = int((holdout_mean > T).sum())
            tn = len(holdout) - fp
            recall = tp / N_INJ_PER_TYPE
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            f1 = 2*precision*recall/(precision+recall) if (precision+recall) > 0 else 0.0
            snr_results[kind] = {
                "n_inj": N_INJ_PER_TYPE, "tp": tp, "fp": fp, "fn": fn, "tn": tn,
                "recall": float(recall), "precision": float(precision), "f1": float(f1),
                "injected_mean_mse_median": float(np.median(inj_mean)),
            }
            recalls.append(recall)
            # same injected spectra, scored against tail-excluded clean threshold
            tp_c = int((inj_mean > T_clean).sum())
            recall_c = tp_c / N_INJ_PER_TYPE
            snr_results_clean[kind] = {"recall": float(recall_c), "tp": tp_c}
            recalls_clean.append(recall_c)
        mean_recall = float(np.mean(recalls))
        mean_recall_c = float(np.mean(recalls_clean))
        results["by_snr"][str(snr)] = snr_results
        results["mean_recall_by_snr"][str(snr)] = mean_recall
        results["by_snr_tail_excluded_threshold"][str(snr)] = snr_results_clean
        results["mean_recall_by_snr_tail_excluded_threshold"][str(snr)] = mean_recall_c
        log(f"SNR={snr:2d} mean_recall(exact)={mean_recall:.3f} "
            f"mean_recall(clean-T)={mean_recall_c:.3f} | " +
            " ".join(f"{k.split('_')[0]}={snr_results[k]['recall']:.2f}" for k in INJECTIONS))

    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    log(f"results -> {OUT_JSON}")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    snr_arr = np.array(SNR_LEVELS, dtype=float)
    mean_r = [results["mean_recall_by_snr"][str(s)] for s in SNR_LEVELS]
    mean_rc = [results["mean_recall_by_snr_tail_excluded_threshold"][str(s)] for s in SNR_LEVELS]
    axes[0].plot(snr_arr, mean_r, "ko-", linewidth=2.2, label=f"exact wave14 T={T:.2f}")
    axes[0].plot(snr_arr, mean_rc, "s--", color="tab:green", linewidth=2.0,
                 label=f"tail-excluded T={T_clean:.3f}")
    axes[0].axhline(0.5, ls=":", color="r", alpha=0.6, label="50% gate")
    axes[0].set_ylabel("Mean recall")
    axes[0].set_title("Fresh 20K re-pull, wave14 protocol — mean recall")
    axes[0].legend(loc="best", fontsize=9, frameon=False)
    for kind in INJECTIONS:
        rc = [results["by_snr"][str(s)][kind]["recall"] for s in SNR_LEVELS]
        axes[1].plot(snr_arr, rc, "o-", label=kind, linewidth=1.6)
    axes[1].set_ylabel("Recall — exact-protocol T")
    axes[1].set_title("Per-injection-type recall (exact T)")
    axes[1].legend(loc="best", fontsize=8, frameon=False)
    for ax in axes:
        ax.set_xscale("log")
        ax.set_xlabel(r"Injection SNR (units of $\sigma_{\rm spec}$)")
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.03, 1.03)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    log(f"figure -> {OUT_PNG}")
    log(f"=== DONE in {(time.time()-t0)/60:.1f} min ===")


if __name__ == "__main__":
    main()
