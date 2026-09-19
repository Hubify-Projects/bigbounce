# PSU R4COMPLETE — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `arxiv/paper_su_criterion/main.pdf` sha256=0fc47bd5f7c49d5c67bead2627ea2628c19b15e8687098d5a5b927c416291563 pages=7
**Review packet(s)**: `6f8963deeb794c48cd081079729ebaea462c87174fd90f34c37b3aa885546150, 847588c450c0f4220b7dc383112c36b3c055f23485417d9d3b9d48ca0d9a3647`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2428 chars)
**Wall time**: 333.4s

---

This is a referee report for "The separate universe computes a different variable: an exact criterion for $\delta N = \zeta$ in non-attractor phases" by Houston Golden, submitted to Physical Review D.

## General Comments
The manuscript presents a highly rigorous and physically insightful clarification of the separate universe ($\delta N$) formalism's applicability in non-attractor cosmological phases. By deriving an exact linear-order threading map and extending it to second order, the author elegantly resolves a known tension in the literature regarding the squeezed-limit bispectrum in matter-dominated contractions and ultra-slow-roll (USR) inflation. The cosmological physics, including the precise distinction between the dominant/decaying $\zeta$ modes and their corresponding Bardeen potentials in ekpyrotic and matter-contracting phases, is exceptionally solid. 

However, the manuscript currently violates several core PRD editorial policies regarding self-containment and data provenance. The paper relies on unpublished GitHub markdown files for load-bearing derivations—most notably, the from-scratch in-in bispectrum shape that forms the basis of the central discrepancy claim, and a factor-of-2 correction to a previously published PRD paper. These must be rectified before acceptance.

## Findings

**ESSENTIAL**
1. **ID: PSU-E1**
   * **Section + Page:** Section I (page 1), Appendix A4 (page 7), and Bibliography (page 5).
   * **Specific Problem:** The manuscript violates the STANDALONE-READER TEST. The core physical discrepancy motivating the paper ($-5$ vs $-15/8$) relies on the from-scratch in-in squeezed bispectrum shape, which is imported directly from an unpublished GitHub markdown file (Ref [23]). Furthermore, Section I uses this same GitHub note to assert a factor-of-2 error in a published PRD paper (Cai et al. [20]): "[23] locates this unprinted factor of 2 downstream of Eq. (37)...". PRD policy strictly prohibits using unpublished, non-peer-reviewed web links as load-bearing evidence for physical derivations or for correcting published literature.
   * **Required Fix:** The author must make the paper self-contained. The derivation of the in-in shape and the explicit proof of the factor-of-2 correction to Cai et al. must be included in the manuscript (e.g., in the Appendix) or cited to a permanent, peer-reviewed publication / arXiv preprint. 

2. **ID: PSU-E2**
   * **Section + Page:** Reproducibility Statement (page 4).
   * **Specific Problem:** The provenance surface relies on local file paths (e.g., `research/theory_audit/...`) and GitHub commit hashes (e.g., `SHA-256 21668ab6...`) without a persistent DOI. The text "Local CPU, $0, under 35 seconds total" reads like an internal log rather than a formal data availability statement.
   * **Required Fix:** Upload the exact scripts and JSON manifests used to generate the paper's results to a permanent, immutable repository (such as Zenodo or the arXiv source files) and cite the corresponding DOI.

**MAJOR**
3. **ID: PSU-M1**
   * **Section + Page:** Table I (page 4) and Section V (page 4).
   * **Specific Problem:** Uncomputed quantitative claims. Table I lists exact values ($5/2$) for $f^{in-in}$ and $f_{\delta N}^{init}$ in the USR row, and states the result is "agree to that order". However, the row itself explicitly notes "(not computed here)", and Section V admits "a full time-dependent-$\epsilon$ second-order calculation was not attempted." Presenting exact numerical matches in a validation table for a calculation that was not actually performed is misleading.
   * **Required Fix:** Either perform the full time-dependent-$\epsilon$ calculation to rigorously justify the $5/2$ entries, or modify the table to clearly reflect that these entries are leading-order structural inferences (e.g., writing $\approx 5/2$) and add a footnote clarifying their epistemological status.

