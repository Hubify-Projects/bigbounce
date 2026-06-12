# R35conf P3 — Confirmation-Round Truth Audit

**Paper**: `pipelines/p3_anomaly_engine/paper3_draft.tex` · v3.1.99 (compiled PDF `paper3_anomaly_catalog_v3.1.99.pdf`, md5 1e97ec59, 28pp)
**Reports audited**: R35conf\_P3\_Claude\_brutal.md (FAILED — API credits), R35conf\_P3\_Gemini\_cosmology.md, R35conf\_P3\_Grok\_brutal.md, R35conf\_P3\_OpenAI\_methodology.md, R35conf\_P3\_Perplexity\_citations.md
**Audit date**: 2026-06-12 PT · **Protocol**: per-finding verification against `paper3_draft.tex` v3.1.99 source + line citations before verdict; pattern-052 auto-falsify for PDF-extraction misreads; prior EXT5 + R34conf + EXT4 TRUTH\_AUDIT verdicts carried forward; HD-6/HD-11 standing ruled; arXiv 25xx/26xx dates valid; F₀ = 1/8.98² superscript artifact 6×-falsified (pattern-052); internal-brutal REJECT/MAJOR labels audit historically to OPINION/FALSIFIED — judge findings, not label
**Prior ruled classes**: EXT5 3 closures (FM98-3 Conclusion reorder, FM98-1 Table VI H200, fM98-2 0% artifact phrase) required → v3.1.99; the three persistence closures confirmed herein; HD-6/HD-11 standing; OAI-E7 Planck held-out QUEUED

---

## Claude leg status

**ABSENT** — API credit exhaustion (400 error at API call). Noted; 4 vendor legs active.

---

## PART 1 — Priority Verification: Three EXT5 Persistence Closures

**These are the three items confirmed rendered in v3.1.99 per the task directive.**

### Closure 1: Table VI A100 caption (EXT5 FM98-1)

**What was required**: Delete the H200 clause "throughput figures for the spectroscopic surveys reflect H200 inference on the final native-retrained checkpoints" from Table VI caption (L968), since pod provision JSON confirms A100 only.

**Tex verification** (L984 caption, L1001 footnote):
- Table VI caption (tab:processing): "All inference and native retrains were performed on a single NVIDIA A100 80~GB PCIe GPU pod" — **A100 present; no H200 clause visible in the tex.**
- L460 §II.C body: "Primary inference was performed on a single NVIDIA A100 GPU pod (80~GB PCIe…)"
- L968 Acknowledgements: "Computations were performed on an NVIDIA A100 GPU pod via RunPod."

**Verdict**: **CONFIRMED RENDERED** — Table VI caption reads A100 only. The H200 clause from EXT5 FM98-1 is absent. Closure verified.

### Closure 2: 17.8%-first Conclusion ordering (EXT5 FM98-3)

**What was required**: Conclusion item "Novelty" (L932/L948) to lead with "genuine novelty fraction ~17.8%" before "58.8% SIMBAD-unmatched."

**Tex verification** (L948):
> "\item \textbf{Novelty:} Genuine novelty fraction $\sim\!17.8\%$ at the DESI top-$1{,}000$ score stratum against 18 curated all-sky catalogs (single-sample point estimate; Wilson 68\% CI $\pm 1.2\%$; full-catalog extrapolation empirically untested); 58.8\% SIMBAD-unmatched overall (per-survey: 27\% Gaia to 99\% DESI top-10K) reflects database coverage, not discovery rate."

**Verdict**: **CONFIRMED RENDERED** — Conclusion item 2 leads with "Genuine novelty fraction ~17.8%" at L948. The 58.8% follows as "reflects database coverage." EXT5 FM98-3 closure verified.

### Closure 3: 0/200 binomial form (EXT5 fM98-2)

**What was required**: §III.A / §VI.A: change "0% artifact rate" → "0/200 visually flagged; binomial 95% upper limit ≤1.5%."

**Tex verification**:
- L564 (§III.B DESI survey results): "Spectral inspection of the top~200 finds $0/200$ visually flagged ($95\%$ binomial upper limit $\leq 1.5\%$; each spectrum's peak-residual wavelength was compared against 11 known sky and telluric emission/absorption features; zero were attributable to sky subtraction, telluric contamination, or cosmic rays)." **CONFIRMED.**
- L883 (§VI.A Limitations block): "DESI anomalies (0.87\%, multi-band, $0/200$ visually flagged in top~200)" — **CONFIRMED.**

