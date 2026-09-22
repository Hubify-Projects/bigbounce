# AF ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM — Claude Opus verdict-blind referee (INT leg)
**Reviewer**: Claude Opus (INT, verdict-blind)
**Input PDF**: pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf sha256=ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca pages=18

---

## Referee report — ApJS, ApJS-CATALOG profile

**Manuscript**: "A provenance-sealed DESI DR1 anomaly-score candidate catalogue: selection, validation, and a null known-object recovery benchmark" (Golden, Hubify Research)

### Preamble on how this was reviewed

I read all 18 pages of the exact PDF, every table, every figure and its caption, the
equation, and every bibliography entry. I independently recomputed every percentage,
ratio, cumulative count, confidence interval, magnitude conversion, and wavelength
conversion I could reconstruct from displayed numbers. I did not review the manuscript
as a discovery paper; the author is explicit that the pre-declared recovery condition
was not met, and I have not penalised the manuscript for that. I have, as instructed by
the ApJS-CATALOG profile, held it to a hard bar on internal consistency, reproducibility,
citation completeness, and whether each number is real.

**What survived my arithmetic audit.** I want this on the record before the findings,
because it is unusual: the numerical spine of this manuscript is very clean. Specifically
I verified and reproduce exactly:

- Tables II and III are fully mutually consistent. All six per-bin all-fibre counts sum
  to 320,418 and all six science counts to 1,244; every cumulative count on the threshold
  ladder (86,053 / 52,188 / 27,180 / 3,810 / 337 and 152 / 44 / 20 / 2 / 1) follows by
  subtraction; all six science fractions (0.39/0.18/0.08/0.07/0.05/0.30 %) and all six
  sky-or-non-science fractions (99.53/99.68/99.90/99.92/99.97/99.70 %) reproduce.
- 28,425,963 − 878,740 = 27,547,223; 1,244/21,793,550 = 5.708 × 10⁻⁵.
- Table V: NED types sum to 562, SIMBAD types to 38, 562 + 38 − 31 = 569,
  1,244 − 569 = 675, 45.7 %/54.3 % both correct.
- Table VII: every Wilson 95 % interval reproduces to the printed digit
  (1/5285 → [0.003, 0.107] %; 0/2060 → 0.186 %; 0/580 → 0.658 %; 0/84 → 4.373 %;
  0/27 → 12.456 %), and the 3.3× enrichment is exactly 1.892 × 10⁻⁴ / 5.708 × 10⁻⁵.
- Validation-contract accounting: 11 PASS + 2 REPORTED + 1 STRUCTURED-BUT-WEAK
  + 2 FAIL = 16 = the number of rows in Table VI.
- Table IV columns sum to exactly 192 as claimed.
- Table VIII: N sums to 675, N_cl to 25, N_W to 6; all eight ZWARN = 0 fractions match
  the bars in Fig. 7 (centre).
- Table IX: the N-weighted mean dominant share is 70.38 % → the quoted 70.4 %; the
  minimum RA span is 51.7°.
- Calibration bound 5 × 1.3605/√20000 = 0.0481.
- Lyman-break wavelengths 6484/7530/8587/8616 Å reproduce from 1215.67(1+z); the
  ~66 % r-band forest fraction reproduces as (6484−5500)/(7000−5500).
- f_g/f_r = 4.326/0.073 = 59; f_z/f_r = 1.75 and 1.42; 0.283/0.289 = 0.98 and
  0.296/0.289 = 1.02; 66/1244 → 94.7th percentile.
- Every quoted Spearman p-value is consistent with a two-sided t at n = 1,244.
- 7 h 42 m 53 s × $0.17/hr = $1.31.
- Table X: 35 tier rows, 3 cross-tier duplicates, 32 distinct objects.

That is a high standard of numerical hygiene and I say so plainly. The problems below
are therefore not arithmetic slips but structural: one section the author states is not
reproducible, one headline statistic that is misattributed, a data-availability statement
that is a placeholder, missing citations, and a substantial residue of internal
version-control language that must not reach print.

---

## ESSENTIAL — the manuscript cannot be accepted without these

### AF-E1 — Sec. VI A, p. 10–11: a reproducibility-first release contains a section that is, by the author's own statement, not reproducible

> "The UMAP and HDBSCAN hyperparameters (neighbourhood size, minimum distance, output
> dimension, random seed, minimum cluster size, and the k-nearest-neighbour
> noise-reassignment rule) are not recorded in this manuscript or its manifest, so this
> section is not reproducible from the released files alone even though the clustering
> pipeline itself is."

