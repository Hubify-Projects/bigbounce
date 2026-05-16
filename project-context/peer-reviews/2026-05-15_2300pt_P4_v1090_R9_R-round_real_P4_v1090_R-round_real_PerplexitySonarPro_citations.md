# P4_v1090 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_2300pt_P4_v1090_R9_R-round_real
**Wall time**: 31.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=80787, completion=1794, total=82581

---

## PAPER-PER-B1 – Ivezic LSST paper: wrong arXiv linkage (MAJOR)

**Location**: Bibliography, ref. `Ivezic:2019` (near end of file).

**Issue**: The bib entry correctly cites the LSST overview paper as ApJ 873, 111 (2019), but then says “arXiv:0805.2366 … the long LSST Science Book preprint whose content underlies the cited ApJ 873, 111 (2019) reference-design article,” implying 0805.2366 is the preprint version of that ApJ article.[2] In fact, 0805.2366 is the LSST Science Book, a 2008 white paper, not the ApJ 873, 111 reference-design paper; the 2019 ApJ paper’s actual arXiv preprint is 0805.2366 *replaced by* 0805.2366? No – ADS shows ApJ 873, 111 with arXiv:0805.2366 *for the science book* and a different arXiv for the reference paper, so this is a fused mapping of journal reference and arXiv ID.[2]  

**Fix (1–2 sentences)**: Remove the explanatory note that 0805.2366 is the preprint of ApJ 873, 111 and instead either (a) drop the arXiv ID entirely and keep only the ApJ citation, or (b) replace the arXiv ID with the correct preprint for ApJ 873, 111 as given on ADS, keeping the Science Book as a separate, clearly labeled reference if you wish to cite it.

---

## PAPER-PER-B2 – Motloch & Pen mapping to “initial conditions” (minor)

**Location**: Sec. Motloch & Pen (around `\label{sec:motloch}`).

**Issue**: You say Motloch & Pen “report an observed correlation between galaxy spin directions and the large-scale tidal field, using Galaxy Zoo 2 … and interpret their marginal (∼2σ) signal as evidence for a physical spin–tidal-field correlation in the linear-theory framework of Yu et al. (2020).” In the paper, they indeed find a correlation and discuss it in terms of the tidal field, but the interpretation is framed cautiously as “evidence for alignment” rather than a strong detection with an agreed linear-theory mapping; the explicit tie to the Yu et al. tidal-tensor modelling is your synthesis, not their own statement.[1][2]  

**Fix (1–2 sentences)**: Soften the claim to something like “Motloch & Pen report a ∼2σ correlation between galaxy spins and the reconstructed large-scale tidal field using Galaxy Zoo 2 spirals, and discuss this in the context of tidal-torque expectations; here we note that, in principle, such correlations could be related to the tidal-tensor modelling of Yu et al. (2020), though that mapping is not derived in their paper.”

---

## PAPER-PER-B3 – Shamir 2022 DESI paper: numbers and description (minor)

**Location**: Introduction, paragraph beginning “In this paper we present a new chirality catalog…”, and multiple later mentions of “Shamir 2022 DESI Legacy” spiral counts.

**Issue**: You summarize Shamir (2022) DESI as “nearly 1.3×10^6 spiral galaxies in DESI Legacy Survey data, per the published abstract” and sometimes gloss this as “spiral sample analyzed by Shamir (2022).”[1] Shamir (2022) indeed quotes “nearly 1.3×10^6 galaxies” but that is his *total* sample; not all are necessarily high-purity spirals, and “spiral sample” reads as if the whole 1.3M are robust spirals in his own sense, which overstates his effective spiral count.[1]  

**Fix (1–2 sentences)**: Rephrase these comparisons to “nearly 1.3×10^6 galaxies analyzed with Ganalyzer in DESI Legacy data (per Shamir’s abstract), not all of which are necessarily high-purity spirals,” and explicitly state that your “∼2.5× larger spiral subsample” comparison is approximate and depends on how spirals are defined in Shamir’s pipeline.

---

## PAPER-PER-B4 – Shamir 2020 description of dataset makeup (nit)

**Location**: Introduction, “Shamir (2020) extended this to ∼10^5 galaxies from multiple surveys, reporting asymmetries of ∼3% with a consistent dipole axis.”

**Issue**: Shamir (2020) explicitly says he uses “∼6.4×10^4 SDSS spirals with spectra” and “∼3.3×10^4 Pan-STARRS galaxies,” and analyzes them separately and jointly, emphasizing the SDSS–Pan-STARRS consistency in both *dipole and quadrupole* patterns, not just a single “consistent dipole axis.”[2] Your summary compresses this into a single ∼10^5 multisurvey sample and only mentions the dipole axis, which is technically true but omits the explicit quadrupole focus and could be read as implying a single homogeneous 10^5-galaxy survey rather than two distinct samples.  

**Fix (1–2 sentences)**: Clarify to “Shamir (2020) analyzed ∼6.4×10^4 SDSS spirals with spectra and ∼3.3×10^4 Pan-STARRS galaxies, reporting ∼3% asymmetries with broadly consistent dipole and quadrupole axes between the two surveys,” which matches his wording more closely.

---

## PAPER-PER-B5 – CE‑ResNet agreement / numbers (nit)

**Location**: Sec. CE‑ResNet comparison (`\label{sec:ceresnet}`), Table \ref{tab:ceresnet_compare} and surrounding text.

**Issue**: You state CE‑ResNet “yields CW/CCW = 0.998” and describe your Catalog C as approaching this balance with CW/(CW+CCW) = 0.4974, i.e. “CW/CCW = 0.990.”[0] The CE‑ResNet paper itself reports a *ratio* of N_Z/N_S ≈ 0.998 (i.e. virtually symmetric), while your wording could be read as “fractions 0.998 vs 0.990,” mixing a ratio from one paper with a fraction from yours. That’s numerically consistent but semantically easy to misread as like-for-like statistics.  

**Fix (1–2 sentences)**: State explicitly that the CE‑ResNet “0.998” is a *Z-to-S number ratio*, and compare to your own *ratio* N_CW/N_CCW ≈ 0.990, or convert both papers to CW fraction and compare those; avoid mixing a quoted ratio from one paper with a fraction from another without saying so.

---

## PAPER-PER-B6 – SpArcFiRe coverage and “near-perfect” self-consistency (nit)

**Location**: Sec. SpArcFiRe (`\label{sec:sparcfire}`).

**Issue**: You write that SpArcFiRe “produces catalogs of ∼140,000 galaxies” and has “near-perfect self-consistency (99.983%).” Davis & Hayes (2014) describe running on ~644,000 SDSS objects with usable spiral-arm segments, and report high—but not literally “99.983%”—agreement metrics; the 140k and 99.983% figures reflect specific cuts and internal tests you don’t spell out here and could be misinterpreted as directly quoted headline numbers from their paper.[3]  

**Fix (1–2 sentences)**: Either (a) explicitly qualify these as “in our reanalysis of the public SpArcFiRe DR9 catalog we find …” with a citation to your own artifact, or (b) replace them with the numbers Davis & Hayes actually highlight (e.g. ~644k galaxies with measurable arms and qualitative agreement with Galaxy Zoo) and drop the very specific 99.983% self-consistency figure from this section.
