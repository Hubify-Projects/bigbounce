# P1A R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.19) + `arxiv/references.bib` (shared bib).
**Scope:** Spot-check the 11 high-stakes bibitems flagged in the prompt (Holst1996, Mercuri2006, Freidel2005, LueWangKamionkowski1999, Alexander:2009tp, Eskilt2022b, Planck2018params, DESI2025DR2, Pantheon+, DES-SN5YR, Golden2026P{1b,2,3,4} cross-paper self-cites), plus opportunistic hygiene sweeps on neighboring entries (Liu2025, ECTorsionDESI2025, SPIDER2025, Legner2025, DiegoPalazuelos2025, Yin2026, Alam2025bounce). The shared bibfile was previously audited at the P2 R-round (2026-05-13 13:30 PT); findings here are P1A-specific or new.
**Method:** WebFetch against `arxiv.org` abstract pages; cross-check against journal landing pages via DOI; spot-check, not exhaustive. WebSearch used for verification when arXiv didn't fully resolve. Sources inline per finding.
**Date:** 2026-05-13 15:30 PT.

---

## TL;DR

- **Total findings: 8** — **1 BLOCKER, 3 MAJOR, 3 MINOR, 1 NIT.**
- **Most concerning citation error (one sentence):** The `Eskilt2022b` bibitem flagged in the prompt as "v1.7.27-aligned (with P2 update)" is **still broken in the shared bib** — it welds the headline value $\beta = 0.342^\circ \pm 0.094^\circ$ (from Eskilt & Komatsu 2022, PRD 106 063503, arXiv:2205.13962) onto a different paper's metadata (Cosmoglobe DR1 II, A&A 679, A144, arXiv:2305.02268, whose actual headline is $\beta = 0.53^\circ \pm 0.28^\circ$ at $\le 70\,\rm GHz$ and which does **not** use ACT data despite the fabricated "Joint Planck and ACT" title); Paper 1A §VIII.D (L666–667 + L1170) and Wave 14-JJJJ note in the bibfile both depend on this entry and inherit the false claim. The P2 R-round (Perplexity, 13:30 PT today) recorded the same BLOCKER on the same entry; either the "P2 update" referenced in this prompt has not been applied, or it was applied to a downstream surface (status doc / wave note) without ever touching the bibitem itself.

---

## BLOCKERs

### B1. `Eskilt2022b` bibitem is still mis-stitched (P2 BLOCKER carries into P1A unchanged)

- **Location:** `arxiv/references.bib` L990–1002; cited at `arxiv/paper1a_ech_nogo.tex` L667 (§VIII.D EB-correlation cite chain) and L1170 (App. C ALP comparison).
- **Claimed in bibitem:**
  ```
  @article{Eskilt2022b,
      author = "Eskilt, J. R. and others",
      collaboration = "{Cosmoglobe}",
      title = "{Joint Planck and ACT measurement of cosmic birefringence: $\beta = 0.342^\circ \pm 0.094^\circ$}",
      journal = "Astron. Astrophys.", volume = "679", pages = "A144", year = "2023",
      eprint = "2305.02268",
      doi = "10.1051/0004-6361/202346829"
  }
  ```
- **Verified reality (sources: arXiv abstract pages for 2305.02268 and 2205.13962, fetched 2026-05-13 15:30 PT):**
  - **arXiv:2305.02268** = Eskilt, Watts, Aurlien, Basyrov, Bersanelli, Brilenkov, Colombo, Eriksen, Fornazier, Franceschet, Fuskeland, Galloway, Gjerløw, Hensley, Hergt, Herman, Ihle, Lee, Lunde, Nerval, Paradiso, Patel, Rahman, Regnier, San, Sanyal, Stutzer, Thommesen, Verma, Wehus, Zhou. **Title: "Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data."** A&A **679**, A144 (2023). Headline value $\beta_{\le 70\,\rm GHz} = 0.53^\circ \pm 0.28^\circ$ (1.9σ from zero). **No ACT data used.**
  - **arXiv:2205.13962** = Eskilt & Komatsu, **"Improved Constraints on Cosmic Birefringence from the WMAP and Planck CMB Polarization Data"**, PRD **106**, 063503 (2022). Headline $\beta = 0.342^\circ \,{}^{+0.094^\circ}_{-0.091^\circ}$ (3.6σ). This is the value Paper 1A actually quotes. Already present in the bib as `Eskilt2022`.
