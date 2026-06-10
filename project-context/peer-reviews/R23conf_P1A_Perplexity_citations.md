# P1A R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.50.pdf` md5=6208734b pages=23
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 35.0s

---

I cannot complete the requested **citation-forensics audit** to the standard you asked for because the only “search results” available here are unrelated metadata/help pages and do not include arXiv/NASA ADS verification for the paper’s references, nor do they provide the external bibliographic evidence needed to check titles, authors, venues, arXiv IDs, or quoted statistics.

What I *can* do from the rendered paper text alone is flag internal problems that do not require web lookup. The paper contains multiple explicit self-admitted limitations and several internal inconsistencies that materially affect its claims, but I cannot honestly certify reference-by-reference correctness against arXiv/ADS from the provided evidence.

**Internal issues visible in the paper text**

- **ESSENTIAL — Scope mismatch in the abstract and title**
  - **Section/Page:** Abstract, p. 1
  - **Problem:** The title and abstract promise “channel-level closure” and a “perturbation transparency theorem,” but the text repeatedly concedes this is *not* an operator-level theorem and excludes explicit operators from the enumeration: “not proven to be a complete diffeomorphism-invariant operator basis,” “explicit closure is left to a follow-up operator-level analysis,” and “the present analysis uses it strictly as an upper-bound EFT ansatz.”
  - **Required fix:** Recast the title/abstract to match the actual scope: a channel-level, assumption-dependent no-go/consistency analysis, not a theorem proving closure of minimal ECH.

- **ESSENTIAL — The central dark-energy mapping is explicitly not derived**
  - **Section/Page:** Abstract; Sec. II A 2; Appendix B, pp. 1, 6, 21–22
  - **Problem:** The paper says the parity-odd operator has off-shell mass dimension \(+1\) and that the mapping to \(\rho_\Lambda\) is a “phenomenological on-shell scaling ansatz, not a derivation.” Appendix B states the same.
  - **Required fix:** Remove all language implying derivation from the ECH action; the paper must present this as a hypothesis or parameterization, not a derivation.

- **ESSENTIAL — Contradictory treatment of Route 4**
  - **Section/Page:** Sec. IV D, Sec. IV E, Sec. XIII, pp. 10–11, 18–20
  - **Problem:** Route 4 is alternately described as “closed by naturalness objection,” then as “not closed by amplitude mismatch,” then as viable if \(\alpha/M\) is floated, then as closed again by explanatory deficit. This is not a stable no-go.
  - **Required fix:** Choose one logically consistent claim: either the route is excluded under a stated fixed coupling assumption, or it is not excluded when couplings are free. The current presentation is internally inconsistent.

- **ESSENTIAL — Internal inconsistency in the \(N_{\text{tot}}\) bookkeeping**
  - **Section/Page:** Abstract; Sec. II C 1; Sec. XII A; Appendix B, pp. 1, 7, 18, 21
  - **Problem:** The paper states \(N_{\text{tot}}\approx 92\) in multiple places, but Appendix B derives \(N_{\text{tot}}\approx 94\) from the genuine \(M_{\rm Pl}^4/\rho_\Lambda\) hierarchy and says the difference is ansatz-dependent. This means the headline number is not stable.
  - **Required fix:** Recompute the mapping consistently, or present the result as a range with explicit dependence on the chosen ansatz. Do not headline a single value as if it were robust.

- **MAJOR — The paper’s own dimensional analysis contradicts the claimed operator interpretation**
  - **Section/Page:** Appendix B, pp. 21–22
  - **Problem:** The operator in Eq. (6) is acknowledged to be dimension \(+1\), and the paper says a controlled local dimension-\(+4\) operator would require inserting “three additional powers of \(M_{\rm Pl}\).” That means the central operator as written is not a valid local EFT operator.
  - **Required fix:** Either rewrite the operator with correct dimensions or explicitly drop any EFT-derived interpretation.

- **MAJOR — Self-contradiction on the perturbation-transparency claim**
  - **Section/Page:** Sec. X, pp. 15–16
  - **Problem:** The paper claims “Holst sector is dynamically inert for both scalar and tensor perturbations at all orders,” but later says the result fails if fermions, propagating torsion, non-minimal couplings, or boundary/topological sectors are included. Since those are physically relevant possibilities, the theorem is only a narrow special case.
  - **Required fix:** State the exact assumptions in the theorem statement itself and remove universal wording.

- **MAJOR — The “four-route closure” is not a complete operator basis**
  - **Section/Page:** Abstract; Sec. IV Scope; Sec. IV E, pp. 1, 8, 11
  - **Problem:** The paper explicitly omits the Jackiw–Pi gravitational Chern–Simons term and a parity-odd four-fermion partner, yet repeatedly uses “closure” language.
  - **Required fix:** Rename the result as a closure of *four enumerated channels*, not of the minimal ECH operator space.

- **MAJOR — The paper repeatedly mixes channel-level and operator-level claims**
  - **Section/Page:** Abstract; Sec. IV, Sec. IX, Sec. XV, pp. 1, 8–11, 20
  - **Problem:** It says “channel-level closure” while also claiming “no-go,” “theorem,” and “operator-basis closure” in adjacent sentences. These are not equivalent.
  - **Required fix:** Use one terminology consistently and define it once.

