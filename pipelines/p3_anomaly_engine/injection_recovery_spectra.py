#!/usr/bin/env python3
"""
Spectral survey injection-recovery validation — P3-PATHC-INJECTION-RECOVERY-ALL-SURVEYS
=======================================================================================
For each BigAE-scored spectral survey (SDSS DR18, LAMOST DR10) this script

  1. loads one training shard + the native BigAE best.pt checkpoint,
  2. applies the same |x|>100 -> drop + clip(-10, 10) defensive filter used
     at train/score time (fire #80 lesson),
  3. splits the shard into clean validation,
  4. plants 500 synthetic gaussian emission-line features at 6 amplitude
     levels (0.5x, 1x, 2x, 5x, 10x, 20x of per-spectrum std), randomly
     placed in the 496-bin DESI grid with FWHM ~5 bins (matches typical
     emission-line resolution at R~1800),
  5. scores clean + planted through the BigAE,
  6. computes recovery fraction at the 99th-percentile MSE threshold on
     the clean set (standard injection-recovery gate),
  7. writes a per-survey + combined summary JSON.

Path-C exit criterion #6 expects >= 50 % recovery at the 5x-noise level
to pass.  Below that, the survey is flagged as having insufficient
variability-autoencoder sensitivity for Paper 3 inclusion.

Runs locally (no pod) on downloaded shards + models at
/tmp/pathc_validation/.  CMB equivalent is baked into
cmb_native_retrain.py and runs at training-gate time.  Native DESI / Gaia
/ eROSITA / NEOWISE validators are out of scope this fire (no local shards
for those three and NEOWISE uses a different feature set; filed as
follow-up fires).

Outputs:
  pipelines/p3_anomaly_engine/pathc_injection_recovery/
    injection_recovery_sdss_native.json
    injection_recovery_lamost_native.json
    injection_recovery_summary.json   <- combined headline table
"""
import json
import os
import numpy as np
import torch
import torch.nn as nn

ART_DIR = '/tmp/pathc_validation'
OUT_DIR = 'pipelines/p3_anomaly_engine/pathc_injection_recovery'
os.makedirs(OUT_DIR, exist_ok=True)

N_PLANT       = 500
AMP_LEVELS    = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]   # in units of per-spectrum std
GATE_AMP      = 5.0       # Path-C gate: recovery at this amplitude must be >= GATE_RECOV
GATE_RECOV    = 0.50
GATE_PCTL     = 99.0
LINE_FWHM_BIN = 5.0       # FWHM in 496-bin DESI units ~= R ~ 1800
CLIP_RANGE    = 10.0
MAX_ABS_TOL   = 100.0
N_LATENT      = 128
N_IN          = 496
SEED          = 42


class BigAE(nn.Module):
    """Same architecture as the native retrains."""
    def __init__(self, n_in=N_IN, n_lat=N_LATENT):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.10),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_lat),
        )
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.10),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in),
        )
    def forward(self, x):
        return self.dec(self.enc(x))


def defensive_filter(arr):
    """Apply fire-#80 filter + clip, matching train/score time exactly."""
    out = []
    n_drop = 0
    for v in arr:
        if not np.isfinite(v).all():
            n_drop += 1; continue
        if np.abs(v).max() > MAX_ABS_TOL:
            n_drop += 1; continue
        v2 = np.clip(v, -CLIP_RANGE, CLIP_RANGE)
        out.append(v2)
    return np.stack(out).astype(np.float32), n_drop


def score_mse(model, x, device, batch=1024):
    out = np.empty(len(x), dtype=np.float32)
    with torch.no_grad():
        for i in range(0, len(x), batch):
            xb = torch.from_numpy(x[i:i+batch]).to(device)
            recon = model(xb)
            m = ((xb - recon) ** 2).mean(dim=1).cpu().numpy()
            out[i:i+batch] = m
    return out


def plant_emission_lines(spectra, amp_sigma, rng):
    """Inject gaussian emission-line bumps (random center, random sign)."""
    planted = spectra.copy()
    n, nbin = spectra.shape
    sigma = LINE_FWHM_BIN / 2.3548
    bins = np.arange(nbin, dtype=np.float32)
    for k in range(n):
        center = rng.integers(40, nbin - 40)
        sign = rng.choice([-1.0, 1.0])
        # Amplitude in units of this spectrum's std; bounded by clip range
        per_std = spectra[k].std()
        peak = amp_sigma * per_std * sign
        bump = peak * np.exp(-0.5 * ((bins - center) / sigma) ** 2)
        planted[k] = spectra[k] + bump.astype(np.float32)
    # Apply the SAME clip the model saw at train/score time — an amplitude
    # above the clip range becomes effectively the clipped saturation value.
    np.clip(planted, -CLIP_RANGE, CLIP_RANGE, out=planted)
    return planted


