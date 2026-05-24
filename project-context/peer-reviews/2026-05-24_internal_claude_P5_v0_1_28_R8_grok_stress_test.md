# P5 v0.1.28 — Grok-style Brutal-Honesty Stress Test (R8)

**Date:** 2026-05-24
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.28-2026-05-23
**Reviewer mode:** Adversarial — Grok-4.3 framing, DeepSeek statistical archaeology
**Context:** Paper passed 7 consecutive Anthropic-default internal reviews
(§4.4.1 3-consec clean). Job is to find what the cautious-default reviewers
missed.

---

## TL;DR

The paper is statistically honest, but the **headline framing slides between
two distinct claims** that an external referee will pick apart, and the
"five independent evidence lines" narrative double-counts. The §4.4.1-clean
status is not fundamentally shaken, but the abstract requires surgical
sharpening before external submission.

---

## FINDING 1 (MAJOR — framing slop) — "Environment-independent" vs. "we did not detect environment dependence at our sensitivity"

**Severity:** MAJOR
**Class:** Headline overclaim by way of underclaim (Grok angle)

The abstract opens with:
> "the CW fraction is statistically independent of cosmic-web class within
> DESI DR1 at V-Web resolution"

and the conclusion repeats:
> "Spiral galaxy chirality is statistically independent of large-scale
> structure environment within DESI Data Release 1 at V-Web resolution."

This is **not what the data show.** What the data show is:

1. The largest single class (cluster, n=397,505) deviates from parity at
   −4.66σ.
2. The second-largest (filament, n=408,187) deviates at −2.61σ.
3. The deviations track the P4 catalog-monopole prediction within
   "order unity" (the paper's own phrase, §IV.B), not exactly.
4. The smallest class (void, n=428) has a 95% CI [0.435, 0.530] — a 9.5pp
   window. This bin is **incapable** of detecting a 1–2pp environmental
   dependence even if one existed.

The honest framing is **"we find no environment dependence above the
sensitivity floor set by counting statistics and the P4 classifier
monopole."** That is a different scientific claim from
"chirality is environment-independent." The former is a measurement upper
bound; the latter is a positive structural statement that the data does
not support.

**Why 7 Anthropic reviewers missed it:** Claude defaults to accepting
"null = independence" framing because it is the cautious read. Grok-style
reads it as Houston quietly upgrading a non-detection into a positive
structural claim, which referees on PRD/MNRAS will flag.

**Fix (concrete, 1 sentence in abstract):**
> Replace "the CW fraction is statistically independent of cosmic-web
> class" → "the CW fraction shows no environment dependence at the
> sensitivity floor of $\sim$0.2 pp (V-Web filament/cluster, $n \gtrsim
> 4 \times 10^5$) and $\sim$5 pp (V-Web void, $n = 428$)."

This costs nothing scientifically and removes the only referee-bait line.

---

## FINDING 2 (MAJOR — double-counting evidence) — The "four catalog-anchored cross-checks" are not four independent constraints

**Severity:** MAJOR
**Class:** Statistical sleight-of-hand (DeepSeek angle)

The abstract bullets:
> "(i) re-running with DESIVAST-defined voids as the classifier ...
> (ii) three-algorithm DESIVAST robustness (VoidFinder + V2-REVOLVER +
> V2-VIDE) ... (iii) HEALPix sky-position stratification ... (iv) the
> per-pixel Pearson correlation"

The paper itself already concedes in the parenthetical that the per-galaxy
and HEALPix-stratified tests **reuse the same matched-spiral subsample by
design.** Translation: (i), (ii), (iii), (iv) are **all** computed on
exactly the same 678,945 z≤0.24 matched-spiral catalog, just sliced by
different DESIVAST-derived classifiers. The Pearson r=+0.006 (iv) is
**arithmetically downstream** of the HEALPix stratification (iii), which
is downstream of the catalog-anchored classifier (i). These are
**re-projections of one analysis**, not four independent tests.

The genuinely independent cross-classifier in the paper is the **Tempel
+2014 FoF cross-validation (§VII)**, which uses a different parent
catalog (SDSS DR10) and a different selection (richness, not tidal
tensor). That is the load-bearing independent check, and the paper
correctly singles it out internally as "the load-bearing cross-classifier
validation." But the abstract elevates the DESIVAST quartet — which are
correlated re-slices — to equal billing.

**Fix:** Demote (i)–(iv) in the abstract to "four DESIVAST-anchored
re-projections, all confirming the V-Web null on a $\sim$130× larger
void sample but methodologically correlated by construction"; promote
Tempel filament 0.026 pp concordance to a separate sentence as the
independent-classifier confirmation.

**Why 7 Anthropic reviewers missed it:** Each cross-check is internally
correctly framed in its own paragraph; the double-counting only emerges
when you tally them as "independent evidence lines." Claude tends to
count what the paper labels as independent; Grok counts the actual
covariance.

---

## FINDING 3 (MAJOR — selective reporting) — The bright-vs-dark sign-flip does NOT replicate on the cluster class; the paper buries this

**Severity:** MAJOR
**Class:** Framing slop disguised as sample-size honesty (Grok angle)

The abstract says:
> "the filament-class sign-flip alone is sufficient to establish that the
> catalog-level deviation is selection-function-conditioned rather than
> environment-driven."

This is the **single most contestable sentence in the paper.** The
filament class returns bright −2.80σ vs dark +2.85σ (opposite sign).
The cluster class returns joint |z|≈0.5σ on the bright-vs-dark
difference — i.e., the sign-flip does **not** replicate, and the paper
attributes this to the dark sample (n=4,234) being underpowered.

A skeptical referee will say: "You have two large V-Web classes (the
only two with n in the 4×10⁵ range). The bright-vs-dark sign-flip
replicates on **one** of them. The other one is null at counting
statistics. You are claiming a 'sign-flip recurrence across both the
cluster and filament classes (the two largest V-Web environments) is the
strongest sign that...' (§VI.E filament-class decomposition paragraph).
**The cluster class does not show the sign-flip recurrence.** It shows
'consistent with no recurrence at the sensitivity available.' Those are
different."

