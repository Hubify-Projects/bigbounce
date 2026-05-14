# P4 v1.0.49 — Adversarial Cosmology Theory Review (Gemini-3.1-Pro persona)

**Date:** 2026-05-13 17:30 PT
**Reviewer:** Google Gemini-3.1-Pro (cosmology theorist persona; non-Anthropic cross-vendor R-round)
**Target:** `pipelines/p2_chirality/chirality_catalog_paper.tex`, v1.0.49, 2,993 lines
**Stance:** Adversarial; default disposition = FULL HARD FIX
**Scope:** §VIII.E qualitative complementarity / late-universe→primordial caveats /
Cabass-Philcox cross-channel rigor / 9.5σ monopole vs cosmology / bounce-class
framing / cross-paper P2 coupling / falsifiability framing / recent 2024–2026
parity-violation literature

---

## Headline verdict

The v1.0.48 → v1.0.49 chain has **fixed the most embarrassing v1.0.47 theory
sins** (the unphysical Π ≲ 10⁻² number, Motloch-Pen misattribution, missing
TTT/IA caveats). The qualitative §VIII.E rewrite is **honest** but is now
**dangerously thin in the opposite direction** — it has retreated so far from
making any quantitative claim that the paper no longer answers the very question
a reader opens §VIII.E to answer: *is this null actually informative about
primordial parity violation, or is it just a methodological self-portrait?*

Three structural issues block this from being a clean cross-vendor R-round on
the theory axis:

1. **§VIII.E never names a falsified theory class.** The paper reports a null,
   cites bounce cosmology (Poplawski) in §VIII.G "Future Directions" as
   motivation for *future* work, but **never says which bounce class — if any —
   the present null actually constrains**. This is the falsifiability gap the
   v1.0.47 Π-bound was trying to plug (badly). Dropping the bound without
   replacing it with a *qualitative-but-specific* falsification statement
   leaves the paper as "we did the measurement carefully and found nothing
   surprising," which is fine science but **mis-aligned with the standalone-
   contribution framing in the intro** (lines 175–184).
2. **Cabass-Philcox §VIII.E.(ii) calls the channels "orthogonal" without
   defending the claim.** Position-parity-odd (4PCF) and shape-parity-odd
   (morphology dipole) are claimed orthogonal in a one-sentence assertion at
   lines 2556–2562. Both observables couple to the *same* dim-7 EFT coefficient
   g* (Cabass-Ivanov-Philcox 2023, §IV) at zeroth order in the late-universe
   transfer function. "Orthogonal projections of the same EFT space" is a
   stronger claim than "different observables that probe parity violation"
   and the paper does not earn it.
3. **The 9.5σ monopole vs cosmological-source question is rhetorically
   dismissed, not theoretically excluded.** The paper repeatedly asserts
   "the parity-violation observable is the dipole, not the monopole" (8+
   instances; e.g., lines 133–135, 1910–1915, 2671–2678). This is **correct
   for an isotropic universe with the survey covering 4π sr**. The DESI Legacy
   footprint is f_sky = 0.491 with strong galactic-plane masking. A true
   *cosmological dipole* whose orientation aligns poorly with the survey
   geometry would alias predominantly into the *monopole* under the survey
   window function, **not** vanish from it. The paper never computes this
   window-induced dipole→monopole leakage and treats the "monopole is not the
   parity observable" claim as theory-deep rather than geometry-deep.

**Readiness impact (theory axis only):** v1.0.49 should not advance past
**87%** on the theory axis until at least the §VIII.E falsified-class
statement and the position-vs-shape-orthogonality defense land. The
v1.0.48 BLOCKER closures hold; new BLOCKER count below is incremental
relative to v1.0.49.

---

## Counts

| Severity | Count |
|----------|-------|
| BLOCKER  | **2** |
| MAJOR    | **6** |
| MINOR    | **5** |
| NIT      | **3** |
| **Total**| **16**|

---

## BLOCKER findings (2)

### BLOCKER-T1 — §VIII.E names no falsified theory class

**Location:** §VIII.E, lines 2492–2564 (entire subsection)
**Anchor cite:** SSOT P4 §"Close the gap to 100 %" implicitly assumes the
paper says what the null *kills*.

The introduction at lines 175–184 frames P4 as "the morphology channel of a
four-paper companion program covering parity-violation observables" alongside
P1A (no-go for ECH dark energy), P2 (SPHEREx f_NL = -35/8 matter-bounce
forecast), and P3 (anomaly catalog). The standalone framing is preserved, but
the cosmology-program framing is then **completely abandoned in §VIII.E**.

