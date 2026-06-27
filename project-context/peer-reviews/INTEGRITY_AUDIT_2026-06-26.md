# Independent Integrity Audit — Big Bounce Review Loop

**Date:** 2026-06-26
**Auditor:** Independent integrity audit (Opus director + 5 adversarial per-paper verification lanes)
**Question Houston posed:** Is the loop's convergence REAL, or is it ENGINEERED — gaming prompts toward ACCEPT/MINOR and/or dismissing real reviewer findings as "false positives" to manufacture a clean exit?
**Method:** (1) read both review prompts line-by-line for verdict-steering; (2) independently re-verified ~19 of the most consequential DISMISSED high-severity findings against the actual `.tex` source; (3) rendered a GENUINE-vs-ENGINEERED verdict.

---

## PART 1 — PROMPT AUDIT

### INT prompt — `tools/v3_native_pdf_review.py` (`REVIEW_PROMPT_TEMPLATE` + personas + `SELF_CRITIQUE_TEMPLATE`)

**Verdict: RIGOROUS. No verdict-severity steering. This is the harsh leg.**

Load-bearing rigor lines:
- L61–62: *"This is one of the most rigorous physics journals in the world. The acceptance bar is HIGH. Reject anything that doesn't meet PRD standards."*
- L74: *"Write a complete referee report. NO cap on findings — list everything you find."*
- L85: *"Do NOT soften findings. Do NOT praise things that are merely adequate."*
- Multiple hard **ESSENTIAL** triggers (L88–89 sigma-comparability, L105–109 abstract-drift, L116–119 uncomputed-claim → MAJOR, L120–123 standalone-reader test).
- A full **pass-2 self-critique** (L137–194) that forces each reviewer to re-attack the paper for missed arithmetic/dimensional/abstract-faithfulness issues.

