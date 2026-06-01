# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-direct-P2
**Wall time**: 29.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33388, completion=2448, total=35836, search_context_size=low, cost={'input_tokens_cost': 0.10016, 'output_tokens_cost': 0.03672, 'request_cost': 0.006, 'total_cost': 0.14288}

---

## PAPER-PER-B1 – Mis-citation and overstated SPHEREx 3–5σ claim from Heinrich et al.

**Classification:** BLOCKER  

**Location:** Abstract, lines around “$\sigma(\fnl^{\rm local}) \approx 0.7$ (Heinrich et al. 2024 [Heinrich:2023], Fig. 6 / Table 3, multi-tracer galaxy bispectrum forecast...) giving template‑corrected significance ~3–5σ after the combined systematic budget ... with 5.2–5.5σ as the optimistic case…” and again in Sec. \ref{sec:spherex}.  

**Issue:**  
The paper claims Heinrich et al. “multi‑tracer galaxy bispectrum” forecast a **bispectrum-only** SPHEREx constraint of **σ(fNL) ≈ 0.7**, from which a **5.2–5.5σ** optimistic detection and **3–5σ** post‑systematic range for the bounce are derived. That exact combination (“Heinrich:2023” SPHEREx, σ ≈ 0.7 from bispectrum alone, multi-tracer Fisher with that normalization) cannot be confirmed in the current literature; the cited work is not verifiable as “Heinrich et al. 2024, Fig. 6 / Table 3” with those numbers and that precise channel. The author’s detection significance chain (0.7 → 6.25σ → r → 5.2–5.5σ → ‘3–5σ after systematics’) is presented as grounded in that specific external forecast, but the existence and details of the cited Heinrich paper in that form remain unverified and thus the core 3–5σ claim is not currently backed by a demonstrable reference.  

**Fix (1–2 sentences):**  
Downgrade the SPHEREx sensitivity to an explicitly *assumed* σ(fNL) baseline (clearly labeled as a theoretical target, not a published Heinrich et al. measurement), or replace it with a verified published forecast (DESI, Euclid, or an actually locatable SPHEREx forecast), and re‑propagate all quoted 5.2–5.5σ / 3–5σ numbers accordingly. Explicitly state that the 3–5σ forecast hinges on an internal Fisher calculation (to be released) rather than on Heinrich et al. 2024 if a suitable external reference cannot be produced.


## PAPER-PER-B2 – Heinrich–Fisher “invariance” assumption left as unvalidated

**Classification:** BLOCKER  

**Location:** Sec. \ref{sec:spherex}, paragraph “The Heinrich et al. Fisher forecast is constructed at the local-template fiducial fNL = 0; applying the resulting σ(fNL)≈0.7 at the bounce-fiducial fNL = −4.375 relies on the leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts… A re-derivation … at the bounce-fiducial is a structural extension on the post-arXiv TODO; the present significance forecasts adopt the leading-order assumption.”  

**Issue:**  
The central 3–5σ claim assumes **Heinrich’s multi-tracer Fisher matrix is unchanged** when moved from fiducial fNL=0 to fNL=−4.375, i.e., that the Fisher curvature and covariance are effectively invariant over a ~6σ excursion. This is a nontrivial assumption for a multi-tracer bispectrum Fisher including SDB-like 1/k² behavior and PNG–bias couplings; it is explicitly marked as a TODO (“re-derivation … is deferred”), but the paper still uses the resulting σ(fNL) as if it were robust. Given that all bounce significance numbers depend on this untested invariance—no recomputed Fisher at the bounce point is provided—this is an unresolved theoretical gap underlying the main result.  

**Fix (1–2 sentences):**  
Either (a) perform and include an explicit recomputation of the multi-tracer Fisher matrix at fiducial fNL = −4.375 and update all σ(fNL) and significance figures, or (b) clearly reframe the 3–5σ SPHEREx numbers as *illustrative extrapolations* contingent on an unverified Fisher invariance assumption, downgrading them from headline claims.


## PAPER-PER-M1 – CFC physical-frame “fNL → 0” statement not matched to precise literature claims

**Classification:** MAJOR  

**Location:** Abstract (first paragraph, CFC consistency-relation discussion) and Introduction, first paragraph referring to Pajer–Tanaka–Urakawa.  

**Issue:**  
The paper states that in the conformal-Fermi “physical-observer” frame *single-field slow-roll inflation predicts fNL^local → 0 at leading order in the squeezed limit*, and uses this as a key theoretical discriminator. The Pajer–Tanaka–Urakawa works indeed show removal of projection / gauge artefacts and suppression of the consistency-relation contribution, but they do **not** phrase the result as “predicts fNL^local → 0” in the same observational-estimator sense used here; there are residual slow-roll–suppressed contributions and subtleties in defining the observable bispectrum in CFC. The manuscript blurs this nuance and elevates a technical result about coordinate/gauge artifacts to a blanket “inflation predicts zero” in the physical frame, which overshoots the wording and scope of the cited papers.  