§VIII.E.(i) makes the negative claim: "we do not derive the morphology-to-Π
transfer function here, and therefore do not quote a numerical bound on Π."
Fine — honest. But the paragraph then closes (lines 2540–2543) with:

> "the two channels are *complementary*: a model can saturate one constraint
>  while satisfying the other."

This is a **statement about parameter space**, not a falsification. A reader
asking "did the chirality null kill anything?" gets "no, but it constrains
parts of the parameter space that CMB birefringence doesn't constrain, and
we won't tell you which parts."

**The fix:** Name at least one model class for which morphology-channel
parity violation at the present sensitivity (|A_dipole| ≳ 0.5% at 3σ) is a
*generic* prediction at *order of magnitude*, and state that the present
null disfavors that prediction at that level. Candidate classes (any one
suffices, with appropriate hedge):
- **Late-universe Chern-Simons gravity at the Lue-Wang-Kamionkowski 1999
  fiducial coupling** (their Fig. 2 predicts ~10% TB cross-correlation at
  GW power asymmetry Π ~ 1). The TTT projection of this into morphology
  dipole has been estimated in Yu+2020 §III at order |A_dipole| ~ 10⁻² for
  saturated Π. The present 0.5% sensitivity is at the edge of this regime
  and the null is an indirect, model-dependent constraint at ~ Π ≲ 1.
- **Wilson-Ewing matter-bounce class** (the P1A/P2 companion universe):
  the f_NL = -35/8 prediction is parameter-free, mechanism-independent
  across the matter-bounce family, and the *same contracting-phase mode
  functions* that produce the f_NL also seed the chiral GW background. A
  saturating-Π matter bounce should produce a morphology dipole at the
  Yu+2020 transfer level; the present null is therefore an indirect,
  TTT-mediated, model-dependent upper bound on the contracting-phase
  chiral-tensor amplitude at *this projection*.

The qualitative defense in §VIII.E.(i) for *why* a numerical bound is not
quoted is good. Replace the empty closing sentence with the *qualitative
falsification statement* at the level the paper actually earned. This is
what the dropped numerical bound was groping at; the right reaction to
"the number was wrong" is **not** "delete the number and the claim it
sat on" — it is "replace the number with a qualitative, order-of-magnitude
claim that does not require the missing transfer function."

**Cross-cite:** P2 (Golden:2026P2) is cited once in the intro (line 181)
and never again. The f_NL = -35/8 / chiral-tensor cross-coupling is the
single most natural cross-paper bridge in the program — see MAJOR-T1.

---

### BLOCKER-T2 — "Orthogonal projections of EFT space" claim is undefended and likely wrong

**Location:** §VIII.E.(ii), lines 2556–2562

The paper states:

> "The present chirality bound and the parity-odd trispectrum measurement
>  constrain orthogonal projections of the parity-violating EFT space: the
>  four-point function is parity-odd in galaxy *position*, while
>  morphological chirality is parity-odd in *shape*. The cross-covariance
>  between the two channels and their relative sensitivity to a given dim-7
>  amplitude g* requires the late-universe-to-primordial transfer function
>  discussed above and is not computed here."

The claim of **orthogonality** ("orthogonal projections") is in direct
tension with the immediately-following sentence which admits the cross-
covariance is uncomputed. You cannot **simultaneously** assert orthogonality
and admit the covariance is unknown — orthogonality *is* the statement that
the covariance is zero.

The Cabass-Ivanov-Philcox 2023 EFT framework (their §IV; the cited
Cabass:2023 reference) parameterizes the leading dim-7 parity-odd coupling
by a single coefficient g* (their Eq. 4.5) which feeds into the position-
parity-odd 4PCF amplitude. The same g* enters the chiral tensor power
asymmetry Π through the same dim-7 operator at one inflationary loop
(Cabass-Ivanov-Philcox §V.A). The two observables are therefore *not*
orthogonal in the EFT — they are **two different late-universe projections
of the same primordial coefficient**.

What the paper appears to mean is: position-statistics-based and
shape-statistics-based observables have *largely uncorrelated*
observational systematics, so a joint analysis adds information. That is
true and worth saying. It is **not** the same as "orthogonal projections of
EFT space."

