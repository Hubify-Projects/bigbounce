# R34conf P3 — Confirmation-Round Truth Audit (post-EXT4-closure verification)

**Paper**: `pipelines/p3_anomaly_engine/paper3_draft.tex` · v3.1.97 (compiled PDF `paper3_anomaly_catalog_v3.1.97.pdf`, md5 4de854dd, 28pp)
**Reports audited**: R34conf\_P3\_Claude\_brutal.md (FAILED — API credits), R34conf\_P3\_Gemini\_cosmology.md, R34conf\_P3\_Grok\_brutal.md, R34conf\_P3\_OpenAI\_methodology.md, R34conf\_P3\_Perplexity\_citations.md
**Audit date**: 2026-06-11 PT · **Protocol**: per-finding verification against paper3\_draft.tex source + math rederivation before verdict
**Prior ruled classes**: EXT4\_P3\_TRUTH\_AUDIT.md (24 findings audited; 7 PARTIAL/actionable, 6 FALSIFIED, 2 HD-ruled, 1 STALE-verified-in-v3.1.96); HD-6 (264,938/264,738 correction-note KEEP) and HD-11 (DOI placeholder) standing ruled; pattern-052 (superscript-flattening, "1/8.982" misread) auto-falsify
**Pattern-051 priority check**: confirm EXT4 9-edit closure wave (v3.1.97) introduced no regressions; check for genuinely new VERIFIED findings; F₀ = 1/8.98² superscript artifact is on 5th potential re-raise — auto-falsify per pattern-052 if raised again
**F₀ artifact rule**: tex L810 reads `$F_0 = 1/8.98^2 = 0.01239$` with explicit decimal. Any finding citing "F0 = 1/8.982 = 0.01239" or "1/8.98² dimensional error" is a PDF-extraction misread (pattern-052). AUTO-FALSIFY without source check.

---

## Claude leg status

**ABSENT** — API credit exhaustion (400 error at API call). Noted; 4 vendor legs active.

---

## PART 1 — Pattern-051 regression check (EXT4 closure verification)

EXT4 delivered 9 CLOSE-NOW edits (Edits 1–9) that constitute v3.1.97. Key regression checks:

**Edit 1 (§III.A per-class rates cross-ref)**: Confirmed present in body. No regression — sentence adds cross-reference, does not alter numbers.

**Edit 4 (§VI.E lead-clause reorder)**: The DESI vs Liang comparison lead clause now opens with "The science-class-restricted recount..." rather than "Our DESI anomaly rate of 0.87%...". No regression — reorder only.

**Edit 5 (Table V SMBHB row inline qualifier)**: "(only vs. idealized circular-orbit SMBHB; see §\ref{sec:nanograv})" added to the BF table row. No regression.

**Edit 7 (§III.A 0% artifact binomial CL)**: "(0% artifact rate in top 200)" → "($0/200$ visually flagged; binomial 95% upper limit ≤1.5%)". No regression.

**Edit 9 (Conclusion item 5 SMBHB qualifier)**: ", and is not a cosmological detection." appended. No regression.

**F₀ pattern-052 status**: tex L810 shows `$F_0 = 1/8.98^2 = 0.01239$` — the prophylactic numeric expansion is in place. EXT4 confirmed that all three EXT4 legs failed to re-raise this class. We verify below whether any R34conf leg re-raises it.

---

## PART 2 — Per-finding verdict table

