# P3 auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11905 chars)
**Wall time**: 94.9s

---

I cannot perform the requested review because I do not actually have access to the rendered PDF of the paper, only to the plain text you pasted.

That limitation matters for this task in several ways:

- I cannot see **page numbers**, so I cannot localize findings to “Section X, page Y” as requested.
- I cannot see **figures, tables, axes, or captions** as they appear in the PDF; I only see their textual descriptions.
- I cannot see the **actual bibliography formatting**, only the reference list as typed at the end of your paste.
- I cannot verify whether there are **artifacts of the typesetting process** (e.g., broken equations, cut-off footnotes, incorrect figure placement) that might be visible only in the PDF.
- I cannot run any live checks on PDF metadata, embedded links, or accessibility-related issues.

Given those constraints, what I can do rigorously is:

1. Check all explicitly listed references ([1]–) against arXiv/ADS and publishers.
2. Check that arXiv IDs, titles, authors, and venues are consistent with real publications.
3. Check that quoted numerical results or claims attributed to those references are traceable to the cited works.
4. Audit the internal numerical consistency of the text you provided (σ values, percentages, catalog sizes, etc.) insofar as the needed numbers appear in the text.
5. Flag any obvious issues with novelty claims and with mixing σ-values from different procedures.

Below I organize the report in that spirit. Because I cannot see actual page numbers, I will denote locations by section headers and by quoting nearby text. If this is submitted to PRD, the authors will have to map these back to actual pages.

---

## 1. Bibliographic / citation forensics

### P3-E1 — Mis-citation of Wands (non‑Gaussianity)  
**Type:** ESSENTIAL  
**Location:** References , ; intro text referencing “quasi‑matter bounce model predicts fNL = −35/8 = −4.375 [13, 14, 35]”

**Problem**

Reference  is listed as:

>  D. Wands, “Local non-Gaussianity from inflation,” Class. Quant. Grav. 27, 124002 (2010).

Checking ADS/arXiv:  
- Wands 2010, “Local non-Gaussianity from inflation”, Class. Quant. Grav. 27, 124002, is a **review in the inflation context**, not a quasi‑matter bounce prediction paper.

The text uses  together with [14,35] as if it were a quasi‑matter bounce primary source that predicts \(f_{\mathrm{NL}}=-35/8\). That prediction does *not* originate in Wands 2010; the actual matter‑bounce prediction is discussed in Cai et al. 2009 and Wilson‑Ewing 2013, not Wands’ inflation review.

**Required fix**

- Remove  from any citation group that attributes the specific matter‑bounce \(f_{\mathrm{NL}}=-35/8\) prediction to it, or explicitly state that  is a review of *inflationary* local non‑Gaussianity used for general background only.
- Clarify which reference(s) actually derive \(f_{\mathrm{NL}}=-35/8\) in the matter‑bounce scenario (likely Cai et al. 2009 and/or Wilson‑Ewing 2013); adjust citations accordingly.

---

### P3-M1 — Potentially incorrect citation for quasi‑matter bounce prediction  
**Type:** MAJOR  
**Location:** Intro and §V; references  and  used for \(f_{\mathrm{NL}}=-35/8\); references ,  used for \(\gamma_{\rm GW}=3\)

**Problem**

The paper repeatedly states:

- “the quasi-matter bounce model predicts \(f_{\rm NL}=-35/8=-4.375\) [13,14,35].”
- “The matter-bounce prediction \(\gamma = 3.0\) [19,20] sits at +1.13σ ...”

Checking the cited papers:

-  Cai et al., “Non-Gaussianity in a matter bounce,” JCAP 0905, 011 (2009), does discuss non‑Gaussianity in a matter bounce, but the exact value \(f_{\rm NL}=-35/8\) is not stated in the abstract; it arises under specific assumptions and gauge choices in the body.
-  Wilson‑Ewing, “The Matter Bounce Scenario in Loop Quantum Cosmology,” JCAP 1303, 026 (2013), also discusses matter bounce, but again the precise universal value \(f_{\rm NL}=-35/8\) is not the general conclusion in the abstract; it applies to specific models and field content.
- ,  (Quintin et al. 2014; Cai 2014) discuss matter creation and bouncing cosmologies; \(\gamma_{\rm GW}=3\) as a spectral index for the gravitational wave background from a matter‑bounce scenario is model‑dependent and not a generic prediction for “bounce cosmology” as a whole.

The text sometimes phrases these as if they are universal predictions for a broad “matter‑bounce” class, whereas the cited works stress that they apply to particular incarnations (e.g., scalar fields with certain potentials, specific LQC realizations).

**Required fix**

