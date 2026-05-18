# P4_v1_0_111_R_INTERNAL R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1745pt
**Wall time**: 38.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=89908, completion=3936, reasoning=2904, total=93844

---

## PAPER-GEM-B1: Contradictory Sigma Reconciliation (BLOCKER)
**Location:** Section IV.D (v1.0.107 Grok-B1 BLOCKER closure) vs. Section VII (Monopole-subtraction note)
**Issue:** The manuscript contains a massive internal contradiction regarding the origin of the $+3.64\sigma$ vs $+1.85\sigma$ canonical-mask results. Section IV.D claims that "after proper monopole subtraction the canonical-mask data corresponds to $\sigma_{\rm corrected}=+3.64$". However, Section VII explicitly states that proper monopole subtraction "reduces decoupled $C_1$ by only $\sim 5\%$... the corrected sigma is approximately $1.85 \times 0.954 \approx 1.77\sigma$" and concludes that improper subtraction does NOT explain the $+1.85\sigma$ residual. You cannot simultaneously claim proper subtraction inflates the signal to $+3.64\sigma$ and deflates it to $+1.77\sigma$.
**Fix:** Reconcile the math. If $+3.64\sigma$ comes from a different injection-sweep baseline or different $N_{\rm MC}$ variance rather than the monopole subtraction itself, state the actual mathematical driver and delete the contradictory $+1.77\sigma$ audit from Section VII.

## PAPER-GEM-B2: Bootstrap Tautology Leakage (BLOCKER)
**Location:** Abstract and Section IV.D (Operational conclusion)
**Issue:** The prompt explicitly states the bootstrap null was dropped from the verdict logic because it is tautological for a cosmological dipole. Yet the Abstract still prominently cites "the bootstrap pixel-resample null... gives $-0.22\sigma$, *consistent with null*" to dismiss the canonical mask excess. Furthermore, Section IV.D concludes: "we recommend any external review treat the canonical-mask result as *null under the bootstrap null*, not as a detection." Recommending a tautological null as the official verdict invalidates the hypothesis test.
**Fix:** Scrub all claims of "consistent with null under bootstrap" from the Abstract and conclusions. Anchor the canonical-mask dismissal strictly on the three valid discriminators ($\ell=2>\ell=1$, $p_{eq}$ washout, cross-spectrum).

## PAPER-GEM-M1: Abstract is a Defensive Changelog (MAJOR)
**Location:** Abstract
**Issue:** The abstract is vastly over journal length limits and reads like an internal Jira ticket history rather than a scientific summary. It contains raw JSON artifact paths, internal review tags ("P4-INTERNAL Gemini-B1 closure", "P4-EXT ChatGPT-B3"), and defensive methodological justifications. No physics journal (PRD/MNRAS) will accept an abstract formatted as a peer-review audit log.
**Fix:** Rewrite the abstract to $\sim 250$ words. State the sample size, the pipeline, the headline null result ($-0.12\sigma$ post-MASTER), the empirical sensitivity ($0.75\%$), and the identification of the monopole-mask leakage channel. Move all internal audit trails, JSON paths, and multi-null triage logic to the main text or an appendix.

## PAPER-GEM-m1: Tautological Discriminator in Evidence List (minor)
**Location:** Section IV.D (Honest scientific verdict across the three interpretations)
**Issue:** In defending interpretation (ii) [depth-correlated systematic], the text lists its supporting features: "the broadband low-$\ell$ signature, direction-coherent under sky rotation (still $+2.56\sigma$), bootstrap-consistent-with-null, and quality-quartile-washout pattern". Including "bootstrap-consistent-with-null" here contradicts your own finding two paragraphs earlier that the bootstrap variance is too wide to distinguish a real $1.7\%$ dipole from null.
**Fix:** Remove "bootstrap-consistent-with-null" from the list of features supporting interpretation (ii).

## PAPER-GEM-m2: Birefringence vs. LSS Chirality Physics Distinction (minor)
**Location:** Section V.G (i) Chiral gravitational-wave power asymmetry
**Issue:** When contrasting the morphology dipole with the CMB birefringence measurement ($\beta=0.342^\circ$), the text states they are "not directly numerically comparable in any common parameter". While true, this misses the fundamental theoretical distinction: CMB birefringence is a line-of-sight integrated propagation effect (Chern-Simons coupling to the electromagnetic tensor), whereas galaxy spin chirality is an initial-conditions/generation effect (coupling to the metric tensor/LSS formation). 
**Fix:** Add a half-sentence clarifying that the two channels probe fundamentally different physical regimes (photon propagation vs. LSS generation) to strengthen the theoretical framing.
