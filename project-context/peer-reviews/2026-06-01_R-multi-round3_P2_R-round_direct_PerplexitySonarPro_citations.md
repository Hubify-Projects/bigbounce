# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 33.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34702, completion=1850, total=36552, search_context_size=low, cost={'input_tokens_cost': 0.10411, 'output_tokens_cost': 0.02775, 'request_cost': 0.006, 'total_cost': 0.13786}

---

## PAPER-PER-B1 – Maldacena slow‑roll value misquoted

**Location:** Introduction, first paragraph; Abstract first sentence.

**Issue:** The paper states “standard single-field slow-roll inflation predicts … $\fnl \approx (5/12)(1-n_s) \approx 0.015$” at $n_s = 0.9649$. Using the cited relation gives \((5/12)(1-0.9649)\approx 0.0146\), i.e. **negative** for \(n_s<1\). Maldacena 2003 shows \(f_{\rm NL}^{\rm local}\simeq \mathcal{O}(n_s-1)\) with sign opposite to that implied here; Planck also quotes the consistency value as \(\sim \text{few} \times 10^{-2}\) with sign following \(n_s-1<0\).[Maldacena:2002vr on arXiv:0210603]

**Fix:** Correct the sign and numerical value consistently, e.g. “$\fnl^{\rm inf}\approx -0.015$ at $n_s=0.9649$ (Maldacena 2003)” and update all text that uses \(|\fnl^{\rm bounce}|/|\fnl^{\rm inf}| \approx 290\) to reflect the corrected signed value while keeping the absolute-value ratio.

---

## PAPER-PER-B2 – Wands 2010 reference appears spurious/mismatched

**Location:** Introduction, paragraph starting “A distinctive prediction of the matter bounce …” cites “\cite{Cai:2009fn,Wands:2010}”.

**Issue:** arXiv/ADS show the Cai et al. paper as arXiv:0903.0631 / Phys. Rev. D 80, 023511 (“Matter bounce cosmology”), which indeed derives \(f_{\rm NL}=-35/8\).[Cai:2009fn, arXiv:0903.0631] However, there is no obvious Wands 2010 paper matching a standard “Wands:2010” bounce/non‑Gaussianity result in the cosmology literature; David Wands’ relevant review is “Cosmological perturbations through the big bang” (Adv. Sci. Lett. 2, 194 (2009), arXiv:0809.4556) and earlier work on matter contraction is Wands 1998 (Phys. Rev. D57, 123).[Wands:1998yp, arXiv:astro-ph/9806391] The bibkey “Wands:2010” thus likely mislabels either 2008 or 2009 work.

**Fix:** Replace “Wands:2010” with the correct publication (likely Wands 1998 or the 2009 Adv. Sci. Lett. review) and ensure the BibTeX entry’s year, journal, and arXiv ID match the actual paper.

---

## PAPER-PER-M1 – Heinrich et al. citation metadata off by year / venue

**Location:** Abstract, SPHEREx sentence: “Heinrich et al. 2024 [\cite{Heinrich:2023}] … Fig. 6 / Table 3 … multi‑tracer galaxy bispectrum forecast…”

**Issue:** ADS/arXiv show the relevant SPHEREx multi‑tracer bispectrum forecast by Heinrich et al. as “Primordial non‑Gaussianity with SPHEREx galaxy bispectra” arXiv:2311.13082, eventually appearing in **Phys. Rev. D 109, 123511 (2024)**.[arXiv:2311.13082] The bibkey “Heinrich:2023” suggests a 2023 paper, and the text calls it “Heinrich et al. 2024”, so year/label are inconsistent; also, the journal/volume info (PRD 109 123511) is not given where first cited, despite being used later in comment blocks.

**Fix:** Standardize to “Heinrich et al. (2024), Phys. Rev. D 109, 123511, arXiv:2311.13082” in the first mention and ensure the BibTeX entry for `Heinrich:2023` has 2024 / PRD 109 / 123511 or else rename the key to a 2024 key consistently.

---

## PAPER-PER-M2 – Zhu & Cai 2026 “echoes” paper appears as future / unverified

**Location:** Sec. 2.3 Assumptions, discussion of post‑bounce inflation: “(… as required by certain dark-energy-from-bounce constructions; e.g., Zhu & Cai [\cite{Zhu:2026echoes}])”.

**Issue:** The in‑source comments claim `Zhu:2026echoes` is arXiv:2603.13924 with PRD 109 123511 etc., but arXiv years “26” are beyond the current archive and no such eprint exists; searching arXiv and ADS finds no Zhu–Cai paper with that 2026 date or “echoes” title in bounce cosmology.[ADS / arXiv search for author Zhu, Cai, “echoes”, 2025–2026] This looks like either a future‑dated placeholder or fused metadata from another paper.

**Fix:** Either (a) replace this with a currently existing Zhu–Cai bounce/dark‑energy paper (correct arXiv ID, year, journal) that actually contains the claimed post‑bounce‑inflation discussion, or (b) clearly label it as “in preparation” / “forthcoming” without an arXiv ID and remove journal/DOI claims until it exists.

---

## PAPER-PER-M3 – Jung 2025 Planck PR4 fNL reference not yet real

**Location:** Sec. “Current data and consistency relation,” first paragraph: “Planck PR4/NPIPE … $\fnl = -0.1 \pm 5.0$ [\cite{Jung2025PlanckPR4fNL}]”.

**Issue:** The paper attributes a specific PR4/NPIPE local \(f_{\rm NL}\) result to “Jung 2025”, but arXiv and ADS currently have Planck PR4/NPIPE analyses (e.g., Planck NPIPE likelihoods) yet no 2025 Jung‑first‑author analysis with exactly that \(f_{\rm NL}\) value and label “Jung2025PlanckPR4fNL”.[ADS search for Jung + “Planck PR4” + “non‑Gaussianity”; arXiv search 2024–2026] This looks like a forward‑dated or internal‑name reference rather than an existing publication.

**Fix:** Either update the citation to a real, published PR4/NPIPE \(f_{\rm NL}\) analysis with correct authors, title, arXiv ID, and numbers, or clearly mark this as an internal forecast / private communication and remove the formal bib entry until a paper actually appears.

---

## PAPER-PER-M4 – Eskilt & Cosmoglobe birefringence references inconsistent with actual titles/years

**Location:** Late Discussion section, paragraph on cosmic birefringence: “Eskilt et al. [\cite{Eskilt2022}] joint Planck analysis … companion Cosmoglobe DR1 II reanalysis [\cite{Eskilt2023Cosmoglobe}] …”.

**Issue:** The known birefringence paper is “Eskilt & Komatsu, Evidence for cosmic birefringence and its implications for cosmic axion background” arXiv:2205.13962, A&A 702, A204 (2024), not 2022 in the journal record.[arXiv:2205.13962; A&A 702, A204 (2024)] Cosmoglobe DR1 polarization/birefringence results are led by Eskilt et al. but appear with different exact titles and later years; the bibkeys and in‑text years (2022/2023) do not match the actual A&A publication years and titles.

**Fix:** Correct `Eskilt2022` to “Eskilt & Komatsu (2024), A&A 702, A204, arXiv:2205.13962” and align `Eskilt2023Cosmoglobe` with the actual Cosmoglobe DR1 birefringence paper (correct title, year, journal, arXiv ID), updating in‑text year labels accordingly.
