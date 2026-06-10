# P3 R27conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper3_anomaly_catalog_v3.1.86.pdf` md5=31284b90 pages=26
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass 1 — PRD brutal referee (native PDF)

### E1 (none)
No exit-level errors. The new §II.B feature-scaling spec paragraph (eROSITA 47f / NEOWISE 15f / Gaia 20f-published + 21f-lineage-inferred) closes the long-standing "what exactly went into the autoencoder?" reproducibility gap for the three tabular surveys. Per-survey sections (§III.E eROSITA, §III.F Gaia, §III.G NEOWISE not directly visible in pp.1-6 but the §II.A architecture line "(47, 20, and 15, respectively)" cross-verifies). The count web (378,280 / 378,080 / 269,317 / 269,117 / 264,938 / 264,738 / 113,342 / 108,963 / 4,379) is internally consistent and traceable through the abstract, Table I footnote-$\spadesuit$, and Table I footnote-$\|$.

### M1 — "lineage-inferred" Gaia preprocessing is honest but leaves one reproducibility hole un-bounded
The new §II.B paragraph states: *"the exact 20-feature production script for the published 50K-source run was not recovered from any committed backup; its nearest committed lineage (`gaia_expanded.py`, a 21-feature/500K-source successor run) applies the same family recipe..."* This is admirably transparent — but a brutal referee will ask: what is the *bound* on the discrepancy? The 21-feature successor differs by *one* feature; which one? Could that 1-feature mismatch reorder the top-1% by more than the published Gaia 500-object cut? Recommend: add one sentence quantifying the worst-case ranking sensitivity (e.g., "the Spearman rank correlation between the 20f-published and 21f-recompute top-5,000 is $\rho > 0.9X$," or "the released 500-object membership list is invariant under add/drop of the 21st feature at $X\%$"). Even a back-of-the-envelope bound closes the audit; "lineage-inferred" alone reads as "we cannot reproduce this."

### M2 — eROSITA 47-feature spec mathematically inconsistent with the simpler description
§II.B reads: *"the feature vector is the 44 multi-band columns ML_RATE/ML_FLUX/ML_CTS/DET_LIKE over the 11 energy bands plus {EXT, EXT_LIKE, POS_ERR}"*. That gives $4 \times 11 + 3 = 47$ ✓ on a first read — but $4 \times 11 = 44$, not $11 \times 4$ explicit columns. A pedantic referee will note that the 11 energy bands × 4 column types should give 44 (correct), and that *"the 33 rate/flux/count columns receive a signed log(1+|x|) transform"* implies 11 (rate) + 11 (flux) + 11 (count) = 33 transformed columns, leaving 11 DET_LIKE columns *not* transformed plus the 3 categorical-ish columns. Recommend: add explicit parenthetical "(ML_RATE × 11 + ML_FLUX × 11 + ML_CTS × 11 are log-transformed; the 11 DET_LIKE columns and the 3 categorical-ish are standardized only)" — removes the residual ambiguity in the same paragraph.

### M3 — "98% blue-excess" LAMOST artifact framing leans on one assertion that needs a number
Multiple places in the paper (abstract, §I, Table I footnote-$\spadesuit$, §III.D LAMOST) repeat "98% blue-excess training-bias artifact." The 98% figure is the *fraction* of the cross-transfer LAMOST anomaly population whose peak residual sits in the blue arm — but the *causal link* to "training bias" rests on the comparison to the post-native-retrain population. Recommend: add one explicit sentence ("post-native-retrain blue-arm peak-residual fraction drops to X%; the X→98% delta is the training-bias attribution") so the headline 98%-blue-excess→training-bias inference is calibrated against the native-retrain control rather than asserted.

### M4 — "ACT DR6 quarantined" framing in §III intro deserves a one-line *why ACT specifically* in the abstract
The abstract says "ACT DR6 quarantined as a cross-transfer artifact" but the abstract reader is left to infer whether this is a known instrumental issue, a Path-C training failure, or a methodological scope choice. The §VI.A native-ACT-retrain paragraph (visible in pass 2 at tex line 920) clarifies it as a GPU-blocked native-retrain. Promote one sentence to the abstract: "ACT DR6 quarantined as a cross-transfer artifact (Path-C native retrain GPU-blocked at submission; documented but contributes zero objects to the headline)." Removes the only "wait, why?" moment in the abstract for a reader unfamiliar with the project history.

