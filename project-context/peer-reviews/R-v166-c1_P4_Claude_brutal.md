# P4 R-v166-c1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (19657 chars)
**Wall time**: 485.3s

---

# Referee Report — P4 (R-v166-c1)

**Submission:** "Survey-Scale Galaxy Chirality with Equivariant TTA..." (15 pp.)
**Journal:** Physical Review D

I have read the rendered PDF end-to-end and recomputed every load-bearing scalar in the abstract, Tables I–V, and Figs. 2–8. The paper has substantive content, but in its present form it falls below the PRD bar on multiple grounds: internal numerical inconsistencies between the abstract, body, Table II, and Fig. 3; survival of internal version-tracking language ("versions ≤1.0.165", "withdrawn"); an abstract that reads as a stitched-together change-log rather than a scientific summary; and a headline "null" claim that is structurally undermined by multiple +3.6σ–+7.3σ residuals that the paper itself acknowledges are not fully understood.

---

## ESSENTIAL findings (must be fixed before acceptance)

### P4-E1 — Numerical contradiction: Table II vs. body text vs. Fig. 2 caption (Catalog A/C excess)

- Table II (p. 5): Catalog A excess = **+0.79%**, Catalog C excess = **−0.26%**.
- Sec. IV B (p. 5): "The 3.86× asymmetry-suppression factor from raw **+2.05%** to equivariant **−0.53%**".
- Fig. 2 caption (p. 5): "the global CW-fraction shift from **+2.05% (A)** to **−0.53% (C)** is dominated by this step (Table II)".
- Sec. VI (p. 9): "a classifier bias of only **0.79%**, combined with non-uniform sky coverage, produces highly significant but entirely spurious dipole signals".
- Sec. VI again (p. 9): "Equivariant averaging collapses the real-space dipole from 2.31σ to 0.43σ".

The body uses **two mutually incompatible numerical pairs** (0.79%/−0.26% in Table II and Sec. VI, vs. 2.05%/−0.53% in Sec. IV B and Fig. 2). Note 2.05/0.53 = 3.87 (matches the quoted "3.86× suppression") but 0.79/0.26 = 3.04 (does not). The two numbers therefore differ by a factor ~2.6× in absolute amplitude — this is not a rounding error.

**Required fix:** state explicitly whether the headline asymmetry is 0.79% or 2.05%, fix Table II or Sec. IV B/Fig. 2 to match, and recompute the suppression factor consistently. The body cannot claim "the difference between Catalog A and Catalog C is the difference between a 2σ 'detection' and a clean null" (Fig. 7 caption) when two different ΔfCW values are used to demonstrate this.

### P4-E2 — Fig. 3 pie-chart numbers do not match Sec. IV A or the figure's own caption

- Fig. 3 caption (p. 6) and Sec. IV A (p. 5) state: "CW 1,592,107 (18.78%), CCW 1,609,053 (18.99%), NS 5,273,371 (62.23%)".
- The pie chart in Fig. 3 itself displays: CW = **1,687,069 (19.9%)**, CCW = **1,634,726 (19.3%)**, Not-Spiral = **5,152,736 (60.8%)**.

Both sets sum to 8,474,531 — they are not arithmetic typos but **distinct catalog states**. The pie-chart numbers give cw/(cw+ccw) = 1,687,069/3,321,795 = **0.5078** — that is Catalog **A**, not Catalog C. The figure plots Catalog A composition while the caption claims Catalog C.

**Required fix:** regenerate Fig. 3 from the Catalog C numbers, or correct the caption. Given Catalog C is "the recommended tier for all cosmological parity analyses" (Sec. III D), showing Catalog A in a figure labeled "Catalog C composition" is misleading.

### P4-E3 — Table III significance values are inconsistent with the displayed Cℓ and σnull

For ℓeff = 4: Cℓ = 3.210, σnull = 0.804 → ratio = 3.99. Reported significance: **+6.097σ**.
For ℓeff = 9: Cℓ = −0.248, σnull = 0.574 → |Cℓ|/σ = 0.43. Reported significance: **+2.232σ**.
For ℓeff = 14: |Cℓ|/σ = 0.387/0.446 = 0.87. Reported: **+2.626σ**.
For ℓeff = 19: 0.576/0.420 = 1.37. Reported: **+2.229σ**.
For ℓeff = 24: 0.648/0.366 = 1.77. Reported: **+2.470σ**.

The numbers presented cannot be reconciled with the simple z = (Cℓ−⟨null⟩)/σnull formula at face value. If a non-zero null mean ⟨Cℓ⟩null is being subtracted, the table must report it; if a different significance estimator is used (e.g. moment-matched empirical rank), it must be defined. As displayed, no reader can reproduce a single significance value.

**Required fix:** publish either ⟨Cℓ⟩null per bandpower in Table III, or restate the significance definition used and recompute.

### P4-E4 — Headline "null" claim is structurally undermined by load-bearing residuals the paper itself flags as not fully explained

The abstract calls the result "a null real-space chirality dipole" while in the same abstract reporting:

- canonical MASTER ℓ=1: **+3.64σ**
- apodized MASTER ℓ=1 vs. global-shuffle: **+7.28σ**
- apodized MASTER ℓ=1 vs. depth-stratified null: **+7.13σ**
- hemisphere local maximum: **3.05σ** (pLEE ≤ 10⁻⁴ in Table I)
- monopole-only null residual: **+1.68σ**

The paper attributes all of these to "interpretation (ii) — a coherent depth/sampling-correlated systematic at low ℓ on the patchy canonical footprint." But the depth-stratified null already controls for depth and the excess is essentially unchanged (+7.28 → +7.13σ), which means **the dominant systematic has not been identified** — only a label has been attached to it. A primary scientific result in PRD cannot be "null" while simultaneously requiring four pages of appendix to argue that ≥+7σ excesses are "in the same coherent low-ℓ systematic family."

**Required fix:** the abstract must either (a) demonstrate quantitative closure of the +7.28σ residual against a *named*, modeled systematic template (not just argue it is "consistent with" a class of systematics), or (b) honestly present the result as ambiguous: "real-space dipole consistent with null; harmonic-space estimators show unresolved ≥+3σ residuals attributed to footprint-correlated systematics." The current framing oversells the null and underplays the residuals.

### P4-E5 — Internal version-tracking and withdrawal language in the published body

The abstract and Appendix A explicitly reference internal version numbers and contain editor/audit-log prose that does not belong in a PRD paper:

- Abstract p. 1: "*Withdrawal note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ = 1 null...*"
- Appendix A p. 11: "*Versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ = 1 null on a putative 'strict-superset subsample mask'... A June 2026 provenance audit found that this number was produced by an uncommitted script operating on a synthetic catalog...*"
- Footnote 1 (p. 6) references "an earlier version misquoted this factor as ≈ 1.49".

PRD papers are not preprint repositories. Internal version tracking, provenance-audit retraction prose, and uncommitted-script forensics are inappropriate. The authors must either (a) post the corrected paper as a clean first submission with no reference to prior internal versions, or (b) if a published prior version exists in the same journal that is being formally corrected, follow the journal's Erratum procedure — not embed the correction in the abstract of a new submission.

**Required fix:** delete all "versions ≤1.0.165", "earlier version misquoted", "uncommitted script", and "synthetic catalog... withdrawn" language from the body, abstract, and footnotes. If the authors wish to document the audit, that belongs in a supplementary release-notes file, not the paper.

### P4-E6 — Side-by-side σ values from incomparable nulls in the abstract without per-juxtaposition disclaimer

The reviewer instructions are explicit on this point. The abstract contains:

- "+0.43σ (p = 0.30, isotropic-null bootstrap)" — null type 1
- "z ≈ −18" — block-bootstrap WLS template fit
- "+3.64σ (z = ∆/σnull moment-ratio; empirical rank pMC = 0.030 ... 500-MC binomial per-pixel-shuffle null)"
- "+7.28σ vs. global label-shuffle"
- "+7.13σ ... depth-stratified null"
- "+3.57σ on C² 2° apodization"
- "σ = −2.89 against permutation null"

These are juxtaposed across paragraphs of the abstract. The single global disclaimer ("σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable") is buried mid-abstract and does not appear at the point of comparison. Worse, the +0.43σ headline and the +3.64σ/+7.28σ residuals are *implicitly* compared when the abstract uses the latter to argue the former is the "true" result.

**Required fix:** restructure the abstract to either (a) state a single primary estimator with one null, or (b) include an explicit table relating every quoted σ to its null at the point it appears. Burying the disclaimer once does not satisfy the instruction.

---

## MAJOR revisions

### P4-M1 — Abstract is 80 lines long and reads as a change-log

A PRD abstract is ~250 words. This one is ~900 words and contains: a withdrawal note, a footnote-style scope statement, a "we emphasize at the outset" parity-channel clarification, an explicit attribution paragraph for interpretations (i)/(ii)/(iii), a falsification criterion with sub-clauses, and a scope paragraph. The headline result (null real-space dipole) is essentially unrecoverable to a casual reader. **Required fix:** rewrite to ≤250 words with one headline number, the data scale, and one sentence on systematics caveats.

### P4-M2 — Training-label independence is weak and the GZ1 floor is overstated

Sec. II B states 67.6% of training labels derive from CE-ResNet predictions. The independent GZ1 cross-match yields 69.91% spiral-chirality accuracy with Cohen's κ = 0.40 ("fair" agreement, not "substantial"). The paper then claims the catalog "advances beyond CE-ResNet" — but the classifier's binary discrimination is largely trained on CE-ResNet labels. The independence of this work from CE-ResNet at the chirality-decision level is essentially the κ = 0.40 cross-match, which is weak. **Required fix:** acknowledge that the chirality decision rule is partially inherited from CE-ResNet and reframe novelty in terms of survey scale and bias-hardening, not classifier independence.

### P4-M3 — Falsification criterion at A95 (not A50) is motivated reasoning