The cluster-class joint z=0.5σ is **honest at the level of the JSON
artifact** but **dishonest at the level of the abstract claim**, because
the abstract framing presents the systematic interpretation as
established by sign-flip recurrence across two classes, when in fact one
class shows it and the other is underpowered to test it.

**The brutal version:** the systematics-vs-environment interpretation
is **partially supported** — one of two large V-Web classes shows the
diagnostic sign-flip; the other has insufficient statistics to confirm
or refute. The honest framing is "the filament-class sign-flip is
consistent with a BGS-selection-function origin; the cluster-class joint
test lacks statistical power to confirm independently."

**Fix:** Replace the abstract's "the filament-class sign-flip alone is
sufficient to establish" → "the filament-class sign-flip is consistent
with a BGS-selection-function origin; the cluster-class joint test is
sample-size-limited ($n_{\rm dark}^{\rm cluster} = 4{,}234$) and does
not independently confirm or refute this interpretation."

**Why 7 Anthropic reviewers missed it:** Each said internally "the
cluster class is underpowered, that's fine." None checked whether the
abstract's positive claim survives the underpowered branch being
removed from the evidence pool.

---

## FINDING 4 (MINOR — numerical sleight of hand) — The −5σ catalog-level signal is alternately called "systematic" and "Paper IV monopole" without dimensional consistency

**Severity:** MINOR
**Class:** Statistical confabulation hazard (DeepSeek angle)

The paper uses three different numbers for the catalog-level monopole:
- Paper IV: $\sim$9.5σ catalog-level monopole.
- P5 envelope: −5.07σ on n=812,793 (matched-spiral env-labeled).
- P5 headline subsample: −5.00σ on n=791,635.

The paper correctly notes (§VI.F) that these are "sample-size-scaled
projections of the same underlying offset" — true, since $\sigma_{\rm
pred} = 2 |\Delta f_{\rm CW}| \sqrt{N}$ and $\sqrt{8.47 \times 10^6
/ 7.9 \times 10^5} \approx 3.27$, so 9.5σ / 3.27 ≈ 2.9σ ≠ 5.0σ.

This **doesn't quite check out** with the monopole-scaling claim.
$\sqrt{N_{P4}/N_{P5}} = \sqrt{8.47\times10^6/7.92\times10^5} \approx
3.27$, so a P4 9.5σ monopole at $\Delta f_{\rm CW} = -0.0026$ should
project to $9.5/3.27 \approx 2.9\sigma$ on the P5 sample, **not** 5σ.
The $-5\sigma$ is consistent with the P5 sample-matched $\Delta f_{\rm
CW} \approx -0.0028$, which is slightly larger than the P4 $-0.0026$
canonical.

This is either:
- (a) honest: the P5 matched-spiral subsample has a slightly larger
  monopole offset than the global P4 catalog, by chance or by selection.
