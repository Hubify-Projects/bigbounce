# INT v3 Independent Referee Report — P1A

- **Model:** claude-opus-4-8 (subagent)
- **Date:** 2026-07-16 (PT)
- **Paper:** P1A v1A.0.123 ("Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches")
- **pdf_sha256:** 4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71
- **Venue:** Classical and Quantum Gravity — profile CQG-NOTE
- **PARSED VERDICT:** MAJOR REVISIONS

---

## Referee prompt applied

"You are an expert referee for Classical and Quantum Gravity. Review this Note manuscript under profile CQG-NOTE to the standard of a real submission. Respond with exactly: (1) VERDICT; (2) numbered ISSUES prefixed [MAJOR]/[MINOR]; (3) one sentence on whether the central claim is supported." Reviewed as a mathematical-physics Note (Einstein–Cartan–Holst algebra): derivations, conventions, dimensional consistency, and claim–evidence alignment checked with genuine rigor.

---

## (1) VERDICT

**MAJOR REVISIONS**

The manuscript is technically sound — every derivation and numeric value I independently recomputed is correct, and the paper is unusually honest about the limits of its claims (it explicitly makes "no ECH dark-energy or birefringence prediction"). The MAJOR flags are therefore about **significance/novelty and the interpretive weight of the two "checks,"** not about correctness. These are gating questions a CQG editor/referee must see addressed before an accept recommendation.

### Independent verification performed (all pass)
- **Eq (2) inverse of the Holst–Cartan bivector operator.** With ⋆² = −1, Q_γ = ⋆ + γ⁻¹𝟙 and Q_γ⁻¹ = (γ²/(1+γ²))(γ⁻¹𝟙 − ⋆): direct product gives (⋆+γ⁻¹)(γ⁻¹−⋆) = 1 + γ⁻², so the prefactor γ²/(1+γ²) is exactly right. Poles at γ=±i (1+γ²=0) and singular γ=0 correctly excluded; γ→∞ EC limit nonsingular. ✓
- **Normalization bridge Eq (6).** 4πG = κ/2 ⇒ πG = κ/8 ⇒ −(3/2)πG = −3κ/16. EC-limit coefficient −3κ/16 = −(3πG/2) matches the standard Hehl–Datta four-fermion value. ✓
- **Torsion-vanishing lemma (p.2).** From e^[I∧T^J]=0 with invertible tetrad: T^J = −e^J∧t ⇒ t ≡ ι_{E_J}T^J = −(4t−t) = −3t ⇒ 4t=0 ⇒ t=0 ⇒ T^J=0. Coefficients (4D contraction) are correct. ✓
- **Dimensional benchmark Eq (10).** With n_ψ=100 cm⁻³ → 7.68×10⁻¹³ eV³, M_Pl=1.2209×10²⁸ eV: κn_ψ² = 8π n_ψ²/M_Pl² ≈ 1.0×10⁻⁷⁹ eV⁴; ρ_Λ=(2.3 meV)⁴≈2.8×10⁻¹¹ eV⁴; ratio ≈ 3.6×10⁻⁶⁹. Coefficient-weighted (×3/16) = 1.9×10⁻⁸⁰ eV⁴ = 6.7×10⁻⁷⁰ ρ_Λ. All ✓.
- **Fierz A→S projection (App. A).** Nieves–Pal normalized F_c, row A col S = (1/4)(−4) = −1; op sign −(F_c) = +1; ×(−3κ/16) ⇒ G_s = −3κ/16. F_c²=1 property holds. ✓
- **NJL gap threshold (App. B).** Chiral-limit gap Eq (B2) → bifurcation G_crit = 2π²/(N_fN_cΛ²); G_s<0 admits no nonzero real M. Correct standard NJL. ✓
- **Table I.** R_S = (3N_fN_c/4π)(Λ/M_Pl)²: 3/4π=0.239, 9/4π=0.716, 27/4π=2.15; R_A = R_S/2 = 0.119, 0.358, 1.07. All arithmetic ✓; the honest retraction of the earlier "blanket magnitude-subcritical" claim (now relying on the sign, not magnitude, since the N_fN_c=9 row is supercritical) is handled correctly.
- **Dimensions.** J₅ (dim 3), J₅² (dim 6), κ (dim −2) ⇒ κJ₅² (dim 4) = energy density. ✓ Bianchi-vanishing of the Holst dual ½ε^μνρσR_μνρσ(Γ̊)=0 correctly distinguished from Nieh–Yan and Pontryagin. Left/right helicity operators equal at T=0 (Eq 12), no birefringence. ✓

