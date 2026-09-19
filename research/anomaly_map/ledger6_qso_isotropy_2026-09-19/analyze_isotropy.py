#!/usr/bin/env python3
"""Ledger #6 second discriminator, step 2: large-angle isotropy statistics of
the DESI DR1 QSO sample.  Everything here is specified in PREREGISTRATION.md,
which was committed (c1acb329) before this file existed.

S1 = number-count dipole (systematics diagnostic + super-horizon gradient bound)
S2 = dipolar modulation A of the degree-scale clustering amplitude, the LSS
     analogue of the Planck 2018 VII CMB modulation A ~ 0.07 toward
     (l,b) = (209 deg, -15 deg).
N1 = Poisson/selection null, N2 = random-axis (look-elsewhere) null,
N3 = systematics bracket.  CPU only, deterministic (seed fixed).
"""
import os, json, itertools
import numpy as np
import healpy as hp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "outputs")
CAPS = ["NGC", "SGC"]
SEED = 20260919
NSIM = 500
NSIDE_AXES = 16
PLANCK_LB = (209.0, -15.0)          # Planck 2018 VII dipolar modulation axis
A_CMB = 0.07                        # its amplitude, ell <~ 60


# ---------------------------------------------------------------- geometry
def gal_vectors(nside):
    """Unit vectors of pixel centres, rotated from equatorial to Galactic."""
    v = np.array(hp.pix2vec(nside, np.arange(hp.nside2npix(nside))))
    rot = hp.Rotator(coord=["C", "G"])
    return np.array(rot(v))          # shape (3, npix), Galactic


def lb_to_vec(l_deg, b_deg):
    t = np.radians(90.0 - b_deg)
    p = np.radians(l_deg)
    return np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])


# ---------------------------------------------------------------- sample
def load_sample(nside, nosys=False, mask_frac=0.5, bcut=None, joint_alpha=False):
    z = np.load(f"{OUT}/maps_nside{nside}.npz")
    pre = "ns" if nosys else ""
    V = gal_vectors(nside)
    b_gal = np.degrees(np.arcsin(np.clip(V[2], -1, 1)))
    rows = []
    for cap in CAPS:
        D = z[f"D{pre}_{cap}"]; Q = z[f"Q{pre}_{cap}"]; R = z[f"R{pre}_{cap}"]
        occ = R > 0
        thr = mask_frac * np.median(R[occ])
        m = R >= thr
        if bcut is not None:
            m &= np.abs(b_gal) > bcut
        rows.append((cap, m, D, Q, R))
    if joint_alpha:
        alpha = sum(r[2][r[1]].sum() for r in rows) / sum(r[4][r[1]].sum() for r in rows)
        alphas = {r[0]: alpha for r in rows}
    else:
        alphas = {r[0]: r[2][r[1]].sum() / r[4][r[1]].sum() for r in rows}
    idx, cap_id, delta, shot = [], [], [], []
    for k, (cap, m, D, Q, R) in enumerate(rows):
        a = alphas[cap]
        i = np.where(m)[0]
        idx.append(i); cap_id.append(np.full(i.size, k))
        delta.append(D[i] / (a * R[i]) - 1.0)
        shot.append(Q[i] / (a * R[i]) ** 2)
    idx = np.concatenate(idx); cap_id = np.concatenate(cap_id)
    return dict(nside=nside, idx=idx, cap=cap_id, delta=np.concatenate(delta),
                shot=np.concatenate(shot), vec=V[:, idx], b=b_gal[idx],
                alphas=alphas, npix_cap=[int((cap_id == k).sum()) for k in range(2)],
                pix_area_deg2=hp.nside2pixarea(nside, degrees=True))


