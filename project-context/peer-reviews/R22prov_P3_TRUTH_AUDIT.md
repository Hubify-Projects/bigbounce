# P3 R22prov — PER-FINDING TRUTH AUDIT

**Paper**: P3 `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.79 (22 pp)
**Round**: R22prov (v3 native-PDF, 5 reviewers + META)
**Audit date**: 2026-06-09
**Auditor**: research-integrity agent (per `feedback_peer_review_truth_audit_protocol`)
**Inputs**: R22prov_P3_SYNTHESIS.md (106 findings), R22prov_P3_META_REVIEW.md, 5 reviewer files, paper3_draft.tex (ground truth), figure PDFs/PNGs (pdftotext + visual), `reproducibility/p3_pta_mcmc/README.md`, WebSearch citation forensics.

**Reviewer asymmetry note**: Claude_brutal and Gemini_cosmology returned **ZERO findings** this round. All 106 findings come from Grok (11), META/gpt-5-pro (15), OpenAI (41), Perplexity (39). Per the R22prov-P2 precedent, Perplexity "citation doesn't exist / mismatched" claims went 5/5 FALSE today on P2 — each was web-verified here before any verdict.

**Verdict schema**: VERIFIED / VERIFIED-LIKELY / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION.

---

## Verdict totals (106 findings)

| Verdict | Count |
|---|---|
| VERIFIED | 36 |
| VERIFIED-LIKELY | 1 |
| PARTIAL | 20 |
| OPINION | 13 |
| STALE | 19 |
| FALSIFIED | 16 |
| HOUSTON-DECISION | 1 |

**Round verdict: NOT CLEAN** — 36 VERIFIED findings including multiple ESSENTIAL/MAJOR (data-availability contradiction, top-1% threshold-semantics cluster, Fig 12 undefined "AE" scale, invalid eROSITA independence null, Planck×ACT trivial-null geometry, unsupported ≲0.1% dedup-robustness claim). A v3.1.80 closure wave is required.

---

## 1. Consensus-group verdicts (6 named groups)

| Group | Sev | Reviewers | Verdict | Evidence / disposition |
|---|---|---|---|---|
| `table_iv` (Fisher F0 / normalization) | ESS | Grok M3, OpenAI E1, Perplexity E3 | **SPLIT: OpenAI E1 FALSIFIED · Perplexity E3 STALE · Grok M3 PARTIAL** | OpenAI E1 ("F0 = 1/8.982 is dimensionally inconsistent") is a **PDF text-layer artifact**: tex L491 and L561 both read `$F_0 = 1/8.98^2$` — the superscript flattens to "1/8.982" in PDF extraction (auto-FALSIFY class c). Dimensionally correct as written; 1/8.98² + 0.0747·0.19² → σ=8.14 ✓. Perplexity E3 (two σ baselines unreconciled) is **STALE**: the v3.1.79 E10 closure added the explicit normalization note to Fig 11 caption (L735-746: "not on the same absolute normalization as the redshift-binned Fisher of §V"). Grok M3 (dedup false-match budget) PARTIAL: §IV.A L396 gives ≲10 expected random vs 637 clusters (<2% contamination), but the ≲0.1% radius-robustness claim is the genuine weak link → folded into OpenAI E9 (VERIFIED, below). |
| `table_ii` (taxonomy / 95.3× / Novel) | MAJ | META M5, OpenAI m5, Perplexity M3+E14 | **SPLIT: META-M5 VERIFIED · OpenAI m5 VERIFIED-minor · Perplexity M3 PARTIAL · E14 STALE** | **META-M5 VERIFIED (load-bearing)**: tex L335 confirms the IsolationForest is "trained on the 16-d BigAE latent feature space" — the detectors share features, so the "95.3× enrichment over random-independence" null (L227, L332) is invalid as evidence of independent cross-method agreement. Fix: drop the ×-enrichment framing or add a dependent-baseline caveat. OpenAI m5: Table III caption lacks the 5″-SIMBAD definition of "Novel" — add note. Perplexity E14 STALE: 41,065/77,905 = 52.71% ✓ and the v3.1.79 E13 closure already rewrote the Table II note (internal band-residual taxonomy, SIMBAD claim removed); 52.7% appears nowhere else (grep). Perplexity M3 PARTIAL: class names ("NIR excess/high-z") remain physical-sounding; minor "heuristic label" qualifier optional. |
| `sigma_mixing` (NANOGrav / σ juxtaposition) | ESS | Grok E2+n2, Perplexity E2 | **FALSIFIED (Grok E2) / STALE-PARTIAL (Perplexity E2)** | Grok E2 claims γ=3.0 (+1.13σ) and γ=4.33 (+4.61σ) are "tested under different assumptions." **FALSE**: both are parameter shifts against the SAME posterior γ=2.567±0.382 from the same Ceffyl KDE MCMC ((3.0−2.567)/0.382=1.13 ✓; (4.33−2.567)/0.382=4.61 ✓) — same null procedure, directly comparable; no qualifier required by the comparability rule. Perplexity E2: SPHEREx σ≈0.7 (intro) vs DESI σ_std=8.98 (§V) are clearly attributed to different surveys/instruments; the Fig 11 normalization note covers the internal split → STALE; notation table = OPINION. |
| `audit_artifact` (internal bookkeeping language) | ESS | Perplexity E10 | **HOUSTON-DECISION (Path-C naming) / STALE (rest)** | grep: zero hits for "R7", "R8", "P2 §IV", "anomaly_gold" in the body (Fig 11 caption now reads "Heinrich-etal §IV 15–30% Fisher-info penalty") — those specifics are STALE. "Path-C" (33 uses, incl. title) is the named protocol; renaming is a Houston branding call. "Quarantined" is used consistently and defined in App E (Perplexity n3 → OPINION). |
| `length` | MAJ | Perplexity M1 | **OPINION** | Paper already condensed 49pp→20pp in v3.1.75; OpenAI's own review says "the length is acceptable for PRD." No action. |
| `companion` (duplicated phrase) | MIN | OpenAI m1 | **VERIFIED** | tex L180: "reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)" — literal duplication. Trivial fix. |

---

## 2. Single-vendor ESSENTIAL / MAJOR verdicts

### META_REVIEW (gpt-5-pro)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| META-E1 (unweighted MSE, no inverse-variance weighting) | ESS | **VERIFIED** | Eq. (1) is per-element unweighted MSE; no noise weighting anywhere; §VI Limitations does not name it. Genuine methods limitation. Disposition: add explicit limitation + (feasible) noise-weighted validation slice on a DESI subsample. |
| META-M1 (percentile-to-S mapping opacity: top-1% at S≥0.1060/0.4613) | MAJ | **VERIFIED** | Compounded by an internal contradiction found during audit: §II.B L156 says "DESI DR1 **and SDSS DR18** use an absolute canonical-S cut at S>5.0" while Table I caption says "DESI DR1 **alone** uses the fixed canonical-S cut at S>5.0." Also footnote ♥ calls 19,253 "the harder top-1% score-knee cut" (it IS 1.0% of 1,925,279) while the caption calls 77,905 "top-1%." Fix the L156 sentence + add the percentile-semantics sentence (percentiles computed on the scored sample's S, not a standard normal). |
| META-M2 (DESI top-10k 0.2% SIMBAD ≈ chance) | MAJ | **VERIFIED** | Paper's own §IV.A L396: P_false ≈ 2.4×10⁻³/source ⇒ 0.24% expected random matches ≈ the observed 0.2%. Add one sentence stating null-consistency (it strengthens the paper's own "SIMBAD-unmatched ≠ novelty" point). |
| META-M3 (Planck×ACT null trivial by disjoint footprints) | MAJ | **VERIFIED** | Planck native trained on \|b\|≥20° masked patches (L173, L352); §IV.D states ACT anomalies "concentrate along the Galactic plane" (L477). Near-disjoint masks make the null nearly guaranteed by construction; §IV.D's "demonstrates" conclusion needs the geometry qualifier. Joint with OpenAI M2 + Perplexity E19. |
| META-M4 (LS randoms construction unspecified) | MAJ | PARTIAL | "anomaly-window-matched randoms" + 30-region jackknife stated (L488) but mask/completeness construction not defined. Add one-sentence construction + companion-repo pointer. |
| META-M5 (95.3× independence null invalid) | MAJ | **VERIFIED** | See `table_ii` group above. |
| META-M6 (16× downsampling biases vs narrow lines) | MAJ | PARTIAL | Mechanism already acknowledged in caveat (ii) L563 ("narrow in-distribution features are reconstructed accurately whereas broad continuum deformations elevate MSE") + LAMOST/SDSS emission-line FAIL labels. Downsampling-specific quantification absent; add a scoping sentence ("narrow-line discovery outside validated capability"). |
| META-M7 (gate thresholds not pre-registered) | MAJ | PARTIAL | Thresholds disclosed; ad hoc but standard practice. A Jaccard 0.65/0.75 sensitivity sentence is a cheap robustness add; not a blocker. |

### OpenAI_methodology

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1 (F0 dimensional) | ESS | **FALSIFIED** | See `table_iv` group — flattened superscript artifact; tex has `1/8.98^2`. |
| E2 (NEOWISE polar-cap factor of 2) | ESS | **FALSIFIED** | OpenAI's math is wrong: spherical-cap fractional area = (1−cos θ)/2 = 0.76% per cap, NOT (1−cos θ)=1.52% per cap. Two caps (\|b_ecl\|≥80°) = 1.52% total — exactly the paper's uniform-null (L362); 17/436 = 3.90%; 3.90/1.52 = 2.57 ≈ 2.6× ✓. Paper is correct. |
| E3 (Table V Planck CAE 10.6 s implausible) | ESS | **VERIFIED-LIKELY** | 10.6 s total training for a 1.1M-param CAE on 2×10⁵ 64×64 patches (A100) is implausible for multi-epoch convergence; likely per-epoch or a logging mislabel. Cannot falsify without training logs. Disposition: clarify units/epochs/batches for all Table V rows (joint m9). |
| E4 ("none of top 100 in any database" contradictory) | ESS | **VERIFIED** | L241: "none of the top 100 appear in any database" (six databases incl. Gaia DR3, AllWISE) sits unreconciled against L393: top-1,000 (a superset) is 82.2% archival-ID'd in 20 catalogs incl. Gaia/AllWISE. Need per-database top-100 counts or scope-limited wording (joint META-m2 VERIFIED). |
| E5 (data not public at submission) | ESS | **VERIFIED** | L613: HuggingFace dataset "private pending arXiv acceptance" directly contradicts abstract L92 "are publicly released." PRD blocker. Fix: flip dataset public with DOI (hard path) or amend abstract wording. Joint Perplexity E30. |
| E6 (Table I ACT-incl. total confusing) | ESS | PARTIAL | Footnotes ¶/∥ fully reconcile; presentational. Optional restructure. |
| E7 (Fig 12 implausible AE values) | ESS | **VERIFIED** | pdftotext of `figures/fig_gallery_top10.pdf` confirms burned-in labels: "AE=83518" (Multi-band), "AE=17663" (BAL QSO), "AE=9240", "AE=8280", "AE=6512"… while panel 1 has "AE=5.30" (= r_Z per §III.B). O(10³–10⁵) values cannot be canonical S (range 5–25.2) or r_Z (mean 3.9) — mixed undefined scales in one figure, caption silent. Fix: re-render panels with canonical S or define the raw-residual scale in the caption. |
| E8 (77,905 ≠ top-1%) | ESS | **VERIFIED** | 77,905 = 3.38% of 2,304,830 (table's own Rate column) / 4.05% of 1,925,279; 1% of 1.93M = 19,253 — which footnote ♥ itself calls "the harder top-1% score-knee cut." Caption simultaneously labels 77,905 "SDSS top-1%." Internal contradiction. Fig 4 title (image) further says "77,905 anomalies (score > 5.0)" — the DESI-trained cross-transfer axis. Fix: relabel 77,905 as "continuity slice equal in size to the cross-transfer set"; reserve "top-1%" for 19,253; repair §II.B L156. |
| E9 (≲0.1% dedup-radius robustness unsupported) | ESS | **VERIFIED** | L446 asserts ≲0.1% but only the 10,213/388,493 = 2.63% compression ceiling is demonstrated; the {3″,5″,7″} sweep is explicitly "on-record deferred." Fix: run the sweep on the dedup manifest (`pathc_dedup/`, cheap) or weaken to the demonstrated ≤2.63% ceiling. Joint OpenAI M6 + Perplexity E21. |
| E10 (Step 1 "2–5×10⁵" vs DESI 47k) | ESS | **VERIFIED** | L172 Step 1 range excludes DESI's 47,000-spectrum pool (L141, L159). Amend to "O(5×10⁴) for DESI; 2–5×10⁵ for others." |
| E11 (footnote ∥ "input sum" ambiguity) | ESS | PARTIAL | "Input sum" = 388,693 anomaly-detection sum (App E L799 reconciles 388,693−10,213=378,480, +200), correct but ambiguous vs N_total (−20,000). Rewrite for precision. |
| M1 (58.8% weighting undefined) | MAJ | **VERIFIED** (minor) | Aggregate method/denominator unstated (L388). One-sentence fix. |
| M2 (Planck×ACT null lacks statistic) | MAJ | **VERIFIED** | §IV.D L477 gives no estimator, uncertainty, or p-value. Joint META-M3. |
| M3 (fixed-α vs empirical-α tags) | MAJ | **STALE** | §V L491 + Fig 9 caption L504-508 already segregate explicitly ("illustrates the fixed-α reference configuration only; the primary forecast uses the empirical α_jk"). |
| M4 (injection plant spec insufficient) | MAJ | PARTIAL | Plant files + per-survey curves deposited in companion repo (caveat ii L563); add 2–3-sentence in-paper plant spec. |
| M5 (in-sample rate line) | MAJ | PARTIAL | 47k = 0.2% of the 22.5M pool — effect on the 0.87% rate is negligible; caveat (i) covers robustness. Optional one-liner. |
| M6 (5″ sensitivity sweep) | MAJ | **VERIFIED** | = E9 family. |
| M7 (NEOWISE score definition) | MAJ | **VERIFIED** (minor) | State canonical-S ranking + top-1% selection explicitly in §III.H. |
| M8 (heterogeneous PASS/FAIL pooling) | MAJ | PARTIAL | Fig 10 caption already discloses morphology variants and "per-survey decisive gate" framing. |
| M9 (3 populations vs 14 clusters) | MAJ | **VERIFIED** | Fig 4 image title: "14 clusters, 99.4% clustered"; text L283 + Conclusions item 3 say "3 latent-space populations." Add the grouping sentence (14 HDBSCAN clusters → 3 physical categories). |
| M10 (1,925,279 vs 2,304,830 drop unexplained) | MAJ | **VERIFIED** | No quality-cut criteria stated anywhere for the native re-score pool. Add criteria + numerator/denominator. |
| M11 (Fig 8 panel d score axis) | MAJ | **VERIFIED** | 49.5 must be the DESI-trained cross-transfer score (native re-score compresses extremes to S<14 per Fig 3 caption); Fig 8 caption says only "SDSS anomaly score (= 49.5)." Label the axis. Joint Perplexity E15. |
| M12 (catalog-grade tier: Planck in or out?) | MAJ | **VERIFIED** | Abstract L92 lists the ~265,000 catalog-grade subset as "DESI + SDSS + eROSITA + Gaia + NEOWISE" (no Planck); footnote ♠ L230 defines the 264,938 catalog-grade tier as "DESI + SDSS native + eROSITA + **Planck native** + Gaia + NEOWISE." Direct inconsistency — fix the abstract list. |

### Grok_brutal (E/M singles)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1 (7.9% improvement language) | ESS | **STALE** | The abstract already contains verbatim the demanded qualifier: "7.9% improvement **consistent with no improvement at <1σ**" (L92); §V repeats it + "not a positive multi-tracer detection claim." |
| E3 (no recovery curves for native models) | ESS | **FALSIFIED** | pdftotext of `figures/fig_injection_recovery.pdf` shows recovery-vs-amplitude curves for SDSS (cont-dip + em-line), LAMOST (both), eROSITA (latent IF), Gaia (variab. IF) — all NATIVE checkpoints (caption: "9.7× improvement post-native-retrain"). The claim "only the cross-transfer baseline appears in Fig. 10" is false. |
| E4 (χ² circularity) | ESS | PARTIAL | §IV.B L423 already carries the full caveat ("should not be cited as evidence of astrophysical clustering without per-survey selection-function corrections"). Residual: tighten the "as expected for a population that traces real astrophysical structures" phrase. |
| M1 (largest-scale superlative unsupported) | MAJ | OPINION | Comparison IS provided: intro lit review (Baron 2017, Liang 2,685, Nicolaou ~208k — "all prior searches sub-million scale"), 141×/73× ratios, §VI.C comparison subsection. A table is optional polish, not a gap. |
| M2 (α_jk selection bias) | MAJ | PARTIAL | Grok misstates the sample: α_jk is measured on the full 5,384 QSO-candidate set (L488), not the 1,122 GS subset (that is the secondary check, caveat j). Result already labeled <1σ-from-null central-value forecast; GS re-measurement is itself the requested stability variant. |

### Perplexity_citations (E/M singles — each citation claim web-verified)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1 (citation forensics incomplete — global) | ESS | OPINION | A reviewer process statement, not a paper defect. All load-bearing citations spot-verified below: every one exists. |
| E4 (NANOGrav KDE traceability) | ESS | **STALE** | App E gives Zenodo DOI 10.5281/zenodo.8060824, product `30f_fs{hd}_ceffyl`, sampler config, diagnostics (ESS≈5,500, τ≈58, acc 0.632); `reproducibility/p3_pta_mcmc/README.md` L397-408 documents the rerun (γ=2.567±0.382, ESS=5,507, 25 s on H200). Fully provenanced. |
| E5 (matter-bounce f_NL=−35/8 and γ=3.0 sourcing) | ESS | **FALSIFIED** | Sources exist and are correctly cited: Cai, Xue, Brandenberger & Zhang, "Non-Gaussianity in a Matter Bounce," JCAP 0905:011 (2009), **arXiv:0903.0631** (the f_NL=−35/8 source); Wilson-Ewing arXiv:1211.6269; Quintin+ PRD 90, 063507 (2014); Cai SCPMA 57, 1414 (2014). The w=0 scalar-only decoupling caveat is present in §V L514 + App E L786. |
| E6 (141× scale claim referencing) | ESS | **FALSIFIED** | Liang et al. exists: **arXiv:2307.07664**, "Outlier Detection in the DESI Bright Galaxy Survey," MNRAS 525, 1078 (2023); comparator 2,685 (1.07%) stated in intro L107; 378,080/2,685 = 140.8 ✓, 195,829/2,685 = 72.9 ✓. |
| E7 (Nicolaou "in press" status) | ESS | PARTIAL | The work exists: **arXiv:2506.17376**, "Identifying Anomalous DESI Galaxy Spectra with a Variational Autoencoder" (~200k DESI spectra, Astronomaly active learning). Bib title ("Anomaly Detection in DESI Early Data Release Spectra with Astronomaly") and "MNRAS in press" status should be refreshed; add the arXiv ID. |
| E8 (SPHEREx σ(fNL)≈0.7 traceability) | ESS | **FALSIFIED** (+ bonus fix) | Heinrich, Doré & Krause **arXiv:2311.13082** confirms verbatim: "fiducial result of σ_fNL = 0.7 from bispectrum alone." The number is exactly traceable. **Bonus audit catch**: the bib venue is wrong — published as **Phys. Rev. D 109, 123511 (2024)** (doi:10.1103/PhysRevD.109.123511), not "J. Cosmol. Astropart. Phys. 2024, 074." Fix the bib entry. |
| E9 (17.8% definition consistency) | ESS | **STALE** | Identically defined + caveated ("single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested") in abstract, §IV.A, Fig 6 caption, Limitations (6), Conclusions item 2. |
| E11 (Table I arithmetic inconsistency) | MAJ | **FALSIFIED** | All arithmetic checks: 195,829+77,905+113,342+298+200+500+419 = 388,493 ✓; −10,213 = 378,280 ✓; 378,080+200 = 378,280 ✓; 637+9,576 = 10,213 ✓; N_total 37,292,042−20,000(ACT) = 37,272,042 ✓. |
| E12 (141×/73× under-specified) | MAJ | **FALSIFIED** | Comparator 2,685 given in intro L107; ratios correct (see E6). |
| E13 (DESI taxonomy percentages inconsistent) | MAJ | **FALSIFIED** | 151,244/195,829 = 77.23→77.2% ✓; 44,436 = 22.69→22.7% ✓; 34 = 0.017→0.02% ✓; 19 = 0.0097→0.01% ✓; 96 = 0.049→0.05% ✓; counts sum exactly to 195,829; the 0.02 pp residual is pure rounding. |
| E15 (Fig 8 score 49.5 conflict) | MAJ | **VERIFIED** | = OpenAI M11. |
| E16 (Fig 10 vs Table I gate granularity) | MAJ | **STALE** | Fig 10 caption explicitly reconciles: "the headline 3-PASS/3-FAIL-with-diagnostic decomposition refers to the per-survey decisive gate result, not to per-morphology variants" + the XV metrics footnote. |
| E17 (77/23 rounding in Conclusions) | MAJ | **FALSIFIED** | Integer rounding in prose; Perplexity's own text concedes "which is fine for prose." Non-finding. |
| E18 (Fig 11 caption heavy lifting) | MAJ | **STALE** | This IS the v3.1.79 E10 closure; caption carries the full reconciliation + "absolute σ values should be read from §V" cross-pointer; App C hosts the implementation detail. |
| E19 (Planck×ACT null overclaims) | MAJ | **VERIFIED** | §IV.D's "demonstrates" rests on (a) the quarantined ACT artifact set (App E admits the null "relies on the cross-transfer ACT anomaly set as its input") and (b) near-disjoint footprints (META-M3). Qualify as expected-by-construction; soften. |
| E20 (17.8% no error model) | MAJ | **VERIFIED** (minor) | Add the binomial CI: 178/1,000 → 17.8% ± 1.2% (Wilson 68%). Trivial DO. |
| E21 (5″ ≲0.1% asserted not derived) | MAJ | **VERIFIED** | = OpenAI E9. |
| E22 (largest-scale comparison set) | MAJ | OPINION | Claim is scoped to "autoencoder anomaly detection across [multiple] archives"; prior-work comparison provided (= Grok M1). |
| E23 ("DESI-only axis" ambiguous) | MAJ | **VERIFIED** (minor) | Change "axis" → "subset/catalog" in abstract. |
| E24 (378,280 mixed-unit count) | MAJ | **STALE** | Abstract, Table I stratification note, and Conclusions item 1 all explicitly stratify 378,080 point-source + 200 patches and direct downstream use to 378,080. |
| E25 (eROSITA threshold language) | MAJ | **STALE**/OPINION | §III.E ("298 at S>0.259, top 0.03%, data-driven score-knee") and Table I caption are consistent; repetition ask is style. |
| E26 (Jaccard tests conflated in Conclusions) | MAJ | **VERIFIED** | The two tests are properly separated in the body, BUT Conclusions item 6 quotes "OOD control-vs-control **0.874** (PASS)" — a number defined nowhere in the body (body has prod×ctrl **0.732**, L159/L561). Real loose end caught by this audit: align Conclusions with 0.732 or define 0.874. |
| E27 ("three independent signatures") | MAJ | **VERIFIED** (minor) | GP trough and Z-arm dominance are physically correlated (both driven by blueward flux suppression at z≈6); change "independent" → "complementary." |
| E28 (Bayes vs parameter-shift bridge) | MAJ | **STALE** | §V.A already labels them separately: "strongly disfavored **as a parameter-shift**" then "**Proper Savage-Dickey Bayes factors** against the γ-uniform prior…" |
| E29 (dense-limit numbers absent from §V) | MAJ | **STALE**/OPINION | Deliberate normalization separation (v3.1.79 closure); cross-pointers present in both directions. |
| E30 ("publicly released" vs private) | MAJ | **VERIFIED** | = OpenAI E5. |
| M2 (over-selling weak constraints) | MAJ | **STALE**/PARTIAL | "<1σ," "not a detection," "marginally consistent," "Neither … constitutes a detection" appear at every quotation site (abstract, §V, §V.A, Conclusions). |

---

## 3. Batched MINOR / NIT verdicts

| ID | Verdict | One-line evidence |
|---|---|---|
| Grok m1 (Fig 3 Poisson bars) | OPINION | Cosmetic; log-density panel disclosure adequate. |
| Grok m2 (0.4437 units) | OPINION | It is val MSE on the same axis as gate criterion (a) ≤0.30; labeled val_loss; CMB comparability handled via criterion (b). |
| Grok n1 ("Dated: June 2026") | **FALSIFIED** | It IS June 2026 (auto-class b). Standard revtex \date. |
| Grok n2 (caption §VI.A drift) | **FALSIFIED** | Zero literal stale references; all cross-refs are `\S\ref{}` macros that resolve at compile. |
| META-m1 (PM epoch propagation) | PARTIAL | Acknowledged un-propagated (L446); quantitative high-PM bound absent. Optional add. |
| META-m2 (top-100 "any database") | **VERIFIED** | Folded into OpenAI E4. |
| META-m3 (Planck patches in spatial tests?) | **VERIFIED** (minor) | tex does not state whether the 200 patches enter the 38,330-pixel χ²/latitude tests; one clarifying sentence. |
| META-m4 (≲10 coincidence underived) | PARTIAL | πr²n method shown for SIMBAD + DESI×SDSS pairs; 7-way figure asserted. Appendix numbers or soften. |
| META-m5 (0.0287 μval = val_loss) | OPINION | Loss is defined as per-element MSE (Eq. 1); μval = mean validation MSE — equal by construction as written. |
| META-m6 (z≈6 FP rate) | PARTIAL | Labeled "candidates" throughout; FP estimate absent. Optional contamination estimate. |
| META-N1 (108″ vs 0.262″/pix) | PARTIAL→NIT | Internally consistent custom pixscale 0.42″/pix (128 px = 54″ §III.B; 256 px = 108″ Fig 5) — Legacy cutout service supports arbitrary pixscale; META assumed native 0.262″. Optionally state the pixscale. |
| OpenAI m2 (0% artifact method) | VERIFIED (minor) | Add inspection-protocol sentence. |
| OpenAI m3 (Fig 3 caption note) | **STALE** | Caption already states the cross-transfer artifact + native compression to S<14. |
| OpenAI m4 (Fig 6 caption novelty note) | **STALE** | Caption already says "database-coverage measurement, not a discovery rate." |
| OpenAI m6 (χ² caution) | **STALE** | §IV.B already says "should not be cited as evidence of astrophysical clustering…" |
| OpenAI m7 (posterior notation) | **STALE** | §V.A already assigns ±0.382 (mean-shift) vs ±0.29 (credible-interval) roles explicitly. |
| OpenAI m8 (bib bracketed note) | **VERIFIED** | L978 bookkeeping note in bibliography text; move to a `%` comment. |
| OpenAI m9 (Table V units/epochs) | PARTIAL | Header has "(s)"; epochs/batch/dataset sizes absent (joint E3). |
| OpenAI m10 (trustworthiness k) | VERIFIED (minor) | k for the trustworthiness metric unreported (App D). |
| OpenAI m11 (Planck score axis) | VERIFIED (minor) | "[0.558, 0.621]" axis undefined in §III.F; name the score. |
| OpenAI m12 (8-way ACT counts) | **FALSIFIED** | App E L799 gives the numbers: 388,693 − 10,213 = 378,480 (+200, zero positional overlaps); Table I footnote ∥ confirms. |
| OpenAI n1 (hyphenation "con- /–") | **FALSIFIED** | Two-column line-break hyphenation in the PDF text layer (auto-class c); tex clean. |
| OpenAI n2 (Path-C capitalization) | **FALSIFIED** | grep: 33/33 occurrences exactly "Path-C"; zero variants. |
| OpenAI n3 (quasi-matter vs matter-bounce) | PARTIAL/NIT | Both terms denote the same w=0 class here; App E carries the harmonizing sentence. Optional standardization. |
| OpenAI n4 ("on the rescaled scale") | OPINION | Wording preference. |
| OpenAI n5 ("Rosatom proprietary control") | **VERIFIED** (+factual fix) | Worse than flagged: "Rosatom" (nuclear agency) is factually wrong — the SRG/eROSITA eastern-hemisphere data rights sit with the Russian consortium (IKI/Roscosmos). Fix to neutral + correct attribution. |
| OpenAI n6 (Ceffyl capitalization) | VERIFIED (NIT) | L550 "Ceffyl" vs App E `\texttt{...ceffyl}`; standardize lowercase. |
| Perplexity n1 (repeated caveats) | OPINION | Deliberate post-condensation redundancy at quotation sites. |
| Perplexity n2 (Fig 11 internal labels) | **STALE** | grep: "P2 §IV" / "anomaly_gold" absent; caption now cites "Heinrich-etal §IV penalty." |
| Perplexity n3 ("quarantined" tone) | OPINION | Consistent technical usage, defined in App E. Houston style call. |
| Perplexity N1 (headline/canonical overuse) | OPINION | Style. |
| Perplexity N2 (σ notation table) | OPINION | Nice-to-have; normalization note already does the load-bearing work. |
| Perplexity N3 (informal wording) | OPINION | "single most important methodological lesson" is mild; "not a science result" is deliberately blunt and accurate. |

---

## 4. FALSIFIED list with evidence (16)

1. **OpenAI P3-E1** (F0 = 1/8.982 dimensional error) — PDF text-layer flattening of `$1/8.98^2$` (tex L491, L561). Auto-class (c).
2. **OpenAI P3-E2** (NEOWISE factor-of-2) — reviewer used (1−cos θ) instead of (1−cos θ)/2 for cap area; paper's 1.52% two-cap null and 2.6× ratio are exactly correct.
3. **Grok P3-E2** (σ juxtaposition rule violation) — +1.13σ and +4.61σ are shifts against the SAME γ=2.567±0.382 posterior; same null procedure, directly comparable.
4. **Grok P3-E3** (no native recovery curves) — `fig_injection_recovery.pdf` contains native-checkpoint recovery-vs-amplitude curves for SDSS/LAMOST/eROSITA/Gaia (pdftotext evidence).
5. **Grok P3-n1** ("Dated: June 2026" internal tag) — it IS June 2026. Auto-class (b).
6. **Grok P3-n2** (caption cross-ref drift) — all refs are `\S\ref{}` macros; no literal stale refs exist.
7. **OpenAI P3-m12** (8-way ACT counts missing) — App E L799: 388,693−10,213=378,480 (+200, zero overlaps).
8. **OpenAI P3-n1** (hyphenation artifacts) — two-column PDF text-layer line breaks. Auto-class (c).
9. **OpenAI P3-n2** (Path-C capitalization varies) — grep 33/33 identical.
10. **Perplexity P3-E5** (matter-bounce sourcing untraceable) — Cai+ "Non-Gaussianity in a Matter Bounce," JCAP 0905:011, **https://arxiv.org/abs/0903.0631**; Wilson-Ewing **https://arxiv.org/abs/1211.6269**; Quintin+ PRD 90, 063507; Cai SCPMA 57, 1414. All cited in bib.
11. **Perplexity P3-E6** (141× comparator unverifiable) — Liang+ MNRAS 525, 1078 (2023), **https://arxiv.org/abs/2307.07664**; 2,685 comparator in intro; 140.8× / 72.9× arithmetic ✓.
12. **Perplexity P3-E8** (SPHEREx 0.7 untraceable) — Heinrich, Doré & Krause, **https://arxiv.org/abs/2311.13082**: "fiducial result of σ_fNL = 0.7 from bispectrum alone" — verbatim match. (Bonus: bib venue must change to Phys. Rev. D 109, 123511 (2024).)
13. **Perplexity P3-E11** (Table I arithmetic) — all five sums verified exactly (see §2).
14. **Perplexity P3-E12** (141×/73× under-specified) — both numerator and denominator in text; ratios exact.
15. **Perplexity P3-E13** (taxonomy percentages) — all five fractions correct to rounding; counts sum exactly to 195,829.
16. **Perplexity P3-E17** (77/23 rounding) — integer prose rounding; reviewer concedes "fine."

**Perplexity citation-forensics scorecard this round: 0 confirmed citation errors in 39 findings** (consistent with the 5/5-FALSE P2 precedent). The only real bib defects (Heinrich venue, Nicolaou arXiv ID) were found by THIS audit's web checks, not asserted by Perplexity.

---

## 5. Bonus audit catches (not in any reviewer's findings — add to v3.1.80)

1. **Heinrich2023 bib venue wrong**: published Phys. Rev. D **109, 123511 (2024)** (doi:10.1103/PhysRevD.109.123511), not "J. Cosmol. Astropart. Phys. 2024, 074." (Surfaced while falsifying Perplexity E8.)
2. **Nicolaou bib**: add arXiv:2506.17376; refresh title ("Identifying Anomalous DESI Galaxy Spectra with a Variational Autoencoder") and in-press status.
3. **Table IV caveat (i)** says "**95%** envelope [3.92, 8.98]" while abstract/§V/Conclusions all call the same interval the "**1σ** envelope." Harmonize.
4. **Conclusions "OOD control-vs-control 0.874"** is defined nowhere in the body (body: prod×ctrl 0.732) — filed under Perplexity E26 VERIFIED.
5. **§II.B L156** ("DESI DR1 and SDSS DR18 use an absolute canonical-S cut at S>5.0") contradicts Table I caption ("DESI DR1 alone…") — filed under OpenAI E8 / META-M1.

---

## 6. Disposition

### v3.1.80 closure wave — DO (ordered hardest-first)

| # | Item | Source findings |
|---|---|---|
| 1 | Data availability: flip HF dataset public with DOI, or amend abstract "publicly released" → release-on-acceptance wording (hard path preferred: make it public) | OpenAI E5, Perplexity E30 |
| 2 | Dedup-radius {3″,5″,7″} sensitivity sweep on the dedup manifest (`pathc_dedup/`); replace ≲0.1% claim with measured numbers (or demonstrated ceiling) | OpenAI E9/M6, Perplexity E21, Grok M3 |
| 3 | Threshold-semantics cleanup: drop "top-1%" label from 77,905 (continuity slice, 3.38%/4.05%); reserve "top-1%" for 19,253; fix §II.B L156 contradiction; add percentile-on-scored-sample sentence | OpenAI E8, META-M1 |
| 4 | Fig 12 gallery: re-render panel labels with canonical S (or define the raw "AE" residual scale in caption); reconcile AE=5.30 vs AE=83,518 mixed scales | OpenAI E7 |
| 5 | eROSITA 95.3×: remove independence-null "enrichment" framing; state IF is trained on the BigAE latent (dependent detectors); reframe 284/298 as internal-consistency, not independent confirmation | META-M5 |
| 6 | Planck×ACT: add disjoint-footprint qualifier (trivial-by-geometry), name the estimator or soften "demonstrates"; note reliance on quarantined ACT set at the §IV.D site | META-M3, OpenAI M2, Perplexity E19 |
| 7 | Top-10k/top-100 cross-match: per-database top-100 counts or scope-limited wording; add SIMBAD-chance-consistency sentence (0.2% ≈ 0.24% random) | OpenAI E4, META-m2, META-M2 |
| 8 | META-E1: add unweighted-MSE/no-inverse-variance limitation to §VI; run noise-weighted validation slice if pod time allows | META-E1 |
| 9 | SDSS native pool: state the 2,304,830 → 1,925,279 quality cuts | OpenAI M10 |
| 10 | Abstract catalog-grade list: include Planck native (footnote ♠ tier = 264,938) or re-derive point-source-only figure | OpenAI M12 |
| 11 | Conclusions item 6: 0.874 → 0.732 (or define) ; Table IV (i) "95%" → "1σ" | Perplexity E26, bonus #3/#4 |
| 12 | Step 1 training-pool wording (DESI 47k); footnote ∥ "input sum" precision | OpenAI E10, E11 |
| 13 | Table V: units/epochs/batches for all rows; resolve the 10.6 s Planck CAE row (per-epoch vs total) | OpenAI E3, m9 |
| 14 | Fig 8 panel (d): label cross-transfer axis; Fig 4: add "14 HDBSCAN clusters → 3 populations" sentence | OpenAI M11/Perplexity E15, OpenAI M9 |
| 15 | Bib hygiene: Heinrich venue → PRD 109, 123511; Nicolaou + arXiv:2506.17376; m8 bracketed note → comment | bonus #1/#2, OpenAI m8 |
| 16 | Minor batch: L180 duplication; Table III "Novel" 5″ note; 58.8% weighting; NEOWISE score def; trustworthiness k; Planck score axis; Planck-patches-in-χ² clarifier; 0% artifact protocol; 17.8% binomial CI; "axis"→"subset"; "independent"→"complementary"; Rosatom→IKI/Russian consortium; ceffyl; χ²-phrase tighten | OpenAI m1/m2/M1/M7/m10/m11, META-m3, Perplexity E20/E23/E27, OpenAI n5/n6, Grok E4 |

### No-action (with reason)

- All 16 FALSIFIED (evidence above) — no text change driven by these.
- All 19 STALE — already addressed in v3.1.75–v3.1.79 (notably the Fig 11 normalization note, Table II taxonomy note, 17.8% caveats, fixed-α segregation, posterior-notation paragraph).
- All 13 OPINION (length, style, term frequency, deliberate redundancy).
- PARTIALs not in the DO table (META-M4/M6/M7/m1/m4/m6/N1, OpenAI E6/M4/M5/M8/n3, Perplexity M3/E7-bib-part) — caveats already present; optional polish items, queue behind the wave.

### HOUSTON-DECISION (1)

- **Perplexity E10**: whether to rename/de-emphasize "Path-C" as protocol branding in a PRD submission (33 uses incl. title). All other internal-tag specifics in that finding are already gone from the body.

### Round verdict

**NOT CLEAN.** 36 VERIFIED + 1 VERIFIED-LIKELY, including ≥6 ESSENTIAL-tier items. Per `feedback_readiness_oscillation`, P3 readiness must roll backward pending the v3.1.80 wave; a follow-up cross-vendor round on v3.1.80 is required before the 99% gate. Reviewer-strength note for the learning loop: Claude and Gemini contributed zero findings on a paper where OpenAI-family reviewers found genuine VERIFIED essentials — investigate the P3 prompt/PDF routing for those two vendors before the next round.
