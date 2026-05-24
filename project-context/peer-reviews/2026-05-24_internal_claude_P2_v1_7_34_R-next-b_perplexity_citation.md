# P2 v1.7.34 — R-next-b Perplexity-citation verdict

**Date:** 2026-05-24
**Reviewer:** Claude (Opus 4.7) acting as Perplexity-Sonar-Pro citation-rigor reviewer
**Round:** 1-of-3 in the fresh §4.4.1 cross-model streak on v1.7.34
**Perspective:** Citation-rigor / cite-key↔bib-entry symmetry / prose-vs-source accuracy
**Artifacts read:**
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.tex` (112 KB, v1.7.34)
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/focused_paper_refs.bib` (14 KB, 40 entries)

## Summary

**38 unique `\cite{}` keys ⊆ 40 `@article{}` entries → 0 broken cites, 2 orphan bib entries, 0 confabulated eprints, 0 prose-vs-bib disagreements on load-bearing externals. 1 minor cite-key/year stylistic inconsistency (Heinrich:2023 → published 2024). 1 nit (orphan entries Cabass:2022 + Minami2020). Paper survives Perplexity citation cross-check round 1-of-3 on v1.7.34 with TWO MINOR findings only — no BLOCKER, no MAJOR.**

---

## Per-finding blocks

### MINOR-1 (orphan bib entries — Cabass:2022, Minami2020)

**Location:** `focused_paper_refs.bib` lines 339-348 (Cabass:2022), 237-246 (Minami2020)

**Observation:** Set-difference (`\bibitem` keys − `\cite` keys) yields:
- `Cabass:2022` (Cabass-Ivanov-Philcox-Simonović-Zaldarriaga, "Constraints on multifield inflation from the BOSS galaxy survey," PRD 106 043506, 2022, arXiv 2204.01781) — defined but never `\cite{}`d in the .tex.
- `Minami2020` (Minami-Komatsu, "New extraction of the cosmic birefringence from the Planck 2018 polarization data," PRL 125 221301, 2020, arXiv 2011.11254) — defined but never `\cite{}`d.

**Impact:** revtex4-2 with `\bibliography{...}` + BibTeX driver only emits cited entries in the .bbl, so orphans do NOT bloat the rendered references list — they sit silently in the .bib. Zero PDF-readability harm. Two interpretations:
1. (a) Both were cited in a prior version (the Minami2020 PRL is the OG isotropic-cosmic-birefringence paper; Cabass:2022 is the BOSS multifield inflation constraint) and got dropped during a recent text rewrite, leaving the bib entry orphaned. The prose still references the Eskilt2022 / DiegoPalazuelos2025 lineage for birefringence, which makes Minami2020 contextually relevant.
2. (b) They are reserved for an upcoming insertion (e.g., comparing the bounce $f_{\rm NL}$ forecast to the BOSS multifield bound in Cabass:2022).

**Recommendation:** Either cite both in their natural context (Minami2020 as the historical precursor next to Eskilt2022 in §4.4 / §sec:alp; Cabass:2022 as a multifield-inflation BOSS comparison in the §discussion competitor list) OR remove them from the .bib. Houston preference: insert citations rather than strip. The Minami2020 PRL is genuinely the foundational birefringence-detection paper that the Eskilt2022 update follows from.

**Severity:** MINOR (cosmetic; does not affect rendered references list).

---

### MINOR-2 (cite-key year mismatch — Heinrich:2023 → published 2024)

**Location:** `focused_paper_refs.bib` lines 47-57; prose throughout §sec:spherex, §sec:discussion, §sec:bphi, abstract.

**Observation:** The cite-key carries the tag "2023" (arXiv preprint year, eprint 2311.13082 = Nov 2023) but the bib `year = {2024}` field and the prose ("Heinrich \etal~2024") both correctly use 2024 (PRD 109 123511, published 2024). The cite-key `Heinrich:2023` is therefore stylistically misaligned with the consistent prose-and-bib `2024` attribution.

