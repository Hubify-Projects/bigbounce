# EXT18 Referee Report — P1A

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic leg — API leg failed on credit balance; this is the in-harness replacement read)
- **Paper:** P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"
- **Round:** EXT18
- **Version:** v1A.0.77
- **Pages:** 29
- **Date:** 2026-06-14
- **Input:** Full native PDF, all 29 pages read in two ranges (1–15, 16–29); every figure, table, and headline equation examined; σ values and hierarchy arithmetic independently recomputed.

---

## Overall assessment

This is a heavily hedged, self-aware negative-result methods paper. The authors have
clearly absorbed many prior review rounds: nearly every potentially-overclaimed statement
is now wrapped in an explicit "ansatz / not a derivation / channel-level not operator-level /
phenomenological" caveat. The central perturbation-transparency result (Sec. X) is a
genuine, clean, correctly-argued structural statement (Holst dual contraction
ε^{μνρσ}R_{μνρσ} vanishes by the first algebraic Bianchi identity at T=0, correctly
distinguished from the Pontryagin density). The arithmetic I spot-checked — β significances
(p1 abstract, p13, p25), the e-fold differentials, the Ξ ≈ 10^-123 = 10^-2 × 10^-121
decomposition, and M_Pl^4/ρ_obs ≈ 10^123 — is internally consistent. The paper is honest to
a fault; the hedging is so dense it borders on unreadable. My substantive findings are about
residual overclaim seams and one unsupported numeric, not about fabrication.

---

## Findings

### MAJOR

**M1 — The "2.6σ" lower bound on the f_NL forecast is asserted but never derived from the
paper's own numbers.**
*Sec. I (abstract), Table I (footnote b), Sec. VII, Sec. XIII; footnote 6 (p16).*
The headline range "2.6–5σ" for the SPHEREx matter-bounce f_NL test appears roughly eight
times. Footnote 6 derives the *upper* end cleanly: raw |f_NL|/σ = 4.375/0.7 = 6.25σ, degraded
to ~5–5.8σ optimistic with template overlap r≈0.84, and ~4.375σ at σ(f_NL)≈1.0 "realistic."
But the *2.6σ lower bound* requires σ(f_NL)≈1.68, which is never stated or justified anywhere.
The abstract itself footnotes that "the degraded-with-systematics sensitivity is σ(f_NL)≈1.0"
— and 4.375/1.0 = 4.375σ, not 2.6σ. So the lower edge of the load-bearing headline range is
unsupported by the paper's own arithmetic.
**Required fix:** Either state and justify the σ(f_NL)≈1.68 that yields 2.6σ in footnote 6 /
Table I footnote b, or correct the range to the actually-derived endpoints (≈4.4σ realistic
to ≈5.8σ optimistic). The forecast is explicitly deferred to Paper II (in prep) — that is
fine — but any σ range quoted in *this* paper must be reproducible from *this* paper.

**M2 — Load-bearing surviving-science narrative rests on three unposted "in preparation"
companion papers; a referee cannot verify the two surviving predictions.**
*Refs [2] (Paper II f_NL forecast), [6] (Paper I(b) MCMC), [46] (Paper III γ_PTA); Table I,
Table III, Fig. 1, Fig. 4, Fig. 6, Sec. XIII, Sec. XV.*
Both surviving "testable predictions" — f_NL = −35/8 and γ_PTA = 2.567±0.382 ("+1.13σ") —
are sourced to companion papers not yet on arXiv. The paper is admirably explicit that none
of these numbers feed the Sec. IV / Sec. IX closure proof (correct and important), but the
entire surviving-prediction story a reader is asked to care about cannot be checked from this
manuscript. For a standalone PRD submission this is a real refereeing obstacle.
**Required fix:** Either sharpen the gating further (mark every companion-derived number as
"forthcoming, not peer-reviewable in this submission") or ensure the companion arXiv IDs are
live at submission so the referee can follow them. As written a PRD referee would reasonably
hold pending the companions.

### MINOR

**m1 — CC-hierarchy magnitude wobbles between 10^120, 10^122, and 10^123 across text and
Fig. 5.**
*p9, Appendix B (p26), Ξ≲10^-123 throughout; Fig. 5 bottom panel labels ΛCDM "10^120" while
its caption says "10^122."* M_Pl^4/ρ_obs ≈ 7.9×10^122 (~10^123). All values sit within the
paper's stated OOM tolerance, but the inconsistent labeling reads as careless.
**Required fix:** Pick one convention, state why Fig. 5 uses 10^120 for ΛCDM while the text
uses 10^122/10^123 (cutoff-scale choice), in one sentence.

**m2 — N_tot ≈ 92 vs the independent ≈ 94 estimate: the ±2 is acknowledged once but the e^32
differential is then quoted as if 92 is exact.**
*p9, Sec. XII A, Sec. XIV D, Appendix B (p26); Fig. 1, Fig. 3.* The e-fold differential
N_tot − N_exit = 92 − 60 = 32 → e^32 ~ 10^14 is built on a number the paper itself says is
only ~2% determined.
**Required fix:** Carry the ±2 / "≈" through to the e^32 differential, or state once that the
differential conclusion is OOM-robust to the ±2.

**m3 — Internal-audit / revision-history residue leaks into body footnotes.**
*Sec. IV D footnote 5 ("apparent dimensional ambiguity flagged in external review"; "earlier
drafts displayed the θ-form... which (correctly) prompted a dimensional-mismatch flag in
external review; the present footnote fixes that gap"); Sec. X G ("An earlier version of this
manuscript misidentified the Holst dual contraction with the Pontryagin density. The
correction...").* A submitted manuscript should not narrate its own draft history or the
review process.
**Required fix:** State the correct dimensional convention and the correct
Holst-vs-Pontryagin distinction as standing facts; delete "earlier draft," "external review
flagged," "the present footnote fixes that gap."

**m4 — Title says "Closure of Four... Routes" but only three are amplitude-closed; R4 is a
naturalness objection.**
*Title vs abstract / Sec. IV D / Sec. XV.* The abstract corrects this within its first
paragraph (R4 "not closed by amplitude mismatch but by an explanatory-deficit objection"),
so this is MINOR, but the title alone over-reads.
**Required fix:** Qualify the title or ensure the R4 asymmetry is unmissable up front.

**m5 — Abstract is ~1.5 pages of dense single-paragraph prose; far over PRD length and buries
the lede under scope disclaimers.**
*Sec. I abstract.*
**Required fix:** Cut to standard PRD length (~200–250 words); move operator-basis scope
caveats to the Sec. IV "Scope and limitations" paragraph where they are already repeated.

---

## FINAL VERDICT

**MINOR REVISIONS**

The science is sound and unusually honest; the perturbation-transparency result (Sec. X) is
correct and the four-route closure is defensibly scoped. The two MAJORs are (M1) one
unsupported endpoint of a load-bearing headline σ range and (M2) reliance on three unposted
companion papers — both fixable without new physics. The MINORs are cleanup (internal-audit
residue, magnitude-label consistency, title strength, abstract length). No fabrication and no
arithmetic errors found in the equations and tables I recomputed. Not a reject; not yet a
clean accept.
