#!/usr/bin/env python3
"""
BigBounce MCMC Monitor v6 — read-only, no process modification.

Changes from v5:
  1) ETA requires >=24h of history. Three-stage model:
     Stage A: Rhat_m1 > 0.3 → EARLY MIXING, no ETA
     Stage B: 0.3 >= Rhat_m1 > 0.05 → exponential decay fit (12-24h window)
     Stage C: Rhat_m1 <= 0.05 → linear ETA (near-convergence)
  2) Freeze summary replaced with ranked top-3 bottleneck params per dataset
  3) Per-chain outlier check: flag chains whose mean deviates >1.0σ from
     the median of other chains (for H0, delta_neff, tau)
  4) New output: bottlenecks_latest.txt

Outputs:
  status_latest.txt, status_cohort_new.txt, convergence_latest.csv,
  chain_means_latest.csv, freeze_check.txt, convergence_history.csv,
  trend_monitor_latest.txt, bottlenecks_latest.txt, trace_*.png
"""
import numpy as np
import glob, os, csv, time
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── config ───────────────────────────────────────────────────────────────
CHAINS_DIR     = "/workspace/bigbounce/reproducibility/chains"
OUT_DIR        = "/workspace/bigbounce/reproducibility/cosmology"
DATASETS       = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]
CORE           = ["H0", "delta_neff", "omegam", "ombh2", "ns", "tau", "sigma8"]
TRACE_PARAMS   = ["H0", "delta_neff"]
TARGET         = 0.01          # Rhat_m1 target for most params
TARGET_TAU     = 0.02          # relaxed target for tau
DRIFT_THRESH   = 0.2           # sigma units
COHORT_WINDOW_H = 24           # hours — chains started within this window are "new"
MIN_HISTORY_H  = 24            # hours of history required before computing ETA
HISTORY_FILE   = os.path.join(OUT_DIR, "convergence_history.csv")
OUTLIER_PARAMS = ["H0", "delta_neff", "tau"]
OUTLIER_THRESH = 1.0           # sigma

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
    input_yaml = os.path.join(chain_dir, "spin_torsion.input.yaml")
    if os.path.exists(input_yaml):
        return os.path.getmtime(input_yaml)
    try:
        return os.stat(chain_dir).st_ctime
    except Exception:
        return 0.0

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

def drift_2040(vals, weights):
    n = len(vals)
    n_r = max(int(n * 0.20), 2)
    n_o = max(int(n * 0.40), 2)
    v_r, w_r = vals[-n_r:], weights[-n_r:]
    v_o, w_o = vals[-n_o:], weights[-n_o:]
    mu_r = weighted_mean(v_r, w_r)
    mu_o = weighted_mean(v_o, w_o)
    sig = max(weighted_std(v_r, w_r), weighted_std(v_o, w_o), 1e-30)
    return (mu_r - mu_o) / sig

def target_for(pname):
    return TARGET_TAU if pname == "tau" else TARGET

# ── chain loading + cohort assignment ─────────────────────────────────────

def load_dataset_chains(ds):
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

# ── per-chain outlier detection ───────────────────────────────────────────

def detect_outliers(chain_list):
    """For each of OUTLIER_PARAMS, flag chains whose weighted mean
    deviates by > OUTLIER_THRESH * σ from the median of other chains.
    Returns list of (chain_label, param, chain_mean, median, sigma, devσ)."""
    flags = []
    # compute per-chain weighted means
    chain_means = []   # list of {label, H0, delta_neff, tau}
    for data, cm, label, cohort, _ in chain_list:
        w = data[:, cm["weight"]]
        wn = w / w.sum()
        row = {"label": label, "cohort": cohort}
        for pn in OUTLIER_PARAMS:
            if pn in cm and cm[pn] < data.shape[1]:
                row[pn] = np.average(data[:, cm[pn]], weights=wn)
            else:
                row[pn] = float("nan")
        chain_means.append(row)

    for pn in OUTLIER_PARAMS:
        vals = [(r["label"], r[pn]) for r in chain_means if not np.isnan(r[pn])]
        if len(vals) < 3:
            continue
        all_vals = np.array([v for _, v in vals])
        median = np.median(all_vals)
        # MAD-based sigma (robust)
        mad = np.median(np.abs(all_vals - median))
        sigma = mad * 1.4826  # scale MAD to sigma for normal distribution
        if sigma < 1e-30:
            continue
        for label, v in vals:
            dev = abs(v - median) / sigma
            if dev > OUTLIER_THRESH:
                flags.append((label, pn, v, median, sigma, dev))
    return flags

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

