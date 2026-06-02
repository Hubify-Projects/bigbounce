# P4 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 64.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=99701, completion=849, total=107198

---

No blocker-grade findings. The paper is exceptionally thorough. The following are major and minor issues for revision.

## PAPER-GEM-B1: Factual Error on Comparison Sample Size

*   **Classification:** BLOCKER
*   **Location:** Section 1 (Introduction) and Section 5.1 (Comparison with Shamir)
*   **Issue:** The paper repeatedly states the Shamir (2022) DESI analysis used "~200,000" spiral galaxies. The abstract of the cited paper (Shamir 2022, MNRAS 516, 2281) explicitly states, "The data include nearly 1.3 × 10^6 spiral galaxies." This is a direct factual contradiction that misrepresents the primary prior work being challenged.
*   **Fix:** Correct the description of the Shamir (2022) sample size to 1.3 million spirals throughout the manuscript. Adjust the narrative regarding the sample-size increase accordingly (the ratio is ~2.5x, not ~16x).

## PAPER-GEM-M1: Buried Load-Bearing Analysis

*   **Classification:** MAJOR
*   **Pattern:** 020 (load-bearing buried)
*   **Location:** Section 4.4, Table VI, footnote b
*   **Issue:** The joint nuisance-marginalized fit that provides the formal exclusion of a primordial-dipole interpretation for the canonical-mask residual is buried in a footnote. This analysis is the quantitative linchpin of the systematics argument and is too important for a footnote.
*   **Fix:** Elevate the joint nuisance-marginalized fit analysis into a dedicated subsection in the main text. This gives proper prominence to the analysis that formally closes the paper's most complex systematic.

## PAPER-GEM-M2: Title Obscures Primary Finding

*   **Classification:** MAJOR
*   **Pattern:** 019 (title-vs-body)
*   **Location:** Title
*   **Issue:** The title is excessively long and structured like a summary, listing multiple sigma values and diagnostic findings. This dilutes the impact of the main null result and reads like an abstract.
*   **Fix:** Shorten the title to focus on the primary scientific result. Suggestion: "A Null Search for a Galaxy Chirality Dipole on 3.2 Million DESI Legacy Spirals and the Systematics of Apparent Signals".

## PAPER-GEM-m3: Imprecise Framing of Parity Test

*   **Classification:** minor
*   **Focus:** Theoretical Physics (gauge-frame vs physical-frame distinctions)
*   **Location:** Abstract, Introduction
*   **Issue:** The abstract and introduction repeatedly frame the dipole analysis as a "parity-violation test" before the excellent discussion in Section 5.8 clarifies it is a parity-EVEN, isotropy-breaking test. This initial framing is imprecise.
*   **Fix:** From the outset, frame the $\ell=1$ dipole as a test for a "cosmological preferred axis" or "isotropy-breaking axial-vector," noting it is a parity-even observable. This aligns the summary framing with the precise theoretical discussion later in the paper.

## PAPER-GEM-m4: Incomplete Estimator Summary

*   **Classification:** minor
*   **Pattern:** 029 (estimator multiplicity without preregistration)
*   **Location:** Section 4.10 (Conclusions), Table IX
*   **Issue:** The summary table of $\ell=1$ estimators (Table IX) is incomplete. It omits the $+0.43\sigma$ real-space dipole, which is declared a "primary cosmological estimator" in the declared analysis hierarchy (Sec 3.1).
*   **Fix:** Add the real-space dipole estimator to Table IX to provide a single, complete summary of all key $\ell=1$ results. This will help the reader reconcile the multiple estimators used.