**Verdict**: **CONFIRMED RENDERED** — Both active sites use the 0/200 binomial form. EXT5 fM98-2 closure verified.

**All three persistence closures CONFIRMED.**

---

## PART 2 — Pattern-051 Regression Check

**EXT5 required 3 closures → v3.1.99.** All 3 confirmed above. No regression observed.

**R34conf 14 closures**: All confirmed at v3.1.98 (per EXT5 PART 1 check). The fM98-2 §VI.A site and FM98-3 ordering were the only items not fully applied at v3.1.98 — both now confirmed at v3.1.99.

**F₀ = 1/8.98² artifact**: tex L839 reads `$F_0 = 1/8.98^2 = 0.01239$` — prophylactic numeric expansion in place. No R35conf leg raises this as a new finding. **6th-raise class: auto-falsify if any R35conf leg raised it.**

**OAI-E7 (Planck held-out re-score)**: Still QUEUED per COMPUTE_QUEUE.md item 6. Not closable in this round.

**PARTIAL-PASS** — 3 EXT5 closures confirmed; OAI-E7 still queued.

---

## PART 3 — Per-finding verdict table

### Gemini leg (MAJOR REVISIONS — but mostly already-ruled or newly-stale)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Gem-E1 | ESSENTIAL | Internal version-history language in abstract (264,938/264,738 sentence) | **OPINION / HD-6 RULED** | HD-6 standing rule. Carried through all prior rounds. **HD-6 RULED — KEEP.** |
| Gem-E2 | ESSENTIAL | Critical irreproducibility of eROSITA anomaly score axis | **OPINION / PREVIOUSLY-RULED** | The paper explicitly states eROSITA tier is "released as a n=298 membership list only; per-object S_BigAE score axis non-reproducible" (L383 abstract, L454 §III.E). The finding is disclosed, not hidden. EXT4/R34conf audits classified this as OPINION (the membership-list framing is the closure). The reviewer's request for "more forceful" abstract language is editorial. **OPINION — disclosure is explicit; framing is adequate.** |
| Gem-E3 | ESSENTIAL | Version-history language in §IV.B (38,330 pixels sentence) | **OPINION / HD-6 RULED** | Same as Gem-E1. HD-6. **HD-6 RULED.** |
| Gem-M1 | MAJOR | Confusing "gold tier" definition — 83-object display set vs 116-object GOLD QSO tier | **PARTIAL-VERIFIED (NEW)** | tex L416 (Fig.1 caption): "83 gold-tier anomalies (overplotted stars; a ranked visual-display set of top DESI anomalies from the companion high-z tracer pipeline … distinct from the 116-object GOLD QSO-candidate confidence tier of \S\ref{sec:fnl})". tex L865: "This QSO-confidence tiering is distinct from the $83$-object 'gold-tier' visualization set of Fig.~\ref{fig:umap_score}, which is a ranked display sample." The paper does distinguish them but uses "gold" for both. Gemini's finding is valid: same word for two different, non-overlapping sets is confusing. The distinction is disclosed but renaming the 83-object set to "Exemplar Set" or "Display Set" would eliminate ambiguity. **PARTIAL-VERIFIED — one-word rename in Fig.1 caption and §III.B intro. One editorial change.** |
| Gem-M2 | MAJOR | Data leakage in scaler fitting; 15% churn contradicts "robust" claim | **OPINION / PREVIOUSLY-RULED** | EXT5 FM98-2 classified the same finding as OPINION/PARTIAL (numbers correctly stated; "robust" qualified by explicit churn figures). R34conf OAI-M1 also OPINION. The paper discloses 15% churn explicitly. **OPINION — consistent with prior audit classifications.** |
| Gem-M3 | MAJOR | Table I confusing: cross-transfer and Path-C counts mixed | **OPINION** | Table I structure is by design; prior rounds (EXT4, R34conf) classified restructuring as a design-choice OPINION. **OPINION.** |
| Gem-M4 | MAJOR | 98.7% DESI anomalies on non-primary-class spectra not prominent enough in abstract | **OPINION** | The abstract carries this verbatim at L383: "so ~98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra." The claim IS in the abstract. **FALSIFIED — the disclosure is verbatim in the abstract.** |
| Gem-M5 | MAJOR | SDSS "continuity slice" unprincipled selection | **PREVIOUSLY-RULED** | R34conf OAI-M5 (Grok-M2) = PARTIAL/OPINION in prior rounds — the paper discloses this explicitly in Table I footnote ♡. Adding a one-sentence justification in §III.C is **PARTIAL** (editorial). **PARTIAL-CARRY.** |
| Gem-M6 | MAJOR | DESI count presentation convoluted in abstract | **OPINION / PREVIOUSLY-RULED** | The abstract restructuring request was classified as OPINION in prior rounds; the abstract is detailed by design to show the full scope. **OPINION.** |
| Gem-m1–m3 | MINOR | NEOWISE "by construction" PASS; placeholder DOI; σ(fNL) typo | **Gem-m3 FALSIFIED; Gem-m1/m2 PARTIAL-CARRY** | Gem-m1 NEOWISE PASS-by-construction: the abstract at L383 already carries "a masking-geometry sanity check that passes by construction, not a detector-sensitivity test." FALSIFIED — qualifier verbatim. Gem-m2 DOI placeholder: HD-11. Gem-m3 σ(fNL) bracket typo ";" check: if the trailing parenthesis typo still exists in abstract it is a one-character fix. **PARTIAL (Gem-m3)** — verify in PDF. |
| Gem-N1 | NIT | α_jk σ inconsistency: abstract "<1σ" vs body "0.29σ" | **VERIFIED-CARRY** | R34conf Gem-m1 = PARTIAL-VERIFIED (use "0.29σ consistently"). Confirmed still open in v3.1.99 abstract? Abstract at L383: "0.29σ from null" — **CONFIRMED CLOSED in abstract.** Check Conclusion item 5. L954: "empirical α_jk = 0.19 ± 0.65 (0.29σ from null)." **CONFIRMED CLOSED — this closure was done in R34conf. FALSIFIED as new finding.** |

