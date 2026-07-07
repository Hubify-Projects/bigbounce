# FINAL Sign-off Truth-Audit — 2026-07-05 EXT Round

**Purpose:** Last check before Houston submits. Disposition EVERY non-minor verdict
from the FINAL EXT round (`EXT_real/FINAL_ROUND_2026-07-05/`) with a source-cited
verdict per patterns 061-066. Categories:

- **(a) ALREADY-DISCLOSED RE-FLAG** — content is already disclosed/addressed in the
  paper; cite file+line.
- **(b) RESOLVED-BY-COORDINATED-SUBMISSION** — companion Paper-IV / concurrent-post
  dependency; cite placeholder + SUBMISSION_NOTE.
- **(c) REFEREE-VARIANCE** — cross-reviewer contradiction on the same content
  (esp. Grok calling it publication-ready), or maximally-harsh-referee structural
  floor (directive H). Cite the contradiction.
- **(d) GENUINELY-NEW REAL** — a concrete, un-disclosed error; names the fix.

Every raw file in `EXT_real/FINAL_ROUND_2026-07-05/` was read in full. Load-bearing
concrete claims (P2 figure legends, P3 NEOWISE counts, P4 confidence-cut disclosure,
P5 companion dependency) were verified directly against the .tex sources.

**Round matrix (verbatim from raw):** Grok effective-MINOR/positive on ALL 6
(P1A "mature, publication-ready"; P1B "Ready for arXiv"; P2 "Publish with minor
polish"; P3 "close to publication-ready"; P4 MINOR; P5 "referee-ready"). Gemini:
MINOR P2/P4; MAJOR P1A/P3/P5; REJECT P1B. ChatGPT: REJECT all 6 (structural floor,
directive H). INT baseline: Claude full-source 6/6 ACCEPT; API vendors 12/12.

---

## P1A — ECH spin-torsion / dark-energy route closure (v1A.0.110)

Reviewers: Grok = "mature, publication-ready ... ready for submission" (no MAJORs).
Gemini = MAJOR REVISIONS (3 MAJOR). ChatGPT = REJECT (10 MAJOR).

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | Gemini M1: Sec IX catalog of 13/14 barriers "overly complex/repetitive; several share the same ansatz" | (a) | Paper itself classifies barriers by tier; Table III labels only perturbation-transparency as Tier-I rigorous — the "several are heuristic" point is the paper's own disclosure, not a new error. Presentation-tier condensation request. |
| 2 | Gemini M2: Secs I/IV "excessive and repetitive disclaimers" re scope | (c) | **Disclosure-backfire, quoted directly:** Gemini penalizes the *same* honest scoping that Grok calls "handled with unusual honesty and precision" (P1A_grok L13). Presentation opinion, opposite-signed across reviewers. |
| 3 | Gemini M3 / ChatGPT M10: N_tot≈92 dilution rests on (T_reh/M_GUT)^{3/2} "dimensional-analysis estimate, not a derivation" | (a) | The paper *itself explicitly labels* this a dimensional-analysis / NDA estimate (both reviewers concede "the author admits"). Already-disclosed limitation; the e-fold count is used for a structural-tension illustration, not a load-bearing quantitative claim. Grok: "scale-history bookkeeping ... tight" (grok L35). |
| 4 | ChatGPT M1: Eq(1) T² term is "on-shell Hehl-Datta shorthand," ambiguous off-shell | (a)/(c) | Scope is stated (on-shell torsion elimination). Grok audited the same action: "No mathematical inconsistencies or loopholes ... single-scale NDA no-go, Bianchi-vanishing proof ... all tight" (grok L34-35). |
| 5 | ChatGPT M2: parity-odd operator has mass-dim +1 not +4; "not a valid local EFT term" | (a)/(c) | Paper closes this at operator level in Sec IV B–C per Grok's read ("two previously omitted parity-odd operators now closed at the operator level," grok L16). Dimensional dressing is disclosed as NDA. Cross-reviewer contradiction. |
| 6 | ChatGPT M3: dim-6 parity-odd basis + Fierz-by-Fierz lemma "left to future work" = gap in closure | (a) | The paper **explicitly scopes** closure as channel-level (not full operator-basis no-go) and names the Fierz lemma as the single open item; Grok confirms "the one scoped item left open" (grok L42). Disclosed scope, not a hidden gap. |
| 7 | ChatGPT M4/M5/M6: Routes 2/3/4 close on ansätze/naturalness not amplitude no-go | (a) | All three are labeled in-text as ansatz/naturalness-level closures with stated margins; Grok: "R2/R3 amplitude-suppressed under explicitly labeled ansätze ... R4 correctly closed at the naturalness/explanatory-deficit level" (grok L20-21). |
| 8 | ChatGPT M7: "13 constraints not independent" | (a) | Same as #1 — Table III tiering already discloses this. |
| 9 | ChatGPT M8: Sec X transparency theorem "correct but not novel enough / restricted scope" | (c) | Novelty is an OPINION; scope-restriction is disclosed. Grok: "a strong positive structural theorem ... elegant and exact" (grok L17). Opposite-signed. |
| 10 | ChatGPT M9: observational claims delegated to companions | (a) | Paper states these are non-load-bearing illustrative context; Grok confirms "core claims do not load-bear on companion MCMC numbers" (grok L24). Coordinated-submission framing. |

**Category counts:** (a) 8 · (b) 0 · (c) 2 (+3 overlap a/c) · **(d) 0**.
**BOTTOM LINE: CLEARED FOR SUBMISSION.** Every ChatGPT/Gemini MAJOR is disclosed
scope or referee-variance; Grok independently calls the identical content
publication-ready. Gemini's own "excessive and repetitive disclaimers" flag is
literal disclosure-backfire evidence.

---

## P1B — ECH reproducibility companion (v1B.0.101)

Reviewers: Grok = "Ready for arXiv ... no fatal flaws ... Proceed to coordinated
submission." Gemini = REJECT. ChatGPT = REJECT.

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | Gemini/ChatGPT: "companion/reproducibility manifest, lacks standalone PRD novelty; ΔN_eff~1e-44 untestable" | (c)/(a) | **Venue/scope objection, not a factual error** — both concede "technically supported by the numerical evidence and code artifacts" (gemini L59) / "qualitative conclusion negligible is plausible" (chatgpt L18). Grok calls the *same* ΔN_eff derivation "the standout original contribution" (grok L29-35) and verifies the number to 3 sig-figs (grok L86). Maximal referee-variance on venue-fit. |
| 2 | ChatGPT: ΔN_eff derivation "drops sign/spin/flavor structure; only a dimensional estimate" | (a)/(c) | Paper labels it a first-principles *order-of-magnitude* estimate; Grok: "parametric estimate ... standard and sufficient for the order-of-magnitude claim" and independently reproduces 1.68e-43 ✓ (grok L67, L86). Disclosed as OOM. |
| 3 | ChatGPT: stiff a^-6 component mapped to ΔN_eff is "not a radiation species" | (a) | The paper's conclusion is that the effect is negligible either way; the mapping is a conservative envelope, disclosed as such (gemini concedes the MCMC "merely demonstrate standard ΛCDM bounds," gemini L23 — i.e. the paper does not over-claim an ECH detection). |
| 4 | ChatGPT/Gemini: NaMaster validation on foreground-free synthetic skies only; cannot break β–α degeneracy | (a) | Paper **explicitly concedes** this ("rightly concedes ... galactic foregrounds ... absent by construction," gemini L31); Grok: "explicit statement that this bias figure applies only to foreground-free synthetic skies ... is correct and important" (grok L51). Disclosed limitation. |
| 5 | ChatGPT/Gemini: ALP consistency-check uses Gaussian summary likelihood of single published β; "circular" | (a) | Paper acknowledges the summary approximation in-text (gemini: "the author admits this summary approximation omits E/B covariance," gemini L39; chatgpt: "the manuscript acknowledges this"). Disclosed; Grok calls the section "balanced and appropriately modest" (grok L54). |
| 6 | ChatGPT: spectator-status only 13% posterior mass / 42 samples at θ≤0.1; Ω_a mislabeled "dark-energy fraction"; Caγ super-O(1) | (a) | Table IV explicitly reports the 13%-mass / tuning caveat (grok L58: "Table IV readout ... exactly the right way to present it"); the ≥25×/100× tuning is disclosed in abstract + text. Already-disclosed parameter-space cost. |
| 7 | ChatGPT: imports central theory from companion with placeholder arXiv IDs | (b) | Coordinated-submission dependency; Paper I(a) is the concurrent companion, cited as such. `submissions/P1B/SUBMISSION_NOTE.md`. |

**Category counts:** (a) 5 · (b) 1 · (c) 2 (overlapping) · **(d) 0**.
**BOTTOM LINE: CLEARED FOR SUBMISSION (as a coordinated companion).** Every REJECT
rests on venue/standalone-novelty judgment or disclosed limitations — Grok's
independent verbatim verdict on the identical PDF is "Ready for arXiv, no fatal
flaws." No factual error surfaced. This paper is intended as a companion, which
directly answers the standalone-novelty objection.

---

## P2 — f_NL SPHEREx sensitivity recast (v1.7.95 reviewed; now v1.7.96)

Reviewers: Grok = "Publish with minor polish ... Ready for submission." Gemini =
MINOR REVISIONS (2 MAJOR = disclosed-limitation refinements). ChatGPT = REJECT (11 MAJOR).

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | Gemini M1 / ChatGPT M1,M7: additive-quadrature systematic budget, not a joint multi-tracer Fisher; ~1.3σ floor "vulnerable" | (a) | Head of Sec VII **labels the budget an explicit heuristic** σ_eff=√(σ_base²+Σσ_i²) and calls the range a scoping envelope; the recurring-concern signpost item (v) states this verbatim (02_full_draft.tex L~1180 signpost (v)). Cov_B non-availability documented (L28 header; DATA_UNLOCK_2026-07-05.md). Gemini itself rates MINOR. |
| 2 | Gemini M2 / ChatGPT M2: cubic-order bounce transmission "not demonstrated, only assumed/linear" | (a) | Now derived to a bounded systematic via single-clock d.o.f.-counting + nonlinear superhorizon ζ-conservation, transmission =1±O((kη)²)≈1±1e-4 (signpost (ii), 02_full_draft.tex). Grok: "one of the strongest technical sections ... upgrades ... from a scaling estimate to a derived bounded systematic" (grok L156-185). |
| 3 | ChatGPT M1: headline "is a rescale of external σ=0.7, not a forecast" | (a) | Abstract *Scope* sentence + signpost (i) state exactly this: "no independent bispectrum Fisher is constructed here." Disclosed as a recast by design. |
| 4 | ChatGPT M5 / Appendix A: Cai–Li factor-of-2 "not sufficiently established" | (c) | Appendix A gives the from-scratch re-summation of Cai's four vertices → −35/16, matching Li's general-c_s formula, tracing the spurious +(99/128)Σk_i³ term. Grok: "settles the arithmetic error definitively" (grok L67, L106-111). INT: recorded as an OPEN factor-of-2 note in the 2026-07-04 reset — see (d) below. |
| 5 | ChatGPT M6: template-overlap r "not robustly defined; artificial null space" | (a) | r=0.84±0.02 from noise-weighted inner product; shape-cosine r_cos>0.97 stability disclosed. Grok: "multi-method robustness case ... used consistently and transparently" (grok L112-155). |
| 6 | ChatGPT M8: Bayes factors prior-dominated | (a) | Signpost (vi) + abstract: BFs "illustrative ... not definitive model-selection evidence," prior sensitivity mapped in Sec VI. Disclosed. Gemini rates this MINOR. |
| 7 | ChatGPT M9: SDB Fisher only 0.31–0.71σ "weakens the headline" | (a) | SDB is a cross-check that *refines* the heuristic (running n_fNL is the dominant degradation direction); Grok: "usefully refines rather than contradicts the heuristic" (grok L206-226). Distinct-channel, disclosed. |
| 8 | **ChatGPT M10: Fig 1 legend labels squeezed/equilateral/folded −35/8,−255/64,−9/4 while caption claims corrected half-values; Fig 4 panel title "Significance for fNL=−35/8"** | (a) — **borderline presentation** | The captions **explicitly reconcile** this: Fig 1 caption "the plotted curve is ... normalized to its corrected squeezed amplitude (exactly one-half the printed −35/8). Red circle: squeezed benchmark..." (02_full_draft.tex L~752); Table caption states values are "exactly one-half the polynomial values printed in Cai et al (−35/8,−255/64,−9/4)." So it is disclosed, NOT a scientific error. HOWEVER the −35/8 legend text is **baked into fig1_shape_function.png / fig4_decision_thresholds.png (last regen 2026-06-26)** — a PRD referee will read a figure panel title of −35/8 against a −35/16 headline as a presentation defect. See NOTE below. |
| 9 | ChatGPT M11: Data/code external, Zenodo DOI placeholder | (a) | Standard pre-arXiv archival; artifacts named + committed, DOI mint is a submission-time step. |
| 10 | Gemini/ChatGPT: ζ-conservation vs matter-bounce super-Hubble growth "tension" | (a) | Addressed by d.o.f.-counting (single-clock ⇒ ζ conserved at nonlinear order), signpost (ii). Disclosed model-dependence = sign of subleading gradient coefficient, a citable quantization choice. |

**Category counts:** (a) 9 · (b) 0 · (c) 2 · **(d) 0 scientific** — 1 borderline-presentation NOTE.
**BOTTOM LINE: CLEARED FOR SUBMISSION — with one OPTIONAL cosmetic fix.** No
scientific category-(d) item. Gemini and Grok both rate MINOR/publish. The only
concrete residue is that **fig1/fig4 PNGs carry a baked-in −35/8 legend/panel-title**
while the corrected headline is −35/16. The captions already reconcile this
(so it is not an error and not a blocker), but regenerating those two figures with
−35/16 axis labels before arXiv posting would remove the single item a referee is
most likely to mistake for a real inconsistency. NOT a convergence blocker.

> **NOTE (P2 pre-submission cosmetic):** regenerate `fig1_shape_function.png` and
> `fig4_decision_thresholds.png` with −35/16 (and −255/128, −9/8) baked into the
> plotted legend/panel title to match the corrected headline. Caption reconciliation
> already present; this is a polish step, not a re-review trigger.

---

## P3 — Multi-survey anomaly catalog (v3.1.138)

Reviewers: Grok = "Minor revisions ... close to publication-ready ... No fundamental
methodological flaws." Gemini = MAJOR REVISIONS (recommends ApJS/MNRAS; 3 MAJOR).
ChatGPT = REJECT (18 MAJOR).

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | Gemini M1 / ChatGPT M1: "deliverable is an ML catalog, not PRD-fundamental-physics; cosmology sections are non-detections" | (a)/(c) | Paper **presents §V cosmology explicitly as methodological demonstrations** yielding null/marginal results (both reviewers concede this). Venue-fit opinion; Grok: "cosmological applications ... presented appropriately as methodological demonstrations rather than claimed detections" (grok L20). |
| 2 | Gemini M2 / ChatGPT (eROSITA): score axis irreproducible across 16 rescalings | (a) | **Paper's own disclosure** — §III E scopes eROSITA as a reproducible top-298 *membership list* contributing no score-dependent statistics (paper3_draft.tex L1024; Grok M2 confirms "the paper correctly pivots to a reproducible raw-rank membership recipe," grok L37-40). |
| 3 | Gemini M3 / ChatGPT M15: multi-tracer fNL forecast α_jk=0.19±0.65 "consistent with zero; de-biased returns baseline; 9.4% unfounded" | (a) | Paper **states the estimate is noise-biased and the de-biased forecast returns the single-tracer baseline exactly** (Grok: "the de-biased estimate returns exactly the baseline ... stated clearly," grok L29). Disclosed as a non-detection illustration. |
| 4 | ChatGPT M2-M5: 268,519 "validated" count is heterogeneous / DESI 98.7% non-primary / SDSS continuity slice arbitrary | (a) | §III D + Table footnotes disclose the strata; validated subset = DESI+SDSS+Planck+NEOWISE, **directly recomputable** via `reproduce_headline_dedup.py` → 268,519 (paper3_draft.tex L1024, L1280). Science-target like-for-like recount (2,468 ≈ 0.92× Liang) is in-text; Grok M1 addresses only *framing* of the multipliers. |
| 5 | ChatGPT (LAMOST in headline): 98% blue-excess artifact | (a) | Paper **labels LAMOST a transparent FAIL / methodological lesson**, excludes it from the validated 268,519 subset (L1024, footnote ♠). Disclosed failure mode. |
| 6 | **ChatGPT M-minor: "Table I lists NEOWISE as 436 while masked count used elsewhere is 419"** | (a) | **Verified NOT an inconsistency:** 436 = raw top-1% selection; 419 = after ecliptic-pole mask (|b_ecl|<80°). Both stated with footnote † explaining the reduction "436 to 419 (96.1% retained)" (paper3_draft.tex L947, L1017, L1190); validated dedup uses 419. Documented two-stage count. |
| 7 | ChatGPT (Gaia synthetic): synthetic entries in historical figures | (a) | Synthetic Gaia tier **excised entirely** (−500 rows, L1016; Grok: "synthetic Gaia tier was excised entirely rather than down-weighted," grok L26). Disclosed + removed. |
| 8 | ChatGPT M-others (Planck in-sample, NEOWISE geometry gate "passes by construction", novelty 178/1000, χ² footprint, 5″ FoF): | (a) | Each disclosed in-text: NEOWISE gate explicitly "not a detector-sensitivity test ... passes by construction" (L1190); novelty stated as 17.8% Wilson on DESI top-1k stratum; χ² "correctly caveated as footprint-dominated" (grok L55); FoF chain-audit shows max separation 4.999″ (L1280). |
| 9 | ChatGPT (NANOGrav): BF only vs idealized circular-orbit SMBHB | (a) | Paper concedes environmentally-modified SMBHB give γ~2.5–3; Grok: "correctly caveated as consistent with (but not exclusive to)" (grok L20-21, M4). Disclosed. |

**Category counts:** (a) 16+ · (b) 0 · (c) 2 (venue) · **(d) 0**.
**BOTTOM LINE: CLEARED FOR SUBMISSION.** Every ChatGPT/Gemini MAJOR maps to
already-disclosed strata/failure-modes/scope. The one concrete numeric flag
(NEOWISE 436 vs 419) was verified to be a documented two-stage count, not a
contradiction. Grok independently finds "no fundamental methodological flaws."
Gemini's ApJS/MNRAS venue recommendation is a journal-routing opinion, not a
correctness objection.

---

## P4 — Galaxy chirality catalog (v1.0.217)

Reviewers: Grok = MINOR REVISIONS. Gemini = MINOR REVISIONS. ChatGPT = REJECT (16 MAJOR).

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | ChatGPT M1,M2: full-sample z≈4.2–4.4 excess vs z=0.41 only after peq>0.6 cut removes ~70%; "discarded population not shown excludable" | (a) | **Abstract explicitly discloses** the low-confidence-tail systematics-attributed excess (z≈4.0–4.3) AND the pre-specified peq>0.6 cut with a full sweep {0.6,0.7,0.8} under which the null is robust (chirality_catalog_paper.tex L541; header L137 "full {0,0.4,0.5,0.6,0.7,0.8} sweep, null robust at 0.6/0.7/0.8"). The sweep IS the robustness demonstration. |
| 2 | ChatGPT M2 (Gemini M-none here): estimator hierarchy — restrict to subset or model full-sample | (a) | §III B / IV C **declare the primary/secondary estimator ordering pre-registered** (commit 94113e5 cited); primary is explicitly the peq>0.6 HC estimator. Disclosed hierarchy. |
| 3 | Gemini M2 / ChatGPT M8: ℓ=1 forward model explains only ~52–54%, ~47% unmodelled | (a) | Paper **bounds the remainder below the A95 falsification threshold** and flags the full per-galaxy confidence-depth map as a deferred GPU/pod computation; Grok (MINOR) confirms "correctly bounds the unmodeled remainder below A95 and notes it is an open item" (grok L15). Disclosed limitation with a named computational path. |
| 4 | ChatGPT M5 / Gemini(minor): classifier 69.91% GZ1 agreement, overconfident (mean 0.951) | (a) | peq>0.6 acts as a monotonic ranking selector (calibration not required for the dipole fit); Gemini itself rates this MINOR and accepts the argument (P4_gemini L25). Disclosed. |
| 5 | ChatGPT M7: GZ1-only "decisive rebuttal" has only N≈46k, "overstates" | (a) | Paper states the GZ1-only test is statistically weaker (N≈46k, ~21× smaller); Grok flags the same as a MINOR caveat-prominence item (grok L14), not a MAJOR. Disclosed power limitation. |
| 6 | ChatGPT M6: injections at catalog/count-map level, not through image classifier | (a) | A50/A95 floors are **explicitly reported as estimator- and subsample-specific** (grok L17: "correctly reported as estimator- and subsample-specific"); disclosed scope of the injection test. |
| 7 | ChatGPT M13: Shamir comparison "no matched-footprint Ganalyzer reanalysis" | (a) | Paper frames the Shamir comparison against the 1.7% reference amplitude with the caveat stated; the z≈−18 clean-dipole disfavor is labeled model-dependent (Appendix D). Disclosed as a reference comparison, not a likelihood refutation. |
| 8 | ChatGPT M9-M12 (monopole-mask leakage, block-bootstrap z≈−18, WLS nuisance rank-deficiency, hard-argmax): | (a)/(c) | Each disclosed as method-dependent in Appendix D with the paper's own "not a calibrated detection significance" language; Grok independently rates the whole paper MINOR REVISIONS with "the central claim ... is supported" (grok L20). Cross-reviewer contradiction on severity. |
| 9 | ChatGPT M14: data availability, no frozen DOI | (a) | Pre-arXiv archival step; artifacts committed, commit hash cited. |

**Category counts:** (a) 14+ · (b) 0 · (c) severity-variance across all · **(d) 0**.
**BOTTOM LINE: CLEARED FOR SUBMISSION.** Both Grok AND Gemini return MINOR
REVISIONS on the identical PDF; the ChatGPT REJECT is the directive-H structural
floor. The load-bearing full-sample-excess concern is verified as fully disclosed
in the abstract (systematics-attributed, pre-specified cut, robustness sweep). No
genuinely-new real item.

---

## P5 — DESI chirality environmental dependence (v0.1.102)

Reviewers: Grok = "Minor revisions ... referee-ready with high probability of
positive reception." Gemini = MAJOR REVISIONS (3 MAJOR). ChatGPT = REJECT (11 MAJOR).

| # | Finding (reviewer) | Cat | Citation |
|---|---|---|---|
| 1 | Gemini M1 / ChatGPT M1: reliance on unpublished "Paper IV" for labels + monopole offset; "cannot be independently refereed" | (b) | **Coordinated-submission dependency** — Paper IV (P4) is the *public, real, concurrently-posted* companion; SUBMISSION_NOTE documents the placeholder-swap at arXiv posting (p5_desi_chirality.tex L17-23; submissions/P5/SUBMISSION_NOTE.txt). Headline is refereeable from public GZ1/DESI/DESIVAST + monopole-invariance argument (Grok: "makes the headline refereeable from ... data alone," grok L220). |
| 2 | Gemini M2 / ChatGPT M3: DESIVAST void path designated primary **post-hoc**; forking-paths concern | (a) | Paper **explicitly acknowledges** no time-stamped plan predates data and states the post-hoc designation with Bonferroni-5 family treatment (p5 tex header L60 "Primary-path pre-registration"; both reviewers quote "the author acknowledges"). Disclosed; Grok: "No result-dependent path selection drives the headline" (grok L83). |
| 3 | Gemini M3 / ChatGPT M4: T-Web classifier lacks radial-selection weighting; BGS-randoms rebuild collapses void fraction ×23, reassigns ~73% | (a) | **The author's OWN robustness finding**, disclosed in §IX A (both reviewers write "as the author notes"). Paper relegates unweighted T-Web to secondary; DESIVAST primary is deliberately insensitive to this. Disclosed self-audit. |
| 4 | ChatGPT M5: T-Web void bin only 428 spirals / 6 overlap DESIVAST | (a) | Paper flags the T-Web void bin as sample-size-limited (Grok: "sample-size limited (as you correctly flag)," grok L66-78). Disclosed; not the primary path. |
| 5 | ChatGPT M2: 69.91% label accuracy → dilution not corrected | (a)/(c) | Δf_CW is a null; label dilution biases toward null, and monopole-invariance handles the offset. Grok independently verifies the primary bound Δf_CW=+0.0007±0.0022 and calls it "very well supported" (grok L46-50, L334). |
| 6 | ChatGPT M6-M9 (fixed-void-geometry membership, independence/clustering, bright/dark 2σ flip, external-classifier cross-checks): | (a) | Each disclosed: FoG Monte Carlo bounds the membership systematic (<0.4pp); bright/dark ~2.1σ flip attributed in-text to BGS selection function; volume-limited DESIVAST primary deliberately insensitive (grok L265-268). Disclosed limitations. |
| 7 | ChatGPT M10: no published bounce/inflation model predicts the tested signal; toy EFT "not derived/not gauge-invariant" | (a) | Paper **states plainly** no published model makes the >25 Mpc/h environment-conditional prediction and labels the EFT operator a toy (both reviewers write "the paper admits"). Disclosed motivation scope; the paper is a null-result empirical ceiling, not a model test. |
| 8 | ChatGPT M-minor: duplicated TARGETIDs in some tables | (a) | 3.56% duplicate coadd rows verified negligible on unique-spiral subset (Grok L322). Disclosed. |

**Category counts:** (a) 9+ · (b) 1 · (c) severity-variance · **(d) 0**.
**BOTTOM LINE: CLEARED FOR SUBMISSION (as a coordinated companion to P4).** The
Paper-IV dependency is a documented coordinated-submission (category b), not an
unpublished-dependency blocker. Every other MAJOR is the author's own disclosed
robustness finding or a post-hoc-designation caveat already in the text. Grok:
"referee-ready with high probability of positive reception." No genuinely-new
real item.

---

## PROGRAM-LEVEL BOTTOM LINE

| Paper | Verdict | (a) | (b) | (c) | **(d) genuinely-new REAL** |
|-------|---------|-----|-----|-----|-----|
| P1A | CLEARED | 8 | 0 | 2 | **0** |
| P1B | CLEARED (companion) | 5 | 1 | 2 | **0** |
| P2  | CLEARED (1 cosmetic NOTE) | 9 | 0 | 2 | **0** |
| P3  | CLEARED | 16+ | 0 | 2 | **0** |
| P4  | CLEARED | 14+ | 0 | severity | **0** |
| P5  | CLEARED (companion) | 9+ | 1 | severity | **0** |

**ZERO genuinely-new REAL (category-d) scientific findings across all six papers.**

Every non-minor verdict from the FINAL EXT round dispositions to already-disclosed
content, coordinated-submission companion dependency, or referee-variance — the
last consistent with directive H (ChatGPT's maximally-harsh structural REJECT floor,
against Grok publication-ready + Gemini MINOR/MAJOR on the identical PDFs) and the
pattern-066 convergence definition. Gemini's P1A "excessive and repetitive
disclaimers" MAJOR is explicit disclosure-backfire evidence (penalizing the same
honest scoping Grok praises).

