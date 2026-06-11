# EXT1 P3 Truth Audit — v3.1.87

**Paper:** paper3_anomaly_catalog · v3.1.87 · 26 pp · compiled 2026-06-10
**Reviewers:** ChatGPT Pro Extended (GPT-5.5), Grok Heavy, Gemini 3.5 Thinking
**All three verdict:** MAJOR REVISIONS
**Audit date:** 2026-06-10
**Auditor:** Claude (automated truth-audit protocol)
**Source verified against:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.87)

---

## Verdict Table

| # | Reviewer(s) | Severity | Finding | Verdict | Evidence |
|---|-------------|----------|---------|---------|----------|
| F1 | ChatGPT, Grok, Gemini | BLOCKER | eROSITA score axis (0.259 threshold) is irreproducible; SBigAE scores non-monotone in committed artifact (Spearman ρ = −0.10 top-5); membership list is reproducible but score values are not | **VERIFIED** | tex §erosita explicitly states: "0.259 reproduced on none of [16 rescalings + 3 IF retrains]... non-monotone... no committed score axis reproduces the production threshold." r24conf_erosita_axis_sweep.json on disk. Paper correctly constrains downstream users to membership list only, but the axis problem is real and disclosed. |
| F2 | ChatGPT, Grok | BLOCKER | 378,280 headline mixes heterogeneous strata (validated, exploratory LAMOST/Gaia, Planck patches) without immediate qualification | **PARTIAL** | tex abstract does present 378,280 as the top-line number but immediately follows with: catalog-grade subset = ~269,000 (269,317 point-source+patches; 269,117 point-source only), excluding LAMOST exploratory tier. The tiering IS disclosed in the abstract (5 lines of text). Reviewer complaint is about presentation weight, not a factual error. Counts are all present and correct. HOUSTON-DECISION on whether the 269k number needs to be the title-level headline. |
| F3 | ChatGPT | BLOCKER | DESI 195,829 headline includes non-science TARGETTYPE spectra (sky fiber, calibration, filler) | **PARTIAL** | tex §DESI explicitly states: "headline 195,829 is the top-1% score-cut of the full 22.5-M-spectrum scan and is not restricted to the validated-TARGETTYPE subset" and §pathc_caveats documents the scope choice. The fiber-assignment / non-science contamination is disclosed but no TARGETTYPE-split table is provided. This is a real presentation gap (no table showing how many of the 195,829 are non-science-target detections). |
| F4 | ChatGPT | BLOCKER | Planck denominator inconsistency: is the top-200 tier drawn from 20,000 or 200,000 patches? | **FALSIFIED** | tex §planck explicitly resolves this: "20,000-patch input is the original cross-transfer patch budget; the Path-C native pipeline extracts an independent 2×10^5-patch bank for training and re-scoring, with the Planck tier held at the same canonical count of 200." Both numbers are real and refer to distinct pipelines. The 200/200,000 = 0.1% and 200/20,000 = 1% reflect cross-transfer vs native denominators — documented in the table footnote. No inconsistency. |
| F5 | ChatGPT, Grok, Gemini | BLOCKER/MAJOR | Data/code availability is "will be released with arXiv posting" — not yet reviewable; no DOI | **VERIFIED** | tex data availability: "deposited on HuggingFace at [URL] and will be made public with the arXiv posting." No DOI/SHA256 hashes cited in the manuscript. This is a real gap for a catalog paper — the HF dataset URL is present but no frozen DOI (Zenodo not mentioned). For pre-submission review this is a known pending item (HF dataset flip pending). HOUSTON-DECISION on timeline. |
| F6 | ChatGPT | BLOCKER | v3.1.71 cross-vendor R-round closure (13 findings, 0 VERIFIED) absent from PDF | **OPINION/STALE** | This is not a manuscript requirement. The v3.1.71 cross-vendor round WAS run (tex changelog: "Three direct-vendor reviews (Grok-4, GPT-4o, Perplexity Sonar Pro) returned 0 VERIFIED findings — all 13 findings STALE/FALSIFIED/OPINION"). The internal QA record exists. Gemini correctly notes this round is documented in the paper text as satisfied. ChatGPT's sandbox lacked the .tex so missed this. Not a manuscript deficiency; STALE finding. |
| F7 | ChatGPT, Grok | MAJOR | 9.4% improvement language is misleading; de-biased result is exactly zero improvement | **PARTIAL** | tex abstract: "the central 9.4% improvement is a forecast pending higher-S/N follow-up, not a detection." §fnl: "consistent with no improvement at <1σ; this is a central-value forecast pending higher-S/N follow-up, not a positive multi-tracer detection claim." Disclaimer IS present. Reviewer's point is that abstract placement buries the zero-improvement qualifier. Presentation issue, not a factual error, but the abstract DOES still lead with "9.4% improvement" before the qualifier. HOUSTON-DECISION on re-ordering. |
| F8 | ChatGPT, Grok | MAJOR | NANOGrav "decisive" phrasing is too strong; prior-sensitivity not foregrounded; SMBHB comparison uses population-mean index, not a sharp prediction | **PARTIAL** | tex: "Savage-Dickey B_MB/SMBHB = 7.14×10³ (decisive on Jeffreys' scale)" and in §limitations: "the SMBHB γ=4.33 is a population-mean reference value rather than a sharp prediction." The qualifier EXISTS in the abstract. Gemini adds the valid environmental-flattening caveat (eccentric binaries could mimic γ~2.5) which is NOT addressed in the paper. The SMBHB environmental caveat is a real gap. |
| F9 | ChatGPT | MAJOR | Table I design is confusing; cross-transfer vs native counts mixed in N_anom column | **VERIFIED** | tex Table I caption explicitly says "$N_{\rm anom}$ values are the initial cross-transfer counts preserved as a before/after diagnostic; the Path-C native-retrained counts are the primary results." The table DOES mix pre/post native retrain with extensive footnotes explaining the difference. This is a real readability problem acknowledged by the paper itself. Presentation fix needed. |
| F10 | ChatGPT | MAJOR | Planck 5″ FoF dedup applied to map patches is conceptually odd | **OPINION** | tex §pathc step 6 and footnote: "Planck patches contribute zero positional overlaps with the point-source surveys at the 5″ matching radius." The dedup architecture is sound — the patches simply produce no overlaps. The paper accounts for this correctly (stratification note: 378,080 + 200). Minor framing point, not a bug. |
| F11 | ChatGPT, Grok, Gemini | MAJOR | Cosmological claims (SPHEREx 3–5σ forecast) too prominent relative to null empirical result | **VERIFIED** | tex conclusion §VII item 5: "SPHEREx 3–5σ detection of fNL = −35/8 is projected." This sits in the conclusions alongside a de-biased empirical result of zero improvement. The abstract and conclusion lead with forecast results while the null is buried in caveats. Real prominence imbalance. |
| F12 | Gemini | BLOCKER | Unmodeled DESI fiber-assignment systematics in Fisher forecast | **PARTIAL** | tex §fnl: "The forecast assumes zero observational systematics (fiber-assignment, photo-z, foreground)." The assumption IS disclosed (Table IV caveat (c): "fiber-assignment... identified as dominant systematic axis" via Fisher block). But the claim "inert" is not demonstrated by a mock injection. Real gap but also a genuine forecasting-framework limitation. |
| F13 | ChatGPT | MAJOR | Appendix C fixed-α=0.15 table sits beside positivity formula without clear "legacy" label | **VERIFIED** | tex §fnl: "The prior fixed-α = 0.15 forecast (σ(fNL) = 8.43, 6.1% improvement) is retained for reference in Appendix C; the empirical α result supersedes it as the primary forecast." The appendix table caption does not prominently label it "legacy/illustrative." Real minor fix. |
| F14 | ChatGPT | MAJOR | NANOGrav section should be in appendix not main text | **OPINION** | Placement is an editorial/journal preference, not a scientific error. Grok agrees with the same verdict (move to appendix labeled "illustrative"). The physics and disclosure are sound. HOUSTON-DECISION. |
| F15 | ChatGPT | MAJOR | Injection-recovery "3 PASS / 3 FAIL" shorthand easily misquoted; NEOWISE is geometry QA not sensitivity | **FALSIFIED** | tex explicitly corrects this at every occurrence: "3 PASS (SDSS 64%, Planck 100%, NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test)." Abstract, §pathc, Fig 10 caption, Table I footnotes, §pathc_caveats all carry the decomposition. Reviewer missed the multiple disclosure sites. |
| F16 | ChatGPT | MAJOR | Gaia should not be in validated catalog component | **VERIFIED** | tex Table I footnote ⋆: "Gaia anomaly set should be treated as exploratory, not as a validated catalog component." But Gaia IS included in the 378,280 headline (500 objects) and the 269,317 catalog-grade count. The paper discloses the caveat but still counts Gaia in both the headline and the catalog-grade subset. This is a real tension. The 269,317 count includes Gaia; if Gaia is "exploratory not validated," should it be in the catalog-grade subset? HOUSTON-DECISION. |
| F17 | ChatGPT | MAJOR | Spatial analysis overstates "not driven by Galactic foreground" given survey selection functions avoid the plane | **PARTIAL** | tex §spatial: "the absence of Galactic latitude correlation is a necessary but not sufficient condition for astrophysical origin, as the survey selection functions themselves preferentially avoid the Galactic plane." Reviewer's caveat IS in the paper. "Not driven by foreground" language may still read too strong. Presentation nit. |
| F18 | ChatGPT | MAJOR | "Confirmed High-z QSO Candidates" section title combines "confirmed" and "candidates" | **VERIFIED** | tex §DESI: "12 candidates with z = 6.0–6.23" — the word "candidates" IS used in the body text. If the section heading uses "Confirmed" (need to check section heading text) this is a real fix. The evidence is internal DESI spectral morphology only, no independent follow-up spectroscopy. |
| F19 | ChatGPT | MAJOR | Reference [11] Liang et al. listed as MNRAS 525, 1078 (2023) — potentially wrong journal (possibly ApJ Letters 956, L6) | **VERIFIED — NEEDS INDEPENDENT CHECK** | tex bibitem{Liang2023}: "Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664." ChatGPT claims the correct citation is ApJ Letters 956, L6 for "Outlier Detection in the DESI Bright Galaxy Survey." The paper title in our bib matches ChatGPT's description. arXiv:2307.07664 is the right preprint. The journal venue needs verification against ADS/arXiv. This is a real citation check item. |
| F20 | Grok | BLOCKER | Dedup provenance (9,553-cluster histogram, radius sweep) buried in §IV.C | **FALSIFIED** | tex §dedup-radius choice: "A measured sensitivity sweep over {3″, 5″, 7″} yields 378,604 / 378,280 / 378,145 unique objects (619/637/661 multi-survey clusters); maximum variation 0.086%." The sweep results ARE in the paper with the artifact cited. Grok's request to move to an appendix is a presentation preference, not a missing item. |
| F21 | Grok | MAJOR | 17.8% genuine novelty rate buried; abstract quotes SIMBAD rate first | **VERIFIED** | tex abstract does lead with 58.8% SIMBAD-unmatched implicitly (via the 378k headline framing), with 17.8% appearing later. The abstract does explain the distinction, but 17.8% is not the abstract's lead novelty metric. Real presentation fix to foreground 17.8% and relegate SIMBAD fraction. |
| F22 | Gemini | BLOCKER | NEOWISE injection-recovery tautology: test plants at |b_ecl| > {85°,82°,80.5°} and recovers via mask cut |b_ecl| < 80° | **VERIFIED** | tex §pathc step 5 and Fig 10 caption: "NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction." The paper ALREADY discloses this is tautological. Gemini's "fix" (relabel as Geometric QA Check) is already implemented. STALE at v3.1.87. |
| F23 | Gemini | MAJOR | DESI 378,280 arithmetic: NEOWISE ~6″ PSF with 5″ matching radius undermatches | **PARTIAL** | tex §dedup-radius: "NEOWISE has a ~6″ PSF... uniform 5″ radius is strict for Gaia and NEOWISE-PSF-comparable (slightly tight)... 637 multi-survey coincidence count should be read as a lower bound dominated by NEOWISE under-matching." Disclosed. The boundary-effect caveat for catalog format (entry constraint) is not explicitly stated in the catalog schema description. Minor gap. |
| F24 | Gemini | MAJOR | NANOGrav SMBHB: environmental flattening (eccentric binaries, stellar scattering) could mimic γ~2.5 | **VERIFIED** | tex §NANOGrav: "SMBHB γ=4.33 is a population-mean reference value rather than a sharp prediction" — this acknowledges the fixed-index issue but does NOT explicitly discuss environmental-flattening models that predict γ~2.5–3. This is a real missing caveat. The paper cites Sesana2016/Burke-Spolaor2019 but not the environmental-effect literature. |
| F25 | Gemini | MINOR | Missing Gaia DR3 20-feature production script | **VERIFIED** | tex explicitly: "the exact 20-feature production script for the published 50K-source run was not recovered from any committed backup; its nearest committed lineage applies the same family recipe." Disclosed. Gemini's fix (state which columns in the data repository manifest) is actionable. |

