# P3 R33conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.94.pdf` md5=f3bb1c93 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5779 chars)
**Wall time**: 377.9s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path‑C Unique Anomalies and a Native‑Trained Novelty Fraction from 37.3 Million Sources and Map Patches” (28 pp.)

Scope of review
I audited the methodology, internal arithmetic, statistical claims, dimensional consistency, and figure/table coherence across the full manuscript. Below I list all issues found, classified by severity, with page‑level citations and required fixes.

ESSENTIAL issues (acceptance-blocking)

P3-E1 (Abstract p.1; Sec. V(b) p.17; Table V note (i) p.20): Dimensionally inconsistent Fisher mapping for σ(fNL)
Quoted text/examples:
– Abstract: “1/σ2(fNL) = F0 + c α2 ... returns a central forecast σ(fNL) = 8.14” with F0 = 1/8.982 (also repeated in Sec. V(b) and Table V (i)).
Problem: 1/σ2 has units of 1/(variance). With σstd = 8.98, F0 must be 1/σ2 std = 1/8.982 ≈ 0.01237, not 1/8.982 ≈ 0.1113. As written, the mapping is dimensionally wrong and (if evaluated) would give σ ≈ 2.96, not 8.14. The correct central value 8.14 is only obtained if F0 = 1/8.982 and interpreted as 1/σ2 std with the square implicitly applied, which is not what the manuscript states.
Required fix: Replace every occurrence of F0 = 1/8.982 by F0 = 1/(8.982)2 = 0.01237 (to quoted precision) and verify all downstream numbers (central 8.14 and the [3.92, 8.98] envelope) recompute from this corrected mapping. State explicitly the units of F0 and c and show the short derivation/calibration of c from your five-α refit so the mapping is auditable.

P3-E2 (Multiple locations: Abstract p.1; Fig. 2 caption p.6; Sec. II.B p.3–4; Sec. III.E p.10–11; Table VI footnote p.23): Version‑history and internal‑round language in the body
Quoted examples:
– Abstract: “an earlier draft quoted 264,938/264,738 ...”
– Table VI footnote: “an earlier draft listed 10.6 s ... withdrawn”
– “recovered production training scripts (committed at pipelines/...)”
– “the figure is withdrawn in favor of the reproducible recompute above”
Problem: PRD does not allow internal version‑history commentary, “earlier draft” language, or opaque internal bookkeeping prose in the body text. Reproducibility pointers are fine, but log‑style notes and retracted numbers belong in a changelog, not the paper.
Required fix: Remove all “earlier draft ... withdrawn” and similar internal‑round language from the main text, captions, and tables. If provenance pointers are kept, confine them to a short Reproducibility appendix with stable identifiers only (commit hash/DOI), without narrative about prior drafts.

P3-E3 (Data availability p.22): Placeholder DOI and incomplete archival identifiers
Quoted text: “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
Problem: This is a placeholder. PRD requires stable, citable artifacts at acceptance. The present text is non‑compliant.
Required fix: Provide the minted DOI(s) (and the exact tag/commit hash of the code release) in the paper. Remove all placeholder language. Ensure that the listed SHA‑256 manifest in the repo matches the versions used to produce the results.

P3-E4 (Sec. V(b) p.17; Table V (i) p.20; Appendix C p.22–24): Primary estimator/formula for σ(fNL) improvement not derived or pre‑declared
Quoted text: “Fisher‑positivity‑respecting asymptotic form 1/σ2(fNL) = F0 + c α2 ... c = 0.0747 (5‑α refit).”
Problem: The mapping from an empirically measured bias ratio α to Fisher information is load‑bearing. At minimum, readers must see (i) the explicit Fisher setup, (ii) how α enters, (iii) how F0 and c are obtained (including the five α grid actually used, with values and fit residuals), and (iv) uncertainty propagation from σα to σ(fNL). Without this, the improvement claim is not reproducible.
Required fix: Add a subsection deriving the mapping. Show the five calibration points, their numerical values, the resulting fit for F0 and c (with uncertainties), and a brief justification that the quadratic form is valid in your regime. Keep the corrected dimensional form per P3‑E1.