---

## (2) ISSUES

**[MAJOR] 1 — Novelty/significance is not delineated (Abstract; §I "Our contribution"; §V).**
Every load-bearing result is standard: the FMT finite-γ four-fermion coefficient γ²/(1+γ²) (Eqs 5,7), the EC axial–axial contact −3κ/16 (Eq 8, Hehl–Datta), the Holst term vanishing by the first Bianchi identity on a torsion-free connection (Eq 13), and canonical scalars not sourcing torsion (§IV). The stated contribution is a "convention-audited consolidation" plus a dimensional benchmark. For a CQG Note this can be acceptable, but as written a reader cannot separate what is original from what is re-derived. The authors must (a) attach an explicit provenance to each central statement (which prior reference already contains it) and (b) state in one sentence the single genuinely new element. The scalar-transparency "theorem" in particular reads as well-known folklore and needs either a novel sharpening or an explicit "we make precise a known fact" framing.

**[MAJOR] 2 — Mean-field NJL "no-condensate" check is Fierz-ambiguous and channel-incomplete (§III.B, App. A–B).**
The conclusion rests on the sign G_scalar=−3κ/16<0 of a single Fierz-projected channel in one operator ordering; no axial/pseudoscalar gap equation is solved and the projection is basis/convention dependent (all disclosed, and the paper says so repeatedly). Because it is this heavily conditioned, it carries little robust physical content yet is presented as a "check" alongside the action-level results. Recommend either strengthening it (beyond-mean-field or channel-complete stability analysis) or explicitly demoting it from a "check" to an illustrative remark, so it cannot be read as a statement about actual vacuum stability. The current §III.B/§VI wording ("no nonzero solution") still risks that over-reading despite the caveats.

**[MINOR] 3 — Finite-density benchmark compares the wrong object (§III.A, Eq 10).**
κn_ψ² uses number-density-squared, whereas the physical contact-energy density is the state-dependent renormalized composite ⟨J₅·J₅⟩, not n_ψ². The manuscript acknowledges this, but then the benchmark's positive content reduces to the near-trivial observation that κ×(density)² ≪ ρ_Λ. State explicitly what quantitative takeaway, if any, the reader should carry away, or the subsection risks being read as more than a dimensional illustration.

**[MINOR] 4 — Torsion-vanishing lemma is compressed (§II, p.2).**
The chain from e^[I∧T^J]=0 through "T^I + e^J∧t" to "t=ι_{E_J}T^J=−3t" is correct but skips the intermediate contraction identities; add one explicit line (or cite a standard source) so a reader can verify the 4D coefficients without reconstructing them.

**[MINOR] 5 — R_A row / |G_A|=3κ/32 in Table I invites misreading (§III.B, Table I).**
R_A is not a derived axial-condensation threshold (stated in the caption), yet it sits in the same table as R_S under a "coefficient-to-threshold" heading. Relabel or separate it so it cannot be read as a physical axial-vector condensation criterion.

**[MINOR] 6 — Verify no residual over-statement of subcriticality.**
The paper correctly retracts the blanket "magnitude-subcritical" claim once the N_fN_c=9 row is shown supercritical; confirm no other passage (e.g., §III.A "does not increase this coefficient benchmark above the EC limit," or §VI) still implies universal subcriticality of the coupling itself.

---

## (3) Is the central claim supported?

Yes — both central claims (the minimal spin-sourced axial contact interaction with coefficient −(3κ/16)γ²/(1+γ²), and classical scalar-sector transparency equal to GR on the torsion-free branch) follow from correct, convention-consistent standard derivations, and the paper does not overclaim any dark-energy or birefringence result; the open question for publication is significance/novelty, not correctness.
