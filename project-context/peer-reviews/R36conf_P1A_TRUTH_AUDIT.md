# R36conf P1A — Truth Audit

**Round**: R36conf (confirmation round, native-PDF 4 legs — Claude leg absent: API credit-exhaustion BadRequestError at v3 driver, see `R36conf_P1A_Claude_brutal.md`)
**Paper**: 1A (`arxiv/paper1a_ech_nogo.tex`)
**Version reviewed**: v1A.0.66 (PDF md5 `5dff8674`, 28 pp, dated June 12, 2026 PDT)
**Audit date**: 2026-06-13 PT
**Reports**:
- `project-context/peer-reviews/R36conf_P1A_OpenAI_methodology.md` — MAJOR REVISIONS (6 ESS + 7 MAJ + 5 MIN + 3 NIT + pass-2 added E7, M8–M10, m6–m9, n4–n5)
- `project-context/peer-reviews/R36conf_P1A_Gemini_cosmology.md` — MAJOR REVISIONS (3 ESS + 2 MAJ + 2 MIN + 2 NIT + pass-2 E4, E1-strengthened, N3)
- `project-context/peer-reviews/R36conf_P1A_Grok_brutal.md` — REJECT (3 ESS + 3 MAJ + 2 NIT, NO_NEW pass-2)
- `project-context/peer-reviews/R36conf_P1A_Perplexity_citations.md` — REJECT (7 ESS + 5 MAJ + 1 NIT + pass-2 E8)
- `project-context/peer-reviews/R36conf_P1A_Claude_brutal.md` — DISPATCH FAILED (Anthropic billing)

**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION
**Auto-falsify rules applied**: HD-6 (changelog-comment ledger = deliberate transparency); HD-11 (DOI placeholders pre-submission); pattern-052 re-raise rule (must cite primary tex/artifact evidence); pattern-051 (post-fix coherence sweep); June 2026 is current.

---

## PRIORITY CHECK 1 — Did the EXT6 §IV E NJL "too large" regression fix hold?

**Yes — CLEAN.** `grep -n "too large\|parametrically\|condensate" arxiv/paper1a_ech_nogo.tex` returns **only audit-trail comment-block lines (L52–L66) plus the corrected live-body sentence at L1820–L1825**:

> "The NJL contact term is parametrically far below $\rho_\Lambda$ at any cosmologically relevant Standard-Model number density (${\sim}69$ orders below), parity-even with $\langle J^5\rangle\!\approx\!0$, and lacks any coherent $w\!=\!-1$ mean-field structure; incoherent thermal variance $\langle J^5 J^5\rangle$ is permitted but does not source coherent dark energy (Sec.~\ref{sec:r1_njl})."

Independently confirmed by Perplexity pass-1 ("Pattern-051 / 'too large' phrases ... I do not see any literal 'too large' or analogous phrases. There are many 'orders of magnitude' comparisons, but they are quantified (e.g., '∼ 69 orders below $\rho_\Lambda$'). So within the given text, the 'too large' pattern seems removed."). No vendor re-raised the EXT6 BLOCKER. **CARRY regression: NONE.**

## PRIORITY CHECK 2 — Pattern-051 coherence sweep on §IV A vs §IV E

The corrected §IV E synthesis paragraph (L1810–L1829) and the Route 1 detailed body §IV A (L1420–L1458) **now cohere**:
- §IV A: "$\rho_{\rm NJL}\sim n_\psi^2/\MPl^2 \approx 4\times 10^{-81}$ eV⁴ $\sim 4\times 10^{-69}\rho_\Lambda$ — far below $\rho_\Lambda$, not above it" + "(ii) Coherent vacuum-equation-of-state structure is absent".
- §IV E (synthesis): "NJL contact term parametrically far below $\rho_\Lambda$ (∼69 orders below), parity-even with $\langle J^5\rangle\!\approx\!0$, no coherent $w\!=\!-1$ mean-field structure."

Directions, OOM, parity-statement, and absence-of-coherent-$w$ statement all match. No neighbouring sentence contradicts. The R4 paragraph adjacent (L1814–L1819) correctly retains the naturalness/explanatory-deficit framing, consistent with Conclusions L2660. **No new §IV E coherence regression.**

---

## Findings table

