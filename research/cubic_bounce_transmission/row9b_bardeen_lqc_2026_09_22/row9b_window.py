#!/usr/bin/env python3
"""Leg C of row 9b: settle the f_NL^after[S2] EVALUATION-WINDOW convention (A3M R11 ESSENTIAL 2).

R11 found that `f_NL^after[S2] = -1.25` was quoted to three significant figures with an UNDISCLOSED and
NON-UNIFORM eta_* convention: `lane9b2_s2_rawadm.main` uses `fac = min(50, 0.2/k eta_B)`, i.e.
eta_*/eta_B = 50 at k eta_B = 1e-3 and 3e-3 but 20 at 1e-2 (because the second condition k eta_* <= 0.2
binds there).  R11 closed the item by DISCLOSING the convention.  This leg closes it by COMPUTING the
sensitivity: a full eta_* scan at all three k-points with the committed machinery, unmodified.

Pre-registered convention (PREREGISTRATION.md section 3): adopt the LARGEST eta_* lying on a plateau
subject to k eta_* <= 0.2, a plateau being three consecutive scanned eta_* agreeing to <= 0.5%.
Pre-registered failure branch: a k-point with no plateau is reported as such and its number carries the
full measured spread as an open systematic.

Run: python3 row9b_window.py -> row9b_window.log, window_results.json
"""
import json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.abspath("../lane9b2_s2_rawadm"))
import lane9b2_s2_rawadm as L9                                   # committed, unmodified

LOG, OUT = [], {}
def log(s=""):
    print(s); LOG.append(str(s))

T0 = time.time()
KT = [1e-3, 3e-3, 1e-2]
FACS = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 30.0, 50.0, 75.0, 100.0, 150.0, 200.0]
PLATEAU_TOL = 0.005
KETA_STAR_CAP = 0.2

log("=" * 104)
log("LEG C - evaluation-window convention for f_NL^after[S2] on the Quintin-type background")
log("=" * 104)

bg = L9.Quintin(1.0)
K3, K2 = L9.build_kernels()
K3f = L9.kernel_fn(K3)
log("background: Quintin-type dtB=1, eta_B=%.6f | committed lane9b2 raw-ADM cubic kernel, unmodified" % bg.eta_B)

rows = {}
for kt in KT:
    before = L9.full_fnl_after_S2(bg, K3f, kt, upto="contraction")["f_NL"]
    scan = []
    for fac in FACS:
        r = L9.full_fnl_after_S2(bg, K3f, kt, eta_star_fac=fac)
        scan.append(dict(fac=fac, k_eta_star=r["k_eta_star"], f_NL_after=r["f_NL_after"],
                         parts=r["parts"], within_cap=bool(r["k_eta_star"] <= KETA_STAR_CAP)))
    rows[str(kt)] = dict(f_NL_before=before, scan=scan)
    log("\n k eta_B = %g   (f_NL^before = %+.6f)" % (kt, before))
    log("   eta*/eta_B :  " + "  ".join("%7.0f" % s["fac"] for s in scan))
    log("   k eta*     :  " + "  ".join("%7.3f" % s["k_eta_star"] for s in scan))
    log("   f_NL^after :  " + "  ".join("%+7.4f" % s["f_NL_after"] for s in scan))
    log("   within cap :  " + "  ".join("%7s" % ("yes" if s["within_cap"] else "NO") for s in scan))

# ---------------------------------------------------------------- plateau detection + adopted convention
log("\n" + "-" * 104)
log("plateau test: three consecutive scanned eta_* agreeing to <= %.1f%%, subject to k eta_* <= %.2f"
    % (100 * PLATEAU_TOL, KETA_STAR_CAP))
