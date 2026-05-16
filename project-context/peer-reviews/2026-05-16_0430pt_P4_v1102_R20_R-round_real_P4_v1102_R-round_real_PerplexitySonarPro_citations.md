# P4_v1102 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0430pt_P4_v1102_R20_R-round_real
**Wall time**: 8.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=84597, completion=859, total=85456

---

## PAPER-FAIR-B1
**BLOCKER**  
**Section:** Bibliography and citations  
**Issue:** The citation for Philcox is fused/mislabeled. The paper cites `Philcox:2023` as “Phys. Rev. D 106, 063501 (2022), arXiv:2206.04227,” but the arXiv record and journal metadata correspond to the same 2022/2023 paper, and the title is not the generic phrase used in some LLM reconstructions; the metadata is okay, but the bibkey/year labeling is internally inconsistent with the cited article’s publication timing.   
**Fix:** Standardize the bibentry to the journal year or arXiv year consistently, and ensure the in-text citation label matches the actual publication record.

## PAPER-FAIR-B2
**MAJOR**  
**Section:** `\bibitem{Jia:2023}`  
**Issue:** The Jia paper metadata is correct on arXiv: title, authors, arXiv ID, and related DOI all match the record. The manuscript’s repeated use of “CE-ResNet” is fine, but the intro/table claims about “1.95 million galaxies” and “accepted by ApJ” should be tied to the cited paper explicitly rather than treated as standing facts without context.   
**Fix:** Keep the citation, but make sure every numerical claim about sample size and performance is clearly attributed to the arXiv record or the journal version in the sentence that uses it.

## PAPER-FAIR-B3
**MAJOR**  
**Section:** `\bibitem{Shamir:2022DESI}`  
**Issue:** The Shamir DESI citation is real and the arXiv ID/title pair match the arXiv record. The manuscript’s text, however, mixes “nearly 1.3M galaxies” with “~200,000 spirals” as if both are direct outputs of the same paper; the arXiv abstract only supports the former, while the latter is a manuscript-internal reinterpretation.   
**Fix:** Separate what the cited paper actually reports from your own filtered subset. Do not present the spiral count as a direct claim of the citation unless the source explicitly says so.

## PAPER-FAIR-B4
**MAJOR**  
**Section:** `\bibitem{Iye:2026P6}`  
**Issue:** The manuscript cites arXiv:2605.05570 as a current paper and treats it as public. I cannot verify that record from the provided sources, so this is unsupported metadata in the current draft.   
**Fix:** Verify the arXiv ID/title/authors against arXiv or ADS before keeping it in the bibliography. If it is a placeholder or future paper, mark it clearly as such or remove it.

## PAPER-FAIR-B5
**minor**  
**Section:** `\bibitem{Cahn:2021}`, `\bibitem{Hou:2023}`, `\bibitem{Cabass:2023}`  
**Issue:** The arXiv IDs and titles are real and match the records, but the prose overstates the mapping from the 4PCF literature to the manuscript’s dipole observable. The cited papers are about parity-odd 4PCFs, not about the galaxy chirality dipole itself.   
**Fix:** Keep the citations, but restrict the claim to “conceptually related parity-violation literature” rather than implying these papers directly validate the chirality dipole interpretation.

## PAPER-FAIR-B6
**nit**  
**Section:** `\bibitem{Shamir:2022}`  
**Issue:** The title and venue are real, but the bib note says this is a “methodology / Ganalyzer-pipeline reference paper” while the actual cited title is a broad analysis paper. That is a descriptive mismatch, not a metadata error.   
**Fix:** If you want a pipeline-method citation, cite a methods-focused source directly. Otherwise, remove the pipeline-label description from the bib note.
