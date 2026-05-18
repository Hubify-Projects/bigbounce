# P1A_v1A032_R15 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1600pt
**Wall time**: 26.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28822, completion=1525, total=30347

---

## PAPER-CIT-1 — Incorrect Mercuri 2009 citation

**Issue (MAJOR, Sec. 2.1, around Eq. (Seff)):**  
You repeatedly cite “Mercuri 2009” for the Holst + non‑minimal fermion construction and Nieh–Yan reconstruction, but the bib tag `Mercuri2009` needs to resolve to the correct paper “Nieh–Yan invariant and fermions in Ashtekar–Barbero–Immirzi formalism” (Class. Quant. Grav. 26 (2009) 065005, arXiv:0901.2768), not to Mercuri’s 2006/2007 Holst papers or to a different 2009 work. Multiple LQG bibliographies show 2009 as Class.Quant.Grav. 26, 065005 with that title and arXiv:0901.2768. [2]

**Fix:**  
Ensure `Mercuri2009` in `references.bib` is mapped to arXiv:0901.2768 with the correct title, journal, year, and author list, and check in-text claims about Nieh–Yan cancellation and “Barbero–Immirzi drops out” match Mercuri’s actual statements (they do, but the metadata must be right). [2]

---

## PAPER-CIT-2 — Mis-specified Hehl–Datta reference

**Issue (MAJOR, Sec. 4.1, “HehlDattaNJL1971”):**  
You cite “HehlDattaNJL1971” as the standard reference for the torsion‑induced four‑fermion contact term. The historical NJL–type spin–torsion contact derivation is due to Hehl, von der Heyde, Kerlick, and Nester 1976 (“General Relativity with spin and torsion: Foundations and prospects”, Rev. Mod. Phys. 48, 393), and Popławski’s reviews cite that, not a 1971 Hehl–Datta paper with that NJL nomenclature. I cannot find any arXiv or journal record for a 1971 Hehl–Datta NJL torsion paper under that name. [3]

**Fix:**  
Replace the phantom “HehlDattaNJL1971” entry with the actual Einstein–Cartan torsion–NJL contact references (Hehl et al. Rev. Mod. Phys. 48 (1976) 393, plus related early EC papers), update the bibkey accordingly (e.g. `Hehl1976` already used), and adjust the text to reference that canonical source instead of a non-existent 1971 item. [3]

---

## PAPER-CIT-3 — Freidel–Minic–Takeuchi metadata needs tightening

**Issue (minor, Sec. 2.1 & 4, Freidel–Minic–Takeuchi):**  
You attribute to “Freidel, Minic & Takeuchi (2005)” the result that the Barbero–Immirzi parameter becomes physically observable via coupling to fermions. The standard reference is “Quantum gravity, torsion, parity violation and all that” (Phys. Rev. D72, 104002 (2005), arXiv:hep‑th/0507253). Your shorthand “Freidel2005” needs to point to that paper with exact title and hep‑th arXiv ID; there is no gr‑qc version. [4]

**Fix:**  
Verify that `Freidel2005` in your `.bib` is arXiv:hep‑th/0507253, Phys.Rev.D72:104002, with correct title and author list “Laurent Freidel, Djordje Minic, Tatsu Takeuchi,” and ensure no cross‑talk with other 2005 Freidel papers (e.g. on holography) in the same bib. [4]

---

## PAPER-CIT-4 — Cai & Brandenberger “Non-Gaussianity in a Matter Bounce”

**Issue (nit, multiple mentions of `Cai:2009fn`):**  
You correctly quote the key result \(\fnl=-35/8\) and treat it as a class‑level matter‑bounce prediction, but the metadata for `Cai:2009fn` must match the actual paper “Non-Gaussianity in a Matter Bounce” (Cai, Brandenberger, Zhang, JCAP 0905:011 (2009), arXiv:0903.0631). The arXiv page shows this precise title, author list and identifier. [5]

**Fix:**  
Check that `Cai:2009fn` is arXiv:0903.0631 with the JCAP 0905:011 journal ref and correct author list; if you currently list only “Cai & Zhu” or omit Zhang, fix the authors and journal metadata, but the in‑text scientific use is fine. [5]

---

## PAPER-CIT-5 — ABCK Immirzi/entropy reference should be arXiv:gr-qc/9710007

**Issue (nit, Eq. (gamma) and “ABCK1998”):**  
You call out “ABCK counting” for the Immirzi parameter and denote it `ABCK1998`. The canonical reference is “Quantum Geometry and Black Hole Entropy” by Ashtekar, Baez, Corichi, and Krasnov, Phys.Rev.Lett. 80 (1998) 904–907, arXiv:gr‑qc/9710007. The arXiv record confirms this title and author list. [2]

**Fix:**  
Make sure `ABCK1998` maps to arXiv:gr‑qc/9710007 with that exact title, author list and PRL reference; if you currently cite a different gr‑qc ID under that key, correct the fusion. [2]

---

## PAPER-CIT-6 — Perez–Rovelli “Physical effects of the Immirzi parameter”

**Issue (nit, Sec. 4 Route 2 & general discussion):**  
Route‑2 discussion relies on the claim that the Immirzi parameter induces a four‑fermion contact term; the standard paper is “Physical effects of the Immirzi parameter” by Alejandro Perez and Carlo Rovelli, Phys.Rev.D73 (2006) 044013, arXiv:gr‑qc/0505081, whose abstract explicitly states this. [1]

**Fix:**  
Check that your `PerezRovelli2005` (or equivalent) entry is gr‑qc/0505081 with title “Physical effects of the Immirzi parameter,” authors Perez & Rovelli, and PRD73:044013 as the journal ref; avoid mixing this metadata with unrelated gr‑qc 2005 entries. [1] 

---

No new BLOCKER‑grade citation errors surfaced; prior rounds’ heavy theory cleanup means the remaining issues are metadata hygiene rather than load‑bearing mis-citations.
