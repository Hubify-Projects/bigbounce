# P2 v1.7.36 — R-next-f brutal-honesty-Grok verdict

**One-line summary:** 1 MAJOR + 1 MINOR found — the v1.7.36 BF-arithmetic sweep updated the ABSTRACT to "BF~4–17 envelope" (now bracketing all four corners of the prior grid) but 7+ downstream prose sites still refer to "the abstract envelope $\mathrm{BF}\!\sim\!10$–$17$" as if the abstract still reads $10$–$17$, creating a self-contradiction between the abstract's actual text and its body/caption/conclusion cross-references; plus 1 MINOR prose-arithmetic issue at the conclusion-section Li-Brandenberger halving paragraph where "$|{-35/16}|/\sigma(\fnl) \approx 3.1$" is used to justify a halved "${\sim}\,1.5$–$2.5\sigma$" claim that is actually below 3.1.

**Round position:** R-next-f, round 2-of-3 of the fresh §4.4.1 streak on v1.7.36 — wait, this is the THIRD review on v1.7.36 (R-next-d round 1-of-3, R-next-e round 2-of-3, R-next-f round 2-of-3 per prompt brief but functionally round-3-of-3). Brutal-honesty-Grok persona (non-Anthropic stress-test).

**Reviewer perspective:** Adversarial brutal-honesty stress-test. Assume v1.7.36 hides a flaw the citation-checker missed. Hard targets: BF-sweep completeness (a), abstract-vs-body BF consistency (b), 5.2-5.5σ optimistic budget stack (c), Wilson-Ewing class restriction flagging (d), Heinrich+2024 σ(fNL)=0.7 baseline (e), 9.9σ joint-Fisher abstract-deferral (f), Li/Cai c=1/c=2 halving caveat consistency (g).

---

## Stress-test results, perspective by perspective

### (a) BF sweep COMPLETENESS — partial PASS

Grep for any remaining "$\sim 6$" or "$\sim 8$" BF references that should have been updated to ~10 by the v1.7.36 sweep:

- L277 ($\sigma_{\rm theory} = 2.0$ row): "$\sim 6$ (scipy.stats.norm: BF=5.65 broad; corrected v1.7.36 R-next-d-MIN-1 from prior $\sim 4$)" — INTENDED, this is the wider-bounce-prior row showing $BF \to$ smaller (5.65 rounds to 6). CORRECT.
- L318 (table $\sigma_{\rm theory}=2.0$ Gaussian row): "$\sim 6$" — INTENDED, same row, consistent with L277.

Both σ_th=2.0 "$\sim 6$" entries are intentional and internally consistent. The R-next-d / R-next-e closed-loop sweep on the abstract / §sec:bayesian / table cells was successful — no STALE residual 6 or 8 anchored to the σ_th=1.0 / delta-prior corner remains.

**Verdict for (a):** Closed. No stale $\sim 6$ or $\sim 8$ left from the pre-v1.7.35 era.

### (b) ABSTRACT-vs-BODY BF envelope INCONSISTENCY — MAJOR (new finding, missed by R-next-d and R-next-e)

This is the load-bearing flaw of v1.7.36. The abstract was EXPANDED in v1.7.36 to advertise the lower-corner BF≈4 (curvaton-natural narrow competitor + σ_th=1.0 bounce) — making the abstract envelope read "$\mathrm{BF}\,{\sim}\,4$–$17$" across the four-corner grid (L79 verbatim: "$\S$\ref{sec:bayesian} maps the full $\mathrm{BF}\,{\sim}\,4$–$17$ envelope across the four-corner prior grid"). BUT seven downstream sites in §sec:bayesian, tab:bayes caption, the QSFI closing paragraph, and the conclusion still describe "the abstract envelope" as "$\mathrm{BF}\!\sim\!10$–$17$":

