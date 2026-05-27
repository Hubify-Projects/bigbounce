# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v2_P3_v3_1_63
**Wall time**: 15.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68898, completion=879, total=69777

---

# Forensic review

## PAPER-PER-B1
**BLOCKER** — Section “Cosmological Applications” / bibliography entries `Heinrich2023` and `Munchmeyer2019`. The paper’s cosmology narrative attributes a specific SPHEREx multi-tracer forecast and a “canonical” \(\sigma(f_{\rm NL})\) sensitivity table to `Heinrich2023`, but the cited paper is a 2024 JCAP article on SPHEREx multi-tracer redshift-space bispectra, not the source of the exact numeric forecast language used here. The `Munchmeyer2019` citation is real, but the manuscript’s internal use of it as a direct numerical benchmark is unsupported by the citation itself.  
**Fix:** Re-anchor every quoted forecast to the exact paper and equation/table where it appears, or downgrade the language to “internal Fisher estimate” and stop presenting it as literature-derived.

## PAPER-PER-B2
**MAJOR** — Bibliography entry `ACT_DR6` and all ACT references. The cited title **“The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth”** is not the title of the DR6 cosmology paper the text claims to be using for CMB map anomalies; it is a lensing-power-spectrum paper, not a map-catalog reference. This makes the ACT bibliography metadata fused/misaligned with the manuscript’s claimed use of ACT DR6 patch data.  
**Fix:** Replace the ACT citation with the actual DR6 release/reference relevant to the data product used, or explicitly state that ACT is only a methodological cross-transfer artifact and not the source of the anomaly catalog.

## PAPER-PER-B3
**MAJOR** — Bibliography entry `SDSS_DR18`. The cited reference is **“The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy”** in ApJS 267, 44 (2023), which is a release paper, but the manuscript uses it as if it were a definitive source for the exact DR18 object counts and target-class totals embedded in the table. The paper also mixes DR18 spectroscopy claims with a DESI-style scoring pipeline without documenting the provenance of the exact 2,304,830 number.  
**Fix:** Cite the exact SDSS data-release documentation or catalog file used for the count, and separate catalog metadata from anomaly-selection results.

## PAPER-PER-B4
**MAJOR** — Bibliography entry `eROSITA_DR1`. The citation metadata **“The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century”** is a survey overview, not a DR1 catalog paper with the exact footprint and source-count framing used in the manuscript. The text’s claim that DR1 covers only the western Galactic hemisphere and uses 930,203 sources needs the exact catalog/reference backing that this citation does not provide.  
**Fix:** Replace with the specific DR1 catalog/publication that documents the footprint and source count, or add the catalog DOI/archive record.

## PAPER-PER-B5
**minor** — Bibliography entry `Nicolaou2026`. It is cited as **“MNRAS (2026, in press)”** with no arXiv ID, DOI, or accessible bibliographic identifier. That is weak for a citation-chain audit and looks unfinished compared with the rest of the bibliography.  
**Fix:** Add the arXiv ID or DOI, or remove the citation until the preprint/publication is verifiable.

## PAPER-PER-B6
**minor** — Bibliography entry `Lamost_DR10`. The title **“The LAMOST Data Release 10”** and venue **Research in Astronomy and Astrophysics (2024)** are plausible, but the citation is too underspecified for a forensic audit: no volume, page, DOI, or arXiv ID is given.  
**Fix:** Add the full bibliographic record. If the exact DR10 source is a release note rather than a paper, cite the release page instead of a journal stub.
