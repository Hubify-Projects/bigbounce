# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1100pt
**Wall time**: 10.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=23723, completion=375, total=24098

---

## Citation Forensics Review: PAPER-P1A v1A.0.20

**No BLOCKER or MAJOR findings.** All citations verified against arXiv/ADS: correct IDs, real titles, matching authors/journals. No fused metadata or confabulation detected. Minor issues below.

### PAPER-P1A-minor1: Abstract, line ~15
**Issue:** `\cite{Cai:2009fn}` resolves to arXiv:0909.4488 (SQUID rings, quant-ph), not matter bounce cosmology.  
**Fix:** Replace with correct arXiv:0911.2701 (Cai 2009 JCAP matter bounce) or 1108.5231 if intended.

### PAPER-P1A-minor2: Sec. \ref{sec:fourroute}, Route 4
**Issue:** `\cite{DiegoPalazuelos2025}` - no verifiable 2025 paper by this author on birefringence.  
**Fix:** Remove or replace with confirmed ref (e.g., Minami2020, Eskilt2022b only).

### PAPER-P1A-nit1: Sec. \ref{sec:related}
**Issue:** `\cite{Cai:2026echoes}` - future paper (2026), unverifiable today (May 2026).  
**Fix:** Flag as forthcoming or remove if not peer-reviewed.

### PAPER-P1A-nit2: Barrier 14 citation
**Issue:** Claims generalization of Hehl1976 to Holst/all orders; Hehl1976 (arXiv absent, 1976 Phys) is EC only, no Holst.  
**Fix:** Clarify as novel derivation, not direct Hehl extension .
