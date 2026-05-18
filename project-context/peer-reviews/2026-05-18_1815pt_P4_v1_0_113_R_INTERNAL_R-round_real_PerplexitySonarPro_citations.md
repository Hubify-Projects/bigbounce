# P4_v1_0_113_R_INTERNAL R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1815pt
**Wall time**: 9.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=91832, completion=732, total=92564

---

## PAPER-PER-B1 — BLOCKER

Section: bibliography + Introduction.

The citation `Iye:2020` is fused metadata: the paper cites `Spin parity of spiral galaxies. III...` with `Astrophys. J. 907, 123 (2021), arXiv:2011.00662`, but the arXiv record’s title/authors match a 2021 ApJ paper and not a 2020 publication label; the in-text “Iye et al. (2021)” is fine, but the bib key/year pairing is inconsistent with the citation string. Fix by making the bib entry internally consistent with the actual journal year and authorship as listed on arXiv, and keep the in-text year aligned. [1]

## PAPER-PER-B2 — MAJOR

Section: bibliography entry `Shamir:2022DESI`.

The title/arXiv/DOI triad is real and consistent, but the prose later calls this “nearly 1.3M galaxies” and elsewhere “~200,000 spiral galaxies,” which are not the same sample and are conflated in the comparison framing. Fix by separating “catalog size” from “spiral subsample size” wherever Shamir 2022 DESI is used, so the paper does not compare a spiral-only count to a total-galaxy count. [1]

## PAPER-PER-B3 — MAJOR

Section: bibliography entry `Walmsley:2023`.

The cited paper is real, but the manuscript repeatedly treats it as a chirality/handedness source and also uses it as if it directly supplies CW/CCW ground truth; the arXiv abstract only describes detailed morphology measurements, not handedness labels. Fix by limiting Walmsley et al. to morphology/depth context and removing any implication that it provides chirality ground truth. [2]

## PAPER-PER-B4 — MAJOR

Section: bibliography entry `Jia:2023`.

The arXiv record confirms the title, authors, and arXiv ID `2210.04168`; the manuscript’s surrounding claims are broadly consistent with the source. But the paper later mixes this with a DESI Legacy “1.95M galaxies” catalog and with “accepted by ApJ” language, which can be read as if the arXiv preprint itself is the final journal record; keep the citation strictly as the arXiv paper unless you verify the final ApJ metadata separately. [1]

## PAPER-PER-B5 — minor

Section: bibliography entry `Ivezić:2019`.

The paper explicitly says the older arXiv ID `0805.2366` was removed to prevent fused-metadata confusion, which is good, but the prose still gestures at a “preprint arXiv:0805.2366” in provenance notes elsewhere in the file. Fix by deleting any residual references to the old arXiv ID outside the canonical bib entry. [3]

## PAPER-PER-B6 — minor

Section: bibliography entry `SpArcFiRe` / `Davis:2014`.

The arXiv ID and journal venue are real, but the manuscript’s later “DR9-overlap catalog” and “public Hayes-Davis DR9 update” wording is uncited and not tied to the bib record. Fix by either adding a real citation for that update or downgrading the language to an uncited internal claim. [4]