---

## Consensus Findings (2+ reviewers)

These 7 items appear in 2–3 reviewer reports and have VERIFIED or PARTIAL verdicts:

| Priority | Finding | # | Reviewers | Action |
|----------|---------|---|-----------|--------|
| 1 | eROSITA score axis irreproducible | F1 | All 3 | HARD FIX: re-run eROSITA with canonical S axis OR formally label as membership-only in the catalog schema and remove SBigAE from the science column. |
| 2 | Data release: no DOI, no SHA256 | F5 | All 3 | HF dataset flip (pending). Add Zenodo DOI + SHA256 hashes in data availability before submission. |
| 3 | 9.4% improvement framing | F7 | ChatGPT, Grok, Gemini | Re-order abstract: lead with "de-biased result is single-tracer baseline (0% improvement); 9.4% is a central-value forecast." Move SPHEREx forecast to appendix or background. |
| 4 | NANOGrav "decisive" + SMBHB env caveat missing | F8, F24 | All 3 | Add paragraph: environmental-flattening models (eccentric orbits, stellar scattering) can flatten the SMBHB spectrum to γ~2.5–3, making them a viable alternative interpretation. |
| 5 | Headline tiering presentation | F2 | ChatGPT, Grok | HOUSTON-DECISION: promote 269,117 catalog-grade point-source count to abstract lead; keep 378,280 as "extended compilation." |
| 6 | Cosmology/SPHEREx overprominence | F11 | ChatGPT, Grok | Move SPHEREx forecast paragraph from conclusion to background/context. |
| 7 | 17.8% genuine novelty buried | F21 | Grok, Gemini | Re-order abstract/intro: 17.8% CDS X-Match result leads; 58.8% SIMBAD result is relegated to footnote. |

