# P5 R28conf — TRUTH AUDIT (final verdict of the six-paper campaign)

**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.59 (+ pre-round word fix "$|z|$ stays below $2\sigma$ (maximum 1.93)")
**Reviewed PDF**: v0.1.59 md5=3a80c50b, 28 pp
**Ground truth**: 17/18/21/22/23/24/25/26-series artifacts under `pipelines/p5_desi_chirality/outputs/`; live arXiv check for citation forensics
**Auditor**: Claude (in-session), 2026-06-10
**Precedent**: R26conf + R27conf truth-audit tables applied (extraction-artifact, future-date, convention-misread, citation classes)

## Verdict schema
VERIFIED (real, fixed/queued) · STALE (already in tex) · FALSIFIED (wrong vs ground truth) · CALIBRATED (deliberate-disclosure hit) · EDITORIAL (style/scope, no factual defect) · HOUSTON (policy decision) · QUEUED (recompute-class)

## Claude_brutal / Claude_brutal_INSESSION (byte-identical, `diff -q` verified)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| P5-m1 | MIN | **STALE** | the round's pre-applied fix: tex L1547 now reads "$|z|$ stays below $2\sigma$ (maximum $1.93$" — exactly the reviewer's option (b) |
| P5-N1 | NIT | EDITORIAL | reviewer self-assessed "no action required"; n=406 anchors the canonical scaled build |
| P5-N2 | NIT | EDITORIAL | reviewer self-assessed "no action"; Δ=3 cells = rebuild jitter, volfrac <5.5e-7 |
| 12 all-clears | — | VERIFIED-CONFIRMED | all 26-series FoG/dilation numbers reproduce |

## Gemini_cosmology (0 findings in R26/R27 → 4E this round; each checked against source)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1 | ESS | EDITORIAL/HOUSTON | dev-history/withdrawn prose = standing disclosure policy (recurring class, = Grok E2, OpenAI E1, Pplx E4); journal-strip at submission packaging |
| E2 | ESS | EDITORIAL/HOUSTON | `\artifact{}` paths = campaign-wide reproducibility macro (recurring class) |
| E3 | ESS | **FALSIFIED → hardened** | Table VIII (tex L1699) declares Δf ≡ f_non-void − f_void → +0.0007; reviewer asserted the opposite convention. Defensively, the convention is now restated inline in the abstract (L222 edit) |
| E4 | ESS | **FALSIFIED** | Table III header IS `$|\sigma_{\rm obs}-\sigma_{\rm pred}|$` (tex L952) and caption says "Per-quintile $|\sigma_{\rm obs}-\sigma_{\rm pred}|$"; values 0.13/1.01/1.87/1.01/0.91 are correct absolute residuals. Reviewer misread the rendered bars |
| M1 | MAJ | HOUSTON | companion P4 ships first in publish order (= Pplx E1) |
| M2 | MAJ | **AUTO-FALSIFIED** | arXiv:2604.02463 / 2604.01456 = April 2026 IDs, valid today (recurring future-date class, R27 Gemini-m3 precedent) |
| M3 | MAJ | EDITORIAL/HOUSTON | length/structure (= Grok M1, Pplx E9) |
| N1 | MIN | AUTO-FALSIFIED | "Dated: June 2026" is the real current date; revtex standard |
| N2 | MIN | **STALE** | f_CW^P5 = 0.4972 defined at §V (tex L610), exactly the requested first-use introduction |
| N3 | MIN | STALE | Fig. 8 caption already reads "pixels containing both voids and ≥200 spirals" (L2018) |
| T1 | NIT | HOUSTON | "one breath" phrasing = deliberate R24conf closure |

