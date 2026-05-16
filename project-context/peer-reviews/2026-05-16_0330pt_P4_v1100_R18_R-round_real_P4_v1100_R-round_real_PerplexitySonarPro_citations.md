# P4_v1100 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0330pt_P4_v1100_R18_R-round_real
**Wall time**: 23.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=83994, completion=1390, total=85384

---

## PAPER-PER-B1 — Mis-cited Motloch & Pen paper

**Location:** Sec. \ref{sec:motloch}, near “Motloch & Pen (2021)”.

**Issue:** The text attributes a galaxy-spin–tidal-field correlation result to “Motloch & Pen (2021)” and cites it as [\cite{Motloch:2021}], but the arXiv ID 2003.04325 (currently in the bib as Motloch:2021) is a different paper by Cartwright, titled *“Entropy production far from equilibrium in a chiral charged plasma in the presence of external electromagnetic fields”*.[1] This is a fused metadata error (correct authors/title/venue are not those of the cited paper).

**Fix (MAJOR):** Replace the incorrect bib entry for `\cite{Motloch:2021}` with the correct Motloch & Pen spin–tidal-field paper (check ADS/arXiv for the correct arXiv ID and journal info), and ensure that arXiv ID, title, authors, and journal all match that paper, not Cartwright’s holographic plasma article.[1]  


## PAPER-PER-B2 — DESI Legacy overview citation OK

**Location:** Sec. \ref{sec:images}, first paragraph citing Dey et al. (2019) as \cite{Dey:2019}.

**Issue:** The paper claims to use “DESI Legacy Imaging Surveys DR8” and cites Dey et al. (2019) “Overview of the DESI Legacy Imaging Surveys” with arXiv:1804.08657 and AJ publication.[2] ArXiv 1804.08657 indeed corresponds to that title, with lead author Arjun Dey, and the abstract and journal (AJ) match the description in the manuscript.[2]

**Fix (nit):** None strictly required; the citation is consistent. If desired, you could explicitly align the journal reference with the AJ DOI given on arXiv (10.3847/1538-3881/ab089d) to make the bib entry fully standard.[2]  


## PAPER-PER-B3 — CE-ResNet citation and DOI OK

**Location:** Secs. \ref{sec:intro}, \ref{sec:ceresnet}; citation \cite{Jia:2023}.

**Issue:** The manuscript cites Jia et al. as “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” arXiv:2210.04168, ApJ, DOI 10.3847/1538-4357/aca8aa.[3] ArXiv 2210.04168 has exactly this title, author list (He Jia, Hong‑Ming Zhu, Ue‑Li Pen), ApJ acceptance, and matching DOI.[3]

**Fix (nit):** None; this citation is correct and internally consistent. Just ensure the bib entry’s year and journal volume/page (ApJ 943, 32) are included, matching the published version linked from the arXiv record.[3]  


## PAPER-PER-B4 — Iye et al. 2021 citation OK

**Location:** Abstract and Secs. \ref{sec:intro}, \ref{sec:comparison}; citation \cite{Iye:2020}.

**Issue:** The paper refers to Iye et al. (2021), “Spin Parity of Spiral Galaxies III – Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations”, arXiv:2011.00662, ApJ, DOI 10.3847/1538-4357/abb3bb.[4] ArXiv 2011.00662 indeed has that title, authors (Masanori Iye, Masafumi Yagi, Hideya Fukumoto), and ApJ DOI, matching the manuscript’s description.[4]

**Fix (nit):** None required; the arXiv ID, title, author list and journal mapping are all correct. If you want strict consistency, ensure the bib year is 2021 (ApJ publication year) while the arXiv tag remains 2020.1100662.[4]  


## PAPER-PER-B5 — DESI Legacy / DR8 description matches Dey et al.

**Location:** Sec. \ref{sec:images}, description of DESI Legacy Imaging Surveys DR8 as combination of DECaLS, BASS, MzLS, footprint, grz bands, and WISE.

**Issue:** The text states that DR8 is composed of the DECaLS, BASS, and MzLS imaging campaigns, covering ≈14,000 deg² in g, r, z, with WISE mid‑IR photometry; this is exactly the summary given in Dey et al. 2019, arXiv:1804.08657.[2] There is no sign of LLM-fused or fabricated survey description.

**Fix (nit):** None; this is a faithful, compressed description of Dey et al.’s abstract and survey overview.[2]  


## PAPER-PER-B6 — No other obvious fused‑metadata in checked external citations

**Location:** External-citation cluster around CE-ResNet, DESI Legacy, and Iye et al., as above.

**Issue:** For the arXiv entries checked (2210.04168, 1804.08657, 2011.00662), titles, authors, topics, and journal venues match the claims in the manuscript; no case was found where a title from one paper was paired with the ID of another, except the mis-assigned Motloch & Pen slot discussed in PAPER-PER-B1.[1][2][3][4]

**Fix (minor):** After correcting the Motloch & Pen citation, run a quick audit pass over any remaining arXiv IDs not covered here (e.g., spin-parity and SpArcFiRe references) to ensure their IDs resolve to papers whose title/author/journal lines match what the manuscript claims. This is a general housekeeping step rather than a specific error.  

---

If you want, I can next systematically step through the full bibliography and build a checklist of “ID ↔ title ↔ authors ↔ journal” matches, but that will require enumerating each bib item from the source.  