P3-E5 (Sec. V.A p.18): Side‑by‑side σ–shift and Bayes‑factor statements without explicit non‑comparability warning
Quoted text: “γ = 3.0 sits at +1.13σ ... SMBHB γ = 4.33 at +4.61σ ... Proper Savage–Dickey Bayes factors ... BMB/SMBHB = 7.14×103 (‘decisive’).”
Problem: You juxtapose σ‑shift summaries and Bayes factors for the same question. These are different evidentiary metrics with different interpretations. Per PRD best practice, such juxtapositions must explicitly warn that they are not directly comparable.
Required fix: Add a sentence (at the point of juxtaposition) explicitly stating that posterior σ‑shift and Bayes factor are not directly comparable measures and quantify different aspects of the evidence; include a pointer to a standard reference (e.g., Trotta 2008).

P3-E6 (Sec. II.B p.3–4): Leakage in tabular feature scaling; effect on rankings not demonstrated
Quoted text: “the scalers are fit on the full sample rather than the training split ... we assume it does not materially reorder the within‑survey anomaly ranking ... a bounded robustness check ... is queued and will be reported with the released artifacts.”
Problem: Using full‑sample statistics (including tails) to scale features contaminates the validation distribution and can alter the ranking, directly impacting the “top‑1%” selections for Gaia/NEOWISE/eROSITA. An assumption plus a promise to check later is not sufficient for PRD.
Required fix: Perform and report the train‑split‑only rescaling for Gaia, NEOWISE, and eROSITA; quantify the Jaccard overlap and Spearman rank correlation for the top‑tier selections versus the published set. If differences exceed a few percent, update the catalogs and all affected tallies.

P3-E7 (Sec. III.E p.10–11; Table I p.7 caption/footnotes): eROSITA “0.259” threshold appears while axis is declared irreproducible
Quoted text: “top‑298 score‑knee cap ... threshold 0.259 on the production scoring run’s score‑knee axis ... axis irreproducible ... selection is best read as fixed top‑298 cap.”
Problem: The number “0.259” appears several times and reads like a data‑driven threshold despite being explicitly irreproducible. This is confusing and undermines reproducibility.
Required fix: Purge “0.259” from all tables/captions/body and uniformly present the eROSITA tier as a membership‑only top‑298 list (ranked by the committed raw reconstruction score). Keep the quantitative IF‑overlap and XV‑stability results; ensure that no per‑object SBigAE values are displayed anywhere.

MAJOR issues

P3-M1 (Sec. G p.12; Data availability p.22): Gaia DR3 preprocessing “lineage‑inferred” rather than recovered
Quoted text: “the exact 20‑feature production script ... was not recovered ... we state explicitly that the Gaia preprocessing specification is lineage‑inferred.”
Problem: This prevents exact reproduction of the Gaia tier. Given the low XV‑stability (41%) already flagged, this is particularly problematic.
Required fix: Reconstruct and publish the exact preprocessing used for the 50K run (or rerun the Gaia analysis with the recovered 21‑feature pipeline and publish that exact configuration). If impossible, demote Gaia to an appendix with an explicit reproducibility caveat and remove it from headline counts.

P3-M2 (Sec. IV.A p.12–13; Fig. 6): “Genuine novelty fraction” lacks a false‑match (chance‑coincidence) budget for the 18‑catalog CDS X‑Match
Quoted text: “17.8% (Wilson 68% ±1.2%) ... absent from all major source catalogs surveyed.”
Problem: While the 5″ matching cone is stated, no false‑match (random‑overlap) rate is computed for the 18‑catalog union. Given heterogeneous source densities, an order‑of‑magnitude estimate is needed to bound spurious “novelty”.
Required fix: Provide an analytic or empirical (offset control) estimate of the random‑match rate for the 18‑catalog union at 5″, and quote the corrected novelty fraction (or an uncertainty band that includes this effect).

