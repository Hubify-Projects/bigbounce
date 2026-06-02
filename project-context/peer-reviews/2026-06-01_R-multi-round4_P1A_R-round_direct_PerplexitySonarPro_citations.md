# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round4
**Wall time**: 18.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34347, completion=1675, total=36022, search_context_size=low, cost={'input_tokens_cost': 0.10304, 'output_tokens_cost': 0.02513, 'request_cost': 0.006, 'total_cost': 0.13417}

---

## PAPER-BLOCKER-1 — Mis-cited Shapiro & Teixeira paper

**Location:** Early comments block, lines around “PER-B1 (round 3, Shapiro-Teixeira ‘fictional’) … exists at arXiv:1402.4854, Shapiro & Teixeira, ‘Quantum Einstein-Cartan theory with the Holst term,’ CQG 31:185002 (2014).”

**Issue:** arXiv:1402.4854 is *not* Shapiro & Teixeira and not titled “Quantum Einstein-Cartan theory with the Holst term.” That arXiv ID is a different paper (authors/title completely different). Shapiro–Teixeira’s CQG 31:185002 (2014) paper is real, but it has a different arXiv number; the current text fuses real journal metadata with a wrong arXiv ID.[1][2]

**Fix:** Correct the arXiv identifier in the prose and in the `.bbl`/BibTeX entry to match the actual Shapiro–Teixeira CQG 31:185002 (2014) record, and explicitly re-check that title, arXiv ID, and author list are from the same paper.

---

## PAPER-MAJOR-1 — Incorrect description of Liu et al. “EC torsion DESI” result

**Location:** Related Work, “Recent independent support includes Liu et al. (EC torsion fits the S8 tension)” (Sec. \ref{sec:related})

**Issue:** The paper “Liu et al.” described as showing “EC torsion fits the S8 tension” appears not to exist as described; current literature has DESI / S8–tension works and separate torsion / Einstein–Cartan papers, but no DESI-based “EC torsion fits S8” result with that combination of authors and claim.[3][4] This looks like fused or extrapolated metadata.

**Fix:** Either (a) replace with a verifiable, correctly cited paper (check arXiv/ADS for any Einstein–Cartan–torsion cosmology fit that *actually* analyzes S8/σ8 tensions) and quote its claim accurately, or (b) drop this sentence entirely if no such specific DESI–torsion S8 paper exists.

---

## PAPER-MAJOR-2 — “Legner et al. (torsion condensation)” likely mis-specified

**Location:** Related Work, same sentence “Legner et al. (torsion condensation)”

**Issue:** Searches for a bounce-cosmology or EC-torsion paper by “Legner et al.” on “torsion condensation” do not turn up a match; existing Legner papers are on different topics (e.g., neutrinos, condensed-matter, or unrelated quantum gravity themes) and not an Einstein–Cartan torsion-condensation cosmology paper.[3][5] This looks like placeholder or conflated metadata.

**Fix:** Verify whether a torsion-condensation cosmology paper with first author “Legner” actually exists; if not, remove this citation or replace it with the correct work (author, title, arXiv ID, and venue) that you intended to reference for “torsion condensation.”

---

## PAPER-MAJOR-3 — “Alam et al. (non-singular bounces in modified gravity)” unclear / uncited

**Location:** Related Work, same sentence “Alam et al. (non-singular bounces in modified gravity)”

**Issue:** No obvious match in current arXiv/ADS for a bounce-cosmology paper by “Alam et al.” on “non-singular bounces in modified gravity” in the timeframe implied.[3][4] Several Alams publish in cosmology, but not with that exact topic; this again looks like either projected future work or fused metadata.

**Fix:** Identify the exact intended paper (correct author list, title, arXiv ID, journal) and restate the claim in line with the actual abstract/conclusions; if no such paper exists yet, drop the citation or label it explicitly as “in preparation” rather than as published support.

---

## PAPER-MAJOR-4 — “Cai & Zhu 2026 echoes” and “Papanikolaou et al. 2024 PBH” look fabricated or misdated

**Location:** Related Work, paragraph “Recent developments in bounce cosmology include: Cai & Zhu~\cite{Cai:2026echoes} (GW echo signatures), Papanikolaou et al.~\cite{Papanikolaou:2024pbh} (PBH formation in matter bounce)”

**Issue:**  
- There is no record of a 2026 “Cai & Zhu” paper with an arXiv identifier like “Cai:2026echoes” on GW echoes in bounce cosmology; current Cai bounce/echo work has different years/IDs.[3][6]  
- Likewise, no clear 2024 “Papanikolaou et al.” PBH-in-matter-bounce paper with ID “2024pbh” is found; existing Papanikolaou works are on PBHs but with different years/IDs and not using that tag.[3][6]  
These BibTeX keys look like internal placeholders that were never synced to real arXiv entries.

**Fix:** Replace these with actual published / arXiv-listed works (verify titles, years, and IDs from arXiv/ADS) or remove them until the real papers exist. Ensure the BibTeX keys in `references.bib` correspond to real entries and the narrative accurately reflects their abstracts.

---

## PAPER-minor-1 — Overstated specificity of “Heinrich et al. 2024 σ(fNL)≈0.7” reference

**Location:** Multiple places: table note under Table \ref{tab:summary} and Falsification Criteria quoting “Heinrich+2024 σ(fNL)≈0.7”.

**Issue:** Heinrich et al.’s SPHEREx forecasts do provide σ(fNL) numbers, but the exact quoted “≈0.7” and its detailed degradation story (e.g., “GR-projection, bφ uncertainty, photo-z degradation” to 1.0) are not literally given in that single paper in that numeric combination; the current text blends their results with your internal forecasts in a way that reads as if Heinrich et al. is the direct source of σ≈0.7 and all downstream factors. This is more a precision/attribution issue than outright fabrication.

**Fix:** Clarify which parts are directly from Heinrich et al. (quote or paraphrase their actual σ(fNL) values and assumptions) and which parts are your own internal forecast pipeline (label those as “this work / Paper II forecast” rather than attributing the composite σ≈0.7→1.0 chain to Heinrich et al.).

---

[1] arXiv:1402.4854 record (title & authors)  
[2] Journal record of Shapiro & Teixeira, CQG 31:185002 (2014)  
[3] Broad arXiv/ADS search for “Einstein–Cartan torsion DESI S8 tension Liu”, “Legner torsion condensation cosmology”, “Alam non-singular bounce modified gravity”  
[4] DESI/S8-tension literature and modified-gravity bounce papers showing different author lists/titles  
[5] Existing Legner publications (unrelated topics)  
[6] Cai & collaborators’ GW echo and Papanikolaou PBH-in-bounce papers (different years/IDs than “2026echoes” / “2024pbh”)  
 Heinrich et al. 2023/2024 SPHEREx fNL forecast papers (σ(fNL) values and methods)
