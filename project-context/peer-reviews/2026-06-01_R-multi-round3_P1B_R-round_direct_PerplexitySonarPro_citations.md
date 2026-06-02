# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 16.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=26838, completion=1594, total=28432, search_context_size=low, cost={'input_tokens_cost': 0.08051, 'output_tokens_cost': 0.02391, 'request_cost': 0.006, 'total_cost': 0.11042}

---

## PAPER-PER-B1 — Mis-cited DESI DR2 torsion paper

**Severity:** MAJOR  

**Location:** §3, “Independent cross-validation” paragraph, citation `\cite{ECTorsionDESI2025}` to “Liu et al. … DESI DR2 … EPJC 2025, arXiv 2507.04265”.  

**Issue:** There is currently no record on arXiv or in EPJC of a 2025 Einstein–Cartan / torsion cosmology paper by “Liu + Li + Xu + Biesiada + Wang” using DESI DR2 with identifier arXiv:2507.04265 or similar; ADS, arXiv, and publisher searches on this author set + topic + DESI DR2 yield no match.[ ] This looks like forward‑dated / non‑public work treated as a standard published reference.  

**Fix:** Reclassify this as “in preparation / private communication” if it is an internal or not‑yet‑posted analysis, remove the arXiv ID and journal venue, and soften the comparison text to “internal” or “unpublished” cross-check; alternatively, delete the paragraph until a real, citable paper exists and can be correctly referenced.  

---

## PAPER-PER-B2 — Eskilt & Komatsu 2022 dataset description slightly off

**Severity:** minor  

**Location:** Abstract and §6 “Headline observational constraint”, reference `\cite{Eskilt2022b}` described as “PR4 NPIPE + WMAP analysis”.  

**Issue:** Eskilt & Komatsu (2022) “Hints of cosmic birefringence in the CMB polarization data from WMAP and Planck” (Phys. Rev. D 106, 063503, arXiv:2205.13962) analyzes WMAP9 and Planck PR3 (2018) polarization data, not Planck PR4/NPIPE.[ ] Calling it “PR4 NPIPE + WMAP” overstates the Planck data release used.  

**Fix:** Change the text to “joint WMAP9 + Planck 2018 (PR3) analysis” or simply “joint WMAP + Planck analysis” without labeling it PR4/NPIPE, matching the actual dataset in the paper.  

---

## PAPER-PER-B3 — ACT DR6 birefringence reference partially synthetic

**Severity:** minor  

**Location:** Abstract, §4 “Data Methods: CMB E–B Analysis”, and §6 “Summary-likelihood combination”, `\cite{DiegoPalazuelos2025}` described as an ACT DR6 birefringence paper with value \(\beta=0.215^\circ\pm 0.074^\circ\) and arXiv year 2025.  

**Issue:** The main published cosmic-birefringence ACT analysis by Diego-Palazuelos et al. is PRL 128, 091302 (2022), arXiv:2201.07682, using ACT DR4/DR6-era data but not a 2025 arXiv “ACT DR6” paper with that title or year; no 2025 Diego-Palazuelos + Komatsu ACT DR6 birefringence paper matching the description can be found in arXiv/ADS.[ ] The 2025 metadata appears to fuse authors/subject with a not-yet-existent ACT DR6 release.  

**Fix:** For the currently published ACT birefringence measurement, cite Diego-Palazuelos et al. 2022 (PRL 128, 091302, arXiv:2201.07682) with its reported central value/uncertainty; if a newer ACT DR6 analysis truly exists but is not yet public, mark it as “in preparation / private communication” instead of giving a fabricated year/identifier.  

---

## PAPER-PER-B4 — ALP birefringence citation to Fujita et al. slightly mismatched in wording

**Severity:** nit  

**Location:** §6 opening note: “The model class was previously studied by Fujita et al. [\cite{Fujita2021}]”.  

**Issue:** Fujita et al. (Phys. Rev. D 103, 043509, arXiv:2011.11894) is titled “Isotropic cosmic birefringence and its implications for axionlike particles including dark energy”, focusing on ALP/DE interpretations of birefringence but not on the specific “spectator ALP with \(f_a\sim M_{\rm Pl}, m\sim H_0\)” construction used here.[ ] The current wording can be read as claiming that Fujita et al. studied exactly this spectator‑ALP scenario, which is stronger than what the paper actually covers.  

**Fix:** Rephrase to something like “Related ALP interpretations of birefringence were studied by Fujita et al.” or “See Fujita et al. for ALP-based explanations of isotropic birefringence,” avoiding the implication that they treated this exact model.  

---

## PAPER-PER-B5 — Eskilt & Komatsu value 0.342° ± 0.094° not explicit in paper

**Severity:** nit  

**Location:** Abstract and §6 “Headline observational constraint”, value “\(\beta = 0.342^\circ \pm 0.094^\circ\) (3.6σ)” attributed to Eskilt & Komatsu (2022) `\cite{Eskilt2022b}`.  

**Issue:** Eskilt & Komatsu report their best-fit birefringence and uncertainty in radians (and sometimes with slightly different central values/uncertainties depending on data subsets) rather than as exactly 0.342° ± 0.094°; that specific pair of numbers appears to be a rounded conversion/choice of one of several fits, not directly quoted.[ ] Treating it as “the published value” without stating that it is a rounded conversion may be slightly misleading.  

**Fix:** Clarify that 0.342° ± 0.094° is the degree-converted, rounded form of the Eskilt & Komatsu best fit (cite the original radian value), or quote their numbers directly and show the converted value parenthetically.  

---

## PAPER-PER-B6 — Literature σ(β) forecast for LiteBIRD mismatched

**Severity:** minor  

**Location:** §6 “LiteBIRD forecast,” citing LiteBIRD 2023 `\cite{LiteBIRD2023}` for “\(\sigma(\beta)\approx 0.03^\circ\)” (≈0.00052 rad).  

**Issue:** LiteBIRD forecasts for isotropic cosmic birefringence (e.g., in the LiteBIRD “Science Goals and Forecasts” papers and white papers) typically quote sensitivities in radians at the few×10⁻⁴–10⁻³ level depending on assumptions and foregrounds; none of the standard published forecasts is literally expressed as “0.03°”.[ ] The specific 0.03° value looks like a back‑of‑envelope conversion / rounding that is not obviously traceable to a single table entry.  

**Fix:** Replace “0.03°” with the forecast as it is actually stated in the LiteBIRD reference (in radians, with its quoted numerical value and conditions), and if you prefer degrees, explicitly mention that the degree value is your conversion of the published radian forecast.
