# P3 auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14903 chars)
**Wall time**: 483.4s

---

# Referee Report — P3 (Physical Review D)

**Author note to editor:** This paper combines a large-scale engineering exercise (anomaly catalog) with two cosmology forecasts, both of which the paper itself shows are consistent with null at <1σ. The presentation systematically inflates the significance of each result while the body text contains the disclaimers. The paper is also ~2× too long for the residual scientific content, and contains pervasive internal-review jargon ("Path-C", "gate FAIL-with-diagnostic", "before/after diagnostic") that should not appear in a PRD article. Below I list issues found by reading the full PDF and recomputing every load-bearing number.

---

## ESSENTIAL findings (blocking acceptance)

### P3-E1 — Abstract headline contradicts body: "largest catalog" vs recommended subset (Abstract, p. 1)
The abstract leads with "**378,280** unique anomalies" as the headline scale claim and asserts this is "∼141× the size of the largest prior single-survey anomaly catalog." But two sentences later the same abstract says "the recommended catalog-grade subset is ∼265,000 unique objects … which excludes the LAMOST exploratory tier (∼113,000 objects retained as a methodological lesson: 98% blue-excess training-bias artifact, injection-recovery gate FAIL)." If the LAMOST 113,342 are a known training-bias artifact with gate FAIL (5.8% recovery at 5σ), they cannot also be counted in the headline catalog size. Recompute: 265,000/2,685 ≈ 99×, not 141×. The "141×" claim is built on objects the authors themselves recommend not be used. **Fix:** restate headline as ~265k and the corresponding multiplier; demote 378,280 to a supplementary number, or remove the LAMOST tier from the catalog entirely.

### P3-E2 — fNL Fisher "1σ envelope [3.92, 8.98]" is mathematically inflated (Abstract, §V, p. 11)
Given the Fisher-positivity form 1/σ² = F0 + cα² with F0 = 1/8.98² and c = 0.0747, the function σ(α) is symmetric around α=0 and monotonically decreasing in |α|. The quoted 1σ interval α ∈ [−0.46, +0.84] (from αjk = 0.19 ± 0.65) maps to σ values:
- α = −0.46: σ = 5.95
- α = 0: σ = 8.98 (only at α=0 exactly)
- α = +0.19: σ = 8.14
- α = +0.84: σ = 3.92

The "1σ envelope [3.92, 8.98]" pads the upper limit up to the α=0 baseline, but α=0 is not the 1σ upper bound of the α interval [−0.46, +0.84]. The honest envelope mapping from the 1σ α-range is [3.92, 5.95], because c·α² > 0 over the entire interval. The 8.98 figure only arises if α is allowed to assume a value (zero) that the data prefers less than the endpoints. **Fix:** correct envelope or, if 8.98 is the local maximum, state that explicitly and note that α=0 (no improvement) sits well inside the 1σ region; remove the "7.9% improvement" framing since the central α=0.19 is itself <0.3σ from zero.

### P3-E3 — NANOGrav posterior γ = 2.567 ± 0.382 is inconsistent with the published NANOGrav 15-yr power-law result (§V A, App. E, p. 12, 15)
The NANOGrav Collaboration's own 15-yr analysis [their ref. 18] of the HD-correlated free-spectrum recovers a power-law γ ≈ 3.2 ± 0.6 (HD-only) with the same parameterization used in Eq. (E1). The author's chain reports γ = 2.567 ± 0.382 — a >1σ shift from the collaboration's own published value, with a smaller uncertainty than the published analysis. There is no discussion of why this analysis recovers a different posterior than the producer of the dataset. The entire SMBHB-vs-matter-bounce Bayes factor argument depends on this posterior. **Fix:** reproduce a NANOGrav fiducial fit alongside; explain the difference; until reconciled, the +1.13σ MB claim and the 7.1×10³ Bayes factor cannot stand.

### P3-E4 — SMBHB γ = 4.33 reference value is the wrong literature baseline (§V A, p. 12)
The "+4.61σ disfavoring SMBHB" sigma is constructed against γ = 4.33 (purely circular-binary GW-driven inspiral). This is not what the SMBHB community uses to confront PTA data: realistic SMBHB population models including stellar/gas hardening produce expected γ ∼ 3.0–3.8, and NANOGrav 15-yr "new physics" companion paper [their ref. 28] reports SMBHB γ posteriors fully overlapping with γ ≈ 3.2. Quoting "+4.61σ" against γ = 4.33 produces a misleading Savage–Dickey ratio of 7100 in favor of matter-bounce. **Fix:** either remove this comparison or compute against the realistic SMBHB γ-distribution; the headline "BMB/SMBHB = 7.1×10³" must come out of the abstract.