4. **ID: PSU-M2**
   * **Section + Page:** Entire manuscript.
   * **Specific Problem:** The manuscript is 7 pages long, which exceeds the standard ~4.5-page (4500 words) limit for PRD Letters / Short Notes. 
   * **Required Fix:** Restructure the paper to fit the Letter limit (e.g., by moving the extensive Appendix A to a separate Supplemental Material document) or contact the editors to change the submission type to a regular PRD article.

**MINOR**
5. **ID: PSU-N1**
   * **Section + Page:** Page 1, top right corner.
   * **Specific Problem:** The text includes an internal version-history tag: "v1S.0.11".
   * **Required Fix:** Remove this internal bookkeeping placeholder prior to publication.

## Summary recommendation
MAJOR REVISIONS

The theoretical physics and mathematical derivations in this manuscript are outstanding and resolve an important ambiguity in cosmological perturbation theory. However, the reliance on unpublished GitHub markdown files for the core in-in bispectrum derivation and for correcting a published PRD paper is a critical violation of journal standards. Once the author incorporates these load-bearing proofs directly into the manuscript (or a Supplemental Material document) and formalizes the reproducibility statement with a persistent DOI, the paper will be an excellent addition to Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a fresh-eyes review of the manuscript, focusing on internal consistency, cross-references, and figure-text alignment. 

**MINOR**

1. **ID: PSU-m1**
   * **Section + Page:** Figure 1 and Caption (page 3).
   * **Specific Problem:** FIGURE-CAPTION VS PLOT MISMATCH. The legend indicates two distinct lines: a black line for $\lambda(w)$ and a red line for $f_{map}^{mono}(w)$. However, due to the specific scaling chosen for the left and right y-axes, the two curves map to the exact same physical coordinates on the page (e.g., at $w=-1$, $\lambda=1.0$ is at the top of the left axis, and $f_{map}^{mono}=0.0$ is at the top of the right axis). Consequently, they perfectly overlap, and only one line is visible. 
   * **Required Fix:** Add a brief note to the Figure 1 caption explicitly stating that the dual-axis scaling causes the two curves to perfectly overlap, preventing reader confusion over a "missing" second line.

2. **ID: PSU-N2**
   * **Section + Page:** Section II (page 2) and Section II (page 3).
   * **Specific Problem:** INTERNAL CROSS-REFERENCE ERROR. The manuscript cites "(App. A2)" in three separate places to support claims about the initial-position map's monopole and its $n_s$-dependence (e.g., "equals the initial-position monopole only at $n_s=1$, App. A2" and "its kernel carries no $1/k_L$ pole (App. A2)"). However, Appendix A.2 only lists the $n_s=1$ totals. The general-$n_s$ translation term, the explicit formula for the initial-position monopole $\frac{5\epsilon(2\epsilon-7+n_s)}{12(3-\epsilon)}$, and the discussion of the $1/k_L$ pole are actually located in **Appendix A.3**.
   * **Required Fix:** Change the three "(App. A2)" cross-references on pages 2 and 3 to "(App. A3)".

3. **ID: PSU-N3**
   * **Section + Page:** Title/Author block (page 1) and Reproducibility Statement (page 4).
   * **Specific Problem:** STALE METADATA / DATE. The manuscript is dated "September 19, 2026", and the reproducibility statement references file names with the same 2026 date (e.g., `..._2026_09_04.py`). While this may be a deliberate placeholder or anonymization choice by the author, it is anomalous for a current submission and will need to be corrected to the actual date of submission/publication for the final version of record.
   * **Required Fix:** Update the manuscript date and file names to reflect the correct current year prior to publication.