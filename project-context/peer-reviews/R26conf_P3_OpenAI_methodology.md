# P3 R26conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.84.pdf` md5=2539e13c pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7535 chars)
**Wall time**: 425.0s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches”

Scope of review
I evaluated the manuscript for methodology rigor, statistical validity, dimensional consistency, internal arithmetic coherence, and reproducibility. I audited all load‑bearing scalars in the abstract and conclusions against the body, checked representative percentages and ratios, and scrutinized figures/tables for consistency. Below I list findings with required fixes classified by severity.

ESSENTIAL (must be fixed for PRD)

P3‑E1 (Section V.b and Section VI.D(i); pp. 15 and 17)
Problem: Fisher mapping constant F0 is dimensionally inconsistent with the stated formula.
Quoted text (p. 15): “1/σ^2(fNL) = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747 … inserting αjk = 0.19 gives σ(fNL) = 8.14 …”
Issue: If 1/σ^2 = F0 + c α^2 and the single‑tracer baseline is σstd = 8.98, then F0 must be 1/σstd^2 = 1/8.98^2 ≈ 0.0124, not 1/8.98 ≈ 0.1113. The central value 8.14 is numerically consistent only if F0 = 1/8.98^2.
Required fix: Correct F0 everywhere to F0 = 1/σstd^2 = 1/8.98^2. Audit all occurrences (pp. 15 and 17), equations, and any downstream numbers to ensure internal consistency.

P3‑E2 (Section III.F; Table I row/footnotes; pp. 9 and 7)
Problem: Inconsistency in the Planck anomaly selection fraction after the Path‑C native retrain.
Quoted text (p. 9): “Input: 20,000 SMICA CMB map patches … Anomaly count: 200 (top 1%). … The Path‑C native pipeline extracts an independent, 10× larger 2 × 10^5‑patch bank … with the Planck tier held at the same canonical count of 200 …”
Issue: After moving to a 200,000‑patch native bank, selecting 200 patches is top‑0.1%, not top‑1%. Table I and Section III.F still describe the Planck tier as “top 1%”, which is only true for the legacy 20,000‑patch cross‑transfer pass.
Required fix: State unambiguously that the published Planck tier is the top‑200 by score from a 200,000‑patch native rescore (i.e., top‑0.1% of that bank), and remove or correct all “top 1%” references for the Planck Path‑C tier. Update the “Rate (%)” for Planck in Table I accordingly or clearly mark it as a fixed‑count selection, not a rate.

P3‑E3 (Section III.E; Table III and associated text; p. 8–10)
Problem: eROSITA selection axis is unreconciled with the canonical S definition; the published threshold 0.259 is not reproducible.
Quoted text (p. 8): “Anomaly count: 298, a fixed top‑298 score‑knee cap … this threshold axis could not be reconciled post hoc with the canonical S … the selection is therefore best read as the fixed top‑298 cap … the SBigAE ordering is non‑monotone in the committed raw artifact …”
Issue: PRD requires a reproducible selection criterion. Publishing a non‑reproducible threshold value (0.259) on an unspecified/non‑monotone axis is not acceptable. While you state the membership list is reproducible, Table III and the narrative still present SBigAE values and a threshold that cannot be regenerated.
Required fix: Either (a) re‑run the eROSITA scoring to place selection on the declared canonical S axis (Eq. 2), or (b) formally redefine the selection as “rank‑298 by reproducible committed‑raw score” and remove all unusable SBigAE values and the 0.259 threshold from the main text and tables. In both cases, provide exact code and data references (DOIs) that reproduce the ranking.

P3‑E4 (Abstract; Table I footnotes; Table V footnote; multiple locations: pp. 1, 7–8, 20)
Problem: Version‑history and review‑log language is embedded in the main text.
Examples:
– Abstract (p. 1): “an earlier draft quoted 264,938/264,738 …”
– Table V footnote (p. 20): “an earlier draft listed 10.6 s … withdrawn”
– Multiple places with internal audit/file references, e.g., “artifact r24conf … pod_session_batch.json”, “r23conf_dedup_audits.json”.
Issue: PRD does not accept version‑history commentary, withdrawn claims, or internal bookkeeping in the finished manuscript.
Required fix: Remove all “earlier draft”, “withdrawn”, and internal audit/file‑name prose from the main text and tables. If reproducibility artifacts are essential, cite a stable Zenodo/DOI with a brief description, not internal paths or review‑log notes.

