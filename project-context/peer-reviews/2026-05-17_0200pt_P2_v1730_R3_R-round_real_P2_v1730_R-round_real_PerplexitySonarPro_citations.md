# P2_v1730 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0200pt_P2_v1730_R3_R-round_real
**Wall time**: 16.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=31464, completion=1500, total=32964

---

## PAPER-PER-B1 — Mis-cited Cai et al. (2009) metadata

**Location:** Abstract, multiple places in Sec. 2, App. A; citation key `\cite{Cai:2009fn}`.  

**Issue:** The paper repeatedly attributes the matter-bounce bispectrum calculation to “Cai et al. 2009” with arXiv key `Cai:2009fn`, but the arXiv entry 0903.0631 is titled “Non-Gaussianity in a Matter Bounce” by Robert Brandenberger only and does not list Cai as an author, nor “Cai et al.” in that year.[0] This looks like fused metadata (author list + year vs. actual arXiv entry).  

**Fix:** Verify the correct arXiv ID, year, title, and author list for the intended matter-bounce bispectrum reference (likely Cai, Brandenberger, and collaborators) and update the citation key and in-text attributions everywhere from “Cai et al. 2009” / “Cai et al.” to the correct bibliographic entry (or change the arXiv ID if 0903.0631 is not the intended paper).  

---

## PAPER-PER-M1 — Heinrich et al. SPHEREx bispectrum forecast details

**Location:** Abstract (Heinrich et al. 2024 SPHEREx multi-tracer bispectrum σ=0.7, Fig. 6 / Table 3 claims) and Sec. 4 (“Heinrich et al. 2024” / “Heinrich:2023” throughout).  

**Issue:** The manuscript quotes specific numerical results and figure/table numbers for a “Heinrich et al. 2023/2024” SPHEREx multi-tracer bispectrum paper with σ(\(f_{\rm NL}^{\rm local}\)) ≈ 0.7 and 0.5, but the cited key `Heinrich:2023` and its exact bibliographic metadata cannot be verified here; this creates risk that the arXiv ID, year, or title in the `.bib` file do not actually match a real Heinrich+ SPHEREx bispectrum forecast with those precise numbers and figure/table labels.  

**Fix:** Cross-check the intended Heinrich et al. SPHEREx forecast on arXiv/ADS and ensure the `.bib` entry has the correct authors, title, year, journal status, and arXiv ID, and that the quoted σ values and references to “Fig. 6 / Table 3” match the real paper; if not, adjust the numbers and figure/table pointers or explicitly mark where you are recasting/combining results rather than quoting them directly.  

---

## PAPER-PER-M2 — Zhu & Cai (2026 echoes) plausibility

**Location:** Sec. 2.3, Assumptions, sentence “…as required by certain dark-energy mechanisms in modified-gravity bounce cosmologies; e.g., Zhu & Cai .”  

**Issue:** The citation key suggests a 2026 paper “Zhu:2026echoes”, but no such work can yet be verified; the title “echoes” and year 2026 look like placeholder / speculative metadata that may not correspond to a real arXiv entry or published article.  

**Fix:** Replace this with a verified, existing dark-energy–from–bounce reference with correct authors, title, and arXiv ID, or else clearly label this as hypothetical/future work and remove it from the formal bibliography until a real paper exists.  

---

## PAPER-PER-M3 — Li & Brandenberger normalization reference

**Location:** Abstract and App. A (discussion of “Li & Brandenberger (c=1) normalization” and “Li et al.”).  

**Issue:** The text attributes one normalization to “Li & Brandenberger” / “Li et al.” but the only verified older matter-bounce NG reference in this family at 0903.0631 is by Brandenberger alone.[0] Without a checked arXiv entry for a Li–Brandenberger paper containing \(\fnl = -35/16\), there is a risk of fused metadata (author pair plus result taken from a different source).  

**Fix:** Identify and cite the exact paper that actually reports \(\fnl = -35/16\) with its correct author list (which may or may not include Li), title, year, and arXiv ID; update all “Li & Brandenberger” / “Li et al.” mentions and the bibliography accordingly, or, if no such paper exists, recast this discussion in terms of “an alternative convention in the literature” with an accurate citation or remove the specific name.  

---

## PAPER-PER-m4 — Schlegel et al. (MegaMapper) metadata check

**Location:** Intro and Sec. 5, citations “MegaMapper ”.  

**Issue:** The manuscript describes MegaMapper as “a proposed Stage V spectroscopic facility” with σ(\(f_{\rm NL}\)) ≈ 0.5, citing Schlegel et al. 2022, but without confirming that the `.bib` entry actually matches the real MegaMapper white paper (correct title, author list including Schlegel, arXiv ID, and year).  

**Fix:** Verify that `Schlegel:2022` corresponds to the actual MegaMapper concept paper on arXiv (correct title and authors) and that the σ(\(f_{\rm NL}\)) ≈ 0.5 figure appears there; if the σ is instead from another forecast (e.g., combined analyses), split the citation and attribute each number to the correct source.  

---

## PAPER-PER-n1 — Doré et al. and Munchmeyer et al. lineage details

**Location:** Sec. 4 and elsewhere: “Doré et al.  (foundational SPHEREx galaxy-survey forecast paper; Munchmeyer et al.  is the CMB kSZ tomography companion forecast for the same parameter target).”  

**Issue:** While the existence of SPHEREx white papers and a kSZ forecast by Munchmeyer et al. is plausible, the exact attributions (years, roles, and the statement that Munchmeyer+2019 is specifically “the CMB kinetic-Sunyaev-Zel’dovich tomography companion forecast for the same parameter target”) may not match the actual titles and scopes of those papers unless carefully checked; this is a typical spot for fused or over-specific metadata.  

**Fix:** Confirm that `Dore:2014` indeed corresponds to the primary SPHEREx survey forecast paper and that `Munchmeyer:2019` is precisely a kSZ-tomography forecast with the described focus; if their scopes are broader/different, soften the language (e.g., “includes kSZ tomography constraints on local \(f_{\rm NL}\)”) and ensure titles, years, and arXiv IDs in the bibliography are correct.