This is fatal in context. The entire thesis of the paper — stated in the title, the first
contribution in the Introduction, and Sec. IX — is that this release publishes "the exact
model, the exact code, the exact parent catalogue, the selection rule, the reason the rule
was chosen". Section VI is the manuscript's third headline contribution (the
"descriptive taxonomy" named in the abstract and in Introduction item 3), Table VIII,
Table IX, Fig. 7, Fig. 8, contract item V12, and the entire FT-E follow-up tier of 25 of
the 32 named targets all derive from it. A provenance paper cannot ship a
non-reproducible headline section, least of all when the missing information is roughly
six scalars that are sitting in the committed code.

**Required fix**: print the full UMAP/HDBSCAN/PCA hyperparameter set and the random seed
in the manuscript *and* in the manifest, add the clustering configuration to the hash-bound
artifact list of Table I, and add a contract item that re-runs the clustering from the
recorded configuration and reproduces the 25/8 partition bit-for-bit. If that cannot be
done, Sec. VI, Tables VIII–IX, Figs. 7–8, V12, and the FT-E tier must be removed from the
paper.

### AF-E2 — Sec. VI A, p. 10–11: the taxonomy is built on a metric the author states is defective, and the corrected version is stated to be cheap

> "Right ascension is periodic at 360°; naive Euclidean distance on (S, α, δ) splits
> objects near α ≈ 0 into maximally distant points, and Table VIII's own RA spans (up to
> 350° for one family) are the signature of exactly that defect, not a genuinely
> sky-spanning family."

and

> "a corrected re-clustering (RA embedded as (cos α cos δ, sin α cos δ, sin δ), every
> hyperparameter and seed stated, and a baseline comparison against (survey, programme)
> cells alone) is needed before the taxonomy's specific cluster and family boundaries are
> treated as anything but provisional."

and, in Sec. VII C, OT-2:

> "Cheap; the released catalogue already carries the latents."

The author has diagnosed the defect, specified the correct embedding, confirmed the input
data are in hand, and labelled the fix cheap — and has then published the defective
version anyway, with a full section, two tables, two figures, and a 25-target follow-up
tier built on it. Disclosure does not substitute for doing a computation that the paper
itself says costs nothing. Every cluster and family boundary in Table VIII, every RA span
in Table IX, and the identity of all 25 FT-E targets are contaminated by a known metric
error.

**Required fix**: re-run the clustering with the stated (cos α cos δ, sin α cos δ, sin δ)
embedding and the (survey, programme) baseline comparison, regenerate Tables VIII–IX,
Figs. 7–8, V12, and the FT-E tier from the corrected partition, and report how much the
partition moved. Alternatively delete the taxonomy from this paper and publish it
separately once corrected. "Provisional" is not an acceptable status for a headline
contribution of a catalogue release.

### AF-E3 — Abstract p. 1, Introduction item 4 p. 2, Sec. V C p. 8, Conclusions p. 16: the headline R² = 0.78 is attributed to the wrong quantity and is contradicted by the manuscript's own numbers

Abstract:

> "it alone accounts for R² = 0.78 of the score's variance, falling to R² = 0.01 without it"

Introduction item 4:

> "it is almost entirely explained by the blue-arm reconstruction residual (R² = 0.78,
> falling to 0.01 without it)"

Conclusions:

> "(R² = 0.78 of the score's variance, falling to 0.01 without it)"

Body, Sec. V C:

> "regressing mean_mse on (r_B, r_R, r_Z) gives R² = 0.777; dropping r_B collapses it to
> R² = 0.006, while dropping r_R or r_Z leaves R² = 0.609 or 0.201."

The 0.777 is the **three-regressor** model, not r_B alone. Worse, the manuscript's own
drop-one results bound r_B's solo R² from above: the two-regressor model that retains r_B
and drops r_Z achieves only R² = 0.201, so R²(r_B alone) ≤ 0.201. The abstract's word
"alone" and the Introduction's "almost entirely explained by" are therefore both
contradicted by the body, by a factor of nearly four. This is the single most-repeated
quantitative claim in the manuscript and it appears in the abstract, the contributions
list, and the conclusions.

I also note that the drop-one pattern (0.777 full; 0.609 without r_R; 0.201 without r_Z;
0.006 without r_B) is internally odd and demands explanation in its own right: if r_B
dominated in the sense claimed, dropping r_Z should not cost two thirds of the explained
variance.

**Required fix**: report the full nested-R² table — the three single-regressor R² values,
the three pairwise values, and the full model — and rewrite the abstract, Introduction
item 4, and the Conclusions to state exactly which model the quoted R² belongs to.
"Almost entirely explained by" must be withdrawn or re-derived from a number that
supports it.

### AF-E4 — Sec. VIII, p. 15: four uncited sources in the f_NL paragraph

> "For the amplitude this programme's matter-dominated-contraction bounce predicts
> (f_NL = −35/16 = −2.1875), applying the LoVerde, Miller, Shandera & Verde (2008)
> non-Gaussian correction to a Planck-2018 ΛCDM mass function (Eisenstein & Hu 1998
> transfer function) shifts the z ≈ 10–14, log M_h/M_⊙ ≈ 11.5 halo abundance by −6 % to
> −16 % relative to the Gaussian case."

