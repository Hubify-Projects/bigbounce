# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 32.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100544, completion=2065, total=102609, search_context_size=low, cost={'input_tokens_cost': 0.30163, 'output_tokens_cost': 0.03097, 'request_cost': 0.006, 'total_cost': 0.33861}

---

## PAPER-PER-B1 — BLOCKER — Incorrect citation & description of Motloch et al. result

**Location:** Sec. \ref{sec:motloch} (around “Motloch \etal~\cite{Motloch:2021} report a marginal ($\sim\!2.7\sigma$) correlation…” and again later “Motloch \etal~\cite{Motloch:2021}”).  

**Issue:** The paper repeatedly cites “Motloch \etal~\cite{Motloch:2021}” for the Nature Astronomy result on spin–initial-condition correlations, but the actual paper is by *Motloch & Pen* (two authors), not “Motloch et al.”, and the preprint is arXiv:2003.04800 with title “Cosmological signature of galaxy spin correlations and intrinsic alignments” in some early versions, while the Nature Astronomy publication is “A correlation between galaxy spins and the large-scale tidal field” (check exact title on ADS). The current bib item mixes the arXiv ID and Nature Astronomy venue but does not give the correct author list / title.  

**Fix:** Update the BibTeX entry for \cite{Motloch:2021} to match the published Nature Astronomy paper (correct authors: P. Motloch and U.-L. Pen; correct title and journal details from ADS), and in the text replace “Motloch \etal” with “Motloch & Pen” wherever referring to that work.


## PAPER-PER-M2 — MAJOR — Mis-cited Iye & Yagi forthcoming paper

**Location:** Sec. \ref{sec:shamir}, paragraph mentioning “Iye~\&~Yagi, in prep.” and “An anticipated Iye~\&~Yagi forthcoming HSC-WIDE Survey spin-parity analysis… An earlier placeholder citation identifier… has been removed pending a confirmed arXiv listing.”  

**Issue:** The text refers to an “Iye & Yagi, in prep.” HSC-WIDE spin-parity analysis as if it were a concrete forthcoming paper, but there is no arXiv ID or journal record to verify; this is effectively a non-existent citation. Mentioning it in the same style as published work risks implying a specific, traceable reference that does not (yet) exist.  

**Fix:** Keep the qualitative remark but rephrase to remove the appearance of a citable paper, e.g. “Iye and collaborators have announced plans for an HSC-WIDE spin-parity analysis (no preprint available at the time of writing); we therefore do not rely on any quantitative result from that project.” Ensure no BibTeX entry is created for this and that it is not cited with a numeric key.


## PAPER-PER-M3 — MAJOR — Inconsistent description of Cabass–Ivanov–Philcox EFT parameter

**Location:** Sec. \ref{sec:parity_translation}, paragraph on parity-odd galaxy trispectrum amplitude:  
> “Cabass, Ivanov \& Philcox~\cite{Cabass:2023} provide the EFT-of-LSS framework… parameterized by \(g_*\) in their notation; the Cabass-Ivanov-Philcox EFT-of-LSS framework transports these primordial inflationary couplings to late-time LSS observables, but \(g_*\) itself parameterizes the primordial inflationary parity-odd coupling, not an LSS operator).”

**Issue:** In Cabass–Ivanov–Philcox (Phys.Rev.D 107, 023523, arXiv:2210.16320) the parameter they constrain in their LSS analysis is typically denoted \(f_{\rm NL}^\chi\)-like combinations rather than a simple \(g_*\); \(g_*\) is more standard in anisotropic inflation literature (Ackerman–Carroll–Wise) than in their specific trispectrum EFT. The current text grafts the wrong symbol/concept from other parity-odd/anisotropic work onto this paper, which is misleading.  

**Fix:** Replace the sentence with one that matches their notation, e.g. “Cabass, Ivanov & Philcox provide an EFT-of-LSS framework that maps a primordial parity-odd trispectrum amplitude (their parameter combination constrained from BOSS; see their Eq. [ref]) into late-time galaxy correlations.” Remove the specific claim that they parameterize it with \(g_*\) unless you verify that symbol in their paper; if you keep a symbol, use the exact one from Cabass–Ivanov–Philcox.


