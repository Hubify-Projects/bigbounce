# P3 R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.80.pdf` md5=03f05e26 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6870 chars)
**Wall time**: 316.5s

---

Referee report for “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches” (23 pages)

Overall scope and assignment
- Role: PRD methodology referee. Focus: statistical/methodological rigor, derivation chains, dimensional consistency, internal arithmetic, uncertainty propagation, and consistency of reported figures/tables with text. I audited all equations, tables, figure captions, and headline numbers in the abstract and conclusions against the body text.

Findings

ESSENTIAL

ID: P3-E1
Section: V.b; Table IV (i); Page(s): 12 and 16
Problem: Misdefined Fisher-baseline constant F0. Text states: “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” This is dimensionally incorrect. With σstd = 8.98, F0 must equal 1/σstd^2 = 1/8.98^2 ≈ 0.01240, not 1/8.98 ≈ 0.1113. The paper’s numerical results (σ(fNL) = 8.14; envelope [3.92, 8.98]) are consistent with F0 = 1/8.98^2, so the written value is wrong even though the downstream numbers use the correct value.
Required fix: Replace “F0 = 1/8.982” with “F0 = 1/8.98^2 = 0.01240” everywhere it appears (Section V.b text and Table IV (i)). Explicitly show the calculation used to obtain σ(fNL) = 8.14 from αjk = 0.19 and c = 0.0747, and show the envelope endpoints are obtained with α = 0 and α = 0.84 to avoid any ambiguity.

ID: P3-E2
Section: Table V footnote; Page: 18
Problem: Version-history language inside the paper body: “an earlier draft listed 10.6 s, which is inconsistent … and has been withdrawn.” PRD instructions require that no version-history/editorial bookkeeping appear in the paper.
Required fix: Remove all version-history/editorial-history phrases from the body, tables, and footnotes. Replace with a neutral statement (e.g., “training wall-clock not preserved in run logs; therefore we do not quote a value”).

ID: P3-E3
Section: Table I footnote (long footnote under “§”); Page: 8–9
Problem: Additional version-history language: “The earlier ‘strict subset’ framing is replaced with this exact 284/298 = 95.3% overlap.” This is internal version-history wording.
Required fix: Remove this sentence or rephrase without version-history (e.g., “We report the exact 284/298 = 95.3% overlap; because the two detectors share the same latent representation, we do not assign an independence-null significance to this figure.”).

MAJOR

ID: P3-M1
Section: Data availability; Page: 17
Problem: Reproducibility timing/availability. The Data availability section states the catalog and code “will be made public with the arXiv posting.” For PRD, methodological claims that rest on large-scale computation must be reproducible at acceptance and, ideally, at review. As written, the artifacts are not yet public.
Required fix: Make the catalog and code repositories public now and include permanent DOIs (e.g., Zenodo) and immutable commit hashes in the manuscript. Confirm that the deposited Path-C catalog reproduces every top-line scalar (e.g., 378,280 unique, 388,493 pre-dedup, 10,213 collapsed, 637 multi-survey clusters, etc.). If embargo is unavoidable before acceptance, supply the editorial office and referees with private but accessible links and commit to public DOIs upon acceptance.

ID: P3-M2
Section: IV.B (Spatial Analysis); Page: 10–11
Problem: Pixel-count and mask ambiguity in the spatial χ^2 test. You report “across 38,330 HEALPix pixels (Nside = 64)” while a full-sky Nside=64 map has 49,152 pixels. It is unclear what mask/footprint selection produced 38,330 pixels, and how the degrees-of-freedom were computed. As given, χ^2, dof, and χ^2_ν are not interpretable without a precise mask description.
Required fix: Specify the exact angular mask used (per-survey footprints, union/intersection, and any latitude or dust masks), how empty or outside-footprint pixels were handled, and how dof = 38,329 was calculated. Provide a link to the mask file(s) in the companion repository or include in Supplemental Material.

ID: P3-M3
Section: Abstract; Table I footnote ♠; Conclusions; Page(s): 1, 8–9, 16
Problem: Inconsistent rounding/definition of the “catalog-grade subset.” The abstract states “∼265,000 unique entries (… including the 200 Planck map patches), which excludes the LAMOST exploratory tier.” Table I footnote ♠ gives “264,938 unique objects” for the catalog-grade tier. This number is used to guide downstream users; it must be consistent across the paper and precisely defined (does it include the 200 Planck patches; at what dedup radius; which surveys exactly).
Required fix: State a single exact figure (to the unit count) for the catalog-grade subset, clarify whether it includes the 200 Planck patches, and ensure this exact number is used consistently in abstract, results, and conclusions. Clarify that this count is at 5″ dedup radius.

