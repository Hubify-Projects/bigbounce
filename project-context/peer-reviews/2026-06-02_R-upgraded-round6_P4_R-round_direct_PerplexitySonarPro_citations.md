# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round6
**Wall time**: 9.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100555, completion=993, total=101548, search_context_size=low, cost={'input_tokens_cost': 0.30167, 'output_tokens_cost': 0.0149, 'request_cost': 0.006, 'total_cost': 0.32256}

---

## PAPER-PER-B1 — **BLOCKER**
**Section:** Bibliography, `\bibitem{Shamir:2022DESI}` and in-text claims around Shamir 2022  
**Issue:** The paper’s metadata is internally inconsistent and likely fused from multiple sources. It cites *MNRAS 516, 2281 (2022)*, arXiv:2208.13866, DOI `10.1093/mnras/stac2372`, and says the paper analyzed “nearly 1.3M galaxies,” but earlier text also mixes “spiral galaxies” and “not all classified as spirals in every version.” The bibliography metadata claims have been repeatedly patched in comments, which is a red flag for citation-chain reliability.  
**Fix:** Verify the exact title, author list, journal page, DOI, and arXiv mapping against ADS/publisher/arXiv, then make the manuscript use one unambiguous description of the sample size and selection. Remove commentary that implies prior metadata was uncertain unless it is retained as an explicit audit note.

## PAPER-PER-B2 — **MAJOR**
**Section:** Bibliography, `\bibitem{Philcox:2023}` and nearby parity-violation references  
**Issue:** The citation metadata is likely mis-ordered or mismatched: the paper is cited as *Phys. Rev. D 106, 063501 (2022)* while the key “2023” label is used in-text. This looks like year/title/venue metadata is being conflated across the published journal version and arXiv record.  
**Fix:** Recheck the publisher record and align the bibkey, year, volume, and page with the actual published version. If the journal year is 2022 and arXiv/publication dates differ, note that explicitly and consistently in the citation string.

## PAPER-PER-B3 — **MAJOR**
**Section:** Bibliography, `\bibitem{Cahn:2021}` and in-text discussion of parity-odd 4-point function  
**Issue:** The citation is formatted as *Phys. Rev. Lett. 130, 201002 (2023)* but is keyed as a 2021 work and described as “2021” in text. This is a classic date/venue mismatch that can break citation-chain provenance.  
**Fix:** Verify whether the journal publication is 2023 and the arXiv preprint is 2021, then standardize the manuscript to either the preprint year or published year consistently. Keep one canonical metadata form throughout the text and bibliography.

## PAPER-PER-B4 — **MAJOR**
**Section:** Bibliography, `\bibitem{Motloch:2021}` and in-text use of Motloch et al.  
**Issue:** The bibliography gives *Nature Astronomy 5, 283 (2021), arXiv:2003.04800*, but the paper text repeatedly uses the result as if it were directly about “galaxy spins and initial conditions” in a way that may overstate what the paper explicitly measured. The citation is probably real, but the claim chain is too compressed and risks attributing stronger conclusions than the source supports.  
**Fix:** Audit the exact wording in the source paper and downgrade any over-strong paraphrases to what was actually demonstrated. Separate “observational correlation” from “physical interpretation” unless the source explicitly establishes the latter.

## PAPER-PER-B5 — **minor**
**Section:** Bibliography, `\bibitem{Eskilt2022}` / `\bibitem{Komatsu:2022}` / `\bibitem{Eskilt2023Cosmoglobe}`  
**Issue:** The manuscript mixes 2022/2023 cosmic birefringence references in a way that makes it hard to tell which result supports which claim. The venues and years are plausible, but the citation chain is messy and looks optimized for rhetorical support rather than provenance clarity.  
**Fix:** Add one sentence per citation stating exactly which measurement or framework each paper supports. If the 2022 and 2023 papers are distinct constraints, keep their roles separate and do not bundle them as interchangeable support.

## PAPER-PER-B6 — **nit**
**Section:** Bibliography, `\bibitem{DESI:2016}`  
**Issue:** The entry is explicitly labeled “white-paper-only, no journal publication,” which is fine, but it is not formatted like the rest and lacks the same bibliographic completeness. This is not wrong, but it is inconsistent with the rest of the citation chain audit style.  
**Fix:** Either format it as a standard arXiv/white-paper reference with a clear note that no journal publication exists, or move it to a methods/data footnote instead of the main bibliography.
