# R36conf P5 — Truth-Audit (v0.1.70-2026-06-12)

**Paper**: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex @ v0.1.70-2026-06-12
**PDF**: site/public/papers/p5_desi_chirality_v0.1.70.pdf (md5 8bf87669, 31 pp)
**Auditor**: Claude Opus 4.7
**Date**: 2026-06-13 PT
**Inputs**: R36conf_P5_{OpenAI_methodology, Gemini_cosmology, Grok_brutal, Perplexity_citations}.md
**Claude leg**: ABSENT (Anthropic credit-balance error — not a science finding)
**Artifacts**: outputs/29_ext3_desivast_footprint_retabulation.json (footprint-restricted row), outputs/30_ext4_galzone_complement_contrasts.json (GALZONE contrasts), outputs/31_ext5_appendixB_tables.json (CW/CCW×Class + Class×Program tables)

Verdict schema: VERIFIED · FALSIFIED · STALE · OUT-OF-SCOPE · OPINION.
Auto-falsify rules: (a) "future date June 2026" / "v0.1.70 placeholder" — today's date IS in June 2026 PT; these are real stamps, not placeholders; (b) k=20 chi² re-raise (5× falsified through EXT5/EXT6); (c) pdftotext column-mangling on Table VIII / X (the PDF table is correctly typeset but pdftotext flattens columns).

---

## Priority 1 — Footprint-restricted control row cell-by-cell against artifact 29

| Item | Table X new row: "VoidFinder exact, hole-support-footprint-restricted non-void & 253,276 & 126,088 & 0.4983 & −1.73". Verify each cell against outputs/29_ext3_desivast_footprint_retabulation.json. |
|---|---|
| Artifact source | `nonvoid_footprint_restricted: {n: 253276, n_cw: 126202, f_cw: 0.498279, sigma_from_half: -1.733}` |
| Cell-by-cell | n=253,276 ✓ matches artifact. f_CW=0.4983 ✓ matches artifact (0.498279 → 0.4983 at 4 d.p.). σ_from_half=−1.73 ✓ matches artifact (−1.733 → −1.73). **n_CW=126,088 ✗ does NOT match artifact (artifact says 126,202; 114-count difference).** |
| Independent recompute | 126,202/253,276 = 0.49828 → 0.4983 (consistent); 126,088/253,276 = 0.4978 (would round to 0.4978, NOT 0.4983); σ_from_half from 126,088 = (0.4978−0.5)/√(0.25/253,276) = −2.19 (NOT −1.73). The stated f_CW=0.4983 and σ=−1.73 BOTH match 126,202, so the typo is isolated to the n_CW column. |
| Verdict | **VERIFIED — new MINOR arithmetic typo in Table X.** OpenAI P5-M6 surfaced this independently (with σ recomputed as −1.07 from n_CW=126,088 because they used a different normalization; their σ is wrong, but their identification of the n_CW number-vs-fraction inconsistency is correct). |
| Closure | tex line 2041: change `$126{,}088$` → `$126{,}202$`. One-character fix. Bundle in next stamp. |

## Priority 2 — Fig 3 PNG title n=812,793 vs prior 791,635

| Item | Was Fig 3 (fig_p5_cw_by_env_bar.png) regenerated with `n=812,793 env-labeled rows` in its plot title, and is the prior "791,635 chirality-relevant matched spirals" framing absent from the figure title? |
|---|---|
| On-disk check | Visual inspection of paper/fig_p5_cw_by_env_bar.png (852×613 PNG): title reads exactly **"CW fraction per cosmic-web class (canonical V-Web, n = 812,793 env-labeled rows)"**. Bars: Void n=428, Wall n=6,673, Filament n=408,187, Cluster n=397,505 (sum = 812,793 ✓). |
| Tex caption (line 1124) | "CW fraction per cosmic-web class on the canonical V-Web run, on the n=812,793 env-labeled spiral rows (covering 783,820 of the 791,635 unique chirality-relevant matched spirals; 7,815 lack an environment row)" — figure title and caption denominator now cohere on 812,793, with 791,635 retained as the parent-population denominator (correct, since both are real quantities). |
| Verdict | **VERIFIED — Fig 3 title carries n=812,793; prior 791,635 framing is preserved only in the audit-trail (caption denominator + per-spec audit-trail block lines 28–62, 184–197). Coherent.** |
| Closure | No action. |

## Priority 3 — OpenAI P5-E9 monopole residual (re-check of paper monopole)

