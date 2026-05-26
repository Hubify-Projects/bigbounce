# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v132verify_P4_v1_0_132
**Wall time**: 18.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=90789, completion=2560, reasoning=1903, total=93349

---

**PAPER-GRO-B4-RESIDUAL (BLOCKER)**  
**Section:** Table~\ref{tab:data_vectors}, row (v)  
**Issue:** Post-closure table still lists `N_MC=500 (10000 in v1.0.130 ext)` for the monopole-only null. The surgical fix to uniform 10,000 was not applied; the parenthetical version tag remains.  
**Fix:** Set the cell to `10,000` and delete the version note entirely.

**PAPER-SCAFFOLD-RESIDUAL (MAJOR)**  
**Section:** Table~\ref{tab:headline_summary} footnotes b, c, d and Table~\ref{tab:data_vectors} caption  
**Issue:** Footnotes retain multi-paragraph review-closure history (ChatGPT-M3, Gemini-BL2, version tags, artifact paths, and internal flag references). These are review-defense text, not scientific content.  
**Fix:** Delete all version-specific and reviewer-attribution sentences; retain only the scientific null-distribution and scope statements.

**PAPER-TITLE-FRAMING (MAJOR)**  
**Section:** Abstract, first paragraph (lines ~80-95) and §\ref{sec:dipole_symmetry_caveat}  
**Issue:** The manuscript correctly states the observable is parity-EVEN axial-vector, yet the abstract and symmetry section still open with "parity violation" language before the clarification. This creates a misleading first impression that the title was intended to avoid.  
**Fix:** Lead the abstract and symmetry section with the parity-EVEN statement; move any historical "prior literature conflated" sentence to a later paragraph.

**PAPER-OVERCLAIM (minor)**  
**Section:** Abstract and §\ref{sec:stats}  
**Issue:** "Largest survey-scale chirality catalog" and "most sensitive" are used without qualification. The 3.2 M spiral count is larger than CE-ResNet but the claim is load-bearing only for the specific ViT+TTA+DESI combination; prior nulls (Iye et al. 2021) already exist at lower sensitivity.  
**Fix:** Qualify as "largest equivariant-TTA chirality catalog on DESI Legacy DR8" or drop the superlative.

**PAPER-MC-INCONSISTENCY (minor)**  
**Section:** Table~\ref{tab:headline_summary} footnote b and §\ref{sec:monopole_mask_null}  
**Issue:** Text alternates between N=500 and the 10,000 extension without a single canonical number for the post-MASTER monopole-only null.  
**Fix:** State the 10,000-run result as the primary number and relegate the 500-run comparison to a parenthetical robustness check.

**PAPER-NULL-LOADBEARING (nit)**  
**Section:** Abstract and §\ref{sec:prereg}  
**Issue:** The load-bearing result is the subsample-mask −0.12σ; the canonical-mask +3.64σ is repeatedly presented as a "diagnostic" yet occupies disproportionate space.  
**Fix:** Shorten the canonical-mask multi-null battery to one paragraph after the headline null is stated; move detailed cross-spectrum and quartile tables to an appendix.