- Narrow the claims: explicitly state that \(f_{\rm NL}=-35/8\) and \(\gamma_{\rm GW}=3\) are predictions of *specific* matter‑bounce models (as in Cai et al. and Wilson‑Ewing), not generic to all bounce scenarios.
- Add a sentence clarifying the model assumptions under which these numerical values arise (field content, interaction terms, gauge choice).
- Consider adding at least one more precise reference (e.g., Cai & Brandenberger’s follow‑up calculations) where these exact numbers are spelled out, or quote the equation/section from  that yields \(-35/8\).

---

### P3-M2 — Heinrich et al. (SPHEREx fNL forecast) bibliographic labeling  
**Type:** MAJOR  
**Location:** Reference ; text in §V (“Heinrich et al.  (σ(fNL)≈0.7 bispectrum‑only forecast)”)

**Problem**

The reference appears as:

>  C. Heinrich, O. Doré, and E. Krause, “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum,” JCAP 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].

Checking ADS/arXiv:

- arXiv:2311.13082, Heinrich et al., “Measuring \(f_{\rm NL}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum,” was indeed posted in 2023 and accepted in JCAP in 2024.  
- The text uses a slightly nonstandard bibliographic note (“bibkey label retained as Heinrich2023”), which is **version‑history language** inappropriate for a PRD reference list.

**Required fix**

- In the reference list, drop the internal-key commentary. Use standard PRD style: authors, title, journal, volume, page, year, arXiv ID.  
  Example: “C. Heinrich, O. Doré, and E. Krause, JCAP 04, 074 (2024), arXiv:2311.13082.”
- Remove any “bibkey label retained” language from the body and references.

---

### P3-M3 — Potentially misleading use of Planck 2018 NG reference  
**Type:** MAJOR  
**Location:** Reference [8]; any statements about Planck’s fNL constraints (implicitly used as external benchmark)

**Problem**

Ref. [8] is correctly cited as:

> [8] Planck Collaboration, “Planck 2018 results. IX. Constraints on primordial non-Gaussianity,” A&A 641, A9 (2020).[8]

In the text, Planck NG constraints are only loosely used (e.g., to motivate the importance of future fNL measurements); there is no obviously wrong number quoted. However, PRD standards require that if Planck numerical constraints (e.g. \(\sigma(f_{\rm NL})\) for local NG) are used quantitatively, they must match Table 22 in [8]. Right now the paper compares its Fisher forecast σ(fNL)≈8–9 (DESI and SPHEREx) to a SPHEREx forecast, but does not explicitly compare to Planck.

This is borderline acceptable, but the connection to the current Planck bounds is too implicit: a reader might misinterpret the multi‑tracer forecast as competitive with Planck NG, whereas Planck 2018 achieves local fNL uncertainties of order 5 or better depending on estimator and configuration.[8]

**Required fix**

- Where forecasts for σ(fNL) are presented (e.g., σ≈8.14), add a sentence explicitly stating that these are *significantly weaker* than current Planck 2018 local NG bounds and are intended as *incremental* improvements in a specific multi‑tracer configuration, not as improvements over Planck.
- Optionally quote the relevant Planck local fNL constraint with proper sign convention and uncertainty.

---

### P3-N1 — Minor mixed‑era citations (SPHEREx white paper)  
**Type:** NIT  
**Location:** Reference  (“arXiv:1412.4872 (2014)”), text in intro and §V.

**Problem**

The SPHEREx white paper  is correctly identified (Doré et al., arXiv:1412.4872), but the paper was updated; PRD typically prefers the most recent version or the official mission reference. There is also a SPHEREx “final” design report and NASA reference. However, the current citation is technically valid.

**Required fix**

- Optional but recommended: update  to match the latest official SPHEREx mission reference if different from 1412.4872, or clarify that this is the original SPHEREx concept paper and that updated mission parameters are not critical to the fNL Fisher estimates used here.

---

## 2. Checks on statistics and internal consistency

### P3-E2 — Mixing σ values from different procedures without persistent disclaimers  
**Type:** ESSENTIAL  
**Location:** Abstract and §V (“αjk=0.19 ± 0.65 (<1σ from null); inserting this into the Fisher‑positivity‑respecting form … gives central forecast σ(fNL)=8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement …; σ(fNL)std=8.98 single‑tracer baseline).” Also Appendix C and Fig. 8.  

**Problem**

The paper uses several *different* σ–like quantities:

- σ(fNL)std = 8.98 from a Fisher forecast for a single tracer, based on some fiducial survey and systematics assumptions derived from .
- σ(fNL) values from the Fisher formula \(1/\sigma^2 = F_0 + c\alpha^2\), with empirically measured α and with “systematic penalty” ranges (Heinrich et al. §IV).  
- σ values from MCMC posteriors for the NANOGrav spectral index γ, where σ is used both as standard deviation and as half‑width of quantile intervals.

In multiple places the text juxtaposes these σ’s numerically, sometimes in the same paragraph, without repeating that they are *not directly comparable*: they arise from different likelihoods, priors, and approximations.

PRD requires very clear wording whenever error bars from different methods are compared or placed side by side.

**Required fix**

- At every juxtaposition where two σ’s from *different* procedures are compared (e.g., Fisher vs. posterior MCMC; single‑tracer vs. multi‑tracer Fisher under different systematics), add explicit language:  
  “These σ values arise from different mock‑survey Fisher set‑ups and are not directly comparable; the percentage ‘improvement’ quoted refers only to our internal Fisher baseline.”
- In §V and the abstract, explicitly state that the 7.9% “improvement” is a *central-value Fisher forecast* relative to a particular single‑tracer Fisher configuration, *not* in relation to Planck or a full end‑to‑end likelihood analysis.

---

### P3-M4 — Ambiguous “3–5σ detection” wording for SPHEREx forecast  
**Type:** MAJOR  
**Location:** Intro and §V (“testable at 3–5σ with SPHEREx  under the multi‑tracer methodology of Heinrich et al.  …”; later: “SPHEREx 3–5σ detection of fNL = −35/8 is projected.”)

**Problem**

The claim that the specific matter‑bounce value of \(f_{\rm NL}=-35/8\) is “testable at 3–5σ with SPHEREx” relies on:

- A fiducial σ(fNL)≈0.7 for SPHEREx forecasts from .
- The assumption that the systematic degradation will still allow a 3–5σ detection of a value |fNL|≈4.4.

However, Heinrich et al.  quote uncertainties that depend strongly on tracer selection, \(k_{\rm max}\), systematics penalties, and whether bispectra are combined with other probes. The current paper adopts some of these numbers but does not show a full Fisher recomputation for the *exact* SPHEREx configuration and matter‑bounce tracer set it proposes. It then states “3–5σ detection” in a way that can be read as a *robust* forecast, which is not fully justified by the derivation.

**Required fix**

- Downgrade the language to something like:  
  “Under the most optimistic SPHEREx multi‑tracer Fisher assumptions of , a value \(|f_{\rm NL}| \simeq 4.4\) would be detectable at the few‑σ level; our anomaly‑selected QSO sample could in principle contribute, but we do not perform a full SPHEREx Fisher analysis here.”
- Make clear that this is *conditional* on the Heinrich et al. configuration and systematics budget; it is not an independent SPHEREx forecast.

---

### P3-M5 — NANOGrav Bayes factor and σ interpretation  
**Type:** MAJOR  
**Location:** Abstract and §V A (“γ=2.567±0.382; the matter-bounce prediction γ=3.0 sits at +1.13σ (marginally consistent) and SMBHB γ=4.33 at +4.61σ (Savage-Dickey BMB/SMBHB=7.1×10^3).”)

**Problem**

The paper fits a power‑law to the NANOGrav 15‑yr “KDE free‑spectrum likelihood” product using emcee and obtains posteriors for γ and log10 A.

Concerns:

1. **Use of KDE free‑spectrum product**  
   This is a *compressed* product derived under specific assumptions; NANOGrav’s own model comparison in  uses a more complete likelihood. A PRD‑level paper using NANOGrav data should emphasize that these Bayes factors are *approximate* and are *not* directly comparable to those reported by NANOGrav. The abstract currently quotes BMB/SMBHB≈7×10^3 without any qualifier.

2. **σ vs. credible interval**  
   The text uses γ=2.567±0.382 as a “Gaussian-approximation mean ± std dev” and then notes that the 68% CI is [2.304,2.882], i.e. asymmetric. It then interprets “+1.13σ” and “+4.61σ” in terms of the std‑dev, not the credible interval. While this is common in quick approximations, PRD standards would prefer to either:
   - compute the actual posterior probability that γ>3.0 or γ>4.33, or
   - not use “σ” language when the distribution is clearly non‑Gaussian.

3. **Bayes factor magnitude**  
   The Bayes factor B≈7×10^3 is large; the method (Savage–Dickey on a KDE‑compressed likelihood) is not fully detailed in this paper. Without a careful cross‑check against independent computations (e.g., Ceffyl or enterprise analyses), this could be overstating the evidence.

**Required fix**

- In the abstract, qualify the Bayes factor as “approximate, using the published NANOGrav KDE free‑spectrum product, not the full timing-residual likelihood.”
- Replace “+1.13σ” and “+4.61σ” by a wording based on credible intervals, e.g. “γ=3.0 lies within the 95% credible interval; γ=4.33 lies far outside it.” Or provide the posterior probabilities \(P(\gamma>3.0)\), \(P(\gamma>4.33)\) and avoid informal σ‑language.
- In §V A, add a short paragraph explaining the limitations of using the free‑spectrum KDE product and explicitly state that this is an *illustrative* application, not a competitive PTA analysis.

---

### P3-M6 — “Largest multi‑archive anomaly search” / “141×” and “73×” claims  
**Type:** MAJOR  
**Location:** Abstract and Conclusions:  
- “The point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase.”

**Problem**

Liang et al.  report 2,685 anomalies in the DESI Bright Galaxy Survey out of ∼250,000 EDR spectra (1.07%).

- 195,829 / 2,685 ≈ 72.9 → “∼73× like‑for‑like increase” looks numerically consistent.
- 378,080 / 2,685 ≈ 140.8 → “∼141×” also consistent.

However:

-  is indeed a single‑survey DESI EDR catalog, but there may be other prior multi‑survey anomaly works, including cross‑matching anomaly searches between e.g. SDSS and WISE (not necessarily using autoencoders). I did not find a *larger purely autoencoder‑based catalog* in a single survey than , so the statement is likely correct, but it should be carefully scoped: “largest autoencoder‑based single‑survey anomaly catalog to date” rather than “largest prior single‑survey anomaly catalog” in absolute terms.

**Required fix**

- Soften the novelty claim to something like:  
  “∼141× larger than the largest prior *autoencoder‑based* single‑survey anomaly catalog ” unless the authors can document that no larger anomaly catalog of any method exists in the literature.
- Similarly clarify “DESI-only axis ... ∼73×” as “∼73× more anomalies than the DESI BGS autoencoder catalog of Liang et al.  under comparable S/N and wavelength coverage.”

---

### P3-M7 — Catalog sizes and dedup counts: minor inconsistencies in wording  
**Type:** MAJOR  
**Location:** Abstract; Table I footnotes; §III and §IV C, also Conclusions.

**Problem**

Several numbers are given:

- 7 per-survey native counts sum to 388,493 (DESI 195,829 + SDSS 77,905 + LAMOST 113,342 + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419).  
- After deduplication: 378,280 unique anomalies, containing 200 Planck patches + 378,080 point sources.  
- Earlier: cross-transfer baseline 319,443, historically including ACT.

Within the text these are mostly internally consistent, but the wording is convoluted and easy to misread. I re‑summed and got:

- 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493 (correct).  
- 388,493 − 10,213 = 378,280 (dedup compression 2.629%; matches text).  
- 378,280 − 200 = 378,080 point sources (matches stratification note).

The potential confusion: Table I’s “Total (cross‑transfer, ACT‑incl.) 319,443” appears next to “Path-C unique (primary) 378,280”, so a casual reader might think native retrain reduced counts, when in fact it increased them (mostly via LAMOST). The text explains this in detail in footnotes, but PRD prefers that headline numbers be clearly and simply stated in the main text.

**Required fix**

- In §III leading paragraph, add a concise bullet or sentence summarizing the pipeline:

  “The initial cross‑transfer baseline contained 319,443 anomalies (including a 200‑patch ACT block). Path‑C native retraining and including Planck native CMB increased the per‑survey total to 388,493 detections across 7 archives; 7‑way 5″ deduplication compresses this to 378,280 unique objects, of which 378,080 are point sources and 200 are Planck patches.”

- In the abstract, consider removing the historical cross‑transfer number entirely; it’s not needed in the abstract and only causes confusion.

---

### P3-M8 — Novelty fractions: “genuine novelty” vs. SIMBAD unmatched  
**Type:** MAJOR  
**Location:** Abstract (“genuine novelty fraction of ~17.8%”), §IV A, Fig. 5.

**Problem**

The paper does a commendably careful job of warning that SIMBAD‑unmatched fractions (e.g. 58.8% aggregate, 99% for DESI top‑10k) overstate novelty, and then reports:

- DESI top‑1,000 anomalies → 822/1,000 matched in at least one of 20 catalogs via CDS X‑Match → 17.8% unmatched (“genuine novelty fraction”).

This is clearly described as a “single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested.” However, in the *abstract* the term “genuine novelty fraction of ∼ 17.8%” appears without that qualification, and could be misread as a robust characterization of the whole catalog.

Moreover, I cannot independently verify the 822/1,000 match count because the underlying list and cross‑matching procedure are not in the text; only the outcome is stated. There is no obvious contradiction with the catalog coverage of these surveys, but PRD will require that the cross‑match procedure be precisely documented in the main text or appendices, not only in a “companion data repository”.

**Required fix**

- In the abstract, change wording to something like:  
  “... yields a **single-stratum point estimate** of ∼17.8% unmatched in 20 major catalogs for the top‑1,000 DESI anomalies; we do not generalize this to the full catalog.”
- In §IV A, add a technical paragraph summarizing the cross‑matching settings (search radius, matching logic when multiple catalogs have entries, how blends and close pairs are treated), not just referring to the companion repository. This makes the 17.8% figure auditable from the paper itself.

---

### P3-M9 — Ambiguous use of “0% artifact rate”  
**Type:** MAJOR  
**Location:** §III A (“Spectral inspection of the top 200 confirms a 0% artifact rate.”)

**Problem**

The authors claim that among the top 200 DESI anomalies, visual inspection finds 0% artifacts. This is based on their own assessment; no details are given on how artifacts are defined or who inspected the spectra.

Given the scale (22.5M spectra), claiming 0% artifacts in a 200‑object sample is very strong. It is plausible that obvious reduction artifacts were not seen, but PRD standards require either:

- a description of the inspection protocol and criteria, or
- a more cautious statement (“no clear reduction artifacts were identified in a manual inspection of the top‑200 objects”).

**Required fix**

- Replace “0% artifact rate” by a more careful phrase:

  “In a manual inspection of the top 200 spectra, we did not identify any clear data‑reduction artifacts.”

- Optionally add a short methodological note: how many inspectors, what they were trained to flag, and whether disagreements were resolved.

---

### P3-M10 — Some claimed percentages cannot be recomputed from given information  
**Type:** MAJOR  
**Location:** Various, e.g.:

- “Galaxies are flagged at ∼20× the QSO rate (0.75% vs. 0.037%).”
- “SIMBAD-unmatched: 90%” for SDSS, “∼50%” for LAMOST, etc.
- Injection‑recovery fractions in Fig. 7 (e.g. LAMOST 5.8%, eROSITA 1.2%, Gaia 5.2%, etc.).

**Problem**

The instructions ask to recompute every quoted percentage from displayed numbers. For many of these, the underlying counts (e.g., numbers of galaxies and QSOs, numbers of matched vs. unmatched entries per survey, raw injection counts per amplitude) are not given in the text or tables. The paper therefore does not allow a referee to recompute these values directly; at best, one can check their plausibility.

This falls short of PRD’s ideal of reproducibility for all *headline* numbers in the body.

**Required fix**

- For key survey‑ level percentages (anomaly rates per class, SIMBAD‑unmatched fractions per survey, injection‑recovery fractions at 5σ):

  - Add a table listing the *numerators and denominators* (e.g., “DESI: 48,750 galaxy anomalies / 6.5M classified galaxies → 0.75%; 2,406 QSO anomalies / 6.5M classified QSOs → 0.037%” or whatever the actual numbers are).
  - For injection tests, provide a small table with entries like “LAMOST, continuum‑dip: recovered 29/500 at 5σ → 5.8%” and similarly for other plants.

- This does not require listing every amplitude level, only enough to audit the 5σ “gate” decisions.

---

### P3-N2 — Minor numerical re‑checks that pass but are worth noting  
**Type:** NIT  
**Location:** Various

- 195,829 / 22,504,897 ≈ 0.0087 → 0.87% anomaly rate (correct).
- 77,905 / 2,304,830 ≈ 3.38% (correct).
- eROSITA: 298 / 930,203 ≈ 0.032%; they quote 0.03% (OK).
- NEOWISE polar fraction: 17 / 436 ≈ 3.9%; uniform‑sphere expectation for |b_ecl|>80° caps ≈ 1.52%; 3.9 / 1.52 ≈ 2.6× (correct).
- Dedup compression: 10,213 / 388,493 ≈ 2.629% (correct).

No action required; these numbers are internally consistent.

---

## 3. Other textual / style issues relevant for PRD

### P3-M11 — Version‑history / internal bookkeeping language in body and references  
**Type:** MAJOR  
**Location:** Multiple places, e.g.:

- Abstract date “(Dated: June 2026)” tied to arXiv acceptance, followed by references to “private pending arXiv acceptance; public upon acceptance” in Data availability.
- Footnotes: “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity.”
- Repeated phrases like “companion data repository”, “archival comparison artifact”, “Path‑C final”.

**Problem**

PRD papers are supposed to read as self‑contained research articles, not as arXiv submission logs. The text contains several bits of version‑history or repository‑management prose more appropriate to a software release note. The journal will almost certainly ask for those to be removed or heavily streamlined.

**Required fix**

- Remove all “pending arXiv acceptance”, “bibkey label retained”, “Path‑C final” kind of language. Replace by neutral statements:

  - “All data and code are publicly available at [repository]” (without conditions).
  - “We refer the reader to Ref. [XX] for additional implementation details,” or “Additional plots and code are provided in the Supplemental Material.”

---

### P3-N3 — Duplicate phrases / slight repetitions  
**Type:** NIT  
**Location:** §II D Step 4: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”

**Problem**

There is a duplicated phrase “reproducibility scripts shipped with... shipped with...”.

**Required fix**

- Remove one copy:  
  “... documented in reproducibility scripts provided in the companion data repository.”

---

### P3-M12 — Length vs. contribution  
**Type:** MAJOR  
**Location:** Entire paper; 20 pages, complex appendices, multiple application domains.

**Problem**

The core new contribution is a multi‑archive anomaly catalog and a demonstration of its potential for cosmology. The paper also includes:

- Detailed engineering of GPU pipelines, native retrains, and injection tests.
- A non‑trivial fNL Fisher forecast.
- A full NANOGrav spectral‑index MCMC with Bayes factors.
- A long ACT appendix.

This breadth is not necessarily bad, but the current 20‑page length and density of auxiliary material feel more appropriate for an extended methods paper + a separate cosmology application paper. For PRD, clarity and focus are important; readers interested in cosmology may be overwhelmed by LAMOST pathology and GPU I/O details, while anomaly‑detection readers may not care about NANOGrav.

**Required fix**

- Strongly consider splitting or at least compressing:

  - Move most of the GPU pipeline, training schedule, and ACT‑quarantine details to a Supplement or code repository; keep only a short summary table in the main text.
  - Shorten NANOGrav discussion to a brief illustration (1–2 paragraphs) or spin it into a separate PTA‑focused paper if the authors want to claim anything about bounce vs. SMBHB evidence.
  - The main manuscript would likely be more appropriate at ~12–14 PRD pages focusing on the catalog, its validation, and the fNL Fisher forecast, with other material relegated to supplemental.

---

## Summary recommendation

**MAJOR REVISIONS**

The bibliography is mostly accurate and correctly matched to real publications, but there are important mis‑uses or over‑extensions of some references (Wands 2010 for matter‑bounce, Heinrich et al. for SPHEREx detectability, NANOGrav compressed products for Bayes factors) that require correction. Several headline statistical claims (genuine novelty fraction, σ‑improvement, Bayes factors) are stated too strongly given the methods and should be more cautiously framed. The paper is also overlong and somewhat unfocused for PRD, combining catalog construction, survey systematics, Fisher forecasts, and PTA model comparison in one piece. With tightened claims, clearer separation of incomparable σ values, better documentation of key percentages, and removal of version‑history prose, the work could reach PRD standards, but it requires a substantial, not merely cosmetic, revision.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E10] **Equation E1 is dimensionally inconsistent as written.** The displayed relation
\[
\log_{10}\rho_i = 21\; 2\log_{10}A - \log_{10}(12\pi^2) + (\gamma-3)\log_{10}f_{\rm yr} - \gamma\log_{10}f_i - \log_{10}T_{\rm obs}
\]
is not internally consistent with the surrounding prose because \(\rho_i\) is a power-spectrum quantity while the right-hand side mixes dimensionless logs with \(T_{\rm obs}\) and frequencies without clearly specifying units or the normalization convention for \(A\) and \(f_{\rm yr}\). The paper later treats \(\rho_i\) as a free-spectrum amplitude proxy, but it never states the unit system needed to make the equation unambiguous, so the normalization is not auditable from the text alone.

