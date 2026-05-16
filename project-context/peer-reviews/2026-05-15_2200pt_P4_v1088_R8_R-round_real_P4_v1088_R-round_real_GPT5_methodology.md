# P4_v1088 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2200pt_P4_v1088_R8_R-round_real
**Wall time**: 84.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=79157, completion=4893, reasoning=3106, total=84050

---

## PAPER-GPT-B1 — BLOCKER — Residual `ℓ_eff=4`/`ℓ=1` conflation remains

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| Introduction; §Dipole “Simple dipole”; §Discussion; Fig. raw-vs-eq caption | “lowest bandpower (`ℓ_eff=4`, `ℓ∈[2,6]`) … at `ℓ=1`” / “pre-MASTER pseudo-`C_ℓ` at `ℓ=1` inflates to `+6.48σ` … in the lowest bandpower” | Table multipole footnote: “`ℓ_eff=4` bandpower spans `ℓ∈[2,6]` and does **not** include `ℓ=1`”; NaMaster appendix: headline `ℓ=1` is a single-multipole bin, not a bandpower | REGRESSION |

**Issue:** The old blocker is not fully fixed: several body sites still describe the `+6.48σ` lowest bandpower as “at `ℓ=1`,” which is mathematically false.  
**Fix:** Replace every remaining “at `ℓ=1`” tied to `+6.48σ` with “lowest pseudo-`C_ℓ` bandpower (`ℓ_eff=4`, `ℓ∈[2,6]`) on the asymmetry map,” and reserve `ℓ=1` only for the single-mode MASTER result.

## PAPER-GPT-B2 — BLOCKER — Sensitivity threshold is overclaimed and numerically inconsistent

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| Introduction | “empirical injection-recovery sensitivity floor of `|A_dipole|≳0.5%` at the same significance level” | Table injection: at `A=0.50%`, `P(σ>3)=0.15`; first 50% recovery is `A=0.75%`, `P(σ>3)=0.55` | STILL-UNRESOLVED |
| Conclusions item 1 | “empirical minimum detectable dipole of `∼0.5%` at `3σ`” and later “at `A=0.5%` … `P(σ>3)=0.03`” | Table injection gives `P(σ>3)=0.15` at `0.5%` | REGRESSION |

**Issue:** The manuscript still advertises `0.5%` as a systematic-inclusive `3σ` floor even though its own MC says `0.5%` is a non-detection and the 50%-recovery threshold is `0.75%`.  
**Fix:** Use `0.75%` everywhere for the empirical 50%-recovery-at-`3σ` full-amplitude threshold; state `0.5%` only as a tested non-detection point with `P(σ>3)=0.15`.

## PAPER-GPT-B3 — BLOCKER — Table “monopole+mask null” caption still claims rows it does not contain

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| Table “Monopole+mask leakage null” caption | “Pre-MASTER pseudo-`C_ℓ` and post-MASTER decoupled `C_ℓ` at `ℓ=1` both reported with their data `z`-score against the null.” | Rows contain only “Pre-MASTER pseudo-`C_ℓ^{(ℓ=1)}`” and “Hemisphere max\|A\|”; post-MASTER values appear only in a separate cross-reference sentence under a different null | REGRESSION |
| §Preregistered hierarchy row (v) | “monopole+mask null … demonstrate that both the `+1.85σ` canonical `ℓ=1` value and the hemisphere maximum statistic are consistent with monopole-mask leakage” | Same table gives hemisphere residual `+4.42σ`; post-MASTER monopole-only null is explicitly “not computed” in Table I footnote b | STILL-UNRESOLVED |

**Issue:** The table caption and methods summary still conflate pre-MASTER monopole-only nulls with post-MASTER label-shuffle MASTER MC, and overstate the hemisphere result as “consistent” despite a `+4.42σ` residual.  
**Fix:** Caption must say the table reports only two monopole-only pre/post? no: pre-MASTER pseudo-`C_ℓ` and hemisphere max statistics; move all post-MASTER values outside the caption with “different null, not comparable,” and delete the claim that the hemisphere statistic is explained by the monopole-only null.

## PAPER-GPT-M1 — MAJOR — Hemisphere look-elsewhere treatment is statistically incoherent

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| §Hemisphere Asymmetry | “`3.05σ` peak does not survive a look-elsewhere correction… trials factor 650 reduces effective significance to `<1σ`” | Footnote: direct max-over-directions MC has zero of `10,000` nulls reaching data, `p_LEE ≤ 10^{-4}` | NOVEL |
| Fig. hemisphere caption / §Hemisphere discussion | “We treat the multiplicity-corrected `<1σ` as the conservative null-consistency statement” while also saying direct MC rejects random-label null at `≳3.7σ` | Direct MC is the correct calibration for the searched maximum statistic, not an optional incomparable statistic | NOVEL |

**Issue:** The paper simultaneously claims the hemisphere statistic is LEE-consistent with null and rejects the random-label max-statistic null at `p≤10^{-4}`.  
**Fix:** Make the direct max-statistic MC the primary LEE result; then state the rejection is of an inadequate random-label null and requires a systematics-preserving null before any physical interpretation.

## PAPER-GPT-M2 — MAJOR — Parity caveat fixes the dipole language but makes a false `C_ℓ` claim

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| §Dipole symmetry caveat | “`a^P_{ℓm}=(-1)^{ℓ+1}a_{ℓm}` … dipole tests isotropy, not parity violation per se” | This transformation is correct for a pseudoscalar field | HOLDS |
| Same paragraph | “the parity-violation tests in our data are the monopole … and the even-`ℓ` pseudo-`C_ℓ` bandpowers” | `C_ℓ=|a_{ℓm}|^2` is parity-even; a nonzero even-`ℓ` power is not itself a parity-odd observable | NOVEL |

**Issue:** The harmonic-coefficient parity statement is fine, but calling even-`ℓ` power spectra “parity-violation tests” is wrong because power spectra discard the sign.  
**Fix:** Say the monopole/even-`ℓ` **signed coefficients or maps** are parity-odd diagnostics; `C_ℓ` bandpowers are anisotropy/systematics diagnostics unless a signed parity-odd statistic is defined.

## PAPER-GPT-M3 — MAJOR — Sky-balance artifact does not verify the table it is cited for

| Section | Paper says | Internal/artifact says | Verdict |
|---|---|---|---|
| Table sky balance caption | Verification artifact: `.../global_cw_fraction.json`; footnote: “per-region breakdown is reported in the table cells directly above” | The cited artifact is global by name and cannot independently verify RA/Dec regional fractions; no per-region JSON is supplied | STILL-UNRESOLVED |

**Issue:** A global CW-fraction JSON is not an appropriate reproducibility artifact for seven per-region sky-balance numbers. The table cells are not an on-disk verification source.  
**Fix:** Either cite an existing per-region artifact containing the seven numerators/denominators/fractions, or remove the verification claim and mark the table as manuscript-only until the promised per-region JSON exists.
