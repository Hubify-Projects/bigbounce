# P1B v1B.0.107 exact-PDF confirmation truth audit

## Target and routing

- Science closure: `29ccead9`
- Review-routing isolation: `902cb712`
- PDF SHA-256: `c7156aa29f381c5d891f5594ac7e0fcaa478dfff30b8f6806ea45055265866c5`
- PDF length: 19 pages
- OpenAI-family leg: Codex CLI authenticated by ChatGPT subscription, `gpt-5.6-sol` high, read-only
- Direct-provider legs: xAI/Grok 4.3 and Google/Gemini 3.1 Pro Preview, with sanitized receipts
- Anthropic: not used

This was the single anti-loop confirmation wave. No further verdict loop is authorized for this closure cycle.

## Board

| Reviewer | Verdict | Disposition |
|---|---|---|
| Grok | ACCEPT | Central claims supported; optional/stale minors |
| Gemini | MAJOR REVISIONS | Mostly venue/editorial opinion; one real minor and release gates |
| Codex subscription | MAJOR REVISIONS | Two real technical majors and three real provenance minors |

## Adjudication

### Codex

1. **REAL / MAJOR — canonical mask coordinates.** `namaster_500mc.py` calls `hp.pix2ang(..., lonlat=True)` twice without a coordinate rotation and uses the same native latitude array as both Galactic latitude and equatorial declination. The resulting binary mask is a synthetic native-coordinate latitude window (`f_sky=0.32260`, analytic `0.32244`), not the stated ACT-like Galactic-plus-equatorial footprint. Because the simulated sky is isotropic, the retained recovery remains a valid synthetic pipeline check; it must be relabeled, not interpreted as survey geometry.
2. **REAL / MAJOR — prior-predictive method absent from rendered text.** The active abstract quotes 11.6% and 6.1%, while the detailed `N`, seed, priors, estimator, and uncertainty are only inside a LaTeX `comment` environment. Minimal active documentation must state `N=100,000` per configuration, seed 1234, the exact priors, nonlinear-EOM estimator, signed-band counting rule, and binomial MC standard errors (0.101 and 0.076 percentage points for fixed and broad coupling).
3. **REAL / MINOR — Git LFS provenance scope.** The outer manifest hashes 133-byte pointer files for frozen cosmology chains, not the scientific payload bytes. Nested records preserve LFS payload OIDs and sizes. Manuscript and manifest language must distinguish pointer verification from payload verification and identify the external payload mirror.
4. **REAL / MINOR — ESS provenance ambiguity.** `convergence_latest.csv` uses a different effective-sample convention and reports values of order 300,000, whereas Table II reports integrated-autocorrelation ESS near 4,700. One authoritative estimator/artifact and the limiting parameter must be named explicitly.
5. **REAL / MINOR — missing changelog record.** The manuscript promises a v1B.0.107 entry and payload links that are not present in `CHANGELOG.md`.

### Gemini

- Standalone theme: **OPINION / venue judgment**. It does not falsify a claim.
- Section order: **PARTLY REAL / editorial**. Readability can be improved later; it is not a scientific blocker.
- `Omega_a<0.01` threshold: **OPINION / already sensitivity-tested**. Table V reports both 0.1 and 0.01 selections and the manuscript explains the conservative spectator criterion.
- Naive 3.9-sigma combination: **REAL / MINOR**. It combines different dataset summaries and is immediately disclaimed; removal reduces misquotation risk without changing any result.
- Placeholders/future reference: **PARTLY REAL / release gate**. Concurrent-paper placeholders must be filled at coordinated submission. `arXiv:2509.13654` is a real cited preprint, not synthetic.
- Covariance prominence: **STALE**. The diagonal-covariance limitation is already stated in the main text and footnote.

### Grok

The disclaimer-repetition and full-EB follow-up suggestions are optional editorial/future-work points. The diagonal-SNR clarification is already active. Grok's ACCEPT cannot override the reproduced coordinate/provenance defects.

## Scientific disposition

The stock-CAMB null posterior, exact-window numerical recovery, and ODE-derived ALP subset remain supported. The confirmation majors are bounded documentation/geometry-scope failures: no new Monte Carlo or MCMC run is required if the mask is accurately described as synthetic. P1B remains at readiness 56 and is not accepted.

## One-pass closure

1. Relabel the canonical mask in code and manuscript as a synthetic native-coordinate latitude window; remove ACT/Galactic-plus-equatorial claims.
2. Add the complete prior-predictive method and binomial uncertainties to rendered text.
3. Separate LFS pointer SHA verification from payload OID/size verification and identify mirrors.
4. Cite an authoritative integrated-autocorrelation ESS artifact, estimator, and slowest parameter.
5. Add the versioned pre-release changelog record and payload links.
6. Remove the mismatched naive 3.9-sigma combination.
7. Version, compile, all-page audit, synchronize bounded status, and stop; do not launch another review wave.
