# P1A_v1A023 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0200pt_P1A_v1A023_R3_R-round_real
**Wall time**: 17.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=27442, completion=1580, total=29022

---

## PAPER-PER-B1 — Mis-cited “Freidel, Minic & Takeuchi 2005”

**Location:** Sec. 2.1, around “This construction builds on Freidel, Minic & Takeuchi~\cite{Freidel2005}”

**Issue:**  
The arXiv ID “Freidel2005” in the bibliography slot is described as a work “connecting the Barbero-Immirzi parameter to parity-violating interactions in LQG” and as the basis for ECH/Immirzi phenomenology with fermions, but the only 2005 Freidel paper in gr-qc with a natural BibTeX key “Freidel2005” is “A group field theory for 3d quantum gravity coupled to a scalar field” (Freidel–Oriti–Ryan), which (i) has different coauthors, (ii) does not involve Minic or Takeuchi, and (iii) does not discuss the Immirzi parameter or Holst parity-odd couplings to fermions. [0] This is fused metadata: the name triple “Freidel, Minic & Takeuchi” should correspond to “Physical effects of the Immirzi parameter”-type work (Perez–Rovelli or Mercuri), not to any existing “Freidel2005” entry.

**Fix (1–2 sentences):**  
Replace the “Freidel, Minic & Takeuchi~\cite{Freidel2005}” citation with the correct paper that actually derives an Immirzi-dependent four-fermion interaction (e.g. Perez & Rovelli, “Physical effects of the Immirzi parameter,” Phys. Rev. D73 (2006) 044013, arXiv:gr-qc/0505081) and update the BibTeX entry so that key, authors, title, and arXiv ID match. [3] Remove or correct any residual mention of “Minic & Takeuchi” unless you add a distinct, verified reference whose metadata matches those authors and topic.

---

## PAPER-PER-B2 — Mischaracterization of “Freidel2005” Content

**Location:** Sec. 2.1, same sentence as above and again in the acknowledgments (“fundamental derivations connecting the Barbero-Immirzi parameter to parity-violating interactions in LQG”)

**Issue:**  
The text attributes to “Freidel, Minic & Takeuchi” a result that “the Barbero-Immirzi parameter becomes physically observable through its coupling to fermionic matter,” which is in line with Perez & Rovelli (Phys. Rev. D73, 044013, arXiv:gr-qc/0505081) rather than with any Freidel paper matching the given 2005 gr-qc arXiv slot. [3] By contrast, gr-qc/0506067 (“A group field theory for 3d quantum gravity coupled to a scalar field,” Freidel–Oriti–Ryan) is about 3D group field theory and a scalar field, not Holst/Immirzi/fermion couplings, so using it as the “foundational derivation” is a content-level mis-citation. [0]

**Fix (1–2 sentences):**  
Cite Perez & Rovelli (gr-qc/0505081) for the claim that the Immirzi parameter yields a four-fermion interaction observable in principle, and ensure the bibliographic key used for that physics is not attached to Freidel–Oriti–Ryan’s 3D GFT paper. [3][0] If you wish to keep a Freidel reference for other reasons, add it separately with a distinct key and a description that matches its actual content (3D GFT with scalar, not Immirzi-fermion parity effects).  

---

## PAPER-PER-M3 — Cai et al. “Non-Gaussianity in a Matter Bounce” citation is incomplete/ambiguous

**Location:** Abstract and throughout (e.g. “property of the matter-bounce class~\cite{Cai:2009fn}”)

**Issue:**  
The paper key \cite{Cai:2009fn} is used for the canonical matter-bounce non-Gaussianity result (\(f_{\mathrm{NL}}=-35/8\)), which is indeed the standard result of the paper “Non-Gaussianity in a Matter Bounce” by Cai, Brandenberger, and Peter (astro-ph.CO, 2009). The arXiv record at 0903.0631, however, currently shows only a partial front page (title and abstract) with no author list or journal metadata visible in the HTML summary; the title matches, but without authors and journal reference in the snippet, a referee cannot confirm that your BibTeX entry (authors, year, journal) is fully accurate. [1]

**Fix (1–2 sentences):**  
Explicitly check your BibTeX entry for \cite{Cai:2009fn} against the full arXiv record for 0903.0631 (authors: Yi-Fu Cai, Wen Zhao, Robert Brandenberger, Xinmin Zhang; correct title and journal if any) and ensure that the key, author list, title, and arXiv ID are consistent. [1] If you are not giving a journal reference, remove any fabricated journal/volume/page metadata and leave it as an arXiv-only citation.

---

## PAPER-PER-M4 — Holst/Immirzi four-fermion origin mis-attributed from Mercuri to “Freidel2005”

**Location:** Sec. 2.1 (“This construction builds on Freidel, Minic & Takeuchi…”) and Sec. 2.2 (“motivated by the Holst+non-minimal-fermion construction of Mercuri~\cite{Mercuri2009}…”)

**Issue:**  
The Holst plus fermion story is split between a mis-labeled “Freidel2005” and Mercuri’s works. Mercuri 2009 and related Holst/Nieh–Yan papers indeed show that adding appropriate non-minimal couplings reconstructs the Nieh–Yan invariant and can make the Immirzi parameter classically unobservable, but they are distinct from Perez & Rovelli’s “Physical effects of the Immirzi parameter” which shows an observable four-fermion coupling. [3] As written, the manuscript implies that “Freidel, Minic & Takeuchi” provided the key Holst/Immirzi four-fermion effect, when in fact that derivation is due to Perez & Rovelli; Mercuri’s 2009 result is about the Immirzi parameter dropping out via Nieh–Yan completion, not about a surviving observable coupling.

**Fix (1–2 sentences):**  
Reassign credit so that Perez & Rovelli (gr-qc/0505081) are cited for the Immirzi-dependent four-fermion interaction, and Mercuri (2006/2009) is cited specifically for the Holst+non-minimal-fermion construction in which Nieh–Yan completion removes Immirzi from the classical dynamics. [3] Remove the “Freidel, Minic & Takeuchi” phrasing unless you add a verified paper by those authors that actually matches the described result.