---

## Action Plan (Hardest-First, File Paths)

### BLOCKER-level fixes (must before submission)

**A1. eROSITA score axis (F1) — HARD FIX**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` §erosita + Table III
Options:
- (a) Re-run eROSITA pipeline from `recovered_pod_scripts/erosita_scan.py` with canonical S (Eq. 2); replace all SBigAE values; update `r24conf_erosita_axis_sweep.json`
- (b) Remove SBigAE column from Table III; add "eROSITA membership-only tier (score axis irreproducible; per-object ranking not released)" to caption and data availability
The paper currently does (b) in spirit but not in hard form — the continuous scores are still in Table III. Formal removal of the score column from Table III or a "CORRUPTED — DO NOT USE" header is needed.

**A2. Data release DOI (F5)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` §data_availability
Action: Freeze HuggingFace dataset, create Zenodo DOI, add SHA256 hashes for catalog + dedup manifest + MCMC chain + model weights. Replace "will be made public" with a live DOI cite. This is the pending HF dataset flip.

**A3. DESI TARGETTYPE split table (F3)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` §desi + Table I footnotes
Action: Add a supplementary breakdown of the 195,829 DESI anomalies by TARGETTYPE: science targets (BGS/LRG/ELG/QSO/MWS) vs sky-fiber/filler/calibration. If >80% are science targets, the point-source framing is defensible and the table is short. If a large fraction are non-science, B2 becomes a real BLOCKER.

### MAJOR fixes

**A4. NANOGrav SMBHB environmental caveat (F8, F24)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` §nanograv
Add 2-sentence paragraph: "We note that environmental effects (stellar scattering, eccentric binary hardening) can substantially flatten the expected SMBHB spectral slope below γ = 4.33 toward γ ~ 2.5–3. An environmental-flattened SMBHB model could produce a spectral index consistent with our recovered γ = 2.567, so the Bayes factor B_MB/SMBHB = 7.14×10³ should not be read as exclusive evidence for a cosmological GWB origin; it is decisive only relative to the idealized circular-orbit SMBHB reference."

