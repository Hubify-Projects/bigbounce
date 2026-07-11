# INT Claude-subscription Review — P3 v3.1.154 — claude-opus-4-8
paper: P3  version: v3.1.154  tex: pipelines/p3_anomaly_engine/paper3_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T15:52:12Z
context-note: rebuild wave 2/2 on v3.1.154; no changes since FR2 (fix verified by independent recompute)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have verified the key numbers against the committed artifacts by recompute. My referee assessment follows.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR] Internal rounding inconsistency in the NANOGrav parameter-shift pair — the matter-bounce shift disagrees with its own committed chain.** `pipelines/p3_anomaly_engine/paper3_draft.tex:1553` (echoed at L994, L1618, L1636, L1857). The paper reports the matter-bounce γ=3.0 at **+1.13σ** and the SMBHB γ=4.33 at **+4.63σ** in the same sentence, computed from γ = 2.567 ± 0.382. But the committed chain (`pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json`, `z_distances_gamma_marginal_gaussian`) gives `matter_bounce_3p0 = 1.13543` and `smbhb = 4.62743`. The SMBHB value was just corrected to +4.63σ (full precision) in v3.1.154, but +1.13σ for the matter bounce matches only the *display-precision* recompute `(3.0−2.567)/0.382 = 1.134`; the committed full-precision value `1.1354` rounds to **+1.14σ**. The pair is thus self-inconsistent: full precision → (+1.14, +4.63); display precision → (+1.13, +4.62). The matter-bounce shift should read +1.14σ to match the artifact and the convention used for the SMBHB value in the same clause.

2. **[MINOR] Presentation density / caveat repetition impairs readability to a degree a real referee would ask to be fixed.** Abstract (L986–994), §III three-tier block (L1100–1108), Table `tab:survey_summary` footnote apparatus (L1170–1187). The "process-volume, not confirmed detections" framing is restated three times in the abstract alone; the 268,519-vs-2,468 and 141×/73×-vs-0.92× distinctions recur across abstract, intro, §III, §desi, and conclusions. The disclosure is scientifically honest and complete, but the redundancy (multiple near-identical footnotes, nested parentheticals, repeated tier definitions) is excessive for a PRD article and should be consolidated once and cross-referenced. This is the paper's single largest weakness; it is presentational, not a scientific error.

3. **[MINOR] Trivial last-digit rounding in F₀.** `paper3_draft.tex:1520`: `F_0 = 1/(8.98)^2 = 0.01239`. Recompute: 1/80.6404 = 0.0123997, which rounds to **0.01240**, not 0.01239. Downstream arithmetic (1/σ² = 0.01509, σ = 8.14, envelope [3.92, 8.98], 9.4%) all verify correctly, so this is cosmetic, but should read 0.01240.

4. **[MINOR] The "decisive" Bayes factor headlines the 1D uniform-prior result while the artifact's 2D SMBHB-native-prior result is not surfaced in the body.** `paper3_draft.tex:1553`. B_MB/SMBHB = 7.14×10³ (log₁₀B = +3.85) is the 1D γ-only Savage-Dickey (verified: `B_matter_bounce_vs_smbhb = 7137.6` in the JSON). The same committed file reports a 2D SMBHB-log₁₀A-prior analysis giving B_SMBHB/free = 0.0148 (log₁₀ = −1.83). The environmental-SMBHB caveat (L1555) correctly scopes the claim to the idealized circular-orbit reference, but showing the 2D-prior number in-text would preempt the obvious referee question about prior sensitivity of a "decisive" classification.

**Verified clean (recomputed against committed artifacts):** the validated headline dedup 195,829+77,905+200+419 = 274,353 → 268,519 unique / 268,319 point-source with 5,834 collapsed (2.13%) reproduces exactly (`reproduce_headline_dedup.json`); the Savage-Dickey factors 3.23 / 4.52×10⁻⁴ / 7.14×10³ / +3.85 match the chain; the f_NL Fisher chain (c=0.0747 grid, de-biased max(0, 0.0361−0.4225)=0, envelope [3.92,8.98]) is arithmetically correct; the provenance/process-volume reconciliation (36.76M / 36.93M / 37.29M) is internally consistent.

**(3)** The central claim — a reproducible, honestly-tiered multi-survey anomaly-*candidate* catalog (with the two cosmology items explicitly framed as null secondary demonstrations) — **is supported**: the headline count is directly recomputable from committed data and every number I independently recomputed matches, with only the minor rounding/presentation items above outstanding.
