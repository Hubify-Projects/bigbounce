# P1A_v1A024 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0930pt_P1A_v1A024_R4_R-round_real
**Wall time**: 24.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=27449, completion=1587, total=29036

---

## PAPER-PER-B1 — Mis-cited “Freidel, Minic & Takeuchi 2005”

**Location:** Sec. 2.1, around Eq. (2.1), citations `\cite{Freidel2005}` and later text describing “Freidel, Minic & Takeuchi”.

**Issue:**  
The paper attributes the physical Immirzi–fermion coupling and the statement that the Immirzi parameter becomes observable through its coupling to fermions to “Freidel, Minic & Takeuchi 2005,” cited as `Freidel2005`.[1] The canonical 2005 paper establishing that the Immirzi parameter determines a four‑fermion coupling is actually Perez & Rovelli, “Physical effects of the Immirzi parameter,” Phys. Rev. D 73, 044013 (2006), arXiv:gr‑qc/0505081.[2] The arXiv entry gr‑qc/0506067 by Freidel et al. is “A group field theory for 3d quantum gravity coupled to a scalar field” and does not contain the Immirzi–fermion four‑fermion result claimed here.[1][2]

**Fix (1–2 sentences):**  
Replace the “Freidel, Minic & Takeuchi” reference with the correct Perez & Rovelli citation and adjust the text accordingly (e.g., “as shown by Perez & Rovelli…”). Ensure that the `Freidel2005` bib entry is either corrected to Perez & Rovelli, Phys. Rev. D 73 (2006) 044013, arXiv:gr‑qc/0505081, or that a new key is added and used consistently.[2]  


## PAPER-PER-M1 — Mercuri 2009 / Nieh–Yan description slightly mis-phrased

**Location:** Sec. 2.1.3, paragraph “Motivated by the Holst+non-minimal-fermion construction of Mercuri~\cite{Mercuri2009}…”.

**Issue:**  
The text says Mercuri “shows that the Nieh–Yan invariant is reconstructed and the Barbero–Immirzi parameter drops out of the classical dynamics,” which matches the content of Mercuri’s short 2006/2007 paper “Nieh-Yan Invariant and Fermions in Ashtekar-Barbero-Immirzi Formalism,” arXiv:gr‑qc/0610026.[3] However, the in-text year “2009” suggests the journal version, while the arXiv ID 0610026 corresponds to 2006/2007; if the bib entry actually points to that preprint, the year or label “2009” is misleading and risks fused metadata for readers trying to locate “Mercuri 2009” on arXiv.[3]

**Fix (1–2 sentences):**  
Align the in-text citation label with the actual reference: either call it “Mercuri (2007)” and keep arXiv:gr‑qc/0610026, or update the bib entry to the correct 2009 journal reference if that is what is meant.[3] Make sure the arXiv ID, year, and venue for `Mercuri2009` are mutually consistent.  


## PAPER-PER-m2 — Overly strong claim about Mercuri’s result

**Location:** Sec. 2.1.3, same Mercuri sentence.

**Issue:**  
Mercuri (arXiv:gr‑qc/0610026) shows that adding a specific non‑minimal fermion term makes the Holst term plus the non‑minimal piece combine into the Nieh–Yan density so that the Immirzi parameter does not affect the classical equations of motion in that setup.[3] The current wording could be read as a completely general statement about “the” Ashtekar–Barbero–Immirzi formalism with fermions, which is stronger than what is actually proven (it relies on a chosen non‑minimal coupling and classical level).[3]

**Fix (1–2 sentences):**  
Qualify the statement to read, for example: “Mercuri shows that, for a specific non‑minimal fermion coupling, the Holst term and the non‑minimal contribution reconstruct the Nieh–Yan invariant so that the Immirzi parameter drops out of the classical dynamics in that setup.”[3] This keeps the claim within the scope of the cited result.  


## PAPER-PER-m3 — Missing core citation for Immirzi–fermion four‑fermion term

**Location:** Sec. 2.1.2, Eq. (2.4) and surrounding discussion of the Hehl–Datta / four‑fermion contact term and Immirzi dependence.

**Issue:**  
The text discusses the four‑fermion contact interaction in the presence of Holst/Immirzi structure and later connects it to a parity‑odd effective coupling, but it does not explicitly cite Perez & Rovelli’s “Physical effects of the Immirzi parameter” (arXiv:gr‑qc/0505081), which is the standard reference showing that the Immirzi parameter becomes observable via such a four‑fermion term.[2] Omitting this while attributing the physical Immirzi effect elsewhere (to “Freidel, Minic & Takeuchi”) misdirects readers and weakens the citation chain.[1][2]

**Fix (1–2 sentences):**  
Add an explicit citation to Perez & Rovelli, Phys. Rev. D 73 (2006) 044013, arXiv:gr‑qc/0505081, when stating that the Immirzi parameter determines a four‑fermion coupling and becomes observable in the presence of fermions.[2] This should replace or supplement the incorrect `Freidel2005` attribution.  


## PAPER-PER-n1 — Minor: ambiguous “Freidel2005” label

**Location:** Throughout where `Freidel2005` is cited as “Freidel, Minic & Takeuchi”.

**Issue:**  
The arXiv paper gr‑qc/0506067 by Freidel et al. is titled “A group field theory for 3d quantum gravity coupled to a scalar field,” which does not match the implied topic (“Barbero-Immirzi parameter becomes physically observable through its coupling to fermionic matter”).[1] Even after correcting the physics attribution to Perez & Rovelli, leaving a `Freidel2005` key in the bibliography without a clear role risks confusion because the title and content don’t line up with how it is currently described.[1]

**Fix (1–2 sentences):**  
If you still need to cite Freidel et al. 2005, update the text to describe it correctly as a 3D group field theory model coupled to a scalar field and ensure the title and arXiv ID (gr‑qc/0506067) are correctly given in the references.[1] Otherwise, remove this citation entirely to avoid fused or misleading metadata.  

---

I did not find any additional blocker‑grade citation-chain problems beyond the misattributed “Freidel, Minic & Takeuchi” result; no arXiv IDs I checked were outright nonexistent, and the Mercuri and Perez–Rovelli entries are real with correct IDs and titles once the metadata is aligned.[1][2][3]
