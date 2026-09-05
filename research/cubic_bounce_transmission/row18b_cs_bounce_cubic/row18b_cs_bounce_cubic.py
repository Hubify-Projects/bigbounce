#!/usr/bin/env python3
"""Ledger row 18(b) / A3-cs-bounce: c_s-dependence of the bounce's own cubic term.

Question: row 14 evaluated the joint (r, f_NL) window with f_NL^pre(c_s) =
-165/16 + 65/(8 c_s^2), a c_s-independent transmission T, and the bounce's own
cubic contribution frozen at its c_s = 1 value.  This lane carries the SAME c_s
through the bounce vertices, so that

    f_NL^after(c_s) = T * f_NL^pre(c_s) + Delta f_NL^bounce(c_s).

Scheme S1 (geometric): z = a exactly, so z''/z = a''/a is c_s-independent and the
Mukhanov-Sasaki equation is mu'' + (c_s^2 k^2 - a''/a) mu = 0.  c_s therefore enters
the S1 MODE FUNCTIONS ONLY through the sound horizon: the problem at physical
wavenumber k with sound speed c_s IS the c_s = 1 problem at wavenumber k_s = c_s k,
and the Bunch-Davies normalisation |v| -> 1/sqrt(2 c_s k) is exactly what the
Wronskian condition Im(v* v') = -1/2 gives for that equation (no extra 1/sqrt(c_s)).
Implemented literally: mode functions are evolved at k_s = c_s k while every momentum
kernel and dot product uses the PHYSICAL k.

c_s enters everywhere else through the lane (a) vertex coefficients, kept exactly as
tabulated, with the S1 substitutions eps -> eps_eff = 1/2, eta_sr -> 0, s -> 0
(constant c_s), lambda -> 0.  This is the c_s extension of lane (a) assumption (A3).

Nothing here is tuned.  The c_s = 1 gate must reproduce the lane (b) totals.
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "lane_b_numerical"))
import a2_transmission_linear as a2                      # noqa: E402
import bounce_cubic_inin as lb                           # noqa: E402

LOG = os.path.join(HERE, "row18b_cs_bounce_cubic.log")
JSON_OUT = os.path.join(HERE, "results.json")
_lines = []


def log(m=""):
    print(m)
    _lines.append(m)


EPS = 0.5          # S1 eps_eff
KT_REF = 1e-3      # k eta_B
SQUEEZE = 0.02
CS_GRID = [0.44, 0.6, 0.8876, 1.0]
PLANCK_1SIG = 5.1
FNL_PRE_C1 = -165.0 / 16.0
FNL_PRE_C2 = 65.0 / 8.0


def fnl_pre(cs):
    """Row 14 / Li+2016 Eq. (4.19) isoceles squeezed limit."""
    return FNL_PRE_C1 + FNL_PRE_C2 / cs ** 2


# ---- S1 vertex coefficients with c_s retained (lane (a) table, eps -> 1/2) ----
def coeffs(a, aH, cs):
    c2, c4 = cs ** 2, cs ** 4
    return {
        "V1": -aH * EPS * (1.0 / c2 - 1.0 / c4) + 0.0 * a,          # -a^3/H * Sigma(1-1/c_s^2)
        "V2": a ** 2 * EPS * (EPS - 3.0 + 3.0 * c2) / c4,
        "V3": EPS * (EPS + 1.0 - c2) / c2 + 0.0 * a,
        "V4": -2.0 * a ** 2 * EPS ** 2 / c4,
        "V5": 0.0 * a,
        "V6": a ** 2 * EPS ** 3 / (2.0 * c4),
        "V7": a ** 2 * EPS ** 3 / (4.0 * c4),
    }


def redef_F(a, H, cs):
    return {"R1": 0.0, "R2": 1.0 / (cs ** 2 * H),
            "R3": 1.0 / (4.0 * a ** 2 * H ** 2), "R4": EPS / (2.0 * cs ** 2 * H)}


def vertex_fnl_cs(bg, modes, ks, D, e1, e2, eta_star, cs, npts=4001):
    """Bulk in-in f_NL per vertex, lane (b) conventions, coefficients at general c_s."""
    eta = np.linspace(e1, e2, npts)
    a = bg["af"](eta)
    aH = bg["af"].derivative()(eta) / a                       # a H = a'/a
    z, dz = zip(*[m.zeta_dz(eta) for m in modes])
    zs = [m.zeta_dz(eta_star)[0] for m in modes]
    pref = zs[0] * zs[1] * zs[2]
    P = [float(abs(v) ** 2) for v in zs]
    Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
    cc = coeffs(a, aH, cs)
    out = {}
    for name, V in lb.VERTICES.items():
        tot = np.zeros_like(eta, dtype=complex)
        for (i, j, l) in lb.PERMS:
            amp = np.ones_like(eta, dtype=complex)
            for slot, leg in zip(V["slots"], (i, j, l)):
                amp = amp * (np.conj(z[leg]) if slot == "z" else np.conj(dz[leg]))
            tot = tot + V["kern"](i, j, l, ks, D) * amp
        B = -2.0 * float(np.imag(pref * lb._simps_c(cc[name] * tot, eta)))
        out[name] = 5.0 / 6.0 * B / Psum
    return out, Psum


def redef_fnl_cs(bg, modes, ks, D, eta_star, cs):
    a = float(bg["af"](eta_star))
    H = float(bg["af"].derivative()(eta_star)) / a ** 2
    vals = [m.zeta_dz(eta_star) for m in modes]
    Q = {}
    for i, (z, dz) in enumerate(vals):
        Q[("z", i)] = float(abs(z) ** 2)
        Q[("d", i)] = float(np.real(dz / a * np.conj(z)))
    P = [Q[("z", i)] for i in range(3)]
    Psum = P[0] * P[1] + P[0] * P[2] + P[1] * P[2]
    FF = redef_F(a, H, cs)
    out = {}
    for name, R in lb.REDEF.items():
        B = 0.0
        for c in range(3):
            p, q = [x for x in range(3) if x != c]
            for (pp, qq) in [(p, q), (q, p)]:
                B += FF[name] * R["kern"](c, pp, qq, ks, D) \
                     * Q[(R["slots"][0], pp)] * Q[(R["slots"][1], qq)]
        out[name] = 5.0 / 6.0 * B / Psum
    return out


def dfnl_bounce(bg, cs, kt=KT_REF, npts=4001):
    """Delta f_NL^bounce at sound speed cs; modes at k_s = cs*k, kernels at k."""
    eB = bg["eta_B"]
    k = kt / eB
    ks = np.array([SQUEEZE * k, k, k])
    D = lb._dots(*ks)
    eta_far = min(0.9 * bg["eta_far"], 300.0 * eB)
    modes = [lb.Modes(bg, cs * kk, eta_far) for kk in ks]
    assert all(m.ev["success"] for m in modes)
    wr = [m.wronskian(0.0) for m in modes]
    esf = min(150.0, 0.05 / (cs * kt), 0.85 * eta_far / eB)
    eta_star = esf * eB
    fv, _ = vertex_fnl_cs(bg, modes, ks, D, -eB, eB, eta_star, cs, npts=npts)
    fr = redef_fnl_cs(bg, modes, ks, D, eta_star, cs)
    return dict(cs=cs, vertices=fv, redefinition=fr, bulk=float(sum(fv.values())),
                redef=float(sum(fr.values())), total=float(sum(fv.values()) + sum(fr.values())),
                wronskian=[float(w) for w in wr], eta_star_over_etaB=float(esf),
                cs_k_eta_star=float(cs * k * eta_star))


def main():
    t0 = time.time()
    log("=" * 78)
    log("Row 18(b) A3-cs-bounce: Delta f_NL^bounce(c_s) in scheme S1   (2026-09-04)")
    log("=" * 78)
    log("S1: z = a  =>  mu'' + (c_s^2 k^2 - a''/a) mu = 0; c_s enters the mode functions ONLY")
    log("through the sound horizon (modes evolved at k_s = c_s k, kernels at physical k).")
    log("Vertices: lane (a) table with eps -> 1/2, eta_sr -> 0, s -> 0, lambda -> 0, c_s kept.")
    log(f"Configuration: squeezed isoceles k1 = {SQUEEZE} k, k eta_B = {KT_REF}.")

    GATE = {"quintin": -0.139818, "lqc": -0.104311, "poly": -0.127111}
    bgs = {"quintin": a2.bg_quintin(dtB=1.0), "lqc": a2.bg_lqc(), "poly": a2.bg_poly(eta_b=1.0)}
    out = {"date": "2026-09-04", "row": "18(b) A3-cs-bounce",
           "scheme": "S1 (geometric, z = a, eps_eff = 1/2, eta_sr = 0, s = 0, lambda = 0; c_s retained)",
           "cs_entry": ("mode functions: only via c_s^2 k^2 (sound horizon), implemented as "
                        "k -> c_s k with the same Wronskian normalisation Im(v* v') = -1/2, "
                        "which is exactly the BD |v| -> 1/sqrt(2 c_s k); vertices: lane (a) "
                        "coefficients with c_s retained; boundary terms R2, R4 carry 1/c_s^2"),
           "fnl_pre": "f_NL^pre(c_s) = -165/16 + 65/(8 c_s^2)  (row 14 / Li+2016 Eq. 4.19)",
           "r_of_cs": "r = 16 eps c_s = 24 c_s  (row 14)",
           "cs_grid": CS_GRID, "k_etaB": KT_REF, "gate_cs1": GATE, "backgrounds": {}}

    for bkey, bg in bgs.items():
        eB, Ii = bg["eta_B"], bg["I_inf"]
        rho_B = abs(float(bg["Jf"](-eB))) / Ii
        T = 0.5 * (1.0 - rho_B)
        log(f"\n{'=' * 74}\n[{bg['label']}]  eta_B={eB:.6g}  rho_B={rho_B:.6f}  T_fNL={T:.6f}")
        brec = dict(label=bg["label"], eta_B=float(eB), rho_B=float(rho_B), T_fNL=float(T),
                    cs_scan=[])
        # --- c_s = 1 regression gate against lane (b) ---
        g = dfnl_bounce(bg, 1.0)
        rel = abs(g["total"] - GATE[bkey]) / abs(GATE[bkey])
        log(f"  [gate c_s=1] total = {g['total']:+.6f} vs lane (b) {GATE[bkey]:+.6f}  "
            f"(rel {rel:.2e})  Wronskian {np.mean(g['wronskian']):+.8f}")
        assert rel < 2e-3, f"c_s=1 gate FAILED for {bkey}: {g['total']} vs {GATE[bkey]}"
        brec["gate_cs1"] = dict(computed=g["total"], reference=GATE[bkey], rel_diff=float(rel))

        for cs in CS_GRID:
            r = dfnl_bounce(bg, cs)
            fpre = fnl_pre(cs)
            r["fnl_pre"] = float(fpre)
            r["T_fnl_pre"] = float(T * fpre)
            r["fnl_after"] = float(T * fpre + r["total"])
            r["r_tensor"] = float(24.0 * cs)
            # analytic V2 scaling check: c_V2(c_s)/c_V2(1) = (6 c_s^2 - 5)/c_s^4
            r["V2_scaling_analytic"] = float((6.0 * cs ** 2 - 5.0) / cs ** 4)
            r["V2_scaling_numeric"] = float(r["vertices"]["V2"] / g["vertices"]["V2"])
            brec["cs_scan"].append(r)
            log(f"  c_s = {cs:<7g} Delta f_NL^bounce = {r['total']:+.6g}   "
                f"(V2 {r['vertices']['V2']:+.6g}, V1 {r['vertices']['V1']:+.3g}, "
                f"V4 {r['vertices']['V4']:+.3g}, V6+V7 {r['vertices']['V6'] + r['vertices']['V7']:+.3g})")
            log(f"              f_NL^pre = {fpre:+.6g}  T*f_NL^pre = {T * fpre:+.6g}  "
                f"=> f_NL^after = {r['fnl_after']:+.6g}   r = {24 * cs:.4g}")
            log(f"              V2 coefficient scaling: numeric {r['V2_scaling_numeric']:+.6f} vs "
                f"analytic (6c_s^2-5)/c_s^4 = {r['V2_scaling_analytic']:+.6f}")

        # --- the boundary: |f_NL^after| = 5.1, with and without the bounce term ---
        D1 = g["total"]

        def f_after_model(cs):
            return T * fnl_pre(cs) + D1 * (6.0 * cs ** 2 - 5.0) / cs ** 4

        def f_after_row14(cs):
            return T * fnl_pre(cs)

        bnd = {}
        for tag, fn in (("with_bounce_term", f_after_model), ("row14_no_bounce_cs", f_after_row14)):
            try:
                cmin = brentq(lambda c: abs(fn(c)) - PLANCK_1SIG, 0.05, 0.999999, xtol=1e-12)
            except ValueError:
                cmin = float("nan")
            bnd[tag] = dict(cs_min=float(cmin), r_min=float(24.0 * cmin),
                            r_over_bk=float(24.0 * cmin / 0.036))
            log(f"  [window] |f_NL^after| <= {PLANCK_1SIG} ({tag}): c_s >= {cmin:.6f}  "
                f"=> r >= {24 * cmin:.4f}  ({24 * cmin / 0.036:.1f} x BICEP/Keck)")
        # sign flip of the full f_NL^after
        try:
            zc = brentq(f_after_model, 0.5, 0.999999, xtol=1e-12)
        except ValueError:
            zc = float("nan")
        bnd["zero_crossing_cs"] = float(zc)
        log(f"  [window] f_NL^after changes sign at c_s = {zc:.6f} "
            f"(row 14, f_NL^pre alone: 0.887567)")
        # at the tensor-viable c_s
        cs_t = 1.5e-3
        bnd["at_tensor_viable_cs"] = dict(
            cs=cs_t, r=24 * cs_t, fnl_after_row14=float(f_after_row14(cs_t)),
            fnl_after_with_bounce=float(f_after_model(cs_t)),
            bounce_term=float(D1 * (6 * cs_t ** 2 - 5) / cs_t ** 4))
        log(f"  [tensor-viable c_s = {cs_t:g}, r = 0.036]  row 14 f_NL^after = "
            f"{f_after_row14(cs_t):.4g}; with the bounce term = {f_after_model(cs_t):.4g}")
        brec["boundary"] = bnd
        brec["model"] = ("f_NL^after(c_s) = T (-165/16 + 65/(8c_s^2)) + Delta_1 (6c_s^2-5)/c_s^4, "
                         f"Delta_1 = Delta f_NL^bounce(c_s=1) = {D1:.6f} (V2-dominated, 99.97%)")
        out["backgrounds"][bkey] = brec

    out["headline"] = {
        b: dict(cs_min_row14=r["boundary"]["row14_no_bounce_cs"]["cs_min"],
                cs_min_with_bounce=r["boundary"]["with_bounce_term"]["cs_min"],
                r_min_row14=r["boundary"]["row14_no_bounce_cs"]["r_min"],
                r_min_with_bounce=r["boundary"]["with_bounce_term"]["r_min"])
        for b, r in out["backgrounds"].items()}
    out["validity"] = ("super-Hubble k eta_B << 1; constant c_s across contraction, bounce and "
                       "post-bounce; S1 scheme assumption (A3) extended to c_s != 1 (vertex eps -> "
                       "eps_eff = 1/2 while c_s is retained exactly); P(X,phi) cubic action only; "
                       "first-order in-in; f_NL^pre inherits Li+2016's kinetic sector (row 14 sec 2)")
    log(f"\nDONE ({time.time() - t0:.1f} s)")
    with open(JSON_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    with open(LOG, "w") as fh:
        fh.write("\n".join(_lines) + "\n")
    make_figure(out)


def make_figure(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cs = np.linspace(0.30, 1.0, 700)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.3))
    cols = {"quintin": "C0", "lqc": "C1", "poly": "C2"}
    for b, rec in out["backgrounds"].items():
        T, D1 = rec["T_fNL"], rec["gate_cs1"]["computed"]
        dB = D1 * (6 * cs ** 2 - 5) / cs ** 4
        pre = T * (FNL_PRE_C1 + FNL_PRE_C2 / cs ** 2)
        axes[0].plot(cs, dB, color=cols[b], label=rf"{rec['label']}  $\Delta f_{{\rm NL}}^{{\rm bounce}}$")
        axes[0].plot(cs, pre, color=cols[b], ls=":", lw=1, label=rf"{rec['label']}  $T f_{{\rm NL}}^{{\rm pre}}$")
        axes[1].plot(cs, pre + dB, color=cols[b], lw=1.8, label=rec["label"])
        axes[1].plot(cs, pre, color=cols[b], ls=":", lw=1)
        sc = [e for e in rec["cs_scan"]]
        axes[0].plot([e["cs"] for e in sc], [e["total"] for e in sc], "o", ms=4, color=cols[b])
        axes[1].plot([e["cs"] for e in sc], [e["fnl_after"] for e in sc], "o", ms=4, color=cols[b])
        axes[1].axvline(rec["boundary"]["with_bounce_term"]["cs_min"], color=cols[b], ls="--", lw=0.8)
        axes[1].axvline(rec["boundary"]["row14_no_bounce_cs"]["cs_min"], color=cols[b], ls="-.", lw=0.8)
    for ax, ttl in zip(axes, [r"bounce term vs transmitted contraction (S1)",
                              r"$f_{\rm NL}^{\rm after}(c_s)=T f_{\rm NL}^{\rm pre}+\Delta f_{\rm NL}^{\rm bounce}$"]):
        ax.set_xlabel(r"$c_s$"); ax.grid(alpha=0.3); ax.set_title(ttl, fontsize=10)
        ax.axhline(0, color="k", lw=0.6)
    axes[0].set_ylim(-15, 30); axes[0].set_ylabel(r"$f_{\rm NL}$ contribution")
    axes[0].legend(fontsize=6, ncol=1)
    axes[1].set_ylim(-8, 30); axes[1].set_ylabel(r"$f_{\rm NL}^{\rm after}$")
    axes[1].axhspan(-5.1, 5.1, color="0.85", zorder=0)
    axes[1].text(0.32, 5.4, r"Planck $1\sigma$: $|f_{\rm NL}|\leq5.1$", fontsize=7)
    axes[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "row18b_cs_bounce_cubic.png"), dpi=140)


if __name__ == "__main__":
    main()
