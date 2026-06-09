# P1A auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11657 chars)
**Wall time**: 719.6s

---

# PRD Referee Report — P1A
## "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes…"

I have read the paper carefully and audited every figure, table, equation, and reference. I am recommending **REJECT**. The paper is a 23-page null-result essay that overclaims its central contribution, contains multiple internal figure/text inconsistencies, and exhibits clear traces of internal review/version bookkeeping in its body and bibliography. The fundamental theoretical content does not meet the bar for PRD.

---

## ESSENTIAL findings (paper cannot proceed without these)

### P1A-E1 — Figure 3 caption is entirely inconsistent with figure content
**Sec. IX, p. 13.** Caption: "Naturalness landscape for the four minimal-ECH dark-energy routes … each route is shown as a point in the (mass×coupling) plane required to source ρ_Λ at the observed value, with the naturalness window (gray band)…". The actual figure shows **(top)** an "RG running of α/M" line plot in log₁₀(μ/GeV) vs α/M and **(bottom)** a "Dark Energy Fine-Tuning Comparison" bar chart with ΛCDM (10¹²⁰), Quintessence (10⁶⁰), f(R) (10⁴⁰), Spin-Torsion (10⁵). Neither panel is a (mass × coupling) scatter, neither shows the four routes as points, and no gray naturalness window is drawn. The caption describes a different figure that does not exist in the manuscript. **Fix:** Replace either the figure or the caption. As a separate issue, the bar values 10⁴⁰ (f(R)) and 10⁶⁰ (quintessence) are not derived or cited anywhere in the text.

### P1A-E2 — Figure 2 is numerically inconsistent with the body
**Sec. II A, p. 5.** Figure 2 labels the inflationary dilution as "× e⁻³ᴺ (~10⁻⁷²)" and "After inflationary dilution (N = 55 e-folds)". But Sec. II C 1 (p. 7), Sec. XII A (p. 16), and Appendix B (p. 21) all use **N_tot ≈ 92** with **D_inf ~ 10⁻¹²¹**. With N = 55 the dilution is e⁻¹⁶⁵ ≈ 10⁻⁷¹·⁶, giving Ξ ≈ 10⁻⁷⁴ — about 49 orders of magnitude **above** ρ_Λ/M_Pl⁴ ≈ 10⁻¹²³. Figure 2 as drawn does not reach the observed dark-energy density. **Fix:** Regenerate the figure with the self-consistent N ≈ 92, D_inf ≈ 10⁻¹²¹.

### P1A-E3 — Figure 1 uses a PTA value the body explicitly says is superseded
**Sec. I, p. 4.** Figure 1 shows "PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)". But Sec. X G (p. 16) writes: "γ = 2.567 ± 0.382 from real-KDE reanalysis … This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts." Figure 1 displays the superseded number. **Fix:** Update the figure to 2.567 ± 0.382.

### P1A-E4 — Figure 4 includes "Galaxy Spins" curve in detection forecast that contradicts the body
**Sec. XIII, p. 18.** Figure 4 plots "Galaxy Spins" as a forward forecast curve reaching ~4σ by 2034, alongside CMB E-B and a combined curve. But Sec. III B (p. 8), Sec. XIV A 2 (p. 19), and Sec. II C 2 (p. 7) all state the galaxy-spin channel is a **confirmed null** and ECH "underpredicts A₀ by > 100 orders of magnitude". A non-detectable signal cannot have a Stage-IV detection forecast climbing to 4σ. Moreover, the figure caption describes the figure as being about fNL and birefringence, not galaxy spins. **Fix:** Remove the "Galaxy Spins" curve from Fig. 4 (or remove the figure entirely).

### P1A-E5 — Internal review/reviewer metadata appears inside Reference [31]
**Bibliography, ref [31], p. 22.** The entry reads: "…canonical quintom-cosmology review (two-field DE with w crossing −1). **Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers.**, arXiv:0909.2776 [hep-th]." The string "P1A" is the **internal reviewer tag for this manuscript** and the sentence is internal cross-referencing prose. This is reviewer/internal-workflow metadata that has leaked into the bibliography. **Fix:** Remove this prose; bibliography entries must contain only standard bibliographic information.

### P1A-E6 — Internal version-history language pervasive in the body
Multiple appearances of pre-publication bookkeeping that must not appear in a published paper:
- **Abstract footnote (p. 1):** "Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…"
- **Sec. X footnote 2 (p. 16):** "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction…"
- **Sec. X G (p. 16):** "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."
- **App. B (p. 20):** "the ∼ 35 misstated in earlier drafts" and "we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."