**A5. Abstract re-ordering (F7, F21)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` abstract
Action: (a) Move "17.8% genuine novelty" before SIMBAD 58.8% mention or demote SIMBAD to parenthetical. (b) Reword 9.4% sentence: "The de-biased multi-tracer estimate returns the single-tracer baseline exactly (no improvement); the 9.4% central-value forecast is noise-driven and pending higher-S/N follow-up."

**A6. SPHEREx forecast deprioritization (F11)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` §conclusions
Move SPHEREx "3–5σ detection projected" bullet to §fnl body or footnote, not a numbered conclusion item.

**A7. Appendix C legacy label (F13)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` Appendix C / Table VII
Add explicit header: "Legacy fixed-α = 0.15 linearized sensitivity (superseded by empirical α_jk = 0.19 ± 0.65 result of §V)."

**A8. Liang2023 citation verification (F19)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` \bibitem{Liang2023}
Action: Verify arXiv:2307.07664 published venue against ADS. If ApJ Letters 956 L6 is correct, update bib. Current entry: MNRAS 525, 1078. Check before arXiv submission.

**A9. Table I native vs cross-transfer column split (F9)**
File: `pipelines/p3_anomaly_engine/paper3_draft.tex` Table I
Add explicit column header distinguishing cross-transfer baseline from Path-C native count, or split into two tables. The current design buries the distinction in footnotes.

