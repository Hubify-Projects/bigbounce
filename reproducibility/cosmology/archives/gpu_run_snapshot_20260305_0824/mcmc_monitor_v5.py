#!/usr/bin/env python3
"""
BigBounce MCMC Monitor v5 — read-only, no process modification.

Two convergence modes per dataset:
  A) cohort_new:  only chains started within the last 24 hours
  B) all_chains:  every chain combined

Each mode reports:
  - Rhat_m1 for core params: H0, delta_neff, omegam, ombh2, ns, tau, sigma8
  - ESS per param (autocorrelation-based, Geyer IPS)
  - Drift20/40 for H0 and delta_neff

Freeze check criteria:
  - PASS if Rhat_m1 < 0.01 for {H0, delta_neff, omegam, ombh2, ns, sigma8}
  - PASS if Rhat_m1 < 0.02 for tau  (relaxed)
  - PASS if drift < 0.2σ for H0 and delta_neff

Outputs:
  status_latest.txt           — full report (both modes)
  status_cohort_new.txt       — cohort_new mode only
  convergence_latest.csv      — machine-readable stats
  chain_means_latest.csv      — per-chain means
  freeze_check.txt            — PASS/FAIL evaluation
  convergence_history.csv     — cumulative append-only trend log
  trend_monitor_latest.txt    — trend extrapolation + plateau detection
  trace_*.png                 — overlay trace plots
"""
import numpy as np
import glob, os, csv, time
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── config ───────────────────────────────────────────────────────────────
CHAINS_DIR   = "/workspace/bigbounce/reproducibility/chains"
OUT_DIR      = "/workspace/bigbounce/reproducibility/cosmology"
DATASETS     = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]
CORE         = ["H0", "delta_neff", "omegam", "ombh2", "ns", "tau", "sigma8"]
TRACE_PARAMS = ["H0", "delta_neff"]
TARGET       = 0.01          # Rhat_m1 target for most params
TARGET_TAU   = 0.02          # relaxed target for tau
DRIFT_THRESH = 0.2           # sigma units
COHORT_WINDOW_H = 24         # hours — chains started within this window are "new"
HISTORY_FILE = os.path.join(OUT_DIR, "convergence_history.csv")

os.makedirs(OUT_DIR, exist_ok=True)
now       = datetime.utcnow()
ts        = now.strftime("%Y-%m-%d %H:%M:%S UTC")
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
    except Exception:
        pass
    return None, None

def chain_start_epoch(chain_dir):
    """Estimate when this chain was started.
    Uses .input.yaml (written once at chain start) if available,
    else falls back to directory ctime."""
    input_yaml = os.path.join(chain_dir, "spin_torsion.input.yaml")
    if os.path.exists(input_yaml):
        return os.path.getmtime(input_yaml)
    # fallback: earliest regular file ctime in directory
    try:
        return os.stat(chain_dir).st_ctime
    except Exception:
        return 0.0

def autocorr_tau(x):
    """Integrated autocorrelation time + ESS via Geyer IPS."""
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
    """Standard Gelman-Rubin R-hat (BDA3 §11.4). Returns R-hat >= 1."""
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

def drift_2040(vals, weights):
    """Drift between last-20% mean and last-40% mean, in sigma units."""
    n = len(vals)
    n_r = max(int(n * 0.20), 2)
    n_o = max(int(n * 0.40), 2)
    v_r, w_r = vals[-n_r:], weights[-n_r:]
    v_o, w_o = vals[-n_o:], weights[-n_o:]
    mu_r = weighted_mean(v_r, w_r)
    mu_o = weighted_mean(v_o, w_o)
    sig = max(weighted_std(v_r, w_r), weighted_std(v_o, w_o), 1e-30)
    return (mu_r - mu_o) / sig

# ── chain loading + cohort assignment ─────────────────────────────────────

