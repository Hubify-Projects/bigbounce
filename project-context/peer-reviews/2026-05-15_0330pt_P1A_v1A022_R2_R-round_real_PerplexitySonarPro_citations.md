# P1A_v1A022_R2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0330pt
**Wall time**: 28.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=25989, completion=1853, total=27842

---

## PAPER-PER-B1 — Mis-cited “Freidel2005” (wrong paper, wrong claim)

**Location:** Sec. 2.1, around Eq. (2) and the paragraph “This construction builds on Freidel, Minic & Takeuchi~\cite{Freidel2005}…”

**Issue (BLOCKER):**  
The paper cites “Freidel, Minic & Takeuchi~\cite{Freidel2005}” in support of the statement that the Barbero–Immirzi parameter becomes physically observable via its coupling to fermions in Einstein–Cartan–Holst theory, but the arXiv entry gr-qc/0506067 (“A group field theory for 3d quantum gravity coupled to a scalar field” by Freidel, Oriti, Ryan) is a 3d group field theory for gravity plus a scalar and does not discuss the Barbero–Immirzi parameter, Holst term, or fermionic couplings at all.[1] This is fused metadata: the authors, title, content, and venue do not match the claimed result.

**Fix:**  
Replace this citation with an actual ECH/Holst+fermions reference (e.g. Freidel–Minic–Takeuchi’s Holst/Immirzi paper if it exists under a different arXiv ID, or another standard source), and ensure the BibTeX entry for `Freidel2005` has correct authors, title, arXiv ID, and journal; if no suitable Freidel–Minic–Takeuchi paper exists, drop that name and cite Mercuri or similar instead, explicitly correcting the earlier misattribution.[1]  


## PAPER-PER-M1 — Misaligned “Mercuri2009” scope vs. citation

**Location:** Sec. 2.1.2, “Derivation of the Parity-Odd Term”, especially the sentence “Following Mercuri~\cite{Mercuri2009}, the effective action acquires a parity-odd term: …”

**Issue (MAJOR):**  
The citation Mercuri 2009 (gr-qc/0610026, “Nieh–Yan Invariant and Fermions in Ashtekar–Barbero–Immirzi Formalism”) shows that adding a non‑minimal fermion term plus Holst reconstructs the Nieh–Yan invariant and removes Immirzi dependence from the classical dynamics, but it does not derive an effective low‑energy parity‑odd term of the form \(S_{\rm eff} = (\alpha/M)\int e\wedge e\wedge\mathcal F\) with a phenomenological mass scale \(M\) and coupling \(\alpha\) as written here.[0] The text blends Mercuri’s topological/Nieh–Yan construction with a new, phenomenologically parameterized operator; attributing that specific EFT form directly to Mercuri overstates what the cited paper actually does.

**Fix:**  
Rephrase this as: Mercuri shows that Holst + a non‑minimal fermion term reconstruct the Nieh–Yan invariant and that Immirzi drops out of the classical dynamics,[0] and then clearly introduce Eqs. (Seff, Seff_comp) as your own phenomenological parity‑odd ansatz motivated by that structure rather than as something “acquired” directly in Mercuri’s paper.  


## PAPER-PER-m2 — Holst / Nieh–Yan literature under-cited around perturbation transparency

**Location:** Sec. 10, “The Perturbation-Transparency Result”, especially the general statement “This generalizes Hehl et al. (1976)… to the Holst sector…”

**Issue (minor):**  
The text asserts that the Holst dual contraction vanishes by the Bianchi identity and that the Holst term is topological/inert on torsion‑free backgrounds, but while Hehl et al. (1976) cover Einstein–Cartan with spin, they do not treat the Holst/Nieh–Yan structure.[0] Mercuri’s 2007 paper explicitly shows that Holst + a non‑minimal term reconstructs Nieh–Yan and clarifies that Immirzi is dynamically irrelevant in the torsion‑free sector,[0] which is exactly the Holst‑sector ingredient you are invoking but not crediting here.

**Fix:**  
Augment the transparency statement with a precise citation to Mercuri for the Holst/Nieh–Yan part (e.g. “…torsion-free, so the Holst term reduces to a Nieh–Yan boundary term and is dynamically inert,[0] cf. Mercuri (2007)”), and reserve Hehl et al. (1976) for the spin–torsion Einstein–Cartan side only.  


## PAPER-PER-m3 — “Holst1996” not clearly tied to its actual content

**Location:** Sec. 4.2, Route 2 discussion: “At the classical level the Holst term … reduces to the Nieh–Yan density on shell once torsion is integrated out~\cite{Holst1996,Freidel2005}.”

**Issue (minor):**  
Holst’s original paper “Barbero’s Hamiltonian derived from a generalized Hilbert–Palatini action” (Phys. Rev. D 53, 5966–5969, 1996) introduces the Holst term and shows its classical equivalence to GR in vacuum, but it does not itself discuss Nieh–Yan or fermions in the modern Mercuri sense.[0] As written, you are using Holst 1996 as if it were a primary reference for the Nieh–Yan reduction and torsion-elimination map; that role is more accurately played by later Holst+fermions/Nieh–Yan papers.

**Fix:**  
Tighten the attributions: cite Holst 1996 specifically for introducing the Holst action and showing its classical equivalence to GR, and cite Mercuri 2007 (and other Nieh–Yan-focused works) for the “reduces to Nieh–Yan on shell with torsion” statement, removing the implication that Holst’s original article contains the Nieh–Yan result.[0]  


## PAPER-PER-n4 — Incomplete bibliographic metadata note for “Freidel2005”

**Location:** Multiple: Sec. 2.1 (“This construction builds on Freidel, Minic & Takeuchi…”), Sec. 4, and Related Work where Freidel et al. are cited as foundational Holst/Immirzi references.

**Issue (nit):**  
Given that arXiv:gr‑qc/0506067 is actually a different Freidel paper (Freidel–Oriti–Ryan, 3d GFT with scalar matter)[1] and there is no indication in the text which exact Holst/Immirzi paper is meant, the current `Freidel2005` label is ambiguous and prone to future mis‑citation in downstream work.

**Fix:**  
Explicitly state in the bibliography (or a brief footnote) the full, correct metadata for the intended Freidel–Minic–Takeuchi Holst/Immirzi reference (title, journal, arXiv ID if available), and note that earlier drafts mis‑aligned this with gr‑qc/0506067; this makes the correction audit‑trail explicit and prevents propagation of the fused citation.[1]  


## PAPER-PER-n5 — Bibliography audit scope not fully satisfied in text

**Location:** Global, per stated “bib metadata audit (Freidel2005, Mercuri2009, Holst1996 should be checked).”

**Issue (nit):**  
You explicitly flag an internal requirement to audit Freidel2005, Mercuri2009, and Holst1996 metadata; while Mercuri’s arXiv ID, title, and authors are correct,[0] and Holst1996 is a standard, correctly-labeled reference in the literature, the Freidel2005 entry is currently mis‑matched to an unrelated 3d GFT paper as noted above.[1] The manuscript does not record the outcome of this audit or the correction, even though other cross‑vendor‑round fixes are logged explicitly.

**Fix:**  
Add a brief note (e.g. in the version‑history paragraph or in the acknowledgments) stating that the Freidel2005 bib entry was corrected in v1A.0.23 after a metadata audit (Mercuri2009 and Holst1996 verified; Freidel2005 realigned), so that the paper’s internal “bib metadata audit” goal is demonstrably satisfied in‑text.[0][1]  


