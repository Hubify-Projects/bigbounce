# P4_v1086_R6 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_1935pt
**Wall time**: 22.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=77239, completion=1379, total=78618

---

## PAPER-PER-B1 – Mis-cited Motloch & Pen parity interpretation (MAJOR)

**Location:** Sec. \ref{sec:motloch}, around “fully consistent with the reading-direction bias previously quantified by Iye et al. (2020)…”.

**Issue:** The text asserts that Motloch & Pen’s claimed spin–tidal-field correlation is “fully consistent” with Galaxy Zoo reading-direction bias, effectively reinterpreting their signal as a labeling artifact, but Motloch & Pen (Nature Astronomy 5, 283, 2021) treat their result as evidence for a physical correlation and do not frame it as merely a manifestation of reading-direction bias.[1]

**Fix:** Rephrase to a neutral comparison: state that (i) Motloch & Pen find a marginal spin–tidal correlation in GZ2, (ii) Iye et al. 2020 and the present work demonstrate that GZ-style labels can contain reading-direction biases, and (iii) therefore part of their signal could, in principle, be contaminated—without claiming “fully consistent” or reinterpreting their conclusion.

---

## PAPER-PER-B2 – Overstated mapping to Cabass–Ivanov–Philcox EFT (MAJOR)

**Location:** Sec. \ref{sec:parity_translation}, discussion of Cahn–Slepian–Hou trispectrum and Cabass–Ivanov–Philcox EFT.

**Issue:** The text says the morphology-dipole channel and the parity-odd 4PCF “share parametric origins” and “can couple to the same dim-7 EFT amplitude \(g_*\)”, but Cabass, Ivanov & Philcox (2023, PRD 107, 023523) develop the mapping specifically for the parity-odd galaxy 4PCF, not for late-time morphology-based spin observables; the paper does not derive a concrete mapping from spiral-handedness to the same EFT operator.[2]

**Fix:** Soften to: “the two probes are conceptually complementary tests of parity-odd physics and may, in some models, be related through a common EFT sector; however, no explicit mapping from morphology-dipole bounds to \(g_*\) has been derived, so we do not translate our limit into that parameter.”

---

## PAPER-PER-M1 – Ivezic LSST citation framing (minor)

**Location:** Bibliography note on Ivezić et al. 2019 (LSST), plus the comment that “arXiv:0805.2366 is the long LSST Science Book preprint whose content underlies the cited ApJ 873, 111 article.”

**Issue:** The 2008 LSST Science Book (arXiv:0805.2366) and the 2019 ApJ “LSST: From science drivers to reference design and anticipated data products” share collaboration and theme but are distinct works; saying the arXiv content “underlies” the ApJ article is interpretive and not something the ApJ paper itself claims explicitly.[3]

**Fix:** Replace this with a strictly factual note: cite the ApJ paper in the main bib entry, and if you want to reference the Science Book, add a separate citation with a neutral description (“earlier, more extensive technical design document”), avoiding any implication of one being a direct preprint of the other.

---

## PAPER-PER-M2 – Over-strong statement about Shamir 2022 DESI sample size (minor)

**Location:** Sec. \ref{sec:comparison}, Shamir 2022 DESI Legacy description.

**Issue:** You write that your spiral subsample is “∼2.5× larger than the spiral sample analyzed by Shamir (2022)… (‘nearly \(1.3\times10^6\) spiral galaxies’ in DESI Legacy Survey data, per the published abstract)”. Shamir (2022, MNRAS 516, 2281) indeed states “nearly 1.3 million spiral galaxies” in the abstract but is less precise in the body about strict spiral-versus-total counts.[4]

**Fix:** Keep the catalog-scale comparison but explicitly flag it as based on the abstract language and not a strict like-for-like spiral-selection match, e.g. “using Shamir’s ‘nearly \(1.3\times10^6\) spiral galaxies’ wording as an approximate comparator, our 3.20M-spiral equivariant sample is ≈2.5× larger.”

---

## PAPER-PER-m3 – SpArcFiRe metadata fine point (minor)

**Location:** Sec. \ref{sec:sparcfire} and bib entry for Davis & Hayes 2014.

**Issue:** You correctly give ApJ 790, 87 and arXiv:1402.1910; the ADS record’s published abstract does not list a DOI string, whereas you leave the DOI field blank in the bib item. That’s acceptable, but the parenthetical “Submitted to ApJ. Letters” in the ADS e-print abstract is not part of the final journal metadata.

**Fix:** Ensure your bib entry reflects the final journal form only—journal, volume, page, year, arXiv ID—and drop any “Submitted to ApJ. Letters” phrasing (that is preprint-only and does not belong in the reference metadata).

---

## PAPER-PER-n1 – Clarify “Shamir DOI stac2342→stac2372” change (nit)

**Location:** Title-page round-context note and Shamir 2022 DESI MNRAS reference.

**Issue:** You note an internal correction “Shamir DOI stac2342→stac2372”, but MNRAS 516, 2281 (Shamir 2022 DESI spin-directions) indeed has DOI 10.1093/mnras/stac2372, while 10.1093/mnras/stac2342 is an unrelated eclipsing-binary paper; you now cite stac2372 correctly.[4]

**Fix:** Leave the bib entry as-is (it is now correct), but if you keep the round-context note, add a parenthetical “(earlier drafts mistakenly used the DOI suffix of an unrelated MNRAS paper; now corrected to stac2372)” so a referee sees clearly that the present metadata match the actual Shamir DESI article, not a fused reference.
