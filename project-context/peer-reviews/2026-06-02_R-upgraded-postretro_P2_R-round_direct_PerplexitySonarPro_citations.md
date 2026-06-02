# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 22.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34801, completion=1635, total=36436, search_context_size=low, cost={'input_tokens_cost': 0.1044, 'output_tokens_cost': 0.02453, 'request_cost': 0.006, 'total_cost': 0.13493}

---

## PAPER-PER-B1 — BLOCKER — Mis-cited Zhu & Cai 2026 bounce+dark energy paper

**Location:** Sec. \ref{sec:assumptions}, paragraph discussing “Zhu & Cai \cite{Zhu:2026echoes}”.

**Issue:** The paper repeatedly cites a work labeled `Zhu:2026echoes` with arXiv ID `2603.13924` and description “dark‑energy‑from‑bounce constructions” and “echoes,” but as of now there is no such arXiv entry or published cosmology paper matching Zhu + Cai + “echoes” + that ID. The claimed arXiv identifier and title-class are almost certainly fabricated/fused metadata.

**Fix:** Replace `Zhu:2026echoes` with a real, verifiable bounce model that includes prolonged post‑bounce inflation (or drop the parenthetical example entirely), and update the bib entry to a checked arXiv ID / journal; do not reference 2603.13924 or “echoes” unless a genuine paper with those properties exists and is verified on arXiv/ADS/publisher sites.


## PAPER-PER-B2 — BLOCKER — Nonexistent Jung 2025 Planck PR4 fNL reference

**Location:** Sec. \ref{sec:currentdata}, first paragraph: “Jung2025PlanckPR4fNL”.

**Issue:** The paper attributes the Planck PR4/NPIPE local‑\(f_{\rm NL}\) constraint to “Jung 2025” with a bibkey `Jung2025PlanckPR4fNL` and arXiv `2504.00884`. There is currently no Planck collaboration local‑\(f_{\rm NL}\) paper by Jung in 2025, and no such arXiv entry with that ID; using this as the definitive source for the latest CMB bispectrum constraint is therefore unsupported.

**Fix:** Replace this with the latest real Planck non‑Gaussianity result (e.g., the 2019 Planck NG paper) or any genuine PR4/NPIPE follow‑up that actually exists, updating author list, arXiv ID, and numerical values to match the real publication; if PR4‑based \(f_{\rm NL}\) is still unpublished, explicitly state that the number is an internal or forecast value rather than a citable result.


## PAPER-PER-M1 — MAJOR — Cosmoglobe birefringence citation appears fabricated / mis‑dated

**Location:** Discussion section, last large paragraph: “Cosmoglobe DR1 II reanalysis~\cite{Eskilt2023Cosmoglobe} … reports the considerably weaker \(\beta = 0.35^\circ \pm 0.70^\circ\).”

**Issue:** The text refers to a specific Cosmoglobe DR1 “II” paper by Eskilt et al. with a precise birefringence value and bibkey `Eskilt2023Cosmoglobe`, with arXiv claimed as `2511.09466` in the audit trail. There is no current arXiv record with that ID or a Cosmoglobe DR1 II birefringence paper in that time frame; this looks like a fused or anticipated reference rather than an on‑disk paper.

**Fix:** Either (a) remove this Cosmoglobe DR1 II citation and numerical value, keeping only the established birefringence result(s) that correspond to real published papers, or (b) once a Cosmoglobe birefringence paper actually appears, update the citation to its real authors, title, arXiv ID, and numbers after verification.


## PAPER-PER-M2 — MAJOR — Barreira 2022 PNG bias reference not verifiable as cited

**Location:** Sec. \ref{sec:systematics}, PNG‑bias discussion; also MegaMapper section.

**Issue:** The manuscript cites “Barreira~\cite{Barreira:2022}” as a key source on \(b_\phi\) priors and PNG‑bias degradation, with arXiv `2205.05673` noted in comments. That arXiv ID does not currently correspond to a Barreira PNG‑bias paper, and there is no clearly matching 2022 Barreira paper with the exact role described here (multi‑tracer \(b_\phi\) prior degradation for future LSS). This suggests a metadata fusion (author/year/topic) rather than a clean citation.

**Fix:** Identify the actual Barreira (or other) paper that quantifies \(b_\phi\)‑prior impact for PNG constraints, and replace `Barreira:2022` with that paper’s correct arXiv ID, title, and year; if no such dedicated analysis exists, soften claims to “see e.g. …” with a real, more general bias‑modeling reference and remove the strong quantitative attribution to a nonexistent 2022 study.


## PAPER-PER-M3 — MAJOR — Jolicoeur 2025 GR‑projection forecast appears anticipatory

**Location:** Sec. \ref{sec:systematics}, GR‑degradation subsection and Table \ref{tab:gr}: “Jolicoeur et al.~\cite{Jolicoeur:2025}”.

**Issue:** The manuscript repeatedly invokes a “Jolicoeur et al. 2025” relativistic‑projection forecast for SPHEREx/MegaMapper, with a bibkey `Jolicoeur:2025` and arXiv `2511.09466` in the comments. No such Jolicoeur 2025 GR‑projection paper currently exists with that ID, and I cannot locate a Jolicoeur paper giving the specific 10–30 % degradation numbers in the exact SPHEREx/MegaMapper context described.

**Fix:** Either (a) substitute a real, existing GR‑projection forecast (with correct authors, ID, and quantitative results) that justifies the degradation priors used here, or (b) clearly label the 10–30 % GR degradation as an internal estimate, remove the fabricated citation, and restrict the discussion to qualitative expectations until an appropriate published reference is available.


## PAPER-PER-m1 — minor — Overconfident “all bibkeys exist” audit trail claim vs. actual missing IDs

**Location:** Front‑matter comments block, lines describing closure of Perplexity B‑series findings (“All bibkeys EXIST … with real arXiv IDs (2603.13924, 2311.13082, 2504.00884, 2205.13962, 2511.09466, 2205.05673, 1712.09998) and real DOIs …”).

**Issue:** The internal note asserts that prior reviewers’ concerns about several bibkeys and arXiv IDs were “FALSIFIED” because those entries exist “in focused\_paper\_refs.bib with real arXiv IDs,” but at least four of the enumerated IDs (2603.13924, 2504.00884, 2511.09466, 2205.05673) do not correspond to real cosmology papers matching the claimed titles/authors as of now. This is a meta‑level inconsistency between the on‑disk .bib file and the external literature.

**Fix:** Replace the blanket “FALSIFIED” statement with a more accurate audit: explicitly check every custom bibkey against arXiv/ADS, remove or correct any that do not map to real papers, and update this comment to reflect that some earlier reviewer concerns were in fact valid (or simply delete this internal “all good” narrative from the public source).
