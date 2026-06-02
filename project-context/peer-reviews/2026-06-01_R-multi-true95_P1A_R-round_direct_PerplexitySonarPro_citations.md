# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 25.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30233, completion=1907, total=32140, search_context_size=low, cost={'input_tokens_cost': 0.0907, 'output_tokens_cost': 0.02861, 'request_cost': 0.006, 'total_cost': 0.1253}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited/fictional reference “Golden2026P2” (Paper II)

**Location:** Multiple: Abstract, Sec. 1/Table I note, Sec. 4 (Route 4), Sec. 7, Sec. 10, Sec. 13, Conclusions, App. A.  

**Issue:** The paper repeatedly cites “Paper II / Golden2026P2” as an existing SPHEREx/Fisher-forecast companion paper and as Ref. \cite{Golden2026P2}, but no such article or arXiv entry is discoverable (author “Houston Golden” + “bounce”/“matter-bounce”/“fnl –35/8” + 2025/2026) in arXiv, ADS, or publisher databases.[ ] The title, venue, and arXiv ID are never given, and all external-facing claims about SPHEREx significance, assumptions, and technical implementation rely on this nonexistent reference.  

**Fix:** Either (a) mark Paper II explicitly as *in preparation* or *internal manuscript* and remove its BibTeX citation key from the bibliography, downgrading all quantitative SPHEREx claims in this paper to “based on internal, not-yet-public forecasts”, or (b) if a preprint exists, supply the correct arXiv ID, full author list, and title, and ensure the bibliography and in‑text citations match that record exactly.


## PAPER-PER-M1 (MAJOR) – Mis-cited / likely nonexistent “Golden2026P3” and “Golden2026P4”

**Location:** Sec. 3 (spin analysis, Paper IV) \& Sec. 10 (PTA, Paper III), Sec. 12/13/Appendix.  

**Issue:** The text cites “Paper III~\cite{Golden2026P3}” for a “real-KDE GPU MCMC” reanalysis of NANOGrav 15‑yr data and “Paper IV~\cite{Golden2026P4}” for a DESI-DR8 galaxy-chirality catalog and ViT classifier, treating them as existing, external references, but no such works by Golden (or with matching titles) appear in arXiv/ADS or journal databases.[ ] Bib items are not visible here, but external search finds nothing matching those identifiers. These references are currently indistinguishable from LLM-invented companion papers.  

**Fix:** As above, either (a) relabel Paper III and Paper IV consistently as *unpublished internal analyses* with no BibTeX entries (and soften all language that implies published status), or (b) provide their correct, verifiable arXiv IDs / journal references and check that all numerical results and claims in the main text truly appear in those works.


## PAPER-PER-M2 (MAJOR) – “Golden2026P1b” (Paper I(b)) appears unpublished / unlocatable

**Location:** Abstract, Introduction (Companion paper paragraph), Secs. 3, 4, 6, 7, 8, 12, 13, App. A, Conclusions.  

**Issue:** The companion MCMC/NaMaster/ALP analysis is consistently referred to as “Paper I(b)~\cite{Golden2026P1b}” and treated as a citable, public reference that hosts the cosmological chains, chain diagnostics, birefringence fits, and reproducibility manifest; however, no such paper or preprint (author “Houston Golden”, 2025–2026, keywords “Einstein–Cartan”, “bounce”, “NaMaster”, “ALP birefringence”) is findable in arXiv, ADS, or journal searches.[ ] From a citation-forensics perspective this is currently a dead reference.  

**Fix:** Before journal submission, either (i) upload Paper I(b) to arXiv and cite it with its correct arXiv identifier and full title, or (ii) if it remains internal, remove it from the formal reference list and rephrase all text to say that these details are “available upon request / in internal documentation”, and avoid treating its numbers as independently peer‑reviewable results.


## PAPER-PER-M3 (MAJOR) – Misleading claim that cosmological-parameter values are “from” an external paper that does not exist

**Location:** Introduction, “Companion paper” paragraph; Sec. 3 (EB / ALP), Sec. 6 (systematics), App. A table notes.  

**Issue:** The paper repeatedly states that key cosmological numbers used here (e.g. \(H_0 = 67.68\pm 1.06\), \(\Delta N_\mathrm{eff}\approx 0\)) are “from” the MCMC analysis in Paper I(b) and that full diagnostics etc. are “documented there”. Since Paper I(b) is not publicly available (see M2), readers have no way to verify those chains, likelihoods, priors, or even whether the quoted numbers are correctly transcribed. This is a provenance problem, not just “in prep” status: the current prose implicitly treats these values as externally citable results.  

**Fix:** Until Paper I(b) is on arXiv or in a journal, explicitly downgrade these to “internal analysis results (not yet publicly documented)” and avoid phrasing that implies they can be checked in a published companion. Alternatively, reproduce the minimal necessary chain setup and summary statistics in this paper so that the claims are self-contained and independently auditable.


## PAPER-PER-m1 (minor) – Ambiguity / potential mis-citation of several external cosmology references

**Location:** Throughout (DESI 2024/2025 BAO, DESI DR2 \(w_0w_a\), Heinrich+2024 SPHEREx \(\sigma(f_\mathrm{NL})\), LiteBIRD 2023, etc.).  

**Issue:** Several key external references are only indicated by shorthand names and years in the prose (e.g. “DESI 2024–2025 BAO results~\cite{DESI2024,DESI2025DR2}”, “Heinrich+2024~\cite{Heinrich:2023}”, “LiteBIRD 2023~\cite{LiteBIRD2023}”), but the LaTeX snippet does not show the BibTeX entries and web search confirms there are multiple plausible candidates for at least some of these keys (e.g. DESI has several 2024/2025 preprints; Heinrich et al. 2023/2024 have multiple non‑Gaussianity/SPHEREx papers).[ ] The current paper does not make clear which exact arXiv IDs or journal papers are meant, which weakens reproducibility of all quoted significances and forecast numbers.  

**Fix:** Ensure that each of these citation keys corresponds to a unique, real paper in the bibliography (with correct author list, title, journal, and arXiv ID) and, where multiple similar papers exist (DESI DR2, Heinrich et al. on SPHEREx, LiteBIRD design), explicitly name the first author and part of the title in the text so readers can unambiguously match the citation to the external work.


## PAPER-PER-m2 (minor) – Self-contradictory status of several routes / results relative to the cited literature

**Location:** Sec. 4 (Routes 2 & 4), Sec. 12, App. B.  

**Issue:** Some statements about what the cited literature “established” are either stronger than what those papers actually show or mix results from different works. For example, Mercuri (2009) and Mercuri & Capozziello (2008) discuss Holst+Nieh–Yan structure and anomalies but do not, in the form given, derive the specific effective action in Eq. (4.7) with the exact coefficient structure claimed; Lue, Wang & Kamionkowski (1999) give the basic Chern–Simons–induced birefringence scaling, but the text blends that with a particular numerical mapping to \(\beta\simeq0.27^\circ\) that actually depends on choices about \(m_\theta\), \(\rho_\theta\), and \(\alpha/M\) made here, not in those papers.[ ] These passages blur the line between “following the general mechanism of Ref. X” and “Ref. X computed the very formula we now use quantitatively.”  

**Fix:** Rephrase these segments to attribute only the mechanisms and qualitative structures to the external papers (e.g. “following the mechanism outlined in…”; “adapting the scaling in…”), and clearly label the specific coefficient choices and numerical substitutions as *this paper’s phenomenological modeling*, not as direct results of the cited works.