I checked all 34 bibliography entries. **None** of the following appears:

1. LoVerde, Miller, Shandera & Verde (2008) — the correction the whole calculation rests on;
2. Eisenstein & Hu (1998) — the transfer function;
3. Planck 2018 cosmological parameters / the Planck f_NL constraint, which is also the
   implicit basis of "far outside current CMB and large-scale-structure constraints";
4. any source at all for the f_NL = −35/16 prediction, which is presented as a derived
   value of "this programme" with no reference, no derivation, and no appendix.

This is a citation-completeness failure that ApJS will not pass. A reader cannot check any
part of this paragraph.

**Required fix**: add all four references. The −35/16 prediction must be given a citation
to its source paper or an explicit derivation; if it is unpublished work of the author's,
say so and cite the preprint.

### AF-E5 — Sec. IX, p. 15: the Data Availability statement is an unresolved placeholder

> "[placeholder: Zenodo DOI for the public deposit]"

rendered in red in the compiled PDF. In addition, the repository itself is identified only
as "the project repository under results_2026-08-07/phase3_v2 and
flagship_assembly_2026-09-18 (both under pipelines/p1_highz_tracers/)" with **no URL, no
DOI, and no access instructions**, and "mirrors on Hugging Face and Backblaze B2" with no
locations. For a paper whose entire claim is provenance and third-party re-runnability,
the deposit is currently unlocatable by a reader.

**Required fix**: mint the Zenodo (or equivalent) DOI, cite it, give the repository URL,
and give the resolvable mirror locations. Also note that Table VI V2 ("every released
artifact's SHA-256 equals the value in the landing receipt") is unverifiable by a referee
until the deposit exists.

---

## MAJOR

### AF-M1 — Sec. V A, p. 7: direct self-contradiction about V1, propagated into the abstract

> "Eleven requirements pass outright (V1–V10, V3b)."

followed four sentences later by

> "V1 is a partial pass: it verifies TARGETID > 0, the one of its three provenance-gate
> conditions that survives in the published file…"

A check cannot simultaneously "pass outright" and be "a partial pass". The abstract
inherits the error — "sixteen machine-checkable requirements (eleven pass outright…)".
Compounding this, the V1 requirement in Table VI is written as
"gates/check_sample_provenance.py exits 0 on the released sample tables (TARGETID > 0;
OBJTYPE/FIBERSTATUS **where carried**)" — the clause "where carried" is an escape hatch
that makes the requirement unfalsifiable and guarantees a PASS regardless of what the
deposit contains. A validation contract whose items are written to be passable by the
data at hand is not a contract.

**Required fix**: mark V1 as PARTIAL (or NOT-CHECKABLE) in Table VI, correct the counts in
Sec. V A and the abstract to "ten pass outright, one partial", and remove the "where
carried" clause so the requirement states the three conditions unconditionally.

### AF-M2 — Sec. III B p. 3 / Sec. V E p. 10 / Abstract: the provenance gate, the paper's second contribution, cannot be re-verified from the release

> "the absent OBJTYPE and COADD_FIBERSTATUS columns, whose absence means the provenance
> gate cannot re-verify its own first two conditions from the published file alone."

The abstract says only "Applying the provenance gate (OBJTYPE = TGT, COADD_FIBERSTATUS = 0,
TARGETID > 0) before any score cut and a pre-declared threshold rule, yields a released
catalogue of 1,244 objects", with no indication that two thirds of that gate is not
re-checkable by a third party. Sec. III B goes further and calls the gate "enforced by a
committed, re-runnable checker" without qualification. The headline framing of the
manuscript — a gate a reader can re-run — is therefore stronger than the deposit supports.

**Required fix**: add the two columns to the deposit (the correct outcome), or state the
limitation in the abstract and in Sec. III B, not only in Sec. V E.

### AF-M3 — Table IV, p. 5 vs. Sec. V E p. 10 and Table VI DEFECT-1: the schema table omits a column the manuscript names twice

Table IV caption: "all 192 released columns accounted for". Its DESI-pipeline group lists
exactly four columns: `z, zwarn, spectype, deltachi2`. But Sec. V E says

> "the enriched table's z, ZWARN, SPECTYPE and SUBTYPE columns are unpopulated"

and Table VI DEFECT-1 says "the enriched table's zcatalog columns (z, zwarn, spectype,
**subtype**) are populated". Either `subtype` is a released column and Table IV is
incomplete (and the count is 193, not 192), or it is not released and the two defect
statements name a column that does not exist. Both readings are defects in the manuscript's
central schema table.