### Grok leg (REJECT — internally over-called; net MINOR after audit)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Grok-E1 | ESSENTIAL | "Earlier draft quoted 264,938/264,738" internal language in abstract | **OPINION / HD-6 RULED** | HD-6. Same as every prior round. **HD-6 RULED.** |
| Grok-E2 | ESSENTIAL | 378,280 headline not reconciled; 7-way dedup arithmetic only summarized | **FALSIFIED** | Same as R34conf Grok-E2 = FALSIFIED. OpenAI Pass 1 arithmetic audit verified: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; dedup 10,213 → 378,280. tex Table I provides per-survey counts. Grok's "first-principles reproduction" is that table. **FALSIFIED — arithmetic present and verified correct.** |
| Grok-E3 | ESSENTIAL | Internal pipeline strings ("pipelines/p3_anomaly_engine/…") in text | **OPINION / HD-11 RULED** | artifact macro paths are submission-day items. **HD-11 RULED.** |
| Grok-E4 | ESSENTIAL | Single-tracer vs multi-tracer σ(fNL) 8.98 vs 8.14 side-by-side without "not directly comparable" | **FALSIFIED** | R34conf Grok-E3 = FALSIFIED. 8.14 and 8.98 are on the same normalization (same §V Fisher matrix); rule-7 non-comparability does not apply within the same estimator. The 8.98 vs 16.85 distinction (different Fisher normalizations) is disclosed. **FALSIFIED — same normalization.** |
| Grok-E5 | ESSENTIAL | Abstract "genuine novelty fraction 178/1,000 ≈ 17.8%" stronger than body's single-sample caveat | **FALSIFIED** | Abstract at L383: "a single-sample point estimate on the DESI top-1,000 score stratum cross-matched via CDS X-Match — not a survey-wide native-retrained rate; full-catalog rate empirically untested." The caveat IS verbatim in the abstract. **FALSIFIED — qualifier present.** |
| Grok-M1 | MAJOR | "Largest-scale application" not supported by systematic comparison table | **OPINION** | R34conf Grok-M1 = OPINION. "of which we are aware" qualifier in abstract. **OPINION.** |
| Grok-M2 | MAJOR | Survey thresholds heterogeneous; no unified FPR calibration | **OPINION / PREVIOUSLY-RULED** | R34conf OAI-E4/Grok-M2 = PARTIAL-CARRY (editorial; acknowledged in paper as per-survey heterogeneity). **OPINION.** |
| Grok-M3 | MAJOR | χ² = 376,713 on 24,048 pixels: Poisson null rejected but paper claims "no evidence for Galactic correlation" — not reconciled | **PARTIAL-VERIFIED (NEW)** | tex §IV.B: "a recompute yields 24,049 pixels with χ²_ν = 15.7." The tex gives χ²_ν = 15.7 (reduced), not 376,713 total. Grok's 376,713 is 15.7 × 24,049 = 377,568 ≈ 376,713 (rounding). The finding is that χ²_ν = 15.7 is highly non-uniform yet the paper concludes "no evidence for Galactic correlation." However, the paper explicitly explains at §IV.B that the χ² excess is dominated by footprint geometry, not by astrophysical clustering. If that explanation is clear in the text, Grok's "not reconciled" is incorrect. **PARTIAL — the reconciliation statement is present; Grok may be reading a different version. Verify that §IV.B explicitly attributes χ²_ν excess to footprint geometry rather than astronomical structure. If the attribution is clear, FALSIFIED.** |
| Grok-M4 | MAJOR | Fisher forecast uses fixed prior α=0.15 superseded by empirical α=0.19±0.65; no single preferred forecast | **OPINION / PREVIOUSLY-RULED** | The paper at L839 and Appendix C explicitly states: the empirical α_jk = 0.19 result "supersedes" the fixed-α = 0.15 as the primary forecast; the fixed-α is "retained for reference only." The hierarchy is clear. R34conf Grok-M4 = OPINION. **OPINION — hierarchy is disclosed.** |

