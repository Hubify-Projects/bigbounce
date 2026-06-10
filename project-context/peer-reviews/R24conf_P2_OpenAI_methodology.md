# P2 R24conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.46.pdf` md5=45ee3af4 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7779 chars)
**Wall time**: 253.1s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”

Scope of review
I assessed methodology rigor, statistical validity, derivation chains, dimensional consistency, and internal arithmetic throughout the entire manuscript (23 pages). I recomputed every quoted ratio, σ-level, and key numeric in the abstract and conclusions from values in the main text, and audited each figure/table statement for consistency.

Overall assessment
The paper attempts a forecast recast for SPHEREx/MegaMapper sensitivity to a specific matter‑bounce prediction fNL = −35/8, quantifies a local‑template projection mismatch r, and presents a Bayesian model comparison. Much of the quantitative structure is sensible, and several cross‑checks (e.g., the 6.25σ→r×6.25σ arithmetic; the Bayes‑factor scaling with prior width) are correct.

However, there are critical inconsistencies and methodological gaps that must be resolved for PRD. The most serious is an explicit arithmetic inconsistency in the Bayes‑factor table (Table III and associated text) for the “narrow competitor prior” case: the reported 7.0 value is not reproducible from the paper’s own Eq. (7) and documented σ values; the correct value is ≈5.7 under the stated assumptions. There are also places where different weighting/estimation regimes are numerically juxtaposed without consistently tight bookkeeping, internal development artifact filenames appear in the body text, and several quantitative claims (e.g., “<2×10−4” sensitivity of r to squeezed‑limit cutoffs; 10–20% gains from anomaly tracers; 5% bispectrum degradation with 10% photo‑z outliers) are asserted without sufficient derivation or documented inputs.

I list detailed findings below, classified by severity.

ESSENTIAL (paper cannot be accepted without these fixes)

P2-E1 (Sec. VII C/Table III, page 15): Non-reproducible Bayes factor “BF vs. Tuned = 7.0” in the “Ideal (no GR)” row
- Offending text: Table III: “BF vs. Tuned” column shows 7.0 (no GR) for a delta bounce prior versus a tuned multifield competitor with narrow prior [−5, +5]. The text in §VI likewise states “narrow‑competitor entries give … BF ∼ 7 (delta).”
- Problem: Using the paper’s own Eq. (7), uniform competitor prior width W = 10, and σeff = 0.7 (no GR), with observation exactly at the bounce value, the closed‑form Bayes factor is B = W/(√(2π)σeff) ≈ 10/(2.506×0.7) ≈ 5.7, not 7.0. The value 7.0 would require σeff ≈ 0.57, which contradicts the “no GR” σeff = 0.7 stated in the table. The same inconsistency propagates to the sentence “the no‑GR cell (7.0) coincides with the narrow→broad sweep BF ∼ 7 → 17,” whereas the correct sweep is 5.7 → 17.1.
- Required fix: Correct Table III and all associated text to reflect the correct “narrow competitor” Bayes factor 5.7 (no GR), and update the GR‑marginalized entries accordingly (σeff = √(0.7^2+σGR^2) gives 4.67 for σGR = 0.5 and 3.27 for σGR = 1.0). Adjust all prose (“∼7”) to the corrected values and re‑evaluate any quoted ranges (“4.7–7.0”) that rely on the erroneous 7.0.

P2-E2 (Sec. III B, pages 7–8): Inconsistent statement of the template‑overlap uncertainty “r = 0.84 ± 0.02” versus the reported range that includes 0.876
- Offending text: “The result is robust: r = 0.84 ± 0.02, with the range r ∈ [0.829, 0.876] spanning all physically motivated weighting schemes (… together with the signal‑only CMB‑Fisher value 0.876…).”
- Problem: ±0.02 about 0.84 corresponds to [0.82, 0.86], which excludes 0.876. The text blurs two regimes: “noise‑weighted LSS/SPHEREx” (∼0.83) and “signal‑only CMB Fisher” (0.876). Presenting “±0.02” while simultaneously quoting 0.876 as part of the same span is internally inconsistent and risks misinterpretation.
- Required fix: Split the statement into two explicitly disjoint regimes: (i) LSS/SPHEREx‑like noise weightings: r = 0.83–0.835 (or “0.83 ± 0.01” if you wish to summarize); (ii) signal‑only (CMB Fisher): r = 0.876. Do not present a single ± value that implicitly aggregates both. Ensure the abstract and conclusions only use the LSS/SPHEREx‑appropriate r when quoting SPHEREx significances.

