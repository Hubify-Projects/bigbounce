# Superseded effective-ell-template results

The top-level `summary.json`, `namaster_500mc.log`,
`c10_robustness_battery.json`, `c1_fsky_sweep.json`, and
`c9f_negative_beta.json` are preserved as historical evidence of the
pre-2026-07-14 analysis. Their beta recovery fit evaluated the theory spectrum
at effective-ell bin centres rather than applying the NaMaster bandpower-window
operator used by the estimator. They must not be cited as current calibration
results.

Corrected results are generated under `exact_window_500mc/`. The replacement
scripts contract the complete rotated `[EE, EB, BE, BB]` theory through
`NmtWorkspace.get_bandpower_windows()` and verify numerical equivalence to
`decouple_cell(couple_cell(theory))` before running an ensemble.
