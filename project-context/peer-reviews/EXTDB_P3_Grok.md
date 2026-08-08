# EXTDB P3 Grok — chat: https://grok.com/c/2b99dc06-967c-4157-b1f6-43f2155827e5

Provider: Grok
Model/Tier: Expert
PDF: /tmp/EXTDB_P3.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

Paper: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches (Houston Golden, June 2026)

1. Recommendation
MAJOR REVISIONS

The work is ambitious in scale, methodologically thoughtful, and unusually transparent about its own limitations and failures. It delivers a genuine technical advance in multi-survey unsupervised anomaly detection and a reusable Path-C validation protocol. However, one serious reproducibility flaw in the eROSITA tier, combined with insufficient foregrounding of the distinction between the full headline catalog and the validated "catalog-grade" subset, prevents acceptance in its current form. These are fixable with targeted revisions; the underlying science and engineering are sound.

2. BLOCKERS

None that are strictly fatal, provided the eROSITA issue below is resolved. The paper already quarantines ACT cleanly and labels multiple tiers exploratory.

3. MAJORS

M1 — eROSITA DR1 tier: irreproducible scoring axis and provenance gap (HIGH severity)
The production threshold (0.259 on the "score-knee axis") cannot be recovered on any of 16 monotone rescalings of the committed raw reconstruction scores, nor on retrained IsolationForest axes. Per-object S_BigAE values in the released table are non-monotone with the raw artifact (Spearman ρ = −0.10 across the top five). The text correctly states that an "undocumented post-hoc rescaling step in the production scoring run whose code was never committed" is the most plausible cause, and pivots to releasing the n = 298 membership list itself as the canonical, reproducible product.
This is unacceptable for a catalog-release paper, even with the exploratory validity flag already attached (1.2 % injection-recovery at 5σ; 81.5 % XV-stability is the highest of any survey but still a FAIL). Downstream users cannot reproduce the exact selection or perform score-weighted analyses from the published numbers.
Required action: Re-derive or fully document a reproducible scoring axis that exactly recovers the committed 298-member list from the raw artifact (or demonstrate why the raw-score ranking + membership list is the only usable product). Add an explicit schema-flag column or README warning. Recompute and clearly state whether the 269,317 catalog-grade unique count includes or excludes the eROSITA tier.

M2 — Headline numbers vs. validated content clarity (MEDIUM-HIGH severity)
The title, abstract, and §VII conclusions prominently feature the inclusive 378,280 Path-C unique count (and the ~141× / ~73× scale claims). The text is internally consistent and transparent that: ~98.7% of DESI anomaly clusters fall on sky-fiber/filler spectra (only 2,468 on validated science-target spectra, ≈0.9× the Liang et al. benchmark); LAMOST is retained only as a methodological lesson; Gaia and eROSITA carry exploratory flags; the recommended catalog-grade tier is 269,317 unique objects.
Required action: Strengthen the tier distinction in the Abstract, first paragraph of §I, and Conclusions point 1. Consider an explicit boxed summary distinguishing the full 378k Path-C count from the 269k catalog-grade subset.

M3 — Validation completeness for the flagship DESI tier (MEDIUM severity)
DESI (195k objects at S > 5) passes 5-fold Jaccard (J̄ = 0.862) and OOD production-vs-control Jaccard (J̄ = 0.732), and top-200 visual inspection finds 0/200 artifacts. However, "DESI injection-recovery was not executed." For a catalog paper of this scale, either run a DESI injection-recovery test or provide a quantitative argument why the existing gates plus the science-class recount and visual inspection suffice.

4. MINORS

m1 — eROSITA presentation: Ensure the released catalog carries explicit "membership-list only / irreproducible axis" schema flag in a machine-readable way, not just in prose.
m2 — Gaia preprocessing: The 20-feature specification is "lineage-inferred" from a successor run. Strengthen the exploratory-flag language accordingly.
m3 — Cosmology section (§V): The empirical α_jk = 0.19 ± 0.65 result is already handled honestly; ensure abstract and conclusions never headline even a qualified "improvement" without immediately pairing it with the consistency-with-null statement.
m4 — NANOGrav environmental caveat (§V A): Keep the explicit warning that the decisive Bayes factor is only vs. the idealized circular-orbit SMBHB reference.
m5 — Minor presentational: A one-sentence "Catalog tiers at a glance" box or table in the introduction would help readers navigate the multiple overlapping counts.

5. Strengths

1. Intellectual honesty and methodological self-audit at an unusually high level. The LAMOST 98% blue-excess training-bias artifact is called out as "the single most important methodological lesson of this work." ACT is cleanly quarantined in Appendix F. Table V enumerates 10 residual caveats with resolution status. This degree of transparency is rare in catalog papers.
2. Path-C protocol and multi-gate validation framework. Native per-survey retraining + explicit Jaccard / injection-recovery / validation-loss gates, followed by systematics masking and 7-way 5″ deduplication, is a reusable contribution. The protocol correctly identifies and mitigates the two first-order cross-transfer failure modes (LAMOST bias, undertrained CMB autoencoder).
3. Scale achieved with documented reproducibility infrastructure. 37.3M sources/patches processed, public release plan with HuggingFace staging, GitHub weights/scripts, Zenodo DOI, SHA-256 manifest, and pod-provenance JSON.
4. Scientific framing and cosmological tie-in without hype. The current multi-tracer result is reported as a noise-driven central-value forecast with no improvement after de-biasing — exactly the correct stance.
5. Clear separation of exploratory vs. validated content. The text repeatedly directs readers that robust science should rely on the DESI, SDSS-native, and Planck components; Gaia and eROSITA are flagged.
