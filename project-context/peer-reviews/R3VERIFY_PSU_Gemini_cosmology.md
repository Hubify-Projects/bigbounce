# PSU R3VERIFY — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `arxiv/paper_su_criterion/main.pdf` sha256=9f1fc41cce00b03f0cbbff80c709353e04958259925519984c87b9632bf0443d pages=6
**Review packet(s)**: `b50705422eea8ed745098d4277e9beaf4e8295af38a7af4268a0faf9bc5e314b, 965d6559012b95dd4e7bb835951a0e40c4a80abecca7b7b736aa94b8bc40f8f4`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3208 chars)
**Wall time**: 343.4s

---

This is a referee report for the manuscript "The separate universe computes a different variable: an exact criterion for $\delta N = \zeta$ in non-attractor phases" submitted to Physical Review D.

The paper presents a rigorous and mathematically elegant analysis of the separate universe (SU) formalism in non-attractor phases, identifying a specific, closed-form criterion ($I$) that controls the exactness of the identification between the SU e-fold count $\delta N_c$ and the curvature perturbation $\zeta$. The demonstration that the $O(1)$ discrepancy in the matter-dominated contraction is an identification error rather than a failure of the SU formalism itself, and the exact cancellation of the second-order map to the isotropic $-5$ value, are excellent theoretical results. 

However, the manuscript in its current form is a draft that contains severe version-history leaks, literal copy-pastes from an internal review log, and relies on unpublished GitHub markdown files for load-bearing derivations. These issues must be corrected before publication.

### Findings

**1. ESSENTIAL: Review-log prose and version-history leaks in the main text**
*   **Location:** Page 6, Appendix A 5
*   **Problem:** The text contains literal internal review log prose and version-history reconciliation notes: "...reconciled by an independent adjudication...", "...the earlier initial-label figure $5/24(2\epsilon-15) = -5/2$ came from composing the map with the linear-mode weight $\lambda' = 2\lambda$...", and "...correcting the weight closes the gap $5(6-\epsilon)/24$ exactly." This is internal bookkeeping and peer-review/audit history that has accidentally been left in the submitted manuscript.
*   **Required fix:** Remove all internal review log prose. State the final, correct physical result and its derivation directly, without narrating the history of how an earlier incorrect figure was reconciled.

**2. ESSENTIAL: Internal bookkeeping placeholders and inline script names**
*   **Location:** Page 6, Appendix A 5; Page 4, Reproducibility Statement
*   **Problem:** The text includes inline references to internal script names and markdown files as if they were citations or standard text: `(psu_gates_S9_S10_2026_09_05.py)` and `(research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md)`. 
*   **Required fix:** Remove all inline file paths and script names from the physics text. If a script must be referenced to point to a specific numerical check, do so formally via a citation to a published repository in the bibliography.

**3. MAJOR: Standalone reader test violation (reliance on unpublished notes)**
*   **Location:** Page 5, Appendix A 2; Bibliography [23, 24]
*   **Problem:** The paper relies on unpublished GitHub markdown files (Refs [23, 24]) for the derivation of the second-order map and the in-in shape. Appendix A lists the 5 kernel contributions ("zlap", "psi2", "grad", etc.) but does not provide the ADM constraint equations or the steps to solve them. A theoretical physics paper must be self-contained. A reader cannot verify the exact ADM constraint solve simply by reading the stated final kernel pieces, and they should not be required to navigate to a GitHub commit of an unpublished `.md` file to find the physics derivation.
*   **Required fix:** Either provide the core steps of the second-order ADM constraint solve in the appendix (or a Supplemental Material PDF), or cite a formally published, peer-reviewed paper that contains this derivation. 

**4. MAJOR: Reproducibility statement points to local file paths**
*   **Location:** Page 4, Reproducibility Statement
*   **Problem:** The manifest lists local file paths: `reproducibility/manifests/experiments/lift2-separate-universe-failure-criterion.json` and `reproducibility/manifests/experiments/psu-gates-s1-s2-label-composition-criterion.json`. 
*   **Required fix:** The data availability / reproducibility statement must point to a public repository (e.g., Zenodo, GitHub release) with a frozen DOI, not local directory paths on the author's machine.

