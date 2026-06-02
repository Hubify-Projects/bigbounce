# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 9.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36004, completion=1156, total=37160, search_context_size=low, cost={'input_tokens_cost': 0.10801, 'output_tokens_cost': 0.01734, 'request_cost': 0.006, 'total_cost': 0.13135}

---

## PAPER-PER-B1 — **BLOCKER**
**Section:** Bibliography / Section `Tempel+2014 FoF cross-validation`

**Issue:** `Tempel2014` is misidentified. The bibitem title `Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation` is **not** the canonical Tempel+2014 environment-catalog paper this manuscript is using for FoF environment classes. The text claims a 4-class environment mapping and DR10 group catalog cross-validation, which is tied to the catalog paper that actually reports the SDSS DR10 group/cluster catalog, not just the mass-estimation companion.

**Fix:** Replace the citation with the correct Tempel et al. catalog paper and align the title, journal, and arXiv ID to the exact DR10 FoF environment catalog used in the analysis. If the current bibitem is meant to be a companion paper, say so explicitly and do not use it as the source for the class-defining catalog.

## PAPER-PER-B2 — **MAJOR**
**Section:** `Concurrent-literature DR1/EDR cosmic-web cross-validation`

**Issue:** `TWebDESI2026` is internally inconsistent with its description. The paper text says the work was “released in 2026 April,” is “currently in submission,” and also cites it as a contemporaneous DR1 cosmic-web analysis with a specific arXiv ID; this is a metadata fusion that needs direct verification against arXiv/ADS. The bibitem author/title pair may be real, but the status claims are not stable and read like stitched metadata from multiple states.

**Fix:** State one status only: either submitted preprint or published/accepted paper. Verify the arXiv record and ADS entry, then make the prose match the source exactly. If the paper is only a preprint, do not imply release timing or peer-review status beyond what the arXiv/ADS record states.

## PAPER-PER-B3 — **MAJOR**
**Section:** `ASTRA EDR per-object cross-validation`

**Issue:** `ASTRADESI2026` is cited as a DESI EDR probabilistic environment catalog with a Zenodo DOI, but the manuscript also asserts exact overlap counts, tracer coverage, and operational details as if they were all documented in the source paper. That is a citation-chain problem: the text is attributing highly specific downstream usage claims to the ASTRA paper without demonstrating that the paper itself states those exact sample sizes and joins.

**Fix:** Separate what ASTRA actually reports from what *this work* computed. Keep only source-backed statements in the ASTRA citation sentence, and attribute the overlap counts, TARGETID join, and CW-fraction statistics to your own analysis pipeline unless the ASTRA paper explicitly states them.

## PAPER-PER-B4 — **MAJOR**
**Section:** Appendix `Toy EFT mapping of the environmental bound`

**Issue:** The appendix now admits the operator is a toy parametrization “introduced in this work,” but the main text still uses it to quote an “order-of-magnitude bound” in a way that can be mistaken for a derived physics constraint. The manuscript mixes invented operator language with cited parity-violation literature in a load-bearing way, which is exactly the kind of citation-impossible attribution the round is meant to catch.

**Fix:** Demote the entire EFT mapping to a purely illustrative sidebar with no numeric constraint language in the main narrative. If you keep it, label every formula as author-constructed, not literature-derived, and avoid phrasing that implies the cited papers support that specific operator form.

## PAPER-PER-B5 — **minor**
**Section:** Abstract / Results / Section `Cross-survey P4-monopole-residual analysis`

**Issue:** The manuscript repeatedly shifts between three different baselines: parity \(0.5\), Paper IV’s global \(f_{\rm CW}=0.4974\), and a derived “P5 monopole” \(f_{\rm CW}^{\rm P5}=0.4972\). This is not a citation error, but it is a forensic clarity problem: the baseline used for each claim is easy to confuse and the paper sometimes treats the P4 monopole as if it were a direct predictor for every subsample without clearly separating inherited bias from new estimation.

**Fix:** Define one baseline hierarchy early and use consistent notation throughout: raw parity null, inherited Paper IV monopole, and any re-estimated subsample monopole. Add one sentence where the paper first introduces \(f_{\rm CW}^{\rm P5}\) stating explicitly whether it is an analysis estimate or a cited external fact.

## PAPER-PER-B6 — **nit**
**Section:** `DESIVAST per-galaxy cross-match` / `Three-algorithm DESIVAST robustness`

**Issue:** The manuscript uses “DESIVAST,” “VoidFinder,” “V2-REVOLVER,” “V2-VIDE,” “maximal voids,” and “catalog-native V2 membership” as if all are directly comparable definitions, but they are not. The text slides between sphere-based hole membership, effective void membership, and catalog-native zone membership without always marking which statistic is being reported, which makes the evidence chain hard to audit.

**Fix:** Add a one-line label before each DESIVAST subsection stating the exact membership definition in use. Keep sphere-approximation results, catalog-native results, and maximal-void HEALPix stratification completely separate.
