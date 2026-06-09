# P1A auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11782 chars)
**Wall time**: 623.2s

---

# Referee Report — P1A (Channel-Level Closure of Four Minimal ECH Dark-Energy Routes)

I have read the manuscript in detail, examined the figures and tables, recomputed the load-bearing scalars, and traced cited claims to the bibliography. My overall conclusion is given at the end; below are the findings in order of severity.

---

## ESSENTIAL findings (paper cannot be accepted without fixing these)

**P1A-E1. Title and abstract overclaim relative to Section IV D.**
The title is "Channel-Level Closure of Four Minimal ECH Dark-Energy Routes," and the abstract repeatedly asserts that the four routes "each fails at the amplitude level under stated assumptions." But Section IV D (Route 4, p. 10–11) explicitly states: *"R4 is therefore not closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H₀ ... Route-4 status: a naturalness objection rather than an amplitude exclusion. ... the channel is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level."* This directly contradicts the abstract. **Required fix:** Rewrite the title and the abstract's opening sentence to say "three routes fail at the amplitude level; the fourth is closed only by a naturalness/explanatory-deficit objection," or remove the "amplitude" framing entirely.

**P1A-E2. Massive load-bearing dependence on "in preparation" companion papers.**
The paper repeatedly cites Paper I(b) [6], Paper II [2], Paper III [46], and Paper IV [23] — all by the same author, all "in preparation," all unposted — as the substrate for the load-bearing numerical claims it summarizes (H₀ = 67.68±1.06, ΔN_eff ≈ 0, the MCMC convergence statistics, the σ(f_NL) ≈ 0.7 forecast, the γ_PTA = 2.567±0.382 PTA reanalysis, the galaxy chirality null, the NaMaster validation, the ALP MCMC fits). The author even concedes (p. 5): *"they are documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted."* PRD does not accept submissions that rest on companion work that is not at minimum posted to arXiv at the time of submission. **Required fix:** Either post the companion papers and replace internal cross-references with public arXiv IDs, or remove every claim that depends on them and the corresponding tables/figures (Table I row "H₀/σ8 tension resolution," Table IV cosmological-parameters and PTA rows, Fig. 4).

**P1A-E3. Reference [47] is a "companion technical note, available upon request" — i.e., not publicly available.** It is cited in §XII B as the basis for the "no photon coupling in the minimal framework" closure. PRD policy does not accept "available on request" as a reference for load-bearing claims. **Required fix:** Post or remove.

**P1A-E4. Reference [44] cites a future arXiv ID that may not exist.** "Y.-F. Cai and J.-H. Zhu, ... (2026), arXiv:2603.13924." The number 2603 indicates March 2026; the paper is dated June 2026. The citation must be verified against the actual arXiv listing; in the form given, it is not traceable. **Required fix:** Verify or remove.

**P1A-E5. Figure 3 caption does not match the panels.**
The caption (p. 13) describes a "Naturalness landscape for the four minimal-ECH dark-energy routes ... shown as a point in the (mass×coupling) plane required to source ρ_Λ at the observed value, with the naturalness window (gray band) ... All four routes either sit outside the naturalness window or require a m_θ ∼ H₀ tuning." But the figure actually shows **(top)** an "RG running of α/M" line plot and **(bottom)** a "Dark Energy Fine-Tuning Comparison" bar chart with rows for ΛCDM, Quintessence, f(R) Gravity, and Spin-Torsion (this work). Neither panel is a (mass × coupling) scatter plot of the four routes; neither shows a naturalness window/gray band. **This is a hard caption-vs-figure mismatch on a featured figure.** **Required fix:** Either replace the figure with the one described in the caption, or rewrite the caption to describe what is actually plotted.

**P1A-E6. Version-history / internal-audit language in the body and footnotes.**
The following pieces of version-control prose appear in the published paper text and must be removed:
- Footnote a (front matter, repeated on p. 2): *"Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."*
- Footnote 2 (p. 16): *"An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density. The correction (Bianchi-vanishing rather than Pontryagin-total-derivative) preserves the headline perturbation-transparency conclusion..."*
- §X G (p. 16): *"This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."*
- Appendix B (p. 20): *"(not the ∼ 35 misstated in earlier drafts: ..."*
- Appendix B (p. 20): *"we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."*

These are review-log/version-history artifacts that have no place in the published paper. **Required fix:** Remove all such language; the corrected statement stands on its own without reference to the prior error.

