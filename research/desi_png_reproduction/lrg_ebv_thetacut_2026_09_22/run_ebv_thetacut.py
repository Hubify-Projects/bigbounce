#!/usr/bin/env python3
"""Lane LS14 -- ledger row 4: re-test the LRG E(B-V) systematic at
0.8 < z < 1.1 on the official `_thetacut0.05` products, exactly as
pre-registered (PRE_REGISTRATION.md, committed before any statistic).

Four computations, in the pre-registered order:

  G  gate     -- reproduce LS11's published untreated E(B-V) row with this
                 lane's code before any thetacut number is believed.
  A  anchor   -- official full-sample z0.8-1.1 fit on the COMPLETE thetacut
                 triple vs the COMPLETE untreated triple. Approximation-free.
  D1 primary  -- E(B-V) split fit on the thetacut convention: each cap's half
                 put on the thetacut convention by that cap's official
                 transfer T_ell^C, then thetacut window + thetacut covariance.
  D2 diagnostic (labelled inconsistent) -- thetacut window + covariance on the
                 UNTREATED split data vectors.
  V  validation -- D1 with the two caps' transfers swapped.

Every fit goes through ../lrg_channel_2026_09_22/lrg_fit_core.py unchanged,
on LS11's grid and LS11's k-range; the only new arithmetic is the transfer
multiplication, which is asserted to reduce bitwise to LS11's
fit_lrg_splits.combine_caps when the transfer is identically 1.
"""
import json
import os
import sys
import time

import numpy as np

HERE = "/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/desi_png_reproduction"
LANE = f"{HERE}/lrg_ebv_thetacut_2026_09_22"
sys.path.insert(0, HERE)
sys.path.insert(0, f"{HERE}/lrg_channel_2026_09_22")
sys.path.insert(0, LANE)

import lrg_fit_core as core            # noqa: E402  LS11, unmodified
import fit_lrg_splits as ls11          # noqa: E402  LS11, unmodified
from fit_lrg_headline import cosmo_at  # noqa: E402  LS11, unmodified
import thetacut_io as tio              # noqa: E402
import http_stream as hs               # noqa: E402

OUT = f"{LANE}/outputs"
PK = f"{HERE}/lrg_channel_2026_09_22/outputs/pk"
ZB = "0.8-1.1"
PROP = "EBV"
GRID = np.linspace(-400, 400, 801)     # LS11's split grid, unchanged
KMIN, KMAX = 0.003, 0.08               # LS11 / v5 convention, unchanged
CLIP4 = (0.5, 1.5)                     # pre-registered ell=4 transfer clip

# LS11's published untreated E(B-V) z0.8-1.1 row (LEDGER4_LRG_RESULT_2026-09-22.md)
LS11_ROW = dict(high=-17.62, low=-0.27, delta=-17.35, sigma_delta=12.32,
                raw=-1.41, corr=-0.995)


# ---------------------------------------------------------------- transfers
def build_transfers():
    """T_ell^C(k) = P_ell^{C,thetacut} / P_ell^{C,untreated} on the official
    fine k grid, per cap. ell=4 clipped to CLIP4 (P_4 crosses zero)."""
    T, meta = {}, {}
    for cap in ("NGC", "SGC"):
        m0 = tio.load_measured(tio.UNTREATED, cap=cap)
        m1 = tio.load_measured(tio.THETACUT, cap=cap)
        T[cap], meta[cap] = {}, {}
        for ell in (0, 2, 4):
            k = np.asarray(m0[ell]["k"], float)
            r = np.asarray(m1[ell]["value"], float) / np.asarray(m0[ell]["value"], float)
            inrange = np.isfinite(k) & (k >= KMIN) & (k <= KMAX)
            if ell == 4:
                bad = inrange & ((r < CLIP4[0]) | (r > CLIP4[1]))
                meta[cap][ell] = dict(n_fine_in_range=int(inrange.sum()),
                                      n_clipped_in_range=int(bad.sum()))
                r = np.clip(r, *CLIP4)
            else:
                meta[cap][ell] = dict(
                    n_fine_in_range=int(inrange.sum()),
                    ratio_min=float(np.nanmin(r[inrange])),
                    ratio_med=float(np.nanmedian(r[inrange])),
                    ratio_max=float(np.nanmax(r[inrange])))
            good = np.isfinite(k) & np.isfinite(r)
            T[cap][ell] = (k[good], r[good])
    # geometry dependence of the transfer between the two caps
    for ell in (0, 2):
        kN, rN = T["NGC"][ell]
        kS, rS = T["SGC"][ell]
        m = (kN >= KMIN) & (kN <= KMAX)
        meta.setdefault("cap_spread", {})[ell] = float(
            np.max(np.abs(rN[m] - np.interp(kN[m], kS, rS))))
    return T, meta