adopted = {}
for kt in KT:
    scan = rows[str(kt)]["scan"]
    ok = [s for s in scan if s["within_cap"]]
    best = None
    for i in range(len(ok) - 2):
        tri = ok[i:i + 3]
        v = np.array([t["f_NL_after"] for t in tri])
        spread = float(np.ptp(v) / abs(np.mean(v)))
        if spread <= PLATEAU_TOL:
            best = dict(i=i, facs=[t["fac"] for t in tri], value=float(v[-1]), spread=spread)
    allv = np.array([s["f_NL_after"] for s in ok])
    full_spread = float(np.ptp(allv) / abs(np.mean(allv))) if len(allv) else float("nan")
    # post-hoc refinement (labelled as such in the .md): the pre-registered "largest plateau" rule is
    # DEGENERATE when every triple within the cap qualifies -- it then picks the most eta_*-DRIFTED triple.
    # The better-motivated choice is the STATIONARY point, i.e. the FLATTEST triple.
    flat = None
    for i in range(len(ok) - 2):
        tri = ok[i:i + 3]
        v = np.array([t["f_NL_after"] for t in tri])
        sp_ = float(np.ptp(v) / abs(np.mean(v)))
        if flat is None or sp_ < flat["spread"]:
            flat = dict(facs=[t["fac"] for t in tri], value=float(v[1]), spread=sp_)
    if best is not None:
        adopted[str(kt)] = dict(status="PLATEAU", eta_star_over_etaB=best["facs"][-1], f_NL_after=best["value"],
                                plateau_facs=best["facs"], plateau_spread=best["spread"],
                                systematic=best["spread"], full_spread_within_cap=full_spread,
                                n_qualifying_triples=sum(
                                    1 for i in range(len(ok) - 2)
                                    if float(np.ptp([t["f_NL_after"] for t in ok[i:i + 3]])
                                             / abs(np.mean([t["f_NL_after"] for t in ok[i:i + 3]]))) <= PLATEAU_TOL),
                                posthoc_stationary=flat)
        log("  k eta_B=%-7g PLATEAU (pre-registered rule) over eta*/eta_B = %s (spread %.3f%%) -> adopt "
            "eta*/eta_B = %g, f_NL^after = %+.4f +- %.4f"
            % (kt, best["facs"], 100 * best["spread"], best["facs"][-1], best["value"],
               abs(best["value"]) * best["spread"]))
        log("              post-hoc STATIONARY triple %s: f_NL^after = %+.4f (spread %.3f%%)"
            % (flat["facs"], flat["value"], 100 * flat["spread"]))
    else:
        v = float(ok[-1]["f_NL_after"]) if ok else float("nan")
        adopted[str(kt)] = dict(status="NO-PLATEAU", eta_star_over_etaB=(ok[-1]["fac"] if ok else None),
                                f_NL_after=v, systematic=full_spread, full_spread_within_cap=full_spread,
                                posthoc_stationary=flat)
        log("  k eta_B=%-7g NO PLATEAU within the cap: values %s -> quote %+.4f with the FULL spread %.2f%% "
            "as an open systematic (fewer significant figures)"
            % (kt, ["%+.4f" % s["f_NL_after"] for s in ok], v, 100 * full_spread))
        log("              post-hoc STATIONARY triple %s: f_NL^after = %+.4f (spread %.3f%%)"
            % (flat["facs"], flat["value"], 100 * flat["spread"]))

OUT = dict(date="2026-09-22", background="Quintin2015-type dtB=1",
           convention=dict(rule="largest eta_* on a plateau (3 consecutive within 0.5%) subject to k eta_* <= 0.2",
                           plateau_tol=PLATEAU_TOL, k_eta_star_cap=KETA_STAR_CAP, facs_scanned=FACS),
           committed_convention_in_lane9b2="fac = min(50, 0.2/k eta_B)",
           rows=rows, adopted=adopted, runtime_s=time.time() - T0)
open("row9b_window.log", "w").write("\n".join(LOG) + "\n")
json.dump(OUT, open("window_results.json", "w"), indent=2, default=str)
log("\n[done] %.1f s" % OUT["runtime_s"])