ID: P3-M4
Section: V (Cosmological applications) and Appendix C; Page(s): 12–14, 19
Problem: Insufficient methodological detail to reproduce σ(fNL)std = 8.98 and c = 0.0747. The baseline single-tracer σ(fNL) = 8.98 and the constant c used in 1/σ^2 = F0 + c α^2 are central to the claimed “7.9% improvement” statement. The paper does not give enough detail to independently reproduce these constants (e.g., redshift binning scheme, tracer biases, number densities, survey volume, k-range, covariance, whether RSD and shot-noise are included).
Required fix: Provide a concise but complete specification of the Fisher setup used to obtain σ(fNL)std = 8.98 and c = 0.0747: redshift bins, b(z), n(z), survey volumes, k-range and binning, included terms (RSD, Alcock-Paczynski, shot-noise), the treatment of systematics, and the exact expression used for the multi-tracer Fisher element that yields the α^2 scaling. Alternatively, post a minimal reproducible notebook and input files in the repository and cite them explicitly.

ID: P3-M5
Section: III.E; Table I footnote “§”; Page(s): 7–9
Problem: Even with caveats, the sentence “the random-independence expectation would be ≈ 3 matches” for the BigAE vs IsolationForest overlap (284/298) invites an inappropriate significance interpretation because the detectors are not independent (shared latent). Including a random-independence number next to a dependent overlap is misleading.
Required fix: Remove the “≈ 3 matches” independence-null reference. Retain only the descriptive overlap and the explicit statement that no independence significance is assigned due to shared latent features.

ID: P3-M6
Section: III.A; Page: 4–5
Problem: Artifact-rate claim without sufficient method detail. “Spectral inspection of the top 200 confirms a 0% artifact rate (each spectrum’s peak-residual wavelength was compared against 11 known sky and telluric emission/absorption features; zero were attributable).”
Required fix: List the 11 features checked and the exact decision rule (tolerance window, multi-line handling). Provide a brief table in the appendix or a link to a CSV in the repository documenting this check for the top 200.

MINOR

ID: P3-m1
Section: Abstract; Page: 1
Problem: Wording may confuse “sources and CMB map patches (DESI DR1, SDSS DR18, …)” as if every survey has map patches.
Required fix: Rephrase to “37.3 million sources across DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Gaia DR3, NEOWISE, and 20,000 Planck CMB map patches (ACT DR6 quarantined…).”

ID: P3-m2
Section: III.E; Table III; Page: 9
Problem: Table III only lists Declination; RA is missing.
Required fix: Add RA (and, ideally, l,b) to the table for completeness.

ID: P3-m3
Section: IV.B; Page: 10–11
Problem: The χ^2 test result is dominated by footprint geometry; this is noted, but the statistical object being tested (uniform over what domain) is still ambiguous.
Required fix: Add one sentence explicitly defining the null hypothesis and sample space (e.g., “we test uniformity over the union of the seven-survey footprints restricted to pixels with …”).

ID: P3-m4
Section: Appendix E (Eq. E1); Page: 18
Problem: The expression for log10 ρi is given without a direct citation to a standard reference for the PTA free-spectrum likelihood parameterization or a derivation for units/normalization.
Required fix: Cite a standard reference for this parameterization and add a sentence on units (ρ is dimensionless per-bin power, fyr = 1/yr).

ID: P3-m5
Section: Fig. 3 caption; Page: 6
Problem: The SDSS transfer-learning panel shows S up to 1.9×10^11 while S is elsewhere described as a per-survey z-score. The caption notes this as a cross-transfer artifact but could be clearer that these are not interpretable as Gaussian z-scores.
Required fix: Add to caption: “In the transfer-learning case, S is numerically large due to severe out-of-distribution residuals; it should not be interpreted as a Gaussian z-score.”

NITS

ID: P3-n1
Section: Throughout; Page: multiple
Problem: Minor style consistency: arcsecond symbol appears as 5′′ and 5" in different places; degree sign spacing varies.
Required fix: Standardize to 5″ for arcseconds and consistently formatted degree symbols.

ID: P3-n2
Section: IV.D; Page: 11
Problem: Tone: “decisive on Jeffreys’ scale.” PRD generally prefers numerical statements over adjectival labels.
Required fix: Consider replacing “decisive” with the numerical log10 B = +3.85 alone or with “log10 B = +3.85 (Jeffreys’ scale).”

ID: P3-n3
Section: VI.A; Page: 14
Problem: Strongly rhetorical phrasing (“single most important methodological lesson”).
Required fix: Tone down to standard scientific style (e.g., “A key methodological lesson…”).

Arithmetic and internal-consistency checks (passed)