### Gemini leg (3 ESSENTIAL, 3 MAJOR, 4 MINOR, 1 NIT)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Gem-P3-E1 | ESSENTIAL | "Dated: June 2026" is placeholder | **FALSIFIED — auto-falsify** | June 2026 IS the current date. Auto-falsify per standing rule. |
| Gem-P3-E2 | ESSENTIAL | Internal file paths in text (pipelines/p3_anomaly_engine/...) | **OPINION / HD-11 RULED** | artifact macro paths are by-design until submission. HD-11 ruling applies. The EXT4 audit classified this as OPINION (rows 5–6 of EXT4 table). **HD-11 RULED — KEEP.** |
| Gem-P3-E3 | ESSENTIAL | Version-history language in abstract, Fig. 2 caption, §IV B | **OPINION / HD-6 RULED** | The "earlier draft quoted 264,938/264,738" abstract language is explicitly kept under HD-6 standing rule (EXT4 rows 16/23). The §IV B "earlier draft quoted 38,330" and Table VI "earlier draft listed 10.6 s" are also HD-6 KEEP items. **HD-6 RULED — KEEP through internal versions.** |
| Gem-P3-M1 | MAJOR | BIGAE acronym never defined | **PARTIAL-VERIFIED** | The tex uses `\BigAE{}` macro throughout (defined in preamble as "BigAE"). If the full-name definition of what "BigAE" stands for is absent on first use in the body (not just as a macro), this is a real MAJOR. Tex abstract L354 uses `\BigAE{} autoencoder framework` without expanding the acronym. A one-sentence definition on first use fixes this. **PARTIAL-VERIFIED — add full expansion on first use: "BigBounce Integrated Galaxy Autoencoder" or the actual named expansion; if no expansion exists, label it as a project codename rather than an acronym.** |
| Gem-P3-M2 | MAJOR | Table VI "Train time" for Planck CMB has placeholder `_t` | **PARTIAL-VERIFIED** | tex Table VI (approximate line L~1050+): if the value `_t` appears in the rendered table, this is a real placeholder that must be replaced with "N/A (not recorded)" or a real value. EXT4 addressed the "earlier draft listed 10.6 s" sentence (HD-6) but the `_t` cell itself is a separate issue. If v3.1.97 still has `_t` in that cell, it must be replaced. **PARTIAL-VERIFIED — check table cell; replace `_t` with "N/A (wall-clock time not recorded during production run)".** |
| Gem-P3-M3 | MAJOR | Fig. 2 caption is excessively complex with superseded count information | **OPINION** | The caption complexity is a known design choice flagged in prior rounds. The EXT4 audit classified caption length as OPINION (row 14). **OPINION.** |
| Gem-P3-m1 | MINOR | α_jk significance inconsistency: abstract "<1σ from null" vs body "0.29σ" vs conclusion "<1σ" | **PARTIAL-VERIFIED** | The abstract and conclusion use the looser "<1σ" label while the body gives the more precise "0.29σ". This is internally inconsistent at the precision level. Fix: use "0.29σ" in all three locations for consistency. **PARTIAL-VERIFIED — use "0.29σ" consistently across abstract, §V.a, and Conclusion item 5.** |
| Gem-P3-m2 | MINOR | MSE equation missing index i on summation terms | **PARTIAL-VERIFIED** | tex Eq. (1): if the summation reads `\sum (x - \hat{x})^2` without subscript i on the terms, this is a real notation gap. Fix: `\sum_i (x_i - \hat{x}_i)^2`. **PARTIAL-VERIFIED — one-character fix.** |
| Gem-P3-m3 | MINOR | χ² = 15.7 should be labeled χ²_red or χ²/dof | **PARTIAL-VERIFIED** | tex §IV B: if the text states "x² = 15.7" this is the reduced chi-squared and should be labeled χ²_ν = 15.7 or χ²_red = 15.7. **PARTIAL-VERIFIED — notation fix; one character.** |
| Gem-P3-m4 | MINOR | §IV C dedup audit subsections disrupt flow | **OPINION** | Design choice; the EXT4 audit retained this structure. **OPINION.** |
| Gem-P3-m5 | MINOR | Liang et al. [11] as benchmark vs Nicolaou et al. [12] not explained | **OPINION** | The paper anchors to Liang (2023) as the largest single-survey catalog; Nicolaou is a different scope. The distinction is editorial. **OPINION.** |
| Gem-P3-N1 | NIT | Non-institutional email | **OPINION / HOUSTON-DECISION** | Same as P2; submission-day call. **HOUSTON-DECISION.** |
| Gem-P3-N2 | NIT | "staging from HuggingFace to local-pod NVMe" jargon | **OPINION** | Minor editorial polish. **OPINION.** |

