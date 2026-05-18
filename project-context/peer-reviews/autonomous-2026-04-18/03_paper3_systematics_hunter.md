# Paper 3 — Systematics Hunter review (autonomous, 2026-04-18)

**Reviewer role:** Cross-survey catalog-validation specialist. Focus: selection effects, flux calibration, hemispheric systematics, in/out-of-sample bias, injection-recovery, dedup, and the gulf between "not in SIMBAD" and "truly novel."

**Source read:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (1,032 L, revtex4-2), SSOT `project-context/SSOT/paper-3/status.md`, `projects/cross_survey/results/P3-B-DESI-EXT_findings.md`, `projects/cross_survey/results/P3-B_findings_v2.md`, `projects/cross_survey/desi_xmatch_crossmatch.py`, `pipelines/p3_anomaly_engine/fisher_full/fisher_result_v2.json`, `pipelines/h200_results/multi_survey_summary.json`, `pipelines/h200_results/injection-recovery/injection_recovery_summary.json`, `pipelines/p3_anomaly_engine/p3a_tess_374313355_lomb_scargle/RESULTS.md`.

---

## Headline

**Paper 3 is largely publishable, but its honesty layer is unevenly deployed and contains two concrete, high-impact defects the reviewer's-eye check flagged on first pass.** The SIMBAD-novel reframing (§5.1 + §7 + abstract) has been substantially improved via the fire #20/#21 audit and is now mostly coherent; the DESI 82.2 % archival-ID and SDSS 100 % archival-ID numbers are both in the footnote on L382 and the limitations paragraph at L600. That part is good. But:

1. **The CMB injection-recovery study was run and it FAILED catastrophically (0.33 % recovery at 99th percentile across 1,200 injections), and that failure is not cited anywhere in the paper.** This turns the Planck/ACT rows of Table 1 from "methodological control" into "undertrained + unvalidated," and makes the §4.4 Planck × ACT null claim a much weaker statement than the text implies.
2. **Train/test contamination is not acknowledged.** BigAE was trained on 47 K DESI spectra, then applied to score 22.5 M DESI spectra. The 0.87 % DESI anomaly rate is an in-sample detection on the same distribution the model learned to reconstruct — it is not directly comparable to the SDSS/LAMOST transfer-learning rates, yet §5.1's "DESI achieves 99 % novelty among the top 10,000" is quoted against those out-of-sample rates with no bias caveat.

Additional smaller issues around abstract-level QC flagging, cross-survey dedup, the TIC 374313355 typing, and the missing machine-readable residual-novel catalog are listed below.

**Verdict:** Accept with moderate revisions. The paper should not hit arXiv in its current form; the two items above are each ~1-2 days of work and would materially improve reviewer reception.

---

## Major

### M1 · CMB injection-recovery ran, failed, is not in the paper

`pipelines/h200_results/injection-recovery/injection_recovery_summary.json` reports a completed injection-recovery study on the CMB autoencoder:

- 1,200 synthetic anomalies injected (6 amplitude levels × 200 each, spanning 0.5× – 20× the noise floor)
- **Overall recovery rate at the 99th-percentile threshold: 0.33 % (4/1,200)**
- **At 5× noise amplitude: 0 % recovery.** At 10× and 20×: 0 % recovery.
- False-positive rate: 1.0 % (by construction, the top-1 % cut)
- Model validation loss: 0.617 — consistent with the "undertrained" flag on Planck/ACT from CLAUDE.md

This is a real result and a real datum. It says the CMB BigAE cannot recover even obvious planted cold spots. That directly bears on §4.4's claim:

> "The Planck × ACT cross-correlation yields a null result … confirming that microwave anomalies trace foreground or noise rather than primordial signals, an important negative result for proposed CMB anomaly detection programs."

The current text frames the null result as evidence about the sky. The injection-recovery result says the null is at least partly evidence about the **detector**: a CMB autoencoder that misses 99.67 % of planted anomalies cannot detect real primordial signals either, so failing to see Planck × ACT agreement is uninformative at the top-of-paper level.

**Fix options (pick one, all are DO-NOW):**

