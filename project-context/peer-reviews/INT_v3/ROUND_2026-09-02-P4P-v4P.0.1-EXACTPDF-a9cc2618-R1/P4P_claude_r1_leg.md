# INT Referee Report — P4′ (Claude Opus leg, R1)

- **Reviewer:** Claude INT referee leg (independent, skeptical ApJS referee stance; no expected verdict supplied)
- **Model:** claude-opus (claude-opus-5[1m])
- **Input PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`
- **sha256:** `a9cc26183c631ba88d021edc4b46f35a295832a9b1ceb7879aacf8d38253099f`
- **Pages:** 6 (letter, AASTeX 7.0.2 twocolumn); PDF ModDate 2026-09-02 12:57:48 PDT
- **Manuscript version:** v4P.0.1, dated September 2, 2026
- **Round label:** ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1
- **Date of review:** 2026-09-02
- **Target venue assumed:** ApJS (catalog paper)

## Evidence base actually inspected

- Full extracted text of the exact bound PDF (`pdftotext -layout`).
- LaTeX source `pipelines/p4prime_chirality_test/paper/main.tex` (569 lines) — grepped for every numeric claim quoted below (line numbers cited).
- Rendered pages 1–6 at 150 DPI and targeted crops of pages 4–5 at 300 DPI (`pdftoppm`). `main.log`: **0 Overfull/Underfull boxes, 0 undefined references, 0 LaTeX warnings.**
- Source paper P4: `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.274).
- Source paper P5: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.147).
- Exclusion script `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` and its committed output `research/bh_universe_dipole/outputs/poplawski_dipole_exclusion_2026_09_02.json`.
- md5 of `pipelines/p4prime_chirality_test/paper/fig_sky_map.png` vs. the P4 tree copies.

### Numbers I checked and found CORRECT (recorded so the disposition trail is complete)

| Claim in P4′ | Source | Status |
|---|---|---|
| 8,474,531 catalog objects | P4 abstract | ✔ |
| 949,584 HC spirals; exclude 59,515 `raw_flip_qc_unsafe`; 890,069 QC rows | P4 abstract + §"Declared Analysis Hierarchy" | ✔ (949,584 − 59,515 = 890,069) |
| N_support = 887,472 | P4 abstract | ✔ |
| A_dip = 0.467%, z_mom = +0.635, one-sided rank p = 0.238 | P4 abstract (p = 0.23768) | ✔ |
| A_95^obs ≃ 0.98% (full-amplitude, observed-label) | P4 Eq. `eq:a95_obs`; script `A95_OBS = 0.0098` | ✔ |
| 10⁴-draw fixed-occupancy label-randomization null | P4 | ✔ |
| DESIVAST GALZONE universe 694,642 TARGETIDs → 145,789 rows → 145,766 with `OUT=0` | P5 l.226, l.5533–5535 | ✔ |
| 31,937 void / 113,829 non-void (sum = 145,766) | P5 l.999, l.1244, l.1956–1957, l.3622 | ✔ |
| Δf_CW = +0.00145, SE = 0.00332, 95% CI [−0.00504, +0.00795], p = 0.661; wild-cluster p = 0.673 | P5 l.1003–1008 (+0.00145442, 0.00331502, [−0.00504290,+0.00795174], 0.66085, 0.67345) | ✔ exact |
| 812,793 env-labelled rows (T-Web); bar counts 428+6,673+408,187+397,505 = 812,793 | P5 l.693–704; Fig. 2 render | ✔ |
| Table 1 ratio column (7.1, 5.1, 2.0, 2.0, 20.4) | JSON `ratio_claim_low_to_A95_obs` = 7.143, 5.102, 2.041, 2.041, 20.408 | ✔ |
| Iye+2021 = arXiv:2011.00662; Patel & Desmond 2024 = arXiv:2404.06617 | refs [6], [7] | ✔ |

The measurement layer of this paper is sound and faithfully condensed. **Every finding below is about framing, figure identity, or omitted material — not about a wrong measurement.**

---

## FINDINGS