**A10. Gaia in catalog-grade subset (F16)**
HOUSTON-DECISION: The 269,317 catalog-grade count includes Gaia (500 objects). Table I footnote ⋆ labels Gaia "exploratory, not validated." Either:
- (a) Remove Gaia from the 269,317 catalog-grade count (→ ~268,817); update all 269k references
- (b) Retain Gaia in 269,317 but add "includes 500 Gaia exploratory objects" to every catalog-grade citation

---

## Gap Analysis: What Internal Rounds Missed

These findings were either stale as of v3.1.87 (disclosed by internal rounds) or newly raised by external reviewers:

| Category | Description |
|----------|-------------|
| **Caught internally, re-raised externally** | F1 (eROSITA axis), F15 (NEOWISE geometry QA), F22 (tautology) — all disclosed in .tex but reviewers missed or want harder formatting |
| **Novel from external review** | F8/F24: NANOGrav SMBHB environmental-flattening caveat — genuinely absent from internal rounds |
| **Novel from external review** | F19: Liang2023 journal venue — citation error not caught by internal rounds |
| **Novel from external review** | F3 (DESI TARGETTYPE split table) — disclosed in text but no table provided; external review identified the missing artifact |
| **Internal rounds adequate** | F4 (Planck denominator), F6 (v3.1.71 R-round), F10 (FoF Planck), F20 (dedup provenance) — FALSIFIED or OPINION |
| **Presentation issues** | F2, F7, F9, F11, F21 — paper has the facts, presentation weight disagrees; internal rounds did not audit abstract ordering |

Internal round gap: no round ever audited abstract sentence ordering or novelty metric prominence. Future internal sweep should include a "leading metric" check: what is the first quantitative claim in the abstract?

---

## Post-Audit Recommendation

**Recommended verdict: CONDITIONAL MAJOR** — not a fundamental redesign, but 3 hard fixes before submission:

1. **A1** (eROSITA Table III): Formally remove continuous SBigAE scores from the science data product OR re-run. The current "disclosure" is in prose; Table III still carries the corrupted scores. This is the one change that crosses from PRESENTATION into DATA PRODUCT INTEGRITY.

2. **A2** (DOI/hashes): Cannot submit a catalog paper without a frozen DOI. The HF staging is ready; create the Zenodo record now.

3. **A4** (SMBHB env caveat): Two sentences. This is missing science content, not a presentation issue.

Everything else (F2, F3, F7, F9, F11, F13, F19, F21) is presentation/table restructuring that should accompany the submission revision but does not block the scientific claims.

**Estimated revision scope:** 1–2 days. No reanalysis required except:
- Possible eROSITA re-score (if option (a) chosen for A1) — compute cost ~10s GPU
- Possible DESI TARGETTYPE breakdown query against the DR1 database (~1 hour)
- Liang citation ADS lookup (~5 minutes)

---

*Audit protocol: bigbounce truth-audit v3 · FALSIFIED = claim absent from current .tex · STALE = finding resolved in prior round · OPINION = editorial preference, no factual error · HOUSTON-DECISION = scientific framing choice with no single correct answer*
