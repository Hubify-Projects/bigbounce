# P5 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round4
**Wall time**: 15.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34650, completion=1453, total=36103, search_context_size=low, cost={'input_tokens_cost': 0.10395, 'output_tokens_cost': 0.0218, 'request_cost': 0.006, 'total_cost': 0.13175}

---

## PAPER-PER-B1 — DESIVAST authorship and citation details

**Severity:** MAJOR  

**Location:** Bibliography entry `\bibitem{DESIVAST2025}` and discussion in §XII.  

**Issue:** The DESIVAST paper is cited as “H. Rincon, S. BenZvi, K. A. Douglass, D. Veyrat et al. (DESI Collaboration)” in ApJ 982, 38 (2025), arXiv:2411.00148, but the actual first author is **Hernan Rincon** and the journal reference is ApJ **962**, 38 (2025). The current bibitem fuses the correct first author name (Hernan Rincon) with an incorrect volume (982). The main text also calls it “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” which matches the arXiv/published title, but the ApJ volume is wrong.[ ]  

**Fix:** Update the DESIVAST bibitem to use the correct ApJ volume (962, 38 (2025)) and ensure the author list ordering matches the journal version (Rincon et al.); verify all in-text mentions of “ApJ 982, 38” are corrected to “ApJ 962, 38”.  

---

## PAPER-PER-M1 — T-Web DESI citation metadata check

**Severity:** minor  

**Location:** `\bibitem{TWebDESI2026}` and §XII (“Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification”).  

**Issue:** arXiv:2604.02463 does exist with title “Cosmic web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification” and authors Ullah, Awais, Matos, Suárez-Pérez; the bibitem’s title, year, and author list are consistent, but the text calls it “submitted to MNRAS (2026)” even though the current arXiv record does not yet list a journal or submission status. This “submitted to MNRAS” is an author-side characterization, not supported by arXiv metadata.  

**Fix:** Soften the venue language to something arXiv-verifiable, e.g. “preprint (2026), arXiv:2604.02463” or “in preparation / under review,” unless and until a formal “submitted to MNRAS” status is publicly documented by the authors.  

---

## PAPER-PER-M2 — ASTRA-DESI metadata precision

**Severity:** minor  

**Location:** `\bibitem{ASTRADESI2026}` and §XII (“The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog”).  

**Issue:** arXiv:2604.01456 exists with title “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” and authors Zapata-Zuluaga, Guevara-Montoya, Torres-Gomez, Hernandez, Forero-Romero; the paper text matches this correctly, but labels it generically as “(2026)” without clarifying it is a preprint with no journal assignment yet. This is not wrong, but it conflates it slightly with fully refereed literature when used as “first public DESI cosmic-web catalog.”  

**Fix:** Add a short qualifier at first mention (e.g. “preprint, arXiv:2604.01456 (2026)”) and in §Limitations where it’s contrasted with peer‑reviewed products, to keep its status clearly distinguished from DESIVAST’s refereed ApJ catalog.  

---

## PAPER-PER-m1 — DESIVAST hole/void counts wording

**Severity:** nit  

**Location:** §XII, DESIVAST description: “1,461 interior voids with VoidFinder, 420 with V2-REVOLVER, and 295 with V2-VIDE… 89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids”.  

**Issue:** These numbers match the DESIVAST public FITS content, but the phrase “comprising the 3,765 maximal voids” could be misread as each hole mapping one-to-one to a maximal void. In DESIVAST, maximal voids are built from multiple holes; holes do not “comprise” the maximal voids in a simple count-equality sense, they are components.  

**Fix:** Rephrase to e.g. “101,863 interior VoidFinder holes associated with 3,765 maximal voids” to avoid suggesting a one-to-one mapping between holes and maximal voids.  

---

## PAPER-PER-m2 — ASTRA volume-filling-fraction calibration phrasing

**Severity:** nit  

**Location:** §XII (“The BGS-anchored volume-filling-fraction calibration in Ref.~\cite{ASTRADESI2026} is consistent with the V-Web sheet/filament fractions…”).  

**Issue:** ASTRADESI2026 states that they calibrate thresholds using BGS to match **GAMA** volume-filling fractions, not specifically DESI DR1 V-Web; saying it is “consistent with the V-Web sheet/filament fractions reported here” is an author’s comparison that is not explicitly made in ASTRADESI itself (though it can be numerically true).  

**Fix:** Make this clearly an author-side consistency check, e.g. “Their BGS-anchored calibration to match GAMA volume-filling fractions yields sheet/filament fractions numerically consistent with our V-Web values,” so it is not read as a claim about what ASTRADESI reports.  

---

## PAPER-PER-m3 — Internal companion-paper references vs external literature

**Severity:** nit  

**Location:** Bibliography entries `\bibitem{golden_chirality_2026}` and `\bibitem{golden_fnl_2026}`, plus abstract and §Introduction.  

**Issue:** Both internal manuscripts are described as “companion paper (Paper IV/II) … an arXiv identifier will be assigned upon submission,” but they are cited in the main text in ways that could be mistaken for established external literature (e.g. “Paper IV establishes the global mixture…”). This is already partially mitigated in several places, but a reader scanning only the bib could still misinterpret their status.  

**Fix:** Add a brief parenthetical “(internal companion manuscript; not yet publicly available)” in each bibitem and ensure every first in‑text mention of Paper II/IV explicitly repeats “companion work, not yet peer‑reviewed / not yet public” so their status cannot be mistaken for published external references.
