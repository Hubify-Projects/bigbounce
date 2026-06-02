# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 20.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29922, completion=1936, total=31858, search_context_size=low, cost={'input_tokens_cost': 0.08977, 'output_tokens_cost': 0.02904, 'request_cost': 0.006, 'total_cost': 0.12481}

---

## PAPER-PER-B1 — BLOCKER — Multiple fabricated/uncited external papers

**Location:** Bibliography entries `\bibitem{TWebDESI2026}`, `\bibitem{ASTRADESI2026}`, and their use in §X (“Concurrent-literature DR1/EDR cosmic-web cross-validation”).

**Issue:**  
Search on arXiv and ADS shows **no record** of the cited works:

- “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” arXiv:2604.02463, “DESI Collaboration”. No such arXiv ID or title exists; 2604.02463 is unassigned / unrelated.[1][2]  
- “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” Zapata‑Zuluaga et al. 2026, arXiv:2604.01456. No such arXiv ID or title exists; again no match on arXiv/ADS for title+author combination.[1][2]

Both are presented as real, public arXiv preprints and used as **external validation of the V‑Web DR1 run**, but they appear to be LLM-composed fusions (plausible titles + plausible authors + invented arXiv IDs), not actual papers.

**Fix:**  
Either (a) delete these references and all text claiming external validation by them, or (b) if these are real internal DESI notes, re‑label them explicitly as *internal/private* documents without arXiv IDs, remove phrases implying public publication, and drastically weaken the “independent publication-grade validation” language. Do not assign fabricated arXiv identifiers under any circumstance.


## PAPER-PER-B2 — BLOCKER — Misrepresentation / overclaim on DESIVAST status

**Location:** §“Concurrent-literature DR1/EDR cosmic-web cross-validation”, discussion of DESIVAST (Douglass et al. 2025), and earlier references to “current public DR1 cosmic-web catalogs”.

**Issue:**  
Douglass et al. (ApJ 982, 38, 2025) “DESIVAST: Catalogs of Low‑Redshift Voids using Data from the DESI Data Release 1 Bright Galaxy Survey” is a **void catalog on BGS DR1 only**, not a *general DR1 cosmic‑web classifier*.[DESIVAST2025] The manuscript repeatedly describes DESIVAST as “current public DR1 cosmic-web catalogs” and treats it as one of “three independent DR1 cosmic-web catalogs” alongside the fabricated T‑Web/ASTRA DR1 works, implying a broader, survey‑wide environment classification than DESIVAST actually provides. That overstates the scope of Douglass et al. relative to what the paper claims to do.

**Fix:**  
Rewrite the DESIVAST paragraphs to accurately describe it as a *BGS void catalog to z≲0.24* (VoidFinder + watershed algorithms) and remove language that lumps it with non‑existent full‑DR1 T‑Web/ASTRA environment VACs. Any claim of “three independent DR1 cosmic‑web catalogs” must be dropped; refer only to DESIVAST as a single, low‑z void catalog plus your own V‑Web run.


## PAPER-PER-M1 — MAJOR — ASTRA EDR citation appears fabricated / mismatched

**Location:** Bibliography `\bibitem{ASTRADESI2026}` and §“ASTRA EDR per-object cross-validation”.

**Issue:**  
The paper cites “D. C. Zapata‑Zuluaga, S. Guevara‑Montoya, V. Torres‑Gomez, J. Hernandez, and J. E. Forero‑Romero, ‘The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog’ (2026), arXiv:2604.01456.”Web search and arXiv/ADS queries show no such preprint, no matching title, and no such arXiv ID for those authors.[1][2] There *are* real cosmic‑web papers by Forero‑Romero et al., but not with this title, year, and arXiv number together — this looks like fused metadata rather than a real citation.