- **Preferred.** Add a one-paragraph subsection to §3.5 or §7.3 titled "CMB autoencoder limitations: injection-recovery" that reports the 0.33 % recovery number, the per-amplitude breakdown (including the 0 % at 5×, 10×, 20×), and explicitly reframes §4.4 as jointly limited by sky systematics and detector undertraining. Point at `injection_recovery_summary.json`.
- **Minimum.** Add a footnote on the §4.4 null-result paragraph stating that injection-recovery on the CMB model recovers only 0.33 % of planted anomalies at 99 %, so the cross-correlation null is not a strong constraint on primordial non-Gaussianity.
- Either way, promote the "Planck + ACT: QC FAIL" flag out of the CLAUDE.md context and into the paper itself.

Without this, external readers will cite the Planck × ACT null as if it is an upper bound on primordial anomaly signals. It is not.

### M2 · Train/test contamination on DESI is not acknowledged

BigAE for DESI is trained on 47 K representative DESI spectra, then scored on the full 22.5 M DESI spectra (§2.2, §3.1). This is an in-sample detection. The 0.87 % anomaly rate therefore measures **the fraction of DESI spectra that reconstruct poorly against a model that was explicitly fit to minimize DESI reconstruction error**. By construction, this will tend to understate the true anomaly rate compared to a truly held-out or cross-survey rate.

That interpretation matters for three claims:

1. "0.87 % rate on DESI" vs "3.38 % on SDSS" (§3.1 / §3.2 / Table 1). §5.3 notes that the SDSS rate is inflated by cross-survey mismatch, but does not note the **complementary** effect: the DESI rate is deflated by in-sample training. The comparison is asymmetric.
2. "Our DESI anomaly rate of 0.87 % is consistent with the 1.07 % rate reported by Liang+2023" (§5.5 / L605). Both are in-sample. The consistency is a consistency between two in-sample training regimes, not a bound on the underlying anomaly rate.
3. **SIMBAD-novelty extrapolation.** 99 % of the top 10 K DESI anomalies are SIMBAD-novel, but the top-of-distribution objects are exactly the ones BigAE fit worst during training — a known in-sample optimizer pathology for autoencoders. Some of these may be "hard to reconstruct" rather than "astrophysically unusual."

**Fix options (all DO-NOW, no re-run required):**

- Add a one-paragraph "Train/test contamination" subsection to §7.3 Limitations. State the in-sample training regime explicitly. Quote the expected direction of bias (in-sample detection understates the true anomaly rate). Note that a cleanly out-of-sample validation would require either (a) a k-fold scoring regime on the 22.5 M spectra, or (b) training a held-out twin on a disjoint fibre pointing set.
- Add a sentence to the §5.5 "consistent with Liang+2023" comparison explicitly noting that both are in-sample.
- Reorder the novelty list in §4.1 so the reader sees "SDSS 90 % (out-of-sample, inflated)" paired with "DESI 99 % (in-sample, may include optimizer-residual objects)."

### M3 · Table 1 thresholds are heterogeneous; defensible but worth one paragraph

Table 1's anomaly rates (DESI 0.87 %, SDSS 3.38 %, LAMOST 0.39 %, eROSITA 0.03 %, Planck 1 %, ACT 1 %, Gaia 1 %, NEOWISE 1 %) use two different threshold protocols:

- **Fixed-score:** DESI, SDSS, LAMOST all use S > 5.0.
- **99th-percentile:** Planck, ACT, Gaia, NEOWISE all use top-1 % cuts. eROSITA uses 99th-percentile yielding 298 objects.

§2.2 L108 acknowledges this ("fixed score … or the 99th percentile of the score distribution"), but the three surveys that end up at exactly 1 % do so by construction, and a reader skimming Table 1 may read them as "independently converging at 1 % natural rate." They are not; they are a cut choice.

**Fix:** Add a one-sentence note under Table 1: "Rates for Planck, ACT, Gaia, NEOWISE are defined by the 99th-percentile cut, not by a natural break in the score distribution; the 1.0 % rate is therefore a catalog-design choice rather than an empirical anomaly fraction." This is a 30-second edit that prevents readers from reading too much structure into the row-level rate.

(eROSITA at 0.03 % is a genuinely extreme cut, quoted in the SSOT as 99th percentile producing 298 objects. The rate-versus-threshold story is legitimate there.)

