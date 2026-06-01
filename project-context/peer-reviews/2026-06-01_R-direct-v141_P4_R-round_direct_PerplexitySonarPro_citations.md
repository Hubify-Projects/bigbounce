# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-direct-v141
**Wall time**: 25.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=108293, completion=1769, total=110062, search_context_size=low, cost={'input_tokens_cost': 0.32488, 'output_tokens_cost': 0.02653, 'request_cost': 0.006, 'total_cost': 0.35741}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited Iye & Yagi 2026 paper

**Location:** §7.1 “Comparison with Previous Work”, paragraph discussing Iye & Yagi (2026), around  
`Iye~\&~Yagi~(2026)~\cite{Iye:2026P6} ... now public as arXiv:2605.05570 (May 2026)`.

**Issue:** The placeholder citation key `\cite{Iye:2026P6}` does not correspond to any standard bib entry here and the text asserts a specific arXiv ID `2605.05570` for a 2026 paper “Spin Parity of Spiral Galaxies VI …”. No such arXiv entry is currently verifiable; the title/ID pair appears to be forward‑dated / speculative rather than confirmed from ADS/arXiv.

**Fix:** Remove the concrete arXiv ID and year claim or clearly mark this as anticipated/unpublished work, or replace with a real, currently indexed paper (with correct arXiv ID, authors, and journal) once it exists. Until then, either drop this sentence or rewrite as “a forthcoming HSC-WIDE analysis (Iye & Yagi, in prep.)” without an arXiv identifier.

---

## PAPER-PER-B2 (MAJOR) – Mischaracterization of Motloch & Pen 2021

**Location:** §7.4 “Motloch & Pen (2021)”, first paragraph:  
`Motloch & Pen (2021)... using Galaxy Zoo 2 citizen-science CW/CCW image classifications of ~2×10^5 spirals.`

**Issue:** Motloch & Pen (2021) use galaxy spin directions inferred from the DESI Legacy Imaging Surveys with an automated chirality classifier and SDSS imaging, not a Galaxy Zoo 2 CW/CCW label sample of ∼2×10^5 spirals as described here.[1][3] The stated data source and sample characterization are incorrect.

**Fix:** Rewrite the description to match the actual paper: e.g., “Motloch & Pen (2021) used spins inferred for SDSS galaxies with an automated classifier on DESI Legacy imaging and reported a marginal (~2σ) correlation between spin and the large-scale tidal field” and remove the “Galaxy Zoo 2 ∼2×10^5 spirals” wording.

---

## PAPER-PER-M3 (MAJOR) – Inconsistent / evolving significance and thresholds (needs one canonical set)

**Location:** Throughout abstract, §Introduction, §Sensitivity, §Results (esp. §4.1, §4.6, §9.6, Conclusions).

**Issue:** Multiple different numerical “floors” and significances are given for the same concepts, sometimes conflicting:  
- Fisher floor quoted as 0.29% full amplitude at 3σ, but also “0.14–0.20%” in places as if for the same quantity.  
- Empirical sensitivity sometimes given as “≥0.75%” (50%-recovery-at-3σ), elsewhere compared to a 0.29% Fisher floor as a factor 2.5 degradation, but that comparison mixes full catalog vs HC subsample.  
- Hemisphere and canonical-mask ℓ=1 significances are variously described as 3.05σ local, <1σ post-LEE, p_LEE ≤ 10⁻⁴ (~3.7σ) under a different null, plus +3.64σ MASTER vs +1.68σ monopole-only vs bootstrap −0.22σ etc.

This makes it hard to see one consistent, numerically coherent sensitivity story and risks overclaiming by selectively comparing different estimators and samples.

**Fix:** Choose a single canonical set for: (a) statistical Fisher floor (state clearly it is 0.29% full-amplitude at 3σ from N=3.2M spirals); (b) empirical 50%-recovery-at-3σ threshold (0.75% from the HC subsample, and explicitly say that is stricter than the Fisher floor because of subsampling and systematics); (c) for canonical-mask and hemisphere signals, present one table that lists, for each estimator, the data value, null type, N_MC, and corresponding p or z, and explicitly state which one is the *official* “no cosmological dipole” verdict (the strict-superset ℓ=1 MASTER and the 0.43σ real-space dipole), with others labeled diagnostic only. Remove cross-sample Fisher vs empirical comparisons that mix full catalog and HC subsample, or re-express them only as like-for-like comparisons.

---

## PAPER-PER-m4 (minor) – CE-ResNet catalog description slightly off

**Location:** §1 Introduction, CE-ResNet paragraph:  
`Their catalog of 1.95 million galaxies from DESI Legacy pre-imaging yields CW/CCW = 0.998... across the SDSS+DESI imaging footprint; CE-ResNet has no NS head and all galaxies receive a CW or CCW label.`

**Issue:** Jia et al. (2023) report 1,953,246 spiral classifications (not “all galaxies receive CW or CCW”) and their catalog is built primarily on DESI Legacy imaging, with SDSS used in training rather than as an equal part of the footprint.[2] The current wording could be read as “all DESI+SDSS galaxies in footprint get a CW/CCW label” which is stronger than what the paper says.

**Fix:** Soften and align with the paper, e.g.: “Jia et al. (2023) released chirality classifications for 1.95 million galaxies based on DESI Legacy imaging (with SDSS used in training); CE-ResNet uses a binary CW/CCW output without an explicit NS class, so all objects in their catalog are assigned one of the two chiralities.”

---

## PAPER-PER-m5 (minor) – SpArcFiRe reference details

**Location:** §7.3 “SpArcFiRe”, Davis & Hayes reference.

**Issue:** The text currently gives SpArcFiRe as “Davis:2014 … ApJ 790, 87” which is correct, but earlier in the comments it mentions a “Hayes-Davis DR9 update” without a clear citation, and it hints at “140k” galaxies where Davis & Hayes (2014) itself refers to ~644 galaxies in the main test and a larger SDSS DR7 catalog in later work.[4] The “∼140,000 galaxies” catalogue statement needs a precise citation if it is meant to be a specific public release.

**Fix:** Either (a) add the explicit paper or data release that corresponds to the ∼140k SpArcFiRe catalog (authors, year, arXiv/journal) or (b) rephrase to a safer, sourced statement grounded in Davis & Hayes 2014 (e.g. “SpArcFiRe has been applied to SDSS to produce catalogues of order 10⁵ galaxies; see Davis & Hayes 2014 and subsequent SDSS DR9 releases”) and ensure any numeric catalog size matches a verifiable source.

---

## PAPER-PER-n6 (nit) – Over-precise numbers and future-dated references

**Location:** Multiple places in abstract, intro, sensitivity section, and discussion.

**Issue:** The manuscript often quotes very high-precision numbers (e.g. z = −250.15, −264.5, p_MC = 2/10,000 = 0.0023 vs previous 0.006) and also refers to 2026 future dates and tags (“Houston Golden — 2026”, “Iye & Yagi 2026” before publication is confirmed). This is stylistically unusual for cosmology papers and makes the narrative brittle if any pipeline rerun slightly changes the numbers or if anticipated papers do not appear as expected.

**Fix:** Round quoted z-scores and probabilities to a sensible precision (e.g. 2–3 significant figures) in the narrative text, reserving full precision for machine-readable JSON. For future or anticipated work, avoid giving specific years and arXiv IDs unless they exist and are verifiable; use “in prep.” or generic phrasing until they are published.