**Fix:** Remove all references to earlier drafts, prior errors, and migrations. The final manuscript must read as the current state of knowledge, not a changelog.

### P1A-E7 — Title and abstract overclaim "closure" relative to what is actually shown
**Title, abstract, Sec. IV E.** The title says "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes." But the paper's own Sec. IV D explicitly states that **R4 is not closed** at the amplitude level — it is closed only by a "naturalness objection rather than an amplitude exclusion" with a "free-coupling spectator-ALP fit" that "reproduces both β_obs and ρ_Λ". The paper also admits in Sec. IV "Scope" that two known operators (Jackiw–Pi gravitational Chern–Simons R∧R̃ and the parity-odd four-fermion partner of R1) are excluded from the enumeration. A "closure of four routes" that does not actually close one of them and excludes known operators is mis-titled. **Fix:** The title and abstract must be rewritten to honestly reflect that R1–R3 are amplitude-suppressed, R4 is a naturalness objection, and the operator basis is not complete.

### P1A-E8 — The "perturbation-transparency theorem" is trivial and is not a new result
**Sec. X, pp. 15–16.** The five-step proof is: (i) canonical scalars have zero spin density; (ii) Cartan algebra ⇒ T = 0; (iii) connection becomes Levi-Civita; (iv) the Holst dual ε^μνρσ R_μνρσ vanishes on a Levi-Civita connection by the first (algebraic) Bianchi identity; (v) no EOM contribution. Steps (i)–(iii) are elementary Einstein–Cartan ("Hehl et al. 1976" is cited for exactly this); step (iv) is the standard Bianchi identity contracted against ε^μνρσ — a textbook result; step (v) is a tautology. The claim that this "generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders" is overclaim: the result is order-independent because torsion is **identically** zero (not perturbatively zero) whenever spin density is zero. This is not a "theorem" warranting headline status in a PRD paper. **Fix:** Demote this from a "central result" to an observation/lemma, or remove.

### P1A-E9 — The paper does not establish a new physics result that meets PRD's threshold
The substantive content of the paper is: (a) four channels in minimal ECH cannot generate dark energy at the required amplitude; (b) the two "surviving" observational signatures (fNL = −35/8 and β ≈ 0.27°) are explicitly stated **not** to be ECH predictions — they are matter-bounce-class and GR+ALP-class signatures shared with other UV completions; (c) the dark-energy mapping rests on an admitted phenomenological scaling ansatz with **wrong off-shell mass dimension (+1 vs +4)**; (d) a "structural tension" is identified that further undermines the framework's own internal consistency. The honest summary of the paper is therefore: "minimal ECH does not work as a dark-energy mechanism in any of the four ways we tried, our scaling ansatz has the wrong mass dimension, and the signatures we name are not really our predictions." This is not a result of the kind PRD publishes; it is a negative literature survey with an admitted phenomenological gap. **Fix:** This is structural — the paper would need to either derive a positive result or be redirected to a more appropriate venue (a review, a comment, or a much-shortened technical note).

---

## MAJOR findings

### P1A-M1 — Mass dimension +1 vs +4 is an unresolved EFT problem
**Appendix B, pp. 20–21.** The paper openly admits that the parity-odd operator (Eq. 6) has off-shell mass dimension **+1**, not the **+4** required for a local Lagrangian density, and that ρ_Λ^bounce ~ (α/M) M_Pl⁵ ~ 10⁻² M_Pl⁴ is "a phenomenological on-shell scaling ansatz, not a controlled EFT result." Every numerical estimate in Secs. II C and XII A depends on this ansatz. A paper whose dark-energy mapping is admitted to be off by three powers of M_Pl cannot be the basis of quantitative cosmological conclusions in PRD. **Fix:** Either supply a controlled operator-basis closure (deferred to a "follow-up companion treatment" per App. B) or remove the quantitative dark-energy claims.

### P1A-M2 — "13 logically-independent" vs "14 historical catalog entries" is incoherently presented
Abstract, Sec. IX, Sec. XIII, Sec. XIV E, Sec. XV all use both 13 and 14 with constant footnoting. The reader cannot keep track of which count is intended in any given sentence, and the "B8 is subsumed by B14 but retained for historical mechanism-class completeness" framing is contrived. **Fix:** Drop B8 (or merge it into B14) and report a single, consistent constraint count.

