# INT REFEREE REPORT — AF (anomaly flagship)

| field | value |
|---|---|
| Paper tag | **AF** |
| Round label | `ROUND_2026-09-19-AF-vAF.0.2-EXACTPDF-b972d890-R1` |
| Reviewer | **claude-opus (INT leg, verdict-blind)** |
| Exact PDF | `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` |
| SHA-256 (verified by me, `shasum -a 256`) | `b972d890cf5b907eec0a7bf614dac5ba5647502efe3ee907533e4b3f96dd4cba` |
| PDF properties | 15 pages, letter, pdfTeX-1.40.29, built 2026-09-19 00:08:31 PDT |
| Version string on page 1 | `(Dated: September 19, 2026 (vAF.0.2))` |
| Date of review | 2026-09-19 |
| Board position | one of three legs (Grok API, Gemini API run separately); no access to their reports |
| Disposition history shown to me | none (verdict-blind; paper's first review board) |
| Target venue assumed | ApJS, catalogue/data-release article |

**Verification method.** I read the rendered PDF in full (`pdftotext -layout`), rendered pages 3, 10 and 11 as images to inspect Figs. 1, 7, 8 and 9 and Tables I, II, VIII, IX, XI, and independently recomputed the paper's quantitative claims against the committed artifacts:

- `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/outputs/draft_numbers.json`
- `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/outputs/validation_contract_results.json`
- `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/outputs/provenance_recheck_2026-09-18.json`
- `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2.parquet`
- `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet`
- `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_{matched,unmatched}.parquet`
- `pipelines/p1_highz_tracers/anomaly_flagship_draft/REPRODUCIBILITY_MANIFEST.md`, `main.log`

Every finding below is anchored to text, a table, or a figure in *this* PDF, and where I make a counter-claim I give the number I computed and the file I computed it from.

---

## 1. Overall recommendation

# MAJOR REVISIONS

This is a serious, unusually honest piece of data-release work and the arithmetic inside its tables is, as far as I can check it, exact — I recomputed roughly forty quoted quantities and the tables themselves did not produce a single error. But the manuscript is not currently refereeable on its merits, for three independent reasons:

1. **The paper mis-states the outcome of its own validation contract** (§V A: "Thirteen requirements pass"; the released checker returns **eleven**). In a paper whose entire claim to novelty is machine-checkable validation, this is the one error that cannot be tolerated.
2. **Table I's caption asserts a provenance verification that the released checks do not perform** (all thirteen re-hashed against the landing receipt; V2's own output says 9/9).
3. **The §VII B photometric result — one of only two concrete outcomes in the paper and half of one abstract sentence — rests on a row the paper itself classifies as a photometric-join defect, and applies only half of its own stated test.** As currently written, "the released Legacy Survey photometry already refutes one and supports one" is not supported by the released photometry.

None of these is fatal in principle: (1) and (2) are corrections to text, and (3) is a ten-minute public query (Legacy Survey DR10 forced photometry with inverse variances) that the paper already identifies as the next step. But the paper cannot be accepted until they are fixed, and if the authors cannot resolve BLOCKER-3/BLOCKER-4 with clean forced photometry, §VII B and its abstract sentence must be **withdrawn entirely** rather than softened — which would move my recommendation toward reject.

On the three focus questions the authors flagged: **(1) No — the title does not carry the null** (MAJOR-1). **(2) The blue-arm origin is neither overstated nor understated, it is under-analysed** — the paper defers the question to an external test (OT-3) while the decisive first-order diagnostics sit unused in its own released columns (MAJOR-4, MAJOR-5). **(3) Yes, the low power is undersold** — it is stated correctly once in §V D and omitted from the abstract, the introduction's contribution list, and the conclusions (MAJOR-6).

---

## 2. BLOCKER findings (must fix before this can be refereed on its merits)

### BLOCKER-1 — §V A, p. 6, first sentence of the paragraph after Table VI is invoked: "Thirteen requirements pass." This is false; eleven pass.

**Claim.** §V A: *"Thirteen requirements pass. V11 and DEFECT-3 are reported quantities rather than thresholds. V12 returns structured-but-weak … DEFECT-1 and DEFECT-2 fail by design."*

**Why it is wrong.** Count the `Outcome` column of Table VI (p. 8) yourself: `pass` appears on V1, V2, V3, V3b, V4, V5, V6, V7, V8, V9, V10 — **eleven rows**. The remaining five are V11 `reported`, V12 `structured-but-weak`, DEFECT-1 `fail`, DEFECT-2 `fail`, DEFECT-3 `reported`. The released checker agrees exactly: `validation_contract_results.json` carries `"n_checks": 16` with statuses `PASS ×11, REPORTED ×2, STRUCTURED-BUT-WEAK ×1, FAIL ×2`.

The sentence is also internally impossible as written: it names V11 and DEFECT-3 as *additional* to the thirteen, which with V12 + DEFECT-1 + DEFECT-2 would require 18 requirements in a contract of 16.

**Why it matters at blocker level.** This paper's central contribution is that its claims are machine-checkable. The first number a referee will check is the pass count, it is stated in the abstract's terms ("a published contract of sixteen machine-checkable requirements"), and it is wrong by two. No reader will extend trust to the other fifty numbers after finding this one.

**Fix.** "Eleven requirements pass." Then state the remaining five explicitly by ID and outcome. Consider adding a summary line to Table VI's caption (`11 pass / 2 reported / 1 structured-but-weak / 2 fail by design`) generated from the JSON so it cannot drift again.

---

### BLOCKER-2 — Table I caption, p. 3: "Every artifact is re-hashed at publication time and compared against the landing receipt; all thirteen match (checks V2 and V3)." The cited checks do not establish this.

**Claim.** Table I lists thirteen artifacts (DR1 zcatalog, run contract, archived model, inference code, and nine released data products) and its caption asserts all thirteen were re-hashed at publication time and matched against the landing receipt, on the authority of V2 and V3.

**Why it is wrong.** From the released checker output:

- **V2** observed: `"9/9 artifacts match"`. V2's requirement text in Table VI is *"every **released artifact's** SHA-256 equals the value in the landing receipt"* — nine artifacts, not thirteen. This is consistent with §II B's own "the nine released data products".
- **V3** observed: `"8/8 links verified; contract=6699d09ff886…, model=f5266ba48f47…, zcatalog=2d95ad993610…"`. V3's requirement says these hashes are **"recorded"**, not re-verified against a landing receipt. Recording a hash in a manifest is not the same operation as re-hashing the artifact and comparing.
- The **inference-code** hash (`3e7efb243fa5cc4e…`, row 4 of Table I) appears in neither V2's nine nor V3's three named hashes. On the evidence in the release it is covered by nothing.
- `provenance_recheck_2026-09-18.json` — the only artifact in the deposit that actually records a publication-time re-hash — contains exactly **two** entries (`flagship_sample_v2.parquet`, `flagship_sample_v2_enriched.parquet`).

So the strongest defensible statement is: nine artifacts receipt-verified, three manifest-recorded, one unaccounted for. The caption claims thirteen re-hashed and matched.

**Why it matters at blocker level.** This is the single sentence that carries the word in the title ("provenance-sealed"). An ApJS referee who checks it and finds it overstated has no basis for trusting the rest of the provenance apparatus, which is the paper's reason to exist.

**Fix.** Rewrite the caption to say exactly what was done to each row, e.g. *"Nine released data products were re-hashed at publication time and matched against the landing receipt (V2); the run contract, archived model and parent zcatalog hashes are recorded and chain-bound under V3; the inference-code hash is recorded in the run contract."* Then either extend the publication-time re-hash to the remaining four artifacts (trivial for the contract, model and code; the zcatalog is large but hashable once) and restore the stronger claim, or leave the weaker claim standing. Adding a `verified_by` column to Table I (`V2` / `V3-recorded`) would make this self-documenting.

---

### BLOCKER-3 — §VII B, p. 11, "Supported." paragraph, and abstract line "the released Legacy Survey photometry already refutes one and supports one." The "supported" candidate is a photometric-join-defect row, and the paper does not say so.

