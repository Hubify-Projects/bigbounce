# Superseded effective-ell-template results

The top-level `summary.json`, `namaster_500mc.log`,
`c10_robustness_battery.json`, `c1_fsky_sweep.json`, and
`c9f_negative_beta.json` are preserved as historical evidence of the
pre-2026-07-14 analysis. Their beta recovery fit evaluated the theory spectrum
at effective-ell bin centres rather than applying the NaMaster bandpower-window
operator used by the estimator. They must not be cited as current calibration
results.

The July 14 exact-window outputs under `exact_window_500mc/` are also retained
but superseded: their operator contraction is correct, while their synthetic
sky passed a D-ell-like semi-analytic EE amplitude to `healpy.synfast` as raw
C-ell and used `BB=0.05*EE`. They must not be cited as a physical-noise,
scatter, SNR, or bias calibration.

The replacement code writes new results under `physical_spectrum_v2/`. It
contracts the complete rotated `[EE, EB, BE, BB]` theory through
`NmtWorkspace.get_bandpower_windows()`, uses pinned raw CAMB lensed EE/BB, and
verifies both the spectrum-unit contract and numerical operator equivalence
before running an ensemble. That corrected rerun is now complete under
`physical_spectrum_v2/`; its `summary.json` and `bandpowers.npz` are the
current production artifacts. The files described above remain superseded.
