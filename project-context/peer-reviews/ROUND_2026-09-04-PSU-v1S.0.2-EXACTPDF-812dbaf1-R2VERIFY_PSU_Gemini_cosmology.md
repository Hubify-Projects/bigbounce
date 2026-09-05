# PSU ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `arxiv/paper_su_criterion/main.pdf` sha256=812dbaf1af7e8eafa5769730fed55c81cfa8b429fbeab022d1125be1527aca31 pages=4
**Review packet(s)**: `2dce9eed30692a1cba7f6f5ccef2296a68029d727fd071b8d51199ac55c9fcca, 13a8748a46b08b72ad779043252acd38b9ca44a25e6945bab461c47e5215d67b`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2136 chars)
**Wall time**: 398.9s

---

This is a referee report for the manuscript "The separate universe computes a different variable: an exact criterion for $\delta N = \zeta$ in non-attractor phases" submitted to Physical Review D (Letter).

### General Comments
The manuscript presents a concise and interesting analysis of the discrepancy between the separate universe ($\delta N$) formalism and the in-in formalism for computing the squeezed bispectrum in non-attractor cosmological phases. By identifying an exact, invertible change of variable between the fluid e-fold count $\delta N_c$ and the curvature perturbation $\zeta$, the author provides a unified criterion (the integral $I$) that explains both the agreement in ultra-slow-roll (USR) inflation and the $O(1)$ discrepancy in matter-dominated contraction. 

While the physical insight is valuable and the core algebraic results appear correct, the manuscript suffers from a fatal contradiction in the abstract, an algebraic sign error in a main equation, and a severe violation of the standalone-reader requirement by delegating load-bearing derivations to unpublished GitHub repositories. These issues must be resolved before the manuscript can be considered for publication.

### Findings

**1. ESSENTIAL: Abstract Contradiction (Abstract-Last Drift Sweep)**
*   **Location:** Abstract, Page 1
*   **Problem:** The abstract claims: "...the initial-position label (the separate universe's own label) reproduces the in-in monopole exactly, $-5$, for every constant $\epsilon$". This directly contradicts the main finding of the paper. In Section I (Page 1) and Table I (Page 4), the author explicitly states that for a matter-dominated contraction ($\epsilon=3/2$), the separate universe gives $-5$, while the in-in monopole is $-15/8$, resulting in an "$O(1)$ discrepancy" and a "monopole gap of $25/8$". The separate universe does *not* reproduce the in-in monopole exactly for non-attractors; it only reproduces the *separate universe* monopole (which happens to be $-5$ universally). 
*   **Required Fix:** Rewrite the abstract to accurately reflect the body's conclusion. It should state that the initial-position label yields a universal monopole of $-5$ for the separate universe, which *disagrees* with the in-in monopole when $I = O(1)$.

**2. ESSENTIAL: Algebraic Sign Error in Second-Order Map**
*   **Location:** Section II, Page 2, Equation (4)
*   **Problem:** Equation (4) states: $f_{\text{map}}^{\text{fin}}(\epsilon, \mu) = -\frac{5\epsilon}{4}(1-\mu^2) = f_{\text{map}}^{\text{init}} + \frac{5\epsilon}{4(3-\epsilon)}(1-3\mu^2)$. 
    This contains a sign error. Using Eq (3), $f_{\text{map}}^{\text{init}} = \frac{5\epsilon}{4(3-\epsilon)}[(\epsilon-2) - \epsilon\mu^2]$. 
    Subtracting the two yields:
    $f_{\text{map}}^{\text{fin}} - f_{\text{map}}^{\text{init}} = -\frac{5\epsilon}{4}(1-\mu^2) - \frac{5\epsilon}{4(3-\epsilon)}[(\epsilon-2) - \epsilon\mu^2] = -\frac{5\epsilon}{4(3-\epsilon)}(1-3\mu^2)$.
    Therefore, the correct relation is $f_{\text{map}}^{\text{fin}} = f_{\text{map}}^{\text{init}} - \frac{5\epsilon}{4(3-\epsilon)}(1-3\mu^2)$. The manuscript incorrectly uses a plus sign.
*   **Required Fix:** Change the plus sign to a minus sign in the second equality of Equation (4).

**3. ESSENTIAL: Standalone-Reader Test Violation (Load-Bearing Citations)**
*   **Location:** Section I (Page 1) and References [21, 22] (Page 4)
*   **Problem:** The manuscript relies on two unpublished GitHub markdown files [21, 22] for its most critical load-bearing inputs. Specifically, Ref [21] is used to claim that the literature value for the in-in bispectrum in Cai et al. [18] is wrong by a factor of 2, which is the foundation for the $O(1)$ discrepancy claim. Ref [22] is cited as the sole derivation of the exact second-order map (Eqs 3-5), which is the primary novel theoretical result of this paper. A PRD Letter must be self-contained or rely on peer-reviewed (or at least stable arXiv) literature for its central proofs.
*   **Required Fix:** The derivations for the corrected in-in bispectrum (currently Ref [21]) and the second-order threading map (currently Ref [22]) must be included in this manuscript, either by expanding the main text or adding an Appendix/Supplemental Material. Alternatively, these companion notes must be posted to the arXiv and cited properly, though including the core steps in this Letter's supplement is strongly preferred.

