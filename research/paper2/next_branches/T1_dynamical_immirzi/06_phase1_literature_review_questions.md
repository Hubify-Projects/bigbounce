# T1 Phase 1 — Literature Review Questions

**Purpose:** Determine in ≤2 weeks whether T1 is genuinely new and tractable
**Output:** Assessment memo answering 6 questions
**Decision:** If Q1 or Q2 is "no," T1 closes at Phase 1. If Q3 is "yes," reconsider scope.

---

## Q1: Is torsion still algebraic with dynamical θ?

**This is the single most important structural question.**

### What to determine
- [ ] In the Mercuri (2009) action with θ(x) replacing γ, write down the torsion equation of motion explicitly
- [ ] Is it algebraic in the contorsion K (solvable without derivatives of K)?
- [ ] Or does promoting γ → θ(x) introduce derivatives of K, making torsion propagating?

### Why it matters
If torsion remains algebraic → the torsion-elimination strategy still works, and we get a modified reduced action with θ-dependent four-fermion couplings. The computation is tractable.

If torsion becomes propagating → the entire framework changes. Torsion is no longer auxiliary. This would require a much heavier program (propagating torsion QFT). T1 would still be interesting but much harder.

### Where to find the answer
- Mercuri (2009) §II: action structure and torsion equation
- Calcagni & Mercuri (2009): explicit torsion elimination with dynamical θ
- Torres-Gomez et al. (2009): Immirzi field equation of motion

### Kill criterion
If torsion becomes propagating AND the resulting theory is not tractable at one loop → T1 is too hard. Close with documented reasoning.

---

## Q2: Is the dynamical-θ route genuinely new?

### What to determine
- [ ] After torsion elimination with dynamical θ, write down the reduced action S_reduced[e, ψ, θ]
- [ ] Compare term by term with: GR + ALP + four-fermion interaction
- [ ] Identify ANY term in S_reduced that is NOT reproducible by simply adding a standard ALP to GR

### The specific test
Take the reduced action. Set θ = const (recovering minimal EC+Holst). The difference S_reduced(θ(x)) − S_reduced(θ=const) should contain terms that are:
1. NOT of the form (∂θ)² (standard kinetic)
2. NOT of the form θ F∧F (standard axion-photon)
3. NOT of the form V(θ) (standard potential)

If ALL new terms are of these standard forms → the dynamical Immirzi field is just an ALP. FM-T1-1 fires.

### Where to find the answer
- Calcagni & Mercuri (2009): reduced action with dynamical θ
- Compare with Alexander & Yunes (2009): Chern-Simons from dynamical θ

### Survival criterion
There must be at least one term in the reduced action that:
- involves θ coupled to fermion bilinears in a way that is NOT standard Yukawa or axion-fermion coupling,
- OR involves θ coupled to curvature in a way that is NOT standard Chern-Simons,
- OR modifies the four-fermion interaction structure in a θ-dependent way that changes the channel analysis (i.e., the Fierz structure depends on θ).

---

## Q3: Has this computation already been done?

### What to determine
- [ ] Has anyone already computed the one-loop effective action with dynamical Immirzi field?
- [ ] Has anyone already computed V_eff(θ) in this framework?
- [ ] Has anyone already assessed whether a vacuum-like term arises?

### Where to check
- Lattanzi & Mercuri (2010): constraints on Barbero-Immirzi field — did they compute V_eff?
- Calcagni & Mercuri (2009): cosmological implications — did they derive late-time behavior?
- Any papers citing Mercuri (2009) that extend the computation

### Implications
If the computation is ALREADY DONE and the answer is negative → T1 closes (the literature already covers it).
If the computation is ALREADY DONE and the answer is positive → T1 shifts to verification/extension, not original computation.
If the computation has NOT been done → T1 proceeds to Phase 2.

---

## Q4: Does θ plausibly generate a vacuum-like term?

