# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v132verify_P4_v1_0_132
**Wall time**: 33.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=101376, completion=1423, total=102799

---

## PAPER-PER-B1 – Shamir 2022 sample description (MAJOR)

The main text states that Shamir (2022) “describes the analyzed DESI Legacy sample as nearly \(1.3\times10^{6}\) spiral galaxies,” and later contrasts this with \(\sim2\times10^{5}\) spirals after Ganalyzer cuts.[0] In the Shamir 2022 DESI paper, the “nearly \(1.3\times10^{6}\)” figure refers to all input galaxies, while the spin-analysis sample is \(\sim2\times10^{5}\) spirals after morphological cuts.[2] That’s what the author intends to say elsewhere, but the wording “spiral galaxies” attached to \(1.3\times10^{6}\) is inaccurate and conflates input vs final spiral subset.[2]

**Fix (1–2 sentences:** Rephrase both Shamir-2022 passages so that “nearly \(1.3\times10^{6}\) galaxies” are clearly labeled as the input DESI Legacy pool, and explicitly state that the spiral sample used in the chirality analysis is \(\sim2\times10^{5}\) after Ganalyzer morphological cuts (matching the MNRAS paper and arXiv abstract wording).[2]

---

## PAPER-PER-M1 – CE-ResNet citation metadata (nit)

The CE-ResNet reference is given as an ApJ article with DOI `10.3847/1538-4357/aca8aa` and the title “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” which matches the arXiv record and ApJ acceptance notice.[3] However, the in-text parenthetical “ApJ 943, 32 (2023)” appears only once near the end and not in the main introduction the first time CE-ResNet is described; the main CE-ResNet introduction mentions only “Jia et al. (2023)” without journal/volume, which is stylistically incomplete for MNRAS/PRD/JCAP style but not factually wrong.[3]

**Fix:** At the first detailed introduction of CE-ResNet, add the ApJ volume and page (“ApJ 943, 32”) alongside the existing arXiv/DOI info so that the primary reference is consistently formatted where it is first used; no change to IDs or titles is needed.[3]

---

## PAPER-PER-M2 – DESI Legacy Surveys overview citation (nit)

The DESI Legacy imaging description correctly cites Dey et al. (2019) and gives arXiv:1804.08657 with the title “Overview of the DESI Legacy Imaging Surveys,” which matches the arXiv record and AJ publication.[4] The text also notes that it is “Astron. J. 157, 168 (2019)” elsewhere, consistent with the official DOI 10.3847/1538-3881/ab089d.[4] There is no fused metadata here, but one of the parenthetical notes still refers to “AJ 157, 168 (2019)” without the DOI, while a later bib entry adds the DOI; that’s just minor style inconsistency, not a citation error.[4]

**Fix:** Standardize the Dey et al. reference in the main text to match the bibliography (AJ 157, 168, 2019, DOI 10.3847/1538-3881/ab089d) the first time it appears, and avoid repeating a slightly different shorthand later.

---

## PAPER-PER-M3 – Shamir 2020 SDSS+Pan-STARRS description (minor)

The manuscript summarizes Shamir (2020) as “SDSS DR8 + Pan-STARRS, \(\sim6.4\times10^{4}\) SDSS spirals plus \(\sim3.3\times10^{4}\) Pan-STARRS galaxies after morphological filtering” and as a “parity-violation multipole framing” paper.[0] The arXiv version of Shamir 2020 indeed describes \(\sim6.4\times10^{4}\) SDSS galaxies and \(\sim3.3\times10^{4}\) Pan-STARRS galaxies (though he doesn’t always qualify them explicitly as “spirals” in the abstract) and is explicitly framed in terms of “parity violation and multipoles” in title and discussion.[1] The numbers and qualitative description are therefore accurate, but the wording “spirals” could be tightened to “galaxies classified as spirals by Ganalyzer” to avoid implying a visually vetted spiral sample.[1]

**Fix:** Replace “\(\sim6.4\times10^{4}\) SDSS spirals plus \(\sim3.3\times10^{4}\) Pan-STARRS galaxies” with “\(\sim6.4\times10^{4}\) SDSS and \(\sim3.3\times10^{4}\) Pan-STARRS galaxies classified as spirals by Ganalyzer,” preserving the counts but aligning the phraseology with Shamir (2020).[1]

---

## PAPER-PER-N1 – Shamir 2020/2022 arXiv IDs, titles, DOIs (nit)

For Shamir (2020) and Shamir (2022) the manuscript gives arXiv IDs 2007.16116 and 2208.13866, the correct titles, and for the 2022 paper the MNRAS reference “MNRAS 516 2281, DOI 10.1093/mnras/stac2372,” all of which match the arXiv and publisher records.[1][2] There is no mixed-up ID or title, and the “parity-violation multipole framing” description is consistent with the 2020 paper’s title and abstract; this is a clean citation chain.[1][2]

**Fix:** None needed; keep as is.

---

## BLOCKER status

I do not see any new BLOCKER-grade citation-chain issues introduced by the v1.0.131→v1.0.132 edits; the Shamir and CE-ResNet references all point to real papers with correct IDs, titles, and venues, and the only substantive issue is the loose “1.3×10^6 spiral galaxies” wording for Shamir 2022, which is easily fixed and does not affect core results.[1][2][3]