MAJOR (significant revisions needed)

P3‑M1 (Section V.b; p. 15)
Problem: Numerical error in the “de‑biased amplitude” example.
Quoted text: “max(0, αˆ^2 − σ^2α) = max(0, 0.192 − 0.652) = 0”
Issue: αˆ = 0.19 ⇒ αˆ^2 = 0.0361; σα = 0.65 ⇒ σ^2α = 0.4225. The printed numbers 0.192 and 0.652 are incorrect. The qualitative conclusion (negative) remains, but a numerical error in a load‑bearing example undermines confidence.
Required fix: Replace with the correct values: max(0, 0.036 − 0.423) = 0. Audit surrounding text to ensure consistency.

P3‑M2 (Section III.C; Table I footnote ♡; pp. 6–8)
Problem: SDSS “native continuity slice” selection is ad‑hoc and conflates thresholds.
Issue: The primary SDSS native result is presented as a fixed‑size “continuity slice” (77,905 at S ≥ 0.1060; 4.046% of 1,925,279) chosen to match the cross‑transfer count, while two other thresholds (top‑1% at S ≥ 0.2051 and S > 5 yielding 12 objects) are also used. This invites confusion and makes rate comparisons opaque.
Required fix: Choose a single, pre‑declared primary SDSS selection axis for the main analysis (preferably the canonical S with a fixed percentile or absolute cut), and relegate the continuity slice to an appendix or data‑release note. Make rate comparisons only on like‑for‑like thresholds (e.g., S > 5).

P3‑M3 (Section IV.A; p. 10–11)
Problem: Aggregate SIMBAD‑unmatched fraction mixes matching radii and denominators.
Quoted text: “aggregate 58.8% … pooled over the top‑100 anomalies of four surveys … at 3″; per‑survey unmatched fractions in Table I use 5″.”
Issue: The mixed radii and pooled sampling make the 58.8% headline hard to interpret and not directly comparable to table entries.
Required fix: Report aggregate unmatched fractions at both 3″ and 5″ with explicit denominators and confidence intervals, or adopt a single radius throughout. Provide an explicit table with the exact counts per survey used in the pooled metric.

P3‑M4 (Section IV.B; p. 11–12)
Problem: Spatial uniformity χ^2 test is methodologically ill‑posed for inhomogeneous survey footprints.
Quoted text: “χ^2 = 376,713, dof = 24,048, χ^2ν = 15.7 … anomaly rate shows no correlation with Galactic latitude …”
Issue: The stated χ^2 test assumes uniform sky coverage and Poisson variance, which is invalid given the strong footprint variations. The authors acknowledge caveats, but the number risks being misinterpreted.
Required fix: Move the χ^2 statistic to an appendix or remove it. Retain the more robust correlation tests (latitude and dust maps) in the main text.

P3‑M5 (Table IV (c, e); Section V.c; p. 18 and p. 15)
Problem: Claims of percent‑level systematic impacts without derivations.
Quoted text: Table IV(c): “|Δσ/σ| < 0.01% …” and Table IV(e): “GR projection: |Δσ/σ| < 0.02% …”
Issue: No derivation or citation is provided in the main text to substantiate these precise fractional impacts.
Required fix: Provide a brief derivation or precise citation and inputs (kmax, volumes, tracer properties) that yield these bounds, or soften/remove the quantitative claims.

P3‑M6 (Multiple sections; e.g., Section IV.C; pp. 12–13)
Problem: Overuse of internal file paths and informal artifact names as references in the main text.
Issue: While reproducibility is commendable, PRD papers should not depend on opaque internal filenames.
Required fix: Replace internal path references with stable DOIs (Zenodo) and conventional citations. Describe in prose what each artifact contains.

