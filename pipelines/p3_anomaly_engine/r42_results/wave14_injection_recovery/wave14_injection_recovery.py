"""
R42 Wave 14 P3-CM-B4 — BigAE injection-recovery on production checkpoints.

Closes Wave 11 P3-CM-B4 BLOCKER ("validation-vs-product mismatch — fresh-IF
injection-recovery used as sensitivity calibrator while catalogs are built
from BigAE rankings"). Runs the same controlled-injection test directly on
the 5 production BigAE seeds (seed101…seed505) trained on the 47k DESI
proxy and used to score the 100k OOD set.

For each of 8 SNR levels (σ ∈ {1, 2, 3, 5, 8, 10, 15, 20}) and 5 anomaly
types (broad emission spike, gaussian noise burst, narrow line, polynomial
bump, spectral break), inject the perturbation into 200 random clean
spectra (lowest-baseline-MSE), score with all 5 BigAE seeds, then compute:

  - Threshold T = p99 of clean ensemble-mean MSE
  - Recall = fraction of injected with ensemble-mean MSE > T
  - Precision = TP / (TP + FP) on the (clean + injected) mix
  - F1 = 2 PR / (P + R)

Output: /workspace/r42_phase2/wave14_injection_recovery_results.json
        /workspace/r42_phase2/wave14_injection_recovery.png
"""
import os, sys, time, json, gc
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path("/workspace/r42_phase2")
DEV = torch.device("cuda")
SEEDS = [101, 202, 303, 404, 505]
SNR_LEVELS = [1, 2, 3, 5, 8, 10, 15, 20]
INJECTIONS = ["broad_emission_spike", "gaussian_noise_burst",
              "narrow_line", "polynomial_bump", "spectral_break"]
N_INJ_PER_TYPE = 200
RNG = np.random.default_rng(20260501)


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(OUT/"wave14_injection_recovery.log", "a") as f:
        f.write(line + "\n")


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
        Xt = torch.from_numpy(X).to(DEV)
        for i in range(0, len(Xt), bs):
            xb = Xt[i:i+bs]
            rb = m(xb)
            out[i:i+bs] = ((rb - xb)**2).mean(dim=1).cpu().numpy()
    return out


def ensemble_score(X):
    mses = np.stack([score(load_seed(s), X) for s in SEEDS])
    return mses.mean(axis=0), mses.std(axis=0)


_models = {}
def load_seed(s):
    if s not in _models:
        m = BigAE().to(DEV)
        m.load_state_dict(torch.load(OUT/f"bigae_seed{s}.pt", map_location=DEV))
        _models[s] = m
    return _models[s]


def inject(spec, kind, snr):
    """Inject anomaly of given type at given SNR into a single spectrum.
    spec is (496,) float32; SNR is in units of spec.std()."""
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
        spec += A * np.exp(-((x - c) ** 2) / 4.0)  # ~2 px FWHM
    elif kind == "polynomial_bump":
        c = RNG.integers(80, n - 80)
        w = RNG.integers(40, 80)
        x = np.arange(n)
        spec += A * np.maximum(0.0, 1.0 - ((x - c) / w) ** 2)
    elif kind == "spectral_break":
        c = RNG.integers(100, n - 100)
        spec[c:] += A
    return spec


