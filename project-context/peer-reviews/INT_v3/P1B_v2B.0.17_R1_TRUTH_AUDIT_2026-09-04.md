# P1B v2B.0.17 R1 — truth audit (2026-09-04)

**Plan header.** Skeptical truth-auditor, told no expected outcome. Scope: the three
active legs (Grok API `grok-4.3`, Gemini API `gemini-3.1-pro-preview`, Claude INT Opus)
against the exact PDF sha256 `0d0c92ab…4001fcac`, 8 pp. Protocol: patterns 061–066,
directive H-refined. Every finding is fingerprinted, merged across legs, and classified
(a) GENUINELY-NEW REAL / (b) re-flag of a canonical disposition / (c) FALSIFIED with a
source citation / (d) OPINION / (e) OUT-OF-SCOPE disclosed. **Post-freeze work is not a
falsification:** findings already answered by the pre-registered batch 2 (frozen 2026-09-04,
after the PDF was frozen) are classed (a) GENUINELY-NEW REAL and marked
*closable in v2B.0.18 by integrating batch 2*. Sections: canonical list → per-leg counts →
verifications → closure plan (editorial + science).

**Steps:** (1) board [done]; (2) canonical list; (3) named verifications; (4) closure plan.

---

## Verification of the post-freeze evidence trail

Read directly, not taken on assertion:

- `pipelines/namaster_proof/blind_test/RULES_v2_FROZEN.md` — rule set R0–R6 with the
  wall-clock floor demoted to advisory and the M-hash rule withdrawn, plus pre-declared
  thresholds, Clopper–Pearson reporting requirement, the independence caveat, and an
  explicit "no rule may be added, removed, or edited between this freeze and the batch-2
  reveal".
- `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md` §6 "Batch 2".
- Commit-ordered trail, each in its own commit: `4451b135` (rules alone) → `28efa21c`
  (seal + S6 variant + `public2/sealed_digest.json`, no run output) → `27300504`
  (35 result+receipt pairs + `verdicts.json`) → `974e2859` (`sealed2/key.txt` reveal +
  scorecard) → `b3347c53` (manifest). Sealed key/assignment held outside the working tree
  through the sealed window; sealed digest `c96b5bf1…`, `seal_verified: true`.
- `pipelines/namaster_proof/RELATED_WORK_NOTE_2026-09-04.md` (commit `05b5940a`).
- Abstract of `arxiv/paper1b_namaster_proof.tex` read verbatim to check every quoted claim.

**Batch-2 outcome (35 runs, 7 arms × 5):** honest 0/5 flagged; S1–S4 5/5 each = **20/20**;
S5 metadata forgery escaped 5/5 (pre-declared); **S6 effective-multipole escaped 5/5**, and
**no rule was added after the fact**. One-sided 95% Clopper–Pearson: sensitivity lower
bound **0.861** (= 0.05^(1/20)); FPR upper bound **0.451** (= 1 − 0.05^(1/5)). Batch-1
equivalents, for the pilot framing: 12/12 → lower bound **0.779**; 0/3 → upper bound **0.632**.

---

## Canonical findings (23), merged across legs

Legend: **(a)** genuinely-new real · **(d)** opinion. No (b) re-flags (R1 on this version,
`DISPOSITIONS/P1B.md` holds no v2B fingerprints), no (c) falsifications, no (e).
"B2" = already answered by pre-registered batch 2 → closable in v2B.0.18 by integrating it.

