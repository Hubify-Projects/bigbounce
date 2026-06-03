# P2 R-upgraded-round9 — Synthesis & Truth-Audit

**Date**: 2026-06-03
**Paper**: P2 — `research/focused_paper_source_integration/02_full_draft.tex` v1.7.42
**Round**: R-upgraded-round9 (regression-check round; R8 declared 3/3 EXIT MET)
**Vendors (4)**: Gemini-2.5-Pro, GPT-4o (fallback from GPT-5), Grok-4, Perplexity Sonar Pro
**Audit protocol**: feedback_peer_review_truth_audit_protocol + pattern-035 auto-FALSIFY for Perplexity citation confab

---

## EXIT STATUS: BROKEN — R9 caught one genuine math error that R8 missed

**Headline**: 1 VERIFIED MAJOR (Gemini-M1, six-monomial S3-orbit miscount). This is a regression of an earlier closure (R3 GEM-m1 was closed by *adding* the incorrect "6 orbits" justification at L225). Three R8 vendors did not catch it; Gemini did on R9. The 3/3 EXIT trigger at R8 was therefore premature.

**Recommended action**: Re-open as the 1 genuine novel BLOCKER/MAJOR of R9. Either (a) correct L225 to acknowledge the basis is a Cai-physics-restricted subset of the full 12-orbit S3-symmetric space, or (b) supply a derivation that the six listed monomials are exactly those with non-zero coefficients in the Cai et al. cubic-action expansion. Until closed, P2 readiness must oscillate backward (cap stays ≤ 95%).

---

## Per-finding truth audit

| ID | Vendor | Class | Topic | Verdict | Evidence |
|---|---|---|---|---|---|
| GEM-M1 | gemini | MAJOR | Six-monomial "complete S3-symmetric" claim | **VERIFIED** | L225 + footnote claim "exactly six orbits" of degree-9 partitions of 3 nonneg parts mod S3. Direct enumeration: (9,0,0),(8,1,0),(7,2,0),(7,1,1),(6,3,0),(6,2,1),(5,4,0),(5,3,1),(5,2,2),(4,4,1),(4,3,2),(3,3,3) = **12 orbits**. Paper's basis omits 6. Closure at L43-46 audit-trail entry introduced the incorrect "6 orbits" justification — that closure is itself wrong. |
| GEM-M2 | gemini | MAJOR | κ_1≈80 lacks citation | **OPINION** | L323 derives κ_1∈[5.6, 80] from explicit-prefactor + Hankel-amplitude propagation channels with refs to Cai App.~B and WilsonEwing. The bound is paper's own physics estimate, not from a single cited derivation; framing as derived range is honest. STALE-style closure already in place. |
| GEM-M3 | gemini | MAJOR | 9.9σ joint-Fisher | **STALE** | L364+ extensively caveats: "illustrative idealized-Fisher internal-consistency check," "deferred to companion artifact," "not as a competing detection forecast." R3-R8 closures land. |
| GEM-m1 | gemini | minor | μ/H→3/2 "mismatch vanishes" overstatement | **OPINION** | L244+ correctly states shape-overlap collapses to BF→1 at this endpoint; residual non-local structure is real but not load-bearing for the headline. Polish-tier nit. |
| GPT-B1 | gpt-4o-fallback | MAJOR | BF ~10–17 abstract vs ~4–17 body | **FALSIFIED** | Abstract L184 explicitly states "a curvaton-natural [-5,+5] competitor narrows this to a lower-envelope sensitivity check of BF ~ 4 ... and BF ~ 7 at the delta prior." Both numbers in abstract; no inconsistency. Pattern-009 gpt-4o-fallback low-rigor hit. |
| GPT-B2 | gpt-4o-fallback | MAJOR | Section-heading wording | **OPINION** | §2.2 heading "(Conditional on Faithful Cubic-Order Transfer)" already encodes the conditional. Rewording preference. |
| GPT-B3 | gpt-4o-fallback | MAJOR | 3–5σ vs 1.5–2.5σ confusion | **STALE** | L184 chain explicit: optimistic 5.2–5.5σ → post-systematic 3–5σ (Planck c=2) → Li/Brand c=1 halves to 1.5–2.5σ. R3 R-next-MIN-1 closed. |
| GPT-B4 | gpt-4o-fallback | MAJOR | Gauge vs physical frame separation | **STALE** | Abstract L184 already explicitly states "the CFC physical-frame statement is therefore a complementary theoretical discriminator, not the on-sky observable." |
| GPT-B5 | gpt-4o-fallback | MAJOR | 9.9σ deferred-companion misleading | **STALE** | Same as GEM-M3; quadruply caveated. |
| GPT-B6 | gpt-4o-fallback | MAJOR | Factor-of-two derivation gap | **FALSIFIED** | L86 + Appendix A.1/A.2 give explicit source-to-source normalization audit + four-vertex agreement check + in-in commutator interpretation. Derivation is extensive. |
| GRO-B1 | grok-4 | BLOCKER | "First time" template-overlap framing | **STALE** | R7/R8 closure of Grok MAJ-1 noted at audit-trail L73-74. Wording survives by Houston decision; pattern-016 wide-net-exit-reflag. |
| GRO-B2 | grok-4 | BLOCKER | "SPHEREx forecast" → "recast" | **STALE** | Conclusion L381 already explicit: "Our Bayesian model comparison ... indicates ..."; abstract L184 says "We forecast tests" which is correct verb (forecast of detectability, not a new Fisher matrix). Body §3-4 says "sensitivity recasting." Audit trail L92-94 closes. |
| GRO-M1 | grok-4 | MAJOR | UV-completion caveat marketing | **STALE** | Abstract L184 + §2.2 heading already disclose "verified only at linear order." Caveat is in abstract per audit-trail L37-38 closure. |
| GRO-M2 | grok-4 | MAJOR | BF 10–17 envelope inflation | **STALE** | v1.7.35 R-next-c-MAJ-1 already corrected Table 1 + abstract to lead with σ_theory=1.0 BF~10; delta-prior BF~17 demoted to upper-bound row. |
| GRO-n1 | grok-4 | nit | Appendix A length | **OPINION** | Houston framing; derivation is load-bearing for the convention closure. |
| GRO-n2 | grok-4 | nit | Audit-trail comments in .tex | **NIT-PROCESS** | VERIFIED but resolved at arXiv-tarball-stage strip per pattern-014; not a content blocker. |
| PER-B1 | sonar-pro | BLOCKER | Cai/Li factor-of-two citation chain | **FALSIFIED** | Pattern-035 auto-FALSIFY: no specific arxiv-id challenge, no citation cited paper, narrative-style forensics. Appendix A.1/A.2 + L86 already source each factor to specific paper statements. |
| PER-B2 | sonar-pro | BLOCKER | "Audit every cited paper" generic | **FALSIFIED** | Pattern-035 auto-FALSIFY: zero specific arxiv-id flagged; generic boilerplate request. |
| PER-B3 | sonar-pro | MAJOR | SPHEREx/MegaMapper/Heinrich mix | **FALSIFIED** | Pattern-035 + content false: §sec:discussion L364+ explicitly distinguishes bispectrum-only Fisher vs joint (f_NL, n_fNL) Fisher; r=0.84 is explicitly disclaimed for the SDB-Fisher channel ("does not apply"). |
| PER-B4 | sonar-pro | MAJOR | "Composite significance not source-backed" | **FALSIFIED** | Pattern-035; systematic budget table §7 itemizes each correction with source. |
| PER-B5 | sonar-pro | minor | "Robustness" overgeneralization | **OPINION** | Pattern-035 generic; no specific overclaim cited. |
| PER-B6 | sonar-pro | nit | Add citation-audit table | **OPINION** | Pattern-035 process-suggestion; non-actionable. |