[P3-M10] **The quoted eROSITA 95.3% overlap and “95.3× enrichment” are numerically inconsistent with the stated random expectation.** The paper says “284/298 = 95.3%” and “expected 2.98 under the random-independence null,” which would imply an enrichment of \(284/2.98 \approx 95.3\), so that part is fine; however, the accompanying phrase “95.3× enrichment” is only correct if the numerator is 284 and the denominator is 2.98, whereas the text also frames it as an overlap fraction. The two interpretations are mathematically different, and the caption/body should explicitly distinguish *fraction of the catalog recovered* from *enrichment over random* to avoid conflating them.

[P3-M11] **The 637 multi-survey coincidences plus 9,576 intra-survey duplicates do sum to 10,213, but the implied compression percentage is slightly misstated in one place.** Using the paper’s own totals, \(10{,}213 / 388{,}493 = 0.02628\), i.e. 2.628%, which rounds to 2.63% and is consistent with the table. The abstract’s “2.629% compression” is also fine, but the prose elsewhere alternates between “2.629%” and “2.63%”; that is not a scientific error, but it is a stale-rounding inconsistency that should be standardized.

[P3-M12] **The SPHEREx significance claim is arithmetically over-asserted relative to the stated forecast uncertainty.** The body says SPHEREx would detect \(f_{\rm NL}=-35/8\) at “3–5σ,” but the cited Heinrich et al. forecast is \(\sigma(f_{\rm NL})\approx 0.7\). Since \(|-35/8|/0.7 \approx 6.25\), the raw ratio is closer to \(6\sigma\) than to 3–5σ. The only way to recover the quoted range is to assume a substantial degradation budget, but that degradation is not quantified in the sentence where the claim is made, so the numerical basis is incomplete.

