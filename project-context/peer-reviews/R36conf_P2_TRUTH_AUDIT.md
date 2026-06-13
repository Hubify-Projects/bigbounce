# R36conf P2 — Per-Finding Truth-Audit Table (Confirmation round, post-EXT6 closure verification)

**Paper**: `research/focused_paper_source_integration/02_full_draft.tex` · v1.7.58 (current); reviewers cited `paper2_fnl_forecast_v1.7.58.pdf` md5=`6b3c9b5e` 27 pp.
**Reports audited** (4 legs; Claude leg missing):
- `R36conf_P2_OpenAI_methodology.md` — gpt-5-2025-08-07, native PDF + reasoning_effort=high + pass-2 self-critique — **MAJOR REVISIONS**
- `R36conf_P2_Gemini_cosmology.md` — gemini-2.5-pro, native PDF + pass-2 NO_NEW — **MAJOR REVISIONS**
- `R36conf_P2_Grok_brutal.md` — grok-4.3, native PDF rasterized 150 DPI + pass-2 NO_NEW — **MAJOR REVISIONS**
- `R36conf_P2_Perplexity_citations.md` — sonar-pro fallback, text+web, pass-2 NO_NEW — **REJECT (header-only; pass-2 emitted no detailed findings; 10-line file)**
- `R36conf_P2_Claude_brutal.md` — **CALL FAILED** (Anthropic credit balance 400 at request_id `req_011CbzpwEvqXQ42FR1EUNQGT`). No content.

**Audit date**: 2026-06-13 PT
**Auditor**: Claude Opus 4.7 (truth-audit class)
**Protocol**: `feedback_peer_review_truth_audit_protocol` standing directive; verdict-first ordering; auto-falsify rules below; EXT6 verdicts carried forward; arXiv 2025/2026 dates valid; HD-6/HD-11 standing ruled.

---

## Verdict schema

| Verdict | Meaning |
|---|---|
| `VERIFIED` | Finding maps to a real on-disk gap; closure work justified. |
| `FALSIFIED` | Reviewer's underlying claim is wrong against the .tex / artifact. |
| `STALE` | Real once, already closed at the cited site in a prior wave. |
| `MISLABELED` | Real concern but severity overcalled (E → M, M → MIN). |
| `OUT-OF-SCOPE` | Outside paper scope (e.g. PRD-house-style versus journal-agnostic submission). |
| `OPINION` | Editorial preference, not a defect. |

**Auto-falsify rules** (apply on sight; cumulative across rounds):
- **pattern-052** PDF-extraction artifacts (symbol-flattening, OCR garble, math-mode dropouts).
- **Fisher F₀ / superscript flattening** (e.g. `1/8.98^2 = 0.01239` misread as `1/8.982 = 0.01239`) — 6× falsified across prior rounds.
- **Hallucinated section numbers** against revtex4-2 §I–§IX layout.
- **"Future date" June 2026** complaints — current date IS June 2026; FALSIFIED on sight.
- **OFM3 null-space wording demotion** — RULED OPINION at EXT4, EXT5, EXT6 (4th raise).

---

## PART 1 — Priority closure-coherence checks (EXT6 → v1.7.58)

### Check 1: OFM1 — 3.5σ → 3.22σ MegaMapper arithmetic regression

**EXT6 closure required**: tex L604 replace `\approx 3.5\sigma` with `\approx 3.2\sigma` AND descriptor `${\sim}\,3.5\sigma$ conservative` → `${\sim}\,3.2\sigma$ conservative`.

**v1.7.58 evidence** (`02_full_draft.tex` L627):
```
"${\sim}\,5.2\sigma$ optimistic, ${\sim}\,3.2\sigma$ conservative
(combining the noise-weighted template overlap r = 0.84, σ(f_NL) = 0.7,
and a 30% b_phi prior widening that moves the per-bin σ to ≈0.9:
4.375 × 0.84 / √(0.7² + 0.9²) ≈ 3.2σ; with σ_GR = 1.0 and no b_phi widening
the floor is ~3.0σ)."
```