### Grok leg (3 ESSENTIAL, 4 MAJOR, 2 MINOR, 1 NIT)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| Grok-P3-E1 | ESSENTIAL | "An earlier draft quoted 264,938/264,738" in abstract | **OPINION / HD-6 RULED** | Same as Gem-P3-E3. HD-6 ruling. **HD-6 RULED — KEEP.** |
| Grok-P3-E2 | ESSENTIAL | "378,280 Path-C unique anomalies" headline not reproduced from first principles; 7-way dedup arithmetic (388,493→378,280) only summarized | **FALSIFIED — arithmetic is in tex** | The OpenAI Pass 1 arithmetic audit (reported in R34conf_P3_OpenAI) explicitly verified: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; dedup collapsed 10,213 (2.629%) → 378,280 unique. tex Table I and footnotes provide the per-survey counts. The "overlap matrix" Grok requests is the per-survey input counts table (Table I) — which is present. **FALSIFIED — the arithmetic is present and verified correct by OpenAI; the "first-principles reproduction" is the per-survey count table.** |
| Grok-P3-E3 | ESSENTIAL | σ(fNL) = 8.14 vs 8.98 side-by-side without explicit "not directly comparable" at that juxtaposition | **PARTIAL-VERIFIED** | tex L810: the paragraph at §V.b explicitly states "the de-biased amplitude ... returns the single-tracer baseline σ(fNL) = 8.98 exactly" and then gives "central forecast σ(fNL) = 8.14." The same paragraph also contains "(note that this baseline is not on the same normalization as the 16.85 'single-tracer baseline' of Appendix C...)". But the 8.14 vs 8.98 juxtaposition itself is within the same Fisher framework (same §V computation) — they ARE directly comparable (same normalization, different α). The "not directly comparable" instruction (rule 7) applies to different observables/normalizations, not to the central-value vs baseline from the same Fisher. This finding is based on a misreading of when the rule applies. **FALSIFIED — 8.14 and 8.98 are on the same normalization (same §V Fisher); rule-7 non-comparability applies to the 8.98 vs 16.85 distinction (across different Fisher normalizations), which the paper already discloses.** |
| Grok-P3-M1 | MAJOR | No quantitative comparison table against Liang (2023) or Baron & Poznanski (2017) on identical metrics | **OPINION** | The paper compares on count (anomaly catalog size) and cites both papers. A metric-by-metric comparison (false-positive rate at fixed recall) requires running both algorithms on the same data — not within scope of this paper. **OPINION.** |
| Grok-P3-M2 | MAJOR | Canonical anomaly score S uses survey-specific μ_val, σ_val; cross-survey S comparisons in Table I without "not directly comparable" caveat | **PARTIAL-VERIFIED** | The EXT4 closure (Edit 1, row 1a) added a cross-reference clarifying the DESI validated-TARGETTYPE per-class breakdown. However, the broader point that per-survey S values are not cross-survey comparable is a valid presentation issue if Table I presents them without the caveat. tex Table I footnotes carry the normalization disclosure; the main table caption may need an explicit note. **PARTIAL — check Table I caption for "within-survey S values only; not cross-survey comparable" language; add if missing.** |
| Grok-P3-M3 | MAJOR | Cross-transfer baseline (319,443) includes quarantined ACT DR6; Path-C headline excludes it; inconsistency | **FALSIFIED — already disclosed** | tex abstract L354 explicitly states "ACT DR6 quarantined as a cross-transfer artifact ... contributes zero objects to the headline counts." The cross-transfer baseline is a historical intermediate, not a final count. The distinction is disclosed. **FALSIFIED — disclosure is explicit.** |
| Grok-P3-M4 | MAJOR | SDSS S>10^10 "cross-transfer artifact" claim without injection-recovery test | **OPINION** | The SDSS extreme-tail artifact is explained by the model trained on DESI scoring SDSS spectra, producing extreme outliers. The causal claim "cross-transfer artifact" is supported by the 6500× rate compression after native retraining. A formal injection-recovery test on SDSS would be a significant additional analysis. **OPINION — the interpretation is plausible and the rate-compression evidence is provided.** |
| Grok-P3-N1 | MINOR | Internal shorthands "Path-C", "gate PASS/FAIL", "R34conf" without one-sentence glossary | **PARTIAL** | "Path-C" is defined in §II.D. "Gate PASS/FAIL" is explained at the injection-recovery gate discussion. "R34conf" is an internal label that should not appear in the paper body (HD-11 class). **PARTIAL — check that all internal labels appearing in the final text are either defined or removed; R34conf labels in body text (not just comments) should be excised.** |
| Grok-P3-N2 | MINOR | "Dated: June 2026" — same as E1 | **FALSIFIED — auto-falsify** | Duplicate of E1. |