**Fix (1–2 sentences):**  
Rephrase the CFC discussion to align with the literature, e.g. “Pajer, Tanaka & Urakawa show that in conformal-Fermi coordinates the leading squeezed-limit contribution in single-field slow-roll is removed as a projection effect, leaving only slow-roll–suppressed residuals, so the observable CFC-frame signal is parametrically smaller than the usual Maldacena gauge-frame value,” and stop short of claiming an exact fNL→0 prediction.


## PAPER-PER-M2 – Matter-bounce bispectrum / coefficients: Cai et al. 2009 does not support specific SVD/null-space construction

**Classification:** MAJOR  

**Location:** Sec. \ref{sec:benchmark}, discussion of polynomial P(k1,k2,k3), the coefficient vectors (2,7,3,−12,−69,19) and (6,2,−18,10,−132,18), the 3×6 constraint matrix, SVD spectrum, and 10,000-sample null-space scan.  

**Issue:**  
Cai et al. 2009 do give a bispectrum shape, benchmark values, and coefficients in one explicit basis, but they **do not** define the six-monomial basis, the alternative coefficient set (2,7,3,−12,−69,19), or the SVD / null-space construction described here. Those are new internal choices. Yet the footnote “the coefficients printed in Eq. (37)… are the single-time-ordering values… after doubling, these give (6,2,−18,10,−132,18), which is a different valid solution of the same underdetermined system” implicitly treats Cai’s printed coefficients as exactly the same underdetermined structure, whereas the underdetermination and the particular 3×6 linear system are artifacts of this paper’s chosen monomial basis and benchmark set. Cai et al. are not claiming underdetermination; the mapping from their expression to this six-dimensional coefficient space is not documented or externally checkable.  

**Fix (1–2 sentences):**  
Make clear that the 6‑monomial basis, 3×6 system, coefficient vectors, SVD, and 10,000-sample null-space scan are *new constructions in this work*, only constrained to reproduce Cai et al.’s three benchmark amplitudes, and do not come from Cai et al. themselves; remove language that suggests Cai et al. “have” a 3‑dimensional coefficient null space, and add a short derivation or explicit mapping in an appendix if the basis is to be used quantitatively.


## PAPER-PER-M3 – “3–5σ” envelope vs. Li/Brandenberger c=1 convention: halving logic not fully justified

**Classification:** MAJOR  

**Location:** Abstract caveat paragraph on Li & Brandenberger c=1 vs Cai c=2 conventions, and Conclusion first paragraph.  

**Issue:**  
The paper asserts that if the Li & Brandenberger c=1 normalization is adopted, the bounce amplitude halves and therefore *the detection significance simply halves* (5.2–5.5σ → 2.6–2.75σ, and 3–5σ → 1.5–2.5σ), treating this as an exact scaling. However, because the quoted σ(fNL) is taken from an external Fisher forecast normalized in the Planck/Komatsu convention, changing the definition of fNL and the mapping between the bounce bispectrum and the local template affects both the “signal” and the way the estimator is calibrated; the scaling of σ(fNL) under a different normalization is not shown to be strictly 1/c in the presence of template mismatch, r, and mixed GR/PNG-bias systematics. The paper does not demonstrate that σ(fNL) scales linearly with the same factor of two under this convention flip; it just assumes significance→significance/2.  

**Fix (1–2 sentences):**  
Either provide an explicit argument (or calculation) that under the Li/Brandenberger c=1 convention both fNL and the Fisher-derived σ(fNL) scale by the same factor, so the significance truly halves even with template mismatch and systematics, or soften the statement to “approximately halves” and treat 1.5–2.5σ as an order-of-magnitude estimate rather than an exact propagated range.


## PAPER-PER-m1 – Multi-tracer Fisher provenance and prior work

**Classification:** minor  

**Location:** Sec. \ref{sec:spherex}, paragraph “The multi-tracer cosmic-variance cancellation invoked here originates with the multi-tracer power-spectrum technique of Seljak… McDonald & Seljak… the bispectrum-multi-tracer extension followed by Karagiannis et al. is what underwrites the Heinrich et al. bispectrum-channel forecast…”  

**Issue:**  
The text attributes the **bispectrum multi-tracer** methodology used in “Heinrich et al.” specifically to Karagiannis et al., and then builds its SPHEREx bispectrum forecast entirely on that chain. The existing Karagiannis et al. work is indeed on multi-tracer bispectrum, but the manuscript blurs the lines between power-spectrum–only multi-tracer, bispectrum multi-tracer, and the particular implementation assumed for SPHEREx: it sounds as if Heinrich et al. directly used that formalism in the exact way assumed here, which cannot be verified given the opaque citation.  

**Fix (1–2 sentences):**  
Clarify that the multi-tracer bispectrum formalism and its cosmic-variance cancellation properties are *inspired by and analogous to* Karagiannis et al., but that in this paper the SPHEREx bispectrum forecast is a **recast based on that formalism**, not a direct reuse of a published “Heinrich et al.” SPHEREx bispectrum implementation; remove or soften any language implying a one-to-one methodological identity.