**P1A-E7. The dimensional analysis underlying the entire dark-energy mapping is admitted to be ad hoc, and the abstract softens it inappropriately.**
Appendix B (p. 20) admits the parity-odd operator has off-shell mass dimension +1, not +4, and that the identification ρ_Λ = Ξ M_Pl⁴ is "a phenomenological on-shell scaling ansatz, not a controlled EFT result." Yet the abstract refers to it as "phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4" without making clear that the entire dark-energy mapping (and hence the "closure" of routes against it) is conditional on this dimensionally-inconsistent ansatz. **A "closure" of a mechanism that requires an ad hoc dimension-uplift to even be defined is not a closure; it is a closure conditional on a not-derived ansatz, applied to a not-derived target.** **Required fix:** Either upgrade to a controlled EFT calculation or state explicitly in both the title and abstract that the closure result is conditional on a dimensional ansatz whose status is not derived.

**P1A-E8. Equation (15) and the surrounding Route 2 dimensional analysis are internally inconsistent.**
The text on p. 9 explicitly admits: *"the eV-vs-GeV unit conversion is exact 1 GeV = 10⁹ eV and is not a source of ambiguity ... an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio."* A factor of ∼10²⁷ ambiguity between two "orderings" of the same dimensional reduction is not a small thing in a load-bearing amplitude no-go. The fact that the paper hedges with "the qualitative closure statement ... survives any reasonable dimensional reconciliation" is not adequate. **Required fix:** Perform the calculation once, correctly, with explicit dimensions on every factor; do not present two values differing by 27 orders of magnitude and assert that the closure survives either.

**P1A-E9. The "definitively erased" structural tension contradicts the survival of f_NL = −35/8.**
The abstract and §XIV D claim that N_tot ≈ 92 e-folds (required for the dark-energy mechanism) would "definitively erase" the matter-bounce f_NL = −35/8 signature at SPHEREx scales. The paper then claims f_NL = −35/8 as a surviving testable prediction. The author resolves this by saying the predictions belong to two different model classes (dark-energy-sourcing ECH vs. bounce-class generically), but this is exactly the point: **the paper claims that the dark-energy mechanism is closed AND that the bounce prediction survives — but the bounce prediction survives only if one rejects the dark-energy mechanism.** Saying "these are independent observational programs" is not a resolution; it is an admission that the framework cannot simultaneously provide both. **Required fix:** State unambiguously, in one place, that the framework cannot do both; remove the framing that the surviving prediction is in any sense a prediction of the present framework.

**P1A-E10. Sigma juxtapositions without "not directly comparable" qualifications.**
The paper cites β_obs = 0.342° ± 0.094° (WMAP+Planck, "∼3.6σ from β=0") next to the ACT DR6 follow-up β = 0.215° ± 0.074° ("∼2.9σ") and asserts they are "consistent within ∼1.4σ" without noting that these are entirely different analyses with different null hypotheses, different sky cuts, and different polarisation-angle calibration assumptions. The "1.4σ" consistency calculation is not justified anywhere; |0.342−0.215|/√(0.094²+0.074²) = 0.127/0.120 ≈ 1.06σ, not 1.4σ. **Required fix:** Either justify the 1.4σ number with the actual calculation (including correlated systematics) or report the correct ∼1.1σ Gaussian-quadrature value, and state explicitly that the two measurements are not directly comparable at face value.

---

## MAJOR findings (significant revision required)

**P1A-M1. Abstract is too long and inappropriate in style for PRD.**
The abstract runs more than a full column with embedded multi-line equations, parenthetical formula derivations ("k_phys_bounce ∼ k_phys_SPHEREx e^(N_tot − N_exit) ∼ e³² ..."), and self-referential meta-comments about scope. PRD abstracts should be a single paragraph of ∼250 words. **Required fix:** Cut to one paragraph; move scope/limitations to §I.

**P1A-M2. The "perturbation transparency theorem" is not novel; it is a near-trivial consequence of textbook identities.**
The claim is: with no spin density, T = 0, the connection is Levi-Civita, and ε^μνρσ R_μνρσ vanishes by the first Bianchi identity. This is correct, but it is a one-line observation that has been implicit in every ECH/LQG treatment for forty years. Presenting it as "the central result" and "a perturbation-transparency theorem" (the abstract gives it top billing) is an overclaim. **Required fix:** Demote to a remark, or demonstrate explicitly what prior literature missed.