**4. MAJOR: Notation Clash for Expansion Parameter**
*   **Location:** Section IV, Page 3
*   **Problem:** The text reads: "...who computed the $O(\epsilon^2)$ (gradient-expansion, $m=2$) correction... the retained term, $(\epsilon/c_s^2)\dot{\zeta}$, is already $O(k^0)$ and $O(1)$ in $\epsilon$". The author uses $\epsilon$ to denote the spatial gradient expansion parameter (following Takamizu et al.) and then immediately uses $\epsilon$ to denote the slow-roll parameter in the very same sentence. This is highly confusing.
*   **Required Fix:** Use a distinct symbol for the gradient expansion parameter (e.g., $\epsilon_{\text{grad}}$ or simply $k/(aH)$) to strictly separate it from the slow-roll parameter $\epsilon$.

**5. MAJOR: Provenance Surfaces and Reproducibility**
*   **Location:** Reproducibility Statement (Page 3) and References [21, 22] (Page 4)
*   **Problem:** The reproducibility statement and references point to raw GitHub commit hashes (e.g., `commit f3516042`). GitHub is a development platform, not a persistent academic archive; repositories can be modified, made private, or deleted, breaking the scientific record.
*   **Required Fix:** Mint a persistent DOI for the exact release of the code and manifests used in this paper via a service like Zenodo, and cite the DOI instead of (or in addition to) the GitHub repository.

**6. MINOR: Phrasing of Ratio vs. Gap**
*   **Location:** Section I, Page 1
*   **Problem:** The text states: "...the gap to $f_{\delta N}^{\text{init}} = -5$ would be $-5/8$, a factor of $8/7$ rather than $8/3$". This phrasing implies the *gap* itself is a factor of $8/7$, but the math indicates the author means the *ratio* of the separate universe result to the in-in result ($(-40/8) / (-35/8) = 8/7$). 
*   **Required Fix:** Clarify the prose to explicitly state that $8/7$ and $8/3$ refer to the ratio $f_{\delta N} / f_{\text{in-in}}$, not a multiplier on the gap.

**7. NIT: Internal Version Tag**
*   **Location:** Top right corner, Page 1
*   **Problem:** The internal version tag "v1S.0.2" appears in the header.
*   **Required Fix:** Remove internal bookkeeping tags for the journal submission.

## Summary recommendation
MAJOR REVISIONS

The paper identifies a mathematically rigorous and physically insightful criterion for when the separate universe formalism diverges from the in-in formalism in non-attractor backgrounds. The identification of the $I$ integral and the worldline-label dependence at second order are valuable contributions to the literature. However, the manuscript cannot be published in its current form due to a direct contradiction in the abstract regarding the core result, an algebraic sign error in Equation 4, and an unacceptable reliance on unpublished GitHub notes for load-bearing derivations. If the author corrects the abstract, fixes the algebra, and incorporates the necessary derivations into an appendix or supplemental material to make the paper self-contained, it will meet the high standards of a PRD Letter.

---

## PASS 2 — self-critique findings (what initial review missed)

[PSU-E1] **Algebraic Contradiction in Textual Definition of $I$**
*   **Location:** Section II, Page 2, immediately below Equation (2).
*   **Problem:** The text states: "$I = 1 - \lambda$ reduces to $\epsilon/3$ for constant $\epsilon$, so $\lambda \equiv 1 - I/3 = 1 - \epsilon/3$". This contains a direct algebraic contradiction. By the author's own definition, $\lambda \equiv 1 - I/3$, which means $1 - \lambda = I/3$. If $1 - \lambda$ reduces to $\epsilon/3$, then $I/3 = \epsilon/3$, meaning $I = \epsilon$. The text incorrectly states "$I = 1 - \lambda$", which would imply $I = \epsilon/3$ and thus $\lambda = 1 - \epsilon/9$, contradicting both the rest of the sentence and the correct mathematical limit of the integral.
*   **Required Fix:** Change "$I = 1 - \lambda$ reduces to $\epsilon/3$" to "$I/3 = 1 - \lambda$ reduces to $\epsilon/3$" or simply state "$I$ reduces to $\epsilon$".

[PSU-m1] **Futuristic Dates**
*   **Location:** Author affiliation block (Page 1) and References [21, 22] (Page 4).
*   **Problem:** The manuscript is dated "September 4, 2026", and the unpublished GitHub notes in the references are dated "2026-09-03" and "2026-09-04". Unless this is an intentional artifact of a specific double-blind or embargoed submission system, these dates are in the future and will confuse the archival record.
*   **Required Fix:** Correct the years to the current year.

[PSU-N1] **Missing Perturbation Amplitude in Gradient Error Term**
*   **Location:** Abstract (Page 1) and Equation (2) (Page 2).
*   **Problem:** The gradient error term is written as an additive $+ O(k_L^2/a^2H^2)$. Since $\delta N_c$ and $\zeta_L$ are first-order perturbations (proportional to the primordial amplitude $\sim 10^{-5}$), the additive error term is actually $O(k_L^2/a^2H^2) \zeta_L$. Writing it without the $\zeta_L$ factor technically implies a zeroth-order error term that would be much larger than the first-order signal itself.
*   **Required Fix:** Move the error term inside the bracket: $\delta N_c = \zeta_{L,f} [1 - I/3 + O(k_L^2/a^2H^2)]$, or explicitly write the amplitude factor as $O(k_L^2/a^2H^2)\zeta_L$.