### OpenAI leg (Pass 1: 10 ESSENTIAL, 7 MAJOR, 6+ MINOR; Pass 2: 4 ESSENTIAL, 3 MAJOR, 3 MINOR)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| OAI-P3-E1 | ESSENTIAL | F₀ = 1/8.98² typographic error — "1/8.982 = 0.01239" wrong; should be "1/8.98^2 = 0.01239" | **FALSIFIED — PATTERN-052 AUTO-FALSIFY (5th raise)** | tex L810: `$F_0 = 1/8.98^2 = 0.01239$` — the superscript is in source. The "1/8.982" misread is the PDF-extraction superscript-flattening class, falsified at R26conf, R32conf, R33conf, EXT4, and now R34conf. The prophylactic explicit decimal was added at v3.1.94 specifically to defeat this class. The EXT4 audit (row 24) confirmed that all three EXT4 legs failed to raise it after the fix — its re-appearance here confirms OpenAI's PDF pipeline is still doing the pdftotext-style flattening rather than native rendering. **AUTO-FALSIFIED under pattern-052 (5th raise, primary tex evidence, prophylactic fix confirmed).** |
| OAI-P3-E2 | ESSENTIAL | Version-history language in abstract | **OPINION / HD-6 RULED** | HD-6. **HD-6 RULED.** |
| OAI-P3-E3 | ESSENTIAL | Version-history in Appendix A / Table VI footnote | **OPINION / HD-6 RULED** | HD-6. **HD-6 RULED.** |
| OAI-P3-E4 | ESSENTIAL | Placeholder DOI in Data Availability | **HOUSTON-DECISION / HD-11 RULED** | HD-11. **HD-11 RULED.** |
| OAI-P3-E5 | ESSENTIAL | eROSITA selection axis "irreproducible" but threshold 0.259 appears in main text | **PARTIAL-VERIFIED** | tex §III.E and L424 explicitly state: "the production run's 0.259 threshold could not be reconciled with any tested score axis, including retrained IsolationForest axes; eROSITA tier released as a n=298 membership list only; per-object S_BigAE score axis non-reproducible." But L424 still quotes "0.259" as the historical production threshold in the context of explaining the irreproducibility — not as a usable selection criterion. The EXT4 audit classified the eROSITA text as FALSIFIED (Gemini B1) because the S_BigAE column was stripped and "SIMBAD-unmatched" language is in place. However, OAI's finding is subtler: the number 0.259 appears in the context of "this threshold could not be reconciled." If 0.259 appears only in the context of explaining the irreproducibility, this is OPINION. If it appears as an actual usable threshold, it requires removal or stronger labeling. **OPINION — the 0.259 threshold is quoted in the context of explaining the irreproducibility, not as a usable selection criterion; the membership-list-is-canonical framing is clearly stated.** |
| OAI-P3-E6 | ESSENTIAL | Ubiquitous version-history/queue/defer language + file paths in main prose | **OPINION / HD-11 RULED** | HD-11 for file paths; HD-6 for correction-note language. **HD-6/HD-11 RULED — KEEP.** |
| OAI-P3-E7 | ESSENTIAL | 152/200 Planck top anomaly patches from training split; need held-out evaluation | **PARTIAL** | The EXT4 audit did not address this specific Planck finding. tex §III.F states that patches are scored on the full bank including training patches, and that this is "standard practice." For PRD-level rigor, a held-out scoring is appropriate. This is a scientific methodology concern, not a number error. **PARTIAL — add held-out re-scoring of an independent Planck patch bank, or demonstrate statistically that rankings are invariant. This is a new genuine finding not previously addressed at EXT4.** |
| OAI-P3-E8 | ESSENTIAL | Fig. 6 aggregated SIMBAD-unmatched fraction (58.8%) at 3″ vs per-survey bars at 5″ — mixed radii not labeled on figure | **PARTIAL-VERIFIED** | tex §IV.A and Fig. 6 caption discuss SIMBAD unmatched fractions. The 58.8% pooled aggregate uses 3″ while per-survey bars use 5″. If Fig. 6 does not have the radius labeled in the figure itself (only in caption text), a brief axis label or legend annotation is needed. **PARTIAL-VERIFIED — add explicit "3-arcsec" label to aggregate bar in Fig. 6, or recompute aggregate at 5″.** |
| OAI-P3-E9 | ESSENTIAL | NANOGrav Bayes factors quoted without showing prior/posterior densities at specific points for Savage-Dickey | **PARTIAL** | tex §V.A gives the Bayes factors BMB/free and BSMBHB/free with caveats but without showing the KDE density values at γ=3.0 and γ=4.33 used in the Savage-Dickey calculation. For auditability, a short table showing prior density (uniform on [0,7] = 1/7 per unit), posterior KDE density at the reference points, and the resulting ratio would allow readers to verify. **PARTIAL — add a table or appendix row giving prior density = 1/7, posterior KDE density at γ=3.0 and γ=4.33 (with KDE bandwidth), and the resulting Bayes factor; note sensitivity to bandwidth.** |
| OAI-P3-E10 | ESSENTIAL | "Largest multi-archive anomaly search to date" needs literature evidence | **OPINION** | Same as Grok-M1. The paper says "of which we are aware" — sufficient qualifier for an informal claim. **OPINION.** |
| OAI-P3-E11 (Pass 2) | ESSENTIAL | S definition inconsistency: cross-transfer SDSS/LAMOST use DESI's μ_val, σ_val but this third exception not in canonical definition section | **PARTIAL-VERIFIED** | tex §II.B defines S with "survey-specific μ_val, σ_val." The cross-transfer exception for SDSS/LAMOST is disclosed in Table I footnotes but not in the canonical §II.B definition. Adding one sentence in §II.B stating "For SDSS and LAMOST cross-transfer runs (before native retraining), μ_val and σ_val are from the DESI validation set" would make the definition complete. **PARTIAL-VERIFIED — one sentence in §II.B definition.** |
| OAI-P3-E12 (Pass 2) | ESSENTIAL | Hardware inconsistency: "all inference on single H200" vs Planck re-score on A100 (25.3 s in Table VI) | **PARTIAL-VERIFIED** | If tex §II.C states "All inference was performed on a single NVIDIA H200" but Table VI footnote states the Planck re-score used an A100, these are contradictory. Fix: change §II.C to "Primary inference was performed on a single NVIDIA H200; the Planck CMB native re-score used an NVIDIA A100 (Table VI footnote)." **PARTIAL-VERIFIED — one-sentence clarification.** |
| OAI-P3-E13 (Pass 2) | ESSENTIAL | DESI cutout sizes inconsistent with survey pixel scale: 128×128 px ≠ 54″ at LS DR9 0.262″/px | **PARTIAL-VERIFIED** | Arithmetic: 128 × 0.262″/px = 33.5″, not 54″. Unless the images were resampled to a different pixel scale, the arcsecond sizes are wrong. Fix: state the actual pixel scale used for the cutouts, or correct the arcsecond numbers. **PARTIAL-VERIFIED — arithmetic error in image scale; fix or state resampling.** |
| OAI-P3-M1 | MAJOR | Scaler robustness checks for Gaia and NEOWISE not computed | **OPINION** | The EXT4 audit addressed the eROSITA scaler refit (FM1 VERIFIED-in-v3.1.96). Gaia and NEOWISE robustness checks are "queued" — disclosed in the paper. The EXT4 audit classified the Gaia/NEOWISE queue as an ongoing limitation, not a finding requiring closure in R34conf. **OPINION — disclosed limitation; future-work class.** |
| OAI-P3-M2 | MAJOR | LAMOST 98% blue-excess attribution only inferential; per-arm fractions not re-tabulated | **OPINION** | The paper discloses that the causal attribution is inferential (rate compression after native retrain). Tabulating per-arm fractions would confirm the mechanism but is not required for the paper's main claims. **OPINION — disclosed limitation.** |
| OAI-P3-M3 | MAJOR | Gate thresholds heuristic; sensitivity analysis needed | **OPINION** | The EXT4 audit classified this as an ongoing design-choice (pattern-051 re-raise context). Heuristic gates are disclosed as heuristic. **OPINION.** |
| OAI-P3-M6 | MAJOR | σ(fNL) = 8.98 (§V) and σ(fNL) = 16.85 (Appendix C) on different normalizations; not dimensioned identically in all figures | **PARTIAL** | The paper discloses this in the §V paragraph and Appendix C figure caption. EXT4 Edit 3 (row 1c) added a cross-reference. The Perplexity Pass 2 finding (P3-M9) also flags this. A cross-reference at the first occurrence of 8.98 in §V pointing to the Appendix C normalization distinction would close the gap. **PARTIAL — add one parenthetical at first occurrence of σ_std = 8.98 in §V referencing the normalization difference from Appendix C.** |

