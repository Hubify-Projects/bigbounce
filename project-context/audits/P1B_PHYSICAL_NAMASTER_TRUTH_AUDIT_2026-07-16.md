# P1B physical-spectrum NaMaster truth audit — 2026-07-16

Status: **OPEN — canonical production complete; robustness battery still running**

This audit is a proactive pre-review comparison between the current P1B
manuscript and the corrected production artifact
`reproducibility/p1_namaster_500mc/results/physical_spectrum_v2/summary.json`.
It does not close any robustness claim whose corresponding 500-realization
receipt is not yet complete.

## Canonical evidence

- Production mode: 500 realizations, deterministic seeds 42--541.
- Resolution: `NSIDE=512`, `LMAX=1024`, with field and bin harmonic limits
  explicitly matched.
- Spectra: CAMB 1.6.6 `lensed_scalar` raw \(C_\ell\), not a semi-analytic
  \(EE\) curve or \(C_\ell^{BB}=0.05C_\ell^{EE}\) proxy.
- Spectrum hashes:
  - EE: `7735597b158c8e4fe2643ef8196f3e597d5db353eebbebdf2c62768797101c19`
  - BB: `c1d4b730565ffb8eaa87663f6fe90bc0114c1596ca828065f3454c98ba92d528`
- Exact-window equivalence maximum absolute residual:
  `1.4094628242311558e-18`.
- Eight ordered realization workers; runtime `701.5474569797516` seconds.
- \(\beta_{\rm inj}=0.270^\circ\):
  - recovered \(0.270^\circ\);
  - signed bias \(0.000^\circ\) at the reported grid precision;
  - per-realization scatter \(0.0128158924^\circ\);
  - MC-mean SE \(0.0005731441^\circ\);
  - diagonal template diagnostic `30.4126953842`.
- \(\beta_{\rm inj}=0.342^\circ\): recovered \(0.342^\circ\), template
  diagnostic `38.4360793570`.
- Null injection: recovered \(0.000^\circ\), template diagnostic `0.0`.

## Manuscript contradictions requiring closure

1. The pipeline description currently says the simulations use a semi-analytic
   Planck-2018 \(EE\) fit and a five-percent \(BB\) proxy. Replace this with the
   exact pinned CAMB parameter and raw-spectrum contract.
2. The manuscript says bin edges extend to \(3N_{\rm side}=1536\), with bins
   above the simulated map limit carrying noise. The corrected contract ends
   the final bin at the inclusive `LMAX=1024`; the field, theory arrays, and
   workspace use that same limit.
3. The canonical table and prose report \(0.269^\circ\), bias
   \(-0.001^\circ\), scatter \(0.0514^\circ\), and SE \(0.0023^\circ\).
   Replace them with the canonical evidence above.
4. The heuristic template diagnostics `20.01` and `25.32` are superseded by
   `30.4127` and `38.4361`. Preserve the limitation that these omit full
   inter-bin covariance and are not real-sky detection significances.
5. All active artifact paths still point to `results/exact_window_500mc`.
   Change current claims to `results/physical_spectrum_v2`; retain historical
   paths only when explicitly labeling superseded evidence.
6. The robustness table contains historical values for the sky-fraction,
   apodization, mask, and purification rows. Do not update those rows until
   each new 500-realization shard and merged receipt validates.
7. The historical purification artifact hash must be removed. The corrected
   purification run uses a matched mask harmonic limit and needs a new result
   hash and receipt.

## Release gates

- [ ] Six active non-purification robustness shards complete and validate.
- [ ] Corrected purification shard completes and validates.
- [ ] C10 and declared-sky merged results and receipts validate exact
      configuration membership, `N=500`, and seeds 42--541.
- [ ] Manuscript table, methods, results, limitations, artifact paths, and
      claims table agree with the merged evidence.
- [ ] Version-matched immutable analysis manifest binds the producing scripts,
      spectra metadata, canonical result, bandpowers, shards, and receipts.
- [ ] PDF compiles and passes the full visual/overflow audit.
- [ ] SSOT, site, Convex, mirrors, archive retention, and exact-PDF review
      packet all bind the same version and SHA-256.

No readiness increase is warranted until these gates pass.