def run_survey(name, shard_path, model_path, device):
    print(f'\n=== {name} ===', flush=True)
    shard = np.load(shard_path)
    print(f'  shard shape {shard.shape}, raw range [{shard.min():.3g}, {shard.max():.3g}]', flush=True)

    clean, n_drop = defensive_filter(shard)
    print(f'  defensive filter: kept {len(clean)}/{len(shard)} (dropped {n_drop})', flush=True)

    # Split: last 1500 held-out for plant set (fixed), first chunk for clean scoring
    rng = np.random.default_rng(SEED)
    perm = rng.permutation(len(clean))
    plant_idx = perm[:N_PLANT]
    clean_plant = clean[plant_idx]
    rest_clean = clean[perm[N_PLANT:]]

    model = BigAE().to(device)
    state = torch.load(model_path, map_location=device, weights_only=True)
    if isinstance(state, dict) and 'state_dict' in state:
        model.load_state_dict(state['state_dict'])
    else:
        model.load_state_dict(state)
    model.eval()

    # Score the unplanted validation pool -> gate threshold
    clean_scores = score_mse(model, rest_clean, device)
    thr = float(np.percentile(clean_scores, GATE_PCTL))
    print(f'  clean n={len(rest_clean)}  MSE p50={np.median(clean_scores):.4e}  '
          f'p99={thr:.4e}  max={clean_scores.max():.4e}', flush=True)

    levels = {}
    for amp in AMP_LEVELS:
        planted = plant_emission_lines(clean_plant, amp, rng)
        ps = score_mse(model, planted, device)
        rec = int((ps > thr).sum())
        frac = rec / N_PLANT
        levels[f'{amp}x'] = {
            'amp_sigma': amp,
            'planted_n': N_PLANT,
            'planted_mse_p50': float(np.median(ps)),
            'planted_mse_p10': float(np.percentile(ps, 10)),
            'recovered': rec,
            'recovery_fraction': float(frac),
        }
        print(f'  amp {amp:5.1f}x:  plant MSE p50={np.median(ps):.4e}  '
              f'recovered {rec:3d}/{N_PLANT} ({100*frac:5.1f}%)', flush=True)

    gate = levels[f'{GATE_AMP}x']['recovery_fraction']
    gate_pass = gate >= GATE_RECOV
    print(f'  GATE ({GATE_AMP}x >= {GATE_RECOV:.0%}): {"PASS" if gate_pass else "FAIL"} '
          f'(observed {100*gate:.1f}%)', flush=True)

    result = {
        'survey': name,
        'shard': os.path.basename(shard_path),
        'model': os.path.basename(model_path),
        'n_shard':  int(len(shard)),
        'n_clean':  int(len(clean)),
        'n_dropped_defensive': int(n_drop),
        'n_plant':  N_PLANT,
        'clip_range': CLIP_RANGE,
        'line_fwhm_bin': LINE_FWHM_BIN,
        'clean_mse_p50': float(np.median(clean_scores)),
        'clean_mse_p99': thr,
        'gate_amp_sigma': GATE_AMP,
        'gate_recovery_required': GATE_RECOV,
        'gate_recovery_observed': gate,
        'gate_pass': bool(gate_pass),
        'levels': levels,
    }
    out_path = os.path.join(OUT_DIR, f'injection_recovery_{name}.json')
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)
    print(f'  wrote {out_path}', flush=True)
    return result


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}', flush=True)

    surveys = [
        ('sdss_native',   f'{ART_DIR}/sdss_shard_00000.npy',   f'{ART_DIR}/best_sdss_native.pt'),
        ('lamost_native', f'{ART_DIR}/lamost_shard_00000.npy', f'{ART_DIR}/best_lamost_native.pt'),
    ]
    results = {}
    for name, shard, model in surveys:
        results[name] = run_survey(name, shard, model, device)

    combined = {
        'task': 'P3-PATHC-INJECTION-RECOVERY-ALL-SURVEYS (spectral surveys subtask)',
        'gate_amp_sigma': GATE_AMP,
        'gate_recovery_required': GATE_RECOV,
        'per_survey': {name: {
            'gate_pass': results[name]['gate_pass'],
            'gate_recovery_observed': results[name]['gate_recovery_observed'],
            'clean_mse_p99': results[name]['clean_mse_p99'],
            'full_curve': {k: v['recovery_fraction'] for k, v in results[name]['levels'].items()},
        } for name in results},
        'note': (
            'Two of five BigAE-scored surveys validated (SDSS DR18 + LAMOST DR10). '
            'CMB native retrain has injection-recovery integrated into '
            'cmb_native_retrain.py and runs at training-gate time (fire #83+). '
            'eROSITA, NEOWISE, Gaia, DESI are deferred to separate fires: '
            'eROSITA + Gaia use different feature extractors, NEOWISE uses '
            'variability features (Stetson-J/chi2), DESI requires its '
            'production BigAE checkpoint which is on pod under the 5-fold '
            'kfold training plan (criterion #4).'
        ),
    }
    out = os.path.join(OUT_DIR, 'injection_recovery_summary.json')
    with open(out, 'w') as f:
        json.dump(combined, f, indent=2)
    print(f'\nwrote combined summary -> {out}', flush=True)


if __name__ == '__main__':
    main()
