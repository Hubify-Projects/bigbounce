# P1B R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `arxiv/paper1b_mcmc_companion.tex` (v1B.0.3) + shared `arxiv/references.bib`.
**Version reviewed:** v1B.0.3 (2026-05-09 17:00 PDT).
**Scope:** Spot-check the 10–12 high-stakes bibitems flagged in the brief (Aghanim2020/Planck2018, Akrami2020/NPIPE, DESI DR2, Pantheon+, DES-SN5YR, Cobaya, CAMB, getdist, NaMaster/Alonso2019, Eskilt2022/Eskilt2022b, DiegoPalazuelos2025, Golden:2026P{1A,2,3,4} self-cites, recent 2024–2026 MCMC literature). Numbers verified against arXiv abstract pages and journal landing pages where reachable.
**Method:** WebFetch + WebSearch against arxiv.org / journal sites. Ten cite-keys traced end-to-end against authoritative sources; the rest hygiene-swept against the bib file.
**Date:** 2026-05-13 16:30 PT.

---

## TL;DR

- **Total findings: 8** — **1 BLOCKER, 3 MAJOR, 3 MINOR, 1 NIT.**
- **Most concerning citation error (one sentence):** P1B prose at L256 and L416 attributes "β = 0.30° ± 0.11° (Planck NPIPE)" to `\cite{Eskilt2022}`, but `Eskilt2022` in the shared bib resolves to Eskilt & Komatsu, *Improved Constraints from the WMAP and Planck CMB Polarization Data*, PRD **106**, 063503 (2022) / arXiv:**2205.13962**, which reports β = 0.342° ± 0.094° from a joint **WMAP+Planck** analysis — **not** the 0.30° ± 0.11° Planck-only NPIPE/PR4 value, which is from **Diego-Palazuelos, Eskilt, Minami, Tristram et al., "Cosmic Birefringence from Planck Data Release 4", PRL 128, 091302 (2022) / arXiv:2201.07682**. A reviewer who clicks through `Eskilt2022` to verify the 0.30° claim will find a different number and a different dataset combination; the citation chain is broken at the two places P1B quotes the Planck-NPIPE β.
- All other high-stakes refs verify clean against arXiv/journal records: Planck 2018 VI (1807.06209 → A&A 641, A6, 2020 ✓), DESI DR2 (2503.14738 → PRD 112, 083515, 2025 ✓ now published, not "preprint"), Cobaya (2005.05290 → JCAP 05 (2021) 057 ✓), Eskilt2022b alias (2205.13962 → PRD 106, 063503, 2022 ✓ — P1A tick-3 fix held), DiegoPalazuelos2025 (2509.13654 → ACT DR6 birefringence ✓), Liu et al. ECTorsionDESI2025 (2507.04265 → EPJ C 85:1351, 2025 ✓ now published, not "preprint"), Walmsley2022 (2102.08414 → MNRAS 509, 3966 ✓), Fujita2021 (2011.11894 → PRD 103, 043509 ✓), LiteBIRD2023 (2202.02773 → PTEP 2023, 042F01 ✓), Mercuri2006 (gr-qc/0601013 → PRD 73, 084016 ✓, P1A tick-3 title fix held).

---

## BLOCKERs

### B1. `\cite{Eskilt2022}` mis-targets the WMAP+Planck joint paper for the NPIPE-only 0.30°±0.11° value

- **Location:** `arxiv/paper1b_mcmc_companion.tex` L256 (Sec. IV "Data Methods: CMB E-B Analysis") and L416 (Sec. VI "Spectator-ALP Consistency Check", inverse-variance combination paragraph).
- **Claimed in prose:**
  ```latex
  Birefringence measurements are adopted from the published literature:
  $\beta = 0.30^\circ\pm 0.11^\circ$ (Planck NPIPE~\cite{Eskilt2022}) and
  $\beta = 0.215^\circ\pm 0.074^\circ$ (ACT~DR6~\cite{DiegoPalazuelos2025}).
  ```
  and again at L416 in the auxiliary inverse-variance combination.
