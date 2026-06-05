# P4 R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: Claude_brutal
**Model**: claude-opus-4-7
**Input**: NATIVE PDF + adaptive thinking + effort=high
**Wall time**: 189.8s

---

# Referee Report — P4 (Survey-Scale Galaxy Chirality with Equivariant TTA)

## Overall assessment

This is a 10-page methods paper that, on careful reading, headlines a null (−0.122σ on the subsample mask) while burying a +3.64σ moment-ratio canonical-mask result that the authors themselves attribute to systematics — but only after admitting (in passing) that the same number corresponds to an empirical rank p of 0.030, i.e. ~1.9σ Gaussian-equivalent. This is exactly the kind of "which mask did you pick, and why?" worry that PRD reviewers must flag. The paper also leaks at least one internal version-history phrase, contains several arithmetic mismatches in the headline table, and uses a sensitivity floor defined on a 471k-spiral HC subsample to characterize an analysis run on 3.2M spirals. The bias-hardening and MASTER work are real and competent, but the paper as written does not yet meet PRD standards of internal consistency and disciplined claiming.

---

## ESSENTIAL findings

### P4-E1. Internal version-history leak in the body
**Section IV D, page 4.** Quote: *"The canonical-mask direct-MC ℓ = 1 value of +3.64σ and the local hemisphere maximum of 3.05σ **were interpreted in earlier paper versions** as mask-geometric leakage of the global 9.5σ monopole."*

This is internal-bookkeeping language that a published paper cannot carry. The paper must either describe the current interpretation in standalone form or remove the temporal reference entirely.

**Fix:** Delete "were interpreted in earlier paper versions as" and rewrite as: "We interpret … as …".

### P4-E2. Headline +3.64σ moment-ratio is incompatible with the empirical rank p = 0.030
**Abstract (page 1) and Sec. IV D / Table III (page 5).** Abstract: *"The post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σ_null moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)."*

A 3.64σ Gaussian event has two-sided p ≈ 2.7×10⁻⁴, not 0.030. The fact that the empirical rank says ~1.9σ means the null distribution is strongly non-Gaussian and the moment-ratio "σ" is misleading by more than a factor of 1.9 in significance units. Despite this, the moment-ratio +3.64σ is used in five places (abstract, Table I, Table III, Sec. IV D, Sec. VII) as if it were the headline. PRD does not permit this kind of double-bookkeeping.

**Fix:** Replace +3.64σ throughout with the empirical-rank Gaussian-equivalent (~1.9σ) as the primary number, and confine the moment-ratio z to a footnote that explicitly states the null is non-Gaussian.

### P4-E3. Table II arithmetic does not match the stated formula
**Table II, page 4.** With σ = √(p(1−p)/N) = √(0.25/3,201,160) = 2.794×10⁻⁴ = 0.000279 (as the table states), the deviations should be:
- Catalog A: 0.0079 / 0.000279 = **28.32σ** (table says 28.8)
- Catalog B: 0.004 / 0.000279 = **14.34σ** (table says 14.6)
- Catalog C: |−0.0026| / 0.000279 = **9.32σ** (table says 9.5)

All three values are inflated. Either the fractions have more decimal places than printed, or N differs across tiers, or the σ formula is not the one stated. A table of three numbers cannot have three arithmetic inconsistencies in a PRD submission.

**Fix:** Either give fractions to enough digits to reproduce the σ exactly, or report the actual N and binomial σ used for each tier.

### P4-E4. The "3.86× asymmetry-suppression factor from +2.05% to −0.53%" does not reconcile with Table II
**Sec. IV B, page 4.** Table II Catalog A says +0.79% CW *excess* (i.e. +1.58% asymmetry under the standard A=(CW−CCW)/(CW+CCW) definition). Table II Catalog C says −0.26% excess (−0.52% asymmetry). The ratio 1.58/0.52 = **3.04×**, not 3.86×. Meanwhile, Sec. VI says raw bias is "only 0.79%" (excess), which is consistent with Table II but not with "+2.05%".

