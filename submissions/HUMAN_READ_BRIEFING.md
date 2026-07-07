# HUMAN-READ BRIEFING — pre-submission expert read

**For:** Houston Golden · **Date:** 2026-07-07 · **Status:** pre-flight, honest

This is the document that makes your irreducible expert-read step efficient. It
directs your attention to exactly what only a human author can judge — the
judgment calls, the framing choices, and the claims you will personally sign.
It does **not** soften anything. The automated pipeline cleared all six papers
(0 genuinely-new category-d findings on the FINAL + POSTPOLISH truth-audits;
`FINAL_SIGNOFF_AUDIT_2026-07-05.md`), but "cleared by the pipeline" is not the
same as "an expert stands behind it." The gap between those two is your job.

**Read deeply: P4 + P2 (minimum). Skim: P1A, P3, P5, P1B.**

**The single most consequential judgment in the whole program is the P2 Cai
arithmetic-error claim.** Read that section first.

---

## The whole program in 6 lines

| Paper | v | pp | One-line claim | Load-bearing result | Pipeline verdict |
|-------|---|----|----------------|---------------------|------------------|
| **P4** | 1.0.220 | 31 | Chirality dipole in 8.5M DESI galaxies is **null** | Real-space HC dipole +0.41σ, p=0.31 | Grok+Gemini MINOR / grok-API ACCEPT; ChatGPT REJECT (floor) |
| **P2** | 1.7.98 | 34 | Matter-bounce f_NL=**−35/16**; resolves Cai/Li factor-of-2; recasts SPHEREx | The −35/16 resolution + ~1.3–2.75σ conditional envelope | Grok+Gemini MINOR; ChatGPT+openai REJECT (floor) |
| P3 | 3.1.140 | 33 | 268,519-source multi-survey anomaly catalog | The catalog + reproducible dedup | grok-API MINOR; ChatGPT+Gemini REJECT/MAJOR |
| P5 | 0.1.104 | 37 | DESI void/non-void chirality is null (Δf_CW≈0) | Δf_CW=+0.0007±0.0022, monopole-invariant | Grok+Gemini MINOR (companion to P4) |
| P1A | 1A.0.112 | 37 | Channel-level no-go: spin-torsion can't be the DE route | The scoped channel-by-channel closure | Grok pub-ready; ChatGPT+Gemini+openai REJECT/MAJOR |
| P1B | 1B.0.102 | 22 | ECH reproducibility companion + derived ΔN_eff bound | ΔN_eff~1e-43 (negligible) | Grok "ready for arXiv"; ChatGPT+Gemini REJECT (venue) |

**The universal pattern you must internalize before reading a single review:**
across every paper, on the *identical PDF*, Grok/grok-API rate MINOR-or-ACCEPT
while ChatGPT/openai-gpt-5.5 REJECT. This is directive-H referee variance (the
maximally-harsh LLM referee's structural floor — it flags majors on any real
manuscript, including published PRD papers). A ChatGPT REJECT is **not** evidence
of an error; it is the noise floor. Treat the ChatGPT/openai REJECT lists as a
**preview of the toughest human referee's *scope* questions**, already answered
in the artifact record — not as a bug list.

---

# P4 — Null chirality dipole in 8.5M DESI galaxies (READ DEEPLY)

### The 5-minute version
- **Claim:** The large-scale chirality dipole of spiral galaxies is consistent
  with null. This is a null-result paper riding on the largest chirality-labeled
  galaxy catalog to date (8,474,531 DESI Legacy DR8 galaxies, flip-equivariant
  ViT, released public with weights).
- **The single load-bearing result:** the primary real-space dipole fit on the
  high-confidence sample (N≈9.5×10⁵, p_eq>0.6) gives **+0.41σ, empirical-rank
  p=0.31** against an isotropic pixel-permutation null. That is the null. Plus a
  block-bootstrap WLS fit disfavoring a clean cosmological dipole at Shamir's
  1.7% reference amplitude at z≈−18.
- **What a hostile expert attacks first:** *"Your null only appears after a
  p_eq>0.6 confidence cut that discards ~70% of the sample; the discarded
  low-confidence tail shows a z≈4.0–4.3 excess you attribute to systematics but
  never prove is excludable. You are cutting to the answer you want."* This is
  ChatGPT M1/M2 and it is the one attack that matters.

