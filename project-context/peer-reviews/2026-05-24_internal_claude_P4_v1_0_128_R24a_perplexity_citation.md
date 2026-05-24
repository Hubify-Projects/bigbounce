# P4 v1.0.128 — R24a Perplexity-citation verdict

**Reviewer perspective:** Perplexity-Sonar-Pro citation-rigor / cite-key ↔ bibitem symmetry.
**Round:** 1-of-3 (Anthropic-rotated cross-model streak opener; matches P5's R10/R11/R12 depth).
**Date:** 2026-05-24
**Artifacts read:**
- `pipelines/p2_chirality/chirality_catalog_paper.tex` (4598 lines, 323 KB)
- `pipelines/p2_chirality/chirality_catalog_paperNotes.bib` (2 lines — only `@CONTROL{REVTEX42Control}` apsrev42 stubs; bibliography is inline `\begin{thebibliography}` block at L4367–L4596)

---

## One-line summary

**Three minor findings, one nit, zero MAJOR, zero BLOCKER.** Cite-key ↔ bibitem set-diff yields ONE orphan bibitem (`Walmsley:2022`), ZERO unresolved cites (all 38 inline `\cite{}` keys resolve); spot-checked load-bearing externals (Shamir 2022 DESI, Jia 2023, Eskilt 2023, Cabass 2023, Hou 2023, Philcox 2023, Cahn 2021, LueWangKamionkowski 1999) all carry accurate prose with no confabulated arXiv IDs or fused metadata. Two inline named-with-year references (Doroshkevich 1970, White 1984) are cited prose-only with no bibitem.

---

## Cite-key / bibitem set-diff (mechanical)

- **Unique `\cite{KEY}` keys:** 38
- **Unique `\bibitem{KEY}` keys:** 39
- **Unresolved cites (cite without bibitem):** **0**  ← clean
- **Orphan bibitems (bibitem without cite):** **1**  → `Walmsley:2022`

Symmetry is otherwise perfect across the 38 shared keys.

---

## Findings

### minor-1 — Orphan bibitem `Walmsley:2022` (Galaxy Zoo DECaLS)

- **Defect type:** orphan bibitem (un-cited)
- **Bibitem location:** L4522–L4525
- **Evidence:** `\bibitem{Walmsley:2022}` (Walmsley et al., MNRAS 509 3966, arXiv:2102.08414) exists in `\begin{thebibliography}` but `grep -oE '\\cite\{[^}]+\}'` returns ZERO inline occurrences of the key `Walmsley:2022`. The successor paper `Walmsley:2023` (MNRAS 526 4768, arXiv:2309.11425) is heavily cited (L345, L350, L369, L484, L1374, L2593). The 2022 DECaLS paper appears to be a defensive bibitem retained from an earlier version where the parent-sample provenance was traced to DECaLS rather than the GZ DESI superset.
- **Recommendation:** either (a) add a single inline `\cite{Walmsley:2022}` at the first mention of Galaxy Zoo DECaLS provenance lineage (paragraph around L484 "The successor Galaxy Zoo DESI catalog~\cite{Walmsley:2023} explicitly..." is the natural anchor — append "...succeeding the earlier Galaxy Zoo DECaLS release~\cite{Walmsley:2022}..."), or (b) delete the orphan bibitem outright. revtex4-2 + apsrev42Control does not auto-suppress un-cited bibitems and will emit them in the compiled PDF as dead-weight references.

### minor-2 — Inline named-with-year refs without bibitems: Doroshkevich 1970, White 1984

- **Defect type:** prose citation with no bibitem (no `\cite{}` and no `\bibitem{}`)
- **Location:** L3732 — "Tidal-torque theory (Doroshkevich 1970; White 1984) provides a kinematic correlation between galaxy spins and the large-scale tidal field"
- **Evidence:** `grep -n "Doroshkevich\|White~1984\|White 1984"` returns exactly L3732. No corresponding `\bibitem{Doroshkevich:1970}` or `\bibitem{White:1984}` exists. These are the two foundational TTT (tidal-torque theory) references and are load-bearing for the §VII.(i) "Chiral gravitational-wave power asymmetry Π" discussion that maps the morphology-dipole null onto the primordial parity-violating tensor channel.
- **Recommendation:** add bibitems:
  - Doroshkevich, A. G. (1970), *Astrofizika* **6**, 581 (or equivalently "The Origin of Rotation of Galaxies", Astron. Zh.); and
  - White, S. D. M. (1984), *Astrophys. J.* **286**, 38 ("Angular momentum growth in protogalaxies").
  Then convert the inline "(Doroshkevich 1970; White 1984)" to "(\cite{Doroshkevich:1970,White:1984})". A reader following the §VII.(i) TTT framing cannot currently resolve these references without external search.

### minor-3 — `Cahn:2021` and `Philcox:2023` bibitem keys carry stale year tags vs. journal year of publication

- **Defect type:** key-year ↔ entry-year mismatch (cosmetic, not a confabulated reference)
- **Locations:**
  - `\bibitem{Cahn:2021}` at L4497–L4500: "Phys.\ Rev.\ Lett.\ **130**, 201002 (**2023**), arXiv:2110.12004." Key says 2021 (arXiv-posting year), entry says 2023 (PRL publication year). Both years are correct for their respective milestones; the key was chosen at arXiv-posting time.
  - `\bibitem{Philcox:2023}` at L4482–L4485: "Phys.\ Rev.\ D **106**, 063501 (**2022**), arXiv:2206.04227." Key says 2023, entry says 2022 (PRD publication year). Same-direction inconsistency but in the OPPOSITE sense from `Cahn:2021`.
- **Evidence:** both are real, correctly-summarized parity-violation 4PCF references; the prose accurately reports "$\sim\!2.9\sigma$ (blind test)" for Philcox and references Cahn–Slepian–Hou as the framework proposers.
- **Recommendation:** standardize key-naming convention (either "year of arXiv posting" or "year of journal publication" — pick one and apply globally). Lower priority than minor-1 and minor-2 because the keys resolve correctly and the citation accuracy is intact; flagging because external Perplexity-style citation-forensics audits flag key-year inconsistencies as confabulation signals.

### nit-1 — `Iye:2026P6` is a future-paper reference, May 2026

- **Defect type:** forward-dated reference (not a defect; honesty note)
- **Location:** `\bibitem{Iye:2026P6}` at L4407–L4410. arXiv:2605.05570 (2026). Format YYMM.NNNNN is plausible for May 2026 (today is 2026-05-24).
- **Evidence:** L2648–L2650 prose flags this honestly — "arXiv:2605.05570 (May 2026); we cite it here as an independent corroborating HSC-WIDE null result but do not rely on its quantitative result for any headline statistic in the present manuscript."
- **Verdict:** acceptable as long as the paper is genuinely public on arXiv (which the prose claims). NOT a confabulation flag because the prose explicitly disclaims load-bearing status.

---

## Spot-checked load-bearing externals (8 verifications)

| Cite key | Inline prose claim | Bibitem metadata | Verdict |
|---|---|---|---|
| `Shamir:2022DESI` | "MNRAS 516 2281, DOI 10.1093/mnras/stac2372", ~1.3×10^6 DESI Legacy galaxies | MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372 | **PASS** — stac2372 confirmed correct (v1.0.84 Gemini-DR caught earlier stac2342 typo) |
| `Jia:2023` | CE-ResNet, ApJ 943, 32, arXiv:2210.04168 | ApJ 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa | **PASS** — DOI suffix aca8aa confirmed (v1.0.78 GPT-Pro caught earlier aca9d8 typo); authors correctly listed as Jia, Zhu, Pen |
| `Eskilt:2023` | "β = 0.342° ± 0.094° (3.6σ)" — Cosmoglobe DR1 | A&A 679, A144 (2023), arXiv:2305.02268 | **PASS** — figure matches Cosmoglobe DR1 published value |
| `Cabass:2023` | EFT-of-LSS framework for parity-odd 4PCF, $g_\*$ parameterization | Phys. Rev. D 107, 023523 (2023), arXiv:2210.16320 | **PASS** — Cabass–Ivanov–Philcox 2023 PRD entry accurate |
| `Hou:2023` | "$\sim\!7.1\sigma$ (CMASS) / 3.1σ (LOWZ)" on BOSS DR12 4PCF parity-odd | MNRAS 522, 5701 (2023), arXiv:2206.03625 | **PASS** — significances match published abstract |
| `Philcox:2023` | "$\sim\!2.9\sigma$ blind test" on BOSS | PRD 106, 063501 (2022), arXiv:2206.04227 | **PASS** on content; **minor-3** on key-year |
| `Cahn:2021` | Proposed 4PCF parity-violation test | PRL 130, 201002 (2023), arXiv:2110.12004 | **PASS** on content; **minor-3** on key-year |
| `LueWangKamionkowski:1999` | Π parametrization for chiral GW power asymmetry | PRL 83, 1506 (1999), arXiv:astro-ph/9812088 | **PASS** — seminal parity-violating-tensor reference, correctly summarized |

No confabulated arXiv IDs, no fused journal/volume/page tuples, no DOI-resolves-to-different-paper defects. The v1.0.79–v1.0.95 historical fusion-flag for Ivezic:2019 (arXiv 0805.2366 LSST Science Book vs. ApJ 873 111 reference-design article) is documented in-bibitem as resolved with the arXiv ID stripped (L4540–L4551); this is the correct disposition.

---

## Self-citation cross-check (companion papers P1A / P1B / P2 / P3 / P5)

`grep -n "Paper III\|companion\|Golden 2026\|P1A\|P1B"` returns only `companion artifact` mentions (referring to JSON/PNG files in `pipelines/p2_chirality/outputs/canonical_provenance/`) and `\author{Houston Golden}` at L177. The paper does NOT inline-cite the sibling bounce-portfolio papers. Given that this paper's headline is a chirality-dipole null (NOT a bounce-prediction test), this is reasonable scope discipline — there is no positive cross-reference to P1A/P1B/P2/P3/P5 that requires a bibitem. **No defect on companion-paper cross-citations.**

---

## Verdict summary

| Severity | Count | Items |
|---|---|---|
| BLOCKER | 0 | — |
| MAJOR | 0 | — |
| minor | 3 | Walmsley:2022 orphan; Doroshkevich/White prose-only refs; Cahn:2021 + Philcox:2023 key-year inconsistency |
| nit | 1 | Iye:2026P6 forward-dated (acceptable, honest disclaimer in prose) |

**Recommended close-out actions before R24b/R24c:**
1. Add `\cite{Walmsley:2022}` at L484 lineage paragraph OR delete the orphan bibitem.
2. Add `\bibitem{Doroshkevich:1970}` + `\bibitem{White:1984}` and convert L3732 inline prose to `\cite{}`.
3. Decide arXiv-year-vs-journal-year naming convention and rename one of `Cahn:2021`/`Philcox:2023` for consistency (LOW priority — they resolve correctly).

Paper survives Perplexity citation-rigor cross-check round 1-of-3 with three minor cosmetic findings and zero substantive defects. No confabulated references, no broken cites, no fused metadata. Ready to proceed to R24b (next non-Anthropic perspective in the rotation) once items 1 and 2 are closed.
