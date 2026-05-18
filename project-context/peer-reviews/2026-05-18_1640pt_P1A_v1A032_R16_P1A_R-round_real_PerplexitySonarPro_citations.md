# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1640pt_P1A_v1A032_R16
**Wall time**: 29.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28726, completion=1701, total=30427

---

## PAPER-PER-B1 — Mis-cited Freidel–Minic–Takeuchi paper

**Classification:** BLOCKER  

**Location:** Sec. 2.1 “Einstein-Cartan-Holst Action”, around “…Freidel, Minic & Takeuchi~\cite{Freidel2005}…”  

**Issue:**  
The citation key `\cite{Freidel2005}` is described as “Freidel, Minic & Takeuchi” and used for the Barbero–Immirzi parameter becoming observable through fermionic couplings, but arXiv:gr-qc/0506067 is “A group field theory for 3d quantum gravity coupled to a scalar field” by Freidel, Oriti & Ryan, and does not involve Minic/Takeuchi or the Holst/Immirzi–fermion story claimed here.   

**Fix:**  
Replace the current `Freidel2005` entry with the correct Freidel–Minic–Takeuchi Holst/fermion paper (update authors, title, arXiv ID, and venue accordingly), or change the in‑text attribution and citation to a paper that actually contains the Barbero–Immirzi–fermion coupling result being invoked.  

---

## PAPER-PER-M1 — Incomplete / wrong “Planck2018params” metadata

**Classification:** MAJOR  

**Location:** Sec. 1 Introduction, first paragraph, `\cite{Planck2018params}`; also Table/Appendix where “Planck 2018” cosmological values are quoted.  

**Issue:**  
The text cites “Planck2018params” as the standard ΛCDM reference and uses numbers like \(H_0 = 67.68 \pm 1.06\) km/s/Mpc as a Planck-level baseline, but Planck 2018 results. VI. Cosmological parameters (Aghanim et al.) give \(H_0 = 67.4 \pm 0.5\) km/s/Mpc and related parameters with smaller uncertainties. [1] The paper attributes the looser values entirely to a companion analysis “Paper I(b)” but the current wording in several places reads as if they are Planck-2018-like baseline numbers, which is misleading. [1]  

**Fix:**  
Ensure the bibliography entry for `Planck2018params` explicitly points to arXiv:1807.06209 / A&A 641 A6, and in the main text clearly distinguish Planck 2018 baseline values from the author’s own MCMC outputs (e.g., “our chains give \(H_0=67.68\pm1.06\), consistent with the Planck 2018 value \(67.4\pm0.5\) km/s/Mpc [Planck Coll. 2018]”). Do not imply the broader-error numbers are Planck’s.  

---

## PAPER-PER-M2 — Ambiguous or incorrect Holst/Immirzi references

**Classification:** MAJOR  

**Location:** Secs. 2.1–2.2, multiple mentions of Holst term, Nieh–Yan, and Barbero–Immirzi running attributed broadly to `\cite{Freidel2005,Mercuri2009,MercuriCapozziello2008,ShapiroTeixeira2014}`.  

**Issue:**  
The paper repeatedly ascribes specific results (e.g., “Freidel, Minic & Takeuchi established that the Barbero–Immirzi parameter becomes physically observable through its coupling to fermionic matter”; “Mercuri & Capozziello one-loop coefficient \(\alpha_{\rm em}/(4\pi)\) in Eq.~(ref)”) without a clean mapping to real titles/arXiv IDs in the text, and at least one supposed Freidel–Minic–Takeuchi citation is actually a different Freidel paper with other co-authors and topic.  This strongly suggests some fused or mis-assigned metadata in the Holst/Immirzi reference cluster.  

**Fix:**  
Audit every Holst/Immirzi-related citation: for each claim (Immirzi observability with fermions, Nieh–Yan reconstruction, one‑loop running, parity-odd term) explicitly tie it to a verifiable paper (correct authors, title, journal, arXiv ID). Remove or correct any references where the author list/topic do not match the claim.  

---

## PAPER-PER-m1 — Vague / nonstandard citation “Weinberg1989”

**Classification:** minor  

**Location:** Introduction, line “…cosmological constant problem~\cite{Weinberg1989}.”  

**Issue:**  
The classic reference is usually S. Weinberg, “The cosmological constant problem,” Rev. Mod. Phys. 61, 1–23 (1989). Many cosmology bibliographies either cite the RMP paper or arXiv:astro-ph/0005265 (Weinberg’s later review). The internal key “Weinberg1989” is fine, but if the bib entry points to an arXiv ID or title inconsistent with that standard reference, it will be confusing. [2]  

**Fix:**  
Verify that `Weinberg1989` in the .bib file is the RMP review (correct title, year, journal) or a clearly labeled later arXiv review, and adjust the in-text label if needed (e.g., “Weinberg’s review [Rev. Mod. Phys. 61, 1 (1989)]”).  

---

## PAPER-PER-m2 — DESI dark-energy references likely pointing to wrong or provisional IDs

**Classification:** minor  

**Location:** Introduction, “DESI 2024–2025 BAO results suggest dynamical dark energy…~\cite{DESI2024,DESI2025DR2}.”  

**Issue:**  
The labels “DESI2024” and “DESI2025DR2” are used as if they point to specific DESI BAO/dark-energy arXiv releases and a DR2 paper, but no arXiv IDs or titles are given in the excerpt. Without correct metadata, these might end up pointed at internal notes, whitepapers, or non-final drafts instead of the public DESI collaboration BAO/DR2 cosmology papers. [2]  

**Fix:**  
Ensure `DESI2024` and `DESI2025DR2` map to the actual DESI BAO/dark-energy and DR2 cosmology papers once available (correct DESI Collaboration author block, title, arXiv IDs). If currently citing private drafts, mark them as “DESI Collaboration, in preparation / private communication,” not as public “results.”  

---

## PAPER-PER-n1 — Non-standard “Golden2026P...” self-citation labels

**Classification:** nit  

**Location:** Throughout (e.g. “Paper~II, Ref.~\cite{Golden2026P2}”; “Paper~I(b)~\cite{Golden2026P1b}”; “Paper~III~\cite{Golden2026P3}”; “Paper~IV~\cite{Golden2026P4}”).  

**Issue:**  
The keys `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4` are used as if they correspond to separate public companion papers, but no titles, journals, or arXiv IDs are visible here. If these are not yet on arXiv, calling them “Paper I(b)/II/III/IV” without a concrete reference makes them hard to verify or locate.  

**Fix:**  
Once available, replace each `Golden2026P*` bib entry with a full citation (author, full title, arXiv ID and/or journal). Until then, clearly label them as “in preparation” or “submitted” and avoid wording that implies they are already-published arXiv entries.