### M4 · QC fail flags are not in the abstract or the data-availability statement

§7.1 (LAMOST blue-excess artifact, 98 % contamination) is prominent, to the paper's credit. But the other three QC-failed surveys (Planck, ACT, NEOWISE) are:

- **Planck.** Abstract calls the Planck × ACT result "null" without the "driven by survey-specific systematics" caveat; the caveat is only in §4.4.
- **ACT.** Same.
- **NEOWISE.** §3.8 says "physical interpretation uncertain." The ecliptic-latitude systematic (CLAUDE.md flags) is not discussed in the paper at all; nowhere does the paper acknowledge that the NEOWISE anomaly distribution is almost certainly dominated by scan-pattern systematics at the ecliptic poles.

The abstract claims 319,443 anomalies and 58.8 % novelty without a single-sentence "QC-failed surveys contribute N of these" disclosure. A reader who pulls the HuggingFace catalog and applies a position-weighted selection will be misled.

**Fix:**

- Add one sentence to the abstract: "Four surveys (LAMOST, Planck, ACT, NEOWISE) show quality-control failures (blue-excess training bias, undertrained CMB models, ecliptic-scan systematics); their contributions to the combined catalog are flagged in §3 and in the public data product."
- Data-availability section L645 should add: "Objects from LAMOST DR10, Planck CMB, ACT DR6, and NEOWISE are released with explicit `qc_fail=True` flags set; users are advised to exclude them for novelty-driven analyses unless the failure mode is understood."

### M5 · Cross-survey dedup is not addressed

The paper aggregates 319,443 anomalies across 8 surveys. Three of the 8 surveys (DESI, SDSS, LAMOST) have spectral overlap in the optical/NIR; two (eROSITA, NEOWISE) have spatial overlap; and one (Gaia) overlaps with all of the optical ones. The only dedup analysis quoted in the paper is the DESI × SDSS 3-arcsec cross-match in §4.3, which yields exactly 3 matched objects.

Three is implausibly small. A DESI × SDSS match over overlapping footprints on a 3-arcsec cone search against 195 K + 77 K anomalies should yield ~hundreds to thousands, not 3. Either:

- The 3-arcsec radius was applied in a non-symmetric way (e.g., on anomalies-of-both-surveys rather than on anomalies of either), in which case the 3 is the count of **agreed** anomalies, not the count of positional matches, and the text L418–420 is misleading.
- Or the footprints are nearly disjoint, in which case the paper should say so with a quantitative sky-overlap figure.

The distinction matters because if the catalog is deduped only on "both-independently-flagged" matches (3 objects), then the 319,443 total can contain the same physical object multiple times under different survey labels — e.g., a DESI QSO at z ≈ 1.55 that is also in the SDSS anomaly list under a different TARGETID.

**Fix (DO-NOW):**

- Run a positional cross-match of **all** anomalies across all 8 surveys at 5 arcsec, quote the N of unique physical objects vs the sum-over-surveys.
- If the unique count is meaningfully smaller than 319,443, update the abstract (quote both "319,443 survey-level detections" and "N unique physical objects").
- If instead the 3 in §4.3 is specifically "objects independently flagged in both DESI and SDSS," rewrite §4.3 to say so explicitly and contrast with the larger positional-match count.

### M6 · Fisher v2b calibration `sigma_base_frac = 1.4123` needs physical justification

The `fisher_result_v2.json` JSON comment calls v2b "the noise variance scaling only, so future PTAs correctly tighten sigma(gamma) monotonically," and calibrates `sigma_base_frac = 1.4123` to recover NG15's published σ(γ) = 0.506.

Two concerns:

1. **The physical meaning of α_noise.** The paper L561 describes α_noise as a "noise-floor scenario factor" such that `C = C_signal + α_noise · C_noise`. This is well-defined mathematically, but the mapping from α_noise to PTA epoch is stated as "α_noise = 0.5 for NG20, 0.2 for CPTA 2030, 0.05 for SKA 2035." These are numerology without a noise-budget derivation. Under what scaling law (T_obs^{-1}? N_pulsars × T_obs^{-13/3}?) does α_noise drop from 1.0 → 0.5 → 0.2 → 0.05? The paper does not say.
2. **The calibration is a post-hoc fit to the answer.** `sigma_base_frac = 1.4123` is explicitly tuned so that the present-day Fisher predicts σ(γ) = 0.506, matching NANOGrav's published value. That is the right sanity check at present epoch, but the onward extrapolation to 10σ at SKA depends on the fidelity of the forward model — which is the piece that has the fewest cross-checks.