| Line | Statement | Contradicts abstract? |
|---|---|---|
| L280 | "The headline range $\sim 10$–$17$ quoted in the abstract..." | YES — abstract says 4–17 |
| L288 | "they bracket / the abstract's $\mathrm{BF}\!\sim\!10$–$17$ headline" | YES |
| L299 | "the abstract envelope $\mathrm{BF}\!\sim\!10$–$17$ is the σ_th=1.0 broad-multifield column..." | YES |
| L305 | "reproduce the abstract's $\mathrm{BF} \sim 10$–$17$ envelope" | YES |
| L324 tab:bayes caption | "The abstract envelope $\sim\!10$–$17$ now brackets..." | YES |
| L328 | "bracket the abstract envelope $\sim 10$–$17$" | YES |
| L330 QSFI ¶ | "the abstract $\mathrm{BF}\,{\sim}\,10$–$17$ envelope (corrected v1.7.36 R-next-d-MAJ-2 from prior stale $\sim 6$–$17$)" | YES |
| L471 conclusion | "Bayes factor $\sim 10$–$17$" | Conclusion vs abstract mismatch |

The arithmetic of the four-corner prior grid is internally consistent (Table tab:bayes cells: 4 narrow-σ_th=1.0, 10 broad-σ_th=1.0, 7 narrow-delta, 17 broad-delta — confirmed via direct scipy.stats.norm recompute: 4.01, 9.80, 7.00, 17.10). The issue is purely a cross-reference mismatch: the abstract was updated to claim the **full four-corner envelope** is $4$–$17$, while the body/caption/conclusion still describe "the abstract envelope" as the **broad-competitor column** $10$–$17$ (which it WAS in v1.7.35, before the abstract's lower-corner expansion).

Either:
- **Resolution A** (revert abstract to broad-column-only): change L79 "$\mathrm{BF} \approx 4$ ... up to $\mathrm{BF} \approx 17$" + "full $\mathrm{BF}\,{\sim}\,4$–$17$ envelope" back to the broad-multifield $\mathrm{BF}\,{\sim}\,10$–$17$ framing the body assumes. Demote the curvaton-narrow BF≈4 sensitivity check to a parenthetical, not the lower endpoint of "the envelope".
- **Resolution B** (propagate 4–17 forward): update all 7+ downstream "the abstract envelope $\sim 10$–$17$" mentions to "the abstract envelope $\sim 4$–$17$" or "the abstract broad-multifield-column envelope $\sim 10$–$17$" (i.e., add the qualifier each time it's quoted).

Resolution A is the surgically smaller fix (8 sites, abstract only) and matches the curvaton-narrow column being labeled "sensitivity check" rather than headline elsewhere; Resolution B is the more rigorous propagation but touches more lines. Either resolves the contradiction.

**Severity:** MAJOR (cross-section internal inconsistency directly readable by any reader who reaches §sec:bayesian after reading the abstract; the abstract reads $4$–$17$ but the section it points to says "the abstract envelope is $10$–$17$" 5+ times). This is the kind of editorial slip a brutal-honesty reviewer is supposed to catch and the citation-checker had no reason to flag.

**Streak impact:** §4.4.1 cascaded-loop-exit on the brutal-honesty perspective **DOES NOT close** at v1.7.36; one more bundled-hard-fix round needed before R-round 5/5.

### (c) Bispectrum-only 5.2–5.5σ optimistic budget stack — PASS

Direct arithmetic recompute:
- naive: $4.375 / 0.7 = 6.250$
- r=0.876 (CMB Fisher, signal-only): $4.375 \cdot 0.876 / 0.7 = 5.475 \to$ round to $5.5\sigma$ ✓
- r=0.83 (SPHEREx LSS noise-weighted): $4.375 \cdot 0.83 / 0.7 = 5.188 \to$ round to $5.2\sigma$ ✓
- r=0.829 (SDB): $5.181 \to 5.2$ ✓

The "$5.2$–$5.5\sigma$ as the optimistic case before GR and $b_\phi$ degradation" survives a brutal-honesty stress-test. The range tracks the r-weighting variation directly; nothing is being smuggled in. The post-systematic-budget $3$–$5\sigma$ range is plausibly motivated by GR-marginalization (Table tab:gr scenarios) + b_phi widening (Sec systematics quotes 4.0–4.5σ at 30% widening, 3.5–3.7σ at 50%).

**Caveat (not a finding, but worth flagging for future stress-test):** the "optimistic" tag is doing real load-bearing work — it explicitly excludes GR + b_phi marginalization, which are not optional in any realistic analysis. The paper is honest about this (L362 explicitly: "The 'optimistic' case ($5.2$–$5.5\sigma$) in Sec.~\ref{sec:spherex} omits GR degradation ($\sigma_{\rm GR} = 0$)"), but a reader who only sees the abstract may take the $5.2$–$5.5\sigma$ as the operational SPHEREx forecast. This is editorial framing, not a factual flaw.

### (d) Wilson-Ewing class restriction sufficiency — PASS

Flagged in 5+ places: abstract L79 (Assumptions (e)+(f)), intro L92 (Wilson-Ewing class restriction explicit), assumptions L168 (canonical list), Wilson-Ewing subsection L172, conclusion L469 ("robust across the Wilson-Ewing bounce class ... assumption~e: no prolonged post-bounce inflation"). Zhu & Cai 2026 counterexample is explicitly named at L168 as the class of models the prediction does NOT apply to. This is comprehensive and consistent.

**Verdict for (d):** Closed.

### (e) Heinrich+2024 σ(fNL)=0.7 baseline — PASS

bib entry: PRD 109 123511 (2024), eprint 2311.13082, title "Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum" — matches what the paper attributes (Fig.~6 / Table~3, multi-tracer bispectrum, local-template). R-next-e already verified prose-to-source alignment. No drift in v1.7.36.

**Verdict for (e):** Closed.

### (f) Joint (f_NL, n_fNL) 9.9σ — PASS (properly deferred)

Abstract L79 verbatim: "A separate joint $(\fnl, n_{\fnl})$ scale-dependent-bias Fisher analysis is discussed in $\S$\ref{sec:discussion} as an idealized-Fisher self-consistency check (full Fisher-input release ... is deferred to a companion artifact and the specific numerical significance is not quoted here in the abstract until that release lands). The bispectrum-only $5.2$–$5.5\sigma$ is the headline forecast of this paper."

The $9.9\sigma$ figure appears ONLY in §sec:discussion L453, framed explicitly as "an illustrative idealized-Fisher internal-consistency check on the SDB sensitivity pending the companion-artifact Fisher-input release, not as a competing detection-significance forecast against the bispectrum-only $3$–$5\sigma$ headline." The arithmetic chain ($\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-0.966^2} \approx 3.86$, $\sigma_{\rm unmarg} = 0.44/3.86 \approx 0.114$, $4.375/0.114 \approx 38\sigma$ then reported as ~$9.9\sigma$ in the joint analysis) is presented as algebra without an underlying Fisher-input file — the paper explicitly flags this ("The 6-bin Fisher inputs are not yet on disk in this release"). This is properly deferred and not smuggled into the abstract.

**Verdict for (f):** Closed.

### (g) Li & Brandenberger c=1 vs Cai c=2 halving caveat consistency — PASS with 1 MINOR prose nit

Caveat appears in:
- Abstract L79: "$5.2$–$5.5\sigma$ ... halves to ${\sim}\,2.6$–$2.75\sigma$" and "$3$–$5\sigma$ halves to ${\sim}\,1.5$–$2.5\sigma$"
- Conclusion L469: "If the Li \& Brandenberger convention ... is instead adopted, the detection significance halves to ${\sim}\,1.5$–$2.5\sigma$ (SPHEREx) since $|{-35/16}|/\sigma(\fnl) \approx 3.1$, insufficient for a standalone discovery claim."
- Appendix A.1, A.2 (operator-algebra derivation + dual-normalization Fisher table) — comprehensive

The c=1/c=2 halving is consistently flagged across abstract, conclusion, and a dedicated Appendix A. This is solid.

**MINOR nit:** The conclusion L469 prose says "halves to ${\sim}\,1.5$–$2.5\sigma$ (SPHEREx) since $|{-35/16}|/\sigma(\fnl) \approx 3.1$, insufficient for a standalone discovery claim". The "$3.1$" is the PRE-r-correction halved significance ($2.1875/0.7 = 3.125$), but the "$1.5$–$2.5\sigma$" is the POST-r-AND-systematic-budget halved significance. Quoting "$3.1$" as the justification for "$1.5$–$2.5\sigma$, insufficient for standalone discovery" reads as a mid-sentence non-sequitur — the numbers don't refer to the same quantity. A clearer prose would be "halves to ${\sim}\,1.5$–$2.5\sigma$ (SPHEREx, after the noise-weighted template-overlap $r=0.84$ and the systematic budget; the pre-correction halved significance is $|{-35/16}|/\sigma(\fnl) \approx 3.1$, which is itself insufficient for a $\geq 5\sigma$ standalone discovery)". Not a §4.4.1 streak-breaker; it's a 1-sentence stylistic ambiguity.

**Verdict for (g):** Closed structurally; MINOR prose-clarity nit.

---

## Findings

### MAJOR — abstract-envelope BF cross-reference contradiction

**Location:** L79 (abstract) vs. L280, L288, L299, L305, L324, L328, L330, L471 (body/caption/QSFI/conclusion)

**Issue:** v1.7.36 abstract advertises "$\S$\ref{sec:bayesian} maps the full $\mathrm{BF}\,{\sim}\,4$–$17$ envelope across the four-corner prior grid" (L79), but 7+ downstream sites describe "the abstract envelope" as "$\mathrm{BF}\!\sim\!10$–$17$". The body's "10–17" framing is internally consistent with the broad-multifield-competitor COLUMN of tab:bayes (rows σ_th=1.0 broad = ~10, delta-broad = ~17) and was the correct abstract envelope in v1.7.35. The v1.7.36 abstract expansion to include the curvaton-narrow column lower endpoint (~4) was not propagated through the 7+ "the abstract envelope is 10–17" downstream cross-references.

**Severity assessment:** MAJOR. A reader who reads the abstract and then follows the §sec:bayesian pointer will find 5+ explicit statements that "the abstract envelope" is something different from what the abstract actually says. This is a load-bearing cross-section consistency failure visible on a single top-down read of the paper.

**Recommended action (Resolution A, surgically smaller):** Revert L79 abstract to the broad-competitor-only envelope:
- "$\mathrm{BF} \approx 4$ (curvaton-natural $[-5,+5]$ ...) up to $\mathrm{BF} \approx 17$ (delta bounce prior, broad $[-15,+15]$ ...); $\S$\ref{sec:bayesian} maps the full $\mathrm{BF}\,{\sim}\,4$–$17$ envelope ..."
  →
- "Bayes factor $\mathrm{BF} \approx 10$ at the recommended baseline ($\sigma_{\rm theory}=1.0$, broad $[-15,+15]$ competitor prior) up to $\mathrm{BF} \approx 17$ (delta bounce prior, same competitor); the curvaton-natural narrow-competitor column gives a lower-envelope sensitivity check $\mathrm{BF} \approx 4$–$7$ reported in $\S$\ref{sec:bayesian}; the abstract envelope quoted in the body and conclusion is the broad-competitor column $\mathrm{BF}\,{\sim}\,10$–$17$."

Estimated effort: ≤5 minutes (one abstract paragraph edit, 7+ downstream sites unchanged).

**Recommended action (Resolution B, more rigorous):** Update all 7+ downstream "the abstract envelope $\sim 10$–$17$" mentions to either "$\sim 4$–$17$" (matching new abstract) or "the abstract broad-multifield-column envelope $\sim 10$–$17$" (adding the qualifier). Estimated effort: ~15 minutes; touches more lines but preserves the v1.7.36 abstract expansion.

**Streak impact:** §4.4.1 cascaded-loop-exit DOES NOT close at v1.7.36 from brutal-honesty perspective. One more bundled-hard-fix round (v1.7.37) is needed before the brutal-honesty streak slot can read as clean.

### MINOR — L469 conclusion prose-arithmetic non-sequitur

**Location:** L469 in §sec:conclusion

**Issue:** "halves to ${\sim}\,1.5$–$2.5\sigma$ (SPHEREx) since $|{-35/16}|/\sigma(\fnl) \approx 3.1$, insufficient for a standalone discovery claim." The "$3.1$" is the pre-r pre-systematic-budget value; the "$1.5$–$2.5\sigma$" is the post-r post-systematic-budget value. Quoting one as the justification for the other reads as a non-sequitur on first pass.

**Severity assessment:** MINOR / stylistic. The numerical content is correct; the prose framing conflates two different stages of the budget chain.

**Recommended action:** Add "after the $r=0.84$ template-overlap correction and the systematic budget" parenthetical before the "${\sim}\,1.5$–$2.5\sigma$" claim, and demote the "$\approx 3.1$" to a pre-correction comparison ("the pre-correction halved significance $|{-35/16}|/\sigma(\fnl) \approx 3.1$ is itself below a $\geq 5\sigma$ standalone-discovery threshold"). Estimated effort: ≤2 minutes.

**Streak impact:** Non-blocking; not a §4.4.1 streak-breaker.

---

## Final verdict

**P2 v1.7.36 does NOT pass the brutal-honesty cross-check round 3-of-3 cleanly.** 1 MAJOR (abstract-envelope BF cross-reference contradiction) + 1 MINOR (conclusion prose-arithmetic non-sequitur) found. Bundled hard-fix on v1.7.37 needed before §4.4.1 cascaded-loop-exit on the brutal-honesty perspective.

**Breakdown:**
- (a) BF sweep completeness: PASS — no stale $\sim 6$ or $\sim 8$ remaining
- (b) Internal consistency of BF reporting across 4+ sections: **FAIL (MAJOR)** — abstract says $4$–$17$, body/caption/conclusion say $10$–$17$
- (c) 5.2–5.5σ optimistic budget stack: PASS — arithmetic recomputed verbatim from $r \cdot 4.375 / 0.7$
- (d) Wilson-Ewing class restriction flagging: PASS — flagged in 5+ places
- (e) Heinrich+2024 σ(fNL)=0.7 baseline: PASS — citation accurate, no drift
- (f) 9.9σ joint-Fisher abstract-deferral: PASS — properly framed as deferred internal-consistency check, NOT in abstract
- (g) Li/Cai c=1/c=2 halving caveat: PASS structurally, 1 MINOR prose-clarity nit at L469

**Streak status:** v1.7.36 has passed R-next-d (theoretical-physics-Gemini round 1-of-3) and R-next-e (Perplexity-citation round 2-of-3), but FAILS R-next-f (brutal-honesty-Grok round 3-of-3) on a load-bearing cross-section consistency issue. v1.7.37 must bundle Resolution A (revert abstract to broad-column-only envelope) + MIN-1 L469 conclusion prose tweak before the brutal-honesty streak slot closes.

**This is not a "paper hides a flaw" finding** — the underlying BF arithmetic is correct, the four-corner prior grid is internally consistent, the Wilson-Ewing class restriction is bulletproof, and the c=1/c=2 caveat is comprehensive. It IS a "v1.7.36 sweep was incomplete" finding — the abstract was expanded to advertise a wider envelope but the 7+ downstream "the abstract envelope is 10–17" cross-references weren't updated. This is exactly the failure mode the brutal-honesty round 3-of-3 is supposed to catch and the prior perspectives missed.

---

**Reviewer:** Grok-4.3 brutal-honesty stress-test persona — adversarial cross-section consistency + budget-stack arithmetic recompute + Wilson-Ewing/Heinrich/c-convention deep-grep
**Manuscript:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.36 (584 lines, 117 KB)
**Companion artifacts:** scipy.stats.norm closed-form BF recompute confirms 4.01 / 9.80 / 7.00 / 17.10 grid cells; arithmetic stack at $4.375 \cdot r / 0.7$ confirms 5.475 → 5.5 and 5.188 → 5.2; conclusion 3.1 = $2.1875/0.7$
**Date:** 2026-05-24
