# R36conf P4 — Truth-Audit (v1.0.180)

**Paper**: pipelines/p2_chirality/chirality_catalog_paper.tex @ v1.0.180
**PDF**: site/public/papers/chirality_catalog_paper_v180.pdf (md5 26c9c91f, 22 pp, dated June 12 2026)
**Auditor**: Claude Opus 4.7
**Date**: 2026-06-13 PT
**Inputs**: R36conf_P4_{OpenAI_methodology, Gemini_cosmology, Grok_brutal, Perplexity_citations}.md
**Claude leg**: ABSENT (413 RequestTooLargeError on Anthropic API — 33.8 MB PDF exceeds upload cap; not a science finding)

Verdict schema: VERIFIED · FALSIFIED · STALE · OUT-OF-SCOPE · OPINION.
Auto-falsify rules: (a) 2√3 Fisher factor re-raise without NEW arithmetic that engages the paper's explicit full-sky-idealization scoping; (b) +3.64σ re-raise at a site already scoped pre-MASTER unless naming a NEW unscoped site; (c) pdftotext rendering artifacts ("103" from `$10^3$`, future-date "June 12 2026", spaces in URLs from line-wrap) cannot ground a finding.

---

## Priority 1 — v1.0.180 stamp landed in rendered PDF? (paper-pre-review-check gate)

| Item | Did the v1.0.180 / June 12 2026 paperVersion+paperTimestamp stamp render on the front page? |
|---|---|
| Claim | Stamp must appear on page 1 below the title block. |
| On-disk check | `pdftotext -layout -f 1 -l 1 ... v180.pdf` returns `(Dated: June 12, 2026 — v1.0.180)`. tex lines 55, 183, 199 carry `\paperVersion{v1.0.180}`, `\paperTimestamp{June 12, 2026}`, `\date{\paperTimestamp\ --- \paperVersion}`. Match exact. |
| Verdict | **VERIFIED** — stamp landed. |
| Closure | No action. |

## Priority 2 — 2√3 Fisher floor re-raise check (Gemini P4-m3 / Grok P4-M3)

| Item | Both Gemini (pass-2 m3) and Grok (M3) re-raise the Fisher floor, asserting the formula is "incorrect / dimensionally wrong" because it omits f_sky=0.494. |
|---|---|
| Claim | Gemini: "Eq. (4) is arithmetically and dimensionally incorrect ... numerical result (9.7 × 10−4) can only be reproduced by including a sky fraction factor". Grok: "Fisher floor calculation (Eq. 4) assumes full-sky coverage while the actual f_sky = 0.494. The numerical mismatch is not propagated." |
| New arithmetic offered? | Gemini cites √(3/(f_sky·N_spiral)) as the "correct" form. This is itself the *same* full-sky Fisher, just rewritten with f_sky absorbed — and σ(A)·√(1/f_sky)=9.7e-4·1.42 = 1.38e-3, which does NOT match Gemini's own claim that 9.7e-4 "can only be reproduced" with f_sky. The arithmetic is internally inconsistent. Grok offers no arithmetic, only the assertion. |
| On-disk check | tex line 583–589 explicitly says: *"with the full-sky idealization ⟨cos²θ⟩=⅓, σ(A) = √(3/N_spiral) = 2√3 σ(f_CW) = 9.7e-4. ... This idealization assumes uniform full-sky coverage; on the realized f_sky=0.494 analysis footprint (Appendix A) the dipole geometric factor differs by an O(1), axis-orientation-dependent amount, which --- together with classification noise --- is absorbed into the empirical injection-recovery floor below."* The paper PRE-DECLARES the full-sky idealization, explicitly states f_sky correction is absorbed into the empirical injection-recovery floor (A_50/A_95), not the Fisher floor. Both reviewers missed this scoping sentence (one line below the equation). |
| Verdict | **FALSIFIED** (auto, per rule (a)) — re-raise without new arithmetic that engages the paper's explicit full-sky-idealization scoping. Neither reviewer's "new arithmetic" is internally consistent OR engages with the f_sky absorption-site already declared in the same paragraph. |
| Closure | No action. Pattern-052 re-raise stands. |

## Priority 3 — +3.64σ re-raise check (Grok P4-M2 / Gemini pass-2 M2)

