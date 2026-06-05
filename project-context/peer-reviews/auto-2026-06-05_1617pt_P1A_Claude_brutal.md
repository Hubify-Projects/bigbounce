# P1A auto-2026-06-05_1617pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11994 chars)
**Wall time**: 371.2s

---

# Referee Report: P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Overall Assessment

This paper is a structural/no-go analysis of Einstein-Cartan-Holst (ECH) gravity as a dark-energy source. After careful reading, I find that the paper has fundamental problems that go well beyond presentation: the central novel "result" (perturbation-transparency theorem) is a trivial restatement of a textbook fact, the "14-barrier closure" is a rhetorical device rather than a theorem, the dimensional analysis in Appendix B explicitly admits the central scaling is an ansatz rather than a derivation, and the paper relies extensively on companion papers that are "in preparation" for load-bearing numerical claims. The writing is severely bloated with self-referential hedging, repeated caveats, and meta-commentary about what the paper does and does not claim. The abstract is ~2 pages long and contains in-text parenthetical caveats that read like response-to-referee insertions.

I recommend **REJECT**.

---

## ESSENTIAL Findings

### P1A-E1: The "perturbation-transparency theorem" is trivial and not novel
**Section X, pages 14**. The "theorem" states: canonical scalar field → zero spin density → zero torsion → Levi-Civita connection → Holst term becomes Pontryagin density (total derivative) → no EOM contribution. This is elementary textbook Einstein-Cartan: that torsion vanishes when spin density vanishes is Hehl et al. (1976), explicitly cited as ref. [12]. That the Holst term on a torsion-free connection reduces to a topological density is standard (Holst 1996, Mercuri 2009). The paper itself acknowledges this generalizes Hehl et al. (1976). Yet the abstract calls it "the central result" and a "perturbation-transparency theorem." A 5-line corollary of a 50-year-old result is not a theorem worth being the headline of a PRD paper.
**Fix**: Either identify a genuinely new theoretical claim or downgrade to "we note for completeness" and remove the theorem framing throughout.

### P1A-E2: Abstract is ~2 pages of self-undermining caveats
**Abstract, page 1**. The abstract spans the entire first page and contains in-line meta-commentary like "This is a channel-level assessment, not an operator-level theorem," "we acknowledge missing operators (Jackiw-Pi gravitational Chern-Simons R∧R̃...) explicitly in Sec. IV and Sec. XI," "we treat this scaling explicitly as an ansatz, not a derivation," "The two predictions discussed below as 'surviving' are accordingly not predictions of ECH itself." An abstract that systematically explains what the paper does not prove is not a PRD abstract.
**Fix**: Rewrite to ≤ 250 words stating concretely what is proven, without recursive caveat structure.

### P1A-E3: Central dimensional analysis admits to being an ansatz
**Appendix B, page 19; Sec. II A 2, Sec. II C, page 6**. The paper states "The parity-odd operator (Eq. 6) has off-shell mass dimension +1, not the +4 required for a local Lagrangian density," and "ρΛ = Ξ M⁴_Pl is therefore a scaling ansatz, not a controlled EFT calculation." Appendix B further admits "the missing powers of mass do not arise from off-shell EFT counting but from on-shell scaling assumptions applied to a Planck-scale bounce geometry." This means the central dark-energy mapping that the paper purports to "close" is itself ill-defined from the start. One cannot give a no-go theorem against an ansatz that has no controlled EFT meaning; one is merely closing one's own phenomenology against itself.
**Fix**: Either provide the controlled EFT operator (with explicit M_Pl factors in the coupling) or withdraw the central dark-energy framing entirely.

### P1A-E4: B8 is admitted to be subsumed by B14; "14 barriers" is rhetoric not theorem
**Sec. IX, page 12; Table II caption, page 13; abstract**. The paper repeatedly says "14 historical catalog entries, of which B8 is subsumed by B14." Then why is the headline number 14 and not 13? The structure smells of inflation. The classification "Novel/Known/Structural-philosophical" in Sec. IX implicitly concedes that Barriers 5, 6, 7, 9, 13 are not original results, and Barriers 8 and 14 are redundant. The remaining "novel" barriers (1, 2, 3, 4, 10, 11, 12) are largely Planck suppression arguments that are individually trivial. Moreover, the structural-philosophical Barrier 13 ("Gravitational Democracy") is a one-paragraph observation, not a constraint.
**Fix**: Either rigorously prove independence of all barriers or relabel honestly (e.g., "we collect known no-go arguments and add three new ones").

