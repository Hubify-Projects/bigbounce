# P4 R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex`
**Version reviewed:** v1.0.49 (46 bibitems, post-v1.0.48→v1.0.49 R-round-2 wave: 9 new bibitems added, Shamir/Iye/Cabass/Eskilt closures verified).
**Scope:** Adversarial spot-check of 11 high-stakes bibitems on the post-v1.0.48 list against arXiv abstract pages, ADS bibcodes, and journal landing pages, with a focused hunt for NEW errors not caught by the previous two R-rounds. Findings below cite the verification source for each error.
**Method:** WebSearch + WebFetch against `arxiv.org`, `ui.adsabs.harvard.edu`, `journals.aps.org`, `academic.oup.com`. Eleven items fully traced; remainder spot-checked at the title-string level only.
**Date:** 2026-05-13 17:30 PT.

---

## TL;DR

- **Total findings: 8** — **2 BLOCKER, 4 MAJOR, 1 MINOR, 1 NIT.**
- **Most concerning citation error (one sentence):** The `Hart:2016` bibitem at L2909-2912 mis-titles the paper as *"Galaxy Zoo: comparing the demographics of spiral arm number and pitch angle"*; the actual MNRAS 461, 3663 (2016) paper is titled *"Galaxy Zoo: comparing the demographics of spiral arm number and **a new method for correcting redshift bias**"* — the "pitch angle" framing belongs to the **2017** Hart-Bamford-Hayes follow-up at MNRAS 472, 2263 (arXiv:1708.04628). As-printed the bibitem is a Frankenstein splice of two different Hart papers and (because the body text invokes Hart:2016 specifically for vote-bias / redshift-debiasing in §IV.D) the wrong-title risk is that a reader who follows the cite expects pitch-angle content and instead lands on a debiasing methodology paper.
- **Two new BLOCKERs that prior R-rounds missed:** wrong-title on Hart:2016 (above) and wrong-title on Yu:2020 (P4 prints *"Probing primordial chiral gravitational waves with galaxy intrinsic alignments"* but PRL 124, 101302 is actually titled *"Probing Primordial Chirality with Galaxy Spins"*). Both titles are plausibly LLM-fabricated; both are easy to verify against ADS in <30 seconds; both survived the prior P4 R-rounds.
- New corrections from v1.0.48 (Shamir:2020 reverted to Ap&SS 365 / arXiv:2007.16116, Iye:2020 arXiv ID fixed to 2011.00662, Cabass:2023 title fixed, Eskilt:2023 stitched fix) all verify clean against canonical sources.
- Hou:2023, Cahn:2021, Komatsu:2022, Bamford:2009, Walmsley:2022, Hayes:2017, Eskilt:2023 metadata (venue + volume + page + arXiv ID + year) all verify clean. The only errors are in the prose titles of Hart:2016, Yu:2020, Hayes:2017, and the year-on-page of Iye:2020.

---

## BLOCKERs

### B1. `Hart:2016` bibitem is mis-titled (wrong paper title; right authors+venue)

- **Location:** L2909-2912, `chirality_catalog_paper.tex`.
- **Claimed title in bibitem:** *"Galaxy Zoo: comparing the demographics of spiral arm number and pitch angle"*.
- **Verified canonical title (source: ADS `2016MNRAS.461.3663H`; Oxford Academic MNRAS 461, 3663 landing page; arXiv:1607.01019):** **"Galaxy Zoo: comparing the demographics of spiral arm number and a new method for correcting redshift bias"**.
- Venue (MNRAS **461**, 3663, 2016), authors (Hart, Bamford, Willett, Masters, et al.), and arXiv ID (1607.01019) are correct. **The title string is fabricated** — it appears to be a conflation with **Hart+2017** (MNRAS **472**, 2263, arXiv:1708.04628), *"Galaxy Zoo and SpArcFiRe: Constraints on spiral arm formation mechanisms from spiral arm number and pitch angles"*, which IS about pitch angles. The 2016 paper is specifically about debiasing GZ2 vote fractions against redshift bias for spiral arm number.
- **Why this matters:** The body cite at L1418-1419 (and the §IV.D vote-bias paragraph) invokes Hart:2016 for **vote-bias correction** — which IS what the actual 2016 paper covers. So the substantive argument is intact. But (i) any peer reviewer who knows the GZ literature will read the title and immediately know it's wrong, and (ii) any reference manager / arXiv crosswalk will flag a title mismatch on this bibkey. The shipped PDF will read as sloppy at exactly the moment we are leaning on GZ vote-bias as the principal observational systematic.
- **Correct bibitem (drop in verbatim):**
  ```
  \bibitem{Hart:2016}
  R.~E.~Hart, S.~P.~Bamford, K.~W.~Willett \textit{et~al.},
  ``Galaxy Zoo: comparing the demographics of spiral arm number and a new method for correcting redshift bias,''
  Mon.\ Not.\ R.\ Astron.\ Soc.\ \textbf{461}, 3663 (2016), arXiv:1607.01019.
  ```