- **What's wrong (same four issues as P2 BLOCKER B1):**
  1. The bibitem title ("Joint Planck and ACT measurement...") is fabricated — no paper at arXiv:2305.02268 has that title or "Planck+ACT" framing.
  2. The headline value 0.342° ± 0.094° belongs to `Eskilt2022` (arXiv:2205.13962), not to arXiv:2305.02268.
  3. Author list ("Eskilt, J. R. and others / Cosmoglobe") matches 2305.02268 but title and value belong to 2205.13962.
  4. Uncertainty is asymmetric ($+0.094^\circ / -0.091^\circ$), not symmetric (separate MINOR, m1 below).
- **Manuscript-level consequence:**
  - **Paper 1A §VIII.D L666–667:** `"...$\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$~\cite{Minami2020, Eskilt2022b,DiegoPalazuelos2025}"`. The `Eskilt2022b` citation here is exactly the false-stitch case — a reviewer who clicks through to A&A 679, A144 finds neither 0.342° nor a Planck+ACT joint analysis.
  - **Paper 1A App. C L1170:** `"...the observed isotropic cosmic-birefringence signal ($\beta=0.342^\circ\pm 0.094^\circ$, Eskilt~\etal~\cite{Eskilt2022b}) at $0.77\sigma$..."`. Same false attribution; the 0.77σ science is rescued by collapsing the cite to `Eskilt2022`, but as-printed the prose attributes a PRD-2022 value to an A&A-2023 paper.
- **SSOT collision:** The prompt says this entry is "v1.7.27-aligned (with P2 update)". Either the "P2 update" never landed in the bibfile (the only canonical surface) or it landed on a downstream status doc. As of 2026-05-13 15:30 PT, `references.bib` L990–1002 still carries the bad stitch.
- **Fix:** Same two-option fix as P2 BLOCKER B1.
  - **(Preferred — collapse):** Drop `Eskilt2022b`. Replace both `\cite{Eskilt2022b}` calls (L667, L1170) with `\cite{Eskilt2022}`. Rewrite the §VIII.D phrase "Cosmoglobe DR1 Planck+ACT joint measurement" if it appears anywhere in P1A prose to "Eskilt & Komatsu WMAP+Planck analysis"; in the current P1A text neither L666 nor L1170 actually use the "Cosmoglobe Planck+ACT" framing in prose (only the bibitem does), so the prose is salvageable as-is once the cite is swapped.
  - **(Alternative — split):** Rewrite `Eskilt2022b` to faithfully describe arXiv:2305.02268 (Cosmoglobe DR1 II, WMAP+LFI synchrotron analysis, $\beta = 0.35^\circ \pm 0.70^\circ$ or $\beta_{\le 70\,\rm GHz} = 0.53^\circ \pm 0.28^\circ$) and swap both `\cite{Eskilt2022b}` calls to `\cite{Eskilt2022}`. Only keep an `Eskilt2022b` (or `EskiltCosmoglobeDR1II`) cite if P1A prose actually invokes the WMAP+LFI synchrotron analysis, which it does not.
- **Priority:** BLOCKER. Same severity as P2 — this is the only finding in the review that produces a verifiably-false manuscript claim. The 0.77σ consistency number is correct; only the citation chain is broken.

---

## MAJORs

### M1. `Mercuri2006` bibitem title does not match the published paper

- **Location:** `arxiv/references.bib` L128–139; cited at `arxiv/paper1a_ech_nogo.tex` L811 (closing-acknowledgments paragraph: "Mercuri~\cite{Mercuri2006,Mercuri2009}").
- **Claimed in bibitem:**
  ```
  title = {Fermion coupling to the {Holst} action}
  ```
- **Verified reality (sources: arxiv.org/abs/gr-qc/0601013 abstract page + PRD landing page for 10.1103/PhysRevD.73.084016):**
  - **Actual title:** "Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter" (identical on arXiv and PRD; verified via dx.doi.org/10.1103/PhysRevD.73.084016).
  - Author (S. Mercuri), arXiv ID (gr-qc/0601013), DOI (10.1103/PhysRevD.73.084016), volume/pages/year (PRD 73, 084016, 2006) all verify clean.
