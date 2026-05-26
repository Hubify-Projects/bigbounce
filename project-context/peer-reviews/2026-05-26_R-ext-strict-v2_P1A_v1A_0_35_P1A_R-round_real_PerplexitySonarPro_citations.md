# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict-v2_P1A_v1A_0_35
**Wall time**: 20.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30091, completion=1602, total=31693

---

## PAPER-PER-B1 — Self-citation “Golden2026P1b” / “Paper I(b)”

**Section:** Abstract; Introduction (Companion paper paragraph); multiple later refs.

**Issue:** The paper repeatedly cites a companion “Paper I(b)” with key results (MCMC, NaMaster, ALP fits) under the citation key `Golden2026P1b`, but no such paper exists on arXiv, ADS, or journal databases as of now; the title and arXiv ID are never specified and appear to be internal placeholders rather than externally verifiable literature. [1]

**Fix (1–2 sentences):** Clearly mark “Paper I(b)” / `Golden2026P1b` as an in-preparation internal companion with no public identifier yet, and remove it from the main bibliography list of external references until it is posted. Once it is on arXiv or accepted in a journal, update all instances with the real authors, title, venue, and arXiv ID and ensure the bib entry matches exactly.


## PAPER-PER-M1 — Cai & Brandenberger matter-bounce citation

**Section:** Abstract paragraph near “Specifically: (i) fnl = -35/8 … property of the matter-bounce class ”.

**Issue:** The text attributes the matter-bounce non-Gaussianity result \(\fnl=-35/8\) to a single citation “Cai:2009fn” and treats it as a precise canonical value, but the arXiv record for “Non-Gaussianity in a Matter Bounce” (arXiv:0903.0631, Brandenberger et al.) does not have a Cai first author nor the cited key; actual author list and citation key differ, indicating at least a metadata mismatch between the in-text key and the real arXiv entry. [2]

**Fix (1–2 sentences):** Correct the reference to the actual paper “Non-Gaussianity in a Matter Bounce,” arXiv:0903.0631, with the proper author list and citation key (e.g., `Brandenberger2009MatterBounce`), and ensure that any derived value like \(\fnl=-35/8\) is explicitly stated as coming from that paper (or from a correctly identified Cai-led follow-up, if that is what is intended). If a distinct Cai et al. paper is meant, replace the arXiv key and metadata accordingly so that ID, authors, and title all match a real arXiv entry.


## PAPER-PER-m1 — Planck parameter citation key vs. actual Planck papers

**Section:** Introduction, first paragraph: “Planck2018params”.

**Issue:** The citation key `Planck2018params` is used for “Planck 2018” cosmological parameters, but the only Planck paper fetched (Planck 2015 Isotropy and statistics, arXiv:1506.07135) does not match that key or topic; without a concrete arXiv ID given in the manuscript, there is a risk that the bibliography will incorrectly point `Planck2018params` to a mismatched Planck paper (e.g., 2015 isotropy paper instead of the 2018 cosmological parameters release). [1]

**Fix (1–2 sentences):** Ensure that `Planck2018params` is mapped in the .bib file to the actual 2018 cosmological parameters paper (e.g., “Planck 2018 results. VI. Cosmological parameters”, arXiv:1807.06209) with correct title and author list, and verify that no Planck 2015 paper (such as arXiv:1506.07135) is accidentally used under this key. Explicitly include the arXiv ID in the bibliography entry to make this transparent.


## PAPER-PER-m2 — Weinberg cosmological-constant review citation metadata

**Section:** Introduction, first paragraph: “cosmological constant problem~\cite{Weinberg1989}”.

**Issue:** The key `Weinberg1989` presumably targets Weinberg’s famous cosmological-constant review (Rev. Mod. Phys. 61, 1–23, 1989), but the paper text provides no explicit title or venue and no arXiv ID; if the bib entry were mistakenly tied to a different Weinberg 1989 article (or an arXiv preprint with different metadata), this would be a fused reference (correct concept but mis-specified venue/year). [1]

**Fix (1–2 sentences):** In the bibliography, explicitly set `Weinberg1989` to “S. Weinberg, ‘The Cosmological Constant Problem,’ Rev. Mod. Phys. 61, 1 (1989)” and avoid attaching any arXiv ID unless it corresponds to an actual preprint of that same article. Double-check that no other Weinberg 1989 paper is linked to this key.


## PAPER-PER-n1 — DESI 2024/2025 BAO citations underspecified

**Section:** Introduction, first paragraph: “DESI 2024–2025 BAO results…~\cite{DESI2024,DESI2025DR2}”.

**Issue:** The placeholders `DESI2024` and `DESI2025DR2` are used without explicit titles, arXiv IDs, or DOIs; as of now multiple DESI BAO and DR2 papers exist or are forthcoming, and an incorrect mapping (e.g., using a general DESI overview instead of the BAO-specific DR2 cosmology paper) would make these references non-auditable. [1]

**Fix (1–2 sentences):** Update the bibliography so that `DESI2024` and `DESI2025DR2` correspond to specific DESI BAO/cosmology papers with full titles, lead authors, arXiv IDs, and journal references, and verify that the quoted “3.1–4.2σ” dark-energy evidence actually appears in those exact papers. If the results are still from internal DESI notes, mark them explicitly as “DESI Collaboration, in preparation / private communication” rather than as standard published citations.


## PAPER-PER-n2 — Golden 2026 internal “Paper II/III/IV” citation cluster

**Section:** Throughout (Table I notes, Sec. 2.1, spin results, PTA results, Fisher forecasts) — citations `Golden2026P2`, `Golden2026P3`, `Golden2026P4`.

**Issue:** Multiple self-citations to “Paper II”, “Paper III”, and “Paper IV” with keys `Golden2026P2`, `Golden2026P3`, and `Golden2026P4` describe substantial external results (SPHEREx Fisher \(\sigma(f_{\rm NL})\), NANOGrav PTA real-KDE analysis, DESI Legacy galaxy spin catalog), but no corresponding arXiv entries or journal publications can be located; these appear to be internal project documents rather than publicly verifiable papers, yet are cited in the same way as established literature. [1]

**Fix (1–2 sentences):** Clearly label these works as “Golden, in preparation” or “Golden, internal Hubify report” in the references, and avoid presenting them as already-published sources; alternatively, remove them from the main literature list and refer to them as forthcoming companion papers, adding full citations only once arXiv IDs or journal DOIs exist.
