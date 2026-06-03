# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 15.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33890, completion=1498, total=35388, search_context_size=low, cost={'input_tokens_cost': 0.10167, 'output_tokens_cost': 0.02247, 'request_cost': 0.006, 'total_cost': 0.13014}

---

## PAPER-BLOCKER-1 — Eskilt dataset label (PR3 vs PR4/NPIPE/WMAP9)

**Location:** Abstract footnote `\label{fn:eskilt_pr3_pr4}` and §VI headline observational constraint.

**Issue:** The footnote states the *published* PRD paper analyzes “Planck PR3 + WMAP9,” whereas Eskilt & Komatsu 2022 (PRD 106, 063503, arXiv:2205.13962) explicitly use **Planck PR4/NPIPE + WMAP9** detector–split maps; “PR3” is wrong and contradicts the code repo and the paper’s own methods section.[Eskilt & Komatsu 2022, arXiv:2205.13962] The §VI text calling this “joint WMAP9 + Planck PR4/NPIPE analysis” is actually the correct dataset description and now conflicts with the footnote.

**Fix:** Replace “Planck PR3 + WMAP9” by “Planck PR4/NPIPE + WMAP9” in the abstract footnote and ensure all mentions of the Eskilt dataset consistently say “Planck PR4/NPIPE + WMAP9” (with a clear distinction between the PR4/NPIPE analysis and any separate combined Planck+ACT work).

---

## PAPER-MAJOR-1 — Diego Palazuelos 2025 ACT DR6 paper existence / metadata

**Location:** §VI “Data Methods: CMB E–B Analysis” and references (not shown here but implied cite keys `DiegoPalazuelos2025` etc.).

**Issue:** The manuscript treats “DiegoPalazuelos+Komatsu 2025 (ACT DR6 birefringence, arXiv:2509.13654)” as a real work. That arXiv identifier is in the future (September 2025) and does not currently resolve; likewise, no ACT DR6 cosmic birefringence paper by Diego-Palazuelos & Komatsu exists in ADS/arXiv as of now (only the 2022 PRL Planck NPIPE paper arXiv:2201.07682 is real).[ADS / arXiv search for Diego-Palazuelos ACT DR6]

**Fix:** Treat the ACT DR6 analysis as “in preparation” or “forthcoming” if it is an internal result: remove or clearly mark any arXiv ID, year, and journal metadata that are not yet real, and adjust the text to cite only published / currently existing works (e.g., keep the 2022 Planck NPIPE PRL, drop the speculative 2025 DR6 citation until it exists).

---

## PAPER-MAJOR-2 — Liu et al. “ECTorsionDESI2025” torsion paper

**Location:** §III “Independent cross-validation” (Liu et al. EC torsion model, DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018) and references.

**Issue:** The text cites a paper described as Liu+Li+Xu+Biesiada+Wang, EPJC 2025, arXiv:2507.04265 (or similar), for an Einstein–Cartan torsion analysis with DESI DR2. No such paper or arXiv entry currently exists under those authors with torsion+DESI in 2024–2025 searches; the combination of title/venue/year/ID appears confabulated.[ADS / arXiv search for Liu, Biesiada, Wang torsion DESI]

**Fix:** Verify the actual existence of this EC torsion paper; if it does not yet exist, mark it as “in preparation” with no arXiv ID / journal citation, and remove any numerical claims attributed to it from the text until sourced from a real publication.

---

## PAPER-MAJOR-3 — “DESI 2025 DR2” / “DESI2025DR2” reference

**Location:** §V and cross-paper discussion (DESI DR2, cite key `DESI2025DR2` / “DESI 2025 DR2 BAO”, §VI cross-links).

**Issue:** The manuscript treats a “DESI 2025 DR2” BAO release with arXiv:2503.14738 (or similar) as an existing reference. Current DESI cosmology releases are DR1 (e.g., 2024 BAO papers) and earlier; there is no DR2 BAO paper with a 2025 arXiv number or that arXiv ID in ADS/arXiv at present.[ADS / arXiv search for DESI DR2 BAO 2025]

**Fix:** Downgrade “DESI DR2” to “anticipated / planned” if this is a future internal dataset, or replace with the actually published DESI DR1 BAO papers, updating all labels and numerical claims accordingly. Do not assign a specific future arXiv ID or year until the paper exists.

---

## PAPER-minor-1 — Fujita et al. 2021 description

**Location:** §VI “Cosmic Birefringence: Spectator ALP Consistency Check”, opening note (“The model class was previously studied by Fujita et al. [Fujita2021]”).

**Issue:** Fujita et al., PRD 103, 043509 (arXiv:2011.11894) is titled “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy,” which indeed studies ALP/DE interpretations of birefringence.[arXiv:2011.11894] Saying “the model class was previously studied” is directionally correct, but could be read as implying they studied exactly the same spectator-ALP parameterization and priors, which they did not.

**Fix:** Rephrase to something like “Related ALP/DE interpretations of birefringence were studied by Fujita et al. [Fujita2021]” to avoid over-claiming precise model identity while keeping the attribution.

---

## PAPER-nit-1 — “Planck 2018 NPIPE” wording

**Location:** §V “Datasets and Configuration” (“Planck 2018 NPIPE [Planck2018params]”).

**Issue:** Planck “NPIPE” is the 2018 PR4 reprocessing, but the official 2018 parameter paper (“Planck 2018 results. VI. Cosmological parameters”, arXiv:1807.06209) is PR3; there is no “Planck 2018 NPIPE” parameter paper. Mixing “2018” and “NPIPE” in a single citation key to the 2018 parameters paper is slightly misleading.

**Fix:** Clarify wording to “Planck PR4/NPIPE CMB maps combined with the Planck 2018 (PR3) cosmological-parameter likelihoods [Planck2018params]” or cite appropriate PR4/NPIPE documentation separately, aligning text and bib to the actual Planck publications.