def load_dataset_chains(ds):
    """Return list of (data, colmap, label, cohort, start_epoch) tuples."""
    paths = []
    orig = f"{CHAINS_DIR}/{ds}/spin_torsion.1.txt"
    if os.path.exists(orig):
        paths.append(orig)
    for p in sorted(glob.glob(f"{CHAINS_DIR}/{ds}_chain*/spin_torsion.1.txt")):
        paths.append(p)

    chain_list = []
    for p in paths:
        data, cm = load_chain(p)
        if data is None:
            continue
        chain_dir = os.path.dirname(p)
        label = os.path.basename(chain_dir)
        start_ep = chain_start_epoch(chain_dir)
        age_hrs = (now_epoch - start_ep) / 3600.0
        cohort = "new" if age_hrs <= COHORT_WINDOW_H else "old"
        chain_list.append((data, cm, label, cohort, start_ep))
    return chain_list

# ── stats computation ─────────────────────────────────────────────────────

def compute_stats(chain_list, cohort_filter=None):
    """Compute Rhat, ESS, drift for a chain subset.
    Returns dict[param] -> {Rhat, Rhat_m1, ESS, tau_int, drift}"""
    result = {}
    subset = chain_list if cohort_filter is None else [
        c for c in chain_list if c[3] == cohort_filter]

    for pname in CORE:
        arrs = []
        all_v, all_w = [], []
        for data, cm, label, cohort, _ in subset:
            if pname in cm and cm[pname] < data.shape[1]:
                arrs.append(data[:, cm[pname]])
                all_v.append(data[:, cm[pname]])
                all_w.append(data[:, cm["weight"]])

        if len(arrs) < 2:
            result[pname] = {
                "Rhat": float("nan"), "Rhat_m1": float("nan"),
                "ESS": float("nan"), "tau_int": float("nan"),
                "drift": float("nan"),
            }
            continue

        rhat = gelman_rubin(arrs)
        total_ess = 0.0
        total_tau = 0.0
        for a in arrs:
            ti, ei = autocorr_tau(a)
            total_ess += ei
            total_tau += ti

        # drift for H0, delta_neff only
        d = float("nan")
        if pname in ("H0", "delta_neff") and all_v:
            v = np.concatenate(all_v)
            w = np.concatenate(all_w)
            d = drift_2040(v, w)

        result[pname] = {
            "Rhat": rhat, "Rhat_m1": rhat - 1.0,
            "ESS": total_ess, "tau_int": total_tau / len(arrs),
            "drift": d,
        }
    return result

# ── history ────────────────────────────────────────────────────────────────

def load_history():
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
            except Exception:
                pass
    return rows

def append_history(rows):
    exists = os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "epoch", "timestamp", "dataset", "param",
            "Rhat_minus_1", "ESS", "raw_rows"])
        if not exists:
            w.writeheader()
        w.writerows(rows)

# ── format helpers ─────────────────────────────────────────────────────────

def status_label(rm1, is_tau=False):
    tgt = TARGET_TAU if is_tau else TARGET
    if np.isnan(rm1):
        return "N/A"
    if rm1 < tgt:
        return "CONVERGED"
    if rm1 < 0.05:
        return "CLOSE"
    if rm1 < 0.20:
        return "MIXING"
    return "RUNNING"

def fmt_stats_table(stats, label_prefix=""):
    """Return list of formatted lines for a stats table."""
    lines = []
    hdr = (f"  {'Param':>12s}  {'Rhat':>8s}  {'Rhat_m1':>9s}  {'ESS':>8s}  "
           f"{'tau_int':>8s}  {'Status':>10s}  {'Drift20/40':>11s}")
    lines.append(hdr)
    lines.append(f"  {'-'*12}  {'-'*8}  {'-'*9}  {'-'*8}  {'-'*8}  {'-'*10}  {'-'*11}")
    for pname in CORE:
        s = stats[pname]
        if np.isnan(s["Rhat"]):
            lines.append(f"  {pname:>12s}  {'N/A':>8s}  {'N/A':>9s}  {'N/A':>8s}  "
                         f"{'N/A':>8s}  {'N/A':>10s}  {'':>11s}")
            continue
        is_tau = (pname == "tau")
        st = status_label(s["Rhat_m1"], is_tau)
        drift_s = ""
        if pname in ("H0", "delta_neff") and not np.isnan(s["drift"]):
            pf = "ok" if abs(s["drift"]) < DRIFT_THRESH else "DRIFT"
            drift_s = f"{s['drift']:+.3f}σ {pf}"
        lines.append(
            f"  {pname:>12s}  {s['Rhat']:8.5f}  {s['Rhat_m1']:9.5f}  "
            f"{s['ESS']:8.1f}  {s['tau_int']:8.1f}  {st:>10s}  {drift_s:>11s}")
    return lines

