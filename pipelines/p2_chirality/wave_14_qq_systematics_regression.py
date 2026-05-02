"""
Wave 14-QQ (FIXED): Deep systematics regression on cached chirality_v2 logits.
class_eq is string ("CW"/"CCW"/"NOT_SPIRAL"), not int. Map "CW"->0, "CCW"->1.
"""
import os, json, time
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

OUT = "/workspace/r42_wave14qq"
os.makedirs(OUT, exist_ok=True)

CATALOG_LOGITS = "/workspace/r42_b20/chirality_catalog/catalog_production.parquet"
CATALOG_BA     = "/workspace/dr8_sweep_fetch/catalog_production_with_ba.parquet"
SEED = 20260501
N_FOLDS = 5
N_EPOCHS = 50
BATCH = 4096
LR = 1e-3
HIDDEN = (256, 128, 64)

torch.manual_seed(SEED); np.random.seed(SEED)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[wave14qq] device={device}, gpu={torch.cuda.get_device_name(0) if device=='cuda' else 'cpu'}")

t0 = time.time()
print("[wave14qq] loading catalogs ...")
df_logits = pd.read_parquet(CATALOG_LOGITS, columns=["dr8_id","class_eq","p_cw_eq","p_ccw_eq","p_ns_eq"])
df_ba     = pd.read_parquet(CATALOG_BA)
print(f"[wave14qq] logits rows={len(df_logits):,}  ba rows={len(df_ba):,}")

df = df_logits.merge(df_ba, on="dr8_id", how="inner")
print(f"[wave14qq] joined rows={len(df):,}")

print(f"[wave14qq] class_eq value_counts: {dict(df['class_eq'].value_counts())}")
df_sp = df[df["class_eq"].isin(["CW","CCW"])].copy()
df_sp["y"] = (df_sp["class_eq"] == "CCW").astype(np.int64)
print(f"[wave14qq] spiral rows (CW+CCW)={len(df_sp):,}  CW={(df_sp['y']==0).sum():,}  CCW={(df_sp['y']==1).sum():,}")

type_cats = sorted(df_sp["type"].astype(str).unique().tolist())
print(f"[wave14qq] type categories: {type_cats}")
type_oh = pd.get_dummies(df_sp["type"].astype(str), prefix="type")

feat_cols = ["b_over_a","fracdev","shape_r_eff","shapedev_e1","shapedev_e2",
             "shapeexp_r","shapeexp_e1","shapeexp_e2","e1_eff","e2_eff",
             "e_mag","ra","dec"]

X_num = df_sp[feat_cols].astype(np.float32).fillna(0.0).values
X_cat = type_oh.astype(np.float32).values
X = np.concatenate([X_num, X_cat], axis=1)
y = df_sp["y"].values.astype(np.int64)

print(f"[wave14qq] X shape={X.shape}")

scaler = StandardScaler()
X[:, :len(feat_cols)] = scaler.fit_transform(X[:, :len(feat_cols)])

class MLP(nn.Module):
    def __init__(self, in_dim, hidden):
        super().__init__()
        layers = []
        d = in_dim
        for h in hidden:
            layers += [nn.Linear(d, h), nn.ReLU(), nn.Dropout(0.2)]
            d = h
        layers += [nn.Linear(d, 1)]
        self.net = nn.Sequential(*layers)
    def forward(self, x):
        return self.net(x).squeeze(-1)

kf = KFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
fold_results = []