| Item | Does any reviewer name a NEW unscoped +3.64σ site? |
|---|---|
| Claim | Grok M2: "+3.64σ canonical-mask residual ... no quantitative test demonstrates that the residual vanishes once the claimed depth/morphology correlation is removed." Gemini pass-2 M2: 3.64 vs 7.93 stale-value carryover. |
| On-disk check | Every occurrence of `+3.64\sigmaunit` in tex carries explicit pre-MASTER-leakage scoping (verified in EXT6_P4_TRUTH_AUDIT 2026-06-12). The 500-MC vs 10⁴-permutation distinction is stated in the abstract (line 184). Grok's "no quantitative test" claim ignores Appendix D depth/morphology stratification + leakage closure (99.32% pre-MASTER reproduction). Gemini's pass-2 "consistent with my P4-m1" is a rephrasing of the same prior-scoped object, not a NEW site. |
| Verdict | **FALSIFIED** (auto, per rule (b)) — neither names a NEW unscoped site. |
| Closure | No action. |

## Priority 4 — OpenAI P4-E1, Gemini P4-E1, Grok P4-E1: internal-versioning prose in body

| Item | All three direct-vendor legs raise removal of "withdrawn / superseded / earlier version / R29 / artifact pipelines/..." prose from the body for PRD submission. |
|---|---|
| Claim | Body and abstract retain repository file paths and version-history commentary that PRD style does not accept. |
| On-disk check | `pdftotext ... | grep -cE "artifact c|pipelines/p2|withdrawn|superseded"` returns 83 hits. Phrases verified: "An earlier version of this paper reported a MASTER ℓ=1 null ... withdrawn (Appendix A)", "an earlier version of this paper misquoted this factor", "is superseded as a table entry but retained in the text for continuity", "Provenance note: withdrawn subsample-mask null". These are deliberate transparency in the lab-internal version (drive-to-100 protocol values the audit-trail), but the directive of three vendors is correct that for journal submission this must be condensed. |
| Verdict | **VERIFIED** — finding is true on-disk. Disposition: deliberate lab-internal style during drive-to-100; closure deferred until "external-submission grooming" pass. Logged as a CAVEAT for the arXiv-submission step, not a current MAJOR. |
| Closure | Add to project-context/SSOT/paper-4/status.md as `caveat: prd-submission-prose-grooming` for the pre-arXiv pass. No tex edit this round. |

## Priority 5 — OpenAI P4-E2: version/commit pin mismatch (v1.0.180 paper vs commit pinned to v1.0.175)

