# P1B_v1B08 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0930pt_P1B_v1B08_R4_R-round_real
**Wall time**: 18.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13331, completion=1885, total=15216

---

## Finding 1 – PAPER-CITES-1 (BLOCKER)

Claimed refs: Planck/ACT birefringence measurements and joint analysis  
(Diego Palazuelos 2022/2025; Eskilt 2022b)

Issue (Sec. 4, Sec. 6, abstract, conclusions):  
The manuscript cites “DiegoPalazuelos2022”, “DiegoPalazuelos2025”, and “Eskilt2022b” as the Planck NPIPE, ACT DR6, and joint Planck+ACT cosmic birefringence analyses with values \(\beta = 0.30^\circ\pm0.11^\circ\), \(\beta = 0.215^\circ\pm0.074^\circ\), and \(\beta = 0.342^\circ\pm0.094^\circ\) at \(3.6\sigma\), respectively, but these identifiers, titles, and author combinations do not correspond to any actual arXiv entries or journal publications; the arXiv IDs and bibliographic metadata are absent or mismatched on arXiv/ADS, so the core observational inputs for the ALP analysis are not verifiable. [1][2]  

Fix (1–2 sentences):  
Explicitly give correct, real arXiv IDs, titles, author lists, and journal references for the Planck NPIPE, ACT DR6, and joint Planck+ACT birefringence papers, or state clearly that these are in-prep/private-comm results and downgrade their status from “published” to “unpublished” with appropriate caveats. If no public references exist yet, the paper must treat all quoted \(\beta\) and \(\sigma\) values as provisional and non-load-bearing, and should not present them as “published” detections.


## Finding 2 – PAPER-CITES-2 (MAJOR)

Claimed ref: Liu et al. torsion with DESI DR2 – “ECTorsionDESI2025”  

Issue (Sec. 3, “Independent cross-validation” paragraph):  
The paper asserts that “Liu et al. [ECTorsionDESI2025]” constrained an Einstein–Cartan torsion model with DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC with \(\Delta\mathrm{AIC}=-5.7\) to \(-6.6\), and that the present MCMC agrees at 0.5 σ in \(H_0\) and 0.4 σ in \(\sigma_8\); however, no such arXiv entry or journal paper can be located matching that combination of authors, dataset list, and focus (EC torsion with DESI DR2), so both the citation and the detailed numerical AIC/σ-level comparison appear to rest on non‑verifiable or misidentified work. [1][2]  

Fix (1–2 sentences):  
Replace “ECTorsionDESI2025” with a verifiable published or submitted paper (correct arXiv ID, title, authors, and venue) that actually performs EC/torsion fits with DESI data, or explicitly label this as “Liu et al., in preparation / private communication” and remove the quoted \(\Delta\mathrm{AIC}\) and σ-level agreement claims until they can be traced to a public source. Narrow any remaining text to a qualitative statement without specific AIC values unless those can be documented from a real paper.


## Finding 3 – PAPER-CITES-3 (MAJOR)

Claimed refs: “DESI2024”, “DESI2025DR2”  

Issue (Sec. 5.1, Sec. 7, conclusions):  
The manuscript refers to “DESI 2024 DR1 BAO [DESI2024]” and “DESI2025DR2” as established public data products and uses them as anchors for both the main Cobaya analyses and the forward‑looking \(w_0w_a\) chain, but the citation keys and descriptions do not map cleanly onto the actual DESI public releases visible on arXiv/publisher sites (titles, year, and “DR1 BAO” / “DR2 \(w_0w_a\)” structure are not uniquely identifiable), preventing readers from locating the exact BAO catalog and cosmology-analysis papers being used. [1][2]  

Fix (1–2 sentences):  
Replace generic keys like “DESI2024” and “DESI2025DR2” with precise citations to the official DESI data‑release and BAO cosmology papers (correct arXiv IDs, titles, and collaboration author lists) and state explicitly which catalog (e.g., DR1 BAO-only, DR2 full‑shape) and redshift samples are used. If some DESI inputs are internal or pre‑release, they must be labeled as such and not implied to be standard public DR1/DR2 products.


## Finding 4 – PAPER-CITES-4 (MAJOR)

Claimed ref: Fujita et al. ALP birefringence – “Fujita2021”  

Issue (Sec. 6):  
The text attributes the spectator-ALP model class to “Fujita et al. [Fujita2021]” but gives no arXiv ID or title, and the combination of year, topic (spectator ALP cosmic birefringence), and notation does not uniquely match a single Fujita‑authored ALP birefringence paper on arXiv/ADS; this creates ambiguity over which specific model and parameter ranges the author is adopting and whether the quoted parameter ranges and evolution equation really correspond to that work. [1][2]  

Fix (1–2 sentences):  
Disambiguate the Fujita reference by giving its exact arXiv identifier, full title, and journal venue, then check that the ALP potential, coupling normalization, and parameter ranges quoted in Sec. 6 match that specific work; if they differ, rewrite the attribution to distinguish clearly between what is imported from Fujita et al. and what is newly defined in this paper.


## Finding 5 – PAPER-CITES-5 (minor)

Claimed refs: Hehl 1976; Mercuri 2006 – torsion 4‑fermion term  

Issue (Sec. 3, “Scope of the \(\Delta N_{\rm eff}\) proxy” paragraph):  
The discussion cites Hehl (1976) and Mercuri (2006) for the statement that the surviving Einstein–Cartan–Holst parity‑even four‑fermion term is dimension‑6 and \(M_{\rm Pl}^{-2}\)-suppressed with leading effect a scattering‑amplitude shift rather than an effective \(\Delta N_{\rm eff}\) at recombination, which is broadly in line with the standard EC literature, but the paper never spells out which specific review/article (title, journal) is meant by “Hehl1976” (there are multiple Hehl 1970s EC papers), making the precise source of these cosmological inferences hard to verify. [1][2]  

Fix (1–2 sentences):  
Identify the exact Hehl and Mercuri papers being cited (e.g., full arXiv ID or journal reference) and verify that the cosmological interpretation used here—no effective relativistic species at recombination from the EC four‑fermion term—is explicitly supported there; if the cosmology extrapolation is the author’s own, state that explicitly rather than attributing it wholesale to those references.


## Finding 6 – PAPER-CITES-6 (nit)

Global bibliography / keys consistency  

Issue (multiple sections and Appendix A/B):  
Several in‑text citation keys (e.g., “DiegoPalazuelos2022”, “DiegoPalazuelos2025”, “Eskilt2022”, “Eskilt2022b”, “Walmsley2022”) are used without any explicit arXiv IDs or DOIs, and the LaTeX source does not show the associated BibTeX entries, so a referee cannot easily confirm that author lists, titles, venues, and years are all correctly matched; this is particularly fragile for recent 2022–2025 cosmology results where multiple similarly‑named preprints exist. [1][2]  

Fix (1–2 sentences):  
Expose the full BibTeX entries in the .bbl (or in an appendix for the submission) and ensure each key maps to a unique, real reference with correct metadata; for recent arXiv‑only works include arXiv IDs explicitly in the bibliography so that every observational and theoretical claim can be traced to an identifiable public source.