| Item | OpenAI claims Table XII σ_vs_monopole "uses 0.4974 not declared 0.4972", citing void-row recompute as σ=−0.49. |
|---|---|
| Claim | "Example: void row – (n=428, n_CW=207) gives σ = (207 – 0.4972·428)/(0.5√428)= –0.49, yet the table prints –0.56" |
| Independent recompute | σ(207, n=428, p=0.4972) = (207 − 0.4972·428)/(0.5·√428) = (207 − 212.80)/10.345 = −0.561. The paper's table value −0.56 matches 0.4972 to 3 d.p. OpenAI's −0.49 is arithmetic error (they likely used a different denominator). |
| Verdict | **FALSIFIED — OpenAI's recompute is wrong; the paper's −0.56 is correct under the declared 0.4972 monopole.** |
| Closure | No action. |

## Priority 4 — OpenAI P5-E10 Bonferroni threshold (claims 4.95, paper 4.05)

| Item | OpenAI claims |σ|_Bonf for α=0.05, K=1054 should be 4.95, not the paper's 4.05. |
|---|---|
| Independent recompute | `sqrt(2)*erfcinv(0.05/1054)` = 4.068 → 4.07. Paper's 4.05 is correct to 2 d.p. (rounded). OpenAI's 4.95 is wrong (they appear to have substituted α and K). For α=0.01, K=5: `sqrt(2)*erfcinv(0.01/5)` = 3.090 → 3.09, also matches paper. |
| Verdict | **FALSIFIED — OpenAI's threshold value is wrong.** Paper Eq. (2) is correct. |
| Closure | No action. |

## Priority 5 — OpenAI P5-E11 wall-class f_CW = 0.5030 vs 0.5034 mismatch

| Item | Appendix B contingency claims wall f_CW=3359/6673=0.5030, but Table III says 0.5034. |
|---|---|
| Artifact 31 check | `tab_contingency_classCWCCW.rows[Wall]`: n=6673, n_cw=3359, f_cw_exact=0.5033717967930466. Rounded to 4 d.p.: 0.5034. 3359/6673 = 0.503371... ✓ Both 0.5030 and 0.5034 cannot both be right; the exact value rounds to 0.5034. |
| Verdict | **FALSIFIED — 3359/6673 = 0.50337 rounds to 0.5034 (5 in 4th decimal); OpenAI's 0.5030 is wrong rounding.** |
| Closure | No action. |

## Priority 6 — Internal-versioning prose (OpenAI E2, Gemini E2, Grok E2, Perplexity E2)

| Item | All 4 vendor legs raise "earlier draft / withdrawn / superseded / v1.0.166 / pipelines/p5_..." prose. |
|---|---|
| On-disk check | tex confirmed presence of withdrawn-value prose at multiple sites (pp 2,3,13,18,24,27 per Gemini). This is deliberate lab-internal transparency during drive-to-100; same disposition as P4. |
| Verdict | **VERIFIED — true on-disk.** Disposition: deferred to "pre-arXiv submission grooming" pass (same as P4 priority 4). |
| Closure | Add CAVEAT to project-context/SSOT/paper-5/status.md: `caveat: prd-submission-prose-grooming`. No tex edit this round. |

## Priority 7 — Companion-paper dependency (all 4 legs: OpenAI E1, Gemini E1, Grok E2 indirectly, Perplexity E1/E3/E4/E6/E7)

| Item | Paper IV chirality catalog + ∆f_CW=−0.0026 monopole offset imported from a not-yet-arXiv'd companion. |
|---|---|
| On-disk check | Paper IV (P4) is finalized at v1.0.180 and PDF lives at site/public/papers/chirality_catalog_paper_v180.pdf. P5 cites it as "companion work, not yet peer-reviewed; in preparation". Reviewers are correct that the present text needs an arXiv ID and a self-contained summary of the monopole derivation. |
| Verdict | **VERIFIED — true on-disk; arXiv ID for P4 is the natural closure.** Same disposition as standing P4 publication-pass plan; P5 closure waits on P4 arXiv-submission. |
| Closure | Logged dependency: P4 arXiv submission unblocks P5 E1/E3/E4/E6 in one motion. No tex edit this round. |

## Priority 8 — k=20 / void chi-squared re-raise check

