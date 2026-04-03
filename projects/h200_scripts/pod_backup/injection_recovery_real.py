#!/usr/bin/env python3
"""
Injection/Recovery Test with REAL BigAE Model
=============================================
Inject synthetic unusual spectra, run through BigAE, measure recovery.
"""
import numpy as np
import torch
import torch.nn as nn
import os, json, time

class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, n_lat))
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in))
    def forward(self, x): return self.dec(self.enc(x))

def make_synthetic_spectra(n=1000):
    """Generate synthetic unusual spectra for injection testing."""
    spectra = []
    labels = []
    wl = np.linspace(3600, 9800, 496)
    
    # Type 1: Strong emission line galaxy (Hα at various z)
    for z in np.linspace(0.1, 1.5, n//5):
        spec = np.random.normal(1.0, 0.1, 496)  # Continuum
        ha_obs = 6563 * (1 + z)
        if 3600 < ha_obs < 9800:
            idx = int((ha_obs - 3600) / (9800 - 3600) * 496)
            spec[max(0,idx-2):min(496,idx+3)] += np.random.uniform(2, 10)  # Strong line
        spectra.append(spec)
        labels.append(f'emission_line_z{z:.2f}')
    
    # Type 2: BAL QSO (broad absorption)
    for _ in range(n//5):
        spec = np.random.normal(1.0, 0.1, 496)
        # Add broad absorption trough
        center = np.random.randint(100, 400)
        width = np.random.randint(20, 60)
        depth = np.random.uniform(0.3, 0.8)
        spec[max(0,center-width):min(496,center+width)] *= (1 - depth)
        spectra.append(spec)
        labels.append('bal_qso')
    
    # Type 3: Lyman break galaxy (flux drops to zero below break)
    for z in np.linspace(2.5, 6.0, n//5):
        spec = np.random.normal(1.0, 0.1, 496)
        break_obs = 912 * (1 + z)
        if 3600 < break_obs < 9800:
            idx = int((break_obs - 3600) / (9800 - 3600) * 496)
            spec[:idx] = np.random.normal(0.0, 0.05, idx)  # Zero flux below break
        spectra.append(spec)
        labels.append(f'lyman_break_z{z:.2f}')
    
    # Type 4: Unusual continuum (very red or very blue)
    for _ in range(n//5):
        spec = np.random.normal(1.0, 0.1, 496)
        slope = np.random.choice([-1, 1]) * np.random.uniform(0.5, 2.0)
        spec *= np.linspace(1 - slope, 1 + slope, 496)
        spectra.append(spec)
        labels.append('unusual_continuum')
    
    # Type 5: Normal galaxies (for false positive testing)
    for _ in range(n//5):
        spec = np.random.normal(1.0, 0.05, 496)  # Low noise, flat
        # Add typical absorption features
        for line_idx in [120, 180, 250]:  # Ca K, Mg, Na
            spec[line_idx-1:line_idx+2] *= 0.85
        spectra.append(spec)
        labels.append('normal_galaxy')
    
    return np.array(spectra, dtype=np.float32), labels

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}')
    
    model = BigAE(496, 128).to(device)
    state_dict = torch.load('best_model_47k.pt', map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
    model.eval()
    print('Model loaded.')
    
    # Generate synthetic spectra
    print('Generating 5000 synthetic spectra...')
    spectra, labels = make_synthetic_spectra(5000)
    
    # Run through model
    print('Running inference...')
    scores = []
    batch_size = 512
    for i in range(0, len(spectra), batch_size):
        batch = torch.tensor(spectra[i:i+batch_size]).to(device)
        with torch.no_grad():
            recon = model(batch)
        residuals = (batch - recon).cpu().numpy()
        batch_scores = np.mean(residuals**2, axis=1)
        scores.extend(batch_scores.tolist())
    
    scores = np.array(scores)
    
    # Analyze recovery by type
    print('\n' + '='*60)
    print('INJECTION/RECOVERY RESULTS (REAL MODEL)')
    print('='*60)
    
    results = {}
    types = set(l.split('_z')[0] for l in labels)
    for t in sorted(types):
        mask = np.array([l.startswith(t) or l.split('_z')[0] == t for l in labels])
        t_scores = scores[mask]
        n = len(t_scores)
        rec_3 = np.sum(t_scores > np.median(scores) * 3) / n * 100
        rec_5 = np.sum(t_scores > np.median(scores) * 5) / n * 100
        mean_s = np.mean(t_scores)
        
        print(f'\n{t} (N={n}):')
        print(f'  Mean score: {mean_s:.4f}')
        print(f'  Recovery >3x median: {rec_3:.1f}%')
        print(f'  Recovery >5x median: {rec_5:.1f}%')
        
        results[t] = {
            'N': int(n), 'mean_score': float(mean_s),
            'recovery_3x': float(rec_3), 'recovery_5x': float(rec_5),
            'scores_p50': float(np.median(t_scores)),
            'scores_p90': float(np.percentile(t_scores, 90)),
            'scores_p99': float(np.percentile(t_scores, 99)),
        }
    
    # Save
    os.makedirs('outputs/injection_recovery_real', exist_ok=True)
    with open('outputs/injection_recovery_real/results.json', 'w') as f:
        json.dump({'method': 'synthetic_injection_real_BigAE', 'results': results,
                   'median_score': float(np.median(scores)), 'n_total': len(scores)}, f, indent=2)
    print(f'\nSaved to outputs/injection_recovery_real/results.json')

if __name__ == '__main__':
    main()
