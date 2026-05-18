# P1B_v1B018_R14 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1500pt
**Wall time**: 22.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18161, completion=1758, total=19919

---

## PAPER-PER-B1 — Mis-citation of Liu et al. EC torsion paper (BLOCKER)

**Location:** Sec. 3, “Independent cross-validation”, sentence starting “Liu et al. constrained an EC torsion model…” and citations `\cite{ECTorsionDESI2025,DESI2025DR2,Brout2022PantheonPlus,DES2024SN5YR}`.  

**Issue:** I cannot locate any EC torsion paper matching the described combination “Liu et al., DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, torsion preferred by AIC (ΔAIC = −5.7 to −6.6)” in arXiv/ADS or publisher databases; the cited key `ECTorsionDESI2025` appears to point to a non-existent or placeholder reference and looks LLM‑fabricated as a composite of “EC torsion + DESI”.[1]  

**Fix:** Either (a) replace this with a real, verifiable reference that actually performs an EC torsion analysis with those datasets and AIC numbers, or (b) delete the paragraph and drop `ECTorsionDESI2025` from the bibliography; if a real but different EC paper is intended, correct the full metadata (authors, title, year, journal/arXiv ID, and dataset/AIC claims) to match the actual publication.

---

## PAPER-PER-B2 — DESI “2024 DR1 / 2025 DR2” naming & citation mismatch (MAJOR)

**Location:** Sec. 5.1 Datasets paragraph (“DESI 2024 DR1 BAO” \cite{DESI2024}) and later references to “DESI 2025 DR2” \cite{DESI2025DR2} in Sec. 6 and forward/claims sections.  

**Issue:** DESI publicly released DR1 BAO in 2024, but I cannot find a DESI “2024 DR1” BAO paper that matches the exact shorthand `DESI2024` plus a separate “DESI 2025 DR2” BAO cosmology reference with that exact key; the DR2 cosmology paper cited as “DESI 2025 DR2” appears to be real, but the internal naming here risks fused metadata (year/DR labels vs BibTeX keys vs actual titles) and could be referencing the wrong or an earlier DR1 BAO summary for the DR2-based results that are claimed.[1]  

**Fix:** Explicitly align each DESI citation with the correct published paper: confirm whether the iter2 \(w_0w_a\) chain uses DR2 (then cite the official DR2 BAO/cosmology paper only) and, if DR1 is also used elsewhere, clearly separate “DR1” and “DR2” in both text and BibTeX, with accurate titles, authors, years, and arXiv IDs.

---

## PAPER-PER-B3 — Eskilt et al. “joint Planck+ACT” ID and title not specified, risk of fused metadata (MAJOR)

**Location:** Abstract and Sec. 6, “Headline observational constraint” citing `\cite{Eskilt2022b}` as the “published Eskilt et al. joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ)”.  

**Issue:** Eskilt and collaborators have multiple birefringence papers (Planck-only and joint Planck+ACT analyses) with similar years and overlapping author lists, and without an explicit arXiv ID or journal reference here, it is ambiguous which paper `Eskilt2022b` is; that ambiguity creates a real risk that the BibTeX entry combines the title/venue of one Eskilt paper with the β = 0.342° ± 0.094° result from another (i.e., fused metadata).[1]  

**Fix:** In the bibliography, ensure `Eskilt2022b` is a single real paper that explicitly reports the joint Planck+ACT β = 0.342° ± 0.094° (3.6σ) result, with correct title, author list, arXiv ID, and journal reference; if that β value actually comes from a different paper than currently cited, split into two correctly labeled entries and make sure the in‑text citation points to the one that actually contains the β measurement.

---

## PAPER-PER-M1 — Diego Palazuelos birefringence citations lack disambiguation, possible confusion of 2022 vs 2025 papers (minor)

**Location:** Abstract (Planck/ACT DR6 references `\cite{Eskilt2022,DiegoPalazuelos2025}`), Sec. 4 first sentence (`\cite{DiegoPalazuelos2022,DiegoPalazuelos2025}`).  

**Issue:** There are distinct Planck NPIPE and ACT DR6 birefringence analyses associated with Diego Palazuelos et al., but the text only gives generic keys “DiegoPalazuelos2022” and “DiegoPalazuelos2025” without unambiguous arXiv IDs; given multiple related works, there is a realistic risk that the 2022 key points to a different NPIPE-focused paper than the one actually reporting β = 0.30° ± 0.11°, or that the 2025 key conflates an ACT instrument/analysis paper with the specific DR6 β measurement.[1]  

**Fix:** Verify that each BibTeX entry “DiegoPalazuelos2022” and “DiegoPalazuelos2025” uniquely corresponds to the cited β values and experiment (Planck NPIPE vs ACT DR6), and update titles, arXiv IDs, and year tags as needed; if another paper has the β numbers, correct the keys or add a new entry and cite that instead.

---

## PAPER-PER-m2 — Fujita et al. ALP model reference underspecified (minor)

**Location:** Sec. 6 opening note: “The model class was previously studied by Fujita et al. [\cite{Fujita2021}].”  

**Issue:** Multiple Fujita et al. ALP/axion papers exist around 2021, some on inflationary axion dynamics rather than late‑time cosmic birefringence, and without an explicit title/arXiv ID it is not guaranteed that `Fujita2021` really matches “spectator ALP cosmic birefringence with \(f_a \sim M_{\rm Pl}, m \sim H_0\)” as described.[1]  

**Fix:** Confirm that the chosen Fujita et al. paper actually studies late‑time ALP-induced birefringence in the parameter regime used here; if not, replace `Fujita2021` with the correct ALP‑birefringence reference (title, arXiv ID, journal) or add an additional citation that explicitly covers the spectator‑ALP cosmic birefringence model.

---

## PAPER-PER-n1 — LiteBIRD forecast citation vague, likely not to the main β-forecast paper (nit)

**Location:** Sec. 6 “LiteBIRD forecast” paragraph citing `\cite{LiteBIRD2023}` for “σ(β) ≈ 0.03°”.  

**Issue:** LiteBIRD has a broad set of collaboration papers and design reports, several in 2022–2023; without an explicit arXiv ID or journal citation, it is unclear whether `LiteBIRD2023` refers to the main mission “LiteBIRD science goals/design” paper that actually contains the specific σ(β) ≈ 0.03° forecast, or to a more general overview that does not quote that number.[1]  

**Fix:** Point `LiteBIRD2023` to the specific LiteBIRD paper that publishes the β forecast used (correct title, full author list, arXiv ID, and journal reference); if the σ(β) value comes instead from a conference proceeding or separate forecast note, add that as a distinct citation and use it for the numerical claim.
