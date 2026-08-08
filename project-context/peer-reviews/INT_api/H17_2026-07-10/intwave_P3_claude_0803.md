# INT Claude-subscription Review — P3 v3.1.153 — claude-opus-4-8
paper: P3  version: v3.1.153  tex: pipelines/p3_anomaly_engine/paper3_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T15:03:00Z
context-note: FR1 fresh round on the July-11 restamped version (no content change since exit)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have completed verification of the load-bearing claims against committed artifacts. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

The central deliverable — a validated catalog-grade subset of **268,519** unique anomaly candidates — is honestly framed, appropriately scoped, and *directly reproducible*: I recomputed the chain from the committed `outputs/reproduce_headline_dedup.json` and confirmed 274,353 → 268,519 (5,834 detections collapse, 2.13%), the four-survey inputs (195,829 + 77,905 + 200 + 419), and the 377,482 inclusive / 387,695 pre-dedup sum all match to the digit. The DESI injection-recovery headline (broad class 99% at 5σ, 100% at ≥8σ) is confirmed in `desi_injrec_CORRECTED.json`, and the NANOGrav posterior (γ=2.567±0.382, ESS≈5507, τ≈58, accept 0.632, B_MB/SMBHB=7137.6) is confirmed in `free_spectrum_real_2026-05-01/results.json`. The paper is unusually candid about its own limitations (single architecture, in-sample DESI scoring, one production-ensemble gate + correlated proxy checks, null secondary cosmology). The remaining issues are confined to the secondary cosmology section and to presentation, not the central claim — hence MINOR.

**(2) ISSUES**

1. **[MAJOR] f_NL empirical-bias claim contradicts the only committed bias artifact.** §VI "Empirical bias measurement" (`paper3_draft.tex:1516`) reports α_jk = 0.19 ± 0.65 on the 5,384 sample and α_GS,jk = +1.83 ± 2.03 on the 1,122-object Gold+Silver sample, both "consistent with zero." But the sole committed bias-calibration file, `bias_calibration/bias_empirical.json` (n_tracers = **1122**), reports α = 0.80 ± 0.155 with a **4.19σ** tension from the fiducial 0.15 and the explicit verdict `"empirical α deviates from theory > 1σ — update Papers"`. For the same 1,122-object sample the committed artifact (0.80±0.155) is irreconcilable with the paper's GS number (1.83±2.03). A referee running the committed pipeline gets a >4σ result opposite to the paper's null — which directly undercuts the paper's stated "reproducibility-by-construction" ethos (`:1653`). The actual Landy–Szalay analysis is said to live "in the companion data repository," so the reported bias is *not verifiable from the committed tree at all*. This does not touch the 268,519 headline (which is fully reproducible), but the contradicting committed file must be reconciled, superseded, or removed, and the load-bearing LS artifact committed.

2. **[MINOR] Absolute σ(f_NL)=8.98 baseline is an external normalization the committed engine does not reproduce.** §VI Fisher forecast (`:1519`, `:1599`) and `r43_4caveats_closure/result.json` agree on F₀=0.012401, c=0.0747 and the α-grid, but the artifact's own `engine_normalization_note` states the committed Fisher engine yields σ_fNL ~ O(10⁻⁷), not 8.98 — only the scale-invariant c/F₀=6.02 ratio is reproducible. The 8.98 anchor thus rests on an undocumented external normalization. Disclosed obliquely (the Appendix-C figure carries a different 16.85 normalization), but the origin of 8.98 itself should be stated.

3. **[MINOR] NANOGrav γ=4.33 parameter-shift mis-rounded.** Text states the SMBHB reference sits at +4.61σ (`:1552`, `:1617`); the committed chain gives (4.333−2.5665)/0.3818 = **4.627σ** (→ +4.63σ). Trivial, but should match the artifact.

4. **[MINOR] A superseded NANOGrav artifact coexists in the repo.** `r42_results/wave_14_rr_nanograv_bayesian.json` reports a *different* analysis (γ=3.201±0.420, 6 signal bins) that is not what the paper reports. It is unreferenced but sits alongside the correct file; a referee browsing `outputs/`/`r42_results/` could easily mistake it. Flag or archive it.

5. **[MINOR] Presentation density harms readability.** The abstract repeats the "process-volume, not confirmed detections" disclaimer 3+ times (`:985`, `:987`, `:993`); §III opens with a three-tier block plus a multi-paragraph footnote thicket (`:1169`–`:1186`) whose caveats overlap heavily. The disclosure is admirable but a real PRD editor would request substantial compression — the honest content is currently hard to extract.

6. **[MINOR] Three residual overfull \hbox in tables.** `paper3_draft.log` shows sub-7pt overfull boxes at the provenance table (`:1112–1122`), caveats table (`:1582–1595`), and Bayes-factor-robustness table (`:1846–1853`). All <7pt and cosmetic, but a `table*`/column-width pass would clear them. (0 undefined references — clean.)

**(3)** Yes — the central claim (a reproducible, honestly-tiered 268,519-object validated multi-survey anomaly catalog) is supported by the committed artifacts I recomputed; the only substantive weakness (Issue 1) is quarantined in the explicitly-null secondary f_NL demonstration and does not affect the headline result.