### P1A-E5: Load-bearing numerical claims rest on "in preparation" companion papers
**Throughout**. Critical numerical inputs — H₀ = 67.68 ± 1.06, ΔN_eff ≈ 0, the 309,189 frozen MCMC samples, the SPHEREx σ(f_NL) ≈ 0.7 forecast, NANOGrav γ = 2.567 ± 0.382, the galaxy spin null — are sourced to refs [2], [6], [23], [46], all marked "in preparation". The paper says explicitly "they are documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted." This is not acceptable for a PRD submission. A paper cannot rely on unpublished companion papers for its empirical anchors.
**Fix**: Either submit the companion papers first or drop all numerical claims that depend on them.

### P1A-E6: Internal audit/version language in body
**Sec. X G, page 15**: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."
**Appendix B, page 19**: "not the ∼35 misstated in earlier drafts."
**Sec. IV, page 8**: "the qualitative closure statement that Route 2 lies below the observed birefringence amplitude by ≳30 orders of magnitude survives any reasonable dimensional reconciliation" (response-to-referee tone).
**Sec. II A 2, page 5**: "the ∼0.020 figure that appears in the parameter-budget table (Appendix B) is the spread between counting prescriptions, retained as an effective range only and not propagated as a statistical error in any quantitative claim."
These are review-log artifacts that do not belong in published text.
**Fix**: Remove all version-history language; rewrite as if the paper has no prior drafts.

### P1A-E7: Figure 1 (mechanism→prediction map) is internally inconsistent with the text
**Page 4, Fig. 1**. The figure shows arrows from ECH/torsion (red, "structurally closed this paper") to f_NL = -35/8, w₀w_a DE, etc. But the caption says ECH is "structurally closed" — so what is the arrow doing? Also "Matter bounce" is shown producing both f_NL = -35/8 and PTA γ = 3.0, but the text (Sec. X G) says the PTA value 2.567 ± 0.382 puts matter-bounce γ=3.0 at +1.13σ, which the paper itself characterizes as "consistent" — not a positive prediction confirmation. The figure misleadingly presents this as a successful matter-bounce signature.
**Fix**: Redraw or remove. The figure has filler character.

### P1A-E8: Route 4 closure changes definition mid-section
**Sec. IV D, page 10**. The section title says "naturalness objection rather than amplitude no-go." Then the text says: "R4 is therefore not closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H₀ to also produce ρ_Λ, and this tuning is the original CC fine-tuning relabelled." Later: "R4 therefore relocates the cosmological-constant problem rather than solving it." But this is the well-known fact that an ALP can fit the birefringence — no actual closure occurs. The paper then admits: "R4 is therefore not closed by amplitude mismatch... it is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level." An "explanatory deficit" is not a no-go. This invalidates the "four-route closure" framing of the abstract.
**Fix**: Rewrite the abstract to reflect that R4 is not closed.

### P1A-E9: Eq. (15) dimensional analysis is opaque and the result varies by 25 orders of magnitude with "ordering"
**Sec. IV B, page 9**. The paper writes "the dimensionless ratio is Δθ_one-loop/Δθ_obs ∼ 10⁻³· 10⁻⁶¹/(10⁻²· 6 × 10⁻³) ∼ 10⁻⁵⁸ to 10⁻⁶⁰" and then notes "We adopt this contraction as the canonical Route-2 estimate; an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼10⁻³³ ratio." A 25–27 order-of-magnitude ambiguity in the closure of an amplitude-budget no-go is fatal to the no-go itself. The paper papers over this by saying the qualitative conclusion survives, but the entire premise of "amplitude-budget granularity" requires the numbers to be well-defined.
**Fix**: Derive Eq. (15) properly from a Lagrangian; do not leave a 10²⁵ factor to choice of "ordering."