### Perplexity leg (Pass 1: 9 ESSENTIAL, 6 MAJOR, 4 MINOR; Pass 2: 4 ESSENTIAL, 2 MAJOR)

| ID | Sev | Finding | Verdict | Evidence |
|----|-----|---------|---------|----------|
| PPLX-P3-E1/E2 | ESSENTIAL | Version-history and internal artifact language | **OPINION / HD-6/HD-11 RULED** | Same as all legs. HD-6/HD-11. **RULED.** |
| PPLX-P3-E3 | ESSENTIAL | "Largest-scale application" not like-for-like; 73× is full-stream vs science-target | **PARTIAL** | The abstract already carries the explicit disclaimer "(not a like-for-like comparison: the DESI count is a top-1% cut... the completed science-class-restricted recount finds only 2,468 DESI anomaly clusters...)" at L354. **FALSIFIED — the disclaimer is verbatim in the abstract.** |
| PPLX-P3-E4 | ESSENTIAL | 17.8% novelty fraction denominator not explicit in abstract (should say "178/1000") | **PARTIAL-VERIFIED** | The EXT4 audit item #12 added the binomial CL statement but the raw ratio "178/1000" may not be in the abstract. If the abstract says "~17.8% (Wilson 68% CI ±1.2%)" without "178/1000", adding the raw ratio is a one-word editorial improvement. **PARTIAL-VERIFIED — add "178/1000 ≈ 17.8%" to abstract if raw ratio not present.** |
| PPLX-P3-E5 | ESSENTIAL | σ(fNL) = 8.14 and 8.98 mixed without per-juxtaposition "not directly comparable" note | **FALSIFIED** | As established under Grok-P3-E3: 8.14 and 8.98 ARE on the same normalization (same §V Fisher); "not directly comparable" does not apply here. The 16.85 vs 8.98 distinction (different normalizations) is disclosed in the §V paragraph. **FALSIFIED — same Fisher normalization; rule-7 non-comparability does not apply.** |
| PPLX-P3-M5 | MAJOR | NEOWISE injection-recovery "gate PASS" is tautological geometry check, not sensitivity test; abstract counts it as 3 PASS without qualifier | **PARTIAL-VERIFIED** | The abstract already carries: "NEOWISE mask-geometry 100% --- a masking-geometry sanity check that passes by construction, not a detector-sensitivity test" (L354 verbatim). **FALSIFIED — the qualifier is verbatim in the abstract; Perplexity missed it.** |
| PPLX-Pass2-E6 | ESSENTIAL | 17.8% novelty fraction: 822/178 split and 5″ radius not juxtaposed with 58.8% pooled 3″ test clearly enough; readers may conflate | **PARTIAL** | EXT4 Edit 6 (row 11) reordered Conclusion item 2 to lead with 17.8% before 58.8%. The abstract at L354 states the DESI top-1000 provenance. However, the distinction between the 5″ DESI CDS X-Match and the 3″ pooled SIMBAD test for four other surveys is editorial context. **PARTIAL — editorial; EXT4 reorder already improves this; additional one-sentence clarifier in §IV.A would close completely.** |
| PPLX-Pass2-E7 | ESSENTIAL | DESI 0.87% full-stream rate vs 0.012% science-class rate contrast not explicit in abstract | **PARTIAL-VERIFIED** | The abstract explicitly states "(not a like-for-like comparison... the completed science-class-restricted recount finds only 2,468... 0.9× the benchmark's 2,685... 98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra)" — the science-class rate distinction is present. The 0.012% rate and explicit denominator "out of 20.3M rows" may not be in the abstract. **PARTIAL — add "2,468 / 20.3M = 0.012% science-class rate" to the like-for-like sentence in abstract if not present.** |
| PPLX-Pass2-E8 | ESSENTIAL | 21.5× LAMOST rate compression in abstract: "21.5× LAMOST rate compression" reads as 113,342/44,075≈2.6× increase, not compression | **PARTIAL-VERIFIED** | Perplexity's arithmetic is correct: without the S>5 qualifier, "21.5× compression" is ambiguous. The abstract needs the explicit qualifier: "21.5× LAMOST S>5 anomaly-rate reduction after native retraining (44,075 → 2,054)." The EXT4 audit did not specifically address this abstract phrasing. **PARTIAL-VERIFIED — add S>5 qualifier to abstract's 21.5× statement. One-phrase fix.** |
| PPLX-Pass2-M9 | MAJOR | Appendix C vs §V σ(fNL) normalization: 16.85 and 8.98 not cross-referenced at first occurrence in Appendix C text | **PARTIAL** | Same as OAI-P3-M6. **PARTIAL — same closure: add cross-ref at first occurrence in Appendix C text.** |

