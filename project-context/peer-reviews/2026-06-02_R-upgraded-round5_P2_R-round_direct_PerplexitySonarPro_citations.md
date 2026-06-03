# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 16.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34679, completion=1707, total=36386, search_context_size=low, cost={'input_tokens_cost': 0.10404, 'output_tokens_cost': 0.0256, 'request_cost': 0.006, 'total_cost': 0.13564}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited Planck PR4 fNL Result

**Location:** Sec. 9 “Current Data and Consistency Relation”, paragraph 1: “Planck PR4/NPIPE (CMB bispectrum, \(\fnl = -0.1 \pm 5.0\)~\cite{Jung2025PlanckPR4fNL})…”

**Issue:** There is, as of now, no public Planck PR4/NPIPE bispectrum paper by “Jung 2025” with that specific \(\fnl\) result; the bibkey `Jung2025PlanckPR4fNL` is not verifiable in arXiv / ADS, and the quoted value is extremely close to the established Planck 2018 PR3 constraint \(\fnl^{\rm local} = -0.9 \pm 5.1\) rather than a documented PR4 update.[ ]  

**Fix:** Either (a) clearly label this as an internal or in-prep forecast (“Jung et al., in preparation; result not yet public”) and remove any implication of a published PR4 paper, or (b) revert to the last citable Planck release (PR3 2018) with its actual author list, arXiv ID, and \(\fnl\) value, and adjust all PR4-specific language accordingly.

---

## PAPER-PER-B2 (MAJOR) – Unverifiable Zhu & Cai 2026 “Echoes” Reference

**Location:** Sec. 2.3 “Assumptions”, sentence: “e.g., Zhu~\&~Cai~\cite{Zhu:2026echoes}…”

**Issue:** A 2026 Zhu & Cai “echoes” bounce paper with arXiv:2603.13924 and the described content cannot be found on arXiv / ADS; earlier rounds note this bibkey was “verified by direct bib lookup” in a private `.bib`, but there is no public record matching the year, ID, or title, so as written it reads as a confabulated or at least non-public reference.[ ]

**Fix:** If this is genuinely an in-preparation or not-yet-public work, change the citation label to “Zhu & Cai, in preparation (2026)” without an arXiv ID, and remove any implication that it is an existing arXiv/published paper; otherwise, update to the actual arXiv identifier, title, and year of the real paper being referenced.

---

## PAPER-PER-M1 (MAJOR) – Eskilt / Cosmoglobe Birefringence Numbers and Citations

**Location:** Sec. 11.3 “Caveats”, long paragraph on cosmic birefringence: “the 3.6σ Eskilt et al.~\cite{Eskilt2022} joint WMAP+Planck analysis … companion Cosmoglobe DR1 II reanalysis~\cite{Eskilt2023Cosmoglobe}…”

**Issue:** The described combination “Eskilt & Komatsu joint WMAP+Planck 3.6σ at β=0.342°±0.094°” and “Cosmoglobe DR1 II β=0.35°±0.70°” does not match the actual published numbers in Eskilt’s birefringence and Cosmoglobe papers (both the central values and significances differ), and the labels “Eskilt2022” / “Eskilt2023Cosmoglobe” as used here are not traceable to unique arXiv IDs with those exact results.[ ]

**Fix:** Replace the numerical values and uncertainties with those actually reported in the corresponding Eskilt / Cosmoglobe papers, and ensure that the bibkeys map to real, uniquely identifiable arXiv entries (correct year, title, and journal); if you want to use bounce-motivated β≈0.27° as an illustrative value, state it explicitly as a model point and clearly separate it from the quoted observational measurements.

---

## PAPER-PER-M2 (MAJOR) – Heinrich et al. (SPHEREx bispectrum) Reference Ambiguity

**Location:** Abstract and multiple sections (Intro, SPHEREx forecast, bφ systematics): “Heinrich \etal~2024~\cite{Heinrich:2023}…” describing a SPHEREx multi-tracer bispectrum forecast with σ(fNL)=0.7.

**Issue:** The bibkey `Heinrich:2023` is claimed to be a 2024 paper forecasting σ(fNL)=0.7 from a SPHEREx multi-tracer bispectrum; however, there is no single, clearly matching public paper by “Heinrich et al.” with the exact SPHEREx-only, bispectrum-only σ(fNL)=0.7 result and the described Fig. 6 / Table 3 structure. The mixing of year (2024 in text vs. 2023 in key) and the very specific σ(fNL) number without a verifiable source is a red flag for fused or approximate metadata.[ ]

**Fix:** Identify the precise published Heinrich et al. paper (correct year, full title, arXiv ID) that provides the σ(fNL) forecast actually used (whether SPHEREx-specific or more general LSS), and adjust the text to match its stated survey setup and σ(fNL); if the σ=0.7 value is derived by you from their Fisher tables rather than quoted directly, say so explicitly and do not attribute that exact forecast to the paper’s abstract/caption.

---

## PAPER-PER-M3 (MAJOR) – Barreira 2022 bφ Systematics Citation Not Cleanly Matched

**Location:** Sec. 7.2 “PNG Bias (bφ) Sensitivity”: “as recommended in Barreira~\cite{Barreira:2022} for upcoming Stage-IV surveys…”

**Issue:** There are several Barreira papers around 2022 on PNG and bias; the manuscript attributes a very specific prescription (“relax bφ universality per tracer bin” and 20–50% σ(fNL) degradation) to a generic `Barreira:2022` without specifying which paper (no unique title / arXiv ID given in text), and the quantitative degradation range does not map one-to-one to any single Barreira result that can be easily verified.[ ]

**Fix:** Disambiguate the reference: give the full citation in the text (e.g., “Barreira 2022, *title*”) and ensure the bibkey points to that exact paper; revise the degradation numbers so they match what that paper actually computes, or state clearly that the 20–50% range is your own extrapolation inspired by Barreira’s qualitative recommendation rather than a direct quoted result.

---

## PAPER-PER-m1 (minor) – Jolicoeur 2025 GR Projection Effects Reference

**Location:** Sec. 7.3 “Parameterized GR-Degradation Analysis”: “Jolicoeur et al.~\cite{Jolicoeur:2025}… find that relativistic corrections … degrade σ(fNL) by 10–30%…”

**Issue:** The text cites a future “2025” Jolicoeur et al. paper with detailed quantitative GR-degradation numbers; there is Jolicoeur work on relativistic corrections and PNG forecasts, but no currently public 2025 paper with exactly those percentages and survey mapping as described, so the precision of the 10–30% range and the DR labels look more like forward-looking assumptions than direct quotations.

**Fix:** If the Jolicoeur result is from an already submitted but not yet public manuscript, mark it clearly as “Jolicoeur et al., in preparation (2025)” and soften the numerical specificity (“of order 10–30%”) or else anchor the degradation factors to an actually published Jolicoeur paper with its correct year and arXiv ID, adjusting the numbers to match what is demonstrably in that work.
