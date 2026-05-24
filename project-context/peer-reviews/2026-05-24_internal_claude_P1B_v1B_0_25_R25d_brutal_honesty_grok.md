# P1B v1B.0.25 — R25d brutal-honesty-Grok verdict

**Reviewer**: Internal Claude, Grok-4.3 brutal-honesty persona (OpenRouter capped → Anthropic-rotated)
**Round**: R25d (round 2-of-3 of a fresh §4.4.1 cross-model streak on v1B.0.25; surgical L345 caption-only delta from v1B.0.24)
**Date**: 2026-05-24
**Protocol**: Read v1B.0.25 top-to-bottom (962 lines), specifically targeting the seven failure modes the prompt enumerated. Cross-check on-disk JSON + SSOT index + prior R25a/b/c findings. Persona = brutal stress-test: assume R25c DeepSeek was too narrowly focused on JSON arithmetic and missed framing/scope/staleness flaws.
**Artifact reviewed**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.tex` (962 lines, v1B.0.25 timestamp 2026-05-24 PDT)

---

## One-line summary

**0 BLOCKER / 2 MAJOR / 3 minor / 2 nit** — v1B.0.25's surgical L345 fix introduces a NEW logical contradiction ("8 cos + 9 nui = 17 total — distinct from k=7+10=17"; both totals equal 17, "distinct" is the wrong word). MAJ-2 from R25a was declared falsified-by-author on the basis that the §V Caveats block carries the unsampled-tail disclaimer, but the "+4.3σ from LCDM" framing still appears in FOUR other locations (Table 1B header, physics-interpretation paragraph, mcmc-inventory caption, cross-paper anchor) without inline qualifier — the disclaimer is buried, the discovery framing is in the headlines. Cross-paper Table I is multi-cron-fire stale AND missing P5 entirely. Six "queued for v1B.0.15+/16+/18+" promises remain in the body of a v1B.0.25 paper.

---

## MAJOR

### R25d-MAJ-1 — v1B.0.25's R25c-MIN-1 surgical fix introduces a NEW logical contradiction: "8 cos + 9 nui = 17 total — distinct from k=7+10=17"

**Severity**: MAJOR (the v1B.0.25 single-line delta was supposed to *close* MIN-1; instead it makes the caption parse as a non-sequitur — the corrected wording asserts "distinct" between two integers that are equal).

**Lines**: L357 (Table 1B caption, the v1B.0.25 R25c-MIN-1 closure).

**Quote** (verbatim):
> Sampled parameter space: 8 cosmological ($\log A$, $n_s$, $\omega_b h^2$, $\omega_c h^2$, $\tau$, $100\theta_{\rm MC}$, $w$, $w_a$) + 9 nuisance ($A_{\rm planck}$, three CamSpec foreground amplitudes, three CamSpec spectral indices, calTE, calEE) **$=17$ total — distinct from the $k=7+10=17$ count** for the frozen $\Lambda$CDM+$\Delta\Neff$ chains in Table~\ref{tab:verification} (R25c-MIN-1 corrected v1B.0.25: prior "$k=7+7=14$" was a stale carry from before R25a-MAJ-1 expanded the cosmological+nuisance enumeration).

**Defect rationale**: The R25c DeepSeek-confab review identified the stale "k=7+7=14" and recommended a single-token surgical fix to either (a) "$k=7+10=17$ count for the frozen chains (see footnote~\ref{fn:rhat_csv})" or (b) explicit prose rewriting if intent was "7 sampled cosmological + 7 derived = 14 cosmological-side params total". The author chose option (a) but left the preceding word "distinct" in place. The result reads "17 total — distinct from k=17". *Numerically these totals coincide.* The two parameter spaces are genuinely structurally different (iter2 samples 8 cosmological including $w$ and $w_a$; frozen samples 7 cosmological with $w$ and $w_a$ held fixed at $\Lambda$CDM; iter2 has 9 nuisance, frozen has 10 nuisance — the two chains differ by which third nuisance is replaced by which cosmological), but the *parameter count* coincides at 17 in both. A brutal reviewer reading this caption parses it as: the author is claiming two parameter spaces are "distinct" by listing two totals that are equal. Either the word "distinct" must change to something accurate ("**comparable in size, structurally distinct**" or "**numerically coincident but structurally distinct**"), or the structural distinction must be made explicit (the iter2 chain samples $w$, $w_a$, $\log A$, $100\theta_{\rm MC}$ as cosmological where frozen samples $\Delta N_{\rm eff}$ and 1 extra Planck nuisance instead). R25c declared "single-token surgical" but the single token was the *number*, not the *adjective* — leaving "distinct from k=17" in the same caption is a textbook own-goal.

**Reproducer**:
```
sed -n '357p' arxiv/paper1b_mcmc_companion.tex | grep -E "distinct from.*k=7\+10=17"
```

**Recommended fix**: replace "distinct from the $k=7+10=17$ count" with one of:
- "numerically coincident with but structurally distinct from the $k=7+10=17$ count for the frozen $\Lambda$CDM+$\Delta\Neff$ chains (which sample $\Delta N_{\rm eff}$ in place of iter2's $w_0, w_a$)"
- or, cleaner: rewrite the entire clause as "same total dimension as the frozen $\Lambda$CDM+$\Delta\Neff$ chains in Table~\ref{tab:verification} ($k=17$) but with a different cosmological-nuisance split (iter2: $8+9$; frozen: $7+10$)"

---

### R25d-MAJ-2 — "+4.3σ from LCDM" discovery framing appears in five locations; only ONE (§V Caveats) carries the unsampled-tail / not-a-Bayes-factor qualifier; the author's R25a-MAJ-2 falsification rested on that single appearance

**Severity**: MAJOR (load-bearing scientific claim; R25a-MAJ-2 was declared FALSIFIED by direct text inspection in the v1B.0.23 changelog (lines 90–94) on the basis that "L584 already includes the R10 GEM-M1 / R7 GPT-B3 caveat". But the +4.3σ framing appears in **five** distinct paper locations — only one carries the inline qualifier; the other four are unmodified discovery-framing. R25a's MAJ-2 is therefore PARTIALLY UNFALSIFIED on v1B.0.25; the falsification covered the §V Caveats appearance, not the four headline appearances).

**Locations** (verbatim quotes from v1B.0.25):
1. **Table 1B header column** (L363–365):
   - `$w_0$ ... $+4.3\sigma$ from $-1$`
   - `$w_a$ ... $-3.6\sigma$ from $0$`
   - `$w_0+w_a$ ... phantom-crossing required`
   - **NO inline qualifier** — the table header is what readers see first.
2. **Physics interpretation paragraph** (L391–393):
   - "converged iter2 posterior empirically **rules out** the LCDM point $(w_0, w_a)=(-1,0)$ at the joint level: $w_0$ departs by $+4.3\sigma$ and $w_a$ departs by $-3.6\sigma$, with $w_0+w_a=-1.48 \pm 0.15$ requiring phantom crossing"
   - **"empirically rules out" + bare +4.3σ — NO inline qualifier**.
3. **§V Cosmological Fits prose** (L633, embedded in long paragraph): "headline result is $w_0 = -0.812 \pm 0.044$ (departing from the $\Lambda$CDM point $w_0=-1$ at $+4.3\sigma$)"
   - Followed *later in the same paragraph* by the unsampled-tail disclaimer — so partial qualifier coverage.
4. **Table mcmc_inventory caption** (L752): "headline result $w_0 = -0.812 \pm 0.044$ ($+4.3\sigma$ from LCDM) and $w_a = -0.667 \pm 0.186$ ($-3.6\sigma$ from LCDM) with $w_0 + w_a = -1.48 \pm 0.15$ requiring phantom crossing is the canonical quintom signature."
   - **NO inline qualifier in caption** — readers who only scan tables get the discovery framing.
5. **Cross-paper anchor §VII** (L811–813): "is in flight for Paper~I(a) Table~II ... ($w_0 = -0.812 \pm 0.044$ at $+4.3\sigma$ from LCDM, $w_a = -0.667 \pm 0.186$ at $-3.6\sigma$ from LCDM, phantom-crossing required)"
   - **NO inline qualifier — and this is the LAUNCH PATH into P1A**.

**Defect rationale**: The R25a-MAJ-2 truth-audit (v1B.0.23 changelog lines 90–94) declared the finding FALSIFIED by citing the §V Caveats disclaimer. But truth-audit-protocol semantics require the finding to be falsified *everywhere it appears*, not at one cherry-picked location. The discovery framing "+4.3σ from LCDM / phantom-crossing required" appears in:
- the table that defines the headline result (L363–365 Table 1B; no qualifier),
- the physics interpretation paragraph that explains the table (L391–393; "empirically rules out", no qualifier),
- the inventory table caption that summarizes chain status (L752; no qualifier),
- the cross-paper anchor that propagates the result to P1A (L811–813; no qualifier — and this is the literal text P1A imports).

The cross-paper consequence is exactly the brutal-reviewer red flag: **L811–813 is the launch path into P1A Table II**. If P1A imports "+4.3σ from LCDM, phantom-crossing required" verbatim from this cross-paper anchor without the inline unsampled-tail qualifier (which is what the section literally says is in-flight), the discovery overclaim metastasizes from P1B into P1A — and the §V Caveats disclaimer that justified the R25a falsification doesn't travel with the import.

**Recommended fix**: add a one-clause inline qualifier to each of the four un-qualified appearances, e.g.: "$+4.3\sigma$ from $-1$ (marginal extrapolation from MCMC bulk; LCDM unsampled by chain; **not a Bayes-factor exclusion**)" — or, more compactly, an asterisk on the Table 1B "vs LCDM" column header pointing to footnote with the caveat. The "$\dagger$" symbol is already in use on Table mcmc_inventory; reuse the symbol on Table 1B's "vs LCDM" column.

---

## minor

### R25d-MIN-1 — Cross-paper Table I is multi-cron-fire stale across ALL FIVE rows AND missing P5 entirely

**Severity**: minor (R25a-NIT-1 already flagged the staleness as nit-tier and the author's response was "nit; bulk sync later" — but on R25d the table is now strictly worse: the SSOT shows 6 papers; the table shows 5).

**Lines**: L734–749 (`tab:crosspaper`).

**Quote** vs **SSOT** (`project-context/SSOT/index.md` headline tick 200 / 2026-05-24):

| Row | Paper version (Table) | SSOT version | Paper readiness (Table) | SSOT readiness | Stale by |
|-----|-----|-----|-----|-----|-----|
| P1(a) | v1A.0.27 | v1A.0.35 | 74% | 95% | 8 patch versions, +21pp |
| P1(b) | v1B.0.13 | **v1B.0.25** (this paper) | 67% | 95% | 12 patch versions, +28pp |
| P2 | v1.7.30 | v1.7.33 | 82% | 95% | 3 patch versions, +13pp |
| P3 | v3.1.45 | v3.1.62 | 85% | 95% | 17 patch versions, +10pp |
| P4 | v1.0.103 | v1.0.128 | 95% | 95% | 25 patch versions, 0pp |
| **P5** | **MISSING** | **v0.1.26 / 95%** | — | — | **paper does not exist in table at all** |

**Defect rationale**: A brutal reviewer reads "P1(b) v1B.0.13 67%" *inside a v1B.0.25 paper that is 95% per SSOT* and concludes one of three things: (i) the author isn't reading their own paper, (ii) the cross-paper table is decorative and not load-bearing, or (iii) the SSOT and the paper disagree about reality. None of these is the reviewer-friendly interpretation. Additionally, **the P5 spiral-chirality companion paper (v0.1.26 / 95% / 29pp drafted / 6 evidence lines) is entirely absent** — the cross-paper table caption literally says "Wave 14 / Mid-May 2026" which predates P5's drafting cycle by ~10 days, but the paper has been recompiled 12 times since and the table has not been updated. The "Houston tracks via site, not terminal" feedback memo explicitly flags multi-fire-stale cross-references as a red flag.

**Recommended fix**: replace the entire `tab:crosspaper` body with SSOT-aligned rows + new P5 row + table caption "Mid-May → Late-May 2026" timestamp:
```
P1(a) & v1A.0.35 & 95\% & Houston sign-off; external R-round queued \\
P1(b) & v1B.0.25 & 95\% & this paper; nested-sampling $\ln B$ queued \\
P2    & v1.7.33  & 95\% & Houston sign-off; external R-round queued \\
P3    & v3.1.62  & 95\% & Houston sign-off; external R-round queued \\
P4    & v1.0.128 & 95\% & Houston sign-off; R-round-blocked on OR cap \\
P5    & v0.1.26  & 95\% & first external R-round blocked on OR cap \\
```

Or, if the author insists Houston-tracked-via-site is the reason for not updating cross-paper tables in the paper, add a footnote: "Live cross-paper status maintained at `project-context/SSOT/index.md`; in-paper table snapshots Mid-May 2026 state and may lag the SSOT by 1–3 cron fires." The current state — paper at v1B.0.25 stating its own version as v1B.0.13 / 67% — is the worst of both worlds.

---

### R25d-MIN-2 — Six "queued for v1B.0.13+ / .15+ / .16+ / .18+" forward-deferred promises remain in the body of a v1B.0.25 paper

**Severity**: minor (the deferred-target version numbers were the *next* version when written; the paper has advanced 7–12 patch versions past those targets without delivering the nested-sampling Bayes factor that was promised).

**Lines and quotes**:
- L408: "Bayes factor $\ln B$ against LCDM is NOT reported in **this v1B.0.14**" — paper IS v1B.0.25, not v1B.0.14
- L423: "queued for **v1B.0.15+** pending a separate pod-side nested-sampling run" — 10 versions stale
- L633: "the evidence metrics are queued for nested-sampling in **v1B.0.18+** pending a separate pod-side run" — 7 versions stale
- L796: "queued for **v1B.0.16+** pending a separate pod-side run" — 9 versions stale
- L815: "queued for **v1B.0.13+** alongside the Savage-Dickey $\ln B$ pull" — 12 versions stale (the promise itself predates v1B.0.13)
- L920: "queued for **v1B.0.15+**" — 10 versions stale
- L947: Table tab:claims "Model-comparison $\Delta$AIC/BIC/$\ln B$ ... Omitted (pending) ... **v1B.0.18+ Nested Sampling**" — 7 versions stale

**Defect rationale**: A brutal reviewer counting forward-deferred promises in a paper that is *already past* every deferred-target version notices that the nested-sampling Bayes factor — the *single* most load-bearing follow-up commitment in this paper — has slipped from v1B.0.13 to v1B.0.25 (twelve patch versions) without being delivered. Either the run is genuinely blocked on infrastructure (in which case the body should say "blocked on PolyChord/MultiNest pod availability — current ETA unknown") or it has been deprioritized (in which case the queue target should be moved to v1B.1.0 or a less-precise "future work" tag). The current state — six different forward-version targets, all in the past, all unmet — reads as a pattern of optimistic deferral rather than concrete scheduling. R25a's MAJ-2 falsification depended on this nested-sampling rerun "being queued"; if the queue itself is not being honored, the falsification weakens further (separately from R25d-MAJ-2).

**Recommended fix**: replace all six "v1B.0.X+" version-stamped queue targets with one of:
- "queued (pending OpenRouter/RunPod pod availability; current ETA blocked by per-key weekly cap)" — honest about infrastructure block,
- or "future work" with no version stamp — concedes the slip,
- or "v1B.1.0+" — explicit re-scheduling to a future minor-version bump that hasn't already been blown past.

Also fix L408 "this v1B.0.14" → "this v1B.0.25" (stale self-reference, 11 versions behind).

---

### R25d-MIN-3 — §VIII Conclusions states $C_{a\gamma}$ "between $\sim 9$ and $\sim 51$" as the natural ALP range, while §VI Birefringence section defines the natural range as $C_{a\gamma}\in[4,12]$

**Severity**: minor (already flagged in v1B.0.24 changelog as "MIN-2 deferred to v1B.0.25+" — and it's still unresolved in v1B.0.25).

**Lines**:
- §VI L675–676: "The prediction spans $\beta\approx 0.17$--$0.43^\circ$ over **$C_{a\gamma}\in[4,12]$**, $m/H_0\in[1,3]$, $\theta_i\in[0.5,2]$"
- §VI L708: "the required $C_{a\gamma}$ spans **$\sim 9$ to $\sim 51$**, comfortably within natural ALP-photon coupling ranges"
- §VIII Conclusions L855–857: "$\Delta\phi/f_a$ in the natural range $[0.2,1.1]$ giving **$C_{a\gamma}$ between $\sim 9$ and $\sim 51$**"

**Defect rationale**: §VI explicitly defines "natural" as $C_{a\gamma}\in[4,12]$ and uses that range to derive the $\beta\in[0.17,0.43]^\circ$ envelope. Five paragraphs later, the same §VI says the *required* $C_{a\gamma}$ spans $\sim 9$ to $\sim 51$ — implying the upper edge ($\sim 51$) is *four times* the §VI "natural" upper edge (12). The Conclusions section then propagates the [9, 51] envelope as "natural" without acknowledging that 51 > 12 = §VI "natural" upper bound. A skeptical reviewer reads this as: §VI defines "natural" as [4,12] to make the prediction fit; then quietly redefines "natural" as [9,51] to make the observed value fit. The two ranges may both be defensible (one is the prior on $C_{a\gamma}$, the other is the posterior implied by $\beta=0.342^\circ$ and a separately-derived $\Delta\phi/f_a\in[0.2,1.1]$), but the paper never distinguishes "prior natural range" from "posterior implied range" in this language.

**Recommended fix**: in Conclusions L855–857, replace "natural range $[0.2,1.1]$ giving $C_{a\gamma}$ between $\sim 9$ and $\sim 51$" with "natural $\Delta\phi/f_a$ range $[0.2,1.1]$ implying $C_{a\gamma}\in[\sim 9, \sim 51]$ — encompassing but slightly broader than the §VI prior range $[4,12]$ used in the joint-trajectory scan". Or rewrite §VI L708 to say "the required $C_{a\gamma}$ spans $\sim 9$ to $\sim 51$, with the lower edge inside the prior natural range [4,12] used in the prediction scan and the upper edge characterizing the broader plausible ALP-coupling space".

---

## nit

### R25d-NIT-1 — Abstract makes NO mention of the iter2 DESI DR2 $w_0w_a$ chain (Table 1B) — the load-bearing converged result with the +4.3σ headline

**Severity**: nit (framing decision: the author's stance per multiple changelog entries is "iter2 is for P1A's Structural Tension test, P1B just verifies"; but on R25d the iter2 result occupies 50+ lines of paper body including the Table 1B 17-row posterior summary, the +4.3σ physics interpretation paragraph, the §V Caveats block, the §VII cross-paper anchor, and a paragraph of the Conclusions).

**Defect rationale**: A brutal reviewer reading the abstract sees three analyses: (1) $\Lambda$CDM+$\Delta N_{\rm eff}$ MCMC proxy, (2) NaMaster pipeline validation, (3) spectator-ALP consistency check. None mentions iter2 / DESI DR2 / $w_0w_a$ / +4.3σ. But the body has an entire Table 1B for iter2 with its own headline, and Table mcmc_inventory's caption (a "Cross-Paper Verification Status" section) literally claims iter2 "is the empirical anchor for Paper I(a)'s §Structural Tension quintom-B test". This is the inverse pattern of R25a-GRO-B2 (where the author argued the +4.3σ was only in `%`-comments): the +4.3σ is now firmly in the live body (Tables 1B, mcmc_inventory; §V Caveats, physics interp; §VII cross-paper; §VIII Conclusions Forward paragraph) but absent from the abstract. Either the abstract should add a 4th analysis ("(4) iter2 DESI DR2 $w_0w_a$ chain converged at $\hat R-1=0.00820$, $N=128{,}385$; posterior reported in Table~\ref{tab:iter2_posterior} as empirical anchor for Paper I(a) Structural Tension test") or the body should demote Table 1B to an appendix (since by current abstract framing the iter2 result is "not in scope").

**Recommended fix**: add a one-sentence iter2 mention to the abstract between (3) and "A cross-paper status table" — frames the iter2 chain as supporting infrastructure for P1A rather than a P1B headline. Avoids the "abstract overpromises by omission" pattern.

---

### R25d-NIT-2 — Sec II references "$(\omega/H)_0$" as a "phenomenological bounce-class indicator ... discussed in Paper I(a)" but the iter2 chain (Table 1B) is the actual bounce-class discriminator — the language is left over from a pre-iter2 era

**Severity**: nit (text-polish; the prose hasn't been updated to reflect that iter2 now *is* the empirical bounce-class test).

**Lines**: L242–246, repeated essentially verbatim at L598–601:
> "$(\omega/H)_0$ (angular momentum transfer) and $\Omega_k$ are fixed to zero ... the $(\omega/H)_0$ parameter is discussed in Paper~I(a) as a phenomenological bounce-class indicator but is not separately sampled here."

**Defect rationale**: minor — the live anchor for "bounce-class discrimination" is now §VII tab:iter2_posterior (the converged quintom-B posterior), not the unsampled $(\omega/H)_0$ parameter. The redundant verbatim repetition L242–246 ≡ L598–601 across §II and §V.A is itself a yellow flag for prose that wasn't touched during the iter2 incorporation.

**Recommended fix**: dedupe one of the two verbatim copies; in the surviving copy, add a forward-pointer "the bounce-class discrimination test is implemented empirically via the iter2 $w_0w_a$ chain (Table~\ref{tab:iter2_posterior}, §VII)".

---

## What was checked and survived (no findings)

- **(a) abstract / results / conclusion +4.3σ caveat coverage**: PARTIALLY FAILS — see R25d-MAJ-2. The caveat is in §V Caveats only; four other appearances are unqualified.
- **(b) §3 Holst topological-invariance scalar-only-sector + Assumption (f)**: NOT APPLICABLE TO P1B. P1B has no §3 Holst topological-invariance section — that section lives in P1A. P1B's §3 is "Stock-CAMB MCMC: Generic Radiation-Proxy Test". The scalar-only-sector caveat *does* appear in L223 ("$\fnl=-35/8$, valid strictly for the minimal scalar-only $w=0$ matter-dominated contraction class") and is appropriately scoped there. No P1B finding.
- **(c) DESI DR2 iter2 vs frozen ΛCDM+ΔNeff conflation**: NOT FOUND. The paper rigorously distinguishes the two: §III "Frozen MCMC program: 309,189 raw samples across 2 frozen dataset combinations (176,240 + 132,949)" and the third (Planck-only, 114,992 raw) is "not aggregated into any frozen-posterior summary statistic". The iter2 chain (128,385) is reported separately in Table 1B and Table mcmc_inventory row 4. Table mcmc_inventory caption clearly states "2 frozen chains below ($\Lambda$CDM+$\Delta\Neff$ proxy, $w_0 w_a$ not sampled) suffice for the P1(b) headline conclusions". No conflation found — clean separation across all six iter2-reference locations.
- **(d) Bayes-factor / model-comparison REMOVAL narrative consistency**: MOSTLY CLEAN. The Savage-Dickey/$\Delta$AIC/$\Delta$BIC block was removed in v1B.0.7 and is consistently reported as removed in §V (L606–633), §VIII Conclusions (L844), Appendix A (L920), and Appendix B Table claims (L947). Three minor asymmetries: (i) L496 cites Liu et al.'s external $\Delta\text{AIC}=-5.7$ to $-6.6$ favoring torsion — accepting external AIC while internally banning it; (ii) "queued v1B.0.X+" version targets are all stale (see R25d-MIN-2); (iii) L408 "this v1B.0.14" stale self-reference (paper is v1B.0.25). None rise to MAJOR.
- **(e) ALP β range [0.17,0.43] vs naive [0.027,0.44] consistency**: CLEAN at §VI L674–682 (the v1B.0.24 R25b-BLK-1 clarification paragraph explicitly distinguishes joint-trajectory scan from independent-extremes product and names the naive envelope). The downstream §VIII Conclusions paragraph L853–860 uses the joint-trajectory range without re-stating the naive-envelope distinction, but the §VI text is self-contained and the Conclusions are appropriately scoped. No β-range framing finding. (Separately, R25d-MIN-3 catches the $C_{a\gamma}$ range internal contradiction.)
- **(f) NaMaster "sky detection" vs "pipeline validation" framing**: CLEAN. The paper consistently distinguishes the two: abstract L161 ("pipeline validation"), abstract L165 ("upper bound on noise-only recovery, not a sky-detection figure of merit"), §I L208 ("Not a competitive sky detection"), §IV L522 ("\textbf{Scope note}... must not be conflated with the published Planck/ACT DR6 $2.4$–$2.9\sigma$ sky detection"), §IV L578–579 ("methodology cross-check, not a competitive sky measurement"), §VIII Conclusions L846 ("methods validation, not a competitive sky detection"). Six independent disclaimers across abstract + intro + §IV + Conclusions. No framing slip found.
- **(g) cross-paper Table 1 freshness vs SSOT 6-paper status**: FAILS — see R25d-MIN-1. All 5 rows stale; P5 missing entirely. The R25a-NIT-1 finding has accumulated severity over time.

---

## Summary

**0 BLOCKER / 2 MAJOR / 3 minor / 2 nit**

R25c DeepSeek-confab was indeed narrowly focused on JSON arithmetic and missed:
- **R25d-MAJ-1**: the surgical L345 fix that closes R25c-MIN-1 introduces a new logical contradiction ("17 = 17, distinct") — a brutal reviewer reads this as the author closing reviews mechanically rather than reading the result. DeepSeek's "single-token surgical" recommendation was followed too literally.
- **R25d-MAJ-2**: the +4.3σ-from-LCDM discovery framing appears in 5 locations; R25a-MAJ-2 was declared falsified on the basis of ONE of them (§V Caveats). The other four — Table 1B header, physics interpretation paragraph, mcmc-inventory caption, cross-paper P1A-anchor — propagate the discovery framing without the unsampled-tail qualifier. The cross-paper P1A anchor (L811–813) is the most consequential: it is the literal text imported into P1A's Table II $\ddagger$ rows.
- **R25d-MIN-1**: cross-paper Table I is now stale across all 5 listed rows AND missing P5 entirely. The R25a-NIT-1 deferral has compounded into a structural staleness issue.
- **R25d-MIN-2**: six "queued for v1B.0.13+/15+/16+/18+" forward-deferred promises in a v1B.0.25 paper — the nested-sampling Bayes factor has slipped 12 patch versions without delivery, and R25a-MAJ-2's falsification rested partly on that rerun being "queued".
- **R25d-MIN-3**: the v1B.0.24 deferred MIN-2 ($C_{a\gamma}\in[4,12]$ vs $C_{a\gamma}\sim[9,51]$) is still unresolved; §VI and §VIII Conclusions use two different "natural" ranges differing by a factor of $\sim 4$ at the upper edge.

Streak status: **round 2-of-3 returns 2 MAJOR + 3 minor + 2 nit**; AGENT_RULES §4.4.1 cascaded-loop-exit **NOT satisfied**. The 1-of-3 streak via R25c (0/0/1-min/0-nit) is broken by R25d-MAJ-1 + R25d-MAJ-2. The v1B.0.25 → v1B.0.26 closure cycle should:
1. **MAJ-1**: rewrite the L357 caption clause "distinct from the $k=7+10=17$ count" → "numerically coincident with but structurally distinct from the $k=7+10=17$ count for the frozen chains (iter2 samples $w_0, w_a$; frozen samples $\Delta N_{\rm eff}$ and one additional Planck nuisance)";
2. **MAJ-2**: add inline unsampled-tail qualifiers to the four un-qualified "+4.3σ" appearances (L363–365 Table 1B header, L391–393 physics interp, L752 mcmc_inventory caption, L811–813 cross-paper anchor) — the propagation into P1A is the load-bearing risk;
3. **MIN-1**: bulk-update `tab:crosspaper` to SSOT-aligned 6-row state with P5 added;
4. **MIN-2 / MIN-3 / NIT-1 / NIT-2**: text-polish bundle for the same fire.

After those four fixes, R25e (round 3-of-3, different persona — recommend theoretical-physics-Grok or perplexity-citation) should verify with high probability of returning 0 BLOCKER + 0 MAJOR.

— Internal Claude / Grok-4.3 brutal-honesty persona, R25d, 2026-05-24 PDT
