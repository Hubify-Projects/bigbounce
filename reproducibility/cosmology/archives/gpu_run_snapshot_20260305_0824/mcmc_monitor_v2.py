#!/usr/bin/env python3
"""
BigBounce MCMC Monitor v2 — read-only, no process modification.

Outputs:
  cosmology/status_latest.txt          human summary
  cosmology/convergence_latest.csv     dataset × param × Rhat × ESS × tau_int
  cosmology/chain_means_latest.csv     dataset × chain × mean(H0, delta_neff, tau)
  cosmology/trace_<dataset>_H0.png     trace overlay
  cosmology/trace_<dataset>_delta_neff.png
"""
import numpy as np
import glob, os, csv
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── config ───────────────────────────────────────────────────────────────
CHAINS_DIR = "/workspace/bigbounce/reproducibility/chains"
OUT_DIR    = "/workspace/bigbounce/reproducibility/cosmology"
DATASETS   = ["planck_only", "planck_bao", "planck_bao_sn", "full_tension"]
CORE       = ["H0", "delta_neff", "omegam", "ombh2", "ns", "tau", "sigma8"]
TRACE_PARAMS = ["H0", "delta_neff"]

os.makedirs(OUT_DIR, exist_ok=True)
now = datetime.utcnow()
ts  = now.strftime("%Y-%m-%d %H:%M:%S UTC")

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
    """Integrated autocorrelation time via FFT (Sokal / Goodman-Weare)."""
    n = len(x)
    if n < 20:
        return float(n), 1.0  # tau, ess
    xc = x - np.mean(x)
    # zero-padded FFT autocorrelation
    f = np.fft.fft(xc, n=2 * n)
    acf = np.fft.ifft(f * np.conjugate(f))[:n].real
    if acf[0] == 0:
        return float(n), 1.0
    acf /= acf[0]
    # Geyer initial-positive-sequence truncation
    tau_int = 1.0
    for k in range(1, n // 2):
        rho_pair = acf[2 * k - 1] + acf[2 * k]
        if rho_pair < 0:
            break
        tau_int += 2.0 * rho_pair
    tau_int = max(tau_int, 1.0)
    ess = n / tau_int
    return tau_int, ess

def gelman_rubin(chain_arrays):
    """
    Standard Gelman-Rubin R-hat (BDA3 §11.4).
    Input: list of 1-d arrays, one per chain.
    Returns R-hat (≥ 1 by construction).
    """
    m = len(chain_arrays)
    if m < 2:
        return float("nan")
    # trim to equal length (shortest chain)
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
    rhat = np.sqrt(var_hat / W)
    return max(rhat, 1.0)   # clamp ≥ 1

def weighted_mean(v, w):
    wn = w / w.sum()
    return np.average(v, weights=wn)

# ── classify chains into cohorts ─────────────────────────────────────────

def chain_cohort(path):
    """Return 'original' or 'parallel' based on directory name."""
    dirname = os.path.basename(os.path.dirname(path))
    if "_chain" in dirname:
        return "parallel"
    return "original"

# ── main ─────────────────────────────────────────────────────────────────

txt_lines = []
def out(s=""):
    print(s)
    txt_lines.append(s)

conv_rows = []   # for convergence CSV
means_rows = []  # for chain_means CSV

out("=" * 115)
out(f"BigBounce MCMC Status — {ts}")
out("=" * 115)
out(f"Method: Gelman-Rubin R-hat (BDA3), autocorrelation ESS (Geyer IPS), per-chain header parsing")
out(f"Target: R-hat < 1.01, ESS > 100000 per param")

for ds in DATASETS:
    # collect paths
    paths = []
    orig = f"{CHAINS_DIR}/{ds}/spin_torsion.1.txt"
    if os.path.exists(orig):
        paths.append(orig)
    for p in sorted(glob.glob(f"{CHAINS_DIR}/{ds}_chain*/spin_torsion.1.txt")):
        paths.append(p)

    # load
    chain_list = []  # (data, cm, label, cohort)
    for p in paths:
        data, cm = load_chain(p)
        if data is not None:
            label = os.path.basename(os.path.dirname(p))
            cohort = chain_cohort(p)
            chain_list.append((data, cm, label, cohort))

    if not chain_list:
        out(f"\n  {ds}: NO DATA\n")
        continue

    originals  = [(d, cm, l, c) for d, cm, l, c in chain_list if c == "original"]
    parallels  = [(d, cm, l, c) for d, cm, l, c in chain_list if c == "parallel"]
    total_raw  = sum(d.shape[0] for d, _, _, _ in chain_list)

    out("")
    out("=" * 115)
    out(f"  {ds.upper().replace('_',' ')}   |   chains: {len(chain_list)} (orig {len(originals)}, parallel {len(parallels)})   |   raw rows: {total_raw}")
    out("=" * 115)

    # ── per-param R-hat / ESS table ──────────────────────────────────────
    header = (f"  {'Param':>12s}  {'R-hat(all)':>10s}  {'R-1(all)':>9s}  "
              f"{'R-hat(par)':>10s}  {'R-1(par)':>9s}  "
              f"{'ESS(AR)':>8s}  {'tau_int':>8s}  {'Status':>10s}")
    out(header)
    out(f"  {'-'*12}  {'-'*10}  {'-'*9}  {'-'*10}  {'-'*9}  {'-'*8}  {'-'*8}  {'-'*10}")

    for pname in CORE:
        # extract per-chain arrays
        all_arrs = []
        par_arrs = []
        for data, cm, label, cohort in chain_list:
            if pname in cm and cm[pname] < data.shape[1]:
                arr = data[:, cm[pname]]
                all_arrs.append(arr)
                if cohort == "parallel":
                    par_arrs.append(arr)

        if len(all_arrs) < 2:
            out(f"  {pname:>12s}  {'N/A':>10s}")
            conv_rows.append([ds, pname, "", "", "", "", ""])
            continue

        rhat_all = gelman_rubin(all_arrs)
        rm1_all  = rhat_all - 1.0
        rhat_par = gelman_rubin(par_arrs) if len(par_arrs) >= 2 else float("nan")
        rm1_par  = rhat_par - 1.0 if not np.isnan(rhat_par) else float("nan")

        # autocorrelation ESS: sum across chains
        total_ess = 0.0
        total_tau = 0.0
        n_tau = 0
        for arr in all_arrs:
            tau_i, ess_i = autocorr_tau(arr)
            total_ess += ess_i
            total_tau += tau_i
            n_tau += 1
        mean_tau = total_tau / n_tau if n_tau > 0 else float("nan")

        if rm1_all < 0.01:     status = "CONVERGED"
        elif rm1_all < 0.05:   status = "CLOSE"
        elif rm1_all < 0.20:   status = "MIXING"
        else:                  status = "RUNNING"

        ra_s = f"{rhat_all:.5f}"
        rm1a = f"{rm1_all:+.5f}"
        rp_s = f"{rhat_par:.5f}" if not np.isnan(rhat_par) else "N/A"
        rm1p = f"{rm1_par:+.5f}" if not np.isnan(rm1_par) else "N/A"

        out(f"  {pname:>12s}  {ra_s:>10s}  {rm1a:>9s}  {rp_s:>10s}  {rm1p:>9s}  {total_ess:8.1f}  {mean_tau:8.1f}  {status:>10s}")
        conv_rows.append([ds, pname, f"{rhat_all:.6f}", f"{rhat_par:.6f}" if not np.isnan(rhat_par) else "",
                          f"{total_ess:.1f}", f"{mean_tau:.2f}", status])

    # ── physics one-liner ────────────────────────────────────────────────
    all_dn = []
    all_dn_w = []
    all_h0 = []
    all_h0_w = []
    for data, cm, _, _ in chain_list:
        if "delta_neff" in cm:
            all_dn.append(data[:, cm["delta_neff"]])
            all_dn_w.append(data[:, cm["weight"]])
        if "H0" in cm:
            all_h0.append(data[:, cm["H0"]])
            all_h0_w.append(data[:, cm["weight"]])
    if all_dn:
        v = np.concatenate(all_dn); w = np.concatenate(all_dn_w)
        mu_dn = weighted_mean(v, w)
        sig_dn = np.sqrt(weighted_mean((v - mu_dn)**2, w))
        wn = w / w.sum()
        ppos = np.sum(wn[v > 0]) * 100
    if all_h0:
        v2 = np.concatenate(all_h0); w2 = np.concatenate(all_h0_w)
        mu_h0 = weighted_mean(v2, w2)
        sig_h0 = np.sqrt(weighted_mean((v2 - mu_h0)**2, w2))
        shoes = abs(mu_h0 - 73.04) / np.sqrt(sig_h0**2 + 1.04**2)
    if all_dn and all_h0:
        sig_str = f"{mu_dn/sig_dn:.2f}σ" if sig_dn > 0 else "N/A"
        out(f"\n  Physics:  ΔNeff = {mu_dn:.4f} ± {sig_dn:.4f} ({sig_str}, P>0={ppos:.1f}%)   "
            f"H₀ = {mu_h0:.2f} ± {sig_h0:.2f}   SH0ES Δ = {shoes:.2f}σ")

    # ── per-chain means ──────────────────────────────────────────────────
    out("")
    out(f"  {'Chain':<30s} {'Cohort':<9s} {'Rows':>5s}  {'H0':>10s}  {'ΔNeff':>10s}  {'tau':>10s}")
    out(f"  {'-'*30} {'-'*9} {'-'*5}  {'-'*10}  {'-'*10}  {'-'*10}")
    for data, cm, label, cohort in chain_list:
        n = data.shape[0]
        w = data[:, cm["weight"]]
        wn = w / w.sum()
        row = {"dataset": ds, "chain": label, "cohort": cohort, "rows": n}
        for pname in ["H0", "delta_neff", "tau"]:
            if pname in cm and cm[pname] < data.shape[1]:
                row[pname] = np.average(data[:, cm[pname]], weights=wn)
            else:
                row[pname] = float("nan")
        h0_s  = f"{row['H0']:.4f}" if not np.isnan(row['H0']) else "N/A"
        dn_s  = f"{row['delta_neff']:.6f}" if not np.isnan(row['delta_neff']) else "N/A"
        tau_s = f"{row['tau']:.6f}" if not np.isnan(row['tau']) else "N/A"
        out(f"  {label:<30s} {cohort:<9s} {n:5d}  {h0_s:>10s}  {dn_s:>10s}  {tau_s:>10s}")
        means_rows.append(row)

    # ── trace plots ──────────────────────────────────────────────────────
    for pname in TRACE_PARAMS:
        fig, ax = plt.subplots(figsize=(14, 5))
        for data, cm, label, cohort in chain_list:
            if pname not in cm or cm[pname] >= data.shape[1]:
                continue
            vals = data[:, cm[pname]]
            style = "-" if cohort == "original" else "--"
            alpha = 1.0 if cohort == "original" else 0.7
            ax.plot(np.arange(len(vals)), vals, style, alpha=alpha, linewidth=0.8, label=label)
        ax.set_xlabel("Step")
        ax.set_ylabel(pname)
        ax.set_title(f"{ds} — {pname} trace   [{ts}]")
        ax.legend(fontsize=7, ncol=2, loc="upper right")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        png_path = os.path.join(OUT_DIR, f"trace_{ds}_{pname}.png")
        fig.savefig(png_path, dpi=150)
        plt.close(fig)
        out(f"  Saved trace plot: {png_path}")

# ── cross-dataset summary ────────────────────────────────────────────────
out("")
out("=" * 115)
out("CROSS-DATASET SUMMARY")
out("=" * 115)
out(f"  {'Dataset':<18s}  {'Chains':>6s}  {'Raw':>6s}  {'ESS(H0)':>8s}  {'ESS(ΔNeff)':>10s}  "
    f"{'R-1(H0)':>8s}  {'R-1(ΔNeff)':>10s}  {'R-1(tau)':>9s}  {'max R-1':>8s}")
out(f"  {'-'*18}  {'-'*6}  {'-'*6}  {'-'*8}  {'-'*10}  {'-'*8}  {'-'*10}  {'-'*9}  {'-'*8}")

for ds in DATASETS:
    ds_rows = [r for r in conv_rows if r[0] == ds and r[2]]
    if not ds_rows:
        continue
    # find specific params
    def find_row(p):
        for r in ds_rows:
            if r[1] == p:
                return r
        return None

    n_chains = len([r for r in means_rows if r["dataset"] == ds])
    n_raw = sum(r["rows"] for r in means_rows if r["dataset"] == ds)
    rh0 = find_row("H0")
    rdn = find_row("delta_neff")
    rtau = find_row("tau")
    max_rm1 = max(float(r[2]) - 1.0 for r in ds_rows if r[2])

    ess_h0 = rh0[4] if rh0 else "N/A"
    ess_dn = rdn[4] if rdn else "N/A"
    rm1_h0 = f"{float(rh0[2])-1:.4f}" if rh0 and rh0[2] else "N/A"
    rm1_dn = f"{float(rdn[2])-1:.4f}" if rdn and rdn[2] else "N/A"
    rm1_tau = f"{float(rtau[2])-1:.4f}" if rtau and rtau[2] else "N/A"

    label = ds.replace("_", " ").title()
    out(f"  {label:<18s}  {n_chains:6d}  {n_raw:6d}  {ess_h0:>8s}  {ess_dn:>10s}  "
        f"{rm1_h0:>8s}  {rm1_dn:>10s}  {rm1_tau:>9s}  {max_rm1:8.4f}")

out(f"\nAll trace plots saved to {OUT_DIR}/trace_*.png")

# ── write files ──────────────────────────────────────────────────────────

# status_latest.txt
with open(os.path.join(OUT_DIR, "status_latest.txt"), "w") as f:
    f.write("\n".join(txt_lines) + "\n")

# convergence_latest.csv
with open(os.path.join(OUT_DIR, "convergence_latest.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["dataset", "param", "rhat_all", "rhat_parallel", "ess_autocorr", "tau_int", "status"])
    for r in conv_rows:
        w.writerow(r)

# chain_means_latest.csv
with open(os.path.join(OUT_DIR, "chain_means_latest.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["dataset", "chain", "cohort", "rows", "H0", "delta_neff", "tau"])
    for r in means_rows:
        w.writerow([r["dataset"], r["chain"], r["cohort"], r["rows"],
                     f"{r['H0']:.6f}" if not np.isnan(r['H0']) else "",
                     f"{r['delta_neff']:.6f}" if not np.isnan(r['delta_neff']) else "",
                     f"{r['tau']:.6f}" if not np.isnan(r['tau']) else ""])

out(f"\nSaved: status_latest.txt, convergence_latest.csv, chain_means_latest.csv")
