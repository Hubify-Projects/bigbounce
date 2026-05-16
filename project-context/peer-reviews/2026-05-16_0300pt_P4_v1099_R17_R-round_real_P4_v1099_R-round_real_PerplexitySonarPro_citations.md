# P4_v1099 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0300pt_P4_v1099_R17_R-round_real
**Wall time**: 26.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=83784, completion=1697, total=85481

---

## PAPER-CIT-B1 — Fused SpArcFiRe metadata

**Location:** Sec. “SpArcFiRe” and nearby discussion in Conclusions; bib entry for Davis & Hayes.

**Issue:** The text asserts that the “published SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with 50/50 to within ∼0.3% at its ∼1.4×10⁵‑galaxy footprint,” and refers to “the public Hayes-Davis DR9 update,” but the cited paper (Davis & Hayes 2014, ApJ 790, 87, arXiv:1402.1910) does not present a DR9 spin-parity catalog of 1.4×10⁵ galaxies or a 0.3% parity measurement.[1] This looks like fused metadata: numerical results from an internal or unpublished catalog are being attributed to the 2014 ApJ article.

**Fix (1–2 sentences):** Replace the claim with what Davis & Hayes (2014) actually report (SpArcFiRe method, sample size, and qualitative parity tests if any), and either (a) clearly label the 1.4×10⁵ / 0.3% numbers as coming from your own DR9 re‑run of SpArcFiRe with an explicit internal or Zenodo reference, or (b) remove them if no citable public source exists. Ensure the bib entry for SpArcFiRe cites only the ApJ 790, 87 paper with its correct arXiv ID 1402.1910 and does not implicitly credit it with DR9 spin-parity statistics.[1]


## PAPER-CIT-M1 — Motloch & Pen interpretation overreach

**Location:** Sec. “Motloch & Pen (2021)” and surrounding discussion.

**Issue:** Motloch & Pen (Nature Astronomy 5, 283, 2021, arXiv:2003.04325) indeed detect a correlation between galaxy spins and the tidal field at ∼2σ, but the text goes further in suggesting that their signal may be “fully reducible” to the same citizen-science reading-direction bias that affects GZ1, without providing a specific quantitative comparison or pointing to a paper that demonstrates this.[2] That is interpretive rather than a supported citation about what Motloch & Pen actually show.

**Fix (1–2 sentences):** Rephrase this passage to state only what Motloch & Pen themselves report (a ∼2σ spin–tidal correlation in GZ2-based spins) and then describe your bias-based alternative as a hypothesis (“could in principle be contaminated…”), not as an implication of their paper. Remove any wording that implies their observed signal has been shown to be entirely due to reading-direction bias unless you add a specific, citable reanalysis that demonstrates that claim.[2]


## PAPER-CIT-M2 — CE-ResNet metadata need a clean pointer

**Location:** Multiple places citing Jia et al. 2023 CE‑ResNet; bibliography entry “Jia:2023”.

**Issue:** The text attributes CE‑ResNet to “Jia et al. 2023, ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa,” with arXiv:2210.04168, which matches the arXiv and DOI record; however, in a couple of narrative spots it still refers generically to “Jia et al. 2023” without giving an unambiguous title or journal, which makes it harder to confirm exactly which paper is meant in those passages.[1]

**Fix (1–2 sentences):** In the first mention in the main text, explicitly name the paper as “Jia, Zhu & Pen (2023), ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,’ ApJ 943, 32 (arXiv:2210.04168)” so that later shorthand references (“CE‑ResNet”) are unambiguous.[1]


## PAPER-CIT-n1 — Ivezic LSST citation cleaned but inconsistent

**Location:** Bibliography entry for Ivezić et al. (LSST) and brief discussion in Sec. “Future Directions”.

**Issue:** The bib entry now correctly cites Ivezić et al., ApJ 873, 111 (2019) with DOI 10.3847/1538-4357/ab042c, but elsewhere you still allude to the older LSST Science Book arXiv:0805.2366 as if it were the preprint for this specific ApJ paper, which it is not; 0805.2366 is a standalone white paper, not the preprint of ApJ 873, 111.[3]

**Fix (1–2 sentences):** Where discussing LSST, clearly distinguish between the LSST Science Book (arXiv:0805.2366) and the ApJ reference-design paper (ApJ 873, 111, 2019) instead of implying a one‑to‑one preprint–journal mapping. If you don’t actually use 0805.2366, drop its arXiv number entirely and cite only the ApJ paper for survey specifications.[3]


## PAPER-CIT-n2 — Shamir 2022 DESI paper citation is correct but mixed with earlier description

**Location:** Shamir (2022) DESI Legacy discussion and bib item “Shamir:2022DESI”.

**Issue:** The MNRAS DESI spin-direction paper is correctly identified as MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372.[4] However, nearby text still echoes older phrasing (“nearly 1.3×10^6 galaxies”) as though it were strictly the spiral subsample size, whereas in Shamir’s abstract that number refers to the full DESI Legacy sample analyzed, not a cleanly defined spiral subsample.[4]

**Fix (1–2 sentences):** Clarify that “nearly 1.3×10^6 galaxies” in Shamir (2022) refers to the full DESI Legacy sample he processes, and be explicit if you adopt a smaller effective spiral subsample for your amplitude comparison. Avoid phrasing that implies Shamir’s paper reports a 1.3×10^6 spiral-only catalog unless you quote an exact statement to that effect.[4]


## PAPER-CIT-n3 — Explicit note on CE‑ResNet catalog size and parity

**Location:** Early Introduction and Methods where you compare catalog sizes and parity balances for CE‑ResNet vs your catalog.

**Issue:** You quote CE‑ResNet as having a catalog of “1.95 million galaxies” and a CW/CCW ratio “CW/CCW = 0.998,” which agrees with the arXiv abstract’s statement that the CE‑ResNet classification reduces the original ∼7σ GZ1 imbalance to <1.8σ and is consistent with parity.[1] However, the phrase “1.95 million galaxies, all classified as CW or CCW since CE‑ResNet lacks a not-spiral class” is an interpretive gloss not literally spelled out in the abstract.

**Fix (1–2 sentences):** Add a parenthetical explicitly tying your “1.95 million, all CW/CCW” statement to the CE‑ResNet data release described in Jia et al. (2023) (ApJ 943, 32) or their tables/appendix where that number appears, so it’s clear this is drawn from their published catalog rather than inferred. If that exact count is only in code or supplemental material, say “≈2 million” in the prose and reserve “1.953 million” for a location where you also cite their table or data file.[1]

---