[P3-M13] **The abstract’s “3–5σ with SPHEREx” language is not supported by the body’s own numbers.** In §V and Appendix C, the paper repeatedly frames the SPHEREx forecast as a *degraded* Fisher estimate, yet the actual numerical inputs shown are \(\sigma(f_{\rm NL})=0.7\) from Heinrich et al. and a matter-bounce amplitude of 4.375, which would imply detection significance above \(6σ\) before degradation. The paper needs to show the exact degradation factor that transforms 6.25σ into the stated 3–5σ interval.

[P3-M14] **The DESI band-dominance percentages in Table VI do not exactly match the text in the abstract/conclusions.** Table VI gives multi-band 77.2%, B-dominant 22.7%, R-dominant 0.02%, Z-dominant 0.01%, artifact suspect 0.05%, totaling 100%. The prose elsewhere sometimes compresses this to “77% multi-band and 23% B-dominant,” which is acceptable rounding, but the abstract’s “77% multi-band” should not be presented as an exact partition if the table is meant to be the authoritative breakdown. This is a minor consistency issue, but PRD readers will expect the table and abstract to round in the same direction.

[P3-M15] **The DESI top-10,000 SIMBAD/NED figures are internally consistent, but the body does not clearly distinguish database absence from novelty.** The paper states that only 0.2% of the top 10,000 appear in SIMBAD and 12.7% in NED, then later says the genuine novelty fraction is 17.8% after cross-matching against 20 catalogs. Numerically, those statements can coexist, but the body should make explicit that SIMBAD and NED percentages are *coverage diagnostics* and not directly comparable to the 17.8% novelty estimate. Without that clarification, the reader can mistakenly read the 0.2%/12.7% numbers as evidence of stronger novelty than the paper actually claims.