Where does +2.05% come from? It is never defined. Either there is a third unit convention silently in play, or the suppression factor is computed inconsistently.

**Fix:** State the asymmetry definition explicitly and reconcile +2.05% with the +0.79% CW excess shown in Table II.

### P4-E5. Table IV z mis-arithmetic
**Table IV, page 5.** Row 1: data 1.696×10⁻², null (1.685±0.007)×10⁻². Then z = (1.696−1.685)/0.007 = **1.571**, not +1.68. Row 2: (3.48−1.69)/0.41 = **4.366**, not +4.42. These are small but, again, in a four-row table this is unacceptable.

**Fix:** Recompute or extend the printed precision of the null mean/std so the printed z matches.

### P4-E6. The "primary" subsample mask is a strict superset of the diagnostic canonical mask, yet only the diagnostic mask shows structure
**Sec. III A, Sec. IV C–D.** If fsky = 0.659 (subsample) is a strict superset of fsky = 0.49005 (canonical), then any true ℓ=1 signal present in the canonical sub-region must, by linearity of the spherical-harmonic projection, also be present in the larger mask — possibly diluted, but not flipped from +3.64σ to −0.122σ. The paper's narrative says the canonical-mask number is monopole-leakage through a more-patchy geometry; that is a plausible explanation, but the abstract does not honestly state that the choice of "primary" estimator was made *after* observing the diagnostic mask. PRD requires the analysis-mask choice to be pre-registered or its discriminating logic to be derivable from blinded systematics tests. The paper does not establish either.

**Fix:** Either (i) provide a clearly *prior* (mask-blind) argument for preferring the subsample mask, or (ii) demote the headline to a range "[−0.122σ, +3.64σ] depending on mask choice; we attribute the latter to systematics on the grounds of A, B, C," and remove the phrase "headline null" from the abstract.

### P4-E7. Look-elsewhere logic is internally contradictory
**Sec. VI / Appendix C, pages 6 and 8.** The paper claims a hemisphere local maximum of 3.05σ, then states *"the direct-MC look-elsewhere test (N = 10,000 random-label shuffles) gives pLEE ≤ 10⁻⁴"*, and then in the same paragraph: *"the conservative Bonferroni/BH penalty across ∼650 tested directions reduces post-LEE significance to <1σ"*. These two statements are mutually exclusive: either the direct-MC null already integrates over the look-elsewhere search (in which case the residual is genuinely ≤10⁻⁴ and Bonferroni is double-counting), or it does not (in which case the ≤10⁻⁴ number is not a look-elsewhere-corrected p-value and should not be labeled "LEE"). Pick one.

**Fix:** Clarify exactly what the direct-MC max-statistic null does (per-direction or over-direction), and report a single LEE-corrected p.

---

## MAJOR findings

### P4-M1. Training-label circularity is acknowledged but not propagated
**Sec. II B, page 2.** "67.6% of training labels derive from CE-ResNet predictions." The headline 93.7% accuracy is therefore largely agreement with another ML model. The GZ1-only cross-match accuracy is 69.91% (κ = 0.40), which is the *real* independent number. The paper says this is propagated "via the sub-percent systematic floor in Sec. IV C," but Sec. IV C does not show a quantitative propagation — only the empirical 0.75% threshold from injection-recovery. The 30% label noise from an independent benchmark is never put into a noise budget on the dipole amplitude.

**Fix:** Add a quantitative propagation: given κ=0.40, derive the dilution factor on a true cosmological dipole and re-express the sensitivity floor in deprojected (true-underlying) amplitude.

### P4-M2. "High-confidence" naming is inconsistent
**Abstract vs Appendix E.** Abstract: HC = pᵉᑫ_CW > 0.9, N = 471,049. Appendix E: "HC-broad-0.6 (pᵉᑫ > 0.6, N = 949,584)" and "HC-strict (pᵉᑫ > 0.8, N = 624,660)". So peq>0.9 is tighter than what the appendix calls "HC-strict" but is itself just labeled "high-confidence" in the abstract. A reader cannot tell which HC is meant where.

