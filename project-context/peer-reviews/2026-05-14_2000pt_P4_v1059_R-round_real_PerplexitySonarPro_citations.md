# P4_v1059 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2000pt
**Wall time**: 15.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=57897, completion=366, total=58263

---

## No BLOCKER or MAJOR Findings

After forensic review of all citations against arXiv/ADS records:

- Jia:2023 correctly maps to ApJ 943, 154 (2023); prior arXiv:2211.03497 fusion with unrelated gr-qc paper resolved in v1.0.59.[1]
- Shamir:2012, Shamir:2020, Shamir:2022 bibitems match actual galaxy spin asymmetry papers (titles/authors/venues verified; no confabulation).[2]
- Lintott:2008 (GZ1), Dey:2019 (DESI DR8), Walmsley:2023 (GZ DESI), Iye:2020, Davis:2014 (SpArcFiRe), etc., all authentic astro-ph.GA/CO papers with exact claims supported.[3]

All arXiv IDs, DOIs, titles, authors, journals correct. No fused metadata, hallucinations, or mismatches.

## minor-PER-1: Sensitivity convention
Abstract/§VIII.B: "0.29% Fisher floor" lacks explicit A-vs-A/2 disclosure pre-v1.0.59 fix. Add footnote: "A uses full modulation; prior drafts used half-A=0.2%."[4]

## nit-PER-2: GZ1 ACW/CCW mapping
Sec. §\ref{sec:labels}: GZ1 P_ACW≡P_CCW stated but not hyperlinked to fn. Cross-ref fn at Sec.\ref{sec:intro} start.[5]

Clean state confirmed. Converge with Gemini/Grok: 5/5 vendors null → arXiv gate met.
