# Single Best Next Path

**Created:** 2026-03-18
**Answer:** Complete Independent f_NL Verification via Gradient Expansion

---

## THE ANSWER: Complete Independent f_NL Verification via Gradient Expansion

---

## Why It Dominates

This is not the most exciting path. It's not the one most likely to produce novel science. But it is the one that MUST be done before anything else matters.

### Reason 1: Foundation dependency.

Every other path in the ranked stack assumes f_NL = -35/8 is correct. The LQC formalism audit, the PBH channel assessment, the ekpyrotic check -- all build on a prediction that has NOT been independently reproduced and has a literature discrepancy.

The f_NL derivation execution (file `fnl_derivation_execution/final_verdict.md`) was explicit: the convention conversion is resolved, the dominant vertex is confirmed, the field redefinition contribution is confirmed -- but the actual numerical coefficient of the in-in time integral was NOT independently reproduced. Confidence stands at 75%. That means there is a 1-in-4 chance the entire program's flagship prediction is wrong at the numerical level.

No research program should build on a 75% foundation when a well-defined calculation can raise it to >95%.

### Reason 2: Quick resolution.

The Salopek-Bond gradient expansion for matter contraction is a well-defined calculation. It can be completed in 1-2 focused sessions. The answer is either -35/8 (confirmed, confidence -> 95%+) or -35/16 (weakened but alive at 4.4 sigma MegaMapper) or something else entirely (major discovery).

The gradient expansion avoids the in-in formalism entirely. It works directly with the perturbed Friedmann equations in real space, solving order by order. This is an independent method -- not a repetition of Cai et al.'s calculation, but a completely different derivation pathway. If both methods agree, the result is established.

### Reason 3: Every outcome is informative.

Unlike many research paths where failure means wasted time, here:

| Outcome | Probability | Implication | Program impact |
|---------|------------|-------------|----------------|
| f_NL = -35/8 | ~75% | Cai et al. confirmed | Granite foundation, confidence >95%, all downstream paths unlocked |
| f_NL = -35/16 | ~20% | Li-Brandenberger correct | Still significant (4.4 sigma MegaMapper), but less decisive. Source of factor-2 becomes publishable finding |
| f_NL = something else | ~5% | New result | Potentially major discovery. Must understand why three groups disagree |

There is no wasted outcome. Every branch produces usable science.

### Reason 4: It unblocks the stack.

Until this is resolved, paths #2-#7 are building on sand. After this is resolved, we can pursue the formalism audit and PBH channel with confidence.

Consider the alternative: we spend a session on the formalism audit, confirm that dressed-metric and hybrid agree for superhorizon modes (the expected result), and then discover in the next session that f_NL is actually -35/16. The formalism audit would have been correct but irrelevant -- we confirmed robustness of a number that was wrong.

The verification must come first. Everything else follows.

---

## Exact First Calculation

**Salopek-Bond Gradient Expansion in Matter Contraction:**

Background: a(t) = a_0(-t/t_0)^{2/3}, H = 2/(3t), w = 0

### Step 1: Perturbed Friedmann equations to second order in gradient expansion

Write the local Hubble rate as H(t, x) = H_0(t) + H^(1)(t, x) + H^(2)(t, x), where the superscripts denote perturbation order and the gradient expansion parameter is epsilon_grad ~ (k/aH)^2 << 1 for superhorizon modes.

### Step 2: First-order growing mode

Solve for zeta^(1) on superhorizon scales. In matter contraction, the curvature perturbation has a GROWING mode:

zeta^(1) proportional to (-t)^{-1}

This is the key subtlety. The delta-N formalism fails because it assumes constant zeta on superhorizon scales. The gradient expansion tracks the growing mode correctly by solving the constraint equations order by order without assuming zeta is conserved.

### Step 3: Second-order source identification

The quadratic source for the second-order perturbation is:

S^(2) ~ (partial zeta^(1))^2 + zeta^(1) * partial^2 zeta^(1)

The exact coefficients come from the nonlinear terms in the Hamiltonian and momentum constraints. These are standard (Salopek & Bond 1990; Rigopoulos & Shellard 2003).

### Step 4: Second-order solution

Solve the second-order constraint equation sourced by S^(2). The growing mode of zeta^(2) will scale as (-t)^{-2} (square of the first-order growing mode), with a definite numerical coefficient.

### Step 5: f_NL extraction

f_NL = (5/6) * [zeta^(2) / (zeta^(1))^2] on superhorizon scales

The factor 5/6 converts from the Salopek-Bond convention to the Planck convention (f_NL defined via Phi = Phi_G + f_NL * Phi_G^2, where Phi = (3/5) zeta in matter domination).

### Step 6: Comparison

Compare with:
- -35/8 = -4.375 (Cai, Chen, Easson, Langlois, 2009)
- -35/16 = -2.1875 (Li & Brandenberger, 2016, at c_s = 1)

---

## What Would Kill It Quickly

- If the gradient expansion gives -35/8 -> confirmed in the first session. Total effort: hours. The entire remaining stack is unlocked.
- If it gives -35/16 -> the program is weakened but not dead. MegaMapper detection drops from 8.75 sigma to 4.4 sigma. The discrepancy between methods becomes the interesting question (why does the in-in formalism and gradient expansion disagree with each other, or why does Li-Brandenberger's approach give a different answer?).
- If it gives a different value -> more work needed to understand why, but the RESULT is the payoff.

---

## What Would Make It Genuinely Important

Independent confirmation of -35/8 would be the strongest foundation any bounce cosmology program has achieved: a parameter-free prediction, independently derived by two methods, testable at 8.75 sigma by MegaMapper.

If it reveals the source of the Li-Brandenberger discrepancy, that's a publishable result in its own right. The community has lived with this disagreement since 2016. Resolving it via an independent method would be a service to the field regardless of which value turns out to be correct.

---

## What Comes After

**If f_NL = -35/8 confirmed:**
1. Formalism audit (#2) -- quick literature check, expected trivial
2. PBH channel (#3) -- second observable, breaks single-point-of-failure
3. Paper with: confirmed f_NL + formalism robustness + (if viable) PBH/GW prediction

**If f_NL = -35/16:**
1. Investigate the factor-of-2 discrepancy -- where exactly does it enter?
2. Recalculate MegaMapper and SPHEREx SNR at the lower value
3. Assess whether 4.4 sigma is still sufficient for a compelling paper
4. Proceed with formalism audit and PBH channel at the revised value

**If f_NL = something unexpected:**
1. Triple-check the calculation
2. Compare term by term with Cai et al. and Li & Brandenberger
3. This becomes the paper's central result
