# paper3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R25_P3_v3_1_56
**Wall time**: 24.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=66705, completion=1342, total=68047

---

## PAPER-PER-B1 – Mis-cited Heinrich et al. forecast numbers (BLOCKER)

The paper states “anchored to the Heinrich+2024 \(\sigma_{f_{\rm NL}} \approx 0.7\) bispectrum-only forecast … internal Fisher diagnostic … \(\sigma_{f_{\rm NL}} \approx 0.07\)–\(0.12\) … 3–10× tighter than the Münchmeyer et al. consensus \(\sigma_{f_{\rm NL}} \approx 0.4\)–0.9 for SPHEREx-class surveys,” but gives no concrete citation to specific numbers in Heinrich et al. or shows that those exact values appear there. [1][2]  
Fix in 1–2 sentences: explicitly quote the exact \(\sigma_{f_{\rm NL}}\) forecast values and configuration (tracers, redshift bins, systematics treatment) from Heinrich et al. with section / figure references, and clearly label the 0.07–0.12 range as an internal diagnostic not appearing in that paper, or remove the numerical comparison and keep only a qualitative anchoring.

## PAPER-PER-M1 – SPHEREx paper metadata mostly correct but needs tightening (MAJOR)

The SPHEREx citation is given as “SPHEREx 2014” with authors “Doré et al.” and is described as “SPHEREx satellite … all-sky spectroscopic survey,” which matches arXiv:1412.4872 (Cosmology with the SPHEREX All-Sky Spectral Survey). [1] However, the current text treats “SPHEREx 2014” like a shorthand paper name and does not give the full title or lead author explicitly in the bibliography block. [1]  
Fix: in the bibliography, explicitly list “O. Doré et al., ‘Cosmology with the SPHEREX All-Sky Spectral Survey,’ arXiv:1412.4872 (2015)” and ensure in-text references use “Doré et al. (2015)” or similar standard citation style.

## PAPER-PER-M2 – Liang et al. citation OK but numbers should be cross-checked (MAJOR)

The paper cites Liang et al. as “Liang et al. 2023” for an outlier search on DESI EDR with 2,685 anomalies at a 1.07% rate from ∼250,000 spectra. [2] The arXiv record (arXiv:2307.07664) confirms the title and author list but does not in the abstract itself show the 1.07% and 2,685 numbers; those are in the main text and need to be verified carefully in the PDF. [2]  
Fix: open the Liang et al. PDF and confirm the exact anomaly count, sample size, and percentage; then either retain the numbers with an explicit “we reproduce their quoted 2,685/1.07% over 250k EDR spectra” or adjust them to match the published values precisely if they differ (e.g., if the denominator or rate is slightly different).

## PAPER-PER-m1 – Münchmeyer et al. reference matches but “consensus” framing is loose (minor)

The paper references Münchmeyer et al. with a “consensus \(\sigma_{f_{\rm NL}} \approx 0.4\)–0.9 for SPHEREx-class surveys,” apparently pointing to arXiv:1810.13424 (“Constraining local non-Gaussianities with kSZ tomography,” M. Münchmeyer et al.). [3] That work indeed forecasts \(\sigma_{f_{\rm NL}}\sim 0.5\) using kSZ tomography plus LSST/CMB-S4, but calling 0.4–0.9 a “Münchmeyer consensus” for SPHEREx-class surveys is broader than what that specific paper actually studies and mixes survey concepts. [3]  
Fix: rephrase to “for comparison, Münchmeyer et al. (2019) forecast \(\sigma_{f_{\rm NL}}\sim 0.5\) using kSZ tomography with LSST and CMB-S4” and drop the “consensus 0.4–0.9 for SPHEREx-class surveys” language unless you can point to specific SPHEREx-focused forecasts with that range.

## PAPER-PER-m2 – SPHEREx detection significance for \(f_{\rm NL}=-35/8\) needs explicit source (minor)

The text claims SPHEREx can test the matter-bounce prediction \(\fnl = -35/8\) at “3–5σ realistic significance” under Heinrich et al.’s multi-tracer methodology, but no explicit source is given that actually computes that detection significance for that model. [1]  
Fix: either (a) make clear this 3–5σ is your own Fisher extrapolation based on Heinrich et al.’s setup (and not a number in Heinrich et al. itself), or (b) if Heinrich et al. or another paper explicitly gives this significance for \(\fnl=-4.375\), cite the exact equation/figure where it appears.

## PAPER-PER-n1 – General bibliography completeness / consistency (nit)

Several key analysis ingredients (e.g., specific DESI DR1 technical documentation, exact version of Gaia DR3 variability catalog, the particular Planck 2018 paper(s) used for CMB maps and non-Gaussianity limits) are cited only generically (e.g., “Planck 2018,” “Gaia DR3”) without full titles and arXiv IDs, while others (like Liang et al., SPHEREx) are more fully specified. [1][2][3]  
Fix: standardize references so that every external dataset or method paper used as a benchmark has a complete citation (title, journal or arXiv ID, year, lead author), and ensure short-hands like “Planck 2018” and “Gaia DR3” are unambiguous by tying them to specific papers in the bibliography.