- **MAJOR — The fNL discussion is not consistently scoped**
  - **Section/Page:** Abstract; Sec. XIII; Sec. XIV D; p. 1, 18–20
  - **Problem:** The paper alternates between presenting \(f_{\rm NL}=-35/8\) as a surviving prediction and admitting it is not ECH-specific, not mechanism-independent, and only valid under Assumption (f) of a companion paper.
  - **Required fix:** Remove it from the abstract as a paper-level prediction unless the paper itself derives it.

- **MAJOR — The birefringence discussion is not consistently scoped**
  - **Section/Page:** Abstract; Sec. XIII; Sec. XIV E, pp. 1, 18–20
  - **Problem:** The paper treats \(\beta\approx 0.27^\circ\) as a benchmark, a consistency check, a test, and a “surviving prediction,” but also states it is not an ECH prediction and is identical in standard GR with the same ALP parameters.
  - **Required fix:** Recast as an external benchmark, not a prediction of the ECH model.

- **MAJOR — Table I and Table IV contain values that are not supported within this paper**
  - **Section/Page:** Tables I and IV, pp. 4, 22
  - **Problem:** These tables list \(H_0=67.68\pm1.06\), \(\Delta N_{\rm eff}\), \(\sigma_8\), \(\Omega_m\), and other posterior quantities that are repeatedly said to live entirely in a companion paper in preparation. The current paper does not provide the chain outputs or diagnostics needed to substantiate them.
  - **Required fix:** Either remove those values or include a self-contained data appendix with full provenance and reproducibility.

- **MAJOR — Table III contains non-evaluated or “not tested” entries but is presented as a discrimination table**
  - **Section/Page:** Table III, p. 16
  - **Problem:** Several cells are “not tested,” “—,” or conditional footnotes. That prevents the table from supporting the strong comparative claims made in the text.
  - **Required fix:** Downgrade the table’s rhetorical role or complete the missing evaluations.

- **MAJOR — The paper’s own citations to “in preparation” works are load-bearing**
  - **Section/Page:** Abstract; Sec. II B; Sec. III; Sec. VII; Sec. XIV; References [2], [6], , , , pp. 1, 3, 8, 12, 19–22
  - **Problem:** Multiple core claims depend on unpublished companion works, which are not independently verifiable from this manuscript.
  - **Required fix:** Either publish those companion results or remove them from load-bearing claims in this paper.

- **MAJOR — Numerical claims are not transparently recomputed in the text**
  - **Section/Page:** Sec. II C, Sec. IV B/C/D, Appendix B, pp. 6–11, 21–22
  - **Problem:** Several quoted orders of magnitude and sigma values are asserted without a full step-by-step derivation in the main paper. Examples include the \(\sim 10^{-58}\) to \(10^{-60}\) ratio, the \(\sim 22\) and \(\sim 36\) order-of-magnitude overshoots, and the “3–5σ” SPHEREx forecast.
  - **Required fix:** Provide explicit arithmetic and parameter propagation in a reproducibility appendix.

- **MINOR — Internal style/terminology instability**
  - **Section/Page:** multiple, especially pp. 1, 8, 15, 20
  - **Problem:** The manuscript alternates between “minimal-ECH,” “minimal Einstein–Cartan–Holst,” “ECH sector,” “Holst-extended Einstein–Cartan,” and “operator-basis closure” without a single consistent taxonomy.
  - **Required fix:** Standardize terminology.

- **MINOR — Footnote and parenthetical overload obscures logical structure**
  - **Section/Page:** Abstract; Sec. IV; Sec. X; Sec. XIV, pp. 1, 8–11, 15–20
  - **Problem:** The argument is buried under dense parentheticals and nested caveats, which makes the logic hard to audit.
  - **Required fix:** Move caveats to a dedicated assumptions section and simplify the mainline argument.

- **MINOR — Table II / Barrier accounting is self-referential**
  - **Section/Page:** Table II, p. 15
  - **Problem:** Barrier 8 and Barrier 14 are explicitly said not to be logically independent, yet the paper repeatedly counts “14 constraints” and “13 logically-independent barriers.” This is confusing, though internally explained.
  - **Required fix:** Use one counting convention everywhere.

- **NIT — Duplicate/near-duplicate phrasing**
  - **Section/Page:** Sec. IV E / Sec. XV, pp. 11, 20
  - **Problem:** Phrases like “channel-level closure” and “amplitude-level closure” recur with nearly identical wording, giving the manuscript a repetitive feel.
  - **Required fix:** Tighten prose.

- **NIT — Some figure captions overclaim relative to body text**
  - **Section/Page:** Figs. 1, 5, 6; pp. 4, 13, 17
  - **Problem:** Several captions imply stronger decisiveness than the body supports, especially where the body repeatedly states “not distinctive ECH prediction” or “not derived from first principles.”
  - **Required fix:** Align caption language with the weaker body claims.

Because I do **not** have the necessary actual web-search evidence for arXiv/NASA ADS verification, I cannot legitimately certify the bibliography entries or identify which cited papers have wrong titles, years, venues, or IDs from the materials provided. If you want, I can still do a second pass limited to the **internal consistency audit** and produce a more formal referee-style report with numbered findings and a recommendation.

## Summary recommendation
**REJECT**

The manuscript’s central claims depend on explicit phenomenological ansätze, unpublished companion papers, and mutually inconsistent scope statements. It repeatedly presents channel-level exclusions as theorem-level closure, while admitting that the key dark-energy mapping is not derived from the ECH action and that the bibliography contains load-bearing in-preparation results. Under PRD standards, this is not yet a publishable physics result; it needs a substantial rewrite, a self-contained derivation or removal of unsupported claims, and full external verification of the cited literature before it can be reconsidered.