#!/usr/bin/env python3
"""
Photo-z from Autoencoder Latent Vectors (H200 GPU).

Trains PyTorch MLP: 128-dim latent -> spectroscopic z. Tests whether the
anomaly-detection autoencoder implicitly encodes redshift — publishable if so.

Data: tries SDSS parquets + spZbest FITS for redshifts, falls back to DESI
parquets (which already have z). Output -> /workspace/bigbounce/outputs/photoz_latent/
"""
import glob, json, os, sys, time, traceback
import numpy as np, torch, torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
sys.stdout.reconfigure(line_buffering=True)

# ─── Config ──────────────────────────────────────────────────────────────
SDSS_DIR  = "/workspace/bigbounce/outputs"
DESI_DIR  = "/workspace/bigbounce/outputs"
ZBEST_DIR = "/workspace/desi_dr1"
OUT_DIR   = "/workspace/bigbounce/outputs/photoz_latent"
SEED, BATCH_SIZE, LR, EPOCHS, PATIENCE = 42, 4096, 1e-3, 80, 10
LAT_COLS = [f"lat_{i:03d}" for i in range(128)]

# ─── Model ───────────────────────────────────────────────────────────────
class PhotozMLP(nn.Module):
    def __init__(self, n_in=128, hidden=(512, 256, 128)):
        super().__init__()
        layers = []
        prev = n_in
        for h in hidden:
            layers += [nn.Linear(prev, h), nn.BatchNorm1d(h), nn.ReLU(), nn.Dropout(0.1)]
            prev = h
        layers.append(nn.Linear(prev, 1))
        self.net = nn.Sequential(*layers)
    def forward(self, x):
        return self.net(x).squeeze(-1)

# ─── Metrics ─────────────────────────────────────────────────────────────
def compute_metrics(yt, yp):
    dz = (yp - yt) / (1.0 + yt)
    return {
        "sigma_nmad": round(float(1.4826 * np.median(np.abs(dz - np.median(dz)))), 6),
        "outlier_fraction_015": round(float(np.mean(np.abs(dz) > 0.15)), 5),
        "bias": round(float(np.mean(dz)), 6),
        "mae": round(float(np.mean(np.abs(yp - yt))), 6),
        "rmse": round(float(np.sqrt(np.mean((yp - yt)**2))), 6),
        "r2": round(float(1 - np.sum((yt - yp)**2) / np.sum((yt - np.mean(yt))**2)), 6),
    }

# ─── Data loading ────────────────────────────────────────────────────────
def load_desi():
    import pyarrow.parquet as pq
    files = sorted(glob.glob(os.path.join(DESI_DIR, "desi_dr1_catalog_batch_*.parquet")))
    if not files: return None, None
    print(f"  Found {len(files)} DESI files")
    Xs, zs, n_raw = [], [], 0
    for i, f in enumerate(files):
        try:
            df = pq.read_table(f, columns=LAT_COLS + ["z", "zwarn"]).to_pandas()
        except Exception:
            try: df = pq.read_table(f, columns=LAT_COLS + ["z"]).to_pandas(); df["zwarn"] = 0
            except Exception: continue
        n_raw += len(df)
        m = (df["z"] > 0.001) & (df["z"] < 6.0) & df["z"].notna() & (df["zwarn"] == 0)
        df = df.loc[m]
        if len(df): Xs.append(df[LAT_COLS].values.astype(np.float32)); zs.append(df["z"].values.astype(np.float32))
        if (i+1) % 10 == 0: print(f"    {i+1}/{len(files)}, {sum(len(c) for c in zs):,} good")
    if not Xs: return None, None
    X, z = np.concatenate(Xs), np.concatenate(zs)
    print(f"  DESI: {n_raw:,} raw -> {len(z):,} valid"); return X, z

