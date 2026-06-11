# P2 R29 — Truth Audit

**Paper version audited**: `research/focused_paper_source_integration/02_full_draft.tex` v1.7.49+EXT1 (post-EXT1 closure wave)
**Audit date**: 2026-06-10
**Auditor**: in-session (Claude Opus 4.7, full repo grep + line-exact `.tex` cross-reference)
**Verdict schema**: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION
**Round-degraded note**: R29 SYNTHESIS flags OpenAI_methodology leg as API-failed; this round does NOT count toward the clean-round counter regardless of closure outcome.

---

## Per-finding verdicts — ESSENTIAL

### R29-P2-E1 (Claude_brutal) — Abstract is a disclaimer-list, not a paper-front
- **Verdict: VERIFIED.**
- **Evidence**: `02_full_draft.tex` L304–306 is a single `\begin{abstract}`…`\end{abstract}` paragraph (one `\par`). Word count ≈ 700; nested parentheticals are 3-deep around the basis-dependence qualifier; tone-switches "sensitivity recast" vs "headline forecast" vs "convention sensitivity should be resolved" are all present in the same paragraph. Both the F14 deferral (abstract length) and the EXT1 caveat-stuffing (F2/F4/F9/C3) directly compounded this.
- **Fix scope (PHASE 2)**: rewrite the abstract to consolidate caveats into 1–2 graceful sentences while preserving ALL informational content (Houston directive: "must read as a confident scoped result, not a disclaimer list"). NOT a two-paragraph split (the reviewer's recommendation), per Houston's tone instruction.

### R29-P2-E2 (Claude_brutal) — Title still says "and Forecasts" while body disclaims forecast
- **Verdict: VERIFIED.**
- **Evidence**: Title L19–20 reads "SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook"; §spherex L449 reads "This makes the present work a sensitivity recast rather than an independent forecast." §megamapper L466 reads "should be understood as illustrative of what a Stage-V spectroscopic survey *could* achieve, not as commitments." So neither SPHEREx nor MegaMapper analysis is a "forecast" in the body's own usage. Title-vs-body mismatch real.
- **Fix scope**: drop "and Forecasts" from title (cheaper surface than rewriting both §spherex + §megamapper). One-token edit.

### R29-P2-E3 (Claude_brutal) — §spherex covariance OOM is dimensionally inconsistent
- **Verdict: VERIFIED.**
- **Dimensional check (auditor-redone)**: Cosmological convention used throughout this paper: $P_\zeta(k)$ has units $[k^{-3}]$ (it's the bare power spectrum, not the dimensionless $\Delta_\zeta^2$). $V_{\rm survey}$ has $[k^{-3}]$. $\delta k$ has $[k]$. So $V_{\rm survey}\,\delta k$ has $[k^{-2}]$. Then $P_\zeta(k)/(V_{\rm survey}\,\delta k)$ has $[k^{-3}]/[k^{-2}] = [k^{-1}]$ — NOT dimensionless. Multiplying by dimensionless $\fnl^2$ does not fix this. The claim "$\lesssim 10^{-3}$" is therefore not derivable from the printed expression at L447.
- **Honest replacement**: the dimensionally correct OOM is
  $$ \frac{\delta C}{C} \;\sim\; \fnl^2 \, \Delta_\zeta^2(k) \;\Big/\; N_{\rm modes}(k), $$
  where $\Delta_\zeta^2 \equiv k^3 P_\zeta/(2\pi^2) \approx 2.1\times 10^{-9}$ (dimensionless) and $N_{\rm modes}(k) \sim V_{\rm survey}\,k^2\,\delta k / (2\pi^2)$ (dimensionless mode count). At $\fnl \sim -4.4$, $\fnl^2 \Delta_\zeta^2 \sim 4\times 10^{-8}$ — well below $10^{-3}$ even without dividing by $N_{\rm modes}$. So the bound $\lesssim 10^{-3}$ holds comfortably; only the formula is broken.
- **Cross-finding M7 (Claude_brutal)**: also flags inconsistency between "$\lesssim 10^{-3}$" and "$<1\%$" propagated. With $\delta\sigma/\sigma \sim \tfrac{1}{2}\delta C/C$, $\delta C/C \lesssim 10^{-3} \Rightarrow \delta\sigma/\sigma \lesssim 5\times 10^{-4}$, much tighter than $1\%$. Fix should reconcile this in one sentence.
- **Fix scope**: rewrite L447 with the dimensionless form; quote one consistent bound for the propagated $\sigma$ shift.

### R29-P2-E4 (Claude_brutal) — §assumptions fermion-suppression bound dimensionally inconsistent
- **Verdict: PARTIAL — dimensional claim FALSIFIED; lack-of-derivation claim VERIFIED.**
- **Dimensional check (auditor-redone)**: In natural units ($\hbar = c = 1$), $[G] = [M_{\rm Pl}^{-2}]$ and $[m_\psi^2] = [M_{\rm Pl}^2]$. Therefore $G\,m_\psi^2$ is dimensionless. $\gamma_{\rm BI}^2$ is dimensionless. So $\gamma_{\rm BI}^2 / (16\pi G m_\psi^2)$ is **dimensionless**. Multiplied by dimensionless $\rho_F/\rho_S$ gives a dimensionless $\Delta\fnl$. The reviewer's chain ("[mass]² / [mass]² · [length]⁻² = [length]⁻²") double-counts the same dimensionful constant in two inequivalent unit systems. **The dimensional inconsistency claim is FALSIFIED.**
- **What IS verified**: the expression has no derivation. No equation links the four-fermion operator $\langle\bar\psi\gamma^5\gamma^a\psi\rangle^2$ to a contribution $\sim \gamma_{\rm BI}^2/(16\pi G m_\psi^2)$ at the cubic-action level. The combinations $G m_\psi^2$, $\gamma_{\rm BI}^2$, $\rho_F/\rho_S$ are physically plausible building blocks for an Einstein-Cartan-Holst four-fermion contact term, but the paper writes them down without a derivation chain.
- **Fix scope (PHASE 2, per /never-fabricate-derivation)**: do not fabricate a derivation we cannot honestly defend. Replace the explicit-formula sentence with an explicit labeled-assumption sentence — e.g. "*A rigorous OOM bound from the contracted Einstein-Cartan-Holst cubic action with fermion sources is not undertaken here; we treat assumption (f) as an external constraint to be checked on a per-model basis.*" This is always acceptable (Houston directive) and avoids the over-claim of "we computed an OOM bound" when we did not.

### R29-P2-E5 (Claude_brutal) — Assumption (d) is weakest link but headline forecast doesn't propagate uncertainty
- **Verdict: PARTIAL.**
- **Evidence verified**: assumption (d) caveat IS present in abstract (L305: "verified only at linear order"); §UV-completion L391 names it as such; §assumptions L395 says "Assumption~(d) is the weakest link"; BF table uses delta + Gaussian $\sigma_{\rm theory}=1.0$ priors (L544 Table III). The reviewer's claim that a $\sigma_{\rm theory}=2.0$ Gaussian gives BF~6 broad / BF~4 narrow is consistent with L546.
- **What's PARTIAL**: the reviewer's "structurally cannot accommodate (d) failure" claim is overstated — the paper's `Bayes-factor closure against the QSFI continuum` paragraph L560 and the $\sigma_{\rm theory}$ sensitivity row L546 ARE the (d)-uncertainty marginalization, just labeled in terms of $\sigma_{\rm theory}$ rather than "(d)-uncertainty". The mapping is one-to-one for symmetric Gaussian priors. So the Bayes-factor calculation is not "wrong" if (d) fails by O(1) — it would be the $\sigma_{\rm theory} = 1.0$ row already reported.
- **What IS verified**: the abstract's "$\mathrm{BF}\,{\sim}\,10$–$17$" envelope is the $r\to 1$ bookkeeping (L558) AND uses the headline $\sigma_{\rm theory}=1.0$-to-delta range; it does NOT inherit the assumption-(d) caveat into the BF interpretation. Combined with M3 (abstract BF endpoint $r\to 1$ vs. body $r=0.84$ giving BF~9–14), the abstract overstates the bookkeeping consistency.
- **Fix scope**: scoping covers what the reviewer asks for — no additional `\sigma_{\rm theory}` row is needed. The MAJOR M3 fix (BF abstract bookkeeping → match body $r=0.84$ → quote $\sim 9$–$14$) handles the actual user-facing inconsistency. Address E5 as part of the E1 abstract consolidation: the (d) caveat should ride alongside the BF qualifier, not as a separate caveat.

---

## Per-finding verdicts — MAJOR (individual)

### R29-P2-M1 (Claude_brutal) — Wick orbit-count "6/3=2" asserted, not derived
- **Verdict: VERIFIED.**
- **Evidence**: L347 footnote claims "(7,2,0) orbit in Cai et al.'s single-time-ordering normalization carries a factor of 3 (three distinct ordered assignments of the momentum labels)" — but the phrase "three distinct ordered assignments" is not standard Wick terminology and no Cai-et-al equation is cited for the factor of 3.
- **Derivation (auditor)**: For the partition $(7,2,0)$ — three distinct exponents, one of which is zero — the $S_3$ orbit under permutation of the three momentum labels $(k_1,k_2,k_3)$ has size $|S_3| / |{\rm stab}(7,2,0)| = 6/1 = 6$. The six ordered monomials are $k_1^7 k_2^2, k_1^7 k_3^2, k_2^7 k_1^2, k_2^7 k_3^2, k_3^7 k_1^2, k_3^7 k_2^2$.
   In Cai et al.'s single-time-ordering convention, the in-in integrand carries only ONE of the two complex-conjugate orderings ("$+$" only, not "$+$" + "$-$"). The cyclic-permutation subgroup of $S_3$ has order 3, and Cai et al.'s explicit monomial in their Eq.~(37) carries the three cyclic images $k_1^7 k_2^2 + k_2^7 k_3^2 + k_3^7 k_1^2$ (the $C_3$ orbit of the ordered tuple, not the full $S_3$ orbit). After in-in commutator doubling ($-2\,\mathrm{Im}$), the doubled integrand carries the full $S_3$ orbit (6 terms). The per-orbit prefactor ratio is therefore $|S_3| / |C_3| = 6/3 = 2$. **Derivation valid; needs one footnote sentence stating this explicitly.**
- **Fix scope (PHASE 2)**: rewrite the orbit-counting footnote sentence to derive 6/3=2 from cyclic-vs-full-S_3 in one line, rather than assert "three distinct ordered assignments" without source.

### R29-P2-M2 (Claude_brutal) — Zenodo checklist enumeration vs paper's named artifacts
- **Verdict: HOUSTON-DECISION.**
- **Evidence**: This is an artifact-bundle audit that requires opening `ZENODO_RELEASE_CHECKLIST.md` and comparing to the paper's 10 named artifacts. It's a real risk but is a pre-submission engineering check, not a paper-edit; defer to a later artifact-link-verify pass.

### R29-P2-M3 (Claude_brutal) — Abstract BF~10–17 envelope vs body $r=0.84$ bookkeeping BF~9–14
- **Verdict: VERIFIED.**
- **Evidence**: L558 explicitly states "the abstract envelope $\mathrm{BF}\,{\sim}\,10$–$17$ correspondingly reads ${\sim}\,9$–$14$ in strict bounce-amplitude bookkeeping" — i.e. the paper acknowledges the mismatch. Abstract L305 quotes only the $r\to 1$ endpoint. The rest of the paper's headline significance ($5.2$–$5.5\sigma$) is reported at the noise-weighted $r = 0.84$ endpoint (L451, L361). So significance and BF are reported in different bookkeeping bookends.
- **Fix scope**: as part of the E1 abstract consolidation, either rebook the abstract BF range to $\sim 9$–$14$ (matching the significance bookkeeping) or add one inline clause noting the bookkeeping choice. Prefer the former (matches the rest of the paper).

### R29-P2-M4 (Claude_brutal) — Abstract BF envelope overstates body's "illustrative" framing
- **Verdict: VERIFIED.** Body L533, L702 explicitly call the BF values "upper bounds … not as robust model-selection evidence" / "illustrative". Abstract does not inherit this caveat. Fix: one short inline qualifier in the abstract beside the BF range. Folded into E1 consolidation.

### R29-P2-M5 (Claude_brutal) — §spherex shot-noise caveat is a standalone-reader orphan
- **Verdict: PARTIAL.** L451 quotes a ${\sim}10$–$20\%$ improvement from anomaly tracers; L453 says shot noise would impose a $15$–$30\%$ degradation on the same tracers. L453 already states "the ${\sim}10$–$20\%$ improvement … should be interpreted as an upper bound until a shot-noise-corrected Fisher matrix is computed" — so the caveat IS self-contained, just placed in a separate paragraph. PARTIAL: net-effect summary sentence would help but is not a blocker.
- **Fix scope**: optional minor; defer.

### R29-P2-M6 (Claude_brutal) — Fig. 4 caption/PNG "BOUNCE EXCLUDED" verification
- **Verdict: HOUSTON-DECISION.** Requires opening the rendered PNG; out of scope for a no-compile audit. Defer to /latex-audit on next recompile.

### R29-P2-M7 (Claude_brutal) — "$\lesssim 10^{-3}$" vs "$<1\%$" $\sigma$-propagation inconsistency
- **Verdict: VERIFIED.** Same site as E3; will be fixed in the E3 edit pass (single consistent bound).

### R29-P2-M8 (Claude_brutal) — Four inline `[Correction note: …]` insertions
- **Verdict: VERIFIED.** Confirmed: L560 (§QSFI endpoint reversal), tab:gr caption (L606 area), SDB joint Fisher (L683 area), QSFI second endpoint (L683 area). The reviewer flags it as a HOUSTON-DECISION item (F25 deferred); not a publication blocker but cosmetically degrading.
- **Fix scope**: defer (HOUSTON-DECISION). Consolidation into a single Errata footnote is a clean fix when Houston wants it; out of scope for this pass.

---

## Per-finding verdicts — MAJOR (cross-vendor, individual)

### Gemini P2-E1 — Abstract claims "additively in quadrature" while r and b_phi are multiplicative
- **Verdict: PARTIAL/OPINION.** The body does use additive-quadrature for some sources (§systematics) and multiplicative for $r$ (Eq. projection). The abstract's "additively in quadrature" caveat is accurate-with-elision; the EXT1-closure-added caveat already labels this as such. The "additively in quadrature" language describes the σ-budget combination, not the projection step. Not a publication blocker; one phrase tweak would close it, but folded into E1 abstract consolidation.

### Gemini P2-E2 / Grok P2-E3 / OpenAI P2-E18 / META P2-META-M4 — Table III correction notes + headline BF
- **Verdict: PARTIAL.** The `[Correction note]` issue maps to M8 above (HOUSTON-DECISION). The headline-vs-recommended BF issue maps to M3 + M4 above (VERIFIED, folded into E1).

### Gemini P2-M2 — Template mismatch r=1 vs r-corrected BF bookkeeping
- **Verdict: VERIFIED (= M3).** Same finding as Claude_brutal M3, already covered.

### Gemini P2-M3 — "First-of-kind" novelty claim too strong
- **Verdict: OPINION.** N3 (first-of-kind demonstration) claims must obey /never-claim-n4 ceiling. Abstract says "for the first time to our knowledge, the template mismatch"; OpenAI P2-M7 cites Byrnes-Langlois-Vernizzi 2010 as a competing claim. Without a literature-search-log artifact (F19, also m5 in Claude_brutal), the claim is unverifiable. Houston-decision-adjacent.
- **Fix scope**: as part of E1 abstract consolidation, downgrade "for the first time to our knowledge" to "to our knowledge" (already present in body); /never-claim-n4 compliant.

### Gemini P2-M4 — Insufficient detail on headline 3–5σ derivation
- **Verdict: STALE/PARTIAL.** §systematics provides the per-component breakdown; the headline range comes from the table aggregation. PRD-acceptable as written; the reviewer's request is a stylistic preference. OPINION.

### Grok P2-E1 — Abstract "σ(fNL)≈0.7 from SPHEREx" is the Heinrich-et-al headline, not the bounce-template-corrected value
- **Verdict: VERIFIED.** L451 explicitly distinguishes optimistic 5.5σ (r=0.876) from noise-weighted 5.2σ (r=0.83). Abstract conflates them under "bispectrum-only 5.2–5.5σ is the headline forecast of this paper". Fix: covered by E1 consolidation.

### Grok P2-E2 — "Realistic range 3–5σ" already includes GR + b_phi + r bookkeeping
- **Verdict: VERIFIED.** §VII confirms this. Abstract elides. Fix: covered by E1 consolidation.

### Grok P2-M1 — Assumption (d) cubic-order verification missing
- **Verdict: VERIFIED (= E5).** Same as Claude_brutal E5; abstract caveat present, body cubic-OOM scaling estimate L395 is "not a derived bound" (the paper itself says so).

### Grok P2-M2 / Gemini P2-M1 / OpenAI P2-M1 — Paper length (25 pages too long)
- **Verdict: OPINION.** PRD page limit not formally violated; reviewer preference for "Brief Report" framing. Not blocking. OPINION.

### Grok P2-M3 — Fig. 2 error-bar interpretation
- **Verdict: PARTIAL.** Fig. 2 caption (L458) was flagged by Claude_brutal m4 as overlong. Edit-overlap: shortening Fig. 2 caption per m4 also addresses Grok's "make explicit" request if we keep the right pointer to §systematics.

### META-E1 — Eqs. (1)–(2) algebraic cancellation of P
- **Verdict: FALSIFIED.**
- **Evidence**: Eq. (2) at L342–343 reads $\BNL = (10/3)\,A_T/\sum_i k_i^3$, NOT $(10/3)\,P/(A_T \sum_i k_i^3)$ as META-E1 transcribes. Re-reading the meta-reviewer's quote: "BNL ≡ (10/3) P / [AT Σi k_i^3]". The actual paper writes $A_T/\sum_i k_i^3$ in the numerator. The meta-reviewer mis-read the equation. Substituting Eq. (1) $A_T = (3/256) k_1^2 k_2^2 k_3^2 P$ into the (correct) Eq. (2) gives $\BNL = (10/3)(3/256) k_1^2 k_2^2 k_3^2 P / \sum_i k_i^3$ — P does NOT cancel; it remains in the numerator. The polynomial $(c_1,\ldots,c_6)$ dependence is preserved through P. **META-E1 is FALSIFIED by direct re-reading of the .tex.**
- **Fix scope**: no edit needed.

### META-E2 — 2D KSW estimator + 3D SPHEREx noise inserted as cross-check
- **Verdict: VERIFIED.** L363 confirms: "tiled flat-sky patches covering the full sky" + "SPHEREx photometric-z power spectra as the diagonal noise covariance". The text already labels it as "not a full simulation pipeline" but still uses r_meas = 0.90 ± 0.01 as a supporting cross-check.
- **Fix scope**: per Houston directive — verify whether BF arithmetic actually needs (d)-propagation or whether scoping covers it. Scoping covers it: the injection-recovery test is labeled as a consistency check, not the headline number; the headline $r = 0.84$ comes from the noise-weighted Fisher overlap, NOT from injection-recovery. Edit minimum: replace the cross-check paragraph's claim with a label "indicative consistency check; not a 3D pipeline validation" — one-line edit. Defer to M5-class minor pass; not blocking E1/E2/E3/E4/M1 priority.

### META-M1 — Vertex symmetry-factor 1/Sv (= M1 above, same finding)
- **Verdict: VERIFIED (= M1).** Same fix as Claude_brutal M1.

### META-M2 — "Basis-independent shape cosine" wording
- **Verdict: VERIFIED.** Abstract uses "basis-independent" for r_cos; the right word is "measure-independent" (or "fixed-coefficient invariant"). Already partially addressed in L351 ("not invariant under linear reparametrizations") for r but not for r_cos. One-word fix in E1 abstract consolidation; replace "basis-independent" → "stable across the same sampling measure" or similar.

### META-M3 — w∝k² as "CMB Fisher" mislabeling
- **Verdict: PARTIAL/OPINION.** L351 already says it's a "stated convention" weight; calling it "Fisher" is schematic. One-word tweak ("Fisher" → "Fisher-style" or "schematic Fisher") would close it.

### META-M4 — BF vs SSFSR omits n_s marginalization
- **Verdict: VERIFIED, scoping-covered.** SSFSR's $\fnl \approx 0.015$ has a finite spread from Planck's $\sigma(n_s) \approx 0.0042$ — about $\pm 0.002$ in $\fnl$. The matter bounce sits at $\fnl = -4.375$ in the same units; the SSFSR competitor likelihood width from $n_s$-marginalization is $\sim 5000\times$ smaller than the bounce-vs-SSFSR separation. The δ(SSFSR) treatment is therefore quantitatively indistinguishable from the n_s-marginalized version at the precision the abstract reports ("$\gg 1$" in the SSFSR column). **OPINION at the abstract level.** No edit needed for headline; could be a one-sentence note in §bayesian.

### META-M5 — Squeezed-vs-folded dominance contradiction
- **Verdict: VERIFIED.** L351 + surrounding paragraphs do read as contradictory without the weighting-scheme separator. Not blocking; minor clarifying-clause fix in §benchmark; defer.

---

## Batched MINOR + NIT verdicts

Batched per Houston directive. Coverage:

| Finding | Verdict | Action |
|---|---|---|
| Claude m1 (abstract length 700 words) | VERIFIED, sub-of-E1 | folded into E1 |
| Claude m2 (verb-tense linear-order cite) | NIT | defer |
| Claude m3 (SPHEREx timeline mismatch) | VERIFIED | one-line fix during E1 |
| Claude m4 (Fig. 2 caption too long) | VERIFIED | defer, cosmetic |
| Claude m5 (literature-search-log) | HOUSTON-DECISION | defer (= F19) |
| Claude m6 (eps/n_s consistency math) | VERIFIED-CLEAN | no fix |
| Claude m7 ("not aware of tensions" weak) | NIT | defer |
| Claude m8 (BF formatting) | NIT | defer |
| Claude m9 (MegaMapper design-dependent in abstract) | PARTIAL | fold into E1 |
| Claude m10 (13% vs ±0.13) | VERIFIED-CLEAN | no fix |
| Claude N1/N2/N3 | NIT | defer |
| OpenAI P2-E11/12/13 (r quoted as 0.84±0.02 but range 0.829–0.876) | VERIFIED minor | language tweak in abstract; fold into E1 |
| OpenAI P2-E14 (3–5σ uses optimistic σ=0.7) | PARTIAL | the σ propagation in §systematics IS consistent; reviewer misreads |
| OpenAI P2-E15 (Fig. 2 bar-heights mismatch) | HOUSTON-DECISION | requires PNG audit |
| OpenAI P2-E16 (Eq. 1 dimensions) | FALSIFIED | $\BNL$ is dimensionless by construction per L345; reviewer misreads |
| OpenAI P2-E17 (κ_ε sign) | FALSIFIED | math check L246-251 confirms sign correct; reviewer error |
| OpenAI P2-E19 (Hermiticity) | OPINION | technically true that sum-of-vertices argument is the right framing; defer |
| OpenAI P2-M7 (Byrnes-Langlois-Vernizzi 2010 cite) | PARTIAL | weaken novelty wording per E1 consolidation handles it |
| OpenAI P2-M8/M9/M10/M11 + m1–m7 + n1–n5 | mix of NIT + STALE | defer or fold into E1 |
| Gemini P2-E2 (correction notes in body) | VERIFIED = M8 | defer (HOUSTON-DECISION) |
| Grok N1/N2/N3 | NIT | defer (date is current; "future date" is FALSIFIED — paper dated June 10, 2026, today is 2026-06-10) |
| Perplexity legs (0 findings) | n/a | no action |

---

## OPINION / HOUSTON-DECISION list (deferred this round)

- **OPINION**: Gemini M3 (novelty wording — already softened to /never-claim-n4 ceiling in E1 fix); Gemini M4 (insufficient breakdown — reviewer preference); Grok M2 / Gemini M1 / OpenAI M1 (paper length — preference); META-M3 (Fisher-vs-toy labels — schematic-acceptable); META-M4 (n_s marginalization — quantitatively negligible at abstract precision); OpenAI E19 (Hermiticity — true but minor); OpenAI E14 (misread of §systematics propagation chain).
- **HOUSTON-DECISION**: M2 (Zenodo checklist enumeration — defer to artifact-link-verify); M6 (Fig. 4 PNG legend — defer to /latex-audit); M8 (correction-note consolidation — Houston choice on whether to flatten the four notes into an Errata block); m5 (literature-search-log artifact — F19 from prior round); F1 (full vertex-to-vertex derivation — long-deferred rigor gap, not publication-blocking).
- **FALSIFIED**: META-E1 (Eq. 1–2 P-cancellation — meta-reviewer mis-quoted Eq. 2); Claude_brutal E4 dimensional claim (the expression IS dimensionless in natural units; the lack-of-derivation issue is real and addressed); OpenAI E16 (B_NL dimensional analysis — paper L345 derives dimensionlessness explicitly); OpenAI E17 (κ_ε sign — math is correct, verifiable from L246–251); Grok N1 (future date — paper date 2026-06-10 is today).

---

## Phase 2 fix targets (PRIORITY ORDER)

1. **E1** — Rewrite abstract: consolidate caveats into 1–2 graceful sentences; preserve all content; confident scoped result tone. Folds in: E2-adjacent (already addressed at title), E5 (d-caveat), M3 (BF bookkeeping), M4 (BF illustrative qualifier), META-M2 (basis-independent → measure-stable language), Gemini E1 (additive-quadrature phrasing), Gemini M3 (novelty wording), Grok E1/E2 (significance origin disclosure), OpenAI E11/E13 (r notation), Claude m1/m3/m9 (length, timeline, MegaMapper design-dep).
2. **E2** — Drop "and Forecasts" from title.
3. **E3** — Rewrite L447 OOM with dimensionless form ($\fnl^2 \Delta_\zeta^2 / N_{\rm modes}$); reconcile $10^{-3}$ and $1\%$ in one sentence.
4. **E4** — Replace the dimensional expression with an explicit labeled-assumption sentence (the dimensional claim was FALSIFIED, but the derivation does not exist; honest framing per /never-fabricate-derivation).
5. **M1** — Footnote at L347: derive 6/3=2 from $|S_3|/|C_3|$ in one explicit sentence.

No \paperVersion bump. No compile. No commit. Phase 2 begins now.
