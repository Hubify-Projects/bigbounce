# Single Best Next Research Path

**Created:** 2026-03-18
**Answer:** LQC Perturbation-Formalism Audit (Dressed-Metric vs Hybrid)

---

## Why It Dominates

### 1. Directly impacts the flagship prediction.

Our entire program rests on f_NL = -35/8. This value was computed in the context of a generic matter bounce contraction phase. But the Wilson-Ewing model we actually advocate uses LQC, which has TWO distinct perturbation formalisms:

- **Dressed-metric** (Agullo, Ashtekar, Nelson 2012): perturbations propagate on a quantum-corrected effective geometry
- **Hybrid** (Fernandez-Mendez, Mena Marugan, Olmedo 2012): perturbations are Fock-quantized on a loop-quantized background

These formalisms agree at the power spectrum level for modes deep in the infrared (k << k_LQC), but differ near the bounce scale. Whether they agree for the BISPECTRUM has not been systematically checked.

If the pre-bounce f_NL = -35/8 is modified differently by the two formalisms during bounce transmission, then either:
- One formalism is wrong (testable prediction about quantum gravity)
- The prediction has a formalism-dependent error bar (must be quantified)

Either outcome is scientifically important.

### 2. Bounded effort.

This is a literature audit plus a targeted comparison, not an open-ended research program. The key papers are:
- arXiv:2405.12296 (2024 LQC perturbation comparison, if it covers bispectrum)
- Agullo et al. (2021) on LQC anomaly predictions (uses dressed-metric)
- Wilson-Ewing (2013) on the matter bounce in LQC
- Any paper computing f_NL through an LQC bounce

Can be completed in 1-2 focused sessions. If the literature already resolves the question, it takes hours.

### 3. Every outcome is informative.

| Outcome | Implication | Next step |
|---------|------------|-----------|
| Formalisms agree for bispectrum | Prediction strengthened, confidence -> ~90% | Move to path #2 (independent derivation) |
| Formalisms disagree for bispectrum | Genuine LQC-specific science | Compute the difference; this becomes the paper's strongest result |
| Literature already resolves it | Free confidence boost | Move to path #2 immediately |
| No paper has computed bispectrum in both | Novel calculation target identified | Do the calculation; publishable regardless of answer |

There is no outcome that wastes time. Every branch produces usable information.

### 4. Minimal sprawl risk.

This is the exact opposite of model-space wandering. We are not exploring new models, new couplings, or new theory spaces. We are performing a precision check on a specific prediction within a specific framework that we have already committed to.

### 5. Directly feeds Paper 1.

Whether the answer is "formalisms agree" or "formalisms disagree," either result goes straight into the paper's discussion of prediction robustness. The current paper cannot honestly claim f_NL = -35/8 without addressing which LQC formalism it assumes and whether the choice matters.

---

## Exact Execution Plan

### Step 1: Literature Extraction (Session Start)

Read arXiv:2405.12296 (the 2024 LQC perturbation comparison paper). Extract:
- What observables are compared between dressed-metric and hybrid?
- At what k-scales do the formalisms differ?
- Does the comparison extend to the bispectrum or only the power spectrum?
- What is the status of third-order perturbation theory in either formalism?

### Step 2: Bispectrum Literature Check

Search for ANY paper that has computed f_NL through an LQC bounce in BOTH formalisms.
- If such a paper exists: extract the comparison, document it, and assess whether the difference is at observable k.
- If no such paper exists: confirm that this is a genuine gap. This itself is a finding worth documenting.

### Step 3: Transfer Function Analysis

For the Wilson-Ewing quasi-dust model specifically:
- Compute (or extract from literature) the bounce transfer function for scalar perturbations in both formalisms.
- For modes at k << k_LQC (which is ALL observable modes), check whether the leading-order transfer coefficient is unity in both formalisms.
- The key quantity: T(k) = zeta_post / zeta_pre for k/k_LQC << 1.

### Step 4: Impact Assessment

If the transfer differs between formalisms:
- Compute the impact on f_NL: delta(f_NL) = f_NL_dressed - f_NL_hybrid
- If |delta(f_NL)| > 0.5 (MegaMapper sigma): this is observationally distinguishable -> major result
- If |delta(f_NL)| < 0.1: effectively irrelevant -> prediction confirmed as robust

If the transfer agrees:
- Confirm and document
- State that f_NL = -35/8 is formalism-independent at leading order for k << k_LQC
- This is a clean positive result for the paper

---

## What Would Kill It Quickly

If the literature already shows that dressed-metric and hybrid agree to all orders for superhorizon modes at k << k_LQC, the question is resolved trivially. This is actually the EXPECTED outcome, because:
- Both formalisms reduce to the classical Friedmann dynamics far from the bounce
- Superhorizon modes with k/k_LQC ~ 10^{-56} are astronomically far from the regime where the formalisms differ
- The bispectrum is generated during CONTRACTION (before the bounce), not during the bounce itself

If this is the case, mark the path as RESOLVED and move immediately to path #2 (independent f_NL derivation).

---

## What Would Make It Genuinely Important

If f_NL is formalism-sensitive even for k << k_LQC, this would mean:
- The choice of quantization scheme for LQC perturbations is empirically testable
- MegaMapper could distinguish dressed-metric from hybrid LQC
- This is a legitimate quantum-gravity-meets-observation result
- It would be the strongest single finding of the entire research program

This outcome is unlikely (for the reasons above) but would be transformative if true.

---

## What Comes After (Regardless of Outcome)

After this path resolves, move to path #2: independent gradient-expansion derivation of f_NL = -35/8. The formalism audit tells us WHETHER the prediction is robust to quantum gravity corrections. The independent derivation tells us WHETHER the prediction is correct in the first place. Both must be answered before the paper can claim f_NL = -35/8 with confidence.