### MAJOR-1 — The "6 to 3,400 times smaller" sample-size claim is arithmetically false
**Location:** §5.2 last sentence, p. 4 (`main.tex` l.332); repeated in the Abstract, p. 1 (`main.tex` l.98, "a sample 6–3,400× larger than the comparison catalogs"); and in §6 Discussion, p. 4 ("At 8,474,531 total catalog objects and 887,472 in the primary supported-pixel test, this is the largest single sample brought to the question").

**What is wrong:** §5.2 states the literature samples are "6 to 3,400 times smaller than the present catalog's **supported-pixel sample**". The supported-pixel sample is 887,472. Against Table 1's own N column:

| Source | N | 887,472 / N | 8,474,531 / N |
|---|---|---|---|
| Longo 2011 | 15,158 | 58.6 | 559 |
| Shamir 2012 | 127,000 | 7.0 | 66.7 |
| Shamir 2020 | 200,000 | 4.4 | 42.4 |
| **Shamir 2022 (DESI Legacy)** | **1,300,000** | **0.68** | **6.5** |
| Shamir 2025 (JADES) | 263 | 3,374 | 32,223 |

Shamir 2022 is **larger** than the supported-pixel sample, not 6× smaller. The stated range mixes denominators: the "3,400" is 887,472/263 (supported-pixel sample), while the "6" is 8,474,531/1,300,000 (total catalog). No single denominator produces the quoted range. Consequently the Discussion's "this is the largest single sample brought to the question" is false for the primary test channel, and true only for the 8.47M-row catalog release — which is not the sample any of this paper's tests are run on.

**Evidence:** `main.tex` l.96–98, l.332; Table 1 as rendered on p. 4 at 300 DPI; arithmetic above.

**Required:** state the ratios against a single, named denominator, and either drop the "largest single sample" claim or restrict it explicitly to the catalog release while conceding that Shamir 2022 (the most directly comparable measurement — same survey) used a larger spiral sample than the primary channel here.

---

### MAJOR-2 — "More than an order of magnitude below" contradicts the paper's own Table 1 and its own Discussion
**Location:** §5.3, p. 4 (`main.tex` l.359–361); Abstract, p. 1 (l.95–97); §7 Conclusions, p. 5 ("well below the ∼7–33% amplitudes").

**What is wrong:** §5.3 asserts the ~1% floor is "more than an order of magnitude below the amplitudes the model's own observational motivation reports (Table 1)". Table 1's Ratio column, which the paper itself computes, runs 2.0–20.4. **Four of five rows are below 10×.** §6 Discussion states the correct figure on the same page: "its sensitivity floor (Eq. 1) is **2–20× tighter**". The abstract further quotes the range as "∼7–33%", silently dropping the 2–4% entries that Table 1 lists — and the dropped entries include Shamir 2022, the *only* comparison measured on the same survey (DESI Legacy) as this catalog, at ratio 2.0.

This is the paper's central quantitative rhetorical claim and it is stated at above its evidential strength in the abstract, §5.3, and the conclusions, while stated correctly in §6.

**Evidence:** `main.tex` l.95–98, l.355–361; rendered p. 4 (Table 1 ratio column + §6 l.293); `poplawski_dipole_exclusion_2026_09_02.json` ratio fields.

**Required:** use "2–20×" (or the ratio range against a stated definition) uniformly in abstract, §5.3, and conclusions, and quote the literature amplitude range as 2–33%, matching Table 1 and §6.

---

### MAJOR-3 — Figure 1 is not the sample its caption claims; the figure's own title contradicts the caption
**Location:** Figure 1, p. 2.

**What is wrong:** The caption reads "Per-pixel HEALPix CW-fraction map of the **887,472-galaxy supported-pixel high-confidence real-space sample used for the primary dipole fit (Sec. 3)**." The rendered figure's baked-in title reads "**Galaxy Chirality Asymmetry Map (8.47M galaxies, equivariant)**" (verified at 150 DPI, p. 2). The file is byte-identical to P4's full-catalog figure:

```
md5 pipelines/p4prime_chirality_test/paper/fig_sky_map.png = 7156f1af3c2ea3e6a0b7e47c6899802d
md5 pipelines/p2_chirality/fig_sky_map.png                 = 7156f1af3c2ea3e6a0b7e47c6899802d
md5 pipelines/p2_chirality/figs/fig_sky_map.png            = 7156f1af3c2ea3e6a0b7e47c6899802d
```

