# P1A_v1A030_R13 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1430pt
**Wall time**: 27.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28836, completion=1531, total=30367

---

## PAPER-PER-B1 — Mis-cited or nonexistent “ABCK1998” reference

**Location:** Sec. 2.1, eq. (2), Barbero–Immirzi discussion (“ABCK 1998” as LQG entropy-counting reference).

**Issue:** “ABCK1998” is not a standard arXiv identifier; the canonical Ashtekar–Baez–Corichi–Krasnov black-hole entropy paper is “Quantum geometry and black hole entropy,” *Phys. Rev. Lett.* 80 (1998) 904–907, arXiv:gr-qc/9710007.[1] Using “ABCK1998” as if it were an arXiv ID is misleading and will fail in automated reference checks.

**Fix:** Replace “ABCK1998” in the bibliography with the correct metadata and arXiv ID, e.g. `Ashtekar, Baez, Corichi, Krasnov, Phys. Rev. Lett. 80 (1998) 904–907, arXiv:gr-qc/9710007`.[1]


## PAPER-PER-B2 — Mis-cited Freidel–Minic–Takeuchi paper

**Location:** Sec. 2.1, paragraph around eq. (1); later again in R2 and R4 route summaries (Freidel–Minic–Takeuchi cited as [Freidel2005]).

**Issue:** The text attributes the statement “Barbero–Immirzi parameter becomes physically observable through its coupling to fermionic matter” to “Freidel, Minic & Takeuchi 2005,” but the well-known paper is “Quantum gravity, torsion, parity violation and all that,” *Phys. Rev. D* 72 (2005) 104002, arXiv:hep-th/0507253.[2] If your BibTeX key is `Freidel2005`, you must ensure the title, authors, journal and arXiv:hep-th/0507253 are used; any mismatch (e.g. wrong year, different paper) would be a fused citation.

**Fix:** Verify that `Freidel2005` in your `.bib` file corresponds exactly to “Quantum gravity, torsion, parity violation and all that,” Freidel–Minic–Takeuchi, *Phys. Rev. D* 72, 104002 (2005), arXiv:hep-th/0507253, and adjust title/year/arXiv ID if needed.[2]


## PAPER-PER-M1 — Ambiguous “HehlDattaNJL1971” / Hehl–Datta NJL reference

**Location:** Sec. 4.1 (Route 1), around eq. (NJL_torsion), citation “[Hehl1976,HehlDattaNJL1971]”.

**Issue:** The standard torsion–NJL contact term is usually traced to Hehl et al. 1976 (*Rev. Mod. Phys.* 48, 393) and earlier Hehl–Datta work, but there is no arXiv:1971… entry; preprint-era papers must be cited via journal details.[3] Using a key like `HehlDattaNJL1971` without a clear journal/year in the bibliography risks either an incomplete or fabricated entry.

**Fix:** Ensure the bibliography contains a real journal reference for the Hehl–Datta NJL paper (authors, journal, volume, pages, year) and not just an invented key; if no 1971 NJL paper exists, drop that key and rely on the 1976 RMP article.[3]


## PAPER-PER-M2 — Minami & Komatsu birefringence reference must match Planck paper

**Location:** Secs. 3.1, 10, 12, 13, Conclusions; various mentions of “Minami & Komatsu [Minami2020]” and Planck birefringence.

**Issue:** The Planck EB-rotation analysis by Minami & Komatsu is “New Extraction of the Cosmic Birefringence from the Planck 2018 Polarization Data,” *Phys. Rev. Lett.* 125, 221301 (2020), arXiv:2010.00039.[4] If your `Minami2020` key points to a different title, year, or arXiv ID, that would be a metadata fusion.

**Fix:** Make sure `Minami2020` is exactly mapped to arXiv:2010.00039 with the correct title and authors, and not to some earlier cosmic birefringence work or a different Minami paper.[4]


## PAPER-PER-M3 — Lue–Wang–Kamionkowski citation needs correct title/venue

**Location:** Sec. 4.4 (Route 4), discussion of Chern–Simons coupling “classical reference … Lue, Wang & Kamionkowski [LueWangKamionkowski1999]”.

**Issue:** The standard cosmic birefringence / Chern–Simons paper is “Cosmological signature of new parity-violating interactions,” Joel Lue, Li-Min Wang, and Marc Kamionkowski, *Phys. Rev. Lett.* 83, 1506 (1999), arXiv:astro-ph/9812088.[5] Any mismatch of title, year, or arXiv ID (e.g. giving a 2000 date or wrong journal) would count as a fused or incorrect citation.

**Fix:** Confirm that the BibTeX entry for `LueWangKamionkowski1999` uses the correct title, *Phys. Rev. Lett.* 83, 1506 (1999), and arXiv:astro-ph/9812088; fix any drift in year, journal or arXiv number.[5]


## PAPER-PER-minor1 — Missing or likely non-existent “Golden2026P1b/P2/P3/P4” arXiv metadata

**Location:** Throughout (abstract, intro, obs sections, barriers, discussion, appendices), e.g. “Golden2026P1b,” “Golden2026P2,” “Golden2026P3,” “Golden2026P4”.

**Issue:** These are self-citations to a 2026 “bigbounce” project; there are no corresponding arXiv IDs visible under those labels, and arXiv does not use a “Golden2026P1b” style identifier.[6] If the bibliography invents arXiv IDs like `arXiv:Golden2026P1b` or assigns them to unrelated records, that would be a hard metadata error.

**Fix:** Treat these as internal project labels only (no fake arXiv IDs); either (i) give them as “in preparation” / “submitted” with no arXiv number, or (ii) once real arXiv submissions exist, replace the placeholders with the actual arXiv:YYMM.NNNNN identifiers and correct titles.[6]