### P1A-M3 — Eq. (7) is undefined
Sec. II A 2, p. 6: α/M ~ (g²/32π²)(γ/M) ln(Λ_UV²/μ²) + δ_NY. The gauge coupling g is not identified (which gauge group?), the Nieh–Yan contribution δ_NY is not given, the UV cutoff Λ_UV is not specified, and the renormalization point μ is not fixed. This equation cannot be used as written. **Fix:** Define every symbol or drop the equation.

### P1A-M4 — Eq. (11) and its "matching" prefactor (T_reh/M_GUT)^(3/2) is admitted to be dimensional-analysis aesthetic
Sec. II C 1, p. 6–7 contains a multi-paragraph defense of why the (T_reh/M_GUT)^(3/2) prefactor in Eq. (11) is "matched to first-principles arguments at the order-of-magnitude level (a fully rigorous first-principles derivation of the half-integer power requires the parity-odd density-of-states phase-space integral, which is dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function)." A central scaling result cannot rest on a prefactor that the authors themselves call "dimensional-analysis aesthetic." **Fix:** Either derive the prefactor or remove the quantitative N_tot ≈ 92 claim.

### P1A-M5 — Route-2 numerical estimate Eq. (15) self-contradicts
Sec. IV B, p. 9. The dimensionless ratio is quoted as "∼ 10⁻⁵⁸ to 10⁻⁶⁰" with a "factor-of-∼100 ambiguity" attributed to "ε-correction perturbative-order scaling alone," but then the text states "An alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio." A 27-order-of-magnitude discrepancy from "reordering" of the same calculation is not "factor-of-∼100." Either the calculation has a 27-OOM systematic error, or two different physical quantities are being conflated. **Fix:** Clarify which contraction is correct and remove the alternative.

### P1A-M6 — Route-4 closure is rebranded as "naturalness objection" without resolution
Sec. IV D, p. 10–11. The text shows that for m_θ = H₀ the spectator-ALP fit reproduces both β_obs and ρ_Λ, but says this re-imports the cosmological-constant problem. However, the structural argument that "the same coupling produces both β_obs and ρ_Λ at m_θ = H₀" is exactly the kind of coincidence that would be considered an attractive *result* in many particle-cosmology papers. The paper closes R4 essentially by deciding to call this coincidence ugly. This is not an amplitude no-go and the manuscript should not market it as a "channel closed." **Fix:** Either accept R4 as a viable spectator-ALP dark-energy mechanism and report it as such, or quantify the naturalness penalty in a defensible way.

### P1A-M7 — N_tot = 92 vs N_tot ≈ 94 inconsistency
Sec. II C 1 gives N_tot ≈ 92; Appendix B gives N_tot ≈ 94. The footnote in App. B acknowledges this "∼ 2% offset" but the rest of the paper uses "92" as if it were a hard prediction. The structural-tension argument (Sec. XIV D) hinges on the gap between ~92 and ~60 e-folds. **Fix:** State a single N_tot value with an uncertainty range, and recompute the structural-tension argument with that range.

### P1A-M8 — "Fine-tuning reduction from 10¹²⁰ to 10⁵" is misleading framing repeated throughout
Sec. II C 1, Sec. XII A. The paper admits explicitly: "we emphasize that this is bookkeeping, not progress … The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions." Yet the "10¹²⁰ → 10⁵" framing reappears in Fig. 3 (bottom panel), in Sec. XII A, and in the executive summary. The paper repeatedly markets a tautology as progress. **Fix:** Remove the "fine-tuning reduction" framing from headline statements and figures.

### P1A-M9 — Reliance on multiple "in preparation" companion papers
Refs [2], [6], [23], [46], [47] are all "in preparation" or "available upon request." The MCMC parameter values quoted in Table IV (H₀ = 67.68 ± 1.06, ΔN_eff = −0.020 ± 0.169, σ₈ = 0.803 ± 0.008, Ω_m = 0.308 ± 0.005) all come from unposted Paper I(b). The "309,189 frozen accepted samples" figure is unverifiable. Similarly, the SPHEREx Fisher 3–5σ figure for fNL is unverifiable; the PTA real-KDE γ = 2.567 ± 0.382 is unverifiable. The paper is not self-contained. **Fix:** Either post the companion papers first or include the relevant material as appendices.

### P1A-M10 — Length grossly disproportionate to content
The paper is 23 pages. The actual content (4 routes fail, plus a trivial observation about scalar matter and torsion) could be presented in 6–8 pages. Repeated restatements of "channel-level closure," "perturbation transparency," and "structural tension" throughout the text — including in the abstract, intro, table captions, multiple sections, conclusions, and footnotes — inflate the manuscript without adding content. **Recommended max for the actual content: 10 pages including references.**