### Read these pages carefully
1. **Abstract + Sec. prereg + Sec. dipole (the p_eq>0.6 cut).** The defense is
   that the cut is **pre-specified** (commit 94113e5 cited, not tuned post-hoc)
   and the null is **robust across the full sweep** p_eq∈{0.6,0.7,0.8}. The sweep
   IS the robustness demonstration. **Your call: is "pre-specified + robust across
   the sweep" a defense you'll make with a straight face to a referee who
   suspects the cut was chosen after seeing the data?** The commit hash is the
   whole ballgame here — if you can't personally vouch that 94113e5 predates the
   analysis, this claim is exposed.
2. **The residual / harmonic-channel treatment (abstract ¶3, Appendix D).** This
   is the "residual framing" the audit flags. You explicitly say the MASTER
   pseudo-C_ℓ channel is **a systematics diagnostic, not an independent
   cosmological null**: a monopole-only null reproduces **99.32%** of the raw
   ℓ=1 power (monopole–mask leakage), and the surviving residuals (+3.64σ
   canonical, +7.28σ apodized) are **attributed to systematics via an
   eight-anchor battery**, not claimed as detections. This is the honest but
   fragile part: you are reporting +3.64σ / +7.28σ numbers and then telling the
   reader not to read them as detections. A skeptical referee will ask why they
   are in the paper at all if they are pure systematics.
3. **The ℓ=1 forward model (Gemini's ~47% residual, the named audit item).**
   The imaging forward model explains only ~52–54% of the ℓ=1 residual; ~47% is
   **explicitly an open item**, bounded below the falsification threshold
   (A_p=0.695% < A_50=0.75% ≪ A_95∈(1.0%,1.5%]) and flagged as a deferred
   GPU/pod computation. Gemini calls it MAJOR; Grok calls it a MINOR open item;
   grok-API returns ACCEPT. Disclosed with a hard bound — but it *is* an
   admitted 47% you-don't-model.
4. **Falsification criterion (end of abstract) — stand behind this personally.**
   You commit to: a future real-space ≥5σ dipole with A≳A_95 would be in tension
   with this null. Make sure you'd defend those thresholds.
5. **AI-methods disclosure (L1306).** Verbatim: *"This work was conducted using
   an agentic AI pipeline … operated under the author's direction. Every
   quantitative result … was verified against committed computational artifacts …
   The author designed the study, made all scientific judgments, and takes full
   responsibility … the AI pipeline is a reproducibility and verification
   instrument, not an author."* **Read this sentence as the thing your name is
   attached to.** It is honest and well-scoped. Confirm you're comfortable that
   "the author made all scientific judgments" is *true* for the residual/anchor
   attribution and the p_eq cut choice — those are the judgments, and this
   sentence asserts you made them.

### Known accepted risks (won't surprise you if a referee raises them)
- ChatGPT's 16-MAJOR REJECT = the structural floor. Every item maps to disclosed
  scope. Grok AND Gemini both return MINOR on the identical PDF; grok-API ACCEPT.
- The p_eq>0.6 / ~70%-discard framing will come back from a human referee. It is
  disclosed, but disclosure ≠ everyone agreeing it's the right cut.
- Shamir comparison is a *reference-amplitude* comparison, not a matched-footprint
  Ganalyzer reanalysis. Disclosed as such.
- No frozen Zenodo DOI yet (mints at submission — standard).

### THE ONE QUESTION only you can answer
> **Is the residual framing — reporting +3.64σ/+7.28σ harmonic residuals and the
> ~47% unmodelled ℓ=1 forward-model remainder, then attributing both to
> systematics rather than signal — something I will personally defend under my
> name, and do I personally vouch that the p_eq>0.6 cut (commit 94113e5) was
> pre-specified?**

---

# P2 — Matter-bounce f_NL, the Cai/Li resolution, SPHEREx recast (READ DEEPLY)

**This paper contains the single highest-stakes claim in the program: that a
published paper (Cai et al. 2009, arXiv:0903.0631, ~cited) contains an arithmetic
error. Everything else in P2 is a conditional forecast; this is an assertion about
another group's algebra, in print, under your name.**

### The 5-minute version
- **Claim (headline, restructured to lead with it):** the matter-bounce local
  non-Gaussianity is **f_NL=−35/16=−2.1875**, and P2's *central contribution* is
  to **resolve** the 8-year Cai(−35/8)-vs-Li(−35/16) factor-of-2 discrepancy in
  favor of −35/16, by re-summing Cai's own four cubic-action vertices at ε=3/2
  and tracing the published −35/8 to a spurious +(99/128)Σkᵢ³ term in Cai's final
  polynomial (their Eq. 37). Secondary: recast SPHEREx/MegaMapper sensitivity onto
  this prediction → conditional ~1.3–2.75σ envelope + Bayes factors ~9–14.
- **The single load-bearing result:** the −35/16 resolution. It **halves** the
  headline amplitude vs the erroneous −35/8 and it is the paper's claim to
  originality. If the arithmetic-error claim is wrong, the paper's central
  contribution collapses and you've publicly accused a group (Cai is a coauthor on
  *both* the 2009 and the correcting-2017 papers) of an error they didn't make.
