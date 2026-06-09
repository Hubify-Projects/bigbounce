# P5 auto-2026-06-08_2353pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 268.6s

---

# META-REVIEW — P5 Environmental Dependence of Spiral Chirality

The five prior reports converged on a strong rejection consensus centered on: (a) reliance on unpublished Paper IV, (b) future-dated/unverifiable references, (c) the 791,635 vs 812,793 sample mismatch, (d) abstract bloat, (e) 0/6 DESIVAST disagreement, and (f) the post-hoc primary/secondary declaration. Below are issues that none of them flagged.

---

## NEW ESSENTIAL findings

### P5-META-E1 — V2-REVOLVER / V2-VIDE void counts contradict themselves between p. 10 and p. 11
**Sections:** §VIII (p. 10) vs §VIII C (p. 11). **Why missed:** Reviewers focused on the headline DESIVAST result and did not cross-tabulate the void counts quoted at different points in the same section.

Page 10 explicitly states: *"1,461 interior voids with VoidFinder, **420 with V2-REVOLVER**, and **295 with V2-VIDE**."*

Page 11 (§VIII C) then states: *"V2-REVOLVER (n_void^catalog = **1,992** effective voids… and V2-VIDE (n_void^catalog = **1,478**, max 55.9 Mpc/h)."*

That is a factor-of-4.7× discrepancy for V2-REVOLVER and 5.0× for V2-VIDE, with no reconciliation. The two pages may be referring to "interior voids" vs "voids including edge zones" but this distinction is never made, and the same N_void quantity is used in the three-algorithm robustness argument that load-bears the headline.

**Required fix:** State the precise DESIVAST catalog quantity used (interior voids, total voids, effective voids including edge zones), reconcile the two values, and confirm which is used in Table VIII.

### P5-META-E2 — Pearson correlation NSIDE mismatch between body claim and supporting table
**Sections:** §VIII E (p. 12, NSIDE = **16**) vs §VIII F (p. 13, Pearson r = +0.006 at NSIDE = **32**). **Why missed:** The reviewers accepted the Pearson r as a single robustness statistic without checking it against the supporting stratification.

The **only** explicit per-pixel void/chirality stratification in the paper (Table IX, p. 12) is reported at NSIDE = 16. The single most-cited "tracks survey mask not environment" statistic — the Pearson r = +0.006, p = 0.88 — is computed at NSIDE = 32, where no corresponding stratification is shown. Worse, in §VIII F the authors note that the NSIDE = 64 cells fail at "n_pix^both < 3" — but with n = 3 a Pearson correlation has 1 degree of freedom and is essentially undefined. Reporting the NSIDE = 32, cut = 200 cell as the headline correlation when the more conservative cells in the 3×3 grid are undefined is a hidden cherry-pick.

**Required fix:** (i) Provide the per-pixel scatter plot at NSIDE = 32 (currently only the Mollweide map is shown); (ii) state the Pearson r at every cell of the NSIDE × cut grid that is defined, not only the 7 of 9 reported in prose; (iii) reconcile NSIDE choice between the stratification (16) and the correlation (32).

### P5-META-E3 — Bonferroni-5 applied to three explicitly correlated DESIVAST tests
**Section:** §V B "Multiplicity bookkeeping" (p. 5). **Why missed:** Reviewers accepted the multiplicity correction as conservative; none noticed the internal contradiction between the correlation acknowledgment and the Bonferroni assumption.

The abstract states the four DESIVAST re-projections are *"methodologically correlated by construction because they reuse the same matched-spiral subsample"*. §V B then applies *Bonferroni-5* at α = 0.05 (threshold |σ| ≈ 2.81) to the same five statistics. **Bonferroni assumes independence (or at worst is conservative for positively correlated tests with arbitrary dependence structure only if the union-bound applies — which itself requires α be small enough that the Šidák correction would converge).** When three statistics share an n = 56,981–102,911 galaxy parent subsample with overlapping void definitions, the effective number of independent tests is closer to 1.5–2, and the appropriate correction is anti-conservative (smaller threshold). The headline robustness claim *"all five return |σ_void| < 2"* therefore overstates the strength of the multi-algorithm cross-check.

**Required fix:** Either compute an empirical max-statistic null across the three DESIVAST algorithms holding the matched-spiral set fixed (this provides the correct correlation-aware threshold), or replace "Bonferroni-5" with the more accurate description "effectively a single sample with three correlated re-classifications".