### P3-E5 — Three of six injection-recovery gates FAIL at 5σ — affected catalogs are not calibrated (§II D, §III, Fig. 7)
LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2% recovery at 5σ. The euphemism "FAIL-with-diagnostic" is used 11 times. A 1.2% recovery rate at 5σ means the eROSITA anomaly tier has essentially undefined completeness — any "novel X-ray source" claim derived from this tier (e.g., 203 novel X-ray sources, headline §V) is not supportable. The IsolationForest cross-validation stability (81.5%) is a different metric (consistency between detectors, not sensitivity to known signals) and is wrongly used as a substitute. **Fix:** state plainly that completeness of these three catalogs is unquantified at 5σ; remove "203 novel X-ray sources" from the conclusions section; remove Gaia and LAMOST from any cross-survey overlap/fNL forecast input until passing gates.

### P3-E6 — Planck CMB autoencoder gate (a) FAILS by 50%+; gate (b) test is circular (§III F, p. 6)
The native CMB convolutional autoencoder reports val_loss = 0.4437 against a criterion ≤ 0.30. It is "rescued" by criterion (b): 100% injection recovery on **Gaussian-bump plants at 5σ**. Searching a CMB map for Gaussian bumps using an autoencoder trained on Gaussian-statistics noise will trivially recover bumps far above the noise floor; this is not an independent test of catalog completeness or specificity. The "200 Planck CMB patches" in the catalog headline rest entirely on a checkpoint that fails the val-loss gate by 48% and was validated only on a target morphology matching the model's null distribution. **Fix:** demote Planck patches to "exploratory" status; redo gate (b) with non-Gaussian plants (point-source contamination, foreground residuals, CIB bumps); or simply remove the 200 patches from the headline 378,280.

### P3-E7 — "Genuine novelty fraction ∼17.8%" is one number with no uncertainty quoted but is the headline discovery rate (Abstract, §IV A, §VII, p. 1, 9, 14)
The abstract and conclusions both quote 17.8% as the headline novelty rate. The body admits: "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested." A single 178/1,000 with no upper/lower bounds, applied only at the extreme top-score stratum, is not a defensible catalog-wide discovery rate. The Wilson 95% interval on 178/1000 is [15.5%, 20.3%] at the top-1k stratum alone, and the rate at lower scores is unknown. The paper does not bracket this and uses 17.8% as the discovery-rate sound bite. **Fix:** state the uncertainty; do the test at additional score strata (top-100, top-10k, top-100k) before headlining a single fraction.

### P3-E8 — "DESI 5-fold Jaccard J̄ = 0.862 (PASS)" is in-sample stability, presented as if it validates OOD ranking (§II B, §VI D (i), p. 2, 12)
The 5-fold CV is on the 47,000-spectrum training pool. Stability of in-sample rank under different 80% training subsets does not constitute out-of-distribution validation, but Table I and the abstract use "PASS" as if it does. The independent 100k SPARCL OOD test reportedly flags >50% of spectra at S>5, which the paper waves away as a "catalog-curation effect" — i.e., the score scale completely breaks on a random sample. This is an unresolved completeness issue affecting the DESI 195,829-anomaly count. **Fix:** the in-sample CV and the OOD test are measuring different things; do not call them both "PASS"; quantify the actual OOD false-positive rate.

### P3-E9 — Internal-review jargon and post-hoc framing throughout body (§II D, §III, §VI D, Tables I, IV, Fig. 7, App. F)
The body is saturated with internal version-control language that should not appear in a PRD article: "Path-C rebuild protocol", "Path-C native retrain", "before/after diagnostic", "FAIL-with-diagnostic", "Path-C residual caveats", "Path-C-final catalog", "8-way-with-ACT variant is preserved as a sensitivity-check artifact", "criterion (a) FAIL but criterion (b) PASS", "first-pass cross-transfer scan exposed two failure modes", "quarantined as a cross-transfer artifact", "is preserved as the §II D before/after baseline." This phrasing is reviewer-loop bookkeeping, not science narrative; it tells the reader the paper went through multiple iterations after the first scan failed. Table IV ("Path-C residual caveats") is essentially a review-response log placed in the body. **Fix:** remove all "Path-C", "gate FAIL-with-diagnostic", "before/after", "criterion (a)/(b)" language; write the methodology as if natively designed; relegate the cross-transfer failure mode to a single appendix paragraph or omit.

### P3-E10 — ACT DR6 appears in the per-survey block, Fig. 1, and Table V despite being "quarantined" (Table I caption, Fig. 1, Table V, App. F)
The paper says "ACT DR6 quarantined" in the abstract, then Fig. 1 (title: "Spatial distribution of all 319,443 anomalies across 8 archives") shows ACT DR6 as one of eight colored species; Table V ("Survey Processing Details") lists ACT DR6 with timing/throughput; Table I caption disclaims ACT inclusion but the row counting that sums to 319,443 (which Fig. 1 plots) does include the 200 ACT patches. The status is internally inconsistent. **Fix:** if quarantined, remove from Fig. 1 entirely; remove from Table V or move to App. F; remove the 319,443 number that includes ACT from the body.