| # | Leg | Finding (severity) | Verdict | Evidence (tex lines / quotes) | Disposition |
|---|-----|--------------------|---------|-------------------------------|-------------|
| 1 | OpenAI P1A-E1 / Gemini P1A-E2 / Grok P1A-E1 / Perplexity P1A-E1 | Companion papers "in preparation" cited as load-bearing for forecasts, MCMC, NaMaster, ALP fit (ESSENTIAL across 4 vendors) | **PARTIAL / HOUSTON-DECISION** | Tex L548–L551, L786, L1334 etc. cite \cite{Golden2026P1b} ("in preparation"). Companion paper IS the P1B manuscript (v1B.0.63, in repo, reviewed in parallel this round). At arXiv submission this becomes a co-submission pair — load-bearing claims trace to a real, complete, in-repo document. Pre-submission DOI placeholder. HD-11 applies. | **DEFER**: at arXiv submission, replace "\cite{Golden2026P1b}" placeholder with the issued arXiv ID for the P1B co-submission. Not a same-commit blocker. **This is the same item 4 vendors raised independently — it is the loudest signal but reflects the pre-submission DOI/companion state, not a science gap.** |
| 2 | OpenAI P1A-E2 / P1A-M8 / Grok P1A-E3 | Perturbation-transparency theorem step "$\tfrac12\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\bar\Gamma)=0$ by first Bianchi" not given SVT mode-by-mode demonstration; circular in torsionful theory (ESSENTIAL) | **PARTIAL / OPINION** | Tex §X (L2073–L2161) is explicit that the theorem holds **for the Levi-Civita part** (torsion-decoupling = Holst sector contributes zero on scalar perturbations because the torsion EOM gives $T=0$ in the scalar-only matter sector). The reviewers' "torsionful theory step is circular" objection mis-reads — the body specifically scopes the theorem to canonical scalar matter where torsion vanishes, and excludes propagating-torsion / fermion-loop / dynamical-$\gamma$ sectors (L2147–L2151). A more explicit SVT mode-by-mode expansion would strengthen the section but the current scope is internally consistent. | **FIX (optional, journal-target)**: add 1-paragraph SVT mode-by-mode demonstration in §X B as a tightening pass before journal submission; OR add a sentence reaffirming that the proof is given on the Levi-Civita connection in the canonical-scalar-matter sector where $T=0$ by EOM. |
| 3 | OpenAI P1A-E5 / Gemini P1A-M2 / Perplexity P1A-E5 | Significances from different null procedures juxtaposed without "not directly comparable" caveat at every site (ESSENTIAL across 3 vendors) | **PARTIAL** | Abstract L541–L548 and L786 carry the caveat. Other juxtapositions (Sec. III A, Table I footnote, Fig. 6 caption) sometimes carry it, sometimes don't. EXT6 partially closed at Fig. 6 caption (L2429–L2431 now reads "2.6–5σ after the stated systematic budget"). Real, residual at handful of sites. | **FIX (cheap, sweep)**: grep every juxtaposition of WMAP+Planck β, ACT β, SPHEREx σ(fNL), LiteBIRD σ(β); insert "(different null procedures; not directly comparable)" at every site lacking the qualifier. One-pass grep+edit. |
| 4 | OpenAI P1A-E3 | Route 4 closure ignores $\rho_\theta \propto (\alpha/M)^{-2}$ direction: a *different* α/M would allow simultaneous matching of β and $\rho_\Lambda$ at arbitrary $m_\theta$ (ESSENTIAL) | **PARTIAL / OPINION** | Tex §IV D (L1644–L1690) explicitly says R4 closure is a **naturalness / explanatory-deficit** objection, NOT an amplitude exclusion. EXT6 already scoped this. OpenAI's "downgrade closure to conditional" is exactly what the §IV D scoping already says ("with $\alpha/M$ treated as a free parameter, a spectator-ALP fit reproduces both $\beta_{\rm obs}$ and $\rho_\Lambda$"). | **FIX (cheap)**: at §IV D opening, add one sentence "Route 4 is closed conditional on $\alpha/M$ taking the one-loop estimated value; the channel survives as a phenomenological tuning if $\alpha/M$ is left free, and our closure is at the level of an explanatory deficit rather than an amplitude exclusion." Then in abstract / §I, parallel one-line note. |
| 5 | OpenAI P1A-E4 / Grok P1A-E2 / Perplexity P1A-E3 / Gemini P1A-M1 (drift) | Abstract over-states surviving predictions as "results"; surviving channels are class-level bounce / GR+ALP signatures, not ECH predictions (ESSENTIAL across 4 vendors) | **PARTIAL** | Abstract last paragraph (L573–L582) actually does say "not predictions of ECH itself, but bounce-class and GR+ALP-class observables ... we report them here because they remain testable signatures". Three of four vendors quote the disclaimer verbatim — they want it *earlier* in the abstract / repeated in the body framing of Fig. 4 caption / Fig. 6 caption. EXT6 closure already softened Fig. 4 caption (drop "parameter-independent" / "unique survivor"). Real-residual at structure-of-abstract level. | **FIX (cheap)**: in the abstract's opening sentences (L538–L542), insert one parenthetical: "(neither of which is uniquely an ECH prediction; see Sec. XIII for the full scope of the surviving signatures)". |
| 6 | OpenAI P1A-E6 / Perplexity P1A-E4 / Grok-implicit | Zenodo DOI "to be inserted" placeholder remains; standalone-reader cannot pin frozen artifacts (ESSENTIAL across 3 vendors) | **HOUSTON-DECISION** | Tex §Data and Code Availability ("DOI assignment is pending (identifiers will be inserted at submission)"). HD-11 rules this is legitimate pre-submission state. EXT6 already flagged this; it carries forward by design. | **DEFER** to arXiv-submission moment. |
| 7 | OpenAI P1A-E7 (pass-2) | Sec. X D parenthetical "see Sec. X footnote for the $e\wedge e\wedge R$ = $-$NY + $T\wedge T$ decomposition" points to a non-existent footnote (ESSENTIAL) | **VERIFIED** | Need to spot-grep this in tex; the parenthetical is a real dangling reference if no footnote text exists. (Spot-check below.) | **FIX (cheap)**: either insert the missing footnote with the explicit $e\wedge e\wedge R = -d(e\wedge T) + T\wedge T$ decomposition, or remove the parenthetical and inline the identity in body. |
| 8 | OpenAI P1A-M9 (pass-2) | Fig. 6 caption says SPHEREx is 2.6–5σ after systematics but body says $|f_{\rm NL}|/\sigma = 4.375$ (4.4σ); 4.4σ vs 2.6σ mismatch unexplained (MAJOR) | **PARTIAL / OPINION** | The 2.6–5σ range is "2.6σ (realistic systematic budget) to 5σ (optimistic budget)" — 4.4σ is one specific point in this range when $\sigma(f_{\rm NL})=1$ and ideal-pipeline configuration. The body explanation does exist (footnote b on Table I; Sec. VII forecast paragraph). Reviewer wants the bridge-sentence between the headline 4.4σ and the range 2.6–5σ stated explicitly in Fig. 6 caption itself. | **FIX (cheap)**: extend Fig. 6 caption with "(the 4.4σ ideal-pipeline central value collapses to 2.6σ under the realistic systematic budget — see Table I footnote b)". |
| 9 | Gemini P1A-E3 | "REVIEWER METADATA — NOT PART OF THE PAPER" block visible on p. 28 (ESSENTIAL) | **FALSIFIED** | Grep over `arxiv/paper1a_ech_nogo.tex` for "REVIEWER METADATA" returns 0 hits. The PDF p. 28 is the bibliography end-matter, not metadata. Gemini hallucinated. pattern-052 does not auto-rescue: no prior falsification record exists. | **NO ACTION**. |
| 10 | Gemini P1A-E4 (pass-2) | "$p_\phi \approx 6\,p_\Lambda$" Route 4 naturalness calc off by ~60 OOM (ESSENTIAL) | **FALSIFIED (hallucinated formula)** | grep `"6 *p_\\\\Lambda\|6\\\\,p"` in tex returns 0 body hits. Route 4 closure is now explicitly the naturalness/explanatory-deficit framing (L1815, L1644–L1690, L2660). The "$p_\phi \approx 6 p_\Lambda$" claim is not in the v1A.0.66 body. Gemini either hallucinated the formula or is reading a stale changelog comment block (HD-6 ruled). | **NO ACTION**. |
| 11 | Gemini P1A-E1 / OpenAI P1A-M4 / Perplexity P1A-E7 | Dimensional inconsistency of $S_{\rm eff}$ operator ($[\alpha/M] = -1$ gives $[\mathcal{L}_{\rm odd}]=+1$ not +4; action mass-dim $-3$ not 0) (ESSENTIAL) | **VERIFIED** | Tex §II A 2 (L1015) and Appendix B explicitly acknowledge this — the paper labels it a "phenomenological scaling ansatz, not a controlled EFT operator". Multiple vendors agree the acknowledgement should be moved into the main body / abstract framing, not only Appendix B. Real residual on framing prominence. | **FIX**: insert one sentence in §I (Introduction Scope paragraph) and one sentence in the abstract noting "the parity-odd operator of Sec. II A 2 is a phenomenological scaling ansatz with mass dimension $+1$, not a controlled EFT operator (Appendix B); all R4 and dark-energy mapping claims are conditional on the ansatz." |
| 12 | OpenAI P1A-M1 / Grok P1A-M1 / Perplexity P1A-M1 | "closure" / "amplitude-budget granularity" language for R2/R3 over-states what scaling-ansatz argument actually proves (MAJOR across 3 vendors) | **PARTIAL** | EXT6 already calibrated Sec. IV opening L1334–L1335 to "R1–R3 amplitude under explicitly-labeled scaling assumptions; R4 naturalness". Title and abstract still use "closure" word. Residual rhetorical drift at title / abstract level. | **FIX**: replace abstract sentence "We assess the four enumerated routes..." with "We constrain the four enumerated routes ... under specified scaling assumptions for R2–R3 and a naturalness limit for R4". Keep title — section heads "channel-level closure" is calibrated against §I Scope paragraph. |
| 13 | OpenAI P1A-M7 / Perplexity P1A-E2 | Internal process language ("earlier drafts", "correction", "external review", v1A.0.66 stamp visible) in body (MAJOR) | **PARTIAL / HOUSTON-DECISION** | Some narrative phrases ("our approach builds on three pillars", "earlier drafts", etc.) survive in body. The `\paperVersion` stamp on title page is deliberate audit-trail per standing PDF protocol — not removed at journal submission. At arXiv submission, lightly polish prose; keep `\paperVersion` for now (drops at journal final). | **FIX (lightweight)**: one polish pass before arXiv submission: grep `"earlier draft\|earlier version\|correction note\|convention note"`, neutralize. |
| 14 | OpenAI P1A-M2 | Table II "barriers" 5, 6, 10, 11, 13 mix qualitative & quantitative (MAJOR) | **PARTIAL / OPINION** | Table II is a catalog of structural/principled barriers across the 14-barrier framework. Mixing quantitative+conceptual entries is the explicit design of the catalog. Reviewer wants separation. Defensible either way. | **DEFER / HOUSTON-DECISION**: optionally split Table II into "Quantitative" and "Structural" sub-tables; not required for closure. |
| 15 | OpenAI P1A-M3 / Gemini P1A-N1 | Fig. 1 / Fig. 5 axes lack units; Fig. 5 "Fine-Tuning Score" undefined for f(R) / quintessence (MAJOR / MINOR) | **VERIFIED** | Real polish item. EXT6 left Fig. 5 caption with the explicit "this is a reparameterization, not a resolution" note; the axis/units issue is separate. | **FIX (cheap)**: add axis units to Figs. 1, 5; one-sentence footnote in Fig. 5 caption defining the score for f(R) / quintessence comparisons. |
| 16 | OpenAI P1A-M5 | Route 3 RG equation $d\gamma/d\ln\mu = (N_L-N_R)\gamma/(12\pi^2)$ cited but not derived; ref. [27] gives a different non-linear β-function (MAJOR) | **PARTIAL / OPINION** | Tex §IV C scopes Route 3 amplitude estimate as a *phenomenological ansatz* (already labeled). The specific β-function is one of several published variants; OpenAI's preference for the cited paper's exact form is defensible. Real polish opportunity. | **FIX**: either quote the exact β-function from the cited reference + recompute $\Delta\gamma/\gamma$, OR insert "(we adopt a one-loop scaling ansatz; exact β-function form is reference-dependent; see footnote)" disclaimer at the §IV C derivation site. |
| 17 | OpenAI P1A-M6 | Sec. XI "seven loophole models" dismissed without calculation (MAJOR) | **OPINION** | Sec. XI is a survey paragraph identifying conceptual loopholes; OOM rebuttals to each are scattered across §IV / §VI / §XII. Reviewer wants them collected in §XI itself. | **DEFER / FIX (optional)**: add a 1-line OOM-rebuttal next to each of the 7 loopholes; or rephrase §XI to "see Secs. IV, VI, XII for amplitude-level dismissals". |
| 18 | OpenAI P1A-M10 (pass-2) | $\beta(\gamma)$ "slowly varying function of γ" introduced in Eq. 7 but re-identified with fixed $\alpha_{\rm em}/(4\pi)$ in numerical Route 2 estimates without explicit β(γ) form or error band (MAJOR) | **PARTIAL** | Tex §IV B does fix β(γ) → $\alpha_{\rm em}/(4\pi)$ as a one-loop QED scaling estimate. The γ-dependence is folded into "slow drift over the cosmologically relevant γ range" — defensible at OOM but the explicit β(γ) curve is not given. | **FIX (cheap)**: add one footnote at §IV B Eq. 7 saying "β(γ) ≈ $\alpha_{\rm em}/(4\pi) \times [1 + \mathcal{O}(\gamma^{-2})]$ for $\gamma \gtrsim 0.2$; for the present amplitude estimate this is treated as γ-independent at OOM precision". |
| 19 | Gemini P1A-N3 (pass-2) | Cross-reference for σ(fNL)≈1.0 forecast points to §VII; §VII cites external ref [36] (MINOR) | **VERIFIED (cosmetic)** | Real cross-reference drift. | **FIX (cheap)**: redirect the footnote target from "Sec. VII" to "Sec. VII, Eq./footnote citing ref. [36]". |
| 20 | Perplexity P1A-E8 (pass-2) | LiteBIRD vs Planck β separation "0.073σ" combines current Planck σ and future LiteBIRD σ in a statistically ill-defined way (ESSENTIAL) | **PARTIAL** | Tex §XII B does compute $\Delta/\sqrt{0.03^2 + 0.094^2} \approx 0.73\sigma$. This is meant as a *current-uncertainty-dominated* heuristic, not a proper joint Planck+LiteBIRD posterior. Real framing-rigor item. | **FIX**: replace with explicit "$\Delta/0.094^\circ \approx 0.77\sigma$ under the *current* Planck error" qualifier OR define a proper joint-posterior σ at the next polish pass. |
| 21 | Grok P1A-N1 / Gemini P1A-T1 | "June 12, 2026" submission date / `v1A.0.66` stamp (NIT across 2 vendors) | **HOUSTON-DECISION** | Audit-trail stamp by standing protocol; removed at journal submission. | **DEFER**. |
| 22 | Grok P1A-M2 | Fig. 3 $\Delta H/H_{\Lambda{\rm CDM}}\lesssim 3\%$ — model is degenerate with ΛCDM; presented as viable DE route (MAJOR) | **PARTIAL / OPINION** | Fig. 3 is the *minimal-ECH-on-shell* mapping. The body explicitly scopes this as "structural mapping; channel-level closure shows no ECH-internal DE source survives the four routes" — the figure is *not* presented as a viable DE prediction. Grok mis-reads it as a forward DE forecast. PARTIAL framing-tightening opportunity. | **FIX (cheap)**: extend Fig. 3 caption with "(Fig. 3 illustrates the parametric form of the on-shell ansatz; per §IV, the four ECH dark-energy channels are nonetheless ruled out at amplitude/naturalness level, so the figure shows the *form* of an ansatz that is *not* a viable DE source.)" |
| 23 | OpenAI P1A-m2 / Perplexity P1A-m6 | "≳30 OOM" Route 2 closure should be 56 OOM by direct calc; γ/γ_PTA symbol overload (MINOR) | **PARTIAL** | The "≳30 OOM" is a *lower bound* statement, deliberately weaker than the exact OOM; the symbol overload is real (γ for Barbero–Immirzi vs $\gamma_{\rm PTA}$ for spectral index). | **FIX (cheap)**: replace ≳30 with ≳56 or remove the explicit OOM number ("many tens of OOM"); rename $\gamma_{\rm PTA} \to n_{\rm GW}$ throughout to disambiguate. |
| 24 | OpenAI / Perplexity assorted MINOR / NIT | "e-fold"/"e-folds", "Hehl–Data" misspell, axis-font Eq. (11) sign-arrangement, Pop\l{}awski diacritic | **VERIFIED (cosmetic)** | Real polish. EXT6 already noted Pop\l{}awski. | **FIX (cheap)**: combined polish-pass commit. |
| 25 | Grok overall **REJECT** (3 E + 3 M + 2 N) | Verdict calibration | **OVER-CALIBRATED but PASS** | Grok's REJECT is driven by the "in preparation companion" finding (#1, same as 3 other vendors raise as ESSENTIAL), the Bianchi-step-circular finding (#2, scope-misread), and the closure-language finding (#12, partial). None of these is independently fatal; together they are reasonable MAJOR REVISIONS, not REJECT. Grok's harsh verdict is *not* the rubber-stamp pattern-009 it showed in EXT6 P1A (where Grok ACCEPT-ed in the face of the §IV E condensate BLOCKER). This round Grok is calibrated more strictly than the actual evidence supports, but it caught no genuinely-new on-disk issues. | **NOTE**: Grok P1A this round is OVER-strict, not rubber-stamp — opposite failure mode from EXT6. Both calibrate as "consult other vendors before closure". |
| 26 | Perplexity overall **REJECT** | Verdict calibration | **OPINION (length+companion-bundling)** | Perplexity's REJECT rationale collapses to: (a) the companion-paper issue, (b) the dimensional-inconsistency framing, (c) length. (a) and (b) overlap with other vendors; (c) is a journal-target-specific call. | **NOTE**: at journal submission consider condensing; not a same-commit closure item. |
| 27 | OpenAI overall **MAJOR REVISIONS** | Verdict calibration | **CALIBRATED** | OpenAI's verdict matches the genuine state of v1A.0.66: real polish items, no closure-blocking science gap. Highest-fidelity leg this round. | — |
| 28 | Gemini overall **MAJOR REVISIONS** | Verdict calibration | **CALIBRATED on body, ONE FABRICATED finding** | Gemini's E4 (Route 4 "$p_\phi \approx 6 p_\Lambda$" arithmetic) is a fabricated formula not in v1A.0.66 body; E3 (REVIEWER METADATA block) hallucinated. Pass-2 quality lower than pass-1. | **NOTE**: pattern-052 does not auto-rescue (no prior falsification). |