def physics_oneliner(chain_list, cohort_filter=None):
    subset = chain_list if cohort_filter is None else [
        c for c in chain_list if c[3] == cohort_filter]
    all_dn, all_dn_w, all_h0, all_h0_w = [], [], [], []
    for data, cm, _, _, _ in subset:
        if "delta_neff" in cm:
            all_dn.append(data[:, cm["delta_neff"]])
            all_dn_w.append(data[:, cm["weight"]])
        if "H0" in cm:
            all_h0.append(data[:, cm["H0"]])
            all_h0_w.append(data[:, cm["weight"]])
    if not all_dn or not all_h0:
        return ""
    v_dn = np.concatenate(all_dn); w_dn = np.concatenate(all_dn_w)
    v_h0 = np.concatenate(all_h0); w_h0 = np.concatenate(all_h0_w)
    mu_dn, sig_dn = weighted_mean(v_dn, w_dn), weighted_std(v_dn, w_dn)
    mu_h0, sig_h0 = weighted_mean(v_h0, w_h0), weighted_std(v_h0, w_h0)
    ppos = np.sum((w_dn / w_dn.sum())[v_dn > 0]) * 100
    shoes = abs(mu_h0 - 73.04) / np.sqrt(sig_h0**2 + 1.04**2)
    sig_str = f"{mu_dn/sig_dn:.2f}σ" if sig_dn > 0 else "N/A"
    return (f"  ΔNeff = {mu_dn:.4f} ± {sig_dn:.4f} ({sig_str}, P>0={ppos:.1f}%)   "
            f"H₀ = {mu_h0:.2f} ± {sig_h0:.2f}   SH0ES Δ = {shoes:.2f}σ")

# ── freeze check evaluation ───────────────────────────────────────────────

def evaluate_freeze(ds_label, stats_all, stats_new):
    """Return list of text lines for freeze check."""
    lines = []
    lines.append("")
    lines.append(f"--- {ds_label} ---")

    for mode_name, stats in [("all_chains", stats_all), ("cohort_new", stats_new)]:
        lines.append(f"  [{mode_name}]")

        # Rhat check
        rhat_pass = True
        worst_param, worst_rm1 = "", 0.0
        for pname in CORE:
            rm1 = stats[pname]["Rhat_m1"]
            tgt = TARGET_TAU if pname == "tau" else TARGET
            if np.isnan(rm1) or rm1 >= tgt:
                rhat_pass = False
                if not np.isnan(rm1) and rm1 > worst_rm1:
                    worst_rm1 = rm1
                    worst_param = pname
        tgt_str = f"Rhat_m1 < {TARGET} (H0..sigma8) + < {TARGET_TAU} (tau)"
        fail_detail = f"  (worst: {worst_param} = {worst_rm1:.5f})" if not rhat_pass else ""
        lines.append(f"    {tgt_str}: {'PASS' if rhat_pass else 'FAIL'}{fail_detail}")

        # Drift check
        drift_pass = True
        drift_details = []
        for pname in ["H0", "delta_neff"]:
            d = stats[pname]["drift"]
            if np.isnan(d):
                drift_details.append(f"{pname}=N/A")
                continue
            pf = "PASS" if abs(d) < DRIFT_THRESH else "FAIL"
            if abs(d) >= DRIFT_THRESH:
                drift_pass = False
            drift_details.append(f"{pname}={d:+.4f}σ [{pf}]")
        lines.append(f"    Drift20/40 < {DRIFT_THRESH}σ: {'PASS' if drift_pass else 'FAIL'}  ({', '.join(drift_details)})")

        # ESS summary
        ess_h0 = stats.get("H0", {}).get("ESS", float("nan"))
        ess_dn = stats.get("delta_neff", {}).get("ESS", float("nan"))
        lines.append(f"    ESS(H0) = {ess_h0:.1f}   ESS(ΔNeff) = {ess_dn:.1f}")

        overall = "PASS" if (rhat_pass and drift_pass) else "FAIL"
        lines.append(f"    >> {mode_name} OVERALL: {overall}")

    return lines

# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════

full_txt    = []   # status_latest.txt (both modes)
cohort_txt  = []   # status_cohort_new.txt (cohort_new only)
conv_rows   = []
means_rows  = []
freeze_lines = []
history_new  = []
all_stats_dict = {}   # dataset -> stats_all

def out_both(s=""):
    print(s)
    full_txt.append(s)

def out_cohort(s=""):
    cohort_txt.append(s)

# ── header ────────────────────────────────────────────────────────────────

banner = f"""\
{'='*120}
BigBounce MCMC Status — {ts}
{'='*120}
Method: Gelman-Rubin Rhat (BDA3 §11.4), autocorrelation ESS (Geyer IPS)
Naming: Rhat >= 1.0 ; Rhat_m1 = Rhat - 1 >= 0.0
Targets: Rhat_m1 < {TARGET} (H0, delta_neff, omegam, ombh2, ns, sigma8) ; Rhat_m1 < {TARGET_TAU} (tau)
Drift: last-20% vs last-40% mean, threshold < {DRIFT_THRESH}σ
Cohort window: chains started within last {COHORT_WINDOW_H}h are "new\""""

for line in banner.split("\n"):
    out_both(line)

cohort_banner = f"""\
{'='*120}
BigBounce MCMC — COHORT NEW ONLY — {ts}
{'='*120}
Only chains started within the last {COHORT_WINDOW_H} hours.
Targets: Rhat_m1 < {TARGET} (core) ; Rhat_m1 < {TARGET_TAU} (tau) ; Drift < {DRIFT_THRESH}σ"""

for line in cohort_banner.split("\n"):
    out_cohort(line)

freeze_lines.append(f"BigBounce MCMC Freeze Check — {ts}")
freeze_lines.append(f"Targets: Rhat_m1 < {TARGET} (H0..sigma8), < {TARGET_TAU} (tau), Drift < {DRIFT_THRESH}σ")
freeze_lines.append("=" * 100)

# ── per-dataset ───────────────────────────────────────────────────────────