**5. MINOR: LaTeX formatting errors causing massive vertical gaps**
*   **Location:** Page 5, Eq (A1); Page 6, Eq (A6)
*   **Problem:** There are massive vertical blank spaces in the rendered PDF inside these equations. This is likely caused by improper sizing of evaluation bars (e.g., using `\Big|_{\rm worldline}` without proper bounding, or mismatched `\left.` and `\right|`).
*   **Required fix:** Correct the LaTeX formatting so the equations render compactly without breaking the page layout.

**6. NIT: Typo**
*   **Location:** Page 1, Section I
*   **Problem:** "isoceles value they print as $-35/8$"
*   **Required fix:** Change "isoceles" to "isosceles".

## Summary recommendation
MAJOR REVISIONS

The core physics results—specifically the identification of the $I$ criterion and the exact second-order mapping that resolves the $O(1)$ discrepancy in matter-dominated contractions—are mathematically sound, novel, and highly relevant to the cosmology community. The exact cancellation of the $\mu^2$ and $\epsilon^2$ terms to yield the isotropic $-5$ value is a beautiful result that is well-supported by the stated equations. However, the manuscript currently reads like an internal draft, complete with review-log prose, inline script names, and a reliance on unpublished GitHub markdown files for load-bearing derivations. The author must clean up the text to meet the formal standards of a Physical Review D Letter and ensure the theoretical derivations are sufficiently self-contained.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a fresh-eyes review of the manuscript, focusing on physical consistency, internal cross-references, and mathematical assumptions. 

[PSU-E1, MAJOR, m1, N1] **Physical inconsistency in the translation term monopole (Appendix A 3)**
*   **Location:** Page 6, Appendix A 3: "the trace part vanishes at $n_s=1$, and the shear gives the quadrupole-only translation term $T(\epsilon, \mu) \dots$ monopole 0 (all $\epsilon$)."
*   **Problem:** The author computes the kinematic effect of the spatial translation $\xi^i \partial_i \zeta$ on the bispectrum and explicitly assumes a scale-invariant spectrum ($n_s=1$) to drop the trace part, concluding the translation term has exactly zero monopole for all $\epsilon$. However, for a general constant-$\epsilon$ background, the exact scalar power spectrum is not scale-invariant ($n_s - 1 \neq 0$, except for specific dualities like $\epsilon=3/2$ or the $\epsilon \to 0$ limit). Because the trace of the translation operator acting on the two-point function is proportional to $n_s-1$, the translation term *must* carry a non-zero, $\epsilon$-dependent monopole for general $\epsilon$. 
*   **Consequence:** By artificially setting $n_s=1$ for this specific term while keeping general $\epsilon$ everywhere else, the author forces $f_{map}^{init}$ and $f_{map}^{fin}$ to have the exact same monopole ($-5\epsilon/6$). If the correct $\epsilon$-dependent trace part were included, $f_{map}^{init}$ would have a different monopole, and the composed map $f_{in-in}/\lambda + f_{map}^{init}$ would no longer evaluate to exactly $-5$ for all $\epsilon$. The author must either restrict the exact $-5$ claim to backgrounds where $n_s=1$ is exact, or re-evaluate the translation monopole using the exact $n_s(\epsilon)$ and report the resulting $\epsilon$-dependent deviation.

[PSU-E2, MINOR, m2, N2] **Internal contradiction regarding contributions to $f_{map}^{fin}$**
*   **Location:** Page 2, Footnote 1.
*   **Problem:** The footnote states: "Each of the five geometric contributions to $f_{map}^{fin}$ carries an overall factor of $\epsilon$: the lapse, the second-order metric perturbation, the gradient term, the final-position worldline displacement, and the initial-label translation." 
*   **Correction required:** The "initial-label translation" is not a contribution to $f_{map}^{fin}$. As correctly derived in Appendix A 2 and A 3, the translation term $T(\epsilon, \mu)$ is the difference between the two labels ($f_{map}^{init} = f_{map}^{fin} + T$). Therefore, it is the fifth contribution to $f_{map}^{init}$, while $f_{map}^{fin}$ only has four contributions. The footnote should be corrected to reflect this.

[PSU-E3, MINOR, m3, N3] **Futuristic / Stale Dates**
*   **Location:** Page 1 dateline; Bibliography Refs. [23] and [24].
*   **Problem:** The manuscript is dated "September 7, 2026", and the unpublished GitHub commits in the bibliography are dated "2026-09-03" and "2026-09-04". 
*   **Correction required:** Unless this manuscript is intentionally post-dated for a specific double-blind review system that requires it, these dates appear to be typos for 2024 and should be corrected to avoid confusion.