# P4_v1_0_109_R_INTERNAL R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1715pt
**Wall time**: 32.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=89682, completion=1779, total=91461

---

## PAPER-PER-B1 — Wrong citation for Iye et al. (2021)

**Location:** Abstract and multiple places in main text, cites `Iye et al. (2021)~\cite{Iye:2020}` as spin-parity paper on SDSS spirals.  

**Issue:** Bib entry `\bibitem{Iye:2020}` correctly refers to “Spin Parity of Spiral Galaxies III — Dipole Analysis of the Distribution of SDSS Spirals…” with arXiv:2011.00662 and ApJ 907, 123, but the body text sometimes glosses this as merely a “reading-direction bias finding” and occasionally implies a broader or different content (“spin-parity program to HSC WIDE Survey regions”; that extension is actually Iye & Yagi 2026). The core claim that Iye et al. 2021 present a SDSS dipole analysis and conclude consistency with random spin distribution is accurate. [1]  

**Severity:** minor  

**Fix:** Tighten the textual description to match the actual title and scope: explicitly say Iye et al. (2021) perform a dipole analysis of SDSS spirals, identify catalog duplication and human reading-direction bias, and conclude no significant spin-parity breaking; move the HSC-WIDE extension entirely to the Iye & Yagi (2026) citation and ensure those two papers are clearly distinguished.  

---

## PAPER-PER-B2 — Totally wrong arXiv ID for Tadaki et al. (2020)

**Location:** Abstract and §Introduction, citation `\cite{Tadaki:2020}` for “Tadaki et al. (2020) studied a smaller sample with HSC-SSP imaging and likewise found null results.”  

**Issue:** The bib entry `Tadaki:2020` is claimed to be an HSC-SSP spin-parity / chirality paper, but the arXiv ID actually used in earlier drafts (and still implied by the label) was 2006.02331, which is “Making Graphene Nano Inductor Using Table Top Laser Engraver,” unrelated to galaxy morphology or cosmology. [2]  

**Severity:** BLOCKER  

**Fix:** Replace the spurious graphene-physics arXiv reference with the correct Tadaki et al. HSC-SSP spiral-spin / chirality paper (correct authors, title, journal, and arXiv ID from ADS/arXiv), or if no such paper exists under that author/year, remove or reframe the claim as “unpublished / private communication” or drop it entirely. Then ensure the bib entry `\bibitem{Tadaki:2020}` points to the real HSC-SSP spin-parity work, not arXiv:2006.02331.  

---

## PAPER-PER-B3 — Fused metadata in Ivezic/LSST citation

**Location:** §Future Directions, LSST discussion; bib item `\bibitem{Ivezic:2019}`.  

**Issue:** The text says the bib formerly fused arXiv:0805.2366 with ApJ 873, 111 and that this is now “cleaned,” but the actual reference still implies that 0805.2366 is the preprint of the ApJ 873, 111 “LSST: From science drivers…” paper. In reality, arXiv:0805.2366 is the older LSST Science Book white paper, not the direct preprint/version of the 2019 ApJ article. Treating them as a single paper conflates two distinct works. [1]  

**Severity:** MAJOR  

**Fix:** Make the citation unambiguous: either (1) cite only the ApJ 873, 111 article with its DOI and omit the arXiv ID, or (2) give two distinct entries, one for the Science Book (arXiv:0805.2366) and one for the ApJ 2019 paper, and adjust in-text references so each statement cites the correct one. Avoid implying that 0805.2366 is the preprint of the ApJ article.  

---

## PAPER-PER-B4 — Ambiguous / partly incorrect description of the Motloch & Pen result

**Location:** §Motloch & Pen (2021), around “Motloch & Pen (2021) report an observed correlation between galaxy spins and the large-scale tidal field… using Galaxy Zoo 2… interpret their marginal (~2σ) signal as evidence for a physical spin–tidal-field correlation.”  

**Issue:** The cited paper (Motloch & Pen, Nature Astronomy 5, 283, arXiv:2003.04325) indeed studies spin–tidal-field correlations, but it does not frame the result simply as a “marginal (~2σ)” detection; the Nature Astronomy article emphasizes an “observed correlation” at higher significance and does not itself attribute the signal mainly to reading-direction biases (that critique comes from Iye et al. and others). The current wording downplays the stated significance and blends in later critique as if part of the original paper. [1]  

**Severity:** minor  

**Fix:** Rephrase to: (i) quote Motloch & Pen’s own stated detection significance and characterization (e.g., “detected correlation between galaxy spins and the reconstructed tidal field”), and (ii) clearly separate your interpretation/concern about GZ reading-direction biases and Iye et al.’s critique as your commentary, not as part of Motloch & Pen’s claims.  

---

## PAPER-PER-B5 — Over-stated link between this null and primordial parity-odd parameters

**Location:** §Mapping the bound onto cosmological parity-violating sectors (§\ref{sec:parity_translation}) and associated discussion of Lue–Wang–Kamionkowski, Cabass–Ivanov–Philcox, parity-odd 4PCF, etc.  

**Issue:** The text is mostly careful but occasionally drifts into implying that the chirality-dipole null directly constrains primordial quantities like the gravitational-wave chirality parameter Π or EFT-of-inflation couplings g\_* in nearly the same sense as CMB birefringence or the galaxy 4PCF analyses; the cited papers (e.g. Lue et al. 1999, Cabass et al. 2023) treat explicitly different observables and do not provide a transfer function for projected late-time morphology dipoles. [1]  

**Severity:** minor  

**Fix:** Add a blunt sentence that this work does not compute any quantitative mapping from the morphology dipole bound to Π, g\_*, or similar parameters, and that the references are conceptual analogs only; remove or soften any phrasing that could be read as claiming a direct numerical constraint on those primordial parity-odd couplings.  

---

## PAPER-PER-N1 — Missing or ambiguous explicit reference for “Tadaki et al. HSC-SSP null” summary

**Location:** Abstract sentence “the present work’s contribution… complements the prior nulls from Iye et al. (2021)… and Tadaki et al. (2020) on independent surveys” and §Comparison with Previous Work where Tadaki is characterized as an HSC-SSP chirality null.  

**Issue:** There is no verified arXiv or journal record matching “Tadaki et al. 2020 HSC-SSP chirality/spin-parity null,” and the current `\bibitem{Tadaki:2020}` is mis-bound to an applied-physics inductor paper. Until the correct cosmology paper is identified, the Tadaki citation is effectively unsupported, and readers cannot trace the supposed HSC-SSP chirality null. [2]  

**Severity:** MAJOR  

**Fix:** Either (1) identify and cite the correct HSC-SSP spin-parity / chirality paper by Tadaki et al. (correct arXiv and journal data from ADS), or (2) if no such publication exists, remove the Tadaki null claim from the abstract and comparison section and state explicitly that, at present, the only fully documented independent survey-level chirality null with parity-bias discussion is Iye et al. (and any others you can correctly cite).
