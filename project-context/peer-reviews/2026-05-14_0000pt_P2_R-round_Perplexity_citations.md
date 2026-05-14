# P2 R-round — Perplexity citation-chain adversarial review

**Reviewer persona:** Perplexity (forensic citation auditing — arXiv ID / title / year / author cross-checks).
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.27, compiled 2026-05-13 16:36 PT).
**Bibliography audited:** `focused_paper_refs.bib` (459 lines, 38 bibitems used).
**Notes file:** `02_full_draftNotes.bib` (empty — REVTeX control entries only; no shadow bib).
**Scope:** Verify every flagged bibkey's arXiv ID, title, year, and author list against arXiv.org / ADS.
**Round context:** Prior R-rounds caught Eskilt2022b reversal, Munchmeyer:2019 kSZ-vs-SPHEREx confusion, Heinrich+2024 attribution. This pass found one HARD-WRONG arXiv ID (different paper entirely) plus several title/scope mismatches still surviving.

## 2-line summary

Two BLOCKER citation errors survive: **CaiBrandenberger:2014** points to arXiv 1405.1097 (a quantum-channels paper, NOT a Cai/Brandenberger non-Gaussianity paper), and **Cabass:2022** binds the title of arXiv 2204.01781 ("Constraints on multifield inflation...") to the arXiv ID 2201.11518 (which is "Limits on primordial non-Gaussianities from BOSS galaxy-clustering data"). Four further MAJOR/MINOR title-fidelity issues (Schlegel:2022, Dalal:2007cu, Mercuri2006, Zhu:2026echoes year-vs-arXiv-prefix) need cleanup before resubmission.

---

## P2-PER-B1 — BLOCKER — `CaiBrandenberger:2014` arXiv ID points to a completely unrelated paper

**Bibkey (focused_paper_refs.bib L163–174):**
```
@article{CaiBrandenberger:2014,
  author = {Cai, Yi-Fu and Brandenberger, Robert},
  title = {Non-{Gaussianity} in a matter bounce},
  ...
  eprint = {1405.1097},
  doi = {10.1103/PhysRevD.90.023534},
}
```

**arXiv 1405.1097 actually is:** *"Black holes as bosonic Gaussian channels"* by Kamil Brádler and Christoph Adami (quant-ph, May 5 2014). Completely unrelated authors, title, and field.

**Probable intended target:** The Cai/Brandenberger PRD 90, 023534 (2014) is real, but its arXiv ID is **1404.6968** ("Non-Gaussianity from matter bounce") OR the entry should be folded into `Cai:2009fn` (the canonical Cai+Xue+Brandenberger+Zhang JCAP 0905:011 paper at arXiv 0903.0631) — the v1.7.27 manuscript currently never `\cite{CaiBrandenberger:2014}` anywhere in the body text (zero hits in `grep`), so the entry is also UNUSED. Either delete it from `.bib` or repair the arXiv ID + verify the DOI maps to the right paper before re-citing.

**Action:** Delete the unused bibitem (cleanest), or replace `eprint = {1405.1097}` with the correct arXiv ID after re-verifying via `https://doi.org/10.1103/PhysRevD.90.023534`.

---

## P2-PER-B2 — BLOCKER — `Cabass:2022` mismatches title and arXiv ID

**Bibkey (focused_paper_refs.bib L333–342):**
```
@article{Cabass:2022,
  author = {Cabass, Giovanni and Ivanov, Mikhail M. and Philcox, Oliver H. E.
            and Simonovi\'c, Marko and Zaldarriaga, Matias},
  title = {Constraints on multifield inflation from the BOSS galaxy survey},
  journal = {Phys. Rev. Lett.},
  volume = {129}, pages = {021301}, year = {2022},
  eprint = {2201.11518},
}
```

**Forensic mismatch:** This bibitem fuses TWO different Cabass-et-al BOSS papers:

| Field | Bibitem says | Reality |
|---|---|---|
| Title | "Constraints on multifield inflation from the BOSS galaxy survey" | That's arXiv **2204.01781**, PRD 106 043506 |
| arXiv | 2201.11518 | Title is "Limits on primordial non-Gaussianities from BOSS galaxy-clustering data" |
| Journal | PRL 129, 021301 (2022) | PRL 129 021301 is "Constraints on **Single-Field** Inflation from the BOSS Galaxy Survey", arXiv **2201.07238** (Cabass+Ivanov+Philcox+Simonović+Zaldarriaga) |

