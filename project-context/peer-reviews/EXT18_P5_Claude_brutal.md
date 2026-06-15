# EXT18 — P5 DESI Environmental Chirality — Claude_brutal Referee Report

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic leg — replaces failed API call, see note)
- **Paper:** P5 — Environmental Dependence of Spiral Chirality (DESIVAST three-algorithm + T-Web tidal cross-check)
- **Version:** v0.1.80 (manuscript tag v0.1.80-2026-06-13)
- **Round:** EXT18
- **Pages reviewed:** 1–32 (full PDF, both halves, every figure/table/equation)
- **Mode:** Brutal honesty; null/independence framing; σ-floor arithmetic; abstract↔body consistency; leftover-tag/duplicate-phrase scan. T-Web nomenclature already disclosed (title footnote + Sec IV footnote) — NOT re-raised.
- **Note:** The API Anthropic leg failed on a billing 400 (credit balance). This report is the live Claude Code sub-agent substitute with full native-PDF read.

---

## Summary judgment

This is an honestly-framed null/independence result. The paper repeatedly and
explicitly labels itself a controlled non-detection ("a null is not positive
evidence"), separates the primary DESIVAST-anchored path from secondary T-Web
diagnostics with a pre-registration caveat (§V B, Table II), and correctly
attributes the large negative σ values (−2.61σ filament, −4.66σ cluster, −5σ
catalog monopole) to the Paper IV catalog-wide classifier monopole leaking into
larger-n bins rather than to environment. The σ_vs-monopole table (Table XII)
collapses all four classes to |σ|<1.15, which is the correct honest move. No
overclaim of "discrimination" or "detection" was found. Arithmetic verified
independently below — all clean.

---

## Arithmetic verification (independent recompute)

All checks PASS.

- **Table III σ_from-half** (n=812,793 parent, σ=(n_CW−0.5n)/(0.5√n)):
  - void n=428, n_CW=207 → −7/10.344 = **−0.677** → −0.68 ✓
  - wall n=6673, n_CW=3359 → +22.5/40.84 = **+0.551** → +0.55 ✓
  - filament n=408,187, n_CW=203,261 → −832.5/319.45 = **−2.606** → −2.61 ✓
  - cluster n=397,505, n_CW=197,284 → −1468.5/315.24 = **−4.658** → −4.66 ✓
- **Range:** 0.5034−0.4836 = **0.0198** (1.98 pp) ✓
- **Eq.(1) σ_pred = 2·Δf·√N, Δf=−0.0026:** filament 2(−0.0026)√408187 = **−3.32** ✓; cluster **−3.28** ✓
- **Table IV σ_pred:** 2(−0.0026)√158327 = **−2.069** → −2.07 ✓
- **Abstract n=428 void floor:** 1σ = 0.5/√428 = **2.42 pp** ✓; offset 0.4836→1.64 pp ✓; 1.64/2.42 = **0.677σ** ✓ (consistent with −0.68)
- **Table XVI marginals:** CW=404,111 (=203261+197284+3359+207 ✓), CCW=408,682, sum=812,793 ✓
- **P5 monopole 0.4972 → σ_pred:** 2·0.0026·√791635 = **+4.6σ** ✓ (text states 4.6σ)
- **Bonferroni thresholds:** √2·erfc⁻¹(0.05/5)=2.58 (B5 two-sided) ✓; 0.05/9→2.77 ✓; 0.01/5→3.09 ✓
- **Abstract per-class fractions** (0.4980 fil, 0.4963 clu, 0.5034 wall, 0.4836 void) **match Table III exactly**; all σ match.

---

## ESSENTIAL findings

None.

## MAJOR findings

**M1 — Title galaxy/void count (KNOWN OPEN HOUSTON ITEM, flagged not adjudicated).**
The title reads "...Test on 56,981 Void Spirals..." while the headline T-Web
environment table (Table III, §VI A) is anchored on 791,635 chirality-relevant
matched spirals / 783,820 environment-matched. The 56,981 figure is the
DESIVAST *primary* void-class sample (§VIII), defensible since §V B declares
DESIVAST the primary path. This is the pre-flagged open title-count decision.
Per task scope: recommend the title foreground the environment-matched
**783,820** sample (or the 791,635 chirality-relevant sample) as the headline
test size, with 56,981 named as the void-class subsample — consistent with how
the abstract orders the ledger. Houston decision item, not a new defect.

## MINOR findings

**m1 — Abstract is dense (~95 lines, single block).** Accurate but exceeds
typical PRD abstract length/readability; packs full primary/secondary ledger,
five σ values, two χ² tests, Phase-2 sweep, three nulls, and RSD scope into one
paragraph. Optional fix: push the secondary-path enumeration to the body so the
headline null + primary DESIVAST Δf_CW=+0.0007 leads more cleanly. Not a
correctness issue.

**m2 — σ_pred denominator convention.** The paper retains the 0.5/√N denominator
for cross-table comparability and documents that exact √(p₀(1−p₀)/N) differs
<0.01% at p₀=0.4972. Disclosed and correct; noting only that a reader could
momentarily read σ_pred as a standard binomial z. Existing footnote covers it.
No action required.

**m3 — Inline artifact-path filenames.** Numerous committed JSON/script
provenance paths (e.g. `outputs/27_ext1_logistic_program_control.json`,
`21_r23conf_meta_closures.json`) appear inline. Legitimate reproducibility
anchors, NOT leftover audit tags — the `ext1`/`r23conf`/`ext5` substrings are
filename fragments. Confirm via `/latex-audit` none overflow the column (visual
render shows them wrapping inside-column). No content fix.

## Checks that came back CLEAN

- No `TODO`/`FIXME`/`XXX`/`TBD`/`placeholder`/`[citation]`/`??` prose tags.
- No leftover EXT-round or R-round audit annotations in body text.
- No duplicate sentence/phrase blocks across abstract/body.
- Null framing honest throughout: "a null is not positive evidence" (§VIII A,
  XIII); primary/secondary separation declared *before* results (§V B); the −5σ
  monopole explicitly attributed to Paper IV classifier bias, not environment
  (Table XII, §VIII F, §XII A).
- σ floors and Bonferroni thresholds all recompute correctly.
- Abstract numbers match body tables exactly.
- T-Web nomenclature disclosure present (title footnote `a` + Sec IV
  "Nomenclature reminder") — as expected, not re-raised.
- RSD limitation honestly scoped (§XIII) as a fixed-redshift-space statement;
  anisotropic-eigenvalue caveat carried explicitly.
- Appendix A toy EFT operator explicitly "order-of-magnitude estimate, not a
  quantitative ALP-coupling exclusion" + rotational/gauge-invariance caveats —
  appropriately hedged, no overclaim.

---

## FINAL VERDICT

**ACCEPT** (pending the M1 title-count Houston decision, which is editorial and
already known — not a scientific defect).

The result is honestly framed as a null, σ floors and Bonferroni arithmetic are
correct, the abstract matches the body, and there are no overclaims, arithmetic
errors, leftover audit tags, or duplicate phrases. The single substantive item
(M1) is the pre-flagged open title-count decision; recommend 783,820 (or
791,635) as the headline anchor with 56,981 named as the primary void subsample.