- 378,280 unique anomalies = 388,493 survey-level detections − 10,213 collapsed (2.629% compression). Verified.
- Point-source unique count = 378,280 − 200 (Planck patches) = 378,080. Verified.
- DESI anomaly rate 195,829/22,504,897 = 0.870%. Verified.
- SDSS rate-compression factor 77,905 (cross-transfer, S>5 scale) → 12 (native, S>5) ≈ 6,492×. Verified.
- LAMOST rate-compression factor 44,075 → 2,054 at S>5 ≈ 21.5×. Verified.
- NEOWISE ecliptic-pole mask: retain 419/436 = 96.1%; polar-cap fraction 17/436 = 3.90% vs uniform two-cap area 1 − cos 10° = 1.52%, ratio ≈ 2.57. Verified.
- SIMBAD random 5″ false-match probability: π(5″)^2 × 3.0×10^−5 arcsec^−2 ≈ 0.235% per source; 0.24% quoted. Verified.
- Dedup-radius sensitivity: unique counts 378,604 / 378,280 / 378,145 at 3″ / 5″ / 7″; maximum fractional deviation from 5″ is 324/378,280 ≈ 0.0856%. Verified.
- Landy–Szalay αjk = 0.19 ± 0.65 used with F0 = 1/8.98^2 and c = 0.0747 gives σ = 8.14; at α = 0.84, σ = 3.92; at α = 0, σ = 8.98. Verified (once F0 is corrected).
- NANOGrav KDE posterior γ = 2.567 ± 0.382; Δ to γ=3.0 is 1.13σ; Δ to 4.33 is 4.61σ; Bayes factor ratio BMB/SMBHB ≈ 7.14×10^3. Verified.

Length assessment
- 23 pages including appendices is acceptable given the multi-survey scope and the two cosmology applications, provided the ESSENTIAL and MAJOR issues are addressed. No reduction is strictly required, though some consolidation of threshold-disclosure footnotes could be moved to an appendix for readability.

## Summary recommendation
MAJOR REVISIONS

The analysis is ambitious and many internal checks are sound, but there is a critical dimensional/numerical error in the Fisher baseline constant F0 (must be 1/σ^2, not 1/σ), version-history/editorial prose must be removed from the body, and the cosmology-forecast section needs enough methodological detail to reproduce σ(fNL)std and c. Reproducibility also requires that the catalog/code be made publicly accessible with persistent identifiers. Clarifications on the spatial-mask χ^2 test and consistent catalog-grade counts are also needed. After these corrections and clarifications, the paper could meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (fresh-eyes)

ESSENTIAL

ID: P3-E4
Section: III.F; Table V footnote; II.C; Table I; Abstract; Pages: 7–8, 10, 18, 1
Problem: Planck patch-count and timing inconsistency (20k vs 200k). The body (III.F) and Table I state the native Planck run scored Ntotal = 20,000 patches with a top-1% = 200 anomalies (used in all headline sums). But Table V’s Planck footnote says “The 200K-patch full re-score took 25.3 s,” implying Ntotal = 200,000. II.C also states “the CMB (Planck) ... ≲10 s of GPU time,” which is inconsistent with 25.3 s if 200k were scored. These cannot all be true simultaneously.
Required fix: State unambiguously how many Planck patches were scored for the released catalog (20,000 or 200,000) and make all occurrences (III.F text, Table I Ntotal, Table V footnote, II.C timing) consistent. If 200,000 were scored, explain why only 200 (not 2,000) are released under a “top-1%” rule (e.g., if a top-0.1% cap was applied), and update all totals if needed. If 20,000 were scored, correct the “200K-patch full re-score” and the ≲10 s vs 25.3 s timing conflict.

MAJOR

ID: P3-M7
Section: IV.A; Fig. 6; Table I; Pages: 9–10
Problem: SIMBAD matching-radius inconsistency across statements used for pooled vs per-survey fractions. The text first states a 5″ cone is used; the pooled aggregate 58.8% line is then computed at 3″ on top-100 subsets; per-survey bars in Fig. 6 appear to be 5″ values. Mixing 3″ and 5″ in the same figure/paragraph invites apples-to-oranges inferences.
Required fix: Use a single matching radius for all quoted SIMBAD fractions in the main text and Fig. 6, or explicitly label which bars/lines are at 3″ vs 5″ and avoid cross-comparing them. Provide the pooled aggregate at the same radius as the per-survey bars or plot both radii side-by-side.

