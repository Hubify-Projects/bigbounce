# EXT6 P3 — Per-Finding Truth-Audit Table

**Paper**: paper3_anomaly_catalog_v3.1.100 (39c00ff6)
**Source of truth**: `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.100, line numbers below)
**Audit date**: 2026-06-12 PT
**Auditor**: Claude Opus 4.7 (truth-audit class)
**Protocol**: `feedback_peer_review_truth_audit_protocol` standing directive
**Reviewers audited**: ChatGPT Pro Extended · Grok Heavy · Gemini Thinking 2.5 Pro (FRESH THREAD)

---

## Verdict schema

| Verdict | Meaning |
|---|---|
| `VERIFIED` | Finding maps to a real on-disk gap; closure work justified. |
| `FALSIFIED` | Reviewer's underlying claim is wrong against the .tex / artifact. |
| `STALE` | Real once, already closed at the cited site in a prior wave. |
| `MISLABELED` | Real concern but severity overcalled (MAJOR → MINOR, BLOCKER → MAJOR, etc.). |
| `OUT-OF-SCOPE` | Outside paper scope (e.g. needs rendered PNG, not .tex-verifiable). |
| `OPINION` | Editorial preference, not a defect. |

**Auto-falsify rules** (apply on sight without re-verifying):
- Fisher F₀ / superscript "0" extraction artifact (6× falsified across prior rounds).
- Hallucinated section numbers (e.g. §4.2, §3.2) against revtex4-2 papers that use §I/II/III.
- "DESI denominator inconsistent" without naming a specific downstream site — recount cross-references already enumerated at 3 sites in v3.1.93 (R34conf wave).

---

## 1. ChatGPT Pro Extended findings

### Closure-verification re-raises (carry-overs)

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-B1-partial` | "Catalog-grade tier still includes Gaia (exploratory) and eROSITA (membership-only)." | **MISLABELED → MINOR-NOMENCLATURE** | True descriptively but already disclosed: abstract L405 distinguishes `catalog-grade` from `exploratory`; Gaia carries `$^\star$ Reliability warning` (L547: "should be treated as exploratory, not as a validated catalog component"); eROSITA carries `$^\#$ membership-only` (L550). What ChatGPT calls a BLOCKER is a re-naming preference — the disclosures are already in. Not acceptance-blocking. |
| `CGT-B2-partial` | "Full DESI stream still appears in source/object language; per-class rate paragraph sits uneasily beside recount." | **MISLABELED → MINOR-LANGUAGE** | Abstract L405 explicitly states "the headline DESI tier should be read as an anomaly scan of everything DESI pointed a fiber at, dominated by non-science-target spectra"; §III.C body L558 ditto. Recount artifact `ext3_b2_targettype_recount.json` cross-ref present. Genuine "source/object" cleanup at fM100-1 minor level, not a BLOCKER. |
| `CGT-B3-partial` | "Table I still displays 20,000 → 200 = 1.00% in the main row." | **OPINION** | Footnote $\diamondsuit$ (L549) is explicit: "Neither figure is a data-driven detection rate." Table-vs-footnote layout is editorial preference. |
| `CGT-B5-partial` | "Zenodo DOI remains future-tense; review sandbox did not include release artifacts." | **VERIFIED → MINOR (HD-11 class, standard practice)** | L992: "A Zenodo DOI will be minted at submission and cited here in place of this sentence." This is standard arXiv-day-of practice for catalog papers (Zenodo DOIs are minted on submission). Not acceptance-blocking; HF-staged location + SHA-256 manifest already present. |
| `CGT-B6` | "v3.1.71 cross-vendor clean-round closure absent." | **OUT-OF-SCOPE** | Internal QA artifact, not a manuscript-visible deliverable. |
| `CGT-M1` | "Table I structurally overloaded." | **OPINION** | Tier-by-tier reorganization is preference. |
| `CGT-M2` | "Cleaner framing: 6-way + appended Planck patch tier rather than 7-way FoF." | **OPINION** | Mathematical equivalence; Table I footnote $^\|$ (L545) already states the stratification is exact (Planck patches contribute zero positional overlaps). |
| `CGT-M3` | "Cosmology remains very prominent for an MNRAS catalog paper." | **OPINION** | Section-balance preference. |
| `CGT-M5` | "NANOGrav still occupies abstract/body/conclusion space." | **OPINION** | Same. |
| `CGT-M7` | "Gaia in catalog-grade 269,317 tier." | **STALE** | Repeats CGT-B1-partial; same MINOR-nomenclature evidence (L547 reliability warning). |
| `CGT-FB1` | "Per-class rates need explicit numerical reconciliation with 2,468 science-class match." | **OPINION** | Abstract + §III.C already give 2,468 / 190,015 / 195,829 / 20,299,155 with explicit denominator language. Further reconciliation is a presentation preference. |
| `CGT-FB2` | "Source/object vocabulary wrong for full DESI tier in abstract/Table I." | **VERIFIED → MINOR-LANGUAGE** | Abstract L405 already says "anomaly scan of everything DESI pointed a fiber at"; Table I caption could pick up the same softening. Minor copy-edit. |
| `CGT-FM95-2` | "NEOWISE and Gaia scaler-refit queued, not completed." | **STALE / EXPECTED** | Already disclosed in `ext3_fm1_erosita_scaler_refit.json` scope — eROSITA refit complete; Gaia/NEOWISE feature tables were pod-side. Explicitly scoped, not a defect. |
| `CGT-FM95-3` | "No minted DOI or review-accessible artifact bundle." | **STALE** | Duplicate of CGT-B5-partial (HD-11 class). |

