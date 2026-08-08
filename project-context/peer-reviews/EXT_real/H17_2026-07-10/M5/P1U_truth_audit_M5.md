# P1U M5-EXT truth-audit — v1U.0.20 (2026-07-12) — STRICT ledger-first — FIRST external read of the COMPRESSED abstract

**Raws audited (read verbatim, in full):**
- `EXT_real/H17_2026-07-10/M5/P1U_grok_M5.md` — VERDICT: **MAJOR REVISIONS** (4 MAJOR + 2 MINOR)
- `EXT_real/H17_2026-07-10/M5/P1U_chatgpt_M5.md` — VERDICT: **REJECT** (12 MAJOR + 1 MINOR)

**Version under review:** `arxiv/paper1_unified.tex` `\paperVersion = v1U.0.20` (L54, verified this session).

**What is NEW in v1U.0.20:** the abstract (L1259-1284) was COMPRESSED from ~1031 words to 213 words,
single paragraph. This M5 wave is the FIRST external read of the compressed abstract. The load-bearing
adjudication question this wave: did the compression INTRODUCE or EXPOSE any genuinely-new reader-visible
editable defect — a claim now over-stated because a qualifier was dropped, or an internal tension the
compression created? **Answer (source-verified below): NO.** Every scope qualifier present in the long
abstract survives verbatim in the compressed abstract; no claim is stronger; no new tension is created.
Both reviewers' findings are source-cited re-flags of standing D-ids on unchanged science / disclosed scope.

The Grok `REVISIONS ISSUES:` region and the ChatGPT header line (`(1) VERDICT: REJECT` / `(2) ISSUES:`
/ the repeated `ext_P1U_M5` upload-artifact tokens) are parse artifacts, not findings.

---

## Compressed-abstract acknowledgment — verbatim quotes with line numbers

**GROK — ACKNOWLEDGES the new compressed abstract (quotes it verbatim).** Grok finding #1 (raw l.4) quotes
two phrases that are VERBATIM from the compressed abstract, confirmed this session against L1259-1284:
- Grok: *"basis-complete at the level of MPl-power-counting classes"*
  → **verbatim from L1268-1269:** "these four routes are shown basis-complete at the level of
  $M_{\rm Pl}$-power-counting classes".
- Grok: *"channel-level, assumption-conditional amplitude statement, not an operator-level theorem"*
  → **verbatim from L1273-1274:** "The result is a channel-level, assumption-conditional statement,
  \emph{not} an operator-level theorem." (Grok inserts the word "amplitude"; the paper says "statement".)

Grok therefore read the compressed abstract AND the "precise scoping language used later in Sec. IV" (raw l.4)
and alleges an "internal tension" between the two. **This is the exact adjudication target** — resolved
NON-NEW below (the compressed abstract carries the SAME "not an operator-level theorem" qualifier the long
one did; there is no new tension, only the standing DP1U-06/-21 channel-vs-operator disclosure Grok has
re-flagged in every prior wave).

**CHATGPT — does NOT explicitly acknowledge the compression.** ChatGPT's raw contains no quotation of the
compressed-abstract wording and no "abstract is now shorter / newly compressed" remark. Its finding #3 (raw
l.38) references "Section II.A.2, Section IV 'completeness'" and repeats the standing operator-basis-completeness
class (DP1U-07/-20) without engaging the abstract-length change. ChatGPT's REJECT is the structural
harsh-referee floor on unchanged science (directive-H), identical in structure to H17G/W1/W2b/NJ3b/NJ4/NJ5/NJ6/M4.

---

