# Wave 14-RRRRR — REPEAT CROSS-VENDOR Perplexity (Citation Chain + arXiv-ID Consistency)

**Reviewer persona:** Perplexity (web-retrieval-grounded fact-checking). Bias profile: arXiv-ID resolution, year-key vs published-year audit, journal-volume-page sanity, cite-key resolution, bibliography integrity.

**Reviewing (post-RRRRR-prep, commit b2fb1537):**
1. P1A v1A.0.19 — `arxiv/paper1a_ech_nogo.tex` + `arxiv/references.bib`
2. P2 v1.7.25 — `research/focused_paper_source_integration/02_full_draft.tex` + `focused_paper_refs.bib`
3. P3 v3.1.36 — `pipelines/p3_anomaly_engine/paper3_draft.tex` (self-contained `\bibitem` block)
4. P4 v1.0.46 — `pipelines/p2_chirality/chirality_catalog_paper.tex` (self-contained `\bibitem` block)

**Mandate:** verify the eight OOOOO closures (O1-O8) held under PPPPP, confirm M12 (Munchmeyer in P2) holds, audit the six P2 journal-stub additions, and surface any new bib-integrity defects.

---

## Closure-verification table (OOOOO findings)

| ID | Severity | Closure target | RRRRR verdict |
|----|----------|----------------|---------------|
| O1 | MAJOR  | `LiBrandenberger:2014` → `CaiBrandenberger:2014` (P2) | **HELD CLEAN** — bib `focused_paper_refs.bib:163-174` reads `Cai, Yi-Fu and Brandenberger, Robert`, journal `Physical Review D`, vol 90, pages 023534, eprint 1405.1097, DOI populated; six inline `\cite{CaiBrandenberger:2014}` invocations in `02_full_draft.tex` resolve correctly; `02_full_draft.bbl` line cited (`{Brandenberger}(2014)}]{CaiBrandenberger:2014}`). |
| O2 | MAJOR  | `Heinrich:2023` bibkey vs 2024 inline year (P1A/P2/P3) | **PARTIAL — RESIDUAL IN P3.** P1A line 772 reads "Heinrich \etal~2024~\cite{Heinrich:2023}" (clean). P2 lines 29 ("Heinrich et al.\ 2024"), 198, 333, 369 (e.g. "Heinrich \etal~2024~\cite{Heinrich:2023}"), 473 all read 2024. **P3 lines 71 (twice), 550 (twice), and 633 still carry the prose anchor "Heinrich+2023" (e.g. line 71: "anchored to the Heinrich+2023 $\sigfnl \approx 0.7$ bispectrum-only forecast"; line 550 closing: "The headline forecast remains the Heinrich+2023 anchor $\sigfnl \approx 0.7$").** The bibitem at P3 line 1107-1110 correctly reads JCAP **2024**, 074 (2024). The defect is that the P3 prose still markets the headline as a "Heinrich+2023" anchor while the bib says 2024. See R1 below. |
| O3 | MAJOR  | Eskilt2022b bibitem added to P2 (Cosmoglobe arXiv:2305.02268) | **HELD STRUCTURALLY, BUT P2 BIB FIELDS ARE WRONG.** Bibitem present at `focused_paper_refs.bib:209-216` and resolves in `02_full_draft.bbl`. P2 §VII.E (line 379) cites it correctly for the 0.342°±0.094° figure. **However**, P2's bib lists `journal = {Astrophys. J.}` with NO volume/page/DOI, while P1A's `references.bib:Eskilt2022b` correctly resolves the same DOI to `Astron. Astrophys. 679, A144 (2023)`. Cross-paper inconsistency on the same key + wrong journal in P2. See R2 below. |
| O4 | MAJOR  | P1A 3-source bundle for β=0.342°±0.094° tightened to disambiguate Minami / Eskilt / Diego-Palazuelos | **PARTIAL — STILL LOOSE.** P1A line 666 was changed from `\cite{Minami2020,Eskilt2022,DiegoPalazuelos2025}` → `\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}`. The Eskilt swap is correct, but the OOOOO suggested fix asked PPPPP to "move the Minami / Diego-Palazuelos refs to a separate sentence" because Minami2020 reports β=0.35°±0.14° (different) and DiegoPalazuelos2025 reports β=0.20°±0.08° (ACT-only). The 3-source bundle still implies all three quote 0.342°±0.094°. Lines 1170 and 812 use the citation cleanly; the residual is at line 666 only. See R3 below (downgraded to MINOR — single-line cosmetic, not a number-correctness defect). |
| O5 | MAJOR  | P3 ACT_DR6 bibitem retitled Madhavacheril → Qu+ ApJ 962 112 | **HELD CLEAN** — P3 line 1018-1021 reads "F.\ J.\ Qu \etal\ (ACT Collaboration), 'The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth,' Astrophys.\ J.\ \textbf{962}, 112 (2024)." Matches `arxiv/references.bib:213` (`{ACT Collaboration} and Qu, Frank J.`). Cross-paper key consistent. |
| O6 | MAJOR  | P2 Cai:2026echoes eprint 2601.00000 → 2603.13924 | **HELD CLEAN** — `focused_paper_refs.bib:320-325` reads `eprint = {2603.13924}`. Matches `arxiv/references.bib:740,743` (`eprint = "2603.13924"`). |
| O7 | MAJOR  | P3 Cai bibkey Cai2009 → Cai:2009fn | **HELD CLEAN** — P3 line 1043 has `\bibitem{Cai:2009fn}`; inline cites all use `Cai:2009fn`. Matches the master `arxiv/references.bib:574 @article{Cai:2009fn,...}`. |
| O8 | BLOCKER | P1A Yin2026 arXiv:2601.13624 | **HELD STRUCTURALLY** — `references.bib:413-421` retains the bibitem with `eprint = {2601.13624}`, year 2026, all four authors (Yin, Du, Li, Zhang). Per OOOOO closure note this was verified via WebFetch as a real Jan-2026 arXiv submission. The journal field `arXiv preprint` is colloquial; preferred is `arXiv e-prints` for revtex bibtex consistency. Not a regression. |