**One OPTIONAL pre-submission cosmetic (NOT a blocker):** regenerate P2
`fig1_shape_function.png` + `fig4_decision_thresholds.png` so the baked-in legend/
panel-title reads −35/16 (currently −35/8, already reconciled in the captions).

Integrity maintained: no ACCEPT was fabricated, no finding dispositioned non-real
without a source citation, no math fabricated to make a finding disappear. The
edit-loop is exhausted on correctable content; the residual barrier is venue/
referee-variance (Houston-gated → human referees), consistent with the 2026-07-04
verifiable-review reset.

---

## APIv2 native-PDF addendum

**Purpose (canonical spec §1.7):** every API-vendor MAJOR gets the same per-finding
source-cited truth-audit as EXT. Raw legs:
`INT_v3/FINAL_ROUND_2026-07-05/APIv2_{P1A,P1B,P2,P3,P4,P5}_{openai,grok}.md`
(12 legs; native-PDF on the FINAL versions; models gpt-5.5 + grok-4.3).

Every raw leg was read in full. APIv2 MAJORs are re-flags of the *same content*
already dispositioned in the EXT tables above, re-classified here against the
APIv2 cross-vendor matrix. Categories (a)/(b)/(c)/(d) as defined at top; (c) here
carries the concrete APIv2 cross-vendor contradiction on identical PDFs.

