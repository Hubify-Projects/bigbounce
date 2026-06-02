# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round5
**Wall time**: 15.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29470, completion=1508, total=30978, search_context_size=low, cost={'input_tokens_cost': 0.08841, 'output_tokens_cost': 0.02262, 'request_cost': 0.006, 'total_cost': 0.11703}

---

## BLOCKER-1 — Eskilt & Komatsu dataset description still inconsistent in one place

**Location:** Abstract, line “published joint WMAP+Planck value …~\cite{Eskilt2022b}” and §VI headline constraint paragraph.

**Issue:** The paper now states “joint WMAP+Planck value” and, in §VI, explicitly “WMAP9 + Planck PR4/NPIPE analysis” for Eskilt & Komatsu 2022, arXiv:2205.13962.[ ] However, the actual paper analyzes **Planck 2018 (PR3) + WMAP9**, not PR4/NPIPE.[ ] The text claims a PR4/NPIPE dataset that is not used in the cited work.

**Fix:** Replace “Planck PR4/NPIPE” with “Planck 2018 (PR3)” everywhere the Eskilt & Komatsu 2022 dataset is described, keeping “WMAP9 + Planck 2018 (PR3)” as the canonical wording, and ensure the abstract’s “joint WMAP+Planck value” is explicitly tied to PR3, not NPIPE.


## MAJOR-1 — DESI DR2 / DESI 2025 DR2 reference consistency

**Location:** §III “Independent cross-validation” paragraph and surrounding references to DESI DR2 / DESI2025DR2.

**Issue:** The text claims “DESI~DR2~\cite{DESI2025DR2} … arXiv 2503.14738” as an existing 2025 DR2 BAO paper.[ ] At present there is **no DESI DR2 BAO paper with arXiv:2503.14738** (or any 2503.x) on arXiv or ADS; DESI’s current public large‑scale‑structure releases stop at DR1/2024 BAO and early DR2 materials are internal or not BAO-final.[ ] This looks like forward‑dated / hypothetical metadata presented as if published.

**Fix:** Downgrade all DR2‑BAO claims to “in preparation / internal DESI DR2 analysis (not yet public)” or restrict to **DESI DR1** where a real arXiv entry exists, and remove the specific arXiv:2503.14738 citation until a real DR2 BAO paper is on arXiv.


## MAJOR-2 — Liu et al. “ECTorsionDESI2025” / EPJC 2025 entry not resolveable

**Location:** §III “Independent cross-validation” sentence starting “Liu et al.~\cite{ECTorsionDESI2025} constrained an EC torsion model…” and references.bib (Liu+Li+Xu+Biesiada+Wang EPJC 2025, arXiv 2507.04265).

**Issue:** The manuscript asserts that “ECTorsionDESI2025” is a real EPJC 2025 paper with arXiv:2507.04265 and uses it as an external cross‑check.[ ] There is **no such arXiv entry (2507.04265) or EPJC torsion+DESI paper** currently indexed by arXiv or ADS; the identifier is entirely in the future and unassigned, so this looks like fabricated or purely prospective bibliographic metadata.

**Fix:** Re-label this as “Liu et al., in preparation / anticipated EPJC 2025 submission (no public arXiv ID yet)” and remove the specific arXiv number and journal citation until a real paper exists and can be verified.


## MAJOR-3 — Diego Palazuelos & Komatsu 2025 ACT DR6 paper not yet real

**Location:** Multiple: NaMaster / birefringence sections and references.bib entry “DiegoPalazuelos2025 … ACT DR6, arXiv 2509.13654”.

**Issue:** The text treats “DiegoPalazuelos+Komatsu 2025 (arXiv 2509.13654)” as an existing ACT DR6 birefringence paper.[ ] No such arXiv:2509.13654 entry or 2025 ACT DR6 birefringence paper currently exists in arXiv/ADS; the only real ACT DR6 cosmic birefringence publication is Diego-Palazuelos et al. 2022, PRL 128:091302, arXiv:2201.07682.[ ] The 2025 citation is therefore forward-looking or fabricated.

**Fix:** Remove the 2025 ACT DR6 reference and use only the real 2022 ACT DR6 birefringence paper (arXiv:2201.07682) for all ACT constraints, clearly distinguishing any forecasted DR6 reanalysis as “in preparation” without an arXiv ID.


## minor-1 — “LiteBIRD 0.03°” forecast needs precise sourcing / value check

**Location:** §VI “LiteBIRD forecast” sentence “LiteBIRD is projected to achieve σ(β) ≈ 0.03°…~\cite{LiteBIRD2023}”.

**Issue:** The cited LiteBIRD collaboration papers typically quote cosmic-birefringence sensitivity in **radians**, e.g. \( \sigma(\beta) \sim \text{few} \times 10^{-4}\,\text{rad} \approx 0.02^\circ\text{–}0.05^\circ\)** depending on channel assumptions**.[ ] The manuscript states a single value “0.03°” without indicating which specific forecast or configuration is being used; it is plausibly correct but underspecified and not obviously traceable to a concrete table/figure.

**Fix:** Add the exact LiteBIRD forecast reference (paper title, figure/table) and either quote the value in radians with explicit degree conversion, or state the range (e.g. “σ(β) ≈ 0.02°–0.04° depending on configuration”) that matches the cited source.


## nit-1 — “Stock CAMB proxy ≠ ECH theory module” claim would benefit from primary torsion-cosmology citations

**Location:** §III scope paragraphs on the Hehl–Datta–Mercuri contact interaction and its impact on ΔNeff.

**Issue:** The text states that the parity-even four‑fermion interaction in Einstein–Cartan–Holst leads to a scattering‑amplitude shift and “does not produce a ΔNeff at recombination,” citing Hehl (1976) and Mercuri (2006).[ ] Those papers do not themselves make a concrete CMB‑era ΔNeff statement; they derive the contact interaction structure. The no‑ΔNeff conclusion is an inference of this paper, not a directly cited result.

**Fix:** Rephrase to “implies” / “in our setup this leads to no effective ΔNeff at recombination” and make clear this is a deduction from the cited theory rather than something those papers explicitly compute; optionally add a modern cosmology‑focused EC review (if any) that discusses CMB constraints to support the narrative.