def apply_T(k_split, vals, Tell):
    """Multiply a measured split multipole by the interpolated transfer."""
    kk, rr = Tell
    f = np.interp(k_split, kk, rr)
    f = np.where(np.isfinite(k_split), f, 1.0)
    return vals * f


def combine_caps_T(zb, prop, half, Tmap):
    """LS11's fit_lrg_splits.combine_caps, with each cap's multipoles put on
    the thetacut convention BEFORE the n_data-weighted NGC+SGC mean.
    Tmap=None reproduces combine_caps bitwise (asserted in main)."""
    parts = {}
    for cap in ("NGC", "SGC"):
        p = f"{PK}/pk_LRG_z{zb}_{cap}_{prop}_{half}.json"
        if not os.path.exists(p):
            return None
        parts[cap] = json.load(open(p))
    n, s = parts["NGC"], parts["SGC"]
    k = np.array(n["k"])
    wN, wS = n["n_data"], s["n_data"]
    comb = {}
    for ell, key in ((0, "p0"), (2, "p2"), (4, "p4")):
        vN, vS = np.array(n[key]), np.array(s[key])
        if Tmap is not None:
            vN = apply_T(k, vN, Tmap["NGC"][ell])
            vS = apply_T(np.array(s["k"]), vS, Tmap["SGC"][ell])
        comb[ell] = (wN * vN + wS * vS) / (wN + wS)
    nmodes = np.array(n["nmodes"]) + np.array(s["nmodes"])
    return k, comb, nmodes, wN + wS


# --------------------------------------------------------------------- fits
def split_row(basis, cov, cov_kedges, krange, zb, prop, Tmap):
    halves = {}
    for half in ("high", "low"):
        c = combine_caps_T(zb, prop, half, Tmap)
        if c is None:
            return {"status": "NOT RUN -- P(k) measurement missing"}
        k, comb, nm, ntot = c
        dvec = np.concatenate([core.rebin(k, comb[ell], nm, cov_kedges[ell])
                               for ell in (0, 2, 4)])
        mask = np.isfinite(dvec) & krange
        cinv = np.linalg.inv(cov[np.ix_(mask, mask)])
        chi2, b1s = core.profile_from_basis(basis, dvec, cinv, mask)
        best, lo, hi, sig = core.interval(GRID, chi2)
        i = int(np.argmin(chi2))
        halves[half] = dict(f_nl=best, sigma=sig, b1=float(b1s[i]),
                            chi2=float(chi2[i]), n_bins=int(mask.sum()),
                            chi2_per_dof=float(chi2[i] / (mask.sum() - 2)),
                            n_data=int(ntot))
    dh, dl = halves["high"]["f_nl"], halves["low"]["f_nl"]
    sh, sl = halves["high"]["sigma"], halves["low"]["sigma"]
    delta = dh - dl
    sd = float(np.sqrt(sh ** 2 + sl ** 2))
    raw = delta / sd
    corr = raw / np.sqrt(2.0)
    return dict(high=halves["high"], low=halves["low"], delta_fnl=delta,
                sigma_delta=sd, delta_over_sigma=raw,
                delta_over_sigma_sqrt2corrected=corr,
                verdict=ls11.verdict(corr))


