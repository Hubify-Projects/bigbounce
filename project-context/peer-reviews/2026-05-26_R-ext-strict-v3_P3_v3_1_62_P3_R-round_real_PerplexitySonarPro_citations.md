# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict-v3_P3_v3_1_62
**Wall time**: 10.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68051, completion=740, total=68791

---

## PAPER-PER-M1
**MAJOR** — `Introduction` bibliography/citation chain. `Heinrich2023` is cited as “JCAP 2024, 074 (2024), arXiv:2311.13082,” but the paper text then layers on an internal “Heinrich+2024” benchmark and multiple Fisher numbers without a clean source boundary. The citation metadata itself is fine, but the claim chain is not auditable as written: separate the published reference from internal calculations, and cite the paper only for the published multi-tracer methodology. 

## PAPER-PER-M2
**MAJOR** — `References` / `NANOGrav2023`, `EPTA2023`, `PPTA2023`, `Afzal2023NewPhys`. `2306.16214`, `2306.16215`, and `2306.16219` are real arXiv IDs and the titles/authors/venues match the arXiv pages. However, the manuscript’s wording “matter-bounce is favored” and “SMBHB strongly disfavored” goes beyond what these sources support; the cited papers report evidence for a common-spectrum process and caution against overinterpreting model preference. Tighten the claim language to “consistent with” / “parameter-shift comparison only.” 

## PAPER-PER-M3
**MAJOR** — `References` / `Liang2023`. The arXiv ID `2307.07664` and title “Outlier Detection in the DESI Bright Galaxy Survey” are correct, but the paper repeatedly attributes the result to a DESI EDR baseline while the manuscript’s own comparison text slides between EDR and DR1. Keep the Liang citation tied strictly to the DESI EDR result and do not reuse it as evidence for DR1-scale rate claims unless you explicitly justify the extrapolation. 

## PAPER-PER-M4
**MAJOR** — `References` / `SPHEREx2014`. `1412.4872` is real and the title is correct, but the manuscript treats it as a direct forecast anchor for present-day anomaly-selected tracers. That is a scope mismatch: the cited SPHEREx white paper is a mission-forecast document, not a validation of your specific tracer-selection pipeline. Rephrase to “SPHEREx mission context” and remove any implication that the paper supports the numeric forecast specifics. 

## PAPER-PER-M5
**minor** — `References` / `ACT_DR6`. The citation metadata for Qu et al. is plausible, but the manuscript repeatedly calls ACT “quarantined” while still using it in cross-transfer baseline counts and null-correlation discussion. That is internally consistent only if you explicitly mark it as an excluded diagnostic dataset everywhere the citation appears; otherwise the reference is being used for both science and non-science roles. 

## PAPER-PER-M6
**nit** — `References` / `Cai:2009fn` and `WilsonEwing2012`. These are real papers, but the manuscript’s title-level physics claims about a tightly coupled \(f_{\rm NL}=-35/8\) and \(\gamma_{\rm GW}=3.0\) “same contracting-phase mode-function calculation” are overstated relative to the cited literature. Keep the citations, but downgrade the wording to “motivated by” / “consistent with the matter-bounce class,” unless you add a direct derivation citation. 