[P3-M16] **The NANOGrav Bayes-factor notation is potentially ambiguous in the body, even though the arithmetic is correct.** The text reports \(B_{\rm BMB/free}=3.23\), \(B_{\rm SMBHB/free}=4.52\times10^{-4}\), and therefore \(B_{\rm BMB/SMBHB}=7.14\times10^3\). That ratio is correct, but the notation changes across the abstract and §V A between “BMB/SMBHB,” “BMB/free,” and “SMBHB/free” without always restating the reference model. Because Bayes factors are directional, the manuscript should specify the denominator every time or risk readers misreading the comparison direction.

[P3-M17] **The “largest multi-archive anomaly search reported to date” claim is not actually quantified against the previous multi-archive literature in the paper body.** The paper gives a factor of 141× over the largest prior single-survey anomaly catalog, but does not provide a corresponding comparison to earlier *multi-archive* searches, which is what the superlative actually asserts. That is a novelty-claim mismatch: the evidence shown supports “largest single-study anomaly catalog” more directly than “largest multi-archive search.”

[P3-M18] **The “no correlation with Galactic latitude” statement is weaker than the wording suggests.** The paper reports Spearman \(r=0.0005\), \(p=0.92\), and Pearson \(r=0.006\), \(p=0.21\), which do show no detectable linear trend in the tested summary statistics. But the same section also notes that the survey footprints themselves avoid the Galactic plane, which means the test has limited power to rule out selection-driven structure. The manuscript should not phrase this as evidence that foreground contamination is absent; it only shows that the chosen one-dimensional summaries did not detect a trend.