def load_sdss():
    import pyarrow.parquet as pq
    files = sorted(glob.glob(os.path.join(SDSS_DIR, "sdss_batch_*.parquet")))
    if not files: return None, None
    print(f"  Found {len(files)} SDSS files")
    chunks = []
    for f in files:
        try: chunks.append(pq.read_table(f, columns=["plate","mjd","fiberid"]+LAT_COLS).to_pandas())
        except Exception: pass
    if not chunks: return None, None
    import pandas as pd
    sdss = pd.concat(chunks, ignore_index=True)
    print(f"  SDSS: {len(sdss):,} spectra")
    # Cross-match redshifts from spZbest FITS
    z_map = {}
    if os.path.isdir(ZBEST_DIR):
        from astropy.io import fits as af
        for zf in glob.glob(os.path.join(ZBEST_DIR, "**", "spZbest-*.fits"), recursive=True):
            try:
                with af.open(zf, memmap=True) as h:
                    for r in h[1].data:
                        z_map[(int(r["PLATE"]),int(r["MJD"]),int(r["FIBERID"]))] = float(r["Z"])
            except Exception: pass
        print(f"  Loaded {len(z_map):,} redshifts from spZbest")
    if len(z_map) < 100:
        print("  Insufficient redshifts for SDSS"); return None, None
    z_arr = np.array([z_map.get((int(r.plate),int(r.mjd),int(r.fiberid)), np.nan)
                      for _, r in sdss.iterrows()], dtype=np.float32)
    ok = np.isfinite(z_arr) & (z_arr > 0.001) & (z_arr < 6.0)
    print(f"  Matched {ok.sum():,}/{len(sdss):,}")
    if ok.sum() < 100: return None, None
    return sdss.loc[ok, LAT_COLS].values.astype(np.float32), z_arr[ok]

def load_data():
    print("\n[1] Trying SDSS + spZbest...")
    X, z = load_sdss()
    if X is not None and len(z) >= 1000: return X, z, "sdss"
    print("[2] Trying DESI catalog...")
    X, z = load_desi()
    if X is not None and len(z) >= 1000: return X, z, "desi"
    print("FATAL: no usable data"); sys.exit(1)

# ─── Training ────────────────────────────────────────────────────────────
def train_model(Xtr, ytr, Xv, yv, dev):
    model = PhotozMLP().to(dev)
    opt = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-5)
    sched = torch.optim.lr_scheduler.ReduceLROnPlateau(opt, patience=5, factor=0.5, min_lr=1e-6)
    crit = nn.HuberLoss(delta=0.1)
    dl = DataLoader(TensorDataset(torch.tensor(Xtr), torch.tensor(ytr)),
                    batch_size=BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True, drop_last=True)
    Xvt, yvt = torch.tensor(Xv).to(dev), torch.tensor(yv).to(dev)
    best_vl, best_st, wait = float("inf"), None, 0
    hist = {"train_loss": [], "val_loss": []}
    for ep in range(EPOCHS):
        model.train(); losses = []
        for xb, yb in dl:
            xb, yb = xb.to(dev, non_blocking=True), yb.to(dev, non_blocking=True)
            loss = crit(model(xb), yb); opt.zero_grad(); loss.backward(); opt.step()
            losses.append(loss.item())
        model.eval()
        with torch.no_grad(): vl = crit(model(Xvt), yvt).item()
        tl = np.mean(losses); sched.step(vl)
        hist["train_loss"].append(round(tl,6)); hist["val_loss"].append(round(vl,6))
        if vl < best_vl: best_vl=vl; best_st={k:v.cpu().clone() for k,v in model.state_dict().items()}; wait=0
        else: wait += 1
        if (ep+1)%5==0 or wait==0:
            print(f"  Ep {ep+1:3d}/{EPOCHS}  train={tl:.5f}  val={vl:.5f}  best={best_vl:.5f}  wait={wait}")
        if wait >= PATIENCE: print(f"  Early stop ep {ep+1}"); break
    model.load_state_dict(best_st); model.eval(); return model, hist

