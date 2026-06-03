# P5 v0.1.43 — R-upgraded-round9 synthesis

**Round**: 2026-06-03_R-upgraded-round9 (P5 DESI Chirality)
**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.43-2026-06-02
**Vendors**: Gemini-2.5-Pro (cosmology), GPT-4o fallback (methodology), Grok-4 (brutal), Perplexity Sonar Pro (citations) — direct vendor APIs
**Cascaded-exit counter**: 1/3 (this is the first non-silent round in 5 rounds — R5+R6+R7+R8 were Gemini-convergent silent)
**Triage protocol**: per `feedback_peer_review_truth_audit_protocol`

---

## Headline finding

First round where vendors saw the compiled v0.1.43 PDF for real. Two substantive recurring themes survive:

1. **Title still leads with V-Web** (Grok GRO-B1) — title currently
   "Environmental Dependence of Spiral Chirality Across DESI Large-Scale
   Structure: A V-Web Cosmic-Web Test on 791,635 Matched Spirals with
   DESIVAST-Anchored Void Cross-Check." Declared primary path is DESIVAST
   (n=56,981, three-algorithm); "V-Web Cosmic-Web Test" framing makes V-Web
   look primary. **Verdict: VERIFIED.**

2. **"Largest-sample null confirmation" / "strongest" wording**
   (Grok GRO-B2) — paper retains both "largest-sample null confirmation"
   AND parenthetical "(a null is not positive evidence; it is the
   strongest available rejection of the alternative ...)" at lines
   1513–1516. The contradiction Grok flags is partially addressed by the
   parenthetical, but the framing still oscillates. **Verdict:
   PARTIALLY VERIFIED — wording is internally hedged but reviewer-visible
   tension remains.**

3. **Toy EFT appendix** (Gemini GEM-B1, Grok GRO-M2) — convergent across
   two vendors. Gemini calls the operator "ill-posed" (rotational + gauge
   invariance), Grok wants it deleted entirely. Paper already has a long
   v0.1.41 GEM-B1/m2 closure caveat (lines 2321–2349) acknowledging both
   issues explicitly. The caveat does not "fix" the operator, it
   documents that it is heuristic-in-slicing. **Verdict: STALE — closure
   already executed in v0.1.41; reviewers re-flag because the operator
   itself is still in the paper. Decision needed: delete vs. retain with
   caveat.**

## Per-finding triage

| ID | Vendor | Class | Verdict | Note |
|----|--------|-------|---------|------|
| GEM-B1 | Gemini | BLOCKER | STALE | Already closed v0.1.41 with explicit caveat (lines 2321–2349). Retain caveat or delete appendix. |
| GEM-M1 | Gemini | MAJOR | VERIFIED | RSD discussion (§XII) leads with scalar-displacement; anisotropic-eigenvalue path is real and not the lead framing. |
| GEM-m1 | Gemini | minor | VERIFIED | "Any future model" overstates; need scale-locality caveat (25 Mpc/h). |
| GEM-m2 | Gemini | minor | OPINION | Asks for Chern-Simons mention in Discussion. Stylistic, low-impact. |
| GEM-n1 | Gemini | nit | VERIFIED | §XI.B title "Bounce vs. inflation discrimination" mislabels its own conclusion. |
| GPT-B1 | GPT-4o | BLOCKER | OPINION | Generic "tempering" ask; abstract already lists 7 stratifications + 4 DESIVAST cross-checks. Over-call. |
| GPT-M1 | GPT-4o | MAJOR | STALE | Empirical max-stat MC null IS the primary path per §sec:primary_path added v0.1.39 (GEM-M2 closure). Reviewer didn't see it. |
| GPT-M2 | GPT-4o | MAJOR | OPINION | Phase 2 max-range IS a sensitivity diagnostic, not a significance claim. Misread. |
| GPT-M3 | GPT-4o | MAJOR | DUP (of GEM-M1) | Same RSD-anisotropy point; merge. |
| GPT-M4 | GPT-4o | MAJOR | OPINION | DR1 VAC generalizability already discussed in §XII. |
| GPT-n1 | GPT-4o | nit | OPINION | Toy EFT relevance — see GEM-B1 verdict. |
| GRO-B1 | Grok | BLOCKER | VERIFIED | Title leads with V-Web despite DESIVAST being declared primary path. Real overclaim risk. |
| GRO-B2 | Grok | BLOCKER | PARTIALLY VERIFIED | "Largest-sample null" + "strongest" tension survives despite v0.1.40 GRO-M1 closure attempt. |
| GRO-M1 | Grok | MAJOR | DUP (of GEM-M1) | Same anisotropic-RSD concern. |
| GRO-M2 | Grok | MAJOR | STALE | Toy EFT — see GEM-B1. |
| GRO-m1 | Grok | minor | VERIFIED | Paper IV companion is "in preparation"; load-bearing numerical anchors (P4 monopole -0.0026) flow from it. Per-PER-M5 it's labeled, but Grok's point about external verifiability stands. |
| GRO-n1 | Grok | nit | VERIFIED | ~380-line preamble comment changelog (lines 22–404) should be stripped before arXiv. Standard practice. |
| PER-M1 | Perplexity | MAJOR | VERIFIED | DESIVAST scope-blur (void catalog vs DR1 environment anchor). Real wording cleanup needed in abstract/§VIII intro. |
| PER-M2 | Perplexity | MAJOR | OPINION | TWebDESI2026 "preprint" standardization. Sweep already done v0.1.40 PER-n1. Likely STALE. |
| PER-M3 | Perplexity | minor | NO-ACTION | Confirms Shamir2022 fixed. |
| PER-M4 | Perplexity | minor | OPINION | Stylistic clarification of foundational vs. specific-implementation refs. |
| PER-M5 | Perplexity | minor | NO-ACTION | Confirms internal-companion labeling is acceptable. |
| PER-M6 | Perplexity | nit | NO-ACTION | Alexander-Yunes + Lue confirmed correct. |

