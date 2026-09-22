# P1B R-CONFIRM-2026-09-22 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-3.1-pro-preview`
**Input PDF**: `arxiv/paper1b_namaster_proof.pdf` sha256=c7cac6c9f16ca00d6494f6108f0d80c925c074596277cce7e1be6f70d3334a22 pages=16
**Review packet(s)**: `71862867f404998ae3396d00619fd3298a8aea1fc7ef15c2ad3305b8baf8df9a`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 133.8s

---

Here is the referee report for the manuscript submitted to the *Journal of Open Research Software*, evaluated from the perspective of a Physical Review D cosmology-physics referee.

### Referee Report

**General Comments**
The manuscript describes `namaster-proof`, a Python wrapper for NaMaster pseudo-$C_\ell$ computations that generates JSON execution receipts to detect structural shortcuts in data analysis pipelines. While the goal of ensuring computational provenance in cosmological analyses is commendable, the manuscript in its current form is entirely unsuitable for publication. It reads less like a software metapaper and more like an unedited lab notebook or a direct paste of a reviewer response log. The text is saturated with internal audit tags, version-history bookkeeping, and explicit response-to-reviewer status flags. Furthermore, the statistical treatment of the blind tests contradicts the paper's own stated inferential units, and the manuscript is vastly over-scoped for the venue. 

Below is an exhaustive list of findings that must be addressed.

---

### ESSENTIAL (Paper cannot be accepted without these fixes)

**P1B-E1: Internal Audit Tags, Version History, and Review-Log Prose**
*   **Section:** Throughout (Abstract, Sec 6, Sec 11, Page 1)
*   **Problem:** The prompt strictly forbids the inclusion of internal audit tags, version-history language, and review-log prose. This manuscript is infested with them. Examples include:
    *   Page 1: "manuscript revision v2B.0.23(2026-09-05 12:00 PT)"
    *   Abstract & Sec 6: Extensive use of internal rule tags "R1–R6", "R7", "R8".
    *   Page 6: "This is disclosed here as a third post-hoc change..."
    *   Page 7: "...the 24/24 an earlier draft misreported."
    *   Page 8: "Attempt 1 was aborted before unsealing, and is preserved."
    *   Pages 12–13: The entire "L1–L4" list contains literal reviewer-response status tags: "(closed for the estimator; open for the hook)", "(partially closed)", and "(closed)".
*   **Required Fix:** Purge all internal bookkeeping tags, version history, "earlier draft" references, and review-log prose. The L1–L4 list must be rewritten as standard scientific limitations without response-to-reviewer status tags.

**P1B-E2: Inconsistent Statistical Treatment and Abstract Contradiction**
*   **Section:** Abstract and Section 6 (Pages 5 and 6)
*   **Problem:** The abstract explicitly promises: "All detection claims are reported as class-level counts, never as run-level probability intervals." Page 7 reiterates: "the inferential unit is the class, not the run". Accordingly, for Batch 2 (Page 5), the 95% Clopper-Pearson lower bound is correctly computed using $n=4$ classes ($0.05^{1/4} \approx 0.473$). However, for Batch 1 (Page 6), the text quotes a lower bound of 0.779 for 12/12 detections. This value is derived using $n=12$ ($0.05^{1/12} \approx 0.779$), which treats the individual runs as independent. This directly contradicts the abstract's promise, violates the stated inferential unit, and artificially inflates the confidence bound for the pilot batch.
*   **Required Fix:** Recompute the Batch 1 lower bound using the correct class-level $n$. If sigma/probability values from different null procedures (run-level vs. class-level) appear side-by-side, they must carry an explicit "not directly comparable" qualification at every juxtaposition. Ensure the abstract's claim matches the body's execution.

**P1B-E3: Scope and Length Mismatch**
*   **Section:** General
*   **Problem:** The manuscript is 16 pages long. For a JORS software metapaper claiming a narrow contribution (a Python wrapper for NaMaster JSON receipts), this is excessively long. The detailed, diary-like narrative of the 4-batch cryptographic blind test (Pages 4–10) is out of scope for a software description and obscures the actual utility of the package.
*   **Required Fix:** Drastically condense the manuscript. The recommended maximum page count for the core software architecture and usage is 6–8 pages. The blind test narrative must be summarized into a single short section of results. The cryptographic timestamping and aborted-attempt diaries should be moved to an appendix or a separate methods paper.