Abstract p. 1: the authors set the falsification boundary at A95 ≈ 1.5–2% rather than at the 50%-recovery threshold A50 ≈ 0.75%, explicitly because "a future 5σ detection at A ∼ 0.75% would be entirely consistent with the present non-detection." This is non-standard. Standard practice is to quote the median sensitivity and let future authors interpret. Setting the falsification bar at the upper end of the recovery distribution maximizes the chance the present null survives future challenge. **Required fix:** quote both A50 and A95 in the abstract without implying that only A95 constitutes falsification; let the reader judge.

### P4-M4 — The "withdrawn −0.122σ" was load-bearing and its replacement is +7.28σ, not null

Per Appendix A, the prior version's headline diagnostic was −0.122σ on the "strict-superset subsample mask." The faithful rerun gives +7.28σ in the same channel. This is not a minor numerical correction — it is a sign-and-amplitude inversion of a load-bearing diagnostic that was previously cited to argue the result was robustly null. The paper now relies on the real-space +0.43σ and template-fit z≈−18 to anchor the null. **Major concern:** if the harmonic-space channel produces a +7σ excess on the correct catalog, the claim that the *real-space* dipole is the "primary" estimator looks chosen post-hoc. **Required fix:** state explicitly in the body that the choice of real-space dipole as the primary estimator post-dates the discovery that the harmonic channel produces +7σ on the corrected catalog, and justify the choice on pre-registered grounds if possible.

### P4-M5 — "Largest catalog" claim is partially refuted by Walmsley et al. (Galaxy Zoo DESI)

Ref. [9] (Walmsley et al. 2023) reports detailed morphology for 8.7M DESI Legacy galaxies. The present paper claims 8.47M galaxies and "the largest galaxy chirality catalog to date." The two claims are compatible (Walmsley does not provide chirality labels per se) but the framing should distinguish chirality-labeled count from total-classified count. **Required fix:** sharpen the novelty claim — "largest *chirality-labeled* catalog."

### P4-M6 — The 24-template extended WLS fit and the 9-template fit are described but never tabulated

Appendix D quotes z ≈ −264.5 from the naive WLS posterior and z ≈ −18.1 after block-bootstrap inflation by 14.7×. No table is given. No design matrix is shown. The 24-template fit's Adipole = 4.51×10⁻³ vs. the 9-template fit's 4.55×10⁻³ is consistent but un-auditable. **Required fix:** supply a table with the template list, the per-template coefficients, and the covariance.

### P4-M7 — Hemisphere LEE: pLEE ≤ 10⁻⁴ in Table I but "< 1σ" in Appendix C

Table I row (v) reports pLEE ≤ 10⁻⁴ (direct-MC). Appendix C states the conservative Bonferroni/BH penalty across ~650 directions brings post-LEE significance to < 1σ. Putting "pLEE ≤ 10⁻⁴" in the summary table without immediately stating that this is *random-label* rejection and not significance-after-LEE-correction is misleading. **Required fix:** Table I row (v) should report the Bonferroni-corrected significance, not the un-corrected p-value, with a footnote explaining the random-label-null vs. trials-corrected distinction.

### P4-M8 — Significance table cited in abstract differs from Sec. IV C body

Abstract: "post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σnull moment-ratio; **empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent**)". Body Sec. IV C and Table III do not flag this gap. A +3.64σ "moment-ratio" headline that converts to ~1.9σ when rank-ordered against the actual MC distribution is a substantial inflation. The two should not be quoted with equal billing.

---

## MINOR revisions

### P4-m1 — PACS numbers are obsolete (PACS was discontinued in 2010). Either remove or replace with PhySH terms.

### P4-m2 — Duplicate / awkward phrasing

- p. 4 Fig. 1 caption: "*the V iT − Small-Small classifier*" — "Small-Small" is a typo/duplication. Should be "ViT-Small classifier."
- Abstract: "consistent with monopole leakage through survey geometry (Sec. IV D) and is not interpreted as a cosmological signal" — repeated in nearly identical form later in the abstract.

### P4-m3 — Sec. III C "flip-swap correlation = 1.000" is trivially true by construction

The TTA averaging in Eq. (2) is symmetrized by definition — reporting "flip-swap correlation = 1.000" as a validation result is circular. State that the procedure is exact by construction.

### P4-m4 — Footnote 1 length

Footnote 1 (p. 6) runs ~20 lines and contains parenthetical bookkeeping ("Artifact: pipelines/p2_chirality/outputs/..."). Move to appendix or supplementary.

### P4-m5 — Sec. IV B "available in the companion data repository" twice in one paragraph

Repeated phrasing on p. 5–6 and again in Appendix C ("results available in the companion data repository"). Consolidate.

### P4-m6 — Table I row (iv) two σ values separated by "/" without per-column null label

"+7.28/+7.13" with footer "global per-galaxy label-shuffle and depth-stratified nulls respectively" — readable but uses a slash for two distinct nulls in a single cell. Split into two rows.

### P4-m7 — Eq. (1) head spec uses "→" arrows in inline LaTeX that may render oddly

Cosmetic; verify in proof.