def main():
    t0 = time.time()
    log("=== R42 Wave 14 P3-CM-B4: BigAE injection-recovery on production checkpoints ===")
    log(f"loading 100k OOD spectra")
    spectra = np.load("/workspace/r42_b10/B10_ood_spectra_100k.npy").astype(np.float32)
    finite = np.isfinite(spectra).all(axis=1)
    spectra = spectra[finite]
    log(f"  finite spectra: {len(spectra):,}")
    log(f"loading 5 production BigAE seeds")
    for s in SEEDS:
        load_seed(s)
    log(f"  loaded {len(SEEDS)} BigAE seeds (496->128, 5 ensemble)")
    log(f"computing baseline ensemble-mean MSE on all {len(spectra):,} clean spectra")
    base_mean, base_std = ensemble_score(spectra)
    log(f"  baseline median MSE = {np.median(base_mean):.4f}, p99 = {np.percentile(base_mean, 99):.4f}")
    cleanest_idx = np.argsort(base_mean)[:5000]
    cleanest = spectra[cleanest_idx]
    log(f"  using lowest-MSE 5,000 spectra as clean injection substrate (median MSE = {np.median(base_mean[cleanest_idx]):.4f})")
    held_out_idx = np.argsort(base_mean)[5000:30000]
    holdout = spectra[held_out_idx]
    holdout_mean, _ = base_mean[held_out_idx], base_std[held_out_idx]
    T = np.percentile(holdout_mean, 99)
    log(f"  detection threshold T (p99 of holdout clean ensemble MSE) = {T:.4f}")

    results = {
        "metadata": {
            "wave": "14",
            "blocker": "P3-CM-B4",
            "method": "BigAE production-checkpoint ensemble injection-recovery",
            "n_clean_substrate": int(len(cleanest)),
            "n_holdout_clean": int(len(holdout)),
            "n_inj_per_type": N_INJ_PER_TYPE,
            "n_seeds": len(SEEDS),
            "seeds": SEEDS,
            "injection_types": INJECTIONS,
            "snr_levels": SNR_LEVELS,
            "rng_seed": 20260501,
            "threshold_T_p99_holdout": float(T),
            "baseline_median_mse": float(np.median(base_mean)),
            "baseline_p99_mse": float(np.percentile(base_mean, 99)),
        },
        "by_snr": {},
    }

    for snr in SNR_LEVELS:
        log(f"--- SNR = {snr} ---")
        snr_results = {}
        for kind in INJECTIONS:
            sample_idx = RNG.choice(len(cleanest), N_INJ_PER_TYPE, replace=False)
            injected = np.stack([inject(cleanest[i], kind, snr) for i in sample_idx])
            inj_mean, inj_std = ensemble_score(injected)
            tp = int((inj_mean > T).sum())
            fn = N_INJ_PER_TYPE - tp
            fp_clean_pool_size = len(holdout)
            fp = int((holdout_mean > T).sum())
            tn = fp_clean_pool_size - fp
            recall = tp / N_INJ_PER_TYPE
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
            snr_results[kind] = {
                "n_inj": N_INJ_PER_TYPE,
                "tp": tp, "fp": fp, "fn": fn, "tn": tn,
                "recall": float(recall),
                "precision": float(precision),
                "f1": float(f1),
                "injected_mean_mse_median": float(np.median(inj_mean)),
                "injected_mean_mse_p10": float(np.percentile(inj_mean, 10)),
                "ensemble_disagreement_median": float(np.median(inj_std)),
            }
            log(f"  {kind:24s} R={recall:.3f} P={precision:.3f} F1={f1:.3f} med_MSE={np.median(inj_mean):.3f}")
        results["by_snr"][str(snr)] = snr_results

    out_json = OUT/"wave14_injection_recovery_results.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    log(f"results -> {out_json}")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    snr_arr = np.array(SNR_LEVELS, dtype=float)
    for kind in INJECTIONS:
        recalls = [results["by_snr"][str(s)][kind]["recall"] for s in SNR_LEVELS]
        f1s = [results["by_snr"][str(s)][kind]["f1"] for s in SNR_LEVELS]
        axes[0].plot(snr_arr, recalls, "o-", label=kind, linewidth=1.6)
        axes[1].plot(snr_arr, f1s, "o-", label=kind, linewidth=1.6)
    for ax in axes:
        ax.set_xscale("log")
        ax.set_xlabel(r"Injection SNR (units of $\sigma_{\rm spec}$)")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="best", fontsize=8, frameon=False)
    axes[0].set_ylabel("Recall (TP / N_inj)")
    axes[0].set_title("BigAE production-ensemble injection-recovery — recall")
    axes[1].set_ylabel("F1 score")
    axes[1].set_title("BigAE production-ensemble injection-recovery — F1")
    fig.tight_layout()
    out_png = OUT/"wave14_injection_recovery.png"
    fig.savefig(out_png, dpi=140)
    log(f"figure -> {out_png}")
    log(f"=== Wave 14 P3-CM-B4 DONE in {(time.time()-t0)/60:.1f} min ===")


if __name__ == "__main__":
    main()