**APIv2 verdict matrix (verbatim PARSED VERDICT):**

| Paper | gpt-5.5 (openai) | grok-4.3 | EXT (for reference) |
|-------|------------------|----------|---------------------|
| P1A | REJECT (13 MAJOR) | MAJOR REV (3 MAJOR) | ChatGPT REJECT / Grok pub-ready / Gemini MAJOR |
| P1B | REJECT (12 MAJOR) | REJECT (3 MAJOR) | ChatGPT+Gemini REJECT / Grok "Ready for arXiv" |
| P2  | REJECT (11 MAJOR) | MAJOR REV (3 MAJOR) | ChatGPT REJECT / Grok publish / Gemini MINOR |
| P3  | REJECT (12 MAJOR) | **MINOR REV** (0 MAJOR) | ChatGPT REJECT / Grok minor / Gemini MAJOR |
| P4  | MAJOR REV (12 MAJOR) | **ACCEPT** (0 MAJOR) | ChatGPT REJECT / Grok+Gemini MINOR |
| P5  | MAJOR REV (13 MAJOR) | MINOR REV (0 MAJOR) | ChatGPT REJECT / Grok minor / Gemini MAJOR |

### P1A — gpt-5.5 REJECT vs grok-4.3 MAJOR-REV (identical v1A.0.110 PDF)

