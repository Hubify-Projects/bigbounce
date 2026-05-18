# P4_v1_0_108_R_INTERNAL R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1645pt
**Wall time**: 29.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=88863, completion=1320, total=90183

---

## PAPER-PER-B1 — Mis-cited Iye & Yagi 2026 paper

**Issue (MAJOR)**  
Abstract and elsewhere cite “Iye & Yagi (2026) — arXiv:2605.05570” as “Spin Parity of Spiral Galaxies VI – A Search for Dynamical Memory in the Spin Distribution of Galaxies in HSC WIDE Survey Regions,” but that arXiv ID does not yet exist / is not resolvable as of now. This looks like forward-dated, fused metadata (title + year + arXiv ID invented in advance).  

**Fix**  
Remove the arXiv ID and year entirely until the paper is actually posted, or replace with “in preparation / private communication” if appropriate, without a fake arXiv number. Once the real arXiv entry exists, update to the exact title, authors, and ID from arXiv/ADS.

---

## PAPER-PER-B2 — CE-ResNet citation metadata

**Issue (nit)**  
The CE‑ResNet paper is cited as Jia et al. (2023), ApJ 943, 32 with DOI 10.3847/1538‑4357/aca8aa and arXiv:2210.04168, which matches arXiv and ApJ records exactly.[1] There is no actual error here, but your text alludes to earlier fused metadata (wrong page or DOI suffix) and “correction” notes in comments/footnotes. That historical commentary is confusing in a final manuscript.  

**Fix**  
Keep the clean, correct bib entry (authors, year, journal, volume, page, DOI, arXiv:2210.04168) and remove any in‑text “NOTE/GPT caught…” provenance remarks about past metadata mistakes. Those belong in your private changelog, not in the scientific text.

---

## PAPER-PER-B3 — Iye et al. 2021 citation

**Issue (minor)**  
You cite Iye et al. (2021) as ApJ 907, 123 with arXiv:2011.00662 and DOI 10.3847/1538‑4357/abb3bb.[0] This matches arXiv and ApJ records; however, in one place you label it “Iye 2020” in the key “Iye:2020” and in text (“Iye (2020)” vs the 2021 ApJ publication year). That is inconsistent but not scientifically wrong.  

**Fix**  
Standardize everywhere as either “Iye et al. (2021)” (journal year) or “Iye et al. (2020, arXiv:2011.00662)” consistently, and make the bib-key/comment match the chosen convention. Avoid mixing “2020” and “2021” for the same paper.

---

## PAPER-PER-B4 — Lue, Wang & Kamionkowski and related parity references

**Issue (nit)**  
For Lue, Wang & Kamionkowski 1999 (parity-violating gravity), you give the standard reference (Phys. Rev. Lett. 83, 1506, arXiv:astro-ph/9812088), and this matches arXiv and journal metadata. Your text correctly describes it qualitatively as a parity-violating tensor source, but you slightly blur the distinction between that class and later EFT-of-LSS scalar parity probes (e.g. Cabass–Ivanov–Philcox) when talking about “same parameter space.” That’s conceptual rather than citation‑metadata, but it’s easy for readers to misread as a direct mapping.  

**Fix**  
In the cosmology-parity discussion, explicitly say that your chirality dipole, CMB birefringence, and parity-odd 4PCF constraints all live in *different* observable and parameter spaces, and that you are not quoting or implying a direct bound on the specific Lue–Wang–Kamionkowski tensor–chirality parameter or on Cabass–Ivanov–Philcox’s EFT coupling. This keeps the references from being over‑interpreted.

---

## PAPER-PER-B5 — LSST reference and arXiv ID

**Issue (MAJOR, citation-chain)**  
You correctly cite the LSST reference-design ApJ paper as Ivezić et al. 2019, ApJ 873, 111, DOI 10.3847/1538‑4357/ab042c. However you also discuss arXiv:0805.2366 as if it were the direct preprint of that paper; arXiv:0805.2366 is the much older “LSST Science Book” and not the actual preprint of the 2019 ApJ article. This is a fused‑metadata chain (one title/DOI and a different arXiv ID).  

**Fix**  
For the ApJ reference‑design paper, cite only the ApJ entry (Ivezić et al. 2019, ApJ 873, 111, DOI) and remove the 0805.2366 arXiv number from that citation. If you want to cite the LSST Science Book as well, give it its own separate reference explicitly labeled as such, with its correct arXiv ID and title.

---

## PAPER-PER-B6 — DESI white paper citation

**Issue (minor)**  
DESI Collaboration “The DESI Experiment Part I: Science, Targeting, and Survey Design” is correctly cited as arXiv:1611.00036, with “white-paper only, no journal publication” noted.[0] That’s accurate. However in one place you speak of it as if it had an associated journal venue (“white-paper-only, no journal publication” parenthetical after treating it like a journal entry). This can confuse bibliographic parsing.  

**Fix**  
Treat DESI Part I uniformly as an arXiv/white paper: give authors, title, arXiv:1611.00036, year, and do not imply a journal. Drop journal-style volume/page fields for this entry in the bib and in-text description.
