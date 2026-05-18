# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1640pt_P4_v1_0_115_R20
**Wall time**: 30.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=88456, completion=1563, total=90019

---

## PAPER-PER-B1 – Mis-cited Iye & Yagi 2026 paper

**Grade:** MAJOR  

**Location:** Sec. \ref{sec:comparison}, para. mentioning “Iye & Yagi (2026)”  

**Issue:** The text says *“Iye & Yagi (2026) is anticipated … but the paper is now public as arXiv:2605.05570 (May 2026)”* and then claims to cite it “here as an independent corroborating HSC‑WIDE null result”. The arXiv ID, title, and detailed results of that paper are not actually checked or specified; this is effectively an unverified forward‑looking citation dressed as a concrete reference.  

**Fix:** Replace the anticipatory phrasing with a concrete, fully checked citation once you have verified the arXiv entry (title, authors, null/positive result) and state explicitly what that paper finds; or, if it is not yet verified, remove it from the “independent corroboration” list and flag it only as “forthcoming work” without implying a specific null result.  

---

## PAPER-PER-M1 – Shamir 2022 DESI paper: title / DOI consistency

**Grade:** MAJOR  

**Location:** Sec. \ref{sec:shamir}, refs. \cite{Shamir:2022} and \cite{Shamir:2022DESI}  

**Issue:** The DESI Legacy spirals paper is correctly linked to arXiv:2208.13866 and DOI 10.1093/mnras/stac2372, and the journal venue (MNRAS 516, 2281) matches the ADS record.[1] However, your text refers to *“Shamir (2022) DESI Legacy Imaging Surveys footprint”* and later to “Shamir 2022 DESI Legacy spirals” with slightly different descriptive phrases and one place calls it just “Shamir (2022)” (which elsewhere in the bib is a different methodological paper). This is easy to confuse with the earlier generic methodology paper in the same year.  

**Fix:** Use a unique, consistent label in text for the DESI-paper only (e.g. “Shamir 2022 DESI Legacy (MNRAS 516, 2281; arXiv:2208.13866)”) wherever you discuss DESI‑footprint amplitudes; reserve \cite{Shamir:2022} for the more general method paper if needed. This avoids metadata fusion between two 2022 Shamir papers.  

---

## PAPER-PER-M2 – CE‑ResNet citation and numbers okay but one fused phrase

**Grade:** minor  

**Location:** Sec. \ref{sec:intro} and \ref{sec:ceresnet}, citing Jia et al. 2023  

**Issue:** The citation to CE‑ResNet (arXiv:2210.04168, ApJ 943, 32, DOI 10.3847/1538‑4357/aca8aa) is fully correct, and the summary “chirality‑equivariant ResNet … guarantees exact swap under horizontal reflection” matches the abstract.[0] However, you say “their catalog of 1.95 million galaxies from DESI Legacy pre‑imaging” while Jia et al. state only that DESI images are *used for classification and increase counts*; the exact catalog size and the “pre‑imaging” phrase are not stated in that form in the paper and risk looking like a fused paraphrase.  

**Fix:** Either explicitly cite where the 1.95 M figure comes from (table/section in Jia et al.) or soften to “of order 2 million DESI galaxies (Jia et al. 2023)” and drop “pre‑imaging” unless you can point to the exact wording in the DESI Legacy documentation demonstrating that specific term.  

---

## PAPER-PER-m3 – Shamir 2020 description is mostly correct, but one over‑statement

**Grade:** minor  

**Location:** Sec. \ref{sec:intro}, para starting “Shamir (2020) extended this to …”  

**Issue:** Shamir 2020 (arXiv:2007.16116, Ap&SS, DOI 10.1007/s10509‑020‑03850‑1) indeed analyzes SDSS and Pan‑STARRS, finds asymmetries of order a few percent, and describes dipole/quadrupole alignments.[1] You say “reporting asymmetries of ~3% with a consistent dipole axis”; the paper actually emphasizes both dipole and quadrupole patterns and quotes significances >5σ and >8σ for quadrupole fits, not a single “consistent axis” phrased as a pure dipole.  

**Fix:** Rephrase to: “Shamir (2020) extended this to SDSS and Pan‑STARRS, reporting few‑percent asymmetries and statistically significant dipole and especially quadrupole alignments,” which more faithfully matches his abstract.  

---

## PAPER-PER-m4 – CE‑ResNet “factor of 4 fewer galaxies” phrasing

**Grade:** minor  

**Location:** Sec. \ref{sec:intro}, the sentence “CE‑ResNet represents … but its catalog covers a factor of 4 fewer galaxies than the full DESI Legacy footprint.”  

**Issue:** Jia et al. explicitly mention the increase in spiral counts when using DESI images but do not directly phrase their catalog as “factor 4 fewer than full DESI Legacy footprint”; that quantitative comparison is your own, and “factor 4 fewer” sounds like a documented claim, though no explicit DESI‑wide baseline is cited.[0]  

**Fix:** Mark this clearly as your derived comparison, e.g. “based on the public DESI Legacy imaging area, their 1.95 M spiral catalog corresponds to roughly a quarter of our footprint,” and cite both Jia et al. and the DESI DR8 overview paper for the footprint.[0][2]  

---

## PAPER-PER-n1 – LSST reference: remove implicit arXiv mapping

**Grade:** nit  

**Location:** Bib item for LSST / Ivezic et al. (2019)  

**Issue:** The ApJ reference (ApJ 873, 111, DOI 10.3847/1538‑4357/ab042c) is correct, but you discuss older arXiv:0805.2366 “LSST Science Book” as if it were a preprint version of that specific ApJ paper; in reality 0805.2366 is a different, earlier LSST white paper and not the preprint of ApJ 873, 111.[3]  

**Fix:** Keep the ApJ reference alone for the design paper and stop implying a one‑to‑one arXiv→journal mapping; mention 0805.2366 separately as “LSST Science Book (white paper)” if needed, to avoid fused metadata between two distinct LSST documents.  


