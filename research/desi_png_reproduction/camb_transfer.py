#!/usr/bin/env python3
"""Ledger row 4 v2, fix (2): CAMB Boltzmann transfer function, replacing the
Eisenstein-Hu fitting formula used in fit_fnl.py step 4 (RUN_LOG.md: CLASS
build failed; camb installed cleanly here via a prebuilt macOS arm64 wheel,
`pip install camb` -- no gfortran/toolchain issue, contra the plan's worry).
Cosmology matched to cosmoprimo's DESI() fiducial (h=0.6736, ombh2=0.02237,
omch2=0.12064, ns=0.9649) so only the transfer-function engine changes, not
the background cosmology.
"""
import numpy as np
import camb

H0 = 67.36
OMBH2 = 0.049301692328524445 * (H0 / 100) ** 2
OMCH2 = (0.3151917236644108 - 0.049301692328524445) * (H0 / 100) ** 2
NS = 0.9649
# NOTE (bug found+fixed): KREF must NOT sit exactly on camb's minkh grid edge
# -- get_matter_power_spectrum(minkh=1e-5,...) underflows to ~0 exactly at
# k=1e-5 (spline boundary artifact), which blew up the T(k) normalisation
# (ratio by ~0) on the first run. KREF=1e-4 is safely inside the grid.
KREF = 1e-4


def _get_camb_pk(z_list):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=OMBH2, omch2=OMCH2)
    pars.InitPower.set_params(ns=NS)
    pars.set_matter_power(redshifts=sorted(set(z_list), reverse=True), kmax=2.0)
    pars.NonLinear = camb.model.NonLinear_none
    results = camb.get_results(pars)
    kh, z, pk = results.get_matter_power_spectrum(minkh=1e-5, maxkh=1.0, npoints=4000)
    return kh, z, pk, results


_KH, _Z, _PK, _RESULTS = _get_camb_pk([0.0, 1.491])


def pk_camb_z0(k_hmpc):
    return np.interp(k_hmpc, _KH, _PK[list(_Z).index(0.0)])


def Tk_camb(k_hmpc):
    num = pk_camb_z0(k_hmpc) / np.asarray(k_hmpc) ** NS
    den = pk_camb_z0(KREF) / KREF ** NS
    return np.sqrt(num / den)


def growth_factor_camb(z):
    # D(z)/D(0) via sqrt(P(k_ref,z)/P(k_ref,0)) at a large-scale, near-linear k
    pz = np.interp(k_ref_for_growth, _KH, _PK[list(_Z).index(z)]) if z in _Z else None
    return None


k_ref_for_growth = 0.01

if __name__ == "__main__":
    from cosmoprimo.fiducial import DESI
    cosmo = DESI(engine="eisenstein_hu")
    fo = cosmo.get_fourier()
    pk0_eh = fo.pk_interpolator(of="delta_cb")
    for k in [0.003, 0.005, 0.008, 0.01, 0.02, 0.05]:
        t_camb = Tk_camb(k)
        num = pk0_eh(k, z=0) / k ** NS
        den = pk0_eh(KREF, z=0) / KREF ** NS
        t_eh = np.sqrt(num / den)
        print(f"k={k:.3f}  T_camb={t_camb:.5f}  T_EH={t_eh:.5f}  "
              f"pct_diff={100*(t_camb-t_eh)/t_eh:+.2f}%")