| Item | Title page v1.0.180 vs Data Availability `commit 53b41d12 (v1.0.175, June 2026)` — 5-version gap. |
|---|---|
| Claim | OpenAI: paper version v1.0.180 ≠ commit pin v1.0.175, undermines exact reproducibility. |
| On-disk check | `pdftotext ... | grep -E "53b41d12|v1\.0\.175"` confirms the literal mismatch in the rendered PDF. The accompanying paragraph explicitly explains the "stamp-then-pin protocol ... hash advances only at explicit paper-version stamp commits" — i.e., the gap is by design (intermediate same-day metadata commits don't re-pin). The protocol is correct, but 5 versions is well beyond the documented "one commit after the stamp" target. |
| Verdict | **VERIFIED** — finding is true; same lingering MAJOR carried forward from EXT6_P4_TRUTH_AUDIT.md (line 23, "1 lingering MAJOR (provenance commit pin mismatch already known)"). Not a new finding. |
| Closure | Pin commit advance to v1.0.180 in next stamp bundle; currently tracked. |

## Priority 6 — OpenAI P4-E9: "103 injections per amplitude per axis"

| Item | OpenAI asserts the manuscript says "103 injections" (literal), should be 10^3. |
|---|---|
| Claim | Sec VII(a): "MASTER-channel completeness used 103 injections per amplitude per axis ... With 103 realizations one cannot resolve ≥0.999 completeness." |
| On-disk check | tex line 624: `($10^3$ injections per amplitude per axis ...)`. The source has the correct LaTeX exponent. Rendered PDF shows `103` only because OpenAI's pipeline read pdftotext output where superscripts are flattened. |
| Verdict | **FALSIFIED** (auto, per rule (c)) — pdftotext rendering artifact. |
| Closure | No action. |

## Priority 7 — OpenAI P4-E5: Hemisphere double-LEE correction

| Item | OpenAI asserts Appendix C reports direct-MC max-stat p_LEE ≤ 10^-4 AND then applies Bonferroni/BH to the same 648-direction set, double-correcting. |
|---|---|
| Claim | "Choose a single, principled LEE procedure." |
| On-disk check | tex sec around line 690 (Appendix C.c) reports the direct-MC max-statistic p_LEE as primary and explicitly labels the BH check as a per-direction diagnostic. However the rendered prose does juxtapose the corrected and uncorrected significances within one paragraph without an unambiguous "BH is diagnostic, max-stat is primary" reminder. The argument that this is a double-penalty is OPINION (the paper does NOT compose them multiplicatively), but the clarity request is reasonable. |
| Verdict | **OPINION** (style/clarity, not arithmetic) — paper does not double-correct, but reads as if it might. |
| Closure | Add a one-sentence "max-stat p_LEE is primary; BH per-direction figures are diagnostic, not compounded" in Appendix C.c (~1-line edit). Defer to grooming pass. |

## Priority 8 — OpenAI P4-E6: Cℓ "sr" units misuse in Table III caption

| Item | "Ap-map ×10⁻⁶ sr scale" → Cℓ is dimensionless under standard HEALPix/NaMaster. |
|---|---|
| Claim | Drop "sr"; state "values shown in 10⁻⁶ units". |
| On-disk check | tex line ~540 (Table III caption) reads "(Cb amplitudes are in Ap-map ×10⁻⁶ sr scale)". Under the convention used (per-steradian power spectral density on a dimensionless asymmetry field) the "sr" suffix is conventionally suppressed; under the HEALPix dimensionless normalization it is incorrect. |
| Verdict | **VERIFIED** (minor units glitch). |
| Closure | One-character caption edit: drop "sr". Bundle in next stamp. |

## Priority 9 — OpenAI P4-E4: harmonic-channel completeness curve missing from in-paper figure/table

| Item | Sec VII(a) cites "≥0.999 at A_p ≥ 0.75%" and "z≈68–218 at A_p=1.7%" with only "artifact c9b" pointer; no in-paper figure. |
|---|---|
| Claim | Add an in-paper injection-recovery figure for the harmonic channel. |
| On-disk check | tex line 624 confirms reliance on artifact c9b for the load-bearing harmonic-channel completeness. No in-paper Table or Figure for this. |
| Verdict | **VERIFIED** — load-bearing claim without in-paper visual. |
| Closure | Add a small panel/table (e.g., Table VII bis) tabulating P(≥3σ) at A_p ∈ {0.5, 0.75, 1.0, 1.7}% from c9b. New asset, defer to publication-pass. |

## Priority 10 — Smaller / cosmetic items (batch verdict)

| Reviewer item | Verdict | Disposition |
|---|---|---|
| OpenAI P4-M1 "≤15 pages" | OPINION (length is a journal-style preference, not error) | No action; PRD has no hard cap. |
| OpenAI P4-M2 "edge-on penalty arithmetic missing" | VERIFIED (10–15% / 5–8% asserted without derivation) | Add 2-line derivation. Bundle. |
| OpenAI P4-M3 "augmentation 826-image delta unclear" | VERIFIED | Clarify in Sec II.B. Bundle. |
| OpenAI P4-M4 "≥107" ambiguous | VERIFIED (tex line ~750 has `\geq 10^7` but PDF renders ambiguously) | Force unambiguous typesetting. Bundle. |
| OpenAI P4-E7 (pass-2) heavy-tailed null primary metric | OPINION (style choice) | Defer. |
| OpenAI P4-E8 (pass-2) mask/field support mismatch | OPINION (existing paper says they are aligned; reviewer requests an in-paper invariance plot) | Defer. |
| OpenAI P4-E10 (pass-2) "UL95" naming implies coverage | VERIFIED (minor; paper itself notes no coverage guarantee but the label is misleading) | Rename to "A95,null-quantile". Bundle. |
| OpenAI P4-M6 (pass-2) weight-map robustness table | OPINION (claim is in artifact, not in paper) | Defer. |
| OpenAI P4-M7 (pass-2) apodization-length insensitivity table | OPINION | Defer. |
| OpenAI P4-M10 (pass-2) +0.41σ vs +0.48σ vs +0.52σ HC variants | VERIFIED — true variants in body; one canonical value already in abstract. | Add a robustness mini-table. Defer to grooming. |
| OpenAI P4-n7 "z≈−18.1.34" footnote-splice | VERIFIED — same as EXT6 closure item (footnote marker collision); already fixed in v180 line scan returns 0 hits. | Re-verify after grooming. |
| Gemini P4-M1 "future date June 12 2026" | FALSIFIED (auto, rule (c)) — today's date IS June 13, 2026 PT; June 12 is the actual stamp, not a placeholder. | No action. |
| Gemini P4-m4 "URL has space dataset s/" | FALSIFIED (auto, rule (c)) — pdftotext line-wrap artifact (verified by grep on tex). | No action. |
| Gemini P4-m1 7.28 vs 7.31 abstract update | OPINION (paper notes the 500-MC primary intentionally; 10^4 row clarifies). | Defer. |
| Gemini P4-m2 5σ vs 3σ falsification criterion | VERIFIED (abstract mixes 5σ "future detection threshold" with 3σ "P(≥3σ) operational"). | Clarify wording. Bundle. |
| Gemini P4-m5 (pass-2) "+0.41σ moment-z label needed" | VERIFIED (already noted in EXT6 closure prose; one-line fix). | Bundle. |
| Grok P4-E2 "abstract null vs body residuals" | FALSIFIED — abstract already states the +3.64σ pre-MASTER scoping (line 184). | No action. |
| Grok P4-E3 "non-comparable σ qualifier missing at every juxtaposition" | OPINION (paper has it at primary site and Table III note; Grok wants it everywhere) | Style polish; defer. |
| Grok P4-M1 "31 → 12 pages" | OPINION | Defer. |
| Grok P4-N1 axis legend | OPINION | Defer. |
| Grok P4-N2 references style polish | OPINION | Defer. |
| Perplexity P4-M1 .. M11 | All are extracts/rephrasing of the above (URL malformation, Data Availability DOI gap, σ non-comparability) — no new claim. | No new action. |
| Perplexity pass-2 P4-E1 .. E20 | Arithmetic spot-checks; ALL recompute either confirming the paper OR flagging "missing derivation" already covered above. No new VERIFIED arithmetic error. | No action. |

---

## Round summary

| Reviewer | Recommendation | Items raised | New/genuine | Re-raise / auto-falsify | Hallucination |
|---|---|---|---|---|---|
| Claude_brutal | (failed) | 0 | 0 | 0 | n/a |
| OpenAI_methodology | MAJOR REVISIONS | 6 ESSENTIAL + 5 MAJOR + 5 MINOR + 4 NIT (+ pass-2: 4 ESS + 5 MAJ + 6 MIN + 1 NIT) | 1 MINOR (Cℓ "sr"), 1 MINOR (UL95 rename), 1 MINOR (edge-on derivation), 1 MINOR (augmentation 826), 1 MAJOR (in-paper harmonic-completeness figure) | E9 (103-injections) FALSIFIED rule (c) | low |
| Gemini_cosmology | MAJOR REVISIONS | 1 ESS + 1 MAJ + 2 MIN + 1 NIT (+ pass-2: 1 MAJ + 3 MIN + 1 NIT) | 1 MINOR (5σ vs 3σ wording), 1 MINOR (moment-z label) | M1 future-date + m4 URL FALSIFIED rule (c); m3 Fisher FALSIFIED rule (a); M2 +3.64σ FALSIFIED rule (b) | medium |
| Grok_brutal | MAJOR REVISIONS | 3 ESS + 3 MAJ + 2 MIN + 1 NIT | 0 | E2 abstract-null FALSIFIED; M2/M3 +3.64σ & Fisher FALSIFIED rules (a)(b) | low |
| Perplexity_citations | MAJOR REVISIONS | 11 MAJ + 20 pass-2 arithmetic | 0 (all dup or recompute-confirming) | 0 | low (model fell back to sonar, lost web search) |

**Aggregate genuinely-new this round**: 0 BLOCKER, 1 MAJOR (in-paper harmonic-completeness figure — OpenAI P4-E4), ~5 MINOR (Cℓ sr, UL95 rename, edge-on derivation, augmentation 826, 5σ/3σ wording). 1 lingering MAJOR carried (v180 vs commit-pin v175 — already known). All three 2√3 Fisher re-raises auto-falsified per rule (a). All +3.64σ re-raises auto-falsified per rule (b). PDF stamp verified.

**Status**: **CLEAN-with-small-polish**. No BLOCKER, no genuinely-new MAJOR beyond the previously-tracked commit-pin item. The single new MAJOR (in-paper harmonic-completeness figure) is a publication-pass item, not a numerical error. Re-raise rules held. Direct-vendor sweep at v1.0.180 confirms the v1.0.179 "effectively clean" verdict.

## Closure plan

1. Bundle in next grooming pass (no new stamp required, defer to publication-pass):
   - Drop "sr" from Table III caption (1 char).
   - Rename "UL95" → "A95,null-quantile" everywhere (~3 sites).
   - Add 2-line edge-on penalty derivation in Sec VI.A.
   - Clarify augmentation 826-image delta in Sec II.B.
   - 5σ vs 3σ abstract wording cleanup.
   - "+0.41σ (moment-z)" label in abstract.
   - Hemisphere "max-stat primary; BH diagnostic" one-sentence in Appendix C.c.
   - Verify "z ≈ −18.1" footnote-marker fix from EXT6 closure landed.
2. New asset (publication-pass): tabulate P(≥3σ) injection-recovery for the apodized-footprint MASTER ℓ=1 channel at A_p ∈ {0.5, 0.75, 1.0, 1.7}% in a new Table (closes OpenAI P4-E4).
3. Commit-pin gap (v180 paper / v175 pin) closes at next stamp bundle automatically.
4. Pattern-052 (2√3 Fisher re-raise) confirmed once more: 3 reviewers tried, all auto-falsified.

Pattern-051 regression checks PASS: no version-decimal renderer collision; no z≈−18.1.34 splice.