# ── ETA: three-stage model ────────────────────────────────────────────────

def compute_eta(pname, current_rm1, ds_param_hist, history_span_h):
    """
    Three-stage ETA model.
    Returns (stage_label, eta_hours_or_None, extra_info).
    """
    tgt = target_for(pname)

    # Stage A: early mixing — no ETA
    if current_rm1 > 0.3:
        return ("EARLY MIXING", None, "")

    # Need >=24h of history for any ETA
    if history_span_h < MIN_HISTORY_H:
        stage = "CLOSE" if current_rm1 <= 0.05 else "MIXING"
        return (stage, None, f"need {MIN_HISTORY_H}h history")

    # Stage C: near-convergence — linear ETA
    if current_rm1 <= 0.05:
        # Use last 12h of data for linear fit
        recent = [h for h in ds_param_hist
                  if h["epoch"] >= now_epoch - 12 * 3600]
        if len(recent) >= 2:
            t_arr = np.array([(h["epoch"] - now_epoch) / 3600.0 for h in recent])
            y_arr = np.array([h["Rhat_minus_1"] for h in recent])
            # linear regression
            if len(t_arr) >= 2:
                coeffs = np.polyfit(t_arr, y_arr, 1)
                slope = coeffs[0]  # per hour
                if slope < 0:
                    remaining = current_rm1 - tgt
                    if remaining > 0:
                        eta = remaining / abs(slope)
                        return ("LINEAR ETA", eta, f"slope={slope:.6f}/h")
        return ("CLOSE", None, "slope>=0 or insufficient data")

    # Stage B: 0.05 < Rhat_m1 <= 0.3 — exponential decay fit
    # Use points from the last 12-24h window
    window_pts = [h for h in ds_param_hist
                  if now_epoch - 24 * 3600 <= h["epoch"] <= now_epoch]
    if len(window_pts) < 3:
        return ("MIXING", None, f"only {len(window_pts)} pts in 24h window")

    t_arr = np.array([(h["epoch"] - now_epoch) / 3600.0 for h in window_pts])
    y_arr = np.array([h["Rhat_minus_1"] for h in window_pts])

    # Filter out non-positive values (can't take log)
    mask = y_arr > 0
    if mask.sum() < 3:
        return ("MIXING", None, "too few positive Rhat_m1 pts for exp fit")

    t_fit = t_arr[mask]
    y_fit = y_arr[mask]
    ln_y  = np.log(y_fit)

    # Linear regression: ln(y) = ln(a) - b*t  →  ln(y) = c0 + c1*t
    try:
        coeffs = np.polyfit(t_fit, ln_y, 1)
    except Exception:
        return ("MIXING", None, "polyfit failed")

    c1 = coeffs[0]    # should be negative for decay
    c0 = coeffs[1]    # ln(a)

    if c1 >= 0:
        return ("MIXING", None, "exp slope>=0 (not decaying)")

    # Rhat_m1(t) = exp(c0 + c1*t)
    # Solve for target: tgt = exp(c0 + c1*t_eta)
    # t_eta = (ln(tgt) - c0) / c1
    t_eta = (np.log(tgt) - c0) / c1  # hours from now
    if t_eta <= 0:
        # Already below target per model (shouldn't happen if current > 0.05)
        return ("MIXING", 0.0, "model says already converged")

    halflife = np.log(2) / abs(c1)
    return ("EXP DECAY", t_eta, f"halflife={halflife:.1f}h")

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

