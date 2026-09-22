"""Ledger row 4 LRG channel: exact profile-likelihood core.

Same model, same window/covariance treatment, same k-range and the same
Delta chi2 = 1 profile-likelihood interval as v3's ../fit_fnl_official.py
and v4/v5's ../fit_fnl_splits.py. The ONLY change is how b1 is profiled
out: because

    b(k) = b1 + 3 f_NL delta_c (b1 - p)/alpha(k) = A(k) b1 + B(k),

the multipole model is exactly QUADRATIC in b1, so the windowed, rebinned
model vector is M(b1) = M0 + M1 b1 + M2 b1^2 and chi2(b1) is an exact
quartic whose minimum is a cubic root -- three matrix-vector products per
f_NL grid point instead of ~50 Nelder-Mead evaluations. This is an
algebraic reorganisation, not a different fit: verify_quadratic() checks it
against a direct evaluation of the original expression, and
tests/regress_qso.py checks the whole core reproduces v5's published QSO
headline numbers to the digit.
"""
import numpy as np

DELTA_C = 1.686


def theory_basis(theory_k, alpha_fn, plin_fn, f_g, fnl, p):
    """T(b1) = T0 + T1 b1 + T2 b1^2, concatenated over ell = 0, 2, 4."""
    t = [[], [], []]
    for ell in (0, 2, 4):
        k = theory_k[ell]
        pl = plin_fn(k)
        c = 3.0 * fnl * DELTA_C / alpha_fn(k)
        A, B = 1.0 + c, -c * p
        if ell == 0:
            t[2].append(A ** 2 * pl)
            t[1].append((2.0 * A * B + (2.0 / 3.0) * A * f_g) * pl)
            t[0].append((B ** 2 + (2.0 / 3.0) * B * f_g + f_g ** 2 / 5.0) * pl)
        elif ell == 2:
            t[2].append(np.zeros_like(pl))
            t[1].append((4.0 / 3.0) * A * f_g * pl)
            t[0].append(((4.0 / 3.0) * B * f_g + (4.0 / 7.0) * f_g ** 2) * pl)
        else:
            t[2].append(np.zeros_like(pl))
            t[1].append(np.zeros_like(pl))
            t[0].append((8.0 / 35.0) * f_g ** 2 * pl)
    return [np.concatenate(x) for x in t]


def theory_direct(theory_k, alpha_fn, plin_fn, f_g, fnl, p, b1):
    """The original expression, verbatim from ../fit_fnl_splits.py."""
    tv = []
    for ell in (0, 2, 4):
        kk = theory_k[ell]
        db = 3.0 * fnl * DELTA_C * (b1 - p) / alpha_fn(kk)
        b = b1 + db
        pl = plin_fn(kk)
        if ell == 0:
            v = (b ** 2 + (2.0 / 3.0) * b * f_g + f_g ** 2 / 5.0) * pl
        elif ell == 2:
            v = (4.0 / 3.0) * b * f_g * pl + (4.0 / 7.0) * f_g ** 2 * pl
        else:
            v = (8.0 / 35.0) * f_g ** 2 * pl
        tv.append(v)
    return np.concatenate(tv)


def verify_quadratic(theory_k, alpha_fn, plin_fn, f_g, p):
    worst = 0.0
    for fnl in (-40.0, -5.0, 0.0, 12.0, 77.0):
        T = theory_basis(theory_k, alpha_fn, plin_fn, f_g, fnl, p)
        for b1 in (0.8, 1.9, 2.3, 4.0):
            a = T[0] + T[1] * b1 + T[2] * b1 ** 2
            d = theory_direct(theory_k, alpha_fn, plin_fn, f_g, fnl, p, b1)
            worst = max(worst, float(np.max(np.abs(a - d) / (np.abs(d) + 1e-300))))
    return worst


def rebin(fine_k, fine_val, fine_nmodes, coarse_kedges):
    """nmodes-weighted rebin -- identical to ../official_window_io.rebin_to_coarse."""
    out = np.full(len(coarse_kedges), np.nan)
    for i, (lo, hi) in enumerate(coarse_kedges):
        m = (fine_k >= lo) & (fine_k < hi)
        if m.sum() == 0:
            continue
        out[i] = np.average(fine_val[m], weights=fine_nmodes[m])
    return out