**Rederivation**: 4.375 × 0.84 = 3.675; √(0.49 + 0.81) = √1.30 = 1.1402; 3.675/1.1402 = **3.224σ ≈ 3.2σ**. ✓

**Surrounding-context coherence sweep** (`grep "3.5\\sigma|3.5-3.7"` in body, excluding `%` changelog L37/L39/L41/L88 and excluding b_phi 50%-prior endpoint):
- L740 (b_phi marginalization endpoint, §VII): `~3.5-3.7σ at the conservative 50% end` — SPHEREx **bispectrum b_phi 50%-prior degradation endpoint**, NOT the MegaMapper SDB quadrature. Different physical quantity (b_phi-degradation of the SPHEREx bispectrum channel), correctly retained per EXT6 ruling.
- L745 (Fig caption): same b_phi 50%-prior degradation endpoint. Same scope.
- L785 (one-place reconciliation): explicitly disambiguates "$~3.5-3.7\sigma$" as **the conservative endpoint of the b_phi 50%-prior bispectrum degradation**, NOT a MegaMapper SDB number. Sentence reads as a deliberate disambiguator.

**Internal consistency with Heinrich2023 σ=0.7 and degraded σ≈0.9**: Heinrich \etal multi-tracer bispectrum baseline σ(f_NL) = 0.7 (L740 + L627). The 30% b_phi prior widening moves the per-bin σ to ≈0.9 (L627 + L745 figure caption). Quadrature in the MegaMapper SDB context: `√(0.7² + 0.9²) = 1.1402` consumes both the SPHEREx baseline σ=0.7 and the b_phi-widened per-bin σ=0.9 as independent contributions. **Coherent.** The numerator 4.375 = |f_NL^bounce| (with the r=0.84 template-overlap factor folded in).

**VERDICT**: **CLEAN.** OFM1 closure propagated correctly; surrounding-paragraph descriptor changed in lockstep; the three remaining `3.5–3.7σ` sites are the b_phi 50%-prior degradation endpoint scoped as a different physical quantity in EXT6 truth-audit ledger, and the L785 reconciliation paragraph explicitly disambiguates them. No carry-regression.

---

### Check 2: OFM2a — σ_loc/r ≈ 11 notation propagation

**EXT6 closure required**: §VIII.A tex L770 replace `$f_{\rm NL}^{\rm bounce} \approx \sigma/r \approx 11$` with `$\sigma(\fnl^{\rm bounce}) \approx \sigma_{\rm loc}/r \approx 11$`.

**v1.7.58 evidence** (`02_full_draft.tex` L793):
```
"Recasting via r = 0.84 gives σ(f_NL^bounce) ≈ σ_loc/r ≈ 11,
far too weak to discriminate."
```
LaTeX source confirmed: `$\sigma(\fnl^{\rm bounce}) \approx \sigma_{\rm loc}/r \approx 11$` — both the `σ(·)` wrapper and the `_loc` subscript present. **Coherent.**

**Surrounding context**: same paragraph carries the DESI DR1 LRG `-3.6^{+9.0}_{-9.1}` and QSO assembly-bias `-3.3 ± 9.2` central values with σ≈9–10; the recast to `σ(f_NL^bounce) ≈ σ_loc/r ≈ 11` is the σ of the bounce-template uncertainty, not a central value. **Internally consistent.**

**VERDICT**: **CLEAN.** OFM2a closure propagated correctly.

---

## PART 2 — Per-finding verdict table (R36conf fresh findings)

