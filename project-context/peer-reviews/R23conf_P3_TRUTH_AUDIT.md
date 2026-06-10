# R23conf P3 — TRUTH AUDIT (META-REVIEW + remaining SYNTHESIS findings)

**Auditor**: Claude (in-session), 2026-06-09, against `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.80 working tree)
**Scope**: every P3-META-* finding + all SYNTHESIS findings not already closed in the R23conf_P3_Claude_brutal_INSESSION wave (E1, M1–M4, m1–m6, N1–N2 = CLOSED-PRIOR; Claude_brutal duplicates of those = CLOSED-PRIOR).
**New artifacts this wave**: `pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.{py,json}` (chain audit, SDSS-threshold dedup variants, DESI×SDSS 3″ shifted-control coincidence).

Verdicts: VERIFIED (real, fixed) / PARTIAL / OPINION / STALE (already addressed in current source) / FALSIFIED / HOUSTON-DECISION / QUEUED (recompute requires non-local data or pod; see R23CONF_COMPUTE_QUEUE.md).

## META-REVIEW findings

| ID | Sev | Claim | Verdict | Disposition |
|----|-----|-------|---------|-------------|
| META-E1 | ESS | α² squaring noise bias makes σ(fNL)=8.14 central forecast optimistic | **VERIFIED** | Closed: de-bias sentence added §V.b — E[α̂²]=α²+Var(α̂); max(0, 0.19²−0.65²)=0 ⇒ de-biased central = baseline 8.98 (no improvement); envelope [3.92, 8.98] declared the appropriate summary (tex ~L548). Pure arithmetic on in-paper numbers. |
| META-M1 | MAJ | FoF union-find can chain-merge >5″ pairs; no audit shown | **VERIFIED→CLOSED by recompute** | Ran full 7-way dedup chain audit: 9,553 multi-member clusters (max 17 detections), max intra-cluster pairwise separation **4.999″**, **0** clusters exceed the 5″ link ⇒ chaining contributes nothing. Text added §IV C; artifact `r23conf_dedup_audits.json`. |
| META-M2 | MAJ | "anomaly rate vs latitude" denominator undefined; rate per pixel uninterpretable | **PARTIAL→QUEUED** | Existing §IV B caveat already disclaims selection functions, but the per-pixel denominator of the Spearman test is genuinely unspecified and the original script is not in the repo. Queued (needs per-survey coverage/target-density maps). |
| META-M3 | MAJ | SIMBAD P_false uses uniform sky density; underestimates crowded fields | **VERIFIED (qualifier) + QUEUED (MC)** | Honest qualifier added §IV A ("global uniform-density estimate; locally higher in crowded fields … HEALPix-weighted map deferred to the data release"). Full local-density MC queued (needs SIMBAD density map / CDS queries). |
| META-M4 | MAJ | Post-hoc 77,905 SDSS slice could distort dedup geometry; rerun with top-1% and S>5 | **VERIFIED→CLOSED by recompute** | Re-ran identical 7-way dedup with SDSS = top-19,253 → 320,020 unique / 251 multi-survey / 2.98% compression; SDSS = S>5 (12) → 301,034 / 2 / 3.08%. Headline conclusions threshold-insensitive. Text §IV C; artifact `r23conf_dedup_audits.json`. |
| META-M5 | MAJ | r_B/r_R/r_Z never defined mathematically | **VERIFIED** | Formula added §II B (L195): r_X = (1/N_X)Σ|x_i−x̂_i| per arm, common normalized scale, NOT per-arm z-scored; within-object use only. Source: `pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py` L343–345. |
| META-M6 | MAJ | Unclear whether scored Planck patches respect the \|b\|≥20° training mask | **VERIFIED** | Clarifier added §III F: native bank positions all drawn at \|b\|≥20° by construction (extraction code `cmb_native_retrain.py` rejects in-cut positions); scored set and training set share the masked domain. |
| META-M7 | MAJ | "expected 2.3 coincidences vs 3 observed" lacks denominators | **VERIFIED→CLOSED by recompute** | §IV A rewritten: denominators stated (195,829 DESI × 77,905 SDSS native slice); empirical RA-shifted-control expectation 2.75 vs 4 raw 3″ matches on released catalogs; positional coincidence carries no significance, only spectroscopy elevates the 3 §IV C matches (which trace to the cross-transfer-era exercise — different objects, so no subset claim made). Artifact `r23conf_dedup_audits.json`. |
| META-m1 | MIN | OOD set "100k" (§II B) vs "103,000" (§VI D) | **VERIFIED** | Fixed to 103,000 at L200; artifact `jaccard_100k_results.json` (`n_spectra_total: 103000`). |
| META-m2 | MIN | Fig 3 "Probability density" normalization unstated | **VERIFIED** | Caption now states per-survey histograms independently normalized to unit area (`density=True`), shapes comparable, y-axis not counts. Source: `generate_figures.py` L581–589. |
| META-m3 | MIN | eROSITA LMC concentration may be exposure-depth-driven | **STALE** | §III E already states "LMC concentration is partly a depth artifact from the ecliptic-pole scan strategy" — the reviewer's "otherwise qualify" branch is already satisfied. |
| META-m4 | MIN | ~265k catalog-grade subset includes Planck patches yet object-level guidance says point-source tier | **VERIFIED** | Abstract now gives both: 264,938 catalog-grade (incl. 200 patches) and 264,738 catalog-grade point-source subset for object-level work (arithmetic: 264,938−200; 378,080−113,342). |

## Remaining SYNTHESIS findings (non-INSESSION)

| ID | Sev | Verdict | Disposition |
|----|-----|---------|-------------|
| Claude m7 (fig layout: Fig 3 label smudge, p.20/21 whitespace) | MIN | **VERIFIED→QUEUED** | Figure regeneration task (annotation offsets, float placement), not a text edit. Queued. |
| Gemini E1 (7.9% arithmetic) | ESS | **CLOSED-PRIOR** | Same as INSESSION E1 (now 9.4% throughout). |
| Gemini E2 / Perp N3 ("earlier draft listed 10.6 s" withdrawal note in Table V footnote) | ESS/MIN | **HOUSTON-DECISION** | Correction-note removal demand; deliberate disclosure policy — kept (per standing rule). |
| Gemini E3 (notation 1/σ(fNL)² incl. Table IV "1/6(fNL)²") | ESS | **VERIFIED** | All four occurrences now $1/\sigma^2(f_{\rm NL})$ (abstract, §V.b, Table IV(i), caveat (i)). The "1/6" was a PDF-extraction misread of the same expression. |
| Gemini M1 (LAMOST 44,075 vs 113,342 ambiguity) | MAJ | **STALE** | Table I footnote ♠ + §III D give the full three-number disclosure and tier labels. |
| Gemini M2 (SIMBAD-unmatched vs genuine novelty emphasis) | MAJ | **STALE** | Abstract leads with 17.8% qualified point estimate; Table I caption + §IV A + Fig 6 caption all subordinate SIMBAD fractions. |
| Gemini M3 / Grok N1 (placeholder/future date "June 2026") | MAJ/NIT | **FALSIFIED** | It IS June 2026 (auto-falsify rule). |
| Gemini m1 (abstract "BMB/SMBHB" missing subscript) | MIN | **FALSIFIED** | Source is `$B_{\rm MB/SMBHB}$` — properly subscripted; pdftotext flattening artifact. |
| Gemini m2 (~265k scope unclear) | MIN | **STALE+VERIFIED** | Survey list parenthetical already present; further sharpened by META-m4 fix. |
| Gemini m3 (ACT quarantine wording) | MIN | **OPINION** | Current phrasing already separates quarantine vs stratification; no error. |
| Gemini m4 ("uval and oval" in Fig 3 caption) | MIN | **STALE** | Caption uses $\mu_{\rm val}$, $\sigma_{\rm val}$. |
| Gemini m5 (§VI D scope-choice cross-ref) | MIN | **STALE** | L278 now points to §pathc_caveats. |
| Gemini m6 (false-match rate cited §IV A vs computed §IV B) | MIN | **FALSIFIED** | P_false is computed inside §IV A ("Expected false-match rates" paragraph, sec:simbad); the L282 cross-ref is correct. |
| Gemini m7 (Fig 3 caption cites §II D for S definition) | MIN | **VERIFIED** | Caption ref changed to §\ref{sec:training} (II B). |
| Gemini m8 (Fig 12 caption §IIIB roman typo) | MIN | **STALE** | Caption cites \S\ref{sec:highz}. |
| Gemini N1 (Path-C naming consistency) | NIT | **OPINION** | Style preference; "Path-C rebuild/protocol" used contextually. |
| Gemini N2 (Fig 1 caption phrasing) | NIT | **OPINION** | Stylistic. |
| Grok E1 (17.8% headline framing) | ESS | **STALE** | Abstract: "single-sample point estimate at the top-1,000 stratum; full-catalog rate empirically untested". |
| Grok E2 / Perp N6 (SPHEREx 3–5σ overconfident) | ESS/NIT | **STALE/PARTIAL** | §I attributes the forecast to Heinrich et al. methodology; abstract/conclusions carry the <1σ qualifier; "is projected" wording. No unqualified detection claim remains. |
| Grok E3 (LAMOST 44k contaminates headline) | ESS | **STALE** | LAMOST is the disclosed 113,342 exploratory tier; catalog-grade tier (264,938) published as the recommendation — exactly the reviewer's requested parallel tier. |
| Grok M1 / Perp E1, N1 (141× / 73× support) | MAJ/ESS | **FALSIFIED** | Both factors derivable in-paper from Liang et al. 2,685 anomalies (§I): 378,080/2,685=140.8; 195,829/2,685=72.9. The like-for-like 73× is already given alongside 141×. |
| Grok M2 (ACT 200 patches inside headline) | MAJ | **FALSIFIED** | The +200 in 378,280 is the native Planck tier; ACT contributes zero (Table I footnote ‖ explicit: 388,693→388,493, 378,480→378,280 when ACT removed). |
| Grok M3 (SDSS 12-dex tail presented as feature) | MAJ | **STALE** | Cross-transfer is framed as before/after diagnostic, "not a science result" (§II D, Fig 3/4 captions); native re-score supersedes. |
| Grok N2 (sky-map captions lack coordinate system) | NIT | **VERIFIED** | Fig 2 caption now "Mollweide projection in equatorial coordinates (RA/Dec, ICRS)" (source: `generate_figures.py` RA/Dec mollweide); Fig 7 caption already says "equatorial sky map". |
| Perp E2/E13 (σ juxtaposition; two Fisher normalizations) | ESS | **STALE** | v3.1.79/80 added the Fig 8/11 16.85-vs-8.98 reconciliation note; abstract gives the <1σ caveat at point of use. |
| Perp E3 (Fisher-positivity form derivation) | ESS | **STALE/PARTIAL** | Caveat (i) documents F₀, c=0.0747, 5-α refit positivity, and the stationary-point argument; further strengthened by META-E1 de-bias sentence. |
| Perp E4 (NANOGrav γ not in cited ref) | ESS | **FALSIFIED** | γ=2.567±0.382 is this paper's own MCMC on NANOGrav's public KDE product (§V A + App E, full provenance); the citation is for the dataset, not the number. |
| Perp E5/E12 (σ_val "is set such that" contradicts Eq. 2) | ESS | **VERIFIED** | Reworded L195: "the measured (μ_val, σ_val) place the S>5 threshold at MSE ≈ 0.143" — removes the tuned-parameter implication; Eq. (2) definition unchanged. |
| Perp E6 (galaxy/QSO 0.75%/0.037% counts unverifiable) | ESS | **QUEUED** | Per-class numerator/denominator artifact not in repo; queued (release parquet recount). |
| Perp E7/E8 (Table I threshold confusion; LAMOST mixing) | ESS | **STALE** | Three-threshold disclosure footnotes ♡/♠ added in v3.1.80. |
| Perp E9/E11 (17.8% breadth; 99% from top-10k only) | ESS | **STALE** | Abstract qualifier + §IV A "(only 0.2% of top 10,000…)" + 0.2%≈0.24% chance-consistency sentence (v3.1.80). |
| Perp E10 (PTA likelihood form/approximations unstated) | ESS | **VERIFIED** | App E sentence added: ceffyl-style KDE likelihood factorizes over 30 bins; inter-bin covariance beyond the free-spectrum product not retained; not a full timing-data likelihood. |
| Perp M1 (bib metadata tightening) | MAJ | **PARTIAL→QUEUED** | Bib polish pass (DESI DR1 entry journal info, ADS cross-checks) queued; Perplexity's 15/15 false "doesn't exist" record noted — no entry removed. |
| Perp M2/M3/M4 (length, figure choice, GPU section) | MAJ | **OPINION** | Editorial; v3.1.75 already condensed 32pp→20pp. |
| Perp M5 (unweighted MSE limitation thin) | MAJ | **STALE** | Limitation (7) added in v3.1.80. |
| Perp M6 (38,330 pixels vs 49,152; low-count χ²) | MAJ | **PARTIAL→QUEUED** | χ² caveat paragraph already disclaims interpretive use; the exact pixel-occupancy criterion needs the original script — queued with META-M2. |
| Perp M7 (high-z QSO total S not shown) | MAJ | **STALE** | §III B: "all objects have total score S>5 by construction". |
| Perp N2 (why SDSS DR12/DR16 in cross-match) | NIT | **OPINION/QUEUED-minor** | CDS X-Match catalog availability choice; no error claimed. |
| Perp N4 (radius sweep table) | NIT | **STALE** | Measured 3/5/7″ numbers in prose (v3.1.80). |
| Perp N5 (IF endorsement risk) | NIT | **STALE** | v3.1.80 reframed 284/298 as descriptive, non-independent. |
| Perp N7 (DOIs for repos) | NIT | **HOUSTON-DECISION** | Zenodo DOI minting is a release-process action at arXiv posting. |
| Perp N8 (redshift provenance/uncertainty for z=6.0–6.23) | NIT | **QUEUED** | Provenance (Redrock vs custom fits) not verifiable from local artifacts; never invent. |
| Perp N9 (χ² low-count caveat) | NIT | **STALE** | Caveat paragraph present. |
| Perp N10 (Gaia feature list) | NIT | **QUEUED** | 20-feature list not in local artifacts. |
| Perp N11 (NEOWISE 11.5 score axis) | NIT | **STALE** | §III H labels it canonical-S ranking (v3.1.80). |
| Perp N12 (high-z taxonomy cross-table) | NIT | **OPINION** | Nice-to-have summary table. |
| Perp N13 (injection placement spec) | NIT | **QUEUED** | Plant-position policy lives in per-survey pod scripts not mirrored locally. |
| Perp N14 ("foregound" typo; hyphenation) | NIT | **FALSIFIED** | grep: no "foregound" in source. |
| Perp N15 (Fig 4 "score > 5.0" burned-in label) | NIT | **STALE** | Caption note present ("refers to the DESI-trained cross-transfer score axis"). |
| Perp N16 (Jeffreys "decisive" quantify) | NIT | **STALE** | §V A already gives log₁₀B = +3.85 alongside "decisive". |
| Perp N17 (rhetoric softening) | NIT | **OPINION** | "Neither constitutes a detection" already present. |
| Perp N7-dup (8-way unique count explicit) | MIN | **STALE** | Footnote ‖: 8-way = 378,480 explicit. |

**Counts**: 12 META audited (7 closed by edit/recompute, 1 stale, 1 partial-queued, 2 queued-compute, 1 verified+queued) · 45 synthesis rows audited (9 VERIFIED-closed, 16 STALE, 7 FALSIFIED, 7 OPINION, 2 HOUSTON-DECISION, 6 QUEUED).