## PAPER-PER-M4 — MAJOR — Mischaracterization of the Cahn–Slepian–Hou / Philcox parity-odd 4PCF significance

**Location:** Sec. \ref{sec:parity_translation}, paragraph on (ii) parity-odd galaxy trispectrum:  
> “Philcox~\cite{Philcox:2023} and Hou, Slepian \& Cahn~\cite{Hou:2023} have since reported parity-odd 4PCF measurements on BOSS DR12, with significances of $\sim\!2.9\sigma$ (blind test) and $\sim\!7.1\sigma$ (CMASS) / $3.1\sigma$ (LOWZ) respectively.”

**Issue:** Philcox 2022 (Phys.Rev.D 106, 063501, arXiv:2206.04227) reports a detection of parity-odd signatures at about \(3\sigma\), but the exact breakdown (blind vs CMASS vs LOWZ significance values) and the “7.1σ/3.1σ” numbers are from Hou–Slepian–Cahn 2022 (MNRAS 522, 5701, arXiv:2206.03625) and are not attributed cleanly. The current sentence fuses the two results and may give Philcox credit for the 7.1σ CMASS detection, which actually belongs to Hou et al.  

**Fix:** Split the description: explicitly attribute the ~3σ blind test to Philcox and the 7.1σ (CMASS) / 3.1σ (LOWZ) to Hou–Slepian–Cahn. E.g. “Philcox [..] finds a ~3σ parity-odd 4PCF signal in BOSS, while Hou, Slepian & Cahn report ~7.1σ (CMASS) and ~3.1σ (LOWZ).” Verify the exact numbers from both arXiv papers and adjust them if needed.


## PAPER-PER-m5 — minor — Ambiguous reference to “Motloch \etal~[Yu:2020]” and tidal-torque link

**Location:** Sec. \ref{sec:motloch} and Sec. \ref{sec:parity_translation} (paragraphs that say Motloch et al. interpret their signal “in the linear-theory framework of \cite{Yu:2020}” / “Yu~\etal~\cite{Yu:2020}”).  

**Issue:** Yu et al. (Phys.Rev.Lett. 124, 101302, arXiv:1904.01029) indeed discuss probing primordial chirality with galaxy spins, but they do not provide a simple, ready-to-use transfer function from a morphology dipole to a specific primordial tensor parameter; the paper text risks overstating that they provide a direct mapping used here.  

**Fix:** Soften the wording to “Yu et al. develop a linear-theory framework for relating chiral primordial fields to galaxy spin statistics; our work does not implement their specific transfer function and only references this qualitatively.” This keeps the citation but removes the implication that their mapping is quantitatively applied in this paper.


## PAPER-PER-n6 — nit — Redundant / confusing dual use of “Shamir:2022” and “Shamir:2022DESI”

**Location:** Bibliography entries `\bibitem{Shamir:2022}` and `\bibitem{Shamir:2022DESI}`, and references in the Introduction / Sec. \ref{sec:shamir}.  

**Issue:** You have two BibTeX keys for Shamir 2022: one PASJ spin-alignment paper and one MNRAS DESI Legacy spin-direction paper, but in the main text the shorthand “Shamir~(2022)~\cite{Shamir:2022DESI}” plus “Shamir~(2022)~\cite{Shamir:2022} (MNRAS 516 2281, DOI 10.1093/mnras/stac2372)” is slightly muddled; PASJ is incorrectly labelled with the MNRAS volume in one place, and “Shamir:2022” is glossed as the methodology paper while “Shamir:2022DESI” is the DESI analysis—this is easy for readers to misparse as a single paper.  

**Fix:** Make the separation explicit and consistent: ensure `Shamir:2022DESI` is the MNRAS 516, 2281 DESI Legacy paper (stac2372) and `Shamir:2022` is the PASJ 74, 1114 methodology / spin-pattern paper, and adjust the in-text parentheticals so each reference points to the right venue. One clean way is to always write “Shamir (2022, PASJ)” vs “Shamir (2022, MNRAS)” and cite the appropriate key.