**Fix:**  
Verify whether an actual ASTRA‑DESI EDR environment catalog exists. If it does, replace the citation with the correct authors, title, year, and arXiv/journal information. If not, remove `\bibitem{ASTRADESI2026}` and all narrative that treats ASTRA as an already‑published DESI EDR VAC; if you used private code or an internal catalog, label it as such and do not attach a fabricated arXiv ID or publication status.


## PAPER-PER-M2 — MAJOR — Overstated “publication-grade” external validation

**Location:** §“Concurrent-literature DR1/EDR cosmic-web cross-validation”, especially:  
> “We therefore treat Ref.~\cite{TWebDESI2026} as a publication-grade independent external validation of the V-Web run that produced this paper's headline result.”

**Issue:**  
Given that `\cite{TWebDESI2026}` is not a real, publicly‑available paper, claiming “publication‑grade independent external validation” is misleading. Even if an internal DR1 T‑Web analysis exists, it is not verifiable by readers, and the text conflates internal, unpublished checks with peer‑reviewed external validation. This materially affects how strong the robustness case appears.

**Fix:**  
Remove all language asserting “publication-grade independent external validation” from T‑Web/ASTRA. Restrict robustness claims to (a) checks fully documented in this paper and repository, and (b) genuinely published, verifiable works (currently DESIVAST only). If internal DESI analyses were consulted, describe them explicitly as *internal, unpublished checks* without equating them to published external validation.


## PAPER-PER-M3 — MAJOR — Unpublished “companion papers” cited as if external literature

**Location:** `\bibitem{golden_chirality_2026}`, `\bibitem{golden_fnl_2026}` and multiple references throughout (Paper IV, Paper II).

**Issue:**  
Both citations are explicitly “in preparation” with no arXiv ID or journal reference. That is acceptable, but several parts of the manuscript **lean on them like established external literature**, e.g. “Paper IV establishes the catalog-wide CW-fraction monopole as a classifier-residual bias…” and “Paper II… SPHEREx discrimination…”, and then use their claims as hard priors (e.g. Eq. (1) σ_pred) and as external evidence in the robustness story. For a standalone paper, these are effectively *self‑referential assumptions*, not independently validated results.

**Fix:**  
Clearly label every use of Papers II/IV as reliance on *companion, not‑yet‑published* work. Where results from Paper IV (e.g. Δf_CW = −0.0026, monopole significance) are essential, briefly reproduce the relevant analysis or, at a minimum, quantify how sensitive the conclusions here are to possible shifts in those numbers once Paper IV undergoes peer review. Remove any phrasing that presents them as already‑established external constraints.


## PAPER-PER-m1 — minor — One GR/early‑universe references fine, but operator‑mapping paragraph is undersourced

**Location:** “Mapping to a physical operator (v0.1.32)” paragraph near the end, and citations `\bibitem{AlexanderYunes2009}`, `\bibitem{LueWangKamionkowski1999}`.

**Issue:**  
The two cited works are real and correctly referenced — Alexander & Yunes 2009 Phys. Rep. 480:1 and Lue, Wang & Kamionkowski 1999 PRL 83:1506.[AlexanderYunes2009][LueWangKamionkowski1999] However, the specific EFT operator you write down, \(\mathcal{L}_{\rm parity}\supset g_\phi (\nabla_i\phi)(\nabla^i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\), and the scaling \(Δf_{\rm CW}^{\rm env} \propto g_\phi (\nabla\phi·\nabla\rho)/\rho_{\rm bg}\) are **not** in either paper; they are your own construction. As written, it is easy for a reader to infer that this specific form and scaling are directly motivated by those references, which they are not.

**Fix:**  
Add one sentence explicitly stating that the operator form and scaling relation are a *toy EFT parametrization introduced in this work*, merely “inspired by” the general parity‑violating mechanisms reviewed in Alexander & Yunes and Lue–Wang–Kamionkowski, but not taken from them. This keeps the citations honest and avoids implying a level of direct theoretical precedent that the cited papers do not provide.