**Required fix**: reconcile. If `subtype` is released, add it to Table IV and correct 192 →
193; if not, remove it from Sec. V E and from DEFECT-1.

### AF-M4 — Sec. VII B, p. 14: the AB-magnitude conversion is wrong by 0.3 mag

> "so a 4.33 nmgy g-band flux (≈ 20.6 AB mag, orders of magnitude above any plausible
> Legacy Survey noise floor)"

With the Legacy Survey/SDSS nanomaggy zero point, m_AB = 22.5 − 2.5 log₁₀(f/nmgy):
4.326 nmgy → **20.91 AB mag**, and 4.33 nmgy → 20.909. The quoted 20.6 corresponds to
5.75 nmgy, which is not any value in Table XI. The conclusion (the object is far above the
noise floor) is unaffected, but in a manuscript that stakes its case on "every number in
this manuscript names its source artifact", a hand-computed number that does not reproduce
is exactly the failure mode the paper claims to have engineered away — and it occurs in
the one follow-up test the paper actually executes.

**Required fix**: correct to ≈ 20.9 AB mag, and state whether this conversion is emitted by
`outputs/draft_numbers.json` or was computed by hand outside the pipeline. If the latter,
move it into the pipeline.

### AF-M5 — Sec. V C p. 8, Table IV p. 5, Fig. 6 p. 10: r_B, r_R, r_Z are never defined

The per-camera residuals `rB`, `rR`, `rZ` carry the manuscript's central diagnostic
(Sec. V C, contract item V11, Fig. 6, and the `r_B` column of Table VIII), yet nowhere is
it stated what they are. Are they per-camera mean squared error, RMS residual, median
absolute residual? Are they normalised, and by what? Their units are never given, and the
Fig. 6 axes read only "r_B (per-camera residual)". The reader is told "median residuals
are correspondingly lopsided: r_B = 2.53 versus r_R = 1.03 and r_Z = 0.94" without knowing
what is being compared. This also blocks any independent check of the variance
decomposition of AF-E3, because the reader cannot tell why R²(mean_mse | r_B, r_R, r_Z) is
0.777 rather than 1.000 when `mean_mse` is presumably an aggregate of the three.

**Required fix**: give the defining formula for r_B/r_R/r_Z alongside Eq. (1), state
units, and state their exact relation to `mean_mse`.

### AF-M6 — Sec. V C, p. 8: the "94.9 % worst-fit camera" statistic has no control

> "the b camera is the worst-fit camera for 1,180 of the 1,244 released objects (94.9 %;
> 60 for z, 4 for r)"

This is presented, in the abstract and body, as evidence that the score is b-arm driven.
It is not, on its own, evidence of anything: the released sample is the top 5.7 × 10⁻⁵ tail
of a reconstruction-error statistic, so conditioning on S > 3 guarantees an extreme camera,
and if the b arm is simply the noisiest arm it will be the worst-fit camera at high rate
everywhere in the survey, not only in the tail. The manuscript acknowledges the noise
reading elsewhere but never supplies the control. The required comparison — the
distribution of `worst_band` over the full 21,793,550-target scan, or at minimum over a
matched-S control sample — is computed from data the author already has (the scan
summary), and its absence leaves the paper's second-most-repeated quantitative claim
uncalibrated.

**Required fix**: report the base rate of `worst_band` over the full science-target scan
and over a set of score-matched controls, and restate the 94.9 % as an excess over that
base rate.

### AF-M7 — Sec. VI C p. 11, Fig. 8 p. 12, contract item V12: a 50-draw permutation null cannot support the claim made from it

> "its silhouette over the 128 latent dimensions is −0.0162, against a 50-draw
> label-permutation null of −0.0244 ± 0.0039 whose largest draw is −0.0184 (check V12,
> Fig. 8). The observed value exceeds every permutation draw, so the empirical p < 1/50."

Fifty draws sets a resolution floor of p ≥ 0.02 — the reported "p < 1/50" is the *only*
statement the design can make, regardless of how strong the effect is, so the p-value
carries almost no information. On the parametric side the effect is
(−0.0162 + 0.0244)/0.0039 = 2.1σ. Fifty permutations of a label vector on 675 objects costs
seconds.

**Required fix**: run ≥ 10⁴ permutations and report the empirical p-value properly
(including the (r+1)/(n+1) convention). This is also a contract item, so V12's outcome
string must be regenerated.

### AF-M8 — Sec. VI C p. 11, contract item V12: the permutation null is unstratified and the result is confounded by survey/programme

The manuscript states in Sec. VI B that

> "Because the clustering features are the score and the sky position, the families are in
> practice a score-tier × survey/programme stratification. Table IX makes this explicit:
> 70.4 % of objects lie in their family's dominant survey/programme cell"