for ds in DATASETS:
    chain_list = load_dataset_chains(ds)
    if not chain_list:
        out_both(f"\n  {ds}: NO DATA\n")
        continue

    n_new = sum(1 for *_, c, _ in chain_list if c == "new")
    n_old = sum(1 for *_, c, _ in chain_list if c == "old")
    total_raw = sum(d.shape[0] for d, *_ in chain_list)
    ds_label = ds.upper().replace("_", " ")

    # compute stats for both modes
    stats_all = compute_stats(chain_list, cohort_filter=None)
    stats_new = compute_stats(chain_list, cohort_filter="new")
    all_stats_dict[ds] = stats_all

    # record history (all_chains mode)
    for pname in CORE:
        s = stats_all[pname]
        if not np.isnan(s["Rhat_m1"]):
            history_new.append({
                "epoch": now_epoch, "timestamp": ts, "dataset": ds, "param": pname,
                "Rhat_minus_1": s["Rhat_m1"], "ESS": s["ESS"], "raw_rows": total_raw,
            })

    # ── full report (status_latest.txt) ──────────────────────────────────
    out_both("")
    out_both("=" * 120)
    out_both(f"  {ds_label}   |   chains: {len(chain_list)} (old {n_old}, new {n_new})   |   raw rows: {total_raw}")
    out_both("=" * 120)

    out_both(f"\n  [A] COHORT NEW ({n_new} chains, started < {COHORT_WINDOW_H}h ago)")
    for line in fmt_stats_table(stats_new):
        out_both(line)
    phys_new = physics_oneliner(chain_list, cohort_filter="new")
    if phys_new:
        out_both(f"\n  Physics (new):{phys_new}")

    out_both(f"\n  [B] ALL CHAINS ({len(chain_list)} chains)")
    for line in fmt_stats_table(stats_all):
        out_both(line)
    phys_all = physics_oneliner(chain_list, cohort_filter=None)
    if phys_all:
        out_both(f"\n  Physics (all):{phys_all}")

    # ── cohort-only report ───────────────────────────────────────────────
    out_cohort("")
    out_cohort("=" * 120)
    out_cohort(f"  {ds_label}   |   new chains: {n_new}   |   rows (new only): "
               f"{sum(d.shape[0] for d, _, _, c, _ in chain_list if c == 'new')}")
    out_cohort("=" * 120)
    for line in fmt_stats_table(stats_new):
        out_cohort(line)
    if phys_new:
        out_cohort(f"\n  Physics:{phys_new}")

    # ── per-chain means table ────────────────────────────────────────────
    out_both("")
    out_both(f"  {'Chain':<30s} {'Cohort':<6s} {'Age(h)':>7s} {'Rows':>5s}  "
             f"{'H0':>10s}  {'ΔNeff':>10s}  {'tau':>10s}")
    out_both(f"  {'-'*30} {'-'*6} {'-'*7} {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}")
    for data, cm, label, cohort, start_ep in chain_list:
        n = data.shape[0]
        w = data[:, cm["weight"]]; wn = w / w.sum()
        age_h = (now_epoch - start_ep) / 3600.0
        row = {"dataset": ds, "chain": label, "cohort": cohort, "rows": n}
        for pn in ["H0", "delta_neff", "tau"]:
            row[pn] = np.average(data[:, cm[pn]], weights=wn) if pn in cm and cm[pn] < data.shape[1] else float("nan")
        out_both(f"  {label:<30s} {cohort:<6s} {age_h:7.1f} {n:5d}  "
                 f"{row['H0']:10.4f}  {row['delta_neff']:10.6f}  {row['tau']:10.6f}")
        means_rows.append(row)

    # ── convergence CSV rows ─────────────────────────────────────────────
    for pname in CORE:
        sa = stats_all[pname]
        sn = stats_new[pname]
        conv_rows.append({
            "dataset": ds, "param": pname,
            "Rhat_all": f"{sa['Rhat']:.6f}" if not np.isnan(sa['Rhat']) else "",
            "Rhat_m1_all": f"{sa['Rhat_m1']:.6f}" if not np.isnan(sa['Rhat_m1']) else "",
            "ESS_all": f"{sa['ESS']:.1f}" if not np.isnan(sa['ESS']) else "",
            "drift_all": f"{sa['drift']:.4f}" if not np.isnan(sa['drift']) else "",
            "Rhat_new": f"{sn['Rhat']:.6f}" if not np.isnan(sn['Rhat']) else "",
            "Rhat_m1_new": f"{sn['Rhat_m1']:.6f}" if not np.isnan(sn['Rhat_m1']) else "",
            "ESS_new": f"{sn['ESS']:.1f}" if not np.isnan(sn['ESS']) else "",
            "drift_new": f"{sn['drift']:.4f}" if not np.isnan(sn['drift']) else "",
        })

    # ── trace plots ──────────────────────────────────────────────────────
    for pname in TRACE_PARAMS:
        fig, ax = plt.subplots(figsize=(14, 5))
        for data, cm, label, cohort, _ in chain_list:
            if pname not in cm or cm[pname] >= data.shape[1]:
                continue
            vals = data[:, cm[pname]]
            style = "-" if cohort == "old" else "--"
            alpha = 1.0 if cohort == "old" else 0.7
            ax.plot(np.arange(len(vals)), vals, style, alpha=alpha, linewidth=0.8,
                    label=f"{label} ({cohort})")
        ax.set_xlabel("Step")
        ax.set_ylabel(pname)
        ax.set_title(f"{ds} — {pname} trace   [{ts}]")
        ax.legend(fontsize=7, ncol=2, loc="upper right")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"trace_{ds}_{pname}.png"), dpi=150)
        plt.close(fig)

    # ── freeze check ─────────────────────────────────────────────────────
    freeze_lines.extend(evaluate_freeze(ds_label, stats_all, stats_new))

