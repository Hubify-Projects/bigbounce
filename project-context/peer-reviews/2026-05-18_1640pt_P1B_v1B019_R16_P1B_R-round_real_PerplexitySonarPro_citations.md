# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1640pt_P1B_v1B019_R16
**Wall time**: 19.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18634, completion=1722, total=20356

---

## PAPER-PER-B1 — Incorrect Planck birefringence citation (BLOCKER)

Paper location: Abstract and Sec. 4, Eq. (29) “Planck NPIPE” value and combined constraint.

Issue: The text cites “DiegoPalazuelos2022” as giving a Planck NPIPE birefringence measurement \(\beta = 0.30^\circ \pm 0.11^\circ\) and uses it in the inverse-variance combination, but the DES paper with that arXiv-style tag (the time-dilation DES SN paper) is “The Dark Energy Survey Supernova Program: Slow supernovae show cosmological time dilation out to \(z \sim 1\)” and has nothing to do with cosmic birefringence or Planck NPIPE polarization measurements.[2] This indicates that at least one of: (a) the arXiv ID, (b) the year, or (c) the author-tag “DiegoPalazuelos2022” is mismatched to the intended Planck NPIPE birefringence paper.

Fix: Identify the correct Planck NPIPE birefringence paper (authors, title, year, arXiv ID) that reports the quoted \(\beta\) value, replace the DiegoPalazuelos2022 BibTeX entry with the correct citation, and ensure that all uses of the Planck-only \(\beta\) value point to that corrected reference.

---

## PAPER-PER-B2 — Eskilt joint Planck+ACT reference metadata incomplete/uncertain (MAJOR)

Paper location: Abstract and Sec. 6, “Eskilt2022b” joint Planck+ACT value \(\beta=0.342^\circ\pm0.094^\circ\) at \(3.6\sigma\).

Issue: Eskilt’s joint Planck+ACT cosmic-birefringence work is plausibly a real result, but in the present draft there is no explicit arXiv ID, journal, or full title given; the “Eskilt2022b” tag is therefore not externally verifiable as written, and I cannot confirm that it in fact reports exactly \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\) from any of the tool-accessible records.[2] This leaves a key load-bearing observational constraint effectively uncited.

Fix: Look up the Eskilt joint Planck+ACT birefringence paper on arXiv/ADS, then update the BibTeX entry so that “Eskilt2022b” includes the correct authors, title, arXiv ID, and journal information matching the quoted \(\beta\) value and significance. Check that the numerical values in the text agree with the paper’s abstract or results section and adjust if needed.

---

## PAPER-PER-B3 — DESI DR2 and DES-SN5YR citations under-specified (MAJOR)

Paper location: Sec. 3 “Independent cross-validation” and Conclusions (“Liu et al. 2025 EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018”), plus references to DESI DR2 BAO and DES-SN5YR SN in Table 1B caption and forward-looking text.

Issue: The draft names DESI DR2, DESI DR2 BAO, and DES-SN5YR but does not give explicit arXiv identifiers, full titles, or collaborations for the DR2 cosmology/BAO and DES-SN5YR supernovae papers, making it impossible to verify that the cited datasets and redshift/likelihood details actually match the described usage.[2] The only DES paper visible via tools is the DES SN time-dilation analysis, which is a different topic and not the “DES-SN5YR” cosmology-release paper.

Fix: Identify the correct DESI DR2 cosmology/BAO paper(s) and the DES-SN5YR supernova cosmology release (full titles, authors, arXiv IDs, journal venues), then update the BibTeX entries so the citations in the text (DESI2025DR2, DES2024SN5YR, etc.) unambiguously map to those works and reflect their actual scope (BAO-only vs full-shape, SN-only vs joint analysis).

---

## PAPER-PER-m1 — DES time-dilation paper mislabelled as birefringence-related (minor)

Paper location: Bibliography tag implied by “DiegoPalazuelos2025” / “DiegoPalazuelos2022” vs the DES time-dilation paper arXiv:2406.05050.

Issue: The tool-accessible DES paper “The Dark Energy Survey Supernova Program: Slow supernovae show cosmological time dilation out to \(z \sim 1\)” (arXiv:2406.05050) has lead author White et al. and is unrelated to CMB EB cosmic birefringence or to authors named Diego Palazuelos.[2] Using a 2024 DES SN paper as the backing record for a 2022–2025 CMB birefringence measurement is therefore a clear metadata mismatch, even if the bibkey “DiegoPalazuelos2025” happens to exist in the unseen .bib file.

Fix: Audit the .bib entries behind “DiegoPalazuelos2022” and “DiegoPalazuelos2025”; if either points to arXiv:2406.05050 or other DES SN work, split the entries so that DES SN time-dilation/cosmology papers have their own correctly labelled keys, and reassign the birefringence citations to the appropriate Planck/ACT EB spectra papers.

---

## PAPER-PER-m2 — Missing arXiv/journal metadata for key cosmology tools (minor)

Paper location: Sec. 5.1 (“We analyze four dataset combinations… DESI 2024 DR1 BAO… DES Y3 S8… Parameter estimation uses Cobaya (v3.5 original; v3.6.1 verification) with stock CAMB…”).

Issue: The text gives internal shorthand keys (e.g. DESI2024, DES2024, Cobaya2021, Planck2018params) but tools cannot confirm the mapping because no explicit arXiv IDs or titles are visible for these staples (Planck 2018 cosmology parameters, Cobaya code paper, DESI DR1 BAO, DES Y3 S8) in the current snippet.[2] This is weaker than it needs to be for reproducibility, even though these references almost certainly exist and are standard.

Fix: Ensure that the BibTeX entries for Planck 2018 parameters, Cobaya, DESI DR1 BAO, and DES Y3 S8 include unambiguous arXiv IDs and titles, and, optionally, mention these IDs once in the main text (e.g. in the datasets subsection) so that a reader can directly match the shorthand keys to the underlying publications.

---

## PAPER-PER-n1 — LiteBIRD forecast citation under-specified (nit)

Paper location: Sec. 6 “LiteBIRD forecast” sentence citing “LiteBIRD2023”.

Issue: The LiteBIRD sensitivity claim \(\sigma(\beta)\approx 0.03^\circ\) is attributed to “LiteBIRD2023” without specifying which design/white-paper (mission overview vs polarization-forecast paper) is meant; tools cannot confirm the match to a specific 2023 LiteBIRD publication.[2] This is a low-stakes but slightly opaque citation.

Fix: Replace “LiteBIRD2023” with a BibTeX entry corresponding to the actual LiteBIRD science- or forecast-paper (authors, title, arXiv ID), and confirm that it indeed gives a birefringence angle sensitivity at the quoted level; if the forecast is only for generic polarization, clarify how that maps to \(\sigma(\beta)\).