## Grok_brutal

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1/E2 | ESS | EDITORIAL/HOUSTON | paths + earlier-draft prose (recurring class) |
| E3 | ESS | **FALSIFIED** | abstract L193–199 already states the n=428 V-Web void bin is "sample-size limited… dominated by survey-edge artifacts" and the controlling constraint is DESIVAST n=56,981 — identical to R27 Grok-E1, falsified then too |
| M1 | MAJ | EDITORIAL/HOUSTON | length |
| M2 | MAJ | STALE/PARTIAL | √n non-comparability in abstract, §V (L630–632), Table II/IV/X captions; Tempel Table XI annotation added this session (closing the one gap, = Pplx M15) |
| M3 | MAJ | **FALSIFIED** | inverts the null logic: DESIVAST Δf consistent with zero/monopole IS the result; environment-differential Δf cancels the monopole by construction |
| N1 | MIN | QUEUED-cosmetic | Fig. 1 caption binning pedantry; median is post-dedup (Table I parent) |
| N2 | MIN | **FALSIFIED** | tex L514–517 explicitly states the convention "∂i∂j ↔ (ik_i)(ik_j) = −k_ik_j" and walks the sign chain to +k_ik_jδ_k/k²; R26 META-E1 code-verified closure |
| NIT1 | NIT | QUEUED-cosmetic | figure-regen bundle (axis-label defs) |

## META_REVIEW (gpt-5-pro)

| ID | Sev | Verdict | Disposition |
|---|---|---|---|
| META-E1 | ESS | **VERIFIED → FIXED** | correct point: a 4-bin range is not bounded by a single-bin 2σ. Claim relabeled as descriptive yardstick with explicit pointer to the per-cell empirical p_LEE (Table VI) as the calibrated control (§VII.A edit) |
| META-M1 | MAJ | **VERIFIED → FIXED** | correct: normalized per-pixel z's have variance 1 regardless of N heterogeneity. Rationale rewritten: excess traces 2.7% duplicates + residual selection-function structure, evidenced by the already-published unique-parent std 1.015 (§VIII.F edit) |
| META-M2 | MAJ | STALE/QUEUED | = R27 META-M1/Q3 (pre-existing queue); unique-parent χ²/per-pixel/correlation recomputes already published in-text |
| META-M3 | MAJ | **VERIFIED → FIXED (relabel leg)** | reviewer's option adopted: FoG MC now labeled "fixed-void-geometry membership sensitivity test"; the 36,181/57,081 definition-swap bound (≫ any RSD flip set, 0.6 pp) remains the boundary-motion argument |
| META-M4 | MAJ | STALE/OPINION | = R26 META-m3 precedent: √(N/N_uniq) is a transparent conservative annotation; unique-parent results published as primary cross-checks |
| META-M5 | MAJ | STALE/PARTIAL | abstract already labels Tempel "approximate richness-to-tidal mapping… supporting rather than load-bearing"; cross-survey-different-definition framing present §IX.B |
| META-M6 | MAJ | **VERIFIED → FIXED** | conditioning now stated explicitly in §V: all permutation tests conditional on the matched-sample monopole, unconditional p=0.5 displayed only via analytic σ_from_half |
| META-m1 | MIN | **FALSIFIED** | Table IV caption (L996–1004) already defines ρ̄ = quartile mean of log10(1+δ_smooth), dimensionless, with monotone-transform note + exact-recompute artifact |
| META-m2 | MIN | **FALSIFIED** | label-vs-position permutation equivalence for bin-count statistics is a row-level combinatorial identity (permuting either side of the assignment); duplicates affect calibration (M2 class), not equivalence |