---

## Totals

- VERIFIED real-action-landed: 0
- VERIFIED needs-action: **1** (GEM-M1, math error introduced by prior closure)
- STALE: 9
- FALSIFIED: 7
- OPINION: 5
- OOS: 0

## Pattern hits

- 001_perplexity_confab: 4
- 009_gpt4o_fallback_low_rigor: 6
- 016_wide_net_exit_reflag: 7
- 035_perplexity_arxiv_confab_HARDENED: 6 (P2 5+ consecutive rounds; auto-FALSIFY fires)
- 030_round_to_round_regression_drift: 1 (GEM-M1 closure-introduced regression)
- **NEW candidate pattern**: "closure-introduced math error" — prior closures can introduce new technical errors when justification is fabricated rather than verified

## Exit criteria assessment

| Criterion | Status |
|---|---|
| Novel BLOCKER/MAJOR (verified) | **1** (GEM-M1) — FAIL |
| Prior-round regressions | 1 (closure-introduced) — FAIL |
| Polish-tier MAJOR ≤ 1–2 | 0 — OK |
| **EXIT** | **NOT MET — re-open R9** |

## Readiness recommendation

Houston-facing: oscillate P2 readiness backward from R8-locked 99% to **≤ 95%** until GEM-M1 closure lands (correct L225 monomial-basis justification). Once fixed + one more clean cross-vendor round, resume to 99% cap.

**Critical flag**: R8 3/3 EXIT was wrong. R9 caught a real math error all four R8 vendors missed. The cascaded-R-rounds protocol prevented regression-shipping; do not declare 9-CLEAN LOCKED until GEM-M1 fix verified.
