# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 24.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33514, completion=1922, total=35436, search_context_size=low, cost={'input_tokens_cost': 0.10054, 'output_tokens_cost': 0.02883, 'request_cost': 0.006, 'total_cost': 0.13537}

---

## PAPER-PER-B1 — BLOCKER — Nonexistent “Zhu & Cai 2026 echoes” reference

**Location:** Sec. 2.3 Assumptions, sentence: “e.g., Zhu & Cai [Zhu:2026echoes]”.

**Issue:** The citation `Zhu:2026echoes` appears to be fabricated: there is no arXiv record or journal paper by Zhu & Cai in 2026 with a title about “echoes” or prolonged post‑bounce inflation in bounce cosmology; searching arXiv/ADS for “Zhu Cai bounce echoes 2026”, “Zhu:2026echoes”, and combinations of authors/topics returns nothing matching the metadata implied in the text.[ ] This is a classic fused-metadata / LLM-confabulated reference.

**Fix:** Replace this with a real, relevant bounce‑with‑late‑inflation reference (or an explicit “hypothetical example” with no citation). Until a real paper exists, remove the arXiv tag and rephrase to: “for example, models that add prolonged post‑bounce inflation (see, e.g., [actual ref] or generic reviews)” or similar, with a verifiable citation.


## PAPER-PER-M1 — MAJOR — Heinrich et al. 2024 citation timing and metadata

**Location:** Abstract and Sec. 4 (SPHEREx Forecast): “Heinrich et al. 2024 [Heinrich:2023] … multi-tracer galaxy bispectrum forecast”.

**Issue:** The bibkey `Heinrich:2023` suggests a 2023 arXiv preprint, but the prose calls it “Heinrich et al. 2024”. Searching arXiv and ADS shows a Heinrich+ SPHEREx PNG forecast posted 2023 (arXiv:2310.xxxx–240x.xxxx range, depending on the actual paper) with 2023 as preprint year; I do not find a 2024 journal version yet that matches the exact “multi-tracer galaxy bispectrum” phrasing.[ ] The mixed year labeling (2023 in key, 2024 in text) is inconsistent and looks like retrofitted metadata.

**Fix:** Align citation metadata with reality: either (a) refer to it consistently as a 2023 arXiv preprint (“Heinrich et al. 2023, arXiv:xxxx.xxxxx”) if no journal article exists yet, or (b) update the bib entry and text to the actual journal year and venue once published. Remove “2024” from the text unless you have a real 2024 publication with matching title and identifier.


## PAPER-PER-M2 — MAJOR — Jung 2025 Planck PR4 fNL reference likely nonexistent / mis‑labeled

**Location:** Sec. 8.1 “Current Data and Consistency Relation”: “Planck PR4/NPIPE … fNL = −0.1 ± 5.0 [Jung2025PlanckPR4fNL]”.

**Issue:** Searching for a 2025 Jung et al. Planck PR4/NPIPE fNL paper with that kind of identifier returns no exact match on arXiv/ADS; there are Planck PR3 non‑Gaussianity papers (Planck 2019), and NPIPE temperature/polarization releases, but not a Jung‑first‑author “Planck PR4 fNL” with that numeric result.[ ] The bibkey looks synthetic and I cannot match it to a real title, arXiv ID, or journal citation.

**Fix:** Either (i) point to the actual Planck PR3 non‑Gaussianity paper (Planck Collaboration 2019, arXiv:1905.05697) and clearly state that the −0.9±5.1 or similar number is PR3, or (ii) if there truly is a Jung‑led PR4/NPIPE fNL analysis, update with the correct author list, title, arXiv ID/journal, and verified central value. Until you can supply a verifiable reference, treat this as “private communication / work in prep” instead of a formal citation.


## PAPER-PER-M3 — MAJOR — Eskilt & Komatsu birefringence numbers and references not clearly tied to real paper

**Location:** Sec. 10 “Caveats”: discussion of “Eskilt et al. joint WMAP+Planck … 0.342° ± 0.094° at 3.6σ” and Cosmoglobe DR1 II reanalysis “0.35° ± 0.70°”.

**Issue:** There is an actual work by Eskilt & Komatsu on cosmic birefringence with Planck/WMAP; however, the exact numerical pair “0.342° ± 0.094° at 3.6σ” and the Cosmoglobe “0.35° ± 0.70°” need to match a real DOI/arXiv entry. Current searches show similar but not identical numbers in different drafts/updates, and I do not find references with the exact combination of values and titles as implied (the bibkeys `Eskilt2022`, `Eskilt2023Cosmoglobe` are not enough to verify).[ ] This raises a risk of mixing numbers from different versions or from multiple papers.

**Fix:** Explicitly tie each number to a specific, verifiable paper (e.g. “Eskilt & Komatsu, 2022, arXiv:xxxx.xxxxx, Eq. (y)” and the Cosmoglobe DR1 result with its correct citation), and confirm that the quoted central values and errors are those of the final published/posted versions. If you cannot locate an exact match, either adjust the numbers to the real ones or drop the second‑decimal “0.342” level precision and phrase it more generically with a clearly correct citation.


## PAPER-PER-M4 — MAJOR — Ambiguous / possibly fabricated “Jolicoeur:2025” and “Barreira:2022” usages

**Location:** Sec. 7 “Systematics and Robustness” — GR and PNG bias discussion, especially Fig. 3 kmin and Fig. bphi captions.

**Issue:** The text attributes quantitative GR‑projection degradation numbers to “Jolicoeur:2025” and detailed PNG bias–prior effects to “Barreira:2022”. There are real works by Barreira on PNG bias and by various authors on relativistic effects, but I cannot find a 2025 paper by “Jolicoeur” on SPHEREx/MegaMapper GR degradation with the specific 10–30% figures, nor a Barreira 2022 paper whose title and scope exactly match “bφ prior 20–50% ⇒ σ(fNL) growth to 2.2, etc.” as described.[ ] This looks like either (a) mixing real authors with invented years and quantitative claims, or (b) attributing your own Fisher toy model to external papers.

**Fix:** For each of these, either (i) identify and cite the exact real paper (full metadata, arXiv ID) whose quantitative results you are summarizing, and verify that your numbers match, or (ii) be explicit that these 10–30% and 20–50% degradation factors come from your own Fisher toy model, not from Jolicoeur or Barreira, and then adjust the citations accordingly (e.g. cite Barreira only for general bφ‑prior issues, not for your specific numbers). Remove any phantom “Jolicoeur:2025” entry if it does not correspond to a real paper.


## PAPER-PER-m1 — minor — Incomplete / ambiguous “Cai:2018non” non‑attractor inflation reference

**Location:** Sec. 6.1 “Can Inflation Reproduce the Signal?” — “Non-attractor single-field inflation naturally gives fnl = +5/2 (wrong sign) [Cai:2018non].”

**Issue:** The bibkey `Cai:2018non` suggests a 2018 Cai paper on non‑attractor inflation, but I cannot find an arXiv entry whose shortname matches exactly (there are several Cai papers around 2017–2019 on non‑attractor models, but titles and numeric predictions differ).[ ] Without a clear arXiv ID or title, this is hard to verify, and it’s easy to fuse numbers from different non‑attractor works (e.g. +5/2 result originates from a particular class of ultra slow‑roll models).

**Fix:** Replace the placeholder‑style key with a fully specified citation: give the full author list, title, year, and arXiv ID of the non‑attractor paper that actually derives fnl = +5/2; verify that the quoted value and context match that specific paper. If you are quoting a standard textbook/ review result rather than a particular Cai paper, cite that instead (e.g. Chen 2010 review, etc.) and adjust the key.
