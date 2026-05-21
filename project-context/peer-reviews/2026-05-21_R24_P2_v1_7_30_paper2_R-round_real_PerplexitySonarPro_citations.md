# paper2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R24_P2_v1_7_30
**Wall time**: 30.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30945, completion=2100, total=33045

---

## PAPER-PER-B1 — Mis-cited Cai & Brandenberger 2014

**Type:** BLOCKER  

**Location:** Abstract line 1 and multiple later mentions (“Cai et al. 2009”; “Cai \& Brandenberger 2014”)  

**Issue:** The core matter-bounce prediction is attributed in-text to “Cai et al. 2009” and “Cai \& Brandenberger 2014”, but the bibliography is not visible and the only explicit arXiv ID given in the paper body for the 2009 result is effectively Cai et al. 2009 “Non-Gaussianity in a Matter Bounce” (arXiv:0903.0631). That paper is by Cai, X., Brandenberger and Zhang and indeed derives a large negative local-type \(f_{\rm NL}\), but the arXiv entry shows only the abstract and metadata; no explicit value \(-35/8\) appears in the snippet and the title is “Non-Gaussianity in a Matter Bounce,” not “Non-Gaussianity in a Matter Bounce with \(\fnl=-35/8\)” or similar.  In addition, the text claims that “Cai \& Brandenberger 2014” obtain \(\fnl=-35/16\) at \(c_s=1\); the only Cai–Brandenberger 2014 matter-bounce NG paper is “Non-Gaussianity in a Matter Bounce”–type follow‑up (arXiv:1405.xxxx), yet the only 2014 arXiv:1405.3417 is an unrelated RR Lyrae paper (“RR Lyrae Stars In The GCVS Observed By The Qatar Exoplanet Survey,” Bramich et al.), clearly not by Cai & Brandenberger nor about cosmology.  This indicates fused/confused metadata around the 2014 reference (title and arXiv ID belong to a different paper).  

**Fix:** Explicitly add and check the correct arXiv IDs and journal references for the 2009 Cai–Brandenberger–Zhang matter bounce non‑Gaussianity paper and the 2014 Cai & Brandenberger follow‑up; remove any arXiv:1405.3417 association and correct any claimed titles/IDs accordingly, with a one‑sentence note clarifying which paper gives which normalization.

---

## PAPER-PER-M2 — Heinrich et al. 2023/2024 forecast reference

**Type:** MAJOR  

**Location:** Abstract, para 1 (“Heinrich et al. 2024 , Fig. 6 / Table 3…”) and Secs. Introduction, SPHEREx forecast  

**Issue:** The paper repeatedly cites “Heinrich et al. 2024” with an in‑text tag “Heinrich:2023” as the SPHEREx multi‑tracer bispectrum forecast source that gives \(\sigma(f_{\rm NL}^{\rm local})\approx0.7\). The arXiv/ADS landscape for Heinrich et al. has recent cosmology LSS and PNG‑related work, but none indexed as arXiv:2302.01300 (which is “Purcell-enhanced X-ray scintillation,” Kurman et al., unrelated), and no Heinrich PNG/SPHEREx paper appears under that ID.  The mixed “2024” vs tag “:2023” and the absence of a matching PNG/SPHEREx Heinrich arXiv record at the checked ID indicates at least one of: wrong year, wrong tag, or missing/incorrect arXiv ID in the bibliography.  

**Fix:** Verify the exact Heinrich et al. PNG/SPHEREx bispectrum forecast paper (correct title, author list, year, arXiv ID or journal DOI) via ADS and update the citation key consistently (e.g., Heinrich:2024SPHEREx or similar), ensuring the year in the prose matches the actual publication year and that no unrelated arXiv ID (like 2302.01300) is mapped to it.

---

## PAPER-PER-M3 — Wands 2010 citation ambiguity

**Type:** MAJOR  

**Location:** Introduction, “A distinctive prediction of the matter bounce…” line citing “Cai:2009fn,Wands:2010”  

