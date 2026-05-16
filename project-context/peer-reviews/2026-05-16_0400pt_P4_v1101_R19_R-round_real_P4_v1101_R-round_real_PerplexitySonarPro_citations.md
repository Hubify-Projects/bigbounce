# P4_v1101 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0400pt_P4_v1101_R19_R-round_real
**Wall time**: 24.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=83966, completion=1576, total=85542

---

## PAPER-PER-B1 – CE-ResNet citation (Jia et al. 2023)

**Location**: Sec. “Introduction”, 3rd paragraph; Sec. 2.2 “Training Labels”; Table/bib entry `\cite{Jia:2023}`.  

**Issue**: The paper correctly cites arXiv:2210.04168 as “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network” by He Jia, Hong‑Ming Zhu, and Ue‑Li Pen, ApJ 943, 32, DOI 10.3847/1538‑4357/aca8aa.[1] The LaTeX source explicitly notes that earlier drafts had wrong initials, page, and DOI suffix and claims these are now corrected; that statement is accurate and internally consistent with the ADS/arXiv record.[1] No fused metadata or wrong IDs remain, so there is **no blocker‑grade problem left here**.  

**Classification**: nit (closure note; not a problem to fix)  

**Fix**: None needed; you can optionally trim the long in‑text “NOTE (v1.0.78…)” about past errors from the main bib comment to keep the bibliography lean, but the core citation is correct.


## PAPER-PER-B2 – Iye et al. (2021) spin‑parity paper

**Location**: Abstract and Introduction, several mentions of “Iye et al. (2021) [\cite{Iye:2020}]”.  

**Issue**: The manuscript cites Iye, Yagi & Fukumoto’s SDSS spin‑parity paper with arXiv:2011.00662 and describes it as an ApJ paper analyzing SDSS spirals and concluding the cleaned catalog is consistent with random spins.[2] That matches the arXiv record “Spin Parity of Spiral Galaxies III -- Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations”, authors Masanori Iye, Masafumi Yagi, Hideya Fukumoto, ApJ, DOI 10.3847/1538‑4357/abb3bb.[2] The label `\cite{Iye:2020}` in the .tex is technically year‑mismatched (2021 ApJ vs “2020” tag) but this is a bibkey naming convention, not public metadata; title, authors, journal and arXiv ID are all correct.  

**Classification**: nit  

**Fix**: Optionally rename the BibTeX key from `Iye:2020` to something like `Iye:2021ApJ` to avoid confusion; no change to the cited content is required.


## PAPER-PER-B3 – Land et al. (Galaxy Zoo spin statistics) metadata

**Location**: Sec. 2.2 GZ1 discussion and Sec. 3.4 bias / reading‑direction paragraphs; bib entry `\cite{Land:2008}`.  

**Issue**: The paper references Land et al. as the Galaxy Zoo spin‑statistics null result showing that, after correcting for bias, the winding sense is consistent with isotropy.[3] ArXiv:0803.3247 “Galaxy Zoo: The large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey” by Kate Land et al., MNRAS, DOI 10.1111/j.1365‑2966.2008.13490.x, matches exactly this description.[3] Author list, title, arXiv ID and venue are correct, and the scientific summary is faithful.  

**Classification**: nit (confirmed clean)  

**Fix**: None; citation is correct and consistent with the source.


## PAPER-PER-M1 – SpArcFiRe paper (Davis & Hayes) metadata

**Location**: Sec. “SpArcFiRe” and related discussion; bib entry `\cite{Davis:2014}`.  

**Issue**: The manuscript cites an automated spiral arm finder SpArcFiRe as ApJ 790, 87 (2014) with arXiv:1402.1910, describing it as “SpArcFiRe: Scalable Automated Detection of Spiral Galaxy Arm Segments”. ADS confirms ApJ 790, 87 (2014), bibcode 2014ApJ...790...87D, arXiv:1402.1910, with that title and authors including D. R. Davis.[4] The text also notes that earlier drafts had the wrong arXiv ID; the current combination (title + arXiv + journal) is now correct.[4]  

**Classification**: minor (because the text narrates prior confusion; current metadata are correct)  

**Fix**: You might shorten the historical “GPT flagged old ID” comment in the bib note to avoid distracting from the now‑correct citation, but no scientific correction is required.


## PAPER-PER-M2 – Houston’s own metadata about “fixed bad citations”

**Location**: Several inline “NOTE (v1.0.xx)” comments around Jia et al., SpArcFiRe, LSST, etc.  

**Issue**: The manuscript embeds meta‑narrative statements like “GPT‑Pro … caught that the prior DOI suffix … was wrong; corrected here” and “Perplexity Sonar Pro flags … were therefore reasonable”. These are accurate about the state of the external papers (e.g., Jia 2023 and Davis 2014 are now correctly cited)[1][4], but they introduce tool‑specific chatter into the scientific text, and risk confusing readers about whether the *current* citations are stable.  

**Classification**: minor  

**Fix**: Remove explicit references to prior LLM/tool mistakes and to particular vendors (“GPT‑Pro”, “Gemini”, “Perplexity Sonar Pro”) from the main narrative and bibliography comments. Replace them with a neutral sentence like “Earlier drafts mis‑stated the DOI; this version uses the corrected ApJ DOI 10.3847/1538‑4357/aca8aa” where you feel historical clarification is needed.


## PAPER-PER-M3 – LSST/Ivezić reference (potential fused arXiv vs journal confusion)

**Location**: Bibliography entry `\cite{Ivezic:2019}` and associated note.  

**Issue**: The paper now cites Ivezić et al. LSST reference design as ApJ 873, 111 (2019), DOI 10.3847/1538‑4357/ab042c, and explicitly notes that the older LSST Science Book arXiv:0805.2366 is a distinct white paper.[5] That is correct: arXiv:0805.2366 is not the preprint of the 2019 ApJ reference‑design paper, so the current decision to drop that arXiv ID from the ApJ citation avoids a fused‑metadata error.[5]  

**Classification**: nit  

**Fix**: None; the corrective note in the bib item is appropriate and the current metadata (ApJ 873, 111; DOI 10.3847/1538‑4357/ab042c; no arXiv ID attached to that journal article) are correct.[5]