### P3-E11 — Paper length disproportionate to content (Whole paper)
20 pages for a methods+catalog paper whose cosmology contributions are (i) a fNL forecast consistent with null at <1σ and (ii) a NANOGrav fit inconsistent with the collaboration's own value. The novel methodological content (autoencoder cross-transfer fails; train natively) is two paragraphs. PRD section II (Methods) is well-formed, but §V, §VI, §VII, Apps. C–F duplicate each other; the bouncing-cosmology + NANOGrav material would be a separate Note. **Recommended max for PRD: 10 pages** for the methods + catalog summary; the fNL forecast and NANOGrav fit should be split into a separate, shorter companion or removed.

---

## MAJOR findings

### P3-M1 — Cross-transfer baseline preserved as central artifact inflates the methodology section (§II D, Table I, §VI)
Table I row "Total (cross-transfer, ACT-incl.)" reports 319,443 from a methodology the authors say is wrong. This is preserved as "before/after diagnostic" but it dominates the table and Figure 1. A clean paper documents only the final method.

### P3-M2 — Abstract sentence: "ACT DR6 quarantined as a cross-transfer artifact" — definition not given
The abstract uses this phrase before any reader can know what cross-transfer is or which step quarantined ACT. The reader sees this twice in the abstract.

### P3-M3 — SDSS native-retrain S>5 yields 12 sources but the headline 77,905 uses top-percentile (§III C, Table I footnotes ♡)
Table I footnote ♡ admits "applying S>5 to SDSS yields only 12 sources" — the abstract and headline use the top-1% slice (S≥0.1060). The reader is told the threshold is "absolute canonical-S cut at S>5.0" (Methods) and elsewhere "per-survey top-percentile." The paper switches threshold definitions between sentences to retain large headline counts. State one threshold per survey, prominently, and accept the small SDSS native count.

### P3-M4 — LAMOST "exploratory tier" retained in the catalog at all (§III D, §VI A)
A catalog where the authors themselves say "98% of cross-transfer anomalies are blue-excess — a training-bias artifact" and which fails the injection gate at 5σ should not be released as part of the headline catalog. The "methodological lesson" is fine; including 113,342 objects in the public catalog labeled as anomalies is not. Either remove or label every entry as "training-bias artifact / not science-grade."

### P3-M5 — Fisher F0 and c values appear ex nihilo (§V, p. 11)
"F0 = 1/8.98² and c = 0.0747 (§VI D caveat (i))" — §VI D (i) does not derive c. The reader has no way to verify the Fisher coefficient that drives the headline σ(fNL) value. Derive c in an appendix.

### P3-M6 — Bayes factor "Savage–Dickey BMB/free = 3.23 and BSMBHB/free = 4.52×10⁻⁴" — prior dependence not discussed (§V A, p. 12)
A Savage–Dickey ratio for a continuous parameter depends entirely on the prior density at the test point. For γ ∈ [0,7] uniform, prior density 1/7, the ratio for both γ=3 and γ=4.33 carries the same factor; for any other prior this changes. The "decisive on Jeffreys' scale" claim is therefore conditional on a prior the authors chose without justification. State the prior sensitivity.

### P3-M7 — Spatial uniformity χ² = 143,936, dof = 38,329 reported then dismissed (§IV B)
The same sentence reports a "significant" χ²ν = 3.76 and then says it is "dominated by the inhomogeneous footprints" and not interpretable. Why report it then? This is wasted text in a 20-page paper.

### P3-M8 — Comparison with prior work is one paragraph (§VI E)
A claim to be "the largest multi-archive anomaly search" requires a comparative table against (e.g.) Baron & Poznanski (2017), Boone+ (2019), Reis+ (2018, 2019), AstroSpec efforts, Astronomaly 2021–2024 work, Galaxy Zoo anomaly literature. The single paragraph is insufficient for a PRD claim of "largest."

### P3-M9 — TIC 374313355 is described as one of three highlighted cross-matches but Match 1 is "Known QSO at z≈1.55" with no SIMBAD/Milliquas ID (§IV C, Fig. 6 caption)
If it is "known," cite it. The reader is told that this is a cross-survey validation match but not given the catalog identifier of the "known" object.

### P3-M10 — Fig. 6 panels (c, d) for TIC 374313355: SDSS reconstruction (red) is essentially flat while the data (black) is highly elevated (Fig. 6, p. 11)
A model that completely fails to reconstruct one epoch and computes "score 49.5" by reconstruction error is not detecting variability — it is computing a normalization mismatch. The interpretation as a "stellar flare or accretion event" is unsupported by anything in the spectral panels shown.

### P3-M11 — Genuine novelty fraction baseline: 20 catalogs are listed; only 17 are named (§IV A, p. 9)
"20 curated all-sky catalogs via CDS X-Match (Gaia DR3, SDSS DR12/DR16, DESI Legacy Imaging DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS)" — I count 17 distinct catalog names (with DR12/DR16 of SDSS). List all 20 explicitly.

### P3-M12 — "Aggregate 58.8% SIMBAD-unmatched" but this number is not in the abstract (Fig. 5, §IV A)
The body uses 58.8% as an aggregate; the abstract uses 17.8% for novelty. Both numbers are presented prominently but neither is reproducible from the per-survey table because no survey weight scheme is described.