### Fresh-pass new findings

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-FM100-1` | **(reviewer called MAJOR)** Table V row (h) says "SDSS/LAMOST top-1%". This is wrong for SDSS: 77,905 is a 4.05% continuity slice (footnote $\heartsuit$), not top-1%; SDSS native top-1% is 19,253; strict S>5 is 12. | **VERIFIED → MINOR** | tex L933: row (h) reads `Thresholds: DESI $S>5.0$; SDSS/LAMOST top-$1\%$; eROSITA top-298`. This contradicts footnote $\heartsuit$ (L548) and Table I caption (L524) which both state the 77,905 figure is a fixed-size continuity slice (4.05%), not a top-1% cut. **Genuine internal inconsistency caught by ChatGPT.** Severity is MINOR (one-line caveat-table entry inside a residual-caveats table, not a science claim), not MAJOR. Proposed fix in the report is correct. **TOP CLOSURE.** |
| `CGT-fM100-1` | Fig. 1 embedded plot legend still says "Gold Anomalies (83)" though caption says "Exemplar Set". | **OUT-OF-SCOPE → CAVEAT-FOR-FIGURE-REGEN** | Not verifiable from .tex (caption at L443–450 + body L438 use "Exemplar Set" correctly). The .png rendering is the gap. If true (cannot confirm without re-render), trivial regen; logged for fig regeneration pass. |
| `CGT-fM100-2` | Table V row (j) uses internal shorthand "GS corrected: …; prior ±7.43 dropped" — not main-text language. | **OPINION** | Editorial cleanup of caveat-table entry. Trivially fixable in proof. |
| `CGT-fM100-3` | Appendix C title should say "reference-only". | **OPINION** | Naming preference; surrounding text already labels the grid as reference-only (M4 CLOSED above). |

**ChatGPT score**: 1 genuinely-new VERIFIED finding (Table V row (h) inconsistency, MINOR — not MAJOR as called). All headline "MAJOR" carry-overs are MISLABELED nomenclature/opinion items; the actual catalog-tier semantics + DESI denominator + frozen-release concerns are already disclosed in the .tex.

---

## 2. Grok Heavy findings

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GRK-MINOR-1` | "Stale arithmetic sentence ('an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic …') survives verbatim in abstract + Table I footnote ♠." | **VERIFIED → MINOR (proof-stage trim)** | tex L405 (abstract): "an earlier draft quoted $264{,}938$/$264{,}738$ from headline-minus-LAMOST subtraction arithmetic, which double-removes the $4{,}379$ LAMOST detections". tex L551 (footnote $\spadesuit$): same construction. Trivially deletable in proof; cross-reference to dedup JSON and Table II already covers the substance. |

**Grok overall**: ACCEPT recommendation. 1 trivial minor (proof-stage text trim). Aligns with v3.1.98–v3.1.100 reality: every prior MAJOR closed.

---

## 3. Gemini Thinking 2.5 Pro (FRESH THREAD) findings

