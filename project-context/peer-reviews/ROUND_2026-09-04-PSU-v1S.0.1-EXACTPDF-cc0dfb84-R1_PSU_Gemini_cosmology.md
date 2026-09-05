# PSU ROUND_2026-09-04-PSU-v1S.0.1-EXACTPDF-cc0dfb84-R1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `arxiv/paper_su_criterion/main.pdf` sha256=cc0dfb84a232967c45ea359d5de18f642af0727c2907512b289931854ed7c48e pages=4
**Review packet(s)**: `f8ac5af68de248a7c485cde2795af5205ed5e0633083f38b5b7ca27d2f855ab1, 4ff6c76420471f864b8f4a5525550a575d961a255049430a584fabbca82ef877`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (1047 chars)
**Wall time**: 357.3s

---

This is a referee report for "When the separate universe fails: a criterion for the squeezed bispectrum in non-attractor phases" submitted to Physical Review D (Letter/Short Note).

The paper investigates the validity of the separate universe ($\delta N$) formalism in non-attractor cosmological phases, proposing a single criterion based on the $\zeta$-growth-weighted mean of $\epsilon/c_s^2$. The author derives an exact threading identity and a second-order map, showing that while $\delta N$ works for ultra-slow-roll (USR) inflation, it fails at $\mathcal{O}(1)$ for a matter-dominated contraction. 

The physical insight is sharp, and the identification of a second, independent failure mode for the separate universe formalism is a valuable contribution to the literature. However, the manuscript contains a critical algebraic error in the main text's presentation of the second-order map, and it violates the standalone-reader requirement by relying on non-archival GitHub links for load-bearing derivations. These issues must be addressed before the paper can be accepted.

### Findings

**1. Algebraic inconsistency in the second-order map (ESSENTIAL)**
*Section II, Page 2*
**Problem:** The text states: "solving the exact ADM constraints to $\mathcal{O}(\zeta_L \zeta_S)$ and integrating Eq. (1) gives $f_{\delta N} = f_{\text{in-in}}/\lambda + f_{\text{map}}$". This equation is algebraically inconsistent with the values provided in Table I and Eq. (3). 
Using the dust case ($w=0, \lambda=1/2$), Table I gives $f_{\delta N} = -5$ and $f_{\text{in-in}} = -35/16 + \frac{15}{16}\mu^2$. Eq. (3) gives $f_{\text{map}} = -\frac{15}{8}(1-\mu^2)$. Substituting these into the stated equation yields:
$-5 = 2(-35/16 + 15/16 \mu^2) - 15/8(1-\mu^2)$
$-5 = -50/8 + 30/8 \mu^2$
This fails to cancel the $\mu^2$ angle dependence and gives the wrong monopole. The correct relation, derived from your own numbers, is $f_{\text{in-in}} = \lambda^2 f_{\delta N} + \lambda f_{\text{map}}$. 
**Required fix:** Correct the equation to $f_{\text{in-in}} = \lambda^2 f_{\delta N} + \lambda f_{\text{map}}$ (or its algebraic equivalent for $f_{\delta N}$) and ensure all text references to this mapping are consistent.

**2. Standalone reader test failure / Non-archival citations (ESSENTIAL)**
*References, Page 4*
**Problem:** References [18] and [19] are GitHub links to `.md` files. The paper relies heavily on these citations for load-bearing results (the from-scratch in-in squeezed bispectrum and the exact second-order map). This violates the standalone reader test, as these are not peer-reviewed archival publications or permanent preprints.
**Required fix:** The derivations for the in-in bispectrum and the second-order map must be included in an appendix, or the citations must be updated to point to archival preprints (e.g., arXiv) that are publicly available and permanent.

**3. Table I header contradiction (MAJOR)**
*Section III, Page 3, Table I*
**Problem:** The header of Table I states "$f_{\text{in-in}}$ the in-in monopole". However, the entry for the dust case is $-35/16 + \frac{15}{16}\mu^2$, which explicitly contains the angle dependence $\mu^2$ and is therefore not the monopole. The actual monopole is $-15/8$.
**Required fix:** Either change the column header to indicate it is the full angle-dependent $f_{\text{in-in}}$, or change the dust entry to the actual monopole value ($-15/8$).

**4. Internal audit tags in the main text (MAJOR)**
*Section III, Page 2 and Reproducibility Statement, Page 3*
**Problem:** The text contains internal audit tags and script names that should not appear in a published paper. Specifically:
- Page 2, column 2: "(script: separate_universe_failure_criterion_2026_09_04.py, exact sympy)"
- Page 3, column 2: "Manifest: reproducibility/manifests/experiments/lift2-separate-universe-failure-criterion.json"
**Required fix:** Remove these internal bookkeeping placeholders from the main text.

## Summary recommendation
MAJOR REVISIONS

The core theoretical result—the $\langle \epsilon/c_s^2 \rangle_\zeta$ criterion and the exact threading identity—is physically sound and well-motivated. The abstract accurately reflects the findings, and the quantitative claims (such as the 8/3 failure factor) are correct. However, the algebraic typo in the second-order map equation is a critical error that contradicts the paper's own data, and the reliance on GitHub markdown files for central derivations is unacceptable for a PRD Letter. Once the algebra is corrected and the derivations are properly archived (either via an appendix or an arXiv preprint), the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a fresh-eyes review of the manuscript, following the requested categories:

**[PSU-B1] Figure-Caption vs Body-Claim (MAJOR)**
*Figure 1 and Caption, Page 2*
**Problem:** The caption for Figure 1 states: "The linear rescaling $\lambda(w) = (1-w)/2$ and the second-order map monopole $f_{\text{map}}^{\text{mono}}(w) = -\frac{5}{4}(1+w)$... **Both vanish at $w=-1$** (attractor limit)". 
This is mathematically incorrect and contradicts the figure itself. Using the provided formula, $\lambda(-1) = (1 - (-1))/2 = 1$. Furthermore, the blue line for $\lambda(w)$ in Figure 1 clearly intersects the left axis at $1.0$ when $w=-1$. Only the second-order correction $f_{\text{map}}^{\text{mono}}$ vanishes at $w=-1$. For $\lambda$, it is the *discrepancy from the identity map* ($\lambda - 1$) that vanishes, not $\lambda$ itself.
**Required fix:** Correct the caption to accurately reflect the plot and formulas (e.g., "At $w=-1$ (attractor limit), $f_{\text{map}}^{\text{mono}}$ vanishes and $\lambda \to 1$...").