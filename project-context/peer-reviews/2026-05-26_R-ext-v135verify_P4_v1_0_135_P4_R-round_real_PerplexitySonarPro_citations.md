# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v135verify_P4_v1_0_135
**Wall time**: 35.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=103934, completion=1629, total=105563

---

## PAPER-PER-B1 – Shamir 2022 DESI metadata

**Section/line:** Intro, Shamir (2022) paragraph; early Methods §1.1, Shamir comparison.

**Issue:** The text describes Shamir (2022) as “PASJ 2022” in one place and “MNRAS 516 2281, DOI 10.1093/mnras/stac2372” in another, but the only DESI-Legacy spin paper with arXiv:2208.13866 is “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372.[1] There is no PASJ version; the PASJ paper is Shamir 2022 on other content.

**Fix:** Ensure every reference to the DESI Legacy spin paper arXiv:2208.13866 is consistently labeled as MNRAS 516, 2281 (2022), DOI 10.1093/mnras/stac2372; do not call it PASJ anywhere. If a PASJ 2022 Shamir paper is also cited, give it its own distinct arXiv ID / journal line.

---

## PAPER-PER-M1 – Shamir 2020 SDSS+Pan-STARRS description

**Section/line:** Intro, Shamir (2020) summary paragraph.

**Issue:** The paper is cited correctly as arXiv:2007.16116 and described as SDSS DR8 + Pan-STARRS with “∼6.4×10⁴ SDSS spirals plus ∼3.3×10⁴ Pan-STARRS galaxies,” which matches the abstract (“~6.4·10⁴ SDSS … compared to ~3.3·10⁴ Pan-STARRS”).[0] However, it is also loosely tagged as “parity-violation multipole framing” without explicitly stating that Shamir’s emphasis is on quadrupole/dipole fits to spin asymmetry, not a clean parity-odd observable in the field-theory sense.[0]

**Fix:** Keep the counts and SDSS+Pan-STARRS description but soften the shorthand: e.g. “reported dipole and quadrupole alignments in spin-direction asymmetries” instead of “parity-violation multipole framing,” or add a clarifying clause that Shamir’s ‘parity violation’ is based on spin-count asymmetries and multipole fits, not on a direct Chern–Simons–type observable.

---

## PAPER-PER-m2 – CE-ResNet citation details

**Section/line:** Intro, CE-ResNet paragraph; Methods §2.2 (Training labels); comparison §4.2.

**Issue:** The CE-ResNet paper is cited as Jia et al. 2023 ApJ with arXiv:2210.04168 and DOI 10.3847/1538-4357/aca8aa, which matches ADS and arXiv (“Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32).[2][3] However, the text at one point abbreviates the title as “Galaxy Spin Classification. I. Z-wise versus S-wise Spirals with the Chirality Equivariant Residual Network” (ADS long form) and elsewhere uses “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network” (arXiv form).[2][3]

**Fix:** Pick one canonical title string (preferably the ApJ / arXiv one) and use it consistently in all bib entries and any in-text long-form mention, to avoid the appearance of fused metadata.

---

## PAPER-PER-m3 – Shamir 2020 / 2022 amplitude language

**Section/line:** Intro, Shamir comparison paragraph; Discussion §7.1, comparison to Shamir.

**Issue:** The text says “The ~2–4% asymmetry range is the union of the two papers’ reported amplitudes, not a single quoted value,” and attributes “~3% asymmetries with a consistent dipole axis” to Shamir 2020 SDSS+Pan-STARRS and similar magnitude for DESI Legacy.[0][1] Those magnitudes are qualitatively correct but Shamir 2020’s abstract emphasizes quadrupole alignments at >5σ–8σ with spin-count asymmetries that vary with direction/redshift, and Shamir 2022’s abstract emphasizes a hemisphere CW/CCW split and cosine dipole fits with P<10⁻⁵, not a single global 3% number.[0][1]

**Fix:** Rephrase to tie amplitudes to specific statistics: e.g. “Shamir (2020) reports direction‑ and redshift‑dependent spin-count asymmetries at the few‑percent level with significant quadrupole fits, and Shamir (2022) reports hemisphere spin-count differences at the few‑percent level with a cosine dipole fit at P<10⁻⁵; we loosely refer to these as a ~2–4% asymmetry range.”

---

## PAPER-PER-m4 – Journal / venue consistency for Shamir 2012

**Section/line:** Intro, first Shamir citation (“Shamir (2012)”).

**Issue:** The 2012 paper is correctly described as Phys. Lett. B 715, 25 (2012) with arXiv:1207.5464 in the bibliography (per the end references), and that matches ADS/arXiv metadata.[4] But in one comments block you mention “ApSS, accepted” in connection with arXiv:2007.16116 (2020), and elsewhere you call Shamir 2012 “the Ganalyzer algorithm” paper without explicitly naming the journal; this is just stylistic, but mixing in “ApSS accepted” near other Shamir references may confuse which paper that refers to.

**Fix:** In the main text, keep “Shamir (2012, Phys. Lett. B 715, 25, arXiv:1207.5464) introduced the Ganalyzer algorithm …” and reserve “Ap&SS, 2020, arXiv:2007.16116” for the 2020 paper; avoid putting “ApSS, accepted” in a generic Shamir context.

---

## PAPER-PER-n1 – ADS/ApJ vs arXiv titles for CE-ResNet (cosmetic)

**Section/line:** Bibliography entry for Jia et al. 2023.

**Issue:** ADS lists the ApJ article as “Galaxy Spin Classification. I. Z-wise versus S-wise Spirals with the Chirality Equivariant Residual Network,”[2] while arXiv uses “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network.”[3] Your bib entry mixes punctuation (“Classification I:” vs “Classification. I.”). This is a harmless stylistic nit, but worth standardizing.

**Fix:** Choose either the ApJ version (with period before “I.”) or the arXiv version (colon after “I”) and use it consistently in the bibliography; no change to arXiv ID, authors, or DOI is needed.