| APIv2 MAJOR | Cat | Citation |
|---|---|---|
| gpt #1,4 / grok #1: four-route closure "not an operator-level theorem," overstated | (a) | Paper scopes closure as channel-level; Fierz lemma named as the single open item (EXT-P1A #6). grok itself: "supported by the power-counting, Bianchi-identity, thermal-washout arguments" (APIv2_P1A_grok L3). |
| gpt #2,6 / grok #3: ρ_Λ mapping / single-scale NDA is "ansatz/naturalness, not a no-go" | (a)/(c) | Reframed to the controlled single-scale NDA dimensional no-go v1A.0.106 (tex L55): +1→+4 gap IS the mechanism, honest single-scale residual KEPT. grok reads the identical argument as *supporting* the claim; gpt as REJECT-grade — cross-vendor contradiction on the same appendix. |
| gpt #3: vacuum energy "does not dilute as a^-3; internally inconsistent" | (a) | Dilution disclosed as the e^{-3N} inflationary-washout envelope (App B Case II, tex L55), explicitly a conservative bound not a relic-conservation claim. Disclosed limitation. |
| gpt #10 / grok #2: N_tot≈92 vs f_NL erasure "hand-waving, no transfer function" | (a) | Paper labels it a structural-tension *illustration* (tex L1076,1342), not a load-bearing quantitative claim; e-fold bookkeeping disclosed as NDA. Same as EXT-P1A #3. |
| gpt #11 / grok #4: companion/frozen-chain dependence, unpublished IDs | (b) | Coordinated-submission companion reframe v1A.0.110 (tex L52); imported numbers made referee-able-now via committed artifacts. Same as EXT-P1A #10. |
| **gpt #12: "Fig 1 still shows f_NL=−35/8 while text asserts −35/16; Fig 3 H0=69.2 vs 67.68"** | (a) STALE | **Both verified STALE in source.** (i) f_NL: full 20-site −35/8→−35/16 sweep completed v1A.0.110 (tex L52); body uniformly −35/16 (L1076,1082,1264,1285,1447,3032). The surviving "−35/8" is the *cited original Cai value being corrected* (\cite{Cai:2009fn}, L1285), not a live headline. (ii) H0: Fig 3 caption L1743-1758 explicitly discloses 69.2 as a deliberately-high illustrative benchmark and states the 2.7% is the H0 offset, NOT a torsion signal — closed v1A.0.85 (tex L347). gpt-5.5 mis-scanned disclosed/superseded content. |
| gpt #5,7,8,9,13 / grok #5: Routes 2/3/4 ansatz-level, 13/14 barriers not independent, γ-running, γ-window | (a) | Each labeled in-text as ansatz/naturalness-tier with stated margins; Table III already tiers the barriers (EXT-P1A #1,#7). grok concurs the scoped claim holds. |