### P1A-M11 — Galaxy-spin discussion is structurally irrelevant
Secs. II C 2, III B, V, VI, XIV A 2, XIV B. The paper admits ECH underpredicts galaxy-spin asymmetry by >100 orders of magnitude. The galaxy-spin null is therefore *not a test of ECH* — it is irrelevant to the framework. Yet the topic is given several pages, an "observational signature" section, a "data methods" section, a "systematic analysis" section, a "discriminating observational channels" section, and a "robustness to galaxy spin null results" section. **Fix:** Remove the galaxy-spin discussion (it belongs in Paper IV).

### P1A-M12 — Eq. (12) is asserted without derivation
Sec. III A. The standard cosmic-birefringence formula C_ℓ^EB ≈ 2β(C_ℓ^EE − C_ℓ^BB) is quoted but the paper then admits: "Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here." The paper therefore cites a formula for which it does not derive the input. **Fix:** Either provide the photon-torsion coupling derivation or remove the equation.

### P1A-M13 — Table I "Status" column for the central question
Page 4: "Can bounce derive dark energy? / 14 constraints map minimal-ECH route space / **Phen. assumption^a required.**" This is a non-answer dressed as an answer. The honest entry is "No (under stated assumptions)" or "Not closed." **Fix:** Replace with an honest verdict.

### P1A-M14 — Sentences with multi-line nested parentheticals are unreadable
Examples: the abstract sentence beginning "(a contracting-phase quantity mode with k_SPHEREx…" runs ~10 lines with three levels of nesting. Sec. I A bullet 2 has similar structure. Sec. XIV D as well. **Fix:** Rewrite into separate sentences.

---

## MINOR findings

### P1A-N1 — Abstract length
The abstract spans roughly 1.5 pages of body text. PRD does not have a hard word limit but ≤300 words is conventional. Current abstract is ~1500+ words. **Fix:** Cut by 80%.

### P1A-N2 — AI assistance acknowledgment
"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author." Given the bibliographic and figure inconsistencies I have flagged above, the verification claim is not credible. The acknowledgment is appropriate but should be supplemented with disclosure of how verification was actually performed.

### P1A-N3 — Ref [47] is "available upon request from the author"
This is not acceptable for a PRD reference. **Fix:** Either remove the citation or post the note publicly.

### P1A-N4 — Funding/computational disclosure
"Computational resources were self-funded (RunPod H200 and H100 instances)." Vendor names are not typical in PRD acknowledgments; "self-funded GPU compute" suffices.

### P1A-N5 — Footnote 1 (p. 11) on the 3–5σ range
The footnote re-derives a Fisher-ideal 6.25σ that is then degraded to "3–5σ realistic after full systematic budget" by uncited template-overlap correction r ≈ 0.84 and "GR-projection and b_φ degradation" of unspecified magnitude. The range "3–5σ" therefore spans a factor of ≈1.7 in significance with no quantitative justification beyond a hand-wave.

### P1A-N6 — Eq. (15) eV/GeV unit mixing
"the eV-vs-GeV unit conversion is exact 1 GeV = 10⁹ eV and is not a source of ambiguity" — true but irrelevant; the OOM ambiguity claimed in the same sentence is 10² to 10²⁷, which is *not* the unit conversion. Drop this aside.

### P1A-N7 — Table III "Quintom-B" row
The "consistent†" entry, with a footnote explaining that the chain has not actually been run, is presented as if it were a result. It is not. **Fix:** Either run the chain or remove the row.

### P1A-N8 — Repeated phrase tic
"channel-level closure" appears 20+ times. "structural barriers" appears 15+ times. "perturbation transparency" appears 10+ times. The repetition reads as marketing.

### P1A-N9 — Table I footnote (c): "Class-level: scalar-only w = 0 matter-bounce under Assumption (f) of the companion forecast [2]; not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction."
This footnote concedes that the surviving prediction is neither universally applicable nor distinctive to ECH. The Table I entry "Testable prediction? Yes, class-level" is therefore an overstatement. **Fix:** Replace with "Class-level only; not distinctive to ECH."

### P1A-N10 — γ_SU(2) ≈ 0.274 "uncertainty range" framing
Sec. II A 1 says "the apparent uncertainty range is scheme dependence rather than a statistical or theoretical error." Good clarification, but then Table IV says "0.274 (scheme range ∼0.020)" without indicating this is not a propagatable error bar. **Fix:** Add a parenthetical "(scheme-dependence range; not propagated as statistical uncertainty)."