### P1A-E10: Eq. (11) "derivation" is order-of-magnitude dimensional aesthetic
**Sec. II C 1, pages 6–7**. The text explicitly admits "a fully rigorous first-principles derivation of the half-integer power requires the parity-odd density-of-states phase-space integral, which is dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function." The (T_reh/M_GUT)^(3/2) factor is then admitted to be "treated as a phenomenological phase-space ansatz." This is the equation that sets N_tot ≈ 92, which drives the entire structural-tension argument in Sec. XIV D. A "structural tension" derived from a dimensional-aesthetic-level equation is not a structural tension.
**Fix**: Either derive Eq. (11) properly or remove the N_tot ≈ 92 number and all structural arguments depending on it.

### P1A-E11: Routes R1–R4 are admitted to not be independent operators
**Sec. IV, page 8**. The paper says "R1 (NJL parity-even four-fermion) and R4 (parity-odd ALP/axial-current CMB coupling) are not logically independent at the dimension-6 operator level: both are projections of the same torsion-elimination operator." And: "additional operators in the parity-odd sector (the Jackiw-Pi gravitational Chern-Simons term R ∧ R̃ and the parity-odd four-fermion partner of R1 carrying the γ_BI/(γ²_BI+1) · 8πG coefficient) are not separately enumerated." So the "four-route closure" is neither complete nor independent. This deflates the central enumeration.
**Fix**: Either prove operator-level completeness or drop "four-route closure" framing.

---

## MAJOR Findings

### P1A-M1: Duplicate/repetitive phrasing throughout
The abstract repeats the same SPHEREx-scale-pushing argument verbatim in Sec. I A 2 and Sec. XIV D and Sec. XIII, sometimes with near-identical wording. The phrase "comoving wavenumbers k are constant by definition and only physical scales scale with a⁻¹ ∝ e⁻ᴺ" appears at least three times. The phrase "channel-level closure under stated assumptions" appears in the abstract, Fig. 1 caption, Sec. I, Sec. IV, Sec. IX, Sec. XIV E, and conclusions.
**Fix**: Cut by 50%.

### P1A-M2: Table I content does not match claims
**Page 4, Table I**. Row "Testable prediction?" shows f_NL = -35/8 with status "Yes, class-level". Footnote c admits "not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction." Then the same paper repeatedly states this is the "surviving prediction." If it's not a distinctive ECH prediction, then strictly nothing distinctive survives, and the row is misleading.
**Fix**: Be honest: "No distinctive ECH-specific testable prediction."

### P1A-M3: Sec. XV conclusion contradicts Sec. XIII
**Sec. XV, page 18**: "LiteBIRD (σ(β) ≈ 0.03°, early 2030s) detects non-zero β at ∼9σ (a 0.27°/0.03° overall sensitivity number)." The same sentence then explains this is "NOT" the model-discrimination significance, which is 0.73σ. Presenting a "9σ" headline number immediately followed by a "NOT" disclaimer is a textbook overclaim pattern.
**Fix**: Lead with the 0.73σ number; do not present 9σ as the headline.

### P1A-M4: The "structural tension" (Sec. XIV D) is self-imposed
The "tension" is between the paper's own ansatz N_tot ≈ 92 (which it admits is dimensional-aesthetic) and a matter-bounce prediction it admits is not ECH-specific. So this is not a tension within ECH; it is a tension between two independent ansätze the paper itself introduced. This is internal narrative inflation.
**Fix**: Remove or restate as observational complementarity.

### P1A-M5: Ref. [44] arXiv ID is suspicious
**Ref. [44], page 21**: "Y.-F. Cai and J.-H. Zhu, ... (2026), arXiv:2603.13924." There is no arXiv:2603.13924 — arXiv IDs start with YYMM, so 2603 would be March 2026. The paper is dated June 2026, so an arXiv ID 2603.13924 is technically possible but the format/checkdigit needs verification, and posting future-dated arXiv IDs is suspicious.
**Fix**: Verify arXiv ID; if speculative or future, remove.

### P1A-M6: NANOGrav comparison in Sec. X G is buried and uses unverified companion result
The "γ = 2.567 ± 0.382 from real-KDE re-analysis" with a +1.13σ result is sourced to companion Paper III [46] "in preparation," then used to declare matter-bounce "consistent with the data." This is exactly the kind of unsupported claim flagged in P1A-E5.

### P1A-M7: "Foundation Studies A-G" and "Branches H, J, L, M, N, O" are not in the paper
The paper repeatedly references "7 foundation studies (Foundations A-G)" and "6 observational research branches (Branches H, J, L, M, N, O)" but these are not actually presented as studies in the paper — they are just labels attached to barriers in Sec. IX. There is no Foundation Study A, B, C, etc. with content. This is administrative scaffolding masquerading as research output.
**Fix**: Drop the Foundation/Branch terminology or actually present the studies.