### What to determine
- [ ] In the reduced action, what is the effective potential for θ?
- [ ] Does it have any non-perturbative contributions (instantons, anomalies)?
- [ ] Is there a Peccei-Quinn-like mechanism that could fix θ at a minimum?
- [ ] If θ sits at a minimum, does the vacuum energy there have the right sign and magnitude?

### Physical intuition check
The Mercuri (2009) analogy is: θ plays the role of the QCD axion, and the Nieh-Yan density plays the role of F∧F̃. In QCD, the axion gets a potential from instantons. In gravity: what generates V(θ)?

- [ ] Is there a gravitational analogue of instantons that generates V(θ)?
- [ ] Or is V(θ) put in by hand? (If so, this is not a first-principles derivation.)

### Kill criterion
If V(θ) must be put in by hand with no dynamical origin → the "vacuum term" is assumed, not derived. The theory gap is just displaced from "why w = −1?" to "why V(θ₀) = Λ_obs?" This is NOT progress.

---

## Q5: What observables would θ produce?

### What to determine
- [ ] Does dynamical θ produce birefringence? (Through Nieh-Yan → F∧F coupling?)
- [ ] Does it produce ΔN_eff modifications? (Through modified radiation-era dynamics?)
- [ ] Does it produce galaxy spin asymmetry modifications?
- [ ] Are any of these MORE testable than the minimal framework's predictions?

### Connection to S1
If θ produces birefringence through a DERIVED coupling (not assumed), this would upgrade S1 from "assumed mapping" to "derived mapping." This would be a significant win for both branches.

---

## Q6: What are the known pathologies?

### What to determine
- [ ] Ghost analysis: does θ have a wrong-sign kinetic term on any background?
- [ ] Strong coupling: does the effective theory break down at accessible energy scales?
- [ ] Is the shift symmetry θ → θ + const preserved or broken? If broken, by what?
- [ ] Are there known unitarity violations?

### Where to check
- Magueijo, Zlosnik & Kibble (2013): stability of scalar-tensor theories from first-order gravity
- Any paper that has analyzed the dynamical Immirzi field's stability

---

## Assessment Memo Template

After answering Q1–Q6, write a 1-page assessment:

```
T1 LITERATURE ASSESSMENT — [date]

Q1 (ALGEBRAIC TORSION): [yes/no/complicated]
Q2 (GENUINELY NEW): [yes/no — with specific novel term identified]
Q3 (ALREADY DONE): [yes/no/partially]
Q4 (VACUUM MECHANISM): [plausible/implausible/requires assumed V(θ)]
Q5 (OBSERVABLES): [list with feasibility]
Q6 (PATHOLOGIES): [known issues]

VERDICT: [T1 Phase 2 warranted / T1 closes at Phase 1]
REASONING: [3-5 sentences]
IF PROCEEDING: [specific computation to do in Phase 2]
IF CLOSING: [specific reason, add to negative-result inventory]
```

---

## Reading Order

| Priority | Paper | Time | Focus |
|----------|-------|------|-------|
| 1 | Mercuri (2009) [0902.2764] | Day 1 | Q1, Q2, Q4 |
| 2 | Calcagni & Mercuri (2009) [0902.0957] | Day 2 | Q1, Q2, Q3 |
| 3 | Taveras & Yunes (2009) [0812.3572] | Day 3 | Q2, Q5 |
| 4 | Torres-Gomez et al. (2009) [0904.4877] | Day 4 | Q1 |
| 5 | Lattanzi & Mercuri (2010) [0911.2698] | Day 5 | Q3, Q5 |
| 6 | Magueijo et al. (2013) [1212.0585] | Day 6 | Q6 |
| 7 | Write assessment memo | Day 7 | — |

---

## What NOT to do in Phase 1

- Do NOT start symbolic computation
- Do NOT write SymPy scripts
- Do NOT derive the torsion equation of motion yourself — find it in the literature first
- Do NOT assume the mechanism works — test it against the questions above
- Do NOT spend more than 2 weeks on this phase