MINOR (addressable without re‑analysis)

P3‑N1 (Figures 7 and 9 captions; pp. 13 and 16)
Problem: Some figure axis labels rely on context rather than explicit units (e.g., RA/Dec axes in degrees).
Required fix: Ensure all figure axes explicitly state units (deg, arcsec, etc.) and that colorbars are labeled with the quantity and units.

P3‑N2 (Section III.H; p. 9–10)
Problem: Matching‑radius choice for NEOWISE/Gaia is described qualitatively (“slightly tight”).
Required fix: Add a brief quantitative justification (e.g., expected completeness/purity trade‑off for WISE PSF ≃6″ at a 5″ association radius).

P3‑N3 (Section V and Appendix C; pp. 15–16 and 19–21)
Problem: Multiple σ(fNL) normalizations are used in different contexts.
Required fix: At every juxtaposition of σ(fNL) values derived under different normalizations (e.g., Fig. 11 vs. §V baseline), include an explicit “not directly comparable normalization” reminder (you already do this in Fig. 11; mirror this clarity anywhere they are juxtaposed in text).

P3‑N4 (Typographic consistency; multiple pages)
Problem: Occasional minor typographic glitches (e.g., spaced punctuation, long em dashes vs. hyphens).
Required fix: Standardize punctuation and typography per PRD style.

P3‑N5 (Data/code availability; p. 19)
Problem: GitHub/HuggingFace links are provided without persistent DOIs.
Required fix: Mint DOIs (Zenodo) for the exact code and dataset versions used to generate the results and cite them in the paper.

NITS (cosmetic)

P3‑n1 (Section III.B; p. 6)
Problem: “printed as ‘AE’ for legacy compatibility” is unclear without the figure.
Fix: Clarify in text what “AE” denotes or remove the aside.

P3‑n2 (Appendix F; p. 23)
Problem: “GPU‑blocked at the time of submission” is project status language.
Fix: Remove; simply state no native ACT retrain was performed.

Checks of arithmetic and internal consistency (selected)

- DESI anomaly rate: 195,829 / 22,504,897 = 0.870% (matches 0.87%).
- “73× like‑for‑like increase”: 195,829 / 2,685 (Liang et al. [11]) = 72.9 (≈73).
- “141× larger than [11]”: 378,080 / 2,685 = 140.8 (≈141).
- SDSS continuity slice proportion: 77,905 / 1,925,279 = 4.046% (≈4.05%).
- LAMOST rate compression: 44,075 / 2,054 ≈ 21.46 (≈21.5×).
- SDSS rate compression: 77,905 / 12 = 6,492 (≈6,500×).
- NEOWISE polar excess: (17/436) / 0.0152 = 2.57 (≈2.6×).
- SIMBAD false‑match (5″): π·5^2·3e−5 ≈ 0.00236 (0.236%; matches 0.24%).
- Dedup compression: (388,493 − 378,280) / 388,493 = 2.629% (matches).
- Multi‑survey clusters: 637; expected random coincidences ≲10 ⇒ <2% contamination (10/637 = 1.6%).
- Fisher envelope check with corrected F0: at α = 0.84, σ = 1/sqrt(0.0124+0.0747·0.7056) ≈ 3.92; at α clipped to 0, σ = 8.98 (matches).
- NANOGrav distances: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ (matches).
- Bayes factor ratio: 3.23 / 4.52e−4 = 7.14×10^3 (matches).

Additional comments on length and focus
The manuscript is lengthy (25 pages plus detailed footnotes). For a PRD methods paper, the core contribution would be clearer if the main text were reduced to ≤18 pages by moving diagnostic footnotes (especially long table footnotes and internal audit pointers) and ancillary spatial/uniformity tests to appendices or the data‑release note.

## Summary recommendation
MAJOR REVISIONS

