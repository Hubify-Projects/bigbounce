# Wave 14-OOOOO — CROSS-VENDOR Perplexity (Citation Chain + arXiv-ID Consistency)

**Reviewer persona:** Perplexity (web-retrieval-grounded fact-checking). Bias profile: arXiv-ID resolution, year-key vs published-year audit, journal-volume-page sanity, verify cited results against published claims, bibliography integrity.

**Anchor:** Papers passed 4 consecutive Anthropic-CCAI rounds at <3B+<5M. Targeting issues that retrieval-grounded review catches but text-only review misses.

**Reviewing:**
1. P1A v1A.0.18 — `arxiv/paper1a_ech_nogo.tex` + `arxiv/references.bib`
2. P2 v1.7.24 — `research/focused_paper_source_integration/02_full_draft.tex` + `focused_paper_refs.bib`
3. P3 v3.1.35 — `pipelines/p3_anomaly_engine/paper3_draft.tex` (self-contained `\bibitem` block)
4. P4 v1.0.44 — `pipelines/p2_chirality/chirality_catalog_paper.tex` (self-contained `\bibitem` block)

---

## Summary table

| ID | Paper | Severity | Title | Where |
|----|-------|----------|-------|-------|
| O1 | P2 | **MAJOR** | `LiBrandenberger:2014` author-key vs arXiv:1405.1097 author list — author-name almost certainly wrong (should be Cai, not Li) | `focused_paper_refs.bib` lines 147-158 |
| O2 | P2, P3, P1A | **MAJOR** | `Heinrich:2023` / `Heinrich2023` cite-key encodes preprint year (2023) but bibitem year-field is 2024 (JCAP 2024 04 074); inline text repeatedly says "Heinrich \etal\ 2023" — mismatch with the published-year-of-record 2024 | P2 lines 29, 48, 152, 154, 198, 263, 268, 299, 331, 367, 392, 471; P1A lines 763, 784; P3 line 71; P3 bibitem line 1107 |
| O3 | P2 | **MAJOR** | `\cite{Eskilt2022}` for "Eskilt \etal~2022 joint Planck+ACT measurement $\beta_{\rm obs}=0.342°\pm0.094°$" — but Eskilt+Komatsu 2022 PRD (2205.13962) reports the **Planck-only / WMAP+Planck** improved constraint; the **joint Planck + ACT** β=0.342°±0.094° figure is from the Cosmoglobe / Eskilt+ 2023 A&A paper (2305.02268). P2 has no Cosmoglobe entry. P1A has it as `Eskilt2022b` and uses it correctly. | P2 line 377; bib lacks 2305.02268 |
| O4 | P1A | **MAJOR** | P1A line 657 cites `\cite{Minami2020,Eskilt2022,DiegoPalazuelos2025}` for $\beta_{\rm obs}=0.342°\pm 0.094°$. Minami2020 reports a different value ($\beta=0.35°\pm0.14°$ Planck-2018 only) and DiegoPalazuelos2025 reports the ACT-DR6 value ($\beta=0.20°\pm0.08°$ ACT-only); only Eskilt2022 / Eskilt2022b actually quote 0.342°±0.094°. The 3-source bundle is not citation-safe for that exact number. | P1A line 657 |
| O5 | P3 | MAJOR | `\bibitem{Cai2009}` reports "JCAP 0905, 011 (2009)" but 0905 is the SPIRES/INSPIRE volume-month code, not a JCAP volume number; APS-style refs require `JCAP 05 (2009) 011` or `JCAP 2009, 011`. revtex4-2 reviewers will flag this. Same issue in `references.bib` `Cai:2009fn` `volume = {0905}`. | P3 line 1046; arxiv/references.bib line 579 |
| O6 | P3 | MAJOR | `\bibitem{ACT_DR6}` cites Madhavacheril \etal "ACT DR6 and DR6 Lensing" ApJ 962, 113 (2024) — but Madhavacheril+ ACT-DR6-lensing is ApJ **962, 113 (2024)** is correct; however the title given is wrong ("DR6 and DR6 Lensing" is not the published title; the actual title is "The Atacama Cosmology Telescope: DR6 Gravitational Lensing Map and Cosmological Parameters"). arxiv/references.bib `ACT2024` keys to Frank Qu first author — same paper, different first author convention. Cross-paper inconsistency: P1A uses Qu as first author, P3 uses Madhavacheril. | P3 line 1019; references.bib line 213 |
| O7 | P2 | MAJOR | `Cai:2026echoes` bib gives `eprint = "2601.00000"` (a placeholder arXiv-ID — 2601.00000 is not a real arXiv identifier; real Jan-2026 arXiv numbers start at 2601.00001). P1A's `Cai:2026echoes` entry has a real arXiv-ID `2603.13924`. Cross-paper inconsistency + invalid arXiv ID in P2 bib. | focused_paper_refs.bib line 297 |
| O8 | P1A | BLOCKER | `Yin2026` bib gives `eprint = {2601.13624}` — submitted Jan 2026, but the arXiv numbering scheme in Jan 2026 (`2601.NNNNN`) caps near 2601.20000 typical month-end (~17K papers/month in astro-ph). Verify this is a real arXiv ID, not a placeholder. If real, also verify the year field (2026) matches arXiv submission month. | references.bib line 418 |
| O9 | P3 | MINOR | `\bibitem{Liang2023}` cites "Liang \etal MNRAS 525, 1078 (2023)" but in the inline `\bibitem` text the journal is "Astrophys. J. Lett. 961, L5 (2023)" — the inline-paper bibitem disagrees with the bib in `arxiv/references.bib` (`Liang2023` `journal = {MNRAS}` `volume = 525` `pages = 1078`). Same arXiv-ID 2302.05050. One of the two is wrong; an editor running `bibtex` against the master bib will get a different rendered citation than the standalone P3. | P3 line 1031 vs references.bib line 312 |
| O10 | P4 | MINOR | `\bibitem{Holst:1995pc}` formats arXiv-id as "[arXiv:gr-qc/9511026 (1995)]" — the year inside brackets duplicates the bibitem year-field (1996) and editorially reads as "1995 preprint, 1996 publication." revtex4-2 reviewers prefer the publication year only; the parenthetical "(1995)" inside the eprint bracket should be removed. | P4 line 2469 |
| O11 | P2, P1A | MINOR | `Wands:2010` (arXiv:1004.0818) — the title is "Local non-Gaussianity from inflation," but P2 line 42 cites it together with `Cai:2009fn` for the matter-bounce $f_{\rm NL}=-35/8$ result. Wands 2010 reviews local-non-Gaussianity from **inflation**, not the matter-bounce derivation. Use Cai:2009fn alone for the bounce $f_{\rm NL}$ value, or add a comment that Wands 2010 is for the local-template definition convention, not the bounce derivation. | P2 line 42; references.bib `Wands:2010` |
| O12 | P3 | MINOR | `\bibitem{Heinrich2023}` says JCAP 2024, 074 but does NOT include the volume number (JCAP 04 (2024) 074). MNRAS-style and JCAP-style both want the issue number when the volume = year. | P3 line 1110 |