for fold, (idx_tr, idx_va) in enumerate(kf.split(X)):
    fold_t0 = time.time()
    print(f"\n[wave14qq] === Fold {fold+1}/{N_FOLDS} ===")
    X_tr = torch.from_numpy(X[idx_tr]).float()
    y_tr = torch.from_numpy(y[idx_tr]).float()
    X_va = torch.from_numpy(X[idx_va]).float()
    y_va = torch.from_numpy(y[idx_va]).float()

    ds_tr = TensorDataset(X_tr, y_tr)
    dl_tr = DataLoader(ds_tr, batch_size=BATCH, shuffle=True, num_workers=4, pin_memory=True)
    X_va_d = X_va.to(device); y_va_d = y_va.to(device)

    model = MLP(X.shape[1], HIDDEN).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=N_EPOCHS)
    bce = nn.BCEWithLogitsLoss()

    for ep in range(N_EPOCHS):
        model.train()
        n_seen, loss_sum = 0, 0.0
        for xb, yb in dl_tr:
            xb = xb.to(device, non_blocking=True); yb = yb.to(device, non_blocking=True)
            logits = model(xb)
            loss = bce(logits, yb)
            opt.zero_grad(set_to_none=True); loss.backward(); opt.step()
            loss_sum += loss.item() * xb.size(0); n_seen += xb.size(0)
        sched.step()
        if ep % 5 == 0 or ep == N_EPOCHS-1:
            model.eval()
            with torch.no_grad():
                logits_va = model(X_va_d).cpu().numpy()
            auc_va = roc_auc_score(y_va.numpy(), logits_va)
            print(f"  ep {ep:3d}  train_loss={loss_sum/n_seen:.5f}  val_AUC={auc_va:.5f}", flush=True)

    model.eval()
    with torch.no_grad():
        logits_va = model(X_va_d).cpu().numpy()
    auc_final = float(roc_auc_score(y_va.numpy(), logits_va))
    fold_dt = time.time() - fold_t0
    print(f"[wave14qq] Fold {fold+1} final AUC={auc_final:.5f}  wall={fold_dt:.1f}s", flush=True)
    fold_results.append({"fold": fold+1, "n_train": int(len(idx_tr)),
                         "n_val": int(len(idx_va)), "auc": auc_final,
                         "wall_s": fold_dt})

aucs = np.array([r["auc"] for r in fold_results])
mean_auc, std_auc = float(aucs.mean()), float(aucs.std(ddof=1))

if abs(mean_auc - 0.5) < 0.02:
    verdict = "CLEAN_NULL"
    interp = f"AUC={mean_auc:.4f} ± {std_auc:.4f} ≈ 0.5: systematics cannot recover chirality. Signal is morphology-orthogonal. Reinforces P4-OA-M1 closure."
elif mean_auc > 0.55:
    verdict = "SYSTEMATICS_LEAK"
    interp = f"AUC={mean_auc:.4f} ± {std_auc:.4f} > 0.55: systematics CAN recover chirality. Signal contamination — re-examine P4 systematics narrative."
else:
    verdict = "MARGINAL"
    interp = f"AUC={mean_auc:.4f} ± {std_auc:.4f}: marginal signal. 0.50 < AUC < 0.55 — minor systematics leakage but below leak threshold."

results = {
    "wave": "14-QQ",
    "issue": "P4-OA-M1 deep systematics regression on cached chirality_v2 logits",
    "n_total_joined": int(len(df)),
    "n_spirals_used": int(len(df_sp)),
    "n_features": int(X.shape[1]),
    "feature_numeric_cols": feat_cols,
    "feature_type_categories": type_cats,
    "n_folds": N_FOLDS,
    "n_epochs_per_fold": N_EPOCHS,
    "batch_size": BATCH,
    "learning_rate": LR,
    "hidden_layers": list(HIDDEN),
    "seed": SEED,
    "label_mapping": {"CW": 0, "CCW": 1},
    "fold_results": fold_results,
    "auc_mean": mean_auc,
    "auc_std": std_auc,
    "auc_5fold_min": float(aucs.min()),
    "auc_5fold_max": float(aucs.max()),
    "verdict": verdict,
    "interpretation": interp,
    "wallclock_s": time.time() - t0,
    "device": device,
    "gpu_name": (torch.cuda.get_device_name(0) if device == "cuda" else None),
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime()),
}

out_path = os.path.join(OUT, "results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, default=float)
print(f"\n[wave14qq] DONE. wall={results['wallclock_s']:.1f}s")
print(f"[wave14qq] mean AUC = {mean_auc:.5f} ± {std_auc:.5f}")
print(f"[wave14qq] verdict: {verdict}")
print(f"[wave14qq] {interp}")
print(f"[wave14qq] wrote {out_path}")