P3-M3 (Sec. III.H p.12): NEOWISE pole‑cap excess: No statistical significance reported
Quoted text: “3.9% polar‑cap fraction represents a 2.6× excess over the uniform‑null expectation (1.52%).”
Problem: The multiplicative factor is reported, but not the binomial significance. From your numbers (17 vs. 6.6 expected), this is ≈4σ. The effect size/significance should be stated if used as scan‑pattern contamination evidence.
Required fix: Add the binomial (or Poisson) significance of the excess with the exact expected and observed counts.

P3-M4 (Sec. IV.B p.14): Spatial χ2 without a normalized effect‑size or model check
Quoted text: “χ2 = 376,713, dof = 24,048, χ2ν = 15.7 ... selection‑uncorrected.”
Problem: While you correctly caution against over‑interpretation, a normalized effect size (e.g., RMS fractional residual per occupied pixel) would help readers gauge the magnitude. Also cite the mean count per occupied pixel (with variance) under the working model.
Required fix: Add a compact effect‑size summary (e.g., RMS fractional deviation) and the mean/variance of the per‑pixel counts under your stated null.

P3-M5 (Sec. III.F p.11): Planck top‑200 include training patches; “mild over‑representation” is asserted but not quantified
Quoted text: “152/48 vs. ≈170/30 expected ... mild over‑represents held‑out patches ...”
Problem: Quantify this with a simple hypergeometric p‑value, so readers see that the deviation from 170/30 is not suggestive of memorization.
Required fix: Add the exact p‑value for observing ≤152 training patches among the top‑200 under 85% train split.

P3-M6 (Throughout): Extensive in‑line file paths and audit‑trail artifacts in main text
Problem: While admirable for reproducibility, the density of pathnames and run‑log commentary distracts from the scientific narrative.
Required fix: Move all pathnames and run‑log citations to a Reproducibility appendix (or the data‑release README) and keep only stable identifiers in the main text.

MINOR issues

P3-m1 (Sec. II.B p.4): DESI S > 5 threshold to MSE ≈ 0.143: show σval
Quoted text: “... places the S > 5 threshold at MSE ≈ 0.143.”
Required fix: Report σval used (≈0.0229 from your numbers) so the mapping is auditable.

P3-m2 (Sec. III.A p.5–6; Table II p.8): Science‑class recount: supply uncertainty on the 1.3% fraction
Required fix: Quote a binomial 68% CI (e.g., Wilson) for the 2,468/190,015 = 1.30% match fraction.

P3-m3 (Sec. III.C p.8–9; Fig. 3 right): Extreme SDSS S values on cross‑transfer axis
Problem: The 1011 dynamic‑range axis is correct but startling. Since you explain this is a transfer‑artifact, explicitly label the panel “DESI‑trained (transfer) score axis; not comparable to native SDSS”.
Required fix: Add this explicit disclaimer to the figure caption or the panel label.

P3-m4 (Sec. IV.C p.14–15): RA‑only shift control for random coincidences
Problem: You already caution that RA‑only shifts are imperfect. A compact statement of the number of shifts and their spread would help.
Required fix: Briefly report the mean and standard deviation of the RA‑shifted control counts over your four shifts.

P3-m5 (Fig. 12 p.25): “Cool Dwarf” vs. “cool/unusual‑star family” wording
Required fix: Make the taxonomy family name consistent between caption and panel label.

NITs (editorial/cosmetic)

P3-n1 (Throughout): Heavy use of long dashes “—” for parentheticals; consider light editing for readability.
P3-n2 (Table I p.7; footnote symbols): Hearts/diamonds/suits‑style glyphs are non‑standard for PRD; switch to numeric/lettered footnotes.
P3-n3 (Units/labels): Ensure all axes include units where relevant (e.g., degrees, arcseconds; most already do).

Arithmetic and consistency checks (spot‑audited and OK unless otherwise noted)

