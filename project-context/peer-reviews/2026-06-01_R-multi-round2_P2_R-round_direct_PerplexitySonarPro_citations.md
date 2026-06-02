# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round2
**Wall time**: 23.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34697, completion=2014, total=36711, search_context_size=low, cost={'input_tokens_cost': 0.10409, 'output_tokens_cost': 0.03021, 'request_cost': 0.006, 'total_cost': 0.1403}

---

## PAPER-PER-B1 – Mis-cited Cai & Brandenberger 2014 paper

**Severity:** MAJOR  

**Location:** Sec. \ref{sec:assumptions}, long paragraph starting “A factor-of-two discrepancy exists…” (around middle of that section).  

**Issue:** The text attributes the competing value \(\fnl=-35/16\) to “Cai & Brandenberger \cite{CaiBrandenberger:2014}” and describes it as being obtained “when evaluated at \(c_s=1\)”. The standard Cai & Brandenberger 2012/2014 paper on matter bounce non‑Gaussianity (arXiv:1207.3204 / 1404.3295) does not present a local-\(f_{\rm NL}\) value of \(-35/16\) normalized in the Planck/Komatsu-Spergel convention; the \(-35/16\) value and the detailed “single‑time‑ordering vs doubled commutator” narrative appear specific to this manuscript’s internal comparison and are not found in the actual Cai–Brandenberger articles.[ ]  

**Fix:** Re-check the specific Cai & Brandenberger paper and equation being referenced; if no published \(-35/16\) value exists, either (i) remove the claim that this number is “obtained” in that paper and instead describe it as an *effective value under an alternative normalization reconstructed by the author*, or (ii) adjust the citation to a source that demonstrably contains \(-35/16\) with the stated normalization. Make clear which expressions come directly from the literature versus from the author’s re-normalization of those results.

---

## PAPER-PER-B2 – Misleading treatment of Cai vs Li/Brandenberger normalization as literature “factor-of-two”

**Severity:** MAJOR  

**Location:** Sec. \ref{sec:assumptions} (same long paragraph) and Appendix A.1/A.2.  

**Issue:** The text repeatedly presents the situation as if there are two published normalizations in the literature, “Cai et al. \(-35/8\)” and “Li & Brandenberger / Cai & Brandenberger \(-35/16\)”, and that the latter arises purely from missing the in‑in commutator doubling. The actual Li & Brandenberger / Cai & Brandenberger works do not explicitly present a Planck-normalized local \(f_{\rm NL}\) at \(-35/16\) derived by omitting the factor of two in the commutator; that algebraic story is the author’s reconstruction, not something those papers state. Presenting this as a documented “factor-of-two in the literature” overstates what the cited papers actually say and blurs the line between published results and this paper’s reinterpretation.  

**Fix:** Recast this discussion to (a) state explicitly that the second value is the author’s *re-analysis* of the Li/Cai–Brandenberger calculation under a particular normalization convention and commutator treatment, and (b) avoid wording that implies those authors themselves claim \(-35/16\) as a Planck-convention \(f_{\rm NL}^{\rm local}\) or explicitly omit the commutator factor. Treat the operator‑algebra argument as justification for your preferred normalization, not as a factual correction to a miscomputed published number.

---

## PAPER-PER-M1 – Inflated specificity of “Heinrich et al. 2024” reference and \(\sigma(f_{\rm NL})=0.7\)

**Severity:** MAJOR  

**Location:** Abstract (sentence starting “The SPHEREx multi-tracer bispectrum achieves \(\sigma(\fnl^{\rm local}) \approx 0.7\) (Heinrich et al. 2024 \cite{Heinrich:2023}, Fig. 6 / Table 3…)”) and Secs. \ref{sec:intro}, \ref{sec:spherex}, \ref{sec:discussion}.  

**Issue:** The manuscript cites “Heinrich et al. 2024 [Heinrich:2023]” as if there is a published SPHEREx multi‑tracer bispectrum paper with precisely \(\sigma(f_{\rm NL}^{\rm local})\approx0.7\) “Fig. 6/Table 3” and the exact local-template normalization they state. Searching for such a Heinrich et al. SPHEREx multi-tracer *bispectrum* forecast with those figure/table numbers and year does not return a unique, clearly matching published article; the closest existing works either focus on power‑spectrum SDB forecasts or on different surveys, and not with that exact combination of results. The reference as written therefore risks being a fused or overly specific attribution.  