# ── cross-dataset summary ────────────────────────────────────────────────

out_both("")
out_both("=" * 120)
out_both("CROSS-DATASET SUMMARY (all_chains mode)")
out_both("=" * 120)
hdr = (f"  {'Dataset':<18s}  {'Chains':>6s}  {'Raw':>6s}  "
       f"{'Rm1(H0)':>10s}  {'Rm1(ΔN)':>10s}  {'Rm1(τ)':>10s}  "
       f"{'ESS(H0)':>8s}  {'ESS(ΔN)':>8s}  {'worst Rm1':>10s}")
out_both(hdr)
out_both(f"  {'-'*18}  {'-'*6}  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*8}  {'-'*8}  {'-'*10}")

for ds in DATASETS:
    ds_means = [r for r in means_rows if r["dataset"] == ds]
    if not ds_means:
        continue
    n_ch = len(ds_means)
    n_raw = sum(r["rows"] for r in ds_means)
    sa = all_stats_dict.get(ds, {})
    if not sa:
        continue
    rm1_h0  = sa["H0"]["Rhat_m1"]
    rm1_dn  = sa["delta_neff"]["Rhat_m1"]
    rm1_tau = sa["tau"]["Rhat_m1"]
    ess_h0  = sa["H0"]["ESS"]
    ess_dn  = sa["delta_neff"]["ESS"]
    worst   = max(sa[p]["Rhat_m1"] for p in CORE if not np.isnan(sa[p]["Rhat_m1"]))
    label   = ds.replace("_", " ").title()
    out_both(f"  {label:<18s}  {n_ch:6d}  {n_raw:6d}  "
             f"{rm1_h0:10.5f}  {rm1_dn:10.5f}  {rm1_tau:10.5f}  "
             f"{ess_h0:8.1f}  {ess_dn:8.1f}  {worst:10.5f}")

out_both(f"\nTargets: Rhat_m1 < {TARGET} (core), < {TARGET_TAU} (tau)")

# ── append to cumulative history ──────────────────────────────────────────
append_history(history_new)

# ── trend analysis ────────────────────────────────────────────────────────
history = load_history()

trend_lines = []
trend_lines.append(f"BigBounce MCMC Trend Monitor — {ts}")
trend_lines.append(f"Method: linear extrapolation of Rhat_m1 toward target")
trend_lines.append(f"Plateau flag: <5% improvement over 12h window")
trend_lines.append("=" * 120)