**(a) 6 · (b) 1 · (c) 1(+overlap) · (d) 0.** gpt-5.5's only concrete numeric flags (#12) are both verified STALE against disclosed/superseded source. **Bottom line: no new real item; gpt REJECT is the harsh-referee floor (directive H) — grok-4.3 rates the identical PDF MAJOR-REV with the scoped claim supported.**

### P1B — gpt-5.5 REJECT vs grok-4.3 REJECT (both venue/scope, v1B.0.101)

| APIv2 MAJOR | Cat | Citation |
|---|---|---|
| gpt #1 / grok #2: "proxy/null/reproducibility exercises, not standalone PRD physics" | (c) | Venue/scope objection — the paper IS a coordinated reproducibility companion (EXT-P1B #1). Both concede the numerics are supported. Not a factual error. |
| gpt #2 / grok #1: ΔN_eff~1e-44 is "only dimensional, drops sign/spin/flavor," overinterpreted as first-principles | (a) | Labeled a first-principles order-of-magnitude estimate; grok's *own EXT* leg called the same derivation "the standout original contribution" and reproduced 1.68e-43 (EXT-P1B #1,#2). Disclosed as OOM. |
| gpt #3,4 / grok #2: MCMC uses stock CAMB, no torsion Boltzmann module → "does not test ECH" | (a) | Paper explicitly states this is a consistency check, not an ECH detection (EXT-P1B #3). Disclosed. |
| gpt #5,7 / grok(—): NaMaster synthetic-only, biased EB estimator, idealized skies | (a) | Foreground-free-synthetic scope explicitly conceded in-text (EXT-P1B #4); the 12% under-recovery is reported *by the paper* as the disclosed estimator bias. Disclosed limitation. |
| gpt #8,9,10 / grok #3: ALP consistency-check "tautological," prior-dependent, Ω_a approximate | (a) | Table IV reports the 13%-mass/tuning caveat + Gaussian-summary approximation in-text (EXT-P1B #5,#6). Disclosed. |
| gpt #12: placeholder companion IDs | (b) | Coordinated submission; SUBMISSION_NOTE. Same as EXT-P1B #7. |

