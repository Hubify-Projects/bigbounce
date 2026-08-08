# P1A R38conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.70.pdf` md5=4e24501f pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 72.5s

---

**Referee Report for Physical Review D**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Finding P1A-E1 (ESSENTIAL)**  
Section: Title page (image 1), line “Dated: June 13, 2026 PDT — v1A.0.70”  
Problem: A submission date in the future and an internal version string appear in the rendered PDF.  
Required fix: Remove all future dates and version-control strings from the manuscript body and metadata before resubmission.

**Finding P1A-E2 (ESSENTIAL)**  
Section: Abstract (image 1) and throughout (e.g., Sec. IV, IX, X)  
Problem: The central claim of “channel-level closure” of four routes is repeatedly qualified as resting on a “phenomenological on-shell scaling ansatz” (explicitly “not a derivation”) and on 13 “logically-independent mechanism-class constraints” whose justification is distributed across seven unshown “Foundation” studies and six “Branches.” The abstract presents the closure as a completed result.  
Required fix: Either (a) derive the scaling from the ECH action or (b) downgrade the abstract and title to “under stated phenomenological assumptions.”

**Finding P1A-E3 (ESSENTIAL)**  
Section: Multiple locations (e.g., abstract, Sec. I, IV, VI, companion citations [2,6])  
Problem: Load-bearing numerical results (MCMC posteriors, Fisher forecasts, \(\sigma(f_{\rm NL})\approx0.7\), LiteBIRD \(\sigma(\beta)\approx0.03^\circ\)) are imported by citation to “companion work in preparation.” The paper fails the standalone-reader test.  
Required fix: All quantitative claims used to support the closure must be either reproduced or removed.

**Finding P1A-E4 (ESSENTIAL)**  
Section: Abstract (image 1) and Table I (image 4)  
Problem: The abstract states “the surviving testable prediction is the matter-bounce \(f_{\rm NL}=-35/8\)”. Table I footnote c and Sec. XIII state this is a class-level (scalar-only \(w=0\)) result “not a distinctive ECH prediction.” The abstract omits the caveat.  
Required fix: Rewrite the abstract sentence to match the calibrated body statement exactly.

**Finding P1A-M1 (MAJOR)**  
Section: Sec. X (image 19) and abstract  
Problem: The “perturbation-transparency” theorem is proved only for canonical scalar matter; the tensor-sector extension is stated without derivation. The abstract does not qualify the scope.  
Required fix: Either restrict the abstract claim or supply the tensor proof.

**Finding P1A-M2 (MAJOR)**  
Section: Sec. IV D (image 13–14) and abstract  
Problem: Route 4 is closed by a “naturalness/explanatory-deficit objection rather than amplitude mismatch.” No quantitative naturalness measure is supplied; the closure is therefore qualitative.  
Required fix: Provide an explicit, falsifiable naturalness criterion or reclassify the route as “conditionally open.”

**Finding P1A-M3 (MAJOR)**  
Section: Fig. 1 (image 5) and Table II (image 17)  
Problem: Barrier 14 (“Perturbation Transparency”) is listed as an “ECH Gate” that subsumes Barrier 8, yet the figure and text treat them as independent. The logical dependence is not shown.  
Required fix: Supply an explicit dependency diagram or merge the barriers.

**Finding P1A-N1 (MINOR)**  
Section: Throughout (e.g., image 2, page 2)  
Problem: The paper is 28 pages long for a result whose positive content is two class-level predictions already present in the broader bounce literature.  
Required fix: Reduce to \(\leq18\) pages by moving all “Foundation” material to appendices or a separate methods paper.

**Finding P1A-N2 (NIT)**  
Section: Title page and running headers  
Problem: Internal bookkeeping string “v1A.0.70” appears.  
Required fix: Remove.

**Finding P1A-E5 (ESSENTIAL)**  
Section: Data Availability statement (image 25)  
Problem: The GitHub link is given without a frozen commit hash or DOI; the statement refers to “reproducibility” files whose contents are not described.  
Required fix: Supply a permanent archive (Zenodo DOI) with exact commit hash matching the submitted manuscript.

**Finding P1A-M4 (MAJOR)**  
Section: Sec. II C 1 and Eq. (7) (image 7)  
Problem: The one-loop coefficient \(\alpha/M\) is treated as a free phenomenological parameter whose value is fixed by matching to \(\beta_{\rm obs}\). No error propagation from the \(\pm0.094^\circ\) uncertainty is shown.  
Required fix: Provide the propagated uncertainty on \(\alpha/M\).

**Finding P1A-E6 (ESSENTIAL)**  
Section: Abstract and Sec. XIII (image 22)  
Problem: The claim that LiteBIRD will “detect non-zero \(\beta\) at \(\sim9\sigma\)” is computed from the difference \(0.27^\circ-0.03^\circ\) divided by the current central-value uncertainty, not from the projected LiteBIRD uncertainty alone. The calculation is therefore not reproducible from the information given.  
Required fix: Recompute the forecast using only the stated LiteBIRD \(\sigma(\beta)\approx0.03^\circ\) and the model prediction.

**Summary recommendation**  
**REJECT**

The manuscript cannot be considered for publication in its present form. It fails the standalone-reader requirement, presents a future date and internal versioning in the rendered PDF, relies on unshown companion papers for all quantitative support, and contains multiple mismatches between abstract claims and the calibrated statements in the body. Even after removal of the most obvious artifacts, the central “closure” result rests on a phenomenological ansatz rather than a derivation from the ECH action, rendering the title and abstract misleading. A substantially shortened, fully self-contained resubmission that either derives the required scaling or explicitly labels every assumption would be required before further consideration.