- **What a hostile expert attacks first:** two fronts. (1) The forecast:
  *"every σ is a rescale of a single external Heinrich σ=0.7 with an
  additive-quadrature systematic budget — this is not an independent Fisher
  forecast; the ~1.3σ floor is vulnerable."* (2) **The dangerous one:**
  *"your factor-of-2 'resolution' is internally inconsistent — the +(99/128)Σk³
  term alone has the wrong sign/magnitude to explain −35/16→−35/8."* ChatGPT +
  openai independently RE-RAISE the factor-of-2 at every round.

### The Cai arithmetic-error claim — the evidence base, read it yourself
- **What the paper asserts (abstract + Appendix A, verbatim):** the −35/8 "traces
  to a single spurious +(99/128)Σᵢkᵢ³ local-shaped term that entered when Cai et
  al. collapsed their (correct) ε-order-grouped expressions into a final
  polynomial (their Eq. 37) — **an arithmetic error, not a convention
  difference.**"
- **The supporting computation** (`project-context/peer-reviews/INT_v3/P2_factor2_RESOLUTION_2026-07-04.md`):
  pulled the arXiv **LaTeX source** of both papers, re-summed Cai's four
  per-vertex in-in shape contributions symbolically (sympy, exact fractions),
  squeezed limit → clean −35/16. Three cross-checks: (i) Cai's own ε-order-grouped
  intermediates sum to −35/16 exactly; (ii) Li's independent general-c_s formula
  gives −35/16 at c_s=1; (iii) only Cai's *final printed polynomial* gives −35/8,
  and it differs from the vertex sum by exactly +(99/128)Σk³.
- **HONEST FLAGS you must weigh — do not skip these:**
  1. **The history is not clean.** This claim went through THREE states in four
     days: v1.7.86 (2026-07-03) declared the factor-of-2 **"a GENUINE UNRESOLVED
     literature discrepancy"** and *retracted a previous false single-time-ordering
     mechanism*; an in-in re-derivation the same day (`P2_inin_rederivation_2026-07-04.md`)
     even concluded it was **"GENUINELY UNRESOLVABLE from the published
     polynomials."** Then v1.7.89 (2026-07-04) flipped to **RESOLVED in favor of
     −35/16** on the strength of the vertex re-summation. The claim you're about to
     publish is 3 days old and reversed a "genuinely unresolvable" verdict. That
     doesn't make it wrong — the vertex-level computation is genuinely stronger
     than working backward from the mis-extracted polynomial — but **you are the
     only one who can judge whether the physics is now actually settled or whether
     the loop talked itself into a resolution.**
  2. **The decisive sympy scripts are in `/tmp/caili/` — ephemeral, NOT committed
     to the repo.** For a claim this consequential (public accusation of a
     published arithmetic error), the reproducing scripts should be committed
     artifacts. Right now the audit trail for the single most aggressive claim in
     the program points at a tmp directory. **Fix before submission if you assert
     this.**
  3. The pre-submission scripts must be re-run by *you* or an independent tool at
     least once — the from-scratch re-summation is the one place the "AI pipeline
     is a verification instrument" disclosure is doing the most work.

### Read these pages carefully
1. **Abstract ¶1 + Appendix A (the −35/16 resolution).** The most-disputed and
   highest-stakes content. Verify the +(99/128)Σk³ trace and the vertex table are
   ones you'd sign. Note the paper is careful: it says −35/8 comes from Cai's *own
   full printed-polynomial squeezed reduction* and the spurious term is *one
   identified discrepancy* — the v1.7.95 changelog explicitly reconciled an earlier
   over-strong "naive additive shift" phrasing (adding +(99/128)Σk³ alone gives the
   *wrong* sign, +2.58). Make sure the abstract/App-A wording matches the honest
   body framing and doesn't over-claim the mechanism.