class Binned:
    """One (tracer, z-bin, data-vector) fit setup on the official window and
    official EZmock covariance."""

    def __init__(self, W, theory_k, obs_k, obs_nmodes, cov, cov_kedges, cov_kc,
                 dvec, kmin=0.003, kmax=0.08, b1_lo=0.5, b1_hi=5.0):
        self.W, self.theory_k, self.obs_k = W, theory_k, obs_k
        self.obs_nmodes, self.cov_kedges = obs_nmodes, cov_kedges
        self.dvec = dvec
        kc = np.concatenate([cov_kc[ell] for ell in (0, 2, 4)])
        self.mask = np.isfinite(dvec) & (kc >= kmin) & (kc <= kmax)
        self.cinv = np.linalg.inv(cov[np.ix_(self.mask, self.mask)])
        self.obs_lens = [len(obs_k[ell]) for ell in (0, 2, 4)]
        self.b1_lo, self.b1_hi = b1_lo, b1_hi

    def _obs(self, tvec):
        mvec = self.W @ tvec
        out, i0 = [], 0
        for ell, n in zip((0, 2, 4), self.obs_lens):
            out.append(rebin(self.obs_k[ell], mvec[i0:i0 + n],
                             self.obs_nmodes[ell], self.cov_kedges[ell]))
            i0 += n
        return np.concatenate(out)

    def chi2_profiled(self, alpha_fn, plin_fn, f_g, fnl, p):
        T = theory_basis(self.theory_k, alpha_fn, plin_fn, f_g, fnl, p)
        M = [self._obs(t) for t in T]
        m = self.mask
        u0 = (M[0] - self.dvec)[m]
        u1, u2 = M[1][m], M[2][m]
        C = self.cinv
        g = np.empty((3, 3))
        U = [u0, u1, u2]
        for i in range(3):
            Cu = C @ U[i]
            for j in range(i, 3):
                g[i, j] = g[j, i] = float(U[j] @ Cu)
        # chi2(b) = g00 + 2 g01 b + (g11 + 2 g02) b^2 + 2 g12 b^3 + g22 b^4
        c0, c1 = g[0, 0], 2 * g[0, 1]
        c2, c3, c4 = g[1, 1] + 2 * g[0, 2], 2 * g[1, 2], g[2, 2]
        der = np.array([4 * c4, 3 * c3, 2 * c2, c1])
        roots = np.roots(der)
        cands = [r.real for r in roots
                 if abs(r.imag) < 1e-8 * (1 + abs(r.real))
                 and self.b1_lo <= r.real <= self.b1_hi]
        cands += [self.b1_lo, self.b1_hi]

        def val(b):
            return c0 + c1 * b + c2 * b ** 2 + c3 * b ** 3 + c4 * b ** 4

        vals = [val(b) for b in cands]
        i = int(np.argmin(vals))
        return float(vals[i]), float(cands[i])

    def profile(self, alpha_fn, plin_fn, f_g, grid, p):
        chi2 = np.empty(len(grid))
        b1 = np.empty(len(grid))
        for i, fv in enumerate(grid):
            chi2[i], b1[i] = self.chi2_profiled(alpha_fn, plin_fn, f_g, fv, p)
        return chi2, b1

    @property
    def n_bins(self):
        return int(self.mask.sum())


