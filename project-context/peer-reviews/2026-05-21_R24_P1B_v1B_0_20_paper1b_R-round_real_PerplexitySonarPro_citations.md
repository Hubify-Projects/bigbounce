# paper1b R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R24_P1B_v1B_0_20
**Wall time**: 17.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=19203, completion=1541, total=20744

---

## Finding 1 — PAPER-PER-B1 (MAJOR)

The bibliography key `\cite{ECTorsionDESI2025}` is used for “Liu et al. constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6).”[1]  
There is no evidence on arXiv/ADS or major publishers of a 2025 cosmology paper matching this description by any Liu et al.; the combination “EC torsion + DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018” with those AIC values appears to be internal/unpublished, not a citable external paper.[1]

**Fix:** Either (a) replace `\cite{ECTorsionDESI2025}` with a real, published arXiv or journal reference that actually reports an EC torsion fit with those datasets and AIC numbers, or (b) explicitly relabel this as an internal analysis (no external citation) and remove the fabricated reference entry from the BibTeX file.

---

## Finding 2 — PAPER-PER-B2 (BLOCKER)

The citation sequence `\cite{Eskilt2022,DiegoPalazuelos2025}` is used for “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ.” in the abstract, and `\cite{Eskilt2022b}` is used later for “published joint Planck+ACT value β = 0.342° ± 0.094° (3.6σ).”[1]  
On arXiv/ADS, the established Planck cosmic-birefringence paper is Eskilt & Komatsu (2020/2021, Planck-only, ∼2.5–3σ), and ACT DR6 EB analyses appear under different author lists; the specific trio of labels “Eskilt 2022 / Eskilt 2022b / Diego Palazuelos 2025” plus exactly these significances looks like fused, forward-dated metadata rather than verifiable published papers with those years, titles, and DR6 joint combination.[1]

**Fix:** Re-audit the bibliography against arXiv/ADS:  
- Map each of `Eskilt2022`, `Eskilt2022b`, and `DiegoPalazuelos2025` to a real arXiv ID and correct journal reference (title, author list, year, and whether Planck-only vs ACT vs joint).  
- Update the text to match the actual reported σ values and dataset combinations; drop “DR6 joint” / 3.6σ language unless there is a published paper explicitly giving β = 0.342° ± 0.094° at 3.6σ with shared-calibration treatment.

---

## Finding 3 — PAPER-PER-B3 (MAJOR)

Throughout the NaMaster section and abstract, the ACT DR6 analysis is attributed as “ACT DR6” with a 0.215° ± 0.074° value and cited as `\cite{DiegoPalazuelos2025}`, but a search shows no 2025 arXiv paper with that author-year combination and that exact β measurement for DR6; it appears to be a forward-dated placeholder based on internal or projected ACT results, not a current published paper.[1]  
This breaks the paper’s verification mission: the claimed external “primary observational evidence” and the specific β and σ values cannot be tied to an identifiable, citable paper.

**Fix:** Verify against the actual ACT EB cosmic-birefringence release that is currently on arXiv/ADS (check title, collaboration name, lead author, year, β value and error bar); then rename the citation key, authors, and year to match that publication, and update the numbers in the text to the published β ± σ. If no DR6 release with those numbers exists yet, relabel these as “internal forecast / private communication” and remove them from the “published” category.

---

## Finding 4 — PAPER-PER-B4 (MAJOR)

The DESI DR2 cosmology reference is given as `\cite{DESI2025DR2}` and described as “DESI DR2” already providing a quintom-B–like signal and used as an “empirical anchor” in 2026.[1]  
Public DESI BAO cosmology papers currently correspond to DR1 / early DR2 schedules with different years; there is at present no verifiable 2025 DESI DR2 cosmology paper with that exact label, and the text’s phrasing suggests a specific published analysis rather than “forthcoming / in preparation” documentation.[1]

**Fix:** Point `DESI2025DR2` to the latest publicly released DESI BAO/cosmology paper actually on arXiv (correct title, collaboration, year, DR label), and adjust the text so that any use of DR2-specific w₀–wₐ constraints explicitly matches what that paper reports. If the DR2 chain is based on internal DESI data not yet public, rephrase as “internal DESI DR2 chains (not yet public)” and remove them from the list of “published” references.

---

## Finding 5 — PAPER-PER-B5 (minor)

The paper cites “LiteBIRD is projected to achieve σ(β) ≈ 0.03°” as `\cite{LiteBIRD2023}` but does not specify which LiteBIRD collaboration white paper / science goals document this is referring to; there are multiple LiteBIRD technical and science papers with different years and arXiv IDs.[1]  
Without a precise mapping, a reader cannot easily confirm that 0.03° is the forecast in the cited document.

**Fix:** Replace `LiteBIRD2023` with the exact LiteBIRD science paper or white paper that publishes the σ(β) forecast (use its correct arXiv ID, title, year, and collaboration name), and, if needed, adjust the 0.03° figure to match the quoted forecast for the appropriate configuration.

---

## Finding 6 — PAPER-PER-B6 (nit)

Several cross-paper self-citations `\cite{Golden2026P1a,Golden2026P2,Golden2026P3,Golden2026P4}` are used as if they were arXiv-submitted or journal-published, but the preamble only states “Houston Golden – 2026, arXiv submission: astro-ph.CO / gr-qc” without concrete arXiv identifiers, volumes, or DOIs.[1]  
This makes it impossible for an external referee to verify those documents or check that tables and constraints cited from them actually exist as public papers.

**Fix:** Once P1(a)–P4 are on arXiv, replace each Golden2026* key with the actual arXiv ID and full reference (title, year, version); until then, clearly label them as “companion manuscripts in preparation (not yet public)” and avoid wording that implies they are already citable arXiv or journal publications.
