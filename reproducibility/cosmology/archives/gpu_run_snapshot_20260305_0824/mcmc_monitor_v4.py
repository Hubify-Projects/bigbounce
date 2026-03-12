#!/usr/bin/env python3
"""
BigBounce MCMC Monitor v4 — read-only, no process modification.

Same as v3 plus:
  - Appends each run to convergence_history.csv (cumulative log)
  - Computes trend: rolling slope of Rhat_minus_1 over last 6h
  - Estimates hours-to-0.01 via linear extrapolation
  - Flags PLATEAU RISK if <5% improvement over 12h
  - Outputs trend_monitor_latest.txt

All existing v3 outputs preserved:
  status_latest.txt, convergence_latest.csv, chain_means_latest.csv,
  freeze_check.txt, trace_*.png
"""
import numpy as np
import glob, os, csv, time
from datetime import datetime, timedelta

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── config ───────────────────────────────────────────────────────────────
CHAINS_DIR   = "/workspace/bigbounce/reproducibility/chains"
OUT_DIR      = "/workspace/bigbounce/reproducibility/cosmology"
DATASETS     = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]
CORE         = ["H0", "delta_neff", "omegam", "ombh2", "ns", "tau", "sigma8"]
TRACE_PARAMS = ["H0", "delta_neff"]
TARGET       = 0.01
HISTORY_FILE = os.path.join(OUT_DIR, "convergence_history.csv")

os.makedirs(OUT_DIR, exist_ok=True)
now = datetime.utcnow()
ts  = now.strftime("%Y-%m-%d %H:%M:%S UTC")
now_epoch = time.time()

# ── helpers ──────────────────────────────────────────────────────────────

def colmap_from_header(path):
    with open(path) as f:
        hdr = f.readline()
    return {n: i for i, n in enumerate(hdr.strip().lstrip("#").split())}

def load_chain(path):
    cm = colmap_from_header(path)
    try:
        d = np.loadtxt(path)
        if d.ndim == 2 and d.shape[0] >= 3:
            return d, cm
    except:
        pass
    return None, None