def interval(grid, chi2):
    """Delta chi2 = 1 profile-likelihood interval; returns (best, lo, hi, sigma)."""
    i = int(np.argmin(chi2))
    # sub-grid vertex from a 3-point parabola, so the central value is not
    # quantised by the grid spacing
    best = float(grid[i])
    cmin = float(chi2[i])
    if 0 < i < len(grid) - 1:
        y0, y1, y2 = chi2[i - 1], chi2[i], chi2[i + 1]
        den = y0 - 2 * y1 + y2
        if den > 0:
            dx = 0.5 * (y0 - y2) / den
            if abs(dx) <= 1:
                h = grid[i + 1] - grid[i]
                best = float(grid[i] + dx * h)
                cmin = float(y1 - 0.25 * (y0 - y2) * dx)
    d = chi2 - cmin
    lo_g, lo_d = grid[:i + 1][::-1], d[:i + 1][::-1]
    hi_g, hi_d = grid[i:], d[i:]
    lo = float(np.interp(1.0, lo_d, lo_g)) if lo_d.max() > 1 else float(grid[0])
    hi = float(np.interp(1.0, hi_d, hi_g)) if hi_d.max() > 1 else float(grid[-1])
    return best, lo, hi, float((hi - lo) / 2.0)


def refine(grid, chi2, alpha_fn, plin_fn, f_g, binned, p, span=None, npts=201):
    """Re-profile on a narrow grid around the coarse minimum for a precise
    central value and interval."""
    best, lo, hi, sig = interval(grid, chi2)
    if span is None:
        span = max(4.0 * max(sig, 1.0), 4.0)
    g2 = np.linspace(best - span, best + span, npts)
    c2, b2 = binned.profile(alpha_fn, plin_fn, f_g, g2, p)
    return g2, c2, b2


class ModelGrid:
    """The windowed, rebinned model basis (M0, M1, M2) on an f_NL grid.

    The basis depends only on the tracer/z-bin's window matrix, cosmology and
    p -- NOT on which data vector it is compared against. Computing it once
    per (z-bin, p) and reusing it for every systematics-split half is what
    makes 60 split fits tractable; the arithmetic per fit is unchanged.
    """

    def __init__(self, W, theory_k, obs_k, obs_nmodes, cov_kedges):
        self.W, self.theory_k, self.obs_k = W, theory_k, obs_k
        self.obs_nmodes, self.cov_kedges = obs_nmodes, cov_kedges
        self.obs_lens = [len(obs_k[ell]) for ell in (0, 2, 4)]

    def _obs(self, tvec):
        mvec = self.W @ tvec
        out, i0 = [], 0
        for ell, n in zip((0, 2, 4), self.obs_lens):
            out.append(rebin(self.obs_k[ell], mvec[i0:i0 + n],
                             self.obs_nmodes[ell], self.cov_kedges[ell]))
            i0 += n
        return np.concatenate(out)

    def basis(self, alpha_fn, plin_fn, f_g, grid, p):
        out = None
        for i, fnl in enumerate(grid):
            T = theory_basis(self.theory_k, alpha_fn, plin_fn, f_g, fnl, p)
            M = [self._obs(t) for t in T]
            if out is None:
                out = np.empty((len(grid), 3, len(M[0])))
            out[i] = np.array(M)
        return out


def profile_from_basis(basis, dvec, cinv, mask, b1_lo=0.5, b1_hi=5.0):
    """chi2 profiled over b1 at each grid point, from a precomputed basis."""
    n = basis.shape[0]
    chi2 = np.empty(n)
    b1s = np.empty(n)
    d = dvec[mask]
    for i in range(n):
        u0 = basis[i, 0][mask] - d
        u1, u2 = basis[i, 1][mask], basis[i, 2][mask]
        U = (u0, u1, u2)
        g = np.empty((3, 3))
        for a in range(3):
            Cu = cinv @ U[a]
            for b in range(a, 3):
                g[a, b] = g[b, a] = float(U[b] @ Cu)
        c0, c1 = g[0, 0], 2 * g[0, 1]
        c2, c3, c4 = g[1, 1] + 2 * g[0, 2], 2 * g[1, 2], g[2, 2]
        roots = np.roots([4 * c4, 3 * c3, 2 * c2, c1])
        cands = [r.real for r in roots
                 if abs(r.imag) < 1e-8 * (1 + abs(r.real)) and b1_lo <= r.real <= b1_hi]
        cands += [b1_lo, b1_hi]
        vals = [c0 + c1 * b + c2 * b ** 2 + c3 * b ** 3 + c4 * b ** 4 for b in cands]
        j = int(np.argmin(vals))
        chi2[i], b1s[i] = vals[j], cands[j]
    return chi2, b1s