**Fix:** Rename consistently (e.g. HC₀.₆, HC₀.₈, HC₀.₉) and use one nomenclature throughout.

### P4-M3. Sensitivity floor measured on the wrong sample
**Sec. VI A, page 6.** The empirical 50%-recovery-at-3σ threshold (A=0.75%) is measured on the 471k HC₀.₉ subsample, but the headline analysis uses 3.2M spirals. With 6.8× more galaxies, the statistical floor should be ~√6.8 ≈ 2.6× tighter. The paper's falsification criterion is therefore set on a different (much smaller) sample than the analysis itself. Either justify why HC-only is the relevant baseline for the full-sample analysis, or quote the floor for the actual analysis sample.

### P4-M4. fsky = 0.46 appears without explanation in the Fisher floor
**Sec. VI A, page 6.** Fisher floor: "σ(A/2)≈0.048% at Nspiral=3,201,160, fsky=0.46". But the canonical mask is fsky=0.49005 and the subsample mask is fsky=0.659. Where does 0.46 come from?

### P4-M5. The classifier excess is "spatially uniform" but the dipole is mask-leaked from it
**Sec. IV B and IV D.** The paper argues simultaneously that (a) the 9.5σ monopole excess is spatially uniform across 7 RA slabs (within 0.5% of 50/50), and (b) that this uniform monopole leaks through patchy mask geometry to produce 99.3% of the observed pre-MASTER ℓ=1 power. Statement (a) is the basis for "does not produce a dipole"; statement (b) is the basis for the leakage explanation. These can be reconciled (mask geometry breaks uniformity by projection), but as written, the two paragraphs sit four sections apart and contradict on first reading. Make the reconciliation explicit.

### P4-M6. The χ²/dof = 4.24 in Table III is never discussed
**Table III, page 5.** "Joint χ²/dof (38 bandpowers) — 161.2/38 = 4.24 — Dominated by mask-coupled monopole". A reduced χ² of 4.24 over 38 dof is a 9σ-class rejection of the white-noise null but is dismissed with "dominated by mask-coupled monopole" without showing the spectrum after monopole-leakage modeling. If the broadband structure is real systematic, show the residuals after subtracting the modeled monopole-leakage; otherwise the table is the strongest evidence in the paper that something is unmodeled.

### P4-M7. Two different bandpower conventions for "ℓ=1" used without disambiguation in the abstract
The "single mode" ℓ=1 (single-bin) and the diagnostic ℓ_eff=4 (bandpower over [2,6]) are different objects. The abstract reports −0.122σ as the single-mode value; Table III reports +6.097σ at ℓ_eff=4 on what is essentially the next-lowest bin. A non-expert reader can easily misread the headline as overall low-ℓ being null.

**Fix:** State explicitly in the abstract that the headline is the *single-multipole bin* ℓ=1, and disclose that the adjacent low-ℓ bandpower shows large structure attributed to systematics.

### P4-M8. The catalog/HuggingFace links should be checked
The data-availability section gives URLs (`huggingface.co/datasets/bamfai/galaxy-chirality-catalog`, `bamfai/galaxy-chirality-v2`, and a GitHub URL). Editors should verify these resolve before publication; if they do not, the reproducibility claims become non-falsifiable.

### P4-M9. "Strict-superset subsample mask" is asserted but never explicitly demonstrated
**Sec. IV C / Table I.** The geometric relationship "subsample ⊃ canonical" is asserted but no figure or quantitative pixel-overlap fraction is provided. Given that the entire mask-choice argument turns on this, the paper needs at least a one-line statement like "every canonical-mask pixel is contained in the subsample mask; the subsample mask adds X% additional pixels selected by criterion Y." If they are not in fact nested, the leakage argument is structurally weaker than presented.

