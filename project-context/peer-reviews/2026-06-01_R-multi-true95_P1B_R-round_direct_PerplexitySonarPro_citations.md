# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-true95
**Wall time**: 19.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24060, completion=1824, total=25884, search_context_size=low, cost={'input_tokens_cost': 0.07218, 'output_tokens_cost': 0.02736, 'request_cost': 0.006, 'total_cost': 0.10554}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited / possibly non-existent torsion paper

**Location:** §3, paragraph “Scope of the ΔNeff proxy: …” – citation `\cite{ECTorsionDESI2025}` with description “Liu et al. constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6).”

**Issue:** A search for an EC/Einstein–Cartan torsion cosmology paper by any “Liu et al.” using *DESI DR2* + *Pantheon+* + *DES-SN5YR* + *Planck 2018* with ΔAIC ≃ −6 in favor of torsion returns no match on arXiv, ADS, or major journals, and there is no obvious DESI-DR2 torsion paper with that author/year combination. This smells like fused metadata or an internal placeholder, not a real external result.

**Fix:** Either (i) replace this with a verified, citable paper (check arXiv/ADS for a real Einstein–Cartan / torsion cosmology analysis and match exact title, authors, year, and data combination), or (ii) explicitly mark it as “work in preparation / internal analysis” and remove the “Liu et al.” external-citation framing until an actual published preprint exists.


## PAPER-PER-B2 (MAJOR) – Eskilt et al. birefringence citation looks confounded

**Location:** Abstract; §6 “Cosmic Birefringence: Spectator ALP Consistency Check”; summary-likelihood paragraphs – repeated use of `\cite{Eskilt2022b}` for “joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ).”

**Issue:** Searching for an “Eskilt et al. 2022b” paper giving a *joint Planck+ACT DR6* birefringence result at β ≈ 0.342° ± 0.094° (3.6σ) yields no clear, uniquely matching publication; the well‑known works are (i) Eskilt & Komatsu’s Planck NPIPE analyses, and (ii) ACT/LAT birefringence results which are not authored by Eskilt. The specific “Planck+ACT joint” combination with that exact number under Eskilt’s authorship appears not to exist in the literature as described and may be an internal fit or conflation of Planck and ACT papers.

**Fix:** Confirm on arXiv/ADS what exact joint analysis you are using (author list, collaboration, year, journal; it may well be ACT collaboration or “Eskilt et al.” but not with the “Planck+ACT DR6” branding you claim). Correct the citation key, year suffix, and textual description to match the real paper, or relabel this as your *own combined fit* based on the published Planck and ACT likelihoods rather than as a “published joint Planck+ACT” result.


## PAPER-PER-B3 (MAJOR) – ACT/Planck birefringence references are not cleanly matched to real papers

**Location:** Abstract and §4/§6: citations `\cite{DiegoPalazuelos2022}`, `\cite{DiegoPalazuelos2025}` for “Planck NPIPE β = 0.30° ± 0.11°” and “ACT DR6 β = 0.215° ± 0.074°.”

**Issue:** Searching for “Diego Palazuelos” birefringence papers with those years and experiments yields no exact matches with these β values and error bars. The ACT DR6 birefringence paper is typically cited under the ACT collaboration author list and different lead author; similarly, Planck–NPIPE birefringence values in the literature are usually associated with Eskilt & Komatsu and not with “Diego Palazuelos 2022.” The combination of author name + year + experiment + β numbers looks like fused/confabulated metadata.

**Fix:** Re‑identify the correct Planck NPIPE and ACT DR6 birefringence references via arXiv/ADS, using their official collaboration titles and lead authors. Update all `\cite{DiegoPalazuelos2022,DiegoPalazuelos2025}` keys, author names, and years to match the actual publications, and verify that the quoted β means and uncertainties agree with the numbers in those papers.


## PAPER-PER-B4 (MAJOR) – ALP-birefringence theory provenance (Fujita et al.) potentially mis‑attributed

**Location:** §6, first paragraph: “The model class was previously studied by Fujita et al. [\cite{Fujita2021}].”

**Issue:** A search for a 2021 Fujita paper on ALP‑induced *late‑time CMB cosmic birefringence* with the same mass scale \(m \sim H_0\), \(f_a \sim M_{\rm Pl}\), and \(C_{a\gamma}\) normalization used here does not reveal a clean one‑to‑one match: Fujita has several axion‑related works, but none obviously provide exactly the parameterization and birefringence formula you are using. This suggests either (i) the wrong Fujita paper is cited, or (ii) the reference is being credited with a model more specific than it actually contains.

**Fix:** Pin down precisely which Fujita paper supplies the ALP model used (title, journal, arXiv ID). If the cited work only discusses a broader ALP scenario (or different parameter regime), soften the text to “related ALP models have been studied by Fujita et al.” and add the true theoretical source for your specific birefringence formula and parameter ranges (or state explicitly that the detailed parameter scan is new to this paper).


## PAPER-PER-B5 (minor) – DESI DR2 / DES-Y5 / DES-SN5YR citation metadata need tightening

**Location:** §3 (“Independent cross-validation”), §3 caveats, §5 and Conclusions, and cross-paper status tables; citations `\cite{DESI2025DR2}`, `\cite{DES2024SN5YR}`, `\cite{DES2024}` etc.

**Issue:** A combined DESI “DR2” BAO cosmology paper labeled 2025, plus DES‑SN “5YR” and DES “Y5” lensing/cluster results with these exact year tags, do not correspond cleanly to current public releases (DESI DR2 cosmology papers and DES five‑year SN analyses have specific collaboration titles and very recent arXiv IDs). The naming here looks like an internal shorthand; without matching titles/IDs, a reader cannot reliably locate the cited works.

**Fix:** Replace all shorthand labels with the official collaboration paper titles, lead authors, and correct year/arXiv IDs (e.g., “DESI 2024 BAO results from DR2: …”, “DES Collaboration: The Dark Energy Survey Supernova Program: 5‑year sample …”). Ensure that each of `DESI2025DR2`, `DES2024SN5YR`, and `DES2024` maps uniquely to a real, published preprint or paper.


## PAPER-PER-B6 (minor) – Cross-paper readiness table (P1, P2, P3, P4) risks fictitious-citation bleed

**Location:** §7, Table \ref{tab:crosspaper} and surrounding prose.

**Issue:** The table lists “Paper II [Golden2026P2], Paper III [Golden2026P3], Paper IV [Golden2026P4]” as if they are already well‑defined preprints, but a search for 2026 arXiv entries with those titles/authors shows no obvious matches yet. While these are internal companion papers by the same author, the combination of hard version numbers, readiness percentages, and cross‑references can be read as implying that external preprints already exist.

**Fix:** Clarify in the text that P2–P4 are *forthcoming manuscripts* (or internal drafts) unless and until arXiv IDs exist, and avoid giving the impression that they are already citable published works. Once actual arXiv submissions are live, update the bibliography entries to the correct titles, author lists, and identifiers.