**Fix:**

- Add one paragraph in §6 or Appendix stating the noise-budget model. Even `α_noise ∝ (T_obs/15 yr)^{-1}` with a citation to the PTA sensitivity literature would be enough.
- Add one sentence acknowledging that the calibration is a one-parameter fit to NG15 published σ(γ) and that this constrains the **present-day** Fisher but not the future-PTA scaling law.

---

## Minor

### m1 · TIC 374313355 classification is not what the review criteria said

The review prompt references "TIC 374313355 … SIMBAD-classified M9V ultra-cool dwarf." The on-disk P3-A RESULTS.md (`p3a_tess_374313355_lomb_scargle/RESULTS.md`) does NOT classify it as M9V. It reports:

- RA/Dec: (160.149°, +5.092°)
- Tmag = 18.52 — "below SPOC pipeline processing thresholds"
- P = 13.782 d, FAP = 3.9×10⁻²⁶³ (via `lightkurve.search_tesscut` FFI cutouts)
- Candidate types: detached eclipsing binary, long-rotation red giant, or long-period Cepheid/RR-Lyrae harmonic
- **Filed as P3-A-TYPING for follow-up SIMBAD/Gaia DR3 cross-match** — i.e., the typing is open

The paper §4.3 L423 states "appears in the TESS Input Catalog as a variable source" — weaker than the review-prompt claim, and arguably correct. But if somewhere the paper claims M9V ultra-cool-dwarf, **that claim is not supported by on-disk data** and should be pulled.

(I grepped the paper for "M9V" / "ultra-cool" / "Lomb" and did not find the M9V classification; §3.2 does say SDSS anomalies include M9 subtypes as a population, but that is not about TIC 374313355.)

**Fix:**

- Consider promoting the 13.782-d period and FAP = 4×10⁻²⁶³ into §4.3 body, since that IS a publishable detection. Current wording says only "The combination of spectroscopic anomaly and time variability makes it a strong candidate for follow-up observations." The Lomb-Scargle result already answers "follow-up observations" in the affirmative — fold the answer in.
- Do **not** add an M9V classification until the Gaia DR3 cross-match completes.

### m2 · eROSITA counts: paper vs review-criteria drift

The review criteria prompt lists "eROSITA DR1: 9,303 anomalies (1%)." The paper, the SSOT, and `multi_survey_summary.json` all agree on 298 anomalies at 0.03 %, which is 99th-percentile derived. The 9,303 number that appears in CLAUDE.md's context is a STALE figure — probably from an earlier pipeline run at a different threshold. This is not a paper bug, but the **SSOT and CLAUDE.md disagreement** should be reconciled in one commit. Paper 3 is internally consistent on 298.

### m3 · DESI 17.8 % residual-novel (178 objects) — no machine-readable table

L600 quotes "17.8 % (178/1000) that remains for spectroscopic follow-up." The per-object data for those 178 does exist (`projects/cross_survey/results/desi_xmatch_summary.json` contains all 1,000 with match status per catalog). But the paper does not publish these 178 RA/Dec + score anywhere a reader can act on.

**Fix:**

- Create `pipelines/p3_anomaly_engine/hf_staging/desi_top1000_residual_novel.csv` with columns `[tid, ra, dec, z, bigae_score, match_count_curated, catalogs_with_no_match]` for the 178 candidate-truly-novel objects. Reference the HuggingFace path from the data-availability statement.
- Add a line to §4.1 or §9 pointing readers to this list specifically.

This is the single most actionable follow-up list in the paper and it's currently buried.

### m4 · §9 data availability: commit hash / dataset version missing

L645 says "staged for release on HuggingFace at `huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog` (private until acceptance)." Once the HF upload is 100 % (SSOT has it at 61.7 % currently, per the review context), the statement should cite:

- An immutable version tag or commit hash on the HF dataset
- A DOI if one is issued
- The git commit hash of the `paper3_draft.tex` submission

Otherwise two years from now "the HF catalog" may be a different snapshot than what was reviewed.

**Fix:** L645 should read, once HF is at 100 %, something like: "the catalog is available at `huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog`, snapshot `v1.0.0`, dataset-hash `sha256:…`, corresponding to paper source at commit `<hash>`."

### m5 · Figures look fine on count (44 files in `figures/`), but two flags

I did not open all 21 PDFs, but the directory shows `.pdf` + matching `.png` for each figure (so both raster and vector are committed). Two concerns from the captions:

- **`fig_sdss_umap.png`** is the one figure whose source format is `.png` (L247) rather than `.pdf`. Vector format is preferable for scatter plots; if this is a rasterized UMAP it will look grainy on arXiv's compiled PDF.
- **`fig_novelty_fractions.pdf`** caption (L401–409) uses color to distinguish 6 surveys plus a dashed aggregate line. No color-blindness-safe flag; if any two of the six surveys render as indistinguishable for a red-green colorblind reader, that's a publication defect.

**Fix:** Convert `fig_sdss_umap.png` to PDF from source if the matplotlib `.pkl` is still on disk; if not, regenerate. Run all 21 figures through a color-blindness simulator once (e.g., `sim_daltonize`) and swap palettes only where needed.

### m6 · "One known QSO at z ≈ 1.55" — provide the TARGETID

§4.3 item 1 mentions "a known QSO at z ≈ 1.55" with no identifier. Anyone trying to reproduce the cross-match cannot. The other two items in that list (TIC 374313355, "uncataloged BAL QSO at z ≈ 0.86") are at least partially identifiable. Add the TARGETID to item 1.

### m7 · Bias enhancement α = 0.15 → latent-space 9.5 % improvement loop

§5.3 reports:

- Classification-based multi-tracer with α = 0.15: 6.1 % improvement
- Latent-space multi-tracer: 9.5 % improvement

The "latent-space" path bypasses the α assumption. If the latent-space result is more reliable (does not depend on the empirically uncalibrated α), why is the headline Table 2 result the α-dependent 6.1 % rather than the 9.5 %? Either:

- Put the latent-space 9.5 % in Table 2 as the headline, with the α-based 6.1 % as a more conservative alternative.
- Or explain in one sentence why the α-based forecast is the headline (e.g., "closer to a linear-bias interpretation that can be compared to Seljak2009 directly").

Either way, the reader currently sees the larger number in prose and the smaller number in the table, and is left to choose.

---

## Nitpicks

### n1 · Abstract number: "319,000" vs "319,443"

§1 Conclusions L621 quotes "319,000" for the scale, while abstract L53 and §3 L147 use "319,443." Pick one and use it consistently. (Both are fine; "319,000" in the Conclusions is a rounding choice, not an error, but readers track these.)

### n2 · NANOGrav 0.33σ vs 0.48σ

`multi_survey_summary.json` says "gamma=3.0 vs observed 3.2±0.6 (0.33 sigma)". Paper §6 says "γ = 3.20 ± 0.42 … consistent with the bounce prediction at 0.48σ" — the 0.48σ is (3.20−3.00)/0.42, with tighter error bar than the 0.6 used in the JSON. The paper uses the own-MCMC value (0.42) not the published NG15 value (0.6). That's fine, but the two numbers coexist in the internal files; update `multi_survey_summary.json` to match or add a provenance line stating which error bar was used.

### n3 · "eight astronomical archives" vs "eight surveys"

Paper uses both. Not a bug; minor.

### n4 · Acknowledgments section — no person-level acknowledgments

L642 acknowledges data sources, computing, and catalogs. Consider adding: "We thank the anonymous reviewer(s) / any collaborator who reviewed the manuscript." Not required for arXiv posting, but is standard PRD style.

### n5 · `preprintnumbers` option but no `\preprint` content

L41 is `\preprint{}` — empty. Either fill with an internal number ("BOUNCE-2026-03") for provenance or remove `preprintnumbers` from the documentclass options.

---