### B2. `Yu:2020` bibitem is mis-titled (wrong paper title; right authors+venue)

- **Location:** L2919-2922.
- **Claimed title in bibitem:** *"Probing primordial chiral gravitational waves with galaxy intrinsic alignments"*.
- **Verified canonical title (source: PRL 124, 101302 landing page at `journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.101302`; arXiv abstract page for 1904.01029; PubMed PMID 32216440):** **"Probing Primordial Chirality with Galaxy Spins"**.
- Authors (Yu, Motloch, Pen, Yu, Wang, Mo, Yang, Jing — paper.tex truncates to "Yu, Motloch, Pen et al.", fine), venue (PRL **124**, 101302), year (2020), and arXiv ID (1904.01029) are correct. **The title string is fabricated** — it mis-frames the observable as "galaxy intrinsic alignments" (a quadrupole shape statistic) when the actual paper measures **spin direction correlations** (a vector / dipole statistic). These are distinct observables and the difference is load-bearing for P4 §VIII.A.iii, where Yu+2020 is cited as the **precursor** for the spin-dipole forecast.
- **Why this matters:** Worse than Hart:2016 because (i) the wrong-title also wrongly characterizes the *physics* (alignments vs. spins are different), and (ii) the chirality literature is small enough that anyone who works in it will recognize Yu+2020 by the correct title and flag the mismatch immediately. This is exactly the kind of citation slop that gets P4 sent back for revision at MNRAS.
- **Correct bibitem (drop in verbatim):**
  ```
  \bibitem{Yu:2020}
  H.-R.~Yu, P.~Motloch, U.-L.~Pen \textit{et~al.},
  ``Probing primordial chirality with galaxy spins,''
  Phys.\ Rev.\ Lett.\ \textbf{124}, 101302 (2020), arXiv:1904.01029.
  ```

---

## MAJORs

### M1. `Hayes:2017` bibitem title uses non-canonical "chirality bias" wording where journal uses "winding bias"

- **Location:** L2899-2902.
- **Claimed title in bibitem:** *"On the nature and correction of the spurious S-wise spiral galaxy **chirality** bias in SDSS DR7"*.
- **Verified canonical title (source: ADS `2017MNRAS.466.3928H`; MNRAS 466, 3928 landing page; arXiv:1701.06587):** **"On the nature and correction of the spurious S-wise spiral galaxy *winding* bias in *Galaxy Zoo 1*"**.
- Two-word delta from the published title: "chirality" should be "winding"; "SDSS DR7" should be "Galaxy Zoo 1". The underlying paper IS the right paper (Hayes, Davis & Silva 2017, addressing the S-wise excess in GZ1 votes); venue + volume + page + arXiv ID all verify clean. But the title-substitution is non-trivial: "winding bias" is the canonical literature term for the vote-bias mechanism this manuscript leans on in §IV.D, and re-naming it "chirality bias" is the *exact* terminological collision P4 is trying to avoid (the whole point of the paper is that the *true* chirality bias is what we measured, distinct from the *vote-process* winding bias). Using the wrong-title here weakens P4's own terminological discipline.
- **Correct bibitem:**
  ```
  \bibitem{Hayes:2017}
  W.~B.~Hayes, D.~Davis, and P.~Silva,
  ``On the nature and correction of the spurious S-wise spiral galaxy winding bias in Galaxy Zoo 1,''
  Mon.\ Not.\ R.\ Astron.\ Soc.\ \textbf{466}, 3928 (2017), arXiv:1701.06587.
  ```

### M2. `Iye:2020` cite-key year mismatches publication year on the page

- **Location:** L2784-2787 + every body cite that says "Iye+2020".
- **Claimed:** bibkey is `Iye:2020`; bibitem body says "(2021)"; multiple body sentences refer to "Iye+2020".
- **Verified (source: ADS `2021ApJ...907..123I`):** The paper was **submitted to arXiv 2020-11-02** but **published in ApJ 907, 123 (2021)**. Year=2021 in the bibitem body is correct; the bibkey "Iye:2020" is conventional (refers to submission year) but a fastidious reviewer will flag this as inconsistent with the body-text "Iye+2020" callouts when the journal record shows 2021.
- **Recommendation:** Either (a) leave bibkey as Iye:2020 + change in-text callouts to "Iye+2021" consistently (preferred; matches journal record); or (b) accept the convention and add a `Note added:` somewhere in §VII.A that the work is `Iye et al. 2021` per ApJ. Option (a) is one-line `sed` change.

