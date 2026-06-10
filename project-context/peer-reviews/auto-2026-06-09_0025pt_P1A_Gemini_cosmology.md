# P1A auto-2026-06-09_0025pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 718.2s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

**To the Editor of Physical Review D,**

This manuscript presents a systematic, channel-level investigation into four potential routes for generating late-time dark energy from minimal Einstein-Cartan-Holst (ECH) gravity. The authors conclude that all four enumerated routes fail at the amplitude level under a set of stated assumptions. The central theoretical result is a "perturbation-transparency" theorem, which demonstrates that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, rendering the Barbero-Immirzi parameter unobservable in these channels.

The work is ambitious and the core theoretical arguments, particularly the perturbation-transparency theorem and the systematic application of constraints, are sound and represent a valuable contribution to the literature on modified gravity and bounce cosmology. The conclusion—a strong negative result for these specific ECH dark energy models—is significant and worthy of publication.

However, the manuscript suffers from several significant presentation issues, including severely confused figures and a reliance on companion papers without sufficient in-text summary of key assumptions. These issues must be addressed before the paper can be considered for publication. I recommend **MAJOR REVISIONS**.

Below is a detailed list of required changes.

---

### Detailed Findings

#### ESSENTIAL REVISIONS

*   **P1A-E1 | Sec XIII, Fig 4, Page 18 | Figure is incomprehensible and self-contradictory.**
    *   **Problem:** Figure 4, intended to forecast detection significance for the two surviving tests, is critically flawed.
        1.  The caption describes two separate tests: "Top: matter-bounce fNL... Bottom: spectator-ALP cosmic birefringence...". However, the figure is a single plot with one set of axes.
        2.  The legend lists "CMB E-B", "Galaxy Spins", and "Combined (γ=0)". The plot shows three corresponding lines.
        3.  The "Galaxy Spins" line is flat at zero, correctly reflecting the null result, but this is a *past* result, not a *forecast*. A forecast plot should show projected sensitivity.
        4.  The "CMB E-B" line (presumably the `β` forecast) and the "Combined (γ=0)" line (presumably the `fNL` forecast) are not clearly associated with the caption's descriptions. The parameter `γ` is undefined in this context.
        5.  The title is "Detection Significance Forecast", but the figure mixes a confirmed null result with two forecasts, which is confusing.
    *   **Required Fix:** This figure must be completely remade. I recommend splitting it into two separate, clear forecast plots:
        1.  A plot for the SPHEREx `fNL` forecast, with the y-axis as `σ(fNL)` or S/N, and the x-axis as Year. The theoretical value `fNL = -35/8` and the null hypothesis `fNL = 0` should be clearly marked.
        2.  A plot for the LiteBIRD `β` forecast, showing the projected error bars `σ(β)` shrinking over time. The current observational value (`β_obs = 0.342° ± 0.094°`) and the benchmark model value (`β ≈ 0.27°`) should be clearly shown.
        Alternatively, remove the figure entirely and describe the forecasts in the text.

#### MAJOR REVISIONS

*   **P1A-M1 | Sec II, Fig 2, Page 5 | Figure is poorly labeled and potentially misleading.**
    *   **Problem:** Figure 2, illustrating the energy density hierarchy, lacks axis labels and clear explanations. The y-axis appears to be energy density, and the x-axis time/epoch, but this is not stated. The labels "This work 10⁵" and "ΛCDM 10¹²⁰" are placed next to each other in a way that obscures their different meanings. The `10^120` is the ratio of energy scales (`M_Pl^4 / ρ_Λ`), while the `10^5` is presented as a reparameterized sensitivity to the number of e-folds (`N_tot`). This is an apples-to-oranges comparison that needs explicit clarification.
    *   **Required Fix:** Add clear labels to both axes (e.g., "Cosmological Epoch" and "Energy Density (GeV⁴)"). The caption and/or in-figure annotations must explicitly state what the `10^120` and `10^5` numbers represent and why they are being compared (i.e., the standard fine-tuning problem vs. a reparameterized sensitivity).

*   **P1A-M2 | Throughout | Over-reliance on companion papers without sufficient context.**
    *   **Problem:** The paper's arguments frequently depend on results and assumptions from companion papers [2, 6, 23]. While referencing is necessary, this manuscript must be reasonably self-contained. Key load-bearing assumptions are not stated. For example, Table I and Sec XIII state that the `fNL = -35/8` prediction is "Class-level: scalar-only w = 0 matter-bounce under Assumption (f) of the companion forecast [2]". The reader has no way to evaluate this claim without knowing what "Assumption (f)" is.
    *   **Required Fix:** For every result or assumption imported from a companion paper that is critical to the logic of *this* paper, the authors must provide a concise summary of that assumption or the method used to obtain the result. For instance, "Assumption (f)" from paper [2] must be explicitly stated and briefly justified in a footnote or in the main text.