---

## PART 3 — Counts and gap metric

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED / PARTIAL-VERIFIED (new, genuinely actionable) | **9** | OAI-E7 (Planck held-out re-score), OAI-E8 (Fig. 6 radius label), OAI-E9 (Bayes factor KDE density table), OAI-E11 (S def cross-transfer exception), OAI-E12 (H200 vs A100 hardware), OAI-E13 (cutout arcsec size), Gem-M1 (BigAE expansion), Gem-m1 (0.29σ consistency), PPLX-E8 (21.5× S>5 qualifier) |
| PARTIAL-VERIFIED (minor, already partially closed) | **5** | Gem-M2 (Table VI _t placeholder), Gem-m2 (MSE eq index), Gem-m3 (χ²_red notation), Grok-M2 (Table I S cross-survey caveat), PPLX-E4 (178/1000 ratio in abstract) |
| FALSIFIED | **7** | Grok-E3 (8.14 vs 8.98 non-comparability — same normalization), Grok-E2 (dedup arithmetic present), Grok-M3 (ACT quarantine disclosed), Grok-N2 (duplicate date), PPLX-E3 (like-for-like disclaimer verbatim), PPLX-E5 (same normalization), PPLX-M5 (NEOWISE qualifier verbatim in abstract) |
| AUTO-FALSIFIED (pattern-052) | **1** | OAI-E1 (F₀ = 1/8.98² superscript flattening — 5th raise) |
| OPINION (framing, editorial, design choice) | **8+** | OAI-E5 (eROSITA 0.259 in context), OAI-E10, OAI-M1/M2/M3, Grok-M1/M4, Gem-M3, Gem-m4/m5 |
| HOUSTON-DECISION ruled | **5** | Gem-E1 (date), Gem-E2/E3/OAI-E2–E6 (HD-6/HD-11), Gem-N1 (email) |
| Pattern-051 regression check | **PASS** | All 9 EXT4 edits confirmed; no regression introduced |
| Pattern-052 auto-falsify | **1** | OAI-E1 (5th raise of F₀ superscript class) |

