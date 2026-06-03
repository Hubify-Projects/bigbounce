# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 12.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=41008, completion=1004, total=42012, search_context_size=low, cost={'input_tokens_cost': 0.12302, 'output_tokens_cost': 0.01506, 'request_cost': 0.006, 'total_cost': 0.14408}

---

## PAPER-PER-B1 — DESIVAST author list formatting

**Type:** minor  

**Issue:** In the DESIVAST citation the author list is truncated as “H. Rincon, S. BenZvi, K. A. Douglass, D. Veyrat *et al.*”. ADS lists many more co‑authors for ApJ 982, 38 (2025) and the collaboration is *not* a DESI-collaboration paper. The “et al.” is acceptable in-text, but the bibliography entry should either include the full list or clearly follow the journal’s author‑truncation style (e.g., first three authors + “et al.”).  

**Fix:** Adjust the `\bibitem{DESIVAST2025}` author list to the standard truncation used by the target journal (e.g. first three authors then “et al.”) and ensure it matches the order given in the ApJ version or arXiv:2411.00148.  

---

## PAPER-PER-B2 — DESIVAST title capitalization

**Type:** nit  

**Issue:** The DESIVAST title is cited as “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey”, while ApJ/ADS list it as “DESIVAST: Catalogs of low-redshift voids using data from the DESI Data Release 1 Bright Galaxy Survey” (lowercase “low-redshift” and “using”).  

**Fix:** Change the bibitem title string to match the published title capitalization exactly (lowercase “low‑redshift” and “using”).  

---

## PAPER-PER-M1 — ASTRA Zenodo reference metadata

**Type:** minor  

**Issue:** The text cites ASTRA as “ASTRA-DESI EDR probabilistic environment catalog … (Zenodo 10.5281/zenodo.19358024)”, but the current Zenodo record for that DOI lists the title “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” and an author list “Zapata-Zuluaga et al.”. The arXiv bibitem already has this title, but the Zenodo reference in the text does not explicitly link to the same work.  

**Fix:** In \S\ref{sec:astra_per_object}, explicitly connect the Zenodo DOI to the same work as arXiv:2604.01456 by adding the full title next to the DOI or replacing “ASTRA-DESI EDR probabilistic environment catalog” with the exact Zenodo title.  

---

## PAPER-PER-n1 — T-Web DESI concurrent paper status wording

**Type:** nit  

**Issue:** The T-Web paper (Ullah et al., arXiv:2604.02463) is described as “submitted to MNRAS (2026)”. The arXiv record currently lists it as a preprint without an accepted‑journal tag; submission status is not verifiable from arXiv alone.  

**Fix:** Soften the wording to “preprint (2026)” or “arXiv:2604.02463 (in preparation / under review)” unless you have a citable statement from the journal; avoid asserting “submitted to MNRAS” as fact.  

---

## PAPER-PER-n2 — Shamir 2022 venue and title cross-check

**Type:** nit  

**Issue:** The Shamir 2022 reference is now “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), which matches both arXiv:2208.13866 and the MNRAS record. The earlier A&A mis‑citation mentioned in comments is fully corrected; there is no remaining issue, but this is the main previously-problematic external cosmology citation and merits explicit verification.  

**Fix:** No change needed; metadata and title already match the MNRAS and arXiv records.  

---

## PAPER-PER-n3 — Planck 2018 reference detail

**Type:** nit  

**Issue:** The Planck 2018 cosmological-parameters paper is cited generically as “Planck Collaboration, Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020), arXiv:1807.06209”, which matches the published record. However, no DOI is given, while DOIs are provided for some other key references (e.g., Shamir 2022, DESIVAST).  

**Fix:** Optionally add the DOI `10.1051/0004-6361/201833910` to the Planck 2018 bibitem for consistency of bibliographic completeness.