- Headline tallies: 195,829 (DESI) + 77,905 (SDSS native continuity slice) + 113,342 (LAMOST native top‑1%) + 298 (eROSITA) + 200 (Planck) + 500 (Gaia) + 419 (NEOWISE) = 388,493; dedup compression 10,213 → 378,280 unique; percent compression 10,213/388,493 = 2.629%. OK.
- Point‑source vs. patches: 378,280 = 378,080 (point‑source) + 200 (Planck patches). OK.
- Catalog‑grade subset: 269,317 unique (6‑way dedup of DESI+SDSS+eROSITA+Planck+Gaia+NEOWISE) with 200 Planck → 269,117 point‑source; LAMOST overlap 4,379; 269,317 + 108,963 = 378,280. OK.
- Benchmarks vs. [11]: 378,080/2,685 ≈ 141×; 269,117/2,685 ≈ 100×; 195,829/2,685 ≈ 73×; science‑class‑restricted 2,468/2,685 ≈ 0.92×. OK and appropriately caveated in body.
- SIMBAD pooled unmatched fraction 235/400 = 58.8%. OK.
- NEOWISE pole‑cap expectation 2×(1−cos 10°)/2 = 1.52%; observed 3.9% (17/436). OK; add significance (P3‑M3).
- NANOGrav σ‑shifts: (3.0−2.567)/0.382 = +1.13σ; (4.33−2.567)/0.382 = +4.61σ. OK.
- Landy–Szalay αjk = 0.19 ± 0.65; 9.4% improvement computed as (8.98−8.14)/8.98 = 9.35%. OK once P3‑E1 is fixed.

Length and focus
At 28 pages, the paper is long for the core methodological contribution (autoencoder anomalies + calibration + two illustrative cosmology applications). With the required corrections/derivations included, you can still streamline by moving most audit‑trail text and survey‑specific operational details to a reproducibility appendix or data‑release README. A target of ~20–22 pages main text would be appropriate.

## Summary recommendation
MAJOR REVISIONS

The work is ambitious and potentially valuable, but there are blocking issues: a dimensionally incorrect Fisher mapping (affects the main cosmology forecast), substantial version‑history prose in the body, incomplete reproducibility (Gaia preprocessing; eROSITA threshold axis), and a few missing statistical controls (novelty false‑match budget, NEOWISE excess significance). Addressing the ESSENTIAL and MAJOR items above will bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL issues

P3-E8 (Sec. IV.B p.14): Pearson p-value inconsistent with quoted r and sample size
Quoted text: “no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21).”
Problem: With N = 24,049 occupied pixels, r = 0.006 gives t ≈ r√[(N−2)/(1−r²)] ≈ 0.93, implying a two-sided p ≈ 0.35, not 0.21. The reported p-value is inconsistent with the stated r and N.
Required fix: Recompute p with the exact N and method (Pearson, two-sided). If weights or a different effective N were used, state them explicitly and report the correct p-value.

MAJOR issues

P3-M7 (Sec. III.F p.11; Table VI footnote p.23): Planck top-200 train/validation composition — “mild” over-representation is statistically strong
Quoted text: “152 of the 200 in the training split and 48 in the 15% validation split, versus ≈170/30 expected ... the anomaly tail mildly over-represents held-out patches.”
Problem: Under the stated 85/15 split, the number of training patches among 200 is Binomial(n=200,p=0.85). P(X ≤ 152) is ≈1.8×10−4 (≈3.6σ), i.e., a statistically strong over-representation of validation patches, not “mild.” This does not suggest memorization (it is in the opposite direction) but the significance should be reported accurately.
Required fix: Add the exact binomial/hypergeometric p-value for ≤152 training patches among the top-200 and revise the wording (e.g., “significant over-representation of held-out patches; direction opposite to memorization”).