2. **Abstract ¶2 "Scope." + the load-bearing caveat (★).** The forecast is a
   *sensitivity recast of a single external Heinrich forecast*, not an independent
   one — stated up front. The ★ caveat: the whole forecast is conditional on
   assumption (d), cubic bispectrum transmission through the bounce, now **derived
   to a bounded systematic** (1±O((kη)²)≈1±1e-4) via single-clock d.o.f.-counting +
   nonlinear superhorizon ζ-conservation. **Your call: is that derivation solid, or
   is it the weakest technical link a referee will push on?** Grok calls this "one
   of the strongest technical sections"; ChatGPT calls it not-demonstrated.
3. **Bayes factors (Table tab:bayes).** BF≈9–14. Note the audit *falsified* a
   ChatGPT claim that the paper quotes "BF≈10⁸/>10⁵" — it does not; the "10⁵" is a
   Monte-Carlo realization count. But you present BFs; confirm the "illustrative,
   not definitive model-selection evidence" framing (signpost vi) is prominent.
4. **AI-methods disclosure (L1380).** Verbatim, and it **specifically names the
   Cai–Li resolution** as AI-reached: *"the Cai–Li factor-of-two resolution
   (Appendix A) was reached by a from-scratch symbolic re-summation cross-checked
   three independent ways and against the original arXiv sources."* This is the
   correct, honest disclosure — but it means the paper openly tells referees that
   its central original contribution was produced by the AI pipeline. **You must
   personally endorse the resolution as if you derived it, because the disclosure
   makes clear a human didn't hand-derive it first.**

### Known accepted risks
- ChatGPT + openai REJECT; Grok + Gemini MINOR ("ready after modest tightening").
- **The factor-of-2 is logged as the sole substantive technical residue,
  Houston-gated → human referee.** ChatGPT/openai re-raise it every round. It is
  NOT dispositioned as "resolved and everyone agrees"; it is dispositioned as
  "resolved by our computation, re-corroborated as disputed by the harsh referees,
  handoff to a human expert." That is an honest but *live* disagreement.
- The forecast's ~1.3σ realistic floor is a conditional envelope under an
  additive-quadrature heuristic, explicitly *not* a joint-covariance forecast.
- **STALE ARTIFACT (fix before submitting):** `submissions/P2/REFEREE_EMAIL.md`
  still describes f_NL=**−35/8**, the old "2.6–5.5σ" envelope, and the factor-of-2
  as **unresolved** with a non-convergent Path-Z attempt. It predates the −35/16
  resolution and directly contradicts the final paper. Do not send it as-is.

### THE ONE QUESTION only you can answer
> **Am I comfortable publicly asserting, in print and under my name, that Cai et
> al. 2009 contains an arithmetic error (a spurious +(99/128)Σkᵢ³ term in their
> Eq. 37) — given that (a) this claim reversed a "genuinely unresolvable" verdict
> from 3 days earlier, (b) the resolution was AI-derived and disclosed as such,
> and (c) the decisive sympy scripts are currently uncommitted in /tmp?** If yes:
> commit the scripts and re-run them yourself first. If not-yet: the honest
> fallback is the pre-v1.7.89 framing (adopt −35/16 as the value, disclose the
> factor-of-2 as an outstanding literature discrepancy) — which is weaker but
> unimpeachable.

---

# P3 — Multi-survey anomaly catalog (SKIM)

- **Claim / load-bearing:** a 268,519-validated-source multi-survey autoencoder
  anomaly catalog from 37.3M spectra + map patches; the count is
  directly recomputable (`reproduce_headline_dedup.py`). Cosmology sections are
  presented as **methodological demonstrations yielding nulls**, not detections.
- **First attack:** *"this is an ML catalog for ApJS/MNRAS, not PRD
  fundamental-physics; the cosmology sections are non-detections."* Venue-fit,
  not correctness. grok-API returns MINOR "central claim supported" on the exact
  PDF ChatGPT+openai REJECT — the round's sharpest variance.
