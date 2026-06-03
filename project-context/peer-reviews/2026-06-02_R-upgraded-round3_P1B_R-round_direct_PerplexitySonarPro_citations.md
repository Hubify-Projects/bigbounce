# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 18.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30314, completion=1256, total=31570, search_context_size=low, cost={'input_tokens_cost': 0.09094, 'output_tokens_cost': 0.01884, 'request_cost': 0.006, 'total_cost': 0.11578}

---

## PAPER-PER-B1 — Mislabeling of Eskilt & Komatsu 2022 dataset (BLOCKER)

**Location:** Abstract, line with “published joint WMAP+Planck value … (3.6σ)” and §VI “Headline observational constraint” paragraph.  

**Issue:** Eskilt & Komatsu 2022 (PRD 106, 063503, arXiv:2205.13962) analyze **Planck PR4 NPIPE + WMAP9**, not “Planck 2018” PR3; the text is internally inconsistent (abstract says “joint WMAP+Planck” without specifying PR4, §VI correctly says “Planck PR4/NPIPE”, elsewhere still implies “Planck 2018”). The history comments document a PR3/PR4 flip-flop; current wording must be checked against the actual paper and its public repo.  

**Fix:** Standardize all mentions of the Eskilt & Komatsu dataset to “joint WMAP9 + Planck PR4/NPIPE analysis” and scrub any residual “Planck 2018 (PR3)” language or ambiguous “Planck 2018” wording for this reference.

---

## PAPER-PER-B2 — Liu et al. “ECTorsionDESI2025” bibliographic metadata (MAJOR)

**Location:** §III, paragraph “Independent cross-validation” citing Liu et al. \cite{ECTorsionDESI2025}.  

**Issue:** The text claims an EPJC 2025 EC-torsion paper with DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018 and ΔAIC ≈ −5.7 to −6.6. Web search cannot currently verify any such 2025 EPJC paper, arXiv:2507.04265, or that exact title / dataset combination; the comments assert it exists but give no verifiable metadata (title, journal, authors) in the LaTeX body. This is a live risk of fused/confabulated metadata.  

**Fix:** In the main text, replace the strong claim with a provisional attribution: explicitly mark the Liu et al. result as “in preparation / private communication” or similar until a citable arXiv ID, title, and venue can be independently verified; remove or soften numerical AIC statements that cannot be checked against a public paper.

---

## PAPER-PER-M1 — Diego Palazuelos & Komatsu 2025 ACT DR6 reference (MAJOR)

**Location:** Multiple places citing \cite{DiegoPalazuelos2025} as “ACT DR6” birefringence measurement.  

**Issue:** No 2025 ACT DR6 cosmic birefringence paper by Diego-Palazuelos & Komatsu (or similar author list) with the described properties is yet discoverable via arXiv or journal search. The draft refers to arXiv:2509.13654 in comments, but that ID and year are in the future relative to all currently-indexed archives and may be placeholder/confabulated.  

**Fix:** Clearly label this as an anticipated / in-prep ACT DR6 result rather than a published paper, and remove precise numerical claims (e.g., β = 0.215° ± 0.074° tagged to that future bibkey) unless they can be tied to an existing arXiv or journal entry with correct title and authors.

---

## PAPER-PER-M2 — Fujita et al. 2021 wording vs subject (minor)

**Location:** §VI “Note.” sentence: “The model class was previously studied by Fujita et al. [Fujita2021].”  

**Issue:** Fujita et al. PRD 103, 043509 (arXiv:2011.11894) indeed studies axionlike particles and cosmic birefringence, but their focus is broader (DE interpretations, constraints) than just this specific spectator-ALP configuration. The phrase “the model class was previously studied” overstates direct identity of setups.  

**Fix:** Rephrase to “A closely related ALP–birefringence model was studied by Fujita et al.” or similar, avoiding the implication that their paper analyzed exactly the same parameterization used here.

---

## PAPER-PER-m1 — Eskilt & Komatsu “3.6σ joint WMAP+Planck” numerical quote (minor)

**Location:** Abstract and §VI “Headline observational constraint” (β = 0.342° ± 0.094° (3.6σ)).  

**Issue:** Eskilt & Komatsu 2022 report β = 0.342° ± 0.094°; the formal significance is ≈3.6σ only if Gaussian and centered exactly as quoted. While consistent, the paper should make clear the σ conversion is directly from their quoted mean and 1σ error rather than an independently computed significance from another combination.  

**Fix:** Add a brief parenthetical or footnote stating that “3.6σ” is simply β/σ_β from Eskilt & Komatsu’s 0.342° ± 0.094° result, not an independently recomputed detection metric.

---

## PAPER-PER-n1 — Use of PR4 “Planck 2018 NPIPE” wording (nit)

**Location:** §IV “Independent verification” and §V dataset descriptions.  

**Issue:** The text mixes “Planck 2018 NPIPE” and “Planck PR4 NPIPE” terminology; technically PR4 NPIPE is a later reprocessing distinct from the 2018 PR3 likelihoods, and “Planck 2018 NPIPE” is slightly imprecise/potentially confusing.  

**Fix:** Standardize to “Planck PR4 NPIPE” for NPIPE-based analyses and reserve “Planck 2018” for PR3-only contexts, to avoid conflating the official 2018 release with the later PR4 reprocessing.