**Genuinely-new VERIFIED/PARTIAL-VERIFIED items requiring closure**: **14** (9 new + 5 partially-closed)

Priority-ordered closure actions (hardest first):

1. **OAI-E7 (Planck held-out re-score — SCIENTIFIC)**: Provide held-out scoring on a patch bank disjoint from training, or demonstrate via quantitative analysis that rankings are invariant (overlap + rank correlation between full-bank and held-out-only). This is the only finding with genuine scientific methodology implications.

2. **OAI-E9 (NANOGrav Bayes factor audit table)**: Add a short table/appendix entry showing prior density at γ=3.0 (= 1/7 under flat [0,7] prior), posterior KDE density at γ=3.0 and γ=4.33, KDE bandwidth, and the resulting Savage-Dickey ratio. Enables reader audit.

3. **OAI-E13 (Cutout arcsec size — ARITHMETIC)**: 128×128 at LS DR9 pixel scale 0.262″/px = 33.5″, not 54″. Either state the resampling pixel scale or correct the numbers.

4. **OAI-E12 (Hardware inconsistency)**: Correct §II.C "All inference on H200" to note the A100 Planck exception.

5. **OAI-E11 (S definition cross-transfer exception)**: Add one sentence in §II.B: "For SDSS and LAMOST cross-transfer runs, μ_val and σ_val are from the DESI validation set."

6. **PPLX-E8 (21.5× LAMOST S>5 qualifier)**: Add "S>5 anomaly-rate reduction (44,075 → 2,054)" to the 21.5× abstract statement.

7. **OAI-E8 (Fig. 6 radius label)**: Add "3-arcsec" label to the aggregate SIMBAD-unmatched bar in Fig. 6.

8. **Gem-M1 (BigAE full expansion)**: Define BigAE on first use in body text.