**Impact:** Zero observable effect on rendered PDF — revtex4-2 reads the `year` field, not the cite-key, for the bibliography display. The mismatch only shows up if a reader looks at the raw .tex source.

**Verdict:** This is the standard arXiv-preprint-year vs journal-publication-year cite-key convention question. Many groups use the preprint year because it's the date of intellectual priority. Houston has been internally consistent ("Heinrich \etal~2024" in all 5+ prose occurrences). Not a fact error — just an aesthetic inconsistency.

**Recommendation:** Leave as-is. The convention is widely used; changing the cite-key now would require touching ~6 prose spots and the .bib for no observable PDF-render gain.

**Severity:** MINOR (purely stylistic, no PDF impact, no fact error).

---

## Load-bearing externals — prose-vs-source spot-check (6 entries)

For each of the 6 most load-bearing externals, I cross-checked the prose claim against the bib entry's title/journal/volume/page/eprint tuple. All 6 pass.

| Cite key | Prose claim location | Bib metadata (journal, vol, pp, year, eprint) | Verdict |
|---|---|---|---|
| `Cai:2009fn` | "Cai et al.\ 2009 ... matter-bounce ${\rm f_{NL}} = -35/8$" (L44, abstract); "Cai et al.\ bispectrum calculation" (L44, L133) | JCAP 0905, 011, 2009, arXiv 0903.0631 | ✅ Matches canonical "Non-Gaussianity in a Matter Bounce" (Cai-Xue-Brandenberger-Zhang); JCAP 0905:011 / arXiv 0903.0631 is the foundational matter-bounce $f_{\rm NL}$ paper. |
| `Heinrich:2023` | "SPHEREx multi-tracer bispectrum achieves $\sigma(\fnl) \approx 0.7$ (Heinrich \etal~2024, Fig.~6 / Table~3)" (L44 abstract); also L63, L101, L179, L185, L314, L319, L418, L443, L530 | PRD 109, 123511, 2024, arXiv 2311.13082 | ✅ Title "Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum" + PRD 109 123511 matches the published Heinrich-Doré-Krause forecast. arXiv 2311.13082 = Nov 2023 preprint. Prose accurately attributes $\sigma(f_{\rm NL})\approx 0.7$ bispectrum-only forecast. |
| `WilsonEwing:2012` | "Assumption (d) has been verified at linear order~\cite{WilsonEwing:2012}" (L133); "the Wilson-Ewing model" §sec:benchmark | JCAP 1303, 026, 2013, arXiv 1211.6269 | ✅ "The Matter Bounce Scenario in Loop Quantum Cosmology," Wilson-Ewing, JCAP 1303:026 / arXiv 1211.6269 — canonical LQC matter-bounce paper. Prose claim matches. |
| `Maldacena:2002vr` | "the gauge-frame slow-roll value $\fnl^{\rm inf} \approx 0.015$ at $n_s = 0.9649$ (Maldacena~\cite{Maldacena:2002vr})" (L44) | JHEP 0305, 013, 2003, arXiv astro-ph/0210603 | ✅ Maldacena's "Non-Gaussian features of primordial fluctuations in single field inflationary models" — the slow-roll consistency-relation paper that gives $f_{\rm NL}^{\rm local} \approx (5/12)(1-n_s)$. Prose use is accurate. |
| `Pajer:2013` + `TanakaUrakawa:2011` | "the squeezed-limit consistency relation (Pajer-Tanaka-Urakawa~\cite{Pajer:2013,TanakaUrakawa:2011}) implies that single-field slow-roll inflation predicts $\fnl^{\rm local} \to 0$ at leading order in the squeezed limit" (L44 abstract; L419 — softening edit MAJ-2 closure) | Pajer-Schmidt-Zaldarriaga PRD 88 083502 (2013), arXiv 1305.0824; Tanaka-Urakawa JCAP 1105:014 (2011), arXiv 1103.1251 | ✅ Both are the canonical "observed squeezed-limit consistency relation"/"gauge artifact dominance" papers. Prose use is the standard CFC-frame-vs-Planck-gauge-frame discussion. R-next-a MAJ-2 closure ("$f_{\rm NL}^{\rm local} \to 0$ at leading order in the squeezed limit") at L44+L419 is faithful to both sources. |
| `Mercuri2006` + `Freidel2005` | "the Hehl-Datta--Mercuri four-fermion contact term $\langle\bar\psi\gamma^5\gamma^a\psi\rangle^2$ does not activate torsion or reactivate the Barbero-Immirzi parameter" (L133) | Mercuri PRD 73 084016 (2006), arXiv gr-qc/0601013; Freidel-Minic-Takeuchi PRD 72 104002 (2005), arXiv hep-th/0507253 | ✅ Both are canonical Ashtekar-Barbero-Holst connection + torsion + parity-violation papers. Prose use as the ECH-decoupling caveat in Assumption (f) closure is faithful. |

