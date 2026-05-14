# P2_v17_28 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2310pt
**Wall time**: 28.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30469, completion=1500, total=31969

---

## PAPER-PER-B1 (MAJOR): Cai & Brandenberger 2014 arXiv ID is wrong

The text says: “CaiBrandenberger:2014 arXiv 1405.1097→1404.6968”. This is still incorrect: arXiv:1404.6968 is a “Computed-torque … orthosis” medical-physics paper, unrelated to cosmology or non‑Gaussianity, and clearly not Cai & Brandenberger’s “Non-Gaussianity in a Matter Bounce” / follow‑up matter-bounce work. [0]

Fix: Replace the arXiv identifier with the correct cosmology ID (e.g., for the main matter-bounce non‑Gaussianity paper use arXiv:0903.0631 “Non-Gaussianity in a Matter Bounce”) and ensure the BibTeX key “CaiBrandenberger:2014” points to the actual Cai–Brandenberger cosmology article (correct title, authors, and journal). [1]

---

## PAPER-PER-B2 (minor): Cabass et al. metadata description slightly off

The text describes “Cabass:2022 PRL 129/2201.11518→PRD 106/2204.01781”. The cited paper arXiv:2204.01781 is indeed “Constraints on Multi-Field Inflation from the BOSS Galaxy Survey” by Cabass, Ivanov, Philcox, Simonović, and Zaldarriaga, published in Phys. Rev. D 106, 043506 (2022), with DOI 10.1103/PhysRevD.106.043506. [3] There is no PRL 129 version of this work; the “129/2201.11518” combination is a fused reference to a different PRL article plus another arXiv entry.

Fix: State the Cabass et al. reference simply as “Phys. Rev. D 106, 043506 (2022), arXiv:2204.01781” and remove mention of the spurious “PRL 129/2201.11518” lineage, which mixes metadata from distinct papers. [3]

---

## PAPER-PER-B3 (nit): Incomplete metadata for Cai et al. 2009

The main matter-bounce bispectrum reference is to Cai et al. 2009, correctly associated with arXiv:0903.0631 (“Non-Gaussianity in a Matter Bounce”) by Cai, Xue, Brandenberger, and Zhang, in astro‑ph.CO. [1] However, no journal reference or DOI is given in the text, and the prose sometimes calls it “Cai et al. 2009” and sometimes “Cai et al.” without year, which can hinder unambiguous tracing in a long paper.

Fix: Standardize the citation as “Cai et al. (2009), arXiv:0903.0631 [astro‑ph.CO]” and, if available in your .bib file, include the journal reference/DOI in the bibliography entry so it is easy to verify against arXiv/ADS. [1]

---

## PAPER-PER-B4 (minor): Stated “bib fix” for CaiBrandenberger:2014 remains unverified

You assert that in v1.7.28 “CaiBrandenberger:2014 arXiv 1405.1097→1404.6968” is a fixed metadata issue, implying the old ID 1405.1097 was also associated with Cai & Brandenberger. A direct lookup shows 1404.6968 is unrelated medical-physics work, and 0903.0631 is the actual “Non-Gaussianity in a Matter Bounce” paper. [0][1] This means the bib “fix” itself is not grounded in any cosmology paper and therefore does not currently “correct” the earlier error.

Fix: Explicitly audit the Cai–Brandenberger entry in the .bib file by title/author, then set its arXiv number to the actual cosmology preprint (e.g., 0903.0631 for the 2009 non‑Gaussianity paper, plus the correct ID for the 2014 follow‑up if that is what “:2014” was meant to denote), and remove any reference to 1404.6968. [0][1]

---

## PAPER-PER-B5 (MAJOR): Ambiguous mapping of “CaiBrandenberger:2014” key to actual article

Throughout the text you discuss a factor-of-two discrepancy “Cai et al. vs Li & Brandenberger” and later refer to “CaiBrandenberger:2014” as if it were the Li & Brandenberger (or Cai & Brandenberger) follow‑up matter‑bounce bispectrum paper. However, in the supplied “bib fixes” note this same key is mapped to arXiv:1404.6968, which is a robotic orthosis control paper with no overlap in authors, title, or field. [0] This creates a situation where a cosmology discussion in the body text points to a completely different subject in the reference list.

Fix: Decide which specific cosmology paper you mean by “CaiBrandenberger:2014” (title, authors, year), then assign that .bib key to the correct arXiv ID and journal entry; remove or rename any unrelated entry that currently uses that key so that in-body citations resolve to an actually relevant paper. [0]

---

## PAPER-PER-B6 (nit): Explicit check of Heinrich et al. and Cabass et al. titles/venues passes

The abstract and body cite “Heinrich et al. 2023, PRD 109, 123511” and “Cabass et al. 2022, PRD 106, 043506 (arXiv:2204.01781)” as the SPHEREx and BOSS LPNG analyses. The Cabass metadata matches arXiv:2204.01781 exactly: title, authors, subject class, and PRD 106 reference. [3] Although I could not cross‑check Heinrich’s PRD 109, 123511 in this tool round, your description—multi‑tracer SPHEREx bispectrum local‑PNG forecast—is consistent with the known Heinrich SPHEREx paper series, and there is no obvious fused metadata (title and arXiv ID 2204.01781 in the Cabass case are clearly for the same work). [3]

Fix: No change required for Cabass; for Heinrich, ensure in the .bib entry that the journal is “Phys. Rev. D 109, 123511 (2024 or 2023 as appropriate)” with its actual arXiv ID, and verify via ADS that the volume/page pair matches the SPHEREx bispectrum forecast title you describe.
