# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 23.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100793, completion=1555, total=102348, search_context_size=low, cost={'input_tokens_cost': 0.30238, 'output_tokens_cost': 0.02333, 'request_cost': 0.006, 'total_cost': 0.3317}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited Motloch & Pen paper

**Location:** §\ref{sec:motloch}, around “Motloch & Pen (2021)… using SDSS spirals with spin‑direction estimates from an automated chirality classifier applied to DESI Legacy imaging cutouts.”

**Issue:** The Motloch & Pen paper is an ApJ Letters article on spin–tidal-field correlations using SDSS spirals and tidal fields from BOSS / 2MRS etc.; it does **not** use a “chirality classifier applied to DESI Legacy imaging cutouts” as described. The arXiv:2003.04325 / ApJL 905 L40 article’s methodology is misrepresented (pipeline and imaging source conflated with later DESI‑based work).

**Fix:** Replace the sentence with a methodologically accurate description of Motloch & Pen, e.g. “using SDSS spiral galaxies with spin directions inferred from SDSS imaging and large‑scale tidal field reconstructions,” and explicitly remove the DESI‑Legacy‑cutout classifier reference. Verify against the actual ApJL text and update the bibitem if necessary.


## PAPER-PER-B2 (MAJOR) – Confusing / fused citation for Ivezic LSST reference

**Location:** Bibliography entry for Ivezić et al. (LSST), plus surrounding discussion (e.g., §\ref{sec:sensitivity}, §\ref{sec:future}).

**Issue:** The bibitem explicitly notes that arXiv:0805.2366 is “the older LSST Science Book preprint, NOT the preprint of this specific ApJ reference‑design article,” but earlier versions evidently mixed that arXiv ID with ApJ 873, 111. Even though the current text says the arXiv ID is removed, the bib comment itself will look like a fused-ID confabulation to readers and referees.

**Fix:** Make the LSST reference purely to **ApJ 873, 111 (2019)** with correct author list and DOI, and omit the 0805.2366 discussion from the bib entry. If you want to acknowledge the LSST Science Book, add it as a separate, clearly labeled citation with its correct arXiv ID and without implying it is the journal preprint for the ApJ article.


## PAPER-PER-M3 (MAJOR) – Shamir (2022) DESI sample size and selection description

**Location:** §\ref{sec:intro}, paragraph starting “Shamir~(2022)~\cite{Shamir:2022DESI} (arXiv:2208.13866, DESI Legacy Survey, $\sim\!1.3\times 10^6$ input galaxies reduced to $\sim\!2\times 10^5$ …).”

**Issue:** The text compresses Shamir’s DESI sample into “$\sim\!1.3\times 10^6$ input galaxies reduced to $\sim\!2\times 10^5$ after Ganalyzer deterministic decision‑tree morphological cuts”, which is a paraphrase rather than a direct quote from MNRAS 516, 2281. That reduction factor and the “deterministic decision‑tree” wording need to match Shamir’s actual described pipeline (number of imaged objects vs classified spirals, specific cut chain).

**Fix:** Re‑read Shamir 2022 (MNRAS 516, 2281, arXiv:2208.13866) and restate the sample and selection in the paper’s own terms (e.g. the exact reported number of spirals used in the asymmetry measurement and how they’re obtained), or add an explicit “of order” caveat if you keep rounded numbers. Avoid adding “deterministic decision‑tree” unless that terminology is present in Shamir’s description or you clearly mark it as your own characterization.


## PAPER-PER-m4 (minor) – Ambiguous / potentially fused SpArcFiRe “DR9-overlap” claim

**Location:** §\ref{sec:sparcfire}, paragraph starting “The published SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with 50/50 to within ~0.3%… (Davis 2014, Table 3 plus the public Hayes‑Davis DR9 update).”

**Issue:** Davis & Hayes (ApJ 790, 87) present SpArcFiRe and SDSS DR7/DR8 tests; the text here invokes a “public Hayes‑Davis DR9 update” and quantitative 0.3% balance as if it were a formal, citable journal dataset. That “DR9 update” looks like a secondary resource (web / code release) rather than a peer‑reviewed table, and the combination “Table 3 + DR9 update” is opaque enough to be a pattern‑027/028 risk (headline number without clear on‑disk artifact in the cited literature).

**Fix:** Either (a) point to a concrete, archived DR9 catalog (with DOI or arXiv / ADS‑indexed reference) and give the CW/CCW numbers explicitly, or (b) weaken the claim to “SpArcFiRe tests reported zero or very small net handedness in SDSS data” and attribute only to Davis & Hayes (ApJ 790, 87) without hanging a specific 0.3% figure on an unreferenced “DR9 update.” Also cite your own SpArcFiRe‑overlap analysis artifact if you want to support the working‑hypothesis argument.


## PAPER-PER-m5 (minor) – Motloch & Pen implications overstated vs cited paper

**Location:** §\ref{sec:motloch}, last sentences discussing Motloch & Pen and “reading‑direction bias” contamination.

**Issue:** The text says Motloch & Pen’s signal is “fully consistent with the same reading-direction citizen-science labelling bias that contaminates our own pre-equivariance pipeline,” but the cited paper does not itself frame the result that way; that is your interpretation. As written, the sentence blurs the line between what Motloch & Pen report and what you infer.

**Fix:** Rephrase to make the attribution explicit, e.g. “Given the documented reading‑direction biases in Galaxy Zoo labels, their marginal (~2σ) correlation could in principle be contaminated by similar effects; our null, which removes such biases by construction, provides a cleaner test of the same physical channel.” Do not imply Motloch & Pen themselves attribute their signal to that bias.


## PAPER-PER-n6 (nit) – Excessively long “Ivezic 2019” bibnote with internal review history

**Location:** Ivezic et al. LSST bibitem note block beginning “NOTE (v1.0.79, PER-B1 update, RETAINED FOR PROVENANCE ONLY)…”

**Issue:** The note embeds internal review history (“Perplexity Sonar Pro flags”, version numbers) inside the bibliography, which is inappropriate for a finished manuscript and may confuse readers about what is and isn’t part of the scientific citation.

**Fix:** Strip all internal‑process commentary from the bib entry. If you want to document internal QA history, move it to a separate changelog in the repository, not into the LaTeX reference list.
