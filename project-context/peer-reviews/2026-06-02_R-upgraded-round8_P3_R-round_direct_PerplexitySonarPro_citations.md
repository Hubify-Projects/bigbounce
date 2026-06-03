# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 13.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79670, completion=1092, total=80762, search_context_size=low, cost={'input_tokens_cost': 0.23901, 'output_tokens_cost': 0.01638, 'request_cost': 0.006, 'total_cost': 0.26139}

---

## PAPER-PER-B1 (MAJOR) – Mis-cited Heinrich et al. SPHEREx paper

**Location:** Intro, para 2: “Heinrich et al. \cite{Heinrich2023} (anchored to the Heinrich+2024 … JCAP 2024 arXiv:2311.13082)” and bib entry `Heinrich2023`.

**Issue:** The SPHEREx multi-tracer bispectrum paper by C. Heinrich et al. is *JCAP 05 (2024) 074, arXiv:2311.13082*; the text calls it “Heinrich+2024” but the bib key is `Heinrich2023` and the preprint year is 2023 while the journal year is 2024. The combination “JCAP 2024 arXiv:2311.13082 Heinrich2023” is internally inconsistent.

**Fix:** Rename the bib key to something like `Heinrich2024` and make sure all in‑text references consistently describe it as a 2024 JCAP paper with arXiv:2311.13082; or, if you insist on year-by-arXiv convention, drop the “JCAP 2024” phrasing and refer to it unambiguously as a 2023 arXiv preprint accepted to JCAP.


## PAPER-PER-M1 (minor) – Wands 2010 citation used for matter‑bounce fNL

**Location:** Intro, para 2: “The quasi-matter bounce model predicts … $f_{\rm NL} = -35/8$~\cite{Wands2010,Cai:2009fn,WilsonEwing2012}.”

**Issue:** The primary detailed derivation of the local‑type $f_{\rm NL}=-35/8$ in a matter bounce is Y.-F. Cai et al., JCAP 05 (2009) 011, arXiv:0903.0631 (`Cai:2009fn`). Wands 2010 (Class. Quant. Grav. 27, 124002, arXiv:1004.0818) is a broad review of primordial non‑Gaussianity in inflation and does not itself derive the specific matter‑bounce value.

**Fix:** Keep citing `Cai:2009fn` and `WilsonEwing2012` for the prediction, but either drop `Wands2010` from that parenthetical or rephrase to make clear that Wands is a general review of local non‑Gaussianity, not the source of the $-35/8$ value.


## PAPER-PER-M2 (minor) – Cai 2014 review described as “Exploring bouncing cosmologies…”

**Location:** Long comment block around line 1350 (internal review notes), and bib entry “Cai2014”.

**Issue:** The review by Y.-F. Cai is indeed *Sci. China Phys. Mech. Astron. 57 (2014) 1414–1452, “Exploring Bouncing Cosmologies with Cosmological Surveys”*, arXiv:1405.1369. The text correctly treats it as a bouncing‑cosmology review, but it is cited alongside Cai:2009fn and Quintin 2014 as if all three carry the same detailed matter‑bounce $n_T=2$ prediction. Cai 2014 summarizes many models and does not add an independent derivation of that specific spectral tilt.

**Fix:** Keep Cai 2014 as a legitimate review citation, but narrow the “matter‑bounce contraction + $n_T=2$ blue‑tilt prediction” attribution to Cai:2009fn (and, if desired, Quintin 2014), clarifying that Cai 2014 is a survey/overview reference rather than an additional primary derivation.


## PAPER-PER-m1 (nit) – NANOGrav KDE data citation could be more explicit

**Location:** Sec. 6.2 (NANOGrav), Appendix \ref{app:pta_mcmc}; cites “Zenodo 10.5281/zenodo.8060824” for the KDE free‑spectrum likelihood.

**Issue:** The description “NANOGrav 15-year HD‑correlated free‑spectrum KDE likelihood release” is accurate, but the main text often informally calls this “the NANOGrav 15-year HD‑correlated free-spectrum KDE” without explicitly tying it to the Agazie et al. 2023 ApJL discovery paper, which can confuse readers about what exactly is being fit.

**Fix:** In the first NANOGrav paragraph, explicitly reference both the evidence paper (Agazie et al., ApJL 951 L8, 2023) and the KDE data release (Zenodo 10.5281/zenodo.8060824), making clear that the MCMC is run on the Zenodo KDE product derived from the NANOGrav 15-year data of Agazie et al.
