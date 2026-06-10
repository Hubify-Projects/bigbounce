# P3 R23conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 452.8s

---

META-REVIEW — new issues not caught by any of the 5 prior reports

P3-META-E1
- Severity: ESSENTIAL
- Section + page: §V.b (p.12), §VI D(i) (p.15)
- Why missed: Prior reviews focused on F0’s typo and the %-improvement arithmetic, not on estimator bias from squaring α.
- Problem: The “Fisher-positivity-respecting” mapping 1/σ²(fNL) = F0 + c·α² is applied to a noisy estimate αjk = 0.19 ± 0.65 without correcting for the noise bias inherent in squaring a Gaussian-distributed quantity. Because E[α̂²] = α² + Var(α̂), the central forecast σ(fNL) computed from α̂² is upward-biased (i.e., over-optimistic improvement) unless one uses a de-biased estimator (α̂² − Var(α̂)). Quote: “Under the Fisher-positivity-respecting asymptotic form … inserting αjk = 0.19 gives a central forecast σ(fNL)=8.14…”
- Required fix: Recompute the central forecast using a de-biased amplitude, e.g., use max(0, α̂² − σ²_α) in place of α̂², or adopt a hierarchical/shrinkage treatment for α in the Fisher mapping. Report both the de-biased central value and the propagated envelope. State explicitly that the convex α² mapping otherwise introduces a noise bias in the improvement.

P3-META-M1
- Severity: MAJOR
- Section + page: §II D Step 6 and §IV C (p.4, p.11)
- Why missed: Reviewers checked the radius sweep but not the graph-theory implications of the union-find dedup.
- Problem: Dedup uses friends-of-friends (FoF) at 5″, which can merge sources with separations >5″ via transitive chains (A within 5″ of B, B within 5″ of C, but A–C ≈ 9″). Quote: “merged via union-find friends-of-friends to produce the unique-object headline.” No check is shown on maximum intra-cluster separation or on “chain bridging” in crowded fields.
- Required fix: Audit all multi-survey clusters for max pairwise separation; break clusters exceeding the stated match radius; re-report the unique-object count and the cluster histogram. Alternatively, cap the link length by enforcing single-link matches (no FoF chaining) and compare results. Provide both numbers to bound potential over-merging.

P3-META-M2
- Severity: MAJOR
- Section + page: §IV B (p.10–11)
- Why missed: Prior critiques focused on mask/dof and low-count χ², not on the rate denominator.
- Problem: The “anomaly rate shows no correlation with Galactic latitude” result does not specify the denominator used to form a rate per pixel. If “rate” is anomalies per pixel (not normalized by the number of scanned sources or survey depth per pixel), the statistic is not interpretable and can be dominated by footprint completeness. Quote: “the anomaly rate shows no correlation with Galactic latitude (Spearman r = 0.0005…).”
- Required fix: Define the rate explicitly as anomalies / scanned-sources per pixel (or per-survey-weighted exposure). Provide or cite the per-survey coverage/target-density maps used for normalization and repeat the correlation tests with proper denominators.

P3-META-M3
- Severity: MAJOR
- Section + page: §IV A (p.10)
- Why missed: Others challenged the pooled-vs-per-survey radii and independence, not the sky-density model.
- Problem: The SIMBAD 5″ false-match estimate assumes a uniform sky density nSIMBAD ≈ 3.0×10⁻⁵ arcsec⁻². This underestimates spurious matches in high-density regions (e.g., Galactic plane, Magellanic Clouds). Quote: “Pfalse ≈ 2.4×10⁻³ per source … negligible compared to the 99% unmatched rate.”
- Required fix: Replace the global uniform estimate with (a) a local-density Monte Carlo (scramble positions within annuli) or (b) a HEALPix-weighted density map to compute Pfalse per object. Report the distribution (median, IQR) of Pfalse and the implied expected total false matches with uncertainty.

P3-META-M4
- Severity: MAJOR
- Section + page: §III C and Table I footnote ♡ (p.6–9)
- Why missed: Reviewers asked for clearer tabulation, but not a robustness test against post-hoc slicing.
- Problem: The SDSS “4.05% continuity slice” at S ≥ 0.1060 is explicitly chosen post-hoc to match the cross-transfer count (77,905) and is then used in the 7-way dedup geometry. Quote: “sized to equal the cross-transfer count … preserved as the continuity slice.” This selection could inflate overlap and dedup-compression in ways that differ from a principled top-1% cut.
- Required fix: Re-run the 7-way dedup with the SDSS native top-1% (19,253) and with S>5 (12) and report (i) the unique-object count, (ii) multi-survey cluster count, and (iii) compression. Show that headline conclusions are robust to the SDSS threshold choice, or qualify any dependence.

P3-META-M5
- Severity: MAJOR
- Section + page: §II B (p.2–3), §III B (p.5)
- Why missed: Prior reviews did not probe the missing mathematical definition here.
- Problem: The per-arm residuals rB, rR, rZ are used repeatedly (e.g., for high-z selection, arm dominance, taxonomy) but are never defined mathematically. Quote: “we additionally decompose the score into per-band contributions rB, rR, rZ … example reconstructions per band are in the companion data repository.”
- Required fix: Provide explicit formulas for rB, rR, rZ (e.g., arm-restricted MSE normalized by the arm-specific μval, σval, or some common scale). State whether these are z-scored independently per arm and whether arm-to-arm σ differences are accounted for.

