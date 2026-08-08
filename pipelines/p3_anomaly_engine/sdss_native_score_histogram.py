"""SDSS DR18 native-retrained anomaly-score histogram (reviewer Grok M2).
Committed reproducible artifact from the released per-object catalog."""
import pandas as pd, numpy as np, json, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from pathlib import Path
D = Path(__file__).parent
df = pd.read_parquet(D/"hf_staging/sdss_dr18_pathc_native.parquet")
s = df["anomaly_score"].to_numpy()
pcts = {p: float(np.percentile(s, p)) for p in [50,90,95,99,99.9]}
summary = {
  "source":"sdss_dr18_pathc_native.parquet (77,905 SDSS DR18 native-retrained rescores)",
  "n":int(len(s)), "mean":float(s.mean()), "std":float(s.std()),
  "min":float(s.min()), "max":float(s.max()), "percentiles":pcts,
  "n_above_99th":int((s>=pcts[99]).sum()),
}
(D/"outputs").mkdir(exist_ok=True)
json.dump(summary, open(D/"outputs/sdss_native_score_histogram.json","w"), indent=2)
fig,ax=plt.subplots(figsize=(6,4))
ax.hist(s, bins=80, color="#2f6f4e", alpha=0.85, log=True)
ax.axvline(pcts[99], color="#b4462b", ls="--", lw=1, label=f"99th pct = {pcts[99]:.3f}")
ax.set_xlabel("BigAE native anomaly score"); ax.set_ylabel("count (log)")
ax.set_title("SDSS DR18 native-retrained anomaly-score distribution (N=77,905)")
ax.legend(fontsize=8); fig.tight_layout()
fig.savefig(D/"outputs/sdss_native_score_histogram.png", dpi=130)
print(json.dumps(summary, indent=2))
