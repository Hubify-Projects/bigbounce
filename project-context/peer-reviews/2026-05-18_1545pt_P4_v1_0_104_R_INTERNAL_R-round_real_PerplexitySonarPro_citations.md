# P4_v1_0_104_R_INTERNAL R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1545pt
**Wall time**: 18.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=86758, completion=416, total=87174

---

## PAPER-PER-B1 — Motloch & Pen citation is correct

The paper cites Motloch & Pen with arXiv ID 2003.04325 and title “An observed correlation between galaxy spins and initial conditions,” which matches the published paper (Nature Astronomy 5, 283, 2021), not arXiv:2003.04325.[1][2] The current arXiv:2003.04325 is Casey Cartwright, “Entropy production far from equilibrium in a chiral charged plasma in the presence of external electromagnetic fields,” unrelated in title, topic, and authorship.[2]

**Issue:** Fused metadata: correct authors, journal, and description for Motloch & Pen, but the arXiv ID belongs to an unrelated plasma-physics paper.[1][2]  

**Fix (1–2 sentences):**  
Replace the arXiv ID 2003.04325 with the correct identifier for Motloch & Pen’s spin–initial-conditions paper (or drop the arXiv reference and keep only the Nature Astronomy citation) after confirming via ADS/arXiv search.[1]  

---

## PAPER-PER-B2 — Lue, Wang & Kamionkowski citation is consistent

The paper cites Lue, Wang & Kamionkowski’s parity-violating CMB paper as “Cosmological signature of new parity-violating interactions,” arXiv:astro-ph/9812088, Phys. Rev. Lett. 83, 1506–1509 (1999), which matches the actual arXiv entry and journal publication (title, authors, venue, and year all correct).[1]

**Issue:** None; citation-chain is internally consistent for this reference.[1]

**Fix (1–2 sentences):**  
No change needed. Keep this citation as-is; it correctly matches arXiv:astro-ph/9812088 and the PRL reference.[1]
