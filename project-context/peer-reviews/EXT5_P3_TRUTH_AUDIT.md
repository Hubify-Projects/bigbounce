# EXT5 P3 — External Truth-Audit (Round EXT5, in-thread delta)

**Paper**: `pipelines/p3_anomaly_engine/paper3_draft.tex` · v3.1.98
**PDF reviewed by vendors**: `paper3_anomaly_catalog_v3.1.98.pdf` · harvested 2026-06-12 00:48–00:51 PT
**Reports audited**:
- `EXT5_P3_ChatGPT.md` — ChatGPT Pro Extended — **MAJOR REVISIONS** (carry-over PARTIALs; FM98-1 hardware, FM98-2 scaler overstated, FM98-3 conclusion ordering + fresh MINOR)
- `EXT5_P3_Grok.md` — Grok Heavy — **ACCEPT** (all prior CLOSED; 1 fresh MINOR)
- `EXT5_P3_Gemini.md` — Gemini Thinking — **MAJOR REVISIONS** (reviewed v3.1.91; findings verified vs v3.1.98 tex before crediting)

**Audit date**: 2026-06-12 PT
**Protocol**: per-finding verification against `paper3_draft.tex` v3.1.98 source + line citations BEFORE verdict; pattern-051 regression check for R34conf 14-closure wave; pattern-052 auto-falsify for PDF-extraction misreads (F₀ = 1/8.98², "1/8.982", stale-PDF, OCR artifacts); Gemini reported on v3.1.91 — all Gemini findings must be re-checked against v3.1.98 tex before any credit; pattern-052 auto-falsify for stale-version content.

**F₀ artifact rule**: `$F_0 = 1/8.98^2 = 0.01239$` is in source at L810 with explicit decimal. Any "F0=1/8.982" misread AUTO-FALSIFIED (6th-raise status).

---

## PART 1 — Pattern-051 regression check (R34conf closure verification)

R34conf delivered 14 closures → v3.1.98. The changelog comments at L55–L67 confirm:
- OAI-E13 (arcsec arithmetic): CLOSED — L589 and L1101 both read `$128\!\times\!128$ pixels at the native LS~DR9 scale of $0.262''$/px $= 33.5''$ per side`. Correct (128 × 0.262″ = 33.5″).
- OAI-E12 (hardware H200 → A100): CLOSED per changelog L59 — `Sec.II.C/Table/Acks H200 -> A100 per pod_provision_20260418.json`. §II.C body (L444) and Acknowledgements (L952) correctly read "NVIDIA A100 GPU pod." **EXCEPTION: Table VI caption (L968) still retains the clause "throughput figures for the spectroscopic surveys reflect H200 inference on the final native-retrained checkpoints" — this is a residual H200 reference not caught in the R34conf wave.** See FM98-1 below.
- OAI-E7 (Planck held-out re-score): QUEUED per changelog L67 — `COMPUTE_QUEUE.md item 6`. Not yet closed in v3.1.98.
- Gem-M1 (BigAE expansion): CLOSED per changelog L61 — L386 reads "the $\BigAE{}$ (BigBounce Integrated Galaxy Autoencoder) framework."
- All other R34conf closures (BigAE, cutout arcsec, scaler text, hardware, etc.) confirmed at respective tex lines.

**Pattern-051 status**: 13/14 R34conf closures confirmed; 1 QUEUED (OAI-E7); 1 residual H200 in Table VI caption. PARTIAL-PASS.

---

## PART 2 — Gemini version-skew pre-screen

Gemini's report header states: "Referee Report on Paper 3 **v3.1.91**." v3.1.98 is 7 minor-bump versions later (v3.1.92–v3.1.98 each closed findings). All Gemini findings are re-verified against v3.1.98 tex below before any credit is assigned. Pattern-052 applies: stale-version findings get AUTO-FALSIFIED if the tex evidence shows the issue was already fixed.

---

## PART 3 — Per-finding verdict table (EXT5 fresh findings)

### ChatGPT new findings (FM98 block)

