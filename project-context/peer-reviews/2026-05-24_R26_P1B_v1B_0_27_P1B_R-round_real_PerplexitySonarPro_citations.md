# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-24_R26_P1B_v1B_0_27
**Wall time**: 26.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=22741, completion=2423, total=25164

---

## PAPER-PER-B1 — Mis-cited Planck/ACT joint birefringence paper

**Grade:** MAJOR  

**Location:** Abstract paragraph (3), sentence citing “the published joint Planck+ACT value \(\beta=0.342^\circ\pm0.094^\circ\) (3.6σ)~\cite{Eskilt2022b}”, and §VI “Headline observational constraint” first sentence.  

**Issue:** The manuscript attributes the joint Planck+ACT DR6 birefringence result \(\beta=0.342^\circ\pm0.094^\circ\) (3.6σ) to “Eskilt et al. 2022b” and cites it as \cite{Eskilt2022b}, but the canonical cosmic-birefringence measurement at roughly that level is Eskilt & Komatsu’s Planck-only reanalysis (Einstein-Boltzmann solver with birefringence and improved systematics) rather than a published Planck+ACT joint calibration paper with that exact value and uncertainty; there is no widely indexed “Eskilt et al. 2022b” Planck+ACT joint birefringence paper with \(\beta=0.342^\circ\pm0.094^\circ\) (3.6σ) matching this description in ADS, arXiv, or major journal databases, which strongly suggests the reference label is either pointing to the wrong paper or combining the numeric result of one work with the (nonexistent) “Planck+ACT joint” descriptor of another.  

**Fix:** Explicitly identify the actual paper that reports \(\beta\approx0.34^\circ\) (author list, year, journal/arXiv ID) and make sure the BibTeX entry \texttt{Eskilt2022b} matches that publication; if no Planck+ACT joint paper with these numbers exists, change the text to the correct experiment(s) (e.g., Planck-only reanalysis) and adjust the “joint Planck+ACT” language accordingly, or else clearly mark \(\beta=0.342^\circ\pm0.094^\circ\) as coming from the author’s own internal joint fit rather than a published external result.  

---

## PAPER-PER-B2 — Diego-Palazuelos / ACT-DR6 citation label likely mismatched

**Grade:** MAJOR  

**Location:** Abstract paragraph (2) “Planck/ACT DR6 2.4–2.9σ~\cite{Eskilt2022,DiegoPalazuelos2025}”; §IV first sentence “\(\beta = 0.30^\circ\pm0.11^\circ\) (Planck NPIPE~\cite{DiegoPalazuelos2022}) and \(\beta = 0.215^\circ\pm0.074^\circ\) (ACT DR6~\cite{DiegoPalazuelos2025})”.  

**Issue:** The ACT DR6 birefringence measurement is due to Diego-Palazuelos et al. (and collaborators) in an ACT DR6 polarization paper; likewise, the Planck NPIPE birefringence value \(\beta=0.30^\circ\pm0.11^\circ\) is associated with specific Planck reanalyses rather than a generic “Diego-Palazuelos 2022” NPIPE paper. In the provided text, both Planck and ACT results are referenced solely by personal-name labels \texttt{DiegoPalazuelos2022} / \texttt{DiegoPalazuelos2025} without any visible verification that (i) the 0.30°±0.11° value really appears in a “Diego-Palazuelos 2022” NPIPE paper, or (ii) the 0.215°±0.074° value is actually from a 2025 ACT DR6 paper with Diego-Palazuelos as lead author rather than, e.g., an ACT collaboration paper led by another first author. This is a classic “fused metadata” risk: numeric values and experiments look plausible, but the specific authors/years implied by the labels are not confirmed against actual arXiv or journal entries.  

**Fix:** Look up the actual Planck NPIPE birefringence and ACT DR6 birefringence publications in ADS/arXiv (by experiment + keyword “cosmic birefringence”), then set each BibTeX entry so that author list, year, arXiv ID, title, and the quoted \(\beta\) and \(\sigma\) all match a real paper; if any of the numbers are instead from your own internal fits, relabel them as such and remove misleading external citations.  

---

## PAPER-PER-B3 — Liu et al. EC torsion paper likely mis-identified

**Grade:** MAJOR  

**Location:** §III “Independent cross-validation” last sentence: “Liu et al. \cite{ECTorsionDESI2025} constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = -5.7 to -6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”  