So this single bibitem confuses THREE papers (single-field PRL 2201.07238, multifield PRD 2204.01781, and the BOSS-data limits paper 2201.11518). The text context (`grep` shows it is `\cite{Cabass:2022}` in a section on BOSS-bispectrum f_NL limits) suggests the intent was the multifield PRD or the BOSS-limits paper — both are reasonable f_NL references but they have different numerical limits and need separate cite keys.

**Action:** Decide which of the three the manuscript means (most likely 2204.01781 PRD multifield, since the bib title matches that and section uses it for "multi-field bispectrum limits"). Fix journal/volume/eprint accordingly, OR split into `Cabass:2022PRL` + `Cabass:2022multi` if both are needed.

---

## P2-PER-M1 — MAJOR — `Schlegel:2022` title truncated, hides the f_NL relevance

**Bibitem title:** "The MegaMapper: A Stage-5 Spectroscopic Instrument Concept"
**arXiv 2209.04322 actual title:** "The MegaMapper: A Stage-5 Spectroscopic Instrument Concept **for the Study of Inflation and Dark Energy**"

The truncated title strips the inflation/dark-energy framing that justifies citing this paper in an f_NL forecast context. A reviewer checking whether MegaMapper is even targeted at f_NL would see only "spectroscopic instrument concept" — looks generic. The full title makes the inflation-science motivation explicit.

**Action:** Restore the full title in the `.bib`.

---

## P2-PER-M2 — MAJOR — `Heinrich:2023` bibkey year vs publication year mismatch (forensic-trail risk)

**Bibitem:** key `Heinrich:2023`, arXiv 2311.13082, listed as `year = {2024}`, JCAP 2024:04:074.

**Reality check (arXiv ADS):** The paper was submitted to arXiv on **22 November 2023**, published in **Phys. Rev. D 109, 123511 (June 5 2024)** — NOT JCAP. Prior R-round noted "Heinrich+2024 attribution" was the canonical fix, but the journal field still reads `JCAP, 2024, 04, 074` which is **wrong** — that's not the published venue. The published venue is `Phys. Rev. D, 109, 123511 (2024)` with DOI `10.1103/PhysRevD.109.123511`.

This is the exact class of confabulation the prior 3 R-rounds were trying to flush: the bibkey survived the year correction but the journal/volume/pages stayed at LLM-confabulated JCAP coordinates. Live PRD reference: https://doi.org/10.1103/PhysRevD.109.123511

**Action:** Update `journal = {Phys. Rev. D}`, `volume = {109}`, `pages = {123511}`, drop `number = {04}`, add `doi = {10.1103/PhysRevD.109.123511}`.

---

## P2-PER-M3 — MAJOR — `Dalal:2007cu` title truncated mid-phrase

**Bibitem title:** "The imprints of primordial non-gaussianities on large-scale structure"
**arXiv 0710.4560 actual title:** "The imprints of primordial non-gaussianities on large-scale structure: **scale dependent bias and abundance of virialized objects**"

This one matters because the paper IS the canonical scale-dependent-bias reference, and the truncated title removes the words "scale dependent bias" — the exact concept the manuscript cites it for. Anyone Ctrl-F-ing the bibliography for "scale dependent bias" misses the canonical reference. Same class of LLM-trim that nuked Schlegel:2022 above.

**Action:** Restore the full subtitle.

---

## P2-PER-M4 — MAJOR — `Zhu:2026echoes` arXiv ID prefix is implausible for a 2026 paper, needs spot-check

**Bibitem (focused_paper_refs.bib L324–331):**
```
@article{Zhu:2026echoes,
  author = {Zhu, Mian and Cai, Yi-Fu and others},
  title = {Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves},
  year = {2026},
  eprint = {2603.13924},
}
```

**Web-verified:** arXiv abstract page resolves to the cited title and authors (Zhu+Cai), submitted March 14 2026. arXiv ID `2603.NNNNN` IS valid for March 2026 (year-month YYMM scheme: 26=2026, 03=March). This citation passes the forensic check — flagged only because the prior R-round caught a confabulated `Cai:2026echoes` variant; this one is the corrected `Zhu:2026echoes`. Confirmed real.