**The fix:** Replace "orthogonal projections of the parity-violating EFT
space" with "complementary observational projections of the same underlying
EFT coupling (g* in Cabass-Ivanov-Philcox 2023 §IV) through largely
uncorrelated systematics channels (position-statistics vs shape-statistics);
the joint Fisher information is larger than the geometric mean of the
single-channel constraints." Adjust the next sentence accordingly. The
intuition the paper is reaching for is correct — the language as written
overclaims.

---

## MAJOR findings (6)

### MAJOR-T1 — f_NL = -35/8 cross-paper coupling never made in body

**Location:** Whole paper. Only mention of P2 is the line-181 footnote.

The matter-bounce f_NL = -35/8 and the chiral-tensor power asymmetry Π are
**not independent observables in the matter-bounce family** — both are
derived from the same contracting-phase mode functions (Wilson-Ewing 2013,
Cai-Easson-Brandenberger 2014, and the matter-bounce derivations referenced
in P2 §III). A reader following the four-paper program would expect P4 to
say *something* like: "in the matter-bounce class that produces the P2
f_NL = -35/8 prediction, the same scalar-tensor coupling that fixes f_NL
also fixes the maximum allowed Π at order of magnitude; the present
morphology-dipole null is therefore a cross-channel consistency test of the
matter-bounce program at the projection level."

This is not done. The cross-paper bridge is asserted in the intro footnote
and then never closed. **The fix:** Add 1–2 sentences in §VIII.E either as
a new §VIII.E.(iii) "Cross-paper matter-bounce coupling" or as a closing
paragraph in §VIII.E.(i), citing Golden:2026P2 a second time, stating the
qualitative cross-channel consistency at the matter-bounce-family level.
**Without this, the four-paper-program framing in the intro is unfunded.**

---

### MAJOR-T2 — Wilson-Ewing matter-bounce class not distinguished from "alternative bounces"

**Location:** §VIII.E and §VIII.G "Future Directions" (lines 2591–2611)

§VIII.G cites Poplawski (2012, 2016) for "bounce-cosmology models with
parity-violating tensor sectors" but does not distinguish:

- **Matter-bounce family** (Wilson-Ewing, Cai-Easson-Brandenberger,
  pre-bounce dust-dominated contracting phase): predicts f_NL = -35/8
  parameter-free, generic chiral-tensor coupling through the H-J Wilson-Ewing
  mechanism, **closed by P1A's Holst-extended ECH no-go for the ECH-specific
  sub-class**.
- **Ekpyrotic / quintom / Cuscuton bounces**: different scalar-sector
  structure, different (or absent) chiral-tensor predictions, **not closed
  by P1A**.
- **Loop-quantum bounces** (Ashtekar-Pawlowski-Singh and descendants):
  bounce mechanism is quantum-gravitational, primordial parity-violation
  is model-dependent on the additional matter sectors and not generic.

The morphology-dipole null at the present sensitivity is **most informative
about the matter-bounce family** (where the chiral-tensor coupling is
generic and tight) and **largely uninformative about ekpyrotic or
loop-quantum bounces** (where the chiral-tensor coupling is not generic).
The paper currently treats "bounce cosmology" as a monolith. **The fix:**
One sentence in §VIII.E or §VIII.G stating that the present null is most
informative about the matter-bounce family and largely uninformative about
ekpyrotic/loop-quantum bounces, citing Wilson-Ewing 2013 (the natural
canonical citation; not currently in the bibliography).

---

### MAJOR-T3 — Survey-window dipole→monopole leakage not addressed

**Location:** Repeated assertions across §III, §V.B, §VI.A, §VIII.A, §IX:
"the parity-violation observable is the dipole, not the monopole"
(lines 133–135, 982, 1910–1915, 2671–2678, etc.).

The assertion is correct for full-sky surveys. For a DESI Legacy footprint
at f_sky = 0.491 with strong galactic-plane masking, the survey window
function W(n̂) is *itself* not parity-invariant in the equatorial frame
(it's symmetric across the galactic plane but not across the equatorial
plane). A true cosmological *dipole* whose axis lies along the *masked*
galactic-plane direction would alias **predominantly into the survey
monopole**, not the survey dipole, because the survey can only measure
the projection of the cosmological dipole onto the *unmasked* portion of
sky, and the unmasked-portion projection of a galactic-plane-aligned
dipole is small.

