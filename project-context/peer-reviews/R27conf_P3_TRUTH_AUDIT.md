# R27conf P3 — TRUTH AUDIT (v3.1.86 → v3.1.87, closures applied 2026-06-10)

Auditor: in-session Claude. Ground truth: `pipelines/p3_anomaly_engine/paper3_draft.tex`, `recovered_pod_scripts/` (erosita_scan.py L18–24/L99 verified this audit), `pathc_dedup/` artifacts, axis-sweep JSONs, R26conf truth-audit precedents.
Auto-falsify rules: future-date → FALSIFIED; recompute claims need SAMPLE+ESTIMATOR+NULL match; correction-note/length/REJECT → HOUSTON-DECISION/OPINION.

## In-session leg (Claude_brutal_INSESSION, M=4 pre-flagged NOT-closed → closed this wave)

| ID | Claim | Verdict | Disposition |
|---|---|---|---|
| M1 (Gaia 20f/21f ranking-perturbation bound) | recompute | **VERIFIED** | **QUEUED**: requires Gaia 50K parent-sample re-run with 21f config; not locally cheap (no committed Gaia parent features). Disclosure already maximal ("lineage-inferred") |
| M2 (47-feature transform split ambiguous) | presentation | **VERIFIED** | **CLOSED (script-backed)**: explicit "33 log-transformed (RATE/FLUX/CTS ×11) vs 11 DET_LIKE + 3 aux standardized-only" split added §II.B; matches erosita_scan.py L99 (`n_log = RATE+FLUX+CTS`) exactly |
| M3 (98% blue-excess→training-bias needs control number) | claim-truth (calibration) | **VERIFIED (partial)** | **CLOSED (textual) + QUEUE**: §III.D now states the attribution rests on the measured 21.5× native-retrain rate compression and discloses that the post-retrain arm fraction is not re-tabulated (pattern-036: no invented X%). Re-tabulation queued |
| M4 (ACT quarantine "why" missing from abstract) | presentation | **VERIFIED** | **CLOSED**: abstract now carries val_loss ≈2.2×10⁴ / both-gates-fail / zero-headline-objects clause (numbers from Table I caption, pre-existing) |
| m1 (count-correction digression in abstract) | presentation | HOUSTON-DECISION | Count-correction-canonical framing is a standing Houston directive; reviewer's own pass-2 retrospect holds it as non-substantive |
| m2 (20 catalogs unenumerated in abstract) | presentation | **VERIFIED** | **CLOSED**: 10-catalog sample + §IV pointer added to abstract (list source: §IV.A L481) |
| m3 (BAL QSO needs per-object entry) | presentation | FALSIFIED-as-stale | §IV.B bullet (L545: broad Mg II, both spectra, absent SIMBAD/Milliquas/NED) + Fig. panels (e,f) already constitute the per-object entry the fix asks to "verify" |
| N1/N2 + all-clears | — | N/A | Changelog comments verified vs PDF; count web 378,280/269,317/269,117 tie-out re-confirmed by reviewer |

## META_REVIEW (gpt-5-pro)

| ID | Class | Verdict | Disposition |
|---|---|---|---|
| META-E1 (Planck gate validated at 99th pctile, selection at top-200/200K ≈ 99.9th) | recompute | **VERIFIED** | **QUEUED**: re-run injection-recovery at ≥99.9th-pctile threshold (pod-side; CAE checkpoint + patch bank required). Genuine new blind spot; not closable textually without the number |
| META-M1 (absolute 0.30 val-loss gate not scale-free) | recompute/method | VERIFIED-PLAUSIBLE | **QUEUED** (low): gate already dual (OR injection-recovery ≥50%); Planck disclosed as raw-MSE exception. Scale-free re-evaluation = methods-hardening queue |
| META-M2 (NaN→0 conflates missing with value) | recompute/method | VERIFIED-PLAUSIBLE | **QUEUED**: documented honestly in §II.B (recovered production spec — changing it = new catalog, not a textual fix); impact quantification joins Gaia M1 queue |
| META-M3 (arm dominance not variance-normalized) | claim-truth (caveat) | PARTIAL/STALE | §II.B already states per-arm sub-scores "not independently z-scored … used only for within-object comparisons"; Table VI global fractions inherit the printed caveat. Sensitivity re-tab queued with M3 above |
| META-M4 (kmax 3D bound vs angular θ-space measurement) | claim-truth | VERIFIED-PLAUSIBLE | **QUEUED** (ℓ-space restatement or Limber mapping); GR-projection bound is a conservatism note, not load-bearing for the [3.92, 8.98] envelope |
| META-m1 (bump-only injection morphology) | recompute | QUEUED | Joins META-E1 Planck injection queue |
| META-m2 (multi-catalog chance-match multiplicity) | recompute | PARTIAL | §IV.A already prints per-catalog false-match rate (0.24% SIMBAD) + "single-stratum, full-catalog rate untested" caveats; composite MC queued (low) |
| META-m3 (S loses z-interpretation under OOD) | presentation | STALE | Eq.(2) blanket non-comparability sentence + Fig.3 display-score disclosures (R26conf META-m1 closure) |
| META-N1 (Table III RA column) | presentation | VERIFIED (minor) | Editorial queue (table regen with RA column) |