- (b) framing slop: the paper invokes "the P4 monopole" as the
  explanation when the P5 subsample carries a slightly *different*
  monopole that just happens to be in the same direction.

Either way, the paper currently does not show the arithmetic that
reconciles 9.5σ (P4) with 5.0σ (P5) at sample-size-scaled projection.
The reader is supposed to take "scaled projection" on faith. A
DeepSeek-style reviewer will catch this.

**Fix:** Add one sentence reconciling: "The P4 catalog-level $9.5\sigma$
monopole at $\Delta f_{\rm CW}^{\rm P4} = -0.0026$ projects to
$\sigma_{\rm pred}^{\rm P5} = 2 \cdot 0.0026 \cdot \sqrt{791{,}635}
\approx 4.62\sigma$ on the P5 chirality-relevant subsample; the
observed P5 monopole of $-5.00\sigma$ corresponds to $\Delta f_{\rm
CW}^{\rm P5} = -0.0028$, $\sim$8% larger than the P4 catalog-mean,
consistent with the spectroscopically-confirmed subsample being more
strongly weighted to the BGS-bright leg that Paper IV identifies as
carrying the largest per-leg systematic."

---

## FINDING 5 (MINOR — bounce-discrimination overreach) — §VIII.B claim about bounce-vs-inflation discrimination

**Severity:** MINOR
**Class:** Conclusion not supported by null (Grok angle)

§VIII.B "Bounce vs. inflation discrimination":
> "The present null is consistent with both matter-bounce and inflation-
> class models: neither predicts an environment-dependent CW fraction at
> the resolution of DESI DR1 spectro spirals."

This is technically defensible **only because** the paper provides no
citation showing that any specific bounce model predicts environment-
dependent chirality at the sensitivity probed. The absence of such a
prediction means this null **cannot** discriminate. Calling it a "clean
negative result on the spiral-chirality axis" of the bounce-vs-inflation
program is borderline — a null result that no model predicts a signal
for is not a discriminating axis; it's an irrelevant axis.

The honest framing: "This null does not currently discriminate between
bounce and inflation models because no published model in either class
predicts an environment-dependent CW signature at DESI DR1 sensitivity;
the null establishes an observational upper bound that any future
parity-violating model must respect."

**Why 7 Anthropic reviewers missed it:** Claude tends to accept
"consistent with both" as a valid framing for nulls in
discrimination programs. Grok says: a null in a non-predicting
parameter is not "consistent with both models" — it is "uninformative
about both models."

---

## Brutal-honesty summary table

| # | Class | Severity | Catch | One-line fix |
|---|-------|----------|-------|--------------|
| 1 | Headline overclaim | MAJOR | "Environment-independent" reads as positive structural claim; actually a sensitivity-limited upper bound | Add sensitivity-floor caveat to abstract |
| 2 | Double-counting | MAJOR | (i)–(iv) abstract bullets are correlated re-slices, not 4 independent tests | Demote in abstract, promote Tempel to standalone independent check |
| 3 | Selective reporting | MAJOR | Bright-vs-dark sign-flip replicates on filament but NOT cluster; paper buries the cluster underpowering | Reframe: "filament-class sign-flip consistent with selection origin; cluster-class lacks power" |
| 4 | Numerical reconciliation | MINOR | P4 9.5σ → P5 5σ arithmetic not shown | Add 2-line reconciliation paragraph |
| 5 | Bounce discrimination overreach | MINOR | Null in non-predicting parameter ≠ "consistent with both models" | Reframe as upper bound for future models |

---

## Does this shake the §4.4.1-clean status?

**No, not fundamentally.** Findings 4 and 5 are sentence-level fixes.
Finding 2 is a one-paragraph reordering. Findings 1 and 3 are
**abstract-only edits** — change one sentence each, no science changes.
The underlying analysis is solid; the artifacts back every numerical
claim; the cross-classifier (Tempel) genuinely confirms the V-Web run
at the load-bearing high-n class. What is broken is the **framing**
between body (honest) and abstract (oversold-by-cautious-default-framing).

**Single sharpest critique (Finding 3):** the systematics-not-environment
interpretation is supported on **one** of two large V-Web classes; the
cluster-class joint z=0.5σ test is underpowered, not confirmatory. The
abstract presents the interpretation as established by sign-flip
recurrence across both classes; the data establish it on filament only.

**Recommendation:** R9 cron should ingest findings 1, 2, 3 as
abstract-rewrites and findings 4, 5 as inline §IV/§VIII rewrites;
re-compile; declare R8 closed with abstract surgery, not with substantive
re-analysis.