ID: P3-M8
Section: III.E; Table I footnote (§); Table III; Pages: 7–9
Problem: Notation collision for eROSITA anomaly threshold. The text and Table I variously describe the eROSITA cut as “S > 0.259 (top 0.03%; score-knee)” while elsewhere clarifying this is on the IsolationForest raw-score axis. “S” is defined earlier as the BigAE z-scored MSE, so using S for the IF raw score is misleading. Table III then introduces SBigAE and SIF,raw, indicating the authors do track two distinct axes.
Required fix: Replace every occurrence of “S > 0.259” tied to the IsolationForest with “SIF,raw > 0.259” (or whatever the exact IF threshold is), and keep “S” exclusively for the BigAE z-scored MSE. Update Table I footnote (§) and III.E text accordingly.

ID: P3-M9
Section: II.C (GPU Inference Pipeline) vs Table V footnote (Planck) and §III.F; Page: 3, 18, 7
Problem: Inference-time inconsistency. II.C claims “the CMB (Planck) and photometric surveys each ≲10 s of GPU time,” while the Planck footnote quotes a 25.3 s re-score. This timing also depends on the inconsistent patch-count noted in P3-E4.
Required fix: Reconcile the Planck inference time with a single, consistent patch-count; correct either II.C (≲10 s) or the 25.3 s figure and ensure the stated throughput matches the corrected count/time.

ID: P3-M10
Section: IV.C (Cross-survey matches); Page: 11
Problem: Unsupported “expected random coincidences ≲ 10” claim. The text asserts ≲10 expected random multi-survey coincidences at 5″ without showing the sky-density and area arithmetic for the seven survey pairs.
Required fix: Provide a back-of-envelope calculation (surface densities per survey, overlap area, 5″ cross-match annulus approximations) or a Monte Carlo null using scrambled positions, and quote the resulting expected count with its uncertainty.

ID: P3-M11
Section: Fig. 2 caption vs content; §III overview; Page: 5
Problem: Caption ambiguity about ACT inclusion. The caption header and legend show ACT points in the 319,443 cross-transfer baseline map, but the caption text says “ACT DR6 is quarantined and excluded.” For a reader, this suggests ACT is excluded from the figure, which it is not.
Required fix: Rephrase to “ACT DR6 is quarantined and excluded from the Path-C headline counts; it is included here only as part of the cross-transfer baseline diagnostic map.”

MINOR

ID: P3-m6
Section: II.B (Training and scoring, DESI thresholds); Page: 3
Problem: Wording implies manual setting of σval. “σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” σval should be the empirical standard deviation on the validation split; the threshold is implied by S = (MSE − μval)/σval.
Required fix: Rephrase to “With μval ≈ 0.0287 and empirical σval measured on the validation split, the S > 5 threshold corresponds to MSE ≈ 0.143.”

ID: P3-m7
Section: III.A; Pages: 4–5
Problem: Duplicate/near-duplicate paragraph on DESI per-class anomaly rates and z-peaks appears twice with slightly different phrasing.
Required fix: Consolidate to a single occurrence to avoid confusion about whether these are two distinct analyses.

ID: P3-m8
Section: Claims of “largest multi-archive anomaly search”; Abstract and Table I; Pages: 1, 8–9
Problem: The “largest multi-archive anomaly search reported to date” claim is plausible but cites only a largest single-survey comparator [11]. No multi-archive comparator is cited.
Required fix: Add a citation (or short survey) establishing that no prior work combined anomaly sweeps across as many archives/sources, or qualify the claim (e.g., “to our knowledge”).

ID: P3-m9
Section: Fig. 2 title and y-axis labeling; Page: 5
Problem: Figure title reads “Spatial distribution of all 319,443 anomalies across 8 archives,” while the paper’s canonical results use Path-C native retrains (7 archives). The caption does clarify “cross-transfer baseline,” but the title as rendered can mislead skim-readers.
Required fix: Prefix the title with “Cross-transfer baseline:” or mirror the caption’s first words.

NITS

ID: P3-n4
Section: Abstract vs §V.A; Pages: 1, 13
Problem: Minor rounding divergence for Bayes factor: abstract gives BMB/SMBHB = 7.1×10^3; body gives 7.14×10^3.
Required fix: Standardize to one rounded value throughout.

ID: P3-n5
Section: Throughout; Pages: multiple
Problem: Minor consistency issues remain in notation for arcseconds/quotes and prime usage in a few places beyond those already noted (e.g., occasional 5" appears alongside 5″).
Required fix: Global search-and-replace to enforce 5″ and consistent degree/arcmin formatting.

EXPLANATION

I focused on items routinely missed in first passes: inconsistent sample sizes/timings (Planck 20k vs 200k re-score, ≲10 s vs 25.3 s), radius-mixing in SIMBAD unmatched fractions (3″ vs 5″ in the same figure/paragraph), notation collisions (eROSITA S vs IF raw), unsupported back-of-envelope claims (expected ≲10 random multi-survey coincidences), and caption/body ambiguities (ACT excluded vs displayed). These are new and not covered by my initial review.