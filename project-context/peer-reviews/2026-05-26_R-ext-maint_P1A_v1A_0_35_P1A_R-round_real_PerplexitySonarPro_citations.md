# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint_P1A_v1A_0_35
**Wall time**: 23.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30080, completion=1836, total=31916

---

## PAPER-PER-B1 – Mis-cited “Planck2018params” reference

**Location**: Sec. I, first paragraph, citation `\cite{Planck2018params}`.  

**Issue**: The text clearly uses Planck 2018 cosmological parameters, but the BibTeX key `Planck2018params` must map to the paper “Planck 2018 results. VI. Cosmological parameters” (Aghanim et al., A&A 641 A6 (2020), arXiv:1807.06209). The placeholder-style key is nonstandard and could easily be mis-filled or mis-mapped; the arXiv ID and title are not explicitly checked in the manuscript and should be. The inflation paper “Planck 2018 results. X. Constraints on inflation” is a different article (Akrami et al., arXiv:1807.06211).[2][1]  

**Fix**: In the .bib file, ensure `Planck2018params` is an entry whose title is exactly “Planck 2018 results. VI. Cosmological parameters”, authors start with “Planck Collaboration: N. Aghanim, Y. Akrami, …”, journal is “A&A 641, A6 (2020)”, and arXiv ID is `1807.06209`. Add a separate key (e.g. `Planck2018inflation`) if the inflation constraints paper (arXiv:1807.06211) is also cited, to avoid title/ID fusion.[2][1]


## PAPER-PER-M1 – Ambiguous DESI citations and titles

**Location**: Sec. I, intro paragraph, citations `\cite{DESI2024,DESI2025DR2}` to “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)”.  

**Issue**: The DESI dark-energy papers are not identified by arXiv ID, author list, or exact title; “DESI2024”/“DESI2025DR2” look like internal keys and multiple DESI collaboration papers exist on BAO and dark energy with overlapping years, increasing risk of fused metadata (e.g. mixing DR1/DR2 BAO paper IDs with a different DESI dark-energy analysis title). Without explicit IDs, it is easy for a .bib entry to carry a wrong or partially matched title.  

**Fix**: In the bibliography, map `DESI2024` and `DESI2025DR2` to concrete DESI collaboration papers with exact titles and arXiv IDs corresponding to dark-energy / BAO analysis (e.g. “DESI 2024 Results: …” with the correct DR1/DR2 BAO dark-energy paper ID), and check that the quoted 3.1–4.2σ numbers match those specific papers. If more than one DESI paper is used (e.g. DR1 BAO only vs DR2 extended analysis), split into separate keys to avoid mixing titles and years.


## PAPER-PER-M2 – Weinberg 1989 citation likely under-specified

**Location**: Sec. I, first paragraph, `\cite{Weinberg1989}` for the cosmological constant problem.  

**Issue**: The canonical reference is Steven Weinberg, “The cosmological constant problem”, Reviews of Modern Physics 61, 1 (1989), not an arXiv paper; multiple secondary writeups and reprints exist. A generic key like `Weinberg1989` is easy to mis-map in a large .bib file (e.g. to an unrelated 1989 Weinberg article) if the title is not exact.  

**Fix**: Ensure the BibTeX entry with key `Weinberg1989` has the exact title “The cosmological constant problem”, journal “Rev. Mod. Phys.”, volume 61, pages 1–23 (or equivalent), and correct DOI. If a different Weinberg 1989 work is also cited, give it a distinct key to avoid any title/venue fusion.


## PAPER-PER-m1 – Planck cosmology numbers need explicit mapping to VI paper

**Location**: Abstract and Sec. I, statements like “$\Lambda$CDM model successfully accounts for observed cosmic acceleration…”, and later parameter values such as “$H_0 = 67.68\pm 1.06$, $\Delta N_{\rm eff}\approx 0$… from the companion” and the implicit use of Planck 2018 best-fit values.  

**Issue**: The canonical Planck cosmological-parameters paper quotes base-ΛCDM values around \(H_0 = 67.4 \pm 0.5\) km/s/Mpc, \(N_{\rm eff} = 2.99 \pm 0.17\), etc., and is “Planck 2018 results. VI. Cosmological parameters” (arXiv:1807.06209), with journal reference A&A 641 A6 (2020).[2] The manuscript’s wording implies direct inheritance from Planck but routes cosmology numbers through the companion MCMC paper; with the current citation key structure, there is room for confusion or accidental mis-attachment of the Planck 2018 title or ID to internal “Paper I(b)” fits.  

**Fix**: Make sure that any time Planck baseline cosmology is cited (even indirectly via the companion) the reference key points to arXiv:1807.06209 with the correct title and venue, and keep the companion-paper key distinct and clearly labeled (e.g. `Golden2026P1b`) so that Planck’s title and ID are never reused for the author’s own MCMC analysis.[2]


## PAPER-PER-m2 – Cai 2009 matter-bounce reference should be uniquely identified

**Location**: Abstract and Sec. I/Table 1, where “$\fnl = -35/8$ is a property of the matter-bounce class~\cite{Cai:2009fn}”.  

**Issue**: The key `Cai:2009fn` is standard for the well-known matter-bounce paper that derives \(\fnl = -35/8\), but arXiv hosts several Cai et al. 2009 bounce-related papers with similar titles; without an explicit arXiv ID and full title in the .bib file, there is a nontrivial risk of accidentally giving `Cai:2009fn` the title or journal metadata of a different Cai 2009 paper (e.g. on related bouncing scenarios), i.e. title–ID fusion.  

**Fix**: Confirm that `Cai:2009fn` in the bibliography corresponds to the specific paper that actually derives \(\fnl=-35/8\) for scalar matter bounce (with the correct arXiv number, title, author list, and journal reference) and not to a differently named Cai 2009 preprint. If multiple Cai 2009 bounce papers are cited, give each its own key and check titles and IDs against arXiv/ADS.


## PAPER-PER-n1 – Companion-paper keys risk metadata mixing

**Location**: Throughout, e.g. Abstract and Secs. I, II, III, where `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`, and `Golden2026supplement` are cited as companion works.  

**Issue**: These keys appear to refer to yet-unpublished or in-prep companion papers hosted in a GitHub repo, not arXiv. Because they resemble arXiv-style keys and some are adjacent to genuine arXiv citations, there is a realistic metadata-fusion risk in the .bib: an arXiv ID or journal field from an external paper could be accidentally attached to one of these internal keys (for example via copy–paste when adding `Golden2026P2`), making it look like an arXiv submission that does not actually exist.  

**Fix**: For each “Golden2026P*” entry, explicitly set `eprint`/`arXivId` fields to empty and use `note = "in preparation"` or a GitHub URL, and check that no arXiv ID or external journal info is attached. Keep these keys visually distinct from external arXiv keys (e.g. prefix with `Hubify-` or `GoldenComp-`) to reduce the chance of title/ID fusion.