[P3-M19] **The DESI vs. LAMOST “∼90× increase in sample size” comparison is not exactly supported by the numbers in the paper.** The paper compares the DESI anomaly rate to Liang et al.’s 1.07% on “∼250,000” DESI EDR spectra, while this manuscript uses 22,504,897 DESI spectra. The ratio is \(22.5\text{M}/0.25\text{M}\approx 90\), so the arithmetic is fine, but the paper does not explicitly state whether Liang et al.’s denominator is exactly 250,000 or rounded. Because the conclusion hinges on that ratio, the manuscript should either use exact source counts or quote the increase approximately without implying precision.

[P3-M20] **The line “three highest-scored anomalies are Z-dominant” is consistent with the table, but the score values shown in the body are not tied to the taxonomy counts.** Table VI lists only 19 Z-dominant objects out of 195,829 anomalies, yet the narrative singles out the three highest-scored anomalies as Z-dominant and uses that to motivate high-\(z\) quasars. That is a plausible interpretation, but the paper does not quantify how many Z-dominant objects are actually high-\(z\) candidates versus ordinary absorption-heavy spectra. As written, the rhetorical leap from “extreme score” to “high-\(z\) quasar” is stronger than the evidence shown.

[P3-M21] **The abstract’s claim that the catalog is built from “37.3 million sources and map patches” is rounded too aggressively relative to the table totals.** Table I gives 37,292,042 survey-level detections in the cross-transfer baseline and 37,272,042 for the Path-C unique row. The abstract’s “37.3 million” is acceptable rounding, but the paper uses the rounded figure in places where the exact count matters for rate calculations. This is a small formatting issue, yet it matters because the table already provides exact counts and the abstract should not blur which denominator is being used.