### P1A-M8: Eq. (15) gives "10⁻⁵⁸ to 10⁻⁶⁰" range and "factor-of-∼100" is called ε-correction
**Sec. IV B, page 9**: "the factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone." A factor of 100 in a "channel-level closure" calculation is not an ε-correction; it is a control-of-factors problem. The author then admits a 10²⁵ ambiguity exists from "ordering." This is unacceptable.

### P1A-M9: γ_SU(2) value 0.274 with "scheme range ~0.020" used as if known
**Sec. II A 1, page 5; Table IV, page 20**. The paper uses γ = 0.274 (SU(2) full counting) for ρ_crit computation but then says the DLM refinement gives γ_DLM ≈ 0.2375 and the U(1) counting gives 0.127. The "scheme range" is therefore ~ a factor of 2, not 0.020. Table IV showing "0.274 (scheme range ∼0.020)" is misleading; the genuine scheme range is much larger.
**Fix**: Either commit to a counting scheme with justification or honestly state the factor-of-2 spread.

### P1A-M10: Table III footnotes contradict the table
**Page 16, Table III**. The "w₀w_a DESI" column has entries "not tested‡" with footnote explaining that the MCMC chain has not yet converged ("R̂ − 1 ≈ 3×10⁻², descending monotonically toward the standard publication-quality convergence target R̂ − 1 < 10⁻²"). A PRD paper cannot rely on a still-running chain.
**Fix**: Remove the column or remove the table.

### P1A-M11: Acknowledgment of LLM use is appropriately disclosed, but the text contains many LLM-style hedges
The acknowledgments correctly disclose use of Claude. However, the document is suffused with characteristic LLM-style padding: nested parenthetical caveats ("not directly comparable... not directly comparable... not directly comparable"), recursive meta-commentary on what the paper does and does not claim, and structurally identical hedge constructions. This is a writing-quality issue: the paper reads more like a model-mediated draft than peer-reviewed prose.
**Fix**: Heavy editorial pass to remove redundancy and meta-commentary.

### P1A-M12: Page count vs. content
The paper is 21 pages including references, with most novel theoretical content occupying maybe 4 pages (Sec. IV: the four-route closure; Sec. X: the perturbation-transparency observation; Appendix B: dimensional analysis). The remaining ~13 pages are barriers (mostly trivial), repeated statements of "structural tension," and surveys of companion papers. For a PRD methods paper, this should be ≤ 12 pages.
**Fix**: Recommended maximum 10–12 pages.

---

## MINOR Findings

### P1A-Mn1: Eq. (4) coefficient
**Sec. II A 2, page 5**. The Lagrangian coefficient -3πG_N/2 × γ²/(γ²+1) is quoted. The standard result for the four-fermion coupling from Holst+fermions is -3πG_N × γ²/(γ²+1) (Freidel et al. 2005). The factor of 1/2 deserves verification.

### P1A-Mn2: Eq. (8) form
H² = (8πG/3)ρ(1 - ρ/ρ_crit) is correct for LQC, but no source for "Pop ławski" approach (which the paper cites as the bounce mechanism). The relevant ECH bounce equation includes a 4-fermion term, not the LQC ρ²/ρ_crit form. There is a conflation of LQC and ECH bounce mechanisms.

### P1A-Mn3: Footnote 1 (page 11) calculation
"raw ratio |f_NL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84." 6.25 × 0.84 = 5.25, OK. But then "with systematics σ(f_NL) ≈ 1.0" gives 4.375/1.0 = 4.375σ, which is in the lower end of the claimed "3–5σ." Inconsistent with "3–5σ realistic" framing.

### P1A-Mn4: Table IV missing units
The table shows "0.27° (midpoint)" for β — but a "midpoint" of what? The observation is 0.342° ± 0.094°; the spectator-ALP fit is 0.27°. These are different things; calling 0.27° a "midpoint" is misleading.

