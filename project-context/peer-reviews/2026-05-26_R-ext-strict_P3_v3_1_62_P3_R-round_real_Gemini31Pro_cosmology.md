# P3 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P3_v3_1_62
**Wall time**: 53.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=70329, completion=3443, reasoning=2437, total=73772

---

## PAPER-GEM-B1: AI-Vendor and Version-History Contamination (BLOCKER)
**Location:** Abstract, Section 3.3, Section 3.4, Section 6.4
**Issue:** The manuscript body is heavily contaminated with internal LLM-reviewer audit trails, version-control notes, and API vendor names (e.g., "R15 GEM-B1 closure", "GPT-5.5, Gemini-2.5-Pro, Grok-4", "queued for the next pod-pull cycle", "Wave 14-VVV"). A journal submission cannot contain raw development logs or AI-reviewer meta-commentary.
**Fix:** Purge all meta-commentary, R-round closure notes, version deferrals, and vendor references from the manuscript body; present only the final scientific methodology and results.

## PAPER-GEM-B2: Uncorrected GR Projection Effects at $f_{NL} \sim \mathcal{O}(1)$ (BLOCKER)
**Location:** Section 5 and Section 6.4 (Caveat e)
**Issue:** The paper claims a multi-tracer Fisher forecast of $\sigma(f_{NL}) = 8.14$ but explicitly admits omitting $\mathcal{O}(\mathcal{H}^2/k^2)$ general-relativistic projection effects (Doppler, Sachs-Wolfe), acknowledging they "perfectly mimic local-PNG scale-dependent bias at large scales" and leaving their inclusion as a "deferral for the recompute plan." You cannot publish an $\mathcal{O}(1)$ $f_{NL}$ forecast while knowingly omitting the exact theoretical contamination that mimics the signal.
**Fix:** Compute and deterministically subtract the GR projection corrections from the theoretical template before quoting the $f_{NL}$ forecast, or remove the cosmological $f_{NL}$ constraint claims entirely.

## PAPER-GEM-B3: "In-Flight" Pipeline Steps and Pending Recompiles (BLOCKER)
**Location:** Section 3.4 (LAMOST) and Section 6.4 (Caveat f)
**Issue:** The manuscript contains placeholder text for unfinished analysis, stating the LAMOST native re-score "will supersede the 44,075 cross-transfer figure... upon the post-rebuild recompile" and that exact intersection counts are "queued for the v3.1.46+ verification table." A paper cannot be accepted while core pipeline steps and verification tables are explicitly marked as pending.
**Fix:** Execute all pending pipeline steps, finalize the tables with the actual intersection counts, and remove all forward-looking "queued for next version" language.

## PAPER-GEM-M1: Missing Data Vector Definitions Table (MAJOR)
**Location:** Section 5 / Appendix C
**Issue:** The text quotes a "canonical 5-tracer configuration" and a "7-bin Fisher result" for the multi-tracer $f_{NL}$ forecast but fails to provide a data vector definitions table specifying the redshift binning, tracer densities, bias priors, and cross-tracer covariance assumptions. 
**Fix:** Add a formal data vector table detailing the exact $(k, z)$ binning, $n(z)$, $b(z)$, and nuisance parameter priors used for the Fisher matrix.

## PAPER-GEM-M2: Unsubstantiated "Pre-registered" Claims (MAJOR)
**Location:** Section 2.2 and Appendix D
**Issue:** The text repeatedly claims metrics passed a "pre-registered" gate (e.g., "pre-registered $\bar{J} \geq 0.70$ stability gate", "preregistered diagnostics"), but provides no citation, DOI, or time-stamped repository link to the actual pre-registration document.
**Fix:** Provide a verifiable citation/URL to the time-stamped pre-registration protocol, or remove the word "pre-registered" and state these were internal *a priori* thresholds.

## PAPER-GEM-M3: Invalid 1D Likelihood Ratio on Correlated Posterior (MAJOR)
**Location:** Section 5.1 and Section 6.4 (Caveat d)
**Issue:** The paper quotes a $\Delta\chi^2 = 21.31$ parameter-shift evidence against SMBHB based on a 1D marginal Gaussian assumption, admits this is invalid for a correlated 2D posterior, and defers the proper Savage-Dickey density ratio to a "companion artifact" that is not presented in the text.
**Fix:** Calculate and report the actual 2D Savage-Dickey Bayes factor in the text, or completely remove the $\Delta\chi^2$ parameter-shift comparison as it is mathematically invalid on the correlated posterior.