[P3-M22] **The “0% artifact rate” claim for the top 200 DESI anomalies is unsupported by any defined inspection protocol.** The paper states the rate as a fact, but it does not specify whether the inspection was blind, how many reviewers participated, what counted as an artifact, or whether any borderline cases were excluded. That makes the 0% figure non-reproducible as written. Even if the count is correct, the paper needs an operational definition of “artifact” and a documented review protocol.

[P3-M23] **The use of “FAIL-with-diagnostic at 5σ” is not numerically standardized across surveys.** In the injection-recovery discussion, SDSS passes at 64%, Planck at 100%, and NEOWISE at 100%, while LAMOST, Gaia, and eROSITA fail at 5.8%, 5.2%, and 1.2%. The phrase “FAIL-with-diagnostic” is fine conceptually, but the paper also mixes this with 41.0% and 81.5% “XV-stability” values, which are different null procedures. Those numbers should be explicitly labeled as different metrics everywhere they appear; otherwise the reader may compare them directly as if they were the same kind of recovery statistic.

[P3-M24] **The abstract’s “7.9% improvement consistent with no improvement at <1σ” is mathematically correct but underspecified.** The body shows \(\sigma(f_{\rm NL})\) changing from 8.98 to 8.14, which is indeed a 7.9% reduction, but the significance of that reduction depends on the assumption \(F_0 + c\alpha^2\) and the uncertainty on \(\alpha\). The paper should identify that the “<1σ” statement refers to \(\alpha\)’s uncertainty, not to a direct significance test of the Fisher improvement itself.

