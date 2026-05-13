# P4 R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Version reviewed:** v1.0.47 (38 bibitems, post-v1.0.46→v1.0.47 standalone-publication wave).
**Scope:** Spot-check 9 high-stakes bibitems flagged in the v1.0.46→v1.0.47 closure (Iye+2020, Shamir:2012, Shamir:2020, Holst:1995pc, LueWangKamionkowski:1999, Cabass:2023, Philcox:2023, Eskilt:2023, the three Golden:2026 self-references) plus a sweep for missing canonical literature. Numbers below are verified against arXiv abstract pages, ADS bibcodes, and journal landing pages (sources listed inline per finding).
**Method:** WebSearch + WebFetch against arxiv.org / ui.adsabs.harvard.edu / journal pages. Spot-check, not exhaustive; the most consequential bibitems were fully traced.
**Date:** 2026-05-13 10:52 PT.

---

## TL;DR

- **Total findings: 11** — **2 BLOCKER, 4 MAJOR, 3 MINOR, 2 NIT.**
- **Most concerning citation error (one sentence):** The `Shamir:2020` bibitem at L2543-2546 was *changed in v1.0.47* from the correct Ap&SS 365, 136 (arXiv:2007.16116) entry to a **fictitious** PASP 132, 124102 (arXiv:2009.09222) entry — neither the venue, nor the volume, nor the arXiv ID match any published Shamir paper that I can locate, and the actual paper this manuscript cites and refutes (the SDSS+Pan-STARRS multipole/parity claim) was published in Ap&SS 365, 136 (2020).
- v1.0.47 also introduced a **wrong arXiv ID on `Iye:2020`** (gave 2010.04830, should be 2011.00662) and a **wrong title on `Cabass:2023`**.
- Aside from those three, the remaining post-v1.0.46 corrections (Shamir:2012 → PLB 715, 25; Holst published-year 1996 in bibitem body) verify clean against arXiv/journal records.

---

## BLOCKERs

### B1. `Shamir:2020` bibitem points to wrong paper entirely (venue + arXiv ID both wrong)

- **Location:** L2543-2546, `chirality_catalog_paper.tex`.
- **Claimed in bibitem:** `Publ.\ Astron.\ Soc.\ Pacific \textbf{132}, 124102 (2020), arXiv:2009.09222`.
- **Verified reality (sources: ADS bibcode `2020Ap&SS.365..136S`, Springer DOI 10.1007/s10509-020-03850-1, arXiv abstract page for 2007.16116):**
  - **Venue:** Astrophysics and Space Science **365**, 136 (2020).
  - **arXiv ID:** **2007.16116** (submitted 2020-07-29).
  - The PASP record for vol. 132 article 124102 does **not** correspond to a Shamir parity / multipole paper — `2009.09222` is unrelated content.
- **What this paper is supposed to cite:** the Shamir 2020 "Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles" paper, which is the load-bearing antagonist for the entire P4 refutation narrative (the ~3% claim Shamir reports that this paper refutes by factor of 9). The title text in the bibitem IS correct; the metadata is wrong.
- **Note on closure history:** v1.0.46 → v1.0.47 SSOT log records this as "M14 closed: Shamir:2020 venue updated Ap&SS 365, 136 → PASP 132, 124102 + arXiv:2009.09222". **The "update" went the wrong direction.** Pre-v1.0.47 the bibitem was correct (Ap&SS 365, 136); the v1.0.47 wave replaced a correct entry with a fictitious one. Likely root cause: confusion with one of the *other* Shamir handedness papers, or an LLM-fabricated metadata pair. Either way, this is the highest-priority fix in the bib file.
- **Correct bibitem (drop in verbatim):**
  ```
  \bibitem{Shamir:2020}
  L.~Shamir,
  ``Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,''
  Astrophys.\ Space Sci.\ \textbf{365}, 136 (2020), arXiv:2007.16116.
  ```

### B2. `Iye:2020` bibitem has wrong arXiv ID

- **Location:** L2563-2566.
- **Claimed in bibitem:** `arXiv:2010.04830`.
- **Verified reality (sources: arXiv listing for the "Spin Parity of Spiral Galaxies III" paper; ADS):**
  - **Correct arXiv ID:** **2011.00662** ("Spin Parity of Spiral Galaxies III -- Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations").
  - arXiv:2010.04830 is an unrelated submission (e-learning readiness, Yousef et al. 2020) — definitely not the Iye/Yagi/Fukumoto paper this manuscript engages with at §VII.A as the priority claim.
  - **Venue:** ApJ 907, 123 — correct in the bibitem.
- **Why it matters:** Paper §VII.A is the new (v1.0.47) Iye-priority engagement paragraph, framing P4 as the 30× statistical extension of Iye+2020's methodological critique. If a reader follows the arXiv ID printed in the bib, they land on an unrelated CS-education paper and the priority engagement reads as fraudulent / sloppy. This is a high-visibility error.
- **Correct bibitem:**
  ```
  \bibitem{Iye:2020}
  M.~Iye, M.~Yagi, and H.~Fukumoto,
  ``Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,''
  Astrophys.\ J.\ \textbf{907}, 123 (2021), arXiv:2011.00662.
  ```
  (Note: published in 2021 ApJ vol. 907 — minor year clarification, sub-finding tracked in N1 below.)

