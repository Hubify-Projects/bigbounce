# P4_v1094 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0100pt_P4_v1094_R13_R-round_real
**Wall time**: 15.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=82065, completion=1060, total=83125

---

## PAPER-PER-B1 — Ivezic LSST citation mismatch (BLOCKER)

**Location:** Bibliography, entry `\bibitem{Ivezic:2019}` and nearby discussion.

**Issue:** The paper claims that the LSST reference design article in ApJ 873, 111 (2019) is associated with arXiv:0805.2366, but 0805.2366 is the older LSST Science Book preprint, not the later ApJ “From science drivers to reference design and anticipated data products” article.[1] This is a fused metadata error (journal article details + older arXiv ID).

**Fix:** Replace the arXiv ID with the correct one (arXiv:0805.2366 should be clearly marked as the Science Book if kept, and the ApJ 873, 111 article should have its own correct arXiv or DOI metadata) or separate the two references cleanly as distinct items with accurate titles, authors, and identifiers.

---

## PAPER-PER-M1 — Shamir 2020 metadata is correct (MAJOR – confirmatory)

**Location:** Bibliography `\bibitem{Shamir:2020}` and main text references to “Shamir (2020)”.

**Issue:** The citation is to “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles”, Ap&SS, 2020, with arXiv:2007.16116.[0] This exactly matches the real paper’s title, author, venue, and arXiv ID, so the metadata is internally consistent and non‑confabulated.[0]

**Fix:** None needed. Keep as-is; this citation is sound.

---

## PAPER-PER-m2 — CE-ResNet Jia et al. 2023 metadata is correct (minor – confirmatory)

**Location:** Bibliography `\bibitem{Jia:2023}` and discussion of CE‑ResNet in Introduction/Methods.

**Issue:** The cited paper “Galaxy Spin Classification. I. Z-wise versus S-wise Spirals with the Chirality Equivariant Residual Network” in ApJ 943, 32 (2023) with arXiv:2210.04168 matches the actual paper in title, authors, journal, volume, page, and arXiv ID.[2] No evidence of title/ID fusion or wrong venue.

**Fix:** None. Leave the CE‑ResNet citation unchanged.

---

## PAPER-PER-m3 — Shamir 2012 citation is consistent (minor – confirmatory)

**Location:** Bibliography `\bibitem{Shamir:2012}` and discussion of early SDSS dipole claims.

**Issue:** The paper is cited as “Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis”, Phys. Lett. B 715, 25 (2012), arXiv:1207.5464, which matches the real PLB article (title, author, year, volume, pages, arXiv ID).[3] No confabulated mix of title, journal, or identifier is evident.[3]

**Fix:** None required; the citation is accurate.

---

## PAPER-PER-m4 — Shamir 2020/2022 DESI Legacy references look internally consistent (minor – to be double-checked)

**Location:** Bibliography `\bibitem{Shamir:2022DESI}` and associated text describing “Analysis of spin directions of galaxies in the DESI Legacy Survey”.

**Issue:** The text gives this as MNRAS 516, 2281 (2022) with the appropriate Shamir DESI Legacy spin‑direction title, and notes the DOI suffix stac2372 after correcting an earlier typo; ADS shows Shamir 2022 MNRAS 516, 2281 with that DOI and matching topic, so the combined title + journal + volume + DOI are coherent.[4] This looks like a previously‑fixed metadata bug now resolved.

**Fix:** None; just ensure the exact title matches the MNRAS version on final check before submission.

---

## PAPER-PER-n1 — Clarify LSST science-book vs reference-design roles (nit)

**Location:** Discussion §IX (future surveys / LSST) and `\bibitem{Ivezic:2019}`.

**Issue:** The current phrasing implies a simple one‑to‑one mapping between the long arXiv LSST Science Book and the later ApJ reference‑design paper, but they are related yet distinct documents; conflating them can confuse readers chasing a specific result.[1]

**Fix:** Add one sentence to clarify that arXiv:0805.2366 is the earlier LSST Science Book white paper, while the ApJ 873, 111 article is the later condensed reference‑design summary; cite them separately and only attribute claims to the document that actually contains them.
