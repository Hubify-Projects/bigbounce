# 30-Day Post-Submission Execution Plan

**Created:** 2026-03-19
**Purpose:** Week-by-week plan for the first 30 days after the focused PNG paper is submitted.

---

## Week 1: Submit + PBH Channel Feasibility (Days 1-7)

### Day 1-2: Final Proofread and Submission
- Final proofread of the focused PNG paper draft
- Verify all figures match the claims table
- Check bibliography completeness (all cited papers present)
- Submit to arXiv (astro-ph.CO primary, gr-qc cross-list)
- Submit to journal (JCAP or Physical Review D) if ready
- Update `version.json` and website activity feed

### Day 3-4: PBH Channel OOM Estimate
- **Calculation:** Characterize Wilson-Ewing bounce transition
  - Solve the LQC effective Friedmann equation for a(t) through the bounce
  - Compute w_eff(t) = p_eff/rho from the modified Raychaudhuri equation
  - Determine the bounce duration Delta_t_bounce and the sharpness parameter |dw/dt|_max
  - Evaluate the non-adiabaticity criterion: |dw/dt|_max / k_bounce^2
- **Compute:** Laptop only. Python + scipy.integrate.odeint. No external resources.
- **Deliverable:** 1-page memo: "Wilson-Ewing Bounce Sharpness and Perturbation Enhancement Potential"

### Day 5-7: Viability Determination
- **If enhancement possible (non-adiabaticity > O(1)):**
  - Begin Bogoliubov coefficient calculation for k ~ k_bounce
  - Estimate T(k) using the sudden approximation
  - Determine the enhancement band: k_min to k_max where T(k) >> 1
  - **Verdict: GO.** Proceed to Week 2 deep dive.
- **If enhancement absent (non-adiabaticity << 1 or symmetric bounce kills resonance):**
  - Document the result: "Wilson-Ewing LQC bounce is adiabatic for all perturbation modes"
  - **Verdict: NO-GO.** Pivot to Path #2 (formalism audit) in Week 2.
- **Deliverable:** PBH viability verdict (GO / NO-GO) with quantitative basis

---

## Week 2: PBH Deep Dive OR Formalism Audit (Days 8-14)

### If PBH GO:

**Days 8-10: Transfer Function Computation**
- Solve the Mukhanov-Sasaki equation numerically through the LQC bounce
- Input: Wilson-Ewing background (dust + Lambda, LQC-corrected Friedmann equation)
- Output: T(k) = |zeta_post-bounce / zeta_pre-bounce| as a function of k
- Map the enhancement profile: peak scale, peak amplitude, bandwidth
- Compute: Laptop (second-order ODE integration, scipy or RK4)

**Days 11-14: PBH Mass Function and GW Spectrum**
- Map enhanced P(k) to PBH mass function f_PBH(M) via Press-Schechter
- Compute induced GW spectrum Omega_GW(f) from second-order perturbation theory
- Compare with observational constraints:
  - PBH: microlensing (Subaru HSC, OGLE), evaporation (diffuse gamma-ray background)
  - GW: LISA sensitivity curve, ET design sensitivity
- Deliverable: "PBH and Induced GW from the Wilson-Ewing LQC Bounce" -- results memo with 2-3 figures

### If PBH NO-GO:

**Days 8-10: LQC Formalism Literature Audit**
- Read arXiv:2405.12296 in detail
- Catalog: what has been compared (power spectrum, tensor modes)
- Identify: what has NOT been compared (bispectrum, third-order perturbations)
- Check all Agullo/Ashtekar/Nelson and Fernandez-Mendez/Mena-Marugan/Olmedo papers for bispectrum results
- Deliverable: "LQC Bispectrum Formalism Comparison: Literature Status" -- gap analysis

**Days 11-14: Formalism Sensitivity Assessment**
- If literature resolves the question: extract and document the answer
- If literature does NOT resolve it: assess feasibility of computing f_NL in both formalisms
  - Estimate effort: what equations need solving, what code needs writing
  - Determine if this is a paper-scale calculation or a quick check