- **What `Eskilt2022` actually resolves to (verified, sources below):**
  - `references.bib` L188–196 → Eskilt, J. R. and Komatsu, E., *"Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data"*, **Phys. Rev. D 106, 063503 (2022)**, arXiv:**2205.13962**, DOI 10.1103/PhysRevD.106.063503.
  - Verified headline value of that paper: **β = 0.342°⁺⁰·⁰⁹⁴ / ⁻⁰·⁰⁹¹ (3.6σ)** from a **joint WMAP + Planck** analysis. Source: arXiv abstract page for 2205.13962. This is also the value `Eskilt2022b` alias is built to cite (and which the P1B abstract and L87/L392/L424 correctly attribute to `\cite{Eskilt2022b}`).
- **What the 0.30° ± 0.11° NPIPE value actually comes from (verified):**
  - Diego-Palazuelos, P., Eskilt, J. R., Minami, Y., Tristram, M., Sullivan, R. M., Banday, A. J., Barreiro, R. B., Eriksen, H. K., Górski, K. M., Keskitalo, R., Komatsu, E., Martínez-González, E., Scott, D., Vielva, P., Wehus, I. K., *"Cosmic Birefringence from Planck Data Release 4"*, **Phys. Rev. Lett. 128, 091302 (2022)**, arXiv:**2201.07682**, DOI 10.1103/PhysRevLett.128.091302. Headline: **β = 0.30° ± 0.11° (68% C.L.)** from the Planck PR4 (NPIPE) full-sky data — the exact number P1B quotes.
  - A near-companion, Eskilt, J. R., *"Frequency-dependent constraints on cosmic birefringence from the LFI and HFI Planck Data Release 4"*, **A&A 662, A10 (2022)**, arXiv:2201.13347, reports β = 0.33° ± 0.10° (frequency-independent, full-sky); this is the *frequency-resolved* NPIPE follow-up by Eskilt alone, also distinct from 2205.13962.
- **What's wrong:**
  1. The 0.30° ± 0.11° value is **not in** PRD 106, 063503 / arXiv:2205.13962. That paper reports 0.342° ± 0.094° from WMAP+Planck. Quoting "0.30° ± 0.11°" and citing `Eskilt2022` is a verifiably false attribution.
  2. The parenthetical label "(Planck NPIPE)" is also wrong for `Eskilt2022` — the WMAP+Planck joint analysis uses Planck PR3 + WMAP9 cleaning; "NPIPE" specifically denotes Planck Data Release 4 / PR4, which is the dataset in arXiv:2201.07682 (Diego-Palazuelos et al.) and arXiv:2201.13347 (Eskilt 2022 A&A).
  3. The downstream inverse-variance combination at L420 (β_combined = 0.241° ± 0.061°, "3.9σ auxiliary cross-check") is computed from these two numbers; if a peer reviewer pulls 2205.13962 expecting 0.30° ± 0.11° they will find 0.342° ± 0.094° and conclude the combination is computed against the wrong inputs.