## Cross-vendor legs

| Group | Verdict | Disposition |
|---|---|---|
| OpenAI P3-E1 (F0 = 1/8.982 dimensional error) | **FALSIFIED** | PDF-rendering misread of $F_0 = 1/8.98^2$ (tex L600, L669); identical falsification logged R26conf (tex header L66). OpenAI itself concedes quoted numbers consistent with correct F0 |
| Perplexity P3-E8 (9.4% should be 9.3%) | **FALSIFIED** | (8.98−8.14)/8.98 = 0.09354 → 9.4% at 1 dp (round-half-up); definition anchored in text |
| Version-history/"earlier draft" removal (Grok E1, OpenAI E2/E3, Perplexity m3) | HOUSTON-DECISION | R26conf precedent (standing disclosure policy) |
| eROSITA axis irreproducible (OpenAI E5, Perplexity E4/M2) | STALE | R26conf adjudication: 16-rescaling sweep + membership-is-canonical framing + downstream warning all printed; axis recovery documented impossible |
| Scaler leakage (OpenAI E4, Perplexity M1/M8) | STALE/PARTIAL | Disclosed in §II.B with ranking-invariance argument; quantitative impact joins methods queue (META-M2) |
| σ(fNL) multi-baseline (Perplexity E2/M9, OpenAI M9) | STALE | Normalization notes printed (§V + Fig.11 caption, R24–R26 closures); Appendix-C linear-scaling relabel = minor editorial queue |
| Grok E2 (9.4% in abstract disclaimed in body) | FALSIFIED/STALE | Abstract itself carries the disclaimer in the same sentence ("not a detection … no improvement") |
| Largest-scale/141× claims (OpenAI M1, Perplexity E5/m1) | STALE | Benchmark anchored to Liang2023 + ~100× catalog-grade companion figure (R26conf m3 closure) |
| Spatial χ² null (OpenAI M5, Perplexity M3/E10) | STALE | Footprint-dominance + no-selection-function caveats printed (R24conf #35 rewrite) |
| Planck top-1% vs top-200/200K labeling (OpenAI M7/M10) | STALE/PARTIAL | Table I note discloses predetermined-count semantics; Ntotal column annotation = editorial queue |
| Length/abstract-length/footnote-symbols (Grok M1/M2, OpenAI E6, Perplexity n1/n2) | HOUSTON-DECISION/OPINION | Format/venue calls |
| Remaining arithmetic spot-checks (OpenAI m1–m3, m7–m10) | ALL-CLEAR | Reviewer's own recomputations confirm paper values |

**Substantive verified-and-closed this round: 3 textual script/artifact-backed (INSESSION M2, M3-disclosure, M4) + 1 abstract enumeration (m2). Queued recompute: Gaia 20f/21f bound, Planck 99.9th-pctile injection gate (META-E1, genuine new finding), missingness/arm-fraction sensitivity. Zero verified arithmetic errors; both vendor recompute attacks on the Fisher numbers FALSIFIED.**
Recompile (v3.1.87): pdflatex×2 + bibtex + pdflatex — 26 pp, 0 errors, 0 undefined refs, 0 overfull hboxes, md5 `16f40c0d9cd219f3f559dd7a59a9f510`. Page 1 visually verified (abstract edits render clean).

**P3 ROUND VERDICT: CLEAN** — zero verified arithmetic/claim-truth errors (both vendor recompute attacks FALSIFIED); 4 verified presentation findings closed same-day in v3.1.87; queued items (Gaia 20f/21f bound, Planck 99.9th-pctile injection gate META-E1) are validation-hardening recomputes on accurately-scoped, disclosed printed claims — flag both at sign-off. Final PDF md5 `16f40c0d9cd219f3f559dd7a59a9f510` (26 pp, 0 errors).