### P5-META-E4 — Sign convention for Δf_CW inconsistent between abstract, Table VIII, and §VIII B
**Sections:** Abstract (p. 1), §VIII B (p. 11), Table VIII (p. 12). **Why missed:** Gemini caught a sign error in the abstract, but the inconsistency propagates further — the convention is not standardized.

Abstract: *"f_CW^void = 0.4964 vs f_CW^non-void = 0.4971, Δf_CW = 0.0007"* — implies Δf = non_void − void (positive convention).
Table VIII row 1 (VoidFinder): Δf_CW = **+0.0007**, consistent with non_void − void.
Table VIII row 2 (V2-REVOLVER): f_void = 0.4986 > f_non_void = 0.4967, Δf_CW = **−0.0019** — here Δf is **void − non_void** (opposite convention).
Table VIII row 3 (V2-VIDE): f_void = 0.4971, f_non_void = 0.4970, Δf_CW = **−0.0001** — again void − non_void.

The first row uses one sign convention; rows 2–3 use the opposite. This is internal arithmetic inconsistency, not just an abstract typo. It makes the headline "Δf_CW = 0.0007" of the wrong sign relative to two of three algorithms.

**Required fix:** Pick a single convention (recommend Δf = f_void − f_non_void), recompute all three rows of Table VIII consistently, and propagate the correction to the abstract and §VIII B.

### P5-META-E5 — The NS-excluded class is not tested for environment-conditional selection
**Section:** Table I (p. 3); never addressed. **Why missed:** All five reviewers treated "NS excluded" as a clean cut; none asked whether the NS rate is itself environment-correlated.

The chirality catalog labels 1,440,577 of the 2,232,212 matched-primary galaxies as **NS** (no spiral structure), i.e. 64.6% are excluded before any environmental analysis. If the NS fraction depends on environment — e.g., elliptical-dominated clusters → higher NS, or distant-void galaxies → lower S/N → higher NS — then the chirality-relevant subsample is non-randomly selected from each V-Web class. This would induce an environment-dependent selection bias **completely independent of any astrophysical chirality–environment coupling**, and the headline null would be testing the wrong hypothesis.

**Required fix:** Report NS fraction by V-Web class (a single 4-row table) and demonstrate that the NS rate does not vary by more than ~1 pp across {void, wall, filament, cluster}. If it does vary, the conclusion must be re-stated as "no chirality dependence conditional on the environment-dependent NS selection."

---

## NEW MAJOR findings

### P5-META-M1 — "Exact binomial" methods description contradicts "Jeffreys" figure captions
**Sections:** §V (p. 4) vs Fig. 2 caption (p. 5), Fig. 3 caption (p. 7), Fig. 7 caption (p. 15). **Why missed:** Reviewers checked σ arithmetic but not which interval estimator was applied to fCW.

§V states: *"we report observed CW fraction, **exact binomial 95% credible interval**"*. The exact binomial (Clopper–Pearson) interval is a frequentist confidence interval, not a credible interval. Every figure caption then states *"95% **Jeffreys** binomial credible intervals"* — Jeffreys is a Bayesian credible interval using a Beta(½,½) prior. These are different procedures that give numerically different intervals, especially at the void bin n = 428. The paper conflates them throughout.

**Required fix:** State exactly which interval is shown in figures and used in tables. If Jeffreys, remove "exact binomial" from §V; if Clopper–Pearson, change figure captions.

### P5-META-M2 — k = 5 NN angular density quintiles are not redshift-corrected
**Section:** §VI C (p. 6) and Fig. 3 (p. 7). **Why missed:** Reviewers accepted "projected k = 5 NN density" as a density proxy without questioning its z-dependence.

The k = 5 NN **angular** separation maps to wildly different physical separations across the matched-sample redshift range 0.01 ≤ z ≤ 3.83. At z = 0.05 the angular density proxy probes ~1 Mpc scales; at z = 0.5 it probes ~25 Mpc scales. The density quintiles therefore mix low-z small-scale neighborhoods with high-z large-scale neighborhoods. The §VI B logistic regression on z is reported separately, but the density quintile test is contaminated by exactly the z-correlation that test was designed to break out. The "no quintile deviates from the prediction by more than ~2σ" in Fig. 3 is therefore not a clean density test.

**Required fix:** Recompute density quintiles using either (i) physical-distance NN in comoving Mpc/h (requires spec-z), or (ii) a z-conditioned percentile cut within thin redshift slices. The current statistic is uninterpretable.

### P5-META-M3 — Volume-fraction vs galaxy-count weighting confusion
**Section:** §IV B and Fig. 1 (p. 4) vs Table II (p. 5). **Why missed:** Reviewers accepted both as descriptive statistics without noting the disjoint weighting.