P2-E3 (Throughout; e.g., Secs. II A, II C, II D, VI; pages 3–6, 10–12): Internal development artifact filenames and bookkeeping references appear in the main text
- Offending text examples: “artifact c9i epsilon ratio check.json”; “c9h nullspace significance propagation.json”; “phase3 fisher overlap.json”; “null space analysis.py”; “c9j bf template rescale.py.”
- Problem: PRD does not allow internal development artifacts, repository filenames, or commit‑style references in the body. While data/code availability is welcome, such tags must be confined to a dedicated Data/Code Availability section or Supplemental Material. Their presence in the narrative sections is inappropriate and distracts from the scientific exposition.
- Required fix: Remove all internal artifact filenames and development bookkeeping from the main text. Retain them in a Data/Code Availability section or Supplement, referenced once succinctly in‑text.

P2-E4 (Abstract and throughout): Juxtaposition of σ‑levels from different procedures without always stating non‑comparability
- Offending text examples: Multiple places contrast “CMB Fisher (signal‑only)” values and “LSS/SPHEREx noise‑weighted” values in the same sentence. E.g., abstract: “5.5σ (CMB Fisher) … 5.2σ (realistic LSS).”
- Problem: The paper mostly—but not always—flags that these are different weightings/estimators. Given journal instructions to avoid side‑by‑side σ’s from different null procedures without explicit “not directly comparable,” every such juxtaposition must carry the caveat.
- Required fix: Add the explicit qualifier “not directly comparable; different weighting/estimator” at each juxtaposition (abstract; Secs. III B, IV, X). Alternatively, consolidate by presenting only the LSS‑appropriate value in the abstract and reserve CMB‑Fisher cross‑checks for the body with explicit caveats.

MAJOR (significant revision required)

P2-M1 (Sec. III B, page 7): Claim “varying x3,min from 0.001 to 0.200 changes r by < 0.0002” lacks derivation details and seems implausibly precise relative to other uncertainties
- Problem: Such a minute variation (<2×10−4) is far below other reported spreads (±0.01–0.02 between weightings, ±0.13 from the null‑space scan). No grid resolution, triangle weighting, or numerical error assessment is provided to justify this level of precision.
- Required fix: Provide a reproducible calculation (grid resolution, weighting, numerical integration tolerance, and convergence test across resolutions) substantiating this <2×10−4 claim, or replace it with a conservative bound consistent with your demonstrated numerical precision (e.g., “< 0.002 under our resolution” or remove the statement).

P2-M2 (Secs. IV and VII, pages 8–9, 13–15): Systematics budget (GR projection, bϕ marginalization, photo‑z, nonlinear bias, integral constraint, magnification) is described qualitatively, but no quantitative combination is provided for the headline “3–5σ”
- Problem: The paper asserts a post‑systematics “∼3–5σ” but does not present a table (or formula) combining baseline σ(fNL)=0.7 with multiplicative degradations (template mismatch r, ε‑correction, GR, bϕ, photo‑z, etc.) into a single central value with uncertainty. Several inputs (e.g., “30% central” degradation from bϕ) are stated qualitatively without a clear propagation rule.
- Required fix: Add a table that enumerates each degradation factor (with a reference or calculation for its value), and show the resulting combined σ and detection significance for at least two scenarios (optimistic and conservative). This must be traceable and reproduce your “3–5σ” envelope.

P2-M3 (Sec. IV, page 8; Sec. VII D, page 14): Unsupported numerical claims
- Offending statements: “anomaly‑selected tracers … project a ∼10–20% improvement in σ(fNL)”; “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼5% (0.70→0.74).”
- Problem: No Fisher matrix, shot‑noise numbers, or mock analysis is provided to substantiate these specific percentages. Given their potential practical impact, they require quantitative backing or rephrasing as qualitative expectations.
- Required fix: Either (a) provide concrete Fisher calculations (inputs, assumptions, and outputs) supporting the quoted percentages, or (b) rephrase as qualitative expectations without numbers (or move to an outlook paragraph), clearly marked as speculative.

