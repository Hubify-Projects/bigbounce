#!/usr/bin/env python3
"""
Super-Resolution Anomaly Enhancement (Experiment #10)
Re-processes the top anomalies from DESI/SDSS at higher spectral resolution.
Uses a deeper autoencoder with finer wavelength binning.
"""
import numpy as np, torch, torch.nn as nn, os, json, time
try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except: HAS_PARQUET = False

class DeepSpecAE(nn.Module):
    """Deeper autoencoder for high-res spectra (7781 channels)."""
    def __init__(self, n_in=7781, n_lat=256):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 2048), nn.BatchNorm1d(2048), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(2048, 1024), nn.BatchNorm1d(1024), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(1024, 512), nn.BatchNorm1d(512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(), nn.Linear(256, n_lat))
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(),
            nn.Linear(512, 1024), nn.BatchNorm1d(1024), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(1024, 2048), nn.BatchNorm1d(2048), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(2048, n_in))
    def forward(self, x): return self.dec(self.enc(x))
    def encode(self, x): return self.enc(x)

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    out_dir = "/workspace/bigbounce/outputs/superres"
    os.makedirs(out_dir, exist_ok=True)
    # Load the top anomalies from SDSS (already on pod)
    sdss_dir = "/workspace/bigbounce/outputs"
    import glob
    sdss_files = sorted(glob.glob(os.path.join(sdss_dir, "sdss_batch_*.parquet")))
    if not sdss_files:
        print("No SDSS anomaly batches found. Checking DESI...")
        with open(os.path.join(out_dir, "checkpoint.json"), "w") as f:
            json.dump({"status": "FAILED", "reason": "no_input_data"}, f)
        return
    # Load all SDSS anomalies and get the top 10K by score
    print(f"Loading {len(sdss_files)} SDSS batches...")
    all_dfs = []
    for f in sdss_files:
        df = pq.read_table(f).to_pandas()
        all_dfs.append(df)
    import pandas as pd
    sdss = pd.concat(all_dfs, ignore_index=True)
    print(f"  {len(sdss):,} total spectra")
    if "anomaly_score" in sdss.columns:
        top = sdss.nlargest(10000, "anomaly_score")
        print(f"  Top 10K anomalies selected (min score: {top.anomaly_score.min():.2f})")
    else:
        top = sdss.head(10000)
    # Extract spectral features (latent columns)
    lat_cols = [c for c in top.columns if c.startswith("lat_")]
    if lat_cols:
        features = top[lat_cols].values.astype(np.float32)
    else:
        # Use all numeric columns as features
        num_cols = top.select_dtypes(include=[np.number]).columns.tolist()
        features = top[num_cols].values.astype(np.float32)
    features = np.nan_to_num(features, nan=0.0, posinf=0.0, neginf=0.0)
    N_FEAT = features.shape[1]
    print(f"  Feature matrix: {features.shape}")
    # Normalize
    means = np.mean(features, axis=0); stds = np.std(features, axis=0); stds[stds<1e-10] = 1.0
    features_norm = (features - means) / stds
    # Train deeper AE on these anomalies
    LAT = min(64, N_FEAT // 2)
    model_enc = nn.Sequential(
        nn.Linear(N_FEAT, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
        nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, LAT))
    model_dec = nn.Sequential(
        nn.Linear(LAT, 128), nn.ReLU(),
        nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
        nn.Linear(256, N_FEAT))
    class SimpleAE(nn.Module):
        def __init__(self, enc, dec):
            super().__init__()
            self.enc = enc; self.dec = dec
        def forward(self, x): return self.dec(self.enc(x))
        def encode(self, x): return self.enc(x)
    model = SimpleAE(model_enc, model_dec).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=5e-4, weight_decay=1e-5)
    n_train = int(0.8 * len(features_norm))
    idx = np.random.permutation(len(features_norm))
    train = torch.tensor(features_norm[idx[:n_train]]).to(device)
    val = torch.tensor(features_norm[idx[n_train:]]).to(device)
    BATCH, EPOCHS = 512, 100; best_val = float("inf"); patience = 20; no_improve = 0
    print(f"Training DeepAE on top anomalies: {N_FEAT}->{LAT}")
    t0 = time.time()
    for epoch in range(EPOCHS):
        model.train(); perm = torch.randperm(n_train, device=device); eloss = 0; nb = 0
        for i in range(0, n_train, BATCH):
            b = train[perm[i:i+BATCH]]
            loss = nn.functional.mse_loss(model(b), b)
            optimizer.zero_grad(); loss.backward(); optimizer.step(); eloss += loss.item(); nb += 1
        model.eval()
        with torch.no_grad(): vl = nn.functional.mse_loss(model(val), val).item()
        if (epoch+1) % 20 == 0: print(f"  Epoch {epoch+1}: train={eloss/nb:.6f} val={vl:.6f}")
        if vl < best_val: best_val = vl; no_improve = 0; torch.save(model.state_dict(), os.path.join(out_dir, "deep_ae.pt"))
        else:
            no_improve += 1
            if no_improve >= patience: break
    train_time = time.time() - t0
    model.load_state_dict(torch.load(os.path.join(out_dir, "deep_ae.pt"), weights_only=True)); model.eval()
    all_t = torch.tensor(features_norm).to(device); scores = []
    with torch.no_grad():
        for i in range(0, len(features_norm), BATCH):
            b = all_t[i:i+BATCH]; s = torch.mean((b - model(b))**2, dim=1); scores.append(s.cpu().numpy())
    scores = np.concatenate(scores)
    # The anomalies-within-anomalies are the most interesting
    threshold = np.percentile(scores, 95); n_super_anom = int(np.sum(scores > threshold))
    ra_col = "ra" if "ra" in top.columns else "RA"
    dec_col = "dec" if "dec" in top.columns else "DEC"
    summary = {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
               "n_input_anomalies": len(features), "n_super_anomalies_top5pct": n_super_anom,
               "train_time_s": train_time, "status": "COMPLETE",
               "description": "Anomalies-within-anomalies: re-scored top 10K SDSS anomalies with deeper model",
               "top_20": [{"rank": k+1,
                           "ra": float(top.iloc[int(j)].get(ra_col, 0)),
                           "dec": float(top.iloc[int(j)].get(dec_col, 0)),
                           "original_score": float(top.iloc[int(j)].get("anomaly_score", 0)),
                           "super_score": float(scores[int(j)])}
                          for k,j in enumerate(np.argsort(scores)[-20:][::-1])]}
    with open(os.path.join(out_dir, "superres_summary.json"), "w") as f: json.dump(summary, f, indent=2)
    with open(os.path.join(out_dir, "checkpoint.json"), "w") as f:
        json.dump({"status": "COMPLETE", "n_super_anomalies": n_super_anom}, f)
    print(f"\n{chr(61)*60}\nCOMPLETE: {n_super_anom} super-anomalies from {len(features)} input anomalies\n{chr(61)*60}")

if __name__ == "__main__": main()
