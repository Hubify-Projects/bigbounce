# P1A auto-2026-06-08_1520pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 139.0s

---

**Referee Report on "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter" by Houston Golden**

This manuscript presents a systematic assessment of four potential channels through which minimal Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The central claims are a "channel-level closure" of these routes at the amplitude level and a new "perturbation-transparency theorem" for canonical scalar matter. The paper is well-structured, ambitious in scope, and commendably transparent about its assumptions and limitations. The perturbation-transparency theorem, in particular, is a clear and significant theoretical result.

However, the manuscript in its current form has several issues that require significant revision before it can be considered for publication in Physical Review D. The most critical issue is the reliance on multiple companion papers cited as "in preparation" for key observational and numerical results.

Below is a detailed list of findings.

---

### ESSENTIAL

*   **P1A-E1: Unsupported Claims from "In Preparation" Companion Papers (Multiple Sections)**
    *   **Location:** Abstract (p. 1), Sec. III B (p. 8), Sec. V (p. 11), Sec. XV (p. 18), and throughout. Citations [2], [6], [23], [46].
    *   **Problem:** The manuscript makes several load-bearing claims that are supported only by citations to companion papers listed as "in preparation". A manuscript submitted to PRD must be self-contained or cite publicly available work (i.e., published or posted on a preprint server like arXiv). Claims without accessible evidence are unsubstantiated.
        *   The cosmological parameter values (`H₀`, `ΔN_eff`, etc.) and MCMC analysis are attributed to [6].
        *   The crucial "confirmed null" result for galaxy spin asymmetry, which refutes previous claims in the literature, is based on work in [23].
        *   The SPHEREx Fisher forecast for `f_NL` is detailed in [2].
        *   The PTA analysis and anomaly catalog are in [46] and [23].
    *   **Required Fix:** The author must, at a minimum, post these companion papers to a public preprint server (e.g., arXiv.org) and update the citations accordingly. The claims cannot be evaluated by the reviewer or the community until the methods and results in these supporting papers are made available. This is non-negotiable for publication.

### MAJOR

*   **P1A-M1: Weak Justification for Inflationary Dilution Prefactor (Sec. II C 1, p. 6-7)**
    *   **Location:** Page 6, Eq. (11) and surrounding text.
    *   **Problem:** The derivation of the inflationary suppression factor `D_inf` includes a term `(T_reh/M_GUT)^(3/2)`. The justification for this term is described as "dimensional-analysis aesthetic" and not derived from a first-principles calculation. This is a significant weak point in the quantitative "bookkeeping" argument that maps the fine-tuning problem to `N_tot ≈ 92`. While the author is transparent about this weakness, it undermines the quantitative precision of the claim.
    *   **Required Fix:** The author should restructure this section to lead with the much stronger and more physical "Reheating thermal-reset barrier" argument (currently on p. 7). This argument provides an independent and more robust closure of the channel by showing that thermalization erases any coherent axial current from the bounce. The `N_tot` bookkeeping argument can then be presented as a secondary, illustrative calculation, with its "aesthetic" nature and dependence on the dimensional ansatz made even more explicit.

*   **P1A-M2: Unclear Notation for Wavenumber Scaling (Sec. I, p. 3 & Sec. XIV D, p. 17)**
    *   **Location:** Abstract (p. 1), Introduction (p. 3), and Limitations (p. 17).
    *   **Problem:** The text describes the erasure of the `f_NL` signal using confusing notation for physical and comoving wavenumbers. For example (p. 17): `k_phys^bounce ~ k_SPHEREx * e^(N_tot - N_exit) ~ e^32 * k_SPHEREx`. The term `k_SPHEREx` is a comoving wavenumber, and multiplying it by `e^ΔN` does not yield a physical wavenumber at the bounce in a standard way. The physical argument is sound—a large number of e-folds of inflation pushes observable comoving scales deep into the sub-horizon regime, erasing pre-inflationary perturbations—but the mathematical expression used to represent this is non-standard and unclear.
    *   **Required Fix:** Rewrite these sentences using standard cosmological notation. For example, clarify the relationship between a comoving scale `k` and its physical scale `k_phys(t) = k/a(t)`. Explain that for `N_tot ≈ 92`, the physical wavelength corresponding to SPHEREx scales (`λ_phys = a/k`) was deep inside the Hubble radius (`1/H`) during the early phase of inflation, ensuring that any pre-bounce signal is replaced by standard vacuum fluctuations. The current phrasing obscures this clear physical point.

### MINOR

*   **P1A-m1: Future Date on Manuscript (p. 1)**
    *   **Location:** Page 1, under the author's name.
    *   **Problem:** The manuscript is dated "June 2, 2026". This is presumably a placeholder or typo.
    *   **Required Fix:** Change the date to the date of submission.

*   **P1A-m2: Misleading Label in Figure 2 (p. 5)**
    *   **Location:** Page 5, Figure 2.
    *   **Problem:** The figure labels the "Parity-odd vacuum energy (one-loop, Holst term)" with the value `ρ_vac = M_Pl^4`. The text and Appendix B make it very clear that this identification is a phenomenological *ansatz*, not a derived result, and is the weak link in the dark energy connection. The figure label presents it as a fact.
    *   **Required Fix:** Modify the label to clarify its status, for example: "Parity-odd vacuum energy (ansatz)" or `ρ_vac ~ M_Pl^4 (ansatz)`. This would align the figure more closely with the laudable transparency of the main text.

*   **P1A-m3: Calculation of LiteBIRD Discriminatory Power (Sec. XV, p. 18)**
    *   **Location:** Page 18, point 2 of the conclusions.
    *   **Problem:** The text states LiteBIRD will detect non-zero `β` at `~9σ` (a 0.27°/0.03° overall sensitivity number). This is a potentially misleading statement of sensitivity. The more relevant test is distinguishing a specific model (`β=0.27°`) from the current data (`β=0.342°±0.094°`). The author correctly computes this distinction to be only `~0.73σ`.
    *   **Required Fix:** The author should remove or rephrase the `~9σ` statement to avoid confusion. The `0.73σ` calculation is the more physically meaningful and correctly derived number for the specific model-discrimination question at hand, and should be the focus.

### NIT

*   **P1A-N1: Superseded Value Mentioned (Sec. XI G, p. 15)**
    *   **Location:** Page 15, Section G.
    *   **Problem:** The text states: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts...". This kind of internal version-history comment is not appropriate for a final publication.
    *   **Required Fix:** Remove this sentence. Simply state the current result and its derivation from the companion paper.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper has the potential to be a strong contribution to the literature. The perturbation-transparency theorem is an elegant and important result for cosmologies with a Holst term. The systematic catalog of constraints and the sharp analysis of the tension between the dark energy and matter-bounce predictions are also valuable.

However, the paper cannot be accepted in its current state. The reliance on "in preparation" works for multiple key results (P1A-E1) is a critical flaw that must be rectified. The manuscript would also be significantly improved by addressing the weaknesses in the presentation of the inflationary dilution argument (P1A-M1) and the wavenumber scaling (P1A-M2).

I recommend that the paper be reconsidered for publication after these major revisions are completed, with the most crucial being the public release and proper citation of the supporting companion papers.