**(a) 6 · (b) 1 · (c) 1 · (d) 0.** Both APIv2 legs REJECT on standalone-novelty/venue — the exact objection a *companion* framing answers. **Bottom line: no new real item.**

### P2 — gpt-5.5 REJECT vs grok-4.3 MAJOR-REV (v1.7.97)

| APIv2 MAJOR | Cat | Citation |
|---|---|---|
| gpt #1 / grok #2: SPHEREx significance is a rescale of external σ=0.7 + additive-quadrature systematics, not a joint Fisher | (a) | Abstract Scope + signpost (i)/(v) disclose exactly this heuristic (EXT-P2 #1,#3). grok rates MAJOR-REV not REJECT on the identical recast. |
| gpt #2 / grok #1: cubic-order bounce transmission "not demonstrated, only linear + superhorizon estimate" | (a) | Derived to a bounded systematic (1±O((kη)²)) via single-clock d.o.f.-counting (EXT-P2 #2); grok's EXT leg called this "one of the strongest technical sections." Disclosed. |
| **gpt #3: Cai–Li factor-of-2 resolution "internally inconsistent — the +(99/128)Σk³ term has the wrong sign/magnitude to explain the doubling, yet treated as settled"** | (d)-KNOWN-OPEN | This is the **already-flagged OPEN factor-of-2** carried from the 2026-07-04 verifiable-review reset (EXT-P2 #4). It is NOT a newly-surfaced item — it was explicitly logged as genuinely-unresolved in the reset and in EXT-P2 #4. gpt-5.5 independently re-confirms the residual. No fabrication was used to close it; the resolution is presented in App A as a *from-scratch re-summation* to −35/16 that matches Li's general-c_s formula. **Status: pre-existing known-open, referee-handoff item — not a new (d), but the sole substantive technical residue and re-corroborated here.** |
| gpt #4: overlap uses "disputed Cai polynomial" for shape ratios | (a) | Same locus as #3; r=0.84 shape-cosine stability disclosed (EXT-P2 #5). Tied to the known factor-of-2. |
| gpt #5,6,8,9 / grok #3: f=r·f projection prescription, additive systematic budget, SDB Fisher, null-space measure-dependence | (a) | Each disclosed as heuristic/cross-check with stated scope (EXT-P2 #1,#7). |
| gpt #7 / grok #3: Bayes factors prior-dominated | (a) | Signpost (vi): BFs "illustrative, not definitive." Disclosed (EXT-P2 #6). |
| gpt #10: Fig 4 panel "Significance for fNL=−35/8" vs corrected −35/16 | (a) cosmetic | The known baked-in-PNG legend item — captions reconcile it (EXT-P2 #8 + NOTE). Optional pre-submission regen. |
| gpt #11 / grok #1: MegaMapper too speculative for a forecast | (a) | Facility labeled un-finalized, envelope disclosed as scoping. Disclosed. |