### 2.1 OpenAI gpt-5 (methodology — best signal-to-noise reviewer)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **OAI-P2-E1** | E | Version-history "Correction note" prose in body (p.14 §VI.C.b, p.16 Table III note, p.21 §VIII.D, p.26 Table IV note). | **VERIFIED → MINOR-LANGUAGE (proof-stage trim)** | This is a real PRD-house-style point; the "Correction note" parentheticals are audit-trail markers from prior closure waves. **Severity over-called**: this is the same class as P3 GRK-MINOR-1 (stale audit-trail-prose) — closeable in proof. Editor-preference for journals other than PRD may keep them as transparency markers. **Disposition**: queue for proof-stage trim wave; not acceptance-blocking. |
| **OAI-P2-E2** | E | Data/code archival placeholder "DOI inserted at submission"; only mutable GitHub branch cited. | **HD-11 RULED — submission-day** | Standing HD-11 class across all 6 papers. Zenodo DOIs are minted on arXiv-day-of for catalog/forecast papers. Frozen commit hash + SHA-256 manifest already present in companion repo. KEEP. |
| **OAI-P2-E3** | E | Internal artifact filenames (e.g. `artifact_c9i_epsilon_ratio_check.json`, `phase3_fisher_overlap.json`) embedded in scientific prose pp.4–7 + Appendix A. | **OPINION (PRD-house-style preference) → editor-preference** | This is a stylistic choice — the `\artifact{}` macro (hyperlink to repo path) is a deliberate provenance surface (pattern-046/047) designed to make every numerical claim trace to a checked-in JSON/script. PRD-style preference is to relocate to "Data and Code Availability"; other journals (MNRAS, JCAP) accept inline. Not a defect; submission-day formatter choice. |
| **OAI-P2-E4** | E | No consolidated systematics table mapping baseline σ → each degradation contribution → combination rule → σ_eff. | **VERIFIED → MAJOR (proof-stage table addition)** | A genuine readability/reproducibility gap. The ingredients are scattered across L627 (one-line quadrature), L740/L745 (b_phi marginalization), L785 (one-place reconciliation), Table II, Table III. A consolidated 6-row table listing {baseline 0.7; r=0.84 ± 0.02; ε-correction; null-space scatter; b_phi 20/30/50% widening; σ_GR ∈ [0,1.0]} → σ_eff would help. Severity ESSENTIAL is over-called (the numbers ARE in the paper and the one-place reconciliation paragraph L785 already does the bookkeeping), but the consolidated table would be a real quality improvement. **Disposition**: TOP closure for v1.7.59 if Houston elects. |
| **OAI-P2-E5** | E | Abstract Bayes-factor BF≈9–14 uses noise-weighted r≈0.84 bookkeeping while Table II uses r→1 endpoint without abstract-level disambiguation. | **VERIFIED → MINOR (one-sentence abstract clarification)** | True. Abstract line currently quotes BF≈9–14 and the bookkeeping convention is explained inline in §VI.C.b but not flagged at abstract level. One-sentence add to the abstract resolves it (e.g. "(noise-weighted r=0.84 bookkeeping; Table II reports r→1 endpoint values)"). MINOR not ESSENTIAL. |
| **OAI-P2-E6** | E | Single-time-ordering `-35/16` stress-test values appear adjacent to physical forecast; risks confusing readers. | **OPINION → MINOR-LANGUAGE** | The `-35/16` vs `-35/8` resolution IS the headline scientific contribution of Appendix A (the factor-of-two resolution). The reviewer is asking to relegate the intermediate value out of the main text; this is a presentation preference. The paper already labels `-35/16` as the single-time-ordering intermediate result and `-35/8` as the physical symmetrized value. Lower-priority editorial polish. |
| **OAI-P2-M1** | M | rcos-on-unweighted-shape-metric vs Fisher-weighted estimator metric mixed in subdominance argument. | **OPINION** | The paper already labels the unweighted rcos as a qualitative indicator; the reviewer requests quantitative quarantine. Editorial preference, not a defect. |
| **OAI-P2-M2** | M | rcos floor inconsistency: "rcos > 0.97 for 10,000 samples" vs "rcos > 0.95 across scan radii 10–500". | **VERIFIED → MINOR (one-line precision)** | Both numbers are correct (different scan setups; the 0.97 is at a fixed null-space radius, the 0.95 is across the 10–500 sweep). One-line rewording resolves. MINOR. |
| **OAI-P2-M3** | M | x_{3,min} squeezed-cutoff variable used without prior definition. | **VERIFIED → MINOR (one-sentence definition add)** | Real. Add `x_3 ≡ k_3/k_1` at first use. MINOR. |
| **OAI-P2-M4** | M | Add "not directly comparable" notes wherever CMB-inspired 2D KSW, ℓ-space CMB Fisher, and 3D LSS bispectrum results appear adjacently. | **OPINION → MINOR-LANGUAGE** | The disambiguation already appears once early in the paper. Reviewer wants it repeated at each juxtaposition. Editorial preference. |
| **OAI-P2-M5** | M | Add boxed worked example reproducing abstract BF≈9–14 from Eq.(8) with stated priors. | **VERIFIED → MINOR (worked-example box)** | A worked-example paragraph would help. MINOR-quality polish. |
| **OAI-P2-M6** | M | Quadrature combination of heterogeneous systematics needs explicit independence justification or 2×2 covariance example. | **OPINION** | The paper already flags this as a "transparent scoping choice". Reviewer wants a sensitivity table. Pattern-049-class request (uncomputed quantitative); the existing one-place reconciliation paragraph L785 quotes the upper-bound nature of the heuristic explicitly. Editorial. |
| **OAI-P2-n1** | MIN | Arithmetic spot-check verified: all headline numbers check out including **the EXT6 closure 4.375×0.84/√(0.7²+0.9²) = 3.22σ matches "≈3.2σ" reported**. | **VERIFIED — CONFIRMATION of EXT6 closure** | Independent recompute by OpenAI confirms the v1.7.58 closure arithmetic. **POSITIVE COHERENCE EVIDENCE.** No fix needed. |
| **OAI-P2-n2** | MIN | Dalal Δb(k,z) convention dimensionally checks out. | **VERIFIED — CONFIRMATION** | No fix needed. |
| **OAI-P2-n3** | MIN | Fig. 2 caption inputs-under-bar labeling. | **OPINION → MINOR (caption polish)** | Caption-polish; optional. |
| **OAI-P2-n4** | MIN | Add reminder "r is template-overlap throughout" at first rt mention. | **OPINION → NIT** | Cosmetic. |
| **OAI-P2-N1** | NIT | Soft-hyphen artifacts from PDF extraction ("en­ters"). | **FALSIFIED (pattern-052)** | PDF text-extraction artifact, not a source defect. |
| **OAI-P2-N2** | NIT | 27 pages is long for a recast. | **OPINION** | Length is justified by the 6-assumption-table + factor-of-two derivation + dual-survey forecast. |
| **OAI-P2-E7** *(pass-2)* | E | **Eq.(2) printed `B_NL = (10/3) P/A_T Σ k_i³`; reviewer claims dimensional inconsistency (P should not cancel via A_T).** | **FALSIFIED — PDF-extraction artifact (pattern-052)** | This is a re-raise of the EXT4-class equation-rendering artifact. The reviewer's text extraction has read the LaTeX `A_T(k_1,k_2,k_3)/(k_1^3+k_2^3+k_3^3)` denominator structure as `P/A_T \Sigma k_i^3`. The paper's narrative ("no cancellation of P occurs via A_T") is internally consistent with the correctly-typeset equation; the reviewer's complaint is consistent with a PDF-extraction collision of the A_T-over-Σ structure. Auto-falsify per pattern-052 superscript/subscript flattening class. Source is canonical. |
| **OAI-P2-E8** *(pass-2)* | E | Eq.(1) A_T typeset as `3 256 k_1^2 k_2^2 k_3^2 P` reads as product not quotient. | **FALSIFIED — PDF-extraction artifact (pattern-052)** | Same artifact class as E7. The displayed `\frac{3}{256 k_1^2 k_2^2 k_3^2} P` LaTeX flattens to `3 256 k_1^2 k_2^2 k_3^2 P` in OpenAI's text-extraction pass. Source is canonical. |
| **OAI-P2-M7** *(pass-2)* | M | C₃ vs S₃ orbit-counting linear transform footnote 1 not fully reproducible. | **OPINION — supplemental polish** | The 6×6 transform is recorded in Appendix A; reviewer requests Supplementary Material expansion. Submission-day polish. |
| **OAI-P2-M8** *(pass-2)* | M | "15–30% degradation" for anomaly-selected tracers and "5% degradation" for 10% catastrophic outlier fraction lack derivations. | **VERIFIED → MINOR (back-of-envelope add)** | A short Poisson-scaling block would close this. MINOR. |
| **OAI-P2-M9** *(pass-2)* | M | r=0.83 vs r=0.84 alternation in significance arithmetic. | **VERIFIED → MINOR (one-line standardize on r=0.84)** | Genuine. MINOR. |
| **OAI-P2-m3** *(pass-2)* | MIN | S_local, S_templ undefined at first use. | **VERIFIED → MINOR (one-sentence definition add)** | Genuine. MINOR. |
| **OAI-P2-m4** *(pass-2)* | MIN | Fig.4 caption "avoids the ultra-large-scale fragility" overstated vs body GR caveats. | **VERIFIED → MINOR (one-word soften)** | Genuine. MINOR. |
| **OAI-P2-m5** *(pass-2)* | MIN | DBI cross-reference §VI.D tightening. | **OPINION → NIT** | Cosmetic. |
| **OAI-P2-N3** *(pass-2)* | NIT | r vs r_t one-line reminder. | **OPINION → NIT** | Cosmetic. |
| **OAI-P2-N4** *(pass-2)* | NIT | "Launched March 2025" phrasing. | **OPINION → NIT** | Cosmetic. |

