# Publishability Report — 2026-06-09 (end of Day 1, Fable-5 push)

**For:** Houston · **From:** research-partner session · **Verdict up front:**
you are **one billing action + one clean review cycle + your sign-off pass**
away from submitting all six papers. Everything agent-doable is done or queued
behind those three gates. Target submission window **2026-06-11/12** holds.

---

## 1. Where each paper stands (all versions live on site + Convex dev/prod)

| # | Paper | Version | pp | Readiness | Review queue | Blocking gate |
|---|---|---|---|---|---|---|
| P4 | Chirality catalog | v1.0.167 | 17 | 85 | **EMPTY** (49 findings closed today) | 2 Claude-inclusive clean rounds (post-retraction rule) |
| P1A | ECH channel closure | v1A.0.50 | 23 | 92 | empty | 1 clean round |
| P1B | Technical companion | v1B.0.51 | 13 | 90 | **EMPTY** (31+2 closed) | 1 clean round |
| P2 | f_NL forecast | v1.7.45 | 22 | 92 | **EMPTY** (8 closed; 3 vendors + meta returned zero) | 1 clean round |
| P3 | Anomaly catalog | v3.1.80 | 23 | 90 | **EMPTY** (36 closed, incl. measured dedup sweep) | 1 clean round + HF dataset flip |
| P5 | DESI chirality×env | v0.1.52 | 24 | 90 | **EMPTY** (24 closed + covariate regression) | 1 clean round; submits after P4's arXiv ID |

Submission order: **P4 → P1A+P1B (same day) → P3 → P2 → P5** (P5 cites P4's
arXiv ID — the only hard dependency).

## 2. What made today decisive (the integrity story)

This was provenance day. The April "close 4 future-work items" pod wave was
audited end-to-end and **all four of its products were untraceable**; every one
is now replaced by committed, reproducible computation:

- **P4**: the −0.122σ headline was computed on a *synthetic* catalog →
  retracted (v1.0.166), paper re-anchored on the real-space null + template
  exclusion, then v1.0.167 closed 49 findings from TWO independent 5-vendor
  rounds + a 12-job compute batch (10k-permutation nulls with printed rank-p,
  weight-map sweep, pool verification, shot-noise floor).
- **P2**: the 9.9σ running-f_NL claim → honest 1.4σ/0.6σ from a
  Doré-validated, committed Fisher (the artifact's numbers were irreproducible
  under any configuration).
- **P3**: NANOGrav numbers already migrated; today the eROSITA enrichment
  null (statistically invalid — dependent detectors) was reframed and the
  deferred dedup sweep was actually run (0.086% measured).
- **P1B**: the NaMaster validation was honestly relabeled (synthetic ΛCDM
  skies, not Commander), SNRs relabeled template-fit, and **w_pivot corrected
  to +2.5σ from −1** (twice-verified from the DESI-DR2 chain — consistent
  with the known DESI evolving-DE preference; the old −1.1σ used a formula
  that provably violated the Cauchy bound).
- **P5**: root-caused a duplicate-TARGETID join inflating several tables;
  rebuilt bright/dark, Phase-2 sweep, and Tempel concordance on the declared
  parent; added omnibus χ² (p=0.31/0.99) and a full physical-covariate
  regression (100% GZ-DESI join; env Wald p=0.46/0.99).

**Why this raises acceptance odds:** every number in all six papers now traces
to a committed artifact or shown arithmetic; the corrections are disclosed in
journal-neutral language; and the new quantitative anchors are *stronger* than
what they replaced (e.g., P4's harmonic-channel completeness: a Shamir-class
1.7% dipole would register at z≈68–218 vs the observed +7.3 — an
order-of-magnitude amplitude refutation independent of the systematics
attribution).

## 3. The splash case (honest, N3-ceiling framing)

1. **P4** — largest chirality-labeled galaxy catalog (3.2M spirals, public,
   model weights + full reproducibility), resolving the long-running
   Shamir-dipole controversy with a quantified leakage mechanism + completeness
   argument. First-of-kind demonstration class.
2. **P3** — 378k-anomaly multi-survey catalog, ~141× the largest prior
   single-survey catalog, with an honest per-survey QA story (the LAMOST tier
   retained as a documented training-bias lesson — reviewers reward this).
3. **P5** — first DESI-scale chirality×environment independence test with
   z-shell selection correction + covariate robustness; clean constraint on
   environment-coupled parity models.
4. **P1A+P1B** — channel-level ECH closure + perturbation-transparency theorem,
   with a verification companion whose every pipeline claim is artifact-traced;
   the corrected w_pivot (+2.5σ) plugs into the live DESI evolving-DE
   conversation.
5. **P2** — the parameter-free f_NL=−35/8 target with a realistic 3–5σ SPHEREx
   forecast and committed Fisher inputs — a falsifiable near-term prediction.
6. **Meta-contribution** — the provenance-audit + retract-and-rebuild
   methodology itself (transparent corrections, truth-audited multi-model
   review, 12-job reproducibility chain for ~$0.55 of compute) is a credibility
   asset; consider a short companion note or blog post at announcement time.

## 4. Remaining gates — exactly who does what

**Houston (≈20 min + reading time):**
1. **Top up Anthropic API credits** (console.anthropic.com → Plans & Billing).
   This is the entire critical path: the Claude reviewer leg has been down
   since ~13:00 PT; all of today's rounds ran 4-vendor (stamped DEGRADED).
2. After rounds come back clean: **sign-off pass per paper** (15 min each via
   the site) — the final 1% is yours by policy.
3. **arXiv mechanics**: endorsement for astro-ph.CO/GA/IM + submit. The kit
   (`project-context/SSOT/arxiv_submission_kit.md`) has all six tarballs
   standalone-verified + ≤1,920-char webform abstracts — 15 min per paper.
4. P3 only: flip the HF dataset public at submission.

**Agents (auto, after your credits top-up — say "credits topped up"):**
1. Claude-inclusive confirmation rounds on all six (P4 needs two).
2. Truth-audit each; close any residual findings same-day.
3. Final /paper-pre-review-check + pattern-040 + closure-ledger sweep.
4. Readiness restoration per the oscillation rule as clean rounds land.

**Running right now:** site data-consistency agent (stale-state elimination,
figure re-seeds, contributions page) + site UI/UX agent (paper pages, status
dashboard, galleries, mobile) — both report back tonight; hourly autoloop
continues as the regression detector with verified mirrors + degraded-round
stamping.

## 5. Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Confirmation rounds find new MAJORs on today's heavy edits | medium | same-day closure capacity demonstrated (5 waves today); buffer day 06-12 |
| P4's +7σ diagnostic invites referee questions despite attribution | medium | completeness + 8-anchor battery + 10k-perm rank-p now in-paper; honest framing |
| arXiv moderation hold (new submitter, multiple same-day papers) | low-medium | stagger P4 day 1, P1A+P1B day 2, P3/P2 day 3; endorsement secured first |
| w_pivot +2.5σ draws attention | low | it agrees with DESI DR2's own preference; framed as consistency, not discovery |
| Site/Convex drift during final edits | low | consistency sweep running; bump protocol enforced |

## 6. Compute + cost ledger (today)

12 pod jobs (C1–C9f) ≈ **$0.55** total. Pod stopped, volume retained,
backup-3plus complete. No compute remains on the critical path.