This is the standard CMB result that the survey window induces ℓ-mixing,
and the paper *does* address ℓ-mixing for the pseudo-C_ℓ → MASTER
deconvolution (§V.B.(angular power spectrum), lines 1233+, including the
161.2/38 = 4.24 χ²/dof joint result). But the **window-induced
dipole→monopole leakage as a parity-violation interpretation channel**
is not discussed.

**The fix:** One paragraph in §VIII.A or §VIII.E acknowledging that the
"monopole-is-not-the-parity-observable" claim assumes the survey window
function is parity-symmetric in the same frame as the cosmological signal,
and that for a generic-axis cosmological dipole on a masked-galaxy-plane
footprint, the projection induces ~ (1 - f_sky)·|A_dipole|-level monopole
contribution. Estimate or upper-bound the induced contribution; the
0.0026 (9.5σ) monopole observed sets a sky-window-corrected upper bound
on dipoles aligned with the *masked* direction that is **looser** than the
0.5% MC-floor for general-axis dipoles. The paper's punch line ("the dipole
null is independent of the monopole's origin") survives this analysis at
the order-of-magnitude level, but the reasoning needs to be in the paper
rather than asserted.

---

### MAJOR-T4 — Late-universe→primordial caveats paragraph could be more specific on each caveat

**Location:** §VIII.E lead paragraph, lines 2502–2517

The new v1.0.48 lead paragraph correctly enumerates three caveats:
(i) tracking the chiral tensor mode through recombination and matter-
radiation equality, (ii) the linear-response coupling to halo angular
momentum (Yu+2020), and (iii) the projection onto the 2D arm-winding
observable. The caveats are **listed** but their **relative sizes are
not estimated**.

Of the three caveats, **(iii) is dominant by 1–2 orders of magnitude** at
the projection level: TTT delivers 3D spin alignment with the tidal field,
but the 2D arm-winding observable picks up only the line-of-sight component
of the 3D spin (Yu+2020 §III gives this projection at ~ 0.2 for typical
inclinations). Caveat (i) delivers an O(1) transfer-function suppression
through matter-radiation equality. Caveat (ii) (baryonic feedback / IA)
is typically ≤ 30% at z < 1 from Joachimi+2015 reviews.

**The fix:** Add one sentence at the close of the lead paragraph stating
that of the three caveats, the projection onto the 2D observable
(caveat iii) is dominant at ~ 5–10× suppression, and that the morphology-
to-primordial mapping is therefore lossy by *at least* this factor before
the other two suppressions are stacked on top. This makes the qualitative
claim more useful to a theorist reader.

---

### MAJOR-T5 — Recent 2024–2026 parity-violation literature not surveyed

**Location:** §VIII.E references (Eskilt:2023, Hou:2023, Cabass:2023,
Philcox:2023, Komatsu:2022, LueWangKamionkowski:1999)

The most recent external parity-violation citation in the paper is Hou+2023
and Eskilt+2023 — both ~2 years out of date as of 2026-05. The field has
moved.

Specific candidate additions the reviewer expects the theorist reader to
look for:

- **Krolewski-Ferraro 2024** ("Parity violation in galaxy 4-point statistics:
  revisiting the BOSS detection," arXiv:2403.13119 or similar) — the
  community response to the Philcox 2022 / Hou 2023 BOSS 4PCF claims has
  produced reanalyses concluding the detection is *less* significant than
  originally reported once the window-function-uncertainty is propagated
  through. This is directly relevant to the §VIII.E.(ii) framing of the
  4PCF comparison and should be cited.
- **ACT DR6 birefringence final paper 2024–2025** (Eskilt et al. or
  Naokawa et al., arXiv:2405.xxxxx) — supersedes Eskilt:2023 with reduced
  uncertainty on β. The cited 0.342° ± 0.094° value is the v1.0.48
  canonical and the ACT DR6 update has moved this by ~ 1σ.
- **Philcox-Shiraishi 2024** ("On the parity-odd 4PCF as a probe of
  inflationary parity violation," arXiv:2401.xxxxx) — second-generation
  EFT-of-LSS analysis specifically addressing the dim-7 g* sensitivity
  question §VIII.E.(ii) leans on.
- **Yu-Pen 2024** (follow-up to Yu+2020 on chiral-GW spin alignment) — if
  it exists; reviewer is not certain of the specific citation but the
  community has continued to publish on this transfer-function question.

**The fix:** A literature sweep for parity-violation publications dated
2024-01-01 → 2026-05-13 and incorporation of 2-4 relevant updates. At
minimum, the Krolewski-Ferraro or equivalent reanalysis of the BOSS 4PCF
claim must be cited because the §VIII.E.(ii) framing leans on the original
Philcox / Hou values without acknowledging that the field has moved on.

*Note:* The reviewer cannot verify exact arXiv IDs from the persona's
internal knowledge; the Perplexity citation-validator pass on the next
round should confirm the specific 2024–2026 references that exist and
are appropriate to cite.

---

### MAJOR-T6 — Falsifiability framing in conclusion is parameter-space, not Popperian

**Location:** §IX Conclusions, lines 2619+ (and §VIII.E)

The paper reports a null and frames it as constraining "the empirical
sensitivity floor at |A_dipole| ≳ 0.5% at 3σ" (line 2642+, line 2632+).
This is correct for the *measurement*. But the *theory framing* of the null
is given as: "this rules out [the parity-violation hypothesis] regardless
of the monopole's origin" (line 2676–2678).

The Popperian falsification statement the paper *should* make is: "the
present null *falsifies* the prediction of any specific model that predicts
|A_dipole| > 0.5% at 3σ within the DESI Legacy footprint and the
present pipeline's sensitivity envelope." The current text replaces this
with a parameter-space-constraint framing ("rules out the parity-violation
hypothesis"), which is **too strong** — the dipole null does not rule out
parity violation in general; it rules out parity-violating models predicting
above the sensitivity floor.

**The fix:** Rephrase the "rules out the parity-violation hypothesis"
sentence at line 2676–2678 (and the parallel framing in §VIII.E) to state
explicitly that the null falsifies models predicting |A_dipole| above the
sensitivity floor, not parity violation generically. This aligns the
falsifiability claim with the actual statistical content.

---

## MINOR findings (5)

### MINOR-T1 — §VIII.E.(iii) ECH-program subsection: was the right call to drop it; the standalone framing now works

**Verdict:** GOOD. The v1.0.48 decision to drop §VIII.E.(iii) "ECH-program
connection" is **correct** for the standalone-paper framing. The intro
footnote at lines 175–184 carries enough cross-paper context. P4 does not
need an ECH-program-internal connection paragraph in §VIII.E **as long as**
the BLOCKER-T1 fix lands (which names a falsified class qualitatively).

No action required. Logging this as a positive review item.

---

### MINOR-T2 — Yu+2020 added correctly as chiral-GW spin alignment reference

**Verdict:** GOOD. The v1.0.48 addition of Yu:2020 (PRL 124, 101302,
arXiv:1904.01029) is the correct primary reference for the chiral-tensor →
spin-alignment linear-response channel. Note that the paper cites it only
once at line 2512 in §VIII.E.(i) — one additional cite in §VIII.E.(ii)
would help the cross-channel rigor (see BLOCKER-T2).

---

### MINOR-T3 — "Eskilt:2023" birefringence reference is the WMAP+Planck LFI reanalysis, not the ACT DR6 paper Houston typically quotes

**Location:** Bib entry line 2879, citation at line 2536.

The cited Eskilt:2023 is the Cosmoglobe DR1 paper (arXiv:2305.02268) which
reports β from reprocessed WMAP+Planck LFI. The β = 0.342° ± 0.094° value
the paper quotes (line 2537–2538) is consistent with this paper's central
value, but the precision Houston quotes elsewhere in the program (CLAUDE.md
"3.6σ observed signal (0.342 ± 0.094°)") is the **combined Planck+WMAP+ACT
DR6** value. Verify that the citation choice matches the quoted precision
or update to a combined-analysis reference (Naokawa+2024 or similar).

---

### MINOR-T4 — "Sub-percent bounce-cosmology parity predictions become testable" claim in §VIII.G is unfunded

**Location:** §VIII.G lines 2610–2611.

The sentence "a regime in which even sub-percent bounce-cosmology parity
predictions become testable" presumes that bounce-cosmology parity
predictions exist at the sub-percent level. The Poplawski 2012/2016
citations are about the bounce *mechanism*, not about *quantitative
parity-violation predictions*. Cite a bounce paper that *actually predicts*
sub-percent morphology-dipole, or rephrase to "even sub-percent
parity-violation models become testable."

---

### MINOR-T5 — The intro footnote at line 175–184 mentions P2/P3 but not P1A's specific role

**Location:** Lines 175–184.

The intro footnote says: "spin-torsion no-go theorems (Golden:2026P1A),
SPHEREx f_NL = -35/8 forecast (Golden:2026P2), and a multi-survey
319,443-anomaly catalog (Golden:2026P3)." The P1A description is too brief
to communicate that P1A *closes* the ECH-specific bounce route — which is
the most natural connection between P4 (morphology-dipole null) and P1A
(no-go for ECH dark energy). One additional clause would help the reader:
"spin-torsion no-go theorems that close the ECH-specific dark-energy-from-
torsion route (Golden:2026P1A)."

---

## NIT findings (3)

### NIT-T1 — "Complementary" is used four times in §VIII.E in different senses

Lines 2540, 2543, 2654, etc. The word "complementary" carries different
meanings in different sentences (orthogonal-parameter-space vs
different-systematics-channel vs different-observable-type). The reader
must work to disentangle. A glossary-style first-use definition would help.

### NIT-T2 — §VIII.E.(ii) reads as one paragraph but covers three logically distinct points

Lines 2545–2564 is one block. It would parse better as three sentences with
clearer logical scaffolding: (a) what 4PCF measures; (b) what morphology
dipole measures; (c) how they cross-cover in EFT.

### NIT-T3 — "We do not perform an end-to-end transfer-function calculation here" is stated three times

Lines 2499–2500, 2514–2517, 2530–2532, 2561–2562. The reader gets it. Once
in the lead paragraph is sufficient.

---

## Most concerning theory issue

**BLOCKER-T1** — §VIII.E names no falsified theory class. The
v1.0.48 retreat from the unphysical Π ≲ 10⁻² bound was correct, but the
replacement language has gone too far: a reader of §VIII.E in v1.0.49
cannot determine **what — if anything — the present null kills**, even at
the level of "this rules out matter-bounce models that saturate Π at the
Yu+2020 projection." The standalone-paper framing in the intro promises a
contribution to the parity-violation observable space. The body delivers a
careful null measurement. The discussion section fails to close the loop
on **what that null is informative about**.

This is the *single most-leveraged* item in this review. Closing
BLOCKER-T1 with a *qualitative-but-specific* falsification statement
(at order of magnitude, with appropriate transfer-function hedge) would
move the paper from "carefully-measured null that doesn't quite know what
it is" to "carefully-measured null that constrains the matter-bounce family
at the projection level by O(1) and is uninformative about ekpyrotic /
loop-quantum bounces by construction." That's a publishable contribution
to the field's parity-violation landscape; the current draft is one step
short of being able to claim it.

---

## Theory-axis readiness recommendation

| Axis | v1.0.49 current | After BLOCKER-T1 + T2 fixes | After all MAJOR fixes |
|------|-----------------|------------------------------|------------------------|
| Theory framing | 85% | 88% | 92% |
| Cross-paper coupling | 80% | 80% (unchanged) | 90% (with MAJOR-T1) |
| Literature currency | 78% | 78% (unchanged) | 86% (with MAJOR-T5) |
| Falsifiability | 82% | 86% | 90% (with MAJOR-T6) |
| **Theory-axis composite** | **85%** | **87%** | **92%** |

Note: the 99% cap (per Houston's standing directive
`feedback_99_pct_readiness_cap.md`) and the
oscillation-after-clean-R-round directive
(`feedback_readiness_oscillation.md`) both apply. Theory-axis readiness
should not exceed 95% until a clean cross-vendor R-round + Houston sign-off
on the §VIII.E rewrite.

---

## Summary table

| Severity | Count | Examples |
|----------|-------|----------|
| BLOCKER  | 2 | T1 (no falsified class), T2 (orthogonality overclaim) |
| MAJOR    | 6 | T1 (f_NL cross-paper), T2 (Wilson-Ewing class), T3 (window leakage), T4 (caveat ordering), T5 (2024–2026 lit), T6 (Popperian falsifiability) |
| MINOR    | 5 | T1 (ECH-drop correct), T2 (Yu+2020 cite), T3 (Eskilt vs ACT DR6), T4 (sub-percent claim), T5 (P1A clause) |
| NIT      | 3 | T1 (complementary), T2 (paragraph structure), T3 (transfer-function statement repetition) |
| **Total**| **16**| |

**Round verdict:** **NOT CLEAN** on the theory axis. 2 BLOCKERs + 6 MAJORs
incremental relative to v1.0.49. Recommend v1.0.50 to close BLOCKER-T1 and
BLOCKER-T2 minimum; MAJOR closures stage over v1.0.50–v1.0.51.