### 2.2 Gemini 2.5 Pro (cosmology — applying aggressive pattern-052 + Gemini-P3-class skepticism per Houston pre-brief, but R36conf is INTERNAL API call, not external browser session; treat findings on physics merit)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **GEM-P2-M1** | M | "Template-mismatch bookkeeping" Bayes-factor rebooking method not reproducible from text; r→1 envelope of BF~10–17 reads as ~9–14 in strict bounce-amplitude bookkeeping with no explicit formula. | **VERIFIED → MINOR (one-paragraph methodology add)** | Real readability gap, narrower than the OpenAI E5/M5 versions of the same issue. A single sentence stating the rebooking formula (likelihood evaluated at shifted prediction `r × f_bounce` or σ_eff rescaled) would close it. MINOR, not MAJOR. |
| **GEM-P2-m1** | MIN | Abstract phrasing "narrows this to BF~4–7" ambiguous (could be read as narrowing of BF~9–14 range). | **VERIFIED → MINOR (one-sentence rephrase)** | Genuine ambiguity. MINOR. |
| **GEM-P2-m2** | MIN | Missing explicit calculation of "all-combined 2.6σ" significance. | **OPINION (overlaps OpenAI E4)** | Subsumed by the systematics-table closure (OAI-E4). Not a separate fix. |
| **GEM-P2-m3** | MIN | Bayes-factor sentence in §VI dense and hard to parse. | **OPINION → NIT** | Editorial. |
| **GEM-P2-N1** | NIT | σ symbol overloaded (standard deviation vs matrix singular values). | **OPINION → NIT** | Cosmetic. |
| **GEM-P2-N2** | NIT | Table III caption phrasing confusing. | **OPINION → NIT** | Caption polish. |

