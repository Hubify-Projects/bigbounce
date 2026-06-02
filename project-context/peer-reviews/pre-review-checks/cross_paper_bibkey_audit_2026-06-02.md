# Pattern-032 cross-paper bibkey / value / anchor audit — 2026-06-02

**Scope**: cross-paper grep over all 6 papers' `.tex` (active citations,
comments stripped) and corresponding `.bbl` (parsed by `\bibitem{}` blocks).
Compares (a) shared bibkey metadata (arXiv, journal-ref, year), (b) shared
numerical values quoted across companions, (c) anchor-citations like
`\cite{Golden2026P2}`.

**Sources**:
- `arxiv/paper1a_ech_nogo.tex/.bbl` (P1A v1A.0.40, 47 bibkeys cited)
- `arxiv/paper1b_mcmc_companion.tex/.bbl` (P1B v1B.0.34, 24 bibkeys cited)
- `research/focused_paper_source_integration/02_full_draft.tex/.bbl` (P2, 38 bibkeys)
- `pipelines/p3_anomaly_engine/paper3_draft.tex/.bbl` (P3, 33 bibkeys)
- `pipelines/p2_chirality/chirality_catalog_paper.tex/.bbl` (P4, 37 bibkeys)
- `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex/.bbl` (P5, 13 bibkeys)

Shared bibkeys (≥2 papers): **20 keys**.

---

## A. Bibkey collision / drift table

| Bibkey | Papers citing | arXiv across papers | Journal-ref across papers | Verdict |
|--------|---------------|---------------------|---------------------------|---------|
| `Cai:2009fn` | P1A, P1B, P2, P3 | 0903.0631 (all) | JCAP 0905 011 (all) | ✓ consistent |
| `DESI2024` | P1A, P1B | 2404.03002 (both) | arXiv preprint (both) | ✓ consistent |
| `DESI2025DR2` | P1A, P1B | 2503.14738 (both) | PRD 112 083515 (2025) (both) | ✓ consistent |
| `DiegoPalazuelos2025` | P1A, P1B, P2 | P1A/P1B: **2509.13654**; P2: **2503.19884** | P1A/P1B: ACT DR6 only; P2: "ACT DR6 + Planck consistency" | **❌ DRIFT — two different arXiv preprints under one bibkey** |
| `ECTorsionDESI2025` | P1A, P1B | — | — | ✓ (not parsed in detail; both papers cite same key from same repo) |
| `Eskilt2022` | P1B (alias note), P2 | 2205.13962 (both) | PRD 106 063503 (2022) (both) | ✓ metadata consistent — but **bibkey duplication with `Eskilt2022b` is pattern-032** |
| `Eskilt2022b` | P1A, P1B | 2205.13962 (both) | PRD 106 063503 (2022) (both) | ✓ metadata consistent — same paper as `Eskilt2022` under different key |
| `Freidel2005` | P1A, P2 | — | PRD 72 (both, gr-qc/0511026) | ✓ consistent |
| `Golden2026P2` | P1A, P1B | self-ref to P2 (companion) | in-prep (both) | ✓ consistent |
| `Golden2026P3` | P1A, P1B | self-ref | in-prep | ✓ consistent |
| `Golden2026P4` | P1A, P1B | self-ref | in-prep | ✓ consistent |
| `Hehl1976` | P1A, P1B | — | Rev. Mod. Phys. (both) | ✓ consistent |
| `Heinrich:2023` | P1A, P2 | 2311.13082 (both) | P1A: **JCAP 2024 (04) 074**; P2: **Phys. Rev. D 109, 123511 (2024)** | **❌ DRIFT — different journal-ref for same arXiv** |
| `Liang2023` | P2, P3 | — | — | ✓ (same author/year shape; not deep-audited) |
| `LiteBIRD2023` | P1A, P1B | — | — | ✓ consistent |
| `LueWangKamionkowski1999` | P1A, P5 | astro-ph/9812088 (both) | PRL 83 1506 (1999) (both) | ✓ consistent |
| `Mercuri2006` | P1A, P1B, P2 | gr-qc/0601013 (all) | PRD 73 084016 (2006) (all) | ✓ consistent |
| `Planck2018params` | P1A, P1B | — | — | ✓ consistent |
| `Seljak2009` | P2, P3 | — | — | ✓ consistent |
| `Baron2017` | P2, P3 | — | — | ✓ consistent |