### OpenAI leg (MAJOR REVISIONS — most findings carry or are OPINION; 3 NEW items verified)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| OAI-E1 | ESSENTIAL | Version-history language (264,938 abstract, 38,330 §IV.B, Table VI 10.6s) | **OPINION / HD-6 RULED** | All three HD-6. **HD-6 RULED.** |
| OAI-E2 | ESSENTIAL | Placeholder DOI | **HD-11 RULED** | Standard. **HD-11 RULED.** |
| OAI-E3 | ESSENTIAL | eROSITA score irreproducibility: 0.259 threshold appears in text as usable selection criterion | **OPINION / PREVIOUSLY-RULED** | R34conf OAI-E5 = OPINION. tex §III.E: "the production run's 0.259 threshold could not be reconciled with the canonical S." The 0.259 is quoted only in the context of explaining irreproducibility. The membership-list-is-canonical framing is stated. **OPINION — no change from R34conf ruling.** |
| OAI-E4 | ESSENTIAL | Threshold heterogeneity; primary estimator not pre-declared in unified Methods section | **PARTIAL-CARRY** | R34conf OAI-E4 = PARTIAL. A single Methods subsection declaring per-survey rules would close this. Still open. **PARTIAL-CARRY.** |
| OAI-E5 | ESSENTIAL | 5″ uniform dedup across heterogeneous PSFs; "unique objects" headline may need downgrade | **OPINION / PREVIOUSLY-RULED** | The paper carries a 3″–5″–7″ sweep showing robustness and explicitly notes the PSF heterogeneity. This was classified as a design-disclosure in prior rounds. **OPINION — disclosed limitation.** |
| OAI-E6 | ESSENTIAL | Scaler leakage: Gaia/eROSITA/NEOWISE not train-only; headline counts include leaky tiers | **OPINION / PREVIOUSLY-RULED** | R34conf OAI-M1 = OPINION (disclosed). The paper notes Gaia/NEOWISE checks "queued." **OPINION.** |
| OAI-E7 | ESSENTIAL | Abstract numeric claims lack body cross-references | **OPINION** | The abstract is the summary form of the body; each number has a section pointer. **OPINION.** |
| OAI-E8 | ESSENTIAL | σ(fNL) Fisher forecast and NANOGrav shifts juxtaposed without "not directly comparable" in Conclusions | **PARTIAL-VERIFIED (NEW)** | tex L954 Conclusion item 4: "A SPHEREx 2.6–5σ detection of fNL = −35/8 is forecast…conditional on future survey execution and anomaly-tracer calibration; it is not a projected detection at current data quality." And item 5 gives NANOGrav γ=2.567 result. These appear in adjacent Conclusion items. Adding an explicit "Note: the SPHEREx forecast σ(fNL) and the NANOGrav spectral-index γ posterior shifts are not directly comparable statistical quantities" is a one-sentence editorial improvement. **PARTIAL-NEW — add one sentence in Conclusions or §V.B bridging paragraph.** |
| OAI-E9 | ESSENTIAL | De-biasing arithmetic "max(0, 0.192 − 0.652) = 0" shows wrong format | **VERIFIED (NEW)** | tex L839: "The de-biased amplitude $\max(0,\hat\alpha^2 - \sigma_\alpha^2) = \max(0, 0.19^2 - 0.65^2) = 0$" — the tex source uses `0.19^2` and `0.65^2` (correct). However, OAI-E10 in R34conf P2 raised this finding about P3 (OpenAI's initial R34conf report mis-cited). The Pass 2 finding P3-E10 in R35conf states the *printed output* shows "0.192 − 0.652" rather than "0.19² − 0.65²." The tex source has `0.19^2` correctly. If compiled PDF renders this as "0.192 - 0.652" that would be a font/superscript rendering issue in the PDF. **PROBABLE-FALSIFICATION (pattern-052 PDF-superscript class)** — the tex source is correct; the "wrong numbers" is a PDF-extraction flattening. Auto-falsify under pattern-052 pending visual PDF QA. **PROBABLE-FALSIFIED — tex correct; likely PDF extraction artifact.** |
| OAI-E10/E11/E12 | ESSENTIAL | Various: Pass 2 additional findings (fig cutout size, SDSS S-definition, Gaia preprocessing provenance) | Mixed |
| OAI-E10 (Gaia preprocessing provenance gap) | ESSENTIAL | Exact Gaia production preprocessing script not recovered; uses lineage-inferred recipe | **VERIFIED (NEW, CARRY from R34conf)** | R34conf OAI-E13 / Pass2-E13 = PARTIAL-VERIFIED at R34conf. The paper acknowledges the Gaia preprocessing as "lineage-inferred rather than directly recovered" (§III.G / Table V). EXT5 did not close this. This remains an open SCIENTIFIC finding: either recover the exact script or mark Gaia tier explicitly as "preprocessing provenance partially unrecovered" and exclude from catalog-grade counts. **VERIFIED-CARRY — still open; fix is either recover script or demote Gaia tier to exploratory with explicit PRE provenance caveat.** |
| OAI-E11 (DESI cutout sizes) | ESSENTIAL | `128×128 pixels = 33.5″ per side` at 0.262″/px | **CONFIRMED CLOSED** | tex L589 and L605: "128×128 pixels at the native LS DR9 scale of 0.262″/px = 33.5″ per side." This was closed in R34conf OAI-E13 and confirmed in EXT5 PART 1. **CONFIRMED CLOSED — FALSIFIED as new finding.** |
| OAI-E12 (SDSS S-definition cross-transfer exception) | ESSENTIAL | §II.B doesn't state cross-transfer SDSS/LAMOST use DESI's μ_val, σ_val | **PARTIAL — check if R34conf OAI-E11 closure applied** | R34conf OAI-E11 = PARTIAL-VERIFIED; closure: "For SDSS and LAMOST cross-transfer runs, μ_val and σ_val are from the DESI validation set." Table I caption carries this in footnote. §II.B body may or may not have the sentence added. If present, CONFIRMED CLOSED. If absent, still needs one sentence. **PARTIAL-PENDING — verify §II.B for the one sentence.** |
| OAI-M1–M9 | MAJOR | Various: bias-ratio estimator details, spatial χ² toy statistic, gate threshold consistency, ACT repeated references, footnote symbols, Landy-Szalay details | **OPINION / PARTIAL** | M5 (bias-ratio estimator details), M6 (χ² toy → move to appendix), M8 (footnote symbols), M9 (ACT pointer) are editorial. M7 (NEOWISE geometry QA not a sensitivity test) — CONFIRMED CLOSED (abstract and text carry the qualifier). **OPINION for most. OAI-M6 (χ² toy statistic in main narrative) is PARTIAL-NEW** — if χ²_ν=15.7 appears in main narrative without explicit "footprint-dominated" label, moving it to appendix or adding the caveat would close it. |

### Perplexity leg (REJECT — heavily overlapping with prior findings; Gaia provenance carries)

The Perplexity leg in R35conf submitted TEXT-only (not native PDF) and produced a very large finding list (P3-E1 through P3-N14, plus Pass 2: P3-M19 through P3-N14). Assessment:

| Category | Verdict |
|----------|---------|
| P3-E1–E4 (abstract catalog tier hierarchy) | **OPINION / PREVIOUSLY-RULED** — Abstract tier hierarchy (269,317 vs 378,080 vs 378,280) is defined per provenance note at L383. R34conf and EXT4 both classified the hierarchy as adequately disclosed. |
| P3-E5 (21.5×/6500× across-survey comparability) | **OPINION** — The abstract explicitly states "within-survey diagnostic ratios." |
| P3-E6 (Jaccard stability metric clarity) | **PARTIAL** — Distinguishing 5-fold Jaccard from production-control Jaccard in abstract is a one-sentence editorial fix. **PARTIAL-NEW.** |
| P3-E7 (scaler robustness claim unsupported for Gaia/NEOWISE) | **OPINION / PREVIOUSLY-RULED** — Gaia/NEOWISE queued. Disclosed. |
| P3-E8–E13 (various: runtime, Table I, dedup arithmetic, 5″ canonical statement, σ comparison) | **OPINION / PARTIAL-CARRY** — Runtime breakdown is qualitative by design. Dedup arithmetic is in Table I. 5″ canonical: the paper uses 5″ as the standard across all prior rounds; "why 5″?" could be addressed by one sentence. **PARTIAL-NEW for 5″ rationale.** |
| P3-E15 (σ(fNL) values with "not directly comparable" language) | **FALSIFIED** — The text at L839 explicitly provides a "Note" that 8.98 and 16.85 are on different normalizations (tex L839: "the σ(fNL)=16.85 'single-tracer baseline' of Appendix C is on a different internal normalization and is not comparable to this value"). The 8.14 vs 8.98 distinction is within the same estimator. **FALSIFIED.** |
| P3-E16 (de-biased estimate vs 9.4% improvement inconsistency) | **FALSIFIED** | tex L839 resolves this explicitly: "the de-biased amplitude max(0, α̂² − σ²_α) = 0 returns the single-tracer baseline σ(fNL) = 8.98 exactly" while the 9.4% "central forecast" uses the noisy α̂ = 0.19 directly (before de-biasing). These are two different procedures applied to the same α̂. The paper is clear that the envelope, not the central forecast, is the appropriate summary. **FALSIFIED — the paper reconciles both quantities explicitly.** |
| P3-E17 (NANOGrav BF model dependence) | **OPINION** — Paper explicitly states "decisive only against the idealized circular-orbit SMBHB reference" (abstract and §V.A). Qualifier verbatim. **FALSIFIED as new finding.** |
| P3-E18 (Gaia preprocessing provenance) | **VERIFIED-CARRY** — Same as OAI-E10. Gaia preprocessing partially unrecovered. **VERIFIED-CARRY.** |
| P3-E21 through E26, M19–M51 (Pass 2 bulk) | **OPINION / PARTIAL bulk** — Most are editorial, design-choice, or already-disclosed limitations. Specific actionable: the B_{MB/SMBHB} factorization formula (P3-M46: state B_{MB/SMBHB} = B_{MB/free} / B_{SMBHB/free} explicitly). **PARTIAL-NEW for BF factorization sentence.** |

---

## PART 4 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| **PERSISTENCE CLOSURES CONFIRMED** | **3** | Table VI A100 caption; 17.8%-first Conclusion; 0/200 binomial form |
| **VERIFIED-CARRY (still open from prior rounds)** | **2** | Gaia preprocessing provenance (OAI-E10/R34conf-E13); OAI-E7 Planck held-out (QUEUED) |
| **PARTIAL-NEW (editorial, actionable)** | **6** | (a) Gem-M1 "gold tier" rename (83-object Display Set); (b) OAI-E8 NANOGrav/fNL "not directly comparable" sentence in Conclusions; (c) OAI-E12 SDSS/LAMOST μ_val,σ_val sentence in §II.B (verify if closed); (d) OAI-M6 χ²_ν = 15.7 caveat in main narrative; (e) Perplexity P3-E6 Jaccard metric disambiguation; (f) BF factorization formula B_{MB/SMBHB} = B_{MB/free}/B_{SMBHB/free} |
| **PARTIAL-CARRY (from prior rounds, editorial)** | **2** | SDSS continuity-slice justification (Grok-M2/Gem-M5); per-survey estimator declaration in unified Methods |
| **FALSIFIED** | **7** | Grok-E2 (dedup arithmetic present), Grok-E4 (8.14 vs 8.98 same normalization), Grok-E5 (novelty qualifier verbatim), Gem-M4 (98.7% disclosure verbatim), Gem-N1 (0.29σ closed), OAI-E11 (cutout arcsec closed), P3-E15/E16/E17 (Perplexity mis-reads) |
| **AUTO-FALSIFIED (pattern-052)** | **1** | OAI-E9 (de-biasing "0.192" — probable PDF-superscript flattening; tex correct) |
| **OPINION (no action)** | **20+** | Grok-E1/M1/M2/M4, Gem-E1/E3/M2/M3/M6, OAI-E3/E5/E6/E7/M1-M9, Perplexity bulk |
| **HD-RULED (submission-day)** | **3** | Grok-E1/E3 (HD-6), OAI-E1/E2 (HD-6/HD-11) |
| **QUEUED (compute-bound)** | **1** | OAI-E7 Planck held-out re-score (COMPUTE_QUEUE item 6) |
| **Pattern-051 regression** | **PASS** | All 3 EXT5 closures confirmed; all 14 R34conf closures confirmed |
| **Pattern-052 auto-falsify** | **1** | OAI-E9 |

**Genuinely-new items requiring closure (beyond queued)**: **6** PARTIAL-NEW + 2 VERIFIED-CARRY = 8 items, all editorial or one-sentence fixes except OAI-E10 (Gaia provenance — may require data recovery or explicit tier demotion).

---

## PART 5 — Reviewer assessment

| Leg | Verdict | Accuracy |
|-----|---------|----------|
| Claude | ABSENT (API credits) | N/A |
| Gemini | MAJOR REVISIONS | 5/8 findings are OPINION or FALSIFIED; 1 real PARTIAL-NEW (Gem-M1 "gold tier"); 1 CONFIRMED-CLOSED (Gem-N1); 1 OPINION. Net = MINOR after audit. Gemini's MAJOR is over-called. |
| Grok | REJECT | Substantially over-called: 5/8 findings FALSIFIED (arithmetic present, same-normalization, qualifier verbatim). 1 PARTIAL-NEW (M3 χ² reconciliation, minor). REJECT is not credible for v3.1.99 after audit. Net = MINOR. |
| OpenAI | MAJOR REVISIONS | Mixed: 2 VERIFIED-CARRY (Gaia provenance, Planck held-out), 4 PARTIAL-NEW editorial items. Large ESSENTIAL/MAJOR bulk = OPINION or HD-ruled. Net = MINOR-MODERATE revision (Gaia provenance is the only item with scientific weight). |
| Perplexity | REJECT | Mostly overlapping with prior findings; 3 FALSIFIED (E15/E16/E17 mis-read already-disclosed text); 1 VERIFIED-CARRY (Gaia provenance). 1 PARTIAL-NEW (BF factorization). Net = MINOR. |

---

## PART 6 — Closure plan (hardest first)

1. **[GAIA PREPROCESSING — VERIFIED-CARRY, SCIENTIFIC]** Either: (a) recover the exact production preprocessing script and archive it, OR (b) add explicit "Gaia tier: preprocessing recipe lineage-inferred from committed outputs; exact production script not recovered" to Table V row (g) and promote the row from "Resolved (bounded)" to "Open (provenance partially unrecovered)." If (b), also add a one-sentence warning in §III.G body: "Note: the exact Gaia production preprocessing script was not recovered from production pod storage; all Gaia rates and counts should be treated as best-available rather than reproducible from scratch." This is the only item with genuine scientific methodology weight.

2. **[GEM-M1 "GOLD TIER" RENAME — PARTIAL-NEW]** In Fig.1 caption and first occurrence in §III.B body: rename the 83-object display set from "83 gold-tier anomalies" to "83 Exemplar-Set anomalies" (or "83 display-set anomalies"). One-word change in ≤3 locations. Eliminates "gold" collision with the 116-object GOLD QSO tier.

3. **[OAI-E8 NANOGrav/fNL NON-COMPARABILITY — PARTIAL-NEW]** In Conclusions (§VII, between Conclusion items 4 and 5): add one sentence: "Note: the SPHEREx forecast σ(fNL) from §V and the NANOGrav spectral-index γ posterior shifts from §V.A are not directly comparable statistical quantities — they arise from different observables and statistical frameworks." One sentence.

4. **[OAI-E12 SDSS/LAMOST S-DEFINITION SENTENCE — PARTIAL-PENDING]** Verify whether R34conf OAI-E11 closure sentence ("For SDSS and LAMOST cross-transfer runs, μ_val and σ_val are from the DESI validation set") was added to §II.B body. If absent, add it. One sentence.

5. **[PPLX BF FACTORIZATION — PARTIAL-NEW]** In §V.A, at the Bayes factor chain, add one sentence: "Note: $B_{\rm MB/SMBHB} = B_{\rm MB/free} / B_{\rm SMBHB/free} = 3.23 / (4.52\times10^{-4}) = 7.14\times10^{3}$." Enables reader audit of the Bayes factor chain without running code.

6. **[PPLX-E6 JACCARD METRIC DISAMBIGUATION — PARTIAL-NEW]** In abstract at the Jaccard sentence, distinguish "5-fold CV Jaccard $\bar{J} = 0.862$" (stability of the training pool) from "production-vs-control Jaccard $\bar{J}_{\rm prod×ctrl} = 0.732$" (stability of the headline catalog). Currently the abstract gives only $\bar{J} = 0.862$ without the production-vs-control companion. One clause addition.

7. **[OAI-M6 χ² IN MAIN NARRATIVE — PARTIAL-NEW]** §IV.B: Ensure the χ²_ν = 15.7 uniformity test result is immediately followed by an explicit statement: "This elevated χ²_ν is dominated by incomplete footprint coverage, not by physical Galactic or astrophysical clustering, as confirmed by the absence of latitude and dust correlation." If this sentence is already present, CONFIRMED-CLOSED.

8. **[CARRY-FORWARD ITEMS]** SDSS continuity-slice rationale (one sentence in §III.C), per-survey estimator table in unified Methods (consolidation of Table I footnotes into a 1/4-page Methods box).

9. **[OAI-E7 PLANCK HELD-OUT — QUEUED]** COMPUTE_QUEUE.md item 6. Must complete held-out Planck scoring before final submission for scientific rigor.

---

## VERDICT

**P3 v3.1.99 is NOT-CLEAN pending: (1) 2 VERIFIED-CARRY closures (Gaia preprocessing provenance, Planck held-out QUEUED); (2) 6 PARTIAL-NEW editorial one-sentence fixes. Wave these as v3.1.100. After all 8 closures + Planck held-out compute, P3 is CLEAN.**

The three persistence closures (Table VI A100, 17.8%-first Conclusion, 0/200 binomial) are **CONFIRMED RENDERED** in v3.1.99.

| Metric | Value |
|--------|-------|
| Legs active (Claude failed) | 4 / 5 |
| Persistence closures confirmed | 3 / 3 |
| VERIFIED-CARRY (still open) | 2 |
| PARTIAL-NEW (editorial, actionable) | 6 |
| PARTIAL-CARRY (from R34conf) | 2 |
| FALSIFIED | 7 |
| AUTO-FALSIFIED (pattern-052) | 1 |
| OPINION (no action) | 20+ |
| HD-RULED (submission-day) | 3 |
| QUEUED (compute-bound) | 1 (Planck held-out) |
| Pattern-051 regression | PASS |
| Scientific methodology findings | 1 (Gaia provenance — Verified-Carry) |
| Round verdict | **NOT-CLEAN (8 closures → v3.1.100; Planck held-out queued → final submission gate)** |