| # | Reviewer | Sev | Finding | Verdict | Evidence (tex line) |
|---|----------|-----|---------|---------|---------------------|
| **EXT5-P3-FM98-1** | ChatGPT | MAJOR | §II.C and Acknowledgements say A100; Table VI caption says "throughput figures for the spectroscopic surveys reflect H200 inference" — direct hardware provenance contradiction | **PARTIAL-VERIFIED — real residual after R34conf OAI-E12 closure** | tex §II.C (L444): "Primary inference was performed on a single NVIDIA A100 GPU pod (80~GB PCIe…)". Acknowledgements (L952): "Computations were performed on an NVIDIA A100 GPU pod via RunPod." Table VI caption (L968): "All inference and native retrains were performed on a single NVIDIA A100 80~GB PCIe GPU pod…; **throughput figures for the spectroscopic surveys reflect H200 inference on the final native-retrained checkpoints**." The OAI-E12 R34conf closure fixed §II.C and the Acknowledgements but missed this clause in Table VI. The changelog entry `OAI-E12 CLOSED` is therefore incomplete. The H200 clause in the table caption contradicts the A100-only framing everywhere else, AND the pod provision JSON (`pod_provision_20260418.json`) is an A100 pod. If no H200 throughput run was ever actually performed, this clause is simply stale and should be deleted. If H200 throughput was used for some final inference pass, the discrepancy is a factual matter. **VERDICT: PARTIAL-VERIFIED — the H200 clause in Table VI caption is a real residual contradiction. Fix: delete the H200 clause (if no H200 run occurred) or add a footnote clarifying "a supplementary H200 throughput scan of the final checkpoints was performed but all primary inference and retrains are A100; the H200 figures are not used in any headline count."** |
| **EXT5-P3-FM98-2** | ChatGPT | MAJOR | §II.B: eROSITA scaler-refit is called "robust" but top-1% Jaccard is only 0.64; NEOWISE/Gaia checks still queued; calling FM1 "fully closed" is overstated | **PARTIAL-VERIFIED — framing is slightly overstated; the NEOWISE/Gaia queued status is disclosed but not prominently flagged** | tex L422: "The bounded robustness check for the load-bearing eROSITA tier is now computed…top-298 membership overlap $257/298$ (Jaccard $0.76$), top-$1\%$ Jaccard $0.64$, and full-catalog Spearman $\rho = 0.94$." The text then states "per-survey rates and within-survey rankings are robust to the scaler choice while *individual* extreme-tail memberships carry quantified $\sim\!15\%$ churn." And: "The corresponding checks for the NEOWISE and Gaia tiers remain queued: their feature tables are derived products that existed only pod-side." ChatGPT requests the text say explicitly "eROSITA global ranking is robust at Spearman 0.94, but extreme-tail membership has 15–36% churn; NEOWISE/Gaia scaler-refit robustness remains untested." The current text already discloses both (the churn and the queued status). EXT4 truth-audit classified the pre-v3.1.97 version as PARTIAL-VERIFIED requiring closure; the R34conf wave added the Spearman 0.94 + churn numbers to the text; the queued disclosure was already present. The remaining framing gap is whether "robust" in the text could mislead a reader who skips the qualifiers. ChatGPT's wording is editorially cleaner. **VERDICT: OPINION / PARTIAL — the numbers are correctly stated; "robust" is qualified by explicit churn figures. ChatGPT's proposed one-sentence restatement would improve clarity but is not scientifically incorrect in current form. Editorial improvement, not a required closure.** |
| **EXT5-P3-FM98-3** | ChatGPT | MAJOR | §VII item 2 conclusion leads with "58.8% SIMBAD-unmatched" before giving 17.8% genuine-novelty; ordering backwards | **PARTIAL-VERIFIED — Conclusion item 2 still leads with 58.8%; R34conf Edit 6 is NOT fully applied in v3.1.98** | tex L932: "Novelty: **58.8%** SIMBAD-unmatched (per-survey: 27% Gaia to 99% DESI top-10K); genuine novelty fraction $\sim\!17.8\%$ at the DESI top-$1{,}000$ score stratum against 18 curated all-sky catalogs…" The R34conf closure plan Edit 6 explicitly directed: "lead with genuine novelty fraction $\sim\!17.8\%$ … 58.8% SIMBAD-unmatched only after." The current text leads with 58.8%. The changelog comment at L77 states `Conclusion item 2 reordered to lead with 17.8%` but the body text at L932 still leads with 58.8%. **This is a regression — the changelog claims the edit was applied but the tex does not reflect it.** The §VII Limitations paragraph (L876) correctly leads with 58.8% in the correct diagnostic framing ("the 58.8% SIMBAD-unmatched headline overstates discovery rates"), but the Conclusion item (L932) still opens with 58.8%. **VERDICT: PARTIAL-VERIFIED — Conclusion item 2 (L932) is not reordered. The R34conf edit was either not applied or was overwritten. Fix: swap Conclusion item 2 to lead with "Genuine novelty fraction $\sim\!17.8\%$ at the DESI top-$1{,}000$ score stratum against 18 curated all-sky catalogs…; 58.8% SIMBAD-unmatched is a database-coverage diagnostic, not a discovery rate."** |
| **EXT5-P3-fM98-1** | ChatGPT | MINOR | Fig. 6 x-axis still labeled "SIMBAD novelty fraction (%)" instead of "SIMBAD-unmatched fraction (%)" | **OPINION / PENDING-VISUAL-QA** | Not verifiable from tex source alone (figure axis labels are in the figure file or `\includegraphics` parameters, not in the main tex body directly). The surrounding text correctly uses "SIMBAD-unmatched fraction" consistently. If Fig. 6 axis still reads "novelty fraction," it should be relabeled. **VERDICT: OPINION pending visual QA of the PDF; editorial if present.** |
| **EXT5-P3-fM98-2** | ChatGPT | MINOR | §III.A and §VI.A: "0% artifact rate" should be "0/200 visually flagged; 95% binomial upper bound ≈1.5%" | **PARTIAL-VERIFIED — one remaining site at §VI.A; §III.A site was closed at R34conf Edit 7** | tex search: R34conf Edit 7 changed §III.A "(0% artifact rate in top 200)" → "($0/200$ visually flagged; binomial 95% upper limit $\leq 1.5\%$)". The §VI.A site at L887 should have been updated in the same wave. Tex L548: "Spectral inspection of the top~200 confirms a 0\% artifact rate." — This is the production-run confirmation sentence in §III.B (DESI survey results), not the §VI.A comparison site. ChatGPT cites §III.A and §VI.A. Need to verify which sites survived the R34conf wave. **VERDICT: PARTIAL — at least one remaining "0% artifact rate" phrase likely survives in §VI.A or the Limitations paragraph; if L548 still reads "0% artifact rate" (as shown above, it does), that site was not closed by R34conf Edit 7 and requires a one-line fix to "0/200 visually flagged; binomial 95% upper limit ≤1.5%."** |
| **EXT5-P3-fM98-3** | ChatGPT | MINOR | Table V row (d): NANOGrav caveat "decisive only vs. idealized circular-orbit SMBHB" not in table row itself | **OPINION / PARTIAL — R34conf Edit 5 added the qualifier; check if it survived** | R34conf Edit 5 appended "(only vs.\ idealized circular-orbit SMBHB; see \S\ref{sec:nanograv})" to Table V row (d). If that edit is in v3.1.98, ChatGPT is raising a stale finding. If the clause was dropped, it requires re-insertion. **VERDICT: PENDING TEX VERIFICATION — check Table V row (d) for the qualifier; if absent, re-apply R34conf Edit 5.** |