## Proposed new tasks (for SSOT queue)

Ordered by severity, each framed as a DO-NOW-eligible queue row.

| Task ID | Title | Estimated effort | Severity |
|---|---|---|---|
| P3-SYS-CMB-QC | Fold `injection_recovery_summary.json` 0.33 %-recovery result into §3.5 / §4.4 / §7.3 | 2 h | Major (M1) |
| P3-SYS-TRAIN-TEST | Add "in-sample detection caveat" paragraph to §7.3 Limitations; adjust §5.5 Liang+2023 comparison; flag in §3.1 and §5.1 | 1 h | Major (M2) |
| P3-SYS-TABLE1-NOTE | Add a 1-sentence footnote to Table 1 distinguishing fixed-score vs 99th-percentile thresholds | 15 min | Major (M3) |
| P3-SYS-ABSTRACT-QC | Add QC-fail disclosure to abstract + data-availability | 30 min | Major (M4) |
| P3-SYS-DEDUP | Full-catalog positional dedup across all 8 surveys at 5 arcsec, update N quoted in abstract | 4 h | Major (M5) |
| P3-SYS-FISHER-NOISE | Add noise-budget paragraph explaining α_noise scaling law | 1 h | Major (M6) |
| P3-SYS-TIC-PROMOTE | Promote P = 13.782 d + FAP = 3.9×10⁻²⁶³ Lomb-Scargle detection into §4.3 body | 30 min | Minor (m1) |
| P3-SYS-RESIDUAL-CSV | Export 178-object residual-novel CSV to `hf_staging/` and link from §9 | 1 h | Minor (m3) |
| P3-SYS-HF-VERSION | Add HF dataset version + commit hash to §9 once upload hits 100 % | 15 min post-upload | Minor (m4) |
| P3-SYS-FIG-AUDIT | Convert `fig_sdss_umap.png` to PDF; run 21 figures through color-blind simulator | 2 h | Minor (m5) |
| P3-SYS-QSO-ID | Add TARGETID for §4.3 "known QSO at z ≈ 1.55" | 10 min | Minor (m6) |
| P3-SYS-TABLE2-LATENT | Decide whether Table 2 headline is 6.1 % (α-dependent) or 9.5 % (latent-space) | 30 min | Minor (m7) |
| P3-SYS-CONSISTENCY | Reconcile CLAUDE.md eROSITA=9,303 vs SSOT/paper=298 | 15 min | Minor (m2) |

Total estimated effort for all 13: **~13 h** — well within a single on-pod work session. The 4 "Major" items (M1–M5, excluding M6 which is a mild framing issue) are each essential for a defensible arXiv submission.

---

## Verdict

**Accept with moderate revisions.**

- **Revise-and-resubmit items (block arXiv submission):** M1 (CMB injection-recovery disclosure), M2 (train/test contamination), M4 (QC-fail flags in abstract + data-availability), M5 (cross-survey dedup quantification).
- **Strongly-recommended items (should land but won't block arXiv):** M3, M6, m1, m3.
- **Nice-to-have items (land in v2 or reviewer response):** m2, m4, m5, m6, m7 and all n-items.

The core science is strong — the 82.2 % DESI / 100 % SDSS archival-ID audit, the Fisher v2b monotonicity fix, the LAMOST blue-excess methodological lesson, and the P = 13.782 d Lomb-Scargle on a Tmag = 18.5 target are all legitimate findings that belong in the literature. The revisions above are about making the paper honest about what it didn't do and what failed, not about the signal.

The pattern I see most clearly is the **asymmetry between good honesty on novelty (excellent) and missing honesty on model validation (absent)**. The SIMBAD → NED → VizieR → CDS X-Match reframing is exactly the right way to report archival follow-through. The same spirit has not been applied to the detector side: DESI in-sample training, CMB injection-recovery failure, and heterogeneous threshold selection all deserve the same transparency the novelty discussion got.

Fix M1–M5 and this paper is ready for `astro-ph.IM` + `astro-ph.GA` + `astro-ph.CO` cross-listing.

---

*Review generated by autonomous Paper-3 systematics-hunter agent, 2026-04-18. No paper source was edited; no commits were made. See task list above for proposed SSOT/queue rows.*