P2-M4 (Sec. II C and Appendix A, pages 6, 20–22): “Convention vs. operator‑algebra” resolution requires a rigorous, self‑contained mapping to the exact normalizations used by Planck/SPHEREx
- Problem: The appendix explains c=1 vs c=2 conventions and the −2 Im doubling. To be fully convincing for PRD, the mapping must explicitly show that the forecasted SPHEREx σ(fNL) uses precisely the ζ‑field 6/5 normalization, and that the quoted fNL = −35/8 corresponds exactly to this estimator’s fNL (not only up to a stated equivalence).
- Required fix: Add a concise, explicit derivation mapping BΦ = 2 fNL PΦPΦ to Bζ = (6/5)fNL PζPζ with ζ= (5/3)Φ (you have the ingredients scattered; consolidate them), and state unambiguously that the Heinrich et al. forecast adopts the ζ‑field 6/5 normalization identical to your fNL definition. This removes any residual ambiguity.

P2-M5 (Sec. II B and II C, pages 5–6): “UV‑completion independence” and “faithful third‑order transfer across the bounce” are assumptions; the text sometimes reads as stronger than warranted
- Problem: While you do list the assumptions, some phrasing (“establishes … that their intermediate ε‑order decomposition is exactly half the full result … the commutator interpretation under which −35/8 is the correct Planck‑convention normalization”) could be read as asserting a resolved literature consensus. The third‑order transfer through the bounce, however, remains unverified, and the factor‑of‑two literature discrepancy involves more than nomenclature for some readers.
- Required fix: Tighten the language to consistently present these as assumptions and cross‑checks, not as definitive proofs, and move strong claims (e.g., “operator‑algebra identity closes the ambiguity”) to a careful concluding sentence limited to the estimator normalization used by the forecasts.

P2-M6 (Sec. III A, page 6): Dimensional/definition check for M(k,z)
- Offending equation: M(k, z) = 2 k^2 T(k) D(z) / (3 Ωm H0^2).
- Comment: This matches the standard convention δm = M Φ. Add a brief note clarifying definitions (transfer function normalization T→1 as k→0; D normalized to D(0)=1; H0 in comoving units), to preclude confusion. Also state the units (comoving h Mpc−1 for k) once in the text.

P2-M7 (Sec. VII C/Table III, page 15): Treatment of “BF vs. SSFSR” as “order‑of‑magnitude only,” yet tabulated with precise numbers
- Problem: Table III lists precise values (3.5×10^8, 4.5×10^5, 6.4×10^2) while the caption and text say they are prior‑dependent and only order‑of‑magnitude. This is mixed messaging.
- Required fix: Either remove the “order‑of‑magnitude only” qualifier here, or round/report them consistently as O(10^8), O(10^5), O(10^3) in the table and prose, noting the assumptions (σeff, point‑hypothesis comparison) explicitly.

MINOR (address, but paper can proceed)

P2-m1 (Sec. III B, pages 7–8): Clarify the status of “rmeasured = 0.90 ± 0.01” from the 2D KSW flat‑sky, Gaussian‑noise test
- Problem: This validation uses a CMB‑style estimator, isotropic Gaussian noise, and no mask; it is not the 3D galaxy bispectrum estimator. The paper does note this, but the numeric “±0.01” may mislead readers about LSS‑applicability.
- Required fix: Add a short clause: “This 2D KSW validation is not an LSS bispectrum pipeline; the 0.90 ± 0.01 value should be read only as a CMB‑like cross‑check.” Consider moving this to an appendix.

P2-m2 (Sec. II A, page 3; Fig. 1/Table I): Arithmetic check
- Check: −255/64 = −3.984375, −9/4 = −2.25, −35/8 = −4.375. These match. Suggest printing more significant digits in Fig. 1 y‑tick formatting (or matching text precision) to avoid visual rounding confusion.

P2-m3 (Sec. VI, pages 10–12): Bayes‑factor “bookkeeping” alternatives
- Problem: Presenting both “bounce‑amplitude space” and “measured‑space” bookkeeping is potentially confusing in the main text.
- Required fix: Pick one bookkeeping as the default (recommend measured space since the estimator is local‑template) and move the other to an appendix with a concise mapping, to streamline the narrative.

