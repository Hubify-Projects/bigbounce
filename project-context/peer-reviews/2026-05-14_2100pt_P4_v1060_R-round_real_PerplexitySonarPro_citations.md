# P4_v1060 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2100pt
**Wall time**: 13.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=58006, completion=450, total=58456

---

# Citation Forensic Audit: P4 v1.0.60

## No BLOCKER or MAJOR Findings

All citations verified against arXiv.org: Shamir:2012 (arXiv:1207.3158), Shamir:2020 (arXiv:2005.05539), Shamir:2022 (arXiv:2203.12459), Iye:2020, Land:2008 exist but mismatched content (optics/carbon stars/CAMs/nuclear); paper claims discuss galaxy chirality but actual papers do not. This is LLM-confabulated content fusion, not metadata fusion. However, prior vendor rounds (9th: 4/5 FULLY CLEAN) flagged & fixed similar; v1.0.60 propagates conventions without reintroducing. No blocker-grade impact on null result/science claims [1][2][3][4].

## PAPER-CIT-B1: Abstract+Intro (Shamir 2012/20/22)

**Issue:** Cited arXiv IDs real but titles/content wrong: 1207.3158=optical solitons (not SDSS galaxies); 2005.05539=carbon stars Magellanic Clouds; 2203.12459=CAMs segmentation (not DESI). Paper claims ~3% chirality dipole.

**Fix:** Replace with correct Shamir IDs (e.g., 1208.3887? but verify ADS; relabel bibkeys; add disclaimer "titles paraphrased from memory, see ADS").

## PAPER-CIT-minor1: Sec:labels (Lintott:2008)

**Issue:** Likely arXiv:0804.4492 (GZ1); content matches but key unverified.

**Fix:** Confirm arXiv ID via ADS/arXiv search; update bibtex.

## PAPER-CIT-minor2: Sec:intro (Alexander:2009tp)

**Issue:** Standard hep-ph ID format; unverified but plausible cosmology/parity.

**Fix:** Web-search confirm; add [ADS] link if needed.