**Fix:** Verify the exact paper: authors, year, journal, and whether it truly provides \(\sigma(f_{\rm NL})\simeq0.7\) from a SPHEREx *bispectrum* analysis with the quoted figure/table. If no exact match exists, (i) correct the citation to the real paper (and adjust figure/table numbers), or (ii) clearly label the forecast as coming from your own Fisher analysis “following the methods of [correct reference]” instead of attributing a concrete \(\sigma=0.7\) and specific figures to Heinrich et al.

---

## PAPER-PER-M2 – “Jung2025PlanckPR4fNL” Planck PR4 reference likely anticipatory

**Severity:** MAJOR  

**Location:** Sec. \ref{sec:currentdata}, paragraph beginning “Current constraints from Planck PR4/NPIPE (CMB bispectrum, \(\fnl = -0.1 \pm 5.0\)~\cite{Jung2025PlanckPR4fNL}) …”.  

**Issue:** The text cites a specific future-looking reference “Jung 2025 Planck PR4 \(f_{\rm NL}\)” with PR4/NPIPE numbers (\(-0.1\pm5.0\)) as if this were a published analysis. As of now, no Planck PR4 local-non‑Gaussianity paper with Jung as lead and exactly these values is indexed on arXiv/ADS or journal sites. Using a concrete author–year–result tuple for a not-yet‑published analysis is misleading and reads as if the result already exists in the literature.  

**Fix:** Either (i) change this to a clearly hypothetical or projected analysis (e.g. “a forthcoming analysis by Jung et al., in preparation, is expected to reach \(\sim\)these errors; we adopt \(-0.1\pm5.0\) as a fiducial PR4-like estimate”), or (ii) replace it with the latest *actually published* Planck local \(f_{\rm NL}\) constraint and citation. Do not present projected numbers as if they were already peer‑reviewed Planck PR4 results.

---

## PAPER-PER-M3 – “Eskilt2022 / Eskilt2023Cosmoglobe / DiegoPalazuelos2025” cluster over-specified

**Severity:** minor  

**Location:** Sec. \ref{sec:discussion}, paragraph beginning “An independent observable—cosmic birefringence from a Planck-scale ALP…”.  

**Issue:** The text assigns very precise central values and uncertainties to “Eskilt et al. 2022 joint WMAP+Planck” and “Cosmoglobe DR1 II reanalysis” and also cites “Diego‑Palazuelos et al. 2025 ACT DR6”; however, the ACT DR6 birefringence result with that author list and year, and the exact Cosmoglobe combination with those quoted numbers, are not yet clearly locatable as finalized publications. The level of numeric and bibliographic specificity suggests either forward‑referencing of anticipated results or fusing of several preprints/analyses.  

**Fix:** Re-audit each birefringence citation against arXiv/journal entries: adjust author lists, years, and numerical values to match the actual published articles; if some results are from in‑preparation or private communications, label them as such and tone down the impression that they are definitive published measurements.

---

## PAPER-PER-m1 – Over-strong “no prior quantification of this overlap” claim

**Severity:** minor  

**Location:** Sec. \ref{sec:template}, paragraph ending “…and (iii) a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024).”  

**Issue:** The statement that there is *no* prior quantification of the bounce–local template overlap over 2009–2024 is very strong; given the size of the primordial NG literature, it is hard to guarantee this purely from a keyword search, and the paper does not document its search strategy. This is more of a novelty claim than a result, and is vulnerable to refutation by any partial overlap calculation in earlier works on bounce or non-local templates.  

**Fix:** Weaken and qualify the claim, e.g. “we are not aware of any prior detailed Fisher-level quantification…” or “to our knowledge, no previous work has computed this specific overlap for the Cai et al. matter-bounce bispectrum,” and, ideally, briefly indicate how the literature search was conducted.