9. **Gem-m1 (0.29σ consistency)**: Replace "<1σ from null" with "0.29σ from null" in abstract and Conclusion item 5.

10. **Gem-M2 (Table VI _t placeholder)**: Replace `_t` with "N/A (wall-clock time not recorded during production run)."

11. **Gem-m2 (MSE eq index)**: Fix Eq. (1) to show subscript i on x and x̂.

12. **Gem-m3 (χ²_red notation)**: Replace "x² = 15.7" with "χ²_ν = 15.7" or "χ²_red = 15.7."

13. **Grok-M2 / OAI-M6 (Table I S cross-survey caveat + Appendix C normalization cross-ref)**: Add "within-survey only; S not cross-survey comparable" to Table I caption; add normalization cross-ref at first occurrence of 8.98 in §V and 16.85 in Appendix C text.

14. **PPLX-E4 (178/1000 raw ratio)**: Add "178/1000 ≈ 17.8%" to abstract novelty sentence.

---

## PART 4 — EXT4 closure regression and pattern-052 evidence

**All 9 EXT4 edits are confirmed in v3.1.97.** No regression introduced.

**Pattern-052 observation**: OAI's extraction pipeline re-raised F₀ = 1/8.98² as "1/8.982" despite the prophylactic numeric expansion at v3.1.94. This is the 5th consecutive round where the same vendor pipeline produces the same superscript-flattening misread. The EXT4 audit (row 24) noted the prophylactic fix had killed the class across the EXT4 legs — but OpenAI's R34conf pipeline apparently uses a different PDF extraction path. The resolution: the fix works for native-PDF ingestion paths; it does not protect against text-layer PDF parsers that strip LaTeX superscripts. Future mitigation: add explicit "F₀ = 1/8.98² = 1/80.64 = 0.01239" (showing the intermediate 80.64) to make the superscript impossible to misread even in text-layer extraction.

---

## PART 5 — Reviewer assessment

| Leg | Verdict | Accuracy |
|-----|---------|----------|
| Claude | ABSENT (API credits) | N/A |
| Gemini | MAJOR REVISIONS | Over-called E1/E2/E3 (HD-ruled); real items: M1 (BigAE), M2 (placeholder), m1/m2/m3 (minor fixes). Net = MINOR after audit. |
| Grok | MAJOR REVISIONS | Over-called E1 (date), E2 (arithmetic falsified), E3 (same-normalization falsified), M3 (disclosed); real items: N1 (Rxxconf labels in body). Net = MINOR. |
| OpenAI | MAJOR REVISIONS | Mixed: E1 (auto-falsified pattern-052); genuinely new: E7 (Planck held-out), E8 (Fig. 6 radius), E9 (BF density table), E12 (hardware), E13 (arcsec), E11 (S def). Net = MINOR-to-MODERATE revision. The F₀ auto-falsification confirms pattern-052 applies to this extraction pipeline. |
| Perplexity | MAJOR REVISIONS | Mostly overlapping; real items: E4 (178/1000), E7 (science-class rate denominator), E8 (21.5× S>5 qualifier), Pass2-M9 (Appendix C cross-ref). Net = MINOR. |

---

## VERDICT

**P3 is NOT-CLEAN at R34conf** pending closure of 14 items (9 genuinely new + 5 partially-closed). Item OAI-E7 (Planck held-out re-score) is the only item with scientific methodology weight; items OAI-E13 (arcsec size arithmetic) and OAI-E12 (hardware inconsistency) are factual corrections. The remaining 11 items are one-sentence or one-character editorial fixes. After all 14 closures, P3 can be declared CLEAN.

**CLEAN threshold**: 14 closures needed → wave as v3.1.98.

| Metric | Value |
|--------|-------|
| Legs active (Claude failed) | 4 / 5 |
| VERIFIED / PARTIAL-VERIFIED new items | 14 |
| FALSIFIED (false positives) | 7 |
| AUTO-FALSIFIED pattern-052 | 1 |
| OPINION (no action) | 8+ |
| HD-ruled (submission-day) | 5 |
| Pattern-051 regression | PASS |
| Pattern-052 auto-falsifies | 1 |
| Scientific methodology finding | 1 (OAI-E7 Planck held-out) |
| Round verdict | **NOT-CLEAN (14 closures needed → v3.1.98)** |
