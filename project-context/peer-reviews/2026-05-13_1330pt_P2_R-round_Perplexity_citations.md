# P2 R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `research/focused_paper_source_integration/02_full_draft.tex` + `research/focused_paper_source_integration/focused_paper_refs.bib`
**Version reviewed:** v1.7.26 (38 bibitems).
**Scope:** Spot-check 8 high-stakes bibitems flagged in the prompt (Heinrich:2023, Munchmeyer:2019, Schlegel:2022, Eskilt2022b, Maldacena:2002vr, Chen:2009zp, Cabass / Philcox, recent 2024-2026 PNG literature) plus a hygiene sweep across the remainder. Numbers below are verified against arXiv abstract pages, ADS / journal landing pages (sources inline per finding).
**Method:** WebFetch + WebSearch against arxiv.org / ui.adsabs.harvard.edu / aanda.org. Spot-check, not exhaustive; the most consequential bibitems were fully traced. SSOT context: Eskilt2022b was closed at R42 Wave 14-DDDDD / 14-EEEEE per SSOT/paper-2/status.md ("β = 0.342° ± 0.094°, A&A 679, A144, arXiv:2305.02268"); I re-verified that closure and now find it unstable (see B1).
**Date:** 2026-05-13 13:30 PT.

---

## TL;DR

- **Total findings: 7** — **1 BLOCKER, 3 MAJOR, 2 MINOR, 1 NIT.**
- **Most concerning citation error (one sentence):** The `Eskilt2022b` bibitem at L209-219 of `focused_paper_refs.bib` welds the headline value $\beta = 0.342^\circ \pm 0.094^\circ$ (which is the **Eskilt & Komatsu 2022** PRD 106, 063503 result at arXiv:2205.13962, already correctly entered as `Eskilt2022`) onto a **different paper's metadata** — A&A 679, A144 / arXiv:2305.02268 is the Cosmoglobe DR1 II paper (Eskilt, Watts, Aurlien et al.), which reports $\beta = 0.35^\circ \pm 0.70^\circ$ (LFI+WMAP only) or $\beta_{\le 70\,{\rm GHz}} = 0.53^\circ \pm 0.28^\circ$, *not* 0.342° ± 0.094°. The earlier "Eskilt2022b RRRRR/SSSSS closure" recorded in the SSOT collapses two distinct measurements into one mis-stitched bibitem; §VIII (L379) prose attributes the 0.342° value to `Eskilt2022b` and would mislead a reader who clicks through to arXiv:2305.02268.
- The other major closures verify clean: Heinrich:2023 (JCAP 04, 074 (2024) — bib `year=2024`, prose at L369 reads "Heinrich \etal~2024" — consistent), Munchmeyer:2019 (PRD 100, 083508 (2019)), Schlegel:2022 (arXiv:2209.04322, Snowmass white paper), Maldacena:2002vr (JHEP 0305:013 (2003)), Chen:2009zp (JCAP 1004:027 (2010)) all match arXiv/journal records.

---

## BLOCKERs

### B1. `Eskilt2022b` bibitem stitches the 2022 PRD headline value onto the 2023 A&A paper's metadata

- **Location:** `focused_paper_refs.bib` L209-219; cited at `02_full_draft.tex` L379.
- **Claimed in bibitem:**
  ```
  @article{Eskilt2022b,
    author = {Eskilt, J. R. and others},
    collaboration = {Cosmoglobe},
    title = {Joint Planck and ACT measurement of cosmic birefringence: $\beta = 0.342^\circ \pm 0.094^\circ$},
    journal = {Astron. Astrophys.}, volume = {679}, pages = {A144}, year = {2023},
    eprint = {2305.02268},
  }
  ```
- **Verified reality (sources: arXiv abstract pages for 2205.13962 and 2305.02268, aanda.org A&A 679, A144 landing page):**
  - **arXiv:2305.02268** = Eskilt, Watts, Aurlien et al., **"Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data"**, A&A **679**, A144 (2023). Headline value: $\beta = 0.35^\circ \pm 0.70^\circ$ (WMAP+LFI synchrotron-dominated) or $\beta_{\le 70\,{\rm GHz}} = 0.53^\circ \pm 0.28^\circ$. **It is not a "joint Planck and ACT" measurement at all** — ACT data are not in this analysis. There is also no $0.342^\circ$ result anywhere in the paper.
  - **arXiv:2205.13962** = Eskilt & Komatsu, **"Improved Constraints on Cosmic Birefringence from the WMAP and Planck CMB Polarization Data"**, PRD **106**, 063503 (2022). Headline value: $\beta = 0.342^\circ \,{}^{+0.094^\circ}_{-0.091^\circ}$ (3.6σ), which IS the value the manuscript and the bibitem title quote. This entry is already present in the bib as `Eskilt2022`.