### P4-m8 — Reference [2] is Shamir 2022 PASJ; reference [3] is Shamir 2022 MNRAS — confusingly both year 2022 with similar abbreviated journal text. Consider "Shamir (2022a)" / "Shamir (2022b)" in the body.

### P4-m9 — "z ≈ −18" used as a significance metric

A "z-score" of −18 from a WLS posterior is not a frequentist σ. The body acknowledges this is from a block-bootstrap-inflated posterior, but the casual reader will conflate it with the Gaussian-tail "18σ" claim — which is nonsensical for an 18σ excursion in a real distribution. Use language like "the 1.7% template is disfavored at the boot-strapped posterior's tail at log10(odds) ≈ X."

### P4-m10 — Fig. 8 caption gives ℓ = 1 and ℓ = 2 panels and a ℓ = 5 bar at "2.5σ" but no body discussion

The figure shows a 2.5σ at ℓ = 5 (red bar) with no body discussion of why ℓ = 5 is highlighted. Either discuss or remove the emphasis.

---

## NIT

### P4-N1 — Page count

15 pages for a paper whose primary scientific finding is "consistent with null" is too long. Recommended target: **9 pages including appendices**. The systematic analysis can move to supplementary. The abstract alone is currently over a full column.

### P4-N2 — Figure 1 (representative galaxies) is decorative and could be supplementary

### P4-N3 — Acknowledgments lists "AI tool usage" — disclosure is good, but the phrasing is informal for PRD.

### P4-N4 — Some hyphens render as "−" (minus) in body (e.g. "Z2 and D4 to within |∆⟨pCW⟩|<0.0016"). Cosmetic.

### P4-N5 — Reference [11] (Land et al. 2008) is cited only in the introduction context implicitly; verify whether it is actually cited in the body — I do not see it in the visible text.

---

## Audit of headline numbers (recomputed from displayed inputs)

| Claim | Source | Recomputed | Match? |
|---|---|---|---|
| 0.4974 ± 0.000279 | Table II, p(1-p)/N for N=3,201,160 | √(0.4974·0.5026/3,201,160) = 2.79e-4 | ✓ |
| 28.8σ for Catalog A | Table II | (0.5079−0.5)/0.000279 = 28.3 | ≈ ✓ (rounding) |
| 14.6σ for Catalog B | Table II | (0.504−0.5)/0.000279 = 14.34 | ≈ ✓ |
| 9.5σ for Catalog C | Table II | (0.4974−0.5)/0.000279 = −9.32 | ≈ ✓ (sign suppressed) |
| 99.3% reproduction (Table IV) | (1.685/1.696) | 0.99352 = 99.35% | ✓ |
| Catalog A excess +0.79% vs. abstract/Fig.2 +2.05% | Table II vs. body | **inconsistent** | ✗ (see E1) |
| 3.86× suppression factor | Sec. IV B | 2.05/0.53 = 3.87 (using body numbers); 0.79/0.26 = 3.04 (using Table II) | depends on which pair |
| Fig. 3 pie chart 1,687,069/3,321,795 = 0.5078 vs. caption Catalog C | Fig. 3 vs. its caption | **inconsistent** | ✗ (see E2) |

---

## Summary recommendation

**REJECT** (with strong invitation to resubmit after major rework)

The paper addresses a topical question with a genuinely large dataset and a methodologically reasonable bias-hardening procedure, and the null real-space dipole is a credible scientific result. However, the submission as written cannot be accepted by PRD. It contains a first-order numerical inconsistency between Table II, the body, and the Fig. 2 caption regarding the headline asymmetry percentages (P4-E1); Fig. 3 displays Catalog A numbers under a "Catalog C" caption (P4-E2); Table III significance values are not reproducible from the displayed Cℓ/σnull (P4-E3); the abstract retains explicit version-tracking and withdrawal language inappropriate for an archival physics paper (P4-E5); and the headline "null" framing is structurally undermined by multiple +3.6σ–+7.3σ unresolved residuals which the paper attributes to but does not close out against a named systematic (P4-E4). The retraction of the prior −0.122σ diagnostic and its replacement by a +7.28σ excess on the corrected catalog raises a serious post-hoc-selection concern about which estimator was chosen as "primary." A complete rewrite — clean abstract, single consistent set of catalog statistics, properly reproducible significance tables, and either quantitative closure of the +7σ residual or honest reframing of the result as "ambiguous with unresolved harmonic-space residuals" — is required before this paper can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P4 (R-v166-c1, supplemental pass)

Below are findings from a second pass focused on the failure modes listed in the prompt. All findings are **new** relative to the initial report.

---

## ADDITIONAL ESSENTIAL findings

### P4-E7 — Three different per-pixel spiral-count thresholds for the canonical mask

The mask definition is stated inconsistently in three places:

- Sec. IV C, p. 6: "In each pixel *p* containing **>10 spiral galaxies**, we compute the asymmetry $A_p$."
- Fig. 5 caption, p. 8: "the canonical mask used for the headline ℓ=1 analysis (§IV C) requires $N_{\rm spiral}(p) \geq 5$ per pixel."
- Appendix A, p. 11: "canonical Catalog C mask (pixels with $\geq 10$ spirals)."

