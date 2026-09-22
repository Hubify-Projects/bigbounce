# Canonical dispositions — anomaly flagship (AF)

Manuscript: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex` → `main.pdf`.
First full draft assembled by lane LA (vAF.0.2, 2026-09-19). Registered in SSOT/Convex/site
and closed 2 of 4 open TODOs (ADS bibliography verification, acknowledgements) by lane LR1
(vAF.0.3, 2026-09-19). Ledger opened 2026-09-19 at vAF.0.2/vAF.0.3.

---

## R1 wave (2026-09-19) — `ROUND_2026-09-19-AF-vAF.0.3-EXACTPDF-d85487e9-R1`

Board: Claude opus (INT, verdict-blind) reviewed the exact vAF.0.2 PDF (sha8 `b972d890`) —
science content identical to vAF.0.3 (only acknowledgements/Appendix-A bib note differ).
Grok API `grok-4.3` + Gemini API `gemini-3.1-pro-preview`
(`tools/v3_native_pdf_review.py`, `ApJS-CATALOG` profile) reviewed the exact vAF.0.3 PDF
(sha8 `d85487e9`).

**Verdicts:** Claude opus MAJOR REVISIONS (6 BLOCKER, 16 MAJOR, 16 MINOR, 9 NIT). Grok
REJECT (6 ESSENTIAL + 3 MAJOR pass 1, 3 ESSENTIAL pass 2, 2 MINOR, 1 NIT). Gemini MAJOR
REVISIONS (5 ESSENTIAL + 1 MAJOR pass 1, 3 findings pass 2, 1 NIT). All three legs
independently converged on the same core defects (validation pass-count error,
abstract/body mismatch on power and blue-arm origin, title not carrying the null) —
strong triangulation, not a single reviewer's idiosyncrasy.

**Orchestrator verification method:** every BLOCKER and the highest-impact MAJOR findings
were independently re-derived from the committed artifacts
(`validation_contract_results.json`, `flagship_sample_v2.parquet`,
`flagship_sample_v2_enriched.parquet`) before any closure — not accepted from reviewer
text alone, per the standing truth-audit rule. Every spot-check confirmed the reviewer's
numbers exactly (10/10 checks: validation pass count 11/16; the "Supported" candidate's
empty morphtype and exact-zero WISE/shape columns; its r/z flux ratio; V10's five p-values;
the `worst_band` census 1180/1244; the mean_mse R² decomposition 0.777→0.006/0.609/0.201;
the residual-vs-SNR Spearman correlations; the rest-frame concentration test; the
matched/unmatched flux/SNR/score medians and p-values; the BAL enrichment 3.3× recompute).

### DAF-01 (BLOCKER, all 3 legs convergent): §V A states "Thirteen requirements pass"; the checker returns eleven
- **class:** CLOSED — GENUINELY-NEW-REAL
- Independently reproduced: `validation_contract_results.json` → PASS×11, REPORTED×2,
  STRUCTURED-BUT-WEAK×1, FAIL×2 (16 total). §V A's own sentence was also internally
  impossible (named 5 more as "additional" to "thirteen", implying 18 of 16).
- **Closure:** "Eleven requirements pass outright" + explicit V1-partial-pass note (folds
  in DAF-06 below). main.tex §V A.
- **fingerprint:** thirteen requirements pass, eleven, validation contract, pass count

### DAF-02 (BLOCKER): Table I caption claims all 13 artifacts re-hashed and matched (checks V2+V3); only 9 are
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: V2 observed "9/9 artifacts match" (nine released data products only); V3
  observed hashes "recorded", not re-verified, for contract/model/zcatalog; inference-code
  hash covered by neither.
- **Closure:** caption rewritten to state exactly what V2 (9 re-hashed) vs. V3 (recorded,
  chain-bound) vs. neither (inference code) each cover. main.tex Table~\ref{tab:chain} caption.
- **fingerprint:** provenance chain caption, thirteen re-hashed, V2 V3

### DAF-03/DAF-04 (BLOCKER, paired): the "Supported" FT-A candidate is a photometric-join-defect row; the break test's r/z halves are unapplied and contradict the verdict
- **class:** CLOSED — GENUINELY-NEW-REAL (the most consequential finding of the round)
- Independently verified against `flagship_sample_v2_enriched.parquet`: TARGETID
  39627849358909321's `morphtype` is empty and `flux_w1=flux_w2=sersic=shape_r=0.0`
  exactly — the identical signature of the disclosed 406-row photometric-join gap. Its
  own `flux_r=0.886`, `flux_z=0.286` (ratio 3.1) is backwards for a z=4.334 Lyman break
  (expected f_r≲f_z, not f_r≈3×f_z). Applying the same g+r dropout test the paper already
  uses for the refuted candidate, uniformly, to the two z≈6.07 candidates also finds their
  r-band fluxes (0.255, 0.330 nmgy) comparable to or larger than their own g fluxes, in a
  band the break requires dark.
- **Closure:** "Supported" downgraded to "Undecidable from the release"; abstract's
  "supports one" removed, replaced with "refutes one... cannot confirm or refute the
  remaining three"; verdict is now 1 refuted / 3 undecided (was 1/1/2). No new photometry
  was fetched (DR10 forced-photometry query remains the honest next step, stated as such).
  main.tex §VII B, abstract, §I item 6, §XI.
- **fingerprint:** Supported, 39627849358909321, morphtype empty, photometric-join, r/z ratio, backwards

### DAF-05 (BLOCKER): 4 rendered `[placeholder:]` blocks; no resolvable data link; missing DESI acknowledgement
- **class:** PARTIALLY CLOSED
- 2 of 4 already closed in vAF.0.3 (ADS bib verification, acknowledgements). The remaining
  2 (OT-1 injection-recovery experiment, Zenodo DOI) genuinely cannot be executed by this
  lane (GPU compute / DOI minting are out of scope for a text-edit closure) — rewritten
  from raw `[placeholder:]` markup to a fully specified-but-not-executed description (OT-1)
  so a reader can judge the remaining work, per the reviewer's own accepted fallback.
- **fingerprint:** placeholder, OT-1, Zenodo DOI, acknowledgements

### DAF-06 (MAJOR, folded into DAF-01's closure): V1 marked an unqualified "pass" while verifying only 1 of 3 provenance-gate conditions
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: `checked_objtype: False, checked_fiberstatus: False` in the checker's own
  output; only `TARGETID>0` is actually checked. §V E already disclosed the underlying
  schema gap in prose, but Table VI read as an unqualified pass.
- **Closure:** §V A now states V1 is a partial pass, naming which condition survives and
  pointing to §V E. main.tex §V A.
- **fingerprint:** V1 partial, TARGETID>0, objtype fiberstatus not carried

### DAF-07 (MAJOR, title, all 3 legs convergent): title does not carry the paper's own null result
- **class:** CLOSED — GENUINELY-NEW-REAL
- **Closure:** title changed to "...selection, validation, and a null known-object
  recovery benchmark" (was "...a descriptive taxonomy"); no-discovery statement moved to
  the abstract's first sentence. main.tex title, abstract.
- **fingerprint:** title, null, descriptive taxonomy, no discovery

### DAF-08 (MAJOR): "rises with score" / "contamination worsens with score" stated without qualification, false in the sparse top bin
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: Table II bins 99.53/99.68/99.90/99.92/99.97/99.70 — the top [10,24.42] bin is
  lower than [8,10), driven by 337 fibres/1 science target (not significant).
- **Closure:** qualified to "up to S=10, above which the single remaining bin is too
  sparse to constrain the trend" in all 3 summary locations (abstract, §I item 2, §XI).
- **fingerprint:** rises with score, contamination worsens, top bin, 337 fibres

### DAF-09/DAF-10/DAF-11 (MAJOR trio, blue-arm evidence): ρ=0.53 does not support "almost entirely"; ρ(S,r_B) is definitional not independent; the paper's own within-catalogue diagnostics were unused
- **class:** CLOSED — GENUINELY-NEW-REAL, real new computation added
- New committed script `blue_arm_diagnostics_2026-09-19.py` (independently written and
  run by the orchestrator, reproducing the reviewer's numbers exactly): `worst_band`=B for
  1180/1244 (94.9%); regressing `mean_mse` on (rB,rR,rZ) gives R²=0.777, dropping rB
  collapses it to R²=0.006 (dropping rR/rZ leaves 0.609/0.201); ρ(rB,snr_b)=-0.008
  (p=0.78, no SNR dependence); for the 502 ZWARN=0 objects, `peak_residual_wavelength`
  concentrates far more tightly in the observed frame (IQR/median 0.39) than the rest
  frame (0.68) — evidence favouring a fixed-wavelength calibration origin over a genuine
  spectral feature, without closing the question.
- **Closure:** §V C rewritten with the variance decomposition + both new diagnostics;
  abstract/§I/§XI updated to state "almost entirely explained by" with the R² figures
  rather than the bare correlation. main.tex §V C, abstract, §I item 4, §XI.
- **fingerprint:** almost entirely, blue arm, R^2, variance decomposition, worst_band, rest frame

### DAF-12 (MAJOR): benchmark's low statistical power (95% UL 12.5%) stated once in §V D, omitted from abstract/intro/conclusions
- **class:** CLOSED — GENUINELY-NEW-REAL
- **Closure:** power caveat added to all 3 summary locations. main.tex abstract, §I item 5, §XI.
- **fingerprint:** statistical power, 12.5%, recovery benchmark, abstract omission

### DAF-13 (MAJOR): Table VII's BAL enrichment (4.2×) uses the all-TARGETID denominator §II A explicitly rules out
- **class:** CLOSED — GENUINELY-NEW-REAL
- **Closure:** fixed at the generator (`make_draft_figures.py::tab_recovery_benchmark`),
  not hand-edited in the `.tex` table — table now prints 3.3× directly; caption and body
  prose updated to match; single-match wide-interval caveat added (folds NIT-8).
- **fingerprint:** enrichment, 4.2x, 3.3x, science-target denominator, Table VII

### DAF-14 (MAJOR): "the significant ones are negative" is false — the S/N coefficient is significant and positive
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: V10 output ρ(S/N)=+0.058, p=0.039 (significant, positive).
- **Closure:** sentence corrected to state the S/N coefficient separately. main.tex §V B.
- **fingerprint:** significant ones negative, S/N positive, V10

### DAF-15 (MAJOR): matched-object score preference read as "a mild positive signal for the method," confounded by brightness
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: top 6 scores all matched; matched vs. unmatched score medians 3.337 vs. 3.237
  (p=4.5e-5); matched objects also brighter/better-measured (flux_r 0.289 vs. 0.184,
  p=8e-4; snr_r 0.079 vs. 0.046, p=1e-6).
- **Closure:** reframed as confounded, not a positive signal; decisive evidence pointed to
  §V D's recovery-benchmark null instead. main.tex §IV D.
- **fingerprint:** mild positive signal, matched unmatched, confounded, brightness

### DAF-16 (MAJOR): Table IV describes no single released file; several released columns (residual_kurtosis, SUBTYPE) undocumented
- **class:** CLOSED — GENUINELY-NEW-REAL (fully closed 2026-09-21, lane LAF2; was
  PARTIALLY CLOSED as of vAF.0.4)
- `residual_kurtosis` added to the anomaly group; `classification`/`discovery_potential`
  (constant placeholders across all rows) added as an explicit "unpopulated placeholder"
  group rather than silently omitted (vAF.0.4).
- **vAF.0.5 closure:** the remaining 9 columns were identified exactly (not estimated) by
  running `assemble_flagship_evidence.py::build_master()` and diffing its real 192-column
  frame against the schema generator's grouped columns:
  `mean_fiber_ra`, `mean_fiber_dec`, `gr_color`, `rz_color`, `w1w2_color`,
  `is_point_source`, `is_star_candidate`, `crossmatch`, `snr_med`. Their definitions were
  read from the committed `enhanced_18M_inference.py` (colours: AB-mag differences from
  already-released fluxes; `is_point_source`: `morphtype=='PSF'`; `is_star_candidate`:
  parallax>0.5 mas or a `gr_color`/`rz_color` stellar-locus cut) and
  `assemble_flagship_evidence.py` (`crossmatch`: the matched/unmatched join tag;
  `snr_med`: median of the three per-band SNR columns). Added as a new schema group in
  the generator (`make_draft_figures.py::tab_catalogue_schema`, never hand-edited) and a
  documenting paragraph in main.tex §IV A. Table IV caption now reads "all 192 released
  columns accounted for." Full pipeline rerun; every other number (V1–V12,
  DEFECT-1/2/3, all draft_numbers.json values) reproduced identically —
  `n_columns_joined` 183→192 is the only number that changed. main.tex §IV A,
  Table~\ref{tab:schema} caption, `tables/tab_catalogue_schema.tex`.
- **fingerprint:** Table IV, released column schema, residual_kurtosis, discovery_potential, mean_fiber_ra, crossmatch, snr_med, 192 columns

### DAF-17 (MAJOR): dedup rule (`878,740` rows removed) is physically arbitrary and its effect on catalogue membership near threshold is unquantified
- **class:** DISCLOSED, NOT CLOSED (genuinely needs new analysis on raw pre-dedup data)
- **Disposition:** honest caveat added in §II A stating the rule has no physical content
  and the near-threshold effect is unquantified, not asserted small. main.tex §II A.
- **fingerprint:** deduplication, arbitrary, near-threshold, unquantified

### DAF-18 (MAJOR): f_NL paragraph (§VIII) had no citation, no equation, and "more than an order of magnitude" is arithmetically wrong (0.3 dex ≈ factor 2, not >10×)
- **class:** CLOSED — GENUINELY-NEW-REAL
- Found a real, already-committed, cited computation
  (`research/anomaly_map/ledger6_png_highz_abundance.py`, LoVerde et al. 2008 + Planck
  2018 + Eisenstein & Hu 1998) that the paper's own trailing-comment convention already
  pointed to but never surfaced as a visible citation. Independently reproduced the
  6–16% abundance-shift range from its output JSON at logM_h≈11.5, z=10–14.
- **Closure:** paragraph rewritten to define f_NL, name the method/citations, cite the
  script as an `\artifactlink`, and correct "more than an order of magnitude" to the
  true ≈1.06–1.19× factor (well inside, not below, the 0.3 dex floor). Added bibitems
  Labbe2023, BoylanKolchin2023. main.tex §VIII.
- **fingerprint:** f_NL, order of magnitude, LoVerde, ledger6, uncited

### DAF-19 (MAJOR): taxonomy construction — RA-wrap artifact, missing hyperparameters, near-vacuous PCA on 3 features
- **class:** DISCLOSED, NOT CLOSED (a corrected re-clustering is real follow-up work, not a text fix)
- Verified: Table VIII's own RA spans (up to 350°) match the unwrapped-coordinate
  signature exactly.
- **Disposition:** honest limitation paragraph added naming all three issues and the
  exact fix (spherical embedding, stated hyperparameters/seed, a (survey,programme)
  baseline) needed before the taxonomy's specific boundaries are non-provisional; states
  this does not affect the already-weak V12 null. main.tex §VI A.
- **fingerprint:** taxonomy, RA wrap, UMAP HDBSCAN hyperparameters, PCA

### DAF-20 (BLOCKER): archived model's training corpus, wavelength grid, and architecture are undocumented and unhashed
- **class:** DISCLOSED, NOT CLOSED (genuinely absent from every artifact in this repo, confirmed by search)
- Confirmed: `best_model_47k.pt` predates the clean-rerun contract system entirely; no
  training-corpus documentation exists anywhere in `pipelines/p1_highz_tracers/`.
- **Disposition:** honest limitation paragraph added in §III A naming exactly what is
  missing and its two concrete consequences (possible train/scan overlap selection
  effect; a candidate contributor to the blue-arm result) — not fabricated, not silently
  dropped. main.tex §III A.
- **fingerprint:** training corpus, best_model_47k, architecture, unhashed

### DAF-21 (MAJOR, both legs): NED (99% of counterparts), VizieR, AllWISE catalogue, and Redrock used throughout, cited nowhere
- **class:** CLOSED — GENUINELY-NEW-REAL
- **Closure:** added bibitems NED, VizieR (Ochsenbein et al. 2000), AllWISE (Cutri et al.
  2014), Redrock; wired `\cite{}` at each first mention. main.tex §II A, §IV D, follow-up
  tiers.
- **fingerprint:** NED VizieR AllWISE Redrock uncited

### MINOR items closed: 
MINOR-4 (abstract "no material structure" vs. §VI C's own "structured but not
separated" — abstract already fixed as part of DAF-09-11's rewrite), Table V caption
(non-disjoint columns sum to 600, not truncated — all 8/6 types shown), V9's mis-grouping
under "the selection rule" (moved to its own sentence), determinism self-contradiction
("apart from... which is seeded" → "fully deterministic; ... is seeded"), the
mid-infrared-criterion citation (Stern2012 alone for the criterion, WISE separately for
the mission), MINOR-10 (percentile/count corrected to 94.7th/66, folded into DAF-03/04).

### Deferred, non-blocking, not touched this wave:
MINOR-1 (defect-count terminology across §I/§V A/§V E — "four release defects" now used
consistently in abstract/§I/§V E; §V A's DEFECT-1..3 label is a distinct technical ID set,
left as-is), MINOR-2 (13/9/10 artifact-count reconciliation), MINOR-5 (50-draw
permutation null too small), MINOR-6 (σ_MSE stability check), MINOR-7 (Fig. 5 log-axis
off-scale points), MINOR-13's [3] `stag010` pagination (debatable — standard MNRAS
advance-access article-ID style, not clearly an error), MINOR-15 (full 64-hex SHA table),
all 9 NIT items except NIT-8 (folded into DAF-13) and NIT-5 (folded into DAF-20). Gemini
AF-N1 (remove the internal `(vAF.0.4)` version tag from the date line): dispositioned
**OPINION/OUT-OF-SCOPE** — every other paper in this repo (P4P, A3M, PSU, P1N) carries the
same tag by deliberate lab convention for internal tracking; not changed.

---

**Directive R2:** this is round 1 of the two-consecutive-round budget. An R2 board, if
run, should (a) verify these closures on the exact vAF.0.4 PDF and (b) assess whether
DAF-17/19/20's disclosures are sufficient or require the named follow-up work
(dedup-sensitivity quantification, corrected re-clustering, training-corpus archaeology)
before further readiness advance.

---

## LAF2 non-review TODO closure (vAF.0.4 → vAF.0.5, 2026-09-21)

Not a review round — directive R2 stays at round 1 of 2 spent. DAF-16 fully closed (see
its updated entry above). Bibliography verification completed for all remaining 26
entries (all match ADS/journal records, no text changed). OT-1 and Zenodo DOI
reconfirmed genuinely not agent-closable, left unchanged as already honestly specified.
DAF-17/19/20 unchanged (still genuinely open, real further work). Full account in
`project-context/SSOT/paper-af/status.md` §"LAF2 non-review TODO closure". An R2 board,
if run, should verify these closures plus the R1 closures on the exact vAF.0.5 PDF.
