# P4 R-round — DIRECT vendor — Grok-4 brutal-honesty reviewer

**Model**: `grok-4` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 17.9s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=89709, completion=901, total=91113, prompt_details={'text_tokens': 89709, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 128}, completion_details={'reasoning_tokens': 503, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, num_sources_used=0, cost_in_usd_ticks=1155118500

---

**PAPER-GRO-B1 (BLOCKER)**  
Lines: Abstract (headline result), Sec. 9 (Declared Analysis Hierarchy), Table II, Sec. 10.3 (canonical-mask direct-MC).  
The load-bearing “null” is reported on the strict-superset subsample mask (\(f_{\rm sky}=0.659\), \(-0.12\sigma\)) while the canonical mask (\(f_{\rm sky}=0.49005\)) yields \(+3.64\sigma\) that is then attributed to systematics. The hierarchy is declared after the fact; the canonical mask is the natural analysis mask for the released catalog. This is post-selection of the mask that produces the desired null.

Fix: State the pre-specified primary mask in Sec. 9 before any results are shown and report the canonical-mask result as the primary number (with the subsample mask as a robustness check), or explicitly pre-register the mask choice.

**PAPER-GRO-B2 (BLOCKER)**  
Lines: Abstract, Sec. 1 (last paragraph), Sec. 13.1.  
The paper repeatedly states that Shamir’s \(\sim 3\%\) signal is “inconsistent in amplitude” by a factor of 6–12 under the present pipeline, yet explicitly declines to run the matched-footprint Ganalyzer reanalysis required for a likelihood-level comparison. Amplitude mismatch under a different classifier/selection is not a statistical exclusion.

Fix: Remove all quantitative “factor of 6–12” language and replace with a single sentence: “A like-for-like reanalysis under Shamir’s exact Ganalyzer pipeline and cuts on the present footprint is required for a formal exclusion and is not performed here.”

**PAPER-GRO-M1 (MAJOR)**  
Lines: Abstract (sensitivity paragraph), Sec. 9.1 (Fisher vs. empirical), Table VII caption.  
The paper mixes the analytic Fisher floor (\(\sim 0.29\%\)) with the empirical 50%-recovery-at-3\(\sigma\) threshold (\(0.75\%\)) and the HC-subsample vs. full-catalog distinction without a single clear statement of which number is the claimed sensitivity. The abstract headline uses the empirical number while the text repeatedly cites the Fisher number as if they are interchangeable.

Fix: Report one number as the headline sensitivity (the empirical 50%-rec-3\(\sigma\) threshold on the exact sample used for the primary estimator) and move all Fisher derivations to an appendix with an explicit “statistical-only, zero-systematic-dipole-projection” caveat.

**PAPER-GRO-M2 (MAJOR)**  
Lines: Sec. 10.3 (multi-null battery), Sec. 10.4 (cross-spectrum), Table VI footnote b.  
The canonical-mask residual is declared “interpretation (ii) systematic” after a 4-null battery whose strongest discriminator (direct cross-spectrum at \(\ell=2\)) is only \(-2.89\sigma\) before trials correction and whose bootstrap test is acknowledged to be uninformative. The paper nevertheless treats the systematic interpretation as settled.

Fix: Downgrade the language to “favored but not formally demonstrated; a joint nuisance-marginalized model comparison is required for a definitive separation of primordial dipole vs. depth/morphology systematic.”

**PAPER-GRO-m1 (minor)**  
Lines: Title, abstract first sentence.  
“Survey-Scale … with Equivariant TTA” and the long subtitle present the work as a methodological advance. The actual methodological novelty (2-fold flip TTA on ViT-Small) is modest relative to CE-ResNet’s architectural equivariance; the scale increase is real but the title over-claims uniqueness.

Fix: Shorten title to “Galaxy Chirality Dipole with DESI Legacy DR8 and Equivariant TTA: A −0.12\(\sigma\) Null on the Subsample Mask”.

**PAPER-GRO-m2 (minor)**  
Lines: Multiple table captions and footnotes (e.g., Table II, Table III, Table VI).  
Dozens of precise \(\sigma\) values and MC counts are given for secondary or diagnostic estimators whose only role is to support the interpretation of the canonical residual. These numbers are not load-bearing for the headline claim and inflate the apparent rigor.

Fix: Move all non-primary estimator tables to an appendix labeled “Diagnostic estimators (not used for the cosmological conclusion)”.