The three thresholds (>10, ≥5, ≥10) are not equivalent. The reported $f_{\rm sky}=0.49005$ depends on which one is correct. Per App. E the result is robust between 5 and 50, so the physical outcome may be insensitive — but the canonical mask used to produce Table I, Table III, Table IV, and Figs. 4–8 must be defined precisely.

**Required fix:** state the canonical threshold once and use it consistently.

### P4-E8 — Fig. 8 caption does not describe what Fig. 8 shows

Fig. 8 caption: "Top: ℓ=1 dipole power. Bottom: ℓ=2 quadrupole." But the figure title is "Angular Power Spectrum of Chirality Asymmetry" and the figure displays a **single bar chart** with five bandpowers (ℓ=1, 2, 3, 4, 5) — not a top/bottom two-panel plot. The annotations "2.7σ" at ℓ=1 and "2.5σ" at ℓ=5 (red bars) are unexplained in the caption text, and the body never discusses why ℓ=5 is highlighted.

Furthermore, the "2.7σ at ℓ=1" displayed in Fig. 8 is inconsistent with every other ℓ=1 number in the paper (+0.43σ real-space, +1.68σ pre-MASTER monopole-only residual, +3.64σ canonical post-MASTER, +7.28σ apodized post-MASTER). A reader trying to identify which null Fig. 8 uses gets no help.

**Required fix:** regenerate the caption to match the figure, label the null used for the displayed σ values, and reconcile the "2.7σ at ℓ=1" with the body's hierarchy.

### P4-E9 — "Four-null battery + cross-spectrum" promised in abstract does not appear in App. D

Abstract, p. 1: "Three interpretations ... are systematically tested with a **four-null battery + direct cross-spectrum**." App. D presents **six labeled anchors**: (a) apodized-mask, (b) multipole-spectrum, (c) leg-proxy, (d) density-stratified, (e) boundary-distance variance, (f) joint WLS — plus the cross-spectrum already named separately. The abstract's promised count does not match the body. This matters because the abstract uses "four nulls" as a quantitative-rigor claim.

**Required fix:** either rename to "five-anchor systematic analysis" (which Sec. IV D already uses, p. 7) and propagate to abstract, or remove the count.

### P4-E10 — Conclusions "headline finding" contradicts the abstract's "headline scientific result"

- Abstract p. 1: "The **headline scientific result** is a null real-space chirality dipole."
- Sec. VII a, p. 10: "**Headline finding**: a quantifiable monopole-mask leakage channel."

The paper cannot have two different headline findings. The title attempts to combine three claims; the abstract picks one; the Conclusions pick a different one. A PRD reader of the abstract takes away "null"; a PRD reader of the Conclusions takes away "leakage channel discovered." These are different scientific narratives.

**Required fix:** unify on one headline across title, abstract, and Conclusions.

---

## ADDITIONAL MAJOR revisions

### P4-M9 — σ rises from +1.85 to +3.64 while $C_1$ falls by 34% — mechanism not explained

App. A, p. 11: "Monopole subtraction reduces decoupled $C_1$ at ℓ=1 from $2.30\times10^{-5}$ to $1.51\times10^{-5}$ (∼34%) and increases σ from +1.85 to +3.64." That is, the *amplitude* drops while the *significance* nearly doubles. Reconstructing implicit null widths: σ_null = 1.24×10⁻⁵ before, 4.15×10⁻⁶ after — a 3× collapse of the null spread. This is plausible (monopole dominates the null variance) but is presented as if obvious. A naïve reader will see "+1.85 → +3.64σ after a routine subtraction" and conclude monopole subtraction *inflated* the signal.

**Required fix:** one sentence explaining that monopole subtraction also collapses the null variance, with the explicit σ_null values before/after.

### P4-M10 — Body Sec. IV C reports +7.28σ and +9.78σ on identical data for two Wp choices; abstract drops the larger value

Sec. IV C: "+7.28σ for $W_p = N_{\rm all}$ (+9.78σ for $W_p = N_{\rm spiral}$)." The 9.78σ result on the same field with a different weighting is mentioned parenthetically but never justified. A weighting-choice ambiguity that moves a significance by 34% is a load-bearing systematic, not a parenthetical. The abstract reports only +7.28σ and +7.13σ.

**Required fix:** pre-register the weighting choice on physical grounds (depth proxy), or quote both values in every comparison.

### P4-M11 — Sec. V A "we do not claim a frequentist exclusion of Shamir" is contradicted by abstract z≈−18

Sec. V A: "We do *not* claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis under his pipeline + cuts (not performed here)."

But abstract p. 1: "a block-bootstrap WLS template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude at z ≈ −18 (Appendix D)."

1.7% is *below* Shamir's 2–4% range. If the 1.7% template is disfavored at z≈−18, then 3% is disfavored even more strongly. Yet the body explicitly disclaims a frequentist exclusion. The paper cannot simultaneously claim z≈−18 disfavor of 1.7% (which implies stronger disfavor of 3%) and "no frequentist exclusion of Shamir." Either the WLS-template exclusion is meaningful and Shamir IS excluded at >5σ, or the z≈−18 is acknowledged as not a usable significance and should not appear in the abstract.

