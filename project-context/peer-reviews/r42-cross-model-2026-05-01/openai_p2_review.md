---
model: gpt-5
paper: p2 — f_NL Forecast — SPHEREx + bounce predictions (matter bounce f_NL=-4.375)
pdf: /Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf
date: 2026-05-01
input_tokens: 23925
output_tokens: 8000
total_tokens: 31925
reviewer: openai (cross-model adversarial)
---
## BLOCKERs
- Incorrect scale-dependent bias formula
  Evidence: Eq. (3) in §III.A writes Δb(k) = 2(b1 − 1) fNL δc D(z) T(k) α(k), i.e., proportional to D(z)T(k) and with no 1/k^2 dependence; the text below says “The signal grows as 1/k^2,” which contradicts the written equation and dimensional analysis (standard result is Δb(k,z) = 2 fNL (b1−1) δc / M(k,z) with M(k,z) ∝ k^2 T(k) D(z)).
  Fix: Replace Eq. (3) by Δb(k,z) = 2 fNL (b1 − 1) δc / M(k,z) with M(k,z) = 2 k^2 T(k) D(z)/(3 Ωm H0^2) (or any equivalent normalization), and ensure all downstream Fisher weightings and plots using SDB adopt the corrected kernel.

- Internal inconsistency in Bayes factor ranges and prior dependence
  Evidence: §VI.C/Table II states “Bounce vs. tuned multifield [−15,+15]: 8–11,” then in the same subsection the text says broadening the bounce prior to σtheory = 1.0 “drops from ∼17 to ∼8,” while the next sentence says “reduces these to ∼ 8–17 (abstract headline).” The abstract also quotes “∼ 8–17 at the broadened bounce prior” while §VI.C/Table II reports 8–11 for the delta-prior case. These are mutually inconsistent and invert the stated prior sensitivity.
  Fix: Recompute and present a single, self-consistent set of Bayes factors for (i) delta prior and (ii) σtheory = 0.5, 1.0, 2.0 Gaussian priors, all with the same competitor prior and GR treatment. Align the abstract, §VI.C text, Table II, and Table III numerically and remove contradictory phrasing (“reduces … to 8–17”).

- Contradiction about the amplitude recovery factor r (r should be ≤ 1 but reported > 1)
  Evidence: §II.A (bottom of p.2) reports “r = 0.85 ± 0.13 (range: 0.55–1.14)” from the null-space scan; §III.B (Eq. 4 and surrounding text) states “r is positive definite and satisfies 0 < r ≤ 1.” Reporting r > 1 indicates either an error in the overlap implementation or that unphysical coefficient sets were included in the scan.
  Fix: Enforce the physical constraint r ≤ 1 by restricting to coefficient sets that do not yield super-squeezed excess power relative to the local template under the adopted Fisher weighting, or diagnose and correct the overlap implementation. Recompute all quoted r ranges and any downstream significance that used the r-distribution.

- Reproducibility gap between manuscript and code release
  Evidence: “DATA AND CODE AVAILABILITY” cites code pinned to release tag v1.7.0, while the manuscript is “v1.7.5” (title page). Several critical results (null-space scans, injection–recovery, Bayes factor MC) depend on code not embedded in the text.
  Fix: Update the repository to a v1.7.5 tag containing the exact scripts/configs used for every figure/table/number in this version, and list commit hashes in the paper. Alternatively, roll back the manuscript claims to match v1.7.0 outputs.

## MAJOR
- Under-determined bispectrum polynomial but used to derive survey-level overlaps without publishing the explicit P(k1,k2,k3)
  Evidence: §II.A introduces a 6-parameter degree-9 polynomial P with only three benchmark constraints and adopts one coefficient set (2, 7, 3, −12, −69, 19), while acknowledging a 3D null space. The explicit polynomial is not printed in the paper; only code is referenced. Yet §III.B and Fig. 1 rely on the full shape to compute r across weightings and triangles.
  Fix: Print the explicit symmetric polynomial P (basis and coefficients) for the reference solution used in all forecasts, and provide a supplementary table with 10–20 representative null-space samples spanning your scan radius that reproduce the three benchmarks. Report r and rcos for each to show robustness.

- Template-overlap methodology lacks full specification and validation under LSS-like covariance
  Evidence: §III.B quotes r across “10 physically motivated weighting schemes” and squeezed cutoffs, but there is no definition of the exact w(k1,k2,k3), k-range, binning, mask treatment, redshift dependence, or shot-noise terms used for “SPHEREx-like” and “MegaMapper-like.” The injection–recovery in §II.A uses “isotropic Gaussian noise” and “full sky,” which is CMB-like and not a realistic SPHEREx covariance (photo-z scatter, mask, multi-tracer covariance).
  Fix: Explicitly define each weighting scheme (equation for w, k-min/max, binning, noise and shot-noise terms, fsky), and add an injection–recovery with an LSS-like non-diagonal covariance and a realistic fsky mask. Report how projection noise (from non-local shape tails) affects σ via a two-template Fisher analysis, not only via rcos.

- Bounce transmission through the nonsingular bounce only argued heuristically at cubic order
  Evidence: §II.C claims “semi-analytic estimate … δfNL ∼ 10−3” from LQC-mode arguments but provides no derivation or citation to a complete cubic-order calculation; linear-order transmission is cited, but the forecasts rest critically on the assumption that third-order effects are negligible.
  Fix: Provide either (i) a detailed derivation (or a robust numerical calculation) of the cubic-order bounce transmission showing δfNL ≪ 1 for the modes of interest, or (ii) propagate a conservative theoretical uncertainty σtheory from plausible bounce-transmission effects