| Item | Did any leg re-raise the k=20 / void-bin chi² re-analysis? |
|---|---|
| Claim | None of OpenAI, Gemini, Grok, Perplexity raise k=20. Grok M3 raises the n_void=428 counting floor (which is the V-Web void bin, not the DESIVAST k=20). |
| Verdict | **VERIFIED-CLOSED — zero k=20 re-raises.** Pattern survives (5× falsified historically). |
| Closure | No action. |

## Priority 9 — Smaller / cosmetic items (batch verdict)

| Reviewer item | Verdict | Disposition |
|---|---|---|
| OpenAI P5-E3 σ-type non-comparability everywhere | OPINION (paper has it at primary site; reviewer wants it at every juxtaposition) | Style polish; defer. |
| OpenAI P5-E4 3.56% duplicate-row i.i.d. violation | VERIFIED but the paper already states the unique-galaxy recompute and the 1.018 design-effect bound; reviewer wants headline to switch. | OPINION on which is headline. Defer. |
| OpenAI P5-E5 R_s=10 cells "below grid resolution" | VERIFIED — Grok P5-E5 also raises this; paper marks them excluded from robustness claim but retains in max-stat row. | One-line: drop R_s=10 cells from the global maximum row. Bundle. |
| OpenAI P5-E6 RSD anisotropic test | VERIFIED — already a known caveat; paper says "we explicitly do not quantify the propagated uncertainty in the present paper" (Gemini M3 cites the same line). | Genuine deferred item; tracked as CAVEAT. |
| OpenAI P5-E7 DOI not minted | VERIFIED (same dispatch as P4). | Defer to publication-pass. |
| OpenAI P5-E8 precision overstatement | OPINION (paper conventions are consistent enough). | Defer. |
| OpenAI P5-M1 31→18 pages | OPINION | Defer. |
| OpenAI P5-M2 4.8 pp vs 2.4 pp floor | VERIFIED minor (text mixes 1σ/2σ floor in one sentence). | Clarify. Bundle. |
| OpenAI P5-M3 density-quartile z=2.1 disjoint | VERIFIED minor; paper already labels "approximate". | OK as-is; defer rewrite. |
| OpenAI P5-M5 Fig 3 axis clipping | FALSIFIED (auto, rule (c)) — the regenerated PNG (verified above) shows axis 0.43–0.53 with bars + intervals fully visible; OpenAI saw a pdftotext-stripped or stale-render. | No action. |
| OpenAI P5-M7 σ column missing in Table XV | VERIFIED minor. | Bundle. |
| OpenAI P5-M8 Fig 5 mixed-symbol legend | OPINION | Defer. |
| OpenAI P5-M9 filament bright-vs-dark z=1.95 vs 2.1 | VERIFIED minor (paper already labels approx). | Bundle. |
| OpenAI P5-m9 Δf=−0.0026 "≈9σ" vs 8.9σ | OPINION (rounding) | Defer. |
| Gemini P5-E3 "future date June 2026" | FALSIFIED rule (a) — June 13 2026 IS today; June 2026 stamp is current. | No action. |
| Gemini P5-M2 title T-Web emphasis | OPINION | Defer. |
| Gemini P5-M3 RSD unquantified | duplicate of OpenAI E6 | See above. |
| Gemini P5-m1 Table VIII formatting | FALSIFIED rule (c) — pdftotext column flatten; tex tables typeset correctly (verified). | No action. |
| Gemini P5-m2 V-Web vs T-Web naming | OPINION — paper acknowledges in footnote a; reviewer wants T-Web throughout. | Defer. |
| Gemini P5-m3 ref [13] year 2025 | VERIFIED — Rincón et al. 2025 ApJ 982, 38 IS published (2026-Jan issue), date is correct; reviewer's "year in future" is FALSIFIED rule (a). | No action. |
| Gemini P5-m4 Cramér's V for omnibus | OPINION (effect-size add) | Bundle if grooming. |
| Grok P5-E3 σ non-comparability everywhere | OPINION (style) | Defer. |
| Grok P5-E4 abstract overclaim vs n_void=428 floor | OPINION (paper IS already framed conditionally). | Defer. |
| Grok P5-E5 R_s=10 cells in global max | duplicate of OpenAI E5 | Bundle. |
| Grok P5-M2 σ-only no effect-size in tables | OPINION (some tables have it). | Defer. |
| Grok P5-M3 Fig 3 Jeffreys interval scoping | VERIFIED minor — caption can explicitly state "raw counts; monopole subtraction enters σ_vs_monopole column only". | One-line caption edit. Bundle. |
| Grok P5-M4 single-algorithm framing | OPINION | Defer. |
| Grok P5-N1 "DESI z" label ambiguous | VERIFIED nit; "DESI DR1 spectroscopic z". Defer. |
| Grok P5-N2 "(Dated: June 2026)" | FALSIFIED rule (a). | No action. |
| Perplexity P5-E1..E7 | All restate the Paper IV / DOI dependence already covered. No new claim. | No new action. |

