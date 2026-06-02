# P4 R-round — DIRECT vendor — Grok-4 brutal-honesty reviewer

**Model**: `grok-4` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 17.0s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=89752, completion=935, total=91182, prompt_details={'text_tokens': 89752, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 128}, completion_details={'reasoning_tokens': 495, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, num_sources_used=0, cost_in_usd_ticks=1156306000

---

**## PAPER-GRO-B1 (BLOCKER) — Abstract + Sec. 1 (lines ~80-110, 200-220)**

The headline "null ℓ=1" is load-bearing only on the strict-superset subsample mask (f_sky=0.659, −0.12σ); the canonical mask (f_sky=0.490) yields +3.64σ post-MASTER that is only ~12% explained by the monopole-only generative null. The paper's own multi-null battery + cross-spectrum favors a depth-correlated systematic, yet the abstract and title present a clean isotropy result.

Fix: Move the subsample-mask −0.12σ result to the title/abstract as the sole load-bearing claim; relegate the canonical +3.64σ to a dedicated systematics section with the explicit statement that it is not a primordial detection.

**## PAPER-GRO-B2 (BLOCKER) — Sec. 9.1 + Table III (lines ~1550-1620)**

The paper claims the result is inconsistent in amplitude with Shamir (2020/2022) by a factor ~6–12 under the present pipeline, yet repeatedly states that a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis that is not performed. Amplitude comparison without the matched estimator is not a statistical exclusion.

Fix: Replace all amplitude-ratio language with "under the present ViT/TTA pipeline and selection the maximum regional asymmetry is 0.32% (vs. Shamir-reported 2–4%)"; remove the factor 6–12 claim.

**## PAPER-GRO-B3 (MAJOR) — Sec. 4.1 + Sec. 9.10 (lines ~780-820, 1680-1720)**

The empirical 50%-recovery-at-3σ threshold is quoted as ≥0.75% on the strict-HC subsample only; the Fisher floor (~0.29% full-amplitude) is statistical-only and assumes zero systematic dipole projection. The 9.5σ residual monopole demonstrates that sub-percent biases survive TTA, yet no PSF/scan-angle cross-power test on the full catalog is reported to close the systematic floor.

Fix: State explicitly that the 0.29% figure is a statistical upper bound under the zero-systematic-dipole-projection assumption; move the 0.75% empirical threshold to the abstract as the operative sensitivity.

**## PAPER-GRO-B4 (MAJOR) — Sec. 5.3 + Table VI (lines ~1050-1120)**

The monopole-only N=500 null reproduces 99.3% of pre-MASTER pseudo-C_ℓ(ℓ=1) but only ~12% of the post-MASTER canonical residual; the remaining 88% is attributed to depth/PSF/morphology without a joint nuisance-marginalized model fit that simultaneously includes a primordial dipole template. The three-discriminator argument against a clean cosmological dipole is post-hoc.

Fix: Add the joint 9-template (dipole + leg + density + density²) WLS fit already performed in the artifacts as a main-text result; report the bootstrap-corrected z(data vs. 1.7%) = −18.1 as the formal exclusion of interpretation (i).

**## PAPER-GRO-B5 (MAJOR) — Abstract + Sec. 1 (lines ~60-90)**

The paper correctly notes that the ℓ=1 dipole is parity-EVEN (isotropy test, not parity violation), yet the title, keywords, and opening paragraphs continue to frame the measurement as a "chirality dipole" in language that historically conflates the two channels. Prior literature citations are not audited for this exact conflation.

Fix: Add a one-sentence parenthetical in the abstract: "(the ℓ=1 observable is parity-even axial-vector; the parity-odd analog requires 3D spin or polarization observables outside this scope)."

**## PAPER-GRO-B6 (minor) — Sec. 4.2 + footnote on MC counts (lines ~850-880)**

MC ensemble sizes are inconsistent across estimators (500 for MASTER, 1000 for pseudo-C_ℓ, 10000 for real-space dipole) with no justification or convergence test; the 500-MC rank resolution (0.2%) is marginal for quoting p_MC≈0.45 on the headline null.

Fix: Standardize on N_MC=10000 for all final quoted significances or demonstrate convergence of the 500-MC null distribution to <1% relative error on σ_null.
