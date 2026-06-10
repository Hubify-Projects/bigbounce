# R26conf P3 — TRUTH AUDIT (clean-round determination)

**Auditor**: Claude (in-session), 2026-06-10, against `pipelines/p3_anomaly_engine/paper3_draft.tex` (working tree, post-audit edits; recompiled clean: 0 overfull hbox, 0 undef refs, 26 pp).
**Scope**: all R26conf SYNTHESIS + META_REVIEW findings (Claude_brutal ×2, Gemini, Grok, META gpt-5-pro; OpenAI + Perplexity returned 0 findings).
**Ground truth used**: `pathc_dedup/r23conf_dedup_audits.json` (9,553 clusters, size histogram, 637 two-survey), `pathc_dedup/pathc_dedup_summary{,_no_act}.json`, `r24conf_pod_session_batch.json` (item34 6-way dedup 269,317/269,117; item35 HEALPix 24,049/χ²ν15.7), `r24conf_erosita_axis_sweep.json`, `cmb_native_retrain.py` (L136-150 normalize-then-save; L304-345 bump added post-standardization, no re-standardize, INJECT_AMP=5.0).

## IN-SESSION findings (Claude_brutal, pre-flagged NOT-closed → closed this wave)

| ID | Claim | Verdict | Disposition |
|----|-------|---------|-------------|
| M1 | Fig.2 caption reads as if dedup grows 319,443 → 378,280 | **VERIFIED** | Caption rewritten: 378,280 = 7-way dedup of native tallies (388,493), not of this baseline; "dedup only ever reduces its input" made explicit. **CLOSED.** |
| m1 | Table I cross-transfer total row mixed basis (DESI native) | **VERIFIED** | Basis note added to footnote ‖: DESI is anchor, cross-transfer ≡ native for DESI. **CLOSED.** |
| m2 | eROSITA S-axis warning for downstream meta-analyses | **VERIFIED** | Loud "Practical consequence" sentence added §IIIE: score-axis meta-analyses impossible; raw artifact + n=298 membership are the only reproducible products. **CLOSED.** |
| m3 | 141× multiplier includes LAMOST exploratory tier (~29%) | **VERIFIED** | "~100× catalog-grade" (269,117/2,685=100.2) added beside 141× in abstract + Conclusions. **CLOSED.** |
| N1–N5 | 24,049 rerun, SMICA footnote, χ²ν ordering, Fig.3 dual scale, Fig.11 abs-vs-rel | all-clear/OPINION | N1/N2 explicit all-clears; N3/N4/N5 polish, not blockers (N5 figure re-render = optional queue). |

## ESSENTIAL

| ID | Claim | Verdict | Disposition |
|----|-------|---------|-------------|
| META-E1 | Tabular feature scaling/imputation (eROSITA 47f, Gaia 20f, NEOWISE 15f) unspecified → S irreproducible | **VERIFIED → QUEUED** | True: tex documents spectroscopic normalization + Planck patch recipe but no tabular-feature spec. Pod-era trainer scripts not in local tree (searched pipelines/, h200_scripts/); pattern-036 forbids fabricating the recipe. **Queue: recover per-survey tabular preprocessing spec from pod backup/HF artifacts and commit schema.** |
| META-E2 | 9,553 clusters vs 637+9,576=10,213 not reconciled | **VERIFIED** | Reconciled exactly from committed artifact: histogram sums to 9,553 clusters, Σ(size−1)=10,213, 637 two-survey clusters (none ≥3-survey), 10,213−637=9,576 intra-survey, 8,916 single-survey clusters. Tying paragraph added §IVC. **CLOSED (artifact-backed).** |
| META-E3 | Planck injection σ convention vs per-patch standardization ambiguous | **VERIFIED** | Script-confirmed: bump added to already-standardized patches, no re-standardization → amplitude exactly 5× pre-injection patch std. Convention note added Table V footnote. **CLOSED (script-backed).** |
| Grok-E1 / Gemini-E1 / Gemini-E4 | Remove "earlier draft / withdrawn" correction notes | **HOUSTON-DECISION** | Standing disclosure policy; correction-note removal = Houston call (per round rules). Not touched. |
| Gemini-E2 | eROSITA selection non-reproducible | **PARTIAL→CLOSED** | Disclosure already exhaustive (16-rescaling sweep, membership-list anchor); in-session m2 closure adds the downstream warning. Score-axis recovery itself is impossible (documented), not queueable. |
| Gemini-E3 | Fig.11 σ normalizations side-by-side misleading | **STALE** | Caption carries full normalization disclaimer (prior-round closure); relative-units re-render = optional figure-regen queue. |
| Gemini-E5 | Eq. E1 NANOGrav likelihood non-standard/dimensionally wrong | **FALSIFIED** | Recomputed: ρ_i² = A²(f_i/f_yr)^{3−γ}/(12π²f_i³T) ⇒ log₁₀ρ_i = ½[2log₁₀A − log₁₀(12π²) + (γ−3)log₁₀f_yr − γlog₁₀f_i − log₁₀T] — matches Eq. E1 term-for-term (standard free-spectrum ρ convention). |
| Grok-E2 (length 25pp) | **HOUSTON-DECISION** | Format/venue call. |
| Grok-E3 (8.14 vs 8.98 framing) | **STALE** | Abstract leads with de-biased no-improvement; envelope rule explicit (R24conf closure). |
| Grok-E4 (dedup completeness; Planck "quarantined") | **PARTIAL/FALSIFIED** | Planck is retained, ACT is quarantined (reviewer conflated). Completeness bounded by 3″/5″/7″ sweep (0.086%) + Budavári–Szalay disclosure. |

