# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v32verify_P5_v0_1_32
**Wall time**: 17.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29443, completion=1338, total=30781

---

## PAPER-PER-B1 — Alexander & Yunes 2009 metadata and usage

**Severity:** MAJOR  

The bibliography entry for Alexander & Yunes has correct authors, year, title, journal, volume, page, DOI, and arXiv ID; it is a real Phys. Rep. review exactly titled “Chern–Simons Modified General Relativity.” The text correctly invokes it as an example of Chern–Simons–style parity-violating gravity in the EFT operator paragraph, which is consistent with the content of the review (leading-order gravitational parity violation and Chern–Simons couplings), so there is no semantic misuse relative to what the paper actually covers.  

**Fix:** No change needed; this item only confirms that the M3 closure for Alexander & Yunes landed cleanly.

---

## PAPER-PER-B2 — Lue–Wang–Kamionkowski 1999 metadata and usage

**Severity:** MAJOR  

The bibliography entry for Lue, Wang & Kamionkowski has correct authors, year, title, journal (Phys. Rev. Lett. 83, 1506–1509), and arXiv ID astro-ph/9812088, and the title matches exactly “Cosmological Signature of New Parity-Violating Interactions.” The main text references it as an example of a chiral–gravitational-wave / parity-violating cosmological coupling, which is consistent with the paper’s focus on CMB signatures of new parity-violating interactions, so the citation is semantically appropriate.  

**Fix:** No change needed; this item only confirms that the M3 closure for Lue–Wang–Kamionkowski landed cleanly.

---

## PAPER-PER-M1 — Chern–Simons review not explicitly tied to density-gradient operator

**Severity:** minor  

The ALP-density-gradient EFT operator is introduced as “e.g. a Chern–Simons-style coupling in the Alexander & Yunes sense,” but Alexander & Yunes 2009 review Chern–Simons terms involving a pseudoscalar coupled to \(R\tilde R\), not to \(\nabla\rho\), so the mapping is heuristic rather than directly realized in that paper. As written, a reader could over-interpret this as “Alexander & Yunes 2009 write down this specific density-gradient operator,” which they do not.  

**Fix:** Add one clarifying clause where the operator is introduced: e.g. change “(e.g. a Chern–Simons-style coupling in the Alexander & Yunes sense…)” to “(e.g. in analogy with Chern–Simons–style parity-violating gravity as reviewed by Alexander & Yunes, though that work couples \(\phi\) to \(R\tilde R\), not directly to density gradients…)” to avoid implying the operator appears in that reference.

---

## PAPER-PER-M2 — Lue–Wang–Kamionkowski link to operator form is implicit

**Severity:** minor  

The text cites Lue–Wang–Kamionkowski 1999 as an example of “a chiral-gravitational-wave coupling” in the same breath as the explicit density-gradient operator, but that paper discusses parity-violating interactions via CMB polarization signatures, not the specific \((\nabla_i\phi)(\nabla^i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\) structure written here. The intended use is as a general exemplar of cosmological parity-violating interactions, which is correct, but the current phrasing can be read as if that exact operator structure is drawn from LW&K.  

**Fix:** Slightly rephrase the parenthetical to e.g. “(…in the spirit of Chern–Simons–type gravity as reviewed by Alexander & Yunes and of the parity-violating cosmological interactions studied by Lue, Wang & Kamionkowski…)” so it is clear these are conceptual precedents, not the source of the specific operator.

---

## PAPER-PER-M3 — Missing arXiv and journal metadata for several key references

**Severity:** minor  

Several cosmology and structure-formation references in the bibliography (Hahn 2007, Hoffman 2012, Cautun 2014, Planck 2018, Tempel 2014, Shamir 2022, Douglass et al. 2025, Zapata-Zuluaga et al. 2026, DESI T-Web 2026) are given with plausible author/title/journal strings but, unlike Alexander & Yunes or Lue–Wang–Kamionkowski, omit arXiv IDs and DOIs even though such identifiers exist and are standard for these works. This is not a confabulation problem — the titles and venues match the real papers — but the inconsistent inclusion of arXiv/DOI metadata makes it harder to check that the exact versions cited correspond to the described analyses.  

**Fix:** For each of these bibliography entries, add the arXiv ID and (where available) DOI in the same style used for Alexander & Yunes and Lue–Wang–Kamionkowski, ensuring that the arXiv number, title, authors, and journal reference are cross-verified against arXiv/ADS or publisher records.

---

## PAPER-PER-M4 — Internal “companion paper” placeholders for Papers II/IV

**Severity:** nit  

The entries for the author’s own “Paper IV” and “Paper II” are given as internal companion drafts with Git paths instead of conventional publication metadata, and the main text occasionally treats them like established external literature (e.g. “Paper IV… ApJ 982, 38” style venue is not present here). While this is acceptable at draft stage, it blurs the distinction between peer-reviewed external references and internal in-prep documents.  

**Fix:** Explicitly label these in the bibliography as “in preparation” or “submitted,” and, once arXiv IDs or journal references exist, replace the internal path-only citation with standard arXiv/journal metadata so it is clear to an external reader which references are archival and which are internal project documents.