- **SSOT/upstream context:** The Wave 14-Z R42 P1-OA-M4 NaMaster methods paragraph (now mirrored in P1B Sec. IV) was added focused on the *pipeline* description; the citation-target check for the *numerical* β values quoted in the same paragraph was not part of that closure. P1A tick-3 fixed `Eskilt2022b` to alias the correct 2205.13962 (the 0.342° value), but the parallel fix — replacing `\cite{Eskilt2022}` with a proper PR4 reference at the two L256/L416 sites — was not performed.
- **Fix (preferred):** Add a new bibitem for the Planck PR4 NPIPE birefringence paper and re-cite it at L256 and L416:
  ```bibtex
  @article{DiegoPalazuelos2022,
      author  = {Diego-Palazuelos, P. and Eskilt, J. R. and Minami, Y. and Tristram, M. and Sullivan, R. M. and Banday, A. J. and Barreiro, R. B. and Eriksen, H. K. and G\'orski, K. M. and Keskitalo, R. and Komatsu, E. and Mart\'inez-Gonz\'alez, E. and Scott, D. and Vielva, P. and Wehus, I. K.},
      title   = {Cosmic Birefringence from {Planck} Data Release 4},
      journal = {Phys. Rev. Lett.},
      volume  = {128},
      pages   = {091302},
      year    = {2022},
      eprint  = {2201.07682},
      archivePrefix = {arXiv},
      doi     = {10.1103/PhysRevLett.128.091302}
  }
  ```
  Then at L256 and L416 replace `\cite{Eskilt2022}` with `\cite{DiegoPalazuelos2022}`. Leave `Eskilt2022` itself in the bib (it still backs the 0.342° headline elsewhere) and leave `Eskilt2022b` alone (the alias is correct and load-bearing for L87/L392/L424).