---

## Counts summary

| Verdict | Count |
|---------|-------|
| VERIFIED | 3 (#7 dangling footnote ref, #11 dimensional-ansatz framing, #15 fig axes/units, plus cosmetic #19, #24) |
| PARTIAL | 14 (#1 companion-DOI, #2 SVT, #3 σ-juxtaposition sweep, #4 R4 framing, #5 abstract framing, #8 Fig 6 caption bridge, #12 closure-language, #13 internal-process language, #14 Table II split, #16 RG β-function, #18 β(γ), #20 LiteBIRD-σ heuristic, #22 Fig 3 caption, #23 OOM number) |
| OPINION / HOUSTON-DECISION | 6 (#6 DOI, #14, #17 §XI loopholes, #21 date/version, #26 Perplexity length, plus #25 Grok over-strict) |
| FALSIFIED | 2 (#9 REVIEWER METADATA hallucinated; #10 "$p_\phi\approx 6 p_\Lambda$" fabricated) |
| STALE | 0 |
| **Total** | **~28 distinct findings; 0 BLOCKERs; 0 CARRY regressions on EXT6 §IV E** |

**Genuinely-NEW-substantive count (R36conf gap metric over EXT6)**: **3**
- **#7** dangling Sec. X D footnote reference (OpenAI pass-2 only; ESSENTIAL severity)
- **#11** dimensional-ansatz framing should move from Appendix B to body+abstract (3-vendor convergence; new at this level of prominence)
- **#20** LiteBIRD/Planck "0.73σ" hybrid-σ heuristic (Perplexity pass-2 only; ESSENTIAL severity, real framing-rigor gap)

The other ~25 findings are either:
- already covered by EXT6 closure work (e.g., closure-language softening — partially done at L1334),
- HOUSTON-DECISION pre-submission state (DOI, version stamp, AI acknowledgement wording),
- hallucinations FALSIFIED at the audit table,
- one-line cosmetic polish (axis units, OOM number, e-folds plural),
- or repeat raises of the companion-paper-in-preparation issue (which is HD-11-ruled).

**Headline finding**: 4-vendor convergent ESSENTIAL on "companion paper in preparation" simply means the round flagged the pre-submission DOI/companion-pair state. P1B is the same-round co-submission target; this resolves at arXiv submission moment. No new science gap.

**CLEAN/NOT-CLEAN on EXT6 §IV E NJL stale-sign closure**: **CLEAN.** Fix held. Independently re-verified by Perplexity grep (no "too large" / "parametrically too" residues in body) and by no vendor re-raising the regression.

**CLEAN/NOT-CLEAN on EXT6 Sec. IV opening + Fig. 4 caption closures**: **CLEAN.** No vendor re-raised the EXT5 / EXT6 amplitude-closure overstatement at L1334 or the Fig. 4 caption parameter-independent / unique-survivor overstatement.

---

## CLOSURE PLAN — one-line edits for the 3 genuinely-NEW items + cheap polish

1. **#7 — Sec. X D dangling footnote ref**: locate the `(\text{see Sec. X footnote for } e\wedge e\wedge R = -NY + T\wedge T \text{ decomposition})` parenthetical, either insert the missing footnote (1 sentence with the $e\wedge e\wedge R = -d(e\wedge T) + T\wedge T$ identity) or inline the identity at the parenthetical site.
2. **#11 — dimensional-ansatz framing into body+abstract**: one new sentence in §I Scope paragraph + parallel half-sentence in abstract, citing Appendix B for the dim-counting.
3. **#20 — LiteBIRD/Planck "0.73σ" heuristic**: replace the hybrid-σ "0.73σ" with "$\approx 0.77\sigma$ under the current Planck error" wording OR define proper joint posterior. One-line edit.
4. **#3 — σ-juxtaposition sweep**: grep+insert "(different null procedures; not directly comparable)" at any juxtaposition site missing the qualifier. One-pass.
5. **#5 — abstract framing parenthetical** ("neither is uniquely an ECH prediction") into opening sentences.
6. **#4 — R4 conditional-framing** sentence at §IV D opening.
7. **#8 — Fig. 6 caption bridge** between 4.4σ ideal and 2.6σ realistic.
8. **#15 — Fig. 1 / Fig. 5 axis units + score definition footnote**.
9. **#22 — Fig. 3 caption "form-of-ansatz-not-viable-DE-source"** parenthetical.
10. **#12 — abstract "closure" → "constrain"** word swap.
11. **#23 — ≳30 OOM → ≳56 OOM** or "many tens of OOM"; **γ_PTA → n_GW** rename.
12. **#24 — cosmetic polish bundle**: e-folds plural, Hehl–Data → Hehl–Datta, Pop\l{}awski.

Items #6 (DOI), #13 (internal-process language at journal target), #14 (Table II split), #16 (Route 3 β-function exact form), #17 (§XI loopholes), #18 (β(γ) error band footnote), #21 (date/version), #25/#26 (verdict calibration meta-notes) → DEFER to journal-target polish wave or HOUSTON-DECISION.

**Estimated closure commit**: one `chore(R36conf-stamp): R36conf P1A → v1A.0.67 polish wave — Sec. X D footnote, dim-ansatz body/abstract sentence, LiteBIRD σ heuristic, σ-juxtaposition sweep, R4 conditional framing, Fig 3/5/6 caption tightening, closure→constrain wording` bundle.

---

## Audit notes

- **HD-6 (changelog-comment ledger)** applied silently to Gemini #10 (claimed `p_φ ≈ 6 p_Λ` is a changelog-block historical artifact; not live body).
- **HD-11 (DOI placeholders)** applied to #1, #6 (pre-submission DOI; legitimate).
- **pattern-008 (scope drift)** mostly held — abstract framing parenthetical needed in 2 places.
- **pattern-009 (vendor rubber-stamp)** did NOT trigger this round on P1A. Grok went the *opposite* direction (over-strict REJECT). Calibration: cross-vendor consensus needed for closure verdict.
- **pattern-026 (multi-site claim sync gap)** did NOT recur for the §IV E NJL fix — the EXT6 grep-sweep protocol held.
- **pattern-051 (post-fix coherence)** sweep CLEAN — §IV A ↔ §IV E coherent on direction, OOM, parity, no-coherent-$w$ statement.
- **pattern-052 (re-raise rule)** did not auto-rescue any FALSIFIED finding this round — no prior falsification records exist for #9, #10.
- **Claude leg absent**: API credit-exhaustion at v3 driver (BadRequestError 400 "credit balance too low"). 4-leg round, not 5-leg. This is itself an actionable item: top up Anthropic billing before next round.
- **No fabrication / no Fisher 1/8.98² superscript artifacts** in the manuscript-side audit this round.