## Truth-audit citation forensics

- **DESIVAST author order** (R-round recurring): bibitem reads
  `H.~Rincón, S.~BenZvi, K.~A.~Douglass et al.`, arXiv:2411.00148.
  Per v0.1.39 PER-B1 closure (line 199) and prior WebFetch verification,
  Rincón is correct first author. **No regression.**
- **Artifact links**: spot-checked `pipelines/p5_desi_chirality/config/p5_config.yaml`,
  `env_finder/reports/01_volume_fractions.json`,
  `results/analysis_cosmic_web/desivast_canonical_void_chirality.json` —
  all present on disk. Pattern-026 anchor-404 risk: low for this round.
- **arXiv IDs** TWebDESI2026 (2604.02463) and ASTRADESI2026
  (2604.01456) previously verified VERIFIED + FALSIFIED tagged respectively
  in changelog; Perplexity now reports both real and matched.

## Recommended actions (DO-NOW classification per /no-future-work-defer)

**BLOCKER-tier (do-now, v0.1.44):**
1. **Title swap** — drop "V-Web Cosmic-Web Test on 791,635 Matched Spirals"
   from lead position; lead with DESIVAST-anchored framing.
2. **"Strongest" wording sweep** — line 1515 + abstract; replace any
   remaining "strongest" / "largest-sample positive" with "largest
   controlled-sample null" + explicit "null ≠ positive evidence" once,
   not twice.

**MAJOR-tier (do-now, v0.1.44):**
3. **RSD anisotropy reframing** (§XII) — lead with tidal-tensor
   anisotropic eigenvalue deformation; treat scalar displacement as
   secondary heuristic. Per GEM-M1 + GPT-M3 + GRO-M1 convergence (3-way).
4. **DESIVAST scope tightening** (PER-M1) — sweep abstract + §VIII intro
   to keep DESIVAST strictly described as a void catalog, not a DR1
   environment anchor.

**minor-tier (do-now):**
5. **"Any future model" scale-locality caveat** (GEM-m1) — add 25 Mpc/h
   smoothing-scale clarifier in §I, §XI.
6. **§XI.B title rename** (GEM-n1) — "Implications for bounce and
   inflation models".
7. **Preamble changelog deletion** (GRO-n1) — strip lines 22–404 before
   arXiv submission. Add a "submission-strip" target to the Makefile.

**Decision needed:**
8. **Toy EFT appendix** — keep with v0.1.41 caveat (current state) or
   delete entirely per Grok GRO-M2. Recommend **keep** because the
   caveat is honest and the appendix is explicitly labeled as a
   guide-for-model-building, not a derived bound. Two vendors disagree;
   if external journal review flags it again, delete.

## Cascaded-exit logic

- Counter: 1/3 toward exit.
- This round produced **substantive new findings** (title + RSD-anisotropy
  + DESIVAST scope) that 5 silent rounds missed because they didn't open
  the PDF. Convergence streak from R5+R6+R7+R8 effectively resets — these
  findings need a v0.1.44 closure pass + a fresh R10 round before the
  counter advances.
- **Cascaded counter rolled back to 0/3.** Need 3 consecutive
  substantively-silent rounds on the post-v0.1.44 PDF.

## Patterns matched

- pattern-008 (RSD restructure regression) — GEM-M1 + GPT-M3 + GRO-M1
  re-fire on the new section structure.
- pattern-020 (load-bearing buried) — GRO-B1 title re-fire; v0.1.39
  GEM-M3 elevation of DESIVAST section happened but title didn't track.
- pattern-026 (anchor 404s) — N/A this round.
- pattern-029 (estimator multiplicity) — addressed v0.1.39, GPT-M1 misread.

## Action

Counter does NOT advance. v0.1.44 closure bundle required for 7 do-now items,
then re-fire as R-upgraded-round10.