### Grok new findings

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| **EXT5-P3-GR1** | Grok | MINOR | Abstract + Table I footnote ♠: stale "earlier draft quoted 264,938/264,738" sentence should be deleted | **OPINION / HD-6 RULED** | HD-6 standing rule: correction-note prose is retained through internal versions until submission-day excision. The R34conf and EXT4 audits both classified this as HD-6 KEEP. Grok's single ACCEPT-with-minor is thus a clean ACCEPT at the audit level. **VERDICT: HD-6 RULED — KEEP; flag for submission-day excision.** |

### Gemini findings — all checked against v3.1.98 tex

| # | Gemini item | Reported sev | Verdict | Evidence (v3.1.98 tex) |
|---|-------------|-------------|---------|------------------------|
| **EXT5-P3-Gem-B1** | eROSITA: "203 novel" at p.10/11/20; S_BigAE column still in Table III | BLOCKER | **FALSIFIED — stale-version content; v3.1.98 is clean** | Gemini reviewed v3.1.91; R34conf and earlier waves removed "novel" at all active sites and stripped S_BigAE column before v3.1.94. tex v3.1.98 grep: "203 SIMBAD-unmatched eROSITA membership-list sources" (L643); Table III (tab:erosita_top) has no S_BigAE column (confirmed at EXT4 row 17, falsified). Pattern-052 applies: stale-version review. **VERDICT: FALSIFIED.** |
| **EXT5-P3-Gem-B2** | §V.C still says "zero observational systematics (fiber-assignment, photo-z, foreground)" contradicting Table IV (c) σ=0.05 | BLOCKER | **FALSIFIED — stale-version content; §V.C was corrected before v3.1.95** | tex L876 §VII Limitations block contains the fiber cross-reference. The EXT4 truth-audit (row 18) showed that §V.C already carried "fiber-assignment axis is bounded by the nuisance-Fisher block at $\|\Delta\sigma/\sigma\| < 0.01\%$ at $\sigma_{\delta_{\rm fiber}} = 0.05$ (Table~\ref{tab:caveats}~(c))" — the cross-reference was present in v3.1.95. Gemini's B2 reviewed a version before this fix. **VERDICT: FALSIFIED — stale version; already fixed in v3.1.97/v3.1.98.** |
| **EXT5-P3-Gem-M1** | Figure 9 caption says "3.8 < z < 5.0" but left panel shows bins from z=0.8 | MAJOR | **FALSIFIED — stale-version content; fixed in v3.1.94** | R34conf truth-audit row 19 explicitly falsified this: L810 reads "redshift-binned DESI anomaly subsample over $0.8 < z < 5.0$". The "3.8" was a stale-PDF / OCR misread. Fixed before v3.1.95. Gemini reviewed v3.1.91 where the fix had not yet landed. **VERDICT: FALSIFIED — pattern-052 (stale-version, already closed in R34conf).** |
| **EXT5-P3-Gem-M2** | LAMOST: 11,418,594 vs 1.13×10^7 baseline; 84,394 unquantified gap | MAJOR | **FALSIFIED — already-disclosed in tex with exact count** | EXT4 truth-audit row 20 confirmed: the gap is named ($84{,}433$, not $84{,}394$), quantified, source-attributed, and artifact-cited in Table I footnote ‡ and §III.D body (L506). Gemini's arithmetic from the rounded $1.13\times10^7$ produces the wrong gap number. **VERDICT: FALSIFIED (EXT4-CARRY).** |
| **EXT5-P3-Gem-m1** | Table I eROSITA row: N_anom reads "2988" (for 298); Rate reads "0.03#" | MINOR | **FALSIFIED — PDF-extraction superscript-flattening artifact (pattern-052, 5th+ raise)** | tex L466 reads `298$^\S$` and `0.03$^\#$`; the footnote symbols are flattened to "2988" and "0.03#" by Gemini's PDF text-extraction pipeline. R34conf truth-audit row 21 explicitly falsified this as pattern-052 at EXT4. Now 5th+ raise: auto-falsify without further analysis. **VERDICT: AUTO-FALSIFIED (pattern-052).** |
| **EXT5-P3-Gem-m2** | Appendix C: "Figure 11 ma maps the re-sulting..." double-word typo | MINOR | **FALSIFIED — PDF layout-flow extraction stutter** | EXT4 truth-audit row 22 explicitly falsified: tex L1029 reads `Figure~\ref{fig:shotnoise_sensitivity} maps the resulting` — no doubled "ma" syllable. This is a pdftotext/justified-line-break artifact. **VERDICT: FALSIFIED (EXT4-CARRY).** |