**Required fix:** reconcile. Either drop "we do not claim frequentist exclusion" and own the z≈−18, or downgrade z≈−18 to a qualitative log-odds statement.

### P4-M12 — Comparison-factor "6–12×" in Sec. V A uses the wrong reference quantity

Sec. V A: "inconsistent in amplitude with Shamir's claimed ∼3% signal by a factor of ∼6–12 under the present pipeline."

The ratio 6–12 comes from dividing Shamir's 2–4% by the **maximum regional asymmetry** 0.32% (per Sec. V A first line). But the relevant comparison is to the **sensitivity floor** A₅₀ ≈ 0.75% (abstract). Using A₅₀, the factor is 2.7–5.3×. Using A₉₅ ≈ 1.5–2%, the factor is 1–2.7×. The 6–12× number is the most flattering ratio and uses a quantity (max regional asymmetry, a fluctuation statistic) incommensurate with Shamir's quoted **dipole amplitude**.

**Required fix:** quote the factor against the formal sensitivity threshold, not the maximum regional fluctuation.

### P4-M13 — z≈−18 from a block-bootstrap WLS posterior is not a Gaussian σ but is presented as one

App. D, p. 13: "Block-bootstrap at NSIDE=8 ($N_{\rm boot}$=1000) inflates σ($A_{\rm dipole}$) by 14.7×, reducing z to ≈−18.1; interpretation (i) at A=1.7% remains strongly disfavored under the spatial-coherence-respecting bootstrap covariance."

A z=−18 from 1000 bootstrap realizations is in the far tail of an empirical distribution with no support past z ≈ −3 (with N=1000 realizations one cannot resolve probabilities below ∼10⁻³, i.e. ∼3σ Gaussian-equivalent). Quoting z=−18 implicitly extrapolates a Gaussian tail well beyond the resolved range. The parenthetical "(far-tail)" earlier in the paragraph does not save the abstract claim.

**Required fix:** report a properly bounded statistic — e.g. "the 1.7% template lies outside all 1000 bootstrap realizations (empirical $p < 10^{-3}$)" — and remove the misleading "z ≈ −18" from the abstract.

### P4-M14 — "Catalog C-full +4.31σ monopole-preserving" estimator appears for the first time in App. E

App. E b introduces a new significance value (+4.31σ) for a "monopole-preserving Catalog-C-full pre-MASTER pseudo-$C_\ell^{(\ell=1)}$ estimator" — neither in Table I nor Table III nor any earlier discussion. Footnote 2 attempts to clarify but introduces yet a *third* estimator family (monopole-preserving pre-MASTER) on top of the canonical (+3.64σ) and apodized-Wp (+7.28σ) families.

The HC-cut "robustness" test then uses *this* new estimator (not the headline +0.43σ real-space dipole) to argue HC-cut collapse. But the natural like-for-like comparison is to apply HC cuts to the real-space estimator and the apodized MASTER, not to introduce a new unprecedented estimator in an appendix. This is a post-hoc estimator choice that should be flagged.

**Required fix:** either include this estimator in Table I/III with its null, or apply the HC-cut test using one of the already-disclosed estimators.

### P4-M15 — References [11] and [13] appear in the bibliography but I cannot find them cited in the body

Ref. [11] Land et al. 2008 ("Galaxy Zoo: large-scale spin statistics") and Ref. [13] Gross & Vitells 2010 ("Trial factors for the look elsewhere effect") are listed but I find no \cite to them in the visible body. App. C uses Bonferroni/BH (the GV2010 LEE framework) without citation — exactly where [13] should appear.

**Required fix:** cite both references in their natural body locations, or remove from bibliography.

### P4-M16 — Depth-stratified null reduces significance by only 2% but is invoked as falsifying the depth interpretation

Sec. IV C: "A depth-stratified null (labels permuted within 10 $N_{\rm all}(p)$ deciles) leaves the excess essentially unchanged (+7.13σ / +9.06σ), **excluding pixel-depth sampling alone as the driver**."

The reduction from +7.28σ to +7.13σ is 2%. The reduction from +9.78σ to +9.06σ is 7%. These are small but non-zero. The logic "if depth were the dominant systematic, the depth-stratified null would absorb most of the signal" only holds if depth correlates linearly with the signal across deciles. A non-monotonic depth-correlated systematic would also survive decile permutation. The "excluding pixel-depth sampling alone" claim is therefore *only* about *monotonic depth correlations within deciles*, not about depth in general.

**Required fix:** weaken the claim to "depth-decile-monotonic sampling alone does not absorb the excess" or extend the null to handle non-monotonic depth correlations.

---

## ADDITIONAL MINOR revisions

### P4-m11 — Table II σ values are systematically ~2% high relative to recomputed binomial

Catalog A: (0.5079−0.5)/0.000279 = 28.32, reported 28.8 (Δ=1.7%).
Catalog B: (0.504−0.5)/0.000279 = 14.34, reported 14.6 (Δ=1.8%).
Catalog C: |(0.4974−0.5)|/0.000279 = 9.32, reported 9.5 (Δ=1.9%).

