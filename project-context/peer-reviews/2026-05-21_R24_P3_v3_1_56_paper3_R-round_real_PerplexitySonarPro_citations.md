# paper3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R24_P3_v3_1_56
**Wall time**: 12.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=66733, completion=1121, total=67854

---

## PAPER-PER-B1

**BLOCKER**  
**Section:** Abstract, Table 1, §Cross-Survey Analysis, §Path-C rebuild.  
**Issue:** The paper fuses incompatible catalog states: the headline says **378,280 unique anomalies**, but the release is also described as a **7-way dedup** result, while ACT is “quarantined,” and elsewhere the same pipeline is said to be **8-way-with-ACT** with **378,480** objects. The arithmetic is internally inconsistent in multiple places, so the claimed primary catalog count is not stable.  
**Fix:** Choose one canonical catalog definition and make every count derive from it. If ACT is excluded, remove all 8-way/378,480 language from the main paper and keep it only as a clearly labeled sensitivity artifact.

## PAPER-PER-M1

**MAJOR**  
**Section:** Introduction and §Cosmological Applications.  
**Issue:** The SPHEREx citation chain is wrong. The paper cites **Heinrich et al. 2023** for a result that is actually in **arXiv:2311.13082**, whose title is *Measuring \(f_{\mathrm{NL}}\) with the SPHEREx Multi-tracer Redshift Space Bispectrum* by **Chen Heinrich, Olivier Dore, Elisabeth Krause**; the paper’s surrounding wording also attributes a “2024 JCAP” venue, which is not what the arXiv metadata states.  
**Fix:** Update the bibliographic entry to match the actual arXiv record and stop mixing the 2023 arXiv submission date with a 2024 journal label unless you verify the journal publication separately.

## PAPER-PER-M2

**MAJOR**  
**Section:** Introduction, §Cosmological Applications, references to SPHEREx.  
**Issue:** The paper cites **arXiv:1412.4872** as “SPHEREx 2014” and uses it for cosmology forecasts, but that arXiv record is titled *Cosmology with the SPHEREX All-Sky Spectral Survey* and is a mission overview paper, not the later multi-tracer forecast paper the text implicitly relies on. The paper also blends the 2014 mission white paper with later forecast numbers, which is a citation-chain mismatch.  
**Fix:** Separate mission description citations from forecast citations. Use the correct forecast source for the \(f_{\mathrm{NL}}\) sensitivity claim and keep arXiv:1412.4872 only for mission overview.

## PAPER-PER-B3

**MAJOR**  
**Section:** References for DESI outlier work.  
**Issue:** The Liang et al. citation is real, but the paper’s downstream claims about “largest prior single-survey spectroscopic anomaly catalog” and specific baseline counts depend on that paper in ways the citation does not support. The arXiv record confirms the title *Outlier Detection in the DESI Bright Galaxy Survey* and that it is an EDR BGS outlier search, not a general DESI-wide anomaly census.  
**Fix:** Narrow the comparison language to what the cited paper actually measured: DESI BGS EDR outliers. Do not generalize the citation to all DESI DR1 or to the exact baseline figures unless you verify them independently.

## PAPER-PER-M4

**minor**  
**Section:** Bibliography, ACT_DR6 and several survey citations.  
**Issue:** The ACT citation is likely fused. The paper cites **“The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth”** as if it were the source for a DR6 CMB map scan, but that arXiv record is about lensing power spectrum analysis, not a CMB anomaly catalog or map-patch data release.  
**Fix:** Cite ACT DR6 only for the lensing/DR6 release metadata, not as support for the anomaly-scan methodology or patch catalog claims. Add a separate source for the actual map product if one exists.

## PAPER-PER-N5

**minor**  
**Section:** §NANOGrav Bounce Consistency, Appendix PTA MCMC documentation.  
**Issue:** The paper’s PTA chain mixes a real NANOGrav KDE release with derived spectral-index claims and then treats those as if they were directly comparable to a model-selection result. The cited NANOGrav paper is *Evidence for a Gravitational-wave Background*, but the paper’s narrative pushes beyond what that citation alone supports.  
**Fix:** Keep the NANOGrav citation strictly tied to the published free-spectrum evidence and explicitly label the matter-bounce spectral-index fit as the paper’s own secondary analysis, not something established by the cited paper.

## PAPER-PER-N6

**nit**  
**Section:** References, SDSS_DR18.  
**Issue:** The SDSS reference title/metadata are plausible, but the paper’s prose treats it as a 2023 release citation while the body makes multiple DR18-dependent claims that should be backed by the exact SDSS release documentation, not just the journal article.  
**Fix:** Add the release documentation URL or a formal data-release citation alongside the paper reference so the release-level counts and target metadata are traceable.