---

## MAJORs

### M1. `Cabass:2023` bibitem title is wrong

- **Location:** L2648-2651.
- **Claimed title:** "Parity violation in the early universe".
- **Verified title (source: APS DOI 10.1103/PhysRevD.107.023523):** **"Colliders and ghosts: Constraining inflation with the parity-odd galaxy four-point function"**.
- Venue (Phys. Rev. D **107**, 023523, 2023) and arXiv ID (2210.16320) are correct; authors (Cabass, Ivanov, Philcox) are correct. **Only the title string is wrong.**
- The body cite at L2317 doesn't quote the title, so the substantive argument survives — but the bibitem as printed is non-locatable: a reader searching for "Parity violation in the early universe" against arXiv:2210.16320 will get a mismatch warning on every reference manager. Replace with the real title.

### M2. Missing canonical reference: Hou, Slepian & Cahn (2023) BOSS 4PCF measurement

- **Location:** §VIII.A.ii parity-odd-galaxy-trispectrum paragraph (L2316-2327).
- **What is cited now:** Cabass:2023 (theory side) and Philcox:2022 (the methodology-paper / blind test side, miscited as Philcox:2023).
- **What is missing:** **Hou, Slepian & Cahn 2023**, MNRAS **522**, 5701, arXiv:2206.03625 — the headline parity-odd 4PCF measurement on BOSS DR12 CMASS + LOWZ that detects the signal at **7.1σ (CMASS) / 3.1σ (LOWZ)**, much higher significance than Philcox+2022's blind-test 2.9σ rank-test result.
- **Why this is a problem:** P4 §VIII.A.ii claims to translate the morphology dipole bound onto "the leading observable parity-violation channel" and cites only Philcox; but in the published literature Hou+2023 is the higher-significance and more directly comparable claim, and *any* peer-reviewer in the parity-violation space will flag the omission as either (a) lack of literature familiarity or (b) cherry-picking the less-significant detection. The two BOSS measurements are universally cited together. Add the Hou+2023 cite alongside Philcox in the same sentence.
- **Suggested bibitem:**
  ```
  \bibitem{Hou:2023}
  J.~Hou, Z.~Slepian, and R.~N.~Cahn,
  ``Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,''
  Mon.\ Not.\ R.\ Astron.\ Soc.\ \textbf{522}, 5701 (2023), arXiv:2206.03625.
  ```

### M3. Missing canonical reference: Cahn, Slepian & Hou (the 4PCF-parity test foundational paper)

- **Location:** Same §VIII.A.ii block as M2.
- **What is missing:** Cahn, Slepian & Hou, "A Test for Cosmological Parity Violation Using the 3D Distribution of Galaxies," which is the theoretical-foundation paper for the 4PCF-parity channel. Without this cite, the manuscript jumps straight to Cabass / Philcox / (eventually) Hou measurements without acknowledging the test was *proposed* before it was *measured*. ADS lists this as Cahn, Slepian & Hou 2021, arXiv:2110.12004 — please verify the venue/year against the current ADS record before insertion; my spot-check returned the Semantic Scholar entry and the arXiv abstract page but did not confirm the published venue/volume.

### M4. `Eskilt:2023` bibitem title is wrong (mis-titled as "Joint Planck and ACT measurement")

- **Location:** L2658-2661.
- **Claimed title:** "Joint Planck and ACT measurement of cosmic birefringence".
- **Verified title (source: A&A landing page for vol. 679, A144; arXiv 2305.02268):** **"Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data"**.
- Author list ("Eskilt et al. (Cosmoglobe Collaboration)") and venue (A&A **679**, A144) and arXiv ID (2305.02268) are correct; **only the title is wrong**.
- Note: the β = 0.342° ± 0.094° value the body of P4 leans on (line 2309) is correctly from this Eskilt+2023 Cosmoglobe paper, so the *science* is fine. But the title misquote suggests the citation was generated rather than read. Also: there *is* a separate Eskilt-led Planck+ACT joint birefringence paper (Eskilt 2022, A&A 662, A10, arXiv:2201.13347, single-mission Planck) plus follow-ups — if the manuscript means to cite the **Cosmoglobe** result the title needs to read "Cosmoglobe DR1 results. II. …"; if it means the **ACT-only or Planck+ACT-joint** result it needs a different arXiv ID and different title. Pick one and reconcile.

---

## MINORs

### m1. `Philcox:2023` bibitem-key year mismatch — paper is 2022

- **Location:** L2653-2656.
- The cite-key is `Philcox:2023` but the published paper is **Phys. Rev. D 106, 063501 (2022)**, arXiv:2206.04227 — i.e., calendar year 2022. The bib body correctly prints "(2022)", but the key suggests 2023, which mis-sorts under any year-keyed bibliography list and is a small but real signal of citation-management sloppiness. Either rename the key to `Philcox:2022` (recommended; touch all `\cite{Philcox:2023}` call sites) OR document the convention.
- Single body call-site is L2317.