def fmt_stats_table(stats):
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

# ── freeze check with ranked bottlenecks ──────────────────────────────────

def evaluate_freeze(ds_label, stats_all, stats_new):
    lines = []
    lines.append("")
    lines.append(f"--- {ds_label} ---")

    for mode_name, stats in [("all_chains", stats_all), ("cohort_new", stats_new)]:
        lines.append(f"  [{mode_name}]")

        # Rhat check
        rhat_pass = True
        param_rm1 = []
        for pname in CORE:
            rm1 = stats[pname]["Rhat_m1"]
            tgt = target_for(pname)
            if np.isnan(rm1) or rm1 >= tgt:
                rhat_pass = False
            if not np.isnan(rm1):
                param_rm1.append((pname, rm1, tgt))

        # Top 3 bottlenecks (highest Rhat_m1 first)
        param_rm1.sort(key=lambda x: x[1], reverse=True)
        top3 = param_rm1[:3]
        top3_str = ", ".join(f"{p}={rm1:.4f}" for p, rm1, _ in top3)

        tgt_str = f"Rhat_m1 < {TARGET} (core) + < {TARGET_TAU} (tau)"
        lines.append(f"    {tgt_str}: {'PASS' if rhat_pass else 'FAIL'}")
        lines.append(f"    Bottlenecks: {top3_str}")

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

        # ESS
        ess_h0 = stats.get("H0", {}).get("ESS", float("nan"))
        ess_dn = stats.get("delta_neff", {}).get("ESS", float("nan"))
        lines.append(f"    ESS(H0) = {ess_h0:.1f}   ESS(ΔNeff) = {ess_dn:.1f}")

        overall = "PASS" if (rhat_pass and drift_pass) else "FAIL"
        lines.append(f"    >> {mode_name} OVERALL: {overall}")

    return lines

# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════