### M3. `Eskilt:2023` author/collaboration credit is non-standard

- **Location:** L2879-2882.
- **Claimed in bibitem:** *"J.~R.~Eskilt \textit{et~al.} (Cosmoglobe Collaboration)"*.
- **Verified (source: A&A 679, A144 landing page; arXiv:2305.02268):** The published author list is **31 named authors** (Eskilt, Watts, Aurlien, Basyrov, Bersanelli, ...) with the Cosmoglobe collaboration acknowledged in affiliation/funding, **not as a formal author-list parenthetical** in the manner of Planck Collaboration or ACT Collaboration. The published author block is a flat 31-name list; treating it as a `(Cosmoglobe Collaboration)` author-line is structurally analogous to citing a 30-author Planck paper as `(Planck Collaboration)` — but Cosmoglobe does not use that convention in this paper's masthead. The minimum-friction fix is to drop the parenthetical:
  ```
  \bibitem{Eskilt:2023}
  J.~R.~Eskilt \textit{et~al.},
  ``Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data,''
  Astron.\ Astrophys.\ \textbf{679}, A144 (2023), arXiv:2305.02268.
  ```
- **Why MAJOR not NIT:** A&A is one of the journals P4 might submit to; A&A's reference style explicitly distinguishes between "et al." author lists and parenthetical-collaboration cites. Getting this wrong on an A&A paper that you're citing IN an A&A submission is a free triage flag.

### M4. Missing canonical reference — Philcox+2022 BOSS detection paper has the wrong cite-year

- **Location:** L2874-2877 (`Philcox:2023` bibitem).
- **Claimed:** *"Probing parity-violating physics with the BOSS galaxy survey," Phys. Rev. D **106**, 063501 (2022), arXiv:2206.04227*.
- **Verified:** Venue + volume + page + arXiv ID all correct; the **year is 2022**, not 2023. The bibkey "Philcox:2023" is a misnomer that risks confusion with the Cabass+Ivanov+Philcox **2023** PRD paper (also cited as `Cabass:2023`, PRD 107). Two adjacent PRD bibitems both keyed to "2023" with one of them actually being 2022 is the kind of small-detail error that compounds with B1 and B2 to make the whole bibliography look thrown together. Rename the bibkey to `Philcox:2022` and update the four body cites:
  ```
  \bibitem{Philcox:2022}
  O.~H.~E.~Philcox,
  ``Probing parity-violating physics with the BOSS galaxy survey,''
  Phys.\ Rev.\ D \textbf{106}, 063501 (2022), arXiv:2206.04227.
  ```

---

## MINORs

### m1. Year on `Holst:1995pc` bibkey vs. body conflict

- **Location:** L2859-2862. Bibkey is `Holst:1995pc` (1995, presumably the arXiv year for gr-qc/9511026), but the bibitem body correctly prints "(1996)" since PRD 53, 5966 was the 1996 published-version. Self-consistent within the bibitem; only inconsistent if any in-text "Holst (1995)" callout is used. The PDF callout is `\cite{Holst:1995pc}` which prints "[Holst 1996]" via the bibitem body, so this is cosmetic. NIT-tier, but flagging because R-rounds have been keying off bibkey year. No fix required.

---

## NITs

### n1. `DESI:2016` bibitem is missing a title

- **Location:** L2939-2941.
- **Claimed:** Just `{DESI Collaboration}, A.~Aghamousa, J.~Aguilar \textit{et~al.}, arXiv:1611.00036 (2016).` No title.
- **Recommendation:** Add the title for completeness. Other arXiv-only bibitems (Wightman:2019, Zonca:2019, Harris:2020, McKinney:2010, Paszke:2019) are similarly title-shy by software-package convention; this one is a survey design report and should follow the academic-paper title convention. Suggested:
  ```
  \bibitem{DESI:2016}
  {DESI Collaboration}, A.~Aghamousa, J.~Aguilar \textit{et~al.},
  ``The DESI Experiment Part I: Science, Targeting, and Survey Design,''
  arXiv:1611.00036 (2016).
  ```

---

## Items verified CLEAN (no findings)

The following high-stakes bibitems were fully traced against the canonical journal landing page / ADS / arXiv and verify clean on every field (authors, title, venue, volume, page, year, arXiv ID):