### P1A-N11 — Bibliography styling
Several references have inconsistent journal abbreviation styles ("Phys. Rev. D" vs "Physical Review D" vs "Phys. Rev. Lett." vs "Physical Review Letters"). **Fix:** Use one style consistently.

---

## NITS

### P1A-NIT1 — Eq. (3) introduces S^abc = (1/4) ψ̄ γ^[a γ^bc] ψ but later writes (Eq. 4 and Sec. IV A) ψ̄ γ^[a γ^b γ^c] ψ. Either form is fine but the manuscript should pick one.

### P1A-NIT2 — Sec. IV A: "where κ = 1/M_Pl² and n_ψ has mass-dim +3" — should be "κ = 1/M_Pl² (in units where 8π is absorbed)" or κ = 8πG explicitly; the parenthetical conflict with the immediately preceding "κ = 8πG" is sloppy.

### P1A-NIT3 — Fig. 4 caption says "Detection forecast for the two surviving mechanism-independent tests" but the figure shows three curves (CMB E-B, Galaxy Spins, Combined). Two vs three mismatch.

### P1A-NIT4 — Reference [22] should give the actual journal page; "Annalen Phys. 520, 693 (2008)" — verify.

### P1A-NIT5 — Fig. 2 description includes "ΛCDM" axis label that is not explained in the caption.

---

## Audit of headline numbers (recomputed)

| Quantity | Paper value | My recomputation | Verdict |
|---|---|---|---|
| ρ_Λ / M_Pl⁴ | 10⁻¹²³ | (2.3 meV)⁴/M_Pl⁴ = 1.4×10⁻¹²³ | ✓ |
| ρ_crit at γ=0.274 | 0.27 ρ_Pl | √3/(32π²·0.274³) = 0.267 | ✓ |
| ρ_crit at γ=0.2375 | 0.41 ρ_Pl | √3/(32π²·0.2375³) = 0.410 | ✓ |
| N_tot for D_inf ~ 10⁻¹²¹ | 92 | 121·ln10/3 = 92.9 | ✓ |
| N_tot for full M_Pl⁴ hierarchy | 94 | 122·ln10/3 = 93.6 | ✓ (but inconsistent with the 92 quoted in body) |
| Fig. 2 dilution 10⁻⁷² → N = ? | "N = 55" | 72·ln10/3 = 55.3 | ✓ internally, but inconsistent with body's 92 |
| Route-2 ratio | 10⁻⁵⁸ to 10⁻⁶⁰ | 10⁻⁶⁰ | ✓ (but see M5: alternative ordering gives 10⁻³³) |
| Spectator-ALP ρ_θ at m_θ=H₀ | ≈ ρ_Λ | 4×10⁻¹¹ eV⁴ vs ρ_Λ ≈ 2.8×10⁻¹¹ eV⁴ | ✓ |
| LiteBIRD discrimination 0.27° vs 0.342° | 0.73σ | 0.072/√(0.03²+0.094²) = 0.73 | ✓ |
| PTA γ tension (γ_pred=3 vs 2.567±0.382) | +1.13σ | 0.433/0.382 = 1.13 | ✓ |
| β_obs from WMAP+Planck | 3.6σ | 0.342/0.094 = 3.64 | ✓ |
| ACT DR6 β | 2.9σ | 0.215/0.074 = 2.91 | ✓ |

Numerical audit is generally OK; the worst issues are **internal inconsistencies between figures and body** (P1A-E2, P1A-E3) and the **27-OOM "alternative ordering" footnote** in Route 2 (P1A-M5).

---

## Summary recommendation

**REJECT.**

The paper is a 23-page null result that markets itself as a structural advance while admitting in its own abstract that (a) the four enumerated routes are not a complete operator basis, (b) the dark-energy mapping rests on a scaling ansatz with the wrong off-shell mass dimension, (c) the two "surviving predictions" are not ECH predictions at all, and (d) an internal structural tension between the dark-energy mechanism and the matter-bounce fNL signature exists. The central "perturbation-transparency theorem" is the elementary observation that canonical scalars source no spin density and therefore no torsion, dressed up to all perturbation orders trivially. Figures 1, 2, 3, and 4 each contain inconsistencies with the body or with each other. Internal version-history language and at least one reviewer-tag string ("P1A") have leaked into the published text and bibliography. Quantitative results depend on four "in preparation" companion papers. The honest physics content of this manuscript — that minimal Einstein–Cartan–Holst gravity does not provide a controlled dark-energy mechanism through the four standard routes — is correct, well-known to specialists, and not a result of the kind PRD publishes. The author may wish to recast a much shorter version (≤ 8 pages) as a comment or a focused technical note in a more appropriate venue after fixing the figure/text inconsistencies and removing all internal bookkeeping.

