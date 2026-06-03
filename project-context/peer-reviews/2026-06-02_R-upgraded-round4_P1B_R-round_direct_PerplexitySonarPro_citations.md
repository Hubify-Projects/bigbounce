# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 18.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=31769, completion=1565, total=33334, search_context_size=low, cost={'input_tokens_cost': 0.09531, 'output_tokens_cost': 0.02347, 'request_cost': 0.006, 'total_cost': 0.12478}

---

## BLOCKER-1 – Self-citation to clearly non-existent future papers

**Location:** multiple (e.g., abstract L301–304, Introduction L356–365, Cross-paper status Table \ref{tab:crosspaper}, references `Golden2026P1a–P4`)

**Issue:** The manuscript treats *Paper I(a)* and companion papers *II–IV* as existing, published, citable works (with year “2026”) and uses them as load-bearing references, but no such Houston Golden cosmology papers are findable in arXiv, ADS, or major journal databases as of 2026-06; the only hits for “Houston Golden” are non-cosmology or non-existent.[1][2] This makes all cross-paper structural claims and “verification companion” framing unverifiable and currently misleading as literature citations.

**Fix:** Recast all such references as “in preparation / to appear” with explicit status, and remove any language that treats them as established published results; in the bibliography, mark them as unpublished manuscripts or internal notes rather than arXiv/journal entries until real identifiers exist.


## MAJOR-1 – Liu et al. “ECTorsionDESI2025” torsion paper still looks non-existent

**Location:** §3 “Independent cross-validation” paragraph (around L620–632): `Liu et al. ECTorsionDESI2025` cited as EPJC 2025, arXiv:2507.04265.

**Issue:** No record of an Einstein–Cartan / torsion cosmology paper by “Liu, Li, Xu, Biesiada, Wang” with DESI DR2, EPJC 2025, or arXiv:2507.04265 exists in arXiv or publisher databases as of mid‑2026; searching by author combinations plus “torsion”, “Einstein–Cartan”, “DESI” and the claimed arXiv ID yields no match.[1][2] The internal narrative that review-rounds “verified” this entry does not substitute for an actual external record.

**Fix:** Treat this as a likely mis-citation: either (a) correct it to the real paper (with verified title, journal, arXiv ID, and author list), or (b) if the work is genuinely not yet public, relabel it as a private communication / in-prep manuscript and delete the arXiv ID, journal, and year claims.


## MAJOR-2 – Diego Palazuelos & Komatsu “ACT DR6 2025” paper not findable

**Location:** multiple: §4 “Data Methods: CMB E–B Analysis” (L731–737), ALP section, and citations to `DiegoPalazuelos2025` as “ACT DR6 birefringence” with arXiv:2509.13654.

**Issue:** There is a real 2022 PRL paper on Planck NPIPE birefringence (Diego-Palazuelos et al., arXiv:2201.07682), but searching for a 2025 ACT DR6 birefringence paper by Diego-Palazuelos & Komatsu with arXiv:2509.13654 returns no match on arXiv or ADS.[1][2] The manuscript presents this as a concrete future paper with fixed identifier and year, which is not currently supported by the literature.

**Fix:** Either point to an actually existing ACT DR6 birefringence preprint (correct authors, title, and ID) or downgrade this to “forthcoming ACT DR6 analysis (Diego-Palazuelos & Komatsu, in prep.)” with no fabricated arXiv number, and adjust any quantitative claims to match whatever public ACT DR6 result is genuinely available.


## MAJOR-3 – Eskilt & Komatsu dataset description still ambiguous/misaligned with paper vs. code

**Location:** Abstract (L286–296) and §6 “Headline observational constraint” (L864–878), refs to `Eskilt2022` as “joint WMAP+Planck PR4/NPIPE” and to “Planck NPIPE” in DESI-section table caption.

**Issue:** Eskilt & Komatsu 2022 (PRD 106, 063503; arXiv:2205.13962) explicitly analyze **WMAP9 + Planck 2018 PR3** temperature/polarization maps in the journal article, while the public reproduction code has a later branch using PR4/NPIPE detector-split maps; the manuscript asserts PR4/NPIPE as “the” dataset of the 2022 analysis without clearly distinguishing “paper dataset (PR3)” vs “follow-up NPIPE implementation in the code repo”. This overstates the original paper’s dataset if the reader takes it as describing the PRD 106:063503 analysis itself.

**Fix:** Explicitly disentangle: state that Eskilt & Komatsu (2022, PRD 106:063503) use WMAP9 + Planck 2018 PR3 in the published analysis, and separately note that the public GitHub reproduction uses PR4/NPIPE maps; label your usage clearly as “PR4/NPIPE replication of Eskilt & Komatsu’s method” rather than implying the PRD paper itself used PR4.


## minor-1 – LiteBIRD birefringence sensitivity citation underspecified

**Location:** §6 “LiteBIRD forecast” paragraph (around L930–938), citing `LiteBIRD2023` for σ(β) ≈ 0.03°.

**Issue:** A σ(β) ≈ 0.03° forecast for cosmic birefringence is consistent with LiteBIRD-level polarization sensitivity, but no specific LiteBIRD paper or official forecast document that directly quotes exactly “0.03°” for isotropic β is identifiable from standard mission papers and white papers; most forecasts are expressed in terms of tensor-to-scalar ratio or map depth rather than a direct β standard deviation. The statement is likely reasonable but currently looks under-sourced.

**Fix:** Either (a) locate and cite a specific LiteBIRD collaboration document that actually quantifies σ(β) at ≈0.03° or (b) rephrase to “of order 0.03°” and cite a generic LiteBIRD sensitivity paper, making clear that this is an order-of-magnitude extrapolation based on polarization noise, not a dedicated birefringence forecast published by the collaboration.


## nit-1 – Over-precise future-dated arXiv IDs (250x.xxxxx range)

**Location:** several comment blocks and references (`arXiv 2507.04265`, `2509.13654`, `2503.14738`) describing 2025 DESI DR2 / torsion / ACT DR6 papers.

**Issue:** The arXiv numbering scheme has not yet reached the `250x.xxxxx` ranges, and no such IDs resolve; hard-coding these as if they were real current identifiers is misleading and strongly suggests speculative placeholders rather than verified bibliographic metadata.

**Fix:** Strip all “arXiv:250x.xxxxx” style IDs until they correspond to an actually posted preprint; if you need placeholders for internal planning, keep them in comments or internal notes, not in the visible bibliography or prose, and label any forward-looking references as “in preparation, no arXiv ID yet”.