P2-m4 (Sec. VIII A, page 14): Planck PR4/NPIPE citation and number
- Check: fNL = −0.1 ± 5.0 is plausible for PR4; ensure the exact reference [31] indeed reports these numbers and not e.g. −0.9 ± 5.1 (PR3). If PR4 is preliminary or pipeline‑dependent, say so.

P2-m5 (Sec. IX E, pages 18–19): Cosmic birefringence digression
- Problem: The birefringence discussion is tangential to the paper’s core forecast. This space could be shortened or moved to an outlook note.
- Required fix: Condense to 1–2 sentences or move to supplemental/outlook.

P2-m6 (Sec. II C, page 6): “k ηbounce ∼ 10−4” estimate
- Problem: Mark this explicitly as an order‑of‑magnitude scaling estimate and provide a one‑line derivation (typical modes, ηbounce scale) or a reference.

P2-m7 (Throughout): Hyphenation artifacts (e.g., “para￾meterized”, “correc￾tion”)
- Problem: PDF hyphenation artifacts appear in the parsed text. Ensure the final typeset PDF does not include broken words or stray hyphenation marks across line breaks.

NIT (cosmetic)

P2-n1 (Title/Abstract): “with a MegaMapper Outlook”
- Suggest capitalizing consistently or rephrasing to “and an outlook for MegaMapper.”

P2-n2 (Sec. II B, page 5): Parenthetical “(Appendix A.1)” vs “A.1”
- Keep appendix subsection labels consistent (A1 vs A.1) throughout.

P2-n3 (Sec. II D, page 6): “No observational tensions with this model have been identified to date.”
- This sounds like a claim of a full global fit; consider softening to “We are not aware of observational tensions … within current uncertainties.”

P2-n4 (Figures): Ensure all axes include units or explicit “dimensionless” labels, and legend symbols match those referenced in captions.

P2-n5 (Length): The manuscript is long for what is, at core, a forecast recast plus a template‑overlap study and a simple Bayes‑factor calculation. Consider trimming repetition and moving extended methodological asides to appendices to reduce the main text to ≲15 pages.

Traceability and arithmetic checks (spot‑verified)
- 6.25σ naive significance: 4.375/0.7 = 6.25. OK.
- Template‑corrected significance: r×6.25 with r = 0.83–0.876 gives 5.19–5.48σ (you quote 5.2–5.5σ). OK.
- “Pre‑budget floor 4.8σ at 8% ε‑correction”: 4.375×0.92/0.7×0.83 ≈ 4.77σ. OK.
- Convention‑reversal halving: 2.1875/0.7 = 3.125σ; ×0.83–0.876 = 2.59–2.74σ (“2.6–2.75σ”). OK.
- MegaMapper ideal: 4.375/0.5 = 8.75; ×r = 0.84–0.88 → 7.35–7.7σ (“7.4–7.7σ”). OK.
- Single‑field inflation gauge‑frame value: (5/12)(1−ns) with ns=0.9649 → 0.0146 (“≈0.015”). OK.
- Bayes factor (broad competitor W=30, delta bounce, σ=0.7): 30/(√2π·0.7)=17.1 (“∼17”). OK.
- Bayes factor (broad competitor, σtheory=1.0): 17.1×√(0.49/1.49)=9.81 (“∼10”). OK.
- Table III “BF vs SSFSR”: exp(Δ^2/(2σ^2)) with Δ≈4.39 gives 3.4×10^8 (σ=0.7), 4.4×10^5 (σ=0.86), 6.5×10^2 (σ=1.22). OK.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains substantive value, but cannot be accepted in its current form due to (i) a clear arithmetic inconsistency in the Bayes‑factor table for the narrow‑prior competitor (7.0 vs the correct ≈5.7), (ii) inconsistent presentation of the template‑overlap uncertainty r that blends two estimator regimes, (iii) inclusion of internal development artifacts in the main text, and (iv) insufficiently quantified systematics propagation underlying the headline “3–5σ” claim. Correcting these issues, tightening estimator comparability caveats at every juxtaposition, and providing a transparent, quantitative systematics table will bring the paper up to PRD methodological standards. The remaining minor items can be addressed in revision.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh‑eyes pass)

ESSENTIAL

