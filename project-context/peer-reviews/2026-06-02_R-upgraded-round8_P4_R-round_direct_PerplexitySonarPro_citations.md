# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 33.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100595, completion=2031, total=102626, search_context_size=low, cost={'input_tokens_cost': 0.30179, 'output_tokens_cost': 0.03047, 'request_cost': 0.006, 'total_cost': 0.33825}

---

## PAPER-PER-B1 — Shamir 2022 DESI paper metadata

**Type:** MAJOR  
**Location:** Intro, first paragraph of comparison (near “Shamir (2022) [Shamir:2022DESI] (arXiv:2208.13866, DESI Legacy Survey, MNRAS 516 2281; …)”  

**Issue:**  
Citation text compresses Shamir (2022) DESI work as “…DESI Legacy Survey, MNRAS 516 2281…”, which is correct, but earlier in the bibliography there are *two distinct Shamir 2022 entries* used in overlapping ways:  
- `\bibitem{Shamir:2022}` is PASJ 74, 1114 / parity paper[ ]  
- `\bibitem{Shamir:2022DESI}` is the MNRAS 516, 2281 DESI Legacy spin‑directions paper[ ].  
In the main text, several phrases like “Shamir (2022)~\cite{Shamir:2022DESI} (arXiv:2208.13866, DESI Legacy Survey, MNRAS 516 2281…)” are fine, but other occurrences (“Shamir’s earlier work~\cite{Shamir:2020} … Shamir~(2022)~\cite{Shamir:2022DESI} reported DESI Legacy Survey results…”) effectively treat “Shamir 2022” as a single DESI paper, while PASJ 2022 is also present in the bib and never clearly disambiguated as a *different* 2022 paper. That’s a metadata / naming confusion risk.  

**Fix:**  
Rename the bibkeys or in‑text labels to make the distinction explicit and consistent, e.g. use “Shamir (2022a)” for PASJ 74, 1114[ ] and “Shamir (2022b)” for DESI MNRAS 516, 2281[ ], and check every “Shamir (2022)” occurrence refers to the correct key. Avoid using “Shamir (2022) [Shamir:2022DESI]” in contexts where both 2022 papers are being discussed.


## PAPER-PER-B2 — Motloch & Pen reference metadata

**Type:** MAJOR  
**Location:** Sec. “Motloch & Pen (2021)” and other mentions of Motloch et al.  

**Issue:**  
The paper is cited as “Motloch et al. (2021) … Nature Astron. 5, 283 (2021), arXiv:2003.04800”[ ]. ADS/arXiv show the article is *“Motloch, Yu, Pen & Xie, ‘An observed correlation between galaxy spins and initial conditions’, Nature Astronomy, volume 5, pages 283–289 (2021)”* with exactly those details, so the core metadata are correct. However, the text repeatedly shortens this to “Motloch & Pen” as though it were a two‑author paper, even in section titles, which is misleading given two additional co‑authors (Yu, Xie) are named in the actual paper.  

**Fix:**  
Change section titles and first mentions to “Motloch et al. (2021)” or “Motloch, Yu, Pen & Xie (2021)” consistently rather than “Motloch & Pen”, and ensure the bib entry lists all four authors as in the Nature Astronomy record[ ].


## PAPER-PER-M3 — CE‑ResNet citation chaining

**Type:** MAJOR  
**Location:** Multiple; e.g. Intro CE‑ResNet paragraph and Table comparing CE‑ResNet vs this work.  

**Issue:**  
The CE‑ResNet paper is cited with arXiv:2210.04168, ApJ 943, 32, DOI 10.3847/1538‑4357/aca8aa, authors Jia, Zhu & Pen, which matches arXiv and ApJ metadata[ ]. The text attributes:  
- architectural chirality equivariance,  
- catalog size ~1.95M spirals,  
- CW/CCW ratio ~0.998,  
all of which are stated in Jia et al. 2023[ ]. No fused or mismatched title/ID/venue is present.  
However, some passages imply CE‑ResNet was trained “primarily on DESI Legacy imaging (with SDSS used in training)” and that its catalog spans “the SDSS+DESI imaging footprint” without an explicit check that the released catalog’s imaging sources indeed match that description. From the paper, CE‑ResNet uses SDSS DR7/DR8 + DESI Legacy (DECaLS) training and constructs a DESI‑footprint catalog; but “SDSS+DESI imaging footprint” as a single combined *inference* footprint is stronger than what is clearly stated.  

**Fix:**  
Tighten wording to match Jia et al.’s exact description, e.g. “trained on SDSS and DESI Legacy data and releasing a catalog of ~1.95M chirality classifications in the DESI imaging region”[ ], unless you have independently verified the catalog’s full footprint. Avoid implying a unified “SDSS+DESI footprint” at inference if that is not explicitly documented.


## PAPER-PER-m4 — SpArcFiRe metadata

**Type:** minor  
**Location:** Sec. “SpArcFiRe” and related bib entry.  

**Issue:**  
The SpArcFiRe paper is cited as Davis & Hayes 2014, ApJ 790, 87 (2014), arXiv:1402.1910, which matches the real article “SpArcFiRe: Scalable Automated Detection of Spiral Galaxy Arm Segments”[ ]. The text’s summary (“~140,000 galaxies, deterministic, 99.983% self‑consistency, 85.8% agreement with Galaxy Zoo 1, 92.5% at high confidence”) is consistent with the numbers in Davis & Hayes’s abstract and results tables[ ]. No ID/title fusion or venue mismatch is present. The only issue is that later, the text references a “Hayes‑Davis DR9 update” catalog as if peer‑reviewed, but that update is only a public catalog release, not a separate journal paper.  

**Fix:**  
Clarify that the “DR9 update” is a catalog release or unpublished supplement, not a second refereed paper, and give its status explicitly (e.g. data release on authors’ site) while keeping the main citation pointing to Davis & Hayes 2014 ApJ 790, 87[ ].


## PAPER-PER-m5 — DESI instrumentation / survey reference

**Type:** minor  
**Location:** “Future directions” and data availability (DESI citation).  

**Issue:**  
DESI is cited via “DESI Collaboration, Aghamousa et al. 2016, ‘The DESI Experiment Part I: Science, Targeting, and Survey Design,’ arXiv:1611.00036; white‑paper only, no journal publication”[ ]. This matches the actual arXiv white paper[ ], but the DESI experiment now also has refereed survey overview papers (e.g. DESI Collaboration 2024, ApJ Suppl. for DR1) not cited here. That’s not wrong, but given the text leans on spectroscopic overlap and DR1/Y1 usage, citing only the 2016 white paper is a bit out of date.  

**Fix:**  
Consider adding at least one modern DESI data‑release reference (e.g. DESI DR1 overview) alongside the 2016 arXiv experiment paper to better anchor statements about current spectroscopic data usage; keep arXiv:1611.00036 as the experiment design reference[ ].


## PAPER-PER-n6 — Minor arXiv / DOI consistency note

**Type:** nit  
**Location:** Bibliography entries for Cahn–Slepian–Hou parity‑odd 4PCF and related works.  

**Issue:**  
Cahn et al. are cited as “Phys. Rev. Lett. 130, 201002 (2023), arXiv:2110.12004”[ ], Philcox as “Phys. Rev. D 106, 063501 (2022), arXiv:2206.04227”[ ], Hou et al. as “MNRAS 522, 5701 (2023), arXiv:2206.03625”[ ], Cabass et al. as “Phys. Rev. D 107, 023523 (2023), arXiv:2210.16320”[ ]. All IDs, years and venues match the real papers[ ]. The only nit is that one inline parenthetical calls Cabass–Ivanov–Philcox an “EFT‑of‑LSS framework for parity‑odd LSS operators” while the title specifically emphasizes “colliders and ghosts” and dimension‑7 inflationary operators; that’s directionally right but hand‑wavy.  

**Fix:**  
Optionally sharpen the one‑line description of Cabass et al. to match the title more closely (e.g. “EFT‑of‑Inflation + EFT‑of‑LSS treatment mapping parity‑odd inflationary dimension‑7 operators to the observed galaxy 4‑point function”[ ]) to avoid any impression of a different paper.
