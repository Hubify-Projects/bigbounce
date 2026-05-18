# P4_v1_0_113_R_INTERNAL R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1815pt
**Wall time**: 149.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=91251, completion=6062, reasoning=4865, total=97313

---

Here is the adversarial peer review of manuscript v1.0.113.

## Finding 1: BLOCKER - Abstract is a 1500-word PR log, not an academic abstract
**ID:** PAPER-GEM-B1
**Section:** Abstract
**Issue:** The abstract is over 1500 words long and reads like an internal JIRA ticket or pull-request log. It contains bolded meta-commentary ("P4-EXT ChatGPT-B3 injection-subsample-predicate clarification", "P4-INTERNAL Gemini-B1 closure"), inline reproducibility paths, and exhaustive methodological patching. This is completely unacceptable for a journal submission and obscures the actual scientific result.
**Fix:** Rewrite the abstract to be a standard ~250-word summary of the final scientific results (the 3.2M sample, the 0.75% sensitivity floor, the $-0.12\sigma$ subsample-mask null, and the identification of the canonical-mask excess as a depth-correlated systematic). Move all internal review provenance to an appendix or cover letter.

## Finding 2: BLOCKER - Schizophrenic/Contradictory $\sigma$ values for the canonical mask
**ID:** PAPER-GEM-B2
**Section:** Abstract, Sections IV.C, IV.D, VIII, Tables III, V, IX
**Issue:** Section VII explicitly states "the v1.0.107 corrected $\sigma = +3.64$ supersedes the v1.0.62 baseline $\sigma = +1.85$ as the canonical canonical-mask number (paper-wide convention from v1.0.107+)". However, the abstract, main text, and all summary tables still quote $+1.85\sigma$ as the primary canonical-mask result, treating $+3.64\sigma$ as an appended footnote. Quoting a mathematically incorrect (improperly monopole-subtracted) number as the baseline is scientific malpractice.
**Fix:** Execute your own declared "paper-wide convention": replace all instances of $+1.85\sigma$ with $+3.64\sigma$ in the main text and tables, and state clearly that $+3.64\sigma$ is the mathematically correct proper-monopole-subtracted result.

## Finding 3: MAJOR - Incomplete scrub of "Bootstrap consistent with null" claim
**ID:** PAPER-GEM-M1
**Section:** Abstract, Section IV.D
**Issue:** Despite the R18 GEM-B2 directive and the paper's own admission that the bootstrap is "TAUTOLOGICAL for cosmological-dipole hypothesis testing", the abstract still explicitly claims the bootstrap "gives $\mathbf{-0.22\sigmaunit}$, \emph{consistent with null}" as part of the definitive resolution battery. This directly contradicts the tautology admission and violates the scrub directive.
**Fix:** Remove the phrase "\emph{consistent with null}" from the bootstrap description in the abstract and Section IV.D. State only that it yields $-0.22\sigma$ as a sampling-variance diagnostic.

## Finding 4: MAJOR - Theoretical conflation of depth proxy with true cosmological density
**ID:** PAPER-GEM-M2
**Section:** Section IV.D (Direct cross-spectrum smoking gun)
**Issue:** The cross-spectrum $C_\ell^{An}$ uses $n_{\rm total}(p)$ as a "direct proxy for depth/sampling-density". However, $n_{\rm total}$ also traces the true cosmological matter density (LSS). While depth variations dominate large-scale power in DESI Legacy, true density fluctuations (and potential magnification bias or intrinsic alignments) also contribute to $n_{\rm total}$. It is a biased tracer of depth.
**Fix:** Add a 1-2 sentence theoretical caveat in Section IV.D acknowledging that $n_{\rm total}$ is a biased tracer of depth because it includes true cosmological density fluctuations, though depth variations dominate the large-scale quadrupole.

## Finding 5: minor - Section IV.D is an unreadable wall of text
**ID:** PAPER-GEM-m1
**Section:** Section IV.D
**Issue:** The "v1.0.107 Grok-B1 BLOCKER closure" and "v1.0.108 multi-null battery" paragraphs are massive, unstructured blocks of text that read like raw review responses rather than a cohesive scientific argument. The 3-discriminator logic is buried inside meta-review headers ("Houston directive", "Grok-B1 R16 demanded").
**Fix:** Refactor the "Honest scientific verdict across the three interpretations" into a standard enumerated list or subsections. Strip all internal meta-review headers from the main text.

## Finding 6: nit - Redundant/ambiguous MC counts in Table III
**ID:** PAPER-GEM-n1
**Section:** Table III
**Issue:** The Table III caption states "500 MC realizations for the post-MASTER $\ell=1$ single-mode row only; the $\ell\ge 2$ bandpower rows use the cheaper $N_{\rm MC}=1,000$". However, footnote 'd' references "the 1000-realization MC null mean". Mixing 500 and 1000 in the same table without a dedicated column makes the $z$-score reverse-engineering ambiguous.
**Fix:** Add the queued "dedicated null-mean column" and explicitly list $N_{\rm MC}$ per row in Table III to resolve the ambiguity.
