# P4_v1100 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0330pt_P4_v1100_R18_R-round_real
**Wall time**: 19.6s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=75045, completion=1865, reasoning=1101, total=76910

---

**PAPER-GRO-B1**  
**BLOCKER** — Abstract L1–3 and §I L124–130 ("parity-violating signal" framing for the dipole)  
The dipole observable is explicitly parity-even (axial-vector projection); attaching "parity-violating" to it in the lead sentence and early framing is factually inverted and revives the exact language the v1.0.100 rewrite was supposed to excise.  
**Fix**: Replace every instance of "parity-violating dipole/signal" with "isotropy-breaking axial-vector dipole" when referring to the ℓ=1 channel; retain "parity-violating sectors" only in the EFT context where it is not attached to the dipole.

**PAPER-GRO-B2**  
**BLOCKER** — Table I (headline_summary) row (iv) and §VIII L4051 ("f_sky=0.494" for canonical mask)  
Stale value persists after the v1.0.100 global update to 0.49005; this is the exact residual the round context flagged for closure.  
**Fix**: Change to 0.49005 in the hemisphere row and any remaining canonical-mask contexts; add a footnote confirming the NaMaster production binning if 0.491 is intentional.

**PAPER-GRO-B3**  
**MAJOR** — §IX.J and abstract sensitivity paragraph (injection sweep on HC subsample only)  
The load-bearing 0.75% 50%-recovery threshold is measured on the 471k HC subsample; the full-catalog 3.2M Fisher floor (0.29%) is never empirically validated, yet the paper presents the 0.75% figure as the survey-scale sensitivity. This is a material overclaim.  
**Fix**: Explicitly label the 0.75% value as "HC-subsample empirical threshold" and state that a full-catalog injection sweep remains deferred; do not equate it to the full-sample sensitivity without the missing run.

**PAPER-GRO-B4**  
**MAJOR** — Abstract L15–20 and §I L201 ("largest survey-scale chirality catalog" + "one of the most extensive bias-hardening suites")  
The 3.2M spiral count is larger than CE-ResNet, but the claim ignores that CE-ResNet is architecturally equivariant (no post-hoc TTA) and that the present bias suite is still post-hoc. The "largest" framing is technically true but narratively inflated given the different methodology.  
**Fix**: Change to "largest spiral sample with post-hoc equivariant TTA and published bias audit" and remove "to our knowledge one of the most extensive" or qualify it against architectural-equivariance methods.

**PAPER-GRO-B5**  
**minor** — Multiple artifact paths (e.g., L702, L2133, L2280) still reference paper4-v1.0.97/v1.0.98 tags in footnotes and reproducibility blocks  
These are the exact stale-tag residuals the round context listed for closure.  
**Fix**: Global search-replace to paper4-v1.0.100 (or current immutable tag) in all \artifact{} and footnote paths.

**PAPER-GRO-B6**  
**nit** — Abstract length and repeated "this-pipeline demonstration / matched-footprint reanalysis not performed" caveats  
The abstract is 650+ words and buries the central leakage result under repeated disclaimers; this is defensive writing rather than crisp reporting.  
**Fix**: Condense the abstract to ≤450 words, lead with the monopole-leakage quantification and post-MASTER null, and move the "matched-pipeline caveat" to a single sentence in the conclusions.
