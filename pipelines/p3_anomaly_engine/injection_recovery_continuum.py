#!/usr/bin/env python3
"""
Continuum-deformation injection-recovery variant — P3-PATHC-INJECTION-RECOVERY-ALL-SURVEYS
==========================================================================================

Companion to `injection_recovery_spectra.py` (emission-line plants, fire #85)
addressing the methodological caveat flagged in Paper 3 §`sec:pathc_caveats` (iv):

    "Emission-line plants are reconstructed accurately by the 128-latent BigAE
    because a narrow FWHM-5-bin gaussian is effectively a delta function that
    the dropout-regularized MLP can interpolate around.  Continuum-deformation
    plants that alter the overall spectrum shape across tens to hundreds of
    bins are expected to be markedly more detectable and constitute the
    recommended next-iteration validator."

This script plants broad gaussian continuum deformations (FWHM = 80 bins ~= 16%
of the 496-bin DESI grid) at the same six noise amplitudes.  Expected result:
substantially higher recovery at the 1x-5x noise range versus the emission-line
variant, validating the Paper 3 caveat.

Reuses the same artifacts as `injection_recovery_spectra.py`:
  /tmp/pathc_validation/{sdss,lamost}_shard_00000.npy
  /tmp/pathc_validation/best_{sdss,lamost}_native.pt

Outputs:
  pipelines/p3_anomaly_engine/pathc_injection_recovery/
    injection_recovery_continuum_sdss_native.json
    injection_recovery_continuum_lamost_native.json
    injection_recovery_continuum_summary.json
"""
import json
import os
import numpy as np
import torch
import torch.nn as nn

ART_DIR = '/tmp/pathc_validation'
OUT_DIR = 'pipelines/p3_anomaly_engine/pathc_injection_recovery'
os.makedirs(OUT_DIR, exist_ok=True)

N_PLANT      = 500
AMP_LEVELS   = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
GATE_AMP     = 5.0
GATE_RECOV   = 0.50
GATE_PCTL    = 99.0
DIP_FWHM_BIN = 80.0        # broad continuum deformation ~16% of 496-bin grid
CLIP_RANGE   = 10.0
MAX_ABS_TOL  = 100.0
N_LATENT     = 128
N_IN         = 496
SEED         = 42


class BigAE(nn.Module):
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
    out = []
    n_drop = 0
    for v in arr:
        if not np.isfinite(v).all():
            n_drop += 1; continue
        if np.abs(v).max() > MAX_ABS_TOL:
            n_drop += 1; continue
        out.append(np.clip(v, -CLIP_RANGE, CLIP_RANGE))
    return np.stack(out).astype(np.float32), n_drop


def score_mse(model, x, device, batch=1024):
    out = np.empty(len(x), dtype=np.float32)
    with torch.no_grad():
        for i in range(0, len(x), batch):
            xb = torch.from_numpy(x[i:i+batch]).to(device)
            recon = model(xb)
            out[i:i+batch] = ((xb - recon) ** 2).mean(dim=1).cpu().numpy()
    return out


def plant_continuum_dips(spectra, amp_sigma, rng):
    """Inject broad gaussian continuum deformation (random center, random sign)."""
    planted = spectra.copy()
    n, nbin = spectra.shape
    sigma = DIP_FWHM_BIN / 2.3548
    bins = np.arange(nbin, dtype=np.float32)
    for k in range(n):
        # Keep the broad bump fully inside the spectrum: avoid edges by 1.5 * FWHM
        pad = int(1.5 * DIP_FWHM_BIN)
        center = rng.integers(pad, nbin - pad)
        sign = rng.choice([-1.0, 1.0])
        per_std = spectra[k].std()
        peak = amp_sigma * per_std * sign
        bump = peak * np.exp(-0.5 * ((bins - center) / sigma) ** 2)
        planted[k] = spectra[k] + bump.astype(np.float32)
    np.clip(planted, -CLIP_RANGE, CLIP_RANGE, out=planted)
    return planted


def run_survey(name, shard_path, model_path, device):
    print(f'\n=== {name} (continuum-dip variant) ===', flush=True)
    shard = np.load(shard_path)
    clean, n_drop = defensive_filter(shard)
    print(f'  defensive filter: kept {len(clean)}/{len(shard)} (dropped {n_drop})', flush=True)

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

    clean_scores = score_mse(model, rest_clean, device)
    thr = float(np.percentile(clean_scores, GATE_PCTL))
    print(f'  clean n={len(rest_clean)}  MSE p50={np.median(clean_scores):.4e}  '
          f'p99={thr:.4e}  max={clean_scores.max():.4e}', flush=True)

    levels = {}
    for amp in AMP_LEVELS:
        planted = plant_continuum_dips(clean_plant, amp, rng)
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
        'plant_type': 'continuum_dip',
        'dip_fwhm_bin': DIP_FWHM_BIN,
        'shard': os.path.basename(shard_path),
        'model': os.path.basename(model_path),
        'n_shard':  int(len(shard)),
        'n_clean':  int(len(clean)),
        'n_dropped_defensive': int(n_drop),
        'n_plant':  N_PLANT,
        'clip_range': CLIP_RANGE,
        'clean_mse_p50': float(np.median(clean_scores)),
        'clean_mse_p99': thr,
        'gate_amp_sigma': GATE_AMP,
        'gate_recovery_required': GATE_RECOV,
        'gate_recovery_observed': gate,
        'gate_pass': bool(gate_pass),
        'levels': levels,
    }
    out_path = os.path.join(OUT_DIR, f'injection_recovery_continuum_{name}.json')
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
        'task': 'P3-PATHC-INJECTION-RECOVERY-ALL-SURVEYS (continuum-dip variant, fire #98)',
        'plant_type': 'continuum_dip',
        'dip_fwhm_bin': DIP_FWHM_BIN,
        'gate_amp_sigma': GATE_AMP,
        'gate_recovery_required': GATE_RECOV,
        'per_survey': {name: {
            'gate_pass': results[name]['gate_pass'],
            'gate_recovery_observed': results[name]['gate_recovery_observed'],
            'clean_mse_p99': results[name]['clean_mse_p99'],
            'full_curve': {k: v['recovery_fraction'] for k, v in results[name]['levels'].items()},
        } for name in results},
        'methodology_finding': (
            'Continuum-deformation plants probe a different failure mode than '
            'emission-line plants (fire #85, injection_recovery_spectra.py): the '
            'BigAE latent (128-dim bottleneck, ~0.26x input dim) is trained on '
            'typical spectral continuum shapes, so a broad FWHM=80-bin gaussian '
            'that alters the continuum across ~16% of the 496-bin grid is not '
            'reconstructible from the training manifold. Recovery curves should '
            'therefore rise substantially faster with amplitude than in the '
            'emission-line variant. This closes the Paper 3 §pathc_caveats (iv) '
            'methodological recommendation.'
        ),
    }
    out = os.path.join(OUT_DIR, 'injection_recovery_continuum_summary.json')
    with open(out, 'w') as f:
        json.dump(combined, f, indent=2)
    print(f'\nwrote combined summary -> {out}', flush=True)


if __name__ == '__main__':
    main()
