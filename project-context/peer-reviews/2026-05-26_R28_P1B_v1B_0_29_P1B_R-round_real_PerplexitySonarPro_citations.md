# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R28_P1B_v1B_0_29
**Wall time**: 17.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=23916, completion=1377, total=25293

---

## Finding 1 — PAPER-GOLDEN2026P1A (minor)

The citation `Golden2026P1a` for “Paper I(a)” appears to be an unpublished or in‑prep companion and does not correspond to a real arXiv ID or journal reference in the current literature or ADS. [1][2]  
**Issue:** The bibliography key is used as if it were a standard external citation, but there is no publicly verifiable record (arXiv/journal) under that label, so external readers cannot locate it.  
**Fix (1–2 sentences):** Explicitly cite Paper I(a) as an internal companion manuscript with its actual arXiv ID once posted (or “in preparation” if not yet public), and ensure the bibliography entry includes either an arXiv number or a clear “unpublished manuscript” tag.

---

## Finding 2 — PAPER-GOLDEN2026P2–P4 (minor)

The cross‑paper references `Golden2026P2`, `Golden2026P3`, and `Golden2026P4` to “Paper II–IV” similarly do not match any current arXiv or journal records discoverable via arXiv.org or ADS. [1][2]  
**Issue:** These keys are treated as standard literature citations but resolve only to internal project nomenclature, so they function as opaque labels rather than verifiable references.  
**Fix (1–2 sentences):** Update each to include a real arXiv ID or journal citation once available, or mark them explicitly as “companion manuscript, in preparation” with enough metadata (title, author, year) that readers can distinguish them from external, peer‑reviewed literature.

---

## Finding 3 — PAPER-ESKILT2022B (MAJOR)

The paper cites a “joint Planck+ACT value” with key `Eskilt2022b` and headline constraint \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\), but the only easily discoverable Eskilt cosmic‑birefringence paper is “Cosmological birefringence from ALP dark matter” (Planck‑only) and the ACT DR6 birefringence measurements are by Diego‑Palazuelos et al., not Eskilt et al., with differing numerical values. [1][2]  
**Issue:** Author and experiment attribution look fused: an Eskilt paper is being credited with a specific “joint Planck+ACT” value and σ‑level that, in the published record, are associated with different author lists and analyses, suggesting mixed metadata (author list from one work + numerical result from another).  
**Fix (1–2 sentences):** Re‑audit the “0.342° ± 0.094° (3.6σ)” reference against the actual Planck+ACT joint analysis; correct the citation key (authors, year, journal/arXiv ID) to match the real joint paper, or, if the value is from combining separate Planck and ACT measurements, attribute it as such and remove the “joint” label and Eskilt authorship.

---

## Finding 4 — PAPER-DIEGOPALAZUELOS2025 (MAJOR)

The text cites an ACT DR6 result as “DiegoPalazuelos2025” with \(\beta = 0.215^\circ \pm 0.074^\circ\), but current ACT birefringence work by Diego‑Palazuelos et al. is associated with earlier releases (e.g., NPIPE/ACT DR4/DR6 timing) and has somewhat different central values and uncertainties. [1][2]  
**Issue:** The combination of year “2025”, “DR6” tag, and the exact \(0.215^\circ \pm 0.074^\circ\) value is not currently traceable to a specific, live arXiv ID or journal reference, suggesting that the numeric result and metadata may be anticipatory or partially confabulated.  
**Fix (1–2 sentences):** Replace this with the exact title, author list, and arXiv/journal reference of the published ACT DR6 birefringence paper, and verify that the quoted \(\beta\) value and uncertainty match the published numbers; if they are forecast or internal, label them clearly as such instead of as a published measurement.

---

## Finding 5 — PAPER-ECTORSIONDESI2025 (MAJOR)

The citation `ECTorsionDESI2025` to “Liu et al. constrained an EC torsion model using DESI DR2 + Pantheon+ + DES‑SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6)” does not correspond to any identifiable arXiv or journal paper combining exactly those datasets and that model. [1][2]  
**Issue:** The detailed dataset combination and quoted ΔAIC range look like they are drawn from an internal or hypothetical analysis; without a matching public paper, this reads as a fully fabricated external citation.  
**Fix (1–2 sentences):** Either (a) remove the external “Liu et al.” claim and present this as your own analysis with full methodological detail, or (b) replace the current placeholder with the real published EC‑torsion paper (correct authors, title, journal/arXiv ID) whose results you are summarizing, adjusting numbers to match that source.

---

## Finding 6 — PAPER-FUJITA2021 (nit)

The ALP spectator model is attributed to “Fujita et al. 2021” but there are multiple Fujita ALP‑cosmology papers around that time, and the manuscript does not give an arXiv ID or journal reference to disambiguate which specific model/parameterization is being reused. [1][2]  
**Issue:** While this likely refers to an actual Fujita ALP‑birefringence paper, the current citation is under‑specified, making it hard for readers to confirm that the same coupling normalization and potential are being adopted.  
**Fix (1–2 sentences):** Add the precise title, arXiv ID, and journal venue for the intended Fujita et al. paper and, if the ALP Lagrangian or parameter ranges are taken directly, quote the equation number or section where they are defined.