## OpenAI_methodology (pass 1 + pass 2)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1/E2 | ESS | EDITORIAL/HOUSTON | dev-history + paths (recurring class) |
| E3 | ESS | STALE/PARTIAL-QUEUED | tex L1124–1142 already discloses row-level overlap, labels the 2.1σ "approximate", cites the overlap-free unique-galaxy whole-catalog |z|≈2.0, and keeps omnibus tests primary; per-class unique split = queue-class |
| E4 | ESS | STALE/HOUSTON | T-Web/V-Web nomenclature title footnote = deliberate R23conf closure |
| M1 | MAJ | **VERIFIED → FIXED** | real σ misstatement: −0.24 pp at n=185,719 is 2.06σ vs the 0.5/√n floor, not ≤1σ. Text corrected to "≈2.1σ … below the 3σ bar" (§XI edit). Verdict unchanged |
| M2 | MAJ | STALE/PARTIAL | dual P4/P5 monopole references deliberate; §V quantifies the convention difference (<0.01%) |
| M3 | MAJ | STALE | §V.B declares primary path + garden-of-forking-paths bound (R27 precedent) |
| M4 | MAJ | **FALSIFIED** | integer counts in Table II: 203,261/408,187 = 0.497960 → σ = −2.607 → −2.61 ✓; reviewer used the rounded 0.4980 |
| M5 | MAJ | STALE/PARTIAL | = Grok M2 |
| m1–m5/n1–n2 | MIN | FALSIFIED (m2: source is $256^3$) / STALE (m4: Jeffreys Beta(1/2,1/2) at §V L570) / QUEUED-cosmetic (rest) | |
| M6 (p2) | MAJ | **VERIFIED → FIXED** | genuine numeric error: Eq. (2) gives √2 erfc⁻¹(0.05/5) = 2.576 for the DESIVAST Bonferroni-5 family, not 2.81 (which is the α/(2K) value). Fixed 2.81→2.58 + α defined as family-wise (per-bin α/K). All other thresholds (3.09, 2.50, 3.02, 4.05) verify against the corrected definition. Verdict unchanged (all |σ_void| < 2 < 2.58) |
| m6 (p2) | MAJ | **FALSIFIED** | source: `$1 - 0.05^{1/6} = 39\%$` — recurring extraction artifact (R26 OpenAI-E3) |
| m7 (p2) | MAJ | STALE | shared-seed disclosure + distinct-stream re-draw check already in §V (L586–591) |
| m8 (p2) | MAJ | QUEUED-cosmetic | units harmonization = R26 OpenAI-M6 OPINION precedent |
| M7 (p2) | MAJ | CALIBRATED/EDITORIAL | 56,981 = catalog-baseline; exact rerun 57,081 disclosed with invariance shown (L1633); disclosed-baseline convention |
| m9 (p2) | MAJ | **VERIFIED → FIXED** | "0.2 pp concordance spec" was never introduced; reference removed per reviewer's option, leaving the ~0.6 pp two-sample floor statement |
| m10 (p2) | MAJ | **VERIFIED → FIXED** | explicit multiplicity handling added: cluster-quartile monopole-subtracted residuals −1.43/−1.78/+1.27/−0.82, all below Bonferroni-4 (2.50) |

## Perplexity_citations (pass 1 + pass 2)