### P1A-Mn5: ACT DR6 follow-up reports β = 0.215° ± 0.074°, which is 2.9σ from zero
The paper correctly notes this, but then says it is "comparable" to WMAP+Planck 0.342° ± 0.094° "consistent within ~1.4σ". |0.342 - 0.215| / √(0.094² + 0.074²) = 0.127 / 0.120 = 1.06σ, not 1.4σ. Recompute.

### P1A-Mn6: "the Cuscuton bounce (fNL ≈ 0)" 
Ref [37] (Dehghani et al. 2025) is cited for this. The Cuscuton bispectrum is non-zero in general; calling it "≈ 0" without qualification is loose.

### P1A-Mn7: Inconsistent use of "the 14-barrier closure" vs. "13 logically-independent"
The paper switches between "14 barriers" and "13 logically-independent (14 historical entries with B8 subsumed)" in different sections. Pick one.

### P1A-Mn8: Acknowledgments list of physicists includes Pop ławski, Mercuri, Freidel, Minic, Takeuchi — all cited. But the paper does not request acknowledgment from anyone who actually read it or commented on it.

### P1A-Mn9: "Spectator-ALP birefringence β ≈ 0.27°" but observation is 0.342° ± 0.094°. The "consistency" claim requires explanation: where does 0.27° come from if not fit to 0.342°?

### P1A-Mn10: "DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)" — refs [9, 10]. The DESI DR2 (ref [10]) reports 2.8–4.2σ; the 3.1σ lower bound deserves a more precise citation.

---

## NITs

### P1A-N1: PACS codes 98.80.-k, 04.50.Kd, 04.60.Pp, 95.36.+x — PACS has been deprecated by APS since 2016; PRD now uses keywords/PhySH.

### P1A-N2: "houston@hubify.com" — institutional email recommended for PRD submission.

### P1A-N3: Independent Researcher affiliation with self-funded computational resources (page 19) is OK but reduces external scrutiny credibility.

### P1A-N4: GitHub link uses "bigbounce" as the repo name; informal for PRD reference.

### P1A-N5: "(Dated: June 2, 2026 PDT)" — future date for a paper to be reviewed. Timezone in a date stamp is unusual.

### P1A-N6: Many equations have ad-hoc labels; some unlabeled equations are referenced as if labeled (e.g., "Eq. (B2)").

### P1A-N7: Inline LaTeX rendering issues: "Pop ławski" appears with broken diacritic.

---

## Summary recommendation

**REJECT**

This paper is a no-go theorem about an ansatz the paper itself admits is not a controlled EFT calculation; its central "perturbation-transparency theorem" is a textbook corollary of Hehl et al. (1976); its "14-barrier closure" is admitted to have only ~7 novel barriers, with one of those (R4) closed by an "explanatory deficit" rather than a no-go; its key amplitude calculation (Eq. 15) varies by 25 orders of magnitude depending on "ordering" of factors; its load-bearing numerical anchors (H₀, ΔN_eff, SPHEREx forecast, NANOGrav, galaxy spin null) all come from companion papers marked "in preparation"; its abstract is 2 pages of self-undermining caveats; and its writing is suffused with version-history artifacts, repeated paragraphs, and LLM-style hedging. The Appendix B admission that ρ_Λ = Ξ M⁴_Pl "is therefore a scaling ansatz, not a controlled EFT calculation" essentially invalidates the central framing — one cannot close routes for a phenomenology one cannot derive. The paper would need to be cut to ≤ 12 pages, have its central theoretical claim genuinely strengthened or accurately downgraded, have all "in preparation" companion-paper dependencies removed or replaced with already-public results, and undergo a heavy editorial pass to remove caveat-stacking and repetition before it could be considered for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Review: Additional Findings

After re-examination focusing on arithmetic, figure-body consistency, internal cross-references, and abstract faithfulness, I found several additional issues not in the initial review.

---

## NEW ESSENTIAL Findings

### P1A-E12: Figure 2 contradicts main text by ~48 orders of magnitude
**Fig. 2, page 5**. The energy-density hierarchy figure shows:
- ρ_vac ≈ 10⁻² M_Pl⁴ at the parity-odd vacuum level
- "× e⁻³ᴺ (~10⁻⁷²)" dilution
- "After inflationary dilution (N = **55** e-folds)" → Λ_obs