- **Fix (alternative, smaller diff):** If you do not want to add a new bibitem, retarget the prose itself to use the 0.342° ± 0.094° joint value at L256 and re-derive the combination at L420 (or drop the auxiliary combination entirely — it's already labeled "auxiliary cross-check only", and the headline number in the abstract is the 3.6σ joint value). But you must not leave a quote of "0.30° ± 0.11°" anywhere in the manuscript if `Eskilt2022` is the only citation, because the number does not appear in PRD 106 063503.
- **Priority:** BLOCKER. Two distinct prose locations where the cited paper does not contain the quoted number; the auxiliary 3.9σ figure is mechanically derived from these two mis-attributed inputs. A diligent peer reviewer pulls the cited paper and finds an immediate factual mismatch. This is the same class of error P1A tick-3 was opened to fix for the 0.342° / 2205.13962 mis-stitch — the parallel surface for the 0.30° / NPIPE / 2201.07682 case is still open in P1B.

---

## MAJORs

### M1. "Pantheon+" used as a dataset at L322 with no citation; canonical `Brout2022PantheonPlus` is in shared bib but unused in P1B

- **Location:** `arxiv/paper1b_mcmc_companion.tex` L320–325 (Sec. V "Cosmological Fits and Model Comparison", Sec. VA "Datasets and Configuration").
- **Claim in prose:**
  ```latex
  We analyze four dataset combinations: (1)~Planck 2018 NPIPE~\cite{Planck2018params};
  (2)~+DESI 2024 DR1 BAO~\cite{DESI2024}; (3)~+Pantheon+; (4)~+SH0ES $H_0$
  prior~\cite{Riess2022} + DES Y3 $S_8$~\cite{DES2024}.
  ```
  "Pantheon+" appears as a labeled dataset with **no citation**.
- **Verified canonical reference (present in shared bib, unused by P1B):**
  - `references.bib` L418–429 → `@article{Brout2022PantheonPlus, ...}` → Brout, D. et al., *"The Pantheon+ Analysis: Cosmological Constraints"*, **Astrophys. J. 938, 110 (2022)**, arXiv:**2202.04077**. Verified: this is the canonical Pantheon+ cosmology paper and is the standard cite for "Pantheon+" SN compilation in 2022+ cosmology analyses.
  - P1A tick-3 *added* `Brout2022PantheonPlus` to the shared bib specifically to close this kind of gap (per the brief). P1B does not yet cite it.
- **What's wrong:** Pantheon+ is a third-party data product — citing the dataset name in prose without backing it with the corresponding paper is the same class of issue as quoting Planck 2018 without `Planck2018params`. The reader has no anchor for which SN compilation is meant (Pantheon+ vs. Pantheon vs. JLA vs. Union3) and which selection cuts.
- **Fix:** Replace `(3)~+Pantheon+;` with `(3)~+Pantheon+~\cite{Brout2022PantheonPlus};`. Same one-character-class edit elsewhere if "Pantheon+" appears in other unflagged locations (a grep on the file shows L554 also mentions "Pantheon+" in the "Forward" paragraph — same fix recommended there).
- **Priority:** MAJOR. Named dataset without a citation in the Datasets and Configuration section is a routine peer-review red flag, and the fix is a 1-line addition with the canonical bibitem already in-tree.

### M2. "DES Y5" mentioned at L234 with no citation; canonical `DES2024SN5YR` is in shared bib but unused in P1B

- **Location:** `arxiv/paper1b_mcmc_companion.tex` L233–236 (Sec. III "Stock-CAMB ΛCDM+ΔNeff MCMC", independent cross-validation paragraph).
- **Claim in prose:**
  ```latex
  Liu~\etal~\cite{ECTorsionDESI2025} constrained an EC torsion model using
  DESI~DR2 + PantheonPlus + DES~Y5 + Planck~2018, finding torsion preferred
  by AIC ($\Delta\text{AIC}=-5.7$ to $-6.6$).
  ```
  "DES Y5" appears as a named dataset with no citation. "DESI DR2" in this paragraph also has no inline cite; the canonical `DESI2025DR2` is used elsewhere (L514, L558) and would belong here too. "PantheonPlus" is the same issue as M1.
- **Verified canonical reference (present in shared bib, unused by P1B):**
  - `references.bib` L431–442 → `@article{DES2024SN5YR, ...}` → DES Collaboration (Abbott et al.), *"The Dark Energy Survey: Cosmology results with ~1500 new high-redshift Type Ia supernovae using the full 5-yr data set"*, **Astrophys. J. Lett. 973, L14 (2024)**, arXiv:**2401.02929**. Verified canonical 2024 DES-SN5YR cosmology paper.
- **What's wrong:** Same class as M1 — the cross-validation paragraph leans on three external dataset names (DESI DR2, Pantheon+, DES Y5) and cites zero of them. The reader cannot pull the data anchors to check whether Liu et al.'s combination matches what P1B's own MCMC consumes.
- **Fix:** Rewrite L234 as:
  ```latex
  Liu~\etal~\cite{ECTorsionDESI2025} constrained an EC torsion model using
  DESI~DR2~\cite{DESI2025DR2} + Pantheon+~\cite{Brout2022PantheonPlus} +
  DES~Y5~\cite{DES2024SN5YR} + Planck~2018~\cite{Planck2018params}, finding
  torsion preferred by AIC ($\Delta\text{AIC}=-5.7$ to $-6.6$).
  ```
  All four bibitems are already in the shared `references.bib`.
- **Priority:** MAJOR. Three uncited named datasets in a single comparison sentence. Mechanical fix.

### M3. L321 calls the Planck dataset "Planck 2018 NPIPE" — internally contradictory; cite is `Planck2018params` (PR3) but "NPIPE" denotes PR4 (Akrami2020); also L181 invokes "NPIPE CamSpec TTTEEE" without an NPIPE citation

- **Location:** L181 (Sec. III "Stock-CAMB ΛCDM+ΔNeff MCMC", scope paragraph) and L321 (Sec. VA "Datasets and Configuration", dataset list item 1).
- **Claims in prose:**
  - L181: "The proxy run (Cobaya~v3.6.1 with **Planck NPIPE CamSpec TTTEEE** + lowl TT/EE + lensing) ..."
  - L321: "(1)~Planck 2018 NPIPE~\cite{Planck2018params};"
- **What `Planck2018params` is (verified):**
  - `references.bib` L162–170 → Planck Collaboration (Aghanim, N. et al.), *"Planck 2018 results. VI. Cosmological parameters"*, **A&A 641, A6 (2020)**, arXiv:**1807.06209**. Verified against arXiv abstract page. **This is the Planck 2018 / PR3 cosmology paper, not NPIPE.**
- **What NPIPE actually denotes (verified):**
  - Planck Collaboration (Akrami et al.), *"Planck intermediate results. LVII. Joint Planck LFI and HFI data processing"*, **A&A 643, A42 (2020)**, arXiv:**2007.04997**, DOI 10.1051/0004-6361/202038073. NPIPE = Planck PR4 = the 2020 reprocessing pipeline described in this paper. It supersedes PR3 (2018 / `Planck2018params`).
- **What's wrong:**
  1. "Planck 2018 NPIPE" is self-contradictory at the dataset-naming level. PR3 (2018) and PR4 (NPIPE, 2020) are different reprocessings of the same survey, with different mission durations included in the LFI-HFI joint solution and different noise/calibration. The literature does not call PR3 "NPIPE".
  2. If the actual MCMC chains consume CamSpec TTTEEE on top of PR3 likelihoods (the typical PR3 chain), `Planck2018params` is the right cite and the word "NPIPE" should be dropped from L181 and L321.
  3. If the chains actually consume the NPIPE PR4 likelihoods (which is what L181's "Planck NPIPE CamSpec TTTEEE" phrasing suggests), `Planck2018params` is the wrong cite — the NPIPE paper Akrami et al. 2020 (arXiv:2007.04997, A&A 643 A42) is the canonical reference, and the CamSpec TTTEEE pipeline running on NPIPE inputs would additionally want the Efstathiou & Gratton CamSpec paper (Open J. Astrophys. 4, 2021, arXiv:1910.00483) — not currently in the bib.
- **SSOT context:** This is a dataset-vintage question that affects which Planck likelihood is being claimed. The SSOT (`project-context/SSOT/paper-1/status.md`) records the analysis as Planck PR4/NPIPE elsewhere ("Wave 14-Z P1-OA-M4 methods paragraph" describes the NaMaster pipeline on the *Commander* foreground-cleaned PR3 map, while the MCMC headline section in P1B uses "NPIPE CamSpec TTTEEE"). The fix needs the author (Houston) to resolve which likelihood is actually consumed by the frozen Cobaya runs whose chain files are in `reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/`, then pick one citation strategy.
- **Fix (two options):**
  - **(a) If the chains use PR3:** Drop "NPIPE" from L181 (rewrite as "Planck 2018 PR3 CamSpec TTTEEE") and from L321 (rewrite as "Planck 2018~\cite{Planck2018params}"). `Planck2018params` stays.
  - **(b) If the chains use PR4/NPIPE:** Add `Akrami2020` (arXiv:2007.04997) and the CamSpec methodology paper to the bib, replace `\cite{Planck2018params}` at L321 with `\cite{Akrami2020,EfstathiouGratton2021}`, and add the same cite at L181 right after "Planck NPIPE CamSpec TTTEEE".
- **Priority:** MAJOR. Dataset-vintage misnaming is a class of error that *can* be caught by a careful reader and undermines the rigor presentation. The fix is small but requires Houston to confirm which Planck likelihood the frozen chains actually consume.

---

## MINORs

### m1. `DESI2024` bibitem in shared bib is journal-incomplete: still tagged `journal = "arXiv preprint"` despite the paper being published

- **Location:** `references.bib` L278–286.
- **Current bibitem:**
  ```bibtex
  @article{DESI2024,
    author  = {{DESI Collaboration} and Adame, A. G. and others},
    title   = {{DESI} 2024 {VI:} Cosmological constraints from the measurements of baryon acoustic oscillations},
    journal = {arXiv preprint},
    year    = {2024},
    eprint  = {2404.03002},
    archivePrefix = {arXiv},
    primaryClass  = {astro-ph.CO}
  }
  ```
- **What's wrong:** As of 2025, DESI DR1 BAO Paper VI (arXiv:2404.03002) has been finalized and the JCAP version is available; tagging it as "arXiv preprint" is stale. The same shape of issue was fixed in the parallel `DESI2025DR2` bibitem (now lists Phys. Rev. D 112, 083515).
- **Fix:** Update `DESI2024` to the JCAP volume/year (verify the JCAP issue against the arXiv journal-ref before committing; I did not pull the JCAP landing page here).
- **Priority:** MINOR. Backward-compatibility — citation still resolves correctly via arXiv, the only loss is journal-completeness.

### m2. `ECTorsionDESI2025` bibitem still tagged `journal = "European Physical Journal C"` with no volume/pages despite paper now being EPJ C 85:1351

- **Location:** `references.bib` L557–565 (Liu et al., torsion cosmology in light of DESI/SN/CMB).
- **Current bibitem:**
  ```bibtex
  @article{ECTorsionDESI2025,
    author  = {Liu, Tonghua and ... and Wang, Jieci},
    title   = {Torsion cosmology in the light of {DESI}, supernovae and {CMB} observational constraints},
    journal = {European Physical Journal C},
    year    = {2025},
    eprint  = {2507.04265},
    ...
  }
  ```
- **Verified upgrade:** arXiv:2507.04265 is now **EPJ C 85:1351 (2025)**, DOI 10.1140/epjc/s10052-025-15090-0 (verified via arXiv abstract page journal-ref).
- **Fix:** Add `volume = {85}`, `pages = {1351}`, `doi = {10.1140/epjc/s10052-025-15090-0}`.
- **Priority:** MINOR.

### m3. `DiegoPalazuelos2025` bibitem still labeled `journal = "arXiv preprint"` despite paper now accepted at PRD

- **Location:** `references.bib` L444–452.
- **Current bibitem:**
  ```bibtex
  @article{DiegoPalazuelos2025,
    author  = {Diego-Palazuelos, P. and Komatsu, E.},
    title   = {Cosmic birefringence from the {Atacama Cosmology Telescope} Data Release 6},
    journal = {arXiv preprint},
    year    = {2025},
    eprint  = {2509.13654},
    ...
  }
  ```
- **Verified upgrade:** arXiv:2509.13654 is "accepted for publication" in PRD per the arXiv abstract page (submitted 2025-09-17, revised 2026-04-14). Journal volume/pages not yet assigned per the arXiv record I pulled, so the safe edit is to swap `journal = "arXiv preprint"` for `journal = {Phys. Rev. D (accepted)}` and re-check the journal-ref field after the next arXiv version. If the user wants to wait for the assigned volume/article number, leave a NOTE.
- **Fix:** Update `journal` to `{Phys. Rev. D (accepted)}` or follow up after the next arXiv version stamp.
- **Priority:** MINOR.

---

## NITs

### n1. P1B does not cite `Alonso2019` (NaMaster pseudo-Cℓ framework) despite Sec. IV being a NaMaster-pipeline methods paragraph

- **Location:** `arxiv/paper1b_mcmc_companion.tex` L260–311 (Sec. IV "Data Methods: CMB E-B Analysis"), which describes the NaMaster pipeline in ~50 lines of methodological prose (NmtField, purify_b, NmtWorkspace.compute_coupling_matrix, band-power binning).
- **Verified canonical reference (present in shared bib, unused by P1B):** `references.bib` L884–892 → Alonso, Sanchez, Slosar (LSST DESC), *"A unified pseudo-Cℓ framework"*, **MNRAS 484, 4127 (2019)**, arXiv:**1809.09603**. P1A Wave 14-Z added this entry specifically to close the parallel R42 P1-OA-M4 NaMaster MAJOR for Paper 1A.
- **What's wrong:** The methods paragraph names every NaMaster API call (NmtField, NmtWorkspace, purify_b) without citing the NaMaster framework paper. This was the exact gap closed in P1A Wave 14-Z. The parallel fix in P1B has not landed.
- **Fix:** Add `\cite{Alonso2019}` at L262 ("We use NaMaster's spin-2 ...") and again at L280 ("NaMaster's NmtWorkspace.compute_coupling_matrix"). Two citation insertions, same bibitem.
- **Priority:** NIT (low cost, high consistency value across the P1A/P1B pair).

---

## Counts and ranking

- **Total findings: 8.** BLOCKER × 1, MAJOR × 3, MINOR × 3, NIT × 1.
- **The single most concerning citation error:** **B1.** Quoting "β = 0.30° ± 0.11° (Planck NPIPE)" while citing `Eskilt2022` is a verifiably false attribution — the cited paper (PRD 106, 063503 / arXiv:2205.13962) is WMAP+Planck and reports 0.342° ± 0.094°, not 0.30°. The NPIPE 0.30° figure is from Diego-Palazuelos et al. PRL 128, 091302 (arXiv:2201.07682). This fires twice in the manuscript (L256 and L416) and propagates into the auxiliary 3.9σ inverse-variance combination at L420.

## Verified-clean (no findings)

- `Planck2018params` → A&A 641, A6 (2020) / arXiv:1807.06209. ✓
- `DESI2025DR2` → Phys. Rev. D 112, 083515 (2025) / arXiv:2503.14738 — now published, ✓.
- `Cobaya2021` → JCAP 05 (2021) 057 / arXiv:2005.05290. ✓
- `Eskilt2022b` (alias of Eskilt2022) → PRD 106, 063503 (2022) / arXiv:2205.13962, headline 0.342° ± 0.094°. P1A tick-3 fix held. ✓
- `Mercuri2006` → PRD 73, 084016 (2006) / arXiv:gr-qc/0601013. P1A tick-3 title fix held. ✓
- `Walmsley2022` → MNRAS 509, 3966 (2022) / arXiv:2102.08414. ✓
- `Fujita2021` → PRD 103, 043509 (2021) / arXiv:2011.11894. ✓
- `LiteBIRD2023` → PTEP 2023, 042F01 (2023) / arXiv:2202.02773. ✓
- `Riess2022` → ApJL 934, L7 (2022) / arXiv:2112.04510. ✓
- `Golden2026P{1a,1b,2,3,4}` all present at `references.bib` L971–1007 as `journal = "(in preparation)"` companion stubs, all five cite-keys used in P1B resolve. No orphans. ✓

---

## Sources (verified URLs pulled during this review)

- [arXiv:2205.13962 — Eskilt & Komatsu, PRD 106 063503 (β = 0.342° joint WMAP+Planck)](https://arxiv.org/abs/2205.13962)
- [arXiv:2201.07682 — Diego-Palazuelos, Eskilt, Minami, Tristram et al., PRL 128 091302 (β = 0.30° NPIPE / Planck PR4)](https://arxiv.org/abs/2201.07682)
- [arXiv:2201.13347 — Eskilt 2022, A&A 662 A10 (frequency-dependent NPIPE)](https://arxiv.org/abs/2201.13347)
- [arXiv:2509.13654 — Diego-Palazuelos & Komatsu, ACT DR6 birefringence (accepted PRD)](https://arxiv.org/abs/2509.13654)
- [arXiv:2503.14738 — DESI Collaboration, DESI DR2 Results II, PRD 112 083515 (2025)](https://arxiv.org/abs/2503.14738)
- [arXiv:2507.04265 — Liu, Li, Xu, Biesiada, Wang, EPJ C 85:1351 (2025)](https://arxiv.org/abs/2507.04265)
- [arXiv:2005.05290 — Torrado & Lewis, Cobaya, JCAP 05 (2021) 057](https://arxiv.org/abs/2005.05290)
- [arXiv:1807.06209 — Planck 2018 VI, A&A 641 A6 (2020)](https://arxiv.org/abs/1807.06209)
- [arXiv:2007.04997 — Akrami et al., Planck intermediate LVII NPIPE, A&A 643 A42 (2020)](https://arxiv.org/abs/2007.04997)