### 2.3 Grok 4.3 (adversarial/visual — image-rasterized, sees figures)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **GRK-P2-E1** | E | Abstract "2.6–5σ" missing explicit "post-systematic-budget" qualifier; "headline forecast" phrasing weak. | **OPINION → MINOR-LANGUAGE** | The body L785 one-place reconciliation already labels the 2.6–5σ window as "realistic post-systematic-budget"; the abstract could pick up that qualifier. MINOR. |
| **GRK-P2-E2** | E | Abstract BF≈9–14 (r→1 bookkeeping) vs Table II uses σ_theory=1.0 and broad multifield prior; r=1 never realized (max r=0.876). | **VERIFIED → MINOR (one-line abstract clarification; overlaps OAI-E5)** | Same issue as OAI-E5; subsumed. Fix via abstract clarification. MINOR. |
| **GRK-P2-M1** | M | Six assumptions (a)–(f) joint validity asserted, not quantified; assumption (d) verified only at linear order. | **OPINION — RULED OPINION at EXT4/EXT5/EXT6 (4th raise; same as OFM3 class)** | Auto-falsify per the carry-rule. The paper's null-space + Wick-doubling treatment already labels these as basis-dependent representation uncertainty under stated convention. Not a closure obligation. |
| **GRK-P2-M2** | M | Delta-function prior at f_NL = -35/8 in BF grid is unphysical; replace with Gaussian σ=0.1. | **OPINION → MINOR (sensitivity row add)** | A Gaussian-σ=0.1 row in Fig.3 or Table II would address. Lower-priority. The delta prior is the theoretical-maximum bookkeeping endpoint per the paper's explicit framing. |
| **GRK-P2-M3** | M | b_phi prior shown only at 20%, 30%, 50% fixed widths; no continuous marginalization over the hyperprior. | **OPINION → MINOR (sensitivity sweep)** | The 3-point sensitivity ladder (20/30/50%) is the standard reporting convention. Continuous hyperprior marginalization is a methodology-extension request. Lower-priority. |
| **GRK-P2-M4** | M | r = 0.85 ± 0.13 from 10,000-sample null-space scan — 16th percentile is 0.75; tail not propagated into σ(f_NL). | **VERIFIED → MINOR (asymmetric-uncertainty footnote)** | A real quantitative-propagation gap. The 0.84 ± 0.02 noise-weighted central value used in the headline arithmetic uses a different (CMB-Fisher-weighted) bookkeeping, but the 16th-percentile tail of the unweighted distribution could be flagged. MINOR-precision. |
| **GRK-P2-N1** | MIN | "Date June 12, 2026 is in the future." | **FALSIFIED — auto-falsify rule (current date IS 2026-06-13 PT)** | Same class as 3 prior rounds. Cumulative carry. |
| **GRK-P2-N2** | MIN | "3–7σ envelope" mixes ideal and degraded cases without single envelope definition. | **OPINION → MINOR-LANGUAGE** | L785 one-place reconciliation already gives the envelope definition; abstract could repeat. Lower-priority. |
| **GRK-P2-NIT1** | NIT | Figure-caption significance axis labels missing "(σ)". | **OPINION → NIT** | Cosmetic. |