# ---------------------------------------------------------------- S1
def fit_dipole(S, niter=6, shared_monopole=False):
    """delta_i = m_cap + d.n_i, weights 1/(shot + sigma2_cap); sigma2_cap set by chi2/dof=1."""
    d, s, cap, V = S["delta"], S["shot"], S["cap"], S["vec"]
    n = d.size
    sig2 = np.zeros(2)
    if shared_monopole:                       # one monopole for both caps
        X = np.column_stack([np.ones(n), V[0], V[1], V[2]])
        j0 = 1
    else:
        X = np.column_stack([(cap == 0).astype(float), (cap == 1).astype(float), V[0], V[1], V[2]])
        j0 = 2
    for _ in range(niter):
        W = 1.0 / (s + sig2[cap])
        XtW = X.T * W
        beta = np.linalg.solve(XtW @ X, XtW @ d)
        r = d - X @ beta
        for k in range(2):
            sel = cap == k
            if not np.any(sel):
                sig2[k] = 0.0
                continue
            lo, hi = 0.0, 1.0
            f = lambda v: np.sum(r[sel] ** 2 / (s[sel] + v)) - (sel.sum() - X.shape[1] / 2.0)
            if f(0.0) <= 0:
                sig2[k] = 0.0
                continue
            while f(hi) > 0:
                hi *= 2
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if f(mid) > 0: lo = mid
                else: hi = mid
            sig2[k] = 0.5 * (lo + hi)
    W = 1.0 / (s + sig2[cap])
    cov = np.linalg.inv((X.T * W) @ X)
    dip = beta[j0:j0 + 3]
    err = np.sqrt(np.diag(cov)[j0:j0 + 3])
    return dict(monopole=beta[:j0].tolist(), dipole=dip.tolist(), dipole_err=err.tolist(),
                amp=float(np.linalg.norm(dip)),
                amp_err=float(np.sqrt(dip @ (cov[j0:j0 + 3, j0:j0 + 3] @ dip)) / max(np.linalg.norm(dip), 1e-30)),
                sigma2_cap=sig2.tolist(),
                chi2_dof=float(np.sum(W * (d - X @ beta) ** 2) / (n - X.shape[1])))


# ---------------------------------------------------------------- S2
def fit_modulation(S, phat, niter=30, a_init=None):
    """e_i = delta_i^2 - shot_i ;  <e_i> = a_cap (1 + 2 A x_i), x_i = n_i.phat."""
    e = S["delta"] ** 2 - S["shot"]
    x = phat @ S["vec"]
    cap, s = S["cap"], S["shot"]
    if a_init is not None:
        a = np.array(a_init, dtype=float)
    else:
        a = np.array([max(float(np.mean(e[cap == k])), 1e-8) if np.any(cap == k) else 1e-8
                      for k in range(2)])
    A = 0.0
    for _ in range(niter):
        W = 1.0 / (2.0 * (a[cap] + s) ** 2)
        g = 2.0 * a[cap] * x
        A = float(np.sum(W * (e - a[cap]) * g) / np.sum(W * g * g))
        gg = 1.0 + 2.0 * A * x
        for k in range(2):
            sel = cap == k
            if not np.any(sel):
                continue
            a[k] = float(np.sum(W[sel] * e[sel] * gg[sel]) / np.sum(W[sel] * gg[sel] ** 2))
        a = np.maximum(a, 1e-10)
    W = 1.0 / (2.0 * (a[cap] + s) ** 2)
    g = 2.0 * a[cap] * x
    A_err = float(1.0 / np.sqrt(np.sum(W * g * g)))
    lev = float(np.sqrt(np.sum(W * x * x) / np.sum(W)))
    return dict(A=A, A_err=A_err, a_cap=a.tolist(), leverage=lev,
                frac_pos=float(np.sum(W[x > 0]) / np.sum(W)))


def profile_A(e, W, a_cap_pix, x):
    g = 2.0 * a_cap_pix * x
    return np.sum(W * (e - a_cap_pix) * g) / np.sum(W * g * g)


def slope_b(e, W, x, cap):
    """Weighted regression of e on x with per-cap intercepts: <e> = c_cap + b x.
    b is well defined even when the clustering variance is zero (pure-noise null),
    unlike A = b / (2 a); the nulls are therefore evaluated on b and rescaled to
    A-equivalent units with the DATA value of a."""
    X = np.column_stack([(cap == 0).astype(float), (cap == 1).astype(float), x])
    XtW = X.T * W
    return float(np.linalg.solve(XtW @ X, XtW @ e)[2])