---

## PASS 2 — self-critique findings (what initial review missed)

# PRD Referee Report (Continued) — Second-Pass Findings

After a focused re-audit driven by the arithmetic / cross-reference / abstract-faithfulness / appendix-mismatch checks, I find substantial **new** issues that escaped the first pass. Several change the verdict landscape (e.g., the headline N_tot = 92 depends on a prefactor the paper itself calls "aesthetic"; the headline β = 0.27° is a stale prediction-target).

---

## ADDITIONAL ESSENTIAL findings

### P1A-E10 — β ≈ 0.27° is a stale prediction-target, inconsistent across the manuscript
**Sec. III A vs Sec. IV D vs Sec. XII B vs Sec. XV vs Fig. 1.** The "predicted/expected" cosmic-birefringence angle is reported inconsistently:
- **Sec. III A (p. 8):** "qualitatively consistent with the observed isotropic birefringence at **β ≈ 0.27°–0.30°**" — this is the original Minami & Komatsu (2020) value, **stale** by ≥ 5 years.
- **Sec. IV D (p. 10), Sec. XII B (p. 17):** correctly cite β_obs = **0.342° ± 0.094°** (Eskilt & Komatsu 2022) and 0.215° ± 0.074° (Diego-Palazuelos & Komatsu 2025).
- **Sec. XV, Fig. 1, Table I/Table IV, Abstract:** treat **0.27°** as the *spectator-ALP-derived* prediction.

So the paper uses 0.27° as both "the observed value" (Sec. III A) and "the model-derived prediction" (Sec. XV, Fig. 1). The 0.27° is in fact neither: it is the obsolete 2020 observation that has been superseded. **There is no derivation anywhere in the paper of "0.27°" as a spectator-ALP prediction.** Sec. IV D shows that fitting α/M ~ 10⁻²¹ GeV⁻¹ to β_obs by construction reproduces β_obs = 0.342°, *not* 0.27°. **Fix:** Either (i) derive 0.27° from first principles, (ii) update Sec. III A to the current measurements, or (iii) acknowledge 0.27° is a stale value and remove it from the surviving-prediction list.

### P1A-E11 — Table I status entry contradicts the question it answers
**Table I, p. 4, last row.** "Question: H₀/σ₈ tension resolution? / Result: H₀ = 67.68 ± 1.06, ΔN_eff ≈ 0 / Status: **Recovers ΛCDM**." Recovering ΛCDM is precisely *not* resolving the H₀/σ₈ tension — ΛCDM is the model that *has* the tension. The status entry literally contradicts the question. **Fix:** Replace "Recovers ΛCDM" with "Does not resolve" or "No tension resolution."

---

## ADDITIONAL MAJOR findings

### P1A-M15 — The headline N_tot = 92 depends entirely on a prefactor the paper calls "aesthetic"
**Sec. II C 1 vs Appendix B.** I traced the two values explicitly:
- Sec. II C 1: matching ρ_Λ ≈ (2.3 meV)⁴ with D_inf = e^(−3N_tot) × (T_reh/M_GUT)^(3/2) requires e^(−3N_tot) × 0.03 = 10⁻¹²¹, giving N_tot = 91.7 ≈ 92.
- App. B: matching the same ρ_Λ with D_inf = e^(−3N_tot) alone gives 122 ln10/3 ≈ 93.6 ≈ 94.

The **only reason** the headline figure is 92 rather than 94 is the inclusion of the (T_reh/M_GUT)^(3/2) ≈ 0.03 prefactor that Sec. II C 1 itself describes as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function." Yet N_tot = 92 (not 94) is the value used to compute the structural-tension argument in §XIV D and the abstract (e^32 = e^(92−60), not e^34). Removing the aesthetic prefactor would shift the structural-tension differential from e^32 to e^34. The "∼2% offset" framing in App. B's footnote understates this — the headline N_tot is exposed to a prefactor admitted to be uncalculated. **Fix:** State this dependence explicitly in the abstract and §XIV D.