### P3-M13 — Quoted Spearman ρ=−0.03, p=0.12 for score vs SNR (§III A)
ρ=−0.03 with N≈2670 should give p ≈ 0.1 (consistent), but on N=2670 a |ρ|=0.03 actually gives p ≈ 0.12 only if the test is two-sided and ρ is exact. Recomputing: t = 0.03√(2668/(1−0.0009)) = 1.55, two-sided p ≈ 0.12. OK that recomputes. But "no practically significant" with p=0.12 is fine; the issue is that a stratified subsample is being used and the stratification is not described. Describe.

### P3-M14 — Cross-transfer SDSS dynamic range S up to 1.9×10¹¹ (Fig. 2 right caption, p. 5)
A score of 10¹¹ from an autoencoder is essentially uninterpretable and is an artifact of OOD generalization failure. The fact that this figure is shown at all in the paper, when the same data has been "Path-C native-retrained" and is much better behaved, signals the cross-transfer pipeline should be moved to an appendix.

### P3-M15 — Page 7 Table I footnotes total ~30 lines and are essential to reading the table
Footnotes ¶, †, ‡, ‖, §, ♡, ♠, ⋆ are all load-bearing. The table is unreadable without footnotes longer than the table. This is a structural problem.

### P3-M16 — Page 7 Table I: 6 of 7 surveys list cross-transfer counts in main column; the actual catalog totals (Path-C) live only in a footnote and one separate row
A reader takes "Nanom" at face value. Replace the main column with Path-C native counts and put cross-transfer in the appendix.

### P3-M17 — "ACT zero-overlap" argument used to justify exact stratification subtraction of 200 (Table I caption, p. 7)
"ACT's 200 patches contributed zero positional overlaps with the other seven surveys (the Planck×ACT null cross-correlation, §IV D, confirms this), so excluding ACT subtracts exactly 200." The Planck×ACT null is among CMB-patch sky regions; ACT vs point sources is a different geometric question (16′ ACT patches vs 5″ matching radius — of course no overlaps in that sense). The argument as stated conflates two different null statements.

### P3-M18 — App. C: 7-bin Fisher result "α=0.15, σ=8.43, 6.1%" linearly scaled to other α values (Table VII)
Linear scaling of a Fisher result that should be quadratic in α (per the form in §V) gives the wrong values. Table VII rows are inconsistent with the Fisher-positivity-respecting form used in §V. Either choose one form or reconcile.

### P3-M19 — Sentence in §III A repeated almost verbatim (p. 4)
"Galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%); anomalies peak at z ∼ 0.75 vs. z ∼ 0.93 for normal spectra." and the next paragraph: "galaxies are flagged as anomalous at ∼20 times the rate of QSOs (0.75% vs. 0.037%), with anomalies peaking at z ∼ 0.75 compared to z ∼ 0.93 for normal spectra." Duplicate text.

### P3-M20 — "BAL QSO at z ≈ 0.86" — Mg II is at 2800 Å rest, observed at 5208 Å at z=0.86 (§IV C, Fig. 6e/f)
The figure caption says "broad Mg II absorption" but does not show the redshifted feature location or mark the BAL trough. A BAL claim needs a clear identification of the absorption trough velocity and rest-frame line. The spectrum on the left of Fig. 6e shows broad absorption near 5000–5500 Å, plausibly Mg II at z=0.86. But the spectra are not labeled with rest-frame markers, and the claim "uncataloged" needs a NED/SIMBAD/Milliquas check at the actual coordinates, which are not given.

---

## MINOR findings

### P3-m1 — Date "June 2026" in title (p. 1)
This is a future date relative to the references used (most 2023–2024). Confirm submission date.

### P3-m2 — Email address in author footnote (p. 1)
houston@hubify.com — appropriate for arXiv, acceptable for PRD.

### P3-m3 — Acronym "BAL QSO" used in Abstract without definition
Define on first use.

### P3-m4 — "z-scored" parenthetical in §II B is awkwardly long
The paragraph "note: 'z-scored' here is the statistics term…the anomaly score S is never called 'z' in this paper to avoid ambiguity" reads like a referee-response note. Trim.

### P3-m5 — Figure 1 title: "Spatial distribution of all 319,443 anomalies across 8 archives"
Inconsistent with the abstract's 378,280 and "seven retained archives". Either re-render with the canonical Path-C set or relabel.

### P3-m6 — Figure 1 axis labels: longitude shown both as −150° to 150° and on circular ticks
Mollweide convention is fine but specify whether ICRS or Galactic.

### P3-m7 — Figure 2 right panel: y-axis ticks unclear, label "Prob. density" abbreviated
Use "Probability density" as on left panel for consistency.

### P3-m8 — Figure 2 caption claims SDSS "native re-score (§III C) compresses the same objects to S<14" — Fig. 2 right panel shows only cross-transfer
The figure caption claims something not shown in the figure. Either add the native panel or revise the caption.

### P3-m9 — Figure 3: UMAP embedding shown for cross-transfer baseline only
Same issue. If the cross-transfer is the wrong methodology, why is the headline UMAP figure built on it?