The submission contains strong and carefully qualified analyses, but several critical methodology and presentation issues must be corrected for PRD: (i) fix the Fisher mapping constant (dimensional error) and the de‑biasing numeric example; (ii) rectify the Planck selection‑fraction inconsistency post‑retrain; (iii) resolve the eROSITA selection‑axis reproducibility (threshold vs. rank); and (iv) remove version‑history/review‑log language from the main text and replace internal file paths with stable DOIs. Clarifications around SDSS thresholding, pooled SIMBAD fractions, and systematic‑impact claims are also needed. With these addressed, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

P3‑E5 (Section III.E; Table III caption/text)
Problem: IsolationForest “raw score” range description contradicts reported negative values.
Quoted text (Table III caption): “SIF,raw is the IsolationForest raw isolation‑score value (anomaly score on a ∼0–3.5×10^4 scale…)”
Issue: Table III lists SIF,raw = −57.2 for J152039.9−570955. If the score is on a ∼0–3.5×10^4 scale, negative values should not occur. In sklearn/IF, score_samples or decision_function can be negative; the range description is therefore incorrect and misleading.
Required fix: Correct the description of SIF,raw to match the actual API/definition used (e.g., specify whether it is −decision_function, score_samples, or a rescaled variant), and remove the “0–3.5×10^4” range (or replace with the correct observed range, including negatives). Ensure consistency across text and tables.

MAJOR

P3‑M7 (Section III.C; Fig. 4 caption vs Table II; pp. 8–9)
Problem: The “84% cool dwarfs” claim does not align with the taxonomy table.
Quoted text (Fig. 4 caption): “dominant cluster (green, ∼84% of objects) contains ultra‑cool dwarfs (M7–T2)…”
Issue: Table II’s category breakdown does not present an 84% “cool dwarf” class. The two largest categories are “Uncategorized” (52.7%) and “NIR excess / high‑z” (33.0%), which by their labels are not equivalent to a pure cool‑dwarf population. The mapping from HDBSCAN clusters to astrophysical types is not quantified in the text.
Required fix: Provide an explicit cross‑tabulation (cluster → astrophysical label) or quantitative classifier that supports “84% cool dwarfs,” or soften to a qualitative statement (“dominant cluster visually consistent with cool dwarfs”) without the percentage. Ensure the figure caption and Section III.C narrative use the same, documented labeling.

P3‑M8 (Fig. 1 caption; §V and throughout)
Problem: Ambiguous reuse of the term “gold.”
Quoted text (Fig. 1): “83 gold‑tier anomalies (visual‑display set) … distinct from the 116‑object GOLD QSO‑candidate confidence tier used in §V.”
Issue: Two non‑identical sets are both called “gold/gold‑tier,” inviting confusion.
Required fix: Rename one of the sets (e.g., “Gold‑Display 83” vs “GOLD‑Confidence 116”) consistently across text, figures, and data release; add an explicit one‑line glossary noting they are disjoint and used for different purposes.

P3‑M9 (Table I, “Path‑C unique (primary)” total row)
Problem: Reporting a catalog‑wide “Rate (%) = 1.01” is misleading when several survey tiers are fixed‑count or fixed‑percentile by construction.
Issue: The Path‑C total mixes: DESI absolute S>5 rate, SDSS continuity slice, LAMOST native top‑1%, Planck fixed‑count (and, post‑retrain, top‑0.1% of the native bank), Gaia/NEOWISE fixed top‑1%, and eROSITA fixed top‑298. A single “Rate (%)” at catalog level suggests a measured frequency, which it is not.
Required fix: Remove the “Rate (%)” from the Path‑C total row or explicitly mark it “not a measured rate; heterogeneous fixed‑count/fixed‑percentile inputs.” If retained, add a footnote stating it is not interpretable as an intrinsic anomaly frequency.

P3‑M10 (Table I, DESI SIMBAD unmatched; §IV.A)
Problem: Table’s DESI “∼99%” unmatched fraction is derived from the top‑10,000‑by‑score subset but is displayed alongside full‑catalog rates for other surveys.
Required fix: Annotate in the table (footnote symbol on the DESI entry) that the DESI percentage refers to the top‑10,000 anomalies only, not the full DESI anomaly set, or provide the figure at a matched sampling depth for all surveys.

