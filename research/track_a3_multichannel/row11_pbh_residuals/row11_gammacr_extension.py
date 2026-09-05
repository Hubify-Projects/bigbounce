"""Ledger row 11(b) -- extend the compaction scan to gamma_cr in [0.2, 1.0].

The committed 27-point grid (`outputs/pbh_compaction_fnl.json`) covers only
gamma_cr in [0.766, 0.968]; this lab's own near-scale-invariant shape sits at
gamma_cr in [0.267, 0.630] -- OUTSIDE that coverage
(`outputs/R5_18_GAMMACR_NOTE_2026-09-04.md`).  The paper quotes the required-
amplitude ratio A(-35/16)/A(-35/8) as "1.7-1.9", a union of the in-coverage scan
(1.732 +- 0.050) and a single out-of-coverage evaluation (1.85-1.89).

This script runs the scan the paper does not have: a genuine grid over
gamma_cr in [0.2, 1.0], and reports the ratio RESTRICTED to the in-lab shape's
own coverage [0.267, 0.630].

Nothing is tuned: at every grid point the amplitude A is SOLVED for, from the
fixed target f_PBH = 1e-3 (the floor of the Choudhury et al. band), exactly as
the committed script does.  The ratio is a property of the solution, not an
input.

Two shape families are used, both with the committed Eqs. 52-54 integrands:
  L  lognormal(Delta, r_p k_p) -- the committed family, extended to broad Delta
  P  in-lab power law Delta^2 = A (k/k_p)^{n_s-1} with an explicit IR cutoff
     k_min/k_p -- the family the lab's own spectrum belongs to; gamma_cr is
     driven by the IR cutoff of sigma_r (see row11_choudhury_sign.py part C)

The committed integrator's k-grid spans [1e-5, 1e3] k_p, which floors gamma_cr
at 0.267 for family P.  `_cov_wide` is the SAME three integrals on a wider grid
[1e-9, 1e3] k_p; it is validated against `PC.covariances` before use.

Venue: local CPU, minutes, $0.
Outputs: results/row11_gammacr_extension.json, results/row11_gammacr_extension.png
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import pbh_compaction_fnl as PC  # noqa: E402

RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)
OUTJSON = RESULTS / "row11_gammacr_extension.json"
OUTPNG = RESULTS / "row11_gammacr_extension.png"

F16, F8 = -35.0 / 16.0, -35.0 / 8.0
C_TH_SCAN = [0.4, 0.5, 0.6]
TARGET_FPBH = 1.0e-3
INLAB_COVERAGE = (0.267, 0.630)         # R5_18_GAMMACR_NOTE_2026-09-04.md
_ORIG_COV, _ORIG_SPEC = PC.covariances, PC.delta2_zeta


def _cov_wide(A, rp, kp=1.0, nk=12000, dl=None):
    """Choudhury et al. Eqs. 52-54, verbatim, on a k-grid widened to 1e-9 k_p."""
    k = np.logspace(np.log10(kp) - 9.0, np.log10(kp) + 3.0, nk)
    lnk = np.log(k)
    d2 = PC.delta2_zeta(k, A, kp, dl) * PC.transfer(k, rp) ** 2
    wg, ws = PC.W_gauss(k, rp), PC.W_sph(k, rp)
    s_c2 = 4.0 * (PC.F_W / 3.0) ** 2 * simpson((k * rp) ** 4 * wg ** 2 * d2, x=lnk)
    s_r2 = simpson(ws ** 2 * d2, x=lnk)
    s_cr2 = 2.0 * (PC.F_W / 3.0) * simpson((k * rp) ** 2 * wg * ws * d2, x=lnk)
    sc, sr = np.sqrt(s_c2), np.sqrt(s_r2)
    return sc, sr, s_cr2, float(np.clip(s_cr2 / (sc * sr), -0.999999, 0.999999))


def _powerlaw(ns, ir_cut):
    def d2(k, A, kp=1.0, dl=None):
        kk = np.asarray(k, dtype=float) / kp
        out = A * kk ** (ns - 1.0)
        return np.where(kk < ir_cut, 0.0, out) if ir_cut > 0 else out
    return d2


def _validate_wide():
    """_cov_wide must reproduce the committed integrator on the committed family."""
    worst = 0.0
    for dl, rpk in [(0.35, 1.5), (0.5, 1.0), (0.8, 0.75), (0.35, 0.75)]:
        PC.DL = dl
        a, b = _ORIG_COV(0.1, rpk, 1.0), _cov_wide(0.1, rpk, 1.0)
        worst = max(worst, max(abs(x - y) / abs(x) for x, y in zip(a[:2] + (a[3],),
                                                                  b[:2] + (b[3],))))
    PC.DL = 0.5
    return worst


def _point(c_th, rpk):
    """Solve for the required amplitude at each f_NL; return the ratio."""
    _, _, _, g = PC.covariances(0.1, rpk, 1.0)
    a0 = PC.A_for_fpbh(TARGET_FPBH, 0.0, c_th, rpk, 1e-5, 200.0)
    a16 = PC.A_for_fpbh(TARGET_FPBH, F16, c_th, rpk, 1e-5, 200.0)
    a8 = PC.A_for_fpbh(TARGET_FPBH, F8, c_th, rpk, 1e-5, 200.0)
    r = (a16 / a8) if (a16 and a8) else None
    return {"gamma_cr": g, "C_th": c_th, "rp_kp": rpk,
            "A_gaussian": a0, "A_-35/16": a16, "A_-35/8": a8,
            "ratio_-35/16_over_-35/8": r}


def main():
    t0 = time.time()
    print("=" * 78)
    print("ROW 11(b): compaction scan extended to gamma_cr in [0.2, 1.0]")
    print("=" * 78)
    w = _validate_wide()
    print(f"wide-grid integrator vs committed integrator: max rel. diff "
          f"{w:.2e} (must be << 1e-6)")
    assert w < 1e-6, "wide-grid integrator does not reproduce the committed one"
    out = {"task": "ledger row 11(b) -- gamma_cr in [0.2,1.0] compaction scan",
           "date": "2026-09-04", "script": Path(__file__).name,
           "target_f_PBH": TARGET_FPBH, "C_th_scan": C_TH_SCAN,
           "inlab_coverage_gamma_cr": list(INLAB_COVERAGE),
           "wide_integrator_validation_max_rel_diff": w, "points": []}

    PC.covariances = _cov_wide
    try:
        print("\n--- family L: lognormal(Delta, r_p k_p) ---")
        print(f"  {'Delta':>6}{'rp*kp':>7}{'C_th':>6}{'gamma_cr':>10}"
              f"{'A(0)':>10}{'A(-35/16)':>11}{'A(-35/8)':>10}{'ratio':>8}")
        for dl in [0.35, 0.5, 0.8, 1.2, 1.8, 2.5, 3.5, 6.0, 10.0]:
            PC.DL = dl
            for rpk in [0.3, 0.5, 0.75, 1.0, 1.5]:
                for ct in C_TH_SCAN:
                    p = _point(ct, rpk)
                    p.update({"family": "lognormal", "Delta": dl})
                    out["points"].append(p)
                    if p["ratio_-35/16_over_-35/8"]:
                        print(f"  {dl:>6}{rpk:>7}{ct:>6}{p['gamma_cr']:>10.4f}"
                              f"{p['A_gaussian']:>10.4f}{p['A_-35/16']:>11.4f}"
                              f"{p['A_-35/8']:>10.4f}"
                              f"{p['ratio_-35/16_over_-35/8']:>8.4f}")
        PC.DL = 0.5

        print("\n--- family P: in-lab power law, IR cutoff scanned ---")
        print(f"  {'n_s':>8}{'k_min/k_p':>11}{'rp*kp':>7}{'C_th':>6}"
              f"{'gamma_cr':>10}{'A(0)':>10}{'A(-35/16)':>11}"
              f"{'A(-35/8)':>10}{'ratio':>8}")
        for ns in [0.9649, 1.0]:
            for irc in [1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 3e-2,
                        1e-1, 3e-1]:
                PC.delta2_zeta = _powerlaw(ns, irc)
                for rpk in [0.75, 1.0]:
                    for ct in C_TH_SCAN:
                        p = _point(ct, rpk)
                        p.update({"family": "powerlaw", "n_s": ns,
                                  "k_min_over_k_p": irc})
                        out["points"].append(p)
                        if p["ratio_-35/16_over_-35/8"]:
                            print(f"  {ns:>8}{irc:>11.0e}{rpk:>7}{ct:>6}"
                                  f"{p['gamma_cr']:>10.4f}{p['A_gaussian']:>10.4f}"
                                  f"{p['A_-35/16']:>11.4f}{p['A_-35/8']:>10.4f}"
                                  f"{p['ratio_-35/16_over_-35/8']:>8.4f}")
    finally:
        PC.covariances, PC.delta2_zeta = _ORIG_COV, _ORIG_SPEC
        PC.DL = 0.5

    ok = [p for p in out["points"] if p["ratio_-35/16_over_-35/8"]]
    g = np.array([p["gamma_cr"] for p in ok])
    r = np.array([p["ratio_-35/16_over_-35/8"] for p in ok])

    def stats(mask, label):
        if mask.sum() == 0:
            return None
        s = {"label": label, "n": int(mask.sum()),
             "gamma_cr_range": [float(g[mask].min()), float(g[mask].max())],
             "mean": float(r[mask].mean()), "std": float(r[mask].std()),
             "min": float(r[mask].min()), "max": float(r[mask].max())}
        print(f"  {label:<34} n={s['n']:>3}  gamma_cr [{s['gamma_cr_range'][0]:.3f},"
              f" {s['gamma_cr_range'][1]:.3f}]  ratio {s['mean']:.3f} "
              f"+- {s['std']:.3f}  [{s['min']:.3f}, {s['max']:.3f}]")
        return s

    print("\n--- required-amplitude ratio A(-35/16)/A(-35/8) ---")
    out["summary"] = {
        "all": stats(np.ones_like(g, bool), "full extended scan"),
        "inlab_coverage": stats((g >= INLAB_COVERAGE[0]) & (g <= INLAB_COVERAGE[1]),
                                "INSIDE in-lab [0.267,0.630]"),
        "committed_grid_coverage": stats((g >= 0.766) & (g <= 0.968),
                                         "committed grid [0.766,0.968]"),
        "below_committed": stats(g < 0.766, "below committed coverage"),
    }
    out["survives_1.7_to_1.9"] = bool(r.min() >= 1.7 and r.max() <= 1.9)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7.2, 4.4))
        for fam, m, c in [("lognormal", "o", "#1f77b4"),
                          ("powerlaw", "s", "#d62728")]:
            sel = [i for i, p in enumerate(ok) if p["family"] == fam]
            ax.scatter(g[sel], r[sel], marker=m, s=22, alpha=0.75, c=c,
                       label=f"{fam} family")
        ax.axvspan(*INLAB_COVERAGE, color="0.85", zorder=0,
                   label=r"in-lab shape $\gamma_{\rm cr}$")
        ax.axvspan(0.766, 0.968, color="#ffe9c4", zorder=0,
                   label="committed 27-pt grid")
        ax.axhspan(1.7, 1.9, color="green", alpha=0.10, zorder=0,
                   label='quoted "1.7-1.9"')
        ax.set_xlabel(r"$\gamma_{\rm cr}=\sigma_{cr}^2/(\sigma_c\sigma_r)$")
        ax.set_ylabel(r"$A(-35/16)\,/\,A(-35/8)$")
        ax.set_title("Row 11(b): required-amplitude ratio over the extended "
                     r"$\gamma_{\rm cr}$ scan", fontsize=10)
        ax.legend(fontsize=7, loc="best")
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(OUTPNG, dpi=150)
        out["png"] = str(OUTPNG.relative_to(HERE.parents[2]))
    except Exception as e:                                    # pragma: no cover
        out["png_error"] = repr(e)

    json.dump(out, open(OUTJSON, "w"), indent=1)
    print(f"\n[{time.time()-t0:.1f}s] wrote {OUTJSON}")


if __name__ == "__main__":
    main()
