# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 7.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100594, completion=774, total=101368, search_context_size=low, cost={'input_tokens_cost': 0.30178, 'output_tokens_cost': 0.01161, 'request_cost': 0.006, 'total_cost': 0.31939}

---

## PAPER-PER-B1

**Section:** References / `Ivezić et al. (2019)`  
**Issue:** The bibitem says the arXiv ID was “removed” to avoid fusion, but the record still mixes provenance narratives: it cites the ApJ paper and then keeps a long note about the older LSST Science Book preprint. That note is not a clean citation record and risks metadata confusion.  
**Fix:** Keep only the ApJ 873, 111 citation with DOI. Move the historical preprint discussion to a prose note outside the bibliography, or delete it entirely.

## PAPER-PER-B2

**Section:** References / `Cahn:2021`  
**Issue:** The bibitem title/year are fused. The paper is the 2021 arXiv preprint, but the journal article is *Phys. Rev. Lett.* 130, 201002 (2023). The entry currently presents the 2023 journal venue with the 2021 arXiv ID without clarifying this is the published version of a 2021 preprint.  
**Fix:** State the published journal citation cleanly and optionally add “arXiv:2110.12004 (2021)” as the preprint. Do not imply the 2023 PRL venue is a 2021 publication.

## PAPER-PER-B3

**Section:** References / `Philcox:2023`  
**Issue:** Same fusion problem: the title is paired with *Phys. Rev. D* 106, 063501 (2022) while the bibkey and surrounding text treat it as a 2023 paper. That is inconsistent metadata presentation.  
**Fix:** Use the journal year from the publication, and if you want a 2023 citation label, rename the bibkey to avoid implying a 2023 journal article.

## PAPER-PER-B4

**Section:** References / `Hou:2023`  
**Issue:** The journal year is 2023, but the cited arXiv ID is 2206.03625 and the paper’s PRD venue is 2023; that part is fine. The real issue is title fidelity: the manuscript elsewhere describes this as “measurement of parity-odd modes in the large-scale 4-point correlation function,” but the bibitem title is more specific and not consistently matched in the prose.  
**Fix:** Align the in-text description with the exact published title, or shorten both to the same canonical wording.

## PAPER-PER-B5

**Section:** References / `Motloch:2021`  
**Issue:** The citation is vulnerable to title/year confusion. The paper is a Nature Astronomy article from 2021, but the manuscript repeatedly treats it as a 2020 result and uses it as if the arXiv date were the publication date.  
**Fix:** Keep the 2021 journal citation as authoritative and refer to the arXiv date only as the preprint date, not as the paper year.

## PAPER-PER-B6

**Section:** Introduction and Results, Shamir comparator citations (`Shamir:2020`, `Shamir:2022DESI`)  
**Issue:** The manuscript repeatedly compresses multiple Shamir papers into merged amplitude claims and mixed sample sizes, then cites them as if each paper supported the same “~3%” or “~1.3M spiral” statement. That is citation-chain fusion, not a faithful per-paper attribution.  
**Fix:** Split each claim by paper and sample. For every numerical comparator, attach only the exact paper that reported it, and do not merge amplitudes across studies unless the text explicitly says it is a derived range across papers.