Fig. 1 reports in-footprint **volume fractions**: {void 24.4%, wall 41.3%, filament 33.3%, cluster 1.0%}.
Table II reports matched-spiral **count fractions**: {void 0.05%, wall 0.82%, filament 50.2%, cluster 48.9%}.

The cluster volume fraction is 1.0% but contains 48.9% of all matched spirals; the void volume is 24.4% but contains 0.05%. This 1000× density contrast is the cosmic-web bias and is normal, but the paper never states the galaxy-density-weighted volume fractions or the implied per-class mean density. Without that, the reader cannot judge whether the cluster signal is concentrated in a few dense cells (potentially survey-mask artifact) or distributed across the full cluster class.

**Required fix:** Add a "galaxies per cell" column to the volume-fraction table; if the cluster class has fewer than ~100 cells carrying ≥ 100 chirality-relevant spirals, the n = 397,505 cluster bin is statistically equivalent to a handful of high-density regions and the cluster σ deviation requires per-cell reporting.

### P5-META-M4 — "Interior voids" / "effective voids" / "maximal voids" / "hole spheres" used interchangeably
**Sections:** §VIII A (p. 10), §VIII C (p. 11), §VIII E (p. 12). **Why missed:** Reviewers focused on the chirality null, not the underlying void taxonomy.

The paper variously cites: "**1,461 interior voids** with VoidFinder", "**101,863 interior hole spheres** comprising the 3,765 maximal voids", "**1,992 effective voids** for V2-REVOLVER", and "**3,765 maximal voids** with explicit RA/Dec/Reff". These are four distinct DESIVAST data products with different definitions and different sky/volume coverage. The point-in-sphere test uses 101,863 hole spheres; the HEALPix stratification uses 3,765 maximal voids; the algorithm comparison uses different "effective void" counts. The reader cannot reconstruct what was tested against what.

**Required fix:** A single methods table mapping each DESIVAST analysis to the exact catalog quantity used.

### P5-META-M5 — σ_pred sign convention switches between Eq. (1) and §VII A
**Sections:** Eq. (1) p. 4 vs §VII A p. 9. **Why missed:** Claude flagged the σ_pred arithmetic but not the sign convention switch.

Eq. (1): σ_pred = 2·Δf_CW·√N, with Δf_CW = −0.0026, giving **negative** σ_pred.
§VII A explicitly: *"σ_pred^class = 2 · **0.0026** · √n_class"* — written with **positive** 0.0026, then quoted as values 0.10σ through 3.32σ (positive).

So Eq. (1)'s σ_pred is signed; §VII A's σ_pred^class is absolute-valued. The §VIII F monopole-residual table then computes |σ_obs − σ_pred| — but σ_obs is signed (−0.56 to +1.01). If σ_pred is taken as positive 3.27 but σ_obs is negative −4.66, the residual is **−7.93**, not the +1.11 that Table X reports. The convention is being silently flipped depending on context.

**Required fix:** Use one signed convention throughout; if absolute-value comparison is intended, write |σ_obs| − |σ_pred|, not σ_obs − σ_pred.

### P5-META-M6 — TARGETID join chain for GALZONE membership is not validated
**Section:** §VIII D (p. 11). **Why missed:** Reviewers focused on the result, not the join methodology.

The chirality catalog comes from DESI Legacy DR8 Tractor positions. It is then SkyCoord-matched to DR1 zall (which yields a DESI TARGETID for each match). The §VIII D analysis then joins GALZONE on TARGETID = desi_targetid. The Tractor → zall match is positional (1″ tolerance), but the zall → GALZONE match is by TARGETID. If a chirality catalog object positionally matches the wrong DESI target (e.g., a confused near-neighbor at < 1″), the GALZONE void assignment is for a different galaxy than the one chirality-labeled. With 791,635 matched spirals at p99 separation 0.30″, this is plausibly a sub-percent effect but is never quantified. The headline DESIVAST σ = −0.24 result depends on this join.

**Required fix:** Quantify the rate of cases where the SkyCoord-matched TARGETID's GALZONE assignment disagrees with the spatial point-in-sphere test against the published void centers/Reff. If > 1%, the catalog-native cross-check is contaminated.

### P5-META-M7 — r ≤ 17.8 selection makes the DESIVAST void sample volume-incomplete at z ≈ 0.24
**Section:** §XIII Limitations (p. 17), but not propagated. **Why missed:** Reviewers noted the selection cut but not its specific impact on the void sample.