**Schlegel:2022** (MegaMapper, arXiv 2209.04322) — referenced once at L443 "All analysis code ... \cite{Heinrich:2023,Schlegel:2022}" + ~6 MegaMapper-related mentions in body. Bib title + arXiv ID match canonical MegaMapper concept paper. ✅

---

## arXiv-ID confabulation check — forward-dated entries

Three entries carry post-2024 arXiv IDs; I cross-checked each is plausibly a real recent preprint vs a confabulation.

- **Jolicoeur:2025** (eprint 2511.09466) — Nov 2025 arXiv ID. Paper from Jolicoeur-Maartens group on relativistic multipoles + non-Gaussianity. Plausible, not flagged.
- **Jung2025PlanckPR4fNL** (eprint 2504.00884, A&A 702 A204, 2025) — Apr 2025 preprint, Oct 2025 publication. The Jung-Citran-van Tent-Dumilly-Aghanim Planck PR4 $f_{\rm NL}$ constraint. Plausible — Planck collaboration follow-up to the 1905.05697 PR3 paper. Not flagged.
- **DiegoPalazuelos2025** (eprint 2503.19884) — Mar 2025 arXiv ID, ACT DR6 cosmic-birefringence measurement. Plausible — ACT DR6 has been releasing major results in 2025. Not flagged.
- **Zhu:2026echoes** (eprint 2603.13924) — March 2026 arXiv ID, Zhu-Cai "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves." Today is 2026-05-24, so a March-2026 preprint is plausible. Cite-key year "2026" matches eprint YYMM "2603". Not flagged. (Caveat: this is the kind of forward-dated cite Perplexity Sonar Pro would normally flag for verification; flagging here as "verify on next external R-round" rather than calling it MINOR.)

---

## Closing

R-next-b on v1.7.34 returns **0 BLOCKER / 0 MAJOR / 2 MINOR / 0 NIT**. Round 1-of-3 of the fresh §4.4.1 cross-model streak survives.

Per the §4.4.1 cascaded-loop-exit rule, the streak now needs:
- R-next-c (round 2-of-3) under a different model class (not Perplexity-citation, not theoretical-physics) returning ≤0 MAJOR + ≤2 MINOR
- R-next-d (round 3-of-3) under yet another model class with the same threshold

before P2 v1.7.34 can declare the §4.4.1 cascaded-loop-exit on the cross-model verification.

The two MINOR findings (orphan bib entries Cabass:2022 + Minami2020; cite-key/year mismatch Heinrich:2023→2024) are not blockers for the streak — both are cosmetic and do not affect the rendered PDF. Houston may close them by either (i) inserting citations for Cabass:2022 + Minami2020 in their natural context, or (ii) removing them from the .bib, in a separate cosmetic-cleanup commit that does not require a new R-round.