def autocorr_tau(x):
    n = len(x)
    if n < 20:
        return float(n), 1.0
    xc = x - np.mean(x)
    f = np.fft.fft(xc, n=2 * n)
    acf = np.fft.ifft(f * np.conjugate(f))[:n].real
    if acf[0] == 0:
        return float(n), 1.0
    acf /= acf[0]
    tau_int = 1.0
    for k in range(1, n // 2):
        rho_pair = acf[2 * k - 1] + acf[2 * k]
        if rho_pair < 0:
            break
        tau_int += 2.0 * rho_pair
    tau_int = max(tau_int, 1.0)
    return tau_int, n / tau_int

def gelman_rubin(chain_arrays):
    m = len(chain_arrays)
    if m < 2:
        return float("nan")
    min_n = min(len(c) for c in chain_arrays)
    if min_n < 10:
        return float("nan")
    chains = [c[:min_n] for c in chain_arrays]
    n = min_n
    chain_means = np.array([np.mean(c) for c in chains])
    chain_vars  = np.array([np.var(c, ddof=1) for c in chains])
    grand_mean  = np.mean(chain_means)
    B = n / (m - 1.0) * np.sum((chain_means - grand_mean) ** 2)
    W = np.mean(chain_vars)
    if W == 0:
        return float("nan")
    var_hat = ((n - 1.0) / n) * W + (1.0 / n) * B
    return max(np.sqrt(var_hat / W), 1.0)

def weighted_mean(v, w):
    wn = w / w.sum()
    return np.average(v, weights=wn)

def weighted_std(v, w):
    mu = weighted_mean(v, w)
    wn = w / w.sum()
    return np.sqrt(np.average((v - mu) ** 2, weights=wn))

def drift(vals, weights, frac_recent, frac_older):
    n = len(vals)
    n_r = max(int(n * frac_recent), 2)
    n_o = max(int(n * frac_older), 2)
    v_r, w_r = vals[-n_r:], weights[-n_r:]
    v_o, w_o = vals[-n_o:], weights[-n_o:]
    mu_r = weighted_mean(v_r, w_r)
    mu_o = weighted_mean(v_o, w_o)
    sig = max(weighted_std(v_r, w_r), weighted_std(v_o, w_o), 1e-30)
    return (mu_r - mu_o) / sig

def chain_cohort(path):
    dirname = os.path.basename(os.path.dirname(path))
    return "parallel" if "_chain" in dirname else "original"

def compute_param_stats(chain_list, subset_filter=None):
    result = {}
    for pname in CORE:
        arrs = []
        for data, cm, label, cohort in chain_list:
            if subset_filter and cohort != subset_filter:
                continue
            if pname in cm and cm[pname] < data.shape[1]:
                arrs.append(data[:, cm[pname]])
        if len(arrs) < 2:
            result[pname] = {"Rhat": float("nan"), "Rhat_minus_1": float("nan"),
                             "ESS": float("nan"), "tau_int": float("nan")}
            continue
        rhat = gelman_rubin(arrs)
        total_ess = 0.0
        total_tau = 0.0
        for a in arrs:
            ti, ei = autocorr_tau(a)
            total_ess += ei
            total_tau += ti
        result[pname] = {"Rhat": rhat, "Rhat_minus_1": rhat - 1.0,
                         "ESS": total_ess, "tau_int": total_tau / len(arrs)}
    return result

# ── load history ─────────────────────────────────────────────────────────

def load_history():
    """Load convergence_history.csv → list of dicts."""
    rows = []
    if not os.path.exists(HISTORY_FILE):
        return rows
    with open(HISTORY_FILE, "r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                r["epoch"] = float(r["epoch"])
                r["Rhat_minus_1"] = float(r["Rhat_minus_1"])
                r["ESS"] = float(r["ESS"])
                r["raw_rows"] = int(r["raw_rows"])
                rows.append(r)
            except:
                pass
    return rows

def append_history(current_data):
    """Append current run's data to history file."""
    exists = os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["epoch", "timestamp", "dataset", "param",
                                           "Rhat_minus_1", "ESS", "raw_rows"])
        if not exists:
            w.writeheader()
        w.writerows(current_data)

# ── main ─────────────────────────────────────────────────────────────────

txt = []
def out(s=""):
    print(s)
    txt.append(s)

conv_rows   = []
means_rows  = []
freeze_lines = []
history_new = []  # rows to append to history

out("=" * 120)
out(f"BigBounce MCMC Status — {ts}")
out("=" * 120)
out(f"Method: Gelman-Rubin Rhat (BDA3 §11.4), autocorrelation ESS (Geyer IPS)")
out(f"Naming: Rhat ≥ 1.0 ; Rhat_minus_1 = Rhat - 1 ≥ 0.0 ; target Rhat_minus_1 < {TARGET}")
out(f"Cohorts: A = new cohort (parallel chains, <24h) ; B = all chains combined")

freeze_lines.append(f"BigBounce MCMC Freeze Check — {ts}")
freeze_lines.append(f"Criteria: Rhat_minus_1 < {TARGET} (all core params), Drift20/40 < 0.2σ (H0, ΔNeff), ESS report")
freeze_lines.append("=" * 100)

all_stats = {}  # dataset -> stats_all

for ds in DATASETS:
    paths = []
    orig = f"{CHAINS_DIR}/{ds}/spin_torsion.1.txt"
    if os.path.exists(orig):
        paths.append(orig)
    for p in sorted(glob.glob(f"{CHAINS_DIR}/{ds}_chain*/spin_torsion.1.txt")):
        paths.append(p)

    chain_list = []
    for p in paths:
        data, cm = load_chain(p)
        if data is not None:
            chain_list.append((data, cm, os.path.basename(os.path.dirname(p)), chain_cohort(p)))

    if not chain_list:
        out(f"\n  {ds}: NO DATA\n")
        continue

    n_orig = sum(1 for _, _, _, c in chain_list if c == "original")
    n_par  = sum(1 for _, _, _, c in chain_list if c == "parallel")
    total_raw = sum(d.shape[0] for d, _, _, _ in chain_list)

    out("")
    out("=" * 120)
    out(f"  {ds.upper().replace('_',' ')}   |   chains: {len(chain_list)} (orig {n_orig}, new_cohort {n_par})   |   raw rows: {total_raw}")
    out("=" * 120)

    stats_all = compute_param_stats(chain_list, subset_filter=None)
    stats_new = compute_param_stats(chain_list, subset_filter="parallel")
    all_stats[ds] = stats_all

    # record history
    for pname in CORE:
        s = stats_all[pname]
        if not np.isnan(s["Rhat_minus_1"]):
            history_new.append({
                "epoch": now_epoch, "timestamp": ts, "dataset": ds, "param": pname,
                "Rhat_minus_1": s["Rhat_minus_1"], "ESS": s["ESS"], "raw_rows": total_raw,
            })

    # [A] new cohort table
    out(f"\n  [A] NEW COHORT ({n_par} parallel chains)")
    out(f"  {'Param':>12s}  {'Rhat':>8s}  {'Rhat_m1':>9s}  {'ESS':>8s}  {'tau_int':>8s}  {'Status':>10s}")
    out(f"  {'-'*12}  {'-'*8}  {'-'*9}  {'-'*8}  {'-'*8}  {'-'*10}")
    for pname in CORE:
        s = stats_new[pname]
        if np.isnan(s["Rhat"]):
            out(f"  {pname:>12s}  {'N/A':>8s}  {'N/A':>9s}  {'N/A':>8s}  {'N/A':>8s}  {'N/A':>10s}")
        else:
            rm1 = s["Rhat_minus_1"]
            status = "CONVERGED" if rm1 < 0.01 else ("CLOSE" if rm1 < 0.05 else ("MIXING" if rm1 < 0.20 else "RUNNING"))
            out(f"  {pname:>12s}  {s['Rhat']:8.5f}  {rm1:9.5f}  {s['ESS']:8.1f}  {s['tau_int']:8.1f}  {status:>10s}")

    # [B] all chains table
    out(f"\n  [B] ALL CHAINS COMBINED ({len(chain_list)} chains)")
    out(f"  {'Param':>12s}  {'Rhat':>8s}  {'Rhat_m1':>9s}  {'ESS':>8s}  {'tau_int':>8s}  {'Status':>10s}")
    out(f"  {'-'*12}  {'-'*8}  {'-'*9}  {'-'*8}  {'-'*8}  {'-'*10}")
    for pname in CORE:
        s = stats_all[pname]
        if np.isnan(s["Rhat"]):
            out(f"  {pname:>12s}  {'N/A':>8s}")
        else:
            rm1 = s["Rhat_minus_1"]
            status = "CONVERGED" if rm1 < 0.01 else ("CLOSE" if rm1 < 0.05 else ("MIXING" if rm1 < 0.20 else "RUNNING"))
            out(f"  {pname:>12s}  {s['Rhat']:8.5f}  {rm1:9.5f}  {s['ESS']:8.1f}  {s['tau_int']:8.1f}  {status:>10s}")

        conv_rows.append({
            "dataset": ds, "param": pname,
            "Rhat_all": f"{stats_all[pname]['Rhat']:.6f}" if not np.isnan(stats_all[pname]['Rhat']) else "",
            "Rhat_minus_1_all": f"{stats_all[pname]['Rhat_minus_1']:.6f}" if not np.isnan(stats_all[pname]['Rhat_minus_1']) else "",
            "Rhat_new": f"{stats_new[pname]['Rhat']:.6f}" if not np.isnan(stats_new[pname]['Rhat']) else "",
            "Rhat_minus_1_new": f"{stats_new[pname]['Rhat_minus_1']:.6f}" if not np.isnan(stats_new[pname]['Rhat_minus_1']) else "",
            "ESS_all": f"{stats_all[pname]['ESS']:.1f}" if not np.isnan(stats_all[pname]['ESS']) else "",
            "ESS_new": f"{stats_new[pname]['ESS']:.1f}" if not np.isnan(stats_new[pname]['ESS']) else "",
            "tau_int_all": f"{stats_all[pname]['tau_int']:.2f}" if not np.isnan(stats_all[pname]['tau_int']) else "",
        })

    # physics one-liner
    all_dn, all_dn_w, all_h0, all_h0_w = [], [], [], []
    for data, cm, _, _ in chain_list:
        if "delta_neff" in cm:
            all_dn.append(data[:, cm["delta_neff"]]); all_dn_w.append(data[:, cm["weight"]])
        if "H0" in cm:
            all_h0.append(data[:, cm["H0"]]); all_h0_w.append(data[:, cm["weight"]])
    if all_dn and all_h0:
        v_dn = np.concatenate(all_dn); w_dn = np.concatenate(all_dn_w)
        v_h0 = np.concatenate(all_h0); w_h0 = np.concatenate(all_h0_w)
        mu_dn, sig_dn = weighted_mean(v_dn, w_dn), weighted_std(v_dn, w_dn)
        mu_h0, sig_h0 = weighted_mean(v_h0, w_h0), weighted_std(v_h0, w_h0)
        ppos = np.sum((w_dn / w_dn.sum())[v_dn > 0]) * 100
        shoes = abs(mu_h0 - 73.04) / np.sqrt(sig_h0**2 + 1.04**2)
        sig_str = f"{mu_dn/sig_dn:.2f}σ" if sig_dn > 0 else "N/A"
        out(f"\n  Physics:  ΔNeff = {mu_dn:.4f} ± {sig_dn:.4f} ({sig_str}, P>0={ppos:.1f}%)   "
            f"H₀ = {mu_h0:.2f} ± {sig_h0:.2f}   SH0ES Δ = {shoes:.2f}σ")

    # per-chain means
    out("")
    out(f"  {'Chain':<30s} {'Cohort':<10s} {'Rows':>5s}  {'H0':>10s}  {'ΔNeff':>10s}  {'tau':>10s}")
    out(f"  {'-'*30} {'-'*10} {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}")
    for data, cm, label, cohort in chain_list:
        n = data.shape[0]
        w = data[:, cm["weight"]]; wn = w / w.sum()
        row = {"dataset": ds, "chain": label, "cohort": cohort, "rows": n}
        for pn in ["H0", "delta_neff", "tau"]:
            row[pn] = np.average(data[:, cm[pn]], weights=wn) if pn in cm and cm[pn] < data.shape[1] else float("nan")
        out(f"  {label:<30s} {cohort:<10s} {n:5d}  "
            f"{row['H0']:10.4f}  {row['delta_neff']:10.6f}  {row['tau']:10.6f}")
        means_rows.append(row)

    # trace plots
    for pname in TRACE_PARAMS:
        fig, ax = plt.subplots(figsize=(14, 5))
        for data, cm, label, cohort in chain_list:
            if pname not in cm or cm[pname] >= data.shape[1]:
                continue
            vals = data[:, cm[pname]]
            style = "-" if cohort == "original" else "--"
            alpha = 1.0 if cohort == "original" else 0.7
            ax.plot(np.arange(len(vals)), vals, style, alpha=alpha, linewidth=0.8, label=f"{label} ({cohort})")
        ax.set_xlabel("Step")
        ax.set_ylabel(pname)
        ax.set_title(f"{ds} — {pname} trace   [{ts}]")
        ax.legend(fontsize=7, ncol=2, loc="upper right")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"trace_{ds}_{pname}.png"), dpi=150)
        plt.close(fig)

    # freeze check
    freeze_lines.append("")
    freeze_lines.append(f"--- {ds.upper().replace('_',' ')} ---")

    rhat_pass = True
    worst_param, worst_rm1 = "", 0.0
    for pname in CORE:
        rm1 = stats_all[pname]["Rhat_minus_1"]
        if np.isnan(rm1) or rm1 >= TARGET:
            rhat_pass = False
            if not np.isnan(rm1) and rm1 > worst_rm1:
                worst_rm1 = rm1; worst_param = pname
    freeze_lines.append(f"  Rhat_minus_1 < {TARGET} (all core):  {'PASS' if rhat_pass else 'FAIL'}  "
                        + (f"(worst: {worst_param} = {worst_rm1:.5f})" if not rhat_pass else ""))

    drift_pass = True
    drift_details = []
    for pname in ["H0", "delta_neff"]:
        all_v, all_w = [], []
        for data, cm, _, _ in chain_list:
            if pname in cm and cm[pname] < data.shape[1]:
                all_v.append(data[:, cm[pname]]); all_w.append(data[:, cm["weight"]])
        if all_v:
            v = np.concatenate(all_v); w = np.concatenate(all_w)
            d = drift(v, w, 0.20, 0.40)
            pf = "PASS" if abs(d) < 0.2 else "FAIL"
            if abs(d) >= 0.2: drift_pass = False
            drift_details.append(f"{pname}={d:+.4f}σ [{pf}]")
    freeze_lines.append(f"  Drift20/40 < 0.2σ (H0, ΔNeff):  {'PASS' if drift_pass else 'FAIL'}  ({', '.join(drift_details)})")

    ess_h0 = stats_all.get("H0", {}).get("ESS", float("nan"))
    ess_dn = stats_all.get("delta_neff", {}).get("ESS", float("nan"))
    freeze_lines.append(f"  ESS(H0) = {ess_h0:.1f}   ESS(ΔNeff) = {ess_dn:.1f}")
    freeze_lines.append(f"  >> OVERALL: {'PASS' if (rhat_pass and drift_pass) else 'FAIL'}")