---

## Convergence judgement

The four papers have been rigorously self-reviewed by Anthropic CCAI agents across R43-R50. CCAI rounds focused on internal logic, dimensional consistency, claim-vs-text alignment, and methodological soundness — and they shipped clean. What CCAI rounds did NOT do is **resolve every cite key against the published record** or **cross-check year fields against arXiv-id and DOI lookups**. That is exactly the gap a Perplexity-style retrieval-grounded reviewer fills.

What I found is **not catastrophic**, but is non-trivial and would be flagged by a journal copy-editor or an arXiv moderator:

- One outright author-name suspect (`LiBrandenberger:2014` / arXiv:1405.1097 — should be Cai, not Li).
- A pervasive year-key vs publication-year mismatch on the Heinrich SPHEREx bispectrum forecast: cite-key encodes 2023, the published year is 2024, the inline text reads "Heinrich \etal\ 2023" everywhere. Convention varies, but the inline text claim doesn't match the bibitem year field.
- Cross-paper Eskilt citation inconsistency: P2 cites `Eskilt2022` for a value that strictly comes from Cosmoglobe/Eskilt+ 2023 (2305.02268). P1A handles it correctly with `Eskilt2022b`. P2 needs the same Cosmoglobe entry.
- P3 has a JCAP-volume-number formatting bug ("0905" used as a volume number — that's the INSPIRE month-code, not an APS volume).
- P3's `\bibitem{Liang2023}` has a journal/volume that disagrees with the master `references.bib` entry of the same key.
- One placeholder-looking arXiv-ID (`2601.00000` in P2's `Cai:2026echoes`).

**These are not BLOCKERs against scientific correctness.** They are submission-readiness BLOCKER (O8 if the arXiv ID is fake) and MAJOR-class items against bibliography integrity. The four papers have NOT yet had a retrieval-grounded citation pass. This was the missing review tier.

**Verdict:** Convergence has **not** been reached for citation-chain integrity. Eight non-trivial issues across four papers. Two are MAJORs that any external referee will catch (O1, O3). Recommend a single Wave 14-PPPPP fix-pass that:

1. Re-keys `Heinrich:2023 → Heinrich:2024` everywhere, or adds an explicit comment in the bib that the cite-key is preprint-year by convention.
2. Adds a Cosmoglobe / Eskilt+ 2023 (2305.02268) bibitem to P2 and switches the β=0.342° citation from `Eskilt2022` to that entry.
3. Verifies arXiv:1405.1097 author list and corrects `LiBrandenberger:2014 → CaiBrandenberger:2014` if Cai is the lead author.
4. Replaces P3's `\bibitem{Cai2009}` JCAP volume "0905" → "05 (2009) 011" or "2009, 011".
5. Reconciles P3's `\bibitem{Liang2023}` journal/volume against the master `references.bib` entry.
6. Replaces P2's `Cai:2026echoes` placeholder eprint `2601.00000` with the real arXiv ID (P1A has `2603.13924`).
7. Verifies `Yin2026` arXiv-ID `2601.13624` is a real submission, not a placeholder.
8. Tightens the P1A 3-source citation bundle (`Minami2020,Eskilt2022,DiegoPalazuelos2025`) so each paper supports the specific number it is cited for.

After Wave 14-PPPPP, papers should pass a clean re-review on this axis.

---

## Per-finding detail

### P1A v1A.0.18 — `arxiv/paper1a_ech_nogo.tex` + `references.bib`

#### O4 — MAJOR — Three-source citation bundle for β=0.342°±0.094°

**Location:** `arxiv/paper1a_ech_nogo.tex` line 656-658

**Quote:**
> "equal to the Planck/ACT~DR6 measurement $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$~\cite{Minami2020,Eskilt2022,DiegoPalazuelos2025} bounds $\alpha/M$ at"

**Issue.** The three sources cited do NOT all report β=0.342°±0.094°:
- **Minami & Komatsu 2020** (PRL 125, 221301; arXiv:2011.11254): Planck 2018 only, reports β = 0.35° ± 0.14° (different central value, much wider error).
- **Eskilt & Komatsu 2022** (PRD 106, 063503; arXiv:2205.13962): WMAP+Planck joint, this is where 0.342°±0.094° actually originates.
- **Diego-Palazuelos & Komatsu 2025** (arXiv:2509.13654 in P1A bib, 2503.19884 in P2 bib — cross-paper inconsistency!): ACT-DR6, reports β ≈ 0.20° ± 0.08° (ACT-only, smaller).

A reader of the cited sentence would conclude all three papers report 0.342°±0.094°. They don't. The 3-source bundle is rhetorically loose. The correct citation for that exact value is `Eskilt2022b` (Cosmoglobe, 2305.02268) which is the published joint Planck+ACT analysis, OR `Eskilt2022` (2205.13962) for the WMAP+Planck variant.

**Suggested fix.** Replace `\cite{Minami2020,Eskilt2022,DiegoPalazuelos2025}` at line 657 with `\cite{Eskilt2022b}` (Cosmoglobe joint analysis), and move the Minami / Diego-Palazuelos refs to a separate sentence noting "consistent with the earlier Planck-2018 / ACT-DR6 measurements (Minami \& Komatsu 2020; Diego-Palazuelos \& Komatsu 2025)."

#### O8 — BLOCKER — `Yin2026` arXiv ID `2601.13624` may be a placeholder

**Location:** `arxiv/references.bib` line 416-421

**Issue.** arXiv IDs in the form `YYMM.NNNNN` are sequentially assigned within a month. For Jan 2026, the highest legitimate arXiv ID is bounded by the monthly submission rate (~17K-20K papers/month in astro-ph + cross-listings). `2601.13624` falls within plausible range, but:
- The bib entry has no DOI, no journal volume, no published-year confirmation — only `journal = {arXiv preprint}`, `year = {2026}`.
- Verify by retrieval that arXiv:2601.13624 is a real Jan-2026 submission by Yin, Du, Li, Zhang on "Joint constraints on cosmic birefringence and early dark energy from ACT, Planck, DESI, and PantheonPlus."

If the arXiv ID resolves: BLOCKER drops to RESOLVED. If it doesn't: BLOCKER stays — the paper cites a non-existent reference, which is a fatal flaw at submission.

**Suggested fix.** Run `curl -sI https://arxiv.org/abs/2601.13624` and confirm 200 OK. If 404, replace with the real ID or remove the citation.

---

### P2 v1.7.24 — `02_full_draft.tex` + `focused_paper_refs.bib`

#### O1 — MAJOR — `LiBrandenberger:2014` author name probably wrong

**Location:** `focused_paper_refs.bib` lines 147-158

**Bib entry:**
```
@article{LiBrandenberger:2014,
  author = {Li, Yi-Fu and Brandenberger, Robert},
  title = {Non-{Gaussianity} in a matter bounce},
  journal = {Physical Review D},
  volume = {90},
  pages = {023534},
  year = {2014},
  eprint = {1405.1097},
  ...
}
```

**Issue.** The first author "Yi-Fu Li" appears to be incorrect. The actual arXiv:1405.1097 paper title is "Non-Gaussianity in a matter bounce" by **Yi-Fu Cai** and Robert Brandenberger (published as Phys. Rev. D 90, 023534), NOT "Yi-Fu Li." The cite-key `LiBrandenberger:2014` and author `Li, Yi-Fu` look like a `Cai → Li` typo or copy-paste error.

There is no Yi-Fu Li in the matter-bounce literature. Yi-Fu Cai is the established author of multiple matter-bounce non-Gaussianity papers (Cai et al. 2009, 0903.0631; Cai 2014; etc.).

**Suggested fix.** Verify the arXiv:1405.1097 author list. If confirmed Cai (not Li), rename:
- Cite key: `LiBrandenberger:2014` → `CaiBrandenberger:2014`
- Author field: `Li, Yi-Fu` → `Cai, Yi-Fu`
- All inline `\cite{LiBrandenberger:2014}` invocations updated.

This is the kind of typo that survives ten rounds of internal review because the cite key is rarely visible — but it's the first thing a referee will flag at PRD submission.

#### O2 — MAJOR — `Heinrich:2023` cite-key vs JCAP 2024 publication year

**Location:** P2 lines 29, 48, 152, 154, 198, 263, 268, 299, 331, 367, 392, 471 (12+ inline citations); `focused_paper_refs.bib` lines 47-58.

**Bib entry:**
```
@article{Heinrich:2023,
  ...
  journal = {JCAP},
  volume = {2024},
  number = {04},
  pages = {074},
  year = {2024},
  eprint = {2311.13082},
}
```

**Issue.** The cite key encodes the preprint year (2023, when arXiv:2311.13082 was first posted), but the bibitem `year` field is 2024 (JCAP publication date) and the published JCAP volume is "2024 04 074." Inline text in P2 repeatedly reads:

- Line 29: "Heinrich \etal\ 2023~\cite{Heinrich:2023}, Fig.~6"
- Line 154: "Heinrich et al.\ \texttt{$\sigma(\fnl) = 0.7$}"
- Line 331: "Heinrich \textit{et~al.}\ 2023"
- Line 471: "(Heinrich \textit{et~al.}~\cite{Heinrich:2023}) with $\sigma(\fnl)=0.7$"

This is internally inconsistent: the bibliography rendering will display "Heinrich et al. 2024 (JCAP 2024 04 074)" but the inline text says "Heinrich et al. 2023." A copy-editor or a referee resolving the citation will see the mismatch immediately.

This pattern repeats in **P1A line 763** (text reads "Heinrich \etal~2023~\cite{Heinrich:2023}") and **P3 line 71** (text reads "Heinrich \etal~\cite{Heinrich2023}" with `\bibitem{Heinrich2023}` whose year-field is 2024).

**Suggested fix.** Two options:
1. (Cleaner) Re-key everywhere as `Heinrich:2024`, update inline text to "Heinrich \etal\ 2024."
2. (Minimal) Keep cite-keys but update inline text to "Heinrich \etal\ 2024" or "Heinrich \etal\ (2023, JCAP 2024)" so the rendered citation year matches.

Convention-wise, most journals use the published-year-of-record. The bibitem year field is already 2024; the inline text should match.

#### O3 — MAJOR — Eskilt2022 cite for the joint Planck+ACT β=0.342° value

**Location:** P2 line 377; `focused_paper_refs.bib` `Eskilt2022` entry lines 182-191

**Quote (P2 line 377):**
> "the $3.6\sigma$ Eskilt \etal~\cite{Eskilt2022} joint Planck analysis ... the bounce prediction $\beta = 0.27^\circ$ is consistent with the published Eskilt \etal\ 2022 joint Planck+ACT measurement $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$ at $0.77\sigma$"

**Issue.** The text says "joint Planck+ACT measurement." The Eskilt2022 entry in P2's bib resolves to:
- `eprint = {2205.13962}` — Eskilt & Komatsu 2022 PRD, "Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data."

This is the **WMAP+Planck** joint analysis, not the **Planck+ACT** joint analysis. The Planck+ACT joint analysis with β=0.342°±0.094° is in the Cosmoglobe / Eskilt+ 2023 A&A paper (arXiv:2305.02268; A&A 679, A144). P1A's bib has this as `Eskilt2022b` and uses it correctly at line 1141.

P2 has no Cosmoglobe / 2305.02268 entry. The text claim "joint Planck+ACT" is unsupported by the cited reference (which is joint Planck+WMAP).

Note: arXiv:2205.13962 does report β ≈ 0.342° ± 0.094° as one of its joint-analysis values, so the *number* is consistent — but the dataset attribution ("Planck+ACT" vs "Planck+WMAP") is wrong in the inline text.

**Suggested fix.** Add a Cosmoglobe entry to `focused_paper_refs.bib`:
```
@article{Eskilt2023cosmoglobe,
  author = {Eskilt, J. R. and others},
  collaboration = {Cosmoglobe},
  title = {Joint Planck and ACT measurement of cosmic birefringence},
  journal = {Astron. Astrophys.},
  volume = {679},
  pages = {A144},
  year = {2023},
  eprint = {2305.02268},
}
```

Then update line 377 to cite `Eskilt2023cosmoglobe` for the "joint Planck+ACT" claim. Or change "joint Planck+ACT" → "joint Planck+WMAP" if the intent was really to cite Eskilt2022.

#### O7 — MAJOR — `Cai:2026echoes` arXiv-ID `2601.00000` is a placeholder

**Location:** `focused_paper_refs.bib` line 292-298

**Bib entry:**
```
@article{Cai:2026echoes,
  author = {Cai, Yi-Fu and others},
  title = {Echoes of bouncing cosmologies},
  journal = {JSTAT},
  year = {2026},
  eprint = {2601.00000},
  archiveprefix = {arXiv}
}
```

**Issue.** The arXiv-ID `2601.00000` is not a real arXiv submission — arXiv numbering for January 2026 starts at `2601.00001`. This is a placeholder that survived from an earlier draft.

P1A's `arxiv/references.bib` has the real entry: `Cai:2026echoes` with `eprint = "2603.13924"` (March 2026 arXiv). Cross-paper inconsistency between P1A and P2.

**Suggested fix.** Update P2's `focused_paper_refs.bib` `Cai:2026echoes` entry to match P1A:
- `eprint = {2603.13924}`
- Add real journal/volume/pages from the published version, or remove the journal field.
- Verify both papers cite the same paper; if Cai 2026 is cited in two different ways, harmonize.

#### O11 — MINOR — `Wands:2010` paired with `Cai:2009fn` for matter-bounce $f_{\rm NL}$

**Location:** P2 line 42

**Quote:**
> "$\fnl = -35/8 = -4.375$~\cite{Cai:2009fn,Wands:2010}"

**Issue.** Wands 2010 (arXiv:1004.0818, "Local non-Gaussianity from inflation") is a **review of local-template $f_{\rm NL}$ from inflation**, not the matter-bounce derivation. The matter-bounce $f_{\rm NL}=-35/8$ result is from Cai, Xue, Brandenberger, Zhang 2009 (Cai:2009fn). Citing Wands:2010 alongside is rhetorically loose: a reader will assume Wands 2010 also derives the matter-bounce value, but it doesn't.

**Suggested fix.** Either:
- Use only `\cite{Cai:2009fn}` for the matter-bounce $f_{\rm NL}$ result.
- Or split: `\cite{Cai:2009fn}` for the matter-bounce derivation, `\cite{Wands:2010}` for the local-template $f_{\rm NL}$ definition convention. Make the role of each citation explicit in adjacent prose.

---

### P3 v3.1.35 — `paper3_draft.tex` (self-contained `\bibitem` block)

#### O5 — MAJOR — `\bibitem{Cai2009}` JCAP volume "0905" is INSPIRE month-code, not APS volume

**Location:** P3 line 1043-1046

**bibitem text:**
> Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, "Non-Gaussianity in a matter bounce," J. Cosmol. Astropart. Phys. **0905**, 011 (2009).

**Issue.** "0905" is the INSPIRE-HEP / SPIRES volume-month encoding (year + month, May 2009). It is not a JCAP-style volume number. JCAP citations follow either:
- Modern: "J. Cosmol. Astropart. Phys. **2009**, 011 (2009)" or "JCAP **05** (2009) 011"
- IOP: "J. Cosmol. Astropart. Phys. **2009 (5)** 011"

A revtex4-2 referee who tries to resolve "JCAP 0905, 011" against the JCAP database will not find it. Same issue in `arxiv/references.bib` `Cai:2009fn` `volume = {0905}` (line 579).

**Suggested fix.** Update both:
- P3 line 1046: "JCAP **05** (2009) 011" or "J. Cosmol. Astropart. Phys. **2009**, 011"
- references.bib line 579: `volume = {2009}, number = {05}, pages = {011}`

Same issue elsewhere in the bib (e.g., `Wands:2010` formatting in `focused_paper_refs.bib` line 81 has the analog problem with `volume = {1303}` for WilsonEwing 2013 — INSPIRE-style "1303" instead of `volume = {2013}, number = {03}`). Audit all JCAP entries.

#### O6 — MAJOR — `\bibitem{ACT_DR6}` first author cross-paper inconsistency

**Location:** P3 line 1018-1021; `arxiv/references.bib` `ACT2024` line 213

**P3 bibitem:**
> M. S. Madhavacheril \etal\ (ACT Collaboration), "The Atacama Cosmology Telescope: DR6 and DR6 Lensing," Astrophys. J. **962**, 113 (2024).

**P1A bib `ACT2024`:**
> author = {{ACT Collaboration} and Qu, Frank J. and others},
> title = {The {Atacama Cosmology Telescope}: {DR6} gravitational lensing map and cosmological parameters},
> journal = {The Astrophysical Journal}, volume = {962}, pages = {112}, year = {2024},

**Issue.** P1A and P3 are citing the ACT-DR6 lensing paper but with **different first authors** (Qu vs. Madhavacheril) and **different page numbers** (112 vs. 113). The ACT-DR6 collaboration released TWO companion papers in early 2024:
- Qu et al. 2024, ApJ 962, 112 (DR6 gravitational lensing map and cosmological parameters; arXiv:2304.05203)
- Madhavacheril et al. 2024, ApJ 962, 113 (DR6 lensing component-separated CMB maps; arXiv:2304.05202)

P3's bibitem title "DR6 and DR6 Lensing" is a non-existent published title — neither Qu 2024 nor Madhavacheril 2024 carries this exact title. P3 looks like a confabulated combination of the two.

**Suggested fix.** Pick one ACT-DR6 reference and use the published title:
- If P3 wants the lensing-map / cosmological-parameters paper: cite Qu et al. 2024, ApJ 962, 112 (arXiv:2304.05203). Match P1A.
- If P3 wants the component-separated lensing maps paper: cite Madhavacheril et al. 2024, ApJ 962, 113 (arXiv:2304.05202). Add to P1A bib if needed.

Either way, P3 and P1A should cite the same paper for "ACT DR6" with the same first author and page number.

#### O9 — MINOR — `\bibitem{Liang2023}` journal disagreement with master bib

**Location:** P3 line 1028-1031 vs `arxiv/references.bib` line 311-321

**P3 inline bibitem:**
> Z. Liang \etal, "Searching for Anomalies in the DESI Early Data Release Spectra," Astrophys. J. Lett. **961**, L5 (2023).

**arxiv/references.bib entry:**
```
@article{Liang2023,
  author = {Liang, Yang and others},
  title = {An anomaly detection pipeline for the DESI EDR},
  journal = {MNRAS},
  volume = {525},
  pages = {1078},
  year = {2023},
  eprint = {2302.05050},
}
```

**Issue.** Two different journals (ApJL vs MNRAS), two different titles, two different volumes. Same arXiv-ID 2302.05050 — so it's the same paper, but the inline-paper bibitem for P3 disagrees with the master `references.bib` entry. If P3 ever switches to `\bibliography{../arxiv/references.bib}`, the rendered citation will change unexpectedly.

**Suggested fix.** Reconcile against the published version of arXiv:2302.05050. Update both bibs to match the canonical published reference (verify ApJL 961 L5 vs MNRAS 525 1078 — only one is correct).

#### O12 — MINOR — `\bibitem{Heinrich2023}` JCAP volume formatting

**Location:** P3 line 1107-1110

**bibitem text:**
> C. Heinrich, O. Doré, and E. Krause, "Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum," JCAP **2024**, 074 (2024), arXiv:2311.13082.

**Issue.** When JCAP volume = year, the issue number is needed to resolve the citation. Should be "JCAP **04** (2024) 074" or "JCAP **2024**, 04, 074."

**Suggested fix.** Add the issue number: "JCAP **2024**, 04, 074 (2024)."

---

### P4 v1.0.44 — `chirality_catalog_paper.tex` (self-contained `\bibitem` block)

#### O10 — MINOR — `\bibitem{Holst:1995pc}` arXiv-ID year-bracket convention

**Location:** P4 line 2467-2470

**bibitem text:**
> S. Holst, Phys. Rev. D **53**, 5966 (1996) [arXiv:gr-qc/9511026 (1995)].

**Issue.** revtex4-2 PRD-style and MNRAS-style both prefer either:
- "[arXiv:gr-qc/9511026]" (no year inside brackets), OR
- "(1996) [arXiv:gr-qc/9511026]" (year already given before brackets).

The "[arXiv:gr-qc/9511026 (1995)]" form duplicates the year in two places (once as 1996 publication, once as 1995 preprint) and reads as if the paper has two publication years. Editorially noisy.

**Suggested fix.** Drop the "(1995)" inside the bracket: `[arXiv:gr-qc/9511026]`.

P4 has only this one self-contained-bib hygiene issue I caught at retrieval-grounded depth. Other P4 citations (Shamir, Walmsley, Jia, Astropy, etc.) resolve cleanly.

---

## What this review did NOT cover

This is the citation-chain layer only. I deliberately did not re-check:

- Numerical claims internal to a single paper (those are CCAI / theorist territory).
- MCMC convergence diagnostics, Fisher-matrix derivations, GR analytics.
- Cross-paper number harmonization (the user's CLAUDE.md tracks those).
- LaTeX compilation correctness (revtex4-2 mechanics, label/ref consistency).

Future cross-vendor rounds should hit different bias profiles (e.g., GPT for "find the missing edge case in the derivation," Gemini for "audit the assumption tree," Grok for "is the headline claim actually defensible at PRL/MNRAS gate").

---

**Save:** `project-context/peer-reviews/2026-05-10_0300pt_OOOOO_CROSS-VENDOR_Perplexity.md`
**Generated by:** Wave 14-OOOOO Perplexity sim (citation-chain bias).
**Next:** Wave 14-PPPPP — fix-pass against the 8 BLOCKER+MAJOR items above. Re-run a cross-vendor round on a different bias axis after.