### m2. `Holst:1995pc` cite key — year of publication is 1996

- **Location:** L2638-2641.
- arXiv submission year = 1995 (gr-qc/9511026, submitted Nov 1995). Published year = 1996 (Phys. Rev. D 53, 5966–5969). The bibitem body now correctly prints "(1996)" — that's the v1.0.47 fix; the cite key itself remains `Holst:1995pc`, which is a long-standing INSPIRE-style key (`pc` is the INSPIRE TeX-key suffix for arXiv-submission cohort) and is conventional, so this is not a fix-required item — flagging for awareness only.

### m3. Three `Golden:2026` self-references lack arXiv / DOI / preprint-server hooks

- **Locations:** L2663-2676 (`Golden:2026P1A`, `Golden:2026P2`, `Golden:2026P3`).
- All three are formatted as `H.~Golden, "Title," in preparation (2026), Hubify-2026-001` (or -002, -003).
- "Hubify-2026-NNN" is a non-standard internal preprint number that will not resolve at any preprint server or DOI registry, and will confuse a referee who tries to follow the cross-reference. Two options:
  - (a) **Replace** "Hubify-2026-NNN" with the actual arXiv ID at the moment of arXiv submission of each companion paper (the SSOT plan is to submit P1A and P4 together for cross-resolvability — do that and the cross-cites become live URLs).
  - (b) **Add** a stable DOI placeholder (e.g., Zenodo deposit) and the bigbounce.hubify.app URL, so the bibitem at least resolves to something a reader can follow. Current state ("Hubify-2026-001" with no URL) is the worst of both worlds.
- This is not blocking — it's standard practice to have "in preparation" companion cites — but for the standalone-publication readiness wave that v1.0.47 claims, this is exactly the kind of seam an A&A / ApJ / PRD referee will flag.

---

## NITs

### N1. `Iye:2020` published year is **2021**, not 2020

- ADS bibcode is `2021ApJ...907..123I`; the volume 907 issue ran Jan 2021. The cite key `Iye:2020` likely tracks the arXiv submission year (Nov 2020). Internal-consistency only — most journals will accept either convention, but if the paper elsewhere uses the published-year convention (e.g., for Shamir 2020), it should be `Iye:2021` here. Low priority.

### N2. v1.0.47 SSOT claim "arXiv IDs added to 26+ bibitems" is true in count, but two of the additions are wrong

- The SSOT log records 26+ arXiv IDs added in v1.0.47 as a quality improvement. Spot-check of five random arXiv IDs in the bib (Walmsley 2309.11425, Dey 1804.08657, Astropy 2206.14220, Alonso 1809.09603, HEALPix astro-ph/0409513) — all five resolve correctly to the cited papers. The wave's mechanical task **succeeded for the bulk of the bibliography**.
- The two failures (B1 `Shamir:2020` → 2009.09222 wrong; B2 `Iye:2020` → 2010.04830 wrong) are concentrated in exactly the two bibitems that v1.0.47 also *modified for venue/methodology engagement*, i.e., the high-touch entries got the high error rate. This is a process-quality finding: when a bibitem is being edited for multiple reasons in the same wave, the metadata-paste step is more error-prone. Recommend a 30-second post-wave WebFetch verification on any bibitem that received both a venue change AND an arXiv-ID change in the same commit. (Mechanical bulk additions for already-stable entries appear to have been done carefully.)

---

## Out of scope (verified but no finding required)

- **`Shamir:2012` venue correction → PLB 715, 25 + arXiv:1207.5464** (v1.0.47 M13): **verified clean.** Physics Letters B accepted, DOI 10.1016/j.physletb.2012.07.054, Lior Shamir sole author, exactly as claimed.
- **`LueWangKamionkowski:1999` → PRL 83, 1506 + astro-ph/9812088**: **verified clean.** PRL 83, page 1506, published 1999, arXiv astro-ph/9812088 confirmed.
- **`Walmsley:2023` → MNRAS 526, 4768 + arXiv:2309.11425**: **verified clean** against the MNRAS landing page and the ADS bibcode 2023MNRAS.526.4768W. (This is the GZ DESI methodology paper underwriting the entire P4 catalog.)

---

## Counts

| Severity | Count |
|----------|-------|
| BLOCKER  | 2     |
| MAJOR    | 4     |
| MINOR    | 3     |
| NIT      | 2     |
| **Total** | **11** |

---

## Most concerning single citation error

The `Shamir:2020` bibitem at L2543-2546 was *changed in v1.0.47* from a correct Ap&SS 365, 136 / arXiv:2007.16116 entry to a fabricated PASP 132, 124102 / arXiv:2009.09222 entry — neither the journal record nor the arXiv ID matches any published Shamir paper, so the load-bearing antagonist citation for the entire P4 refutation narrative is, as of v1.0.47, non-locatable.
