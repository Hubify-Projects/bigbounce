# P1B R-multi-round5 — synthesis

**Date**: 2026-06-01
**Paper**: P1B Technical Verification Companion (`arxiv/paper1b_mcmc_companion.tex`)
**Version reviewed**: v1B.0.34
**Version after closure**: v1B.0.34 (no bump; 0 VERIFIED)
**Round vendors**: Grok-4 (direct), gpt-4o (direct, fallback from gpt-5), Perplexity Sonar Pro (direct). Gemini-2.5-pro skipped.
**Protocol**: `feedback_peer_review_truth_audit_protocol` — per-finding truth-audit before any closure.

---

## Aggregate

| Reviewer | Findings | BLOCKER | MAJOR | minor |
|---|---|---|---|---|
| Grok-4 (brutal) | 6 | 6 (all flagged B) | 0 | 0 |
| GPT-4o (methodology) | 6 | 1 (B1) | 4 (B2-B5) | 1 (B6) |
| Perplexity Sonar Pro (citations) | 6 | 1 (B1) | 3 (M1-M3) | 2 |
| **Total** | **18** | **8** | **7** | **3** |

---

## Truth-audit verdicts

| Reviewer–ID | Verdict | Evidence |
|---|---|---|
| GRO-B1 (preamble audit log in .tex) | OPINION | Stripped at arXiv bundle stage by standing protocol; same as v1B.0.28 R28-GRO-B5 closure and v1B.0.33 round-4 |
| GRO-B2 ("ran stock codes, found nothing new") | OPINION | Companion-paper scope by design; retitling would erase the P1A verification mandate |
| GRO-B3 (Eskilt label unstable across rounds) | OPINION (already correct) | Current L1005-1006 reads "WMAP9 + Planck PR4/NPIPE analysis"; matches Eskilt reproduction repo README (github.com/LilleJohs/Cosmic_Birefringence) which states "Planck Data Release 4 (NPIPE)" + WMAP9. No fix needed; instability is historical, not present |
| GRO-B4 (+4.3σ/−3.6σ tail extrapolations) | OPINION | fn:wcaveat already labels as non-Bayesian/non-frequentist tail extrapolation; in-cell caveat-visibility rule from v1B.0.27 cascade |
| GRO-B5 (ALP MCMC adds no ECH value) | STALE | §VI explicitly says "not a distinctive ECH prediction"; same as GRO-B4 round-4 and GRO-B3 round-3 |
| GRO-B6 (paper is running changelog) | OPINION | Audit-log block stripped at arXiv bundle; same as GRO-B5 round-4 |
| GPT-B1 (CAMB ΛCDM+ΔNeff insufficient ECH proxy) | STALE | §I/§III scope notes already state companion paper performs null-consistency test, no torsion modifications by design |
| GPT-B2 (NaMaster pipeline-validation framing) | STALE | Abstract L298-301 + §IV scope-note L668-673 already label as pipeline-validation, not sky-detection; same as GPT-B2 round-4 |
| GPT-B3 (ALP rationale insufficient) | STALE | §VI explicitly says "not a distinctive ECH prediction"; same as GPT-B3 round-4 |
| GPT-B4 (ΔNeff Hubble-tension stat analysis) | STALE | §III §V Hubble-tension framing already presents posterior + credible intervals; not a tension-resolution claim |
| GPT-B5 (AIC/BIC/ln B model-comparison omitted) | STALE | Table app:claims row "Model-comparison ΔAIC/BIC/ln B — Omitted (pending v1B.0.18+ Nested Sampling)" deferred-by-design; same as GPT-B1/B4 round-4 |
| GPT-B6 (cross-paper table clarity) | OPINION | Cross-paper status table is a meta-Author note for SSOT mirror; minor presentation, not scientific defect |
| **PER5-B1 (Eskilt2022b "PR4/NPIPE" mis-labelled as "PR3" — REVERSE)** | **FALSIFIED** | External verification (re-run): Eskilt & Komatsu 2022 public reproduction repo at github.com/LilleJohs/Cosmic_Birefringence README confirms "The detector split maps of Planck Data Release 4 (NPIPE)". Reviewer's proposed fix ("Planck 2018 (PR3)") is exactly the round-3 regression that round-4 already corrected. Current v1B.0.34 text "WMAP9 + Planck PR4/NPIPE analysis" is correct. **No action — accepting this fix would re-introduce the round-3 regression.** |
| PER5-M1 (DESI DR2 arXiv 2503.14738 doesn't exist) | STALE | references.bib has the entry; flagged round-1 PER-B4 FALSIFIED, round-2 same, round-3 same, round-4 same. Sonar Pro web-search consistently fails to surface DR2 BAO preprint; entry verifiable on local bib |
| PER5-M2 (Liu ECTorsionDESI2025 arXiv 2507.04265 not real) | STALE | references.bib L571-579 has the real Liu+Li+Xu+Biesiada+Wang EPJC 2025 entry; flagged 4 rounds running (PER-B1, PER3-B1, PER4-B1); Sonar Pro web-search persistent miss |
| PER5-M3 (DiegoPalazuelos2025 ACT DR6 arXiv 2509.13654 not real) | STALE | references.bib L444-466 has the entry; flagged round-1 PER-B3 FALSIFIED, round-3 PER3-B3 STALE, round-4 PER4-M1 STALE |
| PER5-m1 (LiteBIRD 0.03° units underspecified) | OPINION | Canonical LiteBIRD sensitivity target ≈ 5×10⁻⁴ rad; round-3 PER3-B6 OPINION and round-4 PER4-m1 OPINION same grounds |
| PER5-nit1 (Hehl/Mercuri ΔNeff inference framing) | OPINION | Paper already attributes as theoretical deduction from contact-interaction structure, not direct CMB-era statement of cited papers; framing already careful |

**Totals**: 0 VERIFIED / 9 STALE / 8 OPINION / 1 FALSIFIED / 0 BLOCKER outstanding.

---

## Closure (v1B.0.34 stands)

**Zero VERIFIED findings.** No version bump. No recompile. No PDF mirror. No Convex bump.

**Special vigilance dispatched**: Perplexity BLOCKER-1 (proposing PR4/NPIPE → PR3 reversion) was truth-audited against the Eskilt reproduction repo per Houston's explicit directive. The reviewer was wrong; the round-3 → round-4 oscillation has converged on the correct phrasing ("WMAP9 + Planck PR4/NPIPE"), and accepting the reviewer's proposed "fix" would have re-introduced the round-3 regression. This is the third consecutive round where a citation-forensic reviewer has confidently mis-attributed the Eskilt dataset; the in-tex audit-log block now documents the full oscillation history so future rounds don't repeat it.

---

## Cascaded-R-rounds telemetry

| Round | Eskilt label state | Vendor clean | Counter |
|---|---|---|---|
| Round 1 closure | (FALSIFIED on bib-existence grounds) | 0/3 | — |
| Round 2 closure (v1B.0.32) | "PR4 NPIPE + WMAP" added | 0/3 | — |
| Round 3 closure (v1B.0.33) | regressed to "PR3" | 0/3 | — |
| Round 4 closure (v1B.0.34) | corrected back to "PR4/NPIPE" via repo cross-check | 0/3 | 0/3 |
| **Round 5 (this round)** | **stable; no change; reviewer-proposed reversion FALSIFIED** | **0/3 substantive findings, but no novel BLOCKER survived audit** | **1/3** |

**Convergence signal**: All 18 findings collapsed to STALE / OPINION / FALSIFIED. No novel BLOCKER, no novel MAJOR. The Eskilt thread is stable.

---

## Clean-vendor counter

- **Round 5**: 0 of 3 vendors fully clean by raw count, but 0 of 18 findings survive truth-audit. Per `cascaded-r-rounds` skill semantics, this is a convergent-silent round (no novel verified defects).
- **Counter advances**: **1/3** on v1B.0.34.
- **99%-gate**: Two more convergent-silent rounds at v1B.0.34 to exit cascade.

---

## Next round

- No rebuild; v1B.0.34 stands.
- Dispatch round 6 against v1B.0.34 (rotate vendors if possible; retry Gemini).
- If two more rounds return convergent-silent (counter 3/3), exit cascade and queue P1B for arXiv submission per `cascaded-r-rounds` exit criterion.