**Issue:** The citation \texttt{ECTorsionDESI2025} describes a 2025 Einstein–Cartan torsion analysis that already incorporates DESI DR2, Pantheon+, DES-SN5YR, and Planck 2018 with quantified AIC preference (ΔAIC ≈ -6). There is currently no easily discoverable arXiv or journal article matching that exact combination of model (EC torsion), dataset stack (DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018), and specific ΔAIC range, which strongly suggests this reference is either (a) an in-prep manuscript not yet on arXiv, or (b) a synthetic fusion of several different works (e.g., Liu+ on EC models plus separate DESI DR2 cosmology papers) into one non-existent paper. Presenting it as a published external “Liu et al. 2025” with that precise dataset mix and AIC result is misleading.  

**Fix:** If this is an unpublished in-preparation analysis, relabel it as “Liu et al., in prep.” with an explicit note and remove any implication that it is an external published reference; if instead it is meant to cite a real paper, replace \texttt{ECTorsionDESI2025} with the actual arXiv ID and correct description of the model and datasets, and verify that the ΔAIC numbers you quote actually appear in that paper.  

---

## PAPER-PER-m1 — DESI DR2 cosmology reference may be confabulated

**Grade:** minor  

**Location:** §III “Independent cross-validation” and §VI cross-paper discussion mentioning “DESI DR2” and citing \cite{DESI2025DR2}.  

**Issue:** The text refers to “DESI DR2” cosmology results in a 2025 DESI collaboration paper \cite{DESI2025DR2}, including specific constraints and the label “DESI 2025 DR2” as if a finalized DR2 cosmology paper with that exact naming and year already exists. DESI DR2 cosmology results are anticipated, but at the time implied by the paper’s timestamp, no definitive, citable DESI DR2 dark-energy w0–wa paper with that BibTeX label, year “2025”, and exact title is obviously locatable via arXiv or ADS, suggesting that the BibTeX key and metadata may be forward-looking or partially invented rather than matching a real, published DESI DR2 paper.  

**Fix:** Confirm whether a DESI DR2 cosmology paper has actually been released and indexed (check arXiv and the DESI publications list); if not yet published, change the wording to “forthcoming DESI DR2 results” without hard numbers and either drop the citation or mark it as “DESI Collaboration, in preparation”; if a real DR2 paper exists, update the citation to its correct author list, title, and arXiv ID.  

---

## PAPER-PER-m2 — LiteBIRD birefringence forecast citation underspecified

**Grade:** minor  

**Location:** §VI “LiteBIRD forecast” sentence: “LiteBIRD is projected to achieve σ(β) ≈ 0.03°~\cite{LiteBIRD2023}.”  

**Issue:** The label \texttt{LiteBIRD2023} is used for a birefringence-forecast number (σ(β) ≈ 0.03°) but LiteBIRD’s public documents consist of several White Papers and design overviews with different years and author lists; without checking against a specific arXiv ID or journal reference, it is unclear whether \texttt{LiteBIRD2023} points to a real, uniquely identifiable document that actually quotes σ(β) ≈ 0.03°, or whether the number has been taken from internal forecasts and attached post hoc to a generic LiteBIRD citation. This is more of a traceability problem than a physics error.  

**Fix:** Identify the precise LiteBIRD design or forecast paper that reports σ(β) at ~0.03° (title, collaboration, arXiv ID) and ensure the BibTeX entry \texttt{LiteBIRD2023} matches it; if the 0.03° figure is instead from internal notes or a non-public forecast, state that explicitly and avoid citing it as a published external result.  

---

## PAPER-PER-n1 — Cross-paper readiness table versions stale relative to current self-citation

**Grade:** nit  

**Location:** §VII Table \ref{tab:crosspaper}: P1(b) row lists “P1(b) v1B.0.13, 67% readiness, key blocker Tab.~\ref{tab:iter2_posterior}; ln B pending”, while the current manuscript header and internal commentary refer to v1B.0.27 with several completed R25x rounds.  

**Issue:** The cross-paper table is being used as a quasi-citation of the status of P1(b) and P1(a–P4) but still lists P1(b) as v1B.0.13 with an old readiness percentage and key blocker, despite the rest of the LaTeX source clearly being v1B.0.27 with R25a–R25g changes implemented and some of those blockers already closed. This makes this internal “citation” of your own paper’s status inconsistent with the current version number and could confuse readers relying on the table as a quick status reference.  

**Fix:** Update the P1(b) row in Table \ref{tab:crosspaper} so that the version and key-blocker description match the present manuscript (v1B.0.27, with the model-comparison block removed and ln B still pending, etc.), or else add a parenthetical note that the table reflects the cross-paper status as of an earlier date and is not being kept in sync with later version increments.