# ---------------------------------------------------------------- nulls
def poisson_null(S, phat, a_cap, sigma2_cap=None, nsim=NSIM, seed=SEED):
    """N1.  Each pixel's weighted data count redrawn as a moment-matched Poisson
    variate (mean alpha*R, variance Q).  With sigma2_cap given, an extra white
    Gaussian component of that variance is added as a clustering proxy, so the
    null brackets the shot-noise-only and clustering-inclusive cases."""
    rng = np.random.default_rng(seed)
    s, cap, V = S["shot"], S["cap"], S["vec"]
    lam = 1.0 / s
    x = phat @ V
    W = 1.0 / (2.0 * (np.asarray(a_cap)[cap] + s) ** 2)
    Xd = np.column_stack([(cap == 0).astype(float), (cap == 1).astype(float), V[0], V[1], V[2]])
    Wd = 1.0 / (s + (np.asarray(sigma2_cap)[cap] if sigma2_cap is not None else 0.0))
    M = np.linalg.solve((Xd.T * Wd) @ Xd, Xd.T * Wd)
    Xs = np.column_stack([np.ones(s.size), V[0], V[1], V[2]])
    Ms = np.linalg.solve((Xs.T * Wd) @ Xs, Xs.T * Wd)
    outB, outD, outDs = [], [], []
    for _ in range(nsim):
        dsim = rng.poisson(lam) / lam - 1.0
        if sigma2_cap is not None:
            dsim = dsim + rng.normal(0.0, np.sqrt(np.asarray(sigma2_cap)[cap]))
        esim = dsim ** 2 - s
        outB.append(slope_b(esim, W, x, cap))
        outD.append(np.linalg.norm((M @ dsim)[2:5]))
        outDs.append(np.linalg.norm((Ms @ dsim)[1:4]))
    return np.array(outB), np.array(outD), np.array(outDs)


def axis_scan(S, nside_axes=NSIDE_AXES, min_frac=0.20):
    e = S["delta"] ** 2 - S["shot"]
    cap, s = S["cap"], S["shot"]
    a0 = np.array([np.mean(e[cap == k]) for k in range(2)])
    W = 1.0 / (2.0 * (a0[cap] + s) ** 2)
    ap = a0[cap]
    V = np.array(hp.pix2vec(nside_axes, np.arange(hp.nside2npix(nside_axes))))
    rot = hp.Rotator(coord=["C", "G"])
    Vg = np.array(rot(V))
    res, keep, lbs = [], [], []
    Wt = W.sum()
    for j in range(Vg.shape[1]):
        p = Vg[:, j]
        if p[2] < 0:            # axes are headless: keep one hemisphere of directions
            continue
        x = p @ S["vec"]
        fpos = W[x > 0].sum() / Wt
        if fpos < min_frac or fpos > 1 - min_frac:
            continue
        res.append(profile_A(e, W, ap, x))
        keep.append(j)
        lbs.append(hp.vec2ang(p.reshape(1, 3), lonlat=True))
    return np.array(res), np.array(keep), a0, W


def injection_recovery(S, phat, a_cap, A_list=(0.0, 0.07, 0.20), nsim=200, seed=SEED + 1):
    """Validation: simulate maps with a KNOWN dipolar modulation of the clustering
    variance plus the measured shot noise, and check the estimator recovers it.
    delta_sim = G(0, a_cap(1+2A x)) + Poisson shot noise (moment-matched)."""
    rng = np.random.default_rng(seed)
    s, cap = S["shot"], S["cap"]
    x = phat @ S["vec"]
    lam = 1.0 / s
    a = np.asarray(a_cap)[cap]
    out = {}
    for A_in in A_list:
        var = a * np.maximum(1.0 + 2.0 * A_in * x, 1e-6)
        rec = []
        for _ in range(nsim):
            dsim = rng.normal(0.0, np.sqrt(var)) + (rng.poisson(lam) / lam - 1.0)
            sub = dict(S); sub["delta"] = dsim
            rec.append(fit_modulation(sub, phat)["A"])
        rec = np.array(rec)
        out[f"A_in_{A_in:g}"] = dict(A_in=A_in, A_out_mean=float(rec.mean()),
                                     A_out_std=float(rec.std(ddof=1)),
                                     bias=float(rec.mean() - A_in))
    return out


def jackknife_A(S, phat, nside_jk=2):
    """Delete-one jackknife over nside=2 superpixels (extra, not pre-registered)."""
    sup = hp.ang2pix(nside_jk, *hp.pix2ang(S["nside"], S["idx"]))
    groups = np.unique(sup)
    vals = []
    for g in groups:
        sel = sup != g
        if sel.sum() < 100:
            continue
        sub = dict(S)
        for k in ("delta", "shot", "cap", "b"):
            sub[k] = S[k][sel]
        sub["vec"] = S["vec"][:, sel]
        vals.append(fit_modulation(sub, phat)["A"])
    vals = np.array(vals)
    n = vals.size
    return float(np.sqrt((n - 1) / n * np.sum((vals - vals.mean()) ** 2))), n