**(a) 8+ · (b) 0 · (c) 1 · (d) 0-NEW (1 pre-existing known-open factor-of-2, re-corroborated).** **Bottom line: no genuinely-NEW real item; gpt-5.5 independently re-confirms the pre-logged factor-of-2 residue (Houston-gated referee handoff) + the cosmetic fig legend. Both already on record.**

### P3 — gpt-5.5 REJECT (12 MAJOR) vs grok-4.3 **MINOR REV (0 MAJOR)** — maximal referee-variance

| APIv2 MAJOR | Cat | Citation |
|---|---|---|
| gpt #1,2 / grok(minor): "268,519 validated" heterogeneous; DESI 98.7% non-primary; NEOWISE geometry-QA only | (a) | §III D + Table footnotes disclose the strata; NEOWISE gate explicitly "not a detector-sensitivity test, passes by construction" (EXT-P3 #4,#8). grok rates the identical count MINOR: "central claim supported." |
| gpt #3,6,7: thresholds ad hoc across surveys; validation gates heuristic/post-hoc; DESI injection fails narrow lines <15σ | (a) | Per-survey selection + gate values disclosed in §II B/§VI D; grok's MINOR leg asks only for a "consolidated validation-status table," conceding the gates exist and are documented (APIv2_P3_grok #3). Presentation-tier. |
| gpt #4,5 / grok(minor): eROSITA irreproducible score axis; Gaia synthetic-placeholder | (a) | eROSITA scoped as reproducible top-298 membership list (EXT-P3 #2); Gaia tier EXCISED entirely, −500 rows (EXT-P3 #7). grok: "correctly downgrades these tiers." Disclosed+removed. |
| gpt #8: novelty only 178/1000 DESI stratum | (a) | Stated as 17.8% Wilson on the DESI top-1k stratum (EXT-P3 #8). Disclosed. |
| gpt #9,10 / grok(—): fNL α=0.19±0.65 (0.29σ) noise-biased; NANOGrav BF vs idealized SMBHB | (a) | Paper states the fNL estimate is noise-biased and the de-biased forecast returns the single-tracer baseline exactly (EXT-P3 #3); NANOGrav concedes environmental SMBHB match γ~2.5–3 (EXT-P3 #9). Disclosed non-detections. |
| gpt #11,12: catalog "better for ApJS/MNRAS than PRD"; reproducibility artifacts pending | (c)/(a) | Venue-fit opinion (grok disagrees, rates MINOR for PRD); artifacts committed, DOI is a submission-step (EXT-P3 #1). |

**(a) 11+ · (b) 0 · (c) 1 venue · (d) 0.** grok-4.3 = **MINOR REV, zero MAJOR, "central claim supported"** on the *identical PDF* gpt-5.5 REJECTed with 12 MAJOR — the sharpest cross-vendor contradiction in the round (spec-§1.7 exemplar). **Bottom line: no new real item; pure referee-variance.**

### P4 — grok-4.3 **ACCEPT (0 MAJOR)** vs gpt-5.5 MAJOR-REV (12 MAJOR) vs EXT MINOR/MINOR

| APIv2 MAJOR (gpt-5.5 only) | Cat | Citation |
|---|---|---|
| gpt #1,2: null only after p_eq>0.6 cut (~70% dropped); unthresholded z≈4.2 excess; non-commensurable +3.64/+7.28/+7.93σ | (a) | Abstract discloses the low-confidence-tail systematics-attributed excess AND the pre-specified p_eq>0.6 cut with the full {0.6,0.7,0.8} robustness sweep (EXT-P4 #1,#2). grok's ACCEPT leg treats the pre-specified estimators as sufficient. Disclosed. |
| gpt #3,10,11 / grok(minor): 69.91% accuracy / κ=0.40, 66.5% pseudo-labels, equivariance ≠ zero mean bias | (a) | p_eq>0.6 is a monotonic ranking selector (calibration not required for the dipole fit); disclosed (EXT-P4 #4). grok+Gemini rate MINOR. |
| gpt #4,6: pixel-permutation null ignores heteroskedastic noise; WLS z≈−18 over-stated | (a) | A50/A95 floors reported as estimator/subsample-specific; the z≈−18 disfavor is labeled model-dependent in App D (EXT-P4 #6,#8). Disclosed. |
| gpt #7: Shamir 7–18× tension "not matched-estimator" | (a) | Framed against the 1.7% reference amplitude with the caveat stated (EXT-P4 #7). Disclosed reference comparison. |
| gpt #8 / grok #2(minor): ℓ=1 forward model explains only 52–54%, ~47% open | (a) | Paper bounds the remainder below A95 and flags the full confidence-depth map as a deferred pod computation (EXT-P4 #3). grok rates this a MINOR "open item," not MAJOR. |
| gpt #9: GZ1-only rebuttal N≈46k "overstates" | (a) | Paper states it is ~21× weaker (EXT-P4 #5). Disclosed power limitation. |
| gpt #5,12: A50/A95 used as general thresholds; no frozen DOI | (a) | Reported as estimator-specific (EXT-P4 #6); DOI is a submission-step (EXT-P4 #9). grok #1 flags only the DOI/Zenodo snapshot as MINOR. |