# ── cross-dataset summary ────────────────────────────────────────────────
out("")
out("=" * 120)
out("CROSS-DATASET SUMMARY (all chains combined)")
out("=" * 120)
hdr = (f"  {'Dataset':<18s}  {'Chains':>6s}  {'Raw':>6s}  "
       f"{'Rhat_m1(H0)':>12s}  {'Rhat_m1(ΔN)':>12s}  {'Rhat_m1(τ)':>11s}  "
       f"{'ESS(H0)':>8s}  {'ESS(ΔN)':>8s}  {'max Rhat_m1':>12s}")
out(hdr)
out(f"  {'-'*18}  {'-'*6}  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*11}  {'-'*8}  {'-'*8}  {'-'*12}")

for ds in DATASETS:
    ds_conv = [r for r in conv_rows if r["dataset"] == ds and r["Rhat_all"]]
    if not ds_conv:
        continue
    n_ch = len([r for r in means_rows if r["dataset"] == ds])
    n_raw = sum(r["rows"] for r in means_rows if r["dataset"] == ds)
    def get_v(p, field):
        for r in ds_conv:
            if r["param"] == p and r[field]:
                return float(r[field])
        return float("nan")
    rm1_h0  = get_v("H0", "Rhat_minus_1_all")
    rm1_dn  = get_v("delta_neff", "Rhat_minus_1_all")
    rm1_tau = get_v("tau", "Rhat_minus_1_all")
    ess_h0  = get_v("H0", "ESS_all")
    ess_dn  = get_v("delta_neff", "ESS_all")
    max_rm1 = max(float(r["Rhat_minus_1_all"]) for r in ds_conv if r["Rhat_minus_1_all"])
    label = ds.replace("_", " ").title()
    out(f"  {label:<18s}  {n_ch:6d}  {n_raw:6d}  "
        f"{rm1_h0:12.5f}  {rm1_dn:12.5f}  {rm1_tau:11.5f}  "
        f"{ess_h0:8.1f}  {ess_dn:8.1f}  {max_rm1:12.5f}")