## Verification of M12 (cross-vendor consolidated)

| Mxx | Closure target | RRRRR verdict |
|-----|----------------|---------------|
| M12 | Munchmeyer:2019 added to P2 bib + cited at σ(f_NL)~0.7 anchor | **HELD CLEAN** — `focused_paper_refs.bib:69-79` has full entry (Phys. Rev. D 100, 083508, 2019, eprint 1810.13424). Inline P2 line 152 cites `\cite{Munchmeyer:2019}` at the SPHEREx multi-tracer anchor; line 369 uses it again for the Fisher forecast lineage. P2 bbl resolves the key cleanly. |

## Verification of P2 journal-field stubs (6 entries)

All six new `journal = {arXiv e-prints}` stubs render correctly in `02_full_draft.bbl`:

| Bibkey | arXiv ID | Stub status |
|--------|----------|-------------|
| Dore:2014 | 1412.4872 | resolves clean |
| Schlegel:2022 | 2209.04322 | resolves clean |
| Barreira:2022 | 2205.05673 | resolves clean |
| Jolicoeur:2025 | 2511.09466 | resolves clean |
| DESI:2016fnl | 1611.00036 | resolves clean (note field preserved) |
| CMBS4:2019 | 1907.04473 | resolves clean (note field preserved) |

No rendering breakage. The stub strategy was implemented correctly.

---

## NEW findings (RRRRR additions, post-OOOOO closure)

| ID | Paper | Severity | Title |
|----|-------|----------|-------|
| R1 | P3 | **MAJOR** | "Heinrich+2023 anchor" prose token persists in P3 while bibitem-year is 2024 (residual O2) |
| R2 | P2 | **MAJOR** | Eskilt2022b bib in `focused_paper_refs.bib` lists wrong journal (`Astrophys. J.`) with no volume/page; P1A `references.bib` correctly resolves to `Astron. Astrophys. 679, A144 (2023)`. Cross-paper inconsistency on same key. |
| R3 | P1A | MINOR | 3-source bundle `\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}` at line 666 still implies all three report β=0.342°±0.094°; only Eskilt2022b does. (OOOOO O4 partial closure.) |
| R4 | P1A | NIT | Yin2026 bib field `journal = {arXiv preprint}` should be `arXiv e-prints` for revtex/INSPIRE consistency (matches P2 stub style). |

### R1 — MAJOR — P3 prose anchor "Heinrich+2023" while bib says 2024

**Locations:**
- `pipelines/p3_anomaly_engine/paper3_draft.tex` line 71: "anchored to the Heinrich+2023 $\sigfnl \approx 0.7$ bispectrum-only forecast as the headline external benchmark"
- line 550: "The headline forecast remains the Heinrich+2023 anchor $\sigfnl \approx 0.7$ (bispectrum-only)"

**Issue.** The OOOOO closure mandate was "replace_all 'Heinrich et al. 2023' → 'Heinrich et al. 2024' across P1A + P2 + P3 inline text". P1A and P2 were edited cleanly. P3 was edited at the `\etal\cite{}` patterns and the `\bibitem` (which now reads `JCAP \textbf{2024}, 074 (2024)`), but the **two prose anchor tokens "Heinrich+2023"** at lines 71 and 550 were missed. A reader of the bibitem will see Heinrich et al. 2024; a reader of the introduction (line 71) and the §IV closing (line 550) will see "Heinrich+2023 anchor." Same paper, two different years for the same reference — exactly the year-vs-cite-key drift OOOOO O2 was meant to close.