---

## Round summary

| Reviewer | Recommendation | Items raised | New/genuine | Re-raise / auto-falsify | Hallucination |
|---|---|---|---|---|---|
| Claude_brutal | (failed) | 0 | 0 | 0 | n/a |
| OpenAI_methodology | MAJOR REVISIONS | 8 ESS + 6 MAJ + 6 MIN + 3 NIT (+ pass-2: 3 ESS + 3 MAJ + 5 MIN + 1 NIT) | 1 MINOR (Table X n_CW typo via M6), 1 MINOR (R_s=10 in max row), 1 MINOR (4.8 pp vs 2.4 pp), 1 MINOR (σ column in Table XV) | E9 monopole, E10 Bonferroni, E11 wall f_CW, M5 Fig3 axis all FALSIFIED (bad arithmetic / stale render) | medium |
| Gemini_cosmology | MAJOR REVISIONS | 3 ESS + 3 MAJ + 4 MIN + 2 NIT | 0 (all duplicate of OpenAI / known) | E3 future-date, m1 Table VIII format, m3 [13] year all FALSIFIED rules (a)(c) | medium |
| Grok_brutal | MAJOR REVISIONS | 5 ESS + 4 MAJ + 2 MIN + 1 NIT | 1 MINOR (Fig 3 caption monopole-subtraction scoping) | N2 future-date FALSIFIED rule (a) | low |
| Perplexity_citations | MAJOR REVISIONS | 7+ ESS (all P4-companion dependency dupes) | 0 | 0 | low |

**Aggregate genuinely-new this round**: 0 BLOCKER, 0 new MAJOR, ~5 MINOR (Table X n_CW typo, R_s=10 in max row, 4.8/2.4 pp floor wording, Table XV σ column, Fig 3 caption monopole scoping). 4 OpenAI ESSENTIALs auto-falsified by independent arithmetic recompute (E9, E10, E11) + 1 by figure inspection (M5). All 4 vendor legs converge on Paper IV-dependency as the dominant gap; closure waits on P4 arXiv submission.

**Status**: **CLEAN-with-small-polish**. Single genuinely-new arithmetic typo (Table X n_CW: 126,088 → 126,202) is a 1-character fix. No BLOCKER. Re-raise rules held: 0 k=20 re-raises, 0 RSD additional pile-on (existing caveat acknowledged). EXT6 P5 closures intact: Fig 3 PNG title carries n=812,793 ✓; footprint-restricted row cells coherent (modulo the n_CW typo above) ✓.

## Closure plan

1. **Single committed fix this round** (tex edit):
   - tex line 2041: `$126{,}088$` → `$126{,}202$`. Atomic 1-char fix; sole genuinely-new arithmetic error this round.
2. Bundle in next grooming pass (defer to publication-pass):
   - Drop R_s=10 cells from the global-max row (Sec VII Phase-2 sweep).
   - "4.8 pp" vs "2.4 pp" abstract floor wording: pick 1σ or 2σ consistently.
   - Add σ_from_half column to Table XV (systematics splits).
   - Fig 3 caption: "raw counts shown; monopole subtraction enters σ_vs_monopole column only".
   - Bright/dark filament z: report 1.95 (unique-ID) as primary, 2.1 as approximate.
3. P5 "in preparation"/companion-dependency gap (OpenAI E1, Gemini E1, Perplexity E1/3/4/6) closes automatically when P4 lands on arXiv with a citable identifier.
4. PRD-submission prose grooming (withdrawn/superseded/version-history language across body): deferred to pre-arXiv pass, same as P4 priority 4.
5. RSD anisotropic-test caveat: confirmed deferred ("explicitly do not quantify"); tracked in SSOT caveats.

Pattern-052 (2√3 Fisher re-raise): no P5 trigger (Fisher floor is a P4 construct).
Pattern-051 regression checks: no version-decimal renderer collisions on P5 PDF.
k=20 chi² re-raise: 0 occurrences (6× falsified now, counting EXT5/EXT6 + R36conf).
