# P3_v3150_R12 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1400pt
**Wall time**: 122.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=65372, completion=13616, reasoning=12373, total=78988

---

## BLOCKER: OOD MSE Contradiction (Multi-Round Carry)
**ID:** PAPER-GEM-B1
**Section:** 2.2 (In-sample scoring and held-out validation)
**Concrete Issue:** The text claims the 0.87% anomaly rate is "preserved on this independent OOD sample," but explicitly states the 100k OOD sample has a median MSE of 0.178, which is *above* the absolute catalog threshold of MSE $\approx 0.143$. It is mathematically impossible for the 0.87% rate to be preserved if >50% of the OOD sample exceeds the absolute threshold. 
**Fix:** Either report the actual >50% anomaly rate on the OOD sample (and admit the model fails to generalize to the broader catalog), or clarify that the 0.87% rate was achieved by computing a new relative 99.13th percentile threshold on the OOD sample rather than using the absolute 0.143 cut.

## BLOCKER: Mathematically Impossible Headline Arithmetic
**ID:** PAPER-GEM-B2
**Section:** Title, Abstract, 4.3, 6.4 caveat (a)
**Concrete Issue:** The title and abstract claim "378,280 Unique Anomalies", but Section 6.4 caveat (a) explicitly admits this number is mathematically impossible given the 637 pairwise cross-matches (which yields 387,856) and leaves the impossible number "frozen... pending a recompute". A known, acknowledged arithmetic error cannot remain in the title and headline metrics of a finalized paper.
**Fix:** Execute the union-find cluster manifest recompute and update the title, abstract, and tables to the mathematically correct value (e.g., 387,856), removing the stale deferral.

## MAJOR: Fisher Error Propagation Terminology
**ID:** PAPER-GEM-M1
**Section:** 5 (Cosmological Applications)
**Concrete Issue:** The text conflates the $+1\sigma$ tail of the $\sigfnl$ forecast with the $+1\sigma$ tail of the bias enhancement $\alpha$. It states "the linear-extrapolation $+1\sigma$ tail $\sigfnl = 10.64$... the $+1\sigma$ tail of $\alpha$ instead drives $\sigfnl$ down". The value 10.64 corresponds to $\alpha = -0.46$, which is the **$-1\sigma$** tail of $\alpha$, not $+1\sigma$.
**Fix:** Correct the text to state that the $+1\sigma$ tail of $\sigfnl$ (10.64) corresponds to the $-1\sigma$ tail of $\alpha$, and that under the $\alpha^2$-form, the $-1\sigma$ tail of $\alpha$ drives $\sigfnl$ down to 5.95, avoiding the unphysical 10.64 extrapolation.

## MAJOR: Multi-Tracer Fisher Mode-Counting Artifact
**ID:** PAPER-GEM-M2
**Section:** 5 (Cosmological Applications)
**Concrete Issue:** The text claims an internal Fisher matrix yields $\sigfnl \approx 0.07$ and that the linear bias nuisance parameter $\delta b$ is "absorbed by the multi-tracer cross-correlations" without degrading the constraint. This is an unphysical EFT mode-counting artifact caused by omitting the photo-z radial damping kernel, which artificially grants photometric tracers infinite spectroscopic radial modes, spuriously breaking the $\delta b$ degeneracy.
**Fix:** Explicitly state that the "absorption" of $\delta b$ and the $\sigfnl \approx 0.07$ floor are unphysical artifacts of the missing photo-z radial damping kernel, not a physical property of the multi-tracer technique.

## MAJOR: eROSITA S-score Standardization
**ID:** PAPER-GEM-M3
**Section:** 3.4 (eROSITA DR1)
**Concrete Issue:** The eROSITA anomaly threshold is defined as $S > 0.259$, which yields 298 anomalies out of 930,203 (the top 0.03%). Equation 2 defines $S$ as a z-score (mean 0, variance 1 on the validation set). A z-score of 0.259 cannot mathematically represent the 99.97th percentile unless the validation distribution is pathologically skewed or the standardization math is broken.
**Fix:** Verify the $\mu_{\rm val}$ and $\sigma_{\rm val}$ computation for eROSITA; if $S=0.259$ is truly the 99.97th percentile, explicitly note the extreme non-Gaussianity of the latent MSE distribution that causes a $\sim 0.26\sigma$ deviation to act as a 1-in-3000 outlier cut.

## minor: Stale Version Deferrals
**ID:** PAPER-GEM-m1
**Section:** 6.4 (Path-C Rebuild Residual Caveats)
**Concrete Issue:** The text lists multiple unresolved tasks (union-find arithmetic, BigAE-IF intersection table, full Fisher recompute) as "queued for v3.1.44+" or "v3.1.46+ task". The current manuscript is v3.1.50, making these version references stale and highlighting that load-bearing technical debt is being ignored across multiple revisions.
**Fix:** Either execute the deferred recomputes, or update the text to reflect the current version (v3.1.50) and explicitly state why these critical verifications remain undone.