for ds in DATASETS:
    trend_lines.append("")
    trend_lines.append(f"--- {ds.upper().replace('_',' ')} ---")
    trend_lines.append(
        f"  {'Param':>12s}  {'Current':>10s}  {'6h ago':>10s}  {'Δ(6h)':>10s}  "
        f"{'12h ago':>10s}  {'Δ(12h)':>10s}  {'%impr 12h':>10s}  {'ETA (hrs)':>10s}  {'Flag':>14s}")
    trend_lines.append(
        f"  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*10}  "
        f"{'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*14}")

    for pname in CORE:
        sa = all_stats_dict.get(ds, {}).get(pname)
        if sa is None:
            continue
        current = sa["Rhat_m1"]
        if np.isnan(current):
            trend_lines.append(f"  {pname:>12s}  {'N/A':>10s}")
            continue

        # find closest history points
        ds_ph = sorted([h for h in history if h["dataset"] == ds and h["param"] == pname],
                       key=lambda x: x["epoch"])

        def nearest(target_ep):
            best, best_d = None, float("inf")
            for h in ds_ph:
                d = abs(h["epoch"] - target_ep)
                if d < best_d:
                    best_d = d; best = h
            return (best["Rhat_minus_1"], best_d) if best else (None, float("inf"))

        v6, d6 = nearest(now_epoch - 6 * 3600)
        v12, d12 = nearest(now_epoch - 12 * 3600)
        if d6 > 2 * 3600: v6 = None
        if d12 > 2 * 3600: v12 = None

        delta_6h  = (current - v6) if v6 is not None else None
        delta_12h = (current - v12) if v12 is not None else None
        pct_impr  = ((v12 - current) / v12 * 100) if v12 is not None and v12 > 0 else None

        tgt = TARGET_TAU if pname == "tau" else TARGET
        eta = None
        if delta_6h is not None and delta_6h < 0:
            slope = delta_6h / 6.0
            remaining = current - tgt
            if remaining > 0 and slope < 0:
                eta = remaining / abs(slope)

        flag = ""
        if pct_impr is not None:
            if pct_impr < 0:
                flag = "WORSENING"
            elif pct_impr < 5:
                flag = "PLATEAU RISK"

        cur_s = f"{current:.5f}"
        v6_s  = f"{v6:.5f}" if v6 is not None else "no data"
        d6_s  = f"{delta_6h:+.5f}" if delta_6h is not None else "—"
        v12_s = f"{v12:.5f}" if v12 is not None else "no data"
        d12_s = f"{delta_12h:+.5f}" if delta_12h is not None else "—"
        pct_s = f"{pct_impr:+.1f}%" if pct_impr is not None else "—"
        eta_s = f"{eta:.1f}" if eta is not None else ("∞" if delta_6h is not None and delta_6h >= 0 else "—")

        trend_lines.append(
            f"  {pname:>12s}  {cur_s:>10s}  {v6_s:>10s}  {d6_s:>10s}  "
            f"{v12_s:>10s}  {d12_s:>10s}  {pct_s:>10s}  {eta_s:>10s}  {flag:>14s}")

# ── write all output files ────────────────────────────────────────────────

with open(os.path.join(OUT_DIR, "status_latest.txt"), "w") as f:
    f.write("\n".join(full_txt) + "\n")

with open(os.path.join(OUT_DIR, "status_cohort_new.txt"), "w") as f:
    f.write("\n".join(cohort_txt) + "\n")

with open(os.path.join(OUT_DIR, "convergence_latest.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=[
        "dataset", "param",
        "Rhat_all", "Rhat_m1_all", "ESS_all", "drift_all",
        "Rhat_new", "Rhat_m1_new", "ESS_new", "drift_new"])
    w.writeheader()
    w.writerows(conv_rows)

with open(os.path.join(OUT_DIR, "chain_means_latest.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["dataset", "chain", "cohort", "rows", "H0", "delta_neff", "tau"])
    for r in means_rows:
        w.writerow([r["dataset"], r["chain"], r["cohort"], r["rows"],
                    f"{r['H0']:.6f}" if not np.isnan(r["H0"]) else "",
                    f"{r['delta_neff']:.6f}" if not np.isnan(r["delta_neff"]) else "",
                    f"{r['tau']:.6f}" if not np.isnan(r["tau"]) else ""])

with open(os.path.join(OUT_DIR, "freeze_check.txt"), "w") as f:
    f.write("\n".join(freeze_lines) + "\n")

with open(os.path.join(OUT_DIR, "trend_monitor_latest.txt"), "w") as f:
    f.write("\n".join(trend_lines) + "\n")

out_both("")
out_both("Saved: status_latest.txt, status_cohort_new.txt, convergence_latest.csv,")
out_both("       chain_means_latest.csv, freeze_check.txt, trend_monitor_latest.txt, trace_*.png")

# print freeze + trend to terminal
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
