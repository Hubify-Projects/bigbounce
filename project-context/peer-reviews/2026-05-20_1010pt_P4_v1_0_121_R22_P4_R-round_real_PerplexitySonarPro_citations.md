# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-20_1010pt_P4_v1_0_121_R22
**Wall time**: 14.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=93920, completion=1066, total=94986

---

## PAPER-BLOCKER-1

**Section:** Introduction; bibliographic references to Shamir works.

**Issue:** The manuscript repeatedly conflates Shamir’s 2020 and 2022 DESI/SDSS claims and then uses those claims as a single comparator set. The actual arXiv records are distinct: arXiv:2007.16116 is the 2020 SDSS/Pan-STARRS parity-violation paper, while arXiv:2208.13866 is the 2022 DESI Legacy Survey paper with a different title and scope [1][2].

**Fix:** Split the comparator discussion by paper and stop compressing them into one “2–4%” bucket unless you explicitly label it as your own derived shorthand. Any amplitude comparison should cite the exact paper and sample size separately.

## PAPER-MAJOR-2

**Section:** References / `Shamir:2022DESI`, `Shamir:2020`, `Iye:2020`.

**Issue:** `Iye:2020` is mis-cited by year/title relative to the arXiv record. The cited paper is arXiv:2011.00662, titled *Spin Parity of Spiral Galaxies III -- Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations*, submitted in 2020 but published as an ApJ paper in 2021 [3].

**Fix:** Rename the citation key or bibliographic year to avoid implying a 2020 journal publication. Keep the arXiv ID and journal metadata aligned with the actual record.

## PAPER-MAJOR-3

**Section:** Bibliography, `Jia:2023`.

**Issue:** The bib entry is structurally close but still metadata-fragile: the actual arXiv title and author list are correct, but the paper is arXiv:2210.04168 with the exact title “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” and the record explicitly lists He Jia, Hong-Ming Zhu, and Ue-Li Pen [1]. If you cite this paper as the basis for “CE-ResNet,” that is fine, but the manuscript’s prose sometimes treats later catalog behavior as if it were in the arXiv record itself.

**Fix:** Keep the bib as-is but ensure every claim about the catalog or DESI outcome is attributed to your own pipeline, not to the 2022 arXiv paper. Do not imply the arXiv paper contains your 2026 catalog statistics.

## PAPER-MAJOR-4

**Section:** References / `Shamir:2022DESI` and introduction.

**Issue:** The manuscript states the Shamir DESI Legacy paper is “MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372,” which matches the arXiv record metadata [2]. However, the prose elsewhere describes it as if it analyzed “nearly 1.3 million spirals,” while the arXiv abstract says “nearly 1.3·10^6 galaxies” and does not specify all were spirals [2].

**Fix:** Use the paper’s own wording: “nearly 1.3 million galaxies” unless you have a direct source for the spiral-only subset. If you mean a spiral subset, cite the exact section or table that supports that narrower number.

## PAPER-minor-5

**Section:** Introduction and comparison sections.

**Issue:** The manuscript fuses title/scope metadata from different papers when discussing parity-violation literature, especially around “dipole,” “quadrupole,” and “spin parity” claims. Example: Shamir 2020 is a parity-violation/multipole paper, while Iye et al. 2020/2021 is a dipole-analysis paper with a cleaned-catalog null result; they are not interchangeable [3][4].

**Fix:** Separate the literature by observable and methodology. Use one sentence per paper and avoid mixed summaries that blend paper titles, observables, and conclusions.

## PAPER-nit-6

**Section:** Bibliography, `DESI:2016` and `Ivezic:2019`.

**Issue:** The manuscript’s bibliographic style is mostly consistent, but the `DESI:2016` entry is only a white paper/arXiv record, while `Ivezic:2019` is a journal article and not the older LSST science-book preprint you discuss in the note. That note is trying to prevent exactly the kind of fused-metadata confusion you’re auditing.

**Fix:** Keep the note, but make the main text avoid any shorthand that could read as “the 2008 arXiv preprint is the same thing as the 2019 ApJ article.” If you mention the preprint at all, identify it separately from the journal reference.