The only "do not flag" content is the `[REVIEWER METADATA … DO NOT FLAG AS ARTIFACTS]` block (L55–58, L66–68) — this is **legitimate false-positive prevention** (stops reviewers flagging the round-label scaffolding that isn't in the paper), not severity steering. There is **no** "default to MINOR," no "style → ACCEPT," no high bar gating MAJOR. CLEAN.

### EXT prompt — `site/src/components/ExternalReviewPanel.tsx` (`prompt[]`, L27–61), as scraped by `/external-review-browser-loop`

**Verdict: MOSTLY fair, but contains REAL verdict-severity steering that the INT prompt does not — an asymmetry that favors lenient EXT verdicts.**

LEGITIMATE false-positive calibration (the `CALIBRATION` block, L48–53) — keep:
- June-2026 dating / arXiv `25xx`–`26xx` validity (L49)
- deliberate correction/transparency notes (L50)
- companion-paper "posted concurrently" placeholders (L51)
- labeled conservatism/ansatz/heuristic allowances (L52)
- PDF-extraction-artifact caution before flagging "garbled math" (L53)

These are exactly the non-issues the loop should not burn referee effort on. Fine.

ILLEGITIMATE / borderline severity steering (the `HONEST VERDICT CALIBRATION` block, L55–60):
- **L58:** *"If the remaining items are style preferences (label choices, abstract emphasis, paragraph ordering), future-work pointers, or submission-day actions … MINOR REVISIONS or ACCEPT is the appropriate verdict."* — pre-labels a whole class as MINOR/ACCEPT.
- **L59:** *"Catalog-class and methodology papers are extensive by nature and should NOT default to MAJOR REVISIONS for that reason alone. Default to MAJOR only when a load-bearing claim is unsupported, a critical control is missing, or the paper cannot be reproduced from its committed artifacts."* — sets a **high three-condition bar for MAJOR** and instructs the referee to default away from it.

Individually each line is defensible journal guidance (a real MNRAS referee shouldn't dock length alone). But **the INT prompt carries no equivalent leniency language**, so the EXT leg — which the loop treats as the *convergence gate* — runs a structurally more lenient bar.

**Compounding structural concern** (`external-review-browser-loop/SKILL.md` L232): unattended EXT sweeps deliberately use **FAST** model tiers (ChatGPT Instant/High, Grok Expert, Gemini regular), explicitly because *"the browser EXT tier is CONFIRMATION,"* and *"The convergence signal is '0 external MAJOR.'"* The SKILL itself states (L10–12) the deep web tiers *"historically catch findings the internal rounds miss"* — yet those deep tiers are reserved for periodic supervised passes. So the gate that declares convergence is run at **both lower model sensitivity and a more lenient prompt** than the INT leg. The INT leg remains the genuine deep review, which mitigates this — but it is a real bias vector.

---

## PART 2 — RE-VERIFICATION OF DISMISSED FINDINGS (the core test)

I selected the most consequential dismissals (vendor REJECT/MAJOR/ESSENTIAL marked FALSIFIED/STALE/OPINION/OUT-OF-SCOPE) and independently checked each against source `.tex`. P1A by me; P1B/P2/P3/P4/P5 by adversarial Sonnet lanes instructed to hunt for "audit claims caveat at line X but line X doesn't contain it."

### P1A (verified directly)
| Vendor finding | Sev | Audit verdict | My check | Verdict |
|---|---|---|---|---|
| OpenAI E4: coefficient `γ²/(γ²+1)` should be `1/(1+γ²)` | ESSENTIAL | FALSIFIED | L1140 `eq:4fermi` confirms `γ²/(γ²+1)`; γ→∞ EC limit (L1688–1696, `γ²/(γ²+1)∈(0,1)`, recovers pure-Einstein–Cartan) makes the paper's factor the only internally-consistent one. OpenAI's would →0 and destroy the EC limit. | **AGREE** |
| Grok E2/Gemini E1/OpenAI E1-E3: self-containment, "in preparation" companion load-bearing | ESSENTIAL | STALE / HOUSTON-DECISION | Abstract L982–994 verbatim: *"none of these companion-imported numerical values is used in the channel-level closure proof … the structural closure rests on the dimensional / operator-counting / perturbation-transparency arguments alone."* Disclosure is real and prominent. | **AGREE** (disclosed standalone-weakness, not a text defect; genuinely a submit-companions-together decision) |
| Gemini E3/OpenAI M3,M10: 3.6σ/2.9σ not comparable | ESSENTIAL/MAJOR | OPINION | L783–785 verbatim: *"arise from different null procedures and are not directly comparable."* | **AGREE** |

### P1B (lane a7ad02b9)
- Gemini M1 "Ω_pix 47.21 wrong → 41.8": recomputed 4π/(12·512²) = **47.21 arcmin²** ✓ paper correct, Gemini's own arithmetic error. **AGREE**
- OpenAI E1 "LiteBIRD √(0.03²+0.094²) misprinted": source L2650 `\sqrt{0.03^2+0.094^2}` correctly typeset (extraction dropped `^2`). **AGREE**
- Grok E3 "σ statements lack 'not directly comparable'": abstract L1115–1116 carries it verbatim, twice. **AGREE**
- OpenAI E3 "SN-overlap control runs missing (20% shared SNe)": **UNCERTAIN** — real gap; paper itself says robustness *"has not been demonstrated quantitatively in the present manuscript"* (L1611–1612) and defers control chains to a follow-up note (L1614–1619). Disclosed in 3 places, NOT buried, but the reviewer's concern is substantively correct and could reopen if the follow-up never posts.

### P2 (lane a9bdea43)
- Gemini E1 "18/25 ≠ 6/5 derivation flawed": L1149 `(5/3)³(3/5)⁴·2 = 6/5` ✓ correct; Gemini used `(5/3)²`. **AGREE** (audit cited wrong line L1125 but math sound)
- Gemini m1 "Eq 2 sign +35/8": L637 `f_NL^local = −35/8 = −4.375` unambiguously negative. **AGREE**
- Grok/Gemini M1 "assumption-(d) weakest-link / ε-quadrature unjustified": L736 + abstract L641 carry both caveats verbatim. **AGREE**
- OpenAI E9/M8 "σ=0.7 borrowed, not independently validated": **UNCERTAIN** — disclosed at L639 (*"sensitivity recast rather than an independent forecast"*) but the entire 5.2–5.5σ headline rests on one external number (Heinrich 2023). Disclosure present but arguably warrants MINOR, not OPINION.

### P3 (lane aaf3b3d4)
- OpenAI E2/Gemini M1 "Planck top-200 train/test overlap": L892 fully discloses the 152/48 split + held-out over-representation (p≈4×10⁻⁴); direction is the correct memorization diagnostic. **AGREE**
- OpenAI E3/Gemini M2 "eROSITA score axis irreproducible": L577 + L872 disclose non-reproducibility across 16 rescalings in abstract+body+table. **AGREE**
- Grok E1/E2/M3 "NANOGrav 'decisive' / 9.4% overstated": all three sites hedged (L581 abstract, §nanograv, L1152 conclusion). **AGREE**
- OpenAI E4/M3 "'catalog-grade' tier includes exploratory eROSITA/Gaia": **UNCERTAIN** — abstract headlines 269,317 "catalog-grade" (L577); exploratory-flag carve-out only at L1177. Real headline-vs-body branding gap; should be MINOR, not OPINION.

### P4 (lane afb16424)
- Grok E5 (REJECT) "abstract +0.41σ vs body −9.47σ inconsistent": different statistics (L605 HC dipole-z vs L587 Catalog-C monopole table row). **AGREE**
- OpenAI E6 "apodized C1 2.348e-5 vs 2.474e-5 5% drift": two distinct estimators, L633 caption says *"should not be numerically equated."* **AGREE**
- OpenAI E2 "two canonical ℓ=1 σ values +3.64/+7.93": same field, 500-MC vs 10⁴-permutation; both labeled systematics-diagnostics, non-cosmological (L795). **AGREE**
- OpenAI M8/Gemini M3 "abstract z=0.70 vs body z=0.58 label-shuffle": **UNCERTAIN** — abstract (L348) headlines the larger secondary-implementation value 0.70; primary (same generator) is 0.58 (L605). Reporting-emphasis smell; MINOR more honest than OPINION. No conclusion flips (both null).

### P5 (lane a44c9584)
- Grok REJECT "central claim on n=428 void bin": n=428 is explicitly secondary; controlling constraint is DESIVAST n=56,981 (L444, L517–523). Grok inverted primary/secondary. **AGREE**
- Gemini M1 "V2-REVOLVER Δ=−0.0037 sign error": L2359–2368 sign convention defined; arithmetic correct. **AGREE**
- Gemini M3 "toy-EFT dimensionally inconsistent": L3476–3522 labels it order-of-magnitude schematic, not covariant operator. **AGREE**
- OpenAI M1 "Bonferroni threshold 4.05 wrong": **UNCERTAIN / mild real error** — correct value for K=1054, two-sided α=0.05 is ≈4.07; paper prints 4.05 (slightly liberal). The audit's "convention-dependent / OPINION" framing is inaccurate — the formula is unambiguous. No verdict flips (all |σ| ≪ 4), but it is a computable factual discrepancy that should have been a MINOR fix.

### Tally (≈19 consequential dismissals re-verified)
- **AGREE — dismissal correct: ~14** (every FALSIFIED arithmetic/extraction/sign/coefficient call held up rock-solid against source; the harsh vendor REJECT/ESSENTIAL items were genuine vendor false positives — own-arithmetic errors, extraction artifacts, primary/secondary inversions, misremembered canonical factors).
- **DISAGREE — real issue buried: 0.**
- **UNCERTAIN / mild-real-issue: 5** — all the SAME character: a genuinely-disclosed-but-imperfect reporting item (abstract headlines the more favorable of two null values; borrows an external σ; marginally-off Bonferroni threshold; deferred control chains) labeled **OPINION/STALE** when **MINOR** would be more honest. **None alters any scientific conclusion.**

**Zero fabricated dismissal justifications.** Every "the caveat is already at line X" claim was checked and the caveat was genuinely present (a couple of trivial line-number slips, substance intact). The lanes specifically hunted for fabricated-citation dismissals and found none.

**Affirmative counter-evidence the loop still surfaces real defects:** `EXT22_CONSOLIDATION.md` NEW-VERIFIED a genuine MINOR — P1A Discussion §XII.B (L2698–2701) asserts a closure mechanism (*"repulsive … subcritical"*) that appears nowhere in the body (which closes Route 1 by Planck suppression). The loop found and verified this rather than dismissing it. A pure rubber-stamp would not have.

---

## PART 3 — VERDICT

**Convergence is GENUINE on substance, with a MILD, REAL self-favoring bias at the OPINION-vs-MINOR boundary.**

The hard claim — "0 surviving BLOCKER / MAJOR / ESSENTIAL" — holds up. Under independent adversarial scrutiny, **not one** dismissed high-severity finding was a real defect swept under the rug; the dismissed REJECT/ESSENTIAL/MAJOR items were authentic vendor false positives (extraction artifacts, the vendor's own arithmetic/sign errors, misremembered canonical coefficients, primary/secondary inversions), and every "already-disclosed-at-line-X" justification was truthful. The INT leg's prompt is genuinely harsh and uncapped. That is the signature of real convergence, not engineered convergence.

The qualification: there is a **consistent, low-grade tendency to round borderline reporting-emphasis items down to OPINION (no action) instead of MINOR (fix it)**, seen in 5/19 sampled dismissals (P1B σ-overlap, P2 σ=0.7 provenance, P3 catalog-grade branding, P4 abstract 0.70-vs-0.58, P5 Bonferroni 4.05). This is not "burying real issues" — none change a conclusion — but it makes the *"0 MINOR"* cleanliness slightly better than reality. And it is **structurally encoded**: the EXT prompt's `HONEST VERDICT CALIBRATION` (L58–59) explicitly steers exactly this class toward MINOR/ACCEPT, the EXT gate runs fast tiers as "confirmation," and the truth-audit then labels the same class OPINION. Prompt steering + gate-leniency + audit-downgrade point the same direction. The effect is real but bounded to the most subjective category (how prominently must a *disclosed* limitation be foregrounded?).

**Confidence:**
- That convergence is NOT grossly engineered / no blockers buried: **HIGH (~90%).**
- That a mild OPINION-vs-MINOR self-favoring bias exists: **MODERATE-HIGH (~75%).**

**Strongest evidence each way:**
- FOR genuine: every dismissed vendor ESSENTIAL/REJECT independently re-derived as a true false positive (e.g. P1A `γ²/(γ²+1)` — the paper's coefficient is the only one consistent with its own γ→∞ Einstein–Cartan limit; P1B Ω_pix 47.21 recomputes exactly), AND the loop NEW-VERIFIED a real P1A Discussion inconsistency in the same round.
- FOR mild engineering: the EXT convergence-gate prompt uniquely contains *"Default to MAJOR only when …"* + *"abstract emphasis … MINOR REVISIONS or ACCEPT is the appropriate verdict"* (L58–59) with no INT counterpart, and 5/19 dismissals matched that steered class — a coherent, reproducible lenience vector on reporting-emphasis items.

---

## RECOMMENDED FIXES

1. **De-bias the EXT prompt (`ExternalReviewPanel.tsx` L58–59).** Strike the "MINOR REVISIONS or ACCEPT is the appropriate verdict" clause and the "Default to MAJOR only when…" three-condition gate. Replace with severity-neutral language: *"Assign severity on the merits. A disclosed limitation is still a MINOR if a referee would expect it foregrounded alongside the headline claim; reserve MAJOR for unsupported load-bearing claims, missing critical controls, or non-reproducibility."* Keep the entire `CALIBRATION` block (L48–53) — that part is legitimate. Add a `kind:"skill-improvement"` timeline entry per the standing CLAUDE.md rule.
2. **Symmetry check:** the INT and EXT bars should match. INT already says "do not soften"; EXT should too. Remove the leniency asymmetry rather than adding leniency to INT.
3. **Re-open 5 items as MINOR (not OPINION)** in SSOT for an honest "0 MINOR" claim — none are blockers, all are ~10-minute abstract/threshold edits:
   - P5: print Bonferroni threshold **4.07** (K=1054, two-sided α=0.05), not 4.05.
   - P4: abstract should headline the **primary** label-shuffle null (same generator, z=0.58) and note z=0.70 as the independent cross-check — not the reverse.
   - P3: add the "two components carry exploratory validity flags" carve-out to the abstract's 269,317 "catalog-grade" headline (currently only at L1177).
   - P2: foreground the "sensitivity recast, σ=0.7 imported from Heinrich 2023" provenance at each 5.2–5.5σ headline, not once.
   - P1B: state plainly in the abstract that the SN-overlap robustness is *not yet quantitatively demonstrated* (it's at L1611 in body; promote it), or compute the deferred control chains.
4. **Periodically run one DEEP-tier EXT sweep** (not fast-tier) before declaring final convergence, since the SKILL concedes deep tiers catch what internal rounds miss; treat fast-tier "0 MAJOR" as necessary-not-sufficient.

**Bottom line for Houston:** the loop is not lying to you about the big stuff — there are genuinely no buried blockers or majors, and the "false positive" dismissals are real false positives. The one honest correction is that a handful of legitimate MINORs got rounded to "opinion/no-action," partly because the EXT prompt and gate are tuned slightly lenient. Fix the four prompt lines, re-open the five MINORs, and the convergence is clean rather than merely substantively-clean.