out(f"\nTarget: Rhat_minus_1 < {TARGET} for ALL core params")

# ── append history ───────────────────────────────────────────────────────
append_history(history_new)

# ── trend analysis ───────────────────────────────────────────────────────
history = load_history()

trend_lines = []
trend_lines.append(f"BigBounce MCMC Trend Monitor — {ts}")
trend_lines.append(f"Method: linear extrapolation of Rhat_minus_1 toward {TARGET}")
trend_lines.append(f"Plateau flag: <5% improvement over 12h window")
trend_lines.append("=" * 120)

for ds in DATASETS:
    trend_lines.append("")
    trend_lines.append(f"--- {ds.upper().replace('_',' ')} ---")
    trend_lines.append(f"  {'Param':>12s}  {'Current':>10s}  {'6h ago':>10s}  {'Δ(6h)':>10s}  "
                       f"{'12h ago':>10s}  {'Δ(12h)':>10s}  {'%impr 12h':>10s}  {'ETA (hrs)':>10s}  {'Flag':>14s}")
    trend_lines.append(f"  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*10}  "
                       f"{'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*14}")

    for pname in CORE:
        # current value
        if ds not in all_stats or pname not in all_stats[ds]:
            continue
        current = all_stats[ds][pname]["Rhat_minus_1"]
        if np.isnan(current):
            trend_lines.append(f"  {pname:>12s}  {'N/A':>10s}")
            continue

        # find closest history point ~6h ago and ~12h ago
        ds_param_hist = [h for h in history if h["dataset"] == ds and h["param"] == pname]
        ds_param_hist.sort(key=lambda x: x["epoch"])

        def find_nearest(target_epoch):
            best = None
            best_dist = float("inf")
            for h in ds_param_hist:
                dist = abs(h["epoch"] - target_epoch)
                if dist < best_dist:
                    best_dist = dist
                    best = h
            return best, best_dist

        val_6h_ago = None
        val_12h_ago = None
        pt_6h, dist_6h = find_nearest(now_epoch - 6 * 3600)
        pt_12h, dist_12h = find_nearest(now_epoch - 12 * 3600)

        # only use if within 2h of target window
        if pt_6h and dist_6h < 2 * 3600:
            val_6h_ago = pt_6h["Rhat_minus_1"]
        if pt_12h and dist_12h < 2 * 3600:
            val_12h_ago = pt_12h["Rhat_minus_1"]

        # compute deltas
        delta_6h = (current - val_6h_ago) if val_6h_ago is not None else None
        delta_12h = (current - val_12h_ago) if val_12h_ago is not None else None

        # % improvement over 12h
        pct_impr_12h = None
        if val_12h_ago is not None and val_12h_ago > 0:
            pct_impr_12h = (val_12h_ago - current) / val_12h_ago * 100

        # ETA via linear extrapolation from 6h slope
        eta_hrs = None
        if delta_6h is not None and delta_6h < 0:
            # slope = delta_6h / 6 hours; need to go from current to TARGET
            slope_per_hr = delta_6h / 6.0
            remaining = current - TARGET
            if remaining > 0 and slope_per_hr < 0:
                eta_hrs = remaining / abs(slope_per_hr)

        # plateau flag
        flag = ""
        if pct_impr_12h is not None and pct_impr_12h < 5:
            flag = "PLATEAU RISK"
        elif pct_impr_12h is not None and pct_impr_12h < 0:
            flag = "WORSENING"

        # format
        cur_s   = f"{current:.5f}"
        v6_s    = f"{val_6h_ago:.5f}" if val_6h_ago is not None else "no data"
        d6_s    = f"{delta_6h:+.5f}" if delta_6h is not None else "—"
        v12_s   = f"{val_12h_ago:.5f}" if val_12h_ago is not None else "no data"
        d12_s   = f"{delta_12h:+.5f}" if delta_12h is not None else "—"
        pct_s   = f"{pct_impr_12h:+.1f}%" if pct_impr_12h is not None else "—"
        eta_s   = f"{eta_hrs:.1f}" if eta_hrs is not None else ("∞" if delta_6h is not None and delta_6h >= 0 else "—")

        trend_lines.append(f"  {pname:>12s}  {cur_s:>10s}  {v6_s:>10s}  {d6_s:>10s}  "
                           f"{v12_s:>10s}  {d12_s:>10s}  {pct_s:>10s}  {eta_s:>10s}  {flag:>14s}")