### P1A-M16 — Sec. VII overclaims LiteBIRD discrimination power; Sec. XV correctly walks it back
**Sec. VII (p. 11) vs Sec. XV (p. 20).** Sec. VII says LiteBIRD will "either confirm a non-zero birefringence at high significance **or rule out the spectator-ALP class** as the source of the WMAP+Planck birefringence signal." But Sec. XV explicitly computes that the discrimination between the "spectator-ALP-derived 0.27°" and the observed 0.342° at LiteBIRD precision σ(β) = 0.03° is **0.73σ**, with the explicit acknowledgment "LiteBIRD's σ(β) = 0.03° will not by itself separate the spectator-ALP value from the current WMAP+Planck birefringence central value in a model-discrimination test." Sec. VII's "rule out" framing is inconsistent with Sec. XV's own analysis. **Fix:** Update Sec. VII to match Sec. XV's caveat.

### P1A-M17 — Sec. IV D admits the spectator-ALP route fits both β_obs and ρ_Λ; the "0.27° prediction" is therefore a derivation gap
**Sec. IV D, p. 10–11.** The text explicitly derives that for m_θ ~ H₀ and α/M ~ 10⁻²¹ GeV⁻¹ (the value fitted from β_obs), the spectator-ALP setup produces ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴ ≈ ρ_Λ. **In this fit, β is by construction β_obs = 0.342°** (the fit input), *not* 0.27°. There is no separate calculation in the paper that produces 0.27° as a derived value of β. Yet Sec. XV, Fig. 1, and the abstract treat 0.27° as if it were a model prediction. Either the paper produces an actual derivation that yields 0.27° (rather than fitting α/M to β_obs by construction), or it admits 0.27° is not a prediction. **Fix:** Derive 0.27° from inputs that are not fits to β, or remove the "0.27° prediction" framing.

### P1A-M18 — Footnote 1 template-overlap correction (5–5.5σ) uses an incorrect projection formula
**Footnote 1, p. 11.** The text: "raw ratio |f_NL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84." The math 6.25 × 0.84 = 5.25 is shown, but this is *not* the correct way to apply a template overlap. For two correlated bispectrum templates with overlap r, the marginalized constraint widens to σ_marg = σ_unmarg/√(1 − r²). For r = 0.84, this gives σ_marg = σ/0.542 = 1.85σ_unmarg, so |f_NL|/σ_marg = 6.25/1.85 ≈ **3.4σ**, not 5.25σ. The "5–5.5σ optimistic" significance is overstated by ≈ 1.5–2σ. Combined with the σ(f_NL) ≈ 1.0 realistic regime (giving 4.4σ direct or 2.4σ marginalized), the honest range is approximately **2.4–4.4σ**, not "3–5σ realistic". The decisive discrimination claim against slow-roll inflation in the abstract is correspondingly weaker. **Fix:** Apply the correct projection formula and update all "3–5σ" cross-references.

### P1A-M19 — Sec. III A treats β = 0.27°–0.30° as observed; this is a 5-year-stale dataset
**Sec. III A (p. 8).** "The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°." The 0.27°–0.30° range corresponds to the original Minami & Komatsu (2020) measurement, superseded by Eskilt & Komatsu (2022) at 0.342° ± 0.094° and Diego-Palazuelos & Komatsu (2025) at 0.215° ± 0.074°. The paper cites both updated measurements elsewhere (Sec. IV D, XII B) but Sec. III A still uses the original range. **Fix:** Update Sec. III A to the current measurements.

### P1A-M20 — The c_ω ω² term in Eq. (10) is included but never used; it is a relic of the deprecated cosmic-rotation framework
**Eq. (10), p. 6.** Λ_eff = Ξ M²_Pl + c_ω ω². The text immediately says "CMB isotropy bounds give (ω/H)₀ < 5 × 10⁻¹¹, making rotation completely negligible." If rotation is negligible by 22 orders of magnitude, why is the term in the parameterization at all? This appears to be a vestige of an earlier "cosmic rotation as dark energy" framework that was scrapped during revisions but whose syntactic remnant survives. The paper now centers on parity-odd torsion rather than rotation. **Fix:** Drop c_ω ω² from Eq. (10) or explain its current relevance.

### P1A-M21 — Fig. 1 labels f_NL = −35/8 as "mechanism-indep." while body Table I footnote (c) explicitly denies this
**Fig. 1 (p. 4) vs Table I footnote (c) (p. 4).** Fig. 1's right column reads "f_NL = −35/8 SPHEREx, **mechanism-indep.**" But Table I footnote (c) on the same page says: "Class-level: scalar-only w = 0 matter-bounce under Assumption (f) of the companion forecast; **not fully mechanism-independent across the bouncing-cosmology landscape**." Sec. XIII (1) repeats the caveat. The figure label and the table footnote on the *same page* contradict. **Fix:** Update Fig. 1 label to "class-level (matter-bounce)" or equivalent.