def anchor_fit(basis, meas, cov, cov_kedges, krange):
    dvec = np.concatenate([
        core.rebin(np.asarray(meas[ell]["k"], float),
                   np.asarray(meas[ell]["value"], float),
                   meas[ell]["nmodes"], cov_kedges[ell]) for ell in (0, 2, 4)])
    mask = np.isfinite(dvec) & krange
    cinv = np.linalg.inv(cov[np.ix_(mask, mask)])
    chi2, b1s = core.profile_from_basis(basis, dvec, cinv, mask)
    best, lo, hi, sig = core.interval(GRID, chi2)
    i = int(np.argmin(chi2))
    return dict(f_nl=best, lo_68=lo, hi_68=hi, sigma=sig, b1=float(b1s[i]),
                chi2_min=float(chi2[i]), n_bins=int(mask.sum()),
                chi2_per_dof=float(chi2[i] / (mask.sum() - 2)))


def main():
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    RES = f"{OUT}/ebv_thetacut_z0.8-1.1.json"
    res = {"lane": "LS14-row4-ebv", "zbin": ZB, "prop": PROP,
           "grid": "np.linspace(-400,400,801) -- LS11's split grid",
           "k_range": [KMIN, KMAX]}
    if os.path.exists(RES):          # resumable: a completed variant is skipped
        res = json.load(open(RES))
        print("[resume] existing:", [k for k in ("untreated", "thetacut0.05")
                                     if k in res], flush=True)

    # ---- transfers (official cap spectra only)
    T, tmeta = build_transfers()
    res["transfer"] = tmeta
    print("[transfer]", json.dumps(tmeta, indent=1)[:900], flush=True)

    # ---- identity check: combine_caps_T(None) == LS11's combine_caps, bitwise
    for half in ("high", "low"):
        a = combine_caps_T(ZB, PROP, half, None)
        b = ls11.combine_caps(ZB, PROP, half)
        eq = lambda x, y: np.array_equal(np.asarray(x, float),
                                         np.asarray(y, float), equal_nan=True)
        assert eq(a[0], b[0]) and a[3] == b[3]
        for ell in (0, 2, 4):
            assert eq(a[1][ell], b[1][ell]), (half, ell)
        assert eq(a[2], b[2])
    res["identity_check"] = ("combine_caps_T(Tmap=None) reproduces LS11's "
                             "fit_lrg_splits.combine_caps bitwise for both halves")
    print("[identity] bitwise OK", flush=True)

    Tswap = {"NGC": T["SGC"], "SGC": T["NGC"]}

    for variant, vname in ((tio.UNTREATED, "untreated"), (tio.THETACUT, "thetacut0.05")):
        if vname in res and all(str(p) in res[vname] for p in (1.0, 1.6)):
            print(f"[skip] {vname} already complete", flush=True)
            continue
        W, theory_k, obs_k, _ = tio.load_window(variant)
        meas = tio.load_measured(variant)
        cov, cov_kedges, cov_kc = tio.load_covariance(variant)
        nmodes = {ell: meas[ell]["nmodes"] for ell in (0, 2, 4)}
        mg = core.ModelGrid(W, theory_k, obs_k, nmodes, cov_kedges)
        kc = np.concatenate([cov_kc[ell] for ell in (0, 2, 4)])
        krange = (kc >= KMIN) & (kc <= KMAX)
        res.setdefault(vname, {})["zeff"] = meas["zeff"]
        for p in (1.0, 1.6):
            a_fn, pl_fn, f_g, _ = cosmo_at(meas["zeff"])
            ts = time.time()
            basis = mg.basis(a_fn, pl_fn, f_g, GRID, p)
            print(f"[basis] {vname} p={p} in {time.time()-ts:.0f}s "
                  f"(streamed {hs.BYTES_STREAMED['n']/1e6:.0f} MB)", flush=True)
            blk = res[vname].setdefault(str(p), {})
            blk["anchor"] = anchor_fit(basis, meas, cov, cov_kedges, krange)
            print(f"  A  {vname} p={p}: full-sample f_NL="
                  f"{blk['anchor']['f_nl']:+.3f} +/- {blk['anchor']['sigma']:.3f} "
                  f"b1={blk['anchor']['b1']:.4f} "
                  f"chi2/dof={blk['anchor']['chi2_per_dof']:.3f}", flush=True)
            if vname == "untreated":
                blk["G_gate"] = split_row(basis, cov, cov_kedges, krange, ZB, PROP, None)
                tag = [("G_gate", blk["G_gate"])]
            else:
                blk["D2_diagnostic_inconsistent"] = split_row(
                    basis, cov, cov_kedges, krange, ZB, PROP, None)
                blk["D1_primary"] = split_row(
                    basis, cov, cov_kedges, krange, ZB, PROP, T)
                blk["V_swapped_cap"] = split_row(
                    basis, cov, cov_kedges, krange, ZB, PROP, Tswap)
                tag = [("D2_diagnostic_inconsistent", blk["D2_diagnostic_inconsistent"]),
                       ("D1_primary", blk["D1_primary"]),
                       ("V_swapped_cap", blk["V_swapped_cap"])]
            for name, r in tag:
                print(f"  {name:<28} p={p}: high={r['high']['f_nl']:+.2f}"
                      f"+/-{r['high']['sigma']:.2f} low={r['low']['f_nl']:+.2f}"
                      f"+/-{r['low']['sigma']:.2f} d={r['delta_fnl']:+.2f} "
                      f"sd={r['sigma_delta']:.2f} raw={r['delta_over_sigma']:+.3f} "
                      f"corr={r['delta_over_sigma_sqrt2corrected']:+.3f} "
                      f"-> {r['verdict']}", flush=True)
            del basis
            json.dump(res, open(RES, "w"), indent=2)
        del W, mg

    # ---- gate verdict (pre-registered tolerances)
    g = res["untreated"]["1.0"]["G_gate"]
    dcorr = abs(g["delta_over_sigma_sqrt2corrected"] - LS11_ROW["corr"])
    dhi = abs(g["high"]["f_nl"] - LS11_ROW["high"])
    dlo = abs(g["low"]["f_nl"] - LS11_ROW["low"])
    res["gate"] = dict(ls11_published=LS11_ROW, reproduced_corr=g["delta_over_sigma_sqrt2corrected"],
                       d_corr=dcorr, d_high=dhi, d_low=dlo,
                       tolerance=dict(corr=0.02, half_fnl=0.05),
                       passed=bool(dcorr <= 0.02 and dhi <= 0.05 and dlo <= 0.05))
    print(f"[GATE] d_corr={dcorr:.4f} d_high={dhi:.4f} d_low={dlo:.4f} "
          f"-> {'PASS' if res['gate']['passed'] else 'FAIL'}", flush=True)

    # ---- robustness rule
    for p in ("1.0", "1.6"):
        d1 = res["thetacut0.05"][p]["D1_primary"]
        v = res["thetacut0.05"][p]["V_swapped_cap"]
        res["thetacut0.05"][p]["robustness"] = dict(
            eps_T=abs(d1["delta_over_sigma_sqrt2corrected"]
                      - v["delta_over_sigma_sqrt2corrected"]),
            verdict_D1=d1["verdict"], verdict_V=v["verdict"],
            robust=bool(d1["verdict"] == v["verdict"]))
        a_u = res["untreated"][p]["anchor"]["f_nl"]
        a_t = res["thetacut0.05"][p]["anchor"]["f_nl"]
        res["thetacut0.05"][p]["delta_theta_full_sample"] = a_t - a_u

    res.setdefault("streamed_bytes_runs", []).append(int(hs.BYTES_STREAMED["n"]))
    res["streamed_bytes"] = int(sum(res["streamed_bytes_runs"]))
    res.setdefault("sha256", {}).update(tio.SHA256)
    res["wall_seconds"] = round(time.time() - t0, 1)
    res["streamed_bytes_note"] = ("bytes streamed by THIS process; a resumed "
                                  "run re-streams the variant it computes")
    with open(RES, "w") as f:
        json.dump(res, f, indent=2)
    print(f"streamed {res['streamed_bytes']/1e6:.0f} MB, {res['wall_seconds']:.0f}s")
    print("DONE")


if __name__ == "__main__":
    main()
