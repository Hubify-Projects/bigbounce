# P2 R29 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7 (in-session)`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.49.pdf` md5=b2766266 pages=25
**Input format**: In-session full read of `02_full_draft.tex` v1.7.49+EXT1 (post-EXT1 closure wave) + PDF sibling reference for figure rendering
**Wall time**: in-session (API leg credit-blocked; this leg substitutes per Houston directive)

---

## Scope and method

Full read of the v1.7.49+EXT1 source (line-exact citations below refer to `research/focused_paper_source_integration/02_full_draft.tex`). I targeted EXT1-closure stability + the upgraded R29 sweep set (15) abstract-last drift, (16) provenance, (17) uncomputed claims, (18) standalone-reader, (19) effect sizes. No cap on finding count.

Verdicts use the P2-E1-style ID convention. Severity: ESSENTIAL (blocks publication) / MAJOR (must address before submission) / MINOR (should address) / NIT.


## ESSENTIAL findings

### R29-P2-E1 — Abstract is now a disclaimer-list, not a paper-front

**Refs:** `02_full_draft.tex` L304–306 (single-paragraph abstract).
**Quote (excerpt):** "...giving template-corrected significance ${\sim}\,3$--$5\sigma$ after the combined systematic budget (noise-weighted shape mismatch, $\epsilon$-correction, polynomial-coefficient null-space amplitude scatter $\pm 0.13$ absolute in $r$ (basis-dependent: indicative of the null-space spread under the stated symmetrized monomial convention; a different basis choice yields a different scatter, while the shape-cosine stability $r_{\cos} > 0.95$ is basis-independent --- see \S\ref{sec:benchmark}; corresponding to ${\sim}15\%$ relative scatter at $\bar r=0.85$, range $0.55$--$1.14$) from the underdetermined $c_1$--$c_6$ benchmark, photometric-$z$ degradation, PNG bias, $b_\phi$ marginalization, and relativistic projection uncertainties; the systematic budget is propagated additively in quadrature rather than through a joint marginalized Fisher matrix, which would require a full multi-parameter forecast beyond the scope of this sensitivity recast)..."

**Finding:** The EXT1-closure F2/F4/F9/C3 sweep stuffed four nested caveat parentheticals into a single sentence in the abstract that is now 14 lines of dense uninterrupted prose with parentheticals nested 3 deep (basis-dependent → ($r_{\cos}>0.95$ basis-independent → see §benchmark → 15% relative scatter at $\bar r=0.85$, range 0.55–1.14)). A first-time PRD reader cannot extract the headline result in one read. The dispositional shift from "results-first" to "caveats-first" is real: caveats now occupy more abstract real-estate than results.

**Coherence check:** The caveats are individually defensible but collectively contradictory in tone. Abstract simultaneously claims (i) "sensitivity recast rather than an independent forecast" (humble) AND (ii) "$5.2$--$5.5\sigma$ as the optimistic case" (assertive) AND (iii) "bispectrum-only $5.2$--$5.5\sigma$ is the headline forecast of this paper" (committed) AND (iv) "convention sensitivity should be resolved before SPHEREx data are interpreted" (open-question). A reader cannot tell what the paper is actually claiming: a sensitivity recast, a headline forecast, or a contingent forecast pending unresolved convention.

**Fix:** Split the abstract into two paragraphs (this is F14 deferred — but F14 is now ESSENTIAL, not deferred):
- **Para 1 (results-first):** the prediction $-35/8$, the SPHEREx headline $3$–$5\sigma$ post-systematic and $5.2$–$5.5\sigma$ optimistic, the bounce-vs-inflation discriminator ratio, the Bayes factor envelope.
- **Para 2 (qualifications):** sensitivity-recast framing, assumption-(d) caveat, basis-dependence note, quadrature-budget note, convention-ambiguity halving.

This is the minimum surgical fix. The abstract as it stands fails the journal-reader test.

### R29-P2-E2 — Title still asserts a "Forecast" the body explicitly disclaims

**Refs:** Title L19–20 vs body L449 (§sec:spherex).
**Quote (title):** "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook"
**Quote (body L449):** "This makes the present work a sensitivity recast rather than an independent forecast."

**Finding:** EXT1 F6 closure inserted "Sensitivity Recast" into the title but kept "and Forecasts" plural and added MegaMapper. The title therefore claims both a sensitivity recast AND forecasts. The body explicitly disclaims being an independent forecast in §spherex; §megamapper L466 says the MegaMapper projections are "illustrative of what a Stage-V spectroscopic survey \emph{could} achieve, not as commitments." So neither the SPHEREx nor MegaMapper analysis is genuinely a "forecast" in the body's own definition; both are recasts/outlooks. The title's "and Forecasts" is internally inconsistent with how the body uses the word "forecast."

**Fix:** Drop "and Forecasts" from the title. Three workable options:
1. "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"
2. "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Sensitivity Recast and MegaMapper Outlook"
3. "...SPHEREx Sensitivity Analysis and MegaMapper Projections" (uses different word)

Recommend Option 1 — singular, mirrors body language exactly.

### R29-P2-E3 — Uncomputed OOM claim §spherex: dimensional analysis incomplete

