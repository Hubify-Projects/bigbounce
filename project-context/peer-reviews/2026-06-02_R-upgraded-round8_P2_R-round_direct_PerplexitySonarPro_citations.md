# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 15.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36352, completion=1507, total=37859, search_context_size=low, cost={'input_tokens_cost': 0.10906, 'output_tokens_cost': 0.02261, 'request_cost': 0.006, 'total_cost': 0.13766}

---

## PAPER-PER-B1 — Mis-cited Hehl–Datta–Mercuri torsion references

**Issue (MAJOR):**  
In the introduction, the text attributes the scalar-sector Holst-term decoupling and the four-fermion contact term to “Mercuri 2006; Freidel et al. 2005” and “Hehl‑Datta–Mercuri,” but no concrete citations (titles, arXiv IDs, or bibkeys) are given, and these names cover multiple distinct papers (e.g., Mercuri 2006 CQG 23 5729; Freidel, Minic & Takeuchi 2005 PRD 72 104002) with different scopes. The wording suggests specific results (exact scalar reduction, explicit form of the axial four‑fermion operator) that are not all contained in a single clearly identified paper.

**Fix:**  
Replace the informal “Mercuri 2006; Freidel et al. 2005” / “Hehl‑Datta–Mercuri” mentions with explicit references (authors, year, full titles) pointing to the precise papers that prove (i) the Holst term’s topological nature in the scalar-only sector, and (ii) the axial four‑fermion contact term, and ensure the bib file contains matching entries; if multiple papers are needed, state explicitly which result comes from which reference.


## PAPER-PER-B2 — Unverified Zhu & Cai 2026 citation

**Issue (MAJOR):**  
The paper cites “Zhu & Cai 2026” with bibkey `Zhu:2026echoes` and arXiv ID claimed as 2603.13924 in comments, described as dealing with dark‑energy‑from‑bounce with prolonged post‑bounce inflation. arXiv IDs of the form 2603.xxxxx correspond to March 2026 and, as of now, there is no public record confirming a Zhu–Cai paper with that identifier and the described content.

**Fix:**  
Verify directly on arXiv/ADS that arXiv:2603.13924 exists, that its authors include Zhu and Cai, and that its title/topic match the description; if not yet public or incorrect, mark it explicitly as “in preparation / private communication” (without an arXiv ID) or remove it from the argument until the real preprint is available.


## PAPER-PER-M1 — Ambiguous Heinrich et al. 2024 reference

**Issue (MAJOR):**  
“Heinrich et al. 2024 [Heinrich:2023]” is repeatedly cited as the SPHEREx multi‑tracer bispectrum forecast with σ(f_NL^local) ≈ 0.7, but no concrete metadata are visible here; prior rounds claim an A&A or PRD publication with specific tables/figures. Without title/journal/ID, it is difficult to confirm whether this is a genuine paper (e.g., a 2023 arXiv preprint published 2024) or an LLM-fused reference, especially since “Heinrich 2023 SPHEREx bispectrum forecast” is not yet a standard widely-known citation.

**Fix:**  
Explicitly supply the full reference (authors, exact title, journal or arXiv ID) for the Heinrich et al. SPHEREx bispectrum forecast, and check that Fig. 6 / Table 3 actually contain a multi‑tracer SPHEREx bispectrum forecast with σ(f_NL) ≈ 0.7 under the local-template normalization used here; adjust numbers and text if the cited paper’s forecast differs.


## PAPER-PER-M2 — Unclear Cai:2018non inflation reference

**Issue (MAJOR):**  
The paper cites “Cai:2018non” for the statement that non‑attractor single‑field inflation “naturally gives f_NL = +5/2,” but there is potential confusion: there is a well‑known Gao–Cai–Piao line of works on non‑attractor inflation, but no obviously standard 2018 paper with bibkey “Cai:2018non” and such a simple headline result without qualifiers (e.g., dependence on potential shape, sound speed, or duration).

**Fix:**  
Confirm that the cited paper (with its real arXiv ID and title) indeed states that non‑attractor single‑field inflation generically yields f_NL^local = +5/2 in the relevant limit, and that this is not conditional on additional model ingredients; otherwise, replace with the correct reference (e.g., Chen et al., Gao & Cai, or other specific non‑attractor paper) and soften the “naturally gives” wording to match the actual claim.


## PAPER-PER-M3 — Jolicoeur 2025 & Barreira 2022 GR / b_φ systematics

**Issue (minor):**  
GR and PNG-bias systematics are attributed to “Jolicoeur:2025” and “Barreira:2022,” but the exact sources are not disambiguated. For example, there is at least one Barreira 2022 paper on PNG bias and b_φ (PRD 106 063503, arXiv:2205.05673) and a Jolicoeur et al. work on relativistic projection in large‑scale structure, but without titles/IDs it is ambiguous which specific results are being used for the quantitative degradation levels quoted.

**Fix:**  
Add full metadata (title, arXiv ID, journal) for the Jolicoeur and Barreira references and verify that (i) Jolicoeur et al. indeed provide the 10–30% σ(f_NL) degradation numbers for SPHEREx/MegaMapper‑like surveys, and (ii) Barreira 2022 is the paper that specifically argues for marginalizing b_φ per tracer bin and quantifies the 20–50% σ(f_NL) degradation; adjust the numerical ranges if the cited papers disagree.


## PAPER-PER-n1 — Eskilt / Cosmoglobe birefringence numbers need tightening

**Issue (nit):**  
The cosmic birefringence paragraph claims Eskilt & Komatsu’s joint WMAP+Planck result is β = 0.342° ± 0.094° at 3.6σ from zero, and that Cosmoglobe DR1 II gives β = 0.35° ± 0.70°, but these values (and “joint WMAP+Planck” vs. “Planck only”) can differ slightly across versions/analyses; the exact numbers and significance levels are sensitive to which dataset combination is used.

**Fix:**  
Cross‑check the latest Eskilt & Komatsu and Cosmoglobe DR1 II papers, ensure the quoted central values, uncertainties, and σ-levels match the specific analysis you intend to reference, and include the exact paper identifiers; if the numbers differ, update the text to the precise published figures or phrase them with “≈” and an explicit citation to avoid over‑precision.
