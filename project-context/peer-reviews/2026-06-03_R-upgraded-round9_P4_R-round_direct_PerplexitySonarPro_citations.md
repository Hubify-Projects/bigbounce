# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 9.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100509, completion=671, total=101180, search_context_size=low, cost={'input_tokens_cost': 0.30153, 'output_tokens_cost': 0.01007, 'request_cost': 0.006, 'total_cost': 0.31759}

---

## PAPER-PER-B1

**BLOCKER** — `\bibitem{Jia:2023}` has the wrong title metadata for the cited ApJ paper. The real paper is *Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network* and the ApJ venue/page/DOI line is fine, but the title in the manuscript (“Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network”) is not enough to detect the bib issue from text alone; the bigger problem is that the body repeatedly attributes “CE-ResNet” to Jia et al. while the bibliographic record and discussion conflate it with a separate “Galaxy Spin Classification I” line. Fix by making the citation metadata exactly match the published title/author/DOI record and then using that exact form consistently everywhere.

## PAPER-PER-M2

**MAJOR** — `\bibitem{Philcox:2023}` is year-mismatched: the cited paper is *Phys. Rev. D 106, 063501 (2022), arXiv:2206.04227*, not 2023. Fix the year in the bibliography and audit every in-text mention that mirrors the wrong year so the citation chain is internally consistent.

## PAPER-PER-M3

**MAJOR** — `\bibitem{Cahn:2021}` is year-mismatched: the citation says *Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004*, but the key is labeled 2021. Fix the bib key or year label to the published year and ensure the body does not refer to it as 2021 if the published record is 2023.

## PAPER-PER-M4

**MAJOR** — `\bibitem{Houston...}` style issue: the manuscript cites `\cite{Iye:2021}` for claims about reading-direction bias and duplicate photometric objects, but those specific claims are not actually in the cited paper as stated here; they are a composite of multiple later discussions. Fix by narrowing the claim to what the cited paper demonstrably says, or split the support across the correct sources instead of overloading one citation.

## PAPER-PER-M5

**minor** — `\bibitem{Walmsley:2023}` is overclaimed in the prose. The manuscript uses it to justify exact DESI Legacy parent-sample selection details and “8.7M galaxies” phrasing, but the cited paper is a morphology catalog paper, not a source for all the selection-function specifics asserted here. Fix by moving the selection-function details to the DESI Legacy survey paper or the dataset documentation and keep Walmsley et al. for the morphology catalog claims only.

## PAPER-PER-M6

**minor** — `\bibitem{Davis:2014}` is correctly identified as SpArcFiRe, but the prose attributes the “Hayes-Davis DR9 update” and overlap-count specifics to this citation without a direct source chain. Fix by citing the actual update/release source separately, or remove the exact overlap-count claims if no verifiable primary source is available.