If families are largely survey/programme cells, and different DESI surveys and programmes
observe different target classes at different exposure depths, then a *free* label
permutation will of course be beaten: the latent space encodes spectral shape, and
spectral shape differs between surveys and programmes for reasons that have nothing to do
with the taxonomy being meaningful. The V12 "structured" verdict, weak as it already is,
is therefore not established. The correct null is a permutation restricted **within**
(survey, programme) cells — which the author in fact names as a needed baseline in
Sec. VI A but does not run.

**Required fix**: repeat the silhouette test against a within-(survey, programme)
stratified permutation null and report that result as V12. If the observed silhouette no
longer beats the stratified null, say so and retire the "structured" language entirely.

### AF-M9 — Sec. II A, p. 2: the deduplication sensitivity is deferred rather than computed

> "The deduplication rule itself has no physical content: which of a repeated TARGETID's
> several DESI (survey, program) observations survives depends on shard file names and row
> order, not on which exposure is better. We have not quantified how many of the 1,244
> released objects sit near enough to threshold that their alternate duplicate would score
> below it, and record this as an open, unquantified caveat on near-threshold catalogue
> membership rather than assert it is small."

I credit the honesty, but for a catalogue paper this is the wrong disposition. Catalogue
membership — the paper's entire product — depends on an arbitrary rule, and the
sensitivity is directly computable from data already in hand: the scores of all 878,740
removed duplicate rows were produced by the same scan. The number of the 1,244 whose
alternate duplicate falls below S = 3 (and the number of objects that would enter if the
other duplicate had survived) is a single join.

**Required fix**: compute and report both numbers, add them as a contract item, and if the
churn is non-negligible, report the catalogue's membership stability as a released column
or flag.

### AF-M10 — Sec. III A, p. 3: the undocumented model is a caveat of abstract-level severity and is not in the abstract

> "its training corpus (parent survey, target classes, selection, any quality cuts, and any
> overlap with the 21.8 million science targets scanned here), its wavelength-to-bin
> mapping across the three cameras, and its architecture beyond 'convolutional autoencoder,
> 496 → 128' are not documented in any artifact this release controls."

and

> "if the training corpus is drawn from the same imaging/spectroscopic population scored
> here, objects inside it would carry an artificially low reconstruction error, a selection
> effect operating on the exact quantity that defines the catalogue"

A possible selection effect on the defining quantity of the catalogue is not a Sec. III A
detail. The abstract presents the model only as "An archived convolutional autoencoder,
bound by SHA-256 to a sealed run contract" — binding a model's bytes says nothing about
whether its selection function is knowable, and a reader of the abstract alone would not
learn that the selection function is not merely unmeasured (OT-1) but potentially
*structurally biased* against already-observed objects.

**Required fix**: state the undocumented-training-corpus caveat in the abstract; and note
that this interacts directly with the Sec. V D benchmark — if the training set overlaps
the reference classes, a null recovery is partly explained by construction, which the
manuscript never considers.

### AF-M11 — Sec. V D p. 9, Table VII p. 10: the benchmark's only quantitative output depends on an unjustified and inconsistent match radius

Sec. IV D uses **3″** for SIMBAD/NED; Sec. V D uses **1.5″** for the five reference classes.
Neither radius is justified, the difference is never explained, and no sensitivity test is
reported. The recovery benchmark is the result the paper's entire framing rests on ("This
is the result that makes the present work a data release with a validated selection rather
than a discovery paper"), and its output is a single match out of 8,036 reference objects —
a quantity that a factor-two change in radius could plausibly move.

**Required fix**: justify both radii against the DESI fibre positioning accuracy and each
reference catalogue's astrometric precision, and report recovery counts at (at minimum)
1″, 1.5″, 3″, and 5″ so the reader can see the null is not a radius artefact.

### AF-M12 — p. 17: an internal bibliography-QA audit log is printed in the manuscript, and it does not add up

> "The four citations not recorded in any committed benchmark artifact (Ref. [25]'s
> journal/volume/page, and the three software citations Refs. [31, 32, 34]) were verified
> against ADS for this manuscript (2026-09-19): … All four entries below already carried
> the correct values; no bibliography text changed."
>
> "The remaining 26 entries below were separately ADS/journal-verified (2026-09-21): every
> journal, volume, and page matches the publisher's or ADS's record exactly, including the
> three least-common entries … No bibliography text changed as a result."

This is an internal manuscript-QA record. It has no place in a published paper — no ApJS
paper narrates its own reference-checking dates, ADS bibcodes of already-correct entries,
or the fact that no text changed as a result. It reads as working notes left in the file.

It is also arithmetically wrong as written: 4 + 26 = 30, but the bibliography contains **34**
entries. I can reconstruct the intent (four entries — [3] NED, [6] Redrock in-prep, [13]
DESI Data Model, [33] Apache Arrow — are web/in-preparation and not ADS-verifiable), but
the text never says this, so as printed the accounting is short by four.