But the main text (Sec. II C 1) states: "Matching ρ_Λ ≈ (2.3 meV)⁴ requires **N_tot ≈ 92**." Checking: ρ_Λ/M_Pl⁴ ≈ 2.8 × 10⁻⁴⁷ GeV⁴ / 10⁷⁶ GeV⁴ ≈ 10⁻¹²³, so 10⁻² × D_inf = 10⁻¹²³ requires D_inf ≈ 10⁻¹²¹, i.e., 3N = 121 × ln 10 ≈ 279, N ≈ 93. The figure's N = 55 yields D_inf ≈ e⁻¹⁶⁵ ≈ 10⁻⁷², leaving the result at 10⁻⁷⁴ M_Pl⁴ — **48 orders of magnitude above ρ_Λ**. The figure that illustrates the dark-energy mapping does not actually reach ρ_Λ.
**Fix**: Replace N = 55 with N ≈ 92 in Fig. 2, or remove the arrow pointing to Λ_obs.

### P1A-E13: Sec. IV E cross-references the wrong section for the condensate route
**Sec. IV E, page 11**: "The condensate mechanism yields a vacuum energy that is parametrically too large by many orders of magnitude and is not a viable DE source; **its role is therefore documented in Sec. X** as a quantitative closure rather than a viable channel."

But Sec. X is "The Perturbation-Transparency Result" — there is no discussion of the condensate route there. The condensate route is actually discussed in **Sec. XII B**: "The condensate route fails because the scalar/pseudoscalar channel is repulsive at γ = 0.274 and subcritical." The cross-reference is to the wrong section and gives a false sense of cross-validation.
**Fix**: Change "Sec. X" to "Sec. XII B" or provide actual condensate analysis where claimed.

---

## NEW MAJOR Findings

### P1A-M13: "6 branches" in abstract conflicts with "6 branches plus ECH perturbation gates" in body
**Abstract; Sec. IX, page 12**. Abstract says: "6 observational research branches (Branches H, J, L, M, N, O)." Sec. IX says: "**6 additional observational channels (Branches H, J, L, M, N, O, plus ECH perturbation gates**) for the possibility of connecting the ECH bounce to late-time dark energy." So there are effectively 7 branches, with the 7th (perturbation gates) hosting B14 — exactly the barrier the paper calls "the central result." The abstract omits this 7th branch even though it contains the headline theorem.
**Fix**: Reconcile abstract and body.

### P1A-M14: γ "scheme range ~0.020" in Table IV does not match any pair of standard counting prescriptions
**Table IV, page 20; Sec. II A 1, page 5**. Table IV quotes "0.274 (scheme range ~0.020)" but the prescription differences are:
- SU(2) full counting (0.274) vs DLM (0.2375): Δ = 0.0365
- SU(2) full counting (0.274) vs U(1) (0.127): Δ = 0.147
The "~0.020" matches neither. If it's meant to encode "spread between counting prescriptions" (as Sec. II A 1 claims), the genuine spread is ≥ 0.037 within SU(2)/DLM alone and ~0.15 across all three. The "0.020" appears to be a stale or invented number.
**Fix**: Quote the actual prescription differences (0.127, 0.2375, 0.274) explicitly; remove "~0.020".

### P1A-M15: Eq. (15) result "10⁻⁵⁸ to 10⁻⁶⁰" — only the lower end is reproducible from quoted inputs
**Sec. IV B, page 9**. Recomputing with the paper's quoted values: 10⁻³ · 10⁻⁶¹/(10⁻² · 6×10⁻³) = 10⁻⁶⁴/(6×10⁻⁵) = **1.67 × 10⁻⁶⁰**. This is the lower (10⁻⁶⁰) end. The upper end (10⁻⁵⁸) requires a factor of 100 that the paper attributes opaquely to "ε-correction perturbative-order scaling alone." A factor of 100 is not an ε correction; it's two full perturbative orders, which would require an explicit higher-order calculation. The range "10⁻⁵⁸ to 10⁻⁶⁰" is therefore not derived from the displayed numbers.
**Fix**: Show the actual two-loop derivation or remove the upper bound.

