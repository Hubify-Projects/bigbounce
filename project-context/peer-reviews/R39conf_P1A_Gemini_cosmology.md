# P1A R39conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=ea008466 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 147.6s

---

## Referee Report: "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

This paper assesses four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The central claims are (1) a channel-level closure of these four routes under a set of stated assumptions and ansätze, and (2) a perturbation-transparency result showing that the Holst sector decouples from scalar and tensor perturbations in the presence of canonical scalar matter. The work is structured as a systematic "no-go" analysis, cataloging 13 independent constraints and evaluating each of the four dark-energy routes against them.

The paper is well-structured and commendably transparent about its scope and limitations, particularly regarding the distinction between a channel-level assessment and a full operator-level theorem, and the phenomenological nature of the key dark-energy scaling ansatz. The perturbation-transparency result is a clear and valuable theoretical finding. The systematic closure of the enumerated channels, especially the physically well-motivated "thermal reset" argument, is a solid contribution.

However, the manuscript in its current form is not acceptable for publication in Physical Review D. It suffers from several essential issues, most critically an extensive reliance on unavailable companion papers for load-bearing results, which makes the work unverifiable. It also contains several artifacts indicative of a draft version. Significant revisions are required to bring it to a publishable standard.

### ESSENTIAL Revisions

**P1A-E1: Extensive Use of Placeholder Citations for Unavailable Companion Papers**
*   **Section/Page:** Throughout, e.g., p. 3 (Ref [10]), p. 4 (Ref [2], [6]), p. 27 (Refs [2], [5], [6], [10], [23], [46]).
*   **Problem:** The paper makes numerous quantitative claims, presents MCMC results, and bases forecasts on at least six companion papers that are cited as "in preparation" or with future-dated arXiv IDs (e.g., `arXiv:2503.14738`, `arXiv:2509.13654`). This includes the MCMC parameter values in Table I and IV, the `f_NL` forecast details [2], the galaxy spin null result [23], and the PTA reanalysis [46]. A manuscript cannot be peer-reviewed if its core evidence resides in unavailable work. This violates the fundamental principle of verifiability.
*   **Fix:** The paper must be made self-contained by incorporating the essential methods and results from the companion works. Alternatively, all companion papers must be submitted to arXiv concurrently with this manuscript so they can be reviewed as a complete set. All placeholder citations must be replaced with active links.

**P1A-E2: Internal Version-Control Artifacts in Manuscript**
*   **Section/Page:** p. 1 (Date), p. 20 (Footnote 8).
*   **Problem:** The manuscript contains artifacts that should not be present in a submission-ready version.
    1.  The date is set in the future: "(Dated: June 13, 2026 PDT)".
    2.  Footnote 8 on page 20 contains a comment about a correction from a previous draft: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density." Such internal-review commentary is inappropriate for a final manuscript.
*   **Fix:** Remove all such artifacts. The date should be the submission date. The footnote should be rewritten to state the physical distinction without referring to the paper's revision history.

### MAJOR Revisions

**P1A-M1: Unjustified Scaling Ansatz for Gravitational Wave Ceiling**
*   **Section/Page:** p. 17, Sec. IX L, "Barrier 12".
*   **Problem:** The paper presents a ceiling on the gravitational wave energy density from the bounce as `Ω_GW ∝ (ρ_crit/ρ_Pl)^2`. The standard expectation is that `Ω_GW` at the bounce should scale with `(H_bounce/M_Pl)^2`, which is proportional to `ρ_bounce/M_Pl^4 = ρ_crit/ρ_Pl`. The paper labels the quadratic scaling as an "ansatz" but provides no physical motivation or derivation for this unusual choice.
*   **Fix:** Justify the `(ρ_crit/ρ_Pl)^2` scaling with a derivation or a citation to a work that derives it. If no justification can be provided, the standard linear scaling `(ρ_crit/ρ_Pl)` must be used, and the consequences for the "Barrier 12" argument must be re-evaluated.