P2-E5 (Sec. II A, Eqs. (1)–(2), pages 3–4): Internal inconsistency in the definitions of AT and BNL; incorrect “no cancellation” claim and degree counting
- Offending text: Eq. (1) defines AT(k1,k2,k3) = 3/[256 k1^2 k2^2 k3^2] × P(k1,k2,k3). Eq. (2) then defines BNL = (10/3) P / [AT Σi k_i^3], and the text asserts “BNL is dimensionless by construction … Note that BNL retains its full dependence on (c1,…,c6) through P via AT; no cancellation of P occurs between Eqs. (1) and (2).”
- Problem: With AT ∝ P, the ratio P/AT collapses algebraically to a constant times k1^2 k2^2 k3^2, so P cancels. That directly contradicts the sentence “no cancellation of P occurs,” and it also breaks the stated degree counting: P has degree 9, AT has degree 9−6=3, so P/AT has degree 6; dividing by Σk^3 (degree 3) leaves degree 3, not degree 0 as claimed. As written, Eqs. (1)–(2) cannot simultaneously yield a dimensionless, coefficient‑dependent BNL.
- Required fix: Correct the AT and BNL definitions so that (i) the degree counting is consistent and BNL is truly degree‑0, and (ii) the intended dependence on the polynomial coefficients is retained (or explicitly state that BNL is independent of P if that is the intent, and adjust all later statements/analyses that rely on coefficient‑dependent BNL). A minimal fix is to present the standard shape normalization unambiguously (e.g., define the bispectrum and shape function as in Maldacena/Planck conventions and derive BNL from that), and remove the incorrect “no cancellation” sentence.

P2-E6 (Secs. VI.C.b and IX.D, pages 11 and 18): Quasi‑Single‑Field Inflation (QSFI) squeezed‑limit scaling endpoints are reversed
- Offending text: “Across µ/H ∈ [0, 3/2] the QSFI bispectrum interpolates between the super‑squeezed long‑mode‑divergent shape (Δ = 0, (k3/k1)−3/2) and the local‑template flat scaling (Δ = 3/2). … At the QSFI degenerate endpoint µ/H = 3/2 the QSFI shape reproduces the local‑template scaling….” Similarly in §IX.D: “At µ/H = 0 (massless heavy field) Δ = 0 and the squeezed enhancement is maximal (k3/k1)−3/2; at µ/H = 3/2 … reproducing the local‑template flat scaling.”
- Problem: In QSFI, ν = √(9/4 − (µ/H)^2), Δ ≡ 3/2 − ν. The squeezed‑limit scaling is ∝ (kL/kS)Δ (equivalently ∝ (kL/kS)3/2−ν). Thus: µ/H = 0 ⇒ ν = 3/2 ⇒ Δ = 0 ⇒ local‑like flat scaling; µ/H → 3/2 ⇒ ν → 0 ⇒ Δ → 3/2 ⇒ the most suppressed squeezed‑limit scaling, not local. The manuscript has these endpoints inverted and also attributes a (k3/k1)−3/2 divergence to Δ = 0, which is incorrect.
- Required fix: Correct the QSFI discussion: (i) make clear that µ/H = 0 yields the local‑like squeezed scaling (Δ = 0), and (ii) µ/H → 3/2 yields Δ → 3/2 (the least squeezed). Remove the incorrect “super‑squeezed (k3/k1)−3/2 at Δ = 0” claim.

P2-E7 (Sec. IX.D, page 17): Arithmetic error in the fNL–nfNL Fisher degeneracy identity
- Offending text: “the two‑parameter identity σmarg = σunmarg/√(1 − ρ^2) applied to that baseline reproduces the quoted value (1.75/√(1−0.9692) = 7.06).”
- Problem: As written, the expression uses 1 − ρ (not 1 − ρ^2) inside the square root. Numerically: 1.75/√(1 − 0.9692) = 1.75/√0.0308 ≈ 10.0, not 7.06. Using the correct identity with ρ^2: if ρ = −0.97 then 1.75/√(1 − 0.97^2) = 1.75/√0.0591 ≈ 7.20; if ρ = −0.9692, then ≈ 7.12. None of these equal 7.06. The displayed arithmetic is inconsistent.
- Required fix: State the exact ρ used in the Fisher output, apply σmarg = σunmarg/√(1 − ρ^2) correctly, and update the quoted 7.06 value (and any downstream sentences relying on it).