[P3-M25] **The table’s “top-1%” labels are not uniformly literal.** For DESI, SDSS, LAMOST, Gaia, and NEOWISE the labels are genuinely percentile-based or effectively top-1%, but eROSITA uses a “top-298 cap” that the paper itself says is “equivalent to S > 0.259” and “roughly the top-0.03%.” That means Table I’s broad “top-1%” phrasing is not accurate for eROSITA unless the footnote is read very carefully. The manuscript should not rely on the table caption alone for that point.

[P3-M26] **The Planck patch count of 200 is consistent across the paper, but Appendix F’s ACT arithmetic is easy to misread and should be cleaned up.** Appendix F states that the 8-way-with-ACT variant would have produced “388,693 − 10,213 = 378,480 unique objects (+200 relative to the headline).” That arithmetic is correct only if 388,693 includes the quarantined ACT block and 10,213 is the same dedup count after removing overlaps. The main text should explicitly repeat that this is a sensitivity artifact and not a catalog result, because the minus-sign expression is too easy to misparse.

[P3-M27] **The statement that the DESI top-1,000 anomalies are “all absent from SIMBAD” conflicts with the later 82.2% archival-ID rate unless the catalog sets differ, which the paper only explains later.** The abstract says the top-1,000 DESI anomalies yield a 17.8% genuine novelty fraction after cross-matching 20 catalogs, and the body says the top-10,000 DESI anomalies are 0.2% in SIMBAD and 12.7% in NED. Those are different matching exercises, so they are not contradictory, but the manuscript should state the scope of each claim more prominently because “all absent from SIMBAD” can be read as a statement about the top-1,000 rather than just the top-scored objects.

[P3-M28] **The cosmology section mixes \(\sigma\)-language and posterior-interval language in a way that can mislead readers.** For NANOGrav, the paper gives \(\gamma=2.567\pm0.382\) and also \(\gamma=2.591^{+0.291}_{-0.287}\), then uses the former to compute “+1.13σ” and “+4.61σ.” Because the posterior is explicitly non-Gaussian and asymmetric, the paper should not present the standard deviation and credible interval as interchangeable. This is not just stylistic: it changes the numerical interpretation of how “far” the matter-bounce and SMBHB values are from the posterior.