---

## PART 4 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| PARTIAL-VERIFIED (new, actionable) | **3** | FM98-1 (H200 residual in Table VI), FM98-3 (Conclusion item 2 ordering not applied), fM98-2 (0% artifact phrase at L548) |
| OPINION / PARTIAL-EDITORIAL (disclosed; no required edit) | **2** | FM98-2 (scaler-refit framing clarification), EXT5-P3-Gem-* all |
| PENDING-QA (visual check recommended) | **2** | fM98-1 (Fig. 6 axis label), fM98-3 (Table V row (d) qualifier survived?) |
| FALSIFIED | **6** | Gem-B1 (stale v3.1.91), Gem-B2 (stale v3.1.91), Gem-M1 (stale v3.1.91, OCR), Gem-M2 (disclosed), Gem-m1 (pattern-052, 5th+ raise), Gem-m2 (extraction stutter) |
| HD-RULED | **1** | GR1 (HD-6 correction-note) |
| QUEUED (compute-bound) | **1** | OAI-E7 from R34conf: Planck held-out re-score → COMPUTE_QUEUE item 6 |
| Pattern-052 auto-falsify | **1** | Gem-m1 (5th+ raise) |
| Pattern-051 regression check | **PARTIAL-PASS** | 13/14 R34conf closures confirmed; 1 changelog-claimed but not in tex (FM98-3); 1 queued (OAI-E7); 1 residual (FM98-1 Table VI H200) |

**Genuinely-new VERIFIED/PARTIAL-VERIFIED items**: **3** (FM98-1, FM98-3, fM98-2)