---

## MINOR findings

### P4-m1. No figures
The paper contains five tables and zero figures. For a paper whose central diagnostic is the angular power spectrum of an asymmetry map, the absence of (i) the asymmetry map itself, (ii) the bandpower spectrum with null band, (iii) the null distribution showing the non-Gaussianity that drives E2, is striking. Consider adding at minimum a map + Cℓ plot.

### P4-m2. "C² 2°" notation
**Appendix A & D.** "C² 2° apodization" is used twice without expansion. Spell out "cosine-squared, 2° apodization scale" on first use.

### P4-m3. Reference list has minor formatting inconsistencies
[1]/[2] are split such that the abstract cites Shamir (2020) as [1] but Shamir (2022) as [3] (with [2] being the PASJ paper). Order is not strictly chronological and the in-text "Shamir [1, 3, 4]" reads oddly. Reorder.

### P4-m4. "Catalog C residual (9.5σ from 0.5000)"
The locution treats a 9.5σ deviation as a residual being downplayed. While the explanation (uniform monopole → no dipole) is acceptable, the rhetorical move "9.5σ is fine because uniform" should be flagged with at least a footnote acknowledging that 9.5σ is, in absolute terms, a large classifier bias.

### P4-m5. Several deprecation-like adjectives
Phrases such as "non-headline, systematics-attributed value" (Sec. IV D) and "non-headline" (Sec. VII) read like internal-status flags. Replace with neutral language describing the role of the diagnostic.

### P4-m6. Edge-on fraction ratio
**Appendix E.** "65.7% of b/a<0.3 receive CW/CCW" is described as a contamination but no quantitative impact on the dipole noise budget is given beyond the qualitative "5–8%".

### P4-m7. "spatial coordinate slabs"
**Sec. IV B.** "all 7 equatorial coordinate slabs within 0.5% of 50/50" — show the table.

---

## NIT findings

### P4-n1. Date in masthead
"Dated: June 2026" — verify the intended date.

### P4-n2. Author block
"Independent Researcher, Los Angeles, California, USA" + a non-academic email. PRD generally requires institutional affiliation or a clearer statement; not a publication blocker but the editor should confirm policy compliance.

### P4-n3. PACS codes
PACS has been deprecated by APS for years; use PhySH/PACS-equivalent classifications if PRD now requires them.

### P4-n4. "1.6×" overlap claim
"survey-scale coverage of 8.47 million galaxies (3,201,160 equivariant-classified spirals, 1.6× CE-ResNet's scale)" — 3.20/1.95 = 1.64×, fine, but CE-ResNet's 1.95M is the *spiral* number; the 8.47M vs 1.95M comparison would actually be 4.3×. Be clear which comparison is meant.

### P4-n5. Length appropriate
10 pages including 5 appendices for a null result with a substantial methods + systematics audit is acceptable. No length cut required.

---

## Summary recommendation

**MAJOR REVISIONS**

The headline science (a careful null on a sub-percent chirality dipole using 3.2M spirals plus a worked monopole→ℓ=1 leakage mechanism) is genuinely useful and would be a fine PRD contribution. However, the paper currently (i) leaks an "earlier paper versions" phrase into the body, (ii) reports a +3.64σ moment-ratio side-by-side with a ~1.9σ empirical-rank significance for the *same* observable without picking a primary, (iii) has three arithmetic mismatches in Table II and two more in Table IV, (iv) carries unreconciled numerical mismatches between the asymmetry-suppression ratio (3.86×) and Table II (3.04×), (v) makes a primary/diagnostic mask choice that, by the paper's own logic, post-selects the null, (vi) presents contradictory look-elsewhere arithmetic, and (vii) contains no figures despite being a map-based power-spectrum analysis. None of these are fatal individually, but the cumulative signal is a paper that needs another full pass for internal consistency, mask-choice justification, and disciplined sigma reporting before it can be accepted.