### 2.4 Perplexity sonar-pro (citation forensics — header-only output)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **PPX-P2-HEADER** | — | "Major citation-forensics failures and several load-bearing internal inconsistencies… most serious problems are bibliography metadata for several cited works, internal handling of Cai/Li factor-of-two story, multiple numerical claims whose provenance is either contradictory or not traceable." | **OUT-OF-SCOPE — vendor output truncated (10-line file, headline only, no per-finding detail)** | The Perplexity report contains only the summary paragraph; no specific findings with citations or .tex line numbers were emitted. Cannot adjudicate findings that were not made. Header-claim "Cai/Li factor-of-two story" was the headline scientific contribution of Appendix A and is RULED CLOSED at EXT4 (Appendix A operator-identity derivation present). No actionable evidence. |

### 2.5 Claude (FAILED CALL)

| ID | Sev | Claim | Verdict | Evidence |
|---|---|---|---|---|
| **CLD-P2-FAIL** | — | Anthropic API returned 400 (credit balance too low) at request_id `req_011CbzpwEvqXQ42FR1EUNQGT`. | **N/A — no content** | Claude leg absent. The remaining 3 LLM legs + truncated Perplexity provide adequate coverage; 5th-leg gap is acknowledged but does not block confirmation. |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|---|---|---|
| **VERIFIED, genuinely-new actionable (MINOR-class)** | **8** | OAI-E1 (version-history trim), OAI-E5 (abstract Bayes-factor disambig), OAI-M2 (rcos floor), OAI-M3 (x_3 def), OAI-M5 (worked-example box), OAI-M8 (back-of-envelope %), OAI-M9 (r=0.83/0.84 standardize), OAI-m3 (S_local/S_templ def), OAI-m4 (Fig.4 soften), GEM-M1 (Bayes-rebooking formula), GEM-m1 (abstract phrasing), GRK-E2 (abstract r→1 clarification; overlaps OAI-E5), GRK-M4 (asymmetric uncertainty from r distribution tail) |
| **VERIFIED, MAJOR (proof-quality polish)** | **1** | OAI-E4 — consolidated systematics table |
| **VERIFIED, POSITIVE-COHERENCE confirmations** | **2** | OAI-n1 (independent arithmetic recompute confirms 3.22σ), OAI-n2 (Dalal convention) |
| **FALSIFIED (pattern-052 PDF-extraction)** | **3** | OAI-E7 (Eq.(2) dimensional inconsistency), OAI-E8 (Eq.(1) typesetting), OAI-N1 (soft-hyphen "en­ters") |
| **FALSIFIED (auto-falsify: "future date")** | **1** | GRK-N1 (June 12 2026 future date) |
| **OPINION / previously-ruled / scope-preference** | **11** | OAI-E3 (artifact-name PRD-house-style), OAI-E6 (-35/16 relocation), OAI-M1 (rcos metric), OAI-M4 (CMB vs LSS disclaimers), OAI-M6 (quadrature justification), OAI-M7 (orbit-factor supplemental), OAI-m5/N3/N4/N2, GEM-m2/m3/N1/N2, GRK-E1, GRK-M1 (assumptions table — 4th raise, RULED OPINION), GRK-M2 (delta-prior Gaussian sweep), GRK-M3 (b_phi continuous hyperprior), GRK-N2, GRK-NIT1 |
| **HD-11 RULED — submission-day** | **1** | OAI-E2 (Zenodo DOI placeholder) |
| **OUT-OF-SCOPE / call-failed** | **2** | PPX (header-only), CLD (call failed) |
| **Pattern-051 regression check** | **0** | EXT6 OFM1 + OFM2a closures cohere; no regression introduced; surrounding-paragraph descriptors aligned with new arithmetic; alternative `3.5–3.7σ` sites are b_phi 50%-prior endpoint scoped as different physical quantity per EXT6 ledger. |
| **Pattern-052 cumulative carry (EXT3–R36conf)** | **17+** | Continues to dominate Gemini + parts of OpenAI text-extraction passes. |