**Required fix**: delete both paragraphs entirely. Reference verification is a
pre-submission activity, not manuscript content.

### AF-M13 — Title page, p. 1: internal draft version tag printed under the author block

> "(Dated: September 21, 2026 (vAF.0.5))"

`vAF.0.5` is an internal document-version identifier from the author's drafting pipeline.
It must not appear on a submitted manuscript.

**Required fix**: remove the version string from `\date`.

### AF-M14 — Sec. V B, p. 7: the manuscript addresses the referee directly

> "A referee should read V10 as closing one explanation, not as opening another."

Instructions to the referee belong in a cover letter, not in Sec. V B of the paper. A
published version of this sentence would be addressed to a person who no longer exists in
the reader's world.

**Required fix**: rewrite as a statement about the result ("V10 closes one explanation; it
does not open another"), and check the manuscript for further instances of this register.

### AF-M15 — Sec. VII B, pp. 13–14: leftover version-history language comparing this draft to an earlier one

Three instances, all of which assume the reader has seen a previous version of this
manuscript:

- p. 13: "We apply that test uniformly below, **which changes one of this section's
  conclusions relative to the released g-only check.**"
- p. 14: "for two distinct reasons, and **we no longer report one of them as supported**."
- p. 14: "until then this tier's verdict is one refuted, three undecided, **not one
  refuted, one supported, two undecided**."

A reader of the published ApJS article has never seen the g-only check, has never been
told any candidate was supported, and cannot parse "no longer". This is version-control
narration, and it is exactly the kind of internal bookkeeping that must be stripped before
submission.

**Required fix**: state the tier verdict positively and only once — "one refuted, three
undecided" — and delete all comparative language referring to earlier drafts or earlier
releases of this same analysis.

### AF-M16 — Manuscript format: abstract length and document class are both out of compliance for ApJS

The abstract is approximately **590 words**. The AAS journals limit abstracts to **250
words**. Separately, the manuscript is set in RevTeX two-column (PRD) style; ApJS requires
AASTeX (6.3 or later).

**Required fix**: cut the abstract to ≤ 250 words and re-set the manuscript in AASTeX.
Note that the abstract cut is not cosmetic here — it will force a decision about which of
the six contributions actually leads, which in my view would improve the paper.

### AF-M17 — Acknowledgments, pp. 16–17: two broken cross-references, and they are swapped

> "All computation for this manuscript's assembled numbers **(Sec. A)** ran locally on the
> author's own hardware at zero incremental cost. The upstream scan and characterisation
> stage **(Sec. 2)** used a single low-cost RunPod GPU rental ($1.31 total)"

Neither "Sec. A" nor "Sec. 2" exists — the manuscript numbers its sections I–XI with one
"Appendix A". Both look like `\ref{}` calls resolving against the wrong counters. Worse,
Sec. IX labels these **Stage A** (scan and characterisation, GPU, $1.31) and **Stage B**
(every number in this paper, local, free) — so the acknowledgment attaches label "A" to the
assembled-numbers stage, which is Stage B, exactly inverting the manuscript's own labels.
This lands in the compute-provenance statement, which is a place this paper cannot afford
to be sloppy.

**Required fix**: repair both references to point to Sec. IX's Stage A and Stage B, in the
correct order.

### AF-M18 — Sec. VIII, p. 15: a number in the paper is produced by a script outside the sealed provenance chain

> "The full computation is the committed, deterministic script
> `ledger6_png_highz_abundance.py` (no fitting, no randomness), SHA-256 f1121e2b79c4…,
> whose output is `ledger6_png_highz_abundance.json`."

Neither artifact appears in Table I's thirteen hash-bound artifacts, nor among the nine
released data products re-hashed against the landing receipt (V2), nor in the manifest
chain (V3). This directly contradicts Sec. II B: "Every stage binds the exact SHA-256 of
its input and output under a single sealed run contract". A partially-sealed chain in a
paper titled "provenance-sealed" is a real defect, not a technicality.

**Required fix**: either bring this script and its output into the run contract, Table I,
and check V2, or state explicitly in Sec. VIII that this computation sits outside the
sealed chain and why.

### AF-M19 — Sec. VIII, p. 15: the f_NL sub-calculation is out of scope, unsupported by shown work, and under-specified

Beyond the missing citations of AF-E4, the calculation itself is reported only by its
conclusion. The stated shift is "−6 % to −16 %" over a range "z ≈ 10–14, log M_h/M_⊙ ≈ 11.5"
with no indication of which end of the range gives which number, no halo mass function
variant named beyond "Planck-2018 ΛCDM", and no σ₈/n_s/Ω_m values. The follow-on claim

> "a factor-of-two abundance effect at this halo mass and redshift would require
> |f_NL| ∼ 30"

is an extrapolation by a factor of ~14 in f_NL from a computation shown only at
f_NL = −2.1875, presented without the intermediate curve. Linear scaling of the quoted
range gives 14–36, so "∼ 30" is inside the plausible band but is not established by
anything printed.

More fundamentally: this is a separate cosmology calculation with no dependence on the
catalogue, in a data-release paper, in a section the author introduces by warning against
over-connecting the catalogue to cosmology. I would cut it. If it stays, it must be
supported.

**Required fix**: either move Sec. VIII's second half to a separate paper/appendix, or
supply the cosmological parameters, the mass-function variant, a figure of abundance shift
versus f_NL across the quoted redshift and mass range, and the four missing citations.

---

## MINOR

### AF-N1 — Sec. VI A, p. 10: wrong table cross-reference
> "and Table VIII's own RA spans (up to 350° for one family)"

RA spans appear in **Table IX** (350.4° for family 0), not Table VIII, which has no RA
column. Fix the reference.

### AF-N2 — Sec. VII B, p. 12: stated Lyman-α wavelength does not match the one used
> "A quasar at redshift z places Lyman-α at 1216 (1 + z) Å"

The four quoted break wavelengths (6484, 7530, 8587, 8616 Å) reproduce from **1215.67** Å,
not 1216 Å (which gives 6486, 7532, 8590, 8619). Quote the value actually used.

### AF-N3 — Table X, p. 13: the tier rules cannot be audited from the table
Table X carries no `deltachi2` column and no `family_id` column, so neither the FT-C rule
("ZWARN = 0, Δχ² > 25 and S in the top 5 %") nor the claim "three of the five are in family
3" (Sec. VII A) nor FT-E's "highest-score member of each cluster" can be checked against
the printed table. Add `deltachi2`, `family_id`, and `cluster_id` columns.

### AF-N4 — Sec. IV D p. 6 vs. Table XI caption p. 13: an identical value for two different quantities
Sec. IV D: "median r-band flux 0.289 vs. 0.184 nmgy". Table XI caption: "the sample-wide
median f_g is 0.289 nmgy". The same number, 0.289 nmgy, is reported as (a) the median
r-band flux of the 569 matched objects and (b) the median g-band flux of all 1,244. Please
confirm this coincidence is real and not a transcription of one quantity into the other's
slot; if real, it is worth a parenthetical so the reader does not stumble.

### AF-N5 — Sec. IV D, p. 6: undefined signal-to-noise units
"median coadd r-band signal-to-noise 0.079 vs. 0.046" — values well below unity for a coadd
S/N need a per-pixel or per-Å qualifier and a definition; as printed they read as an error.

### AF-N6 — Sec. VII A, p. 11: the FT-A rule as stated does not produce "quasar candidates"
The rule is given as "ZWARN = 0 and z ≥ 4", with no SPECTYPE condition, yet the tier is
described as "four anomaly-selected DESI-pipeline z ≥ 4 quasar candidates" and all four
rows in Table X carry SPECTYPE = QSO. Either the rule includes SPECTYPE (state it) or say
that all four selected objects happen to be pipeline-classified QSO.

### AF-N7 — Sec. VII C OT-4, p. 15 vs. Sec. V D, p. 9: imprecise restatement
OT-4: "Six of eleven candidate reference classes lacked usable positions". Sec. V D says
four lacked identifiable coordinate columns, one had no known catalogue identifier, and one
timed out. Only four of the six lacked positions. Restate.

### AF-N8 — Sec. V B, p. 7: a p-value that does not quite reproduce
ρ_s = +0.058 at n = 1,244 gives a two-sided t-test p ≈ 0.041, not the quoted 0.039. The
difference is rounding in ρ; either give ρ to three decimals or the p to one significant
figure.

### AF-N9 — Sec. IX, p. 15: the artifact that carries the number-to-source mapping is not deposited
> "Every number in this manuscript names its source artifact in a comment in the LaTeX
> source."

The LaTeX source is not among the deposited items listed in Sec. IX. Deposit it, or move
the mapping into `outputs/draft_numbers.json` where the reader can reach it.

### AF-N10 — Sec. VII B, p. 14: DR10 forced photometry is invoked without a DR10 citation
"Legacy Survey DR10 forced photometry with inverse variances" is named as the immediate
next step, but the only Legacy Survey citation is Dey et al. 2019 [20], which predates DR10.
Cite the DR10 release.

### AF-N11 — Title block, p. 1: incomplete author metadata
"Hubify Research" carries no postal address; no ORCID is given. ApJS requires a full
institutional address and strongly expects an ORCID.

### AF-N12 — Fig. 1 caption, p. 4: the caption omits the non-monotone top bin that the figure plots
> "The fraction exceeds 99.5 % in every bin and rises monotonically to 99.97 % in [8, 10)."

The plotted top bin, [10, 24.42], falls to 99.70 %, which is visible in the figure and
explained in the abstract but not in the caption. Add the last bin and its sparsity to the
caption so the figure is self-contained.

### AF-N13 — Sec. III B p. 3 / contract item V9: state the pass margin
The [3, 4) bin sits at 99.53 % against a "> 99.5 %" requirement — a 0.03 pp margin on a
threshold that appears to have been chosen after the fact. State the margin explicitly, or
restate V9 as "the minimum per-bin sky fraction is reported" rather than as a threshold
test.

### AF-N14 — Sec. VI A, p. 10: self-contradictory wording
> "This construction has three undisclosed weaknesses we record rather than silently carry."

They are disclosed, in this sentence. Reword to "three weaknesses".

---

## NIT

### AF-N15 — Dated internal working paths in body text
`blue_arm_diagnostics_2026-09-19.py` (Sec. V C and Sec. IX), `results_2026-08-07/phase3_v2`,
`flagship_assembly_2026-09-18`, `PHASE3_V2_LANDING_2026-09-03.md`. Date-stamped
working-directory names read as internal bookkeeping. Give stable deposit paths and, if
the dates are provenance-relevant, record them in the manifest rather than the prose.

### AF-N16 — `ledger6_png_highz_abundance.py` (Sec. VIII)
"ledger6" is an internal task-tracker row label surfacing in a published filename. Rename
for the deposit.

### AF-N17 — Sec. IV B, p. 4: uniform ZWARN
All 742 unreliable redshifts carry exactly ZWARN = 4 (SMALL_DELTA_CHI2), with no other bit
set anywhere in the sample. State explicitly that no other ZWARN bits occur (and, if the
provenance gate removed them, say so), because as written it reads as suspiciously uniform.

### AF-N18 — Eq. (1), p. 2
The overline on MSE denotes a mean over the 496 input bins of a single spectrum; say so in
the sentence following the equation, since an overline more naturally reads as a
population average.

### AF-N19 — Table VI, V1 requirement text
"(TARGETID > 0; OBJTYPE/FIBERSTATUS **where carried**)" — see AF-M1. A requirement that is
conditional on what the data happen to contain cannot fail, and should not be listed
alongside requirements that can.

### AF-N20 — "AI-assisted methodology" note, p. 17
The note is well-judged in content, but it floats between the Acknowledgments and
Appendix A with no section anchor. AAS journals expect such statements inside the
Acknowledgments.

---

## Assessment of the framing, for the record

I want to be explicit that the manuscript's central editorial decision — to report a
negative recovery benchmark as a negative benchmark, to name the catalogue's defects in a
numbered contract rather than bury them, and to write a "What this catalogue is not"
section — is correct, and I have not treated any of it as a weakness. Sections V D, V E,
and X are the best parts of the paper. The manuscript is also numerically careful to a
degree I do not usually encounter: I attempted roughly fifty independent recomputations and
found exactly one wrong (AF-M4).

What holds it back is that the paper does not consistently meet the standard it sets for
itself. It is a provenance paper with a placeholder DOI and an out-of-chain script; a
reproducibility paper with a section that states it is not reproducible; a paper about
validated selection whose selection gate is not re-verifiable from the deposit and whose
flagship contract item is written so it cannot fail; and a paper about every number being
real whose most-repeated statistic is attached to the wrong model. Each of these is fixable
with work the author has already shown is cheap and mostly already has the inputs for. None
requires new observations.

---

## Recommendation

**MAJOR REVISIONS**

This is a genuinely useful data product with an unusually honest framing and an unusually
clean numerical spine, and I expect it to be publishable in ApJS. But five ESSENTIAL items
stand between it and acceptance, and none is cosmetic: Sec. VI is by the author's own
statement not reproducible and is built on a metric the author has diagnosed as defective
while calling the fix cheap (AF-E1, AF-E2); the R² = 0.78 that appears in the abstract, the
contributions list, and the conclusions is attached to the wrong regression and is
contradicted by the body's own drop-one numbers (AF-E3); the f_NL section rests on four
sources that appear nowhere in the bibliography (AF-E4); and the Data Availability statement
is an unresolved placeholder with no repository URL (AF-E5). Added to these are a
self-contradiction about V1 that propagates into the abstract, a schema table that omits a
column the paper names twice, an uncontrolled headline statistic, a 50-draw permutation
test with an unstratified null, a wrong magnitude conversion, and a substantial residue of
version-history and internal-QA language — including a printed bibliography-audit log, a
draft version string on the title page, a sentence addressed to the referee, and three
"relative to the previous version" constructions — none of which can appear in print. The
manuscript also needs to be re-set in AASTeX with a ≤ 250-word abstract. I would be glad to
review a revised version; most of this work is the author's own stated next step.