---

### MAJOR (Significant revision required)

**P1B-M1: Contradictory Batch Counts**
*   **Section:** 6 (Page 4)
*   **Problem:** The text states "Protocol, two batches." but the subsequent subsections explicitly detail Batch 1, Batch 2, Batch 3, and Batch 4.
*   **Required Fix:** Correct the text to accurately reflect the four batches described in the protocol.

**P1B-M2: Uncomputed Quantitative Claims**
*   **Section:** 6 (Page 6) and 12 (Page 13)
*   **Problem:** The paper makes quantitative assertions without providing the computed numbers or artifact pointers. 
    *   Page 13 claims "heap use is dominated by NumPy allocation overhead... no formal memory profiling was performed." This is a qualitative confidence claim where a number is checkable.
    *   Page 6 claims "the shortcut arms ran 3–15x faster than honest ones" without citing the specific benchmark artifact.
*   **Required Fix:** Remove the memory claim if no formal profiling was performed, or perform the profile and quote the numbers. Provide the exact artifact pointer/script that generated the 3–15x speedup metric.

**P1B-M3: Missing Effect Size for Cosmological Bias**
*   **Section:** 2 (Page 2)
*   **Problem:** The text claims the effective-multipole shortcut produces "order-unity fractional deviations... large enough to bias a fit." In a cosmology context, a fractional deviation in a bandpower is only meaningful if translated into an effect size on a physical parameter.
*   **Required Fix:** Quantify the bias. State the expected shift in a relevant cosmological parameter (e.g., $\Delta r$ or $\Delta \beta$) caused by this shortcut, or explicitly bound the practical significance of the "order-unity" deviation.

---

### MINOR (Address but paper can proceed)

**P1B-N1: Implicit Parity Assumptions**
*   **Section:** 4 (Page 3)
*   **Problem:** Equations 1–3 assume an "initially vanishing EB spectrum". For a generic spin-2 field, EB and BE need not vanish. The equations implicitly assume standard parity-even CMB cosmology.
*   **Required Fix:** Add a brief explicit caveat that these equations assume a parity-even unrotated sky ($C_\ell^{EB} = C_\ell^{BE} = 0$).

**P1B-N2: Undefined Residual Metric**
*   **Section:** 6 (Page 7)
*   **Problem:** The text quotes "honest relative residuals $8.4 \times 10^{-13}$–$1.4 \times 10^{-12}$", but the exact dimensionless quantity being quoted is not mathematically defined. The rule is defined as $|\sum M C - p| > 10^{-6} \|p\|_2$, but it is unclear if the quoted residual is the LHS divided by $\|p\|_2$ or something else.
*   **Required Fix:** Explicitly define the mathematical form of the "relative residual" being quoted to ensure the argument is self-contained.

---

### NIT (Cosmetic)

**P1B-N3: Informal Bash-Brace Syntax**
*   **Section:** 12 (Page 14)
*   **Problem:** The text uses bash-brace expansion syntax `sealed{,2,3,4}/key.txt` in the main prose.
*   **Required Fix:** Write out the paths or describe them in standard English (e.g., "the `key.txt` files in the respective `sealed` directories").

---

## Summary recommendation
REJECT

**Justification:**
The manuscript in its current state is fundamentally incompatible with journal publication standards. It contains literal reviewer-response logs (e.g., "closed for the estimator; open for the hook"), internal audit tags, and diary-like entries regarding aborted drafts, which explicitly violate the venue's formatting and professional requirements. Furthermore, the statistical treatment of the blind tests is internally inconsistent, contradicting the paper's own stated inferential units to artificially inflate confidence bounds in the pilot batch. Finally, the manuscript is vastly over-scoped, spending the majority of its 16 pages on a cryptographic audit narrative rather than the software itself. The paper requires a complete rewrite to remove the internal bookkeeping, correct the statistical claims, and condense the text to a length appropriate for a software metapaper.