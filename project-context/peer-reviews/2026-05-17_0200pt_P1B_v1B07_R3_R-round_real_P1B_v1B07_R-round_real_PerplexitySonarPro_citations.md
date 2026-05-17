# P1B_v1B07 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_0200pt_P1B_v1B07_R3_R-round_real
**Wall time**: 17.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13167, completion=1621, total=14788

---

## PAPER-PER-B1 — Self-contradiction about removal of model-comparison block (BLOCKER)

**Location:** Sec. \ref{sec:cosmo_fits} “Model-comparison statistics…” paragraph vs Conclusions §\ref{sec:conclusions}.  

**Issue:** Sec. \ref{sec:cosmo_fits} states that the numerical model-comparison block (χ²\_{\rm eff}, AIC, BIC, ln B) has been fully removed in v1B.0.7 and deferred to v1B.0.8, but the Conclusions section still quotes specific Savage–Dickey Bayes factor and AIC/BIC values (“ln B = +4.8… ΔAIC = −5.9, ΔBIC = −0.7”), directly contradicting that claim and reviving numbers already flagged as unreproducible in R2.  

**Fix (1–2 sentences):** Delete the entire sentence in Conclusions that reports ln B, ΔAIC, and ΔBIC, and explicitly state that all model-comparison statistics are deferred to v1B.0.8. Ensure the claims table (Table \ref{tab:claims}) has no remaining “Model-comparison … Deferred” row that implies any residual use of those numbers in the current version.

---

## PAPER-PER-B2 — Cross-paper reference to Paper I(a) version (MAJOR)

**Location:** Introduction, “What is NOT in this paper” paragraph: “Paper I(a) v1A.0.22”; Cross-paper status Table \ref{tab:crosspaper}: “P1(a) v1A.0.23”.  

**Issue:** The manuscript cites two different current versions for Paper I(a): v1A.0.22 in the prose and v1A.0.23 in the cross-paper table, creating internal inconsistency about which version is the canonical target for cross-references and for statements like “14 historical catalog entries; see Paper I(a) v1A.0.22”.  

**Fix (1–2 sentences):** Harmonize all references to the main theory paper to the same version (almost certainly v1A.0.23), and if “14 historical catalog entries” refers to an earlier state, explicitly note that it is historical and that the current canonical version is v1A.0.23.

---

## PAPER-PER-M1 — Eskilt et al. cosmic-birefringence citations (MAJOR)

**Location:** Abstract (Planck/ACT DR6 “2.4–2.9σ” and joint Planck+ACT “β = 0.342° ± 0.094° (3.6σ)” with refs. \cite{Eskilt2022,DiegoPalazuelos2025,Eskilt2022b}); Sec. \ref{sec:birefringence_check} “Headline observational constraint.”  

**Issue:** The paper attributes the headline β = 0.342° ± 0.094° (3.6σ) joint Planck+ACT result to Eskilt et al. (refs. “Eskilt2022b” and “Eskilt2022”), but the actual Eskilt cosmic-birefringence result is β ≈ 0.342° ± 0.070° (4.9σ) in its original form, and the 3.6σ downgraded significance, joint Planck+ACT combination, and precise 0.094° error bar are not standard numbers from the published literature; they mix values from different analyses and look like fused metadata. [1][2]  

**Fix (1–2 sentences):** Re-check the Eskilt and related birefringence papers on arXiv/ADS, cite the exact β and σ values that actually appear there (including the correct polarization combinations and instruments), and if you construct a degraded or joint value (e.g., to account for calibration systematics) label it clearly as your own derived figure rather than as a “published” number.

---

## PAPER-PER-M2 — Liu et al. EC torsion constraint paper metadata (MAJOR)

**Location:** Sec. \ref{sec:verification}, “Independent cross-validation” paragraph, citing “Liu et al. \cite{ECTorsionDESI2025} constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018…”.  

**Issue:** A DESI-DR2 + Pantheon+ + DES-SN5YR + Planck EC torsion paper by “Liu et al.” with the described dataset combination and ΔAIC ≈ −5.7 to −6.6 is not findable in arXiv/ADS under plausible search terms (Einstein–Cartan torsion, DESI DR2, Liu as lead author), suggesting that the citation may have fused a real author name with an as-yet-unpublished internal note or with unrelated DESI cosmology results. [2]  

**Fix (1–2 sentences):** Either replace this reference with a verifiable, publicly available torsion-cosmology paper (correct title, authors, arXiv ID, and journal) that actually reports the stated AIC preference, or explicitly mark the result as an internal/unpublished analysis and remove it from the formal bibliography until a real arXiv or journal reference exists.

---

## PAPER-PER-m1 — Diego Palazuelos Planck / ACT birefringence references (minor)

**Location:** Abstract; Sec. \ref{sec:data_cmb}; Sec. \ref{sec:birefringence_check}, citing “DiegoPalazuelos2022” and “DiegoPalazuelos2025” for Planck NPIPE and ACT DR6 birefringence.  

**Issue:** The text uses shorthand like “DiegoPalazuelos2025” and labels ACT DR6 as providing β = 0.215° ± 0.074°, but an ACT DR6 birefringence result at that exact value and error bar from a paper led by “Diego Palazuelos” is not directly verifiable in the current arXiv record; ACT DR6 birefringence analyses involve multiple collaborations and specific titles that should be referenced precisely. [2]  

**Fix (1–2 sentences):** Replace the placeholder-style keys “DiegoPalazuelos2022/2025” with full, accurate references (correct first author, full title, arXiv ID, journal/volume) corresponding to the Planck NPIPE and ACT DR6 birefringence measurements that actually report the two quoted β values, or adjust the numbers to match the real published results.

---

## PAPER-PER-n1 — ADS/arXiv channel metadata in the preamble (nit)

**Location:** Preamble comments: “arXiv submission: astro-ph.CO / gr-qc”.  

**Issue:** A single arXiv submission cannot simultaneously belong to two primary categories (“astro-ph.CO / gr-qc” as written); in practice, one is the primary category and the other is at most a secondary cross-list, so the current comment is slightly misleading as metadata. [1]  

**Fix (1–2 sentences):** Change the preamble to something like “arXiv primary: astro-ph.CO; cross-listed: gr-qc” or pick whichever will actually be used as the primary submission category and remove the other from this comment.