**P1A-M3. Inconsistency in the description of the "13 logically-independent / 14 historical catalog" barriers.**
The paper repeatedly says there are "13 logically-independent" barriers but lists 14, with B8 subsumed by B14. The catalog (Table II) presents 14 rows; the prose treats them as if they are non-overlapping; Barrier 13 ("Gravitational Democracy") is itself labelled "structural/philosophical observations" (p. 12) and is not a derivation; Barriers 5, 6, 7, 9 are labelled "known results" (i.e., not the author's contribution). Effectively the paper presents perhaps 4–5 ECH-specific calculations plus 9 already-known or qualitative observations and counts them all toward "channel-level closure." **Required fix:** Be explicit in the abstract and §IX about how many barriers are (a) novel calculations, (b) restatements of standard results, (c) qualitative observations, rather than blurring them into a single "14 constraints" headline.

**P1A-M4. The galaxy-spin discussion adds no signal but inflates the paper.**
The paper acknowledges (p. 7, p. 11, p. 19) that the ECH parity-odd coupling "underpredicts any plausible spin asymmetry by > 100 orders of magnitude" — i.e., the framework predicts a null, and the observation is null. This contributes zero constraining power but is treated as a confirmation of the framework, and occupies §III B, §V, §VI, §XIV B with discussion. **Required fix:** Consolidate to one paragraph noting that the channel is not predictive within the framework and the null is unsurprising; remove the framing as "a confirmed null" supporting the theory.

**P1A-M5. Figure 4 shows "Galaxy Spins" approaching ∼3σ "detection significance" by 2030 even though the paper's own text says the framework predicts no detectable galaxy spin signal.**
This is an internal contradiction between Fig. 4 and the body text. **Required fix:** Remove the galaxy-spins curve from Fig. 4 or relabel it; do not present a "detection forecast" for a channel the paper says is unobservable in principle.

**P1A-M6. Table III final column ("w₀w_a DESI") is honest but unhelpful.**
The footnote ‡ admits that none of the rows were tested against the DESI w₀w_a evidence ("the frozen MCMC posteriors hosted in Paper I(b) ... contain zero free-w₀w_a samples"). A new chain is admitted to be running ("Rˆ − 1 ≈ 3 × 10⁻²"). The column therefore has no content. **Required fix:** Remove the column until the chain converges; do not present an empty discrimination claim.

**P1A-M7. Equation (11): the (T_reh/M_GUT)^(3/2) prefactor is explicitly "dimensional-analysis aesthetic" and not derived.**
The author admits in §II C 1, §XII A, and elsewhere that the half-integer power is order-of-magnitude motivated rather than calculated. This prefactor is one of the two factors carrying the entire N_tot ≈ 92 numerology. **Required fix:** Either derive it, or remove the headline "fine-tuning reduced from 10¹²⁰ to 10⁵" claim, which inherits its precision from this prefactor.

**P1A-M8. Equation (10) and Appendix B: the dimensional reconciliation between ρ_Λ^bounce ∼ (α/M) M_Pl⁵ and the operator written in Eq. (6) is internally inconsistent.**
Eq. (6) gives [L_odd] = +1; the ρ_Λ^bounce = (α/M) M_Pl⁵ relation in Eq. (B2) carries dimension +4 — that means three additional powers of mass have been pulled in *between* Eqs. (6) and (B2). The author admits the operator must "carry three additional powers of M_Pl in its coefficient (α/M → α M_Pl³ / M)" to make this work. But then the "α/M ∼ 10⁻²¹ GeV⁻¹" estimate quoted throughout — which is the value used in the Route 4 analysis (§IV D) — cannot be the same coupling as the one used in Eq. (B2). The two halves of the paper are using "α/M" to mean different things. **Required fix:** Use distinct symbols, or commit to one definition and propagate consistently.

**P1A-M9. The "8" in the f_NL = −35/8 sigma forecast is double-counted.**
Footnote 1 (p. 11) says σ(f_NL) ≈ 0.7 Fisher-ideal gives |f_NL|/σ = 4.375/0.7 ≈ 6.25σ, "degraded to ∼5–5.5σ optimistic after template-overlap correction ... and σ(f_NL) ≈ 1.0 after GR-projection and photo-z marginalization (3–5σ realistic)." Then the text in §VII calls it "3–5σ realistic." Then §XV says "3–5σ realistic significance." But the abstract and Table I use "3–5σ realistic" without ever defining whether this is bispectrum-only or post-systematic. **Required fix:** Quote one number with a single set of assumptions, in the abstract and throughout; do not migrate between regimes.

**P1A-M10. The "factor of ∼9σ" LiteBIRD-vs-zero claim in §XV is misleading.**
The text says "LiteBIRD ... detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)." This is a sensitivity number, not a detection significance against a meaningful null. The relevant test is exactly the one the paper then performs ("0.73σ" against the WMAP+Planck central). **Required fix:** Do not present the 9σ number even as context; it is not what the experiment will measure.

**P1A-M11. The paper conflates "channel" and "operator" enumeration in §IV throughout.**
The Scope paragraph on p. 8 acknowledges that R1 and R4 "are not logically independent at the dimension-6 operator level: both are projections of the same torsion-elimination operator." If R1 and R4 are not independent operators, then "four routes" is a category-mismatch with the abstract's framing of the closure as exhausting a route space. **Required fix:** State this in the abstract, not in a footnote-style scope paragraph in §IV.

**P1A-M12. The "ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴ ≈ ρ_Λ" recovery in §IV D is not what the closure claim implies.**
Plugging α/M = 10⁻²¹ GeV⁻¹, β = β_obs, m_θ = H₀ gives ρ_θ ≈ 3.7 × 10⁻¹¹ eV⁴ (I recompute; the paper says 2.8 × 10⁻¹¹, close enough). This means Route 4 **does** match the observed dark-energy density at the spectator-ALP fit. The paper closes this not by amplitude failure but by saying m_θ ∼ H₀ "is the cosmological-constant problem in disguise." That is *the* known ALP-tuning argument and was not derived in this paper; it is not a closure of the route, it is an admission that ALPs don't solve the CC problem (which everyone knows). **Required fix:** Present Route 4 honestly as "not a closure; the ALP fit does reproduce both observables, but the required mass is fine-tuned by the standard amount." Remove from any "four-route closure" headline.

---

## MINOR findings

**P1A-Mn1.** Table I row "f_NL = −35/8 (Paper II forecast)" gives "3–5σ realistic" but the footnote then qualifies it as "class-level," "scalar-only w = 0 matter-bounce under Assumption (f)," and "not a distinctive ECH prediction." The "Yes, class-level" status flag in a summary table for a paper whose central work is ECH is misleading.

**P1A-Mn2.** §IX explicitly classifies Barriers as Novel / Known / Structural-philosophical, and yet the abstract still summarises them as a unified "13 logically-independent mechanism-class constraints." Pick one framing.

**P1A-Mn3.** The phrase "channel-level closure" appears ∼25 times. The repetition suggests anxiety about the strength of the claim; tighten.

**P1A-Mn4.** §II A 2 footnote on γ scheme dependence: the "scheme range ∼0.020" treated as an "effective range" rather than a statistical error is the right call, but Table IV (p. 21) lists it as "0.274 (scheme range ∼0.020)" with what looks like an uncertainty. Make consistent.

**P1A-Mn5.** Reference [7] cites Planck 2018 VI for ΛCDM. The arXiv ID 1807.06209 is correct. OK.

**P1A-Mn6.** Reference [22] arXiv:0808.0571 is "Annalen Phys. 520, 693 (2008)"; that number is in fact the volume of *Ann. Phys.* (Berlin). Acceptable but format inconsistent with other refs.

**P1A-Mn7.** Eq. (12): C_ℓ^EB ≈ 2β (C_ℓ^EE − C_ℓ^BB) requires β in radians and is the small-angle approximation; state this.

**P1A-Mn8.** "Tatsu Takeuchi" is correctly attributed; verify spelling of "Pop ławski" (with the stroke through l) is consistent throughout — the paper uses "Pop lawski" with what may be a rendering artifact.

**P1A-Mn9.** Acknowledgments disclose Claude (Anthropic) use for "systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation." This disclosure is appropriate but raises a question: which of the 14 barriers were "catalogued" by the model? PRD readers should know whether the literature audit underlying §IX was done by a human.

**P1A-Mn10.** "RunPod H200 and H100" hardware acknowledgment is irrelevant to PRD; remove.

**P1A-Mn11.** Multiple acronyms (NJL, EA, LQC, LQG, ECH, ALP, NY) are not all defined on first use.

**P1A-Mn12.** Table IV header "Verified Value" suggests a level of confidence not warranted, given that the MCMC values are from a companion paper not yet posted. Rename to "Adopted value (companion Paper I(b), in preparation)."

**P1A-Mn13.** §VIII (Related Work) is one paragraph and does not engage seriously with the substantial recent ECH-cosmology literature; expand to a proper related-work section or merge into §I.

**P1A-Mn14.** Fig. 1 caption begins "Bounce-mechanism → observable-prediction map" but the figure is a mostly-decorative diagram with arrows; consider whether it earns a page-1 figure slot.

**P1A-Mn15.** Fig. 2 caption acknowledges "This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action." Good. But the figure itself shows clean arrows from "Planck density" to "Observed dark energy" through "Parity-odd vacuum energy" with a "×e^(−3N) (∼10⁻¹²²)" factor that visually implies a derivation. Caveat in the figure itself.

---

## NIT findings

**P1A-N1.** "We thank the Planck, CMB-S4, LiteBIRD, LSST, and DESI collaborations" — the author is independent and is not part of these collaborations; "thank for providing the observational foundation" is overly generous phrasing for "we used public data and forecast specs."

**P1A-N2.** "houston@hubify.com" personal email; PRD prefers institutional. The author is listed as Independent Researcher so this is acceptable but unusual.

**P1A-N3.** "PACS numbers" are deprecated; PRD now uses PhySH terms.

**P1A-N4.** Repeated typography artifacts: "Pop lawski" vs "Pop ławski"; "G¨odel" → "Gödel"; "Domaga la" → "Domagała". Possibly PDF rendering only; verify in source.

---

## Audit of load-bearing numerics

I recomputed the following:

- α_em/(4π) ≈ 1/(137·4π) ≈ 5.81 × 10⁻⁴. Paper: 5 × 10⁻⁴. ✓ (factor of 1.16)
- H₀/M_Pl: H₀ ≈ 1.44 × 10⁻³³ eV, M_Pl ≈ 1.22 × 10²⁸ eV → ratio ≈ 1.2 × 10⁻⁶¹. Paper: 10⁻⁶¹. ✓
- (α/M)M_Pl with α/M = 10⁻²¹ GeV⁻¹, M_Pl = 1.22 × 10¹⁹ GeV → 1.2 × 10⁻². Paper: 10⁻². ✓
- ρ_θ from Eq. (17): m_θ² β² / [2(α/M)²] = (1.44×10⁻³³)²(5.97×10⁻³)² / [2(10⁻³⁰)²] = 3.7×10⁻¹¹ eV⁴. Paper: 2.8 × 10⁻¹¹ eV⁴ (≈ρ_Λ). Within factor 1.3 ✓. **Note: This means Route 4 DOES match ρ_Λ at the R4-fitted coupling, undermining the "amplitude no-go" framing.**
- LiteBIRD vs WMAP+Planck Gaussian quadrature: |0.342 − 0.27|/√(0.03² + 0.094²) = 0.072/0.0987 = 0.73. Paper: 0.73σ. ✓
- WMAP+Planck vs ACT DR6 consistency: |0.342 − 0.215|/√(0.094² + 0.074²) = 0.127/0.120 = 1.06σ. **Paper says "consistent within ∼1.4σ" — off by ~30%.** Flag as P1A-E10.
- exp(−3 × 92) = exp(−276) ≈ 10⁻¹²⁰. With (α/M)M_Pl ∼ 10⁻² gives Ξ ∼ 10⁻¹²² × prefactor — paper says ∼ 10⁻¹²³. Consistent at the order-of-magnitude level given prefactor uncertainty.
- f_NL ratio: |f_NL|/σ = 4.375/0.7 = 6.25 (Fisher-ideal); 4.375/1.0 = 4.4 (with systematics). Paper "3–5σ realistic" floor of 3σ requires σ ≈ 1.46, which is not the quoted σ ≈ 1.0. **The lower bound of the "3–5σ realistic" range is not earned by the quoted forecast.**

---

## Page count vs contribution

The paper is 22 pages for what is essentially one theorem (perturbation transparency, a near-trivial consequence of the first Bianchi identity), one closure exercise (three of four "routes" closed by standard arguments; the fourth not closed), and a fine-tuning bookkeeping exercise (N_tot ≈ 92 relabelling of the CC problem). The 22 pages contain extensive repetition of caveats, three scope paragraphs, a 14-barrier catalog whose components are partially redundant, and constant cross-references to companion papers that do not exist. **Recommended maximum length for the actual content: 8–10 pages.**

---

## Summary recommendation

**REJECT**

The paper rests load-bearingly on four unposted companion papers by the same author; the title and abstract overclaim a four-route closure that Section IV D explicitly contradicts; Figure 3's caption does not match the figure; multiple internal version-history annotations remain in the published text; the dimensional analysis underlying the entire dark-energy mapping is admitted to be an ad hoc on-shell ansatz; the central "perturbation transparency theorem" is a one-line consequence of the first Bianchi identity that has been implicit in the LQG/ECH literature for decades; the matter-bounce f_NL prediction and the dark-energy mechanism are admitted to be mutually exclusive yet both are presented as "surviving" results; the Route 4 calculation (which I verified) actually shows the spectator-ALP fit reproducing ρ_Λ at the observed value, contradicting the "amplitude no-go" framing; and a 22-page manuscript for this content is roughly 2–3× too long. The paper as submitted is not at the level PRD requires. A substantially shortened, dimensionally-controlled, and self-contained successor that (a) posts the companion papers as preconditions, (b) honestly characterises the closure as a closure of three amplitude routes plus a naturalness argument against a fourth, (c) demotes the Bianchi-vanishing observation to a remark, and (d) drops the f_NL/birefringence "surviving predictions" framing in favour of an explicit statement that the framework cannot simultaneously provide both, could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh-Eyes Pass

## Additional ESSENTIAL findings

**P1A-E11. Figure 1 contains stale numerical content explicitly retracted in body text.**
Fig. 1 displays "PTA γ = 3.0 / v.s. data 3.20 ± 0.42 (P3 §6)." However, §X G (p. 16) explicitly states: *"NANOGrav model comparison: γ = 2.567 ± 0.382 from real-KDE reanalysis... This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts."* Table IV confirms the new value. **Fig. 1 was not updated when the PTA reanalysis migrated to real-KDE.** The figure now displays the value the paper has explicitly retracted. **Required fix:** Redraw Fig. 1 with γ_data = 2.567 ± 0.382.

**P1A-E12. Figure 4 actual contents do not match caption.**
Caption claims: *"Top: matter-bounce f_NL = −35/8 in the SPHEREx multi-tracer f_NL Fisher landscape... Bottom: spectator-ALP cosmic birefringence in the LiteBIRD σ(β) ≈ 0.03° window."* But the actual single-panel figure shows a "Detection Significance Forecast" with three lines labeled "CMB E-B," "Galaxy Spins," and "Combined (g=0)" plotted vs. year 2024–2034. **None of "matter-bounce f_NL," "SPHEREx Fisher landscape," "spectator-ALP," or "LiteBIRD window" appears in the plotted figure.** This is a hard mismatch on the load-bearing detection-forecast figure. Additionally: "Galaxy Spins" is plotted approaching ~3σ by 2030, which contradicts the body's repeated statement that the framework underpredicts spin asymmetry by >100 OOM. **Required fix:** Replace the figure with what the caption describes, or replace the caption with what the figure shows.

**P1A-E13. §IV "Three technical aspects" paragraph (p. 8) presents two dimensionally-inequivalent expressions as "equivalent rewritings."**
The text reads: *"the dimensional reconstruction of ρ_Λ^bounce in Appendix B requires an internally consistent mass-dimension accounting between (α/M) M_Pl³ (dimension +2) and the equivalent rewriting [(α/M) M_Pl] M_Pl⁴ (dimension +4); the choice of M_Pl⁵ vs. M_Pl³ controls the subsequent N_tot ≈ 92 bookkeeping."* The two expressions explicitly have mass dimensions +2 and +4 respectively. **They cannot be "equivalent rewritings" of the same quantity** — they differ by mass². The phrase "the choice of M_Pl⁵ vs. M_Pl³" admits the framework requires choosing between two non-equivalent normalizations, but does not commit to one. The entire load-bearing N_tot ≈ 92 bookkeeping is therefore ambiguous by 2 powers of M_Pl, i.e. by ~40 orders of magnitude. **Required fix:** Commit to one dimensional assignment; do not call differently-dimensioned expressions "equivalent."

---

## Additional MAJOR findings

**P1A-M13. §II C 1 contains confused dimensional analysis: "cube of the fermion bilinear scales as the cube of the fermion number density."**
The fermion spin density S^abc = (1/4) ψ̄γ^[a γ^b γ^c]ψ is **bilinear** in ψ (two ψ's, three gamma matrices), not cubic. Three antisymmetric gammas in 4D dualize to a single gamma γ^5, so the spin density is essentially the axial current ψ̄γ_d γ^5 ψ — a bilinear. There is no "cubic fermion bilinear" or "cube of the bilinear" structure anywhere in minimal ECH. The torsion ∝ bilinear scales as n_ψ ∝ a^(-3); the four-fermion contact term (T·T) is then **quartic** and scales as a^(-6); upon volume integration over a^3, the action contribution scales as a^(-3). The conclusion (exp[-3N_tot]) is plausible but the derivation as written misidentifies the operator power-counting. **Required fix:** Rewrite the dimensional argument correctly; do not invoke a "cubic" structure that does not exist in ECH.

**P1A-M14. Cross-reference §IV D → §II A 2 for α/M ∼ 10⁻²¹ GeV⁻¹ is wrong.**
§IV D states: *"bounds α/M at ∼ 10⁻²¹ GeV⁻¹, identical to the value already quoted in Sec. II A 2."* But §II A 2 contains no specific numerical value for α/M; it says only *"We treat α/M as a phenomenological parameter constrained by data."* The value 10⁻²¹ GeV⁻¹ first appears in §II C 2. **Required fix:** Correct the cross-reference.

**P1A-M15. §II B claims the LQC bounce has "no free parameters" but ρ_crit depends on γ scheme-dependently.**
*"The factor (1 − ρ/ρ_crit) ensures H² → 0 as ρ → ρ_crit, producing a smooth bounce with no free parameters."* But the immediately preceding sentences establish that ρ_crit ranges from 0.27 to 0.41 ρ_Pl depending on γ-counting scheme — a factor-of-1.5 spread that the paper itself flags as scheme-dependent. **Required fix:** Replace "no free parameters" with "with γ fixed by the LQG scheme choice."

**P1A-M16. §IX taxonomy of "Novel" barriers (9 entries) contradicts abstract's "13 logically-independent" framing.**
§IX explicitly partitions the 14 barriers as: *Novel results (Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14)* — that is **9 barriers**; *Known results (Barriers 5, 6, 7, 9)* — 4 barriers; *Structural/philosophical observations (Barrier 13)* — 1 barrier. Subtracting the historical B8↔B14 redundancy leaves 8 novel results. The abstract's "13 logically-independent mechanism-class constraints" therefore lumps 4 "known results" and 1 "philosophical observation" into the headline count without flagging their classification. **Required fix:** Quote the actual count of novel constraints in the abstract; do not present known results as part of the closure case.

**P1A-M17. §III A explicitly admits the central CMB observational signature has no ECH derivation, yet the abstract features β ≈ 0.27° prominently.**
§III A states: *"Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here. The parity-odd structure is qualitatively consistent with the observed isotropic birefringence..."* The β ≈ 0.27° "prediction" is in fact a GR+ALP calculation with no ECH input (the abstract correctly hedges this as "not an ECH prediction" but only after billing it). **Required fix:** Move the β = 0.27° benchmark off the abstract's headline list of surviving predictions, or state in the same sentence that no photon-torsion coupling has been derived.

**P1A-M18. §XI (Hybrid Dark-Energy Loophole) contradicts Table III footnote.**
§XI states: *"The loophole was explored theoretically but the w₀w_a extension was never implemented computationally in this program (the MCMC program uses stock CAMB with ΔN_eff only)."* But Table III footnote ‡ explicitly describes a w₀w_a-extended Cobaya chain currently running (16 chains, ~3.8 × 10⁴ accepted samples, R̂−1 ≈ 3×10⁻²). One of these two statements is wrong. **Required fix:** Reconcile.

**P1A-M19. Table I row "H₀/σ₈ tension resolution? ... Recovers ΛCDM" is misleading as a "tension resolution" entry.**
The row poses the question "H₀/σ₈ tension resolution?" and answers "Recovers ΛCDM" with status checkmark unstated. Recovering ΛCDM is, by definition, **not** a resolution of the H₀ tension (which is between Planck-like ΛCDM and SH0ES). **Required fix:** Either change the row to ask "Modifies H₀ from ΛCDM?" and answer "No," or remove the row.

---

## Additional MINOR findings

**P1A-Mn16.** Cross-reference in §II C 1 (p. 7) cites "the Cartan algebraic equation T^abc ∝ ψ̄γ^[a γ^b γ^c] ψ (Sec. IV A, Eq. 13)." But Eq. 13 is the Hehl-Datta NJL contact Lagrangian, not the Cartan equation. The Cartan equation is **Eq. 3** (in §II A 2). Fix the reference.

**P1A-Mn17.** §IV D ρ_θ recompute: with m_θ = 1.5×10⁻³³ eV, β = 6×10⁻³ rad, α/M = 10⁻³⁰ eV⁻¹, ρ_θ = m²β²/[2(α/M)²] = 4.05×10⁻¹¹ eV⁴, not 2.8×10⁻¹¹ as quoted. The quoted value coincides with (2.3 meV)⁴ = ρ_Λ exactly, suggesting the author wrote the desired endpoint rather than the calculation result. Difference is a factor 1.4, within OOM but worth noting.

**P1A-Mn18.** §IV B footnote calls the 5×10⁻⁴ vs 5.8×10⁻⁴ rounding of α_em/(4π) "this ∼2× factor." The actual ratio is 1.16, i.e. 16% — nowhere near 2×.

**P1A-Mn19.** §IV D "consistent within ∼1.4σ" between WMAP+Planck β = 0.342°±0.094° and ACT DR6 β = 0.215°±0.074° is arithmetically wrong. |0.342−0.215|/√(0.094²+0.074²) = 0.127/0.120 = **1.06σ**, not 1.4σ. (Already in P1A-E10 as a general issue; flagging the specific arithmetic here.)

**P1A-Mn20.** Appendix B contains the typo "10¹⁹ GeV×4" meaning (10¹⁹ GeV)⁴. Reformat.

**P1A-Mn21.** Appendix B claim "the genuine cosmological-constant hierarchy is ... ∼ 10¹²²" recomputes (with full Planck mass 1.22×10¹⁹ GeV) to ρ_Pl/ρ_Λ ≈ 10¹²³ — a factor-of-few off, within OOM but inconsistent with the precise number stated.

**P1A-Mn22.** "PTA" appears in Fig. 1 caption without definition. First textual occurrence with definition is much later. Define on first use.

**P1A-Mn23.** "EA" (effective action) used in abstract enumeration "(NJL, one-loop EA, Immirzi running, parity-CMB)" without definition.

**P1A-Mn24.** §II A 2 says γ_SU(2) ≈ 0.274 "where the apparent uncertainty range is scheme dependence rather than a statistical or theoretical error." Table IV row formats this as "0.274 (scheme range ∼0.020)." A reader scanning the table will read "0.020" as an uncertainty in the standard tabular sense. Reformat (e.g., "0.274 [scheme; SU(2) full counting; cf. 0.127 U(1), 0.2375 DLM]").

**P1A-Mn25.** Footnote 1 (p. 11) defines two distinct f_NL forecast regimes (bispectrum-only σ ≈ 0.7 vs. post-systematic σ ≈ 1.0) yielding ~6σ and ~4σ respectively, then conflates them as "3–5σ realistic." Quote one regime in the abstract; do not migrate between regimes between abstract and footnote.

**P1A-Mn26.** §X B Step 2 writes torsion as "T^λ_μν = 8πG S^λ_μν + ..." with an unexplained "+..." In minimal ECH the Cartan algebraic equation is exact (no additional terms); the ellipsis suggests something has been omitted. Either drop the "+..." or specify what is being suppressed.

**P1A-Mn27.** Eq. (23) writes the "Holst dual contraction" as ε^μνρσ R_μνρσ with spacetime indices. The Holst term in Eq. (1) is ε^abcd e^μ_a e^ν_b R_{cd μν} with Lorentz-internal ε contracted via tetrads. The two are related on T=0 but not literally the same object. The proof goes through, but the notation in §X conflates Lorentz and spacetime ε's. Worth tightening.

---

## NIT findings

**P1A-N2.** "Pop ławski" appears throughout with what looks like a rendering issue (broken Polish ł character). Verify the Unicode handles correctly in final typesetting.

**P1A-N3.** Repeated phrases "channel-level closure," "under stated assumptions," "phenomenological ansatz" appear so frequently they signal defensive hedging rather than confidence. Consolidate.

**P1A-N4.** The 22-page paper repeatedly references its own §X (perturbation transparency) as if it were a major theorem. As noted in P1A-M2, the result is a textbook consequence; the volume of self-reference inflates the apparent contribution.

**P1A-N5.** Acknowledgments thank "Lior Shamir for providing aggregate CW/CCW galaxy spin counts" — but §III B and §V cite his work as the one being refuted. Decide whether this is acknowledgment of data sharing or implicit endorsement of his prior null-refuted analysis.

---

**Summary of fresh-eyes pass:** The additional findings principally concern (i) Fig. 1 / Fig. 4 caption-vs-content mismatches that I missed by not looking carefully at the actual plotted axes (P1A-E11, E12); (ii) an explicit dimensional inconsistency in §IV's "Three technical aspects" paragraph that I had only flagged at the Appendix-B level (P1A-E13, M-13); (iii) cross-reference errors (P1A-M14, Mn16); (iv) several arithmetic mistakes including the 1.4σ vs 1.06σ recomputation and the "∼2× factor" mislabeling; and (v) the §XI-vs-Table III internal contradiction about whether w₀w_a was computationally implemented (P1A-M18). These bring the total to 13 ESSENTIAL findings, 19 MAJOR findings, 27 MINOR findings, and 5 NIT findings.