**Suggested fix.** Two-token edit:
- L71: `Heinrich+2023 $\sigfnl \approx 0.7$` → `Heinrich+2024 $\sigfnl \approx 0.7$`
- L550: `the Heinrich+2023 anchor $\sigfnl \approx 0.7$` → `the Heinrich+2024 anchor $\sigfnl \approx 0.7$`

### R2 — MAJOR — P2 Eskilt2022b bib entry has wrong journal/missing volume

**Location:** `research/focused_paper_source_integration/focused_paper_refs.bib:209-216`

**Current entry:**
```
@article{Eskilt2022b,
  author = {Eskilt, Johannes R. and others},
  title = {Cosmoglobe DR1: Improved cosmic microwave background polarization analysis with full posterior sampling},
  journal = {Astrophys. J.},
  year = {2023},
  eprint = {2305.02268},
  archiveprefix = {arXiv}
}
```

**Reference (P1A `arxiv/references.bib`, lines for the same key):**
```
@article{Eskilt2022b,
    author = "Eskilt, J. R. and others",
    collaboration = "{Cosmoglobe}",
    title = "{Joint Planck and ACT measurement of cosmic birefringence: $\beta = 0.342^\circ \pm 0.094^\circ$}",
    journal = "Astron. Astrophys.",
    volume = "679",
    pages = "A144",
    year = "2023",
    eprint = "2305.02268",
    ...
}
```