| # | Fingerprint | Legs | Class | Source check | Closure action |
|---|---|---|---|---|---|
| C1 | Headline 12/12 + 0/3 obtained on the repo's own spin-0 MASTER estimator, not NaMaster and not the spin-2 operator; abstract does not qualify | Grok E1, E3; Gemini E1; Claude M6 | **(a)** | VERIFIED. Abstract says "evaluates … through the complete NaMaster bandpower-window operator" then "detected all 12 runs" with no surrogate clause; §6 "Scope limits" discloses it. Abstract/body mismatch is real. | Abstract clause: "demonstrated on an instrumented spin-0 MASTER estimator in this repository, not on NaMaster itself". |
| C2 | The "pre-declared, sealed blind protocol" had two rules amended *after* unblinding; the 0% FPR is a rule-fitting number, not a blind result | Gemini E2; Claude M1 | **(a)**, **B2** | VERIFIED and **TRUE for batch 1**: §4 states the wall floor "would have fired on 3/3 honest runs" and was excluded, and the M-hash rule was corrected, both "discovered by running the test". | **B2 fixes it**: rules frozen alone in `4451b135` *before* the seal `28efa21c`. Reframe batch 1 as the pilot/rule-development round with the post-hoc change disclosed; batch 2 becomes the primary result. |
| C3 | Seal priority asserted, not externally anchored; "independently verified" overstates; only 8 hex chars given | Grok M1; Claude M2 | **(a)**, **B2 partial** | VERIFIED. §6 quotes `0f4ca4ba…` with no timestamp or witness; batch 1's digest and outputs entered git in one commit (`d60949b7`). | **B2 partially fixes it**: commit-ordering trail (rules→seal→outputs→key→manifest), sealed material outside the tree, `seal_verified: true`. Residual = external anchor → SCIENCE item S2. Delete "independently verified"; state ordering, not witness. |
| C4 | Implemented R6 flags equality with `reference_bandpowers_sha256`; the paper describes only cross-run reuse — verifier and paper disagree | Claude M3; Q4 | **(a)**, **B2** | VERIFIED against `verify.py::main` via `RULES_v2_FROZEN.md`. | **B2 fixes it**: R6 restated verbatim with both disjuncts; batch 2 reports **all 5 S4 detections fired the reference disjunct, 0 the cross-run disjunct** — under the rule as previously *described*, S4 would have gone undetected. Print the verbatim R0–R6 table. |
| C5 | The five classes omit the effective-multipole shortcut the paper itself names as the common one, and were chosen inside the verifier's visible space | Claude M4; Q3 | **(a)**, **B2** | VERIFIED. §2 motivates the whole windows module by that shortcut; no arm tests it. | **B2 tests it and it ESCAPED 5/5**, with no pre-declared expectation and **no rule added afterwards**. The paper must now state the escape as a finding and narrow the claim to *structural shortcuts in instrumented steps*. |
| C6 | n=3 per arm supports neither "100%" nor "0%"; no intervals; replicates are not independent | Claude M5; Q7 | **(a)**, **B2** | VERIFIED — abstract prints bare percentages. | **B2 fixes it**: 20/20 with one-sided 95% lower bound **0.861**; 0/5 with upper bound **0.451**; independence caveat pre-declared (effective independent n per class = 1 for R1–R5). Paper must **print the CIs**, never a bare percentage. |
| C7 | No related work on provenance/attestation; novelty unlocatable | Claude M7; Q8 | **(a)**, **B2** | VERIFIED — reference list has no in-toto/SLSA/Sigstore/Rekor/RO-Crate entry. | `RELATED_WORK_NOTE_2026-09-04.md` (`05b5940a`) exists post-freeze; integrate as a half-page related-work subsection with citations. |
| C8 | Abstract's "non-adversarial-analyst threat model" overstates the guarantee §10 already limits (metadata forgery uncatchable in principle) | Grok E2; Claude M8 | **(a)** | VERIFIED — abstract phrase present; §10 states the stronger limit. | Replace with the operative wording: analyst may alter the computation but runs an **unmodified, instrumented harness**; forged metadata and downstream value-level shortcuts are out of reach. |
| C9 | 0.270°→0.270°, 0.342°→0.342°, null 0.000° over 500 realizations with no standard error | Gemini M1 | **(a)** | VERIFIED — §8 gives no uncertainty. **Not answered by batch 2.** | Report the SEM, or state that the recovery is algebraically exact (shared seeds) and explain why 500 realizations were run. |
| C10 | "maximum absolute difference 1.41e-18" quoted without the scale of the multiplicands | Gemini M2; Claude m5 | **(a)** | VERIFIED. | Give bandpower magnitude/units, or say "zero to double-precision rounding" rather than 3 s.f. of noise. |
| C11 | 8 pp is long / scope too narrow for a JORS software metapaper; recommend 4–5 pp | Grok M2 | **(d)** | Venue-fit judgment; JORS publishes no such page limit and the length carries a sealed protocol + results. Recorded, not actioned as a defect. | Optional tightening only. No claim change. |
| C12 | "manuscript revision v2B.0.17" internal versioning in the header | Grok N1 | **(a)** trivial | VERIFIED — lab stamp per directive G. | Strip from the submission copy only; keep in the served/lab copy. |
| C13 | 41 tests advertised, 2 skipped in a standalone install; no coverage figure or CI link | Grok N2; Claude m4 | **(a)** | Consistent with §7. | State 39/41 standalone-effective, add line/branch coverage and cite the workflow file. |
| C14 | Eq. 4 index k never defined at point of use | Gemini N1 | **(a)** | VERIFIED. | Define k ∈ {0, c, s} immediately after Eq. 4. |
| C15 | §6 opening claim stated without the threat-model qualifier | Claude m1 | **(a)** | VERIFIED. | Inline qualifier at point of claim. |
| C16 | "HMAC(key, run_id)" understates a balanced per-arm multiset that is HMAC-permuted | Claude m2 | **(a)** | VERIFIED against `seal.py`. | Say "HMAC-derived random permutation of a balanced design". |
| C17 | The effective-multipole deviation is asserted but never quantified anywhere | Claude m3 | **(a)** | VERIFIED — §8 says the comparison is recorded, never reports it. | Report max fractional bandpower deviation or induced angle shift; it is the quantitative motivation for the windows module and now also the S6 arm. |
| C18 | "~1 minute" (§6) vs "one to two minutes" (§11) | Claude m6 | **(a)** trivial | VERIFIED. | Harmonize. |
| C19 | The 54× cold/warm ratio vs the 3–15× shortcut signal deserves a generalizing sentence | Claude m7 | **(d)** | Enhancement, not a defect; the point is already made. | Optional; batch 2 confirms the wall rule fires 5/5 honest + 5/5 S6. |
| C20 | macOS listed "untested" though the suite is developed there | Claude m8 | **(a)** | VERIFIED. | "Exercised locally on macOS, not covered by CI." |
| C21 | Table 2 gives prose rule names, not R1–R6 identifiers | Claude m9 | **(a)** | VERIFIED. | Use implemented identifiers so the table maps onto `verdicts.json`. |
| C22 | Sealed digest published but not the sha256 of `verify.py` — self-inconsistent for a receipts paper | Claude m10 | **(a)**, **B2** | VERIFIED. | **B2 fixes it**: `public2/frozen_rules_digest.json` records the verifier digest at seal time. Quote it. |
| C23 | Per-run verdicts not inspectable without a checkout | Claude m11 | **(a)** | VERIFIED. | Include `verdicts.json` as an appendix table (35 rows, batch 2). |