**Refs:** L447 §spherex (the F27 closure insertion).
**Quote:** "the fractional covariance correction is $\sim \fnl^2 P_\zeta(k) / (V_{\rm survey} \delta k) \lesssim 10^{-3}$, well below the percent level..."

**Finding:** The expression $\fnl^2 P_\zeta(k) / (V_{\rm survey}\,\delta k)$ is dimensionally not a fractional correction. $P_\zeta$ has units of volume (or is dimensionless depending on convention — here $\mathcal{P}_\zeta$ is dimensionless ~$2\times 10^{-9}$ but the bare power spectrum $P_\zeta(k)$ has $[k]^{-3}$ in standard cosmological convention). $V_{\rm survey}$ has $[k]^{-3}$ and $\delta k$ has $[k]$, so $V_{\rm survey}\,\delta k$ has $[k]^{-2}$, while $P_\zeta(k)$ has $[k]^{-3}$. The ratio $P_\zeta(k)/(V_{\rm survey}\,\delta k)$ therefore has $[k]^{-1}$ — not dimensionless. Multiplying by $\fnl^2$ (dimensionless) does not fix this.

The intended scaling is presumably the inverse mode count $1/N_{\rm modes}(k)$ where $N_{\rm modes}\sim V_{\rm survey}\,k^2\,\delta k/(2\pi^2)$, combined with the dimensionless power $\mathcal{P}_\zeta(k) = k^3 P_\zeta(k)/(2\pi^2)$. The correct dimensionless OOM estimate would read something like $\fnl^2\,\mathcal{P}_\zeta(k)/N_{\rm modes}(k)$ or $\fnl^2\,\mathcal{P}_\zeta(k)\,(k\,L_{\rm survey})^{-3}$ depending on which mode count regularization is used.

At $\fnl\approx -4.4$, $\mathcal{P}_\zeta\sim 2.1\times 10^{-9}$, $k\sim 0.05\,h/\rm Mpc$, $V_{\rm survey}\sim (10^3\,h^{-1}\rm Mpc)^3$ → $\fnl^2\mathcal{P}_\zeta\sim 4\times 10^{-8}$, $N_{\rm modes}(k\sim 0.05)\sim 10^4$, so $\fnl^2\mathcal{P}_\zeta/N\sim 4\times 10^{-12}$. The actual fractional correction is therefore far smaller than the quoted $10^{-3}$ — but the formula as written is dimensionally wrong and the numerical bound $\lesssim 10^{-3}$ is not derivable from it.

**Fix:** Either (a) write the dimensionally correct estimate $\fnl^2\,\mathcal{P}_\zeta/N_{\rm modes}$ with an explicit $N_{\rm modes}$ value at the relevant $k$, or (b) drop the OOM expression and replace with a citation to the literature value for the leading non-Gaussian covariance correction (Sefusatti et al. or Chan & Blot, depending on context).

### R29-P2-E4 — Uncomputed OOM claim §assumptions: fermion-suppression bound is hand-waved

**Refs:** L395 §sec:assumptions (the F29 closure insertion).
**Quote:** "the four-fermion operator contributes $\Delta\fnl \sim (\rho_{\rm fermion}/\rho_{\rm scalar}) \times (\gamma_{\rm BI}^2 / 16\pi G m_\psi^2)$ at the cubic-action level"

**Finding:** This expression is dimensionally inconsistent. $\gamma_{\rm BI}^2$ is dimensionless. $G$ has $[\rm length]^2$ in natural units (or $[\rm mass]^{-2}$). $m_\psi^2$ has $[\rm mass]^2$. So $\gamma_{\rm BI}^2/(16\pi G m_\psi^2)$ has $[\rm mass]^2/[\rm mass]^2 \cdot [\rm length]^{-2} = [\rm length]^{-2}$. Multiplying by the dimensionless ratio $\rho_{\rm fermion}/\rho_{\rm scalar}$ gives something with $[\rm length]^{-2}$, not dimensionless $\Delta\fnl$.

The correct scaling for a four-fermion-operator contribution to $\fnl$ should be $\sim \langle\bar\psi\gamma^5\gamma^a\psi\rangle^2/(M_{\rm Pl}^2 H^2) \times (\rho_F/\rho_S)$ or similar — with the right combination of $M_{\rm Pl}$ and $H$ to make it dimensionless. The bound "$\rho_F/\rho_S \lesssim 0.1 \times (16\pi G m_\psi^2/\gamma_{\rm BI}^2)$" inherits the dimensional problem and gives a numerical bound that depends on what units the reader assumes for $G$ and $m_\psi$.

**Fix:** Either (a) replace with a dimensionally consistent estimate $\Delta\fnl \sim (\rho_F/\rho_S)(\gamma_{\rm BI}^2 H^2/M_{\rm Pl}^2 m_\psi^2)^{?}$ — properly derived from the contracted Maldacena cubic action with fermion sources — or (b) honestly label this as a placeholder ("an order-of-magnitude bound has not yet been rigorously derived; we expect $\Delta\fnl \ll 0.1$ when $\rho_{\rm fermion} \ll \rho_{\rm scalar}$ but a derivation is left to follow-up work") rather than offering an explicit but dimensionally inconsistent expression. The current text reads as a derived bound but is not.

### R29-P2-E5 — "Verified only at linear order" assumption (d) caveat now propagates into the headline-significance arithmetic but is still being treated as a parenthetical