The consistent ~2% inflation suggests a slightly different σ being used (perhaps $1/\sqrt{N_{\rm CW}+N_{\rm CCW}}$ for a different per-tier N). Either way, recompute or document.

### P4-m12 — Hemisphere max|A| z-score is reported as +4.42σ but recomputed gives +4.37σ

Table IV row 2: data 3.48×10⁻³, null (1.69±0.41)×10⁻³. (3.48−1.69)/0.41 = 4.366, reported +4.42. ~1% discrepancy.

### P4-m13 — Pre-MASTER pseudo-C₁ z = +1.68σ recomputes as +1.57σ

Table IV row 1: data 1.696×10⁻², null (1.685±0.007)×10⁻², gives (0.011/0.007) = 1.57, not 1.68. If σ_null is actually 0.0066 truncated to 0.007 in display, the value rounds correctly — but the table should not display a truncated value alongside a derived ratio that requires the un-truncated form.

### P4-m14 — Table III binning changes silently within the table

Row 1 (ℓ=1 single mode) uses nlb=1 (App. A config). Rows 2–5 are bandpowers spanning 5 multipoles each (e.g. ℓ∈[2,6]), implying nlb=5. The joint χ²/dof = 161.2/38 = 4.24 then implies ℓ_max/nlb = 191/5 ≈ 38 bandpowers — consistent with nlb=5 for the joint fit. So Table III mixes nlb=1 (row 1) and nlb=5 (rows 2+) without stating it. **Required fix:** add a binning column.

### P4-m15 — Table V row T7 "qualitative PASS" in a quantitative table

T7 confidence calibration has Threshold = "qualitative" and Result = "PASS". A qualitative entry in a column whose other rows are numerical thresholds and percentages is mixed-type. Either define a quantitative criterion (e.g. Brier score < X) or remove from the table and document separately.

### P4-m16 — "Brick-interior subsample" used in App. C without defining "brick"

App. C: "vanishing to −0.03σ in the brick-interior subsample." DESI Legacy bricks are 0.25°-square sky tiles; "brick-interior" excludes pixels near brick boundaries. This is jargon undefined in the paper.

### P4-m17 — Per-imaging-leg σ decomposition does not combine to the reported full-catalog value

App. C: "full-catalog [0.5, 0.6) confidence bin +3.29σ decomposes as BASS+MzLS +0.30σ / DECaLS +4.50σ / DES +2.46σ."

For independent samples with sub-significance combination, $\sigma_{\rm comb}^2 = \sum \sigma_i^2 w_i^2 / \sum w_i^2$ for some weights $w_i$. Without weights, $\sqrt{0.30^2 + 4.50^2 + 2.46^2} = 5.13$ — far from 3.29. With weights proportional to sample size in each leg, the answer depends on those (undisclosed) sample sizes. The paper does not show that the 3-leg decomposition combines to the reported 3.29σ.

**Required fix:** show per-leg sample sizes and the combination formula.

### P4-m18 — Two-point correlation: 1 of 10 bins exceeds 2σ but no LEE correction is applied

App. C: "consistent with the label-shuffle null at |σ| < 1.2 in 9 of 10 bins; the maximum deviation −2.41σ at θ ≈ 0.5°." A −2.41σ in any of 10 bins has trial-corrected p ≈ 0.16. The paper attributes this to brick-boundary artifacts — but does not first apply LEE before assigning a physical explanation.

### P4-m19 — Sec. III A row (v) cites "$p_{\rm LEE} \leq 10^{-4}$" but App. C clarifies this is the *random-label* null, not the *direction* trial correction

Table I row (v): "max-stat MC, $p_{\rm LEE} \leq 10^{-4}$." App. C: "The direct-MC look-elsewhere test (N=10,000 random-label shuffles) gives $p_{\rm LEE} \leq 10^{-4}$; the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ."

The "LEE" abbreviation in the table refers to a label-shuffle null over MC realizations, not the multi-direction look-elsewhere correction that the abbreviation normally implies (Gross & Vitells). Using "LEE" for two different procedures within the same paper is confusing.

### P4-m20 — Median classification confidence 0.9997 vs. mean 0.951 implies an extreme bimodality but Fig. 6 does not annotate the percentile

Sec. IV A: "Mean classification confidence is 0.951, median 0.9997." The 5-percentile gap between mean and median signals a long lower tail. Fig. 6 shows this qualitatively but does not annotate where the 0.951 mean lies on the curve.

---

## ADDITIONAL NITS

### P4-N6 — Reference labeling: refs [2] and [3] both Shamir 2022

Ref. [2] is Shamir 2022 PASJ, Ref. [3] is Shamir 2022 MNRAS. Both appear as "Shamir (2022)" in the body. Adopt (2022a)/(2022b) disambiguation.

### P4-N7 — Footnote 1 (p. 6) contains its own discussion of artifact paths and reproduction comparisons spanning ~25 lines