**Claim.** §VII B: *"**Supported.** TARGETID 39627849358909321 (z = 4.334) carries f_g = −0.019 nmgy, consistent with zero and in the 0.8th percentile of the catalogue, with f_r = 0.886 nmgy … This candidate passes the cheap test and is the one worth spectroscopy."* The abstract elevates this to "…refutes one and supports one."

**Why it is wrong.** I pulled that object's row out of `flagship_sample_v2_enriched.parquet`:

```
targetid          morphtype  flux_g     flux_r    flux_z   flux_w1  flux_w2  sersic  shape_r
39627849358909321  ""        -0.019273  0.886495  0.28591  0.0      0.0      0.0     0.0
```

`morphtype` is **empty**, and `flux_w1 = flux_w2 = sersic = shape_r = 0.0` exactly. This is precisely the defect the paper itself names in §IV C, p. 4: *"406 rows carrying an empty MORPHTYPE — a gap in the photometric join that the deposit must close."* The association is essentially perfect: of the 407 rows with `flux_w1 == 0.0` exactly, **406** also carry an empty `MORPHTYPE`, and 363 rows carry `flux_g = flux_r = flux_z = flux_w1 = 0.0`. Empty morphtype is the signature of an incomplete Legacy Survey join, and the "supported" candidate is inside that set.

The asymmetry in the paper's treatment makes this worse. Two paragraphs earlier, for the refuted object, the paper adds *"and its morphology is SER rather than point-like"* as a supporting strike. For the supported object it never discloses that there is no morphology at all, that both WISE fluxes and both shape parameters are hard zeros, and that this row is one of the 406 the paper elsewhere says must be repaired before deposit.

**Why it matters at blocker level.** One half of one abstract sentence — the only positive outcome the paper reports — is derived from photometry the paper itself classifies as defective. A referee who cross-checks the deposit will find this in five minutes, and it reads as selective disclosure even if it is an oversight.

**Fix.** (a) State explicitly in §VII B that this candidate falls in the 406-row photometric-join gap, and report which of its photometric quantities are real measurements and which are join artefacts. (b) Re-derive the result from a Legacy Survey DR10 forced-photometry query with inverse variances — the paper already names this as the immediate next step for the other two candidates, so run it for all four and replace §VII B's flux table wholesale. (c) Until (b) is done, **downgrade "Supported" to "Undecidable"** and remove "supports one" from the abstract. A g-band non-detection is in any case a necessary, not a sufficient, condition (see BLOCKER-4).

---

### BLOCKER-4 — §VII B / Fig. 9, p. 11: the paper states a two-band break test, then executes only the g-band half, and the r- and z-band fluxes it prints contradict its own verdicts.

**Claim.** §VII B sets up the test as: *"…the Legacy Survey g band (≈4000–5500 Å) is fully blueward of the break for all four, and the r band (≈5500–7000 Å) for the three at z > 4.5."* Fig. 9's caption then reduces it to: *"A Lyman break at the pipeline redshift requires f_g to vanish in every panel."*

**Why it is wrong.**