**Issue.** P2's PPPPP-added Eskilt2022b entry:
1. **Wrong journal** — lists `Astrophys. J.` but the Cosmoglobe DR1 / Joint Planck-ACT birefringence paper is published in `Astron. Astrophys. 679, A144 (2023)`. Same arXiv ID 2305.02268 confirms.
2. **Missing volume + pages** — no `volume`, no `pages`, no DOI. The .bbl renders an incomplete reference (just journal name + year + arXiv ID).
3. **Title is wrong** — the title given is the Cosmoglobe-DR1 polarization-analysis title (Watts et al. companion paper), but the actual Eskilt+ first-author paper at 2305.02268 is "Joint Planck and ACT measurement of cosmic birefringence" (per P1A's correct entry).

**Cross-paper inconsistency** with P1A's own correct rendering of the same bibkey. Either P2 was hand-typed without copying P1A's master entry, or someone confused the Watts companion paper with the Eskilt first-author paper. The arXiv ID is correct; the bib metadata is wrong.

**Suggested fix.** Replace P2's `Eskilt2022b` entry with P1A's, preserving the bibkey:
```
@article{Eskilt2022b,
  author = {Eskilt, Johannes R. and others},
  collaboration = {Cosmoglobe},
  title = {Joint {Planck} and {ACT} measurement of cosmic birefringence: $\beta = 0.342^\circ \pm 0.094^\circ$},
  journal = {Astron. Astrophys.},
  volume = {679},
  pages = {A144},
  year = {2023},
  eprint = {2305.02268},
  archiveprefix = {arXiv}
}
```

This is a load-bearing bib entry — it's the source of the headline 0.342°±0.094° figure cited in P2 §VII.E. A copy-editor will flag it.

### R3 — MINOR — P1A 3-source bundle for β=0.342°±0.094° still loose

**Location:** `arxiv/paper1a_ech_nogo.tex` line 666: `\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}`

**Issue.** PPPPP swapped Eskilt2022 → Eskilt2022b (correct), but kept the 3-source bundle. Of the three:
- **Minami2020** (PRL 125, 221301): β = 0.35° ± 0.14° (Planck-2018 only) — DIFFERENT central value, different errorbar.
- **Eskilt2022b** (A&A 679, A144): β = 0.342° ± 0.094° — THE SOURCE OF THE QUOTED FIGURE.
- **DiegoPalazuelos2025**: β ≈ 0.20° ± 0.08° (ACT-DR6-only) — DIFFERENT.

A reader of "$\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$~\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}" concludes all three sources report 0.342°±0.094°. They don't. The OOOOO O4 mandate was to move Minami2020 and DiegoPalazuelos2025 to a separate sentence noting "consistent with the earlier Planck-2018 / ACT-DR6 measurements"; only Eskilt2022b should anchor the exact number.

**Downgrade rationale.** Calling this MINOR rather than MAJOR because the cited value is correct (the lead source supports it), and the surrounding context elsewhere in P1A (lines 812, 1170) already disambiguates Minami and Diego-Palazuelos as separate measurements. The line-666 bundle is rhetorically loose but not number-wrong.

**Suggested fix.** Replace `\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}` at line 666 with `\cite{Eskilt2022b}` (sole source of the quoted value). Optionally add a separate sentence: "consistent with earlier independent Planck-2018 (Minami \& Komatsu~\cite{Minami2020}) and ACT-DR6 (Diego-Palazuelos \& Komatsu~\cite{DiegoPalazuelos2025}) measurements at lower individual significance."

### R4 — NIT — Yin2026 journal-field stylistic inconsistency

**Location:** `arxiv/references.bib:416`: `journal = {arXiv preprint}`

**Issue.** revtex4-2 / INSPIRE-style preprint entries use `journal = {arXiv e-prints}` (matches the 6 P2 stub additions at PPPPP). `arXiv preprint` is informal and inconsistent with house style.

**Fix.** One-line change: `arXiv preprint` → `arXiv e-prints`. Cosmetic only; bbl rendering already works.

---

## Summary table

| ID | Paper | Severity | Title | Where |
|----|-------|----------|-------|-------|
| R1 | P3 | **MAJOR** | Prose anchor "Heinrich+2023" persists at lines 71 + 550 while bib reads 2024 (residual O2) | `paper3_draft.tex` |
| R2 | P2 | **MAJOR** | Eskilt2022b bib entry has wrong journal (ApJ vs A&A) + missing volume/pages/DOI; cross-paper inconsistent with P1A | `focused_paper_refs.bib:209-216` |
| R3 | P1A | MINOR | 3-source bundle `Minami2020,Eskilt2022b,DiegoPalazuelos2025` for 0.342°±0.094° still loose | `paper1a_ech_nogo.tex:666` |
| R4 | P1A | NIT | Yin2026 `journal = {arXiv preprint}` should be `arXiv e-prints` for house consistency | `references.bib:416` |

**Totals: 0 BLOCKER, 2 MAJOR, 1 MINOR, 1 NIT (= 4 findings).**

---

## Convergence judgement

**Citation-chain integrity has substantially improved since OOOOO**, but is not yet fully clean. Of the 8 OOOOO findings (O1-O8):
- 5 closed cleanly (O1, O5, O6, O7, O8)
- 1 partially closed with residual prose token (O2 → R1)
- 1 closed structurally but with new bib defect introduced (O3 → R2)
- 1 partially closed with looser cite bundle than mandated (O4 → R3)
- M12 (Munchmeyer) closed cleanly

The two new MAJORs (R1, R2) are both **verifiable from the on-disk .tex/.bib without WebFetch**. R1 is a missed find/replace target. R2 is a hand-typed bib entry that diverged from P1A's correct master. Both are five-line fixes.

**Comparison vs OOOOO:** OOOOO surfaced 8 findings (1B + 7M + 4m + 0n = 12 raw, 8 unique). RRRRR surfaces 4 findings (0B + 2M + 1m + 1n). That's a **−50% reduction** at the BLOCKER+MAJOR layer (1B+7M=8 → 0B+2M=2; **−75%**), with the residuals concentrated where PPPPP applied surgical edits but missed adjacent surfaces (R1 prose, R2 bib metadata).

**Verdict.** The exit gate "<3B+<5M cleanly without sub-agent regressions" is **MET at BLOCKER level (0/3) but partially met at MAJOR level (2/5)**. The 2 MAJORs are mechanical bib-integrity fixes (one prose replace_all, one bib entry copy-paste from P1A to P2), not scientific-correctness defects. A single fix-pass Wave 14-RRRRR-fix should close them; the post-fix R-round should achieve clean (<1M+0B) on this axis.

**Recommend Wave 14-SSSSS-prep:**
1. R1: P3 `replace_all` "Heinrich+2023" → "Heinrich+2024" at lines 71 + 550 (2 prose token edits).
2. R2: P2 replace `Eskilt2022b` bib entry with P1A's correct A&A 679, A144 form.
3. R3: P1A line 666 trim 3-source bundle to `\cite{Eskilt2022b}`, optionally add disambiguation sentence.
4. R4: P1A `references.bib:416` `arXiv preprint` → `arXiv e-prints`.

Total: ~10-line edit + recompile P2 + recompile P1A. No P3 recompile needed (self-contained `\bibitem` block + 2 prose tokens; bbl unchanged).

After SSSSS-prep + a confirming RRRRR-2 cross-vendor pass, the citation-chain axis should close. Combined with the already-clean R51 CCAI re-confirmation, this would meet both "clean CCAI round AND clean cross-vendor round" exit criteria per `feedback_99_pct_readiness_cap.md`, and the 95% cap can lift to 99%.