P4's own caption for that file (`chirality_catalog_paper.tex` l.1233–1244) describes it as the "Equivariant (Catalog C) chirality asymmetry map of the 8.47 M-galaxy catalog … NSIDE = 64 … f_sky = 0.49005 in the **FULL-SPIRAL-CANONICAL** support". That is a different support (FSC, 24,087 pixels, all spirals) from the primary fit's HC-REALSPACE-INCLUSIVE support (23,633 pixels, quality-controlled HC rows only). The figure does not show the sample the primary dipole fit uses, and the visual assertion "No coherent large-scale structure is visually apparent" is therefore made about the wrong map. This is a stale-figure propagation failure of exactly the class the caption is supposed to guard against.

**Required:** regenerate the map from the 887,472-row HC supported-pixel sample (or retitle the figure and caption honestly as the full-catalog map, and state that the primary-fit support is a subset).

---

### MAJOR-4 — The only classifier-validation number given belongs to a model that did not produce the released labels
**Location:** §2, p. 2, l.103–106: "a from-scratch, manifest-retained retrain of the GZ1-core classifier component validates at Cohen's κ = 0.97 on a provably training-disjoint held-out GZ1 sample."

**What is wrong:** This is the *only* classifier-quality number in the manuscript, and it does not characterise the catalog being released. P4 states explicitly (`chirality_catalog_paper.tex`, §Training Labels): the retrain "does *not* alter the released Catalog C labels, which remain the historical production outputs: the retrain demonstrates regenerability of the GZ1 core, it does not replace what was released." For the **released** classifier, P4 reports "The full GZ1 overlap gives **69.91% chirality agreement (κ = 0.40)**".

P4 additionally discloses three material facts that P4′ omits entirely:
1. The historical training realization is not reproducible — committed records conflict (26,616 vs 26,626 rows; 826 vs 846 CE non-spirals; 93.6878% vs 92.10% validation accuracy), with no retained object/split manifest or random-state record.
2. Roughly 67.5–72% of the training labels are CE-ResNet-derived, so "the catalogs are not fully independent and model-output permutation nulls cannot test inherited survey-correlated structure by themselves."
3. A composition-faithful, seeded CE-included retrain **collapses to chance on chirality** (best three-class validation 0.5617; binary CW/CCW agreement 0.517 on clean held-out GZ1 spirals) — P4 calls this "a genuine honest negative" and concludes the historical CE-included accuracy "is not reproducible under honest ingestion."

A referee reading only P4′ would conclude the released catalog labels are validated at κ = 0.97. They are not. Quoting the favourable κ from the regenerable component while omitting the released classifier's κ = 0.40 is selective reporting on the single most load-bearing quality metric in a catalog paper.

**Required:** report the released classifier's GZ1 confusion matrix and κ = 0.40 / 69.91% agreement in §2, and carry over P4's training-provenance disclosure and the CE-included honest negative, at least in condensed form.

---

### MAJOR-5 — Not self-contained as an ApJS catalog paper: no completeness, no purity, no schema, no selection function
**Location:** §2 (whole section, p. 2, 30 lines) and Data Availability, p. 5.

**What is missing:** §2 explicitly defers ("Full architecture, training-data provenance, bias-hardening audit … and per-region calibration are described in the archived release paper (15) and are not reproduced here; this section gives only what the black-hole-universe test in Sec. 5 needs"). For a *catalog* paper at ApJS, the deferred items are the paper. Specifically absent and not derivable from anything in P4′:

- **Completeness and purity.** P4 records ~70% integrated chirality purity and ~30% completeness at N_HC = 949,584 (and halving to ~15% at p_eq > 0.9). P4′ gives neither number nor a definition.
- **Catalog schema.** No column list, no data types, no flag definitions beyond a one-clause gloss of `raw_flip_qc_unsafe`, no row count per class. The paper releases a catalog and never shows its structure.
- **Selection function.** The parent sample's inherited GZ-DESI cuts (photometric types REX/DEV/EXP/SER, r ≤ 19.0, half-light radius ≥ 3″) and the three DR8 imaging campaigns (BASS+MzLS δ > +32°, DECaLS δ < +32°, DES overlap) appear nowhere.
- **Estimator specification.** The primary fit's HEALPix NSIDE, the numerical definition of "sufficient coverage" (P4: N_spiral(p) ≥ 10; 23,633 pixels), and f_sky (P4: 0.49005) are never stated. "sufficient coverage" (l.98–99) is left undefined.
- **Systematics.** No table of the rotation/flip/leg/depth covariate audit; no magnitude, size, redshift, or per-leg distributions; no sky-density figure.
- **The injection–recovery curve behind Eq. 1** is described in two sentences and never plotted, so a referee cannot judge how sharply detection probability crosses 95%, nor how the curve behaves near 0.98%.
- **For §4:** the P5 clustering-robustness ladder (NSIDE 2/4/8 and 3,750 nearest-MAXIMALS 3-D clusters, all intervals containing zero — P5 l.2020) is the evidence that Eq. 2's SE is not an artefact of one clustering choice; none of it is carried over.

---

### MAJOR-6 — A nominally significant discrepant diagnostic and an unresolved systematic are dropped without mention
**Location:** §3, p. 2, l.139–142 ("Full harmonic, weighted-least-squares, and GZ1 human-vote diagnostics are retained as systematics cross-checks in the archived release and are not repeated here"); §2, l.100–103.

**What is wrong:**
1. P4 reports that on the FSC support the fixed-occupancy 500-draw null gives an ℓ = 1 moment **z = +6.923 (add-one rank p = 0.001996)**, with the binomial-monopole null giving z = +6.983 / +7.207. That is a nominally strong ℓ = 1 on a support differing from the primary one only by the QC cut, and it is the single most important robustness question a referee would ask of a dipole null. P4′ disposes of it in a subordinate clause as a "systematics cross-check".
2. P4′ §2 states the classifier-injection forward model "rules out classifier label confusion as the source of any residual handedness monopole (0.0% of the observed value)" but stops there. P4's own sentence continues: it "localizes its origin **upstream of the classifier, without resolving whether that origin is a true sky asymmetry or a DESI imaging systematic**." The truncation converts an unresolved systematic into an apparently closed one.

**Required:** state the FSC ℓ = 1 result and why it does not undermine the primary null (support/estimator/null differences), and restore the unresolved-origin clause on the monopole.

---

### MAJOR-7 — The two principal citations are unpublished internal file paths; a repo path is cited in body text
**Location:** References [15], [16], p. 6; §1, p. 2, l.63–64.

**What is wrong:**
- **[15]** = "H. Golden, *An Observed-Label Chirality-Dipole Null…*, v4P.0.1 archived release, `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.274, 2026)". **[16]** = "…`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.147, 2026)". These are working-tree LaTeX source paths in a private repository — no journal, no arXiv id, no DOI, no URL. Every substantive deferral in the manuscript (MAJOR-5, MAJOR-6) points at them. As submitted, a referee cannot obtain them, so the deferrals are unresolvable and the paper cannot be evaluated at all on catalog construction, validation, completeness, purity, or systematics.
  - Note also that [15]'s version stamp is given as "v4P.0.1" (this manuscript's own version) while the file path says v1.0.274 — internally inconsistent.
- **§1 body text** cites "(see `project-context/PORTFOLIO_DECISION_2026-09-02.md`, Track C1 Addendum)" — an internal project-governance document, in a journal manuscript, as justification for the paper's framing ("which is why the present catalog is an on-vision test … rather than a detached data product"). This must be removed; a paper's scientific motivation cannot rest on the authors' internal portfolio decisions.
- **[14]** DESIVAST: "DESI Collaboration, 'DESIVAST: A Cosmic Void Catalog from the DESI Data Release 1,' DESI Collaboration public release (2025)" — no author list, no arXiv id, no DOI, no URL. The void catalog is the entire basis of §4.

---

### MAJOR-8 — Eq. 1 is a detection-power threshold, used throughout as if it were a confidence upper limit
**Location:** Eq. 1 and surrounding text, p. 2 (l.120–131); §5.2–5.3, p. 3–4; Abstract l.13–15.