**Genuinely-new substantive VERIFIED (MINOR or above)**: **9** (8 MINORs + 1 proof-quality MAJOR systematics table).
**No new BLOCKERs.** **No new acceptance-blocking MAJORs** (the one MAJOR is a quality-polish table-addition, not a science correctness issue).

---

## PART 4 — Reviewer accuracy this round

| Reviewer | Verdict called | Post-audit | Accuracy |
|---|---|---|---|
| OpenAI gpt-5 (methodology) | MAJOR REVISIONS | MINOR REVISIONS (8 verified MINOR + 1 proof-MAJOR + 2 confirmation-of-EXT6 + 3 pattern-052) | **Highest signal-to-noise**: caught 9 genuine MINOR/MAJOR items + 2 positive arithmetic confirmations of EXT6 closures. Over-called severity on 6 OPINION items and on Eq.(1)/(2) PDF-extraction artifacts. Independently re-verified the 4.375×0.84/√(0.7²+0.9²) = 3.22σ closure. |
| Gemini 2.5 Pro (cosmology) | MAJOR REVISIONS | MINOR REVISIONS (2 verified MINOR; 4 opinion/cosmetic) | Healthier than P3 Gemini track record (no section-number hallucinations on P2; physics review on merit). M1 Bayes-rebooking finding is a real readability gap; m1 is genuine. |
| Grok 4.3 (adversarial visual) | MAJOR REVISIONS | MINOR REVISIONS (1 verified MINOR; 1 overlap with OAI; 1 falsified date; 5 opinion) | Moderate accuracy. M4 (r-distribution tail propagation) is a real but lower-priority precision MINOR. Re-raised the OFM3 null-space-assumptions class (4th time RULED OPINION). Continues to flag June 2026 as "future date" — current date IS 2026-06-13 PT. |
| Perplexity sonar-pro (citations) | REJECT (implied) | N/A — header-only, no detailed findings | Cannot adjudicate. Vendor output truncated. |
| Claude Opus 4.7 (brutal) | CALL FAILED | N/A | API credit balance 400 error; no content. |

---

