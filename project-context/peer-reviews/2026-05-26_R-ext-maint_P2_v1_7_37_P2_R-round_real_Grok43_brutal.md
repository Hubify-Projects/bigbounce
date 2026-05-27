# P2 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P2_v1_7_37
**Wall time**: 14.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=30203, completion=2204, reasoning=1386, total=32407

---

**PAPER-GRO-B1**  
**Classification:** BLOCKER  
**Location:** Abstract (entire paragraph) + §1 (L29–38) + §8 (L419)  
**Issue:** The central claim that the matter-bounce \(f_{\rm NL}=-35/8\) is a "minimally parameterized" discriminator is false. The prediction only holds under six restrictive assumptions (a–f), one of which (e) explicitly excludes the majority of published bounce models that include post-bounce inflation. The Li/Brandenberger convention halves the signal, and the paper itself shows this drops the headline significance to 1.5–2.5σ.  
**Fix:** Replace all "minimally parameterized" and "mechanism-independent" language with "conditional on assumptions (a)–(f) and the Cai normalization convention."

**PAPER-GRO-B2**  
**Classification:** BLOCKER  
**Location:** Abstract (L79–82) + §6 (L293–309) + Table 2 caption  
**Issue:** The Bayes-factor headline "BF ∼10–17" is not load-bearing. It requires the broadest competitor prior \([-15,+15]\) and the delta-function bounce prior; the physically motivated curvaton prior \([-5,+5]\) gives BF∼4. The version history documents repeated numerical corrections (6→4, 8→10) from scipy.stats.norm mismatches.  
**Fix:** State the recommended baseline as BF∼4 (curvaton prior) or remove the 10–17 envelope from the abstract.

**PAPER-GRO-B3**  
**Classification:** MAJOR  
**Location:** Abstract (L67) + §3.2 (L216) + §4 (L254)  
**Issue:** The claim "we quantify for the first time the template mismatch" is overstated. The bounce shape has been public since Cai et al. (2009); computing its overlap with the local template is a standard Fisher inner-product exercise. No evidence is provided that no one performed this calculation in 15 years.  
**Fix:** Change to "we compute the template overlap factor \(r=0.84\pm0.02\)" and drop the "first time" framing.

**PAPER-GRO-B4**  
**Classification:** MAJOR  
**Location:** Abstract (L55–60) + §4 (L241–245)  
**Issue:** The 3–5σ (post-systematics) and 5.2–5.5σ (optimistic) figures are not independent forecasts. They are a rescaling of Heinrich et al. (2024) \(\sigma(f_{\rm NL})=0.7\) by ad-hoc factors (\(r\), \(\epsilon\)-correction, GR, \(b_\phi\)). No new Fisher matrix is computed.  
**Fix:** Explicitly label the result as "a sensitivity recast of Heinrich et al. (2024)" rather than a new forecast.

**PAPER-GRO-B5**  
**Classification:** MAJOR  
**Location:** §2.3 (L145–160) + assumption (e)  
**Issue:** The paper repeatedly states the prediction is "robust across the bounce class" while assumption (e) restricts it to the narrow Wilson-Ewing subclass that excludes prolonged post-bounce inflation. This is a direct internal contradiction.  
**Fix:** Remove all "robust across the bounce class" and "mechanism-independent" statements; replace with "restricted to the Wilson-Ewing class without post-bounce inflation."

**PAPER-GRO-B6**  
**Classification:** minor  
**Location:** Abstract + §9 (L436)  
**Issue:** The conclusion still contains the retired phrase about ">6×10^5 MC realizations" in an earlier draft; the current text uses the corrected 3×10^5 figure but the surrounding prose retains legacy language about Monte Carlo discovery.  
**Fix:** Delete the remaining reference to the retired aggregate count.
