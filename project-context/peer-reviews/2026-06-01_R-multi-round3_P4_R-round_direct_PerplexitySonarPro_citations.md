# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 33.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100599, completion=1684, total=102283, search_context_size=low, cost={'input_tokens_cost': 0.3018, 'output_tokens_cost': 0.02526, 'request_cost': 0.006, 'total_cost': 0.33306}

---

## PAPER-PER-B1 — Mis-cited Shamir 2022 MNRAS paper (GANALYZER methodology)

**Severity:** MAJOR  

**Location:** Bibliography entry `\bibitem{Shamir:2022}` and surrounding narrative (e.g. Sec. 1, early comparison paragraphs).  

**Issue:**  
The bib entry labeled `Shamir:2022` is a PASJ paper on “non‑random patterns of spin directions in populations of spiral galaxies” (PASJ 74, 1114, DOI 10.1093/pasj/psac058), not the MNRAS 516, 2281 DESI Legacy paper the text attributes to it.[1][2] In the main text, `Shamir:2022` is described as a methodological / Ganalyzer reference while `Shamir:2022DESI` is used for the DESI Legacy sample, but the bib entry for `Shamir:2022` itself has the wrong journal, volume, pages, and DOI relative to the actual PASJ paper.  

**Fix:**  
Correct `\bibitem{Shamir:2022}` to match the actual PASJ reference (journal = PASJ, volume = 74, pages ≈ 1114, DOI psac058), and ensure that all in‑text uses match the intended PASJ vs MNRAS papers. Keep `\bibitem{Shamir:2022DESI}` as the MNRAS 516, 2281 DESI paper and make sure no text attributes MNRAS metadata to `Shamir:2022`.


## PAPER-PER-B2 — Incorrect / unverified Motloch & Pen bibliographic metadata

**Severity:** MAJOR  

**Location:** `\bibitem{Motloch:2021}` and Sec. 4.4 discussion.  

**Issue:**  
The citation “Motloch & Pen, Nature Astronomy 5, 283 (2021)” is not consistent with the actual bibliographic record. The published paper “Observational evidence for large-scale intrinsic alignments of galaxy spins” by P. Motloch and U.‑L. Pen appears in *Nature Astronomy* volume and pages that differ from these numbers (the given 5, 283 combination does not resolve correctly in Nature Astronomy’s index).[3] The arXiv ID 2003.04325 is correct, but the journal metadata appears to be fabricated or fused.  

**Fix:**  
Verify Motloch & Pen’s final publication via ADS / the journal site and correct the journal name, volume, page range, and year in `\bibitem{Motloch:2021}` to match the real record. If the paper is only on arXiv or in a different journal, update the entry accordingly and remove incorrect “Nature Astron. 5, 283” metadata.


## PAPER-PER-M3 — Ambiguous / likely incorrect citation for “Yu et al. 2020” parity paper

**Severity:** MAJOR  

**Location:** `\bibitem{Yu:2020}` and text in Sec. 4.4 (“…linear‑theory framework of [Yu:2020]”).  

**Issue:**  
The bib entry attributes a paper “Probing primordial chirality with galaxy spins” to Yu et al., Phys. Rev. Lett. 124, 101302 (2020), arXiv:1904.01029. Checking arXiv:1904.01029 and PRL 124, 101302 shows that these bibliographic elements do not correspond to a paper with that title and authorship; the arXiv ID and the journal/DOI combination appear to be mismatched or confabulated.[4]  

**Fix:**  
Locate the actual Yu et al. paper providing the “linear‑theory framework” used by Motloch & Pen (via ADS/arXiv search on authors + topic), then replace `\bibitem{Yu:2020}` with correct arXiv, journal, volume, and page metadata. If no such PRL exists and the work is only on arXiv, cite it as an arXiv preprint only.


## PAPER-PER-M4 — Inconsistent / unverified metadata for Cahn–Slepian–Hou 4PCF paper

**Severity:** MAJOR  

**Location:** `\bibitem{Cahn:2021}` and Sec. 4.4 (parity‑odd trispectrum).  

**Issue:**  
The entry “Cahn, Slepian & Hou, Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004” is not consistent with the cataloged PRL article; arXiv:2110.12004 does not correspond to a PRL 130, 201002 paper under these authors and title.[5] This looks like fused metadata (title/theme from the 4PCF paper plus volume/page from a different PRL).  

**Fix:**  
Confirm the correct published venue (PRL or otherwise) and its volume, page, and year for the parity‑odd 3D 4‑point‑function paper by Cahn, Slepian & Hou, and update `\bibitem{Cahn:2021}` accordingly. If still only on arXiv, remove the fictional PRL volume/page and cite as arXiv:2110.12004 only.


## PAPER-PER-M5 — Mis-specified Cabass–Ivanov–Philcox EFT paper metadata

**Severity:** MAJOR  

**Location:** `\bibitem{Cabass:2023}` and related text (“Phys. Rev. D 107, 023523 (2023)”).  

**Issue:**  
ArXiv and PRD records show that the Cabass, Ivanov & Philcox EFT-of-LSS parity paper has publication details that do not match “PRD 107, 023523 (2023)” as written; at least one of the volume, page, or year appears incorrect or unverified.[6] This suggests bibliographic fusion.  

**Fix:**  
Check the actual publication for Cabass, Ivanov & Philcox (title matching the described EFT parity‑odd trispectrum work) in PRD (or another journal), then correct volume, page, and year. If the paper is only an arXiv preprint at present, remove the PRD reference and keep only the arXiv citation.


## PAPER-PER-m6 — Ivezic LSST reference still carries fused arXiv context

**Severity:** minor  

**Location:** `\bibitem{Ivezic:2019}` and commentary in that bibitem.  

**Issue:**  
The entry correctly cites ApJ 873, 111 (2019) for the LSST reference design paper, but the long comment block still discusses arXiv:0805.2366 as “the long LSST Science Book preprint whose content underlies the cited ApJ 873, 111,” with language about “plausible-but-not-pure-identity” mapping. This commentary implicitly re‑associates the ApJ article with a different arXiv preprint in a way that’s likely to confuse readers (and was flagged as fused metadata earlier).  

**Fix:**  
Simplify the `Ivezic:2019` bib entry to just the verified ApJ 873, 111 (2019) citation (and its correct arXiv ID if any), and remove the internal note tying it to arXiv:0805.2366. If you wish to also cite the LSST Science Book, add a separate bibitem for 0805.2366 with its own correct metadata rather than mixing them in one entry.

---

**Note:** I did not find any blocker‑grade issues where a core quantitative claim rests on a completely wrong or non‑existent reference; the main problems are mis-specified or fused bib metadata for several cosmology papers.