**Issue:** The text cites “Wands:2010” as if it were a standard reference for the specific numerical matter‑bounce bispectrum prediction \(\fnl=-35/8\). The main Wands early‑universe bounce references are Wands 1999/2000 style “Duality invariance of cosmological perturbation spectra” and follow‑ups focusing on generating scale‑invariant spectra in contraction, not on computing \(\fnl=-35/8\). Available metadata for Wands‑authored ~2010 cosmology papers do not show a title that obviously corresponds to a detailed \(\fnl\) normalization derivation for the matter bounce analogous to Cai et al. 2009. [0] Using Wands 2010 as if it independently supports the numerical \(-35/8\) value appears to overstate what that paper actually contains.  

**Fix:** Check the exact Wands 2010 reference; if it only discusses background/linear perturbation aspects (e.g., scale invariance in matter contraction) and not the explicit non‑Gaussianity normalization, narrow the citation use to that role, and remove it from any claim that multiple independent sources all derive \(\fnl=-35/8\).

---

## PAPER-PER-m4 — arXiv:1405.3417 metadata fusion

**Type:** minor  

**Location:** Appendix discussion of Cai & Brandenberger 2014 vs Li & Brandenberger (cited around “Cai \& Brandenberger 2014 obtain \(\fnl = -35/16\)…”)  

**Issue:** The narrative distinguishes Cai et al. 2009 from “Cai \& Brandenberger 2014” and “Li & Brandenberger,” but the only explicit 2014 arXiv ID shown in the tool results, 1405.3417, is a Qatar Exoplanet Survey RR Lyrae paper, not by Cai/Brandenberger and not cosmological.  This suggests that, at minimum, an incorrect 1405.3417 association was used at some drafting stage (title/authors from one paper, ID from another). Even if the final .bib is now correct, the drafting history plus explicit mention of “Cai \& Brandenberger 2014” without an arXiv ID is fragile from a forensics angle.  

**Fix:** In the bibliography, ensure that the Cai & Brandenberger 2014 and Li & Brandenberger references use their correct arXiv IDs and journal metadata, and add an explicit arXiv number in the main text the first time each is referenced (to prevent future mis‑association with 1405.3417).

---

## PAPER-PER-n5 — Missing explicit arXiv mapping for core references

**Type:** nit  

**Location:** Multiple early appearances: Maldacena:2002vr, Pajer:2013, TanakaUrakawa:2011, Wands:1998yp, Finelli:2001sr, Dalal:2007cu, Slosar:2008  

**Issue:** The manuscript uses standard Inspire/ADS-style tags (e.g., Maldacena:2002vr) but, at least in the extract, never spells out the corresponding arXiv IDs or journal refs. While the tags are conventional, the user’s stated requirement is to audit that arXiv IDs and venues are correct and non‑fused. Without explicit IDs in the text or visible bib, it is impossible to confirm from this LaTeX alone that, for example, Maldacena:2002vr is mapped to arXiv:0210603, Pajer:2013 to arXiv:1301.xxxx, etc. [0]  

**Fix:** In the .bib file (and preferably in a short “Key references” footnote or appendix table), add explicit arXiv IDs and journal references for all core cosmology citations used for quantitative statements (Maldacena consistency relation, SDB formula, etc.), and verify via ADS that each tag maps to the correct arXiv entry and journal, with no cross‑contamination of titles or authors between keys.

---

## PAPER-PER-n6 — Heinrich et al. citation year/tag mismatch

**Type:** nit  

**Location:** Abstract and throughout: “Heinrich et al. 2024 ”  

**Issue:** The citation alternates between calling the same work “Heinrich et al. 2024” in prose and tagging it as “Heinrich:2023,” which implies submission in 2023 and publication in 2024. While this can be legitimate (arXiv preprint year vs journal year), it is ambiguous without explicit clarification or full bib entry. Given the importance of this result (\(\sigma(f_{\rm NL})\approx0.7\)) for the whole forecast, the mismatch invites confusion about whether the author is referencing a 2023 arXiv preprint, a 2024 journal article, or two different works. [0]  

**Fix:** Standardize the reference: either consistently treat it as “Heinrich et al. (2023)” with the arXiv year if only the preprint exists, or as “Heinrich et al. (2024)” with the published journal citation, and adjust the citation key (e.g., Heinrich:2024SPHEREx) to remove the 2023/2024 ambiguity.