P3‑M11 (Section IV.B; “anomaly rate vs. Galactic latitude”)
Problem: The “no correlation with Galactic latitude” statement lacks a precise observable definition and normalization.
Issue: It is unclear whether “anomaly rate” is counts per HEALPix pixel, per unit area, or normalized by the parent‑catalog density/coverage (which vary strongly with footprint). Without an exposure/coverage model, the statistic can be dominated by selection geometry.
Required fix: Define the observable explicitly (e.g., anomalies per square degree per unit parent‑catalog density), or restrict the main‑text claim to the more robust dust‑correlation null. Move the latitude‑rate result to an appendix with details on normalization or remove it.

MINOR

P3‑N6 (Appendix E, Eq. E1)
Problem: Notation/definition gaps in the PTA likelihood model.
Issues:
- The symbol f_yr appears in Eq. (E1) but is never defined (presumably 1/year).
- The quantity ρ_i is introduced without a units/meaning statement (e.g., is this log10 ρ_gw per Fourier bin, proportional to Ω_GW?).
Required fix: Define f_yr explicitly and state what ρ_i represents (units or “dimensionless by construction”), plus any conventional normalizations used.

P3‑N7 (Section II.B; per‑arm residuals rB, rR, rZ usage)
Problem: The text quotes large per‑arm mean‑absolute‑residual values (e.g., rZ ≈ 5.3) without restating units or scale.
Required fix: Add a brief reminder that rX are on the normalized input scale (not σ‑units), are mean‑absolute residuals across downsampled bins, and are not comparable across surveys as significance measures. A one‑sentence clarification near §III.B would prevent misinterpretation.

P3‑N8 (Table V, footnotes; Section II.C)
Problem: Minor clarity on Planck throughput/processing scale.
Issue: The paper processes both the legacy 20,000‑patch bank (cross‑transfer baseline) and a 200,000‑patch native bank; “37.3M sources and patches” excludes the native 200k rescore in the Ntotal arithmetic, while throughput numbers reference the 200k rescore.
Required fix: Add a single clarifying sentence in §II.C or Table V footnote stating that headline Ntotal counts refer to the cross‑transfer inputs used for anomaly‑tier selection, while the native 200k rescore is an internal training/scoring bank used to rank the same published top‑200.

P3‑N9 (Fig. 2 caption; Fig. 3 axes)
Problem: Axis unit labels are implicit.
Required fix: Add “deg” to RA/Dec axes in Fig. 2 and ensure Fig. 3 right‑panel x‑axis explicitly states “Anomaly score S (dimensionless)”; ensure all axis units are printed consistently.

P3‑N10 (Section IV.C; multi‑survey coincidence denominator)
Problem: The text cites “<2% contamination” by comparing expected random coincidences (≲10) to 637 observed multi‑survey clusters, but the construction of the expected value is only sketched.
Required fix: Add a parenthetical with the exact null procedure used (e.g., sky‑density model or scrambling scheme) or move the contamination estimate to an appendix table alongside the RA‑shift controls already mentioned.

EXPLANATION
This fresh‑eyes pass focused on points that frequently slip through initial reviews: table/figure numerical coherence, dimension/notation consistency in equations, and ambiguous or potentially misleading presentation choices. I did not repeat items already flagged in my first report. The new essential/major items above address (i) an IsolationForest score‑range contradiction, (ii) an unsupported and potentially misleading “84% cool dwarfs” claim, (iii) ambiguous “gold” tier naming, (iv) a misleading catalog‑level “Rate,” (v) table‑level clarity on how DESI’s unmatched percentage was computed, and (vi) an ill‑defined latitude‑correlation statement. The minor items tighten notation, units, and scope clarifications. With these addressed in addition to the earlier essential fixes, the manuscript’s methodological rigor and presentation should meet PRD standards.