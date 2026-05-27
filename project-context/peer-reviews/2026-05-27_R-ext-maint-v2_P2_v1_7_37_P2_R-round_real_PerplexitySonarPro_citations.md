# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v2_P2_v1_7_37
**Wall time**: 22.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33343, completion=1546, total=34889

---

## PAPER-PER-B1 – Mis-cited Cai et al. arXiv ID

**Issue (BLOCKER)**  
In multiple places the paper attributes the matter-bounce bispectrum and \(\fnl = -35/8\) to “Cai et al.\ 2009” with citation key `Cai:2009fn`, but the arXiv ID `0903.0631` corresponds to Brandenberger’s paper “Non-Gaussianity in a Matter Bounce,” not to a Cai–Brandenberger multi-author paper with Cai as first author.[1] The title and authorship implied by the text (“Cai et al.”) do not match the arXiv record, which lists only Robert Brandenberger on 0903.0631.[1]

**Fix**  
Audit the bib entry behind `\cite{Cai:2009fn}` and either (a) correct the arXiv ID, title, and author list to match the actual matter-bounce bispectrum paper being used, or (b) if 0903.0631 is indeed the intended source, change the in-text references from “Cai et al.” to the correct author(s) and update the year/title so that author string, title, and arXiv metadata are consistent with arXiv.org.[1]  

---

## PAPER-PER-M1 – Spurious arXiv cross-identification for “Cai:2009fn”

**Issue (MAJOR)**  
The notation `Cai:2009fn` strongly suggests a standard INSPIRE/arXiv-style key for a Cai-first-author cosmology paper in 2009, but the only cosmology paper at arXiv:0903.0631 is titled “Non-Gaussianity in a Matter Bounce” by R. Brandenberger alone, with no Cai listed.[1] There is no arXiv record in 2009 matching a “Cai et al.” matter-bounce bispectrum paper with that ID; this looks like fused metadata (author/year from one source, arXiv ID from another).[1]

**Fix**  
Resolve the source of the matter-bounce bispectrum formula: locate the correct Cai-involving reference in ADS/arXiv and rebuild the bib entry from the actual record (authors, title, journal, arXiv ID), then ensure all in-text “Cai et al. 2009” mentions and the key `Cai:2009fn` point to that real paper; if no such Cai-first-author paper exists, drop “Cai et al. 2009” and consistently cite the actual Brandenberger paper or other correct sources instead.[1]  

---

## PAPER-PER-M2 – Ambiguous “Cai & Brandenberger 2014” versus arXiv reality

**Issue (MAJOR)**  
The text repeatedly contrasts “Cai & Brandenberger 2014” (and “Li & Brandenberger”) with “Cai et al. 2009,” but only a Brandenberger-single-author matter-bounce non-Gaussianity paper exists at `0903.0631`, and there is no straightforward 2014 Cai–Brandenberger follow-up with the exact claimed normalization and factor-of-two story at that ID.[1] Given the already-mismatched 2009 citation, this looks like a second instance of fused or invented metadata (names and years attached to an arXiv record that does not actually match the described paper).[1]

**Fix**  
Do a fresh ADS/arXiv search for the specific 2014 follow-up you intend (title, authors, and normalization issue) and replace the current `CaiBrandenberger:2014`-style reference with the real paper’s correct authors, title, year, journal, and arXiv ID; if the “-35/16” normalization comparison actually comes from a different group or date, rewrite the discussion and labels to match that real source.  

---

## PAPER-PER-m1 – Missing explicit mapping from “Cai et al. 2009” to arXiv entry

**Issue (minor)**  
Throughout the manuscript, “Cai et al.\ 2009” is treated as a standard cosmology reference whose details are assumed known, but no explicit bibliographic line (authors, journal, arXiv:nnnn.nnnn) is shown in the provided LaTeX snippet, and the only related arXiv record actually visible (0903.0631) doesn’t match that authorship.[1] This makes it impossible for a reader to trace the bispectrum benchmark back to a uniquely identified paper.

**Fix**  
In the bibliography, add a complete, explicit entry for “Cai et al.\ 2009” with full author list, title, journal reference, and correct arXiv identifier; in the main text, include the year and possibly arXiv ID at the first mention so that readers can unambiguously locate the source.  

---

## PAPER-PER-m2 – Unsupported “Cai et al. Eq. (37) coefficients” claim

**Issue (minor)**  
The footnote in Sec. 2 claims that “the coefficients printed in Eq. (37) of ~\cite{Cai:2009fn}—(3, 1, -9, 5, -66, 9)—are the single-time-ordering values,” but the only public arXiv record associated in the text (0903.0631) does not expose any such polynomial-coefficient tuple in its abstract or metadata.[1] Without a correctly mapped underlying paper, this detailed coefficient attribution is effectively unverifiable.

**Fix**  
Once the correct bispectrum source paper is identified and cited with accurate metadata, verify that Eq. (37) in that paper actually contains the quoted coefficient set; if it does, add a short parenthetical “see Eq. (37) of [correct ref]” with full citation, and if it does not, correct the numbers or remove the claim.  

---

## PAPER-PER-n1 – Heinlein-style “Zhu & Cai 2026 echoes” citation with no verifiable record

**Issue (nit)**  
The text cites “Zhu & Cai 2026 echoes” as if it were a concrete reference, but no arXiv entry or journal record is given, and as of now there is no arXiv listing with that exact combination and year in the cosmology category that matches a dark-energy-from-bounce, “echoes”-titled paper.[1] As written, this reads like forward-dated or speculative metadata rather than a verifiable citation.

**Fix**  
Either (a) replace “Zhu & Cai 2026 echoes” with a currently existing, properly cited paper (full bib info, arXiv ID) that actually supports the claim about post-bounce inflation, or (b) relabel it as “forthcoming/ in preparation” without a year and remove it from the numbered reference list until a real publication exists.  

---

Do you want me to extend this audit to the Heinrich et al. SPHEREx reference and the claimed \(\sigma(f_{\rm NL}) \approx 0.7\) forecast as well?  