| bibkey | Verified source | All fields clean? |
|--------|------------------|-------------------|
| `Hou:2023` | MNRAS 522, 5701 landing page; arXiv:2206.03625 | YES |
| `Cahn:2021` | PRL 130, 201002 landing page; arXiv:2110.12004 | YES |
| `Komatsu:2022` | Nat.\ Rev.\ Phys.\ 4, 452 (2022) DOI:10.1038/s42254-022-00452-4 | YES |
| `Walmsley:2022` | ADS `2022MNRAS.509.3966W`; arXiv:2102.08414 | YES |
| `Bamford:2009` | ADS `2009MNRAS.393.1324B`; arXiv:0805.2612 | YES |
| `Cabass:2023` (title) | PRD 107, 023523; Note: title is *"Colliders and ghosts: Constraining inflation with the parity-odd galaxy four-point function"* — paper.tex has it correctly post-v1.0.48 closure. | YES (clean post-closure) |
| `Shamir:2020` (post-revert) | Ap&SS 365, 136; arXiv:2007.16116 — confirmed not retracted | YES (clean post-revert) |
| `Iye:2020` arXiv ID (post-fix) | arXiv:2011.00662 → ApJ 907, 123 | YES on ID; year-discord noted in M2 |
| `Eskilt:2023` title + venue + arXiv | A&A 679, A144 (2023); arXiv:2305.02268 — title is canonical | YES on title; collaboration parenthetical flagged in M3 |

---

## Summary count

| Severity | Count |
|----------|-------|
| BLOCKER  | 2     |
| MAJOR    | 4     |
| MINOR    | 1     |
| NIT      | 1     |
| **Total**| **8** |

Citation health post-v1.0.49: 4 of 5 v1.0.48 closures verify clean (Shamir, Iye arXiv ID, Cabass title, Eskilt title); 1 of 5 has a residual structural issue (Eskilt collaboration parenthetical, M3). The two new BLOCKERs (Hart:2016 title, Yu:2020 title) appear to be **pre-existing** errors that survived the v1.0.47 and v1.0.48 R-rounds because the prior reviews focused on venue/page/arXiv-ID corrections and did not adversarially re-verify titles. Both are 1-line `sed` fixes.

**Recommended close-out commit:** single-pass `sed` to fix the four title strings (Hart:2016, Yu:2020, Hayes:2017), drop the Eskilt collaboration parenthetical, rename `Philcox:2023` → `Philcox:2022` with body-cite update, optionally add the DESI:2016 title — net diff under 20 lines, no figure / no science changes, recompile + restamp.

---

## Sources used

- ADS bibcode `2017MNRAS.466.3928H` ([https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.3928H/abstract](https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.3928H/abstract))
- ADS bibcode `2016MNRAS.461.3663H` ([https://ui.adsabs.harvard.edu/abs/2016MNRAS.461.3663H/abstract](https://ui.adsabs.harvard.edu/abs/2016MNRAS.461.3663H/abstract))
- ADS bibcode `2022MNRAS.509.3966W` ([https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.3966W/abstract](https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.3966W/abstract))
- ADS bibcode `2009MNRAS.393.1324B` ([https://ui.adsabs.harvard.edu/abs/2009MNRAS.393.1324B/abstract](https://ui.adsabs.harvard.edu/abs/2009MNRAS.393.1324B/abstract))
- ADS bibcode `2021ApJ...907..123I` ([https://ui.adsabs.harvard.edu/abs/2021ApJ...907..123I/abstract](https://ui.adsabs.harvard.edu/abs/2021ApJ...907..123I/abstract))
- PRL 124, 101302 landing page ([https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.101302](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.101302))
- PRL 130, 201002 landing page ([https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.201002](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.201002))
- PRD 107, 023523 landing page ([https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.023523](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.023523))
- A&A 679 A144 ([https://www.aanda.org/articles/aa/full_html/2023/11/aa46829-23/aa46829-23.html](https://www.aanda.org/articles/aa/full_html/2023/11/aa46829-23/aa46829-23.html))
- MNRAS 522, 5701 Oxford Academic ([https://academic.oup.com/mnras/article/522/4/5701/7169316](https://academic.oup.com/mnras/article/522/4/5701/7169316))
- Nature Reviews Physics 4, 452 (Komatsu) DOI ([https://doi.org/10.1038/s42254-022-00452-4](https://doi.org/10.1038/s42254-022-00452-4))
- arXiv abstract pages for each verified preprint (2007.16116, 2011.00662, 1904.01029, 1701.06587, 1607.01019, 2102.08414, 0805.2612, 2206.03625, 2110.12004, 2202.13919, 2210.16320, 2305.02268, 2206.04227, gr-qc/9511026, 1611.00036)
