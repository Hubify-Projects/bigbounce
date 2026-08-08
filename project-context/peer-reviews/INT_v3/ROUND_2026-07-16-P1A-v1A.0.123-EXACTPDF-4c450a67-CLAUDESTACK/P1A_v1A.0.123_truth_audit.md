# P1A v1A.0.123 — Truth Audit (FIRST Claude leg)

- **Paper:** P1A v1A.0.123 — "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches" (CQG Note, 7 pp)
- **PDF SHA-256:** `4c450a6706b2f4e53faac5ffbc6ec720f21e45c7406aa7186ef830f3fef33f71`
- **Source:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.123; rendered ranges are the gaps between `\begin{comment}…\end{comment}` blocks — L1126–1178, 1298–1346, 1682–1800, 2569–2669, 3764–3988, 4675–4816)
- **Referee report audited:** `API_P1A_claude.md` — claude-opus-4-8 subagent, verdict MAJOR REVISIONS (2 MAJOR / 4 MINOR)
- **Auditor stance:** fresh, skeptical, source-cited. Never dismiss without citation; when in doubt → GENUINELY-NEW-REAL.
- **Prior board:** Codex-subscription gpt-5.6-sol ACCEPT (0 MAJOR / 0 MINOR), v1A.0.123 exact PDF (SSOT banner L12).

**Headline:** The referee found **ZERO correctness errors** and hand-reverified every derivation and numeric (his own §"Independent verification performed (all pass)"). All 6 findings are significance/presentation/verification asks, not defects. On source-check, every one is either already-disclosed in the manuscript, already a tracked SSOT gate, or a bounded ≤1-sentence editorial polish. **No science change is indicated by any finding.**

---

## Verdict matrix

| # | Sev | Finding (compressed) | Verdict | Source citation |
|---|-----|----------------------|---------|-----------------|
| M1 | MAJOR | Per-claim novelty/provenance not delineated; state the one new element | **DISCLOSED-RE-FLAG** + **ALREADY-TRACKED-GATE** | inline provenance present; significance = human CQG gate |
| M2 | MAJOR | NJL check Fierz-ambiguous / channel-incomplete; strengthen or demote | **DISCLOSED-RE-FLAG** + **ALREADY-TRACKED-GATE** | ~6 explicit caveats; strengthen path = alt-regulator gate |
| m3 | MINOR | Benchmark uses n_ψ² not ⟨J₅·J₅⟩ | **DISCLOSED-RE-FLAG** + **ALREADY-TRACKED-GATE** | L2607–2611, L2629–2633; state-specific ⟨J₅J₅⟩ is a tracked gate |
| m4 | MINOR | Torsion-vanishing lemma compressed | **GENUINELY-NEW-REAL (trivial editorial)** | steps present L2748–2753; 4D contraction coeffs not shown |
| m5 | MINOR | R_A row invites axial-threshold misreading | **DISCLOSED-RE-FLAG** | caption L4779–4786 already disclaims verbatim |
| m6 | MINOR | Verify no residual subcriticality over-statement | **FALSIFIED (as a finding) / verified-clean** | all 3 hits retract/bound: L2655, L3950, L4801 |

**Counts:** 6 findings audited · 0 correctness errors (referee-confirmed) · 0 BLOCKER · 2 MAJOR → both DISCLOSED-RE-FLAG/tracked · 4 MINOR → 1 falsified-clean, 2 disclosed/tracked, 1 trivial-editorial. **Genuinely-new-real editable items: 1 (m4, trivial), plus 2 optional ≤1-sentence editorial polishes surfaced by M1/M2.**

---

## MAJOR findings

### M1 — Novelty/provenance delineation → DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE

The referee asks the authors to (a) attach explicit provenance to each central statement and (b) state the single genuinely-new element. Source-check shows both are already present:

- **General provenance statement (twice):** Abstract L1172–1175 "The identities used here are standard. The contribution is their convention-audited consolidation into the two Cartan branches and the sharply bounded dimensional coefficient benchmark above; no ECH dark-energy or birefringence prediction is made." Intro L1323–1326 "The underlying Cartan elimination, axial contact interaction, and torsion-free Bianchi identity are standard. Our contribution is to place their normalizations, operator ordering, logical branches, and observable scope in one convention-audited derivation."
- **Per-equation inline attribution for the FMT chain** (the referee's load-bearing results 1–2): Eq. `holst_cartan_inverse` L1731–1733 "the same γ²/(1+γ²) bivector inverse displayed … by Freidel, Minic, and Takeuchi [Freidel2005], Eq. (6)"; Eq. `fmt_contorsion` L1770 "their Eq. (17) [Freidel2005]"; back-substitution L1772 "Their direct back-substitution, Eq. (23)"; normalization bridge L1780–1781 "same Freidel–Minic–Takeuchi normalization."
- **Hehl–Datta attribution for the EC −3κ/16 coefficient:** L2591–2592 "Following the standard Hehl–Datta derivation, the resulting axial–axial contact interaction is …" with `\cite{Hehl1976,HehlDattaNJL1971}`.
- **Holst-vanishing (result 3):** L3821–3831 names it "the first (algebraic) Bianchi identity R_{μ[νρσ]}=0" — a named textbook identity, and explicitly distinguishes it from Pontryagin/Nieh–Yan.
- **The "single new element" answer is honestly given:** there is no new physics; the contribution is stated as convention-audited consolidation + the bounded benchmark (abstract L1172–1175). The paper does not overclaim novelty — the referee's own §(3) agrees the open question "is significance/novelty, not correctness."

The **significance judgment** the referee is really invoking ("a CQG editor must see this") is exactly the **tracked "human CQG/editorial review" gate** (SSOT status.md L12: OPEN gates include "human CQG/editorial review"). That is not an editable defect; it is a venue call already on the ledger.

Residual: there is no *single consolidated* place delineating result-by-result "X from ref [Y], new element = Z." The material is present but distributed inline. A one-sentence "Relation to prior work" summary would fully close the referee's "a reader cannot separate what is original from re-derived" phrasing. This is an optional editorial nicety (surfaced in the GENUINELY-NEW-REAL section), not a genuine gap. **Verdict: DISCLOSED-RE-FLAG; significance = ALREADY-TRACKED-GATE.**

### M2 — NJL check Fierz-ambiguous/channel-incomplete → DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE

The referee (who explicitly notes "all disclosed, and the paper says so repeatedly") asks to either strengthen (beyond-mean-field/channel-complete) or explicitly demote so it cannot be read as vacuum stability. Source-check:

- **Fierz-ambiguity + channel-incompleteness are disclosed ≥6 times:** Abstract L1152–1156 "In the declared direct-channel, hard-four-momentum-cutoff, standard mean-field NJL convention … This conditional sign result does not exclude other truncations, species structures, non-minimal couplings, or propagating torsion." Intro L1334–1337 "A mean-field NJL calculation does not eliminate Fierz ambiguity or beyond-mean-field strong-coupling completions." §III.B L2663–2667 "This result is deliberately conditional. … It does not remove the known Fierz ambiguity of mean-field truncations and does not exclude beyond-mean-field strong coupling, additional flavor/color exchange structure, or non-minimal torsion couplings." App A L2729–2737 (operator-order-specific, not basis-independent). App B L4809–4814 "Its interpretation is strictly standard mean field with this regulator and channel convention … not presented as a regulator- or basis-independent exclusion of every condensate mechanism. No alternate regulator is evaluated here, so we make no claim about how one would change the stability condition."
- **The "strengthen" path is a tracked SSOT gate:** status.md L12 OPEN gates include "alternate-regulator analysis." The referee's beyond-mean-field / channel-complete ask maps directly onto that tracked robustness gate.
- **The demotion is PARTIALLY present already:** App B/table already use "diagnostic" (L4773, L4779 "Coefficient-to-threshold diagnostics") and "we make no claim"; §III.B L2653 uses "coefficient-magnitude diagnostic." What survives is the word "check" (section header L2642 "Standard mean-field NJL check", prose "conditional check") and "closes the scalar condensate" / "no nonzero solution" (L2650–2652, 2663–2664), which the referee says still risks the vacuum-stability over-reading.

Because the over-reading is already blocked by the explicit disclaimers above, this is DISCLOSED-RE-FLAG with the strengthen-path on the tracked ledger. The residual is a bounded editorial relabel (GENUINELY-NEW-REAL section). **Verdict: DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE (alternate-regulator).**

---

## MINOR dispositions

- **m3 (n_ψ² vs ⟨J₅·J₅⟩) — DISCLOSED-RE-FLAG + ALREADY-TRACKED-GATE.** Explicitly disclosed: L2607–2611 "This definition is not an inequality for |⟨J₅ᴵJ₅ᵢ⟩|: number density does not determine that state-dependent coincident composite …"; L2629–2633 "a one-point current does not determine the state-dependent composite ⟨J⁵J⁵⟩". The explicit takeaway the referee requests is already stated: L2632–2633 "The only late-density statement made here is the explicit finite-density coefficient-scale comparison above." "State-specific renormalized axial expectation value" is itself a tracked OPEN gate (status.md L12). No fix required.
- **m4 (torsion lemma compressed) — GENUINELY-NEW-REAL (trivial editorial).** The derivation IS shown (L2748–2753: define t≡ι_{E_I}Tᴵ, contract to get T^J+e^J∧t=0, second contraction t=ι_{E_J}T^J=−3t ⇒ t=0 ⇒ Tᴵ=0). But the intermediate 4D contraction coefficients (the +1 giving "4" and the "−3") are stated as results, not shown. One added line or a standard-source cite would let a reader verify without reconstructing. This is the only finding where a reader genuinely must reconstruct arithmetic. Minimal fix below.
- **m5 (R_A row misreading) — DISCLOSED-RE-FLAG.** The table caption already disclaims it verbatim: L4782–4783 "Thus R_A is a coefficient-magnitude benchmark, not a derived axial-vector condensation threshold"; L4785–4786 "This table tests neither coherent axial order nor a cosmological stress tensor or equation of state." Body L2656–2658 repeats "it is not an independently derived axial-condensation threshold." The disclaimer the referee requests is present in the exact place he points to. Optional cosmetic column separation only; no genuine fix.
- **m6 (residual subcriticality over-statement) — FALSIFIED as a finding / verified-clean.** This was a verification request; grep of every "subcritical" occurrence returns exactly three, all of which retract or bound the blanket claim: L2655 "are not uniformly subcritical," L3950 "does not use a blanket magnitude-subcriticality," L4800–4801 "The old blanket magnitude-subcritical statement is false." No passage implies universal subcriticality of the coupling. Verification satisfied — no residual over-statement exists.

---

## GENUINELY-NEW-REAL (minimal honest fixes)

None touch correctness or science. All are ≤1 sentence, zero-numeric-change editorial polish. In descending order of genuine value:

1. **m4 — add one line to the torsion-vanishing lemma (§ "Minimal ECH and Algebraic Torsion", after L2751).** Minimal fix: append the intermediate contraction, e.g. "(in 4D, ι_{E_I}(e^{[I}∧T^{J]}) = ½(Tᴶ + eᴶ∧t) with ι_{E_J}eᴶ = 4, giving the −3t coefficient on the second contraction)," or cite a standard Einstein–Cartan reference for the contraction identity. Closes the "reader must reconstruct 4D coefficients" gap. ~1 line.

2. **M2 — relabel §III.B to match the appendix's already-present "diagnostic" framing.** Minimal fix: change the §III.B header "Standard mean-field NJL check" → "Standard mean-field NJL diagnostic" (or "illustrative mean-field remark"), and soften "closes the scalar condensate … has no nonzero solution" → "admits no nonzero scalar gap solution in this single mean-field convention." Blocks any residual vacuum-stability over-reading; consistent with App B's existing "diagnostic"/"we make no claim." ~2 clauses. (The substantive strengthen-path stays the tracked alternate-regulator gate.)

3. **M1 — add one consolidated provenance sentence (optional nicety).** Minimal fix: a single "Relation to prior work" line collecting the already-inline attributions, e.g. "The bivector inverse and finite-γ contact coefficient are Freidel–Minic–Takeuchi (Eqs. 6, 17, 23); the EC −3κ/16 axial contact is Hehl–Datta; the Holst-density vanishing is the first Bianchi identity; the contribution here is their convention-audited consolidation plus the bounded benchmark." Fully closes the "reader cannot separate original from re-derived" phrasing. The distributed inline attribution already satisfies the substance, so this is polish, not a gap.

**Recommended disposition:** m4 is the only item that a fresh reader genuinely needs; the M2 relabel is a cheap honesty upgrade worth taking; the M1 sentence is optional. None warrant a science-tier revision. The significance question (M1) and alternate-regulator robustness (M2) remain the two Houston-gated/tracked ledger items already recorded in SSOT.

---

## State assessment

P1A v1A.0.123 is a technically correct, unusually honestly-scoped 7-page CQG Note whose two central claims — the minimal spin-sourced axial contact interaction −(3κ/16)[γ²/(1+γ²)]J₅² and classical zero-spin scalar-sector transparency to GR on the torsion-free branch — the Claude referee independently re-derived and confirmed with zero correctness errors, matching the prior Codex-subscription ACCEPT. Both MAJORs are significance/interpretation asks, not defects: M1's provenance is already delineated inline (Freidel Eqs. 6/17/23, Hehl–Datta, first Bianchi) with an explicit "the contribution is consolidation, no new prediction" statement, and its significance dimension is the already-tracked human-CQG-review gate; M2's Fierz-ambiguity/channel-incompleteness is disclosed ~6× and its strengthen-path is the already-tracked alternate-regulator gate, with the appendix already using "diagnostic" framing. Of the four minors, m3 and m5 are disclosed verbatim in the exact locations flagged (m3 also on the tracked ⟨J₅J₅⟩ gate), m6 falsifies clean on grep (no residual subcriticality), and only m4 (a one-line torsion-lemma contraction) is a genuine, trivial editorial gap. Net: the paper does not require any science change; at most three ≤1-sentence editorial polishes (m4 line, M2 "check"→"diagnostic" relabel, optional M1 provenance sentence) would fully close the referee's language, and the two substantive open questions are Houston-gated ledger items already on the SSOT banner — consistent with a paper sitting at its verified external cap awaiting human venue disposition, not one with open editable science.