This footnote is longer than several paragraphs of body text and includes a numerical comparison ("99.33% of the observed pre-MASTER... vs. 99.32% for the spiral-trial draw"). Move to App. A or supplementary.

### P4-N8 — Eq. (B1) does not state the dimensionality or shape of p(x) or S

S is described as "the permutation matrix swapping the CW and CCW channels (leaving not_spiral unchanged)" — so it's 3×3. The L2 norm $\|p(x_i) - S\,p(\tilde x_i)\|^2$ is over the 3-dim probability vector. State explicitly.

### P4-N9 — App. A's f_sky^eff formula uses ⟨⟩ over "the full sky" but should clarify the normalization

"$f_{\rm sky}^{\rm eff} \equiv \langle W\rangle^2/\langle W^2\rangle$ (means over the full sky)". For a mask with W=0 outside, ⟨W⟩_fullsky = (1/N_pix_fullsky)Σ W_p,in-mask. State whether normalization is N_pix(in-mask) or N_pix(full-sky). This affects the 0.494 / 0.488 / 0.452 / 0.420 values.

### P4-N10 — "BASS+MzLS +0.30σ / DECaLS +4.50σ / DES +2.46σ" — DECaLS-concentration is consistent with DR8 known photometric calibration differences

This deserves a sentence connecting to known DR8 imaging-leg systematics in the literature (DR9/DR10 release notes document this). As stated, the reader doesn't know whether DECaLS is known to be problematic or whether the +4.50σ is novel.

### P4-N11 — Data Availability: "Release tag: v2026.04" but the paper is dated "June 2026" — the catalog was released April 2026 before the paper finalized in June

This is fine, but the gap should be noted: the released catalog corresponds to a snapshot prior to the audit that withdrew the −0.122σ. Confirm the published catalog matches the analyses in the paper.

---

## Audit of additional headline numbers (recomputed)

| Claim | Source | Recomputed | Match? |
|---|---|---|---|
| 28.8σ (Catalog A) | Table II from p=0.5079, σ=0.000279 | 28.32 | ✗ (~2% high) |
| 14.6σ (Catalog B) | Table II from p=0.504 | 14.34 | ✗ (~2% high) |
| 9.5σ (Catalog C) | Table II from p=0.4974 | 9.32 | ✗ (~2% high) |
| +4.42σ hemisphere | Table IV row 2 | 4.37 | ≈ (~1% off) |
| +1.68σ pre-MASTER | Table IV row 1 from displayed inputs | 1.57 | ✗ (~7% off; σ truncation suspected) |
| Joint χ²/dof = 4.24 | Table III | 161.2/38 = 4.242 | ✓ |
| 14.7× bootstrap inflation | App. D | 264.5/18.1 = 14.61 | ≈ ✓ |
| 99.3% leakage reproduction | Table IV | 1.685/1.696 = 99.35% | ✓ |
| Catalog C 1.6× CE-ResNet | Sec. I | 3.201/1.950 = 1.64 | ✓ |
| 1.84% GZ1-diluted threshold | Sec. VI A | 0.75/0.398 = 1.884 | ✓ |
| z ≈ −18.1 inflated | App. D from z=−264.5, factor 14.7 | 264.5/14.7 = 17.99 | ✓ |
| f_sky 0.49005 vs. 0.494 vs. 0.482 | abstract / Table I / App. D | three different masks | Internally distinct, but reader confusion likely |
| Table III ℓ_eff=4 sig | (3.21−?)/0.804 = 6.097 ⇒ implied ⟨null⟩ = −1.69 | implied | ✗ — null mean not displayed (P4-E3) |
| Fig. 8 "2.7σ at ℓ=1" | figure annotation | doesn't match any other ℓ=1 in paper | ✗ (P4-E8) |

---

## Updated recommendation

The new findings reinforce the original **REJECT (resubmit invited)** verdict. In particular:

- **P4-E10** (two different "headline findings" in abstract vs. Conclusions) is a major narrative-coherence failure that compounds the abstract problems already flagged.
- **P4-M11** (z≈−18 vs. "we do not claim frequentist exclusion") is a logical contradiction that the original review missed.
- **P4-M13** (z=−18 from a 1000-realization bootstrap cannot be quoted as a Gaussian σ) is independently disqualifying — the abstract's most quantitatively impressive number is statistically not what it claims to be.
- **P4-E8** and **P4-m14** show that even the figure-and-table-level numerical claims are not internally reproducible.
- **P4-M11 + M12** together suggest the comparison with Shamir is rhetorically inflated in both directions: the 6–12× factor uses a max-fluctuation reference (favorable framing) while the body explicitly disclaims an actual exclusion.

The combination of (a) Table II σ-value off-by-2% across three rows, (b) Table III significances irreproducible without a hidden null mean, (c) Table IV row 1 z-score off by 7%, and (d) Fig. 8's annotated 2.7σ matching no other ℓ=1 result in the paper means the displayed numbers are not internally consistent at the precision a PRD paper requires. Compounded with the larger structural issues (multiple "headline findings", undisclosed estimator families introduced in appendices, logical contradiction in the Shamir comparison), the manuscript needs a thorough numerical audit and rewrite before resubmission.