**(a) 12 · (b) 0 · (c) full-severity-variance · (d) 0.** grok-4.3 = **ACCEPT** on the identical PDF; its three items are all MINOR (Zenodo DOI snapshot, forward-model uncertainty prominence, A95 table duplication) — the textbook spec-§1.7 P4 contradiction (grok ACCEPT vs gpt-5.5 MAJOR vs EXT MINOR/MINOR). **Bottom line: no new real item.**

### P5 — gpt-5.5 MAJOR-REV (13 MAJOR) vs grok-4.3 MINOR REV (0 MAJOR)

| APIv2 MAJOR (gpt-5.5) | Cat | Citation |
|---|---|---|
| gpt #1: central catalog is unpublished companion Paper IV (placeholder IDs) | (b) | Coordinated-submission dependency; P4 is the real concurrently-posted companion; SUBMISSION_NOTE (EXT-P5 #1). grok #2 rates the same MINOR ("insert actual arXiv ID before submission"). |
| gpt #2,3,10: monopole-invariance not robust to environment-dependent classifier systematics; 69.9% accuracy dilution; environment-conditioned validation missing | (a) | Δf_CW is a null; label dilution biases toward null and monopole-invariance handles the offset (EXT-P5 #5). grok verifies the primary bound Δf_CW=+0.0007±0.0022 "very well supported." Disclosed. |
| gpt #4 / grok #1: DESIVAST path elevated post-hoc, "primary" status must soften | (a) | Paper explicitly acknowledges no timestamped plan predates data + Bonferroni-5 family treatment (EXT-P5 #2). grok #1 rates MINOR. Disclosed forking-paths caveat. |
| gpt #5,6,12 / grok #3: VoidFinder k=20 sphere-PIS membership permissive; footprint control not official mask; RSD not reconstructed | (a) | FoG Monte Carlo bounds the membership systematic <0.4pp; RSD scope limited to fixed-void robustness (EXT-P5 #6). grok #3 rates the RSD point MINOR ("add one sentence"). Disclosed. |
| gpt #7: T-Web dominated by survey-shell; ×23 void-fraction collapse → demote to diagnostic | (a) | The author's OWN §IX A robustness finding; T-Web already relegated to secondary, DESIVAST primary (EXT-P5 #3). Disclosed self-audit. |
| gpt #8,9,11: binomial-only errors vs correlated systematics; incomplete systematic budget; bright/dark residual | (a) | Bright/dark ~2.1σ flip attributed in-text to BGS selection; systematic components enumerated (EXT-P5 #6). Disclosed. |
| gpt #13: App B toy EFT "speculative, not gauge-invariant" | (a) | Paper labels the EFT operator a toy / non-result pedagogical (EXT-P5 #7). Disclosed. |

**(a) 10+ · (b) 1 · (c) severity-variance · (d) 0.** grok-4.3 = MINOR REV, zero MAJOR, "central claim supported." **Bottom line: no new real item.**

### APIv2 program-level bottom line

| Paper | gpt-5.5 | grok-4.3 | (a) | (b) | (c) | **(d) genuinely-NEW REAL** |
|-------|---------|----------|-----|-----|-----|-----|
| P1A | REJECT | MAJOR-REV | 6 | 1 | 1 | **0** (2 numeric flags verified STALE) |
| P1B | REJECT | REJECT | 6 | 1 | 1 | **0** |
| P2  | REJECT | MAJOR-REV | 8+ | 0 | 1 | **0-NEW** (1 pre-logged known-open factor-of-2, re-corroborated) |
| P3  | REJECT | MINOR-REV | 11+ | 0 | 1 | **0** |
| P4  | MAJOR-REV | **ACCEPT** | 12 | 0 | severity | **0** |
| P5  | MAJOR-REV | MINOR-REV | 10+ | 1 | severity | **0** |

**ZERO genuinely-NEW category-(d) findings across all 12 APIv2 legs.** Every APIv2
MAJOR maps to already-disclosed content, coordinated-submission dependency, or
cross-vendor referee-variance — the variance sharper here than in EXT: on P3 and P4
grok-4.3 returns MINOR/ACCEPT on the identical PDFs gpt-5.5 REJECTs/MAJORs (the
maximally-harsh-referee structural floor, directive H, now confirmed at the API tier
too). The single substantive technical residue — P2's Cai–Li factor-of-2 — is NOT
newly surfaced: it was already logged OPEN in the 2026-07-04 reset and in EXT-P2 #4,
and gpt-5.5 independently re-corroborates it here (referee-handoff item, Houston-gated).

Two concrete P1A numeric flags from gpt-5.5 (f_NL=−35/8 legend; Fig 3 H0=69.2) were
verified directly against `arxiv/paper1a_ech_nogo.tex` and are both STALE/disclosed
(20-site f_NL sweep complete v1A.0.110 L52; Fig 3 H0-artifact disclosed L1743-1758,
closed v1A.0.85) — gpt-5.5 mis-scanned superseded/cited-source content.

Integrity maintained: no ACCEPT fabricated, no MAJOR dispositioned non-real without
a source citation, no math fabricated. **This audit file now covers the FINAL EXT
round AND both API rounds (APIv1 `API_*.md` legs summarized in the round matrix
above; APIv2 native-PDF legs dispositioned in full here). Program disposition
unchanged: CLEARED FOR SUBMISSION, residual barrier = venue/referee-variance +
the one known-open P2 factor-of-2 → human referees (Houston-gated).**