**What is wrong:** Eq. 1 is defined operationally as the amplitude at which "Recovered detection probability crosses 95% coverage" in an injection–recovery experiment. That is a *power* threshold. The paper calls it a "95% sensitivity upper limit" (abstract) and then uses it as an exclusion: "the catalog's coverage-calibrated 95% sensitivity upper limit **excludes** η > A_95^obs ≃ 0.98% at ≥ 95% coverage" (§5.2), and §5.3's headline verb is "excludes". A power-based argument ("an amplitude of 0.98% would have been detected with 95% probability, and was not") is legitimate, but it is not the same object as a 95% CL upper limit on the measured amplitude, and the two are used interchangeably.

Compounding this: **no confidence interval or upper limit is ever quoted for the measured A_dip = 0.467%**, despite a committed 10⁴-draw null being in hand from which one is directly constructible. The paper's only quantitative bound is therefore the power threshold.

**Required:** quote a proper 95% CL upper limit on A_dip from the committed null distribution alongside Eq. 1, and state plainly wherever "excludes" is used that the statement is a power/coverage statement, not a likelihood-based limit.

---

### MAJOR-9 — Table 1 compares non-commensurable statistics, and the paper's own script contradicts the comparison under its own bridge factor
**Location:** Table 1 and §5.2, p. 4; numbered assumption 2, p. 4.

**What is wrong:**
1. The single "Amplitude" column pools four different statistics: Longo's dipole amplitude; Shamir 2012's *per-bin* asymmetry (5–20%, which P4 itself flags as "per-bin … as reported"); Shamir 2020/2022's global asymmetry fraction; and Shamir 2025's CW:CCW *count-ratio* imbalance. They were produced by different pipelines (Ganalyzer, visual/algorithmic) on different label definitions. They are then all compared to a single observed-label floor produced by *this* paper's ViT-Small + TTA classifier. Assumption 2 addresses the observed→physical bridge but never addresses cross-pipeline label incommensurability, which is the more immediate problem: A_95^obs is a floor on *this classifier's* labels, and the literature amplitudes are not measured in that label space.
2. The committed script's own output records, for the two 2–4% entries:
   ```
   shamir2020      exceeds_A95_obs_face_value=True   exceeds_A95_obs_after_g_bridge=False
   shamir2022desi  exceeds_A95_obs_face_value=True   exceeds_A95_obs_after_g_bridge=False
   ```
   (0.02 × 0.398 = 0.00796 < 0.0098.) Under the paper's own illustrative bridge factor, the two largest-N literature claims — including the same-survey Shamir 2022 — do **not** exceed the floor. Assumption 2 says g = 0.398 "is not used to strengthen this statement", which is fair, but the fact that applying it *weakens* the statement to the point of eliminating two rows is a material result of the committed script that the manuscript does not report.

---

## MINOR findings