# ── write all files ──────────────────────────────────────────────────────

with open(os.path.join(OUT_DIR, "status_latest.txt"), "w") as f:
    f.write("\n".join(txt) + "\n")

with open(os.path.join(OUT_DIR, "convergence_latest.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=[
        "dataset", "param", "Rhat_all", "Rhat_minus_1_all",
        "Rhat_new", "Rhat_minus_1_new", "ESS_all", "ESS_new", "tau_int_all"])
    w.writeheader()
    w.writerows(conv_rows)

with open(os.path.join(OUT_DIR, "chain_means_latest.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["dataset", "chain", "cohort", "rows", "H0", "delta_neff", "tau"])
    for r in means_rows:
        w.writerow([r["dataset"], r["chain"], r["cohort"], r["rows"],
                     f"{r['H0']:.6f}" if not np.isnan(r['H0']) else "",
                     f"{r['delta_neff']:.6f}" if not np.isnan(r['delta_neff']) else "",
                     f"{r['tau']:.6f}" if not np.isnan(r['tau']) else ""])

with open(os.path.join(OUT_DIR, "freeze_check.txt"), "w") as f:
    f.write("\n".join(freeze_lines) + "\n")

with open(os.path.join(OUT_DIR, "trend_monitor_latest.txt"), "w") as f:
    f.write("\n".join(trend_lines) + "\n")

out("")
out("Saved: status_latest.txt, convergence_latest.csv, chain_means_latest.csv,")
out("       freeze_check.txt, trend_monitor_latest.txt, trace_*.png")

# print trend + freeze to terminal
print("\n" + "=" * 120)
print("FREEZE CHECK")
print("=" * 120)
for line in freeze_lines:
    print(line)

print("\n" + "=" * 120)
print("TREND MONITOR")
print("=" * 120)
for line in trend_lines:
    print(line)