- **Read carefully:** the strata disclosure (§III D) and the two concrete numeric
  flags the audit verified are NON-issues: **NEOWISE 436 vs 419** (raw top-1% vs
  ecliptic-pole-masked, footnote "436→419, 96.1% retained") and **LAMOST 98%
  blue-excess** (labeled a transparent FAIL, excluded from the validated subset).
  Both are documented, not contradictions.
- **The one question:** **PRD or ApJS/AJ?** Both Gemini and the audit recommend a
  catalog/data-release venue. This is a venue routing call, not a science call.

---

# P5 — DESI environmental chirality null (SKIM — companion to P4)

- **Claim / load-bearing:** void/non-void chirality difference is null,
  **Δf_CW=+0.0007±0.0022**, and the headline is **algebraically
  monopole-shift-invariant** so it rests only on P4's *public* labels + public
  DESI/DESIVAST data — refereeable independently of P4's internals.
- **First attack:** *"depends on unpublished companion Paper IV; DESIVAST 'primary'
  path was designated post-hoc (forking paths)."* The Paper-IV dependency is a
  documented coordinated submission (P4 posts first, its ID swaps in). The post-hoc
  designation is explicitly acknowledged with Bonferroni-5 treatment.
- **Read carefully:** the §IX A T-Web robustness self-audit (the author's *own*
  finding that unweighted T-Web collapses void fraction ×23 — disclosed, and T-Web
  relegated to secondary; DESIVAST primary is deliberately insensitive to it).
- **The one question:** **Am I comfortable that "DESIVAST primary designated
  post-hoc, disclosed with Bonferroni treatment" survives a forking-paths referee,
  and that shipping P5 as a P4-coordinated companion (not standalone) is the right
  call?**

---

# P1A — ECH spin-torsion no-go (SKIM)

- **Claim / load-bearing:** a **channel-level** (not full operator-basis) no-go
  that spin-torsion can't be the dark-energy route, closed channel-by-channel at
  M_Pl power-counting, with the Fierz-by-Fierz lemma named as **the single open
  item**.
- **First attack:** *"you call it a no-go 'theorem' but it's channel-level with an
  open Fierz lemma and NDA/dimensional-analysis estimates, not an operator-level
  proof."* Grok calls the identical content "mature, publication-ready"; ChatGPT
  calls it REJECT. The scope (channel-level, one open lemma) is disclosed.
- **The one question:** **Am I comfortable calling this a "no-go" with the scope
  explicitly channel-level and one lemma open — expecting (and being fine with) a
  real scope exchange with a human referee at JCAP/PRD?** The audit predicts "a
  real scope exchange — normal refereeing." Note: the POSTPOLISH round found and
  **fixed** a real item here — `fig_theory_map.png` had a baked-in −35/8 (now
  −35/16, v1A.0.112). Confirm no other figure carries a stale value.

---

# P1B — ECH reproducibility companion (SKIM)

- **Claim / load-bearing:** a reproducibility companion to P1A; the one original
  contribution is a **derived ΔN_eff~1e-43 bound** (negligible, i.e. ECH doesn't
  spoil BBN/CMB). Grok: "the standout original contribution … Ready for arXiv."
- **First attack:** *"companion/reproducibility manifest, lacks standalone PRD
  novelty; ΔN_eff untestable."* This is a **venue/scope** objection, not a factual
  error — and it's precisely the objection that a *companion* framing answers.
  Both harsh reviewers concede the numerics are supported.
- **THE ONE QUESTION (structural):** **Standalone, or fold into P1A?** The audit,
  the CAMPAIGN_STATUS, and the reviewers all circle this. Options: (a) post as a
  coordinated companion (current plan, `SUBMISSION_NOTE.md` — P1B first-wave, IDs
  swap reciprocally with P1A); (b) merge the ΔN_eff derivation + reproducibility
  material into P1A as appendices and drop P1B; (c) route to a methods venue. The
  reviewers' standalone-novelty REJECT is answered by (a) or (b), *not* by
  shipping P1B as a standalone PRD physics paper. This is a pure structure call
  only you can make.

---

# CROSS-CUTTING (1 page)

### 1. The AI-involvement disclosure — what it says, why
Both P4 (L1306) and P2 (L1380) carry an explicit, near-identical **"AI-assisted
methodology"** paragraph in-body (all six papers do). It states: an agentic
multi-model AI pipeline did literature review, code, computation, and *adversarial
internal peer review* under the author's direction; every result is verified
against committed artifacts with a public audit trail; **the author designed the
study, made all scientific judgments, and takes full responsibility; the AI is a
reproducibility/verification instrument, not an author.** P2 goes further and names
the Cai–Li resolution as AI-reached.