P3-META-m1
- Severity: MINOR
- Section + page: §II B.b (p.3), §VI D(i) (p.15)
- Why missed: Others cited cross-refs and masks; this is a small but real internal inconsistency.
- Problem: OOD-set size appears as “100k unseen DESI spectra” in §II B.b, but “an independent 103,000-spectrum OOD holdout” in §VI D(i).
- Required fix: Use a single, exact OOD sample size consistently and ensure the repository includes the OOD list with checksum.

P3-META-M6
- Severity: MAJOR
- Section + page: §III F and Table V footnote † (p.7–8, p.18)
- Why missed: Prior reviews flagged 20k vs 200k patches and timing; not whether scoring respected the training mask.
- Problem: The native Planck CAE is trained on |b| ≥ 20° masked patches, but it is unclear whether the 20,000 scored catalog patches are drawn under the same mask. Quote: “trained on 2×10⁵ galactic-plane-masked (|b| ≥ 20°) SMICA patches” vs “Input: 20,000 SMICA CMB map patches … Anomaly count: 200 (top 1%).”
- Required fix: State explicitly whether the 20,000 scored patches also exclude |b| < 20°. If not, justify domain transfer (masked→unmasked) and report performance differences or restrict the scored set to the training domain for consistency.

P3-META-m2
- Severity: MINOR
- Section + page: Fig. 3 left caption and axes (p.6)
- Why missed: Reviewers noted “twelve orders of magnitude,” not the normalization implied by “probability density.”
- Problem: The y-axis is labeled “Probability density” for overlaid DESI and LAMOST score distributions, but the normalization scheme (per-sample kernel density vs. histogram normalized to unit area) is not stated; with different N per survey this can mislead comparative reading.
- Required fix: Specify the normalization (e.g., KDE with bandwidth X; histograms normalized to unit area), or relabel to “normalized density” and add a sentence clarifying comparability across samples of unequal size.

P3-META-M7
- Severity: MAJOR
- Section + page: §IV C (p.11), Fig. 8 (p.13)
- Why missed: Prior review flagged sub-threshold scores in the gallery but not the denominator problem for the “expected 2.3 coincidences.”
- Problem: The text compares an “expected random coincidence count ∼2.3” at 3″ with “the 3 observed matches,” but never defines the sample area, the total number of DESI and SDSS anomalies actually cross-matched at 3″, or their surface densities. Quote: “For the DESI×SDSS cross-match at 3″, the expected random coincidence count is ∼2.3, comparable to the 3 observed matches…”
- Required fix: Provide the full denominator (catalog sizes and overlap area used for this pairwise 3″ exercise) or drop the comparison. If these are merely the three gallery objects, say so and remove any suggestion of a statistical test.

P3-META-m3
- Severity: MINOR
- Section + page: §III E (p.6–7)
- Why missed: Others commented on IF overlap, not exposure variation.
- Problem: The eROSITA top anomalies cluster near the LMC, attributed to scan strategy depth, but no exposure- or detection-significance normalization is applied in the anomaly scoring for photometric features. Depth variations can alter feature distributions and hence BigAE residuals.
- Required fix: Add a control showing the eROSITA anomaly fraction as a function of local exposure/depth or include depth as an input feature (and state this). Otherwise, qualify the LMC concentration as potentially depth-driven instrumentally.

P3-META-m4
- Severity: MINOR
- Section + page: Preprint-wide (Abstract p.1 vs §II D and §IV A, p.4, p.10)
- Why missed: One reviewer asked to clarify whether the ~265k subset includes Planck; none flagged the deeper guidance conflict.
- Problem: The paper advises “Downstream object-level analyses … should use the 378,080 point-source tier,” yet the “recommended catalog-grade subset” (~265k) is said to include the 200 Planck map patches (not point sources). This is inconsistent guidance for end-users.
- Required fix: Define two recommended subsets explicitly: (i) catalog-grade point-source subset (exclude Planck), and (ii) full catalog-grade including map patches; give exact counts for both and ensure the abstract and §Data availability use the same definitions.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential/major blockers: numerical/notation fixes in the fNL forecast, Planck patch-count/timing consistency, SIMBAD radius consistency, table redesign for clarity of thresholds, data/code availability with DOIs, plus the new items above (α² noise-bias in the Fisher mapping; FoF transitive-chaining in dedup; missing rate denominator in spatial tests; uniform-density false-match estimate; post-hoc SDSS slice robustness; missing rB/rR/rZ definition; and several smaller consistency fixes). My confidence that the paper can pass external peer review after a focused major-revision round is moderate-to-high, provided the authors (i) correct the cosmology-forecast mapping with a de-biased α estimator, (ii) tighten the catalog construction/dedup logic with the proposed audits, and (iii) make the reproducibility package public and self-consistent.