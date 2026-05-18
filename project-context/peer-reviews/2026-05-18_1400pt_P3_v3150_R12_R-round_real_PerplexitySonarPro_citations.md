# P3_v3150_R12 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1400pt
**Wall time**: 21.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=63813, completion=262, total=64075

---

## PAPER-PER-B1 – Liang 2023 citation scope (MAJOR)

The paper repeatedly cites Liang et al. (2023) as “Liang et al. [Liang2023] (2,685 anomalies on DESI EDR; 1.07% rate)” as the largest prior single-survey spectroscopic anomaly catalog and as a DESI comparison baseline.[0] Liang 2023 is purely a Bright Galaxy Survey (BGS) subset of DESI EDR, not “DESI EDR” as a whole, and it focuses on BGS galaxies (with substantial star contamination) rather than a full DESI spectroscopic sample.[0]  

**Fix (1–2 sentences):** Everywhere “DESI EDR” is used for Liang et al., replace with “the DESI EDR Bright Galaxy Survey (BGS) subset” and clarify that the 2,685 anomalies and 1.07% rate refer to BGS galaxies in EDR, not to the full DESI EDR spectroscopic catalog; correspondingly, rephrase “largest prior single-survey spectroscopic anomaly catalog” as “largest prior single-survey DESI-BGS spectroscopic anomaly catalog.”