- If the superhorizon argument (k/k_LQC ~ 10^{-56} -> trivially insensitive) is rigorous: document as a robustness theorem
- Deliverable: Formalism sensitivity verdict with either resolution or calculation plan

---

## Week 3: Second Paper Skeleton OR Framework Paper (Days 15-21)

### If PBH viable:

**Days 15-18: Paper Skeleton**
- Draft structure for "Primordial Black Holes from the LQC Matter Bounce: Predictions for LISA and Einstein Telescope"
- Sections: Introduction, Wilson-Ewing Model, Bounce Transfer Function, PBH Mass Function, Induced GW Spectrum, Observational Prospects, Discussion
- Write Introduction and Model sections (reuse from PNG paper where appropriate)
- Generate publication-quality figures: T(k), f_PBH(M), Omega_GW(f) with sensitivity curves

**Days 19-21: Claims Table and Internal Review**
- Draft claims table (same format as PNG paper: Derived vs Assumed vs Fit)
- Self-audit: are all claims defensible? Are caveats visible?
- Identify remaining calculations needed for a complete draft

### If PBH dead + formalism interesting:

**Days 15-21: Formalism Note or Paper 1 Pivot**
- If formalism sensitivity found: draft note for publication
- If formalism insensitive: document as supporting result; pivot to Paper 1 framework paper
- Paper 1 tasks: review `arxiv/main.tex` current state, identify sections needing update, begin revision pass

### If both dead:

**Days 15-21: Paper 1 Framework Paper Completion**
- Review `research/final_phase/01_final_paper_structure.md`
- Update manuscript to reflect focused-path results (f_NL range, ECH closure, Wilson-Ewing selection)
- Complete any remaining sections
- Target: full draft ready for internal review by Day 21

---

## Week 4: Consolidation + Referee Preparation (Days 22-30)

### Days 22-25: Referee Response Preparation
- Assemble the reserve materials from File 06 (reviewer response reserve list)
- Prepare concise responses for each of the 8 likely criticisms
- Draft supplementary material if needed (extended shape function verification, additional Fisher scan results)
- Organize all supporting computations into a referee-response directory

### Days 26-28: Website and Repository Updates
- Update `activity.html` with submission event and any new results
- Update `paper.html` with new paper status
- Update `index.html` stat cards if any numbers have changed
- If PBH results exist: add to data explorer and figures gallery
- Commit and push for Netlify deployment

### Days 29-30: Strategic Review
- Assess what the first month produced:
  - Is the PBH channel alive? If yes, what remains for a complete paper?
  - Is the formalism question resolved? If yes, what did we learn?
  - Is Paper 1 progressing? If yes, what is the completion timeline?
- Draft a 3-month plan based on actual results (not projections)
- Update this roadmap if the landscape has changed

---

## Decision Points

| Day | Decision | Consequence |
|-----|----------|-------------|
| Day 5 | PBH GO/NO-GO | Determines Week 2-3 direction |
| Day 14 | Second observable verdict | Determines Week 3-4 direction |
| Day 21 | Paper skeleton or framework progress | Determines 3-month plan |
| Day 30 | Strategic review | Determines next quarter |

---

## Resource Budget

| Resource | Allocation |
|----------|-----------|
| Compute | Laptop only (all calculations are ODE integration or analytical) |
| External tools | None required |
| Collaboration | None required for first 30 days |
| Literature access | arXiv (free), ADS (free) |
| Total cost | $0 (excluding time) |

---

## Non-Negotiables

1. **Do not delay submission to start PBH work.** The paper is ready. Submit first.
2. **Do not skip the PBH quick kill.** The OOM estimate takes 1-2 sessions. Do it before committing to a deep dive.
3. **Do not pursue deprioritized paths.** The list in File 02 is binding. No ECH perturbation loops, no gradient expansion extensions, no MCMC without theory hooks.
4. **Document every result.** Even negative results (PBH channel dead, formalism insensitive) are worth documenting. Create a final_verdict.md for every investigation.
5. **Update the website.** After submission and after any new results. The website is the public face of the program.