At z = 0.24 the DESI Legacy r ≤ 17.8 chirality-catalog cut corresponds to M_r ≲ −22.0, i.e. only the most luminous spirals. The DESIVAST BGS sample is volume-limited to z = 0.24 at M_r ≈ −20 to −21. The chirality-relevant void sample (n = 56,981) is therefore a luminosity-biased subset of the DESIVAST void population: void galaxies in DESIVAST are systematically less luminous, but the chirality-labeled void galaxies are systematically more luminous, so they may not be representative of "the population of void galaxies." Any chirality–environment coupling that operates preferentially on faint void galaxies would be undetectable by construction.

**Required fix:** Report the absolute-magnitude distribution of the n = 56,981 void spirals vs the n = 621,964 non-void spirals; if the void sample is M_r-shifted by ≳ 0.5 mag relative to non-void, the comparison is luminosity-confounded and the headline ∆f_CW = 0.0007 null is conditional on the luminosity bias.

---

## NEW MINOR findings

### P5-META-m1 — Pearson r at n < 3 is "undefined", not "sample-limited"
**Section:** §VIII F (p. 13). The paper says NSIDE = 64 cells with cuts 200 and 500 are "sample-limited at n_pix^both < 3". A Pearson correlation with n = 2 has zero degrees of freedom and is not just sample-limited — it is mathematically undefined (or trivially r = ±1). Rephrase.

### P5-META-m2 — "Mean +0.020, std 1.184, skewness +0.044, excess kurtosis +0.825" pixel statistics (§VIII F)
**Section:** §VIII F (p. 13). Excess kurtosis +0.825 is **not** consistent with a Gaussian shot-noise null (which would have excess kurtosis 0). The paper claims this is "consistent with a pure shot-noise residual" — false. Excess kurtosis 0.8 is a tail-heavy distribution. The statement should be qualified or the kurtosis result should be tested against the null distribution.

### P5-META-m3 — Inconsistent void radius range
**Section:** §VIII E (p. 12) gives DESIVAST maximal void Reff = 10–32 Mpc/h, but the VoidFinder hole-sphere acceptance radius implied by the 28.7–158.1 Mpc/h spiral-to-nearest-hole quote in §VIII A implies smaller hole radii. The "24 Mpc/h maximum hole radius" quoted in §VIII B doesn't match either. Reconcile.

---

## NEW NIT findings

### P5-META-N1 — Paper title uses "V-Web" for what footnote (a) acknowledges is T-Web
The title is *"…with V-Web Cross-Check…"* but footnote a admits the classifier is the Hahn 2007 T-Web (tidal-tensor), not the Hoffman 2012 V-Web (velocity-shear). PRD readers searching for V-Web cosmology results may be misled. Rename to "T-Web" in the title.

---

## Meta-review recommendation

**REJECT**

Combined across all six reviews, the active blocker list is: (1) Paper IV is unpublished and load-bears every chirality label (Claude E1, Gemini E1, Grok M-implicit, Perplexity E1, E4); (2) two future-dated arXiv refs are unverifiable (Claude E2, Gemini E2, Grok E4); (3) the headline 791,635 sample does not match Table II's 812,793 (Claude E12); (4) the filament bright+dark sum (437,904) exceeds the total filament class (408,187) by ~30k (Claude E13); (5) the abstract Δf_CW sign and the Table VIII sign convention are internally inconsistent (Gemini E3 + this report META-E4); (6) the V2-REVOLVER/V2-VIDE void counts differ by 5× between two pages of §VIII (META-E1); (7) the Pearson NSIDE cherry-pick (META-E2); (8) the Bonferroni-5 multiplicity correction applied to correlated tests (META-E3); (9) the NS selection function is environment-conditional and untested (META-E5); (10) the 3.4σ bright-vs-dark sign-flip is real and unexplained (Claude E8, Gemini N2); (11) the post-hoc primary/secondary designation (Grok M1, Perplexity); (12) RSD treatment is hand-waved (Claude M9, Grok). That is twelve independent showstoppers spanning data provenance, arithmetic consistency, statistical methodology, and astrophysical interpretation. My confidence that this paper would survive non-bigbounce external peer review at PRD is **below 5%** — the unpublished-Paper-IV dependency alone is a hard rejection at any reputable journal, and the arithmetic inconsistencies surfaced here and in Claude's review would force major revisions even if Paper IV were public. A substantially shorter (8–10 page) paper anchored exclusively on the DESIVAST result, contingent on Paper IV's prior publication, with all sign conventions and join chains verified, could be reconsidered; the present manuscript cannot.