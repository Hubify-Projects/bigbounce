# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 13.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36324, completion=1286, total=37610, search_context_size=low, cost={'input_tokens_cost': 0.10897, 'output_tokens_cost': 0.01929, 'request_cost': 0.006, 'total_cost': 0.13426}

---

## PAPER-PER-B1 – Mis-cited Zhu & Cai 2026 echo paper  
**Type:** MAJOR  

- **Location:** Assumptions §2.3, “Models that invoke prolonged post-bounce inflation … Zhu & Cai~\cite{Zhu:2026echoes}” and audit trail comments.  
- **Issue:** The paper insists `Zhu:2026echoes` exists with arXiv:2603.13924 and PRD 109, 123511, but no such paper or arXiv ID is currently findable; arXiv IDs in the 2603.x range do not yet exist and there is no Zhu–Cai 2026 “echoes” PRD109:123511 in ADS or publisher databases. The earlier self‑defense (“FALSIFIED. All bibkeys EXIST…”) is itself unsupported.  
- **Fix:** Replace this reference with a real, verifiable published/arXiv work (with correct authors, title, journal, and ID), or explicitly mark it as an unpublished in‑prep manuscript / private communication and remove all claims that it has a real arXiv ID and DOI.

---

## PAPER-PER-M1 – Nonstandard Heinrich et al. 2024 citation string  
**Type:** MAJOR  

- **Location:** Abstract, multiple places in body: “Heinrich \etal~2024~\cite{Heinrich:2023} (Fig.~6 / Table~3…)”.  
- **Issue:** The key `Heinrich:2023` is described as “Heinrich et al. 2024”, but the citation string suggests a 2023 arXiv entry; this is at best confusing and at worst inconsistent with the actual paper metadata (year of arXiv posting vs. journal publication year).  
- **Fix:** Make the citation internally consistent: either treat it as Heinrich et al. (2023) throughout, or update the bib entry and in‑text year to the actual publication year of the specific paper being used (and check that figure/table numbering matches that paper).

---

## PAPER-PER-M2 – Cai & Brandenberger 2014 normalization claim needs precise metadata  
**Type:** MAJOR  

- **Location:** Assumptions §2.3 and Appendix A, discussion of “Cai & Brandenberger~\cite{CaiBrandenberger:2014} obtain $\fnl=-35/16$…”.  
- **Issue:** The text talks about “Li & Brandenberger” and “Cai & Brandenberger 2014” somewhat interchangeably and attributes the $-35/16$ normalization to them, but does not give a concrete, checkable paper title / arXiv ID. Without that, it is hard to verify whether the cited paper actually computes $f_{\rm NL}=-35/16$ in the stated convention.  
- **Fix:** Identify explicitly which paper is meant (full author list, title, arXiv ID, and journal reference) and confirm that it indeed quotes $f_{\rm NL}=-35/16$ at $c_s=1$; if not, correct the normalization comparison and attributions.

---

## PAPER-PER-m1 – Wilson–Ewing 2012 usage needs precise reference  
**Type:** minor  

- **Location:** Intro first section (“Wilson-Ewing class… \cite{WilsonEwing:2012}”), Assumptions §2.3, and consistency‑relation §8.2.  
- **Issue:** The text relies heavily on “Wilson-Ewing 2012” for the quasi‑dust spectrum and bounce transmission, but never states the full title or arXiv ID; there are multiple Wilson-Ewing 2012 bounce‑related papers, and only one may contain the exact relations used (e.g. \(n_s = 1+12w\)).  
- **Fix:** Specify exactly which Wilson‑Ewing paper is being used (full title + arXiv ID) and verify that it indeed contains the quoted spectral‑index formula and the linear‑order bispectrum transmission statement; if the formula comes from a different work, correct the citation accordingly.

---

## PAPER-PER-m2 – Eskilt & Komatsu birefringence references loosely specified  
**Type:** minor  

- **Location:** Systematics §9.5 and Discussion §10.3 (Eskilt 2022 WMAP+Planck, Cosmoglobe DR1 II, ACT DR6 Diego‑Palazuelos et al.).  
- **Issue:** Several birefringence papers are cited in a narrative way (Eskilt 2022, Eskilt 2023 Cosmoglobe, Diego‑Palazuelos 2025) with approximate years and no clear mapping to specific arXiv IDs or journal entries; this makes it difficult to confirm the quoted numbers (e.g., β=0.342°±0.094° at 3.6σ) against the correct paper.  
- **Fix:** For each of these results, pin down the exact paper (full author list or first author + “et al.”, title, arXiv ID, journal and year) and check that the stated central values and errors match; update the text if any numbers or years differ.

---

## PAPER-PER-n1 – “No DESI DR1 fNL yet” claim will go stale  
**Type:** nit  

- **Location:** §8.1 “DESI DR1 has not published an independent $\fnl$ constraint… as of this writing”.  
- **Issue:** This time‑sensitive statement will quickly become false once DESI releases PNG constraints; it is not anchored to a date in the text, so readers cannot tell which “as of this writing” epoch was intended.  
- **Fix:** Add an explicit “as of mid‑2026” (or similar) time‑stamp to the sentence, and/or rephrase to something less brittle such as “At the time of writing (mid‑2026), DESI DR1 had not yet…”.