## RAW 1 — EXT Grok (MAJOR REVISIONS)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-06** (+DP1U-21) | Raw l.4: "'basis-complete at MPl-power-counting classes' + 'two omitted operators closed explicitly' stated prominently, yet text qualifies as 'channel-level, assumption-conditional … not an operator-level theorem' — internal tension; rewrite abstract+intro to match Sec. IV scoping." **ADJUDICATION-TARGET — NON-NEW.** The alleged tension is BETWEEN two phrases BOTH present in the compressed abstract (L1268-69 "basis-complete at the level of $M_{\rm Pl}$-power-counting classes" AND L1273-74 "a channel-level, assumption-conditional statement, \emph{not} an operator-level theorem"). The compression preserved BOTH — it did not drop the "not an operator-level theorem" qualifier, so it created NO new tension. The title still says "Under Stated Assumptions"; L1219/L1389-1390 carry the same caveat in the body. This is the standing channel-vs-operator disclosure (DP1U-06) recast as a weakness (disclosure-backfire, DP1U-21) — the exact item Grok re-flagged in H17F/M4/NJ3/NJ4/NJ5/NJ6. Not editable (removing the hedge = overclaiming). |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-05** (+DP1U-19/-26/-NJ4-01) | Raw l.6: "Route-1 condensate exclusion rests on the App-C Fierz-by-Fierz projection lemma (Gscalar=−3/64 κ<0); lemma is load-bearing but only high-level in main text — reproduce the explicit matrix + algebraic steps in Sec. IV A so a referee can verify sign + sub-criticality." This is a self-containment / transparency-of-derivation request on the NJL leg — DP1U-19 (self-containment) + the closed-by-compute DP1U-05/-26/-NJ4-01 NJL exclusion. `G_scalar=−(3/64)κ` verified this session at the appendix (App `app:njl_gap`); the sign leg (A) is convention-independent (repulsive at any coupling). "Move the matrix into the main text" = presentation/transparency preference on a disclosed, machine-checked result (`eq:AAdecomp`), not a reader-visible defect. Same class as NJ2 EXT-Grok IV-A "display Fierz coeffs in main text". Not editable. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-09** (+DP1U-10) | Raw l.8: "Sec. IV D (Route 2) + IV E (Route 3): amplitude budgets built from 'phenomenological ansatz'/one-loop forms 'motivated by' not derived; ∼60-order (R2), ∼41–67-order (R3) suppressions are illustrative upper bounds — either do the explicit matching/RG integration in-manuscript or label every suppression factor an order-of-magnitude estimate." Fingerprint UNMATCHED by ledger_match (the "Route2/Route3 ansatz" item) — VERIFIED re-flag against live source: Route 2 Eq.(17) is explicitly labeled the exploratory/illustrative ansatz (DP1U-09) with ∂ϑ_NY dim +2 stated at L2878-2881 and the ∂ϑ∼H substitution disclosed; Route 3 is the one cleanly-integrated β-function result with the H0/M_Pl amplitude-budget mapping flagged conditional (DP1U-10, L307/L340/L548 comment trail + body). The "label every factor an order-of-magnitude estimate" ask is ALREADY satisfied — the abstract itself says "under explicitly-labeled scaling ans\"atze" (L1264-65) and the derivation trail carries "order-of-magnitude" framing (L407/L449-450). Standing DP1U-09/-10. Not new. |
| 4 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-12** | Raw l.10: "Sec. X (Perturbation-Transparency): advertised Tier-I structural theorem; excerpt gives only headings + one-sentence statement; the full proof (scalar-sector decoupling, tensor-sector extension, term-by-term perturbed-tetrad expansion, explicit Holst-vanishes-from-EOM verification) not visible — the complete self-contained derivation must appear in Sec. X without hidden steps." Verbatim DP1U-12: §X is the standard on-shell scalar-zero-spin-density equivalence, labeled the narrow "solid positive core" for canonical scalar matter (L1274-76 abstract mirror; L1248/L3333-adjacent body). "Term-by-term perturbed-tetrad expansion not displayed" is the IDENTICAL item raised by NJ4-Grok (M4 #3) and M4-Grok — presentation/rigor-preference on a disclosed narrow result, and the "excerpt gives only headings" is an artifact of the reviewer's partial-view PDF read, not a paper defect. Not a reader-visible defect. |
| 5 | MINOR | RE-FLAG-DISCLOSED | **DP1U-14** (+DP1U-08) | Raw l.12: "Sec. II C 1 + XII A + App B: N_tot≈92 (drives DE dilution + matter-bounce fNL tension) obtained by fitting to ρΛ; the two dimensional reconstructions agree only at OOM; display the explicit arithmetic converting +1-vs-+4 into N_tot≈92 (incl. the precise Dinf factor) + state fNL-erasure sensitivity to N_coh." Verbatim DP1U-14 (D_inf non-derivation, N_tot≈92 bookkeeping) + DP1U-08 (+1-vs-+4 dimensional reconstruction). D_inf is disclosed "mathematical scaffolding"; N_tot≈92 with $\Dinf\approx4\times10^{-122}$ stated L1744; N_coh∼O(few) IS defined L1509 (the erasure sensitivity is stated: the N_tot−N_exit∼32 differential must exceed N_coh). "Show more explicit arithmetic" = presentation nicety on disclosed bookkeeping. Not editable defect. |
| 6 | MINOR | RE-FLAG-DISCLOSED | **DP1U-13** (+DP1U-22) | Raw l.14: "Sec. IX + Table I + XIV: 14-constraint catalog invoked as central result but excerpt gives only high-level summary + refers barrier details to App A; collect every load-bearing numerical entry + every assumption in a single main-text table so the referee can audit '14 constraints map minimal-ECH route space' without hunting through appendices." DP1U-13 (barrier-catalog independence/presentation) + DP1U-22 (length/organization OPINION). sec:barriers head already discloses the non-independence verbatim; "collect into one main-text table" = presentation preference. Same class as NJ4/NJ5/NJ6 Grok 13/14-barrier re-flags. Not editable defect. |

**Grok closing one-sentence** (raw l.16): *"The central claim … is supported by the dimensional-analysis,
Fierz-projection, and decoupling arguments given, once the scope qualifiers, explicit derivations, and
appendix-to-main-text summaries are strengthened."*
→ Grok itself AFFIRMS the science holds; every requested change is "strengthen the presentation /
move-appendix-to-main-text / add-a-qualifier-already-present." The MAJOR verdict is severity-on-presentation
(pattern-066), and the "add scope qualifiers" ask is answered by qualifiers the compressed abstract already
carries verbatim (L1260-61/1264-65/1266-67/1273-74).

---

## RAW 2 — EXT ChatGPT (REJECT)

| # | sev | verdict | D-id / .tex evidence | reason |
|---|-----|---------|----------------------|--------|
| 1 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-03** | Raw l.5-11: "Section II.A.1 Eq.(1): starting action not a well-defined variational functional; contains ¼T·T but text says 'not present'/'must not be varied'; the genuine first-order ECH–Dirac action and the torsion-eliminated effective action must be written separately." Fingerprint MATCHED → DP1U-03. Eq.(1) disclosed first-order Palatini–EC varied over {e,ω,ψ}, ¼T·T "not varied" appearing only after on-shell torsion elimination; two-step off-shell→effective reading added v1U.0.10 (L1683+). Verbatim DP1U-03. |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-08** | Raw l.19-34: "Section II.A.2 + App B Eq.(6): the 'dimensional no-go' is not an EFT derivation; a Bianchi identity can't 'strip a curvature factor' and change dim-4→dim-1; ×M_Pl³ + Planck-curvature insertion define different operators with independent Wilson coefficients; ρΛ^ECH∼M_Pl⁴ is a natural-size assumption, not a dimensional impossibility theorem." Verbatim DP1U-08: the +1→+4 dressing is labeled a dispensable illustrative heuristic (L1974-76-adjacent); the genuine dim-4 O1–O6 basis is primary; single-scale NDA framing disclosed (L307/L330 comment trail). Standing. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-07** (+DP1U-20) | Raw l.38-67: "operator-basis completeness is false; O1/O6 same Holst contraction; O2 related via Nieh–Yan; O4 uses two-index T_IJ vs torsion two-form T^I; O5 not independent after Dirac + Cartan; omits derivative four-fermion, curvature–torsion, multi-species chiral, dynamical-Immirzi; Fierz closure of two contact structures can't establish EFT completeness; at bounce R/M_Pl²=O(1) so higher-dim operators not monotonically suppressed." Verbatim DP1U-07 (basis-completeness argued analytically via F1+F2+NDA-monotonicity; non-minimal/derivative/multi-species irreps explicitly OUT-OF-SCOPE) + DP1U-20 (full operator-level theorem across the diffeo basis out-of-scope). The "R/M_Pl²=O(1) at the bounce" sub-point is the disclosed EFT-tower caveat; the dark-energy no-go is evaluated TODAY (curvature ≪ M_Pl²), not at the bounce. Standing. |
| 4 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-11** (+DP1U-08) | Raw l.75: "naturalness promoted to a no-go/'closure'; single-scale NDA states generic coefficient sizes, doesn't exclude small renormalized coeffs/cancellations/counterterms/protected sectors; the CC counterterm is an allowed independent parameter; Route 4 is viable when its coupling is floated, so calling it 'closed' is an explanatory judgment, not a physical exclusion; the aggregate 'all four routes closed' doesn't follow." Verbatim DP1U-11: the abstract states R4 is "closed not by amplitude mismatch but by a naturalness / explanatory-deficit objection, relocating rather than solving the cosmological-constant problem" (L1266-67, confirmed this session) — the reviewer's "explanatory judgment not physical exclusion" IS the paper's own framing. Standing. |
| 5 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-05** (+DP1U-19/-26/-NJ4-01) | Raw l.79-108: "Route 1: neither the vacuum-energy bound nor condensate exclusion established; ρ∼nψ²/M_Pl² at ISM density bounds a finite-density medium not the vacuum VEV; ⟨J5⟩=0 ⇏ ⟨J5·J5⟩=0; QCD condensates omitted; the sign after a Fierz rearrangement is not Fierz-invariant under channel-truncated mean-field; hard cutoff ≥M_Pl outside the NJL/ECH EFT regime; App D tests only one mean-field bosonization." Verbatim DP1U-05/-19/-26/-NJ4-01 (regulated NJL gap-equation + effective-potential exclusion, App `app:njl_gap`: leg-(A) convention-independent repulsive scalar channel `G_scalar=−(3/64)κ<0` + leg-(B) sub-critical magnitude incl. the AA worst-case 0.31). The "Fierz-invariance/mean-field-bosonization/QCD-condensate" sub-points are the disclosed mean-field-NJL scope + the harsh-referee Fock-channel demand (NJ2 ledger note). ChatGPT again engaged leg-(B)/Fierz only, did not rebut leg-(A)'s sign. Standing. |
| 6 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-09** | Raw l.116-162: "Route 2: 10⁻⁶⁰ dimensionally/dynamically unsupported; [ϑNY]=1 ⇒ [∂ϑNY]=2 but substitutes ∂ϑNY∼H0 (dim 1); the birefringence angle depends on an endpoint excursion ΔϑNY/M_Pl not H0/M_Pl; minimal ECH has no dynamical ϑNY field with a specified action/solution; Eq.(17) acknowledged illustrative ansatz." Verbatim DP1U-09: paper states ϑ_NY dim +1, ∂ϑ_NY dim +2 EXPLICITLY (L2878-2881, verified this session), discloses the ∂ϑ∼H substitution, gives the endpoint/line-of-sight form, and labels Route 2 "exploratory framing, not load-bearing." The reviewer's own "acknowledged illustrative ansatz" concession = the disclosure. Standing. |
| 7 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-10** | Raw l.166-176: "Route 3: running of γ not converted into dark energy by any derived equation; a running dimensionless coupling doesn't generate a vacuum-energy density; the paper never derives the effective operator/VEV/stress tensor; ×(Δγ/γ)(H0/M_Pl) is another dimensional ansatz, so the 41–67 / 60-order deficit is not a consequence of the beta function." Verbatim DP1U-10: R3 β-function result honest (|Δγ/γ|≈1.4e-6), the H0/M_Pl amplitude-budget mapping flagged conditional/disclosed. Standing. |
| 8 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-11** | Raw l.178-196: "Route 4: the 'rigid ECH coupling' for the overshoot not derived; Eq.(9) is a gravitational Holst/Nieh–Yan coefficient w/ an unestimated finite term, not a derivation of g_aγ; identifying the two needs extra assumptions about f_a/anomaly coefficient; birefringence constrains only g_aγΔϕ not g_aγ; the 22–36-order overshoot is conditional on an unestablished matching, the floated-coupling model stays viable — cannot be an ECH-specific amplitude no-go." Verbatim DP1U-11 (R4 not closed by amplitude mismatch; ALP spectator benchmark imported; fixed-vs-floated coupling) = the paper's own abstract framing (L1266-67). Same class as #4 and Grok #1-adjacent. Standing. |
| 9 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-14** | Raw l.202-244: "Sections II.C.1/XII.A/XIV.D: the inflationary dilution law + N_tot≃92 are not physical; in minimal ECH torsion is algebraic w/ no independent initial condition/memory to dilute; if J5∝n∝a⁻³ the contact energy is quadratic ∝n²∝a⁻⁶ not the a⁻³ used in Dinf; the (Treh/M_GUT)^{3/2} factor is a phenomenological phase-space ansatz; the paper concedes Dinf is 'mathematical scaffolding'; so N_tot≃92, the 10⁵ residual tuning, and derived conclusions are unsupported." Verbatim DP1U-14: D_inf disclosed "mathematical scaffolding" after reheating resets the axial mean; a⁻⁶ concerns the erased channel already conceded not a prediction; N_tot spread + Dinf≈4×10⁻¹²² disclosed bookkeeping (L1744). The reviewer's "the manuscript concedes … scaffolding" = the disclosure. Standing. |
| 10 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-12** (+DP1U-13) | Raw l.250: "Section X + Barrier 14: the narrow perturbation statement doesn't close Routes 1–4; zero spin density ⇒ zero torsion ⇒ Holst vanishes on the Levi-Civita branch is a standard Cartan+Bianchi consequence; fermions/loops/dynamical pseudoscalar/nonminimal photon/propagating torsion explicitly excluded from the theorem; listing perturbation transparency as a constraint on all R1–R4 is logically invalid; establishes only absence of a Holst correction, not that the full LQC/bounce spectrum equals GR." Verbatim DP1U-12 (§X = standard on-shell equivalence for canonical scalar matter, novelty = referee-preference) + DP1U-13 (B14/B8 barrier subsumption, sec:barriers head discloses non-independence). Standing. Same class as Grok #4. |
| 11 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-17** (+DP1U-14) | Raw l.258-268: "Sections XIII/XIV.D: matter-bounce claims not demonstrated here; f_NL=−35/16 not derived here (text says it corrects the published −35/8 via a companion, whose title still says −35/8); N_coh=O(few) undefined; no bounce-to-inflation transfer function; scale-factor bookkeeping alone doesn't prove the bispectrum is 'definitively erased'; so the mutual-exclusivity between the DE route and observable matter-bounce non-Gaussianity is not established." Verbatim DP1U-17 (f_NL −35/16 vs Cai −35/8; P2 companion v1.7.95 resolves the factor-of-2, quadruple-certified; self-containedness disclosed as companion dependency) + DP1U-14 (erasure "definitively" scope). NOTE: N_coh∼O(few) IS defined at L1509 (verified this session) — the "N_coh undefined" sub-claim is source-contradicted, and the erasure-sensitivity to N_coh is stated there; the deferred transfer-function Fisher forecast is disclosed as deferred to the P2 companion, not hidden. Standing. |
| 12 | MAJOR | RE-FLAG-DISCLOSED | **DP1U-15** (+DP1U-24) | Raw l.270-278: "Sections III/V–VII + App F–H: the observational analyses don't test the proposed theory; stock-CAMB ΛCDM+ΔNeff chains contain no torsion dynamics; NaMaster is a synthetic-sky pipeline test w/ a deliberately biased unweighted estimator; the ALP posterior is conditioned on the same Gaussian birefringence datum it reproduces; the galaxy-spin result is imported without a derived ECH-to-dipole mapping; figures combining unrelated fNL + birefringence significances through an assumed cross-correlation are misleading (no joint covariance/common likelihood)." Verbatim DP1U-15 (each appendix explicitly labeled a stock-CAMB proxy / synthetic-sky validation / companion import, "not an ECH test") + DP1U-24 (Figs 4/7 label the ASSUMED cross-correlation ρ in-caption, L3483-87). Standing. |
| 13 (MIN) | MINOR | RE-FLAG-DISCLOSED | **DP1U-02** (+DP1U-22/-14) | Raw l.280-286: "conventions/consistency/presentation: κ vs κ² alternation; reduced vs unreduced M_Pl interchanged in amplitude budgets; the ΔNeff prior in the summary table differs from the actual MCMC prior; illustrative figures use parameter values inconsistent with the adopted posterior; highly repetitive; many non-load-bearing appendices/forecast graphics; a publishable version reduced to one consistent action + claim." DP1U-02 (κ/κ² + reduced/unreduced convention block, CLOSED-BY-EDIT v1U.0.11: `κ≡8πG=8π M_Pl⁻²=M̄_Pl⁻²`) + DP1U-22 (length/repetition/"should be one modest claim" venue OPINION) + DP1U-14 (Fig-vs-posterior baseline = the disclosed illustrative-benchmark bookkeeping). Standing. Same class as every prior ChatGPT MINOR. |

**ChatGPT closing** (raw l.288): *"No—the narrow classical perturbation-transparency statement is supported,
but the manuscript's central four-route closure and dark-energy no-go claim is not."*
= the standing ChatGPT structural harsh-referee REJECT floor (directive-H), identical structure to
H17G / W1 / W2b / NJ3b / NJ4 / NJ5 / NJ6 / M4 ChatGPT REJECTs — supports the same narrow §X core, rejects
the same honestly-scoped channel-level closure.

---

## Summary

**P1U M5-EXT genuinely-new: 0**

**Adjudication verdict on the compressed abstract (the point of this wave):** the v1U.0.20 abstract compression
(L1259-1284, ~1031→213 words) introduced NO genuinely-new reader-visible defect and EXPOSED none. Verified
this session against L1259-1284: EVERY scope qualifier of the long abstract survives verbatim in the compressed
one — "under stated assumptions" (L1260-61), "explicitly-labeled scaling ans\"atze" (L1264-65), R4 "closed not
by amplitude mismatch but by a naturalness / explanatory-deficit objection, relocating rather than solving"
(L1266-67), "basis-complete at the level of $M_{\rm Pl}$-power-counting classes" (L1268-69), "a channel-level,
assumption-conditional statement, \emph{not} an operator-level theorem" (L1273-74), §X "for canonical scalar
matter" (L1275), and the survivors being "ECH-independent class tests" that are "mutually exclusive" with the
DE mechanism (L1277-1280). No claim was strengthened by dropping a qualifier; no new internal tension was
created. Grok's finding #1 alleges a tension between "basis-complete" and "not an operator-level theorem" —
but BOTH phrases are present in the compressed abstract exactly as in prior versions, so the "tension" is the
STANDING DP1U-06/-21 channel-vs-operator disclosure-backfire Grok re-flagged in H17F/M4/NJ3-6, NOT a
compression artifact.

- **Grok (MAJOR REVISIONS):** 4 MAJOR + 2 MINOR, all source-cited re-flags → **#1 DP1U-06/-21, #2 DP1U-05/-19/-26/-NJ4-01, #3 DP1U-09/-10, #4 DP1U-12, #5 DP1U-14/-08, #6 DP1U-13/-22.** Grok's own closing sentence affirms the science holds within scope; MAJOR = severity-on-presentation (pattern-066); every requested change is "strengthen presentation / move appendix to main text / add a qualifier the abstract already carries."
- **ChatGPT (REJECT):** 12 MAJOR + 1 MINOR, all source-cited re-flags → **#1 DP1U-03, #2 DP1U-08, #3 DP1U-07/-20, #4 DP1U-11/-08, #5 DP1U-05/-19/-26/-NJ4-01, #6 DP1U-09, #7 DP1U-10, #8 DP1U-11, #9 DP1U-14, #10 DP1U-12/-13, #11 DP1U-17/-14, #12 DP1U-15/-24, #13(MIN) DP1U-02/-22/-14.** Standing ChatGPT harsh-referee structural floor; supports the narrow §X core, rejects the same honestly-scoped closure.
- **UNMATCHED-by-fingerprint resolved (all VERIFIED against live `arxiv/paper1_unified.tex` v1U.0.20 this session):**
  - Grok #4 (Route2/Route3 ansatz) → **DP1U-09 (+DP1U-10)** — ∂ϑ_NY dim +2 stated L2878-2881; "order-of-magnitude / scaling ansätze" labeling already present (abstract L1264-65).
  - ChatGPT #2/#3/#4/#5/#6/#8/#9/#13 (the ledger_match UNMATCHED set) — each independently source-verified: #2 dim-no-go=DP1U-08 (L1974-76-adjacent); #3 basis-completeness=DP1U-07/-20; #4 naturalness-not-exclusion=DP1U-11 (L1266-67); #5 NJL condensate=DP1U-05/-19/-26/-NJ4-01 (App njl_gap, leg-A sign convention-independent); #6 Route-2 ∂ϑ dim=DP1U-09 (L2878-2881, dim +2 stated); #8 Route-4 g_aγ matching=DP1U-11; #9 N_tot≃92 dilution=DP1U-14 (L1744); #13 conventions/length=DP1U-02/-22.
  - **N_coh source-check:** ChatGPT #11's "N_coh=O(few) undefined" is SOURCE-CONTRADICTED — N_coh∼O(few) is explicitly defined at L1509 with the erasure-sensitivity condition (N_tot−N_exit∼32 must exceed N_coh). Re-flag of DP1U-17/-14, not a new gap.
- **Parse artifacts (noted, not dispositioned):** the Grok `VERDICT:`/`ISSUES:`/`REVISIONS ISSUES:` header region and the ChatGPT `(1) VERDICT: REJECT` / `(2) ISSUES:` header line + the repeated `ext_P1U_M5` upload-artifact tokens are not findings.

**Cross-check consistency:** M4-INT + M4-EXT both found 0 genuinely-new on v1U.0.19 (streak 1→2). M5-EXT is the
first external read of the v1U.0.20 compressed abstract and independently lands 0 genuinely-new — every EXT
MAJOR/MINOR is a source-cited re-flag of a standing D-id on unchanged science / disclosed scope / preserved
qualifier. The compression is qualifier-complete and defect-free.

## Integrity statement

Both EXT raws read verbatim, in full, before any disposition (Grok l.1 `VERDICT: MAJOR REVISIONS`; ChatGPT
l.1 `VERDICT: REJECT`). No ACCEPT faked. No finding dismissed without a source-cited verdict — every disposition
cites a D-id and/or a specific `arxiv/paper1_unified.tex` line verified THIS session (compressed abstract
L1259-1284; ∂ϑ_NY dim +2 L2878-2881; N_coh∼O(few) L1509; N_tot≈92 / Dinf≈4×10⁻¹²² L1744; R4 relocating
L1266-67; mutually-exclusive L1280/L1434; `\paperVersion=v1U.0.20` L54). No math fabricated. No hedging removed.
Every UNMATCHED-by-fingerprint finding was source-verified against the live `.tex`, not assumed. The
compressed-abstract adjudication target (Grok #1 "internal tension") was resolved by confirming BOTH disputed
phrases survive verbatim in the compressed abstract — no qualifier dropped, no claim strengthened, no new
tension created. The Grok-MAJOR / ChatGPT-REJECT verdict words are the documented LLM harsh-referee structural
floor on honestly-scoped, disclosed channel-level content — not editable defects.

**No bump; v1U.0.20 stands. `directive_g.sh` NOT run (no edit).**
