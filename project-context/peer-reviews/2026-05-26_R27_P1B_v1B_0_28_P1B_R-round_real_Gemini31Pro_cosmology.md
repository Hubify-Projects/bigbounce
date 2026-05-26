# P1B R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R27_P1B_v1B_0_28
**Wall time**: 115.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=24920, completion=10765, reasoning=10059, total=35685

---

**META-NOTE: Grok Scope-Pushback Accepted**
I confirm the acceptance of the Grok scope-pushback. The author's explicit framing of the paper as a "Technical Verification Companion" with repeated, prominent disclaimers (e.g., "Not a spin-torsion theory module", "Not a distinctive ECH prediction") adequately neutralizes the critique that the pipelines are not ECH-specific. The companion's purpose is pipeline validation, which has been successfully scoped.

**STATUS:** 0 BLOCKERs found. The defense against the R14 GEM-B1 SH0ES YAML alias failure is mathematically flawless, and the explanation of the KDE Savage-Dickey failure in the unsampled tails is statistically rigorous. 

## PAPER-GEM-M1 (MAJOR)
**Location:** Section 7.1, paragraph 3 ("Quintom-B is the only class admitted...")
**Concrete Issue:** Claiming Quintom-B is the *only* class capable of crossing the phantom divide overstates the model-class boundary. Single-field models with kinetic gravity braiding (e.g., Horndeski/Galileons) can also cross $w=-1$ smoothly without gradient instabilities or ghosts.
**Fix:** Soften to "Quintom-B is a primary class admitted..." or explicitly acknowledge Horndeski/braiding exceptions.

## PAPER-GEM-m2 (minor)
**Location:** Section 6, "comfortably within natural ALP-photon coupling ranges"
**Concrete Issue:** While $C_{a\gamma} \sim 51$ is not fine-tuned, it requires specific UV completions (e.g., clockwork mechanisms, large anomaly coefficients, or many charged species) and is not generically "natural" in minimal $\mathcal{O}(1)$ setups. This slightly overstates UV-completion independence.
**Fix:** Change "comfortably within natural ALP-photon coupling ranges" to "achievable in specific UV completions (e.g., clockwork or large-charge models)".

## PAPER-GEM-m3 (minor)
**Location:** Section 6, "yields the field displacement from recombination to today: $\Delta\phi/f_a \approx 0.65$ ($m = H_0$)"
**Concrete Issue:** For $m \sim H_0$, the field is Hubble-dragged until very recently, meaning the displacement (and thus the birefringence) is accumulated almost entirely at late times ($z \lesssim 1$). This tomographic distinction is physically important when comparing CMB rotation to high-$z$ galaxy rotation.
**Fix:** Add a brief note clarifying that for $m \sim H_0$, the rotation is predominantly accumulated at late times ($z \lesssim 1$) rather than uniformly since recombination.

## PAPER-GEM-n4 (nit)
**Location:** Section 4, "drawn at ACT-noise level... (a conservative worst-case bias check)"
**Concrete Issue:** Injecting low (ACT-level) noise into a high-noise (Planck) map is a worst-case check for *pipeline bias detectability* (because it maximizes the SNR of the bias itself), not a worst-case for the map's actual sky recovery.
**Fix:** Change to "a conservative worst-case check for pipeline bias detectability".