# ---------------------------------------------------------------- main
def main():
    phat = lb_to_vec(*PLANCK_LB)
    R = {"preregistration": "PREREGISTRATION.md (commit c1acb329)",
         "planck_axis_lb": PLANCK_LB, "A_CMB_reference": A_CMB, "seed": SEED}

    S = load_sample(64)
    R["baseline_sample"] = dict(nside=64, npix=int(S["delta"].size),
                                npix_cap=S["npix_cap"],
                                area_deg2=float(S["delta"].size * S["pix_area_deg2"]),
                                alphas={k: float(v) for k, v in S["alphas"].items()},
                                pix_overlap=int(len(S["idx"]) - len(np.unique(S["idx"]))))
    s1 = fit_dipole(S)
    R["S1_dipole"] = s1
    R["S1_dipole"]["proj_planck"] = float(np.dot(s1["dipole"], phat))
    s1s = fit_dipole(S, shared_monopole=True)
    R["S1_dipole_shared_monopole"] = dict(
        dipole=s1s["dipole"], amp=s1s["amp"], dipole_err=s1s["dipole_err"],
        proj_planck=float(np.dot(s1s["dipole"], phat)),
        note="single monopole for both caps; sensitive to the NGC/SGC relative offset, "
             "hence to imaging systematics, so quoted only as an upper bound")
    s2 = fit_modulation(S, phat)
    R["S2_modulation"] = s2
    xp = phat @ S["vec"]
    W2 = 1.0 / (2.0 * (np.asarray(s2["a_cap"])[S["cap"]] + S["shot"]) ** 2)
    e_data = S["delta"] ** 2 - S["shot"]
    b_data = slope_b(e_data, W2, xp, S["cap"])
    a_bar = float(np.mean(np.asarray(s2["a_cap"])))
    R["S2_modulation"]["slope_b"] = b_data
    R["S2_modulation"]["a_bar"] = a_bar

    # N1 (evaluated on the slope b, rescaled to A-equivalent units by 2*a_data)
    R["N1_poisson_null"] = {"nsim": NSIM}
    for tag, sig in (("shot_only", None), ("shot_plus_clustering", s2["a_cap"])):
        nB, nD, nDs = poisson_null(S, phat, s2["a_cap"], sigma2_cap=sig)
        R["N1_poisson_null"][tag] = dict(
            b_mean=float(nB.mean()), b_std=float(nB.std(ddof=1)),
            A_equiv_std=float(nB.std(ddof=1) / (2 * a_bar)),
            p_two_sided_b=float((np.abs(nB) >= abs(b_data)).mean()),
            D_mean=float(nD.mean()), D_std=float(nD.std(ddof=1)),
            p_D=float((nD >= s1["amp"]).mean()),
            D_shared_std=float(nDs.std(ddof=1)),
            p_D_shared=float((nDs >= s1s["amp"]).mean()))

    # N2
    scanA, keep, a0, W = axis_scan(S)
    np.save(f"{OUT}/axis_scan_A.npy", scanA)
    A_planck_profile = float(profile_A(S["delta"] ** 2 - S["shot"], W, a0[S["cap"]], xp))
    R["N2_axis_scan"] = dict(
        n_axes_admissible=int(scanA.size), A_profile_planck=A_planck_profile,
        scan_rms=float(np.sqrt(np.mean(scanA ** 2))),
        scan_absA_median=float(np.median(np.abs(scanA))),
        scan_absA_max=float(np.abs(scanA).max()),
        p_LEE=float((np.abs(scanA) >= abs(A_planck_profile)).mean()),
        percentile_absA_planck=float((np.abs(scanA) < abs(A_planck_profile)).mean() * 100),
        sign_convention="one direction kept per headless axis (Galactic z>=0), so only "
                        "|A| statistics are meaningful; rms is over the kept sample")

    # jackknife (extra)
    jk, njk = jackknife_A(S, phat)
    R["jackknife"] = dict(sigma_A=jk, n_regions=njk, note="delete-one over nside=2 superpixels; not pre-registered, added as the conservative error")

    # bounds
    sig_pre = float(np.hypot(R["N1_poisson_null"]["shot_plus_clustering"]["A_equiv_std"], s2["A_err"]))
    R["bounds"] = dict(
        sigma_prereg=sig_pre,
        A95_prereg=float(abs(s2["A"]) + 1.645 * sig_pre),
        sigma_conservative=float(max(jk, R["N2_axis_scan"]["scan_rms"])),
        A95_conservative=float(abs(s2["A"]) + 1.645 * max(jk, R["N2_axis_scan"]["scan_rms"])),
        D95_prereg=float(s1["amp"] + 1.645 * R["N1_poisson_null"]["shot_plus_clustering"]["D_std"]),
        D95_shared_monopole=float(s1s["amp"] + 1.645 * R["N1_poisson_null"]["shot_plus_clustering"]["D_shared_std"]))

    R["validation_injection"] = injection_recovery(S, phat, s2["a_cap"])

    # comparison with the CMB modulation on the same axis
    errs = {"fit": s2["A_err"], "jackknife": jk, "axis_scatter": R["N2_axis_scan"]["scan_rms"],
            "poisson_null_equiv": R["N1_poisson_null"]["shot_plus_clustering"]["A_equiv_std"]}
    R["comparison_to_CMB"] = {
        "A_QSO": s2["A"],
        "A_CMB": A_CMB,
        "tension_sigma": {k: float(abs(s2["A"] - A_CMB) / v) for k, v in errs.items()},
        "errors": {k: float(v) for k, v in errs.items()}}

    # N3 bracket
    br = {}
    variants = [("baseline", dict()),
                ("no_weight_sys", dict(nosys=True)),
                ("bgal_gt_30", dict(bcut=30.0)),
                ("mask_0.8", dict(mask_frac=0.8)),
                ("joint_alpha", dict(joint_alpha=True)),
                ("nside32", dict(nside=32)),
                ("nside128", dict(nside=128)),
                ("nside128_mask0.8", dict(nside=128, mask_frac=0.8)),
                ("nside128_mask0.95", dict(nside=128, mask_frac=0.95)),
                ("nside64_mask0.95", dict(mask_frac=0.95))]
    for name, kw in variants:
        ns = kw.pop("nside", 64)
        Sv = load_sample(ns, **kw)
        f = fit_modulation(Sv, phat)
        d1 = fit_dipole(Sv)
        br[name] = dict(A=f["A"], A_err=f["A_err"], leverage=f["leverage"],
                        npix=int(Sv["delta"].size), dipole_amp=d1["amp"],
                        dipole_proj_planck=float(np.dot(d1["dipole"], phat)))
    for k, cap in enumerate(CAPS):          # per-cap
        Sv = load_sample(64)
        sel = Sv["cap"] == k
        sub = dict(Sv)
        for key in ("delta", "shot", "cap", "b"):
            sub[key] = Sv[key][sel]
        sub["vec"] = Sv["vec"][:, sel]
        sub["idx"] = Sv["idx"][sel]
        f = fit_modulation(sub, phat)
        br[f"{cap}_only"] = dict(A=f["A"], A_err=f["A_err"], leverage=f["leverage"],
                                 npix=int(sel.sum()))
    R["N3_bracket"] = br

    # pre-registered decision rule
    det = (R["N1_poisson_null"]["shot_plus_clustering"]["p_two_sided_b"] < 0.01
           and R["N2_axis_scan"]["p_LEE"] < 0.05)
    R["decision"] = {
        "criterion_1_poisson_p_lt_0p01": bool(R["N1_poisson_null"]["shot_plus_clustering"]["p_two_sided_b"] < 0.01),
        "criterion_2_LEE_p_lt_0p05": bool(R["N2_axis_scan"]["p_LEE"] < 0.05),
        "detection": bool(det)}
    with open(f"{OUT}/ledger6_qso_isotropy.json", "w") as fh:
        json.dump(R, fh, indent=2)
    print(json.dumps({k: R[k] for k in
                      ["baseline_sample", "S1_dipole", "S1_dipole_shared_monopole",
                       "S2_modulation", "validation_injection", "comparison_to_CMB", "N1_poisson_null",
                       "N2_axis_scan", "jackknife", "bounds", "decision"]}, indent=2))
    print("\nN3 bracket:"); print(json.dumps(R["N3_bracket"], indent=2))


if __name__ == "__main__":
    main()