### P3-m10 — Figure 4 caption: source described as "optical counterpart is a bright, saturated source with diffraction spikes" — image shows clear saturation
Worth flagging that "extreme W1–W2 color excess" of a saturated source is most plausibly a saturation/diffraction artifact in WISE, not a physical excess. The caption acknowledges interpretation is uncertain but should mention the saturation-artifact possibility explicitly.

### P3-m11 — Fig. 6 caption "Score = 8.1" (DESI epoch of TIC 374313355) vs "Score = 49.5" (SDSS epoch)
The score scale is per-survey and not comparable (per §II B's own admonition), but Fig. 6 panels visually invite the reader to compare scores 8.1 and 49.5.

### P3-m12 — Table III: SBigAE values 1.084, 0.815, 0.591, etc., versus DESI's "S>5" threshold
Per-survey threshold families are different; reader cannot compare. Caption clarifies but the comparison is jarring.

### P3-m13 — App. E: "ESS ≈ 5,500; τ ≈ 58 samples/walker" — N_total/τ = 320,000/58 ≈ 5,517, OK
Arithmetic checks out.

### P3-m14 — Reference [33] note: "publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity"
Bibliography metadata comment in the reference list is internal bookkeeping. Remove.

### P3-m15 — Reference [12]: "Mon. Not. Roy. Astron. Soc. (2026, in press)"
Future date. Confirm or remove.

### P3-m16 — Reference [1]: "DESI DR1 documentation" — not a complete bibliographic entry
DESI DR1 has formal collaboration papers; cite them.

### P3-m17 — Footnote citation style: "[18]" used both for NANOGrav abstract paper and for the Zenodo dataset
These are different objects; cite the dataset DOI separately.

### P3-m18 — Fig. 7 legend: "FAIL*" for three surveys is acceptable but caption sentence is too long (15 lines)
Trim caption.

### P3-m19 — App. F: "ACT DR6 cross-transfer scan: quarantined methodological artifact"
The appendix exists; remove from main text completely.

### P3-m20 — Acknowledgments do not include any human collaborators
Single-author paper; if this is genuine, fine. If anyone provided feedback they should be acknowledged.

### P3-m21 — §VII Conclusions item 6: "OOD control-vs-control 0.874 (PASS)"
This number does not appear earlier in the paper. Where is the 0.874 from?

### P3-m22 — §V c. "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹"
Self-evident at the wavenumbers in question; one sentence is enough, currently a paragraph.

---

## NIT

### P3-N1 — Multiple "∼" and "approximately" in the same sentence (Abstract)
Pick one notation.

### P3-N2 — "Path-C" appears 50+ times; even renaming as "the catalog protocol" once would be cleaner.

### P3-N3 — Conclusion bullet 1: "stratified: 378,080 point-source + 200 Planck CMB patches"
Word "stratified" misused; the catalog is a union, not a stratification.

### P3-N4 — Acronym "OOD" used 8 times; spell out "out-of-distribution" on first use.

### P3-N5 — Spelling: "Atacama Cosmology Telescope" capitalized correctly throughout.

### P3-N6 — Date format "(Dated: June 2026)" should match PRD style.

---

## Summary recommendation
**REJECT**

The paper combines a large catalog-engineering exercise with two cosmology forecasts and presents both as significant. On inspection, the cosmology results are consistent with null at <1σ (the fNL Fisher headline) or in tension with the producing collaboration's own published posterior (the NANOGrav fit). Three of six injection-recovery gates fail at 5σ; the Planck CMB gate is rescued by a trivially circular test; the LAMOST tier (98% blue-excess training bias) is included in the headline 378,280 yet recommended for exclusion in the same abstract; the "largest catalog" multiplier (141×) is computed against a number the authors themselves disclaim. The body is saturated with internal-review jargon ("Path-C", "FAIL-with-diagnostic", "before/after diagnostic", "criterion (a) vs (b)") that does not belong in a PRD article. Figures and tables are built on the cross-transfer methodology the paper rejects. The paper is approximately twice the length warranted by its residual content. A complete restructuring (drop LAMOST and cross-transfer from main text, derive Fisher coefficient honestly, reconcile or remove the NANOGrav fit, demote 17.8% to a stratum-conditioned point estimate, recompute "largest" multiplier against the recommended subset) is required before this can be considered for PRD. The current submission cannot be repaired by minor revisions.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P3, Second Pass (New Findings Only)

Re-reading with fresh eyes against the ten classes A–J above, I find a number of issues missed in the first pass. The fNL forecast machinery is internally inconsistent at the arithmetic level, the cosmology appendix uses a different single-tracer baseline than §V, a key conclusion contains a Jaccard number that appears nowhere else in the paper, and one of the three "cross-survey matches" highlighted in §IV C contains objects whose stated scores fall below the published anomaly threshold.

---

## NEW ESSENTIAL findings

### P3-E12 — Single-tracer σ(fNL) baseline conflict: 8.98 in §V vs 16.85 in App. C Fig. 8 (Class I, J)
The Fisher machinery in §V is anchored to **σ(fNL)std = 8.98** ("single-tracer DESI QSO baseline"). Table VII of Appendix C reproduces this: top row α=0.05 gives σ=8.80 against a baseline of 8.98, etc. But the same appendix's Figure 8 caption states: "dashed gray line marks the dense-tracer limit (σ(fNL) = 11.71); the dotted dark-red line marks the **single-tracer baseline (σ(fNL) = 16.85)**." The baseline multi-tracer is reported as 12.72 in the same figure caption. These are not perturbations of 8.98 — they are nearly twice as large. The figure also annotates the gold (¯n = 8.5×10⁻⁶) and silver (¯n = 4.5×10⁻⁵) sub-samples on this 16.85-baseline scale. There is no reconciliation in the text. Either §V is using a wrong baseline (in which case all fNL improvements quoted in the abstract are based on a fictitious reference), or App. C Fig. 8 is plotting a different forecast entirely. The reader cannot tell which. **Fix:** reconcile the two baselines explicitly with derivations; remove whichever is incorrect.

### P3-E13 — "7.9% improvement" arithmetic does not match the Fisher form's central σ(fNL)=8.14 (Abstract, §V, Conclusion 5)
From the displayed values:
- σ(fNL)std = 8.98
- σ(fNL) = 8.14 (central forecast at αjk = 0.19)
- True improvement = (8.98 − 8.14)/8.98 = **9.35%**, not 7.9%

7.9% is what one gets by **linear** scaling of the Appendix C α=0.15 result: (6.1%/0.15) × 0.19 = 7.73% ≈ 7.9%. But §V states explicitly that the Fisher form is the **quadratic** 1/σ² = F0 + cα². The two forms give different answers and cannot both be right. The abstract uses the linear-form number (7.9%), but the abstract's σ(fNL) = 8.14 is from the quadratic form. The two are stapled together inconsistently. Same problem in §V para. (b) and Conclusion 5. **Fix:** pick one form, recompute, and remove the linear scaling from App. C if the quadratic Fisher form is the headline.

### P3-E14 — Fig. 6 "Match 1" anomaly scores (3.2 and 2.8) are below the published anomaly threshold (§IV C, Fig. 6, p. 11)
Match 1 in Fig. 6 (a known QSO at z ≈ 1.55) shows **Score = 3.2 (DESI)** and **Score = 2.8 (SDSS)**. The DESI anomaly catalog threshold is **S > 5.0** (Table I, §III A). On the canonical-S axis, Score = 3.2 is **below threshold and would not be in the DESI anomaly catalog at all**. The paper claims this object is the first of "three highest-confidence cross-survey detections… from the DESI×SDSS pairwise channel" used to "validate the cross-survey approach." If it is not actually in the anomaly catalog at the published threshold, then it is not a cross-survey anomaly match — it is a coincident known QSO. The Fig. 6 caption does not specify which score axis it uses; if a different scale is used than the canonical S, that scale needs to be defined and reconciled with Table I. As written, the cross-survey validation section (§IV C) is built on a figure that contradicts the catalog's own selection criterion. **Fix:** state the score scale used in Fig. 6, recompute on the canonical scale, and either justify why a sub-threshold match counts as a "validation match" or replace with a genuine top-S cross-survey match.

### P3-E15 — Gold+Silver fNL envelope [0.94, 8.98] repeats the same logical error as the main result (§V, p. 11)
For the high-confidence Gold+Silver subset: αGS,jk = +1.83 ± 2.03, with the quoted "1σ envelope [0.94, 8.98]". Plugging in the Fisher form:
- α = −0.20 (lower 1σ bound): σ = 8.06
- α = 0 (stationary point, inside the 1σ interval): σ = 8.98
- α = +3.86 (upper 1σ bound): σ = 0.94

The 8.98 again is the value at α=0, which is inside the 1σ α-window, not at its edge. The honest 1σ envelope mapped from the α-uncertainty is [0.94, 8.06] (taking the maximum of σ at the endpoints |α|=0.20 vs |α|=3.86). The 8.98 figure here, as in P3-E2, requires the stationary-point identification of a 1σ upper bound. **Fix:** correct the envelope; this is not an isolated typo but a systematic mistake repeated in the main and high-confidence forecasts.

---

## NEW MAJOR findings

### P3-M21 — Conclusion 6 cites "OOD control-vs-control 0.874 (PASS)" — the number appears nowhere in the body (Conclusions, p. 14)
Conclusion 6 says "DESI 5-fold Jaccard stability J̄ = 0.862 (PASS); **OOD control-vs-control 0.874 (PASS)**." The body's only OOD-Jaccard number is **0.732** (§II B and §VI D (i): "production-vs-5-seed-control J̄prod×ctrl = 0.732 (≥ 0.50, PASS)"). I cannot find 0.874 anywhere in §II, §III, §VI, or Appendix E. Either the body or the conclusion is wrong, or 0.874 is a stale number from an earlier draft. **Fix:** reconcile; if 0.874 is the OOD result, derive and report it in §II B; if 0.732 is correct, fix the conclusion.

### P3-M22 — Fig. 2 caption claims LAMOST is "native" but the legend count (44,075) is the cross-transfer value (Fig. 2, p. 5)
Caption: "cross-transfer for SDSS, **native** for DESI/LAMOST." But the LAMOST histogram is labeled "LAMOST DR10 (44,075)" — 44,075 is explicitly the cross-transfer count (§III D); the LAMOST native S>5 count is 2,054. The Path-C native re-scoring is the "21.5× anomaly-rate reduction" lead finding of §III D. The figure shows the wrong distribution against the caption's claim. **Fix:** either re-render Fig. 2 with the native LAMOST distribution, or correct the caption to say "cross-transfer for SDSS and LAMOST."

### P3-M23 — Three inconsistent labeling schemes for §VI D residual caveats (§VI D, Table IV)
The body of §VI D enumerates caveats as **(i), (ii)**. Table IV labels them **(a)–(j)**. Inline references elsewhere cite **§VI D (f), (v), (e), (j)** etc. mixing alphabetic and roman-numeral indices. Table I footnote § says "see caveat (v)" but Table IV has no (v); the closest is row (b) or (e). The mapping between the three schemes is never given. **Fix:** unify to a single (a)–(j) scheme; verify every cross-reference.

### P3-M24 — Validation-MSE gate (a) "≤ 0.30" applied across different data normalizations (§II D Step 1)
The "Path-C two-part gate" criterion (a) uses an absolute val-loss threshold of 0.30 across spectra (DESI ~0.029, SDSS 0.031, LAMOST 0.033) and CMB maps (Planck 0.4437). On any reasonable normalization, MSE units depend on the input data's amplitude distribution, and 0.30 is somewhere between "trivially loose" (for spectra) and "structurally tight" (for 4096-pixel CMB patches). The Planck native autoencoder fails the gate by 48% on this criterion, which the paper then sidesteps via the injection-recovery criterion (b). The 0.30 number is given no derivation. **Fix:** either replace with a per-modality gate (e.g., relative to a baseline of random reconstruction) or eliminate criterion (a) entirely in favor of injection-recovery.

### P3-M25 — Equation E1 vs Lentati et al. [36] form: convention worth verifying explicitly
Eq. E1 uses (γ−3) log10 fyr − γ log10 fi, which is consistent with a P(f) = A²/(12π²) × (f/fyr)^(−γ) × fyr^(−3) × Tobs^(−1) convention (the fyr^(−3) gives the −3 log10 fyr term). But Lentati et al. [36] and Ceffyl [their ref. 18] do not use a uniform notation; the meaning of A depends on whether the fyr^(−3) is absorbed or factored. Given that this normalization fixes log10 A = −14.025 (a key reported posterior), the convention must be made explicit or the cited A cannot be compared to other PTA papers. **Fix:** add one sentence stating which convention is used and cite the exact Ceffyl source line.

### P3-M26 — App. C "shot-noise sensitivity" section uses incompatible Fisher numbers vs §V (Appendix C section 1)
Fig. 8 quotes σ(fNL) = 12.72 (multi-tracer baseline) → 12.56 (with 15% Heinrich penalty) → 13.35 (with 30%), and asserts this range "is consistent with the shot-noise-degraded value across the full 15–30% Heinrich-et al. penalty range." But the headline §V improvement is from 8.98 → 8.14, on an entirely different scale. The conclusion "+7.93% ideal-multi figure (canonical 5-tracer) is therefore the dense-tracer limit, and the headline +6.1% DESI-only improvement is consistent…" reads as if the two are on the same axis. They are not (see P3-E12). The "consistency" claim is then unverifiable. **Fix:** if Appendix C is meant to be a validation of §V, the baselines must match.

### P3-M27 — Abstract sentence "fNL=−35/8…testable at 3–5σ with SPHEREx" cites Heinrich et al. [33] σ(fNL)≈0.7
At σ(fNL) ≈ 0.7, the fNL = −4.375 prediction is detectable at |fNL|/σ ≈ 6.3σ, not "3–5σ". The body (§V para. (c)) reproduces "3–5σ detection significance for the matter-bounce fNL = −35/8 prediction (uncertainty range reflects systematic degradation budget)" without showing the degradation calculation that takes 6.3σ down to 3–5σ. **Fix:** show the systematic budget that maps σ=0.7 to 3–5σ, or correct the significance.

### P3-M28 — Fig. 6 caption "BigAE reconstruction" (red dashed) shown for SDSS panels even though SDSS was native-retrained
Fig. 6 panels (b), (d), (f) are labeled "SDSS DR18" and show "red dashed: BigAE reconstruction." Which BigAE? The cross-transfer DESI-trained one, or the native-retrained SDSS one (val_loss 0.0311)? Given the catalog version released is Path-C native, the SDSS panels should show the native reconstruction. As written, the figure caption is ambiguous and likely shows cross-transfer reconstructions that are no longer the published method.

### P3-M29 — "Mean Z-arm sub-score ⟨rZ⟩ = 3.9 across the 12 selected candidates; all objects have total score S > 5" (§III B)
This says the per-arm Z-score is 3.9 but the total score is >5. If rZ > rB and rZ > rR is the selection rule, and rZ ≈ 3.9, then for the total S > 5 to hold, the per-band scores must combine in a way the paper does not define. The relation between per-band rB,R,Z and total S is never given (Eq. 2 defines only S). The 12 high-z candidates' selection criterion is therefore unreproducible from the paper. **Fix:** define the per-band-to-total score relation explicitly.

### P3-M30 — "Spearman rank correlation ρ = −0.03 (p = 0.12 on a stratified subsample of 2,670 spectra, log-uniform in SNR)" (§III A)
Recomputing: for ρ = −0.03 with N = 2670, t = ρ × √((N−2)/(1−ρ²)) = −0.03 × √(2668/0.9991) = −1.55, two-sided p = 0.121. ✓ The arithmetic is fine, but the stratification is not described. "log-uniform in SNR" — over what range? With what bin count? Without these details, the test is unreproducible.

---

## NEW MINOR findings

### P3-m10 — Abstract uses "log10 B = +3.85, 'decisive' on Jeffreys' scale" but the formal Jeffreys boundary for "decisive" is log10 B > 2
Calling +3.85 "decisive" is fine on Kass-Raftery / Jeffreys, but the prior dependence noted in P3-M6 means the actual log10 B depends on prior choice. State the prior explicitly in the abstract or remove the qualifier.

### P3-m11 — Page 4 "DESI fiber assignment incompleteness… introduces a spatial selection function that could correlate with anomaly rate" — this systematic is acknowledged but not quantified
The systematic is named and dismissed in the same sentence. Either bound it or drop the mention.

### P3-m12 — Conclusion 6 reports "Planck native convolutional autoencoder: val_loss 0.4437, 100% injection-recovery"
Same compression as in §III F. The 0.4437 fails gate (a) by 48%; calling it a "PASS" in the conclusion (via gate (b)) without restating the gate (a) failure misleads. The full conclusion should say "(criterion (a) FAIL, criterion (b) PASS)" if internal labeling is to be used at all.

### P3-m13 — Table III column "SBigAE" gives J053856.1−640457 a value of 1.084, but Table I footnote § says the eROSITA threshold is "S > 0.259"
This is consistent (1.084 > 0.259), but the canonical-S axis described elsewhere in the paper has DESI scores up to 25.2 with threshold 5.0. The eROSITA canonical-S therefore lives on a different numeric scale than the spectroscopic surveys' canonical S despite using the same symbol. Note this explicitly or use a survey-specific subscript.

### P3-m14 — "deterministic permutation, checksum 1812395110" (§VI D (i))
A checksum without a hash algorithm specified is uncheckable. State "MD5", "SHA-256", or "CRC32".

### P3-m15 — Figure 9 panel labels include "AE=83518" for "Multi-band unknown" but §III A reports the score range 5.0–25.2
"AE=83518" is in the cross-transfer score scale (the unbounded scale seen in Fig. 2 right panel up to 10¹¹). After native retrain the same object's canonical-S should be much smaller. The taxonomy figure therefore mixes cross-transfer scores with the Path-C catalog representation. Update to native-retrain scores.

### P3-m16 — Equation E1 sets fi = (i+1)/Tobs for i = 0,…,29 → 30 frequency bins
But the abstract says "30 Fourier bins" and Appendix E says "NANOGrav 15-yr… (30f_fs{hd}_ceffyl)". The fi = (i+1)/Tobs convention misses the i=0 fundamental and double-counts; standard PTA convention is fi = i/Tobs for i=1,…,30. Verify this is the convention used by Ceffyl in [18] and that the chain ran the same one.

### P3-m17 — Abstract: "log10 B = +3.85, 'decisive' on Jeffreys' scale"; Body §V A: "BMB/SMBHB = 7.14×10³ (log10 B = +3.85, 'decisive' on Jeffreys' scale)"
Repeated decoration of the same number. In a 20-page paper this kind of repetition is space-wasting; pick one location.

---

## Summary of new-pass corrections

Of the new findings, the most critical are:
- **P3-E12** (σ(fNL) baseline of 8.98 vs 16.85 — the cosmology forecast and its appendix do not share an axis)
- **P3-E13** (7.9% improvement arithmetically inconsistent with σ=8.14 in the same sentence)
- **P3-E14** (one of three "validation" cross-survey matches has scores below the anomaly threshold)
- **P3-M21** (a Jaccard number in the conclusions appears nowhere in the body)

Each of these is independently sufficient to require major revision before acceptance. Together with the P3-E# items in the first-pass review, the paper requires (i) restructuring the headline claims around the recommended-catalog subset, (ii) correcting the Fisher envelope and the linear-vs-quadratic ambiguity, (iii) reconciling cosmology baselines between §V and Appendix C, (iv) re-verifying every cross-survey match against the published threshold, and (v) removing internal version-control jargon. I recommend **major revision** with a re-review on resubmission.