*   **P1A-M3 | Sec II C 1, Page 7 | Justification for the `(T_reh/M_GUT)^(3/2)` prefactor is weak.**
    *   **Problem:** The derivation of the inflationary dilution factor `D_inf` in Eq. (11) includes a prefactor `(T_reh/M_GUT)^(3/2)`. The justification for this specific power is based on "dimensional / phase-space grounds for the axial-current variance" and is explicitly called a "phenomenological phase-space ansatz". While the authors are commendably transparent about this, it remains a significant weak point in the quantitative claim that `N_tot ≈ 92`. The subsequent "reheating thermal-reset barrier" argument is much stronger and more physical.
    *   **Required Fix:** The authors should restructure this section to lead with the stronger, more physical "reheating thermal-reset" argument as the primary reason for the channel's closure. The dimensional bookkeeping leading to `N_tot ≈ 92` should be presented as a secondary, illustrative calculation that is conditional on the stated ansatz. This would make the paper's overall conclusion less sensitive to this weak link.

#### MINOR REVISIONS

*   **P1A-m1 | Abstract & Sec XIV D, Page 1, 19 | Calculation of `k_phys` scaling needs clarification.**
    *   **Problem:** The abstract and Sec XIV D state that a mode `k_SPHEREx` is pushed to `k_phys ~ e^32 k_SPHEREx_phys`. The text explains this comes from `N_tot ~ 92, N_exit ~ 60`. The physical scale `λ_phys` scales as `a`, so wavenumber `k_phys` scales as `a^-1`. The number of e-folds between exit and the bounce is `N_exit`. The total number of e-folds from the bounce to the end of inflation is `N_tot`. The scale factor ratio is `a_end / a_bounce = e^N_tot`. The scale factor ratio from exit to end is `a_end / a_exit = e^(N_tot - N_exit)`. A mode that exits the horizon has `k_comoving = a_exit H_exit`. Its physical wavenumber at the bounce would be `k_phys_bounce = k_comoving / a_bounce = (a_exit / a_bounce) H_exit = e^N_exit H_exit`. The text seems to be comparing the physical scale of a comoving mode `k_SPHEREx` at the bounce vs. at horizon exit. The scaling should be `k_phys(bounce) / k_phys(exit) = a(exit) / a(bounce) = e^N_exit`. The `e^32` factor comes from `N_tot - N_exit`, which is the number of e-folds *after* horizon exit. This seems to describe how far inside the horizon the mode is at the end of inflation, not its physical scale at the bounce.
    *   **Required Fix:** Please clarify the exact comparison being made. The current phrasing `k_phys ~ k_SPHEREx e^(N_tot - N_exit)` seems to be comparing the physical wavenumber of a mode today with its value if it were pushed back to the bounce, but the logic is slightly tangled. A clearer step-by-step derivation of the `e^32` factor is needed.

*   **P1A-m2 | Sec X, Page 15 | Distinction between Holst dual and Pontryagin density.**
    *   **Problem:** The text and a footnote correctly state that the Bianchi-vanishing of the Holst dual `εR` is distinct from the topological nature of the Pontryagin density `RR`. An earlier version of the manuscript apparently confused the two.
    *   **Required Fix:** While the correction is noted, this point is critical enough to warrant slightly more emphasis in the main text of Sec X. The authors should explicitly write out the form of the Pontryagin density (`ε^{μνρσ} R_{μν}{}^{αβ} R_{ρσ αβ}`) to make the distinction from the Holst term (`ε^{μνρσ} R_{μνρσ}`) visually and textually unambiguous for the reader.

*   **P1A-m3 | Sec IV, Page 8 | Scope of "channel-level enumeration".**
    *   **Problem:** The paper emphasizes that its "four-route closure" is a "channel-level enumeration, not an operator-level basis." It explicitly lists omitted operators like the gravitational Chern-Simons term.
    *   **Required Fix:** To strengthen this point, the authors should briefly state *why* these operators were omitted from the "minimal" set. For example, are they higher-dimension, or do they require additional fields not present in the minimal ECH setup? A sentence of clarification would improve the scoping.

#### NIT-PICKS (Cosmetic)

*   **P1A-N1 | Page 1 | Date format.**
    *   **Problem:** The date is "June 8, 2026 PDT". Future dates are unconventional for submissions.
    *   **Required Fix:** Change to the current date of submission.

*   **P1A-N2 | Page 1 | Footnote formatting.**
    *   **Problem:** The footnote `a` on page 1 has its text ("This Bianchi-identity vanishing...") separated from its marker in the main text by the author's email address.
    *   **Required Fix:** Adjust the LaTeX formatting to place the footnote text at the bottom of the page as is standard.

*   **P1A-N3 | Page 20 | Acknowledgments.**
    *   **Problem:** The author acknowledges an AI research assistant (Claude). While transparency is good, PRD's policies on this are evolving.
    *   **Required Fix:** The author should ensure this acknowledgment complies with the journal's latest guidelines on the use of AI in manuscript preparation.

---

### Summary recommendation

**MAJOR REVISIONS**

The manuscript provides a valuable, rigorous, and ultimately negative assessment of minimal ECH as a source for dark energy, a result of significant interest to the cosmology community. The perturbation-transparency theorem is a particularly elegant and important finding. However, the paper is marred by critical flaws in its figures and a lack of self-containment regarding key assumptions from companion works. These issues prevent a clear and critical evaluation of the paper's claims. Once the figures are corrected and the logical dependencies on external work are properly contextualized within the manuscript, it will likely be suitable for publication in Physical Review D.