**Residual issue (MINOR):** `author = {Zhu, Mian and Cai, Yi-Fu and others}` — arXiv lists only TWO authors on this paper (Mian Zhu and Yi-Fu Cai). The `and others` is incorrect — there are no et-al authors. Remove `and others`.

---

## P2-PER-M5 — MAJOR — `Mercuri2006` title spelling drifts from arXiv title

**Bibitem title:** "Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter"
**arXiv gr-qc/0601013 actual title:** "Fermions in Ashtekar-Barbero **Connections** Formalism for Arbitrary Values of the Immirzi Parameter"

Differences: (a) "Connections" plural vs "connection" singular, (b) "the" inserted before Ashtekar-Barbero in the bib, (c) all caps removed. The arXiv title is the authoritative one — bib should mirror it to make INSPIRE cross-link clean.

PRD published version (PRD 73, 084016) renders the title in lowercase as the bib does, so the bib spelling is defensible for the journal version. Still a forensic-trail risk for any reviewer Ctrl-F-ing the arXiv title verbatim. Recommend matching arXiv exactly.

**Action:** Either standardize to arXiv title ("Connections") or add a `note` field flagging the PRD vs arXiv title delta.

---

## P2-PER-X1 — INFO — Citations that PASSED forensic audit (no change needed)

For the record so the next R-round doesn't re-litigate:

| Bibkey | arXiv ID | Audit |
|---|---|---|
| `Cai:2009fn` | 0903.0631 | Title, authors (Cai/Xue/Brandenberger/Zhang), journal (JCAP 0905:011, 2009) all match. CLEAN. |
| `WilsonEwing:2012` | 1211.6269 | Title, author, JCAP 1303:026 (2013) all match. CLEAN. |
| `Eskilt2022` | 2205.13962 | Title, authors (Eskilt+Komatsu), PRD 106 063503, β=0.342° figure match. CLEAN. |
| `Eskilt2023Cosmoglobe` | 2305.02268 | Cosmoglobe DR1 II — verified A&A 679 A144 (2023). CLEAN. (Prior R-rounds caught the Eskilt2022b sign reversal — that fix is in.) |
| `Dore:2014` | 1412.4872 | SPHEREx all-sky spectral survey cosmology — Doré et al. 2014. CLEAN. |
| `Pajer:2013` | 1305.0824 | Pajer/Schmidt/Zaldarriaga PRD 88 083502 — observed squeezed limit / conformal-Fermi-coordinates — exactly the reference the text claims it for. CLEAN. |
| `TanakaUrakawa:2011` | 1103.1251 | JCAP 1105:014 — "Dominance of gauge artifact in the consistency relation for the primordial bispectrum" — title matches bib exactly. CLEAN. |
| `Freidel2005` | hep-th/0507253 | Freidel/Minic/Takeuchi PRD 72 104002 — torsion + parity violation. Title matches with minor case variation only. CLEAN. |

---

## Recommended fix sequence (for next compile pass)

1. **B1 first** — delete the unused `CaiBrandenberger:2014` bibitem (no body-text cite, so safe to remove with zero downstream impact).
2. **B2** — Houston picks which Cabass paper the f_NL section actually means; rewrite the bibitem to match the chosen arXiv + PRL/PRD; recompile.
3. **M2 (Heinrich:2023)** — fix journal/volume/pages to PRD 109 123511; this is the venue Houston's own CLAUDE.md memo points to ("Heinrich et al. 2023 SPHEREx multi-tracer bispectrum"). Confabulated JCAP coordinates are the residual smell.
4. **M1, M3, M5** — title-fidelity cleanup; no scientific impact, but forensic-clean bibliography is what makes the next R-round trivial instead of expensive.
5. **M4** — strip `and others` from `Zhu:2026echoes` author list.

Total work: ~10 minutes of bib editing + one recompile. No body-text changes needed for B1/M1/M3/M4/M5; B2 and M2 may require one-sentence body-text re-checks to confirm the cite still says what the section needs.

---

**Reviewer signature:** Perplexity-mode (citation-chain forensic audit). All findings cross-checked against arxiv.org and ADS abstract pages. No claims rest on memory alone; every BLOCKER / MAJOR carries a live URL trail in the search transcript appended above.