### P1A-M22 — "Scheme range ∼0.020" for γ_BI does not correspond to any cited pairwise difference
**Sec. II A 1 (p. 5) and Table IV (p. 21).** The text lists three counting schemes: γ_U(1) ≈ 0.127, γ_DLM ≈ 0.2375, γ_SU(2) ≈ 0.274. The pairwise spreads are: U(1)–DLM = 0.110, DLM–SU(2) = 0.037, U(1)–SU(2) = 0.147. **None of these equals ∼0.020.** Yet Table IV records "0.274 (scheme range ∼0.020)" and Sec. II A 1 calls the ∼0.020 a "spread between counting prescriptions." There is no pair of schemes that yields 0.020. The figure appears to be unattested. **Fix:** Identify the source of the 0.020 figure or replace it with the correct DLM–SU(2) spread of 0.037 (or 0.147 if including U(1)).

### P1A-M23 — Fig. 3 top panel shows an RG running of α/M not derived in the text
**Fig. 3 top panel (p. 13).** The figure shows α/M running from ≈ 4 × 10⁻²² at log₁₀(μ/GeV) = −12 ("Present") to 10⁻²¹ at log₁₀(μ/GeV) = +19 ("M_Pl"), with a smooth log-linear trajectory. But the text's only β-function discussion is for γ (Eq. 16, Sec. IV C), not for α/M. Eq. (7) provides only the one-loop *value* of α/M, not its β-function. The trajectory shown in Fig. 3 top has no derivation. **Fix:** Either derive the running of α/M shown in the figure or remove the panel.

### P1A-M24 — "Reheating thermal-reset barrier" expression in Sec. II C 1 is dimensionally questionable
**Sec. II C 1, p. 7.** The text writes: "the r.m.s. residual scales as ∼ √(n_ψ/T^(1/2)_reh) under standard fluctuation-dissipation counting and vanishes in mean." With n_ψ having mass dim +3 and T_reh^(1/2) having mass dim +1/2, the ratio n_ψ/T_reh^(1/2) has mass dim +5/2 and the square root has dim +5/4 — which is not the mass dim of any quantity ⟨J^5⟩ (dim +3) or related fluctuation amplitude (dim +3/2 for r.m.s. number density fluctuation). The expression as written is dimensionally inconsistent. Either the formula is mistyped or the dimensional balance requires unstated factors. **Fix:** Repair the dimensional balance or rewrite the formula.

### P1A-M25 — Appendix B hierarchy "10¹²²" vs body's "10⁻¹²³" inconsistency
**Appendix B, p. 21.** App. B writes "the genuine cosmological-constant hierarchy is M_Pl⁴/ρ_Λ^obs ~ 10¹⁹×⁴/(10⁻³ eV)⁴ ~ 10¹²²". Computing this rigorously: M_Pl⁴ ≈ 2.2 × 10⁷⁶ GeV⁴; ρ_Λ ≈ (2.3 × 10⁻³ eV)⁴ = 2.8 × 10⁻⁴⁷ GeV⁴; ratio ≈ 8 × 10¹²² ≈ **10¹²³**, not 10¹²². The body (Sec. XII A) uses Ξ ≈ 10⁻¹²³ consistently. App. B's "10¹²²" is off by a factor of 10. This is small but propagates: the N_tot ≈ 94 in App. B derives from "122 ln 10/3 ≈ 94"; with the correct 123 it should be "123 ln 10/3 ≈ 94.4" — still rounds to 94 but introduces yet another N_tot variant.

---

## ADDITIONAL MINOR findings

### P1A-m26 — Sec. XV computes "9σ overall sensitivity" by mixing null procedures
**Sec. XV (p. 20).** "LiteBIRD detects non-zero β at ∼9σ (a 0.27°/0.03° overall sensitivity number)." The 9σ is *detection against β = 0*, while the 0.73σ later in the same paragraph is *model discrimination against the observed central value*. Putting both numbers in the same sentence without saying which null is which invites the reader to conflate "detection" with "discrimination" — a common error in null-procedure communication.

### P1A-m27 — The 32 e-fold differential is reported alternately as "physical scale" and "comoving scale" ratio
**Abstract, Sec. I A bullet 2, Sec. XIV D.** The formula k^phys_bounce ~ k^phys_SPHEREx × e^32 is written with both k^phys labels, where "k^phys_SPHEREx" implicitly means "k^phys at horizon exit of the SPHEREx-accessible comoving mode" but is not labeled as such. Readers may be confused whether the reference scale is k_phys today, k_