### P1A-M16: Δγ/γ ~ 10⁻² in Route 3 is asserted without justification
**Sec. IV C, page 10**. The text states: "In the Standard Model, the chiral asymmetry is generated by the SU(2)_L doublets; numerically, **Δγ/γ ~ 10⁻²** over the running from the GUT scale to the IR." This number drives the Route-3 closure suppression of 10⁻⁶³. But Date-Kaul-Sengupta [26] is not cited as the source of this 10⁻² number, and Benedetti-Speziale [27] (cited for the sign-dependent β-function) is also not quoted as yielding 10⁻². The number is asserted with no derivation and no citation.
**Fix**: Derive or cite the 10⁻² estimate.

### P1A-M17: "Smooth bounce with no free parameters" contradicts γ scheme-dependence
**Sec. II B, page 6**. After Eq. (9): "The factor (1 − ρ/ρ_crit) ensures H² → 0 as ρ → ρ_crit, producing **a smooth bounce with no free parameters**." But the same paragraph admits ρ_crit depends on the LQG counting scheme via γ, yielding the range ρ_crit/ρ_Pl ∈ [0.27, 0.41] — a factor of 1.5 from this "free parameter." The "no free parameters" claim is in direct contradiction with the prior sentence.
**Fix**: Replace "no free parameters" with "one scheme-dependent parameter γ."

### P1A-M18: Sec. III A 0.27°–0.30° "qualitative consistency" hides the offset from observation
**Sec. III A, page 8**: "The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ **0.27°–0.30°**." But the observed value is **0.342° ± 0.094°**. The 0.27°–0.30° range is below the central value by 0.04–0.07°, inside the 1σ band but not on the central value. The word "consistent" hides the offset. Worse, the 0.27°–0.30° "prediction" is never derived in this paper — it appears as an asserted benchmark. The figure mentioned in Sec. XIII clarifies this is a "consistency check, not a prediction," but Sec. III A presents it as if it were a prediction.
**Fix**: State that 0.27°–0.30° is a fitted benchmark range, not a derived prediction, and quote the actual offset from the observed central value.

### P1A-M19: Footnote 1 σ(f_NL) inconsistency
**Footnote 1, page 11**. The footnote says the "3–5σ realistic range" comes from two regimes: σ(f_NL) ≈ 0.7 (Fisher-ideal → 5–5.5σ optimistic after r = 0.84 correction) and σ(f_NL) ≈ 1.0 (with systematics → "3–5σ realistic"). Checking the systematics regime: 4.375/1.0 = 4.375σ raw, times r = 0.84 = 3.67σ. So the σ(f_NL) = 1.0 regime gives ~3.7σ, **not the entire 3–5σ range**. The "5σ" upper bound of the realistic range is not reachable from σ(f_NL) = 1.0. Conversely, the "3σ" lower bound requires σ(f_NL) ≈ 1.22, which is not quoted as a degraded value. The 3–5σ headline range is therefore wider than its own footnote justification supports.
**Fix**: Quote the actual realistic significance as 3.7σ, or justify the 5σ upper end with explicit systematics.

### P1A-M20: Acknowledgments references "A(z) comparison" not in this paper
**Acknowledgments, page 18**: "We acknowledge Lior Shamir for providing aggregate CW/CCW galaxy spin counts for the **A(z) comparison**." But there is no A(z) (presumably asymmetry as a function of redshift) analysis in this paper — galaxy spin appears only as a confirmed null. The A(z) work is presumably in Paper IV [23], but acknowledging here for work not done here is unusual.
**Fix**: Move acknowledgment to the paper where the A(z) comparison appears.

---

## NEW MINOR Findings

### P1A-Mn11: Sec. XV "0.73σ" calculation is correct but the implied conclusion is wrong
**Sec. XV, page 18**. The 0.73σ separation is calculated correctly: |0.342 - 0.27|/√(0.03² + 0.094²) = 0.073σ — wait, 0.072/0.0987 = 0.730. ✓. But the paper concludes that "a future tightening of the observational central value's uncertainty below ∼0.05° would be needed for LiteBIRD-vs-current-central tension to cross 1σ." Recheck: if σ_obs drops to 0.05°, then √(0.03² + 0.05²) = 0.058°, and 0.072/0.058 = 1.24σ. So the "0.05°" threshold for 1σ tension is approximately correct. ✓ The arithmetic is fine; my second-pass flag was unwarranted on this point. **No change needed.**

