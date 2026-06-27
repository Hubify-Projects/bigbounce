# EXTDB P1A Truth Audit — De-biased external round (R57, v1A.0.82)

Round: EXTDB (DE-BIASED neutral referee prompt), 2026-06-27
Source audited: `arxiv/paper1a_ech_nogo.tex` (v1A.0.82)
Verdicts: Gemini = MAJOR REVISIONS, Grok = MAJOR REVISIONS, ChatGPT = MINOR REVISIONS (contrast anchor)
Calibration applied: patterns 061 (in-text verdict), 063 (math = FALSIFIED until source-checked),
064 (Grok harsh-outlier — audit each reason; prior P1A Grok REJECTs all false-positives); June 2026
calibration (arXiv valid; "in preparation / posted concurrently" companions = deliberate OUT-OF-SCOPE;
f_NL 2.6–5σ range now cites P2 per R57).

---

## Headline

**Verdict: the two MAJOR recommendations are driven mostly by KNOWN, ALREADY-DISCLOSED
limitation classes (companion-dependency + the on-shell dimensional ansatz) — NOT real
defects. BUT one convergent point is a GENUINE, fixable polish-tier overstatement: the
repeated "13 logically-independent barriers" headline.** That is the single honest open
finding the de-bias surfaced. P1A's science holds; one wording fix is owed.

---

## MAJOR-by-MAJOR verdict against source

### Gemini Major 1 — "Heavy reliance on unverifiable companion papers" (P1b, P2, P3, P4 in-prep)
**Verdict: OUT-OF-SCOPE (deliberate companion-coupling class).**
P1A is by design a companion-coupled no-go paper. Companions are registered in
`paper1a_ech_nogo.bbl` "(in preparation)" and posted concurrently; arXiv referees cannot
see in-prep companions, so "I can't verify them" is a visibility artifact, not a defect
(matches prior FALSIFIED PER-B1 calls, e.g. v1A.0.37). The de-bias simply made reviewers
weight this harder. Per the standing calibration this is the known OUT-OF-SCOPE class:
"not self-contained / depends on companions" is NOT a load-bearing problem. Grok files the
same point as MINOR m1 — correct severity; Gemini's MAJOR-tier escalation is uncalibrated.
*No science is wrong; companion inlining is a presentation upgrade, not a required fix.*

### Gemini Major 2 / Grok M2 — "Dimensional integrity / centrality of the on-shell scaling ansatz"
**Verdict: STALE (already disclosed) + OPINION (presentation preference).**
The Eq.(6) off-shell mass-dimension +1 (vs +4) status is stated in §II.C, Appendix B, AND
the abstract. Source L729–733: *"The dark-energy mapping rests on a phenomenological on-shell
scaling ansatz whose off-shell mass dimension is +1 rather than +4 … we treat this scaling
explicitly as an ansatz, not a derivation; all R4 and dark-energy mapping claims are
conditional on this ansatz."* This is verbatim what Grok M2 demands ("qualify closure by
'under the stated phenomenological on-shell scaling ansatz'"). Gemini itself concedes it is
"labeled transparently as an ansatz." The residual asks — move dimensional analysis to main
text, discuss alternative mappings — are strengthening suggestions, not defects. The substance
is fully disclosed and the no-go is explicitly conditioned. *Not load-bearing.*

### Grok M1 — "Insufficient justification that the four routes are representative/exhaustive"
**Verdict: OUT-OF-SCOPE / OPINION (the feared overstatement is already guarded).**
The title says "**Four** Minimal ECH Dark-Energy Routes" (explicit count, not "all").
Abstract L722–728: *"This is a channel-level assessment, not an operator-level theorem: the
four enumerated routes … are not proven to be a complete … operator basis … we acknowledge
missing operators (Jackiw–Pi …, parity-odd four-fermion partner) explicitly."* §IV "Scope"
(L1572–1591) repeats this. So the paper does NOT claim the four exhaust the route space — it
explicitly disclaims it. Prior identical Grok call (GRO-M1, "exhaust") was closed v1A.0.37 and
re-flagged STALE. Grok's requested operator-enumeration table would strengthen the paper but is
not required; the overstatement it fears is already neutralized. *Not load-bearing (pattern-064
confirmed: Grok over-escalates an already-guarded point).*

### Grok M3 + ChatGPT Major 1 — "'13 logically-independent barriers' overstates the actual logical structure"
**Verdict: VERIFIED — REAL, polish-tier overstatement / internal inconsistency. The one honest open finding.**
This is the CONVERGENT point: the harsh outlier (Grok) AND the careful anchor (ChatGPT, MINOR
overall) independently flag it — convergence raises signal above pattern-064 noise. Source check
confirms a live inconsistency **inside the abstract itself**:
- L734–741: "13 **distinct** barriers … described as distinct **mechanism-class constraints**" (careful)
- L764: "constrained … by 13 **logically-independent** barriers" (strong headline)
and "13 logically-independent" recurs ~10× in the body (L764, 829, 968, 991, 1300, 2194, 2780,
2936, 2980, 3145). Meanwhile the paper itself admits several barriers are heuristic (B9, L2210),
conditional, share the same scaling ansatz, or are general/classificatory (Grok lists B5,B6,B7,
B9,B10,B13). "Logically-independent" repeated as a headline strength therefore overstates relative
to the paper's own caveats — a genuine self-favoring framing the de-bias was built to catch.
ChatGPT names the exact fix.

**EXACT .tex FIX (honest open finding):**
Replace the recurring headline "13 logically-independent barriers" with ChatGPT's calibrated
phrasing — "13 mechanism-class constraints, several of which rely on shared assumptions but probe
distinct physical failure modes" — OR add a one-line clarifier at first use that "logically-independent"
means *no barrier is a logical consequence of another* (NOT disjoint assumptions; several share the
on-shell scaling ansatz and several are heuristic/classificatory). Apply consistently across L764,
829, 968, 991, 1300, 2194, 2780, 2936, 2980, 3145, and resolve the L735-vs-L764 abstract
inconsistency. Polish-tier, not a blocker; no science changes.

---

## ChatGPT Majors 2 & 3 (contrast — both MINOR-grade requests)
- Major 2 (Route 2/3 = conservative EFT bounds, label consistently): **STALE/OPINION.** L1584,
  v0.74 comment, and §IV already mark R2/R3 as "explicitly-labeled ansatz-level scoping … not
  load-bearing for the no-go." Wording-consistency polish.
- Major 3 ("minimal ECH cannot" vs "channels examined cannot"): **STALE.** Same class as Grok M1;
  abstract + Scope already restrict to the four enumerated channels. Conclusions could be swept once
  more for stray broad phrasings (cheap), but the scope is established.

---

## Bottom line
- BLOCKERS: none (all three reviewers agree; core Bianchi-decoupling result sound).
- Companion-dependency (Gemini M1, Grok m1): OUT-OF-SCOPE — known deliberate class, not a defect.
- On-shell ansatz centrality (Gemini M2, Grok M2): STALE — fully disclosed + conditioned in abstract.
- Four-route representativeness (Grok M1, ChatGPT M3): OUT-OF-SCOPE/OPINION — explicitly disclaimed already.
- **"13 logically-independent" (Grok M3 + ChatGPT M1): VERIFIED-real polish overstatement → one wording fix owed.**

The de-bias earned its keep: it converted a soft framing slip into a flagged open finding. P1A's
substance holds; close the one VERIFIED item by softening the "logically-independent" headline.