P3-M8 (Abstract p.1; Table I p.7 caption; Sec. I p.2): “Largest multi-archive anomaly search” not substantiated
Quoted text: “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware … the total represents the largest multi-archive anomaly search reported to date.”
Problem: The manuscript benchmarks against a single-survey [11]. No citation or survey-of-surveys is provided to substantiate the multi-archive superlative.
Required fix: Either (a) add a brief literature scan (with citations) showing no larger multi-archive anomaly catalogs exist, or (b) soften to “to our knowledge” and remove the categorical “largest” claim in captions/abstract.

P3-M9 (Sec. III A p.6): “0% artifact rate in the top 200” lacks a reproducible QA protocol
Quoted text: “Spectral inspection of the top 200 confirms a 0% artifact rate … compared against 11 known sky and telluric features; zero were attributable...”
Problem: A zero-artifact claim needs a documented, reproducible QC procedure (criteria, feature list, reviewer count/blinding, inter-rater agreement, and example flags). As written, this is an unsupported assertion.
Required fix: Provide the artifact-QA protocol (feature list; how sky/telluric/cosmic rays were identified; who inspected; inter-rater consistency) and deposit the per-object QA flags. If that cannot be provided, soften the claim (e.g., “no artifacts were identified under our 11-feature checklist”) and avoid “0%.”

MINOR issues

P3-m6 (Fig. 8 caption p.16 vs. body Sec. III.C p.8–10): Transfer-axis caveat should be explicit on the panel that shows S = 49.5
Problem: While the caption notes that panel annotations are “display values,” the SDSS S = 49.5 is on the DESI-trained cross-transfer axis and not comparable to native SDSS scores. This is clear in the body but easy to miss in the figure.
Required fix: Add an explicit label on the SDSS panel with S = 49.5: “DESI-trained transfer score axis; not comparable to native SDSS scores.”

P3-m7 (Fig. 12 p.25): Taxonomy naming consistency
Problem: Caption says “cool/unusual-star family; panel label ‘Cool Dwarf.’”
Required fix: Use one taxonomy name consistently in caption and panel (e.g., “Cool dwarf” everywhere).

P3-m8 (Sec. IV.C p.15, RA-shift control): Summarize control variability
Problem: The text says the RA-shifted control mean is 2.75 but not its dispersion across the four shifts.
Required fix: Report the mean ± standard deviation over the ±0.5°, ±1.0° shifts to quantify the control’s spread.

P3-m9 (Sec. II.C p.4): Wall-clock accounting clarity
Problem: You state ≈42 h total with ≈9.4 h pure inference and ~32 h “dominated by I/O … and an ~11 h pod-restart.” This balances, but readers would benefit from a concise subtotal table (I/O, retrains, restart).
Required fix: Add a one-line breakdown (I/O staging, retrains, restart, misc) in Appendix/Computational details, or cite a table in the repo.

P3-m10 (Sec. IV.B p.14; Fig. 7 bottom-right): Units on distance from Galactic plane
Problem: The y-axis is “Anomaly score S” (dimensionless), but the x-axis “distance from the Galactic plane” should explicitly state degrees to match the text.
Required fix: Add “(deg)” to the x-axis label.

NITs

P3-n4 (Sec. III.F p.11): Typo “over -represents” (extra space before dash).
Required fix: Remove stray space.

P3-n5 (Sec. III.F p.11; Table VI footnote p.23): Consistent significant figures on Planck MSE range
Problem: The top-200 range is given as [0.558, 0.621] while the validation MSE is 0.4437; harmonize precision (either 3 or 4 decimals consistently) to improve readability.

Explanation
This fresh-eyes pass focused on arithmetic/p-values, caption/body alignment, dimensional checks, cross-reference fidelity, null comparability, and abstract faithfulness. Most core arithmetic checks were already covered in the initial review. The new issues above surfaced (i) a concrete p-value inconsistency in the spatial dust correlation, (ii) the statistical strength (not “mildness”) of the Planck train/validation composition deviation, (iii) an unsubstantiated superlative claim, and (iv) the need for a reproducible artifact-QA protocol behind the “0% artifact” statement, plus several smaller clarity/labeling fixes.