- **MINOR-10.** Numbered assumption 4 (p. 4) refers to "The √N-scaling comparison in Table 1". Table 1 has no N-scaling column. The script computes `illustrative_sensitivity_floor_at_this_N` (e.g. 0.0750 at N = 15,158) but it is not tabulated. Either add the column or drop the assumption.
- **MINOR-11.** Numbered assumption 3 states the analysis "tests amplitude only … not a search matched to a specific predicted axis." `healpy.fit_dipole` fits amplitude *and* direction, so a free-axis fit is precisely the correct match to a model whose axis is a free direction. As written the caveat is inverted and understates the test's applicability.
- **MINOR-12.** Shamir 2025's "20–33%" conflates two encodings of the same 263-galaxy measurement (asymmetry fraction ≈ 20% vs. a 2:1 count ratio rendered as 33%); the committed script's note says "~2:1 to 1.5:1 CW:CCW imbalance". The 33% end drives the abstract's headline range. Fix the definition or give both encodings explicitly.
- **MINOR-13.** §1 gives Longo 2011 as "a > 5σ dipole signal"; the committed script's own note says "~5 sigma". Reconcile against Longo 2011 and use one value.
- **MINOR-14.** Abstract quotes "∼7–33%", §6 quotes "2–33%", Table 1 spans 2–33%. Unify.
- **MINOR-15.** No software/version statement (healpy, numpy, HEALPix NSIDE, scikit-learn/torch for the classifier). ApJS expects a Software section; none is present. No acknowledgements, no ORCID, no funding statement.
- **MINOR-16.** Figure 2's legend cites "Paper IV global f̄_CW = 0.4974". "Paper IV" is undefined anywhere in this manuscript. Rename to a resolvable reference.
- **MINOR-17.** Citation style is bracketed-numeric ([1], and "(1)" in text). AASTeX/ApJS uses author-year (`\bibliographystyle{aasjournal}`). Also, reference labels sit slightly into the left margin on p. 6 (cosmetic).
- **MINOR-18.** §4 is declared "exploratory and post-hoc (the void/non-void hierarchy was fixed after inspecting the data)" — an honest and welcome disclosure — but the manuscript reports three tests (§3 dipole, §4 void/non-void, §4 T-Web four-class) with no multiplicity statement anywhere. Add one sentence.
- **MINOR-19.** Fig. 2 shows Filament (0.4980) and Cluster (0.4958) sitting visibly below parity with small error bars; the text asserts only "no significant CW-fraction trend". The offset from f_CW = 0.5 is the residual monopole of MAJOR-6 and deserves one sentence connecting the two, rather than being left visible-but-unmentioned.
- **MINOR-20.** Please confirm the Zenodo DOIs resolve publicly (10.5281/zenodo.21461899, concept 10.5281/zenodo.21461898) and that the HuggingFace mirror `bamfai/galaxy-chirality-catalog` is public; I could not verify these from the manuscript alone. Also state the catalog file format and size.

**Presentation positives (recorded):** `main.log` shows 0 overfull/underfull boxes and 0 undefined references. Both figures are legible at print size; Table 1 is clean; the long script paths and URLs break correctly and do not overflow the column. Eq. 2's CI matches P5's committed value to the digit.

---

## Is 6 pages adequate?

**No.** As a *test of the Popławski prediction*, six pages is the right length and §§1, 5–7 are well constructed. As an **ApJS catalog paper** — which is what the title, the keywords, the Data Availability section, and the framing "We release an 8,474,531-object … catalog" all claim — six pages is not adequate, because the material a referee needs to evaluate the catalog is precisely the material that has been removed.

The following must come back from P4/P5 (my estimate: this takes the paper to ~12–18 pages):

**From P4 (`pipelines/p2_chirality/chirality_catalog_paper.tex`):**
1. **Catalog schema and release contract** — column list, dtypes, flag semantics, per-class row counts, file format/size, quarantine definition.
2. **Selection function** — the inherited GZ-DESI cuts (REX/DEV/EXP/SER, r ≤ 19.0, r₅₀ ≥ 3″), the three DR8 imaging campaigns and their sky partition, f_sky = 0.49005.
3. **Completeness and purity**, with definitions: ~30% completeness at N_HC = 949,584, ~70% integrated chirality purity, and the ~15% figure at p_eq > 0.9.
4. **The released classifier's validation**: the GZ1 confusion matrix, 69.91% agreement / κ = 0.40, plus the north/south × confidence stratified confusion table (N = 40,987 of 46,017 matches) and the 5,030 GZ1-confident spirals assigned to NOT_SPIRAL as an unquantified completeness channel.
5. **Training provenance disclosure**: the irreproducible historical realization, the 26,616-vs-26,626 conflict, the ~67.5–72% CE-ResNet dependence, and the CE-included honest negative (0.5617 / 0.517).
6. **Estimator specification**: NSIDE = 64, the N_spiral(p) ≥ 10 coverage cut, the 23,633-pixel HC-REALSPACE-INCLUSIVE support vs the 24,087-pixel FULL-SPIRAL-CANONICAL support, and the null construction.
7. **The residual-monopole diagnosis** including its unresolved origin, and **the FSC MASTER ℓ = 1 result (z = +6.923, p = 0.002)** with the reason it does not overturn the primary null.
8. **The injection–recovery curve** behind Eq. 1, as a figure, with the axis-sampling scheme (2,000 axes per amplitude) and the amplitude grid.
9. **A corrected Figure 1** built from the 887,472-row primary sample.