**Why it's worded this way:** it is honest (the pipeline genuinely did the work),
it pre-empts the "did an LLM write this?" question by answering it plainly, and it
draws the responsibility line where it belongs — on you. **The exposure:** the
disclosure is a magnet. Some referees/community members will treat "AI-derived
central result" (P2's Cai claim especially) as a reason for extra scrutiny. That is
*correct* scrutiny and the disclosure invites it. Your job is to ensure that for
every claim the disclosure covers, "the author made the scientific judgment" is
*actually true* — i.e. you personally endorse it, not just approved a summary.

### 2. The Cai email decision
You are about to publish that Cai et al. 2009 contains an arithmetic error, with
Cai a coauthor on the correcting 2017 paper. **Options, hardest-first:**
- **(A — recommended) Email Cai (and Li/Quintin) before or at submission.** Send
  the from-scratch vertex re-summation and the +(99/128)Σk³ trace; ask them to
  confirm or refute. Upside: if they confirm, your central claim is bulletproof and
  you have the original authors on record; if they refute, you learn it *before*
  publishing an accusation. This is the collegial and scientifically safest path,
  and it directly de-risks the single highest-stakes claim in the program.
- (B) Post to arXiv first, notify Cai simultaneously. Faster, less safe.
- (C) Publish without contacting them. Lowest effort, highest reputational risk —
  do not do this for an arithmetic-error accusation.
The decision is yours, but the asymmetry strongly favors (A): the cost is one
email; the downside of skipping it is a public error-accusation that the original
author could rebut after the fact.

### 3. Expected community reception + how to answer the first critical email
- **Most likely first critical email** will be one of two: (i) *"Your P4/P5 nulls
  only appear after confidence cuts / post-hoc path choices — this is
  garden-of-forking-paths."* Answer: point to the pre-registered cut (commit hash),
  the full robustness sweep, the Bonferroni family treatment, and the fact that the
  monopole-invariant headline doesn't depend on the disputed choices. (ii) *"Your
  P2 Cai-error claim is wrong / the +(99/128) term doesn't work the way you say."*
  Answer: the committed sympy re-summation of Cai's own vertices + the two
  independent cross-checks (Cai's own ε-grouped intermediates, Li's general-c_s
  formula). **This is why committing the scripts and emailing Cai first matters —
  both make this email a 10-minute reply instead of a crisis.**
- **On the ChatGPT/openai REJECTs:** do not be rattled if a human referee's first
  pass reads like ChatGPT's. The whole point of directive-H is that a maximally
  harsh referee flags majors on *any* real paper. Every such item is already
  dispositioned in `FINAL_SIGNOFF_AUDIT_2026-07-05.md` with a source citation.
  Keep that file open when the first tough review lands.

### 4. Before you click submit — the honest pre-flight residue
1. **P2:** commit the `/tmp/caili/` sympy scripts; re-run them yourself; reconcile
   the stale `REFEREE_EMAIL.md`; decide the Cai email.
2. **P4:** personally vouch that commit 94113e5 (the p_eq cut) is genuinely
   pre-analysis.
3. **P1B:** decide standalone vs fold-into-P1A.
4. Submission order (dependencies): **P4 first** → P5 (needs P4's ID) and P1A/P1B
   (reciprocal IDs). Zenodo DOIs mint at submission.

---

## Per-paper one-questions (the yes/no only you can answer)

- **P4:** Is the residual framing (+3.64σ/+7.28σ systematics-attributed, ~47%
  unmodelled ℓ=1) something I'll defend under my name, and do I vouch the p_eq>0.6
  cut was pre-specified?
- **P2:** Am I comfortable publicly asserting Cai 2009 contains an arithmetic
  error, given the 3-day-old reversal, the AI-derived provenance, and the
  uncommitted scripts?
- **P3:** PRD, or ApJS/AJ (catalog venue)?
- **P5:** Does "DESIVAST-primary designated post-hoc, disclosed + Bonferroni"
  survive a forking-paths referee, and is P4-companion (not standalone) right?
- **P1A:** Am I comfortable calling this a channel-level "no-go" with one lemma
  open, expecting a real scope exchange?
- **P1B:** Standalone companion, or fold into P1A?
