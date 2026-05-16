# P4_v1092 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0000pt_P4_v1092_R11_R-round_real
**Wall time**: 10.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=81694, completion=732, total=82426

---

## PAPER-FOR-B1

The bibliography mixes real entries with metadata that is not cleanly supported by the cited records. In particular, the LSST cite is fused: the paper’s journal entry is real, but the arXiv ID `0805.2366` is not the preprint of the 2019 ApJ article; the text should cite the correct journal record or a separately verified preprint. 

Fix: split the journal citation from the arXiv citation, and verify the exact preprint/journal pairing before keeping both in one entry. If you cannot verify the preprint identity, remove the arXiv ID and cite only the journal article. 

## PAPER-FOR-B2

The `Iye et al. 2021` cite is malformed in the manuscript body: it is written as `Iye et al. (2021) \cite{Iye:2020}`, but the bib entry itself is for the 2021 ApJ paper `Spin parity of spiral galaxies. III...` with arXiv:2011.00662. That is okay as a citation key, but the prose should not imply a 2020 paper when the bibliographic record is 2021. 

Fix: standardize all in-text mentions to `Iye et al. (2021)` and keep the key as `Iye:2020` only if you retain the current key naming convention. 

## PAPER-FOR-B3

The `Walmsley et al.` citation is correct in substance, but the manuscript overstates the result as a “detailed morphology measurements for 8.7M galaxies” source for chirality-related claims. The arXiv abstract verifies detailed morphology for 8.67 million galaxies, not handedness labels or chirality ground truth. 

Fix: constrain every use of this cite to morphology-measurement context only, and avoid implying it provides CW/CCW labels or independent chirality validation. 

## PAPER-FOR-B4

The `Shamir:2022DESI` metadata is internally consistent in the bib entry, but the paper text repeatedly uses it to support sample-size and spiral-count comparisons that are not directly stated in the arXiv abstract. The verified abstract says “nearly 1.3 million galaxies” and a dipole probability `P<10^-5`, but does not support the manuscript’s stronger claims about exact spiral counts or like-for-like spiral subsamples. 

Fix: downgrade those comparisons to “catalog-scale context” unless you can verify the exact spiral count from the paper PDF or ADS. 

## PAPER-FOR-B5

The `Jia et al. 2023` citation is real and correctly identified by title, authors, arXiv ID, and DOI. The manuscript’s claim that CE-ResNet is “architecturally equivariant” is also supported by the arXiv abstract. 

Fix: none needed for citation forensics; this one holds. 

## PAPER-FOR-B6

The `DESI:2016` entry is only partially resolved in the bibliography. The arXiv ID `1611.00036` is real, but the bib item is incomplete because it gives no journal venue, volume, or DOI, despite the manuscript elsewhere treating it like a standard published reference. 

Fix: either make it a pure arXiv citation consistently, or add the final journal metadata from the published DESI overview paper before submission. 
