# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round6
**Wall time**: 8.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35881, completion=968, total=36849, search_context_size=low, cost={'input_tokens_cost': 0.10764, 'output_tokens_cost': 0.01452, 'request_cost': 0.006, 'total_cost': 0.12816}

---

## PAPER-PER-B1 — **minor**

**Line:** `\bibitem{Tempel2014}` / `\section{Tempel+2014 FoF cross-validation}`

**Issue:** The paper cites Tempel et al. 2014 as a “FoF group catalog” and uses it as a galaxy-environment classifier, but the bibitem title is the group catalogue paper, not a dedicated environment-classification paper. The text’s mapping from richness bins to V-Web classes is an in-paper construct, not something Tempel 2014 itself provides.

**Fix:** Rephrase to say you *derive* the 4-class mapping from the Tempel catalog for this analysis. Do not imply Tempel 2014 natively defines the same environment taxonomy.

## PAPER-PER-B2 — **minor**

**Line:** `\bibitem{DESIVAST2025}` and `\section{Concurrent-literature DR1/EDR cosmic-web cross-validation}`

**Issue:** The paper previously notes the DESIVAST title was corrected, but the current bibitem still appends `\textit{et al.}` after only four named authors while the paper text elsewhere treats the collaboration as a peer-reviewed public DESI void catalog. That is sloppy metadata, not a citation-chain failure.

**Fix:** Keep the shortened author list if desired, but ensure the author truncation style matches the journal format consistently across all bibitems and in-text mentions.

## PAPER-PER-M3 — **major**

**Line:** `\section{Concurrent-literature DR1/EDR cosmic-web cross-validation}` / `\bibitem{TWebDESI2026}`

**Issue:** `TWebDESI2026` is cited as “submitted to MNRAS (2026)” with arXiv:2604.02463, but the paper text repeatedly treats it as a contemporaneous independent validation of the V-Web result and quotes survey-level volume-fraction ranges from it. That is fine only if the arXiv preprint actually contains those exact results; the current manuscript does not show a direct citation-to-claim trace for the quoted fraction ranges.

**Fix:** Add a sentence limiting the claim to what is explicitly in the arXiv abstract or main text, or cite the exact section/table/figure from the preprint that supports the quoted ranges.

## PAPER-PER-B4 — **major**

**Line:** `\section{ASTRA EDR per-object cross-validation}` / `\bibitem{ASTRADESI2026}`

**Issue:** The manuscript assigns a strong validation role to ASTRA while calling it “published only on EDR,” but the bibitem is just an arXiv preprint with no venue. The paper’s language overstates publication status relative to the citation metadata.

**Fix:** Replace “published”/“published only on EDR” with “arXiv preprint / preprint on the EDR overlap” unless there is an actual journal venue. Keep the validation claim scoped to the preprint’s reported results.

## PAPER-PER-B5 — **major**

**Line:** `\section{Concurrent-literature DR1/EDR cosmic-web cross-validation}` / `\paragraph{DESIVAST per-galaxy cross-match (this work)}`

**Issue:** The paper treats DESIVAST as a direct public void catalog and then builds a large part of the argument on `0/6` overlap, `56,981` void galaxies, and `86,276` catalog-native void galaxies. Those numbers may be internally consistent, but the manuscript does not provide a citation-chain check that DESIVAST’s published products actually expose the exact fields and object-level join logic being used.

**Fix:** Add an explicit methods citation to the DESIVAST release documentation or catalog schema showing the relevant FITS HDUs/fields. Otherwise the per-galaxy join claims read as script-dependent inference rather than paper-supported fact.

## PAPER-PER-B6 — **blocker**

**Line:** `\bibitem{golden_chirality_2026}` / `\bibitem{golden_fnl_2026}`

**Issue:** Both citations are internal, unpublished companion works with no arXiv IDs or venue. The manuscript leans on them for core quantitative baselines (`f_CW = 0.4974`, monopole offset, dipole null, fNL forecast) without any external bibliographic anchor, so a citation-chain audit cannot verify the claims from the bibliography alone.

**Fix:** Either publish these companion works or clearly label the numbers as *internal unpublished inputs* with no external verification. For a journal paper, the core quantitative baseline should not depend on uncitable internal manuscripts.