### m1 — Count web has too many numbers in one sentence
The abstract paragraph "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic, which double-removes the 4,379 LAMOST detections that merge into catalog-grade clusters at 5"" is correct *and* hard to parse on one read. Move the count-correction footnote to a Table I footnote (or to §III.D LAMOST section) and keep only "(269,317 catalog-grade / 269,117 point-source after dropping the 200 Planck patches)" in the abstract. The lesson-of-the-double-removal is great for the methods section but breaks reading flow in the abstract.

### m2 — "20 curated all-sky catalogs via CDS X-Match" cited without enumeration in the abstract
The abstract names "20 curated all-sky catalogs" for the 17.8% novelty fraction; the reader has to dig to §IV or §VI to find the list. Cheap fix: parenthetical "(SIMBAD, NED, AllWISE, Milliquas, Gaia DR3, SDSS, ...)" or a §IV.A pointer-cite.

### m3 — "BAL QSO at z≈0.86" cited as a discovery-class result without a per-object §
The abstract teases an "uncataloged BAL QSO at z ≈ 0.86" as one of the three highest-confidence DESI×SDSS cross-matches. Pass-2 search for "BAL" in the tex confirms it appears in the count-web sentence but the discovery-class object should have its own short subsection (§IV.B "Three high-confidence cross-survey detections" already exists per tex line 534; verify the BAL QSO has a row in Table IV or equivalent so a reader following the abstract can find the spectrum/coordinates).

### N1 — Tex comments at lines 73, 80, 101, 147 (R26→R27 changelog block)
Pass 2 confirms the changelog comments are accurate and match the v3.1.86 PDF render:
- Line 73: "lineage-inferred from gaia_expanded.py successor (disclosed). SII spec paragraph added." ✓ verified in PDF p.3.
- Line 80: "269,317/269,117 (prior 264,938/264,738 double-removed 4,379 LAMOST-overlap…)" ✓ verified in PDF abstract.
- Line 101: "378,604/378,280/378,145 unique, max variation 0.086% — deferred claim" ✓ verified in PDF tex line 536 (3″/5″/7″ sweep).
- Line 147: "All headline numbers preserved: 378,280 / 37.3M / 378,080 / 200 / 17.8% / 7.9%" ✓.

### N2 — June 2026 calibration intact
DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3, NEOWISE, ACT DR6 quarantined. SPHEREx 2028 forecast. Heinrich+2024 σ(f_NL)≈0.7 cited. NANOGrav 15-yr KDE free-spectrum γ=2.567±0.382 cited. All current as of June 2026.

## Explicit all-clears

1. **The new §II.B feature-scaling spec paragraph (R27conf priority).** Internally consistent with §II.A architecture (47/20/15) and §III.E eROSITA (47 features). The Gaia "lineage-inferred" disclosure is brutally transparent — exactly the framing this project committed to in `[[feedback-take-critiques-seriously]]`. ✓

2. **The count web (R27conf priority).** Headline 378,280 = 378,080 point-source + 200 Planck CMB. Catalog-grade 269,317 = 6-way dedup of DESI+SDSS+eROSITA+Planck+Gaia+NEOWISE (including 200 Planck patches). Catalog-grade point-source 269,117 = 269,317 − 200. The double-removed 264,938/264,738 are explicitly retired with arithmetic provenance. Per-survey native sum 388,493 = DESI 195,829 + SDSS 77,905 + LAMOST 113,342 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419 ✓. After 7-way 5″ dedup (10,213 duplicates), unique = 378,280 ✓. 8-way-with-ACT variant = 378,480 = 378,280 + 200 ✓. All internally consistent.

3. **Path-C native-retrain framing.** "Path-C native retrain is the core methodology" appears in abstract, §I, §II.D, §III.A, Table I footnote-$\|$, §VI.A. Cross-transfer 319,443 is preserved as before/after diagnostic, not headline. No mixed-tier ambiguity.

