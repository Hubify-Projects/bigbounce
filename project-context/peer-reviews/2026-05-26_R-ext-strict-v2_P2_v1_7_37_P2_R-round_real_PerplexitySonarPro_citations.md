# P2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict-v2_P2_v1_7_37
**Wall time**: 23.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33368, completion=1529, total=34897

---

## PAPER-PER-B1 – Mis-cited Heinrich et al. SPHEREx paper

The paper repeatedly cites “Heinrich et al. 2024” / “Heinrich:2023” as a SPHEREx multi-tracer bispectrum forecast with σ(fNL) ≈ 0.7, including “Fig. 6 / Table 3” and explicit bispectrum-only vs bispectrum+power-spectrum numbers, but the actual Heinrich et al. arXiv paper on SPHEREx primordial non-Gaussianity is arXiv:2109.13945 (Heinrich, Dvorkin, Hu, “Primordial non-Gaussianity with SPHEREx”), not “Heinrich:2023”, and its detailed σ(fNL) numbers and figure/table mapping must match that specific source. [1]  
Fix: Replace the placeholder cite key “Heinrich:2023” by the correct arXiv ID and bibliographic entry for the SPHEREx PNG paper (checking that the quoted σ(fNL)=0.7, the “multi-tracer bispectrum” language, and the “Fig. 6 / Table 3” references match the actual figures/tables), or else adjust the text to accurately reflect the true Heinrich et al. results.

## PAPER-PER-M1 – Wilson-Ewing model and Zhu & Cai 2026 echo paper

The Wilson-Ewing quasi-dust model is cited as “WilsonEwing:2012” with n_s = 1 + 12 w, but the canonical LQC matter-bounce paper is “L. Linsefors, A. Barrau, Class. Quant. Grav. 32 (2015) 035010” while Wilson & Ewing’s key ΛCDM-like matter bounce work is arXiv:1206.1474 (“The Matter Bounce Scenario in Loop Quantum Cosmology”). [2] The text also cites a “Zhu & Cai 2026 echoes” paper with ID “Zhu:2026echoes”, which appears not to exist on arXiv or ADS as of now. [3]  
Fix: Verify that “WilsonEwing:2012” actually points to arXiv:1206.1474 (or the appropriate Wilson & Ewing LQC bounce paper) in the .bib file and that the quoted n_s = 1 + 12 w relation is indeed stated there; either remove or clearly label the Zhu & Cai “2026 echoes” as a hypothetical/unpublished work, or replace it with an existing, correctly cited bounce-with-late-inflation paper.

## PAPER-PER-M2 – Cai & Brandenberger normalization / factor-of-two discussion

The paper attributes an alternative normalization “fnl = -35/16” at c_s = 1 to “Li & Brandenberger” and describes “Cai & Brandenberger 2014” as adopting this value, but the non-Gaussianity-in-a-matter-bounce reference is Cai et al. arXiv:0903.0631 (“Non-Gaussianity in a Matter Bounce”), and the later Li & Brandenberger follow-up is arXiv:1010.XXXX / 1100.XXXX (exact IDs must be checked) with a specific convention; there is no arXiv record matching the exact author/normalization fusion as written. [0][4]  
Fix: Explicitly map each statement to a real paper: (i) keep Cai et al. 2009 as arXiv:0903.0631 with fnl = -35/8 in the Planck/Komatsu–Spergel convention; (ii) identify the precise Li & Brandenberger paper and confirm whether it ever quotes -35/16 at c_s = 1; if not, remove or rewrite the “Li & Brandenberger (c = 1)” language to reflect the actual conventions in those papers and avoid attributing an fnl value that does not appear in the cited source.

## PAPER-PER-m3 – Mercuri & Freidel Einstein–Cartan–Holst citations

The text attributes the statement that the Holst term becomes a topological invariant with vanishing torsion for canonical scalar matter to “Mercuri 2006” and “Freidel et al. 2005”, but the likely intended sources are Mercuri, Phys. Rev. D 73, 084016 (arXiv:gr-qc/0601013) and Freidel, Minic, Takeuchi, Phys. Rev. D 72, 104002 (arXiv:hep-th/0507253); these need to be confirmed as actually stating the scalar-sector decoupling in the way claimed. [5][6]  
Fix: Check that Mercuri (2006) and Freidel et al. (2005) really state the topological-invariant argument for the Holst term in the scalar-only sector exactly as summarized; if the scalar-only conclusion is only implicit or only derived for fermions, adjust the prose to more conservative wording (e.g. “implies” / “is consistent with”) and give precise equation or section references in those papers.

## PAPER-PER-m4 – Dalal, Slosar and Heinrich projection of SDB formulae

The scale-dependent bias formula and M(k,z) kernel are correctly attributed to Dalal et al. (2008) and Slosar et al. (2008), but the paper then mixes this with Heinrich et al. 2024 SPHEREx bispectrum forecasts to talk about “SDB Fisher” and “multi-tracer cancellation” in a way that implicitly assumes those later forecasts adopt precisely eqs. (sdb)–(Mkz) with the same normalization and δ_c ≈ 1.686. The Heinrich SPHEREx paper (arXiv:2109.13945) must be checked to ensure that the normalization, δ_c value, and multi-tracer treatment are indeed identical to Dalal/Slosar and that there is no mismatch in the definition of fNL or the transfer kernel. [1][7]  
Fix: Verify in Heinrich et al. that the same Δb(k,z) and M(k,z) conventions are used (including δ_c and transfer normalization); if there is any difference, explicitly state the mapping between conventions and adjust the Fisher discussion so that it does not assume exact identity of kernels without comment.

## PAPER-PER-n1 – Bibliography key “Heinrich:2023” and year mismatch

Throughout, the Heinrich SPHEREx reference is tagged “Heinrich:2023” but described as “Heinrich et al. 2024” in the abstract and body; arXiv:2109.13945 was posted in 2021 and the associated published version has its own year. [1]  
Fix: Harmonize the year and citation key: either consistently treat the paper as “Heinrich et al. 2021” with the correct journal year, or if using “2024” as the publication year, update the cite key and in-text year to match the actual published bibliographic record.