**Counts: 23 canonical · 21 genuinely-new REAL · 2 OPINION · 0 FALSIFIED · 0 re-flags · 0 out-of-scope.**
Of the 21 real items, **8 (C2, C3-partial, C4, C5, C6, C7, C22 + C1's evidence base) are already
answered by post-freeze work** and close by integration rather than by new computation.

**Author questions (8, Claude leg).** Q1/Q2 → answered by the batch-2 commit ordering.
Q3 → answered: S6 escaped 5/5. Q4 → answered: reference disjunct 5/5, cross-run 0/5.
Q7 → answered: effective independent n = 1, pre-declared. Q5/Q6 (run the blind test against
real PyMaster; which hook carries the 3j counter) remain **open and honest** — they are the
NaMaster-applicability limitation, disclosed, not closable by editing. Q8 → the related-work
note addresses in-toto/Rekor as the S5 anchor.

---

## CLOSURE PLAN

### (i) Editorial / real edits for v2B.0.18 — integrate batch 2

**Abstract (rewrite the empirical block).** Replace the 18-run sentence with the batch-2
result plus the three qualifiers that C1, C2, C6, C8 demand: surrogate estimator, frozen
rules, counts-with-intervals. Add one scope sentence naming the threat model as
*unmodified, instrumented harness*.

**§2 (motivation).** Quantify the effective-multipole deviation (C17) — the number that
motivates the windows module is also the S6 arm's subject.

**§4 (notation).** Define k ∈ {0, c, s} after Eq. 4 (C14).

**§6 (protocol + result) — the largest edit.**
1. Relabel batch 1 explicitly as the **pilot / rule-development round**, and *disclose* that
   two rules were amended after outcomes were seen (wall floor fired 3/3 honest; M-hash
   collision non-evidential). Do not delete it and do not defend it — state it (C2).
2. Present **batch 2 as the primary result**: rules frozen in their own commit before the
   seal, 35 runs / 7 arms × 5, commit-ordered trail `4451b135 → 28efa21c → 27300504 →
   974e2859 → b3347c53`, sealed digest `c96b5bf1…`, `seal_verified: true`, sealed material
   held outside the tree (C3 ordering half).
3. Print the **verbatim R0–R6 rule table** with both R6 disjuncts, and the withdrawn/advisory
   rules in a separate "not part of the decision set" block (C4).
4. Report **counts with one-sided 95% Clopper–Pearson bounds, never bare percentages**:
   S1–S4 20/20, lower bound 0.861; honest 0/5, FPR upper bound 0.451; S5 escaped 5/5;
   **S6 escaped 5/5** (C6, C5). Carry the pre-declared **independence caveat**: effective
   independent n per class is 1 for R1–R5; replicates measure firing reproducibility.
5. Add the **S6 subsection**: what it does (builds the operator genuinely, shortcuts
   downstream at one effective multipole), why R0–R6 cannot see it (no rule inspects result
   *values*), and the explicit statement that **no rule was added after the fact**.
6. Replace "independently verified" with what was actually checked (C3).
7. Fix the HMAC/balanced-design description (C16) and the inline threat-model qualifier (C15).
8. Quote the frozen-verifier digest from `public2/frozen_rules_digest.json` (C22).

**§7.** Give the bandpower scale beside 1.41e-18 (C10); state 39/41 standalone-effective plus
coverage and the CI workflow (C13).

**§8.** Report the SEM on the 0.270°/0.342°/0.000° recoveries, or state algebraic exactness
and justify 500 realizations (C9). **This is the one real item batch 2 does not touch.**

**New §"Related work".** Half a page from `RELATED_WORK_NOTE_2026-09-04.md` placing execution
receipts against in-toto/SLSA provenance, Sigstore/Rekor transparency logs, and RO-Crate /
research-object provenance (C7, Q8).

**§10–11.** Threat model as an explicit early assumption (C8); NaMaster applicability stated as
the open limitation with Q5/Q6 named honestly; harmonize the timing figures (C18); macOS
wording (C20); Table 2 by R-identifier (C21); appendix of the 35 per-run verdicts (C23).
Strip the internal version stamp from the submission copy only (C12).

**Tables/figures.** Table 2 is regenerated from `public2/verdicts.json` (7 arms × 5); per
directive I6 check that no figure image bakes in a batch-1 number.

### (ii) SCIENCE items (not closable by editing)

- **S1 — Batch 3 with a value-level rule, pre-registered.** S6 escaped because nothing in
  R0–R6 inspects result *values*. Pre-register (own commit, before the seal) a value-level
  rule — a declared tolerance band on bandpowers against an independently-known reference,
  or a cross-checked second estimator — then seal, run, reveal in the same commit order.
  Batch 3 is the only thing that converts the S6 escape into a closed class. Explicitly
  **future work, not claimed** in v2B.0.18.
- **S2 — External timestamp for the seal.** Ordering is provable from git; witness is not.
  Deposit the sealed digest alone into an external anchor (OpenTimestamps / Rekor / a Zenodo
  or OSF deposit of the digest) before the batch-3 seal. This is the *same* anchor that would
  close S5 metadata forgery, so it retires C3's residual and the S5 limitation together.
  Until then it stays a stated limitation, not a claim.
- **S3 — NaMaster applicability (Q5/Q6).** Either add a 3j-count instrumentation hook inside
  PyMaster and re-run the honest + S1 arms at small nside, or keep the surrogate scope
  statement. Not required for v2B.0.18; required before any claim about NaMaster itself.
- **S4 — Zenodo DOI + ASCL entry** (Houston account actions, §5 of the design note).

### The exact N3-eligible sentence that survives batch 2

Everything stronger than this is now unsupported. The phrase "shortcut detector, not a fraud
detector" survives only with the second escape named beside it:

> Under a non-adversarial-analyst threat model — the analyst may alter the computation but
> runs an unmodified, instrumented harness — execution-trace receipts decide, from receipts
> alone and without re-running the computation, whether the *structural* steps of an
> expensive pseudo-C_ℓ analysis were performed: in a sealed batch of 35 runs scored by
> decision rules frozen and committed before the seal was drawn, the verifier flagged 20/20
> operator-skipping, operator-truncating, grid-reducing and cache-substituting runs
> (one-sided 95% lower bound 0.86) with 0/5 false positives on honest runs (one-sided 95%
> upper bound 0.45), while both the metadata-forgery arm and the effective-multipole arm
> escaped 5/5. Receipts of this kind are therefore a detector of *structural* shortcuts in
> instrumented steps — not of forged metadata, and not of value-level shortcuts taken
> downstream of the instrumented operator. An earlier 18-run pilot developed these rules and
> is reported as such.

**"First-of-kind" after batch 2.** No first-of-kind claim survives on the primitive itself —
C7 shows the provenance/attestation literature (in-toto, SLSA, Sigstore/Rekor, RO-Crate) is
unaddressed, so priority is unlocatable until the related-work section lands. What is
defensible is narrower and should be stated that way: *the first pre-registered, sealed blind
measurement of shortcut-detection sensitivity for pseudo-C_ℓ execution receipts, including a
negative class (S6) reported as an escape.* Demonstration on a surrogate spin-0 estimator
must accompany it.