### P1A-Mn12: Eq. (10) bracket notation inconsistent with Appendix B
**Eq. (10), page 6; Appendix B, page 19**. Eq. (10) defines Ξ ≡ [(α/M) M_Pl] D_inf with square brackets emphasizing the dimensionless combination. Appendix B writes the equivalent form ρ_bounce_Λ ~ (α/M) M_Pl⁵ without brackets. These are dimensionally equivalent (since (α/M) has dim -1, M_Pl⁵ has dim +5, total +4 ✓) but the notational inconsistency hides the dimensional accounting from the reader.
**Fix**: Use one notation throughout.

### P1A-Mn13: NANOGrav γ +1.13σ arithmetic is correct
**Sec. X G**: (3.0 - 2.567)/0.382 = 0.433/0.382 = 1.133σ. ✓ Confirms the in-text claim. **No issue.**

### P1A-Mn14: ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴ in Sec. IV D matches ρ_Λ ≈ (2.3 meV)⁴
Recompute: (2.3 × 10⁻³)⁴ eV⁴ = 28 × 10⁻¹² = 2.8 × 10⁻¹¹ eV⁴. ✓ Paper's claim "≈ ρ_Λ to within a factor of unity" is exact, not approximate. Could be tightened to "= ρ_Λ exactly under fit."

### P1A-Mn15: Repeated use of "scheme range ~0.020" propagates through Table IV but never defined
**Table IV row 1, page 20**. The "(scheme range ~0.020)" annotation is presented in a parameter table without being defined in the caption. A table that includes an uncertainty value not defined in the immediate context is incomplete documentation.

---

## NEW NITs

### P1A-N8: Eq. (5)/(6) notation: F^IJ is the "curvature of the Lorentz connection" but the same symbol R^ab_μν is used in Eq. (1). Two different notations for the same object.

### P1A-N9: Sec. II C uses M_Pl (Planck mass) and M_GUT (GUT scale) for the (T_reh/M_GUT)^(3/2) prefactor. The numerical evaluation at T_reh ≈ 10¹⁵ GeV and M_GUT ≈ 10¹⁶ GeV gives (10⁻¹)^(3/2) = 0.0316 ≈ 0.03 ✓. But T_reh ≈ 10¹⁵ GeV is at the *upper* end of plausible reheating temperatures; instantaneous reheating after slow-roll typically gives T_reh < 10¹⁴ GeV. The choice T_reh = 10¹⁵ GeV biases the prefactor upward.

### P1A-N10: Sec. II C 1 "reheating thermal-reset barrier" paragraph (page 7) reads as if added late: it interrupts the dimensional bookkeeping with a thermodynamic argument that, if taken at face value, makes the entire D_inf machinery moot. Either D_inf does the work or thermal reset does the work; both cannot be load-bearing.

### P1A-N11: Sec. XIV D wording: "if minimal ECH *were* to source dark energy through one of the four channels enumerated in Sec. IV, would require N_tot ≈ 92" — using subjunctive "were" tacitly admits the four-channel closure is conditional on the dimensional ansatz of Appendix B, weakening the whole closure claim.

### P1A-N12: Fig. 1 caption says "structurally closed under stated assumptions (this paper)" but the legend in the figure body says only "structurally closed this paper" — minor inconsistency.

---

## Summary of Second-Pass Findings

The fresh-eyes pass added **2 essential**, **8 major**, and **5 minor/nit** findings. The most significant new issues are:

1. **Figure 2 contradicts the main text by 48 orders of magnitude** (P1A-E12) — the figure illustrating the dark-energy mapping uses N=55 while the text requires N≈92.
2. **A cross-reference points to the wrong section** for the condensate-route closure (P1A-E13).
3. **The "scheme range ~0.020" for γ doesn't match any actual prescription difference** (P1A-M14).
4. **Eq. (15) upper bound 10⁻⁵⁸ is not derivable from quoted inputs** (P1A-M15) — only the 10⁻⁶⁰ lower end is.
5. **The footnote-justified "3–5σ realistic" SPHEREx range is wider than its own footnote supports** (P1A-M19).
6. **"Smooth bounce with no free parameters" directly contradicts the γ scheme-dependence in the same paragraph** (P1A-M17).

These issues reinforce the original recommendation of **REJECT**. The paper has not undergone the careful internal-consistency check that PRD expects, and several load-bearing numbers (Fig. 2, Table IV scheme range, Eq. (15) upper bound, footnote 1 sigma range) cannot be reproduced from the paper's own quoted inputs.