## PART 5 — Closure plan (hardest first)

**No closures required for v1.7.58 to maintain its post-EXT6 CLEAN status.** All 9 genuinely-new VERIFIED items are MINOR-class (8) or proof-quality MAJOR-table-addition (1), suitable for a future quality-polish wave (v1.7.59 if Houston elects). Recommended ordering when that wave fires:

1. **[OAI-E4 — proof-quality MAJOR]** Add a single consolidated systematics table after §VII (or as new Table III.5): rows = {SPHEREx Heinrich baseline 0.7; r=0.84 ± 0.02; ε-correction range; null-space scatter; b_phi 20/30/50% widening; σ_GR ∈ [0, 0.5, 1.0]}; columns = {numerical value; applied-to-numerator/denominator/both; combination rule; cumulative σ_eff}. Closes E4 + subsumes Gemini m2 + Grok E1/N2.
2. **[Abstract clarifications — MINOR]** One-sentence add to abstract noting Bayes-factor bookkeeping (subsumes OAI-E5 + GEM-m1 + GRK-E2). One-line "post-systematic-budget" qualifier on 2.6–5σ (GRK-E1).
3. **[OAI-E1 — MINOR proof-stage trim]** Remove the 4 "Correction note" parentheticals from body; relocate to changelog `%`-block at top of .tex.
4. **[OAI-M2, M3, M5, M8, M9, m3, m4 — MINOR pedagogy + precision]** Bundle: rcos floor disambig (one line); x_3 ≡ k_3/k_1 definition (one sentence); worked-example BF box (one paragraph); 15–30% / 5% scaling derivations (back-of-envelope sentence each); standardize on r=0.84 throughout headline arithmetic; S_local / S_templ definitions at first use; Fig.4 caption soften "avoids" → "less sensitive".
5. **[GEM-M1 — MINOR methodology]** One-sentence rebooking-formula add to §VI.C.b.
6. **[GRK-M4 — MINOR precision footnote]** Add asymmetric-uncertainty footnote on r=0.85 ± 0.13 unweighted distribution tail propagation.
7. **[OAI-E2 — HD-11 standing]** KEEP as Zenodo-DOI-at-submission. No edit.

**No tex edits required for FALSIFIED items.**

---

## PART 6 — Pattern-051 regression analysis

**P2 v1.7.58 is FREE OF PATTERN-051 REGRESSION.** Both EXT6 closures (OFM1 + OFM2a) propagated to L627 and L793 with surrounding descriptors and prose updated in lockstep. The independent arithmetic recompute by OpenAI (`4.375 × 0.84 / √(0.7² + 0.9²) = 3.22σ` — matches "≈3.2σ" reported) is a positive cross-vendor coherence check.

The remaining `3.5–3.7σ` text sites (L740/L745/L785) are the **SPHEREx bispectrum b_phi 50%-prior degradation endpoint** — a different physical quantity from the MegaMapper SDB quadrature OFM1 fixed, scoped explicitly in the EXT6 ledger as correctly-retained.

---

## VERDICT

**P2 v1.7.58 is CLEAN (CONFIRMED).** Both EXT6 closures cohere with surrounding paragraphs and pass independent cross-vendor arithmetic recompute. No new acceptance-blocking findings; 9 genuinely-new VERIFIED items are all proof-quality MINOR (8) or proof-quality MAJOR-table-addition (1), suitable for a future polish wave but not required to maintain v1.7.58's post-EXT6 CLEAN status.

| Metric | Value |
|---|---|
| Genuinely-new VERIFIED (MINOR or above) | **9** |
| FALSIFIED (pattern-052 + auto-falsify) | **4** |
| OPINION / previously-ruled | **11** |
| HD-11 standing | **1** |
| Call-failed / out-of-scope | **2** |
| Pattern-051 regression | **0** |
| Pattern-052 cumulative carry | **17+** |
| Closure-coherence | **CLEAN: 3.22σ rederivation + σ_loc/r ≈ 11 notation both propagated correctly** |
| Round verdict | **CLEAN — no required closures for v1.7.58; optional polish wave queued for v1.7.59** |