- **What's wrong:** The bib title is a fabricated paraphrase — there is a paper titled "Hamiltonian analysis of fermions coupled to the Holst action" (Bombacigno+Montani, PRD 103, 124030, 2021), and the Mercuri 2006 paper is the foundational reference *for* fermion-Holst coupling, so the paraphrase is thematically right; but the actual title is the Ashtekar-Barbero / Immirzi-parameter framing. A literature-hawk referee searching by the bib title will not find this paper.
- **Fix:**
  ```latex
  @article{Mercuri2006,
    author  = {Mercuri, Simone},
    title   = {Fermions in the {Ashtekar-Barbero} connection formalism for arbitrary values of the {Immirzi} parameter},
    journal = {Physical Review D},
    volume  = {73}, pages = {084016}, year = {2006},
    doi     = {10.1103/PhysRevD.73.084016},
    eprint  = {gr-qc/0601013}, archivePrefix = {arXiv}, primaryClass = {gr-qc}
  }
  ```
- **Priority:** MAJOR. Title-fabrication is a citation-chain integrity hit. The cite key (`Mercuri2006`), in-text label ("Mercuri~\cite{Mercuri2006}"), and arXiv ID all line up — only the title is wrong — so the fix is mechanical (one bib line). Same class of bug as the `Cai:2026echoes` MAJOR in the P2 review.

### M2. `Liu2025` is a phantom-duplicate of `ECTorsionDESI2025` (wrong first name, dead DOI, redundant entry)

- **Location:** `arxiv/references.bib` L61–69 (Liu2025) vs L536–544 (ECTorsionDESI2025); Liu2025 cited at `arxiv/paper1a_ech_nogo.tex` L813 ("Liu~\etal~\cite{Liu2025} (EC torsion fits the $S_8$ tension)").
- **Claimed in bibitem (Liu2025):**
  ```
  @article{Liu2025,
    author  = {Liu, Rui-Yun and others},
    title   = {Einstein-Cartan torsion and the $S_8$ tension},
    journal = {European Physical Journal C}, volume = {85}, pages = {112}, year = {2025},
    doi     = {10.1140/epjc/s10052-025-13754-3}
  }
  ```
- **Verified reality (sources: arXiv:2507.04265 abstract page; WebSearch for the DOI):**
  - The actual "torsion + DESI + S8" 2025 EPJC paper is **Liu, Tonghua; Li, Xiaolei; Xu, Tengpeng; Biesiada, Marek; Wang, Jieci**, "Torsion cosmology in the light of DESI, supernovae and CMB observational constraints", **EPJC 85:1351 (2025)**, DOI **10.1140/epjc/s10052-025-15090-0**, arXiv:2507.04265. This paper reports S8 = 0.812 ± 0.006 from EC torsion + DESI DR2 BAO + Pantheon+ + DES-Y5 + Planck 2018, reducing the KiDS-1000 S8 tension from ~2.3σ to 0.1σ — which matches the L813 prose attribution ("EC torsion fits the $S_8$ tension") exactly.
  - This is **already in the bib** as `ECTorsionDESI2025` (L536–544) — verified clean against arXiv.
  - The `Liu2025` first-author name "Rui-Yun" does not match any author on arXiv:2507.04265. WebSearch for "Liu Rui-Yun" + "Einstein-Cartan" + "S8 tension" returns no hit.
  - The DOI `10.1140/epjc/s10052-025-13754-3` returns 404 on doi.org (verified live). The real DOI is `15090-0`.
  - The pages claim "85, 112" is also not the actual reference (EPJC 85, 1351).
- **What's wrong:** `Liu2025` appears to be a phantom-duplicate of `ECTorsionDESI2025` with three independent fabrications (first name, DOI, page number). It is cited at L813 where the prose ("Liu~\etal... EC torsion fits the $S_8$ tension") matches Liu, Tonghua et al. arXiv:2507.04265 exactly — so the intent is clearly to cite that paper, but the cite key resolves to the broken duplicate.
- **Fix:** Either (preferred) delete `Liu2025` and change L813 to `\cite{ECTorsionDESI2025}`, or rewrite `Liu2025` with the corrected author / DOI / pages and pick one of the two keys to retire. The cleanest fix is the delete-and-swap because `ECTorsionDESI2025` is already verified clean.
- **Priority:** MAJOR. Wrong first-author + fabricated DOI + fabricated pages — a referee following the L813 cite will land on a 404 and then find the same paper sitting in the bib under a different key 470 lines below. Embarrassing in front of a referee.