**From P5 (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`):**
10. The **clustering-robustness ladder** for Eq. 2 (NSIDE 2/4/8 and 3,750 nearest-MAXIMALS 3-D clusters; point estimate +0.00145442 throughout, all intervals containing zero) and the 13-column nuisance-basis specification.

**The alternative** — keeping the paper at six pages as a focused Letter on the Popławski test — is viable *only* if [15] and [16] become citable published or DOI-archived objects. As long as they are private-repository `.tex` paths, no deferral in this manuscript is resolvable and the paper fails self-containedness at any length.

---

## Framing-honesty assessment (dimension 3)

This is the strongest part of the manuscript and I want to record it explicitly, because the MAJOR findings above should not be read as an indictment of the paper's honesty:

- §5.1's core move — reading Popławski's papers, finding **no** computed amplitude, and saying so ("the claim is qualitative … not quantitative") — is exactly right and is the paper's real contribution.
- Eq. 3 is labelled, in the paper's own italics, as "*not* derived from Popławski's papers", with the reason given.
- The five numbered assumptions are genuinely limiting and are stated as such; assumption 2 in particular refuses to use g = 0.398 to strengthen the result.
- §5.2's closing paragraph and §6's "genuine, if qualified, exclusion — qualified because Popławski's papers do not themselves commit to a quantitative amplitude" are the correct evidential register.
- The disclaimer that the catalog "does not test, and is not evidence for or against, the matter-bounce cosmology this research program otherwise develops" appears in the abstract, §1, §5.2, §7, and the Discussion — no bounce claim is smuggled in anywhere. I checked for this specifically and found none.

The honesty failures are localized and fixable: MAJOR-2 (the "order of magnitude" overstatement contradicting the paper's own table), MAJOR-1 (the sample-size range), MAJOR-4 (the favourable κ quoted where the released-classifier κ belongs), and MAJOR-6 (a truncated caveat and a dropped discrepant diagnostic). Three of these four are *selective presentation of material the authors themselves computed correctly elsewhere*, which is why I regard them as revisable rather than disqualifying.

---

## VERDICT: **major-revisions**

**Justification.** The measurements underlying this manuscript are sound: I verified every headline number against its committed source and found no arithmetic or transcription error in the catalog size, the QC ladder, the dipole statistics, A_95^obs, the void/non-void contrast, or the Table 1 ratio column — the P5 confidence interval matches to six decimal places. The theoretical section is the paper's genuine contribution and is executed with unusual candour: it establishes by direct reading that Popławski's model supplies no quantitative amplitude, adopts a minimal closure that is explicitly flagged as the authors' own, and enumerates five real limitations. I do not recommend rejection. But the paper cannot be accepted in this form for two independent reasons. First, four framing defects overstate the result against evidence the manuscript itself contains: the "6 to 3,400× smaller" range is false for the largest and most directly comparable literature sample (Shamir 2022, DESI Legacy, N = 1.3M, which is *larger* than the primary channel); "more than an order of magnitude" contradicts the paper's own Table 1 (ratios 2.0–20.4) and its own Discussion ("2–20×"); the sole classifier-validation figure (κ = 0.97) belongs to a retrained model that P4 states did not produce the released labels, whose actual GZ1 agreement is κ = 0.40; and Figure 1 is a byte-identical copy of the full-catalog map on a different support, captioned as the primary-fit sample while its own embedded title says "8.47M galaxies". Second, as an ApJS catalog paper it is not self-contained: completeness, purity, schema, selection function, estimator NSIDE and coverage cut, systematics, the injection–recovery curve, and the unresolved residual-monopole origin are all deferred to references [15] and [16], which are private-repository `.tex` file paths with no journal, arXiv id, or DOI — making every deferral unresolvable for a referee or reader. Fixing the framing costs a day; fixing self-containedness requires either restoring roughly 6–12 pages of catalog material or publishing P4/P5 first so the deferrals become legitimate citations. Both are squarely within the authors' reach, which is why this is major revisions rather than reject.

**Counts: 9 MAJOR, 11 MINOR.**