| ID | Sev | Verdict | Evidence |
|---|---|---|---|
| E1 | ESS | HOUSTON | = Gemini M1 (P4 co-submission) |
| E2 | ESS | STALE/PARTIAL | = Grok M2; Tempel Table XI caption gap closed this session |
| E3 | ESS | **VERIFIED → FIXED** | residual ambiguity real: abstract now carries Δf ≡ f_non-void − f_void = +0.0007 explicitly |
| E4 | ESS | EDITORIAL/HOUSTON | provenance prose class |
| E5 | ESS | **FALSIFIED** (live-web check) | arXiv:2411.00148 resolves to "DESIVAST: A Catalog of Low-Redshift Voids using Data from the DESI DR1 Bright Galaxy Survey" (curl-verified this session) — reviewer's "does not map" is wrong; Planck entry DOES list arXiv:1807.06209 (L2970); 2604.x IDs valid (future-date class); [3]/[4] in-prep = Houston co-submission |
| E6 | ESS | STALE/PARTIAL | convention + sign chain stated L514–517 + title footnote; constants-dropped eigenvalue-ordering note present; fuller Poisson derivation = editorial depth |
| E7 | ESS | **STALE** | §V.B explicitly declares primary vs secondary + multiplicity bookkeeping + descriptive framing for secondary scans |
| E8 | ESS | STALE/PARTIAL | membership spec (hole-union vs maximal-sphere, radii layers) at §VIII.E; boundary sensitivity quantified by 36,181-spiral definition swap (0.6 pp) + FoG MC [−0.34,+0.37] pp; per-Δr boundary-bin table = queue-class refinement |
| E9 | ESS | EDITORIAL/HOUSTON | length |
| M1 | MAJ | STALE/PARTIAL | Table I + abstract ledger numerically consistent (reviewer re-derived and confirmed); 7,815 dropout documented §VIII.F |
| M2 | MAJ | STALE | Table II caption carries √n caveat + monopole framing; §V.B pointer to primary |
| M3 | MAJ | STALE | bright/dark labeled approximate/exploratory with overlap caveat (L1124–1142) |
| M4 | MAJ | **STALE** | §XII.C already carries the exact requested scope caveat: "does not by itself adjudicate Shamir's global (full-sky dipole) anisotropy claim"; "no room" is quantified (2–4 pp required vs <2 pp ranges) |
| M5 | MAJ | STALE | toy EFT labeled schematic (R23–R24 closures) |
| M6 | MAJ | STALE/PARTIAL | shared-provenance 6.6 mas + radius sweep flat to 0.02 pp; analytic chance-alignment estimate = queue-class nicety |
| M7 | MAJ | STALE/QUEUED | randoms rebuild documented w/ α normalization (R26 META-M4 closed-compute) |
| M8/M16 | MAJ | STALE | ASTRA weight capped in abstract ("label disagreement caps its independent statistical weight") |
| M9 | MAJ | EDITORIAL/HOUSTON | figure pruning (Houston wants MORE figures) |
| Min1–5, N1–3 | MIN/NIT | EDITORIAL/HOUSTON (Min5 Zenodo DOI = submission packaging) | |
| E10/M14 (p2) | ESS/MAJ | CALIBRATED/EDITORIAL | = OpenAI M7: baseline-vs-rerun disclosed with invariance |
| M10 (p2) | MAJ | **VERIFIED → FIXED** | real internal sign inconsistency: §VIII.E quoted −0.06 pp (artifact's f_void−f_non-void) against Table VIII's declared convention while L1633 quotes +0.0006 for the same rerun. Passage flipped to declared convention (+0.06/−0.54 pp, z=+0.28/−1.55) with explicit artifact-sign note; verified vs `24_r24conf_pod_session.json` (defA −0.0616, defB +0.5429, z=+1.546) |
| M11 (p2) | MAJ | STALE | se_MC resolution sentence in §V (R26 OpenAI-M3 closure) |
| M12 (p2) | MAJ | STALE | dimensionless log-density stated in Table IV caption |
| M13/M18 (p2) | MAJ | EDITORIAL | structure; catalog-layer distinction paragraph present |
| M15 (p2) | MAJ | **VERIFIED → FIXED** | Tempel Table XI caption lacked the √n annotation other tables carry; added |
| M17 (p2) | MAJ | **VERIFIED → FIXED** | correct: Table XIII prints only 0.5″/5.0″ rows while prose cites 5 radii; parenthetical added directing to the artifact for intermediate rows |

## Score
61 synthesis findings (+ OpenAI/Perplexity pass-1 legs audited in full): **13 VERIFIED → all 13 closed in-session** (META-E1, META-M1, META-M3-relabel, META-M6, OpenAI-M1, OpenAI-M6, OpenAI-m9, OpenAI-m10, Pplx-E3, Pplx-M10, Pplx-M15, Pplx-M17, + Gemini-E3 defensive hardening), 12 FALSIFIED/AUTO-FALSIFIED (incl. all 4 Gemini ESSENTIALs falsified or hardened-only — the precedent skepticism was warranted; and Pplx E5 falsified by live arXiv check), 14 STALE / STALE-PARTIAL, 2 CALIBRATED, rest EDITORIAL/HOUSTON (recurring dev-history/paths/length/companion classes) + 3 QUEUED-cosmetic (figure-regen bundle, units pass — pre-existing queue rows).

**Zero VERIFIED findings remain open. No new recompute-class items**: META-M2 = pre-existing Q3; every other recompute ask is already answered by published 17/22/23/24/25/26-series artifacts. The two genuine numeric errors caught (2.81→2.58 threshold; ≤1σ→2.1σ characterization) move no verdict.

## Round verdict rationale
All 6 legs ran natively (no degraded leg); every ESSENTIAL is falsified, editorial-class (standing Houston disclosure policy), or closed in-session with artifact-backed edits; the 13 verified items are textual and all closed against ground truth; no new recompute queue entries. Recompile clean (see closeout commit).

P5 ROUND VERDICT: CLEAN (0 open verified findings; 13/13 verified items closed in-session; all ESSENTIALs falsified, policy-class, or closed; no new recompute queue; recompiled 28 pp, 0 errors)
