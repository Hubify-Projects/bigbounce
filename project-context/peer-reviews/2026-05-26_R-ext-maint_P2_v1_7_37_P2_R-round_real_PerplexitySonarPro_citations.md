# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint_P2_v1_7_37
**Wall time**: 23.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33351, completion=1759, total=35110

---

## PAPER-PER-B1 — Cai et al. arXiv ID and details

**Issue (MAJOR):**  
Throughout the paper, the main matter-bounce bispectrum reference is cited as `Cai et al. 2009` with key formulae (e.g., Eq. (37), Eqs. 34–36, the benchmark values) attributed to `\cite{Cai:2009fn}` and treated as the “Non-Gaussianity in a Matter Bounce” paper that derives \(\fnl=-35/8\). In reality, arXiv:0903.0631 is titled “Non-Gaussianity in a Matter Bounce” and lists authors as Yi-Fu Cai, Wenjuan Xue, Robert Brandenberger, and Xinmin Zhang, not “Cai et al.” in the sense of a distinct 2009 paper `Cai:2009fn` with the exact polynomial/benchmark apparatus as described here.[0] The current bibliography key `Cai:2009fn` must be explicitly tied to arXiv:0903.0631 with correct full author list, and the text should be checked so that references to specific equation numbers, coefficients, and benchmark tables actually exist in that paper’s LaTeX (or else clearly flagged as re-derived/renotated here rather than “their Eq. (37)”).

**Fix:**  
Map `\cite{Cai:2009fn}` unambiguously to arXiv:0903.0631 with its correct title and authors, verify that all quoted equation numbers and coefficients actually appear there, and either (i) adjust equation/benchmark references to match the real numbering, or (ii) rephrase to say “following the structure of Cai et al. (arXiv:0903.0631) we define…” instead of attributing non-existent equation numbers to that paper.[0]

---

## PAPER-PER-B2 — Misleading “Li & Brandenberger” labeling

**Issue (MAJOR):**  
The text repeatedly refers to a “Li & Brandenberger” or “Li & Brandenberger (c=1)” normalization and also to “Li & Brandenberger value \(-35/16\)” but, in the bibliography excerpted in the LaTeX shown, there is no explicit Li & Brandenberger reference key or arXiv ID, and no verification is presented that any paper by Li & Brandenberger actually quotes \(\fnl=-35/16\) in the precise normalization you describe. This makes it likely that “Li & Brandenberger” here is a conflation of multiple works (e.g., Cai & Brandenberger plus a separate Li paper) rather than a single, correctly-cited article.

**Fix:**  
Add a concrete reference with correct authors, title, arXiv ID, and journal (if any) for the work that actually uses \(\fnl=-35/16\). If no such single “Li & Brandenberger” paper exists, rename this convention everywhere to the correct pair of papers (e.g., “Cai & Brandenberger 2014” and Li’s work) and explicitly separate “c=1 convention” from any specific author pair to avoid conflating metadata.

---

## PAPER-PER-M1 — Incomplete metadata for Heinrich et al. 2023 / 2024

**Issue (MAJOR):**  
The SPHEREx bispectrum forecast is attributed to “Heinrich et al. 2024” with citation key `\cite{Heinrich:2023}`, and described as “multi-tracer galaxy bispectrum forecast” with \(\sigma(f_{\rm NL}^{\rm local})\approx 0.7\) from Fig. 6 / Table 3. No arXiv identifier or journal reference is given in the excerpt, and `Heinrich:2023` is ambiguous (there are multiple cosmology papers by Heinrich et al. in 2023–2024, none trivially identifiable only from the description without a search).[1] This makes it hard to confirm that the stated σ values and figure/table mapping are accurate.

**Fix:**  
Add the precise reference details: full author list first author “Heinrich”, full title, arXiv ID, and journal/DOI, and double-check that Fig. 6 and Table 3 in that exact paper report \(\sigma(f_{\rm NL}^{\rm local})\approx 0.7\) for the SPHEREx multi-tracer bispectrum under the normalization \(B^{\rm local}=(6f_{\rm NL}/5)[P(k_1)P(k_2)+2\mathrm{ perms}]\). Adjust figure/table numbers in the text if they differ in the canonical version.

---

## PAPER-PER-M2 — Wands 2010 citation is ambiguous

**Issue (minor):**  
The Introduction says “\(\fnl = -35/8\) … \cite{Cai:2009fn,Wands:2010}” and later refers to Wands 2010 in a way that suggests a paper focused specifically on matter-bounce \(\fnl\). Jonathan Wands has multiple 2010 works on cosmological perturbations and bouncing/alternatives to inflation, but none obviously titled or indexed simply as “Wands:2010” without more metadata; arXiv and ADS indices show several Wands papers around that time whose titles do not match the implied “matter bounce local \(\fnl\)” focus.[0] Without a precise ID, a reader cannot verify that Wands 2010 supports the exact claims made.

**Fix:**  
Replace `\cite{Wands:2010}` with a concrete bibliographic entry: title, journal, year, and arXiv number of the specific Wands paper you mean (e.g., “Cosmological perturbations through a simple bounce” vs “Scale-invariant perturbations in …”). Ensure that the text only claims what that particular paper actually states about matter-dominated contraction and non-Gaussianity.

---

## PAPER-PER-m1 — Check “Non-Gaussianity in a Matter Bounce” author list

**Issue (minor):**  
The body text refers generically to “Cai et al.” and “Cai & Brandenberger” and uses the key `Cai:2009fn`. The arXiv record for “Non-Gaussianity in a Matter Bounce” (arXiv:0903.0631) lists four authors (Yi-Fu Cai, Wenjuan Xue, Robert Brandenberger, Xinmin Zhang).[0] If your BibTeX for `Cai:2009fn` only includes Cai and Brandenberger, or mis-orders authors, that would be fused and incorrect metadata.

**Fix:**  
Ensure the BibTeX entry for `Cai:2009fn` exactly matches arXiv:0903.0631 (full four-author list, correct title and year). If you want to distinguish “Cai & Brandenberger 2014” or later works, assign them separate keys (`CaiBrandenberger:2014`, etc.) rather than overloading `Cai:2009fn`.

---

## PAPER-PER-n1 — Use of “Zhu & Cai 2026” without concrete citation

**Issue (nit):**  
Several sections mention “Zhu & Cai 2026” or “Zhu & Cai 2026 echoes” as a counterexample bounce model with prolonged post-bounce inflation. No arXiv ID or journal citation is provided, and a search up to now does not surface a 2026 cosmology paper by Zhu & Cai specifically on bounce “echoes” with that phrasing.[1] This looks like a forward-dated or placeholder reference.

**Fix:**  
Either (i) replace “Zhu & Cai 2026” with a concrete, currently-existing paper (with correct arXiv ID and title) that actually presents the relevant counterexample, or (ii) mark it explicitly as “forthcoming work by Zhu & Cai (in preparation)” without assigning a year or implying publication, until such a paper exists and can be cited properly.
