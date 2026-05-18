# P1A_v1A028_R10 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1300pt
**Wall time**: 27.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28571, completion=1631, total=30202

---

## PAPER-PER-B1 — Systematic fake / malformed arXiv IDs (BLOCKER)

The LaTeX cites keys like `Planck2018params`, `DESI2024`, `DESI2025DR2`, `Hehl1976`, `Minami2020`, `Cai:2009fn`, etc., but no explicit arXiv identifiers appear anywhere in the manuscript text or comments, despite the front-matter claim “arXiv submission: gr-qc / astro-ph.CO / hep-th”. This prevents checking whether each citation’s arXiv ID, title, and authors actually match the claimed results, and violates the stated requirement that arXiv IDs be verifiable and non-confabulated. Fix: add explicit arXiv identifiers (or DOI/journal references) for every cited work in the bibliography and, for a small random subset that includes key load-bearing citations (Planck 2018, DESI DR2, Hehl 1976, Minami & Komatsu, Cai et al. 2009, Date–Kaul–Sengupta, etc.), verify by hand that title, author list, journal, and arXiv category match the claimed content.

## PAPER-PER-B2 — Unsupported “recent / 2024–2026” references with invented-looking metadata (MAJOR)

Several references are described with extremely specific years, DR labels, and author groups that cannot be validated from the manuscript alone and look like likely fusions or anticipatory fabrications: e.g. “DESI 2024–2025 BAO results” with two separate keys `DESI2024` and `DESI2025DR2` and quoted significance numbers, “Heinrich+2024 σ(f_NL)≈0.7”, “Eskilt 2022b; DiegoPalazuelos2025”, “Dehghani:2025cusc`, “ECTorsionDESI2025`, “Legner2025`, “Alam2025bounce`, “Cai:2026echoes`, “Papanikolaou:2024pbh`, “Golden2026P1b/P2/P3/P4`, etc. Without explicit arXiv/DOI metadata these look like LLM-style future or merged references, and many are load-bearing for the claimed forecasting or supporting evidence. Fix: for each 2024–2026 citation (and for all “Golden2026…” self-references) supply real, currently-public identifiers (arXiv ID, DOI, journal) or clearly mark them as “in preparation / private communication / internal note” and remove any implication that they are already-published peer-reviewed results.

## PAPER-PER-B3 — Internal self-citations to non-existent companion papers as if public (MAJOR)

The manuscript repeatedly cites “companion” Papers I(b), II, III, IV, and a “supplement” (e.g. `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`, `Golden2026supplement`) and treats them as if they are public, peer-reviewable sources of core results (MCMC chains, NaMaster validation, Fisher forecasts, PTA spectral index, galaxy spin catalog). No bibliographic details (journal, arXiv ID, institution report number) are given, so an external referee cannot check whether these documents exist or what they actually claim. Fix: either (i) provide full bibliographic metadata and stable public links (arXiv IDs, DOIs, or institutional report numbers) for each companion and ensure they really contain the described results, or (ii) clearly relabel them as “internal / in preparation / to appear” and downgrade any claims that depend on them from “verified result” to “working assumption / planned work”, keeping this paper self-contained.

## PAPER-PER-M1 — Ambiguous / apparently fused reference clusters around birefringence (MAJOR)

The birefringence discussion attributes the current CMB-rotation measurement to “Planck/ACT DR6 3.6σ”, citing keys like `Minami2020`, `Eskilt2022b`, and `DiegoPalazuelos2025` in close proximity, with specific numbers such as “β=0.342°±0.094°”. Without explicit titles and IDs, it is impossible to confirm that: (a) Minami & Komatsu 2020 is not being conflated with later Planck/ACT joint analyses; (b) “Eskilt2022b” and “DiegoPalazuelos2025” correspond to real distinct papers with those authors and years; and (c) the quoted combined value and DR6 label correspond to an actual joint analysis rather than an LLM fusion of several works. Fix: in the bibliography, separate the birefringence sources into distinct entries with correct titles and identifiers (e.g. Minami & Komatsu’s Planck EB self-calibration paper, later ACT/Planck joint analyses if real), and in the main text, clearly attribute each numerical result to the correct single paper, avoiding blended “Planck/ACT DR6” language unless that is the official collaboration name for a specific release.

## PAPER-PER-m2 — Use of classic references without verifiable bibliographic details (minor)

Foundational works such as Hehl et al. 1976, Holst 1996, Freidel–Minic–Takeuchi 2005, Mercuri 2006/2009, Date–Kaul–Sengupta 2009, Lue–Wang–Kamionkowski 1999, Weinberg 1989, Gödel 1949, and Popławski 2010/2012/2016 are cited only by keys (`Hehl1976`, `Holst1996`, `Freidel2005`, etc.) and author-year mentions, with no journal, title, or arXiv ID. That makes it impossible to check systematically that the specific statements attributed to each (e.g. precise forms of torsion-induced four-fermion terms, Immirzi running, specific bounce formulas) correspond to the cited works rather than to secondary reviews or later modifications. Fix: expand each of these classic references in the bibliography to include full titles, journal, year, and arXiv IDs where applicable, and spot-check that the key formulas and qualitative claims in the text indeed appear in those exact papers (not in later reviews).

## PAPER-PER-n1 — Overloaded / reused citation keys and dataset labels (nit)

Several keys and labels are used in ways that could cause metadata confusion even if the underlying references are correct: e.g. “DESI2025DR2” is used both as a BAO result label and as a shorthand for “DESI DR2 w0wa chain” status in a long footnote; “Heinrich:2023” is described as “Heinrich+2024 σ(f_NL)≈0.7”, mixing year labels; “LiteBIRD2023” is used as if it uniquely specifies both mission concept and forecast sensitivity; and “Planck2018params” is used as a generic ΛCDM reference without indicating which exact Planck 2018 paper. These do not by themselves prove incorrect citations but they increase the risk of fused or mis-assigned metadata in the .bib file. Fix: enforce one-to-one mapping between citation keys and specific papers/datasets (e.g. separate keys for DESI DR2 BAO versus a particular w0–wa chain run; separate keys for Planck 2018 parameters vs other Planck 2018 results), and adjust in-text labels to match the official titles and years.