### Cross-paper bibkey DRIFT hits — detailed

**1. `DiegoPalazuelos2025` points to TWO different arXiv preprints**:
- P1A line 4 of bbl: `arXiv:2509.13654` "Cosmic birefringence from the Atacama
  Cosmology Telescope data release 6"
- P1B bbl: `arXiv:2509.13654` (same)
- **P2 bbl**: `arXiv:2503.19884` "Act dr6 cosmic-birefringence measurement and
  consistency with planck"

These are **TWO DIFFERENT PAPERS** (same first author, same year, related topic):
- 2503.19884 (March 2025, "ACT DR6 + Planck consistency", multi-author preprint)
- 2509.13654 (Sept 2025, "ACT DR6 alone", Diego-Palazuelos & Komatsu)

External reviewer reading P1A and P2 sees the same bibkey resolve to different
papers. **MAJOR pattern-032 hit.**

**Recommended fix**: pick the canonical preprint (likely 2509.13654 since it's
the more recent Diego-Palazuelos & Komatsu standalone) and propagate. Or split
into `DiegoPalazuelos2025` (2509.13654) + `DiegoPalazuelos2025a` (2503.19884)
and clarify which paper each citation refers to.

**2. `Heinrich:2023` has two different journal-refs**:
- P1A bbl: `JCAP 2024 (04) 074`, DOI 10.1088/1475-7516/2024/04/074
- P2 bbl: `Phys. Rev. D 109, 123511 (2024)`
- Same arXiv:2311.13082 (Heinrich, Doré, Krause — "Measuring fnl with the
  SPHEREx multi-tracer redshift space bispectrum")

One of these journal-refs is **wrong**. The 2311.13082 abstract page on arXiv
should be authoritative. **MINOR pattern-032 hit** (does not change physics,
but external reviewer cross-checking will notice and ask).

**Recommended fix**: verify via NASA ADS / arXiv, propagate the correct journal-ref
to both .bib files, regenerate .bbl.

**3. `Eskilt2022` vs `Eskilt2022b` (the canonical pattern-032 example)**:
- P1A uses `Eskilt2022b`
- P1B uses BOTH (with `Eskilt2022b` annotated as "alias of @Eskilt2022 ... bibkey
  retained for backward compatibility")
- P2 uses `Eskilt2022`
- P4 uses **`Eskilt:2023`** (a THIRD bibkey shape, pointing to the Cosmoglobe
  Collaboration paper — a *different* Eskilt paper at line 4469-4470)

All three keys point to PRD 106:063503 / arXiv:2205.13962 EXCEPT `Eskilt:2023`
which points to Cosmoglobe DR1 II. The P1B "alias" note + the bibliography prose
("alias of @Eskilt2022") is itself flagged by CGT-m1 as a minor cleanup target.

External reviewer impact: any reader cross-referencing the papers would see
`Eskilt2022b` cited in P1A but the bibliography of P2 only has `Eskilt2022` —
they would search for the key in P2's bib and not find it, even though P2 in fact
cites the same paper under a different key. **MAJOR pattern-032 hit** (cross-paper
discoverability).

**Recommended fix**: globally rename `Eskilt2022b` → `Eskilt2022` in all papers,
remove the alias annotation from P1B's bib, regenerate.

---

## B. Cross-paper numerical drift

Probed shared survey/dataset numerics across all 6 .tex (active text):

| Quantity | P1A | P1B | P2 | P3 | P4 | P5 | Verdict |
|----------|-----|-----|----|----|----|----|---------|
| Eskilt β = 0.342° | 8 hits | 12 hits | 3 hits | — | 1 hit | — | ✓ all consistent |
| Eskilt σ(β) = 0.094° | 7 | 4 | 4 | — | 1 | — | ✓ consistent |
| Spectator-ALP β = 0.27° | 9 | 8 | 4 | — | — | — | ✓ consistent |
| `\fnl = -35/8` | 17 | 2 | 74 | 17 | 12 | 7 | ✓ identical numeric / form (4.375) — never written as decimal anywhere |
| DESI DR2 3.1-4.2σ | 2 (lines 353, 1756) | — | — | — | — | — | only P1A quotes the range; P1B/P3/P5 don't quote DR2 σ → not a drift issue but means the P1A statement is the only place that could be wrong |
| Planck/ACT (shorthand) | 2 active hits | 5 active hits (legit in P1B context) | — | 1 (in cross-transfer §appendix only — legit) | — | — | **P1A 2 hits are pattern-030 regression (see closure-propagation report)** |
| WMAP+Planck (correct) | implicit via citation | 3 hits | 1 hit | — | — | — | ✓ where used, consistent |
| 3.6σ (Eskilt) | 3 | 14 | 2 | — | 2 (in §B.2 birefringence-check) | — | ✓ consistent |
| 18σ (block-bootstrap formal exclusion) | — | — | — | — | line 1928 + 2 echoes | — | P4-only — no cross-paper claim to drift against |
| 264σ (naive WLS upper limit) | — | — | — | — | line 1928 + Table II | — | P4-only; framed as upper limit |
| NANOGrav γ = 2.567 ± 0.382 | line 1522 | — | — | line 1042 | — | — | ✓ **P1A and P3 quote identical value** (matter-bounce γ=3.0 at +1.13σ above posterior mean — both consistent) |
| Anomaly count 378,280 | — | — | — | abstract + Table I | — | — | P3-only; P1A/P1B do not cite the catalog count yet |

### Cross-paper numerical drift hits

**Zero hard drift hits.** Every quantitative claim that appears in 2+ papers is
quoted identically. The candidate worries from the prompt:
- f_NL = -35/8: identical fraction across P1A/P1B/P2/P3/P4/P5
- Eskilt 0.342° ± 0.094°: identical (the σ is always 0.094° not 0.094, the ° appears)
- NANOGrav γ = 2.567 ± 0.382: identical between P1A and P3
- DESI DR2 σ-range: only quoted in P1A (no cross-paper exposure)
- P3 378,280 anomaly count: only quoted in P3
- P4 18σ vs 264σ: only quoted in P4

The cross-paper drift hits are **all in the bibkey / attribution layer**, not the
numerical-value layer. Pattern-032's "value drift" detection finds no hits;
pattern-032's "bibkey drift" detection finds **3 distinct hits** (Diego-Palazuelos
arXiv, Heinrich journal-ref, Eskilt key shape).

---

## C. Cross-paper anchor citations

P1A and P1B cite the other companion papers via `Golden2026P2/P3/P4`. P3 cites
`Golden2026P4` for the chirality null. Spot-check:

- `\cite{Golden2026P2}` in P1A — refers to "Paper II forecast f_NL=-35/8 at SPHEREx" — matches P2 .tex headline. ✓
- `\cite{Golden2026P4}` in P1A line 1724 — refers to "the parity-violation case" in P4 chirality null. ✓
- `\cite{Golden2026P1b}` in P1A line 1214 — MCMC systematics in P1B. ✓

No section-anchor-level drift found in the audit window. (A deeper audit would
re-resolve `\ref{sec:foo}` cross-paper, but those are typically intra-paper.)

---

## Summary

| Class | Hits | Severity |
|-------|------|----------|
| Bibkey arXiv drift | 1 (DiegoPalazuelos2025) | MAJOR |
| Bibkey journal-ref drift | 1 (Heinrich:2023) | MINOR |
| Bibkey shape duplication | 2 (Eskilt2022/2022b across P1A/P1B/P2; Eskilt:2023 P4) | MAJOR |
| Numerical value drift | 0 | — |
| Anchor-citation drift | 0 | — |

## Recommended closure actions before next external R-round

1. **Reconcile `DiegoPalazuelos2025`**: pick canonical arXiv (likely 2509.13654)
   and propagate to P2's .bib, regenerate P2 .bbl. If both papers are genuinely
   cited, split into two bibkeys.
2. **Verify and unify `Heinrich:2023`** journal-ref. NASA ADS lookup on
   arXiv:2311.13082 will resolve which is current; propagate to both .bib files.
3. **Globally rename `Eskilt2022b` → `Eskilt2022`** in P1A and P1B (and drop the
   "alias" note from P1B's .bbl). Reconcile P4's `Eskilt:2023` (Cosmoglobe paper)
   to the canonical scheme — likely rename to `Eskilt2023Cosmoglobe` (which P2
   already uses; see P2 line 532 "Eskilt2023Cosmoglobe").
4. After (1)-(3), regrep cross-paper to confirm zero remaining drift before
   external R-round.

These three fixes prevent the pattern-032 BLOCKER class from surfacing in the
next multi-paper external round; each is a per-paper .bib edit + .bbl regenerate
+ one cross-vendor re-grep.