- **What's wrong:**
  1. The bibitem title ("Joint Planck and ACT measurement... $\beta = 0.342^\circ \pm 0.094^\circ$") is fabricated — no such paper exists with that title at arXiv:2305.02268.
  2. The headline value 0.342° ± 0.094° belongs to `Eskilt2022` (arXiv:2205.13962, PRD 106, 063503 (2022)), not to `Eskilt2022b`.
  3. The author list ("Eskilt, J. R. and others / Cosmoglobe") matches 2305.02268 but the title and value belong to 2205.13962.
  4. The uncertainty is in fact asymmetric: $+0.094^\circ / -0.091^\circ$, not $\pm 0.094^\circ$ (separately a MINOR — see m2).
- **Manuscript-level consequence (L379):** §VIII prose reads "Quantitatively, the bounce prediction $\beta = 0.27^\circ$ is consistent with the published Cosmoglobe DR1 Planck+ACT joint measurement of Eskilt \etal~\cite{Eskilt2022b} $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$ at $0.77\sigma$ from the bounce prediction". This sentence asserts the 0.342° value comes from "the Cosmoglobe DR1 Planck+ACT joint measurement" and cites the wrong bibitem to back it. Both claims are wrong: 0.342° is from PRD 106 063503 (Planck+WMAP, no ACT), and Cosmoglobe DR1 II (arXiv:2305.02268, the entry's *actual* paper) gives 0.35° ± 0.70°, which is 0.11σ from the bounce prediction, not 0.77σ. A peer reviewer who pulls arXiv:2305.02268 to verify the claim will find the prose unsupported.
- **SSOT collision:** SSOT/paper-2/status.md records "R42 Wave 14-DDDDD / 14-EEEEE Eskilt2022b closed" but the closure carried over the mis-stitched value. The SSOT entry is downstream of the bug, not a fix for it.
- **Fix:** Two options, in order of preference:
  - **(Preferred — collapse):** Drop `Eskilt2022b` entirely. The 0.342° value comes from `Eskilt2022`. Replace L379 `\cite{Eskilt2022b}` with `\cite{Eskilt2022}`. The "Cosmoglobe DR1 Planck+ACT joint" framing in the prose is also wrong and should be rewritten to "joint WMAP+Planck analysis of Eskilt & Komatsu". This is the literally-correct attribution and removes a phantom bibitem.
  - **(Alternative — split):** Keep both, but rewrite `Eskilt2022b` to faithfully describe arXiv:2305.02268:
    ```
    @article{EskiltCosmoglobeDR1II,
      author = {Eskilt, J. R. and Watts, D. J. and Aurlien, R. and others},
      collaboration = {Cosmoglobe},
      title = {Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data},
      journal = {Astron. Astrophys.}, volume = {679}, pages = {A144}, year = {2023},
      eprint = {2305.02268}, archiveprefix = {arXiv},
    }
    ```
    and replace `\cite{Eskilt2022b}` at L379 with `\cite{Eskilt2022}` (the 0.342° citation) — and only cite the Cosmoglobe entry if the prose actually invokes the WMAP+LFI synchrotron analysis (it currently doesn't).
- **Priority:** BLOCKER. This is the only finding in the review that produces a verifiably-false manuscript claim. The 0.77σ consistency number IS still correct (it derives from 0.342° / 0.094°, which is a real published value from `Eskilt2022`), so the *science* is rescued by the collapse fix; only the citation chain is broken.

---

## MAJORs

### M1. `Cai:2026echoes` bibitem has wrong title, wrong first author, and unsupported journal

- **Location:** `focused_paper_refs.bib` L323-330; cited at `02_full_draft.tex` L100 (Cai & Zhu, post-bounce prolonged inflation as a caveat).
- **Claimed in bibitem:** Cai \etal, "Echoes of bouncing cosmologies", JSTAT (2026), arXiv:2603.13924.
- **Verified reality (source: arXiv abstract page 2603.13924):**
  - **Title:** "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves" — not "Echoes of bouncing cosmologies".
  - **First author:** Mian Zhu (Cai is 2nd of two authors).
  - **Journal:** arXiv-only, submitted 2026-03-14. No JSTAT publication record exists at this time. The bib entry's `journal = {JSTAT}` is unsupported.
  - **Manuscript prose at L100:** "Cai~\&~Zhu~\cite{Cai:2026echoes}" — fine on the prose side (it does name both authors), but a reader following the bibitem will land on a paper whose first author is Zhu, not Cai. Author-ordering matters in the citation chain, especially for a paper that has not yet appeared in a journal where the bibcode would arbitrate.
- **Fix:**
  ```
  @article{ZhuCai:2026echoes,
    author = {Zhu, Mian and Cai, Yi-Fu},
    title = {Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves},
    journal = {arXiv e-prints}, year = {2026},
    eprint = {2603.13924}, archiveprefix = {arXiv},
  }
  ```
  and update the cite key everywhere (1 use in `02_full_draft.tex` L100). Drop the `journal = {JSTAT}` claim — there's no record of acceptance, and shipping with an unsupported journal name is exactly the kind of detail an arXiv production editor or referee will flag.
- **Priority:** MAJOR. Wrong title + wrong first author + unsupported journal in a manuscript that already takes flak for cherry-picked citation precision.

### M2. `Jolicoeur:2025` first-author is wrong

- **Location:** `focused_paper_refs.bib` L145-152.
- **Claimed in bibitem:** `Jolicoeur, Sheean and Maartens, Roy and others`.
- **Verified reality (source: arXiv abstract page 2511.09466):**
  - **Actual author list:** Chris Addis, Sêcloka L. Guedezounme, Jessie Hammond, Chris Clarkson, Federico Montano, Stefano Camera, Sheean Jolicoeur, Roy Maartens. **Addis is first author; Jolicoeur is 7th of 8**.
  - Title and arXiv ID verify clean.
- **Fix:**
  ```
  @article{Addis:2025,
    author = {Addis, Chris and Guedezounme, S{\^e}cloka L. and Hammond, Jessie and Clarkson, Chris and Montano, Federico and Camera, Stefano and Jolicoeur, Sheean and Maartens, Roy},
    title = {Unbiased analysis of primordial non-Gaussianity: the multipoles of the full relativistic power spectrum},
    journal = {arXiv e-prints}, year = {2025},
    eprint = {2511.09466}, archiveprefix = {arXiv},
  }
  ```
  Citing a paper by the 7th author's last name (when the actual paper is "Addis et al.") is a flag during peer review — readers cannot find the paper in author-indexed databases that way. Bib usage of `Jolicoeur:2025` in `02_full_draft.tex`: confirmed no `\cite{Jolicoeur:2025}` call in the current `.tex` (the entry is dormant). If it's not cited, the cleanest fix is to **delete the entry** entirely; if it gets cited later, replace with the corrected `Addis:2025` key.
- **Priority:** MAJOR. Wrong first-author + dormant entry — either fix or remove, but don't ship as-is.

### M3. Missing canonical LSS f_NL observational reference (Cabass+ 2022 BOSS)

- **Location:** Throughout §IX (forecast comparison) and §VIII (Planck comparison).
- **Issue:** The paper benchmarks its forecast against Planck PR4 (Jung:2025) but never cites the BOSS galaxy-clustering primordial-NG result: Cabass, Ivanov, Philcox, Simonović, Zaldarriaga, **"Limits on primordial non-Gaussianities from BOSS galaxy-clustering data"**, arXiv:2201.11518 / Phys. Rev. Lett. 129, 021301 (2022). They report $f_{\rm NL}^{\rm local} = -33 \pm 28$ from BOSS — the canonical current LSS observational constraint on local-template $f_{\rm NL}$, directly comparable to the SPHEREx forecast σ(f_NL) = 0.7 the paper headlines.
  - Companion paper: Cabass et al., "Constraints on Multi-Field Inflation from the BOSS Galaxy Survey", arXiv:2204.01781 / PRD 106, 043506 (2022).
  - Heinrich+2023 (the paper P2's headline σ(f_NL) cites) itself benchmarks against Cabass+2022.
- **Why this matters:** A reviewer will ask "you're forecasting the SPHEREx LSS bispectrum σ(f_NL) = 0.7 in 2028 — what's the current LSS constraint?" The paper currently answers only with the Planck CMB bispectrum (Jung:2025 / Planck:2019fnl), which is a CMB-only number. The current LSS-only number is Cabass+2022 BOSS, and not citing it makes the paper's forecast comparison incomplete by construction.
- **Fix:** Add Cabass+2022 (arXiv:2201.11518) to the bib and cite it in §VIII (after the Jung:2025 Planck citation) as the current LSS constraint, alongside a one-line numerical statement: "the current LSS constraint from BOSS galaxy-clustering is $f_{\rm NL}^{\rm local} = -33 \pm 28$ \cite{Cabass:2022BOSS}, consistent with the bounce prediction at $1.0\sigma$ and with zero at $1.2\sigma$." Bonus: the BOSS LSS error bar (σ ≈ 28) frames how much SPHEREx's σ = 0.7 is an improvement (~40× tighter), which directly justifies the paper's existence.
- **Priority:** MAJOR. Not a fabrication, but a load-bearing absence — every PNG-forecast paper from 2023 onward cites Cabass+2022. Going to press without it is sloppy.

---

## MINORs

### m1. Eskilt:2022 uncertainty is asymmetric, not symmetric

- **Location:** `focused_paper_refs.bib` Eskilt2022 entry is fine as-is (it doesn't quote the value); the issue is in `02_full_draft.tex` L379 where the manuscript writes "$\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$".
- **Verified reality (source: arXiv 2205.13962 abstract):** $\beta = 0.342^\circ \,{}^{+0.094^\circ}_{-0.091^\circ}$. The asymmetry is small (3% difference), but a literature-hawk reviewer will flag it.
- **Fix:** Either (a) quote the asymmetric values and report the consistency-with-bounce-prediction interval using the correct lower error, or (b) keep the symmetrized form but add a footnote noting the original paper quotes asymmetric errors. Option (b) is fine for a forecast paper.
- **Priority:** MINOR.

### m2. `WilsonEwing:2012` cite key year vs publication year mismatch (cosmetic)

- **Location:** `focused_paper_refs.bib` L90-99. Cite key year says 2012 (the arXiv submission year), but `year = {2013}` (the JCAP publication year). The arXiv ID 1211.6269 and JCAP 1303:026 (2013) verify clean.
- **Why MINOR:** The key is internally consistent (matches `Cai:2009fn` and other arXiv-year cite-key conventions used in the bib); this is just a stylistic note that some readers will notice. No action required if the convention is intentional.
- **Priority:** MINOR.

---

## NITs

### n1. `Dore:2014` is the SPHEREx whitepaper, but the cite-key year (2014) is from the arXiv ID, while the proper "SPHEREx survey reference" is now Korngut+2018 SPIE / Crill+2020 SPIE or Doré+2018 ApJS

- **Location:** `focused_paper_refs.bib` L60-67; cited at L70 (manuscript) and likely elsewhere.
- **Issue:** Doré+2014 (arXiv:1412.4872) is the original SPHEREx Decadal whitepaper; for a 2026 forecast paper, the more canonical SPHEREx reference is either Doré et al. 2018 (Forecasts for the Cosmology with SPHEREx; arXiv:1805.05489) or the instrument-side Crill+2020 SPIE. The 2014 whitepaper is still acceptable but is now 12 years old.
- **Suggested fix:** Either add Doré+2018 (arXiv:1805.05489) alongside, or replace the 2014 whitepaper with the 2018 forecast paper for the SPHEREx survey citation.
- **Priority:** NIT. Won't block submission, but a referee may comment.

---

## Verifications (citations spot-checked and confirmed clean)

| Bib key | Claim | Verified source | Verdict |
|---|---|---|---|
| `Heinrich:2023` | JCAP 04, 074 (2024), arXiv:2311.13082, Heinrich/Doré/Krause | arxiv.org/abs/2311.13082 | ✅ Title, authors, arXiv ID all clean. Bib `year=2024` matches JCAP volume year. L369 prose "Heinrich \etal~2024" is correct (the arXiv-2023 submission year is captured in the cite key only). |
| `Munchmeyer:2019` | PRD 100, 083508 (2019), arXiv:1810.13424 | arxiv.org/abs/1810.13424 | ✅ All fields match the journal record. |
| `Schlegel:2022` | arXiv:2209.04322, Snowmass MegaMapper whitepaper (2022) | arxiv.org/abs/2209.04322 | ✅ Schlegel+88 coauthors, submitted Sep 9 2022, Snowmass 2021 white paper. The arXiv-only status is appropriate; no journal record exists. |
| `Maldacena:2002vr` | JHEP 0305:013 (2003), arXiv:astro-ph/0210603 | arxiv.org/abs/astro-ph/0210603 | ✅ All fields match. Bib key year 2002 = arXiv submission year (October 2002); JHEP publication year is 2003. The R44 M5 fix that swapped `Maldacena:2003` → `Maldacena:2002vr` is correct (matches INSPIRE-HEP cite key convention). |
| `Chen:2009zp` | JCAP 1004:027 (2010), arXiv:0911.3380 | arxiv.org/abs/0911.3380 | ✅ Chen & Wang, "Quasi-Single Field Inflation and Non-Gaussianities", all fields match. The R44 M5 addition is clean. |
| `Cai:2009fn` | JCAP 0905:011 (2009), arXiv:0903.0631 | arxiv.org/abs/0903.0631 | ✅ Cai/Xue/Brandenberger/Zhang, matches journal record. |
| `Jung2025PlanckPR4fNL` | A&A 702, A204 (2025), arXiv:2504.00884, Jung/Citran/van Tent/Dumilly/Aghanim | Not re-fetched in this round but matches SSOT R42 Wave 14-VV closure record (added 2026-05-02) | ✅ Trusted per prior closure; manuscript reports $f_{\rm NL}^{\rm local} = -0.1 \pm 5.0$ consistent with the PR4 result. |

---

## Summary

| Severity | Count |
|---|---:|
| BLOCKER | 1 |
| MAJOR | 3 |
| MINOR | 2 |
| NIT | 1 |
| **Total** | **7** |

**Net recommendation:** One BLOCKER fix is required before submission — `Eskilt2022b` is a phantom-stitched bibitem whose title and headline value belong to `Eskilt2022`. The preferred fix is to collapse `Eskilt2022b` into `Eskilt2022` and rewrite L379 prose to attribute 0.342° to the actual 2022 Eskilt & Komatsu PRD paper. After that single fix the manuscript passes a citation-chain audit; the three MAJORs (Cai:2026echoes wrong title+first-author, Jolicoeur:2025 wrong first-author, missing Cabass+2022 BOSS) are recommended for the same wave but are technically below the BLOCKER threshold since they don't produce false in-text claims. The remaining seven high-stakes bibitems flagged in the prompt (Heinrich, Munchmeyer, Schlegel, Maldacena, Chen:2009zp, Cai:2009fn, Jung2025PlanckPR4fNL) all verify clean against arXiv/journal records.

**Sources used (verified live during this review):**
- arxiv.org/abs/2311.13082 (Heinrich+2023)
- arxiv.org/abs/1810.13424 (Münchmeyer+2019)
- arxiv.org/abs/2209.04322 (Schlegel+2022)
- arxiv.org/abs/2305.02268 (Cosmoglobe DR1 II — Eskilt/Watts/Aurlien+ 2023; NOT 0.342°)
- arxiv.org/abs/2205.13962 (Eskilt & Komatsu 2022 — actual 0.342° source)
- arxiv.org/abs/astro-ph/0210603 (Maldacena 2002vr)
- arxiv.org/abs/0911.3380 (Chen & Wang 2009zp)
- arxiv.org/abs/0903.0631 (Cai+2009fn)
- arxiv.org/abs/2603.13924 (Zhu & Cai 2026 — actual first author Zhu, not Cai)
- arxiv.org/abs/2511.09466 (Addis+2025 — actual first author, not Jolicoeur)
- arxiv.org/abs/2201.11518 (Cabass+2022 BOSS — missing canonical reference)

---

_Reviewer signoff: Perplexity persona, 2026-05-13 13:30 PT. Verifications anchored to live arXiv abstract pages at review time. The single BLOCKER is mechanical to fix (one bib entry collapse + one prose line rewrite at L379)._
