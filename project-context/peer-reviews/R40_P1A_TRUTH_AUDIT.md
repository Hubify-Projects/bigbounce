# R40 P1A Truth Audit — Einstein-Cartan-Holst chirality no-go (v1A.0.77)

**Auditor**: Opus truth-audit + synthesis lead
**Source**: `arxiv/paper1a_ech_nogo.tex` (3202 lines), `arxiv/paper1a_ech_nogo.pdf` md5=f1eab008, 29pp
**Inputs**: R40 OpenAI (gpt-5), Gemini-2.5-pro, Grok-4.3, Perplexity (FAILED — 100KB cap, zero findings), + Claude Opus leg = ACCEPT
**Protocol**: peer-review-truth-audit (reviewers over-call on stale/mislabeled artifacts; this paper has a documented Pontryagin/pair-exchange false-positive history — verified carefully)

---

## Merged verdict: **MAJOR REVISIONS → reduces to 3 trivial cosmetic closures**

Grok returned REJECT; OpenAI + Gemini returned MAJOR REVISIONS. After grounding every finding against the .tex, the substantive "fatal" claims are STALE or MISLABELED (already closed in prior EXT rounds, or reviewer math error). Only 3 trivial editorial items survive as VERIFIED-OPEN — all PRD-style cosmetics, none scientific.

---

## Per-finding audit

### Gemini-E1 — "Mathematical error: ε^{μνρσ}R_{μνρσ} is the Pontryagin density, not identically zero"
**Verdict: MISLABELED (reviewer math error).** This is the documented false-positive class. Gemini conflates the **single-curvature** Holst dual ε^{μνρσ}R_{μνρσ} with the **two-curvature** Pontryagin density ε^{μνρσ}R_{μν}{}^{αβ}R_{ρσαβ} ∝ R∧R̃. On a torsion-free Levi-Civita connection the first (algebraic) Bianchi identity R_{μ[νρσ]}=0 contracted with totally-antisymmetric ε **does** vanish pointwise — standard, correct. The paper explicitly distinguishes the two objects (tex 738-753, 2391-2393, 2451-2458) and reserves "Pontryagin" for the two-curvature invariant. Claude leg independently verified "Bianchi-vs-Pontryagin consistent." Paper math is correct; no change.

### Grok-M1 — "transparency proof only valid after dynamical torsion integrated out"
**Verdict: OPINION / scoped (not a defect).** The paper's claim is explicitly for canonical scalar matter where T=0 by the algebraic torsion constraint (no fermion bilinear source); it does not advertise the result for dynamical-fermion torsion. Title/abstract already scope to "scalar matter." Tex 2375-2401, 752. No closure.

### OpenAI-E4 / Gemini-E2 / Grok-E4 — companion-paper reliance ("in preparation" [2,6,23,46])
**Verdict: OUT-OF-SCOPE (program structure).** This is a 6-paper concurrent program (P1A/P1B/P2/P3/P4/P5); companions are posted concurrently, not vaporware. Paper already labels every such number "in preparation / illustrative / no claim made here." Recurring known item, not a R40 regression. Not a closure for this round.

### OpenAI-M8 / Grok-M2 — "13 logically-independent barriers overstated / B8 not subsumed"
**Verdict: STALE (already closed, EXT M8 wave).** Paper already reads "13 logically-independent barriers; 14 historical catalog entries, of which B8 is subsumed by B14" at every site (tex 727-728, 756-757, 821-822, 2196-2201). The softening these reviewers demand is already in the PDF. The GRO-M2 STALE note is recorded in the .tex changelog (tex 595-598).

### Grok-E1/E2/E3 — "abstract claims stronger than body (closure / f_NL / β)"
**Verdict: STALE.** Abstract already says "channel-level amplitude closure" (not operator-basis), and explicitly states f_NL and β are "**not** predictions of ECH itself" / "benchmark consistency point" with the not-directly-comparable σ caveat inline (tex 756-794). Reviewer read an older framing.

### OpenAI-E6 — "Eq.(14) dimensional inconsistency (1/M_Pl prefactor)"
**Verdict: STALE.** The Nieh-Yan one-loop operator dimensions were closed in EXT11/EXT13 (tex changelog 66, 77). ϑ_NY dimensionful convention is stated locally. OOM-unaffected per OpenAI's own arithmetic-check section ("the text's ∼10^-60 statement is correct," line 130). No regression.

### OpenAI-M6 / E7 — "two ρ_Λ normalizations / CC hierarchy exponent 10^121–123"
**Verdict: OPINION (harmonization request, OOM-invariant).** Both normalizations [(2.3 meV)^4 and (10^-3 eV)^4] give the same ~69-order conclusion; OpenAI's own check confirms "~1.4×10^-70 vs 4×10^-69 numerically consistent." Cosmetic harmonization, not an error. Claude leg verified "~69 orders correct."

### Arithmetic regression sweep (sign-error / OOM watch)
**All CLEAN.** OpenAI's independent recompute matches paper at every site: NJL ~4e-69, one-loop ~10^-60, β Planck-vs-ACT 1.06σ, ρ_θ≈5.7ρ_Λ, Ξ~10^-123, rotation (ω/H)^2~1.2×10^-21, ρ_crit(γ) scaling. No sign error, no OOM regression. Matches Claude leg (γ spread 0.0365≈0.037, e-folds 92−60=32 at 4 sites). **No pair-exchange false positive present.**

### Perplexity
**Verdict: N/A.** Reviewer call FAILED (400, content >100KB). Zero findings. Citation forensics covered by Claude leg (ShapiroTeixeira2014, Cai:2009fn f_NL=−35/8, Minami2020/Eskilt2022 all real in .bbl, no fabrication).

### Grok-N1 — PACS 95.36.+x (dark energy) misleading
**Verdict: OPINION.** Paper is *about* DE routes; code is defensible. Optional. Not blocking.

---

## VERIFIED-OPEN (the only real closures — 3 trivial cosmetics)

| ID | Source | File:line | Issue | Edit |
|----|--------|-----------|-------|------|
| V1 | OpenAI-E1 | `arxiv/paper1a_ech_nogo.tex:1890-1894` | Version-history prose in body ("Earlier drafts displayed… prompted a dimensional-mismatch flag in external review; the present footnote fixes that gap") | Delete the sentence; keep only the authoritative convention statement ("…no two operators are in play. All indices are fully contracted…") |
| V2 | OpenAI-E2 | `arxiv/paper1a_ech_nogo.tex:2462-2468` | Version-history footnote ("An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction…") | Delete the footnote; the Bianchi-vs-Pontryagin distinction is already stated positively in the body (tex 2451-2458) and needs no version narrative |
| V3 | Grok-E5 / Gemini-T1 | `arxiv/paper1a_ech_nogo.tex:49` (`\paperTimestamp`) + `:700` (`\date`) | Future date "June 13, 2026" (today 2026-06-18) reads as a future-dated submission | Bump `\paperTimestamp` to actual submission date via `/bigbounce-version-bump` |

Plus the 3 trivial overfull hboxes (max 13.1pt) noted by the Claude leg — handle in the same recompile via `/latex-audit`.

---

## Closure plan
Single cosmetic-cleanup bundle: strip V1+V2 version-history prose, restamp date (V3), recompile, `/latex-audit` the 3 hboxes, mirror PDF, add R40 `/reviews` timeline entry. No scientific change. After bundle, P1A is arXiv-clean: all "MAJOR/REJECT" verdicts traced to STALE framing or MISLABELED reviewer math.