**Refs:** Abstract L305 + L391 §UV-completion + L395 §assumptions + L700 §conclusion.
**Quote (abstract):** "...under assumptions (a)--(f), conditional in particular on assumption~(d): faithful third-order bispectrum transmission through the bounce, verified only at linear order..."

**Finding:** Assumption (d) is the weakest link of the paper's central prediction (the paper says so itself, L395). The cubic-order OOM argument quoted at L395 ("$(k\,\eta_{\rm bounce})^2 \sim 10^{-4}$ for modes of observational interest, giving a correction $\delta\fnl \sim 10^{-3}$") is a scaling estimate, not a derived bound — but the abstract and conclusion treat the $\fnl = -35/8$ prediction as the headline number while burying the "verified only at linear order" caveat in a parenthetical. The Bayesian comparison then uses $\fnl = -35/8$ as a delta-function prior, which structurally cannot accommodate the possibility that (d) fails. If (d) fails by O(1), the entire Bayes-factor calculation is wrong.

**Fix:** Either (a) elevate (d) to a top-line abstract claim ("conditional on assumption (d)... whose cubic-order verification is left to follow-up work") on equal footing with the headline number, or (b) propagate a finite (d)-uncertainty into the $\sigma_{\rm theory}$ prior width (currently 1.0; an honest (d)-uncertainty would push this to $\sigma_{\rm theory} \gtrsim 2$, which the paper itself computes gives BF~6 broad / BF~$<4$ narrow — substantially weaker than the headline). Doing nothing about (d) keeps the paper structurally dishonest about its own weakest link.

## MAJOR findings

### R29-P2-M1 — Wick-permutation orbit-count arithmetic in the F31 footnote is asserted, not derived

**Refs:** L347 footnote (the F31 closure insertion, in the §benchmark monomial-basis paragraph).
**Quote:** "the $(7,2,0)$ orbit in Cai et al.'s single-time-ordering normalization carries a factor of 3 (three distinct ordered assignments of the momentum labels), while in our in-in-doubled symmetrized-orbit sum the same term carries a factor of 6, giving a row-entry ratio of $6/3 = 2$"

**Finding:** The arithmetic is internally consistent BUT the source-of-truth for "factor of 3" is not derived. For partition $(7,2,0)$ with three distinct parts, the $S_3$ orbit has size $|S_3|/|\rm stab(7,2,0)| = 6/1 = 6$ — the symmetrized basis factor of 6 is correct.

The "factor of 3" attributed to Cai et al.'s single-time-ordering normalization is asserted as "three distinct ordered assignments of the momentum labels." That phrase is not standard terminology. Three plausible interpretations:
- (a) Three cyclic permutations $(k_1,k_2,k_3) \to (k_2,k_3,k_1) \to (k_3,k_1,k_2)$ — the cyclic subgroup of $S_3$, which has order 3. This is plausible if Cai et al. only sum over cyclic time-orderings.
- (b) Three "distinct" partitions of the (7,2,0) monomial across the three slots $k_1^7 k_2^2 + k_2^7 k_3^2 + k_3^7 k_1^2$ — but this is 3 only if cyclic symmetry is imposed; the full $S_3$ orbit has 6 terms.
- (c) Three transpositions $\times$ 2 internal symmetries — doesn't recover 3 cleanly.

Without specifying which interpretation, the claim "factor of 3" is a placeholder. The ratio $6/3 = 2$ is suggestive but the doubling factor is supposed to come from the $-2\,\mathrm{Im}$ in-in identity (App.~A.1, Eq.~commid), NOT from a Wick-permutation counting argument. The footnote is conflating two distinct factors of 2: (i) the in-in commutator doubling (operator algebra, derived in App.~A.1) and (ii) a per-orbit Wick-permutation ratio (claimed but not derived). If both factors are 2 and they have the same origin, the footnote double-counts; if they are different, the footnote needs to clearly distinguish them.

**Cross-check:** The c9i_epsilon_ratio_check.json artifact is referenced as the numerical verification but the in-paper text doesn't say what number it returns for the (7,2,0) row of the transformation matrix. A reader cannot reproduce the claim from the paper.

**Fix:** Either (a) cite Cai et al.'s exact normalization equation (their Eq.~37 or the equation that defines their per-orbit prefactor) and derive the factor 3 explicitly, or (b) drop the explicit orbit-counting argument and say "the per-orbit ratios are documented in artifact c9i_epsilon_ratio_check.json; they are orbit-dependent and not a global factor of 2" without committing to the specific 3 vs 6 numbers.

### R29-P2-M2 — Provenance: Zenodo DOI placeholder + checklist not yet consistent with paper claim

**Refs:** L709 §Data and Code Availability + `ZENODO_RELEASE_CHECKLIST.md` (sibling file).
**Quote (paper):** "...available at [GitHub URL] and archived at Zenodo (DOI inserted at submission)."

**Finding:** The paper now claims Zenodo archival but the actual DOI is a placeholder. This is acceptable pre-submission only if (i) the checklist is complete enough that the DOI can be inserted by a one-line edit at submission time AND (ii) the README inside the planned Zenodo bundle enumerates every artifact named in the paper. I verified the sibling `ZENODO_RELEASE_CHECKLIST.md` exists but did NOT verify its content matches the paper's named-artifact list. Mismatch risk:

- Paper L709 names 6 explicit artifacts: c9h, c9i, phase3_fisher_overlap.json, null_space_analysis.py, c9j, c9k, c9l (that's 7).
- Paper L347 footnote names c9i_epsilon_ratio_check.json.
- Paper L508 names c9l_sigma_theory_continuous_marginalization.py.
- Paper L590 names c9k_gr_continuous_marginalization.py.
- Paper L606 names c9g_bf_table_recompute.py.
- Paper L806 names appendix_A1_wick_doubling.py.
- §spherex implies c8_fnl_running_fisher.py (referenced as part of §systematics provenance).

That's 10 named artifacts. The Zenodo checklist must enumerate all 10. If even one is missing from the bundle, the post-submission DOI lookup will return an incomplete archive and a reviewer running reproducibility checks will land on missing files.

**Fix:** Verify (and fix the checklist file to reflect) the full 10-artifact list. Add a one-line "Files referenced in this paper:" enumeration block to the Zenodo README so the mapping is one-to-one. The single-source-of-truth gap (paper claims artifacts → checklist may not enumerate them → Zenodo bundle may not contain them) is the kind of post-submission embarrassment that the F18 closure was supposed to prevent.

### R29-P2-M3 — Abstract-vs-body Bayes-factor envelope numerics differ by template-mismatch bookkeeping but the abstract doesn't say so

**Refs:** Abstract L305 (BF~10–17 envelope) vs L558 template-mismatch bookkeeping paragraph.
**Quote (abstract):** "the recommended-to-theoretical-maximum envelope is therefore $\mathrm{BF}\,{\sim}\,10$--$17$"
**Quote (body L558):** "$17.1 \to 14.4$ (delta, broad), $9.8 \to 9.2$ ($\sigma_{\rm theory}=1.0$, broad)... the abstract envelope $\mathrm{BF}\,{\sim}\,10$--$17$ correspondingly reads ${\sim}\,9$--$14$ in strict bounce-amplitude bookkeeping."

**Finding:** The abstract quotes the $r\to 1$ bookkeeping endpoint (BF~10–17). The body explicitly says that under the noise-weighted $r=0.84$ bookkeeping endpoint — which is the bookkeeping the rest of the paper uses for the headline $5.2$–$5.5\sigma$ optimistic significance — the envelope reads BF~9–14. The two endpoints disagree by ~20% on each side.

The abstract should EITHER:
- (a) quote the same bookkeeping endpoint as the headline significance (i.e. BF~9–14 to match the noise-weighted $r=0.84$ used for $5.2$–$5.5\sigma$), or
- (b) flag in the abstract that the BF envelope is the $r\to 1$ endpoint while the significance is the noise-weighted endpoint, and explain why.

Currently doing neither makes the abstract internally inconsistent in its bookkeeping convention: the significance is reported in one bookkeeping, the Bayes factor in another. An expert reader will catch this; the truth-audit table won't because both numbers are individually defensible.

**Fix:** Either rebookkeep the abstract BF to ~9–14 (preferred — matches the rest of the paper) or add one explicit clause: "(at the $r\to 1$ template-overlap bookkeeping endpoint; the noise-weighted $r=0.84$ endpoint gives BF~9–14, see \S\ref{sec:bayesian})."

### R29-P2-M4 — Effect size: the abstract Bayes-factor "envelope" is not a robust model-selection statement

**Refs:** Abstract L305 BF~10–17 + L533 ("upper bounds given the current theoretical uncertainty in the bounce prediction, not as robust model-selection evidence") + L702 conclusion.
**Quote (L533):** "The Bayes factors reported in Table~\ref{tab:bayes} should be interpreted as upper bounds given the current theoretical uncertainty in the bounce prediction, not as robust model-selection evidence."
**Quote (L702 conclusion):** "These Bayes factors are sensitive to the assumed prior widths and model-class definitions (Sec.~\ref{sec:bayesian}); they should be interpreted as illustrative of the discriminating power available, not as definitive model-selection evidence."

**Finding:** The body explicitly disclaims the Bayes factors as "not as robust model-selection evidence" in two places (L533, L702) and "illustrative of the discriminating power available" in the conclusion. But the abstract presents BF~10–17 as a positive scientific result on equal footing with the $\sigma(\fnl)$ forecast. A reader who only reads the abstract gets a stronger claim than the paper makes internally. This is the canonical "abstract overstates body" failure mode that PRD referees flag.

**Effect-size check:** BF~10 on Jeffreys' scale is "strong" evidence; BF~17 is "very strong". The paper's own disclaimer says these should be read as "illustrative" — that's a quantitative downgrade from "strong evidence" to "not definitive." Without the body's caveats inherited into the abstract, the abstract's BF claim is misleading.

**Fix:** Add one inline qualifier in the abstract immediately after the BF~10–17 phrase: "(illustrative of the discriminating power available; see \S\ref{sec:bayesian} for the prior-width and model-class sensitivities that determine the precise value)." This is one sentence that brings the abstract in line with the body's own self-assessment.

### R29-P2-M5 — Standalone reader §spherex shot-noise caveat orphan

**Refs:** L453 §spherex shot-noise caveat block.

**Finding:** The shot-noise caveat says anomaly-selected tracers have $\bar{n} \sim 10^{-5}$ vs the baseline $\bar{n} \sim 10^{-3}$ and "would need to be included in any definitive forecast based on anomaly-selected subsamples." Earlier in the same section (L451) the paper claims a "preliminary Fisher forecast on DESI–SDSS cross-matched anomaly tracers projects a ${\sim}\,10$–$20\%$ improvement in $\sigma(\fnl)$." A standalone reader is left with:
- L451 implies anomaly tracers IMPROVE $\sigma(\fnl)$ by 10–20%.
- L453 caveats that the same anomaly tracers would DEGRADE $\sigma(\fnl)$ by 15–30% due to shot noise.

These two statements are individually defensible (the 10–20% improvement assumes shot noise is already corrected; the 15–30% degradation is the bare shot-noise hit before improvement from independence). But for a standalone reader reading §spherex without §conclusion, the net effect of anomaly tracers is ambiguous: net positive? net negative? net wash? The paper never says.

**Fix:** Add one summary sentence at the end of the shot-noise caveat: "Net effect: combined with the multi-tracer improvement, the $10$–$20\%$ gain quoted above is reduced to ${\sim}\,X\%$ after shot-noise correction; the value depends on the anomaly subsample's number density and bias parameters and is left to follow-up work." Plug in the actual number from the c8 Fisher script, or say "neutral net effect within the current Fisher uncertainties."

### R29-P2-M6 — Fig. 4 caption + EXT1 demoted "BOUNCE EXCLUDED" not reconciled with the legacy "kills live lane" framing

**Refs:** L675 fig:thresholds caption.
**Quote:** "dark red (legend label ``bounce excluded'') --- measurement consistent with zero, disfavoring the quasi-dust matter bounce while remaining consistent with standard single-field inflation"

**Finding:** The "BOUNCE EXCLUDED" label was the M4 closure target in R25conf (per the v1.7.47→48 header). The current caption matches. But the figure file `fig4_decision_thresholds.png` itself may have stale text from before the regeneration. I cannot verify the PNG content from the LaTeX source alone. The figure-rendering audit must include opening the actual PNG (or the PDF page rendering of Fig.~4) to confirm the legend matches the caption.

**Fix:** A latex-audit step opening the PDF at the Fig.~4 page should verify "BOUNCE EXCLUDED" appears in the legend rendering. If the PNG was regenerated but not committed in lockstep with the .tex caption update, the caption-figure mismatch persists. Confirm via `pdftoppm` + visual check.

### R29-P2-M7 — §spherex new OOM bound implies $<1\%$ but it's offered with $\lesssim 10^{-3}$ — order-of-magnitude phrasing inconsistent

**Refs:** L447 §spherex.
**Quote:** "fractional covariance correction is $\sim \fnl^2 P_\zeta(k) / (V_{\rm survey} \delta k) \lesssim 10^{-3}$, well below the percent level, so the linearized Fisher matrix is a reliable approximation at this fiducial and the corresponding fractional shift in $\sigma(\fnl)$ is $< 1\%$."

**Finding:** "$\lesssim 10^{-3}$" is "below the per-mille level," much tighter than "below the percent level." If the bound is genuinely $\lesssim 10^{-3}$, why claim only "$<1\%$" for the propagated $\sigma(\fnl)$ shift? The fractional shift in $\sigma$ from a fractional covariance correction $\delta C/C$ is $\delta\sigma/\sigma \sim \tfrac{1}{2}\delta C/C$, so $\lesssim 10^{-3}$ in $C$ propagates to $\lesssim 5\times 10^{-4}$ in $\sigma$ — well under 0.1%, not 1%. The two bounds are inconsistent.

If the actual goal is to bound $\delta\sigma/\sigma < 1\%$, the covariance fractional correction can be up to ~$2\times 10^{-2}$, much weaker than the quoted $\lesssim 10^{-3}$. The text seems to be quoting both bounds without reconciling them.

**Fix:** Pick one bound and propagate it consistently. The defensible chain is: covariance fractional correction $\lesssim X$ → $\sigma$ fractional correction $\lesssim X/2$ → quote one number. The current text quotes two numbers that don't connect.


### R29-P2-M8 — Correction-note proliferation (4 visible in the body)

**Refs:** L560 §QSFI ("Correction note"), L606 tab:gr caption ("Correction note"), L683 SDB joint Fisher ("Correction note"), L683 second QSFI endpoint ("Correction note").

**Finding:** The paper now carries 4 visible "[Correction note: ...]" inline insertions. These are honest disclosures, BUT they sap reader confidence: a paper that contains 4 inline self-corrections in the published body reads as a still-evolving manuscript, not a finished result. Two of the 4 correction notes (the two QSFI endpoint reversals) are the SAME correction repeated in §bayesian and §discussion — the reader sees the same self-flagged error twice.

This is the HOUSTON-DECISION item F25 deferred from EXT1 — but as the paper accumulates more closure passes, the correction-note count rises monotonically without consolidation. A reader sees a paper that the author themselves keeps catching errors in.

**Fix:** Consolidate the 4 correction notes into a single bulleted "Errata and corrections to prior preprint versions" subsection at the end of §discussion (before §conclusion) or as a footnote on the title page. Remove the inline insertions and replace with a single forward reference: "(see Errata, §X)." The information content is preserved; the visual disposition shifts from "active errata stream" to "completed errata, archived."

## MINOR findings

### R29-P2-m1 — Abstract length: now 14 lines of single-paragraph dense prose (≈700 words)

**Refs:** L304–306.

**Finding:** PRD abstract guideline is ≤500 words; many journals enforce 250. The current abstract is roughly 700 words in one paragraph. Even setting aside the disclaimer-stuffing critique of E1, the raw word count exceeds standard PRD format. Required compression at submission anyway.

**Fix:** The E1 two-paragraph split target should also enforce a 250-word/paragraph ceiling, giving ≤500 words total — a hard PRD-compatible budget.

### R29-P2-m2 — "Verified only at linear order" verb-tense inconsistency

**Refs:** Abstract L305 vs L391 §UV-completion.
**Quote (abstract):** "verified only at linear order"
**Quote (L391):** "verified only at linear order~\cite{WilsonEwing:2012}"

**Finding:** Consistent across the body. NIT-level only — the citation is missing from the abstract instance but present in the body. Either cite at both or neither.

**Fix:** Drop the citation from the body abstract is the cleaner read; add a forward-reference instead.

### R29-P2-m3 — "(launched March 2025; survey data collection through ~2027)" vs "(launched March 2025; first all-sky survey completed December 2025; science data release expected ~2028)"

**Refs:** Abstract L305 vs L655 §discussion staged strategy vs L704 conclusion.

**Finding:** Three different SPHEREx timeline phrasings across the paper:
- Abstract: "survey data collection through $\sim$2027"
- §discussion: "first all-sky survey completed December 2025; science data release expected $\sim$2028"
- §conclusion: "primary survey nominally complete after $\sim$25 months of operations, with the first PNG-suitable public data release expected $\sim$2028"

These are individually defensible but inconsistent. If the science data release is 2028, the abstract's "$\sim$2027" is the wrong reference epoch.

**Fix:** Pick one timeline phrasing and use it uniformly. Recommend "data collection through ~2027, first PNG-suitable release ~2028."

### R29-P2-m4 — Figure caption brevity audit: Fig. 2 is now ~12 lines

**Refs:** L458 fig:surveys caption.

**Finding:** Fig.~2's caption now reads: "Detection significance for $\fnl = -35/8$ across survey configurations. Error bars span the optimistic endpoint (published ideal $\sigma(\fnl)$ with template-overlap correction only) to the conservative endpoint (full \S\ref{sec:systematics} budget: $r=0.84$ overlap, $\epsilon$-correction, photometric-$z$ degradation, PNG bias, $b_\phi$ marginalization, and GR-projection marginalization ($\sigma_{\rm GR}$, Table~\ref{tab:gr})); i.e.\ optimistic-to-conservative ranges accounting for multi-tracer, photo-$z$, bias, and GR systematics." That's a 7-line caption. PRD figures should be ≤3 lines of caption. The information is duplicated from §systematics.

**Fix:** Shorten Fig.~2's caption to: "Detection significance for $\fnl = -35/8$ across survey configurations. Error bars span the optimistic endpoint (template-overlap correction only) to the conservative endpoint (full systematic budget; see \S\ref{sec:systematics})."

### R29-P2-m5 — "(2009--2024)" literature-search bracket is the F19 HOUSTON-DECISION

**Refs:** L435 §template.
**Quote:** "(iii)~a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009--2024)."

**Finding:** F19 was deferred to HOUSTON-DECISION. The claim is unverified without a literature-search-log artifact in the data availability. A standalone reader has to trust the assertion. The right artifact would be a `literature_search_log.md` enumerating the search terms, databases, date, and the null result.

**Fix:** Either (a) commit the literature-search-log artifact and reference it in §Data and Code Availability, or (b) downgrade the claim to "to our knowledge, no prior quantification..." which doesn't require external validation.

### R29-P2-m6 — Eq. consistency: $\fnl(n_s)$ vs $\fnl(\epsilon)$ sign convention check

**Refs:** L638 (Eq. defining $\fnl(\epsilon)$) and L644 (Eq.~consistency).
**Quote (L638):** "$\fnl(\epsilon) = -\frac{35}{8} - \kappa_\epsilon(\epsilon - \tfrac{3}{2}) + \mathcal{O}(\epsilon - \tfrac{3}{2})^2$"
**Quote (L644):** "$\fnl(n_s) \approx -\frac{35}{8} - c'\,(n_s - 1)$ where $c' \equiv \kappa_\epsilon/8 \in [0.7,\,10]$"

**Finding:** Substituting $\Delta\epsilon = (n_s-1)/8$ into the $\epsilon$-form gives $\fnl - (-35/8) = -\kappa_\epsilon\,(n_s-1)/8 = -c'(n_s-1)$. Consistent. At $n_s = 0.9649$, $\fnl - (-35/8) = -c'(-0.0351) = +c'\,(0.0351)$ → $\fnl$ moves toward zero. With $c'\in[0.7, 10]$ this gives a range $\fnl \in [-35/8 + 0.025, -35/8 + 0.351] = [-4.35, -4.02]$, matching the body claim. Math checks. NIT only.

**Fix:** None needed; this is verification.

### R29-P2-m7 — "We are not aware of observational tensions" is a soft empirical claim

**Refs:** L399 §sec:viable.
**Quote:** "We are not aware of observational tensions with this model within current uncertainties."

**Finding:** No citations. The Wilson-Ewing model has known issues with $H_0$ tension and ISW (depending on the specific dark-energy completion). "Not aware" is too soft.

**Fix:** Either drop the sentence or expand to "specifically, the model is consistent with Planck 2018 $n_s$, current $r$ bounds from BICEP, and Planck PR4 $\fnl$ within their respective $1\sigma$ uncertainties; we have not undertaken a comprehensive $H_0$ or ISW comparison."


### R29-P2-m8 — "BF~$\sim X$" vs "BF~$\approx X$" formatting inconsistency

**Refs:** scattered.

**Finding:** The paper uses both $\mathrm{BF}\,{\sim}\,X$ and $\mathrm{BF}\,\approx\,X$ and bare "BF~$X$" in different sites. PRD style prefers one symbol. The semantic difference (~ for order-of-magnitude, ≈ for approximate equality) is being used inconsistently — Table~\ref{tab:bayes} alternates between "$\sim 10$" and "$\sim 17^b$" (with footnote b giving 17.10 to 2 dp).

**Fix:** Standardize on $\mathrm{BF}\approx X$ in tables (where the value is computed to 2 dp from c9g) and $\mathrm{BF}\sim X$ only in prose where the rounding-to-OOM is intentional.

### R29-P2-m9 — §megamapper $3$–$7\sigma$ envelope still labeled "design uncertainty in the instrument concept (survey area, spectral resolution, target selection, and number density) at least as much as measurement uncertainty"

**Refs:** L468.

**Finding:** Honest disclosure, BUT the abstract still quotes "$3$–$7\sigma$ realistic" for MegaMapper without inheriting this caveat. The abstract's MegaMapper range is presented on the same footing as the SPHEREx range, even though the body says the MegaMapper range "should not be interpreted as a well-characterized error bar."

**Fix:** Add one inline qualifier to the abstract: "MegaMapper... could reach... ($3$--$7\sigma$ realistic, design-dependent, conditional on instrument realization and survey funding)..." — adding "design-dependent" reduces the false-equivalence with the SPHEREx range.

### R29-P2-m10 — "13% scatter" vs "$\pm 0.13$ absolute" framing in abstract vs body

**Refs:** Abstract L305 ("$\pm 0.13$ absolute in $r$") vs L361 ("$r = 0.85 \pm 0.13$").

**Finding:** Internally consistent — $\pm 0.13$ in $r$, with $\bar r = 0.85$ giving ~15% relative scatter. The "13%" framing only appears in the abstract parenthetical and §systematics; the §benchmark scan reports the absolute number. Consistent. NIT.

**Fix:** None; this is verification.

## NIT findings

### R29-P2-N1 — `\paragraph{Auxiliary consistency check: cosmic birefringence.}` lacks ending period

**Refs:** L692.

**Finding:** PRD style nit. The `\paragraph` heading ends with a period, but it's also italicized inline (the auxiliary-paragraph next-line text starts with `\textit{(This paragraph is...)}`). Visually clean.

**Fix:** None.

### R29-P2-N2 — `\cite{CaiBrandenberger:2014}` bibkey points at Li et al. — confusing but documented

**Refs:** Multiple sites; documented in the v1.7.47 header.

**Finding:** The bibkey `CaiBrandenberger:2014` actually resolves to the Li et al. 2017 paper (the v1.7.47 closure noted this). A reviewer who only reads the bib will see Li et al. cited as `CaiBrandenberger:2014` everywhere — confusing without the closure history. The bibkey survived the v1.7.47 sweep but the body text refers to "Li \etal" everywhere. This is a documented decision but reads as a bibkey-content mismatch.

**Fix:** Either rename the bibkey to `Li:2017` and update all 17 cite sites, or leave as-is with a single bib-file comment explaining the legacy bibkey. Renaming is the cleaner long-term fix.

### R29-P2-N3 — `\BNL` macro used inconsistently — sometimes bare $B_{\rm NL}$ in text

**Refs:** Most sites use the macro; spot-check L341 uses macro, but the Cai-et-al numerical table footnote uses bare $\BNL^{\rm squeeze}=-35/8$.

**Finding:** Consistent. NIT-level.

**Fix:** None.


## EXT1 closure-stability verification

Per R29 charge, verify the EXT1-closure edits survived as advertised:

- **F6 title change** "SPHEREx Forecasts" → "SPHEREx Sensitivity Recast and Forecasts": HALF-CLOSED. "Sensitivity Recast" inserted, but "and Forecasts" plural retained, creating a new inconsistency with §spherex which explicitly disclaims being a forecast. See R29-P2-E2.

- **F9 abstract assumption-(d) caveat:** PRESENT (abstract L305: "conditional in particular on assumption~(d): faithful third-order bispectrum transmission through the bounce, verified only at linear order"). But the caveat is buried in a nested parenthetical and not propagated into the headline-significance arithmetic. See R29-P2-E5.

- **F2/F28 basis-dependence qualifier on ±0.13 scatter:** PRESENT (abstract L305: "basis-dependent: indicative of the null-space spread under the stated symmetrized monomial convention"). Honest, but contributes to abstract-overload (E1).

- **F3 "sensitivity recast rather than an independent forecast" label:** PRESENT in abstract (L305) AND body (L449). Consistent.

- **F4/C3 additive-quadrature caveat:** PRESENT (abstract L305: "propagated additively in quadrature rather than through a joint marginalized Fisher matrix, which would require a full multi-parameter forecast beyond the scope of this sensitivity recast"). Adds another nested parenthetical to abstract — see E1.

- **F27 §spherex Fisher fiducial-shift bound:** PRESENT (L447). Dimensionally inconsistent as written. See R29-P2-E3.

- **F29 §assumptions fermion-suppression bound:** PRESENT (L395). Dimensionally inconsistent as written. See R29-P2-E4.

- **F31 §benchmark Wick-permutation footnote:** PRESENT (L347 footnote). Arithmetic claim "$6/3 = 2$" is asserted, not derived. See R29-P2-M1.

- **F13 birefringence demotion:** CLOSED. Section now scoped as a single `\paragraph{Auxiliary consistency check: cosmic birefringence.}` block with explicit "headline forecasts independent" label at L693. No orphaned references to the old subsection structure remain (verified via grep; the only other matches are header-comment annotations referring to the closure itself). The basis-cancel chain holds.

- **F18 Zenodo placeholder + checklist:** PARTIAL. The placeholder is in place (L709). The sibling `ZENODO_RELEASE_CHECKLIST.md` exists but its content-vs-paper-claim consistency is unverified. See R29-P2-M2.

**Houston-Decision items deferred from EXT1:**
- F1 (full vertex-to-vertex derivation): still deferred. Not blocking publication but is an outstanding rigor gap.
- F14 (abstract length split): **promoted to ESSENTIAL** in this round (see R29-P2-E1) — deferral is no longer defensible because the EXT1 closure inserts compounded the abstract-overload.
- F19 (literature-search-log artifact): see R29-P2-m5.
- F25 (correction note consolidation): see R29-P2-M8.

## Counts

- ESSENTIAL: 5 (E1–E5)
- MAJOR: 8 (M1–M8)
- MINOR: 10 (m1–m10)
- NIT: 3 (N1–N3)
- Total: 26 findings

## Summary recommendation

**Recommendation: MAJOR REVISION before resubmission.**

**Justification.** The v1.7.49+EXT1 closure wave honestly addressed F2/F3/F4/F6/F9/F13/F18/F27/F29/F31 — closures that move the paper toward publishability on the dimensions the EXT1 reviewers flagged (sensitivity-recast framing, basis-dependence honesty, fermion-suppression caveat, Wick-arithmetic provenance, birefringence demotion, Zenodo provenance). But the closure introduced or left unaddressed five ESSENTIAL items that block submission:

1. **The abstract has become a disclaimer-list (E1).** Four nested caveat parentheticals stuffed into one 700-word paragraph. The headline result is hard to extract on first read. The disposition tone is internally contradictory (humble "sensitivity recast" vs assertive "headline forecast"). This is the F14 HOUSTON-DECISION deferral coming due — it's now a publication blocker, not a deferred item.

2. **The title still says "and Forecasts" (E2)** when the body explicitly disclaims being an independent forecast in §spherex. One-word fix; high payoff.

3. **Two new OOM bounds (F27, F29) are dimensionally inconsistent as written (E3, E4).** They are honest attempts to provide quantitative bounds where prior versions had hand-waves, but the formulae as printed don't carry the dimensions claimed and the numerical bounds quoted ($\lesssim 10^{-3}$ for the Fisher shift, $\lesssim 0.1$ for the fermion contribution) are not derivable from the printed expressions. A PRD referee with first-principles physics training will catch both.

4. **Assumption (d) is the paper's own self-flagged weakest link, but the headline forecast structurally cannot fail under (d) failure (E5).** The Bayes factors use a delta-prior on $\fnl = -35/8$; if (d) fails by O(1), the entire BF calculation is wrong. The recommended $\sigma_{\rm theory}=1.0$ doesn't propagate (d)-uncertainty.

5. **F31 Wick-arithmetic "6/3 = 2" is asserted, not derived (M1).** The "factor of 3" attributed to Cai et al.'s single-time-ordering normalization is plausible but not sourced to a specific Cai-et-al equation. A reviewer cannot reproduce the claim from the paper.

The 8 MAJOR items collectively erode reader confidence: abstract-vs-body BF bookkeeping mismatch (M3), abstract overstates body BF interpretation (M4), 4 inline correction notes (M8), Zenodo checklist-vs-paper enumeration risk (M2). The 10 MINORs and 3 NITs are below the threshold for blocking but should be folded into the same revision pass.

The paper is closer to publication than v1.7.47 was, but EXT1-closure has shifted the failure modes from "missing caveats" to "caveat-overload + new uncomputed expressions" — and both failure modes require a focused surgical pass before this can go out to an external journal-style review (Stage 3 of the three-stage protocol).

**Predicted outcome if the 5 ESSENTIALs + 8 MAJORs are closed cleanly:** v1.7.50+ would be at the readiness threshold for external review. Until then, readiness should oscillate backward from the post-EXT1 high to ~93–94% (consistent with the readiness-cap-99 standing directive: cap at 95% until clean cross-vendor R-round, which this round is not).
