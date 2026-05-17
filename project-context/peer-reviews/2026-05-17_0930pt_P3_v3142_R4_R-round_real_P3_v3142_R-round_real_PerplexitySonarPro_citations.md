# P3_v3142 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0930pt_P3_v3142_R4_R-round_real
**Wall time**: 17.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=58105, completion=1601, total=59706

---

## PAPER-PER-B1 — Mis-cited Liang et al. DESI sample size

**Location:** Introduction, paragraph 2: “Liang *et al.* … approximately 250,000 DESI Early Data Release (EDR) spectra…”  

**Issue:** Liang *et al.* 2023 (“Outlier Detection in the DESI Bright Galaxy Survey”) analyze the Bright Galaxy Survey subset of DESI EDR, not “approximately 250,000” spectra as stated; the arXiv abstract and metadata do not support that specific sample size figure or wording, and the paper is about BGS rather than a generic DESI EDR spectral sample.[1]  

**Fix (minor):** Change the phrase to something faithful but non-fabricated, e.g. “Liang *et al.* applied an autoencoder plus normalizing flow to BGS galaxies in the DESI Early Data Release, identifying 2,685 outliers,” and drop the unsupported “approximately 250,000” unless you add an explicit inline citation to their actual sample size from the body of the paper.[1]  


## PAPER-PER-B2 — SPHEREx citation lacks correct title and author formatting

**Location:** Introduction, paragraph 2: “SPHEREx satellite~\cite{SPHEREx2014}” and corresponding bibliography entry.  

**Issue:** The referenced work is clearly Doré *et al.* “Cosmology with the SPHEREX All-Sky Spectral Survey,” arXiv:1412.4872, but the in-text description and likely BibTeX key are generic (“SPHEREx satellite”) rather than reflecting the actual title and first author; the real title and lead author are explicitly “Cosmology with the SPHEREX All-Sky Spectral Survey” by Olivier Doré *et al.*.[2]  

**Fix (nit):** Ensure the BibTeX entry for `SPHEREx2014` has title “Cosmology with the SPHEREX All-Sky Spectral Survey” and first author Doré, and adjust the first in-text mention to something like “the SPHEREx all-sky spectral survey (Doré *et al.* 2014)” so that title and authors match the real paper.[2]  


## PAPER-PER-B3 — UMAP reference correct but under-specified

**Location:** SDSS clustering section and taxonomy appendix: “UMAP~\cite{McInnes2018}”.  

**Issue:** The cited method is UMAP, and the paper is “UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction” by McInnes, Healy, and Melville, arXiv:1802.03426; this matches what is claimed, but the LaTeX source never gives the full title or arXiv identifier, making it harder to verify and potentially ambiguous with later UMAP-related works.[3]  

**Fix (nit):** In the bibliography, make sure the title is exactly “UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction” with the three authors and include the arXiv identifier 1802.03426; optionally, spell out “Uniform Manifold Approximation and Projection (UMAP; McInnes *et al.* 2018)” at first mention to tie the acronym unambiguously to the cited paper.[3]  


## PAPER-PER-B4 — NANOGrav new-physics paper correctly cited but slightly mis-described

**Location:** NANOGrav bounce-consistency section and PTA appendix: citation to “NANOGrav new-physics companion paper” / Afzal *et al.*  

**Issue:** The intended reference is “The NANOGrav 15-year Data Set: Search for Signals from New Physics,” arXiv:2306.16219, which indeed studies cosmic strings, scalar-induced GWs, phase transitions, etc., and compares to SMBHB scenarios, with Bayes factors in the 10–100 range in some models; this matches the paper’s stated scope and conclusions.[4] However, the current wording in the draft lightly paraphrases their conclusions as “Bayes factors in the range 10–100” without stating that these are conditional on SMBHB population modeling assumptions, which the Afzal *et al.* abstract explicitly stresses.[4]  

**Fix (minor):** Keep the citation but tighten the wording to mirror Afzal *et al.*: explicitly mention that the quoted Bayes factors depend strongly on SMBHB-population modeling assumptions and “should not be regarded as evidence for new physics,” matching the caveat language in their abstract.[4]  


## PAPER-PER-B5 — arXiv IDs and titles for key cosmology references are missing or implicit

**Location:** Introduction (bounce and non-Gaussianity references) and cosmology section; citations to Wands 2010, Cai 2009, Wilson-Ewing 2012, Munchmeyer 2019, Heinrich 2023, etc.  

**Issue:** Several core cosmology references are referred to only by author-year without explicit arXiv IDs or full titles in the LaTeX snippet; e.g. Wands (2010) is “Local non-Gaussianity from inflation,” Cai *et al.* (2009) “Non-Gaussianity in a matter bounce,” and the SPHEREx-class non-Gaussianity comparison “Constraining local non-Gaussianities with kinetic Sunyaev–Zel’dovich tomography” by Münchmeyer *et al.* (2019).[2][1] While the author-year mappings are correct, the absence of explicit titles/IDs in the bibliography risks confusion and makes auditing harder.  

**Fix (nit):** Ensure the BibTeX entries for these cosmology papers include their exact published titles and arXiv identifiers (e.g. Wands 2010 CQG 27 124002; Cai *et al.* 2009 JCAP 0905:011; Münchmeyer *et al.* 2019 Phys. Rev. D 100, 083508), and, where the text relies on a specific numerical forecast from a given paper, consider adding the arXiv ID inline at first mention for clarity.[1][2]  


## PAPER-PER-B6 — No blocker-grade citation-chain errors found

**Location:** Global (all external-paper citations audited above).  

**Issue:** For the sampled high-impact references, each cited paper exists with the claimed or compatible title, authors, and scope: Liang *et al.* 2023 on DESI BGS outliers,[1] Doré *et al.* 2014 on SPHEREx cosmology,[2] McInnes *et al.* 2018 on UMAP,[3] and Afzal *et al.* 2023 on NANOGrav new-physics interpretations.[4] No fused-metadata cases (e.g. title from one work plus arXiv ID from another) were found in these checks.  

**Fix (MAJOR/none):** No blocker-grade citation-chain failures were identified; the issues above are corrections and clarifications rather than fatal mis-citations. If you want to harden the paper further, expand a few key BibTeX records with explicit arXiv IDs and double-check that every arXiv key in the .bib resolves to the intended paper on arXiv.org or a journal site.[1][2][3][4]