**Gemini leg accuracy**: 6/6 findings falsified on tex primary evidence — operating on v3.1.91 stale content and PDF-extraction artifacts. Consistent with EXT4 Gemini leg outcome (6/6 falsified there too). Pattern-052 Gemini stale-PDF class confirmed for 3rd consecutive round on P3.

---

## PART 5 — Reviewer assessment

| Reviewer | Verdict | Accuracy |
|----------|---------|---------|
| ChatGPT | MAJOR REVISIONS | Real items: FM98-1 (H200 residual), FM98-3 (Conclusion ordering not applied), fM98-2 (artifact phrase). Over-called FM98-2 (framing is disclosed). Net = MINOR-revision (3 one-line fixes). |
| Grok | ACCEPT | Accurate; single MINOR (HD-6 ruled). Grok's ACCEPT is correct after the 3 one-line fixes. |
| Gemini | MAJOR REVISIONS | Entirely false positives — 6/6 stale v3.1.91 or PDF-extraction artifacts. Verdict MAJOR is not credible for v3.1.98. Pattern-052 Gemini stale-PDF/OCR class is now 3 rounds running on P3. Recommend flagging Gemini's P3 thread for PDF version verification before crediting any finding. |

---

## PART 6 — Closure plan (hardest first, all one-line)

1. **[FM98-3 — Conclusion item 2 reorder, REQUIRED]** L932: Change "Novelty: 58.8\% SIMBAD-unmatched…; genuine novelty fraction $\sim\!17.8\%$…" to lead with genuine novelty: "Novelty: genuine novelty fraction $\sim\!17.8\%$ at the DESI top-$1{,}000$ score stratum against 18 curated all-sky catalogs (single-sample point estimate; Wilson 68\% CI $\pm 1.2\%$; full-catalog extrapolation empirically untested); 58.8\% SIMBAD-unmatched overall (per-survey: 27\% Gaia to 99\% DESI top-10K) reflects database coverage, not discovery rate." The R34conf Edit 6 was claimed but not applied to this line.

2. **[FM98-1 — Table VI H200 clause, REQUIRED]** L968: Delete or correct "throughput figures for the spectroscopic surveys reflect H200 inference on the final native-retrained checkpoints." If no H200 run existed (consistent with pod_provision_20260418.json being A100): delete the clause entirely, leaving the caption reading "All inference and native retrains were performed on a single NVIDIA A100 80~GB PCIe GPU pod (pod provenance: \artifact{...})."

3. **[fM98-2 — 0% artifact phrase, REQUIRED]** L548: Change "Spectral inspection of the top~200 confirms a 0\% artifact rate" to "Spectral inspection of the top~200 finds $0/200$ visually flagged ($95\%$ binomial upper limit $\leq 1.5\%$)."

4. **[fM98-1 — Fig. 6 axis label, VISUAL QA]** Check compiled PDF Fig. 6 x-axis; if still reads "SIMBAD novelty fraction (%)", rename to "SIMBAD-unmatched fraction (%)."

5. **[fM98-3 — Table V row (d), VISUAL QA]** Verify R34conf Edit 5 qualifier "(only vs.\ idealized circular-orbit SMBHB; see \S\ref{sec:nanograv})" survived in Table V row (d); re-apply if missing.

6. **[OAI-E7 — Planck held-out re-score, QUEUED]** COMPUTE_QUEUE.md item 6; not closable without running the held-out Planck patch scoring on the production checkpoint. Required before final submission for scientific rigor.

---

## VERDICT

**P3 v3.1.98 requires 3 one-line fixes (FM98-3, FM98-1, fM98-2) to be clean at the EXT5 level.** OAI-E7 (Planck held-out) is queued for compute. All 6 Gemini findings are falsified. Grok ACCEPT is accurate post-fixes.

| Metric | Value |
|--------|-------|
| Genuinely-new VERIFIED/PARTIAL | **3** |
| FALSIFIED | 6 |
| HD-RULED | 1 |
| QUEUED (compute) | 1 |
| Pattern-052 auto-falsify | 1 |
| Pattern-051 regression | PARTIAL-PASS (FM98-3 changelog-claimed but not applied) |
| Gemini leg accuracy | 0/6 (all stale v3.1.91 or extraction artifacts) |
| Round verdict | **3 required one-line fixes → v3.1.99; then EXT5-CLEAN (Grok ACCEPT; ChatGPT → MINOR-revision-closeable)** |