### M3. Pantheon+ and DES-SN5YR are namechecked in P1A prose but missing from the bib

- **Location:** Paper 1A footnote L1075 references "DESI~DR2 + Planck~NPIPE + Pantheon$+$ + DES-SN5YR cobaya chain" by name; no `\cite{}` accompanies "Pantheon+" or "DES-SN5YR" anywhere in P1A.
- **Verified reality:**
  - **Pantheon+** = Brout et al., "The Pantheon+ Analysis: Cosmological Constraints", ApJ **938**, 110 (2022), DOI 10.3847/1538-4357/ac8e04, arXiv:2202.04077. (Verified live via INSPIRE-HEP.)
  - **DES-SN5YR** = DES Collaboration, "The Dark Energy Survey: Cosmology Results With ~1500 New High-Redshift Type Ia Supernovae Using the Full 5-Year Dataset", ApJL **973**, L14 (2024), DOI 10.3847/2041-8213/ad6f9f, arXiv:2401.02929.
- **What's wrong:** The footnote names two specific public supernova samples (Pantheon+ and DES-SN5YR) as ingredients in a currently-running cobaya chain whose results P1A will eventually cite. Right now, the named samples are dangling — they're invoked by name without a citation, and the bib has no Brout2022 / DES2024SN5YR entry. The DESI side is properly cited (`DESI2025DR2`); the SN side is unsupported.
- **Why MAJOR not MINOR:** The footnote is a key honesty disclosure (it's the place where Paper 1A confesses that the frozen MCMC posteriors contain zero free-$w_0 w_a$ samples and that the chain is "1–3 days from publication-quality convergence"). A reviewer will read this footnote carefully. Naming two SN samples without citing them invites the comment "which Pantheon+? Scolnic+2018 or Brout+2022?" — and the answer matters numerically.
- **Fix:** Add `Brout2022PantheonPlus` and `DES2024SN5YR` entries to the bib, and append `\cite{Brout2022PantheonPlus, DES2024SN5YR}` after each of the two namechecks at L1075. Bib entries:
  ```latex
  @article{Brout2022PantheonPlus,
    author  = {Brout, Dillon and Scolnic, Dan and Popovic, Brodie and others},
    title   = {The {Pantheon$+$} Analysis: Cosmological Constraints},
    journal = {The Astrophysical Journal}, volume = {938}, pages = {110}, year = {2022},
    doi     = {10.3847/1538-4357/ac8e04},
    eprint  = {2202.04077}, archivePrefix = {arXiv}, primaryClass = {astro-ph.CO}
  }
  @article{DES2024SN5YR,
    author  = {{DES Collaboration} and Abbott, T. M. C. and others},
    title   = {The {Dark Energy Survey}: Cosmology Results With $\sim$1500 New High-Redshift {Type Ia} Supernovae Using the Full 5-Year Dataset},
    journal = {The Astrophysical Journal Letters}, volume = {973}, pages = {L14}, year = {2024},
    doi     = {10.3847/2041-8213/ad6f9f},
    eprint  = {2401.02929}, archivePrefix = {arXiv}, primaryClass = {astro-ph.CO}
  }
  ```
- **Priority:** MAJOR. Named-but-uncited datasets in a footnote that's already a load-bearing honesty disclosure is exactly the kind of detail an arXiv production editor or referee flags.

---

## MINORs

### m1. Eskilt:2022 uncertainty quoted as symmetric in Paper 1A prose

- **Location:** `arxiv/paper1a_ech_nogo.tex` L666 ("$\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$") and L1170 (same phrasing).
- **Verified reality:** arXiv:2205.13962 abstract: $\beta = 0.342^\circ \,{}^{+0.094^\circ}_{-0.091^\circ}$. Asymmetry is small (~3%) but real.
- **Fix:** Add a footnote at first use ("Eskilt & Komatsu quote the asymmetric interval $+0.094^\circ / -0.091^\circ$; we symmetrize for clarity") or quote the true asymmetric values. P2 review made the same call.
- **Priority:** MINOR. Same status as P2 m1.

### m2. `SPIDER2025` bibitem author is "{SPIDER Collaboration}" but the actual paper is by Yin / Xiong / Kochappan / Lee / Ghosh (not a SPIDER-Collaboration paper)

- **Location:** `arxiv/references.bib` L526–534. Not cited in Paper 1A as of v1A.0.19 (grep returns no `\cite{SPIDER2025}` calls), so the entry is dormant in P1A — but is in the shared bib and may be cited by P1B / P3 / P4.
- **Verified reality (source: arxiv.org/abs/2510.25489 abstract):** Authors are Lu Yin, Shuhang Xiong, Joby Kochappan, Bum-Hoon Lee, Tuhin Ghosh. The paper analyzes public SPIDER + Planck + ACT data — it is **not** a SPIDER-Collaboration paper. Lu Yin is the same first author as `Yin2026` (arXiv:2601.13624), and the two papers are likely a series by Yin's group.
- **What's wrong:** `author = "{SPIDER Collaboration}"` is fabricated. The arXiv list has no collaboration tag; it's a five-author independent analysis.
- **Fix:**
  ```latex
  @article{Yin2025SPIDER,
    author  = {Yin, Lu and Xiong, Shuhang and Kochappan, Joby and Lee, Bum-Hoon and Ghosh, Tuhin},
    title   = {Constraints on Cosmic Birefringence from {SPIDER}, {Planck}, and {ACT} observations},
    journal = {arXiv e-prints}, year = {2025},
    eprint  = {2510.25489}, archivePrefix = {arXiv}, primaryClass = {astro-ph.CO}
  }
  ```
  and update the cite key (zero uses in P1A; check P1B / P3 / P4 before renaming).
- **Priority:** MINOR. Dormant in P1A, but a fabrication that ships in the shared bib stays a liability until removed. Below the BLOCKER bar (no in-text false claim in P1A).

### m3. `Legner2025` bib entry missing fourth author and missing journal reference

- **Location:** `arxiv/references.bib` L546–554; cited at `arxiv/paper1a_ech_nogo.tex` L813 ("Legner~\etal~\cite{Legner2025}").
- **Verified reality (source: arxiv.org/abs/2507.09228 abstract):**
  - **Actual author list:** Sinah Legner, Will Handley, Will Barker, **Adam Ormondroyd** (bib has only the first three).
  - **Journal:** Now published — JCAP **03** (2026) 003, DOI 10.1088/1475-7516/2026/03/003. The bib still claims `journal = {arXiv e-prints}`.
- **Fix:**
  ```latex
  @article{Legner2025,
    author  = {Legner, Sinah and Handley, Will and Barker, Will and Ormondroyd, Adam},
    title   = {Alleviating the {Hubble} tension with {Torsion Condensation} ({TorC})},
    journal = {Journal of Cosmology and Astroparticle Physics}, volume = {03}, pages = {003}, year = {2026},
    doi     = {10.1088/1475-7516/2026/03/003},
    eprint  = {2507.09228}, archivePrefix = {arXiv}, primaryClass = {astro-ph.CO}
  }
  ```
- **Priority:** MINOR. Etiquette / journal-stamp hygiene — won't trigger a referee report on its own, but is a sloppy detail in a paper that names Legner et al. at L813 in the same paragraph it names Liu et al. and Alam et al.

---

## NITs

### n1. Cross-paper `Golden2026P{1b,2,3,4}` self-cites use `journal = "(in preparation)"` — format is consistent across the four self-cites, but the preprint IDs in the `note` field are HUBIFY-internal numbers that mean nothing to an external reader

- **Location:** `arxiv/references.bib` L950–988 (the five Golden2026P{1a,1b,2,3,4} entries).
- **Format check:** All four entries Paper 1A cites (`Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4`) follow the same template — `journal = "(in preparation)"`, `note = "HUBIFY-2026-00XY; companion paper, this volume"`. Internally consistent. Good.
- **External-reader friction:** `HUBIFY-2026-001B` etc. are private preprint numbers (Hubify-Projects/bigbounce GitHub release tags pending arXiv submission per the comment at L946–948). An external referee or arXiv production editor will not be able to resolve "HUBIFY-2026-001B" to anything — no public preprint server is named, no arXiv ID is given.
- **Suggested fix (post-arXiv-submission):** Once any of P1B/P2/P3/P4 lands on arXiv, replace `journal = "(in preparation)"` with `eprint = {YYMM.NNNNN}, archivePrefix = {arXiv}` and drop the `HUBIFY-2026-00XY` note. Pre-submission, leave as-is — but consider adding a `url = {https://bigbounce.hubify.app/papers}` field so an external reader can find the latest draft.
- **Priority:** NIT. Won't block submission. Worth a single-line tweak once any of the companion papers gets an arXiv ID.

---

## Verifications (citations spot-checked and confirmed clean)

| Bib key | Claim | Verified source | Verdict |
|---|---|---|---|
| `Holst1996` | PRD 53, 5966 (1996), arXiv:gr-qc/9511026, Holst single-author | arxiv.org/abs/gr-qc/9511026 | ✅ Title "Barbero's Hamiltonian derived from a generalized Hilbert-Palatini action", author, journal, DOI all match. |
| `Freidel2005` | PRD 72, 104002 (2005), arXiv:hep-th/0507253, Freidel/Minic/Takeuchi | arxiv.org/abs/hep-th/0507253 | ✅ Title "Quantum Gravity, Torsion, Parity Violation and all that", authors, journal, DOI all match. |
| `LueWangKamionkowski1999` | PRL 83, 1506 (1999), arXiv:astro-ph/9812088, Lue/Wang/Kamionkowski | arxiv.org/abs/astro-ph/9812088 | ✅ Title "Cosmological Signature of New Parity-Violating Interactions", authors, journal, DOI all match. Bib key year 1999 matches PRL pub year (arXiv-v1 was Dec 1998). |
| `Planck2018params` | A&A 641, A6 (2020), arXiv:1807.06209, Planck Collaboration | arxiv.org/abs/1807.06209 | ✅ Title, collaboration, journal, DOI all match. |
| `DESI2025DR2` | PRD 112, 083515 (2025), arXiv:2503.14738, DESI Collaboration / Abdul-Karim+ | arxiv.org/abs/2503.14738 | ✅ Title "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints", DESI Collab, journal/DOI match. |
| `Eskilt2022` | PRD 106, 063503 (2022), Eskilt & Komatsu, $\beta = 0.342^\circ \,{}^{+0.094^\circ}_{-0.091^\circ}$ | arxiv.org/abs/2205.13962 | ✅ Title, authors, journal, DOI, value all match. **This is the bib entry that should be cited in place of `Eskilt2022b` everywhere.** |
| `DiegoPalazuelos2025` | arXiv:2509.13654 (PRD accepted), Diego-Palazuelos & Komatsu | arxiv.org/abs/2509.13654 | ✅ Title "Cosmic Birefringence from the Atacama Cosmology Telescope Data Release 6", authors, arXiv ID match. PRD accepted, no volume/pages yet — appropriate to keep as `journal = "arXiv preprint"` for now. |
| `Yin2026` | arXiv:2601.13624, Yin/Du/Li/Zhang | arxiv.org/abs/2601.13624 | ✅ Title "Joint constraints on cosmic birefringence and early dark energy from ACT, Planck, DESI, and PantheonPlus", authors, arXiv ID all match. No journal yet — `journal = "arXiv preprint"` is correct. |
| `Alam2025bounce` | EPJC 2025, arXiv:2509.03508, Alam/Sen/Sengupta | arxiv.org/abs/2509.03508 | ✅ Title "Bouncing Cosmologies in modified gravity with space time torsion", authors, journal, DOI (10.1140/epjc/s10052-025-15123-8) verify; bib could add the DOI field but the eprint is sufficient. |
| `ECTorsionDESI2025` | EPJC 85, 1351 (2025), arXiv:2507.04265, Liu/Li/Xu/Biesiada/Wang | arxiv.org/abs/2507.04265 | ✅ Title, authors, arXiv ID match. (Bib could add `volume = "85"`, `pages = "1351"`, and DOI `10.1140/epjc/s10052-025-15090-0` for completeness, but those are NITs — the eprint suffices.) |
| `Golden2026P{1b,2,3,4}` | Internal cross-paper self-cites | references.bib L958–988 | ✅ All four follow the same template; format-consistent across the portfolio. See n1 for a forward-looking NIT (replace HUBIFY-internal preprint IDs with arXiv IDs once available). |

---

## Items in the prompt that were NOT findable as P1A issues

- **`Alexander:2009tp`** — not present in `references.bib` and not cited in `paper1a_ech_nogo.tex`. The Chern-Simons gravity Phys Rep review (Alexander & Yunes 2009, arXiv:0907.2562) is not in the P1A citation chain. If P1A should be citing it for the parity-odd-action chain in §IV (Step 4 Parity-Odd Coefficient, L320), that's a *missing-citation* gap, but it's outside the citation-hawk remit (the manuscript can legitimately decide which reviews to lean on). Flagging here for record only; not graded.
- **Pantheon+ and DES-SN5YR as cited bibitems** — graded above as MAJOR M3, but the prompt asked me to "verify" them as if they were in the bib. They are not. M3 is the constructive fix.

---

## Summary

| Severity | Count |
|---|---:|
| BLOCKER | 1 |
| MAJOR | 3 |
| MINOR | 3 |
| NIT | 1 |
| **Total** | **8** |

**Net recommendation:** The single BLOCKER (`Eskilt2022b` mis-stitch) is the **same** finding as P2 R-round BLOCKER B1 — the prompt called out "v1.7.27-aligned (with P2 update)" status for this entry, but as of 2026-05-13 15:30 PT the bib still carries the bad stitch. Either the P2 fix was never applied to the shared bibfile, or it was applied to a downstream status surface (SSOT note, wave log) without ever touching `references.bib` L990–1002. **Recommended action: do the collapse fix once at the shared bib level (drop `Eskilt2022b`, swap two cites in P1A and any others in P1B / P2 / P3 / P4 to `Eskilt2022`), and close this BLOCKER across the entire portfolio in a single commit.** After that, the three MAJORs (Mercuri2006 title-fabrication, Liu2025 phantom-duplicate, Pantheon+/DES-SN5YR namecheck without cite) are mechanical fixes; the three MINORs and one NIT are hygiene. The eleven high-stakes entries spot-checked from arXiv (Holst, Freidel, Lue+, Planck2018, DESI2025DR2, Eskilt2022 itself, DiegoPalazuelos, Yin2026, Alam2025bounce, ECTorsionDESI2025, Golden2026 cross-cites) all verify clean.

**Sources used (verified live during this review):**
- arxiv.org/abs/gr-qc/9511026 (Holst1996 — clean)
- arxiv.org/abs/gr-qc/0601013 (Mercuri2006 — bib title is fabricated, see M1)
- arxiv.org/abs/hep-th/0507253 (Freidel2005 — clean)
- arxiv.org/abs/astro-ph/9812088 (Lue/Wang/Kamionkowski 1999 — clean)
- arxiv.org/abs/1807.06209 (Planck 2018 VI — clean)
- arxiv.org/abs/2503.14738 (DESI DR2 II — clean)
- arxiv.org/abs/2205.13962 (Eskilt & Komatsu 2022 — actual 0.342° source)
- arxiv.org/abs/2305.02268 (Cosmoglobe DR1 II, Eskilt/Watts/Aurlien+ 2023 — NOT 0.342°, NOT Planck+ACT joint; mis-stitched into `Eskilt2022b`)
- arxiv.org/abs/2509.13654 (Diego-Palazuelos & Komatsu 2025 — clean)
- arxiv.org/abs/2601.13624 (Yin/Du/Li/Zhang 2026 — clean)
- arxiv.org/abs/2510.25489 (Yin/Xiong/Kochappan/Lee/Ghosh 2025 — `SPIDER2025` author field fabricated, see m2)
- arxiv.org/abs/2507.09228 (Legner/Handley/Barker/Ormondroyd 2026 — bib missing 4th author and journal, see m3)
- arxiv.org/abs/2507.04265 (Liu/Li/Xu/Biesiada/Wang 2025 EPJC 85:1351 — see M2 for `Liu2025` phantom-dup)
- arxiv.org/abs/2509.03508 (Alam/Sen/Sengupta 2025 EPJC — clean)
- doi.org/10.1103/PhysRevD.73.084016 (Mercuri 2006 PRD landing — confirms actual title is "Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter", not the bib's paraphrase)

---

_Reviewer signoff: Perplexity persona, 2026-05-13 15:30 PT. Verifications anchored to live arXiv abstract pages and journal landing pages at review time. The BLOCKER is the same one P2 flagged at 13:30 PT today — a single shared-bib fix resolves it portfolio-wide._