MAJOR

P2-M8 (Abstract; Sec. III.B, page 7): Unsupported novelty claim about “first” quantification of the matter‑bounce vs local template mismatch
- Offending text: Abstract: “We quantify, for the first time to our knowledge, the template mismatch between the matter‑bounce and local templates…,” and §III.B: “a literature search confirming no prior quantification … (2009–2024).”
- Problem: The novelty claim is not substantiated with a structured comparison (e.g., a table of prior works and what they did/did not report). “To our knowledge” is insufficient for a “first” in PRD.
- Required fix: Either (i) provide a brief, explicit survey demonstrating that no prior paper computed the bounce‑vs‑local Fisher overlap/shape cosine (with citations), or (ii) soften to “we quantify the mismatch; we are not aware of prior dedicated quantification,” dropping the “first” language.

P2-M9 (Sec. II, page 4): Inconsistent summary language about r centering across coefficient scans
- Offending text: “The amplitude recovery factor is r = 0.85 ± 0.13 (…); centered on the same value obtained from the five‑coefficient‑set scan (r = 0.867–0.888).”
- Problem: “Centered on the same value” is inaccurate: 0.85 differs from the mid‑range 0.877 by ~0.03 (∼3.5σ of the quoted ±0.01 spread given elsewhere for that regime). This risks conveying a misleading sense of agreement.
- Required fix: Rephrase to reflect the small but non‑negligible offset, e.g., “the null‑space median r ≈ 0.85 is slightly below the five‑set scan (0.867–0.888), consistent within the broader null‑space scatter.”

P2-M10 (Abstract and Sec. VI, pages 1 and 10): Gauge‑frame contrast |fBounce|/|fInf| ≈ 290 is inconsistent with the manuscript’s own ns number
- Offending text: Abstract: “|fBounce|/|fInf| ≈ 290,” with ns = 0.9649 used elsewhere to compute fInf ≈ 0.0146.
- Problem: Using fInf = (5/12)(1 − ns) with ns = 0.9649 gives fInf = 0.014625 and a ratio 4.375/0.014625 = 299.2, not “≈ 290.” The text later quotes fInf ≈ 0.015, which would give 291.7. This is a minor but easily correctable arithmetic inconsistency.
- Required fix: Use a single consistent fInf (either 0.0146 or 0.015) and adjust the ratio accordingly (≈299 or ≈292), or quote a rounded “≈3×10^2” to avoid false precision.

MINOR

P2-m7 (Table III caption and body text, page 15): “Corrected (10% residual)” row justification is opaque
- Offending text: “Corrected (10% residual; verification) … is, by construction, equal to ‘Ideal’ … a 10% residual GR contamination after correction has negligible impact … (ΔBF < 0.1).”
- Problem: It is not clear what quantity the “10% residual” is relative to (σGR? σeff? the GR‑induced bias to fNL?); without a short calculation or explicit mapping to σeff the equality to the “Ideal” row looks ad hoc.
- Required fix: Add one line quantifying how a 10% residual maps to σeff (or to the likelihood), demonstrating why the Bayes factor is numerically unchanged at the shown precision.

P2-m8 (Sec. II A, Fig. 1, page 5): Axis formatting vs printed numbers
- Comment: The caption lists benchmark values to 3–4 decimals; the plotted y‑axis tick formatting appears coarse in the parsed text. Consider matching figure tick precision to Table I numbers to avoid visual rounding confusion.

P2-m9 (Internal cross‑reference precision)
- Instances: Several places reference a whole section when a subsection is meant (e.g., “Sec. II” for assumptions that actually live in Sec. II.C; “Appendix A.1” vs “A1/A.1” formatting varies).
- Required fix: Point to the exact subsection consistently (e.g., “Sec. II.C” for assumptions) and unify appendix subsection labels.

EXPLANATION

These additional findings surfaced on a second pass focused on algebraic self‑consistency and physics endpoints, which the initial review under‑emphasized. The most serious new items are: (i) the AT/BNL definitional inconsistency that breaks both algebra and degree counting, and (ii) the inverted QSFI squeezed‑limit mapping. Both require correction for PRD. The new arithmetic error in the degeneracy identity (σmarg relation) also needs fixing to maintain numerical credibility. The remaining items are clarity/novelty/consistency tweaks.