1. **The r-band criterion is never applied to two of the three objects it covers.** The committed artifact agrees with the text: `draft_numbers.json → ft_a` sets `"r_band_fully_blueward_of_break": true` for both z ≈ 6.07 candidates and for the z = 5.19 candidate. Yet the r-band flux is discussed only for the refuted object. The two "undecidable" candidates carry `flux_r = 0.2546` and `0.3296` nmgy — **comparable to or larger than their g fluxes** (0.283, 0.296; the artifact's own `flux_g_over_flux_r` = 1.11 and 0.90) — in a band the paper says must also go dark. That evidence is printed in Fig. 9 and discussed nowhere.

2. **The z-band colours are inconsistent with the redshifts the paper leaves standing.** For the two z ≈ 6.07 candidates, `flux_z` = 0.446 and 0.470, giving f_z/f_r = 1.75 and 1.42 — a far shallower break than a z ≈ 6 quasar with a Gunn–Peterson trough can produce, where r should be effectively zero and z should carry the whole continuum.

3. **The same test, applied symmetrically, undercuts the "supported" object.** TARGETID 39627849358909321 at z = 4.334: f_r = 0.886, f_z = 0.286, i.e. **r brighter than z by a factor 3.1**. For a quasar at that redshift, ~66% of the r band lies blueward of the 6484 Å break and is forest-absorbed, while the z band is unabsorbed continuum on a spectrum whose f_ν rises to the red — so the expected ordering is f_r ≲ f_z, not f_r ≈ 3 f_z. The observed colour is backwards for the solution the paper says is supported.

4. **The logic is not closed in either direction.** The paper's stated reason for declaring two candidates undecidable is the absence of `FLUX_IVAR` (confirmed: `has_flux_ivar_columns: false`). But that same absence applies to the "supported" object's f_r = 0.886 and f_z = 0.286. Either the ~0.3 nmgy level is a detection — in which case the two z ≈ 6 candidates are **refuted by their r fluxes**, not undecidable — or it is noise, in which case the "supported" object's f_z is noise too and its break is undemonstrated. The paper takes the first reading for one object and the second for two others without stating a criterion.

**Fix.** Apply the test to every band that the break makes predictive, for every candidate, in one table: for each object give the bands fully blueward, the bands straddling, the bands fully redward, and the measured flux with an uncertainty. A Lyman-break test requires **both** a dropout blueward **and** a detection redward; the paper currently checks only the first and only in one band. Then state a single, explicit detection criterion and apply it uniformly. This will almost certainly require the DR10 forced photometry of BLOCKER-3, which is the right outcome.

---

### BLOCKER-5 — four unresolved `[placeholder: …]` blocks are rendered in the submitted PDF, one of which admits four references are unverified; and no resolvable data link exists anywhere in the paper.

**Locations.** §VII C OT-1, p. 13; §IX, p. 13; Acknowledgments, p. 14; Appendix A, p. 14.

**Claim / problem.** The rendered PDF contains, verbatim:

- p. 13, inside numbered open test OT-1: `[placeholder: run and report per-class injection recovery with the exact model and substrate named]`
- p. 13, §IX: `[placeholder: Zenodo DOI for the public deposit]`
- p. 14: `[placeholder: DESI collaboration and facility acknowledgements; SIMBAD/NED/VizieR service acknowledgements; compute acknowledgement]`
- p. 14, Appendix A: `[placeholder: final bibliography verification pass against ADS before submission. The five recovery-benchmark reference-class citations (Refs. [17–21]) are taken verbatim from the committed benchmark artifact, except the journal/volume/page of Ref. [19], which the artifact does not carry; the software citations (Refs. [25, 26, 28]) are not recorded in any committed artifact either. Verify those four before submission.]`

Compounding this, §IX's data-availability statement gives **no resolvable identifier of any kind**: it names repository subdirectories (`results_2026-08-07/phase3_v2`, `flagship_assembly_2026-09-18`) and says mirrors exist "on Hugging Face and Backblaze B2", with no URL, no accession, no DOI. The Zenodo DOI is the placeholder above.

**Why it matters at blocker level.** (a) The manuscript openly tells the referee that four of its references are unverified. (b) The DESI collaboration acknowledgement and data-rights statement are a **policy requirement** for any DR1 publication, not a courtesy. (c) A paper whose sole contribution is reproducibility currently offers a reader no way to obtain a single one of the thirteen hash-bound artifacts. Every claim in §IX ("Stage B … runs on a laptop CPU in under 60 s") is unexercisable as published.

**Fix.** Resolve all four placeholders. Mint the Zenodo DOI and put it in the abstract as well as §IX. Add the full DESI, SIMBAD, NED, VizieR and Legacy Survey acknowledgement text. Either run the OT-1 injection experiment or convert OT-1 into prose that states what would be run (its current form is a note-to-self inside a numbered result). Complete the ADS verification pass — I checked the bibliography independently and it is in better shape than the placeholder implies (see Strength 5), but the authors must confirm it, not the referee.

---

### BLOCKER-6 — §III A, p. 2: the archived autoencoder's training corpus, architecture and wavelength grid are specified nowhere, in the paper or the manifest, and the training set is not hash-bound.

**Claim.** §III A: *"Spectra are scored by an archived autoencoder frozen for this run. The input is a per-spectrum median-absolute-flux-normalised 496-bin resampling; the encoder compresses it to 128 latent dimensions…"* Table I hash-binds the model weights `best_model_47k.pt`. §IX: *"retraining from scratch is not part of this reproduction path."*

**Why it is wrong / incomplete.** The following are absent from the PDF *and* from `REPRODUCIBILITY_MANIFEST.md` (I grepped it for `train`, `47k`, `wavelength`, `496`; the only hits are the weights file name and hash and the note that retraining is out of scope):

- **What the 47k training spectra were.** Parent survey, data release, target classes, selection, any quality cuts. The file name implies 47,000 spectra; the paper never says 47,000 of what.
- **Whether the training spectra are inside the 21,793,550 scored science targets.** If they are — and for a DESI autoencoder this is the likely case — then ~47k objects in the parent carry artificially low reconstruction error because the model memorised them. That is a selection effect operating directly on the quantity that defines the catalogue, and the paper says nothing about it.
- **The wavelength grid of the 496 bins**, and how many bins fall in each of the b/r/z cameras. This is not cosmetic: it is the first thing a referee needs in order to judge §V C's blue-arm result (see MAJOR-5). If the b arm contributes disproportionate bins, or if median-absolute-flux normalisation amplifies the low-throughput blue end, then `ρ(S, r_B) = +0.53` is partly an artefact of the loss construction.
- **The architecture.** "Convolutional" appears in the abstract and nowhere else. No layer count, kernel sizes, activations, bottleneck construction, or loss definition beyond "mean squared reconstruction error".
- **A hash for the training set.** Table I binds the weights but not the data that produced them, so the chain the paper calls sealed has an unsealed root.
- **Whether the 200 calibration groups / 40,000 calibration+validation spectra were excluded from the scan.** If (µ_MSE, σ_MSE) were fit on spectra that are also in the scored population, the standardisation is partly in-sample.

**Why it matters at blocker level.** For a candidate catalogue, the model *is* the selection function. A paper titled "provenance-sealed" cannot leave its single most important input undescribed, unhashed, and explicitly out of the reproduction path. This is also the root cause of OT-1: no injection–recovery experiment can be interpreted without knowing what the model saw.

**Fix.** Add a subsection (or appendix) giving: the training corpus and its selection, its SHA-256 or its own archival identifier, the wavelength grid with per-camera bin counts, the architecture and loss, and an explicit statement of the overlap between training/calibration spectra and the 21.8M scored population — with the number of released objects that were in training. Add the training-set hash to Table I.

---

## 3. MAJOR findings

### MAJOR-1 — Title, p. 1. The title does not carry the null. *(Direct answer to the authors' focus question 1: no, it does not.)*

**Current title.** *"A provenance-sealed anomaly-score candidate catalogue of DESI DR1 spectra: selection, validation, and a descriptive taxonomy."*

**Why this is a problem.** The paper's own load-bearing result — the failed known-object recovery benchmark and the resulting decision to report this as a data release and not a discovery — appears nowhere in the title. Three of the title's content words ("anomaly-score", "candidate catalogue", "taxonomy") are precisely the words a reader scanning an ApJS table of contents will read as *a catalogue of anomalies with a classification scheme*. "Candidate" is doing all of the hedging, and it is the weakest word available: every catalogue of this kind calls its entries candidates. "Descriptive taxonomy" is honest but its force depends on §VI C, which no title-scanner reads.

This matters more than usual here because the paper is explicitly written to resist over-reading (§VIII: "the temptation to over-connect a candidate list to a cosmological question is exactly what a provenance-first release exists to resist"). The title is the one surface where that resistance is absent, and the title is what gets cited, indexed, and quoted second-hand.

**Fix.** Put the null in the subtitle. Options, in decreasing strength:
- *"…: selection, validation, and a null known-object recovery benchmark"*
- *"…: selection, a validated contract, and no recovered anomaly class"*
- *"…: a validated selection with no recovered known-object class"*

I would also add "no discovery is claimed" or equivalent to the **first** sentence of the abstract rather than the seventh. At present the abstract's opening is "We publish a machine-flagged candidate catalogue of spectroscopically unusual objects…", and the no-discovery statement arrives after eight numbers and three results.

---

### MAJOR-2 — Abstract, p. 1; §I contribution 2, p. 1; §XI, p. 14: "that fraction rises with score" / "the contamination worsens with score" is stated without qualification and is false in the top bin.

**Claim.** Abstract: *"above S = 3, more than 99.5% of raw fibres in every score bin are sky or non-science fibres, **and that fraction rises with score**."* §I item 2: *"…**and the contamination worsens with score**."* §XI: *"…**and the contamination worsens with score**."*

**Why it is wrong.** Table II, p. 3: the bins run 99.53, 99.68, 99.90, 99.92, **99.97**, **99.70**. The top bin [10, 24.42] is *lower* than [5,6), [6,8) and [8,10). Fig. 1's top panel (p. 3) shows this drop plainly — the curve rises to a peak at [8,10) and then falls. §III B states the exception correctly and honestly (*"…to 99.97% in [8,10); the sparsely populated top bin (337 fibres, one science target) sits at 99.70%"*), and Fig. 1's caption carefully stops at [8,10). **Three summary locations state the unqualified version, and those are the three places most readers will stop.**

Note also that the monotonic run is driven by bins containing 24, 18 and 1 science targets; the Wilson interval on 99.70% from 337 fibres is wide enough that the top-bin "drop" is itself not significant. The honest statement covers both directions.

**Fix.** In all three summary locations: *"…and rises with score up to S = 10, above which the single remaining bin is too sparse to constrain (337 fibres, one science target)."* Or drop the monotonicity claim from the summaries entirely — the >99.5% floor is the transferable result and it needs no trend.

---

### MAJOR-3 — Abstract, p. 1: "the score is driven almost entirely by the blue spectrograph arm (ρ_s = +0.53…)". ρ = 0.53 does not support "almost entirely"; the statistics that do are in the released files and unreported.

**Claim.** Abstract and §V C rest the blue-arm result on Spearman coefficients: `+0.527` for r_B against `−0.037` (r_R) and `−0.142` (r_Z).

**Why it is wrong as argued.** ρ = 0.527 corresponds to ρ² ≈ 0.28 of rank variance. Read on its own, that is a moderate monotone association, not "almost entirely". A referee who checks only the reported statistic will conclude the claim is overstated.

**The irony is that the claim is true and the paper has much better evidence for it, unused.** From `flagship_sample_v2_enriched.parquet`:

- `worst_band` (a released column, listed in Table IV's anomaly group) is **`B` for 1,180 of the 1,244 released objects — 94.9%**; `Z` for 60, `R` for 4. This is the cleanest one-line statement of the result in the entire dataset and the paper never quotes it.
- Regressing `mean_mse` on (r_B, r_R, r_Z): full R² = 0.777. **Dropping r_B collapses R² to 0.006**; dropping r_R leaves 0.609; dropping r_Z leaves 0.201. That is what "driven almost entirely" means, stated in the right currency.
- `peak_residual_wavelength` (also a released column) has median **4057 Å**, minimum 3632 Å, and **89.5% of released objects peak below 5930 Å**. The residual is not merely in the b arm; it is piled against the DESI blue cutoff.

**Fix.** Replace the Spearman-only argument with the `worst_band` census and a variance decomposition, and add the `peak_residual_wavelength` distribution as a figure panel. This strengthens the paper's own result at zero cost. Keep the Spearman coefficients as a secondary line if desired.

---

### MAJOR-4 — §V C, p. 6: ρ(S, r_B) is partly definitional, and the relation between r_B/r_R/r_Z and `mean_mse` is never defined.

**Claim.** §V C presents the per-camera Spearman coefficients as one of the paper's "three measurements of what the score responds to" (§I item 4).

**Why it is wrong.** S is an **exact affine function of `mean_mse`**. I verified directly against the released tables that `S = (mean_mse − 0.8770776222235043)/1.3605120637453498` holds to `atol=1e-6` for all 1,244 rows, and ρ(S, mean_mse) = 1.000. Therefore ρ(S, r_B) ≡ ρ(mean_mse, r_B): it is a correlation between a loss and one of its own components. A positive coefficient for whichever component dominates the loss is arithmetically guaranteed, and the near-zero coefficients for r_R and r_Z are the expected consequence of r_B carrying the variance, not independent evidence. Presenting this as a *measurement* of what the score responds to, rather than as a *decomposition* of the score, misdescribes the inference.

Separately, **the reader cannot reconstruct the decomposition at all**, because r_B, r_R, r_Z are never defined relative to `mean_mse`. Their medians (2.529, 1.026, 0.943, summing to 4.50) do not reproduce the median `mean_mse` (5.344); the median ratio `mean_mse / (r_B + r_R + r_Z)` is 1.19; an OLS fit needs an intercept of −6.17. Some normalisation is in play that the paper does not state.

**Fix.** (a) Reframe §V C explicitly as a decomposition of the score into its components — which is a legitimate and useful thing to report — and drop the framing that presents it as an independent measurement. (b) Give the exact definitions of r_B, r_R, r_Z, their normalisation, and how they combine into `mean_mse`, with per-camera bin counts. Without this the section is not checkable.

---

### MAJOR-5 — §V C / §VII C OT-3, pp. 6, 13: the instrumental-vs-astrophysical question is deferred to external exposure tables while the decisive first-order tests sit unused in the released catalogue. *(Direct answer to focus question 2.)*

**Claim.** §V C: *"Two readings survive this measurement, and the data here do not separate them: blue-end sky-subtraction and calibration residuals … or genuine spectral behaviour … This is the single most consequential open question about the catalogue."* OT-3 then defers the diagnosis to *"the b-camera residual against airmass, lunar phase, and blue-end sky-subtraction residuals in the DR1 exposure tables."*

**Why it is wrong.** "The data here do not separate them" is too strong. Table IV's `exposure` group releases `median_coadd_snr_b`, `median_coadd_snr_r`, `median_coadd_snr_z` per object, and the `anomaly` group releases `peak_residual_wavelength`. Running the obvious within-catalogue tests on `flagship_sample_v2_enriched.parquet`:

| test | result |
|---|---|
| ρ(r_B, `median_coadd_snr_b`) | **−0.008, p = 0.78** |
| ρ(r_R, `median_coadd_snr_r`) | −0.078, p = 6.2e−3 |
| ρ(r_Z, `median_coadd_snr_z`) | −0.171, p = 1.2e−9 |
| `peak_residual_wavelength` | median 4057 Å, min 3632 Å, 89.5% below 5930 Å |

These are directly relevant and cut both ways. The **blue-arm residual has no detectable dependence on blue-arm signal-to-noise** — which disfavours the simplest instrumental reading (that the b arm reconstructs worst because it is noisiest), and is a stronger statement than the paper currently makes. Meanwhile the **z-arm** residual shows the clearest S/N dependence of the three, which is worth saying. And the residual's concentration against the 3600 Å DESI cutoff is a strong hint about where to look, whichever reading wins.

The paper is therefore neither overstating nor understating which explanation is favoured — it declines to state anything, while holding the data. For the question it calls "the single most consequential open question about the catalogue", that is not acceptable.

**Fix.** Add a subsection running every within-catalogue diagnostic the release already supports: per-camera residual vs per-camera S/N; residual vs `coadd_numexp`; `peak_residual_wavelength` distribution, and its distribution in the *rest* frame for the ZWARN = 0 subset (which would test the astrophysical reading directly — a rest-frame feature would pile up at a rest wavelength, a calibration artefact at an observed one). Keep OT-3 for the airmass/lunar-phase work that genuinely needs external tables, but state what the released data already establish before deferring.

---

### MAJOR-6 — Abstract, §I item 5, §XI: the recovery benchmark's lack of statistical power is stated once in §V D and omitted from all three summary locations. *(Direct answer to focus question 3: yes, undersold.)*

**Claim.** Abstract: *"A known-object recovery benchmark against five reference classes recovers no class at the pre-declared bar, so this work is reported as a validated data release and not as a discovery."* §I item 5: *"A negative recovery benchmark … against five published reference classes, no class is recovered at the pre-declared bar."* §XI: *"The known-object recovery benchmark does not clear its pre-declared bar."*

**Why this is an undersell.** §V D, p. 6, states the correct thing and states it well: *"the reference footprints are small compared with the parent survey, so the test has little power for rare classes: the 95% upper limit on the recovery of superluminous-supernova hosts is 12.5%, which excludes almost nothing. The honest summary is that the benchmark rules out a strong recovery signal and is consistent with anything weaker."* Table VII confirms it quantitatively: N_ref = 27 for SLSN hosts, 84 for LAEs, 580 for CVs. I verified every interval in Table VII independently and they are correct Wilson intervals — which is exactly why they are so wide.

The three summary locations report the null as though it were informative. "Recovers no class at the pre-declared bar" is a statement about the bar; "is consistent with anything weaker than a strong signal" is a statement about the data, and only the second belongs in an abstract that a reader will use to decide how well-characterised this catalogue's completeness and purity are. As written, a reader of the abstract alone would reasonably conclude the catalogue has been tested and found to contain nothing unusual. The correct conclusion is that the catalogue has not been meaningfully tested at all — which is also what OT-1 says.

**Fix.** Add one clause to each of the three locations. Abstract: *"…recovers no class at the pre-declared bar, though with reference samples of 27–5,285 objects the benchmark has little power (95% upper limits up to 12.5% recovery) and excludes only a strong signal."* Same in §I item 5 and §XI. This costs fifteen words and converts an overclaimed null into an honest one.

---

### MAJOR-7 — Table VII, p. 9, `Enrichment` column: computed with the denominator §II A explicitly forbids.

**Claim.** Table VII's caption: *"enrichment is recovery over the catalogue's base rate **in the parent**."* The BAL row reads **4.2×**.

**Why it is wrong.** §II A, p. 2, declares: *"21,793,550 satisfy the science-target provenance gate … **that number, not the full 27.5 million, is the parent population of this catalogue, and every selected fraction quoted below uses it**."* The released benchmark stores `benchmark/parent_total = 27547223` and `benchmark/base_rate = 4.5158e-05`, i.e. Table VII uses the 27.5M denominator — the one §II A rules out. The artifact also stores the correct value: `benchmark/enrichment_science_denominator/bal_quasars = 3.3148`. I confirm both: 1/5285 ÷ (1244/27547223) = 4.19; 1/5285 ÷ (1244/21793550) = 3.31.

The paper then *corrects itself in prose* three paragraphs later (§V D: *"the fairer denominator is the 21,793,550 science-target parent, which raises the base rate and lowers the BAL enrichment from 4.2× to 3.3×"*) — while leaving the wrong number printed in the table a reader will cite.

**Fix.** Recompute the Enrichment column with the science-target parent (the artifact already carries it), and say so in the caption. If both are wanted, print both columns. Do not leave a table whose only numerical content contradicts the paper's declared convention.

---

### MAJOR-8 — §V B, p. 6: "four of these are formally significant … the significant ones are negative." Both halves cannot be true.

**Claim.** *"At n = 1,244 four of these are formally significant and all are negligible in size; the significant ones are negative, i.e. longer exposures score marginally lower."*

**Why it is wrong.** The released V10 output gives all five p-values explicitly:

```
median coadd S/N: rho=+0.058 (p=0.039)   <-- significant AND POSITIVE
coadd exposure time: rho=-0.076 (p=0.0072)
TSNR2_LRG: rho=-0.093 (p=0.00098)
TSNR2_QSO: rho=-0.096 (p=0.00067)
r-band flux: rho=-0.016 (p=0.56)
```

At α = 0.05 exactly four are significant — and the fourth is the **positive** S/N coefficient. So "four are significant" and "the significant ones are negative" are mutually exclusive. (At α = 0.01 three are significant and all three are negative, but then "four" is wrong.) I reproduced each p-value from ρ and n = 1,244 via the Spearman t-approximation and they all match the stored values.

**Fix.** State the significance threshold and then the true statement, e.g.: *"At n = 1,244, four reach p < 0.05; the three strongest are negative (longer exposures score marginally lower) while the S/N coefficient is positive and marginal (ρ = +0.058, p = 0.039). All are negligible in size."* The paper's underlying conclusion — that none of these explains the tail — survives intact; only the sentence is wrong.

---

### MAJOR-9 — §IV D, p. 5: "The score's strongest responses are to known objects, which is a mild positive signal for the method" is untested and confounded by brightness.

**Claim.** *"The point is reinforced by the extreme tail: the three highest-scoring objects in the whole sample (S = 11.33, 8.01, 7.80) are all matched, i.e. already catalogued. The score's strongest responses are to known objects, which is a mild positive signal for the method…"*

**Why it is wrong as argued.** The fact is real and stronger than stated (the top **six** scores are all matched — 11.332, 8.012, 7.799, 7.739, 7.568, 7.331), and the population-level version is real too: matched objects score significantly higher than unmatched (median 3.337 vs 3.237, Mann–Whitney p = 4.5e−5). But the interpretation is confounded and the confound is checkable in the released table:

```
                 matched med   unmatched med   MWU p
flux_r              0.2887        0.1840       8.2e-04
median_coadd_snr_r  0.0792        0.0460       1.1e-06
median_coadd_snr_b  0.0329        0.0263       2.3e-02
```

SIMBAD/NED-matched objects are **brighter and better measured**, because that is what makes an object catalogued elsewhere. Any score preference for brighter objects therefore produces exactly the observed matched/unmatched score difference with no implication whatsoever for whether the score finds unusual astrophysics. The paper cannot argue in §V B that the score is not a brightness proxy (ρ = −0.016 against r-band flux across the released sample) and then in §IV D read a matched/unmatched score difference as a positive signal for the method, without testing the two together.

The decisive counter-evidence is the paper's own §V D: the score preferentially selects objects that are *catalogued*, but recovers **no specific class of genuinely unusual object** at any enrichment. The economical reading is detectability, not anomalousness.

**Fix.** Either test the matched/unmatched score difference at fixed brightness and S/N (stratify or partial-correlate — a few lines against the released table), and report the result whichever way it falls; or delete the "mild positive signal for the method" reading and state only the fact. Do not leave an untested favourable interpretation in a paper that is otherwise this careful about not over-reading.

---

### MAJOR-10 — Table VI, p. 8, row V1 marked `pass` without qualification, when the checker verified one of the gate's three conditions.

**Claim.** V1's requirement reads *"gates/check_sample_provenance.py exits 0 on the released sample tables (TARGETID > 0; OBJTYPE/FIBERSTATUS **where carried**)"*, outcome `pass`. §V A counts it among the passes.

**Why it is wrong.** The checker's own stdout, recorded in both `validation_contract_results.json` and `provenance_recheck_2026-09-18.json`, is for both released tables:

```
{'row_count': 1244, 'checked_objtype': False, 'checked_fiberstatus': False, 'status': 'clean'}
```

Neither column is carried, so V1 verified **TARGETID > 0 and nothing else** — one of the three conditions of the provenance gate. The gate is §III B's headline methodological result and the abstract's central claim. §V E does disclose the underlying schema gap (*"whose absence means the provenance gate cannot re-verify its own first two conditions from the published file alone"*), which is to the authors' credit — but the disclosure is in prose three pages after a table that reads as an unqualified pass, and the parenthetical "where carried" in V1's requirement text conceals rather than reveals that nothing was carried.

**Fix.** Mark V1 `partial` in Table VI, with the observed string (`checked_objtype=False, checked_fiberstatus=False`) in the row or caption. Correct the pass count accordingly (this interacts with BLOCKER-1). Best fix: add `OBJTYPE` and `COADD_FIBERSTATUS` to the deposit and re-run V1 to a genuine full pass — the schema gap is already flagged as must-repair in §V E, so this is work the authors have committed to anyway.

---

### MAJOR-11 — Table IV, p. 5, "Released column schema, by group": does not describe any released artifact.

**Claim.** Table IV presents 9 column groups summing to 180 columns as "the published columns by group" of the released catalogue.

**Why it is wrong.** The released enriched table carries **177** columns, and its column set does not match Table IV in either direction:

- **Table IV lists, the file lacks:** the entire AllWISE group (`w1, w2, w1_w2, match_separation_arcsec, match_flag`), the entire SIMBAD/NED group (6 columns), and the entire taxonomy group (`cluster_id, family_id, family_descriptor, is_core_member`). These live in separate released artifacts (`flagship_wise_v2.parquet`, `flagship_crossmatch_v2_*.parquet`, `flagship_taxonomy_v2.json`).
- **The file has, Table IV omits:** `zerr`, `mean_fiber_ra`, `mean_fiber_dec`, `gr_color`, `rz_color`, `w1w2_color`, `is_point_source`, `is_star_candidate`, `classification`, `discovery_potential`, and — notably — `residual_kurtosis`, the column that DEFECT-2 is entirely about.
- **Mis-grouped:** `parallax` and `gaia_phot_g_mean_mag` are listed under "Legacy Survey photometry"; they are Gaia DR3 quantities. `flux_w1`/`flux_w2` (Legacy forced photometry) and `w1`/`w2` (AllWISE) both appear with no guidance on which to use.

So a reader cannot map Table IV onto any file in the deposit, which defeats its purpose in a paper about reproducibility. `draft_numbers.json` records `n_columns_joined = 180` and `n_columns_master_frame = 192`, neither of which is 177, and neither number is explained in the paper.

**Fix.** Make Table IV a per-artifact schema: one block per released file, with the file name, its column count, and its columns — generated from the files so it cannot drift. Reconcile 177 / 180 / 192 explicitly.

---

### MAJOR-12 — undeclared all-constant columns in the released table, including one named `discovery_potential`.

**Claim.** DEFECT-2 is scoped to *"every derived residual-diagnostic column in the enriched table carries values"* and its observed output names one column: `['residual_kurtosis']`.

**Why it is incomplete.** Two further columns in `flagship_sample_v2_enriched.parquet` are content-free for all 1,244 rows:

```
discovery_potential : "TBD"          × 1244
classification      : "UNCLASSIFIED" × 1244
```

and a third, `is_star_candidate`, is `True` for 121 objects on an undocumented criterion never mentioned in the paper (against 5 pipeline `STAR` classifications).

A column literally named **`discovery_potential`**, shipped in the deposit of a paper whose §X is titled "What this catalogue is not" and whose first bullet is "It is not a discovery catalogue", is going to be quoted back at the authors. Whatever its provenance, it must not ship.

**Fix.** Drop `discovery_potential` and `classification` from the deposit, or populate them and document them. Widen DEFECT-2 from "residual-diagnostic" to "any released column that is null or constant for every row", and re-run it — that check should catch all three automatically. Document or drop `is_star_candidate`.

---

### MAJOR-13 — §II A, p. 2: the deduplication rule is arbitrary and its effect on catalogue membership is unquantified.

**Claim.** *"Deduplication by last TARGETID occurrence in lexical shard-then-row order removed 878,740 duplicate rows and left 27,547,223 unique TARGETIDs."*

**Why it matters.** 878,740 rows — 3.1% of the raw scan — were dropped by a rule with no physical content: which observation survives depends on shard file names and row order. In DESI, the same `TARGETID` recurs across (survey, program) coadds with genuinely different spectra and therefore different reconstruction errors; the released catalogue itself spans eleven (survey, program) cells, from `main/dark` (445) to `sv2/bright` (1). Since the catalogue is the top 5.7 × 10⁻⁵ of the parent and 1,244 of its objects sit between S = 3.0002 and S = 3.28, membership near threshold is plausibly decided by which duplicate the lexical ordering happened to keep.

The paper cannot claim a reproducible, contract-defined selection while a 3.1% arbitrary tie-break is unexamined.

**Fix.** Report (a) the distribution of ΔS among duplicate TARGETIDs, (b) how many of the 1,244 released objects have a duplicate whose alternative score falls below threshold, and (c) how many objects above S = 3 were excluded because the retained duplicate scored lower. If the answer is "a handful", say so and the issue closes. If it is not, the rule needs to be replaced with a defensible one (highest S, or best `COADD_FIBERSTATUS`, or per-(survey, program) rows kept separately) and justified.

---

### MAJOR-14 — §VIII, pp. 12–13: the f_NL paragraph is the only quantitative passage in the paper with no equation, no citation, no table and no artifact.

**Claim.** *"A local-shape primordial non-Gaussianity of the amplitude predicted by a matter-dominated contraction shifts the z ≈ 10–12 massive-halo abundance by roughly 6–15%, more than an order of magnitude below the ≳0.3 dex stellar-mass systematic floor of current high-redshift photometric censuses, and with the wrong sign to explain an over-abundance; a factor-of-two effect would require |f_NL| ∼ 30, far outside current constraints."*

**Why it is a problem.**

1. **Unsourced and unreproducible.** §IX states *"Every number in this manuscript names its source artifact in a comment in the LaTeX source."* This paragraph names no artifact, cites no reference, and gives no equation. The assumed f_NL amplitude is not stated; the halo mass is not stated; the non-Gaussian mass-function correction used (LoVerde et al., Matarrese–Verde–Jimenez, or another) is not named; the "≳0.3 dex stellar-mass systematic floor" has no citation. This is the one place in a scrupulously sourced paper where a reader is asked to take numbers on trust.
2. **"More than an order of magnitude below" is false at the stated upper end.** 0.3 dex is a factor 10^0.3 ≈ 2.0, i.e. ~100%. A 15% shift is a factor 6.7 below 100%, not more than an order of magnitude. The claim holds at the 6% end and fails at the 15% end.
3. **The comparison is not like-for-like.** A 0.3 dex *stellar-mass* systematic and a percentage *abundance* shift are different quantities. On the steep z ≳ 10 halo mass function a 0.3 dex mass error propagates to an abundance error of factors, not tens of percent — so the comparison as constructed probably *understates* the systematic and thereby understates the paper's own point. Convert both to the same quantity.

I note the numbers are physically plausible: for the standard matter-bounce local amplitude and ν ≈ 5–6 at z ≈ 10–12, a several-percent to ~15% abundance shift and a |f_NL| ∼ 30 requirement for a factor-of-two effect are the right order. The objection is entirely about sourcing and internal consistency, not about the physics being wrong.

**Fix.** State the assumed f_NL and its origin, give the mass-function correction with a citation, name the halo mass and redshift, cite the 0.3 dex floor, commit the calculation as an artifact and reference it as the rest of the paper does, express both effects in the same units, and correct "more than an order of magnitude".

---

### MAJOR-15 — §VI A, p. 8: the taxonomy's clustering is under-specified and its feature space appears mis-constructed.

**Claim.** *"The 675 unmatched objects are grouped by PCA → UMAP [9] → HDBSCAN [10] on (S, α, δ), with k-nearest-neighbour noise reassignment, giving 25 clusters…"*

**Problems, all checkable against the text and Table IX:**

1. **PCA on a 3-dimensional feature vector is near-vacuous.** Applied to (S, α, δ) it can only rotate and rescale; it cannot reduce dimension usefully. Its presence in the pipeline is unexplained.
2. **No relative scaling is given.** S is a dimensionless standardised statistic with released range 3.0002–11.3316; α and δ are angles spanning 360° and ~170°. Euclidean distance between them is meaningless without a stated standardisation, and the resulting clusters depend entirely on that choice. It is not stated.
3. **Right ascension wrap is not handled.** RA is periodic at 360°; naive Euclidean distance splits objects at α ≈ 0 into maximally distant points. Table IX shows family 0 spanning **350.4°** in RA and family 1 spanning 260.7° — exactly the signature of an unwrapped angular coordinate. The fix (embed as (cos α cos δ, sin α cos δ, sin δ)) is standard.
4. **Hyperparameters absent.** UMAP `n_neighbors`, `min_dist`, output dimension, random seed; HDBSCAN `min_cluster_size`, `min_samples`; the "k-nearest-neighbour noise reassignment" k and rule. None appear in the paper or the manifest, so §VI is the one section of the paper that cannot be reproduced even with the released files.
5. **UMAP before density clustering is known to distort densities**, and HDBSCAN run on a UMAP embedding of three raw features is a lot of machinery to recover what §VI B then concedes is a survey/programme stratification (70.4% dominant-cell purity). A direct comparison against clustering on (survey, program) alone would settle whether the pipeline adds anything.

**Fix.** Give every hyperparameter and the seed; justify or remove PCA; handle the RA wrap and re-run; state the feature standardisation; and add the (survey, program) baseline comparison. Given §VI C's negative silhouette and §VI B's own concession, the honest outcome may be that the taxonomy should be replaced by an explicit score-tier × (survey, program) stratification, which would be simpler, fully reproducible, and no weaker.

---

### MAJOR-16 — NED, VizieR, AllWISE and Redrock are used throughout and cited nowhere.

**Locations.** §IV D (562 of 569 counterparts are NED matches), §IV C and Table V, Appendix A, §IV B.

**Why it is wrong.** SIMBAD is properly cited ([8], Wenger et al. 2000). **NED — which supplies 562 of the paper's 569 counterparts, i.e. 99% of the cross-match result — has no reference and no acknowledgement anywhere in the paper**, and the Acknowledgments section that would carry its required service statement is a placeholder (BLOCKER-5). **VizieR** is used via astroquery (Appendix A) and is uncited (Ochsenbein et al. 2000). The **AllWISE source catalogue** is used for 74 matches with only the WISE mission paper [12] and NEOWISE [13] cited — neither is the AllWISE catalogue. **Redrock**, the redshift fitter on whose `z`, `ZWARN` and `ΔΧ²` the entirety of §IV B, the FT-A/FT-C tier rules, and DEFECT-3 depend, is never cited by name (only the pipeline paper [6] and the bitmask documentation [7]).

NED and VizieR both carry standard, mandatory acknowledgement text.

**Fix.** Add references and the required service acknowledgement text for NED, VizieR and AllWISE; cite Redrock; and state the NED and SIMBAD query dates and versions, since both are living databases and the cross-match result is not reproducible without them (this matters for §V D's base rates and for the 675-object unmatched subset that the entire taxonomy is built on).

---

## 4. MINOR findings

**MINOR-1 — The number of "defects" takes four different values in four places.** §I item 3: *"including **two** defects the release carries openly"*. §V A: *"**three** defects the release must state rather than hide (DEFECT-1 to DEFECT-3)"*. §V E heading paragraph: *"**Two** defects in the released tables are recorded openly"*, closing with *"The deposit must carry all **four**"*. Abstract: *"one of **four** release defects we record openly"*. These refer to overlapping but different sets (contract rows vs actual failures vs schema gaps) and the paper never reconciles them. **Fix:** define one term ("release defect") once, enumerate the members, and use that count everywhere.

**MINOR-2 — Artifact counts 13 / 9 / 10 are unreconciled.** Table I and §II B: thirteen hash-bound artifacts, of which "the nine released data products". §IX: *"The assembly reads only the **ten** hashed artifacts."* Ten is never defined. **Fix:** name the ten.

**MINOR-3 — §IV C, p. 4: the morphology census does not close.** *"441 are typed PSF (point-like) and 316 REX, with 406 rows carrying an empty MORPHTYPE"* = 1,163 of 1,244. The released table also contains `EXP` 61, `SER` 14, `DEV` 6 (=81). The omission matters because §VII B uses "SER rather than point-like" as evidence against a candidate, so the reader needs to know how many SER objects exist. **Fix:** report all six categories.

**MINOR-4 — Abstract overstates the null direction relative to §VI C.** Abstract: the taxonomy *"carries **no material structure** in the model's own latent space"*. §VI C: the families *"carry **a small amount** of latent-space information"*, and the observed silhouette beats all 50 permutation draws; V12's own status is `structured-but-weak`. **Fix:** align the abstract to "structured but not separated" — the paper's own phrase, in Fig. 8's caption.

**MINOR-5 — §VI C, p. 9: a 50-draw permutation null is far too small for a test the paper says runs in under 60 s.** Observed −0.0162 vs null −0.0244 ± 0.0039 and max draw −0.0184: the observed value is 2.1 null-σ above the mean and only 0.56 null-σ above the largest of 50 draws. "Empirical p < 1/50" is the resolution floor of the test, not a measurement. **Fix:** use ≥10,000 draws and report p = (r+1)/(B+1). Separately, a label-permutation null only asks whether the partition beats random relabelling — nearly guaranteed for any partition correlated with anything. The informative comparison is against **alternative partitions** of the same sizes (survey/programme cells; random contiguous sky strata), which would test whether the families add information beyond the footprint stratification §VI B already concedes.

**MINOR-6 — §III A, p. 2: the sealed stability check tests only the mean.** The check is |µ_val − µ| ≤ 5σ/√n; I verify the bound exactly (5 × 1.3605120637/√20000 = 0.0481014, matching `calibration/stability_bound` to seven digits) and the observed deviation (0.0054285). But σ_MSE enters S with equal weight and is never checked, nor is the shape of the held-out MSE distribution. Since S is defined by both constants, a drift in σ would move every score. **Fix:** add a scale check (e.g. an F-test or bootstrap CI on σ_val/σ) and a distribution-shape check (KS against the fit sample) to the sealed contract.

**MINOR-7 — Figs. 5 and 9 carry no uncertainties, and Fig. 5's log axis cannot show the sample it claims.** Fig. 5's caption says *"for the 1,244 released objects"*, but its third panel plots r-band flux on a log axis from 10⁻³ to 10²; the released table contains 11 negative `flux_r` values and 363 rows where `flux_g = flux_r = flux_z = flux_w1 = 0.0` exactly. Those points cannot appear. **Fix:** state how many points are off-scale, how zero/negative fluxes were handled in the quoted Spearman (ρ = −0.016), and whether the join-gap rows were excluded — if they were not, a third of the sample entered the brightness correlation as hard zeros, which would materially affect it.

**MINOR-8 — Table VII caption: "95% binomial interval" does not identify the construction.** The intervals are Wilson — I reproduced all five exactly (e.g. 1/5285 → [0.0033%, 0.107%]; 0/27 → [0, 12.456%]). Clopper–Pearson on 1/5285 would give a lower bound near 0.0005%, an order of magnitude different. **Fix:** name the method in the caption.

**MINOR-9 — Table V caption, p. 5: "Counterpart types of the 569 matched objects, by service" but the columns sum to 600.** NED sums to 562, SIMBAD to 38; 562 + 38 = 600 > 569 because 31 objects match both. The caption also says *"Only the eight most common types per service are listed"*, but the release records exactly 8 distinct NED types and 6 SIMBAD types (`n_ned_types_distinct: 8`, `n_simbad_types_distinct: 6`) — nothing is truncated, and the SIMBAD column shows six rows. **Fix:** say the columns are per-service and non-disjoint, and that all types are listed.

**MINOR-10 — §VII B: "the 95th percentile of the whole sample" is the 94.7th, and the framing cuts against the argument.** `ft_a[2].flux_g_percentile_in_sample = 0.9469`. More usefully: `flux_g_p99_all = 24.13` nmgy, so ~62 catalogue objects carry a g flux at least as bright as the refuted object's 4.33 nmgy. It is a bright value, not an extreme one. **Fix:** quote the percentile correctly, and rest the refutation on the physics (a z = 5.19 break requires f_g ≈ 0, and 4.33 nmgy ≈ 20.6 AB mag is orders of magnitude above any plausible Legacy Survey noise) rather than on a percentile rank within a catalogue whose flux column is partly join-corrupted.

**MINOR-11 — §VII A: "five rules-based tiers" but FT-D is empty, and FT-A's rule as stated returns 36 objects, not 4.** The FT-A bullet gives the rule as *"ZWARN = 0 and z ≥ 4"*, which by §IV B selects 36 objects; the restriction to the unmatched subset appears only in the preamble sentence. **Fix:** state each tier rule completely and self-containedly; say four of five tiers are populated.

**MINOR-12 — §V A mis-assigns V9.** *"Requirements cover … the selection rule (V4, V7, V9)…"*; V9 is the sky-fraction-by-score check (§III B), not a selection-rule check. **Fix:** move V9 to its own group.

**MINOR-13 — Two citation defects.** Ref. [3] reads *"Mon. Not. R. Astron. Soc. **547, stag010** (2026)"*, mixing a volume number with an advance-access/DOI suffix. Ref. [12] (Wright et al. 2010 — the WISE mission paper) is cited as one of two references for *"the standard mid-infrared AGN criterion [11, 12]"*; only [11] (Stern et al. 2012) is that criterion. **Fix:** correct [3]'s pagination; cite [11] alone for the criterion and [12] for WISE itself.

**MINOR-14 — §IX contradicts itself on determinism.** *"The pipeline is deterministic apart from the V12 permutation null, which is seeded."* A seeded null is deterministic. **Fix:** "The pipeline is fully deterministic; the V12 permutation null is seeded."

**MINOR-15 — Table I gives only the first 16 hex of each SHA-256.** The paper's claim is SHA-256 binding; 64-bit prefixes are fine for a printed table but the full digests must be locatable. **Fix:** state where the full 64-hex values live and include them in a machine-readable file in the deposit.

**MINOR-16 — §IV D understates its own strongest version.** The top **six** scores in the catalogue are SIMBAD/NED-matched (11.332, 8.012, 7.799, 7.739, 7.568, 7.331), not the top three. (Interpretation still subject to MAJOR-9.)

---

## 5. NIT findings

**NIT-1 — §VII B writes the break as 1216(1+z) Å while the stored values use 1215.67 Å.** The quoted break wavelengths (6484, 7530, 8587, 8616 Å) reproduce exactly with 1215.67 Å and are 2–3 Å off with 1216. Harmless; state the line centre used.

**NIT-2 — Fig. 7 (left panel), p. 10, hides the object §VI D singles out.** The axis tops at 6.5 and fliers appear suppressed, so family 3's S = 7.15 object — *"the highest-scoring unmatched object in the catalogue"*, discussed two paragraphs below and named as an FT-C/FT-E target — is not visible in its own box. State the whisker convention (5–95%?) and that outliers are hidden, or show them.

**NIT-3 — Fig. 9's "sample median f_g" dashed line is drawn across the r and z bars**, where it has no meaning. Restrict it to the g bars or add per-band medians.

**NIT-4 — Table IV lists `flux_w1`/`flux_w2` (Legacy forced photometry) and `w1`/`w2` (AllWISE) with no guidance on which to use.** Relevant because §IV C quotes a median AllWISE W1−W2 = 0.51 while the Legacy `flux_w1` column contains negative values as low as −1.51 nmgy.

**NIT-5 — The abstract calls the model "convolutional"; §III A never says so and never describes the architecture.** (Subsumed by BLOCKER-6, but the abstract/body mismatch is independently worth fixing.)

**NIT-6 — §II A does not say whether the 200 calibration groups and 40,000 calibration+validation spectra were excluded from the 21.8M scored population.** (Related to BLOCKER-6.)

**NIT-7 — §I forward-references "Secs. V B–VI C" for the three measurements**, spanning a section boundary where §V C and §VI C are the actual targets. Cite the three subsections individually.

**NIT-8 — §V D: "One broad-absorption-line quasar [17] matches, at 4.2× the base rate."** With N_match = 1, "4.2×" (or the corrected 3.3×) should be quoted with its interval — Table VII gives recovery [0.003%, 0.107%], i.e. the enrichment is consistent with 0.7×–24×. A single match supports no enrichment statement at all.

**NIT-9 — §III B: "the last asserted rather than merely filtered"** (of `TARGETID > 0`) is opaque on first reading; one clause explaining the distinction would help, since it is the only one of the gate's three conditions V1 actually verifies (MAJOR-10).

---

## 6. Genuine strengths

**STRENGTH 1 — The arithmetic inside the tables is exact, and I checked a lot of it.** I independently recomputed, and found correct: the six bins of Table II summing to 320,418 all-fibres and 1,244 science targets, matching Table III's S > 3 row exactly; every survival count on Table III's ladder as the correct partial sum of Table II (86,053 / 52,188 / 27,180 / 3,810 / 337 and 152 / 44 / 20 / 2 / 1); all six science fractions (0.39, 0.18, 0.08, 0.07, 0.05, 0.30%); all six sky/non-science percentages bin by bin; the threshold rule replay (largest grid point with science count ≥ 300 → S > 3, n = 1,244); 1,244/21,793,550 = 5.708 × 10⁻⁵; 28,425,963 − 27,547,223 = 878,740; 502 + 742 = 1,244 and 502/1,244 = 40.4%; 424 + 73 + 5 = 502 and 1,153 + 86 + 5 = 1,244; 562 + 38 − 31 = 569 and 569 + 675 = 1,244; both counterpart-type columns of Table V summing exactly to their service totals; Table VIII's family sizes summing to 675 with N_cl summing to 25; Table IX's dominant-cell share weighting to 70.4%; the 35 tier rows of Table X reducing to 32 distinct objects with exactly three cross-tier repeats; all five Wilson intervals in Table VII; the stability bound 5 × 1.3605/√20,000 = 0.0481; all five V10 p-values and all three V11 p-values from ρ and n = 1,244; and the four Lyman-α break wavelengths. **I did not find a single arithmetic error inside a table.** Across referee reports this is genuinely rare, and it makes the errors I did find (all in prose *about* the tables) correspondingly easy to fix.

**STRENGTH 2 — §III B is a real, transferable result and is the most valuable thing in the paper.** The demonstration that a raw reconstruction-error tail on DESI public coadds is >99.5% sky or non-science in *every* bin above S = 3 — with the mechanism named (sky fibres reconstruct worst precisely because they contain no source) and the conclusion drawn correctly (this is a property of the substrate, not of this model, and applies to any reconstruction-error search on these data) — is a result that will save other groups real time. Table II and Fig. 1 present it cleanly, Fig. 1 flags its suppressed zero, and the survival-curve restatement in Fig. 2 (right) is the right complement. If the rest of the paper were withdrawn this section would still deserve publication.

**STRENGTH 3 — The paper reports its negative results as negatives, with a discipline most catalogue papers do not attempt.** FT-D returning zero targets is stated as a result and the rule retained for auditability. V12's weaker reading is adopted throughout rather than the flattering one. DEFECT-1 and DEFECT-2 are designed to fail so the release must carry its own defects. §V B explicitly instructs the referee how *not* to over-read V10 ("A referee should read V10 as closing one explanation, not as opening another") — I have never seen that sentence in a paper before and it is exactly right. §V D concedes the benchmark "is consistent with anything weaker". §VIII spends its length explaining how little the catalogue bears on the programme that motivated it. §X is an explicit five-bullet list of what the catalogue is not. My MAJOR findings about the abstract's framing (MAJOR-2, -3, -6) are all cases where the **body already contains the honest version** and the summary drifted — which is a much better failure mode than the reverse, and makes them cheap to fix.

**STRENGTH 4 — The follow-up set is rule-generated, replayable, and the cheapest named test is executed in the paper rather than deferred.** Fixing tier rules from literature criteria before counting targets, retaining a rule that returns nothing, spanning the taxonomy by construction in FT-E, and then running the zero-cost public-imaging test in §VII B instead of listing it as future work — this is the right instinct, and it is the reason I was able to find BLOCKER-3 and BLOCKER-4 at all. A paper that had deferred the test would have been *less* wrong and *much* less useful. Fix the execution; keep the practice.

**STRENGTH 5 — Bibliographic and production quality are high where they are checkable.** I spot-verified the references the paper's own Appendix A placeholder flags as uncertain and they check out: Gibson et al. 2009 ApJ 692, 758; Massaro et al. 2015 Ap&SS 357, 75; Ritter & Kolb 2003 A&A 404, 301; Ouchi et al. 2008 ApJS 176, 301; Perley et al. 2016 ApJ 830, 13; and beyond those, Stern et al. 2012 ApJ 753, 30; Dey et al. 2019 AJ 157, 168; Gaia DR3 A&A 674, A1; Bellm et al. 2019 PASP 131, 018002; Mainzer et al. 2014 ApJ 792, 30; Baron & Poznanski 2017 MNRAS 465, 4530; Wenger et al. 2000 A&AS 143, 9; Harris et al. 2020 Nature 585, 357; Virtanen et al. 2020 Nat. Methods 17, 261; Pedregosa et al. 2011 JMLR 12, 2825; Hunter 2007 CSE 9, 90; Ginsburg et al. 2019 AJ 157, 98 — all correct. LaTeX production is clean: `main.log` shows **zero overfull hboxes**, no undefined references, 15 pages; no column overflow or figure escape anywhere in the rendered PDF. Fig. 1's suppressed-zero annotation, Fig. 3's z = 4 tier line, and Fig. 2's marked release cut are all good figure craft.

---

## 7. Summary table

| Severity | Count | IDs |
|---|---|---|
| **BLOCKER** | **6** | validation pass count (11 not 13); Table I provenance caption; "supported" candidate is a join-defect row; half of the break test unapplied / colours contradict verdicts; four rendered placeholders + no resolvable data link + missing DESI acknowledgement; training corpus, grid and architecture unspecified and unhashed |
| **MAJOR** | **16** | title carries no null; "rises with score" false in top bin; "almost entirely blue" unsupported by ρ=0.53; ρ(S,r_B) definitional + residuals undefined; blue-arm diagnostics unused in own columns; benchmark power omitted from abstract/intro/conclusions; Table VII wrong denominator; "significant ones are negative" contradicted; matched-score claim confounded by brightness; V1 marked pass on 1 of 3 conditions; Table IV describes no released file; `discovery_potential`/`classification` constant columns; dedup rule arbitrary and unquantified; f_NL paragraph unsourced; clustering under-specified + RA wrap; NED/VizieR/AllWISE/Redrock uncited |
| **MINOR** | **16** | MINOR-1 … MINOR-16 |
| **NIT** | **9** | NIT-1 … NIT-9 |
| **Strengths** | **5** | table arithmetic exact; §III B transferable result; negative results reported as negatives; rule-generated follow-up set with the cheap test executed; bibliography and LaTeX production quality |

**Recommendation: MAJOR REVISIONS.** I would referee a revised version willingly. The authors should treat BLOCKER-3 and BLOCKER-4 as the priority: if a clean Legacy Survey DR10 forced-photometry query with inverse variances does not sustain a "supported" verdict for TARGETID 39627849358909321, §VII B and the corresponding abstract clause must be removed rather than rewritten, and the abstract's concrete outcome becomes "refutes one of four and cannot decide three" — which is a weaker but honest result, and entirely consistent with the rest of this paper's stance.

---

*End of report. Reviewer: claude-opus, INT leg, verdict-blind. Exact PDF SHA-256 `b972d890cf5b907eec0a7bf614dac5ba5647502efe3ee907533e4b3f96dd4cba`, verified by `shasum -a 256` before review. No prior disposition list, truth-audit or closure history was consulted; no other reviewer leg's report was accessible.*
