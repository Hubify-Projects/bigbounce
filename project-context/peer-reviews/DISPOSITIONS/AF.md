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

---

## R2 confirmation wave (2026-09-22) — `ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM`

Lane LAF3. Directive R2 authorized exactly one confirmation board because vAF.0.5 (this
round's exact target) had never been reviewed: R1 ran on vAF.0.2/vAF.0.3, and lane LAF2
then closed real items and bumped twice (vAF.0.3→vAF.0.4→vAF.0.5) without an intervening
board. Directive-G pre-check on vAF.0.5 PASS before dispatch: fresh 4-pass recompile
0 errors/0 undef refs/0 overfull >10pt/18pp, `pdftotext` byte-identical to the served
build (the raw PDF md5 differs only in pdflatex's embedded build timestamp), and all 5
served paths md5-matched at `60de7e9dbfbcc77336b3050ee788e68e`. Convex arm UNAVAILABLE
(spending limit) — no board-registration mutation possible; queued below.

**Board:** Grok API `grok-4.3` + Gemini API `gemini-3.1-pro-preview`
(`tools/v3_native_pdf_review.py`, `ApJS-CATALOG` profile — the paper's own registered
profile, a catalogue+data-release referee stance) + one Claude-opus verdict-blind
referee (INT leg, dispatched as a separate sub-agent with no access to the other two
legs' reports), all against the exact vAF.0.5 PDF (sha256 `ea81ef41...`). Fable was not
attempted for this leg — the lane brief authorizes opus directly for non-flagship INT
legs. Raws saved and read in full before any verdict recorded:
`project-context/peer-reviews/ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM_AF_Grok_brutal.md`,
`..._AF_Gemini_cosmology.md`,
`project-context/peer-reviews/INT_v3/ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM/AF_vAF.0.5_CONFIRM_claude_opus.md`.

**Verdicts (words diagnostic only, per directive H):** Grok REJECT (4 ESSENTIAL, 4
MAJOR, 4 MINOR/NIT). Gemini MAJOR REVISIONS (4 ESSENTIAL, 4 MAJOR, 2 MINOR/NIT).
Claude-opus MAJOR REVISIONS (5 ESSENTIAL, 19 MAJOR, 14 MINOR, 6 NIT). All three legs
independently converged on the flux-to-magnitude arithmetic error and the missing
LoVerde/Eisenstein-Hu/Planck citations; opus additionally caught a genuinely-new,
higher-value statistical-attribution error the other two legs did not (DAF-22 below).

**Orchestrator verification method (before any closure):** every ESSENTIAL/BLOCKER-tier
finding was independently re-derived from the exact main.tex source and, where a
released-data claim was involved, from the committed parquet files directly (not
accepted from reviewer text alone) — a new committed script,
`flagship_assembly_2026-09-18/scripts/confirm_round_2026-09-22.py`, reproduces two of the
closures below (the blue-arm univariate R² and the score-vs-redshift Spearman test) from
`clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2{,_enriched}.parquet`.

### DAF-22 (ESSENTIAL, Claude-opus only — genuinely new, most consequential): abstract/§I/§XI claim "it alone accounts for R²=0.78" conflates the full three-camera regression's R² with the blue arm's own univariate R²
- **class:** CLOSED — GENUINELY-NEW-REAL
- Independently verified: §V C's own body text already correctly reports the full-model
  regression (`mean_mse ~ r_B+r_R+r_Z`, R²=0.777) and the drop-one-collapses-to-0.006
  result — that arithmetic was never wrong. But three summary locations (abstract, §I
  item 4, §XI) simplified this to "it [the blue arm] alone accounts for R²=0.78,"
  which is a different, previously uncomputed quantity: a univariate regression of
  `mean_mse` on `r_B` alone. Computed fresh (`confirm_round_2026-09-22.py`): R²=0.198
  for `r_B` alone (0.001 for `r_R`, 0.004 for `r_Z`) — roughly a factor of 4 below the
  0.78 figure the summary locations attributed to it alone.
- **Closure:** all three summary locations rewritten to state both numbers explicitly
  and distinguish them ("the full three-camera regression explains R²=0.78 ... and
  collapses to R²=0.01 when it is dropped, while it alone, univariately, explains
  R²=0.20"); §V C gains one paragraph naming the confirmation board and stating why the
  two numbers are not interchangeable. No conclusion changes — the blue arm still
  dominates the score by every measure — but the specific number attributed to "the blue
  arm alone" is now the one actually computed for that quantity. main.tex abstract, §I
  item 4, §V C, §XI.
- **fingerprint:** R^2=0.78, it alone, univariate, blue arm, drop rB, full model

### DAF-23 (ESSENTIAL, all 3 legs convergent): §VII.B flux-to-magnitude conversion "≈20.6 AB mag" is arithmetically wrong
- **class:** CLOSED — GENUINELY-NEW-REAL
- Independently recomputed: $m = 22.5 - 2.5\log_{10}(4.33) = 20.91$, not $20.6$. Does not
  change the physical conclusion (still far too bright for the claimed dropout).
- **Closure:** corrected to "≈20.9 AB mag" with the formula shown inline. main.tex §VII.B.
- **fingerprint:** 20.6 AB mag, flux to magnitude, 4.33 nmgy, 22.5

### DAF-24 (ESSENTIAL, all 3 legs convergent): §VIII names LoVerde et al. 2008, Eisenstein & Hu 1998, and Planck 2018 in prose with no bibliography entry
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: none of the three had a `\bibitem`/`\cite` in vAF.0.5, despite the paper's
  own stated standalone-reader-test standard (already applied to NED/VizieR/AllWISE in
  DAF-21).
- **Closure:** three new bibitems added, `\cite{}` wired at first mention. The two also
  cited in the same paragraph (Labbé 2023, Boylan-Kolchin 2023, added by DAF-18) were
  already present. main.tex §VIII, bibliography.
- **fingerprint:** LoVerde, Eisenstein Hu, Planck 2018, uncited, f_NL abundance

### DAF-25 (ESSENTIAL, Gemini + Claude-opus convergent): §VII.B "we no longer report one of them as supported" is leftover version-history language
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified: the phrase is literal in vAF.0.5, referring to the R1-wave downgrade
  (DAF-03/04) rather than describing the current analysis.
- **Closure:** removed; the sentence now states the current classification directly with
  no reference to a prior draft. main.tex §VII.B.
- **fingerprint:** no longer report, supported, version history, previous draft

### DAF-26 (MAJOR, Claude-opus): §IV.C morphology census (441 PSF + 316 REX + 406 empty = 1,163) does not reach the released 1,244
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified against `draft_numbers.json::morphtype_counts`: the missing 81 are EXP (61),
  SER (14), DEV (6); all six values sum to 1,244 exactly.
- **Closure:** the three missing categories added to the sentence, with an explicit
  sum-check clause. main.tex §IV.C.
- **fingerprint:** morphology census, 441 PSF, 316 REX, unaccounted, 81 objects

### DAF-27 (MAJOR, Claude-opus): "A referee should read V10 as..." addresses a referee directly inside the manuscript body
- **class:** CLOSED — GENUINELY-NEW-REAL
- **Closure:** reworded to address the reader generically ("V10 should be read as...").
  main.tex §III B.
- **fingerprint:** referee should read, V10, addressing referee

### DAF-28 (MAJOR, Claude-opus): Appendix A's bibliography-verification arithmetic (4 + 26 = 30) does not reconcile with the actual 34-entry (now 37) bibliography
- **class:** CLOSED — GENUINELY-NEW-REAL
- Verified by direct enumeration of every `\bibitem` key: 3 entries are disclosed
  non-journal citations correctly excluded from ADS checking (Redrock in-prep,
  DESIBitmasks, ApacheArrow); 5 entries (Labbé 2023, Boylan-Kolchin 2023 added
  2026-09-21; LoVerde 2008, Eisenstein & Hu 1998, Planck 2018 added 2026-09-22 by
  DAF-24 above) postdate the 2026-09-21 ADS sweep and were not part of it.
- **Closure:** the verification paragraph rewritten to name all four categories
  explicitly (ADS-verified, disclosed-non-journal, post-sweep-additions) instead of
  asserting two counts that silently didn't sum to the total; the 5 post-sweep entries
  are honestly flagged as stated at the author's domain-knowledge confidence, not a
  fresh ADS lookup, with a live check left open. main.tex Appendix A.
- **fingerprint:** 4+26, bibliography count, does not reconcile, 34 entries

### DAF-29 (ESSENTIAL, Gemini; substance is a re-flag of DAF-19, but the specific abstract-scoping gap is new): abstract's "complete provenance chain needed to reproduce it" reads as contradicted by §VI.A's own "not reproducible from the released files alone"
- **class:** CLOSED — GENUINELY-NEW-REAL (presentational scope, not new substance)
- The underlying fact (UMAP/HDBSCAN hyperparameters unrecorded) is DAF-19, already
  disclosed and correctly left open (needs a corrected re-clustering, not a text fix).
  What is new here is that the abstract's own reproducibility claim was unscoped enough
  to read as a blanket promise the taxonomy subsection immediately contradicts.
- **Closure:** abstract sentence scoped precisely to what is reproducible (the catalogue
  selection: score, provenance gate, threshold), with an explicit forward pointer to the
  taxonomy's own disclosed limitation. DAF-19 itself is unchanged and still open.
  main.tex abstract.
- **fingerprint:** complete provenance chain, contradiction, not reproducible, hyperparameters

### Findings FALSIFIED against source (not real):
- **Grok AF-E1** ("the paper never states the effect size of the null result"): FALSE —
  the abstract already states "95% upper limits up to 12.5% recovery for the rarest
  class" verbatim, and Table VII already gives the 3.3× BAL enrichment.
- **Grok AF-M3** ("95% ULs should be per-class, not only aggregate"): FALSE — Table VII
  already reports a per-class Wilson 95% CI for all five reference classes (0.107% to
  12.456%); the "12.5%" in the abstract is the worst (SLSN) class's own per-class UL.
- **Grok AF-E4** (partial): "the landing receipt date post-dates the paper date" is
  backwards — `PHASE3_V2_LANDING_2026-09-03.md` is dated 18 days *before* the paper
  (September 21/22, 2026), not after.
- **Grok/Gemini/opus "double punctuation" and typo claims on `\item[Refuted.]`-style
  labels**: the *source* had no double punctuation; the *rendered PDF* did — revtex's
  `description` environment appends its own colon after a bracketed label, so a label
  ending in "." rendered as "Label.:". CONFIRMED as a real rendering defect once checked
  against the rendered PDF (not the source diff) and closed by removing the 7 redundant
  in-bracket periods across `\item[Refuted]`, `\item[Undecidable from the release]`, and
  the five `\item[OT-N ...]` labels. Logged here rather than as a numbered DAF because it
  is presentational, not a factual/scientific claim.
- **Grok AF-N4** ("5.7×10⁻⁵ should be 5.71×10⁻⁵ for consistency with the body"): FALSE —
  all three occurrences (abstract, §II, §IX) already read "5.7×10⁻⁵" identically; there
  is no inconsistency to fix.

### Re-flags of already-disclosed content (not genuinely new, no change):
- **Grok AF-E2/AF-M4, Claude-opus AF-E1/E2** (taxonomy is a non-physical stratification;
  Family 0 spans 350° RA): re-flag of DAF-19, already DISCLOSED-NOT-CLOSED, unchanged.
- **Grok AF-E4 (DOI half), Gemini finding 4** (Zenodo DOI placeholder): re-flag of
  DAF-05, Houston-only, unchanged.
- **Claude-opus** ("vAF.0.5 on the title page" internal version tag): re-flag of R1's
  Gemini AF-N1, dispositioned OPINION/OUT-OF-SCOPE (deliberate lab-wide convention
  across all papers), unchanged.

### Genuinely real, honestly left open (not closable this wave without fabricating a threshold or an uncited physical claim):
- **DAF-30 (Grok AF-M2):** no quantitative statement of how much of the released
  catalogue a "simple blue-arm quality cut" would remove — real ask, but no such cut is
  defined anywhere in the release; computing one now would require inventing a threshold
  never pre-declared, which `/never-fabricate-derivation` forbids. Left as a named
  follow-up for whoever defines and pre-registers a cut.
- **DAF-31 (Gemini finding 6):** the "far shallower than a Gunn-Peterson trough at
  z≈6 would produce" claim (§VII.B) has no cited expected $f_z/f_r$ ratio. A real,
  literature-sourced number is needed (e.g. from a GP-trough transmission model); this
  lane does not have a live literature-search path it can respectably attach a citation
  from without risking an uncited or misremembered physical claim, so it is left as a
  named gap rather than guessed.
- **Gemini finding 8** (MINOR): the "orders of magnitude above any plausible noise
  floor" claim in §VII.B is not given a numeric noise-floor value. Same reasoning as
  DAF-31 — deferred rather than guessed, non-blocking.

### OPINION/OUT-OF-SCOPE (editorial/venue, per directive R2's genre-length-venue guidance):
Grok AF-M1 (recommend cutting to 10-12pp — a venue/length call, Houston-gated if ever
pursued, not a correctness defect); Grok AF-N1 (the "future" date header — same
deliberate lab-wide dating convention as every other current paper, already the subject
of R1's Gemini AF-N1 disposition); Grok AF-N3 (minor "sky/non-science" vs. "non-science
fibres" terminology drift — cosmetic, deferred non-blocking in the same class as R1's
MINOR-1).

**Directive-G bundle:** `\paperVersion` vAF.0.5→vAF.0.6; `\paperTimestamp` September
21→22, 2026. 4-pass `pdflatex`, 0 errors, 0 undefined refs/citations, 0 overfull hboxes
>10pt, 18 pages (unchanged — additive sentence-level edits, no padding).
`/latex-audit` full visual pass on all 8 touched pages (1, 2, 5, 6, 7, 13, 15, 17) plus
the OT-list page (14) after the description-label fix — no overflow, no overlap.
`/artifact-link-verify`: all 6 GitHub `\artifact{}`/`\artifactdirlink{}` links (extracted
from the compiled PDF's link annotations, not guessed from the source) resolve on `main`,
unchanged. Standalone tarball-style compile (`.tex` + `figures/` + `tables/` only, no
other source files) reproduces the served build's text byte-for-byte identically
(4-pass, 0 errors, 0 undef refs, 18pp); discarded after the smoke test per protocol.
5-way md5-verified mirror (source dir, `site/public/papers/` versioned+alias,
`public/papers/` versioned+alias) at `47fca3cb5d827518aebde7499b8dc810`.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `47fca3cb5d827518aebde7499b8dc810`, SHA-256
  `e3099173d5f0f96ac3d179a3a16abf0c7a14dc043bfb4626c8609ed4560365b2`.
- **New committed script:**
  `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/confirm_round_2026-09-22.py`
  → `pipelines/p1_highz_tracers/anomaly_flagship_draft/outputs_blue_arm/confirm_round_2026-09-22.json`.
- **Convex:** DISABLED — intended mutations queued to
  `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
- **Readiness:** 77→80, COMPUTED by the author's own reasoning against the directive-P
  components (no automated calculator exists for this draft-registry paper): a real,
  independently-verified science-attribution correction (DAF-22) plus 8 further real
  closures raise evidence/reproducibility and science-closure quality, but "automated
  review convergence" earns no additional credit this wave — the board found genuinely-
  new-real items (not a clean confirmation) and 2 new items (DAF-30/31) join the 3
  pre-existing disclosed-open items (DAF-17/19/20) plus OT-1 and the Zenodo DOI as still
  open. This is a reasoned estimate, not a Convex-computed value (Convex disabled);
  flagged as such for the director to reconcile once Convex is restored.

**Result: AF is NOT CONFIRMED on this pass.** A real board ran on the exact vAF.0.5 PDF,
found real items across all three legs (most consequentially DAF-22, a genuine
statistical-attribution error the R1 board never had the chance to catch since it
concerned language introduced only at vAF.0.4), and closed the substantial majority with
real edits or new, independently-verified computation. Per the no-re-board rule, this
round does not re-test the new vAF.0.6 PDF. **Directive R2: round 2 of 2 spent — no
further board on paper-af without an intervening science/scope decision** (e.g., landing
OT-1's GPU compute, a corrected re-clustering for DAF-19, or Houston's Zenodo DOI).