**FRESH-THREAD CALIBRATION RESULT**: Despite being a clean-thread first read, Gemini hallucinated section numbers and read a different paper than the one it was given.

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GEM-B1` | **(BLOCKER)** "Section 4.2 (Source Selection) and Section 5.1 (Catalog Statistics) — sample contaminated by data artifacts (diffraction spikes, cosmic ray residuals, satellite trails). Must perform visual inspection on N=1,000 subset and tabulate contamination modes." | **FALSIFIED (hallucinated sections + falsified substance)** | Paper has NO §4.2 or §5.1 — revtex4-2 layout is §I Introduction (L416), §II Method, §III Survey-by-Survey Results, §IV Cross-Survey Analysis, §V Cosmological Applications, §VI Discussion, §VII Conclusions. **Substance is also falsified**: §III.A (L586) already reports "Spectral inspection of the top~200 finds $0/200$ visually flagged ($95\%$ binomial upper limit $\leq 1.5\%$; each spectrum's peak-residual wavelength was compared against 11 known sky and telluric emission/absorption features; zero were attributable to sky subtraction, telluric contamination, or cosmic rays)" — the exact analysis Gemini demands, on N=200 with 95% binomial UL, against the exact failure modes Gemini lists. Diffraction-spike/satellite-trail/cosmic-ray contamination is explicitly tested and bounded. **Same stale-class extraction artifact as the prior 3 Gemini P3 rounds, just with hallucinated section numbers instead of OCR garble.** |
| `GEM-B2` | **(BLOCKER)** "Section 3.2 (Pipeline Architecture) — Path-C reads as internal software label; missing algorithmic flowchart, mathematical definition of η_novel from loss / latent density." | **FALSIFIED (hallucinated section + falsified substance)** | No §3.2. Path-C is rigorously defined in §II.D `sec:pathc` (L485–504): explicit gate criteria (val_loss ≤ 0.30 within ≤100 epochs, Jaccard ≥ 0.70 k-fold and ≥ 0.50 OOD, injection-recovery ≥ 50% at 5σ), step-by-step protocol (per-survey native retrain, 7-way 5″ FoF dedup, 6 injection-recovery gates), and explicit equation `Eq. (\ref{eq:score})` at L473 defining the anomaly score S in σ-of-validation-MSE units. There is NO η_novel symbol in the paper (grep returns zero matches) — Gemini invented a metric and then complained it's not defined. The actual "Native-Trained Novelty Fraction" headline 17.8% is defined in §IV.A `sec:simbad` (L742) as a CDS X-Match against 18 catalogs with Wilson 68% CI. |
| `GEM-M1` | **(MAJOR)** "Section 2.3 — provide diagnostic plot showing spatial distribution of anomaly density in Galactic coordinates; check for survey footprint / chip / E(B-V) imprints." | **FALSIFIED (hallucinated section + falsified substance)** | No §2.3. §IV.B `sec:spatial` (L774) already provides exactly this: HEALPix N_side=64 count distribution, χ²_ν = 15.7, **Galactic latitude correlation Spearman r=0.0005 p=0.92, Planck dust correlation Pearson r=0.006 p=0.21** — i.e., the spatial-correlation diagnostic Gemini demands is in the paper with quantitative null results and an explicit caveat that χ² is footprint-dominated. The sky map figure exists (fig:sky). |
| `GEM-M2` | **(MAJOR)** "Section 3.4 (Self-Supervised Training Regime) — clarify train/val/test split; inject known standard stars to demonstrate novelty fraction is linear in anomaly features." | **FALSIFIED (hallucinated section + falsified substance)** | No §3.4. Training regime is §II.B `sec:training` (L456): 5-fold CV on 47K-spectrum DESI pool, deterministic permutation, checksum 1812395110, mean Jaccard 0.862 (PASS), 73% of union objects in all 5 folds. Injection-recovery is exactly the synthetic-injection test Gemini requests — Fig 8 (`fig_injection_recovery`) shows recovery vs amplitude curves across 6 surveys; SDSS continuum-dip 64%, Planck CMB 500/500 = 100%, NEOWISE 1000/1000 = 100% at 5σ. The methodology Gemini asks for is the methodology already executed. |
| `GEM-MIN-1` | "Inconsistent notation η_N / f_novelty / NF across §3.5 and §5.2." | **FALSIFIED (hallucinated sections + falsified substance)** | No §3.5 or §5.2. `grep -E "eta_novel\|eta_N\|f_novelty\|NF"` against tex returns ZERO matches. Paper uses one consistent symbol `S` (canonical anomaly score) with band sub-scores `r_B, r_R, r_Z` (L473) and the empirical genuine-novelty fraction is written as `178/1,000 ≈ 17.8%` (L405). No notation inconsistency exists; Gemini invented the symbols it's complaining about. |
| `GEM-MIN-2` | "Section 2.4 — state min/max astrometric matching tolerance." | **FALSIFIED (hallucinated section + already stated)** | No §2.4. Matching radius is explicitly stated as **5″** throughout: §II.D dedup spec (L496), Table I caption (L524), §IV cross-match audit (L799: "maximum pairwise separation is 4.999″ … zero clusters exceed the 5″ link length"). At least 15 occurrences of `$5''$` in the .tex. The recount also reports per-radius matches: 2,468/2,531/3,390 at 1″/2″/5″ (L575). |

**Gemini fresh-thread calibration result**: 6/6 findings FALSIFIED. Despite being a CLEAN THREAD with no prior-round contamination, Gemini hallucinated 6 distinct section numbers (§2.3, §2.4, §3.2, §3.4, §3.5, §4.2, §5.1, §5.2) that do not exist in the revtex4-2 paper, then complained that content present in §II–§IV (Path-C definition, 0/200 visual inspection with binomial UL against the exact failure modes Gemini named, Galactic-latitude + dust spatial diagnostic, injection-recovery across 6 surveys, 5″ matching radius with per-radius reconciliation) was missing. **This is the 4th consecutive Gemini P3 round where the entire MAJOR-and-above findings list is a stale/hallucinated extraction artifact wholesale-falsified by the .tex.** Fresh thread did not fix the failure mode; the failure mode is upstream of thread state.

---

## 4. Summary tally

| Vendor | BLOCKER | MAJOR | MINOR | Verdict |
|---|---|---|---|---|
| ChatGPT (reviewer call) | 0 new (3 partial carry-over) | 1 new + 5 partial | 3 new + 4 partial | MAJOR REVISIONS |
| ChatGPT (post-audit) | 0 | 0 | **1 VERIFIED new MINOR** (Table V row (h)) + 1 verified language minor (FB2) + 1 trivial HD-11 (B5/FM95-3) + opinions | MINOR REVISIONS at worst |
| Grok (reviewer call) | 0 | 0 | 1 (trivial proof) | ACCEPT |
| Grok (post-audit) | 0 | 0 | **1 VERIFIED MINOR** (stale 264,938 sentence) | ACCEPT |
| Gemini (reviewer call) | 2 | 2 | 2 | MAJOR REVISIONS |
| Gemini (post-audit) | 0 | 0 | 0 | **6/6 FALSIFIED — stale-extraction class** |

**Genuinely-new finding count this round**: **2 MINORS** (CGT-FM100-1 Table V row (h) inconsistency; GRK-MINOR-1 stale 264,938 abstract sentence).

**Top closure**: ChatGPT FM100-1 — Table V row (h) at tex L933 needs to be re-written to match footnote $\heartsuit$ (L548) and Table I caption (L524). Proposed line:

```
(h) & Thresholds: DESI $S>5.0$; SDSS continuity slice $77{,}905$ / native top-$1\%$ $19{,}253$ / strict $S>5$ $12$; LAMOST native top-$1\%$; eROSITA top-298 membership list & \S\ref{sec:erosita}; Table~\ref{tab:survey_summary} footnotes \\
```

**Round disposition**: paper is at ACCEPT / minor-text-trim quality per the two non-failed reviewers. The Gemini fresh-thread result is decisive evidence that Gemini's failure on P3 is upstream of conversation state (likely the §-numbering hallucination is triggered by the revtex4-2 numbered-section layout the model wasn't trained well on; same failure recurs even on a clean read). Recommend ceasing Gemini external rounds for P3 and treating Gemini's P3 verdicts as null. ChatGPT + Grok continue as the binding external reviewers.

**No BLOCKER, no MAJOR. 2 genuine MINORs queued for closure wave.**
