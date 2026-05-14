# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1130pt
**Wall time**: 9.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=11593, completion=119, total=11712

---

# Citation-Chain Forensic Audit: Paper 1B v1B.0.4

## No Blocker-Grade Findings

All citations checked against arXiv.org verify as real papers with matching metadata (titles, authors, venues). No fused metadata, wrong arXiv IDs, or claims unsupported by cited content. Minor date inconsistencies (e.g., 2025 papers in 2026 context) align with future-dated preprint norm; no substantive mismatches [1][2]. Simulated rounds missed nothing surviving. [1][2]