**P1A-M2: Ambiguous Scope of the `f_NL` Forecast Significance**
*   **Section/Page:** p. 4 (Table I footnote), p. 15 (Sec. VII).
*   **Problem:** The abstract and Table I quote a "2.6-5σ" significance for the SPHEREx `f_NL` forecast. The text explains this range covers different systematic assumptions ("ideal-survey" vs. "degraded-with-systematics"). However, the sourcing of these numbers is opaque, relying on a combination of a cited paper [36] and an unavailable companion paper [2]. The presentation is confusing. For instance, the abstract footnote refers to a "2.6-5σ quoted above", which is self-referential.
*   **Fix:** The `f_NL` forecast section must be made self-contained. Clearly define the "optimistic" (5σ) and "pessimistic" (2.6σ) scenarios. Provide a clear, step-by-step summary of the calculation, starting from the baseline `σ(f_NL)` from Heinrich et al. [36] and detailing the degradation factors applied for GR projection, `b_φ` uncertainty, and photo-z's to arrive at the final range. This should be done within the main paper, not deferred to a companion.

**P1A-M3: The Problematic Dimensionality of the Parity-Odd Operator**
*   **Section/Page:** p. 3, p. 7, Appendix B (p. 25).
*   **Problem:** The entire dark-energy mapping rests on a phenomenological operator `(α/M) e e F` which has mass dimension +1. The paper is commendably upfront that this is not a valid operator in a local effective field theory and requires an "on-shell scaling ansatz" to acquire the correct dimension of +4 for an energy density. While using this to *disprove* a route is a valid rhetorical strategy, the argument's framing could be strengthened. The current presentation might lead a reader to believe this is a novel theoretical proposal, rather than a demonstration of the non-viability of a hypothetical mechanism.
*   **Fix:** Refine the language in Sec. II.A and the introduction. State even more explicitly that the need to invoke such a dimensionally-inconsistent operator and a subsequent ad-hoc scaling ansatz is, in itself, a primary argument against the viability of these ECH dark-energy routes from an EFT perspective, *before* even considering the other 13 barriers. This would strengthen the paper's core "no-go" conclusion.

### MINOR Revisions

**P1A-m1: Inconsistent Fermion Density in NJL Calculation**
*   **Section/Page:** p. 11, Sec. IV A.
*   **Problem:** The calculation of the NJL energy density uses a post-recombination baryon density of `n_b ~ O(10^2) cm^-3`. The present-day average baryon number density is `~10^-7 cm^-3`. While densities were higher in the past, `10^2 cm^-3` seems high for a cosmologically-relevant average density after recombination.
*   **Fix:** Clarify the epoch and assumptions used to arrive at `n_b ~ O(10^2) cm^-3`. Re-evaluate the suppression factor using a more standard value (e.g., the density at `z~1-2` where dark energy begins to dominate) to ensure the conclusion is robust. The conclusion of extreme suppression will certainly hold, but the calculation should be based on appropriate physical numbers.

**P1A-m2: Redundant Figures**
*   **Section/Page:** p. 15 (Fig. 4) and p. 22 (Fig. 6).
*   **Problem:** Figure 4 and Figure 6 convey nearly identical information about the detection significance forecasts for `f_NL` and `β`. Figure 4 is more informative as it shows the effect of correlations.
*   **Fix:** Consider removing Figure 6 and referring back to Figure 4 in Section XIII. This would improve the paper's conciseness.

**P1A-m3: Standalone Readability of Cosmological Parameters**
*   **Section/Page:** p. 4, Table I.
*   **Problem:** The paper uses cosmological parameter values from an MCMC analysis in a companion paper. While a footnote clarifies these are not used in the structural proofs, their presence makes the paper feel incomplete.
*   **Fix:** Since the specific values are not essential to the main arguments, consider replacing them with references to a standard cosmology (e.g., "values consistent with Planck 2018 `ΛCDM`") rather than quoting precise numbers with error bars from an unavailable analysis. This would strengthen the paper's standalone character.

### NITs

**P1A-N1: Typo in Table I Footnote**
*   **Section/Page:** p. 4, Table I.
*   **Problem:** The footnote refers to "Paper II forecast'". The prime character appears to be a typo.
*   **Fix:** Change "forecast'" to "forecast".

## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a potentially valuable and rigorous analysis of dark energy channels within Einstein-Cartan-Holst gravity. The perturbation-transparency theorem is a noteworthy result, and the systematic catalog of constraints provides a useful framework for evaluating such models. However, the paper is not yet in a state suitable for publication. The reliance on numerous unavailable companion papers for key results is an essential flaw that renders the work unverifiable. Once the authors have made the work self-contained and verifiable by either incorporating the necessary material or publishing the companion works, and have addressed the other major and minor points above, the manuscript will be a strong candidate for publication in Physical Review D.