# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 21.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100538, completion=1665, total=102203, search_context_size=low, cost={'input_tokens_cost': 0.30161, 'output_tokens_cost': 0.02498, 'request_cost': 0.006, 'total_cost': 0.33259}

---

## PAPER-PER-B1 (BLOCKER) – Wrong citation for Shamir 2012

**Location:** Introduction, first paragraph on prior claims; also bibliography entry `\bibitem{Shamir:2012}`.  

**Issue:** The text cites “Shamir (2012) [\cite{Shamir:2012}]” as the SDSS spiral‐handedness paper with 10⁴ SDSS galaxies and 5–20% asymmetries, but the bibliography entry for `Shamir:2012` is actually the *Phys. Lett. B* parity-violation paper “Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis” (arXiv:1207.5464), based on ∼10⁵ SDSS galaxies and different details. The description (sample size, survey, amplitudes) in the prose does not match what that 2012 paper reports; it matches Shamir’s earlier SDSS work (e.g. 2011 ApJ 736, 141) rather than the 2012 PLB paper.[Shamir:2012]  

**Fix:** Decide which Shamir paper you actually intend to summarize.  
- If it is the 2012 PLB paper (arXiv:1207.5464), adjust the text to use that paper’s correct sample size, survey description, and quoted asymmetry/dipole statistics.  
- If it is an earlier SDSS-only paper (e.g. Shamir 2011 ApJ 736, 141), change the citation key, arXiv ID, title, journal, and year in the bibliography to that paper and update the in‑text year accordingly; do not use the PLB 2012 metadata for a different article.


## PAPER-PER-M1 (MAJOR) – Fused reference: Motloch et al. authorship / title mismatch

**Location:** Sec. \ref{sec:motloch}, bibliography entry `\bibitem{Motloch:2021}`.  

**Issue:** The paper cites “Motloch \etal~\cite{Motloch:2021}” and describes “Motloch & Pen (2021)”, but the bibliography entry lists four authors “P. Motloch, H.-R. Yu, U.-L. Pen, and Y. Xie” and a Nature Astronomy title about “observed correlation between galaxy spins and initial conditions.” The well-known Nature Astronomy paper is authored by Yu, Pen & Xie with differing author order, and the arXiv/source metadata do not match the four-author string given here. This is a fused-metadata reference (author list from one version / description from another) and likely misidentifies the canonical paper.[Motloch:2021]  

**Fix:** Re‑verify the Nature Astronomy “galaxy spins and initial conditions” paper on ADS/arXiv and correct the reference to its exact author list, title, journal, volume, page and year. Ensure that the in‑text description (“Motloch & Pen 2021” vs full author list) is consistent with that corrected citation; do not invent additional coauthors or mis-order them.


## PAPER-PER-M2 (MAJOR) – Incorrect or ambiguous Shamir 2022 DESI sample size description

**Location:** Introduction, paragraph starting “Shamir (2022) [\cite{Shamir:2022DESI}]”, and again in the “Comparison with Previous Work” section.  

**Issue:** The prose describes Shamir (2022) DESI Legacy as “$\sim\!1.3\times10^6$ input galaxies reduced to $\sim\!2\times10^5$ after Ganalyzer cuts” and later as “nearly $1.3\times10^6$ spiral galaxies,” citing the same MNRAS 516, 2281 paper. The actual MNRAS paper’s abstract and data description give a different breakdown and do not support treating “1.3×10⁶” as the *spiral* sample; that 1.3M is the parent catalogue, not the final spiral set.[Shamir:2022DESI]  

**Fix:** Align the text to the exact numbers in Shamir (2022): clearly distinguish between the full DESI Legacy parent sample and the much smaller spiral subsample after Ganalyzer filtering, and do not describe 1.3×10⁶ as “spiral galaxies” unless that is explicitly what Shamir reports.


## PAPER-PER-m1 (minor) – Mis-cited “Yu et al. 2020” transfer-function reference

**Location:** Sec. \ref{sec:motloch}, sentences referencing “linear-theory framework of \cite{Yu:2020}” and tidal-torque transfer functions.  

**Issue:** The Yu et al. 2020 paper you cite is a PRL on primordial chirality and tidal torque, but the way it is referenced suggests a fully developed quantitative transfer function from primordial parity-odd tensor modes to late-time morphology dipoles, which that paper does not provide for your exact observable; it focuses on spin–tidal correlations and CMB/LSS signatures, not specifically on 2D projected arm winding in DESI Legacy.[Yu:2020]  

**Fix:** Rephrase the text to say that Yu et al. provide a *framework / motivation* for spin–tidal correlations and possible chiral signatures, but that a quantitative transfer function from primordial chiral tensors to your projected chirality dipole is not derived there and remains future work (as you state elsewhere).


## PAPER-PER-m2 (minor) – SpArcFiRe sample-size / agreement claims not supported by cited paper

**Location:** Sec. \ref{sec:sparcfire}, paragraph beginning “The SpArcFiRe algorithm…”.  

**Issue:** The text states that SpArcFiRe provides catalogs of “∼140,000 galaxies” and quotes agreement figures with GZ1 (e.g. “85.8% overall, 92.5% at high confidence”) that are not explicitly present in the Davis & Hayes 2014 ApJ paper you cite, which describes a method and a much smaller test sample.[Davis:2014] These numbers appear to come from later, unpublished or web-catalog work rather than the referenced article, so as written they are not supported by the citation.  

**Fix:** Either (a) remove the specific numerical claims and keep a qualitative comparison (“SpArcFiRe produced a public catalog and showed high self-consistency but lower agreement with GZ1”), or (b) add and verify the correct citation(s) for the catalog paper / technical report where those 140k and 85.8%/92.5% numbers are actually documented.


## PAPER-PER-n1 (nit) – Ambiguous reference to “Iye & Yagi, in prep.” as if citable

**Location:** Sec. \ref{sec:shamir}, sentence starting “An anticipated Iye & Yagi forthcoming HSC-WIDE Survey…”  

**Issue:** You mention “Iye & Yagi, in prep.” and say an “earlier placeholder citation identifier… has been removed,” but there is no corresponding entry in the bibliography and “in prep.” work is not verifiable. As written, this looks like a dangling reference in the body of a paper that otherwise stresses citation rigor.  

**Fix:** Either (i) delete the “Iye & Yagi, in prep.” sentence entirely, or (ii) clearly label it as an informal expectation without treating it as part of the literature (e.g. “Private communication with M. Iye indicates that a related HSC-wide analysis is in preparation; we do not rely on it here and therefore do not cite it formally.”).
