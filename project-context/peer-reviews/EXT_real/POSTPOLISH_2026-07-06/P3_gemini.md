# EXT POSTPOLISH 2026-07-06 — P3 — Gemini

- **Provider:** Gemini (houston@bamf.com, Ultra, /u/1/)
- **Model/effort:** 3.5 Thinking
- **Chat URL:** https://gemini.google.com/u/1/app/1df37c9e9a70a8dd
- **PDF:** P3_v3.1.140.pdf (md5 55459a5f46ec48754a74db448f1e7657)
- **Harvested:** 2026-07-07
- **Parsed verdict (from response):** MAJOR REVISIONS

## Raw verbatim response

(1) VERDICT: MAJOR REVISIONS
(2) ISSUES:

[MAJOR] Section II B / Section III E (eROSITA Anomaly Score Provenance): The production anomaly score threshold axis (S_BigAE = 0.259) is unrecoverable and irreproducible across monotone rescalings due to uncommitted post-hoc code. Relying on an unrecoverable metric axis for a primary catalog tier violates fundamental data provenance and scientific reproducibility standards.

[MAJOR] Section II B (Data Leakage via Preprocessing): Feature scaling normalization constants for the eROSITA and NEOWISE tabular catalogs were fit on the full datasets rather than strictly on the training splits. This methodological flaw introduces validation and tail information leakage into the preprocessing constants, artificially biasing the absolute scale of the validation mean-squared error and risking an unverified reordering of the extreme anomaly tail.

[MAJOR] Section III D & Section III E (Inclusion of Failed Tiers in Unique Counts): The inclusive Path-C total of 377,780 unique anomalies aggregates validated cosmic signals with known systematic instrument artifacts and unquantified data. This total is heavily inflated by the LAMOST tier (~113,000 objects) and the eROSITA tier (298 objects), both of which explicitly failed their detector-sensitivity injection-recovery gates.

[MAJOR] Section V (Cosmological Constraints and Noise Bias): The central multi-tracer Fisher forecast reports a 9.4% tightening of f_NL bounds, but the noise-de-biased point estimate returns the single-tracer baseline exactly, indicating zero actual multi-tracer cosmological improvement at current signal-to-noise levels. Promoting a noise-driven shift as a central forecast is mathematically misleading and requires major revisions to the introductory, abstract, and concluding text.

[MINOR] Section III A (DESI Scan Target Composition): Approximately 98.7% of the raw DESI anomaly clusters coincide with blank sky fibers or secondary filler spectra rather than validated primary science targets. Consequently, the paper's nominal multipliers are highly misleading when juxtaposed against science-target benchmarks rather than full-instrument streams.

[MINOR] Section V A (NANOGrav Application and Environmental Caveats): The Savage-Dickey Bayes factor calculation claims a decisive preference for the matter-bounce model over an idealized circular-orbit supermassive black hole binary (SMBHB) reference index of gamma = 4.33. However, because environmentally modified SMBHB models involving stellar scattering or eccentric hardening can flatten the expected spectral index to gamma ~ 2.5-3, the recovered value of gamma = 2.567 +/- 0.382 holds no real statistical power to discriminate a primordial background from standard astrophysical environments.

[MINOR] Section II B & Section VI C (Unweighted Optimization Loss): The BIGAE model architecture minimizes an unweighted per-element mean-squared error loss function that treats all input feature elements equally. This design choice places low-signal-to-noise spectral regions on an equal footing with high-signal-to-noise regions, introducing noise-driven residuals that degrade the absolute optimality of the anomaly rankings.

(3) The central claim of delivering a validated, multi-survey anomaly catalog is supported for the specific point-source subsets that successfully cleared independent stability and sensitivity gates, but it is severely undermined by the inclusion of failed data tiers, uncorrected instrument training biases, and unrecoverable scoring metrics within the broader collective total.
