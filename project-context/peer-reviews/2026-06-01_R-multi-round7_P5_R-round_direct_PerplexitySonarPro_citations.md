# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round7
**Wall time**: 16.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35860, completion=1503, total=37363, search_context_size=low, cost={'input_tokens_cost': 0.10758, 'output_tokens_cost': 0.02254, 'request_cost': 0.006, 'total_cost': 0.13612}

---

## BLOCKER-PAPER-B1 – Misclassified Ullah et al. 2026 (T-Web DR1) as “submitted to MNRAS”

**Location:** Bibliography, `\bibitem{TWebDESI2026}` and §XIII (“Concurrent-literature DR1/EDR cosmic-web cross-validation”).  

**Issue:** arXiv:2604.02463 (Ullah, Awais, Matos, Suárez‑Pérez) exists with the correct title and author list, but there is no public record that it is “submitted to MNRAS” or accepted there; that submission status is not verifiable from arXiv, ADS, or publisher sites.[1][2] The paper is being presented with a specific journal‑submission state that may be inaccurate.  

**Fix:** Remove the “submitted to MNRAS” qualification and describe it neutrally as an arXiv preprint (e.g., “2026, arXiv:2604.02463”) unless and until an actual journal submission/acceptance is verifiable.

---

## MAJOR-PAPER-M1 – Internal-only companion papers cited as literature

**Location:** Bibliography entries `\bibitem{golden_chirality_2026}` and `\bibitem{golden_fnl_2026}`, and multiple mentions in text (Introduction, Relation to Paper IV, Discussion).  

**Issue:** Both “Paper IV” and “Paper II” are internal manuscripts without arXiv IDs or journal venues; the bibitems currently read like standard literature references but point only to a GitHub path and explicitly say “an arXiv identifier will be assigned upon submission.” They are being used heavily as if they were established external results (e.g., for the monopole offset, dipole bounds, and cosmological interpretation) while their status is essentially “unpublished internal work.”  

**Fix:** In the bibliography and all first mentions, explicitly label them as “unpublished internal manuscript, in preparation; not peer‑reviewed” and avoid treating them as part of the external literature (e.g., say “companion internal analysis” rather than citing them on the same footing as refereed or arXiv work).

---

## MAJOR-PAPER-M2 – DESIVAST catalog description slightly misaligned with official metadata

**Location:** §XIII, paragraph beginning “A complementary public DR1 product, DESIVAST~\cite{DESIVAST2025}…”.  

**Issue:** Rincon et al. 2025 (ApJ 982, 38; arXiv:2411.00148) describes DESIVAST as a void catalog based on DESI BGS DR1 using VoidFinder and ZOBOV-based methods, but the text here glosses it as “a publicly released, peer‑reviewed DR1 BGS void catalog at low z (VoidFinder + ZOBOV watershed algorithms)” and later relies on detailed counts and structure. While broadly correct, the phrase “publicly released, peer‑reviewed DR1 BGS void catalog” suggests an official DESI‑collaboration VAC; in the paper it is authored by Rincon et al. (not the DESI Collaboration paper) and is not branded as a DESI value‑added catalog in the DESI sense.  

**Fix:** Rephrase to “a public void catalog constructed from DESI DR1 BGS data (Rincon et al. 2025, ApJ 982, 38) using VoidFinder and ZOBOV‑based methods” and avoid implying it is an official DESI VAC product.

---

## minor-PAPER-m1 – DESIVAST 101,863 “holes” wording vs. catalog structure

**Location:** §XIII, paragraph “The DESIVAST public release … provides the VoidFinder NGC/SGC FITS files … 89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids.”  

**Issue:** In Rincon et al. and the DESIVAST distribution, the terms “voids”, “holes”, and “maximal voids” have specific technical meanings (e.g. maximal voids built from multiple holes). The paper’s phrasing “101,863 interior hole spheres comprising the 3,765 maximal voids” is plausible but not literally spelled out in that wording in the original catalog description; if taken literally, it could be read as quoting DESIVAST’s text rather than summarizing.  

**Fix:** Make this clearly paraphrastic, e.g., “DESIVAST provides 3,765 maximal voids constructed from 101,863 constituent interior spheres (holes) in the NGC and SGC samples,” and, if desired, add a short in‑text note “numbers from Rincon et al. 2025 and the public FITS headers” rather than implying exact quoted terminology.

---

## minor-PAPER-m2 – ASTRA catalog scope phrasing

**Location:** §XIII, paragraph starting “A second concurrent DESI cosmic-web paper~\cite{ASTRADESI2026}…”.  

**Issue:** arXiv:2604.01456 (Zapata‑Zuluaga et al.) is correctly cited as an EDR‑based probabilistic environment catalog, but describing it as providing a “BGS-anchored volume-filling-fraction calibration” is close to verbatim language from the abstract; this is fine scientifically but rides the line between paraphrase and quotation without quotation marks or explicit “following their terminology”.  

**Fix:** Either put the exact phrase in quotation marks and attribute (“as they describe, they ‘calibrate…’”), or lightly rephrase to avoid near‑verbatim reuse while keeping the meaning (e.g., “they calibrate their thresholds against BGS such that the inferred volume fractions match those reported for GAMA”).

---

## nit-PAPER-n1 – DESIVAST author list truncation / “et al.” placement

**Location:** Bibliography `\bibitem{DESIVAST2025}`.  

**Issue:** Rincon et al. 2025 has a relatively long author list including Rincon, BenZvi, Douglass, Veyrat, and others; the bibitem uses “H. Rincon, S. BenZvi, K. A. Douglass, D. Veyrat \textit{et al.}” which is acceptable, but in text the first mention uses “H. Rincon, S. BenZvi, K. A. Douglass, D. Veyrat \textit{et al.}” only in the bib while §XIII refers generically to “Rincon et al. 2025” without initials. For consistency and to avoid subtle confusion with earlier drafts that mis‑attributed authorship to the DESI Collaboration, it would be cleaner to adopt a single style.  

**Fix:** Standardize to “Rincon et al. (2025)” in the text and keep a consistent “Rincon, BenZvi, Douglass, Veyrat et al.” form in the bibitem, explicitly dropping any residual implication of DESI‑collaboration authorship.
