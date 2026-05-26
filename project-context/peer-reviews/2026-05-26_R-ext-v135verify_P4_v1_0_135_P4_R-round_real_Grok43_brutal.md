# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v135verify_P4_v1_0_135
**Wall time**: 26.1s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=93211, completion=2298, reasoning=1596, total=95509

---

**PAPER-GRO-B1**  
**Title + Abstract (L1-2, abstract para 1)**  
**BLOCKER**  
Title frames result as "No Evidence for Large-Scale Parity Violation," but abstract and §I explicitly state the ℓ=1 dipole is parity-EVEN axial-vector and "NOT a direct parity-violation test." Framing mismatches content.  
**Fix:** Retitle to "No Evidence for Large-Scale Isotropy-Breaking Chirality Dipole on 8.47M DESI Legacy Galaxies."

**PAPER-GRO-B2**  
**Abstract + §VI.D (multi-null battery)**  
**MAJOR**  
Claims "favored verdict" for interpretation (ii) depth/morphology systematic on basis of ℓ=2 > ℓ=1, cross-spectrum r=-0.65 (σ=-2.89), and quartile washout. But text acknowledges no joint nuisance-marginalized fit; bootstrap is tautological; cross-spectrum is single-multipole and marginal post-trials. Overstates positive evidence against (i).  
**Fix:** Replace "favored verdict" and "directly confirmed" with "most consistent with" and "suggestive but not confirmatory pending joint model fit."

**PAPER-GRO-B3**  
**§IX (Conclusions) + sensitivity section**  
**MAJOR**  
States "most sensitive chirality measurement ever performed" with sub-percent sensitivity. Empirical 50%-recovery-3σ threshold is 0.75% on HC subsample (471k); full-catalog injection claims ≤0.50% but is not the load-bearing estimator. Fisher 0.29% is asymptotic only. "Most sensitive" is not load-bearing.  
**Fix:** Qualify as "largest sample with equivariant TTA" or drop superlative; report both HC and full-catalog thresholds explicitly.

**PAPER-GRO-B4**  
**§VII (Shamir comparison)**  
**MAJOR**  
Headline states inconsistency "by a factor of ~6-12 in amplitude" with Shamir 2020/2022. Text immediately adds "not strictly like-for-like" and "no likelihood-level exclusion" without matched Ganalyzer reanalysis. The numerical factor is not supported by performed analysis.  
**Fix:** Remove factor claim from body; retain only as "amplitude difference under present pipeline" in footnote.

**PAPER-GRO-B5**  
**§I + abstract (novelty framing)**  
**minor**  
Describes catalog as advancing "beyond CE-ResNet in three respects" and "the most sensitive." Prior nulls (Iye 2021, Tadaki 2020) exist on smaller samples; size advantage is real but method + footprint differences prevent clean "unprecedented" claim.  
**Fix:** Change to "largest equivariant-TTA chirality catalog to date" without comparative superlatives.

**PAPER-GRO-B6**  
**Table II + §IV.D (monopole leakage)**  
**minor**  
Table and text promote 88% "requires depth/PSF/morphology" after monopole-only null accounts for 12%. This is post-hoc partitioning of residual; no template regression or full systematics model is executed. Number is illustrative, not load-bearing.  
**Fix:** Demote 12%/88% split to footnote or remove; retain only the direct null result (monopole explains ~12%).