4. **Injection-recovery gate decomposition.** "3 PASS (SDSS 64%, Planck 100%, NEOWISE mask-geometry 100% — a masking-geometry sanity check that passes by construction, not a detector-sensitivity test) and 3 FAIL-with-diagnostic at 5σ (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%)" — the NEOWISE-is-geometry-not-sensitivity caveat is repeated in abstract, §III intro, and §VI.B (ii). Hostile referee cannot accuse the paper of inflating its PASS count.

5. **f_NL forecast caveat.** "central forecast σ(f_NL)=8.14 with 1σ envelope [3.92, 8.98]; the de-biased point estimate returns the single-tracer baseline σ(f_NL)^std=8.98 exactly (no improvement), so the central 9.4% improvement is a forecast pending higher-S/N follow-up, not a detection." This is exactly the right framing for a Path-C catalog paper — no over-claim of measurement.

6. **NANOGrav γ result framing.** "γ=2.567±0.382; matter-bounce γ=3.0 at +1.13σ (marginally consistent) and SMBHB γ=4.33 at +4.61σ (Savage-Dickey B_MB/SMBHB=7.14×10³ under the flat γ∈[0,7] prior; prior-sensitive by construction, and the SMBHB γ=4.33 is a population-mean reference value rather than a sharp prediction)." Prior-sensitivity disclosure prevents the standard PRD referee complaint about Bayes-factor laundering.

7. **N4-novelty hygiene.** Paper self-positions as the largest *catalog* (N3 first-of-kind multi-survey scale) and a *forecast* (not a detection) for f_NL. Compatible with `/never-claim-n4`.

## Pass-2 self-critique (PDF vs `pipelines/p3_anomaly_engine/paper3_draft.tex`)

- **Verified §II.B feature-scaling paragraph (tex line 225) matches PDF render verbatim.** The "byte-identical copies in two independent pod backups" provenance claim for `erosita_scan.py` is a strong reproducibility statement. ✓
- **Verified §II.A architecture sentence (tex line 199) matches PDF p.2:** "for photometric and catalog surveys (eROSITA, Gaia, NEOWISE), the input dimension matches the number of catalog features (47, 20, and 15, respectively)." Internal consistency between §II.A and §II.B is exact. ✓
- **Verified eROSITA §III.E (tex line 420): "Input: 930K sources characterized by 47 features."** Cross-section consistency. ✓
- **Verified Table I footnote-$\spadesuit$ (tex line 314):** the catalog-grade arithmetic `269,317 = 113,342 LAMOST exploratory − 4,379 LAMOST-overlap → 108,963 net LAMOST contribution → 378,280 − 108,963 = 269,317` is consistent (within rounding to the published `269,317` artifact). ✓
- **Pass-2 retrospect on M1:** worth keeping. "Lineage-inferred" is the right standard of honesty, but a 1-feature bound on the ranking-perturbation is a 30-minute compute that closes the audit cleanly. The catalog has the data to do it now.
- **Pass-2 retrospect on M2:** worth keeping. The 33-transformed / 14-not-transformed split is implicit in the §II.B paragraph but not stated. Trivial fix; removes the only ambiguity in an otherwise excellent reproducibility paragraph.
- **Pass-2 retrospect on m1:** the count-correction in the abstract *is* a 60-word digression in the middle of the most-read paragraph. Moving it to a Table I footnote is a strict improvement. But: it does demonstrate the count-correction-is-canonical framing Houston explicitly requested. Hold as minor presentation, not substantive.

## Summary recommendation

**Verdict: ACCEPT with MINOR revisions.** The new §II.B feature-scaling paragraph is exactly the kind of reproducibility prose this paper has been promising for the eROSITA/NEOWISE/Gaia tier; the "lineage-inferred" Gaia disclosure is admirable. The count web is internally consistent at PRD granularity, with the 269,317/269,117 catalog-grade tier cleanly derived and the retired 264,938/264,738 figures explicitly identified as double-removal arithmetic. Main remaining work: (i) bound the Gaia 20f/21f ranking perturbation, (ii) one sentence on the 47-feature transformation split, (iii) calibrate the 98% blue-excess attribution against the native-retrain control, (iv) one-line ACT-quarantine *why* in the abstract. Headline catalog claim (378,280 / 378,080 point-source) and f_NL forecast caveat are unaffected by any of these.

### Counts line
E=0 M=4 m=3 N=2 — accept w/ minor revisions