## MAJOR

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-M1 (gate thresholds not pre-registered) | **VERIFIED** | Honest provenance sentence added §VID(ii): heuristic design-time thresholds, margin analysis (only SDSS 64%-vs-50% could flip). **CLOSED (textual).** |
| META-M2 (NEOWISE counted as PASS) | **VERIFIED (partial-prior)** | Abstract + Fig.10 caption already carried by-construction disclaimer; explicit "2 detector-sensitivity + 1 geometry-QA" decomposition added §VID(ii). **CLOSED.** |
| META-M3 (w(θ)→bias formula absent) | **STALE/QUEUED** | Same family as R24conf META-M4 queue (geomean LS estimator artifact not locally recoverable). Queue stands. |
| META-M4 ("1σ envelope" label) | **VERIFIED** | "Image of ±1σ interval in α — translated band, not 68% interval for σ(fNL)" added §V. **CLOSED.** |
| META-M5 (stratified SNR sample p-value) | **VERIFIED** | Caveat added §IIIA (stratified design ≠ population p; effect size operative); random-subsample recompute queued. **CLOSED (textual) + QUEUE.** |
| META-M6 (Planck×ACT null over-interpreted) | **VERIFIED** | Rewritten: geometry-driven null is non-diagnostic; systematics case rests on ACT gate failures + Planck scanning concentration. **CLOSED.** |
| Gemini-M1 (Fig.9 fixed-α forecast misleading) | **STALE** | §V declares empirical-α primary, fixed-α "retained for reference in Appendix C"; Fig.9 caption labels it the reference forecast. |
| Gemini-M2 (validation failures under-discussed) | **STALE** | FAIL-with-diagnostic in abstract, Table I footnotes, §VID(ii), Limitations (2). |
| Gemini-M3 (Fig.8 display scores) | **STALE/QUEUED** | Caption warning in place (R23conf); on-plot relabel = figure-regen queue (R24conf M4). |
| Grok-M1 (17.8% no bootstrap/radius sweep) | **STALE/PARTIAL** | Wilson 68% CI ±1.2% + single-stratum caveat printed; radius-variation recompute = queue (low priority). |
| Grok-M2 (SDSS UCD tail no PM/parallax cut) | **VERIFIED → QUEUED** | Recompute-class: Gaia PM cross-match on the S>10¹⁰ tail. |
| Grok-M3 (α=0.19 dual use) | **STALE** | De-biased α²=0 result primary; envelope rule explicit. |

## MINOR / NIT

| ID | Verdict | Disposition |
|----|---------|-------------|
| META-m1 (cross-survey S comparability) | **VERIFIED** | Blanket non-comparability sentence added at Eq. (2). **CLOSED.** |
| META-n1 (total-row Rate %) | **VERIFIED** | Rate note added footnote ‖ (bookkeeping ratio, not measured frequency). **CLOSED.** |
| Gemini-m1 (gold dual use) | **STALE** | Disambiguated R23conf (Fig.1, §IIA, §V tier block). |
| Gemini-m2 (fNL systematics sentence) | **FALSIFIED/STALE** | §V already has the requested 1–2 sentences (4n+1 nuisance block, δs dominant). |
| Gemini-m3 (GR 0.02% uncited) | **VERIFIED** | Labeled internal order-of-magnitude bound from (H/k)² suppression. **CLOSED.** |
| Gemini-m4 (abstract §VI ref wrong) | **FALSIFIED** | Liang size benchmark IS in §VI (Comparison with Prior Work subsection, L677). |
| Gemini-m5 (abstract §II for SDSS slice) | **FALSIFIED/OPINION** | §II (L229) defines the continuity slice and points to footnote ♥. |
| Gemini-m6 (§IID → §VIA ref) | **FALSIFIED** | Source ref is `\S\ref{sec:lamost_lesson}` = the LAMOST before/after diagnostic section — correct target. |
| Gemini-m7 (footnote § → VID(ii)) | **FALSIFIED** | §VID(ii) is the injection-recovery + XV-stability synthesis; Limitations (1) uses the same pointer for IF stability — internally consistent. |
| Gemini-N1 (title length) | **HOUSTON-DECISION** | |
| Gemini-N2 ("June 2026" date) | **AUTO-FALSIFIED** | It is June 2026 (future-date class). |
| Grok-N1 (0.259 not 99th pctile undisclosed) | **FALSIFIED** | Table I caption states "fixed top-298 cap (≈top-0.03%; production-run score-knee 0.259, axis distinct…)". |
| Grok-N2 (μ_val/σ_val per survey unlisted) | **STALE/PARTIAL** | DESI values printed; per-object scores released for alternate cuts; full constants table = data-release item. |

## Verdict counts (P3, this wave)
- ESSENTIAL: 3 META audited → 2 CLOSED (E2 artifact-backed, E3 script-backed), 1 QUEUED (E1); 4 reviewer-E → 2 HOUSTON, 1 FALSIFIED, 1 PARTIAL→CLOSED/STALE.
- MAJOR: 6 META → 5 CLOSED textual, 1 STALE/QUEUED; 6 reviewer-M → 5 STALE, 1 QUEUED (Grok-M2).
- In-session M1+m1+m2+m3: all 4 CLOSED per Required fixes. Minors: 3 closed, 4 falsified, rest stale/Houston.
- Zero verified arithmetic errors; count web reconciles end-to-end (in-session ledger + this audit's cluster-accounting tie-out).