# ─── Main ────────────────────────────────────────────────────────────────
def main():
    t0 = time.time(); os.makedirs(OUT_DIR, exist_ok=True)
    ckpt = os.path.join(OUT_DIR, "checkpoint.json")
    print("="*65+"\nPHOTO-Z FROM AUTOENCODER LATENT VECTORS\n"+"="*65)
    dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {dev}" + (f"  GPU: {torch.cuda.get_device_name()}" if dev.type=="cuda" else ""))
    np.random.seed(SEED); torch.manual_seed(SEED)

    X, z, src = load_data()
    # Cap at 2M, drop NaN
    if len(z) > 2_000_000: idx=np.random.choice(len(z),2_000_000,replace=False); X,z=X[idx],z[idx]
    ok = np.all(np.isfinite(X),1) & np.isfinite(z); X,z = X[ok],z[ok]
    print(f"Source: {src}  |  N={len(z):,}  |  z=[{z.min():.3f},{z.max():.3f}]  med={np.median(z):.3f}")

    # Split: 70/10/20
    idx = np.random.permutation(len(z))
    nt = int(len(z)*0.2); nv = int(len(z)*0.1)
    Xte,yte = X[idx[:nt]],z[idx[:nt]]
    Xv,yv   = X[idx[nt:nt+nv]],z[idx[nt:nt+nv]]
    Xtr,ytr = X[idx[nt+nv:]],z[idx[nt+nv:]]
    print(f"Split: train={len(ytr):,}  val={len(yv):,}  test={len(yte):,}")
    _ckpt(ckpt,"data_loaded",source=src,n_train=int(len(ytr)),n_test=int(len(yte)))

    # Train
    print(f"\n{'='*65}\nTRAINING: PyTorch MLP (512-256-128) HuberLoss\n{'='*65}")
    tt = time.time(); model, hist = train_model(Xtr,ytr,Xv,yv,dev); tt = time.time()-tt
    print(f"Train time: {tt:.1f}s"); _ckpt(ckpt,"trained",time_s=round(tt,1))

    # Evaluate
    print(f"\n{'='*65}\nEVALUATION\n{'='*65}")
    model.eval()
    with torch.no_grad(): yp = model(torch.tensor(Xte).to(dev)).cpu().numpy()
    met = compute_metrics(yte, yp)
    for k,v in met.items(): print(f"  {k:25s} {v}")

    # Baseline: Ridge
    print(f"\n{'='*65}\nBASELINE: Ridge Regression\n{'='*65}")
    try:
        from sklearn.linear_model import Ridge
        rp = Ridge(alpha=1.0).fit(Xtr,ytr).predict(Xte)
        bm = compute_metrics(yte, rp)
        print(f"  Ridge sigma_NMAD={bm['sigma_nmad']:.6f}  outlier={bm['outlier_fraction_015']*100:.2f}%")
    except ImportError:
        w,_,_,_ = np.linalg.lstsq(np.c_[Xtr,np.ones(len(Xtr))],ytr,rcond=None)
        rp = np.c_[Xte,np.ones(len(Xte))] @ w; bm = compute_metrics(yte, rp)

    # Save predictions
    try:
        import pyarrow as pa, pyarrow.parquet as pq
        pq.write_table(pa.table({"z_true":yte.astype(np.float64),"z_pred":yp.astype(np.float64),
            "dz_norm":((yp-yte)/(1+yte)).astype(np.float64)}),
            os.path.join(OUT_DIR,"photoz_predictions.parquet"), compression="zstd")
    except ImportError:
        np.savez(os.path.join(OUT_DIR,"photoz_predictions.npz"), z_true=yte, z_pred=yp)

    # Summary JSON
    total = time.time()-t0
    summary = {"description":"Photo-z from 128-dim autoencoder latent vectors",
        "source":src, "n_total":int(len(z)), "n_train":int(len(ytr)),
        "n_val":int(len(yv)), "n_test":int(len(yte)),
        "z_range":[round(float(z.min()),4),round(float(z.max()),4)],
        "model":{"type":"PyTorch MLP","arch":"128->512->BN->ReLU->256->BN->ReLU->128->BN->ReLU->1",
            "loss":"Huber(0.1)","epochs":len(hist["train_loss"]),"time_s":round(tt,1),
            "n_params":sum(p.numel() for p in model.parameters())},
        "metrics":met, "baseline_ridge":bm,
        "improvement":{"sigma_nmad_ratio":round(bm["sigma_nmad"]/max(met["sigma_nmad"],1e-9),2),
            "outlier_ratio":round(bm["outlier_fraction_015"]/max(met["outlier_fraction_015"],1e-9),2)},
        "device":str(dev), "runtime_s":round(total,1)}
    with open(os.path.join(OUT_DIR,"photoz_summary.json"),"w") as f: json.dump(summary,f,indent=2)
    _ckpt(ckpt,"COMPLETE",metrics=met,source=src,runtime_s=round(total,1))

    print(f"\n{'='*65}\nDONE  sigma_NMAD={met['sigma_nmad']:.6f}  outlier={met['outlier_fraction_015']*100:.2f}%"
          f"  R2={met['r2']:.4f}  vs Ridge {summary['improvement']['sigma_nmad_ratio']:.1f}x"
          f"\n{'='*65}")

def _ckpt(p, status, **kw):
    with open(p,"w") as f: json.dump({"status":status,"ts":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),**kw},f,indent=2)

if __name__ == "__main__":
    try: main()
    except Exception: traceback.print_exc(); sys.exit(1)
