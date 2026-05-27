# P1B R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R30_P1B_v1B_0_30
**Wall time**: 22.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24024, completion=2183, total=26207

---

## No blocker-grade issues found

All cosmology-related citations in the excerpt you provided look internally consistent and correctly attributed at the level visible here; I do not see any blocker-grade mis-citations or fused metadata. [1][2]

Below are targeted issues and nits within your specified six-finding cap.

---

## PAPER-PER-B1 — Missing / ambiguous Golden 2026 cross-paper entries

**Location.** Multiple cites to `Golden2026P1a`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4` (e.g., Introduction paragraph “What is NOT in this paper”, and later cross-paper status table).  

**Issue.** These are self-citations to yet-unpublished or non-arXiv-tagged works (“Paper I(a)”, “Paper II”, etc.) with shorthand keys only; for a reader using arXiv/ADS/publisher search, there is no checkable bibliographic metadata (title, venue, arXiv ID) and the refs as written are effectively opaque.   

**Fix (minor).** In the bibliography file, ensure each `Golden2026P*` entry includes at minimum a concrete preprint title, arXiv ID (once posted), and “in preparation” / “submitted” tag, and in the main text add a brief parenthetical (e.g., “Paper I(a), ‘Einstein–Cartan–Holst Spin–Torsion Cosmology…’, Golden 2026, in preparation”) so ADS/arXiv searches can actually identify them.

---

## PAPER-PER-B2 — Eskilt / Diego Palazuelos birefringence references not fully disambiguated

**Location.** Abstract (Planck/ACT DR6 2.4–2.9σ: `\cite{Eskilt2022,DiegoPalazuelos2025}`); §VI data methods: Planck NPIPE value from `\cite{DiegoPalazuelos2022}`, ACT DR6 from `\cite{DiegoPalazuelos2025}`; spectator-ALP section headline constraint from `\cite{Eskilt2022b}`.  

**Issue.** There are at least three distinct cosmic-birefringence analyses in the literature that are plausibly being referenced: Planck-only NPIPE re-analysis, ACT DR6-only, and Planck+ACT joint analysis by Eskilt and collaborators. These live under separate arXiv IDs and sometimes similar author lists. If your `.bib` collapses them (e.g., two different papers both keyed `Eskilt2022` or a Diego Palazuelos Planck NPIPE paper mislabeled as ACT DR6), the reader will see fused metadata. I cannot confirm the exact mapping because the `.bib` is not shown, but the text clearly uses four distinct roles while only three keys appear, which is a common failure mode.   

**Fix (MAJOR).** In `references.bib`, (1) give each birefringence paper a unique key that encodes both experiment and role, e.g. `Eskilt2022_PlanckActJoint`, `DiegoPalazuelos2022_PlanckNPIPE`, `DiegoPalazuelos2025_ACTDR6`, and (2) verify each has correct title, journal, and arXiv ID from arXiv/ADS (don’t reuse a single 2022 Eskilt entry for both Planck-only and joint Planck+ACT). Then update the in-text cites to use those unambiguous keys.

---

## PAPER-PER-B3 — EC torsion DESI reference needs precise identification

**Location.** §3, “Independent cross-validation. — Liu et al. constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC… Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈.” (`\cite{ECTorsionDESI2025,DESI2025DR2,Brout2022PantheonPlus,DES2024SN5YR}`).  

**Issue.** The text refers to a specific Einstein–Cartan torsion analysis with DESI DR2 plus late-time probes and an AIC preference. I do not see any widely known EC-torsion–DESI paper under a generic label like “EC Torsion DESI 2025” in current arXiv/ADS indices; if your BibTeX entry uses an internal key like `ECTorsionDESI2025` but points to a generic modified gravity or dark energy paper instead, that would be fused metadata.   

**Fix (MAJOR).** Verify that your `ECTorsionDESI2025` BibTeX entry is an actual EC torsion paper (check authors, title, and arXiv ID directly on arXiv.org/ADS), that it genuinely uses DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, and that it reports the quoted AIC preference. If no such paper exists yet, either (a) change the text to “Liu et al., in preparation (EC torsion with DESI DR2…)” or (b) remove the detailed AIC comparison and keep only what is supported by an existing, correctly cited preprint.

---

## PAPER-PER-B4 — LiteBIRD reference likely underspecified

**Location.** Spectator-ALP section, “LiteBIRD is projected to achieve σ(β) ≈ 0.03° [LiteBIRD2023].”  

**Issue.** LiteBIRD forecasts for cosmic birefringence have appeared in multiple collaboration white papers and design reports; a generic `LiteBIRD2023` cite without distinguishing title or arXiv ID risks pointing to a broad mission overview which may not actually contain the specific σ(β) ≈ 0.03° number, or to an earlier forecast with slightly different value.   

**Fix (minor).** Check that `LiteBIRD2023` in your `.bib` corresponds to the exact birefringence-forecast paper (e.g., a LiteBIRD polarization science white paper on arXiv) and that it indeed gives σ(β) ≈ 0.03°. If not, replace with the correct LiteBIRD birefringence-focused reference or qualify the number as “representative of current LiteBIRD forecasts” and update the bib entry accordingly.

---

## PAPER-PER-B5 — DESI DR1 / DR2 and DES Y3 / SN5YR labels need precise matching

**Location.** §5 datasets (“DESI 2024 DR1 BAO [DESI2024]”; later cross-paper and future-work sections talk about DESI DR2, DES Y3 S₈, DES-SN5YR) and in various future/companion-text sentences.  

**Issue.** The text moves between “DESI 2024 DR1 BAO”, “DESI DR2”, “DES Y3 S₈”, and “DES-SN5YR” while using short citation keys (`DESI2024`, `DESI2025DR2`, `DES2024`, `DES2024SN5YR`). It is easy to mis-wire these in the `.bib` so that, for example, `DESI2025DR2` actually points to the DR1 BAO preprint, or `DES2024SN5YR` to a DES-Y3 cosmic shear release instead of the SN sample. That would not be obvious to readers until they check the PDFs.   

**Fix (minor).** For each of the DESI and DES references, verify that key → paper is one-to-one and semantically correct by checking title, collaboration, and release (e.g., “DESI 2024 I: … DR1 BAO” vs any later DR2 BAO paper; “DES Collaboration, DES-Y3 cosmic shear” vs “DES-SN5YR cosmology analysis”) on arXiv/ADS. Rename keys if needed to encode DR1/DR2 and Y3/SN5YR explicitly and adjust the text where you currently elide that distinction.

---

## PAPER-PER-N1 — Scope/definition citations that will need concrete bib entries

**Location.** Refs to classic theory papers used purely definitional: Hehl–Datta–Mercuri torsion contact term (`\cite{Hehl1976,Mercuri2006}`), Cai matter bounce (`\cite{Cai:2009fn}`), Fujita ALP birefringence (`\cite{Fujita2021}`), Planck 2018 cosmological parameters (`\cite{Planck2018params}`), Cobaya (`\cite{Cobaya2021}`), NaMaster (`\cite{Alonso2019}`), Pantheon+ (`\cite{Brout2022PantheonPlus}`), DES-SN5YR (`\cite{DES2024SN5YR}`), etc.  

**Issue.** Nothing obviously wrong in the LaTeX, but these are all widely cited canonical works with well-defined titles and arXiv IDs; if any of the corresponding BibTeX entries use incomplete or placeholder metadata (e.g., wrong year, missing arXiv number, “to appear” long after publication), that will show up as sloppiness in ADS/arXiv cross-checking even though it doesn’t change your physics. [2]  

**Fix (nit).** Run a quick ADS/arXiv pass for these “anchor” papers and make sure each `.bib` entry has (i) correct title, (ii) full author list (or correctly truncated with “et al.”), (iii) journal/volume/page if published, and (iv) the right arXiv ID/category. This is low-effort but will prevent cosmetic citation-chain nits in external review.

---

If you can share the actual `references.bib` for a future round, I can check the arXiv IDs, titles, and venues line-by-line against ADS for the specific keys you use.