full_txt       = []
cohort_txt     = []
conv_rows      = []
means_rows     = []
freeze_lines   = []
history_new    = []
bottleneck_lines = []
all_stats_dict = {}
all_outliers   = {}   # ds -> list of outlier tuples

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
Cohort window: chains started within last {COHORT_WINDOW_H}h are "new"
ETA model: Stage A (>0.3)=EARLY MIXING, Stage B (0.05-0.3)=exp decay, Stage C (<=0.05)=linear"""

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

bottleneck_lines.append(f"BigBounce MCMC Bottleneck Report — {ts}")
bottleneck_lines.append("=" * 100)

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

    stats_all = compute_stats(chain_list, cohort_filter=None)
    stats_new = compute_stats(chain_list, cohort_filter="new")
    all_stats_dict[ds] = stats_all

    # record history
    for pname in CORE:
        s = stats_all[pname]
        if not np.isnan(s["Rhat_m1"]):
            history_new.append({
                "epoch": now_epoch, "timestamp": ts, "dataset": ds, "param": pname,
                "Rhat_minus_1": s["Rhat_m1"], "ESS": s["ESS"], "raw_rows": total_raw,
            })

    # outlier detection
    outliers = detect_outliers(chain_list)
    all_outliers[ds] = outliers

    # ── full report ──────────────────────────────────────────────────────
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

    # ── per-chain means + outlier flags ──────────────────────────────────
    outlier_set = {(o[0], o[1]) for o in outliers}  # (label, param)

    out_both("")
    out_both(f"  {'Chain':<30s} {'Cohort':<6s} {'Age(h)':>7s} {'Rows':>5s}  "
             f"{'H0':>10s}  {'ΔNeff':>10s}  {'tau':>10s}  {'Outlier':>10s}")
    out_both(f"  {'-'*30} {'-'*6} {'-'*7} {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    for data, cm, label, cohort, start_ep in chain_list:
        n = data.shape[0]
        w = data[:, cm["weight"]]; wn = w / w.sum()
        age_h = (now_epoch - start_ep) / 3600.0
        row = {"dataset": ds, "chain": label, "cohort": cohort, "rows": n}
        for pn in ["H0", "delta_neff", "tau"]:
            row[pn] = np.average(data[:, cm[pn]], weights=wn) if pn in cm and cm[pn] < data.shape[1] else float("nan")

        # check if this chain is flagged
        chain_flags = [pn for pn in OUTLIER_PARAMS if (label, pn) in outlier_set]
        flag_str = ",".join(chain_flags) if chain_flags else ""

        out_both(f"  {label:<30s} {cohort:<6s} {age_h:7.1f} {n:5d}  "
                 f"{row['H0']:10.4f}  {row['delta_neff']:10.6f}  {row['tau']:10.6f}  "
                 f"{flag_str:>10s}")
        means_rows.append(row)

    # print outlier details if any
    if outliers:
        out_both("")
        out_both(f"  ** OUTLIER CHAINS (>{OUTLIER_THRESH}σ from median) **")
        for label, pn, val, med, sig, dev in outliers:
            out_both(f"     {label}: {pn} = {val:.4f}  (median={med:.4f}, σ={sig:.4f}, dev={dev:.1f}σ)")

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

    # ── bottleneck report ────────────────────────────────────────────────
    bottleneck_lines.append("")
    bottleneck_lines.append(f"--- {ds_label} ---")
    param_rm1 = [(p, stats_all[p]["Rhat_m1"]) for p in CORE
                 if not np.isnan(stats_all[p]["Rhat_m1"])]
    param_rm1.sort(key=lambda x: x[1], reverse=True)
    for rank, (pn, rm1) in enumerate(param_rm1[:3], 1):
        tgt = target_for(pn)
        ratio = rm1 / tgt
        bottleneck_lines.append(f"  #{rank}  {pn:<14s}  Rhat_m1={rm1:.5f}  target={tgt}  ({ratio:.0f}x target)")

    if outliers:
        bottleneck_lines.append(f"  Outlier chains:")
        for label, pn, val, med, sig, dev in outliers:
            bottleneck_lines.append(f"    {label}: {pn}={val:.4f} ({dev:.1f}σ from median)")

# ── cross-dataset summary ────────────────────────────────────────────────

out_both("")
out_both("=" * 120)
out_both("CROSS-DATASET SUMMARY (all_chains mode)")
out_both("=" * 120)
hdr = (f"  {'Dataset':<18s}  {'Chains':>6s}  {'Raw':>6s}  "
       f"{'Rm1(H0)':>10s}  {'Rm1(ΔN)':>10s}  {'Rm1(τ)':>10s}  "
       f"{'ESS(H0)':>8s}  {'ESS(ΔN)':>8s}  {'Top Bottleneck':>20s}")
out_both(hdr)
out_both(f"  {'-'*18}  {'-'*6}  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*8}  {'-'*8}  {'-'*20}")

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
    # top 3 bottleneck names
    param_rm1 = [(p, sa[p]["Rhat_m1"]) for p in CORE if not np.isnan(sa[p]["Rhat_m1"])]
    param_rm1.sort(key=lambda x: x[1], reverse=True)
    top3_str = ", ".join(p for p, _ in param_rm1[:3])
    label = ds.replace("_", " ").title()
    out_both(f"  {label:<18s}  {n_ch:6d}  {n_raw:6d}  "
             f"{rm1_h0:10.5f}  {rm1_dn:10.5f}  {rm1_tau:10.5f}  "
             f"{ess_h0:8.1f}  {ess_dn:8.1f}  {top3_str:>20s}")

out_both(f"\nTargets: Rhat_m1 < {TARGET} (core), < {TARGET_TAU} (tau)")

# ── append to cumulative history ──────────────────────────────────────────
append_history(history_new)

# ── trend analysis (three-stage ETA) ──────────────────────────────────────
history = load_history()

# compute total history span
all_epochs = [h["epoch"] for h in history]
history_span_h = (max(all_epochs) - min(all_epochs)) / 3600.0 if len(all_epochs) >= 2 else 0.0

trend_lines = []
trend_lines.append(f"BigBounce MCMC Trend Monitor — {ts}")
trend_lines.append(f"ETA model: Stage A (Rm1>0.3)=EARLY MIXING | Stage B (0.05-0.3)=exp decay | Stage C (<=0.05)=linear")
trend_lines.append(f"History span: {history_span_h:.1f}h ({len(all_epochs)} data points). ETA requires >= {MIN_HISTORY_H}h.")
trend_lines.append(f"Plateau flag: <5% improvement over 12h window")
trend_lines.append("=" * 120)

for ds in DATASETS:
    trend_lines.append("")
    trend_lines.append(f"--- {ds.upper().replace('_',' ')} ---")
    trend_lines.append(
        f"  {'Param':>12s}  {'Rhat_m1':>10s}  {'Stage':>14s}  {'ETA (hrs)':>10s}  "
        f"{'12h ago':>10s}  {'Δ(12h)':>10s}  {'%impr 12h':>10s}  {'Flag':>14s}  {'Note':>20s}")
    trend_lines.append(
        f"  {'-'*12}  {'-'*10}  {'-'*14}  {'-'*10}  "
        f"{'-'*10}  {'-'*10}  {'-'*10}  {'-'*14}  {'-'*20}")

    for pname in CORE:
        sa = all_stats_dict.get(ds, {}).get(pname)
        if sa is None:
            continue
        current = sa["Rhat_m1"]
        if np.isnan(current):
            trend_lines.append(f"  {pname:>12s}  {'N/A':>10s}")
            continue

        ds_ph = sorted([h for h in history if h["dataset"] == ds and h["param"] == pname],
                       key=lambda x: x["epoch"])

        # three-stage ETA
        stage, eta, note = compute_eta(pname, current, ds_ph, history_span_h)

        # 12h comparison for plateau detection
        def find_nearest(target_ep):
            best, best_d = None, float("inf")
            for h in ds_ph:
                d = abs(h["epoch"] - target_ep)
                if d < best_d:
                    best_d = d; best = h
            return (best["Rhat_minus_1"], best_d) if best else (None, float("inf"))

        v12, d12 = find_nearest(now_epoch - 12 * 3600)
        if d12 > 2 * 3600:
            v12 = None

        delta_12h = (current - v12) if v12 is not None else None
        pct_impr  = ((v12 - current) / v12 * 100) if v12 is not None and v12 > 0 else None

        flag = ""
        if pct_impr is not None:
            if pct_impr < 0:
                flag = "WORSENING"
            elif pct_impr < 5:
                flag = "PLATEAU RISK"

        cur_s = f"{current:.5f}"
        eta_s = f"{eta:.1f}" if eta is not None else "—"
        v12_s = f"{v12:.5f}" if v12 is not None else "no data"
        d12_s = f"{delta_12h:+.5f}" if delta_12h is not None else "—"
        pct_s = f"{pct_impr:+.1f}%" if pct_impr is not None else "—"

        trend_lines.append(
            f"  {pname:>12s}  {cur_s:>10s}  {stage:>14s}  {eta_s:>10s}  "
            f"{v12_s:>10s}  {d12_s:>10s}  {pct_s:>10s}  {flag:>14s}  {note:>20s}")

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

with open(os.path.join(OUT_DIR, "bottlenecks_latest.txt"), "w") as f:
    f.write("\n".join(bottleneck_lines) + "\n")

out_both("")
out_both("Saved: status_latest.txt, status_cohort_new.txt, convergence_latest.csv,")
out_both("       chain_means_latest.csv, freeze_check.txt, trend_monitor_latest.txt,")
out_both("       bottlenecks_latest.txt, trace_*.png")

# print freeze + bottleneck + trend to terminal
print("\n" + "=" * 120)
print("FREEZE CHECK")
print("=" * 120)
for line in freeze_lines:
    print(line)

print("\n" + "=" * 120)
print("BOTTLENECK REPORT")
print("=" * 120)
for line in bottleneck_lines:
    print(line)

print("\n" + "=" * 120)
print("TREND MONITOR")
print("=" * 120)
for line in trend_lines:
    print(line)
