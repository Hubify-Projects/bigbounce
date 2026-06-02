# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round4
**Wall time**: 20.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28152, completion=1993, total=30145, search_context_size=low, cost={'input_tokens_cost': 0.08446, 'output_tokens_cost': 0.0299, 'request_cost': 0.006, 'total_cost': 0.12035}

---

## PAPER-B1 (MAJOR) – Liu et al. “ECTorsionDESI2025” citation

**Location:** §Verification, “Independent cross-validation” paragraph; also preamble comments (multiple mentions of `ECTorsionDESI2025` / “EPJC 2025, arXiv 2507.04265”).

**Issue:** The paper repeatedly cites an EC torsion analysis “Liu et al. ECTorsionDESI2025” described as an EPJC 2025 paper with arXiv:2507.04265 using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018 and reporting ΔAIC ≈ −5.7 to −6.6 in favor of torsion. There is currently no such arXiv entry or journal paper matching this description; “2507.04265” is in the future and unassigned, and no Liu+Li+Xu+Biesiada+Wang EC‑torsion DESI DR2 paper is findable via arXiv, ADS, or publisher searches. The metadata and claims look internally consistent but externally unverifiable, and the text asserts them as if published.

**Fix:** Reframe this as an **unpublished / in-prep** analysis if it exists (and remove arXiv/journal identifiers), or remove the paragraph entirely until a real, citable paper exists. At minimum, delete the arXiv ID, journal claim, and ΔAIC numbers, and replace with a generic statement such as “independent EC torsion fits to DESI DR2+SN+CMB are in preparation, with preliminary trends broadly consistent with our proxy MCMC” or simply drop the cross-validation claim.


## PAPER-B2 (MAJOR) – Eskilt & Komatsu dataset wording vs actual paper

**Location:** Abstract; §Birefringence check “Headline observational constraint”; §Data methods (NaMaster section) via context.

**Issue:** The paper now describes Eskilt & Komatsu 2022 (PRD 106, 063503, arXiv:2205.13962) as a “joint WMAP+Planck value” and as “the joint WMAP9 + Planck 2018 (PR3) analysis.” According to the actual paper, Eskilt & Komatsu analyze **Planck 2018 polarization data only**, with WMAP entering only in a comparison/consistency role, not as a joint combined estimator of β; there is no single quoted “WMAP+Planck” combined β with 0.342° ± 0.094° in that paper. The 0.342° ± 0.094° value is consistent with Planck‑only fits in the literature, but calling it a “joint WMAP+Planck” headline measurement overstates WMAP’s role and misdescribes the dataset.

**Fix:** Replace all “joint WMAP+Planck value / WMAP9 + Planck 2018 (PR3) analysis” language with **“Planck 2018 polarization value (with WMAP used only for cross-checks)”** and check that the numerical β and σ match a specific result quoted in the paper. If the 0.342° ± 0.094° figure is taken from a particular table/fit in Eskilt & Komatsu, cite it explicitly as “Planck 2018 PR3” rather than a WMAP+Planck combination.


## PAPER-M1 (MAJOR) – Diego Palazuelos et al. ACT DR6 2025 reference

**Location:** Preamble comments (multiple mentions of “DiegoPalazuelos2025 ACT DR6 birefringence; arXiv 2509.13654”); §Data methods (ACT DR6 β=0.215° ± 0.074°); §Birefringence check summary text.

**Issue:** The manuscript treats “DiegoPalazuelos+Komatsu 2025 (ACT DR6, arXiv 2509.13654)” as an existing reference. As of now, there is a real **ACT DR4/DR6 birefringence** paper (Diego-Palazuelos et al., PRL 128, 091302, arXiv:2201.07682) but no ACT DR6 birefringence paper with a 2025 date or arXiv:2509.13654. The metadata appear to fuse the real 2022 PRL (Planck+ACT) with a speculative future DR6 paper and arXiv ID.

**Fix:** Replace any “2025 / arXiv 2509.13654 / ACT DR6” bib entry with the actually published **Diego-Palazuelos et al. 2022 PRL 128, 091302, arXiv:2201.07682**, and ensure the β=0.215° ± 0.074° value and “ACT DR6” wording are aligned with what that paper really reports (e.g., Planck+ACT or ACT-specific subsets). If a pure “DR6‑only 2025” paper is intended but not yet public, relabel it clearly as “in preparation” and remove arXiv/journal tags.


## PAPER-M2 (MAJOR) – ACT DR6 value and “published Planck/ACT DR6 2.4–2.9σ” phrasing

**Location:** Abstract (NaMaster paragraph); §Data methods “Birefringence measurements are adopted…”; §Birefringence check “Summary-likelihood combination”.

**Issue:** The paper states that “the primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ” and uses β = 0.215° ± 0.074° as “ACT DR6.” Review of Diego-Palazuelos et al. 2022 (arXiv:2201.07682) shows Planck+ACT analyses with specific β and σ values, but there is no separate, later “ACT DR6” paper with exactly β = 0.215° ± 0.074° and a 2.4–2.9σ headline labelled as such. The manuscript appears to have rebranded Planck+ACT (or ACT‑inclusive) results as “ACT DR6” and then combined them with another β for the 3.9σ auxiliary result; the exact mapping of numbers to specific published analyses is not transparent and risks mismatching dataset labels to particular fits.

**Fix:** For each β and σ, explicitly tie it to a **specific published result** (e.g., “Planck+ACT joint fit from Diego-Palazuelos et al. 2022, Table X, giving β = …”), and drop or correct the “ACT DR6” label if it is not the paper’s term. If no published analysis uses the exact 0.215° ± 0.074° as an ACT‑only DR6 value, relabel it accurately (e.g., as a Planck+ACT subset) or remove the “ACT DR6” language and 2.4–2.9σ phrase until a precise, checkable mapping to the literature is demonstrated in the text.


## PAPER-m1 (minor) – LiteBIRD σ(β) forecast value and units

**Location:** §Birefringence check “LiteBIRD forecast.”

**Issue:** The paper quotes “LiteBIRD is projected to achieve σ(β) ≈ 0.03°” without specifying which collaboration forecast or configuration this number is taken from. Current LiteBIRD forecasts often quote σ(β) in radians (e.g., ≲ 5×10⁻⁴ rad) and sometimes in degrees, but there is variation between documents and assumptions (channels, delensing, multipole cuts). Without a direct citation, the 0.03° value is hard to audit.

**Fix:** Add an explicit citation to the **specific LiteBIRD forecast paper or memo** used, and confirm the quoted σ(β) value and units match that source; if the source uses radians, present the value in radians with the degree conversion parenthetically.


## PAPER-m2 (minor) – ALP MCMC dataset description vs what is actually run

**Location:** §Birefringence check “MCMC parameter estimation.”

**Issue:** The text claims that the internal ALP MCMC “model-independent fit” uses “Planck PR4 + ACT DR6 EB-spectrum likelihoods” with three configurations (C_{aγ}=4,8,12). Given the earlier issues around ACT DR6 and the absence of a clearly documented public Planck PR4 birefringence likelihood, this description reads as if a fully public, standard likelihood stack exists when in practice this may be an internal or custom construction. Without clarification, readers could misunderstand the provenance of β_free = 0.344° ± 0.096°.

**Fix:** Clarify that these ALP MCMC runs use a **custom EB-spectrum likelihood stack** constructed from public Planck / ACT data products (if that is the case), and state explicitly that this likelihood is internal and not an official “Planck PR4 + ACT DR6” release. Alternatively, if only Planck PR3 or the published Planck+ACT spectra are used, adjust the wording to match the actual datasets.
